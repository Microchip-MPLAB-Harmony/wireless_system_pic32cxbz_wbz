/**
 * @file app_p2p_phy_config.h
 *
 * @brief File contains P2P PHY App configuration parameters.
 *
 * Copyright (c) 2023 Microchip Technology Inc. and its subsidiaries.
 *
 *
 * Subject to your compliance with these terms, you may use Microchip
 * software and any derivatives exclusively with Microchip products.
 * It is your responsibility to comply with third party license terms applicable
 * to your use of third party software (including open source software) that
 * may accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES,
 * WHETHER EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE,
 * INCLUDING ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY,
 * AND FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT WILL MICROCHIP BE
 * LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL
 * LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE
 * SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS BEEN ADVISED OF THE
 * POSSIBILITY OR THE DAMAGES ARE FORESEEABLE.  TO THE FULLEST EXTENT
 * ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY
 * RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 */


/* Prevent double inclusion */
#ifndef APP_P2P_PHY_CONFIG_H
#define APP_P2P_PHY_CONFIG_H

/* === INCLUDES ============================================================ */

/* === EXTERNALS =========================================================== */

/* === MACROS ============================================================== */

/*
 * TAL PIB default values
 */
#if defined(RF215V3)
    #define CHANNEL_TRANSMIT_RECEIVE_SUB_GHZ            ${CHANNEL}U  
    #define CHANNEL_TRANSMIT_RECEIVE_2_4_GHZ            ${CHANNEL}U  
#elif defined(PHY_AT86RF212B)
    #define CHANNEL_TRANSMIT_RECEIVE            ${CHANNEL}U
#else
   #define CHANNEL_TRANSMIT_RECEIVE            ${CHANNEL}U  
#endif

#define SRC_ADDR                            0x${MAC_SHORT_ADDRESS}U
#define IEEE_ADDR                           0x${MAC_EXTENDED_ADDRESS}U
#define SRC_PAN_ID                          0x${MAC_PAN_ID}U
#define MAXBE                               ${MAX_BE}U
#define MINBE                               ${MIN_BE}U
#define CSMA_BACKOFF                        ${MAX_CSMA_RETRY}U
#define FRAME_RETRY                         ${MAX_FRAME_RETRY}U
#define CCA_MODE                            ${CCA_Mode}U
#define TRANSMIT_POWER                      ${TX_PWR}
#define APP_PAYLOAD_BUFFER_SIZE             ${TX_PAYLOAD_BUFFER_SIZE}U
#define DST_ADDR                            0x${DESTINATION_ADDRESS}U
#define DST_IEEE_ADDR                       0x${EXTENDED_DESTINATION_ADDRESS}U
#define NUM_OF_DEVICES                      ${NUM_OF_DEVICES}U
#define ED_SCAN_DURATION                    ${ED_SCAN_DURATION}U
#define CSMA_MODE		                    ${CSMA_MODE}

/* === TYPES =============================================================== */

<#if Promiscuous_Mode == true>
#define PROMISCUOUS_MODE
</#if>

/* === PROTOTYPES ========================================================== */

#endif /* APP_P2P_PHY_CONFIG_H */
