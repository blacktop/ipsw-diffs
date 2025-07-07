## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2381.0.1.0.0
-  __TEXT.__text: 0xae06c
+2385.1.0.1.0
+  __TEXT.__text: 0xae4f8
   __TEXT.__auth_stubs: 0x1eb0
-  __TEXT.__objc_methlist: 0x440c
+  __TEXT.__objc_methlist: 0x4424
   __TEXT.__const: 0x398
-  __TEXT.__cstring: 0x8211
-  __TEXT.__oslogstring: 0xaa6e
-  __TEXT.__gcc_except_tab: 0x4248
+  __TEXT.__cstring: 0x81b8
+  __TEXT.__oslogstring: 0xaafa
+  __TEXT.__gcc_except_tab: 0x4274
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2248
+  __TEXT.__unwind_info: 0x2280
   __TEXT.__objc_classname: 0x4d0
-  __TEXT.__objc_methname: 0xeb26
-  __TEXT.__objc_methtype: 0x24ef
+  __TEXT.__objc_methname: 0xec1a
+  __TEXT.__objc_methtype: 0x25b6
   __TEXT.__objc_stubs: 0xba00
   __DATA_CONST.__got: 0xac0
   __DATA_CONST.__const: 0x3c30

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35b8
+  __DATA_CONST.__objc_selrefs: 0x35c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x338
   __AUTH_CONST.__auth_got: 0xf70
-  __AUTH_CONST.__const: 0x1048
-  __AUTH_CONST.__cfstring: 0x7340
-  __AUTH_CONST.__objc_const: 0x5a90
+  __AUTH_CONST.__const: 0x1068
+  __AUTH_CONST.__cfstring: 0x7300
+  __AUTH_CONST.__objc_const: 0x5ae0
   __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __DATA.__objc_ivar: 0x46c
   __DATA.__data: 0x868
-  __DATA.__bss: 0x121
+  __DATA.__bss: 0x131
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x2e8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: ACF7CD71-0439-3DA1-B910-0FDCE4372A06
-  Functions: 2826
-  Symbols:   9626
-  CStrings:  5831
+  UUID: 218DEB4C-FC15-3003-8F26-D8DE93682D12
+  Functions: 2829
+  Symbols:   9634
+  CStrings:  5843
 
