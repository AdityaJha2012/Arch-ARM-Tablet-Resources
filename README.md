# Arch ARM Tablet Resources

Resources for building an Arch Linux ARM based system, with extra research for the Samsung Galaxy Tab A9+ 5G.

**This is a developer resource pack. It is not an OS image or a complete tablet driver pack.** No tablet hardware has been tested. The exact SM-X model and firmware are still unknown.

## Download the files

**[Download the complete resource pack](https://github.com/AdityaJha2012/Arch-ARM-Tablet-Resources/releases/download/v0.1.0/Arch-ARM-Tablet-Resources-v0.1.0.zip)**

Extract the ZIP and open `docs/START-HERE.md`. It includes actual source archives, these guides, an inventory and checksums. Large upstream archives live in the release download rather than Git history.

[View the release and checksum](https://github.com/AdityaJha2012/Arch-ARM-Tablet-Resources/releases/tag/v0.1.0)

## What is included

* A maintained upstream Linux LTS source archive and its verified signature
* An older Samsung community 5.4 kernel snapshot for reference
* Android kernel build tools and Devicetree compiler sources
* Community driver sources covering display, graphics, touch, WiFi, Bluetooth, audio, cameras, video, DSP and data networking
* Android USB, power and thermal integration references
* Arch Linux ARM downloads, signing instructions, package recipes and development resources
* Pinned source commits, a hardware checklist and a development roadmap

The older kernel and the newer driver modules are **different development baselines**. They are not a matched build kit. Android drivers and HALs are not ready made Arch packages. Some references in the newer community kernel manifests are unavailable publicly. These gaps are recorded rather than hidden.

## Read in this order

1. [Start here and download guidance](docs/START-HERE.md)
2. [Root filesystem, kernel and drivers explained](docs/KERNEL-AND-ROOTFS.md)
3. [Tablet hardware status](docs/DEVICE-STATUS.md)
4. [Development roadmap](docs/BUILD-ROADMAP.md)
5. [All resources and source snapshots](docs/RESOURCE-CATALOG.md)
6. [Source limitations and licenses](docs/SOURCE-LIMITATIONS.md)

## Arch base

Get the current base filesystem and its signature from [Arch Linux ARM's official downloads](https://archlinuxarm.org/about/downloads). Use the [generic AArch64 developer guide](https://archlinuxarm.org/platforms/armv8/generic) to understand the base. It is not a Galaxy tablet installation guide. The base filesystem and proprietary firmware are not mirrored in this pack.

## Scope

This is an independent collection for study and porting. Galaxy OS was cancelled. Nothing here changes Bodh OS. There are no flashing scripts, unlock tools, tablet firmware images or claims of complete hardware support.

Collection version: **0.1.0**, researched **24 October 2026**. Our documentation and helper code use MIT. Upstream code retains its own licenses.
