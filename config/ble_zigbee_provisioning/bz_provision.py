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

ZIGBEE_DEVICE_TYPES= ['ZIGBEE_COLOR_SCENE_CONTROLLER',
                'ZIGBEE_MULTI_SENSOR',
                'ZIGBEE_COMBINED_INTERFACE',
                'ZIGBEE_THERMOSTAT',
                'ZIGBEE_IAS_ACE',
                'ZIGBEE_ON_OFF_LIGHT',
                'ZIGBEE_DIMMABLE_LIGHT',
                'ZIGBEE_COLOR_LIGHT',
                'ZIGBEE_EXTENDED_COLOR_LIGHT',
                'ZIGBEE_TEMPERATURE_COLOR_LIGHT',
                'ZIGBEE_CUSTOM']
                
def check_zigbee_device():
    for comp in Database.getActiveComponentIDs():
        if comp in ZIGBEE_DEVICE_TYPES:
            return comp
    return None
            

def update_BZparamters():
    trpComponent = Database.getComponentByID("PROFILE_TRSP")
    if (trpComponent != None):
        if (trpComponent.getSymbolValue("TRSP_BOOL_SERVER") == False):
            trpServerChoice = trpComponent.getSymbolByID("TRSP_BOOL_SERVER")
            trpServerChoice.setValue(True)
    bleStackComponent = Database.getComponentByID("BLE_STACK_LIB")
    if (bleStackComponent != None):
        if (bleStackComponent.getSymbolValue("GAP_ADV_DATA_LOCAL_NAME_EN") == True):
            advDataLocalNameEN = bleStackComponent.getSymbolByID('GAP_ADV_DATA_LOCAL_NAME_EN')
            advDataLocalNameEN.setValue(False)
        if (bleStackComponent.getSymbolValue("GAP_ADV_DATA_SERVICE_DATA_EN") == False):
            advSrvDataEN = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_DATA_EN')
            advSrvDataEN.setValue(True)
            advSrvDataUUID = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_UUID')
            advSrvDataUUID.setValue("DAFE")
            advSrvDataVal = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_DATA')
            advSrvDataVal.setValue("FF03")
        


def onAttachmentConnected(source, target):
    # print('BZ Provisioning --> onAttachmentConnected source= {}'.format(str(source)))
    # print('BZ Provisioning --> onAttachmentConnected target= {}'.format(str(target)))
    if (source['id'] == 'BLE_Device_Information_Dependency'):
        Database.sendMessage("app_service", "APP_PROV", {"appBleDis":True,"appBZProv":True})
    update_BZparamters()
    zb_dev = check_zigbee_device()
    if (zb_dev != None):
        appZbDevType.setValue(zb_dev)
        print('BZ Provisioning --> onAttachmentConnected zb_dev= {}'.format(str(zb_dev))) 
        zbDevComponent = Database.getComponentByID(zb_dev)
        if(zbDevComponent != None):
            #if(zbDevComponent.getSymbolValue('AUTOMATIC_CONFIGURATION') == True):
            #    autoConfig = zbDevComponent.getSymbolByID('AUTOMATIC_CONFIGURATION')
            #    autoConfig.setValue(False)
            if (zbDevComponent.getSymbolValue('AUTOMATIC_COMMISSIONING_ON_STARTUP') == True):
                autoCommStartup = zbDevComponent.getSymbolByID('AUTOMATIC_COMMISSIONING_ON_STARTUP')
                autoCommStartup.setValue(False)

def onAttachmentDisconnected(source, target):
    # print('BZ Provisioning --> onAttachmentDisconnected source= {}'.format(str(source)))
    # print('BZ Provisioning --> onAttachmentDisconnected target= {}'.format(str(target)))
    if (source['id'] == 'BLE_Device_Information_Dependency'):
        Database.sendMessage("app_service", "APP_PROV", {"appBleDis":False,"appBZProv":False})

