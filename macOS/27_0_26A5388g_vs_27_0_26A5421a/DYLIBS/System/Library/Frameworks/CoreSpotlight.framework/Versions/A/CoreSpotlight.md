## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x194574
-  __TEXT.__objc_methlist: 0x14518
-  __TEXT.__const: 0xf50
-  __TEXT.__cstring: 0x2c1bf
-  __TEXT.__oslogstring: 0xb833
-  __TEXT.__gcc_except_tab: 0x9444
-  __TEXT.__ustring: 0x2040
-  __TEXT.__dlopen_cstrs: 0x40f
+2459.405.0.0.0
+  __TEXT.__text: 0x19c65c
+  __TEXT.__objc_methlist: 0x146f8
+  __TEXT.__const: 0xf60
+  __TEXT.__cstring: 0x2c481
+  __TEXT.__oslogstring: 0xbce7
+  __TEXT.__gcc_except_tab: 0x988c
+  __TEXT.__ustring: 0x218e
+  __TEXT.__dlopen_cstrs: 0x49a
   __TEXT.__constg_swiftt: 0x1bc
   __TEXT.__swift5_typeref: 0x2ba
   __TEXT.__swift5_reflstr: 0x8e

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5fa0
+  __TEXT.__unwind_info: 0x6158
   __TEXT.__eh_frame: 0x1e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ed0
-  __DATA_CONST.__objc_classlist: 0xaa0
+  __DATA_CONST.__const: 0x3f28
+  __DATA_CONST.__objc_classlist: 0xab0
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa4e0
+  __DATA_CONST.__objc_selrefs: 0xa5d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x718
-  __DATA_CONST.__objc_arraydata: 0x110d0
-  __DATA_CONST.__got: 0xea0
-  __AUTH_CONST.__const: 0x5310
-  __AUTH_CONST.__cfstring: 0x2dc00
-  __AUTH_CONST.__objc_const: 0x1fa98
+  __DATA_CONST.__objc_superrefs: 0x728
+  __DATA_CONST.__objc_arraydata: 0x11108
+  __DATA_CONST.__got: 0xeb8
+  __AUTH_CONST.__const: 0x54b0
+  __AUTH_CONST.__cfstring: 0x2de00
+  __AUTH_CONST.__objc_const: 0x1ff20
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3a80
+  __AUTH_CONST.__objc_arrayobj: 0x3a98
   __AUTH_CONST.__objc_dictobj: 0xaf78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x180
-  __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1230
-  __AUTH.__objc_data: 0x5af0
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0x1320
+  __AUTH.__objc_data: 0x5b90
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0x141c
-  __DATA.__data: 0x1be0
-  __DATA.__bss: 0x1930
+  __AUTH.__thread_vars: 0x48
+  __AUTH.__thread_bss: 0x18
+  __DATA.__objc_ivar: 0x145c
+  __DATA.__data: 0x1c40
+  __DATA.__bss: 0x19a0
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xa7e0
+  __DATA_DIRTY.__bss: 0xa7f0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
+  - /System/Library/PrivateFrameworks/PommesRankingCore.framework/Versions/A/PommesRankingCore
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/SpotlightEmbeddingCore.framework/Versions/A/SpotlightEmbeddingCore

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8993
-  Symbols:   17949
-  CStrings:  8034
+  Functions: 9103
+  Symbols:   18171
+  CStrings:  8083
 
