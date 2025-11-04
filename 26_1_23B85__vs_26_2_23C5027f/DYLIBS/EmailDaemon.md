## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.200.81.2.5
-  __TEXT.__text: 0x26a424
+3864.300.11.2.1
+  __TEXT.__text: 0x26429c
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_methlist: 0x1329c
-  __TEXT.__const: 0x399c
-  __TEXT.__gcc_except_tab: 0x4f5bc
-  __TEXT.__cstring: 0x26f0a
-  __TEXT.__oslogstring: 0x1a6e4
+  __TEXT.__objc_methlist: 0x12ee4
+  __TEXT.__const: 0x398c
+  __TEXT.__gcc_except_tab: 0x4e828
+  __TEXT.__cstring: 0x2665a
+  __TEXT.__oslogstring: 0x1a084
   __TEXT.__dlopen_cstrs: 0x3bc
-  __TEXT.__ustring: 0x2c
+  __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0xb84
   __TEXT.__swift5_typeref: 0xdc7
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x10b88
+  __TEXT.__unwind_info: 0x107f0
   __TEXT.__eh_frame: 0xfb0
-  __TEXT.__objc_classname: 0x2c94
-  __TEXT.__objc_methname: 0x37ddf
-  __TEXT.__objc_methtype: 0x7a1d
-  __TEXT.__objc_stubs: 0x253c0
-  __DATA_CONST.__got: 0x1bc8
-  __DATA_CONST.__const: 0x95b0
-  __DATA_CONST.__objc_classlist: 0x940
+  __TEXT.__objc_classname: 0x2bfe
+  __TEXT.__objc_methname: 0x373f8
+  __TEXT.__objc_methtype: 0x7807
+  __TEXT.__objc_stubs: 0x24cc0
+  __DATA_CONST.__got: 0x1b90
+  __DATA_CONST.__const: 0x9340
+  __DATA_CONST.__objc_classlist: 0x928
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x400
+  __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb080
+  __DATA_CONST.__objc_selrefs: 0xaec0
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x5f8
+  __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x1398
-  __AUTH_CONST.__const: 0x5cd8
-  __AUTH_CONST.__cfstring: 0x10600
-  __AUTH_CONST.__objc_const: 0x219f0
+  __AUTH_CONST.__const: 0x5c78
+  __AUTH_CONST.__cfstring: 0x10160
+  __AUTH_CONST.__objc_const: 0x21390
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0xef0
   __AUTH.__data: 0x4f8
-  __DATA.__objc_ivar: 0x1490
-  __DATA.__data: 0x36b0
+  __DATA.__objc_ivar: 0x1458
+  __DATA.__data: 0x35e0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x4750
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x50b0
+  __DATA_DIRTY.__objc_data: 0x4fc0
   __DATA_DIRTY.__data: 0xc30
-  __DATA_DIRTY.__bss: 0x1640
+  __DATA_DIRTY.__bss: 0x1620
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 45081888-8671-36C5-89E6-C34BF0A4B4B3
-  Functions: 10776
-  Symbols:   34699
-  CStrings:  16435
+  UUID: B8C631E8-E63A-3E1B-AC31-42C3FDBCB460
+  Functions: 10657
+  Symbols:   34252
+  CStrings:  16230
 
