## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x39c9fc
+5691.0.0.0.0
+  __TEXT.__text: 0x39df74
   __TEXT.__auth_stubs: 0x3540
-  __TEXT.__objc_methlist: 0x3305c
-  __TEXT.__const: 0x7a48
+  __TEXT.__objc_methlist: 0x3310c
+  __TEXT.__const: 0x8068
   __TEXT.__swift5_typeref: 0x2b1a
   __TEXT.__constg_swiftt: 0x1f1c
   __TEXT.__swift5_reflstr: 0x1450
   __TEXT.__swift5_fieldmd: 0x1a2c
   __TEXT.__swift5_proto: 0x554
   __TEXT.__swift5_types: 0x268
-  __TEXT.__cstring: 0x4f96d
+  __TEXT.__cstring: 0x4f8b4
   __TEXT.__swift5_capture: 0x8ac
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_assocty: 0x310
   __TEXT.__swift_as_entry: 0x22c
   __TEXT.__swift_as_ret: 0x2ac
-  __TEXT.__oslogstring: 0x15668
+  __TEXT.__oslogstring: 0x1584d
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x53c8
+  __TEXT.__gcc_except_tab: 0x5408
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x27a
-  __TEXT.__unwind_info: 0xd038
+  __TEXT.__unwind_info: 0xd048
   __TEXT.__eh_frame: 0x7468
-  __TEXT.__objc_classname: 0x74d9
-  __TEXT.__objc_methname: 0x83de4
-  __TEXT.__objc_methtype: 0xc786
-  __TEXT.__objc_stubs: 0x34920
+  __TEXT.__objc_classname: 0x74db
+  __TEXT.__objc_methname: 0x83f94
+  __TEXT.__objc_methtype: 0xc74e
+  __TEXT.__objc_stubs: 0x349a0
   __DATA_CONST.__got: 0x2a68
-  __DATA_CONST.__const: 0x116c8
+  __DATA_CONST.__const: 0x116a8
   __DATA_CONST.__objc_classlist: 0x1bd8
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x880
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x141f0
+  __DATA_CONST.__objc_selrefs: 0x14230
   __DATA_CONST.__objc_protorefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x1558
   __DATA_CONST.__objc_arraydata: 0x1d38
   __AUTH_CONST.__auth_got: 0x1ab8
   __AUTH_CONST.__const: 0x90d8
-  __AUTH_CONST.__cfstring: 0x30400
-  __AUTH_CONST.__objc_const: 0x745d8
+  __AUTH_CONST.__cfstring: 0x30460
+  __AUTH_CONST.__objc_const: 0x74708
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH.__objc_data: 0xbb0
-  __AUTH.__data: 0x8f0
-  __DATA.__objc_ivar: 0x43ac
-  __DATA.__data: 0x6b60
+  __AUTH.__data: 0x8e0
+  __DATA.__objc_ivar: 0x43b0
+  __DATA.__data: 0x6580
   __DATA.__bss: 0x8798
   __DATA.__common: 0xd0
-  __DATA_DIRTY.__objc_ivar: 0xf08
+  __DATA_DIRTY.__objc_ivar: 0xf18
   __DATA_DIRTY.__objc_data: 0x10b68
   __DATA_DIRTY.__data: 0x1200
   __DATA_DIRTY.__common: 0x2b8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CF2F0EAC-4D2E-37C4-9EE3-7B93E9E4102F
-  Functions: 22417
-  Symbols:   64139
-  CStrings:  36737
+  UUID: E8AFF70A-A895-3C7F-85DE-25CE1B2702DA
+  Functions: 22431
+  Symbols:   64173
+  CStrings:  36760
 
