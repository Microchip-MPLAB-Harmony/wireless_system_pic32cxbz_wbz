# coding: utf-8
##############################################################################
# Copyright (C) 2019-2020 Microchip Technology Inc. and its subsidiaries.
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

print('Load Module: Harmony RGB LED System Service')

rgb_LedComponent  = Module.CreateComponent('rgb_led', 'RGB LED SERVICE', '/Wireless/Board Support/', 'config/rgb_led/rgb_led.py')
rgb_LedComponent.setDisplayType('RGB LED Service')
if( processor in pic32cx_bz2_family):
    rgb_LedComponent.addDependency('RGB_LED_PWM_Dependency1', 'TMR', 'TC(Red,Green)', False, True)
    rgb_LedComponent.addDependency('RGB_LED_PWM_Dependency2', 'TMR', 'TC(Blue)', False, True)    
if( processor in pic32cx_bz3_family):
    rgb_LedComponent.addDependency('RGB_LED_PWM_Dependency', 'PWM', 'TCC', False, True)    
if( processor in pic32cx_bz6_family):
    rgb_LedComponent.addDependency('RGB_LED_PWM_Dependency', 'PWM', 'TCC', False, True)        