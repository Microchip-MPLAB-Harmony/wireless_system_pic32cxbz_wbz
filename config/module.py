"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

######################  Harmony replaceme  ######################
def loadModule():
    print('Load Module: Harmony Wireless Service for PIC32CXBZx and WBZx Family')

    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          'WBZ451H',
                          }
    pic32cx_bz3_family = {'PIC32CX5109BZ31048',
                          'PIC32CX5109BZ31032',
                          'WBZ351',
                          'WBZ350',
                          }                          
    pic32cx_bz6_family = {'PIC32CX2051BZ62132',
                          'PIC32CX2051BZ62064',
                          'PIC32CX2051BZ66048',
                          'WBZ651',
                          'WBZ652',
                          'WBZ653',
                          'PIC32WM_BZ6204',
                          }                          
    atsam_family       = {'ATSAML21J18B',
	                      'ATSAMD21G18A',
						  'ATSAMR21G18A',
						  'ATSAMR30G18A',
						 }
                         
    processor = Variables.get('__PROCESSOR')
    print('processor={}'.format(processor))

    if( processor in pic32cx_bz2_family):
        ## PIC32CX-BZ BLE ZIGBEE Provisioning Service
        execfile(Module.getPath() + '/config/module_ble_zigbee_provision.py')
        # app timer service
        execfile(Module.getPath() + '/config/module_app_timer_freertos.py')
        # ble virtual sniffer
        execfile(Module.getPath() + '/config/module_ble_virtual_sniffer.py')
        # ble ota application service
        execfile(Module.getPath() + '/config/module_ble_ota.py')
        # Thread CoAP Application Service
        execfile(Module.getPath() + '/config/module_thread_coap.py')
        # BLE Thread Provisioning Service
        execfile(Module.getPath() + '/config/module_ble_provision.py')
    if((processor in pic32cx_bz2_family) or (processor in atsam_family)):
	    # IEEE 802.15.4 P2P PHY Application
        execfile(Module.getPath() + '/config/module_15_4_p2p_phy_app.py')		
    if( processor in pic32cx_bz3_family):
        # app timer service
        execfile(Module.getPath() + '/config/module_app_timer_freertos.py')
        # rgb led service
        execfile(Module.getPath() + '/config/module_rgb_led.py')
        # ble virtual sniffer
        execfile(Module.getPath() + '/config/module_ble_virtual_sniffer.py')        
        # temp sensor service
        execfile(Module.getPath() + '/config/module_temp_sensor.py')
        # ble ota application service
        execfile(Module.getPath() + '/config/module_ble_ota.py')
    if( processor in pic32cx_bz6_family):
        # app timer service
        execfile(Module.getPath() + '/config/module_app_timer_freertos.py')
        # rgb led service
        execfile(Module.getPath() + '/config/module_rgb_led.py')
        # ble virtual sniffer
#        execfile(Module.getPath() + '/config/module_ble_virtual_sniffer.py')        
        # temp sensor service
        execfile(Module.getPath() + '/config/module_temp_sensor.py')
        # ble ota application service
        execfile(Module.getPath() + '/config/module_ble_ota.py')
