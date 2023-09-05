/*******************************************************************************
  Application BLE log Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_ble_log_handler.c

  Summary:
    This file contains the Application BLE functions for this project.

  Description:
    This file contains the Application BLE functions for this project.
 *******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include "definitions.h"
#include "ble_log/ble_log.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Variables
// *****************************************************************************
// *****************************************************************************
  

// *****************************************************************************
// *****************************************************************************
// Section: Functions
// *****************************************************************************
// *****************************************************************************

void APP_BleLogOutput(uint8_t logType, uint16_t packetLength, uint8_t *p_logPacket)
{
   uint8_t testDbg[256];
   
   if(logType == BLE_LOG_TYPE_HCI_COMMAND)
   {
       testDbg[1] = 0x82;   
   }
   else if(logType == BLE_LOG_TYPE_HCI_ACL_TX)
   {
       testDbg[1] = 0x83;
   }
   else if(logType == BLE_LOG_TYPE_HCI_ACL_RX)
   {
       testDbg[1] = 0x86;
   }
   else if(logType == BLE_LOG_TYPE_HCI_EVENT)
   {
       testDbg[1] = 0x85;
   }
   else
   {
       return;
   }
   
   testDbg[0] = 0x66;
   memcpy(&testDbg[2],p_logPacket,packetLength);
   testDbg[packetLength+2] = 0x5A;
<#if SERCOM_CONNECTED = true>
   ${SERCOM_INST}_USART_Write(&testDbg[0] ,packetLength+3);
</#if>
}