/*******************************************************************************
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
*******************************************************************************/

/*******************************************************************************
  Application CoAP Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap.c

  Summary:
    This file contains the Application CoAP for this project.

  Description:
    This file contains the Application CoAP for this project.
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "app_coap/app_coap_common.h"
<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_CLIENT") >
#include "app_coap/app_coap_client.h"
</#if>
<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_SERVER") >
#include "app_coap/app_coap_server.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************

<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_SERVER") >
static void APP_CoapServerGetDataToSend(uint8_t resourceID, uint8_t** dataBuffer,uint16_t* dataSize)
{
   switch(resourceID)
   {
        case ${RESOURCE_ID1_CONFIG}:
        {
            /*TODO: implement your application code, copy user data buffer address to dataBuffer*/
        }
        break;
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
        case ${RESOURCE_ID2_CONFIG}:
        {
           /*TODO: implement your application code, copy user data buffer address to dataBuffer*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
        case ${RESOURCE_ID3_CONFIG}:
        {
            /*TODO: implement your application code, copy user data buffer address to dataBuffer*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
        case ${RESOURCE_ID4_CONFIG}:
        {
            /*TODO: implement your application code, copy user data buffer address to dataBuffer*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
        case ${RESOURCE_ID5_CONFIG}:
        {
            /*TODO: implement your application code, copy user data buffer address to dataBuffer*/
        }
        break;
</#if>

        default:
        break;
   } 
}

static void APP_CoapServerGetByteToRead(uint8_t resourceID, uint16_t* bytesToRead)
{
   switch(resourceID)
   {
        case ${RESOURCE_ID1_CONFIG}:
        {
            /*TODO: implement your application code, Update the value for the bytes to read*/
        }
        break;
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
        case ${RESOURCE_ID2_CONFIG}:
        {
           /*TODO: implement your application code, Update the value for the bytes to read*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
        case ${RESOURCE_ID3_CONFIG}:
        {
            /*TODO: implement your application code, Update the value for the bytes to read*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
        case ${RESOURCE_ID4_CONFIG}:
        {
            /*TODO: implement your application code, Update the value for the bytes to read*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
        case ${RESOURCE_ID5_CONFIG}:
        {
            /*TODO: implement your application code, Update the value for the bytes to read*/
        }
        break;
</#if>

        default:
        break;
   } 
}
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************

<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_CLIENT") >
void APP_CoapClientAckReceiveHandler(uint8_t resourceID)
{
    switch(resourceID)
    {
        case ${RESOURCE_ID1_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
        case ${RESOURCE_ID2_CONFIG}:
        {
           /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
        case ${RESOURCE_ID3_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
        case ${RESOURCE_ID4_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
        case ${RESOURCE_ID5_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
        
        default:
        break;
    }
}

void APP_CoapClientDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff)
{
    switch(resourceID)
    {
        case ${RESOURCE_ID1_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
        case ${RESOURCE_ID2_CONFIG}:
        {
           /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
        case ${RESOURCE_ID3_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
        case ${RESOURCE_ID4_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
        case ${RESOURCE_ID5_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
        
        default:
        break;
    }
}
</#if>

<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_SERVER") >
void APP_CoapServerDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff)
{
    switch(resourceID)
    {
        case ${RESOURCE_ID1_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
        case ${RESOURCE_ID2_CONFIG}:
        {
           /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
        case ${RESOURCE_ID3_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
        case ${RESOURCE_ID4_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
        case ${RESOURCE_ID5_CONFIG}:
        {
            /*TODO: implement your application code*/
        }
        break;
</#if>
        
        default:
        break;
    }
}
</#if>

void APP_CoapAppInit()
{
<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_CLIENT") >
    APP_CoapStart();
</#if>
<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_SERVER") >
    APP_CoapStart();
    APP_CoapServerAddResource();
    APP_CoapServerRegisterCallback(APP_CoapServerGetDataToSend,APP_CoapServerGetByteToRead);
</#if>
}

/* *****************************************************************************
 End of File
 */