def finalizeComponent(ble_zigbee_prov):
    result = Database.connectDependencies([['bz_prov', 'BLE_ZIGBEE_TRP_Dependency', 'PROFILE_TRSP', 'BLE_TRP_Capability']])
    result = Database.connectDependencies([['PROFILE_TRSP', 'BLE_TRS_Denpendency', 'SERVICE_TRS', 'BLE_TRS_Capability']])
    result = Database.connectDependencies([['bz_prov', 'PDS_Module_Dependency', 'pdsSystem', 'pds_Command_Capability']])
    result = Database.connectDependencies([['bz_prov', 'PIC32CX_BZ2_DevSupport_Dependency', 'pic32cx_bz2_devsupport', 'Device_Support_Capability']])
    result = Database.connectDependencies([['SERVICE_TRS', 'BLE_STACK_Dependency', 'BLE_STACK_LIB', 'BLE_Stack_Capability']])
    # result = Database.connectDependencies([['bz_prov', 'BLE_Device_Information_Dependency', 'svcBLE_DIS', 'BLE_DIS_Capability']])
    update_BZparamters()
    # Database.setSymbolValue("PROFILE_TRSP", "TRP_BOOL_SERVER", True)

        



def instantiateComponent(ble_zigbee_prov):
    print('ble_zigbee_prov')
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    processor = Variables.get("__PROCESSOR")
    print processor

    print('HarmonyCore.ENABLE_APP_FILE = {}'.format(str(Database.getSymbolValue("HarmonyCore", 'ENABLE_APP_FILE'))))
    print('HarmonyCore.ENABLE_OSAL = {}'.format(str(Database.getSymbolValue("HarmonyCore", 'ENABLE_OSAL'))))
    print('FreeRTOS.FREERTOS_USE_QUEUE_SETS = {}'.format(str(Database.getSymbolValue("FreeRTOS", 'FREERTOS_USE_QUEUE_SETS'))))
    
    res = Database.activateComponents(["PROFILE_TRSP","SERVICE_TRS","pdsSystem","pic32cx_bz2_devsupport","BLE_STACK_LIB"])

    print('Config Name: {} processor: {}'.format(configName, processor))    

    appTrpsEnable = ble_zigbee_prov.createBooleanSymbol("BZProv_TRPS_ENABLE", None)
    appTrpsEnable.setLabel("Enable BLE Transparent GATT Service")
    appTrpsEnable.setDefaultValue(True)
    appTrpsEnable.setVisible(False)

    global appZbDevType
    appZbDevType = ble_zigbee_prov.createStringSymbol("ZIGBEE_DEV_TYPE", None)
    appZbDevType.setLabel("ZIGBEE Device Type")
    appZbDevType.setDefaultValue("")
    appZbDevType.setVisible(True)
    appZbDevType.setReadOnly(True)
    
    # zigbeeProv_autoConfig = ble_zigbee_prov.createBooleanSymbol("DISABLE_AUTOMATIC_COMM_ON_STARTUP", None)
    # zigbeeProv_autoConfig.setLabel("Disable Automatic Commissioning on Startup")
    # zigbeeProv_autoConfig.setVisible(True)
    # zigbeeProv_autoConfig.setDefaultValue(False)
    # zigbeeProv_autoConfig.setDescription("Disable Automatic Commissioning on Startup in ZigBee Device")

    # Add app_trps.c
    appTrpsSourceFile = ble_zigbee_prov.createFileSymbol(None, None)
    appTrpsSourceFile.setSourcePath('driver/templates/app_trps.c.ftl')
    appTrpsSourceFile.setOutputName('app_trps.c')
    appTrpsSourceFile.setOverwrite(True)
    appTrpsSourceFile.setDestPath('../../app_trps')
    appTrpsSourceFile.setProjectPath('app_trps')
    appTrpsSourceFile.setType('SOURCE')
    appTrpsSourceFile.setMarkup(True)
    appTrpsSourceFile.setEnabled(True)
    
    # Add app_trps.h
    appTrpsHeaderFile = ble_zigbee_prov.createFileSymbol(None, None)
    appTrpsHeaderFile.setSourcePath('driver/templates/app_trps.h.ftl')
    appTrpsHeaderFile.setOutputName('app_trps.h')
    appTrpsHeaderFile.setOverwrite(True)
    appTrpsHeaderFile.setDestPath('../../app_trps')
    appTrpsHeaderFile.setProjectPath('app_trps')
    appTrpsHeaderFile.setType('HEADER')
    appTrpsHeaderFile.setMarkup(True)
    appTrpsHeaderFile.setEnabled(True)

    # Add app_prov_handler.c
    appProvHandlerSourceFile = ble_zigbee_prov.createFileSymbol(None, None)
    appProvHandlerSourceFile.setSourcePath('driver/templates/app_prov_handler.c.ftl')
    appProvHandlerSourceFile.setOutputName('app_prov_handler.c')
    appProvHandlerSourceFile.setOverwrite(True)
    appProvHandlerSourceFile.setDestPath('../../app_prov')
    appProvHandlerSourceFile.setProjectPath('app_prov')
    appProvHandlerSourceFile.setType('SOURCE')
    appProvHandlerSourceFile.setMarkup(True)
    appProvHandlerSourceFile.setEnabled(True)
    
    # Add app_prov_handler.h
    appProvHandlerHeaderFile = ble_zigbee_prov.createFileSymbol(None, None)
    appProvHandlerHeaderFile.setSourcePath('driver/templates/app_prov_handler.h.ftl')
    appProvHandlerHeaderFile.setOutputName('app_prov_handler.h')
    appProvHandlerHeaderFile.setOverwrite(True)
    appProvHandlerHeaderFile.setDestPath('../../app_prov')
    appProvHandlerHeaderFile.setProjectPath('app_prov')
    appProvHandlerHeaderFile.setType('HEADER')
    appProvHandlerHeaderFile.setMarkup(True)
    appProvHandlerHeaderFile.setEnabled(True)

    # Add app_prov.c - generated file ftl
    appProvSourceFile = ble_zigbee_prov.createFileSymbol(None, None)
    appProvSourceFile.setSourcePath('driver/templates/app_prov.c.ftl')
    appProvSourceFile.setOutputName('app_prov.c')
    appProvSourceFile.setOverwrite(True)
    appProvSourceFile.setDestPath('../../app_prov')
    appProvSourceFile.setProjectPath('app_prov')
    appProvSourceFile.setType('SOURCE')
    appProvSourceFile.setEnabled(True)
    appProvSourceFile.setMarkup(True) 

    # Add app_prov.h - static file ftl
    appProvHeaderFile = ble_zigbee_prov.createFileSymbol(None, None)
    appProvHeaderFile.setSourcePath('driver/templates/app_prov.h.ftl')
    appProvHeaderFile.setOutputName('app_prov.h')
    appProvHeaderFile.setOverwrite(True)
    appProvHeaderFile.setDestPath('../../app_prov')
    appProvHeaderFile.setProjectPath('app_prov')
    appProvHeaderFile.setType('HEADER')
    appProvHeaderFile.setEnabled(True)
    appProvHeaderFile.setMarkup(True) 

    # Add app_error_defs.h - static file
    appErrorHeaderFile = ble_zigbee_prov.createFileSymbol(None, None)
    appErrorHeaderFile.setSourcePath('driver/src/app_error_defs.h')
    appErrorHeaderFile.setOutputName('app_error_defs.h')
    appErrorHeaderFile.setOverwrite(True)
    appErrorHeaderFile.setDestPath('../../')
    appErrorHeaderFile.setProjectPath('')
    appErrorHeaderFile.setType('HEADER')
    appErrorHeaderFile.setEnabled(True)
    
      # Add app_ble_conn_handler.c
    appConnSourceFile = ble_zigbee_prov.createFileSymbol(None, None)
    appConnSourceFile.setSourcePath('driver/src/app_ble_conn_handler.c')
    appConnSourceFile.setOutputName('app_ble_conn_handler.c')
    appConnSourceFile.setOverwrite(True)
    appConnSourceFile.setDestPath('../../')
    appConnSourceFile.setType('SOURCE')
    appConnSourceFile.setMarkup(True)
    appConnSourceFile.setEnabled(True)
    
    # Add app_ble_conn_handler.h
    appConnHeaderFile = ble_zigbee_prov.createFileSymbol(None, None)
    appConnHeaderFile.setSourcePath('driver/src/app_ble_conn_handler.h')
    appConnHeaderFile.setOutputName('app_ble_conn_handler.h')
    appConnHeaderFile.setOverwrite(True)
    appConnHeaderFile.setDestPath('../../')
    appConnHeaderFile.setType('HEADER')
    appConnHeaderFile.setMarkup(True)
    appConnHeaderFile.setEnabled(True)