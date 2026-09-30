## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/Versions/A/CloudDocsDaemon`

```diff

-3097.0.148.0.1
-  __TEXT.__text: 0x382dc8
+3097.0.187.0.4
+  __TEXT.__text: 0x382e28
   __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_methlist: 0x17d18
-  __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x7d914
-  __TEXT.__oslogstring: 0x44ddf
-  __TEXT.__gcc_except_tab: 0x1da2c
+  __TEXT.__objc_methlist: 0x17d38
+  __TEXT.__const: 0x538
+  __TEXT.__cstring: 0x7da56
+  __TEXT.__oslogstring: 0x44d3b
+  __TEXT.__gcc_except_tab: 0x1da04
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x9530
-  __TEXT.__objc_classname: 0x248e
-  __TEXT.__objc_methname: 0x40125
-  __TEXT.__objc_methtype: 0x875e
-  __TEXT.__objc_stubs: 0x2bde0
+  __TEXT.__unwind_info: 0x9538
+  __TEXT.__objc_classname: 0x2490
+  __TEXT.__objc_methname: 0x4027c
+  __TEXT.__objc_methtype: 0x873b
+  __TEXT.__objc_stubs: 0x2be40
   __DATA_CONST.__got: 0x16c0
   __DATA_CONST.__const: 0x1c60
   __DATA_CONST.__objc_classlist: 0x920
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb10
+  __DATA_CONST.__objc_selrefs: 0xdb50
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x828
   __DATA_CONST.__objc_arraydata: 0xe38
   __AUTH_CONST.__auth_got: 0xe18
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0xa3f0
-  __AUTH_CONST.__cfstring: 0x21140
-  __AUTH_CONST.__objc_const: 0x3eb30
-  __AUTH_CONST.__objc_intobj: 0xa08
+  __AUTH_CONST.__const: 0xa3c0
+  __AUTH_CONST.__cfstring: 0x21100
+  __AUTH_CONST.__objc_const: 0x3eb40
+  __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x5780
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2068
+  __DATA.__objc_ivar: 0x206c
   __DATA.__data: 0x2410
   __DATA.__bss: 0x558
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13553
-  Symbols:   29221
-  CStrings:  7574
+  Functions: 13550
+  Symbols:   29228
+  CStrings:  7578
 
Symbols:
+ +[CKPackage(BRCAdvancedDataProtectionAdditions) br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:error:]
+ -[BRCAccountSession(BRCDatabaseManager) _appLibraryByName:db:]
+ -[BRCAccountSession(BRCDatabaseManager) _loadClientStateFromDB:].cold.5
+ -[BRCAccountSession(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:]
+ -[BRCClientState _prepareToSaveStateData]
+ -[BRCClientState _stateToData]
+ -[BRCClientState _stateToData].cold.1
+ -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]
+ -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:].cold.1
+ -[BRCClientState initWithDictionary:clientStateData:]
+ -[BRCPCSChainingOperation canSyncDownBeforeRetry]
+ -[BRCPCSChainingOperation setCanSyncDownBeforeRetry:]
+ -[BRCSaltingBatchOperation _createStructureRecordForParentItem]
+ -[BRCSaltingBatchOperation _createStructureRecordForParentItem].cold.1
+ -[BRCSaltingBatchOperation _createStructureRecordForParentItem].cold.2
+ -[BRCSaltingBatchOperation _createStructureRecordForParentItem].cold.3
+ -[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:]
+ -[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:].cold.1
+ -[BRCSaltingBatchOperation _saltChildRecordFields:serverItem:basehashSalt:]
+ -[BRCSaltingBatchOperation _saltChildRecordFields:serverItem:basehashSalt:].cold.1
+ -[BRCSaltingBatchOperation initWithParentItem:sessionContext:]
+ -[BRCSaltingBatchOperation initWithParentItem:sessionContext:].cold.1
+ -[BRCSaltingBatchOperation initWithParentItem:sessionContext:].cold.2
+ -[BRCThrottleBase isBlocking]
+ -[BRFetchRecordsOperation .cxx_destruct]
+ -[BRFetchRecordsOperation init]
+ -[BRFetchRecordsOperation setFetchRecordsCompletionBlock:]
+ -[NSError(BRCAdditions) brc_ckPartialErrorsByItemID]
+ -[NSError(BRCAdditions) brc_isCloudKitShouldBeUsingEnhancedDrivePrivacyWithFieldName:]
+ BRCGetAccountDSIDForMobileDocsRoot.cold.1
+ OBJC_IVAR_$_BRCClientState._needsSave
+ OBJC_IVAR_$_BRCClientState._originalState
+ OBJC_IVAR_$_BRCPCSChainingOperation._canSyncDownBeforeRetry
+ OBJC_IVAR_$_BRCSaltingBatchOperation._baseHashSaltValidationKey
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentClientZone
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentItemEncounteredValidationError
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentItemID
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentPluginFields
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentRecordID
+ OBJC_IVAR_$_BRCSaltingBatchOperation._parentSaltingState
+ OBJC_IVAR_$_BRFetchRecordsOperation._fetchRecordsCompletionBlock
+ _OBJC_CLASS_$_BRFetchRecordsOperation
+ _OBJC_METACLASS_$_BRFetchRecordsOperation
+ _OBJC_METACLASS_$_CKFetchRecordsOperation
+ __113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.401
+ __113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.404
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.275
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.275.cold.1
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.279
+ __22-[_BRCOperation start]_block_invoke.95
+ __22-[_BRCOperation start]_block_invoke.95.cold.1
+ __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke.617
+ __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke_2.618
+ __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke_3.619
+ __43-[_BRCOperation completedWithResult:error:]_block_invoke.114
+ __43-[_BRCOperation completedWithResult:error:]_block_invoke.115
+ __47-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke.2
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.1
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.2
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.3
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.4
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.5
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.6
+ __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.485
+ __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.489
+ __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.530
+ __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.556
+ __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.281
+ __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.281.cold.1
+ __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.165
+ __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.165.cold.1
+ __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.165.cold.2
+ __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.165.cold.3
+ __70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.123
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.34
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.36
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.35
+ __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.778
+ __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.782
+ __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.787
+ __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.787.cold.1
+ __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.789
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26.cold.1
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26.cold.2
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.339
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.339.cold.1
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.343
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.343.cold.1
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.356
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.356.cold.1
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.356.cold.2
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.357
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.cold.1
+ __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.cold.2
+ __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.711
+ __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.711.cold.1
+ __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.714
+ __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.446
+ __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.446.cold.1
+ __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.450
+ __OBJC_$_INSTANCE_METHODS_BRFetchRecordsOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRFetchRecordsOperation
+ __OBJC_CLASS_RO_$_BRFetchRecordsOperation
+ __OBJC_METACLASS_RO_$_BRFetchRecordsOperation
+ ___31-[BRFetchRecordsOperation init]_block_invoke
+ ___70-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]_block_invoke
+ ___77-[BRCDownloadContent _stageWithSession:manifest:package:xattrsPackage:error:]_block_invoke
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96s_e23_v16?0"PQLConnection"8l
+ ___block_descriptor_40_e8_32s_e32_v28?0"NSArray"8B16"NSError"20l
+ ___block_descriptor_41_e8_32s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e57_v36?0"BRCDocumentItem"8"BRCServerItem"16"NSData"24B32l
+ ___block_descriptor_92_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ __block_literal_global.160
+ __block_literal_global.1768
+ __block_literal_global.1780
+ __block_literal_global.1946
+ __block_literal_global.2111
+ __block_literal_global.2146
+ __block_literal_global.2157
+ __block_literal_global.231
+ __block_literal_global.2422
+ __block_literal_global.2437
+ __block_literal_global.2522
+ __block_literal_global.270
+ __block_literal_global.272
+ __block_literal_global.2736
+ __block_literal_global.360
+ __block_literal_global.385
+ __block_literal_global.400
+ __block_literal_global.414
+ __block_literal_global.419
+ __block_literal_global.436
+ __block_literal_global.452
+ __block_literal_global.457
+ __block_literal_global.462
+ __block_literal_global.467
+ __block_literal_global.472
+ __block_literal_global.477
+ __block_literal_global.482
+ __block_literal_global.487
+ __block_literal_global.495
+ __block_literal_global.500
+ __block_literal_global.505
+ __block_literal_global.533
+ __block_literal_global.810
+ _objc_msgSend$_createStructureRecordForParentItem
+ _objc_msgSend$_createStructureRecordWithRecordID:serverItem:
+ _objc_msgSend$_prepareToSaveStateData
+ _objc_msgSend$_saltChildRecordFields:serverItem:basehashSalt:
+ _objc_msgSend$_stateToData
+ _objc_msgSend$br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:error:
+ _objc_msgSend$br_setIOPolicy:type:forBlock:
+ _objc_msgSend$brc_ckPartialErrorsByItemID
+ _objc_msgSend$brc_isCloudKitShouldBeUsingEnhancedDrivePrivacyWithFieldName:
+ _objc_msgSend$hasStateChangesAndClearSaveStatusWithResultingState:
+ _objc_msgSend$initWithDictionary:clientStateData:
+ _objc_msgSend$initWithParentItem:sessionContext:
+ _objc_msgSend$newAppLibraryFromPQLResultSet:version:
+ _objc_msgSend$recordIDs
+ _objc_msgSend$setCanSyncDownBeforeRetry:
- +[CKPackage(BRCAdvancedDataProtectionAdditions) br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:signature:error:]
- -[BRCAccountSession(BRCDatabaseManager) _createSharedAppLibrary:]
- -[BRCAccountSession(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:error:]
- -[BRCClientState initWithDictionary:]
- -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.2
- -[BRCConstantThrottle incrementRetryCount:]
- -[BRCConstantThrottle initWithName:andRetryBackoff:]
- -[BRCConstantThrottle nsecsToNextRetry:now:increment:]
- -[BRCConstantThrottle nsecsToNextRetry:retryCount:now:]
- -[BRCConstantThrottle reset]
- -[BRCSaltingBatchOperation _createStructureRecordForRootItem]
- -[BRCSaltingBatchOperation _createStructureRecordForRootItem].cold.1
- -[BRCSaltingBatchOperation _createStructureRecordForRootItem].cold.2
- -[BRCSaltingBatchOperation _createStructureRecordForRootItem].cold.3
- -[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:basehashSalt:]
- -[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:basehashSalt:].cold.1
- -[BRCSaltingBatchOperation initWithRootItem:sessionContext:]
- -[BRCSaltingBatchOperation initWithRootItem:sessionContext:].cold.1
- -[BRCSaltingBatchOperation initWithRootItem:sessionContext:].cold.2
- -[BRCThrottleBase _initWithName:]
- -[BRCUserDefaults accountWaiterErrorRetryBackoff]
- -[BRCUserDefaults accountWaiterRefreshPacerDelay]
- -[CKRecord(BRCSerializationAdditions) processAppLibraryDataWithMovedZoneNames:serverZone:isDeltaSync:].cold.10
- -[NSError(BRCAdditions) brc_isCloudKitShouldBeUsingEnhancedDrivePrivacy]
- -[_BRCOperation _completedWithResult:error:].cold.2
- GCC_except_table139
- OBJC_IVAR_$_BRCAccountWaitOperation._refetchPacer
- OBJC_IVAR_$_BRCAccountWaitOperation._refetchPacerQueue
- OBJC_IVAR_$_BRCAccountWaitOperation._throttle
- OBJC_IVAR_$_BRCConstantThrottle._retryBackoff
- OBJC_IVAR_$_BRCSaltingBatchOperation._baseHashSaltValidation
- OBJC_IVAR_$_BRCSaltingBatchOperation._rootClientZone
- OBJC_IVAR_$_BRCSaltingBatchOperation._rootItemID
- OBJC_IVAR_$_BRCSaltingBatchOperation._rootPluginFields
- OBJC_IVAR_$_BRCSaltingBatchOperation._rootRecordID
- OBJC_IVAR_$_BRCSaltingBatchOperation._rootSaltingState
- _OBJC_CLASS_$_BRCConstantThrottle
- _OBJC_METACLASS_$_BRCConstantThrottle
- __113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.392
- __113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.395
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.276
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.276.cold.1
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.280
- __22-[_BRCOperation start]_block_invoke.92
- __22-[_BRCOperation start]_block_invoke.92.cold.1
- __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke.636
- __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke_2.637
- __43-[BRCSyncHealthReport telemetryErrorEvents]_block_invoke_3.638
- __43-[_BRCOperation completedWithResult:error:]_block_invoke.111
- __43-[_BRCOperation completedWithResult:error:]_block_invoke.112
- __47-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke.6
- __47-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke.9
- __47-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke.9.cold.1
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.1
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.2
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.3
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.4
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.5
- __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.33.cold.6
- __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.504
- __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.508
- __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.549
- __49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.575
- __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.282
- __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.282.cold.1
- __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.181
- __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.181.cold.1
- __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.181.cold.2
- __57+[BRCAnalyticsReporter _fetchIsTelemetryReportingEnabled]_block_invoke.181.cold.3
- __70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.120
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.35
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.37
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.36
- __74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.45.cold.6
- __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.797
- __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.801
- __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.805
- __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.805.cold.1
- __76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.807
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.27.cold.1
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.27.cold.2
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.28
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.329
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.329.cold.1
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.333
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.333.cold.1
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.346
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.346.cold.1
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.346.cold.2
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.347
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.351
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.351.cold.1
- __84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.351.cold.2
- __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.730
- __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.730.cold.1
- __95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.733
- __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.437
- __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.437.cold.1
- __96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.441
- __OBJC_$_INSTANCE_METHODS_BRCConstantThrottle
- __OBJC_$_INSTANCE_VARIABLES_BRCConstantThrottle
- __OBJC_CLASS_RO_$_BRCConstantThrottle
- __OBJC_METACLASS_RO_$_BRCConstantThrottle
- ___120-[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:enhancedDrivePrivacyEnabled:error:]_block_invoke
- ___120-[BRCAnalyticsReporter aggregateReportForAppTelemetryIdentifier:itemID:zoneMangledID:enhancedDrivePrivacyEnabled:error:]_block_invoke_2
- ___61-[BRCSyncHealthReport _collectAggregatedTelemetryForSession:]_block_invoke
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112s_e23_v16?0"PQLConnection"8l
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40w_e23_v16?0"PQLConnection"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_68_e8_32s40s48s56s_e23_B16?0"PQLConnection"8l
- ___block_descriptor_76_e8_32s40s48s56s64s_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e79_v52?0"BRCDocumentItem"8"BRCServerItem"16"NSData"24"NSData"32"NSData"40B48l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
- __block_literal_global.176
- __block_literal_global.1774
- __block_literal_global.1786
- __block_literal_global.1952
- __block_literal_global.2117
- __block_literal_global.2158
- __block_literal_global.2163
- __block_literal_global.225
- __block_literal_global.2428
- __block_literal_global.2443
- __block_literal_global.2528
- __block_literal_global.273
- __block_literal_global.2742
- __block_literal_global.275
- __block_literal_global.386
- __block_literal_global.391
- __block_literal_global.405
- __block_literal_global.410
- __block_literal_global.427
- __block_literal_global.443
- __block_literal_global.448
- __block_literal_global.453
- __block_literal_global.458
- __block_literal_global.463
- __block_literal_global.468
- __block_literal_global.473
- __block_literal_global.478
- __block_literal_global.486
- __block_literal_global.491
- __block_literal_global.496
- __block_literal_global.552
- __block_literal_global.829
- _objc_msgSend$_accountDidChange
- _objc_msgSend$_createStructureRecordForRootItem
- _objc_msgSend$_createStructureRecordWithRecordID:serverItem:basehashSalt:
- _objc_msgSend$_initWithName:
- _objc_msgSend$accountWaiterErrorRetryBackoff
- _objc_msgSend$accountWaiterRefreshPacerDelay
- _objc_msgSend$br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:signature:error:
- _objc_msgSend$brc_isCloudKitShouldBeUsingEnhancedDrivePrivacy
- _objc_msgSend$initWithName:andRetryBackoff:
- _objc_msgSend$initWithRootItem:sessionContext:
- _objc_msgSend$newAggregatedEventWithIdentifier:recordID:zoneMangledID:enhancedDrivePrivacyEnabled:error:count:
- _objc_msgSend$newAppLibraryFromPQLResultSet:version:error:
CStrings:
+ " next-try:%!@(MISSING) ago"
+ "-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2"
+ "-[BRCClientState _stateToData]"
+ "-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]"
+ "-[BRCDownloadContent _stageWithSession:manifest:package:xattrsPackage:error:]_block_invoke"
+ "-[BRCSaltingBatchOperation _createStructureRecordForParentItem]"
+ "-[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:]"
+ "-[BRCSaltingBatchOperation _saltChildRecordFields:serverItem:basehashSalt:]"
+ "-[BRCSaltingBatchOperation initWithParentItem:sessionContext:]"
+ "-[BRFetchRecordsOperation init]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/legacy/BRCFSEventsMonitor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/legacy/support-categories/BRCDiskSpaceReclaimer+LegacyAdditions.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
+ "BRCGetAccountDSIDForMobileDocsRoot"
+ "Error while unarchiving client state %!@(MISSING)"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid FROM app_libraries WHERE app_library_name = %!@(MISSING)"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries WHERE app_library_name = %!@(MISSING)"
+ "Unexpected error while converting client state to data!"
+ "v24@?0B8B12@\"NSError\"16"
+ "v28@?0@\"NSArray\"8B16@\"NSError\"20"
+ "v36@?0@\"BRCDocumentItem\"8@\"BRCServerItem\"16@\"NSData\"24B32"
- " not"
- "-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke"
- "-[BRCSaltingBatchOperation _createStructureRecordForRootItem]"
- "-[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:basehashSalt:]"
- "-[BRCSaltingBatchOperation initWithRootItem:sessionContext:]"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/legacy/BRCFSEventsMonitor.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/legacy/support-categories/BRCDiskSpaceReclaimer+LegacyAdditions.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
- "AccountWaiterThrottle"
- "DELETE FROM aggregated_daily_telemetry"
- "INSERT INTO aggregated_daily_telemetry (app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description) VALUES (%!d(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!l(MISSING)d, %!@(MISSING)) ON CONFLICT DO UPDATE SET count=count+1"
- "SELECT app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, count FROM aggregated_daily_telemetry"
- "account-waiter-error-retry-backoff"
- "account-waiter-refetch-pacer"
- "account-waiter-refresh-delay"
- "com.apple.bird.account-waiter-refresh-queue"
- "n't"
- "v52@?0@\"BRCDocumentItem\"8@\"BRCServerItem\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40B48"

```
