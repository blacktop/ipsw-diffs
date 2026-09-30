## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2393.100.0.0.0
-  __TEXT.__text: 0xaf82c
-  __TEXT.__auth_stubs: 0x1ed0
-  __TEXT.__objc_methlist: 0x444c
+2400.8.1.0.0
+  __TEXT.__text: 0xb0148
+  __TEXT.__auth_stubs: 0x1f00
+  __TEXT.__objc_methlist: 0x4454
   __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x82cd
-  __TEXT.__oslogstring: 0xab33
-  __TEXT.__gcc_except_tab: 0x42d8
+  __TEXT.__cstring: 0x85a3
+  __TEXT.__oslogstring: 0xab32
+  __TEXT.__gcc_except_tab: 0x42e0
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__unwind_info: 0x22b0
   __TEXT.__objc_classname: 0x4dd
-  __TEXT.__objc_methname: 0xec54
-  __TEXT.__objc_methtype: 0x25d3
-  __TEXT.__objc_stubs: 0xba20
+  __TEXT.__objc_methname: 0xeca8
+  __TEXT.__objc_methtype: 0x25e3
+  __TEXT.__objc_stubs: 0xba80
   __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__const: 0x3c80
+  __DATA_CONST.__const: 0x3cf8
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35d0
+  __DATA_CONST.__objc_selrefs: 0x35e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x338
-  __AUTH_CONST.__auth_got: 0xf80
+  __DATA_CONST.__objc_arraydata: 0x350
+  __AUTH_CONST.__auth_got: 0xf98
   __AUTH_CONST.__const: 0x10a8
-  __AUTH_CONST.__cfstring: 0x7480
+  __AUTH_CONST.__cfstring: 0x76c0
   __AUTH_CONST.__objc_const: 0x5b98
   __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_intobj: 0x240

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: DB4DC0F9-9B8A-3ED8-9AB5-2D933E8B21CF
-  Functions: 2852
-  Symbols:   9707
-  CStrings:  5873
+  UUID: 2CFED1C9-DEFF-3636-A4C0-15113561819F
+  Functions: 2861
+  Symbols:   9734
+  CStrings:  5915
 
Symbols:
+ -[MDSearchableIndexService _issueDiagnose:bundleID:logQuery:completionHandler:]
+ -[MDSearchableIndexService _issueDiagnose:bundleID:logQuery:completionHandler:].cold.1
+ -[SPCoreSpotlightIndexer _issueDiagnose:bundleID:logQuery:completionHandler:]
+ -[SPCoreSpotlightIndexer _issueDiagnose:bundleID:logQuery:completionHandler:].cold.1
+ -[SPCoreSpotlightIndexer leakDebugDump:]
+ GCC_except_table1266
+ GCC_except_table1267
+ GCC_except_table1335
+ GCC_except_table1338
+ GCC_except_table1340
+ GCC_except_table1341
+ GCC_except_table1508
+ GCC_except_table1537
+ __SIDumpIndexSetRefs
+ __SIDumpJobRefs
+ __SIDumpQueryInfo
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3171
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_2
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_3
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_4
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_5
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_6
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_7
+ ___40-[SPCoreSpotlightIndexer leakDebugDump:]_block_invoke_8
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3182
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3183
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3170
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3121
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3123
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3123.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3124
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3125
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3125.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3126
+ ___96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.76
+ ___block_descriptor_40_e8_32s_e11_v24?0Q8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e26_v32?0Q8Q16^{__SIQuery=}24ls32l8
+ ___block_descriptor_48_e8_32s_e22_v40?0^i8B16i20^*24d32ls32l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_99_e8_32s40s48s56s64s72s80w_e18_v20?0^{__SI=}8C16lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.3129
+ ___block_literal_global.3181
+ ___block_literal_global.3194
+ ___block_literal_global.3770
+ ___block_literal_global.3889
+ ___block_literal_global.3897
+ ___block_literal_global.3899
+ ___block_literal_global.3936
+ ___block_literal_global.3943
+ ___processItemsForImportInner_block_invoke.3857
+ _objc_msgSend$_issueDiagnose:bundleID:logQuery:completionHandler:
+ _objc_msgSend$jobOptionsFromProvideOptions:
+ _objc_msgSend$leakDebugDump:
+ _objc_msgSend$provideOptionsFromJobOptions:
- -[MDSearchableIndexService _issueDiagnose:logQuery:completionHandler:]
- -[MDSearchableIndexService _issueDiagnose:logQuery:completionHandler:].cold.1
- -[SPCoreSpotlightIndexer _issueDiagnose:logQuery:completionHandler:]
- -[SPCoreSpotlightIndexer _issueDiagnose:logQuery:completionHandler:].cold.1
- GCC_except_table1257
- GCC_except_table1258
- GCC_except_table1326
- GCC_except_table1329
- GCC_except_table1331
- GCC_except_table1332
- GCC_except_table1499
- GCC_except_table1528
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.3165
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.3176
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.3177
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.3164
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3113
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3113.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3115
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3117
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3117.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3118
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.3120
- ___96-[SpotlightDaemonServer handleJob:protectionClass:perClientCompletionHandler:completionHandler:]_block_invoke.75
- ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_99_e8_32s40s48s56s64s72s80s88w_e18_v20?0^{__SI=}8C16lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.24
- ___block_literal_global.3123
- ___block_literal_global.3175
- ___block_literal_global.3188
- ___block_literal_global.3721
- ___block_literal_global.3791
- ___block_literal_global.3848
- ___block_literal_global.3850
- ___block_literal_global.3887
- ___block_literal_global.3894
- ___processItemsForImportInner_block_invoke.3808
- _objc_msgSend$_issueDiagnose:logQuery:completionHandler:
CStrings:
+ "\n\t\t>>> %s"
+ "\n\t>> [%d] %@ stack trace (%lfs ago):"
+ "\n> [%llu] Begin stack traces for active job ref 0x%llx: %@"
+ "\n> [%llu] Begin stack traces for index set 0x%llx"
+ "\n> [%llu] End stack traces for active job ref 0x%llx: %@\n"
+ "\n> [%llu] End stack traces for index set 0x %llx"
+ "\nTotal %llu index sets allocated, %llu index sets deallocated, %llu index sets remaining\n"
+ "\nTotal %llu job refs allocated, %llu job refs deallocated, %llu jobs remaining\n"
+ "2400.8.1"
+ "Error updating items for checked in client (%@): %@"
+ "Release"
+ "Retain"
+ "Supported: sijob, ciindexset, sdtransaction"
+ "_issueDiagnose:bundleID:logQuery:completionHandler:"
+ "ciindexset"
+ "com.apple.Search.framework.SpotlightDiagnostic"
+ "com.apple.diagnosticextensions.osx.spotlight.user.helper"
+ "com.apple.spotlight.mddiagnose"
+ "jobOptionsFromProvideOptions:"
+ "leakDebugDump:"
+ "leaks"
+ "provideOptionsFromJobOptions:"
+ "sdtransaction"
+ "sijob"
+ "v24@?0Q8Q16"
+ "v32@?0Q8Q16^{__SIQuery=}24"
+ "v40@0:8i16@\"NSString\"20B28@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8i16@20B28@?32"
+ "v40@?0^i8B16i20^*24d32"
- "2393.100"
- "Error udpdating items for checked in client (%@): %@"
- "_issueDiagnose:logQuery:completionHandler:"
- "v32@0:8i16B20@?24"
- "v32@0:8i16B20@?<v@?@\"NSData\"@\"NSError\">24"

```
