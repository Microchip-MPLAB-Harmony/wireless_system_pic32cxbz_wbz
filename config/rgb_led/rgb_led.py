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
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if (connectID == "RGB_LED_PWM_Dependency"):
        print('rgb_led_dependency')
        print remoteComponent
        tccinst = localComponent.getSymbolByID("TCC_INSTANCE")
        tccinst.setValue(remoteComponent.getID().upper())
        print tccinst.getValue()        
        if (remoteComponent != None):
            mode = remoteComponent.getSymbolByID("TCC_OPERATION_MODE")
            mode.setValue("Compare")
            stdby = remoteComponent.getSymbolByID("TCC_CTRLA_RUNSTDBY")
            stdby.setValue(True)
            wavemode = remoteComponent.getSymbolByID("TCC_COMPARE_WAVE_WAVEGEN")
            wavemode.setValue(2)
            doublebuf = remoteComponent.getSymbolByID("TCC_COMPARE_CTRLBSET_LUPD")
            doublebuf.setValue(False)           
            #coreComponent = Database.getComponentByID("core")
            #if (coreComponent != None):
                #refo = coreComponent.getSymbolByID("CONFIG_SYS_CLK_REFCLK3_ENABLE")
                #refo.setValue(True)
                #clksource = coreComponent.getSymbolByID("CONFIG_SYS_CLK_REFCLK_SOURCE3")                
                #clksource.setValue("POSC")
                #sleep = coreComponent.getSymbolByID("CONFIG_SYS_CLK_REFCLK_RSLP3")                
                #sleep.setValue(True)
                
    if (connectID == "RGB_LED_PWM_Dependency1"):
        print('rgb_led_dependency1')
        print remoteComponent
        tc2inst = localComponent.getSymbolByID("TC2_INSTANCE")
        tc2inst.setValue(remoteComponent.getID().upper())
        print tc2inst.getValue()        
        if (remoteComponent != None):
            mode = remoteComponent.getSymbolByID("TC_OPERATION_MODE")
            mode.setValue("Compare")
            stdby = remoteComponent.getSymbolByID("TC_CTRLA_RUNSTDBY")
            stdby.setValue(True)
            wavemode = remoteComponent.getSymbolByID("TC_COMPARE_WAVE_WAVEGEN")
            wavemode.setValue(2)
            
    if (connectID == "RGB_LED_PWM_Dependency2"):
        print('rgb_led_dependency2')
        print remoteComponent
        tc3inst = localComponent.getSymbolByID("TC3_INSTANCE")
        tc3inst.setValue(remoteComponent.getID().upper())
        print tc3inst.getValue()        
        if (remoteComponent != None):
            mode = remoteComponent.getSymbolByID("TC_OPERATION_MODE")
            mode.setValue("Compare")
            stdby = remoteComponent.getSymbolByID("TC_CTRLA_RUNSTDBY")
            stdby.setValue(True)
            wavemode = remoteComponent.getSymbolByID("TC_COMPARE_WAVE_WAVEGEN")
            wavemode.setValue(2)            
                
            
   

def onAttachmentDisconnected(source, target):
    Log.writeInfoMessage('RGB LED:onAttachmentDisconnected: source = {} remote = {}'.format(source["component"].getID(), target["component"].getID()))

def finalizeComponent(rgb_led):
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
    processor = Variables.get("__PROCESSOR")
    if( processor in pic32cx_bz2_family):
        Database.connectDependencies([['rgb_led', 'RGB_LED_PWM_Dependency1', 'tc2', 'TC2_TMR']])
        Database.connectDependencies([['rgb_led', 'RGB_LED_PWM_Dependency2', 'tc3', 'TC3_TMR']])        
    if( processor in pic32cx_bz3_family):  
        Database.connectDependencies([['rgb_led', 'RGB_LED_PWM_Dependency', 'tcc0', 'TCC0_PWM']])
    print ('rgb_led_final')
            

def instantiateComponent(rgb_led):
    print('rgb_led')
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    processor = Variables.get("__PROCESSOR")
    print processor


    print('Config Name: {} processor: {}'.format(configName, processor))
    
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
 
    deviceFamily = rgb_led.createStringSymbol("DEVICE_FAM", None)
    deviceFamily.setVisible(False)
    
    if( processor in pic32cx_bz2_family):
        Database.activateComponents(["tc2"])
        Database.activateComponents(["tc3"])
        tc2InstanceName = rgb_led.createStringSymbol("TC2_INSTANCE", None)
        tc2InstanceName.setVisible(False)
        tc3InstanceName = rgb_led.createStringSymbol("TC3_INSTANCE", None)
        tc3InstanceName.setVisible(False)
        deviceFamily.setValue("BZ2")
        # WO configuration Warning status
        WOComment = rgb_led.createCommentSymbol("TC_WO_PIN_CONF", None)
        WOComment.setVisible(True)
        WOComment.setLabel("Warning!!! Configure TC(Red, Green) with WO0, W01 and TC(Blue) with WO0 output pins in Pin Configuration")
        WOComment = rgb_led.createCommentSymbol("TC_WO_PIN_CONF_1", None)
        WOComment.setVisible(True)
        WOComment.setLabel("Note: On WBZ451 Curiosity Board, Red -> RB0, Green -> RB3, Blue -> RB5")      
        print ('rgb warning')
        
    if( processor in pic32cx_bz3_family):    
        Database.activateComponents(["tcc0"])
        tccInstanceName = rgb_led.createStringSymbol("TCC_INSTANCE", None)
        tccInstanceName.setVisible(False)
        deviceFamily.setValue("BZ3")
        # WO configuration Warning status
        WOComment = rgb_led.createCommentSymbol("TCC_WO_PIN_CONF", None)
        WOComment.setVisible(True)
        WOComment.setLabel("Warning!!! Configure TCC WO1 (Red), W03 (Green), WO5 (Blue) output pins in Pin Configuration ")
        WOComment = rgb_led.createCommentSymbol("TCC_WO_PIN_CONF_1", None)
        WOComment.setVisible(True)
        WOComment.setLabel("Note: On WBZ351 Curiosity Board, Red -> RB0, Green -> RB3, Blue -> RB5")         
        print ('rgb warning')

  
   
    
    # Add rgb_led.c
    appSourceFile = rgb_led.createFileSymbol(None, None)
    appSourceFile.setSourcePath('driver/templates/sensors/rgb_led.c.ftl')
    appSourceFile.setOutputName('rgb_led.c')
    appSourceFile.setOverwrite(True)
    appSourceFile.setDestPath('../../sensors/src')
    appSourceFile.setProjectPath('sensors')
    appSourceFile.setType('SOURCE')
    appSourceFile.setMarkup(True)
    appSourceFile.setEnabled(True)
    
    # Add rgb_led.h
    appHeaderFile = rgb_led.createFileSymbol(None, None)
    appHeaderFile.setSourcePath('driver/templates/sensors/rgb_led.h.ftl')
    appHeaderFile.setOutputName('rgb_led.h')
    appHeaderFile.setOverwrite(True)
    appHeaderFile.setDestPath('../../sensors/inc')
    appHeaderFile.setProjectPath('sensors')
    appHeaderFile.setType('HEADER')
    appHeaderFile.setMarkup(True)
    appHeaderFile.setEnabled(True)