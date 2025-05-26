## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-898.42.3.0.0
-  __TEXT.__text: 0x7fa0
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x840
-  __TEXT.__objc_methlist: 0x2dc
+898.62.2.0.0
+  __TEXT.__text: 0x980c
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0xbd1
-  __TEXT.__objc_methname: 0x9ab
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methtype: 0x39d
+  __TEXT.__cstring: 0x115b
+  __TEXT.__objc_methname: 0xd07
+  __TEXT.__objc_classname: 0xb2
+  __TEXT.__objc_methtype: 0x437
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0x871
-  __TEXT.__unwind_info: 0x200
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x628
-  __DATA_CONST.__cfstring: 0x1240
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__oslogstring: 0xa0e
+  __TEXT.__unwind_info: 0x22c
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__cfstring: 0x1980
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xa80
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_classrefs: 0x60
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x48
-  __DATA.__objc_data: 0x190
+  __DATA.__objc_const: 0xca0
+  __DATA.__objc_selrefs: 0x348
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 170
-  Symbols:   1496
-  CStrings:  402
+  Functions: 203
+  Symbols:   1786
+  CStrings:  529
 
Symbols:
+ -[AppleUSBCLightningAdapterAnalytics .cxx_destruct]
+ -[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:]
+ -[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:].cold.1
+ -[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:].cold.2
+ -[AppleUSBCLightningAdapterAnalytics _startEventMonitoring]
+ -[AppleUSBCLightningAdapterAnalytics _startEventMonitoring].cold.1
+ -[AppleUSBCLightningAdapterAnalytics _stopEventMonitoring]
+ -[AppleUSBCLightningAdapterAnalytics analyticsEventsEnabled]
+ -[AppleUSBCLightningAdapterAnalytics init]
+ -[AppleUSBCLightningAdapterAnalytics ioNotificationPort]
+ -[AppleUSBCLightningAdapterAnalytics ioServiceMatchingIterator]
+ -[AppleUSBCLightningAdapterAnalytics log]
+ -[AppleUSBCLightningAdapterAnalytics monitoring]
+ -[AppleUSBCLightningAdapterAnalytics queue]
+ -[AppleUSBCLightningAdapterAnalytics setAnalyticsEventsEnabled:]
+ -[AppleUSBCLightningAdapterAnalytics setIoNotificationPort:]
+ -[AppleUSBCLightningAdapterAnalytics setIoServiceMatchingIterator:]
+ -[AppleUSBCLightningAdapterAnalytics setLog:]
+ -[AppleUSBCLightningAdapterAnalytics setMonitoring:]
+ -[AppleUSBCLightningAdapterAnalytics setQueue:]
+ -[AppleUSBCLightningAdapterAnalytics setStarted:]
+ -[AppleUSBCLightningAdapterAnalytics start]
+ -[AppleUSBCLightningAdapterAnalytics started]
+ -[AppleUSBCLightningAdapterAnalytics stop]
+ -[IOAnalyticsHIDSessionFilter setUsbCLightningAdapterAnalytics:]
+ -[IOAnalyticsHIDSessionFilter usbCLightningAdapterAnalytics]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/ACCAnalyticsConstants.o
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/AppleUSBCLightningAdapterAnalytics.o
+ /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/Common_ObjC/
+ ACCAnalyticsConstants.m
+ AppleUSBCLightningAdapterAnalytics.m
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._analyticsEventsEnabled
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._ioNotificationPort
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._ioServiceMatchingIterator
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._log
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._monitoring
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._queue
+ OBJC_IVAR_$_AppleUSBCLightningAdapterAnalytics._started
+ OBJC_IVAR_$_IOAnalyticsHIDSessionFilter._usbCLightningAdapterAnalytics
+ _AnalyticsSendEventLazy
+ _IOObjectRetain
+ _IORegistryEntryGetParentIterator
+ _NSStringFromClass
+ _OBJC_CLASS_$_AppleUSBCLightningAdapterAnalytics
+ _OBJC_METACLASS_$_AppleUSBCLightningAdapterAnalytics
+ __42-[AppleUSBCLightningAdapterAnalytics stop]_block_invoke.cold.1
+ __43-[AppleUSBCLightningAdapterAnalytics start]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_AppleUSBCLightningAdapterAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_AppleUSBCLightningAdapterAnalytics
+ __OBJC_$_PROP_LIST_AppleUSBCLightningAdapterAnalytics
+ __OBJC_CLASS_RO_$_AppleUSBCLightningAdapterAnalytics
+ __OBJC_METACLASS_RO_$_AppleUSBCLightningAdapterAnalytics
+ ___42-[AppleUSBCLightningAdapterAnalytics stop]_block_invoke
+ ___43-[AppleUSBCLightningAdapterAnalytics start]_block_invoke
+ ___60-[AppleUSBCLightningAdapterAnalytics _handleServiceMatched:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ __serviceMatched
+ _dispatch_sync
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUVDM_FirmwareVersion
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUVDM_HardwareVersion
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_AccessoryFirmwareVersion
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_AccessoryHardwareVersion
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_AccessoryManufacturer
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_AccessoryModel
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_AccessoryName
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_BD
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_CC
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_DB
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_HS
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_MB
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_PU
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_PWR
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_UART
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_DigitalID_USB
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_HID_PID
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_AID_HID_VID
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_FirmwareRevision
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_HardwareRevision
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_PID
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_ProductModelNumber
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_ProductName
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_ProductVendorName
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_MikeyBus_VID
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_AUXP_USBMode
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_ConnectionDurationS
+ _kACCCoreAnalytics_Event_USBCLightningAdapter_Disconnected_USB2_DataRole
+ _kIOMainPortDefault
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_handleServiceMatched:
+ _objc_msgSend$_startEventMonitoring
+ _objc_msgSend$_stopEventMonitoring
+ _objc_msgSend$analyticsEventsEnabled
+ _objc_msgSend$boolValue
+ _objc_msgSend$ioNotificationPort
+ _objc_msgSend$log
+ _objc_msgSend$monitoring
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$queue
+ _objc_msgSend$setIoNotificationPort:
+ _objc_msgSend$setMonitoring:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setStarted:
+ _objc_msgSend$start
+ _objc_msgSend$started
+ _objc_msgSend$stop
+ _objc_msgSend$stringWithFormat:
+ _objc_opt_new
CStrings:
+ "\x12"
+ "%@.%@.%@"
+ "@\"AppleUSBCLightningAdapterAnalytics\""
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_os_log>\""
+ "AID Info"
+ "AUVDM_FirmwareVersion"
+ "AUVDM_HardwareVersion"
+ "AUXP_AID_AccessoryFirmwareVersion"
+ "AUXP_AID_AccessoryHardwareVersion"
+ "AUXP_AID_AccessoryManufacturer"
+ "AUXP_AID_AccessoryModel"
+ "AUXP_AID_AccessoryName"
+ "AUXP_AID_DigitalID"
+ "AUXP_AID_DigitalID_BD"
+ "AUXP_AID_DigitalID_CC"
+ "AUXP_AID_DigitalID_DB"
+ "AUXP_AID_DigitalID_HS"
+ "AUXP_AID_DigitalID_MB"
+ "AUXP_AID_DigitalID_PU"
+ "AUXP_AID_DigitalID_PWR"
+ "AUXP_AID_DigitalID_UART"
+ "AUXP_AID_DigitalID_USB"
+ "AUXP_AID_HID_PID"
+ "AUXP_AID_HID_VID"
+ "AUXP_MikeyBus_FirmwareRevision"
+ "AUXP_MikeyBus_HardwareRevision"
+ "AUXP_MikeyBus_PID"
+ "AUXP_MikeyBus_ProductModelNumber"
+ "AUXP_MikeyBus_ProductName"
+ "AUXP_MikeyBus_ProductVendorName"
+ "AUXP_MikeyBus_VID"
+ "AUXP_USBMode"
+ "Accessory Firmware Version Major"
+ "Accessory Firmware Version Minor"
+ "Accessory Firmware Version Rev"
+ "Accessory HID PID"
+ "Accessory HID VID"
+ "Accessory Hardware Version Major"
+ "Accessory Hardware Version Minor"
+ "Accessory Hardware Version Rev"
+ "Accessory Manufacturer"
+ "Accessory Model"
+ "Accessory Name"
+ "Already started... ignoring!"
+ "Already stopped... ignoring!"
+ "Analytics disabled for this event - ignoring... (eventName: %@)"
+ "AppleUSBCLightningAdapterAnalytics"
+ "AppleUSBLightningAdapter"
+ "B"
+ "BuiltIn"
+ "ConnectionActiveDurationS"
+ "ConnectionDuration_S"
+ "DataRole"
+ "Digital ID"
+ "Failed to send analytics event! (eventName: %@)"
+ "Firmware Version"
+ "Hardware Version"
+ "I16@0:8"
+ "IOPort"
+ "IOPortTransportProtocolAppleUVDM"
+ "IOPortTransportStateUSB2"
+ "IOServiceAddMatchingNotification failed: %08x"
+ "MikeyBus Info"
+ "Product Firmware Revision"
+ "Product Hardware Revision"
+ "Product ID"
+ "Product Model Number"
+ "Product Name"
+ "Product Vendor ID"
+ "Product Vendor Name"
+ "Sending analytics event... (eventName: %@)"
+ "Service matched!"
+ "Starting %@..."
+ "Starting event monitoring..."
+ "Starting matching notifications..."
+ "Stopping %@..."
+ "Stopping event monitoring..."
+ "T@\"AppleUSBCLightningAdapterAnalytics\",&,N,V_usbCLightningAdapterAnalytics"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_os_log>\",&,N,V_log"
+ "TB,N,V_analyticsEventsEnabled"
+ "TB,N,V_monitoring"
+ "TB,N,V_started"
+ "TI,N,V_ioServiceMatchingIterator"
+ "T^{IONotificationPort=},N,V_ioNotificationPort"
+ "USB Mode"
+ "USB2_DataRole"
+ "UTF8String"
+ "^{IONotificationPort=}16@0:8"
+ "_analyticsEventsEnabled"
+ "_handleServiceMatched:"
+ "_ioNotificationPort"
+ "_ioServiceMatchingIterator"
+ "_log"
+ "_monitoring"
+ "_startEventMonitoring"
+ "_started"
+ "_stopEventMonitoring"
+ "_usbCLightningAdapterAnalytics"
+ "analyticsEventsEnabled"
+ "boolValue"
+ "com.apple.accessories"
+ "com.apple.accessories.USBCLightningAdapter.Disconnected"
+ "eventDict: %@"
+ "ioNotificationPort"
+ "ioServiceMatchingIterator"
+ "log"
+ "monitoring"
+ "numberWithUnsignedChar:"
+ "queue"
+ "setAnalyticsEventsEnabled:"
+ "setIoNotificationPort:"
+ "setIoServiceMatchingIterator:"
+ "setLog:"
+ "setMonitoring:"
+ "setObject:forKey:"
+ "setQueue:"
+ "setStarted:"
+ "setUsbCLightningAdapterAnalytics:"
+ "start"
+ "started"
+ "stop"
+ "stringWithFormat:"
+ "usbCLightningAdapterAnalytics"
+ "v20@0:8B16"
+ "v20@0:8I16"
+ "v24@0:8^{IONotificationPort=}16"
- "\x01"

```
