## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.60.12.0.0
-  __TEXT.__text: 0x60a44
+1188.80.10.0.0
+  __TEXT.__text: 0x60a68
   __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_methlist: 0x1e1c
+  __TEXT.__objc_methlist: 0x1e24
   __TEXT.__const: 0x3a0
   __TEXT.__cstring: 0xd352
   __TEXT.__oslogstring: 0x3439

   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0x1690
   __TEXT.__objc_classname: 0x30c
-  __TEXT.__objc_methname: 0x4faf
+  __TEXT.__objc_methname: 0x4ff8
   __TEXT.__objc_methtype: 0x1595
-  __TEXT.__objc_stubs: 0x4080
+  __TEXT.__objc_stubs: 0x40a0
   __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__const: 0x27d8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x1538
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x4130
   __AUTH_CONST.__auth_got: 0xcb8
   __AUTH_CONST.__const: 0x940
   __AUTH_CONST.__cfstring: 0x17e60
-  __AUTH_CONST.__objc_const: 0x3510
+  __AUTH_CONST.__objc_const: 0x3540
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x264
+  __DATA.__objc_ivar: 0x268
   __DATA.__data: 0x8d8
   __DATA.__bss: 0x330
   __DATA.__common: 0x30

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3640EBFC-A2D6-34A2-A561-CA1C12CA0750
-  Functions: 1880
-  Symbols:   5830
-  CStrings:  7879
+  UUID: 3C44ACE2-BE34-3060-B410-50F876F190B0
+  Functions: 1882
+  Symbols:   5836
+  CStrings:  7882
 
Symbols:
+ -[PCSMigrationState setRecordTypeForReading:]
+ GCC_except_table129
+ GCC_except_table137
+ GCC_except_table155
+ GCC_except_table173
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table194
+ GCC_except_table198
+ _OBJC_IVAR_$_PCSMigrationState._recordTypeForReading
+ _OUTLINED_FUNCTION_16
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.848
+ ___PCSEngineAddMissingCurrentPointers_block_invoke.851
+ ___PCSEngineExtractKeys_block_invoke.575
+ ___PCSEngineExtractKeys_block_invoke.586
+ ___PCSEngineStoreHSM_block_invoke.740
+ ___block_literal_global.1049
+ ___block_literal_global.784
+ _objc_msgSend$setRecordTypeForReading:
- GCC_except_table128
- GCC_except_table136
- GCC_except_table154
- GCC_except_table172
- GCC_except_table177
- GCC_except_table181
- GCC_except_table193
- GCC_except_table197
- ___PCSEngineAddMissingCurrentPointers_block_invoke.844
- ___PCSEngineAddMissingCurrentPointers_block_invoke.847
- ___PCSEngineExtractKeys_block_invoke.571
- ___PCSEngineExtractKeys_block_invoke.582
- ___PCSEngineStoreHSM_block_invoke.736
- ___block_literal_global.1045
- ___block_literal_global.780
Functions:
~ _OUTLINED_FUNCTION_2 : 24 -> 12
~ _OUTLINED_FUNCTION_1 : 12 -> 24
+ -[PCSMigrationState done]
- -[PCSMigrationState done]
+ -[PCSMigrationState iCDP]
- -[PCSMigrationState modified]
+ -[PCSMigrationState brokenEncryptedMetadatakeys]
- -[PCSMigrationState restart]
+ -[PCSMigrationState escrowMissing]
- -[PCSMigrationState escrowMissing]
+ -[PCSMigrationState setRecordTypeForReading:]
~ _OUTLINED_FUNCTION_5 : 12 -> 16
~ _OUTLINED_FUNCTION_7 : 16 -> 12
~ _OUTLINED_FUNCTION_12 : 28 -> 12
~ _OUTLINED_FUNCTION_14 : 24 -> 28
+ _OUTLINED_FUNCTION_16
~ _PCSIdentityMigrateEngineCreate : 468 -> 488
~ _PCSEngineStoreLocal.cold.1 : 60 -> 56
CStrings:
+ "TI,V_recordTypeForReading"
+ "_recordTypeForReading"
+ "setRecordTypeForReading:"

```
