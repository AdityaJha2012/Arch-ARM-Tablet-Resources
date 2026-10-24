"""Fetch one maintained upstream LTS source and verify its detached signature.

The result is general kernel source, not a tablet kernel image.
"""
import hashlib
import json
import lzma
from pathlib import Path
import shutil
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'archives'
GPG = shutil.which('gpg') or r'C:\Program Files\Git\usr\bin\gpg.exe'
FINGERPRINT = '647F28654894E3BD457199BE38DBBDC86092693E'


def download(url, path):
    if path.exists():
        return  # The full source is still authenticated by the signature below.
    with urllib.request.urlopen(url, timeout=120) as response, path.open('wb') as out:
        shutil.copyfileobj(response, out, length=1024*1024)


def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


if __name__ == '__main__':
    releases = json.load(urllib.request.urlopen('https://www.kernel.org/releases.json', timeout=30))
    selected = next(x for x in releases['releases'] if x['moniker'] == 'longterm' and x['version'].startswith('6.12.') and not x.get('iseol'))
    OUT.mkdir(exist_ok=True)
    source = OUT / selected['source'].rsplit('/', 1)[1]
    sign = OUT / selected['pgp'].rsplit('/', 1)[1]
    download(selected['source'], source)
    download(selected['pgp'], sign)
    home = ROOT / '.gnupg'
    home.mkdir(exist_ok=True)
    key = home / 'gregkh-full.asc'
    download('https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x' + FINGERPRINT, key)
    # Git for Windows ships an MSYS gpg, so use relative POSIX paths.
    subprocess.run([GPG, '--homedir', '.gnupg', '--batch', '--import', '.gnupg/gregkh-full.asc'], cwd=ROOT, check=True, capture_output=True)
    check = subprocess.run([GPG, '--homedir', '.gnupg', '--with-colons', '--fingerprint', FINGERPRINT], cwd=ROOT, check=True, capture_output=True, text=True)
    if f'fpr:::::::::{FINGERPRINT}:' not in check.stdout:
        raise RuntimeError('Signing key fingerprint mismatch')
    proc = subprocess.Popen([GPG, '--homedir', '.gnupg', '--batch', '--status-fd', '1', '--verify', sign.relative_to(ROOT).as_posix(), '-'], cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        with lzma.open(source, 'rb') as f:
            shutil.copyfileobj(f, proc.stdin, length=1024*1024)
        proc.stdin.close()
        stdout = proc.stdout.read().decode(errors='replace')
        stderr = proc.stderr.read().decode(errors='replace')
        code = proc.wait(timeout=60)
    except BaseException:
        proc.kill()
        raise
    if code or '[GNUPG:] VALIDSIG ' not in stdout or FINGERPRINT not in stdout:
        raise RuntimeError('Kernel signature verification failed: ' + stderr)
    record = dict(version=selected['version'], source_url=selected['source'], signature_url=selected['pgp'],
                  archive_name=source.name, signature_name=sign.name, sha256=sha(source), signature_sha256=sha(sign),
                  signature_validated=True, primary_key_fingerprint=FINGERPRINT,
                  key_fingerprint_reference='https://www.kernel.org/signature.html',
                  purpose='Maintained upstream LTS source. Not a tablet ready kernel.', tablet_support='unverified')
    (ROOT/'kernel-source.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    (ROOT/'docs'/'KERNEL-SIGNATURE.txt').write_text(stdout + '\n' + stderr, encoding='utf-8')
    print('Fetched and verified upstream Linux ' + selected['version'], flush=True)