Symbols:
+ -[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:]
+ -[MDSearchableIndexService deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:deleteAllReason:completionHandler:]
+ -[MDSearchableIndexService deleteAllSearchableItemsWithProtectionClass:forBundleID:options:deleteAllReason:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]
+ -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:]
+ -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:deleteAllReason:completionHandler:]
+ -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithProtectionClass:forBundleID:options:deleteAllReason:completionHandler:]
+ ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1517
+ ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1557
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1486
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1494
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1500
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1506
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.1509
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke.cold.2
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1501
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1507
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1510
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2.1510.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1502
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1502.cold.1
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3.1508
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_4
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_5
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_6
+ ___124-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:]_block_invoke_7
+ ___133-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:]_block_invoke
+ ___133-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:]_block_invoke_2
+ ___133-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:]_block_invoke_3
+ ___133-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:]_block_invoke
+ ___133-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:]_block_invoke_2
+ ___133-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:]_block_invoke_3
+ ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1640
+ ___54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.212
+ ___block_descriptor_89_e8_32s40s48bs56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ ___block_literal_global.1512
+ ___block_literal_global.1567
+ ___block_literal_global.1577
+ ___block_literal_global.2075
+ ___block_literal_global.2080
+ ___block_literal_global.2086
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.260
+ ___block_literal_global.264
+ ___block_literal_global.31
+ ___block_literal_global.3672
+ ___block_literal_global.3742
+ ___block_literal_global.3791
+ ___block_literal_global.3799
+ ___block_literal_global.3801
+ ___block_literal_global.3845
+ ___block_literal_global.40
+ ___block_literal_global.44
+ ___logForCSLogCategoryDeleteAll_block_invoke
+ ___processItemsForImportInner_block_invoke.3759
+ _logForCSLogCategoryDeleteAll
+ _logForCSLogCategoryDeleteAll.cold.1
+ _logForCSLogCategoryDeleteAll.onceToken
+ _logForCSLogCategoryDeleteAll.sDeleteAllLog
+ _objc_msgSend$_deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:
+ _objc_msgSend$deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:
+ _objc_msgSend$deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:
+ _objc_msgSend$deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:deleteAllReason:completionHandler:
+ _objc_msgSend$deleteAllSearchableItemsWithProtectionClass:forBundleID:options:deleteAllReason:completionHandler:
- -[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:]
- -[MDSearchableIndexService deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:completionHandler:]
- -[MDSearchableIndexService deleteAllSearchableItemsWithProtectionClass:forBundleID:options:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]
- -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:]
- -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:completionHandler:]
- -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithProtectionClass:forBundleID:options:completionHandler:]
- ___101-[SPConcreteCoreSpotlightIndexer _deleteSearchableItemsMatchingQuery:forBundleIds:completionHandler:]_block_invoke.1516
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1485
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1493
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1499
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1505
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.1508
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.cold.1
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke.cold.2
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1500
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1506
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1509
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_2.1509.cold.1
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1501
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1501.cold.1
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_3.1507
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_4
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_5
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_6
- ___108-[SPConcreteCoreSpotlightIndexer deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:]_block_invoke_7
- ___108-[SPConcreteCoreSpotlightIndexer fetchLastClientStateForBundleID:clientStateName:options:completionHandler:]_block_invoke.1556
- ___117-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:]_block_invoke
- ___117-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:]_block_invoke_2
- ___117-[MDSearchableIndexService _deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:]_block_invoke_3
- ___117-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:]_block_invoke
- ___117-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:]_block_invoke_2
- ___117-[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:]_block_invoke_3
- ___52-[SPConcreteCoreSpotlightIndexer setHasPhotosOrText]_block_invoke.1639
- ___54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.211
- ___block_descriptor_81_e8_32s40s48bs56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_literal_global.1511
- ___block_literal_global.1566
- ___block_literal_global.1576
- ___block_literal_global.2074
- ___block_literal_global.2079
- ___block_literal_global.2085
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.266
- ___block_literal_global.270
- ___block_literal_global.3665
- ___block_literal_global.37
- ___block_literal_global.3735
- ___block_literal_global.3784
- ___block_literal_global.3792
- ___block_literal_global.3794
- ___block_literal_global.3831
- ___block_literal_global.41
- ___processItemsForImportInner_block_invoke.3752
- _objc_msgSend$_deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:
- _objc_msgSend$deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:
- _objc_msgSend$deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:
- _objc_msgSend$deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:completionHandler:
- _objc_msgSend$deleteAllSearchableItemsWithProtectionClass:forBundleID:options:completionHandler:
CStrings:
+ "(_kMDItemBundleID=\"com.apple.Preferences\" && FieldMatch(kMDItemRelatedAppBundleIdentifier"
+ "2385.1.0.1"
+ "DeleteAll"
+ "_deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:deleteAllReason:completionHandler:"
+ "bid:%s, client:%s, pc:%s, reason:%ld"
+ "dar"
+ "deleteAll"
+ "deleteAllSearchableItemsForBundleID:fromClient:shouldGC:deleteAllReason:completionHandler:"
+ "deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:deleteAllReason:completionHandler:"
+ "deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:deleteAllReason:completionHandler:"
+ "deleteAllSearchableItemsWithProtectionClass:forBundleID:options:deleteAllReason:completionHandler:"
+ "err: device locked"
+ "err: read only"
+ "pc:%s, index wipe: %s"
+ "searchutil full wipe"
+ "trial full wipe"
+ "v52@0:8@\"NSString\"16@\"NSString\"24B32q36@?<v@?@\"NSError\">44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24q32q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24q32q40@?48"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40q44@?<v@?@\"NSError\">52"
+ "v60@0:8@16@24@32B40q44@?52"
+ "v60@0:8@16@24B32q36q44@?52"
- "(_kMDItemBundleID=\"com.apple.Preferences\" && (FieldMatch(kMDItemTheme, "
- "(_kMDItemBundleID=\"com.apple.Preferences\" && FieldMatch(kMDItemTheme, "
- ") || FieldMatch(kMDItemRelatedAppBundleIdentifier, "
- "2381.0.1"
- "_deleteAllSearchableItemsWithBundleID:protectionClass:shouldGC:options:completionHandler:"
- "deleteAllSearchableItemsForBundleID:fromClient:shouldGC:completionHandler:"
- "deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:"
- "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSError\">44"

```
