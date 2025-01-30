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

            
def onAttachmentConnected(source, target):
    print('APP Timer --> onAttachmentConnected source= {}'.format(str(source)))
    print('APP Timer --> onAttachmentConnected target= {}'.format(str(target)))
    # if (source['id'] == 'App_Timer_Capability'):
        # Database.sendMessage("app_service", "APP_TIMER_SERVICE", {"isEnabled":True})
    useTimerComponent = Database.getComponentByID("FreeRTOS")
    if (useTimerComponent != None):
        useTimerChoice = useTimerComponent.getSymbolByID("FREERTOS_USE_TIMERS")
        useTimerChoice.setValue(True)

def onAttachmentDisconnected(source, target):
    print('APP Timer --> onAttachmentDisconnected source= {}'.format(str(source)))
    print('APP Timer --> onAttachmentDisconnected target= {}'.format(str(target)))
    # if (source['id'] == 'App_Timer_Capability'):
        # Database.sendMessage("app_service", "APP_TIMER_SERVICE", {"isEnabled":False})
    useTimerComponent = Database.getComponentByID("FreeRTOS")
    if (useTimerComponent != None):
        useTimerChoice = useTimerComponent.getSymbolByID("FREERTOS_USE_TIMERS")
        useTimerChoice.setValue(False)

def finalizeComponent(app_Timer_Component):
    print('App Timer -> finalizeComponent - {}'.format(str(app_Timer_Component)))
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
                          'PIC32WM_BZ6204',
                          }  
    processor = Variables.get("__PROCESSOR")
    if( processor in pic32cx_bz2_family):
        result = Database.connectDependencies([['app_timer', 'PIC32CX_BZ2_DevSupport_Dependency', 'pic32cx_bz2_devsupport', 'Device_Support_Capability']])
    if( processor in pic32cx_bz3_family):
        result = Database.connectDependencies([['app_timer', 'PIC32CX_BZ3_DevSupport_Dependency', 'pic32cx_bz3_devsupport', 'Device_Support_Capability']])
    if( processor in pic32cx_bz6_family):
        result = Database.connectDependencies([['app_timer', 'PIC32CX_BZ6_DevSupport_Dependency', 'pic32cx_bz6_devsupport', 'Device_Support_Capability']])
    print('App Timer -> finalizeComponent - {}'.format(str(app_Timer_Component)))

def instantiateComponent(app_Timer_Component):
    print('App Timer -> instantiateComponent - {}'.format(str(app_Timer_Component)))
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
                          'PIC32WM_BZ6204',                          
                          }  
    
    if( processor in pic32cx_bz2_family):
        Database.activateComponents(["pic32cx_bz2_devsupport"])
    if( processor in pic32cx_bz3_family):
        Database.activateComponents(["pic32cx_bz3_devsupport"])
    if( processor in pic32cx_bz6_family):
        Database.activateComponents(["pic32cx_bz6_devsupport"])
    

    useTimerComponent = Database.getComponentByID("FreeRTOS")
    if (useTimerComponent != None):
        useTimerChoice = useTimerComponent.getSymbolByID("FREERTOS_USE_TIMERS")
        useTimerChoice.setValue(True)

    appTimerEnable = app_Timer_Component.createBooleanSymbol("APP_TIMER_ENABLE", None)
    appTimerEnable.setLabel("Enable App Timer")
    appTimerEnable.setDefaultValue(True)
    appTimerEnable.setVisible(False)

    # Add app_timer.c - generated file ftl
    appTimerSourceFile = app_Timer_Component.createFileSymbol(None, None)
    appTimerSourceFile.setSourcePath('driver/templates/app_timer.c.ftl')
    appTimerSourceFile.setOutputName('app_timer.c')
    appTimerSourceFile.setOverwrite(True)
    appTimerSourceFile.setDestPath('../../app_timer')
    appTimerSourceFile.setProjectPath('app_timer')
    appTimerSourceFile.setType('SOURCE')
    appTimerSourceFile.setEnabled(True)
    appTimerSourceFile.setMarkup(True) 

    # Add app_timer.h - static file ftl
    appTimerHeaderFile = app_Timer_Component.createFileSymbol(None, None)
    appTimerHeaderFile.setSourcePath('driver/templates/app_timer.h.ftl')
    appTimerHeaderFile.setOutputName('app_timer.h')
    appTimerHeaderFile.setOverwrite(True)
    appTimerHeaderFile.setDestPath('../../app_timer')
    appTimerHeaderFile.setProjectPath('app_timer')
    appTimerHeaderFile.setType('HEADER')
    appTimerHeaderFile.setEnabled(True)
    appTimerHeaderFile.setMarkup(True) 
    
    # Add app_error_defs.h - static file
    appErrorHeaderFile = app_Timer_Component.createFileSymbol(None, None)
    appErrorHeaderFile.setSourcePath('driver/src/app_error_defs.h')
    appErrorHeaderFile.setOutputName('app_error_defs.h')
    appErrorHeaderFile.setOverwrite(True)
    appErrorHeaderFile.setDestPath('../../')
    appErrorHeaderFile.setProjectPath('')
    appErrorHeaderFile.setType('HEADER')
    appErrorHeaderFile.setEnabled(True)
    
    # Device Name
    appTimerID0 = app_Timer_Component.createStringSymbol("APP_TIMER_ID0", None)
    appTimerID0.setLabel("APP TIMER ID0")
    appTimerID0.setDefaultValue("APP_TIMER_ID_0")
    appTimerID0.setVisible(True)
    appTimerID0.setReadOnly(False)
    print('app_timer --> appTimerID0 = {}'.format(str(appTimerID0)))
    
    appTimerID1 = app_Timer_Component.createStringSymbol("APP_TIMER_ID1", None)
    appTimerID1.setLabel("APP TIMER ID1")
    appTimerID1.setDefaultValue("APP_TIMER_ID_1")
    appTimerID1.setVisible(True)
    appTimerID1.setReadOnly(False)
    
    appTimerID2 = app_Timer_Component.createStringSymbol("APP_TIMER_ID2", None)
    appTimerID2.setLabel("APP TIMER ID2")
    appTimerID2.setDefaultValue("APP_TIMER_ID_2")
    appTimerID2.setVisible(True)
    appTimerID2.setReadOnly(False)
    
    appTimerID3 = app_Timer_Component.createStringSymbol("APP_TIMER_ID3", None)
    appTimerID3.setLabel("APP TIMER ID3")
    appTimerID3.setDefaultValue("APP_TIMER_ID_3")
    appTimerID3.setVisible(True)
    appTimerID3.setReadOnly(False)
    
    appTimerID4 = app_Timer_Component.createStringSymbol("APP_TIMER_ID4", None)
    appTimerID4.setLabel("APP TIMER ID4")
    appTimerID4.setDefaultValue("APP_TIMER_ID_4")
    appTimerID4.setVisible(True)
    appTimerID4.setReadOnly(False)
    
    appTimerID5 = app_Timer_Component.createStringSymbol("APP_TIMER_ID5", None)
    appTimerID5.setLabel("APP TIMER ID5")
    appTimerID5.setDefaultValue("APP_TIMER_ID_5")
    appTimerID5.setVisible(True)
    appTimerID5.setReadOnly(False)

    
    