Symbols:
+ +[CSTestSearchableIndex cs_indexConnectionClassForTesting]
+ -[CSInlineDonation _errorWithCode:description:underlying:]
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
+ GCC_except_table120
+ GCC_except_table135
+ GCC_except_table147
+ GCC_except_table165
+ GCC_except_table175
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table192
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table257
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table287
+ GCC_except_table289
+ GCC_except_table294
+ GCC_except_table296
+ GCC_except_table300
+ GCC_except_table305
+ GCC_except_table323
+ GCC_except_table327
+ GCC_except_table329
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table356
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table364
+ GCC_except_table368
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table388
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table410
+ GCC_except_table417
+ GCC_except_table422
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table439
+ GCC_except_table445
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table470
+ GCC_except_table475
+ GCC_except_table561
+ GCC_except_table563
+ GCC_except_table564
+ GCC_except_table572
+ GCC_except_table609
+ GCC_except_table663
+ GCC_except_table83
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._evaluator
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._isMail
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._retrievalEvaluator
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._retrievalTree
+ OBJC_IVAR_$_CSPommesQueryCandidateEvaluator._weightedTree
+ OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._configuration
+ OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._memoCandidate
+ OBJC_IVAR_$_CSRankingModelQueryCandidateEvaluator._memoResult
+ OBJC_IVAR_$_CSSearchQuery._xpcGroupedResultCounts
+ OBJC_IVAR_$_CSSearchQueryContext._drainBundleIDs
+ OBJC_IVAR_$_CSSearchQueryContext._drainToken
+ OBJC_IVAR_$_CSUserQuery._candidateEvaluator
+ OBJC_IVAR_$_CSUserQuery._candidateEvaluatorResolved
+ OBJC_IVAR_$_CSUserQuery._candidateItems
+ OBJC_IVAR_$_CSUserQuery._candidatesDelivered
+ OBJC_IVAR_$_CSUserQuery._deliveredCandidateKeys
+ TCCLibraryCore.frameworkLibrary
+ _CFDictionaryGetCount
+ _CFStringGetLength
+ _CSCopyContentSchemaContainer
+ _CSCopyContentSchemaContainer.sCachedSchema
+ _CSCopyContentSchemaContainer.sOnce
+ _CSDonationProgressFailedIndexesKey
+ _CSQueryCandidateEvaluatorForQuery
+ _ContactsLibraryCore
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_CSPommesQueryCandidateEvaluator
+ _OBJC_CLASS_$_CSRankingModelQueryCandidateEvaluator
+ _OBJC_METACLASS_$_CSPommesQueryCandidateEvaluator
+ _OBJC_METACLASS_$_CSRankingModelQueryCandidateEvaluator
+ _OUTLINED_FUNCTION_25
+ _PRBuildDefaultQueryTree
+ _PRBuildHomeQueryTree
+ _PRBuildMailQueryTree
+ _PRBuildMessagesQueryTree
+ _PRBuildPhotosQueryTree
+ _TCCLibrary
+ _TCCLibraryCore
+ __65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke
+ __CSCopyContentSchemaContainer
+ __MDCreateSimpleQueryEvaluatorWithWeightedTree
+ __MDQueryCopyGroupedResultCounts
+ __MDSimpleQueryComputeRankingScore
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
+ __ZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE22__base_destruct_at_endB9nqe220106EPS2_
+ __ZZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE12emplace_backIJjU8__strongU13block_pointerFvvERU8__strongP24CSSearchableIndexRequestEEEvDpOT_ENKUlvE0_clEv
+ ___33-[CSUserQuery setCandidateItems:]_block_invoke
+ ___42-[CSRequestQueue _forceDispatchAllLocked:]_block_invoke
+ ___49-[CSUserQuery enqueueStartTimeCandidateInjection]_block_invoke
+ ___49-[_CSLimitStage sortRecordArray:withDescriptors:]_block_invoke
+ ___65-[CSSearchableIndex cs_enqueueDrainSentinelWithToken:retryCount:]_block_invoke
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke_2
+ ___65-[CSSearchableIndex deleteDonationProgressWithCompletionHandler:]_block_invoke_3
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke_2
+ ___TCCLibraryCore_block_invoke
+ ____CSCopyContentSchemaContainer_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e30_v32?0"CSSearchQuery"8Q16^B24l
+ ___block_descriptor_72_e8_32s40s48s56s64r_e26_v16?0"CSSearchableItem"8l
+ ___block_descriptor_72_e8_32s40s48s56s64r_e27_"NSArray"16?0"NSString"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b
+ ___cs_me_email_set_block_invoke
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s
+ ___firstCyclePath_block_invoke
+ ___getTCCAccessPreflightSymbolLoc_block_invoke
+ ___getkTCCServiceAddressBookSymbolLoc_block_invoke
+ ___logForCSLogCategoryDrain_block_invoke
+ ___wireDonationQueries_block_invoke
+ ___wireDonationQueries_block_invoke_2
+ __cs_me_email_set_block_invoke
+ __cs_pommes_current_attrs
+ __cs_pommes_current_attrs$tlv$init
+ __cs_pommes_current_provider
+ __cs_pommes_current_provider$tlv$init
+ __cs_pommes_current_synth_cache
+ __cs_pommes_current_synth_cache$tlv$init
+ __tlv_bootstrap
+ __wireDonationQueries_block_invoke
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
+ _isMailClient
+ _isMessagesClient
+ _isPhotosClient
+ _isSearchToolClient
+ _isSettingsClient
+ _isSpotlightUIClient
+ _isSupportedCommandLineTool
+ _isWalletClient
+ _logForCSLogCategoryDrain
+ _mach_vm_allocate
+ _mach_vm_deallocate
+ _match_and_score_candidates
+ _merge_candidates
+ _objc_moveWeak
+ _objc_msgSend$_errorWithCode:description:underlying:
+ _objc_msgSend$_forceDispatchAllLocked:
+ _objc_msgSend$_processWorkItemsUpToRequestIDLocked:qosFloor:
+ _objc_msgSend$_releaseContextCFRefs:
+ _objc_msgSend$cs_enqueueDrainSentinelWithToken:retryCount:
+ _objc_msgSend$cs_requiresInitializationForConnection:
+ _objc_msgSend$cs_sendDrainResponseWithToken:outcome:queueDepth:
+ _objc_msgSend$deliverInjectedCandidatesAtStart
+ _objc_msgSend$drainBundleIDs
+ _objc_msgSend$drainToken
+ _objc_msgSend$drainWithQoSFloor:
+ _objc_msgSend$enqueueStartTimeCandidateInjection
+ _objc_msgSend$evalResultForCandidate:
+ _objc_msgSend$evaluate:item:pass:
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
+ _objc_msgSend$variations
+ _pommes_attribute_getter
+ _pommes_resolve_friendly_field_name
+ _populate_pr_context
+ _sCSSearchableIndexAvailableRequestCountLock
+ _s_me_email_set
+ _s_me_email_set_once
+ _si_calendar_release
+ _si_calendar_retain
+ _strdup
+ cs_me_email_set
+ getTCCAccessPreflightSymbolLoc.ptr
+ getkTCCServiceAddressBookSymbolLoc.ptr
+ logForCSLogCategoryDrain
+ logForCSLogCategoryDrain.onceToken
+ logForCSLogCategoryDrain.sDrainLog
- -[CSInlineDonation _logErrorWithCode:description:underlying:]
- GCC_except_table100
- GCC_except_table132
- GCC_except_table148
- GCC_except_table149
- GCC_except_table160
- GCC_except_table176
- GCC_except_table180
- GCC_except_table184
- GCC_except_table188
- GCC_except_table194
- GCC_except_table196
- GCC_except_table214
- GCC_except_table217
- GCC_except_table218
- GCC_except_table221
- GCC_except_table222
- GCC_except_table226
- GCC_except_table239
- GCC_except_table246
- GCC_except_table247
- GCC_except_table260
- GCC_except_table266
- GCC_except_table268
- GCC_except_table270
- GCC_except_table275
- GCC_except_table277
- GCC_except_table278
- GCC_except_table288
- GCC_except_table292
- GCC_except_table297
- GCC_except_table301
- GCC_except_table310
- GCC_except_table311
- GCC_except_table314
- GCC_except_table319
- GCC_except_table330
- GCC_except_table338
- GCC_except_table342
- GCC_except_table348
- GCC_except_table357
- GCC_except_table359
- GCC_except_table362
- GCC_except_table366
- GCC_except_table367
- GCC_except_table381
- GCC_except_table391
- GCC_except_table392
- GCC_except_table398
- GCC_except_table400
- GCC_except_table407
- GCC_except_table408
- GCC_except_table428
- GCC_except_table429
- GCC_except_table432
- GCC_except_table438
- GCC_except_table442
- GCC_except_table448
- GCC_except_table458
- GCC_except_table551
- GCC_except_table552
- GCC_except_table553
- GCC_except_table554
- GCC_except_table599
- GCC_except_table76
- GCC_except_table85
- __ZZNSt3__16vectorIN12_GLOBAL__N_18WorkItemENS_9allocatorIS2_EEE12emplace_backIJjU8__strongU13block_pointerFvvEEEEvDpOT_ENKUlvE0_clEv
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8l
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8l
- _objc_msgSend$_logErrorWithCode:description:underlying:
- _objc_msgSend$sortedArrayUsingDescriptors:
CStrings:
+ " → "
+ "%@\x1f%@"
+ "%{public}@"
+ "/System/Library/PrivateFrameworks/TCC.framework/Contents/MacOS/TCC"
+ "@\"NSArray\"16@?0@\"NSString\"8"
+ "B24@?0@8@\"NSDictionary\"16"
+ "CSDonationProgressFailedIndexes"
+ "Capping managed donation-progress queries at %lu; dropping %lu enabled index path(s)"
+ "Completed donation: %@ result: success"
+ "Cycle detected in pipeline dependencies (stages not orderable: %@)."
+ "Cycle detected in pipeline dependencies: %@. A stage's input chain must not lead back to itself — restructure so each stage reads from an earlier, distinct stage."
+ "Donation progress payload is not NSData, skipping. bundle: %@, indexName: %@"
+ "Donation progress query failed for index: %@, error: %@"
+ "Donation unsuccessful: %@ result: %@"
+ "Drain"
+ "Drain acknowledged, token:%@ declined:%d depth:%lu"
+ "Drain completed, token:%@ outcome:%llu depth:%@"
+ "Drain received, bundleID:%@ token:%@"
+ "Requested drain for %lu bundles, only the first %lu are considered"
+ "Skipping managed donation-progress query, index path does not exist: %@"
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
- "\rU"
- "%@: %@ %@"
- "DEBUG CSStructuredQuery: compiled queryString = '%s'\n"
- "kMDItemLocation"
```
