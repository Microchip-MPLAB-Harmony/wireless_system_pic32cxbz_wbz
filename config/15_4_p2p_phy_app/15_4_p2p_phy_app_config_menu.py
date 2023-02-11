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

global p2pPhyAppMenu
p2pPhyAppMenu = p2pPhyApp.createMenuSymbol("P2P_PHY_APP_MENU", None)
p2pPhyAppMenu.setLabel("PHY Configuration")
p2pPhyAppMenu.setVisible(True)

global p2pPhyAppMenuChannel
p2pPhyAppMenuChannel = p2pPhyApp.createIntegerSymbol("CHANNEL", p2pPhyAppMenu)
p2pPhyAppMenuChannel.setLabel("CHANNEL")
p2pPhyAppMenuChannel.setMin(11)
p2pPhyAppMenuChannel.setMax(26)
p2pPhyAppMenuChannel.setDefaultValue(11)

# comboValues = ["0","2","16","17"]
# global p2pPhyAppMenuChannelPage
# p2pPhyAppMenuChannelPage = p2pPhyApp.createComboSymbol("CHANNEL_PAGE", p2pPhyAppMenu, comboValues)
# p2pPhyAppMenuChannelPage.setLabel("CHANNEL PAGE")
# p2pPhyAppMenuChannelPage.setDefaultValue("0")

global p2pPhyAppMenuShortAddress
p2pPhyAppMenuShortAddress = p2pPhyApp.createHexSymbol("MAC_SHORT_ADDRESS", p2pPhyAppMenu)
p2pPhyAppMenuShortAddress.setLabel("SOURCE ADDRESS (16-BITS SHORT ADDRESS)")
p2pPhyAppMenuShortAddress.setMin(0x0000)
p2pPhyAppMenuShortAddress.setMax(0xFFFF)
p2pPhyAppMenuShortAddress.setDefaultValue(0x0001)

global p2pPhyAppMenuExtendedAddress
p2pPhyAppMenuShortAddress = p2pPhyApp.createHexSymbol("MAC_EXTENDED_ADDRESS", p2pPhyAppMenu)
p2pPhyAppMenuShortAddress.setLabel("EXTENDED IEEE ADDRESS (64-BITS)")
p2pPhyAppMenuShortAddress.setMin(0x0000000000000000)
p2pPhyAppMenuShortAddress.setMax(0x7FFFFFFFFFFFFFFF)
p2pPhyAppMenuShortAddress.setDefaultValue(0x0000000000000001)

global p2pPhyAppMenuPanId
p2pPhyAppMenuPanId = p2pPhyApp.createHexSymbol("MAC_PAN_ID", p2pPhyAppMenu)
p2pPhyAppMenuPanId.setLabel("PAN ID (16-BITS)")
p2pPhyAppMenuPanId.setMin(0x0000)
p2pPhyAppMenuPanId.setMax(0xFFFF)
p2pPhyAppMenuPanId.setDefaultValue(0xCAFE)

global p2pPhyAppMenuMaxBE
p2pPhyAppMenuMaxBE = p2pPhyApp.createIntegerSymbol("MAX_BE", p2pPhyAppMenu)
p2pPhyAppMenuMaxBE.setLabel("MAX BE")
p2pPhyAppMenuMaxBE.setMin(3)
p2pPhyAppMenuMaxBE.setMax(8)
p2pPhyAppMenuMaxBE.setDefaultValue(5)

global p2pPhyAppMenuMinBE
p2pPhyAppMenuMinBE = p2pPhyApp.createIntegerSymbol("MIN_BE", p2pPhyAppMenu)
p2pPhyAppMenuMinBE.setLabel("MIN BE")
p2pPhyAppMenuMinBE.setMin(0)
p2pPhyAppMenuMinBE.setMax(3)
p2pPhyAppMenuMinBE.setDefaultValue(3)

global p2pPhyAppMenuCSMAretry
p2pPhyAppMenuCSMAretry = p2pPhyApp.createIntegerSymbol("MAX_CSMA_RETRY", p2pPhyAppMenu)
p2pPhyAppMenuCSMAretry.setLabel("CSMA BACKOFF")
p2pPhyAppMenuCSMAretry.setMin(0)
p2pPhyAppMenuCSMAretry.setMax(5)
p2pPhyAppMenuCSMAretry.setDefaultValue(4)

global p2pPhyAppMenuFrameRetry
p2pPhyAppMenuFrameRetry = p2pPhyApp.createIntegerSymbol("MAX_FRAME_RETRY", p2pPhyAppMenu)
p2pPhyAppMenuFrameRetry.setLabel("FRAME RETRY")
p2pPhyAppMenuFrameRetry.setMin(0)
p2pPhyAppMenuFrameRetry.setMax(7)
p2pPhyAppMenuFrameRetry.setDefaultValue(3)

