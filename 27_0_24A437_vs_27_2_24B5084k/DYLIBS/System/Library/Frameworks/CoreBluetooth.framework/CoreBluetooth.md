## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-2700.51.1.3.0
-  __TEXT.__text: 0xd3c8c
-  __TEXT.__objc_methlist: 0xd6a4
-  __TEXT.__const: 0x2d49
+2701.3.0.0.0
+  __TEXT.__text: 0xd3fe0
+  __TEXT.__objc_methlist: 0xd734
+  __TEXT.__const: 0x2d59
   __TEXT.__oslogstring: 0x320b
-  __TEXT.__cstring: 0x1af09
+  __TEXT.__cstring: 0x1af0c
   __TEXT.__gcc_except_tab: 0x25f8
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x3ab8
+  __TEXT.__unwind_info: 0x3ad0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cc8
+  __DATA_CONST.__objc_selrefs: 0x5cf8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x420
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__cfstring: 0x11260
-  __AUTH_CONST.__objc_const: 0x1c580
+  __AUTH_CONST.__objc_const: 0x1c630
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xa30
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x1374
+  __DATA.__objc_ivar: 0x1380
   __DATA.__data: 0xf98
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1770

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5531
-  Symbols:   10160
-  CStrings:  5124
+  Functions: 5543
+  Symbols:   10181
+  CStrings:  5126
 
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
+ GCC_except_table538
+ GCC_except_table553
+ GCC_except_table616
+ _CBAdvReportMetricHeySiri
+ _OBJC_IVAR_$_CBDeviceDataProximityService._proximityServiceAccessoryCategory
+ _OBJC_IVAR_$_CBDeviceDataProximityService._proximityServiceColorCode
+ _OBJC_IVAR_$_CBHomeKitProxAccessoryMetadata._accessoryCategory
+ _objc_msgSend$_clearProximityServiceAccessoryCategory
+ _objc_msgSend$_clearProximityServiceColorCode
+ _objc_msgSend$proximityServiceAccessoryCategory
+ _objc_msgSend$proximityServiceColorCode
+ _objc_msgSend$setProximityServiceAccessoryCategory:
+ _objc_msgSend$setProximityServiceColorCode:
- GCC_except_table527
- GCC_except_table532
- GCC_except_table547
- GCC_except_table610
- _CBManagerIsIOBluetoothShim
CStrings:
+ "MobileBluetooth-2701.3"
+ "kCBAdvReportMetricHeySiri"
+ "psAC"
+ "psCC"
- "MobileBluetooth-2700.51.1.3"
- "kCBManagerIsIOBluetoothShim"
```
