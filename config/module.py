######################  Harmony replaceme  ######################
def loadModule():
    print('Load Module: Harmony Wireless Service for PIC32CXBZ2 and WBZ45x Family')
    
    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          }

    processor = Variables.get('__PROCESSOR')
    print('processor={}'.format(processor))

    if( processor in pic32cx_bz2_family):
        # app timer service
        execfile(Module.getPath() + '/config/module_app_timer_freertos.py')
        # ble virtual sniffer
        execfile(Module.getPath() + '/config/module_ble_virtual_sniffer.py')
        # ble ota application service
        execfile(Module.getPath() + '/config/module_ble_ota.py')