Symbols:
+ -[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:]
+ -[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:].cold.1
+ -[EDMessageCategorizer _categorizeMessages:signpostID:results:cancelationToken:reason:]
+ -[EDMessageCategorizer categorizeMessages:cancelationToken:reason:]
+ -[EDMessageCountQueryHandler _adjustLocalCount:logMessage:generationWindow:]
+ -[EDMessageCountQueryHandler _hasStaleFlags:persistentMessages:]
+ ___104-[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:]_block_invoke
+ ___104-[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:]_block_invoke.cold.1
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.384
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.389
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.390
+ ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.391
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.179
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.184
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.188
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke_2.187
+ ___46-[EDMessageCountQueryHandler willSyncMailbox:]_block_invoke.94
+ ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.314
+ ___59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.317
+ ___60-[EDMessageCountQueryHandler _notifyObserverWithLogMessage:]_block_invoke.87
+ ___60-[EDMessageCountQueryHandler _notifyObserverWithLogMessage:]_block_invoke.92
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.260
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.265
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.267
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.272
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.273
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.275
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.261
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.270
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_3.262
+ ___64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.312
+ ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.313
+ ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.313.cold.1
+ ___67-[EDMessageCategorizer categorizeMessages:cancelationToken:reason:]_block_invoke
+ ___67-[EDMessageCategorizer categorizeMessages:cancelationToken:reason:]_block_invoke.127
+ ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.321
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.299
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.299.cold.1
+ ___76-[EDMessageCountQueryHandler _adjustLocalCount:logMessage:generationWindow:]_block_invoke
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.250
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.243
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.243.cold.1
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.246
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.247
+ ___87-[EDMessageCategorizer _categorizeMessages:signpostID:results:cancelationToken:reason:]_block_invoke
+ ___87-[EDMessageCategorizer _categorizeMessages:signpostID:results:cancelationToken:reason:]_block_invoke_3
+ ___87-[EDMessageCategorizer _categorizeMessages:signpostID:results:cancelationToken:reason:]_block_invoke_4
+ ___block_descriptor_160_ea8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8
+ ___block_literal_global.140
+ ___block_literal_global.142
+ ___block_literal_global.153
+ ___block_literal_global.162
+ ___block_literal_global.24
+ ___block_literal_global.290
+ ___block_literal_global.332
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.438
+ ___block_literal_global.55
+ ___block_literal_global.726
+ _objc_msgSend$_categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:
+ _objc_msgSend$_categorizeMessages:signpostID:results:cancelationToken:reason:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$categorizeMessages:cancelationToken:reason:
- +[EDGroupedSender supportsSecureCoding]
- +[EDSearchableIndexVerifier log]
- +[EDSearchableIndexVerifier signpostLog]
- -[EDGroupedSender encodeWithCoder:]
- -[EDGroupedSender initWithCoder:]
- -[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:reason:]
- -[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:reason:].cold.1
- -[EDMessageCategorizer _categorizeMessages:signpostID:results:reason:]
- -[EDMessageCategorizer categorizeMessages:reason:]
- -[EDMessageCountQueryHandler _decrementLocalCount:logMessage:generationWindow:]
- -[EDMessageCountQueryHandler _incrementLocalCount:logMessage:generationWindow:]
- -[EDPersistenceDatabaseConnection deleteAttachmentsInTransactions:]
- -[EDPersistenceDatabaseConnection deleteMessagesInTransactions:]
- -[EDPersistenceDatabaseConnection deleteRichLinksInTransactions:]
- -[EDPersistenceDatabaseConnection deleteTombstonesInTransactions:]
- -[EDPersistenceDatabaseConnection messageIDTransactionIDDictionaryToVerifyWithCount:lastVerifiedMessageID:]
- -[EDPersistenceDatabaseConnection selectAttachmentIdentifiersForTransactions:]
- -[EDPersistenceDatabaseConnection selectMessageIdentifiersForTransactions:]
- -[EDPersistenceDatabaseConnection selectTombstoneIdentifiersForTransactions:]
- -[EDSearchableIndex _dataSourceVerifyRepresentativeSampleWithCompletion:]
- -[EDSearchableIndex _handleFailingTransactionIDs:]
- -[EDSearchableIndex _handleFailingTransactionIDs:].cold.1
- -[EDSearchableIndex _invalidateItemsInTransactions:]
- -[EDSearchableIndex _processSpotlightVerificationWithCompletion:]
- -[EDSearchableIndex _registerDistantFutureSpotlightVerification]
- -[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]
- -[EDSearchableIndex _scheduleSpotlightVerification]
- -[EDSearchableIndex _verifySpotlightIndex]
- -[EDSearchableIndex bundleIDForSearchableIndexVerifier:]
- -[EDSearchableIndex dataSamplesForSearchableIndexVerifier:searchableIndex:count:lastVerifiedMessageID:]
- -[EDSearchableIndex enableSpotlightVerification]
- -[EDSearchableIndex knownTransactionIDsForSearchableIndexVerifier:]
- -[EDSearchableIndex scheduleRecurringActivity]
- -[EDSearchableIndex searchableIndexForSearchableIndexVerifier:]
- -[EDSearchableIndex setEnableSpotlightVerification:]
- -[EDSearchableIndexDataSample .cxx_destruct]
- -[EDSearchableIndexDataSample copyWithZone:]
- -[EDSearchableIndexDataSample dateReceived]
- -[EDSearchableIndexDataSample deleted]
- -[EDSearchableIndexDataSample flags]
- -[EDSearchableIndexDataSample indexedAsEmptySubject]
- -[EDSearchableIndexDataSample setDateReceived:]
- -[EDSearchableIndexDataSample setDeleted:]
- -[EDSearchableIndexDataSample setFlags:]
- -[EDSearchableIndexDataSample setIndexedAsEmptySubject:]
- -[EDSearchableIndexDataSample setSubject:]
- -[EDSearchableIndexDataSample setToEmailAddresses:]
- -[EDSearchableIndexDataSample setTransactionID:]
- -[EDSearchableIndexDataSample setUserInfo:]
- -[EDSearchableIndexDataSample subject]
- -[EDSearchableIndexDataSample toEmailAddresses]
- -[EDSearchableIndexDataSample transactionID]
- -[EDSearchableIndexDataSample userInfo]
- -[EDSearchableIndexManager needsToScheduleRecurringActivity]
- -[EDSearchableIndexManager scheduleRecurringActivity]
- -[EDSearchableIndexManager setNeedsToScheduleRecurringActivity:]
- -[EDSearchableIndexPersistence searchableIndex:invalidateItemsInTransactions:]
- -[EDSearchableIndexPersistence verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:]
- -[EDSearchableIndexPersistence verificationDataSamplesFromMessageIDTransactionIDDictionary:]
- -[EDSearchableIndexState needsToScheduleVerification]
- -[EDSearchableIndexState needsVerification]
- -[EDSearchableIndexState scheduledVerification]
- -[EDSearchableIndexState setNeedsVerification:]
- -[EDSearchableIndexState setScheduledVerification:]
- -[EDSearchableIndexSubjectTester expressionFromDataSamples:]
- -[EDSearchableIndexSubjectTester fetchAttributes]
- -[EDSearchableIndexSubjectTester transformDataForVerification:]
- -[EDSearchableIndexSubjectTester verifySearchableItem:matchesDataSample:]
- -[EDSearchableIndexVerifier .cxx_destruct]
- -[EDSearchableIndexVerifier _addFailingSamples:toResultDictionary:]
- -[EDSearchableIndexVerifier _findMissingTransactionIDs:dataSource:]
- -[EDSearchableIndexVerifier _findMissingTransactionIDs:dataSource:].cold.1
- -[EDSearchableIndexVerifier _missingTransactionIDsFromTransactionIDs:]
- -[EDSearchableIndexVerifier _verifyDataSamples:]
- -[EDSearchableIndexVerifier _verifyDataSamples:].cold.1
- -[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]
- -[EDSearchableIndexVerifier _verifySamples:]
- -[EDSearchableIndexVerifier dataSource]
- -[EDSearchableIndexVerifier indexVerificationActivity]
- -[EDSearchableIndexVerifier initWithDataSource:]
- -[EDSearchableIndexVerifier setDataSource:]
- -[EDSearchableIndexVerifier setIndexVerificationActivity:]
- -[EDSearchableIndexVerifier signpostID]
- -[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]
- -[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:].cold.1
- _EDSpotlightVerificationActivityIdentifier
- _OBJC_CLASS_$_EDSearchableIndexDataSample
- _OBJC_CLASS_$_EDSearchableIndexSubjectTester
- _OBJC_CLASS_$_EDSearchableIndexVerifier
- _OBJC_CLASS_$_SDRDiagnosticReporter
- _OBJC_IVAR_$_EDSearchableIndex._enableSpotlightVerification
- _OBJC_IVAR_$_EDSearchableIndexDataSample._dateReceived
- _OBJC_IVAR_$_EDSearchableIndexDataSample._deleted
- _OBJC_IVAR_$_EDSearchableIndexDataSample._flags
- _OBJC_IVAR_$_EDSearchableIndexDataSample._indexedAsEmptySubject
- _OBJC_IVAR_$_EDSearchableIndexDataSample._subject
- _OBJC_IVAR_$_EDSearchableIndexDataSample._toEmailAddresses
- _OBJC_IVAR_$_EDSearchableIndexDataSample._transactionID
- _OBJC_IVAR_$_EDSearchableIndexDataSample._userInfo
- _OBJC_IVAR_$_EDSearchableIndexManager._needsToScheduleRecurringActivity
- _OBJC_IVAR_$_EDSearchableIndexState._needsVerification
- _OBJC_IVAR_$_EDSearchableIndexState._scheduledVerification
- _OBJC_IVAR_$_EDSearchableIndexVerifier._dataSource
- _OBJC_IVAR_$_EDSearchableIndexVerifier._indexVerificationActivity
- _OBJC_METACLASS_$_EDSearchableIndexDataSample
- _OBJC_METACLASS_$_EDSearchableIndexSubjectTester
- _OBJC_METACLASS_$_EDSearchableIndexVerifier
- _XPC_ACTIVITY_INTERVAL_4_HOURS
- __OBJC_$_CLASS_METHODS_EDSearchableIndexVerifier
- __OBJC_$_CLASS_PROP_LIST_EDGroupedSender
- __OBJC_$_CLASS_PROP_LIST_EDSearchableIndexVerifier
- __OBJC_$_INSTANCE_METHODS_EDSearchableIndexDataSample
- __OBJC_$_INSTANCE_METHODS_EDSearchableIndexSubjectTester
- __OBJC_$_INSTANCE_METHODS_EDSearchableIndexVerifier
- __OBJC_$_INSTANCE_VARIABLES_EDSearchableIndexDataSample
- __OBJC_$_INSTANCE_VARIABLES_EDSearchableIndexVerifier
- __OBJC_$_PROP_LIST_EDSearchableIndexDataSample
- __OBJC_$_PROP_LIST_EDSearchableIndexSubjectTester
- __OBJC_$_PROP_LIST_EDSearchableIndexTesting
- __OBJC_$_PROP_LIST_EDSearchableIndexVerifier
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDSearchableIndexTesting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDSearchableIndexVerifierDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_EDSearchableIndexTesting
- __OBJC_$_PROTOCOL_METHOD_TYPES_EDSearchableIndexVerifierDataSource
- __OBJC_$_PROTOCOL_REFS_EDSearchableIndexTesting
- __OBJC_$_PROTOCOL_REFS_EDSearchableIndexVerifierDataSource
- __OBJC_CLASS_PROTOCOLS_$_EDSearchableIndexDataSample
- __OBJC_CLASS_PROTOCOLS_$_EDSearchableIndexSubjectTester
- __OBJC_CLASS_PROTOCOLS_$_EDSearchableIndexVerifier
- __OBJC_CLASS_RO_$_EDSearchableIndexDataSample
- __OBJC_CLASS_RO_$_EDSearchableIndexSubjectTester
- __OBJC_CLASS_RO_$_EDSearchableIndexVerifier
- __OBJC_LABEL_PROTOCOL_$_EDSearchableIndexTesting
- __OBJC_LABEL_PROTOCOL_$_EDSearchableIndexVerifierDataSource
- __OBJC_METACLASS_RO_$_EDSearchableIndexDataSample
- __OBJC_METACLASS_RO_$_EDSearchableIndexSubjectTester
- __OBJC_METACLASS_RO_$_EDSearchableIndexVerifier
- __OBJC_PROTOCOL_$_EDSearchableIndexTesting
- __OBJC_PROTOCOL_$_EDSearchableIndexVerifierDataSource
- ___102-[EDSearchableIndexPersistence verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:]_block_invoke
- ___105-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) selectMessageIdentifiersForTransactions:]_block_invoke
- ___107-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) selectTombstoneIdentifiersForTransactions:]_block_invoke
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.420
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.425
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.426
- ___107-[EDSearchableIndexPersistence itemsToIndexForSearchableIndex:excludingIdentifiers:count:cancelationToken:]_block_invoke.427
- ___137-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) messageIDTransactionIDDictionaryToVerifyWithCount:lastVerifiedMessageID:]_block_invoke
- ___32+[EDSearchableIndexVerifier log]_block_invoke
- ___40+[EDSearchableIndexVerifier signpostLog]_block_invoke
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.211
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.215
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.218
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke_2.217
- ___42-[EDSearchableIndex _verifySpotlightIndex]_block_invoke
- ___46-[EDMessageCountQueryHandler willSyncMailbox:]_block_invoke.91
- ___48-[EDSearchableIndexVerifier _verifyDataSamples:]_block_invoke
- ___48-[EDSearchableIndexVerifier _verifyDataSamples:]_block_invoke.cold.1
- ___50-[EDMessageCategorizer categorizeMessages:reason:]_block_invoke
- ___50-[EDMessageCategorizer categorizeMessages:reason:]_block_invoke.127
- ___51-[EDSearchableIndex _scheduleSpotlightVerification]_block_invoke
- ___51-[EDSearchableIndex _scheduleSpotlightVerification]_block_invoke_2
- ___51-[EDSearchableIndex _scheduleSpotlightVerification]_block_invoke_3
- ___51-[EDSearchableIndex _scheduleSpotlightVerification]_block_invoke_4
- ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke
- ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.342
- ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.345
- ___59-[EDSearchableIndex _doIndexItems:fromRefresh:immediately:]_block_invoke.348
- ___60-[EDMessageCountQueryHandler _notifyObserverWithLogMessage:]_block_invoke.84
- ___60-[EDMessageCountQueryHandler _notifyObserverWithLogMessage:]_block_invoke.89
- ___60-[EDSearchableIndexSubjectTester expressionFromDataSamples:]_block_invoke
- ___60-[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]_block_invoke
- ___60-[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]_block_invoke_2
- ___60-[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]_block_invoke_3
- ___60-[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]_block_invoke_4
- ___60-[EDSearchableIndexVerifier _verifyDataSamples:usingTester:]_block_invoke_5
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.291
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.295
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.297
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.302
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.303
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.305
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.292
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_2.300
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke_3.293
- ___64-[EDSearchableIndex _registerDistantFutureSpotlightVerification]_block_invoke
- ___64-[EDSearchableIndex _registerDistantFutureSpotlightVerification]_block_invoke_2
- ___64-[EDSearchableIndex redonateAllItemsWithAcknowledgementHandler:]_block_invoke.343
- ___65-[EDSearchableIndex _processSpotlightVerificationWithCompletion:]_block_invoke
- ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.344
- ___66-[EDSearchableIndex resetIndexForNewLibraryWithCompletionHandler:]_block_invoke.344.cold.1
- ___67-[EDSearchableIndexVerifier _addFailingSamples:toResultDictionary:]_block_invoke
- ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.352
- ___70-[EDMessageCategorizer _categorizeMessages:signpostID:results:reason:]_block_invoke
- ___70-[EDMessageCategorizer _categorizeMessages:signpostID:results:reason:]_block_invoke_3
- ___70-[EDMessageCategorizer _categorizeMessages:signpostID:results:reason:]_block_invoke_4
- ___70-[EDSearchableIndexVerifier _missingTransactionIDsFromTransactionIDs:]_block_invoke
- ___70-[EDSearchableIndexVerifier _missingTransactionIDsFromTransactionIDs:]_block_invoke_2
- ___70-[EDSearchableIndexVerifier _missingTransactionIDsFromTransactionIDs:]_block_invoke_3
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.329
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.329.cold.1
- ___73-[EDSearchableIndex _dataSourceVerifyRepresentativeSampleWithCompletion:]_block_invoke
- ___78-[EDSearchableIndexPersistence searchableIndex:invalidateItemsInTransactions:]_block_invoke
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke.31
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke.33
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke.34
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke_2
- ___78-[EDSearchableIndexVerifier verifyDataSamplesWithCompletionHandler:scheduler:]_block_invoke_2.32
- ___79-[EDMessageCountQueryHandler _decrementLocalCount:logMessage:generationWindow:]_block_invoke
- ___79-[EDMessageCountQueryHandler _incrementLocalCount:logMessage:generationWindow:]_block_invoke
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.281
- ___81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke
- ___81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.184
- ___81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.cold.1
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.273
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.273.cold.1
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.276
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.277
- ___87-[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:reason:]_block_invoke
- ___87-[EDMessageCategorizer _categorizeMessages:senderAttributes:signpostID:results:reason:]_block_invoke.cold.1
- ___block_descriptor_176_ea8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8
- ___block_descriptor_32_e17_v16?0"NSArray"8l
- ___block_descriptor_32_e47_"NSString"16?0"EDSearchableIndexDataSample"8l
- ___block_descriptor_40_ea8_32r_e22_v16?0"NSDictionary"8lr32l8
- ___block_descriptor_40_ea8_32r_e54_v32?0"NSNumber"8"EDSearchableIndexDataSample"16^B24lr32l8
- ___block_descriptor_40_ea8_32s_e30_v24?0"NSString"8"NSArray"16ls32l8
- ___block_descriptor_40_ea8_32s_e35_v32?0"NSNumber"8"NSString"16^B24ls32l8
- ___block_descriptor_48_ea8_32bs_e5_v8?0ls32l8
- ___block_descriptor_48_ea8_32s40s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e54_v32?0"NSNumber"8"EDSearchableIndexDataSample"16^B24ls32l8s40l8
- ___block_descriptor_49_ea8_32s40s_e21_v24?0Q8"EFFuture"16ls32l8s40l8
- ___block_descriptor_56_ea8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_ea8_32s40s48bs_e31_v32?0Q8"EFFuture"16"NSSet"24ls32l8s48l8s40l8
- ___block_descriptor_56_ea8_32s40s48s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8
- ___block_descriptor_73_ea8_32s40s48s56s64r_e17_v16?0"NSArray"8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_89_ea8_32s40s48s56s64s72s80r_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8r80l8s48l8s56l8s64l8s72l8
- ___block_literal_global.152
- ___block_literal_global.165
- ___block_literal_global.167
- ___block_literal_global.192
- ___block_literal_global.338
- ___block_literal_global.361
- ___block_literal_global.412
- ___block_literal_global.474
- ___block_literal_global.72
- ___block_literal_global.782
- ___block_literal_global.82
- ___block_literal_global.89
- _kFailingVerificationFullReindexThreshold
- _kSpotlightVerificationSampleSize
- _kSymptomDiagnosticReplyReason
- _kSymptomDiagnosticReplySessionID
- _kSymptomDiagnosticReplySuccess
- _objc_msgSend$_addFailingSamples:toResultDictionary:
- _objc_msgSend$_categorizeMessages:senderAttributes:signpostID:results:reason:
- _objc_msgSend$_categorizeMessages:signpostID:results:reason:
- _objc_msgSend$_dataSourceVerifyRepresentativeSampleWithCompletion:
- _objc_msgSend$_findMissingTransactionIDs:dataSource:
- _objc_msgSend$_handleFailingTransactionIDs:
- _objc_msgSend$_invalidateItemsInTransactions:
- _objc_msgSend$_missingTransactionIDsFromTransactionIDs:
- _objc_msgSend$_processSpotlightVerificationWithCompletion:
- _objc_msgSend$_registerDistantFutureSpotlightVerification
- _objc_msgSend$_scheduleSpotlightVerification
- _objc_msgSend$_scheduleSpotlightVerificationOnIndexingQueueWithCompletion:
- _objc_msgSend$_verifyDataSamples:
- _objc_msgSend$_verifyDataSamples:usingTester:
- _objc_msgSend$_verifySamples:
- _objc_msgSend$_verifySpotlightIndex
- _objc_msgSend$bundleIDForSearchableIndexVerifier:
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$categorizeMessages:reason:
- _objc_msgSend$dataSamplesForSearchableIndexVerifier:searchableIndex:count:lastVerifiedMessageID:
- _objc_msgSend$decodeInt64ForKey:
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$distinctTransactionIDsForSearchableIndex:
- _objc_msgSend$ef_temporarilyUnavailableError
- _objc_msgSend$enableSpotlightVerification
- _objc_msgSend$encodeInt64:forKey:
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$expressionFromDataSamples:
- _objc_msgSend$expressionWithQueryString:
- _objc_msgSend$fetchAttributes
- _objc_msgSend$indexedAsEmptySubject
- _objc_msgSend$initWithQueue:
- _objc_msgSend$knownTransactionIDsForSearchableIndexVerifier:
- _objc_msgSend$mainBundle
- _objc_msgSend$needsToScheduleRecurringActivity
- _objc_msgSend$needsToScheduleVerification
- _objc_msgSend$needsVerification
- _objc_msgSend$scheduledVerification
- _objc_msgSend$searchableIndex:invalidateItemsInTransactions:
- _objc_msgSend$searchableIndexForSearchableIndexVerifier:
- _objc_msgSend$setAttribute:
- _objc_msgSend$setChangedAttributeResultsBlock:
- _objc_msgSend$setDateReceived:
- _objc_msgSend$setFoundAttributeResultsBlock:
- _objc_msgSend$setIndexedAsEmptySubject:
- _objc_msgSend$setNeedsToScheduleRecurringActivity:
- _objc_msgSend$setNeedsVerification:
- _objc_msgSend$setScheduledVerification:
- _objc_msgSend$setToEmailAddresses:
- _objc_msgSend$setTransactionID:
- _objc_msgSend$setUserInfo:
- _objc_msgSend$signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:
- _objc_msgSend$snapshotWithSignature:duration:events:payload:actions:reply:
- _objc_msgSend$toEmailAddresses
- _objc_msgSend$transactionID
- _objc_msgSend$transformDataForVerification:
- _objc_msgSend$verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:
- _objc_msgSend$verificationDataSamplesFromMessageIDTransactionIDDictionary:
- _objc_msgSend$verifyDataSamplesWithCompletionHandler:scheduler:
- _objc_msgSend$verifySearchableItem:matchesDataSample:
CStrings:
+ "%@ local counts"
+ "<%p: %{public}@> %{public}@ ignored due to newer resync generation (ours: %llu, window: %llu:%llu)"
+ "<%p: %{public}@> %{public}@ overlaps resync generation, scheduling full fetch (ours: %llu, window: %llu:%llu)"
+ "<%p: %{public}@> %{public}@: Scheduling %{public}@ of %lld (window: %llu:%llu)"
+ "<%p: %{public}@> Detected stale flags during prepare (matched %ld of %lu), triggering recalculation"
+ "<%p: %{public}@> STALE FLAGS - globalMessageID %lld: EMMessage.flags.read=%d, expectedRead=%d"
+ "@\"EFCancelationToken\""
+ "B56@0:8@16Q24^@32@40q48"
+ "B64@0:8@16@24Q32@40@48q56"
+ "Changed messages from %lld matches to %lld matches (delta=%ld, currentCount=%ld)"
+ "Stale flags during prepare - changesKey:%@"
+ "_categorizeMessages:senderAttributes:signpostID:results:cancelationToken:reason:"
+ "_categorizeMessages:signpostID:results:cancelationToken:reason:"
+ "capitalizedString"
+ "categorizeMessages:cancelationToken:reason:"
+ "decrement"
+ "increment"
- "  needs verification:             %@\n"
- "  scheduled verification:         %@\n"
- "%@ = '%@'"
- "%@=*"
- "%{public}@ - token canceled"
- "-[EDSearchableIndexPersistence searchableIndex:invalidateItemsInTransactions:]"
- "-[EDSearchableIndexPersistence verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:]"
- "-[EDSearchableIndexPersistence verificationDataSamplesFromMessageIDTransactionIDDictionary:]"
- "0O@"
- "<%p: %{public}@> %{public}@: Scheduling decrement of %lld (window: %llu:%llu)"
- "<%p: %{public}@> %{public}@: Scheduling increment of %lld (window: %llu:%llu)"
- "<%p: %{public}@> decrement ignored due to newer resync generation (ours: %llu, window: %llu:%llu)"
- "<%p: %{public}@> decrement occured during generation window, scheduling full fetch (ours: %llu, window: %llu:%llu)"
- "<%p: %{public}@> increment ignored due to newer resync generation (ours: %llu, window: %llu:%llu)"
- "<%p: %{public}@> increment occured during generation window, scheduling full fetch (ours: %llu, window: %llu:%llu)"
- "<%{public}@:%p> did not return a spotlight query. dataSamples.count=%lu transformedDataSamples.count=%lu"
- "@\"<EDSearchableIndexVerifierDataSource>\""
- "@\"EDSearchableIndex\"24@0:8@\"EDSearchableIndexVerifier\"16"
- "@\"EDSearchableIndexDataSample\"24@0:8@\"EDSearchableIndexDataSample\"16"
- "@\"EMSearchableIndexQueryExpression\"24@0:8@\"NSDictionary\"16"
- "@\"NSDictionary\"40@0:8@\"EDSearchableIndex\"16Q24q32"
- "@\"NSDictionary\"48@0:8@\"EDSearchableIndexVerifier\"16@\"EDSearchableIndex\"24Q32q40"
- "@\"NSSet\"24@0:8@\"EDSearchableIndexVerifier\"16"
- "@\"NSString\"16@?0@\"EDSearchableIndexDataSample\"8"
- "@\"NSString\"24@0:8@\"EDSearchableIndexVerifier\"16"
- "@40@0:8@16Q24q32"
- "@48@0:8@16@24Q32q40"
- "B32@0:8@\"CSSearchableItem\"16@\"EDSearchableIndexDataSample\"24"
- "B48@0:8@16Q24^@32q40"
- "B56@0:8@16@24Q32@40q48"
- "Changed messages from %lld matches to %lld matches"
- "DELETE FROM searchable_attachments WHERE transaction_id IN (%@)"
- "DELETE FROM searchable_message_tombstones WHERE transaction_id IN (%@)"
- "DELETE FROM searchable_messages WHERE transaction_id IN (%@)"
- "DELETE FROM searchable_rich_links WHERE transaction_id IN (%@)"
- "Datasource couldn't verify or Mail didn't fetch any samples"
- "Decrementing local counts"
- "Deleting %lu items from Spotlight index: %{public}@"
- "DisableSpotlightVerification"
- "EDSearchableIndexDataSample"
- "EDSearchableIndexPostFakeCorruptSearchableIndexErrors"
- "EDSearchableIndexSubjectTester"
- "EDSearchableIndexTesting"
- "EDSearchableIndexVerifier"
- "EDSearchableIndexVerifierDataSource"
- "EFPropertyKey_businessDisplayName"
- "EFPropertyKey_businessID"
- "EFPropertyKey_businessLogoID"
- "EFPropertyKey_emailAddress"
- "EFPropertyKey_externalBusinessID"
- "EFPropertyKey_messages"
- "EFPropertyKey_sortDescriptors"
- "EFPropertyKey_unreadCount"
- "FAKED: %@"
- "Failed to delete messages for items in searchable_attachments"
- "Failed to delete messages for items in searchable_message_tombstones"
- "Failed to delete messages for items in searchable_messages"
- "Failed to get diagnostic signature with reason: %@"
- "Failed to get messages for transaction ids in searchable_message_tombstones"
- "Failed to get messages for transaction ids in searchable_messages"
- "Failed to query for transaction identifiers"
- "Failed verification for row:%@ citd:%lld"
- "Found %lu missing transaction(s)"
- "Found all expected transaction identifiers"
- "Incrementing local counts"
- "Index verification failed for %@ transactions: %@"
- "LastVerificationFailureReportDate"
- "No data samples fetched from database. Resetting kDefaultsKeyLastVerifiedMessageID to 0"
- "No transactionIDs were fetched from the database, which implies nothing has been indexed yet. Skipping further verification."
- "Removing corrupt indexes for %lu transactions: %{public}@"
- "SELECT attachment_id FROM searchable_attachments WHERE transaction_id in (%@)"
- "SELECT message_id, transaction_id FROM searchable_messages WHERE reindex_type = 0 AND message IS NOT NULL AND message_id > %lu LIMIT %lu"
- "SELECT rowid FROM searchable_message_tombstones WHERE transaction_id IN (%@)"
- "SELECT rowid FROM searchable_messages WHERE transaction_id IN (%@)"
- "Searchable Index Verification failed\n%@"
- "Searchable Index verification found missing rowids: %@"
- "Searching for random sample of messages to verify for spotlight integrity"
- "Skipping transaction ID verification. Protected data unavailable"
- "Skipping verifyDataSamplesWithCompletionHandler. Protected data unavailable."
- "Spotlight found everything from the sample"
- "Spotlight index and Mail database are out of sync, items may be missing or duplicated"
- "SpotlightVerificationSamples=%{public,signpost.telemetry:number1}lu SpotlightVerificationResultFailures=%{public,signpost.telemetry:number2}ld SpotlightVerificationFailingRatio=%{public,signpost.description:attribute}f enableTelemetry=YES "
- "T@\"<EDSearchableIndexVerifierDataSource>\",W,N,V_dataSource"
- "T@\"NSArray\",C,N,V_toEmailAddresses"
- "T@\"NSDate\",&,N,V_dateReceived"
- "T@\"NSDictionary\",C,N,V_userInfo"
- "T@\"NSNumber\",&,N,V_flags"
- "T@\"NSNumber\",&,N,V_indexedAsEmptySubject"
- "T@\"NSNumber\",&,N,V_transactionID"
- "T@\"NSObject<OS_os_activity>\",&,N,V_indexVerificationActivity"
- "T@\"NSString\",C,N,V_deleted"
- "T@\"NSString\",C,N,V_subject"
- "TB,N,V_enableSpotlightVerification"
- "TB,N,V_needsToScheduleRecurringActivity"
- "TB,N,V_needsVerification"
- "TB,N,V_scheduledVerification"
- "Verification Failed"
- "Verification failed at ratio %f. Performing verification with a larger sample of size %lu"
- "Verification failed at ratio: %f. threshold: %f"
- "Verification query results empty"
- "VerificationStateCorrupt"
- "_addFailingSamples:toResultDictionary:"
- "_categorizeMessages:senderAttributes:signpostID:results:reason:"
- "_categorizeMessages:signpostID:results:reason:"
- "_dataSourceVerifyRepresentativeSampleWithCompletion:"
- "_deleted"
- "_enableSpotlightVerification"
- "_findMissingTransactionIDs:dataSource:"
- "_handleFailingTransactionIDs:"
- "_indexVerificationActivity"
- "_indexedAsEmptySubject"
- "_invalidateItemsInTransactions:"
- "_missingTransactionIDsFromTransactionIDs:"
- "_needsToScheduleRecurringActivity"
- "_needsVerification"
- "_processSpotlightVerificationWithCompletion:"
- "_registerDistantFutureSpotlightVerification"
- "_scheduleSpotlightVerification"
- "_scheduleSpotlightVerificationOnIndexingQueueWithCompletion:"
- "_scheduledVerification"
- "_subject"
- "_toEmailAddresses"
- "_transactionID"
- "_userInfo"
- "_verifyDataSamples:"
- "_verifyDataSamples:usingTester:"
- "_verifySamples:"
- "_verifySpotlightIndex"
- "bundleIDForSearchableIndexVerifier:"
- "categorizeMessages:reason:"
- "com.apple.email.spotlightVerification"
- "dataSamplesForSearchableIndexVerifier:searchableIndex:count:lastVerifiedMessageID:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "ef_temporarilyUnavailableError"
- "enableSpotlightVerification"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "expressionFromDataSamples:"
- "expressionWithQueryString:"
- "fetchAttributes"
- "indexVerificationActivity"
- "indexedAsEmptySubject"
- "initWithQueue:"
- "kDefaultsKeyLastVerifiedMessageID"
- "kEDSearchableIndexVerifierErrorDomain"
- "knownTransactionIDsForSearchableIndexVerifier:"
- "needsToScheduleRecurringActivity"
- "needsToScheduleVerification"
- "needsVerification"
- "row:%@ cid:%@\n"
- "scheduledVerification"
- "searchableIndex:invalidateItemsInTransactions:"
- "searchableIndexForSearchableIndexVerifier:"
- "setAttribute:"
- "setChangedAttributeResultsBlock:"
- "setDateReceived:"
- "setEnableSpotlightVerification:"
- "setFoundAttributeResultsBlock:"
- "setIndexVerificationActivity:"
- "setIndexedAsEmptySubject:"
- "setNeedsToScheduleRecurringActivity:"
- "setNeedsVerification:"
- "setScheduledVerification:"
- "setToEmailAddresses:"
- "setTransactionID:"
- "setUserInfo:"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "toEmailAddresses"
- "transactionID"
- "transformDataForVerification:"
- "v24@?0@\"NSString\"8@\"NSArray\"16"
- "v24@?0Q8@\"EFFuture\"16"
- "v32@0:8@?16@24"
- "v32@?0@\"NSNumber\"8@\"EDSearchableIndexDataSample\"16^B24"
- "v32@?0@\"NSNumber\"8@\"NSString\"16^B24"
- "v32@?0Q8@\"EFFuture\"16@\"NSSet\"24"
- "verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:"
- "verificationDataSamplesFromMessageIDTransactionIDDictionary:"
- "verifyDataSamplesWithCompletionHandler:scheduler:"
- "verifySearchableItem:matchesDataSample:"
- "verifying representative sample of items in the datasource are actually indexed"
- "verifying searchable index"

```
