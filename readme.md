﻿![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# MPLAB® Harmony 3 PIC32CXBZ wireless system services

MPLAB® Harmony 3 is an extension of the MPLAB® ecosystem for creating
embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller
and microprocessor devices.  Refer to the following links for more information.

- [Microchip 32-bit MCUs](https://www.microchip.com/design-centers/32-bit)
- [Microchip 32-bit MPUs](https://www.microchip.com/design-centers/32-bit-mpus)
- [Microchip MPLAB X IDE](https://www.microchip.com/mplab/mplab-x-ide)
- [Microchip MPLAB® Harmony](https://www.microchip.com/mplab/mplab-harmony)
- [Microchip MPLAB® Harmony Pages](https://microchip-mplab-harmony.github.io/)

This repository contains the MPLAB® Harmony 3 Wireless, wireless system services for the PIC32CXBZ family of devices. Wireless system services abstracts out the complexities of a networked system design and simplifies development using PIC32CXBZ. Refer to the following links for more information about each system service.

* [BLE Application Timer Services](https://onlinedocs.microchip.com/pr/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C-en-US-1/index.html?GUID-E1A30ECC-1212-4B25-AE72-7EAF982C6D50)
  - Application timer component used to configure the different time intervals, one-shot timer, and periodic timer for Chimera WBZ45x application requirements.
* [BLE Over The Air (OTA) Services](https://onlinedocs.microchip.com/pr/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C-en-US-1/index.html?GUID-E1A30ECC-1212-4B25-AE72-7EAF982C6D50)
  - BLE Over the Air (OTA) component is used to do the device firmware upgrade over the wireless interface available.
* [BLE BLE Virtual Sniffer Tool Services](https://onlinedocs.microchip.com/pr/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C-en-US-1/index.html?GUID-E1A30ECC-1212-4B25-AE72-7EAF982C6D50)
  - BLE Virtual Sniffer system service component for capturing the HCI packets and feed it to the sniffer tool for debugging purposes
* [IEEE 802.15.4 P2P PHY APPLICATION](https://onlinedocs.microchip.com/pr/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C-en-US-2/index.html?GUID-7663617B-0DD1-45FA-86B5-EB0778A5A424)
  - P2P PHY Application built on top of the Standalone IEEE 802.15.4 Physical Layer for PIC32CX-BZ2 platform devices. The application demonstrates the usage of Standalone 15.4 PHY MCC compoenent which provides interface to access the 802.15.4(zigbee) subsystem of PIC32CX-BZ2 devices through which user can enable various functionaities of the transceiver.
* [Thread CoAP Application Service](https://onlinedocs.microchip.com/oxy/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C)
  - CoAP Application service component build on top of Thread stack for PIC32CX-BZ2 platform devices. This component is used to develop CoAP applications on the Thread stack.
* [BLE Provision Service](https://onlinedocs.microchip.com/oxy/GUID-A5330D3A-9F51-4A26-B71D-8503A493DF9C)
  - The BLE Provisioning Service component is built on top of the BLE and Thread stacks for PIC32CX-BZ2 platform devices. This component is used to develop BLE Provisioning applications on the Thread stack.

Refer to the following links for release notes, training materials, and interface reference information.

- [Release Notes](./release_notes.md)
- [MPLAB® Harmony License](mplab_harmony_license.md)
- [MPLAB® Harmony 3 PIC32CXBZ System Services Wiki](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz/wiki)
- [MPLAB® Harmony 3 PIC32CXBZ System Services API Help](https://microchip-mplab-harmony.github.io/wireless_system_pic32cxbz_wbz)

<br />
<br />

## Contents Summary

| Folder     | Description                             |
| ---        | ---                                     |
| system       | Contains Wireless service code and configuration files. |
| docs       | [Wireless System Services documentation](https://onlinedocs.microchip.com/g/GUID-2085FE66-A762-4CC0-B054-7F98E8AF999A)

## Code Examples

- Wireless subsystem code examples for PIC32CXBZ2 can be found in the [wireless_apps_pic32cxbz2_wbz45](https://github.com/Microchip-MPLAB-Harmony/wireless_apps_pic32cxbz2_wbz45) repo.
- Wireless subsystem code examples for PIC32CXBZ3 can be found in the [wireless_apps_pic32cxbz3_wbz35](https://github.com/Microchip-MPLAB-Harmony/wireless_apps_pic32cxbz3_wbz35) repo.
- Wireless subsystem code examples for PIC32CXBZ6 can be found in the [wireless_apps_pic32_bz6](https://github.com/Microchip-MPLAB-Harmony/wireless_apps_pic32_bz6) repo.


____

[![License](https://img.shields.io/badge/license-Harmony%20license-orange.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32mzw1_wfi32e01/blob/master/mplab_harmony_license.md)
[![Latest release](https://img.shields.io/github/release/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz/releases/latest)
[![Latest release date](https://img.shields.io/github/release-date/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz/releases/latest)
[![Commit activity](https://img.shields.io/github/commit-activity/y/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg)](https://github.com/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz/graphs/commit-activity)
[![Contributors](https://img.shields.io/github/contributors-anon/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg)]()

____

[![Follow us on Youtube](https://img.shields.io/badge/Youtube-Follow%20us%20on%20Youtube-red.svg)](https://www.youtube.com/user/MicrochipTechnology)
[![Follow us on LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20us%20on%20LinkedIn-blue.svg)](https://www.linkedin.com/company/microchip-technology)
[![Follow us on Facebook](https://img.shields.io/badge/Facebook-Follow%20us%20on%20Facebook-blue.svg)](https://www.facebook.com/microchiptechnology/)
[![Follow us on Twitter](https://img.shields.io/twitter/follow/MicrochipTech.svg?style=social)](https://twitter.com/MicrochipTech)

[![](https://img.shields.io/github/stars/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg?style=social)]()
[![](https://img.shields.io/github/watchers/Microchip-MPLAB-Harmony/wireless_system_pic32cxbz_wbz.svg?style=social)]()
