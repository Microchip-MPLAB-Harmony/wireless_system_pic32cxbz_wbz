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
    pic32cx_bz6_family = {'PIC32CX2051BZ62132',
                          'PIC32CX2051BZ62064',
                          'PIC32CX2051BZ66048',
                          'WBZ651',
                          'WBZ652',
                          'WBZ653',
                          'PIC32WM_BZ6204',
                          }
    processor = Variables.get("__PROCESSOR")

    if (connectID == "Temp_Sensor_Dependency"):
        print('Temp_Sensor_Dependency')
        print remoteComponent        
        if (remoteComponent != None):
            module_en = remoteComponent.getSymbolByID("ADCHS_7_ENABLE")
            module_en.setValue(True)

            if (processor in pic32cx_bz6_family):
                trigsrc = remoteComponent.getSymbolByID("ADCCON1__STRGSRC")
                trigsrc.setValue(1)
                ch = remoteComponent.getSymbolByID("ADCCSS1__CSS10")
                ch.setValue(True)
            else:
                ch = remoteComponent.getSymbolByID("AN2")
                ch.setValue(True)
                trigsrc = remoteComponent.getSymbolByID("ADCTRG1__TRGSRC2")
                trigsrc.setValue(1)
   

def onAttachmentDisconnected(source, target):
    Log.writeInfoMessage('Temp Sensor:onAttachmentDisconnected: source = {} remote = {}'.format(source["component"].getID(), target["component"].getID()))

def finalizeComponent(temp_sensor):
    processor = Variables.get("__PROCESSOR")
    Database.connectDependencies([['temp_sensor', 'Temp_Sensor_Dependency', 'adchs', 'ADCHS_ADC']])
    print ('temp_sensor_final')
            

def instantiateComponent(temp_sensor):
    print('temp_sensor')
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
    pic32cx_bz6_family = {'PIC32CX2051BZ62132',
                          'PIC32CX2051BZ62064',
                          'PIC32CX2051BZ66048',
                          'WBZ651',
                          'WBZ652',
                          'WBZ653',
                          'PIC32WM_BZ6204',
                          }  
    deviceFamily = temp_sensor.createStringSymbol("DEVICE_FAMILY", None)
    deviceFamily.setVisible(False)
    
  
    Database.activateComponents(["adchs"])
    
    if( processor in pic32cx_bz2_family):
        deviceFamily.setValue("BZ2")
        # ADC Pin mapping configuration Warning status
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Warning!!! Configure ADC Input Pin in Pin Configuration")
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF_1", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Note: On WBZ451 Curiosity Board,MCP9700A Temp Sensor mapped to AN2 (PB6)")      
        print ('temp sensor warning')
        
    if( processor in pic32cx_bz3_family):    
        deviceFamily.setValue("BZ3")
        # ADC Pin mapping configuration Warning status
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF_BZ3", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Warning!!! Configure ADC Input Pin in Pin Configuration")
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF_1_BZ3", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Note: On WB351 Curiosity Board,MCP9700A Temp Sensor mapped to AN2 (PB6)")      
        print ('temp sensor warning')

    if( processor in pic32cx_bz6_family):    
        deviceFamily.setValue("BZ6")
        # ADC Pin mapping configuration Warning status
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF_BZ6", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Warning!!! Configure ADC Input Pin in Pin Configuration")
        ADCComment = temp_sensor.createCommentSymbol("ADC_PIN_CONF_1_BZ6", None)
        ADCComment.setVisible(True)
        ADCComment.setLabel("Note: On WB653 Curiosity Board,MCP9700A Temp Sensor mapped to AN10 (PD4)")      
        print ('temp sensor warning')
        
    # Add temp_sensor.c
    appSourceFile = temp_sensor.createFileSymbol(None, None)
    appSourceFile.setSourcePath('driver/templates/sensors/temp_sensor.c.ftl')
    appSourceFile.setOutputName('temp_sensor.c')
    appSourceFile.setOverwrite(True)
    appSourceFile.setDestPath('../../sensors/src')
    appSourceFile.setProjectPath('sensors')
    appSourceFile.setType('SOURCE')
    appSourceFile.setMarkup(True)
    appSourceFile.setEnabled(True)
    
    # Add temp_sensor.h
    appHeaderFile = temp_sensor.createFileSymbol(None, None)
    appHeaderFile.setSourcePath('driver/templates/sensors/temp_sensor.h')
    appHeaderFile.setOutputName('temp_sensor.h')
    appHeaderFile.setOverwrite(True)
    appHeaderFile.setDestPath('../../sensors/inc')
    appHeaderFile.setProjectPath('sensors')
    appHeaderFile.setType('HEADER')
    appHeaderFile.setMarkup(True)
    appHeaderFile.setEnabled(True)