global p2pPhyAppMenuPromiscuousMode
p2pPhyAppMenuPromiscuousMode = p2pPhyApp.createBooleanSymbol("Promiscuous_Mode", p2pPhyAppMenu)
p2pPhyAppMenuPromiscuousMode.setLabel("PROMISCUOUS MODE")
p2pPhyAppMenuPromiscuousMode.setDefaultValue(False)

global p2pPhyAppMenuCCAmode
p2pPhyAppMenuCCAmode = p2pPhyApp.createIntegerSymbol("CCA_Mode", p2pPhyAppMenu)
p2pPhyAppMenuCCAmode.setLabel("CCA MODE")
p2pPhyAppMenuCCAmode.setMin(0)
p2pPhyAppMenuCCAmode.setMax(13)
p2pPhyAppMenuCCAmode.setDefaultValue(1)

global p2pPhyAppMenuTxPower
p2pPhyAppMenuTxPower = p2pPhyApp.createIntegerSymbol("TX_PWR", p2pPhyAppMenu)
p2pPhyAppMenuTxPower.setLabel("TRANSMIT POWER")
p2pPhyAppMenuTxPower.setMin(0)
p2pPhyAppMenuTxPower.setMax(15)
p2pPhyAppMenuTxPower.setDefaultValue(4)

global p2pPhyAppMenuCSMAmode
p2pPhyAppMenuCSMAmode = p2pPhyApp.createIntegerSymbol("CSMA_Mode", p2pPhyAppMenu)
p2pPhyAppMenuCSMAmode.setLabel("CSMA MODE")
p2pPhyAppMenuCSMAmode.setMin(0)
p2pPhyAppMenuCSMAmode.setMax(3)
p2pPhyAppMenuCSMAmode.setDefaultValue(0)


global p2pPhyAppConfig
p2pPhyAppConfig = p2pPhyApp.createMenuSymbol("P2P_PHY_APP_CONFIG", None)
p2pPhyAppConfig.setLabel("APP Configuration")
p2pPhyAppConfig.setVisible(True)

global p2pPhyAppMenuPayloadBuf
p2pPhyAppMenuPayloadBuf = p2pPhyApp.createIntegerSymbol("TX_PAYLOAD_BUFFER_SIZE", p2pPhyAppConfig)
p2pPhyAppMenuPayloadBuf.setLabel("TX PAYLOAD BUFFER SIZE")
p2pPhyAppMenuPayloadBuf.setMin(128)
p2pPhyAppMenuPayloadBuf.setMax(8192)
p2pPhyAppMenuPayloadBuf.setDefaultValue(500)

global p2pPhyAppMenuDestinationAddress
p2pPhyAppMenuDestinationAddress = p2pPhyApp.createHexSymbol("DESTINATION_ADDRESS", p2pPhyAppConfig)
p2pPhyAppMenuDestinationAddress.setLabel("DESTINATION ADDRESS (16-BITS SHORT ADDRESS)")
p2pPhyAppMenuDestinationAddress.setMin(0x0000)
p2pPhyAppMenuDestinationAddress.setMax(0xFFFF)
p2pPhyAppMenuDestinationAddress.setDefaultValue(0x0002)

global p2pPhyAppMenuExtendedDestinationAddress
p2pPhyAppMenuExtendedDestinationAddress = p2pPhyApp.createHexSymbol("EXTENDED_DESTINATION_ADDRESS", p2pPhyAppConfig)
p2pPhyAppMenuExtendedDestinationAddress.setLabel("EXTENDED DESTINATION ADDRESS (64-BITS)")
p2pPhyAppMenuExtendedDestinationAddress.setMin(0x0000000000000000)
p2pPhyAppMenuExtendedDestinationAddress.setMax(0x7FFFFFFFFFFFFFFF)
p2pPhyAppMenuExtendedDestinationAddress.setDefaultValue(0x0000000000000002)

global p2pPhyAppMenuNumDevices
p2pPhyAppMenuNumDevices = p2pPhyApp.createIntegerSymbol("NUM_OF_DEVICES", p2pPhyAppConfig)
p2pPhyAppMenuNumDevices.setLabel("NUM OF DEVICES")
p2pPhyAppMenuNumDevices.setMin(0)
p2pPhyAppMenuNumDevices.setMax(100)
p2pPhyAppMenuNumDevices.setDefaultValue(64)

global p2pPhyAppMenuEDscanDuration
p2pPhyAppMenuEDscanDuration = p2pPhyApp.createIntegerSymbol("ED_SCAN_DURATION", p2pPhyAppConfig)
p2pPhyAppMenuEDscanDuration.setLabel("ED SCAN DURATION")
p2pPhyAppMenuEDscanDuration.setMin(0)
p2pPhyAppMenuEDscanDuration.setMax(14)
p2pPhyAppMenuEDscanDuration.setDefaultValue(8)
