"""Download pinned source snapshots. No flashing, extraction, or execution.

Run from any directory with Python 3. Archives remain outside Git history.
Existing files are accepted only when their SHA256 matches the published list.
"""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import shutil
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def fetch(item):
    target = ROOT / 'archives' / item['archive_name']
    expected = item.get('sha256')
    if target.exists():
        if not expected or digest(target) != expected:
            raise RuntimeError(f'Existing file has no matching trusted checksum: {target.name}')
        return target.name, 'already verified'
    target.parent.mkdir(exist_ok=True)
    partial = target.with_suffix(target.suffix + '.partial')
    req = urllib.request.Request(item['archive_url'], headers={'User-Agent': 'Arch-ARM-Resource-Catalog/1.0'})
    with urllib.request.urlopen(req, timeout=120) as response, partial.open('wb') as out:
        shutil.copyfileobj(response, out, length=1024 * 1024)
    actual = digest(partial)
    if expected and actual != expected:
        raise RuntimeError(f'Checksum mismatch: {target.name}. Partial file retained for inspection.')
    # Read the entire archive to detect truncation, without extracting it.
    count = 0
    if item.get('is_archive', True):
        with tarfile.open(partial, 'r:*') as archive:
            for member in archive:
                if member.isfile():
                    f = archive.extractfile(member)
                    while f.read(1024 * 1024):
                        pass
                count += 1
    partial.replace(target)
    return target.name, f'{actual} ({count} entries)'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=3, choices=range(1, 5))
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'sources.json').read_text(encoding='utf-8'))
    items = [x for x in catalog['repositories'] if x.get('download_archive')]
    kernel_path = ROOT / 'kernel-source.json'
    if kernel_path.exists():
        kernel = json.loads(kernel_path.read_text(encoding='utf-8'))
        items += [dict(repo='Upstream LTS kernel', archive_name=kernel['archive_name'],
                       archive_url=kernel['source_url'], sha256=kernel['sha256']),
                  dict(repo='Upstream LTS signature', archive_name=kernel['signature_name'],
                       archive_url=kernel['signature_url'], sha256=kernel['signature_sha256'], is_archive=False)]
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch, x): x for x in items}
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]['repo']
            try:
                print(*future.result(), flush=True)
            except Exception as exc:
                failures.append(name)
                print(f'FAILED {name}: {exc}', flush=True)
    raise SystemExit(1 if failures else 0)
