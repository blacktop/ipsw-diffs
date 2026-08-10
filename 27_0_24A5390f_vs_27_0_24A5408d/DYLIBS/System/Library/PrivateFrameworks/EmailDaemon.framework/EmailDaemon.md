## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3897.100.8.2.5
-  __TEXT.__text: 0x28d200
-  __TEXT.__objc_methlist: 0x133dc
-  __TEXT.__const: 0x522c
-  __TEXT.__gcc_except_tab: 0x4a340
-  __TEXT.__cstring: 0x28eaa
-  __TEXT.__oslogstring: 0x1b12f
+3901.100.1.2.7
+  __TEXT.__text: 0x290f84
+  __TEXT.__objc_methlist: 0x133f4
+  __TEXT.__const: 0x524c
+  __TEXT.__gcc_except_tab: 0x4a5dc
+  __TEXT.__cstring: 0x28fca
+  __TEXT.__oslogstring: 0x1b3bf
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x26
-  __TEXT.__constg_swiftt: 0x10d0
-  __TEXT.__swift5_typeref: 0x17db
+  __TEXT.__constg_swiftt: 0x10ec
+  __TEXT.__swift5_typeref: 0x182f
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_reflstr: 0x10df
-  __TEXT.__swift5_fieldmd: 0x1654
+  __TEXT.__swift5_fieldmd: 0x1664
   __TEXT.__swift5_assocty: 0x248
   __TEXT.__swift5_proto: 0x39c
-  __TEXT.__swift5_types: 0x1d4
-  __TEXT.__swift5_capture: 0x7fc
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift5_capture: 0x810
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x11170
+  __TEXT.__unwind_info: 0x11210
   __TEXT.__eh_frame: 0x16b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x94b8
+  __DATA_CONST.__const: 0x94e0
   __DATA_CONST.__objc_classlist: 0x9e0
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x428
+  __DATA_CONST.__objc_protolist: 0x430
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb128
-  __DATA_CONST.__objc_protorefs: 0x120
+  __DATA_CONST.__objc_selrefs: 0xb130
+  __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __DATA_CONST.__got: 0x1e50
-  __AUTH_CONST.__const: 0x76fb
+  __DATA_CONST.__got: 0x1e70
+  __AUTH_CONST.__const: 0x77fb
   __AUTH_CONST.__cfstring: 0xfce0
-  __AUTH_CONST.__objc_const: 0x226a8
+  __AUTH_CONST.__objc_const: 0x22648
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x17f8
+  __AUTH_CONST.__auth_got: 0x1818
   __AUTH.__objc_data: 0xb98
   __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x1484
-  __DATA.__data: 0x39a0
+  __DATA.__objc_ivar: 0x147c
+  __DATA.__data: 0x39c0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x67c0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x5c78
-  __DATA_DIRTY.__data: 0x1b10
-  __DATA_DIRTY.__bss: 0x1b60
+  __DATA_DIRTY.__data: 0x1b00
+  __DATA_DIRTY.__bss: 0x1b80
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11529
-  Symbols:   19984
-  CStrings:  5469
+  Functions: 11564
+  Symbols:   20005
+  CStrings:  5480
 
