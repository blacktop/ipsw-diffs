## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1627.0.0.0.0
-  __TEXT.__text: 0x331154
-  __TEXT.__objc_methlist: 0x108d8
+1629.1.0.0.0
+  __TEXT.__text: 0x33173c
+  __TEXT.__objc_methlist: 0x108f8
   __TEXT.__const: 0x2e30
   __TEXT.__constg_swiftt: 0x9d8
   __TEXT.__swift5_typeref: 0x12d0

   __TEXT.__swift5_types: 0xd4
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift5_capture: 0x340
-  __TEXT.__cstring: 0x3bf28
+  __TEXT.__cstring: 0x3bf73
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x187c8
-  __TEXT.__oslogstring: 0x36910
-  __TEXT.__unwind_info: 0x77d8
+  __TEXT.__gcc_except_tab: 0x1883c
+  __TEXT.__oslogstring: 0x36900
+  __TEXT.__unwind_info: 0x7808
   __TEXT.__eh_frame: 0x9d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4be8
+  __DATA_CONST.__const: 0x4c38
   __DATA_CONST.__objc_classlist: 0xed8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6240
+  __DATA_CONST.__objc_selrefs: 0x6258
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xbb8
   __DATA_CONST.__objc_arraydata: 0x8860
   __DATA_CONST.__got: 0xca0
   __AUTH_CONST.__const: 0x2dd8
   __AUTH_CONST.__cfstring: 0x1fdc0
-  __AUTH_CONST.__objc_const: 0x25dc8
+  __AUTH_CONST.__objc_const: 0x25df8
   __AUTH_CONST.__objc_dictobj: 0x2698
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x8f88

   __AUTH_CONST.__auth_got: 0x17e0
   __AUTH.__objc_data: 0x32d8
   __AUTH.__data: 0x238
-  __DATA.__objc_ivar: 0x1898
+  __DATA.__objc_ivar: 0x189c
   __DATA.__data: 0x1660
   __DATA.__bss: 0x16d0
   __DATA.__common: 0x650

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9338
-  Symbols:   20132
-  CStrings:  8339
+  Functions: 9344
+  Symbols:   20144
+  CStrings:  8340
 
