# coding: utf-8
##############################################################################
# Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

print('Load Module: Harmony Wireless Thread BLE Provisioning Driver')

## Thread Devices 
provBle  = Module.CreateComponent('ble_prov', 'BLE PROVISIONING', '/Wireless/System Services/', 'config/ble_provisioning/ble_provision.py')
provBle.setDisplayType('BLE PROVISIONING')
provBle.addDependency('BLE_TRP_Dependency', 'Transparent Profile', 'Transparent Profile', True, False)
provBle.addDependency('PDS_Module_Dependency', 'PDS_SubSystem', 'PDS Subsytem', True, True)
provBle.addDependency('PIC32CX_BZ2_DevSupport_Dependency', 'Device_Support', 'Device Support', True, True)
provBle.addDependency('openthread_Dependency', 'Thread Stack', 'Thread Stack', True, True)
provBle.addDependency('Ieee802154PhyDependency', 'IEEE 802.15.4 PHY', 'IEEE 802.15.4 PHY', True, True)
provBle.addDependency('Ieee802154MacDependency', 'IEEE 802.15.4 MAC', 'IEEE 802.15.4 MAC', True, True)