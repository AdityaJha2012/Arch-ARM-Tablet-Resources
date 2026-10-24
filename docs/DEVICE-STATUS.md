# Tablet hardware status

Research date: 24 October 2026. No tablet has been connected or tested for this collection.

User supplied target: Galaxy Tab A9+ 5G, 8 GB RAM, 128 GB storage, purchased in India. **The exact model and firmware build are unknown.** Do not infer the variant from the country alone.

The [Samsung-QTI community](https://github.com/Samsung-QTI) distinguishes `gta9p` / SM-X216 from `gta9pwifi` / SM-X210. This is community Android development, not official Samsung Linux support. WiFi model files must not be assumed compatible with the 5G tablet. The smaller Tab A9 is also a different device.

Every native Arch hardware item below is **unverified**. A repository name indicates a research lead, not a working driver for this model.

| Component | Research lead | Evidence still required |
| --- | --- | --- |
| Boot, CPU, RAM | Samsung sources, downstream kernel, ARM64 boot protocol | Exact board, boot format and successful recoverable boot |
| Internal storage and microSD | Kernel MMC/storage drivers and board description | Read/write integrity and removable media |
| Display and brightness | Community display modules and Linux DRM | Correct panel, modes, backlight and suspend |
| Touch | Community touch drivers | Exact controller, firmware, scaling and multitouch |
| GPU | Community graphics modules, Mesa Freedreno | Matching kernel interface, firmware and acceleration |
| WiFi | Community WLAN modules and firmware | Correct chip, board data, authentication and reconnect |
| Bluetooth | Community BT modules | Firmware, pairing, audio and suspend |
| Speakers and microphone | Audio/DSP sources | Routing, calibration, capture and playback |
| Cameras | Camera/video sources | Sensors, ISP, firmware and Linux camera userspace |
| 5G and SIM | Data networking sources, modem integration | Modem firmware, control interface, SIM and mobile data |
| USB | Android USB sources and kernel | Host/device mode, charging and reconnect |
| Battery and charging | Kernel power drivers and Android power sources | Safe charging, battery readings and thermal behavior |
| Sleep and thermals | Kernel/platform configuration | Suspend, resume, battery drain and throttling |
| Buttons and sensors | Kernel/input and board configuration | Rotation, buttons and sensor access |
| Location | Modem/GNSS integration | Actual fix and power behavior |

No claim is made that all required source code or firmware is publicly available. Some hardware may depend on proprietary components and substantial engineering.
