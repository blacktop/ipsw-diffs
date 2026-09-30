## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

```diff

-5.0.13.0.0
-  __TEXT.__text: 0x39214
+5.0.15.1.0
+  __TEXT.__text: 0x39a98
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__delay_helper: 0x220
-  __TEXT.__objc_stubs: 0x45c0
-  __TEXT.__objc_methlist: 0x2858
-  __TEXT.__const: 0x140
-  __TEXT.__objc_methname: 0x6073
-  __TEXT.__cstring: 0x8f08
+  __TEXT.__objc_stubs: 0x4620
+  __TEXT.__objc_methlist: 0x2888
+  __TEXT.__const: 0x150
+  __TEXT.__objc_methname: 0x6107
+  __TEXT.__cstring: 0x904b
   __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methtype: 0x1d96
-  __TEXT.__gcc_except_tab: 0x710
+  __TEXT.__objc_methtype: 0x1da2
+  __TEXT.__gcc_except_tab: 0x764
   __TEXT.__oslogstring: 0xac4
-  __TEXT.__unwind_info: 0xae0
+  __TEXT.__unwind_info: 0xaf8
   __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x5900
+  __DATA_CONST.__cfstring: 0x59e0
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x6158
-  __DATA.__objc_selrefs: 0x1780
-  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_const: 0x6178
+  __DATA.__objc_selrefs: 0x1798
+  __DATA.__objc_ivar: 0x4d4
   __DATA.__objc_data: 0x1360
-  __DATA.__data: 0xa28
+  __DATA.__data: 0xa60
   __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A54A752-F58F-3D44-BD29-0D6C25DB46F7
-  Functions: 952
-  Symbols:   288
-  CStrings:  3275
+  UUID: E9BEA545-C355-3E84-99B3-7A179700EDBB
+  Functions: 957
+  Symbols:   290
+  CStrings:  3296
 
Symbols:
+ _STSBluetoothErrorDescriptions
+ _STSWifiErrorDescriptions
CStrings:
+ "-[ISO18013_3_Central _isBTPowerOn:]"
+ "-[ISO18013_3_Peripheral _isBTPowerOn:]"
+ "-[STSXPCHelper _iso18013DeviceProcessRequest:]_block_invoke_4"
+ "<%@ isHandoverSessionEstablishmentSupported=%@ isExtendedRequestSupported=%@ isReaderAuthAllSupported=%@>"
+ "B24@0:8^q16"
+ "ISODeviceEngagementCapabilitiesExtendedRequestSupported"
+ "Network cancelled"
+ "Power off"
+ "Previously started"
+ "Self reset"
+ "Unable to determine BT state, assumes off"
+ "Underlying P2P Error"
+ "Unexpected BT power state"
+ "Waiting on state update, current value=%ld"
+ "_extendedRequestSupported"
+ "_isBTPowerOn:"
+ "_startCBCentralManagerAndWaitForPowerOn"
+ "_startCBPeripheralManagerAndWaitForPowerOn"
+ "dateWithTimeIntervalSinceNow:"
- "%ld"
- "-[STSXPCHelper _iso18013DeviceProcessRequest:]_block_invoke_3"
- "<%@ isHandoverSessionEstablishmentSupported=%@ isReaderAuthAllSupported=%@>"
- "Waiting on state update"
- "wait"

```
