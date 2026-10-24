"""Refresh upstream metadata using an authenticated GitHub CLI. Does not build code."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[1]
GH = shutil.which('gh') or r'C:\Program Files\GitHub CLI\gh.exe'

# Only source repositories. No proprietary device trees or prebuilt firmware.
REPOS = [
    ('archlinuxarm/PKGBUILDs', 'Arch ARM packaging recipes', False),
    ('Samsung-QTI/manifest', 'Android source manifest, reference only', False),
    ('Samsung-QTI/android_kernel_msm-5.4', 'Older downstream 5.4 kernel, historical reference', True),
    ('Samsung-QTI/android_kernel_build', 'Android kernel build tools, not the kernel itself', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_touch-drivers', 'Touch source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_graphics-kernel', 'Graphics source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_display-drivers', 'Display source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_audio-kernel-ar', 'Audio source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_bt-kernel', 'Bluetooth source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_camera-kernel', 'Camera source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_video-driver', 'Video source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_wlan_platform', 'WLAN platform source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qcacld-3.0', 'WLAN driver source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_dsp-kernel', 'DSP source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_dataipa', 'Data networking source', True),
    ('Samsung-QTI/android_vendor_qcom_opensource_usb', 'Android USB integration source', True),
    ('Samsung-QTI/android_vendor_qcom_opensource_power', 'Android power integration source', True),
    ('Samsung-QTI/android_hardware_qcom_thermal', 'Android thermal integration source', True),
    ('Samsung-QTI/device_samsung_gta9pwifi', 'WiFi model Android product configuration, not 5G', False),
    ('Samsung-QTI-Blair/android_kernel_platform_build_config', 'WiFi oriented kernel build configuration reference', False),
    ('Samsung-QTI-Blair/android_kernel_platform_external_dtc', 'Devicetree compiler source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_mm-drivers', 'Multimedia source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_mmrm-driver', 'Multimedia resource manager source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet', 'Data networking kernel source', True),
    ('Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet-ext', 'Data networking extension source', True),
]

LINKS = [
    ('Arch Linux ARM', 'https://archlinuxarm.org/', 'Maintained ARM distribution'),
    ('Generic AArch64 base', 'https://archlinuxarm.org/platforms/armv8/generic', 'Userspace base, not a tablet image'),
    ('Official downloads and signatures', 'https://archlinuxarm.org/about/downloads', 'Download the base tarball and signature upstream'),
    ('Package signing', 'https://archlinuxarm.org/about/package-signing', 'Official trust and signature guidance'),
    ('Supported platforms', 'https://archlinuxarm.org/platforms', 'Check platform support separately'),
    ('Arch ARM package search', 'https://archlinuxarm.org/packages', 'Check ARM package availability'),
    ('PKGBUILD reference', 'https://man.archlinux.org/man/PKGBUILD.5.en', 'Packaging concepts, not x86 binary packages'),
    ('makepkg reference', 'https://man.archlinux.org/man/makepkg.8.en', 'Package builder'),
    ('Linux kernel sources', 'https://www.kernel.org/', 'Maintained upstream kernel sources and signatures'),
    ('ARM64 boot protocol', 'https://www.kernel.org/doc/html/latest/arch/arm64/booting.html', 'Kernel boot requirements'),
    ('Linux Devicetree', 'https://docs.kernel.org/devicetree/usage-model.html', 'Hardware description'),
    ('Kernel build documentation', 'https://docs.kernel.org/kbuild/index.html', 'Kernel configuration and compilation'),
    ('Samsung Open Source', 'https://opensource.samsung.com/', 'Official model and firmware matching source lookup, automated fetch timed out'),
    ('Samsung-QTI', 'https://github.com/Samsung-QTI', 'Community Android development, not official Samsung Linux support'),
    ('Samsung-QTI-Blair', 'https://github.com/Samsung-QTI-Blair', 'Community downstream kernel module sources'),
    ('Android GKI', 'https://source.android.com/docs/core/architecture/kernel/generic-kernel-image', 'Android kernel architecture'),
    ('Android kernel build guide', 'https://source.android.com/docs/setup/build/building-kernels', 'Android build reference, not Arch port instructions'),
    ('Android common kernel', 'https://android.googlesource.com/kernel/common/', 'Generic Android kernel source, not complete tablet BSP'),
    ('Mesa Freedreno', 'https://docs.mesa3d.org/drivers/freedreno.html', 'Adreno graphics userspace, board integration still needed'),
    ('Linux firmware', 'https://kernel.googlesource.com/pub/scm/linux/kernel/git/firmware/linux-firmware/', 'Firmware source repository, individual file licenses apply'),
    ('QEMU ARM virt', 'https://www.qemu.org/docs/master/system/arm/virt.html', 'Generic ARM virtual board, not tablet hardware emulation'),
    ('postmarketOS porting guide', 'https://wiki.postmarketos.org/wiki/Porting_to_a_new_device', 'Cross distribution porting reference, automated access blocked/redirected'),
    ('XFCE developer documentation', 'https://developer.xfce.org/', 'Lightweight desktop development'),
    ('Wayland documentation', 'https://wayland.freedesktop.org/docs/html/', 'Display stack reference'),
    ('Termux proot-distro', 'https://github.com/termux/proot-distro', 'Optional userspace inside Android, not a replacement kernel'),
    ('Termux X11', 'https://github.com/termux/termux-x11', 'Optional graphical server inside Android'),
]


def api(path):
    result = subprocess.run([GH, 'api', path], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return json.loads(result.stdout)


def collect(entry):
    repo, purpose, download = entry
    data = api('repos/' + repo)
    branch = data['default_branch']
    sha = api('repos/' + repo + '/commits/' + branch)['sha']
    return dict(repo=repo, purpose=purpose, url=data['html_url'], branch=branch, commit=sha,
                reviewed_utc=datetime.now(timezone.utc).isoformat(), archived=data['archived'],
                detected_license=(data.get('license') or {}).get('spdx_id'),
                download_archive=download, redistribution_review='pending' if download else 'link only',
                archive_url=f'https://codeload.github.com/{repo}/tar.gz/{sha}',
                archive_name=repo.replace('/', '--') + '--' + sha[:12] + '.tar.gz',
                tablet_support='unverified')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        repos = list(pool.map(collect, REPOS))
    missing = []
    for repo in ['Samsung-QTI-Blair/kernel-common', 'Samsung-QTI-Blair/kernel-qcom',
                 'Samsung-QTI-Blair/vendor_qcom_opensource_wlan_fw-api',
                 'Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qca-wifi-host-cmn']:
        try:
            api('repos/' + repo)
        except RuntimeError:
            missing.append(dict(repo=repo, status='not publicly accessible via GitHub API during collection',
                                context='Referenced by community kernel manifests. Not included in source bundle.'))
    catalog = dict(collection_version='0.1.0', checked_date='2026-10-24',
                   target='Galaxy Tab A9+ 5G, exact SM-X model and firmware unknown',
                   hardware_validated=False, repositories=repos, unavailable_references=missing,
                   resources=[dict(title=t, url=u, purpose=p) for t,u,p in LINKS])
    (ROOT / 'sources.json').write_text(json.dumps(catalog, indent=2) + '\n', encoding='utf-8')
    print(f'Collected {len(repos)} pinned repositories and {len(LINKS)} reference resources. {len(missing)} unresolved upstream references.')
