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

def update_DISParamters():
    disComponent = Database.getComponentByID("SERVICE_DIS")
    if (disComponent != None):
        disIDEn = disComponent.getSymbolByID("DIS_FW_REV_ENABLE")
        disIDEn.setValue(True)
        disFWver = disComponent.getSymbolByID("DIS_FW_REV_STRING")
        if ( disFWver.getValue() == "Firmware"):
            disFWver.setValue("1.0.0.0")
            
def update_OTAParamters():
    otaComponent = Database.getComponentByID("PROFILE_OTAP")
    if (otaComponent != None):
        otaIDEn = otaComponent.getSymbolByID("OTAP_BOOL_SERVER")
        otaIDEn.setValue(True)            

        
def update_TimerParamters():
    timerComponent = Database.getComponentByID("app_timer")
    if (timerComponent != None):
        timerID = timerComponent.getSymbolByID("APP_TIMER_ID0")
        timerID.setValue("APP_TIMER_OTA_TIMEOUT")
        timerID = timerComponent.getSymbolByID("APP_TIMER_ID1")
        timerID.setValue("APP_TIMER_OTA_REBOOT")    

def update_BZparamters():
    bleStackComponent = Database.getComponentByID("BLE_STACK_LIB")
    if (bleStackComponent != None):
        if (bleStackComponent.getSymbolValue("GAP_ADV_DATA_LOCAL_NAME_EN") == True):
            advDataLocalNameEN = bleStackComponent.getSymbolByID('GAP_ADV_DATA_LOCAL_NAME_EN')
            advDataLocalNameEN.setValue(False)
        if (bleStackComponent.getSymbolValue("GAP_ADV_DATA_SERVICE_DATA_EN") == False):
            advSrvDataEN = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_DATA_EN')
            advSrvDataEN.setValue(True)
            advSrvDataUUID = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_UUID')
            advSrvDataUUID.setValue("FEDA")
            advSrvDataVal = bleStackComponent.getSymbolByID('GAP_ADV_DATA_SERVICE_DATA')
            advSrvDataVal.setValue("FFFF")        

def update_Bootloaderparamters():
    blComponent = Database.getComponentByID("BootloaderServices")
    if (blComponent != None):
        if (blComponent.getSymbolValue("APP_FW_SIGN_VERIFY") == False):
            signVerify = blComponent.getSymbolByID('APP_FW_SIGN_VERIFY')
            signVerify.setValue(True)


def onAttachmentConnected(source, target):
    update_TimerParamters()
    update_DISParamters()
    update_BZparamters()
    update_Bootloaderparamters()    

def onAttachmentDisconnected(source, target):
    Log.writeInfoMessage('BLE OTA:onAttachmentDisconnected: source = {} remote = {}'.format(source["component"].getID(), target["component"].getID()))

def finalizeComponent(ble_ota): 
    #result = Database.connectDependencies([['pic32cx_bz2_devsupport', 'Bootloader_Service_Dependency', 'BootloaderServices', 'PIC32CX_BZ2_BOOTLOADER_SERVICES']])  
    update_TimerParamters()
    update_DISParamters()   
    update_BZparamters()
    update_Bootloaderparamters()

def modifyImageDecryDependency(symbol, event):
    symbol.setVisible(event["value"])
    requiredComponents = ['lib_crypto', 'lib_wolfcrypt']
    Database.activateComponents(["lib_crypto","lib_wolfcrypt"])
    coreComponent = Database.getComponentByID("core")
    if (coreComponent != None):
        Database.setSymbolValue("core", "AES_CLOCK_ENABLE", True)
     

def modifyImageIDcheckDependency(symbol, event):
    symbol.setVisible(event["value"])
            

