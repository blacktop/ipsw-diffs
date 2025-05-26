## LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

-1835.102.2.0.0
-  __TEXT.__text: 0x938f70
+1835.120.53.0.0
+  __TEXT.__text: 0x940178
   __TEXT.__auth_stubs: 0x5090
   __TEXT.__objc_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0x19a8
+  __TEXT.__objc_methlist: 0x19d8
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__const: 0x19e8c
-  __TEXT.__cstring: 0x37ade
-  __TEXT.__objc_methname: 0xa367
-  __TEXT.__objc_classname: 0x417
-  __TEXT.__objc_methtype: 0x3110
-  __TEXT.__constg_swiftt: 0xe758
-  __TEXT.__swift5_typeref: 0xdfa3
+  __TEXT.__const: 0x1a09c
+  __TEXT.__cstring: 0x380fe
+  __TEXT.__objc_methname: 0xa56f
+  __TEXT.__objc_classname: 0x43a
+  __TEXT.__objc_methtype: 0x32b9
+  __TEXT.__constg_swiftt: 0xe75c
+  __TEXT.__swift5_typeref: 0xe0a3
   __TEXT.__swift5_builtin: 0x618
-  __TEXT.__swift5_reflstr: 0x8dfe
-  __TEXT.__swift5_fieldmd: 0x80c4
+  __TEXT.__swift5_reflstr: 0x8e7e
+  __TEXT.__swift5_fieldmd: 0x8110
   __TEXT.__swift5_assocty: 0x1ac8
   __TEXT.__swift5_proto: 0x1360
-  __TEXT.__swift5_types: 0x87c
-  __TEXT.__swift5_capture: 0x125f0
+  __TEXT.__swift5_types: 0x880
+  __TEXT.__swift5_capture: 0x12724
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__ustring: 0x30
   __TEXT.__oslogstring: 0xccc
   __TEXT.__swift5_mpenum: 0xdc
-  __TEXT.__unwind_info: 0x11b68
-  __TEXT.__eh_frame: 0x21b20
+  __TEXT.__unwind_info: 0x11dbc
+  __TEXT.__eh_frame: 0x21ca8
   __DATA_CONST.__auth_got: 0x2858
   __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__auth_ptr: 0x4c8
-  __DATA_CONST.__const: 0x40820
+  __DATA_CONST.__auth_ptr: 0x4d8
+  __DATA_CONST.__const: 0x40c20
   __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x280
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __DATA_CONST.__objc_catlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_classrefs: 0x380
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_classrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x11fd8
-  __DATA.__objc_selrefs: 0x24f8
+  __DATA.__objc_const: 0x120a8
+  __DATA.__objc_selrefs: 0x2548
   __DATA.__objc_ivar: 0x128
   __DATA.__objc_data: 0x3310
-  __DATA.__data: 0x16278
+  __DATA.__data: 0x162f8
   __DATA.__bss: 0x25da0
   __DATA.__common: 0x770
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29749
-  Symbols:   904
-  CStrings:  6274
+  Functions: 29844
+  Symbols:   907
+  CStrings:  6313
 
Symbols:
+ _OBJC_CLASS_$_NSPredicate
+ _fpfs_get_purgeable_stats
+ _statfs
CStrings:
+ "\nGROUP BY metadata_is_dataless"
+ "\nWHERE metadata_is_in_pinned_folder AND metadata_kind = "
+ "/Library/Caches/com.apple.xbs/Sources/FileProviderExtensions/fssync/libfssync/implementations/file-system/persistence/SQLSnapshot.swift"
+ "@\"NSProgress\"56@0:8@\"NSDictionary\"16{CGSize=dd}24@?<v@?@\"NSString\"@\"NSFileProviderItemVersion\"@\"NSData\"@\"NSData\"@\"NSError\">40@?<v@?@\"NSError\">48"
+ "@\"NSProgress\"56@0:8@\"NSDictionary\"16{CGSize=dd}24@?<v@?@\"NSString\"@\"NSFileProviderItemVersion\"@\"NSData\"@\"NSError\">40@?<v@?@\"NSError\">48"
+ "@\"NSProgress\"56@0:8@\"NSDictionary\"16{CGSize=dd}24@?<v@?@\"NSString\"@\"NSFileProviderItemVersion\"@\"NSURL\"@\"NSData\"@\"NSError\">40@?<v@?@\"NSError\">48"
+ "Failed to gather volume stats on %@: %@"
+ "Invalid call on FP snapshot"
+ "Invalid call on FS snapshot"
+ "Retrieved statfs() for volume %@"
+ "SELECT SUM(metadata_size),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-30 days') THEN metadata_size ELSE 0 END),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-60 days') THEN metadata_size ELSE 0 END),\n       SUM(CASE WHEN DATETIME(metadata_last_used_date, 'unixepoch') >= date('now', '-90 days') THEN metadata_size ELSE 0 END)\n  FROM "
+ "SELECT SUM(metadata_size), metadata_is_dataless\n FROM "
+ "SELECT rec.fs_id, rec.item_is_flocked, throttle.job_type, throttle.last_error\n  FROM reconciliation_table AS rec\nLEFT JOIN fs_throttle AS throttle ON throttle.item_id == rec.fs_id\nWHERE rec.fs_disk_import_status == "
+ "SQLDB: building FP telemetry report"
+ "_NSFileProviderVersionThumbnailing"
+ "available_disk_size"
+ "dynamicErrorSampleRatePerProvider"
+ "evaluateWithObject:"
+ "fetchThumbnailsForDictionary:requestedSize:perThumbnailCompletionHandler:completionHandler:"
+ "fetchThumbnailsForDictionary:requestedSize:perThumbnailCompletionHandlerDataURLWithMetadata:completionHandler:"
+ "fetchThumbnailsForDictionary:requestedSize:perThumbnailCompletionHandlerWithMetadata:completionHandler:"
+ "fp_realPathRelationshipToItemAtRealPathURL:"
+ "isProviderForRealPathURL:"
+ "itemPendingReconciliationJobCode"
+ "lastDeferralDate"
+ "optimize_storage"
+ "pinned_documents_size"
+ "pinned_resident_pct"
+ "purgeable_high_size"
+ "purgeable_low_size"
+ "purgeable_medium_size"
+ "recent_documents_size_30_days"
+ "recent_documents_size_60_days"
+ "recent_documents_size_90_days"
+ "setXpcActivityTimeSinceLastAbleToRun:"
+ "total_account_size"
+ "xpcActivityIsActive"
+ "⚔️  Fetch thumbnail for %@ finished after global handler was called"
+ "⚔️  Fetch thumbnail for %@ has an unbalanced fetch %ld"
+ "⚔️  Global fetch thumbnail is executed before %ld thumbnails fetch finished"
+ "⚔️ Global fetch thumbnail failed: %@"
- "- Iconsistent item "
- "SELECT rec.fs_id, rec.item_is_flocked, throttle.job_type\n  FROM reconciliation_table AS rec\nLEFT JOIN fs_throttle AS throttle ON throttle.item_id == rec.fs_id\nWHERE rec.fs_disk_import_status == "
- "isProviderForURL:"

```
