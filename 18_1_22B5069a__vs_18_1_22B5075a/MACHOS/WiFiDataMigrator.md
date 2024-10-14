## WiFiDataMigrator

> `/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator`

```diff

-1760.7.0.0.0
-  __TEXT.__text: 0x1cec
-  __TEXT.__auth_stubs: 0x3d0
+1760.8.0.0.0
+  __TEXT.__text: 0x1d4c
+  __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x321
+  __TEXT.__cstring: 0x345
   __TEXT.__oslogstring: 0x289
   __TEXT.__objc_classname: 0x11
-  __TEXT.__objc_methname: 0x246
-  __TEXT.__objc_methtype: 0xa7
+  __TEXT.__objc_methname: 0x25b
+  __TEXT.__objc_methtype: 0xaa
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 27
-  Symbols:   100
-  CStrings:  81
+  Symbols:   101
+  CStrings:  82
 
Symbols:
+ _WiFiNetworkIsCarPlay
CStrings:
+ "UpdatePrivateMacReasonLegacyCarplay"
+ "migratePrivateMacAddress:network:upgradeToRotate:upgradeToTriState:upgradeLegacyCarplay:"
+ "v44@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24B32B36B40"
- "migratePrivateMacAddress:network:upgradeToRotate:upgradeToTriState:"
- "v40@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24B32B36"

```
