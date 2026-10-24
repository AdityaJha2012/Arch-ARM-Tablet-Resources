# Resource catalog

Collected 24 October 2026. Source availability is not tablet compatibility.

## Arch ARM, kernel and development documentation

| Resource | Purpose |
| --- | --- |
| [Arch Linux ARM](https://archlinuxarm.org/) | Maintained ARM distribution |
| [Generic AArch64 base](https://archlinuxarm.org/platforms/armv8/generic) | Userspace base, not a tablet image |
| [Official downloads and signatures](https://archlinuxarm.org/about/downloads) | Download the base tarball and signature upstream |
| [Package signing](https://archlinuxarm.org/about/package-signing) | Official trust and signature guidance |
| [Supported platforms](https://archlinuxarm.org/platforms) | Check platform support separately |
| [Arch ARM package search](https://archlinuxarm.org/packages) | Check ARM package availability |
| [PKGBUILD reference](https://man.archlinux.org/man/PKGBUILD.5.en) | Packaging concepts, not x86 binary packages |
| [makepkg reference](https://man.archlinux.org/man/makepkg.8.en) | Package builder |
| [Linux kernel sources](https://www.kernel.org/) | Maintained upstream kernel sources and signatures |
| [ARM64 boot protocol](https://www.kernel.org/doc/html/latest/arch/arm64/booting.html) | Kernel boot requirements |
| [Linux Devicetree](https://docs.kernel.org/devicetree/usage-model.html) | Hardware description |
| [Kernel build documentation](https://docs.kernel.org/kbuild/index.html) | Kernel configuration and compilation |
| [Samsung Open Source](https://opensource.samsung.com/) | Official model and firmware matching source lookup, automated fetch timed out |
| [Samsung-QTI](https://github.com/Samsung-QTI) | Community Android development, not official Samsung Linux support |
| [Samsung-QTI-Blair](https://github.com/Samsung-QTI-Blair) | Community downstream kernel module sources |
| [Android GKI](https://source.android.com/docs/core/architecture/kernel/generic-kernel-image) | Android kernel architecture |
| [Android kernel build guide](https://source.android.com/docs/setup/build/building-kernels) | Android build reference, not Arch port instructions |
| [Android common kernel](https://android.googlesource.com/kernel/common/) | Generic Android kernel source, not complete tablet BSP |
| [Mesa Freedreno](https://docs.mesa3d.org/drivers/freedreno.html) | Adreno graphics userspace, board integration still needed |
| [Linux firmware](https://kernel.googlesource.com/pub/scm/linux/kernel/git/firmware/linux-firmware/) | Firmware source repository, individual file licenses apply |
| [QEMU ARM virt](https://www.qemu.org/docs/master/system/arm/virt.html) | Generic ARM virtual board, not tablet hardware emulation |
| [postmarketOS porting guide](https://wiki.postmarketos.org/wiki/Porting_to_a_new_device) | Cross distribution porting reference, automated access blocked/redirected |
| [XFCE developer documentation](https://developer.xfce.org/) | Lightweight desktop development |
| [Wayland documentation](https://wayland.freedesktop.org/docs/html/) | Display stack reference |
| [Termux proot-distro](https://github.com/termux/proot-distro) | Optional userspace inside Android, not a replacement kernel |
| [Termux X11](https://github.com/termux/termux-x11) | Optional graphical server inside Android |

## Source snapshots

The release ZIP contains the rows marked Included. Others are references only. No build or tablet test has been performed.

| Repository | Purpose | Snapshot | In ZIP |
| --- | --- | --- | --- |
| [archlinuxarm/PKGBUILDs](https://github.com/archlinuxarm/PKGBUILDs) | Arch ARM packaging recipes | [89ff712fd8a8](https://github.com/archlinuxarm/PKGBUILDs/tree/89ff712fd8a8bd898a62020c416800b464c97f14) | Link only |
| [Samsung-QTI/manifest](https://github.com/Samsung-QTI/manifest) | Android source manifest, reference only | [01dc6edc3ad4](https://github.com/Samsung-QTI/manifest/tree/01dc6edc3ad4ccc7c34a060cbc0c16afec223a57) | Link only |
| [Samsung-QTI/android_kernel_msm-5.4](https://github.com/Samsung-QTI/android_kernel_msm-5.4) | Older downstream 5.4 kernel, historical reference | [a3e637fe3e9c](https://github.com/Samsung-QTI/android_kernel_msm-5.4/tree/a3e637fe3e9c50ad1431d48e158da949ad06d19b) | Included |
| [Samsung-QTI/android_kernel_build](https://github.com/Samsung-QTI/android_kernel_build) | Android kernel build tools, not the kernel itself | [9c2058f23284](https://github.com/Samsung-QTI/android_kernel_build/tree/9c2058f2328403803d7f88dd6a825fbc15d6997d) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_touch-drivers](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_touch-drivers) | Touch source | [51e2b47435d7](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_touch-drivers/tree/51e2b47435d7e504413e3ccfb3c059998db128c0) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_graphics-kernel](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_graphics-kernel) | Graphics source | [05a7c0968a35](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_graphics-kernel/tree/05a7c0968a354287e6081878419d695cf5ece8be) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_display-drivers](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_display-drivers) | Display source | [9fe7a9013eee](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_display-drivers/tree/9fe7a9013eee34dd4f41d1b38a4faec07f0310d4) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_audio-kernel-ar](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_audio-kernel-ar) | Audio source | [30300204f5f6](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_audio-kernel-ar/tree/30300204f5f6e38dbf45ca68c393938dd90feb31) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_bt-kernel](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_bt-kernel) | Bluetooth source | [5fccb3531bc7](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_bt-kernel/tree/5fccb3531bc718200d5e0a0a5b0f4c3e0c8e8591) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_camera-kernel](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_camera-kernel) | Camera source | [2a1eaa132775](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_camera-kernel/tree/2a1eaa132775b060d2b3b674cfc3c04ac245662b) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_video-driver](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_video-driver) | Video source | [559ad87ab3e6](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_video-driver/tree/559ad87ab3e6904c3cbd1ff1f73024e0d22de979) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_wlan_platform](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_wlan_platform) | WLAN platform source | [6a5f454400ce](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_wlan_platform/tree/6a5f454400ce0446961a0b7fdaa45b7372933fbb) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qcacld-3.0](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qcacld-3.0) | WLAN driver source | [267b65986bce](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qcacld-3.0/tree/267b65986bcec01b307c4f4f7534e6ed21bff094) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_dsp-kernel](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_dsp-kernel) | DSP source | [a17b604c7e57](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_dsp-kernel/tree/a17b604c7e57f80093657dfefe7f54d628d2782d) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_dataipa](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_dataipa) | Data networking source | [049a43c96619](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_dataipa/tree/049a43c966195136041de68b90ec62b9c2ec33b0) | Included |
| [Samsung-QTI/android_vendor_qcom_opensource_usb](https://github.com/Samsung-QTI/android_vendor_qcom_opensource_usb) | Android USB integration source | [6b9b73beedf1](https://github.com/Samsung-QTI/android_vendor_qcom_opensource_usb/tree/6b9b73beedf17430a5bae64fd984243c2948502f) | Included |
| [Samsung-QTI/android_vendor_qcom_opensource_power](https://github.com/Samsung-QTI/android_vendor_qcom_opensource_power) | Android power integration source | [e4b95d738173](https://github.com/Samsung-QTI/android_vendor_qcom_opensource_power/tree/e4b95d7381734fabfa045cc3e39cd0fd1d534727) | Included |
| [Samsung-QTI/android_hardware_qcom_thermal](https://github.com/Samsung-QTI/android_hardware_qcom_thermal) | Android thermal integration source | [9a914ee03ed6](https://github.com/Samsung-QTI/android_hardware_qcom_thermal/tree/9a914ee03ed648ed027005fdc58589623e739746) | Included |
| [Samsung-QTI/device_samsung_gta9pwifi](https://github.com/Samsung-QTI/device_samsung_gta9pwifi) | WiFi model Android product configuration, not 5G | [086f9b8489ce](https://github.com/Samsung-QTI/device_samsung_gta9pwifi/tree/086f9b8489ce8c66a2d11a6150118984374f2e87) | Link only |
| [Samsung-QTI-Blair/android_kernel_platform_build_config](https://github.com/Samsung-QTI-Blair/android_kernel_platform_build_config) | WiFi oriented kernel build configuration reference | [1fa1c2735359](https://github.com/Samsung-QTI-Blair/android_kernel_platform_build_config/tree/1fa1c2735359d0a920bd445f98873e097ff9dcd2) | Link only |
| [Samsung-QTI-Blair/android_kernel_platform_external_dtc](https://github.com/Samsung-QTI-Blair/android_kernel_platform_external_dtc) | Devicetree compiler source | [5925a0237fc3](https://github.com/Samsung-QTI-Blair/android_kernel_platform_external_dtc/tree/5925a0237fc31031a16737f3a4b63404e3519a60) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_mm-drivers](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_mm-drivers) | Multimedia source | [e992605039e0](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_mm-drivers/tree/e992605039e0712ed09fdebdfc8888e2261be9bc) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_mmrm-driver](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_mmrm-driver) | Multimedia resource manager source | [81a24dcd2b5f](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_mmrm-driver/tree/81a24dcd2b5ff463664b0ec125587b757cb5357c) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet) | Data networking kernel source | [c8bd2fc6789b](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet/tree/c8bd2fc6789b58c9cf90d1132895a50e52acd583) | Included |
| [Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet-ext](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet-ext) | Data networking extension source | [0b92e6839c44](https://github.com/Samsung-QTI-Blair/vendor_qcom_opensource_datarmnet-ext/tree/0b92e6839c44d184c36640468badb44238a0ab7c) | Included |

## Maintained upstream kernel source

Linux **6.12.114**, [official source](https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.12.114.tar.xz) and [signature](https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.12.114.tar.sign). Included in the ZIP. Its signature was verified using the key fingerprint published by kernel.org. See [verification output](KERNEL-SIGNATURE.txt). This is general kernel source, not a tablet ready image.

## Unresolved manifest references

These projects were referenced in the community manifests but could not be accessed publicly during collection:

* `Samsung-QTI-Blair/kernel-common`
* `Samsung-QTI-Blair/kernel-qcom`
* `Samsung-QTI-Blair/vendor_qcom_opensource_wlan_fw-api`
* `Samsung-QTI-Blair/vendor_qcom_opensource_wlan_qca-wifi-host-cmn`

No replacement for those missing projects is implied by the generic upstream kernel. The community build needs its own matching sources and dependencies.

## License records

Detected GitHub licenses and source notice locations are recorded in [sources.json](../sources.json). The presence of a license header in one file does not relicense the whole repository. Consult each file before reusing it. Archive paths and original notices are preserved.
