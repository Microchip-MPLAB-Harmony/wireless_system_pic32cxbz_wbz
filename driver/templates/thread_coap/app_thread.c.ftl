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
#include "openthread/thread.h"
<#if THREAD_SLEEP_ENABLE == true>
#include "timers.h"
</#if>
#include "app_thread/app_thread_common.h"
#include "app_thread.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

static otDeviceRole s_appthreadstate = OT_DEVICE_ROLE_DISABLED;
<#if THREAD_SLEEP_ENABLE == true>
static TimerHandle_t s_sedtimerhandle = NULL;
extern bool otIsIdle(void);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************
<#if THREAD_SLEEP_ENABLE == true>

static void APP_ThreadSEDTimeoutCb(TimerHandle_t xTimer)
{
    APP_Msg_T sleepReq;

    sleepReq.msgId = APP_TIMER_SED_TIMEOUT_MSG;      
    OSAL_QUEUE_Send(&appData.appQueue, &sleepReq, 0);   
}
</#if>

static void APP_ThreadRoleChangeHandler(otChangedFlags aFlags)
{
    switch(aFlags)
    {
        case OT_DEVICE_ROLE_CHILD:
        {
<#if THREAD_SLEEP_ENABLE == true>
            if(s_sedtimerhandle)
            {
                xTimerStart(s_sedtimerhandle, 0);
            }
</#if>
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

void APP_ThreadAppInit(void)
{
  APP_ThreadInit(APP_ThreadHandler);
  APP_ThreadSetNwParameters();
  APP_ThreadNwStart();
<#if THREAD_SLEEP_ENABLE == true>
  /*sed timeout period can be changed as per the application need.*/
  s_sedtimerhandle = xTimerCreate("sed tmr", (APP_TIMER_SED_TIMEOUT_PERIOD / portTICK_PERIOD_MS), pdFALSE, ( void * ) 0, APP_ThreadSEDTimeoutCb);
</#if>
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
        APP_Msg_T sleepReq;

        sleepReq.msgId = APP_TIMER_SED_TIMEOUT_MSG;      
        OSAL_QUEUE_Send(&appData.appQueue, &sleepReq, 0);
    }
}

void APP_ThreadResetActiveTimer(void)
{
    if (s_sedtimerhandle != NULL)
    {
        if (xTimerReset(s_sedtimerhandle, 0) != pdPASS)
        {
            //Timer reset fail
        }
    }
}
</#if>