def instantiateComponent(ble_ota):
    print('ble_ota')
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    processor = Variables.get("__PROCESSOR")
    print processor

    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
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
                          } 
    deviceFamily = ble_ota.createStringSymbol("DEVICE_FAM", None)
    deviceFamily.setVisible(False)
    
    if( processor in pic32cx_bz2_family):        
        deviceFamily.setValue("BZ2")
    if( processor in pic32cx_bz3_family):        
        deviceFamily.setValue("BZ3")
    if( processor in pic32cx_bz6_family):        
        deviceFamily.setValue("BZ6")

    print('HarmonyCore.ENABLE_APP_FILE = {}'.format(str(Database.getSymbolValue("HarmonyCore", 'ENABLE_APP_FILE'))))
    print('HarmonyCore.ENABLE_OSAL = {}'.format(str(Database.getSymbolValue("HarmonyCore", 'ENABLE_OSAL'))))
    print('FreeRTOS.FREERTOS_USE_QUEUE_SETS = {}'.format(str(Database.getSymbolValue("FreeRTOS", 'FREERTOS_USE_QUEUE_SETS'))))
    
    ble_ota.addDependency('BLE_DIS_Dependency', 'BLE_DIS', 'BLE DIS', True, True)
    ble_ota.addDependency('RCON_Module', 'RCON', 'RCON', True, False)

    res = Database.activateComponents(["PROFILE_OTAP","app_timer","SERVICE_DIS","rcon","BootloaderServices"])


    print('Config Name: {} processor: {}'.format(configName, processor))    
   

    enableImageIDCheckbox = ble_ota.createBooleanSymbol("FLASH_IMAGE_ID_ENABLE", None)
    enableImageIDCheckbox.setLabel("Enable Flash Image ID")
    enableImageIDCheckbox.setDescription("This option can be used to enable checking Flash Image sent in Header")
    enableImageIDCheckbox.setDefaultValue(False)
    enableImageIDCheckbox.setVisible(True)
    enableImageIDCheckbox.setReadOnly(False)

    appImageID = ble_ota.createStringSymbol("FLASH_IMAGE_ID", None)
    appImageID.setLabel("Flash Image ID")
    appImageID.setVisible(False)    
    appImageID.setDescription("Flash Image ID in OTA Header")    
    appImageID.setDefaultValue("0x9B000000")
    appImageID.setDependencies(modifyImageIDcheckDependency, ["FLASH_IMAGE_ID_ENABLE"])
    
    # Enable OTA Decryption in MHC - By default it is disabled
    #global enableDecCheckbox
    enableDecCheckbox = ble_ota.createBooleanSymbol("IMAGE_DECRYPTION_ENABLE", None)
    enableDecCheckbox.setLabel("Enable Image Decryption")
    enableDecCheckbox.setDescription("This option can be used for decryption if OTA image is encrypted")
    enableDecCheckbox.setDefaultValue(False)
    enableDecCheckbox.setVisible(True)
    enableDecCheckbox.setReadOnly(False)


    eccEncKey = ble_ota.createStringSymbol("ENCRYPTION_KEY", None)
    eccEncKey.setLabel("AES Key")
    eccEncKey.setVisible(False)
    eccEncKey.setDefaultValue('0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99')
    eccEncKey.setDescription("AES 128 Key used for Image Decryption")   
    eccEncKey.setDependencies(modifyImageDecryDependency, ["IMAGE_DECRYPTION_ENABLE"])
    
    eccEncKey = ble_ota.createStringSymbol("INIT_VECTOR", None)
    eccEncKey.setLabel("Init Vector")
    eccEncKey.setVisible(False)
    eccEncKey.setDefaultValue('0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00')
    eccEncKey.setDescription("AES 128 Initialisation Vector")   
    eccEncKey.setDependencies(modifyImageDecryDependency, ["IMAGE_DECRYPTION_ENABLE"])    
    
    # Add app_ota_handler.c
    appOtaSourceFile = ble_ota.createFileSymbol(None, None)
    appOtaSourceFile.setSourcePath('driver/templates/app_ota_handler.c.ftl')
    appOtaSourceFile.setOutputName('app_ota_handler.c')
    appOtaSourceFile.setOverwrite(True)
    appOtaSourceFile.setDestPath('../../app_ota')
    appOtaSourceFile.setProjectPath('app_ota')
    appOtaSourceFile.setType('SOURCE')
    appOtaSourceFile.setMarkup(True)
    appOtaSourceFile.setEnabled(True)
    
    # Add app_ota_handler.h
    appOtaHeaderFile = ble_ota.createFileSymbol(None, None)
    appOtaHeaderFile.setSourcePath('driver/templates/app_ota_handler.h.ftl')
    appOtaHeaderFile.setOutputName('app_ota_handler.h')
    appOtaHeaderFile.setOverwrite(True)
    appOtaHeaderFile.setDestPath('../../app_ota')
    appOtaHeaderFile.setProjectPath('app_ota')
    appOtaHeaderFile.setType('HEADER')
    appOtaHeaderFile.setMarkup(True)
    appOtaHeaderFile.setEnabled(True)
    
    # Add app_ble_conn_handler.c
    appOtaSourceFile = ble_ota.createFileSymbol(None, None)
    appOtaSourceFile.setSourcePath('driver/src/app_ble_conn_handler.c')
    appOtaSourceFile.setOutputName('app_ble_conn_handler.c')
    appOtaSourceFile.setOverwrite(True)
    appOtaSourceFile.setDestPath('../../')
    appOtaSourceFile.setType('SOURCE')
    appOtaSourceFile.setMarkup(True)
    appOtaSourceFile.setEnabled(True)
    
    # Add app_ble_conn_handler.h
    appOtaHeaderFile = ble_ota.createFileSymbol(None, None)
    appOtaHeaderFile.setSourcePath('driver/src/app_ble_conn_handler.h')
    appOtaHeaderFile.setOutputName('app_ble_conn_handler.h')
    appOtaHeaderFile.setOverwrite(True)
    appOtaHeaderFile.setDestPath('../../')
    appOtaHeaderFile.setType('HEADER')
    appOtaHeaderFile.setMarkup(True)
    appOtaHeaderFile.setEnabled(True)    