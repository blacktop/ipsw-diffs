## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon`

```diff

-3826.500.181.1.5
-  __TEXT.__text: 0x299950
+3826.600.15.1.1
+  __TEXT.__text: 0x29a64c
   __TEXT.__auth_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x15c44
+  __TEXT.__objc_methlist: 0x15c6c
   __TEXT.__const: 0x1e08
-  __TEXT.__gcc_except_tab: 0x4c810
-  __TEXT.__cstring: 0x21227
-  __TEXT.__oslogstring: 0x18e06
+  __TEXT.__gcc_except_tab: 0x4c9cc
+  __TEXT.__cstring: 0x213e7
+  __TEXT.__oslogstring: 0x18eb6
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x92b

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x108e8
+  __TEXT.__unwind_info: 0x10940
   __TEXT.__eh_frame: 0xc40
   __TEXT.__objc_classname: 0x2ed9
-  __TEXT.__objc_methname: 0x39c13
-  __TEXT.__objc_methtype: 0x8686
-  __TEXT.__objc_stubs: 0x25080
-  __DATA_CONST.__got: 0x1af0
-  __DATA_CONST.__const: 0x1f48
+  __TEXT.__objc_methname: 0x39d06
+  __TEXT.__objc_methtype: 0x869d
+  __TEXT.__objc_stubs: 0x25120
+  __DATA_CONST.__got: 0x1b00
+  __DATA_CONST.__const: 0x1f50
   __DATA_CONST.__objc_classlist: 0x9a8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba28
+  __DATA_CONST.__objc_selrefs: 0xba30
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x5b8
   __AUTH_CONST.__auth_got: 0x1290
   __AUTH_CONST.__auth_ptr: 0x2e8
-  __AUTH_CONST.__const: 0xbf98
-  __AUTH_CONST.__cfstring: 0x10e80
-  __AUTH_CONST.__objc_const: 0x24e98
-  __AUTH_CONST.__objc_intobj: 0x8b8
+  __AUTH_CONST.__const: 0xbfc8
+  __AUTH_CONST.__cfstring: 0x10f80
+  __AUTH_CONST.__objc_const: 0x24ef8
+  __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x3448
   __AUTH.__data: 0xc50
-  __DATA.__objc_ivar: 0x16ec
+  __DATA.__objc_ivar: 0x16f4
   __DATA.__data: 0x3680
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x30e0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10864
-  Symbols:   26641
-  CStrings:  14556
+  Functions: 10870
+  Symbols:   26664
+  CStrings:  14574
 
Symbols:
+ -[EDPersistenceDatabaseConnection messagesWithUnindexedBodiesAfterID:limit:]
+ -[EDSearchableIndex _sendAnalyticsForRedonatingItems:]
+ -[EDSearchableIndex performMaintenancePreWork]
+ -[EDSearchableIndexDiagnosticsSnapshot initWithDate:indexableMessages:messagesIndexed:messagesToRedonate:turboMode:]
+ -[EDSearchableIndexDiagnosticsSnapshot messagesToRedonate]
+ -[EDSearchableIndexPersistence assignIndexingType:forIdentifiers:]
+ -[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]
+ GCC_except_table266
+ OBJC_IVAR_$_EDSearchableIndex._redonatedItems
+ OBJC_IVAR_$_EDSearchableIndexDiagnosticsSnapshot._messagesToRedonate
+ _EDSearchableIndexDiagnosticsSnapshotKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyRemoteMessagesToRedonate
+ __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.416
+ __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.420
+ __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.424
+ __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.425
+ __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.426
+ __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.219
+ __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.223
+ __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.227
+ __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.228
+ __46-[EDSearchableIndexScheduler _startScheduling]_block_invoke.52
+ __46-[EDSearchableIndexScheduler _startScheduling]_block_invoke.52.cold.1
+ __52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.396
+ __57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.405
+ __59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.414
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.321
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.322
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.334
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.336
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.337
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.341
+ __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.323
+ __61-[EDSearchableIndexScheduler _beginIndexingForTaskType:task:]_block_invoke.62
+ __64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.399
+ __66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.400
+ __66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.400.cold.1
+ __68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.420
+ __71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.373
+ __71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.373.cold.1
+ __75-[EDSearchableIndexPersistence _assignIndexedItems:transaction:connection:]_block_invoke.502
+ __79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.303
+ __79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.304
+ __81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.185
+ __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.293.cold.1
+ __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.296
+ __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.297
+ __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.299
+ __86-[EDSearchableIndexPersistence _richLinkItemsFromRichLinkData:limit:cancelationToken:]_block_invoke.522
+ __86-[EDSearchableIndexPersistence _richLinkItemsFromRichLinkData:limit:cancelationToken:]_block_invoke.535
+ __90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke.512
+ ___106-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) messagesWithUnindexedBodiesAfterID:limit:]_block_invoke
+ ___46-[EDSearchableIndex performMaintenancePreWork]_block_invoke
+ ___54-[EDSearchableIndex _sendAnalyticsForRedonatingItems:]_block_invoke
+ ___66-[EDSearchableIndexPersistence assignIndexingType:forIdentifiers:]_block_invoke
+ ___87-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]_block_invoke
+ ___block_descriptor_40_ea8_32s_e21_B16?0"<EDAccount>"8l
+ ___block_descriptor_56_ea8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8l
+ __block_literal_global.195
+ __block_literal_global.200
+ __block_literal_global.362
+ __block_literal_global.417
+ __block_literal_global.431
+ __block_literal_global.433
+ __block_literal_global.478
+ __block_literal_global.843
+ _objc_msgSend$_sendAnalyticsForRedonatingItems:
+ _objc_msgSend$initWithDate:indexableMessages:messagesIndexed:messagesToRedonate:turboMode:
+ _objc_msgSend$isMessageContentLocallyAvailable
+ _objc_msgSend$messagesToRedonate
+ _objc_msgSend$performMaintenancePreWork
+ _objc_msgSend$queueRedonationForDownloadedMessagesWithUnindexedBodies
+ _objc_msgSend$requireClassA
+ _objc_msgSend$tokenWithLabel:invocationBlock:
- -[EDSearchableIndexDiagnosticsSnapshot initWithDate:indexableMessages:messagesIndexed:turboMode:]
- -[EDSearchableIndexDiagnosticsSnapshot setDate:]
- -[EDSearchableIndexDiagnosticsSnapshot setIndexableMessages:]
- -[EDSearchableIndexDiagnosticsSnapshot setMessagesIndexed:]
- -[EDSearchableIndexDiagnosticsSnapshot setTurboMode:]
- _OBJC_CLASS_$_EFProcessBoost
- __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.397
- __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.401
- __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.405
- __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.406
- __107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.407
- __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.213
- __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.217
- __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.221
- __42-[EDSearchableIndex _fetchLastClientState]_block_invoke.222
- __46-[EDSearchableIndexScheduler _startScheduling]_block_invoke.49
- __46-[EDSearchableIndexScheduler _startScheduling]_block_invoke.49.cold.1
- __52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.390
- __57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.399
- __59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.408
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.315
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.316
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.325
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.328
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.330
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.335
- __61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.317
- __61-[EDSearchableIndexScheduler _beginIndexingForTaskType:task:]_block_invoke.59
- __64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.393
- __66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.394
- __66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.394.cold.1
- __68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.414
- __71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.367
- __71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.367.cold.1
- __75-[EDSearchableIndexPersistence _assignIndexedItems:transaction:connection:]_block_invoke.482
- __79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.297
- __79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.298
- __81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.179
- __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.287
- __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.287.cold.1
- __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.290
- __84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.291
- __86-[EDSearchableIndexPersistence _richLinkItemsFromRichLinkData:limit:cancelationToken:]_block_invoke.502
- __86-[EDSearchableIndexPersistence _richLinkItemsFromRichLinkData:limit:cancelationToken:]_block_invoke.515
- __90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke.492
- ___82-[EDSearchableIndexPersistence searchableIndex:assignIndexingType:forIdentifiers:]_block_invoke
- ___block_descriptor_48_ea8_32s40s_e21_B16?0"<EDAccount>"8l
- __block_literal_global.189
- __block_literal_global.194
- __block_literal_global.269
- __block_literal_global.356
- __block_literal_global.384
- __block_literal_global.411
- __block_literal_global.425
- __block_literal_global.427
- __block_literal_global.457
- __block_literal_global.833
- _objc_msgSend$drop
- _objc_msgSend$initWithBoost:
- _objc_msgSend$initWithDate:indexableMessages:messagesIndexed:turboMode:
CStrings:
+ "\x055\x11\x11!#!"
+ "   SELECT message_id     FROM searchable_messages    WHERE transaction_id > :transaction      AND message_id > :after_id      AND NOT message_body_indexed ORDER BY message_id ASC    LIMIT :limit"
+ "-[EDSearchableIndexPersistence assignIndexingType:forIdentifiers:]"
+ "-[EDSearchableIndexPersistence queueRedonationForDownloadedMessagesWithUnindexedBodies]"
+ ":after_id"
+ ":transaction"
+ "@52@0:8@16@24@32@40B48"
+ "Could not load unindexed bodies from searchable_messages table"
+ "EDClientState-%p"
+ "EDSearchableIndexPersistenceUnindexedBodies"
+ "Found %@ messages with unindexed bodies in %0.2f seconds. %@ are available locally."
+ "MessagesToRedonate"
+ "T@\"NSDate\",R,N,V_date"
+ "T@\"NSNumber\",R,N,V_indexableMessages"
+ "T@\"NSNumber\",R,N,V_messagesIndexed"
+ "T@\"NSNumber\",R,N,V_messagesToRedonate"
+ "TB,R,N,V_turboMode"
+ "_messagesToRedonate"
+ "_redonatedItems"
+ "_sendAnalyticsForRedonatingItems:"
+ "assignIndexingType:forIdentifiers:"
+ "com.apple.mail.searchableIndex.redonateItems"
+ "duration: %g, unindexed: %llu , available: %llu"
+ "initWithDate:indexableMessages:messagesIndexed:messagesToRedonate:turboMode:"
+ "itemCount"
+ "messagesToRedonate"
+ "performMaintenancePreWork"
+ "queueRedonationForDownloadedMessagesWithUnindexedBodies"
+ "tokenWithLabel:invocationBlock:"
+ "\xf0R"
- "\x055\x11\x11\x11#!"
- "-[EDSearchableIndexPersistence searchableIndex:assignIndexingType:forIdentifiers:]"
- "T@\"NSNumber\",&,N,V_indexableMessages"
- "T@\"NSNumber\",&,N,V_messagesIndexed"
- "TB,N,V_turboMode"
- "drop"
- "initWithBoost:"
- "initWithDate:indexableMessages:messagesIndexed:turboMode:"
- "setIndexableMessages:"
- "setMessagesIndexed:"
- "setTurboMode:"
- "\xf0B"

```
