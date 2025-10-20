## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.200.72.2.3
-  __TEXT.__text: 0x266db4
+3864.200.81.2.5
+  __TEXT.__text: 0x26a424
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_methlist: 0x1306c
-  __TEXT.__const: 0x358c
-  __TEXT.__gcc_except_tab: 0x4ef88
-  __TEXT.__cstring: 0x26eaa
-  __TEXT.__oslogstring: 0x1a594
+  __TEXT.__objc_methlist: 0x1329c
+  __TEXT.__const: 0x399c
+  __TEXT.__gcc_except_tab: 0x4f5bc
+  __TEXT.__cstring: 0x26f0a
+  __TEXT.__oslogstring: 0x1a6e4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x2c
-  __TEXT.__constg_swiftt: 0xb68
-  __TEXT.__swift5_typeref: 0xdc1
+  __TEXT.__constg_swiftt: 0xb84
+  __TEXT.__swift5_typeref: 0xdc7
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0xd04
-  __TEXT.__swift5_fieldmd: 0x111c
+  __TEXT.__swift5_fieldmd: 0x1120
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x26c
-  __TEXT.__swift5_types: 0x140
+  __TEXT.__swift5_types: 0x144
   __TEXT.__swift5_capture: 0x3dc
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x109f0
+  __TEXT.__unwind_info: 0x10b88
   __TEXT.__eh_frame: 0xfb0
-  __TEXT.__objc_classname: 0x2c79
-  __TEXT.__objc_methname: 0x3765d
-  __TEXT.__objc_methtype: 0x7979
-  __TEXT.__objc_stubs: 0x24f00
-  __DATA_CONST.__got: 0x1b78
-  __DATA_CONST.__const: 0x94f0
-  __DATA_CONST.__objc_classlist: 0x938
+  __TEXT.__objc_classname: 0x2c94
+  __TEXT.__objc_methname: 0x37ddf
+  __TEXT.__objc_methtype: 0x7a1d
+  __TEXT.__objc_stubs: 0x253c0
+  __DATA_CONST.__got: 0x1bc8
+  __DATA_CONST.__const: 0x95b0
+  __DATA_CONST.__objc_classlist: 0x940
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf38
+  __DATA_CONST.__objc_selrefs: 0xb080
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x1398
-  __AUTH_CONST.__const: 0x5c08
-  __AUTH_CONST.__cfstring: 0x105e0
-  __AUTH_CONST.__objc_const: 0x21780
+  __AUTH_CONST.__const: 0x5cd8
+  __AUTH_CONST.__cfstring: 0x10600
+  __AUTH_CONST.__objc_const: 0x219f0
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xea0
+  __AUTH.__objc_data: 0xef0
   __AUTH.__data: 0x4f8
-  __DATA.__objc_ivar: 0x146c
-  __DATA.__data: 0x3570
+  __DATA.__objc_ivar: 0x1490
+  __DATA.__data: 0x36b0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x4750
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x50b8
-  __DATA_DIRTY.__data: 0xda8
+  __DATA_DIRTY.__objc_data: 0x50b0
+  __DATA_DIRTY.__data: 0xc30
   __DATA_DIRTY.__bss: 0x1640
-  __DATA_DIRTY.__common: 0x48
+  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3620E621-4C0C-3330-8A06-5C1980562ED2
-  Functions: 10713
-  Symbols:   34481
-  CStrings:  14264
+  UUID: F09BC7CF-0C44-392E-A6D9-2F303BA9ACC6
+  Functions: 10776
+  Symbols:   34699
+  CStrings:  14339
 
