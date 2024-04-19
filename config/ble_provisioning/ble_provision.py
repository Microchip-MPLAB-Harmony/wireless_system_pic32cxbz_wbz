"""*****************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

def enableOrDisableThreadFiles(value):
    if (value):
       appProvThreadSourceFile.setEnabled(True)
       appThreadCommonHeaderFile.setEnabled(True) 
       appThreadCommonSourceFile.setEnabled(True)
       appThreadAppHeaderFile.setEnabled(True)
       appThreadAppSourceFile.setEnabled(True)
    else:
       appProvThreadSourceFile.setEnabled(False)
       appThreadCommonHeaderFile.setEnabled(False) 
       appThreadCommonSourceFile.setEnabled(False)
       appThreadAppHeaderFile.setEnabled(False)
       appThreadAppSourceFile.setEnabled(False)

def configForThread():
    res = Database.activateComponents(["OPEN_THREAD"])
    appProvPhySourceFile.setEnabled(False)
    appProvMacSourceFile.setEnabled(False)
    enableOrDisableThreadFiles(True)
    threadComponent = Database.getComponentByID("OPEN_THREAD")
    if (threadComponent):
       temSymbol = threadComponent.getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_1")
       temsymbol1 = threadComponent.getSymbolByID("OPEN_THREAD_MTD_SLEEP_ENABLE")
       temSymbol.setReadOnly(True)
       temsymbol1.setReadOnly(True)
    threaddeviceconfig.setVisible(True)

def updateParamters():
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

def protocolConfigcallback(symbol,event):
    symbolID = event["id"]
    value = event["value"]
    
    if symbolID == "COMBO_APP_CONFIG":
        if value == 0:
            appProvPhySourceFile.setEnabled(True)
            appProvMacSourceFile.setEnabled(False)
            enableOrDisableThreadFiles(False)
            Database.deactivateComponents(["OPEN_THREAD","IEEE_802154_MAC","BLE_STACK_LIB","PROFILE_TRSP"])
            res = Database.activateComponents(["IEEE_802154_PHY","BLE_STACK_LIB","PROFILE_TRSP"])
            threaddeviceconfig.setVisible(False)
            updateParamters()
        elif value == 1:
            appProvPhySourceFile.setEnabled(False)
            appProvMacSourceFile.setEnabled(True)
            enableOrDisableThreadFiles(False)
            Database.deactivateComponents(["OPEN_THREAD","BLE_STACK_LIB","PROFILE_TRSP"])
            res = Database.activateComponents(["IEEE_802154_MAC","BLE_STACK_LIB","PROFILE_TRSP"])
            threaddeviceconfig.setVisible(False)
            updateParamters()
        elif value == 2:
            Database.deactivateComponents(["IEEE_802154_MAC","BLE_STACK_LIB","PROFILE_TRSP"])
            res = Database.activateComponents(["OPEN_THREAD","BLE_STACK_LIB","PROFILE_TRSP"])
            appProvPhySourceFile.setEnabled(False)
            appProvMacSourceFile.setEnabled(False)
            enableOrDisableThreadFiles(True)
            threadComponent = Database.getComponentByID("OPEN_THREAD")
            if (threadComponent):
               temSymbol = threadComponent.getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_1")
               temsymbol1 = threadComponent.getSymbolByID("OPEN_THREAD_MTD_SLEEP_ENABLE")
               temSymbol.setReadOnly(True)
               temsymbol1.setReadOnly(True)
            threaddeviceconfig.setVisible(True)
            updateParamters()
    
    elif symbolID == "THREAD_DEVICE_CONFIG":
        if value == 0:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_DEVICE_ROLE_CONFIG_1",0)
            threadsedenableconfig.setValue(False)
            threadsedenableconfig.setReadOnly(True)
        elif value == 1:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_DEVICE_ROLE_CONFIG_1",1)
            threadsedenableconfig.setValue(False)
            threadsedenableconfig.setReadOnly(False)
    
    elif symbolID == "THREAD_SLEEP_ENABLE":
        if value == True:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_SLEEP_ENABLE",True)
            appIdleTaskSourceFile.setEnabled(True)
        elif value == False:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_SLEEP_ENABLE",False)
            appIdleTaskSourceFile.setEnabled(False)


def onAttachmentConnected(source, target):
    updateParamters()

def onAttachmentDisconnected(source, target):
    remoteComponent = Database.getComponentByID("OPEN_THREAD")
    if (remoteComponent):
        symbol = remoteComponent.getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_1")
        symbol.setReadOnly(False)

def finalizeComponent(provBle):
    result = Database.connectDependencies([['PROFILE_TRSP', 'BLE_TRS_Denpendency', 'SERVICE_TRS', 'BLE_TRS_Capability']])
    result = Database.connectDependencies([['ble_prov', 'PDS_Module_Dependency', 'pdsSystem', 'pds_Command_Capability']])
    result = Database.connectDependencies([['ble_prov', 'PIC32CX_BZ2_DevSupport_Dependency', 'pic32cx_bz2_devsupport', 'Device_Support_Capability']])
    result = Database.connectDependencies([['SERVICE_TRS', 'BLE_STACK_Dependency', 'BLE_STACK_LIB', 'BLE_Stack_Capability']])
    updateParamters()

        



def instantiateComponent(provBle):
    print('ble_prov')
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    processor = Variables.get("__PROCESSOR")
    print processor
    
    res = Database.activateComponents(["PROFILE_TRSP","SERVICE_TRS","pdsSystem","pic32cx_bz2_devsupport","BLE_STACK_LIB","IEEE_802154_PHY"])

    print('Config Name: {} processor: {}'.format(configName, processor))
    
    global protocoltypeconfig
    protocoltypeconfig = provBle.createKeyValueSetSymbol("COMBO_APP_CONFIG", None)
    protocoltypeconfig.setLabel("Combo APP Config")
    protocoltypeconfig.addKey("15_4_PHY", "15_4_PHY", "15_4_PHY")
    protocoltypeconfig.addKey("15_4_MAC", "15_4_MAC", "15_4_MAC")
    protocoltypeconfig.addKey("THREAD", "THREAD", "THREAD")
    protocoltypeconfig.setDefaultValue(2)
    protocoltypeconfig.setOutputMode("Value")
    protocoltypeconfig.setDisplayMode("Description")
    protocoltypeconfig.setDescription("protocol type Configuration")
    protocoltypeconfig.setVisible(True)
    protocoltypeconfig.setReadOnly(True)
    protocoltypeconfig.setDependencies(protocolConfigcallback,["COMBO_APP_CONFIG"])
    
    global threaddeviceconfig
    threaddeviceconfig = provBle.createKeyValueSetSymbol("THREAD_DEVICE_CONFIG", protocoltypeconfig)
    threaddeviceconfig.setLabel("Thread Device Role")
    threaddeviceconfig.addKey("FTD", "FTD", "FTD")
    threaddeviceconfig.addKey("MTD", "MTD", "MTD")
    threaddeviceconfig.setDefaultValue(0)
    threaddeviceconfig.setOutputMode("Value")
    threaddeviceconfig.setDisplayMode("Description")
    threaddeviceconfig.setDescription("Open Thread Device Role Configuration")
    threaddeviceconfig.setVisible(False)
    threaddeviceconfig.setDependencies(protocolConfigcallback,["THREAD_DEVICE_CONFIG"])
    
    global threadsedenableconfig
    threadsedenableconfig = provBle.createBooleanSymbol("THREAD_SLEEP_ENABLE", protocoltypeconfig)
    threadsedenableconfig.setLabel("Enable As Sleep End Device")
    threadsedenableconfig.setDefaultValue(False)
    threadsedenableconfig.setVisible(True)
    threadsedenableconfig.setDescription("Option to enable the device as SED")
    threadsedenableconfig.setReadOnly(True)
    threadsedenableconfig.setDependencies(protocolConfigcallback,["THREAD_SLEEP_ENABLE"])

    # Add app_trps.c
    appTrpsSourceFile = provBle.createFileSymbol(None, None)
    appTrpsSourceFile.setSourcePath('driver/templates/app_trps.c.ftl')
    appTrpsSourceFile.setOutputName('app_trps.c')
    appTrpsSourceFile.setOverwrite(True)
    appTrpsSourceFile.setDestPath('../../app_trps')
    appTrpsSourceFile.setProjectPath('app_trps')
    appTrpsSourceFile.setType('SOURCE')
    appTrpsSourceFile.setMarkup(True)
    appTrpsSourceFile.setEnabled(True)
    
    # Add app_trps.h
    appTrpsHeaderFile = provBle.createFileSymbol(None, None)
    appTrpsHeaderFile.setSourcePath('driver/templates/app_trps.h.ftl')
    appTrpsHeaderFile.setOutputName('app_trps.h')
    appTrpsHeaderFile.setOverwrite(True)
    appTrpsHeaderFile.setDestPath('../../app_trps')
    appTrpsHeaderFile.setProjectPath('app_trps')
    appTrpsHeaderFile.setType('HEADER')
    appTrpsHeaderFile.setMarkup(True)
    appTrpsHeaderFile.setEnabled(True)

    # Add app_prov.c - generated file ftl
    appProvSourceFile = provBle.createFileSymbol(None, None)
    appProvSourceFile.setSourcePath('driver/templates/ble_prov/app_prov.c.ftl')
    appProvSourceFile.setOutputName('app_prov.c')
    appProvSourceFile.setOverwrite(True)
    appProvSourceFile.setDestPath('../../app_prov')
    appProvSourceFile.setProjectPath('app_prov')
    appProvSourceFile.setType('SOURCE')
    appProvSourceFile.setEnabled(True)
    appProvSourceFile.setMarkup(True) 

    # Add app_prov.h - generated file ftl
    appProvHeaderFile = provBle.createFileSymbol(None, None)
    appProvHeaderFile.setSourcePath('driver/templates/ble_prov/app_prov.h.ftl')
    appProvHeaderFile.setOutputName('app_prov.h')
    appProvHeaderFile.setOverwrite(True)
    appProvHeaderFile.setDestPath('../../app_prov')
    appProvHeaderFile.setProjectPath('app_prov')
    appProvHeaderFile.setType('HEADER')
    appProvHeaderFile.setEnabled(True)
    appProvHeaderFile.setMarkup(True)

    # Add app_prov_phy.c - static file
    global appProvPhySourceFile
    appProvPhySourceFile = provBle.createFileSymbol(None, None)
    appProvPhySourceFile.setSourcePath('driver/src/ble_prov/app_prov_phy.c')
    appProvPhySourceFile.setOutputName('app_prov_phy.c')
    appProvPhySourceFile.setOverwrite(True)
    appProvPhySourceFile.setDestPath('../../app_prov')
    appProvPhySourceFile.setProjectPath('app_prov')
    appProvPhySourceFile.setType('SOURCE')
    appProvPhySourceFile.setMarkup(True)
    appProvPhySourceFile.setEnabled(True)

    # Add app_prov_mac.c - static file
    global appProvMacSourceFile
    appProvMacSourceFile = provBle.createFileSymbol(None, None)
    appProvMacSourceFile.setSourcePath('driver/src/ble_prov/app_prov_mac.c')
    appProvMacSourceFile.setOutputName('app_prov_mac.c')
    appProvMacSourceFile.setOverwrite(True)
    appProvMacSourceFile.setDestPath('../../app_prov')
    appProvMacSourceFile.setProjectPath('app_prov')
    appProvMacSourceFile.setType('SOURCE')
    appProvMacSourceFile.setMarkup(True)
    appProvMacSourceFile.setEnabled(False)

    # Add app_prov_thread.c - static file
    global appProvThreadSourceFile
    appProvThreadSourceFile = provBle.createFileSymbol(None, None)
    appProvThreadSourceFile.setSourcePath('driver/src/ble_prov/app_prov_thread.c')
    appProvThreadSourceFile.setOutputName('app_prov_thread.c')
    appProvThreadSourceFile.setOverwrite(True)
    appProvThreadSourceFile.setDestPath('../../app_prov')
    appProvThreadSourceFile.setProjectPath('app_prov')
    appProvThreadSourceFile.setType('SOURCE')
    appProvThreadSourceFile.setMarkup(True)
    appProvThreadSourceFile.setEnabled(False)     

    # Add app_error_defs.h - static file
    appErrorHeaderFile = provBle.createFileSymbol(None, None)
    appErrorHeaderFile.setSourcePath('driver/src/app_error_defs.h')
    appErrorHeaderFile.setOutputName('app_error_defs.h')
    appErrorHeaderFile.setOverwrite(True)
    appErrorHeaderFile.setDestPath('../../')
    appErrorHeaderFile.setProjectPath('')
    appErrorHeaderFile.setType('HEADER')
    appErrorHeaderFile.setEnabled(True)
    
      # Add app_ble_conn_handler.c
    appConnSourceFile = provBle.createFileSymbol(None, None)
    appConnSourceFile.setSourcePath('driver/src/app_ble_conn_handler.c')
    appConnSourceFile.setOutputName('app_ble_conn_handler.c')
    appConnSourceFile.setOverwrite(True)
    appConnSourceFile.setDestPath('../../')
    appConnSourceFile.setType('SOURCE')
    appConnSourceFile.setMarkup(True)
    appConnSourceFile.setEnabled(True)
    
    # Add app_ble_conn_handler.h
    appConnHeaderFile = provBle.createFileSymbol(None, None)
    appConnHeaderFile.setSourcePath('driver/src/app_ble_conn_handler.h')
    appConnHeaderFile.setOutputName('app_ble_conn_handler.h')
    appConnHeaderFile.setOverwrite(True)
    appConnHeaderFile.setDestPath('../../')
    appConnHeaderFile.setType('HEADER')
    appConnHeaderFile.setMarkup(True)
    appConnHeaderFile.setEnabled(True)
    
    global appThreadCommonHeaderFile
    appThreadCommonHeaderFile = provBle.createFileSymbol(None, None)
    appThreadCommonHeaderFile.setSourcePath('driver/templates/ble_prov/app_thread/app_thread_common.h.ftl')
    appThreadCommonHeaderFile.setOutputName('app_thread_common.h')
    appThreadCommonHeaderFile.setOverwrite(True)
    appThreadCommonHeaderFile.setDestPath('../../app_thread')
    appThreadCommonHeaderFile.setProjectPath('app_thread')
    appThreadCommonHeaderFile.setType('HEADER')
    appThreadCommonHeaderFile.setEnabled(False)
    appThreadCommonHeaderFile.setMarkup(True)

    global appThreadCommonSourceFile
    appThreadCommonSourceFile = provBle.createFileSymbol(None, None)
    appThreadCommonSourceFile.setSourcePath('driver/templates/ble_prov/app_thread/app_thread_common.c.ftl')
    appThreadCommonSourceFile.setOutputName('app_thread_common.c')
    appThreadCommonSourceFile.setOverwrite(True)
    appThreadCommonSourceFile.setDestPath('../../app_thread')
    appThreadCommonSourceFile.setProjectPath('app_thread')
    appThreadCommonSourceFile.setType('SOURCE')
    appThreadCommonSourceFile.setEnabled(False)
    appThreadCommonSourceFile.setMarkup(True)

    global appThreadAppHeaderFile
    appThreadAppHeaderFile = provBle.createFileSymbol(None, None)
    appThreadAppHeaderFile.setSourcePath('driver/templates/ble_prov/app_thread/app_thread.h.ftl')
    appThreadAppHeaderFile.setOutputName('app_thread.h')
    appThreadAppHeaderFile.setOverwrite(True)
    appThreadAppHeaderFile.setDestPath('../../')
    appThreadAppHeaderFile.setType('HEADER')
    appThreadAppHeaderFile.setEnabled(False)
    appThreadAppHeaderFile.setMarkup(True)

    global appThreadAppSourceFile
    appThreadAppSourceFile = provBle.createFileSymbol(None, None)
    appThreadAppSourceFile.setSourcePath('driver/templates/ble_prov/app_thread/app_thread.c.ftl')
    appThreadAppSourceFile.setOutputName('app_thread.c')
    appThreadAppSourceFile.setOverwrite(True)
    appThreadAppSourceFile.setDestPath('../../')
    appThreadAppSourceFile.setType('SOURCE')
    appThreadAppSourceFile.setEnabled(False)
    appThreadAppSourceFile.setMarkup(True)
    
    global appIdleTaskSourceFile
    appIdleTaskSourceFile = provBle.createFileSymbol(None, None)
    appIdleTaskSourceFile.setSourcePath('driver/src/thread_coap/app_idle_task.c')
    appIdleTaskSourceFile.setOutputName('app_idle_task.c')
    appIdleTaskSourceFile.setOverwrite(True)
    appIdleTaskSourceFile.setDestPath('../../')
    appIdleTaskSourceFile.setType('SOURCE')
    appIdleTaskSourceFile.setEnabled(False)
    
    #To configure for Thread
    configForThread()