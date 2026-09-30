## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Versions/A/Spotlight`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0x5465c
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x3b8c
+2333.41.1.3.0
+  __TEXT.__text: 0x55510
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x3bb4
   __TEXT.__const: 0x578
-  __TEXT.__cstring: 0x4e3d
-  __TEXT.__gcc_except_tab: 0x21f0
+  __TEXT.__cstring: 0x4eec
+  __TEXT.__gcc_except_tab: 0x2224
   __TEXT.__oslogstring: 0xc90
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x10b0
+  __TEXT.__unwind_info: 0x10e0
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x58b
-  __TEXT.__objc_methname: 0xbca4
-  __TEXT.__objc_methtype: 0x1371
-  __TEXT.__objc_stubs: 0xa380
-  __DATA_CONST.__got: 0xaf0
+  __TEXT.__objc_classname: 0x58c
+  __TEXT.__objc_methname: 0xbde8
+  __TEXT.__objc_methtype: 0x1445
+  __TEXT.__objc_stubs: 0xa480
+  __DATA_CONST.__got: 0xb10
   __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3298
+  __DATA_CONST.__objc_selrefs: 0x32d8
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x8b0
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__auth_got: 0x820
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x15e8
-  __AUTH_CONST.__cfstring: 0x5a80
-  __AUTH_CONST.__objc_const: 0x59d0
+  __AUTH_CONST.__const: 0x1628
+  __AUTH_CONST.__cfstring: 0x5be0
+  __AUTH_CONST.__objc_const: 0x5a20
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x484
-  __DATA.__data: 0x6d0
-  __DATA.__bss: 0x474
+  __DATA.__objc_ivar: 0x48c
+  __DATA.__data: 0x6a8
+  __DATA.__bss: 0x4a4
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x108
   __DATA_DIRTY.__bss: 0x1d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1541
-  Symbols:   4646
-  CStrings:  3254
+  Functions: 1562
+  Symbols:   4684
+  CStrings:  3277
 
