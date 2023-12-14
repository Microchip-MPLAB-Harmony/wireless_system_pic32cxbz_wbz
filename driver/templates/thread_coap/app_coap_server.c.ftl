/*******************************************************************************
  Application CoAP Server Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap_server.c

  Summary:
    This file contains the Application CoAP Server Source code for this project.

  Description:
    This file contains the Application CoAP server Source code for this project.
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "app_coap_server.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

static APP_COAP_Resource_T appCoapResources[APP_RESOURCE_TOTAL] = 
{
    {${RESOURCE_ID1_CONFIG},{"${RESOURCE_URI1_CONFIG}",NULL,NULL,NULL}},
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
    {${RESOURCE_ID2_CONFIG},{"${RESOURCE_URI2_CONFIG}",NULL,NULL,NULL}},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
    {${RESOURCE_ID3_CONFIG},{"${RESOURCE_URI3_CONFIG}",NULL,NULL,NULL}},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
    {${RESOURCE_ID4_CONFIG},{"${RESOURCE_URI4_CONFIG}",NULL,NULL,NULL}},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
    {${RESOURCE_ID5_CONFIG},{"${RESOURCE_URI5_CONFIG}",NULL,NULL,NULL}}
</#if>
};

static APP_COAP_ServerGetDataToSend_T appCoapServerGetDataToSend;
static APP_COAP_CoapServerGetByteToRead_T appCoapServerGetByteToRead;

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************

static void app_CoapReqHandler(void * pcontext, otMessage * pmessage,
                               const otMessageInfo * pmessageinfo)
{
    APP_Msg_T   appMsg;
    APP_Msg_T   *p_appMsg;
    uint16_t byteToRead = 0;
    uint8_t resourceID = 0;
    
    do
    {
        resourceID = *((int*)pcontext);
        if (otCoapMessageGetCode(pmessage) == OT_COAP_CODE_GET)
        {
            if (otCoapMessageGetType(pmessage) == OT_COAP_TYPE_CONFIRMABLE) 
            {
              APP_COAP_Resp_T coapResp;
              coapResp.pmessage = pmessage;
              coapResp.pmessageinfo = pmessageinfo;
              coapResp.coapCode = OT_COAP_CODE_CONTENT;
              coapResp.coapType = OT_COAP_TYPE_ACKNOWLEDGMENT;
              
              if(appCoapServerGetDataToSend != NULL)
                appCoapServerGetDataToSend(resourceID,&coapResp.coapData,&coapResp.coapDataSize);
              
              APP_CoapResponseSend(&coapResp);
            }
        }

        else if (otCoapMessageGetCode(pmessage) == OT_COAP_CODE_PUT)
        {
            appMsg.msgData[0] = resourceID;
            if(appCoapServerGetDataToSend != NULL)
                appCoapServerGetByteToRead(resourceID,&byteToRead);
             if(otMessageRead(pmessage, otMessageGetOffset(pmessage), &appMsg.msgData[1], byteToRead) != byteToRead)
            {
               break; 
            }
            else
            {
                appMsg.msgId = APP_COAP_SERVER_DATA_RECEIVED;

                p_appMsg = &appMsg;
                OSAL_QUEUE_Send(&appData.appQueue, p_appMsg, 0); 
            }
            
            if (otCoapMessageGetType(pmessage) == OT_COAP_TYPE_CONFIRMABLE) 
            {
              APP_COAP_Resp_T coapResp;
              coapResp.pmessage = pmessage;
              coapResp.pmessageinfo = pmessageinfo;
              coapResp.coapCode = OT_COAP_CODE_CHANGED;
              coapResp.coapType = OT_COAP_TYPE_ACKNOWLEDGMENT;
              coapResp.coapData = NULL;
              APP_CoapResponseSend(&coapResp);
            }
        }
        else
        {
            break;
        }

    } while (false);
}


// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************

void APP_CoapServerRegisterCallback(APP_COAP_ServerGetDataToSend_T coapServerGetDataToSend, 
                                    APP_COAP_CoapServerGetByteToRead_T coapServerGetByteToRead)
{
   appCoapServerGetDataToSend =  coapServerGetDataToSend;
   appCoapServerGetByteToRead = coapServerGetByteToRead;
}

void APP_CoapServerAddResource(void)
{
    for(uint8_t i = 0; i < APP_RESOURCE_TOTAL; i++)
    {
        appCoapResources[i].resouce.mHandler = app_CoapReqHandler;
        appCoapResources[i].resouce.mContext = (void *)&appCoapResources[i].resourceID;
        appCoapResources[i].resouce.mNext    = NULL;
        APP_CoapAddResource(&appCoapResources[i].resouce);
    }
}


/* *****************************************************************************
 End of File
 */
