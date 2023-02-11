# coding: utf-8
##############################################################################
# Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

print("Load Module: Harmony P2P PHY Application")
p2pPhyApp  = Module.CreateComponent('APP_P2P_PHY', 'IEEE 802.15.4 P2P PHY APP', '/Wireless/System Services/', 'config/15_4_p2p_phy_app/15_4_p2p_phy_app.py')
p2pPhyApp.setDisplayType('P2P PHY Application')
p2pPhyApp.addDependency('SysCmdDependency', 'SYS_COMMAND', 'CMD', True, True)
print("***** CPU: ", Variables.get("__PROCESSOR"))
if ("WBZ" in Variables.get("__PROCESSOR")) or ("PIC32CX" in Variables.get("__PROCESSOR")) or  ("SAMR30" in Variables.get("__PROCESSOR")) or  ("SAMR21" in Variables.get("__PROCESSOR")):
    p2pPhyApp.addDependency('DeviceSupportDependency', 'Device_Support', 'Device_Support', True, True)