## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3774.100.2.2.5
-  __TEXT.__text: 0x19f06c
-  __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0xfbe4
-  __TEXT.__gcc_except_tab: 0x32b48
-  __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x15b77
-  __TEXT.__oslogstring: 0x11247
+3774.200.91.2.1
+  __TEXT.__text: 0x1a4214
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_methlist: 0xfdac
+  __TEXT.__gcc_except_tab: 0x334ec
+  __TEXT.__const: 0x2c2
+  __TEXT.__cstring: 0x194ab
+  __TEXT.__oslogstring: 0x11693
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
-  __TEXT.__unwind_info: 0xc210
+  __TEXT.__swift5_typeref: 0x2c
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__unwind_info: 0xc370
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x26ba
-  __TEXT.__objc_methname: 0x2d1d6
-  __TEXT.__objc_methtype: 0x6adf
-  __TEXT.__objc_stubs: 0x1e220
+  __TEXT.__objc_classname: 0x2843
+  __TEXT.__objc_methname: 0x2e6bc
+  __TEXT.__objc_methtype: 0x739f
+  __TEXT.__objc_stubs: 0x1e740
   __DATA_CONST.__got: 0x680
-  __DATA_CONST.__const: 0x7878
-  __DATA_CONST.__objc_classlist: 0x778
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x318
+  __DATA_CONST.__const: 0x7950
+  __DATA_CONST.__objc_classlist: 0x788
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b7e0
-  __DATA_CONST.__objc_selrefs: 0x9698
+  __DATA_CONST.__objc_const: 0x1c5d8
+  __DATA_CONST.__objc_selrefs: 0x9818
   __DATA_CONST.__objc_arraydata: 0x6c0
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__cfstring: 0xe040
+  __AUTH_CONST.__objc_const: 0x160
+  __AUTH_CONST.__cfstring: 0xe160
   __AUTH_CONST.__objc_intobj: 0x750
-  __AUTH_CONST.__const: 0x538
+  __AUTH_CONST.__const: 0x838
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x940
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0xdb0
-  __DATA.__objc_superrefs: 0x570
-  __DATA.__objc_ivar: 0x1370
-  __DATA.__data: 0x2560
+  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_protorefs: 0x98
+  __DATA.__objc_classrefs: 0xdd0
+  __DATA.__objc_superrefs: 0x580
+  __DATA.__objc_ivar: 0x1398
+  __DATA.__data: 0x28c0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xc0
-  __DATA_DIRTY.__const: 0x1820
+  __DATA.__bss: 0xe8
+  __DATA_DIRTY.__const: 0x1660
   __DATA_DIRTY.__objc_const: 0x5a30
   __DATA_DIRTY.__objc_data: 0x4ab0
   __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x8c0
+  __DATA_DIRTY.__bss: 0x8b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Synapse.framework/Synapse
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E4367A2B-348A-3104-A366-0424AC6305AE
-  Functions: 7492
-  Symbols:   28217
-  CStrings:  13116
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 44BA7254-C3A4-3032-82CE-146FA89C217A
+  Functions: 7561
+  Symbols:   28536
+  CStrings:  13562
 
