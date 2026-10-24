# How the pieces fit together

| Part | What it does | What this collection provides |
| --- | --- | --- |
| AArch64 userspace | Programs, libraries, pacman and system configuration | Official Arch Linux ARM base and packaging links |
| Kernel | Memory, processes and hardware drivers | Linux documentation, a downstream Samsung community kernel snapshot and current Android kernel references |
| Hardware description | Board wiring, addresses, interrupts and peripheral configuration | Devicetree documentation and model specific research pointers |
| Firmware | Code loaded into some peripherals | Upstream linux-firmware reference and Samsung source lookup. No proprietary firmware bundle |
| Boot chain | Loads and authorizes boot images | Architecture and Android boot documentation. No tablet unlocking or flashing script |
| Hardware services | Graphics, sound, networking, power and sensors | Source references and a checklist of unresolved integration work |
| Desktop | Windows, launcher, settings and applications | XFCE, Wayland and packaging documentation |

A 64 bit ARM CPU can run AArch64 instructions. It does not imply that a generic ARM image knows the tablet's display, touchscreen, storage, power management or boot format.

An Android device tree repository usually means Android product configuration and build files. A Linux DTS/DTB describes hardware. These are related parts of porting, but they are not interchangeable files.

Android HALs and GKI modules target Android interfaces and particular kernel ABIs. They are useful references, not ready to install pacman drivers. Downstream Qualcomm graphics code may use KGSL, while the usual Linux Mesa Freedreno path uses the DRM/MSM interface. Userspace, firmware and kernel interfaces must match.

Two possible research paths are a downstream vendor kernel adapted for Linux userspace, or a mainline kernel with the missing board support implemented. Neither is selected or validated here. The included older 5.4 kernel is historical source material, not a security recommendation. The community describes newer 6.1 GKI work, but some repositories named in its manifests are unavailable publicly at the time of collection. See [source limitations](SOURCE-LIMITATIONS.md).

Running an Arch userspace inside Android through Termux or a container keeps Android's kernel. That can be useful for learning, but is not a native Arch tablet port.

References: [Linux AArch64 boot protocol](https://www.kernel.org/doc/html/latest/arch/arm64/booting.html), [Linux Devicetree](https://docs.kernel.org/devicetree/usage-model.html), [Android GKI](https://source.android.com/docs/core/architecture/kernel/generic-kernel-image), [Mesa Freedreno](https://docs.mesa3d.org/drivers/freedreno.html).
