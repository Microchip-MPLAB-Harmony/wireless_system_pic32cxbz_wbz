"""*****************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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

####################################################################################
########################Configuration Callback######################################
####################################################################################

def threadCoapConfigcallback(symbol,event):
    # print("openthreadMtdConfigcallback",symbol,event)
    symbolID = event["id"]
    value = event["value"]
    
    if symbolID == "THREAD_DEVICE_ROLE_CONFIG":
        if value == 0:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_DEVICE_ROLE_CONFIG_1",0)
            threadsedenableconfig.setReadOnly(True)
            
        elif value == 1:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_DEVICE_ROLE_CONFIG_1",1)
            threadsedenableconfig.setReadOnly(False)
    
    elif symbolID == "COAP_DEVICE_ROLE_CONFIG":
        if value == 0:
            appCoapClientHeaderFile.setEnabled(True)
            appCoapClientSourceFile.setEnabled(True)
            appCoapServerHeaderFile.setEnabled(False)
            appCoapServerSourceFile.setEnabled(False)
            
        elif value == 1:
            appCoapServerHeaderFile.setEnabled(True)
            appCoapServerSourceFile.setEnabled(True)
            appCoapClientHeaderFile.setEnabled(False)
            appCoapClientSourceFile.setEnabled(False)
    
    elif symbolID == "COAP_RESOUCES_NUMBER_CONFIG":
        for x in range(1, 5):
            if x < value:
                if coapresourceconfigMenu[x].getVisible() == False:
                    coapresourceconfigMenu[x].setVisible(True)
            elif x >= value:
                if coapresourceconfigMenu[x].getVisible() == True:
                    coapresourceconfigMenu[x].setVisible(False)
            
    elif symbolID == "THREAD_SLEEP_ENABLE":
        if value == True:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_SLEEP_ENABLE",True)
            appIdleTaskSourceFile.setEnabled(True)
        elif value == False:
            Database.setSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_SLEEP_ENABLE",False)
            appIdleTaskSourceFile.setEnabled(False)


#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPONENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def instantiateComponent(threadcoap):
    print("Thread CoAP Application Service")
    
    global configName
    configName = Variables.get("__CONFIGURATION_NAME")

    print configName
    
    global requiredComponents
    requiredComponents = [
        "OPEN_THREAD"
    ]
    
    res = Database.activateComponents(requiredComponents)

    remoteComponent = Database.getComponentByID("OPEN_THREAD")
    if (remoteComponent):
        symbol = remoteComponent.getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_1")
        symbol1 = remoteComponent.getSymbolByID("OPEN_THREAD_MTD_SLEEP_ENABLE")
        symbol.setReadOnly(True)
        symbol1.setReadOnly(True)

    global threaddeviceroleconfig
    threaddeviceroleconfig = threadcoap.createKeyValueSetSymbol("THREAD_DEVICE_ROLE_CONFIG", None)
    threaddeviceroleconfig.setLabel("Thread Device Role")
    threaddeviceroleconfig.addKey("FTD", "FTD", "FTD")
    threaddeviceroleconfig.addKey("MTD", "MTD", "MTD")
    threaddeviceroleconfig.setDefaultValue(0)
    threaddeviceroleconfig.setOutputMode("Value")
    threaddeviceroleconfig.setDisplayMode("Description")
    threaddeviceroleconfig.setDescription("Open Thread Device Role Configuration")
    threaddeviceroleconfig.setVisible(True)
    threaddeviceroleconfig.setDependencies(threadCoapConfigcallback,["THREAD_DEVICE_ROLE_CONFIG"])

    global threadsedenableconfig
    threadsedenableconfig = threadcoap.createBooleanSymbol("THREAD_SLEEP_ENABLE", None)
    threadsedenableconfig.setLabel("Enable As Sleep End Device")
    threadsedenableconfig.setDefaultValue(False)
    threadsedenableconfig.setVisible(True)
    threadsedenableconfig.setDescription("Option to enable the device as SED")
    threadsedenableconfig.setReadOnly(True)
    threadsedenableconfig.setDependencies(threadCoapConfigcallback,["THREAD_SLEEP_ENABLE"])

    global coapdeviceroleconfig
    coapdeviceroleconfig = threadcoap.createKeyValueSetSymbol("COAP_DEVICE_ROLE_CONFIG", None)
    coapdeviceroleconfig.setLabel("CoAP Device Role")
    coapdeviceroleconfig.addKey("COAP_CLIENT", "COAP_CLIENT", "COAP_CLIENT")
    coapdeviceroleconfig.addKey("COAP_SERVER", "COAP_SERVER", "COAP_SERVER")
    coapdeviceroleconfig.setDefaultValue(0)
    coapdeviceroleconfig.setOutputMode("Value")
    coapdeviceroleconfig.setDisplayMode("Description")
    coapdeviceroleconfig.setDescription("CoAP Role Configuration")
    coapdeviceroleconfig.setVisible(True)
    coapdeviceroleconfig.setDependencies(threadCoapConfigcallback,["COAP_DEVICE_ROLE_CONFIG"])
    
    global coapportconfig
    coapportconfig = threadcoap.createIntegerSymbol("COAP_PORT_CONFIG", None)
    coapportconfig.setLabel("CoAP Port")
    coapportconfig.setDefaultValue(5683)
    coapportconfig.setDescription("CoAP Port Configuration")
    coapportconfig.setVisible(True)

    global coapnumresourceconfig
    coapnumresourceconfig = threadcoap.createIntegerSymbol("COAP_RESOUCES_NUMBER_CONFIG", None)
    coapnumresourceconfig.setLabel("Number of CoAP resources")
    coapnumresourceconfig.setDefaultValue(1)
    coapnumresourceconfig.setMin(1)
    coapnumresourceconfig.setMax(5)
    coapnumresourceconfig.setVisible(True)
    coapnumresourceconfig.setDescription("Number of CoAP resources")
    coapnumresourceconfig.setDependencies(threadCoapConfigcallback,["COAP_RESOUCES_NUMBER_CONFIG"])

    global coapresourceconfigMenu
    coapresourceconfigMenu = []
    coapresourceconfigMenu.append(threadcoap.createMenuSymbol("COAP_RESOURCE1_CONFIG_MENU", coapnumresourceconfig))
    coapresourceconfigMenu[0].setLabel("Resource1")
    coapresourceconfigMenu[0].setVisible(True)

    global coapresourcenameconfig
    coapresourcenameconfig = []
    coapresourcenameconfig.append(threadcoap.createStringSymbol("RESOURCE_ID1_CONFIG",coapresourceconfigMenu[0]))
    coapresourcenameconfig[0].setLabel("Resource Name")
    coapresourcenameconfig[0].setDefaultValue("APP_RESOURCE_ID1")
    coapresourcenameconfig[0].setVisible(True)

   
    global coapresourceuriconfig
    coapresourceuriconfig = []
    coapresourceuriconfig.append(threadcoap.createStringSymbol("RESOURCE_URI1_CONFIG",coapresourceconfigMenu[0]))
    coapresourceuriconfig[0].setLabel("Resource URI")
    coapresourceuriconfig[0].setDefaultValue("Resourceuri1")
    coapresourceuriconfig[0].setVisible(True)

    coapresourceconfigMenu.append(threadcoap.createMenuSymbol("COAP_RESOURCE2_CONFIG_MENU", coapnumresourceconfig))
    coapresourceconfigMenu[1].setLabel("Resource2")
    coapresourceconfigMenu[1].setVisible(False)

    coapresourcenameconfig.append(threadcoap.createStringSymbol("RESOURCE_ID2_CONFIG",coapresourceconfigMenu[1]))
    coapresourcenameconfig[1].setLabel("Resource Name")
    coapresourcenameconfig[1].setDefaultValue("APP_RESOURCE_ID2")
    coapresourcenameconfig[1].setVisible(True)

    coapresourceuriconfig.append(threadcoap.createStringSymbol("RESOURCE_URI2_CONFIG",coapresourceconfigMenu[1]))
    coapresourceuriconfig[1].setLabel("Resource URI")
    coapresourceuriconfig[1].setDefaultValue("Resourceuri2")
    coapresourceuriconfig[1].setVisible(True)

    coapresourceconfigMenu.append(threadcoap.createMenuSymbol("COAP_RESOURCE3_CONFIG_MENU", coapnumresourceconfig))
    coapresourceconfigMenu[2].setLabel("Resource3")
    coapresourceconfigMenu[2].setVisible(False)

    coapresourcenameconfig.append(threadcoap.createStringSymbol("RESOURCE_ID3_CONFIG",coapresourceconfigMenu[2]))
    coapresourcenameconfig[2].setLabel("Resource Name")
    coapresourcenameconfig[2].setDefaultValue("APP_RESOURCE_ID3")
    coapresourcenameconfig[2].setVisible(True)

    coapresourceuriconfig.append(threadcoap.createStringSymbol("RESOURCE_URI3_CONFIG",coapresourceconfigMenu[2]))
    coapresourceuriconfig[2].setLabel("Resource URI")
    coapresourceuriconfig[2].setDefaultValue("Resourceuri3")
    coapresourceuriconfig[2].setVisible(True)

    coapresourceconfigMenu.append(threadcoap.createMenuSymbol("COAP_RESOURCE4_CONFIG_MENU", coapnumresourceconfig))
    coapresourceconfigMenu[3].setLabel("Resource4")
    coapresourceconfigMenu[3].setVisible(False)

    coapresourcenameconfig.append(threadcoap.createStringSymbol("RESOURCE_ID4_CONFIG",coapresourceconfigMenu[3]))
    coapresourcenameconfig[3].setLabel("Resource Name")
    coapresourcenameconfig[3].setDefaultValue("APP_RESOURCE_ID4")
    coapresourcenameconfig[3].setVisible(True)

    coapresourceuriconfig.append(threadcoap.createStringSymbol("RESOURCE_URI4_CONFIG",coapresourceconfigMenu[3]))
    coapresourceuriconfig[3].setLabel("Resource URI")
    coapresourceuriconfig[3].setDefaultValue("Resourceuri4")
    coapresourceuriconfig[3].setVisible(True)

    coapresourceconfigMenu.append(threadcoap.createMenuSymbol("COAP_RESOURCE5_CONFIG_MENU", coapnumresourceconfig))
    coapresourceconfigMenu[4].setLabel("Resource5")
    coapresourceconfigMenu[4].setVisible(False)

    coapresourcenameconfig.append(threadcoap.createStringSymbol("RESOURCE_ID5_CONFIG",coapresourceconfigMenu[4]))
    coapresourcenameconfig[4].setLabel("Resource Name")
    coapresourcenameconfig[4].setDefaultValue("APP_RESOURCE_ID5")
    coapresourcenameconfig[4].setVisible(True)

    coapresourceuriconfig.append(threadcoap.createStringSymbol("RESOURCE_URI5_CONFIG",coapresourceconfigMenu[4]))
    coapresourceuriconfig[4].setLabel("Resource URI")
    coapresourceuriconfig[4].setDefaultValue("Resourceuri5")
    coapresourceuriconfig[4].setVisible(True)


    # Add app_coap_common.h - generated file ftl
    appCoapCommonHeaderFile = threadcoap.createFileSymbol(None, None)
    appCoapCommonHeaderFile.setSourcePath('driver/templates/thread_coap/app_coap_common.h.ftl')
    appCoapCommonHeaderFile.setOutputName('app_coap_common.h')
    appCoapCommonHeaderFile.setOverwrite(True)
    appCoapCommonHeaderFile.setDestPath('../../app_coap')
    appCoapCommonHeaderFile.setProjectPath('app_coap')
    appCoapCommonHeaderFile.setType('HEADER')
    appCoapCommonHeaderFile.setEnabled(True)
    appCoapCommonHeaderFile.setMarkup(True)

    # Add app_coap_common.c - static file
    appCoapCommonSourceFile = threadcoap.createFileSymbol(None, None)
    appCoapCommonSourceFile.setSourcePath('driver/src/thread_coap/app_coap_common.c')
    appCoapCommonSourceFile.setOutputName('app_coap_common.c')
    appCoapCommonSourceFile.setOverwrite(True)
    appCoapCommonSourceFile.setDestPath('../../app_coap')
    appCoapCommonSourceFile.setProjectPath('app_coap')
    appCoapCommonSourceFile.setType('SOURCE')
    appCoapCommonSourceFile.setEnabled(True)

    # Add app_coap_client.h - static file
    global appCoapClientHeaderFile
    appCoapClientHeaderFile = threadcoap.createFileSymbol(None, None)
    appCoapClientHeaderFile.setSourcePath('driver/src/thread_coap/app_coap_client.h')
    appCoapClientHeaderFile.setOutputName('app_coap_client.h')
    appCoapClientHeaderFile.setOverwrite(True)
    appCoapClientHeaderFile.setDestPath('../../app_coap')
    appCoapClientHeaderFile.setProjectPath('app_coap')
    appCoapClientHeaderFile.setType('HEADER')
    appCoapClientHeaderFile.setEnabled(True)

    # Add app_coap_client.c - generated file ftl
    global appCoapClientSourceFile
    appCoapClientSourceFile = threadcoap.createFileSymbol(None, None)
    appCoapClientSourceFile.setSourcePath('driver/templates/thread_coap/app_coap_client.c.ftl')
    appCoapClientSourceFile.setOutputName('app_coap_client.c')
    appCoapClientSourceFile.setOverwrite(True)
    appCoapClientSourceFile.setDestPath('../../app_coap')
    appCoapClientSourceFile.setProjectPath('app_coap')
    appCoapClientSourceFile.setType('SOURCE')
    appCoapClientSourceFile.setEnabled(True)
    appCoapClientSourceFile.setMarkup(True)

    # Add app_coap_server.h - - static file
    global appCoapServerHeaderFile
    appCoapServerHeaderFile = threadcoap.createFileSymbol(None, None)
    appCoapServerHeaderFile.setSourcePath('driver/src/thread_coap/app_coap_server.h')
    appCoapServerHeaderFile.setOutputName('app_coap_server.h')
    appCoapServerHeaderFile.setOverwrite(True)
    appCoapServerHeaderFile.setDestPath('../../app_coap')
    appCoapServerHeaderFile.setProjectPath('app_coap')
    appCoapServerHeaderFile.setType('HEADER')
    appCoapServerHeaderFile.setEnabled(False)

    # Add app_coap_server.c - generated file ftl
    global appCoapServerSourceFile
    appCoapServerSourceFile = threadcoap.createFileSymbol(None, None)
    appCoapServerSourceFile.setSourcePath('driver/templates/thread_coap/app_coap_server.c.ftl')
    appCoapServerSourceFile.setOutputName('app_coap_server.c')
    appCoapServerSourceFile.setOverwrite(True)
    appCoapServerSourceFile.setDestPath('../../app_coap')
    appCoapServerSourceFile.setProjectPath('app_coap')
    appCoapServerSourceFile.setType('SOURCE')
    appCoapServerSourceFile.setEnabled(False)
    appCoapServerSourceFile.setMarkup(True)

    appCoapAppHeaderFile = threadcoap.createFileSymbol(None, None)
    appCoapAppHeaderFile.setSourcePath('driver/templates/thread_coap/app_coap.h.ftl')
    appCoapAppHeaderFile.setOutputName('app_coap.h')
    appCoapAppHeaderFile.setOverwrite(True)
    appCoapAppHeaderFile.setDestPath('../../')
    appCoapAppHeaderFile.setType('HEADER')
    appCoapAppHeaderFile.setEnabled(True)
    appCoapAppHeaderFile.setMarkup(True)

    appCoapAppSourceFile = threadcoap.createFileSymbol(None, None)
    appCoapAppSourceFile.setSourcePath('driver/templates/thread_coap/app_coap.c.ftl')
    appCoapAppSourceFile.setOutputName('app_coap.c')
    appCoapAppSourceFile.setOverwrite(True)
    appCoapAppSourceFile.setDestPath('../../')
    appCoapAppSourceFile.setType('SOURCE')
    appCoapAppSourceFile.setEnabled(True)
    appCoapAppSourceFile.setMarkup(True)

    appThreadCommonHeaderFile = threadcoap.createFileSymbol(None, None)
    appThreadCommonHeaderFile.setSourcePath('driver/templates/thread_coap/app_thread_common.h.ftl')
    appThreadCommonHeaderFile.setOutputName('app_thread_common.h')
    appThreadCommonHeaderFile.setOverwrite(True)
    appThreadCommonHeaderFile.setDestPath('../../app_thread')
    appThreadCommonHeaderFile.setProjectPath('app_thread')
    appThreadCommonHeaderFile.setType('HEADER')
    appThreadCommonHeaderFile.setEnabled(True)
    appThreadCommonHeaderFile.setMarkup(True)

    appThreadCommonSourceFile = threadcoap.createFileSymbol(None, None)
    appThreadCommonSourceFile.setSourcePath('driver/templates/thread_coap/app_thread_common.c.ftl')
    appThreadCommonSourceFile.setOutputName('app_thread_common.c')
    appThreadCommonSourceFile.setOverwrite(True)
    appThreadCommonSourceFile.setDestPath('../../app_thread')
    appThreadCommonSourceFile.setProjectPath('app_thread')
    appThreadCommonSourceFile.setType('SOURCE')
    appThreadCommonSourceFile.setEnabled(True)
    appThreadCommonSourceFile.setMarkup(True)

    appThreadAppHeaderFile = threadcoap.createFileSymbol(None, None)
    appThreadAppHeaderFile.setSourcePath('driver/templates/thread_coap/app_thread.h.ftl')
    appThreadAppHeaderFile.setOutputName('app_thread.h')
    appThreadAppHeaderFile.setOverwrite(True)
    appThreadAppHeaderFile.setDestPath('../../')
    appThreadAppHeaderFile.setType('HEADER')
    appThreadAppHeaderFile.setEnabled(True)
    appThreadAppHeaderFile.setMarkup(True)

    appThreadAppSourceFile = threadcoap.createFileSymbol(None, None)
    appThreadAppSourceFile.setSourcePath('driver/templates/thread_coap/app_thread.c.ftl')
    appThreadAppSourceFile.setOutputName('app_thread.c')
    appThreadAppSourceFile.setOverwrite(True)
    appThreadAppSourceFile.setDestPath('../../')
    appThreadAppSourceFile.setType('SOURCE')
    appThreadAppSourceFile.setEnabled(True)
    appThreadAppSourceFile.setMarkup(True)

    appHeaderFile = threadcoap.createFileSymbol(None, None)
    appHeaderFile.setSourcePath('/driver/templates/thread_coap/app.h.ftl')
    appHeaderFile.setOutputName('app.h')
    appHeaderFile.setOverwrite(False)
    appHeaderFile.setDestPath('../../')
    appHeaderFile.setType('HEADER')
    appHeaderFile.setEnabled(True)
    appHeaderFile.setMarkup(True)

    appSourceFile = threadcoap.createFileSymbol(None, None)
    appSourceFile.setSourcePath('/driver/templates/thread_coap/app.c.ftl')
    appSourceFile.setOutputName('app.c')
    appSourceFile.setOverwrite(False)
    appSourceFile.setDestPath('../../')
    appSourceFile.setType('SOURCE')
    appSourceFile.setEnabled(True)
    appSourceFile.setMarkup(True)
    
    global appIdleTaskSourceFile
    appIdleTaskSourceFile = threadcoap.createFileSymbol(None, None)
    appIdleTaskSourceFile.setSourcePath('driver/src/thread_coap/app_idle_task.c')
    appIdleTaskSourceFile.setOutputName('app_idle_task.c')
    appIdleTaskSourceFile.setOverwrite(True)
    appIdleTaskSourceFile.setDestPath('../../')
    appIdleTaskSourceFile.setType('SOURCE')
    appIdleTaskSourceFile.setEnabled(False)

def onAttachmentDisconnected(source, target):
        remoteComponent = Database.getComponentByID("OPEN_THREAD")
        if (remoteComponent):
            symbol = remoteComponent.getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_1")
            symbol1 = remoteComponent.getSymbolByID("OPEN_THREAD_MTD_SLEEP_ENABLE")
            symbol.setReadOnly(False)
            symbol1.setReadOnly(False)