Symbols:
+ +[EDDataDetectionUtilities _isRealWord:locale:]
+ +[EDDataDetectionUtilities _isRealWord:locale:].cold.1
+ +[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:].cold.1
+ +[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:].cold.2
+ -[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]
+ -[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:].cold.1
+ -[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:].cold.2
+ -[EDInMemoryThreadQueryHandler _reportChanges:reloadSummaries:]
+ -[EDMessagePersistence expressionForFilteringUnavailableMessagesFromCountForGlobalMessageQuery]
+ -[EDMessagePersistence expressionForFilteringUnavailableMessages]
+ -[EDMessageQueryParser additionalSQLClauseForGlobalMessageCountQuery]
+ -[EDPersistenceDatabase __performReadWithCaller:usingBlock:]
+ -[EDPersistenceDatabase __performWriteWithCaller:usingBlock:]
+ -[EDPersistenceDatabase performWithOptions:caller:block:]
+ -[EDPersistenceDatabase queryLogger]
+ -[EDPersistenceDatabase test_tearDown]
+ -[EDPersistenceDatabaseConnection SQLQueryLogger]
+ -[EDPersistenceDatabaseConnection setTransactionLabel:]
+ -[EDPersistenceDatabaseConnection transactionLabel]
+ -[EDPersistenceDatabaseJournalManager test_tearDown]
+ -[EDPersistenceHookRegistry _messageRespondersWithInvocation:].cold.1
+ -[EDProtectedDatabasePersistence test_tearDown]
+ -[EDRemindMeNotificationController addRemindMeObserver:]
+ -[EDRemindMeNotificationController removeRemindMeObserver:]
+ -[EDSQLQueryLogger .cxx_destruct]
+ -[EDSQLQueryLogger _createFileHandle]
+ -[EDSQLQueryLogger _createQueryInfoFilePath]
+ -[EDSQLQueryLogger _saveSQLQueryInfo:]
+ -[EDSQLQueryLogger fileHandle]
+ -[EDSQLQueryLogger init]
+ -[EDSQLQueryLogger logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:]
+ -[EDSQLQueryLogger queryInfoFilePath]
+ -[EDSQLQueryLogger queryLoggingScheduler]
+ -[EDSQLQueryLogger setFileHandle:]
+ -[EDSQLQueryLogger setQueryInfoFilePath:]
+ -[EDSearchableIndex _processAttachmentItemsForSuggestionsService:]
+ -[EDSearchableIndex _processAttachmentItemsForSuggestionsService:].cold.1
+ -[EDSearchableIndex _processAttachmentItemsForSuggestionsService:].cold.2
+ -[EDSearchableIndex _suggestionsService]
+ -[EDSearchableIndexAttachmentItemMetadatum messageIDHeader]
+ -[EDSearchableIndexAttachmentItemMetadatum setMessageIDHeader:]
+ -[EDSynapseAttributes .cxx_destruct]
+ -[EDSynapseAttributes initWithSenderAddressComment:senderAddress:messagePersistentID:receivedDate:]
+ -[EDSynapseAttributes messagePersistentID]
+ -[EDSynapseAttributes receivedDate]
+ -[EDSynapseAttributes saveToFile:error:]
+ -[EDSynapseAttributes senderAddressComment]
+ -[EDSynapseAttributes senderAddress]
+ -[EDVisibleMessagesReloadRegistry addVisibleMessagesObserver:]
+ -[EDWebContentParser _extractOneTimeCodeFromHTMLString:orWithData:characterEncodingName:withSubject:]
+ -[EDWebContentParser _extractPlainTextFromHTMLString:orWithData:characterEncodingName:]
+ -[EDWebContentParser _extractPlainTextFromHTMLString:orWithData:characterEncodingName:].cold.1
+ -[EDWebContentParser _parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:]
+ -[EDWebContentParser _parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:].cold.1
+ -[EDWebContentParser parseHTMLData:characterEncodingName:withOptions:forMessage:withSubject:completionHandler:]
+ -[EDWebContentParser parseHTMLString:withOptions:forMessage:withSubject:completionHandler:]
+ -[SYDocumentAttributes(EDSynapseAttributes) initWithEDAttributes:file:]
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table289
+ GCC_except_table299
+ GCC_except_table300
+ GCC_except_table305
+ _ECConvertCharacterSetNameToEncoding
+ _EDSearchableIndexAttachmentIsOrderFile
+ _OBJC_CLASS_$_EDSQLQueryLogger
+ _OBJC_CLASS_$_EDSynapseAttributes
+ _OBJC_CLASS_$_SYDocumentAttributes
+ _OBJC_CLASS_$_SYDocumentSender
+ _OBJC_CLASS_$_SYDocumentWorkflows
+ _OBJC_IVAR_$_EDMessageQueryParser._additionalSQLClauseForGlobalMessageCountQuery
+ _OBJC_IVAR_$_EDPersistenceDatabase._queryLogger
+ _OBJC_IVAR_$_EDPersistenceDatabaseConnection._transactionLabel
+ _OBJC_IVAR_$_EDSQLQueryLogger._fileHandle
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryInfoFilePath
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryLoggingScheduler
+ _OBJC_IVAR_$_EDSearchableIndexAttachmentItemMetadatum._messageIDHeader
+ _OBJC_IVAR_$_EDSynapseAttributes._messagePersistentID
+ _OBJC_IVAR_$_EDSynapseAttributes._receivedDate
+ _OBJC_IVAR_$_EDSynapseAttributes._senderAddress
+ _OBJC_IVAR_$_EDSynapseAttributes._senderAddressComment
+ _OBJC_METACLASS_$_EDSQLQueryLogger
+ _OBJC_METACLASS_$_EDSynapseAttributes
+ _OSAtomicDecrement32Barrier
+ _OSAtomicIncrement32Barrier
+ __Block_copy
+ __Block_release
+ __OBJC_$_CATEGORY_SYDocumentAttributes_$_EDSynapseAttributes
+ __OBJC_$_INSTANCE_METHODS_EDSQLQueryLogger
+ __OBJC_$_INSTANCE_METHODS_EDSynapseAttributes
+ __OBJC_$_INSTANCE_METHODS_SYDocumentAttributes(EDSynapseAttributes)
+ __OBJC_$_INSTANCE_VARIABLES_EDSQLQueryLogger
+ __OBJC_$_INSTANCE_VARIABLES_EDSynapseAttributes
+ __OBJC_$_PROP_LIST_EDPersistenceDatabaseConnectionDelegate
+ __OBJC_$_PROP_LIST_EDSQLQueryLogger
+ __OBJC_$_PROP_LIST_EDSynapseAttributes
+ __OBJC_$_PROTOCOL_CLASS_METHODS__SGSuggestionsServiceBaseProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EFSQLQueryLogging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EDPersistenceDatabaseConnectionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SGSuggestionsServiceMailProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceBaseProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceContactsConfirmRejectProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceContactsObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceEventsConfirmRejectProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceEventsObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceMailIntelligenceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceMetricsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EFSQLQueryLogging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SGSuggestionsServiceMailProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceBaseProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceContactsConfirmRejectProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceContactsObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceEventsConfirmRejectProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceEventsObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceMailIntelligenceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceMetricsProtocol
+ __OBJC_$_PROTOCOL_REFS_EFSQLQueryLogging
+ __OBJC_$_PROTOCOL_REFS_SGSuggestionsServiceMailProtocol
+ __OBJC_$_PROTOCOL_REFS__SGSuggestionsServiceBaseProtocol
+ __OBJC_CLASS_PROTOCOLS_$_EDSQLQueryLogger
+ __OBJC_CLASS_RO_$_EDSQLQueryLogger
+ __OBJC_CLASS_RO_$_EDSynapseAttributes
+ __OBJC_LABEL_PROTOCOL_$_EFSQLQueryLogging
+ __OBJC_LABEL_PROTOCOL_$_SGSuggestionsServiceMailProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceBaseProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceContactsConfirmRejectProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceContactsObserverProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceEventsConfirmRejectProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceEventsObserverProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceMailIntelligenceProtocol
+ __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceMetricsProtocol
+ __OBJC_METACLASS_RO_$_EDSQLQueryLogger
+ __OBJC_METACLASS_RO_$_EDSynapseAttributes
+ __OBJC_PROTOCOL_$_EFSQLQueryLogging
+ __OBJC_PROTOCOL_$_SGSuggestionsServiceMailProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceBaseProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceContactsConfirmRejectProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceContactsObserverProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceEventsConfirmRejectProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceEventsObserverProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceMailIntelligenceProtocol
+ __OBJC_PROTOCOL_$__SGSuggestionsServiceMetricsProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SGSuggestionsServiceMailProtocol
+ ___105-[EDSenderPersistence _addressesGroupedByContactForAddresses:unmatchedAddresses:otherAddressesByContact:]_block_invoke.138
+ ___109-[EDSenderPersistence _moveSenderWithSimpleEmailAddresses:toBucket:sync:userInitiated:transactionGeneration:]_block_invoke.90
+ ___109-[EDSenderPersistence _moveSenderWithSimpleEmailAddresses:toBucket:sync:userInitiated:transactionGeneration:]_block_invoke_2.92
+ ___111-[EDWebContentParser parseHTMLData:characterEncodingName:withOptions:forMessage:withSubject:completionHandler:]_block_invoke
+ ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke.48
+ ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke_2.47
+ ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke_2.50
+ ___119-[EDSenderPersistence _blockOrUnblockSendersForAddresses:block:blockedAddressDatabaseIDs:connection:addressesToUpdate:]_block_invoke.128
+ ___140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.150
+ ___140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.158
+ ___36-[EDSenderPersistence test_tearDown]_block_invoke
+ ___39-[EDMessageQueryHelper _foundMessages:]_block_invoke.47
+ ___40-[EDSearchableIndex _suggestionsService]_block_invoke
+ ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke.37
+ ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke_2.38
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.217
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.222
+ ___47+[EDDataDetectionUtilities _isRealWord:locale:]_block_invoke
+ ___47-[EDSenderPersistence relevantSendersForSearch]_block_invoke.76
+ ___52-[EDPersistenceDatabaseJournalManager test_tearDown]_block_invoke
+ ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.369
+ ___52-[EDSearchableIndex removeItemsForDomainIdentifier:]_block_invoke.386
+ ___56-[EDRemindMeNotificationController addRemindMeObserver:]_block_invoke
+ ___56-[EDRemindMeNotificationController addRemindMeObserver:]_block_invoke_2
+ ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.373
+ ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke_2.374
+ ___59-[EDRemindMeNotificationController removeRemindMeObserver:]_block_invoke
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.311
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.313
+ ___62-[EDVisibleMessagesReloadRegistry addVisibleMessagesObserver:]_block_invoke
+ ___63-[EDInMemoryThreadQueryHandler _reportChanges:reloadSummaries:]_block_invoke
+ ___63-[EDInMemoryThreadQueryHandler _reportChanges:reloadSummaries:]_block_invoke_2
+ ___64-[EDMessageTransformer transformPersistedMessages:mailboxScope:]_block_invoke.cold.1
+ ___64-[EDSearchableIndex searchableItemSnippetDataMatchingCriterion:]_block_invoke.393
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.193
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.239
+ ___66-[EDSearchableIndex _processAttachmentItemsForSuggestionsService:]_block_invoke
+ ___66-[EDSearchableIndex _processAttachmentItemsForSuggestionsService:]_block_invoke.cold.1
+ ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.383
+ ___69+[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:]_block_invoke.82
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.337
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.337.cold.1
+ ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.370
+ ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.370.cold.1
+ ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.371
+ ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.392
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.292
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.293
+ ___81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.191
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.285.cold.1
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.288
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.289
+ ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.52
+ ___86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.105
+ ___86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke_2.107
+ ___91-[EDWebContentParser parseHTMLString:withOptions:forMessage:withSubject:completionHandler:]_block_invoke
+ ___94-[EDWebContentParser _parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:]_block_invoke
+ ___94-[EDWebContentParser _parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:]_block_invoke_2
+ ___95-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:]_block_invoke
+ ____ef_log_EDPersistenceDatabaseConnectionPool_block_invoke
+ ___block_descriptor_32_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e28_v16?0"EFCancelationToken"8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1000
+ ___block_literal_global.1036
+ ___block_literal_global.130
+ ___block_literal_global.148
+ ___block_literal_global.181
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.261
+ ___block_literal_global.270
+ ___block_literal_global.30
+ ___block_literal_global.328
+ ___block_literal_global.329
+ ___block_literal_global.340
+ ___block_literal_global.357
+ ___block_literal_global.365
+ ___block_literal_global.381
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.58
+ ___block_literal_global.60
+ ___block_literal_global.75
+ ___block_literal_global.77
+ ___block_literal_global.82
+ ___block_literal_global.86
+ ___block_literal_global.998
+ ___swift_reflection_version
+ __ef_log_EDPersistenceDatabaseConnectionPool
+ __ef_log_EDPersistenceDatabaseConnectionPool.log
+ __ef_log_EDPersistenceDatabaseConnectionPool.onceToken
+ __parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:.baseURLCount
+ __suggestionsService.onceToken
+ __suggestionsService.suggestionsInstance
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreGraphics_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFileProvider_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftWebKit
+ __swift_FORCE_LOAD_$_swiftWebKit_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_EmailDaemon
+ _block_copy_helper
+ _block_copy_helper.5
+ _block_descriptor
+ _block_descriptor.7
+ _block_destroy_helper
+ _block_destroy_helper.6
+ _objc_msgSend$SQLQueryLogger
+ _objc_msgSend$__performReadWithCaller:usingBlock:
+ _objc_msgSend$__performWriteWithCaller:usingBlock:
+ _objc_msgSend$_createFileHandle
+ _objc_msgSend$_createQueryInfoFilePath
+ _objc_msgSend$_extractOneTimeCodeFromHTMLString:orWithData:characterEncodingName:withSubject:
+ _objc_msgSend$_extractPlainTextFromHTMLString:orWithData:characterEncodingName:
+ _objc_msgSend$_isRealWord:locale:
+ _objc_msgSend$_parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:
+ _objc_msgSend$_processAttachmentItemsForSuggestionsService:
+ _objc_msgSend$_reportChanges:reloadSummaries:
+ _objc_msgSend$_saveSQLQueryInfo:
+ _objc_msgSend$_suggestionsService
+ _objc_msgSend$addRemindMeObserver:
+ _objc_msgSend$additionalSQLClauseForGlobalMessageCountQuery
+ _objc_msgSend$canUseSearchableIndex
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$dissectAttachmentsFromSearchableItem:options:withCompletion:
+ _objc_msgSend$documentAttributesForFileAtURL:error:
+ _objc_msgSend$ef_secureCodableError
+ _objc_msgSend$expressionForFilteringUnavailableMessages
+ _objc_msgSend$expressionForFilteringUnavailableMessagesFromCountForGlobalMessageQuery
+ _objc_msgSend$fileHandle
+ _objc_msgSend$fileHandleForWritingAtPath:
+ _objc_msgSend$initWithEDAttributes:file:
+ _objc_msgSend$initWithName:handle:
+ _objc_msgSend$initWithSourceBundleIdentifier:indexKey:originalFileURL:receivedDate:sender:
+ _objc_msgSend$isSupportedContentType:
+ _objc_msgSend$loadHTMLString:baseURL:
+ _objc_msgSend$parseHTMLData:characterEncodingName:withOptions:forMessage:withSubject:completionHandler:
+ _objc_msgSend$performWithOptions:caller:block:
+ _objc_msgSend$preparedStatementForQueryString:transactionLabel:queryLogger:
+ _objc_msgSend$queryInfoFilePath
+ _objc_msgSend$queryLogger
+ _objc_msgSend$queryLoggingScheduler
+ _objc_msgSend$queryWithPredicate:
+ _objc_msgSend$queryWithTargetClass:predicate:
+ _objc_msgSend$receivedDate
+ _objc_msgSend$redactedQueryStringForQueryString:
+ _objc_msgSend$removeRemindMeObserver:
+ _objc_msgSend$saveToFile:error:
+ _objc_msgSend$saveToFileURL:error:
+ _objc_msgSend$seekToEndReturningOffset:error:
+ _objc_msgSend$senderAddressComment
+ _objc_msgSend$setAttachmentNames:
+ _objc_msgSend$setAttachmentPaths:
+ _objc_msgSend$setAttachmentTypes:
+ _objc_msgSend$setTransactionLabel:
+ _objc_msgSend$transactionLabel
+ _objc_msgSend$waitForDeletes
+ _objc_msgSend$writeData:error:
+ _protocol_getMethodDescription
+ _swift_allocObject
+ _swift_deallocObject
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release
+ _swift_retain
+ _symbolic So31EDPersistenceDatabaseConnectionCSbIggd_
- -[EDMessagePersistence expressionForFilteringUnavailableMessagesForGlobalMessageQuery:]
- -[EDMessageQueryParser additionalSQLClauseForGlobalMessageQuery]
- -[EDPersistenceDatabase performReadBlock:]
- -[EDPersistenceDatabase performWithOptions:block:]
- -[EDPersistenceDatabase performWriteBlock:]
- -[EDRemindMeNotificationController addObserver:]
- -[EDRemindMeNotificationController removeObserver:]
- -[EDVisibleMessagesReloadRegistry addObserver:]
- -[EDWebContentParser _checkHTMLDataForOneTimeCodes:withSubject:]
- -[EDWebContentParser _parseHTMLData:withOptions:characterEncodingName:messageID:]
- -[EDWebContentParser _parseHTMLData:withOptions:characterEncodingName:messageID:].cold.1
- -[EDWebContentParser parseHTMLData:withOptions:characterEncodingName:forMessage:withSubject:completionHandler:]
- GCC_except_table242
- GCC_except_table285
- GCC_except_table291
- GCC_except_table292
- GCC_except_table297
- _OBJC_IVAR_$_EDMessageQueryParser._additionalSQLClauseForGlobalMessageQuery
- _OUTLINED_FUNCTION_10
- ___105-[EDSenderPersistence _addressesGroupedByContactForAddresses:unmatchedAddresses:otherAddressesByContact:]_block_invoke.135
- ___109-[EDSenderPersistence _moveSenderWithSimpleEmailAddresses:toBucket:sync:userInitiated:transactionGeneration:]_block_invoke.87
- ___109-[EDSenderPersistence _moveSenderWithSimpleEmailAddresses:toBucket:sync:userInitiated:transactionGeneration:]_block_invoke_2.89
- ___111-[EDWebContentParser parseHTMLData:withOptions:characterEncodingName:forMessage:withSubject:completionHandler:]_block_invoke
- ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke.46
- ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke.47
- ___116-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke_2.49
- ___119-[EDSenderPersistence _blockOrUnblockSendersForAddresses:block:blockedAddressDatabaseIDs:connection:addressesToUpdate:]_block_invoke.125
- ___140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.148
- ___140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.156
- ___39+[EDDataDetectionUtilities isRealWord:]_block_invoke
- ___39-[EDMessageQueryHelper _foundMessages:]_block_invoke.46
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.214
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.219
- ___47-[EDInMemoryThreadQueryHandler _reportChanges:]_block_invoke
- ___47-[EDInMemoryThreadQueryHandler _reportChanges:]_block_invoke_2
- ___47-[EDSenderPersistence relevantSendersForSearch]_block_invoke.74
- ___47-[EDVisibleMessagesReloadRegistry addObserver:]_block_invoke
- ___48-[EDRemindMeNotificationController addObserver:]_block_invoke
- ___48-[EDRemindMeNotificationController addObserver:]_block_invoke_2
- ___51-[EDRemindMeNotificationController removeObserver:]_block_invoke
- ___52-[EDSearchableIndex _invalidateItemsInTransactions:]_block_invoke.366
- ___52-[EDSearchableIndex removeItemsForDomainIdentifier:]_block_invoke.383
- ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke.370
- ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke_2.371
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.302
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.307
- ___64-[EDSearchableIndex searchableItemSnippetDataMatchingCriterion:]_block_invoke.390
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.192
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.238
- ___68-[EDSearchableIndex removeItemsWithIdentifiers:reasons:fromRefresh:]_block_invoke.380
- ___69+[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:]_block_invoke_2
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.334
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.334.cold.1
- ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.367
- ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.367.cold.1
- ___71-[EDSearchableIndex reindexAllItemsWithOptions:acknowledgementHandler:]_block_invoke.368
- ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.391
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.289
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.290
- ___81-[EDSearchableIndex _scheduleSpotlightVerificationOnIndexingQueueWithCompletion:]_block_invoke.188
- ___81-[EDWebContentParser _parseHTMLData:withOptions:characterEncodingName:messageID:]_block_invoke
- ___81-[EDWebContentParser _parseHTMLData:withOptions:characterEncodingName:messageID:]_block_invoke_2
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.282
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.282.cold.1
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.286
- ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.51
- ___86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.102
- ___86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke_2.104
- ___block_descriptor_64_ea8_32s40s48s56r_e28_v16?0"EFCancelationToken"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.131
- ___block_literal_global.145
- ___block_literal_global.174
- ___block_literal_global.178
- ___block_literal_global.196
- ___block_literal_global.198
- ___block_literal_global.258
- ___block_literal_global.267
- ___block_literal_global.27
- ___block_literal_global.325
- ___block_literal_global.351
- ___block_literal_global.362
- ___block_literal_global.375
- ___block_literal_global.386
- ___block_literal_global.56
- ___block_literal_global.59
- ___block_literal_global.70
- ___block_literal_global.74
- ___block_literal_global.841
- ___block_literal_global.843
- ___block_literal_global.85
- ___block_literal_global.880
- ___block_literal_global.89
- __parseHTMLData:withOptions:characterEncodingName:messageID:.baseURLCount
- _createLexiconWithLocale
- _createLexiconWithLocale.cold.1
- _objc_msgSend$_checkHTMLDataForOneTimeCodes:withSubject:
- _objc_msgSend$_parseHTMLData:withOptions:characterEncodingName:messageID:
- _objc_msgSend$addObserver:
- _objc_msgSend$additionalSQLClauseForGlobalMessageQuery
- _objc_msgSend$expressionForFilteringUnavailableMessagesForGlobalMessageQuery:
- _objc_msgSend$isFullTextSearchableCriterion
- _objc_msgSend$parseHTMLData:withOptions:characterEncodingName:forMessage:withSubject:completionHandler:
- _objc_msgSend$performReadBlock:
- _objc_msgSend$performWithOptions:block:
- _objc_msgSend$performWriteBlock:
CStrings:
+ "\x1a"
+ "&"
+ "+[EDTruncateMailboxUpgradeStep presentNeedlessAlertIfNecessaryWithPersistence:]_block_invoke_2"
+ "-[EDAttachmentPersistence attachmentMetadataForMessage:mimePartNumber:]"
+ "-[EDAttachmentPersistence attachmentMetadataForMessage:remoteURL:]"
+ "-[EDAttachmentPersistence attachmentMetadataForMessageAttachmentID:]"
+ "-[EDAttachmentPersistence attachmentsForGlobalMessageIDs:]"
+ "-[EDAttachmentPersistence enumerateAttachmentsInfoForGlobalMessageIDs:withBlock:]"
+ "-[EDAttachmentPersistence globalMessageIDsForAttachment:]"
+ "-[EDAttachmentPersistence insertAttachmentMetadata:]"
+ "-[EDAttachmentPersistence insertMessageAttachmentMetadata:]"
+ "-[EDAttachmentPersistence insertMimePartAttachments:forGlobalMessageID:]"
+ "-[EDAttachmentPersistence messageAttachmentExistsForGlobalMessageID:mimePartNumber:hasAttachmentEntry:]"
+ "-[EDAttachmentPersistence messageAttachmentExistsForGlobalMessageID:remoteURL:hasAttachmentEntry:]"
+ "-[EDAttachmentPersistence messageAttachmentMetadataForMessageID:]"
+ "-[EDAttachmentPersistence removeAttachments:]"
+ "-[EDAttachmentPersistence uniqueAttachmentDataForHash:]"
+ "-[EDAttachmentPersistence updateAttachmentIDForMessageAttachment:]"
+ "-[EDConversationPersistence clearConversationFlagsAndSyncKeyForConversationIDs:]"
+ "-[EDConversationPersistence conversationIDForMessageIDs:]"
+ "-[EDConversationPersistence createConversationWithFlags:]"
+ "-[EDConversationPersistence currentSyncAnchorForDailyExport]"
+ "-[EDConversationPersistence flaggedConversationsChangedBetweenStartAnchor:endAnchor:]"
+ "-[EDConversationPersistence messageIDsForConversationID:limit:]"
+ "-[EDConversationPersistence persistenceConversationFlagsForConversationID:]"
+ "-[EDConversationPersistence previousSyncAnchorForDailyExport]"
+ "-[EDConversationPersistence pruneConversationTables:]"
+ "-[EDConversationPersistence setNewPreviousSyncAnchorForDailyExport:]"
+ "-[EDConversationPersistence setPersistenceConversationFlags:syncKey:forConversationID:reason:]"
+ "-[EDConversationPersistence syncedConversationIDsBySyncKey]"
+ "-[EDConversationPersistence updateAssociationTableForMessageID:dateSent:conversationID:]"
+ "-[EDConversationPersistence updateAssociationTableForMessagePersistentIDs:conversationID:]"
+ "-[EDDataDetectionPersistence addDataDetectionResults:globalMessageID:]"
+ "-[EDDataDetectionPersistence getDataDetectionResultRowIDsForGlobalMessageID:]"
+ "-[EDDataDetectionPersistence getDataDetectionResultsForGlobalMessageID:]"
+ "-[EDLocalActionPersistence messageActionsForAccountURL:previousActionID:]"
+ "-[EDLocalActionPersistence persistFlagChangeAction:]"
+ "-[EDLocalActionPersistence persistFlagChangeUndownloadedAction:]"
+ "-[EDLocalActionPersistence persistLabelChangeAction:]"
+ "-[EDLocalActionPersistence persistTransferAction:]"
+ "-[EDLocalActionPersistence persistTransferUndownloadedAction:]"
+ "-[EDLocalActionPersistence removeMessageAction:]"
+ "-[EDLocalActionPersistence removeMessageActions:]"
+ "-[EDLocalActionPersistence updateFlagChangeAction:withRemainingUIDs:]"
+ "-[EDLocalActionPersistence updateTransferAction:withResults:]"
+ "-[EDLocalActionPersistence updateTransferUndownloadedMessageAction:withResults:]"
+ "-[EDMailboxActionPersistence allMailboxActionForAccountID:]"
+ "-[EDMailboxActionPersistence deleteMailboxAction:]"
+ "-[EDMailboxActionPersistence deleteMailboxActions:]"
+ "-[EDMailboxActionPersistence nextMailboxActionForAccountID:]"
+ "-[EDMailboxActionPersistence saveMailboxActionForAccountID:action:]"
+ "-[EDMessageChangeManager _applyReadLaterDate:toMessages:changeIsRemote:]"
+ "-[EDMessageChangeManager _persistFlagChangeResults:forFlagChangeAction:]"
+ "-[EDMessageChangeManager _persistResults:forFlagChangeAction:]"
+ "-[EDMessageChangeManager _persistResults:forLabelChangeAction:]"
+ "-[EDMessageChangeManager _persistResults:forTransferAction:]"
+ "-[EDMessageChangeManager _reflectFlagChanges:messages:remoteIDs:mailboxURL:]"
+ "-[EDMessageChangeManager addLabels:removeLabels:forMessages:]_block_invoke_2"
+ "-[EDMessageChangeManager addNewMessages:mailboxURL:userInitiated:]_block_invoke"
+ "-[EDMessageChangeManager applyFlagChange:toMessages:]_block_invoke_3"
+ "-[EDMessageChangeManager reflectAddedLabels:removedLabels:forMessagesWithRemoteIDs:mailboxURL:]"
+ "-[EDMessageChangeManager reflectAllMessagesDeletedInMailboxURL:]"
+ "-[EDMessageChangeManager reflectDeletedAllClearedMessagesInMailboxURL:]"
+ "-[EDMessageChangeManager reflectDeletedMessages:]"
+ "-[EDMessageChangeManager reflectDeletedMessagesWithRemoteIDs:mailboxURL:]_block_invoke"
+ "-[EDMessageChangeManager reflectNewMessages:mailboxURL:]_block_invoke"
+ "-[EDMessageChangeManager transferMessages:transferType:destinationMailboxURL:userInitiated:oldMessagesByNewMessage:]_block_invoke"
+ "-[EDMessagePersistence _cachedMetadataJSONForKey:globalMessageID:]"
+ "-[EDMessagePersistence _checkForFollowUpExpirationWithQuery:]"
+ "-[EDMessagePersistence _countForSQLQuery:]"
+ "-[EDMessagePersistence _databaseIDsDictionaryForGlobalMessageIDs:mailboxScope:]"
+ "-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]"
+ "-[EDMessagePersistence _persistedMessageIDsForMessagesForConversationIDs:onlyFollowUps:]"
+ "-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]"
+ "-[EDMessagePersistence addBrandIndicatorWithData:]"
+ "-[EDMessagePersistence brandIndicatorForDatabaseID:]"
+ "-[EDMessagePersistence brandIndicatorForURL:]"
+ "-[EDMessagePersistence brandIndicatorsForURLs:]"
+ "-[EDMessagePersistence collectStatisticsWithStatistics:]"
+ "-[EDMessagePersistence completeCachedMetadataJSONForGlobalMessageID:]"
+ "-[EDMessagePersistence countOfMessageStatement:]"
+ "-[EDMessagePersistence globalIDForMessageIDHash:]"
+ "-[EDMessagePersistence messageObjectIDsForSearchableItemIdentifiers:]"
+ "-[EDMessagePersistence metadataForAddresses:]"
+ "-[EDMessagePersistence performDatabaseReadBlock:]"
+ "-[EDMessagePersistence persistFollowUp:forMessages:]"
+ "-[EDMessagePersistence persistSendLaterForMessages:date:]"
+ "-[EDMessagePersistence persistedMessageIDsForGlobalMessageIDs:]"
+ "-[EDMessagePersistence removeBrandIndicatorForURL:]"
+ "-[EDMessagePersistence retrieveFollowUpJsonStringForModelEvaluationForSuggestionsForMessages:]"
+ "-[EDMessagePersistence setBrandIndicator:forURL:]"
+ "-[EDMessagePersistence setBrandIndicatorDatabaseID:location:forMessages:]"
+ "-[EDMessagePersistence setMetadata:forAddress:]"
+ "-[EDMessagePersistence undownloadedBrandIndicatorsWithLimit:]"
+ "-[EDMessagePersistence updateBeforeDisplayForMessagesMatchingQuery:]"
+ "-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]"
+ "-[EDPersistenceDatabase performDatabaseSetupUsingTransaction:block:]"
+ "-[EDPersistenceDatabase test_tearDown]"
+ "-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:]"
+ "-[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:]"
+ "-[EDPersistenceDatabaseJournalManager test_tearDown]"
+ "-[EDProtectedDatabasePersistence _databaseIDsToDeleteForTable:]"
+ "-[EDProtectedDatabasePersistence _deleteDatabaseIDs:fromTable:]"
+ "-[EDProtectedDatabasePersistence test_tearDown]"
+ "-[EDReadLaterPersistence _persistReadLater:date:]"
+ "-[EDRemoteContentPersistence _refillFromAdditionalTable]"
+ "-[EDRemoteContentPersistence _rowCountForTable:]"
+ "-[EDRemoteContentPersistence addRemoteContentLinks:newLinks:]"
+ "-[EDRemoteContentPersistence countOfLinksLastSeenSince:]"
+ "-[EDRemoteContentPersistence countOfUnrequestedLinks]"
+ "-[EDRemoteContentPersistence getRemoteContentURLInfoOrderedBy:inReverseOrder:limit:error:]"
+ "-[EDRemoteContentPersistence initWithDatabase:useAdditionalTable:]_block_invoke"
+ "-[EDRemoteContentPersistence pruneAllRemoteContentLinksWithMinimumCount:]"
+ "-[EDRemoteContentPersistence remoteContentLinksBelowCount:limit:]"
+ "-[EDRemoteContentPersistence updateRequestCountForRemoteContentLinks:updateLastSeen:]"
+ "-[EDRichLinkPersistence datasForPersistentIDs:basePath:]"
+ "-[EDRichLinkPersistence richLinkDataForPersistentID:basePath:]"
+ "-[EDRichLinkPersistence richLinkPersistentIDsForGlobalMessageID:]"
+ "-[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]"
+ "-[EDSearchableIndexPersistence _addSearchableDataDetectionResults:withMessage:transaction:]"
+ "-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]"
+ "-[EDSearchableIndexPersistence _canPerformIncrementalIndexForIdentifier:indexingType:]"
+ "-[EDSearchableIndexPersistence _richLinkItemsFromRichLinkData:limit:cancelationToken:]"
+ "-[EDSearchableIndexPersistence childIdentifiersToRemoveFromSearchableIndex:whenRemovingParentIdentifiers:]"
+ "-[EDSearchableIndexPersistence clearOrphanedSearchableMessagesFromDatabase]"
+ "-[EDSearchableIndexPersistence distinctTransactionIDsForSearchableIndex:]"
+ "-[EDSearchableIndexPersistence lastProcessedAttachmentID]"
+ "-[EDSearchableIndexPersistence searchableIndex:assignIndexingType:forIdentifiers:]"
+ "-[EDSearchableIndexPersistence searchableIndex:assignTransaction:updates:]"
+ "-[EDSearchableIndexPersistence searchableIndex:attachmentItemsForMessageWithIdentifier:]"
+ "-[EDSearchableIndexPersistence searchableIndex:invalidateItemsGreaterThanTransaction:]"
+ "-[EDSearchableIndexPersistence searchableIndex:invalidateItemsInTransactions:]"
+ "-[EDSearchableIndexPersistence searchableIndex:prepareToIndexAttachmentsForMessageWithIdentifier:]"
+ "-[EDSearchableIndexPersistence searchableIndex:willRemoveIdentifiers:type:]"
+ "-[EDSearchableIndexPersistence setLastProcessedAttachmentID:]"
+ "-[EDSearchableIndexPersistence updatesForSearchableIndex:excludingIdentifiers:count:cancelationToken:]"
+ "-[EDSearchableIndexPersistence verificationDataSamplesForSearchableIndex:count:lastVerifiedMessageID:]"
+ "-[EDSenderPersistence _bucketForSenderAddress:]"
+ "-[EDSenderPersistence _moveSenderWithSimpleEmailAddresses:toBucket:sync:userInitiated:transactionGeneration:]"
+ "-[EDSenderPersistence _updateBlockedSendersWithBlockedSenderAddresses:newlyBlockedAddresses:newlyUnblockedAddresses:]"
+ "-[EDSenderPersistence addAddresses:toSender:]"
+ "-[EDSenderPersistence relevantSendersForSearch]"
+ "-[EDSenderPersistence removeAddresses:fromSender:]"
+ "-[EDServerMessagePersistence _serverMessagesWithWhereClause:limitClause:returnLastEntries:]"
+ "-[EDServerMessagePersistence addLabels:removeLabels:toMessagesWithRemoteIDs:]"
+ "-[EDServerMessagePersistence addServerMessage:invalidMessage:duplicateRemoteID:]"
+ "-[EDServerMessagePersistence applyFlagChange:toMessagesWithRemoteIDs:]"
+ "-[EDServerMessagePersistence applySortedFlags:]"
+ "-[EDServerMessagePersistence attachMessage:toServerMessageWithRemoteID:]"
+ "-[EDServerMessagePersistence deleteAllClearedUIDMessages]"
+ "-[EDServerMessagePersistence deleteAllServerMessagesInMailbox]"
+ "-[EDServerMessagePersistence deleteServerMessagesWithRemoteIDs:]"
+ "-[EDServerMessagePersistence downloadStateForUIDs:]"
+ "-[EDServerMessagePersistence enumerateMessageBatchLimitUIDsWithWindow:batchSize:newUIDCount:block:]"
+ "-[EDServerMessagePersistence enumerateUIDsInIndexSet:includingJSON:excludingJSON:withBlock:]"
+ "-[EDServerMessagePersistence enumerateUIDsInRanges:withBlock:]"
+ "-[EDServerMessagePersistence maximumIMAPUID]"
+ "-[EDServerMessagePersistence messageCount]"
+ "-[EDServerMessagePersistence minimumIMAPUID]"
+ "-[EDServerMessagePersistence serverMessagesForMessageIDHeaders:]"
+ "-[EDServerMessagePersistence setDownloadStateForUIDs:]"
+ "-[EDServerMessagePersistence undeletedMessageCount]"
+ "-[EDServerMessagePersistence unreadMessageCount]"
+ "-[EDThreadPersistence _addThreadScopeToDatabase:needsUpdate:lastViewedDate:updateThreadScopeManager:]"
+ "-[EDThreadPersistence _addressesFromSelectStatement:additionalRowHandling:]"
+ "-[EDThreadPersistence _databaseIDForThreadObjectID:]"
+ "-[EDThreadPersistence _deleteMailboxesFromWrappedMessages:fromThreadWithDatabaseID:messageThreadExpression:]"
+ "-[EDThreadPersistence _deleteRecipientsOfType:fromThreadWithDatabaseID:messageThreadExpression:]"
+ "-[EDThreadPersistence _deleteSendersFromThreadWithDatabaseID:messageThreadExpression:]"
+ "-[EDThreadPersistence _enumerateThreadObjectIDsForThreadScope:filterClause:sortDescriptors:batchBlock:]"
+ "-[EDThreadPersistence _iterateWrappedMessagesByConversationForPersistedMessages:messageFilter:writeBlock:]"
+ "-[EDThreadPersistence _mailboxesForThreadDatabaseID:]"
+ "-[EDThreadPersistence _messagesAreJournaledForThreadWithObjectID:]"
+ "-[EDThreadPersistence _persistedMessagesForMailboxScope:messageExpression:]"
+ "-[EDThreadPersistence _persistenceIsChangingFlags:wrappedMessages:threadObjectID:threadScopeDatabaseID:]"
+ "-[EDThreadPersistence _recalculateDisplayMessageForThreadObjectID:threadScopeDatabaseID:]"
+ "-[EDThreadPersistence _recalculateNewestReadMessageForThreadObjectID:threadScopeDatabaseID:]"
+ "-[EDThreadPersistence _recomputeThreads]_block_invoke_3"
+ "-[EDThreadPersistence _reportSenderBucketChangeForThreadsWithSenderAddresses:generation:]"
+ "-[EDThreadPersistence _resetThreadScope:withDatabaseID:]"
+ "-[EDThreadPersistence _updateBasicPropertiesAfterDeleteForThreadObjectID:threadScopeDatabaseID:]"
+ "-[EDThreadPersistence _updateNewestReadMessageWithWrappedMessage:threadExpression:]"
+ "-[EDThreadPersistence _updateThreadForDeleteWithObjectID:threadScopeDatabaseID:generationWindow:]"
+ "-[EDThreadPersistence addThreads:]"
+ "-[EDThreadPersistence beginMigratingThreadScope:]"
+ "-[EDThreadPersistence changeForThreadWithObjectID:changedKeyPaths:]"
+ "-[EDThreadPersistence deleteThreadsWithObjectIDs:]"
+ "-[EDThreadPersistence endMigratingThreadScope:wasCanceledOrReset:]"
+ "-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortDescriptors:journaledThreadsToCheck:excluding:]"
+ "-[EDThreadPersistence oldestThreadObjectIDForMailbox:threadScope:]"
+ "-[EDThreadPersistence persistenceDidChangeReadLaterDate:messages:changeIsRemote:generationWindow:]_block_invoke"
+ "-[EDThreadPersistence persistenceDidUpdateProperties:message:generationWindow:]_block_invoke"
+ "-[EDThreadPersistence persistenceIsAddingMailboxWithDatabaseID:objectID:generationWindow:]"
+ "-[EDThreadPersistence persistenceIsUpdatingDisplayDateForMessage:fromDate:generation:]_block_invoke"
+ "-[EDThreadPersistence resetThreadScopesForMailboxScope:]"
+ "-[EDThreadPersistence setPriorityForDisplayMessageSenderForThreadObjectID:]"
+ "-[EDThreadPersistence threadForObjectID:originatingQuery:error:]"
+ "-[EDThreadPersistence threadObjectIDsForThreadScope:sortDescriptors:initialBatchSize:journaledObjectIDs:batchBlock:]"
+ "-[EDThreadPersistence threadScopeManager:evictThreadScopesWithDatabaseIDs:completionBlock:]"
+ "-[EDThreadPersistence threadScopeManager:gatherStatisticsForThreadScopesWithDatabaseIDs:block:]"
+ "-[EDThreadPersistence threadScopeManager:populateThreadScopesWithBlock:]"
+ "-[EDThreadPersistence updateLastViewedDateForThreadScope:]"
+ "-[EDThreadPersistence verifyConsistencyOfThreadScope:]_block_invoke"
+ "@\"<EFSQLQueryLogging>\""
+ "@\"<EFSQLQueryLogging>\"16@0:8"
+ "@\"NSArray\"40@0:8@\"CSSearchableItem\"16Q24^@32"
+ "@\"NSArray\"40@0:8@\"NSString\"16q24^@32"
+ "@\"NSArray\"40@0:8q16Q24^@32"
+ "@\"NSArray\"56@0:8q16Q24d32Q40^@48"
+ "@\"NSArray\"60@0:8@\"NSArray\"16@\"NSArray\"24@\"NSDate\"32B40Q44^@52"
+ "@\"NSArray\"96@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSArray\"64@\"NSArray\"72@\"NSArray\"80^@88"
+ "@\"NSNumber\"36@0:8B16@\"SGMailIntelligenceWarning\"20^@28"
+ "@\"NSNumber\"36@0:8B16q20^@28"
+ "@\"NSNumber\"40@0:8q16@\"NSString\"24^@32"
+ "@\"SGMailIntelligenceFollowUpWarning\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32^@40"
+ "@\"SGMailIntelligenceSaliency\"32@0:8@\"NSData\"16^@24"
+ "@\"SGMailIntelligenceSaliency\"32@0:8@\"SGMailHeaders\"16^@24"
+ "@24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
+ "@36@0:8B16@20^@28"
+ "@36@0:8B16q20^@28"
+ "@40@0:8@16Q24^@32"
+ "@40@0:8q16@24^@32"
+ "@40@0:8q16Q24^@32"
+ "@56@0:8@16@24@32Q40@48"
+ "@56@0:8q16Q24d32Q40^@48"
+ "@60@0:8@16@24@32B40Q44^@52"
+ "@96@0:8@16@24@32@40@48@56@64@72@80^@88"
+ "Attachment '%@' already has synapse attributes."
+ "B24@0:8^@16"
+ "B32@0:8@\"SGRecordId\"16^@24"
+ "B36@0:8@\"SGRecordId\"16i24^@28"
+ "B36@0:8@16i24^@28"
+ "B40@0:8Q16@24@?32"
+ "B40@0:8q16@\"NSArray\"24^@32"
+ "B40@0:8q16@24^@32"
+ "Data from HTML in this message could not be decoded with our UTF8 encoding protocol."
+ "Did add Synapse attributes to '%@'."
+ "EDSQLQueryLogger"
+ "EDSearchableIndexAttachmentIsOrderFile"
+ "EDSynapseAttributes"
+ "EFSQLQueryLogging"
+ "Failed to create %{public}@ LXLexiconRef: %{public}@"
+ "Failed to write Synapse attributes to attachment '%@': %@"
+ "Logs/queryInfo"
+ "Messaging responders for hook `-%{public}@`: %{public}@"
+ "Nil searchableItem for item:%{public}@"
+ "No mailbox URL was found for legacy message database id: %{public}@"
+ "No mailbox was found for legacy message database id: %{public}@"
+ "No mailboxes were found for legacy message database id: %{public}@"
+ "Not adding Synapse attributes to '%@': unsupported type %{public}@"
+ "Not adding Synapse attributes. No content type."
+ "Not adding Synapse attributes. No file URL."
+ "Preparing to index attachment from message %@ immediately %@"
+ "Processing attachment items %@ with suggestions service"
+ "SGSuggestionsServiceMailProtocol"
+ "SQLQueryLogger"
+ "SQLQueryLogging"
+ "T@\"<EFSQLQueryLogging>\",R,N"
+ "T@\"<EFSQLQueryLogging>\",R,N,V_queryLogger"
+ "T@\"<EFSQLValueExpressable>\",R,N,V_additionalSQLClauseForGlobalMessageCountQuery"
+ "T@\"<EFScheduler>\",R,N,V_queryLoggingScheduler"
+ "T@\"NSDate\",R,C,N,V_receivedDate"
+ "T@\"NSFileHandle\",&,N,V_fileHandle"
+ "T@\"NSString\",&,N,V_queryInfoFilePath"
+ "T@\"NSString\",C,N,V_messageIDHeader"
+ "T@\"NSString\",C,N,V_transactionLabel"
+ "T@\"NSString\",R,C,N,V_messagePersistentID"
+ "T@\"NSString\",R,C,N,V_senderAddress"
+ "T@\"NSString\",R,C,N,V_senderAddressComment"
+ "Unable to connect to suggestions service mail protocol"
+ "Unable to process the attachment items %{public}@"
+ "_SGSuggestionsServiceBaseProtocol"
+ "_SGSuggestionsServiceContactsConfirmRejectProtocol"
+ "_SGSuggestionsServiceContactsObserverProtocol"
+ "_SGSuggestionsServiceEventsConfirmRejectProtocol"
+ "_SGSuggestionsServiceEventsObserverProtocol"
+ "_SGSuggestionsServiceMailIntelligenceProtocol"
+ "_SGSuggestionsServiceMetricsProtocol"
+ "__performReadWithCaller:usingBlock:"
+ "__performWriteWithCaller:usingBlock:"
+ "_additionalSQLClauseForGlobalMessageCountQuery"
+ "_createFileHandle"
+ "_createQueryInfoFilePath"
+ "_extractOneTimeCodeFromHTMLString:orWithData:characterEncodingName:withSubject:"
+ "_extractPlainTextFromHTMLString:orWithData:characterEncodingName:"
+ "_fileHandle"
+ "_isRealWord:locale:"
+ "_messageIDHeader"
+ "_parseHTMLString:orWithData:characterEncodingName:withOptions:messageID:"
+ "_processAttachmentItemsForSuggestionsService:"
+ "_queryInfoFilePath"
+ "_queryLogger"
+ "_queryLoggingScheduler"
+ "_receivedDate"
+ "_reportChanges:reloadSummaries:"
+ "_saveSQLQueryInfo:"
+ "_senderAddressComment"
+ "_suggestionsService"
+ "_transactionLabel"
+ "acquired background read connection (%d waiters)"
+ "acquired write connection (%d waiters)"
+ "addRemindMeObserver:"
+ "addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:"
+ "addVisibleMessagesObserver:"
+ "additionalSQLClauseForGlobalMessageCountQuery"
+ "canUseSearchableIndex"
+ "com.apple.email.EFSQLPreparedStatement"
+ "com.apple.mobilemail"
+ "confirmContact:withCompletion:"
+ "confirmContactDetailRecord:confirmationUI:error:"
+ "confirmContactDetailRecord:confirmationUI:withCompletion:"
+ "confirmContactDetailRecord:error:"
+ "confirmContactDetailRecord:withCompletion:"
+ "confirmEvent:withCompletion:"
+ "confirmEventByRecordId:error:"
+ "confirmEventByRecordId:withCompletion:"
+ "confirmRecord:error:"
+ "confirmRecord:withCompletion:"
+ "createFileAtPath:contents:attributes:"
+ "deleteEventByRecordId:error:"
+ "deleteEventByRecordId:withCompletion:"
+ "deregisterContactsChangeObserverWithToken:"
+ "deregisterEventsChangeObserverWithToken:"
+ "dissectAttachmentsFromSearchableItem:options:error:"
+ "dissectAttachmentsFromSearchableItem:options:withCompletion:"
+ "documentAttributesForFileAtURL:error:"
+ "ef_secureCodableError"
+ "expressionForFilteringUnavailableMessages"
+ "expressionForFilteringUnavailableMessagesFromCountForGlobalMessageQuery"
+ "fileHandle"
+ "fileHandleForWritingAtPath:"
+ "firstRowExecutionTime"
+ "fullDownloadRequestBatch:withCompletion:"
+ "harvestedSuggestionsFromSearchableItem:options:withCompletion:"
+ "identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:error:"
+ "identifyFollowUpWarningFromSubject:body:date:error:"
+ "initWithEDAttributes:file:"
+ "initWithName:handle:"
+ "initWithSenderAddressComment:senderAddress:messagePersistentID:receivedDate:"
+ "initWithSourceBundleIdentifier:indexKey:originalFileURL:receivedDate:sender:"
+ "isEnabledWithError:"
+ "isHarvestingSupported"
+ "isSupportedContentType:"
+ "keepDirty:"
+ "loadHTMLString:baseURL:"
+ "logEventInteractionForEventWithExternalIdentifier:interface:actionType:"
+ "logEventInteractionForEventWithUniqueKey:interface:actionType:"
+ "logMetricAutocompleteResult:recordId:contactIdentifier:bundleId:"
+ "logMetricAutocompleteUserSelectedRecordId:contactIdentifier:bundleId:"
+ "logMetricContactCreated:contactIdentifier:bundleId:"
+ "logMetricContactSearchResult:recordId:contactIdentifier:bundleId:"
+ "logMetricContactSearchResultSelected:contactIdentifier:bundleId:"
+ "logMetricSearchResultsIncludedPureSuggestionWithBundleId:"
+ "logMetricSuggestedContactDetailShown:contactIdentifier:bundleId:"
+ "logMetricSuggestedContactDetailUsed:contactIdentifier:bundleId:"
+ "logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:"
+ "logSuggestionInteractionForRecordId:interface:actionType:"
+ "messagesToRefreshWithCompletion:"
+ "numberOfRows"
+ "parseHTMLData:characterEncodingName:withOptions:forMessage:withSubject:completionHandler:"
+ "parseHTMLString:withOptions:forMessage:withSubject:completionHandler:"
+ "performWithOptions:caller:block:"
+ "prepareForRealtimeExtraction:"
+ "prepareForRealtimeExtractionWithCompletion:"
+ "preparedStatementForQueryString:transactionLabel:queryLogger:"
+ "preventUnsubscriptionOpportunitiesSuggestionsForField:toValues:error:"
+ "preventUnsubscriptionOpportunitiesSuggestionsForField:toValues:withCompletion:"
+ "queryInfoFilePath"
+ "queryLogger"
+ "queryLoggingScheduler"
+ "queryWithPredicate:"
+ "queryWithTargetClass:predicate:"
+ "queuesRequestsIfBusy"
+ "receivedDate"
+ "redactedQuery"
+ "redactedQueryStringForQueryString:"
+ "registerContactsChangeObserver:"
+ "registerEventsChangeObserver:"
+ "rejectContact:rejectionUI:withCompletion:"
+ "rejectContact:withCompletion:"
+ "rejectContactDetailRecord:error:"
+ "rejectContactDetailRecord:rejectionUI:error:"
+ "rejectContactDetailRecord:rejectionUI:withCompletion:"
+ "rejectContactDetailRecord:withCompletion:"
+ "rejectEvent:withCompletion:"
+ "rejectEventByRecordId:error:"
+ "rejectEventByRecordId:withCompletion:"
+ "rejectRecord:error:"
+ "rejectRecord:rejectionUI:error:"
+ "rejectRecord:rejectionUI:withCompletion:"
+ "rejectRecord:withCompletion:"
+ "removeRemindMeObserver:"
+ "reportMessagesFound:lost:withCompletion:"
+ "reportUserEngagement:forWarning:error:"
+ "reportValue:forFeatureSetting:error:"
+ "resolveFullDownloadRequests:withCompletion:"
+ "saliencyFromEmailHeaders:error:"
+ "saliencyFromEmailHeaders:withCompletion:"
+ "saliencyFromRFC822Data:error:"
+ "saliencyFromRFC822Data:withCompletion:"
+ "saveToFile:error:"
+ "saveToFileURL:error:"
+ "seekToEndReturningOffset:error:"
+ "senderAddressComment"
+ "setAttachmentNames:"
+ "setAttachmentPaths:"
+ "setAttachmentTypes:"
+ "setFileHandle:"
+ "setMessageIDHeader:"
+ "setQueryInfoFilePath:"
+ "setQueuesRequestsIfBusy:"
+ "setTransactionLabel:"
+ "sortedUnsubscriptionOpportunitiesForField:limit:error:"
+ "suggestionsFromSearchableItem:options:processingType:withCompletion:"
+ "suggestionsFromSearchableItem:options:withCompletion:"
+ "syncTimeout"
+ "topSalienciesForMailboxId:limit:error:"
+ "totalExecutionTime"
+ "transactionLabel"
+ "updateMessages:state:withCompletion:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"SGMailIntelligenceSaliency\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSString\"16S24S28"
+ "v32@0:8@\"SGMailHeaders\"16@?<v@?@\"SGMailIntelligenceSaliency\"@\"NSError\">24"
+ "v32@0:8@\"SGRealtimeContact\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SGRealtimeEvent\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SGRecordId\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SGRecordId\"16S24S28"
+ "v32@0:8@16S24S28"
+ "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v36@0:8@\"SGRealtimeContact\"16i24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"SGRecordId\"16i24@?<v@?@\"NSError\">28"
+ "v36@0:8@16i24@?28"
+ "v40@0:8@\"CSSearchableItem\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSDate\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"SGRecordId\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8q16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v44@0:8i16@\"SGRecordId\"20@\"NSString\"28@\"NSString\"36"
+ "v44@0:8i16@20@28@36"
+ "v48@0:8@\"CSSearchableItem\"16Q24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16Q24Q32@?40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24d32d40Q48"
+ "v56@0:8@16@24d32d40Q48"
+ "v64@0:8@16@24Q32@40@48@?56"
+ "waitForEventWithIdentifier:toAppearInEventStoreWithCompletion:"
+ "waitForEventWithIdentifier:toAppearInEventStoreWithLastModificationDate:completion:"
+ "waiting for background read connection (%d waiters)"
+ "waiting for write connection (%d waiters)"
+ "writeData:error:"
- "\t"
- "\x19"
- "%"
- "B24@0:8@?16"
- "B32@0:8Q16@?24"
- "Failed to create %@ LXLexiconRef: %@"
- "T@\"<EFSQLValueExpressable>\",R,N,V_additionalSQLClauseForGlobalMessageQuery"
- "_additionalSQLClauseForGlobalMessageQuery"
- "_checkHTMLDataForOneTimeCodes:withSubject:"
- "_parseHTMLData:withOptions:characterEncodingName:messageID:"
- "addObserver:"
- "additionalSQLClauseForGlobalMessageQuery"
- "expressionForFilteringUnavailableMessagesForGlobalMessageQuery:"
- "isFullTextSearchableCriterion"
- "parseHTMLData:withOptions:characterEncodingName:forMessage:withSubject:completionHandler:"
- "performReadBlock:"
- "performWithOptions:block:"
- "performWriteBlock:"
- "v64@0:8@16Q24@32@40@48@?56"

```
