## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-919.100.33.0.0
-  __TEXT.__text: 0xaae4
+919.120.14.0.1
+  __TEXT.__text: 0xb81c
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x51c
+  __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x18
-  __TEXT.__objc_methname: 0xdbb
-  __TEXT.__cstring: 0x12db
+  __TEXT.__objc_methname: 0xe27
+  __TEXT.__cstring: 0x138e
   __TEXT.__oslogstring: 0xac1
-  __TEXT.__objc_classname: 0xc5
-  __TEXT.__objc_methtype: 0x44d
+  __TEXT.__objc_classname: 0xde
+  __TEXT.__objc_methtype: 0x467
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__unwind_info: 0x2a8
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x1c60
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__cfstring: 0x1d40
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xec0
-  __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_ivar: 0x88
-  __DATA.__objc_data: 0x230
-  __DATA.__data: 0x160
+  __DATA.__objc_const: 0x10e0
+  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x178
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FEE5BAF-C871-3DD3-B506-8B3A2AF4C2A7
-  Functions: 241
-  Symbols:   2057
-  CStrings:  798
+  UUID: D7D8A8FC-771D-33D8-9C5B-5C360C54598A
+  Functions: 277
+  Symbols:   2284
+  CStrings:  820
 
Symbols:
+ -[AppleFireWireAnalytics .cxx_destruct]
+ -[AppleFireWireAnalytics _handleServiceMatched:]
+ -[AppleFireWireAnalytics _handleServiceMatched:].cold.1
+ -[AppleFireWireAnalytics _handleServiceMatched:].cold.2
+ -[AppleFireWireAnalytics _startEventMonitoring]
+ -[AppleFireWireAnalytics _startEventMonitoring].cold.1
+ -[AppleFireWireAnalytics _stopEventMonitoring]
+ -[AppleFireWireAnalytics analyticsEventsEnabled]
+ -[AppleFireWireAnalytics init]
+ -[AppleFireWireAnalytics ioNotificationPort]
+ -[AppleFireWireAnalytics ioServiceMatchingIterator]
+ -[AppleFireWireAnalytics log]
+ -[AppleFireWireAnalytics monitoring]
+ -[AppleFireWireAnalytics queue]
+ -[AppleFireWireAnalytics setAnalyticsEventsEnabled:]
+ -[AppleFireWireAnalytics setIoNotificationPort:]
+ -[AppleFireWireAnalytics setIoServiceMatchingIterator:]
+ -[AppleFireWireAnalytics setLog:]
+ -[AppleFireWireAnalytics setMonitoring:]
+ -[AppleFireWireAnalytics setQueue:]
+ -[AppleFireWireAnalytics setStarted:]
+ -[AppleFireWireAnalytics start]
+ -[AppleFireWireAnalytics started]
+ -[AppleFireWireAnalytics stop]
+ -[IOAnalyticsHIDSessionFilter firewireAnalytics]
+ -[IOAnalyticsHIDSessionFilter setFirewireAnalytics:]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/AppleFireWireAnalytics.o
+ AppleFireWireAnalytics.m
+ OBJC_IVAR_$_AppleFireWireAnalytics._analyticsEventsEnabled
+ OBJC_IVAR_$_AppleFireWireAnalytics._ioNotificationPort
+ OBJC_IVAR_$_AppleFireWireAnalytics._ioServiceMatchingIterator
+ OBJC_IVAR_$_AppleFireWireAnalytics._log
+ OBJC_IVAR_$_AppleFireWireAnalytics._monitoring
+ OBJC_IVAR_$_AppleFireWireAnalytics._queue
+ OBJC_IVAR_$_AppleFireWireAnalytics._started
+ OBJC_IVAR_$_IOAnalyticsHIDSessionFilter._firewireAnalytics
+ _OBJC_CLASS_$_AppleFireWireAnalytics
+ _OBJC_METACLASS_$_AppleFireWireAnalytics
+ __30-[AppleFireWireAnalytics stop]_block_invoke.cold.1
+ __31-[AppleFireWireAnalytics start]_block_invoke.cold.1
+ __31-[AppleFireWireAnalytics start]_block_invoke.cold.2
+ __OBJC_$_INSTANCE_METHODS_AppleFireWireAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_AppleFireWireAnalytics
+ __OBJC_$_PROP_LIST_AppleFireWireAnalytics
+ __OBJC_CLASS_RO_$_AppleFireWireAnalytics
+ __OBJC_METACLASS_RO_$_AppleFireWireAnalytics
+ ___30-[AppleFireWireAnalytics stop]_block_invoke
+ ___31-[AppleFireWireAnalytics start]_block_invoke
+ ___48-[AppleFireWireAnalytics _handleServiceMatched:]_block_invoke
+ _kAppleFireWireAnalytics_Event_IOFireWireDevice_FirstMatch
+ _kAppleFireWireAnalytics_Event_IOFireWireDevice_ProductName
+ _kAppleFireWireAnalytics_Event_IOFireWireDevice_VendorID
+ _kAppleFireWireAnalytics_Event_IOFireWireDevice_VendorName
+ _kAppleFireWireAnalytics_IOFireWireDevice_Property_ProductName
+ _kAppleFireWireAnalytics_IOFireWireDevice_Property_VendorID
+ _kAppleFireWireAnalytics_IOFireWireDevice_Property_VendorName
CStrings:
+ "\x04"
+ "@\"AppleFireWireAnalytics\""
+ "AppleFireWireAnalytics"
+ "FireWire Product Name"
+ "FireWire Vendor Name"
+ "FireWire_ProductName"
+ "FireWire_VendorID"
+ "FireWire_VendorName"
+ "IOFireWireDevice"
+ "T@\"AppleFireWireAnalytics\",&,N,V_firewireAnalytics"
+ "Vendor_ID"
+ "_firewireAnalytics"
+ "com.apple.accessories.IOFireWireDevice.FirstMatch"
+ "firewireAnalytics"
+ "setFirewireAnalytics:"

```
