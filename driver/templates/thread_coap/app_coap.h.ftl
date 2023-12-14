/*******************************************************************************
  Application CoAP Header File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap.h

  Summary:
    This file contains the Application CoAP header file for this project.

  Description:
    This file contains the Application CoAP header file for this project.
 *******************************************************************************/

#ifndef _APP_COAP_H    /* Guard against multiple inclusion */
#define _APP_COAP_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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


// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************

<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_CLIENT") >
void APP_CoapClientAckReceiveHandler(uint8_t resourceID);
void APP_CoapClientDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff);
</#if>   
<#if (COAP_DEVICE_ROLE_CONFIG == "COAP_SERVER") >
void APP_CoapServerDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff);
</#if>
void APP_CoapAppInit();


    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _APP_COAP_H */

/* *****************************************************************************
 End of File
 */
