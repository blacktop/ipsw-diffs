## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon`

```diff

-3897.100.8.1.1
-  __TEXT.__text: 0x2bb378
-  __TEXT.__objc_methlist: 0x13594
-  __TEXT.__const: 0x519c
-  __TEXT.__gcc_except_tab: 0x4ab14
-  __TEXT.__cstring: 0x2839a
-  __TEXT.__oslogstring: 0x1af0f
+3901.100.1.1.11
+  __TEXT.__text: 0x2be48c
+  __TEXT.__objc_methlist: 0x1359c
+  __TEXT.__const: 0x51fc
+  __TEXT.__gcc_except_tab: 0x4acd0
+  __TEXT.__cstring: 0x2849a
+  __TEXT.__oslogstring: 0x1b1bf
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x26
-  __TEXT.__constg_swiftt: 0x108c
-  __TEXT.__swift5_typeref: 0x1759
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x10bf
-  __TEXT.__swift5_fieldmd: 0x1628
+  __TEXT.__constg_swiftt: 0x10c8
+  __TEXT.__swift5_typeref: 0x17fb
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_reflstr: 0x10df
+  __TEXT.__swift5_fieldmd: 0x1654
   __TEXT.__swift5_assocty: 0x248
   __TEXT.__swift5_proto: 0x398
-  __TEXT.__swift5_types: 0x1cc
-  __TEXT.__swift5_capture: 0x704
+  __TEXT.__swift5_types: 0x1d4
+  __TEXT.__swift5_capture: 0x7d0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x110d8
+  __TEXT.__unwind_info: 0x11168
   __TEXT.__eh_frame: 0x1590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x428
+  __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb208
-  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x5e0
   __DATA_CONST.__objc_arraydata: 0x5f0
-  __DATA_CONST.__got: 0x1e00
-  __AUTH_CONST.__const: 0xfc03
-  __AUTH_CONST.__cfstring: 0xf920
-  __AUTH_CONST.__objc_const: 0x229f8
+  __DATA_CONST.__got: 0x1e20
+  __AUTH_CONST.__const: 0xff23
+  __AUTH_CONST.__cfstring: 0xf960
+  __AUTH_CONST.__objc_const: 0x22988
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1640
+  __AUTH_CONST.__auth_got: 0x1658
   __AUTH.__objc_data: 0xbe8
   __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x14ac
-  __DATA.__data: 0x39b0
+  __DATA.__objc_ivar: 0x14a0
+  __DATA.__data: 0x39f0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x66c0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x5c78
-  __DATA_DIRTY.__data: 0x1a48
-  __DATA_DIRTY.__bss: 0x1be0
+  __DATA_DIRTY.__data: 0x1a58
+  __DATA_DIRTY.__bss: 0x1bf0
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11594
-  Symbols:   20344
-  CStrings:  5431
+  Functions: 11649
+  Symbols:   20367
+  CStrings:  5442
 
Symbols:
+ +[EDMessagePersistence paginationBoundaryHasAlreadyDeliveredRowWithDatabaseID:sortDate:cursorBoundaryDatabaseID:cursorSortDate:]
+ +[EDServer signpostLog]
+ -[EDLocalSearchInfoCollector processResultMetadataBySearchableItemID:forMessages:]
+ -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:resultMetadata:]
+ -[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:]
+ -[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:]
+ -[EDPersistence lastSpotlightReportDate]
+ -[EDPersistence setLastSpotlightReportDate:]
+ -[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodiesWithCancelationToken:]
+ -[EDServer signpostID]
+ -[EDThreadPersistence _threadScopeIsTooLargeToMigrate:]
+ -[EDThreadPersistence persistenceIsChangingCategorizationForMessages:generationWindow:]
+ -[_EDInMemoryThreadState _minSearchRelevanceRank]
+ GCC_except_table223
+ GCC_except_table306
+ GCC_except_table343
+ GCC_except_table347
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table374
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table385
+ OBJC_IVAR_$_EDPersistence._lastSpotlightReportDate
+ _OBJC_CLASS_$_EMSearchResultMetadata
+ _OBJC_CLASS_$_EMServerConfiguration
+ __86-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:]_block_invoke
+ ___108-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodiesWithCancelationToken:]_block_invoke
+ ___23+[EDServer signpostLog]_block_invoke
+ ___49-[_EDInMemoryThreadState _minSearchRelevanceRank]_block_invoke
+ ___82-[EDLocalSearchInfoCollector processResultMetadataBySearchableItemID:forMessages:]_block_invoke
+ ___82-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:resultMetadata:]_block_invoke
+ ___86-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:]_block_invoke
+ ___87-[EDThreadPersistence persistenceIsChangingCategorizationForMessages:generationWindow:]_block_invoke
+ ___95-[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:]_block_invoke
+ ___block_descriptor_56_ea8_32s40bs48r_e17_v16?0"NSArray"8l
+ ___block_descriptor_64_ea8_32s40bs48r56r_e34_v32?0q8"EMMessage"16"NSError"24l
+ ___block_descriptor_64_ea8_32s40s48bs56r_e5_v8?0l
+ ___block_descriptor_80_ea8_32s40s48bs56r64r72r_e34_v32?0q8"EMMessage"16"NSError"24l
+ ___block_descriptor_89_ea8_32s40s48s56s64bs_e5_v8?0l
+ ___copy_helper_block_ea8_32s40b48r56r
+ ___copy_helper_block_ea8_32s40s48b56r64r72r
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy4_4
+ __swift_closure_destructor.25Tm
+ __swift_closure_destructor.44Tm
+ _flat unique So12EFCancelable_p
+ _flat unique So9EDAccount_p
+ _objc_msgSend$_minSearchRelevanceRank
+ _objc_msgSend$_threadScopeIsTooLargeToMigrate:
+ _objc_msgSend$defaultPolicyForIMAPHost:
+ _objc_msgSend$getValueForKey:
+ _objc_msgSend$initWithRankingSignals:rankPosition:
+ _objc_msgSend$lastSpotlightReportDate
+ _objc_msgSend$loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:
+ _objc_msgSend$localSearchDidFindMessages:itemSnippetData:resultMetadata:
+ _objc_msgSend$localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:
+ _objc_msgSend$paginationBoundaryHasAlreadyDeliveredRowWithDatabaseID:sortDate:cursorBoundaryDatabaseID:cursorSortDate:
+ _objc_msgSend$processResultMetadataBySearchableItemID:forMessages:
+ _objc_msgSend$queueRedonationForDownloadedMessagesWithUnindexedBodiesWithCancelationToken:
+ _objc_msgSend$rankPosition
+ _objc_msgSend$rankingSignals
+ _objc_msgSend$setLastSpotlightReportDate:
+ _objc_msgSend$shouldCancel
+ _symbolic SbIegd_
+ _symbolic Sbz_Xx
+ _symbolic So26EDSearchableIndexTelemetryCSgXwz_Xx
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So31EDSearchableIndexDownloadPolicyC11EmailDaemonE05DailyC5LimitO
+ _symbolic ______p So12EFCancelableP
+ _symbolic ______p So9EDAccountP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _type_layout_string So16os_unfair_lock_sV
- -[EDBatchingMessageQueryIterator cursorBoundaryDatabaseID]
- -[EDBatchingMessageQueryIterator cursorBoundarySortAscending]
- -[EDBatchingMessageQueryIterator lastEmittedDatabaseID]
- -[EDBatchingMessageQueryIterator rawRowsReceived]
- -[EDBatchingMessageQueryIterator setCursorBoundaryDatabaseID:]
- -[EDBatchingMessageQueryIterator setCursorBoundarySortAscending:]
- -[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]
- -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]
- -[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]
- -[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:]
- -[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]
- -[EDThreadPersistence persistenceIsChangingCategorizationForMessages:userInitiated:generationWindow:]
- -[_EDInMemoryThreadState _maxSearchRelevanceScore]
- GCC_except_table230
- GCC_except_table231
- GCC_except_table240
- GCC_except_table309
- GCC_except_table327
- GCC_except_table346
- GCC_except_table350
- GCC_except_table362
- GCC_except_table369
- GCC_except_table370
- GCC_except_table377
- OBJC_IVAR_$_EDBatchingMessageQueryIterator._cursorBoundaryDatabaseID
- OBJC_IVAR_$_EDBatchingMessageQueryIterator._cursorBoundarySortAscending
- OBJC_IVAR_$_EDBatchingMessageQueryIterator._lastEmittedDatabaseID
- OBJC_IVAR_$_EDBatchingMessageQueryIterator._rawRowsReceived
- __97-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:]_block_invoke
- ___101-[EDThreadPersistence persistenceIsChangingCategorizationForMessages:userInitiated:generationWindow:]_block_invoke
- ___50-[_EDInMemoryThreadState _maxSearchRelevanceScore]_block_invoke
- ___82-[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]_block_invoke
- ___82-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]_block_invoke
- ___87-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]_block_invoke
- ___95-[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]_block_invoke
- ___97-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:]_block_invoke
- ___block_descriptor_40_ea8_32s_e20_v24?0"NSArray"8q16l
- ___block_descriptor_48_ea8_32s40bs_e34_v32?0q8"EMMessage"16"NSError"24l
- ___block_descriptor_48_ea8_32s40r_e20_v24?0"NSArray"8q16l
- ___block_descriptor_97_ea8_32s40s48s56s64bs72bs_e5_v8?0l
- ___copy_helper_block_ea8_32s40s48s56s64b72b
- _objc_msgSend$_maxSearchRelevanceScore
- _objc_msgSend$l1Score
- _objc_msgSend$l2Score
- _objc_msgSend$lastEmittedDatabaseID
- _objc_msgSend$loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:
- _objc_msgSend$localSearchDidFindMessages:itemSnippetData:rankingSignals:
- _objc_msgSend$localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:
- _objc_msgSend$processRankingSignalsBySearchableItemID:forMessages:
- _objc_msgSend$queueRedonationForDownloadedMessagesWithUnindexedBodies
- _objc_msgSend$rawRowsReceived
- _objc_msgSend$setCursorBoundaryDatabaseID:
- _objc_msgSend$setCursorBoundarySortAscending:
CStrings:
+ "-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodiesWithCancelationToken:]"
+ "Data source updates were canceled (watchdog fired, no items returned); deferring background-scheduled indexing run to a later retry instead of re-arming immediately."
+ "Data source updates were canceled (watchdog fired, no items returned, no caller waiting); skipping re-arm and waiting for the next natural trigger (new mail, unlock, plug-in, background-scheduled activity)."
+ "EDServerListenerResumed"
+ "EDThreadScopeMigrationSizeCheck"
+ "EMInternalPreferenceIndexerDailyDownloadLimitOverride"
+ "Expiring %{public}s task; deferring and asking maintenance work to stop"
+ "Sending backfillDailyStatus event: %{public}s"
+ "Skipping Spotlight progress report: on battery, last report %.0fs ago"
+ "Threadscope matches %ld messages (>= %ld); using in-memory threads instead of migrating: %{public}@"
+ "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT accountId,       messageId,       NULL AS senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       hadFirstReadWithBlackPearlEnabled,       hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
+ "com.apple.mail.searchableIndex.maintenanceCancelation"
+ "indexer-daily-download-limit-bytes"
+ "indexer-daily-download-limit-bytes-per-host"
- "-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]"
- "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT accountId,       messageId,       senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       hadFirstReadWithBlackPearlEnabled,       hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
- "v24@?0@\"NSArray\"8q16"
```
