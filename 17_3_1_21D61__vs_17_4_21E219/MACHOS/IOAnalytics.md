## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0x980c
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x3fc
+919.100.33.0.0
+  __TEXT.__text: 0xaae4
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x51c
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x115b
-  __TEXT.__objc_methname: 0xd07
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methtype: 0x437
+  __TEXT.__objc_methname: 0xdbb
+  __TEXT.__cstring: 0x12db
+  __TEXT.__oslogstring: 0xac1
+  __TEXT.__objc_classname: 0xc5
+  __TEXT.__objc_methtype: 0x44d
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0xa0e
-  __TEXT.__unwind_info: 0x22c
-  __DATA_CONST.__auth_got: 0x2d8
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x740
-  __DATA_CONST.__cfstring: 0x1980
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__cfstring: 0x1c60
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x390
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xca0
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x120
+  __DATA.__objc_const: 0xec0
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x160
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6519898-4330-30F6-82D6-AAE48D99C9C0
-  Functions: 203
-  Symbols:   1786
-  CStrings:  733
+  UUID: 18F1A872-7A49-3C5C-A1F3-E25326A0F017
+  Functions: 241
+  Symbols:   2057
+  CStrings:  798
 
Symbols:
+ -[ApplePCIeAnalytics .cxx_destruct]
+ -[ApplePCIeAnalytics _handleServiceMatched:]
+ -[ApplePCIeAnalytics _handleServiceMatched:].cold.1
+ -[ApplePCIeAnalytics _handleServiceMatched:].cold.2
+ -[ApplePCIeAnalytics _startEventMonitoring]
+ -[ApplePCIeAnalytics _startEventMonitoring].cold.1
+ -[ApplePCIeAnalytics _stopEventMonitoring]
+ -[ApplePCIeAnalytics analyticsEventsEnabled]
+ -[ApplePCIeAnalytics init]
+ -[ApplePCIeAnalytics ioNotificationPort]
+ -[ApplePCIeAnalytics ioServiceMatchingIterator]
+ -[ApplePCIeAnalytics log]
+ -[ApplePCIeAnalytics monitoring]
+ -[ApplePCIeAnalytics queue]
+ -[ApplePCIeAnalytics setAnalyticsEventsEnabled:]
+ -[ApplePCIeAnalytics setIoNotificationPort:]
+ -[ApplePCIeAnalytics setIoServiceMatchingIterator:]
+ -[ApplePCIeAnalytics setLog:]
+ -[ApplePCIeAnalytics setMonitoring:]
+ -[ApplePCIeAnalytics setQueue:]
+ -[ApplePCIeAnalytics setStarted:]
+ -[ApplePCIeAnalytics start]
+ -[ApplePCIeAnalytics started]
+ -[ApplePCIeAnalytics stop]
+ -[IOAnalyticsHIDSessionFilter pcieAnalytics]
+ -[IOAnalyticsHIDSessionFilter setPcieAnalytics:]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/ApplePCIeAnalytics.o
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/ApplePCIeAnalyticsConstants.o
+ ApplePCIeAnalytics.m
+ ApplePCIeAnalyticsConstants.m
+ OBJC_IVAR_$_ApplePCIeAnalytics._analyticsEventsEnabled
+ OBJC_IVAR_$_ApplePCIeAnalytics._ioNotificationPort
+ OBJC_IVAR_$_ApplePCIeAnalytics._ioServiceMatchingIterator
+ OBJC_IVAR_$_ApplePCIeAnalytics._log
+ OBJC_IVAR_$_ApplePCIeAnalytics._monitoring
+ OBJC_IVAR_$_ApplePCIeAnalytics._queue
+ OBJC_IVAR_$_ApplePCIeAnalytics._started
+ OBJC_IVAR_$_IOAnalyticsHIDSessionFilter._pcieAnalytics
+ _IOServiceGetMatchingService
+ _OBJC_CLASS_$_ApplePCIeAnalytics
+ _OBJC_METACLASS_$_ApplePCIeAnalytics
+ __26-[ApplePCIeAnalytics stop]_block_invoke.cold.1
+ __27-[ApplePCIeAnalytics start]_block_invoke.cold.1
+ __27-[ApplePCIeAnalytics start]_block_invoke.cold.2
+ __OBJC_$_INSTANCE_METHODS_ApplePCIeAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_ApplePCIeAnalytics
+ __OBJC_$_PROP_LIST_ApplePCIeAnalytics
+ __OBJC_CLASS_RO_$_ApplePCIeAnalytics
+ __OBJC_METACLASS_RO_$_ApplePCIeAnalytics
+ ___26-[ApplePCIeAnalytics stop]_block_invoke
+ ___27-[ApplePCIeAnalytics start]_block_invoke
+ ___44-[ApplePCIeAnalytics _handleServiceMatched:]_block_invoke
+ _convertNSDataToHexString
+ _getPropFromReg
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_ATCPort
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_ClassCode
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_DeviceID
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_IsPCIe
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_LinkSpeed
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_LinkWidth
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_PCIeCapabilities
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_PCIeLinkCapabilities
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_Slot
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_SubsystemID
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_SubsystemVendorID
+ _kApplePCIeAnalytics_Event_IOPCIDevice_FirstMatch_VendorID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_ClassCode
+ _kApplePCIeAnalytics_IOPCIDevice_Property_DeviceID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_RouterID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_SlotName
+ _kApplePCIeAnalytics_IOPCIDevice_Property_SubsystemID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_SubsystemVendorID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_ThunderboltEntryID
+ _kApplePCIeAnalytics_IOPCIDevice_Property_VendorID
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$setValue:forKey:
+ _objc_retain_x26
+ _strtol
CStrings:
+ "%@ already started... ignoring!"
+ "%@ already stopped... ignoring!"
+ "%@ failed to start!"
+ "0x%X"
+ "@\"ApplePCIeAnalytics\""
+ "AAPL,slot-name"
+ "Analytics events are disabled for this event - ignoring... (eventName: %@)"
+ "ApplePCIeAnalytics"
+ "IOPCI2PCIBridge"
+ "IOPCIDevice"
+ "IOPCIExpressCapabilities"
+ "IOPCIExpressLinkCapabilities"
+ "PCIe_Capabilities"
+ "PCIe_ClassCode"
+ "PCIe_DID"
+ "PCIe_LinkCapabilities"
+ "PCIe_Subsystem_ID"
+ "PCIe_Subsystem_VID"
+ "PCIe_VID"
+ "T@\"ApplePCIeAnalytics\",&,N,V_pcieAnalytics"
+ "T@\"NSString\",?,R,C"
+ "Thunderbolt Entry ID"
+ "_pcieAnalytics"
+ "atcPort"
+ "class-code"
+ "com.apple.accessories.IOPCIDevice.FirstMatch"
+ "device-id"
+ "eventDictionary: %@"
+ "getBytes:length:"
+ "isPCIe"
+ "linkSpeed"
+ "linkWidth"
+ "numberWithBool:"
+ "numberWithLong:"
+ "pcieAnalytics"
+ "setPcieAnalytics:"
+ "setValue:forKey:"
+ "slot"
+ "subsystem-id"
+ "subsystem-vendor-id"
+ "vendor-id"

```