Symbols:
+ +[FCCKRecordFieldSchema fieldWithName:type:isEncrypted:]
+ +[FCEdgeCacheHint(NewsSpecific) edgeCacheHintForWidgetArticles]
+ +[FCEdgeCacheHint(NewsSpecific) edgeCacheHintForWidgetConfig]
+ -[FCCKDatabaseEncryptionMiddleware _removeField:fromRecord:]
+ -[FCCKRecordFieldSchema sanitizeValue:]
+ -[FCCKRecordSchema schemaForField:]
+ -[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:]
+ -[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:]
+ -[FCMultiSourceHeadlinesOperation cachePolicyForArticles]
+ -[FCMultiSourceHeadlinesOperation edgeCacheHint]
+ -[FCMultiSourceHeadlinesOperation heldRecordsCompletionHandler]
+ -[FCMultiSourceHeadlinesOperation resultHeldRecordsByType]
+ -[FCMultiSourceHeadlinesOperation setCachePolicyForArticles:]
+ -[FCMultiSourceHeadlinesOperation setEdgeCacheHint:]
+ -[FCMultiSourceHeadlinesOperation setHeldRecordsCompletionHandler:]
+ -[FCMultiSourceHeadlinesOperation setResultHeldRecordsByType:]
+ -[FCNewsAppConfig adSponsorshipsEnabled]
+ -[FCNewsAppConfig isTodaySponsorshipEligible]
+ -[FCWritablePrivateDataStorage writeReadHistoryItem:]
+ -[FCWritablePrivateDataStorage writeSeenHistoryItems:]
+ -[NSFileManager(FCAdditions) fc_removeContentsOfDirectoryAtURL:removedItemCount:error:]
+ _FCWidgetShouldIgnoreJSONRecordsSharedPreferenceKey
+ _NSURLFileResourceIdentifierKey
+ _OBJC_IVAR_$_FCCKRecordFieldSchema._type
+ ___41-[NTPBAVAsset(Bookmark) resolvedCacheURL]_block_invoke.138
+ ___44-[FCAVAssetDownloadManager _isAssetInCache:]_block_invoke.32
+ ___47-[NTPBAVAsset(Bookmark) resolvedFileResourceID]_block_invoke_2
+ ___51-[FCMultiSourceHeadlinesOperation performOperation]_block_invoke.19
+ ___51-[FCMultiSourceHeadlinesOperation performOperation]_block_invoke_3
+ ___60-[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:]_block_invoke
+ ___96-[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:]_block_invoke
+ ___Block_byref_object_copy_.35
+ ___Block_byref_object_dispose_.36
+ ___block_literal_global.2203
+ ___block_literal_global.2232
+ ___block_literal_global.2621
+ ___block_literal_global.2712
+ ___block_literal_global.2793
+ ___block_literal_global.2795
+ ___block_literal_global.2797
+ ___block_literal_global.2805
+ ___block_literal_global.2816
+ ___block_literal_global.2821
+ ___block_literal_global.2826
+ ___block_literal_global.2831
+ ___block_literal_global.42
+ ___block_literal_global.532
+ _fsctl
+ _objc_msgSend$cachePolicyForArticles
+ _objc_msgSend$depositSyncWithAccessor:
+ _objc_msgSend$enqueueTransaction:withMaxTransactionCount:
+ _objc_msgSend$fc_removeContentsOfDirectoryAtURL:removedItemCount:error:
+ _objc_msgSend$heldRecordsCompletionHandler
+ _objc_msgSend$resultHeldRecordsByType
+ _objc_msgSend$setResultHeldRecordsByType:
- +[FCCKRecordFieldSchema fieldWithName:isEncrypted:]
- +[FCEdgeCacheHint(NewsSpecific) edgeCacheHintForToday]
- -[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:withCompletion:]
- -[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:completion:]
- -[FCWritablePrivateDataStorage writeReadHistoryItem:withCompletion:]
- -[FCWritablePrivateDataStorage writeSeenHistoryItems:withCompletion:]
- _CacheManagementEnumerateAssets
- _OBJC_CLASS_$_CacheManagementAsset
- ___107-[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:completion:]_block_invoke
- ___41-[NTPBAVAsset(Bookmark) resolvedCacheURL]_block_invoke.137
- ___44-[FCAVAssetDownloadManager _isAssetInCache:]_block_invoke.34
- ___51-[FCMultiSourceHeadlinesOperation performOperation]_block_invoke.25
- ___68-[FCWritablePrivateDataStorage writeReadHistoryItem:withCompletion:]_block_invoke
- ___69-[FCWritablePrivateDataStorage writeSeenHistoryItems:withCompletion:]_block_invoke
- ___75-[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:withCompletion:]_block_invoke
- ___76-[FCAVAssetDownloadManager initWithAssetCache:keyCache:networkReachability:]_block_invoke_3
- ___Block_byref_object_copy_.37
- ___Block_byref_object_dispose_.38
- ___block_descriptor_40_e8_32s_e30_B16?0"CacheManagementAsset"8ls32l8
- ___block_literal_global.2200
- ___block_literal_global.2229
- ___block_literal_global.2615
- ___block_literal_global.2706
- ___block_literal_global.2787
- ___block_literal_global.2789
- ___block_literal_global.2791
- ___block_literal_global.2799
- ___block_literal_global.2810
- ___block_literal_global.2815
- ___block_literal_global.2820
- ___block_literal_global.2825
- ___block_literal_global.529
- _objc_msgSend$assetFromPath:withIdentifier:
- _objc_msgSend$commit
- _objc_msgSend$enqueueTransaction:withMaxTransactionCount:completion:
CStrings:
+ "-[FCCKRecordFieldSchema sanitizeValue:]"
+ "-[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:]"
+ "-[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:]"
+ "-[FCWritablePrivateDataStorage writeReadHistoryItem:]"
+ "-[FCWritablePrivateDataStorage writeSeenHistoryItems:]"
+ "AV asset cache failed to look up resource ID, assetID=%{public}@, url=%{public}@, error=%{public}@"
+ "AV asset cache failed to look up resource ID, url=%{public}@, error=%{public}@"
+ "AV asset download manager failed to mark asset as purgeable, URL=%{public}@, errno=%{public}@"
+ "Client record field is missing from the schema: %{public}@.%{public}@"
+ "Server record field is missing from the schema: %{public}@.%{public}@"
+ "T@\"FCCachePolicy\",&,N,V_cachePolicyForArticles"
+ "T@\"NSArray\",C,N,V_articleIDs"
+ "T@\"NSDictionary\",&,N,V_resultHeldRecordsByType"
+ "T@?,C,N,V_heldRecordsCompletionHandler"
+ "_cachePolicyForArticles"
+ "_heldRecordsCompletionHandler"
+ "adSponsorshipsEnabled"
+ "adSponsorshipsEnabledLevel"
+ "cachePolicyForArticles"
+ "edgeCacheHintForWidgetArticles"
+ "edgeCacheHintForWidgetConfig"
+ "enqueueTransaction:withMaxTransactionCount:"
+ "failed to create directory for AV asset downloads with error: %{public}@"
+ "failed to create directory for AV asset downloads with exception: %{public}@"
+ "fc_removeContentsOfDirectoryAtURL:removedItemCount:error:"
+ "heldRecordsCompletionHandler"
+ "isTodaySponsorshipEligible"
+ "privateDataCleanupToV4Level3"
+ "privateDataMigrateToV4Level3"
+ "resultHeldRecordsByType"
+ "setCachePolicyForArticles:"
+ "setHeldRecordsCompletionHandler:"
+ "setResultHeldRecordsByType:"
+ "submitUpdate:"
+ "unexpected type %@ for field %@"
+ "unexpected type within array %@ for field %@"
+ "v24@0:8@\"<FCReadingHistoryItem>\"16"
+ "widget_ignore_json_records"
+ "widgetarticles"
+ "writeReadHistoryItem:"
+ "writeSeenHistoryItems:"
- "*** Assertion failure (Identifier: UnknownRecordField) : %s %s:%d %{public}@"
- "-[FCCKDatabaseEncryptionMiddleware _decryptRecord:withEncryptionKey:mapping:error:]"
- "-[FCFileCoordinatedTodayPersonalizationUpdate submitUpdate:withCompletion:]"
- "-[FCFileCoordinatedTodayPrivateDataTransactionQueue enqueueTransaction:withMaxTransactionCount:completion:]"
- "-[FCWritablePrivateDataStorage writeReadHistoryItem:withCompletion:]"
- "-[FCWritablePrivateDataStorage writeSeenHistoryItems:withCompletion:]"
- "B16@?0@\"CacheManagementAsset\"8"
- "Client record field is missing from the schema: %@.%@"
- "Server record field is missing from the schema: %@.%@"
- "assetFromPath:withIdentifier:"
- "commit"
- "edgeCacheHintForToday"
- "enqueueTransaction:withMaxTransactionCount:completion:"
- "multi-source headlines operation requires a cached records lookup block whenever record source persistence is bypassed"
- "privateDataCleanupToV4Level2"
- "privateDataMigrateToV4Level2"
- "submitUpdate:withCompletion:"
- "v32@0:8@\"<FCReadingHistoryItem>\"16@?<v@?>24"
- "v32@0:8@\"NSArray\"16@?<v@?>24"
- "v40@0:8@16Q24@?32"
- "writeReadHistoryItem:withCompletion:"
- "writeSeenHistoryItems:withCompletion:"

```
