/*******************************************************************************
  Application CoAP Server Header File

  Company:
    Microchip Technology Inc.

  File Name:
    app_coap_server.h

  Summary:
    This file contains the Application CoAP Server header file for this project.

  Description:
    This file contains the Application CoAP Server header file for this project.
 *******************************************************************************/

#ifndef _APP_COAP_SERVER_H    /* Guard against multiple inclusion */
#define _APP_COAP_SERVER_H


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

typedef void (*APP_COAP_ServerGetDataToSend_T)(uint8_t resourceID, uint8_t** dataBuffer,uint16_t* dataSize);
typedef void (*APP_COAP_CoapServerGetByteToRead_T)(uint8_t resourceID, uint16_t* bytesToRead);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************
	
void APP_CoapServerDataReceiveHandler(uint8_t resourceID, uint8_t* dataBuff);
void APP_CoapServerAddResource(void);
void APP_CoapServerRegisterCallback(APP_COAP_ServerGetDataToSend_T coapServerGetDataToSend, 
									APP_COAP_CoapServerGetByteToRead_T coapServerGetByteToRead);


/* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _APP_COAP_SERVER_H */

/* *****************************************************************************
 End of File
 */
