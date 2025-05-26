## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2461.80.8.0.0
-  __TEXT.__text: 0x2bd174
-  __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x15da4
-  __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x71719
-  __TEXT.__oslogstring: 0x36f59
-  __TEXT.__gcc_except_tab: 0x13044
-  __TEXT.__ustring: 0x2be
-  __TEXT.__unwind_info: 0x8018
-  __TEXT.__objc_classname: 0x2075
-  __TEXT.__objc_methname: 0x3a031
-  __TEXT.__objc_methtype: 0x7114
-  __TEXT.__objc_stubs: 0x277c0
-  __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x7de8
-  __DATA_CONST.__objc_classlist: 0x830
+2720.100.117.0.0
+  __TEXT.__text: 0x2bfea4
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__objc_methlist: 0x158b4
+  __TEXT.__const: 0x358
+  __TEXT.__cstring: 0x73e63
+  __TEXT.__oslogstring: 0x37ec6
+  __TEXT.__gcc_except_tab: 0x134a8
+  __TEXT.__ustring: 0x36
+  __TEXT.__unwind_info: 0x82e8
+  __TEXT.__objc_classname: 0x21a9
+  __TEXT.__objc_methname: 0x39bf7
+  __TEXT.__objc_methtype: 0x6b14
+  __TEXT.__objc_stubs: 0x27ec0
+  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__const: 0x8120
+  __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x30e50
-  __DATA_CONST.__objc_selrefs: 0xc880
-  __DATA_CONST.__objc_arraydata: 0xe80
-  __AUTH_CONST.__cfstring: 0x1f980
-  __AUTH_CONST.__objc_const: 0x62f8
-  __AUTH_CONST.__const: 0x23b0
-  __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH_CONST.__objc_dictobj: 0x190
+  __DATA_CONST.__objc_const: 0x30a98
+  __DATA_CONST.__objc_selrefs: 0xc728
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xcc8
+  __DATA_CONST.__objc_superrefs: 0x7a0
+  __DATA_CONST.__objc_arraydata: 0xd98
+  __AUTH_CONST.__cfstring: 0x1f8a0
+  __AUTH_CONST.__objc_const: 0x6808
+  __AUTH_CONST.__const: 0x2528
+  __AUTH_CONST.__objc_intobj: 0xa08
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0xda0
-  __AUTH.__objc_data: 0x2760
+  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH.__objc_data: 0x2940
   __AUTH.__data: 0x18
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xc88
-  __DATA.__objc_superrefs: 0x778
-  __DATA.__objc_ivar: 0x1c5c
-  __DATA.__data: 0x1e08
-  __DATA.__bss: 0x230
-  __DATA_DIRTY.__objc_data: 0x2a80
+  __DATA.__objc_ivar: 0x1bec
+  __DATA.__data: 0x1ee0
+  __DATA.__bss: 0x270
+  __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x2e8
+  __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12932
-  Symbols:   38716
-  CStrings:  20798
+  Functions: 12904
+  Symbols:   38855
+  CStrings:  20831
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newBasehashSaltingProblemCountWithProblemCount:mangledID:itemIDString:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newDanglingZombieProblemCountWithProblemCount:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIntEvent:UUID:value:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:UUID:value:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:UUID:value:round:]
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _openConnection:serverTruth:databaseName:baseURL:initialVersion:lastCurrentVersion:error:].cold.8
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]
+ +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:].cold.1
+ +[BRCAutoBugCaptureReporter sharedABCReporter]
+ +[BRCDocumentSignatureCalculator _calculateSignatureForFileAtURL:error:]
+ +[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]
+ +[BRCDocumentSignatureCalculator calculateSignatureForURL:error:]
+ +[BRCEventsAnalytics sharedAnalytics]
+ +[BRCFlatLevelEnumerator newEnumeratorForItemID:clientZone:]
+ +[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:]
+ +[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:].cold.1
+ +[BRCItemID isAppLibraryRootItemIDWithSQLiteValue:]
+ +[BRCPackageItem(FPFSAdditions) newItemForSignatureCalculationWithURL:inPackage:error:]
+ +[BRCSQLBackedSet _databaseRootDirectory]
+ +[BRCSQLBackedSet clearTempDatabases]
+ +[BRCSQLBackedSet createSetOfClass:withSQLType:error:]
+ +[BRCSQLBackedSet createStringsSetWithError:]
+ +[BRCThumbnailGenerationManager defaultManager]
+ +[BRCUTITypeCache defaultCache]
+ +[BRCUploadSyncUpRequestsManager _fetchManagersDictionary]
+ +[BRCUploadSyncUpRequestsManager defaultManagerWithPersonaIdentifier:]
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
+ -[BRCAccountSessionFPFS _cloudDocsAppsListDidChange:].cold.2
+ -[BRCAccountSessionFPFS _createGroupContainerDownloadStage].cold.1
+ -[BRCAccountSessionFPFS _recoverAndReportDanglingLostZombieDirectories]
+ -[BRCAccountSessionFPFS _reportBasehashSalting]
+ -[BRCAccountSessionFPFS _reportBasehashSalting].cold.1
+ -[BRCAccountSessionFPFS _reportBasehashSalting].cold.2
+ -[BRCAccountSessionFPFS _reportBasehashSalting].cold.3
+ -[BRCAccountSessionFPFS waitForUploadsToCompleteInSyncBubbleWithReply:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) _appLibrariesEnumerator:version:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) lastBootHistoryTime]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:error:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) runDatabaseFixupsForDB:serverTruth:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) runDatabaseFixups]
+ -[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]
+ -[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:].cold.1
+ -[BRCAccountSessionFPFS(FPFSAdditions) _createRecoveryExecutedErrorForImportError:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _daysSinceLastMigrationProgress:itemsNotMigrated:reconciledItems:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _shouldTriggerTapToRadar:daysSinceLastMigrationProgress:]
+ -[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]
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
+ -[BRCClientZone(AdvancedDataProtection) contentBoundaryKeyForItemID:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.1
+ -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.2
+ -[BRCClientZone(BRCBaseHashSaltAdditions) directUnsaltedItemsInServerTruthEnumeratorParentedTo:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) saltingStateForItemID:]
+ -[BRCClientZone(BRCBaseHashSaltAdditions) saltingStateForItemID:].cold.1
+ -[BRCContainerScheduler _scheduleAfterFlush:]
+ -[BRCDaemonFPFS _dbgSleepIfRequested]
+ -[BRCDaemonFPFS _dbgSleepIfRequested].cold.1
+ -[BRCDeviceConfiguration .cxx_destruct]
+ -[BRCDeviceConfiguration _isFPFS]
+ -[BRCDeviceConfiguration _isIsSycBubble]
+ -[BRCDeviceConfiguration _isSharedIPad:]
+ -[BRCDeviceConfiguration _isTesting]
+ -[BRCDeviceConfiguration getConfiguration]
+ -[BRCDeviceConfiguration getDeviceConfigurationString]
+ -[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildrenForce:]
+ -[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildrenForce:].cold.1
+ -[BRCDirectoryItem(FPFSAdditions) forceSignalPropagationToChildren]
+ -[BRCDirectoryItem(FPFSAdditions) signalPropagationToChildren]
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
+ -[BRCFSImporter _deleteAppLibrary:documentsFolder:error:]
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.1
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.2
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.3
+ -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.4
+ -[BRCFSImporter _shouldRejectItemDeleteDueToEtags:baseVersion:error:]
+ -[BRCFSImporter deleteItem:recursively:baseVersion:error:]
+ -[BRCFSImporter importNewItemAtURL:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:]
+ -[BRCFSImporter importNewItemAtURL:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:].cold.1
+ -[BRCFSUploader _cancelJobs:state:uploadError:]
+ -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.7
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
+ -[BRCImportObject(BRCPackageAdditions) initWithPackageURL:error:]
+ -[BRCItemID debugItemIDStringWithVerbose:]
+ -[BRCItemID debugItemIDStringWithVerbose:].cold.1
+ -[BRCItemID debugItemIDStringWithVerbose:].cold.2
+ -[BRCLocalItem saveToDBForServerEdit:keepAliases:].cold.2
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
+ -[BRCPackageItem(FPFSAdditions) _initWithURL:inPackage:forItem:error:]
+ -[BRCPackageItem(FPFSAdditions) _initWithURL:inPackage:forItem:error:].cold.1
+ -[BRCPackageItem(FPFSAdditions) updateContentSignature:error:]
+ -[BRCQueryItemUtil contentPolicyForZoneRoot:optimizeStorage:isAppInstalled:isWallet:isGreedyDocument:]
+ -[BRCRecentsEnumeratorBatch initWithBatchSize:]
+ -[BRCRequestData .cxx_destruct]
+ -[BRCRequestData copyWithZone:]
+ -[BRCRequestData description]
+ -[BRCRequestData description].cold.1
+ -[BRCRequestData finishBlock]
+ -[BRCRequestData initWithProgress:requestType:finishBlock:]
+ -[BRCRequestData progress]
+ -[BRCRequestData requestType]
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
+ -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step].cold.1
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
+ -[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]
+ -[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step].cold.1
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
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step].cold.3
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step].cold.1
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step].cold.2
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step].cold.3
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step].cold.1
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step].cold.2
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]
+ -[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step].cold.1
+ -[BRCSharingAcceptFlowOperation initWithShareMetadata:client:session:userNotifier:userActionsNavigator:]
+ -[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]
+ -[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:].cold.1
+ -[BRCStageRegistry _hasActiveUploadWithStageID:]
+ -[BRCStageRegistry(FPFSAdditions) createStageURLForThumbnailFromItem:error:]
+ -[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]
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
+ -[BRCUploadSyncUpRequestsManager .cxx_destruct]
+ -[BRCUploadSyncUpRequestsManager _callFinishBlockOnDataRequest:finishError:]
+ -[BRCUploadSyncUpRequestsManager _initWithPersonaIdentifier:]
+ -[BRCUploadSyncUpRequestsManager _invalidateRequestsTableWithNewSource:]
+ -[BRCUploadSyncUpRequestsManager cancelRequestForIdentifier:error:]
+ -[BRCUploadSyncUpRequestsManager dumpToContext:]
+ -[BRCUploadSyncUpRequestsManager finishRequestForIdentifer:finishError:error:]
+ -[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:]
+ -[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:].cold.1
+ -[BRCUploadSyncUpRequestsManager getProgressForIdentifier:]
+ -[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:]
+ -[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:].cold.1
+ -[BRCUploadSyncUpRequestsManager registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:]
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
+ -[BRCUserDefaults dbIntegrityCheckLostZombieDirectories]
+ -[BRCUserDefaults fpfsStuckMigrationRecoveryDaysSinceImportStartedThreshold]
+ -[BRCUserDefaults fpfsStuckMigrationRecoveryDaysSinceUpgradeThreshold]
+ -[BRCUserDefaults fpfsStuckMigrationRecoveryDaysWithoutProgressThreshold]
+ -[BRCUserDefaults fpfsStuckMigrationTakeReconciledItemsIntoAccount]
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
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:].cold.1
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) getSaltingVerificationKeysAtItemIdentifier:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) removeFPFSDomain:].cold.5
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]
+ -[BRFieldContentSignature(BRCItemAdditions) _initWithVersionIdentifier:size:oldVersionIdentifier:contentSignature:]
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
+ -[NSFileProviderItemVersion(BRItemAdditions) br_prettyDescription]
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
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table160
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table182
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table210
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table231
+ GCC_except_table238
+ GCC_except_table267
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table284
+ GCC_except_table300
+ GCC_except_table303
+ GCC_except_table306
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table328
+ GCC_except_table331
+ GCC_except_table338
+ GCC_except_table355
+ GCC_except_table360
+ GCC_except_table366
+ GCC_except_table371
+ GCC_except_table374
+ GCC_except_table376
+ GCC_except_table381
+ GCC_except_table384
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table395
+ GCC_except_table402
+ GCC_except_table405
+ GCC_except_table410
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table421
+ GCC_except_table423
+ GCC_except_table429
+ GCC_except_table88
+ OBJC_IVAR_$_AppTelemetryInvestigation._migrationUUID
+ OBJC_IVAR_$_AppTelemetryTimeSeriesEvent._telemetrySchema
+ OBJC_IVAR_$_BRCAppLibrary._activeAliasQueries
+ OBJC_IVAR_$_BRCAppLibrary._activeQueries
+ OBJC_IVAR_$_BRCAppLibrary._activeRecursiveQueries
+ OBJC_IVAR_$_BRCAppLibrary._db
+ OBJC_IVAR_$_BRCAppLibrary._dbRowID
+ OBJC_IVAR_$_BRCAppLibrary._defaultClientZone
+ OBJC_IVAR_$_BRCAppLibrary._mangledID
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
+ _OBJC_CLASS_$_BRCDocumentSignatureCalculator
+ _OBJC_CLASS_$_BRCEventsAnalytics
+ _OBJC_CLASS_$_BRCFlatLevelEnumerator
+ _OBJC_CLASS_$_BRCMiniCiconia
+ _OBJC_CLASS_$_BRCRequestData
+ _OBJC_CLASS_$_BRCSQLBackedSet
+ _OBJC_CLASS_$_BRCSaltingBatchOperation
+ _OBJC_CLASS_$_BRCThumbnailGenerationManager
+ _OBJC_CLASS_$_BRCUTITypeCache
+ _OBJC_CLASS_$_BRCUploadSyncUpRequestsManager
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
+ _OBJC_IVAR_$_BRCRequestData._finishBlock
+ _OBJC_IVAR_$_BRCRequestData._progress
+ _OBJC_IVAR_$_BRCRequestData._requestType
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
+ _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._latestSourceIdentifier
+ _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._personaIdentifer
+ _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._requestsByItemGlobalID
+ _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._zoneIDToItemIDs
+ _OBJC_IVAR_$__BRCOperation._maxBackoff
+ _OBJC_IVAR_$__BRCOperation._timedOut
+ _OBJC_IVAR_$__BRCOperation._timeout
+ _OBJC_METACLASS_$_BRCBasehashSaltInfo
+ _OBJC_METACLASS_$_BRCDeviceConfiguration
+ _OBJC_METACLASS_$_BRCDocumentSignatureCalculator
+ _OBJC_METACLASS_$_BRCEventsAnalytics
+ _OBJC_METACLASS_$_BRCFlatLevelEnumerator
+ _OBJC_METACLASS_$_BRCMiniCiconia
+ _OBJC_METACLASS_$_BRCRequestData
+ _OBJC_METACLASS_$_BRCSQLBackedSet
+ _OBJC_METACLASS_$_BRCSaltingBatchOperation
+ _OBJC_METACLASS_$_BRCThumbnailGenerationManager
+ _OBJC_METACLASS_$_BRCUTITypeCache
+ _OBJC_METACLASS_$_BRCUploadSyncUpRequestsManager
+ _OBJC_METACLASS_$_BRCUserActionsNavigator
+ _SecRandomCopyBytes
+ __OBJC_$_CATEGORY_CKAsset_$_BRCAdvancedDataProtectionAdditions
+ __OBJC_$_CLASS_METHODS_BRCDocumentSignatureCalculator
+ __OBJC_$_CLASS_METHODS_BRCEventsAnalytics
+ __OBJC_$_CLASS_METHODS_BRCFlatLevelEnumerator
+ __OBJC_$_CLASS_METHODS_BRCSQLBackedSet
+ __OBJC_$_CLASS_METHODS_BRCThumbnailGenerationManager
+ __OBJC_$_CLASS_METHODS_BRCUTITypeCache
+ __OBJC_$_CLASS_METHODS_BRCUploadSyncUpRequestsManager
+ __OBJC_$_CLASS_METHODS_BRCUserActionsNavigator
+ __OBJC_$_CLASS_METHODS_CKAsset(BRCAdvancedDataProtectionAdditions)
+ __OBJC_$_CLASS_METHODS_NSData(BRCSignatureAdditions|BRCQuarantine|BRCCryptographicAdditions)
+ __OBJC_$_CLASS_PROP_LIST_BRCDaemonFPFS
+ __OBJC_$_INSTANCE_METHODS_BRCAutoBugCaptureReporter
+ __OBJC_$_INSTANCE_METHODS_BRCBasehashSaltInfo
+ __OBJC_$_INSTANCE_METHODS_BRCClientZone(BRCBaseHashSaltAdditions|BRCZoneReset|FPFSAdditions|AdvancedDataProtection)
+ __OBJC_$_INSTANCE_METHODS_BRCDeviceConfiguration
+ __OBJC_$_INSTANCE_METHODS_BRCEventsAnalytics
+ __OBJC_$_INSTANCE_METHODS_BRCFlatLevelEnumerator
+ __OBJC_$_INSTANCE_METHODS_BRCMiniCiconia
+ __OBJC_$_INSTANCE_METHODS_BRCRequestData
+ __OBJC_$_INSTANCE_METHODS_BRCSQLBackedSet
+ __OBJC_$_INSTANCE_METHODS_BRCSaltingBatchOperation
+ __OBJC_$_INSTANCE_METHODS_BRCThumbnailGenerationManager
+ __OBJC_$_INSTANCE_METHODS_BRCUTITypeCache
+ __OBJC_$_INSTANCE_METHODS_BRCUploadSyncUpRequestsManager
+ __OBJC_$_INSTANCE_METHODS_BRCUserActionsNavigator
+ __OBJC_$_INSTANCE_METHODS_NSData(BRCSignatureAdditions|BRCQuarantine|BRCCryptographicAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_BRCBasehashSaltInfo
+ __OBJC_$_INSTANCE_VARIABLES_BRCDeviceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BRCFlatLevelEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_BRCMiniCiconia
+ __OBJC_$_INSTANCE_VARIABLES_BRCRequestData
+ __OBJC_$_INSTANCE_VARIABLES_BRCSQLBackedSet
+ __OBJC_$_INSTANCE_VARIABLES_BRCSaltingBatchOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRCThumbnailGenerationManager
+ __OBJC_$_INSTANCE_VARIABLES_BRCUTITypeCache
+ __OBJC_$_INSTANCE_VARIABLES_BRCUploadSyncUpRequestsManager
+ __OBJC_$_PROP_LIST_BRCBasehashSaltInfo
+ __OBJC_$_PROP_LIST_BRCDeviceConfiguration
+ __OBJC_$_PROP_LIST_BRCRequestData
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
+ __OBJC_CLASS_PROTOCOLS_$_BRCRequestData
+ __OBJC_CLASS_PROTOCOLS_$_BRCSaltingBatchOperation
+ __OBJC_CLASS_PROTOCOLS_$_BRCUserActionsNavigator
+ __OBJC_CLASS_RO_$_BRCBasehashSaltInfo
+ __OBJC_CLASS_RO_$_BRCDeviceConfiguration
+ __OBJC_CLASS_RO_$_BRCDocumentSignatureCalculator
+ __OBJC_CLASS_RO_$_BRCEventsAnalytics
+ __OBJC_CLASS_RO_$_BRCFlatLevelEnumerator
+ __OBJC_CLASS_RO_$_BRCMiniCiconia
+ __OBJC_CLASS_RO_$_BRCRequestData
+ __OBJC_CLASS_RO_$_BRCSQLBackedSet
+ __OBJC_CLASS_RO_$_BRCSaltingBatchOperation
+ __OBJC_CLASS_RO_$_BRCThumbnailGenerationManager
+ __OBJC_CLASS_RO_$_BRCUTITypeCache
+ __OBJC_CLASS_RO_$_BRCUploadSyncUpRequestsManager
+ __OBJC_CLASS_RO_$_BRCUserActionsNavigator
+ __OBJC_LABEL_PROTOCOL_$_BRCScreenLockDelegate
+ __OBJC_LABEL_PROTOCOL_$_BRCUserNavigationActions
+ __OBJC_LABEL_PROTOCOL_$_BRScreenLockObserver
+ __OBJC_METACLASS_RO_$_BRCBasehashSaltInfo
+ __OBJC_METACLASS_RO_$_BRCDeviceConfiguration
+ __OBJC_METACLASS_RO_$_BRCDocumentSignatureCalculator
+ __OBJC_METACLASS_RO_$_BRCEventsAnalytics
+ __OBJC_METACLASS_RO_$_BRCFlatLevelEnumerator
+ __OBJC_METACLASS_RO_$_BRCMiniCiconia
+ __OBJC_METACLASS_RO_$_BRCRequestData
+ __OBJC_METACLASS_RO_$_BRCSQLBackedSet
+ __OBJC_METACLASS_RO_$_BRCSaltingBatchOperation
+ __OBJC_METACLASS_RO_$_BRCThumbnailGenerationManager
+ __OBJC_METACLASS_RO_$_BRCUTITypeCache
+ __OBJC_METACLASS_RO_$_BRCUploadSyncUpRequestsManager
+ __OBJC_METACLASS_RO_$_BRCUserActionsNavigator
+ __OBJC_PROTOCOL_$_BRCScreenLockDelegate
+ __OBJC_PROTOCOL_$_BRCUserNavigationActions
+ __OBJC_PROTOCOL_$_BRScreenLockObserver
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.419
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.419.cold.1
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.423
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke_10
+ ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke_11
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.97
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.80
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.80.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.82
+ ___107-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]_block_invoke
+ ___107-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]_block_invoke.105
+ ___107-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]_block_invoke.105.cold.1
+ ___107-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]_block_invoke.cold.1
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.103
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.103.cold.1
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.636
+ ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.106
+ ___111-[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:]_block_invoke.173
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.1
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.2
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.3
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke.cold.4
+ ___112-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke_2
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.229
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.229.cold.1
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.231
+ ___116-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke
+ ___116-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]_block_invoke
+ ___116-[BRCThumbnailGenerationManager addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:]_block_invoke.7
+ ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.379
+ ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.380
+ ___122-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:]_block_invoke
+ ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.83
+ ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.84
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.38
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.39
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.41
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.41.cold.1
+ ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.42
+ ___144-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]_block_invoke
+ ___144-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]_block_invoke.150
+ ___144-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]_block_invoke_2
+ ___144-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]_block_invoke_2.cold.1
+ ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.202
+ ___151-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke
+ ___151-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke_2
+ ___151-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke_2.cold.1
+ ___151-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke_2.cold.2
+ ___176-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke
+ ___176-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke.43
+ ___22-[BRCClientZone close]_block_invoke.65
+ ___22-[BRCDaemonFPFS start]_block_invoke.99
+ ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.135
+ ___25-[BRCFSUploader schedule]_block_invoke.125
+ ___26-[BRCStageRegistry resume]_block_invoke.154
+ ___26-[BRCStageRegistry resume]_block_invoke.162
+ ___26-[BRCStageRegistry resume]_block_invoke.163
+ ___26-[BRCStageRegistry resume]_block_invoke.163.cold.1
+ ___26-[BRCStageRegistry resume]_block_invoke.163.cold.2
+ ___26-[BRCStageRegistry resume]_block_invoke.163.cold.3
+ ___26-[BRCSyncUpOperation main]_block_invoke.66
+ ___27-[BRCClientZone _startSync]_block_invoke.188
+ ___27-[BRCClientZone _startSync]_block_invoke.188.cold.1
+ ___27-[BRCClientZone _startSync]_block_invoke.188.cold.2
+ ___27-[BRCDaemonFPFS selfCheck:]_block_invoke.153
+ ___27-[BRCSQLBackedSet _closeDB]_block_invoke
+ ___27-[BRCSQLBackedSet _closeDB]_block_invoke_2
+ ___29-[BRCAccountMigrator perform]_block_invoke.96
+ ___29-[BRCAccountMigrator perform]_block_invoke.96.cold.1
+ ___30-[BRCAccountSessionFPFS close]_block_invoke.265
+ ___31+[BRCUTITypeCache defaultCache]_block_invoke
+ ___32-[BRCPeriodicSyncOperation main]_block_invoke.16
+ ___32-[BRCPeriodicSyncOperation main]_block_invoke_2.20
+ ___32-[BRCSaltingBatchOperation main]_block_invoke
+ ___32-[BRCSaltingBatchOperation main]_block_invoke_2
+ ___32-[BRCSaltingBatchOperation main]_block_invoke_2.cold.1
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.184
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.184.cold.1
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.189
+ ___34-[BRCPendingChangesStream _openDB]_block_invoke.189.cold.1
+ ___34-[BRCSafeDBHolder closeWithError:]_block_invoke
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
+ ___36-[BRCSharingSaveShareOperation main]_block_invoke.149
+ ___37+[BRCEventsAnalytics sharedAnalytics]_block_invoke
+ ___37-[BRCAccountMigrationChecker perform]_block_invoke.111
+ ___37-[BRCAccountMigrationChecker perform]_block_invoke.111.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.234
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.236.cold.3
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.244
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.244.cold.1
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.215
+ ___39-[BRCSharingDestroyShareOperation main]_block_invoke.166
+ ___39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.95
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_4
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_5
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_6
+ ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_6.cold.1
+ ___40-[BRCMiniCiconia _removeFPDomain:error:]_block_invoke
+ ___40-[BRCPQLConnection setProfilingEnabled:]_block_invoke.106
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.289
+ ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.289.cold.1
+ ___41-[BRCSyncUpOperation performShareUpdate:]_block_invoke.51
+ ___43+[BRCUserActionsNavigator defaultNavigator]_block_invoke
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.162
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.162.cold.1
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.166
+ ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke_2.167
+ ___44-[BRCFSUploader recoverAndReportMissingJobs]_block_invoke.247
+ ___44-[BRCMiniCiconia _cleanupOldCiconiaDomains:]_block_invoke
+ ___44-[BRCThumbnailGenerationManager description]_block_invoke
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.232
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.233
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.236
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.249
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.237
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.237.cold.1
+ ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.241
+ ___45-[BRCContainerScheduler _scheduleAfterFlush:]_block_invoke
+ ___45-[BRCContainerScheduler _scheduleAfterFlush:]_block_invoke_2
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.329
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.329.cold.1
+ ___46+[BRCAutoBugCaptureReporter sharedABCReporter]_block_invoke
+ ___46-[BRCUserDefaults locateRecordsThrottleParams]_block_invoke
+ ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.437
+ ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.338
+ ___47+[BRCThumbnailGenerationManager defaultManager]_block_invoke
+ ___47-[BRCAccountSessionFPFS _reportBasehashSalting]_block_invoke
+ ___47-[BRCAccountSessionFPFS _reportBasehashSalting]_block_invoke.180
+ ___47-[BRCAccountSessionFPFS _reportBasehashSalting]_block_invoke.180.cold.1
+ ___47-[BRCAccountSessionFPFS _reportBasehashSalting]_block_invoke.cold.1
+ ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.296
+ ___47-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_3
+ ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke.105
+ ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke_2.112
+ ___48-[BRCStageRegistry _hasActiveUploadWithStageID:]_block_invoke
+ ___48-[BRCUploadSyncUpRequestsManager dumpToContext:]_block_invoke
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.2
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.3
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.4
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.297.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.300
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.312
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.312.cold.1
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.339
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.340
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.341
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.346
+ ___49-[BRCSQLBackedSet _createSchemaForSQLType:error:]_block_invoke
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.457
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.232
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.232.cold.1
+ ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke.97
+ ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke_2
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.222
+ ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.155
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.139
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.139.cold.1
+ ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke_2.145
+ ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.375
+ ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.376
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
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.487
+ ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.167
+ ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.169
+ ___54-[BRCDeviceConfiguration getDeviceConfigurationString]_block_invoke
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.13
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.15
+ ___54-[BRCSQLBackedSet initArrayOfClass:withSQLType:error:]_block_invoke.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.80.cold.2
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.403
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.404
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.430
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.431
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.158
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.158.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.159
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.166
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.166.cold.1
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.167
+ ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.168
+ ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.46
+ ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.48
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke.cold.1
+ ___55-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke.cold.2
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.665
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.666
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
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke.182
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke.cold.1
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_2
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_3
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_4
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_5
+ ___56-[BRCSharingAcceptFlowOperation _finishShareAccept_step]_block_invoke_5.cold.1
+ ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.287
+ ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.289
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88.cold.1
+ ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.88.cold.2
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.216
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.225
+ ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.228
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.472
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.472.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.472.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.473
+ ___57-[BRCFSImporter _deleteAppLibrary:documentsFolder:error:]_block_invoke
+ ___57-[BRCSharingAcceptFlowOperation _parseShareMetadata_step]_block_invoke
+ ___57-[BRCThumbnailGenerationManager operationForThumbnailID:]_block_invoke
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.347
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.348
+ ___58+[BRCUploadSyncUpRequestsManager _fetchManagersDictionary]_block_invoke
+ ___58-[BRCFSImporter deleteItem:recursively:baseVersion:error:]_block_invoke
+ ___58-[BRCFSImporter deleteItem:recursively:baseVersion:error:]_block_invoke.cold.1
+ ___58-[BRCFSUploader setState:forUploadJobID:zone:uploadError:]_block_invoke
+ ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.189
+ ___58-[BRCSharingAcceptFlowOperation _isAccountRestricted_step]_block_invoke
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.448
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.448.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.456
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.458
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.412
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.413
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.429
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.429.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.468
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.468.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.470
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.471
+ ___59-[BRCContainerScheduler _syncScheduleForContainersMetadata]_block_invoke.83
+ ___59-[BRCServerZone dumpTablesToContext:includeAllItems:error:]_block_invoke.297
+ ___60-[BRCSQLBackedSet enumerateObjectsWithSortOrder:usingBlock:]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.1
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.2
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.3
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.4
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.5
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.6
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.148.cold.7
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.149
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.159
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.166
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.1
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.2
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.cold.3
+ ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke
+ ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke.134
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.604
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.604.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.246
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.246.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.246.cold.2
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.248
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.251
+ ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke
+ ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke.204
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke.142
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_2
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_3
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_4
+ ___62-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.598
+ ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.428
+ ___63-[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:]_block_invoke
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.138
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.138.cold.1
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.138.cold.2
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.145
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.150
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.150.cold.1
+ ___63-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step]_block_invoke
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.89
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.89.cold.1
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.327
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.328
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.179
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.180
+ ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.299
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.645
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.645.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.645.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.646
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.83
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.83.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.86
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.86.cold.1
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.132
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.132.cold.1
+ ___66-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive_step]_block_invoke.cold.1
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke.195
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke_2
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.606
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.607
+ ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.93
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214.cold.1
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.214.cold.2
+ ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.219
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.417
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.417.cold.1
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.474
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.475
+ ___68-[BRCSaltingBatchOperation _createCKOperationForRecords:completion:]_block_invoke
+ ___68-[BRCSaltingBatchOperation _updateSaltingInfoInClientDBWithRecords:]_block_invoke
+ ___68-[BRCSaltingBatchOperation _updateSaltingInfoInServerDBWithRecords:]_block_invoke
+ ___68-[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]_block_invoke
+ ___68-[BRCThumbnailGenerationManager _addThumbnailOperation:thumbnailID:]_block_invoke.cold.1
+ ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.331
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.58
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.59
+ ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.59.cold.1
+ ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.303
+ ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.405
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.194
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.196
+ ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2.195
+ ___70-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.343
+ ___70-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke_2
+ ___70-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke_2.cold.1
+ ___70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.122
+ ___71-[BRCAccountSessionFPFS _recoverAndReportDanglingLostZombieDirectories]_block_invoke
+ ___71-[BRCAccountSessionFPFS waitForUploadsToCompleteInSyncBubbleWithReply:]_block_invoke
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.7
+ ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.7.cold.1
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.482
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.483
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.491
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.491.cold.1
+ ___71-[BRCMiniCiconia cleanupCiconiaAtURL:diagnosticsURL:completionHandler:]_block_invoke
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.660
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.641
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.85
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.89
+ ___72-[BRCUserNotification showJoinDialogForShareMetadata:ckContainer:reply:]_block_invoke
+ ___72-[BRCUserNotification showJoinDialogForShareMetadata:ckContainer:reply:]_block_invoke_2
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.600
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.593
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.148
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke.147
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke_2
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke.144
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2.145
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2.cold.1
+ ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.30
+ ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.31
+ ___73-[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]_block_invoke
+ ___73-[BRCThumbnailGenerationManager _removeThumbnailOperationForThumbnailID:]_block_invoke.cold.1
+ ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.406
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.568
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.79
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.87
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.92
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.88
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.93
+ ___74-[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]_block_invoke
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.1
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.10
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.2
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.3
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.4
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.5
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.6
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.7
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.8
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.36.cold.9
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.37
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.41
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.44
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.cold.1
+ ___74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.cold.2
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.613
+ ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.133
+ ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.133.cold.1
+ ___75+[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]_block_invoke
+ ___75+[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]_block_invoke.7
+ ___75+[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]_block_invoke.7.cold.1
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.22
+ ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.22.cold.1
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.172
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.173
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.cold.1
+ ___75-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.cold.2
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.610
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.611
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.664
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.667
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.666
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.666.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.188
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.188.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.189
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.189.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.189.cold.2
+ ___76-[BRCStageRegistry(FPFSAdditions) createStageURLForThumbnailFromItem:error:]_block_invoke
+ ___76-[BRCStageRegistry(FPFSAdditions) createStageURLForThumbnailFromItem:error:]_block_invoke.cold.1
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.602
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.602.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.565
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.596
+ ___77-[BRCAccountSessionFPFS(BRCDatabaseManager) _appLibrariesEnumerator:version:]_block_invoke
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke.203
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke.202
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2.cold.1
+ ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.410
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.129
+ ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.66
+ ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.cold.1
+ ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.cold.2
+ ___79-[BRCAccountSessionFPFS(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.80
+ ___79-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke
+ ___79-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke.659
+ ___80-[BRCAccountSessionFPFS(BRCDatabaseManager) runDatabaseFixupsForDB:serverTruth:]_block_invoke
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25.cold.1
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.25.cold.2
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26
+ ___80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke_2
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.555
+ ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.327
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.432
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.433
+ ___80-[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]_block_invoke
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.632
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.567
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.634
+ ___82-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke
+ ___82-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke.cold.1
+ ___82-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke.cold.2
+ ___82-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke.cold.3
+ ___82-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke.cold.4
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.102
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.102.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.102.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.103
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.103.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.103.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.104
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.104.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.107
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.504
+ ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.506
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.489
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.489.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.489.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.489.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.493
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.503
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.638
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.446
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.447
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.125
+ ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke
+ ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke_2
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke.cold.1
+ ___86-[BRCSafeDBHolder closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:]_block_invoke.cold.2
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.507
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.509
+ ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.296
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.90
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.92
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.43
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.43.cold.1
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.45
+ ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.60
+ ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.83
+ ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.86
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.320
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.320.cold.1
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.313
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.313.cold.1
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.315
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.315.cold.1
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.324
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.328
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.328.cold.1
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.328.cold.2
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.572
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]_block_invoke
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]_block_invoke.119
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]_block_invoke.120
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]_block_invoke.121
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke.60
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.105
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.130
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.138
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.575
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.576
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.582
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.587
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.588
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.585
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.131
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.624
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.108
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke.123
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.69
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.69.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.69.cold.2
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.69.cold.3
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.73
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.73.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.74
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.74.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.76
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.76.cold.1
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.352
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.353
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.354
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.355
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.356
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.357
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.597
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.597.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.598
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.601.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.603
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.604
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.127
+ ___96-[BRCClientZone(BRCBaseHashSaltAdditions) directUnsaltedItemsInServerTruthEnumeratorParentedTo:]_block_invoke
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14
+ ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14.cold.1
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.107
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.319
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.319.cold.1
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104bs_e17_B16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s40l8r96l8s48l8s56l8s64l8s88l8s72l8s80l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
+ ___block_descriptor_32_e19_24?0"NSData"8Q16l
+ ___block_descriptor_40_e8_32bs_e58_v32?0"NSData"8"NSFileProviderItemVersion"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e21_24?0"NSString"8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e27_v16?0"BRCFPImportReport"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e30_"NSData"16?0"BRCLocalItem"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"BRCContainerScheduler"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e48_v32?0"BRCItemGlobalID"8"BRCRequestData"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_41_e8_32s_e23_B16?0"BRCAppLibrary"8ls32l8
+ ___block_descriptor_44_e8_32s_e26_24?0"PQLResultSet"8^16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e36_v32?0"BRQueryItem"8Q16"NSError"24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"BRCServerItem"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_52_e8_32bs40r_e44_v24?0"FPImportProgressReport"8"NSError"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e23_v16?0"PQLConnection"8ls32l8r48l8s40l8
+ ___block_descriptor_60_e8_32s40bs48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_60_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_60_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e8_i12?0i8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e22_v24?0"NSString"8^B16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e28_v24?0"FPItem"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48w_e27_v16?0"BRCFPImportReport"8lw48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e27_v24?0"NSURL"8"NSError"16lr56l8s32l8s48l8s40l8
+ ___block_descriptor_65_e8_32s40s48r56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr48l8s32l8s40l8r56l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e20_v24?08"NSError"16lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48bs56bs64bs72w_e5_v8?0ls48l8w72l8s32l8s40l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8ls32l8s40l8w72l8s64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e8_v12?0B8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
+ ___block_literal_global.108
+ ___block_literal_global.1162
+ ___block_literal_global.117
+ ___block_literal_global.1180
+ ___block_literal_global.135
+ ___block_literal_global.139
+ ___block_literal_global.149
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.1619
+ ___block_literal_global.165
+ ___block_literal_global.1658
+ ___block_literal_global.1661
+ ___block_literal_global.169
+ ___block_literal_global.1700
+ ___block_literal_global.171
+ ___block_literal_global.1712
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.18
+ ___block_literal_global.180
+ ___block_literal_global.1816
+ ___block_literal_global.1824
+ ___block_literal_global.1866
+ ___block_literal_global.192
+ ___block_literal_global.2
+ ___block_literal_global.2049
+ ___block_literal_global.2084
+ ___block_literal_global.2090
+ ___block_literal_global.2095
+ ___block_literal_global.2096
+ ___block_literal_global.2122
+ ___block_literal_global.2141
+ ___block_literal_global.2144
+ ___block_literal_global.218
+ ___block_literal_global.227
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.2360
+ ___block_literal_global.2375
+ ___block_literal_global.241
+ ___block_literal_global.2460
+ ___block_literal_global.249
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.269
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.288
+ ___block_literal_global.298
+ ___block_literal_global.299
+ ___block_literal_global.30
+ ___block_literal_global.308
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.336
+ ___block_literal_global.35
+ ___block_literal_global.378
+ ___block_literal_global.387
+ ___block_literal_global.392
+ ___block_literal_global.399
+ ___block_literal_global.40
+ ___block_literal_global.409
+ ___block_literal_global.418
+ ___block_literal_global.425
+ ___block_literal_global.430
+ ___block_literal_global.435
+ ___block_literal_global.440
+ ___block_literal_global.445
+ ___block_literal_global.455
+ ___block_literal_global.460
+ ___block_literal_global.468
+ ___block_literal_global.473
+ ___block_literal_global.478
+ ___block_literal_global.496
+ ___block_literal_global.50
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.688
+ ___block_literal_global.70
+ ___block_literal_global.73
+ ___block_literal_global.768
+ ___block_literal_global.776
+ ___block_literal_global.82
+ ___block_literal_global.87
+ ___block_literal_global.88
+ ___block_literal_global.92
+ ___block_literal_global.93
+ ___br_update_tables_14_000_block_invoke.1178
+ ___br_update_tables_14_000_block_invoke.1178.cold.1
+ ___br_update_tables_30_000_block_invoke.1804
+ ___br_update_tables_30_000_block_invoke.1804.cold.1
+ ___br_update_tables_30_000_block_invoke.1804.cold.2
+ ___br_update_tables_30_000_block_invoke.1814
+ ___recursive_table_recreate_schema_block_invoke.1659
+ ___recursive_table_recreate_schema_block_invoke.1659.cold.1
+ __fetchManagersDictionary.managersByPersona
+ __fetchManagersDictionary.onceToken
+ __unnamed_array_storage.101
+ __unnamed_array_storage.111
+ __unnamed_array_storage.118
+ __unnamed_array_storage.119
+ __unnamed_array_storage.127
+ __unnamed_array_storage.128
+ __unnamed_array_storage.136
+ __unnamed_array_storage.137
+ __unnamed_array_storage.1549
+ __unnamed_array_storage.1592
+ __unnamed_array_storage.168
+ __unnamed_array_storage.186
+ __unnamed_array_storage.2436
+ __unnamed_array_storage.2454
+ __unnamed_array_storage.2666
+ __unnamed_array_storage.2708
+ __unnamed_array_storage.2724
+ __unnamed_array_storage.411
+ __unnamed_array_storage.414
+ _br_db_fixup_0
+ _br_update_tables_30_017
+ _br_update_tables_30_018
+ _br_update_tables_30_019
+ _br_update_tables_30_020
+ _br_update_tables_31_000
+ _br_update_tables_31_001
+ _br_update_tables_31_002
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
+ _item_errors_recreate_schema
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
+ _objc_msgSend$_calculateSignatureForFileAtURL:error:
+ _objc_msgSend$_calculateSignatureForPackageAtURL:error:
+ _objc_msgSend$_callFinishBlockOnDataRequest:finishError:
+ _objc_msgSend$_cancelJobs:state:uploadError:
+ _objc_msgSend$_checkIfShouldDedicateOpToSaltingBasehashItem:
+ _objc_msgSend$_cleanupOldCiconiaDomains:
+ _objc_msgSend$_closeDB
+ _objc_msgSend$_createCKOperationForRecords:completion:
+ _objc_msgSend$_createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:
+ _objc_msgSend$_createRecoveryExecutedErrorForImportError:
+ _objc_msgSend$_createSchemaForSQLType:error:
+ _objc_msgSend$_createStructureRecordForRootItem
+ _objc_msgSend$_createStructureRecordForServerItem:salt:
+ _objc_msgSend$_createStructureRecordWithRecordID:itemID:basehashSalt:statInfo:
+ _objc_msgSend$_databaseRootDirectory
+ _objc_msgSend$_daysSinceLastMigrationProgress:itemsNotMigrated:reconciledItems:
+ _objc_msgSend$_dbBecameCorrupted
+ _objc_msgSend$_dbgSleepIfRequested
+ _objc_msgSend$_deleteAppLibrary:documentsFolder:error:
+ _objc_msgSend$_fetchManagersDictionary
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
+ _objc_msgSend$_initWithPersonaIdentifier:
+ _objc_msgSend$_initWithURL:inPackage:forItem:error:
+ _objc_msgSend$_initWithVersionIdentifier:size:oldVersionIdentifier:contentSignature:
+ _objc_msgSend$_invalidateCahceIfNeeded
+ _objc_msgSend$_invalidateRequestsTableWithNewSource:
+ _objc_msgSend$_invalidateScreenLockManager
+ _objc_msgSend$_isFPFS
+ _objc_msgSend$_isIsSycBubble
+ _objc_msgSend$_isSharedIPad:
+ _objc_msgSend$_isTesting
+ _objc_msgSend$_locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:
+ _objc_msgSend$_performMetadataSaltingOperationIfNecessaryWithCompletion:
+ _objc_msgSend$_performModifyRecordsOrBatchOperationWithCompletion:
+ _objc_msgSend$_populateUUID:
+ _objc_msgSend$_processSaltingOnAppLibrary:
+ _objc_msgSend$_recoverAndReportDanglingLostZombieDirectories
+ _objc_msgSend$_recoverItemIDChangedWhileUploadingIfNecessary:
+ _objc_msgSend$_refreshLatestRevisionForItemIdentifier:reply:
+ _objc_msgSend$_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:
+ _objc_msgSend$_registerOperation:throttler:
+ _objc_msgSend$_registerStaticDBFunctionsWithError:
+ _objc_msgSend$_removeDiagnosticsDirectoryAtURL:withError:
+ _objc_msgSend$_removeFPDomain:error:
+ _objc_msgSend$_removeThumbnailOperationForThumbnailID:
+ _objc_msgSend$_removeWorkDirectory:
+ _objc_msgSend$_reportBasehashSalting
+ _objc_msgSend$_reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:
+ _objc_msgSend$_rescheduleJobsPendingScreenUnlock
+ _objc_msgSend$_saveAppLibraryIfNecessary:
+ _objc_msgSend$_saveItemID:version:record:contentBoundaryKey:iWorkSharingOptions:
+ _objc_msgSend$_scheduleAfterFlush:
+ _objc_msgSend$_sendDictionaryToCoreAnalytics:eventName:
+ _objc_msgSend$_setXattrs:stageRegistry:
+ _objc_msgSend$_setupExtensionID
+ _objc_msgSend$_shouldIgnoreReportForOperationType:ofSubtype:forError:
+ _objc_msgSend$_shouldRejectItemDeleteDueToEtags:baseVersion:error:
+ _objc_msgSend$_shouldTriggerTapToRadar:daysSinceLastMigrationProgress:
+ _objc_msgSend$_signalPropagationToChildrenForce:
+ _objc_msgSend$_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:
+ _objc_msgSend$_triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:
+ _objc_msgSend$_updateRootItemInClientDB
+ _objc_msgSend$_updateRootItemInServerDB
+ _objc_msgSend$_updateSaltingInfoInClientDBWithRecords:
+ _objc_msgSend$_updateSaltingInfoInServerDBWithRecords:
+ _objc_msgSend$_updateServerTruthForItemID:
+ _objc_msgSend$_utiForExtension:
+ _objc_msgSend$_validateAsset:advancedDataProtectionEnabled:
+ _objc_msgSend$addObject:error:
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
+ _objc_msgSend$br_prettyDescription
+ _objc_msgSend$br_shouldOverwriteExistingName
+ _objc_msgSend$br_signalEnumeratorForContainerItemIdentifier:completionHandler:
+ _objc_msgSend$brc_SHA256WithSalt:
+ _objc_msgSend$brc_errorAcceptShareFailedForItem:
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
+ _objc_msgSend$closeFD:
+ _objc_msgSend$contentBoundaryKeyForItemID:
+ _objc_msgSend$contentPolicyForZoneRoot:optimizeStorage:isAppInstalled:isWallet:isGreedyDocument:
+ _objc_msgSend$createSetOfClass:withSQLType:error:
+ _objc_msgSend$createStageURLForThumbnailFromItem:error:
+ _objc_msgSend$createStageURLFromLiveURLForItem:options:error:
+ _objc_msgSend$createStringsSetWithError:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dataWithSQL:
+ _objc_msgSend$dbIntegrityCheckBasehashSalting
+ _objc_msgSend$dbIntegrityCheckLostZombieDirectories
+ _objc_msgSend$debugItemIDStringWithVerbose:
+ _objc_msgSend$defaultCache
+ _objc_msgSend$defaultManagerWithPersonaIdentifier:
+ _objc_msgSend$defaultNavigator
+ _objc_msgSend$deleteItem:recursively:baseVersion:error:
+ _objc_msgSend$deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:
+ _objc_msgSend$directUnsaltedItemsInServerTruthEnumeratorParentedTo:
+ _objc_msgSend$dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:
+ _objc_msgSend$encryptedValues
+ _objc_msgSend$enumerateObjectsWithSortOrder:usingBlock:
+ _objc_msgSend$fetchLatestContentRevisionForItemIdentifier:reply:
+ _objc_msgSend$finishRequestForIdentifer:finishError:error:
+ _objc_msgSend$forceSignalPropagationToChildren
+ _objc_msgSend$fpfsStuckMigrationRecoveryDaysSinceImportStartedThreshold
+ _objc_msgSend$fpfsStuckMigrationRecoveryDaysSinceUpgradeThreshold
+ _objc_msgSend$fpfsStuckMigrationRecoveryDaysWithoutProgressThreshold
+ _objc_msgSend$fpfsStuckMigrationTakeReconciledItemsIntoAccount
+ _objc_msgSend$fpfsUploadV2
+ _objc_msgSend$getConfiguration
+ _objc_msgSend$getDomainsForProviderIdentifier:completionHandler:
+ _objc_msgSend$getKnowledgeUUID:andSequenceNumber:
+ _objc_msgSend$getOrGenerateChildBasehashSaltingKey
+ _objc_msgSend$importNewItemAtURL:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:
+ _objc_msgSend$initArrayOfClass:withSQLType:error:
+ _objc_msgSend$initWithBasehashSaltInfo:
+ _objc_msgSend$initWithBatchSize:
+ _objc_msgSend$initWithItemID:clientZone:
+ _objc_msgSend$initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:
+ _objc_msgSend$initWithPackageURL:error:
+ _objc_msgSend$initWithProgress:requestType:finishBlock:
+ _objc_msgSend$initWithRecordID:serverZone:isUserWaiting:maxBackoff:
+ _objc_msgSend$initWithRootItem:
+ _objc_msgSend$initWithShareMetadata:client:session:userNotifier:userActionsNavigator:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$invalidateRequestsOfClient:
+ _objc_msgSend$isAppLibraryRootItemIDWithSQLiteValue:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$isRunningOnMacOS
+ _objc_msgSend$isSeedBuild
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$isSyncBubbleClientEntitled
+ _objc_msgSend$itemNeedingBasehashSalting
+ _objc_msgSend$itemVersion
+ _objc_msgSend$lastBootHistoryTime
+ _objc_msgSend$lazyXattrWithStageRegistry:
+ _objc_msgSend$locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:
+ _objc_msgSend$locateRecordsThrottleParams
+ _objc_msgSend$newAppLibraryFromPQLResultSet:version:error:
+ _objc_msgSend$newBasehashSaltingProblemCountWithProblemCount:mangledID:itemIDString:
+ _objc_msgSend$newDanglingZombieProblemCountWithProblemCount:
+ _objc_msgSend$newEnumeratorForItemID:clientZone:
+ _objc_msgSend$newIntEvent:UUID:value:
+ _objc_msgSend$newItemForSignatureCalculationWithURL:inPackage:error:
+ _objc_msgSend$newLongEvent:UUID:value:
+ _objc_msgSend$newLongEvent:UUID:value:round:
+ _objc_msgSend$open:flags:
+ _objc_msgSend$openAppStoreForBundleID:
+ _objc_msgSend$openShareURLInWebBrowser:withReason:
+ _objc_msgSend$openiCloudSettings
+ _objc_msgSend$operationForThumbnailID:
+ _objc_msgSend$paddedFileSize
+ _objc_msgSend$priority
+ _objc_msgSend$providerDomainWithID:cachePolicy:error:
+ _objc_msgSend$refreshRevisionMaxBackoff
+ _objc_msgSend$registerAndSendNewContainerResetWithOutcome:
+ _objc_msgSend$registerAndSendNewFolderSharePCSChainingTime:chainedRecordsCount:zoneMangledID:itemIDString:error:analyticsReporter:
+ _objc_msgSend$registerAndSendNewPeriodicSyncWithOutcome:
+ _objc_msgSend$registerAndSendNewShareAcceptationWithLastStep:zoneMangledID:itemIDString:error:analyticsReporter:
+ _objc_msgSend$removeDomain:forProviderIdentifier:completionHandler:
+ _objc_msgSend$removeScreenLockObserver:
+ _objc_msgSend$retriableCKInteralErrorCodesForRejectedRequestedError
+ _objc_msgSend$rootChildBasehashSalt
+ _objc_msgSend$rootRecordCreated
+ _objc_msgSend$runDatabaseFixups
+ _objc_msgSend$runDatabaseFixupsForDB:serverTruth:
+ _objc_msgSend$saltingState
+ _objc_msgSend$saltingStateForItemID:
+ _objc_msgSend$screenLockChanged:
+ _objc_msgSend$seralizeBirthtime:
+ _objc_msgSend$serializeContentBoundaryKey:
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
+ _objc_msgSend$sharedConnectionProxy
+ _objc_msgSend$sharedScreenLockMonitor
+ _objc_msgSend$shouldUseAdvancedDataProtection
+ _objc_msgSend$showJoinDialogForShareMetadata:ckContainer:reply:
+ _objc_msgSend$signalPropagationToChildren
+ _objc_msgSend$signatureWithFileDescriptor:error:
+ _objc_msgSend$startDownloadFileObject:options:etagIfLoser:reply:
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
+ _objc_msgSend$updateContentSignature:error:
+ _objc_msgSend$useMMCSEncryptionV2
+ _objc_msgSend$validateAdvancedDataProtectionFieldsWithSession:error:
+ _objc_msgSend$validationKeyTruncationLength
+ _objc_msgSend$verbose
+ _objc_msgSend$waitForUploadsToCompleteInSyncBubbleWithReply:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_release_x11
+ _sharedABCReporter.onceToken
+ _sharedABCReporter.reporter
+ _sharedAnalytics.analytics
+ _sharedAnalytics.onceToken
+ _sleep
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newCiconiaReportEvent:state:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newIntEvent:eventGroupUUID:value:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:eventGroupUUID:value:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newLongEvent:eventGroupUUID:value:round:]
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.1
- +[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:].cold.2
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:forError:waitForCompletion:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:]
- +[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:]
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.1
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.2
- +[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:].cold.3
- +[BRCDaemonFPFS UTIForExtension:]
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
- -[BRCAccountSessionFPFS lastCiconiaVersion:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) getMigrationAttemptOriginatorIDsForVersion:withDB:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) getPreviousMigrationAttempts:failed:beforeVersion:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) getPreviousMigrationAttempts:failed:forVersion:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) getPreviousMigrationAttempts:failed:withVersion:comperator:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) newAppLibraryFromPQLResultSet:error:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]
- -[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]
- -[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:].cold.1
- -[BRCAccountSessionFPFS(FPFSAdditions) _fpckReportFileNameForMigrationID:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _saveFPCKStatusForTapToRadar:stats:report:withMigrationID:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent].cold.2
- -[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent].cold.3
- -[BRCAccountSessionFPFS(FPFSAdditions) _shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]
- -[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:].cold.1
- -[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:].cold.2
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
- -[BRCDaemonFPFS startedUpInSyncBubble]
- -[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildren]
- -[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildren].cold.1
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.1
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.2
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.3
- -[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:].cold.4
- -[BRCFSImporter _updateCiconiaDatabaseForBouncing:existingItem:]
- -[BRCFSImporter changeItem:baseVersion:changedFields:newValues:contents:additionalAttrs:clearCKInfoOnSyncUp:stillPendingFields:error:].cold.7
- -[BRCFSImporter importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:]
- -[BRCFSImporter importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:].cold.1
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
- -[BRCPackageItem(FPFSAdditions) initWithURL:inPackage:forItem:error:].cold.1
- -[BRCQueryItemUtil contentPolicyForZoneRoot:isAppInstalled:isWallet:isGreedyDocument:]
- -[BRCRecentsEnumerator(FPFSAdditions) itemWasDeletedWithFileObjectID:notifRank:].cold.1
- -[BRCRecentsEnumeratorBatch init]
- -[BRCSafeDBHolder closeWithError:].cold.1
- -[BRCSafeDBHolder closeWithError:].cold.2
- -[BRCSafeDBHolder closeWithError:].cold.3
- -[BRCServerZone _saveItemID:version:record:iWorkSharingOptions:]
- -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion]
- -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion].cold.1
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
- -[BRCSharingAcceptFlowOperation _setSpotlightAttribute]
- -[BRCSharingAcceptFlowOperation _setSpotlightAttribute].cold.1
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
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner].cold.3
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient].cold.1
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient].cold.2
- -[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient].cold.3
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
- -[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]
- -[BRCStatInfo lazyXattrWithSession:]
- -[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]
- -[BRCSyncUpOperation prepareWithMaxCost:retryAfter:].cold.8
- -[BRCSyncUpOperationBuilder addItem:].cold.3
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
- -[BRCUserDefaults runFPCKInPostImportAnalysis]
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
- -[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:].cold.1
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
- -[FPCKStats(BRAdditions) br_description]
- -[FPCKStats(BRAdditions) br_getStatsErrorBitmap]
- -[NSData(BRCCryptographicAdditions) brc_SHA256WithSalt:]
- -[NSFileProviderItemVersion(BRItemAdditions) description]
- -[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]
- -[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:].cold.1
- GCC_except_table131
- GCC_except_table138
- GCC_except_table154
- GCC_except_table161
- GCC_except_table163
- GCC_except_table165
- GCC_except_table183
- GCC_except_table187
- GCC_except_table188
- GCC_except_table195
- GCC_except_table198
- GCC_except_table203
- GCC_except_table206
- GCC_except_table214
- GCC_except_table220
- GCC_except_table223
- GCC_except_table228
- GCC_except_table230
- GCC_except_table239
- GCC_except_table264
- GCC_except_table269
- GCC_except_table276
- GCC_except_table278
- GCC_except_table281
- GCC_except_table282
- GCC_except_table304
- GCC_except_table307
- GCC_except_table314
- GCC_except_table317
- GCC_except_table318
- GCC_except_table320
- GCC_except_table332
- GCC_except_table339
- GCC_except_table354
- GCC_except_table359
- GCC_except_table364
- GCC_except_table370
- GCC_except_table375
- GCC_except_table378
- GCC_except_table380
- GCC_except_table385
- GCC_except_table388
- GCC_except_table391
- GCC_except_table394
- GCC_except_table403
- GCC_except_table406
- GCC_except_table411
- GCC_except_table415
- GCC_except_table417
- GCC_except_table419
- GCC_except_table422
- GCC_except_table431
- GCC_except_table439
- GCC_except_table441
- GCC_except_table444
- GCC_except_table446
- GCC_except_table448
- GCC_except_table451
- GCC_except_table452
- GCC_except_table55
- GCC_except_table89
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
- _AppTelemetryCiconiaBouncesInvestigationReadFrom
- _AppTelemetryCiconiaEAccessInvestigationReadFrom
- _AppTelemetryCiconiaInvestigationReadFrom
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
- _BRIsFPFSCiconiaOnly
- _NSTemporaryDirectory
- _OBJC_CLASS_$_AppTelemetryCiconiaBouncesInvestigation
- _OBJC_CLASS_$_AppTelemetryCiconiaEAccessInvestigation
- _OBJC_CLASS_$_AppTelemetryCiconiaInvestigation
- _OBJC_CLASS_$_BRDeviceConfiguration
- _OBJC_CLASS_$_FPCKStats
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_IVAR_$_BRCAccountsManager._isInSyncBubble
- _OBJC_IVAR_$_BRCAnalyticsReporter._currentTelemetryToken
- _OBJC_IVAR_$_BRCAnalyticsReporter._forceTelemetryDequeueQueued
- _OBJC_IVAR_$_BRCAnalyticsReporter._lastSentTelemetryEvents
- _OBJC_IVAR_$_BRCAnalyticsReporter._lastTelemetryBatchRowIDs
- _OBJC_IVAR_$_BRCAnalyticsReporter._syncTelemetryState
- _OBJC_IVAR_$_BRCAppLibrary._activeAliasQueries
- _OBJC_IVAR_$_BRCAppLibrary._activeQueries
- _OBJC_IVAR_$_BRCAppLibrary._activeRecursiveQueries
- _OBJC_IVAR_$_BRCAppLibrary._db
- _OBJC_IVAR_$_BRCAppLibrary._dbRowID
- _OBJC_IVAR_$_BRCAppLibrary._defaultClientZone
- _OBJC_IVAR_$_BRCAppLibrary._mangledID
- _OBJC_IVAR_$_BRCAppLibrary._session
- _OBJC_IVAR_$_BRCAppTelemetryConverter._investigationKeysToRemove
- _OBJC_IVAR_$_BRCAppTelemetryConverter._oldToNewKeys
- _OBJC_IVAR_$_BRCFSUploader._thumbnailQueue
- _OBJC_IVAR_$_BRCFSUploader._thumbnailsOperations
- _OBJC_IVAR_$_BRCPrivateClientZone._createZoneOperation
- _OBJC_IVAR_$_BRCPrivateClientZone._createZoneQueue
- _OBJC_IVAR_$_BRCPrivateClientZone._zoneCreationCompletionBlocks
- _OBJC_IVAR_$_BRCSharingCopyParticipantTokenOperation._shouldFetchParticipantDocumentToken
- _OBJC_IVAR_$_BRCStageRegistry._currentlyDumpingForCiconia
- _OBJC_METACLASS_$_AppTelemetryCiconiaBouncesInvestigation
- _OBJC_METACLASS_$_AppTelemetryCiconiaEAccessInvestigation
- _OBJC_METACLASS_$_AppTelemetryCiconiaInvestigation
- _UTIForExtension:.onceToken
- _UTIForExtension:.utiCache
- _XPC_ACTIVITY_INTERVAL_15_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- __OBJC_$_CATEGORY_FPCKStats_$_BRAdditions
- __OBJC_$_CLASS_METHODS_NSData(BRCSignatureAdditions|BRCCryptographicAdditions|BRCQuarantine)
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_INSTANCE_METHODS_AppTelemetryCiconiaInvestigation
- __OBJC_$_INSTANCE_METHODS_BRCClientZone(BRCZoneReset|FPFSAdditions)
- __OBJC_$_INSTANCE_METHODS_FPCKStats(BRAdditions)
- __OBJC_$_INSTANCE_METHODS_NSData(BRCSignatureAdditions|BRCCryptographicAdditions|BRCQuarantine)
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_INSTANCE_VARIABLES_AppTelemetryCiconiaInvestigation
- __OBJC_$_INSTANCE_VARIABLES_BRCAppTelemetryConverter
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_$_PROP_LIST_AppTelemetryCiconiaInvestigation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CiconiaProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_CiconiaProtocol
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_CLASS_PROTOCOLS_$_AppTelemetryCiconiaInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_CLASS_RO_$_AppTelemetryCiconiaInvestigation
- __OBJC_LABEL_PROTOCOL_$_CiconiaProtocol
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaBouncesInvestigation
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaEAccessInvestigation
- __OBJC_METACLASS_RO_$_AppTelemetryCiconiaInvestigation
- __OBJC_PROTOCOL_$_CiconiaProtocol
- __OBJC_PROTOCOL_REFERENCE_$_CiconiaProtocol
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.456
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.456.cold.1
- ___100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.460
- ___101-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:]_block_invoke
- ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke
- ___102-[BRCXPCRegularIPCsClient reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:]_block_invoke.662
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.86
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.61
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.61.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.63
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.65
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.68
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.68.cold.1
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.93
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.93.cold.1
- ___108-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.638
- ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.96
- ___111-[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:]_block_invoke.162
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke.cold.1
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke.cold.2
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke.cold.3
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke.cold.4
- ___113-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke.cold.5
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.222
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.222.cold.1
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.224
- ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.416
- ___117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.417
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.73
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.74
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.29
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.31
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.31.cold.1
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.32
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke_2
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke_2.cold.1
- ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke_2.cold.2
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.198
- ___188-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke
- ___188-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]_block_invoke.68
- ___22-[BRCClientZone close]_block_invoke.62
- ___22-[BRCDaemonFPFS start]_block_invoke.91
- ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.120
- ___25-[BRCFSUploader schedule]_block_invoke.112
- ___26-[BRCStageRegistry resume]_block_invoke.152
- ___26-[BRCStageRegistry resume]_block_invoke.160
- ___26-[BRCStageRegistry resume]_block_invoke.161
- ___26-[BRCStageRegistry resume]_block_invoke.161.cold.1
- ___26-[BRCStageRegistry resume]_block_invoke.161.cold.2
- ___26-[BRCStageRegistry resume]_block_invoke.161.cold.3
- ___26-[BRCSyncUpOperation main]_block_invoke.56
- ___27-[BRCClientZone _startSync]_block_invoke.180
- ___27-[BRCClientZone _startSync]_block_invoke.184.cold.1
- ___27-[BRCClientZone _startSync]_block_invoke.184.cold.2
- ___27-[BRCDaemonFPFS selfCheck:]_block_invoke.145
- ___29-[BRCAccountMigrator perform]_block_invoke.95
- ___29-[BRCAccountMigrator perform]_block_invoke.95.cold.1
- ___30-[BRCAccountSessionFPFS close]_block_invoke.262
- ___32-[BRCPeriodicSyncOperation main]_block_invoke.15
- ___32-[BRCPeriodicSyncOperation main]_block_invoke_2.19
- ___33+[BRCDaemonFPFS UTIForExtension:]_block_invoke
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.208
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.208.cold.1
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.213
- ___34-[BRCPendingChangesStream _openDB]_block_invoke.213.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.135
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.135.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.1
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.2
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.3
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.142.cold.4
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.146
- ___36-[BRCSharingSaveShareOperation main]_block_invoke.148
- ___37-[BRCAccountMigrationChecker perform]_block_invoke.110
- ___37-[BRCAccountMigrationChecker perform]_block_invoke.110.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.230
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.232.cold.3
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.240
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.240.cold.1
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.211
- ___39-[BRCSharingDestroyShareOperation main]_block_invoke.165
- ___39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.87
- ___40-[BRCFSUploader initWithAccountSession:]_block_invoke_3.cold.1
- ___40-[BRCPQLConnection setProfilingEnabled:]_block_invoke.36
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.286
- ___41-[BRCAccountSessionFPFS destroyLocalData]_block_invoke.286.cold.1
- ___41-[BRCSyncUpOperation performShareUpdate:]_block_invoke.41
- ___42-[BRCPendingChangesStream destroyDatabase]_block_invoke
- ___42-[BRCPendingChangesStream destroyDatabase]_block_invoke.cold.1
- ___43-[BRCAnalyticsReporter findTelemetryEvent:]_block_invoke
- ___44-[BRCAnalyticsReporter _getPriorityOfEvent:]_block_invoke
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.154
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.154.cold.1
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke.158
- ___44-[BRCDaemonFPFS networkReachabilityChanged:]_block_invoke_2.159
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.230
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.231
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.234
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke.247
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.233
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_2.233.cold.1
- ___45-[BRCAccountSessionFPFS _fixupItemsAtStartup]_block_invoke_3.239
- ___45-[BRCAnalyticsReporter forceTelemetryDequeue]_block_invoke
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.320
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.320.cold.1
- ___46-[BRCFSUploader setState:forUploadJobID:zone:]_block_invoke
- ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.448
- ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.329
- ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.292
- ___47-[BRCSharingCopyParticipantTokenOperation main]_block_invoke.276
- ___48-[BRCContainerScheduler _syncScheduleForSideCar]_block_invoke.103
- ___48-[BRCSharingAcceptFlowOperation _isAppInstalled]_block_invoke
- ___48-[BRCSharingAcceptFlowOperation _isAppInstalled]_block_invoke.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.2
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.3
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.287.cold.4
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.294
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.294.cold.1
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.309
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.309.cold.1
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.1
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.2
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.3
- ___49-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke.156.cold.4
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.335
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.336
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.337
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.342
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.554
- ___50-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke
- ___50-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke.cold.1
- ___50-[BRCLocalItem saveToDBForServerEdit:keepAliases:]_block_invoke.cold.13
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke.cold.1
- ___50-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke.cold.2
- ___50-[BRCStageRegistry setCurrentlyDumpingForCiconia:]_block_invoke
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.225
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.225.cold.1
- ___51-[BRCContainerScheduler _syncScheduleForZoneHealth]_block_invoke.95
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.211
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
- ___51-[BRCXPCRegularIPCsClient queryLastCiconiaVersion:]_block_invoke.657
- ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke.167
- ___52-[BRCAccountSessionFPFS openWithError:pushWorkloop:]_block_invoke_3
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.131
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke.131.cold.1
- ___52-[BRCDaemonFPFS listener:shouldAcceptNewConnection:]_block_invoke_2.137
- ___52-[BRCSharingAcceptFlowOperation _parseShareMetadata]_block_invoke
- ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.412
- ___53-[BRCAccountSessionFPFS(BRCDatabaseManager) closeDBs]_block_invoke.413
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
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.498
- ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.162
- ___54-[BRCAccountHandler startAndLoadAccountSynchronously:]_block_invoke.164
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76.cold.1
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.76.cold.2
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.414
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.415
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.441
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.442
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke.124
- ___54-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]_block_invoke_2
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.169
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.169.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.170
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.177
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.177.cold.1
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke.178
- ___55-[BRCAccountSessionFPFS _pcsChainAllItemsWithActivity:]_block_invoke_2.179
- ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.39
- ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.41
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.1
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.2
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.3
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.4
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.5
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.6
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.152.cold.7
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.153
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.163
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.170
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.1
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.2
- ___55-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk]_block_invoke.cold.3
- ___55-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke
- ___55-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke.139
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.706
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.707
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
- ___56-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk]_block_invoke.209
- ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.278
- ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.280
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97.cold.1
- ___57+[BRCItemID migrateItemIDsToVersion11WithDB:serverTruth:]_block_invoke.97.cold.2
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.215
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.224
- ___57-[BRCAccountSessionFPFS _registerBackgroundXPCActivities]_block_invoke.227
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.468
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.468.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.468.cold.2
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.469
- ___57-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke.145
- ___57-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke.147
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke.147
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_2
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_3
- ___57-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_4
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.338
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.339
- ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.188
- ___58-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively]_block_invoke
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.467
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.469
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.423
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.424
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.464
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.464.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.466
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.467
- ___59-[BRCServerZone dumpTablesToContext:includeAllItems:error:]_block_invoke.290
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.606.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.242
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.242.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.242.cold.2
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.244
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.247
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.137
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.137.cold.1
- ___61-[BRCSharingAcceptFlowOperation _isUserSignedInToiCloudDrive]_block_invoke.cold.1
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke.200
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke_2
- ___61-[BRCXPCRegularIPCsClient reportDummyCiconiaMigration:reply:]_block_invoke
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.600
- ___62-[BRCXPCRegularIPCsClient logoutAccountWithACAccountID:reply:]_block_invoke.439
- ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke
- ___62-[BRCXPCRegularIPCsClient reportFinishedMigration:uuid:reply:]_block_invoke.683
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.157
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.157.cold.1
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.157.cold.2
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.165
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.170
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.170.cold.1
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.85
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.85.cold.1
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.324
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.325
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.168
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.169
- ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke_2
- ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.289
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.647.cold.2
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.648
- ___66-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]_block_invoke
- ___66-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]_block_invoke_2
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.103
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.103.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.105
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.105.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.106
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.106.cold.1
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.608
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.611
- ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.82
- ___67-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke
- ___67-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke.177
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.1
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.213.cold.2
- ___67-[BRCFSDownloader _finishedDownload:syncContext:operationID:error:]_block_invoke.218
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428.cold.1
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.470
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.471
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke.151
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke_2
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke.149
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2
- ___68-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2.cold.1
- ___68-[BRCUserNotification showJoinDialogForShareMetadata:session:reply:]_block_invoke
- ___68-[BRCUserNotification showJoinDialogForShareMetadata:session:reply:]_block_invoke_2
- ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.322
- ___69-[BRCAccountSessionFPFS(BRCDatabaseManager) _appLibrariesEnumerator:]_block_invoke
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.48
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.49
- ___69-[BRCSyncUpOperation _performUpdateSharingProtectionDataIfNecessary:]_block_invoke.49.cold.1
- ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.293
- ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.416
- ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.193
- ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke.195
- ___70-[BRCAccountSessionFPFS _recoverAndReportContentPolicyWithCompletion:]_block_invoke_2.194
- ___70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke_5
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403.cold.1
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.403.cold.2
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.406
- ___70-[BRCXPCRegularIPCsClient refreshSharingStateForItemIdentifier:reply:]_block_invoke.406.cold.1
- ___70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.133
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.6
- ___71-[BRCAccountsManager cleanupAccountDataForLoggedOutAccountWithPersona:]_block_invoke.6.cold.1
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.478
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.479
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.487
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.487.cold.1
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.656
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.643
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.75
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.78
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke.208
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke.207
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2
- ___72-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2.cold.1
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.602
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.595
- ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.19
- ___73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.20
- ___73-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:forCiconia:reply:]_block_invoke
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.417
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.572
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.78
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.86
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.90
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.87
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.92
- ___74-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]_block_invoke
- ___74-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]_block_invoke.cold.1
- ___74-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]_block_invoke.cold.2
- ___74-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]_block_invoke.cold.3
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.617
- ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.116
- ___74-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDOfAppLibraryID:reply:]_block_invoke.116.cold.1
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.21
- ___75+[NSString(BRCPathAdditions) br_currentMobileDocumentsDirWithRefreshCache:]_block_invoke.21.cold.1
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.612
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.613
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.760
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.763
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.762
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.762.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.193
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.193.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.194.cold.2
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.604.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.568
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.598
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.1
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.2
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.3
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.4
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.5
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.6
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.7
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.8
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.26.cold.9
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.27
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.31
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.34
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.cold.1
- ___77-[BRCSyncUpOperation _performModifyRecordsOrPCSChainOperationWithCompletion:]_block_invoke.cold.2
- ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.421
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.112
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.75
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.75.cold.1
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.82
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.82.cold.1
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.82.cold.2
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke.97
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_2.103
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_3.109
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_4
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_4.116
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5.122
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5.cold.1
- ___78+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_6
- ___79-[BRCAccountSessionFPFS(BRCDatabaseManager) _registerDynamicDBFunctions:error:]_block_invoke.131
- ___80-[BRCAccountSessionFPFS(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]_block_invoke
- ___80-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPFSImportFinishedTelemetryEvent]_block_invoke.172
- ___80-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPFSImportFinishedTelemetryEvent]_block_invoke_2
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.565
- ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.317
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.443
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.444
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.634
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.569
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.636
- ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke
- ___82-[BRCXPCRegularIPCsClient signalStartOfSilentTelemetry:uuid:manual:version:reply:]_block_invoke.658
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.119
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.119.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.119.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.120
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.120.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.120.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.121
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.121.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.121.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.122
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.122.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.122.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.123
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.123.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.123.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.124
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.124.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.126
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.515
- ___84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.517
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.500.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.514
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.640
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.457
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.458
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.346
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.347
- ___86-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:reply:]_block_invoke.348
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.518
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.520
- ___87-[BRCAccountSessionFPFS(FPFSAdditions) triggerFPFSImportFinishedTelemetryEventIfNeeded]_block_invoke_2
- ___87-[BRCAccountSessionFPFS(FPFSAdditions) triggerFPFSImportFinishedTelemetryEventIfNeeded]_block_invoke_3
- ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.286
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.79
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.81
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.33
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.33.cold.1
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.35
- ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.72
- ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.95
- ___88-[BRCAccountSessionFPFS _addOrImportDomainIfNeededWithError:domainAdded:domainImported:]_block_invoke.98
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.317
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.317.cold.1
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355.cold.1
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.357
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.357.cold.1
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.366
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.375
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.375.cold.1
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.370
- ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.370.cold.1
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.574
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.95
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.109
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.109.cold.1
- ___89-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke.cold.1
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.113
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.121
- ___90-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]_block_invoke
- ___90-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]_block_invoke.cold.1
- ___90-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]_block_invoke.cold.2
- ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke
- ___90-[BRCXPCRegularIPCsClient reportItemMismatchDuringSilentMigration:information:uuid:reply:]_block_invoke.661
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.580
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.581
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.586
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.590
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.591
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.587
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.114
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.626
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.98
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke.106
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke.107
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]_block_invoke.108
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.53
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.53.cold.1
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.54
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.54.cold.1
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.55
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke.57
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.343
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.344
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.345
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.694
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.694.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.695
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.697
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.697.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.697.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.699
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.700
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.110
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.15
- ___97+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.15.cold.1
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.97
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.316
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.316.cold.1
- ___BRCSendDictionaryToCoreAnalytics_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e17_B16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s88l8s72l8s80l8
- ___block_descriptor_32_e16_16?0"NSData"8l
- ___block_descriptor_40_e8_32s_e18_16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e23_v16?0"PQLConnection"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v12?0I8ls32l8
- ___block_descriptor_44_e8_32r_e44_v24?0"FPImportProgressReport"8"NSError"16lr32l8
- ___block_descriptor_48_e8_32bs40w_e30_v24?0"NSNumber"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s40r_e23_B16?0"BRCAppLibrary"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e23_v16?0"CKRequestInfo"8ls32l8s40l8
- ___block_descriptor_52_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e28_v24?0"FPItem"8"NSError"16ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e20_v24?08"NSError"16lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e23_v16?0"PQLConnection"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e23_v16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s56s_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56r_e34_v24?0"NSDictionary"8"NSError"16lr56l8s32l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e61_v40?0"NSString"8"FPCKStats"16"NSDictionary"24"NSError"32lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88w_e17_v16?0"NSError"8ls32l8s40l8w88l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.105
- ___block_literal_global.111
- ___block_literal_global.1158
- ___block_literal_global.1176
- ___block_literal_global.118
- ___block_literal_global.122
- ___block_literal_global.124
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.129
- ___block_literal_global.134
- ___block_literal_global.141
- ___block_literal_global.15
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.157
- ___block_literal_global.1618
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.1654
- ___block_literal_global.1657
- ___block_literal_global.166
- ___block_literal_global.167
- ___block_literal_global.168
- ___block_literal_global.1702
- ___block_literal_global.1724
- ___block_literal_global.1736
- ___block_literal_global.178
- ___block_literal_global.181
- ___block_literal_global.1821
- ___block_literal_global.1829
- ___block_literal_global.1887
- ___block_literal_global.191
- ___block_literal_global.2053
- ___block_literal_global.2070
- ___block_literal_global.2079
- ___block_literal_global.2098
- ___block_literal_global.2101
- ___block_literal_global.2102
- ___block_literal_global.2108
- ___block_literal_global.2113
- ___block_literal_global.217
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.237
- ___block_literal_global.2380
- ___block_literal_global.2395
- ___block_literal_global.2480
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.259
- ___block_literal_global.264
- ___block_literal_global.266
- ___block_literal_global.273
- ___block_literal_global.285
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.302
- ___block_literal_global.322
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.369
- ___block_literal_global.398
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.424
- ___block_literal_global.429
- ___block_literal_global.446
- ___block_literal_global.462
- ___block_literal_global.467
- ___block_literal_global.472
- ___block_literal_global.477
- ___block_literal_global.482
- ___block_literal_global.487
- ___block_literal_global.492
- ___block_literal_global.500
- ___block_literal_global.505
- ___block_literal_global.557
- ___block_literal_global.66
- ___block_literal_global.71
- ___block_literal_global.74
- ___block_literal_global.766
- ___block_literal_global.77
- ___block_literal_global.772
- ___block_literal_global.784
- ___block_literal_global.91
- ___block_literal_global.96
- ___br_update_tables_14_000_block_invoke.1174
- ___br_update_tables_14_000_block_invoke.1174.cold.1
- ___br_update_tables_30_000_block_invoke.1809
- ___br_update_tables_30_000_block_invoke.1809.cold.1
- ___br_update_tables_30_000_block_invoke.1809.cold.2
- ___br_update_tables_30_000_block_invoke.1819
- ___recursive_table_recreate_schema_block_invoke.1655
- ___recursive_table_recreate_schema_block_invoke.1655.cold.1
- __getPriorityOfEvent:.HIGH_PRIORITY_EVENTS
- __getPriorityOfEvent:.HIGH_PRIORITY_TELEMTRY_DOMAINS
- __getPriorityOfEvent:.onceToken
- __unnamed_array_storage.115
- __unnamed_array_storage.122
- __unnamed_array_storage.123
- __unnamed_array_storage.131
- __unnamed_array_storage.132
- __unnamed_array_storage.140
- __unnamed_array_storage.141
- __unnamed_array_storage.150
- __unnamed_array_storage.152
- __unnamed_array_storage.1548
- __unnamed_array_storage.1591
- __unnamed_array_storage.165
- __unnamed_array_storage.1715
- __unnamed_array_storage.1716
- __unnamed_array_storage.183
- __unnamed_array_storage.194
- __unnamed_array_storage.195
- __unnamed_array_storage.240
- __unnamed_array_storage.241
- __unnamed_array_storage.2456
- __unnamed_array_storage.2474
- __unnamed_array_storage.249
- __unnamed_array_storage.250
- __unnamed_array_storage.258
- __unnamed_array_storage.259
- __unnamed_array_storage.2631
- __unnamed_array_storage.2643
- __unnamed_array_storage.2722
- __unnamed_array_storage.2771
- __unnamed_array_storage.448
- __unnamed_array_storage.451
- _br_update_tables_30_000.cold.8
- _getegid
- _kBRCiconiaVersion
- _kSymptomDiagnosticActionGetNetworkInfo
- _objc_msgSend$_ciconiaOriginatorIDs:byDefault:
- _objc_msgSend$_createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:
- _objc_msgSend$_doneFetchingThumbnailForJobID:
- _objc_msgSend$_fetchTelemetryEventCountOrAdd:
- _objc_msgSend$_fpckReportFileNameForMigrationID:
- _objc_msgSend$_garbageCollectUploadThumbnails
- _objc_msgSend$_getPriorityOfEvent:
- _objc_msgSend$_handleTrashedItemsMigration
- _objc_msgSend$_isCiconiaErrorTTRWorthy:
- _objc_msgSend$_isExpectedCiconiaError:originatorId:
- _objc_msgSend$_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:
- _objc_msgSend$_openAppStoreForShareURL:
- _objc_msgSend$_openShareURLInWebBrowser:withReason:
- _objc_msgSend$_openiCloudSettings
- _objc_msgSend$_performModifyRecordsOrPCSChainOperationWithCompletion:
- _objc_msgSend$_postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:
- _objc_msgSend$_postponeLoserForWinner:etag:
- _objc_msgSend$_prepareSyncTelemetryEventsToSend
- _objc_msgSend$_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:
- _objc_msgSend$_reportEAccessDuringSilentMigration:uuid:
- _objc_msgSend$_reportForFPFSImportStatusTelemetryEventIfNeeded:
- _objc_msgSend$_reportOverBounceDuringSilentMigration:total:uuid:
- _objc_msgSend$_saveFPCKStatusForTapToRadar:stats:report:withMigrationID:
- _objc_msgSend$_saveItemID:version:record:iWorkSharingOptions:
- _objc_msgSend$_setTelemetryHeaderOnCKOpIfNecessary:
- _objc_msgSend$_setXattrs:session:
- _objc_msgSend$_shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:
- _objc_msgSend$_signalPropagationToChildren
- _objc_msgSend$_startFetchThumbnail:jobID:
- _objc_msgSend$_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:
- _objc_msgSend$_thumbnailOperationForItemRowID:
- _objc_msgSend$_triggerFPCKForProviderDomainID:completionHandler:
- _objc_msgSend$_updateCiconiaDatabaseForBouncing:existingItem:
- _objc_msgSend$_updateCiconiaState:uuid:
- _objc_msgSend$allowForceTelemetryDequeue
- _objc_msgSend$bounceReport
- _objc_msgSend$bouncedDocumentsFolders
- _objc_msgSend$bouncedItems
- _objc_msgSend$bouncedItemsMatrix
- _objc_msgSend$br_description
- _objc_msgSend$br_getStatsErrorBitmap
- _objc_msgSend$br_quotaUpdateTelemetry
- _objc_msgSend$captureLogsForOperationType:ofSubtype:withContext:
- _objc_msgSend$ciconiaOriginatorIDsTTRWorthy
- _objc_msgSend$cleanupCiconiaForPersonaID:atURL:diagnosticsURL:withReply:
- _objc_msgSend$cloningDuration
- _objc_msgSend$cloudEnabledStatusForSession:
- _objc_msgSend$container
- _objc_msgSend$contentPolicyForZoneRoot:isAppInstalled:isWallet:isGreedyDocument:
- _objc_msgSend$copyDatabaseForFPCKStartingAtPath:completionHandler:
- _objc_msgSend$copyItemAtPath:toPath:error:
- _objc_msgSend$crashReporterKey
- _objc_msgSend$createSQLConditionForRowIDs:
- _objc_msgSend$createStageURLFromLiveURLForItem:error:
- _objc_msgSend$datalessItems
- _objc_msgSend$deserializeVersion:fakeStatInfo:clientZone:error:
- _objc_msgSend$documentsFoldersWithoutItemID
- _objc_msgSend$dropAllSyncTelemetryEvents
- _objc_msgSend$dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:
- _objc_msgSend$eaccessReport
- _objc_msgSend$expectedAmountOfItemsMigrated
- _objc_msgSend$fetchParticipantDocumentToken
- _objc_msgSend$forceTelemetryDequeue
- _objc_msgSend$forceTelemetryDequeuePercentage
- _objc_msgSend$forceTelemetryDequeueWithCompletionHandler:
- _objc_msgSend$fpfsMigrationFinishedTelemetryXPCActivity
- _objc_msgSend$getPreviousMigrationAttempts:failed:beforeVersion:
- _objc_msgSend$getPreviousMigrationAttempts:failed:forVersion:
- _objc_msgSend$getPreviousMigrationAttempts:failed:withVersion:comperator:
- _objc_msgSend$has_acls
- _objc_msgSend$highPriorityTelemetryEventsPercentage
- _objc_msgSend$ignoredContentProtectedItems
- _objc_msgSend$importDuration
- _objc_msgSend$importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:
- _objc_msgSend$incidents
- _objc_msgSend$initForTestingDevice:
- _objc_msgSend$initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:
- _objc_msgSend$initWithRecordID:serverZone:isUserWaiting:
- _objc_msgSend$initWithShareMetadata:client:session:
- _objc_msgSend$itemsChangedDuringCloning
- _objc_msgSend$itemsNotFoundInDB
- _objc_msgSend$itemsThatAreNotMigrated
- _objc_msgSend$lastCiconiaVersion:
- _objc_msgSend$lazyXattrWithSession:
- _objc_msgSend$manuallyTriggered
- _objc_msgSend$materialisedCountOnFPFS
- _objc_msgSend$materialisedCountOnICD
- _objc_msgSend$minForceTelemetrySyncInterval
- _objc_msgSend$newAppLibraryFromPQLResultSet:error:
- _objc_msgSend$newAppTelemetryMetricEvent:
- _objc_msgSend$newDoubleEvent:eventGroupUUID:value:
- _objc_msgSend$newDroppedEventWithCount:
- _objc_msgSend$newIntEvent:eventGroupUUID:value:
- _objc_msgSend$newLongEvent:eventGroupUUID:value:
- _objc_msgSend$newLongEvent:eventGroupUUID:value:round:
- _objc_msgSend$newTimestampEvent:eventGroupUUID:value:
- _objc_msgSend$nonSideFaultsCompletelyMigrated
- _objc_msgSend$numberFromString:
- _objc_msgSend$numberOfBrokenFilesInFSAndFSSnapshotCheck
- _objc_msgSend$numberOfBrokenFilesInFSSnapshotAndFPSnapshotCheck
- _objc_msgSend$numberOfBrokenFilesInReconciliationTableCheck
- _objc_msgSend$numberOfFilesChecked
- _objc_msgSend$offline
- _objc_msgSend$orderedSet
- _objc_msgSend$outputStreamToFileAtPath:append:
- _objc_msgSend$packageItemsForFileObjectID:order:db:
- _objc_msgSend$packagesWithoutBundleBit
- _objc_msgSend$protection_class
- _objc_msgSend$providerDomainWithID:error:
- _objc_msgSend$responseHTTPHeaders
- _objc_msgSend$runFPCKForDomainWithID:databasesBackupsPath:options:reason:completionHandler:
- _objc_msgSend$runFPCKInPostImportAnalysis
- _objc_msgSend$serializeFilename:forCreation:
- _objc_msgSend$serializeFilename:forCreation:setExtension:
- _objc_msgSend$serializeFilename:forCreation:setExtension:inSharedAlias:
- _objc_msgSend$serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:
- _objc_msgSend$serializeVersion:diffs:deadInServerTruth:
- _objc_msgSend$setAliasToFileCount:
- _objc_msgSend$setAliasToFolderCount:
- _objc_msgSend$setAliasToPackageCount:
- _objc_msgSend$setAliasToSymlinkCount:
- _objc_msgSend$setAreMigratedFaultsBelowThreshold:
- _objc_msgSend$setAreNonFaultAllMigrated:
- _objc_msgSend$setBouncedDocumentsFoldersCount:
- _objc_msgSend$setBouncesInvestigation:
- _objc_msgSend$setCiconiaInvestigation:
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
- _objc_msgSend$setItemsChangedDuringCloning:
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
- _objc_msgSend$setUnderlyingErrorCode:
- _objc_msgSend$setUnderlyingErrorDescription:
- _objc_msgSend$setUnderlyingErrorDomain:
- _objc_msgSend$setUnexpectedCreations:
- _objc_msgSend$shouldIgnoreReportForOperationType:ofSubtype:forError:
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
- _packageItemsOrderedByPathForFileObjectIDFPFS
CStrings:
+ "\x01\x13\x12\x11\x1a"
+ "\x01\x1a"
+ "\x01&\x11\x18\x11#"
+ "\x04\x12"
+ "\x04\x1a\x11\x11\x16"
+ "\b\x11\"\x11\x1c\x13\x14\x1d\x12$"
+ "\x13\x13"
+ "   o %@ [appLib]"
+ "   o %@ [zone]"
+ " (SB)"
+ " base-valid{%@}"
+ " child-base-salt-validation{%@}"
+ " child-valid{%@}"
+ " ctvk{%@}"
+ " salt-st{%@}"
+ "%@%s"
+ "%@:%@;"
+ "%@::"
+ "+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:]"
+ "+[BRCDocumentSignatureCalculator _calculateSignatureForFileAtURL:error:]"
+ "+[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]"
+ "+[BRCDocumentSignatureCalculator _calculateSignatureForPackageAtURL:error:]_block_invoke"
+ "+[BRCDocumentSignatureCalculator calculateSignatureForURL:error:]"
+ "+[BRCItemID appLibraryRowIDFromRootOrDocumentsSQLiteValue:]"
+ "+[BRDSIDString(BRCPathAdditions) brc_dbAccountDSIDForPath:]"
+ "+[NSData(BRCCryptographicAdditions) brc_generateSaltingKey]"
+ ", upload_error = %@ "
+ "-[BRCAccountHandler initWithACAccountID:]"
+ "-[BRCAccountSessionFPFS _recoverAndReportDanglingLostZombieDirectories]"
+ "-[BRCAccountSessionFPFS _reportBasehashSalting]"
+ "-[BRCAccountSessionFPFS _reportBasehashSalting]_block_invoke"
+ "-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke_2"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) runDatabaseFixupsForDB:serverTruth:]_block_invoke"
+ "-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]"
+ "-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke"
+ "-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:]_block_invoke"
+ "-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke"
+ "-[BRCAccountSessionFPFS(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2"
+ "-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]"
+ "-[BRCAccountSessionFPFS(FPFSAdditions) _triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:]_block_invoke_2"
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
+ "-[BRCDaemonFPFS _dbgSleepIfRequested]"
+ "-[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildrenForce:]"
+ "-[BRCEventsAnalytics _sendDictionaryToCoreAnalytics:eventName:]"
+ "-[BRCFSImporter _deleteAppLibrary:documentsFolder:error:]"
+ "-[BRCFSImporter _deleteAppLibrary:documentsFolder:error:]_block_invoke"
+ "-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]"
+ "-[BRCFSImporter _shouldRejectItemDeleteDueToEtags:baseVersion:error:]"
+ "-[BRCFSImporter deleteItem:recursively:baseVersion:error:]"
+ "-[BRCFSImporter deleteItem:recursively:baseVersion:error:]_block_invoke"
+ "-[BRCFSImporter importNewItemAtURL:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:]"
+ "-[BRCFSUploader _cancelJobs:state:uploadError:]"
+ "-[BRCFSUploader _rescheduleJobsPendingScreenUnlock]"
+ "-[BRCFSUploader initWithAccountSession:]_block_invoke_6"
+ "-[BRCFSUploader setState:forUploadJobID:zone:uploadError:]"
+ "-[BRCImportObject(BRCPackageAdditions) initWithPackageURL:error:]"
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
+ "-[BRCPackageItem(FPFSAdditions) _initWithURL:inPackage:forItem:error:]"
+ "-[BRCPackageItem(FPFSAdditions) updateContentSignature:error:]"
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
+ "-[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step]"
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
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke_4"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded_step]"
+ "-[BRCSharingAcceptFlowOperation _openSharedSideFaultFile_step]"
+ "-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step]"
+ "-[BRCSharingAcceptFlowOperation _parseShareMetadata_step]"
+ "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument_step]"
+ "-[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]"
+ "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]"
+ "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _startShareAccept_step]"
+ "-[BRCSharingAcceptFlowOperation _startShareAccept_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]"
+ "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke_2"
+ "-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_3"
+ "-[BRCStageRegistry _garbageCollectUploadThumbnailsIncludingActiveUploads:]"
+ "-[BRCStageRegistry(FPFSAdditions) createStageURLForThumbnailFromItem:error:]"
+ "-[BRCStageRegistry(FPFSAdditions) createStageURLForThumbnailFromItem:error:]_block_invoke"
+ "-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]"
+ "-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:options:error:]_block_invoke"
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
+ "-[BRCUploadSyncUpRequestsManager finishRequestForIdentifer:finishError:error:]"
+ "-[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:]"
+ "-[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:]"
+ "-[BRCUploadSyncUpRequestsManager registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:]"
+ "-[BRCUserActionsNavigator openAppStoreForBundleID:]"
+ "-[BRCUserActionsNavigator openShareURLInWebBrowser:withReason:]"
+ "-[BRCVersion lazyXattrWithStageRegistry:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]"
+ "-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]"
+ "-[BRCXPCRegularIPCsClient setAdvancedDataProtectionEnabled:forContainer:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionForItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getSaltingVerificationKeysAtItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke"
+ "-[CKRecord(BRCItemAdditions) validateAdvancedDataProtectionFieldsWithSession:error:]"
+ "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:basehashSalt:parentIDIsCloudDocsRoot:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:basehashSalt:childBasehashSalt:]"
+ "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:basehashSalt:]"
+ "-[NSFileProviderManager(BRCAdditions) _br_signalEnumeratorForContainerItemIdentifier:retries:completionHandler:]_block_invoke"
+ "-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke_2"
+ "1.1"
+ "2\x14\x15\x11"
+ "4\"H\x12"
+ "<%@ count:%lu>"
+ "<%@ saltingState:'%@' basehashValidation: '%@' >"
+ "<%@: %p type:%@ %@ progress:%@>"
+ "<BRCSafeDBHolder %p>"
+ "@\"<BRCUserNavigationActions>\""
+ "@\"BRCBasehashSaltInfo\""
+ "@\"BRCThumbnailGenerationManager\""
+ "@\"NSCache\""
+ "@\"NSData\"16@?0@\"BRCLocalItem\"8"
+ "@\"NSMutableArray<NSFileProviderItem>\""
+ "@104@0:8@16@24Q32@40^Q48^B56@64@72^B80^Q88^@96"
+ "@24@?0@\"NSData\"8Q16"
+ "@24@?0@\"NSString\"8Q16"
+ "@36@0:8@16B24d28"
+ "@36@0:8@16i24^@28"
+ "@36@0:8@16s24@?28"
+ "@40@0:8#16@24^@32"
+ "@40@0:8q16q24@32"
+ "@44@0:8@16@24B32d36"
+ "@48@0:8@16q24@32@40"
+ "@48@0:8B16@20C28@?32@40"
+ "@48@0:8B16C20@24@?32@40"
+ "@88@0:8@16@24@32Q40Q48@56@64^Q72^@80"
+ "@96@0:8@16@24@32@40@48@56B64B68B72@76@84I92"
+ "ALTER TABLE app_libraries ADD COLUMN child_basehash_salt blob default null"
+ "ALTER TABLE app_libraries ADD COLUMN salting_state integer default 1"
+ "ALTER TABLE item_errors RENAME TO temp_item_errors"
+ "ALTER TABLE server_items ADD COLUMN basehash_salt_validation_key blob default null"
+ "ALTER TABLE server_items ADD COLUMN child_basehash_salt blob default null"
+ "ALTER TABLE server_items ADD COLUMN content_boundary_key blob"
+ "ALTER TABLE server_items ADD COLUMN salting_state integer default 1"
+ "Advanced Data Protection Not Enabled"
+ "AdvancedDataProtection"
+ "B56@0:8@16@24@32@40Q48"
+ "B56@0:8@16@24B32B36@40^@48"
+ "B56@0:8^@16^@24^@32@40^@48"
+ "B60@0:8@16s24@28@36@?44^@52"
+ "BRCAdvancedDataProtectionAdditions"
+ "BRCBaseHashSaltAdditions"
+ "BRCBasehashSaltInfo"
+ "BRCDeviceConfiguration"
+ "BRCDocumentSignatureCalculator"
+ "BRCEventsAnalytics"
+ "BRCFlatLevelEnumerator"
+ "BRCMiniCiconia"
+ "BRCRequestData"
+ "BRCSQLBackedSet"
+ "BRCSaltingBatchOperation"
+ "BRCScreenLockDelegate"
+ "BRCThumbnailGenerationManager"
+ "BRCUTITypeCache"
+ "BRCUploadSyncUpRequestsManager"
+ "BRCUserActionsNavigator"
+ "BRCUserNavigationActions"
+ "BRScreenLockObserver"
+ "CREATE INDEX \"client_items/fp_creation_item_identifier\" ON client_items (fp_creation_item_identifier) WHERE fp_creation_item_identifier IS NOT NULL"
+ "CREATE TABLE array_items (item %@ PRIMARY KEY)"
+ "CREATE TABLE completed_db_fixups ( fixup_version integer PRIMARY KEY )"
+ "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, service))"
+ "DANGLING_ZOMBIE_DIRECTORY_COUNT"
+ "DROP INDEX IF EXISTS \"ciconia_history/counting_index\""
+ "DROP INDEX IF EXISTS \"telemetry_events/priority\""
+ "DROP INDEX IF EXISTS \"telemetry_events/priority__rowid\""
+ "DROP TABLE IF EXISTS ciconia_history"
+ "DROP TABLE IF EXISTS telemetry_events"
+ "DROP TABLE temp_item_errors"
+ "Download for thumbnail only should be small file"
+ "EDS"
+ "ErrorCreatingItem"
+ "FPFS Migration Recovery Initiated"
+ "Got a nil account path"
+ "INSERT INTO completed_db_fixups (fixup_version) VALUES (%u)"
+ "INSERT INTO server_items ( item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_rank, item_origname, pcs_state, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, zone_rowid, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count, child_basehash_salt, salting_state, basehash_salt_validation_key) VALUES ( %@, %@, %ld, %@, NULL, %@, %d, %@, %d, %d, %d, %lld, %lld, %lld, %@, %@, %d, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %u, %@)"
+ "INSERT OR IGNORE INTO array_items (item) VALUES (%@)"
+ "INSERT OR REPLACE INTO app_libraries (rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state)  VALUES (%@, %@, %@, %@, %@, %@)"
+ "INSERT OR REPLACE INTO item_errors SELECT * FROM temp_item_errors"
+ "Library/CloudStorage/"
+ "ORDER BY item ASC"
+ "ORDER BY item DESC"
+ "ORDER BY rowid"
+ "Possible issue in QL, Thumbnail generation operation was running for too long"
+ "Request is already registered for %@"
+ "SELECT COUNT(*), child.item_id, child.zone_rowid FROM server_items AS child INNER JOIN server_items AS parent ON child.item_parent_id = parent.item_id AND child.zone_rowid = parent.zone_rowid WHERE IFNULL(child.basehash_salt_validation_key, 0) != IFNULL(validation_key(parent.child_basehash_salt), 0) AND LENGTH(child.item_filename) > 0 AND (parent.salting_state = 3 OR child.basehash_salt_validation_key IS NOT NULL)"
+ "SELECT COUNT(*), item_id, zone_rowid FROM server_items AS child WHERE item_id_is_app_library_root(child.item_parent_id) AND IFNULL(child.basehash_salt_validation_key, 0) != IFNULL(call_block(%p, child.item_parent_id), 0) AND LENGTH(child.item_filename) > 0 AND (call_block(%p, child.item_parent_id) = 3 OR child.basehash_salt_validation_key IS NOT NULL)"
+ "SELECT basehash_salt_validation_key, validation_key(child_basehash_salt), validation_key(content_boundary_key), salting_state FROM server_items WHERE item_id = %@ AND zone_rowid = %@"
+ "SELECT child_basehash_salt FROM server_items WHERE item_id = %@ AND zone_rowid = %@ LIMIT 1"
+ "SELECT ci1.rowid, ci1.zone_rowid, ci1.item_id, ci1.item_creator_id, ci1.item_sharing_options, ci1.item_side_car_ckinfo, ci1.item_parent_zone_rowid, ci1.item_localsyncupstate, ci1.item_local_diffs, ci1.item_notifs_rank, ci1.app_library_rowid, ci1.item_min_supported_os_rowid, ci1.item_user_visible, ci1.item_stat_ckinfo, ci1.item_state, ci1.item_type, ci1.item_mode, ci1.item_birthtime, ci1.item_lastusedtime, ci1.item_favoriterank,ci1.item_parent_id, ci1.item_filename, ci1.item_hidden_ext, ci1.item_finder_tags, ci1.item_xattr_signature, ci1.item_trash_put_back_path, ci1.item_trash_put_back_parent_id, ci1.item_alias_target, ci1.item_creator, ci1.item_processing_stamp, ci1.item_bouncedname, ci1.item_scope, ci1.item_local_change_count, ci1.item_old_version_identifier, ci1.fp_creation_item_identifier, ci1.version_name, ci1.version_ckinfo, ci1.version_mtime, ci1.version_size, ci1.version_thumb_size, ci1.version_thumb_signature, ci1.version_content_signature, ci1.version_xattr_signature, ci1.version_edited_since_shared, ci1.version_device, ci1.version_conflict_loser_etags, ci1.version_quarantine_info, ci1.version_uploaded_assets, ci1.version_upload_error, ci1.version_old_zone_item_id, ci1.version_old_zone_rowid, ci1.version_local_change_count, ci1.version_old_version_identifier, ci1.item_live_conflict_loser_etags, ci1.item_file_id, ci1.item_generation FROM client_items AS ci1                             LEFT JOIN client_items AS ci2                             ON ci2.version_old_zone_item_id = ci1.item_id AND ci2.version_old_zone_rowid = ci1.zone_rowid                             WHERE ci2.version_old_zone_rowid IS NULL                               AND ci2.version_old_zone_item_id IS NULL                               AND ci1.item_state = -3                               AND ci1.item_type IN (0, 9, 10)"
+ "SELECT content_boundary_key FROM server_items WHERE item_id = %@ AND zone_rowid = %@"
+ "SELECT csu.throttle_id, csu.last_try_stamp, li.zone_rowid FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
+ "SELECT date FROM boot_history ORDER BY rowid DESC LIMIT 1"
+ "SELECT item FROM array_items %@"
+ "SELECT item_origname, item_filename FROM server_items  WHERE item_id = %@ AND item_parent_id = %@ AND +zone_rowid = %@"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_state = 1    AND li.item_localsyncupstate = 4    AND NOT EXISTS(SELECT 1 FROM client_items AS ci                     WHERE li.item_id = ci.item_parent_id                      AND ci.zone_rowid = su.zone_rowid)    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (1, 2, 8, 5, 6, 7, 3)    AND li.item_state = 0    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su  ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (0, 9, 10, 4)    AND (li.item_state = 0)    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL ORDER BY su.retry_count ASC"
+ "SELECT max(fixup_version) + 1 FROM completed_db_fixups"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries WHERE zone_rowid = %@"
+ "SELECT salting_state FROM server_items WHERE item_id = %@ AND zone_rowid = %@ LIMIT 1"
+ "SELECT si.zone_rowid, si.item_rank, si.item_origname, si.pcs_state, si.item_id, si.item_creator_id, si.item_sharing_options, si.item_side_car_ckinfo, si.item_stat_ckinfo, si.item_state, si.item_type, si.item_mode, si.item_birthtime, si.item_lastusedtime, si.item_favoriterank,si.item_parent_id, si.item_filename, si.item_hidden_ext, si.item_finder_tags, si.item_xattr_signature, si.item_trash_put_back_path, si.item_trash_put_back_parent_id, si.item_alias_target, si.item_creator, si.version_name, si.version_ckinfo, si.version_mtime, si.version_size, si.version_thumb_size, si.version_thumb_signature, si.version_content_signature, si.version_xattr_signature, si.version_edited_since_shared, si.version_device, si.version_conflict_loser_etags, si.version_quarantine_info, si.child_basehash_salt, si.salting_state, si.basehash_salt_validation_key, si.quota_used, si.recursive_child_count, si.shared_children_count, si.shared_alias_count, si.child_count, ci.item_id FROM server_items AS si LEFT JOIN client_items AS ci ON si.item_id = ci.item_id AND si.zone_rowid = ci.zone_rowid WHERE si.item_alias_target = %@ AND si.item_type = 3 AND si.item_state = 0 AND (ci.item_id IS NULL OR ci.item_state != 1) %@ ORDER BY si.item_id"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_filename = %@ AND item_type = 3 AND zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_id = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_id = %@ AND zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND basehash_salt_validation_key IS NULL and zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND item_filename = %@ AND +zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND zone_rowid = %@ AND item_filename != '.Trash' AND pcs_state NOT IN (2, 3) LIMIT 1"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_rank = %lld AND zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE rowid = %lld"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE zone_rowid = %@"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE zone_rowid = %@ AND call_block(%@, rowid)"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count, rowid      FROM server_items    WHERE zone_rowid = %@ AND item_parent_id = %@ ORDER BY item_filename"
+ "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, child_basehash_salt, salting_state, basehash_salt_validation_key, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count, rowid , validation_key(content_boundary_key)     FROM server_items    WHERE zone_rowid = %@ AND item_parent_id = %@"
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
+ "T@?,R,N,V_finishBlock"
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
+ "Ts,R,N,V_requestType"
+ "UPDATE app_libraries SET app_library_plist = %@, zone_rowid = %@, child_basehash_salt = %@, salting_state = %@ WHERE rowid = %@"
+ "UPDATE app_libraries SET child_basehash_salt = %@,  salting_state = %@ WHERE rowid = %@ "
+ "UPDATE app_libraries SET child_basehash_salt = validation_key(child_basehash_salt)"
+ "UPDATE client_items SET fp_creation_item_identifier = NULL WHERE fp_creation_item_identifier IS NOT NULL"
+ "UPDATE client_items SET item_notifs_rank = bump_notifs_rank_and_trigger_notifs(rowid) WHERE item_type = 5"
+ "UPDATE client_items SET version_upload_error = NULL WHERE rowid IN (SELECT throttle_id FROM client_uploads WHERE throttle_state = 35)"
+ "UPDATE client_uploads    SET throttle_state = %d, %@ transfer_operation = NULL  WHERE %@"
+ "UPDATE client_uploads SET  throttle_state = %d, transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL%@ WHERE throttle_id = %@"
+ "UPDATE client_uploads SET throttle_state = 1, next_retry_stamp = 0  WHERE throttle_id IN (SELECT cu.throttle_id from client_uploads AS cu LEFT JOIN client_items AS ci                       ON cu.throttle_id = ci.rowid                        WHERE cu.throttle_state = 33                         AND call_block(%p, ci.version_upload_error))"
+ "UPDATE client_uploads SET throttle_state = 1, upload_error = NULL WHERE throttle_state = 35"
+ "UPDATE server_items    SET item_rank = NULL, item_depth = 0, item_sharing_options = (%lu | (item_sharing_options & %lu)),         content_boundary_key = %@, version_name = %@, version_ckinfo = %@, version_mtime = %lld, version_size = %lld, version_thumb_size = %lld, version_thumb_signature = %@, version_content_signature = %@, version_xattr_signature = %@, version_edited_since_shared = %@, version_device = %@, version_conflict_loser_etags = %@, version_quarantine_info = %@  WHERE item_id = %@ AND zone_rowid = %@"
+ "UPDATE server_items SET   item_rank = NULL, item_depth = 0, item_origname = %@, pcs_state = %d, item_sharing_options = (%lu | (item_sharing_options & %lu)), item_side_car_ckinfo = %@, item_stat_ckinfo = %@, item_state = %d, item_type = %d, item_mode = %d, item_birthtime = %lld, item_lastusedtime = %lld, item_favoriterank = %lld, item_parent_id = %@, item_filename = %@, item_hidden_ext = %d, item_finder_tags = %@, item_xattr_signature = %@, item_trash_put_back_path = %@, item_trash_put_back_parent_id = %@, item_alias_target = %@, item_creator = %@, quota_used = %@, recursive_child_count = %@, shared_children_count = %@, shared_alias_count = %@, child_count = %@, child_basehash_salt = %@, salting_state = %u, basehash_salt_validation_key = %@ WHERE item_id = %@ AND zone_rowid = %@"
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
+ "[CRIT] Assertion failed: rs.next%@"
+ "[CRIT] Assertion failed: salt != nil%@"
+ "[CRIT] Assertion failed: self.isPrivateZone%@"
+ "[CRIT] Assertion failed: si != nil%@"
+ "[CRIT] Assertion failed: zombieItem.isDirectory%@"
+ "[CRIT] UNREACHABLE: %@ is not in mmcsV2 when it should be%@"
+ "[CRIT] UNREACHABLE: %@ is not rounded the correct amount%@"
+ "[CRIT] UNREACHABLE: Attempt to download %@ which is uploading%@"
+ "[CRIT] UNREACHABLE: Can't compute padded file size%@"
+ "[CRIT] UNREACHABLE: Failed to adopt persona for _br_signalEnumeratorForContainerItemIdentifier retry%@"
+ "[CRIT] UNREACHABLE: Recieved an invalid request type%@"
+ "[CRIT] UNREACHABLE: Rounding amount should be at least 1 minute%@"
+ "[CRIT] UNREACHABLE: Unable to remove thumbnail temporary file: %@ error %@%@"
+ "[CRIT] UNREACHABLE: can't initialize document with invalid library rowid %@%@"
+ "[CRIT] UNREACHABLE: can't initialize library root with invalid library rowid %@%@"
+ "[CRIT] UNREACHABLE: can't initialize shared zone root with invalid zone rowid %@%@"
+ "[DEBUG] %@ - Database closed%@"
+ "[DEBUG] <BRCSafeDBHolder %p> - Creating for db in path: %@%@"
+ "[DEBUG] <BRCSafeDBHolder %p> - dealloc called%@"
+ "[DEBUG] Application proxy: %@, proxy.bundleURL = %@%@"
+ "[DEBUG] Apply Changes: Deleted %llu non-rejection jobs%@"
+ "[DEBUG] Calling finish block for %@ with %@%@"
+ "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
+ "[DEBUG] Creating sync task%@"
+ "[DEBUG] Dedicating this sync up operation to %@ %@%@"
+ "[DEBUG] Deleting old sync up job%@"
+ "[DEBUG] Didn't find any FPFS domain to remove for persona = %@%@"
+ "[DEBUG] Done Force Ingestion AppLibrary %@ to update the contentPolicy%@"
+ "[DEBUG] Finished metadata salting a batch for item %@ when completed: %d error: %@%@"
+ "[DEBUG] Finishing all requests under zone %@%@"
+ "[DEBUG] Found %u items with inconsistent basehash salting%@"
+ "[DEBUG] Found cached child basehash salt %@ for parent %@%@"
+ "[DEBUG] Found child basehash salt %@ from database for %@%@"
+ "[DEBUG] Found old domain %@, dropping%@"
+ "[DEBUG] Generated child basehash salt %@ for %@%@"
+ "[DEBUG] Generated root child basehash salt %@ for %@%@"
+ "[DEBUG] Generating thumbnail for ID %@ (shouldTransferThumbnail:yes) %@%@"
+ "[DEBUG] Got unexpected exception %@. rethrow%@"
+ "[DEBUG] Invalidating UTI cache%@"
+ "[DEBUG] Invalidating state of client = %@%@"
+ "[DEBUG] Keeping bounce of %@ even though it clashes with %@%@"
+ "[DEBUG] Learning new child basehash salt %@ from %@ for %@%@"
+ "[DEBUG] Learning salt state %@ from %@ for %@%@"
+ "[DEBUG] Looking for old Ciconia domains%@"
+ "[DEBUG] Moving salting root record ID %@ from %@ to %@%@"
+ "[DEBUG] Opening db at: %@%@"
+ "[DEBUG] Postponing sync up for item %@%@"
+ "[DEBUG] Registered request %@ for identifier %@%@"
+ "[DEBUG] Removing FP domain on disk: %@%@"
+ "[DEBUG] Removing work directory%@"
+ "[DEBUG] Retry removing work directory%@"
+ "[DEBUG] Running in sync bubble. Ignoring app list did change event%@"
+ "[DEBUG] Running in sync bubble. Should not try to create the group container download stage folder%@"
+ "[DEBUG] Salting batch operation is not allowed on %@%@"
+ "[DEBUG] Scheduling sync down for zone %@%@"
+ "[DEBUG] Screen no longer locked. Try upload item: %@%@"
+ "[DEBUG] Seems that item %@ has started a czm after requesting a download%@"
+ "[DEBUG] Start date expired: %@ (%f)%@"
+ "[DEBUG] Sync: Dedicating sync op to metadata salting %@%@"
+ "[DEBUG] Target application seems missing%@"
+ "[DEBUG] The accept share op [%@] failed --> return with failure%@"
+ "[DEBUG] Thumbnail manager: below maximum allowed number of thumbnails retrieval (%ld)%@"
+ "[DEBUG] Thumbnail manager: reached maximum allowed number of thumbnails retrieval (%ld)%@"
+ "[DEBUG] Uploader: scheduling %lld upload jobs that where in permenant failure state%@"
+ "[DEBUG] We shouldn't re-upload in case of structure records failures%@"
+ "[DEBUG] Will remove domain: %@%@"
+ "[DEBUG] _garbageCollectUploadThumbnailsIncludingActiveUploads: [%s]%@"
+ "[DEBUG] basename is nil -> replace with empty string%@"
+ "[DEBUG] dropping item which was deleted %@ with notif rank %llu%@"
+ "[DEBUG] failing on CKErrorAssetNotAvailable/CKUnderlyingErrorMMCSItemNotAvailable when screen is locked --> Suspending for data protection class%@"
+ "[DEBUG] item with id [%@] still don't exist after sync down --> return with failure%@"
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
+ "[ERROR] %@ - Failed calculating content signature at '%@'. Error: %@%@"
+ "[ERROR] %@ - Failed opening contents at '%@'. Error: %@%@"
+ "[ERROR] Auto rollback handler called - %@ (%@)%@"
+ "[ERROR] Can't generate salting key %{errno}d%@"
+ "[ERROR] Could not create stage URL for thumbnail for %@%@"
+ "[ERROR] Couldn't add item for checksumming at %@%@"
+ "[ERROR] Download for thumbnail only was asked, but the file is not small.%@"
+ "[ERROR] Error: %lld%@"
+ "[ERROR] FPFS Migration recovery failed: %@%@"
+ "[ERROR] Failed creating root folder for DB: %@. %@%@"
+ "[ERROR] Failed removing domain %{errno}d%@"
+ "[ERROR] Got error reading the account DSID from '%@': %@%@"
+ "[ERROR] Operation %@ is missing syncContext%@"
+ "[ERROR] Stage directory path for live items does not exist!%@"
+ "[ERROR] Unable to create temp file for thumbnail creation stage url for item %@ with error %@%@"
+ "[ERROR] Unable to move thumbnail file %@ to %@ with error %@%@"
+ "[ERROR] Zone %@ has items which need sync. Clearing app sync blocked%@"
+ "[ERROR] _registerStaticDBFunctions failed with %@%@"
+ "[ERROR] cancelling operation since reached to maximal allowed backoff%@"
+ "[ERROR] db corruption handler called: %@%@"
+ "[ERROR] db fixup %d failed %@%@"
+ "[ERROR] failed opening connection: %@%@"
+ "[ERROR] failed registering completion of db fixup %d with error %@%@"
+ "[ERROR] failed sending salted records - %@%@"
+ "[ERROR] passed nil app bundle ID%@"
+ "[ERROR] sqlite error handler called - %@ (%@)%@"
+ "[INFO] %@: reply(%@, %@, %@, %d, %@)%@"
+ "[NOTICE] %@ - shared iPad: needs to sync items in the sync bubble (sz:%llu)%@"
+ "[NOTICE] Days import is stuck (%lld) are less then threshold%@"
+ "[NOTICE] Days since import started (%lld) are less then threshold%@"
+ "[NOTICE] Days since last boot history (%ld) are less then threshold%@"
+ "[NOTICE] Got %@ while opening account. Exiting without an error%@"
+ "[NOTICE] Got nil content URL and the item is not a symbolic link. Ignoring the content change field%@"
+ "[NOTICE] Recovered %lld symbolic links%@"
+ "[NOTICE] Recovering symbolic links%@"
+ "[NOTICE] Running db fixup %d for %s db%@"
+ "[NOTIF] document %@ didCompleteDownloadEtagIfLoser %@ withError %@ -- notifying trackers%@"
+ "[WARNING] %@ - We already have a bubble sync task %@%@"
+ "[WARNING] %d: enumerating domains failed: %@%@"
+ "[WARNING] %d: removeDomain:%@ failed: %@%@"
+ "[WARNING] %d: removeDomain:%@ timed out%@"
+ "[WARNING] Adding advanced data protection bit because it's forced on %@%@"
+ "[WARNING] Failed to remove old domain %@: %@%@"
+ "[WARNING] Found %d items parented to root with basehash salting issues example itemID %@ zone %@%@"
+ "[WARNING] Found %d items with basehash salting issues example itemID %@%@"
+ "[WARNING] Item %@ is undergoing CZM so returning back with busy error%@"
+ "[WARNING] Item %@ is undergoing zone reset so returning back with busy error%@"
+ "[WARNING] Migration progress is stuck for %lld days, invoking recovery flow...%@"
+ "[WARNING] Recovery was already invoked once, ignoring%@"
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
+ "_calculateSignatureForFileAtURL:error:"
+ "_calculateSignatureForPackageAtURL:error:"
+ "_callFinishBlockOnDataRequest:finishError:"
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
+ "_createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:options:reply:"
+ "_createRecoveryExecutedErrorForImportError:"
+ "_createSchemaForSQLType:error:"
+ "_createSideFaultOnDisk_step"
+ "_createStructureRecordForRootItem"
+ "_createStructureRecordForServerItem:salt:"
+ "_createStructureRecordWithRecordID:itemID:basehashSalt:statInfo:"
+ "_databaseRootDirectory"
+ "_daysSinceLastMigrationProgress:itemsNotMigrated:reconciledItems:"
+ "_dbBecameCorrupted"
+ "_dbRootFolder"
+ "_dbgSleepIfRequested"
+ "_deleteAppLibrary:documentsFolder:error:"
+ "_endAcceptationFlow_step"
+ "_extensionID"
+ "_fetchManagersDictionary"
+ "_finishShareAccept_step"
+ "_fixupAdvancedDataProtectionState"
+ "_fsRemoveWorkDirectory:"
+ "_garbageCollectUploadThumbnailsIncludingActiveUploads:"
+ "_generateSaltGetterBlock"
+ "_generateThumbnailOperationAtURL:targetURL:"
+ "_getChildBasehashSaltForItem:"
+ "_getLaunchServicesDatabaseGeneration"
+ "_getRequestTypeDescription"
+ "_getSaltForItem:"
+ "_getWorkloop"
+ "_hasActiveUploadWithStageID:"
+ "_hasThumbnailAvailableSlot"
+ "_initScreenLockManager"
+ "_initWithPersonaIdentifier:"
+ "_initWithURL:inPackage:forItem:error:"
+ "_initWithVersionIdentifier:size:oldVersionIdentifier:contentSignature:"
+ "_invalidateCahceIfNeeded"
+ "_invalidateRequestsTableWithNewSource:"
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
+ "_latestSourceIdentifier"
+ "_locateMatchingItemForTemplateItem:parentItem:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:"
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
+ "_personaIdentifer"
+ "_populateUUID:"
+ "_prepareToDownloadSharedDocument_step"
+ "_processSaltingOnAppLibrary:"
+ "_reachedThumbnailMaximumCapacity"
+ "_recoverAndReportDanglingLostZombieDirectories"
+ "_recoverItemIDChangedWhileUploadingIfNecessary:"
+ "_refreshLatestRevisionForItemIdentifier:reply:"
+ "_registerLastBootIfNeeded:table:skipControlFiles:deviceIDChanged:"
+ "_registerOperation:throttler:"
+ "_registerStaticDBFunctionsWithError:"
+ "_removeDiagnosticsDirectoryAtURL:withError:"
+ "_removeFPDomain:error:"
+ "_removeThumbnailOperationForThumbnailID:"
+ "_removeWorkDirectory:"
+ "_reportBasehashSalting"
+ "_reportForFPFSImportStatusTelemetryEventIfNeeded:completionHandler:"
+ "_requestType"
+ "_requestsByItemGlobalID"
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
+ "_shouldRejectItemDeleteDueToEtags:baseVersion:error:"
+ "_shouldTriggerTapToRadar:daysSinceLastMigrationProgress:"
+ "_showSharingJoinDialog_step"
+ "_signalPropagationToChildrenForce:"
+ "_startShareAccept_step"
+ "_syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:throttledItemInBatch:"
+ "_telemetrySchema"
+ "_throttledItemInBatch"
+ "_thumbnailGenerationManager"
+ "_thumbnailPrivateQueue"
+ "_timedOut"
+ "_timeout"
+ "_triggerMigrationStuckRecoveryIfNeededDaysSinceImportStarted:daysSinceLastMigrationProgress:importError:"
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
+ "_zoneIDToItemIDs"
+ "addObject:error:"
+ "addScreenLockObserver:"
+ "addThumbnailGenerationJobAtURL:targetURL:thumbnailID:syncContext:completionHandler:"
+ "advanced-data-protection"
+ "advanced-data-protection.basehash-salting.batch-size"
+ "advancedDataProtectionBasehashSaltingBatchSize"
+ "advancedDataProtectionEnabled"
+ "advancedDataProtectionForced"
+ "advancedDataProtectionSupported"
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
+ "br_fixup_symbolic_links"
+ "br_isCKErrorCode:underlyingErrorCode:"
+ "br_isInSyncBubble"
+ "br_prettyDescription"
+ "br_shouldOverwriteExistingName"
+ "br_signalEnumeratorForContainerItemIdentifier:completionHandler:"
+ "brc_errorAcceptShareFailedForItem:"
+ "brc_fillWithChildBasehashSalt:"
+ "brc_generateSaltingKey"
+ "brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors"
+ "brc_isCloudKitErrorDataProtectionClass"
+ "brc_isCloudKitRequestRejectedError"
+ "brc_isFrontBoardOpenApplicationRequestDenied"
+ "brc_truncatedSHA256"
+ "calculateSignatureForURL:error:"
+ "cancelRequestForIdentifier:error:"
+ "childBaseSaltForItemID:"
+ "childBasehashSalt"
+ "childBasehashSaltValidationKey"
+ "cleanupCiconiaAtURL:diagnosticsURL:completionHandler:"
+ "clearTempDatabases"
+ "cloneLatestContentRevisionForItemIdentifier:reply:"
+ "closeDatabaseSynchronously:dispatchToSerialQueue:completionHandler:"
+ "closeFD:"
+ "com.apple.CloudDocs.debug.sleepOnStartDuration"
+ "com.apple.CloudDocs.debug.sleepOnStartInitialDate"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.bird.thumbnails.private"
+ "com.apple.iCloudDriveCore.telemetry-disk-checker"
+ "contentBoundaryKeyForItemID:"
+ "contentPolicyForZoneRoot:optimizeStorage:isAppInstalled:isWallet:isGreedyDocument:"
+ "createSetOfClass:withSQLType:error:"
+ "createStageURLForThumbnailFromItem:error:"
+ "createStageURLFromLiveURLForItem:options:error:"
+ "createStringsSetWithError:"
+ "data-protection-class"
+ "dataWithLength:"
+ "dataWithSQL:"
+ "db.integrity-check.basehash-salting"
+ "db.integrity-check.lost-zombie-directories"
+ "dbIntegrityCheckBasehashSalting"
+ "dbIntegrityCheckLostZombieDirectories"
+ "debugItemIDStringWithVerbose:"
+ "defaultCache"
+ "defaultManagerWithPersonaIdentifier:"
+ "defaultNavigator"
+ "delete"
+ "deleteItem:recursively:baseVersion:error:"
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
+ "finishRequestForIdentifer:finishError:error:"
+ "finishRequestForItemsInZoneRowID:finishError:"
+ "forceSignalPropagationToChildren"
+ "fpfs modifications tracked requests"
+ "fpfs.migration.stuck-migration-recovery-days-since-import-started-threshold"
+ "fpfs.migration.stuck-migration-recovery-days-since-upgrade-threshold"
+ "fpfs.migration.stuck-migration-recovery-days-without-progress-threshold"
+ "fpfs.migration.stuck-migration-take-reconciled-items-into-account"
+ "fpfsStuckMigrationRecoveryDaysSinceImportStartedThreshold"
+ "fpfsStuckMigrationRecoveryDaysSinceUpgradeThreshold"
+ "fpfsStuckMigrationRecoveryDaysWithoutProgressThreshold"
+ "fpfsStuckMigrationTakeReconciledItemsIntoAccount"
+ "fpfsUploadV2"
+ "fully salted"
+ "generateSmallItemThumbnailForFileObject:reply:"
+ "getConfiguration"
+ "getDomainsForProviderIdentifier:completionHandler:"
+ "getKnowledgeUUID:andSequenceNumber:"
+ "getOrGenerateChildBasehashSaltingKey"
+ "getProgressForIdentifier:"
+ "getSaltingVerificationKeysAtItemIdentifier:reply:"
+ "hasMigrationUUID"
+ "hasThumbnailAvailableSlot"
+ "importNewItemAtURL:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:"
+ "initArrayOfClass:withSQLType:error:"
+ "initWithBasehashSaltInfo:"
+ "initWithBatchSize:"
+ "initWithItemID:clientZone:"
+ "initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:childBasehashSalt:saltingState:"
+ "initWithPackageURL:error:"
+ "initWithProgress:requestType:finishBlock:"
+ "initWithRecordID:serverZone:isUserWaiting:maxBackoff:"
+ "initWithRootItem:"
+ "initWithShareMetadata:client:session:userNotifier:userActionsNavigator:"
+ "integerForKey:"
+ "invalid"
+ "invalidateRequestsOfClient:"
+ "isAppLibraryRootItemIDWithSQLiteValue:"
+ "isInternalBuild"
+ "isRunningOnMacOS"
+ "isSeedBuild"
+ "isSharedIPad"
+ "isSyncBubbleClientEntitled"
+ "item is not a document"
+ "itemGlobalID = %@, requestData = %@"
+ "itemNeedingBasehashSalting"
+ "itemVersion"
+ "item_id_is_app_library_root"
+ "kBRCFPFSMigrationRecoveryWasInvokedAtKey"
+ "lastBootHistoryTime"
+ "lazyXattrWithStageRegistry:"
+ "locate-records-throttle"
+ "locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:"
+ "locateRecordsThrottleParams"
+ "lost(z)"
+ "maxBackoff"
+ "metadata-salting/"
+ "metadataCompletionBlock"
+ "modify"
+ "newAppLibraryFromPQLResultSet:version:error:"
+ "newBasehashSaltingProblemCountWithProblemCount:mangledID:itemIDString:"
+ "newDanglingZombieProblemCountWithProblemCount:"
+ "newEnumeratorForItemID:clientZone:"
+ "newIntEvent:UUID:value:"
+ "newItemForSignatureCalculationWithURL:inPackage:error:"
+ "newLongEvent:UUID:value:"
+ "newLongEvent:UUID:value:round:"
+ "no server item"
+ "open:flags:"
+ "openAppStoreForBundleID:"
+ "openShareURLInWebBrowser:withReason:"
+ "openiCloudSettings"
+ "operationForThumbnailID:"
+ "paddedFileSize"
+ "partially salted"
+ "pcs chaining"
+ "providerDomainWithID:cachePolicy:error:"
+ "q36@0:8B16B20B24B28B32"
+ "q40@0:8q16q24q32"
+ "reachedThumbnailMaximumCapacity"
+ "refresh-revision-max-backoff"
+ "refreshRevisionMaxBackoff"
+ "registerAndSendNewApplyFailureWithOutcome:"
+ "registerAndSendNewContainerResetWithOutcome:"
+ "registerAndSendNewFolderSharePCSChainingTime:chainedRecordsCount:zoneMangledID:itemIDString:error:analyticsReporter:"
+ "registerAndSendNewPeriodicSyncWithOutcome:"
+ "registerAndSendNewShareAcceptationWithLastStep:zoneMangledID:itemIDString:error:analyticsReporter:"
+ "registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:"
+ "removeDomain:forProviderIdentifier:completionHandler:"
+ "removeScreenLockObserver:"
+ "requestType"
+ "retriableCKInteralErrorCodesForRejectedRequestedError"
+ "rootChildBasehashSalt"
+ "rootRecordCreated"
+ "rounding amount"
+ "runDatabaseFixups"
+ "runDatabaseFixupsForDB:serverTruth:"
+ "s16@0:8"
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
+ "sharedConnectionProxy"
+ "sharedScreenLockMonitor"
+ "shouldUseAdvancedDataProtection"
+ "showJoinDialogForShareMetadata:ckContainer:reply:"
+ "signalPropagationToChildren"
+ "signatureWithFileDescriptor:error:"
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
+ "there is no request for %@"
+ "throttledItemInBatch"
+ "thumbnail generation encountered an error"
+ "thumbnail-%@"
+ "thumbnail-generation-operation-timeout"
+ "thumbnailGenerationManager"
+ "thumbnailGenerationOperationTimeout"
+ "timedOut"
+ "timeout"
+ "timestampRoundingAmount"
+ "tracked requests of client (%lu) : (%lu):"
+ "transferOptionsWithBoundaryKey:"
+ "treatPerItemThrottleAsOperationSuccess"
+ "unsalted"
+ "updateContentSignature:error:"
+ "upload_error = %@, "
+ "useMMCSEncryptionV2"
+ "v16@?0@\"BRCContainerScheduler\"8"
+ "v16@?0@\"BRCFPImportReport\"8"
+ "v24@0:8@\"NSString\"16"
+ "v24@?0@\"BRCServerItem\"8@\"NSError\"16"
+ "v28@0:8I16@?20"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8B16B20@?24"
+ "v32@?0@\"BRCItemGlobalID\"8@\"BRCRequestData\"16^B24"
+ "v32@?0@\"BRQueryItem\"8Q16@\"NSError\"24"
+ "v32@?0@\"NSData\"8@\"NSFileProviderItemVersion\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@\"CKShareMetadata\"16@\"CKContainer\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16B24@28B36"
+ "v44@0:8@16@24B32^B36"
+ "v44@0:8@16B24B28@32B40"
+ "v44@0:8@16Q24B32@36"
+ "v44@0:8i16@20@28@36"
+ "v48@0:8@16@24@32B40B44"
+ "v48@0:8@16B24B28B32@36B44"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32B40B44@?48"
+ "v64@0:8@16Q24@32B40C44@48@56"
+ "v64@0:8d16@24@32@40@48@56"
+ "v72@0:8@16@24@32@40@48Q56@?64"
+ "validateAdvancedDataProtectionFieldsWithSession:error:"
+ "validationKeyTruncationLength"
+ "validation_key"
+ "verbose"
+ "waitForStabilizationWithReply:"
+ "waitForUploadsToCompleteInSyncBubbleWithReply:"
+ "whitespaceAndNewlineCharacterSet"
- "\x01\x12\x12\x11\x1a"
- "\x01\x19\x12\x12"
- "\x01'\x18\x11#"
- "\x03\x1a\x11\x11\x16"
- "\x06\x11"
- "\b\x11\"\x11\x1c\x12\x14\x1d\x12$"
- "\n======================================\n\n"
- "   o %@ [container]"
- "  [%@] OS:%@ CloudDocs:%@ BirdSchema:%@ DBSchema:%@ CiconiaVersion:%@ Duration:%@ UUID:%@ LastOriginatorID:%@ LastError:%@"
- "%*s%@"
- "%@: %@\n"
- "%llu"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:]"
- "+[BRCAccountSessionFPFS(BRCDatabaseManager) _registerStaticDBFunctions:error:]_block_invoke_5"
- "+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]"
- "+[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke"
- "+[BRCAutoBugCaptureReporter shouldIgnoreReportForOperationType:ofSubtype:forError:]"
- "+[BRCSharingAcceptFlowOperation _openAppStoreForShareURL:]"
- "+[BRCSharingAcceptFlowOperation _openShareURLInWebBrowser:withReason:]"
- ",last_originator"
- "-[BRCAccountSessionFPFS(BRCDatabaseManager) saveMigrationAttemptForReport:uuid:]_block_invoke"
- "-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]"
- "-[BRCAccountSessionFPFS(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:tracker:error:]_block_invoke"
- "-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]"
- "-[BRCAccountSessionFPFS(FPFSAdditions) _postImportAnalysisForProviderDomainID:withLostItemCount:withMigrationID:]_block_invoke"
- "-[BRCAccountSessionFPFS(FPFSAdditions) _reportForFPFSImportStatusTelemetryEventIfNeeded:]_block_invoke"
- "-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]"
- "-[BRCAccountSessionFPFS(FPFSAdditions) _triggerFPCKForProviderDomainID:completionHandler:]_block_invoke"
- "-[BRCAnalyticsReporter _fetchTelemetryEventCountOrAdd:]"
- "-[BRCAnalyticsReporter _prepareSyncTelemetryEventsToSend]"
- "-[BRCAnalyticsReporter dropAllSyncTelemetryEvents]_block_invoke"
- "-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]"
- "-[BRCAnalyticsReporter forceTelemetryDequeueWithCompletionHandler:]_block_invoke"
- "-[BRCAnalyticsReporter postReportForDefaultSubCategoryWithCategory:telemetryTimeEvent:]"
- "-[BRCAnalyticsReporter submitSyncTelemetryEvent:]_block_invoke"
- "-[BRCAnalyticsReporter updateCurrentTelemetryToken:]"
- "-[BRCAppLibrary initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:]"
- "-[BRCClientZone _registerServerStitchingOperation:]"
- "-[BRCClientZone _syncUpOfRecords:createdAppLibraryNames:didFinishWithError:errorWasOnPCSChainedItem:]"
- "-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:]"
- "-[BRCDatabaseBackupStorage setUpDatabaseWithError:]"
- "-[BRCDirectoryItem(FPFSAdditions) _signalPropagationToChildren]"
- "-[BRCDownloadContent initWithDocument:stageID:etagIfLoser:]"
- "-[BRCFSImporter _locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:]"
- "-[BRCFSImporter _updateCiconiaDatabaseForBouncing:existingItem:]"
- "-[BRCFSImporter importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:]"
- "-[BRCFSUploader _cancelJobs:state:]"
- "-[BRCFSUploader _computeRecordForJobID:item:syncContext:]_block_invoke"
- "-[BRCFSUploader _doneFetchingThumbnailForJobID:]"
- "-[BRCFSUploader _startFetchThumbnail:jobID:]"
- "-[BRCFSUploader initWithAccountSession:]_block_invoke_3"
- "-[BRCFSUploader setState:forUploadJobID:zone:]"
- "-[BRCImportObject(BRCPackageAdditions) initWithURL:packageRoot:error:]"
- "-[BRCItemID debugItemIDString]"
- "-[BRCLocalItem(BRCSharedToMeTopLevel) structureRecordBeingDeadInServerTruth:shouldPCSChainStatus:inZone:]"
- "-[BRCLocalItem(CKConversions) structureRecordBeingDeadInServerTruth:stageID:shouldPCSChainStatus:]"
- "-[BRCLocateRecordOperation initWithRecordID:serverZone:isUserWaiting:]"
- "-[BRCPackageItem(FPFSAdditions) initWithURL:inPackage:forItem:error:]"
- "-[BRCPendingChangesStream destroyDatabase]_block_invoke"
- "-[BRCSafeDBHolder asyncCloseWithCompletionHandler:]_block_invoke"
- "-[BRCServerZone _saveItemID:version:record:iWorkSharingOptions:]"
- "-[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion]"
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
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner]_block_invoke_4"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _openSharedItemIfStillNeeded]"
- "-[BRCSharingAcceptFlowOperation _openSharedSideFaultFile]"
- "-[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively]"
- "-[BRCSharingAcceptFlowOperation _parseShareMetadata]"
- "-[BRCSharingAcceptFlowOperation _prepareToDownloadSharedDocument]"
- "-[BRCSharingAcceptFlowOperation _setSpotlightAttribute]"
- "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]"
- "-[BRCSharingAcceptFlowOperation _showSharingJoinDialog]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _startShareAccept]"
- "-[BRCSharingAcceptFlowOperation _startShareAccept]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient]_block_invoke"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner]_block_invoke_2"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]"
- "-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient]_block_invoke_2"
- "-[BRCSharingCopyParticipantTokenOperation main]_block_invoke_2"
- "-[BRCStageRegistry setStageDirectoryForXattr:]"
- "-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]"
- "-[BRCStageRegistry(FPFSAdditions) createStageURLFromLiveURLForItem:error:]_block_invoke"
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
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) fetchLatestContentRevisionForItemIdentifier:reply:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:options:etagIfLoser:reply:]_block_invoke_2"
- "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:clientZone:error:]"
- "-[CKRecord(BRCSerializationAdditions) serializeFilename:forCreation:setExtension:inSharedAlias:]"
- "-[CKRecord(BRCSerializationAdditions) serializeStatInfo:diffs:stageID:deadInServerTruth:shouldPCSChainStatus:]"
- "-[CKRecord(BRCSerializationAdditions) serializeVersion:diffs:deadInServerTruth:]"
- "-[_BRCOperation _setTelemetryHeaderOnCKOpIfNecessary:]"
- "-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]"
- "2\x14\x15"
- "4\"8\x11"
- "<"
- "="
- "@\"AppTelemetryCiconiaBouncesInvestigation\""
- "@\"AppTelemetryCiconiaEAccessInvestigation\""
- "@\"AppTelemetryCiconiaInvestigation\""
- "@\"NSMutableOrderedSet<NSFileProviderItem>\""
- "@112@0:8@16@24@32Q40@48^Q56^B64@72@80^B88^Q96^@104"
- "@16@?0@\"NSData\"8"
- "@16@?0@\"NSString\"8"
- "@28@0:8Q16i24"
- "@32@0:8B16C20@24"
- "@84@0:8@16@24@32@40@48@56B64B68B72@76"
- "@96@0:8@16@24@32@40Q48Q56@64@72^Q80^@88"
- "Als"
- "AppTelemetryCiconiaBouncesInvestigation"
- "AppTelemetryCiconiaEAccessInvestigation"
- "AppTelemetryCiconiaInvestigation"
- "B40@0:8q16q24q32"
- "B48@0:8@16@24@32Q40"
- "B48@0:8^@16^@24@32^@40"
- "B52@0:8@16@24B32@36^@44"
- "BRCSendDictionaryToCoreAnalytics"
- "BounceBucket:%d"
- "BouncingCountFrom%@To%@"
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
- "CleanupFailure"
- "DELETE FROM telemetry_events"
- "DELETE FROM telemetry_events ORDER BY priority ASC, rowid ASC LIMIT %u"
- "DELETE FROM telemetry_events WHERE %@"
- "Dir"
- "Doc"
- "FPCK Error: %@"
- "FPCK Stats: %@"
- "FPFS_MIGRATION"
- "Get provider domain error: %@"
- "INSERT INTO ciconia_history (date, os, br, bird_schema, db_schema, ciconia_version, duration, uuid, last_error, last_originator) VALUES (%lu, %@, %@, %u, %@, %llu, %f, %@, %@, %llu)"
- "INSERT INTO server_items ( item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_rank, item_origname, pcs_state, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, zone_rowid, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count) VALUES ( %@, %@, %ld, %@, NULL, %@, %d, %@, %d, %d, %d, %lld, %lld, %lld, %@, %@, %d, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@, %@)"
- "INSERT INTO telemetry_events (payload, priority) VALUES (%@, %d)"
- "INSERT OR REPLACE INTO ciconia_migration_info values (%@, %d)"
- "INSERT OR REPLACE INTO ciconia_migration_info values (%@, %lld)"
- "Lnk"
- "No DSID"
- "OverBounce"
- "Pkg"
- "Provider domain empty storageURLs"
- "SELECT 1 FROM pragma_table_info('ciconia_history') WHERE name='last_originator'"
- "SELECT 1 FROM sqlite_master where type = 'table' AND name = 'ciconia_history'"
- "SELECT 1 FROM sqlite_master where type = 'table' AND name = 'ciconia_migration_info'"
- "SELECT COUNT(1) FROM ciconia_history WHERE ciconia_version = %llu AND last_originator = %llu"
- "SELECT COUNT(1) FROM telemetry_events"
- "SELECT COUNT(uuid), COUNT(last_error) FROM ciconia_history %@"
- "SELECT MAX(ciconia_version) FROM ciconia_history WHERE last_error IS NULL"
- "SELECT csu.throttle_id, csu.last_try_stamp FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
- "SELECT date,os,br,bird_schema,db_schema,ciconia_version,last_error,duration,uuid %@ FROM ciconia_history ORDER BY date DESC LIMIT 10"
- "SELECT last_originator FROM ciconia_history WHERE ciconia_version == %lu AND last_originator != 0"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_state = 1    AND li.item_localsyncupstate = 4    AND NOT EXISTS(SELECT 1 FROM client_items AS ci                     WHERE li.item_id = ci.item_parent_id                      AND ci.zone_rowid = su.zone_rowid)    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su    ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (1, 2, 8, 5, 6, 7, 3)    AND li.item_state = 0    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT li.rowid, li.zone_rowid, li.item_id, li.item_creator_id, li.item_sharing_options, li.item_side_car_ckinfo, li.item_parent_zone_rowid, li.item_localsyncupstate, li.item_local_diffs, li.item_notifs_rank, li.app_library_rowid, li.item_min_supported_os_rowid, li.item_user_visible, li.item_stat_ckinfo, li.item_state, li.item_type, li.item_mode, li.item_birthtime, li.item_lastusedtime, li.item_favoriterank,li.item_parent_id, li.item_filename, li.item_hidden_ext, li.item_finder_tags, li.item_xattr_signature, li.item_trash_put_back_path, li.item_trash_put_back_parent_id, li.item_alias_target, li.item_creator, li.item_processing_stamp, li.item_bouncedname, li.item_scope, li.item_local_change_count, li.item_old_version_identifier, li.fp_creation_item_identifier, li.version_name, li.version_ckinfo, li.version_mtime, li.version_size, li.version_thumb_size, li.version_thumb_signature, li.version_content_signature, li.version_xattr_signature, li.version_edited_since_shared, li.version_device, li.version_conflict_loser_etags, li.version_quarantine_info, li.version_uploaded_assets, li.version_upload_error, li.version_old_zone_item_id, li.version_old_zone_rowid, li.version_local_change_count, li.version_old_version_identifier, li.item_live_conflict_loser_etags, li.item_file_id, li.item_generation FROM client_items AS li  INNER JOIN client_sync_up AS su  ON su.throttle_id = li.rowid  WHERE         su.throttle_state = 50    AND su.zone_rowid = %@    AND su.in_flight_diffs IS NULL    AND li.item_type IN (0, 9, 10, 4)    AND (li.item_state = 0)    AND li.item_localsyncupstate = 4    AND li.item_min_supported_os_rowid IS NULL"
- "SELECT payload FROM telemetry_events"
- "SELECT rowid, payload FROM telemetry_events WHERE NOT %@ ORDER BY rowid ASC LIMIT %llu"
- "SELECT rowid, payload FROM telemetry_events WHERE priority = 1 ORDER BY rowid LIMIT %u"
- "SELECT si.zone_rowid, si.item_rank, si.item_origname, si.pcs_state, si.item_id, si.item_creator_id, si.item_sharing_options, si.item_side_car_ckinfo, si.item_stat_ckinfo, si.item_state, si.item_type, si.item_mode, si.item_birthtime, si.item_lastusedtime, si.item_favoriterank,si.item_parent_id, si.item_filename, si.item_hidden_ext, si.item_finder_tags, si.item_xattr_signature, si.item_trash_put_back_path, si.item_trash_put_back_parent_id, si.item_alias_target, si.item_creator, si.version_name, si.version_ckinfo, si.version_mtime, si.version_size, si.version_thumb_size, si.version_thumb_signature, si.version_content_signature, si.version_xattr_signature, si.version_edited_since_shared, si.version_device, si.version_conflict_loser_etags, si.version_quarantine_info, si.quota_used, si.recursive_child_count, si.shared_children_count, si.shared_alias_count, si.child_count, ci.item_id FROM server_items AS si LEFT JOIN client_items AS ci ON si.item_id = ci.item_id AND si.zone_rowid = ci.zone_rowid WHERE si.item_alias_target = %@ AND si.item_type = 3 AND si.item_state = 0 AND (ci.item_id IS NULL OR ci.item_state != 1) %@ ORDER BY si.item_id"
- "SELECT version_ckinfo FROM client_items WHERE rowid = %ld"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_filename = %@ AND item_type = 3 AND zone_rowid = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_id = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_id = %@ AND zone_rowid = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND item_filename = %@ AND +zone_rowid = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_parent_id = %@ AND zone_rowid = %@ AND item_filename != '.Trash' AND pcs_state NOT IN (2, 3) LIMIT 1"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE item_rank = %lld AND zone_rowid = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE rowid = %lld"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE zone_rowid = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count FROM server_items WHERE zone_rowid = %@ AND call_block(%@, rowid)"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count, rowid      FROM server_items    WHERE zone_rowid = %@ AND item_parent_id = %@"
- "SELECT zone_rowid, item_rank, item_origname, pcs_state, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, quota_used, recursive_child_count, shared_children_count, shared_alias_count, child_count, rowid      FROM server_items    WHERE zone_rowid = %@ AND item_parent_id = %@ ORDER BY item_filename"
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
- "TI,N,V_identifier"
- "TI,N,V_stFlags"
- "Td,N,V_cloningTime"
- "Tf,N,V_previousReleasesSuccessRate"
- "Ti,N,V_aliasToFileCount"
- "Ti,N,V_aliasToFolderCount"
- "Ti,N,V_aliasToPackageCount"
- "Ti,N,V_aliasToSymlinkCount"
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
- "UPDATE ciconia_migration_info SET value = value + 1 WHERE key = %@"
- "UPDATE client_items SET fp_creation_item_identifier = NULL"
- "UPDATE client_uploads    SET throttle_state = %d, transfer_operation = NULL  WHERE %@"
- "UPDATE client_uploads SET  throttle_state = %d, transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL WHERE throttle_id = %@"
- "UPDATE server_items    SET item_rank = NULL, item_depth = 0, item_sharing_options = (%lu | (item_sharing_options & %lu)), version_name = %@, version_ckinfo = %@, version_mtime = %lld, version_size = %lld, version_thumb_size = %lld, version_thumb_signature = %@, version_content_signature = %@, version_xattr_signature = %@, version_edited_since_shared = %@, version_device = %@, version_conflict_loser_etags = %@, version_quarantine_info = %@  WHERE item_id = %@ AND zone_rowid = %@"
- "UPDATE server_items SET   item_rank = NULL, item_depth = 0, item_origname = %@, pcs_state = %d, item_sharing_options = (%lu | (item_sharing_options & %lu)), item_side_car_ckinfo = %@, item_stat_ckinfo = %@, item_state = %d, item_type = %d, item_mode = %d, item_birthtime = %lld, item_lastusedtime = %lld, item_favoriterank = %lld, item_parent_id = %@, item_filename = %@, item_hidden_ext = %d, item_finder_tags = %@, item_xattr_signature = %@, item_trash_put_back_path = %@, item_trash_put_back_parent_id = %@, item_alias_target = %@, item_creator = %@, quota_used = %@, recursive_child_count = %@, shared_children_count = %@, shared_alias_count = %@, child_count = %@ WHERE item_id = %@ AND zone_rowid = %@"
- "WHERE ciconia_version %@ %llu"
- "X-APPLE-APP-TELEMETRY"
- "[CRIT] Assertion failed: (NSUInteger)self->_session.clientDB.changes == _lastTelemetryBatchRowIDs.count%@"
- "[CRIT] Assertion failed: [originatorID intValue] > 0%@"
- "[CRIT] Assertion failed: [targetItem.contentType br_isSymbolicLinkType]%@"
- "[CRIT] Assertion failed: _currentTelemetryToken.longLongValue == [persistedState telemetryToken]%@"
- "[CRIT] Assertion failed: _session.offline%@"
- "[CRIT] Assertion failed: _telemetryEventCount >= 0 _telemetryEventCount: %lld. Amount: %lld%@"
- "[CRIT] Assertion failed: priority <= 1%@"
- "[CRIT] Assertion failed: self->_telemetryEventCount == 0%@"
- "[CRIT] Assertion failed: self.session%@"
- "[CRIT] UNREACHABLE: Operation %@ is missing syncContext%@"
- "[DEBUG] %@ - dealloc called%@"
- "[DEBUG] %@ needs to sync items in the sync bubble (sz:%llu)%@"
- "[DEBUG] Application proxy: %@%@"
- "[DEBUG] Calling copyDatabaseForFPCKStartingAtPath:%@ ...%@"
- "[DEBUG] Calling runFPCKForDomainWithID:%@ ...%@"
- "[DEBUG] Can't delete shared top level item yet which is still syncing in another zone %@%@"
- "[DEBUG] Cleaning telemetry after updating BR version%@"
- "[DEBUG] Closing database%@"
- "[DEBUG] Completed upload for all items for %@%@"
- "[DEBUG] Copying account DSID from %@ to %@%@"
- "[DEBUG] Copying xattrs from %@ to %@%@"
- "[DEBUG] Creating a BRCSafeDBHolder %p for db in path: %@%@"
- "[DEBUG] Database closed%@"
- "[DEBUG] Dedicating this sync up operation to pcs chaining %@%@"
- "[DEBUG] Deleting telemetry events: %@%@"
- "[DEBUG] Dequeued %lu telemetry events to send with token %lld (size %lu)%@"
- "[DEBUG] Download canceled for document %@ and etag:%@. Notifying download trackers%@"
- "[DEBUG] Dropping telemtry events due to queue overflow%@"
- "[DEBUG] FPCK Report: %@%@"
- "[DEBUG] FPCK Result: %@%@"
- "[DEBUG] FPCK returned no error, checking for the report%@"
- "[DEBUG] Force Telemetry Deque passed the minimum interval%@"
- "[DEBUG] Found table ciconia_migration_info, trying to fill it up%@"
- "[DEBUG] Inserting telemetry event %u%@"
- "[DEBUG] Not considering %@ for sync bubble tasks because sync is blocked%@"
- "[DEBUG] Offline work, skipping notification%@"
- "[DEBUG] Sending telemetry events in operation %@%@"
- "[DEBUG] Setting the dump flag on stage registry%@"
- "[DEBUG] Still need to sync up %@ more items for sync bubble for %@%@"
- "[DEBUG] The server has detected a problem on the client. Resetting all sync telemetry%@"
- "[DEBUG] There are more telemetry events to dequeue%@"
- "[DEBUG] Triggering FPCK for domain: %@%@"
- "[DEBUG] Uploader: below maximum allowed number of thumbnails retrieval (%ld)%@"
- "[DEBUG] Uploader: reached maximum allowed number of thumbnails retrieval (%ld)%@"
- "[DEBUG] Uploader[%@]: generating thumbnail (shouldTransferThumbnail:yes) %@%@"
- "[DEBUG] dropping item which was deleted %@%@"
- "[DEBUG] iCloud Analytics collection has been disabled, not sending PoC telemetry%@"
- "[DEBUG] sending batch from %llu to %llu (%@,%@)%@"
- "[DEBUG] updating telemetry token %@ -> %lld%@"
- "[DEBUG] ┏%llx Failed to get participantDocumentToken --> use participantKey as before. item: %@%@"
- "[DEBUG] ┏%llx Fetch participantDocumentToken disabled --> use participantKey as before. item: %@%@"
- "[DEBUG] ┏%llx Saving item %@%@"
- "[DEBUG] ┏%llx received a push in the %@ database for topic:'%@' payload:%@ token:%@%@"
- "[ERROR] Ciconia DB was dropped - domain removal will happen on next start%@"
- "[ERROR] Error copying FPFS databases for FPCK: %@%@"
- "[ERROR] FPCK return failures in the report%@"
- "[ERROR] FPCK returned an error: %@%@"
- "[ERROR] Failed to saved migration attempt %@: %@%@"
- "[ERROR] nil app bundle ID for share URL: %@%@"
- "[INFO] Failed inserting into ciconia_migration_info. Error = %@. Ignoring%@"
- "[NOTICE] Current Ciconia failure is TTR worthy? %d (%ld)%@"
- "[NOTICE] Forcing telemetry events dequeue%@"
- "[NOTICE] Telemetry dequeue already queued%@"
- "[NOTICE] Will send the report %@%@"
- "[NOTIF] document %@ didCompleteDownloadEtagIfLoser %@ withError %@ - Found trackers: %s%@"
- "[WARNING] Bypassing FPCK post import analysis due to user default: fpfs.run-fpck-in-post-import-analysis%@"
- "[WARNING] Clearing sharing options on missing share for %@%@"
- "[WARNING] Copying account DSID from %@ to %@%@"
- "[WARNING] Failed updating ciconia_migration_info for key %@: %@%@"
- "[WARNING] Importing unknown item: %@ - that's unexpected!%@"
- "[WARNING] Learning new sharing options %@ from refresh state for %@%@"
- "[WARNING] Learning updated item mode %s from refresh state for %@%@"
- "[WARNING] Not submitting event which is disabled %u%@"
- "[WARNING] Server zone was updated during refresh - avoiding races%@"
- "[WARNING] Skipping xattr check because we're in the middle of a dump%@"
- "[WARNING] We already have a bubble sync task %@%@"
- "[WARNING] calling the upload handler because sync is failing: %@%@"
- "[WARNING] force deleting item with missing share in shared zone %@%@"
- "_aliasToFileCount"
- "_aliasToFolderCount"
- "_aliasToPackageCount"
- "_aliasToSymlinkCount"
- "_areMigratedFaultsBelowThreshold"
- "_areNonFaultAllMigrated"
- "_bouncedDocumentsFoldersCount"
- "_bouncesInvestigation"
- "_checkIfShouldWaitUntilDownloadCompletion"
- "_ciconiaInvestigation"
- "_ciconiaOriginatorIDs:byDefault:"
- "_ciconiaVersion"
- "_cloningTime"
- "_crashReporterKey"
- "_createFileProvidingRequestOperationOfFileObject:localItem:etagIfLoser:etagToDownload:progress:reply:"
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
- "_fpckReportFileNameForMigrationID:"
- "_garbageCollectUploadThumbnails"
- "_getPriorityOfEvent:"
- "_identifier"
- "_ignoredContentProtectedItems"
- "_investigationKeysToRemove"
- "_isAccountRestricted"
- "_isAppInstalled"
- "_isCiconiaErrorTTRWorthy:"
- "_isDesktopEnabled"
- "_isExpectedCiconiaError:originatorId:"
- "_isFolderSharingSupported"
- "_isUserSignedInToiCloudDrive"
- "_itemsChangedDuringCloning"
- "_lastSentTelemetryEvents"
- "_lastTelemetryBatchRowIDs"
- "_locateMatchingItemForTemplateItem:parentItem:logicalName:options:fileURL:fields:shouldReject:additionalAttrs:importBookmark:ignoreImportBookmark:stillPendingFields:error:"
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
- "_registerLastBootIfNeeded:table:cleanTelemetryIfNeeded:skipControlFiles:deviceIDChanged:"
- "_reportEAccessDuringSilentMigration:uuid:"
- "_reportForFPFSImportStatusTelemetryEventIfNeeded:"
- "_reportOverBounceDuringSilentMigration:total:uuid:"
- "_saveFPCKStatusForTapToRadar:stats:report:withMigrationID:"
- "_saveItemID:version:record:iWorkSharingOptions:"
- "_setSpotlightAttribute"
- "_setTelemetryHeaderOnCKOpIfNecessary:"
- "_setXattrs:session:"
- "_shouldFetchParticipantDocumentToken"
- "_shouldTriggerTapToRadar:itemsNotMigrated:reconciledItems:"
- "_showSharingJoinDialog"
- "_signalPropagationToChildren"
- "_stGid"
- "_stUid"
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
- "_triggerFPCKForProviderDomainID:completionHandler:"
- "_underlyingErrorCode"
- "_underlyingErrorDescription"
- "_underlyingErrorDomain"
- "_unexpectedCreations"
- "_updateCiconiaDatabaseForBouncing:existingItem:"
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
- "br_description"
- "br_getStatsErrorBitmap"
- "can't initialize document with invalid library rowid %@"
- "can't initialize shared zone root with invalid zone rowid %@"
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
- "ciconia_history"
- "cleanupCiconiaForPersonaID:atURL:diagnosticsURL:withReply:"
- "cloningTime"
- "cloudEnabledStatusForSession:"
- "com.apple.CloudDocsDaemon.ciconia"
- "com.apple.CloudDocsDaemon.telemetry-disk-checker"
- "com.apple.bird.fpfs-migration-finished-telemetry"
- "container"
- "contentPolicyForZoneRoot:isAppInstalled:isWallet:isGreedyDocument:"
- "copyDatabaseForFPCKStartingAtPath failed: %@"
- "copyDatabaseForFPCKStartingAtPath:completionHandler:"
- "copyItemAtPath:toPath:error:"
- "createSQLConditionForRowIDs:"
- "createStageURLFromLiveURLForItem:error:"
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
- "fpck-%@.txt"
- "fpfs.migration.finished.telemetry.xpc"
- "fpfs.run-fpck-in-post-import-analysis"
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
- "importNewItemAtURL:logicalName:parentItem:templateItem:fields:options:additionalItemAttributes:importBookmark:stillPendingFields:error:"
- "initForTestingDevice:"
- "initWithMangledID:dbRowID:zoneRowID:db:plist:session:initialCreation:createdRootOnDisk:createdCZMMoved:rootFileID:"
- "initWithRecordID:serverZone:isUserWaiting:"
- "initWithShareMetadata:client:session:"
- "initiateSilentMigrationOf:forPersonaID:withParameters:andReply:"
- "iwork-collaboration.fetch-participant-document-token"
- "lastCiconiaVersion:"
- "lastForceTelemetrySyncDate"
- "lazyXattrWithSession:"
- "libfssync.FileTreeError<libfssync.VFSItem>"
- "manuallyTriggeredMigration"
- "materialisedOnCDItemsCount"
- "materialisedOnFPFSItemsCount"
- "migration encountered a fatal error"
- "newAppLibraryFromPQLResultSet:error:"
- "newCiconiaReportEvent:state:"
- "newIntEvent:eventGroupUUID:value:"
- "newLongEvent:eventGroupUUID:value:"
- "newLongEvent:eventGroupUUID:value:round:"
- "nonConflictingKindCount"
- "numberFromString:"
- "numberOfBrokenFilesInFSAndFSSnapshotCheck"
- "numberOfBrokenFilesInFSSnapshotAndFPSnapshotCheck"
- "numberOfBrokenFilesInReconciliationTableCheck"
- "numberOfBrokenFilesInReconciliationTableCheck: %ld, numberOfBrokenFilesInFSAndFSSnapshotCheck :%ld, numberOfBrokenFilesInFSSnapshotAndFPSnapshotCheck: %ld"
- "numberOfFilesChecked"
- "orderedSet"
- "outputStreamToFileAtPath:append:"
- "packageToAliasCount"
- "packageToFileCount"
- "packageToFolderCount"
- "packageToSymlinkCount"
- "post-fpfs-import-analysis"
- "previousAttempts"
- "previousFailedAttempts"
- "previousReleasesSuccessRate"
- "protectionClass"
- "providerDomainWithID:error:"
- "q32@0:8B16B20B24B28"
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
- "runFPCKForDomainWithID:databasesBackupsPath:options:reason:completionHandler:"
- "runFPCKInPostImportAnalysis"
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
- "v16@?0@\"CKRequestInfo\"8"
- "v32@0:8@\"BRCMigrationReport\"16@?<v@?@\"NSError\">24"
- "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
- "v36@0:8@16B24B28B32"
- "v40@0:8@\"BRCMigrationReport\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"CKShareMetadata\"16@\"BRCAccountSessionFPFS\"24@?<v@?B@\"NSError\">32"
- "v40@0:8^Q16^Q24@32"
- "v40@?0@\"NSString\"8@\"FPCKStats\"16@\"NSDictionary\"24@\"NSError\"32"
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
- "v64@0:8@16@24@32@40@48@?56"
- "x-apple-app-telemetry-new-server-token"
- "{?=\"accountQuotaUsage\"b1\"bouncedDocumentsFoldersCount\"b1\"bouncedItemsCount\"b1\"bouncedItemsMatrix\"b1\"ciconiaVersion\"b1\"cloningTime\"b1\"datalessItemsCount\"b1\"diskSpaceLeft\"b1\"documentsFoldersWithoutItemIDCount\"b1\"expectedMigratedItemsCount\"b1\"ignoredContentProtectedItems\"b1\"importTime\"b1\"itemsChangedDuringCloning\"b1\"itemsNotFoundInDB\"b1\"itemsNotMigratedCount\"b1\"materialisedOnCDItemsCount\"b1\"materialisedOnFPFSItemsCount\"b1\"packagesWithoutBundleBit\"b1\"previousAttempts\"b1\"previousFailedAttempts\"b1\"symlinkedDocumentsFolderCount\"b1\"totalItemCount\"b1\"underlyingErrorCode\"b1\"unexpectedCreations\"b1\"previousReleasesSuccessRate\"b1\"typesOfMigratedItemsMask\"b1\"typesOfNonMigratedItemsMask\"b1\"areMigratedFaultsBelowThreshold\"b1\"areNonFaultAllMigrated\"b1\"isAccountDataSeparated\"b1\"isDesktopEnabled\"b1\"manuallyTriggeredMigration\"b1}"
- "{?=\"aliasToFileCount\"b1\"aliasToFolderCount\"b1\"aliasToPackageCount\"b1\"aliasToSymlinkCount\"b1\"fileToAliasCount\"b1\"fileToFolderCount\"b1\"fileToPackageCount\"b1\"fileToSymlinkCount\"b1\"folderToAliasCount\"b1\"folderToFileCount\"b1\"folderToPackageCount\"b1\"folderToSymlinkCount\"b1\"nonConflictingKindCount\"b1\"packageToAliasCount\"b1\"packageToFileCount\"b1\"packageToFolderCount\"b1\"packageToSymlinkCount\"b1\"symlinkToAliasCount\"b1\"symlinkToFileCount\"b1\"symlinkToFolderCount\"b1\"symlinkToPackageCount\"b1}"
- "{?=\"curGid\"b1\"curUid\"b1\"protectionClass\"b1\"stFlags\"b1\"stGid\"b1\"stMode\"b1\"stUid\"b1\"hasAcls\"b1}"
- "\xf0\x92\x12\x12"

```
