## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.200.33.2.2
-  __TEXT.__text: 0x261804
-  __TEXT.__auth_stubs: 0x2640
-  __TEXT.__objc_methlist: 0x13054
+3864.200.63.0.0
+  __TEXT.__text: 0x262d98
+  __TEXT.__auth_stubs: 0x26b0
+  __TEXT.__objc_methlist: 0x1305c
   __TEXT.__const: 0x33ac
-  __TEXT.__gcc_except_tab: 0x4ee68
-  __TEXT.__cstring: 0x269fa
-  __TEXT.__oslogstring: 0x1a464
+  __TEXT.__gcc_except_tab: 0x4ef30
+  __TEXT.__cstring: 0x26aaa
+  __TEXT.__oslogstring: 0x1a474
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xb44
-  __TEXT.__swift5_typeref: 0xc87
+  __TEXT.__swift5_typeref: 0xcd5
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0xd04
   __TEXT.__swift5_fieldmd: 0x10dc
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x24c
   __TEXT.__swift5_types: 0x13c
-  __TEXT.__swift5_capture: 0x3bc
+  __TEXT.__swift5_capture: 0x3cc
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x10938
+  __TEXT.__unwind_info: 0x10948
   __TEXT.__eh_frame: 0xe90
   __TEXT.__objc_classname: 0x2c79
-  __TEXT.__objc_methname: 0x374c8
-  __TEXT.__objc_methtype: 0x7968
-  __TEXT.__objc_stubs: 0x24e80
-  __DATA_CONST.__got: 0x1b48
-  __DATA_CONST.__const: 0x9518
+  __TEXT.__objc_methname: 0x375a7
+  __TEXT.__objc_methtype: 0x795c
+  __TEXT.__objc_stubs: 0x24f00
+  __DATA_CONST.__got: 0x1b70
+  __DATA_CONST.__const: 0x94f0
   __DATA_CONST.__objc_classlist: 0x938
-  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaef0
+  __DATA_CONST.__objc_selrefs: 0xaf20
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x658
-  __AUTH_CONST.__auth_got: 0x1330
-  __AUTH_CONST.__const: 0x5ab8
-  __AUTH_CONST.__cfstring: 0x10560
-  __AUTH_CONST.__objc_const: 0x21740
+  __AUTH_CONST.__auth_got: 0x1368
+  __AUTH_CONST.__const: 0x5b28
+  __AUTH_CONST.__cfstring: 0x105e0
+  __AUTH_CONST.__objc_const: 0x21750
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x10f8
-  __AUTH.__data: 0x578
-  __DATA.__objc_ivar: 0x146c
-  __DATA.__data: 0x36d0
+  __AUTH.__objc_data: 0xea0
+  __AUTH.__data: 0x500
+  __DATA.__objc_ivar: 0x1468
+  __DATA.__data: 0x3500
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x43d0
-  __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x4e60
-  __DATA_DIRTY.__data: 0xac8
-  __DATA_DIRTY.__bss: 0x15a0
-  __DATA_DIRTY.__common: 0x38
+  __DATA.__bss: 0x4340
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x50b8
+  __DATA_DIRTY.__data: 0xd90
+  __DATA_DIRTY.__bss: 0x1640
+  __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C45B5DD1-DE4A-3666-89D6-3C4479478FC4
-  Functions: 10645
-  Symbols:   34444
-  CStrings:  14236
+  UUID: A5FBC4DD-4104-3629-AA56-38B3E81E58AF
+  Functions: 10661
+  Symbols:   34453
+  CStrings:  14251
 
