/*******************************************************************************
  Application Thread Common Header File

  Company:
    Microchip Technology Inc.

  File Name:
    app_thread_common.h

  Summary:
    This file contains the Application Thread Common header file for this project.

  Description:
    This file contains the Application Thread Common header file for this project.
 *******************************************************************************/

#ifndef _APP_THREAD_COMMON_H    /* Guard against multiple inclusion */
#define _APP_THREAD_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "openthread/instance.h"


/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Macros
// *****************************************************************************
// *****************************************************************************

#define PANID           0x1234
#define EXD_PANID       {0x00,0x01,0x02,0x03,0x4,0x05,0x06,0x07}
#define NWK_NAME        "MCHP_THREAD" // max charin nwk name <= 16
#define CHANNEL         15
#define CHANNEL_MASK    0x7fff800
#define NW_KEY          {0x11,0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,0xaa,0xbb,0xcc,0xdd,0xee,0xff}
#define ML_PREFIX       {0xfd,0x00,0x00,0x00,0xfb,0x01,0x00,0x01}

<#if THREAD_DEVICE_ROLE_CONFIG == "FTD">  
#define DEVICE_AS_LEADER (1U)
</#if>

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
    
void APP_ThreadInit(otStateChangedCallback stateChangedCallback);
void APP_ThreadSetNwParameters(void);
void APP_ThreadNwStart(void);
otInstance* APP_ThreadGetInstance(void);


/* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _APP_THREAD_COMMON_H */

/* *****************************************************************************
 End of File
 */
