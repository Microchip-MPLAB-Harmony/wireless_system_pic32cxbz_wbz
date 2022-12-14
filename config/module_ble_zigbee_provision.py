# coding: utf-8
##############################################################################
# Copyright (C) 2019-2020 Microchip Technology Inc. and its subsidiaries.
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

print('Load Module: Harmony Wireless Zigbee BLE Provisioning Driver')

## Zigbee Devices 
provComponent  = Module.CreateComponent('bz_prov', 'BLE ZIGBEE PROVISIONING', '/Wireless/System Services/', 'config/ble_zigbee_provisioning/bz_provision.py')
provComponent.setDisplayType('BLE Zigbee PROVISIONING')
# provComponent.addCapability("BLE_Zigbee_Prov_Service_Capability", "BZPROV_SERV", "Provisioning Application", False)
provComponent.addDependency('BLE_ZIGBEE_TRP_Dependency', 'PROFILE_TRSP', 'BLE Transparent Profile', True, False)
provComponent.addDependency('PDS_Module_Dependency', 'PDS_SubSystem', 'PDS Subsytem', True, True)
provComponent.addDependency('PIC32CX_BZ2_DevSupport_Dependency', 'Device_Support', 'Device Support', True, True)
# provComponent.addDependency('BLE_Device_Information_Dependency', 'BLE_DIS', 'BLE Device Discovery Service', True, True)
# provComponent.addDependency('BLE_MBD_APP_ADV_Dependency', 'BLE_MBD_ADV', 'BLE MBD App Advertizement', False, True)
provComponent.addDependency('BLE_ZIGBEE_PROV_Dependency', 'BZ_PROV', "ZigBee Device", False, True)

