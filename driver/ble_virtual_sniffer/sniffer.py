global log_symbol  
log_symbol = {"log_symbol_obj": "",
              "remote_symbol_obj": "",
              "remote_log_File_sym_obj":"",
              "local_log_File_sym_obj":"",
              "console_inst": "",}

def handleMessage(messageID, args):
    #print("messageID:", messageID)
    #print("args:", args)
    pass

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    log_symbol.update({"remote_symbol_obj": remoteComponent})
    Log.writeInfoMessage('blesniffer:onAttachmentConnected: source = {} remote = {}'.
            format(localComponent.getID(), targetID))   
    if(connectID == "BLE_Stack_Dependency"):
        ble_Log_enabled = remoteComponent.getSymbolByID("BLE_SYS_LOG_EN").getValue()
        print("isBleLogEnabled:",ble_Log_enabled)     
        if ble_Log_enabled == False:
            remoteComponent.setSymbolValue("BLE_SYS_LOG_EN",True)  
            ble_Log_enabled1 = remoteComponent.getSymbolByID("BLE_SYS_LOG_EN").getValue()
            print("isBleLogEnabled:",ble_Log_enabled1)   
        symbol = remoteComponent.getSymbolByID("BLE_SYS_LOG_EN")
        log_symbol.update({"log_symbol_obj": symbol})
        symbol.setReadOnly(True)
        remotelogHandlerFileSymbol = remoteComponent.getSymbolByID("APP_LOG_HANDLER_C_FILE")
        log_symbol.update({"remote_log_File_sym_obj": remotelogHandlerFileSymbol}) 
    
    if(connectID == "Sniffer_Uart_dependency"):
        #print("RemoteComponent_ID",remoteID)
        log_symbol.update({"console_inst": remoteID.upper()})
        log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_CONNECTED",True)
        log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_INST", str(log_symbol["console_inst"]))
        SnifferUartInst.setValue(remoteID.upper())
        if log_symbol["console_inst"] != '':
            symbolID_oper = remoteComponent.getSymbolByID("USART_OPERATING_MODE")
            usart_Operating_mode = symbolID_oper.getSelectedKey()       
            if usart_Operating_mode != 'RING_BUFFER':
                symbolID_oper.setSelectedKey("RING_BUFFER")
            symbolID_oper.setReadOnly(True)
            global symbol_TXRingBuffer,symbol_RxRingBuffer,symbol_BaudRate
            symbol_TXRingBuffer = remoteComponent.getSymbolByID("USART_TX_RING_BUFFER_SIZE")
            symbol_RxRingBuffer = remoteComponent.getSymbolByID("USART_RX_RING_BUFFER_SIZE")
            symbol_BaudRate = remoteComponent.getSymbolByID("USART_BAUD_RATE")
            if  symbol_TXRingBuffer.getValue() != 1000:
                symbol_TXRingBuffer.setValue(1000)
            symbol_TXRingBuffer.setReadOnly(True)
            if  symbol_RxRingBuffer.getValue() != 1000:
                symbol_RxRingBuffer.setValue(1000)
            symbol_RxRingBuffer.setReadOnly(True)
            if  symbol_BaudRate.getValue() != 921600:
                symbol_BaudRate.setValue(921600)
            symbol_BaudRate.setReadOnly(True)
            print("TX Buffer Size Updated to ",symbol_TXRingBuffer.getValue())
            print("RX Buffer Size Updated to",symbol_RxRingBuffer.getValue())
            print("Baud Rate Updated to ",symbol_BaudRate.getValue())
    
    log_symbol["remote_log_File_sym_obj"].setOverwrite(False)
    log_symbol["remote_log_File_sym_obj"].setMarkup(False)
    log_symbol["remote_log_File_sym_obj"].setEnabled(False)         
    log_symbol["local_log_File_sym_obj"].setOverwrite(True)
    log_symbol["local_log_File_sym_obj"].setEnabled(True)

       
def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    if(connectID == "Sniffer_Uart_dependency"):
       log_symbol["local_log_File_sym_obj"].addMarkupVariable("SYS_CONSOLE_CONNECTED",False)
       if log_symbol["console_inst"] != '':
           symbol_TXRingBuffer.setReadOnly(False)
           symbol_RxRingBuffer.setReadOnly(False)
           symbol_BaudRate.setReadOnly(False)
       log_symbol.update({"console_inst": ''})
       log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_CONNECTED",False)
       log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_INST", str(log_symbol["console_inst"]))
       SnifferUartInst.setValue('')
        

def instantiateComponent(snifferblock):
    Log.writeInfoMessage("Initiating RN HOST LIBRARY")
    #print(rnHostLib)
    configName = Variables.get("__CONFIGURATION_NAME")
    #print configName
    processor = Variables.get("__PROCESSOR")
    #print processor
    components = Database.getActiveComponentIDs()
    if 'BLE_STACK_LIB' not in components:
        res = Database.activateComponents(['BLE_STACK_LIB'])
    snifferblock.setDependencyEnabled("BLE_Stack_Dependency",True)
    
    global SnifferUartInst
    SnifferUartInst  = snifferblock.createStringSymbol("SNIFFER_UART_INST_USED",None)
    SnifferUartInst.setLabel("UART INSTANCE")
    SnifferUartInst.setReadOnly(True)
    SnifferUartInst.setDefaultValue("")
    
    # Add app_ble_log_handler.c - generated file
    app_bleLogHandlerSourceFile = snifferblock.createFileSymbol(None,None)
    app_bleLogHandlerSourceFile.setSourcePath("driver/templates/app_ble_log_handler.c.ftl")
    app_bleLogHandlerSourceFile.setOutputName("app_ble_log_handler.c")
    #app_bleLogHandlerSourceFile.setOverwrite(True)
    app_bleLogHandlerSourceFile.setDestPath("../../app_ble/")
    app_bleLogHandlerSourceFile.setProjectPath("app_ble")
    app_bleLogHandlerSourceFile.setType("SOURCE")
    app_bleLogHandlerSourceFile.setMarkup(True)
    app_bleLogHandlerSourceFile.setOverwrite(True)
    app_bleLogHandlerSourceFile.setEnabled(True)
    log_symbol.update({"local_log_File_sym_obj": app_bleLogHandlerSourceFile})
    
    log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_CONNECTED",False)
    log_symbol["local_log_File_sym_obj"].addMarkupVariable("SERCOM_INST", str(log_symbol["console_inst"]))
    
def finalizeComponent(snifferblock):
    #print("finalizeComponent",snifferblock)
    pass     

def destroyComponent(snifferblock) :
    if log_symbol["log_symbol_obj"] != '':
        log_symbol["log_symbol_obj"].setReadOnly(False)
    pass
    #print("destroyComponent")  