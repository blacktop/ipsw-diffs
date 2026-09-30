## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth`

```diff

-2700.51.0.0.0
-  __TEXT.__text: 0xdcab0
-  __TEXT.__objc_methlist: 0xd64c
-  __TEXT.__const: 0x2d39
+2701.3.0.0.0
+  __TEXT.__text: 0xdcdfc
+  __TEXT.__objc_methlist: 0xd6dc
+  __TEXT.__const: 0x2d49
   __TEXT.__oslogstring: 0x31cb
-  __TEXT.__cstring: 0x1b18d
+  __TEXT.__cstring: 0x1b194
   __TEXT.__gcc_except_tab: 0x2658
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x3ad8
+  __TEXT.__unwind_info: 0x3af0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c90
+  __DATA_CONST.__objc_selrefs: 0x5cc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x400
   __AUTH_CONST.__const: 0x1630
   __AUTH_CONST.__cfstring: 0x11040
-  __AUTH_CONST.__objc_const: 0x1c4e0
+  __AUTH_CONST.__objc_const: 0x1c590
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x978
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x1374
+  __DATA.__objc_ivar: 0x1380
   __DATA.__data: 0xf28
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1900

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5579
-  Symbols:   10202
-  CStrings:  5133
+  Functions: 5591
+  Symbols:   10223
+  CStrings:  5135
 
Symbols:
+ -[CBDevice _clearProximityServiceAccessoryCategory]
+ -[CBDevice _clearProximityServiceColorCode]
+ -[CBDevice proximityServiceAccessoryCategory]
+ -[CBDevice proximityServiceColorCode]
+ -[CBDevice setProximityServiceAccessoryCategory:]
+ -[CBDevice setProximityServiceColorCode:]
+ -[CBDeviceDataProximityService proximityServiceAccessoryCategory]
+ -[CBDeviceDataProximityService proximityServiceColorCode]
+ -[CBDeviceDataProximityService setProximityServiceAccessoryCategory:]
+ -[CBDeviceDataProximityService setProximityServiceColorCode:]
+ -[CBHomeKitProxAccessoryMetadata accessoryCategory]
+ -[CBHomeKitProxAccessoryMetadata setAccessoryCategory:]
+ GCC_except_table533
+ GCC_except_table540
+ GCC_except_table555
+ GCC_except_table620
+ OBJC_IVAR_$_CBDeviceDataProximityService._proximityServiceAccessoryCategory
+ OBJC_IVAR_$_CBDeviceDataProximityService._proximityServiceColorCode
+ OBJC_IVAR_$_CBHomeKitProxAccessoryMetadata._accessoryCategory
+ _CBAdvReportMetricHeySiri
+ _objc_msgSend$_clearProximityServiceAccessoryCategory
+ _objc_msgSend$_clearProximityServiceColorCode
+ _objc_msgSend$proximityServiceAccessoryCategory
+ _objc_msgSend$proximityServiceColorCode
+ _objc_msgSend$setProximityServiceAccessoryCategory:
+ _objc_msgSend$setProximityServiceColorCode:
- GCC_except_table527
- GCC_except_table534
- GCC_except_table549
- GCC_except_table614
- _CBManagerIsIOBluetoothShim
CStrings:
+ "MobileBluetooth-2701.3"
+ "kCBAdvReportMetricHeySiri"
+ "psAC"
+ "psCC"
- "MobileBluetooth-2700.51"
- "kCBManagerIsIOBluetoothShim"
```
