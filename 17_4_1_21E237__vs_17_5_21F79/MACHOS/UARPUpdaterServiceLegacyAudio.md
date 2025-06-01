## UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

-975.100.86.0.1
-  __TEXT.__text: 0x222ac
+975.120.15.0.0
+  __TEXT.__text: 0x226ac
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_stubs: 0x4360
   __TEXT.__objc_methlist: 0x132c
-  __TEXT.__cstring: 0x8128
+  __TEXT.__cstring: 0x817d
   __TEXT.__const: 0x2c0
   __TEXT.__objc_methname: 0x4e82
   __TEXT.__objc_classname: 0x24e
   __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__oslogstring: 0x72b
+  __TEXT.__oslogstring: 0x75d
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__unwind_info: 0x804
   __DATA_CONST.__auth_got: 0x560
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1528
-  __DATA_CONST.__cfstring: 0x68e0
+  __DATA_CONST.__const: 0x1530
+  __DATA_CONST.__cfstring: 0x6900
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20900253-7CDE-3767-BDFD-7A40DD7FEC40
-  Functions: 949
-  Symbols:   1132
-  CStrings:  3093
+  UUID: 4FEFD981-0C2C-30B4-9AC7-D062F81AC97E
+  Functions: 950
+  Symbols:   1134
+  CStrings:  3097
 
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
