## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1015.60.1.0.0
-  __TEXT.__text: 0x28c4
+1017.100.15.0.0
+  __TEXT.__text: 0x2868
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2f7e
+  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__cstring: 0x2f9a
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc12
   __TEXT.__objc_methtype: 0x2da
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x118
   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf50
-  __DATA_CONST.__cfstring: 0x4aa0
+  __DATA_CONST.__const: 0xf58
+  __DATA_CONST.__cfstring: 0x4ae0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x440
+  __DATA_CONST.__objc_arraydata: 0x448
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x838
-  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_const: 0x328
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 53
-  Symbols:   1424
-  CStrings:  766
+  Functions: 59
+  Symbols:   1455
+  CStrings:  768
 
Symbols:
+ +[GestaltHlpr getSharedInstance].cold.1
+ __block_literal_global.362
+ __block_literal_global.394
+ __block_literal_global.402
+ _kMAOptionsBAAClientNameSuffix
+ data_migration_supported.cold.1
+ isRunningInDiagnosticsMode.cold.1
+ isSupportedActivationLockClient.cold.2
+ isSupportedDeviceIdentityClient.cold.2
+ isSupportedRecoveryLogClient.cold.1
+ is_erase_installed_build.cold.1
+ is_upgrade_installed_build.cold.1
- __block_literal_global.359
- __block_literal_global.391
- __block_literal_global.399
CStrings:
+ "BAAClientNameSuffix"
+ "imagent"

```
