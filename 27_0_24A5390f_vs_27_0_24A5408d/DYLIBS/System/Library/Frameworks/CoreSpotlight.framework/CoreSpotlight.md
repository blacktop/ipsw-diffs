## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x175384
-  __TEXT.__objc_methlist: 0x14220
-  __TEXT.__const: 0xee8
-  __TEXT.__gcc_except_tab: 0x9134
-  __TEXT.__cstring: 0x2b95f
-  __TEXT.__oslogstring: 0xb7a9
-  __TEXT.__ustring: 0x2040
-  __TEXT.__dlopen_cstrs: 0x49b
+2459.102.0.0.0
+  __TEXT.__text: 0x17c894
+  __TEXT.__objc_methlist: 0x14400
+  __TEXT.__const: 0xef8
+  __TEXT.__gcc_except_tab: 0x9480
+  __TEXT.__cstring: 0x2bc05
+  __TEXT.__oslogstring: 0xbb7e
+  __TEXT.__ustring: 0x218e
+  __TEXT.__dlopen_cstrs: 0x526
   __TEXT.__constg_swiftt: 0x1bc
   __TEXT.__swift5_typeref: 0x2ba
   __TEXT.__swift5_reflstr: 0x8e

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5d80
+  __TEXT.__unwind_info: 0x5f40
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6460
-  __DATA_CONST.__objc_classlist: 0xa80
+  __DATA_CONST.__const: 0x65a8
+  __DATA_CONST.__objc_classlist: 0xa90
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa3a8
+  __DATA_CONST.__objc_selrefs: 0xa4b0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x710
-  __DATA_CONST.__objc_arraydata: 0x11258
-  __DATA_CONST.__got: 0xe38
-  __AUTH_CONST.__const: 0x2370
-  __AUTH_CONST.__cfstring: 0x2dc00
-  __AUTH_CONST.__objc_const: 0x1f2f8
+  __DATA_CONST.__objc_superrefs: 0x720
+  __DATA_CONST.__objc_arraydata: 0x11290
+  __DATA_CONST.__got: 0xe50
+  __AUTH_CONST.__const: 0x23f0
+  __AUTH_CONST.__cfstring: 0x2de60
+  __AUTH_CONST.__objc_const: 0x1f780
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3ac8
+  __AUTH_CONST.__objc_arrayobj: 0x3ae0
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
-  __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1058
-  __AUTH.__objc_data: 0x5af0
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH.__objc_data: 0x5b90
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0x13b8
-  __DATA.__data: 0x1bf8
-  __DATA.__bss: 0x1930
+  __AUTH.__thread_vars: 0x48
+  __AUTH.__thread_bss: 0x18
+  __DATA.__objc_ivar: 0x13f8
+  __DATA.__data: 0x1c58
+  __DATA.__bss: 0x1990
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xa7f8
+  __DATA_DIRTY.__bss: 0xa808
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
+  - /System/Library/PrivateFrameworks/PommesRankingCore.framework/PommesRankingCore
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpotlightEmbeddingCore.framework/SpotlightEmbeddingCore

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8752
-  Symbols:   17393
-  CStrings:  8018
+  Functions: 8858
+  Symbols:   17615
+  CStrings:  8066
 
