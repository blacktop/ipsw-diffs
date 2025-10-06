## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0x1a4214
+3774.300.61.2.4
+  __TEXT.__text: 0x1aa05c
   __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0xfdac
-  __TEXT.__gcc_except_tab: 0x334ec
-  __TEXT.__const: 0x2c2
-  __TEXT.__cstring: 0x194ab
-  __TEXT.__oslogstring: 0x11693
+  __TEXT.__objc_methlist: 0x1007c
+  __TEXT.__gcc_except_tab: 0x34234
+  __TEXT.__const: 0x2d2
+  __TEXT.__cstring: 0x1983b
+  __TEXT.__oslogstring: 0x11baa
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x2c
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0xc370
+  __TEXT.__unwind_info: 0xc598
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x2843
-  __TEXT.__objc_methname: 0x2e6bc
-  __TEXT.__objc_methtype: 0x739f
-  __TEXT.__objc_stubs: 0x1e740
+  __TEXT.__objc_classname: 0x2723
+  __TEXT.__objc_methname: 0x2eaf8
+  __TEXT.__objc_methtype: 0x6bbb
+  __TEXT.__objc_stubs: 0x1ede0
   __DATA_CONST.__got: 0x680
-  __DATA_CONST.__const: 0x7950
-  __DATA_CONST.__objc_classlist: 0x788
+  __DATA_CONST.__const: 0x79f0
+  __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x360
+  __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c5d8
-  __DATA_CONST.__objc_selrefs: 0x9818
-  __DATA_CONST.__objc_arraydata: 0x6c0
-  __AUTH_CONST.__objc_const: 0x160
-  __AUTH_CONST.__cfstring: 0xe160
-  __AUTH_CONST.__objc_intobj: 0x750
-  __AUTH_CONST.__const: 0x838
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
+  __DATA_CONST.__objc_const: 0x1c1e8
+  __DATA_CONST.__objc_selrefs: 0x9a00
+  __DATA_CONST.__objc_arraydata: 0x750
+  __AUTH_CONST.__objc_const: 0x280
+  __AUTH_CONST.__cfstring: 0xe580
+  __AUTH_CONST.__objc_intobj: 0x7f8
+  __AUTH_CONST.__const: 0x9b8
+  __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0xdd0
-  __DATA.__objc_superrefs: 0x580
-  __DATA.__objc_ivar: 0x1398
-  __DATA.__data: 0x28c0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_protorefs: 0x90
+  __DATA.__objc_classrefs: 0xdf0
+  __DATA.__objc_superrefs: 0x590
+  __DATA.__objc_ivar: 0x1410
+  __DATA.__data: 0x25c0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xe8
-  __DATA_DIRTY.__const: 0x1660
+  __DATA_DIRTY.__const: 0x15e0
   __DATA_DIRTY.__objc_const: 0x5a30
   __DATA_DIRTY.__objc_data: 0x4ab0
   __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x8b8
+  __DATA_DIRTY.__bss: 0x8d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy
   - /System/Library/PrivateFrameworks/Email.framework/Email
   - /System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing

   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 44BA7254-C3A4-3032-82CE-146FA89C217A
-  Functions: 7561
-  Symbols:   28536
-  CStrings:  13562
+  UUID: B1AC902A-EF83-3FA7-A56B-F68B22C2C121
+  Functions: 7660
+  Symbols:   28861
+  CStrings:  13650
 
