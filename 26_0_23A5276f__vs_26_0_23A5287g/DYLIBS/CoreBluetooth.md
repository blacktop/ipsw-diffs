## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-190.43.0.0.0
-  __TEXT.__text: 0xb41a0
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0xa074
+190.45.1.0.0
+  __TEXT.__text: 0xb421c
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0xa084
   __TEXT.__const: 0x271b
   __TEXT.__oslogstring: 0x2b1b
-  __TEXT.__cstring: 0x14f22
+  __TEXT.__cstring: 0x14f61
   __TEXT.__gcc_except_tab: 0x2f40
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__unwind_info: 0x2148
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x805
-  __TEXT.__objc_methname: 0x16bb8
+  __TEXT.__objc_methname: 0x16be8
   __TEXT.__objc_methtype: 0x251a
-  __TEXT.__objc_stubs: 0xb680
+  __TEXT.__objc_stubs: 0xb6a0
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x5578
+  __DATA_CONST.__const: 0x5580
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ff8
+  __DATA_CONST.__objc_selrefs: 0x5008
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__cfstring: 0xdc20
   __AUTH_CONST.__objc_const: 0x11e68
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDB11C70-DF5F-31E4-9D5F-C7C5782675B5
-  Functions: 4237
-  Symbols:   13782
-  CStrings:  10438
+  UUID: 4D8A7A0C-E1C3-3AAE-8A17-913F2DF691BF
+  Functions: 4240
+  Symbols:   13793
+  CStrings:  10448
 
Symbols:
+ -[CBClassicManager sendLocalDeviceStateRequest]
+ -[CBManager getLocalDeviceState]
+ _CBUUIDMFiAuthPSMCharacteristicString
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _objc_msgSend$getLocalDeviceState
CStrings:
+ "7401DD11-3558-4459-98EE-371BBFC84C45"
+ "MFi Auth PSM"
+ "MobileBluetooth-190.45.1"
+ "false"
+ "getLocalDeviceState"
+ "sendLocalDeviceStateRequest"
+ "true"
- "MobileBluetooth-190.43"

```