Symbols:
+ -[EDConcreteLocalSearchProvider _instantAnswersDebuggingIfNeededForMessage:]
+ -[EDConcreteLocalSearchProvider _updateParsecBundleIdentifierIfNeeded]
+ -[EDDiagnosticInfoGatherer _copyAndCompressDatabaseIntoDirectoryURL:originalURL:targetName:]
+ -[EDDiagnosticInfoGatherer _copyAndCompressDatabaseIntoDirectoryURL:originalURL:targetName:].cold.1
+ -[EDDiagnosticInfoGatherer _copyAndCompressDatabaseIntoDirectoryURL:originalURL:targetName:].cold.2
+ -[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:]
+ -[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:].cold.1
+ -[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:].cold.2
+ -[EDMessageRepository recordHydrationTelemetryWithRequestSource:isLocallyAvailable:startTimestamp:messageDate:error:]
+ -[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:]
+ -[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:]
+ -[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:].cold.1
+ -[EDRichLinkData initWithPersistentID:title:url:]
+ -[EDRichLinkData initWithTitle:url:]
+ -[EDRichLinkPersistence cleanUpLegacyRichLinkFilesAtBasePath:]
+ -[EDRichLinkPersistence cleanUpLegacyRichLinkFilesAtBasePath:].cold.1
+ -[EDRichLinkPersistence cleanUpLegacyRichLinkFilesAtBasePath:].cold.2
+ -[EDRichLinkPersistence cleanUpLegacyRichLinkFilesAtBasePath:].cold.3
+ GCC_except_table286
+ GCC_except_table288
+ GCC_except_table301
+ GCC_except_table307
+ GCC_except_table314
+ GCC_except_table323
+ _OBJC_CLASS_$_EMParsecInstantAnswers
+ __CATEGORY_CLASS_METHODS_EMCoreAnalyticsEvent_$_EmailDaemon
+ __CATEGORY_EMCoreAnalyticsEvent_$_EmailDaemon
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.403
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.403.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.405
+ ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.504
+ ___37-[EDMessagePersistence test_tearDown]_block_invoke
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.752
+ ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.756
+ ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.633
+ ___67-[EDRichLinkPersistence saveRichLinkData:globalMessageID:basePath:]_block_invoke
+ ___67-[EDRichLinkPersistence saveRichLinkData:globalMessageID:basePath:]_block_invoke_2
+ ___70-[EDConcreteLocalSearchProvider _updateParsecBundleIdentifierIfNeeded]_block_invoke
+ ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.620
+ ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.449
+ ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.502
+ ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.466
+ ___85-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:]_block_invoke
+ ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.739
+ ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.56
+ ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.56.cold.1
+ ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.64
+ ___95-[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:]_block_invoke
+ ___95-[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:]_block_invoke.cold.1
+ ___block_descriptor_56_ea8_32s40s48s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.305
+ ___block_literal_global.364
+ ___block_literal_global.439
+ ___block_literal_global.443
+ ___block_literal_global.452
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.545
+ ___block_literal_global.551
+ ___block_literal_global.569
+ ___block_literal_global.572
+ ___block_literal_global.581
+ ___block_literal_global.584
+ ___block_literal_global.587
+ ___block_literal_global.616
+ ___block_literal_global.622
+ ___block_literal_global.635
+ ___block_literal_global.67
+ ___block_literal_global.683
+ ___block_literal_global.715
+ ___block_literal_global.723
+ ___block_literal_global.731
+ ___block_literal_global.734
+ ___block_literal_global.738
+ ___block_literal_global.742
+ ___block_literal_global.748
+ ___block_literal_global.751
+ ___block_literal_global.755
+ ___block_literal_global.762
+ ___swift_memcpy41_8
+ __updateParsecBundleIdentifierIfNeeded.onceToken
+ _block_copy_helper.116
+ _block_copy_helper.123
+ _block_copy_helper.131
+ _block_copy_helper.139
+ _block_copy_helper.16
+ _block_copy_helper.160
+ _block_copy_helper.167
+ _block_copy_helper.177
+ _block_copy_helper.187
+ _block_copy_helper.197
+ _block_copy_helper.34
+ _block_copy_helper.42
+ _block_copy_helper.50
+ _block_copy_helper.57
+ _block_copy_helper.64
+ _block_copy_helper.7
+ _block_copy_helper.71
+ _block_copy_helper.79
+ _block_copy_helper.86
+ _block_copy_helper.93
+ _block_descriptor.118
+ _block_descriptor.125
+ _block_descriptor.133
+ _block_descriptor.141
+ _block_descriptor.162
+ _block_descriptor.169
+ _block_descriptor.179
+ _block_descriptor.18
+ _block_descriptor.189
+ _block_descriptor.199
+ _block_descriptor.36
+ _block_descriptor.44
+ _block_descriptor.52
+ _block_descriptor.59
+ _block_descriptor.66
+ _block_descriptor.73
+ _block_descriptor.81
+ _block_descriptor.88
+ _block_descriptor.9
+ _block_descriptor.95
+ _block_destroy_helper.117
+ _block_destroy_helper.124
+ _block_destroy_helper.132
+ _block_destroy_helper.140
+ _block_destroy_helper.161
+ _block_destroy_helper.168
+ _block_destroy_helper.17
+ _block_destroy_helper.178
+ _block_destroy_helper.188
+ _block_destroy_helper.198
+ _block_destroy_helper.35
+ _block_destroy_helper.43
+ _block_destroy_helper.51
+ _block_destroy_helper.58
+ _block_destroy_helper.65
+ _block_destroy_helper.72
+ _block_destroy_helper.8
+ _block_destroy_helper.80
+ _block_destroy_helper.87
+ _block_destroy_helper.94
+ _objc_msgSend$_copyAndCompressDatabaseIntoDirectoryURL:originalURL:targetName:
+ _objc_msgSend$_copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:
+ _objc_msgSend$_instantAnswersDebuggingIfNeededForMessage:
+ _objc_msgSend$_updateParsecBundleIdentifierIfNeeded
+ _objc_msgSend$cleanUpLegacyRichLinkFilesAtBasePath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$gatherIndexingDiagnosticsWithRedaction:completionHandler:
+ _objc_msgSend$hydrationEventWithRequestSource:isLocallyAvailable:startTimestamp:messageDate:error:
+ _objc_msgSend$initFakeWithMessage:
+ _objc_msgSend$initWithPersistentID:title:url:
+ _objc_msgSend$initWithTitle:url:
+ _objc_msgSend$setBundleIdentifier:
+ _symbolic SS_So8NSObjectCt
+ _symbolic Si_Sit
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s11_SetStorageC 10Foundation8CalendarV9ComponentO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation8CalendarV9ComponentO
- -[EDDiagnosticInfoGatherer _copySearchIndexerDatabaseIntoDirectoryURL:].cold.1
- -[EDDiagnosticInfoGatherer _copySearchIndexerDatabaseIntoDirectoryURL:].cold.2
- -[EDMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]
- -[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:error:]
- -[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:error:]
- -[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:error:].cold.1
- -[EDRichLinkData data]
- -[EDRichLinkData initWithPersistentID:title:url:data:]
- -[EDRichLinkData initWithTitle:url:data:]
- -[EDRichLinkPersistence _richLinkDirectoryURLWithBasePath:]
- -[EDRichLinkPersistence _richLinkDirectoryURLWithBasePath:].cold.1
- -[EDRichLinkPersistence _richLinkDirectoryURLWithBasePath:].cold.2
- -[EDRichLinkPersistence _richLinkFileURLWithID:basePath:]
- -[EDRichLinkPersistence richLinkFileURLWithID:basePath:]
- -[EDRichLinkPersistence richLinkMetadataDataForPersistentID:basePath:]
- -[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]
- -[EDRichLinkPersistence verifyFileExistsForRichLinkID:basePath:]
- -[EDSearchableIndexPersistence searchableRichLinkItemMetadataForRichLinkID:messagePersistentID:mailboxID:title:url:result:].cold.2
- GCC_except_table281
- GCC_except_table287
- GCC_except_table289
- GCC_except_table302
- GCC_except_table308
- GCC_except_table315
- _OBJC_IVAR_$_EDRichLinkData._data
- ___105-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:error:]_block_invoke
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.406
- ___115-[EDMessagePersistence _iteratePersistedMessagesMatchingQuery:limit:cancelationToken:requireProtectedData:handler:]_block_invoke.502
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke.750
- ___46-[EDMessagePersistence setGeneratedSummaries:]_block_invoke_2.754
- ___51-[EDRichLinkPersistence richLinkURLsForMessageIDs:]_block_invoke.cold.2
- ___67-[EDMessagePersistence _checkCachedMetadataRowLimitWithConnection:]_block_invoke.631
- ___70-[EDMessagePersistence _setCachedMetadataJSON:forKey:globalMessageID:]_block_invoke.618
- ___76-[EDMessagePersistence messageObjectIDCriterionExpressionForPredicateValue:]_block_invoke.447
- ___77-[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]_block_invoke
- ___77-[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]_block_invoke.cold.1
- ___77-[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]_block_invoke_2
- ___82-[EDMessagePersistence persistedMessagesMatchingQuery:limit:requireProtectedData:]_block_invoke.500
- ___85-[EDMessagePersistence _iterateMessagesMatchingQuery:limit:cancelationToken:handler:]_block_invoke.464
- ___88-[EDMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke
- ___88-[EDMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.cold.1
- ___88-[EDMessageRepository requestRichLinkMetadataForRichLinkID:messageID:completionHandler:]_block_invoke.cold.2
- ___89-[EDMessagePersistence updateDisplayDateForPersistedMessages:displayDate:changeIsRemote:]_block_invoke.737
- ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.52
- ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.52.cold.1
- ___90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.60
- ___block_descriptor_56_ea8_32s40s48r_e25_v32?0"EFSQLRow"8Q16^B24lr48l8s32l8s40l8
- ___block_descriptor_96_ea8_32s40s48s56s64s72s80r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
- ___block_literal_global.303
- ___block_literal_global.440
- ___block_literal_global.444
- ___block_literal_global.450
- ___block_literal_global.518
- ___block_literal_global.521
- ___block_literal_global.543
- ___block_literal_global.549
- ___block_literal_global.565
- ___block_literal_global.570
- ___block_literal_global.579
- ___block_literal_global.582
- ___block_literal_global.585
- ___block_literal_global.614
- ___block_literal_global.620
- ___block_literal_global.63
- ___block_literal_global.633
- ___block_literal_global.681
- ___block_literal_global.711
- ___block_literal_global.719
- ___block_literal_global.729
- ___block_literal_global.732
- ___block_literal_global.736
- ___block_literal_global.740
- ___block_literal_global.746
- ___block_literal_global.749
- ___block_literal_global.753
- ___block_literal_global.760
- ___swift_memcpy25_8
- _block_copy_helper.122
- _block_copy_helper.129
- _block_copy_helper.136
- _block_copy_helper.161
- _block_copy_helper.169
- _block_copy_helper.179
- _block_copy_helper.189
- _block_copy_helper.19
- _block_copy_helper.33
- _block_copy_helper.40
- _block_copy_helper.48
- _block_copy_helper.55
- _block_copy_helper.62
- _block_copy_helper.69
- _block_copy_helper.77
- _block_copy_helper.85
- _block_copy_helper.9
- _block_copy_helper.92
- _block_descriptor.11
- _block_descriptor.124
- _block_descriptor.131
- _block_descriptor.138
- _block_descriptor.163
- _block_descriptor.171
- _block_descriptor.181
- _block_descriptor.191
- _block_descriptor.21
- _block_descriptor.35
- _block_descriptor.42
- _block_descriptor.50
- _block_descriptor.57
- _block_descriptor.64
- _block_descriptor.71
- _block_descriptor.79
- _block_descriptor.87
- _block_descriptor.94
- _block_destroy_helper.10
- _block_destroy_helper.123
- _block_destroy_helper.130
- _block_destroy_helper.137
- _block_destroy_helper.162
- _block_destroy_helper.170
- _block_destroy_helper.180
- _block_destroy_helper.190
- _block_destroy_helper.20
- _block_destroy_helper.34
- _block_destroy_helper.41
- _block_destroy_helper.49
- _block_destroy_helper.56
- _block_destroy_helper.63
- _block_destroy_helper.70
- _block_destroy_helper.78
- _block_destroy_helper.86
- _block_destroy_helper.93
- _objc_msgSend$_richLinkDirectoryURLWithBasePath:
- _objc_msgSend$_richLinkFileURLWithID:basePath:
- _objc_msgSend$initWithPersistentID:title:url:data:
- _objc_msgSend$initWithTitle:url:data:
- _objc_msgSend$richLinkFileURLWithID:basePath:
- _objc_msgSend$richLinkMetadataDataForPersistentID:basePath:
- _objc_msgSend$saveRichLinkData:url:title:globalMessageID:basePath:
- _objc_msgSend$verifyFileExistsForRichLinkID:basePath:
CStrings:
+ "-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:]"
+ "-[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:]"
+ "-[EDRichLinkPersistence saveRichLinkData:globalMessageID:basePath:]"
+ "@48@0:8i16B20d24@32@40"
+ "Added %@."
+ "Cannot cleanup rich link files, base path is null."
+ "CountQueryDeltaUpdates"
+ "EDRichLinkPersistence.m"
+ "EmailDaemon"
+ "Evicted from Queue"
+ "Expected directory at %@ but found a file."
+ "Failed to compress %@."
+ "Failed to copy %@."
+ "Failed to fetch requested message: %{public}@"
+ "Failed to gather indexing diagnostics."
+ "Failed to remove legacy RichLinkData directory at %@: %{public}@"
+ "Fetching transaction write generation"
+ "Found requested message in initial batch: objectID=%{public}@"
+ "IndexingDiagnostics-database"
+ "Looking for requested message with objectID: %{public}@"
+ "MISMATCH: Requested objectID %{public}@ but found message with objectID %{public}@"
+ "Requested message not in initial batch, fetching separately: %{public}@"
+ "RichLinkData directory does not exist at %@, no cleanup needed."
+ "Storing transaction write generation"
+ "Successfully fetched requested message: %{public}@"
+ "Successfully removed legacy RichLinkData directory at %@"
+ "T@\"EDEnqueuedDonation\",&"
+ "T@\"EDEnqueuedDonation\",&,V_enqueuedDonation"
+ "_copyAndCompressDatabaseIntoDirectoryURL:originalURL:targetName:"
+ "_copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:"
+ "_instantAnswersDebuggingIfNeededForMessage:"
+ "_updateParsecBundleIdentifierIfNeeded"
+ "calculateMessageAge:"
+ "cleanUpLegacyRichLinkFilesAtBasePath:"
+ "com.apple.mail.hydration"
+ "fileExistsAtPath:isDirectory:"
+ "hydrationEventWithRequestSource:isLocallyAvailable:startTimestamp:messageDate:error:"
+ "initFakeWithMessage:"
+ "initWithInt:"
+ "initWithPersistentID:title:url:"
+ "initWithTitle:url:"
+ "initWithUnsignedInteger:"
+ "recordHydrationTelemetryWithRequestSource:isLocallyAvailable:startTimestamp:messageDate:error:"
+ "setBundleIdentifier:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v48@0:8i16B20d24@\"NSDate\"32@\"NSError\"40"
+ "v48@0:8i16B20d24@32@40"
- "-[EDPersistenceDatabaseConnection _fetchTransactionWriteGenerationWithSQLConnection:newGeneration:error:]"
- "-[EDPersistenceDatabaseConnection _storeTransactionWriteGenerationWithSQLConnection:newGeneration:error:]"
- "-[EDRichLinkPersistence saveRichLinkData:url:title:globalMessageID:basePath:]"
- "@56@0:8@16@24@32q40@48"
- "Added Search Indexer database."
- "Batch Error Rate"
- "Batch Success Rate"
- "Could not find a message for persistent ID: %@"
- "Could not find rich link directory, base path is null."
- "Donation Success Rate"
- "Encountered a reference to an invalid file in the rich_links table for richLinkPersistentID:%{public}@, messagePersistentID:%{public}@"
- "Failed to compress Search Indexer database."
- "Failed to copy Search Indexer database."
- "Failed to create Rich Link data directory:\n%{public}@"
- "Fetched data: %@ for rich link with richLinkID:%@"
- "Message %@ does not have a base path"
- "Requesting rich link metadata for rich link id: %@ in base path: %@"
- "T@\"EDEnqueuedDonation\",&,N"
- "T@\"EDEnqueuedDonation\",&,N,V_enqueuedDonation"
- "T@\"NSData\",R,N,V_data"
- "Unable to find url for rich link with ID %@"
- "Unable to persist rich link with richLinkID: %@ and messageID: %lld to database"
- "Unable to read rich link at URL %@"
- "_richLinkDirectoryURLWithBasePath:"
- "_richLinkFileURLWithID:basePath:"
- "initWithPersistentID:title:url:data:"
- "initWithTitle:url:data:"
- "requestRichLinkMetadataForRichLinkID:messageID:completionHandler:"
- "richLinkFileURLWithID:basePath:"
- "richLinkMetadataDataForPersistentID:basePath:"
- "saveRichLinkData:url:title:globalMessageID:basePath:"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\">32"
- "verifyFileExistsForRichLinkID:basePath:"

```