Symbols:
+ +[EDMessagePersistence paginationBoundaryHasAlreadyDeliveredRowWithDatabaseID:sortDate:cursorBoundaryDatabaseID:cursorSortDate:]
+ +[EDServer signpostLog]
+ -[EDLocalSearchInfoCollector processResultMetadataBySearchableItemID:forMessages:]
+ -[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]
+ -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:resultMetadata:]
+ -[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:]
+ -[EDMessageRepository loadOlderItemsForObservationIdentifier:mailboxesToLoad:]
+ -[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:]
+ -[EDServer signpostID]
+ -[EDThreadPersistence _invalidateAllCachedSizeDecisions]
+ -[EDThreadPersistence _invalidateCachedMigratableSizeDecisions]
+ -[EDThreadPersistence _threadScopeIsTooLargeToMigrate:]
+ -[EDThreadPersistence persistenceIsChangingCategorizationForMessages:generationWindow:]
+ -[_EDInMemoryThreadState _minSearchRelevanceRank]
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table311
+ GCC_except_table323
+ GCC_except_table336
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table348
+ _OBJC_CLASS_$_EMSearchResultMetadata
+ _OBJC_CLASS_$_EMServerConfiguration
+ _OBJC_IVAR_$_EDThreadPersistence._tooLargeToMigrateDecisionCache
+ _OBJC_IVAR_$_EDThreadPersistence._tooLargeToMigrateDecisionCacheGeneration
+ ___23+[EDServer signpostLog]_block_invoke
+ ___49-[_EDInMemoryThreadState _minSearchRelevanceRank]_block_invoke
+ ___70-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]_block_invoke
+ ___70-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]_block_invoke_2
+ ___78-[EDMessageRepository loadOlderItemsForObservationIdentifier:mailboxesToLoad:]_block_invoke
+ ___82-[EDLocalSearchInfoCollector processResultMetadataBySearchableItemID:forMessages:]_block_invoke
+ ___82-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:resultMetadata:]_block_invoke
+ ___86-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:]_block_invoke
+ ___87-[EDThreadPersistence persistenceIsChangingCategorizationForMessages:generationWindow:]_block_invoke
+ ___95-[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:]_block_invoke
+ ___block_descriptor_56_ea8_32s40bs48r_e17_v16?0"NSArray"8ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e25_v32?0"NSString"816^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_ea8_32s40bs48r56r_e34_v32?0q8"EMMessage"16"NSError"24ls40l8s32l8r48l8r56l8
+ ___block_descriptor_64_ea8_32s40s48bs56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_80_ea8_32s40s48bs56r64r72r_e34_v32?0q8"EMMessage"16"NSError"24ls48l8s32l8r56l8r64l8s40l8r72l8
+ ___block_descriptor_89_ea8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ _flat unique So9EDAccount_p
+ _objc_msgSend$_invalidateAllCachedSizeDecisions
+ _objc_msgSend$_invalidateCachedMigratableSizeDecisions
+ _objc_msgSend$_minSearchRelevanceRank
+ _objc_msgSend$_threadScopeIsTooLargeToMigrate:
+ _objc_msgSend$countOfMessagesInMailboxDatabaseIDs:upToLimit:
+ _objc_msgSend$defaultPolicyForIMAPHost:
+ _objc_msgSend$getValueForKey:
+ _objc_msgSend$initWithRankingSignals:rankPosition:
+ _objc_msgSend$loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:
+ _objc_msgSend$localSearchDidFindMessages:itemSnippetData:resultMetadata:
+ _objc_msgSend$localSearchDidFindTopHits:itemSnippetData:resultMetadata:instantAnswer:
+ _objc_msgSend$paginationBoundaryHasAlreadyDeliveredRowWithDatabaseID:sortDate:cursorBoundaryDatabaseID:cursorSortDate:
+ _objc_msgSend$processResultMetadataBySearchableItemID:forMessages:
+ _objc_msgSend$rankPosition
+ _objc_msgSend$rankingSignals
+ _objc_msgSend$shouldCancel
+ _symbolic SDySSypG
+ _symbolic SS3key_yp5valuet
+ _symbolic _____ So31EDSearchableIndexDownloadPolicyC11EmailDaemonE05DailyC5LimitO
+ _symbolic ______p So9EDAccountP
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
- -[EDBatchingMessageQueryIterator cursorBoundaryDatabaseID]
- -[EDBatchingMessageQueryIterator cursorBoundarySortAscending]
- -[EDBatchingMessageQueryIterator lastEmittedDatabaseID]
- -[EDBatchingMessageQueryIterator rawRowsReceived]
- -[EDBatchingMessageQueryIterator setCursorBoundaryDatabaseID:]
- -[EDBatchingMessageQueryIterator setCursorBoundarySortAscending:]
- -[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]
- -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]
- -[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]
- -[EDMessageRepository loadOlderItemsForObservationIdentifier:]
- -[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:]
- -[EDThreadPersistence persistenceIsChangingCategorizationForMessages:userInitiated:generationWindow:]
- -[_EDInMemoryThreadState _maxSearchRelevanceScore]
- GCC_except_table186
- GCC_except_table300
- GCC_except_table302
- GCC_except_table315
- GCC_except_table327
- GCC_except_table340
- _OBJC_IVAR_$_EDBatchingMessageQueryIterator._cursorBoundaryDatabaseID
- _OBJC_IVAR_$_EDBatchingMessageQueryIterator._cursorBoundarySortAscending
- _OBJC_IVAR_$_EDBatchingMessageQueryIterator._lastEmittedDatabaseID
- _OBJC_IVAR_$_EDBatchingMessageQueryIterator._rawRowsReceived
- ___101-[EDThreadPersistence persistenceIsChangingCategorizationForMessages:userInitiated:generationWindow:]_block_invoke
- ___50-[_EDInMemoryThreadState _maxSearchRelevanceScore]_block_invoke
- ___62-[EDMessageRepository loadOlderItemsForObservationIdentifier:]_block_invoke
- ___82-[EDLocalSearchInfoCollector processRankingSignalsBySearchableItemID:forMessages:]_block_invoke
- ___82-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:rankingSignals:]_block_invoke
- ___95-[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]_block_invoke
- ___97-[EDPaginationCursor loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:]_block_invoke
- ___block_descriptor_40_ea8_32s_e20_v24?0"NSArray"8q16ls32l8
- ___block_descriptor_48_ea8_32s40bs_e34_v32?0q8"EMMessage"16"NSError"24ls40l8s32l8
- ___block_descriptor_48_ea8_32s40r_e20_v24?0"NSArray"8q16ls32l8r40l8
- ___block_descriptor_56_ea8_32s40s48r_e25_v32?0"NSString"816^B24ls32l8r48l8s40l8
- ___block_descriptor_97_ea8_32s40s48s56s64bs72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$_maxSearchRelevanceScore
- _objc_msgSend$l1Score
- _objc_msgSend$l2Score
- _objc_msgSend$lastEmittedDatabaseID
- _objc_msgSend$loadMoreWithQuery:sortAscending:cancelationToken:messageHandler:completion:
- _objc_msgSend$localSearchDidFindMessages:itemSnippetData:rankingSignals:
- _objc_msgSend$localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:
- _objc_msgSend$processRankingSignalsBySearchableItemID:forMessages:
- _objc_msgSend$rawRowsReceived
- _objc_msgSend$setCursorBoundaryDatabaseID:
- _objc_msgSend$setCursorBoundarySortAscending:
CStrings:
+ "-[EDMessagePersistence countOfMessagesInMailboxDatabaseIDs:upToLimit:]"
+ "Data source updates were canceled (watchdog fired, no items returned); deferring background-scheduled indexing run to a later retry instead of re-arming immediately."
+ "Data source updates were canceled (watchdog fired, no items returned, no caller waiting); skipping re-arm and waiting for the next natural trigger (new mail, unlock, plug-in, background-scheduled activity)."
+ "EDServerListenerResumed"
+ "EMInternalPreferenceIndexerDailyDownloadLimitOverride"
+ "Resolved per-host policy for account %{public}s host=%{public}s quota=%{public}s"
+ "Sending backfillDailyStatus event: %{public}s"
+ "Thread-scope migration size check: mailbox membership %ld (cap %ld, tooLarge=%d) in %.3fs for %{public}@"
+ "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT accountId,       messageId,       NULL AS senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       hadFirstReadWithBlackPearlEnabled,       hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
+ "configuration_matchedHost"
+ "configuration_resolvedQuotaBytes"
+ "indexer-daily-download-limit-bytes"
+ "indexer-daily-download-limit-bytes-per-host"
- "WITH receive_row_num AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesCategoriesEnabled AS isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountCategoriesEnabled AS isMailAccountBlackPearlEnabled,           CASE WHEN receiveTimestamp >= %llu                     THEN TRUE                ELSE FALSE                END AS isL1,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY eventTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Receive\"    WHERE receiveTimestamp >= %llu          AND receiveTimestamp < %llu          AND accountId IN (%@) ),receive AS (    SELECT accountId,           messageId,           senderId,           receivingAccountDomain,           metadataPrimaryKey,           predictedCategory,           currCategoryView,           reasonCodes,           isAllInboxesBlackPearlEnabled,           isMailAccountPersonalAccount,           isMailAccountBlackPearlEnabled,           isL1    FROM receive_row_num    WHERE rn = 1),read_row_num AS (    SELECT accountId,           messageId,           readTimestamp,           readWithCategoriesEnabled,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY readTimestamp ASC) AS rn    FROM \"Mail.CategorizationAnalytics.Read\"),read AS (    SELECT accountId,           messageId,           readTimestamp AS firstReadTimestamp,           readWithCategoriesEnabled AS hadFirstReadWithBlackPearlEnabled    FROM read_row_num    WHERE rn = 1),recategorize_row_num AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp,           ROW_NUMBER() OVER (PARTITION BY accountId, messageId ORDER BY recategorizeTimestamp DESC) AS rn    FROM \"Mail.CategorizationAnalytics.Recategorize\"),recategorize AS (    SELECT accountId,           messageId,           currCategoryView,           recategorizationBy,           recategorizeTimestamp AS lastRecategorizeTimestamp    FROM recategorize_row_num    WHERE rn = 1),flattened AS (    SELECT receive.accountId,           receive.messageId,           receive.senderId,           receive.receivingAccountDomain,           receive.metadataPrimaryKey,           receive.isAllInboxesBlackPearlEnabled,           receive.isMailAccountPersonalAccount,           receive.isMailAccountBlackPearlEnabled,           receive.predictedCategory,           COALESCE(recategorize.currCategoryView, receive.currCategoryView) AS currCategoryView,           read.hadFirstReadWithBlackPearlEnabled,           CASE                 WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN TRUE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                     THEN FALSE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp < recategorize.lastRecategorizeTimestamp                     THEN TRUE                WHEN read.firstReadTimestamp IS NOT NULL                         AND recategorize.lastRecategorizeTimestamp IS NOT NULL                         AND read.firstReadTimestamp >= recategorize.lastRecategorizeTimestamp                     THEN FALSE                WHEN read.firstReadTimestamp IS NULL                         AND recategorize.lastRecategorizeTimestamp IS NULL                     THEN False                ELSE NULL                END AS hadReadBeforeRecat,           receive.reasonCodes,           recategorize.recategorizationBy,           receive.isL1,           ROW_NUMBER() OVER (ORDER BY RANDOM()) AS rn    FROM receive         LEFT JOIN read                 ON receive.accountId = read.accountId                    AND receive.messageId = read.messageId         LEFT JOIN recategorize                 ON receive.accountId = recategorize.accountId                    AND receive.messageId = recategorize.messageId), sampled_msg_cnt AS (    SELECT MIN(500, (ABS(RANDOM()) %% (COUNT(*) - FLOOR(0.9 * COUNT(*)) + 1)) + FLOOR(0.9 * COUNT(*))) AS max_rn    FROM flattened) SELECT accountId,       messageId,       senderId,       receivingAccountDomain,       metadataPrimaryKey,       isAllInboxesBlackPearlEnabled,       isMailAccountPersonalAccount,       isMailAccountBlackPearlEnabled,       predictedCategory,       currCategoryView,       hadFirstReadWithBlackPearlEnabled,       hadReadBeforeRecat,       reasonCodes,       recategorizationBy,       isL1 FROM flattened      JOIN sampled_msg_cnt           ON 1=1 WHERE rn <= max_rn;"
- "v24@?0@\"NSArray\"8q16"
```
