"""Record downloaded source hashes and package the collection for a GitHub release."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def license_evidence(path):
    evidence = []
    with tarfile.open(path, 'r:gz') as archive:
        for member in archive:
            if not member.isfile() or member.size > 200000:
                continue
            name = PurePosixPath(member.name).name.lower()
            if name in ('copying', 'license', 'license.txt', 'notice') or name.startswith('license.'):
                evidence.append(member.name)
            elif member.name.endswith(('.c','.h','.cpp','.mk')) and len(evidence) < 6:
                text = archive.extractfile(member).read(5000).decode(errors='replace')
                marker = re.search(r'SPDX-License-Identifier:\s*([^\r\n*]+)', text)
                if marker:
                    evidence.append(member.name + ': SPDX ' + marker.group(1).strip())
                elif 'GNU General Public License' in text:
                    evidence.append(member.name + ': GPL notice in source header')
                elif 'Permission to use, copy, modify, and/or distribute' in text:
                    evidence.append(member.name + ': permissive notice in source header')
                elif 'Redistribution and use in source and binary forms' in text:
                    evidence.append(member.name + ': BSD style notice in source header')
    if not evidence:
        raise RuntimeError('No license evidence found. Do not publish: ' + path.name)
    return evidence[:10]


if __name__ == '__main__':
    catalog = json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
    kernel = json.loads((ROOT/'kernel-source.json').read_text(encoding='utf-8'))
    if not kernel['signature_validated']:
        raise RuntimeError('Upstream kernel signature must be verified before packaging')
    for item in catalog['repositories']:
        if not item['download_archive']:
            continue
        path = ROOT/'archives'/item['archive_name']
        item.update(sha256=sha(path), bytes=path.stat().st_size,
                    license_evidence=license_evidence(path),
                    redistribution_review='Upstream notices/source license headers retained. Per file terms apply.')
    (ROOT/'sources.json').write_text(json.dumps(catalog, indent=2)+'\n', encoding='utf-8')
    # Include the GPL text separately as well as its copy in the kernel source.
    old = next(x for x in catalog['repositories'] if x['repo']=='Samsung-QTI/android_kernel_msm-5.4')
    licenses = ROOT/'LICENSES'
    licenses.mkdir(exist_ok=True)
    with tarfile.open(ROOT/'archives'/old['archive_name'], 'r:gz') as archive:
        wanted = next(x for x in archive.getmembers() if x.name.endswith('/LICENSES/preferred/GPL-2.0'))
        (licenses/'GPL-2.0.txt').write_bytes(archive.extractfile(wanted).read())
    lines = ['# Resource catalog', '', 'Collected 24 October 2026. Source availability is not tablet compatibility.', '',
             '## Arch ARM, kernel and development documentation', '', '| Resource | Purpose |', '| --- | --- |']
    for x in catalog['resources']:
        lines.append(f"| [{x['title']}]({x['url']}) | {x['purpose']} |")
    lines += ['', '## Source snapshots', '', 'The release ZIP contains the rows marked Included. Others are references only. No build or tablet test has been performed.', '',
              '| Repository | Purpose | Snapshot | In ZIP |', '| --- | --- | --- | --- |']
    for x in catalog['repositories']:
        lines.append(f"| [{x['repo']}]({x['url']}) | {x['purpose']} | [{x['commit'][:12]}]({x['url']}/tree/{x['commit']}) | {'Included' if x['download_archive'] else 'Link only'} |")
    lines += ['', '## Maintained upstream kernel source', '',
              f"Linux **{kernel['version']}**, [official source]({kernel['source_url']}) and [signature]({kernel['signature_url']}). Included in the ZIP. Its signature was verified using the key fingerprint published by kernel.org. See [verification output](KERNEL-SIGNATURE.txt). This is general kernel source, not a tablet ready image.", '',
              '## Unresolved manifest references', '', 'These projects were referenced in the community manifests but could not be accessed publicly during collection:', '']
    lines += ['* `' + x['repo'] + '`' for x in catalog['unavailable_references']]
    lines += ['', 'No replacement for those missing projects is implied by the generic upstream kernel. The community build needs its own matching sources and dependencies.', '',
              '## License records', '', 'Detected GitHub licenses and source notice locations are recorded in [sources.json](../sources.json). The presence of a license header in one file does not relicense the whole repository. Consult each file before reusing it. Archive paths and original notices are preserved.', '']
    (ROOT/'docs'/'RESOURCE-CATALOG.md').write_text('\n'.join(lines), encoding='utf-8')
    archive_paths = [ROOT/'archives'/x['archive_name'] for x in catalog['repositories'] if x['download_archive']]
    archive_paths += [ROOT/'archives'/kernel['archive_name'], ROOT/'archives'/kernel['signature_name']]
    if sha(archive_paths[-2]) != kernel['sha256'] or sha(archive_paths[-1]) != kernel['signature_sha256']:
        raise RuntimeError('Kernel files changed after signature verification')
    sums = ''.join(f'{sha(p)}  archives/{p.name}\n' for p in sorted(archive_paths))
    (ROOT/'SHA256SUMS').write_text(sums, encoding='ascii')
    release = ROOT/'release'
    release.mkdir(exist_ok=True)
    target = release/'Arch-ARM-Tablet-Resources-v0.1.0.zip'
    if target.exists():
        raise RuntimeError('Refusing to overwrite an existing release ZIP')
    included = [p for p in ROOT.rglob('*') if p.is_file() and not set(p.relative_to(ROOT).parts) & {'.git','.gnupg','release','archives','__pycache__'}]
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as out:
        for p in included:
            out.write(p, 'Arch-ARM-Tablet-Resources/' + p.relative_to(ROOT).as_posix())
        for p in archive_paths:
            out.write(p, 'Arch-ARM-Tablet-Resources/archives/' + p.name, compress_type=zipfile.ZIP_STORED)
    (release/'SHA256SUMS.txt').write_text(sha(target) + '  ' + target.name + '\n', encoding='ascii')
    print(f'Packaged {len(archive_paths)} source/signature files. ZIP {target.stat().st_size/1024/1024:.1f} MiB. SHA256 {sha(target)}')
