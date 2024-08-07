/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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
  Application Thread Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_thread.c

  Summary:
    This file contains the Application Thread Source code for this project.

  Description:
    This file contains the Application Thread Source code for this project.
 *******************************************************************************/
 
// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "definitions.h"
#include "app_thread/app_thread_common.h"
#include "app_thread.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

static otDeviceRole s_appthreadstate = OT_DEVICE_ROLE_DISABLED;
<#if THREAD_SLEEP_ENABLE == true>
extern bool otIsIdle(void);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************

static void APP_ThreadRoleChangeHandler(otChangedFlags aFlags)
{
    switch(aFlags)
    {
        case OT_DEVICE_ROLE_CHILD:
        {
            /* TODO: implement your application code.*/
        }
        break;

        case OT_DEVICE_ROLE_ROUTER:
        {
            /* TODO: implement your application code.*/
        }
        break;

        case OT_DEVICE_ROLE_LEADER:
        {
            /* TODO: implement your application code.*/
        }
        break;

        case OT_DEVICE_ROLE_DETACHED:
        {
            /* TODO: implement your application code.*/
        }
        break;

        case OT_DEVICE_ROLE_DISABLED:
        {
            /* TODO: implement your application code.*/
        }
        break;

        default:
        break;
    }  
}


static void APP_ThreadHandler(otChangedFlags aFlags, void *aContext)
{
    //Check if Device role is changed
    if(aFlags & OT_CHANGED_THREAD_ROLE)
    {
        otInstance * pinstance = APP_ThreadGetInstance();
        s_appthreadstate = otThreadGetDeviceRole(pinstance);
        APP_ThreadRoleChangeHandler(s_appthreadstate);
    }
    /* TODO: Not handling other flags as of now, add if required*/
}


// *****************************************************************************
// *****************************************************************************
// Section: Interface Functions
// *****************************************************************************
// *****************************************************************************

otChangedFlags APP_ThreadGetDeviceRole(void)
{
    return s_appthreadstate;
}

void APP_ThreadResetToFactoryNew(void)
{
    APP_Msg_T appMsg;
    //appMsg.msgId = APP_THREAD_FACTORY_RESET;
    OSAL_QUEUE_Send(&appData.appQueue, &appMsg, 0);
}

void APP_ThreadAppStackInit(APP_ProvNwData_T *provNwData)
{
  otError error;
  error = APP_ThreadInit(APP_ThreadHandler);
  if(OT_ERROR_NONE == error)
  {
      error = APP_ThreadSetNwParameters(provNwData);
      if(OT_ERROR_NONE == error)
      {
          error =  APP_ThreadNwStart();
      }
  }
  if(error != OT_ERROR_NONE)
  {
      /* TODO: implement your application code.*/
  }
  else
  {
    /* TODO: implement your application code.*/  
  }
  /* TODO: implement any initialization for application code.*/
}
<#if THREAD_SLEEP_ENABLE == true>

void APP_ThreadDeviceSleep(void)
{
    if(otIsIdle())
    {
       DEVICE_EnterDeepSleep(false, APP_THREAD_DEVICE_SLEEP_PERIOD);
    }
    else
    {
		/* TODO: implement your application code.*/
    }
}
</#if>
