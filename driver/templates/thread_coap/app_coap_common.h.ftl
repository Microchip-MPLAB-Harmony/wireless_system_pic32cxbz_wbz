/*******************************************************************************
  Application CoAP Common Header File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap_common.h

  Summary:
    This file contains the Application CoAP Common header file for this project.

  Description:
    This file contains the Application CoAP Common header file for this project.
 *******************************************************************************/

#ifndef _APP_COAP_COMMON_H    /* Guard against multiple inclusion */
#define _APP_COAP_COMMON_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "openthread/coap.h"
#include "definitions.h"


/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Macros
// *****************************************************************************
// *****************************************************************************
    
#define APP_COAP_PORT ${COAP_PORT_CONFIG}


// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef struct APP_COAP_Req_T
{
	otCoapCode coapCode;
	otCoapType coapType;
	char* coapUriPath;
	uint8_t* coapData;
	uint16_t coapDataSize;
	otCoapResponseHandler coapResponseHandler;
	void* coapContext;
} APP_COAP_Req_T;

typedef struct APP_COAP_Resp_T
{
	otMessage * pmessage;
	const otMessageInfo * pmessageinfo;
	otCoapCode coapCode;
	otCoapType coapType;
	uint8_t* coapData;
	uint16_t coapDataSize;
} APP_COAP_Resp_T;

/**@brief The definition of Resource ID. */
typedef enum APP_COAP_ResourceId_T
{
	${RESOURCE_ID1_CONFIG},
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 2) >
	${RESOURCE_ID2_CONFIG},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 3) >
	${RESOURCE_ID3_CONFIG},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 4) >
	${RESOURCE_ID4_CONFIG},
</#if>
<#if (COAP_RESOUCES_NUMBER_CONFIG >= 5) >
	${RESOURCE_ID5_CONFIG},
</#if>
	APP_RESOURCE_TOTAL
} APP_COAP_ResourceId_T;

typedef struct APP_COAP_Resource_T
{
   APP_COAP_ResourceId_T resourceID;
   otCoapResource resouce;
}APP_COAP_Resource_T;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************

void APP_CoapStart(void);
void APP_CoapRequestSend(APP_COAP_Req_T* appCoapReq);
void APP_CoapAddResource(otCoapResource* coapResource);
void APP_CoapResponseSend(APP_COAP_Resp_T* appCoapResp);
    


/* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _APP_COAP_COMMON_H */

/* *****************************************************************************
 End of File
 */