Symbols:
+ +[CSTestSearchableIndex cs_indexConnectionClassForTesting]
+ -[CSPommesQueryCandidateEvaluator _releaseContextCFRefs:]
+ -[CSPommesQueryCandidateEvaluator dealloc]
+ -[CSPommesQueryCandidateEvaluator evaluate:item:pass:]
+ -[CSPommesQueryCandidateEvaluator initWithRankingConfig:queryContext:]
+ -[CSPommesQueryCandidateEvaluator initWithRankingConfig:queryContext:queryStartTime:]
+ -[CSPommesQueryCandidateEvaluator matchesCandidate:]
+ -[CSPommesQueryCandidateEvaluator scoreCandidate:]
+ -[CSRankingModelQueryCandidateEvaluator .cxx_destruct]
+ -[CSRankingModelQueryCandidateEvaluator evalResultForCandidate:]
+ -[CSRankingModelQueryCandidateEvaluator initWithConfiguration:]
+ -[CSRankingModelQueryCandidateEvaluator matchesCandidate:]
+ -[CSRankingModelQueryCandidateEvaluator scoreCandidate:]
+ -[CSRequestQueue _forceDispatchAllLocked:]
+ -[CSRequestQueue _processWorkItemsUpToRequestIDLocked:qosFloor:]
+ -[CSRequestQueue drainWithQoSFloor:]
+ -[CSRequestQueue pendingWorkItemCount]
+ -[CSSearchQuery copyGroupedResultCounts]
+ -[CSSearchQuery queryStartTime]
+ -[CSSearchQueryContext drainBundleIDs]
+ -[CSSearchQueryContext drainDonations]
+ -[CSSearchQueryContext drainToken]
+ -[CSSearchQueryContext setDrainBundleIDs:]
+ -[CSSearchQueryContext setDrainDonations:]
+ -[CSSearchableIndex cs_enqueueDrainSentinelWithToken:retryCount:]
+ -[CSSearchableIndex cs_requiresInitializationForConnection:]
+ -[CSSearchableIndex cs_sendDrainResponseWithToken:outcome:queueDepth:]
+ -[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]
+ -[CSSearchableIndex performDrainWithToken:]
+ -[CSUserQuery deliverInjectedCandidatesAtStart]
+ -[CSUserQuery enqueueStartTimeCandidateInjection]
+ -[CSUserQuery pommesRankingConfiguration]
+ -[CSUserQuery processResultsForTopHitRanking:protectionClass:]
+ -[CSUserQuery resolveCandidateEvaluatorIfNeeded]
+ -[CSUserQuery setCandidateItems:]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table143
+ GCC_except_table160
+ GCC_except_table173
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table205
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table256
+ GCC_except_table269
+ GCC_except_table271
+ GCC_except_table278
+ GCC_except_table282
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table298
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table315
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table327
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table344
+ GCC_except_table349
+ GCC_except_table356
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table367
+ GCC_except_table372
+ GCC_except_table375
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table390
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table470
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table480
+ GCC_except_table517
+ GCC_except_table564
+ GCC_except_table67
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table81
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._isMail
+ _CFDictionaryGetCount
+ _CFStringGetLength
+ _CSDonationProgressFailedIndexesKey
+ _CSQueryCandidateEvaluatorForQuery
+ _ContactsLibraryCore
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_CSPommesQueryCandidateEvaluator
+ _OBJC_CLASS_$_CSRankingModelQueryCandidateEvaluator
+ _OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._evaluator
+ _OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._retrievalEvaluator
+ _OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._retrievalTree
+ _OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._weightedTree
+ _OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._configuration
+ _OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._memoCandidate
+ _OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._memoResult
+ _OBJC_IVAR_$_CSSearchQuery._xpcGroupedResultCounts
+ _OBJC_IVAR_$_CSSearchQueryContext._drainBundleIDs
+ _OBJC_IVAR_$_CSSearchQueryContext._drainToken
+ _OBJC_IVAR_$_CSUserQuery._candidateEvaluator
+ _OBJC_IVAR_$_CSUserQuery._candidateEvaluatorResolved
+ _OBJC_IVAR_$_CSUserQuery._candidateItems
+ _OBJC_IVAR_$_CSUserQuery._candidatesDelivered
+ _OBJC_IVAR_$_CSUserQuery._deliveredCandidateKeys
+ _OBJC_METACLASS_$_CSPommesQueryCandidateEvaluator
+ _OBJC_METACLASS_$_CSRankingModelQueryCandidateEvaluator
+ _PRBuildDefaultQueryTree
+ _PRBuildHomeQueryTree
+ _PRBuildMailQueryTree
+ _PRBuildMessagesQueryTree
+ _PRBuildPhotosQueryTree
+ _TCCLibrary
+ _TCCLibraryCore
+ _TCCLibraryCore.frameworkLibrary
+ __CSCopyContentSchemaContainer
+ __CSCopyContentSchemaContainer.sCachedSchema
+ __CSCopyContentSchemaContainer.sOnce
+ __MDCreateSimpleQueryEvaluatorWithWeightedTree
+ __MDSimpleQueryComputeRankingScore
+ __MDSimpleQueryDeallocate
+ __MDSimpleQueryObjectMatches
+ __OBJC_$_INSTANCE_METHODS_CSPommesQueryCandidateEvaluator
+ __OBJC_$_INSTANCE_METHODS_CSRankingModelQueryCandidateEvaluator
+ __OBJC_$_INSTANCE_VARIABLES_CSPommesQueryCandidateEvaluator
+ __OBJC_$_INSTANCE_VARIABLES_CSRankingModelQueryCandidateEvaluator
+ __OBJC_$_PROP_LIST_CSPommesQueryCandidateEvaluator
+ __OBJC_$_PROP_LIST_CSRankingModelQueryCandidateEvaluator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSQueryCandidateEvaluator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSQueryCandidateEvaluator
+ __OBJC_$_PROTOCOL_REFS_CSQueryCandidateEvaluator
+ __OBJC_CLASS_PROTOCOLS_$_CSPommesQueryCandidateEvaluator
+ __OBJC_CLASS_PROTOCOLS_$_CSRankingModelQueryCandidateEvaluator
+ __OBJC_CLASS_RO_$_CSPommesQueryCandidateEvaluator
+ __OBJC_CLASS_RO_$_CSRankingModelQueryCandidateEvaluator
+ __OBJC_LABEL_PROTOCOL_$_CSQueryCandidateEvaluator
+ __OBJC_METACLASS_RO_$_CSPommesQueryCandidateEvaluator
+ __OBJC_METACLASS_RO_$_CSRankingModelQueryCandidateEvaluator
+ __OBJC_PROTOCOL_$_CSQueryCandidateEvaluator
+ __ZNSt3__114priority_queueIN12_GLOBAL__N_18WorkItemENS_6vectorIS2_NS_9allocatorIS2_EEEENS1_18WorkItemComparatorEE3popEv
+ __ZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE22__base_destruct_at_endB9fqe220106EPS2_
+ __ZZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE12emplace_backIJjU8__strongU13block_pointerFvvERU8__strongP24CSSearchableIndexRequestEEEvDpOT_ENKUlvE0_clEv
+ ___33-[CSUserQuery setCandidateItems:]_block_invoke
+ ___42-[CSRequestQueue _forceDispatchAllLocked:]_block_invoke
+ ___49-[CSUserQuery enqueueStartTimeCandidateInjection]_block_invoke
+ ___49-[_CSLimitStage sortRecordArray:withDescriptors:]_block_invoke
+ ___65-[CSSearchableIndex cs_enqueueDrainSentinelWithToken:retryCount:]_block_invoke
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke_2
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke_3
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke_4
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke_2
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke_3
+ ___TCCLibraryCore_block_invoke
+ ____CSCopyContentSchemaContainer_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s88l8s72l8s80l8
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSString"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e30_v32?0"CSSearchQuery"8Q16^B24ls32l8s48l8s40l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e26_v16?0"CSSearchableItem"8ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e27_"NSArray"16?0"NSString"8ls32l8s40l8s48l8s56l8r64l8
+ ___cs_me_email_set_block_invoke
+ ___firstCyclePath_block_invoke
+ ___getTCCAccessPreflightSymbolLoc_block_invoke
+ ___getkTCCServiceAddressBookSymbolLoc_block_invoke
+ ___logForCSLogCategoryDrain_block_invoke
+ ___wireDonationQueries_block_invoke
+ ___wireDonationQueries_block_invoke_2
+ ___wireDonationQueries_block_invoke_3
+ __cs_pommes_current_attrs
+ __cs_pommes_current_attrs$tlv$init
+ __cs_pommes_current_provider
+ __cs_pommes_current_provider$tlv$init
+ __cs_pommes_current_synth_cache
+ __cs_pommes_current_synth_cache$tlv$init
+ __tlv_bootstrap
+ _audit_stringTCC
+ _build_ann_search_params
+ _build_pommes_search_params
+ _build_token_rewrites_map
+ _build_weighted_tree
+ _bundleIDTypeMaskForBundleIDs
+ _cs_any_address_in_me_set
+ _cs_copy_CompletionDate_Ranking
+ _cs_copy_DateAdded_Ranking
+ _cs_copy_DueDate_Ranking
+ _cs_copy_IsFromMe
+ _cs_copy_IsMe_attribute
+ _cs_copy_IsToMe
+ _cs_copy_MailDateLastViewed_Ranking
+ _cs_copy_MailDateReceived_Ranking
+ _cs_copy_StartDate_Ranking
+ _cs_interesting_date_consider
+ _cs_me_email_set
+ _db_free_query_node
+ _db_optimize_query_tree
+ _db_query_tree_expand_dynamic_values
+ _db_query_tree_lift_for_ranking
+ _db_query_tree_remap_field_names
+ _dedup_key_for_item
+ _getCNContactEmailAddressesKeySymbolLoc
+ _getTCCAccessPreflightSymbolLoc
+ _getTCCAccessPreflightSymbolLoc.ptr
+ _getkTCCServiceAddressBookSymbolLoc.ptr
+ _isMailClient
+ _isMessagesClient
+ _isPhotosClient
+ _isSearchToolClient
+ _isSettingsClient
+ _isSpotlightUIClient
+ _isSupportedCommandLineTool
+ _isWalletClient
+ _logForCSLogCategoryDrain
+ _logForCSLogCategoryDrain.onceToken
+ _logForCSLogCategoryDrain.sDrainLog
+ _mach_vm_allocate
+ _mach_vm_deallocate
+ _match_and_score_candidates
+ _merge_candidates
+ _objc_moveWeak
+ _objc_msgSend$_forceDispatchAllLocked:
+ _objc_msgSend$_processWorkItemsUpToRequestIDLocked:qosFloor:
+ _objc_msgSend$_releaseContextCFRefs:
+ _objc_msgSend$authorizationStatusForEntityType:
+ _objc_msgSend$cs_enqueueDrainSentinelWithToken:retryCount:
+ _objc_msgSend$cs_requiresInitializationForConnection:
+ _objc_msgSend$cs_sendDrainResponseWithToken:outcome:queueDepth:
+ _objc_msgSend$deliverInjectedCandidatesAtStart
+ _objc_msgSend$dimension
+ _objc_msgSend$drainBundleIDs
+ _objc_msgSend$drainToken
+ _objc_msgSend$drainWithQoSFloor:
+ _objc_msgSend$enqueueStartTimeCandidateInjection
+ _objc_msgSend$evalResultForCandidate:
+ _objc_msgSend$evaluate:item:pass:
+ _objc_msgSend$format
+ _objc_msgSend$initWithRankingConfig:queryContext:queryStartTime:
+ _objc_msgSend$isHome
+ _objc_msgSend$matchesCandidate:
+ _objc_msgSend$originalToken
+ _objc_msgSend$pendingWorkItemCount
+ _objc_msgSend$performDrainWithToken:
+ _objc_msgSend$pommesRankingConfiguration
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$queryStartTime
+ _objc_msgSend$resolveCandidateEvaluatorIfNeeded
+ _objc_msgSend$scoreCandidate:
+ _objc_msgSend$setDrainBundleIDs:
+ _objc_msgSend$setSearchableIndex:
+ _objc_msgSend$tokenRewrites
+ _objc_msgSend$variations
+ _objc_msgSend$vectors
+ _pommes_attribute_getter
+ _pommes_resolve_friendly_field_name
+ _populate_pr_context
+ _sCSSearchableIndexAvailableRequestCountLock
+ _s_me_email_set
+ _s_me_email_set_once
+ _si_calendar_release
+ _si_calendar_retain
- GCC_except_table101
- GCC_except_table112
- GCC_except_table113
- GCC_except_table119
- GCC_except_table154
- GCC_except_table155
- GCC_except_table174
- GCC_except_table177
- GCC_except_table188
- GCC_except_table190
- GCC_except_table198
- GCC_except_table203
- GCC_except_table211
- GCC_except_table215
- GCC_except_table234
- GCC_except_table238
- GCC_except_table240
- GCC_except_table242
- GCC_except_table247
- GCC_except_table248
- GCC_except_table252
- GCC_except_table254
- GCC_except_table264
- GCC_except_table270
- GCC_except_table274
- GCC_except_table279
- GCC_except_table288
- GCC_except_table299
- GCC_except_table305
- GCC_except_table308
- GCC_except_table310
- GCC_except_table312
- GCC_except_table314
- GCC_except_table318
- GCC_except_table321
- GCC_except_table322
- GCC_except_table337
- GCC_except_table342
- GCC_except_table346
- GCC_except_table347
- GCC_except_table350
- GCC_except_table355
- GCC_except_table364
- GCC_except_table368
- GCC_except_table373
- GCC_except_table377
- GCC_except_table381
- GCC_except_table383
- GCC_except_table461
- GCC_except_table462
- GCC_except_table463
- GCC_except_table464
- GCC_except_table508
- GCC_except_table62
- GCC_except_table74
- GCC_except_table75
- GCC_except_table84
- GCC_except_table88
- GCC_except_table90
- __ZZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE12emplace_backIJjU8__strongU13block_pointerFvvEEEEvDpOT_ENKUlvE0_clEv
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- _objc_msgSend$sortedArrayUsingDescriptors:
CStrings:
+ " → "
+ "%@\x1f%@"
+ "%{public}@"
+ "@\"NSArray\"16@?0@\"NSString\"8"
+ "B24@?0@8@\"NSDictionary\"16"
+ "CSDonationProgressFailedIndexes"
+ "Cycle detected in pipeline dependencies (stages not orderable: %@)."
+ "Cycle detected in pipeline dependencies: %@. A stage's input chain must not lead back to itself — restructure so each stage reads from an earlier, distinct stage."
+ "Donation progress payload is not NSData, skipping. bundle: %@, indexName: %@"
+ "Donation progress query failed for index: %@, error: %@"
+ "Drain"
+ "Drain acknowledged, token:%@ declined:%d depth:%lu"
+ "Drain completed, token:%@ outcome:%llu depth:%@"
+ "Drain received, bundleID:%@ token:%@"
+ "Requested drain for %lu bundles, only the first %lu are considered"
+ "Stage '%@' references undefined stage '%@'"
+ "TCCAccessPreflight"
+ "[CSUserQuery] setCandidateItems: called with %lu item(s)"
+ "[CSUserQuery][qid=%ld] candidate evaluator resolved: %@"
+ "[CSUserQuery][qid=%ld] merged %lu matched candidates (%lu indexed → %lu merged)"
+ "[CSUserQuery][qid=%ld] merged %lu matched candidates into top-hit batch (%lu indexed → %lu merged)"
+ "[CSUserQuery][qid=%ld] no candidate evaluator for this query; candidate injection skipped"
+ "[CSUserQuery][qid=%ld] no candidates matched the query; batch unchanged"
+ "[CSUserQuery][qid=%ld] no candidates matched the query; top-hit batch unchanged"
+ "[CSUserQuery][qid=%ld] start-time injection delivered %lu candidate(s)"
+ "_kMDItemApplicationLastLaunchedDate_Ranking"
+ "com.apple.notes.spotlightrecord"
+ "delete-donation-progress"
+ "drain-declined-queue-depth"
+ "drain-outcome"
+ "drain-queue"
+ "drain-response"
+ "drain-token"
+ "drainBundleIDs"
+ "drainToken"
+ "drb"
+ "drt"
+ "kMDItemCompletionDate_Ranking"
+ "kMDItemContentModificationDate_Ranking"
+ "kMDItemDueDate_Ranking"
+ "kMDItemInterestingDate_Ranking"
+ "kMDItemMailDateLastViewed_Ranking"
+ "kMDItemStartDate_Ranking"
+ "kTCCServiceAddressBook"
+ "softlink:o:path:/System/Library/Frameworks/Contacts.framework/Contacts"
+ "softlink:o:path:/System/Library/PrivateFrameworks/TCC.framework/TCC"
+ "v16@?0@\"CSSearchableItem\"8"
+ "v32@?0@\"CSSearchQuery\"8Q16^B24"
+ "vec_data_format"
+ "vec_dimensions"
+ "vectors"
- "\rU"
- "DEBUG CSStructuredQuery: compiled queryString = '%s'\n"
- "kMDItemLocation"
```
