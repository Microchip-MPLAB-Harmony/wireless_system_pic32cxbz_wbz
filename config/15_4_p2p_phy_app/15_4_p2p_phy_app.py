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
#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPONENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def instantiateComponent(p2pPhyApp):
    print("P2P PHY Application component")
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    # === Activate required components automatically
    requiredComponents = [
        "IEEE_802154_PHY",
        "sys_command",
        "sys_console"
    ]

    conditionAlwaysInclude = [True, None, []]
    res = Database.activateComponents(requiredComponents)
    
    execfile(Module.getPath() + "config/15_4_p2p_phy_app/15_4_p2p_phy_app_config_menu.py")
    
    #Source File Processing
    appP2PphySrc = p2pPhyApp.createFileSymbol("APP_P2P_PHY_SOURCE", None)
    appP2PphySrc.setSourcePath("/driver/src/app_p2p_phy.c")
    appP2PphySrc.setOutputName("app_p2p_phy.c")
    appP2PphySrc.setDestPath("app_p2p_phy/src/" + "")
    appP2PphySrc.setProjectPath("app_p2p_phy/"+ "app_p2p_phy/src/" + "")
    appP2PphySrc.setType("SOURCE")
    appP2PphySrc.setOverwrite(True)
    appP2PphySrc.setEnabled(True)

    appPhyCmdProcessorSrc = p2pPhyApp.createFileSymbol("APP_PHY_CMD_PROCESSOR_SOURCE", None)
    appPhyCmdProcessorSrc.setSourcePath("/driver/src/app_phy_cmd_processor.c")
    appPhyCmdProcessorSrc.setOutputName("app_phy_cmd_processor.c")
    appPhyCmdProcessorSrc.setDestPath("app_p2p_phy/app_phy_cmd_processor/src/" + "")
    appPhyCmdProcessorSrc.setProjectPath("app_p2p_phy/"+ "app_phy_cmd_processor/src/" + "")
    appPhyCmdProcessorSrc.setType("SOURCE")
    appPhyCmdProcessorSrc.setOverwrite(True)
    appPhyCmdProcessorSrc.setEnabled(True)


    #Header File Processing
    appP2PphyHdr = p2pPhyApp.createFileSymbol("APP_P2P_PHY_HEADER", None)
    appP2PphyHdr.setSourcePath("/driver/src/app_p2p_phy.h")
    appP2PphyHdr.setOutputName("app_p2p_phy.h")
    appP2PphyHdr.setDestPath("app_p2p_phy/inc/" + "")
    appP2PphyHdr.setProjectPath("app_p2p_phy/"+ "app_p2p_phy/inc/" + "")
    appP2PphyHdr.setType("HEADER")
    appP2PphyHdr.setOverwrite(True)
    appP2PphyHdr.setEnabled(True)

    appPhyCmdProcessorHdr = p2pPhyApp.createFileSymbol("APP_PHY_CMD_PROCESSOR_HEADER", None)
    appPhyCmdProcessorHdr.setSourcePath("/driver/src/app_phy_cmd_processor.h")
    appPhyCmdProcessorHdr.setOutputName("app_phy_cmd_processor.h")
    appPhyCmdProcessorHdr.setDestPath("app_p2p_phy/app_phy_cmd_processor/inc/" + "")
    appPhyCmdProcessorHdr.setProjectPath("app_p2p_phy/"+ "app_phy_cmd_processor/inc/" + "")
    appPhyCmdProcessorHdr.setType("HEADER")
    appPhyCmdProcessorHdr.setOverwrite(True)
    appPhyCmdProcessorHdr.setEnabled(True)

    # === File templates processing
    appConfHeader = p2pPhyApp.createFileSymbol("APP_P2P_PHY_CONF_HEADER", None)
    appConfHeader.setSourcePath("/driver/templates/app_p2p_phy_config.h.ftl")
    appConfHeader.setOutputName("app_p2p_phy_config.h")
    appConfHeader.setDestPath("app_p2p_phy/inc/" + "")
    appConfHeader.setProjectPath("app_p2p_phy/"+ "app_p2p_phy/inc/" + "")
    appConfHeader.setType("HEADER")
    appConfHeader.setOverwrite(True)
    appConfHeader.setMarkup(True)

    phyp2pAppdefFile = p2pPhyApp.createFileSymbol('P2PPHYAPP_DEFINITIONS_H', None)
    phyp2pAppdefFile.setType('STRING')
    phyp2pAppdefFile.setOutputName('core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES')
    phyp2pAppdefFile.setSourcePath('/driver/templates/system_definitions.h.ftl')
    phyp2pAppdefFile.setOverwrite(True)
    phyp2pAppdefFile.setMarkup(True)

    phyp2pAppdefFile_1 = p2pPhyApp.createFileSymbol('P2PPHYAPP_DEFINITIONS_ADDON_H', None)
    phyp2pAppdefFile_1.setType('STRING')
    phyp2pAppdefFile_1.setOutputName('core.LIST_SYSTEM_DEFINITIONS_H_EXTERNS')
    phyp2pAppdefFile_1.setSourcePath('/driver/templates/system_definitions_addon.h.ftl')
    phyp2pAppdefFile_1.setOverwrite(True)
    phyp2pAppdefFile_1.setMarkup(True)

    SourceFile = p2pPhyApp.createFileSymbol(None, None)
    SourceFile.setSourcePath('/driver/templates/app.c.ftl')
    SourceFile.setOutputName('app.c')
    SourceFile.setOverwrite(True)
    SourceFile.setDestPath('../../')
    SourceFile.setProjectPath('')
    SourceFile.setType('SOURCE')
    SourceFile.setEnabled(True)
    SourceFile.setMarkup(True)


def finalizeComponent(p2pPhyApp):
        pass
#end finalizeComponent

