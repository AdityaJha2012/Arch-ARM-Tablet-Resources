# Development roadmap

## 1. Learn and assemble the base

Study Linux, C, shell, Python, pacman, PKGBUILD, systemd, cross compilation and Devicetree. Use Arch Linux ARM's own ARM repositories. Desktop Arch x86_64 packages cannot replace ARM64 packages.

Obtain the official AArch64 filesystem and verify its signature. Keep the original download name, date, signature, key fingerprint and a locally calculated SHA256 in your build records. The upstream latest URL changes over time.

## 2. Validate software in a VM

Use QEMU's ARM64 `virt` platform and a kernel/UEFI setup prepared for that virtual board. Start with a console, then networking, storage, pacman and a small graphical session. Use a disposable disk image. Record the root filesystem, kernel, packages and commands used.

QEMU virt is not a Galaxy tablet emulator. Passing this stage validates userspace and virtual devices only.

## 3. Identify the real tablet

Record the exact SM-X model, firmware build and bootloader version. Obtain matching Samsung published kernel sources and inspect community work for that exact variant. Establish a model specific restore procedure before considering any hardware change. Never use a different variant's firmware as a substitute.

## 4. Make the source build reproducible

Choose a downstream or mainline research path. Inventory every repository, commit, submodule, compiler, generated file, firmware requirement and license. Review any build scripts before running them. Resolve missing or inconsistent upstream manifest projects first. The snapshots in this collection are references, not a complete Android checkout.

Use PKGBUILD packages for your own kernel, configuration and applications once they build. Keep package signatures enabled. Do not use partial upgrades or disable signature verification to get past failures.

## 5. Port and measure one component at a time

Begin hardware work only with the exact model and a recoverable development setup. Prove boot and console, then storage, display, input, networking, graphics, sound, power and remaining peripherals. Preserve logs and mark each item unknown, partial, passed or failed. Do not call the port daily usable until charging, thermals, sleep and restore have been validated.

## 6. Build a product on the validated base

Add branding, a lightweight desktop, account defaults and your applications as versioned packages. Keep your own changes separate from upstream. Publish source obligations, licenses, installation and recovery instructions, known issues and actual hardware results with each release.

This repository completes the resource collection. It does not complete these future porting stages.
