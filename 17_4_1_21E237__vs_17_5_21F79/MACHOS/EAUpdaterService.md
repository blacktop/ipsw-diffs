## EAUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService`

```diff

-975.100.86.0.1
-  __TEXT.__text: 0x10550
+975.120.15.0.0
+  __TEXT.__text: 0x108b4
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_stubs: 0x31e0
   __TEXT.__objc_methlist: 0xbe0
-  __TEXT.__cstring: 0x6aae
+  __TEXT.__cstring: 0x6b03
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__objc_methname: 0x3853
-  __TEXT.__oslogstring: 0x233
+  __TEXT.__oslogstring: 0x265
   __TEXT.__objc_classname: 0x107
   __TEXT.__objc_methtype: 0x794
   __TEXT.__dlopen_cstrs: 0x52

   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xf00
-  __DATA_CONST.__cfstring: 0x5b60
+  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__cfstring: 0x5b80
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 349
-  Symbols:   587
-  CStrings:  1676
+  Functions: 350
+  Symbols:   589
+  CStrings:  1679
 
Symbols:
+ _getAccessoryDatabaseKeyForAccessoryID
+ _kAccessoryReachableKey
+ _updateReachabilityForAccessoryID
- _getAccessoryDatabaseForAccessoryID
CStrings:
+ "%s: Not adding empty serial number with info = %@"
+ "-[AUDeveloperSettingsDatabase addAccessoryWithSerialNumber:info:]"
+ "DawnF"
+ "accessoryReachable"
- "DawnE"

```
