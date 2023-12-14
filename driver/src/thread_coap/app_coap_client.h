/*******************************************************************************
  Application CoAP Client Header File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap_client.h

  Summary:
    This file contains the Application CoAP Client header file for this project.

  Description:
    This file contains the Application CoAP Client header file for this project.
 *******************************************************************************/

#ifndef _APP_COAP_CLIENT_H    /* Guard against multiple inclusion */
#define _APP_COAP_CLIENT_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app_coap_common.h"


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

void APP_CoapClientAckReceiveHandler(uint8_t resourceID);
void APP_CoapClientDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff);
void APP_CoapClientPutReq(APP_COAP_ResourceId_T resourceID, uint8_t* dataBuffer, uint16_t dataBuffSize);
void APP_CoapClientGetReq(APP_COAP_ResourceId_T resourceID, uint16_t byteToRead);


    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _APP_COAP_CLIENT_H */

/* *****************************************************************************
 End of File
 */
