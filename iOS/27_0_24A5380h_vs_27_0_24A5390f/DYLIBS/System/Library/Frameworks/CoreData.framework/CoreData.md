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

-1624.0.0.0.0
-  __TEXT.__text: 0x32fd90
-  __TEXT.__objc_methlist: 0x108a0
+1627.0.0.0.0
+  __TEXT.__text: 0x331154
+  __TEXT.__objc_methlist: 0x108d8
   __TEXT.__const: 0x2e30
   __TEXT.__constg_swiftt: 0x9d8
   __TEXT.__swift5_typeref: 0x12d0

   __TEXT.__swift5_types: 0xd4
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift5_capture: 0x340
-  __TEXT.__cstring: 0x3bceb
+  __TEXT.__cstring: 0x3bf28
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x187a0
-  __TEXT.__oslogstring: 0x36758
-  __TEXT.__unwind_info: 0x77a0
+  __TEXT.__gcc_except_tab: 0x187c8
+  __TEXT.__oslogstring: 0x36910
+  __TEXT.__unwind_info: 0x77d8
   __TEXT.__eh_frame: 0x9d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4bc8
+  __DATA_CONST.__const: 0x4be8
   __DATA_CONST.__objc_classlist: 0xed8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6218
+  __DATA_CONST.__objc_selrefs: 0x6240
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xbb8
   __DATA_CONST.__objc_arraydata: 0x8860
   __DATA_CONST.__got: 0xca0
-  __AUTH_CONST.__const: 0x2db8
-  __AUTH_CONST.__cfstring: 0x1fce0
-  __AUTH_CONST.__objc_const: 0x25d78
+  __AUTH_CONST.__const: 0x2dd8
+  __AUTH_CONST.__cfstring: 0x1fdc0
+  __AUTH_CONST.__objc_const: 0x25dc8
   __AUTH_CONST.__objc_dictobj: 0x2698
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x8f88

   __AUTH_CONST.__auth_got: 0x17e0
   __AUTH.__objc_data: 0x32d8
   __AUTH.__data: 0x238
-  __DATA.__objc_ivar: 0x1890
+  __DATA.__objc_ivar: 0x1898
   __DATA.__data: 0x1660
   __DATA.__bss: 0x16d0
   __DATA.__common: 0x650
   __DATA_DIRTY.__objc_ivar: 0x514
   __DATA_DIRTY.__objc_data: 0x63c8
   __DATA_DIRTY.__data: 0x5a0
-  __DATA_DIRTY.__bss: 0x698
+  __DATA_DIRTY.__bss: 0x6c0
   __DATA_DIRTY.__common: 0x178
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9325
-  Symbols:   20112
-  CStrings:  8316
+  Functions: 9338
+  Symbols:   20132
+  CStrings:  8339
 