Symbols:
+ +[EDMailboxPersistence log]
+ +[EDSQLQueryLogger log]
+ -[EDDiagnosticInfoGatherer searchableIndexDatabaseStatisticsWithCompletionHandler:]
+ -[EDMailboxPersistence _reportPersistenceStatistics:]
+ -[EDMailboxPersistence _startReportingPersistenceStatistics]
+ -[EDMailboxPersistence _stopReportingPersistenceStatistics]
+ -[EDMailboxPersistence dealloc]
+ -[EDMailboxPersistence mailboxDatabaseIDsForMailboxURLStrings:]
+ -[EDMailboxPersistence scheduleRecurringActivity]
+ -[EDMailboxPersistence setStatisticsReportingScheduler:]
+ -[EDMailboxPersistence statisticsReportingScheduler]
+ -[EDMailboxPersistence statistics]
+ -[EDMailboxPersistenceStatistics .cxx_destruct]
+ -[EDMailboxPersistenceStatistics debugDescription]
+ -[EDMailboxPersistenceStatistics initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:messagesPerInbox:]
+ -[EDMailboxPersistenceStatistics mailboxesPerAccount]
+ -[EDMailboxPersistenceStatistics messagesInLargestMailbox]
+ -[EDMailboxPersistenceStatistics messagesInSecondLargestMailbox]
+ -[EDMailboxPersistenceStatistics messagesPerAccount]
+ -[EDMailboxPersistenceStatistics messagesPerInbox]
+ -[EDMailboxPersistenceStatistics messagesPerMailbox]
+ -[EDMailboxPersistenceStatistics redactedDescription]
+ -[EDMessageChangeManager _applyReadLaterDate:displayDate:toMessages:changeIsRemote:]
+ -[EDMessageChangeManager applyReadLaterDate:displayDate:toMessages:]
+ -[EDPersistence searchableIndexStatistics]
+ -[EDPersistenceDatabase _fileProtectionTypeForDatabaseType:]
+ -[EDPersistenceDatabase _scheduleProcessSQLQueryPerformanceData]
+ -[EDPersistenceDatabase protectedDatabaseIsAvailable]
+ -[EDPersistenceDatabase protectedDatabasePath]
+ -[EDPersistenceDatabase requestProtectedDatabaseBackgroundProcessingForDuration:error:]
+ -[EDPersistenceDatabase urlFileProtectionTypeForDatabaseType:]
+ -[EDReadLaterCloudStorage _keyForMessage:]
+ -[EDReadLaterPersistence _persistDisplayDate:message:connection:]
+ -[EDReadLaterPersistence _persistReadLater:date:displayDate:]
+ -[EDReadLaterPersistence persistReadLaterForMessage:date:displayDate:]
+ -[EDSQLQueryLogger _bucketTransactionLabels:]
+ -[EDSQLQueryLogger _createFileIfNeeded:]
+ -[EDSQLQueryLogger _createQueryCountDict:]
+ -[EDSQLQueryLogger _createQueryCountDict:].cold.1
+ -[EDSQLQueryLogger _createQueryCountDict:].cold.2
+ -[EDSQLQueryLogger _createQueryCountLogFilePath]
+ -[EDSQLQueryLogger _createQueryLogDirectoryPath]
+ -[EDSQLQueryLogger _createQueryLogDirectoryPath].cold.1
+ -[EDSQLQueryLogger _createQueryLogFilePath]
+ -[EDSQLQueryLogger _createQueryStatisticsDictionary:queryCountByTransactionLabel:queryCountNum:firstRowExecutionTimeStats:totalExecutionTimeStats:timePerRowExecutionTimeStats:]
+ -[EDSQLQueryLogger _preprocessQueryInfo]
+ -[EDSQLQueryLogger _recreateFile:]
+ -[EDSQLQueryLogger _removeFile:]
+ -[EDSQLQueryLogger _removeFile:].cold.1
+ -[EDSQLQueryLogger _sortQueryCountDict]
+ -[EDSQLQueryLogger _writeQueryStatistics:]
+ -[EDSQLQueryLogger logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:]
+ -[EDSQLQueryLogger queryCountDict]
+ -[EDSQLQueryLogger queryCountLogFilePath]
+ -[EDSQLQueryLogger queryLogDirectoryPath]
+ -[EDSQLQueryLogger queryLogFilePath]
+ -[EDSQLQueryLogger queryStatisticsArray]
+ -[EDSQLQueryLogger rawQueryLogInputFileHandle]
+ -[EDSQLQueryLogger setQueryCountDict:]
+ -[EDSQLQueryLogger setQueryCountLogFilePath:]
+ -[EDSQLQueryLogger setQueryLogDirectoryPath:]
+ -[EDSQLQueryLogger setQueryLogFilePath:]
+ -[EDSQLQueryLogger setQueryStatisticsArray:]
+ -[EDSQLQueryLogger setRawQueryLogInputFileHandle:]
+ -[EDSQLQueryLogger submitQueryLogData]
+ -[EDSQLQueryStatistics .cxx_destruct]
+ -[EDSQLQueryStatistics addStatisticWithTransactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:]
+ -[EDSQLQueryStatistics firstRowEightyPercentileExecutionTime]
+ -[EDSQLQueryStatistics firstRowMaxExecutionTime]
+ -[EDSQLQueryStatistics firstRowMeanExecutionTime]
+ -[EDSQLQueryStatistics firstRowMinExecutionTime]
+ -[EDSQLQueryStatistics firstRowTwentyPercentileExecutionTime]
+ -[EDSQLQueryStatistics initWithQuery:transactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:]
+ -[EDSQLQueryStatistics queryCountByTransactionLabel]
+ -[EDSQLQueryStatistics queryCount]
+ -[EDSQLQueryStatistics redactedQuery]
+ -[EDSQLQueryStatistics timePerRowEightyPercentileExecutionTime]
+ -[EDSQLQueryStatistics timePerRowMaxExecutionTime]
+ -[EDSQLQueryStatistics timePerRowMeanExecutionTime]
+ -[EDSQLQueryStatistics timePerRowMinExecutionTime]
+ -[EDSQLQueryStatistics timePerRowTwentyPercentileExecutionTime]
+ -[EDSQLQueryStatistics totalEightyPercentileExecutionTime]
+ -[EDSQLQueryStatistics totalMaxExecutionTime]
+ -[EDSQLQueryStatistics totalMeanExecutionTime]
+ -[EDSQLQueryStatistics totalMinExecutionTime]
+ -[EDSQLQueryStatistics totalTwentyPercentileExecutionTime]
+ -[EDThreadPersistence beginMigratingThreadScope:].cold.1
+ -[EDThreadPersistence endMigratingThreadScope:]
+ -[EDThreadPersistence endMigratingThreadScope:].cold.1
+ -[_EDThreadMigrationState migrationCancelable]
+ -[_EDThreadMigrationState setMigrationCancelable:]
+ GCC_except_table242
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table292
+ GCC_except_table298
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table308
+ _DRSubmitLog
+ _NSFileProtectionCompleteUnlessOpen
+ _OBJC_CLASS_$_EDMailboxPersistenceStatistics
+ _OBJC_CLASS_$_EDSQLQueryStatistics
+ _OBJC_CLASS_$_EFProtectedFile
+ _OBJC_CLASS_$_EFProtectedFileGroup
+ _OBJC_IVAR_$_EDMailboxPersistence._statisticsReportingScheduler
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._mailboxesPerAccount
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._messagesInLargestMailbox
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._messagesInSecondLargestMailbox
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._messagesPerAccount
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._messagesPerInbox
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._messagesPerMailbox
+ _OBJC_IVAR_$_EDMessageRepository._analyticsCollector
+ _OBJC_IVAR_$_EDPersistenceDatabase._protectedDatabaseFile
+ _OBJC_IVAR_$_EDPersistenceDatabase._protectedDatabasePath
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryCountDict
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryCountLogFilePath
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryLogDirectoryPath
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryLogFilePath
+ _OBJC_IVAR_$_EDSQLQueryLogger._queryStatisticsArray
+ _OBJC_IVAR_$_EDSQLQueryLogger._rawQueryLogInputFileHandle
+ _OBJC_IVAR_$_EDSQLQueryStatistics._firstRowEightyPercentileExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._firstRowMaxExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._firstRowMeanExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._firstRowMinExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._firstRowTwentyPercentileExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._queryCount
+ _OBJC_IVAR_$_EDSQLQueryStatistics._queryCountByTransactionLabel
+ _OBJC_IVAR_$_EDSQLQueryStatistics._redactedQuery
+ _OBJC_IVAR_$_EDSQLQueryStatistics._timePerRowEightyPercentileExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._timePerRowMaxExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._timePerRowMeanExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._timePerRowMinExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._timePerRowTwentyPercentileExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._totalEightyPercentileExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._totalMaxExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._totalMeanExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._totalMinExecutionTime
+ _OBJC_IVAR_$_EDSQLQueryStatistics._totalTwentyPercentileExecutionTime
+ _OBJC_IVAR_$_EDThreadPersistence._backgroundProcessingAssertionsByMigratingThreadScope
+ _OBJC_IVAR_$__EDThreadMigrationState._migrationCancelable
+ _OBJC_METACLASS_$_EDMailboxPersistenceStatistics
+ _OBJC_METACLASS_$_EDSQLQueryStatistics
+ __OBJC_$_CLASS_METHODS_EDMailboxPersistence
+ __OBJC_$_CLASS_METHODS_EDSQLQueryLogger
+ __OBJC_$_INSTANCE_METHODS_EDMailboxPersistenceStatistics
+ __OBJC_$_INSTANCE_METHODS_EDSQLQueryStatistics
+ __OBJC_$_INSTANCE_VARIABLES_EDMailboxPersistenceStatistics
+ __OBJC_$_INSTANCE_VARIABLES_EDSQLQueryStatistics
+ __OBJC_$_PROP_LIST_EDMailboxPersistenceStatistics
+ __OBJC_$_PROP_LIST_EDSQLQueryStatistics
+ __OBJC_CLASS_RO_$_EDMailboxPersistenceStatistics
+ __OBJC_CLASS_RO_$_EDSQLQueryStatistics
+ __OBJC_METACLASS_RO_$_EDMailboxPersistenceStatistics
+ __OBJC_METACLASS_RO_$_EDSQLQueryStatistics
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.353
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.353.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.355
+ ___120-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortDescriptors:journaledThreadsToCheck:excluding:]_block_invoke.274
+ ___121-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:]_block_invoke
+ ___121-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:]_block_invoke.cold.1
+ ___121-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:]_block_invoke.cold.2
+ ___121-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:]_block_invoke.cold.3
+ ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.303
+ ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.244
+ ___23+[EDSQLQueryLogger log]_block_invoke
+ ___25-[EDThreadMigrator start]_block_invoke.8
+ ___27+[EDMailboxPersistence log]_block_invoke
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.1
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.2
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.3
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.4
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.5
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.6
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.7
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.8
+ ___38-[EDSQLQueryLogger submitQueryLogData]_block_invoke.cold.9
+ ___39-[EDSQLQueryLogger _sortQueryCountDict]_block_invoke
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.221
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.224
+ ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke_2.223
+ ___42-[EDThreadMigrator addObjectIDsToMigrate:]_block_invoke.32
+ ___43+[EDOTCKeywords localizedExpressionStrings]_block_invoke.20
+ ___43+[EDOTCKeywords localizedExpressionStrings]_block_invoke_2
+ ___45-[EDThreadMigrator changeObjectIDsToMigrate:]_block_invoke.34
+ ___45-[EDThreadMigrator deleteObjectIDsToMigrate:]_block_invoke.36
+ ___47-[EDThreadPersistence endMigratingThreadScope:]_block_invoke
+ ___49-[EDThreadPersistence beginMigratingThreadScope:]_block_invoke_2
+ ___50-[EDMailboxPersistenceStatistics debugDescription]_block_invoke
+ ___50-[EDMailboxPersistenceStatistics debugDescription]_block_invoke_2
+ ___50-[EDMailboxPersistenceStatistics debugDescription]_block_invoke_3
+ ___50-[EDMailboxPersistenceStatistics debugDescription]_block_invoke_4
+ ___52-[EDSearchableIndex setDataSourceIndexingPermitted:]_block_invoke_2
+ ___52-[EDThreadMigrator _migrateNextBatchWithGeneration:]_block_invoke.13
+ ___53-[EDMailboxPersistenceStatistics redactedDescription]_block_invoke
+ ___53-[EDMailboxPersistenceStatistics redactedDescription]_block_invoke_2
+ ___53-[EDMailboxPersistenceStatistics redactedDescription]_block_invoke_3
+ ___53-[EDMailboxPersistenceStatistics redactedDescription]_block_invoke_4
+ ___54-[EDThreadPersistence verifyConsistencyOfThreadScope:]_block_invoke.438
+ ___60-[EDMailboxPersistence _startReportingPersistenceStatistics]_block_invoke
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.70
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.70.cold.1
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.72
+ ___61-[EDReadLaterPersistence _persistReadLater:date:displayDate:]_block_invoke
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.307
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.312
+ ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.315
+ ___63+[EDDataDetectionUtilities detectOneTimeCodeWithDataDetectors:]_block_invoke
+ ___64-[EDPersistenceDatabase _scheduleProcessSQLQueryPerformanceData]_block_invoke
+ ___64-[EDPersistenceDatabase _scheduleProcessSQLQueryPerformanceData]_block_invoke_2
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.194
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.240
+ ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.222
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.339
+ ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.339.cold.1
+ ___72-[EDMessageChangeManager _persistFlagChangeResults:forFlagChangeAction:]_block_invoke.125
+ ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.104
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.294
+ ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.295
+ ___83-[EDDiagnosticInfoGatherer searchableIndexDatabaseStatisticsWithCompletionHandler:]_block_invoke
+ ___84-[EDMessageChangeManager _applyReadLaterDate:displayDate:toMessages:changeIsRemote:]_block_invoke
+ ___84-[EDMessageChangeManager _applyReadLaterDate:displayDate:toMessages:changeIsRemote:]_block_invoke_2
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.287
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.287.cold.1
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.290
+ ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.291
+ ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88r96r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r88l8s64l8s72l8r96l8s80l8
+ ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88r96r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8s40l8s48l8s56l8r88l8s64l8s72l8r96l8s80l8
+ ___block_descriptor_112_ea8_32s40s48s56s64s72s80s88bs96r104r_e41_B16?0"EDPersistenceDatabaseConnection"8lr96l8s32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8r104l8
+ ___block_descriptor_32_e29_q24?0"NSArray"8"NSArray"16l
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_32_e55_q24?0"EDSQLQueryStatistics"8"EDSQLQueryStatistics"16l
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.119
+ ___block_literal_global.132
+ ___block_literal_global.137
+ ___block_literal_global.141
+ ___block_literal_global.17
+ ___block_literal_global.213
+ ___block_literal_global.248
+ ___block_literal_global.25
+ ___block_literal_global.263
+ ___block_literal_global.272
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.332
+ ___block_literal_global.338
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.413
+ ___block_literal_global.415
+ ___block_literal_global.436
+ ___block_literal_global.44
+ ___block_literal_global.46
+ ___block_literal_global.789
+ ___block_literal_global.791
+ ___block_literal_global.852
+ ___block_literal_global.854
+ ___block_literal_global.88
+ ___block_literal_global.891
+ __unnamed_array_storage.104
+ __unnamed_array_storage.95
+ _kBucketValues
+ _kRandomSelectionPercentage
+ _kSelectionPercentage
+ _objc_msgSend$_applyReadLaterDate:displayDate:toMessages:changeIsRemote:
+ _objc_msgSend$_bucketTransactionLabels:
+ _objc_msgSend$_createFileIfNeeded:
+ _objc_msgSend$_createQueryCountDict:
+ _objc_msgSend$_createQueryCountLogFilePath
+ _objc_msgSend$_createQueryLogDirectoryPath
+ _objc_msgSend$_createQueryLogFilePath
+ _objc_msgSend$_createQueryStatisticsDictionary:queryCountByTransactionLabel:queryCountNum:firstRowExecutionTimeStats:totalExecutionTimeStats:timePerRowExecutionTimeStats:
+ _objc_msgSend$_keyForMessage:
+ _objc_msgSend$_persistDisplayDate:message:connection:
+ _objc_msgSend$_persistReadLater:date:displayDate:
+ _objc_msgSend$_preprocessQueryInfo
+ _objc_msgSend$_recreateFile:
+ _objc_msgSend$_removeFile:
+ _objc_msgSend$_reportPersistenceStatistics:
+ _objc_msgSend$_sortQueryCountDict
+ _objc_msgSend$_stopReportingPersistenceStatistics
+ _objc_msgSend$_writeQueryStatistics:
+ _objc_msgSend$addStatisticWithTransactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:
+ _objc_msgSend$applyReadLaterDate:displayDate:toMessages:
+ _objc_msgSend$backgroundProcessingIsAllowed
+ _objc_msgSend$bucketValueForQueryLogCount:bucketValues:
+ _objc_msgSend$compressedDataUsingAlgorithm:error:
+ _objc_msgSend$endMigratingThreadScope:
+ _objc_msgSend$firstRowMaxExecutionTime
+ _objc_msgSend$firstRowMinExecutionTime
+ _objc_msgSend$initWithFilePath:protectionType:
+ _objc_msgSend$initWithFilePaths:protectionType:
+ _objc_msgSend$initWithQuery:transactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:
+ _objc_msgSend$insertString:atIndex:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$mailboxesPerAccount
+ _objc_msgSend$messagesInLargestMailbox
+ _objc_msgSend$messagesInSecondLargestMailbox
+ _objc_msgSend$messagesPerAccount
+ _objc_msgSend$messagesPerInbox
+ _objc_msgSend$messagesPerMailbox
+ _objc_msgSend$migrationCancelable
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$persistReadLaterForMessage:date:displayDate:
+ _objc_msgSend$protectedDatabaseIsAvailable
+ _objc_msgSend$queryCount
+ _objc_msgSend$queryCountByTransactionLabel
+ _objc_msgSend$queryCountDict
+ _objc_msgSend$queryCountLogFilePath
+ _objc_msgSend$queryLogDirectoryPath
+ _objc_msgSend$queryLogFilePath
+ _objc_msgSend$queryStatisticsArray
+ _objc_msgSend$rawQueryLogInputFileHandle
+ _objc_msgSend$redactedQuery
+ _objc_msgSend$requestBackgroundProcessingForDuration:error:
+ _objc_msgSend$requestProtectedDatabaseBackgroundProcessingForDuration:error:
+ _objc_msgSend$roundedInteger:
+ _objc_msgSend$scanLocation
+ _objc_msgSend$scanUpToString:intoString:
+ _objc_msgSend$searchableIndexStatistics
+ _objc_msgSend$setMigrationCancelable:
+ _objc_msgSend$setRawQueryLogInputFileHandle:
+ _objc_msgSend$setScanLocation:
+ _objc_msgSend$setStatisticsReportingScheduler:
+ _objc_msgSend$statisticsReportingScheduler
+ _objc_msgSend$submitQueryLogData
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$timePerRowMaxExecutionTime
+ _objc_msgSend$timePerRowMinExecutionTime
+ _objc_msgSend$totalMaxExecutionTime
+ _objc_msgSend$totalMinExecutionTime
+ _objc_msgSend$urlFileProtectionTypeForDatabaseType:
+ _objc_msgSend$writeToFile:options:error:
- -[EDMessageChangeManager _applyReadLaterDate:toMessages:changeIsRemote:]
- -[EDMessageChangeManager applyReadLaterDate:toMessages:]
- -[EDMessagePersistenceStatistics attachmentsIndexed]
- -[EDMessagePersistenceStatistics attachmentsToIndex]
- -[EDMessagePersistenceStatistics indexableAttachments]
- -[EDMessagePersistenceStatistics indexableMessages]
- -[EDMessagePersistenceStatistics setAttachmentsIndexed:]
- -[EDMessagePersistenceStatistics setAttachmentsToIndex:]
- -[EDMessagePersistenceStatistics setIndexableAttachments:]
- -[EDMessagePersistenceStatistics setIndexableMessages:]
- -[EDPersistenceDatabase fileProtectionForDatabaseType:]
- -[EDPersistenceDatabaseConnection protectedDatabasePath]
- -[EDReadLaterCloudStorage _keyFormessage:]
- -[EDReadLaterCloudStorage addEntryForMessage:date:].cold.1
- -[EDReadLaterCloudStorage addEntryForMessage:date:].cold.2
- -[EDReadLaterCloudStorage updateDisplayDateForMessage:displayDate:].cold.1
- -[EDReadLaterPersistence _persistReadLater:date:]
- -[EDReadLaterPersistence _resetDisplayDateForMessage:connection:]
- -[EDReadLaterPersistence persistReadLaterForMessage:date:]
- -[EDSQLQueryLogger _createFileHandle]
- -[EDSQLQueryLogger _createQueryInfoFilePath]
- -[EDSQLQueryLogger _saveSQLQueryInfo:]
- -[EDSQLQueryLogger fileHandle]
- -[EDSQLQueryLogger logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:]
- -[EDSQLQueryLogger queryInfoFilePath]
- -[EDSQLQueryLogger setFileHandle:]
- -[EDSQLQueryLogger setQueryInfoFilePath:]
- -[EDSenderPersistence _addNewSender:toBucket:connection:]
- -[EDThreadPersistence endMigratingThreadScope:wasCanceledOrReset:]
- -[EDThreadPersistence endMigratingThreadScope:wasCanceledOrReset:].cold.1
- GCC_except_table257
- GCC_except_table258
- GCC_except_table289
- GCC_except_table295
- GCC_except_table296
- GCC_except_table300
- GCC_except_table301
- GCC_except_table305
- _EDPersistenceProtectedDatabaseFilename
- _OBJC_IVAR_$_EDMessagePersistenceStatistics._attachmentsIndexed
- _OBJC_IVAR_$_EDMessagePersistenceStatistics._attachmentsToIndex
- _OBJC_IVAR_$_EDMessagePersistenceStatistics._indexableAttachments
- _OBJC_IVAR_$_EDMessagePersistenceStatistics._indexableMessages
- _OBJC_IVAR_$_EDSQLQueryLogger._fileHandle
- _OBJC_IVAR_$_EDSQLQueryLogger._queryInfoFilePath
- __OBJC_$_PROTOCOL_CLASS_METHODS__SGSuggestionsServiceBaseProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SGSuggestionsServiceMailProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceBaseProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceContactsConfirmRejectProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceContactsObserverProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceEventsConfirmRejectProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceEventsObserverProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceMailIntelligenceProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SGSuggestionsServiceMetricsProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SGSuggestionsServiceMailProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceBaseProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceContactsConfirmRejectProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceContactsObserverProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceEventsConfirmRejectProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceEventsObserverProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceMailIntelligenceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES__SGSuggestionsServiceMetricsProtocol
- __OBJC_$_PROTOCOL_REFS_SGSuggestionsServiceMailProtocol
- __OBJC_$_PROTOCOL_REFS__SGSuggestionsServiceBaseProtocol
- __OBJC_LABEL_PROTOCOL_$_SGSuggestionsServiceMailProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceBaseProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceContactsConfirmRejectProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceContactsObserverProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceEventsConfirmRejectProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceEventsObserverProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceMailIntelligenceProtocol
- __OBJC_LABEL_PROTOCOL_$__SGSuggestionsServiceMetricsProtocol
- __OBJC_PROTOCOL_$_SGSuggestionsServiceMailProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceBaseProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceContactsConfirmRejectProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceContactsObserverProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceEventsConfirmRejectProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceEventsObserverProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceMailIntelligenceProtocol
- __OBJC_PROTOCOL_$__SGSuggestionsServiceMetricsProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SGSuggestionsServiceMailProtocol
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.342
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.342.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.344
- ___120-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortDescriptors:journaledThreadsToCheck:excluding:]_block_invoke.273
- ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.291
- ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.234
- ___25-[EDThreadMigrator start]_block_invoke.7
- ___42-[EDSearchableIndex _fetchLastClientState]_block_invoke.222
- ___42-[EDThreadMigrator addObjectIDsToMigrate:]_block_invoke.31
- ___43+[EDOTCKeywords localizedExpressionStrings]_block_invoke.12
- ___45-[EDThreadMigrator changeObjectIDsToMigrate:]_block_invoke.33
- ___45-[EDThreadMigrator deleteObjectIDsToMigrate:]_block_invoke.34
- ___49-[EDReadLaterPersistence _persistReadLater:date:]_block_invoke
- ___52-[EDThreadMigrator _migrateNextBatchWithGeneration:]_block_invoke.12
- ___54-[EDThreadPersistence verifyConsistencyOfThreadScope:]_block_invoke.437
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.60
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.60.cold.1
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.62
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.305
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.308
- ___61-[EDSearchableIndex _scheduleProcessPendingItemsFromRefresh:]_block_invoke.311
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.193
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.239
- ___66-[EDThreadPersistence endMigratingThreadScope:wasCanceledOrReset:]_block_invoke
- ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.212
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.337
- ___71-[EDSearchableIndex _processIndexingBatch:clientState:itemsNotIndexed:]_block_invoke.337.cold.1
- ___72-[EDMessageChangeManager _applyReadLaterDate:toMessages:changeIsRemote:]_block_invoke
- ___72-[EDMessageChangeManager _applyReadLaterDate:toMessages:changeIsRemote:]_block_invoke_2
- ___72-[EDMessageChangeManager _persistFlagChangeResults:forFlagChangeAction:]_block_invoke.127
- ___79-[EDProtectedDatabasePersistence _mergeTable:connection:journaledRows:newRows:]_block_invoke.101
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.292
- ___79-[EDSearchableIndex _dataSourcePrepareToIndexItems:fromRefresh:withCompletion:]_block_invoke.293
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.285
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.285.cold.1
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.288
- ___84-[EDSearchableIndex _dataSourceRequestNeededUpdatesExcludingIdentifiers:completion:]_block_invoke.289
- ___95-[EDSQLQueryLogger logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:]_block_invoke
- ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88r96r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8r88l8s56l8s64l8r96l8s72l8s80l8
- ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88r96r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8s40l8s48l8r88l8s56l8s64l8r96l8s72l8s80l8
- ___block_descriptor_96_ea8_32s40s48s56s64s72s80r88r_e41_B16?0"EDPersistenceDatabaseConnection"8lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
- ___block_literal_global.1000
- ___block_literal_global.1036
- ___block_literal_global.121
- ___block_literal_global.139
- ___block_literal_global.143
- ___block_literal_global.170
- ___block_literal_global.261
- ___block_literal_global.270
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.310
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.327
- ___block_literal_global.334
- ___block_literal_global.340
- ___block_literal_global.344
- ___block_literal_global.370
- ___block_literal_global.569
- ___block_literal_global.571
- ___block_literal_global.776
- ___block_literal_global.778
- ___block_literal_global.86
- ___block_literal_global.998
- _objc_msgSend$_applyReadLaterDate:toMessages:changeIsRemote:
- _objc_msgSend$_createFileHandle
- _objc_msgSend$_createQueryInfoFilePath
- _objc_msgSend$_keyFormessage:
- _objc_msgSend$_persistReadLater:date:
- _objc_msgSend$_resetDisplayDateForMessage:connection:
- _objc_msgSend$_saveSQLQueryInfo:
- _objc_msgSend$applyReadLaterDate:toMessages:
- _objc_msgSend$contactIdentifier
- _objc_msgSend$endMigratingThreadScope:wasCanceledOrReset:
- _objc_msgSend$fileHandle
- _objc_msgSend$fileProtectionForDatabaseType:
- _objc_msgSend$persistReadLaterForMessage:date:
- _objc_msgSend$queryInfoFilePath
- _objc_msgSend$seekToEndReturningOffset:error:
- _objc_msgSend$setDatabaseID:
- _protocol_getMethodDescription
CStrings:
+ "\x01\x11\x1f\n\x15"
+ "\x01\x12\x19"
+ "\t%@: %@\n"
+ "\t%@: %ld\n"
+ "\t%@: %lu\n"
+ "\x1c"
+ "-[EDMailboxPersistence mailboxDatabaseIDsForMailboxURLStrings:]"
+ "-[EDMailboxPersistence statistics]"
+ "-[EDMessageChangeManager _applyReadLaterDate:displayDate:toMessages:changeIsRemote:]"
+ "-[EDPersistence searchableIndexStatistics]"
+ "-[EDReadLaterPersistence _persistReadLater:date:displayDate:]"
+ "-[EDThreadPersistence endMigratingThreadScope:]"
+ "<id=%lld, subject=%@, displayDate=%@, readLater=%@>"
+ "@\"<EFProtectedFile>\""
+ "@32@0:8d16^@24"
+ "@64@0:8@16@24Q32@40@48@56"
+ "@64@0:8q16q24@32@40@48@56"
+ "An existing display date (%{public}@) already exists for message: %{public}@, key: %{public}@"
+ "Applying new read later date due to remote change for messages with global message id: %lld, new read later date: %{public}@, old read later date: %{public}@, new display date: %{public}@, old display date: %{public}@"
+ "Collected mailbox persistence statistics.\n%@"
+ "Detected empty query log"
+ "EDMailboxPersistenceStatistics"
+ "EDSQLQueryStatistics"
+ "Failed to compress file at %@ due to error: %{public}@"
+ "Failed to convert query statistics array to NSData due to error: %{public}@"
+ "Failed to convert raw log to json data: %{public}@"
+ "Failed to create directory at path: %@"
+ "Failed to create valid key for the query count dictionary"
+ "Failed to find query log file at file path: %@"
+ "Failed to find valid query for log line: %@"
+ "Failed to read query log file at file path: %@"
+ "Failed to remove processed file at %@ due to error: %{public}@"
+ "Failed to rename file from: %@ to %@ due to error: %{public}@"
+ "Failed to submit logs to diagnostic pipeline %{public}@"
+ "Failed to write raw log: %{public}@"
+ "Failed to write to file with compressed data at %@ due to error: %{public}@"
+ "Finishing because indexing is disabled"
+ "Found %lu potential codes, filtered down to %lu codes."
+ "Largest mailbox: %@ messages\n"
+ "Largest mailbox: %ld messages\n"
+ "Logs"
+ "MailSQLQueryPerformance"
+ "Mailboxes per account:\n"
+ "Mapping subjectID %{public}@ to %{public}@"
+ "Messages per account:\n"
+ "Messages per inbox:\n"
+ "Messages per mailbox:\n"
+ "Nil searchableItem for item: %@"
+ "QueryPerformance"
+ "Remove file failed in the middle of preprocessing: %@"
+ "Second Largest mailbox: %@ messages\n"
+ "Second Largest mailbox: %ld messages\n"
+ "Setting read later date=%{public}@, displayDate=%{public}@ on %lu messages, changeIsRemote:%{BOOL}d"
+ "Skipping one-time code with length %ld"
+ "Starting to report mailbox persistence statistics."
+ "Stopping to report mailbox persistence statistics."
+ "T@\"<EFAssertableScheduler>\",R,N,V_queryLoggingScheduler"
+ "T@\"<EFCancelable>\",&,N,V_migrationCancelable"
+ "T@\"EDMailboxPersistenceStatistics\",R,N"
+ "T@\"NSBackgroundActivityScheduler\",&,N,V_statisticsReportingScheduler"
+ "T@\"NSDictionary\",R,&,N,V_mailboxesPerAccount"
+ "T@\"NSDictionary\",R,&,N,V_messagesPerAccount"
+ "T@\"NSDictionary\",R,&,N,V_messagesPerInbox"
+ "T@\"NSDictionary\",R,&,N,V_messagesPerMailbox"
+ "T@\"NSDictionary\",R,N,V_queryCountByTransactionLabel"
+ "T@\"NSFileHandle\",&,N,V_rawQueryLogInputFileHandle"
+ "T@\"NSMutableArray\",&,N,V_queryStatisticsArray"
+ "T@\"NSMutableDictionary\",&,N,V_queryCountDict"
+ "T@\"NSString\",&,N,V_queryCountLogFilePath"
+ "T@\"NSString\",&,N,V_queryLogDirectoryPath"
+ "T@\"NSString\",&,N,V_queryLogFilePath"
+ "T@\"NSString\",R,C,N,V_protectedDatabasePath"
+ "T@\"NSString\",R,N,V_redactedQuery"
+ "TQ,R,N,V_firstRowEightyPercentileExecutionTime"
+ "TQ,R,N,V_firstRowMaxExecutionTime"
+ "TQ,R,N,V_firstRowMeanExecutionTime"
+ "TQ,R,N,V_firstRowMinExecutionTime"
+ "TQ,R,N,V_firstRowTwentyPercentileExecutionTime"
+ "TQ,R,N,V_queryCount"
+ "TQ,R,N,V_timePerRowEightyPercentileExecutionTime"
+ "TQ,R,N,V_timePerRowMaxExecutionTime"
+ "TQ,R,N,V_timePerRowMeanExecutionTime"
+ "TQ,R,N,V_timePerRowMinExecutionTime"
+ "TQ,R,N,V_timePerRowTwentyPercentileExecutionTime"
+ "TQ,R,N,V_totalEightyPercentileExecutionTime"
+ "TQ,R,N,V_totalMaxExecutionTime"
+ "TQ,R,N,V_totalMeanExecutionTime"
+ "TQ,R,N,V_totalMinExecutionTime"
+ "TQ,R,N,V_totalTwentyPercentileExecutionTime"
+ "Tq,R,N,V_messagesInLargestMailbox"
+ "Tq,R,N,V_messagesInSecondLargestMailbox"
+ "Transaction label is nil"
+ "Unable to request background processing assertion: %{public}@"
+ "Updating display date for message: id=%lld, subject=%{public}@, displayDate=%{public}@, remindMe=%{public}@, potentialDate=%{public}@"
+ "Updating read later date"
+ "_applyReadLaterDate:displayDate:toMessages:changeIsRemote:"
+ "_backgroundProcessingAssertionsByMigratingThreadScope"
+ "_bucketTransactionLabels:"
+ "_createFileIfNeeded:"
+ "_createQueryCountDict:"
+ "_createQueryCountLogFilePath"
+ "_createQueryLogDirectoryPath"
+ "_createQueryLogFilePath"
+ "_createQueryStatisticsDictionary:queryCountByTransactionLabel:queryCountNum:firstRowExecutionTimeStats:totalExecutionTimeStats:timePerRowExecutionTimeStats:"
+ "_firstRowEightyPercentileExecutionTime"
+ "_firstRowMaxExecutionTime"
+ "_firstRowMeanExecutionTime"
+ "_firstRowMinExecutionTime"
+ "_firstRowTwentyPercentileExecutionTime"
+ "_keyForMessage:"
+ "_mailboxesPerAccount"
+ "_messagesInLargestMailbox"
+ "_messagesInSecondLargestMailbox"
+ "_messagesPerAccount"
+ "_messagesPerInbox"
+ "_messagesPerMailbox"
+ "_migrationCancelable"
+ "_persistDisplayDate:message:connection:"
+ "_persistReadLater:date:displayDate:"
+ "_preprocessQueryInfo"
+ "_processing"
+ "_protectedDatabaseFile"
+ "_protectedDatabasePath"
+ "_queryCount"
+ "_queryCountByTransactionLabel"
+ "_queryCountDict"
+ "_queryCountLogFilePath"
+ "_queryLogDirectoryPath"
+ "_queryLogFilePath"
+ "_queryStatisticsArray"
+ "_rawQueryLogInputFileHandle"
+ "_recreateFile:"
+ "_redactedQuery"
+ "_removeFile:"
+ "_reportPersistenceStatistics:"
+ "_sortQueryCountDict"
+ "_startReportingPersistenceStatistics"
+ "_statisticsReportingScheduler"
+ "_stopReportingPersistenceStatistics"
+ "_timePerRowEightyPercentileExecutionTime"
+ "_timePerRowMaxExecutionTime"
+ "_timePerRowMeanExecutionTime"
+ "_timePerRowMinExecutionTime"
+ "_timePerRowTwentyPercentileExecutionTime"
+ "_totalEightyPercentileExecutionTime"
+ "_totalMaxExecutionTime"
+ "_totalMeanExecutionTime"
+ "_totalMinExecutionTime"
+ "_totalTwentyPercentileExecutionTime"
+ "_writeQueryStatistics:"
+ "addStatisticWithTransactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:"
+ "applyReadLaterDate:displayDate:toMessages:"
+ "backgroundProcessingIsAllowed"
+ "bucketValueForQueryLogCount:bucketValues:"
+ "com.apple.email.ProcessSQLQueryPerformanceData"
+ "com.apple.mail.mailboxPersistence.statisticsReportingScheduler"
+ "com.apple.mail.oneTimeCodes"
+ "compressedDataUsingAlgorithm:error:"
+ "endMigratingThreadScope:"
+ "expressions"
+ "filled"
+ "firstRowEightyPercentileExecutionTime"
+ "firstRowExecutionTimeStats"
+ "firstRowMaxExecutionTime"
+ "firstRowMeanExecutionTime"
+ "firstRowMinExecutionTime"
+ "firstRowTwentyPercentileExecutionTime"
+ "initWithFilePath:protectionType:"
+ "initWithFilePaths:protectionType:"
+ "initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:messagesPerInbox:"
+ "initWithQuery:transactionLabel:firstRowExecutionTime:timePerRowExecutionTime:totalExecutionTime:"
+ "insertString:atIndex:"
+ "json.compressed"
+ "keysSortedByValueUsingComparator:"
+ "logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:"
+ "mailboxDatabaseIDsForMailboxURLStrings:"
+ "mailboxesPerAccount"
+ "messagesInLargestMailbox"
+ "messagesInSecondLargestMailbox"
+ "messagesPerAccount"
+ "messagesPerInbox"
+ "messagesPerMailbox"
+ "migrationCancelable"
+ "moveItemAtPath:toPath:error:"
+ "no-word-boundaries"
+ "oneTimeCodeEvent"
+ "persistReadLaterForMessage:date:displayDate:"
+ "plainText"
+ "protectedDatabaseIsAvailable"
+ "q24@?0@\"EDSQLQueryStatistics\"8@\"EDSQLQueryStatistics\"16"
+ "q24@?0@\"NSArray\"8@\"NSArray\"16"
+ "queryCount"
+ "queryCountByTransactionLabel"
+ "queryCountDict"
+ "queryCountLogFilePath"
+ "queryCountLogs_"
+ "queryLogDirectoryPath"
+ "queryLogFilePath"
+ "queryLogs"
+ "queryStatisticsArray"
+ "queryStatisticsArray is nil"
+ "rawQueryLogInputFileHandle"
+ "redactedDescription"
+ "requestBackgroundProcessingForDuration:error:"
+ "requestProtectedDatabaseBackgroundProcessingForDuration:error:"
+ "roundedInteger:"
+ "scanLocation"
+ "scanUpToString:intoString:"
+ "searchableIndexDatabaseStatisticsWithCompletionHandler:"
+ "searchableIndexStatistics"
+ "setMigrationCancelable:"
+ "setQueryCountDict:"
+ "setQueryCountLogFilePath:"
+ "setQueryLogDirectoryPath:"
+ "setQueryLogFilePath:"
+ "setQueryStatisticsArray:"
+ "setRawQueryLogInputFileHandle:"
+ "setScanLocation:"
+ "setStatisticsReportingScheduler:"
+ "statisticsReportingScheduler"
+ "submitQueryLogData"
+ "substringFromIndex:"
+ "timePerRowEightyPercentileExecutionTime"
+ "timePerRowExecutionTimeStats"
+ "timePerRowMaxExecutionTime"
+ "timePerRowMeanExecutionTime"
+ "timePerRowMinExecutionTime"
+ "timePerRowTwentyPercentileExecutionTime"
+ "totalEightyPercentileExecutionTime"
+ "totalExecutionTimeStats"
+ "totalMaxExecutionTime"
+ "totalMeanExecutionTime"
+ "totalMinExecutionTime"
+ "totalTwentyPercentileExecutionTime"
+ "unnamed transaction"
+ "urlFileProtectionTypeForDatabaseType:"
+ "v56@0:8@\"NSString\"16@\"NSString\"24Q32Q40Q48"
+ "v56@0:8@16@24Q32Q40Q48"
+ "writeToFile:options:error:"
+ "}"
+ "}{"
+ "\xf0\xe1"
- "\x01\x11\x19"
- "\x01\x11\x1f\t\x15"
- "\x1a"
- "-[EDMessageChangeManager _applyReadLaterDate:toMessages:changeIsRemote:]"
- "-[EDProtectedDatabasePersistence protectedDataAvailable]"
- "-[EDReadLaterPersistence _persistReadLater:date:]"
- "-[EDThreadPersistence endMigratingThreadScope:wasCanceledOrReset:]"
- "@\"NSArray\"40@0:8@\"CSSearchableItem\"16Q24^@32"
- "@\"NSArray\"40@0:8@\"NSString\"16q24^@32"
- "@\"NSArray\"40@0:8q16Q24^@32"
- "@\"NSArray\"56@0:8q16Q24d32Q40^@48"
- "@\"NSArray\"60@0:8@\"NSArray\"16@\"NSArray\"24@\"NSDate\"32B40Q44^@52"
- "@\"NSArray\"96@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSArray\"64@\"NSArray\"72@\"NSArray\"80^@88"
- "@\"NSNumber\"36@0:8B16@\"SGMailIntelligenceWarning\"20^@28"
- "@\"NSNumber\"36@0:8B16q20^@28"
- "@\"NSNumber\"40@0:8q16@\"NSString\"24^@32"
- "@\"SGMailIntelligenceFollowUpWarning\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32^@40"
- "@\"SGMailIntelligenceSaliency\"32@0:8@\"NSData\"16^@24"
- "@\"SGMailIntelligenceSaliency\"32@0:8@\"SGMailHeaders\"16^@24"
- "@24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
- "@36@0:8B16@20^@28"
- "@36@0:8B16q20^@28"
- "@40@0:8@16Q24^@32"
- "@40@0:8q16@24^@32"
- "@40@0:8q16Q24^@32"
- "@56@0:8q16Q24d32Q40^@48"
- "@60@0:8@16@24@32B40Q44^@52"
- "@96@0:8@16@24@32@40@48@56@64@72@80^@88"
- "An existing display date already exists for message: %{public}@, key: %{public}@"
- "Applying new display date due to remote change for messages with global message id: %lld, new display date: %{public}@, old display date: %{public}@"
- "Applying new read later date due to remote change for messages with global message id: %lld, new read later date: %{public}@, old read later date: %{public}@"
- "B24@0:8^@16"
- "B32@0:8@\"SGRecordId\"16^@24"
- "B36@0:8@\"SGRecordId\"16i24^@28"
- "B36@0:8@16i24^@28"
- "B40@0:8q16@\"NSArray\"24^@32"
- "B40@0:8q16@24^@32"
- "Logs/queryInfo"
- "Nil searchableItem for item:%{public}@"
- "SGSuggestionsServiceMailProtocol"
- "Setting read later date %{public}@ on %lu messages changeIsRemote:%{BOOL}d"
- "T@\"<EFScheduler>\",R,N,V_queryLoggingScheduler"
- "T@\"NSFileHandle\",&,N,V_fileHandle"
- "T@\"NSString\",&,N,V_queryInfoFilePath"
- "TQ,N,V_attachmentsIndexed"
- "TQ,N,V_attachmentsToIndex"
- "TQ,N,V_indexableAttachments"
- "TQ,N,V_indexableMessages"
- "_SGSuggestionsServiceBaseProtocol"
- "_SGSuggestionsServiceContactsConfirmRejectProtocol"
- "_SGSuggestionsServiceContactsObserverProtocol"
- "_SGSuggestionsServiceEventsConfirmRejectProtocol"
- "_SGSuggestionsServiceEventsObserverProtocol"
- "_SGSuggestionsServiceMailIntelligenceProtocol"
- "_SGSuggestionsServiceMetricsProtocol"
- "_addNewSender:toBucket:connection:"
- "_applyReadLaterDate:toMessages:changeIsRemote:"
- "_attachmentsIndexed"
- "_attachmentsToIndex"
- "_createFileHandle"
- "_createQueryInfoFilePath"
- "_fileHandle"
- "_indexableAttachments"
- "_indexableMessages"
- "_keyFormessage:"
- "_persistReadLater:date:"
- "_queryInfoFilePath"
- "_resetDisplayDateForMessage:connection:"
- "_saveSQLQueryInfo:"
- "applyReadLaterDate:toMessages:"
- "attachmentsIndexed"
- "attachmentsToIndex"
- "confirmContact:withCompletion:"
- "confirmContactDetailRecord:confirmationUI:error:"
- "confirmContactDetailRecord:confirmationUI:withCompletion:"
- "confirmContactDetailRecord:error:"
- "confirmContactDetailRecord:withCompletion:"
- "confirmEvent:withCompletion:"
- "confirmEventByRecordId:error:"
- "confirmEventByRecordId:withCompletion:"
- "confirmRecord:error:"
- "confirmRecord:withCompletion:"
- "contactIdentifier"
- "deleteEventByRecordId:error:"
- "deleteEventByRecordId:withCompletion:"
- "deregisterContactsChangeObserverWithToken:"
- "deregisterEventsChangeObserverWithToken:"
- "dissectAttachmentsFromSearchableItem:options:error:"
- "endMigratingThreadScope:wasCanceledOrReset:"
- "fileHandle"
- "fileProtectionForDatabaseType:"
- "fullDownloadRequestBatch:withCompletion:"
- "harvestedSuggestionsFromSearchableItem:options:withCompletion:"
- "identifyComposeWarningsFromSubject:content:attributes:toRecipients:ccRecipients:bccRecipients:originalToRecipients:originalCcRecipients:attachments:error:"
- "identifyFollowUpWarningFromSubject:body:date:error:"
- "indexableAttachments"
- "indexableMessages"
- "isEnabledWithError:"
- "isHarvestingSupported"
- "keepDirty:"
- "logEventInteractionForEventWithExternalIdentifier:interface:actionType:"
- "logEventInteractionForEventWithUniqueKey:interface:actionType:"
- "logMetricAutocompleteResult:recordId:contactIdentifier:bundleId:"
- "logMetricAutocompleteUserSelectedRecordId:contactIdentifier:bundleId:"
- "logMetricContactCreated:contactIdentifier:bundleId:"
- "logMetricContactSearchResult:recordId:contactIdentifier:bundleId:"
- "logMetricContactSearchResultSelected:contactIdentifier:bundleId:"
- "logMetricSearchResultsIncludedPureSuggestionWithBundleId:"
- "logMetricSuggestedContactDetailShown:contactIdentifier:bundleId:"
- "logMetricSuggestedContactDetailUsed:contactIdentifier:bundleId:"
- "logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:"
- "logSuggestionInteractionForRecordId:interface:actionType:"
- "messagesToRefreshWithCompletion:"
- "persistReadLaterForMessage:date:"
- "prepareForRealtimeExtraction:"
- "prepareForRealtimeExtractionWithCompletion:"
- "preventUnsubscriptionOpportunitiesSuggestionsForField:toValues:error:"
- "preventUnsubscriptionOpportunitiesSuggestionsForField:toValues:withCompletion:"
- "queryInfoFilePath"
- "queuesRequestsIfBusy"
- "registerContactsChangeObserver:"
- "registerEventsChangeObserver:"
- "rejectContact:rejectionUI:withCompletion:"
- "rejectContact:withCompletion:"
- "rejectContactDetailRecord:error:"
- "rejectContactDetailRecord:rejectionUI:error:"
- "rejectContactDetailRecord:rejectionUI:withCompletion:"
- "rejectContactDetailRecord:withCompletion:"
- "rejectEvent:withCompletion:"
- "rejectEventByRecordId:error:"
- "rejectEventByRecordId:withCompletion:"
- "rejectRecord:error:"
- "rejectRecord:rejectionUI:error:"
- "rejectRecord:rejectionUI:withCompletion:"
- "rejectRecord:withCompletion:"
- "reportMessagesFound:lost:withCompletion:"
- "reportUserEngagement:forWarning:error:"
- "reportValue:forFeatureSetting:error:"
- "resolveFullDownloadRequests:withCompletion:"
- "saliencyFromEmailHeaders:error:"
- "saliencyFromEmailHeaders:withCompletion:"
- "saliencyFromRFC822Data:error:"
- "saliencyFromRFC822Data:withCompletion:"
- "seekToEndReturningOffset:error:"
- "setAttachmentsIndexed:"
- "setAttachmentsToIndex:"
- "setDatabaseID:"
- "setFileHandle:"
- "setIndexableAttachments:"
- "setIndexableMessages:"
- "setQueryInfoFilePath:"
- "setQueuesRequestsIfBusy:"
- "sortedUnsubscriptionOpportunitiesForField:limit:error:"
- "suggestionsFromSearchableItem:options:processingType:withCompletion:"
- "suggestionsFromSearchableItem:options:withCompletion:"
- "syncTimeout"
- "topSalienciesForMailboxId:limit:error:"
- "updateMessages:state:withCompletion:"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"SGMailIntelligenceSaliency\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16S24S28"
- "v32@0:8@\"SGMailHeaders\"16@?<v@?@\"SGMailIntelligenceSaliency\"@\"NSError\">24"
- "v32@0:8@\"SGRealtimeContact\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"SGRealtimeEvent\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"SGRecordId\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"SGRecordId\"16S24S28"
- "v32@0:8@16S24S28"
- "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v36@0:8@\"SGRealtimeContact\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@\"SGRecordId\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"CSSearchableItem\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDate\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"SGRecordId\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8q16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v44@0:8i16@\"SGRecordId\"20@\"NSString\"28@\"NSString\"36"
- "v44@0:8i16@20@28@36"
- "v48@0:8@\"CSSearchableItem\"16Q24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16Q24Q32@?40"
- "v56@0:8@\"NSString\"16@\"NSString\"24d32d40Q48"
- "v56@0:8@16@24d32d40Q48"
- "waitForEventWithIdentifier:toAppearInEventStoreWithCompletion:"
- "waitForEventWithIdentifier:toAppearInEventStoreWithLastModificationDate:completion:"
- "\xf0\xd1"

```
