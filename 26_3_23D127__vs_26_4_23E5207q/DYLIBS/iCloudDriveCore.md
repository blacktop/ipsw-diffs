## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.80.8.0.0
-  __TEXT.__text: 0x314384
-  __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1a44c
-  __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7dc6b
-  __TEXT.__oslogstring: 0x3c3ae
-  __TEXT.__gcc_except_tab: 0x1a634
-  __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0xa070
-  __TEXT.__objc_classname: 0x2b47
-  __TEXT.__objc_methname: 0x44a54
-  __TEXT.__objc_methtype: 0x90b4
-  __TEXT.__objc_stubs: 0x2f520
+4479.100.79.0.4
+  __TEXT.__text: 0x31fbc0
+  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__objc_methlist: 0x1a9d4
+  __TEXT.__const: 0x4e0
+  __TEXT.__cstring: 0x7dcb5
+  __TEXT.__oslogstring: 0x3b548
+  __TEXT.__gcc_except_tab: 0x19e88
+  __TEXT.__ustring: 0x36
+  __TEXT.__unwind_info: 0xa7a8
+  __TEXT.__objc_classname: 0x2ae4
+  __TEXT.__objc_methname: 0x45972
+  __TEXT.__objc_methtype: 0x94bb
+  __TEXT.__objc_stubs: 0x2fa60
   __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__const: 0x9640
-  __DATA_CONST.__objc_classlist: 0xa80
-  __DATA_CONST.__objc_catlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x288
+  __DATA_CONST.__const: 0x94d8
+  __DATA_CONST.__objc_classlist: 0xa58
+  __DATA_CONST.__objc_catlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe7e0
+  __DATA_CONST.__objc_selrefs: 0xea78
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x940
+  __DATA_CONST.__objc_superrefs: 0x910
   __DATA_CONST.__objc_arraydata: 0xe78
-  __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH_CONST.__const: 0x2c00
-  __AUTH_CONST.__cfstring: 0x22cc0
-  __AUTH_CONST.__objc_const: 0x3d560
-  __AUTH_CONST.__objc_intobj: 0xbd0
-  __AUTH_CONST.__objc_arrayobj: 0x228
+  __AUTH_CONST.__auth_got: 0xd58
+  __AUTH_CONST.__const: 0x2bc0
+  __AUTH_CONST.__cfstring: 0x227c0
+  __AUTH_CONST.__objc_const: 0x3d878
+  __AUTH_CONST.__objc_intobj: 0xbe8
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x28c8
+  __AUTH.__objc_data: 0x2698
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1fb4
-  __DATA.__data: 0x2740
+  __DATA.__objc_ivar: 0x1f40
+  __DATA.__data: 0x2800
   __DATA.__bss: 0x210