Symbols:
+ -[NSCoreDataCoreSpotlightDelegate _handleSpotlightWipeTimeoutError:]
+ -[NSPersistentCloudKitContainerOptions initWithContainer:scheduler:]
+ -[NSPersistentCloudKitContainerOptions setTestSchedulerOverride:]
+ -[NSPersistentCloudKitContainerOptions testSchedulerOverride]
+ GCC_except_table88
+ _$s8CoreData13CDSwiftResultV8populate4from5using14columnMetadata16compositeIndices14requestContext11moidFactory03oidO0ySo18FetchResultsRow_stVz_So0Q10EntityPlanazSayAA06ColumnI0VGs15ContiguousArrayVySiGSo017NSSQLFetchRequestM0CSo17NSManagedObjectIDCs5Int64VXEAYA_cSo11NSSQLEntityCXEtF49$ss5Int64VSo17NSManagedObjectIDCIegnr_AbDIegyo_TRA_AYIegnr_105$sSo11NSSQLEntityCxq_Ri_zRi0_zRi__Ri0__r0_lys5Int64VSo17NSManagedObjectIDCIsegnr_Iegnr_AbdFIegyo_Ieggo_TRA1_xq_Ri_zRi0_zRi__Ri0__r0_lyA_AYIsegnr_Iegnr_Tf1nnnnnEEn_n
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerOptions._testSchedulerOverride
+ ___77-[NSCoreDataCoreSpotlightDelegate _resetSpotlightIndexWithCompletionHandler:]_block_invoke
+ ___77-[NSCoreDataCoreSpotlightDelegate deleteSpotlightIndexWithCompletionHandler:]_block_invoke_3
+ ___block_descriptor_48_e8_32b40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_56_e8_32o40b48r_e5_v8?0ls40l8r48l8s32l8
+ _objc_msgSend$initWithContainer:scheduler:
+ _objc_msgSend$testSchedulerOverride
- _$s8CoreData13CDSwiftResultV8populate4from5using14columnMetadata16compositeIndices14requestContext11moidFactory03oidO0ySo18FetchResultsRow_stVz_So0Q10EntityPlanazSayAA06ColumnI0VGs15ContiguousArrayVySiGSo017NSSQLFetchRequestM0CSo17NSManagedObjectIDCs5Int64VXEAYA_cSo11NSSQLEntityCXEtF49$ss5Int64VSo17NSManagedObjectIDCIegnr_AbDIegyo_TRA_AYIegnr_105$sSo11NSSQLEntityCxq_Ri_zRi0_zRi__Ri0__r0_lys5Int64VSo17NSManagedObjectIDCIsegnr_Iegnr_AbdFIegyo_Ieggo_TRA1_xq_Ri_zRi0_zRi__Ri0__r0_lyA_AYIsegnr_Iegnr_Tf1nnnnnccn_n
CStrings:
+ "CDCS pre-reindex wipe reported error; continuing to reindex anyway (index %@): %@"
+ "CREATE TRIGGER IF NOT EXISTS %@_DELETE AFTER DELETE ON %@ FOR EACH ROW BEGIN DELETE FROM %@ WHERE rowid = OLD.Z_PK; END"
+ "CREATE TRIGGER IF NOT EXISTS %@_UPDATE AFTER UPDATE ON %@ FOR EACH ROW BEGIN DELETE FROM %@ WHERE rowid = OLD.Z_PK; INSERT INTO %@ (rowid, %@) VALUES (NEW.Z_PK, %@); END"
+ "CREATE VIRTUAL TABLE IF NOT EXISTS %@ USING fts5(%@, content='', contentless_delete=1, tokenize = '_CoreDataTokenizer')"
+ "CoreData: error: CDCS pre-reindex wipe reported error; continuing to reindex anyway (index %@): %@\n"
+ "CoreData: error: Timed out waiting for pre-reindex domain wipe to complete (index %@)\n"
+ "CoreData: error: disconnectAllConnections reconnect failed with exception: %@\n"
+ "INSERT INTO %@ (rowid, %@) SELECT Z_PK, %@ FROM %@"
+ "Timed out waiting for CoreSpotlight domain wipe"
+ "Timed out waiting for pre-reindex domain wipe to complete (index %@)"
+ "com.apple.coredata.tokenizer.default.v2"
+ "disconnectAllConnections reconnect failed with exception: %@"
- "%@OLD.%@"
- "CDCS pre-reindex wipe reported error; continuing to reindex anyway (index %@)"
- "CREATE TRIGGER IF NOT EXISTS %@_DELETE AFTER DELETE ON %@ FOR EACH ROW BEGIN INSERT INTO %@(%@, rowid, %@) VALUES('delete', OLD.Z_PK, %@); END"
- "CREATE TRIGGER IF NOT EXISTS %@_UPDATE AFTER UPDATE ON %@ FOR EACH ROW BEGIN INSERT INTO %@(%@, rowid, %@) VALUES('delete', OLD.Z_PK, %@); INSERT INTO %@ (rowid, %@) VALUES (NEW.Z_PK, %@); END"
- "CREATE VIRTUAL TABLE IF NOT EXISTS %@ USING fts5(%@, content='%@', content_rowid='Z_PK', tokenize = '_CoreDataTokenizer')"
- "CoreData: error: CDCS pre-reindex wipe reported error; continuing to reindex anyway (index %@)\n"
- "CoreData: error: Error while resetting the client spotlight index before re-index, %@.\n"
- "CoreData: warning: CDCS pre-reindex wipe reported error; continuing to reindex anyway (index %@)\n"
- "Error while resetting the client spotlight index before re-index, %@."
- "INSERT INTO %@(%@) VALUES('rebuild')"
- "com.apple.coredata.tokenizer.default.v1"
```