Symbols:
+ +[SPCoreSpotlightResult attrHasPhotosAlbumMemoryResult:isSearchToolClient:]
+ +[SPCoreSpotlightResult descriptionFromEntityType:displayName:]
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:]
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:].cold.1
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolClient:]
+ -[SPCoreSpotlightResult isSearchToolClient]
+ -[SPCoreSpotlightResult setIsSearchToolClient:]
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table6
+ GCC_except_table92
+ GCC_except_table97
+ OBJC_IVAR_$_SPCoreSpotlightQuery._retrievedIds
+ OBJC_IVAR_$_SPCoreSpotlightResult._isSearchToolClient
+ SPRedactStringClient.cold.1
+ SPRedactStringClient.isSearchToolDebugMode
+ SPRedactStringClient.onceToken
+ _LLMQUIntentDocument
+ _MDItemAppEntityType
+ _MDItemAppEntityTypeDisplayRepresentationName
+ _OBJC_CLASS_$_SFFormattedText
+ _SPRedactString
+ _SPRedactStringClient
+ _Z23isSearchToolDebugModeOnv.cold.1
+ _Z25canLogIdentifierForBundleP8NSString.cold.1
+ _Z25canLogIdentifierForBundleP8NSString.cold.2
+ __120-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:]_block_invoke.cold.1
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.420
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.431
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.436
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.439
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke_2.425
+ __35-[SPCoreSpotlightResult markAsUsed]_block_invoke.197
+ __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEiP8NSStringb
+ __Z23isSearchToolDebugModeOnv
+ __Z25canLogIdentifierForBundleP8NSString
+ __ZNSt3__110unique_ptrINS_11__tree_nodeIU8__strongP8NSStringPvEENS_22__tree_node_destructorINS_9allocatorIS6_EEEEE5resetB8nn190102EPS6_
+ __ZNSt3__114__split_bufferINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEERNS7_IS9_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEERNS7_IS9_EEED2Ev
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_3setIU8__strongP8NSStringNS_4lessIS5_EENS1_IS5_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorINS_3setIU8__strongP8NSStringNS_4lessIS5_EENS1_IS5_EEEEEES9_EEvRT_PT0_SE_SE_
+ __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSD_SD_
+ __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JS3_EEENS_4pairINS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE
+ __ZNSt3__16vectorINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEENS7_IS9_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEENS7_IS9_EEE24__emplace_back_slow_pathIJS9_EEEPS9_DpOT_
+ __ZZ23isSearchToolDebugModeOnvE12debugEnabled
+ __ZZ23isSearchToolDebugModeOnvE9onceToken
+ ___120-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:]_block_invoke
+ ___SPRedactStringClient_block_invoke
+ ____Z23isSearchToolDebugModeOnv_block_invoke
+ __block_literal_global.199
+ __block_literal_global.243
+ __block_literal_global.256
+ __block_literal_global.4
+ __block_literal_global.427
+ __block_literal_global.80
+ _objc_msgSend$attrHasPhotosAlbumMemoryResult:isSearchToolClient:
+ _objc_msgSend$descriptionFromEntityType:displayName:
+ _objc_msgSend$inferredLlmQUIntentType
+ _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:
+ _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolClient:
+ _objc_msgSend$logItems:prefix:queryId:query:isSearchToolClient:
+ _objc_msgSend$logSections:prefix:queryId:query:isSearchToolClient:
+ _objc_msgSend$logStats:prefix:queryId:query:isSearchToolClient:
+ _objc_msgSend$sendTTRLogsWithSections:queryContext:isCommittedSearch:parsecCameLaterThanSRT:
+ _objc_msgSend$setCurrentTime:
+ _objc_msgSend$setDescriptions:
+ _objc_msgSend$setFormattedTextPieces:
+ _objc_msgSend$setGlyph:
+ _objc_msgSend$setIsTemplate:
+ _objc_msgSend$updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:
- +[SPCoreSpotlightResult attrHasPhotosAlbumMemoryResult:]
- -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]
- -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:].cold.1
- -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:]
- GCC_except_table107
- GCC_except_table109
- GCC_except_table110
- GCC_except_table13
- GCC_except_table3
- GCC_except_table91
- _SSEnableSearchToolCleanSlate
- _Z19printRetrievedItemsyRKNSt3__13setIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEEEiS2_b.cold.1
- __119-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]_block_invoke.cold.1
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.405
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.416
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.421
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.424
- __32-[SPMetadataQuery _prepareQuery]_block_invoke_2.410
- __35-[SPCoreSpotlightResult markAsUsed]_block_invoke.182
- __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEP8NSStringb
- __Z18computeHybridScoreffP8NSString
- __ZGVZ18computeHybridScoreffP8NSStringE19isCleanSlateEnabled
- __ZZ18computeHybridScoreffP8NSStringE19isCleanSlateEnabled
- __ZZ25canLogIdentifierForBundleP8NSStringE12debugEnabled
- ___119-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]_block_invoke
- ___cxa_guard_abort
- __block_literal_global.184
- __block_literal_global.228
- __block_literal_global.241
- __block_literal_global.412
- _objc_msgSend$attrHasPhotosAlbumMemoryResult:
- _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:
- _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:
- _objc_msgSend$logItems:prefix:queryId:query:
- _objc_msgSend$logStats:prefix:queryId:query:
- _objc_msgSend$sendTTRLogsWithSections:searchString:queryKind:isCommittedSearch:parsecCameLaterThanSRT:
- _objc_msgSend$updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:
CStrings:
+ "\x01\x12\x11\xc5\x12"
+ " %@"
+ "%@...%@<%lu chars>"
+ "%@...<%lu chars>"
+ "(kMDItemDisableSearchInSpotlight!=1 || _kMDItemBundleID=%@)"
+ "2\x13"
+ "B28@0:8@16B24"
+ "TB,N,V_isSearchToolClient"
+ "_isSearchToolClient"
+ "_retrievedIds"
+ "attrHasPhotosAlbumMemoryResult:isSearchToolClient:"
+ "descriptionFromEntityType:displayName:"
+ "ignoreFutureDates"
+ "ignorePastDates"
+ "inferredLlmQUIntentType"
+ "initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolClient:"
+ "initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolClient:"
+ "logItems:prefix:queryId:query:isSearchToolClient:"
+ "logSections:prefix:queryId:query:isSearchToolClient:"
+ "logStats:prefix:queryId:query:isSearchToolClient:"
+ "memories"
+ "photo"
+ "rectangle.stack.fill"
+ "resolveDatesInFuture"
+ "resolveDatesInPast"
+ "sendTTRLogsWithSections:queryContext:isCommittedSearch:parsecCameLaterThanSRT:"
+ "setCurrentTime:"
+ "setDescriptions:"
+ "setFormattedTextPieces:"
+ "setGlyph:"
+ "setIsTemplate:"
+ "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:"
+ "{vector<std::set<NSString *>, std::allocator<std::set<NSString *>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::set<NSString *> *, std::allocator<std::set<NSString *>>>=\"__value_\"^v}}"
- "\x01\x12\x11\x95\x12"
- "5"
- "SearchToolCleanSlateDenseRetrieval"
- "attrHasPhotosAlbumMemoryResult:"
- "initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:"
- "initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:"
- "logItems:prefix:queryId:query:"
- "logStats:prefix:queryId:query:"
- "sendTTRLogsWithSections:searchString:queryKind:isCommittedSearch:parsecCameLaterThanSRT:"
- "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:"

```