-  __DATA_DIRTY.__objc_data: 0x4038
+  __DATA_DIRTY.__objc_data: 0x40d8
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x410
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/C2.framework/C2
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 54E24E67-29F5-3205-BCF0-A918E9C7D288
-  Functions: 13649
-  Symbols:   44440
-  CStrings:  27827
+  UUID: 4BBF399B-7E2C-390F-90AF-CF95ECC02A02
+  Functions: 13755
+  Symbols:   45297
+  CStrings:  27781
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newClientDBCachedStatementsCountEventWithValue:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newDiskSpaceReclaimedBytes:]
+ +[BRCAccountSession(BRCDatabaseManager) upgradeOfflineDB:serverTruth:session:error:].cold.2
+ +[BRCRFAEmailSettingHandler isEmailSettingEnabledWithSyncContext:reply:]
+ +[BRCRFAEmailSettingHandler isEmailSettingEnabledWithSyncContext:reply:].cold.1
+ +[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:]
+ +[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:].cold.1
+ +[BRCSyncUpOperation pcsChainItem:forZone:sessionContext:]
+ +[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToPCSChainingItem:fullyChainedParentIDs:]
+ +[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToPCSChainingItem:fullyChainedParentIDs:].cold.1
+ +[BRCSyncUpOperationBuilder checkIfShouldDedicateOpToPCSChainingItem:]
+ +[BRCUserDefaults _personaToUserDefaultsManager]
+ +[BRCUserDefaults _personaToUserDefaultsManager].cold.1
+ +[CKOperationGroup(BRAdditions) br_rsaEmailSettingRetrieve]
+ +[CKOperationGroup(BRAdditions) br_rsaEmailSettingUpdate]
+ +[CKOperationGroup(BRAdditions) br_syncUpForPCSChain]
+ -[BRCAccountSession _loadSyncEngine]
+ -[BRCAccountSession _loadSyncEngine].cold.1
+ -[BRCAccountSession _loadSyncEngine].cold.2
+ -[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]
+ -[BRCAccountSession _registerBackgroundSystemTasks]
+ -[BRCAccountSession enableEnhancedDrivePrivacyForZone:ownerName:completionHandler:]
+ -[BRCAccountSession fileProviderItemIdentifierForItemIdentifierString:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession generateRequestIDForZone:ownerName:completionHandler:]
+ -[BRCAccountSession hasSyncedDownZoneSinceStartup:ownerName:completionHandler:]
+ -[BRCAccountSession invokePCSChainOnItem:zoneName:completionHandler:]
+ -[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession recoverAndReportNamespaceAndContentPolicyWithCompletion:]
+ -[BRCAccountSession serverItemForItemIdentifier:]
+ -[BRCAccountSession serverItemForItemIdentifierString:zoneName:ownerName:]
+ -[BRCAccountSession serverItemWithParent:filename:zoneName:ownerName:]
+ -[BRCAccountSession shouldPCSChainItem:zoneName:completionHandler:]
+ -[BRCAccountSession syncEngine]
+ -[BRCAccountSession updatePCSStateForItemIdentifier:newState:zoneName:ownerName:completionHandler:]
+ -[BRCAccountSession uploadV2Enabled]
+ -[BRCAccountSession waitForSyncDownOfZone:ownerName:completionHandler:]
+ -[BRCAnalyticsReporter _sendCachedStatementsCountTelemetryEvent]
+ -[BRCAppLibrary trashItemIDWithFacade:]
+ -[BRCClientZone _activateZoneActiveStateIfNeededWithOrigState:]
+ -[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:]
+ -[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:].cold.1
+ -[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:].cold.2
+ -[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:].cold.3
+ -[BRCClientZone _closeHandlersAndBarriersBlocks]
+ -[BRCClientZone _deferredPlistFromPlist:]
+ -[BRCClientZone _getPrivateClientZone]
+ -[BRCClientZone _hasAnyItemInZoneOtherThanDocumentsFolder]
+ -[BRCClientZone _initializeZoneActiveStateIfNeeded]
+ -[BRCClientZone _initializeZoneActiveStateIfNeeded].cold.1
+ -[BRCClientZone _initializeZoneActiveStateIfNeeded].cold.2
+ -[BRCClientZone _initializeZoneActiveStateIfNeeded].cold.3
+ -[BRCClientZone _invalidateZoneActiveStateIfNeeded]
+ -[BRCClientZone _invalidateZoneActiveStateIfNeeded].cold.1
+ -[BRCClientZone _invalidateZoneActiveStateIfNeeded].cold.2
+ -[BRCClientZone _invalidateZoneActiveStateIfNeeded].cold.3
+ -[BRCClientZone _isResetting]
+ -[BRCClientZone _memoryOptimizationEnabled]
+ -[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary].cold.1
+ -[BRCClientZone _sendZoneResetAnalyticsAndTTRForError:resetReason:alternativeError:]
+ -[BRCClientZone clearSyncStateBits:].cold.1
+ -[BRCClientZone createPCSChainOperationForItem:]
+ -[BRCClientZone plist].cold.1
+ -[BRCClientZone plist].cold.2
+ -[BRCClientZone postContainerStatusChangeNotificationForKey:value:]
+ -[BRCClientZone postContainerStatusChangeNotificationForKey:value:].cold.1
+ -[BRCClientZone resume].cold.4
+ -[BRCClientZone scheduleResetServerAndClientTruthsWithError:]
+ -[BRCClientZone scheduleResetServerAndClientTruthsWithError:completionHandler:]
+ -[BRCClientZone scheduleSyncUp].cold.1
+ -[BRCClientZone setSyncStateBits:].cold.3
+ -[BRCClientZone shouldPCSChainItem:completionHandler:]
+ -[BRCClientZone updateWithPlist:isDeferredPlist:]
+ -[BRCClientZone waitForSyncDownWithCompletionHandler:]
+ -[BRCClientZoneActiveState .cxx_destruct]
+ -[BRCClientZoneActiveState addToPlist:]
+ -[BRCClientZoneActiveState allItemsDidUploadTrackers]
+ -[BRCClientZoneActiveState allocateSyncUpRequestID]
+ -[BRCClientZoneActiveState appliedTombstoneRanks]
+ -[BRCClientZoneActiveState blockedOperationsOnInitialSync]
+ -[BRCClientZoneActiveState bubbleSyncTask]
+ -[BRCClientZoneActiveState close]
+ -[BRCClientZoneActiveState currentSyncDownBarriers]
+ -[BRCClientZoneActiveState decreaseSyncUpBatchSizeAfterError]
+ -[BRCClientZoneActiveState description]
+ -[BRCClientZoneActiveState directoriesCreatedLastSyncUp]
+ -[BRCClientZoneActiveState downloadedBlockToPerformForItemID]
+ -[BRCClientZoneActiveState faultsLiveBarriers]
+ -[BRCClientZoneActiveState fetchAndClearSyncStateBits:]
+ -[BRCClientZoneActiveState fetchAndSetSyncStateBits:]
+ -[BRCClientZoneActiveState fetchParentOperations]
+ -[BRCClientZoneActiveState fetchRecentsOperation]
+ -[BRCClientZoneActiveState hasWorkDidUpdateObserver]
+ -[BRCClientZoneActiveState increaseSyncUpBatchSizeAfterSuccess]
+ -[BRCClientZoneActiveState initWithMangledID:]
+ -[BRCClientZoneActiveState invokeFetchRecentsOperation]
+ -[BRCClientZoneActiveState lastAttemptedSyncDownDate]
+ -[BRCClientZoneActiveState lastInsertedRank]
+ -[BRCClientZoneActiveState lastSyncDownDate]
+ -[BRCClientZoneActiveState lastSyncDownError]
+ -[BRCClientZoneActiveState lastSyncUpErrorWasOnChainedItem]
+ -[BRCClientZoneActiveState lastSyncUpError]
+ -[BRCClientZoneActiveState locateBlocksToPerformForRecordID]
+ -[BRCClientZoneActiveState locateRecordOperations]
+ -[BRCClientZoneActiveState locateRecordsOperationThrottle]
+ -[BRCClientZoneActiveState markRequestIDAcked]
+ -[BRCClientZoneActiveState nextIdleHandlers]
+ -[BRCClientZoneActiveState nextSyncDownBarriers]
+ -[BRCClientZoneActiveState onDiskBlockToPerformForItemID]
+ -[BRCClientZoneActiveState osNameRequiredToSync]
+ -[BRCClientZoneActiveState outOfBandSyncOperations]
+ -[BRCClientZoneActiveState recursiveListOperations]
+ -[BRCClientZoneActiveState requestID]
+ -[BRCClientZoneActiveState resetAfterAppUninstallTimer]
+ -[BRCClientZoneActiveState resetSyncBudgetAndThrottle]
+ -[BRCClientZoneActiveState resetTimer]
+ -[BRCClientZoneActiveState runningListOperations]
+ -[BRCClientZoneActiveState serverStitchingOperationThrottle]
+ -[BRCClientZoneActiveState setAllItemsDidUploadTrackers:]
+ -[BRCClientZoneActiveState setAppliedTombstoneRanks:]
+ -[BRCClientZoneActiveState setBlockedOperationsOnInitialSync:]
+ -[BRCClientZoneActiveState setBubbleSyncTask:]
+ -[BRCClientZoneActiveState setCurrentSyncDownBarriers:]
+ -[BRCClientZoneActiveState setDirectoriesCreatedLastSyncUp:]
+ -[BRCClientZoneActiveState setDownloadedBlockToPerformForItemID:]
+ -[BRCClientZoneActiveState setFaultsLiveBarriers:]
+ -[BRCClientZoneActiveState setFetchParentOperations:]
+ -[BRCClientZoneActiveState setFetchRecentsOperation:]
+ -[BRCClientZoneActiveState setHasWorkDidUpdateObserver:]
+ -[BRCClientZoneActiveState setInvokeFetchRecentsOperation:]
+ -[BRCClientZoneActiveState setLastAttemptedSyncDownDate:]
+ -[BRCClientZoneActiveState setLastInsertedRank:]
+ -[BRCClientZoneActiveState setLastSyncDownDate:]
+ -[BRCClientZoneActiveState setLastSyncDownError:]
+ -[BRCClientZoneActiveState setLastSyncUpError:]
+ -[BRCClientZoneActiveState setLastSyncUpErrorWasOnChainedItem:]
+ -[BRCClientZoneActiveState setLocateBlocksToPerformForRecordID:]
+ -[BRCClientZoneActiveState setLocateRecordOperations:]
+ -[BRCClientZoneActiveState setLocateRecordsOperationThrottle:]
+ -[BRCClientZoneActiveState setNextIdleHandlers:]
+ -[BRCClientZoneActiveState setNextSyncDownBarriers:]
+ -[BRCClientZoneActiveState setOnDiskBlockToPerformForItemID:]
+ -[BRCClientZoneActiveState setOsNameRequiredToSync:]
+ -[BRCClientZoneActiveState setOutOfBandSyncOperations:]
+ -[BRCClientZoneActiveState setRecursiveListOperations:]
+ -[BRCClientZoneActiveState setRequestID:]
+ -[BRCClientZoneActiveState setResetAfterAppUninstallTimer:]
+ -[BRCClientZoneActiveState setResetTimer:]
+ -[BRCClientZoneActiveState setRunningListOperations:]
+ -[BRCClientZoneActiveState setServerStitchingOperationThrottle:]
+ -[BRCClientZoneActiveState setShouldShowiCloudDriveAppInstallationNotification:]
+ -[BRCClientZoneActiveState setSyncDeadlineSource:]
+ -[BRCClientZoneActiveState setSyncDeadlineSourceResumer:]
+ -[BRCClientZoneActiveState setSyncDownBlockToPerformForBookmarkData:]
+ -[BRCClientZoneActiveState setSyncDownBlockToPerformForItemID:]
+ -[BRCClientZoneActiveState setSyncDownCompletionHandlers:]
+ -[BRCClientZoneActiveState setSyncDownDependencies:]
+ -[BRCClientZoneActiveState setSyncDownGroup:]
+ -[BRCClientZoneActiveState setSyncDownOperation:]
+ -[BRCClientZoneActiveState setSyncDownThrottle:]
+ -[BRCClientZoneActiveState setSyncThrottles:]
+ -[BRCClientZoneActiveState setSyncUpBackoffRatio:]
+ -[BRCClientZoneActiveState setSyncUpBatchSizeMultiplier:]
+ -[BRCClientZoneActiveState setSyncUpBudget:]
+ -[BRCClientZoneActiveState setSyncUpOperation:]
+ -[BRCClientZoneActiveState setSyncUpRetryAfter:]
+ -[BRCClientZoneActiveState setSyncUpThrottle:]
+ -[BRCClientZoneActiveState setTaskTracker:]
+ -[BRCClientZoneActiveState shouldShowiCloudDriveAppInstallationNotification]
+ -[BRCClientZoneActiveState syncDeadlineSourceResumer]
+ -[BRCClientZoneActiveState syncDeadlineSource]
+ -[BRCClientZoneActiveState syncDownBlockToPerformForBookmarkData]
+ -[BRCClientZoneActiveState syncDownBlockToPerformForItemID]
+ -[BRCClientZoneActiveState syncDownCompletionHandlers]
+ -[BRCClientZoneActiveState syncDownDependencies]
+ -[BRCClientZoneActiveState syncDownGroup]
+ -[BRCClientZoneActiveState syncDownOperation]
+ -[BRCClientZoneActiveState syncDownThrottle]
+ -[BRCClientZoneActiveState syncState]
+ -[BRCClientZoneActiveState syncThrottles]
+ -[BRCClientZoneActiveState syncUpBackoffRatio]
+ -[BRCClientZoneActiveState syncUpBatchSizeMultiplier]
+ -[BRCClientZoneActiveState syncUpBatchSize]
+ -[BRCClientZoneActiveState syncUpBudget]
+ -[BRCClientZoneActiveState syncUpOperation]
+ -[BRCClientZoneActiveState syncUpRetryAfter]
+ -[BRCClientZoneActiveState syncUpThrottle]
+ -[BRCClientZoneActiveState taskTracker]
+ -[BRCClientZoneActiveState updateFromPlist:]
+ -[BRCClientZoneActiveState updateFromPlist:].cold.1
+ -[BRCDatabaseFacade fetchRootItemIDAboveItemID:zoneRowID:serverTruth:itemState:depth:itemType:]
+ -[BRCDatabaseFacade fetchShareRootItemIDWithSharedChildItemID:zoneRowID:serverTruth:]
+ -[BRCDatabaseFacade serverItemFromClientRowID:itemBuilder:]
+ -[BRCDiskSpaceReclaimer _downloadGroupContainerStageSize]
+ -[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]
+ -[BRCDiskSpaceReclaimer resume]
+ -[BRCFSUploader _rescheduleUploadJobsPendingState:].cold.3
+ -[BRCFetchRecordSubResourcesOperation finishWithResult:error:].cold.5
+ -[BRCFileProviderDaemonUtils _initWithSyncBubble:]
+ -[BRCFileProvidingRequestOperation initWithDocumentItem:sessionContext:downloadTrackersManager:]
+ -[BRCFileProvidingRequestOperation initWithDocumentItem:sessionContext:downloadTrackersManager:].cold.1
+ -[BRCFileProvidingRequestOperation initWithDocumentItem:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:]
+ -[BRCFileUnlinker _moveOldUnlinkDir]
+ -[BRCFileUnlinker init]
+ -[BRCFileUnlinker init].cold.1
+ -[BRCFileUnlinker resumeWithTapToRadarManager:]
+ -[BRCFileUnlinker resumeWithTapToRadarManager:].cold.1
+ -[BRCLocalItem syncEngineMarkForceIdleWithVersion:]
+ -[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]
+ -[BRCMigrationQueryOperation _updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:]
+ -[BRCNotification initWithFileProviderItem:appLibraryID:]
+ -[BRCProgress brc_publish].cold.1
+ -[BRCProgress brc_unpublish].cold.1
+ -[BRCProgress group]
+ -[BRCProgress initUploadProgressForDocument:totalUnitCount:completedUnitCount:]
+ -[BRCProgress initWithUploadProgress:]
+ -[BRCProgress initWithUploadProgress:].cold.1
+ -[BRCProgress init]
+ -[BRCProgress session]
+ -[BRCQueryItemUtil contentAndNamespacePolicyForItemInfo:sessionContext:contentPolicy:namespacePolicy:]
+ -[BRCQueryItemUtil contentAndNamespacePolicyForRootContainerWithSessionContext:contentPolicy:namespacePolicy:]
+ -[BRCServerItem _computeIsTrashed]
+ -[BRCServerItem _initWithItemID:ownerKey:sideCarCKInfo:st:latestVersion:serverMetrics:serverZone:clientZone:session:sharingOptions:pcsChainState:]
+ -[BRCServerItem appLibrary]
+ -[BRCServerItem appLibrary].cold.1
+ -[BRCServerItem childItemCount]
+ -[BRCServerItem contentETag]
+ -[BRCServerItem contentExtendedAttributesSignature]
+ -[BRCServerItem contentSignature]
+ -[BRCServerItem creationTime]
+ -[BRCServerItem favoriteRank]
+ -[BRCServerItem fileName]
+ -[BRCServerItem fileSystemMode]
+ -[BRCServerItem finderTagData]
+ -[BRCServerItem hasUnresolvedConflicts]
+ -[BRCServerItem isSharedByCurrentUser]
+ -[BRCServerItem isTrashed]
+ -[BRCServerItem isTrashed].cold.1
+ -[BRCServerItem itemIdentifierString]
+ -[BRCServerItem itemType]
+ -[BRCServerItem itemType].cold.1
+ -[BRCServerItem lastModifiedTime]
+ -[BRCServerItem lastUsedTime]
+ -[BRCServerItem parentItemIdentifier]
+ -[BRCServerItem parentZoneETag]
+ -[BRCServerItem sideCarETag]
+ -[BRCServerItem size]
+ -[BRCServerItem structuralExtendedAttributesSignature]
+ -[BRCServerItem structureETag]
+ -[BRCServerItem symlinkTargetPath]
+ -[BRCServerItem zoneName]
+ -[BRCServerItem zoneOwnerName]
+ -[BRCSharedServerItem appLibrary]
+ -[BRCSharedServerItem appLibrary].cold.1
+ -[BRCSharedServerItem topLevelSharedItemID]
+ -[BRCSharingAcceptFlowOperation initWithShareMetadata:sessionContext:userNotifier:userActionsNavigator:]
+ -[BRCStageRegistry _garbageCollectSpace]
+ -[BRCStageRegistry _purgeSpaceUnderQueue]
+ -[BRCStageRegistry garbageCollectSpace]
+ -[BRCStageRegistry garbageCollectSpace].cold.1
+ -[BRCStageRegistry purgeGraveyardSpace]
+ -[BRCStageRegistry purgeGraveyardSpace].cold.1
+ -[BRCStageRegistry purgeSpace]
+ -[BRCStageRegistry workDirectoryForSyncEngine]
+ -[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:]
+ -[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:].cold.1
+ -[BRCSyncContext _nillifyMembers]
+ -[BRCSyncContext _setupCKContainerIfNeeded]
+ -[BRCSyncContext _setupCKContainerIfNeeded].cold.1
+ -[BRCSyncContext _setupDownloadStreamsIfNeeded]
+ -[BRCSyncContext _setupOperationQueuesIfNeeded]
+ -[BRCSyncContext _setupUploadStreamIfNeeded]
+ -[BRCSyncContext addOperation:allowsCellularAccess:]
+ -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:].cold.1
+ -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:].cold.2
+ -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:].cold.3
+ -[BRCSyncContext reclaimMemoryIfPossible]
+ -[BRCSyncContext reclaimMemoryIfPossible].cold.1
+ -[BRCSyncContextProvider dealloc]
+ -[BRCSyncContextProvider reclaimMemory]
+ -[BRCSyncUpOperation _clearErrorForRecord:inZone:]
+ -[BRCSyncUpOperation _localItemFromRecord:inZone:validateSyncUpState:]
+ -[BRCSyncUpOperation _localItemFromRecord:inZone:validateSyncUpState:].cold.1
+ -[BRCSystemResourcesManager _initReclaimMemory]
+ -[BRCSystemResourcesManager _initReclaimMemory].cold.1
+ -[BRCSystemResourcesManager _invalidateReclaimMemory]
+ -[BRCSystemResourcesManager _reclaimMemoryFromObserversDueToMemoryPressure:]
+ -[BRCSystemResourcesManager _reclaimMemoryFromObserversDueToMemoryPressure:].cold.1
+ -[BRCSystemResourcesManager addReclaimMemoryObserver:]
+ -[BRCSystemResourcesManager removeReclaimMemoryObserver:]
+ -[BRCUserDefaults _cacheValueLocally:forKey:]
+ -[BRCUserDefaults _checkLocalCacheForKey:inherit:validateWithBlock:]
+ -[BRCUserDefaults _checkLocalNSUserDefaultsForKey:validateWithBlock:]
+ -[BRCUserDefaults _checkServerOverrideForKey:validateWithBlock:]
+ -[BRCUserDefaults _handleGlobalFallbackForKey:validateWithBlock:]
+ -[BRCUserDefaults _handleGlobalFallbackForKey:validateWithBlock:].cold.1
+ -[BRCUserDefaults clientZoneMemoryOptimizationEnabled]
+ -[BRCUserDefaults dbFixupNamespaceAndContentPolicyRecoverAfterTimeInterval]
+ -[BRCUserDefaults diskSpaceReclaimedThresholdForSendingTelemetry]
+ -[BRCUserDefaults fpfsNamespacePolicyEnabled]
+ -[BRCUserDefaults graveyardAgeDelta]
+ -[BRCUserDefaults ignoredInternalCloudDocsErrorCodesForABCInReset]
+ -[BRCUserDefaults initAsGlobalWithServerConfiguration:localNSUserDefaultsDict:]
+ -[BRCUserDefaults initWithServerConfiguration:globalUserDefaults:localNSUserDefaultsDict:clientZoneIdentifier:]
+ -[BRCUserDefaults memoryReclaimerBGSystemTaskConfig]
+ -[BRCUserDefaults memoryReclaimerBGSystemTaskEnabled]
+ -[BRCUserDefaults periodicCacheDeleteBGSystemTaskConfig]
+ -[BRCUserDefaults syncContextIdleTimeBeforeMemoryReclaim]
+ -[BRCUserDefaultsManager _prepopulateLocalNSUserDefaults]
+ -[BRCUserDefaultsManager defaultsForIdentifier:].cold.3
+ -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:doNotObfuscate:reply:]
+ -[BRCXPCRegularIPCsClient computePurgeableSpaceWithReply:]
+ -[BRCXPCRegularIPCsClient handleUserNotificationResponse:reply:]
+ -[BRCXPCRegularIPCsClient isAccountCZM:]
+ -[BRCXPCRegularIPCsClient isRFAEmailSettingEnabledWithReply:]
+ -[BRCXPCRegularIPCsClient reclaimDiskSpaceWithReply:]
+ -[BRCXPCRegularIPCsClient setRFAEmailSettingEnabled:reply:]
+ -[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:].cold.1
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:].cold.1
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:].cold.2
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]
+ -[BRFieldStructureSignature StringAsFormatVersion:]
+ -[BRFieldStructureSignature formatVersionAsString:]
+ -[BRFieldStructureSignature formatVersion]
+ -[BRFieldStructureSignature hasFormatVersion]
+ -[BRFieldStructureSignature hasParentZoneEtag]
+ -[BRFieldStructureSignature hasSideCarEtag]
+ -[BRFieldStructureSignature parentZoneEtag]
+ -[BRFieldStructureSignature setFormatVersion:]
+ -[BRFieldStructureSignature setHasFormatVersion:]
+ -[BRFieldStructureSignature setParentZoneEtag:]
+ -[BRFieldStructureSignature setSideCarEtag:]
+ -[BRFieldStructureSignature sideCarEtag]
+ -[BRFieldXattrBlob(FPFSAdditions) extendedAttributesDictionary]
+ -[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]
+ -[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]
+ GCC_except_table105
+ GCC_except_table115
+ GCC_except_table126
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table162
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table179
+ GCC_except_table183
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table236
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table288
+ GCC_except_table293
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table318
+ GCC_except_table322
+ GCC_except_table339
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table354
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table370
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table398
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table405
+ GCC_except_table408
+ GCC_except_table413
+ GCC_except_table419
+ GCC_except_table425
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table445
+ GCC_except_table458
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table468
+ GCC_except_table472
+ GCC_except_table474
+ GCC_except_table475
+ GCC_except_table485
+ GCC_except_table499
+ GCC_except_table501
+ GCC_except_table529
+ GCC_except_table558
+ GCC_except_table560
+ GCC_except_table565
+ GCC_except_table571
+ GCC_except_table573
+ OBJC_IVAR_$_BRCClientZone._dbFacade
+ OBJC_IVAR_$_BRCClientZone._deferredPlist
+ OBJC_IVAR_$_BRCClientZone._zoneActiveState
+ OBJC_IVAR_$_BRFieldStructureSignature._formatVersion
+ OBJC_IVAR_$_BRFieldStructureSignature._has
+ OBJC_IVAR_$_BRFieldStructureSignature._parentZoneEtag
+ OBJC_IVAR_$_BRFieldStructureSignature._sideCarEtag
+ OBJC_IVAR_$_BRQueryItem._namespacePolicy
+ OBJC_IVAR_$_BRQueryItem._userInfo
+ _BRContainerDidChangeStatusDistributedNotification
+ _BRContainerIDKey
+ _BREntitlementRFAEmailSetting
+ _BREntitlementRFANotificationHandling
+ _OBJC_CLASS_$_BRCClientZoneActiveState
+ _OBJC_CLASS_$_BRCRFAEmailSettingHandler
+ _OBJC_CLASS_$_BRContainersMonitor
+ _OBJC_IVAR_$_BRCAccountSession._syncEngine
+ _OBJC_IVAR_$_BRCAppLibrary._trashItemID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._allItemsDidUploadTrackers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._appliedTombstoneRanks
+ _OBJC_IVAR_$_BRCClientZoneActiveState._blockedOperationsOnInitialSync
+ _OBJC_IVAR_$_BRCClientZoneActiveState._bubbleSyncTask
+ _OBJC_IVAR_$_BRCClientZoneActiveState._currentSyncDownBarriers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._directoriesCreatedLastSyncUp
+ _OBJC_IVAR_$_BRCClientZoneActiveState._downloadedBlockToPerformForItemID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._faultsLiveBarriers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._fetchParentOperations
+ _OBJC_IVAR_$_BRCClientZoneActiveState._fetchRecentsOperation
+ _OBJC_IVAR_$_BRCClientZoneActiveState._hasWorkDidUpdateObserver
+ _OBJC_IVAR_$_BRCClientZoneActiveState._invokeFetchRecentsOperation
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastAttemptedSyncDownDate
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastInsertedRank
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastSyncDownDate
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastSyncDownError
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastSyncUpError
+ _OBJC_IVAR_$_BRCClientZoneActiveState._lastSyncUpErrorWasOnChainedItem
+ _OBJC_IVAR_$_BRCClientZoneActiveState._locateBlocksToPerformForRecordID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._locateRecordOperations
+ _OBJC_IVAR_$_BRCClientZoneActiveState._locateRecordsOperationThrottle
+ _OBJC_IVAR_$_BRCClientZoneActiveState._mangledID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._nextIdleHandlers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._nextSyncDownBarriers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._onDiskBlockToPerformForItemID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._osNameRequiredToSync
+ _OBJC_IVAR_$_BRCClientZoneActiveState._outOfBandSyncOperations
+ _OBJC_IVAR_$_BRCClientZoneActiveState._recursiveListOperations
+ _OBJC_IVAR_$_BRCClientZoneActiveState._requestID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._resetAfterAppUninstallTimer
+ _OBJC_IVAR_$_BRCClientZoneActiveState._resetTimer
+ _OBJC_IVAR_$_BRCClientZoneActiveState._runningListOperations
+ _OBJC_IVAR_$_BRCClientZoneActiveState._serverStitchingOperationThrottle
+ _OBJC_IVAR_$_BRCClientZoneActiveState._shouldShowiCloudDriveAppInstallationNotification
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDeadlineSource
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDeadlineSourceResumer
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownBlockToPerformForBookmarkData
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownBlockToPerformForItemID
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownCompletionHandlers
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownDependencies
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownGroup
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownOperation
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncDownThrottle
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncState
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncThrottles
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpBackoffRatio
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpBatchSizeMultiplier
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpBudget
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpOperation
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpRetryAfter
+ _OBJC_IVAR_$_BRCClientZoneActiveState._syncUpThrottle
+ _OBJC_IVAR_$_BRCClientZoneActiveState._taskTracker
+ _OBJC_IVAR_$_BRCFileUnlinker._internalDaemonContainerError
+ _OBJC_IVAR_$_BRCServerItem._isTrashed
+ _OBJC_IVAR_$_BRCSyncContext._activeOperationAdds
+ _OBJC_IVAR_$_BRCSyncContext._lastActivityDate
+ _OBJC_IVAR_$_BRCSystemResourcesManager._reclaimMemoryObservers
+ _OBJC_IVAR_$_BRCUserDefaults._localNSUserDefaultsDict
+ _OBJC_IVAR_$_BRCUserDefaultsManager._localNSUserDefaultsDict
+ _OBJC_METACLASS_$_BRCClientZoneActiveState
+ _OBJC_METACLASS_$_BRCRFAEmailSettingHandler
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ __BGSTBirdRateLimitConfigurationName
+ __OBJC_$_CLASS_METHODS_BRCRFAEmailSettingHandler
+ __OBJC_$_CLASS_METHODS_BRCSyncUpOperationBuilder
+ __OBJC_$_INSTANCE_METHODS_BRCClientZoneActiveState
+ __OBJC_$_INSTANCE_METHODS_BRCFileProvidingRequestOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRCClientZoneActiveState
+ __OBJC_$_PROP_LIST_BRCClientZoneActiveState
+ __OBJC_$_PROP_LIST_BRCSyncContextProvider
+ __OBJC_$_PROP_LIST_OSServerItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCReclaimMemoryDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OSServerItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OSServiceProviderProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SyncEngineProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRCReclaimMemoryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_OSServerItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_OSServiceProviderProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SyncEngineProtocol
+ __OBJC_$_PROTOCOL_REFS_BRCReclaimMemoryDelegate
+ __OBJC_$_PROTOCOL_REFS_OSServerItem
+ __OBJC_$_PROTOCOL_REFS_OSServiceProviderProtocol
+ __OBJC_$_PROTOCOL_REFS_SyncEngineProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BRCSyncContextProvider
+ __OBJC_CLASS_RO_$_BRCClientZoneActiveState
+ __OBJC_CLASS_RO_$_BRCRFAEmailSettingHandler
+ __OBJC_LABEL_PROTOCOL_$_BRCReclaimMemoryDelegate
+ __OBJC_LABEL_PROTOCOL_$_OSServerItem
+ __OBJC_LABEL_PROTOCOL_$_OSServiceProviderProtocol
+ __OBJC_LABEL_PROTOCOL_$_SyncEngineProtocol
+ __OBJC_METACLASS_RO_$_BRCClientZoneActiveState
+ __OBJC_METACLASS_RO_$_BRCRFAEmailSettingHandler
+ __OBJC_PROTOCOL_$_BRCReclaimMemoryDelegate
+ __OBJC_PROTOCOL_$_OSServerItem
+ __OBJC_PROTOCOL_$_OSServiceProviderProtocol
+ __OBJC_PROTOCOL_$_SyncEngineProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SyncEngineProtocol
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.77
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.77.cold.1
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.181
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.181.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.147
+ ___106-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]_block_invoke
+ ___106-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]_block_invoke.63
+ ___106-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]_block_invoke_2
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.153
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.153.cold.1
+ ___108-[BRCAccountSession fileProviderItemIdentifierForItemIdentifierString:zoneName:ownerName:completionHandler:]_block_invoke
+ ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.161
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.641
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.111
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.111.cold.1
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.111.cold.2
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.115
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.115.cold.1
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.116
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.116.cold.1
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.118
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.118.cold.1
+ ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.156
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.119
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.119.cold.1
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.121
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.121.cold.1
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.122
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.123
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke.127
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke_2
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke_2.124
+ ___113-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke_2.cold.1
+ ___115+[BRCServerChangesApplyUtil handleApplyChangesForUnliveServerItem:isDeleteOfShareRoot:rank:scheduler:zone:session:]_block_invoke.35
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.100
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.100.cold.1
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.102
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.104
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.109
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.109.cold.1
+ ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke.159
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.212
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.189
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.190
+ ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke
+ ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.281
+ ___132-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.cold.1
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.128
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.129
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.131
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke.133
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.130
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.132
+ ___138-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2.cold.1
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.43
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.47
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.49
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.1
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.2
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.3
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.4
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.56
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.60
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.60.cold.1
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.62
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.62.cold.1
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.63
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke.66
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2
+ ___143-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2.64
+ ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.246
+ ___18-[BRCDaemon start]_block_invoke.52
+ ___23-[BRCDaemon selfCheck:]_block_invoke.108
+ ___23-[BRCFileUnlinker init]_block_invoke
+ ___25-[BRCFSUploader schedule]_block_invoke.151
+ ___26-[BRCAccountSession close]_block_invoke.364
+ ___26-[BRCStageRegistry resume]_block_invoke.158
+ ___27-[BRCClientZone _startSync]_block_invoke.494
+ ___27-[BRCClientZone _startSync]_block_invoke.498
+ ___27-[BRCClientZone _startSync]_block_invoke.498.cold.1
+ ___27-[BRCClientZone _startSync]_block_invoke.498.cold.2
+ ___30-[BRCNotificationPipe __flush]_block_invoke.143
+ ___30-[BRCNotificationPipe __flush]_block_invoke.144
+ ___30-[BRCStageRegistry purgeSpace]_block_invoke
+ ___31-[BRCDiskSpaceReclaimer resume]_block_invoke
+ ___31-[BRCDiskSpaceReclaimer resume]_block_invoke.cold.1
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.41.cold.1
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.42
+ ___34-[BRCAccountsManager loadAccounts]_block_invoke.49
+ ___36-[BRCAccountSession _loadSyncEngine]_block_invoke
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.387
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.387.cold.1
+ ___39-[BRCClientZone addSyncDownDependency:]_block_invoke_2.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.537
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.538
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.538.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.538.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.538.cold.3
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.538.cold.4
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.544
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.544.cold.1
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.259
+ ___39-[BRCStageRegistry purgeGraveyardSpace]_block_invoke
+ ___39-[BRCSyncContextProvider reclaimMemory]_block_invoke
+ ___39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.87
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.116
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.116.cold.1
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.120
+ ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke_2.121
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.325
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.326
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.329
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.330
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.330.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.343
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.328.cold.2
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.334
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.338
+ ___41-[BRCSyncContext reclaimMemoryIfPossible]_block_invoke
+ ___41-[BRCSyncContext reclaimMemoryIfPossible]_block_invoke_2
+ ___41-[BRCSyncContext reclaimMemoryIfPossible]_block_invoke_2.cold.1
+ ___42-[BRCClientZone removeSyncDownDependency:]_block_invoke.cold.1
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.263
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.263.cold.1
+ ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.136
+ ___44-[BRCSyncContext _setupUploadStreamIfNeeded]_block_invoke
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.389.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.396
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.396.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.399
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.421
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.421.cold.1
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.327
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.327.cold.1
+ ___46-[BRCFSUploader rescheduleJobsPendingCellular]_block_invoke.110
+ ___46-[BRCStageRegistry workDirectoryForSyncEngine]_block_invoke
+ ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.453
+ ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.336
+ ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.77
+ ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.597
+ ___47-[BRCNotificationPipe processUpdates:withRank:]_block_invoke.141
+ ___47-[BRCSyncContext _setupDownloadStreamsIfNeeded]_block_invoke
+ ___47-[BRCSyncContext _setupDownloadStreamsIfNeeded]_block_invoke.49
+ ___47-[BRCSyncContext _setupDownloadStreamsIfNeeded]_block_invoke_2
+ ___47-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke
+ ___47-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke.29
+ ___47-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke_2
+ ___47-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke_3
+ ___47-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke_3.cold.1
+ ___48+[BRCUserDefaults _personaToUserDefaultsManager]_block_invoke
+ ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.231
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.94
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.94.cold.1
+ ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.100
+ ___49-[BRCAccountSession serverItemForItemIdentifier:]_block_invoke
+ ___49-[BRCAccountSession serverItemForItemIdentifier:]_block_invoke_2
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.643
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.644
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.645
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.650
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.518
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.304.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.308
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.318.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.322
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.305
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.1
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.2
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.3
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.312.cold.4
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2.319
+ ___51-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_3
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.429
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.430
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.431
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.272
+ ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.234
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.497
+ ___53-[BRCXPCRegularIPCsClient reclaimDiskSpaceWithReply:]_block_invoke
+ ___54-[BRCClientZone waitForSyncDownWithCompletionHandler:]_block_invoke
+ ___54-[BRCClientZone waitForSyncDownWithCompletionHandler:]_block_invoke.cold.1
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.169
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.169.cold.1
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.170
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.170.cold.1
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.171
+ ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.171.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.91
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.91.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.91.cold.2
+ ___54-[BRCSystemResourcesManager addReclaimMemoryObserver:]_block_invoke
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.408
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.409
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.446
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.447
+ ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.437
+ ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.437.cold.1
+ ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.396
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.16
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.16.cold.1
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.16.cold.2
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.16.cold.3
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.16.cold.4
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.30.cold.1
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.30.cold.2
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.30.cold.3
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.30.cold.4
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.30.cold.5
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.31
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.37.cold.1
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.37.cold.2
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.37.cold.3
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.37.cold.4
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.37.cold.5
+ ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.38
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.19
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.22
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.1
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.2
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.3
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.4
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.5
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.6
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke.cold.7
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke_2
+ ___56-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke_2.23
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.366
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.367
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.663
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.663.cold.1
+ ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.292
+ ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.294
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.728
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.728.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.728.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.729
+ ___57-[BRCSystemResourcesManager removeReclaimMemoryObserver:]_block_invoke
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.345
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.346
+ ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.42
+ ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.42.cold.1
+ ___58-[BRCXPCRegularIPCsClient computePurgeableSpaceWithReply:]_block_invoke
+ ___58-[BRCXPCRegularIPCsClient computePurgeableSpaceWithReply:]_block_invoke.411
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.459.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.466
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.468
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.416
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.417
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.435
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.435.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.724
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.724.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.726
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.727
+ ___59-[BRCDatabaseFacade serverItemFromClientRowID:itemBuilder:]_block_invoke
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.33
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.33.cold.1
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.35
+ ___59-[BRCXPCRegularIPCsClient setRFAEmailSettingEnabled:reply:]_block_invoke
+ ___59-[BRCXPCRegularIPCsClient setRFAEmailSettingEnabled:reply:]_block_invoke.352
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.434
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.435
+ ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.47
+ ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.50
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.1
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.2
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.3
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.4
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.5
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.6
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.153.cold.7
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.163
+ ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.169
+ ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke.137
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.609
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.609.cold.1
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.248
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.251
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.546
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.546.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.546.cold.2
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.548
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.551
+ ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke.191
+ ___61-[BRCXPCRegularIPCsClient isRFAEmailSettingEnabledWithReply:]_block_invoke
+ ___61-[BRCXPCRegularIPCsClient isRFAEmailSettingEnabledWithReply:]_block_invoke.353
+ ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke.148
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.604
+ ___63-[BRCClientZone _activateZoneActiveStateIfNeededWithOrigState:]_block_invoke
+ ___63-[BRCClientZone _activateZoneActiveStateIfNeededWithOrigState:]_block_invoke_2
+ ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke.463
+ ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke.463.cold.1
+ ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke.463.cold.2
+ ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke_2
+ ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke_2.cold.1
+ ___63-[BRCClientZone(BRCZoneReset) scheduleReset:completionHandler:]_block_invoke.11
+ ___63-[BRCClientZone(BRCZoneReset) scheduleReset:completionHandler:]_block_invoke.11.cold.1
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.96
+ ___64-[BRCUserDefaultsManager _setServerConfigurationURL:whenLoaded:]_block_invoke.253
+ ___64-[BRCXPCRegularIPCsClient handleUserNotificationResponse:reply:]_block_invoke
+ ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.395
+ ___65-[BRCAccountsManager updateAccountDisplayName:completionHandler:]_block_invoke.70
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.225
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.226
+ ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.661
+ ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.305
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.657
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.657.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.657.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.658
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.451
+ ___66-[BRCFetchRecordSubResourcesOperation saveRecordsWithQueryCursor:]_block_invoke.55
+ ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke.182
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.611
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.612
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.614
+ ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.142
+ ___67-[BRCAccountSession shouldPCSChainItem:zoneName:completionHandler:]_block_invoke
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.425
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.425.cold.1
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke.86
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke_2.87
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.730
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.731
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.158
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.162
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.162.cold.1
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_2.160
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.161
+ ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.161.cold.1
+ ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.329
+ ___69-[BRCAccountSession invokePCSChainOnItem:zoneName:completionHandler:]_block_invoke
+ ___69-[BRCAccountSession invokePCSChainOnItem:zoneName:completionHandler:]_block_invoke_2
+ ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.312
+ ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.410
+ ___70+[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:]_block_invoke
+ ___70+[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:]_block_invoke.cold.1
+ ___70-[BRCAccountSession serverItemWithParent:filename:zoneName:ownerName:]_block_invoke
+ ___70-[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:]_block_invoke
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.645
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.647
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.647.cold.1
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.648
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.648.cold.1
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.738
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.739
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.747
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.747.cold.1
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.707
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.653
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.134
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.138
+ ___71-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke
+ ___71-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.130
+ ___71-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.cold.1
+ ___72+[BRCRFAEmailSettingHandler isEmailSettingEnabledWithSyncContext:reply:]_block_invoke
+ ___72+[BRCRFAEmailSettingHandler isEmailSettingEnabledWithSyncContext:reply:]_block_invoke_2
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.605
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.599
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.210
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke.152
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke.150
+ ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2.151
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.402
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.402.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.403
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.403.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.404
+ ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.662
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.368
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.384
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.574
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.576
+ ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.214
+ ___74-[BRCAccountSession generateRequestIDForZone:ownerName:completionHandler:]_block_invoke
+ ___74-[BRCAccountSession serverItemForItemIdentifierString:zoneName:ownerName:]_block_invoke
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.84
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.90
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.95
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.91
+ ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.97
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.618
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.620
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397.cold.1
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.397.cold.2
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.398
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.398.cold.1
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.615
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.616
+ ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke
+ ___75-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke.215
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.739
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.743
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.741
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.175
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.175.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.176
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.176.cold.1
+ ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.176.cold.2
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.607
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.607.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.571
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.602
+ ___77-[BRCAccountSession recoverAndReportNamespaceAndContentPolicyWithCompletion:]_block_invoke
+ ___77-[BRCAccountSession recoverAndReportNamespaceAndContentPolicyWithCompletion:]_block_invoke_2
+ ___77-[BRCAccountSession recoverAndReportNamespaceAndContentPolicyWithCompletion:]_block_invoke_3
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke.190
+ ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke.189
+ ___77-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:doNotObfuscate:reply:]_block_invoke
+ ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.414
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.175
+ ___79-[BRCAccountSession hasSyncedDownZoneSinceStartup:ownerName:completionHandler:]_block_invoke
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33.cold.1
+ ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.33.cold.2
+ ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.347
+ ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.348
+ ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.349
+ ___80-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke.49
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.562
+ ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.325
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.448
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.449
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.61.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.64.cold.1
+ ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.65
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.637
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.573
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.639
+ ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.66
+ ___83-[BRCAccountSession enableEnhancedDrivePrivacyForZone:ownerName:completionHandler:]_block_invoke
+ ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke
+ ___83-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.486
+ ___83-[BRCProgress _setupDownloadProgressForDocument:totalUnitCount:completedUnitCount:]_block_invoke.40
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.427
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.427.cold.1
+ ___84-[BRCNotificationPipe __performBlockafterDBAndNotifFlush:session:description:error:]_block_invoke.148
+ ___84-[BRCNotificationPipe __performBlockafterDBAndNotifFlush:session:description:error:]_block_invoke_2.149
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.499
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.499.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.499.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.499.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.503
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.513
+ ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.699
+ ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.700
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.643
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.163
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.164
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.164.cold.1
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.457
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.458
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.197
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.203
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.171
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.514
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.516
+ ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.301
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.139
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.141
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.68
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.68.cold.1
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.70
+ ___87-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke
+ ___87-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke.cold.1
+ ___87-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke.cold.2
+ ___87-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke.cold.3
+ ___87-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke.cold.4
+ ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.69
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.578
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke.105
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.155
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.177
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.184
+ ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.625
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.581
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.582
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.583
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.584
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.585
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.594
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.591
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.178
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.204
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.205
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.629
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.169
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.169.cold.1
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.158
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.170
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.355
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.356
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.357
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.302
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.308
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.308.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.309
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.306
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.306.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.310
+ ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.675
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.358
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.359
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.360
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.672
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.675
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.675.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.675.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.678
+ ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.441
+ ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.441.cold.1
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.688
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.696
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.173
+ ___96-[BRCFileProvidingRequestOperation initWithDocumentItem:sessionContext:downloadTrackersManager:]_block_invoke
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.189
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.157
+ ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.242
+ ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke
+ ___99-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke.484
+ ___99-[BRCAccountSession updatePCSStateForItemIdentifier:newState:zoneName:ownerName:completionHandler:]_block_invoke
+ ___99-[BRCMigrationQueryOperation _updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke
+ ___99-[BRCMigrationQueryOperation _updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke_2
+ ___99-[BRCMigrationQueryOperation _updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke_3
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104bs_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s104l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104bs112r_e5_B8?0ls32l8s40l8r112l8s48l8s56l8s64l8s104l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s112l8s88l8s96l8s104l8
+ ___block_descriptor_148_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e17_B16?0"NSError"8ls32l8s40l8s48l8s120l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
+ ___block_descriptor_164_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs_e5_v8?0ls32l8s40l8s48l8s136l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
+ ___block_descriptor_32_e41_v32?0"NSString"8"BRCSyncContext"16^B24l
+ ___block_descriptor_32_e8_i12?0i8l
+ ___block_descriptor_40_e8_32bs_e35_v24?0"CKQueryCursor"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e16_v16?0"NSData"8lr32l8
+ ___block_descriptor_40_e8_32s_e31_v24?0"NSNumber"8"NSNumber"16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e39_v36?0"BRQueryItem"8Q16B24"NSError"28lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v32?0"NSNumber"8"NSNumber"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e35_v24?0"CKQueryCursor"8"NSError"16lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32r40r_e17_B16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_64_e8_32s40r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_B8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e42_v16?0"BRCReadWriteServerDatabaseFacade"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56bs64bs72bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s64l8s48l8s72l8u80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e48_v36?0"<NSFileProviderItem>"8Q16B24"NSError"28ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.101
+ ___block_literal_global.1031
+ ___block_literal_global.107
+ ___block_literal_global.112
+ ___block_literal_global.136
+ ___block_literal_global.1606
+ ___block_literal_global.1751
+ ___block_literal_global.1763
+ ___block_literal_global.183
+ ___block_literal_global.192
+ ___block_literal_global.1928
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.2080
+ ___block_literal_global.2115
+ ___block_literal_global.2126
+ ___block_literal_global.2262
+ ___block_literal_global.2288
+ ___block_literal_global.2307
+ ___block_literal_global.2310
+ ___block_literal_global.2319
+ ___block_literal_global.2328
+ ___block_literal_global.2383
+ ___block_literal_global.2407
+ ___block_literal_global.2423
+ ___block_literal_global.2504
+ ___block_literal_global.252
+ ___block_literal_global.256
+ ___block_literal_global.264
+ ___block_literal_global.27
+ ___block_literal_global.2850
+ ___block_literal_global.299
+ ___block_literal_global.314
+ ___block_literal_global.321
+ ___block_literal_global.33
+ ___block_literal_global.366
+ ___block_literal_global.374
+ ___block_literal_global.386
+ ___block_literal_global.398
+ ___block_literal_global.40
+ ___block_literal_global.410
+ ___block_literal_global.432
+ ___block_literal_global.439
+ ___block_literal_global.443
+ ___block_literal_global.504
+ ___block_literal_global.52
+ ___block_literal_global.564
+ ___block_literal_global.57
+ ___block_literal_global.599
+ ___block_literal_global.650
+ ___block_literal_global.672
+ ___block_literal_global.76
+ ___block_literal_global.764
+ ___block_literal_global.80
+ ___block_literal_global.85
+ ___block_literal_global.86
+ ___block_literal_global.88
+ ___br_fixup_namspace_and_contentPolicy_block_invoke
+ ___br_fixup_namspace_and_contentPolicy_block_invoke_2
+ ___br_fixup_namspace_and_contentPolicy_block_invoke_2.cold.1
+ __loadSyncEngine.library
+ __loadSyncEngine.onceToken
+ __loadSyncEngine.syncEngineClass
+ __personaToUserDefaultsManager.once
+ __personaToUserDefaultsManager.personaToUserDefaultsManager
+ _br_update_tables_34_100
+ _br_update_tables_34_101
+ _br_update_tables_5_000.cold.3
+ _br_update_tables_5_000.cold.4
+ _initWithDocumentItem:sessionContext:downloadTrackersManager:.onceToken
+ _initWithDocumentItem:sessionContext:downloadTrackersManager:.queue
+ _kBRQueryItemDLErrorKey
+ _objc_msgSend$__performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:
+ _objc_msgSend$_activateZoneActiveStateIfNeededWithOrigState:
+ _objc_msgSend$_addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:
+ _objc_msgSend$_addSubOperation:overrideContext:allowsCellularAccess:
+ _objc_msgSend$_cacheValueLocally:forKey:
+ _objc_msgSend$_cancelAndWaitForRunningOperations:dispatchOnDbQueue:
+ _objc_msgSend$_checkIfShouldDedicateOpToPCSChainingItem:fullyChainedParentIDs:
+ _objc_msgSend$_checkLocalCacheForKey:inherit:validateWithBlock:
+ _objc_msgSend$_checkLocalNSUserDefaultsForKey:validateWithBlock:
+ _objc_msgSend$_checkServerOverrideForKey:validateWithBlock:
+ _objc_msgSend$_clearErrorForRecord:inZone:
+ _objc_msgSend$_closeHandlersAndBarriersBlocks
+ _objc_msgSend$_computeIsTrashed
+ _objc_msgSend$_deferredPlistFromPlist:
+ _objc_msgSend$_downloadGroupContainerStageSize
+ _objc_msgSend$_garbageCollectSpace
+ _objc_msgSend$_getPrivateClientZone
+ _objc_msgSend$_handleGlobalFallbackForKey:validateWithBlock:
+ _objc_msgSend$_hasAnyItemInZoneOtherThanDocumentsFolder
+ _objc_msgSend$_initReclaimMemory
+ _objc_msgSend$_initWithItemID:ownerKey:sideCarCKInfo:st:latestVersion:serverMetrics:serverZone:clientZone:session:sharingOptions:pcsChainState:
+ _objc_msgSend$_initWithSyncBubble:
+ _objc_msgSend$_initializeZoneActiveStateIfNeeded
+ _objc_msgSend$_invalidateReclaimMemory
+ _objc_msgSend$_invalidateZoneActiveStateIfNeeded
+ _objc_msgSend$_isResetting
+ _objc_msgSend$_loadSyncEngine
+ _objc_msgSend$_localItemFromRecord:inZone:validateSyncUpState:
+ _objc_msgSend$_memoryOptimizationEnabled
+ _objc_msgSend$_moveOldUnlinkDir
+ _objc_msgSend$_nillifyMembers
+ _objc_msgSend$_personaToUserDefaultsManager
+ _objc_msgSend$_prepopulateLocalNSUserDefaults
+ _objc_msgSend$_purgeSpaceUnderQueue
+ _objc_msgSend$_reclaimMemoryFromObserversDueToMemoryPressure:
+ _objc_msgSend$_recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:
+ _objc_msgSend$_registerBackgroundSystemTasks
+ _objc_msgSend$_sendCachedStatementsCountTelemetryEvent
+ _objc_msgSend$_sendZoneResetAnalyticsAndTTRForError:resetReason:alternativeError:
+ _objc_msgSend$_setupCKContainerIfNeeded
+ _objc_msgSend$_setupDownloadStreamsIfNeeded
+ _objc_msgSend$_setupOperationQueuesIfNeeded
+ _objc_msgSend$_setupUploadStreamIfNeeded
+ _objc_msgSend$_updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:
+ _objc_msgSend$addOperation:allowsCellularAccess:
+ _objc_msgSend$addReclaimMemoryObserver:
+ _objc_msgSend$addToPlist:
+ _objc_msgSend$allItemsDidUploadTrackers
+ _objc_msgSend$alloc
+ _objc_msgSend$appliedTombstoneRanks
+ _objc_msgSend$blockedOperationsOnInitialSync
+ _objc_msgSend$br_isFileType
+ _objc_msgSend$br_rsaEmailSettingRetrieve
+ _objc_msgSend$br_rsaEmailSettingUpdate
+ _objc_msgSend$br_structureEtag
+ _objc_msgSend$br_syncUpForPCSChain
+ _objc_msgSend$brc_containerResetErrorForSharedZone:resetReason:matchedError:
+ _objc_msgSend$brc_errorZoneResetCrashRecovery
+ _objc_msgSend$brc_errorZoneResetHierarchyTooDeep
+ _objc_msgSend$brc_errorZoneResetOrphanLive
+ _objc_msgSend$brc_errorZoneResetOrphanTombstone
+ _objc_msgSend$brc_errorZoneResetStillWantsDataUnlinked
+ _objc_msgSend$brc_errorZoneResetZoneBecameHealthy
+ _objc_msgSend$bubbleSyncTask
+ _objc_msgSend$checkIfShouldDedicateOpToPCSChainingItem:
+ _objc_msgSend$clientZoneMemoryOptimizationEnabled
+ _objc_msgSend$computePurgeableSpaceWithReply:
+ _objc_msgSend$contentAndNamespacePolicyForItemInfo:sessionContext:contentPolicy:namespacePolicy:
+ _objc_msgSend$contentAndNamespacePolicyForRootContainerWithSessionContext:contentPolicy:namespacePolicy:
+ _objc_msgSend$createItemBasedOnTemplate:createItemContext:fields:contents:options:request:completionHandler:
+ _objc_msgSend$createPCSChainOperationForItem:
+ _objc_msgSend$currentSyncDownBarriers
+ _objc_msgSend$dbFixupNamespaceAndContentPolicyRecoverAfterTimeInterval
+ _objc_msgSend$decreaseSyncUpBatchSizeAfterError
+ _objc_msgSend$deleteItemWithIdentifier:baseVersion:options:request:completionHandler:
+ _objc_msgSend$directoriesCreatedLastSyncUp
+ _objc_msgSend$diskSpaceReclaimedThresholdForSendingTelemetry
+ _objc_msgSend$distinctCachedStatementsCount
+ _objc_msgSend$downloadedBlockToPerformForItemID
+ _objc_msgSend$downloadingError
+ _objc_msgSend$extendedAttributesDictionary
+ _objc_msgSend$faultsLiveBarriers
+ _objc_msgSend$fetchAndClearSyncStateBits:
+ _objc_msgSend$fetchAndSetSyncStateBits:
+ _objc_msgSend$fetchParentOperations
+ _objc_msgSend$fetchRecentsOperation
+ _objc_msgSend$fetchRootItemIDAboveItemID:zoneRowID:serverTruth:itemState:depth:itemType:
+ _objc_msgSend$fetchShareRootItemIDWithSharedChildItemID:zoneRowID:serverTruth:
+ _objc_msgSend$fpfsNamespacePolicyEnabled
+ _objc_msgSend$garbageCollectSpace
+ _objc_msgSend$graveyardAgeDelta
+ _objc_msgSend$hasUnresolvedConflicts
+ _objc_msgSend$ignoredInternalCloudDocsErrorCodesForABCInReset
+ _objc_msgSend$increaseSyncUpBatchSizeAfterSuccess
+ _objc_msgSend$initAsGlobalWithServerConfiguration:localNSUserDefaultsDict:
+ _objc_msgSend$initUploadProgressForDocument:totalUnitCount:completedUnitCount:
+ _objc_msgSend$initWithAccountID:osServiceProvider:workDirectory:
+ _objc_msgSend$initWithDocumentItem:sessionContext:downloadTrackersManager:
+ _objc_msgSend$initWithDocumentItem:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:
+ _objc_msgSend$initWithFileProviderItem:appLibraryID:
+ _objc_msgSend$initWithMangledID:
+ _objc_msgSend$initWithReserverItemIDString:reservedFileProviderIdentifier:parentZoneName:parentZoneOwner:parentIdentifier:primaryZoneNeedsCreation:symlinkTarget:
+ _objc_msgSend$initWithServerConfiguration:globalUserDefaults:localNSUserDefaultsDict:clientZoneIdentifier:
+ _objc_msgSend$initWithShareMetadata:sessionContext:userNotifier:userActionsNavigator:
+ _objc_msgSend$initWithUploadProgress:
+ _objc_msgSend$internalDaemonContainerPathWithError:
+ _objc_msgSend$invokeFetchRecentsOperation
+ _objc_msgSend$isDownloaded
+ _objc_msgSend$isEmailSettingEnabledWithSyncContext:reply:
+ _objc_msgSend$isMostRecentVersionDownloaded
+ _objc_msgSend$isTrashed
+ _objc_msgSend$isUploaded
+ _objc_msgSend$isUploading
+ _objc_msgSend$lastSyncDownError
+ _objc_msgSend$lastSyncUpError
+ _objc_msgSend$lastSyncUpErrorWasOnChainedItem
+ _objc_msgSend$locateBlocksToPerformForRecordID
+ _objc_msgSend$locateRecordOperations
+ _objc_msgSend$locateRecordsOperationThrottle
+ _objc_msgSend$markRequestIDAcked
+ _objc_msgSend$memoryReclaimerBGSystemTaskConfig
+ _objc_msgSend$memoryReclaimerBGSystemTaskEnabled
+ _objc_msgSend$modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:
+ _objc_msgSend$namespacePolicy
+ _objc_msgSend$newClientDBCachedStatementsCountEventWithValue:
+ _objc_msgSend$newDiskSpaceReclaimedBytes:
+ _objc_msgSend$nextIdleHandlers
+ _objc_msgSend$nextSyncDownBarriers
+ _objc_msgSend$notifyContainer:isForegroundState:
+ _objc_msgSend$obfuscatedDescription
+ _objc_msgSend$onDiskBlockToPerformForItemID
+ _objc_msgSend$operationCount
+ _objc_msgSend$outOfBandSyncOperations
+ _objc_msgSend$periodicCacheDeleteBGSystemTaskConfig
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$postContainerStatusChangeNotificationForKey:value:
+ _objc_msgSend$privateFrameworksURL
+ _objc_msgSend$publish
+ _objc_msgSend$purgeGraveyardSpace
+ _objc_msgSend$purgeSpace
+ _objc_msgSend$reclaimMemory
+ _objc_msgSend$reclaimMemoryIfPossible
+ _objc_msgSend$recoverAndReportNamespaceAndContentPolicyWithCompletion:
+ _objc_msgSend$recursiveListOperations
+ _objc_msgSend$removeReclaimMemoryObserver:
+ _objc_msgSend$resetAfterAppUninstallTimer
+ _objc_msgSend$resetNotifications
+ _objc_msgSend$resetTimer
+ _objc_msgSend$resumeWithTapToRadarManager:
+ _objc_msgSend$runningListOperations
+ _objc_msgSend$scheduleResetServerAndClientTruthsWithError:
+ _objc_msgSend$scheduleResetServerAndClientTruthsWithError:completionHandler:
+ _objc_msgSend$serverItemFromClientRowID:itemBuilder:
+ _objc_msgSend$serverStitchingOperationThrottle
+ _objc_msgSend$setAllItemsDidUploadTrackers:
+ _objc_msgSend$setAppliedTombstoneRanks:
+ _objc_msgSend$setBubbleSyncTask:
+ _objc_msgSend$setDownloadedBlockToPerformForItemID:
+ _objc_msgSend$setEmailSettingEnabled:syncContext:reply:
+ _objc_msgSend$setFaultsLiveBarriers:
+ _objc_msgSend$setFetchRecentsOperation:
+ _objc_msgSend$setInvokeFetchRecentsOperation:
+ _objc_msgSend$setItemNeedingPCSChaining:
+ _objc_msgSend$setLastInsertedRank:
+ _objc_msgSend$setLastSyncDownError:
+ _objc_msgSend$setLastSyncUpError:
+ _objc_msgSend$setLastSyncUpErrorWasOnChainedItem:
+ _objc_msgSend$setLocateBlocksToPerformForRecordID:
+ _objc_msgSend$setNextIdleHandlers:
+ _objc_msgSend$setNextSyncDownBarriers:
+ _objc_msgSend$setOnDiskBlockToPerformForItemID:
+ _objc_msgSend$setOsNameRequiredToSync:
+ _objc_msgSend$setParentZoneEtag:
+ _objc_msgSend$setRequestID:
+ _objc_msgSend$setResetAfterAppUninstallTimer:
+ _objc_msgSend$setResetTimer:
+ _objc_msgSend$setSideCarEtag:
+ _objc_msgSend$setSyncDeadlineSource:
+ _objc_msgSend$setSyncDeadlineSourceResumer:
+ _objc_msgSend$setSyncDownBlockToPerformForBookmarkData:
+ _objc_msgSend$setSyncDownBlockToPerformForItemID:
+ _objc_msgSend$setSyncDownCompletionHandlers:
+ _objc_msgSend$setSyncDownGroup:
+ _objc_msgSend$setSyncDownOperation:
+ _objc_msgSend$setSyncUpOperation:
+ _objc_msgSend$setSyncUpRetryAfter:
+ _objc_msgSend$setZoneRowID:
+ _objc_msgSend$shouldPCSChainItem:completionHandler:
+ _objc_msgSend$syncContextIdleTimeBeforeMemoryReclaim
+ _objc_msgSend$syncDeadlineSourceResumer
+ _objc_msgSend$syncDownBlockToPerformForBookmarkData
+ _objc_msgSend$syncDownBlockToPerformForItemID
+ _objc_msgSend$syncDownCompletionHandlers
+ _objc_msgSend$syncDownDependencies
+ _objc_msgSend$syncDownGroup
+ _objc_msgSend$syncDownOperation
+ _objc_msgSend$syncEngine
+ _objc_msgSend$syncEngineMarkForceIdleWithVersion:
+ _objc_msgSend$syncUpOperation
+ _objc_msgSend$syncUpRetryAfter
+ _objc_msgSend$topLevelSharedItemID
+ _objc_msgSend$trashItemIDWithFacade:
+ _objc_msgSend$unpublish
+ _objc_msgSend$updateFromPlist:
+ _objc_msgSend$updateWithPlist:isDeferredPlist:
+ _objc_msgSend$uploadV2Enabled
+ _objc_msgSend$uploadingError
+ _objc_msgSend$waitForSyncDownWithCompletionHandler:
+ _objc_msgSend$workDirectoryForSyncEngine
+ _reclaimMemoryIfPossible.onceToken
+ _reclaimMemoryIfPossible.specialContainers
- +[BRCDiskSpaceReclaimer accessTimeDeltaForUrgency:]
- +[BRCDiskSpaceReclaimer simpleUrgencyForCacheDeleteUrgency:]
- +[BRCProgress _progressForDocument:group:totalUnitCount:completedUnitCount:]
- +[BRCProgress progressToReplaceUploadProgress:]
- +[BRCProgress progressToReplaceUploadProgress:].cold.1
- +[BRCProgress uploadProgressForDocument:totalUnitCount:completedUnitCount:]
- +[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]
- +[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:].cold.1
- +[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:].cold.2
- +[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:].cold.3
- +[BRCServerChangesApplyUtil shouldForceApplyContentForItem:]
- +[BRCServerChangesApplyUtil_Private localItemHasUnsyncedChanges:si:rank:scheduler:clientZone:zone:isDeleteOfShareRoot:session:].cold.7
- +[BRCSyncContext _contextIdentifierForMangledID:metadata:]
- +[BRCUploadSyncUpRequestsManager _fetchManagersDictionary]
- +[BRCUploadSyncUpRequestsManager _fetchManagersDictionary].cold.1
- +[BRCUploadSyncUpRequestsManager defaultManagerWithPersonaIdentifier:]
- +[BRCUserDefaults _userDefaultsManager].cold.1
- -[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]
- -[BRCAccountSession _registerBackgroundXPCActivities]
- -[BRCAccountSession recoverAndReportContentPolicyWithCompletion:]
- -[BRCBGSystemTaskContext addReference]
- -[BRCBGSystemTaskContext initWithOptions:]
- -[BRCBGSystemTaskContext options]
- -[BRCBGSystemTaskContext releaseReference]
- -[BRCBGSystemTaskContext setOptions:]
- -[BRCClientZone _decreaseSyncUpBatchSizeAfterError]
- -[BRCClientZone _increaseSyncUpBatchSizeAfterSuccess]
- -[BRCClientZone _recreateSyncBudgetsAndThrottlesIfNeeded]
- -[BRCClientZone close].cold.2
- -[BRCClientZone close].cold.3
- -[BRCClientZone close].cold.4
- -[BRCClientZone itemIDsBlockedFromSyncForCZMProcessing]
- -[BRCClientZone parentsOfCZMFaults]
- -[BRCClientZone scheduleResetServerAndClientTruthsForReason:]
- -[BRCClientZone scheduleResetServerAndClientTruthsForReason:completionHandler:]
- -[BRCClientZone scheduleResetServerAndClientTruthsForReason:completionHandler:].cold.1
- -[BRCClientZone scheduleResetServerAndClientTruthsForReason:completionHandler:].cold.2
- -[BRCClientZone updateWithPlist:].cold.1
- -[BRCDaemon _setupCacheDelete]
- -[BRCDaemon resumeIPCAcceptation]
- -[BRCDaemon suspendIPCAcceptation]
- -[BRCDataOrDocsScopeGatherer invalidate].cold.1
- -[BRCDiskSpaceReclaimer _asyncAutovacuumIfNeeds:]
- -[BRCDiskSpaceReclaimer _purgeSpaceUnderQueue:withUrgency:]
- -[BRCDiskSpaceReclaimer _purgeSpaceUnderQueue:withUrgency:].cold.1
- -[BRCDiskSpaceReclaimer _purgeSpaceUnderQueue:withUrgency:].cold.2
- -[BRCDiskSpaceReclaimer _vacuumDB:amount:withUrgency:]
- -[BRCDiskSpaceReclaimer cachedNonPurgeableSpace]
- -[BRCDiskSpaceReclaimer cachedPurgeableSpaceForUrgency:]
- -[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]
- -[BRCDiskSpaceReclaimer performOptimizeStorageWithTimeDelta:onDiskAccessTimeDelta:error:]
- -[BRCDiskSpaceReclaimer performOptimizeStorageWithTimeDelta:onDiskAccessTimeDelta:error:].cold.1
- -[BRCDiskSpaceReclaimer purgeSpace:withUrgency:]
- -[BRCDiskSpaceReclaimer renameAndUnlinkInBackgroundItemAt:path:]
- -[BRCDiskSpaceReclaimer urgencyForCacheDeleteUrgency:]
- -[BRCDocumentItem downloadStatus]
- -[BRCFileProviderDaemonUtils _initWithSyncBubble:isFPFS:]
- -[BRCFileProvidingRequestOperation initWithDocumentItem:client:sessionContext:downloadTrackersManager:]
- -[BRCFileProvidingRequestOperation initWithDocumentItem:client:sessionContext:downloadTrackersManager:].cold.1
- -[BRCFileProvidingRequestOperation(FPFSAdditions) initWithDocumentItem:client:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:]
- -[BRCFileUnlinker initWithCacheDirPath:]
- -[BRCFileUnlinker resume]
- -[BRCFileUnlinker resume].cold.1
- -[BRCLocalStatInfo checkStateWithItemID:logToFile:]
- -[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]
- -[BRCMigrationQueryOperation _updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:]
- -[BRCNotification aliasSourceAppLibraryID]
- -[BRCNotification generateLogicalExtension:physicalExtension:]
- -[BRCNotification generateLogicalExtension:physicalExtension:].cold.1
- -[BRCNotification generateLogicalExtension:physicalExtension:].cold.2
- -[BRCPipeline .cxx_destruct]
- -[BRCPipeline _armResumeTimer]
- -[BRCPipeline _buildJobPlanForJob:error:]
- -[BRCPipeline _buildJobPlanForJob:error:].cold.1
- -[BRCPipeline _buildJobPlanForJob:error:].cold.2
- -[BRCPipeline _buildJobPlanForJob:error:].cold.3
- -[BRCPipeline _completedJob:forStage:recoveryStage:error:]
- -[BRCPipeline _completedJob:forStage:recoveryStage:error:].cold.1
- -[BRCPipeline _computeStageStringifier]
- -[BRCPipeline _generateProgressForJob:]
- -[BRCPipeline _pauseStageHandlerScheduling]
- -[BRCPipeline _resumeStageHandlerScheduling]
- -[BRCPipeline _sendJob:toStageHandlerWithStageID:]
- -[BRCPipeline _sendJob:toStageHandlerWithStageID:].cold.1
- -[BRCPipeline _setStageJobCompletionHandlers]
- -[BRCPipeline _validateStageHandlers]
- -[BRCPipeline addJob:moreComing:]
- -[BRCPipeline description]
- -[BRCPipeline dumpToContext:]
- -[BRCPipeline initWithName:stageHandlers:]
- -[BRCPipelineJob .cxx_destruct]
- -[BRCPipelineJob initWithCompletionHandler:]
- -[BRCPipelineJob initWithQualityOfService:completionHandler:]
- -[BRCPipelineJob qualityOfService]
- -[BRCPipelineJob subclassDescription]
- -[BRCPipelineJob(InternalPipeline) activeStageID]
- -[BRCPipelineJob(InternalPipeline) advanceJobToInitialStage]
- -[BRCPipelineJob(InternalPipeline) advanceJobToInitialStage].cold.1
- -[BRCPipelineJob(InternalPipeline) advanceJobToNextStage]
- -[BRCPipelineJob(InternalPipeline) advanceJobToNextStage].cold.1
- -[BRCPipelineJob(InternalPipeline) advanceJobToNextStage].cold.2
- -[BRCPipelineJob(InternalPipeline) advanceToRecoveryStage:]
- -[BRCPipelineJob(InternalPipeline) advanceToRecoveryStage:].cold.1
- -[BRCPipelineJob(InternalPipeline) completeWithError:]
- -[BRCPipelineJob(InternalPipeline) completeWithError:].cold.1
- -[BRCPipelineJob(InternalPipeline) descriptionWithContext:]
- -[BRCPipelineJob(InternalPipeline) description]
- -[BRCPipelineJob(InternalPipeline) dumpToContext:]
- -[BRCPipelineJob(InternalPipeline) jobPlan]
- -[BRCPipelineJob(InternalPipeline) setJobPlan:additionalToRequestingStageMap:]
- -[BRCPipelineJob(InternalPipeline) setJobPlan:additionalToRequestingStageMap:].cold.1
- -[BRCPipelineJob(InternalPipeline) setStageStringifier:]
- -[BRCPipelineJobQueue .cxx_destruct]
- -[BRCPipelineJobQueue addJob:withGroupIdentifier:]
- -[BRCPipelineJobQueue dequeueHighestQualityOfServiceJobsWithHandler:]
- -[BRCPipelineJobQueue dequeueHighestQualityOfServiceJobsWithHandler:].cold.1
- -[BRCPipelineJobQueue dumpToContext:]
- -[BRCPipelineJobQueue init]
- -[BRCPipelineJobQueue removeJob:withGroupIdentifier:]
- -[BRCPipelineStageHandlerBase .cxx_destruct]
- -[BRCPipelineStageHandlerBase _asJobCostVendor]
- -[BRCPipelineStageHandlerBase _cancelActiveBatchIfNecessary]
- -[BRCPipelineStageHandlerBase _cancelActiveBatchIfNecessary].cold.1
- -[BRCPipelineStageHandlerBase _cancelActiveBatchIfNecessary].cold.2
- -[BRCPipelineStageHandlerBase _completedJob:withRecoveryStage:error:]
- -[BRCPipelineStageHandlerBase _completedJob:withRecoveryStage:error:].cold.1
- -[BRCPipelineStageHandlerBase _pauseScheduling]
- -[BRCPipelineStageHandlerBase _resumeScheduling]
- -[BRCPipelineStageHandlerBase dealloc]
- -[BRCPipelineStageHandlerBase init]
- -[BRCPipelineStageHandlerBase schedule]
- -[BRCPipelineStageHandlerBase schedule].cold.1
- -[BRCPipelineStageHandlerBase(InternalPipeline) _groupIdentifierForJob:]
- -[BRCPipelineStageHandlerBase(InternalPipeline) _initializeSourceAndQueues]
- -[BRCPipelineStageHandlerBase(InternalPipeline) addJob:]
- -[BRCPipelineStageHandlerBase(InternalPipeline) cancelJob:]
- -[BRCPipelineStageHandlerBase(InternalPipeline) description]
- -[BRCPipelineStageHandlerBase(InternalPipeline) disableScheduling]
- -[BRCPipelineStageHandlerBase(InternalPipeline) dumpToContext:]
- -[BRCPipelineStageHandlerBase(InternalPipeline) enableScheduling]
- -[BRCPipelineStageHandlerBase(InternalPipeline) setupWithInternalPipelineJobCompletionHandler:]
- -[BRCProgress _updateToBeProgressForDocument:group:totalUnitCount:completedUnitCount:]
- -[BRCProgress initWithGroup:session:]
- -[BRCProgress setCompletedUnitCount:]
- -[BRCProgress setSession:group:]
- -[BRCQueryItemUtil contentPolicyForItemInfo:sessionContext:]
- -[BRCQueryItemUtil contentPolicyForRootContainerWithSessionContext:]
- -[BRCRequestData .cxx_destruct]
- -[BRCRequestData copyWithZone:]
- -[BRCRequestData description]
- -[BRCRequestData description].cold.1
- -[BRCRequestData finishBlock]
- -[BRCRequestData initWithProgress:requestType:finishBlock:]
- -[BRCRequestData progress]
- -[BRCRequestData requestType]
- -[BRCServerItem appLibraryForRootItem]
- -[BRCServerItem appLibraryForRootItem].cold.1
- -[BRCServerItem appLibraryForRootItem].cold.2
- -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step]
- -[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step].cold.1
- -[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]
- -[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step].cold.1
- -[BRCSharingAcceptFlowOperation initWithShareMetadata:client:sessionContext:userNotifier:userActionsNavigator:]
- -[BRCStageRegistry _garbageCollectSpace:]
- -[BRCStageRegistry _garbageCollectUnusedLiveItems]
- -[BRCStageRegistry _purgeSpaceUnderQueue:withUrgency:]
- -[BRCStageRegistry garbageCollectSpace:]
- -[BRCStageRegistry garbageCollectSpace:].cold.1
- -[BRCStageRegistry purgeGraveyardSpace:withUrgency:]
- -[BRCStageRegistry purgeGraveyardSpace:withUrgency:].cold.1
- -[BRCStageRegistry purgeSpace:withUrgency:]
- -[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]
- -[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:].cold.1
- -[BRCSyncContext _buildBGSystemTaskIdentifierForCKOperation:]
- -[BRCSyncContext _cancelBGSystemTasks]
- -[BRCSyncContext _cancelBgSystemTaskIfNeededForCKOperation:]
- -[BRCSyncContext _resumeAllDownloadStreams]
- -[BRCSyncContext _setupBGSystemTaskCompletionFor:]
- -[BRCSyncContext _setupBGSystemTaskCompletionFor:].cold.1
- -[BRCSyncContext _updateSubmittedBGSystemTasksWithState:]
- -[BRCSyncContext _updateSubmittedBGSystemTasksWithState:].cold.1
- -[BRCSyncContext _updateSubmittedBGSystemTasksWithState:submittedBGSystemTaskIdentifiers:]
- -[BRCSyncContext _updateWifiOnlyBGSystemTaskWithCancelledTaskIdentifiers:inexpensiveNetworkConnectivity:]
- -[BRCSyncContext addOperation:allowsCellularAccess:asCompletionOf:]
- -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:]
- -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:].cold.1
- -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:].cold.2
- -[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:].cold.3
- -[BRCSyncContext dealloc]
- -[BRCSyncContext numberOfSubmittedBGSystemTasks]
- -[BRCSyncContext readerThrottle]
- -[BRCSyncContext setupIfNeeded].cold.1
- -[BRCSyncContext submittedBGSystemTaskIdentifiers]
- -[BRCSyncUpOperation _handleErrorForRecord:inZone:error:].cold.2
- -[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToPCSChainingItem:].cold.1
- -[BRCSystemResourcesManager _didReceiveMemoryWarning]
- -[BRCSystemResourcesManager _didReceiveMemoryWarning].cold.1
- -[BRCSystemResourcesManager _initLowMemory]
- -[BRCSystemResourcesManager _initLowMemory].cold.1
- -[BRCSystemResourcesManager _invalidateLowMemory]
- -[BRCSystemResourcesManager addLowMemoryObserver:]
- -[BRCSystemResourcesManager removeLowMemoryObserver:]
- -[BRCUploadSyncUpRequestsManager .cxx_destruct]
- -[BRCUploadSyncUpRequestsManager _callFinishBlockOnDataRequest:finishError:]
- -[BRCUploadSyncUpRequestsManager _initWithPersonaIdentifier:]
- -[BRCUploadSyncUpRequestsManager _invalidateRequestsTableWithNewSource:]
- -[BRCUploadSyncUpRequestsManager cancelRequestForIdentifier:error:]
- -[BRCUploadSyncUpRequestsManager dumpToContext:]
- -[BRCUploadSyncUpRequestsManager finishRequestForIdentifer:finishError:error:]
- -[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:]
- -[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:].cold.1
- -[BRCUploadSyncUpRequestsManager getProgressForIdentifier:]
- -[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:]
- -[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:].cold.1
- -[BRCUploadSyncUpRequestsManager registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:]
- -[BRCUserDefaults _loadObjectForKey:inheritFromGlobal:suiteName:validateWithBlock:]
- -[BRCUserDefaults _loadObjectForKey:inheritFromGlobal:suiteName:validateWithBlock:].cold.1
- -[BRCUserDefaults _shouldRampForKey:accountFacade:].cold.1
- -[BRCUserDefaults _shouldRampForKey:accountFacade:].cold.2
- -[BRCUserDefaults _shouldRampForKey:accountFacade:].cold.3
- -[BRCUserDefaults _shouldRampForKey:accountFacade:].cold.4
- -[BRCUserDefaults accessTimeDeltaInHighUrgency]
- -[BRCUserDefaults accessTimeDeltaInLowUrgency]
- -[BRCUserDefaults accessTimeDeltaInMedUrgency]
- -[BRCUserDefaults accessTimeDeltaInVeryHighUrgency]
- -[BRCUserDefaults cacheDeletePushBGSystemTaskConfig]
- -[BRCUserDefaults dbFixupContentPolicyRecoverAfterTimeInterval]
- -[BRCUserDefaults discretionaryOperationBGSystemTaskConfigForBackgroundContext]
- -[BRCUserDefaults discretionaryOperationBGSystemTaskConfigForForegroundContext]
- -[BRCUserDefaults discretionaryOperationBGSystemTaskConfigWithForegroundState:]
- -[BRCUserDefaults graveyardAgeDeltaInLowUrgency]
- -[BRCUserDefaults graveyardAgeDeltaInMedUrgency]
- -[BRCUserDefaults initAsGlobalWithServerConfiguration:]
- -[BRCUserDefaults initWithServerConfiguration:globalUserDefaults:clientZoneIdentifier:]
- -[BRCUserDefaults objectForKey:inheritFromGlobal:suiteName:validateWithBlock:]
- -[BRCUserDefaults onDiskAccessTimeDeltaInHighUrgency]
- -[BRCUserDefaults onDiskAccessTimeDeltaInLowUrgency]
- -[BRCUserDefaults onDiskAccessTimeDeltaInMedUrgency]
- -[BRCUserDefaults onDiskAccessTimeDeltaInVeryHighUrgency]
- -[BRCUserDefaults readerThrottleParams]
- -[BRCUserDefaults spotlightIndexingEnabled]
- -[BRCUserDefaults useBGSTForSchedulingDiscretionaryOperations]
- -[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]
- -[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]
- -[BRCXPCRegularIPCsClient dropSpotlightIndexWithReply:]
- -[BRCXPCRegularIPCsClient purgeAmount:withUrgency:reply:]
- -[BRCXPCRegularIPCsClient reclaimAmount:withUrgency:reply:]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:].cold.1
- -[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:].cold.2
- -[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]
- -[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]
- -[BRContainer(Daemon) currentStatus]
- -[BRContainer(Daemon) currentStatus].cold.1
- -[BRContainer(Daemon) lastServerUpdate]
- -[BRContainer(Daemon) lastServerUpdate].cold.1
- -[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]
- -[NSProgress(BRCAdditions) brc_publish]
- -[NSProgress(BRCAdditions) brc_publish].cold.1
- -[NSProgress(BRCAdditions) brc_unpublish]
- -[NSProgress(BRCAdditions) brc_unpublish].cold.1
- -[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]
- -[_BRCOperation addSubOperation:asCompletionOf:]
- -[_BRCOperation addSubOperation:asCompletionOf:].cold.1
- GCC_except_table112
- GCC_except_table128
- GCC_except_table137
- GCC_except_table142
- GCC_except_table146
- GCC_except_table156
- GCC_except_table170
- GCC_except_table176
- GCC_except_table188
- GCC_except_table189
- GCC_except_table204
- GCC_except_table206
- GCC_except_table209
- GCC_except_table211
- GCC_except_table213
- GCC_except_table214
- GCC_except_table219
- GCC_except_table223
- GCC_except_table225
- GCC_except_table227
- GCC_except_table234
- GCC_except_table247
- GCC_except_table249
- GCC_except_table252
- GCC_except_table254
- GCC_except_table260
- GCC_except_table264
- GCC_except_table266
- GCC_except_table268
- GCC_except_table270
- GCC_except_table271
- GCC_except_table280
- GCC_except_table282
- GCC_except_table295
- GCC_except_table313
- GCC_except_table323
- GCC_except_table325
- GCC_except_table341
- GCC_except_table348
- GCC_except_table355
- GCC_except_table357
- GCC_except_table359
- GCC_except_table372
- GCC_except_table378
- GCC_except_table383
- GCC_except_table404
- GCC_except_table418
- GCC_except_table421
- GCC_except_table423
- GCC_except_table430
- GCC_except_table437
- GCC_except_table443
- GCC_except_table449
- GCC_except_table453
- GCC_except_table462
- GCC_except_table464
- GCC_except_table466
- GCC_except_table469
- GCC_except_table55
- GCC_except_table575
- GCC_except_table66
- OBJC_IVAR_$_BRCClientZone._appliedTombstoneRanks
- OBJC_IVAR_$_BRCClientZone._blockedOperationsOnInitialSync
- OBJC_IVAR_$_BRCClientZone._faultsLiveBarriers
- OBJC_IVAR_$_BRCClientZone._fetchParentOperations
- OBJC_IVAR_$_BRCClientZone._fetchRecentsOperation
- OBJC_IVAR_$_BRCClientZone._invokeFetchRecentsOperation
- OBJC_IVAR_$_BRCClientZone._lastAttemptedSyncDownDate
- OBJC_IVAR_$_BRCClientZone._lastInsertedRank
- OBJC_IVAR_$_BRCClientZone._lastSyncDownDate
- OBJC_IVAR_$_BRCClientZone._lastSyncDownError
- OBJC_IVAR_$_BRCClientZone._lastSyncUpError
- OBJC_IVAR_$_BRCClientZone._lastSyncUpErrorWasOnChainedItem
- OBJC_IVAR_$_BRCClientZone._locateRecordOperations
- OBJC_IVAR_$_BRCClientZone._locateRecordsOperationThrottle
- OBJC_IVAR_$_BRCClientZone._readerThrottle
- OBJC_IVAR_$_BRCClientZone._recursiveListOperations
- OBJC_IVAR_$_BRCClientZone._resetTimer
- OBJC_IVAR_$_BRCClientZone._runningListOperations
- OBJC_IVAR_$_BRCClientZone._serverStitchingOperationThrottle
- OBJC_IVAR_$_BRCClientZone._shouldShowiCloudDriveAppInstallationNotification
- OBJC_IVAR_$_BRCClientZone._syncDeadlineSource
- OBJC_IVAR_$_BRCClientZone._syncDeadlineSourceResumer
- OBJC_IVAR_$_BRCClientZone._syncDownBlockToPerformForBookmarkData
- OBJC_IVAR_$_BRCClientZone._syncDownOperation
- OBJC_IVAR_$_BRCClientZone._syncDownThrottle
- OBJC_IVAR_$_BRCClientZone._syncState
- OBJC_IVAR_$_BRCClientZone._syncUpBackoffRatio
- OBJC_IVAR_$_BRCClientZone._syncUpBudget
- OBJC_IVAR_$_BRCClientZone._syncUpOperation
- OBJC_IVAR_$_BRCClientZone._syncUpRetryAfter
- OBJC_IVAR_$_BRCClientZone._syncUpThrottle
- OBJC_IVAR_$_BRCFileProvidingRequestOperation._appLibrariesMonitored
- OBJC_IVAR_$_BRCFileProvidingRequestOperation._client
- OBJC_IVAR_$_BRCNotification._aliasSourceAppLibraryID
- OBJC_IVAR_$_BRQueryItem._parentPath
- OBJC_IVAR_$_BRQueryItem._physicalName
- _BRCBGSystemTaskRateLimitConfigurationName
- _BRCMigrateLegacyUbiquityRoot
- _BRCMigrateLegacyUbiquityRoot.cold.1
- _BRCMigrateLegacyUbiquityRoot.cold.2
- _BRCMigrateLegacyUbiquityRoot.cold.3
- _BRCMigrateLegacyUbiquityRoot.cold.4
- _BRCMigrateLegacyUbiquityRoot.cold.5
- _BRCMigrateLegacyUbiquityRoot.cold.6
- _BRCPipelineStageNone
- _BRCRootIsOwnedByUbd
- _BRCRootIsOwnedByUbd.cold.1
- _BRCRootIsOwnedByUbd.cold.2
- _BRCSyncContextDidBecomeForeground_block_invoke.__personaOnceToken
- _BRCSyncContextDidBecomeForeground_block_invoke.__personalPersona
- _BRCTouchRootMergeWitness
- _BRDefaultsDomain
- _BRNotifyNameForForegroundChangeWithContainerID
- _BRUbiquitousDefaultMangledContainerID
- _CFPreferencesAppSynchronize
- _CFPreferencesSetAppValue
- _CacheDeleteRegisterInfoCallbacks
- _NSFilePosixPermissions
- _NSURLCreationDateKey
- _NSURLIsHiddenKey
- _OBJC_CLASS_$_BRCBGSystemTaskContext
- _OBJC_CLASS_$_BRCPipeline
- _OBJC_CLASS_$_BRCPipelineJob
- _OBJC_CLASS_$_BRCPipelineJobQueue
- _OBJC_CLASS_$_BRCPipelineStageHandlerBase
- _OBJC_CLASS_$_BRCRequestData
- _OBJC_CLASS_$_BRCUploadSyncUpRequestsManager
- _OBJC_CLASS_$_CSSearchableIndex
- _OBJC_IVAR_$_BRCAccountSession._isInCarry
- _OBJC_IVAR_$_BRCBGSystemTaskContext._options
- _OBJC_IVAR_$_BRCBGSystemTaskContext._referenceCounter
- _OBJC_IVAR_$_BRCClientZone._allItemsDidUploadTrackers
- _OBJC_IVAR_$_BRCClientZone._bubbleSyncTask
- _OBJC_IVAR_$_BRCClientZone._currentSyncDownBarriers
- _OBJC_IVAR_$_BRCClientZone._dbFacade
- _OBJC_IVAR_$_BRCClientZone._directoriesCreatedLastSyncUp
- _OBJC_IVAR_$_BRCClientZone._downloadedBlockToPerformForItemID
- _OBJC_IVAR_$_BRCClientZone._itemIDsBlockedFromSyncForCZMProcessing
- _OBJC_IVAR_$_BRCClientZone._locateBlocksToPerformForRecordID
- _OBJC_IVAR_$_BRCClientZone._nextIdleHandlers
- _OBJC_IVAR_$_BRCClientZone._nextSyncDownBarriers
- _OBJC_IVAR_$_BRCClientZone._onDiskBlockToPerformForItemID
- _OBJC_IVAR_$_BRCClientZone._osNameRequiredToSync
- _OBJC_IVAR_$_BRCClientZone._outOfBandSyncOperations
- _OBJC_IVAR_$_BRCClientZone._parentsOfCZMFaults
- _OBJC_IVAR_$_BRCClientZone._requestID
- _OBJC_IVAR_$_BRCClientZone._resetAfterAppUninstallTimer
- _OBJC_IVAR_$_BRCClientZone._syncDownBlockToPerformForItemID
- _OBJC_IVAR_$_BRCClientZone._syncDownDependencies
- _OBJC_IVAR_$_BRCClientZone._syncDownGroup
- _OBJC_IVAR_$_BRCClientZone._syncThrottles
- _OBJC_IVAR_$_BRCClientZone._syncUpBatchSizeMultiplier
- _OBJC_IVAR_$_BRCClientZone._taskTracker
- _OBJC_IVAR_$_BRCFileProviderDaemonUtils._isFPFS
- _OBJC_IVAR_$_BRCPipeline._cancelledJobs
- _OBJC_IVAR_$_BRCPipeline._name
- _OBJC_IVAR_$_BRCPipeline._pipelineAutoResumeTimer
- _OBJC_IVAR_$_BRCPipeline._queue
- _OBJC_IVAR_$_BRCPipeline._stageHandlers
- _OBJC_IVAR_$_BRCPipeline._stageStringifier
- _OBJC_IVAR_$_BRCPipelineJob._additionalToRequestingStageMap
- _OBJC_IVAR_$_BRCPipelineJob._completionHandler
- _OBJC_IVAR_$_BRCPipelineJob._currentStageID
- _OBJC_IVAR_$_BRCPipelineJob._jobPlan
- _OBJC_IVAR_$_BRCPipelineJob._qualityOfService
- _OBJC_IVAR_$_BRCPipelineJob._stageStringifier
- _OBJC_IVAR_$_BRCPipelineJob._stageToRecoveryPlanMap
- _OBJC_IVAR_$_BRCPipelineJobQueue._activeQOSValues
- _OBJC_IVAR_$_BRCPipelineJobQueue._qosToGroupingToJobMapping
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._activelyExecutingJobs
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._activelyExecutingProgress
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._cancelledActivelyExecutingJobs
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._enqueuedJobs
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._handlerQueue
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._schedulingEnabled
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._schedulingQueue
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._schedulingSource
- _OBJC_IVAR_$_BRCPipelineStageHandlerBase._suspended
- _OBJC_IVAR_$_BRCRequestData._finishBlock
- _OBJC_IVAR_$_BRCRequestData._progress
- _OBJC_IVAR_$_BRCRequestData._requestType
- _OBJC_IVAR_$_BRCSharingAcceptFlowOperation._xpcClient
- _OBJC_IVAR_$_BRCStageRegistry._stageDirectoryFileID
- _OBJC_IVAR_$_BRCSyncContext._notifyTokenForFramework
- _OBJC_IVAR_$_BRCSyncContext._readerThrottle
- _OBJC_IVAR_$_BRCSyncContext._submittedBGSystemTaskIdentifiers
- _OBJC_IVAR_$_BRCSystemResourcesManager._lowMemoryObservers
- _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._latestSourceIdentifier
- _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._personaIdentifer
- _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._requestsByItemGlobalID
- _OBJC_IVAR_$_BRCUploadSyncUpRequestsManager._zoneIDToItemIDs
- _OBJC_METACLASS_$_BRCBGSystemTaskContext
- _OBJC_METACLASS_$_BRCPipeline
- _OBJC_METACLASS_$_BRCPipelineJob
- _OBJC_METACLASS_$_BRCPipelineJobQueue
- _OBJC_METACLASS_$_BRCPipelineStageHandlerBase
- _OBJC_METACLASS_$_BRCRequestData
- _OBJC_METACLASS_$_BRCUploadSyncUpRequestsManager
- __OBJC_$_CATEGORY_BRContainer_$_Daemon
- __OBJC_$_CATEGORY_INSTANCE_METHODS_BRContainer_$_Daemon
- __OBJC_$_CLASS_METHODS_BRCDiskSpaceReclaimer
- __OBJC_$_CLASS_METHODS_BRCProgress
- __OBJC_$_CLASS_METHODS_BRCRecentsEnumerator
- __OBJC_$_CLASS_METHODS_BRCUploadSyncUpRequestsManager
- __OBJC_$_INSTANCE_METHODS_BRCBGSystemTaskContext
- __OBJC_$_INSTANCE_METHODS_BRCFileProvidingRequestOperation(FPFSAdditions)
- __OBJC_$_INSTANCE_METHODS_BRCPipeline
- __OBJC_$_INSTANCE_METHODS_BRCPipelineJob(InternalPipeline)
- __OBJC_$_INSTANCE_METHODS_BRCPipelineJobQueue
- __OBJC_$_INSTANCE_METHODS_BRCPipelineStageHandlerBase(InternalPipeline)
- __OBJC_$_INSTANCE_METHODS_BRCRequestData
- __OBJC_$_INSTANCE_METHODS_BRCUploadSyncUpRequestsManager
- __OBJC_$_INSTANCE_VARIABLES_BRCBGSystemTaskContext
- __OBJC_$_INSTANCE_VARIABLES_BRCPipeline
- __OBJC_$_INSTANCE_VARIABLES_BRCPipelineJob
- __OBJC_$_INSTANCE_VARIABLES_BRCPipelineJobQueue
- __OBJC_$_INSTANCE_VARIABLES_BRCPipelineStageHandlerBase
- __OBJC_$_INSTANCE_VARIABLES_BRCRequestData
- __OBJC_$_INSTANCE_VARIABLES_BRCUploadSyncUpRequestsManager
- __OBJC_$_PROP_LIST_BRCBGSystemTaskContext
- __OBJC_$_PROP_LIST_BRCPipelineStageHandlerJobCostVendor
- __OBJC_$_PROP_LIST_BRCPipelineStageHandlerProtocol
- __OBJC_$_PROP_LIST_BRCRequestData
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCPipelineStageHandlerJobCostVendor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCPipelineStageHandlerProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BRCPipelineStageHandlerJobCostVendor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BRCPipelineStageHandlerProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRCPipelineStageHandlerJobCostVendor
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRCPipelineStageHandlerProtocol
- __OBJC_$_PROTOCOL_REFS_BRCPipelineStageHandlerJobCostVendor
- __OBJC_$_PROTOCOL_REFS_BRCPipelineStageHandlerProtocol
- __OBJC_CLASS_PROTOCOLS_$_BRCRequestData
- __OBJC_CLASS_RO_$_BRCBGSystemTaskContext
- __OBJC_CLASS_RO_$_BRCPipeline
- __OBJC_CLASS_RO_$_BRCPipelineJob
- __OBJC_CLASS_RO_$_BRCPipelineJobQueue
- __OBJC_CLASS_RO_$_BRCPipelineStageHandlerBase
- __OBJC_CLASS_RO_$_BRCRequestData
- __OBJC_CLASS_RO_$_BRCUploadSyncUpRequestsManager
- __OBJC_LABEL_PROTOCOL_$_BRCPipelineStageHandlerJobCostVendor
- __OBJC_LABEL_PROTOCOL_$_BRCPipelineStageHandlerProtocol
- __OBJC_METACLASS_RO_$_BRCBGSystemTaskContext
- __OBJC_METACLASS_RO_$_BRCPipeline
- __OBJC_METACLASS_RO_$_BRCPipelineJob
- __OBJC_METACLASS_RO_$_BRCPipelineJobQueue
- __OBJC_METACLASS_RO_$_BRCPipelineStageHandlerBase
- __OBJC_METACLASS_RO_$_BRCRequestData
- __OBJC_METACLASS_RO_$_BRCUploadSyncUpRequestsManager
- __OBJC_PROTOCOL_$_BRCPipelineStageHandlerJobCostVendor
- __OBJC_PROTOCOL_$_BRCPipelineStageHandlerProtocol
- __OBJC_PROTOCOL_REFERENCE_$_BRCPipelineStageHandlerJobCostVendor
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.83
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.83.cold.1
- ___103-[BRCFileProvidingRequestOperation initWithDocumentItem:client:sessionContext:downloadTrackersManager:]_block_invoke
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.162
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.162.cold.1
- ___105-[BRCSyncContext _updateWifiOnlyBGSystemTaskWithCancelledTaskIdentifiers:inexpensiveNetworkConnectivity:]_block_invoke
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.128
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.110
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.110.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.112
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.134
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.134.cold.1
- ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.142
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.646
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100.cold.2
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.104
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.104.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.105
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.105.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.107
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.107.cold.1
- ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.137
- ___115+[BRCServerChangesApplyUtil handleApplyChangesForUnliveServerItem:isDeleteOfShareRoot:rank:scheduler:zone:session:]_block_invoke.36
- ___115-[BRCMigrationQueryOperation _updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke
- ___115-[BRCMigrationQueryOperation _updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke_2
- ___115-[BRCMigrationQueryOperation _updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:]_block_invoke_3
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.108
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.110
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.115
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.115.cold.1
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.222
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.cold.1
- ___123-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]_block_invoke
- ___123-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]_block_invoke.63
- ___123-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]_block_invoke_2
- ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke.140
- ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.193
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.195
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.196
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.113
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.114
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke_2
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.43
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.47
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.49
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.1
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.49.cold.2
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke.56
- ___135-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke_2
- ___148-[BRCServerZone didSyncDownRequestID:serverChangeToken:editedRecords:deletedRecordIDs:deletedShareRecordIDs:allocRankZones:caughtUp:pendingChanges:]_block_invoke.255
- ___18-[BRCDaemon start]_block_invoke.95
- ___18-[BRCDaemon start]_block_invoke_4
- ___22-[BRCClientZone close]_block_invoke.89
- ___23-[BRCClientZone resume]_block_invoke_2
- ___23-[BRCClientZone resume]_block_invoke_3
- ___23-[BRCDaemon selfCheck:]_block_invoke.149
- ___25-[BRCFSUploader schedule]_block_invoke.156
- ___26-[BRCAccountSession close]_block_invoke.305
- ___26-[BRCStageRegistry resume]_block_invoke.151
- ___27-[BRCClientZone _startSync]_block_invoke.193
- ___27-[BRCClientZone _startSync]_block_invoke.197
- ___27-[BRCClientZone _startSync]_block_invoke.197.cold.1
- ___27-[BRCClientZone _startSync]_block_invoke.197.cold.2
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.43
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.48
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.48.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.49
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.51
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.57
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.67
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.54
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.2
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.63.cold.3
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.68
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.68.cold.1
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.68.cold.2
- ___30-[BRCDaemon _setupCacheDelete]_block_invoke_2.68.cold.3
- ___30-[BRCNotificationPipe __flush]_block_invoke.140
- ___30-[BRCNotificationPipe __flush]_block_invoke.141
- ___30-[BRCPipeline _armResumeTimer]_block_invoke
- ___33-[BRCPipeline addJob:moreComing:]_block_invoke
- ___33-[BRCPipeline addJob:moreComing:]_block_invoke.cold.1
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.40
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.40.cold.1
- ___34-[BRCAccountsManager loadAccounts]_block_invoke.48
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.328
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.328.cold.1
- ___37-[BRCPipelineJobQueue dumpToContext:]_block_invoke
- ___37-[BRCPipelineJobQueue dumpToContext:]_block_invoke_2
- ___39+[BRCUserDefaults _userDefaultsManager]_block_invoke
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.244
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.3
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.4
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.1
- ___39-[BRCPipeline _computeStageStringifier]_block_invoke
- ___39-[BRCPipeline _generateProgressForJob:]_block_invoke
- ___39-[BRCPipeline _generateProgressForJob:]_block_invoke.42
- ___39-[BRCPipeline _generateProgressForJob:]_block_invoke.42.cold.1
- ___39-[BRCPipeline _generateProgressForJob:]_block_invoke.42.cold.2
- ___39-[BRCPipelineStageHandlerBase schedule]_block_invoke
- ___39-[BRCPipelineStageHandlerBase schedule]_block_invoke_2
- ___39-[BRCPipelineStageHandlerBase schedule]_block_invoke_2.cold.1
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.269
- ___39-[BRCUserDefaults readerThrottleParams]_block_invoke
- ___39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.95
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.157
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.157.cold.1
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke.161
- ___40-[BRCDaemon networkReachabilityChanged:]_block_invoke_2.162
- ___40-[BRCFileUnlinker initWithCacheDirPath:]_block_invoke
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.266
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.267
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.270
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.283
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.269
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.269.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.271
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.271.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.275
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_4
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.204
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.204.cold.1
- ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.129
- ___43-[BRCStageRegistry purgeSpace:withUrgency:]_block_invoke
- ___43-[BRCSystemResourcesManager _initLowMemory]_block_invoke
- ___43-[BRCSystemResourcesManager _initLowMemory]_block_invoke_2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.337
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.337.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.340
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.362
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.362.cold.1
- ___45-[BRCPipeline _setStageJobCompletionHandlers]_block_invoke
- ___45-[BRCPipeline _setStageJobCompletionHandlers]_block_invoke_2
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.335
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.335.cold.1
- ___46-[BRCFSUploader rescheduleJobsPendingCellular]_block_invoke.115
- ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.458
- ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.344
- ___47-[BRCAccountsManager waitUntilDeviceIsUnlocked]_block_invoke.76
- ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.306
- ___47-[BRCNotificationPipe processUpdates:withRank:]_block_invoke.138
- ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.172
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.135
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke.135.cold.1
- ___48-[BRCDaemon listener:shouldAcceptNewConnection:]_block_invoke_2.141
- ___48-[BRCDiskSpaceReclaimer purgeSpace:withUrgency:]_block_invoke
- ___48-[BRCUploadSyncUpRequestsManager dumpToContext:]_block_invoke
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.352
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.353
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.354
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.359
- ___49-[BRCDiskSpaceReclaimer _asyncAutovacuumIfNeeds:]_block_invoke
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.517
- ___49-[BRCSystemResourcesManager _invalidateLowMemory]_block_invoke
- ___50-[BRCSyncContext _setupBGSystemTaskCompletionFor:]_block_invoke
- ___50-[BRCSyncContext _setupBGSystemTaskCompletionFor:]_block_invoke.cold.1
- ___50-[BRCSystemResourcesManager addLowMemoryObserver:]_block_invoke
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.131
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.132
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.133
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.277
- ___52-[BRCStageRegistry purgeGraveyardSpace:withUrgency:]_block_invoke
- ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.175
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.249
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.263
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.260
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_3
- ___53-[BRCSystemResourcesManager removeLowMemoryObserver:]_block_invoke
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.502
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.164
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.165
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.166
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.166.cold.1
- ___54-[BRCNotificationPipe _watchItem:options:gatherReply:]_block_invoke.167.cold.1
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133.cold.1
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133.cold.2
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.411
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.412
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.451
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.452
- ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.442
- ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.442.cold.1
- ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.399
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.15
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.15.cold.1
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.15.cold.2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.15.cold.3
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.15.cold.4
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29.cold.1
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29.cold.2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29.cold.3
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29.cold.4
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.29.cold.5
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36.cold.1
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36.cold.2
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36.cold.3
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36.cold.4
- ___55-[BRCAnalyticsReporter registerBackgroundXPCActivities]_block_invoke.36.cold.5
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.721
- ___56-[BRCPipelineStageHandlerBase(InternalPipeline) addJob:]_block_invoke
- ___56-[BRCPipelineStageHandlerBase(InternalPipeline) addJob:]_block_invoke.cold.1
- ___56-[BRCPipelineStageHandlerBase(InternalPipeline) addJob:]_block_invoke.cold.2
- ___56-[BRCSystemResourcesManager _invalidateProcessObservers]_block_invoke
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.369
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.370
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.668
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.668.cold.1
- ___56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.300
- ___56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.302
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437.cold.2
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.438
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.353
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.354
- ___57-[BRCXPCRegularIPCsClient purgeAmount:withUrgency:reply:]_block_invoke
- ___58+[BRCUploadSyncUpRequestsManager _fetchManagersDictionary]_block_invoke
- ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.48
- ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.48.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.464
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.464.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.471
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.473
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.420
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.421
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.433
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.433.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.435
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.436
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.39
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.39.cold.1
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.41
- ___59-[BRCPipelineJob(InternalPipeline) descriptionWithContext:]_block_invoke
- ___59-[BRCPipelineJob(InternalPipeline) descriptionWithContext:]_block_invoke_2
- ___59-[BRCPipelineJob(InternalPipeline) descriptionWithContext:]_block_invoke_3
- ___59-[BRCPipelineStageHandlerBase(InternalPipeline) cancelJob:]_block_invoke
- ___59-[BRCPipelineStageHandlerBase(InternalPipeline) cancelJob:]_block_invoke.cold.1
- ___59-[BRCXPCRegularIPCsClient reclaimAmount:withUrgency:reply:]_block_invoke
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.375
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.376
- ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.53
- ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.56
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.1
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.2
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.3
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.4
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.5
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.6
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.157.cold.7
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.167
- ___60-[BRCSharingAcceptFlowOperation _createSideFaultOnDisk_step]_block_invoke.173
- ___60-[BRCSharingAcceptFlowOperation _showSharingJoinDialog_step]_block_invoke.141
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.614.cold.1
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.189
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.192
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256.cold.2
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.258
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.261
- ___61-[BRCPipelineJob initWithQualityOfService:completionHandler:]_block_invoke
- ___61-[BRCSharingAcceptFlowOperation _locateSharedItemOnDisk_step]_block_invoke.195
- ___61-[BRCSyncContext initWithSession:contextIdentifier:isShared:]_block_invoke
- ___61-[BRCSyncContext initWithSession:contextIdentifier:isShared:]_block_invoke.49
- ___61-[BRCSyncContext initWithSession:contextIdentifier:isShared:]_block_invoke.55
- ___61-[BRCSyncContext initWithSession:contextIdentifier:isShared:]_block_invoke_2
- ___62-[BRCSharingAcceptFlowOperation _locateSharedItemOnOwner_step]_block_invoke.152
- ___62-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.609
- ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke.cold.1
- ___63-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke.cold.2
- ___63-[BRCClientZone(BRCZoneReset) scheduleReset:completionHandler:]_block_invoke.7
- ___63-[BRCClientZone(BRCZoneReset) scheduleReset:completionHandler:]_block_invoke.7.cold.1
- ___63-[BRCPipelineStageHandlerBase(InternalPipeline) dumpToContext:]_block_invoke
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.138
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.138.cold.1
- ___64-[BRCUserDefaultsManager _setServerConfigurationURL:whenLoaded:]_block_invoke.249
- ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.398
- ___65-[BRCAccountSession recoverAndReportContentPolicyWithCompletion:]_block_invoke
- ___65-[BRCAccountSession recoverAndReportContentPolicyWithCompletion:]_block_invoke_2
- ___65-[BRCAccountSession recoverAndReportContentPolicyWithCompletion:]_block_invoke_3
- ___65-[BRCAccountsManager updateAccountDisplayName:completionHandler:]_block_invoke.69
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.230
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.231
- ___65-[BRCPipelineStageHandlerBase(InternalPipeline) enableScheduling]_block_invoke
- ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.666
- ___65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.313
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.662.cold.2
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.663
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.392
- ___66-[BRCFetchRecordSubResourcesOperation saveRecordsWithQueryCursor:]_block_invoke.61
- ___66-[BRCPipelineStageHandlerBase(InternalPipeline) disableScheduling]_block_invoke
- ___66-[BRCSharingAcceptFlowOperation _locateSharedItemOnRecipient_step]_block_invoke.186
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.616
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.617
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.619
- ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.123
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.429
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.429.cold.1
- ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke.83
- ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke_2.84
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.439
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.440
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.155
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.156
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke.159.cold.1
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_2.157
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.158
- ___68-[BRCNotificationPipe watchScopes:trustedAppLibraryIDs:gatherReply:]_block_invoke_3.158.cold.1
- ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.337
- ___69-[BRCPipelineJobQueue dequeueHighestQualityOfServiceJobsWithHandler:]_block_invoke
- ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.320
- ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.413
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.650
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.652
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.652.cold.1
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.653
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.653.cold.1
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.447
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.448
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.456
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.456.cold.1
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.15
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.18
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.1
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.2
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.3
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.4
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.5
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.cold.6
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke_2
- ___71-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke_2.19
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.712
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.658
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.115
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.119
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.610
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.604
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.191
- ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnOwner_step]_block_invoke.156
- ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke.154
- ___73-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnOwner_step]_block_invoke_2.155
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.414
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.405
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.405.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.406
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.406.cold.1
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.407
- ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.667
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.371
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.387
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.579
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.581
- ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.195
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.85
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.91
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke.97
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.92
- ___74-[BRCRecentsEnumerator _enumerateChangesFromChangeToken:limit:completion:]_block_invoke_2.98
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.623
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.625
- ___74-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke
- ___74-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke.cold.1
- ___74-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke.cold.2
- ___74-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke.cold.3
- ___74-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke.cold.4
- ___75-[BRCPipelineStageHandlerBase(InternalPipeline) _initializeSourceAndQueues]_block_invoke
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400.cold.1
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400.cold.2
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401.cold.1
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.620
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.621
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.738
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.742
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.740
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.179
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.179.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.180
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.180.cold.1
- ___76-[BRCSharingAcceptFlowOperation _createServerFaultIfPossibleWithCompletion:]_block_invoke.180.cold.2
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.612.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.576
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.607
- ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToBeOnDiskOnRecipient_step]_block_invoke.194
- ___77-[BRCSharingAcceptFlowOperation _waitForSharedItemToSyncDownOnRecipient_step]_block_invoke.193
- ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.418
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.156
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.36
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.36.cold.1
- ___79-[BRCBGSystemTaskManager submitBGSystemTaskWithIdentifier:configuration:block:]_block_invoke.36.cold.2
- ___79-[BRCClientZone scheduleResetServerAndClientTruthsForReason:completionHandler:]_block_invoke
- ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.355
- ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.356
- ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.357
- ___80-[BRCClientZone(BRCZoneReset) _finishedReset:signpostTracker:completionHandler:]_block_invoke.46
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.567
- ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.333
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.453
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.454
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.59
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.60.cold.1
- ___81-[BRCAccountsManager _maintainExistingFileProviderDomainsWithAccounts:withError:]_block_invoke.63.cold.1
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.642
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.578
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.644
- ___82+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]_block_invoke
- ___82+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]_block_invoke.cold.1
- ___82+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]_block_invoke.cold.2
- ___82+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]_block_invoke.cold.3
- ___82-[BRCAccountsManager _scheduleExistingFileProviderDomainsMaintenanceWithAccounts:]_block_invoke.65
- ___83-[BRCProgress _setupDownloadProgressForDocument:totalUnitCount:completedUnitCount:]_block_invoke.50
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.368
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.368.cold.1
- ___84-[BRCNotificationPipe __performBlockafterDBAndNotifFlush:session:description:error:]_block_invoke.145
- ___84-[BRCNotificationPipe __performBlockafterDBAndNotifFlush:session:description:error:]_block_invoke_2.146
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.504.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.508
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.518
- ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.704
- ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.705
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.648
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.144
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.145
- ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.145.cold.1
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.462
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.463
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.178
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.184
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.152
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.519
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.521
- ___86-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]_block_invoke
- ___86-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]_block_invoke.130
- ___86-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]_block_invoke.cold.1
- ___87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.309
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.120
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.122
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.57
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.57.cold.1
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) listNonLocalVersionsWithItemIdentifier:reply:]_block_invoke.59
- ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.75
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.583
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke.94
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.136
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.158
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.165
- ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.334
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.586
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.587
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.589
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.598
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.599
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.600
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.596
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.159
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.185
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.186
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.634
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.150
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.150.cold.1
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.139
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.151
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.358
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.359
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.360
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.307
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.313
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.313.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.314
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.311
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.311.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.315
- ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.680
- ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.362
- ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.363
- ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.364
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.670
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.670.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.676
- ___95-[BRCPipelineStageHandlerBase(InternalPipeline) setupWithInternalPipelineJobCompletionHandler:]_block_invoke
- ___95-[BRCPipelineStageHandlerBase(InternalPipeline) setupWithInternalPipelineJobCompletionHandler:]_block_invoke_2
- ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.446
- ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.446.cold.1
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.693
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.701
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.154
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.170
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.138
- ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.247
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke.96
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke.cold.1
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke.cold.2
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke.cold.3
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke.cold.4
- ___98-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke_2
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs_e23_B16?0"PQLConnection"8ls32l8s40l8s48l8s56l8s88l8s64l8s72l8s80l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96bs104r_e5_v8?0ls32l8s40l8r104l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
- ___block_descriptor_140_e8_32s40s48s56s64s72s80s88s96s104s112bs_e17_B16?0"NSError"8ls32l8s40l8s112l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_156_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs_e5_v8?0ls32l8s40l8s128l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_32_e18_"NSString"16?0Q8l
- ___block_descriptor_32_e25_v16?0"BRCBGSystemTask"8l
- ___block_descriptor_32_e45_^{__CFDictionary=}20?0i8^{__CFDictionary=}12l
- ___block_descriptor_40_e8_32r_e27_v16?0"BRCAccountHandler"8lr32l8
- ___block_descriptor_40_e8_32s_e25_"NSMutableString"16?0Q8ls32l8
- ___block_descriptor_40_e8_32s_e27_v16?0"BRCAccountHandler"8ls32l8
- ___block_descriptor_40_e8_32s_e31_v32?08"NSMutableArray"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e35_v24?0"NSDictionary"8"NSNumber"16ls32l8
- ___block_descriptor_40_e8_32s_e45_^{__CFDictionary=}20?0i8^{__CFDictionary=}12ls32l8
- ___block_descriptor_40_e8_32s_e48_v32?0"BRCItemGlobalID"8"BRCRequestData"16^B24ls32l8
- ___block_descriptor_40_e8_32w_e18_"NSString"16?0Q8lw32l8
- ___block_descriptor_41_e8_32s_e49_v32?0"NSString"8"BRCBGSystemTaskContext"16^B24ls32l8
- ___block_descriptor_48_e8_32bs40r_e36_v32?0"BRQueryItem"8Q16"NSError"24lr40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e39_v32?0"BRCPipelineJob"8Q16"NSError"24lw40l8s32l8
- ___block_descriptor_48_e8_32r40r_e31_v32?08"NSMutableArray"16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e47_v32?0"NSDictionary"8"NSNumber"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e16_v16?0"NSData"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e47_v32?0"NSDictionary"8"NSNumber"16"NSError"24lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e18_"NSString"16?0Q8ls32l8s40l8
- ___block_descriptor_48_e8_32w_e39_v32?0"BRCPipelineJob"8Q16"NSError"24lw32l8
- ___block_descriptor_49_e8_32r_e17_B16?0"NSError"8lr32l8
- ___block_descriptor_52_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_52_e8_32s40s_e27_v16?0"BRCAccountSession"8ls32l8s40l8
- ___block_descriptor_60_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_60_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_60_e8_32s40s48s_e27_v16?0"BRCAccountSession"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48w56w_e5_v8?0lw48l8w56l8s40l8s32l8
- ___block_descriptor_64_e8_32s40s48r_e24_B16?0"BRCPipelineJob"8ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8r40l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e12_v24?0Q8^B16ls32l8s40l8s56l8s64l8s48l8
- ___block_descriptor_72_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs64bs72bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s64l8s48l8u80l8s72l8
- ___block_descriptor_88_e8_32s40s48s56r64w72w80w_e22_v16?0"BGSystemTask"8ls32l8w64l8w72l8w80l8s40l8r56l8s48l8
- ___block_literal_global.102
- ___block_literal_global.113
- ___block_literal_global.117
- ___block_literal_global.131
- ___block_literal_global.145
- ___block_literal_global.153
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.1604
- ___block_literal_global.165
- ___block_literal_global.1756
- ___block_literal_global.1768
- ___block_literal_global.185
- ___block_literal_global.193
- ___block_literal_global.1939
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.2156
- ___block_literal_global.2162
- ___block_literal_global.2167
- ___block_literal_global.2247
- ___block_literal_global.2273
- ___block_literal_global.2292
- ___block_literal_global.2295
- ___block_literal_global.2304
- ___block_literal_global.2313
- ___block_literal_global.240
- ___block_literal_global.2422
- ___block_literal_global.2446
- ___block_literal_global.2462
- ___block_literal_global.247
- ___block_literal_global.248
- ___block_literal_global.251
- ___block_literal_global.2543
- ___block_literal_global.255
- ___block_literal_global.261
- ___block_literal_global.262
- ___block_literal_global.272
- ___block_literal_global.273
- ___block_literal_global.2884
- ___block_literal_global.30
- ___block_literal_global.308
- ___block_literal_global.315
- ___block_literal_global.32
- ___block_literal_global.327
- ___block_literal_global.339
- ___block_literal_global.373
- ___block_literal_global.389
- ___block_literal_global.39
- ___block_literal_global.408
- ___block_literal_global.444
- ___block_literal_global.448
- ___block_literal_global.509
- ___block_literal_global.51
- ___block_literal_global.53
- ___block_literal_global.56
- ___block_literal_global.655
- ___block_literal_global.66
- ___block_literal_global.677
- ___block_literal_global.71
- ___block_literal_global.763
- ___block_literal_global.953
- ___block_literal_global.98
- ___br_fixup_contentPolicy_block_invoke
- ___br_fixup_contentPolicy_block_invoke_2
- ___br_fixup_contentPolicy_block_invoke_2.cold.1
- __fetchManagersDictionary.managersByPersona
- __fetchManagersDictionary.onceToken
- __issueReadWriteSandboxExtensionForURL
- __issueReadWriteSandboxExtensionForURL.cold.1
- __userDefaultsManager.once
- __userDefaultsManager.userDefaultsManagers
- _initWithDocumentItem:client:sessionContext:downloadTrackersManager:.onceToken
- _initWithDocumentItem:client:sessionContext:downloadTrackersManager:.queue
- _kBRCCacheDeleteID
- _kBRCUserDefaultsFSReaderCoordinationThrottleKey
- _kBRRecordKeyFinderBookmarkTarget
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$__performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:
- _objc_msgSend$_addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:
- _objc_msgSend$_addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:
- _objc_msgSend$_armResumeTimer
- _objc_msgSend$_asJobCostVendor
- _objc_msgSend$_asyncAutovacuumIfNeeds:
- _objc_msgSend$_buildBGSystemTaskIdentifierForCKOperation:
- _objc_msgSend$_buildJobPlanForJob:error:
- _objc_msgSend$_callFinishBlockOnDataRequest:finishError:
- _objc_msgSend$_cancelActiveBatchIfNecessary
- _objc_msgSend$_cancelBGSystemTasks
- _objc_msgSend$_cancelBgSystemTaskIfNeededForCKOperation:
- _objc_msgSend$_completedJob:forStage:recoveryStage:error:
- _objc_msgSend$_completedJob:withRecoveryStage:error:
- _objc_msgSend$_computeStageStringifier
- _objc_msgSend$_decreaseSyncUpBatchSizeAfterError
- _objc_msgSend$_didReceiveMemoryWarning
- _objc_msgSend$_fetchManagersDictionary
- _objc_msgSend$_garbageCollectSpace:
- _objc_msgSend$_garbageCollectUnusedLiveItems
- _objc_msgSend$_generateProgressForJob:
- _objc_msgSend$_groupIdentifierForJob:
- _objc_msgSend$_increaseSyncUpBatchSizeAfterSuccess
- _objc_msgSend$_initLowMemory
- _objc_msgSend$_initWithPersonaIdentifier:
- _objc_msgSend$_initWithSyncBubble:isFPFS:
- _objc_msgSend$_initializeSourceAndQueues
- _objc_msgSend$_invalidateLowMemory
- _objc_msgSend$_invalidateRequestsTableWithNewSource:
- _objc_msgSend$_loadObjectForKey:inheritFromGlobal:suiteName:validateWithBlock:
- _objc_msgSend$_pauseScheduling
- _objc_msgSend$_pauseStageHandlerScheduling
- _objc_msgSend$_progressForDocument:group:totalUnitCount:completedUnitCount:
- _objc_msgSend$_publish
- _objc_msgSend$_purgeSpaceUnderQueue:withUrgency:
- _objc_msgSend$_recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:
- _objc_msgSend$_recreateSyncBudgetsAndThrottlesIfNeeded
- _objc_msgSend$_registerBackgroundXPCActivities
- _objc_msgSend$_resumeAllDownloadStreams
- _objc_msgSend$_resumeScheduling
- _objc_msgSend$_resumeStageHandlerScheduling
- _objc_msgSend$_sendJob:toStageHandlerWithStageID:
- _objc_msgSend$_setStageJobCompletionHandlers
- _objc_msgSend$_setupBGSystemTaskCompletionFor:
- _objc_msgSend$_setupCacheDelete
- _objc_msgSend$_unpublish
- _objc_msgSend$_updateSubmittedBGSystemTasksWithState:
- _objc_msgSend$_updateSubmittedBGSystemTasksWithState:submittedBGSystemTaskIdentifiers:
- _objc_msgSend$_updateToBeProgressForDocument:group:totalUnitCount:completedUnitCount:
- _objc_msgSend$_updateWifiOnlyBGSystemTaskWithCancelledTaskIdentifiers:inexpensiveNetworkConnectivity:
- _objc_msgSend$_updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:
- _objc_msgSend$_vacuumDB:amount:withUrgency:
- _objc_msgSend$_validateStageHandlers
- _objc_msgSend$accessTimeDeltaInHighUrgency
- _objc_msgSend$accessTimeDeltaInLowUrgency
- _objc_msgSend$accessTimeDeltaInMedUrgency
- _objc_msgSend$accessTimeDeltaInVeryHighUrgency
- _objc_msgSend$activeStageID
- _objc_msgSend$addJob:
- _objc_msgSend$addJob:withGroupIdentifier:
- _objc_msgSend$addOperation:allowsCellularAccess:asCompletionOf:
- _objc_msgSend$addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:
- _objc_msgSend$addReference
- _objc_msgSend$addSubOperation:asCompletionOf:
- _objc_msgSend$advanceJobToInitialStage
- _objc_msgSend$advanceJobToNextStage
- _objc_msgSend$advanceToRecoveryStage:
- _objc_msgSend$aliasSourceAppLibraryID
- _objc_msgSend$brc_containerResetErrorForSharedZone:resetReason:
- _objc_msgSend$brc_errorCantCallFPInSyncBubble
- _objc_msgSend$brc_errorCantRegisterBGSystemTask
- _objc_msgSend$cacheDeletePushBGSystemTaskConfig
- _objc_msgSend$cachedNonPurgeableSpace
- _objc_msgSend$cachedPurgeableSpaceForUrgency:
- _objc_msgSend$cancelJob:
- _objc_msgSend$cancelTaskRequestWithIdentifier:error:
- _objc_msgSend$completeWithError:
- _objc_msgSend$computePurgeableSpaceForAllUrgenciesWithReply:
- _objc_msgSend$contentPolicyForItemInfo:sessionContext:
- _objc_msgSend$contentPolicyForRootContainerWithSessionContext:
- _objc_msgSend$costForJob:
- _objc_msgSend$dbFixupContentPolicyRecoverAfterTimeInterval
- _objc_msgSend$defaultManagerWithPersonaIdentifier:
- _objc_msgSend$defaultOnDiskAccessTimeDefaultForEviction
- _objc_msgSend$defaultTimeDeltaForEviction
- _objc_msgSend$deleteAllSearchableItemsWithCompletionHandler:
- _objc_msgSend$dequeueHighestQualityOfServiceJobsWithHandler:
- _objc_msgSend$dictionaryForKey:
- _objc_msgSend$didReceiveMemoryWarning
- _objc_msgSend$disableScheduling
- _objc_msgSend$discretionaryOperationBGSystemTaskConfigForBackgroundContext
- _objc_msgSend$discretionaryOperationBGSystemTaskConfigForForegroundContext
- _objc_msgSend$discretionaryOperationBGSystemTaskConfigWithForegroundState:
- _objc_msgSend$downloadStatus
- _objc_msgSend$dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:
- _objc_msgSend$enableScheduling
- _objc_msgSend$enumerateIndexesWithOptions:usingBlock:
- _objc_msgSend$exceptionWithName:reason:userInfo:
- _objc_msgSend$finishRequestForIdentifer:finishError:error:
- _objc_msgSend$garbageCollectSpace:
- _objc_msgSend$graveyardAgeDeltaInLowUrgency
- _objc_msgSend$graveyardAgeDeltaInMedUrgency
- _objc_msgSend$groupByIdentifierForJob:
- _objc_msgSend$handleJobsBatch:
- _objc_msgSend$indexGreaterThanIndex:
- _objc_msgSend$initAsGlobalWithServerConfiguration:
- _objc_msgSend$initWithCacheDirPath:
- _objc_msgSend$initWithDocumentItem:client:sessionContext:downloadTrackersManager:
- _objc_msgSend$initWithDocumentItem:client:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:
- _objc_msgSend$initWithGroup:session:
- _objc_msgSend$initWithName:protectionClass:
- _objc_msgSend$initWithOptions:
- _objc_msgSend$initWithProgress:requestType:finishBlock:
- _objc_msgSend$initWithQualityOfService:completionHandler:
- _objc_msgSend$initWithServerConfiguration:globalUserDefaults:clientZoneIdentifier:
- _objc_msgSend$initWithShareMetadata:client:sessionContext:userNotifier:userActionsNavigator:
- _objc_msgSend$invalidateRequestsOfClient:
- _objc_msgSend$isCancellable
- _objc_msgSend$isIndexingAvailable
- _objc_msgSend$isReadonly
- _objc_msgSend$itemIDsBlockedFromSyncForCZMProcessing
- _objc_msgSend$jobPlan
- _objc_msgSend$lastIndex
- _objc_msgSend$maxJobsPerBatch
- _objc_msgSend$needsToHandleJob:
- _objc_msgSend$needsToHandleJob:asRequestedByStage:
- _objc_msgSend$objectForKey:inheritFromGlobal:suiteName:validateWithBlock:
- _objc_msgSend$parentsOfCZMFaults
- _objc_msgSend$perJobCompletionHandler
- _objc_msgSend$performOptimizeStorageWithTimeDelta:onDiskAccessTimeDelta:error:
- _objc_msgSend$performWithSessionForVolume:action:
- _objc_msgSend$pipelineAutoResumeTimeout
- _objc_msgSend$postContainerStatusChangeNotificationWithID:key:value:
- _objc_msgSend$progressToReplaceUploadProgress:
- _objc_msgSend$purgeGraveyardSpace:withUrgency:
- _objc_msgSend$purgeSpace:withUrgency:
- _objc_msgSend$raise
- _objc_msgSend$readerThrottleParams
- _objc_msgSend$recoverAndReportContentPolicyWithCompletion:
- _objc_msgSend$releaseReference
- _objc_msgSend$removeJob:withGroupIdentifier:
- _objc_msgSend$requestedAdditionalStages
- _objc_msgSend$requiresInexpensiveNetworkConnectivity
- _objc_msgSend$scheduleResetServerAndClientTruthsForReason:
- _objc_msgSend$scheduleResetServerAndClientTruthsForReason:completionHandler:
- _objc_msgSend$setGroupConcurrencyLimit:
- _objc_msgSend$setGroupName:
- _objc_msgSend$setJobPlan:additionalToRequestingStageMap:
- _objc_msgSend$setPerJobCompletionHandler:
- _objc_msgSend$setRequiresInexpensiveNetworkConnectivity:
- _objc_msgSend$setSession:group:
- _objc_msgSend$setStageStringifier:
- _objc_msgSend$setSystemTask:
- _objc_msgSend$setupWithInternalPipelineJobCompletionHandler:
- _objc_msgSend$shouldForceApplyContentForItem:
- _objc_msgSend$simpleUrgencyForCacheDeleteUrgency:
- _objc_msgSend$softCostLimit
- _objc_msgSend$spotlightIndexingEnabled
- _objc_msgSend$subclassDescription
- _objc_msgSend$submittedBGSystemTaskIdentifiers
- _objc_msgSend$systemTask
- _objc_msgSend$taskRequestForIdentifier:
- _objc_msgSend$updateTaskRequest:error:
- _objc_msgSend$uploadProgressForDocument:totalUnitCount:completedUnitCount:
- _objc_msgSend$urgencyForCacheDeleteUrgency:
- _objc_msgSend$useBGSTForSchedulingDiscretionaryOperations
- _objc_msgSend$writeToURL:atomically:
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
- _scheduleResetServerAndClientTruthsForReason:completionHandler:.onceToken
- _scheduleResetServerAndClientTruthsForReason:completionHandler:.reasonsToIgnoreForABC
CStrings:
+ " receiver"
+ "(current user)"
+ "+[BRCRFAEmailSettingHandler isEmailSettingEnabledWithSyncContext:reply:]"
+ "+[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:]"
+ "+[BRCRFAEmailSettingHandler setEmailSettingEnabled:syncContext:reply:]_block_invoke"
+ "+[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToPCSChainingItem:fullyChainedParentIDs:]"
+ "-[BRCAccountSession _loadSyncEngine]"
+ "-[BRCAccountSession _recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke"
+ "-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke"
+ "-[BRCAccountSession _registerBackgroundSystemTasks]_block_invoke_2"
+ "-[BRCAccountSession enableEnhancedDrivePrivacyForZone:ownerName:completionHandler:]"
+ "-[BRCAccountSession enableEnhancedDrivePrivacyForZone:ownerName:completionHandler:]_block_invoke"
+ "-[BRCAccountSession fileProviderItemIdentifierForItemIdentifierString:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession fileProviderItemIdentifierForItemIdentifierString:zoneName:ownerName:completionHandler:]_block_invoke"
+ "-[BRCAccountSession generateRequestIDForZone:ownerName:completionHandler:]"
+ "-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:]_block_invoke"
+ "-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession locateItemWithIdentifier:zoneName:ownerName:completionHandler:]_block_invoke"
+ "-[BRCAccountSession updatePCSStateForItemIdentifier:newState:zoneName:ownerName:completionHandler:]"
+ "-[BRCAccountSession updatePCSStateForItemIdentifier:newState:zoneName:ownerName:completionHandler:]_block_invoke"
+ "-[BRCAccountSession waitForSyncDownOfZone:ownerName:completionHandler:]"
+ "-[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:]"
+ "-[BRCClientZone _cancelAndWaitForRunningOperations:dispatchOnDbQueue:]_block_invoke"
+ "-[BRCClientZone _initializeZoneActiveStateIfNeeded]"
+ "-[BRCClientZone _invalidateZoneActiveStateIfNeeded]"
+ "-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke_2"
+ "-[BRCClientZone plist]"
+ "-[BRCClientZone postContainerStatusChangeNotificationForKey:value:]"
+ "-[BRCClientZone scheduleResetServerAndClientTruthsWithError:completionHandler:]"
+ "-[BRCClientZone scheduleSyncUp]"
+ "-[BRCClientZone waitForSyncDownWithCompletionHandler:]"
+ "-[BRCClientZone waitForSyncDownWithCompletionHandler:]_block_invoke"
+ "-[BRCClientZoneActiveState updateFromPlist:]"
+ "-[BRCDaemon start]_block_invoke_4"
+ "-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke"
+ "-[BRCDiskSpaceReclaimer computePurgeableSpaceWithReply:]_block_invoke_3"
+ "-[BRCDiskSpaceReclaimer resume]_block_invoke"
+ "-[BRCFileUnlinker init]"
+ "-[BRCFileUnlinker resumeWithTapToRadarManager:]"
+ "-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]"
+ "-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:]_block_invoke_2"
+ "-[BRCMigrationQueryOperation _updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:]"
+ "-[BRCNotification initWithFileProviderItem:appLibraryID:]"
+ "-[BRCProgress brc_publish]"
+ "-[BRCProgress brc_unpublish]"
+ "-[BRCProgress initUploadProgressForDocument:totalUnitCount:completedUnitCount:]"
+ "-[BRCProgress initWithUploadProgress:]"
+ "-[BRCServerItem appLibrary]"
+ "-[BRCServerItem isTrashed]"
+ "-[BRCServerItem itemType]"
+ "-[BRCSharedServerItem appLibrary]"
+ "-[BRCStageRegistry garbageCollectSpace]"
+ "-[BRCStageRegistry purgeGraveyardSpace]"
+ "-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:]"
+ "-[BRCSyncContext _setupCKContainerIfNeeded]"
+ "-[BRCSyncContext _setupDownloadStreamsIfNeeded]_block_invoke"
+ "-[BRCSyncContext _setupUploadStreamIfNeeded]_block_invoke"
+ "-[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:]"
+ "-[BRCSyncContext reclaimMemoryIfPossible]_block_invoke"
+ "-[BRCSyncContext reclaimMemoryIfPossible]_block_invoke_2"
+ "-[BRCSyncUpOperation _localItemFromRecord:inZone:validateSyncUpState:]"
+ "-[BRCSystemResourcesManager _initReclaimMemory]"
+ "-[BRCSystemResourcesManager _initReclaimMemory]_block_invoke_3"
+ "-[BRCSystemResourcesManager _reclaimMemoryFromObserversDueToMemoryPressure:]"
+ "-[BRCUserDefaults _handleGlobalFallbackForKey:validateWithBlock:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:doNotObfuscate:reply:]"
+ "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:doNotObfuscate:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient computePurgeableSpaceWithReply:]"
+ "-[BRCXPCRegularIPCsClient computePurgeableSpaceWithReply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient handleUserNotificationResponse:reply:]"
+ "-[BRCXPCRegularIPCsClient handleUserNotificationResponse:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient isAccountCZM:]"
+ "-[BRCXPCRegularIPCsClient isRFAEmailSettingEnabledWithReply:]"
+ "-[BRCXPCRegularIPCsClient isRFAEmailSettingEnabledWithReply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient reclaimDiskSpaceWithReply:]"
+ "-[BRCXPCRegularIPCsClient reclaimDiskSpaceWithReply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient setRFAEmailSettingEnabled:reply:]"
+ "-[BRCXPCRegularIPCsClient setRFAEmailSettingEnabled:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke_2"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) getFPItemIDsForCKRecordIDs:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:]_block_invoke_2"
+ "-[BRFieldXattrBlob(FPFSAdditions) extendedAttributesDictionary]"
+ "-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:matchedError:]_block_invoke"
+ "-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke"
+ "-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke_2"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/account/BRCAccountSession.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/account/BRCAccountsManager.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCClientZone.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCContainerScheduler.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/containers/BRCServerZone.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/daemon/BRCDaemon.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCClientDatabaseFacade.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCClientState.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseManager.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseSchema.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/database/BRCServerPersistedState.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/foundation/BRCFairScheduler.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/foundation/BRCPQLConnection.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/items/BRCItemID.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/notifs/BRCAccountHandler.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/Library/Caches/com.apple.xbs/0FD35CCE-4CE2-4733-8E70-63767E5BD155/TemporaryDirectory.NhdZbO/Sources/CloudDocs_plugins/core/shared/sync/transfers/BRCTransferStream.m"
+ "<%@[%@] %@ {client:%@ server:%@ sync:%@ %@ zoneActiveState:{%@} appuninstalled:%@}>"
+ "@\"<OSServerItem>\"24@0:8@\"NSString\"16"
+ "@\"<OSServerItem>\"40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
+ "@\"<OSServerItem>\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
+ "@\"<SyncEngineProtocol>\""
+ "@\"BRCClientZoneActiveState\""
+ "@\"BRCItemID\"36@0:8@\"BRCItemID\"16@\"BRCZoneRowID\"24B32"
+ "@\"BRCItemID\"60@0:8@\"BRCItemID\"16@\"BRCZoneRowID\"24B32^c36^q44^c52"
+ "@\"NSOperation\"40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "@\"NSProgress\"56@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@\"NSFileProviderRequest\"40@?<v@?@\"NSError\">48"
+ "@\"NSProgress\"72@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"NSURL\"40Q48@\"NSFileProviderRequest\"56@?<v@?@\"<NSFileProviderItem>\"QB@\"NSError\">64"
+ "@\"NSProgress\"72@0:8@\"<NSFileProviderItem>\"16@\"iCDCreateItemContext\"24Q32@\"NSURL\"40Q48@\"NSFileProviderRequest\"56@?<v@?@\"<NSFileProviderItem>\"QB@\"NSError\">64"
+ "@100@0:8@16@24@32@40@48@56@64@72@80Q88I96"
+ "@40@0:8@\"NSString\"16@\"<OSServiceProviderProtocol>\"24@\"NSURL\"32"
+ "@60@0:8@16@24B32^c36^q44^c52"
+ "@72@0:8@16@24Q32@40Q48@56@?64"
+ "ALTER TABLE client_items DROP COLUMN desired_version"
+ "B44@0:8@16c24q28q36"
+ "BRCClientZoneActiveState"
+ "BRCRFAEmailSettingHandler"
+ "BRCReclaimMemoryDelegate"
+ "CLIENT_DB_STATEMENTS_CACHE_COUNT"
+ "Can't reset, zone is deactivated"
+ "DISABLED"
+ "DISK_SPACE_RECLAIMED"
+ "DROP INDEX \"client_items/version_block_sync_until_timestamp\""
+ "DROP INDEX IF EXISTS \"client_items/download_index\""
+ "DROP INDEX IF EXISTS \"client_items/download_job\""
+ "DROP INDEX IF EXISTS \"client_items/pending_download_docs\""
+ "ENABLED"
+ "Failed getting internal daemon container"
+ "FileProvider"
+ "I20@0:8I16"
+ "ICLOUD_DRIVE_USER_NOTIFICATION_REQUEST_BUTTON_APPROVE"
+ "ICLOUD_DRIVE_USER_NOTIFICATION_REQUEST_BUTTON_DECLINE"
+ "OSServerItem"
+ "OSServiceProviderProtocol"
+ "OSSyncEngine"
+ "Q36@0:8B16^@20^@28"
+ "RSA Email (retrieve)"
+ "RSA Email (update)"
+ "Reset"
+ "RetrieveBladeRunnerConfig"
+ "SELECT si.zone_rowid, si.item_rank, si.item_origname, si.pcs_state, si.item_id, si.item_creator_id, si.item_sharing_options, si.item_side_car_ckinfo, si.item_stat_ckinfo, si.item_state, si.item_type, si.item_mode, si.item_birthtime, si.item_lastusedtime, si.item_favoriterank,si.item_parent_id, si.item_filename, si.item_hidden_ext, si.item_finder_tags, si.item_xattr_signature, si.item_trash_put_back_path, si.item_trash_put_back_parent_id, si.item_alias_target, si.item_creator, si.version_name, si.version_ckinfo, si.version_mtime, si.version_size, si.version_thumb_size, si.version_thumb_signature, si.version_content_signature, si.version_xattr_signature, si.version_edited_since_shared, si.version_device, si.version_conflict_loser_etags, si.version_quarantine_info, si.child_basehash_salt, si.salting_state, si.basehash_salt_validation_key, si.quota_used, si.recursive_child_count, si.shared_children_count, si.shared_alias_count, si.child_count FROM server_items as si INNER JOIN client_items as ci  ON ci.rowid = %lld and ci.zone_rowid = si.zone_rowid and ci.item_id = si.item_id"
+ "StringAsFormatVersion:"
+ "Sync up (PCS chain)"
+ "SyncEngineProtocol"
+ "T@\"<NSObject>\",&,N,V_hasWorkDidUpdateObserver"
+ "T@\"<SyncEngineProtocol>\",R,N,V_syncEngine"
+ "T@\"BRCDeadlineSource\",&,N,V_syncDeadlineSource"
+ "T@\"BRCDeadlineSource\",R,N"
+ "T@\"BRCFetchRecentAndFavoriteDocumentsOperation\",&,N,V_fetchRecentsOperation"
+ "T@\"BRCSyncBudgetThrottle\",&,N,V_syncUpBudget"
+ "T@\"BRCSyncDownOperation\",&,N,V_syncDownOperation"
+ "T@\"BRCSyncOperationBackoffRatio\",&,N,V_syncUpBackoffRatio"
+ "T@\"BRCSyncOperationThrottle\",&,N,V_syncDownThrottle"
+ "T@\"BRCSyncOperationThrottle\",&,N,V_syncUpThrottle"
+ "T@\"BRCSyncUpOperation\",&,N,V_syncUpOperation"
+ "T@\"BRCThrottle\",&,N,V_locateRecordsOperationThrottle"
+ "T@\"BRCThrottle\",&,N,V_serverStitchingOperationThrottle"
+ "T@\"BRCThrottleBase\",R,N"
+ "T@\"BRCTransferStream\",R,N"
+ "T@\"BRTimer\",&,N,V_resetAfterAppUninstallTimer"
+ "T@\"CKOperationGroup\",&,N,V_syncDownGroup"
+ "T@\"NSArray\",&,N,V_syncThrottles"
+ "T@\"NSDate\",&,N"
+ "T@\"NSError\",&,N,V_lastSyncDownError"
+ "T@\"NSError\",&,N,V_lastSyncUpError"
+ "T@\"NSMutableArray\",&,N,V_allItemsDidUploadTrackers"
+ "T@\"NSMutableArray\",&,N,V_blockedOperationsOnInitialSync"
+ "T@\"NSMutableArray\",&,N,V_currentSyncDownBarriers"
+ "T@\"NSMutableArray\",&,N,V_directoriesCreatedLastSyncUp"
+ "T@\"NSMutableArray\",&,N,V_faultsLiveBarriers"
+ "T@\"NSMutableArray\",&,N,V_nextIdleHandlers"
+ "T@\"NSMutableArray\",&,N,V_nextSyncDownBarriers"
+ "T@\"NSMutableArray\",&,N,V_outOfBandSyncOperations"
+ "T@\"NSMutableArray\",&,N,V_syncDownCompletionHandlers"
+ "T@\"NSMutableArray\",&,N,V_syncDownDependencies"
+ "T@\"NSMutableDictionary\",&,N,V_downloadedBlockToPerformForItemID"
+ "T@\"NSMutableDictionary\",&,N,V_fetchParentOperations"
+ "T@\"NSMutableDictionary\",&,N,V_locateBlocksToPerformForRecordID"
+ "T@\"NSMutableDictionary\",&,N,V_locateRecordOperations"
+ "T@\"NSMutableDictionary\",&,N,V_onDiskBlockToPerformForItemID"
+ "T@\"NSMutableDictionary\",&,N,V_recursiveListOperations"
+ "T@\"NSMutableDictionary\",&,N,V_runningListOperations"
+ "T@\"NSMutableDictionary\",&,N,V_syncDownBlockToPerformForBookmarkData"
+ "T@\"NSMutableDictionary\",&,N,V_syncDownBlockToPerformForItemID"
+ "T@\"NSMutableIndexSet\",&,N,V_appliedTombstoneRanks"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_resetTimer"
+ "T@\"NSString\",&,N,V_osNameRequiredToSync"
+ "T@\"NSString\",&,N,V_parentZoneEtag"
+ "T@\"NSString\",&,N,V_sideCarEtag"
+ "T@\"UMUserSyncTask\",&,N,V_bubbleSyncTask"
+ "T@\"brc_task_tracker\",R,N"
+ "T@,N,V_syncDeadlineSourceResumer"
+ "TB,N,V_invokeFetchRecentsOperation"
+ "TB,N,V_lastSyncUpErrorWasOnChainedItem"
+ "TB,N,V_shouldShowiCloudDriveAppInstallationNotification"
+ "TQ,N,V_requestID"
+ "Tc,R,N,V_group"
+ "Tf,N,V_syncUpBatchSizeMultiplier"
+ "Ti,N,V_formatVersion"
+ "Tq,N,V_lastInsertedRank"
+ "Tq,N,V_syncUpRetryAfter"
+ "UPDATE client_items SET version_upload_error = NULL, item_notifs_rank = bump_notifs_rank_and_trigger_notifs(rowid) WHERE rowid IN (SELECT throttle_id FROM client_uploads WHERE throttle_state = %u)"
+ "UPDATE client_uploads SET throttle_state = 1, upload_error = NULL WHERE throttle_state = %u"
+ "Unlinker"
+ "UpdateBladeRunnerConfig"
+ "V1"
+ "V2"
+ "WITH RECURSIVE item_parents (item_id, item_sharing_options, item_parent_id) AS (     SELECT item_id, item_sharing_options, item_parent_id       FROM %@      WHERE zone_rowid = %@ AND item_id = %@  UNION ALL     SELECT p.item_id, p.item_sharing_options, p.item_parent_id       FROM %@ AS p INNER JOIN item_parents AS c      WHERE p.zone_rowid = %@        AND c.item_parent_id = p.item_id      LIMIT %u) SELECT item_id FROM item_parents WHERE (item_sharing_options & 4) != 0"
+ "WITH RECURSIVE item_parents (item_id, item_state, item_type, depth) AS (     SELECT item_id, item_state, item_type, 0       FROM %@      WHERE zone_rowid = %@ AND item_id = %@  UNION ALL     SELECT p.item_parent_id, c.item_state, c.item_type, c.depth + 1       FROM %@ AS p INNER JOIN item_parents AS c USING (item_id)      WHERE p.zone_rowid = %@      LIMIT %u) SELECT item_state, depth, item_type, item_id FROM item_parents WHERE item_id_is_root(item_id) OR item_type = 4"
+ "[9@\"NSString\"]"
+ "[CRIT] Assertion failed: ![self hasHighPriorityWatchers]%@"
+ "[CRIT] Assertion failed: !_clientZoneIdentifier%@"
+ "[CRIT] Assertion failed: !_deferredPlist%@"
+ "[CRIT] Assertion failed: !_zoneActiveState%@"
+ "[CRIT] Assertion failed: !localNSUserDefaultsTargetDict || localNSUserDefaultIsDictionary%@"
+ "[CRIT] Assertion failed: !self->_zoneActiveState.resetTimer%@"
+ "[CRIT] Assertion failed: !self.isCloudDocsZone && !self.isSharedZone && self.isSyncBlocked%@"
+ "[CRIT] Assertion failed: [self _memoryOptimizationEnabled] && ![self _isResetting] && self.isSyncBlocked && self.isPrivateZone%@"
+ "[CRIT] Assertion failed: [self _memoryOptimizationEnabled] && self.isSyncBlocked && self.isPrivateZone%@"
+ "[CRIT] Assertion failed: [self _memoryOptimizationEnabled]%@"
+ "[CRIT] Assertion failed: _zoneActiveState.syncDownOperation == nil%@"
+ "[CRIT] Assertion failed: _zoneActiveState.syncUpOperation == nil%@"
+ "[CRIT] Assertion failed: errcode == 0%@"
+ "[CRIT] Assertion failed: isFixingState || (_zoneActiveState.requestID == 0 || requestID <= _zoneActiveState.requestID) isFixingState = %d, _requestID = %llu, requestID = %llu, zone = %@%@"
+ "[CRIT] Assertion failed: itemID.appLibraryRowID != nil%@"
+ "[CRIT] Assertion failed: key != nil && value != nil%@"
+ "[CRIT] UNREACHABLE: Couldn't initialize _flags.kind from the content type %@ for %@%@"
+ "[CRIT] UNREACHABLE: Error while getting the internal daemon container path %@%@"
+ "[CRIT] UNREACHABLE: Failed to find top-level shared item for child item %@%@"
+ "[CRIT] UNREACHABLE: No client zone found for %@ [%@]%@"
+ "[CRIT] UNREACHABLE: No server zone found for %@ [%@]%@"
+ "[CRIT] UNREACHABLE: SyncEngine doesn't conform to the sync engine protocol%@"
+ "[CRIT] UNREACHABLE: Unable to load context class%@"
+ "[CRIT] UNREACHABLE: Unexpected item type %d%@"
+ "[CRIT] UNREACHABLE: Unsupported record type %@%@"
+ "[CRIT] UNREACHABLE: Zone %@:%@ not found%@"
+ "[CRIT] UNREACHABLE: isTrashed is uploadv2 only%@"
+ "[DEBUG] %@ - Queueing faults live barrier for %@%@"
+ "[DEBUG] %@ finished record fetcher%@"
+ "[DEBUG] Activated zone active state%@"
+ "[DEBUG] Allocating zone active state for %@%@"
+ "[DEBUG] Applying deferred plist for zone %@, plist = %@%@"
+ "[DEBUG] Calling resetCompletionHandler for %@%@"
+ "[DEBUG] Checking the value of rfa email setting%@"
+ "[DEBUG] Done Force Ingestion of %@ to update the content or namespace policy - %@%@"
+ "[DEBUG] Enabling enhanced drive privacy for zone %@ [%@]%@"
+ "[DEBUG] Finished fixing namespace and content policy after upgrade with %llu problems%@"
+ "[DEBUG] Ignoring documents directory creation in the sync engine%@"
+ "[DEBUG] Invaldiating zone active state for %@%@"
+ "[DEBUG] Item %@ has unexpected namespace policy. Expected:%ld Actual:%ld%@"
+ "[DEBUG] Learning new item identifier %@ for old item %@%@"
+ "[DEBUG] Locating item with identifier %@ in zone %@%@"
+ "[DEBUG] Not doing a database migration on an offline database where the major version matches%@"
+ "[DEBUG] Not reclaiming memory for %@ - not idle long enough (%.1fs < %.1fs)%@"
+ "[DEBUG] Reclaiming memory for %@%@"
+ "[DEBUG] Reclaiming memory from observers%@"
+ "[DEBUG] Running memory reclaimer task%@"
+ "[DEBUG] Scheduling zone reset on %@%@"
+ "[DEBUG] Skipping sync job scheduler fixing up in uploadv2%@"
+ "[DEBUG] Sync Engine create item finished with error %@%@"
+ "[DEBUG] Sync Engine delete item finished with error %@%@"
+ "[DEBUG] UpdateBladeRunnerConfig query operation finished with %@%@"
+ "[DEBUG] Updating PCS chain state for item %@ to state %u%@"
+ "[DEBUG] Using sync engine to create item%@"
+ "[DEBUG] Using sync engine to delete item%@"
+ "[DEBUG] Using sync engine to modify item%@"
+ "[DEBUG] We are denylisted from %@ because %d > %d[std] %d[int+car:%s] %d[car:%s] and %d[int:%s]%@"
+ "[DEBUG] We are not denylisted from %@ %d vs %d%@"
+ "[DEBUG] We are not denylisted from %@ because we are on an internal build %d vs %d%@"
+ "[DEBUG] We are not denylisted from %@ because we are on an internal build and in carry %d vs %d%@"
+ "[DEBUG] We are not denylisted from %@ chaining because we are in carry %d vs %d%@"
+ "[DEBUG] added %@ as a sync-down dependency%@"
+ "[DEBUG] broadcasting to framework clients zone %@ change %@=%@%@"
+ "[DEBUG] download group container stage size from stage is %@%@"
+ "[DEBUG] removed %@ as a sync-down dependency%@"
+ "[DEBUG] returning purgeable info from cache\npurgeableSpace:%@\nnonPurgeableSpace:%@%@"
+ "[DEBUG] setEmailSettingEnabled called with %d%@"
+ "[DEBUG] ┏%llx Reclaiming Space...%@"
+ "[DEBUG] ┣%llx %@ - waiting for sync down to complete%@"
+ "[DEBUG] ┳%llx container-metadata received server change token %@, caught-up:%s client change token %@ error:%@%@"
+ "[DEBUG] ┳%llx forcing sync down and waiting for completion%@"
+ "[DEBUG] ┳%llx timed out waiting for idle%@"
+ "[ERROR] %@: EINTR: client gather phase was invalidated, cb %@%@"
+ "[ERROR] Should not schedule sync up in uploadV2%@"
+ "[INFO] %@: reply(%@, %d, %d, %@)%@"
+ "[INFO] %@: reply(%@, %lu, %d, %@)%@"
+ "[NOTIF] Receiver is nil, invalidating the gatherer%@"
+ "[WARNING] New item ID %@ already exists for a different item%@"
+ "[WARNING] No client zone found for %@ [%@]%@"
+ "[WARNING] No local item found for item ID %@%@"
+ "[WARNING] No local item found for old item ID %@%@"
+ "[WARNING] No server item found for item ID %@%@"
+ "[WARNING] completionHandler cannot be nil%@"
+ "[WARNING] no BRCItemID found for %@:%@; %@%@"
+ "[WARNING] no fpItemID found for %@:%@%@"
+ "__performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:completion:"
+ "_activateZoneActiveStateIfNeededWithOrigState:"
+ "_activeOperationAdds"
+ "_addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:"
+ "_addSubOperation:overrideContext:allowsCellularAccess:"
+ "_cacheValueLocally:forKey:"
+ "_cancelAndWaitForRunningOperations:dispatchOnDbQueue:"
+ "_checkIfShouldDedicateOpToPCSChainingItem:fullyChainedParentIDs:"
+ "_checkLocalCacheForKey:inherit:validateWithBlock:"
+ "_checkLocalNSUserDefaultsForKey:validateWithBlock:"
+ "_checkServerOverrideForKey:validateWithBlock:"
+ "_clearErrorForRecord:inZone:"
+ "_closeHandlersAndBarriersBlocks"
+ "_computeIsTrashed"
+ "_deferredPlist"
+ "_deferredPlistFromPlist:"
+ "_downloadGroupContainerStageSize"
+ "_formatVersion"
+ "_garbageCollectSpace"
+ "_getPrivateClientZone"
+ "_handleGlobalFallbackForKey:validateWithBlock:"
+ "_hasAnyItemInZoneOtherThanDocumentsFolder"
+ "_initReclaimMemory"
+ "_initWithItemID:ownerKey:sideCarCKInfo:st:latestVersion:serverMetrics:serverZone:clientZone:session:sharingOptions:pcsChainState:"
+ "_initWithSyncBubble:"
+ "_initializeZoneActiveStateIfNeeded"
+ "_internalDaemonContainerError"
+ "_invalidateReclaimMemory"
+ "_invalidateZoneActiveStateIfNeeded"
+ "_isResetting"
+ "_isTrashed"
+ "_lastActivityDate"
+ "_loadSyncEngine"
+ "_localItemFromRecord:inZone:validateSyncUpState:"
+ "_localNSUserDefaultsDict"
+ "_memoryOptimizationEnabled"
+ "_moveOldUnlinkDir"
+ "_nillifyMembers"
+ "_parentZoneEtag"
+ "_personaToUserDefaultsManager"
+ "_prepopulateLocalNSUserDefaults"
+ "_purgeSpaceUnderQueue"
+ "_reclaimMemoryFromObserversDueToMemoryPressure:"
+ "_reclaimMemoryObservers"
+ "_recoverNamespaceAndContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:"
+ "_registerBackgroundSystemTasks"
+ "_sendCachedStatementsCountTelemetryEvent"
+ "_sendZoneResetAnalyticsAndTTRForError:resetReason:alternativeError:"
+ "_setupCKContainerIfNeeded"
+ "_setupDownloadStreamsIfNeeded"
+ "_setupOperationQueuesIfNeeded"
+ "_setupUploadStreamIfNeeded"
+ "_sideCarEtag"
+ "_syncDownCompletionHandlers"
+ "_syncEngine"
+ "_trashItemID"
+ "_updatedContinuationCursor:fetchedRecords:alreadyOnServerTruth:reply:"
+ "_zoneActiveState"
+ "abc.ignored-clouddocs-errors-reset"
+ "addOperation:allowsCellularAccess:"
+ "addReclaimMemoryObserver:"
+ "addToPlist:"
+ "allItemsDidUploadTrackers"
+ "alloc"
+ "backupDatabaseWithURLWrapper:doNotObfuscate:reply:"
+ "bird.memory-client-zone-optimization"
+ "bird.memory-reclaimer-bg-system-task-enabled"
+ "bird.memory-reclaimer.bgst"
+ "bird.sync-context-memory-reclaimer-idle-time"
+ "blockedOperationsOnInitialSync"
+ "br_fixup_namspace_and_contentPolicy_block_invoke_2"
+ "br_isFileType"
+ "br_rsaEmailSettingRetrieve"
+ "br_rsaEmailSettingUpdate"
+ "br_syncUpForPCSChain"
+ "brc_containerResetErrorForSharedZone:resetReason:matchedError:"
+ "brc_errorZoneResetCrashRecovery"
+ "brc_errorZoneResetHierarchyTooDeep"
+ "brc_errorZoneResetOrphanLive"
+ "brc_errorZoneResetOrphanTombstone"
+ "brc_errorZoneResetStillWantsDataUnlinked"
+ "brc_errorZoneResetZoneBecameHealthy"
+ "bubbleSyncTask"
+ "checkIfShouldDedicateOpToPCSChainingItem:"
+ "clientZoneMemoryOptimizationEnabled"
+ "com.apple.bird.memory-reclaimer"
+ "com.apple.bird.periodic-disk-space-reclaimer"
+ "computePurgeableSpaceWithReply:"
+ "contentAndNamespacePolicyForItemInfo:sessionContext:contentPolicy:namespacePolicy:"
+ "contentAndNamespacePolicyForRootContainerWithSessionContext:contentPolicy:namespacePolicy:"
+ "contentETag"
+ "contentExtendedAttributesSignature"
+ "createItemBasedOnTemplate:createItemContext:fields:contents:options:request:completionHandler:"
+ "createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:"
+ "createPCSChainOperationForItem:"
+ "creationTime"
+ "currentSyncDownBarriers"
+ "dbFixupNamespaceAndContentPolicyRecoverAfterTimeInterval"
+ "decreaseSyncUpBatchSizeAfterError"
+ "deleteItemWithIdentifier:baseVersion:options:request:completionHandler:"
+ "directoriesCreatedLastSyncUp"
+ "disk-space-reclaimer-threshold-for-sending-telemetry"
+ "disk-space-reclaimer.max-graveyard-time"
+ "diskSpaceReclaimedThresholdForSendingTelemetry"
+ "distinctCachedStatementsCount"
+ "downloadedBlockToPerformForItemID"
+ "downloadingError"
+ "enableEnhancedDrivePrivacyForZone:ownerName:completionHandler:"
+ "extendedAttributesDictionary"
+ "failed getting internal daemon container"
+ "faultsLiveBarriers"
+ "fetchAndClearSyncStateBits:"
+ "fetchAndSetSyncStateBits:"
+ "fetchParentOperations"
+ "fetchRecentsOperation"
+ "fetchRootItemIDAboveItemID:zoneRowID:serverTruth:itemState:depth:itemType:"
+ "fetchShareRootItemIDWithSharedChildItemID:zoneRowID:serverTruth:"
+ "fileName"
+ "fileProviderItemIdentifierForItemIdentifierString:zoneName:ownerName:completionHandler:"
+ "fileSystemMode"
+ "finderTagData"
+ "formatVersion"
+ "formatVersionAsString:"
+ "fpfs.namespace-policy-enabled"
+ "fpfsNamespacePolicyEnabled"
+ "garbageCollectSpace"
+ "gave up on resetting"
+ "generateRequestIDForZone:ownerName:completionHandler:"
+ "getFPItemIDsForCKRecordIDs:reply:"
+ "getRequestAccessEmail == 1"
+ "graveyardAgeDelta"
+ "handleNotificationForResponse:completionHandler:"
+ "handleUserNotificationResponse:reply:"
+ "hasFormatVersion"
+ "hasParentZoneEtag"
+ "hasSideCarEtag"
+ "hasSyncedDownZoneSinceStartup:ownerName:completionHandler:"
+ "hasUnresolvedConflicts"
+ "hasWorkDidUpdateObserver"
+ "iCDCreateItemContext"
+ "ignoredInternalCloudDocsErrorCodesForABCInReset"
+ "increaseSyncUpBatchSizeAfterSuccess"
+ "initAsGlobalWithServerConfiguration:localNSUserDefaultsDict:"
+ "initUploadProgressForDocument:totalUnitCount:completedUnitCount:"
+ "initWithAccountID:osServiceProvider:workDirectory:"
+ "initWithDocumentItem:sessionContext:downloadTrackersManager:"
+ "initWithDocumentItem:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:"
+ "initWithFileProviderItem:appLibraryID:"
+ "initWithMangledID:"
+ "initWithReserverItemIDString:reservedFileProviderIdentifier:parentZoneName:parentZoneOwner:parentIdentifier:primaryZoneNeedsCreation:symlinkTarget:"
+ "initWithServerConfiguration:globalUserDefaults:localNSUserDefaultsDict:clientZoneIdentifier:"
+ "initWithShareMetadata:sessionContext:userNotifier:userActionsNavigator:"
+ "initWithUploadProgress:"
+ "internalDaemonContainerPathWithError:"
+ "invokeFetchRecentsOperation"
+ "invokePCSChainOnItem:zoneName:completionHandler:"
+ "isAccountCZM:"
+ "isDownloaded"
+ "isEmailSettingEnabledWithSyncContext:reply:"
+ "isMostRecentVersionDownloaded"
+ "isRFAEmailSettingEnabledWithReply:"
+ "isSharedByCurrentUser"
+ "isTrashed"
+ "isUploaded"
+ "isUploading"
+ "itemIdentifierString"
+ "lastModifiedTime"
+ "lastSyncDownError"
+ "lastSyncUpError"
+ "lastSyncUpErrorWasOnChainedItem"
+ "learnNewItemIdentifier:forItemIdentifier:zoneName:ownerName:completionHandler:"
+ "libos-brain.dylib"
+ "locateBlocksToPerformForRecordID"
+ "locateItemWithIdentifier:zoneName:ownerName:completionHandler:"
+ "locateRecordOperations"
+ "locateRecordsOperationThrottle"
+ "markRequestIDAcked"
+ "markZoneConsolidatedForZone:ownerName:completionHandler:"
+ "memoryReclaimerBGSystemTaskConfig"
+ "memoryReclaimerBGSystemTaskEnabled"
+ "modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:"
+ "modifyItem:baseVersion:changedFields:contents:options:request:completionHandler:"
+ "namespacePolicy"
+ "newClientDBCachedStatementsCountEventWithValue:"
+ "newDiskSpaceReclaimedBytes:"
+ "nextIdleHandlers"
+ "nextSyncDownBarriers"
+ "notifyContainer:isForegroundState:"
+ "obfuscatedDescription"
+ "onDiskBlockToPerformForItemID"
+ "operationCount"
+ "outOfBandSyncOperations"
+ "parentZoneETag"
+ "parentZoneEtag"
+ "pcsChainItem:forZone:sessionContext:"
+ "periodicCacheDeleteBGSystemTaskConfig"
+ "persistentDomainForName:"
+ "postContainerStatusChangeNotificationForKey:value:"
+ "preparePCSForZone:ownerName:completionHandler:"
+ "privateFrameworksURL"
+ "publish"
+ "purgeGraveyardSpace"
+ "purgeSpace"
+ "reclaimDiskSpaceWithReply:"
+ "reclaimMemory"
+ "reclaimMemoryIfPossible"
+ "recoverAndReportNamespaceAndContentPolicyWithCompletion:"
+ "recursiveListOperations"
+ "removeReclaimMemoryObserver:"
+ "requestAccessEmail"
+ "resetAfterAppUninstallTimer"
+ "resetNotifications"
+ "resetTimer"
+ "resumeWithTapToRadarManager:"
+ "rid:%llu"
+ "runningListOperations"
+ "scheduleResetServerAndClientTruthsWithError:"
+ "scheduleResetServerAndClientTruthsWithError:completionHandler:"
+ "se"
+ "serverItemForItemIdentifier:"
+ "serverItemForItemIdentifierString:zoneName:ownerName:"
+ "serverItemFromClientRowID:itemBuilder:"
+ "serverItemWithParent:filename:zoneName:ownerName:"
+ "serverStitchingOperationThrottle"
+ "setAllItemsDidUploadTrackers:"
+ "setAppliedTombstoneRanks:"
+ "setBlockedOperationsOnInitialSync:"
+ "setBubbleSyncTask:"
+ "setCurrentSyncDownBarriers:"
+ "setDirectoriesCreatedLastSyncUp:"
+ "setDownloadedBlockToPerformForItemID:"
+ "setEmailSettingEnabled:syncContext:reply:"
+ "setFaultsLiveBarriers:"
+ "setFetchParentOperations:"
+ "setFetchRecentsOperation:"
+ "setFormatVersion:"
+ "setHasFormatVersion:"
+ "setHasWorkDidUpdateObserver:"
+ "setInvokeFetchRecentsOperation:"
+ "setLastInsertedRank:"
+ "setLastSyncDownError:"
+ "setLastSyncUpError:"
+ "setLastSyncUpErrorWasOnChainedItem:"
+ "setLocateBlocksToPerformForRecordID:"
+ "setLocateRecordOperations:"
+ "setLocateRecordsOperationThrottle:"
+ "setNextIdleHandlers:"
+ "setNextSyncDownBarriers:"
+ "setOnDiskBlockToPerformForItemID:"
+ "setOsNameRequiredToSync:"
+ "setOutOfBandSyncOperations:"
+ "setParentZoneEtag:"
+ "setRFAEmailSettingEnabled:reply:"
+ "setRecursiveListOperations:"
+ "setRequestID:"
+ "setResetAfterAppUninstallTimer:"
+ "setResetTimer:"
+ "setRunningListOperations:"
+ "setServerStitchingOperationThrottle:"
+ "setShouldShowiCloudDriveAppInstallationNotification:"
+ "setSideCarEtag:"
+ "setSyncDeadlineSource:"
+ "setSyncDeadlineSourceResumer:"
+ "setSyncDownBlockToPerformForBookmarkData:"
+ "setSyncDownBlockToPerformForItemID:"
+ "setSyncDownCompletionHandlers:"
+ "setSyncDownDependencies:"
+ "setSyncDownGroup:"
+ "setSyncDownOperation:"
+ "setSyncDownThrottle:"
+ "setSyncThrottles:"
+ "setSyncUpBackoffRatio:"
+ "setSyncUpBatchSizeMultiplier:"
+ "setSyncUpBudget:"
+ "setSyncUpOperation:"
+ "setSyncUpRetryAfter:"
+ "setSyncUpThrottle:"
+ "shouldPCSChainItem:completionHandler:"
+ "shouldPCSChainItem:zoneName:completionHandler:"
+ "shouldShowiCloudDriveAppInstallationNotification"
+ "sideCarETag"
+ "sideCarEtag"
+ "structuralExtendedAttributesSignature"
+ "structureETag"
+ "syncContextIdleTimeBeforeMemoryReclaim"
+ "syncDeadlineSourceResumer"
+ "syncDownBlockToPerformForBookmarkData"
+ "syncDownBlockToPerformForItemID"
+ "syncDownCompletionHandlers"
+ "syncDownDependencies"
+ "syncDownOperation"
+ "syncEngine"
+ "syncEngineMarkForceIdleWithVersion:"
+ "syncUpBatchSizeMultiplier"
+ "syncUpOperation"
+ "syncUpRetryAfter"
+ "topLevelSharedItemID"
+ "trashItemIDWithFacade:"
+ "unpublish"
+ "unreachable: No client zone found for %@ [%@]"
+ "unreachable: No server zone found for %@ [%@]"
+ "unreachable: Zone %@:%@ not found"
+ "updateFromPlist:"
+ "updatePCSStateForItemIdentifier:newState:zoneName:ownerName:completionHandler:"
+ "updateWithPlist:isDeferredPlist:"
+ "uploadV2Enabled"
+ "uploadingError"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8@?<v@?q>16"
+ "v24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "v32@0:8@\"UNNotificationResponse\"16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"BRCSyncContext\"16^B24"
+ "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
+ "v36@?0@\"<NSFileProviderItem>\"8Q16B24@\"NSError\"28"
+ "v36@?0@\"BRQueryItem\"8Q16B24@\"NSError\"28"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@16^q24^q32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40"
+ "v48@0:8@16@24^q32^q40"
+ "v52@0:8@\"NSString\"16I24@\"NSString\"28@\"NSString\"36@?<v@?@\"NSError\">44"
+ "v52@0:8@16I24@28@36@?44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24Q32@40@?48"
+ "v72@0:8@16Q24@32Q40@48@56@?64"
+ "v80@0:8@16@24Q32@40Q48@56@64@?72"
+ "waitForSyncDownOfZone:ownerName:completionHandler:"
+ "waitForSyncDownWithCompletionHandler:"
+ "workDirectoryForSyncEngine"
+ "zoneOwnerName"
+ "{?=\"formatVersion\"b1}"
- " WITH RECURSIVE item_parents (item_id, item_sharing_options, item_parent_id) AS (          SELECT item_id, item_sharing_options, item_parent_id FROM client_items           WHERE item_id = %@ AND zone_rowid = %@       UNION ALL          SELECT li.item_id, li.item_sharing_options, li.item_parent_id FROM client_items AS li     INNER JOIN item_parents AS p WHERE li.zone_rowid = %@ AND p.item_parent_id = li.item_id          LIMIT %u )        SELECT item_id FROM item_parents WHERE (item_sharing_options & 4) != 0"
- " WITH RECURSIVE item_parents (item_id, item_sharing_options, item_parent_id) AS (          SELECT item_id, item_sharing_options, item_parent_id FROM server_items           WHERE item_id = %@ AND zone_rowid = %@       UNION ALL          SELECT li.item_id, li.item_sharing_options, li.item_parent_id FROM server_items AS li     INNER JOIN item_parents AS p WHERE li.zone_rowid = %@ AND p.item_parent_id = li.item_id          LIMIT %u )        SELECT item_id FROM item_parents WHERE (item_sharing_options & 4) != 0"
- " alias-container:%@"
- " operation cancelled."
- " ⏸️"
- "%@%@%@"
- "%lu"
- "+ Submitted BGSystemTasks: %@"
- "+ process-removal: %@"
- "+[BRCProgress progressToReplaceUploadProgress:]"
- "+[BRCProgress uploadProgressForDocument:totalUnitCount:completedUnitCount:]"
- "+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]"
- "+[BRCRecentsEnumerator dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:]_block_invoke"
- "-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke"
- "-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke"
- "-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2"
- "-[BRCClientZone close]_block_invoke"
- "-[BRCClientZone scheduleResetServerAndClientTruthsForReason:completionHandler:]"
- "-[BRCClientZone updateWithPlist:]"
- "-[BRCDaemon _setupCacheDelete]_block_invoke"
- "-[BRCDaemon _setupCacheDelete]_block_invoke_2"
- "-[BRCDaemon _setupCacheDelete]_block_invoke_3"
- "-[BRCDaemon start]_block_invoke_5"
- "-[BRCDiskSpaceReclaimer _purgeSpaceUnderQueue:withUrgency:]"
- "-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke"
- "-[BRCDiskSpaceReclaimer computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke_3"
- "-[BRCDiskSpaceReclaimer performOptimizeStorageWithTimeDelta:onDiskAccessTimeDelta:error:]"
- "-[BRCDiskSpaceReclaimer purgeSpace:withUrgency:]_block_invoke"
- "-[BRCFileUnlinker resume]"
- "-[BRCLocalItem extendedAttributes]_block_invoke"
- "-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]"
- "-[BRCMigrationQueryOperation __performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:]_block_invoke_2"
- "-[BRCMigrationQueryOperation _updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:]"
- "-[BRCNotification generateLogicalExtension:physicalExtension:]"
- "-[BRCPipeline _buildJobPlanForJob:error:]"
- "-[BRCPipeline _completedJob:forStage:recoveryStage:error:]"
- "-[BRCPipeline _generateProgressForJob:]_block_invoke"
- "-[BRCPipeline _sendJob:toStageHandlerWithStageID:]"
- "-[BRCPipeline _validateStageHandlers]"
- "-[BRCPipeline addJob:moreComing:]_block_invoke"
- "-[BRCPipelineJob(InternalPipeline) advanceJobToInitialStage]"
- "-[BRCPipelineJob(InternalPipeline) advanceJobToNextStage]"
- "-[BRCPipelineJob(InternalPipeline) advanceToRecoveryStage:]"
- "-[BRCPipelineJob(InternalPipeline) completeWithError:]"
- "-[BRCPipelineJob(InternalPipeline) setJobPlan:additionalToRequestingStageMap:]"
- "-[BRCPipelineJobQueue dequeueHighestQualityOfServiceJobsWithHandler:]"
- "-[BRCPipelineStageHandlerBase _cancelActiveBatchIfNecessary]"
- "-[BRCPipelineStageHandlerBase _completedJob:withRecoveryStage:error:]"
- "-[BRCPipelineStageHandlerBase schedule]"
- "-[BRCPipelineStageHandlerBase schedule]_block_invoke_2"
- "-[BRCPipelineStageHandlerBase(InternalPipeline) addJob:]_block_invoke"
- "-[BRCPipelineStageHandlerBase(InternalPipeline) cancelJob:]_block_invoke"
- "-[BRCServerItem appLibraryForRootItem]"
- "-[BRCSharingAcceptFlowOperation _checkIfShouldWaitUntilDownloadCompletion_step]"
- "-[BRCSharingAcceptFlowOperation _setSpotlightAttribute_step]"
- "-[BRCStageRegistry garbageCollectSpace:]"
- "-[BRCStageRegistry purgeGraveyardSpace:withUrgency:]"
- "-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]"
- "-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke"
- "-[BRCSyncContext _addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:]_block_invoke_2"
- "-[BRCSyncContext _setupBGSystemTaskCompletionFor:]"
- "-[BRCSyncContext _setupBGSystemTaskCompletionFor:]_block_invoke"
- "-[BRCSyncContext _updateSubmittedBGSystemTasksWithState:]"
- "-[BRCSyncContext _updateSubmittedBGSystemTasksWithState:submittedBGSystemTaskIdentifiers:]"
- "-[BRCSyncContext _updateWifiOnlyBGSystemTaskWithCancelledTaskIdentifiers:inexpensiveNetworkConnectivity:]_block_invoke"
- "-[BRCSyncContext addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:]"
- "-[BRCSyncContext initWithSession:contextIdentifier:isShared:]_block_invoke"
- "-[BRCSyncContext setupIfNeeded]"
- "-[BRCSyncUpOperationBuilder _checkIfShouldDedicateOpToPCSChainingItem:]"
- "-[BRCSystemResourcesManager _didReceiveMemoryWarning]"
- "-[BRCSystemResourcesManager _initLowMemory]"
- "-[BRCUploadSyncUpRequestsManager finishRequestForIdentifer:finishError:error:]"
- "-[BRCUploadSyncUpRequestsManager finishRequestForItemsInZoneRowID:finishError:]"
- "-[BRCUploadSyncUpRequestsManager invalidateRequestsOfClient:]"
- "-[BRCUploadSyncUpRequestsManager registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:]"
- "-[BRCUserDefaults _loadObjectForKey:inheritFromGlobal:suiteName:validateWithBlock:]"
- "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]"
- "-[BRCXPCRegularIPCsClient backupDatabaseWithURLWrapper:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]"
- "-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient purgeAmount:withUrgency:reply:]"
- "-[BRCXPCRegularIPCsClient purgeAmount:withUrgency:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient reclaimAmount:withUrgency:reply:]"
- "-[BRCXPCRegularIPCsClient reclaimAmount:withUrgency:reply:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke_2"
- "-[BRContainer(Daemon) currentStatus]"
- "-[BRContainer(Daemon) lastServerUpdate]"
- "-[NSError(BRCAdditions) brc_containerResetErrorForSharedZone:resetReason:]_block_invoke"
- "-[NSProgress(BRCAdditions) brc_publish]"
- "-[NSProgress(BRCAdditions) brc_unpublish]"
- "-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]_block_invoke"
- "-[_BRCOperation _addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:]_block_invoke_2"
- "-[_BRCOperation addSubOperation:asCompletionOf:]"
- ".do-not-delete"
- ".handler-queue"
- ".icloud-drive.do-not-delete"
- ".queue"
- ".scheduler-queue"
- ".ubd"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/account/BRCAccountSession.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/account/BRCAccountsManager.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/containers/BRCClientZone.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/containers/BRCContainerScheduler.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/containers/BRCServerZone.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/daemon/BRCDaemon.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/database/BRCClientDatabaseFacade.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/database/BRCClientState.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseManager.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/database/BRCDatabaseSchema.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/database/BRCServerPersistedState.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/foundation/BRCFairScheduler.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/foundation/BRCPQLConnection.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/items/BRCItemID.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/notifs/BRCAccountHandler.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/sync/transfers/BRCTransferStream.m"
- "35"
- "36"
- "37"
- "38"
- "<%@: %p type:%@ %@ progress:%@>"
- "<%@:%p %@ 🏃\u200d♂️:%@ ☑️:[%@] ✅:[%@]%@>"
- "<%@:%p [%@]>"
- "<%@:%p%@ [%@]>"
- "<%@[%@] %@ {client:%@ server:%@ sync:%@ %@ rid:%llu appuninstalled:%@}>"
- "<rdar://problem/37451020>"
- ">[%@]"
- "@\"BRCPipelineJobQueue\""
- "@\"NSMutableString\"16@?0Q8"
- "@\"NSProgress\"24@0:8@\"NSArray\"16"
- "@\"NSString\"16@?0Q8"
- "@24@0:8@\"BRCPipelineJob\"16"
- "@28@0:8I16@?20"
- "@28@0:8c16@20"
- "@36@0:8@16s24@?28"
- "@44@0:8@16B24@28@?36"
- "@44@0:8@16c24q28q36"
- "@72@0:8@16@24@32@40@48@56Q64"
- "@?<v@?@\"BRCPipelineJob\"Q@\"NSError\">16@0:8"
- "Application Support/Ubiquity"
- "Approve"
- "B16@?0@\"BRCPipelineJob\"8"
- "B24@0:8@\"BRCPipelineJob\"16"
- "B32@0:8@\"BRCPipelineJob\"16Q24"
- "B40@0:8d16d24^@32"
- "B60@0:8@16s24@28@36@?44^@52"
- "BRCBGSystemTaskContext"
- "BRCMigrateLegacyUbiquityRoot"
- "BRCPipeline"
- "BRCPipelineJob"
- "BRCPipelineJobQueue"
- "BRCPipelineStageHandlerBase"
- "BRCPipelineStageHandlerJobCostVendor"
- "BRCPipelineStageHandlerProtocol"
- "BRCRequestData"
- "BRCRootIsOwnedByUbd"
- "BRCTouchRootMergeWitness"
- "BRCUploadSyncUpRequestsManager"
- "BRCValidateDirAt"
- "BirdConfiguration"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_ID"
- "CACHE_DELETE_NONPURGEABLE_AMOUNT"
- "CACHE_DELETE_VOLUME"
- "CKErrorUserDeleteZone"
- "Caches/com.apple.bird"
- "Caches/com.apple.ubd"
- "Daemon"
- "Decline"
- "InternalPipeline"
- "Logs/CrashReporter/DiagnosticLogs/Ubiquity"
- "Q24@0:8@\"BRCPipelineJob\"16"
- "Q28@0:8B16^@20"
- "Request is already registered for %@"
- "Stage handlers should be a sorted array starting at stageID 0 without holes"
- "T@\"BRCDeadlineSource\",R,N,V_syncDeadlineSource"
- "T@\"BRCThrottleBase\",R,N,V_applyThrottle"
- "T@\"BRCThrottleBase\",R,N,V_downloadThrottle"
- "T@\"BRCThrottleBase\",R,N,V_perItemSyncUpThrottle"
- "T@\"BRCThrottleBase\",R,N,V_readerThrottle"
- "T@\"BRCThrottleBase\",R,N,V_uploadFileModifiedThrottle"
- "T@\"BRCThrottleBase\",R,N,V_uploadThrottle"
- "T@\"BRCTransferStream\",R,N,V_uploadStream"
- "T@\"NSArray\",?,R,N"
- "T@\"NSArray\",R,N,V_syncThrottles"
- "T@\"NSDictionary\",R,N,V_parentsOfCZMFaults"
- "T@\"NSDictionary\",R,N,V_submittedBGSystemTaskIdentifiers"
- "T@\"NSSet\",R,N,V_itemIDsBlockedFromSyncForCZMProcessing"
- "T@\"NSString\",R,N,V_aliasSourceAppLibraryID"
- "T@\"NSString\",R,N,V_osNameRequiredToSync"
- "T@\"brc_task_tracker\",R,N,V_taskTracker"
- "T@?,C,N"
- "T@?,R,N,V_finishBlock"
- "TI,R,N,V_qualityOfService"
- "TQ,?,R,N"
- "TQ,N,V_options"
- "Tq,R,N,V_lastInsertedRank"
- "Ts,R,N,V_requestType"
- "UPDATE client_items SET version_upload_error = NULL, item_notifs_rank = bump_notifs_rank_and_trigger_notifs(rowid) WHERE rowid IN (SELECT throttle_id FROM client_uploads WHERE throttle_state = %@)"
- "UPDATE client_uploads SET throttle_state = 1, upload_error = NULL WHERE throttle_state = %@"
- "WITH RECURSIVE item_parents (item_id, item_state, item_type, depth) AS (     SELECT item_id, item_state, item_type, 0       FROM server_items      WHERE zone_rowid = %@ AND item_id = %@  UNION ALL     SELECT p.item_parent_id, c.item_state, c.item_type, c.depth + 1       FROM server_items AS p INNER JOIN item_parents AS c USING (item_id)      WHERE p.zone_rowid = %@      LIMIT %u) SELECT item_state, depth, item_type FROM item_parents WHERE item_id_is_root(item_id) OR item_type = 4"
- "WITH RECURSIVE item_parents (item_parent_id, item_sharing_options) AS (     SELECT item_parent_id, item_sharing_options       FROM server_items      WHERE zone_rowid = %@ AND item_id = %@  UNION ALL     SELECT p.item_parent_id, p.item_sharing_options       FROM server_items AS p INNER JOIN item_parents AS c      WHERE p.zone_rowid = %@        AND c.item_parent_id = p.item_id      LIMIT %u) SELECT 1 FROM item_parents WHERE (item_sharing_options & 4) != 0"
- "Zone Error Reset: %@"
- "[8@\"NSString\"]"
- "[8Q]"
- "[CRIT] Assertion failed: !_jobPlan%@"
- "[CRIT] Assertion failed: !self->_resetTimer%@"
- "[CRIT] Assertion failed: _currentStageID != BRCPipelineStageNone%@"
- "[CRIT] Assertion failed: _jobPlan%@"
- "[CRIT] Assertion failed: _stageDirectoryFileID[dirIndex] != 0%@"
- "[CRIT] Assertion failed: _syncDownOperation == nil%@"
- "[CRIT] Assertion failed: _syncUpOperation == nil%@"
- "[CRIT] Assertion failed: groupToJobsMap.count > 0%@"
- "[CRIT] Assertion failed: index%@"
- "[CRIT] Assertion failed: isFixingState || (_requestID == 0 || requestID <= _requestID) isFixingState = %d, _requestID = %llu, requestID = %llu, zone = %@%@"
- "[CRIT] Assertion failed: job.activeStageID == [(BRCPipelineStageHandler *)self stageID]%@"
- "[CRIT] Assertion failed: logicalName%@"
- "[CRIT] Assertion failed: physicalName.br_isSideFaultName%@"
- "[CRIT] Assertion failed: progress.isCancellable%@"
- "[CRIT] Assertion failed: self.isFSRoot%@"
- "[CRIT] Assertion failed: taskIdentifier%@"
- "[CRIT] UNREACHABLE: -[BRContainer currentStatus] shouldn't be called by the daemon.%@"
- "[CRIT] UNREACHABLE: -[BRContainer lastServerUpdate] shouldn't be called by the daemon.%@"
- "[CRIT] UNREACHABLE: Can't advance job to next state when haven't started or already finished%@"
- "[CRIT] UNREACHABLE: Can't cancel job %@ which isn't a part of the current stage %@%@"
- "[CRIT] UNREACHABLE: Can't complete a job which has already completed %@%@"
- "[CRIT] UNREACHABLE: Can't schedule when we already have running jobs%@"
- "[CRIT] UNREACHABLE: Container needs server and client truths reset: %@%@"
- "[CRIT] UNREACHABLE: Failed removing root folder from the wrong account%@"
- "[CRIT] UNREACHABLE: Failed to remove mobile documents directory not belonging to us%@"
- "[CRIT] UNREACHABLE: Invalid additional index %lu%@"
- "[CRIT] UNREACHABLE: Invalid additional stage handler %lu%@"
- "[CRIT] UNREACHABLE: Invalid stage plan -- no stage handler for %lu%@"
- "[CRIT] UNREACHABLE: Job active stage doesn't match completed stage for %@ vs %@. Was the completion handler called more than once?%@"
- "[CRIT] UNREACHABLE: No additional stage handler found %lu%@"
- "[CRIT] UNREACHABLE: Recieved an invalid request type%@"
- "[CRIT] UNREACHABLE: Recovery stage handler is out of index%@"
- "[CRIT] UNREACHABLE: Unsuported record type %@%@"
- "[CRIT] UNREACHABLE: can't find the appLibrary of %@%@"
- "[CRIT] UNREACHABLE: handler is at an invalid index %@%@"
- "[CRIT] We own both the root and had an old one renamed away\nWe have purged the old one, and will now reset%@"
- "[DEBUG] %@ %@ finished record fetcher.%@%@"
- "[DEBUG] %s dir at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[DEBUG] Advancing job %@ to %@%@"
- "[DEBUG] Attempting to cancel %@%@"
- "[DEBUG] BGSystemTask with task identifier %@ is still being used%@"
- "[DEBUG] BGSystemTask with task identifier %@ started to run, operation(finished:%s, executing:%s, cancelled:%s), taskLaunched=%s%@"
- "[DEBUG] Calling finish block for %@ with %@%@"
- "[DEBUG] Cancelling current batch for %@ because all jobs are cancelled%@"
- "[DEBUG] Completed last job for batch -- resuming the source%@"
- "[DEBUG] Completing Job %@ with error %@%@"
- "[DEBUG] Computed plan for job %@%@"
- "[DEBUG] CoreSpotlight index has already been dropped%@"
- "[DEBUG] Couldn't update the task request %@ - error = %@%@"
- "[DEBUG] Done Force Ingestion of %@ to update the contentPolicy - %@%@"
- "[DEBUG] Error case in computePurgeableSpaceForAllUrgenciesWithReply for kBRCCacheDeletePushBGSystemTaskId%@"
- "[DEBUG] Finished fixing content policy after upgrade with %llu problems%@"
- "[DEBUG] Finishing all requests under zone %@%@"
- "[DEBUG] Invalidating state of client = %@%@"
- "[DEBUG] Marked BGSystemTask with task identifier %@ as completed - deregister result %d%@"
- "[DEBUG] Memory warning received%@"
- "[DEBUG] Moving ownership of system task %@ to CKOperation with identifier %@%@"
- "[DEBUG] Not suspending download of an item that needs CZM processing %@%@"
- "[DEBUG] Purgeable info: %@ (not returned)%@"
- "[DEBUG] Purged %@ when asked to purge %@ for urgency %d%@"
- "[DEBUG] Purged space is %@%@"
- "[DEBUG] Queueing faults live barrier for %@%@"
- "[DEBUG] Queueing job %@ with stage handler %@%@"
- "[DEBUG] Registered request %@ for identifier %@%@"
- "[DEBUG] Removing job which is cancelled and hasn't started executing %@%@"
- "[DEBUG] Starting job %@ with %@%@"
- "[DEBUG] Successfully submitted BGSystemTask %@ in %@, with %@ configuration%@"
- "[DEBUG] Sync: denylist %@ because it's already being processed for CZM%@"
- "[DEBUG] Updating bg system tasks to new state %d%@"
- "[DEBUG] Using parent %@ for %@ because it's in the CZM fault list%@"
- "[DEBUG] We are denylisted from %@ because %d < %d and %d%@"
- "[DEBUG] We are not denylisted from %@ because we are on an internal build and in carry%@"
- "[DEBUG] We are not denylisted from %@ because we are on an internal build%@"
- "[DEBUG] We are not denylisted from %@ chaining because we are in carry%@"
- "[DEBUG] We are not denylisted from %@%@"
- "[DEBUG] We still have non-cancelled jobs executing in %@%@"
- "[DEBUG] _checkIfShouldWaitUntilDownloadCompletion is not relevant in FPFS.%@"
- "[DEBUG] _setSpotlightAttribute is not relevant in FPFS%@"
- "[DEBUG] added %@ as a sync-down dependency of %@%@"
- "[DEBUG] device does not support CoreSpotlight indexing, no need to drop any index%@"
- "[DEBUG] dropped Spotlight index successfully%@"
- "[DEBUG] evicted %@ from stage%@"
- "[DEBUG] no need to evict, amount requested is %@%@"
- "[DEBUG] purgeable space is %@%@"
- "[DEBUG] removed %@ as a sync-down dependency of %@%@"
- "[DEBUG] returning purgeable info from cache\npurgeableSpaceByUrgency:%@\nnonPurgeableSpace:%@%@"
- "[DEBUG] root has a .ubd folder: deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[DEBUG] root has accountString %@%@"
- "[DEBUG] server default for %@: %@%@"
- "[DEBUG] success case kBRCCacheDeletePushBGSystemTaskId%@"
- "[DEBUG] user default for %@: %@%@"
- "[DEBUG] ┏%llx cache delete requested us to compute purgeable space: (urgency: %d) %@%@"
- "[DEBUG] ┏%llx cache delete requested us to periodically purge: %@%@"
- "[DEBUG] ┏%llx cache delete requested us to purge: (urgency: %d) %@%@"
- "[DEBUG] ┏%llx deleting root folder%@"
- "[DEBUG] ┏%llx deleting ubd's support files%@"
- "[DEBUG] ┏%llx migrating legacy ubiquity root%@"
- "[DEBUG] ┏%llx pushing purgeable update to cache delete%@"
- "[DEBUG] ┳%llx container-metadata receieved server change token %@, caught-up:%s client change token %@ error:%@%@"
- "[ERROR] %@: EINTR: client gather phase was invalidated%@"
- "[ERROR] Error in computePurgeableSpaceForAllUrgenciesWithReply: %@%@"
- "[ERROR] Failed to create root at %@ - %@%@"
- "[ERROR] Failed to get volume path%@"
- "[ERROR] Failed to submit BGSystemTask %@ due to %@%@"
- "[ERROR] Timed out waiting for eviction!%@"
- "[ERROR] Unable to create directory \"%@\": %@%@"
- "[ERROR] Unable to set mtime & hidden on \"%@\": %@%@"
- "[ERROR] can't fstat (%d, '%@') %{errno}d%@"
- "[ERROR] can't fstat (%d, '%@') after mkdir %{errno}d%@"
- "[ERROR] can't lstat '%@' %{errno}d%@"
- "[ERROR] can't open (%d, '%@') %{errno}d%@"
- "[ERROR] can't open (%d, '%@') after mkdir %{errno}d%@"
- "[ERROR] can't open root '%@' %{errno}d%@"
- "[ERROR] failed chmod at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x %{errno}d%@"
- "[ERROR] failed dropping Spotlight index: %@%@"
- "[ERROR] failed renaming root back from '%@' to '%@' %{errno}d%@"
- "[ERROR] failed to issue sandbox extension for %@: %@%@"
- "[ERROR] failed to synchronize user defaults for %@%@"
- "[ERROR] mkdirat(%d, '%@') %{errno}d%@"
- "[ERROR] not a directory at (%d, '%@') after mkdir deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[ERROR] not a directory at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[ERROR] unexpected permissions at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[ERROR] unexpected uid != %u at (%d, '%@')deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[INFO] %@: reply(%@, %lu, %@)%@"
- "[NOTICE] Device is in sync bubble%@"
- "[NOTICE] evicting for storage optimization%@"
- "[NOTICE] found our root at '%@' deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
- "[NOTICE] migrating root from accountString %@ to %@%@"
- "[NOTICE] moved '%@' back to '%@'%@"
- "[NOTICE] tagging root with accountString %@%@"
- "[NOTIF] issued sandbox extension for %@%@"
- "[NOTIF] ┏%llx generating sandbox extensions for %@%@"
- "[WARNING] Another task instance for %@ has been launched.. completing right away.%@"
- "[WARNING] Can't cancel a job that has already completed%@"
- "[WARNING] Can't find sself!%@"
- "[WARNING] Found recovery stage %@ after executing %@%@"
- "[WARNING] dropping CoreSpotlight index%@"
- "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
- "__performQuery:recordFetchedBlock:cursorUpdatedBlock:desiredKeys:asContinuationOf:completion:"
- "_activeQOSValues"
- "_activelyExecutingJobs"
- "_activelyExecutingProgress"
- "_addCKOperationToCKDatabaseQueue:allowsCellularAccess:ckDatabase:asCompletionOf:"
- "_addSubOperation:overrideContext:allowsCellularAccess:asCompletionOf:"
- "_additionalToRequestingStageMap"
- "_aliasSourceAppLibraryID"
- "_appLibrariesMonitored"
- "_armResumeTimer"
- "_asJobCostVendor"
- "_asyncAutovacuumIfNeeds:"
- "_buildBGSystemTaskIdentifierForCKOperation:"
- "_buildJobPlanForJob:error:"
- "_callFinishBlockOnDataRequest:finishError:"
- "_cancelActiveBatchIfNecessary"
- "_cancelBGSystemTasks"
- "_cancelBgSystemTaskIfNeededForCKOperation:"
- "_cancelledActivelyExecutingJobs"
- "_cancelledJobs"
- "_checkIfShouldWaitUntilDownloadCompletion_step"
- "_completedJob:forStage:recoveryStage:error:"
- "_completedJob:withRecoveryStage:error:"
- "_computeStageStringifier"
- "_contextIdentifierForMangledID:metadata:"
- "_currentStageID"
- "_decreaseSyncUpBatchSizeAfterError"
- "_didReceiveMemoryWarning"
- "_enqueuedJobs"
- "_fetchManagersDictionary"
- "_garbageCollectSpace:"
- "_garbageCollectUnusedLiveItems"
- "_generateProgressForJob:"
- "_getRequestTypeDescription"
- "_groupIdentifierForJob:"
- "_handlerQueue"
- "_increaseSyncUpBatchSizeAfterSuccess"
- "_initLowMemory"
- "_initWithPersonaIdentifier:"
- "_initWithSyncBubble:isFPFS:"
- "_initializeSourceAndQueues"
- "_invalidateLowMemory"
- "_invalidateRequestsTableWithNewSource:"
- "_isFPFS"
- "_issueReadWriteSandboxExtensionForURL"
- "_itemIDsBlockedFromSyncForCZMProcessing"
- "_jobPlan"
- "_latestSourceIdentifier"
- "_loadObjectForKey:inheritFromGlobal:suiteName:validateWithBlock:"
- "_lowMemoryObservers"
- "_notifyTokenForFramework"
- "_parentsOfCZMFaults"
- "_pauseScheduling"
- "_pauseStageHandlerScheduling"
- "_personaIdentifer"
- "_pipelineAutoResumeTimer"
- "_progressForDocument:group:totalUnitCount:completedUnitCount:"
- "_publish"
- "_purgeSpaceUnderQueue:withUrgency:"
- "_qosToGroupingToJobMapping"
- "_qualityOfService"
- "_readerThrottle"
- "_recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:"
- "_recreateSyncBudgetsAndThrottlesIfNeeded"
- "_referenceCounter"
- "_registerBackgroundXPCActivities"
- "_requestType"
- "_requestsByItemGlobalID"
- "_resumeAllDownloadStreams"
- "_resumeScheduling"
- "_resumeStageHandlerScheduling"
- "_schedulingEnabled"
- "_schedulingQueue"
- "_sendJob:toStageHandlerWithStageID:"
- "_setSpotlightAttribute_step"
- "_setStageJobCompletionHandlers"
- "_setupBGSystemTaskCompletionFor:"
- "_setupCacheDelete"
- "_stageDirectoryFileID"
- "_stageHandlers"
- "_stageStringifier"
- "_stageToRecoveryPlanMap"
- "_submittedBGSystemTaskIdentifiers"
- "_suspended"
- "_unlinkUbiquitySupportFiles"
- "_unpublish"
- "_updateSubmittedBGSystemTasksWithState:"
- "_updateSubmittedBGSystemTasksWithState:submittedBGSystemTaskIdentifiers:"
- "_updateToBeProgressForDocument:group:totalUnitCount:completedUnitCount:"
- "_updateWifiOnlyBGSystemTaskWithCancelledTaskIdentifiers:inexpensiveNetworkConnectivity:"
- "_updatedContinuationCursor:parentOperation:fetchedRecords:alreadyOnServerTruth:reply:"
- "_vacuumDB:amount:withUrgency:"
- "_validateStageHandlers"
- "_xpcClient"
- "_zoneIDToItemIDs"
- "accessTimeDeltaForUrgency:"
- "accessTimeDeltaInHighUrgency"
- "accessTimeDeltaInLowUrgency"
- "accessTimeDeltaInMedUrgency"
- "accessTimeDeltaInVeryHighUrgency"
- "active:"
- "activeStageID"
- "addJob:"
- "addJob:moreComing:"
- "addJob:withGroupIdentifier:"
- "addLowMemoryObserver:"
- "addOperation:allowsCellularAccess:asCompletionOf:"
- "addOperation:allowsCellularAccess:nonDiscretionary:asCompletionOf:"
- "addReference"
- "addSubOperation:asCompletionOf:"
- "advanceJobToInitialStage"
- "advanceJobToNextStage"
- "advanceToRecoveryStage:"
- "aliasSourceAppLibraryID"
- "appLibraryForRootItem"
- "backupDatabaseWithURLWrapper:reply:"
- "bird.use-bgst-to-schedule-discretionary-ops"
- "br_fixup_contentPolicy_block_invoke_2"
- "brc_containerResetErrorForSharedZone:resetReason:"
- "brc_errorCantCallFPInSyncBubble"
- "brc_errorCantRegisterBGSystemTask"
- "cacheDeletePushBGSystemTaskConfig"
- "cachedNonPurgeableSpace"
- "cachedPurgeableSpaceForUrgency:"
- "cancelJob:"
- "cancelRequestForIdentifier:error:"
- "cancelTaskRequestWithIdentifier:error:"
- "com.apple.bird.bgst.%@"
- "com.apple.bird.cache-delete.push"
- "com.apple.bird.eviction"
- "com.apple.clouddocs-items"
- "completeWithError:"
- "computePurgeableSpaceForAllUrgenciesWithReply:"
- "com~apple~Keynote/Documents/Recovered Data"
- "com~apple~Keynote/Documents/Recovered Data.folder"
- "com~apple~Numbers/Documents/Recovered Data"
- "com~apple~Numbers/Documents/Recovered Data.folder"
- "com~apple~Pages/Documents/Recovered Data"
- "com~apple~Pages/Documents/Recovered Data.folder"
- "contentPolicyForItemInfo:sessionContext:"
- "contentPolicyForRootContainerWithSessionContext:"
- "costForJob:"
- "crash-recovery"
- "createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:"
- "created"
- "currentStatus"
- "d20@0:8i16"
- "dbFixupContentPolicyRecoverAfterTimeInterval"
- "defaultManagerWithPersonaIdentifier:"
- "delete"
- "deleteAllSearchableItemsWithCompletionHandler:"
- "deleteItemWithIdentifier:baseVersion:options:completionHandler:"
- "dequeueHighestQualityOfServiceJobsWithHandler:"
- "dictionaryForKey:"
- "didDropCoreSpotlightIndex"
- "didReceiveMemoryWarning"
- "disableScheduling"
- "discretionary-ops-bgst-background-config"
- "discretionary-ops-bgst-foreground-config"
- "discretionaryOperationBGSystemTaskConfigForBackgroundContext"
- "discretionaryOperationBGSystemTaskConfigForForegroundContext"
- "discretionaryOperationBGSystemTaskConfigWithForegroundState:"
- "disk-space-reclaimer.max-access-time.high-urgency"
- "disk-space-reclaimer.max-access-time.low-urgency"
- "disk-space-reclaimer.max-access-time.med-urgency"
- "disk-space-reclaimer.max-access-time.very-high-urgency"
- "disk-space-reclaimer.max-graveyard-time.low-urgency"
- "disk-space-reclaimer.max-graveyard-time.med-urgency"
- "disk-space-reclaimer.max-ondisk-access-time.high-urgency"
- "disk-space-reclaimer.max-ondisk-access-time.low-urgency"
- "disk-space-reclaimer.max-ondisk-access-time.med-urgency"
- "disk-space-reclaimer.max-ondisk-access-time.very-high-urgency"
- "downloadStatus"
- "dropLegacyCoreSpotlightIndexIfNeededWithCompletionHandler:"
- "dropSpotlightIndexWithReply:"
- "enableScheduling"
- "enumerateIndexesWithOptions:usingBlock:"
- "exceptionWithName:reason:userInfo:"
- "finishRequestForIdentifer:finishError:error:"
- "finishRequestForItemsInZoneRowID:finishError:"
- "found"
- "fpfs modifications tracked requests"
- "fsreader.coordination.throttle"
- "garbageCollectSpace:"
- "generateLogicalExtension:physicalExtension:"
- "getProgressForIdentifier:"
- "graveyardAgeDeltaInLowUrgency"
- "graveyardAgeDeltaInMedUrgency"
- "groupByIdentifierForJob:"
- "handleJobsBatch:"
- "indexGreaterThanIndex:"
- "initAsGlobalWithServerConfiguration:"
- "initWithCacheDirPath:"
- "initWithCompletionHandler:"
- "initWithDocumentItem:client:sessionContext:downloadTrackersManager:"
- "initWithDocumentItem:client:sessionContext:downloadTrackersManager:etagIfLoser:stageFileName:options:"
- "initWithGroup:session:"
- "initWithName:protectionClass:"
- "initWithName:stageHandlers:"
- "initWithOptions:"
- "initWithProgress:requestType:finishBlock:"
- "initWithQualityOfService:completionHandler:"
- "initWithServerConfiguration:globalUserDefaults:clientZoneIdentifier:"
- "initWithShareMetadata:client:sessionContext:userNotifier:userActionsNavigator:"
- "invalid"
- "invalidateRequestsOfClient:"
- "ipc-com.apple.finder"
- "isCancellable"
- "isIndexingAvailable"
- "itemGlobalID = %@, requestData = %@"
- "itemIDsBlockedFromSyncForCZMProcessing"
- "jobPlan"
- "lastIndex"
- "lastServerUpdate"
- "maxJobsPerBatch"
- "modify"
- "modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:"
- "needsToHandleJob:"
- "needsToHandleJob:asRequestedByStage:"
- "numberOfSubmittedBGSystemTasks"
- "objectForKey:inheritFromGlobal:suiteName:validateWithBlock:"
- "onDiskAccessTimeDeltaInHighUrgency"
- "onDiskAccessTimeDeltaInLowUrgency"
- "onDiskAccessTimeDeltaInMedUrgency"
- "onDiskAccessTimeDeltaInVeryHighUrgency"
- "parentsOfCZMFaults"
- "perJobCompletionHandler"
- "performOptimizeStorageWithTimeDelta:onDiskAccessTimeDelta:error:"
- "postContainerStatusChangeNotificationWithID:key:value:"
- "progressToReplaceUploadProgress:"
- "purgeAmount:withUrgency:reply:"
- "purgeGraveyardSpace:withUrgency:"
- "purgeSpace:withUrgency:"
- "q28@0:8q16i24"
- "q36@0:8@16q24i32"
- "raise"
- "readerThrottle"
- "readerThrottleParams"
- "reclaimAmount:withUrgency:reply:"
- "recoverAndReportContentPolicyWithCompletion:"
- "registerRequestForIdentifier:requestType:requestSource:progress:finishBlock:error:"
- "releaseReference"
- "removeJob:withGroupIdentifier:"
- "removeLowMemoryObserver:"
- "requestType"
- "requestedAdditionalStages"
- "requiresInexpensiveNetworkConnectivity"
- "resumeIPCAcceptation"
- "s16@0:8"
- "scheduleResetServerAndClientTruthsForReason:"
- "scheduleResetServerAndClientTruthsForReason:completionHandler:"
- "scheduled:"
- "setGroupConcurrencyLimit:"
- "setGroupName:"
- "setJobPlan:additionalToRequestingStageMap:"
- "setOptions:"
- "setPerJobCompletionHandler:"
- "setRequiresInexpensiveNetworkConnectivity:"
- "setSession:group:"
- "setStageStringifier:"
- "setSystemTask:"
- "setupWithInternalPipelineJobCompletionHandler:"
- "shouldForceApplyContentForItem:"
- "simpleUrgencyForCacheDeleteUrgency:"
- "softCostLimit"
- "spotlight-indexer.enabled"
- "spotlightIndexingEnabled"
- "start-scan"
- "still-wants-data-unlinked"
- "submittedBGSystemTaskIdentifiers"
- "suspendIPCAcceptation"
- "systemTask"
- "taskRequestForIdentifier:"
- "there is no request for %@"
- "timed out waiting for eviction"
- "tracked requests of client (%lu) : (%lu):"
- "unreachable: Invalid additional index %lu"
- "unreachable: Invalid additional stage handler %lu"
- "unreachable: Invalid stage plan -- no stage handler for %lu"
- "unreachable: No additional stage handler found %lu"
- "unreachable: Recovery stage handler is out of index"
- "updateTaskRequest:error:"
- "uploadProgressForDocument:totalUnitCount:completedUnitCount:"
- "urgencyForCacheDeleteUrgency:"
- "useBGSTForSchedulingDiscretionaryOperations"
- "v24@0:8@?<v@?@\"BRCPipelineJob\"Q@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSNumber\"@\"NSError\">16"
- "v24@?0@\"NSDictionary\"8@\"NSNumber\"16"
- "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@?0@\"BRCItemGlobalID\"8@\"BRCRequestData\"16^B24"
- "v32@?0@\"BRCPipelineJob\"8Q16@\"NSError\"24"
- "v32@?0@\"BRQueryItem\"8Q16@\"NSError\"24"
- "v32@?0@\"NSDictionary\"8@\"NSNumber\"16@\"NSError\"24"
- "v32@?0@\"NSString\"8@\"BRCBGSystemTaskContext\"16^B24"
- "v32@?0@8@\"NSMutableArray\"16^B24"
- "v36@0:8q16i24@?28"
- "v36@0:8q16i24@?<v@?q>28"
- "v44@0:8@16c24q28q36"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24Q32@40"
- "v52@0:8@16@24@32B40@?44"
- "v64@0:8@16@?24@?32@40@48@?56"
- "v64@0:8@16Q24@32Q40@48@?56"
- "v72@0:8@16@24Q32@40Q48@56@?64"
- "writeToURL:atomically:"
- "{%@}"

```