Symbols:
+ -[EDGroupedSenderQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:]
+ -[EDGroupedSenderQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:]
+ -[EDInMemoryThreadQueryHandler _extraInfoFromLocalSearchInfoCollector:]
+ -[EDInMemoryThreadQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:]
+ -[EDInMemoryThreadQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:].cold.1
+ -[EDInMemoryThreadQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:]
+ -[EDLocalSearchInfoCollector .cxx_destruct]
+ -[EDLocalSearchInfoCollector _combinedHasQueryEmbedding]
+ -[EDLocalSearchInfoCollector _combinedQueryStatus]
+ -[EDLocalSearchInfoCollector allRankingsByObjectID]
+ -[EDLocalSearchInfoCollector hasEmbeddingResults]
+ -[EDLocalSearchInfoCollector hasKeywordResults]
+ -[EDLocalSearchInfoCollector hasLiveSearchQueryEmbedding]
+ -[EDLocalSearchInfoCollector hasTopHitsQueryEmbedding]
+ -[EDLocalSearchInfoCollector init]
+ -[EDLocalSearchInfoCollector liveSearchQueryStatus]
+ -[EDLocalSearchInfoCollector localSearchInfoForConversationIDs:]
+ -[EDLocalSearchInfoCollector localSearchInfoForMessageObjectIDs:]
+ -[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]
+ -[EDLocalSearchInfoCollector rankingObjectIDsByConversation]
+ -[EDLocalSearchInfoCollector setAllRankingsByObjectID:]
+ -[EDLocalSearchInfoCollector setHasEmbeddingResults:]
+ -[EDLocalSearchInfoCollector setHasKeywordResults:]
+ -[EDLocalSearchInfoCollector setHasLiveSearchQueryEmbedding:]
+ -[EDLocalSearchInfoCollector setHasTopHitsQueryEmbedding:]
+ -[EDLocalSearchInfoCollector setLiveSearchQueryStatus:]
+ -[EDLocalSearchInfoCollector setRankingObjectIDsByConversation:]
+ -[EDLocalSearchInfoCollector setTopHitsQueryStatus:]
+ -[EDLocalSearchInfoCollector topHitsQueryStatus]
+ -[EDMessageQueryHandler _extraInfoFromLocalSearchInfoCollector:]
+ -[EDMessageQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:]
+ -[EDMessageQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:].cold.1
+ -[EDMessageQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:]
+ -[EDMessageQueryHelper localSearchDidFail]
+ -[EDMessageQueryHelper localSearchDidFail].cold.1
+ -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]
+ -[EDMessageQueryHelper localSearchDidFinishTopHitsQuery:]
+ -[EDMessageQueryHelper localSearchDidHaveQueryEmbedding:]
+ -[EDMessageQueryHelper localSearchDidHaveTopHitsQueryEmbedding:]
+ -[EDMessageQueryHelper localSearchInfoCollector]
+ -[EDMessageQueryHelper setLocalSearchInfoCollector:]
+ -[EDPersistenceDatabaseConnection deleteAttachmentItems:]
+ -[EDPersistenceDatabaseConnection deleteRichLinkItems:]
+ -[EDSearchableIndexUpdates initWithIdentifiers:]
+ -[EDSearchableIndexUpdates initWithIndexableItems:]
+ -[EDSearchableIndexUpdates initWithIndexableItems:removedIdentifiers:removedDomainIdentifiers:]
+ -[EDThreadQueryHandler observerDidFailInitialLoad:extraInfo:]
+ -[EDThreadQueryHandler observerDidFailInitialLoad:extraInfo:].cold.1
+ -[EDThreadQueryHandler observerDidFinishInitialLoad:extraInfo:]
+ -[EDThreadQueryHandler observerDidFinishInitialLoad:extraInfo:].cold.1
+ -[_EDMessageItemIDCollector queryHelperDidFailInitialLoad:localSearchInfoCollector:]
+ -[_EDMessageItemIDCollector queryHelperDidFindAllMessages:localSearchInfoCollector:]
+ -[_EDMessageQueryHandlerList allMessageObjectIDs]
+ -[_EDMessageQueryHelperEntry messageObjectID]
+ _EMMessageListExtraInfoKeyLocalSearchInfo
+ _MDItemUseCount
+ _MDItemUsedDates
+ _MDMailFlagged
+ _MDMailRepliedTo
+ _MDQueryResultScoreL1
+ _MDQueryResultScoreL2
+ _OBJC_CLASS_$_EDLocalSearchInfoCollector
+ _OBJC_CLASS_$_EMLocalSearchInfo
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._allRankingsByObjectID
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._hasEmbeddingResults
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._hasKeywordResults
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._hasLiveSearchQueryEmbedding
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._hasTopHitsQueryEmbedding
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._liveSearchQueryStatus
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._rankingObjectIDsByConversation
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._topHitsQueryStatus
+ _OBJC_IVAR_$_EDMessageQueryHelper._localSearchInfoCollector
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._messageObjectID
+ _OBJC_METACLASS_$_EDLocalSearchInfoCollector
+ __OBJC_$_INSTANCE_METHODS_EDLocalSearchInfoCollector
+ __OBJC_$_INSTANCE_VARIABLES_EDLocalSearchInfoCollector
+ __OBJC_$_PROP_LIST_EDLocalSearchInfoCollector
+ __OBJC_$_PROP_LIST_EDThreadQueryHandler.272
+ __OBJC_CLASS_RO_$_EDLocalSearchInfoCollector
+ __OBJC_METACLASS_RO_$_EDLocalSearchInfoCollector
+ ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.77
+ ___106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.64
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.425
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.426
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.427
+ ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke.74
+ ___29-[EDMessageQueryHelper start]_block_invoke.37
+ ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke.46
+ ___42-[EDMessageQueryHelper localSearchDidFail]_block_invoke
+ ___49-[_EDMessageQueryHandlerList allMessageObjectIDs]_block_invoke
+ ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.342
+ ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.345
+ ___59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.348
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.291
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.297
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.302
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.303
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.305
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.292
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.300
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_3.293
+ ___61-[EDThreadQueryHandler observerDidFailInitialLoad:extraInfo:]_block_invoke
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.19
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.24
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.25
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.25.cold.1
+ ___63-[EDMessageQueryHandler queryHelper:didAddMessages:searchInfo:]_block_invoke.49
+ ___63-[EDThreadQueryHandler observerDidFinishInitialLoad:extraInfo:]_block_invoke
+ ___64-[EDMessageQueryHandler _extraInfoFromLocalSearchInfoCollector:]_block_invoke
+ ___64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.343
+ ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.344
+ ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.344.cold.1
+ ___67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.60
+ ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.352
+ ___71-[EDInMemoryThreadQueryHandler _extraInfoFromLocalSearchInfoCollector:]_block_invoke
+ ___71-[EDInMemoryThreadQueryHandler _extraInfoFromLocalSearchInfoCollector:]_block_invoke_2
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.329
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.329.cold.1
+ ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke.56
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.17
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.281
+ ___80-[EDMessageQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:]_block_invoke
+ ___80-[EDMessageQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:]_block_invoke
+ ___82-[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]_block_invoke
+ ___82-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]_block_invoke
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.273
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.273.cold.1
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.276
+ ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.64
+ ___87-[EDInMemoryThreadQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:]_block_invoke
+ ___87-[EDInMemoryThreadQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:]_block_invoke
+ ___87-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) deleteAttachmentItems:]_block_invoke
+ ___block_descriptor_32_e39_"NSNumber"16?0"EDIndexedAttachment"8l
+ ___block_descriptor_32_e55_"EMMessageObjectID"16?0"_EDMessageQueryHelperEntry"8l
+ ___block_descriptor_40_ea8_32r_e21_v24?0"NSArray"8^B16lr32l8
+ ___block_descriptor_48_ea8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_ea8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e33_v32?0"CSSearchableItem"8Q16^B24lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.167
+ ___block_literal_global.320
+ ___block_literal_global.338
+ ___block_literal_global.34
+ ___block_literal_global.361
+ ___block_literal_global.369
+ ___block_literal_global.372
+ ___block_literal_global.41
+ ___block_literal_global.417
+ ___block_literal_global.474
+ ___block_literal_global.782
+ ___block_literal_global.99
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _kMSParsecSearchSessionMaximumRankedSectionResultsCount
+ _objc_msgSend$_combinedHasQueryEmbedding
+ _objc_msgSend$_combinedQueryStatus
+ _objc_msgSend$_extraInfoFromLocalSearchInfoCollector:
+ _objc_msgSend$allMessageObjectIDs
+ _objc_msgSend$allRankingsByObjectID
+ _objc_msgSend$ef_setOptionalObject:forKey:
+ _objc_msgSend$em_mailRankingSignals
+ _objc_msgSend$hasEmbeddingResults
+ _objc_msgSend$hasKeywordResults
+ _objc_msgSend$hasLiveSearchQueryEmbedding
+ _objc_msgSend$hasTopHitsQueryEmbedding
+ _objc_msgSend$initWithIdentifiers:
+ _objc_msgSend$initWithIndexableItems:
+ _objc_msgSend$initWithIndexableItems:removedIdentifiers:removedDomainIdentifiers:
+ _objc_msgSend$initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:rankingSignalsByObjectID:
+ _objc_msgSend$isSemanticMatch
+ _objc_msgSend$isSyntacticMatch
+ _objc_msgSend$liveSearchQueryStatus
+ _objc_msgSend$localSearchDidFail
+ _objc_msgSend$localSearchDidFindMessages:itemSnippetData:rankingSignals:
+ _objc_msgSend$localSearchDidFinishTopHitsQuery:
+ _objc_msgSend$localSearchDidHaveQueryEmbedding:
+ _objc_msgSend$localSearchDidHaveTopHitsQueryEmbedding:
+ _objc_msgSend$localSearchInfoCollector
+ _objc_msgSend$localSearchInfoForConversationIDs:
+ _objc_msgSend$localSearchInfoForMessageObjectIDs:
+ _objc_msgSend$messageObjectID
+ _objc_msgSend$observerDidFailInitialLoad:extraInfo:
+ _objc_msgSend$observerDidFinishInitialLoad:extraInfo:
+ _objc_msgSend$processRankingSignalsBySearchableItemID:forMessages:
+ _objc_msgSend$queryHelperDidFailInitialLoad:localSearchInfoCollector:
+ _objc_msgSend$queryHelperDidFindAllMessages:localSearchInfoCollector:
+ _objc_msgSend$rankingObjectIDsByConversation
+ _objc_msgSend$setEmbeddingBlock:
+ _objc_msgSend$setEmbeddingHandler:
+ _objc_msgSend$setHasEmbeddingResults:
+ _objc_msgSend$setHasKeywordResults:
+ _objc_msgSend$setHasLiveSearchQueryEmbedding:
+ _objc_msgSend$setHasTopHitsQueryEmbedding:
+ _objc_msgSend$setLiveSearchQueryStatus:
+ _objc_msgSend$setTopHitsQueryStatus:
+ _objc_msgSend$topHitsQueryStatus
+ _symbolic _____ 11EmailDaemon19MailMessageEntityIDV7VersionO
- -[EDGroupedSenderQueryHandler queryHelperDidFindAllMessages:]
- -[EDInMemoryThreadQueryHandler queryHelperDidFindAllMessages:]
- -[EDMessageQueryHandler queryHelperDidFindAllMessages:]
- -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]
- -[EDSearchableIndexUpdates initWithIndexedItems:]
- -[EDThreadQueryHandler observerDidFinishInitialLoad:]
- -[EDThreadQueryHandler observerDidFinishInitialLoad:].cold.1
- -[_EDMessageItemIDCollector queryHelperDidFindAllMessages:]
- _OBJC_IVAR_$__EDMessageQueryHelperEntry._globalMessageID
- __OBJC_$_PROP_LIST_EDThreadQueryHandler.271
- ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.76
- ___106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.63
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.413
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.418
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.419
- ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke.73
- ___29-[EDMessageQueryHelper start]_block_invoke.35
- ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke.45
- ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.346
- ___53-[EDThreadQueryHandler observerDidFinishInitialLoad:]_block_invoke
- ___55-[EDMessageQueryHandler queryHelperDidFindAllMessages:]_block_invoke
- ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.349
- ___59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.352
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.299
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.301
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.306
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.307
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.309
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.296
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.304
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_3.297
- ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.17
- ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.22
- ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.22.cold.1
- ___62-[EDInMemoryThreadQueryHandler queryHelperDidFindAllMessages:]_block_invoke
- ___63-[EDMessageQueryHandler queryHelper:didAddMessages:searchInfo:]_block_invoke.46
- ___64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.347
- ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.348
- ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.348.cold.1
- ___67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.59
- ___67-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]_block_invoke
- ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.356
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.333
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.333.cold.1
- ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke.55
- ___76-[EDSearchableIndex _dataSourceAssignTransaction:forIdentifiers:completion:]_block_invoke
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.285
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.277.cold.1
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.280
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.281
- ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.63
- ___block_descriptor_32_e41_"EDSearchableIndexItem"16?0"NSString"8l
- ___block_descriptor_56_ea8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48s56r_e33_v32?0"CSSearchableItem"8Q16^B24lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_ea8_32s40s48s56s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.261
- ___block_literal_global.324
- ___block_literal_global.342
- ___block_literal_global.367
- ___block_literal_global.415
- ___block_literal_global.463
- ___block_literal_global.51
- ___block_literal_global.68
- ___block_literal_global.786
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _objc_msgSend$initWithIndexedItems:
- _objc_msgSend$localSearchDidFindMessages:itemSnippetData:
- _objc_msgSend$observerDidFinishInitialLoad:
- _objc_msgSend$queryHelperDidFindAllMessages:
CStrings:
+ "%p: Failed initial load"
+ "%p: Failed initial load\n%{public}@"
+ "%p: Failed live query %{public}@"
+ "%p: ID %{public}@ failed initial load."
+ "%p: Returning local search info %{public}@"
+ "@\"EDLocalSearchInfoCollector\""
+ "@\"EMMessageObjectID\""
+ "@\"EMMessageObjectID\"16@?0@\"_EDMessageQueryHelperEntry\"8"
+ "@\"NSNumber\"16@?0@\"EDIndexedAttachment\"8"
+ "DELETE FROM searchable_rich_links WHERE rich_link = ? AND message_id = ?"
+ "EDLocalSearchInfoCollector"
+ "Failed to delete items in searchable_rich_links"
+ "Spotlight live search hasQueryEmbedding: %{BOOL}d for query %{public}@"
+ "Spotlight top hits and instant answers search hasQueryEmbedding: %{BOOL}d for query %{public}@"
+ "T@\"EDLocalSearchInfoCollector\",&,N,V_localSearchInfoCollector"
+ "T@\"EMMessageObjectID\",R,N,V_messageObjectID"
+ "T@\"NSMutableDictionary\",C,N,V_allRankingsByObjectID"
+ "T@\"NSMutableDictionary\",C,N,V_rankingObjectIDsByConversation"
+ "TB,N,V_hasEmbeddingResults"
+ "TB,N,V_hasKeywordResults"
+ "TB,N,V_hasLiveSearchQueryEmbedding"
+ "TB,N,V_hasTopHitsQueryEmbedding"
+ "Ti,N,V_liveSearchQueryStatus"
+ "Ti,N,V_topHitsQueryStatus"
+ "_allRankingsByObjectID"
+ "_combinedHasQueryEmbedding"
+ "_combinedQueryStatus"
+ "_extraInfoFromLocalSearchInfoCollector:"
+ "_hasEmbeddingResults"
+ "_hasKeywordResults"
+ "_hasLiveSearchQueryEmbedding"
+ "_hasTopHitsQueryEmbedding"
+ "_liveSearchQueryStatus"
+ "_localSearchInfoCollector"
+ "_messageObjectID"
+ "_rankingObjectIDsByConversation"
+ "_topHitsQueryStatus"
+ "allMessageObjectIDs"
+ "allRankingsByObjectID"
+ "ef_setOptionalObject:forKey:"
+ "em_mailRankingSignals"
+ "hasEmbeddingResults"
+ "hasKeywordResults"
+ "hasLiveSearchQueryEmbedding"
+ "hasTopHitsQueryEmbedding"
+ "initWithIdentifiers:"
+ "initWithIndexableItems:"
+ "initWithIndexableItems:removedIdentifiers:removedDomainIdentifiers:"
+ "initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:rankingSignalsByObjectID:"
+ "isSemanticMatch"
+ "isSyntacticMatch"
+ "liveSearchQueryStatus"
+ "localSearchDidFail"
+ "localSearchDidFindMessages:itemSnippetData:rankingSignals:"
+ "localSearchDidFinishTopHitsQuery:"
+ "localSearchDidHaveQueryEmbedding:"
+ "localSearchDidHaveTopHitsQueryEmbedding:"
+ "localSearchInfoCollector"
+ "localSearchInfoForConversationIDs:"
+ "localSearchInfoForMessageObjectIDs:"
+ "messageObjectID"
+ "observerDidFailInitialLoad:extraInfo:"
+ "observerDidFinishInitialLoad:extraInfo:"
+ "processRankingSignalsBySearchableItemID:forMessages:"
+ "queryHelperDidFailInitialLoad:localSearchInfoCollector:"
+ "queryHelperDidFindAllMessages:localSearchInfoCollector:"
+ "rankingObjectIDsByConversation"
+ "setAllRankingsByObjectID:"
+ "setEmbeddingBlock:"
+ "setEmbeddingHandler:"
+ "setHasEmbeddingResults:"
+ "setHasKeywordResults:"
+ "setHasLiveSearchQueryEmbedding:"
+ "setHasTopHitsQueryEmbedding:"
+ "setLiveSearchQueryStatus:"
+ "setLocalSearchInfoCollector:"
+ "setRankingObjectIDsByConversation:"
+ "setTopHitsQueryStatus:"
+ "topHitsQueryStatus"
+ "v32@0:8@\"EDMessageQueryHelper\"16@\"EDLocalSearchInfoCollector\"24"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSDictionary\"32"
- "@\"EDSearchableIndexItem\"16@?0@\"NSString\"8"
- "Failed to delete messages for items in searchable_rich_links"
- "initWithIndexedItems:"
- "localSearchDidFindMessages:itemSnippetData:"
- "observerDidFinishInitialLoad:"
- "queryHelperDidFindAllMessages:"

```
