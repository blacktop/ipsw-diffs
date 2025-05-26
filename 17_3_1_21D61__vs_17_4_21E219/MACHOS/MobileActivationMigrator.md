## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-898.60.6.0.0
-  __TEXT.__text: 0x2974
+921.100.31.0.0
+  __TEXT.__text: 0x2978
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__cstring: 0x2cab
+  __TEXT.__cstring: 0x2d56
   __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0xc0c
+  __TEXT.__objc_methname: 0xc20
   __TEXT.__objc_methtype: 0x2da
   __TEXT.__oslogstring: 0x28
   __TEXT.__const: 0x28

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__cfstring: 0x45e0
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__cfstring: 0x4700
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x330
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x370
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x818
   __DATA.__objc_selrefs: 0x218
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x98
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x5c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 56
-  Symbols:   1420
-  CStrings:  729
+  Symbols:   1422
+  CStrings:  739
 
Symbols:
+ __44-[MobileActivationMigrator performMigration]_block_invoke.91
+ __block_literal_global.302
+ __block_literal_global.334
+ __block_literal_global.342
+ _kMAPreDawnDataMigrationCompleted
+ _unnamed_array_storage.331
+ _unnamed_array_storage.336
- __44-[MobileActivationMigrator performMigration]_block_invoke.90
- __block_literal_global.278
- __block_literal_global.310
- __block_literal_global.318
- _unnamed_array_storage.307
- _unnamed_array_storage.312
CStrings:
+ "MapsTransactionInsightsExtension"
+ "MobileAssetLibTests-Runner"
+ "Passbook"
+ "PreDawnDataMigrationCompleted"
+ "SPREngineIntegrationTests-Runner"
+ "T@\"NSString\",?,R,C"
+ "asutil"
+ "financed"
+ "mapspushd"
+ "mobileassetd"

```
