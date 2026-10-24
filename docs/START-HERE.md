# Start here

This collection helps a developer research an Arch Linux ARM system and a possible Samsung Galaxy Tab A9+ port. It is not an installer, a finished OS, or a complete driver pack.

## First steps

1. Read the [resource list](../README.md) and [hardware status](DEVICE-STATUS.md).
2. Obtain the exact tablet model and firmware build from Settings > About tablet > Software information. The country and RAM size are not enough. Record those locally. Do not post a serial number or IMEI.
3. Start with the official [Arch Linux ARM generic AArch64 base](https://archlinuxarm.org/platforms/armv8/generic). Its root filesystem provides packages and configuration. It does not supply a tablet specific boot path.
4. Read [the difference between the root filesystem and hardware support](KERNEL-AND-ROOTFS.md).
5. Download source archives from this repository's Releases page. Each archive is named after its upstream repository and pinned commit. Keep the upstream license files.
6. Follow the [development roadmap](BUILD-ROADMAP.md). First validate the software in an ARM64 VM. Native tablet work is a separate porting task.

## What to download

For study, GitHub's Code > Download ZIP contains this guide, the catalog, source pins, and helper. The release also contains actual kernel, packaging, build-tool and driver source snapshots, plus SHA256SUMS and an index. These are source archives, not flashable firmware.

The Arch Linux ARM base filesystem stays on its official download service. Use the [official downloads page](https://archlinuxarm.org/about/downloads) for its current tarball and detached signature. Read the [official signing instructions](https://archlinuxarm.org/about/package-signing). Verify the signature against the published signing key. A checksum alone does not authenticate an upstream download.

To fetch the exact source snapshots again:

```text
python tools/fetch-sources.py
```

The helper downloads archives and checks their published SHA256 values. It never executes the downloaded code or writes to a tablet. Source archives do not include full Git history, submodule contents, toolchain prebuilts or every transitive build dependency.

Use a Linux development environment to unpack and build the kernel sources. Windows archive tools and filesystems may not preserve Linux names, links and permissions. The optional catalog and LTS refresh helpers are for maintainers. They update the selected upstream versions and do not reproduce a historical release.

## Important boundary

Do not flash an Arch root filesystem tarball, a generic kernel, a WiFi model recovery image, or one of these source archives onto the tablet. This collection has no validated tablet installation procedure. A working Android build or a successful VM boot would not establish native Arch hardware support.
