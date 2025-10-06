## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2461.80.8.0.0
-  __TEXT.__text: 0x331830
-  __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0x17c5c
+2720.100.117.0.0
+  __TEXT.__text: 0x32a1bc
+  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__objc_methlist: 0x173e4
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7c2c0
-  __TEXT.__oslogstring: 0x436ba
-  __TEXT.__gcc_except_tab: 0x1849c
-  __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x9214
-  __TEXT.__objc_classname: 0x22e3
-  __TEXT.__objc_methname: 0x3ec75
-  __TEXT.__objc_methtype: 0x852a
-  __TEXT.__objc_stubs: 0x2b2e0
-  __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x8948
-  __DATA_CONST.__objc_classlist: 0x8b0
-  __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x200
+  __TEXT.__cstring: 0x7c785
+  __TEXT.__oslogstring: 0x4393c
+  __TEXT.__gcc_except_tab: 0x1823c
+  __TEXT.__ustring: 0x36
+  __TEXT.__unwind_info: 0x92c0
+  __TEXT.__objc_classname: 0x2397
+  __TEXT.__objc_methname: 0x3ddc3
+  __TEXT.__objc_methtype: 0x7e7e
+  __TEXT.__objc_stubs: 0x2aec0
+  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__const: 0x8ac8
+  __DATA_CONST.__objc_classlist: 0x8e8
+  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x368d0
-  __DATA_CONST.__objc_selrefs: 0xd8c0
-  __DATA_CONST.__objc_arraydata: 0xdd0
-  __AUTH_CONST.__const: 0x24e8
-  __AUTH_CONST.__objc_const: 0x6950
-  __AUTH_CONST.__cfstring: 0x20720
-  __AUTH_CONST.__objc_intobj: 0xaf8
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_const: 0x35f00
+  __DATA_CONST.__objc_selrefs: 0xd560
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xd78
+  __DATA_CONST.__objc_superrefs: 0x818
+  __DATA_CONST.__objc_arraydata: 0xd28
+  __AUTH_CONST.__const: 0x2568
+  __AUTH_CONST.__objc_const: 0x6d80
+  __AUTH_CONST.__cfstring: 0x20240
+  __AUTH_CONST.__objc_intobj: 0x9d8
+  __AUTH_CONST.__objc_arrayobj: 0x168
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0xe98
-  __AUTH.__objc_data: 0x22b0
+  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH.__objc_data: 0x24e0
   __AUTH.__data: 0x18
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xd40
-  __DATA.__objc_superrefs: 0x800
-  __DATA.__objc_ivar: 0x2030
-  __DATA.__data: 0x1ff0
-  __DATA.__bss: 0x360
+  __DATA.__objc_ivar: 0x1f74
+  __DATA.__data: 0x2068
+  __DATA.__bss: 0x380
   __DATA_DIRTY.__objc_data: 0x3430
   __DATA_DIRTY.__data: 0x2c8
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3A61F826-E2CA-3D42-8B2A-72164529AC53
-  Functions: 14593
-  Symbols:   43326
-  CStrings:  27381
+  UUID: 5523DD45-DF0A-33B0-84EE-F98D07E57666
+  Functions: 14408
+  Symbols:   42973
+  CStrings:  27136
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newBasehashSaltingProblemCountWithProblemCount:mangledID:itemIDString:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newDanglingZombieProblemCountWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIntEvent:UUID:value:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:UUID:value:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:UUID:value:round:]
+ +[BRCAccountSession(BRCDatabaseManager) _openConnection:serverTruth:databaseName:baseURL:initialVersion:lastCurrentVersion:error:].cold.8
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]
+ +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:].cold.1
+ +[BRCAutoBugCaptureReporter sharedABCReporter]
+ +[BRCEventsAnalytics sharedAnalytics]
+ +[BRCFlatLevelEnumerator newEnumeratorForItemID:clientZone:]
+ +[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:]
+ +[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:].cold.1
+ +[BRCItemID isAppLibraryRootItemIDWithSQLiteValue:]
+ +[BRCSQLBackedSet _databaseRootDirectory]
+ +[BRCSQLBackedSet clearTempDatabases]
+ +[BRCSQLBackedSet createSetOfClass:withSQLType:error:]
+ +[BRCSQLBackedSet createStringsSetWithError:]
+ +[BRCThumbnailGenerationManager defaultManager]
+ +[BRCUTITypeCache defaultCache]
+ +[BRCUserActionsNavigator defaultNavigator]
+ +[CKAsset(BRCAdvancedDataProtectionAdditions) br_assetWithDeviceID:fileID:generationID:boundaryKey:]
+ +[CKAsset(BRCAdvancedDataProtectionAdditions) br_assetWithFileURL:]
+ +[CKAsset(BRCAdvancedDataProtectionAdditions) br_assetWithFileURL:boundaryKey:]
+ +[CKAsset(BRCAdvancedDataProtectionAdditions) transferOptionsWithBoundaryKey:]
+ +[CKRecord(BRCItemAdditions) _validateAsset:advancedDataProtectionEnabled:]
+ +[NSData(BRCCryptographicAdditions) brc_generateSaltingKey]
+ +[NSData(BRCCryptographicAdditions) brc_generateSaltingKey].cold.1
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasMigrationUUID]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) migrationUUID]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setMigrationUUID:]
+ -[AppTelemetryTimeSeriesEvent setTelemetrySchema:]
+ -[AppTelemetryTimeSeriesEvent telemetrySchema]
+ -[AppTelemetryTimeSeriesEvent(BRCAdditions) _populateUUID:]
+ -[BRCAccountHandler initWithACAccountID:].cold.1
+ -[BRCAccountSession _cloudDocsAppsListDidChange:].cold.2
+ -[BRCAccountSession _reportBasehashSalting]
+ -[BRCAccountSession(BRCDatabaseManager) _appLibrariesEnumerator:version:]
+ -[BRCAccountSession(BRCDatabaseManager) lastBootHistoryTime]
+ -[BRCAccountSession(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:error:]
+ -[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]
+ -[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:].cold.1
+ -[BRCAccountsManager loadAccounts].cold.1
+ -[BRCAppLibrary childBasehashSalt]
+ -[BRCAppLibrary dumpToContext:]
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:]
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:].cold.1
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:].cold.2
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:].cold.3
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:].cold.4
+ -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:].cold.5
+ -[BRCAppLibrary rootRecordCreated]
+ -[BRCAppLibrary saltingState]
+ -[BRCAppLibrary setChildBasehashSalt:]
+ -[BRCAppLibrary setChildBasehashSalt:].cold.1
+ -[BRCAppLibrary setSaltingState:]
+ -[BRCApplyScheduler deleteNonRejectionJobsForZone:].cold.1
+ -[BRCAutoBugCaptureReporter _shouldIgnoreReportForOperationType:ofSubtype:forError:]
+ -[BRCAutoBugCaptureReporter _shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.1
+ -[BRCAutoBugCaptureReporter _shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.2
+ -[BRCAutoBugCaptureReporter _shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.3
+ -[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:]
+ -[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:waitForCompletion:]
+ -[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:]
+ -[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]
+ -[BRCBasehashSaltInfo .cxx_destruct]
+ -[BRCBasehashSaltInfo basehashSaltValidation]
+ -[BRCBasehashSaltInfo childBasehashSalt]
+ -[BRCBasehashSaltInfo copyWithZone:]
+ -[BRCBasehashSaltInfo description]
+ -[BRCBasehashSaltInfo initFromResultSet:pos:]
+ -[BRCBasehashSaltInfo initWithBasehashSaltInfo:]
+ -[BRCBasehashSaltInfo initWithRecord:]
+ -[BRCBasehashSaltInfo init]
+ -[BRCBasehashSaltInfo saltingState]
+ -[BRCBasehashSaltInfo setBasehashSaltValidation:]
+ -[BRCBasehashSaltInfo setChildBasehashSalt:]
+ -[BRCBasehashSaltInfo setSaltingState:]
+ -[BRCClientPrivilegesDescriptor isSyncBubbleClientEntitled]
+ -[BRCClientZone _registerOperation:throttler:]
+ -[BRCClientZone _registerOperation:throttler:].cold.1
+ -[BRCClientZone _registerOperation:throttler:].cold.2
+ -[BRCClientZone _registerOperation:throttler:].cold.3
+ -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:]
+ -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:].cold.1
+ -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:].cold.2
+ -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:].cold.3
+ -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]
+ -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.1
+ -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.2
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.1
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.2
+ -[BRCClientZone(BRCBaseHashSaltAdditions) directUnsaltedItemsInServerTruthEnumeratorParentedTo:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) saltingStateForItemID:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) saltingStateForItemID:].cold.1
+ -[BRCContainerScheduler _scheduleAfterFlush:]
+ -[BRCDaemon _dbgSleepIfRequested]
+ -[BRCDaemon _dbgSleepIfRequested].cold.1
+ -[BRCDeviceConfiguration .cxx_destruct]
+ -[BRCDeviceConfiguration _isFPFS]
+ -[BRCDeviceConfiguration _isIsSycBubble]
+ -[BRCDeviceConfiguration _isSharedIPad:]
+ -[BRCDeviceConfiguration _isTesting]
+ -[BRCDeviceConfiguration getConfiguration]
+ -[BRCDeviceConfiguration getDeviceConfigurationString]
+ -[BRCDumpContext setVerbose:]
+ -[BRCDumpContext verbose]
+ -[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:]
+ -[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:].cold.1
+ -[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:].cold.2
+ -[BRCEventsAnalytics registerAndSendNewApplyFailureWithOutcome:]
+ -[BRCEventsAnalytics registerAndSendNewContainerResetWithOutcome:]
+ -[BRCEventsAnalytics registerAndSendNewFolderSharePCSChainingTime:chainedRecordsCount:zoneMangledID:itemIDString:error:analyticsReporter:]
+ -[BRCEventsAnalytics registerAndSendNewPeriodicSyncWithOutcome:]
+ -[BRCEventsAnalytics registerAndSendNewShareAcceptationWithLastStep:zoneMangledID:itemIDString:error:analyticsReporter:]
+ -[BRCFPFSMigrationScheduler init]
+ -[BRCFSUploader _cancelJobs:state:uploadError:]
+ -[BRCFSUploader _rescheduleJobsPendingScreenUnlock]
+ -[BRCFSUploader _rescheduleJobsPendingScreenUnlock].cold.1
+ -[BRCFSUploader _rescheduleJobsPendingScreenUnlock].cold.2
+ -[BRCFSUploader recoverAndReportMissingJobs].cold.3
+ -[BRCFSUploader screenLockChanged:]
+ -[BRCFSUploader setState:forItem:uploadError:]
+ -[BRCFSUploader setState:forUploadJobID:zone:uploadError:]
+ -[BRCFSUploader thumbnailGenerationManager]
+ -[BRCFlatLevelEnumerator .cxx_destruct]
+ -[BRCFlatLevelEnumerator dealloc]
+ -[BRCFlatLevelEnumerator initWithItemID:clientZone:]
+ -[BRCFlatLevelEnumerator nextObject]
+ -[BRCItemID debugItemIDStringWithVerbose:]
+ -[BRCItemID debugItemIDStringWithVerbose:].cold.1
+ -[BRCItemID debugItemIDStringWithVerbose:].cold.2
+ -[BRCLocalItem saveToDBForServerEdit:keepAliases:].cold.3
+ -[BRCLocalItem shouldUseAdvancedDataProtection]
+ -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:]
+ -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:].cold.1
+ -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:].cold.2
+ -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:].cold.3
+ -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:].cold.4
+ -[BRCLocalItem(BRCSharedToMeTopLevel) updateParentZoneRowID:].cold.5
+ -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:]
+ -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:].cold.1
+ -[BRCLocateRecordOperation initWithRecordID:serverZone:isUserWaiting:maxBackoff:]
+ -[BRCMiniCiconia .cxx_destruct]
+ -[BRCMiniCiconia _cleanupOldCiconiaDomains:]
+ -[BRCMiniCiconia _cleanupOldCiconiaDomains:].cold.1
+ -[BRCMiniCiconia _fsRemoveWorkDirectory:]
+ -[BRCMiniCiconia _removeDiagnosticsDirectoryAtURL:withError:]
+ -[BRCMiniCiconia _removeFPDomain:error:]
+ -[BRCMiniCiconia _removeWorkDirectory:]
+ -[BRCMiniCiconia _removeWorkDirectory:].cold.1
+ -[BRCMiniCiconia _removeWorkDirectory:].cold.2
+ -[BRCMiniCiconia _removeWorkDirectory:].cold.3
+ -[BRCMiniCiconia _removeWorkDirectory:].cold.4
+ -[BRCMiniCiconia _removeWorkDirectory:].cold.5
+ -[BRCMiniCiconia _setupExtensionID]
+ -[BRCMiniCiconia cleanupCiconiaAtURL:diagnosticsURL:completionHandler:]
+ -[BRCMiniCiconia init]
+ -[BRCPQLConnection _registerStaticDBFunctionsWithError:]
+ -[BRCPQLConnection _registerStaticDBFunctionsWithError:].cold.1
+ -[BRCPackageItem _setXattrs:stageRegistry:]
+ -[BRCRecentsEnumeratorBatch initWithBatchSize:]
+ -[BRCSQLBackedSet .cxx_destruct]
+ -[BRCSQLBackedSet _closeDB]
+ -[BRCSQLBackedSet _createSchemaForSQLType:error:]
+ -[BRCSQLBackedSet _dbBecameCorrupted]
+ -[BRCSQLBackedSet addObject:error:]
+ -[BRCSQLBackedSet count]
+ -[BRCSQLBackedSet dealloc]
+ -[BRCSQLBackedSet description]
+ -[BRCSQLBackedSet enumerateObjectsWithSortOrder:usingBlock:]
+ -[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]
+ -[BRCSQLBackedSet initArrayOfClass:withSQLType:error:].cold.1
+ -[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]
+ -[BRCSaltingBatchOperation .cxx_destruct]
+ -[BRCSaltingBatchOperation _buildRecordsWithCompletion:]
+ -[BRCSaltingBatchOperation _createCKOperationForRecords:completion:]
+ -[BRCSaltingBatchOperation _createStructureRecordForRootItem]
+ -[BRCSaltingBatchOperation _createStructureRecordForRootItem].cold.1
+ -[BRCSaltingBatchOperation _createStructureRecordForServerItem:salt:]
+ -[BRCSaltingBatchOperation _createStructureRecordForServerItem:salt:].cold.1
+ -[BRCSaltingBatchOperation _createStructureRecordWithRecordID:itemID:basehashSalt:statInfo:]
+ -[BRCSaltingBatchOperation _getWorkloop]
+ -[BRCSaltingBatchOperation _sendRecordBatch:completion:]
+ -[BRCSaltingBatchOperation _updateRootItemInClientDB]
+ -[BRCSaltingBatchOperation _updateRootItemInServerDB]
+ -[BRCSaltingBatchOperation _updateSaltingInfoInClientDBWithRecords:]
+ -[BRCSaltingBatchOperation _updateSaltingInfoInServerDBWithRecords:]
+ -[BRCSaltingBatchOperation _updateServerTruthForItemID:]
+ -[BRCSaltingBatchOperation finishWithResult:error:]
+ -[BRCSaltingBatchOperation getOrGenerateChildBasehashSaltingKey]
+ -[BRCSaltingBatchOperation initWithRootItem:]
+ -[BRCSaltingBatchOperation initWithRootItem:].cold.1
+ -[BRCSaltingBatchOperation initWithRootItem:].cold.2
+ -[BRCSaltingBatchOperation main]
+ -[BRCSaltingBatchOperation metadataCompletionBlock]
+ -[BRCSaltingBatchOperation setMetadataCompletionBlock:]
+ -[BRCServerItem basehashSaltInfo]
+ -[BRCServerZone _fixupAdvancedDataProtectionState]
+ -[BRCServerZone _saveItemID:version:record:contentBoundaryKey:iWorkSharingOptions:]
+ -[BRCServerZone advancedDataProtectionEnabled]
+ -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step]
+ -[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]
+ -[BRCSharingAcceptFlowOperation _endAcceptationFlow_step]
+ -[BRCSharingAcceptFlowOperation _finishShareAccept_step]
+ -[BRCSharingAcceptFlowOperation _finishShareAccept_step].cold.1
+ -[BRCSharingAcceptFlowOperation _isAccountRestricted_step]
+ -[BRCSharingAcceptFlowOperation _isAccountRestricted_step].cold.1
+ -[BRCSharingAcceptFlowOperation _isAccountRestricted_step].cold.2
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step]
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.1
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.2
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.3
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.4
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.5
+ -[BRCSharingAcceptFlowOperation _isAppInstalled_step].cold.6
+ -[BRCSharingAcceptFlowOperation _isFolderSharingSupported_step]
+ -[BRCSharingAcceptFlowOperation _isFolderSharingSupported_step].cold.1
+ -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]
+ -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step].cold.1
+ -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step].cold.2
+ -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step].cold.3
+ -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step].cold.4
+ -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]
+ -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step].cold.1
+ -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step].cold.2
+ -[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]
+ -[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]
+ -[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded_step]
+ -[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded_step].cold.1
+ -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile_step]
+ -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile_step].cold.1
+ -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile_step].cold.2
+ -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step]
+ -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step].cold.1
+ -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step].cold.2
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step]
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step].cold.1
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step].cold.2
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step].cold.3
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step].cold.4
+ -[BRCSharingAcceptFlowOperation _parseShareMetadata_step].cold.5
+ -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]
+ -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step].cold.1
+ -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step].cold.2
+ -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step].cold.3
+ -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step].cold.4
+ -[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]
+ -[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]
+ -[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step].cold.1
+ -[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step].cold.2
+ -[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step].cold.3
+ -[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step].cold.4
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step]
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.1
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.2
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.3
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.4
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.5
+ -[BRCSharingAcceptFlowOperation _startShareAccept_step].cold.6
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step].cold.1
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step].cold.2
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step].cold.1
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step].cold.2
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step].cold.1
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step].cold.2
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step].cold.1
+ -[BRCSharingAcceptFlowOperation initWithShareMetadata:client:session:userNotifier:userActionsNavigator:]
+ -[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]
+ -[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:].cold.1
+ -[BRCStageRegistry _hasActiveUploadWithStageID:]
+ -[BRCStatInfo lazyXattrWithStageRegistry:]
+ -[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]
+ -[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]
+ -[BRCSyncUpOperation itemNeedingBasehashSalting]
+ -[BRCSyncUpOperation setItemNeedingBasehashSalting:]
+ -[BRCSyncUpOperation setThrottledItemInBatch:]
+ -[BRCSyncUpOperation throttledItemInBatch]
+ -[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToSaltingBasehashItem:]
+ -[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToSaltingBasehashItem:].cold.1
+ -[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToSaltingBasehashItem:].cold.2
+ -[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToSaltingBasehashItem:].cold.3
+ -[BRCSyncUpOperationBuilder _generateSaltGetterBlock]
+ -[BRCSyncUpOperationBuilder _getChildBasehashSaltForItem:]
+ -[BRCSyncUpOperationBuilder _getSaltForItem:]
+ -[BRCSyncUpOperationBuilder _getSaltForItem:].cold.1
+ -[BRCSyncUpOperationBuilder _getSaltForItem:].cold.2
+ -[BRCSyncUpOperationBuilder _recoverItemIDChangedWhileUploadingIfNecessary:]
+ -[BRCSyncUpOperationBuilder addEditOfDirectory:].cold.1
+ -[BRCSyncUpOperationBuilder itemNeedingBasehashSalting]
+ -[BRCSyncUpOperationBuilder rootChildBasehashSalt]
+ -[BRCSystemResourcesManager _initScreenLockManager]
+ -[BRCSystemResourcesManager _invalidateScreenLockManager]
+ -[BRCSystemResourcesManager addScreenLockObserver:]
+ -[BRCSystemResourcesManager removeScreenLockObserver:]
+ -[BRCSystemResourcesManager screenLockChanged:]
+ -[BRCThumbnailGenerateOperation cancel]
+ -[BRCThumbnailGenerationManager .cxx_destruct]
+ -[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]
+ -[BRCThumbnailGenerationManager _generateThumbnailOperationAtURL:targetURL:]
+ -[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]
+ -[BRCThumbnailGenerationManager _thumbnailOperationsMax]
+ -[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]
+ -[BRCThumbnailGenerationManager canScheduleMoreJobs]
+ -[BRCThumbnailGenerationManager description]
+ -[BRCThumbnailGenerationManager hasThumbnailAvailableSlot]
+ -[BRCThumbnailGenerationManager init]
+ -[BRCThumbnailGenerationManager operationForThumbnailID:]
+ -[BRCThumbnailGenerationManager reachedThumbnailMaximumCapacity]
+ -[BRCThumbnailGenerationManager setHasThumbnailAvailableSlot:]
+ -[BRCThumbnailGenerationManager setReachedThumbnailMaximumCapacity:]
+ -[BRCUTITypeCache .cxx_destruct]
+ -[BRCUTITypeCache UTIForExtension:]
+ -[BRCUTITypeCache _getLaunchServicesDatabaseGeneration]
+ -[BRCUTITypeCache _init]
+ -[BRCUTITypeCache _invalidateCahceIfNeeded]
+ -[BRCUTITypeCache _invalidateCahceIfNeeded].cold.1
+ -[BRCUTITypeCache _utiForExtension:]
+ -[BRCUserActionsNavigator openAppStoreForBundleID:]
+ -[BRCUserActionsNavigator openAppStoreForBundleID:].cold.1
+ -[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:]
+ -[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:].cold.1
+ -[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:].cold.2
+ -[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:].cold.3
+ -[BRCUserActionsNavigator openiCloudSettings]
+ -[BRCUserDefaults advancedDataProtectionBasehashSaltingBatchSize]
+ -[BRCUserDefaults advancedDataProtectionForced]
+ -[BRCUserDefaults dbIntegrityCheckBasehashSalting]
+ -[BRCUserDefaults fpfsUploadV2]
+ -[BRCUserDefaults locateRecordsThrottleParams]
+ -[BRCUserDefaults refreshRevisionMaxBackoff]
+ -[BRCUserDefaults retriableCKInteralErrorCodesForRejectedRequestedError]
+ -[BRCUserDefaults supportsAdvancedDataProtection]
+ -[BRCUserDefaults thumbnailGenerationOperationTimeout]
+ -[BRCUserDefaults timestampRoundingAmount]
+ -[BRCUserDefaults treatPerItemThrottleAsOperationSuccess]
+ -[BRCUserDefaults validationKeyTruncationLength]
+ -[BRCUserNotification showJoinDialogForShareMetadata:ckContainer:reply:]
+ -[BRCVersion lazyXattrWithStageRegistry:]
+ -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]
+ -[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]
+ -[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]
+ -[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]
+ -[CKRecord(BRCItemAdditions) brc_fillWithChildBasehashSalt:]
+ -[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:]
+ -[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:].cold.1
+ -[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:].cold.2
+ -[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:].cold.3
+ -[CKRecord(BRCSerializationAdditions) _processSaltingOnAppLibrary:]
+ -[CKRecord(BRCSerializationAdditions) _saveAppLibraryIfNecessary:]
+ -[CKRecord(BRCSerializationAdditions) deserializeFilename:basename:bounceno:extension:userInfo:error:].cold.2
+ -[CKRecord(BRCSerializationAdditions) deserializeFilename:basename:bounceno:extension:userInfo:error:].cold.3
+ -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:]
+ -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:].cold.1
+ -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:].cold.2
+ -[CKRecord(BRCSerializationAdditions) seralizeBirthtime:]
+ -[CKRecord(BRCSerializationAdditions) serializeContentBoundaryKey:]
+ -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:basehashSalt:parentIDIsCloudDocsRoot:]
+ -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:basehashSalt:parentIDIsCloudDocsRoot:]
+ -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:]
+ -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:].cold.1
+ -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:].cold.2
+ -[CKRecord(BRCSerializationAdditions) serializeSpecialIdentityForFilename:parentIDIsCloudDocsRoot:]
+ -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]
+ -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:].cold.1
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.1
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.2
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.3
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.4
+ -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:].cold.5
+ -[NSData(BRCCryptographicAdditions) brc_truncatedSHA256]
+ -[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]
+ -[NSError(BRCAdditions) brc_isCloudKitErrorDataProtectionClass]
+ -[NSError(BRCAdditions) brc_isCloudKitRequestRejectedError]
+ -[NSError(BRCAdditions) brc_isFrontBoardOpenApplicationRequestDenied]
+ -[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]
+ -[NSFileProviderManager(BRCAdditions) br_signalEnumeratorForContainerItemIdentifier:completionHandler:]
+ -[NSString(BRCCryptographicAdditions) brc_SHA256WithSalt:]
+ -[PQLConnection(BRCAdditions) dataWithSQL:]
+ -[_BRCOperation _scheduleExecutionWithPreviousError:].cold.5
+ -[_BRCOperation maxBackoff]
+ -[_BRCOperation setMaxBackoff:]
+ -[_BRCOperation setTimedOut:]
+ -[_BRCOperation setTimeout:]
+ -[_BRCOperation timedOut]
+ -[_BRCOperation timeout]
+ GCC_except_table125
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table192
+ GCC_except_table205
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table229
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table245
+ GCC_except_table247
+ GCC_except_table256
+ GCC_except_table258
+ GCC_except_table264
+ GCC_except_table268
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table308
+ GCC_except_table312
+ GCC_except_table315
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table329
+ GCC_except_table332
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table343
+ GCC_except_table347
+ GCC_except_table368
+ GCC_except_table376
+ GCC_except_table386
+ GCC_except_table389
+ GCC_except_table392
+ GCC_except_table401
+ GCC_except_table404
+ GCC_except_table407
+ GCC_except_table412
+ GCC_except_table416
+ GCC_except_table423
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table75
+ GCC_except_table91
+ GCC_except_table97
+ OBJC_IVAR_$_AppTelemetryInvestigation._migrationUUID
+ OBJC_IVAR_$_AppTelemetryTimeSeriesEvent._telemetrySchema
+ OBJC_IVAR_$_BRCAppLibrary._XPCClientsUsingUbiquity
+ OBJC_IVAR_$_BRCAppLibrary._activeAliasQueries
+ OBJC_IVAR_$_BRCAppLibrary._activeQueries
+ OBJC_IVAR_$_BRCAppLibrary._activeRecursiveQueries
+ OBJC_IVAR_$_BRCAppLibrary._db
+ OBJC_IVAR_$_BRCAppLibrary._dbRowID
+ OBJC_IVAR_$_BRCAppLibrary._deepScanReason
+ OBJC_IVAR_$_BRCAppLibrary._deepScanStamp
+ OBJC_IVAR_$_BRCAppLibrary._defaultClientZone
+ OBJC_IVAR_$_BRCAppLibrary._fileID
+ OBJC_IVAR_$_BRCAppLibrary._generationID
+ OBJC_IVAR_$_BRCAppLibrary._mangledID
+ OBJC_IVAR_$_BRCAppLibrary._maxLostStamp
+ OBJC_IVAR_$_BRCAppLibrary._pendingFileCoordinators
+ OBJC_IVAR_$_BRCAppLibrary._session
+ OBJC_IVAR_$_BRCPrivateClientZone._createZoneOperation
+ OBJC_IVAR_$_BRCPrivateClientZone._createZoneQueue
+ OBJC_IVAR_$_BRCPrivateClientZone._zoneCreationCompletionBlocks
+ _BRCRecursiveRemoveBelow
+ _BRCRoundedTimestamp
+ _BREntitlementSyncBubbleClient
+ _FBSOpenApplicationServiceErrorDomain
+ _OBJC_CLASS_$_BRCBasehashSaltInfo
+ _OBJC_CLASS_$_BRCDeviceConfiguration
+ _OBJC_CLASS_$_BRCEventsAnalytics
+ _OBJC_CLASS_$_BRCFlatLevelEnumerator
+ _OBJC_CLASS_$_BRCMiniCiconia
+ _OBJC_CLASS_$_BRCSQLBackedSet
+ _OBJC_CLASS_$_BRCSaltingBatchOperation
+ _OBJC_CLASS_$_BRCThumbnailGenerationManager
+ _OBJC_CLASS_$_BRCUTITypeCache
+ _OBJC_CLASS_$_BRCUserActionsNavigator
+ _OBJC_CLASS_$_BRRuntimeBehavior
+ _OBJC_CLASS_$_BRScreenLockMonitor
+ _OBJC_CLASS_$_CKAssetTransferOptions
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_IVAR_$_BRCAppLibrary._childBasehashSalt
+ _OBJC_IVAR_$_BRCAppLibrary._saltingState
+ _OBJC_IVAR_$_BRCBasehashSaltInfo._basehashSaltValidation
+ _OBJC_IVAR_$_BRCBasehashSaltInfo._childBasehashSalt
+ _OBJC_IVAR_$_BRCBasehashSaltInfo._saltingState
+ _OBJC_IVAR_$_BRCClientPrivilegesDescriptor._isSyncBubbleClientEntitled
+ _OBJC_IVAR_$_BRCClientZone._locateRecordsOperationThrottle
+ _OBJC_IVAR_$_BRCDeviceConfiguration._configuration
+ _OBJC_IVAR_$_BRCDumpContext._verbose
+ _OBJC_IVAR_$_BRCFSUploader._isScreenLocked
+ _OBJC_IVAR_$_BRCFSUploader._thumbnailGenerationManager
+ _OBJC_IVAR_$_BRCFlatLevelEnumerator._enumerator
+ _OBJC_IVAR_$_BRCFlatLevelEnumerator._itemID
+ _OBJC_IVAR_$_BRCMiniCiconia._extensionID
+ _OBJC_IVAR_$_BRCMiniCiconia._isDataSeparated
+ _OBJC_IVAR_$_BRCMiniCiconia._targetURL
+ _OBJC_IVAR_$_BRCMiniCiconia._workQueue
+ _OBJC_IVAR_$_BRCSQLBackedSet._class
+ _OBJC_IVAR_$_BRCSQLBackedSet._count
+ _OBJC_IVAR_$_BRCSQLBackedSet._db
+ _OBJC_IVAR_$_BRCSQLBackedSet._dbRootFolder
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._baseHashSaltValidation
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._batchSize
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._childBaseSalt
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._metadataCompletionBlock
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._rootClientZone
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._rootItemID
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._rootRecordID
+ _OBJC_IVAR_$_BRCSaltingBatchOperation._rootSaltingState
+ _OBJC_IVAR_$_BRCServerItem._basehashSaltInfo
+ _OBJC_IVAR_$_BRCSharingAcceptFlowOperation._userActionsNavigator
+ _OBJC_IVAR_$_BRCSyncUpOperation._itemNeedingBasehashSalting
+ _OBJC_IVAR_$_BRCSyncUpOperation._throttledItemInBatch
+ _OBJC_IVAR_$_BRCSyncUpOperationBuilder._itemNeedingBasehashSalting
+ _OBJC_IVAR_$_BRCSyncUpOperationBuilder._parentItemIDToChildBasehashSalt
+ _OBJC_IVAR_$_BRCSyncUpOperationBuilder._rootChildBasehashSalt
+ _OBJC_IVAR_$_BRCSystemResourcesManager._screenLockObservers
+ _OBJC_IVAR_$_BRCSystemResourcesManager._screenLocked
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._hasThumbnailAvailableSlot
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._prepareReachedMax
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._reachedThumbnailMaximumCapacity
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._thumbnailPrivateQueue
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._thumbnailQueue
+ _OBJC_IVAR_$_BRCThumbnailGenerationManager._thumbnailsOperations
+ _OBJC_IVAR_$_BRCUTITypeCache._lastUTIDatabaseGeneration
+ _OBJC_IVAR_$_BRCUTITypeCache._utiCache
+ _OBJC_IVAR_$__BRCOperation._maxBackoff
+ _OBJC_IVAR_$__BRCOperation._timedOut
+ _OBJC_IVAR_$__BRCOperation._timeout
+ _OBJC_METACLASS_$_BRCBasehashSaltInfo
+ _OBJC_METACLASS_$_BRCDeviceConfiguration
+ _OBJC_METACLASS_$_BRCEventsAnalytics
+ _OBJC_METACLASS_$_BRCFlatLevelEnumerator
+ _OBJC_METACLASS_$_BRCMiniCiconia
+ _OBJC_METACLASS_$_BRCSQLBackedSet
+ _OBJC_METACLASS_$_BRCSaltingBatchOperation
+ _OBJC_METACLASS_$_BRCThumbnailGenerationManager
+ _OBJC_METACLASS_$_BRCUTITypeCache
+ _OBJC_METACLASS_$_BRCUserActionsNavigator
+ _SecRandomCopyBytes
+ __OBJC_$_CATEGORY_CKAsset_$_BRCAdvancedDataProtectionAdditions
+ __OBJC_$_CLASS_METHODS_BRCEventsAnalytics
+ __OBJC_$_CLASS_METHODS_BRCFlatLevelEnumerator
+ __OBJC_$_CLASS_METHODS_BRCSQLBackedSet
+ __OBJC_$_CLASS_METHODS_BRCThumbnailGenerationManager
+ __OBJC_$_CLASS_METHODS_BRCUTITypeCache
+ __OBJC_$_CLASS_METHODS_BRCUserActionsNavigator
+ __OBJC_$_CLASS_METHODS_CKAsset(BRCAdvancedDataProtectionAdditions)
+ __OBJC_$_CLASS_PROP_LIST_BRCDaemon
+ __OBJC_$_INSTANCE_METHODS_BRCAutoBugCaptureReporter
+ __OBJC_$_INSTANCE_METHODS_BRCBasehashSaltInfo
+ __OBJC_$_INSTANCE_METHODS_BRCClientZone(BRCBaseHashSaltAdditions|BRCZoneReset|LegacyAdditions)
+ __OBJC_$_INSTANCE_METHODS_BRCDeviceConfiguration
+ __OBJC_$_INSTANCE_METHODS_BRCEventsAnalytics
+ __OBJC_$_INSTANCE_METHODS_BRCFlatLevelEnumerator
+ __OBJC_$_INSTANCE_METHODS_BRCMiniCiconia
+ __OBJC_$_INSTANCE_METHODS_BRCSQLBackedSet
+ __OBJC_$_INSTANCE_METHODS_BRCSaltingBatchOperation
+ __OBJC_$_INSTANCE_METHODS_BRCThumbnailGenerationManager
+ __OBJC_$_INSTANCE_METHODS_BRCUTITypeCache
+ __OBJC_$_INSTANCE_METHODS_BRCUserActionsNavigator
+ __OBJC_$_INSTANCE_VARIABLES_BRCBasehashSaltInfo
+ __OBJC_$_INSTANCE_VARIABLES_BRCDeviceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BRCFlatLevelEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_BRCMiniCiconia
+ __OBJC_$_INSTANCE_VARIABLES_BRCSQLBackedSet
+ __OBJC_$_INSTANCE_VARIABLES_BRCSaltingBatchOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRCThumbnailGenerationManager
+ __OBJC_$_INSTANCE_VARIABLES_BRCUTITypeCache
+ __OBJC_$_PROP_LIST_BRCBasehashSaltInfo
+ __OBJC_$_PROP_LIST_BRCDeviceConfiguration
+ __OBJC_$_PROP_LIST_BRCSQLBackedSet
+ __OBJC_$_PROP_LIST_BRCSaltingBatchOperation
+ __OBJC_$_PROP_LIST_BRCThumbnailGenerationManager
+ __OBJC_$_PROP_LIST_BRCUserActionsNavigator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCUserNavigationActions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRScreenLockObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRCUserNavigationActions
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRScreenLockObserver
+ __OBJC_$_PROTOCOL_REFS_BRCScreenLockDelegate
+ __OBJC_$_PROTOCOL_REFS_BRCUserNavigationActions
+ __OBJC_$_PROTOCOL_REFS_BRScreenLockObserver
+ __OBJC_CLASS_PROTOCOLS_$_BRCBasehashSaltInfo
+ __OBJC_CLASS_PROTOCOLS_$_BRCSaltingBatchOperation
+ __OBJC_CLASS_PROTOCOLS_$_BRCUserActionsNavigator
+ __OBJC_CLASS_RO_$_BRCBasehashSaltInfo
+ __OBJC_CLASS_RO_$_BRCDeviceConfiguration
+ __OBJC_CLASS_RO_$_BRCEventsAnalytics
+ __OBJC_CLASS_RO_$_BRCFlatLevelEnumerator
+ __OBJC_CLASS_RO_$_BRCMiniCiconia
+ __OBJC_CLASS_RO_$_BRCSQLBackedSet
+ __OBJC_CLASS_RO_$_BRCSaltingBatchOperation
+ __OBJC_CLASS_RO_$_BRCThumbnailGenerationManager
+ __OBJC_CLASS_RO_$_BRCUTITypeCache
+ __OBJC_CLASS_RO_$_BRCUserActionsNavigator
+ __OBJC_LABEL_PROTOCOL_$_BRCScreenLockDelegate
+ __OBJC_LABEL_PROTOCOL_$_BRCUserNavigationActions
+ __OBJC_LABEL_PROTOCOL_$_BRScreenLockObserver
+ __OBJC_METACLASS_RO_$_BRCBasehashSaltInfo
+ __OBJC_METACLASS_RO_$_BRCDeviceConfiguration
+ __OBJC_METACLASS_RO_$_BRCEventsAnalytics
+ __OBJC_METACLASS_RO_$_BRCFlatLevelEnumerator
+ __OBJC_METACLASS_RO_$_BRCMiniCiconia
+ __OBJC_METACLASS_RO_$_BRCSQLBackedSet
+ __OBJC_METACLASS_RO_$_BRCSaltingBatchOperation
+ __OBJC_METACLASS_RO_$_BRCThumbnailGenerationManager
+ __OBJC_METACLASS_RO_$_BRCUTITypeCache
+ __OBJC_METACLASS_RO_$_BRCUserActionsNavigator
+ __OBJC_PROTOCOL_$_BRCScreenLockDelegate
+ __OBJC_PROTOCOL_$_BRCUserNavigationActions
+ __OBJC_PROTOCOL_$_BRScreenLockObserver
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.225
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.225.cold.1
+ ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.228
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.624
+ ___109-[BRCXPCRegularIPCsClient(LegacyAdditions) _sendPausedFileListBatchToUpdater:fromRowID:batchSize:completion:]_block_invoke.181
+ ___111-[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:]_block_invoke.173
+ ___112-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke
+ ___112-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke.257
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.1
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.2
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.3
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.4
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke_2
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.364
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.365
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.259
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.259.cold.1
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.261
+ ___116-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]_block_invoke
+ ___116-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]_block_invoke.7
+ ___120-[BRCXPCRegularIPCsClient(LegacyAdditions) startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:]_block_invoke.112
+ ___120-[BRCXPCRegularIPCsClient(LegacyAdditions) startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:]_block_invoke.114
+ ___122-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:]_block_invoke
+ ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.201
+ ___18-[BRCDaemon start]_block_invoke.98
+ ___22-[BRCClientZone close]_block_invoke.65
+ ___23-[BRCDaemon selfCheck:]_block_invoke.152
+ ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.166
+ ___25-[BRCFSUploader schedule]_block_invoke.125
+ ___26-[BRCAccountSession close]_block_invoke.199
+ ___26-[BRCAccountSession close]_block_invoke.201
+ ___26-[BRCStageRegistry resume]_block_invoke.160
+ ___26-[BRCStageRegistry resume]_block_invoke.168
+ ___26-[BRCStageRegistry resume]_block_invoke.169
+ ___26-[BRCStageRegistry resume]_block_invoke.169.cold.1
+ ___26-[BRCStageRegistry resume]_block_invoke.169.cold.2
+ ___26-[BRCStageRegistry resume]_block_invoke.169.cold.3
+ ___26-[BRCSyncUpOperation main]_block_invoke.66
+ ___27-[BRCClientZone _startSync]_block_invoke.188
+ ___27-[BRCClientZone _startSync]_block_invoke.188.cold.1
+ ___27-[BRCClientZone _startSync]_block_invoke.188.cold.2
+ ___27-[BRCSQLBackedSet _closeDB]_block_invoke
+ ___27-[BRCSQLBackedSet _closeDB]_block_invoke_2
+ ___29-[BRCAccountMigrator perform]_block_invoke.96
+ ___29-[BRCAccountMigrator perform]_block_invoke.96.cold.1
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke.51
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke.57
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke.61
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.54
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.60
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.60.cold.1
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.62
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.62.cold.1
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.62.cold.2
+ ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.62.cold.3
+ ___31+[BRCUTITypeCache defaultCache]_block_invoke
+ ___32-[BRCPeriodicSyncOperation main]_block_invoke.16
+ ___32-[BRCPeriodicSyncOperation main]_block_invoke_2.20
+ ___32-[BRCSaltingBatchOperation main]_block_invoke
+ ___32-[BRCSaltingBatchOperation main]_block_invoke_2
+ ___32-[BRCSaltingBatchOperation main]_block_invoke_2.cold.1
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.36
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.39
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.184
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.184.cold.1
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.189
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.189.cold.1
+ ___34-[BRCSafeDBHolder closeWithError:]_block_invoke
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.267
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.269
+ ___35-[BRCFSDownloader makeContentLive:]_block_invoke.269.cold.1
+ ___35-[BRCFSUploader screenLockChanged:]_block_invoke
+ ___35-[BRCSQLBackedSet addObject:error:]_block_invoke
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.136
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.136.cold.1
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.143
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.143.cold.1
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.143.cold.2
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.143.cold.3
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.143.cold.4
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.147
+ ___37+[BRCEventsAnalytics sharedAnalytics]_block_invoke
+ ___37-[BRCAccountMigrationChecker perform]_block_invoke.111
+ ___37-[BRCAccountMigrationChecker perform]_block_invoke.111.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.230
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.3
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.240
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.240.cold.1
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.214
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.204
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.204.cold.1
+ ___40-[BRCAccountSession closeOfflineSession]_block_invoke.205
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_4
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_5
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_6
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_6.cold.1
+ ___40-[BRCMiniCiconia _removeFPDomain:error:]_block_invoke
+ ___40-[BRCPQLConnection setProfilingEnabled:]_block_invoke.106
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.169
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.170
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.173
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.179
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.184
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.172
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.172.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.174
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.174.cold.1
+ ___41-[BRCSyncUpOperation performShareUpdate:]_block_invoke.51
+ ___43+[BRCUserActionsNavigator defaultNavigator]_block_invoke
+ ___44-[BRCFSUploader recoverAndReportMissingJobs]_block_invoke.247
+ ___44-[BRCMiniCiconia _cleanupOldCiconiaDomains:]_block_invoke
+ ___44-[BRCThumbnailGenerationManager description]_block_invoke
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.236
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.236.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.239
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.251
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.251.cold.1
+ ___45-[BRCContainerScheduler _scheduleAfterFlush:]_block_invoke
+ ___45-[BRCContainerScheduler _scheduleAfterFlush:]_block_invoke_2
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.326
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.326.cold.1
+ ___46+[BRCAutoBugCaptureReporter sharedABCReporter]_block_invoke
+ ___46-[BRCUserDefaults locateRecordsThrottleParams]_block_invoke
+ ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.435
+ ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.335
+ ___47+[BRCThumbnailGenerationManager defaultManager]_block_invoke
+ ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.65
+ ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.307
+ ___47-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_3
+ ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke.105
+ ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke_2.112
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.138
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.138.cold.1
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.144
+ ___48-[BRCStageRegistry _hasActiveUploadWithStageID:]_block_invoke
+ ___49-[BRCAccountSession(BRCDatabaseManager) closeDBs]_block_invoke.360
+ ___49-[BRCAccountSession(BRCDatabaseManager) closeDBs]_block_invoke.361
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.353
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.354
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.355
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.360
+ ___49-[BRCSQLBackedSet _createSchemaForSQLType:error:]_block_invoke
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.441
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.467
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.262
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.262.cold.1
+ ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.112.cold.1
+ ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.113
+ ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.120.cold.1
+ ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.121
+ ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke_2.122
+ ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke.97
+ ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke_2
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.222
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.141
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.141.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.141.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.141.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.141.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.153
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.153.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.153.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.153.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.153.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.154
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.161
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.165
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.162
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.162.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.162.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.162.cold.3
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.102
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.104
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.109
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.76
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.76.cold.1
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.81
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.103
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.103.cold.1
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.107
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.111
+ ___53-[BRCSharingAcceptFlowOperation _isAppInstalled_step]_block_invoke
+ ___53-[BRCSharingAcceptFlowOperation _isAppInstalled_step]_block_invoke.cold.1
+ ___53-[BRCSharingAcceptFlowOperation _isAppInstalled_step]_block_invoke.cold.2
+ ___53-[BRCSyncUpOperationBuilder _generateSaltGetterBlock]_block_invoke
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.482
+ ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.170
+ ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.172
+ ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.174
+ ___54-[BRCDeviceConfiguration getDeviceConfigurationString]_block_invoke
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.13
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.15
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80.cold.2
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.401
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.402
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.428
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.429
+ ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.389
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke.cold.1
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke.cold.2
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.656
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.657
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.59
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.59.cold.1
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.59.cold.2
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.59.cold.3
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.63
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.63.cold.1
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.66
+ ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.66.cold.1
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke.54
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke.54.cold.1
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke.61
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_2
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_2.68
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_3
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_3.74
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_4
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_4.80
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_5
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_5.86
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_5.cold.1
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_6
+ ___56-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_6.cold.1
+ ___56-[BRCPendingChangesStream _getChangesStreamSafeDBHolder]_block_invoke.103
+ ___56-[BRCSaltingBatchOperation _buildRecordsWithCompletion:]_block_invoke
+ ___56-[BRCSaltingBatchOperation _buildRecordsWithCompletion:]_block_invoke.cold.1
+ ___56-[BRCSaltingBatchOperation _buildRecordsWithCompletion:]_block_invoke.cold.2
+ ___56-[BRCSaltingBatchOperation _buildRecordsWithCompletion:]_block_invoke.cold.3
+ ___56-[BRCSaltingBatchOperation _sendRecordBatch:completion:]_block_invoke
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke.181
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke.cold.1
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_2
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_3
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_4
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_5
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_5.cold.1
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.360
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.361
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.643
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.643.cold.1
+ ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.283
+ ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.285
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88.cold.1
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.486
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.486.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.486.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.487
+ ___57-[BRCSharingAcceptFlowOperation _parseShareMetadata_step]_block_invoke
+ ___57-[BRCThumbnailGenerationManager operationForThumbnailID:]_block_invoke
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.345
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.346
+ ___58-[BRCAnalyticsReporter _checkSyncConsistencyWithActivity:]_block_invoke.66
+ ___58-[BRCFSUploader setState:forUploadJobID:zone:uploadError:]_block_invoke
+ ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.189
+ ___58-[BRCSharingAcceptFlowOperation _isAccountRestricted_step]_block_invoke
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.445
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.453
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.410
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.411
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.427
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.427.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.482
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.482.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.482.cold.2
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.482.cold.3
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.484
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.485
+ ___59-[BRCContainerScheduler _syncScheduleForContainersMetadata]_block_invoke.83
+ ___59-[BRCServerZone dumpTablesToContext:includeAllItems:error:]_block_invoke.296
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.267
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.268
+ ___60-[BRCSQLBackedSet enumerateObjectsWithSortOrder:usingBlock:]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.1
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.10
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.11
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.12
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.13
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.2
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.3
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.4
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.5
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.6
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.7
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.8
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.143.cold.9
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.144
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.154
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.165
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.1
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.2
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.3
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.4
+ ___60-[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke.133
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.591
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.591.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.246
+ ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke
+ ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.51
+ ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.58
+ ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.58.cold.1
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_2
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_3
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_4
+ ___62-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.585
+ ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.426
+ ___63-[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:]_block_invoke
+ ___63-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step]_block_invoke
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.89
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.89.cold.1
+ ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.388
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.179
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.180
+ ___65-[BRCNonLocalVersionsSender(IPCs) listNonLocalVersionsWithReply:]_block_invoke.129
+ ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.295
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.633
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.633.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.633.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.633.cold.3
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.637
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.131
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.131.cold.1
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.cold.1
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke.194
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke_2
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.594
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.595
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.597
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.1
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.2
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.218
+ ___67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.641
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.415
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.415.cold.1
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.488
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.489
+ ___68-[BRCSaltingBatchOperation _createCKOperationForRecords:completion:]_block_invoke
+ ___68-[BRCSaltingBatchOperation _updateSaltingInfoInClientDBWithRecords:]_block_invoke
+ ___68-[BRCSaltingBatchOperation _updateSaltingInfoInServerDBWithRecords:]_block_invoke
+ ___68-[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]_block_invoke
+ ___68-[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]_block_invoke.cold.1
+ ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.328
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.58
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.59
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.59.cold.1
+ ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.299
+ ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.403
+ ___69-[BRCXPCRegularIPCsClient(LegacyAdditions) getPausedFilesList:reply:]_block_invoke.182
+ ___69-[BRCXPCRegularIPCsClient(LegacyAdditions) removeItemFromDisk:reply:]_block_invoke.127
+ ___70-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]_block_invoke
+ ___70-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]_block_invoke.cold.1
+ ___70-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]_block_invoke.cold.2
+ ___70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.122
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.10
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.10.cold.1
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.15
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.15.cold.1
+ ___71-[BRCAnalyticsReporter _setupSyncConsistencyDeferralTimerWithActivity:]_block_invoke.60
+ ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.191
+ ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.191.cold.1
+ ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.191.cold.2
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.493
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.494
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.502
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.502.cold.1
+ ___71-[BRCMiniCiconia cleanupCiconiaAtURL:diagnosticsURL:completionHandler:]_block_invoke
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.651
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.629
+ ___72-[BRCUserNotification showJoinDialogForShareMetadata:ckContainer:reply:]_block_invoke
+ ___72-[BRCUserNotification showJoinDialogForShareMetadata:ckContainer:reply:]_block_invoke_2
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.587
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.580
+ ___73-[BRCAccountSession(BRCDatabaseManager) _appLibrariesEnumerator:version:]_block_invoke
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke_2
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke_3
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2.cold.1
+ ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.30
+ ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.31
+ ___73-[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]_block_invoke
+ ___73-[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]_block_invoke.cold.1
+ ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.404
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.395
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.395.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.396
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.396.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.397
+ ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.642
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.362
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.377
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.556
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.558
+ ___73-[BRCXPCRegularIPCsClient(LegacyAdditions) copyBulkShareIDsAtURLs:reply:]_block_invoke.108
+ ___73-[BRCXPCRegularIPCsClient(LegacyAdditions) copyBulkShareIDsAtURLs:reply:]_block_invoke.110
+ ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.64
+ ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.cold.1
+ ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.cold.2
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.78
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.85
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.90
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.86
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.91
+ ___74-[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]_block_invoke
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.1
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.2
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.3
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.4
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.5
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.37
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.41
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.44
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.cold.1
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.cold.2
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.601
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.603
+ ___74-[BRCXPCRegularIPCsClient(LegacyAdditions) getURLForItemIdentifier:reply:]_block_invoke.101
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.22
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.22.cold.1
+ ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.78
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.390
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.390.cold.1
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.390.cold.2
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.391
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.391.cold.1
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.598
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.599
+ ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) gatherInformationForPath:reply:]_block_invoke.175
+ ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveFileObjectIDToURL:reply:]_block_invoke.185
+ ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveFileObjectIDToURL:reply:]_block_invoke.185.cold.1
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.670
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.673
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.672
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.672.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.187
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.187.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.188
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.188.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.188.cold.2
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.589
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.589.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.553
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.583
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke_2
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke_3
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2.cold.1
+ ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.408
+ ___79-[BRCAnalyticsReporter _resumePausedTreeConsistencyCheckOperationWithActivity:]_block_invoke.65
+ ___79-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke
+ ___79-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke.650
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25.cold.1
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25.cold.2
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke_2
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.543
+ ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.323
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.430
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.431
+ ___80-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveConflictWithName:atURL:reply:]_block_invoke.118
+ ___80-[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]_block_invoke
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.52
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.53
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.53.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.54
+ ___81-[BRCDocumentItem(LegacyAdditions) resumeSyncForBundleID:dropLocalChanges:error:]_block_invoke.98
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.620
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.555
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.622
+ ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.142
+ ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.142.cold.1
+ ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.142.cold.2
+ ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.154
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.55
+ ___82-[BRCXPCRegularIPCsClient(LegacyAdditions) checkIfItemIsShareableWithInode:reply:]_block_invoke.203
+ ___83-[BRCAnalyticsReporter _setupSyncConsistencyCancellationTimerWithActivity:session:]_block_invoke.63
+ ___83-[BRCClientZone didSyncDownRequestID:maxApplyRank:caughtUpWithServer:syncDownDate:]_block_invoke.269
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.260
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.260.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.314
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.314.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.316
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.316.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.325
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.329
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.329.cold.1
+ ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.329.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.492
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.494
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.484
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.484.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.484.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.484.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.488
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.491
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.626
+ ___84-[BRCXPCRegularIPCsClient(LegacyAdditions) _gatherInformationForPath:session:reply:]_block_invoke.174
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.443
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.444
+ ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke
+ ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke_2
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke.cold.1
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke.cold.2
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.495
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.497
+ ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.292
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.187
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.187.cold.1
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.187.cold.2
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.187.cold.3
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.192
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.192.cold.1
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.192.cold.2
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.200
+ ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) waitForFileSystemChangeProcessingWithReply:]_block_invoke.183
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.560
+ ___88-[BRCXPCRegularIPCsClient(LegacyAdditions) getBackReferencingContainerIDsForURLs:reply:]_block_invoke.176
+ ___88-[BRCXPCRegularIPCsClient(LegacyAdditions) pauseSyncForFileAtURL:timeout:options:reply:]_block_invoke.140
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.563
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.564
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.565
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.566
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.567
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.571
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.574
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.575
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.576
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.572
+ ___90-[BRCXPCRegularIPCsClient(LegacyAdditions) resumeSyncForFileAtURL:dropLocalChanges:reply:]_block_invoke.141
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.612
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.351
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.352
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.353
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.354
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.355
+ ___94-[BRCXPCRegularIPCsClient(LegacyAdditions) forceConflictForURL:bookmarkData:forcedEtag:reply:]_block_invoke.119
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.607
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.607.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.608
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.405
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.405.cold.1
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.409
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke_10
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke_11
+ ___96-[BRCClientZone(BRCBaseHashSaltAdditions) directUnsaltedItemsInServerTruthEnumeratorParentedTo:]_block_invoke
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14.cold.1
+ ___Block_byref_object_copy_.106
+ ___Block_byref_object_dispose_.107
+ ___block_descriptor_40_e8_32s_e21_24?0"NSString"8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e30_"NSData"16?0"BRCLocalItem"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"BRCContainerScheduler"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_44_e8_32s_e26_24?0"PQLResultSet"8^16ls32l8
+ ___block_descriptor_60_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_60_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48r56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr48l8s32l8s40l8r56l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e20_v24?08"NSError"16lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8ls32l8s40l8w72l8s64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.108
+ ___block_literal_global.115
+ ___block_literal_global.1175
+ ___block_literal_global.1193
+ ___block_literal_global.129
+ ___block_literal_global.13
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.140
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.1616
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.1671
+ ___block_literal_global.1674
+ ___block_literal_global.1697
+ ___block_literal_global.1709
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.1791
+ ___block_literal_global.1817
+ ___block_literal_global.1828
+ ___block_literal_global.1838
+ ___block_literal_global.1841
+ ___block_literal_global.1843
+ ___block_literal_global.1863
+ ___block_literal_global.187
+ ___block_literal_global.189
+ ___block_literal_global.192
+ ___block_literal_global.2
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.2046
+ ___block_literal_global.207
+ ___block_literal_global.2081
+ ___block_literal_global.2087
+ ___block_literal_global.2092
+ ___block_literal_global.227
+ ___block_literal_global.230
+ ___block_literal_global.2357
+ ___block_literal_global.237
+ ___block_literal_global.2372
+ ___block_literal_global.238
+ ___block_literal_global.2457
+ ___block_literal_global.249
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.265
+ ___block_literal_global.267
+ ___block_literal_global.269
+ ___block_literal_global.274
+ ___block_literal_global.279
+ ___block_literal_global.286
+ ___block_literal_global.30
+ ___block_literal_global.308
+ ___block_literal_global.309
+ ___block_literal_global.328
+ ___block_literal_global.35
+ ___block_literal_global.363
+ ___block_literal_global.370
+ ___block_literal_global.373
+ ___block_literal_global.378
+ ___block_literal_global.395
+ ___block_literal_global.399
+ ___block_literal_global.40
+ ___block_literal_global.411
+ ___block_literal_global.416
+ ___block_literal_global.418
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.45
+ ___block_literal_global.454
+ ___block_literal_global.459
+ ___block_literal_global.464
+ ___block_literal_global.50
+ ___block_literal_global.51
+ ___block_literal_global.547
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.66
+ ___block_literal_global.68
+ ___block_literal_global.694
+ ___block_literal_global.70
+ ___block_literal_global.71
+ ___block_literal_global.730
+ ___block_literal_global.738
+ ___block_literal_global.76
+ ___block_literal_global.87
+ ___block_literal_global.88
+ ___block_literal_global.94
+ ___block_literal_global.99
+ ___br_fixup_tables_7_002_block_invoke.1836
+ ___br_fixup_tables_7_002_block_invoke_2.1839
+ ___br_update_tables_10_000_block_invoke.1013
+ ___br_update_tables_14_000_block_invoke.1191
+ ___br_update_tables_14_000_block_invoke.1191.cold.1
+ ___recursive_table_recreate_schema_block_invoke.1672
+ ___recursive_table_recreate_schema_block_invoke.1672.cold.1
+ __unnamed_array_storage.1546
+ __unnamed_array_storage.1589
+ __unnamed_array_storage.2433
+ __unnamed_array_storage.2451
+ __unnamed_array_storage.2643
+ __unnamed_array_storage.2659
+ __unnamed_array_storage.397
+ __unnamed_array_storage.400
+ __unnamed_array_storage.99
+ _container_create_or_lookup_path_for_current_user
+ _db_fixups
+ _db_fixups_len
+ _defaultCache.defaultCache
+ _defaultCache.onceToken
+ _defaultManager.defaultManager
+ _defaultManager.onceToken
+ _defaultNavigator.navigator
+ _defaultNavigator.onceToken
+ _fpfs_enable_fault_handling
+ _fpfs_recursive_prune_fault
+ _kBRRecordKeyBasehashSaltValidation
+ _kBRRecordKeyBoundaryKeyValidationKey
+ _kBRRecordKeyChildBasehashSalt
+ _kBRRecordKeyChildBasehashSaltValidation
+ _kBRRecordKeyContentBoundaryKey
+ _kBRRecordKeyExactBirthtime
+ _kBRRecordKeyExactModificationTime
+ _kBRRecordKeyExactSize
+ _kBRRecordKeySaltingState
+ _kBRRecordKeySpecialDirectoryIdentity
+ _kSecRandomDefault
+ _objc_exception_throw
+ _objc_msgSend$_addThumbnailOperation:thumbnailID:
+ _objc_msgSend$_appLibrariesEnumerator:version:
+ _objc_msgSend$_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:
+ _objc_msgSend$_buildRecordsWithCompletion:
+ _objc_msgSend$_cancelJobs:state:uploadError:
+ _objc_msgSend$_checkIfShouldDedicateOpToSaltingBasehashItem:
+ _objc_msgSend$_cleanupOldCiconiaDomains:
+ _objc_msgSend$_closeDB
+ _objc_msgSend$_createCKOperationForRecords:completion:
+ _objc_msgSend$_createSchemaForSQLType:error:
+ _objc_msgSend$_createStructureRecordForRootItem
+ _objc_msgSend$_createStructureRecordForServerItem:salt:
+ _objc_msgSend$_createStructureRecordWithRecordID:itemID:basehashSalt:statInfo:
+ _objc_msgSend$_databaseRootDirectory
+ _objc_msgSend$_dbBecameCorrupted
+ _objc_msgSend$_dbgSleepIfRequested
+ _objc_msgSend$_fixupAdvancedDataProtectionState
+ _objc_msgSend$_fsRemoveWorkDirectory:
+ _objc_msgSend$_garbageCollectUploadThumbnailsIncludingActiveUploads:
+ _objc_msgSend$_generateSaltGetterBlock
+ _objc_msgSend$_generateThumbnailOperationAtURL:targetURL:
+ _objc_msgSend$_getChildBasehashSaltForItem:
+ _objc_msgSend$_getLaunchServicesDatabaseGeneration
+ _objc_msgSend$_getSaltForItem:
+ _objc_msgSend$_getWorkloop
+ _objc_msgSend$_hasActiveUploadWithStageID:
+ _objc_msgSend$_initScreenLockManager
+ _objc_msgSend$_invalidateCahceIfNeeded
+ _objc_msgSend$_invalidateScreenLockManager
+ _objc_msgSend$_isFPFS
+ _objc_msgSend$_isIsSycBubble
+ _objc_msgSend$_isSharedIPad:
+ _objc_msgSend$_isTesting
+ _objc_msgSend$_performMetadataSaltingOperationIfNecessaryWithCompletion:
+ _objc_msgSend$_performModifyRecordsOrBatchOperationWithCompletion:
+ _objc_msgSend$_populateUUID:
+ _objc_msgSend$_processSaltingOnAppLibrary:
+ _objc_msgSend$_recoverItemIDChangedWhileUploadingIfNecessary:
+ _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:
+ _objc_msgSend$_registerOperation:throttler:
+ _objc_msgSend$_registerStaticDBFunctionsWithError:
+ _objc_msgSend$_removeDiagnosticsDirectoryAtURL:withError:
+ _objc_msgSend$_removeFPDomain:error:
+ _objc_msgSend$_removeThumbnailOperationForThumbnailID:
+ _objc_msgSend$_removeWorkDirectory:
+ _objc_msgSend$_reportBasehashSalting
+ _objc_msgSend$_rescheduleJobsPendingScreenUnlock
+ _objc_msgSend$_saveAppLibraryIfNecessary:
+ _objc_msgSend$_saveItemID:version:record:contentBoundaryKey:iWorkSharingOptions:
+ _objc_msgSend$_scheduleAfterFlush:
+ _objc_msgSend$_sendDictionaryToCoreAnalytics:eventName:
+ _objc_msgSend$_setXattrs:stageRegistry:
+ _objc_msgSend$_setupExtensionID
+ _objc_msgSend$_shouldIgnoreReportForOperationType:ofSubtype:forError:
+ _objc_msgSend$_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:
+ _objc_msgSend$_updateRootItemInClientDB
+ _objc_msgSend$_updateRootItemInServerDB
+ _objc_msgSend$_updateSaltingInfoInClientDBWithRecords:
+ _objc_msgSend$_updateSaltingInfoInServerDBWithRecords:
+ _objc_msgSend$_updateServerTruthForItemID:
+ _objc_msgSend$_utiForExtension:
+ _objc_msgSend$_validateAsset:advancedDataProtectionEnabled:
+ _objc_msgSend$addScreenLockObserver:
+ _objc_msgSend$addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:
+ _objc_msgSend$advancedDataProtectionBasehashSaltingBatchSize
+ _objc_msgSend$advancedDataProtectionEnabled
+ _objc_msgSend$advancedDataProtectionForced
+ _objc_msgSend$appLibraryRowIDFromRootOrDocumentsSQLiteValue:
+ _objc_msgSend$assetTransferOptions
+ _objc_msgSend$basehashSaltValidation
+ _objc_msgSend$br_any_of:
+ _objc_msgSend$br_assetWithDeviceID:fileID:generationID:boundaryKey:
+ _objc_msgSend$br_assetWithFileURL:
+ _objc_msgSend$br_assetWithFileURL:boundaryKey:
+ _objc_msgSend$br_badFilenameAlternativeName
+ _objc_msgSend$br_isCKErrorCode:underlyingErrorCode:
+ _objc_msgSend$br_isInSyncBubble
+ _objc_msgSend$br_shouldOverwriteExistingName
+ _objc_msgSend$br_signalEnumeratorForContainerItemIdentifier:completionHandler:
+ _objc_msgSend$brc_SHA256WithSalt:
+ _objc_msgSend$brc_fillWithChildBasehashSalt:
+ _objc_msgSend$brc_generateSaltingKey
+ _objc_msgSend$brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors
+ _objc_msgSend$brc_isCloudKitErrorDataProtectionClass
+ _objc_msgSend$brc_isCloudKitRequestRejectedError
+ _objc_msgSend$brc_isFrontBoardOpenApplicationRequestDenied
+ _objc_msgSend$brc_truncatedSHA256
+ _objc_msgSend$childBaseSaltForItemID:
+ _objc_msgSend$childBasehashSalt
+ _objc_msgSend$cleanupCiconiaAtURL:diagnosticsURL:completionHandler:
+ _objc_msgSend$clearTempDatabases
+ _objc_msgSend$closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:
+ _objc_msgSend$createSetOfClass:withSQLType:error:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dataWithSQL:
+ _objc_msgSend$dbIntegrityCheckBasehashSalting
+ _objc_msgSend$debugItemIDStringWithVerbose:
+ _objc_msgSend$defaultCache
+ _objc_msgSend$defaultNavigator
+ _objc_msgSend$deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:
+ _objc_msgSend$directUnsaltedItemsInServerTruthEnumeratorParentedTo:
+ _objc_msgSend$dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:
+ _objc_msgSend$encryptedValues
+ _objc_msgSend$getConfiguration
+ _objc_msgSend$getDomainsForProviderIdentifier:completionHandler:
+ _objc_msgSend$getKnowledgeUUID:andSequenceNumber:
+ _objc_msgSend$getOrGenerateChildBasehashSaltingKey
+ _objc_msgSend$initArrayOfClass:withSQLType:error:
+ _objc_msgSend$initWithBasehashSaltInfo:
+ _objc_msgSend$initWithBatchSize:
+ _objc_msgSend$initWithItemID:clientZone:
+ _objc_msgSend$initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:
+ _objc_msgSend$initWithRecordID:serverZone:isUserWaiting:maxBackoff:
+ _objc_msgSend$initWithRootItem:
+ _objc_msgSend$initWithShareMetadata:client:session:userNotifier:userActionsNavigator:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isAppLibraryRootItemIDWithSQLiteValue:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$isSyncBubbleClientEntitled
+ _objc_msgSend$itemNeedingBasehashSalting
+ _objc_msgSend$lazyXattrWithStageRegistry:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:
+ _objc_msgSend$locateRecordsThrottleParams
+ _objc_msgSend$newAppLibraryFromPQLResultSet:version:error:
+ _objc_msgSend$newEnumeratorForItemID:clientZone:
+ _objc_msgSend$newIntEvent:UUID:value:
+ _objc_msgSend$newLongEvent:UUID:value:round:
+ _objc_msgSend$openAppStoreForBundleID:
+ _objc_msgSend$openShareURLInWebBrowser:withReason:
+ _objc_msgSend$openiCloudSettings
+ _objc_msgSend$operationForThumbnailID:
+ _objc_msgSend$paddedFileSize
+ _objc_msgSend$priority
+ _objc_msgSend$providerDomainWithID:cachePolicy:error:
+ _objc_msgSend$registerAndSendNewApplyFailureWithOutcome:
+ _objc_msgSend$registerAndSendNewContainerResetWithOutcome:
+ _objc_msgSend$registerAndSendNewFolderSharePCSChainingTime:chainedRecordsCount:zoneMangledID:itemIDString:error:analyticsReporter:
+ _objc_msgSend$registerAndSendNewPeriodicSyncWithOutcome:
+ _objc_msgSend$registerAndSendNewShareAcceptationWithLastStep:zoneMangledID:itemIDString:error:analyticsReporter:
+ _objc_msgSend$removeDomain:forProviderIdentifier:completionHandler:
+ _objc_msgSend$removeScreenLockObserver:
+ _objc_msgSend$retriableCKInteralErrorCodesForRejectedRequestedError
+ _objc_msgSend$rootChildBasehashSalt
+ _objc_msgSend$rootRecordCreated
+ _objc_msgSend$saltingState
+ _objc_msgSend$saltingStateForItemID:
+ _objc_msgSend$screenLockChanged:
+ _objc_msgSend$seralizeBirthtime:
+ _objc_msgSend$serializeFilename:forCreation:basehashSalt:parentIDIsCloudDocsRoot:
+ _objc_msgSend$serializeFilename:forCreation:setExtension:basehashSalt:parentIDIsCloudDocsRoot:
+ _objc_msgSend$serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:
+ _objc_msgSend$serializeSpecialIdentityForFilename:parentIDIsCloudDocsRoot:
+ _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:
+ _objc_msgSend$serializeVersion:diffs:deadInServerTruth:basehashSalt:
+ _objc_msgSend$setAssetTransferOptions:
+ _objc_msgSend$setChildBasehashSalt:
+ _objc_msgSend$setDatabase:
+ _objc_msgSend$setEvictsObjectsWithDiscardedContent:
+ _objc_msgSend$setHasThumbnailAvailableSlot:
+ _objc_msgSend$setMaxBackoff:
+ _objc_msgSend$setMetadataCompletionBlock:
+ _objc_msgSend$setMigrationUUID:
+ _objc_msgSend$setMmcsEncryptionSupport:
+ _objc_msgSend$setReachedThumbnailMaximumCapacity:
+ _objc_msgSend$setSaltingState:
+ _objc_msgSend$setState:forItem:uploadError:
+ _objc_msgSend$setState:forUploadJobID:zone:uploadError:
+ _objc_msgSend$setTelemetrySchema:
+ _objc_msgSend$setThrottledItemInBatch:
+ _objc_msgSend$setTimedOut:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$setUseMMCSEncryptionV2:
+ _objc_msgSend$setVerbose:
+ _objc_msgSend$sharedABCReporter
+ _objc_msgSend$sharedAnalytics
+ _objc_msgSend$sharedScreenLockMonitor
+ _objc_msgSend$shouldUseAdvancedDataProtection
+ _objc_msgSend$showJoinDialogForShareMetadata:ckContainer:reply:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:
+ _objc_msgSend$structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:
+ _objc_msgSend$supportsAdvancedDataProtection
+ _objc_msgSend$telemetrySchema
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$throttledItemInBatch
+ _objc_msgSend$thumbnailGenerationManager
+ _objc_msgSend$thumbnailGenerationOperationTimeout
+ _objc_msgSend$timedOut
+ _objc_msgSend$timeout
+ _objc_msgSend$timestampRoundingAmount
+ _objc_msgSend$transferOptionsWithBoundaryKey:
+ _objc_msgSend$treatPerItemThrottleAsOperationSuccess
+ _objc_msgSend$useMMCSEncryptionV2
+ _objc_msgSend$validateAdvancedDataProtectionFieldsWithSession:error:
+ _objc_msgSend$validationKeyTruncationLength
+ _objc_msgSend$verbose
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _reuploadItemInContainer.cold.3
+ _sharedABCReporter.onceToken
+ _sharedABCReporter.reporter
+ _sharedAnalytics.analytics
+ _sharedAnalytics.onceToken
+ _sleep
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newCiconiaReportEvent:state:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIntEvent:eventGroupUUID:value:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:eventGroupUUID:value:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:eventGroupUUID:value:round:]
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.1
- +[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.2
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:waitForCompletion:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:]
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.1
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.2
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.3
- +[BRCDaemon UTIForExtension:]
- +[BRCSharingAcceptFlowOperation _openAppStoreForShareURL:]
- +[BRCSharingAcceptFlowOperation _openAppStoreForShareURL:].cold.1
- +[BRCSharingAcceptFlowOperation _openAppStoreForShareURL:].cold.2
- +[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:]
- +[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:].cold.1
- +[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:].cold.2
- +[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:].cold.3
- +[BRCSharingAcceptFlowOperation _openiCloudSettings]
- +[BRCSharingAcceptFlowOperation userNotificationClass]
- -[AppTelemetryCiconiaBouncesInvestigation aliasToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation aliasToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation aliasToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation aliasToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation copyTo:]
- -[AppTelemetryCiconiaBouncesInvestigation copyWithZone:]
- -[AppTelemetryCiconiaBouncesInvestigation description]
- -[AppTelemetryCiconiaBouncesInvestigation dictionaryRepresentation]
- -[AppTelemetryCiconiaBouncesInvestigation fileToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation fileToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation fileToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation fileToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation folderToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation folderToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation folderToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation folderToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasAliasToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasAliasToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasAliasToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasAliasToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFileToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFileToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFileToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFileToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFolderToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFolderToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFolderToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasFolderToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasNonConflictingKindCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasPackageToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasPackageToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasPackageToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasPackageToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasSymlinkToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasSymlinkToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasSymlinkToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation hasSymlinkToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation hash]
- -[AppTelemetryCiconiaBouncesInvestigation isEqual:]
- -[AppTelemetryCiconiaBouncesInvestigation mergeFrom:]
- -[AppTelemetryCiconiaBouncesInvestigation nonConflictingKindCount]
- -[AppTelemetryCiconiaBouncesInvestigation packageToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation packageToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation packageToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation packageToSymlinkCount]
- -[AppTelemetryCiconiaBouncesInvestigation readFrom:]
- -[AppTelemetryCiconiaBouncesInvestigation setAliasToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setAliasToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setAliasToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setAliasToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFileToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFileToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFileToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFileToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFolderToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFolderToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFolderToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setFolderToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasAliasToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasAliasToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasAliasToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasAliasToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFileToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFileToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFileToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFileToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFolderToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFolderToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFolderToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasFolderToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasNonConflictingKindCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasPackageToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasPackageToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasPackageToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasPackageToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasSymlinkToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasSymlinkToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasSymlinkToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setHasSymlinkToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setNonConflictingKindCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setPackageToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setPackageToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setPackageToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setPackageToSymlinkCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setSymlinkToAliasCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setSymlinkToFileCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setSymlinkToFolderCount:]
- -[AppTelemetryCiconiaBouncesInvestigation setSymlinkToPackageCount:]
- -[AppTelemetryCiconiaBouncesInvestigation symlinkToAliasCount]
- -[AppTelemetryCiconiaBouncesInvestigation symlinkToFileCount]
- -[AppTelemetryCiconiaBouncesInvestigation symlinkToFolderCount]
- -[AppTelemetryCiconiaBouncesInvestigation symlinkToPackageCount]
- -[AppTelemetryCiconiaBouncesInvestigation writeTo:]
- -[AppTelemetryCiconiaEAccessInvestigation copyTo:]
- -[AppTelemetryCiconiaEAccessInvestigation copyWithZone:]
- -[AppTelemetryCiconiaEAccessInvestigation curGid]
- -[AppTelemetryCiconiaEAccessInvestigation curUid]
- -[AppTelemetryCiconiaEAccessInvestigation description]
- -[AppTelemetryCiconiaEAccessInvestigation dictionaryRepresentation]
- -[AppTelemetryCiconiaEAccessInvestigation hasAcls]
- -[AppTelemetryCiconiaEAccessInvestigation hasCurGid]
- -[AppTelemetryCiconiaEAccessInvestigation hasCurUid]
- -[AppTelemetryCiconiaEAccessInvestigation hasHasAcls]
- -[AppTelemetryCiconiaEAccessInvestigation hasProtectionClass]
- -[AppTelemetryCiconiaEAccessInvestigation hasStFlags]
- -[AppTelemetryCiconiaEAccessInvestigation hasStGid]
- -[AppTelemetryCiconiaEAccessInvestigation hasStMode]
- -[AppTelemetryCiconiaEAccessInvestigation hasStUid]
- -[AppTelemetryCiconiaEAccessInvestigation hash]
- -[AppTelemetryCiconiaEAccessInvestigation isEqual:]
- -[AppTelemetryCiconiaEAccessInvestigation mergeFrom:]
- -[AppTelemetryCiconiaEAccessInvestigation protectionClass]
- -[AppTelemetryCiconiaEAccessInvestigation readFrom:]
- -[AppTelemetryCiconiaEAccessInvestigation setCurGid:]
- -[AppTelemetryCiconiaEAccessInvestigation setCurUid:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasAcls:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasCurGid:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasCurUid:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasHasAcls:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasProtectionClass:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasStFlags:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasStGid:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasStMode:]
- -[AppTelemetryCiconiaEAccessInvestigation setHasStUid:]
- -[AppTelemetryCiconiaEAccessInvestigation setProtectionClass:]
- -[AppTelemetryCiconiaEAccessInvestigation setStFlags:]
- -[AppTelemetryCiconiaEAccessInvestigation setStGid:]
- -[AppTelemetryCiconiaEAccessInvestigation setStMode:]
- -[AppTelemetryCiconiaEAccessInvestigation setStUid:]
- -[AppTelemetryCiconiaEAccessInvestigation stFlags]
- -[AppTelemetryCiconiaEAccessInvestigation stGid]
- -[AppTelemetryCiconiaEAccessInvestigation stMode]
- -[AppTelemetryCiconiaEAccessInvestigation stUid]
- -[AppTelemetryCiconiaEAccessInvestigation writeTo:]
- -[AppTelemetryCiconiaInvestigation .cxx_destruct]
- -[AppTelemetryCiconiaInvestigation accountQuotaUsage]
- -[AppTelemetryCiconiaInvestigation areMigratedFaultsBelowThreshold]
- -[AppTelemetryCiconiaInvestigation areNonFaultAllMigrated]
- -[AppTelemetryCiconiaInvestigation bouncedDocumentsFoldersCount]
- -[AppTelemetryCiconiaInvestigation bouncedItemsCount]
- -[AppTelemetryCiconiaInvestigation bouncedItemsMatrix]
- -[AppTelemetryCiconiaInvestigation ciconiaVersion]
- -[AppTelemetryCiconiaInvestigation cloningTime]
- -[AppTelemetryCiconiaInvestigation copyTo:]
- -[AppTelemetryCiconiaInvestigation copyWithZone:]
- -[AppTelemetryCiconiaInvestigation crashReporterKey]
- -[AppTelemetryCiconiaInvestigation datalessItemsCount]
- -[AppTelemetryCiconiaInvestigation description]
- -[AppTelemetryCiconiaInvestigation dictionaryRepresentation]
- -[AppTelemetryCiconiaInvestigation diskSpaceLeft]
- -[AppTelemetryCiconiaInvestigation documentsFoldersWithoutItemIDCount]
- -[AppTelemetryCiconiaInvestigation expectedMigratedItemsCount]
- -[AppTelemetryCiconiaInvestigation experimentId]
- -[AppTelemetryCiconiaInvestigation hasAccountQuotaUsage]
- -[AppTelemetryCiconiaInvestigation hasAreMigratedFaultsBelowThreshold]
- -[AppTelemetryCiconiaInvestigation hasAreNonFaultAllMigrated]
- -[AppTelemetryCiconiaInvestigation hasBouncedDocumentsFoldersCount]
- -[AppTelemetryCiconiaInvestigation hasBouncedItemsCount]
- -[AppTelemetryCiconiaInvestigation hasBouncedItemsMatrix]
- -[AppTelemetryCiconiaInvestigation hasCiconiaVersion]
- -[AppTelemetryCiconiaInvestigation hasCloningTime]
- -[AppTelemetryCiconiaInvestigation hasCrashReporterKey]
- -[AppTelemetryCiconiaInvestigation hasDatalessItemsCount]
- -[AppTelemetryCiconiaInvestigation hasDiskSpaceLeft]
- -[AppTelemetryCiconiaInvestigation hasDocumentsFoldersWithoutItemIDCount]
- -[AppTelemetryCiconiaInvestigation hasExpectedMigratedItemsCount]
- -[AppTelemetryCiconiaInvestigation hasExperimentId]
- -[AppTelemetryCiconiaInvestigation hasIgnoredContentProtectedItems]
- -[AppTelemetryCiconiaInvestigation hasImportTime]
- -[AppTelemetryCiconiaInvestigation hasIsAccountDataSeparated]
- -[AppTelemetryCiconiaInvestigation hasIsDesktopEnabled]
- -[AppTelemetryCiconiaInvestigation hasItemsChangedDuringCloning]
- -[AppTelemetryCiconiaInvestigation hasItemsNotFoundInDB]
- -[AppTelemetryCiconiaInvestigation hasItemsNotMigratedCount]
- -[AppTelemetryCiconiaInvestigation hasManuallyTriggeredMigration]
- -[AppTelemetryCiconiaInvestigation hasMaterialisedOnCDItemsCount]
- -[AppTelemetryCiconiaInvestigation hasMaterialisedOnFPFSItemsCount]
- -[AppTelemetryCiconiaInvestigation hasPackagesWithoutBundleBit]
- -[AppTelemetryCiconiaInvestigation hasPreviousAttempts]
- -[AppTelemetryCiconiaInvestigation hasPreviousFailedAttempts]
- -[AppTelemetryCiconiaInvestigation hasPreviousReleasesSuccessRate]
- -[AppTelemetryCiconiaInvestigation hasRampId]
- -[AppTelemetryCiconiaInvestigation hasSymlinkedDocumentsFolderCount]
- -[AppTelemetryCiconiaInvestigation hasTotalItemCount]
- -[AppTelemetryCiconiaInvestigation hasTreatmentId]
- -[AppTelemetryCiconiaInvestigation hasTypesOfMigratedItemsMask]
- -[AppTelemetryCiconiaInvestigation hasTypesOfNonMigratedItemsMask]
- -[AppTelemetryCiconiaInvestigation hasUnderlyingErrorCode]
- -[AppTelemetryCiconiaInvestigation hasUnderlyingErrorDescription]
- -[AppTelemetryCiconiaInvestigation hasUnderlyingErrorDomain]
- -[AppTelemetryCiconiaInvestigation hasUnexpectedCreations]
- -[AppTelemetryCiconiaInvestigation hash]
- -[AppTelemetryCiconiaInvestigation ignoredContentProtectedItems]
- -[AppTelemetryCiconiaInvestigation importTime]
- -[AppTelemetryCiconiaInvestigation isAccountDataSeparated]
- -[AppTelemetryCiconiaInvestigation isDesktopEnabled]
- -[AppTelemetryCiconiaInvestigation isEqual:]
- -[AppTelemetryCiconiaInvestigation itemsChangedDuringCloning]
- -[AppTelemetryCiconiaInvestigation itemsNotFoundInDB]
- -[AppTelemetryCiconiaInvestigation itemsNotMigratedCount]
- -[AppTelemetryCiconiaInvestigation manuallyTriggeredMigration]
- -[AppTelemetryCiconiaInvestigation materialisedOnCDItemsCount]
- -[AppTelemetryCiconiaInvestigation materialisedOnFPFSItemsCount]
- -[AppTelemetryCiconiaInvestigation mergeFrom:]
- -[AppTelemetryCiconiaInvestigation packagesWithoutBundleBit]
- -[AppTelemetryCiconiaInvestigation previousAttempts]
- -[AppTelemetryCiconiaInvestigation previousFailedAttempts]
- -[AppTelemetryCiconiaInvestigation previousReleasesSuccessRate]
- -[AppTelemetryCiconiaInvestigation rampId]
- -[AppTelemetryCiconiaInvestigation readFrom:]
- -[AppTelemetryCiconiaInvestigation setAccountQuotaUsage:]
- -[AppTelemetryCiconiaInvestigation setAreMigratedFaultsBelowThreshold:]
- -[AppTelemetryCiconiaInvestigation setAreNonFaultAllMigrated:]
- -[AppTelemetryCiconiaInvestigation setBouncedDocumentsFoldersCount:]
- -[AppTelemetryCiconiaInvestigation setBouncedItemsCount:]
- -[AppTelemetryCiconiaInvestigation setBouncedItemsMatrix:]
- -[AppTelemetryCiconiaInvestigation setCiconiaVersion:]
- -[AppTelemetryCiconiaInvestigation setCloningTime:]
- -[AppTelemetryCiconiaInvestigation setCrashReporterKey:]
- -[AppTelemetryCiconiaInvestigation setDatalessItemsCount:]
- -[AppTelemetryCiconiaInvestigation setDiskSpaceLeft:]
- -[AppTelemetryCiconiaInvestigation setDocumentsFoldersWithoutItemIDCount:]
- -[AppTelemetryCiconiaInvestigation setExpectedMigratedItemsCount:]
- -[AppTelemetryCiconiaInvestigation setExperimentId:]
- -[AppTelemetryCiconiaInvestigation setHasAccountQuotaUsage:]
- -[AppTelemetryCiconiaInvestigation setHasAreMigratedFaultsBelowThreshold:]
- -[AppTelemetryCiconiaInvestigation setHasAreNonFaultAllMigrated:]
- -[AppTelemetryCiconiaInvestigation setHasBouncedDocumentsFoldersCount:]
- -[AppTelemetryCiconiaInvestigation setHasBouncedItemsCount:]
- -[AppTelemetryCiconiaInvestigation setHasBouncedItemsMatrix:]
- -[AppTelemetryCiconiaInvestigation setHasCiconiaVersion:]
- -[AppTelemetryCiconiaInvestigation setHasCloningTime:]
- -[AppTelemetryCiconiaInvestigation setHasDatalessItemsCount:]
- -[AppTelemetryCiconiaInvestigation setHasDiskSpaceLeft:]
- -[AppTelemetryCiconiaInvestigation setHasDocumentsFoldersWithoutItemIDCount:]
- -[AppTelemetryCiconiaInvestigation setHasExpectedMigratedItemsCount:]
- -[AppTelemetryCiconiaInvestigation setHasIgnoredContentProtectedItems:]
- -[AppTelemetryCiconiaInvestigation setHasImportTime:]
- -[AppTelemetryCiconiaInvestigation setHasIsAccountDataSeparated:]
- -[AppTelemetryCiconiaInvestigation setHasIsDesktopEnabled:]
- -[AppTelemetryCiconiaInvestigation setHasItemsChangedDuringCloning:]
- -[AppTelemetryCiconiaInvestigation setHasItemsNotFoundInDB:]
- -[AppTelemetryCiconiaInvestigation setHasItemsNotMigratedCount:]
- -[AppTelemetryCiconiaInvestigation setHasManuallyTriggeredMigration:]
- -[AppTelemetryCiconiaInvestigation setHasMaterialisedOnCDItemsCount:]
- -[AppTelemetryCiconiaInvestigation setHasMaterialisedOnFPFSItemsCount:]
- -[AppTelemetryCiconiaInvestigation setHasPackagesWithoutBundleBit:]
- -[AppTelemetryCiconiaInvestigation setHasPreviousAttempts:]
- -[AppTelemetryCiconiaInvestigation setHasPreviousFailedAttempts:]
- -[AppTelemetryCiconiaInvestigation setHasPreviousReleasesSuccessRate:]
- -[AppTelemetryCiconiaInvestigation setHasSymlinkedDocumentsFolderCount:]
- -[AppTelemetryCiconiaInvestigation setHasTotalItemCount:]
- -[AppTelemetryCiconiaInvestigation setHasTypesOfMigratedItemsMask:]
- -[AppTelemetryCiconiaInvestigation setHasTypesOfNonMigratedItemsMask:]
- -[AppTelemetryCiconiaInvestigation setHasUnderlyingErrorCode:]
- -[AppTelemetryCiconiaInvestigation setHasUnexpectedCreations:]
- -[AppTelemetryCiconiaInvestigation setIgnoredContentProtectedItems:]
- -[AppTelemetryCiconiaInvestigation setImportTime:]
- -[AppTelemetryCiconiaInvestigation setIsAccountDataSeparated:]
- -[AppTelemetryCiconiaInvestigation setIsDesktopEnabled:]
- -[AppTelemetryCiconiaInvestigation setItemsChangedDuringCloning:]
- -[AppTelemetryCiconiaInvestigation setItemsNotFoundInDB:]
- -[AppTelemetryCiconiaInvestigation setItemsNotMigratedCount:]
- -[AppTelemetryCiconiaInvestigation setManuallyTriggeredMigration:]
- -[AppTelemetryCiconiaInvestigation setMaterialisedOnCDItemsCount:]
- -[AppTelemetryCiconiaInvestigation setMaterialisedOnFPFSItemsCount:]
- -[AppTelemetryCiconiaInvestigation setPackagesWithoutBundleBit:]
- -[AppTelemetryCiconiaInvestigation setPreviousAttempts:]
- -[AppTelemetryCiconiaInvestigation setPreviousFailedAttempts:]
- -[AppTelemetryCiconiaInvestigation setPreviousReleasesSuccessRate:]
- -[AppTelemetryCiconiaInvestigation setRampId:]
- -[AppTelemetryCiconiaInvestigation setSymlinkedDocumentsFolderCount:]
- -[AppTelemetryCiconiaInvestigation setTotalItemCount:]
- -[AppTelemetryCiconiaInvestigation setTreatmentId:]
- -[AppTelemetryCiconiaInvestigation setTypesOfMigratedItemsMask:]
- -[AppTelemetryCiconiaInvestigation setTypesOfNonMigratedItemsMask:]
- -[AppTelemetryCiconiaInvestigation setUnderlyingErrorCode:]
- -[AppTelemetryCiconiaInvestigation setUnderlyingErrorDescription:]
- -[AppTelemetryCiconiaInvestigation setUnderlyingErrorDomain:]
- -[AppTelemetryCiconiaInvestigation setUnexpectedCreations:]
- -[AppTelemetryCiconiaInvestigation symlinkedDocumentsFolderCount]
- -[AppTelemetryCiconiaInvestigation totalItemCount]
- -[AppTelemetryCiconiaInvestigation treatmentId]
- -[AppTelemetryCiconiaInvestigation typesOfMigratedItemsMask]
- -[AppTelemetryCiconiaInvestigation typesOfNonMigratedItemsMask]
- -[AppTelemetryCiconiaInvestigation underlyingErrorCode]
- -[AppTelemetryCiconiaInvestigation underlyingErrorDescription]
- -[AppTelemetryCiconiaInvestigation underlyingErrorDomain]
- -[AppTelemetryCiconiaInvestigation unexpectedCreations]
- -[AppTelemetryCiconiaInvestigation writeTo:]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) bouncesInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) ciconiaInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) eaccessInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasBouncesInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasCiconiaInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasEaccessInvestigation]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setBouncesInvestigation:]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setCiconiaInvestigation:]
- -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setEaccessInvestigation:]
- -[AppTelemetryTimeSeriesEvent identifier]
- -[AppTelemetryTimeSeriesEvent setIdentifier:]
- -[BRCAccountHandler shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup]
- -[BRCAccountSession _cancelCiconiaRepeatQueue]
- -[BRCAccountSession _isExpectedCiconiaError:]
- -[BRCAccountSession _refreshCiconiaState]
- -[BRCAccountSession _refreshCiconiaState].cold.1
- -[BRCAccountSession _refreshCiconiaState].cold.2
- -[BRCAccountSession _refreshCiconiaState].cold.3
- -[BRCAccountSession _reportFailedQueueingMigration:]
- -[BRCAccountSession _setupCiconiaRepeatQueue]
- -[BRCAccountSession _setupCiconiaRepeatQueue].cold.1
- -[BRCAccountSession _startCiconiaIfRelevant]
- -[BRCAccountSession _startCiconiaIfRelevant].cold.1
- -[BRCAccountSession ciconiaState]
- -[BRCAccountSession ciconiaVersion]
- -[BRCAccountSession lastCiconiaVersion:]
- -[BRCAccountSession setCiconiaState:]
- -[BRCAccountSession setCiconiaVersion:]
- -[BRCAccountSession shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup]
- -[BRCAccountSession shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup].cold.1
- -[BRCAccountSession shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup].cold.2
- -[BRCAccountSession(BRCDatabaseManager) getMigrationAttemptOriginatorIDsForVersion:withDB:]
- -[BRCAccountSession(BRCDatabaseManager) getPreviousMigrationAttempts:failed:beforeVersion:]
- -[BRCAccountSession(BRCDatabaseManager) getPreviousMigrationAttempts:failed:forVersion:]
- -[BRCAccountSession(BRCDatabaseManager) getPreviousMigrationAttempts:failed:withVersion:comperator:]
- -[BRCAccountSession(BRCDatabaseManager) newAppLibraryFromPQLResultSet:error:]
- -[BRCAccountSession(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]
- -[BRCAccountSession(BRCDatabaseManager) shouldStartCiconiaBasedOnItemsCountWithAcountHash:]
- -[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]
- -[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:].cold.1
- -[BRCAccountsManager notifyAccountsListChanged]
- -[BRCAccountsManager performWhenAccountsListChanges:]
- -[BRCAccountsManager shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollupForAllAccounts]
- -[BRCAccountsManager startedUpInSyncBubble]
- -[BRCAnalyticsReporter _fetchTelemetryEventCountOrAdd:]
- -[BRCAnalyticsReporter _getPriorityOfEvent:]
- -[BRCAnalyticsReporter _prepareSyncTelemetryEventsToSend]
- -[BRCAnalyticsReporter _prepareSyncTelemetryEventsToSend].cold.1
- -[BRCAnalyticsReporter createSQLConditionForRowIDs:]
- -[BRCAnalyticsReporter currentTelemetryToken]
- -[BRCAnalyticsReporter dropAllSyncTelemetryEvents]
- -[BRCAnalyticsReporter findTelemetryEvent:]
- -[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]
- -[BRCAnalyticsReporter forceTelemetryDequeue]
- -[BRCAnalyticsReporter postReportForDefaultSubCategoryWithCategory:telemetryTimeEvent:].cold.1
- -[BRCAnalyticsReporter submitSyncTelemetryEvent:]
- -[BRCAnalyticsReporter syncTelemetryEventsToSend]
- -[BRCAnalyticsReporter updateCurrentTelemetryToken:]
- -[BRCAnalyticsReporter updateCurrentTelemetryToken:].cold.1
- -[BRCAnalyticsReporter updateCurrentTelemetryToken:].cold.2
- -[BRCAnalyticsReporter updateCurrentTelemetryToken:].cold.3
- -[BRCAnalyticsReporter updateCurrentTelemetryToken:].cold.4
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:]
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:].cold.1
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:].cold.2
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:].cold.3
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:].cold.4
- -[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:].cold.5
- -[BRCAppTelemetryConverter .cxx_destruct]
- -[BRCAppTelemetryConverter init]
- -[BRCClientPrivilegesDescriptor cloudEnabledStatusForSession:]
- -[BRCClientZone _registerServerStitchingOperation:].cold.1
- -[BRCClientZone _registerServerStitchingOperation:].cold.2
- -[BRCClientZone _registerServerStitchingOperation:].cold.3
- -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:]
- -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:].cold.1
- -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:].cold.2
- -[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:].cold.3
- -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:].cold.1
- -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:].cold.2
- -[BRCDaemon startedUpInSyncBubble]
- -[BRCFPFSMigrationScheduler _isCoconiaSuccessful]
- -[BRCFPFSMigrationScheduler initWithCiconiaStatusProvider:]
- -[BRCFSUploader _cancelJobs:state:]
- -[BRCFSUploader _doneFetchingThumbnailForJobID:]
- -[BRCFSUploader _doneFetchingThumbnailForJobID:].cold.1
- -[BRCFSUploader _startFetchThumbnail:jobID:]
- -[BRCFSUploader _startFetchThumbnail:jobID:].cold.1
- -[BRCFSUploader _thumbnailOperationForItemRowID:]
- -[BRCFSUploader thumbnailsOperationsByID]
- -[BRCItemID debugItemIDString].cold.1
- -[BRCItemID debugItemIDString].cold.2
- -[BRCItemID debugItemIDString].cold.3
- -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:]
- -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:].cold.1
- -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:].cold.2
- -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:].cold.3
- -[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:].cold.4
- -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:]
- -[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:].cold.1
- -[BRCLocateRecordOperation initWithRecordID:serverZone:isUserWaiting:]
- -[BRCPackageItem _setXattrs:session:]
- -[BRCRecentsEnumeratorBatch init]
- -[BRCSafeDBHolder closeWithError:].cold.1
- -[BRCSafeDBHolder closeWithError:].cold.2
- -[BRCSafeDBHolder closeWithError:].cold.3
- -[BRCServerZone _saveItemID:version:record:iWorkSharingOptions:]
- -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion]
- -[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]
- -[BRCSharingAcceptFlowOperation _endAcceptationFlow]
- -[BRCSharingAcceptFlowOperation _finishShareAccept]
- -[BRCSharingAcceptFlowOperation _finishShareAccept].cold.1
- -[BRCSharingAcceptFlowOperation _isAccountRestricted]
- -[BRCSharingAcceptFlowOperation _isAccountRestricted].cold.1
- -[BRCSharingAcceptFlowOperation _isAccountRestricted].cold.2
- -[BRCSharingAcceptFlowOperation _isAppInstalled]
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.1
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.2
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.3
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.4
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.5
- -[BRCSharingAcceptFlowOperation _isAppInstalled].cold.6
- -[BRCSharingAcceptFlowOperation _isFolderSharingSupported]
- -[BRCSharingAcceptFlowOperation _isFolderSharingSupported].cold.1
- -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]
- -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive].cold.1
- -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive].cold.2
- -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive].cold.3
- -[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive].cold.4
- -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk]
- -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk].cold.1
- -[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk].cold.2
- -[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]
- -[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]
- -[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded]
- -[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded].cold.1
- -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile]
- -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile].cold.1
- -[BRCSharingAcceptFlowOperation _openSharedSideFaultFile].cold.2
- -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively]
- -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively].cold.1
- -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively].cold.2
- -[BRCSharingAcceptFlowOperation _parseShareMetadata]
- -[BRCSharingAcceptFlowOperation _parseShareMetadata].cold.1
- -[BRCSharingAcceptFlowOperation _parseShareMetadata].cold.2
- -[BRCSharingAcceptFlowOperation _parseShareMetadata].cold.3
- -[BRCSharingAcceptFlowOperation _parseShareMetadata].cold.4
- -[BRCSharingAcceptFlowOperation _parseShareMetadata].cold.5
- -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]
- -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument].cold.1
- -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument].cold.2
- -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument].cold.3
- -[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument].cold.4
- -[BRCSharingAcceptFlowOperation _setSpotlightAttribute]
- -[BRCSharingAcceptFlowOperation _showSharingJoinDialog]
- -[BRCSharingAcceptFlowOperation _showSharingJoinDialog].cold.1
- -[BRCSharingAcceptFlowOperation _showSharingJoinDialog].cold.2
- -[BRCSharingAcceptFlowOperation _showSharingJoinDialog].cold.3
- -[BRCSharingAcceptFlowOperation _showSharingJoinDialog].cold.4
- -[BRCSharingAcceptFlowOperation _startShareAccept]
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.1
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.2
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.3
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.4
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.5
- -[BRCSharingAcceptFlowOperation _startShareAccept].cold.6
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner].cold.1
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner].cold.2
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient].cold.1
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient].cold.2
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner].cold.1
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner].cold.2
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient].cold.1
- -[BRCSharingAcceptFlowOperation initWithShareMetadata:client:session:]
- -[BRCStageRegistry _garbageCollectUploadThumbnails]
- -[BRCStageRegistry currentlyDumpingForCiconia]
- -[BRCStageRegistry setCurrentlyDumpingForCiconia:]
- -[BRCStageRegistry setStageDirectoryForXattr:]
- -[BRCStageRegistry setStageDirectoryForXattr:].cold.1
- -[BRCStatInfo lazyXattrWithSession:]
- -[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]
- -[BRCSyncUpOperation prepareWithMaxCost:retryAfter:].cold.8
- -[BRCSyncUpOperationBuilder addItem:].cold.3
- -[BRCTrialConfiguration ciconiaGatedForFPFSMigration]
- -[BRCTrialConfiguration ignorePercentsOnInternal]
- -[BRCTrialConfiguration maxFailurePerVersion]
- -[BRCTrialConfiguration percent100kAndAbove]
- -[BRCTrialConfiguration percentBelow100k]
- -[BRCTrialConfiguration percentBelow10k]
- -[BRCTrialConfiguration percentBelow1k]
- -[BRCUserDefaults _ciconiaOriginatorIDs:byDefault:]
- -[BRCUserDefaults ciconiaDisableAutomatedStart]
- -[BRCUserDefaults ciconiaHideMigrationDomain]
- -[BRCUserDefaults ciconiaImportTimeout]
- -[BRCUserDefaults ciconiaKeepDomainAfterMigration]
- -[BRCUserDefaults ciconiaMarkSuccessAsFailOnContentProtectedItems]
- -[BRCUserDefaults ciconiaMaxFailurePerVersion]
- -[BRCUserDefaults ciconiaMaxReconciliationFailures]
- -[BRCUserDefaults ciconiaMaxSideFaultsMigration]
- -[BRCUserDefaults ciconiaOriginatorIDsTTRWorthy]
- -[BRCUserDefaults ciconiaOriginatorIDsToTreatAsSuccess]
- -[BRCUserDefaults ciconiaRepeatInterval]
- -[BRCUserDefaults ciconiaSkipTrial]
- -[BRCUserDefaults ciconiaSleepTimeAtInvalidate]
- -[BRCUserDefaults fetchParticipantDocumentToken]
- -[BRCUserDefaults fpfsMigrationFinishedTelemetryXPCActivity]
- -[BRCUserDefaults requireSuccessfulCiconiaRunForFPFSMigration]
- -[BRCUserDefaults telemetryRTCDisabledInvestigationKeys]
- -[BRCUserDefaults telemetryRTCPayloadKeysConverter]
- -[BRCUserDefaults thumbnailUploadAgeDelta]
- -[BRCUserNotification showJoinDialogForShareMetadata:session:reply:]
- -[BRCVersion lazyXattrWithSession:]
- -[BRCXPCRegularIPCsClient _isCiconiaErrorTTRWorthy:]
- -[BRCXPCRegularIPCsClient _isExpectedCiconiaError:originatorId:]
- -[BRCXPCRegularIPCsClient _reportEAccessDuringSilentMigration:uuid:]
- -[BRCXPCRegularIPCsClient _reportOverBounceDuringSilentMigration:total:uuid:]
- -[BRCXPCRegularIPCsClient _updateCiconiaState:uuid:]
- -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:]
- -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:].cold.1
- -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:].cold.2
- -[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]
- -[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]
- -[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]
- -[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]
- -[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]
- -[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]
- -[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]
- -[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]
- -[BRCXPCRegularIPCsClient(LegacyAdditions) launchItemCountMismatchChecksAtURL:reply:]
- -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:clientZone:error:]
- -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:clientZone:error:].cold.1
- -[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:clientZone:error:].cold.2
- -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:]
- -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:]
- -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:]
- -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:].cold.1
- -[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:].cold.2
- -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:]
- -[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:].cold.1
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:]
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:].cold.1
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:].cold.2
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:].cold.3
- -[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:].cold.4
- -[NSData(BRCCryptographicAdditions) brc_SHA256WithSalt:]
- -[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]
- -[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:].cold.1
- GCC_except_table112
- GCC_except_table124
- GCC_except_table128
- GCC_except_table147
- GCC_except_table155
- GCC_except_table163
- GCC_except_table170
- GCC_except_table171
- GCC_except_table176
- GCC_except_table190
- GCC_except_table191
- GCC_except_table195
- GCC_except_table196
- GCC_except_table203
- GCC_except_table210
- GCC_except_table212
- GCC_except_table216
- GCC_except_table218
- GCC_except_table220
- GCC_except_table224
- GCC_except_table230
- GCC_except_table232
- GCC_except_table239
- GCC_except_table243
- GCC_except_table246
- GCC_except_table248
- GCC_except_table255
- GCC_except_table257
- GCC_except_table259
- GCC_except_table261
- GCC_except_table263
- GCC_except_table265
- GCC_except_table266
- GCC_except_table271
- GCC_except_table272
- GCC_except_table280
- GCC_except_table281
- GCC_except_table284
- GCC_except_table307
- GCC_except_table310
- GCC_except_table313
- GCC_except_table317
- GCC_except_table320
- GCC_except_table323
- GCC_except_table334
- GCC_except_table337
- GCC_except_table341
- GCC_except_table344
- GCC_except_table348
- GCC_except_table367
- GCC_except_table381
- GCC_except_table388
- GCC_except_table391
- GCC_except_table394
- GCC_except_table402
- GCC_except_table406
- GCC_except_table409
- GCC_except_table414
- GCC_except_table422
- GCC_except_table428
- GCC_except_table434
- GCC_except_table442
- GCC_except_table445
- GCC_except_table448
- GCC_except_table450
- GCC_except_table452
- GCC_except_table455
- GCC_except_table456
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._aliasToFileCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._aliasToFolderCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._aliasToPackageCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._aliasToSymlinkCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._fileToAliasCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._fileToFolderCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._fileToPackageCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._fileToSymlinkCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._folderToAliasCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._folderToFileCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._folderToPackageCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._folderToSymlinkCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._has
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._nonConflictingKindCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._packageToAliasCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._packageToFileCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._packageToFolderCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._packageToSymlinkCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._symlinkToAliasCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._symlinkToFileCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._symlinkToFolderCount
- OBJC_IVAR_$_AppTelemetryCiconiaBouncesInvestigation._symlinkToPackageCount
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._curGid
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._curUid
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._has
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._hasAcls
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._protectionClass
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._stFlags
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._stGid
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._stMode
- OBJC_IVAR_$_AppTelemetryCiconiaEAccessInvestigation._stUid
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._accountQuotaUsage
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._areMigratedFaultsBelowThreshold
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._areNonFaultAllMigrated
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._bouncedDocumentsFoldersCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._bouncedItemsCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._bouncedItemsMatrix
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._ciconiaVersion
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._cloningTime
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._crashReporterKey
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._datalessItemsCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._diskSpaceLeft
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._documentsFoldersWithoutItemIDCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._expectedMigratedItemsCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._experimentId
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._has
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._ignoredContentProtectedItems
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._importTime
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._isAccountDataSeparated
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._isDesktopEnabled
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._itemsChangedDuringCloning
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._itemsNotFoundInDB
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._itemsNotMigratedCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._manuallyTriggeredMigration
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._materialisedOnCDItemsCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._materialisedOnFPFSItemsCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._packagesWithoutBundleBit
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._previousAttempts
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._previousFailedAttempts
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._previousReleasesSuccessRate
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._rampId
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._symlinkedDocumentsFolderCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._totalItemCount
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._treatmentId
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._typesOfMigratedItemsMask
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._typesOfNonMigratedItemsMask
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._underlyingErrorCode
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._underlyingErrorDescription
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._underlyingErrorDomain
- OBJC_IVAR_$_AppTelemetryCiconiaInvestigation._unexpectedCreations
- OBJC_IVAR_$_AppTelemetryInvestigation._bouncesInvestigation
- OBJC_IVAR_$_AppTelemetryInvestigation._ciconiaInvestigation
- OBJC_IVAR_$_AppTelemetryInvestigation._eaccessInvestigation
- OBJC_IVAR_$_AppTelemetryTimeSeriesEvent._identifier
- OBJC_IVAR_$_BRCAccountSession._ciconiaState
- OBJC_IVAR_$_BRCAccountSession._ciconiaVersion
- _AppTelemetryCiconiaBouncesInvestigationReadFrom
- _AppTelemetryCiconiaEAccessInvestigationReadFrom
- _AppTelemetryCiconiaInvestigationReadFrom
- _BRCEventKindUserDownload_block_invoke_2.__personaOnceToken
- _BRCEventKindUserDownload_block_invoke_2.__personalPersona
- _BRCEventKindUserDownload_block_invoke_3.__personaOnceToken
- _BRCEventKindUserDownload_block_invoke_3.__personalPersona
- _BRCIsInternalBuild
- _BRCRegisterAndSendNewApplyFailure
- _BRCRegisterAndSendNewContainerReset
- _BRCRegisterAndSendNewFolderSharePCSChainingTime
- _BRCRegisterAndSendNewPeriodicSync
- _BRCRegisterAndSendNewShareAcceptation
- _BRCSendDictionaryToCoreAnalytics
- _BRCSendDictionaryToCoreAnalytics.cold.1
- _BRCSendDictionaryToCoreAnalytics.cold.2
- _BRCSharingNoOverrideString
- _BREntitlementCiconia
- _FPIsCloudDocsWithFPFSEnabled
- _OBJC_CLASS_$_AppTelemetryCiconiaBouncesInvestigation
- _OBJC_CLASS_$_AppTelemetryCiconiaEAccessInvestigation
- _OBJC_CLASS_$_AppTelemetryCiconiaInvestigation
- _OBJC_CLASS_$_BRDeviceConfiguration
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_IVAR_$_BRCAccountSession._ciconiaRepeatQueue
- _OBJC_IVAR_$_BRCAccountSession._ciconiaRepeatSource
- _OBJC_IVAR_$_BRCAccountsManager._isInSyncBubble
- _OBJC_IVAR_$_BRCAnalyticsReporter._currentTelemetryToken
- _OBJC_IVAR_$_BRCAnalyticsReporter._forceTelemetryDequeueQueued
- _OBJC_IVAR_$_BRCAnalyticsReporter._lastSentTelemetryEvents
- _OBJC_IVAR_$_BRCAnalyticsReporter._lastTelemetryBatchRowIDs
- _OBJC_IVAR_$_BRCAnalyticsReporter._syncTelemetryState
- _OBJC_IVAR_$_BRCAppLibrary._XPCClientsUsingUbiquity
- _OBJC_IVAR_$_BRCAppLibrary._activeAliasQueries
- _OBJC_IVAR_$_BRCAppLibrary._activeQueries
- _OBJC_IVAR_$_BRCAppLibrary._activeRecursiveQueries
- _OBJC_IVAR_$_BRCAppLibrary._db
- _OBJC_IVAR_$_BRCAppLibrary._dbRowID
- _OBJC_IVAR_$_BRCAppLibrary._deepScanReason
- _OBJC_IVAR_$_BRCAppLibrary._deepScanStamp
- _OBJC_IVAR_$_BRCAppLibrary._defaultClientZone
- _OBJC_IVAR_$_BRCAppLibrary._fileID
- _OBJC_IVAR_$_BRCAppLibrary._generationID
- _OBJC_IVAR_$_BRCAppLibrary._mangledID
- _OBJC_IVAR_$_BRCAppLibrary._maxLostStamp
- _OBJC_IVAR_$_BRCAppLibrary._pendingFileCoordinators
- _OBJC_IVAR_$_BRCAppLibrary._session
- _OBJC_IVAR_$_BRCAppTelemetryConverter._investigationKeysToRemove
- _OBJC_IVAR_$_BRCAppTelemetryConverter._oldToNewKeys
- _OBJC_IVAR_$_BRCFPFSMigrationScheduler._ciconiaStatusProvider
- _OBJC_IVAR_$_BRCFSUploader._thumbnailQueue
- _OBJC_IVAR_$_BRCFSUploader._thumbnailsOperations
- _OBJC_IVAR_$_BRCPrivateClientZone._createZoneOperation
- _OBJC_IVAR_$_BRCPrivateClientZone._createZoneQueue
- _OBJC_IVAR_$_BRCPrivateClientZone._zoneCreationCompletionBlocks
- _OBJC_IVAR_$_BRCSharingCopyParticipantTokenOperation._shouldFetchParticipantDocumentToken
- _OBJC_IVAR_$_BRCStageRegistry._currentlyDumpingForCiconia
- _OBJC_IVAR_$_BRCTrialConfiguration.ciconiaGatedForFPFSMigration
- _OBJC_IVAR_$_BRCTrialConfiguration.ignorePercentsOnInternal
- _OBJC_IVAR_$_BRCTrialConfiguration.maxFailurePerVersion
- _OBJC_IVAR_$_BRCTrialConfiguration.percent100kAndAbove
- _OBJC_IVAR_$_BRCTrialConfiguration.percentBelow100k
- _OBJC_IVAR_$_BRCTrialConfiguration.percentBelow10k
- _OBJC_IVAR_$_BRCTrialConfiguration.percentBelow1k
- _OBJC_METACLASS_$_AppTelemetryCiconiaBouncesInvestigation
- _OBJC_METACLASS_$_AppTelemetryCiconiaEAccessInvestigation
- _OBJC_METACLASS_$_AppTelemetryCiconiaInvestigation
- _UTIForExtension:.onceToken
- _UTIForExtension:.utiCache
- _XPC_ACTIVITY_INTERVAL_15_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaInvestigation
- __OBJC_$_INSTANCE_METHODS_BRCClientZone(BRCZoneReset|LegacyAdditions)
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaInvestigation
- __OBJC_$_INSTANCE_VARIABLES_BRCAppTelemetryConverter
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaInvestigation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCCiconiaStatusProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CiconiaProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRCCiconiaStatusProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CiconiaProtocol
- __OBJC_$_PROTOCOL_REFS_BRCCiconiaStatusProvider
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaInvestigation
- __OBJC_LABEL_PROTOCOL_$_BRCCiconiaStatusProvider
- __OBJC_LABEL_PROTOCOL_$_CiconiaProtocol
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaInvestigation
- __OBJC_PROTOCOL_$_BRCCiconiaStatusProvider
- __OBJC_PROTOCOL_$_CiconiaProtocol
- __OBJC_PROTOCOL_REFERENCE_$_CiconiaProtocol
- ___101-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:]_block_invoke
- ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke
- ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke.664
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.257
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.257.cold.1
- ___103-[BRCAccountSession _destroyLocalDataWaitingForFilesToBeUnlinked:pristineContainerIDs:completionBlock:]_block_invoke.260
- ___104-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke
- ___104-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke.279
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.639
- ___109-[BRCXPCRegularIPCsClient(LegacyAdditions) _sendPausedFileListBatchToUpdater:fromRowID:batchSize:completion:]_block_invoke.182
- ___111-[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:]_block_invoke.163
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.406
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.407
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.254
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.254.cold.1
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.256
- ___120-[BRCXPCRegularIPCsClient(LegacyAdditions) startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:]_block_invoke.113
- ___120-[BRCXPCRegularIPCsClient(LegacyAdditions) startOperation:toDownloadItemAtURL:readingOptions:wantsCurrentVersion:reply:]_block_invoke.115
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.198
- ___18-[BRCDaemon start]_block_invoke.91
- ___22-[BRCClientZone close]_block_invoke.62
- ___23-[BRCDaemon selfCheck:]_block_invoke.145
- ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.151
- ___25-[BRCFSUploader schedule]_block_invoke.112
- ___26-[BRCAccountSession close]_block_invoke.231
- ___26-[BRCAccountSession close]_block_invoke.233
- ___26-[BRCStageRegistry resume]_block_invoke.158
- ___26-[BRCStageRegistry resume]_block_invoke.166
- ___26-[BRCStageRegistry resume]_block_invoke.167
- ___26-[BRCStageRegistry resume]_block_invoke.167.cold.1
- ___26-[BRCStageRegistry resume]_block_invoke.167.cold.2
- ___26-[BRCStageRegistry resume]_block_invoke.167.cold.3
- ___26-[BRCSyncUpOperation main]_block_invoke.56
- ___27-[BRCClientZone _startSync]_block_invoke.180
- ___27-[BRCClientZone _startSync]_block_invoke.184.cold.1
- ___27-[BRCClientZone _startSync]_block_invoke.184.cold.2
- ___29+[BRCDaemon UTIForExtension:]_block_invoke
- ___29-[BRCAccountMigrator perform]_block_invoke.95
- ___29-[BRCAccountMigrator perform]_block_invoke.95.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.52
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.58
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.62
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.55
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.61
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.61.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.2
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.3
- ___32-[BRCPeriodicSyncOperation main]_block_invoke.15
- ___32-[BRCPeriodicSyncOperation main]_block_invoke_2.19
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.47
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.50
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.208
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.208.cold.1
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.213
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.213.cold.1
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.266
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.268
- ___35-[BRCFSDownloader makeContentLive:]_block_invoke.268.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.135
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.135.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.2
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.3
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.4
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.146
- ___37-[BRCAccountMigrationChecker perform]_block_invoke.110
- ___37-[BRCAccountMigrationChecker perform]_block_invoke.110.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.226
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.228
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.228.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.228.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.228.cold.3
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236.cold.1
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.211
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.236
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.236.cold.1
- ___40-[BRCAccountSession closeOfflineSession]_block_invoke.237
- ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_3.cold.1
- ___40-[BRCPQLConnection setProfilingEnabled:]_block_invoke.36
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.203
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.204
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.207
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.213
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.218
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.206
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.206.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.208
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.208.cold.1
- ___41-[BRCAccountSession _refreshCiconiaState]_block_invoke
- ___41-[BRCSyncUpOperation performShareUpdate:]_block_invoke.41
- ___42-[BRCPendingChangesStream destroyDatabase]_block_invoke
- ___42-[BRCPendingChangesStream destroyDatabase]_block_invoke.cold.1
- ___43-[BRCAnalyticsReporter findTelemetryEvent:]_block_invoke
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.153
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.153.cold.1
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.1
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.2
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.3
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.154.cold.4
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.156
- ___44-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke.160
- ___44-[BRCAnalyticsReporter _getPriorityOfEvent:]_block_invoke
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.261.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.268
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.268.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.271
- ___45-[BRCAccountSession _setupCiconiaRepeatQueue]_block_invoke
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.283
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.283.cold.1
- ___45-[BRCAnalyticsReporter forceTelemetryDequeue]_block_invoke
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.324
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.324.cold.1
- ___46-[BRCFSUploader setState:forUploadJobID:zone:]_block_invoke
- ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.460
- ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.333
- ___47-[BRCAccountsManager notifyAccountsListChanged]_block_invoke
- ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.80
- ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.303
- ___47-[BRCSharingCopyParticipantTokenOperation main]_block_invoke.273
- ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke.103
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.131
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.131.cold.1
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.137
- ___48-[BRCSharingAcceptFlowOperation _isAppInstalled]_block_invoke
- ___48-[BRCSharingAcceptFlowOperation _isAppInstalled]_block_invoke.cold.1
- ___49-[BRCAccountSession(BRCDatabaseManager) closeDBs]_block_invoke.402
- ___49-[BRCAccountSession(BRCDatabaseManager) closeDBs]_block_invoke.403
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.1
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.2
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.3
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.4
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.349
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.350
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.351
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.356
- ___49-[BRCFPFSMigrationScheduler _isCoconiaSuccessful]_block_invoke
- ___49-[BRCFPFSMigrationScheduler _isCoconiaSuccessful]_block_invoke_2
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.546
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.572
- ___50-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke
- ___50-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke.cold.1
- ___50-[BRCLocalItem saveToDBForServerEdit:keepAliases:]_block_invoke.cold.15
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke.cold.1
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke.cold.2
- ___50-[BRCStageRegistry setCurrentlyDumpingForCiconia:]_block_invoke
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.257
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.257.cold.1
- ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.111
- ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.111.cold.1
- ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.119
- ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke.119.cold.1
- ___51-[BRCAccountSession _pcsChainAllItemsWithActivity:]_block_invoke_2.121
- ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke.95
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.212
- ___51-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke
- ___51-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke.cold.1
- ___51-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke.cold.2
- ___51-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke.cold.3
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke.187
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke.cold.1
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_2
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_3
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_4
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_5
- ___51-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_5.cold.1
- ___51-[BRCStageRegistry _garbageCollectUploadThumbnails]_block_invoke
- ___51-[BRCUserDefaults _ciconiaOriginatorIDs:byDefault:]_block_invoke
- ___51-[BRCUserDefaults telemetryRTCPayloadKeysConverter]_block_invoke
- ___51-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke
- ___51-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke.658
- ___52-[BRCSharingAcceptFlowOperation _parseShareMetadata]_block_invoke
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.179.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.187.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.188
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.195
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.199
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.196.cold.3
- ___53-[BRCAccountsManager performWhenAccountsListChanges:]_block_invoke
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.101
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.103
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.108
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.75
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.75.cold.1
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.79
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.102
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.102.cold.1
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.106
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.110
- ___53-[BRCSharingAcceptFlowOperation _isAccountRestricted]_block_invoke
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.506
- ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.167
- ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.169
- ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.171
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76.cold.1
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76.cold.2
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.426
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.427
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.453
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.454
- ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.396
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke.124
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke_2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.1
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.3
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.4
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.5
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.39.cold.6
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.40
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.1
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.3
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.4
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.5
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.43.cold.6
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.44
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.1
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.10
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.11
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.12
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.13
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.2
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.3
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.4
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.5
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.6
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.7
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.8
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.148.cold.9
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.149
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.159
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.170
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.1
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.2
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.3
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.4
- ___55-[BRCSharingAcceptFlowOperation _setSpotlightAttribute]_block_invoke
- ___55-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke
- ___55-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke.138
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.711
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.712
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.68
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.68.cold.1
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.68.cold.2
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.68.cold.3
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.72
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.72.cold.1
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.75
- ___56+[BRCItemID migrateItemIDsToVersion5WithDB:serverTruth:]_block_invoke.75.cold.1
- ___56-[BRCPendingChangesStream _getChangesStreamSafeDBHolder]_block_invoke.127
- ___56-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk]_block_invoke
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.367
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.368
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.653
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.653.cold.1
- ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.282
- ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.284
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97.cold.1
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97.cold.2
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.482
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.482.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.482.cold.2
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.483
- ___57-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke.146
- ___57-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke.148
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_2
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_3
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_4
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.343
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.344
- ___58-[BRCAnalyticsReporter _checkSyncConsistencyWithActivity:]_block_invoke.74
- ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.188
- ___58-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively]_block_invoke
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.470
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.477
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.435
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.436
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.452
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.452.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.478
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.478.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.478.cold.2
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.478.cold.3
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.480
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.481
- ___59-[BRCServerZone dumpTablesToContext:includeAllItems:error:]_block_invoke.290
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.299
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.300
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.238
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.136
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.136.cold.1
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.cold.1
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke.200
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke_2
- ___61-[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]_block_invoke
- ___61-[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]_block_invoke.686
- ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.59
- ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.66
- ___62-[BRCAnalyticsReporter _gatherAppTelemetryEventsWithActivity:]_block_invoke.66.cold.1
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.600
- ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.451
- ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke
- ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke.688
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.85
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.85.cold.1
- ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.395
- ___65-[BRCAccountSession(BRCDatabaseManager) _appLibrariesEnumerator:]_block_invoke
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.169
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.170
- ___65-[BRCNonLocalVersionsSender(IPCs) listNonLocalVersionsWithReply:]_block_invoke.128
- ___65-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]_block_invoke
- ___65-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]_block_invoke.cold.1
- ___65-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]_block_invoke.cold.2
- ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke_2
- ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.293
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648.cold.2
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648.cold.3
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.649
- ___66-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]_block_invoke
- ___66-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]_block_invoke_2
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.609
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.610
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.612
- ___67-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke
- ___67-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke.177
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.212
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.212.cold.1
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.212.cold.2
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.217
- ___67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.651
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.440
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.440.cold.1
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.484
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.485
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke_2
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke_3
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2.cold.1
- ___68-[BRCUserNotification showJoinDialogForShareMetadata:session:reply:]_block_invoke
- ___68-[BRCUserNotification showJoinDialogForShareMetadata:session:reply:]_block_invoke_2
- ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.326
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.48
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.49
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.49.cold.1
- ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.297
- ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.428
- ___69-[BRCXPCRegularIPCsClient(LegacyAdditions) getPausedFilesList:reply:]_block_invoke.183
- ___69-[BRCXPCRegularIPCsClient(LegacyAdditions) removeItemFromDisk:reply:]_block_invoke.128
- ___70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke_5
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.408
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.408.cold.1
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.408.cold.2
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.408.cold.3
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.414
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.414.cold.1
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.414.cold.2
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.422
- ___70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.133
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.19
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.19.cold.1
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.21
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.21.cold.1
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.23
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.23.cold.1
- ___71-[BRCAnalyticsReporter _setupSyncConsistencyDeferralTimerWithActivity:]_block_invoke.68
- ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.187
- ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.187.cold.1
- ___71-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke.187.cold.2
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.489
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.490
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.498
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.498.cold.1
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.657
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.644
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke_2
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke_3
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2.cold.1
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.602
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.595
- ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.19
- ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.20
- ___73-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:]_block_invoke
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.429
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.402
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.402.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.403
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.403.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.404
- ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.652
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.369
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.384
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.571
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.573
- ___73-[BRCXPCRegularIPCsClient(LegacyAdditions) copyBulkShareIDsAtURLs:reply:]_block_invoke.109
- ___73-[BRCXPCRegularIPCsClient(LegacyAdditions) copyBulkShareIDsAtURLs:reply:]_block_invoke.111
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.73
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.73.cold.1
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.80
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.80.cold.1
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.80.cold.2
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.95
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_2.101
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_3.107
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_4
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_4.114
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5.120
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5.cold.1
- ___74+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_6
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.77
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.84
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.88
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.85
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.90
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.616
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.618
- ___74-[BRCXPCRegularIPCsClient(LegacyAdditions) getURLForItemIdentifier:reply:]_block_invoke.102
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.21
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.21.cold.1
- ___75-[BRCAccountSession(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.129
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397.cold.1
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397.cold.2
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.398
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.398.cold.1
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.613
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.614
- ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) gatherInformationForPath:reply:]_block_invoke.176
- ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveFileObjectIDToURL:reply:]_block_invoke.186.cold.1
- ___75-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveFileObjectIDToURL:reply:]_block_invoke.187
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.774
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.777
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.776
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.776.cold.1
- ___76-[BRCAccountSession(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]_block_invoke
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.193
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.193.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194.cold.2
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.569
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.598
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.1
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.2
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.3
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.4
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.5
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.27
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.31
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.34
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.cold.1
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.cold.2
- ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.433
- ___79-[BRCAnalyticsReporter _resumePausedTreeConsistencyCheckOperationWithActivity:]_block_invoke.73
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.566
- ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.321
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.455
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.456
- ___80-[BRCXPCRegularIPCsClient(LegacyAdditions) resolveConflictWithName:atURL:reply:]_block_invoke.119
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.63
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.65
- ___81-[BRCDocumentItem(LegacyAdditions) resumeSyncForBundleID:dropLocalChanges:error:]_block_invoke.97
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.635
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.570
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.637
- ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.143
- ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.143.cold.1
- ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.143.cold.2
- ___81-[BRCXPCRegularIPCsClient(LegacyAdditions) fetchLatestVersionForFileAtURL:reply:]_block_invoke.155
- ___82-[BRCAccountHandler shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup]_block_invoke
- ___82-[BRCAccountSession shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup]_block_invoke
- ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.66
- ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke
- ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke.659
- ___82-[BRCXPCRegularIPCsClient(LegacyAdditions) checkIfItemIsShareableWithInode:reply:]_block_invoke.188
- ___83-[BRCAnalyticsReporter _setupSyncConsistencyCancellationTimerWithActivity:session:]_block_invoke.71
- ___83-[BRCClientZone didSyncDownRequestID:maxApplyRank:caughtUpWithServer:syncDownDate:]_block_invoke.265
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.292
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.292.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.357
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.357.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.366
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.375
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.375.cold.1
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.370
- ___84-[BRCAccountSession(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.370.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.516
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.518
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.512
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.515
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.641
- ___84-[BRCXPCRegularIPCsClient(LegacyAdditions) _gatherInformationForPath:session:reply:]_block_invoke.175
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.468
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.469
- ___85-[BRCXPCRegularIPCsClient(LegacyAdditions) launchItemCountMismatchChecksAtURL:reply:]_block_invoke
- ___85-[BRCXPCRegularIPCsClient(LegacyAdditions) launchItemCountMismatchChecksAtURL:reply:]_block_invoke.101
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.351
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.352
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.353
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.519
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.521
- ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.290
- ___87-[BRCXPCRegularIPCsClient(LegacyAdditions) waitForFileSystemChangeProcessingWithReply:]_block_invoke.185
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.575
- ___88-[BRCXPCRegularIPCsClient(LegacyAdditions) getBackReferencingContainerIDsForURLs:reply:]_block_invoke.178
- ___88-[BRCXPCRegularIPCsClient(LegacyAdditions) pauseSyncForFileAtURL:timeout:options:reply:]_block_invoke.141
- ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke
- ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke.663
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.578
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.579
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.580
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.581
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.582
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.586
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.589
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.590
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.591
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.587
- ___90-[BRCXPCRegularIPCsClient(LegacyAdditions) resumeSyncForFileAtURL:dropLocalChanges:reply:]_block_invoke.142
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.627
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.348
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.349
- ___94-[BRCXPCRegularIPCsClient(LegacyAdditions) forceConflictForURL:bookmarkData:forcedEtag:reply:]_block_invoke.121
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.712
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.712.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.713
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.447
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.447.cold.1
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.451
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.15
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.15.cold.1
- ___97-[BRCAccountsManager shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollupForAllAccounts]_block_invoke
- ___BRCSendDictionaryToCoreAnalytics_block_invoke
- ___Block_byref_object_copy_.107
- ___Block_byref_object_dispose_.108
- ___block_descriptor_32_e21_v32?0?<v?>8Q16^B24l
- ___block_descriptor_40_e8_32s_e18_16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v12?0I8ls32l8
- ___block_descriptor_48_e8_32bs40w_e30_v24?0"NSNumber"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e23_v16?0"CKRequestInfo"8ls32l8s40l8
- ___block_descriptor_56_e8_32r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr32l8
- ___block_descriptor_64_e8_32s40s48bs56r_e20_v24?08"NSError"16lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e23_v16?0"PQLConnection"8ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88w_e17_v16?0"NSError"8ls32l8s40l8w88l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.103
- ___block_literal_global.109
- ___block_literal_global.116
- ___block_literal_global.1171
- ___block_literal_global.1189
- ___block_literal_global.122
- ___block_literal_global.124
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.136
- ___block_literal_global.137
- ___block_literal_global.15
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.1615
- ___block_literal_global.166
- ___block_literal_global.1667
- ___block_literal_global.1670
- ___block_literal_global.168
- ___block_literal_global.1699
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.1721
- ___block_literal_global.173
- ___block_literal_global.1733
- ___block_literal_global.1787
- ___block_literal_global.181
- ___block_literal_global.1813
- ___block_literal_global.1824
- ___block_literal_global.1830
- ___block_literal_global.1837
- ___block_literal_global.1839
- ___block_literal_global.1884
- ___block_literal_global.190
- ___block_literal_global.198
- ___block_literal_global.2067
- ___block_literal_global.209
- ___block_literal_global.2099
- ___block_literal_global.2105
- ___block_literal_global.211
- ___block_literal_global.2110
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.2377
- ___block_literal_global.239
- ___block_literal_global.2392
- ___block_literal_global.243
- ___block_literal_global.246
- ___block_literal_global.2477
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.261
- ___block_literal_global.270
- ___block_literal_global.278
- ___block_literal_global.292
- ___block_literal_global.297
- ___block_literal_global.302
- ___block_literal_global.305
- ___block_literal_global.317
- ___block_literal_global.331
- ___block_literal_global.366
- ___block_literal_global.369
- ___block_literal_global.398
- ___block_literal_global.405
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.420
- ___block_literal_global.437
- ___block_literal_global.453
- ___block_literal_global.458
- ___block_literal_global.46
- ___block_literal_global.463
- ___block_literal_global.468
- ___block_literal_global.473
- ___block_literal_global.478
- ___block_literal_global.483
- ___block_literal_global.491
- ___block_literal_global.496
- ___block_literal_global.503
- ___block_literal_global.54
- ___block_literal_global.549
- ___block_literal_global.57
- ___block_literal_global.59
- ___block_literal_global.61
- ___block_literal_global.64
- ___block_literal_global.69
- ___block_literal_global.74
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.788
- ___block_literal_global.794
- ___block_literal_global.798
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.97
- ___br_fixup_tables_7_002_block_invoke.1832
- ___br_fixup_tables_7_002_block_invoke_2.1835
- ___br_update_tables_10_000_block_invoke.1009
- ___br_update_tables_14_000_block_invoke.1187
- ___br_update_tables_14_000_block_invoke.1187.cold.1
- ___recursive_table_recreate_schema_block_invoke.1668
- ___recursive_table_recreate_schema_block_invoke.1668.cold.1
- __getPriorityOfEvent:.HIGH_PRIORITY_EVENTS
- __getPriorityOfEvent:.HIGH_PRIORITY_TELEMTRY_DOMAINS
- __getPriorityOfEvent:.onceToken
- __isCoconiaSuccessful.onceToken
- __refreshCiconiaState.__personaOnceToken
- __refreshCiconiaState.__personalPersona
- __unnamed_array_storage.150
- __unnamed_array_storage.1545
- __unnamed_array_storage.1588
- __unnamed_array_storage.1712
- __unnamed_array_storage.1713
- __unnamed_array_storage.2453
- __unnamed_array_storage.2471
- __unnamed_array_storage.2628
- __unnamed_array_storage.2640
- __unnamed_array_storage.2726
- __unnamed_array_storage.439
- __unnamed_array_storage.442
- _dispatch_set_qos_class_fallback
- _getegid
- _kBRCiconiaVersion
- _kSymptomDiagnosticActionGetNetworkInfo
- _objc_msgSend$_cancelCiconiaRepeatQueue
- _objc_msgSend$_checkSyncConsistencyWithActivity:
- _objc_msgSend$_ciconiaOriginatorIDs:byDefault:
- _objc_msgSend$_cleanupAPFSSnapshotWhenNoSessionExists
- _objc_msgSend$_doneFetchingThumbnailForJobID:
- _objc_msgSend$_fetchTelemetryEventCountOrAdd:
- _objc_msgSend$_garbageCollectUploadThumbnails
- _objc_msgSend$_getPriorityOfEvent:
- _objc_msgSend$_isCiconiaErrorTTRWorthy:
- _objc_msgSend$_isCoconiaSuccessful
- _objc_msgSend$_isExpectedCiconiaError:
- _objc_msgSend$_isExpectedCiconiaError:originatorId:
- _objc_msgSend$_launchItemCountMismatchChecksForLocalItem:itemIdentifier:reply:
- _objc_msgSend$_openAppStoreForShareURL:
- _objc_msgSend$_openShareURLInWebBrowser:withReason:
- _objc_msgSend$_openiCloudSettings
- _objc_msgSend$_performModifyRecordsOrPCSChainOperationWithCompletion:
- _objc_msgSend$_prepareSyncTelemetryEventsToSend
- _objc_msgSend$_refreshCiconiaState
- _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:
- _objc_msgSend$_reportEAccessDuringSilentMigration:uuid:
- _objc_msgSend$_reportFailedQueueingMigration:
- _objc_msgSend$_reportOverBounceDuringSilentMigration:total:uuid:
- _objc_msgSend$_saveItemID:version:record:iWorkSharingOptions:
- _objc_msgSend$_setTelemetryHeaderOnCKOpIfNecessary:
- _objc_msgSend$_setXattrs:session:
- _objc_msgSend$_setupCiconiaRepeatQueue
- _objc_msgSend$_startCiconiaIfRelevant
- _objc_msgSend$_startFetchThumbnail:jobID:
- _objc_msgSend$_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:
- _objc_msgSend$_thumbnailOperationForItemRowID:
- _objc_msgSend$_updateCiconiaState:uuid:
- _objc_msgSend$allowForceTelemetryDequeue
- _objc_msgSend$appTelemetryGatherXPCActivity
- _objc_msgSend$bounceReport
- _objc_msgSend$bouncedDocumentsFolders
- _objc_msgSend$bouncedItems
- _objc_msgSend$bouncedItemsMatrix
- _objc_msgSend$br_quotaUpdateTelemetry
- _objc_msgSend$captureLogsForOperationType:ofSubtype:withContext:
- _objc_msgSend$ciconiaDisableAutomatedStart
- _objc_msgSend$ciconiaGatedForFPFSMigration
- _objc_msgSend$ciconiaMaxFailurePerVersion
- _objc_msgSend$ciconiaOriginatorIDsTTRWorthy
- _objc_msgSend$ciconiaOriginatorIDsToTreatAsSuccess
- _objc_msgSend$ciconiaRepeatInterval
- _objc_msgSend$ciconiaSkipTrial
- _objc_msgSend$ciconiaState
- _objc_msgSend$cleanupCiconiaForPersonaID:atURL:diagnosticsURL:withReply:
- _objc_msgSend$cleanupStateURL
- _objc_msgSend$cloningDuration
- _objc_msgSend$cloudEnabledStatusForSession:
- _objc_msgSend$container
- _objc_msgSend$copyItemAtPath:toPath:error:
- _objc_msgSend$crashReporterKey
- _objc_msgSend$createSQLConditionForRowIDs:
- _objc_msgSend$datalessItems
- _objc_msgSend$deserializeVersion:fakeStatInfo:clientZone:error:
- _objc_msgSend$documentsFoldersWithoutItemID
- _objc_msgSend$dropAllSyncTelemetryEvents
- _objc_msgSend$dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:
- _objc_msgSend$eaccessReport
- _objc_msgSend$expectedAmountOfItemsMigrated
- _objc_msgSend$fetchParticipantDocumentToken
- _objc_msgSend$finishCleanupForPersonaID:withReply:
- _objc_msgSend$forceTelemetryDequeue
- _objc_msgSend$forceTelemetryDequeuePercentage
- _objc_msgSend$forceTelemetryDequeueWithCompletionHandler:
- _objc_msgSend$getMigrationAttemptOriginatorIDsForVersion:withDB:
- _objc_msgSend$getPreviousMigrationAttempts:failed:beforeVersion:
- _objc_msgSend$getPreviousMigrationAttempts:failed:forVersion:
- _objc_msgSend$getPreviousMigrationAttempts:failed:withVersion:comperator:
- _objc_msgSend$has_acls
- _objc_msgSend$highPriorityTelemetryEventsPercentage
- _objc_msgSend$ignorePercentsOnInternal
- _objc_msgSend$ignoredContentProtectedItems
- _objc_msgSend$importDuration
- _objc_msgSend$incidents
- _objc_msgSend$initForTestingDevice:
- _objc_msgSend$initWithCiconiaStatusProvider:
- _objc_msgSend$initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:
- _objc_msgSend$initWithRecordID:serverZone:isUserWaiting:
- _objc_msgSend$initWithShareMetadata:client:session:
- _objc_msgSend$isShuttingDown
- _objc_msgSend$itemsChangedDuringCloning
- _objc_msgSend$itemsNotFoundInDB
- _objc_msgSend$itemsThatAreNotMigrated
- _objc_msgSend$lastCiconiaVersion:
- _objc_msgSend$lazyXattrWithSession:
- _objc_msgSend$longLongForFactor:client:namespace:min:max:byDefault:
- _objc_msgSend$manuallyTriggered
- _objc_msgSend$materialisedCountOnFPFS
- _objc_msgSend$materialisedCountOnICD
- _objc_msgSend$maxFailurePerVersion
- _objc_msgSend$minForceTelemetrySyncInterval
- _objc_msgSend$newAppLibraryFromPQLResultSet:error:
- _objc_msgSend$newAppTelemetryMetricEvent:
- _objc_msgSend$newCiconiaReportEvent:state:
- _objc_msgSend$newDoubleEvent:eventGroupUUID:value:
- _objc_msgSend$newDroppedEventWithCount:
- _objc_msgSend$newIntEvent:eventGroupUUID:value:
- _objc_msgSend$newLongEvent:eventGroupUUID:value:
- _objc_msgSend$newLongEvent:eventGroupUUID:value:round:
- _objc_msgSend$newTimestampEvent:eventGroupUUID:value:
- _objc_msgSend$nonSideFaultsCompletelyMigrated
- _objc_msgSend$notifyAccountsListChanged
- _objc_msgSend$numberFromString:
- _objc_msgSend$offline
- _objc_msgSend$orderedSet
- _objc_msgSend$packageItemsForFileObjectID:order:db:
- _objc_msgSend$packagesWithoutBundleBit
- _objc_msgSend$percent100kAndAbove
- _objc_msgSend$percentBelow100k
- _objc_msgSend$percentBelow10k
- _objc_msgSend$percentBelow1k
- _objc_msgSend$performWhenAccountsListChanges:
- _objc_msgSend$protection_class
- _objc_msgSend$providerDomainWithID:error:
- _objc_msgSend$queueSilentMigrationActivityForPersonaID:withReply:
- _objc_msgSend$requireSuccessfulCiconiaRunForFPFSMigration
- _objc_msgSend$responseHTTPHeaders
- _objc_msgSend$saveMigrationAttemptForReport:uuid:
- _objc_msgSend$serializeFilename:forCreation:
- _objc_msgSend$serializeFilename:forCreation:setExtension:
- _objc_msgSend$serializeFilename:forCreation:setExtension:inSharedAlias:
- _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:
- _objc_msgSend$serializeVersion:diffs:deadInServerTruth:
- _objc_msgSend$setAccountQuotaUsage:
- _objc_msgSend$setAliasToFileCount:
- _objc_msgSend$setAliasToFolderCount:
- _objc_msgSend$setAliasToPackageCount:
- _objc_msgSend$setAliasToSymlinkCount:
- _objc_msgSend$setAreMigratedFaultsBelowThreshold:
- _objc_msgSend$setAreNonFaultAllMigrated:
- _objc_msgSend$setBouncedDocumentsFoldersCount:
- _objc_msgSend$setBouncedItemsCount:
- _objc_msgSend$setBouncedItemsMatrix:
- _objc_msgSend$setBouncesInvestigation:
- _objc_msgSend$setCiconiaInvestigation:
- _objc_msgSend$setCiconiaState:
- _objc_msgSend$setCiconiaVersion:
- _objc_msgSend$setCloningTime:
- _objc_msgSend$setCrashReporterKey:
- _objc_msgSend$setCurGid:
- _objc_msgSend$setCurUid:
- _objc_msgSend$setCurrentlyDumpingForCiconia:
- _objc_msgSend$setDatalessItemsCount:
- _objc_msgSend$setDiskSpaceLeft:
- _objc_msgSend$setDocumentsFoldersWithoutItemIDCount:
- _objc_msgSend$setEaccessInvestigation:
- _objc_msgSend$setExpectedMigratedItemsCount:
- _objc_msgSend$setFileToAliasCount:
- _objc_msgSend$setFileToFolderCount:
- _objc_msgSend$setFileToPackageCount:
- _objc_msgSend$setFileToSymlinkCount:
- _objc_msgSend$setFolderToAliasCount:
- _objc_msgSend$setFolderToFileCount:
- _objc_msgSend$setFolderToPackageCount:
- _objc_msgSend$setFolderToSymlinkCount:
- _objc_msgSend$setIdentifier:
- _objc_msgSend$setIgnoredContentProtectedItems:
- _objc_msgSend$setImportTime:
- _objc_msgSend$setIsAccountDataSeparated:
- _objc_msgSend$setItemsChangedDuringCloning:
- _objc_msgSend$setItemsNotFoundInDB:
- _objc_msgSend$setItemsNotMigratedCount:
- _objc_msgSend$setManuallyTriggeredMigration:
- _objc_msgSend$setMaterialisedOnCDItemsCount:
- _objc_msgSend$setMaterialisedOnFPFSItemsCount:
- _objc_msgSend$setNonConflictingKindCount:
- _objc_msgSend$setNumberStyle:
- _objc_msgSend$setPackageToAliasCount:
- _objc_msgSend$setPackageToFileCount:
- _objc_msgSend$setPackageToFolderCount:
- _objc_msgSend$setPackageToSymlinkCount:
- _objc_msgSend$setPackagesWithoutBundleBit:
- _objc_msgSend$setPreviousAttempts:
- _objc_msgSend$setPreviousFailedAttempts:
- _objc_msgSend$setPreviousReleasesSuccessRate:
- _objc_msgSend$setProtectionClass:
- _objc_msgSend$setRequestCompletedBlock:
- _objc_msgSend$setStGid:
- _objc_msgSend$setStUid:
- _objc_msgSend$setSymlinkToAliasCount:
- _objc_msgSend$setSymlinkToFileCount:
- _objc_msgSend$setSymlinkToFolderCount:
- _objc_msgSend$setSymlinkToPackageCount:
- _objc_msgSend$setSymlinkedDocumentsFolderCount:
- _objc_msgSend$setTelemetryToken:
- _objc_msgSend$setToken:
- _objc_msgSend$setTotalItemCount:
- _objc_msgSend$setTypesOfMigratedItemsMask:
- _objc_msgSend$setTypesOfNonMigratedItemsMask:
- _objc_msgSend$setUnderlyingErrorCode:
- _objc_msgSend$setUnderlyingErrorDescription:
- _objc_msgSend$setUnderlyingErrorDomain:
- _objc_msgSend$setUnexpectedCreations:
- _objc_msgSend$shouldIgnoreReportForOperationType:ofSubtype:forError:
- _objc_msgSend$shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup
- _objc_msgSend$shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollupForAllAccounts
- _objc_msgSend$shouldStartCiconiaBasedOnItemsCountWithAcountHash:
- _objc_msgSend$showJoinDialogForShareMetadata:session:reply:
- _objc_msgSend$sideFaultsBelowThreshold
- _objc_msgSend$st_flags
- _objc_msgSend$st_gid
- _objc_msgSend$st_mode
- _objc_msgSend$st_uid
- _objc_msgSend$startedUpInSyncBubble
- _objc_msgSend$structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:
- _objc_msgSend$structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:
- _objc_msgSend$submitSyncTelemetryEvent:
- _objc_msgSend$symlinkedDocumentsFolders
- _objc_msgSend$syncConsistencyCheckerEnabled
- _objc_msgSend$syncConsistencyCheckerXPCActivity
- _objc_msgSend$syncTelemetryEventsToSend
- _objc_msgSend$telemetryEventDisabledMessages
- _objc_msgSend$telemetryEventQueueReductionAmount
- _objc_msgSend$telemetryEventReportBatchSize
- _objc_msgSend$telemetryHeaderSupportedClasses
- _objc_msgSend$telemetryRTCDisabledInvestigationKeys
- _objc_msgSend$telemetryRTCPayloadKeysConverter
- _objc_msgSend$telemetryToken
- _objc_msgSend$thumbnailUploadAgeDelta
- _objc_msgSend$thumbnailsOperationsByID
- _objc_msgSend$token
- _objc_msgSend$totalItemCount
- _objc_msgSend$typeOfMigrated
- _objc_msgSend$typeOfNotMigrated
- _objc_msgSend$unexpectedCreations
- _objc_msgSend$updateCurrentTelemetryToken:
- _objc_msgSend$userNotificationClass
- _packageItemsOrderedByPathForFileObjectID
- _performWhenAccountsListChanges:.onceToken
CStrings:
+ "\x01\x13\x12\x11\x1a"
+ "\x01\x1a"
+ "\x01&\x11\x18\x11#"
+ "\x04\x19\x11\x17"
+ "\b\x11\"\x11\x1c\x13\x14\x1f\x01\x12\""
+ "\t\x15\x18\xf0/5\x11\x12\x1f\n"
+ "\x13\x13"
+ "   o %@ [appLib]"
+ "   o %@ [zone]"
+ " (SB)"
+ " base-valid{%@}"
+ " child-base-salt-validation{%@}"
+ " child-valid{%@}"
+ " salt-st{%@}"
+ "%@%s"
+ "%@:%@;"
+ "%@::"
+ "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]"
+ "+[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:]"
+ "+[BRDSIDString(BRCPathAdditions) brc_dbAccountDSIDForPath:]"
+ "+[NSData(BRCCryptographicAdditions) brc_generateSaltingKey]"
+ ", upload_error = %@ "
+ "-[BRCAccountHandler initWithACAccountID:]"
+ "-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]"
+ "-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke"
+ "-[BRCAccountsManager loadAccounts]"
+ "-[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:]"
+ "-[BRCAppLibrary setChildBasehashSalt:]"
+ "-[BRCAppLibrary setSaltingState:]"
+ "-[BRCApplyScheduler deleteNonRejectionJobsForZone:]"
+ "-[BRCAutoBugCaptureReporter _shouldIgnoreReportForOperationType:ofSubtype:forError:]"
+ "-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]"
+ "-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke"
+ "-[BRCClientZone _registerOperation:throttler:]"
+ "-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:]"
+ "-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]"
+ "-[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:]"
+ "-[BRCClientZone(BRCBaseHashSaltAdditions) saltingStateForItemID:]"
+ "-[BRCDaemon _dbgSleepIfRequested]"
+ "-[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:]"
+ "-[BRCFSUploader _cancelJobs:state:uploadError:]"
+ "-[BRCFSUploader _rescheduleJobsPendingScreenUnlock]"
+ "-[BRCFSUploader initWithAccountSession:]_block_invoke_6"
+ "-[BRCFSUploader setState:forUploadJobID:zone:uploadError:]"
+ "-[BRCItemID debugItemIDStringWithVerbose:]"
+ "-[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:]"
+ "-[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:]"
+ "-[BRCLocateRecordOperation initWithRecordID:serverZone:isUserWaiting:maxBackoff:]"
+ "-[BRCMiniCiconia _cleanupOldCiconiaDomains:]"
+ "-[BRCMiniCiconia _cleanupOldCiconiaDomains:]_block_invoke"
+ "-[BRCMiniCiconia _removeFPDomain:error:]"
+ "-[BRCMiniCiconia _removeFPDomain:error:]_block_invoke"
+ "-[BRCMiniCiconia _removeWorkDirectory:]"
+ "-[BRCPQLConnection _registerStaticDBFunctionsWithError:]"
+ "-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke"
+ "-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_5"
+ "-[BRCPQLConnection _registerStaticDBFunctionsWithError:]_block_invoke_6"
+ "-[BRCSQLBackedSet _createSchemaForSQLType:error:]"
+ "-[BRCSQLBackedSet addObject:error:]"
+ "-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]"
+ "-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke"
+ "-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke"
+ "-[BRCSaltingBatchOperation _buildRecordsWithCompletion:]_block_invoke"
+ "-[BRCSaltingBatchOperation _createStructureRecordForRootItem]"
+ "-[BRCSaltingBatchOperation _createStructureRecordForServerItem:salt:]"
+ "-[BRCSaltingBatchOperation initWithRootItem:]"
+ "-[BRCSaltingBatchOperation main]_block_invoke_2"
+ "-[BRCServerZone _fixupAdvancedDataProtectionState]"
+ "-[BRCServerZone _saveItemID:version:record:contentBoundaryKey:iWorkSharingOptions:]"
+ "-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _finishShareAccept_step]"
+ "-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_5"
+ "-[BRCSharingAcceptFlowOperation _isAccountRestricted_step]"
+ "-[BRCSharingAcceptFlowOperation _isAppInstalled_step]"
+ "-[BRCSharingAcceptFlowOperation _isAppInstalled_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _isFolderSharingSupported_step]"
+ "-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]"
+ "-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded_step]"
+ "-[BRCSharingAcceptFlowOperation _openSharedSideFaultFile_step]"
+ "-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step]"
+ "-[BRCSharingAcceptFlowOperation _parseShareMetadata_step]"
+ "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]"
+ "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]"
+ "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _startShareAccept_step]"
+ "-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2"
+ "-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_3"
+ "-[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]"
+ "-[BRCStatInfo lazyXattrWithStageRegistry:]"
+ "-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke"
+ "-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke_2"
+ "-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke"
+ "-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke_2"
+ "-[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToSaltingBasehashItem:]"
+ "-[BRCSyncUpOperationBuilder _getSaltForItem:]"
+ "-[BRCSyncUpOperationBuilder _recoverItemIDChangedWhileUploadingIfNecessary:]"
+ "-[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]_block_invoke"
+ "-[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]_block_invoke"
+ "-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]"
+ "-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]_block_invoke"
+ "-[BRCUTITypeCache _invalidateCahceIfNeeded]"
+ "-[BRCUserActionsNavigator openAppStoreForBundleID:]"
+ "-[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:]"
+ "-[BRCVersion lazyXattrWithStageRegistry:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]"
+ "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]"
+ "-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(LegacyAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke_2"
+ "-[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:]"
+ "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]"
+ "-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke"
+ "-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke_2"
+ "1.1"
+ "2\x14\x15\x11"
+ "<%@ count:%lu>"
+ "<%@ saltingState:'%@' basehashValidation: '%@' >"
+ "<BRCSafeDBHolder %p>"
+ "@\"<BRCUserNavigationActions>\""
+ "@\"BRCBasehashSaltInfo\""
+ "@\"BRCThumbnailGenerationManager\""
+ "@\"NSCache\""
+ "@\"NSData\"16@?0@\"BRCLocalItem\"8"
+ "@\"NSMutableArray<NSFileProviderItem>\""
+ "@24@?0@\"NSString\"8Q16"
+ "@36@0:8@16B24d28"
+ "@36@0:8@16i24^@28"
+ "@40@0:8#16@24^@32"
+ "@44@0:8@16@24B32d36"
+ "@48@0:8B16@20C28@?32@40"
+ "@48@0:8B16C20@24@?32@40"
+ "@56@0:8@16@24@32@40@48"
+ "@96@0:8@16@24@32@40@48@56B64B68B72@76@84I92"
+ "Advanced Data Protection Not Enabled"
+ "B56@0:8@16@24@32@40Q48"
+ "B56@0:8@16@24B32B36@40^@48"
+ "B56@0:8^@16^@24^@32@40^@48"
+ "BRCAdvancedDataProtectionAdditions"
+ "BRCBaseHashSaltAdditions"
+ "BRCBasehashSaltInfo"
+ "BRCDeviceConfiguration"
+ "BRCEventsAnalytics"
+ "BRCFlatLevelEnumerator"
+ "BRCMiniCiconia"
+ "BRCSQLBackedSet"
+ "BRCSaltingBatchOperation"
+ "BRCScreenLockDelegate"
+ "BRCThumbnailGenerationManager"
+ "BRCUTITypeCache"
+ "BRCUserActionsNavigator"
+ "BRCUserNavigationActions"
+ "BRScreenLockObserver"
+ "CREATE TABLE array_items (item %@ PRIMARY KEY)"
+ "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, service))"
+ "DANGLING_ZOMBIE_DIRECTORY_COUNT"
+ "EDS"
+ "Got a nil account path"
+ "INSERT OR IGNORE INTO array_items (item) VALUES (%@)"
+ "INSERT OR REPLACE INTO app_libraries (rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state)  VALUES (%@, %@, %@, %@, %@, %@)"
+ "J\"F\x12"
+ "Library/CloudStorage/"
+ "ORDER BY item ASC"
+ "ORDER BY item DESC"
+ "ORDER BY rowid"
+ "Possible issue in QL, Thumbnail generation operation was running for too long"
+ "SELECT child_basehash_salt FROM server_items WHERE item_id = %@ AND zone_rowid = %@ LIMIT 1"
+ "SELECT csu.throttle_id, csu.last_try_stamp, li.zone_rowid FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
+ "SELECT date FROM boot_history ORDER BY rowid DESC LIMIT 1"
+ "SELECT item FROM array_items %@"
+ "SELECT item_origname, item_filename FROM server_items  WHERE item_id = %@ AND item_parent_id = %@ AND +zone_rowid = %@"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_state = 1    AND li.item_localsyncupstate = 4    AND NOT EXISTS(SELECT 1 FROM client_items AS ci                     WHERE li.item_id = ci.item_parent_id                      AND ci.zone_rowid = su.zone_rowid                      AND ci.item_state != -2)    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (1, 2, 8, 5, 6, 7, 3)    AND li.item_state = 0    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su  ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (0, 9, 10, 4)    AND (li.item_state = 0)    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries WHERE zone_rowid = %@"
+ "SELECT salting_state FROM server_items WHERE item_id = %@ AND zone_rowid = %@ LIMIT 1"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND basehash_salt_validation_key IS NULL and zone_rowid = %@"
+ "SHARED_IPAD"
+ "SYNC_BUBBLE"
+ "T@\"BRCBasehashSaltInfo\",R,N,V_basehashSaltInfo"
+ "T@\"BRCLocalItem\",&,N,V_itemNeedingBasehashSalting"
+ "T@\"BRCLocalItem\",R,N,V_itemNeedingBasehashSalting"
+ "T@\"BRCPQLConnection\",&,N,V_database"
+ "T@\"BRCThumbnailGenerationManager\",R,N,V_thumbnailGenerationManager"
+ "T@\"NSData\",&,N,V_basehashSaltValidation"
+ "T@\"NSData\",&,N,V_childBasehashSalt"
+ "T@\"NSData\",R,N,V_rootChildBasehashSalt"
+ "T@\"NSDictionary\",R,N,GgetConfiguration"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_hasThumbnailAvailableSlot"
+ "T@?,C,N,V_metadataCompletionBlock"
+ "T@?,C,N,V_reachedThumbnailMaximumCapacity"
+ "TB,N,V_throttledItemInBatch"
+ "TB,N,V_timedOut"
+ "TB,N,V_verbose"
+ "TB,R,N,V_isSyncBubbleClientEntitled"
+ "TESTING"
+ "TI,N,V_saltingState"
+ "TI,N,V_telemetrySchema"
+ "Td,N,V_maxBackoff"
+ "Td,N,V_timeout"
+ "Thumbnail generation operation got timeouted after %fs"
+ "UPDATE app_libraries SET app_library_plist = %@, zone_rowid = %@, child_basehash_salt = %@, salting_state = %@ WHERE rowid = %@"
+ "UPDATE app_libraries SET child_basehash_salt = %@,  salting_state = %@ WHERE rowid = %@ "
+ "UPDATE app_libraries SET child_basehash_salt = validation_key(child_basehash_salt)"
+ "UPDATE client_items SET version_upload_error = NULL WHERE rowid IN (SELECT throttle_id FROM client_uploads WHERE throttle_state = 35)"
+ "UPDATE client_uploads    SET throttle_state = %d, %@ transfer_operation = NULL  WHERE %@"
+ "UPDATE client_uploads SET  throttle_state = %d, transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL%@ WHERE throttle_id = %@"
+ "UPDATE client_uploads SET throttle_state = 1, next_retry_stamp = 0  WHERE throttle_id IN (SELECT cu.throttle_id from client_uploads AS cu LEFT JOIN client_items AS ci                       ON cu.throttle_id = ci.rowid                        WHERE cu.throttle_state = 33                         AND call_block(%p, ci.version_upload_error))"
+ "UPDATE client_uploads SET throttle_state = 1, upload_error = NULL WHERE throttle_state = 35"
+ "UPDATE server_items SET basehash_salt_validation_key = %@  WHERE item_id = %@"
+ "UPDATE server_items SET child_basehash_salt = %@,  salting_state = %@ WHERE item_id = %@ AND zone_rowid = %@ "
+ "UPDATE server_items SET child_basehash_salt = validation_key(child_basehash_salt), content_boundary_key = validation_key(content_boundary_key)"
+ "[CRIT] %@ - Error closing BRCPendingChangesStream DB connection: %@%@"
+ "[CRIT] Assertion failed: BRNeedsSalting(state)%@"
+ "[CRIT] Assertion failed: _childBasehashSalt == nil%@"
+ "[CRIT] Assertion failed: _parentItemIDToChildBasehashSalt[item.itemID] == nil%@"
+ "[CRIT] Assertion failed: _parentItemIDToChildBasehashSalt[parentItemID] == nil%@"
+ "[CRIT] Assertion failed: appLibraryRowID%@"
+ "[CRIT] Assertion failed: parentItemID != nil%@"
+ "[CRIT] Assertion failed: record != nil%@"
+ "[CRIT] Assertion failed: record.encryptedValues[kBRRecordKeyChildBasehashSalt]%@"
+ "[CRIT] Assertion failed: salt != nil%@"
+ "[CRIT] Assertion failed: self.isPrivateZone%@"
+ "[CRIT] Assertion failed: si != nil%@"
+ "[CRIT] UNREACHABLE: %@ is not in mmcsV2 when it should be%@"
+ "[CRIT] UNREACHABLE: %@ is not rounded the correct amount%@"
+ "[CRIT] UNREACHABLE: Can't compute padded file size%@"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for _br_signalEnumeratorForContainerItemIdentifier retry%@"
+ "[CRIT] UNREACHABLE: Rounding amount should be at least 1 minute%@"
+ "[CRIT] UNREACHABLE: can't initialize document with invalid library rowid %@%@"
+ "[CRIT] UNREACHABLE: can't initialize library root with invalid library rowid %@%@"
+ "[CRIT] UNREACHABLE: can't initialize shared zone root with invalid zone rowid %@%@"
+ "[DEBUG] %@ - Database closed%@"
+ "[DEBUG] <BRCSafeDBHolder %p> - Creating for db in path: %@%@"
+ "[DEBUG] <BRCSafeDBHolder %p> - dealloc called%@"
+ "[DEBUG] Application proxy: %@, proxy.bundleURL = %@%@"
+ "[DEBUG] Apply Changes: Deleted %llu non-rejection jobs%@"
+ "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
+ "[DEBUG] Creating sync task%@"
+ "[DEBUG] Dedicating this sync up operation to %@ %@%@"
+ "[DEBUG] Deleting old sync up job%@"
+ "[DEBUG] Finished metadata salting a batch for item %@ when completed: %d error: %@%@"
+ "[DEBUG] Found cached child basehash salt %@ for parent %@%@"
+ "[DEBUG] Found child basehash salt %@ from database for %@%@"
+ "[DEBUG] Found old domain %@, dropping%@"
+ "[DEBUG] Generated child basehash salt %@ for %@%@"
+ "[DEBUG] Generated root child basehash salt %@ for %@%@"
+ "[DEBUG] Generating thumbnail for ID %@ (shouldTransferThumbnail:yes) %@%@"
+ "[DEBUG] Got unexpected exception %@. rethrow%@"
+ "[DEBUG] Invalidating UTI cache%@"
+ "[DEBUG] Keeping bounce of %@ even though it clashes with %@%@"
+ "[DEBUG] Learning new child basehash salt %@ from %@ for %@%@"
+ "[DEBUG] Learning salt state %@ from %@ for %@%@"
+ "[DEBUG] Looking for old Ciconia domains%@"
+ "[DEBUG] Moving salting root record ID %@ from %@ to %@%@"
+ "[DEBUG] Opening db at: %@%@"
+ "[DEBUG] Postponing sync up for item %@%@"
+ "[DEBUG] Removing FP domain on disk: %@%@"
+ "[DEBUG] Removing work directory%@"
+ "[DEBUG] Retry removing work directory%@"
+ "[DEBUG] Running in sync bubble. Ignoring app list did change event%@"
+ "[DEBUG] Salting batch operation is not allowed on %@%@"
+ "[DEBUG] Scheduling sync down for zone %@%@"
+ "[DEBUG] Screen no longer locked. Try upload item: %@%@"
+ "[DEBUG] Start date expired: %@ (%f)%@"
+ "[DEBUG] Sync: Dedicating sync op to metadata salting %@%@"
+ "[DEBUG] Target application seems missing%@"
+ "[DEBUG] Thumbnail manager: below maximum allowed number of thumbnails retrieval (%ld)%@"
+ "[DEBUG] Thumbnail manager: reached maximum allowed number of thumbnails retrieval (%ld)%@"
+ "[DEBUG] Uploader: scheduling %lld upload jobs that where in permenant failure state%@"
+ "[DEBUG] We shouldn't re-upload in case of structure records failures%@"
+ "[DEBUG] Will remove domain: %@%@"
+ "[DEBUG] _garbageCollectUploadThumbnailsIncludingActiveUploads: [%s]%@"
+ "[DEBUG] basename is nil -> replace with empty string%@"
+ "[DEBUG] itemID %@ does not exits yet in the server%@"
+ "[DEBUG] overwriting serverUpdate to YES because the item is moving to IDLE%@"
+ "[DEBUG] sending batch from %llu to %llu\n updatedItems = %@\n deletedItems = %@%@"
+ "[DEBUG] shared iPad: Completed upload for all items for %@%@"
+ "[DEBUG] shared iPad: Not considering %@ for sync bubble tasks because sync is blocked%@"
+ "[DEBUG] shared iPad: Still need to sync up %@ more items for sync bubble for %@%@"
+ "[DEBUG] ┏%llx Failed to get participantDocumentToken for item: %@ with error %@%@"
+ "[DEBUG] ┏%llx Saving item %@, serverUpdate = %d%@"
+ "[DEBUG] ┏%llx Screen is unlocked - re-uploading failed items for data protection class%@"
+ "[DEBUG] ┏%llx received a push in the %@ database for topic:'%@' payload:%@ token:%@ priority:%ld%@"
+ "[ERROR] Auto rollback handler called - %@ (%@)%@"
+ "[ERROR] Can't generate salting key %{errno}d%@"
+ "[ERROR] Error: %lld%@"
+ "[ERROR] Failed creating root folder for DB: %@. %@%@"
+ "[ERROR] Failed removing domain %{errno}d%@"
+ "[ERROR] Got error reading the account DSID from '%@': %@%@"
+ "[ERROR] Operation %@ is missing syncContext%@"
+ "[ERROR] Zone %@ has items which need sync. Clearing app sync blocked%@"
+ "[ERROR] _registerStaticDBFunctions failed with %@%@"
+ "[ERROR] cancelling operation since reached to maximal allowed backoff%@"
+ "[ERROR] db corruption handler called: %@%@"
+ "[ERROR] failed opening connection: %@%@"
+ "[ERROR] failed sending salted records - %@%@"
+ "[ERROR] passed nil app bundle ID%@"
+ "[ERROR] sqlite error handler called - %@ (%@)%@"
+ "[NOTICE] %@ - shared iPad: needs to sync items in the sync bubble (sz:%llu)%@"
+ "[NOTICE] Got %@ while opening account. Exiting without an error%@"
+ "[NOTIF] document %@ didCompleteDownloadEtagIfLoser %@ withError %@ -- notifying trackers%@"
+ "[WARNING] %@ - We already have a bubble sync task %@%@"
+ "[WARNING] %d: enumerating domains failed: %@%@"
+ "[WARNING] %d: removeDomain:%@ failed: %@%@"
+ "[WARNING] %d: removeDomain:%@ timed out%@"
+ "[WARNING] Adding advanced data protection bit because it's forced on %@%@"
+ "[WARNING] Failed to remove old domain %@: %@%@"
+ "[WARNING] Stripping advanced data protection bit because it's not supported on %@%@"
+ "[WARNING] bird is going to sleep for %lds%@"
+ "[WARNING] shared iPad: calling the upload handler because sync is failing: %@%@"
+ "_addThumbnailOperation:thumbnailID:"
+ "_appLibrariesEnumerator:version:"
+ "_baseHashSaltValidation"
+ "_basehashSaltInfo"
+ "_basehashSaltValidation"
+ "_br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:"
+ "_buildRecordsWithCompletion:"
+ "_cancelJobs:state:uploadError:"
+ "_checkIfShouldDedicateOpToSaltingBasehashItem:"
+ "_checkIfShouldWaitUntilDownloadCompletion_step"
+ "_childBaseSalt"
+ "_childBasehashSalt"
+ "_class"
+ "_cleanupOldCiconiaDomains:"
+ "_closeDB"
+ "_configuration"
+ "_createCKOperationForRecords:completion:"
+ "_createSchemaForSQLType:error:"
+ "_createSideFaultOnDisk_step"
+ "_createStructureRecordForRootItem"
+ "_createStructureRecordForServerItem:salt:"
+ "_createStructureRecordWithRecordID:itemID:basehashSalt:statInfo:"
+ "_databaseRootDirectory"
+ "_dbBecameCorrupted"
+ "_dbRootFolder"
+ "_dbgSleepIfRequested"
+ "_endAcceptationFlow_step"
+ "_extensionID"
+ "_finishShareAccept_step"
+ "_fixupAdvancedDataProtectionState"
+ "_fsRemoveWorkDirectory:"
+ "_garbageCollectUploadThumbnailsIncludingActiveUploads:"
+ "_generateSaltGetterBlock"
+ "_generateThumbnailOperationAtURL:targetURL:"
+ "_getChildBasehashSaltForItem:"
+ "_getLaunchServicesDatabaseGeneration"
+ "_getSaltForItem:"
+ "_getWorkloop"
+ "_hasActiveUploadWithStageID:"
+ "_hasThumbnailAvailableSlot"
+ "_initScreenLockManager"
+ "_invalidateCahceIfNeeded"
+ "_invalidateScreenLockManager"
+ "_isAccountRestricted_step"
+ "_isAppInstalled_step"
+ "_isFolderSharingSupported_step"
+ "_isIsSycBubble"
+ "_isScreenLocked"
+ "_isSharedIPad:"
+ "_isSyncBubbleClientEntitled"
+ "_isTesting"
+ "_isUserSignedInToiCloudDrive_step"
+ "_itemNeedingBasehashSalting"
+ "_lastUTIDatabaseGeneration"
+ "_locateRecordsOperationThrottle"
+ "_locateSharedItemOnDisk_step"
+ "_locateSharedItemOnOwner_step"
+ "_locateSharedItemOnRecipient_step"
+ "_maxBackoff"
+ "_metadataCompletionBlock"
+ "_migrationUUID"
+ "_openSharedItemIfStillNeeded_step"
+ "_openSharedSideFaultFile_step"
+ "_openiWorkAppPreemptively_step"
+ "_parentItemIDToChildBasehashSalt"
+ "_parseShareMetadata_step"
+ "_performMetadataSaltingOperationIfNecessaryWithCompletion:"
+ "_performModifyRecordsOrBatchOperationWithCompletion:"
+ "_populateUUID:"
+ "_prepareToDownloadSharedDocument_step"
+ "_processSaltingOnAppLibrary:"
+ "_reachedThumbnailMaximumCapacity"
+ "_recoverItemIDChangedWhileUploadingIfNecessary:"
+ "_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:"
+ "_registerOperation:throttler:"
+ "_registerStaticDBFunctionsWithError:"
+ "_removeDiagnosticsDirectoryAtURL:withError:"
+ "_removeFPDomain:error:"
+ "_removeThumbnailOperationForThumbnailID:"
+ "_removeWorkDirectory:"
+ "_reportBasehashSalting"
+ "_rescheduleJobsPendingScreenUnlock"
+ "_rootChildBasehashSalt"
+ "_rootRecordID"
+ "_rootSaltingState"
+ "_saltingState"
+ "_saveAppLibraryIfNecessary:"
+ "_saveItemID:version:record:contentBoundaryKey:iWorkSharingOptions:"
+ "_scheduleAfterFlush:"
+ "_screenLockObservers"
+ "_screenLocked"
+ "_sendDictionaryToCoreAnalytics:eventName:"
+ "_setSpotlightAttribute_step"
+ "_setXattrs:stageRegistry:"
+ "_setupExtensionID"
+ "_shouldIgnoreReportForOperationType:ofSubtype:forError:"
+ "_showSharingJoinDialog_step"
+ "_startShareAccept_step"
+ "_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:"
+ "_telemetrySchema"
+ "_throttledItemInBatch"
+ "_thumbnailGenerationManager"
+ "_thumbnailPrivateQueue"
+ "_timedOut"
+ "_timeout"
+ "_updateRootItemInClientDB"
+ "_updateRootItemInServerDB"
+ "_updateSaltingInfoInClientDBWithRecords:"
+ "_updateSaltingInfoInServerDBWithRecords:"
+ "_updateServerTruthForItemID:"
+ "_userActionsNavigator"
+ "_utiCache"
+ "_utiForExtension:"
+ "_validateAsset:advancedDataProtectionEnabled:"
+ "_verbose"
+ "_waitForSharedItemToBeOnDiskOnOwner_step"
+ "_waitForSharedItemToBeOnDiskOnRecipient_step"
+ "_waitForSharedItemToSyncDownOnOwner_step"
+ "_waitForSharedItemToSyncDownOnRecipient_step"
+ "_workQueue"
+ "addObject:error:"
+ "addScreenLockObserver:"
+ "addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:"
+ "advanced-data-protection"
+ "advanced-data-protection.basehash-salting.batch-size"
+ "advancedDataProtectionBasehashSaltingBatchSize"
+ "advancedDataProtectionEnabled"
+ "advancedDataProtectionForced"
+ "appLibraryRowIDFromRootOrDocumentsSQLiteValue:"
+ "app_library_rowid_from_root_or_documents"
+ "assetTransferOptions"
+ "backup-db"
+ "backupDatabaseWithURLWrapper:reply:"
+ "basehashSaltInfo"
+ "basehashSaltValidation"
+ "basehashSaltValidationKey"
+ "boundaryKey"
+ "boundaryKeyValidationKey"
+ "br_any_of:"
+ "br_assetWithDeviceID:fileID:generationID:boundaryKey:"
+ "br_assetWithFileURL:"
+ "br_assetWithFileURL:boundaryKey:"
+ "br_badFilenameAlternativeName"
+ "br_isCKErrorCode:underlyingErrorCode:"
+ "br_isInSyncBubble"
+ "br_shouldOverwriteExistingName"
+ "br_signalEnumeratorForContainerItemIdentifier:completionHandler:"
+ "brc_fillWithChildBasehashSalt:"
+ "brc_generateSaltingKey"
+ "brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors"
+ "brc_isCloudKitErrorDataProtectionClass"
+ "brc_isCloudKitRequestRejectedError"
+ "brc_isFrontBoardOpenApplicationRequestDenied"
+ "brc_truncatedSHA256"
+ "childBaseSaltForItemID:"
+ "childBasehashSalt"
+ "childBasehashSaltValidationKey"
+ "cleanupCiconiaAtURL:diagnosticsURL:completionHandler:"
+ "clearTempDatabases"
+ "closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:"
+ "com.apple.CloudDocs.debug.sleepOnStartDuration"
+ "com.apple.CloudDocs.debug.sleepOnStartInitialDate"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.bird.thumbnails.private"
+ "com.apple.iCloudDriveCore.telemetry-disk-checker"
+ "createSetOfClass:withSQLType:error:"
+ "createStringsSetWithError:"
+ "data-protection-class"
+ "dataWithLength:"
+ "dataWithSQL:"
+ "db.integrity-check.basehash-salting"
+ "dbIntegrityCheckBasehashSalting"
+ "debugItemIDStringWithVerbose:"
+ "defaultCache"
+ "defaultNavigator"
+ "deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:"
+ "directUnsaltedItemsInServerTruthEnumeratorParentedTo:"
+ "dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:"
+ "dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:"
+ "encryptedValues"
+ "enumerateObjectsWithSortOrder:usingBlock:"
+ "exactBirthtime"
+ "exactMtime"
+ "exactSize"
+ "files"
+ "fpfsUploadV2"
+ "fully salted"
+ "getConfiguration"
+ "getDomainsForProviderIdentifier:completionHandler:"
+ "getKnowledgeUUID:andSequenceNumber:"
+ "getOrGenerateChildBasehashSaltingKey"
+ "hasMigrationUUID"
+ "hasThumbnailAvailableSlot"
+ "initArrayOfClass:withSQLType:error:"
+ "initWithBasehashSaltInfo:"
+ "initWithBatchSize:"
+ "initWithItemID:clientZone:"
+ "initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:"
+ "initWithRecordID:serverZone:isUserWaiting:maxBackoff:"
+ "initWithRootItem:"
+ "initWithShareMetadata:client:session:userNotifier:userActionsNavigator:"
+ "integerForKey:"
+ "isAppLibraryRootItemIDWithSQLiteValue:"
+ "isInternalBuild"
+ "isSyncBubbleClientEntitled"
+ "itemNeedingBasehashSalting"
+ "item_id_is_app_library_root"
+ "lastBootHistoryTime"
+ "lazyXattrWithStageRegistry:"
+ "lengthOfBytesUsingEncoding:"
+ "locate-records-throttle"
+ "locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:"
+ "locateRecordsThrottleParams"
+ "maxBackoff"
+ "metadata-salting/"
+ "metadataCompletionBlock"
+ "newAppLibraryFromPQLResultSet:version:error:"
+ "newBasehashSaltingProblemCountWithProblemCount:mangledID:itemIDString:"
+ "newDanglingZombieProblemCountWithProblemCount:"
+ "newEnumeratorForItemID:clientZone:"
+ "newIntEvent:UUID:value:"
+ "newLongEvent:UUID:value:"
+ "newLongEvent:UUID:value:round:"
+ "no server item"
+ "openAppStoreForBundleID:"
+ "openShareURLInWebBrowser:withReason:"
+ "openiCloudSettings"
+ "operationForThumbnailID:"
+ "paddedFileSize"
+ "partially salted"
+ "pcs chaining"
+ "providerDomainWithID:cachePolicy:error:"
+ "reachedThumbnailMaximumCapacity"
+ "refresh-revision-max-backoff"
+ "refreshRevisionMaxBackoff"
+ "registerAndSendNewApplyFailureWithOutcome:"
+ "registerAndSendNewContainerResetWithOutcome:"
+ "registerAndSendNewFolderSharePCSChainingTime:chainedRecordsCount:zoneMangledID:itemIDString:error:analyticsReporter:"
+ "registerAndSendNewPeriodicSyncWithOutcome:"
+ "registerAndSendNewShareAcceptationWithLastStep:zoneMangledID:itemIDString:error:analyticsReporter:"
+ "removeDomain:forProviderIdentifier:completionHandler:"
+ "removeScreenLockObserver:"
+ "retriableCKInteralErrorCodesForRejectedRequestedError"
+ "rootChildBasehashSalt"
+ "rootRecordCreated"
+ "rounding amount"
+ "salting"
+ "saltingState"
+ "saltingStateForItemID:"
+ "screenLockChanged:"
+ "seralizeBirthtime:"
+ "serializeContentBoundaryKey:"
+ "serializeFilename:forCreation:basehashSalt:parentIDIsCloudDocsRoot:"
+ "serializeFilename:forCreation:setExtension:basehashSalt:parentIDIsCloudDocsRoot:"
+ "serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:"
+ "serializeSpecialIdentityForFilename:parentIDIsCloudDocsRoot:"
+ "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:"
+ "serializeVersion:diffs:deadInServerTruth:basehashSalt:"
+ "session/tmp"
+ "setAdvancedDataProtectionEnabled:forContainer:reply:"
+ "setAssetTransferOptions:"
+ "setBasehashSaltValidation:"
+ "setChildBasehashSalt:"
+ "setEvictsObjectsWithDiscardedContent:"
+ "setHasThumbnailAvailableSlot:"
+ "setItemNeedingBasehashSalting:"
+ "setMaxBackoff:"
+ "setMetadataCompletionBlock:"
+ "setMmcsEncryptionSupport:"
+ "setReachedThumbnailMaximumCapacity:"
+ "setSaltingState:"
+ "setState:forItem:uploadError:"
+ "setState:forUploadJobID:zone:uploadError:"
+ "setTelemetrySchema:"
+ "setThrottledItemInBatch:"
+ "setTimedOut:"
+ "setTimeout:"
+ "setUseMMCSEncryptionV2:"
+ "setVerbose:"
+ "sharedABCReporter"
+ "sharedAnalytics"
+ "sharedScreenLockMonitor"
+ "shouldUseAdvancedDataProtection"
+ "showJoinDialogForShareMetadata:ckContainer:reply:"
+ "specialDirectoryIdentity"
+ "stringByTrimmingCharactersInSet:"
+ "structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:saltGetter:childBasehashSalt:"
+ "structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:saltGetter:childBasehashSalt:"
+ "supportsAdvancedDataProtection"
+ "sync.advanced-data-protection.timestamp-rounding-amount"
+ "sync.advanced-data-protection.validation-key-length"
+ "sync.locate-records.throttle-params"
+ "sync.retriable-internal-error-codes-for-ck-rejected-requested-error"
+ "sync.treat-per-item-throttle-as-success"
+ "temporaryDirectory"
+ "text"
+ "throttledItemInBatch"
+ "thumbnail generation encountered an error"
+ "thumbnail-generation-operation-timeout"
+ "thumbnailGenerationManager"
+ "thumbnailGenerationOperationTimeout"
+ "timedOut"
+ "timeout"
+ "timestampRoundingAmount"
+ "transferOptionsWithBoundaryKey:"
+ "treatPerItemThrottleAsOperationSuccess"
+ "unsalted"
+ "upload_error = %@, "
+ "useMMCSEncryptionV2"
+ "v16@?0@\"BRCContainerScheduler\"8"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8B16B20@?24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v40@0:8@\"CKShareMetadata\"16@\"CKContainer\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16B24@28B36"
+ "v44@0:8@16@24B32^B36"
+ "v44@0:8@16B24B28@32B40"
+ "v44@0:8@16Q24B32@36"
+ "v44@0:8i16@20@28@36"
+ "v48@0:8@16B24B28B32@36B44"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32B40B44@?48"
+ "v64@0:8@16Q24@32B40C44@48@56"
+ "v64@0:8d16@24@32@40@48@56"
+ "validateAdvancedDataProtectionFieldsWithSession:error:"
+ "validationKeyTruncationLength"
+ "validation_key"
+ "verbose"
+ "whitespaceAndNewlineCharacterSet"
- "\x01\x12\x12\x11\x1a"
- "\x01\x19\x12\x12"
- "\x01'\x18\x11#"
- "\x03\x19\x11\x17"
- "\x06\x11"
- "\b\x11\"\x11\x1c\x12\x14\x1f\x01\x12\""
- "\t\x158\xf0/5\x11\x14\x1f\n"
- "   o %@ [container]"
- "  [%@] OS:%@ CloudDocs:%@ BirdSchema:%@ DBSchema:%@ CiconiaVersion:%@ Duration:%@ UUID:%@ LastOriginatorID:%@ LastError:%@"
- "%*s%@"
- "%llu"
- "+[BRCAccountSession(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]"
- "+[BRCAccountSession(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5"
- "+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]"
- "+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke"
- "+[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:]"
- "+[BRCSharingAcceptFlowOperation _openAppStoreForShareURL:]"
- "+[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:]"
- ",last_originator"
- "-[BRCAccountSession _cancelCiconiaRepeatQueue]"
- "-[BRCAccountSession _refreshCiconiaState]"
- "-[BRCAccountSession _setupCiconiaRepeatQueue]"
- "-[BRCAccountSession _setupCiconiaRepeatQueue]_block_invoke"
- "-[BRCAccountSession _startCiconiaIfRelevant]"
- "-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke"
- "-[BRCAccountSession _startCiconiaIfRelevant]_block_invoke_2"
- "-[BRCAccountSession shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup]"
- "-[BRCAccountSession(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]_block_invoke"
- "-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]"
- "-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke"
- "-[BRCAnalyticsReporter _fetchTelemetryEventCountOrAdd:]"
- "-[BRCAnalyticsReporter _prepareSyncTelemetryEventsToSend]"
- "-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke"
- "-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]"
- "-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke"
- "-[BRCAnalyticsReporter postReportForDefaultSubCategoryWithCategory:telemetryTimeEvent:]"
- "-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke_2"
- "-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke"
- "-[BRCAnalyticsReporter updateCurrentTelemetryToken:]"
- "-[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:]"
- "-[BRCClientZone _registerServerStitchingOperation:]"
- "-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:]"
- "-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]"
- "-[BRCDatabaseBackupStorage setUpDatabaseWithError:]"
- "-[BRCFPFSMigrationScheduler _isCoconiaSuccessful]"
- "-[BRCFPFSMigrationScheduler _isCoconiaSuccessful]_block_invoke_2"
- "-[BRCFSUploader _cancelJobs:state:]"
- "-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke"
- "-[BRCFSUploader _doneFetchingThumbnailForJobID:]"
- "-[BRCFSUploader _startFetchThumbnail:jobID:]"
- "-[BRCFSUploader initWithAccountSession:]_block_invoke_3"
- "-[BRCFSUploader setState:forUploadJobID:zone:]"
- "-[BRCItemID debugItemIDString]"
- "-[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:]"
- "-[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:]"
- "-[BRCLocateRecordOperation initWithRecordID:serverZone:isUserWaiting:]"
- "-[BRCPendingChangesStream destroyDatabase]_block_invoke"
- "-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke"
- "-[BRCServerZone _saveItemID:version:record:iWorkSharingOptions:]"
- "-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _finishShareAccept]"
- "-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _finishShareAccept]_block_invoke_5"
- "-[BRCSharingAcceptFlowOperation _isAccountRestricted]"
- "-[BRCSharingAcceptFlowOperation _isAppInstalled]"
- "-[BRCSharingAcceptFlowOperation _isAppInstalled]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _isFolderSharingSupported]"
- "-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]"
- "-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk]"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded]"
- "-[BRCSharingAcceptFlowOperation _openSharedSideFaultFile]"
- "-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively]"
- "-[BRCSharingAcceptFlowOperation _parseShareMetadata]"
- "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]"
- "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _setSpotlightAttribute]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]"
- "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _startShareAccept]"
- "-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2"
- "-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_2"
- "-[BRCStageRegistry setStageDirectoryForXattr:]"
- "-[BRCStatInfo lazyXattrWithSession:]"
- "-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke"
- "-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke_2"
- "-[BRCUserDefaults _ciconiaOriginatorIDs:byDefault:]_block_invoke"
- "-[BRCVersion lazyXattrWithSession:]"
- "-[BRCXPCRegularIPCsClient _isCiconiaErrorTTRWorthy:]"
- "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:]"
- "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]"
- "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]"
- "-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke"
- "-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]"
- "-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]"
- "-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]"
- "-[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]"
- "-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]"
- "-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]"
- "-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(LegacyAdditions) launchItemCountMismatchChecksAtURL:reply:]"
- "-[BRCXPCRegularIPCsClient(LegacyAdditions) launchItemCountMismatchChecksAtURL:reply:]_block_invoke"
- "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:clientZone:error:]"
- "-[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:]"
- "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:]"
- "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:]"
- "-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]"
- "-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]"
- "2\x14\x15"
- "<"
- "="
- "@\"<BRCCiconiaStatusProvider>\""
- "@\"AppTelemetryCiconiaBouncesInvestigation\""
- "@\"AppTelemetryCiconiaEAccessInvestigation\""
- "@\"AppTelemetryCiconiaInvestigation\""
- "@\"NSMutableOrderedSet<NSFileProviderItem>\""
- "@16@?0@\"NSString\"8"
- "@28@0:8Q16i24"
- "@32@0:8B16C20@24"
- "@84@0:8@16@24@32@40@48@56B64B68B72@76"
- "AppTelemetryCiconiaBouncesInvestigation"
- "AppTelemetryCiconiaEAccessInvestigation"
- "AppTelemetryCiconiaInvestigation"
- "B48@0:8@16@24@32Q40"
- "B48@0:8^@16^@24@32^@40"
- "B52@0:8@16@24B32@36^@44"
- "BRCCiconiaStatusProvider"
- "BRCSendDictionaryToCoreAnalytics"
- "BounceBucket:%d"
- "CICONIA"
- "CICONIA_CLEANUP_FAILURE"
- "CICONIA_EACCESS_ERROR"
- "CICONIA_MIGRATION_FINISHED"
- "CICONIA_MISMATCHING_ITEM_DB_DISK"
- "CICONIA_OVER_BOUNCE"
- "CICONIA_QUEUEING_FAILED"
- "CICONIA_STARTED_MIGRATION"
- "CICONIA_STATUS_REPORT"
- "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, error_message, service))"
- "Ciconia"
- "Ciconia Migration Failed (%@: %ld)"
- "CiconiaProtocol"
- "CiconiaQueue"
- "CleanupFailure"
- "DELETE FROM telemetry_events"
- "DELETE FROM telemetry_events ORDER BY priority ASC, rowid ASC LIMIT %u"
- "DELETE FROM telemetry_events WHERE %@"
- "FPFS_MIGRATION"
- "INSERT INTO ciconia_history (date, os, br, bird_schema, db_schema, ciconia_version, duration, uuid, last_error, last_originator) VALUES (%lu, %@, %@, %u, %@, %llu, %f, %@, %@, %llu)"
- "INSERT INTO telemetry_events (payload, priority) VALUES (%@, %d)"
- "J\"6\x11"
- "MigrationFailure"
- "No DSID"
- "OverBounce"
- "SELECT 1 FROM pragma_table_info('ciconia_history') WHERE name='last_originator'"
- "SELECT 1 FROM sqlite_master where type = 'table' AND name = 'ciconia_history'"
- "SELECT COUNT(*) FROM client_items"
- "SELECT COUNT(1) FROM ciconia_history WHERE ciconia_version = %llu AND last_originator = %llu"
- "SELECT COUNT(1) FROM client_state"
- "SELECT COUNT(1) FROM telemetry_events"
- "SELECT COUNT(uuid), COUNT(last_error) FROM ciconia_history %@"
- "SELECT MAX(ciconia_version) FROM ciconia_history WHERE last_error IS NULL"
- "SELECT csu.throttle_id, csu.last_try_stamp FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
- "SELECT date,os,br,bird_schema,db_schema,ciconia_version,last_error,duration,uuid %@ FROM ciconia_history ORDER BY date DESC LIMIT 10"
- "SELECT last_originator FROM ciconia_history WHERE ciconia_version == %lu AND last_originator != 0"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_state = 1    AND li.item_localsyncupstate = 4    AND NOT EXISTS(SELECT 1 FROM client_items AS ci                     WHERE li.item_id = ci.item_parent_id                      AND ci.zone_rowid = su.zone_rowid                      AND ci.item_state != -2)    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (1, 2, 8, 5, 6, 7, 3)    AND li.item_state = 0    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_doc_id, li.item_file_id, li.item_generation, li.item_localname, li.item_processing_stamp, li.item_staged_file_id, li.item_staged_generation, li.item_bouncedname, li.item_scope, li.item_tmpbounceno, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.desired_version, li.item_live_conflict_loser_etags, li.item_thumb_live_signature, li.item_thumb_greedy, li.version_block_sync_until_bundle_id, li.version_block_sync_until_timestamp FROM client_items AS li  INNER JOIN client_sync_up AS su  ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (0, 9, 10, 4)    AND (li.item_state = 0)    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT payload FROM telemetry_events"
- "SELECT rowid, payload FROM telemetry_events WHERE NOT %@ ORDER BY rowid ASC LIMIT %llu"
- "SELECT rowid, payload FROM telemetry_events WHERE priority = 1 ORDER BY rowid LIMIT %u"
- "T@\"AppTelemetryCiconiaBouncesInvestigation\",&,N"
- "T@\"AppTelemetryCiconiaEAccessInvestigation\",&,N"
- "T@\"AppTelemetryCiconiaInvestigation\",&,N"
- "T@\"NSDictionary\",R,N,V_thumbnailsOperations"
- "T@\"NSString\",&,N,V_crashReporterKey"
- "T@\"NSString\",&,N,V_underlyingErrorDescription"
- "T@\"NSString\",&,N,V_underlyingErrorDomain"
- "T@\"PQLConnection\",&,N,V_database"
- "TB,N,SsetCurrentlyDumpingForCiconia:,V_currentlyDumpingForCiconia"
- "TB,N,V_areMigratedFaultsBelowThreshold"
- "TB,N,V_areNonFaultAllMigrated"
- "TB,N,V_isDesktopEnabled"
- "TB,N,V_manuallyTriggeredMigration"
- "TB,R,N,V_isInSyncBubble"
- "TB,R,N,VciconiaGatedForFPFSMigration"
- "TB,R,N,VignorePercentsOnInternal"
- "TI,N,V_identifier"
- "TI,N,V_stFlags"
- "TQ,N,V_ciconiaVersion"
- "Td,N,V_cloningTime"
- "Tf,N,V_previousReleasesSuccessRate"
- "Ti,N,V_aliasToFileCount"
- "Ti,N,V_aliasToFolderCount"
- "Ti,N,V_aliasToPackageCount"
- "Ti,N,V_aliasToSymlinkCount"
- "Ti,N,V_ciconiaState"
- "Ti,N,V_curGid"
- "Ti,N,V_curUid"
- "Ti,N,V_fileToAliasCount"
- "Ti,N,V_fileToFolderCount"
- "Ti,N,V_fileToPackageCount"
- "Ti,N,V_fileToSymlinkCount"
- "Ti,N,V_folderToAliasCount"
- "Ti,N,V_folderToFileCount"
- "Ti,N,V_folderToPackageCount"
- "Ti,N,V_folderToSymlinkCount"
- "Ti,N,V_nonConflictingKindCount"
- "Ti,N,V_packageToAliasCount"
- "Ti,N,V_packageToFileCount"
- "Ti,N,V_packageToFolderCount"
- "Ti,N,V_packageToSymlinkCount"
- "Ti,N,V_protectionClass"
- "Ti,N,V_stGid"
- "Ti,N,V_stMode"
- "Ti,N,V_stUid"
- "Ti,N,V_symlinkToAliasCount"
- "Ti,N,V_symlinkToFileCount"
- "Ti,N,V_symlinkToFolderCount"
- "Ti,N,V_symlinkToPackageCount"
- "Tq,N,V_bouncedDocumentsFoldersCount"
- "Tq,N,V_ciconiaVersion"
- "Tq,N,V_datalessItemsCount"
- "Tq,N,V_diskSpaceLeft"
- "Tq,N,V_documentsFoldersWithoutItemIDCount"
- "Tq,N,V_expectedMigratedItemsCount"
- "Tq,N,V_ignoredContentProtectedItems"
- "Tq,N,V_itemsChangedDuringCloning"
- "Tq,N,V_materialisedOnCDItemsCount"
- "Tq,N,V_materialisedOnFPFSItemsCount"
- "Tq,N,V_packagesWithoutBundleBit"
- "Tq,N,V_previousAttempts"
- "Tq,N,V_previousFailedAttempts"
- "Tq,N,V_symlinkedDocumentsFolderCount"
- "Tq,N,V_underlyingErrorCode"
- "Tq,N,V_unexpectedCreations"
- "Tq,R,N,VmaxFailurePerVersion"
- "Tq,R,N,Vpercent100kAndAbove"
- "Tq,R,N,VpercentBelow100k"
- "Tq,R,N,VpercentBelow10k"
- "Tq,R,N,VpercentBelow1k"
- "UPDATE client_uploads    SET throttle_state = %d, transfer_operation = NULL  WHERE %@"
- "UPDATE client_uploads SET  throttle_state = %d, transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL WHERE throttle_id = %@"
- "WHERE ciconia_version %@ %llu"
- "X-APPLE-APP-TELEMETRY"
- "[CRIT] Assertion failed: !FPIsCloudDocsWithFPFSEnabled()%@"
- "[CRIT] Assertion failed: (NSUInteger)self->_session.clientDB.changes == _lastTelemetryBatchRowIDs.count%@"
- "[CRIT] Assertion failed: [originatorID intValue] > 0%@"
- "[CRIT] Assertion failed: _currentTelemetryToken.longLongValue == [persistedState telemetryToken]%@"
- "[CRIT] Assertion failed: _session.offline%@"
- "[CRIT] Assertion failed: _telemetryEventCount >= 0 _telemetryEventCount: %lld. Amount: %lld%@"
- "[CRIT] Assertion failed: priority <= 1%@"
- "[CRIT] Assertion failed: self->_telemetryEventCount == 0%@"
- "[CRIT] Assertion failed: self.session%@"
- "[CRIT] UNREACHABLE: Operation %@ is missing syncContext%@"
- "[CRIT] UNREACHABLE: client_state is empty! Not queuing migration%@"
- "[DEBUG] %@ - Ciconia originator IDs considered as success: %@%@"
- "[DEBUG] %@ - Ciconia originator IDs were %@%@"
- "[DEBUG] %@ - Ciconia state is: %d%@"
- "[DEBUG] %@ - We had Ciconia runs completing with an originator ID which is considered as a success. Returning YES%@"
- "[DEBUG] %@ - dealloc called%@"
- "[DEBUG] %@ needs to sync items in the sync bubble (sz:%llu)%@"
- "[DEBUG] Application proxy: %@%@"
- "[DEBUG] Can't delete shared top level item yet which is still syncing in another zone %@%@"
- "[DEBUG] Checking sync consistency%@"
- "[DEBUG] Ciconia %lu state: %d%@"
- "[DEBUG] Ciconia will try to relaunch every %llu s%@"
- "[DEBUG] Cleaning telemetry after updating BR version%@"
- "[DEBUG] Closing database%@"
- "[DEBUG] Completed upload for all items for %@%@"
- "[DEBUG] Copying account DSID from %@ to %@%@"
- "[DEBUG] Copying xattrs from %@ to %@%@"
- "[DEBUG] Creating a BRCSafeDBHolder %p for db in path: %@%@"
- "[DEBUG] Creating the Ciconia repeater%@"
- "[DEBUG] Database closed%@"
- "[DEBUG] Dedicating this sync up operation to pcs chaining %@%@"
- "[DEBUG] Deleting telemetry events: %@%@"
- "[DEBUG] Dequeued %lu telemetry events to send with token %lld (size %lu)%@"
- "[DEBUG] Download canceled for document %@ and etag:%@. Notifying download trackers%@"
- "[DEBUG] Dropping telemtry events due to queue overflow%@"
- "[DEBUG] Force Telemetry Deque passed the minimum interval%@"
- "[DEBUG] Inserting telemetry event %u%@"
- "[DEBUG] Looking whether we should run Ciconia...%@"
- "[DEBUG] Not considering %@ for sync bubble tasks because sync is blocked%@"
- "[DEBUG] Offline work, skipping notification%@"
- "[DEBUG] Queueing silent migration for release %lu and persona %@%@"
- "[DEBUG] Sending telemetry events in operation %@%@"
- "[DEBUG] Setting the dump flag on stage registry%@"
- "[DEBUG] Still need to sync up %@ more items for sync bubble for %@%@"
- "[DEBUG] The server has detected a problem on the client. Resetting all sync telemetry%@"
- "[DEBUG] There are more telemetry events to dequeue%@"
- "[DEBUG] Uploader: below maximum allowed number of thumbnails retrieval (%ld)%@"
- "[DEBUG] Uploader: reached maximum allowed number of thumbnails retrieval (%ld)%@"
- "[DEBUG] Uploader[%@]: generating thumbnail (shouldTransferThumbnail:yes) %@%@"
- "[DEBUG] iCloud Analytics collection has been disabled, not sending PoC telemetry%@"
- "[DEBUG] sending batch from %llu to %llu (%@,%@)%@"
- "[DEBUG] updating telemetry token %@ -> %lld%@"
- "[DEBUG] ┏%llx Failed to get participantDocumentToken --> use participantKey as before. item: %@%@"
- "[DEBUG] ┏%llx Fetch participantDocumentToken disabled --> use participantKey as before. item: %@%@"
- "[DEBUG] ┏%llx Saving item %@%@"
- "[DEBUG] ┏%llx cancelling sync consistency report with mount path %@%@"
- "[DEBUG] ┏%llx received a push in the %@ database for topic:'%@' payload:%@ token:%@%@"
- "[ERROR] Ciconia DB was dropped - domain removal will happen on next start%@"
- "[ERROR] Failed adopting persona for Ciconia, skipping: %@%@"
- "[ERROR] Failed creating Ciconia proxy: %@%@"
- "[ERROR] Failed queueing silent migration cleanup: %@%@"
- "[ERROR] Failed queueing silent migration: %@%@"
- "[ERROR] Failed to continue the xpc activity%@"
- "[ERROR] Failed to saved migration attempt %@: %@%@"
- "[ERROR] nil app bundle ID for share URL: %@%@"
- "[INFO] Cancelling Ciconia repeater%@"
- "[INFO] Repeating Ciconia automatically%@"
- "[NOTICE] Accounts list changed, revisiting migration schedule%@"
- "[NOTICE] Ciconia was successful on all accounts. We are good to go with FPFS migration (pending Trial allocation)%@"
- "[NOTICE] Current Ciconia failure is TTR worthy? %d (%ld)%@"
- "[NOTICE] Forcing telemetry events dequeue%@"
- "[NOTICE] No persona available, skipping Ciconia%@"
- "[NOTICE] Not running Ciconia because the device is shutting down%@"
- "[NOTICE] Not running Ciconia yet because buddy needs to run%@"
- "[NOTICE] Not running Ciconia yet because device is still locked%@"
- "[NOTICE] Skipping Ciconia because user default set%@"
- "[NOTICE] Telemetry dequeue already queued%@"
- "[NOTICE] Will send the report %@%@"
- "[NOTICE] Won't queue Ciconia run, there's a previous one to finish%@"
- "[NOTIF] document %@ didCompleteDownloadEtagIfLoser %@ withError %@ - Found trackers: %s%@"
- "[WARNING] Ciconia was not successful for all accounts. Defering checking if we need to migrate to FPFS%@"
- "[WARNING] Copying account DSID from %@ to %@%@"
- "[WARNING] Not submitting event which is disabled %u%@"
- "[WARNING] Skipping xattr check because we're in the middle of a dump%@"
- "[WARNING] We already have a bubble sync task %@%@"
- "[WARNING] calling the upload handler because sync is failing: %@%@"
- "_aliasToFileCount"
- "_aliasToFolderCount"
- "_aliasToPackageCount"
- "_aliasToSymlinkCount"
- "_areMigratedFaultsBelowThreshold"
- "_areNonFaultAllMigrated"
- "_bouncedDocumentsFoldersCount"
- "_bouncesInvestigation"
- "_cancelCiconiaRepeatQueue"
- "_checkIfShouldWaitUntilDownloadCompletion"
- "_ciconiaInvestigation"
- "_ciconiaOriginatorIDs:byDefault:"
- "_ciconiaRepeatQueue"
- "_ciconiaRepeatSource"
- "_ciconiaState"
- "_ciconiaStatusProvider"
- "_ciconiaVersion"
- "_cloningTime"
- "_crashReporterKey"
- "_createSideFaultOnDisk"
- "_curGid"
- "_curUid"
- "_currentTelemetryToken"
- "_currentlyDumpingForCiconia"
- "_datalessItemsCount"
- "_diskSpaceLeft"
- "_documentsFoldersWithoutItemIDCount"
- "_doneFetchingThumbnailForJobID:"
- "_eaccessInvestigation"
- "_endAcceptationFlow"
- "_expectedMigratedItemsCount"
- "_fetchTelemetryEventCountOrAdd:"
- "_fileToAliasCount"
- "_fileToFolderCount"
- "_fileToPackageCount"
- "_fileToSymlinkCount"
- "_finishShareAccept"
- "_folderToAliasCount"
- "_folderToFileCount"
- "_folderToPackageCount"
- "_folderToSymlinkCount"
- "_forceTelemetryDequeueQueued"
- "_garbageCollectUploadThumbnails"
- "_getPriorityOfEvent:"
- "_identifier"
- "_ignoredContentProtectedItems"
- "_investigationKeysToRemove"
- "_isAccountRestricted"
- "_isAppInstalled"
- "_isCiconiaErrorTTRWorthy:"
- "_isCoconiaSuccessful"
- "_isDesktopEnabled"
- "_isExpectedCiconiaError:"
- "_isExpectedCiconiaError:originatorId:"
- "_isFolderSharingSupported"
- "_isUserSignedInToiCloudDrive"
- "_itemsChangedDuringCloning"
- "_lastSentTelemetryEvents"
- "_lastTelemetryBatchRowIDs"
- "_locateSharedItemOnDisk"
- "_locateSharedItemOnOwner"
- "_locateSharedItemOnRecipient"
- "_manuallyTriggeredMigration"
- "_materialisedOnCDItemsCount"
- "_materialisedOnFPFSItemsCount"
- "_nonConflictingKindCount"
- "_oldToNewKeys"
- "_openAppStoreForShareURL:"
- "_openShareURLInWebBrowser:withReason:"
- "_openSharedItemIfStillNeeded"
- "_openSharedSideFaultFile"
- "_openiCloudSettings"
- "_openiWorkAppPreemptively"
- "_packageToAliasCount"
- "_packageToFileCount"
- "_packageToFolderCount"
- "_packageToSymlinkCount"
- "_packagesWithoutBundleBit"
- "_parseShareMetadata"
- "_performModifyRecordsOrPCSChainOperationWithCompletion:"
- "_prepareSyncTelemetryEventsToSend"
- "_prepareToDownloadSharedDocument"
- "_previousAttempts"
- "_previousFailedAttempts"
- "_previousReleasesSuccessRate"
- "_protectionClass"
- "_refreshCiconiaState"
- "_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:"
- "_reportEAccessDuringSilentMigration:uuid:"
- "_reportFailedQueueingMigration:"
- "_reportOverBounceDuringSilentMigration:total:uuid:"
- "_saveItemID:version:record:iWorkSharingOptions:"
- "_setSpotlightAttribute"
- "_setTelemetryHeaderOnCKOpIfNecessary:"
- "_setXattrs:session:"
- "_setupCiconiaRepeatQueue"
- "_shouldFetchParticipantDocumentToken"
- "_showSharingJoinDialog"
- "_stGid"
- "_stUid"
- "_startCiconiaIfRelevant"
- "_startFetchThumbnail:jobID:"
- "_startShareAccept"
- "_symlinkToAliasCount"
- "_symlinkToFileCount"
- "_symlinkToFolderCount"
- "_symlinkToPackageCount"
- "_symlinkedDocumentsFolderCount"
- "_syncTelemetryState"
- "_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:"
- "_thumbnailOperationForItemRowID:"
- "_underlyingErrorCode"
- "_underlyingErrorDescription"
- "_underlyingErrorDomain"
- "_unexpectedCreations"
- "_updateCiconiaState:uuid:"
- "_waitForSharedItemToBeOnDiskOnOwner"
- "_waitForSharedItemToBeOnDiskOnRecipient"
- "_waitForSharedItemToSyncDownOnOwner"
- "_waitForSharedItemToSyncDownOnRecipient"
- "aliasToFileCount"
- "aliasToFolderCount"
- "aliasToPackageCount"
- "aliasToSymlinkCount"
- "areMigratedFaultsBelowThreshold"
- "areNonFaultAllMigrated"
- "backupDatabaseWithURLWrapper:forCiconia:reply:"
- "bouncedDocumentsFoldersCount"
- "bouncesInvestigation"
- "can't initialize document with invalid library rowid %@"
- "can't initialize shared zone root with invalid zone rowid %@"
- "ciconia state: %d"
- "ciconia version: %lu"
- "ciconia-repeat-queue"
- "ciconia.disable-automated-start"
- "ciconia.hide-migration-domain"
- "ciconia.import-timeout"
- "ciconia.keep-migration-domain"
- "ciconia.mark-success-as-fail-for-content-protected-items"
- "ciconia.max-migration-failure"
- "ciconia.max-reconciliation-failures"
- "ciconia.max-side-faults-migration"
- "ciconia.originatorids-treat-as-success"
- "ciconia.originatorids-ttr-worthy"
- "ciconia.repeat-interval"
- "ciconia.skip-trial"
- "ciconia.sleep-time-at-invalidate"
- "ciconiaDisableAutomatedStart"
- "ciconiaGatedForFPFSMigration"
- "ciconiaHideMigrationDomain"
- "ciconiaImportTimeout"
- "ciconiaInvestigation"
- "ciconiaInvestigation,bouncesInvestigation,eaccessInvestigation"
- "ciconiaKeepDomainAfterMigration"
- "ciconiaMarkSuccessAsFailOnContentProtectedItems"
- "ciconiaMaxFailurePerVersion"
- "ciconiaMaxReconciliationFailures"
- "ciconiaMaxSideFaultsMigration"
- "ciconiaOriginatorIDsTTRWorthy"
- "ciconiaOriginatorIDsToTreatAsSuccess"
- "ciconiaRepeatInterval"
- "ciconiaSkipTrial"
- "ciconiaSleepTimeAtInvalidate"
- "ciconiaState"
- "ciconia_history"
- "cleanupCiconiaForPersonaID:atURL:diagnosticsURL:withReply:"
- "cloningTime"
- "cloudEnabledStatusForSession:"
- "com.apple.CloudDocsDaemon.ciconia"
- "com.apple.CloudDocsDaemon.telemetry-disk-checker"
- "copyItemAtPath:toPath:error:"
- "createSQLConditionForRowIDs:"
- "curGid"
- "curUid"
- "cur_gid"
- "cur_uid"
- "currentTelemetryToken"
- "currentlyDumpingForCiconia"
- "datalessItemsCount"
- "deserializeVersion:fakeStatInfo:clientZone:error:"
- "disk-space-reclaimer.thumbanil-upload-age-time"
- "diskSpaceLeft"
- "documentsFoldersWithoutItemIDCount"
- "dropAllSyncTelemetryEvents"
- "dumpDatabaseTo:containerID:personaID:includeAllItems:reply:"
- "dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:"
- "eaccessInvestigation"
- "expectedMigratedItemsCount"
- "fetchParticipantDocumentToken"
- "fileToAliasCount"
- "fileToFolderCount"
- "fileToPackageCount"
- "fileToSymlinkCount"
- "findTelemetryEvent:"
- "finishCleanupForPersonaID:withReply:"
- "folderToAliasCount"
- "folderToFileCount"
- "folderToPackageCount"
- "folderToSymlinkCount"
- "forceTelemetryDequeue"
- "forceTelemetryDequeueWithCompletionHandler:"
- "fpfs.migration.finished.telemetry.xpc"
- "fpfsMigrationFinishedTelemetryXPCActivity"
- "getMigrationAttemptOriginatorIDsForVersion:withDB:"
- "getPreviousMigrationAttempts:failed:beforeVersion:"
- "getPreviousMigrationAttempts:failed:forVersion:"
- "getPreviousMigrationAttempts:failed:withVersion:comperator:"
- "hasAliasToFileCount"
- "hasAliasToFolderCount"
- "hasAliasToPackageCount"
- "hasAliasToSymlinkCount"
- "hasAreMigratedFaultsBelowThreshold"
- "hasAreNonFaultAllMigrated"
- "hasBouncedDocumentsFoldersCount"
- "hasBouncesInvestigation"
- "hasCiconiaInvestigation"
- "hasCiconiaVersion"
- "hasCloningTime"
- "hasCrashReporterKey"
- "hasCurGid"
- "hasCurUid"
- "hasDatalessItemsCount"
- "hasDiskSpaceLeft"
- "hasDocumentsFoldersWithoutItemIDCount"
- "hasEaccessInvestigation"
- "hasExpectedMigratedItemsCount"
- "hasFileToAliasCount"
- "hasFileToFolderCount"
- "hasFileToPackageCount"
- "hasFileToSymlinkCount"
- "hasFolderToAliasCount"
- "hasFolderToFileCount"
- "hasFolderToPackageCount"
- "hasFolderToSymlinkCount"
- "hasIgnoredContentProtectedItems"
- "hasIsDesktopEnabled"
- "hasItemsChangedDuringCloning"
- "hasManuallyTriggeredMigration"
- "hasMaterialisedOnCDItemsCount"
- "hasMaterialisedOnFPFSItemsCount"
- "hasNonConflictingKindCount"
- "hasPackageToAliasCount"
- "hasPackageToFileCount"
- "hasPackageToFolderCount"
- "hasPackageToSymlinkCount"
- "hasPackagesWithoutBundleBit"
- "hasPreviousAttempts"
- "hasPreviousFailedAttempts"
- "hasPreviousReleasesSuccessRate"
- "hasProtectionClass"
- "hasStGid"
- "hasStUid"
- "hasSymlinkToAliasCount"
- "hasSymlinkToFileCount"
- "hasSymlinkToFolderCount"
- "hasSymlinkToPackageCount"
- "hasSymlinkedDocumentsFolderCount"
- "hasUnderlyingErrorCode"
- "hasUnderlyingErrorDescription"
- "hasUnderlyingErrorDomain"
- "hasUnexpectedCreations"
- "ignorePercentsOnInternal"
- "initForTestingDevice:"
- "initWithCiconiaStatusProvider:"
- "initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:"
- "initWithRecordID:serverZone:isUserWaiting:"
- "initWithShareMetadata:client:session:"
- "initiateSilentMigrationOf:forPersonaID:withParameters:andReply:"
- "iwork-collaboration.fetch-participant-document-token"
- "lastCiconiaVersion:"
- "lastForceTelemetrySyncDate"
- "launchItemCountMismatchChecksAtURL:reply:"
- "lazyXattrWithSession:"
- "libfssync.FileTreeError<libfssync.VFSItem>"
- "manuallyTriggeredMigration"
- "materialisedOnCDItemsCount"
- "materialisedOnFPFSItemsCount"
- "maxFailurePerVersion"
- "migration encountered a fatal error"
- "newAppLibraryFromPQLResultSet:error:"
- "newCiconiaReportEvent:state:"
- "newIntEvent:eventGroupUUID:value:"
- "newLongEvent:eventGroupUUID:value:"
- "newLongEvent:eventGroupUUID:value:round:"
- "nonConflictingKindCount"
- "notifyAccountsListChanged"
- "numberFromString:"
- "orderedSet"
- "packageToAliasCount"
- "packageToFileCount"
- "packageToFolderCount"
- "packageToSymlinkCount"
- "percent100kAndAbove"
- "percentBelow100k"
- "percentBelow10k"
- "percentBelow1k"
- "performWhenAccountsListChanges:"
- "previousAttempts"
- "previousFailedAttempts"
- "previousReleasesSuccessRate"
- "protectionClass"
- "providerDomainWithID:error:"
- "queryLastCiconiaVersion:"
- "queueSilentMigrationActivityForPersonaID:withReply:"
- "reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:"
- "reportDummyCiconiaMigration:reply:"
- "reportFinishedMigration:uuid:reply:"
- "reportItemMismatchDuringSilentMigration:information:uuid:reply:"
- "require-successful-ciconia-run-forFPFS-migration"
- "requireSuccessfulCiconiaRunForFPFSMigration"
- "responseHTTPHeaders"
- "rowid in (%@)"
- "saveMigrationAttemptForReport:uuid:"
- "serializeFilename:forCreation:"
- "serializeFilename:forCreation:setExtension:"
- "serializeFilename:forCreation:setExtension:inSharedAlias:"
- "serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:"
- "serializeVersion:diffs:deadInServerTruth:"
- "setAliasToFileCount:"
- "setAliasToFolderCount:"
- "setAliasToPackageCount:"
- "setAliasToSymlinkCount:"
- "setAreMigratedFaultsBelowThreshold:"
- "setAreNonFaultAllMigrated:"
- "setBouncedDocumentsFoldersCount:"
- "setBouncesInvestigation:"
- "setCiconiaInvestigation:"
- "setCiconiaState:"
- "setCloningTime:"
- "setCurGid:"
- "setCurUid:"
- "setCurrentlyDumpingForCiconia:"
- "setDatalessItemsCount:"
- "setDiskSpaceLeft:"
- "setDocumentsFoldersWithoutItemIDCount:"
- "setEaccessInvestigation:"
- "setExpectedMigratedItemsCount:"
- "setFileToAliasCount:"
- "setFileToFolderCount:"
- "setFileToPackageCount:"
- "setFileToSymlinkCount:"
- "setFolderToAliasCount:"
- "setFolderToFileCount:"
- "setFolderToPackageCount:"
- "setFolderToSymlinkCount:"
- "setHasAliasToFileCount:"
- "setHasAliasToFolderCount:"
- "setHasAliasToPackageCount:"
- "setHasAliasToSymlinkCount:"
- "setHasAreMigratedFaultsBelowThreshold:"
- "setHasAreNonFaultAllMigrated:"
- "setHasBouncedDocumentsFoldersCount:"
- "setHasCiconiaVersion:"
- "setHasCloningTime:"
- "setHasCurGid:"
- "setHasCurUid:"
- "setHasDatalessItemsCount:"
- "setHasDiskSpaceLeft:"
- "setHasDocumentsFoldersWithoutItemIDCount:"
- "setHasExpectedMigratedItemsCount:"
- "setHasFileToAliasCount:"
- "setHasFileToFolderCount:"
- "setHasFileToPackageCount:"
- "setHasFileToSymlinkCount:"
- "setHasFolderToAliasCount:"
- "setHasFolderToFileCount:"
- "setHasFolderToPackageCount:"
- "setHasFolderToSymlinkCount:"
- "setHasIgnoredContentProtectedItems:"
- "setHasIsDesktopEnabled:"
- "setHasItemsChangedDuringCloning:"
- "setHasManuallyTriggeredMigration:"
- "setHasMaterialisedOnCDItemsCount:"
- "setHasMaterialisedOnFPFSItemsCount:"
- "setHasNonConflictingKindCount:"
- "setHasPackageToAliasCount:"
- "setHasPackageToFileCount:"
- "setHasPackageToFolderCount:"
- "setHasPackageToSymlinkCount:"
- "setHasPackagesWithoutBundleBit:"
- "setHasPreviousAttempts:"
- "setHasPreviousFailedAttempts:"
- "setHasPreviousReleasesSuccessRate:"
- "setHasProtectionClass:"
- "setHasStGid:"
- "setHasStUid:"
- "setHasSymlinkToAliasCount:"
- "setHasSymlinkToFileCount:"
- "setHasSymlinkToFolderCount:"
- "setHasSymlinkToPackageCount:"
- "setHasSymlinkedDocumentsFolderCount:"
- "setHasUnderlyingErrorCode:"
- "setHasUnexpectedCreations:"
- "setIdentifier:"
- "setIsDesktopEnabled:"
- "setManuallyTriggeredMigration:"
- "setMaterialisedOnCDItemsCount:"
- "setMaterialisedOnFPFSItemsCount:"
- "setNonConflictingKindCount:"
- "setNumberStyle:"
- "setPackageToAliasCount:"
- "setPackageToFileCount:"
- "setPackageToFolderCount:"
- "setPackageToSymlinkCount:"
- "setPreviousAttempts:"
- "setPreviousFailedAttempts:"
- "setPreviousReleasesSuccessRate:"
- "setProtectionClass:"
- "setRequestCompletedBlock:"
- "setStGid:"
- "setStUid:"
- "setStageDirectoryForXattr:"
- "setSymlinkToAliasCount:"
- "setSymlinkToFileCount:"
- "setSymlinkToFolderCount:"
- "setSymlinkToPackageCount:"
- "setSymlinkedDocumentsFolderCount:"
- "setUnderlyingErrorCode:"
- "setUnderlyingErrorDescription:"
- "setUnderlyingErrorDomain:"
- "shouldIgnoreReportForOperationType:ofSubtype:forError:"
- "shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollup"
- "shouldLastCiconiaRunConsideredAsSuccessForFPFSMigrationRollupForAllAccounts"
- "shouldStartCiconiaBasedOnItemsCountWithAcountHash:"
- "showJoinDialogForShareMetadata:session:reply:"
- "signalStartOfSilentTelemetry:uuid:manual:version:reply:"
- "stGid"
- "stUid"
- "startedUpInSyncBubble"
- "structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:"
- "submitSyncTelemetryEvent:"
- "symlinkToAliasCount"
- "symlinkToFileCount"
- "symlinkToFolderCount"
- "symlinkToPackageCount"
- "symlinkedDocumentsFolderCount"
- "sync.consistency-checker.enabled"
- "syncConsistencyChecker"
- "syncTelemetryEventsToSend"
- "telemetry.rtc.disabled-investigation"
- "telemetry.rtc.payload-keys-converter"
- "telemetryRTCDisabledInvestigationKeys"
- "telemetryRTCPayloadKeysConverter"
- "thumbnailUploadAgeDelta"
- "thumbnailsOperationsByID"
- "underlyingErrorCode"
- "underlyingErrorDescription"
- "underlyingErrorDomain"
- "updateCurrentTelemetryToken:"
- "userNotificationClass"
- "v12@?0I8"
- "v16@?0@\"CKRequestInfo\"8"
- "v32@0:8@\"BRCMigrationReport\"16@?<v@?@\"NSError\">24"
- "v32@?0@?<v@?>8Q16^B24"
- "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
- "v36@0:8@16B24B28B32"
- "v40@0:8@\"BRCMigrationReport\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"CKShareMetadata\"16@\"BRCAccountSession\"24@?<v@?B@\"NSError\">32"
- "v40@0:8^Q16^Q24@32"
- "v48@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"BRCMigrationParameters\"32@?<v@?@\"BRCMigrationStats\"@\"NSError\">40"
- "v48@0:8@16@24B32B36^B40"
- "v48@0:8@16Q24@32B40C44"
- "v48@0:8^Q16^Q24@32@40"
- "v52@0:8@\"NSDate\"16@\"NSUUID\"24B32Q36@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24B32Q36@?44"
- "v56@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32Q40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32Q40@?48"
- "x-apple-app-telemetry-new-server-token"
- "{?=\"accountQuotaUsage\"b1\"bouncedDocumentsFoldersCount\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"ciconiaVersion\"b1\"cloningTime\"b1\"datalessItemsCount\"b1\"diskSpaceLeft\"b1\"documentsFoldersWithoutItemIDCount\"b1\"expectedMigratedItemsCount\"b1\"ignoredContentProtectedItems\"b1\"importTime\"b1\"itemsChangedDuringCloning\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"materialisedOnCDItemsCount\"b1\"materialisedOnFPFSItemsCount\"b1\"packagesWithoutBundleBit\"b1\"previousAttempts\"b1\"previousFailedAttempts\"b1\"symlinkedDocumentsFolderCount\"b1\"totalItemCount\"b1\"underlyingErrorCode\"b1\"unexpectedCreations\"b1\"previousReleasesSuccessRate\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"areMigratedFaultsBelowThreshold\"b1\"areNonFaultAllMigrated\"b1\"isAccountDataSeparated\"b1\"isDesktopEnabled\"b1\"manuallyTriggeredMigration\"b1}"
- "{?=\"aliasToFileCount\"b1\"aliasToFolderCount\"b1\"aliasToPackageCount\"b1\"aliasToSymlinkCount\"b1\"fileToAliasCount\"b1\"fileToFolderCount\"b1\"fileToPackageCount\"b1\"fileToSymlinkCount\"b1\"folderToAliasCount\"b1\"folderToFileCount\"b1\"folderToPackageCount\"b1\"folderToSymlinkCount\"b1\"nonConflictingKindCount\"b1\"packageToAliasCount\"b1\"packageToFileCount\"b1\"packageToFolderCount\"b1\"packageToSymlinkCount\"b1\"symlinkToAliasCount\"b1\"symlinkToFileCount\"b1\"symlinkToFolderCount\"b1\"symlinkToPackageCount\"b1}"
- "{?=\"curGid\"b1\"curUid\"b1\"protectionClass\"b1\"stFlags\"b1\"stGid\"b1\"stMode\"b1\"stUid\"b1\"hasAcls\"b1}"
- "\xf0\x92\x12\x12"

```