Symbols:
+ +[NSManagedObject(_PFDynamicAccessorsAndPropertySupport) allocBatch:withEntity:andContext:count:]
+ +[NSManagedObject(_PFDynamicAccessorsAndPropertySupport) allocWithEntity:context:]
+ +[NSManagedObjectModel _invalidateStaticCaches]
+ +[NSManagedObjectModel initialize]
+ +[_PFRoutines stringByStrippingLeadingByteOrderMark:]
+ -[NSCoreDataCoreSpotlightDelegate _asyncContextBlock:completion:]
+ -[NSCoreDataCoreSpotlightDelegate _deletionErrorToReturn]
+ -[NSCoreDataFullTextNaturalLanguageTokenizerProvider tokenizerIdentifier]
+ -[NSEntityDescription _createCachesForNoClassesVariant]
+ -[NSEntityDescription _entityClassForContext:]
+ -[NSManagedObjectContext _setXPCServerContext:]
+ -[NSManagedObjectModel _createCachesForNoClassesVariant]
+ -[NSManagedObjectModel(CoreDataSPI) initWithContentsOfURL:allowCaching:]
+ GCC_except_table111
+ GCC_except_table124
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table143
+ GCC_except_table154
+ GCC_except_table243
+ GCC_except_table247
+ GCC_except_table260
+ GCC_except_table268
+ GCC_except_table290
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table303
+ GCC_except_table312
+ GCC_except_table317
+ GCC_except_table43
+ GCC_except_table66
+ _OBJC_IVAR_$_NSEntityDescription._propertyAccessors
+ _OBJC_IVAR_$_NSSQLEntity_DerivedAttributesExtension._triggerSQLLock
+ _OBJC_IVAR_$__NSSQLiteStoreMigrator._historyModel
+ ___30-[NSEntityDescription dealloc]_block_invoke
+ ___65-[NSCoreDataCoreSpotlightDelegate _asyncContextBlock:completion:]_block_invoke
+ ___77-[NSCoreDataCoreSpotlightDelegate deleteSpotlightIndexWithCompletionHandler:]_block_invoke_2
+ ____PFBackgroundRuntimeProviderCacheUIApplicationInstance_block_invoke
+ ___block_descriptor_40_e9_v16?0^8l
+ ___block_descriptor_64_e8_32o40b48b56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___pf_isProcess_partlycloudd
+ ___pf_isProcess_partlycloudd_debug
+ ___pf_isProcess_voicebankingd
+ __kvcPropertysPublicValidationMethods
+ _objc_msgSend$acquisitionError
+ _objc_msgSend$allocBatch:withEntity:andContext:count:
+ _objc_msgSend$allocWithEntity:context:
+ _objc_msgSend$predicateWithFormat:argumentArray:
+ _objc_msgSend$tokenizerIdentifier
- +[NSManagedObject(_PFDynamicAccessorsAndPropertySupport) allocBatch:withEntity:count:]
- +[NSManagedObject(_PFDynamicAccessorsAndPropertySupport) allocWithEntity:]
- -[NSCoreDataCoreSpotlightDelegate _asyncContextBlock:]
- -[NSEntityDescription _entityClass]
- -[NSPersistentStoreCoordinator _repairFullTextIndiciesForStoreWithIdentifier:synchronous:]
- GCC_except_table114
- GCC_except_table138
- GCC_except_table146
- GCC_except_table152
- GCC_except_table177
- GCC_except_table196
- GCC_except_table241
- GCC_except_table246
- GCC_except_table259
- GCC_except_table267
- GCC_except_table288
- GCC_except_table295
- GCC_except_table299
- GCC_except_table301
- GCC_except_table311
- GCC_except_table316
- GCC_except_table42
- GCC_except_table80
- _OBJC_IVAR_$_NSEntityDescription._kvcPropertyAccessors
- ___54-[NSCoreDataCoreSpotlightDelegate _asyncContextBlock:]_block_invoke
- ___block_descriptor_56_e8_32o40b48w_e5_v8?0lw48l8s32l8s40l8
- _objc_msgSend$allocBatch:withEntity:count:
- _objc_msgSend$allocWithEntity:
- _objc_msgSend$performSelector:
CStrings:
+ "%%"
+ "%K"
+ "CDCS OS-driven index deletion abandoned; delivering completion for index %@"
+ "CDCS OS-driven reindex (%lu identifiers) acknowledged without reindexing (reindex abandoned) for index %@"
+ "CDCS OS-driven reindex (all items) acknowledged without reindexing (reindex abandoned) for index %@"
+ "CoreData: error: CDCS OS-driven index deletion abandoned; delivering completion for index %@\n"
+ "CoreData: error: CDCS OS-driven reindex (%lu identifiers) acknowledged without reindexing (reindex abandoned) for index %@\n"
+ "CoreData: error: CDCS OS-driven reindex (all items) acknowledged without reindexing (reindex abandoned) for index %@\n"
+ "CoreData: error: Finished rebuilding full-text indicies for store - %@ (tokenizer=%@)\n"
+ "CoreData: error: Rebuilding full-text indexes for store - %@ (storedTokenizer=%@, currentTokenizer=%@)\n"
+ "CoreData: error: sqlite3_db_config for SQLITE_DBCONFIG_FP_DIGITS failed: %d\n"
+ "CoreData: warning: CDCS OS-driven index deletion abandoned; delivering completion for index %@\n"
+ "CoreData: warning: CDCS OS-driven reindex (%lu identifiers) acknowledged without reindexing (reindex abandoned) for index %@\n"
+ "CoreData: warning: CDCS OS-driven reindex (all items) acknowledged without reindexing (reindex abandoned) for index %@\n"
+ "CoreData: warning: Finished rebuilding full-text indicies for store - %@ (tokenizer=%@)\n"
+ "CoreData: warning: Rebuilding full-text indexes for store - %@ (storedTokenizer=%@, currentTokenizer=%@)\n"
+ "Finished rebuilding full-text indicies for store - %@ (tokenizer=%@)"
+ "NSPersistentStoreFullTextTokenizerIdentifier"
+ "Predicate string '%@' contains unresolved format specifiers"
+ "Rebuilding full-text indexes for store - %@ (storedTokenizer=%@, currentTokenizer=%@)"
+ "_PFManagedObject_coerceValueForKeyWithDescription"
+ "_allocWithEntity"
+ "_batchRetainedObjects:"
+ "_implicitObservationInfoForEntity:"
+ "_retainedObjectWithID:"
+ "allocBatch:"
+ "com.apple.coredata.tokenizer.default.v1"
+ "initWithEntity:"
+ "partlycloudd"
+ "partlycloudd_debug"
+ "sqlite3_db_config for SQLITE_DBCONFIG_FP_DIGITS failed: %d"
+ "v16@?0^@8"
+ "voicebankingd"
- "CoreData: annotation: Deferring full-text index repair until after migration is complete (NSPersistentStoreCoordinatorIsMigratingStoreWithStagedMigrationOptionKey is set).\n"
- "CoreData: error: Deferring full-text index repair until after migration is complete (NSPersistentStoreCoordinatorIsMigratingStoreWithStagedMigrationOptionKey is set).\n"
- "CoreData: error: Finished rebuilding full-text indicies for store - %@\n"
- "CoreData: error: Rebuilding full-text indexes for store created by older framework version (fvk=%@) - %@\n"
- "CoreData: warning: Finished rebuilding full-text indicies for store - %@\n"
- "CoreData: warning: Rebuilding full-text indexes for store created by older framework version (fvk=%@) - %@\n"
- "Deferring full-text index repair until after migration is complete (NSPersistentStoreCoordinatorIsMigratingStoreWithStagedMigrationOptionKey is set)."
- "Finished rebuilding full-text indicies for store - %@"
- "NSApplication"
- "Rebuilding full-text indexes for store created by older framework version (fvk=%@) - %@"
```
