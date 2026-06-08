## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x1a42a4
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x130fc
-  __TEXT.__const: 0x300
-  __TEXT.__gcc_except_tab: 0x46f4
-  __TEXT.__oslogstring: 0x147ec
-  __TEXT.__cstring: 0x15728
-  __TEXT.__unwind_info: 0x5f90
-  __TEXT.__objc_classname: 0x1ea7
-  __TEXT.__objc_methname: 0x2aadf
-  __TEXT.__objc_methtype: 0x4787
-  __TEXT.__objc_stubs: 0x19e40
-  __DATA_CONST.__got: 0xa48
-  __DATA_CONST.__const: 0x6340
-  __DATA_CONST.__objc_classlist: 0x888
+910.14.107.0.0
+  __TEXT.__text: 0x1c714c
+  __TEXT.__objc_methlist: 0x15afc
+  __TEXT.__const: 0x328
+  __TEXT.__gcc_except_tab: 0x4a40
+  __TEXT.__oslogstring: 0x16bd2
+  __TEXT.__cstring: 0x17e47
+  __TEXT.__unwind_info: 0x6b88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6ee8
+  __DATA_CONST.__objc_classlist: 0x9d8
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8578
+  __DATA_CONST.__objc_selrefs: 0x9258
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x820
-  __DATA_CONST.__objc_arraydata: 0x1320
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0x26e0
-  __AUTH_CONST.__cfstring: 0x15700
-  __AUTH_CONST.__objc_const: 0x1e390
-  __AUTH_CONST.__objc_intobj: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x938
+  __DATA_CONST.__objc_arraydata: 0x1438
+  __DATA_CONST.__got: 0xb28
+  __AUTH_CONST.__const: 0x2c80
+  __AUTH_CONST.__cfstring: 0x17a20
+  __AUTH_CONST.__objc_const: 0x23240
+  __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x17e0
-  __DATA.__data: 0x1068
-  __DATA.__bss: 0xa88
-  __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x52d0
-  __DATA_DIRTY.__bss: 0x3a0
+  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__objc_floatobj: 0x50
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x1bbc
+  __DATA.__data: 0x14f0
+  __DATA.__bss: 0xcd0
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0x5960
+  __DATA_DIRTY.__bss: 0x320
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
-  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A289B6AD-B46F-3CF2-B0BF-D4A562B75FA0
-  Functions: 8520
-  Symbols:   26294
-  CStrings:  14879
+  UUID: 40719E94-FB57-3851-99BC-EC6F084CB5A6
+  Functions: 9698
+  Symbols:   29817
+  CStrings:  8424
 
Symbols:
+ +[CPLAssetChange(DefaultsSupport) serverSupportsProxyConflictResolution]
+ +[CPLCallObserver observeAsyncCallOn:selector:timeout:block:]
+ +[CPLCallObserver observeAsyncCallWithFunction:timeout:block:]
+ +[CPLCallObserver observeSyncCallOn:selector:timeout:block:]
+ +[CPLCallObserver observeSyncCallWithFunction:timeout:block:]
+ +[CPLCollectionShareScopeChange descriptionForExpiringState:]
+ +[CPLCollectionShareScopeChange descriptionForMigrationState:]
+ +[CPLCollectionShareScopeChange descriptionForViewingMode:]
+ +[CPLCollectionShareScopeChange mappingForExpiringState]
+ +[CPLCollectionShareScopeChange mappingForMigrationState]
+ +[CPLCollectionShareScopeChange mappingForViewingMode]
+ +[CPLEngineBackupSyncTask taskDescription]
+ +[CPLEngineDefaultStoreWipeHandler resetNotificationForLibraryIdentifier:]
+ +[CPLEngineDefaultStoreWipeHandler setShouldPreventWipeOnUpgrade:]
+ +[CPLEngineDefaultStoreWipeHandler shouldPreventWipeOnUpgrade]
+ +[CPLEngineDefaultStoreWipeHandler shouldWarnUserBeforeWipeOnUpgrade]
+ +[CPLEngineDerivativesCache initialize]
+ +[CPLEngineDownloadSyncTask taskDescription]
+ +[CPLEngineForceProcessingStagedScopesTask taskDescription]
+ +[CPLEngineForceSyncWithPushFromClientTask taskDescription]
+ +[CPLEnginePushRepository setShouldDisableUploadRate:]
+ +[CPLEnginePushRepository shouldDisableUploadRate]
+ +[CPLEngineResourceDownloadTask taskDescription]
+ +[CPLEngineResourceUploadTask taskDescription]
+ +[CPLEngineStore wipeStoreAtNextOpeningWithCloudLibraryStorageURL:reason:]
+ +[CPLErrors _errorWithErrorSpecifiers:]
+ +[CPLErrors errorWithErrorSpecifier:]
+ +[CPLErrors isPermanentError:]
+ +[CPLFingerprintContext newContext]
+ +[CPLFingerprintContext setSharedEPPContext:]
+ +[CPLFingerprintContext sharedEPPContext]
+ +[CPLForceSyncTask taskDescription]
+ +[CPLInMemoryResourceDownloadTask taskDescription]
+ +[CPLLibraryManager descriptionForFeatureDataclass:]
+ +[CPLLibraryManager descriptionForFeatureDataclasses:]
+ +[CPLLibraryManager enumerateFeatureDataclassesWithBlock:]
+ +[CPLLibraryManager mappingForFeatureDataclasses]
+ +[CPLLibraryParameters allLibraryOptionsDescriptions]
+ +[CPLLibraryParameters descriptionForLibraryOptions:]
+ +[CPLLibraryParameters mappingForLibraryOptions]
+ +[CPLLibraryParameters optionsFromDescription:]
+ +[CPLLibraryParameters reverseMappingForLibraryOptions]
+ +[CPLLibraryParameters supportsSecureCoding]
+ +[CPLPostChange supportsCollectionShare]
+ +[CPLPostChange supportsDeletion]
+ +[CPLPostChange supportsDirectDeletion]
+ +[CPLResource _resourceTypesThatCountAgainstiCloudQuota]
+ +[CPLResource isResourceTypeCountingForQuota:]
+ +[CPLResourceTransferTask taskDescription]
+ +[CPLScopeChange scopeTypeForScopeChangeClass:scopeIdentifier:]
+ +[CPLScopedIdentifier mappingForScopeIdentifierPrefixToFeatureDataclass]
+ +[CPLShareParticipant _descriptionForPermission:]
+ +[CPLShareParticipant _descriptionForRole:]
+ +[CPLTransportContainerConfiguration allOptionDescriptions]
+ +[CPLTransportContainerConfiguration configurationForTestManateeContainer]
+ +[CPLTransportContainerConfiguration configurationWithContainerIdentifier:bundleIdentifier:options:]
+ +[CPLTransportContainerConfiguration defaultTransportContainerConfigurationForE2E]
+ +[CPLTransportContainerConfiguration defaultTransportContainerConfigurationWithBoundaryKey:]
+ +[CPLTransportContainerConfiguration defaultTransportContainerConfiguration]
+ +[CPLTransportContainerConfiguration descriptionForOptions:]
+ +[CPLTransportContainerConfiguration mappingForOptions]
+ +[CPLTransportContainerConfiguration optionsFromDescription:]
+ +[CPLTransportContainerConfiguration photosBundleIdentifier]
+ +[CPLTransportContainerConfiguration photosContainerIdentifier]
+ +[CPLTransportContainerConfiguration reverseMappingForOptions]
+ +[CPLTransportContainerConfiguration supportsSecureCoding]
+ +[CPLTransportContainerConfiguration wellKnownConfigurations]
+ +[CPLUIObservedEvent supportsSecureCoding]
+ +[CPLUIObservedSource observationType]
+ +[CPLUIObserver observationType]
+ +[CPLUIObserverRegistration supportsSecureCoding]
+ +[CPLUIRecordObservedEvent supportsSecureCoding]
+ +[CPLUIRecordObservedSource observationType]
+ +[CPLUIRecordObserver observationType]
+ +[CPLUIRecordObserverRegistration supportsSecureCoding]
+ +[CPLUIRecordStatus descriptionForType:]
+ +[CPLUIScopeObservedEvent supportsSecureCoding]
+ +[CPLUIScopeObservedSource observationType]
+ +[CPLUIScopeObserver observationType]
+ +[CPLUIScopeObserverRegistration supportsSecureCoding]
+ +[CPLUIScopeStatus supportsSecureCoding]
+ +[CPLUISyncActivityObservedEvent supportsSecureCoding]
+ +[CPLUISyncActivityObservedSource observationType]
+ +[CPLUISyncActivityObserver descriptionForSyncActivityType:]
+ +[CPLUISyncActivityObserver observationType]
+ +[CPLUITestObservedEvent supportsSecureCoding]
+ +[CPLUITestObservedSource observationType]
+ +[CPLUITestObserver observationType]
+ -[CPLActiveDownloadQueue setShouldFetchExportedID:]
+ -[CPLActiveDownloadQueue setShouldFetchReference:]
+ -[CPLActiveDownloadQueue shouldFetchExportedID]
+ -[CPLActiveDownloadQueue shouldFetchReference]
+ -[CPLAssetChange assetBatchIdentifier]
+ -[CPLAssetChange proxyBestResourceType]
+ -[CPLAssetChange proxyExpectedMasterIdentifier]
+ -[CPLAssetChange proxyExpectedVideoDuration]
+ -[CPLAssetChange proxyExpirationDate]
+ -[CPLAssetChange rating]
+ -[CPLAssetChange setAssetBatchIdentifier:]
+ -[CPLAssetChange setProxyBestResourceType:]
+ -[CPLAssetChange setProxyExpectedMasterIdentifier:]
+ -[CPLAssetChange setProxyExpectedVideoDuration:]
+ -[CPLAssetChange setProxyExpirationDate:]
+ -[CPLAssetChange setRating:]
+ -[CPLBatterySaverWatcher .cxx_destruct]
+ -[CPLBatterySaverWatcher _batterySaverModeTriggered]
+ -[CPLBatterySaverWatcher _updateBatterySaverMode]
+ -[CPLBatterySaverWatcher delegate]
+ -[CPLBatterySaverWatcher inBatterySaverMode]
+ -[CPLBatterySaverWatcher initWithDispatchQueue:delegate:]
+ -[CPLBatterySaverWatcher startWatching]
+ -[CPLBatterySaverWatcher stopWatching]
+ -[CPLBeforeUploadCheckItems _items]
+ -[CPLBeforeUploadCheckItems didDropFullRecordItemWithScopedIdentifier:]
+ -[CPLBeforeUploadCheckItems itemWillBeDropped:]
+ -[CPLBeforeUploadCheckItems setUiUploadProgressHub:]
+ -[CPLBeforeUploadCheckItems uiUploadProgressHub]
+ -[CPLCallObserver initWithObject:selector:functionName:timeout:]
+ -[CPLCallObserver onTimeOutBlock]
+ -[CPLCallObserver setOnTimeOutBlock:]
+ -[CPLChangeBatch pullUUID]
+ -[CPLChangeBatch setPullUUID:]
+ -[CPLCollectionShareScopeChange .cxx_destruct]
+ -[CPLCollectionShareScopeChange _additionalDescription]
+ -[CPLCollectionShareScopeChange expiringState]
+ -[CPLCollectionShareScopeChange expiryDate]
+ -[CPLCollectionShareScopeChange keyAssetIdentifier]
+ -[CPLCollectionShareScopeChange migrationOriginatingSharedAlbumIdentifier]
+ -[CPLCollectionShareScopeChange migrationStartTime]
+ -[CPLCollectionShareScopeChange migrationState]
+ -[CPLCollectionShareScopeChange setExpiringState:]
+ -[CPLCollectionShareScopeChange setExpiryDate:]
+ -[CPLCollectionShareScopeChange setKeyAssetIdentifier:]
+ -[CPLCollectionShareScopeChange setMigrationOriginatingSharedAlbumIdentifier:]
+ -[CPLCollectionShareScopeChange setMigrationStartTime:]
+ -[CPLCollectionShareScopeChange setMigrationState:]
+ -[CPLCollectionShareScopeChange setThumbnailImageData:]
+ -[CPLCollectionShareScopeChange setUserLastViewedNotificationDate:]
+ -[CPLCollectionShareScopeChange setViewingMode:]
+ -[CPLCollectionShareScopeChange thumbnailImageData]
+ -[CPLCollectionShareScopeChange updateScopeFromScopeChange:direction:didHaveChanges:]
+ -[CPLCollectionShareScopeChange userLastViewedNotificationDate]
+ -[CPLCollectionShareScopeChange viewingMode]
+ -[CPLCommentChange isPostComment]
+ -[CPLCommentChange postIdentifier]
+ -[CPLCommentChange postScopedIdentifier]
+ -[CPLCommentChange setIsPostComment:]
+ -[CPLCommentChange setPostIdentifier:]
+ -[CPLCommentChange setPostScopedIdentifier:]
+ -[CPLCommentChange(CPLPlaceholderRecord) relatedRecordClass]
+ -[CPLCommentChange(CPLPushSessionTracker) validateRecordForTracker:]
+ -[CPLContainerRelationChange reportingScopedIdentifier]
+ -[CPLDefaultBrokenScope .cxx_destruct]
+ -[CPLDefaultBrokenScope attemptRecovery]
+ -[CPLDefaultBrokenScope engineLibrary]
+ -[CPLDefaultBrokenScope engineScope]
+ -[CPLDefaultBrokenScope initWithEngineScope:engineLibrary:]
+ -[CPLDefaultBrokenScope recoverDescription]
+ -[CPLDirectUploadTask .cxx_destruct]
+ -[CPLDirectUploadTask _didFinishSubtask]
+ -[CPLDirectUploadTask _didFinishTaskWithError:]
+ -[CPLDirectUploadTask _generateDerivativesIfNecessaryWithFetchCache:]
+ -[CPLDirectUploadTask _launchSubtask:]
+ -[CPLDirectUploadTask _launchTransportTask:phaseDescription:]
+ -[CPLDirectUploadTask _observationCenter]
+ -[CPLDirectUploadTask _phaseDescription]
+ -[CPLDirectUploadTask _removeFileURLsFromChange:]
+ -[CPLDirectUploadTask _reportProgressToUIStep:]
+ -[CPLDirectUploadTask _uploadRecordsIfNecessaryWithFetchCache:]
+ -[CPLDirectUploadTask _willNeedToAccessScopeWithIdentifier:error:]
+ -[CPLDirectUploadTask allowsBackgroundDispatch]
+ -[CPLDirectUploadTask allowsForcedTaskQueuing]
+ -[CPLDirectUploadTask availableResourceTypesToUploadForChange:]
+ -[CPLDirectUploadTask batch]
+ -[CPLDirectUploadTask bypassLimits]
+ -[CPLDirectUploadTask cancelFromSyncManager:]
+ -[CPLDirectUploadTask cancelTask]
+ -[CPLDirectUploadTask creationDate]
+ -[CPLDirectUploadTask description]
+ -[CPLDirectUploadTask discardedError]
+ -[CPLDirectUploadTask engine]
+ -[CPLDirectUploadTask forcedTaskPriority]
+ -[CPLDirectUploadTask generateDerivativesSubtask:derivativesGenerationForChange:didProgress:]
+ -[CPLDirectUploadTask generateDerivativesSubtask:didFinishGeneratingDerivativesForChange:]
+ -[CPLDirectUploadTask generateDerivativesSubtask:didFinishWithError:]
+ -[CPLDirectUploadTask generateDerivativesSubtask:didProgressGeneratingDerivativesFromResourceSize:]
+ -[CPLDirectUploadTask generateDerivativesSubtask:willStartGeneratingDerivativesForChange:]
+ -[CPLDirectUploadTask generateDerivativesSubtask:willStartWithChangeCount:]
+ -[CPLDirectUploadTask initWithEngineLibrary:batch:owner:]
+ -[CPLDirectUploadTask isCancelled]
+ -[CPLDirectUploadTask isCloudRecordWithScopedIdentifierShared:]
+ -[CPLDirectUploadTask isResourceDynamic:]
+ -[CPLDirectUploadTask knownCloudRecordWithScopedIdentifier:]
+ -[CPLDirectUploadTask launchFromSyncManager:]
+ -[CPLDirectUploadTask launchTask]
+ -[CPLDirectUploadTask notifyProgress:forScopeWithIdentifier:]
+ -[CPLDirectUploadTask notifySyncActivityIsBlocked:]
+ -[CPLDirectUploadTask owner]
+ -[CPLDirectUploadTask scopeIdentifiers]
+ -[CPLDirectUploadTask setBypassLimits:]
+ -[CPLDirectUploadTask setTaskDidFinishWithErrorBlock:]
+ -[CPLDirectUploadTask setTransportUserIdentifier:]
+ -[CPLDirectUploadTask simpleDescription]
+ -[CPLDirectUploadTask startSyncActivityForScopeIdentifier:]
+ -[CPLDirectUploadTask startSyncActivity]
+ -[CPLDirectUploadTask stopSyncActivityForScopeIdentifier:]
+ -[CPLDirectUploadTask stopSyncActivity]
+ -[CPLDirectUploadTask syncActivityType]
+ -[CPLDirectUploadTask taskDidFinishWithErrorBlock]
+ -[CPLDirectUploadTask taskIdentifier]
+ -[CPLDirectUploadTask transportUserIdentifier]
+ -[CPLDirectUploadTask uploadedBatch]
+ -[CPLDirectUploadTask willNeedToAccessRecordWithScopedIdentifier:error:]
+ -[CPLDirectUploadTask willUploadCloudResource:localResource:error:]
+ -[CPLEngineChangePipe checkNextBatchToPopWithPullUUID:]
+ -[CPLEngineChangePipe popNextBatchWithUUID:error:]
+ -[CPLEngineCloudCache acknowledgeRecordWithScopedIdentifier:error:]
+ -[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:uiUploadProgressHub:withError:]
+ -[CPLEngineComponentEnumerator initWithComponents:queue:handler:]
+ -[CPLEngineDefaultStoreWipeHandler .cxx_destruct]
+ -[CPLEngineDefaultStoreWipeHandler initWithLibraryIdentifier:reason:]
+ -[CPLEngineDefaultStoreWipeHandler reason]
+ -[CPLEngineDefaultStoreWipeHandler shouldPreventWipeOnUpgradeCreateRadar:]
+ -[CPLEngineDerivativesCache identifier]
+ -[CPLEngineDerivativesCache initWithCacheURL:identifier:parentCache:queue:]
+ -[CPLEngineDerivativesCache parentCache]
+ -[CPLEngineDerivativesCache subCacheWithIdentifier:]
+ -[CPLEngineForceSyncTask _observationCenter]
+ -[CPLEngineForceSyncTask allowsBackgroundDispatch]
+ -[CPLEngineForceSyncTask allowsForcedTaskQueuing]
+ -[CPLEngineForceSyncTask cancelFromSyncManager:]
+ -[CPLEngineForceSyncTask discardedError]
+ -[CPLEngineForceSyncTask forcedTaskPriority]
+ -[CPLEngineForceSyncTask launchFromSyncManager:]
+ -[CPLEngineForceSyncTask notifyProgress:forScopeWithIdentifier:]
+ -[CPLEngineForceSyncTask notifySyncActivityIsBlocked:]
+ -[CPLEngineForceSyncTask simpleDescription]
+ -[CPLEngineForceSyncTask startSyncActivityForScopeIdentifier:]
+ -[CPLEngineForceSyncTask startSyncActivity]
+ -[CPLEngineForceSyncTask stopSyncActivityForScopeIdentifier:]
+ -[CPLEngineForceSyncTask stopSyncActivity]
+ -[CPLEngineForceSyncTask syncActivityType]
+ -[CPLEngineForceSyncWithPushFromClientTask .cxx_destruct]
+ -[CPLEngineForceSyncWithPushFromClientTask cancelTask]
+ -[CPLEngineForceSyncWithPushFromClientTask didFinishSubTask:]
+ -[CPLEngineForceSyncWithPushFromClientTask didStartSubTask:]
+ -[CPLEngineForceSyncWithPushFromClientTask engineLibrary]
+ -[CPLEngineForceSyncWithPushFromClientTask initWithScopeIdentifiers:engineLibrary:onPushFromClientCompleted:]
+ -[CPLEngineForceSyncWithPushFromClientTask launchTask]
+ -[CPLEngineForceSyncWithPushFromClientTask onPushFromClientCompleted]
+ -[CPLEngineForceSyncWithPushFromClientTask setEngineLibrary:]
+ -[CPLEngineForceSyncWithPushFromClientTask setOnPushFromClientCompleted:]
+ -[CPLEngineLibrary _engineDidUpdateParameters]
+ -[CPLEngineLibrary accountPartitionType]
+ -[CPLEngineLibrary allowedDisabledFeatureDataclasses]
+ -[CPLEngineLibrary allowedFeatureDataclasses]
+ -[CPLEngineLibrary catastrophicExit]
+ -[CPLEngineLibrary initWithParameters:]
+ -[CPLEngineLibrary lastSuccessfulSyncDate]
+ -[CPLEngineLibrary observationCenter]
+ -[CPLEngineLibrary parameters]
+ -[CPLEngineLibrary resetMainScopeStatus]
+ -[CPLEngineLibrary schemaFilter]
+ -[CPLEngineLibrary setAccountPartitionType:]
+ -[CPLEngineLibrary updateContainerConfiguration:]
+ -[CPLEngineLibrary updateLastSuccessfulSyncDate:]
+ -[CPLEngineLibrary updateLibraryOptions:]
+ -[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]
+ -[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]
+ -[CPLEngineLibrary(CPLManagement) getStatusWithCompletionHandler:]
+ -[CPLEngineMultiscopeSyncTask isPermanentError:]
+ -[CPLEngineMultiscopeSyncTask shouldProcessScope:optionalExcludedReason:inTransaction:]
+ -[CPLEngineMultiscopeSyncTask shouldSkipScopesWithPermanentError]
+ -[CPLEngineMultiscopeSyncTask taskDidFinishWithError:]
+ -[CPLEnginePushRepository performMaintenanceWithError:]
+ -[CPLEnginePushRepository removeChange:error:]
+ -[CPLEnginePushRepository setShouldOrderRecordsBySize:]
+ -[CPLEnginePushRepository shouldOrderRecordsBySize]
+ -[CPLEngineScheduler _updateTurboModeOnQueue]
+ -[CPLEngineScheduler createBackgroundSchedulerForSession:]
+ -[CPLEngineScheduler firstStateNeedingClientInSync]
+ -[CPLEngineScheduler getBackgroundSchedulingStatusDictionaryWithCompletionHandler:]
+ -[CPLEngineScheduler getBackgroundSchedulingStatusWithCompletionHandler:]
+ -[CPLEngineScheduler getSystemBudgetsForBackgroundActivityWithCompletionHandler:]
+ -[CPLEngineScheduler setCanUseTurboMode:]
+ -[CPLEngineScheduler setShouldOverride:forSystemBudgets:]
+ -[CPLEngineScheduler shouldUseTurboMode]
+ -[CPLEngineScheduler usesBackgroundScheduling]
+ -[CPLEngineScopeStorage _allRelatedScopesForScope:]
+ -[CPLEngineScopeStorage _classesForInitialQueriesForScopeType:]
+ -[CPLEngineScopeStorage _fillAllRelatedScopes:withScope:]
+ -[CPLEngineScopeStorage activateScopesWithScopeTypes:error:]
+ -[CPLEngineScopeStorage clearAllPermanentErrorWithError:]
+ -[CPLEngineScopeStorage deactivateScopesWithScopeTypes:error:]
+ -[CPLEngineScopeStorage defaultFlagsForScopeChange:]
+ -[CPLEngineScopeStorage fillUIScopeStatus:forScopeWithIdentifier:]
+ -[CPLEngineScopeStorage permanentErrorForScope:]
+ -[CPLEngineScopeStorage scopeForUIObservingForScope:]
+ -[CPLEngineScopeStorage shouldAutoActivateScopeWithIdentifier:scopeType:]
+ -[CPLEngineScopeStorage shouldAutoActivateScopeWithType:]
+ -[CPLEngineScopeStorage shouldTryToBypassBackgroundSchedulingDuringPullFromTransportForScope:]
+ -[CPLEngineScopeStorage storeLastSyncDateFromSession:error:]
+ -[CPLEngineScopeStorage storePermanentError:forScope:error:]
+ -[CPLEngineScopeStorage supportsActivationOfScopeWithType:]
+ -[CPLEngineScopedTask scopeIdentifierForUIObservation]
+ -[CPLEngineScopedTask setScopeIdentifierForUIObservation:]
+ -[CPLEngineStore _disableFeatureDataclass:error:]
+ -[CPLEngineStore _enableFeatureDataclass:error:]
+ -[CPLEngineStore blockWriteTransactionsWithReason:completionHandler:]
+ -[CPLEngineStore blockedDateWithReason:]
+ -[CPLEngineStore containerConfiguration]
+ -[CPLEngineStore featureDataclasses]
+ -[CPLEngineStore noteUIStatusForAllRecordsHaveChanged]
+ -[CPLEngineStore noteUIStatusForAllRecordsWithScopeIdentifierHaveChanged:]
+ -[CPLEngineStore noteUIStatusForAllScopesHaveChanged]
+ -[CPLEngineStore noteUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:]
+ -[CPLEngineStore noteUIStatusForScopesWithIdentifiersHaveChanged:]
+ -[CPLEngineStore storeLastSuccessfulSyncDateFromSyncSession:]
+ -[CPLEngineStore updateContainerConfigurationIfNecessary:error:]
+ -[CPLEngineStore updateFeatureDataclasses:error:]
+ -[CPLEngineSyncTask bypassBackgroundSchedulingIfPossible]
+ -[CPLEngineSyncTask redactedDescription]
+ -[CPLEngineSyncTask setSyncActivitySource:]
+ -[CPLEngineSyncTask shouldReportProgressToUI]
+ -[CPLEngineSyncTask syncActivitySource]
+ -[CPLEngineSystemMonitor _updateCanUseTurboModeOnScheduler]
+ -[CPLEngineSystemMonitor batterySaverWatcherDidChangeState:]
+ -[CPLEngineSystemMonitor hasGoodQualityNetwork]
+ -[CPLEngineSystemMonitor isNetworkExpensive]
+ -[CPLEngineTransport concreteTransportReferenceFromTransportReference:error:]
+ -[CPLEngineTransport createGroupForAcceptingScopeWithType:]
+ -[CPLEngineTransport createGroupForDecliningScopeWithType:]
+ -[CPLEngineTransport createGroupForDirectTransportScopeDelete]
+ -[CPLEngineTransport createGroupForDirectUpload]
+ -[CPLEngineTransport createGroupForFetchingScopeWithType:]
+ -[CPLEngineTransport createGroupForPublishingScopeWithType:]
+ -[CPLEngineTransport createGroupForRemovingParticipantsFromShare]
+ -[CPLEngineTransport createGroupForThumbnailPrefetchWithIntent:]
+ -[CPLEngineTransport createGroupForUpdatingScopeWithType:]
+ -[CPLEngineTransport declineTaskForSharedScope:completionHandler:]
+ -[CPLEngineTransport discardContainerWithCompletionHandler:]
+ -[CPLEngineTransport removeParticipantsInShareTaskFromSharedScope:transportScope:share:userIdentifiersToRemove:participantIDsToRemove:completionHandler:]
+ -[CPLEngineTransport updateContainerConfiguration:]
+ -[CPLEngineUIObservationCenter .cxx_destruct]
+ -[CPLEngineUIObservationCenter _sources]
+ -[CPLEngineUIObservationCenter _withObservedSourceOfType:block:]
+ -[CPLEngineUIObservationCenter closeAndDeactivate:completionHandler:]
+ -[CPLEngineUIObservationCenter componentName]
+ -[CPLEngineUIObservationCenter engineLibrary]
+ -[CPLEngineUIObservationCenter getStatusDictionaryWithCompletionHandler:]
+ -[CPLEngineUIObservationCenter getStatusWithCompletionHandler:]
+ -[CPLEngineUIObservationCenter initWithEngineLibrary:]
+ -[CPLEngineUIObservationCenter managerNameForObserver:]
+ -[CPLEngineUIObservationCenter openWithCompletionHandler:]
+ -[CPLEngineUIObservationCenter refreshObservedEventForObserver:completionHandler:]
+ -[CPLEngineUIObservationCenter registerObserver:withRegistration:completionHandler:]
+ -[CPLEngineUIObservationCenter unregisterObserver:completionHandler:]
+ -[CPLEngineUIObservationCenter updateRegistration:forObserver:completionHandler:]
+ -[CPLEngineUIObservationCenter withObservedSourceOfType:block:]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyRecordsUploadDidFinish]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyRecordsWithLocalScopedIdentifiersHaveStartedUploading:step:]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForAllRecordsHaveChanged]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForAllRecordsWithScopeIdentifiersHaveChanged:]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUploadProgressForRecordsWithLocalScopedIdentifiers:step:]
+ -[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) recordObservedSource:computeStatusesWithAccumulator:completionHandler:]
+ -[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusForAllScopesHaveChanged]
+ -[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusForScopesWithIdentifiersHaveChanged:]
+ -[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusScopeWithIdentifiers:isSynchronizing:]
+ -[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) scopeObservedSource:getStatusesForScopesWithIdentifiers:synchronizingScopeWithIdentifiers:completionHandler:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) notifyProgress:forScopeWithIdentifier:fromSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) notifySyncActivityIsBlocked:forSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startClientSession]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startSyncActivityForScopeWithIdentifier:fromSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startSyncActivityFromSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopClientSession]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopSyncActivityForScopeWithIdentifier:fromSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopSyncActivityForSource:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) syncActivitySource:isBlocked:]
+ -[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) syncActivitySource:isSynchronizing:scopeWithIdentifier:]
+ -[CPLEngineUIObservationCenter(CPLUITestObservedSource) testKey:value:completionHandler:]
+ -[CPLExtractedBatch isEmpty]
+ -[CPLExtractedBatch scopedIdentifiers]
+ -[CPLFingerprintContext forceMMCSv2AsDefault]
+ -[CPLForceSyncTask context]
+ -[CPLForceSyncTask setContext:]
+ -[CPLGenerateDerivativesSubtask .cxx_destruct]
+ -[CPLGenerateDerivativesSubtask _discardGenerateDerivativesProgress]
+ -[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]
+ -[CPLGenerateDerivativesSubtask _taskDidFinishWithError:]
+ -[CPLGenerateDerivativesSubtask allowsCancellingActiveDerivativesGeneration]
+ -[CPLGenerateDerivativesSubtask cancel]
+ -[CPLGenerateDerivativesSubtask changes]
+ -[CPLGenerateDerivativesSubtask delegate]
+ -[CPLGenerateDerivativesSubtask derivativesCache]
+ -[CPLGenerateDerivativesSubtask derivativesFilter]
+ -[CPLGenerateDerivativesSubtask fingerprintContext]
+ -[CPLGenerateDerivativesSubtask initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:]
+ -[CPLGenerateDerivativesSubtask launch]
+ -[CPLGenerateDerivativesSubtask observeValueForKeyPath:ofObject:change:context:]
+ -[CPLGenerateDerivativesSubtask predictor]
+ -[CPLGenerateDerivativesSubtask session]
+ -[CPLGenerateDerivativesSubtask setAllowsCancellingActiveDerivativesGeneration:]
+ -[CPLGenerateDerivativesSubtask setDelegate:]
+ -[CPLGenerateDerivativesSubtask setPredictor:]
+ -[CPLGenerateDerivativesSubtask setSession:]
+ -[CPLGenerateDerivativesSubtask setShouldUseCache:]
+ -[CPLGenerateDerivativesSubtask shouldUseCache]
+ -[CPLLibraryInfo totalAssetCount]
+ -[CPLLibraryManager _updateParameters:]
+ -[CPLLibraryManager acceptShareFromFetchedScope:completionHandler:]
+ -[CPLLibraryManager clearAllPermanentErrorsWithCompletionHandler:]
+ -[CPLLibraryManager clearPermanentErrorForScopeWithIdentifier:completionHandler:]
+ -[CPLLibraryManager declineSharedScope:completionHandler:]
+ -[CPLLibraryManager disableFeatureDataclasses:completionHandler:]
+ -[CPLLibraryManager enableFeatureDataclasses:completionHandler:]
+ -[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]
+ -[CPLLibraryManager initForUIWithLibraryIdentifier:]
+ -[CPLLibraryManager initWithParameters:]
+ -[CPLLibraryManager initWithParameters:libraryIdentifier:libraryManagerType:]
+ -[CPLLibraryManager libraryManagerType]
+ -[CPLLibraryManager managerNameForObserver:]
+ -[CPLLibraryManager parameters]
+ -[CPLLibraryManager ping]
+ -[CPLLibraryManager refreshObservedEventForObserver:completionHandler:]
+ -[CPLLibraryManager registerObserver:withRegistration:completionHandler:]
+ -[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]
+ -[CPLLibraryManager setFeatureDataclasses:completionHandler:]
+ -[CPLLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]
+ -[CPLLibraryManager shouldDispatchDelegateCalls]
+ -[CPLLibraryManager unregisterObserver:completionHandler:]
+ -[CPLLibraryManager updateRegistration:forObserver:completionHandler:]
+ -[CPLLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]
+ -[CPLLibraryManager uploadChangeBatch:completionHandler:]
+ -[CPLLibraryManager(CPLManagement) getStatusForComponents:timeout:completionHandler:]
+ -[CPLLibraryParameters .cxx_destruct]
+ -[CPLLibraryParameters _upgradeFromVersion:]
+ -[CPLLibraryParameters _url:matchesURL:]
+ -[CPLLibraryParameters asPlist]
+ -[CPLLibraryParameters clientLibraryBaseURL]
+ -[CPLLibraryParameters cloudLibraryResourceStorageURL]
+ -[CPLLibraryParameters cloudLibraryStateStorageURL]
+ -[CPLLibraryParameters copyChangingLibraryOptions:]
+ -[CPLLibraryParameters copyChangingTransportContainerConfiguration:]
+ -[CPLLibraryParameters description]
+ -[CPLLibraryParameters encodeWithCoder:]
+ -[CPLLibraryParameters hash]
+ -[CPLLibraryParameters initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:transportContainerConfiguration:]
+ -[CPLLibraryParameters initWithCoder:]
+ -[CPLLibraryParameters initWithOldPlist:]
+ -[CPLLibraryParameters initWithPlist:]
+ -[CPLLibraryParameters isEqual:]
+ -[CPLLibraryParameters libraryIdentifier]
+ -[CPLLibraryParameters mainScopeIdentifier]
+ -[CPLLibraryParameters matchesParameters:]
+ -[CPLLibraryParameters options]
+ -[CPLLibraryParameters redactedDescription]
+ -[CPLLibraryParameters transportContainerConfiguration]
+ -[CPLMasterChange reportingScopedIdentifier]
+ -[CPLMingleChangesTask shouldProcessScope:optionalExcludedReason:inTransaction:]
+ -[CPLNetworkState isExpensive]
+ -[CPLNetworkState isGoodQuality]
+ -[CPLNetworkState linkQuality]
+ -[CPLPartialDerivativesGenerationResult .cxx_destruct]
+ -[CPLPartialDerivativesGenerationResult description]
+ -[CPLPartialDerivativesGenerationResult initWithResources:partialResultsURL:]
+ -[CPLPartialDerivativesGenerationResult safeFilenames]
+ -[CPLPhotosSchemaFilter copyAllowingAllRecordClassesForContainerIdentifier:]
+ -[CPLPhotosSchemaFilter shortDescription]
+ -[CPLPhotosSchemaFilter transportFilterPlistForTransportIdentifier:]
+ -[CPLPlistSchemaFilter .cxx_destruct]
+ -[CPLPlistSchemaFilter _loadIfNecessary]
+ -[CPLPlistSchemaFilter allowsAll]
+ -[CPLPlistSchemaFilter allowsPropertyWithName:forClass:]
+ -[CPLPlistSchemaFilter allowsResourceType:]
+ -[CPLPlistSchemaFilter copyAllowingAllRecordClassesForContainerIdentifier:]
+ -[CPLPlistSchemaFilter filterDefinition]
+ -[CPLPlistSchemaFilter initForContainerIdentifier:]
+ -[CPLPlistSchemaFilter initForContainerIdentifier:filterDefinition:]
+ -[CPLPlistSchemaFilter shortDescription]
+ -[CPLPlistSchemaFilter supportsRecordsOfClass:]
+ -[CPLPlistSchemaFilter transportFilterPlistForTransportIdentifier:]
+ -[CPLPostChange .cxx_destruct]
+ -[CPLPostChange caption]
+ -[CPLPostChange creationDate]
+ -[CPLPostChange setCaption:]
+ -[CPLPostChange setCreationDate:]
+ -[CPLProxyLibraryManager _dropConnectionCompletelyLocked]
+ -[CPLProxyLibraryManager _dropConnectionCompletely]
+ -[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]
+ -[CPLProxyLibraryManager clearAllPermanentErrorsWithCompletionHandler:]
+ -[CPLProxyLibraryManager declineSharedScope:completionHandler:]
+ -[CPLProxyLibraryManager disableFeatureDataclasses:completionHandler:]
+ -[CPLProxyLibraryManager enableFeatureDataclasses:completionHandler:]
+ -[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]
+ -[CPLProxyLibraryManager getStatusForComponents:timeout:completionHandler:]
+ -[CPLProxyLibraryManager managerNameForObserver:]
+ -[CPLProxyLibraryManager observedEventDidChangeForObserverWithIdentifier:]
+ -[CPLProxyLibraryManager ping]
+ -[CPLProxyLibraryManager refreshObservedEventForObserver:completionHandler:]
+ -[CPLProxyLibraryManager registerObserver:withRegistration:completionHandler:]
+ -[CPLProxyLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]
+ -[CPLProxyLibraryManager setFeatureDataclasses:completionHandler:]
+ -[CPLProxyLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]
+ -[CPLProxyLibraryManager unregisterObserver:completionHandler:]
+ -[CPLProxyLibraryManager updateRegistration:forObserver:completionHandler:]
+ -[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]
+ -[CPLPushSessionTracker checkScopeIdentifier:invalidReason:]
+ -[CPLPushToTransportScopeTask shouldReportProgressToUI]
+ -[CPLPushToTransportTask isPermanentError:]
+ -[CPLPushToTransportTask shouldReportProgressToUI]
+ -[CPLPushToTransportTask shouldSkipScopesWithPermanentError]
+ -[CPLReactChange .cxx_destruct]
+ -[CPLReactChange reactText]
+ -[CPLReactChange setReactText:]
+ -[CPLRecordChange isFromInitialDownload]
+ -[CPLRecordChange isProxyRecord]
+ -[CPLRecordChange proxyState]
+ -[CPLRecordChange reportingScopedIdentifier]
+ -[CPLRecordChange setFromInitialDownload:]
+ -[CPLRecordChange setIsProxyRecord:]
+ -[CPLRecordChange setProxyState:]
+ -[CPLRecordChange totalResourceSizeAccountingForQuota]
+ -[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:willAddChangeBlock:]
+ -[CPLResource isResourceCountingForQuota]
+ -[CPLResourceIdentity setTransportReference:]
+ -[CPLResourceIdentity transportReference]
+ -[CPLResourceTransferTaskOptions shouldFetchExportedID]
+ -[CPLResourceTransferTaskOptions shouldFetchReference]
+ -[CPLSchemaFilter .cxx_destruct]
+ -[CPLSchemaFilter allowsAll]
+ -[CPLSchemaFilter allowsPropertyWithName:forClass:]
+ -[CPLSchemaFilter allowsResourceType:]
+ -[CPLSchemaFilter containerIdentifier]
+ -[CPLSchemaFilter copyAllowingAllRecordClassesForContainerIdentifier:]
+ -[CPLSchemaFilter initForContainerIdentifier:]
+ -[CPLSchemaFilter shortDescription]
+ -[CPLSchemaFilter supportsRecordsOfClass:]
+ -[CPLSchemaFilter transportFilterForTransportIdentifier:constructor:]
+ -[CPLSchemaFilter transportFilterPlistForTransportIdentifier:]
+ -[CPLScopeChange isOverLimit]
+ -[CPLScopeChange isOverQuota]
+ -[CPLScopeChange permanentError]
+ -[CPLScopeChange setOverLimit:]
+ -[CPLScopeChange setOverQuota:]
+ -[CPLScopeChange setPermanentError:]
+ -[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]
+ -[CPLScopeUpdateTask shouldProcessScope:optionalExcludedReason:inTransaction:]
+ -[CPLScopedIdentifier qualifiesForEnabledFeatureDataclasses:]
+ -[CPLShare adminIsCurrentUser]
+ -[CPLShare allowsAccessRequests]
+ -[CPLShare allowsAnonymousPublicAccess]
+ -[CPLShare setAllowsAccessRequests:]
+ -[CPLShare setAllowsAnonymousPublicAccess:]
+ -[CPLShareParticipant isPlaceholder]
+ -[CPLShareParticipant nTimeURL]
+ -[CPLShareParticipant setIsPlaceholder:]
+ -[CPLShareParticipant setNTimeURL:]
+ -[CPLShareParticipant setSubscriptionDate:]
+ -[CPLShareParticipant subscriptionDate]
+ -[CPLStatus accountPartitionType]
+ -[CPLStatus resetMainScopeStatus]
+ -[CPLStatus setAccountPartitionType:]
+ -[CPLSyncSession _observationCenter]
+ -[CPLSyncSession backgroundScheduler]
+ -[CPLSyncSession createBackgroundSchedulerIfNecessary]
+ -[CPLSyncSession hasBeenJustInCaseSession]
+ -[CPLSyncSession needsToAcquireBackgroundScheduler]
+ -[CPLSyncSession setBackgroundScheduler:]
+ -[CPLSyncSession shouldBypassBackgroundScheduling]
+ -[CPLSyncSession startBypassingBackgroundSchedulingIfPossible]
+ -[CPLSyncSession stopBypassingBackgroundSchedulingIfPossible]
+ -[CPLSyncSession usesTurboMode]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) notifyProgress:forScopeWithIdentifier:]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) notifySyncActivityIsBlocked:]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) startSyncActivityForScopeIdentifier:]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) startSyncActivity]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) stopSyncActivityForScopeIdentifier:]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) stopSyncActivity]
+ -[CPLSyncSession(CPLUISyncActivityObservedSource) syncActivityType]
+ -[CPLSyncSessionBlockedState backgroundScheduler]
+ -[CPLSyncSessionBlockedState initWithBackgroundScheduler:blocked:syncHasBeenRequested:runtimeCharacteristics:]
+ -[CPLTransportContainerConfiguration .cxx_destruct]
+ -[CPLTransportContainerConfiguration allowsFeedback]
+ -[CPLTransportContainerConfiguration allowsGatekeeper]
+ -[CPLTransportContainerConfiguration allowsServerConfiguration]
+ -[CPLTransportContainerConfiguration allowsUploadRequests]
+ -[CPLTransportContainerConfiguration asPlist]
+ -[CPLTransportContainerConfiguration bundleIdentifier]
+ -[CPLTransportContainerConfiguration containerIdentifier]
+ -[CPLTransportContainerConfiguration copyWithFingerprintContext:]
+ -[CPLTransportContainerConfiguration description]
+ -[CPLTransportContainerConfiguration encodeWithCoder:]
+ -[CPLTransportContainerConfiguration fingerprintContext]
+ -[CPLTransportContainerConfiguration forcesEPP]
+ -[CPLTransportContainerConfiguration hasServerSideConflictResolution]
+ -[CPLTransportContainerConfiguration hash]
+ -[CPLTransportContainerConfiguration initWithCoder:]
+ -[CPLTransportContainerConfiguration initWithContainerIdentifier:bundleIdentifier:options:]
+ -[CPLTransportContainerConfiguration initWithContainerIdentifier:bundleIdentifier:options:fingerprintContext:schemaFilter:]
+ -[CPLTransportContainerConfiguration initWithPlist:]
+ -[CPLTransportContainerConfiguration isEqual:]
+ -[CPLTransportContainerConfiguration isUsualPhotosContainer]
+ -[CPLTransportContainerConfiguration manatee]
+ -[CPLTransportContainerConfiguration matchesConfiguration:]
+ -[CPLTransportContainerConfiguration options]
+ -[CPLTransportContainerConfiguration redactedDescription]
+ -[CPLTransportContainerConfiguration requiresSubscription]
+ -[CPLTransportContainerConfiguration sandboxed]
+ -[CPLTransportContainerConfiguration schemaFilter]
+ -[CPLTransportContainerConfiguration simpleDescription]
+ -[CPLTransportContainerConfiguration supportedFeatureVersion]
+ -[CPLTransportContainerConfiguration zoneish]
+ -[CPLTransportScopeMapping scopes]
+ -[CPLTransportUpdateScopeTask initWithEngineLibrary:session:clientCacheIdentifier:scope:transportScope:]
+ -[CPLTransportUpdateTask shouldSkipScopesWithPermanentError]
+ -[CPLUIObservedEvent description]
+ -[CPLUIObservedEvent encodeWithCoder:]
+ -[CPLUIObservedEvent eventDescription]
+ -[CPLUIObservedEvent initWithCoder:]
+ -[CPLUIObservedEvent plistDescription]
+ -[CPLUIObservedEvent redactedDescription]
+ -[CPLUIObservedSource .cxx_destruct]
+ -[CPLUIObservedSource _discardObserverNotifications]
+ -[CPLUIObservedSource _scheduleObserverNotifications]
+ -[CPLUIObservedSource addObserver:registration:]
+ -[CPLUIObservedSource delegate]
+ -[CPLUIObservedSource enumerateObserversWithBlock:]
+ -[CPLUIObservedSource fetchObservedEventForObserver:completionHandler:]
+ -[CPLUIObservedSource fireObserverNotifications]
+ -[CPLUIObservedSource hasObservers]
+ -[CPLUIObservedSource initWithDelegate:queue:]
+ -[CPLUIObservedSource isValidRegistration:]
+ -[CPLUIObservedSource notifyAllObservers]
+ -[CPLUIObservedSource notifyObserver:]
+ -[CPLUIObservedSource observerStatusDictionaries]
+ -[CPLUIObservedSource observerStatuses]
+ -[CPLUIObservedSource queue]
+ -[CPLUIObservedSource registeredObserverForObserver:]
+ -[CPLUIObservedSource removeObserver:]
+ -[CPLUIObservedSource sourceStatusDictionary]
+ -[CPLUIObservedSource sourceStatus]
+ -[CPLUIObservedSource statusDictionaryForObserver:]
+ -[CPLUIObservedSource statusForObserver:]
+ -[CPLUIObservedSource updateRegistration:forObserver:]
+ -[CPLUIObserver .cxx_destruct]
+ -[CPLUIObserver _dispatchObservedEventToDelegate:registration:]
+ -[CPLUIObserver _forceRegistrationUpdateIfNecessary]
+ -[CPLUIObserver _unscheduleRegistrationUpdate]
+ -[CPLUIObserver _updateRegistration]
+ -[CPLUIObserver _withDelegateDo:]
+ -[CPLUIObserver currentRegistration]
+ -[CPLUIObserver delegate]
+ -[CPLUIObserver description]
+ -[CPLUIObserver didDisconnectFromObservedSource]
+ -[CPLUIObserver didRefreshObservedEvent:]
+ -[CPLUIObserver forceRefresh]
+ -[CPLUIObserver identifier]
+ -[CPLUIObserver initWithIdentifier:manager:queue:]
+ -[CPLUIObserver initWithIdentifier:manager:queue:initialRegistration:]
+ -[CPLUIObserver initWithLibraryManager:queue:]
+ -[CPLUIObserver initWithManager:]
+ -[CPLUIObserver manager]
+ -[CPLUIObserver newEmptyRegistration]
+ -[CPLUIObserver observedEventDidChange]
+ -[CPLUIObserver observedEventWasFetchedExternally:registration:]
+ -[CPLUIObserver observedSourceDidDisconnect]
+ -[CPLUIObserver queue]
+ -[CPLUIObserver redactedDescription]
+ -[CPLUIObserver registrationDidChange]
+ -[CPLUIObserver setCurrentRegistration:]
+ -[CPLUIObserver startObservingWithDelegate:]
+ -[CPLUIObserver startObservingWithDelegate:completionHandler:]
+ -[CPLUIObserver stopObservingWithCompletionHandler:]
+ -[CPLUIObserver stopObserving]
+ -[CPLUIObserver type]
+ -[CPLUIObserver underlyingManager]
+ -[CPLUIObserverAndRegistration .cxx_destruct]
+ -[CPLUIObserverAndRegistration identifier]
+ -[CPLUIObserverAndRegistration initWithObserver:]
+ -[CPLUIObserverAndRegistration observer]
+ -[CPLUIObserverAndRegistration registration]
+ -[CPLUIObserverAndRegistration setRegistration:]
+ -[CPLUIObserverAndRegistration setState:]
+ -[CPLUIObserverManager .cxx_destruct]
+ -[CPLUIObserverManager _autoOpen]
+ -[CPLUIObserverManager dealloc]
+ -[CPLUIObserverManager delegate]
+ -[CPLUIObserverManager description]
+ -[CPLUIObserverManager forceRefresh]
+ -[CPLUIObserverManager forceSyncScopesWithIdentifiers:]
+ -[CPLUIObserverManager initWithLibraryIdentifier:queue:]
+ -[CPLUIObserverManager init]
+ -[CPLUIObserverManager libraryIdentifier]
+ -[CPLUIObserverManager libraryManager:didFinishForceSyncTask:withErrors:]
+ -[CPLUIObserverManager libraryManager]
+ -[CPLUIObserverManager managerNameForObserver:]
+ -[CPLUIObserverManager queue]
+ -[CPLUIObserverManager redactedDescription]
+ -[CPLUIObserverManager refreshObservedEventForObserver:completionHandler:]
+ -[CPLUIObserverManager registerObserver:withRegistration:completionHandler:]
+ -[CPLUIObserverManager setDelegate:]
+ -[CPLUIObserverManager setTurboModeExpirationDate:]
+ -[CPLUIObserverManager tearDown]
+ -[CPLUIObserverManager turboModeExpirationDate]
+ -[CPLUIObserverManager unregisterObserver:completionHandler:]
+ -[CPLUIObserverManager updateRegistration:forObserver:completionHandler:]
+ -[CPLUIObserverRegistration .cxx_destruct]
+ -[CPLUIObserverRegistration description]
+ -[CPLUIObserverRegistration encodeWithCoder:]
+ -[CPLUIObserverRegistration initWithCoder:]
+ -[CPLUIObserverRegistration initWithType:]
+ -[CPLUIObserverRegistration plistArchiveWithCPLArchiver:]
+ -[CPLUIObserverRegistration plistDescription]
+ -[CPLUIObserverRegistration redactedDescription]
+ -[CPLUIObserverRegistration simpleDescription]
+ -[CPLUIObserverRegistration type]
+ -[CPLUIRecordObservedEvent .cxx_destruct]
+ -[CPLUIRecordObservedEvent blocked]
+ -[CPLUIRecordObservedEvent encodeWithCoder:]
+ -[CPLUIRecordObservedEvent eventDescription]
+ -[CPLUIRecordObservedEvent initWithBlocked:updatedNonUploadingStatuses:updatedUploadingProgresses:]
+ -[CPLUIRecordObservedEvent initWithCoder:]
+ -[CPLUIRecordObservedEvent updatedNonUploadingStatuses]
+ -[CPLUIRecordObservedEvent updatedUploadingProgresses]
+ -[CPLUIRecordObservedEventAccumulator .cxx_destruct]
+ -[CPLUIRecordObservedEventAccumulator blocked]
+ -[CPLUIRecordObservedEventAccumulator initWithUpdatedScopedIdentifiers:blocked:]
+ -[CPLUIRecordObservedEventAccumulator scopedIdentifiersNeedingStatusesWithScopeIndexFinder:]
+ -[CPLUIRecordObservedEventAccumulator synthesizedEvent]
+ -[CPLUIRecordObservedEventAccumulator updateStatusType:forScopedIdentifier:]
+ -[CPLUIRecordObservedEventAccumulator updateWithUploadProgresses:]
+ -[CPLUIRecordObservedEventAccumulator updatedScopedIdentifiers]
+ -[CPLUIRecordObservedSource .cxx_destruct]
+ -[CPLUIRecordObservedSource addObserver:registration:]
+ -[CPLUIRecordObservedSource fetchObservedEventForObserver:completionHandler:]
+ -[CPLUIRecordObservedSource isValidRegistration:]
+ -[CPLUIRecordObservedSource notifyRecordsUploadDidFinish]
+ -[CPLUIRecordObservedSource notifyRecordsWithLocalScopedIdentifiersHaveStartedUploading:step:]
+ -[CPLUIRecordObservedSource notifySyncActivityIsBlocked:]
+ -[CPLUIRecordObservedSource notifyUIStatusForAllRecordsHaveChanged]
+ -[CPLUIRecordObservedSource notifyUIStatusForAllRecordsWithScopeIdentifiersHaveChanged:]
+ -[CPLUIRecordObservedSource notifyUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:]
+ -[CPLUIRecordObservedSource notifyUploadProgressForRecordsWithLocalScopedIdentifiers:step:]
+ -[CPLUIRecordObservedSource sourceStatusDictionary]
+ -[CPLUIRecordObservedSource sourceStatus]
+ -[CPLUIRecordObservedSource statusDictionaryForObserver:]
+ -[CPLUIRecordObservedSource statusForObserver:]
+ -[CPLUIRecordObservedSource updateRegistration:forObserver:]
+ -[CPLUIRecordObserver .cxx_destruct]
+ -[CPLUIRecordObserver addObservedRecordsWithScopedIdentifiers:]
+ -[CPLUIRecordObserver addObservedRecordsWithScopedIdentifiers:removeObservedRecordsWithScopedIdentifiers:]
+ -[CPLUIRecordObserver didDisconnectFromObservedSource]
+ -[CPLUIRecordObserver didRefreshObservedEvent:]
+ -[CPLUIRecordObserver newEmptyRegistration]
+ -[CPLUIRecordObserver observedRecordScopedIdentifiers]
+ -[CPLUIRecordObserver removeObservedRecordsWithScopedIdentifiers:]
+ -[CPLUIRecordObserver setObservedRecordScopedIdentifiers:]
+ -[CPLUIRecordObserverRegistration .cxx_destruct]
+ -[CPLUIRecordObserverRegistration coveredScopedIdentifiersFromScopeIdentifiers:]
+ -[CPLUIRecordObserverRegistration coveredScopedIdentifiersFromScopedIdentifiers:]
+ -[CPLUIRecordObserverRegistration coveredScopedIdentifiersFromScopedIdentifiersEnumeration:]
+ -[CPLUIRecordObserverRegistration coveredScopedIdentifiers]
+ -[CPLUIRecordObserverRegistration encodeWithCoder:]
+ -[CPLUIRecordObserverRegistration forAllRecords]
+ -[CPLUIRecordObserverRegistration getAddedScopedIdentifiers:deletedScopedIdentifiers:withNewRegistration:]
+ -[CPLUIRecordObserverRegistration initForAllRecords]
+ -[CPLUIRecordObserverRegistration initWithCoder:]
+ -[CPLUIRecordObserverRegistration initWithCoveredScopedIdentifiers:]
+ -[CPLUIRecordObserverRegistration init]
+ -[CPLUIRecordObserverRegistration isObservedScopedIdentifier:]
+ -[CPLUIRecordObserverRegistration plistDescription]
+ -[CPLUIRecordObserverRegistration registrationByAddingScopedIdentifiers:removingScopedIdentifiers:]
+ -[CPLUIRecordObserverRegistration simpleDescription]
+ -[CPLUIRecordStatus initWithProgress:]
+ -[CPLUIRecordStatus initWithType:]
+ -[CPLUIRecordStatus progress]
+ -[CPLUIRecordStatus type]
+ -[CPLUIScopeObservedEvent .cxx_destruct]
+ -[CPLUIScopeObservedEvent encodeWithCoder:]
+ -[CPLUIScopeObservedEvent eventDescription]
+ -[CPLUIScopeObservedEvent initWithCoder:]
+ -[CPLUIScopeObservedEvent initWithStatuses:]
+ -[CPLUIScopeObservedEvent statuses]
+ -[CPLUIScopeObservedSource .cxx_destruct]
+ -[CPLUIScopeObservedSource addObserver:registration:]
+ -[CPLUIScopeObservedSource fetchObservedEventForObserver:completionHandler:]
+ -[CPLUIScopeObservedSource initWithDelegate:queue:]
+ -[CPLUIScopeObservedSource isValidRegistration:]
+ -[CPLUIScopeObservedSource notifyUIStatusForAllScopesHaveChanged]
+ -[CPLUIScopeObservedSource notifyUIStatusForScopesWithIdentifiersHaveChanged:]
+ -[CPLUIScopeObservedSource notifyUIStatusScopeWithIdentifiers:isSynchronizing:]
+ -[CPLUIScopeObservedSource sourceStatusDictionary]
+ -[CPLUIScopeObservedSource sourceStatus]
+ -[CPLUIScopeObservedSource statusDictionaryForObserver:]
+ -[CPLUIScopeObservedSource statusForObserver:]
+ -[CPLUIScopeObservedSource updateRegistration:forObserver:]
+ -[CPLUIScopeObserver .cxx_destruct]
+ -[CPLUIScopeObserver addObservedScopesWithIdentifiers:]
+ -[CPLUIScopeObserver addObservedScopesWithIdentifiers:removeObservedScopesWithIdentifiers:]
+ -[CPLUIScopeObserver didDisconnectFromObservedSource]
+ -[CPLUIScopeObserver didRefreshObservedEvent:]
+ -[CPLUIScopeObserver newEmptyRegistration]
+ -[CPLUIScopeObserver observedScopeIdentifiers]
+ -[CPLUIScopeObserver removeObservedScopesWithIdentifiers:]
+ -[CPLUIScopeObserver setObservedScopeIdentifiers:]
+ -[CPLUIScopeObserverRegistration .cxx_destruct]
+ -[CPLUIScopeObserverRegistration coveredScopeIdentifiersFromScopeIdentifiers:]
+ -[CPLUIScopeObserverRegistration coveredScopeIdentifiersFromScopeIdentifiersEnumeration:]
+ -[CPLUIScopeObserverRegistration coveredScopeIdentifiers]
+ -[CPLUIScopeObserverRegistration encodeWithCoder:]
+ -[CPLUIScopeObserverRegistration forAllScopes]
+ -[CPLUIScopeObserverRegistration getAddedScopeIdentifiers:deletedScopeIdentifiers:withNewRegistration:]
+ -[CPLUIScopeObserverRegistration initForAllScopes]
+ -[CPLUIScopeObserverRegistration initWithCoder:]
+ -[CPLUIScopeObserverRegistration initWithCoveredScopeIdentifiers:]
+ -[CPLUIScopeObserverRegistration init]
+ -[CPLUIScopeObserverRegistration isObservedScopeIdentifier:]
+ -[CPLUIScopeObserverRegistration plistDescription]
+ -[CPLUIScopeObserverRegistration registrationByAddingScopeIdentifiers:removingScopeIdentifiers:]
+ -[CPLUIScopeObserverRegistration simpleDescription]
+ -[CPLUIScopeStatus .cxx_destruct]
+ -[CPLUIScopeStatus _deserializeAssetCountPerType]
+ -[CPLUIScopeStatus assetCountPerTypeData]
+ -[CPLUIScopeStatus assetCountPerType]
+ -[CPLUIScopeStatus busyState]
+ -[CPLUIScopeStatus clientFeatureCompatibleVersion]
+ -[CPLUIScopeStatus copyWithoutSynchronizing]
+ -[CPLUIScopeStatus deleteDate]
+ -[CPLUIScopeStatus description]
+ -[CPLUIScopeStatus encodeWithCoder:]
+ -[CPLUIScopeStatus estimatedCountOfRemainingRecordsDuringSharedLibraryExit]
+ -[CPLUIScopeStatus hasChangesToDownload]
+ -[CPLUIScopeStatus hasChangesToProcess]
+ -[CPLUIScopeStatus hasChangesToUpload]
+ -[CPLUIScopeStatus initEmpty]
+ -[CPLUIScopeStatus initWithCoder:]
+ -[CPLUIScopeStatus isBlockedBySnapshot]
+ -[CPLUIScopeStatus isEqual:]
+ -[CPLUIScopeStatus isExceedingLimit]
+ -[CPLUIScopeStatus isExceedingQuota]
+ -[CPLUIScopeStatus isExceedingSharedLibraryLimit]
+ -[CPLUIScopeStatus isExceedingSharedLibraryQuota]
+ -[CPLUIScopeStatus isInResetSync]
+ -[CPLUIScopeStatus isSynchronizing]
+ -[CPLUIScopeStatus lastSyncDate]
+ -[CPLUIScopeStatus numberOfOtherAssets]
+ -[CPLUIScopeStatus numberOfPhotoAssets]
+ -[CPLUIScopeStatus numberOfVideoAssets]
+ -[CPLUIScopeStatus permanentError]
+ -[CPLUIScopeStatus serverFeatureCompatibleVersion]
+ -[CPLUIScopeStatus setAssetCountPerTypeData:]
+ -[CPLUIScopeStatus setBusyState:]
+ -[CPLUIScopeStatus setDeleteDate:]
+ -[CPLUIScopeStatus setEstimatedCountOfRemainingRecordsDuringSharedLibraryExit:]
+ -[CPLUIScopeStatus setHasChangesToDownload:]
+ -[CPLUIScopeStatus setHasChangesToProcess:]
+ -[CPLUIScopeStatus setHasChangesToUpload:]
+ -[CPLUIScopeStatus setIsExceedingLimit:]
+ -[CPLUIScopeStatus setIsExceedingQuota:]
+ -[CPLUIScopeStatus setIsExceedingSharedLibraryLimit:]
+ -[CPLUIScopeStatus setIsExceedingSharedLibraryQuota:]
+ -[CPLUIScopeStatus setIsInResetSync:]
+ -[CPLUIScopeStatus setIsSynchronizing:]
+ -[CPLUIScopeStatus setLastSyncDate:]
+ -[CPLUIScopeStatus setPermanentError:]
+ -[CPLUIScopeStatus setServerFeatureCompatibleVersion:]
+ -[CPLUIScopeStatus shouldUpgradeToAccessAllPhotos]
+ -[CPLUISyncActivityObservedEvent .cxx_destruct]
+ -[CPLUISyncActivityObservedEvent encodeWithCoder:]
+ -[CPLUISyncActivityObservedEvent eventDescription]
+ -[CPLUISyncActivityObservedEvent initWithCoder:]
+ -[CPLUISyncActivityObservedEvent initWithSyncActivity:type:clientSessionActivity:scopeIdentifier:]
+ -[CPLUISyncActivityObservedEvent initWithSyncActivity:type:clientSessionActivity:scopeIdentifier:progress:]
+ -[CPLUISyncActivityObservedEvent isDoingSomeActivity]
+ -[CPLUISyncActivityObservedEvent isInClientSession]
+ -[CPLUISyncActivityObservedEvent isInSyncActivity]
+ -[CPLUISyncActivityObservedEvent plistDescription]
+ -[CPLUISyncActivityObservedEvent progress]
+ -[CPLUISyncActivityObservedEvent scopeIdentifier]
+ -[CPLUISyncActivityObservedEvent type]
+ -[CPLUISyncActivityObservedSource .cxx_destruct]
+ -[CPLUISyncActivityObservedSource fetchObservedEventForObserver:completionHandler:]
+ -[CPLUISyncActivityObservedSource notifyProgress:forScopeWithIdentifier:fromSource:]
+ -[CPLUISyncActivityObservedSource notifySyncActivityIsBlocked:forSource:]
+ -[CPLUISyncActivityObservedSource sourceStatusDictionary]
+ -[CPLUISyncActivityObservedSource sourceStatus]
+ -[CPLUISyncActivityObservedSource startClientSession]
+ -[CPLUISyncActivityObservedSource startSyncActivityForScopeWithIdentifier:fromSource:]
+ -[CPLUISyncActivityObservedSource startSyncActivityFromSource:]
+ -[CPLUISyncActivityObservedSource stopClientSession]
+ -[CPLUISyncActivityObservedSource stopSyncActivityForScopeWithIdentifier:fromSource:]
+ -[CPLUISyncActivityObservedSource stopSyncActivityForSource:]
+ -[CPLUISyncActivityObservedSource syncActivitySource]
+ -[CPLUISyncActivityObserver .cxx_destruct]
+ -[CPLUISyncActivityObserver didDisconnectFromObservedSource]
+ -[CPLUISyncActivityObserver didRefreshObservedEvent:]
+ -[CPLUITestObservedEvent encodeWithCoder:]
+ -[CPLUITestObservedEvent eventDescription]
+ -[CPLUITestObservedEvent initWithCoder:]
+ -[CPLUITestObservedEvent initWithStartEvent:]
+ -[CPLUITestObservedEvent isStartEvent]
+ -[CPLUITestObservedEvent plistDescription]
+ -[CPLUITestObservedSource fetchObservedEventForObserver:completionHandler:]
+ -[CPLUITestObservedSource isStarted]
+ -[CPLUITestObservedSource sourceStatusDictionary]
+ -[CPLUITestObservedSource sourceStatus]
+ -[CPLUITestObservedSource start]
+ -[CPLUITestObservedSource stop]
+ -[CPLUITestObserver didDisconnectFromObservedSource]
+ -[CPLUITestObserver didRefreshObservedEvent:]
+ -[CPLUIUploadProgressHub .cxx_destruct]
+ -[CPLUIUploadProgressHub _progressDidChangeForCloudScopedIdentifier:]
+ -[CPLUIUploadProgressHub _reportProgressForItem:]
+ -[CPLUIUploadProgressHub addUploadType:forCloudScopedIdentifier:]
+ -[CPLUIUploadProgressHub dropUploadType:forCloudScopedIdentifier:]
+ -[CPLUIUploadProgressHub init]
+ -[CPLUIUploadProgressHub noteUploadProgress:uploadType:forCloudScopedIdentifier:]
+ -[CPLUIUploadProgressHub popProgressUpdates]
+ -[CPLUIUploadProgressHub willUploadCloudChange:forLocalChange:]
+ -[CPLUploadComputeStatesTask shouldSkipScopesWithPermanentError]
+ -[CPLUploadPushedChangesTask _finishUIProgressReport]
+ -[CPLUploadPushedChangesTask _observationCenter]
+ -[CPLUploadPushedChangesTask _reportProgressToUIStep:]
+ -[CPLUploadPushedChangesTask _thresholdWithDefaultValue:defaultsKey:]
+ -[CPLUploadPushedChangesTask didUseOverLimitStrategy]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:derivativesGenerationForChange:didProgress:]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:didFinishGeneratingDerivativesForChange:]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:didFinishWithError:]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:didProgressGeneratingDerivativesFromResourceSize:]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:willStartGeneratingDerivativesForChange:]
+ -[CPLUploadPushedChangesTask generateDerivativesSubtask:willStartWithChangeCount:]
+ -[NSError(CPLAdditions) cplOriginalError]
+ -[NSError(CPLAdditions) cplSimpleDescription]
+ -[NSError(CPLAdditions) cplSimpleRedactedDescription]
+ -[_CPLDirectUploadSubtask .cxx_destruct]
+ -[_CPLDirectUploadSubtask initWithObject:phaseDescription:launchHandler:cancelHandler:]
+ -[_CPLKeyValueObserver .cxx_destruct]
+ -[_CPLKeyValueObserver observeValueForKeyPath:ofObject:change:context:]
+ -[_CPLUIRecordObserverState .cxx_destruct]
+ -[_CPLUIRecordObserverState _updateChangedScopedIdentifiers:]
+ -[_CPLUIRecordObserverState notifyUploadProgressForRecordsWithLocalScopedIdentifiers:registration:]
+ -[_CPLUIScopeObserverState .cxx_destruct]
+ -[_CPLUIScopeObserverState _updateChangedScopeIdentifiers:]
+ -[_CPLUIScopeObserverState notifyUIStatusForScopesWithIdentifiersHaveChanged:registration:]
+ -[_CPLUIUploadProgressItem .cxx_destruct]
+ -[_CPLUIUploadProgressItem _notifyProgressDidChangeToHub:]
+ -[_CPLUIUploadProgressItem currentProgress]
+ GCC_except_table1115
+ GCC_except_table1195
+ GCC_except_table1249
+ GCC_except_table1300
+ GCC_except_table1318
+ GCC_except_table1320
+ GCC_except_table1494
+ GCC_except_table1543
+ GCC_except_table1547
+ GCC_except_table1549
+ GCC_except_table1554
+ GCC_except_table1556
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1573
+ GCC_except_table1576
+ GCC_except_table1579
+ GCC_except_table1585
+ GCC_except_table1587
+ GCC_except_table1589
+ GCC_except_table1591
+ GCC_except_table1673
+ GCC_except_table172
+ GCC_except_table1761
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table19
+ GCC_except_table193
+ GCC_except_table200
+ GCC_except_table2009
+ GCC_except_table2017
+ GCC_except_table215
+ GCC_except_table22
+ GCC_except_table2240
+ GCC_except_table2241
+ GCC_except_table2244
+ GCC_except_table2251
+ GCC_except_table2255
+ GCC_except_table2282
+ GCC_except_table2289
+ GCC_except_table2299
+ GCC_except_table2302
+ GCC_except_table239
+ GCC_except_table2489
+ GCC_except_table254
+ GCC_except_table2588
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table265
+ GCC_except_table2654
+ GCC_except_table2662
+ GCC_except_table267
+ GCC_except_table2703
+ GCC_except_table2795
+ GCC_except_table2802
+ GCC_except_table2955
+ GCC_except_table297
+ GCC_except_table3044
+ GCC_except_table3330
+ GCC_except_table3332
+ GCC_except_table3411
+ GCC_except_table3415
+ GCC_except_table3425
+ GCC_except_table3435
+ GCC_except_table3493
+ GCC_except_table3495
+ GCC_except_table3620
+ GCC_except_table3644
+ GCC_except_table370
+ GCC_except_table3726
+ GCC_except_table3730
+ GCC_except_table3732
+ GCC_except_table3734
+ GCC_except_table3738
+ GCC_except_table376
+ GCC_except_table3899
+ GCC_except_table3946
+ GCC_except_table40
+ GCC_except_table4191
+ GCC_except_table426
+ GCC_except_table4267
+ GCC_except_table4271
+ GCC_except_table4273
+ GCC_except_table4282
+ GCC_except_table437
+ GCC_except_table4484
+ GCC_except_table4498
+ GCC_except_table45
+ GCC_except_table4655
+ GCC_except_table4685
+ GCC_except_table4716
+ GCC_except_table4734
+ GCC_except_table4741
+ GCC_except_table4749
+ GCC_except_table4751
+ GCC_except_table4765
+ GCC_except_table4767
+ GCC_except_table4770
+ GCC_except_table510
+ GCC_except_table514
+ GCC_except_table5142
+ GCC_except_table5175
+ GCC_except_table5177
+ GCC_except_table5203
+ GCC_except_table53
+ GCC_except_table530
+ GCC_except_table5337
+ GCC_except_table5347
+ GCC_except_table5404
+ GCC_except_table5407
+ GCC_except_table552
+ GCC_except_table5585
+ GCC_except_table5593
+ GCC_except_table5683
+ GCC_except_table5687
+ GCC_except_table569
+ GCC_except_table5693
+ GCC_except_table570
+ GCC_except_table5700
+ GCC_except_table5715
+ GCC_except_table5716
+ GCC_except_table5722
+ GCC_except_table5766
+ GCC_except_table5772
+ GCC_except_table5776
+ GCC_except_table58
+ GCC_except_table580
+ GCC_except_table5837
+ GCC_except_table5839
+ GCC_except_table5841
+ GCC_except_table5853
+ GCC_except_table598
+ GCC_except_table6002
+ GCC_except_table6044
+ GCC_except_table6054
+ GCC_except_table6055
+ GCC_except_table611
+ GCC_except_table6114
+ GCC_except_table6117
+ GCC_except_table6202
+ GCC_except_table6204
+ GCC_except_table6220
+ GCC_except_table6243
+ GCC_except_table6259
+ GCC_except_table6261
+ GCC_except_table6421
+ GCC_except_table6449
+ GCC_except_table6490
+ GCC_except_table6510
+ GCC_except_table6536
+ GCC_except_table6547
+ GCC_except_table6568
+ GCC_except_table6588
+ GCC_except_table6592
+ GCC_except_table6618
+ GCC_except_table6690
+ GCC_except_table6753
+ GCC_except_table6779
+ GCC_except_table6783
+ GCC_except_table6810
+ GCC_except_table6823
+ GCC_except_table6828
+ GCC_except_table6836
+ GCC_except_table6837
+ GCC_except_table6851
+ GCC_except_table6906
+ GCC_except_table7031
+ GCC_except_table7045
+ GCC_except_table7048
+ GCC_except_table7174
+ GCC_except_table7176
+ GCC_except_table7178
+ GCC_except_table7182
+ GCC_except_table7185
+ GCC_except_table721
+ GCC_except_table727
+ GCC_except_table7560
+ GCC_except_table7600
+ GCC_except_table7604
+ GCC_except_table762
+ GCC_except_table7621
+ GCC_except_table7627
+ GCC_except_table7635
+ GCC_except_table7641
+ GCC_except_table7645
+ GCC_except_table7653
+ GCC_except_table7656
+ GCC_except_table766
+ GCC_except_table7676
+ GCC_except_table7683
+ GCC_except_table769
+ GCC_except_table7706
+ GCC_except_table771
+ GCC_except_table774
+ GCC_except_table7741
+ GCC_except_table776
+ GCC_except_table7772
+ GCC_except_table7783
+ GCC_except_table780
+ GCC_except_table7803
+ GCC_except_table7806
+ GCC_except_table7808
+ GCC_except_table7810
+ GCC_except_table782
+ GCC_except_table7841
+ GCC_except_table7891
+ GCC_except_table791
+ GCC_except_table795
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table803
+ GCC_except_table8040
+ GCC_except_table805
+ GCC_except_table8063
+ GCC_except_table807
+ GCC_except_table809
+ GCC_except_table8093
+ GCC_except_table811
+ GCC_except_table813
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table8248
+ GCC_except_table825
+ GCC_except_table8250
+ GCC_except_table827
+ GCC_except_table8280
+ GCC_except_table8289
+ GCC_except_table829
+ GCC_except_table8294
+ GCC_except_table8310
+ GCC_except_table8324
+ GCC_except_table8334
+ GCC_except_table8339
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table8423
+ GCC_except_table844
+ GCC_except_table846
+ GCC_except_table848
+ GCC_except_table850
+ GCC_except_table8510
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table8569
+ GCC_except_table8647
+ GCC_except_table8662
+ GCC_except_table8684
+ GCC_except_table8690
+ GCC_except_table8709
+ GCC_except_table8719
+ GCC_except_table874
+ GCC_except_table8755
+ GCC_except_table8762
+ GCC_except_table880
+ GCC_except_table8843
+ GCC_except_table889
+ GCC_except_table898
+ GCC_except_table910
+ _CPLAppBundleIdentifierForAppContainerIdentifier
+ _CPLAppContainerIdentifierForLibraryIdentifier
+ _CPLBrokenScopeClass
+ _CPLEnableNTimeURLInSharedCollection
+ _CPLEngineScopeStatusKeyLastSyncDate
+ _CPLEngineScopeStatusKeyPermanentError
+ _CPLEngineScopeStatusKeyPermanentErrorDate
+ _CPLIsCollectionShareFeatureDataclassAutomaticallyEnabled
+ _CPLIsValidCollectionShareScopeIdentifier
+ _CPLRegisterForTurboModeUpdates
+ _CPLScopeChangeScopeIdentifier
+ _CPLScopeIdentifierPrefixForCollectionShareSilentMigration
+ _CPLSetBrokenScopeClass
+ _CPLSetShouldRedactURLs
+ _CPLSetStoreWipeHandlerClass
+ _CPLSetTurboMode
+ _CPLSetTurboModeExpirationDate
+ _CPLShouldUseDebugTurboMode
+ _CPLShouldUseTurboMode
+ _CPLStoreWipeHandlerClass
+ _CPLStringFromAccountPartitionType
+ _CPLTurboModeExpirationDate
+ _CPLTurboModeNonExpiredExpirationDate
+ _CPLUnregisterFromTurboModeUpdates
+ _CPLUploadCheckRuleDeleteProxyRecordsFunction
+ _NSProcessInfoPowerStateDidChangeNotification
+ _OBJC_CLASS_$_CPLBatterySaverWatcher
+ _OBJC_CLASS_$_CPLDefaultBrokenScope
+ _OBJC_CLASS_$_CPLDirectUploadTask
+ _OBJC_CLASS_$_CPLEngineDefaultStoreWipeHandler
+ _OBJC_CLASS_$_CPLEngineForceSyncWithPushFromClientTask
+ _OBJC_CLASS_$_CPLEngineUIObservationCenter
+ _OBJC_CLASS_$_CPLGenerateDerivativesSubtask
+ _OBJC_CLASS_$_CPLLibraryParameters
+ _OBJC_CLASS_$_CPLPartialDerivativesGenerationResult
+ _OBJC_CLASS_$_CPLPhotosSchemaFilter
+ _OBJC_CLASS_$_CPLPlistSchemaFilter
+ _OBJC_CLASS_$_CPLPostChange
+ _OBJC_CLASS_$_CPLSchemaFilter
+ _OBJC_CLASS_$_CPLTransportContainerConfiguration
+ _OBJC_CLASS_$_CPLUIObservedEvent
+ _OBJC_CLASS_$_CPLUIObservedSource
+ _OBJC_CLASS_$_CPLUIObserver
+ _OBJC_CLASS_$_CPLUIObserverAndRegistration
+ _OBJC_CLASS_$_CPLUIObserverManager
+ _OBJC_CLASS_$_CPLUIObserverRegistration
+ _OBJC_CLASS_$_CPLUIRecordObservedEvent
+ _OBJC_CLASS_$_CPLUIRecordObservedEventAccumulator
+ _OBJC_CLASS_$_CPLUIRecordObservedSource
+ _OBJC_CLASS_$_CPLUIRecordObserver
+ _OBJC_CLASS_$_CPLUIRecordObserverRegistration
+ _OBJC_CLASS_$_CPLUIRecordStatus
+ _OBJC_CLASS_$_CPLUIScopeObservedEvent
+ _OBJC_CLASS_$_CPLUIScopeObservedSource
+ _OBJC_CLASS_$_CPLUIScopeObserver
+ _OBJC_CLASS_$_CPLUIScopeObserverRegistration
+ _OBJC_CLASS_$_CPLUIScopeStatus
+ _OBJC_CLASS_$_CPLUISyncActivityObservedEvent
+ _OBJC_CLASS_$_CPLUISyncActivityObservedSource
+ _OBJC_CLASS_$_CPLUISyncActivityObserver
+ _OBJC_CLASS_$_CPLUITestObservedEvent
+ _OBJC_CLASS_$_CPLUITestObservedSource
+ _OBJC_CLASS_$_CPLUITestObserver
+ _OBJC_CLASS_$_CPLUIUploadProgressHub
+ _OBJC_CLASS_$__CPLDirectUploadSubtask
+ _OBJC_CLASS_$__CPLKeyValueObserver
+ _OBJC_CLASS_$__CPLUIRecordObserverState
+ _OBJC_CLASS_$__CPLUIScopeObserverState
+ _OBJC_CLASS_$__CPLUIUploadProgressItem
+ _OBJC_IVAR_$_CPLActiveDownloadQueue._shouldFetchExportedID
+ _OBJC_IVAR_$_CPLActiveDownloadQueue._shouldFetchReference
+ _OBJC_IVAR_$_CPLAssetChange._assetBatchIdentifier
+ _OBJC_IVAR_$_CPLAssetChange._proxyBestResourceType
+ _OBJC_IVAR_$_CPLAssetChange._proxyExpectedMasterIdentifier
+ _OBJC_IVAR_$_CPLAssetChange._proxyExpectedVideoDuration
+ _OBJC_IVAR_$_CPLAssetChange._proxyExpirationDate
+ _OBJC_IVAR_$_CPLAssetChange._rating
+ _OBJC_IVAR_$_CPLBatterySaverWatcher._batterySaverMode
+ _OBJC_IVAR_$_CPLBatterySaverWatcher._delegate
+ _OBJC_IVAR_$_CPLBatterySaverWatcher._queue
+ _OBJC_IVAR_$_CPLBatterySaverWatcher._watching
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItem._droppingChange
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItems._droppedFullRecordScopedIdentifiers
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItems._immutableItems
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItems._mutableItems
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItems._uiUploadProgressHub
+ _OBJC_IVAR_$_CPLCallObserver._onTimeOutBlock
+ _OBJC_IVAR_$_CPLChangeBatch._pullUUID
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._expiringState
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._expiryDate
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._keyAssetIdentifier
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._migrationOriginatingSharedAlbumIdentifier
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._migrationStartTime
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._migrationState
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._thumbnailImageData
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._userLastViewedNotificationDate
+ _OBJC_IVAR_$_CPLCollectionShareScopeChange._viewingMode
+ _OBJC_IVAR_$_CPLCommentChange._isPostComment
+ _OBJC_IVAR_$_CPLCommentChange._postIdentifier
+ _OBJC_IVAR_$_CPLDefaultBrokenScope._engineLibrary
+ _OBJC_IVAR_$_CPLDefaultBrokenScope._engineScope
+ _OBJC_IVAR_$_CPLDirectUploadTask._batch
+ _OBJC_IVAR_$_CPLDirectUploadTask._bypassLimits
+ _OBJC_IVAR_$_CPLDirectUploadTask._cancelled
+ _OBJC_IVAR_$_CPLDirectUploadTask._checkItems
+ _OBJC_IVAR_$_CPLDirectUploadTask._cloudCache
+ _OBJC_IVAR_$_CPLDirectUploadTask._cloudScopedIdentifierToCloudRecordToCommit
+ _OBJC_IVAR_$_CPLDirectUploadTask._cloudScopedIdentifiersToLocalChange
+ _OBJC_IVAR_$_CPLDirectUploadTask._creationDate
+ _OBJC_IVAR_$_CPLDirectUploadTask._currentSubtask
+ _OBJC_IVAR_$_CPLDirectUploadTask._derivativesCache
+ _OBJC_IVAR_$_CPLDirectUploadTask._derivativesFilter
+ _OBJC_IVAR_$_CPLDirectUploadTask._engine
+ _OBJC_IVAR_$_CPLDirectUploadTask._fetchCache
+ _OBJC_IVAR_$_CPLDirectUploadTask._finished
+ _OBJC_IVAR_$_CPLDirectUploadTask._hasStartedUIProgressReporting
+ _OBJC_IVAR_$_CPLDirectUploadTask._lock
+ _OBJC_IVAR_$_CPLDirectUploadTask._owner
+ _OBJC_IVAR_$_CPLDirectUploadTask._progressPerRecord
+ _OBJC_IVAR_$_CPLDirectUploadTask._scope
+ _OBJC_IVAR_$_CPLDirectUploadTask._scopeIdentifier
+ _OBJC_IVAR_$_CPLDirectUploadTask._scopes
+ _OBJC_IVAR_$_CPLDirectUploadTask._sharedScope
+ _OBJC_IVAR_$_CPLDirectUploadTask._store
+ _OBJC_IVAR_$_CPLDirectUploadTask._targetMapping
+ _OBJC_IVAR_$_CPLDirectUploadTask._taskDidFinishWithErrorBlock
+ _OBJC_IVAR_$_CPLDirectUploadTask._taskIdentifier
+ _OBJC_IVAR_$_CPLDirectUploadTask._transport
+ _OBJC_IVAR_$_CPLDirectUploadTask._transportScopeMapping
+ _OBJC_IVAR_$_CPLDirectUploadTask._transportUserIdentifier
+ _OBJC_IVAR_$_CPLDirectUploadTask._uiUploadProgressHub
+ _OBJC_IVAR_$_CPLDirectUploadTask._uploadedBatch
+ _OBJC_IVAR_$_CPLEngineComponentEnumerator._queue
+ _OBJC_IVAR_$_CPLEngineDefaultStoreWipeHandler._reason
+ _OBJC_IVAR_$_CPLEngineDerivativesCache._identifier
+ _OBJC_IVAR_$_CPLEngineDerivativesCache._parentCache
+ _OBJC_IVAR_$_CPLEngineDerivativesCache._subCacheIdentifiers
+ _OBJC_IVAR_$_CPLEngineForceSyncTask._isFullSyncSession
+ _OBJC_IVAR_$_CPLEngineForceSyncTask._uniqueScopeIdentifier
+ _OBJC_IVAR_$_CPLEngineForceSyncWithPushFromClientTask._currentSubTask
+ _OBJC_IVAR_$_CPLEngineForceSyncWithPushFromClientTask._engineLibrary
+ _OBJC_IVAR_$_CPLEngineForceSyncWithPushFromClientTask._lock
+ _OBJC_IVAR_$_CPLEngineForceSyncWithPushFromClientTask._onPushFromClientCompleted
+ _OBJC_IVAR_$_CPLEngineForceSyncWithPushFromClientTask._pushFromClientProgress
+ _OBJC_IVAR_$_CPLEngineLibrary._allowedDisabledFeatureDataclasses
+ _OBJC_IVAR_$_CPLEngineLibrary._allowedFeatureDataclasses
+ _OBJC_IVAR_$_CPLEngineLibrary._observationCenter
+ _OBJC_IVAR_$_CPLEngineLibrary._parameters
+ _OBJC_IVAR_$_CPLEngineLibrary._parametersLock
+ _OBJC_IVAR_$_CPLEngineMultiscopeSyncTask._coveredScopeIndex
+ _OBJC_IVAR_$_CPLEngineMultiscopeSyncTask._currentTaskLock
+ _OBJC_IVAR_$_CPLEngineMultiscopeSyncTask._initialCoveredScopesCount
+ _OBJC_IVAR_$_CPLEngineMultiscopeSyncTask._scopeIdentifiersForUIObservation
+ _OBJC_IVAR_$_CPLEnginePushRepository._shouldOrderRecordsBySize
+ _OBJC_IVAR_$_CPLEngineScheduler._canUseTurboMode
+ _OBJC_IVAR_$_CPLEngineScheduler._isUsingTurboMode
+ _OBJC_IVAR_$_CPLEngineScheduler._turboModeLock
+ _OBJC_IVAR_$_CPLEngineScheduler._turboModeObserver
+ _OBJC_IVAR_$_CPLEngineScopeStorage._classesForInitialQueriesPerScopeType
+ _OBJC_IVAR_$_CPLEngineScopedTask._scopeIdentifierForUIObservation
+ _OBJC_IVAR_$_CPLEngineStore._uiObserving
+ _OBJC_IVAR_$_CPLEngineSyncTask._backgroundSchedulingBypassTransaction
+ _OBJC_IVAR_$_CPLEngineSyncTask._shouldBypassBackgroundSchedulingIfPossible
+ _OBJC_IVAR_$_CPLEngineSyncTask._syncActivitySource
+ _OBJC_IVAR_$_CPLEngineSystemMonitor._lowPowerModeWatcher
+ _OBJC_IVAR_$_CPLEngineSystemMonitor._turboModeFlags
+ _OBJC_IVAR_$_CPLEngineUIObservationCenter._engineLibrary
+ _OBJC_IVAR_$_CPLEngineUIObservationCenter._queue
+ _OBJC_IVAR_$_CPLEngineUIObservationCenter._sources
+ _OBJC_IVAR_$_CPLExtractedBatch._mutableScopedIdentifiers
+ _OBJC_IVAR_$_CPLExtractedBatch._mutableUntrustableScopedIdentifiers
+ _OBJC_IVAR_$_CPLExtractedBatch._scopedIdentifiers
+ _OBJC_IVAR_$_CPLFingerprintContext._forceMMCSv2AsDefault
+ _OBJC_IVAR_$_CPLForceSyncTask._context
+ _OBJC_IVAR_$_CPLForceSyncTask._lock
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._acquireBackgroundSchedulerRequest
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._allowsCancellingActiveDerivativesGeneration
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._cancelled
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._changes
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._delegate
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._derivativesCache
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._derivativesFilter
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._derivativesSizeReportTimer
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._derivativesSizeToReport
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._fingerprintContext
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesCancellationHandler
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesChange
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesDeferredHandler
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesLastFractionCompleted
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesProgress
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._generateDerivativesTotalSize
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._predictor
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._queue
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._session
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._shouldUseCache
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._startTime
+ _OBJC_IVAR_$_CPLGenerateDerivativesSubtask._totalSourceResourceSize
+ _OBJC_IVAR_$_CPLLibraryManager._libraryManagerType
+ _OBJC_IVAR_$_CPLLibraryManager._parameters
+ _OBJC_IVAR_$_CPLLibraryManager._parametersLock
+ _OBJC_IVAR_$_CPLLibraryManager._uiObservers
+ _OBJC_IVAR_$_CPLLibraryParameters._clientLibraryBaseURL
+ _OBJC_IVAR_$_CPLLibraryParameters._cloudLibraryResourceStorageURL
+ _OBJC_IVAR_$_CPLLibraryParameters._cloudLibraryStateStorageURL
+ _OBJC_IVAR_$_CPLLibraryParameters._libraryIdentifier
+ _OBJC_IVAR_$_CPLLibraryParameters._mainScopeIdentifier
+ _OBJC_IVAR_$_CPLLibraryParameters._options
+ _OBJC_IVAR_$_CPLLibraryParameters._transportContainerConfiguration
+ _OBJC_IVAR_$_CPLPartialDerivativesGenerationResult._safeFilenames
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._allowedResources
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._droppedResources
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._filterDefinition
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._ignoreProperties
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._loaded
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._lock
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._supportedRecordClasses
+ _OBJC_IVAR_$_CPLPlistSchemaFilter._testingSchema
+ _OBJC_IVAR_$_CPLPostChange._caption
+ _OBJC_IVAR_$_CPLPostChange._creationDate
+ _OBJC_IVAR_$_CPLProxyLibraryManager._registeredObservers
+ _OBJC_IVAR_$_CPLPullFromTransportScopeTask._supportedFeatureVersion
+ _OBJC_IVAR_$_CPLReactChange._reactText
+ _OBJC_IVAR_$_CPLRecordChange._fromInitialDownload
+ _OBJC_IVAR_$_CPLRecordChange._proxyState
+ _OBJC_IVAR_$_CPLResourceIdentity._transportReference
+ _OBJC_IVAR_$_CPLSchemaFilter._containerIdentifier
+ _OBJC_IVAR_$_CPLSchemaFilter._lock
+ _OBJC_IVAR_$_CPLSchemaFilter._transportFilters
+ _OBJC_IVAR_$_CPLScopeChange._overLimit
+ _OBJC_IVAR_$_CPLScopeChange._overQuota
+ _OBJC_IVAR_$_CPLScopeChange._permanentError
+ _OBJC_IVAR_$_CPLShare._allowsAccessRequests
+ _OBJC_IVAR_$_CPLShare._allowsAnonymousPublicAccess
+ _OBJC_IVAR_$_CPLShareParticipant._isPlaceholder
+ _OBJC_IVAR_$_CPLShareParticipant._nTimeURL
+ _OBJC_IVAR_$_CPLShareParticipant._subscriptionDate
+ _OBJC_IVAR_$_CPLSyncSession._backgroundScheduler
+ _OBJC_IVAR_$_CPLSyncSession._bypassBackgroundSchedulingRetainCount
+ _OBJC_IVAR_$_CPLSyncSession._hasBeenJustInCaseSession
+ _OBJC_IVAR_$_CPLSyncSession._hasEnoughPowerToBypassBackgroundScheduling
+ _OBJC_IVAR_$_CPLSyncSession._usesTurboMode
+ _OBJC_IVAR_$_CPLSyncSessionBlockedState._backgroundScheduler
+ _OBJC_IVAR_$_CPLTransportContainerConfiguration._bundleIdentifier
+ _OBJC_IVAR_$_CPLTransportContainerConfiguration._containerIdentifier
+ _OBJC_IVAR_$_CPLTransportContainerConfiguration._fingerprintContext
+ _OBJC_IVAR_$_CPLTransportContainerConfiguration._options
+ _OBJC_IVAR_$_CPLTransportContainerConfiguration._schemaFilter
+ _OBJC_IVAR_$_CPLTransportUpdateScopeTask._queue
+ _OBJC_IVAR_$_CPLTransportUpdateScopeTask._transportTask
+ _OBJC_IVAR_$_CPLUIObservedSource._coalescingTimer
+ _OBJC_IVAR_$_CPLUIObservedSource._delegate
+ _OBJC_IVAR_$_CPLUIObservedSource._observersToNotify
+ _OBJC_IVAR_$_CPLUIObservedSource._queue
+ _OBJC_IVAR_$_CPLUIObservedSource._registeredObservers
+ _OBJC_IVAR_$_CPLUIObservedSource._shouldNotifyAllObservers
+ _OBJC_IVAR_$_CPLUIObserver._currentRegistration
+ _OBJC_IVAR_$_CPLUIObserver._delegate
+ _OBJC_IVAR_$_CPLUIObserver._hasPrivateObserverDelegateMethods
+ _OBJC_IVAR_$_CPLUIObserver._identifier
+ _OBJC_IVAR_$_CPLUIObserver._lastRegistrationUpdate
+ _OBJC_IVAR_$_CPLUIObserver._queue
+ _OBJC_IVAR_$_CPLUIObserver._underlyingManager
+ _OBJC_IVAR_$_CPLUIObserver._updateRegistrationTimer
+ _OBJC_IVAR_$_CPLUIObserverAndRegistration._observer
+ _OBJC_IVAR_$_CPLUIObserverAndRegistration._registration
+ _OBJC_IVAR_$_CPLUIObserverAndRegistration._state
+ _OBJC_IVAR_$_CPLUIObserverManager._closed
+ _OBJC_IVAR_$_CPLUIObserverManager._delegate
+ _OBJC_IVAR_$_CPLUIObserverManager._libraryIdentifier
+ _OBJC_IVAR_$_CPLUIObserverManager._libraryManager
+ _OBJC_IVAR_$_CPLUIObserverManager._notifyToken
+ _OBJC_IVAR_$_CPLUIObserverManager._opened
+ _OBJC_IVAR_$_CPLUIObserverManager._opening
+ _OBJC_IVAR_$_CPLUIObserverManager._queue
+ _OBJC_IVAR_$_CPLUIObserverManager._registeredObservers
+ _OBJC_IVAR_$_CPLUIObserverManager._shouldTryToReopen
+ _OBJC_IVAR_$_CPLUIObserverRegistration._type
+ _OBJC_IVAR_$_CPLUIRecordObservedEvent._blocked
+ _OBJC_IVAR_$_CPLUIRecordObservedEvent._updatedNonUploadingStatuses
+ _OBJC_IVAR_$_CPLUIRecordObservedEvent._updatedUploadingProgresses
+ _OBJC_IVAR_$_CPLUIRecordObservedEventAccumulator._blocked
+ _OBJC_IVAR_$_CPLUIRecordObservedEventAccumulator._invalidScopeIdentifiers
+ _OBJC_IVAR_$_CPLUIRecordObservedEventAccumulator._progresses
+ _OBJC_IVAR_$_CPLUIRecordObservedEventAccumulator._statuses
+ _OBJC_IVAR_$_CPLUIRecordObservedEventAccumulator._updatedScopedIdentifiers
+ _OBJC_IVAR_$_CPLUIRecordObservedSource._isBlocked
+ _OBJC_IVAR_$_CPLUIRecordObservedSource._localScopedIdentifiersAndProgress
+ _OBJC_IVAR_$_CPLUIRecordObserver._blocked
+ _OBJC_IVAR_$_CPLUIRecordObserver._scopedIdentifiersAndProgress
+ _OBJC_IVAR_$_CPLUIRecordObserverRegistration._coveredScopedIdentifiers
+ _OBJC_IVAR_$_CPLUIRecordStatus._progress
+ _OBJC_IVAR_$_CPLUIRecordStatus._type
+ _OBJC_IVAR_$_CPLUIScopeObservedEvent._statuses
+ _OBJC_IVAR_$_CPLUIScopeObservedSource._synchronizingScopeIdentifiers
+ _OBJC_IVAR_$_CPLUIScopeObserver._lastStatuses
+ _OBJC_IVAR_$_CPLUIScopeObserverRegistration._coveredScopeIdentifiers
+ _OBJC_IVAR_$_CPLUIScopeStatus._assetCountPerTypeData
+ _OBJC_IVAR_$_CPLUIScopeStatus._busyState
+ _OBJC_IVAR_$_CPLUIScopeStatus._deleteDate
+ _OBJC_IVAR_$_CPLUIScopeStatus._estimatedCountOfRemainingRecordsDuringSharedLibraryExit
+ _OBJC_IVAR_$_CPLUIScopeStatus._hasChangesToDownload
+ _OBJC_IVAR_$_CPLUIScopeStatus._hasChangesToProcess
+ _OBJC_IVAR_$_CPLUIScopeStatus._hasChangesToUpload
+ _OBJC_IVAR_$_CPLUIScopeStatus._hasDeserializedAssetCountPerType
+ _OBJC_IVAR_$_CPLUIScopeStatus._isExceedingLimit
+ _OBJC_IVAR_$_CPLUIScopeStatus._isExceedingQuota
+ _OBJC_IVAR_$_CPLUIScopeStatus._isExceedingSharedLibraryLimit
+ _OBJC_IVAR_$_CPLUIScopeStatus._isExceedingSharedLibraryQuota
+ _OBJC_IVAR_$_CPLUIScopeStatus._isInResetSync
+ _OBJC_IVAR_$_CPLUIScopeStatus._isSynchronizing
+ _OBJC_IVAR_$_CPLUIScopeStatus._lastSyncDate
+ _OBJC_IVAR_$_CPLUIScopeStatus._lock
+ _OBJC_IVAR_$_CPLUIScopeStatus._numberOfOtherAssets
+ _OBJC_IVAR_$_CPLUIScopeStatus._numberOfPhotoAssets
+ _OBJC_IVAR_$_CPLUIScopeStatus._numberOfVideoAssets
+ _OBJC_IVAR_$_CPLUIScopeStatus._permanentError
+ _OBJC_IVAR_$_CPLUIScopeStatus._serverFeatureCompatibleVersion
+ _OBJC_IVAR_$_CPLUISyncActivityObservedEvent._isInClientSession
+ _OBJC_IVAR_$_CPLUISyncActivityObservedEvent._isInSyncActivity
+ _OBJC_IVAR_$_CPLUISyncActivityObservedEvent._progress
+ _OBJC_IVAR_$_CPLUISyncActivityObservedEvent._scopeIdentifier
+ _OBJC_IVAR_$_CPLUISyncActivityObservedEvent._type
+ _OBJC_IVAR_$_CPLUISyncActivityObservedSource._isBlocked
+ _OBJC_IVAR_$_CPLUISyncActivityObservedSource._lastEvent
+ _OBJC_IVAR_$_CPLUISyncActivityObservedSource._syncActivitySource
+ _OBJC_IVAR_$_CPLUISyncActivityObserver._lastEvent
+ _OBJC_IVAR_$_CPLUITestObservedEvent._isStartEvent
+ _OBJC_IVAR_$_CPLUITestObservedSource._isStarted
+ _OBJC_IVAR_$_CPLUITestObserver._didStartTest
+ _OBJC_IVAR_$_CPLUIUploadProgressHub._cloudScopedIdentifierToItem
+ _OBJC_IVAR_$_CPLUIUploadProgressHub._progressUpdates
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._fetchCache
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesSubtask
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._hasStartedUIProgressReporting
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._isUsingOverLimitStrategy
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._networkIsTooSlow
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._shouldCheckAssetsWithServer
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._uiUploadProgressHub
+ _OBJC_IVAR_$__CPLDirectUploadSubtask._cancelHandler
+ _OBJC_IVAR_$__CPLDirectUploadSubtask._launchHandler
+ _OBJC_IVAR_$__CPLDirectUploadSubtask._object
+ _OBJC_IVAR_$__CPLDirectUploadSubtask._phaseDescription
+ _OBJC_IVAR_$__CPLKeyValueObserver._changeHandler
+ _OBJC_IVAR_$__CPLUIRecordObserverState._lastChangedScopedIdentifiers
+ _OBJC_IVAR_$__CPLUIScopeObserverState._lastChangedScopeIdentifiers
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._assetCloudScopedIdentifiers
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._cloudScopedIdentifier
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._masterCloudScopedIdentifier
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._masterItem
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._progressForDerivatives
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._progressForResourcesUpload
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._reportingLocalScopedIdentifier
+ _OBJC_IVAR_$__CPLUIUploadProgressItem._uploadType
+ _OBJC_METACLASS_$_CPLBatterySaverWatcher
+ _OBJC_METACLASS_$_CPLDefaultBrokenScope
+ _OBJC_METACLASS_$_CPLDirectUploadTask
+ _OBJC_METACLASS_$_CPLEngineDefaultStoreWipeHandler
+ _OBJC_METACLASS_$_CPLEngineForceSyncWithPushFromClientTask
+ _OBJC_METACLASS_$_CPLEngineUIObservationCenter
+ _OBJC_METACLASS_$_CPLGenerateDerivativesSubtask
+ _OBJC_METACLASS_$_CPLLibraryParameters
+ _OBJC_METACLASS_$_CPLPartialDerivativesGenerationResult
+ _OBJC_METACLASS_$_CPLPhotosSchemaFilter
+ _OBJC_METACLASS_$_CPLPlistSchemaFilter
+ _OBJC_METACLASS_$_CPLPostChange
+ _OBJC_METACLASS_$_CPLSchemaFilter
+ _OBJC_METACLASS_$_CPLTransportContainerConfiguration
+ _OBJC_METACLASS_$_CPLUIObservedEvent
+ _OBJC_METACLASS_$_CPLUIObservedSource
+ _OBJC_METACLASS_$_CPLUIObserver
+ _OBJC_METACLASS_$_CPLUIObserverAndRegistration
+ _OBJC_METACLASS_$_CPLUIObserverManager
+ _OBJC_METACLASS_$_CPLUIObserverRegistration
+ _OBJC_METACLASS_$_CPLUIRecordObservedEvent
+ _OBJC_METACLASS_$_CPLUIRecordObservedEventAccumulator
+ _OBJC_METACLASS_$_CPLUIRecordObservedSource
+ _OBJC_METACLASS_$_CPLUIRecordObserver
+ _OBJC_METACLASS_$_CPLUIRecordObserverRegistration
+ _OBJC_METACLASS_$_CPLUIRecordStatus
+ _OBJC_METACLASS_$_CPLUIScopeObservedEvent
+ _OBJC_METACLASS_$_CPLUIScopeObservedSource
+ _OBJC_METACLASS_$_CPLUIScopeObserver
+ _OBJC_METACLASS_$_CPLUIScopeObserverRegistration
+ _OBJC_METACLASS_$_CPLUIScopeStatus
+ _OBJC_METACLASS_$_CPLUISyncActivityObservedEvent
+ _OBJC_METACLASS_$_CPLUISyncActivityObservedSource
+ _OBJC_METACLASS_$_CPLUISyncActivityObserver
+ _OBJC_METACLASS_$_CPLUITestObservedEvent
+ _OBJC_METACLASS_$_CPLUITestObservedSource
+ _OBJC_METACLASS_$_CPLUITestObserver
+ _OBJC_METACLASS_$_CPLUIUploadProgressHub
+ _OBJC_METACLASS_$__CPLDirectUploadSubtask
+ _OBJC_METACLASS_$__CPLKeyValueObserver
+ _OBJC_METACLASS_$__CPLUIRecordObserverState
+ _OBJC_METACLASS_$__CPLUIScopeObserverState
+ _OBJC_METACLASS_$__CPLUIUploadProgressItem
+ __CPLSharedDefaultsForTurboMode
+ __CPLSharedDefaultsForTurboMode.onceToken
+ __CPLSharedDefaultsForTurboMode.result
+ __OBJC_$_CLASS_METHODS_CPLCollectionShareScopeChange
+ __OBJC_$_CLASS_METHODS_CPLEngineBackupSyncTask
+ __OBJC_$_CLASS_METHODS_CPLEngineDefaultStoreWipeHandler
+ __OBJC_$_CLASS_METHODS_CPLEngineDerivativesCache
+ __OBJC_$_CLASS_METHODS_CPLEngineDownloadSyncTask
+ __OBJC_$_CLASS_METHODS_CPLEngineForceProcessingStagedScopesTask
+ __OBJC_$_CLASS_METHODS_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_$_CLASS_METHODS_CPLEnginePushRepository
+ __OBJC_$_CLASS_METHODS_CPLEngineResourceUploadTask
+ __OBJC_$_CLASS_METHODS_CPLForceSyncTask
+ __OBJC_$_CLASS_METHODS_CPLLibraryParameters
+ __OBJC_$_CLASS_METHODS_CPLLibraryShareScopeChange(CPLNSCoding)
+ __OBJC_$_CLASS_METHODS_CPLPostChange
+ __OBJC_$_CLASS_METHODS_CPLTransportContainerConfiguration
+ __OBJC_$_CLASS_METHODS_CPLUIObservedEvent
+ __OBJC_$_CLASS_METHODS_CPLUIObservedSource
+ __OBJC_$_CLASS_METHODS_CPLUIObserver
+ __OBJC_$_CLASS_METHODS_CPLUIObserverRegistration
+ __OBJC_$_CLASS_METHODS_CPLUIRecordObservedEvent
+ __OBJC_$_CLASS_METHODS_CPLUIRecordObservedSource
+ __OBJC_$_CLASS_METHODS_CPLUIRecordObserver
+ __OBJC_$_CLASS_METHODS_CPLUIRecordObserverRegistration
+ __OBJC_$_CLASS_METHODS_CPLUIRecordStatus
+ __OBJC_$_CLASS_METHODS_CPLUIScopeObservedEvent
+ __OBJC_$_CLASS_METHODS_CPLUIScopeObservedSource
+ __OBJC_$_CLASS_METHODS_CPLUIScopeObserver
+ __OBJC_$_CLASS_METHODS_CPLUIScopeObserverRegistration
+ __OBJC_$_CLASS_METHODS_CPLUIScopeStatus
+ __OBJC_$_CLASS_METHODS_CPLUISyncActivityObservedEvent
+ __OBJC_$_CLASS_METHODS_CPLUISyncActivityObservedSource
+ __OBJC_$_CLASS_METHODS_CPLUISyncActivityObserver
+ __OBJC_$_CLASS_METHODS_CPLUITestObservedEvent
+ __OBJC_$_CLASS_METHODS_CPLUITestObservedSource
+ __OBJC_$_CLASS_METHODS_CPLUITestObserver
+ __OBJC_$_CLASS_PROP_LIST_CPLClientTask
+ __OBJC_$_CLASS_PROP_LIST_CPLCollectionShareScopeChange
+ __OBJC_$_CLASS_PROP_LIST_CPLEngineDefaultStoreWipeHandler
+ __OBJC_$_CLASS_PROP_LIST_CPLEnginePushRepository
+ __OBJC_$_CLASS_PROP_LIST_CPLEngineStoreWipeHandler
+ __OBJC_$_CLASS_PROP_LIST_CPLForceSyncTask
+ __OBJC_$_CLASS_PROP_LIST_CPLLibraryParameters
+ __OBJC_$_CLASS_PROP_LIST_CPLTransportContainerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPLUIObservedEvent
+ __OBJC_$_CLASS_PROP_LIST_CPLUIObservedSource
+ __OBJC_$_CLASS_PROP_LIST_CPLUIObserver
+ __OBJC_$_CLASS_PROP_LIST_CPLUIObserverRegistration
+ __OBJC_$_CLASS_PROP_LIST_CPLUIScopeStatus
+ __OBJC_$_INSTANCE_METHODS_CPLBatterySaverWatcher
+ __OBJC_$_INSTANCE_METHODS_CPLCollectionShareScopeChange
+ __OBJC_$_INSTANCE_METHODS_CPLCommentChange(CPLPushSessionTracker|CPLPlaceholderRecord)
+ __OBJC_$_INSTANCE_METHODS_CPLDefaultBrokenScope
+ __OBJC_$_INSTANCE_METHODS_CPLDirectUploadTask
+ __OBJC_$_INSTANCE_METHODS_CPLEngineDefaultStoreWipeHandler
+ __OBJC_$_INSTANCE_METHODS_CPLEngineForceSyncTask
+ __OBJC_$_INSTANCE_METHODS_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_$_INSTANCE_METHODS_CPLEngineUIObservationCenter(CPLUIScopeObservedSource|CPLUITestObservedSource|CPLUIRecordObservedSource|CPLUISyncActivityObservedSource)
+ __OBJC_$_INSTANCE_METHODS_CPLGenerateDerivativesSubtask
+ __OBJC_$_INSTANCE_METHODS_CPLLibraryParameters
+ __OBJC_$_INSTANCE_METHODS_CPLPartialDerivativesGenerationResult
+ __OBJC_$_INSTANCE_METHODS_CPLPhotosSchemaFilter
+ __OBJC_$_INSTANCE_METHODS_CPLPlistSchemaFilter
+ __OBJC_$_INSTANCE_METHODS_CPLPostChange
+ __OBJC_$_INSTANCE_METHODS_CPLReactChange(CPLIDMapping)
+ __OBJC_$_INSTANCE_METHODS_CPLSchemaFilter
+ __OBJC_$_INSTANCE_METHODS_CPLSyncSession(CPLUISyncActivityObservedSource)
+ __OBJC_$_INSTANCE_METHODS_CPLTextCommentChange(CPLIDMapping)
+ __OBJC_$_INSTANCE_METHODS_CPLTransportContainerConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPLUIObservedEvent
+ __OBJC_$_INSTANCE_METHODS_CPLUIObservedSource
+ __OBJC_$_INSTANCE_METHODS_CPLUIObserver
+ __OBJC_$_INSTANCE_METHODS_CPLUIObserverAndRegistration
+ __OBJC_$_INSTANCE_METHODS_CPLUIObserverManager
+ __OBJC_$_INSTANCE_METHODS_CPLUIObserverRegistration
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordObservedEvent
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordObservedEventAccumulator
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordObservedSource
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordObserver
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordObserverRegistration
+ __OBJC_$_INSTANCE_METHODS_CPLUIRecordStatus
+ __OBJC_$_INSTANCE_METHODS_CPLUIScopeObservedEvent
+ __OBJC_$_INSTANCE_METHODS_CPLUIScopeObservedSource
+ __OBJC_$_INSTANCE_METHODS_CPLUIScopeObserver
+ __OBJC_$_INSTANCE_METHODS_CPLUIScopeObserverRegistration
+ __OBJC_$_INSTANCE_METHODS_CPLUIScopeStatus
+ __OBJC_$_INSTANCE_METHODS_CPLUISyncActivityObservedEvent
+ __OBJC_$_INSTANCE_METHODS_CPLUISyncActivityObservedSource
+ __OBJC_$_INSTANCE_METHODS_CPLUISyncActivityObserver
+ __OBJC_$_INSTANCE_METHODS_CPLUITestObservedEvent
+ __OBJC_$_INSTANCE_METHODS_CPLUITestObservedSource
+ __OBJC_$_INSTANCE_METHODS_CPLUITestObserver
+ __OBJC_$_INSTANCE_METHODS_CPLUIUploadProgressHub
+ __OBJC_$_INSTANCE_METHODS__CPLDirectUploadSubtask
+ __OBJC_$_INSTANCE_METHODS__CPLKeyValueObserver
+ __OBJC_$_INSTANCE_METHODS__CPLUIRecordObserverState
+ __OBJC_$_INSTANCE_METHODS__CPLUIScopeObserverState
+ __OBJC_$_INSTANCE_METHODS__CPLUIUploadProgressItem
+ __OBJC_$_INSTANCE_VARIABLES_CPLBatterySaverWatcher
+ __OBJC_$_INSTANCE_VARIABLES_CPLCollectionShareScopeChange
+ __OBJC_$_INSTANCE_VARIABLES_CPLDefaultBrokenScope
+ __OBJC_$_INSTANCE_VARIABLES_CPLDirectUploadTask
+ __OBJC_$_INSTANCE_VARIABLES_CPLEngineDefaultStoreWipeHandler
+ __OBJC_$_INSTANCE_VARIABLES_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_$_INSTANCE_VARIABLES_CPLEngineUIObservationCenter
+ __OBJC_$_INSTANCE_VARIABLES_CPLGenerateDerivativesSubtask
+ __OBJC_$_INSTANCE_VARIABLES_CPLLibraryParameters
+ __OBJC_$_INSTANCE_VARIABLES_CPLPartialDerivativesGenerationResult
+ __OBJC_$_INSTANCE_VARIABLES_CPLPlistSchemaFilter
+ __OBJC_$_INSTANCE_VARIABLES_CPLPostChange
+ __OBJC_$_INSTANCE_VARIABLES_CPLReactChange
+ __OBJC_$_INSTANCE_VARIABLES_CPLSchemaFilter
+ __OBJC_$_INSTANCE_VARIABLES_CPLTransportContainerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIObservedSource
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIObserver
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIObserverAndRegistration
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIObserverManager
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIObserverRegistration
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordObservedEvent
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordObservedEventAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordObservedSource
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordObserver
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordObserverRegistration
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIRecordStatus
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIScopeObservedEvent
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIScopeObservedSource
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIScopeObserver
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIScopeObserverRegistration
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIScopeStatus
+ __OBJC_$_INSTANCE_VARIABLES_CPLUISyncActivityObservedEvent
+ __OBJC_$_INSTANCE_VARIABLES_CPLUISyncActivityObservedSource
+ __OBJC_$_INSTANCE_VARIABLES_CPLUISyncActivityObserver
+ __OBJC_$_INSTANCE_VARIABLES_CPLUITestObservedEvent
+ __OBJC_$_INSTANCE_VARIABLES_CPLUITestObservedSource
+ __OBJC_$_INSTANCE_VARIABLES_CPLUITestObserver
+ __OBJC_$_INSTANCE_VARIABLES_CPLUIUploadProgressHub
+ __OBJC_$_INSTANCE_VARIABLES__CPLDirectUploadSubtask
+ __OBJC_$_INSTANCE_VARIABLES__CPLKeyValueObserver
+ __OBJC_$_INSTANCE_VARIABLES__CPLUIRecordObserverState
+ __OBJC_$_INSTANCE_VARIABLES__CPLUIScopeObserverState
+ __OBJC_$_INSTANCE_VARIABLES__CPLUIUploadProgressItem
+ __OBJC_$_PROP_LIST_CPLBatterySaverWatcher
+ __OBJC_$_PROP_LIST_CPLCallObserver
+ __OBJC_$_PROP_LIST_CPLClientTask
+ __OBJC_$_PROP_LIST_CPLCollectionShareScopeChange
+ __OBJC_$_PROP_LIST_CPLDefaultBrokenScope
+ __OBJC_$_PROP_LIST_CPLDirectUploadTask
+ __OBJC_$_PROP_LIST_CPLEngineDefaultStoreWipeHandler
+ __OBJC_$_PROP_LIST_CPLEngineForceSyncTask
+ __OBJC_$_PROP_LIST_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_$_PROP_LIST_CPLEngineStoreWipeHandler
+ __OBJC_$_PROP_LIST_CPLGenerateDerivativesSubtask
+ __OBJC_$_PROP_LIST_CPLLibraryParameters
+ __OBJC_$_PROP_LIST_CPLPartialDerivativesGenerationResult
+ __OBJC_$_PROP_LIST_CPLPlistSchemaFilter
+ __OBJC_$_PROP_LIST_CPLPostChange
+ __OBJC_$_PROP_LIST_CPLReactChange
+ __OBJC_$_PROP_LIST_CPLSchemaFilter
+ __OBJC_$_PROP_LIST_CPLSyncActivitySource
+ __OBJC_$_PROP_LIST_CPLTransportContainerConfiguration
+ __OBJC_$_PROP_LIST_CPLUIObservedEvent
+ __OBJC_$_PROP_LIST_CPLUIObservedSource
+ __OBJC_$_PROP_LIST_CPLUIObserver
+ __OBJC_$_PROP_LIST_CPLUIObserverManager
+ __OBJC_$_PROP_LIST_CPLUIObserverRegistration
+ __OBJC_$_PROP_LIST_CPLUIRecordObservedEvent
+ __OBJC_$_PROP_LIST_CPLUIRecordObservedEventAccumulator
+ __OBJC_$_PROP_LIST_CPLUIRecordObserver
+ __OBJC_$_PROP_LIST_CPLUIRecordObserverRegistration
+ __OBJC_$_PROP_LIST_CPLUIRecordStatus
+ __OBJC_$_PROP_LIST_CPLUIScopeObservedEvent
+ __OBJC_$_PROP_LIST_CPLUIScopeObserver
+ __OBJC_$_PROP_LIST_CPLUIScopeObserverRegistration
+ __OBJC_$_PROP_LIST_CPLUIScopeStatus
+ __OBJC_$_PROP_LIST_CPLUISyncActivityObservedEvent
+ __OBJC_$_PROP_LIST_CPLUISyncActivityObservedSource
+ __OBJC_$_PROP_LIST_CPLUITestObservedEvent
+ __OBJC_$_PROP_LIST_CPLUITestObservedSource
+ __OBJC_$_PROTOCOL_CLASS_METHODS_CPLClientTask
+ __OBJC_$_PROTOCOL_CLASS_METHODS_CPLEngineStoreWipeHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLBatterySaverWatcherDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLBrokenScope
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLClientTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLEngineStoreWipeHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLGenerateDerivativesSubtaskDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLLibraryManagerForceSyncDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLSyncActivitySource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLUIGenericObserverManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLUIRecordObservedSourceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLUIScopeObservedSourceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLUISyncActivityObservedSourceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLBatterySaverWatcherDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLBrokenScope
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLClientTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLEngineStoreWipeHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLGenerateDerivativesSubtaskDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLLibraryManagerForceSyncDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLSyncActivitySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLUIGenericObserverManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLUIRecordObservedSourceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLUIScopeObservedSourceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLUISyncActivityObservedSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLBatterySaverWatcherDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLBrokenScope
+ __OBJC_$_PROTOCOL_REFS_CPLClientTask
+ __OBJC_$_PROTOCOL_REFS_CPLEngineStoreWipeHandler
+ __OBJC_$_PROTOCOL_REFS_CPLGenerateDerivativesSubtaskDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLLibraryManagerForceSyncDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLSyncActivitySource
+ __OBJC_$_PROTOCOL_REFS_CPLUIGenericObserverManager
+ __OBJC_$_PROTOCOL_REFS_CPLUIObservedSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLUIRecordObservedSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLUIScopeObservedSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLUISyncActivityObservedSourceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPLDefaultBrokenScope
+ __OBJC_CLASS_PROTOCOLS_$_CPLDirectUploadTask
+ __OBJC_CLASS_PROTOCOLS_$_CPLEngineDefaultStoreWipeHandler
+ __OBJC_CLASS_PROTOCOLS_$_CPLEngineForceSyncTask
+ __OBJC_CLASS_PROTOCOLS_$_CPLEngineUIObservationCenter(CPLUIScopeObservedSource|CPLUITestObservedSource|CPLUIRecordObservedSource|CPLUISyncActivityObservedSource)
+ __OBJC_CLASS_PROTOCOLS_$_CPLForceSyncTask
+ __OBJC_CLASS_PROTOCOLS_$_CPLLibraryParameters
+ __OBJC_CLASS_PROTOCOLS_$_CPLLibraryShareScopeChange(CPLNSCoding)
+ __OBJC_CLASS_PROTOCOLS_$_CPLSyncSession(CPLUISyncActivityObservedSource)
+ __OBJC_CLASS_PROTOCOLS_$_CPLTransportContainerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CPLUIObservedEvent
+ __OBJC_CLASS_PROTOCOLS_$_CPLUIObserverManager
+ __OBJC_CLASS_PROTOCOLS_$_CPLUIObserverRegistration
+ __OBJC_CLASS_PROTOCOLS_$_CPLUIScopeStatus
+ __OBJC_CLASS_RO_$_CPLBatterySaverWatcher
+ __OBJC_CLASS_RO_$_CPLDefaultBrokenScope
+ __OBJC_CLASS_RO_$_CPLDirectUploadTask
+ __OBJC_CLASS_RO_$_CPLEngineDefaultStoreWipeHandler
+ __OBJC_CLASS_RO_$_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_CLASS_RO_$_CPLEngineUIObservationCenter
+ __OBJC_CLASS_RO_$_CPLGenerateDerivativesSubtask
+ __OBJC_CLASS_RO_$_CPLLibraryParameters
+ __OBJC_CLASS_RO_$_CPLPartialDerivativesGenerationResult
+ __OBJC_CLASS_RO_$_CPLPhotosSchemaFilter
+ __OBJC_CLASS_RO_$_CPLPlistSchemaFilter
+ __OBJC_CLASS_RO_$_CPLPostChange
+ __OBJC_CLASS_RO_$_CPLSchemaFilter
+ __OBJC_CLASS_RO_$_CPLTransportContainerConfiguration
+ __OBJC_CLASS_RO_$_CPLUIObservedEvent
+ __OBJC_CLASS_RO_$_CPLUIObservedSource
+ __OBJC_CLASS_RO_$_CPLUIObserver
+ __OBJC_CLASS_RO_$_CPLUIObserverAndRegistration
+ __OBJC_CLASS_RO_$_CPLUIObserverManager
+ __OBJC_CLASS_RO_$_CPLUIObserverRegistration
+ __OBJC_CLASS_RO_$_CPLUIRecordObservedEvent
+ __OBJC_CLASS_RO_$_CPLUIRecordObservedEventAccumulator
+ __OBJC_CLASS_RO_$_CPLUIRecordObservedSource
+ __OBJC_CLASS_RO_$_CPLUIRecordObserver
+ __OBJC_CLASS_RO_$_CPLUIRecordObserverRegistration
+ __OBJC_CLASS_RO_$_CPLUIRecordStatus
+ __OBJC_CLASS_RO_$_CPLUIScopeObservedEvent
+ __OBJC_CLASS_RO_$_CPLUIScopeObservedSource
+ __OBJC_CLASS_RO_$_CPLUIScopeObserver
+ __OBJC_CLASS_RO_$_CPLUIScopeObserverRegistration
+ __OBJC_CLASS_RO_$_CPLUIScopeStatus
+ __OBJC_CLASS_RO_$_CPLUISyncActivityObservedEvent
+ __OBJC_CLASS_RO_$_CPLUISyncActivityObservedSource
+ __OBJC_CLASS_RO_$_CPLUISyncActivityObserver
+ __OBJC_CLASS_RO_$_CPLUITestObservedEvent
+ __OBJC_CLASS_RO_$_CPLUITestObservedSource
+ __OBJC_CLASS_RO_$_CPLUITestObserver
+ __OBJC_CLASS_RO_$_CPLUIUploadProgressHub
+ __OBJC_CLASS_RO_$__CPLDirectUploadSubtask
+ __OBJC_CLASS_RO_$__CPLKeyValueObserver
+ __OBJC_CLASS_RO_$__CPLUIRecordObserverState
+ __OBJC_CLASS_RO_$__CPLUIScopeObserverState
+ __OBJC_CLASS_RO_$__CPLUIUploadProgressItem
+ __OBJC_LABEL_PROTOCOL_$_CPLBatterySaverWatcherDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLBrokenScope
+ __OBJC_LABEL_PROTOCOL_$_CPLClientTask
+ __OBJC_LABEL_PROTOCOL_$_CPLEngineStoreWipeHandler
+ __OBJC_LABEL_PROTOCOL_$_CPLGenerateDerivativesSubtaskDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLLibraryManagerForceSyncDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLSyncActivitySource
+ __OBJC_LABEL_PROTOCOL_$_CPLUIGenericObserverManager
+ __OBJC_LABEL_PROTOCOL_$_CPLUIObservedSourceDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLUIRecordObservedSourceDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLUIScopeObservedSourceDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLUISyncActivityObservedSourceDelegate
+ __OBJC_METACLASS_RO_$_CPLBatterySaverWatcher
+ __OBJC_METACLASS_RO_$_CPLDefaultBrokenScope
+ __OBJC_METACLASS_RO_$_CPLDirectUploadTask
+ __OBJC_METACLASS_RO_$_CPLEngineDefaultStoreWipeHandler
+ __OBJC_METACLASS_RO_$_CPLEngineForceSyncWithPushFromClientTask
+ __OBJC_METACLASS_RO_$_CPLEngineUIObservationCenter
+ __OBJC_METACLASS_RO_$_CPLGenerateDerivativesSubtask
+ __OBJC_METACLASS_RO_$_CPLLibraryParameters
+ __OBJC_METACLASS_RO_$_CPLPartialDerivativesGenerationResult
+ __OBJC_METACLASS_RO_$_CPLPhotosSchemaFilter
+ __OBJC_METACLASS_RO_$_CPLPlistSchemaFilter
+ __OBJC_METACLASS_RO_$_CPLPostChange
+ __OBJC_METACLASS_RO_$_CPLSchemaFilter
+ __OBJC_METACLASS_RO_$_CPLTransportContainerConfiguration
+ __OBJC_METACLASS_RO_$_CPLUIObservedEvent
+ __OBJC_METACLASS_RO_$_CPLUIObservedSource
+ __OBJC_METACLASS_RO_$_CPLUIObserver
+ __OBJC_METACLASS_RO_$_CPLUIObserverAndRegistration
+ __OBJC_METACLASS_RO_$_CPLUIObserverManager
+ __OBJC_METACLASS_RO_$_CPLUIObserverRegistration
+ __OBJC_METACLASS_RO_$_CPLUIRecordObservedEvent
+ __OBJC_METACLASS_RO_$_CPLUIRecordObservedEventAccumulator
+ __OBJC_METACLASS_RO_$_CPLUIRecordObservedSource
+ __OBJC_METACLASS_RO_$_CPLUIRecordObserver
+ __OBJC_METACLASS_RO_$_CPLUIRecordObserverRegistration
+ __OBJC_METACLASS_RO_$_CPLUIRecordStatus
+ __OBJC_METACLASS_RO_$_CPLUIScopeObservedEvent
+ __OBJC_METACLASS_RO_$_CPLUIScopeObservedSource
+ __OBJC_METACLASS_RO_$_CPLUIScopeObserver
+ __OBJC_METACLASS_RO_$_CPLUIScopeObserverRegistration
+ __OBJC_METACLASS_RO_$_CPLUIScopeStatus
+ __OBJC_METACLASS_RO_$_CPLUISyncActivityObservedEvent
+ __OBJC_METACLASS_RO_$_CPLUISyncActivityObservedSource
+ __OBJC_METACLASS_RO_$_CPLUISyncActivityObserver
+ __OBJC_METACLASS_RO_$_CPLUITestObservedEvent
+ __OBJC_METACLASS_RO_$_CPLUITestObservedSource
+ __OBJC_METACLASS_RO_$_CPLUITestObserver
+ __OBJC_METACLASS_RO_$_CPLUIUploadProgressHub
+ __OBJC_METACLASS_RO_$__CPLDirectUploadSubtask
+ __OBJC_METACLASS_RO_$__CPLKeyValueObserver
+ __OBJC_METACLASS_RO_$__CPLUIRecordObserverState
+ __OBJC_METACLASS_RO_$__CPLUIScopeObserverState
+ __OBJC_METACLASS_RO_$__CPLUIUploadProgressItem
+ __OBJC_PROTOCOL_$_CPLBatterySaverWatcherDelegate
+ __OBJC_PROTOCOL_$_CPLBrokenScope
+ __OBJC_PROTOCOL_$_CPLClientTask
+ __OBJC_PROTOCOL_$_CPLEngineStoreWipeHandler
+ __OBJC_PROTOCOL_$_CPLGenerateDerivativesSubtaskDelegate
+ __OBJC_PROTOCOL_$_CPLLibraryManagerForceSyncDelegate
+ __OBJC_PROTOCOL_$_CPLSyncActivitySource
+ __OBJC_PROTOCOL_$_CPLUIGenericObserverManager
+ __OBJC_PROTOCOL_$_CPLUIObservedSourceDelegate
+ __OBJC_PROTOCOL_$_CPLUIRecordObservedSourceDelegate
+ __OBJC_PROTOCOL_$_CPLUIScopeObservedSourceDelegate
+ __OBJC_PROTOCOL_$_CPLUISyncActivityObservedSourceDelegate
+ ___100-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:uiUploadProgressHub:withError:]_block_invoke
+ ___100-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:uiUploadProgressHub:withError:]_block_invoke.35
+ ___100-[CPLUploadPushedChangesTask generateDerivativesSubtask:derivativesGenerationForChange:didProgress:]_block_invoke
+ ___103-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) notifySyncActivityIsBlocked:forSource:]_block_invoke
+ ___103-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke
+ ___103-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke.386
+ ___103-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke_2
+ ___103-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke_2.cold.1
+ ___103-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke_3
+ ___105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.403
+ ___106-[CPLUploadPushedChangesTask generateDerivativesSubtask:didProgressGeneratingDerivativesFromResourceSize:]_block_invoke
+ ___106-[CPLUploadPushedChangesTask generateDerivativesSubtask:didProgressGeneratingDerivativesFromResourceSize:]_block_invoke_2
+ ___108-[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusForScopesWithIdentifiersHaveChanged:]_block_invoke
+ ___109-[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusScopeWithIdentifiers:isSynchronizing:]_block_invoke
+ ___110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.315
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.81
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.85
+ ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.86
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.61
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.65
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.76
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.70
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.77
+ ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_3.78
+ ___114-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) notifyProgress:forScopeWithIdentifier:fromSource:]_block_invoke
+ ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.59
+ ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.62
+ ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.64
+ ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke_2.60
+ ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke_2.63
+ ___115-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopSyncActivityForScopeWithIdentifier:fromSource:]_block_invoke
+ ___115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.408
+ ___115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.357
+ ___116-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startSyncActivityForScopeWithIdentifier:fromSource:]_block_invoke
+ ___118-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForAllRecordsWithScopeIdentifiersHaveChanged:]_block_invoke
+ ___120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.321
+ ___121-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:]_block_invoke
+ ___121-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUploadProgressForRecordsWithLocalScopedIdentifiers:step:]_block_invoke
+ ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.505
+ ___124-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyRecordsWithLocalScopedIdentifiersHaveStartedUploading:step:]_block_invoke
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.408
+ ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.409
+ ___129-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) recordObservedSource:computeStatusesWithAccumulator:completionHandler:]_block_invoke
+ ___129-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) recordObservedSource:computeStatusesWithAccumulator:completionHandler:]_block_invoke.65
+ ___129-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) recordObservedSource:computeStatusesWithAccumulator:completionHandler:]_block_invoke_2
+ ___136-[CPLScopeUpdateScopeTask _updateScopeWithNewScopeType:updatedScopeChange:updatedFlags:oldTransportScope:session:updatedTransportScope:]_block_invoke.55
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.198
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.205
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.207
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.208
+ ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.210
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.237
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.239
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.238
+ ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.240
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.227
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.229
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.232
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.233
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.235
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.234
+ ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.236
+ ___166-[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) scopeObservedSource:getStatusesForScopesWithIdentifiers:synchronizingScopeWithIdentifiers:completionHandler:]_block_invoke
+ ___29-[CPLUIObserver forceRefresh]_block_invoke
+ ___29-[CPLUIObserver forceRefresh]_block_invoke_2
+ ___30-[CPLEngineLibrary parameters]_block_invoke
+ ___30-[CPLForceSyncTask cancelTask]_block_invoke
+ ___30-[CPLProxyLibraryManager ping]_block_invoke
+ ___30-[CPLProxyLibraryManager ping]_block_invoke.370
+ ___30-[CPLProxyLibraryManager ping]_block_invoke.cold.1
+ ___30-[CPLUIObserver stopObserving]_block_invoke
+ ___31-[CPLForceSyncTask isCancelled]_block_invoke
+ ___31-[CPLLibraryManager parameters]_block_invoke
+ ___31-[CPLUIObserverManager dealloc]_block_invoke
+ ___31-[CPLUIScopeStatus description]_block_invoke
+ ___32-[CPLUIObserverManager tearDown]_block_invoke
+ ___32-[CPLUIObserverManager tearDown]_block_invoke_2
+ ___33-[CPLDirectUploadTask cancelTask]_block_invoke
+ ___33-[CPLLibraryInfo totalAssetCount]_block_invoke
+ ___33-[CPLStatus accountPartitionType]_block_invoke
+ ___33-[CPLStatus resetMainScopeStatus]_block_invoke
+ ___33-[CPLUIObserver _withDelegateDo:]_block_invoke
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke.12
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke.15
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke_2
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke_2.16
+ ___33-[CPLUIObserverManager _autoOpen]_block_invoke_3
+ ___34-[CPLDirectUploadTask isCancelled]_block_invoke
+ ___36-[CPLEngineLibrary startSyncSession]_block_invoke.53
+ ___36-[CPLEngineLibrary startSyncSession]_block_invoke.54
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.56
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.61
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke.81
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.62
+ ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.71
+ ___36-[CPLUIObserver _updateRegistration]_block_invoke
+ ___36-[CPLUIObserver _updateRegistration]_block_invoke_2
+ ___36-[CPLUIObserverManager forceRefresh]_block_invoke
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.144
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.145
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.146
+ ___37-[CPLStatus setAccountPartitionType:]_block_invoke
+ ___37-[CPLSyncSession backgroundScheduler]_block_invoke
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke.14
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke.20
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke.23
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_2.15
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_2.21
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_2.24
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_3.22
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_3.25
+ ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_4.26
+ ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.176
+ ___38-[CPLDirectUploadTask _launchSubtask:]_block_invoke
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.95
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.97
+ ___39-[CPLBatterySaverWatcher startWatching]_block_invoke
+ ___39-[CPLEngineForceSyncTask _reallyCancel]_block_invoke
+ ___39-[CPLEngineForceSyncTask _reallyLaunch]_block_invoke
+ ___39-[CPLGenerateDerivativesSubtask cancel]_block_invoke
+ ___39-[CPLGenerateDerivativesSubtask launch]_block_invoke
+ ___39-[CPLLibraryManager _updateParameters:]_block_invoke
+ ___39-[CPLUIObserver observedEventDidChange]_block_invoke
+ ___39-[CPLUIObserver observedEventDidChange]_block_invoke.39
+ ___39-[CPLUIObserver observedEventDidChange]_block_invoke_2
+ ___40-[CPLDirectUploadTask _didFinishSubtask]_block_invoke
+ ___40-[CPLDirectUploadTask _phaseDescription]_block_invoke
+ ___40-[CPLEngineScheduler shouldUseTurboMode]_block_invoke
+ ___40-[CPLPlistSchemaFilter _loadIfNecessary]_block_invoke
+ ___40-[CPLPlistSchemaFilter _loadIfNecessary]_block_invoke.71
+ ___41+[CPLFingerprintContext sharedEPPContext]_block_invoke
+ ___41-[CPLEngineLibrary updateLibraryOptions:]_block_invoke
+ ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.154
+ ___41-[CPLEngineScheduler setCanUseTurboMode:]_block_invoke
+ ___41-[CPLSyncSession setBackgroundScheduler:]_block_invoke
+ ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.81
+ ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.82
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.162
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.163
+ ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.164
+ ___42-[CPLLibraryManager discardCurrentSession]_block_invoke.280
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.295
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.296
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.302
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.303
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.304
+ ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke_3
+ ___42-[CPLScopeUpdateScopeTask _getLibraryInfo]_block_invoke.66
+ ___42-[CPLSyncSession hasBeenJustInCaseSession]_block_invoke
+ ___43-[CPLRecordChange propertiesForChangeType:]_block_invoke.162
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.260
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.282
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.286
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.294
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.296
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.301
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke_2.297
+ ___44-[CPLEngineSystemMonitor isNetworkExpensive]_block_invoke
+ ___44-[CPLUIObserver _scheduleRegistrationUpdate]_block_invoke
+ ___44-[CPLUIObserver observedSourceDidDisconnect]_block_invoke
+ ___44-[CPLUIObserver startObservingWithDelegate:]_block_invoke
+ ___45+[CPLFingerprintContext setSharedEPPContext:]_block_invoke
+ ___45-[CPLDirectUploadTask cancelFromSyncManager:]_block_invoke
+ ___45-[CPLDirectUploadTask launchFromSyncManager:]_block_invoke
+ ___45-[CPLDirectUploadTask launchFromSyncManager:]_block_invoke.51
+ ___45-[CPLDirectUploadTask launchFromSyncManager:]_block_invoke_2
+ ___45-[CPLEngineScheduler _updateTurboModeOnQueue]_block_invoke
+ ___45-[CPLFingerprintContext forceMMCSv2AsDefault]_block_invoke
+ ___45-[CPLUIScopeStatus setAssetCountPerTypeData:]_block_invoke
+ ___46-[CPLEngineLibrary _engineDidUpdateParameters]_block_invoke
+ ___46-[CPLUIScopeObserver didRefreshObservedEvent:]_block_invoke
+ ___47-[CPLBeforeUploadCheckItems itemWillBeDropped:]_block_invoke
+ ___47-[CPLDirectUploadTask _checkRecordsIfNecessary]_block_invoke
+ ___47-[CPLDirectUploadTask _didFinishTaskWithError:]_block_invoke
+ ___47-[CPLDirectUploadTask _didFinishTaskWithError:]_block_invoke.18
+ ___47-[CPLDirectUploadTask _didFinishTaskWithError:]_block_invoke_2
+ ___47-[CPLDirectUploadTask _didFinishTaskWithError:]_block_invoke_3
+ ___47-[CPLDirectUploadTask _didFinishTaskWithError:]_block_invoke_4
+ ___47-[CPLEngineSystemMonitor hasGoodQualityNetwork]_block_invoke
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.176
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.177
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.185
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke_2
+ ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke_3
+ ___47-[CPLUIRecordObserver didRefreshObservedEvent:]_block_invoke
+ ___47-[CPLUIRecordObserver didRefreshObservedEvent:]_block_invoke_2
+ ___47-[CPLUIRecordObserver didRefreshObservedEvent:]_block_invoke_3
+ ___47-[CPLUIRecordObserver didRefreshObservedEvent:]_block_invoke_4
+ ___47-[NSObject(CPLCodingProxy) cplClearProperties:]_block_invoke.131
+ ___48+[CPLLibraryParameters mappingForLibraryOptions]_block_invoke
+ ___48-[CPLEngineScheduler openWithCompletionHandler:]_block_invoke_3
+ ___49+[CPLLibraryManager mappingForFeatureDataclasses]_block_invoke
+ ___49-[CPLEngineLibrary updateContainerConfiguration:]_block_invoke
+ ___49-[CPLEngineStore getStatusWithCompletionHandler:]_block_invoke_4
+ ___49-[CPLEngineStore updateFeatureDataclasses:error:]_block_invoke
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.321
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.324
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.325
+ ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.328
+ ___49-[CPLUIScopeStatus _deserializeAssetCountPerType]_block_invoke
+ ___49-[CPLUIScopeStatus _deserializeAssetCountPerType]_block_invoke_2
+ ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1795
+ ___50-[CPLEngineScheduler _turboModeSettingsHasChanged]_block_invoke
+ ___50-[CPLSyncSession shouldBypassBackgroundScheduling]_block_invoke
+ ___51-[CPLEngineComponentEnumerator handleNextComponent]_block_invoke
+ ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.361
+ ___51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.334
+ ___51-[CPLProxyLibraryManager _dropConnectionCompletely]_block_invoke
+ ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.74
+ ___51-[CPLSyncSession needsToAcquireBackgroundScheduler]_block_invoke
+ ___51-[CPLUIObservedSource enumerateObserversWithBlock:]_block_invoke
+ ___51-[CPLUIRecordObservedSource sourceStatusDictionary]_block_invoke
+ ___52-[CPLBatterySaverWatcher _batterySaverModeTriggered]_block_invoke
+ ___52-[CPLEngineDerivativesCache subCacheWithIdentifier:]_block_invoke
+ ___52-[CPLEngineSyncManager _launchForcedTaskIfNecessary]_block_invoke.276
+ ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke.233
+ ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke_2.236
+ ___52-[CPLEngineSystemMonitor openWithCompletionHandler:]_block_invoke_3
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.336
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.338
+ ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.339
+ ___52-[CPLUIObserver stopObservingWithCompletionHandler:]_block_invoke
+ ___52-[CPLUIObserver stopObservingWithCompletionHandler:]_block_invoke_2
+ ___52-[CPLUIObserver stopObservingWithCompletionHandler:]_block_invoke_3
+ ___53+[CPLLibraryParameters descriptionForLibraryOptions:]_block_invoke
+ ___53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.340
+ ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.95
+ ___53-[CPLUIObservedSource _scheduleObserverNotifications]_block_invoke
+ ___53-[CPLUIScopeObserver didDisconnectFromObservedSource]_block_invoke
+ ___53-[CPLUIScopeObserver didDisconnectFromObservedSource]_block_invoke_2
+ ___54+[CPLCollectionShareScopeChange mappingForViewingMode]_block_invoke
+ ___54+[CPLLibraryManager descriptionForFeatureDataclasses:]_block_invoke
+ ___54-[CPLEngineForceSyncWithPushFromClientTask cancelTask]_block_invoke
+ ___54-[CPLEngineForceSyncWithPushFromClientTask launchTask]_block_invoke
+ ___54-[CPLEngineForceSyncWithPushFromClientTask launchTask]_block_invoke_2
+ ___54-[CPLEngineForceSyncWithPushFromClientTask launchTask]_block_invoke_3
+ ___54-[CPLEngineForceSyncWithPushFromClientTask launchTask]_block_invoke_4
+ ___54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.490
+ ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_2.46
+ ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_3.47
+ ___55+[CPLLibraryParameters reverseMappingForLibraryOptions]_block_invoke
+ ___55+[CPLLibraryParameters reverseMappingForLibraryOptions]_block_invoke_2
+ ___55+[CPLTransportContainerConfiguration mappingForOptions]_block_invoke
+ ___55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.68
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.160
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.163
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.164
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.161
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.165
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_3.166
+ ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.34
+ ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.37
+ ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.45
+ ___55-[CPLSyncSessionPredictor removePredictedValueForType:]_block_invoke.62
+ ___55-[CPLUIObservedSource _reallyFireObserverNotifications]_block_invoke
+ ___55-[CPLUIObserverManager forceSyncScopesWithIdentifiers:]_block_invoke
+ ___55-[CPLUIObserverManager forceSyncScopesWithIdentifiers:]_block_invoke_2
+ ___55-[CPLUIObserverManager forceSyncScopesWithIdentifiers:]_block_invoke_3
+ ___55-[CPLUIObserverManager forceSyncScopesWithIdentifiers:]_block_invoke_4
+ ___55-[CPLUIObserverManager forceSyncScopesWithIdentifiers:]_block_invoke_5
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.152
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.159
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.161
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.162
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.163
+ ___56+[CPLCollectionShareScopeChange mappingForExpiringState]_block_invoke
+ ___56+[CPLResource _resourceTypesThatCountAgainstiCloudQuota]_block_invoke
+ ___56+[CPLResource _resourceTypesThatCountAgainstiCloudQuota]_block_invoke_2
+ ___56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.341
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.287
+ ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.289
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.115
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.116
+ ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.143
+ ___56-[CPLUIObserverManager initWithLibraryIdentifier:queue:]_block_invoke
+ ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke.59
+ ___56-[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]_block_invoke.11
+ ___57+[CPLCollectionShareScopeChange mappingForMigrationState]_block_invoke
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.106
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.114
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.120
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.126
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.132
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.138
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.145
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.150
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.156
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.162
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.168
+ ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.174
+ ___57-[CPLEngineSyncManager setSyncSessionShouldBeForeground:]_block_invoke.246
+ ___57-[CPLEngineSystemMonitor getStatusWithCompletionHandler:]_block_invoke_4
+ ___57-[CPLUIRecordObservedSource notifyRecordsUploadDidFinish]_block_invoke
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.42
+ ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.47
+ ___57-[CPLUploadPushedChangesTask _uploadBatchWithFetchCache:]_block_invoke.119
+ ___58-[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]_block_invoke.46
+ ___58-[CPLEngineSystemMonitor _permanentDataOverrideHasChanged]_block_invoke.204
+ ___58-[CPLEngineUIObservationCenter openWithCompletionHandler:]_block_invoke
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.190
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.191
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.192
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.193
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_4
+ ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_5
+ ___58-[CPLLibraryManager declineSharedScope:completionHandler:]_block_invoke
+ ___58-[CPLLibraryManager declineSharedScope:completionHandler:]_block_invoke.429
+ ___58-[CPLLibraryManager declineSharedScope:completionHandler:]_block_invoke_2
+ ___58-[CPLLibraryManager unregisterObserver:completionHandler:]_block_invoke
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.341
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.342
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.344
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.343
+ ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.345
+ ___58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.377
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.28
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.31
+ ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke_2.29
+ ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.97
+ ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.98
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke.157
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke_27
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke_28
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke_29
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke_30
+ ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke_31
+ ___59-[CPLEngineStore getStatusDictionaryWithCompletionHandler:]_block_invoke_2
+ ___59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.339
+ ___59-[CPLProxyLibraryManager _reallyOpenWithCompletionHandler:]_block_invoke.312
+ ___59-[CPLProxyLibraryManager _reallyOpenWithCompletionHandler:]_block_invoke_2.313
+ ___59-[CPLProxyLibraryManager _reallyOpenWithCompletionHandler:]_block_invoke_4
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.109
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.111
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.110
+ ___60+[CPLTransportContainerConfiguration descriptionForOptions:]_block_invoke
+ ___60-[CPLEngineDerivativesCache _discardSubCacheWithIdentifier:]_block_invoke
+ ___60-[CPLEngineForceSyncWithPushFromClientTask didStartSubTask:]_block_invoke
+ ___60-[CPLGenerateDerivativesSubtask _acquireActivityIfNecessary]_block_invoke
+ ___60-[CPLGenerateDerivativesSubtask _acquireActivityIfNecessary]_block_invoke_2
+ ___60-[CPLGenerateDerivativesSubtask _acquireActivityIfNecessary]_block_invoke_3
+ ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.183
+ ___61-[CPLEngineForceSyncWithPushFromClientTask didFinishSubTask:]_block_invoke
+ ___61-[CPLEngineStore storeLastSuccessfulSyncDateFromSyncSession:]_block_invoke
+ ___61-[CPLEngineStore storeLastSuccessfulSyncDateFromSyncSession:]_block_invoke_2
+ ___61-[CPLEngineStore storeLastSuccessfulSyncDateFromSyncSession:]_block_invoke_3
+ ___61-[CPLLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke
+ ___61-[CPLLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___61-[CPLLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke.88
+ ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke_2.89
+ ___61-[CPLSyncSession stopBypassingBackgroundSchedulingIfPossible]_block_invoke
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.25
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.33
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.53
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.55
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke_2.34
+ ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke_2.56
+ ___62+[CPLTransportContainerConfiguration reverseMappingForOptions]_block_invoke
+ ___62+[CPLTransportContainerConfiguration reverseMappingForOptions]_block_invoke_2
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.123
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.131
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.132
+ ___62-[CPLSyncSession startBypassingBackgroundSchedulingIfPossible]_block_invoke
+ ___62-[CPLSyncSessionPredictor updatePredictionWithValuesAndTypes:]_block_invoke.59
+ ___62-[CPLUIObserver startObservingWithDelegate:completionHandler:]_block_invoke
+ ___62-[CPLUIObserver startObservingWithDelegate:completionHandler:]_block_invoke_2
+ ___62-[_CPLDirectUploadSubtask initWithGenerateDerivativesSubtask:]_block_invoke
+ ___62-[_CPLDirectUploadSubtask initWithGenerateDerivativesSubtask:]_block_invoke_2
+ ___63-[CPLDirectUploadTask _uploadRecordsIfNecessaryWithFetchCache:]_block_invoke
+ ___63-[CPLDirectUploadTask _uploadRecordsIfNecessaryWithFetchCache:]_block_invoke_2
+ ___63-[CPLDirectUploadTask _uploadRecordsIfNecessaryWithFetchCache:]_block_invoke_3
+ ___63-[CPLEngineUIObservationCenter getStatusWithCompletionHandler:]_block_invoke
+ ___63-[CPLEngineUIObservationCenter withObservedSourceOfType:block:]_block_invoke
+ ___63-[CPLProxyLibraryManager declineSharedScope:completionHandler:]_block_invoke
+ ___63-[CPLProxyLibraryManager declineSharedScope:completionHandler:]_block_invoke_2
+ ___63-[CPLProxyLibraryManager declineSharedScope:completionHandler:]_block_invoke_3
+ ___63-[CPLProxyLibraryManager declineSharedScope:completionHandler:]_block_invoke_4
+ ___63-[CPLProxyLibraryManager declineSharedScope:completionHandler:]_block_invoke_5
+ ___63-[CPLProxyLibraryManager unregisterObserver:completionHandler:]_block_invoke
+ ___63-[CPLProxyLibraryManager unregisterObserver:completionHandler:]_block_invoke.cold.1
+ ___63-[CPLProxyLibraryManager unregisterObserver:completionHandler:]_block_invoke_2
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke.68
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke_2
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke_2.69
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke_3
+ ___63-[CPLScopeUpdateScopeTask _fetchTransportScopeWithActiveScope:]_block_invoke_3.70
+ ___63-[CPLUIObserver _dispatchObservedEventToDelegate:registration:]_block_invoke
+ ___64-[CPLCallObserver initWithObject:selector:functionName:timeout:]_block_invoke
+ ___64-[CPLEngineQuarantinedRecords _quarantineRejectedRecords:error:]_block_invoke.41
+ ___64-[CPLEngineQuarantinedRecords _quarantineRejectedRecords:error:]_block_invoke.46
+ ___64-[CPLEngineUIObservationCenter _withObservedSourceOfType:block:]_block_invoke
+ ___64-[CPLLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke
+ ___64-[CPLLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___64-[CPLLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___65-[CPLLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke
+ ___65-[CPLLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___65-[CPLLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.416
+ ___65-[CPLUIScopeObservedSource notifyUIStatusForAllScopesHaveChanged]_block_invoke
+ ___66-[CPLEngineLibrary(CPLManagement) getStatusWithCompletionHandler:]_block_invoke
+ ___66-[CPLEngineLibrary(CPLManagement) getStatusWithCompletionHandler:]_block_invoke_2
+ ___66-[CPLEngineLibrary(CPLManagement) getStatusWithCompletionHandler:]_block_invoke_3
+ ___66-[CPLEngineLibrary(CPLManagement) getStatusWithCompletionHandler:]_block_invoke_4
+ ___66-[CPLLibraryManager clearAllPermanentErrorsWithCompletionHandler:]_block_invoke
+ ___66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.357
+ ___66-[CPLProxyLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke
+ ___66-[CPLProxyLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___66-[CPLProxyLibraryManager setFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___66-[CPLUIRecordObservedEventAccumulator updateWithUploadProgresses:]_block_invoke
+ ___66-[_CPLDirectUploadSubtask initWithTransportTask:phaseDescription:]_block_invoke
+ ___66-[_CPLDirectUploadSubtask initWithTransportTask:phaseDescription:]_block_invoke_2
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.195
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.198
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.196
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.199
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.197
+ ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.200
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.137
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.138
+ ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.139
+ ___67-[CPLEngineStore wipeStoreAtNextOpeningWithReason:completionBlock:]_block_invoke
+ ___67-[CPLEngineSystemMonitor getStatusDictionaryWithCompletionHandler:]_block_invoke.132
+ ___67-[CPLEngineSystemMonitor getStatusDictionaryWithCompletionHandler:]_block_invoke.146
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_2
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_3
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_4
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_5
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_6
+ ___67-[CPLGenerateDerivativesSubtask _generateDerivativesForNextRecord:]_block_invoke_7
+ ___67-[CPLLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke
+ ___67-[CPLLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke.425
+ ___67-[CPLLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke_2
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.108
+ ___67-[CPLUIRecordObservedSource notifyUIStatusForAllRecordsHaveChanged]_block_invoke
+ ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.122
+ ___68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.421
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.101
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.94
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.99
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_2.102
+ ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_3.103
+ ___69-[CPLEngineUIObservationCenter closeAndDeactivate:completionHandler:]_block_invoke
+ ___69-[CPLEngineUIObservationCenter unregisterObserver:completionHandler:]_block_invoke
+ ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.51
+ ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.60
+ ___69-[CPLProxyLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke
+ ___69-[CPLProxyLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___69-[CPLProxyLibraryManager enableFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___69-[CPLSchemaFilter transportFilterForTransportIdentifier:constructor:]_block_invoke
+ ___70-[CPLLibraryManager updateRegistration:forObserver:completionHandler:]_block_invoke
+ ___70-[CPLProxyLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke
+ ___70-[CPLProxyLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke_2
+ ___70-[CPLProxyLibraryManager disableFeatureDataclasses:completionHandler:]_block_invoke_3
+ ___70-[CPLScopeUpdateScopeTask _markScopeAsDeletedAndSucceedTaskWithFlags:]_block_invoke.40
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.108
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.109
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.115
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.119
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.116
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.120
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.117
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.121
+ ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_4.118
+ ___71-[CPLLibraryManager refreshObservedEventForObserver:completionHandler:]_block_invoke
+ ___71-[CPLProxyLibraryManager clearAllPermanentErrorsWithCompletionHandler:]_block_invoke
+ ___71-[CPLProxyLibraryManager clearAllPermanentErrorsWithCompletionHandler:]_block_invoke_2
+ ___71-[CPLProxyLibraryManager clearAllPermanentErrorsWithCompletionHandler:]_block_invoke_2.cold.1
+ ___71-[CPLProxyLibraryManager clearAllPermanentErrorsWithCompletionHandler:]_block_invoke_3
+ ___72+[CPLAssetChange(DefaultsSupport) serverSupportsProxyConflictResolution]_block_invoke
+ ___72+[CPLScopedIdentifier mappingForScopeIdentifierPrefixToFeatureDataclass]_block_invoke
+ ___72+[CPLScopedIdentifier mappingForScopeIdentifierPrefixToFeatureDataclass]_block_invoke_2
+ ___72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.353
+ ___72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.494
+ ___72-[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke
+ ___72-[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke_2
+ ___72-[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke_3
+ ___72-[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke_4
+ ___72-[CPLProxyLibraryManager acceptShareFromFetchedScope:completionHandler:]_block_invoke_5
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke.56
+ ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_2.58
+ ___73-[CPLEngineUIObservationCenter getStatusDictionaryWithCompletionHandler:]_block_invoke
+ ___73-[CPLLibraryManager registerObserver:withRegistration:completionHandler:]_block_invoke
+ ___73-[CPLUIObserverManager libraryManager:didFinishForceSyncTask:withErrors:]_block_invoke
+ ___74+[CPLTransportContainerConfiguration configurationForTestManateeContainer]_block_invoke
+ ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.126
+ ___74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.433
+ ___74-[CPLUIObserverManager _receivedLibraryMightBeReadyNotificationFromToken:]_block_invoke
+ ___75-[CPLProxyLibraryManager getStatusForComponents:timeout:completionHandler:]_block_invoke
+ ___75-[CPLProxyLibraryManager getStatusForComponents:timeout:completionHandler:]_block_invoke_2
+ ___75-[CPLProxyLibraryManager getStatusForComponents:timeout:completionHandler:]_block_invoke_2.cold.1
+ ___75-[CPLProxyLibraryManager getStatusForComponents:timeout:completionHandler:]_block_invoke_3
+ ___75-[CPLProxyLibraryManager updateRegistration:forObserver:completionHandler:]_block_invoke
+ ___75-[CPLProxyLibraryManager updateRegistration:forObserver:completionHandler:]_block_invoke_2
+ ___75-[CPLProxyLibraryManager updateRegistration:forObserver:completionHandler:]_block_invoke_2.cold.1
+ ___75-[CPLProxyLibraryManager updateRegistration:forObserver:completionHandler:]_block_invoke_3
+ ___76+[CPLTransportContainerConfiguration defaultTransportContainerConfiguration]_block_invoke
+ ___76-[CPLEngineDerivativesCache _selectivelyCleanUpTempURL:preservingFilenames:]_block_invoke
+ ___76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.96
+ ___76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.438
+ ___76-[CPLProxyLibraryManager refreshObservedEventForObserver:completionHandler:]_block_invoke
+ ___76-[CPLProxyLibraryManager refreshObservedEventForObserver:completionHandler:]_block_invoke.cold.1
+ ___76-[CPLProxyLibraryManager refreshObservedEventForObserver:completionHandler:]_block_invoke_2
+ ___76-[CPLUIScopeObservedSource fetchObservedEventForObserver:completionHandler:]_block_invoke
+ ___76-[CPLUploadPushedChangesTask generateDerivativesSubtask:didFinishWithError:]_block_invoke
+ ___77-[CPLLibraryManager initWithParameters:libraryIdentifier:libraryManagerType:]_block_invoke
+ ___77-[CPLUIRecordObservedSource fetchObservedEventForObserver:completionHandler:]_block_invoke
+ ___77-[NSObject(CPLCodingProxy) _cplCopyProperties:fromOtherObject:withCopyBlock:]_block_invoke.139
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.161
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.168
+ ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.165
+ ___78-[CPLProxyLibraryManager registerObserver:withRegistration:completionHandler:]_block_invoke
+ ___78-[CPLProxyLibraryManager registerObserver:withRegistration:completionHandler:]_block_invoke_2
+ ___78-[CPLProxyLibraryManager registerObserver:withRegistration:completionHandler:]_block_invoke_2.cold.1
+ ___78-[CPLProxyLibraryManager registerObserver:withRegistration:completionHandler:]_block_invoke_3
+ ___78-[CPLUIScopeObservedSource notifyUIStatusForScopesWithIdentifiersHaveChanged:]_block_invoke
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke.67
+ ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_2.68
+ ___79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.95
+ ___79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.467
+ ___79-[CPLLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]_block_invoke
+ ___79-[CPLUIScopeObservedSource notifyUIStatusScopeWithIdentifiers:isSynchronizing:]_block_invoke
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.148
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.151
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.155
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.149
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.156
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.150
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.157
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.158
+ ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_5.159
+ ___80-[CPLGenerateDerivativesSubtask _installGenerateDerivativesCancellationHandler:]_block_invoke
+ ___80-[CPLGenerateDerivativesSubtask _installGenerateDerivativesCancellationHandler:]_block_invoke_2
+ ___80-[CPLGenerateDerivativesSubtask _installGenerateDerivativesCancellationHandler:]_block_invoke_3
+ ___80-[CPLGenerateDerivativesSubtask observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___81-[CPLEngineUIObservationCenter updateRegistration:forObserver:completionHandler:]_block_invoke
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.125
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.137
+ ___82+[CPLTransportContainerConfiguration defaultTransportContainerConfigurationForE2E]_block_invoke
+ ___82-[CPLEngineUIObservationCenter refreshObservedEventForObserver:completionHandler:]_block_invoke
+ ___82-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopClientSession]_block_invoke
+ ___82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.325
+ ___82-[CPLUploadPushedChangesTask generateDerivativesSubtask:willStartWithChangeCount:]_block_invoke
+ ___83-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startClientSession]_block_invoke
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke.691
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_2
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_2.692
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_3
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_3.693
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_4
+ ___84-[CPLEngineLibrary(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke_5
+ ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.315
+ ___84-[CPLEngineUIObservationCenter registerObserver:withRegistration:completionHandler:]_block_invoke
+ ___84-[CPLProxyLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]_block_invoke
+ ___84-[CPLProxyLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]_block_invoke_2
+ ___84-[CPLProxyLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]_block_invoke_2.cold.1
+ ___84-[CPLProxyLibraryManager setPermanentError:onScopeWithIdentifier:completionHandler:]_block_invoke_3
+ ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.91
+ ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_2.92
+ ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_3.93
+ ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_4.94
+ ___85-[CPLLibraryManager(CPLManagement) getStatusForComponents:timeout:completionHandler:]_block_invoke
+ ___86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.327
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke.666
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke_2
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke_2.667
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke_3
+ ___87-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:timeout:completionHandler:]_block_invoke_3.677
+ ___87-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyRecordsUploadDidFinish]_block_invoke
+ ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke.498
+ ___87-[CPLLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke
+ ___87-[CPLLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke.446
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.176
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.185
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.189
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.175
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.178
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.186
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.190
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_3.180
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_3.187
+ ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_4.181
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.125
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.135
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.139
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.126
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.136
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.140
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.127
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.138
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.141
+ ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_4.142
+ ___88-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke
+ ___88-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke.412
+ ___88-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke_2
+ ___88-[CPLUIRecordObservedSource notifyUIStatusForAllRecordsWithScopeIdentifiersHaveChanged:]_block_invoke
+ ___89-[CPLEngineUIObservationCenter(CPLUITestObservedSource) testKey:value:completionHandler:]_block_invoke
+ ___91-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) stopSyncActivityForSource:]_block_invoke
+ ___91-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.365
+ ___91-[CPLUIRecordObservedSource notifyUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:]_block_invoke
+ ___91-[CPLUIRecordObservedSource notifyUploadProgressForRecordsWithLocalScopedIdentifiers:step:]_block_invoke
+ ___92-[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke
+ ___92-[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke_2
+ ___92-[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke_3
+ ___92-[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke_4
+ ___92-[CPLProxyLibraryManager uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:]_block_invoke_5
+ ___92-[CPLUIRecordObservedEventAccumulator scopedIdentifiersNeedingStatusesWithScopeIndexFinder:]_block_invoke
+ ___93-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) startSyncActivityFromSource:]_block_invoke
+ ___93-[CPLProxyLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke
+ ___93-[CPLProxyLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke_2
+ ___93-[CPLProxyLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke_3
+ ___93-[CPLProxyLibraryManager removeParticipants:fromSharedScopeWithIdentifier:completionHandler:]_block_invoke_4
+ ___94-[CPLEngineUIObservationCenter(CPLUISyncActivityObservedSource) syncActivitySource:isBlocked:]_block_invoke
+ ___94-[CPLUIRecordObservedSource notifyRecordsWithLocalScopedIdentifiersHaveStartedUploading:step:]_block_invoke
+ ___94-[CPLUIRecordObserver _updateProgressDictionaryWithUpdatedProgress:registration:updateStatus:]_block_invoke
+ ___95-[CPLEngineUIObservationCenter(CPLUIScopeObservedSource) notifyUIStatusForAllScopesHaveChanged]_block_invoke
+ ___95-[CPLGenerateDerivativesSubtask _generatingDerivativesForChange:fractionCompleted:chunkLength:]_block_invoke
+ ___95-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:willAddChangeBlock:]_block_invoke
+ ___95-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:willAddChangeBlock:]_block_invoke.10
+ ___95-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:willAddChangeBlock:]_block_invoke.8
+ ___96-[CPLGenerateDerivativesSubtask _copyResourceChangeFromChange:toChange:fingerprintScheme:error:]_block_invoke
+ ___97-[CPLEngineUIObservationCenter(CPLUIRecordObservedSource) notifyUIStatusForAllRecordsHaveChanged]_block_invoke
+ ___97-[CPLUploadPushedChangesTask generateDerivativesSubtask:didFinishGeneratingDerivativesForChange:]_block_invoke
+ ___97-[CPLUploadPushedChangesTask generateDerivativesSubtask:willStartGeneratingDerivativesForChange:]_block_invoke
+ ___97-[CPLUploadPushedChangesTask generateDerivativesSubtask:willStartGeneratingDerivativesForChange:]_block_invoke_2
+ ___98-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke
+ ___98-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:]_block_invoke.441
+ ___Block_byref_object_copy_.10164
+ ___Block_byref_object_copy_.10615
+ ___Block_byref_object_copy_.1072
+ ___Block_byref_object_copy_.1199
+ ___Block_byref_object_copy_.12231
+ ___Block_byref_object_copy_.12510
+ ___Block_byref_object_copy_.13414
+ ___Block_byref_object_copy_.1382
+ ___Block_byref_object_copy_.14101
+ ___Block_byref_object_copy_.14409
+ ___Block_byref_object_copy_.15221
+ ___Block_byref_object_copy_.1543
+ ___Block_byref_object_copy_.16310
+ ___Block_byref_object_copy_.16955
+ ___Block_byref_object_copy_.17330
+ ___Block_byref_object_copy_.17521
+ ___Block_byref_object_copy_.18361
+ ___Block_byref_object_copy_.19006
+ ___Block_byref_object_copy_.19770
+ ___Block_byref_object_copy_.20134
+ ___Block_byref_object_copy_.20643
+ ___Block_byref_object_copy_.21255
+ ___Block_byref_object_copy_.21965
+ ___Block_byref_object_copy_.22068
+ ___Block_byref_object_copy_.2269
+ ___Block_byref_object_copy_.23593
+ ___Block_byref_object_copy_.23732
+ ___Block_byref_object_copy_.24237
+ ___Block_byref_object_copy_.24846
+ ___Block_byref_object_copy_.25324
+ ___Block_byref_object_copy_.256
+ ___Block_byref_object_copy_.25656
+ ___Block_byref_object_copy_.2586
+ ___Block_byref_object_copy_.26748
+ ___Block_byref_object_copy_.27052
+ ___Block_byref_object_copy_.28183
+ ___Block_byref_object_copy_.2900
+ ___Block_byref_object_copy_.3388
+ ___Block_byref_object_copy_.3465
+ ___Block_byref_object_copy_.3760
+ ___Block_byref_object_copy_.411
+ ___Block_byref_object_copy_.4136
+ ___Block_byref_object_copy_.4855
+ ___Block_byref_object_copy_.516
+ ___Block_byref_object_copy_.6084
+ ___Block_byref_object_copy_.6988
+ ___Block_byref_object_copy_.7518
+ ___Block_byref_object_copy_.801
+ ___Block_byref_object_copy_.8442
+ ___Block_byref_object_copy_.8629
+ ___Block_byref_object_copy_.9481
+ ___Block_byref_object_copy_.9875
+ ___Block_byref_object_dispose_.10165
+ ___Block_byref_object_dispose_.10616
+ ___Block_byref_object_dispose_.1073
+ ___Block_byref_object_dispose_.1200
+ ___Block_byref_object_dispose_.12232
+ ___Block_byref_object_dispose_.12511
+ ___Block_byref_object_dispose_.13415
+ ___Block_byref_object_dispose_.1383
+ ___Block_byref_object_dispose_.14102
+ ___Block_byref_object_dispose_.14410
+ ___Block_byref_object_dispose_.15222
+ ___Block_byref_object_dispose_.1544
+ ___Block_byref_object_dispose_.16311
+ ___Block_byref_object_dispose_.16956
+ ___Block_byref_object_dispose_.17331
+ ___Block_byref_object_dispose_.17522
+ ___Block_byref_object_dispose_.18362
+ ___Block_byref_object_dispose_.19007
+ ___Block_byref_object_dispose_.19771
+ ___Block_byref_object_dispose_.20135
+ ___Block_byref_object_dispose_.20644
+ ___Block_byref_object_dispose_.21256
+ ___Block_byref_object_dispose_.21966
+ ___Block_byref_object_dispose_.22069
+ ___Block_byref_object_dispose_.2270
+ ___Block_byref_object_dispose_.23594
+ ___Block_byref_object_dispose_.23733
+ ___Block_byref_object_dispose_.24238
+ ___Block_byref_object_dispose_.24847
+ ___Block_byref_object_dispose_.25325
+ ___Block_byref_object_dispose_.25657
+ ___Block_byref_object_dispose_.257
+ ___Block_byref_object_dispose_.2587
+ ___Block_byref_object_dispose_.26749
+ ___Block_byref_object_dispose_.27053
+ ___Block_byref_object_dispose_.28184
+ ___Block_byref_object_dispose_.2901
+ ___Block_byref_object_dispose_.3389
+ ___Block_byref_object_dispose_.3466
+ ___Block_byref_object_dispose_.3761
+ ___Block_byref_object_dispose_.412
+ ___Block_byref_object_dispose_.4137
+ ___Block_byref_object_dispose_.4856
+ ___Block_byref_object_dispose_.517
+ ___Block_byref_object_dispose_.6085
+ ___Block_byref_object_dispose_.6989
+ ___Block_byref_object_dispose_.7519
+ ___Block_byref_object_dispose_.802
+ ___Block_byref_object_dispose_.8443
+ ___Block_byref_object_dispose_.8630
+ ___Block_byref_object_dispose_.9482
+ ___Block_byref_object_dispose_.9876
+ ___CPLCenterOSLogDomain
+ ___CPLCenterOSLogDomain.onceToken
+ ___CPLCenterOSLogDomain.result
+ ___CPLConfigurationOSLogDomain.22921
+ ___CPLConfigurationOSLogDomain.onceToken.22927
+ ___CPLConfigurationOSLogDomain.result.22929
+ ___CPLParametersOSLogDomain
+ ___CPLParametersOSLogDomain.onceToken
+ ___CPLParametersOSLogDomain.onceToken.28769
+ ___CPLParametersOSLogDomain.result
+ ___CPLParametersOSLogDomain.result.28770
+ ___CPLPullSessionOSLogDomain
+ ___CPLPullSessionOSLogDomain.onceToken
+ ___CPLPullSessionOSLogDomain.result
+ ___CPLResumableDerivativeGenerationOSLogDomain
+ ___CPLResumableDerivativeGenerationOSLogDomain.onceToken
+ ___CPLResumableDerivativeGenerationOSLogDomain.result
+ ___CPLSchedulerOSLogDomain.9801
+ ___CPLSchedulerOSLogDomain.onceToken.9802
+ ___CPLSchedulerOSLogDomain.result.9803
+ ___CPLSessionOSLogDomain.19629
+ ___CPLSessionOSLogDomain.21536
+ ___CPLSessionOSLogDomain.26259
+ ___CPLSessionOSLogDomain.onceToken.19631
+ ___CPLSessionOSLogDomain.onceToken.21541
+ ___CPLSessionOSLogDomain.onceToken.26261
+ ___CPLSessionOSLogDomain.result.19632
+ ___CPLSessionOSLogDomain.result.21542
+ ___CPLSessionOSLogDomain.result.26263
+ ___CPLSetTurboMode_block_invoke
+ ___CPLShouldUseTurboMode_block_invoke
+ ___CPLStorageOSLogDomain.10110
+ ___CPLStorageOSLogDomain.1088
+ ___CPLStorageOSLogDomain.11079
+ ___CPLStorageOSLogDomain.11513
+ ___CPLStorageOSLogDomain.11682
+ ___CPLStorageOSLogDomain.11877
+ ___CPLStorageOSLogDomain.14069
+ ___CPLStorageOSLogDomain.14155
+ ___CPLStorageOSLogDomain.21223
+ ___CPLStorageOSLogDomain.23712
+ ___CPLStorageOSLogDomain.248
+ ___CPLStorageOSLogDomain.24997
+ ___CPLStorageOSLogDomain.25643
+ ___CPLStorageOSLogDomain.25895
+ ___CPLStorageOSLogDomain.2884
+ ___CPLStorageOSLogDomain.580
+ ___CPLStorageOSLogDomain.8182
+ ___CPLStorageOSLogDomain.onceToken.10112
+ ___CPLStorageOSLogDomain.onceToken.1101
+ ___CPLStorageOSLogDomain.onceToken.11084
+ ___CPLStorageOSLogDomain.onceToken.11519
+ ___CPLStorageOSLogDomain.onceToken.11684
+ ___CPLStorageOSLogDomain.onceToken.11879
+ ___CPLStorageOSLogDomain.onceToken.14080
+ ___CPLStorageOSLogDomain.onceToken.14158
+ ___CPLStorageOSLogDomain.onceToken.17875
+ ___CPLStorageOSLogDomain.onceToken.21225
+ ___CPLStorageOSLogDomain.onceToken.23714
+ ___CPLStorageOSLogDomain.onceToken.23993
+ ___CPLStorageOSLogDomain.onceToken.250
+ ___CPLStorageOSLogDomain.onceToken.25001
+ ___CPLStorageOSLogDomain.onceToken.25648
+ ___CPLStorageOSLogDomain.onceToken.25903
+ ___CPLStorageOSLogDomain.onceToken.2886
+ ___CPLStorageOSLogDomain.onceToken.582
+ ___CPLStorageOSLogDomain.onceToken.8184
+ ___CPLStorageOSLogDomain.result.10113
+ ___CPLStorageOSLogDomain.result.1103
+ ___CPLStorageOSLogDomain.result.11085
+ ___CPLStorageOSLogDomain.result.11521
+ ___CPLStorageOSLogDomain.result.11685
+ ___CPLStorageOSLogDomain.result.11880
+ ___CPLStorageOSLogDomain.result.14082
+ ___CPLStorageOSLogDomain.result.14160
+ ___CPLStorageOSLogDomain.result.17877
+ ___CPLStorageOSLogDomain.result.21227
+ ___CPLStorageOSLogDomain.result.23716
+ ___CPLStorageOSLogDomain.result.23994
+ ___CPLStorageOSLogDomain.result.25003
+ ___CPLStorageOSLogDomain.result.252
+ ___CPLStorageOSLogDomain.result.25650
+ ___CPLStorageOSLogDomain.result.25905
+ ___CPLStorageOSLogDomain.result.2888
+ ___CPLStorageOSLogDomain.result.584
+ ___CPLStorageOSLogDomain.result.8186
+ ___CPLStoreOSLogDomain.3917
+ ___CPLStoreOSLogDomain.onceToken.3918
+ ___CPLStoreOSLogDomain.result.3919
+ ___CPLTaskOSLogDomain.14345
+ ___CPLTaskOSLogDomain.1541
+ ___CPLTaskOSLogDomain.17297
+ ___CPLTaskOSLogDomain.17780
+ ___CPLTaskOSLogDomain.18880
+ ___CPLTaskOSLogDomain.20549
+ ___CPLTaskOSLogDomain.24797
+ ___CPLTaskOSLogDomain.26675
+ ___CPLTaskOSLogDomain.28094
+ ___CPLTaskOSLogDomain.3447
+ ___CPLTaskOSLogDomain.4840
+ ___CPLTaskOSLogDomain.7171
+ ___CPLTaskOSLogDomain.743
+ ___CPLTaskOSLogDomain.9399
+ ___CPLTaskOSLogDomain.onceToken.14391
+ ___CPLTaskOSLogDomain.onceToken.1570
+ ___CPLTaskOSLogDomain.onceToken.17299
+ ___CPLTaskOSLogDomain.onceToken.17782
+ ___CPLTaskOSLogDomain.onceToken.18890
+ ___CPLTaskOSLogDomain.onceToken.20556
+ ___CPLTaskOSLogDomain.onceToken.24833
+ ___CPLTaskOSLogDomain.onceToken.26686
+ ___CPLTaskOSLogDomain.onceToken.28102
+ ___CPLTaskOSLogDomain.onceToken.3454
+ ___CPLTaskOSLogDomain.onceToken.4843
+ ___CPLTaskOSLogDomain.onceToken.7178
+ ___CPLTaskOSLogDomain.onceToken.746
+ ___CPLTaskOSLogDomain.onceToken.9414
+ ___CPLTaskOSLogDomain.result.14393
+ ___CPLTaskOSLogDomain.result.1571
+ ___CPLTaskOSLogDomain.result.17301
+ ___CPLTaskOSLogDomain.result.17784
+ ___CPLTaskOSLogDomain.result.18891
+ ___CPLTaskOSLogDomain.result.20557
+ ___CPLTaskOSLogDomain.result.24835
+ ___CPLTaskOSLogDomain.result.26687
+ ___CPLTaskOSLogDomain.result.28103
+ ___CPLTaskOSLogDomain.result.3456
+ ___CPLTaskOSLogDomain.result.4845
+ ___CPLTaskOSLogDomain.result.7180
+ ___CPLTaskOSLogDomain.result.748
+ ___CPLTaskOSLogDomain.result.9416
+ ___CPLUIObserverOSLogDomain
+ ___CPLUIObserverOSLogDomain.13403
+ ___CPLUIObserverOSLogDomain.15520
+ ___CPLUIObserverOSLogDomain.1914
+ ___CPLUIObserverOSLogDomain.2539
+ ___CPLUIObserverOSLogDomain.6869
+ ___CPLUIObserverOSLogDomain.9011
+ ___CPLUIObserverOSLogDomain.onceToken
+ ___CPLUIObserverOSLogDomain.onceToken.13406
+ ___CPLUIObserverOSLogDomain.onceToken.15529
+ ___CPLUIObserverOSLogDomain.onceToken.1918
+ ___CPLUIObserverOSLogDomain.onceToken.2548
+ ___CPLUIObserverOSLogDomain.onceToken.6875
+ ___CPLUIObserverOSLogDomain.onceToken.9025
+ ___CPLUIObserverOSLogDomain.result
+ ___CPLUIObserverOSLogDomain.result.13408
+ ___CPLUIObserverOSLogDomain.result.15531
+ ___CPLUIObserverOSLogDomain.result.1919
+ ___CPLUIObserverOSLogDomain.result.2550
+ ___CPLUIObserverOSLogDomain.result.6876
+ ___CPLUIObserverOSLogDomain.result.9026
+ ___CPLUploadOSLogDomain
+ ___CPLUploadOSLogDomain.onceToken
+ ___CPLUploadOSLogDomain.result
+ ____CPLFeedbackRecordClassForClass_block_invoke.27
+ ____CPLGetAccountDSID_block_invoke.138
+ ____CPLGetAccountDSID_block_invoke_2.144
+ ____CPLSharedDefaultsForTurboMode_block_invoke
+ _____CPLCenterOSLogDomain_block_invoke
+ _____CPLConfigurationOSLogDomain_block_invoke.22932
+ _____CPLParametersOSLogDomain_block_invoke
+ _____CPLParametersOSLogDomain_block_invoke.28773
+ _____CPLPullSessionOSLogDomain_block_invoke
+ _____CPLResumableDerivativeGenerationOSLogDomain_block_invoke
+ _____CPLSchedulerOSLogDomain_block_invoke.9805
+ _____CPLSessionOSLogDomain_block_invoke.19634
+ _____CPLSessionOSLogDomain_block_invoke.21544
+ _____CPLSessionOSLogDomain_block_invoke.26266
+ _____CPLStorageOSLogDomain_block_invoke.10115
+ _____CPLStorageOSLogDomain_block_invoke.1106
+ _____CPLStorageOSLogDomain_block_invoke.11087
+ _____CPLStorageOSLogDomain_block_invoke.11524
+ _____CPLStorageOSLogDomain_block_invoke.11687
+ _____CPLStorageOSLogDomain_block_invoke.11882
+ _____CPLStorageOSLogDomain_block_invoke.14085
+ _____CPLStorageOSLogDomain_block_invoke.14163
+ _____CPLStorageOSLogDomain_block_invoke.17882
+ _____CPLStorageOSLogDomain_block_invoke.21230
+ _____CPLStorageOSLogDomain_block_invoke.23719
+ _____CPLStorageOSLogDomain_block_invoke.24000
+ _____CPLStorageOSLogDomain_block_invoke.25006
+ _____CPLStorageOSLogDomain_block_invoke.255
+ _____CPLStorageOSLogDomain_block_invoke.25653
+ _____CPLStorageOSLogDomain_block_invoke.25908
+ _____CPLStorageOSLogDomain_block_invoke.2891
+ _____CPLStorageOSLogDomain_block_invoke.587
+ _____CPLStorageOSLogDomain_block_invoke.8189
+ _____CPLStoreOSLogDomain_block_invoke.3921
+ _____CPLTaskOSLogDomain_block_invoke.14396
+ _____CPLTaskOSLogDomain_block_invoke.1573
+ _____CPLTaskOSLogDomain_block_invoke.17304
+ _____CPLTaskOSLogDomain_block_invoke.17787
+ _____CPLTaskOSLogDomain_block_invoke.18893
+ _____CPLTaskOSLogDomain_block_invoke.20559
+ _____CPLTaskOSLogDomain_block_invoke.24838
+ _____CPLTaskOSLogDomain_block_invoke.26689
+ _____CPLTaskOSLogDomain_block_invoke.28106
+ _____CPLTaskOSLogDomain_block_invoke.3459
+ _____CPLTaskOSLogDomain_block_invoke.4848
+ _____CPLTaskOSLogDomain_block_invoke.7183
+ _____CPLTaskOSLogDomain_block_invoke.751
+ _____CPLTaskOSLogDomain_block_invoke.9419
+ _____CPLUIObserverOSLogDomain_block_invoke
+ _____CPLUIObserverOSLogDomain_block_invoke.13411
+ _____CPLUIObserverOSLogDomain_block_invoke.15534
+ _____CPLUIObserverOSLogDomain_block_invoke.1921
+ _____CPLUIObserverOSLogDomain_block_invoke.2553
+ _____CPLUIObserverOSLogDomain_block_invoke.6878
+ _____CPLUIObserverOSLogDomain_block_invoke.9028
+ _____CPLUploadOSLogDomain_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e67_"CPLActiveDownloadQueue"24?0Q8"CPLResourceTransferTaskOptions"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96r104r_e5_v8?0lr96l8s32l8s40l8r104l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs104r112r_e71_v32?0"NSArray"8"CPLPartialDerivativesGenerationResult"16"NSError"24ls32l8s40l8s48l8s96l8s56l8s64l8s72l8r104l8s80l8r112l8s88l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88bs96bs104r112r_e71_v32?0"NSArray"8"CPLPartialDerivativesGenerationResult"16"NSError"24ls32l8s40l8s48l8s88l8s56l8s64l8r104l8s72l8r112l8s80l8s96l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136r_e5_v8?0ls32l8s40l8s120l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r128l8s104l8r136l8s112l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs128r136r_e5_v8?0ls32l8s40l8s112l8s48l8s56l8s64l8s72l8s80l8s88l8r128l8s96l8r136l8s104l8s120l8
+ ___block_descriptor_200_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s_e67_"CPLActiveDownloadQueue"24?0Q8"CPLResourceTransferTaskOptions"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8s176l8s184l8s192l8
+ ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
+ ___block_descriptor_32_e28_v16?0"CPLUIObservedEvent"8l
+ ___block_descriptor_32_e34_v16?0"<CPLEngineTransportTask>"8l
+ ___block_descriptor_32_e34_v16?0"CPLUIScopeObservedSource"8l
+ ___block_descriptor_32_e35_v16?0"CPLUIRecordObservedSource"8l
+ ___block_descriptor_32_e39_v16?0"CPLGenerateDerivativesSubtask"8l
+ ___block_descriptor_32_e41_v16?0"CPLUISyncActivityObservedSource"8l
+ ___block_descriptor_32_e42_v24?0"CPLUIObserverAndRegistration"8^B16l
+ ___block_descriptor_32_e53_v32?0"NSUUID"8"CPLUIObserverAndRegistration"16^B24l
+ ___block_descriptor_33_e35_v16?0"CPLUIRecordObservedSource"8l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e53_v32?0"NSUUID"8"CPLUIObserverAndRegistration"16^B24ls32l8
+ ___block_descriptor_40_e8_32r_e43_v32?0"NSString"8"CPLUIScopeStatus"16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e12_v24?0q8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e18_q16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8I16ls32l8
+ ___block_descriptor_40_e8_32s_e33_B32?0"<CPLBrokenScope>"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e34_v16?0"CPLUIScopeObservedSource"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v16?0"CPLUIRecordObservedSource"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_v24?0"CPLEngineScope"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v16?0"CPLGenerateDerivativesSubtask"8ls32l8
+ ___block_descriptor_40_e8_32s_e40_v16?0"<CPLUIObserverPrivateDelegate>"8ls32l8
+ ___block_descriptor_40_e8_32s_e41_v16?0"CPLUISyncActivityObservedSource"8ls32l8
+ ___block_descriptor_40_e8_32s_e42_v24?0"CPLUIObserverAndRegistration"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e43_v32?0"NSString"8"CPLUIScopeStatus"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e45_v28?0"CPLScopedIdentifier"8"NSNumber"16B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e53_v32?0"NSUUID"8"CPLUIObserverAndRegistration"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e62_v32?0"CPLScopedIdentifier"8"CPLBeforeUploadCheckItem"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_41_e8_32s_e34_v16?0"CPLUIScopeObservedSource"8ls32l8
+ ___block_descriptor_41_e8_32s_e41_v16?0"CPLUISyncActivityObservedSource"8ls32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e29_16?0"CPLScopedIdentifier"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"CPLUITestObservedSource"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"CPLChangeBatch"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e55_v32?0"NSError"8"NSString"16"CPLLibraryParameters"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e25_v16?0"CPLCallObserver"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e28_v16?0"CPLUIObservedEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_v16?0"CPLUIRecordObservedSource"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e40_v16?0"<CPLUIObserverPrivateDelegate>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e41_v16?0"CPLUISyncActivityObservedSource"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e42_v24?0"CPLUIObserverAndRegistration"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e55_v32?0"NSError"8"NSString"16"CPLLibraryParameters"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e29_v16?0"CPLUIObservedSource"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e29_B16?0"CPLScopedIdentifier"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e25_v16?0"CPLCallObserver"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e36_v24?0"CPLScopeChange"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v24?0"CPLEngineSchedulerBlocker"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e26_v16?0"CPLForceSyncTask"8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e32_v20?0"CPLScopedIdentifier"8f16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e28_v16?0"CPLUIObservedEvent"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e41_v16?0"CPLUISyncActivityObservedSource"8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e25_v16?0"CPLCallObserver"8ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e46_v32?0"CPLScopedIdentifier"8"NSNumber"16^B24ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e87_v80?0"NSError"8"NSDictionary"16Q24Q32Q40Q48Q56"NSString"64"CPLLibraryParameters"72ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r_e12_v24?0q8^B16ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls48l8s32l8s40l8s56l8
+ ___block_descriptor_64_e8_32s40s48bs_e29_v16?0"CPLUIObservedSource"8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e64_B48?0"CPLRecordChange"8"CPLRecordChange"16"NSString"24:32:40lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e28_v16?0"CPLUIObservedEvent"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v16?0"CPLScopedIdentifier"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56s_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r_e12_v24?0q8^B16lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e89_v32?0"_CPLResourcesMutableArray"8"CPLPartialDerivativesGenerationResult"16"NSError"24ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e30_v16?0"<CPLEngineComponent>"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e30_v24?0"NSString"8"NSError"16ls32l8r72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e30_v24?0"NSString"8"NSError"16ls32l8r64l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e35_v16?0"CPLEngineStoreTransaction"8ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e5_B8?0ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_81_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8r72l8r80l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.10
+ ___block_literal_global.100.16317
+ ___block_literal_global.100.17783
+ ___block_literal_global.102
+ ___block_literal_global.10239
+ ___block_literal_global.10693
+ ___block_literal_global.109.22444
+ ___block_literal_global.109.24532
+ ___block_literal_global.1090
+ ___block_literal_global.1093
+ ___block_literal_global.110.28160
+ ___block_literal_global.1102
+ ___block_literal_global.11201
+ ___block_literal_global.11413
+ ___block_literal_global.11520
+ ___block_literal_global.11619
+ ___block_literal_global.118
+ ___block_literal_global.118.28146
+ ___block_literal_global.11931
+ ___block_literal_global.12.10242
+ ___block_literal_global.12105
+ ___block_literal_global.122
+ ___block_literal_global.12298
+ ___block_literal_global.1239
+ ___block_literal_global.12616
+ ___block_literal_global.129.13407
+ ___block_literal_global.129.24834
+ ___block_literal_global.129.6783
+ ___block_literal_global.12958
+ ___block_literal_global.130
+ ___block_literal_global.130.10268
+ ___block_literal_global.13308
+ ___block_literal_global.134
+ ___block_literal_global.13419
+ ___block_literal_global.13676
+ ___block_literal_global.1387
+ ___block_literal_global.139
+ ___block_literal_global.13915
+ ___block_literal_global.14.13430
+ ___block_literal_global.14.17818
+ ___block_literal_global.14081
+ ___block_literal_global.141.16312
+ ___block_literal_global.141.22445
+ ___block_literal_global.141.24535
+ ___block_literal_global.14159
+ ___block_literal_global.14392
+ ___block_literal_global.145.10271
+ ___block_literal_global.145.22446
+ ___block_literal_global.147
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.152.24537
+ ___block_literal_global.15392
+ ___block_literal_global.155
+ ___block_literal_global.15530
+ ___block_literal_global.158
+ ___block_literal_global.158.24538
+ ___block_literal_global.15826
+ ___block_literal_global.16.28466
+ ___block_literal_global.1616
+ ___block_literal_global.162
+ ___block_literal_global.163
+ ___block_literal_global.16335
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.17.11929
+ ___block_literal_global.170
+ ___block_literal_global.170.24539
+ ___block_literal_global.173
+ ___block_literal_global.17300
+ ___block_literal_global.17568
+ ___block_literal_global.1777
+ ___block_literal_global.17817
+ ___block_literal_global.17876
+ ___block_literal_global.18038
+ ___block_literal_global.1812
+ ___block_literal_global.1814
+ ___block_literal_global.1819
+ ___block_literal_global.1822
+ ___block_literal_global.1824
+ ___block_literal_global.1826
+ ___block_literal_global.1826.7496
+ ___block_literal_global.1828
+ ___block_literal_global.1830
+ ___block_literal_global.1832
+ ___block_literal_global.1834
+ ___block_literal_global.1836
+ ___block_literal_global.1838
+ ___block_literal_global.184
+ ___block_literal_global.1840
+ ___block_literal_global.1842
+ ___block_literal_global.1844
+ ___block_literal_global.1846
+ ___block_literal_global.1848
+ ___block_literal_global.1850
+ ___block_literal_global.1852
+ ___block_literal_global.1854
+ ___block_literal_global.1856
+ ___block_literal_global.18578
+ ___block_literal_global.18598
+ ___block_literal_global.1866
+ ___block_literal_global.18660
+ ___block_literal_global.187
+ ___block_literal_global.1874
+ ___block_literal_global.1882
+ ___block_literal_global.1884
+ ___block_literal_global.1889
+ ___block_literal_global.18901
+ ___block_literal_global.1891
+ ___block_literal_global.19
+ ___block_literal_global.1945
+ ___block_literal_global.19484
+ ___block_literal_global.196
+ ___block_literal_global.19700
+ ___block_literal_global.199
+ ___block_literal_global.199.12596
+ ___block_literal_global.20314
+ ___block_literal_global.2044
+ ___block_literal_global.2050
+ ___block_literal_global.20665
+ ___block_literal_global.2069
+ ___block_literal_global.21015
+ ___block_literal_global.21226
+ ___block_literal_global.214
+ ___block_literal_global.21554
+ ___block_literal_global.21725
+ ___block_literal_global.218
+ ___block_literal_global.21910
+ ___block_literal_global.221
+ ___block_literal_global.224
+ ___block_literal_global.22560
+ ___block_literal_global.2266
+ ___block_literal_global.229
+ ___block_literal_global.22928
+ ___block_literal_global.231
+ ___block_literal_global.232
+ ___block_literal_global.23328
+ ___block_literal_global.23715
+ ___block_literal_global.23878
+ ___block_literal_global.23996
+ ___block_literal_global.242
+ ___block_literal_global.24528
+ ___block_literal_global.2465
+ ___block_literal_global.24853
+ ___block_literal_global.25002
+ ___block_literal_global.251
+ ___block_literal_global.25175
+ ___block_literal_global.2549
+ ___block_literal_global.25649
+ ___block_literal_global.258
+ ___block_literal_global.25904
+ ___block_literal_global.26075
+ ___block_literal_global.26262
+ ___block_literal_global.26417
+ ___block_literal_global.26744
+ ___block_literal_global.271
+ ___block_literal_global.27414
+ ___block_literal_global.2752
+ ___block_literal_global.27646
+ ___block_literal_global.27782
+ ___block_literal_global.27854
+ ___block_literal_global.282
+ ___block_literal_global.28288
+ ___block_literal_global.283
+ ___block_literal_global.28440
+ ___block_literal_global.28599
+ ___block_literal_global.28848
+ ___block_literal_global.2887
+ ___block_literal_global.29169
+ ___block_literal_global.293
+ ___block_literal_global.300
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.315
+ ___block_literal_global.3153
+ ___block_literal_global.322
+ ___block_literal_global.322.15765
+ ___block_literal_global.324
+ ___block_literal_global.325
+ ___block_literal_global.325.15711
+ ___block_literal_global.325.6075
+ ___block_literal_global.326
+ ___block_literal_global.327
+ ___block_literal_global.328
+ ___block_literal_global.33.26042
+ ___block_literal_global.3329
+ ___block_literal_global.3387
+ ___block_literal_global.34.12507
+ ___block_literal_global.34.3326
+ ___block_literal_global.344
+ ___block_literal_global.3455
+ ___block_literal_global.355
+ ___block_literal_global.36
+ ___block_literal_global.363
+ ___block_literal_global.367
+ ___block_literal_global.37.13600
+ ___block_literal_global.372
+ ___block_literal_global.376
+ ___block_literal_global.382
+ ___block_literal_global.3822
+ ___block_literal_global.3897
+ ___block_literal_global.39
+ ___block_literal_global.4166
+ ___block_literal_global.42.10249
+ ___block_literal_global.43.22482
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.4437
+ ___block_literal_global.450
+ ___block_literal_global.466
+ ___block_literal_global.470
+ ___block_literal_global.4725
+ ___block_literal_global.4844
+ ___block_literal_global.497
+ ___block_literal_global.499
+ ___block_literal_global.50.28494
+ ___block_literal_global.50.9523
+ ___block_literal_global.51
+ ___block_literal_global.51.28829
+ ___block_literal_global.5106
+ ___block_literal_global.527
+ ___block_literal_global.54.28824
+ ___block_literal_global.54.4714
+ ___block_literal_global.5582
+ ___block_literal_global.561
+ ___block_literal_global.564
+ ___block_literal_global.57.10253
+ ___block_literal_global.5726
+ ___block_literal_global.582
+ ___block_literal_global.583
+ ___block_literal_global.6.18899
+ ___block_literal_global.6083
+ ___block_literal_global.621
+ ___block_literal_global.624
+ ___block_literal_global.6264
+ ___block_literal_global.64
+ ___block_literal_global.645
+ ___block_literal_global.648
+ ___block_literal_global.65
+ ___block_literal_global.651
+ ___block_literal_global.6753
+ ___block_literal_global.6993
+ ___block_literal_global.7038
+ ___block_literal_global.7179
+ ___block_literal_global.7332
+ ___block_literal_global.74
+ ___block_literal_global.74.20273
+ ___block_literal_global.79
+ ___block_literal_global.797
+ ___block_literal_global.8.28458
+ ___block_literal_global.800
+ ___block_literal_global.8013
+ ___block_literal_global.803
+ ___block_literal_global.806
+ ___block_literal_global.8185
+ ___block_literal_global.8418
+ ___block_literal_global.873
+ ___block_literal_global.8739
+ ___block_literal_global.89
+ ___block_literal_global.892
+ ___block_literal_global.9162
+ ___block_literal_global.92
+ ___block_literal_global.9415
+ ___block_literal_global.9531
+ ___block_literal_global.96.10007
+ ___block_literal_global.97
+ ___block_literal_global.99
+ ___block_literal_global.9940
+ ___cpl_dispatch_async_block_invoke.10122
+ ___cpl_dispatch_async_block_invoke.10684
+ ___cpl_dispatch_async_block_invoke.12218
+ ___cpl_dispatch_async_block_invoke.12591
+ ___cpl_dispatch_async_block_invoke.13394
+ ___cpl_dispatch_async_block_invoke.14341
+ ___cpl_dispatch_async_block_invoke.15005
+ ___cpl_dispatch_async_block_invoke.1575
+ ___cpl_dispatch_async_block_invoke.17310
+ ___cpl_dispatch_async_block_invoke.17693
+ ___cpl_dispatch_async_block_invoke.17773
+ ___cpl_dispatch_async_block_invoke.18985
+ ___cpl_dispatch_async_block_invoke.1912
+ ___cpl_dispatch_async_block_invoke.20079
+ ___cpl_dispatch_async_block_invoke.20618
+ ___cpl_dispatch_async_block_invoke.20967
+ ___cpl_dispatch_async_block_invoke.21881
+ ___cpl_dispatch_async_block_invoke.22907
+ ___cpl_dispatch_async_block_invoke.2358
+ ___cpl_dispatch_async_block_invoke.24221
+ ___cpl_dispatch_async_block_invoke.24794
+ ___cpl_dispatch_async_block_invoke.25182
+ ___cpl_dispatch_async_block_invoke.26419
+ ___cpl_dispatch_async_block_invoke.26691
+ ___cpl_dispatch_async_block_invoke.28136
+ ___cpl_dispatch_async_block_invoke.3809
+ ___cpl_dispatch_async_block_invoke.4839
+ ___cpl_dispatch_async_block_invoke.514
+ ___cpl_dispatch_async_block_invoke.806
+ ___cpl_dispatch_async_block_invoke.8675
+ ___cpl_dispatch_async_block_invoke.9397
+ ___cpl_dispatch_async_block_invoke.9691
+ __brokenScopeClass
+ __connectedLibraryManagerRegisterLock
+ __doProtected:.onceToken.18597
+ __doProtected:.onceToken.26416
+ __doProtected:.queue.26418
+ __enableRedactedURLs
+ __logResumableDerivativeGeneration
+ __nsDateClass
+ __nsURLClass
+ __resourceTypeSetFromPlist
+ __resourceTypesThatCountAgainstiCloudQuota.onceToken
+ __resourceTypesThatCountAgainstiCloudQuota.result
+ __sharedEPPContext
+ __shouldDisableUploadRate
+ __shouldPreventWipeOnUpgrade
+ __shouldUseTurboMode
+ __shouldUseTurboModeSet
+ __statusDidChange.15238
+ __storeWipeHandlerClass
+ __turboModeLock
+ _computeExpandedBatchWithError:.onceToken.36
+ _configurationForTestManateeContainer.onceToken
+ _configurationForTestManateeContainer.result
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.22466
+ _cplAdditionalSecureClassesForProperty:.additionalClasses.126
+ _cplAdditionalSecureClassesForProperty:.additionalClasses.159
+ _cplAdditionalSecureClassesForProperty:.onceToken.127
+ _cplAdditionalSecureClassesForProperty:.onceToken.155
+ _cplAdditionalSecureClassesForProperty:.onceToken.160
+ _defaultTransportContainerConfiguration.onceToken
+ _defaultTransportContainerConfiguration.result
+ _defaultTransportContainerConfigurationForE2E.onceToken
+ _defaultTransportContainerConfigurationForE2E.result
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _initWithCPLArchiver:.onceToken.2047
+ _initWithCPLArchiver:.stringClass.2048
+ _initWithCoder:.logOnceToken.23880
+ _initWithCoder:.onceToken.106
+ _initWithCoder:.onceToken.13619
+ _initWithCoder:.onceToken.17567
+ _initWithCoder:.onceToken.21553
+ _initWithCoder:.onceToken.23877
+ _initWithCoder:.onceToken.26074
+ _initWithCoder:.onceToken.29168
+ _initWithCoder:.onceToken.6726
+ _initWithCoder:.onceToken.7037
+ _initWithCoder:.onceToken.77
+ _initWithCoder:.onceToken.8413
+ _initWithCoder:.onceToken.87
+ _initWithCoder:.onceToken.94
+ _initWithCoder:.pushContextsClasses.26076
+ _initWithCoder:.stringClass.107
+ _initWithCoder:.stringClass.13620
+ _initWithParameters:libraryIdentifier:libraryManagerType:.onceToken
+ _mappingForExpiringState.mapping
+ _mappingForExpiringState.onceToken
+ _mappingForFeatureDataclasses.mapping
+ _mappingForFeatureDataclasses.onceToken
+ _mappingForMigrationState.mapping
+ _mappingForMigrationState.onceToken
+ _mappingForOptions.mapping
+ _mappingForOptions.onceToken
+ _mappingForScopeIdentifierPrefixToFeatureDataclass.mapping
+ _mappingForScopeIdentifierPrefixToFeatureDataclass.onceToken
+ _mappingForViewingMode.mapping
+ _mappingForViewingMode.onceToken
+ _nw_path_get_link_quality
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_allRelatedScopesForScope:
+ _objc_msgSend$_dropConnectionCompletely
+ _objc_msgSend$_dropConnectionCompletelyLocked
+ _objc_msgSend$_fetchTransportScopeWithActiveScope:
+ _objc_msgSend$_fillStatus:forComponents:timeout:completionHandler:
+ _objc_msgSend$_scheduleObserverNotifications
+ _objc_msgSend$_updateCanUseTurboModeOnScheduler
+ _objc_msgSend$_updateParameters:
+ _objc_msgSend$_upgradeFromVersion:
+ _objc_msgSend$acceptShareFromFetchedScope:completionHandler:
+ _objc_msgSend$accountPartitionType
+ _objc_msgSend$acknowledgeRecordWithScopedIdentifier:error:
+ _objc_msgSend$acquireBackgroundActivityWithCompletionHandler:
+ _objc_msgSend$activateScopesWithScopeTypes:error:
+ _objc_msgSend$addObserver:registration:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addUploadType:forCloudScopedIdentifier:
+ _objc_msgSend$allowedDisabledFeatureDataclasses
+ _objc_msgSend$allowedFeatureDataclasses
+ _objc_msgSend$allowsAccessRequests
+ _objc_msgSend$allowsAnonymousPublicAccess
+ _objc_msgSend$allowsFeedback
+ _objc_msgSend$assetCountPerType
+ _objc_msgSend$assetCountPerTypeData
+ _objc_msgSend$attemptRecovery
+ _objc_msgSend$backgroundScheduler
+ _objc_msgSend$batterySaverWatcherDidChangeState:
+ _objc_msgSend$blockWriteTransactionsWithReason:completionHandler:
+ _objc_msgSend$blocked
+ _objc_msgSend$blockedDateWithReason:
+ _objc_msgSend$bypassBackgroundSchedulingIfPossible
+ _objc_msgSend$cancelBackgroundActivityRequest:
+ _objc_msgSend$cancelFromSyncManager:
+ _objc_msgSend$checkNextBatchToPopWithPullUUID:
+ _objc_msgSend$checkScopeIdentifier:invalidReason:
+ _objc_msgSend$clearAllPermanentErrorHasChanges:error:
+ _objc_msgSend$clearAllPermanentErrorWithError:
+ _objc_msgSend$clearAllPermanentErrorsWithCompletionHandler:
+ _objc_msgSend$cloudChangeBatchFromBatch:usingMapping:isFinal:uiUploadProgressHub:withError:
+ _objc_msgSend$concreteTransportReferenceFromTransportReference:error:
+ _objc_msgSend$configurationForTestManateeContainer
+ _objc_msgSend$configurationWithContainerIdentifier:bundleIdentifier:options:
+ _objc_msgSend$containerConfiguration
+ _objc_msgSend$context
+ _objc_msgSend$copyAllowingAllRecordClassesForContainerIdentifier:
+ _objc_msgSend$copyChangingLibraryOptions:
+ _objc_msgSend$copyChangingTransportContainerConfiguration:
+ _objc_msgSend$copyWithFingerprintContext:
+ _objc_msgSend$copyWithoutSynchronizing
+ _objc_msgSend$coveredScopeIdentifiers
+ _objc_msgSend$coveredScopeIdentifiersFromScopeIdentifiers:
+ _objc_msgSend$coveredScopedIdentifiers
+ _objc_msgSend$coveredScopedIdentifiersFromScopeIdentifiers:
+ _objc_msgSend$coveredScopedIdentifiersFromScopedIdentifiers:
+ _objc_msgSend$coveredScopedIdentifiersFromScopedIdentifiersEnumeration:
+ _objc_msgSend$cplOriginalError
+ _objc_msgSend$cplSimpleDescription
+ _objc_msgSend$createBackgroundSchedulerForSession:
+ _objc_msgSend$createBackgroundSchedulerIfNecessary
+ _objc_msgSend$createGroupForAcceptingScopeWithType:
+ _objc_msgSend$createGroupForDecliningScopeWithType:
+ _objc_msgSend$createGroupForDirectTransportScopeDelete
+ _objc_msgSend$createGroupForDirectUpload
+ _objc_msgSend$createGroupForFetchingScopeWithType:
+ _objc_msgSend$createGroupForPublishingScopeWithType:
+ _objc_msgSend$createGroupForRemovingParticipantsFromShare
+ _objc_msgSend$createGroupForThumbnailPrefetchWithIntent:
+ _objc_msgSend$createGroupForUpdatingScopeWithType:
+ _objc_msgSend$currentRegistration
+ _objc_msgSend$deactivateScopesWithScopeTypes:error:
+ _objc_msgSend$declineSharedScope:completionHandler:
+ _objc_msgSend$declineTaskForSharedScope:completionHandler:
+ _objc_msgSend$defaultFlagsForScopeChange:
+ _objc_msgSend$defaultTransportContainerConfiguration
+ _objc_msgSend$defaultTransportContainerConfigurationForE2E
+ _objc_msgSend$descriptionForExpiringState:
+ _objc_msgSend$descriptionForFeatureDataclass:
+ _objc_msgSend$descriptionForFeatureDataclasses:
+ _objc_msgSend$descriptionForOptions:
+ _objc_msgSend$descriptionForSyncActivityType:
+ _objc_msgSend$descriptionForViewingMode:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$didDisconnectFromObservedSource
+ _objc_msgSend$didDropFullRecordItemWithScopedIdentifier:
+ _objc_msgSend$didRefreshObservedEvent:
+ _objc_msgSend$didUseOverLimitStrategy
+ _objc_msgSend$disableFeatureDataclasses:completionHandler:
+ _objc_msgSend$disablePrimaryScopeWithError:
+ _objc_msgSend$discardContainerWithCompletionHandler:
+ _objc_msgSend$displayablePropertyListWithRootObject:
+ _objc_msgSend$dropUploadType:forCloudScopedIdentifier:
+ _objc_msgSend$enableFeatureDataclasses:completionHandler:
+ _objc_msgSend$engineLibrary:getStatusSummaryWithCompletionHandler:
+ _objc_msgSend$engineLibraryCatastrophicExit:
+ _objc_msgSend$engineLibraryDidUpdateParameters:
+ _objc_msgSend$enumerateFeatureDataclassesWithBlock:
+ _objc_msgSend$enumerateObserversWithBlock:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$eventDescription
+ _objc_msgSend$excludedScopeIdentifiers
+ _objc_msgSend$expiringState
+ _objc_msgSend$featureDataclasses
+ _objc_msgSend$fetchObservedEventForObserver:completionHandler:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$fillUIScopeStatus:forScope:sharingScope:
+ _objc_msgSend$fillUIScopeStatus:forScopeWithIdentifier:
+ _objc_msgSend$fireObserverNotifications
+ _objc_msgSend$firstStateNeedingClientInSync
+ _objc_msgSend$forAllRecords
+ _objc_msgSend$forAllScopes
+ _objc_msgSend$forceMMCSv2AsDefault
+ _objc_msgSend$forceRefresh
+ _objc_msgSend$forceSyncForScopeIdentifiers:forcePushFromClient:reply:
+ _objc_msgSend$forceSynchronizingScopeWithIdentifiers:forcePushFromClient:completionHandler:
+ _objc_msgSend$generateDerivativesSubtask:derivativesGenerationForChange:didProgress:
+ _objc_msgSend$generateDerivativesSubtask:didFinishGeneratingDerivativesForChange:
+ _objc_msgSend$generateDerivativesSubtask:didFinishWithError:
+ _objc_msgSend$generateDerivativesSubtask:didProgressGeneratingDerivativesFromResourceSize:
+ _objc_msgSend$generateDerivativesSubtask:willStartGeneratingDerivativesForChange:
+ _objc_msgSend$generateDerivativesSubtask:willStartWithChangeCount:
+ _objc_msgSend$getAddedScopeIdentifiers:deletedScopeIdentifiers:withNewRegistration:
+ _objc_msgSend$getAddedScopedIdentifiers:deletedScopedIdentifiers:withNewRegistration:
+ _objc_msgSend$getStatusForComponents:timeout:completionHandler:
+ _objc_msgSend$getSystemBudgetsForBackgroundActivityWithCompletionHandler:
+ _objc_msgSend$hasChangesToDownload
+ _objc_msgSend$hasChangesToUpload
+ _objc_msgSend$hasGoodQualityNetwork
+ _objc_msgSend$hasObservers
+ _objc_msgSend$inBatterySaverMode
+ _objc_msgSend$initForContainerIdentifier:
+ _objc_msgSend$initForContainerIdentifier:filterDefinition:
+ _objc_msgSend$initForUIWithLibraryIdentifier:
+ _objc_msgSend$initWithBlocked:updatedNonUploadingStatuses:updatedUploadingProgresses:
+ _objc_msgSend$initWithCacheURL:identifier:parentCache:queue:
+ _objc_msgSend$initWithChanges:fingerprintContext:derivativesCache:derivativesFilter:
+ _objc_msgSend$initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:transportContainerConfiguration:
+ _objc_msgSend$initWithComponents:queue:handler:
+ _objc_msgSend$initWithContainerIdentifier:bundleIdentifier:options:
+ _objc_msgSend$initWithContainerIdentifier:bundleIdentifier:options:fingerprintContext:schemaFilter:
+ _objc_msgSend$initWithCoveredScopeIdentifiers:
+ _objc_msgSend$initWithCoveredScopedIdentifiers:
+ _objc_msgSend$initWithDelegate:queue:
+ _objc_msgSend$initWithDispatchQueue:delegate:
+ _objc_msgSend$initWithIdentifier:manager:queue:
+ _objc_msgSend$initWithIdentifier:manager:queue:initialRegistration:
+ _objc_msgSend$initWithLibraryIdentifier:queue:
+ _objc_msgSend$initWithObject:selector:functionName:timeout:
+ _objc_msgSend$initWithParameters:libraryIdentifier:libraryManagerType:
+ _objc_msgSend$initWithProgress:
+ _objc_msgSend$initWithStartEvent:
+ _objc_msgSend$initWithStatuses:
+ _objc_msgSend$initWithSyncActivity:type:clientSessionActivity:scopeIdentifier:
+ _objc_msgSend$initWithSyncActivity:type:clientSessionActivity:scopeIdentifier:progress:
+ _objc_msgSend$initWithType:
+ _objc_msgSend$initWithUpdatedScopedIdentifiers:blocked:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$isDoingSomeActivity
+ _objc_msgSend$isExceedingLimit
+ _objc_msgSend$isExceedingSharedLibraryLimit
+ _objc_msgSend$isExpensive
+ _objc_msgSend$isForeground
+ _objc_msgSend$isGoodQuality
+ _objc_msgSend$isInClientSession
+ _objc_msgSend$isInResetSync
+ _objc_msgSend$isInSyncActivity
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$isNetworkExpensive
+ _objc_msgSend$isObservedScopedIdentifier:
+ _objc_msgSend$isPermanentError:
+ _objc_msgSend$isPlaceholder
+ _objc_msgSend$isPostComment
+ _objc_msgSend$isProxy
+ _objc_msgSend$isProxyRecord
+ _objc_msgSend$isResourceCountingForQuota
+ _objc_msgSend$isStartEvent
+ _objc_msgSend$isStarted
+ _objc_msgSend$isSynchronizing
+ _objc_msgSend$isUsualPhotosContainer
+ _objc_msgSend$isValidRegistration:
+ _objc_msgSend$itemWillBeDropped:
+ _objc_msgSend$lastSuccessfulSyncDate
+ _objc_msgSend$lastSyncDate
+ _objc_msgSend$lastSyncDateForScope:
+ _objc_msgSend$launchFromSyncManager:
+ _objc_msgSend$libraryManagerType
+ _objc_msgSend$linkQuality
+ _objc_msgSend$managerNameForObserver:
+ _objc_msgSend$mappingForExpiringState
+ _objc_msgSend$mappingForFeatureDataclasses
+ _objc_msgSend$mappingForMigrationState
+ _objc_msgSend$mappingForOptions
+ _objc_msgSend$mappingForScopeIdentifierPrefixToFeatureDataclass
+ _objc_msgSend$mappingForViewingMode
+ _objc_msgSend$matchesConfiguration:
+ _objc_msgSend$matchesParameters:
+ _objc_msgSend$nTimeURL
+ _objc_msgSend$needsToAcquireBackgroundScheduler
+ _objc_msgSend$newContext
+ _objc_msgSend$newEmptyRegistration
+ _objc_msgSend$noteUIStatusForAllRecordsHaveChanged
+ _objc_msgSend$noteUIStatusForAllRecordsWithScopeIdentifierHaveChanged:
+ _objc_msgSend$noteUIStatusForAllScopesHaveChanged
+ _objc_msgSend$noteUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:
+ _objc_msgSend$noteUploadProgress:uploadType:forCloudScopedIdentifier:
+ _objc_msgSend$notifyAllObservers
+ _objc_msgSend$notifyObserver:
+ _objc_msgSend$notifyProgress:forScopeWithIdentifier:
+ _objc_msgSend$notifyProgress:forScopeWithIdentifier:fromSource:
+ _objc_msgSend$notifyRecordsUploadDidFinish
+ _objc_msgSend$notifyRecordsWithLocalScopedIdentifiersHaveStartedUploading:step:
+ _objc_msgSend$notifySyncActivityIsBlocked:
+ _objc_msgSend$notifySyncActivityIsBlocked:forSource:
+ _objc_msgSend$notifyUIStatusForAllRecordsHaveChanged
+ _objc_msgSend$notifyUIStatusForAllRecordsWithScopeIdentifiersHaveChanged:
+ _objc_msgSend$notifyUIStatusForAllScopesHaveChanged
+ _objc_msgSend$notifyUIStatusForRecordsWithLocalScopedIdentifiersHaveChanged:
+ _objc_msgSend$notifyUIStatusForScopesWithIdentifiersHaveChanged:
+ _objc_msgSend$notifyUIStatusScopeWithIdentifiers:isSynchronizing:
+ _objc_msgSend$notifyUploadProgressForRecordsWithLocalScopedIdentifiers:step:
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$observationCenter
+ _objc_msgSend$observationType
+ _objc_msgSend$observeAsyncCallOn:selector:timeout:block:
+ _objc_msgSend$observeAsyncCallWithFunction:timeout:block:
+ _objc_msgSend$observeSyncCallOn:selector:timeout:block:
+ _objc_msgSend$observeSyncCallWithFunction:timeout:block:
+ _objc_msgSend$observedEventDidChange
+ _objc_msgSend$observedEventWasFetchedExternally:registration:
+ _objc_msgSend$observedSourceDidDisconnect
+ _objc_msgSend$observer:didProgress:forScopeWithIdentifier:
+ _objc_msgSend$observer:didReceiveObservedEvent:
+ _objc_msgSend$observer:didStartSyncActivityForScopeWithIdentifier:
+ _objc_msgSend$observer:didStartSyncActivityOfType:
+ _objc_msgSend$observer:didStopSyncActivityForScopeWithIdentifier:
+ _objc_msgSend$observer:didStopSyncActivityOfType:
+ _objc_msgSend$observer:recordStatusesHaveChanged:
+ _objc_msgSend$observer:statusDidChange:forScopeWithIdentifier:
+ _objc_msgSend$observerDidDisconnectFromObservedSource:
+ _objc_msgSend$observerDidReceiveEventDidChange:
+ _objc_msgSend$observerDidStartTest:
+ _objc_msgSend$observerDidStopTest:
+ _objc_msgSend$observerManagerDidConnectToLibraryManager:
+ _objc_msgSend$observerManagerDidFailToConnectToLibraryManager:
+ _objc_msgSend$observerManagerWillConnectToLibraryManager:
+ _objc_msgSend$observerStatusDictionaries
+ _objc_msgSend$observerStatuses
+ _objc_msgSend$onTimeOutBlock
+ _objc_msgSend$openLibraryWithParameters:libraryIdentifier:libraryManagerType:completionHandler:
+ _objc_msgSend$parameters
+ _objc_msgSend$permanentError
+ _objc_msgSend$permanentErrorDateForScope:
+ _objc_msgSend$permanentErrorForScope:
+ _objc_msgSend$photosBundleIdentifier
+ _objc_msgSend$photosContainerIdentifier
+ _objc_msgSend$ping
+ _objc_msgSend$popNextBatchWithUUID:error:
+ _objc_msgSend$popProgressUpdates
+ _objc_msgSend$postIdentifier
+ _objc_msgSend$postScopedIdentifier
+ _objc_msgSend$pullUUID
+ _objc_msgSend$recordObservedSource:computeStatusesWithAccumulator:completionHandler:
+ _objc_msgSend$recoverDescription
+ _objc_msgSend$refreshObservedEventForObserver:completionHandler:
+ _objc_msgSend$refreshObservedEventForObserverWithIdentifier:completionHandler:
+ _objc_msgSend$registerObserver:withRegistration:completionHandler:
+ _objc_msgSend$registerObserverWithIdentifier:withRegistration:completionHandler:
+ _objc_msgSend$registeredObserverForObserver:
+ _objc_msgSend$registrationByAddingScopeIdentifiers:removingScopeIdentifiers:
+ _objc_msgSend$registrationByAddingScopedIdentifiers:removingScopedIdentifiers:
+ _objc_msgSend$registrationDidChange
+ _objc_msgSend$removeParticipants:fromSharedScopeWithIdentifier:completionHandler:
+ _objc_msgSend$removeParticipantsInShareTaskFromSharedScope:transportScope:share:userIdentifiersToRemove:participantIDsToRemove:completionHandler:
+ _objc_msgSend$replaceChangeWithChange:pushContext:error:
+ _objc_msgSend$reportingScopedIdentifier
+ _objc_msgSend$resetInitialSyncAnchorForScope:error:
+ _objc_msgSend$resetMainScopeStatus
+ _objc_msgSend$resourceTypeFromShortDescription:
+ _objc_msgSend$reverseMappingForLibraryOptions
+ _objc_msgSend$reverseMappingForOptions
+ _objc_msgSend$safeFilenames
+ _objc_msgSend$sandboxed
+ _objc_msgSend$schemaFilter
+ _objc_msgSend$scopeForStagingScope:
+ _objc_msgSend$scopeForUIObservingForScope:
+ _objc_msgSend$scopeIdentifierForUIObservation
+ _objc_msgSend$scopeObservedSource:getStatusesForScopesWithIdentifiers:synchronizingScopeWithIdentifiers:completionHandler:
+ _objc_msgSend$scopedIdentifiers
+ _objc_msgSend$scopedIdentifiersNeedingStatusesWithScopeIndexFinder:
+ _objc_msgSend$setAccountPartitionType:
+ _objc_msgSend$setAllowsAccessRequests:
+ _objc_msgSend$setAllowsAnonymousPublicAccess:
+ _objc_msgSend$setAllowsCancellingActiveDerivativesGeneration:
+ _objc_msgSend$setAssetCountPerTypeData:
+ _objc_msgSend$setBackgroundScheduler:
+ _objc_msgSend$setCanUseTurboMode:
+ _objc_msgSend$setCurrentRegistration:
+ _objc_msgSend$setDeleteDate:
+ _objc_msgSend$setDerivativeGeneratorClass:
+ _objc_msgSend$setFeatureDataclasses:completionHandler:
+ _objc_msgSend$setForceSyncDelegate:
+ _objc_msgSend$setHasChangesToDownload:
+ _objc_msgSend$setHasChangesToUpload:
+ _objc_msgSend$setIsExceedingLimit:
+ _objc_msgSend$setIsExceedingSharedLibraryLimit:
+ _objc_msgSend$setIsInResetSync:
+ _objc_msgSend$setIsPlaceholder:
+ _objc_msgSend$setIsSynchronizing:
+ _objc_msgSend$setLastSyncDate:
+ _objc_msgSend$setNTimeURL:
+ _objc_msgSend$setOnTimeOutBlock:
+ _objc_msgSend$setOverLimit:
+ _objc_msgSend$setOverQuota:
+ _objc_msgSend$setPermanentError:
+ _objc_msgSend$setPermanentError:onScopeWithIdentifier:completionHandler:
+ _objc_msgSend$setPersonsData:
+ _objc_msgSend$setPostIdentifier:
+ _objc_msgSend$setPostScopedIdentifier:
+ _objc_msgSend$setPullUUID:
+ _objc_msgSend$setScopeIdentifierForUIObservation:
+ _objc_msgSend$setSession:
+ _objc_msgSend$setShouldFetchExportedID:
+ _objc_msgSend$setShouldFetchReference:
+ _objc_msgSend$setShouldOrderRecordsBySize:
+ _objc_msgSend$setShouldUseCache:
+ _objc_msgSend$setSubscriptionDate:
+ _objc_msgSend$setSyncActivitySource:
+ _objc_msgSend$setUiUploadProgressHub:
+ _objc_msgSend$setUserLastViewedNotificationDate:
+ _objc_msgSend$sharedEPPContext
+ _objc_msgSend$shouldAutoActivateScopeWithIdentifier:scopeType:
+ _objc_msgSend$shouldBypassBackgroundScheduling
+ _objc_msgSend$shouldDisableUploadRate
+ _objc_msgSend$shouldDispatchDelegateCalls
+ _objc_msgSend$shouldFetchReference
+ _objc_msgSend$shouldProcessScope:optionalExcludedReason:inTransaction:
+ _objc_msgSend$shouldReportProgressToUI
+ _objc_msgSend$shouldSkipScopesWithPermanentError
+ _objc_msgSend$shouldTryToBypassBackgroundSchedulingDuringPullFromTransportForScope:
+ _objc_msgSend$shouldUseTurboMode
+ _objc_msgSend$sourceStatus
+ _objc_msgSend$sourceStatusDictionary
+ _objc_msgSend$startBypassingBackgroundSchedulingIfPossible
+ _objc_msgSend$startClientSession
+ _objc_msgSend$startObservingWithDelegate:completionHandler:
+ _objc_msgSend$startSyncActivity
+ _objc_msgSend$startSyncActivityForScopeIdentifier:
+ _objc_msgSend$startSyncActivityForScopeWithIdentifier:fromSource:
+ _objc_msgSend$startSyncActivityFromSource:
+ _objc_msgSend$startWatching
+ _objc_msgSend$statusDictionaryForObserver:
+ _objc_msgSend$statusForObserver:
+ _objc_msgSend$statuses
+ _objc_msgSend$stopBypassingBackgroundSchedulingIfPossible
+ _objc_msgSend$stopClientSession
+ _objc_msgSend$stopObservingWithCompletionHandler:
+ _objc_msgSend$stopSyncActivity
+ _objc_msgSend$stopSyncActivityForScopeIdentifier:
+ _objc_msgSend$stopSyncActivityForScopeWithIdentifier:fromSource:
+ _objc_msgSend$stopSyncActivityForSource:
+ _objc_msgSend$stopWatching
+ _objc_msgSend$storeLastSuccessfulSyncDateFromSyncSession:
+ _objc_msgSend$storeLastSyncDateFromSession:error:
+ _objc_msgSend$storePermanentError:forScope:error:
+ _objc_msgSend$storePermanentError:hasChanges:forScope:error:
+ _objc_msgSend$subCacheWithIdentifier:
+ _objc_msgSend$supportedFeatureVersion
+ _objc_msgSend$supportsRecordsOfClass:
+ _objc_msgSend$syncActivitySource
+ _objc_msgSend$syncActivitySource:isBlocked:
+ _objc_msgSend$syncActivitySource:isSynchronizing:scopeWithIdentifier:
+ _objc_msgSend$syncActivityType
+ _objc_msgSend$synthesizedEvent
+ _objc_msgSend$transportContainerConfiguration
+ _objc_msgSend$transportFilterPlistForTransportIdentifier:
+ _objc_msgSend$uiUploadProgressHub
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$underlyingManager
+ _objc_msgSend$unregisterObserver:completionHandler:
+ _objc_msgSend$unregisterObserverWithIdentifier:completionHandler:
+ _objc_msgSend$updateContainerConfiguration:
+ _objc_msgSend$updateContainerConfigurationIfNecessary:error:
+ _objc_msgSend$updateFeatureDataclasses:error:
+ _objc_msgSend$updateLastSuccessfulSyncDate:
+ _objc_msgSend$updateLibraryOptions:
+ _objc_msgSend$updateRegistration:forObserver:
+ _objc_msgSend$updateRegistration:forObserver:completionHandler:
+ _objc_msgSend$updateRegistration:forObserverWithIdentifier:completionHandler:
+ _objc_msgSend$updateStatusType:forScopedIdentifier:
+ _objc_msgSend$updateWithUploadProgresses:
+ _objc_msgSend$updatedNonUploadingStatuses
+ _objc_msgSend$updatedUploadingProgresses
+ _objc_msgSend$uploadChangeBatch:bypassLimits:allowsCancelling:completionHandler:
+ _objc_msgSend$userLastViewedNotificationDate
+ _objc_msgSend$usesBackgroundScheduling
+ _objc_msgSend$viewingMode
+ _objc_msgSend$willUploadCloudChange:forLocalChange:
+ _objc_msgSend$wipeStoreAtNextOpeningWithCloudLibraryStorageURL:reason:
+ _objc_msgSend$withObservedSourceOfType:block:
+ _objc_msgSend$zoneish
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x6
+ _objc_retain_x7
+ _propertiesForChangeType:.onceToken.18437
+ _propertiesForChangeType:.onceToken.185
+ _propertiesForChangeType:.onceToken.22481
+ _propertiesForChangeType:.onceToken.27781
+ _propertiesForChangeType:.properties.27783
+ _realpath$DARWIN_EXTSN
+ _reverseMappingForLibraryOptions.onceToken
+ _reverseMappingForLibraryOptions.reverseMapping
+ _reverseMappingForOptions.onceToken
+ _reverseMappingForOptions.reverseMapping
+ _serverSupportsProxyConflictResolution.onceToken
+ _serverSupportsProxyConflictResolution.serverSupportsProxyConflictResolution
- +[CPLAssetChange(DefaultsSupport) serverSupportsComputeState]
- +[CPLAssetChange(DefaultsSupport) serverSupportsDeletedByUserIdentifier]
- +[CPLAssetChange(DefaultsSupport) serverSupportsLastViewedDate]
- +[CPLAssetChange(DefaultsSupport) serverSupportsSharedLibrarySharingState]
- +[CPLAssetChange(DefaultsSupport) serverSupportsVision]
- +[CPLCommentChange supportsRecordModificationDate]
- +[CPLLibraryManager _reverseMappingForLibraryOptions]
- +[CPLLibraryManager allLibraryOptionsDescriptions]
- +[CPLLibraryManager descriptionForLibraryOptions:]
- +[CPLLibraryManager mappingForLibraryOptions]
- +[CPLLibraryManager optionsFromDescription:]
- +[CPLLibraryShareScopeChange(DefaultsSupport) serverSupportsLibraryShareSettingsRecordSyncing]
- +[CPLLibraryShareScopeChange(DefaultsSupport) serverSupportsLibraryShareSettingsUserViewedParticipantTrashNotificationDateSyncing]
- +[CPLReactChange(CPLPlaceholderRecord) relatedRecordClass]
- +[CPLScopeChange shouldAutoActivateScopeWithType:]
- +[CPLScopeChange supportsActivationOfScopeWithType:]
- +[CPLTextCommentChange(CPLPlaceholderRecord) relatedRecordClass]
- -[CPLBrokenScope .cxx_destruct]
- -[CPLBrokenScope _showAlertWithMessage:readMoreURL:createRadarURL:showsRecoverButton:]
- -[CPLBrokenScope alertMessage]
- -[CPLBrokenScope alertTitle]
- -[CPLBrokenScope alternateRecoverDescription]
- -[CPLBrokenScope brokenMessage]
- -[CPLBrokenScope brokenTitle]
- -[CPLBrokenScope createRadarButtonTitle]
- -[CPLBrokenScope createRadarURL]
- -[CPLBrokenScope engineLibrary]
- -[CPLBrokenScope engineScope]
- -[CPLBrokenScope hasEngineRecoveryMechanism]
- -[CPLBrokenScope initWithEngineScope:engineLibrary:]
- -[CPLBrokenScope internalRecoveryInstructions]
- -[CPLBrokenScope isInternal]
- -[CPLBrokenScope radarDescription]
- -[CPLBrokenScope radarTitle]
- -[CPLBrokenScope readMoreButtonTitle]
- -[CPLBrokenScope readMoreURL]
- -[CPLBrokenScope recoverButtonTitle]
- -[CPLBrokenScope recoverUsingEngineWithCompletionHandler:]
- -[CPLBrokenScope shouldShowAlertToUser]
- -[CPLBrokenScope showAlertToUser]
- -[CPLCallObserver initWithObject:selector:functionName:]
- -[CPLEngineChangePipe popNextBatchWithError:]
- -[CPLEngineCloudCache ackownledgeRecordWithScopedIdentifier:error:]
- -[CPLEngineComponentEnumerator initWithComponents:handler:]
- -[CPLEngineDerivativesCache _cacheKeyForReferenceResource:adjustments:includePosterFrame:]
- -[CPLEngineDerivativesCache _cachedResourcesForReferenceResource:adjustment:includePosterFrame:]
- -[CPLEngineDerivativesCache _cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:]
- -[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]
- -[CPLEngineForceSyncTask reallyCancel]
- -[CPLEngineForceSyncTask reallyLaunch]
- -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) allowsBackgroundDispatch]
- -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) allowsForcedTaskQueuing]
- -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) discardedError]
- -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) forcedTaskPriority]
- -[CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask) simpleDescription]
- -[CPLEngineLibrary hasSomeSharedCollections]
- -[CPLEngineLibrary initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:]
- -[CPLEngineLibrary setHasSomeSharedCollections:]
- -[CPLEngineLibrary updateLastSuccessfullSyncDate:]
- -[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:completionHandler:]
- -[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]
- -[CPLEngineMultiscopeSyncTask shouldProcessScope:inTransaction:]
- -[CPLEngineMultiscopeSyncTask shouldStartTaskInTransaction:]
- -[CPLEngineScheduler _writeFirstSynchronizationMarker]
- -[CPLEngineScopeStorage shouldAutoactivateScopeWithIdentifier:scopeType:]
- -[CPLEngineStore blockWriteTransactionsWithCompletionHandler:]
- -[CPLEngineSystemMonitor canBoostBackgroundOperations]
- -[CPLEngineSystemMonitor canBoostOperations]
- -[CPLEngineTransport acquireReschedulerTaskWithCompletionHandler:]
- -[CPLEngineTransport createGroupForAcceptingLibraryShare]
- -[CPLEngineTransport createGroupForAcceptingMomentShare]
- -[CPLEngineTransport createGroupForFetchingLibraryShare]
- -[CPLEngineTransport createGroupForFetchingMomentShare]
- -[CPLEngineTransport createGroupForPublishingLibraryShare]
- -[CPLEngineTransport createGroupForPublishingMomentShare]
- -[CPLEngineTransport createGroupForThumbnailPrefetch]
- -[CPLEngineTransport dropPersistedInitialSyncSession]
- -[CPLEngineTransport findPersistedInitialSyncSession:completionHandler:]
- -[CPLEngineTransport getBackgroundSchedulingStatusDictionaryWithCompletionHandler:]
- -[CPLEngineTransport getBackgroundSchedulingStatusWithCompletionHandler:]
- -[CPLEngineTransport getSystemBudgetsWithCompletionHandler:]
- -[CPLEngineTransport noteClientIsBeginningSignificantWork]
- -[CPLEngineTransport noteClientIsEndingSignificantWork]
- -[CPLEngineTransport setShouldOverride:forSystemBudgets:]
- -[CPLLibraryManager initForManagement]
- -[CPLLibraryManager initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:]
- -[CPLLibraryManager initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:options:]
- -[CPLMingleChangesTask shouldProcessScope:inTransaction:]
- -[CPLProxyLibraryManager _dropConnectionCompletlyLocked]
- -[CPLProxyLibraryManager _dropConnectionCompletly]
- -[CPLProxyLibraryManager acceptSharedScope:completionHandler:]
- -[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]
- -[CPLProxyLibraryManager getStatusForComponents:completionHandler:]
- -[CPLPushSessionTracker checkScopeIdentifier:]
- -[CPLRecordChange originalResourceSize]
- -[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:]
- -[CPLScopeChange defaultFlags]
- -[CPLScopeUpdateTask shouldProcessScope:inTransaction:]
- -[CPLSocialGroupChange setPersonData:]
- -[CPLStatus hasSomeSharedCollections]
- -[CPLStatus setHasSomeSharedCollections:]
- -[CPLSyncSession needsToAcquireRescheduler]
- -[CPLSyncSession rescheduler]
- -[CPLSyncSession setRescheduler:]
- -[CPLSyncSessionBlockedState initWithRescheduler:blocked:syncHasBeenRequested:runtimeCharacteristics:]
- -[CPLSyncSessionBlockedState rescheduler]
- -[CPLUploadPushedChangesTask _discardGenerateDerivativesProgress]
- -[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]
- -[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]
- -[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]
- -[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]
- -[CPLUploadPushedChangesTask _popNextBatchAndContinue]
- -[CPLUploadPushedChangesTask _prepareTransportGroupForOneBatch]
- -[CPLUploadPushedChangesTask _updateQuotaStrategyAfterSuccessInTransaction:]
- -[CPLUploadPushedChangesTask observeValueForKeyPath:ofObject:change:context:]
- -[NSError(CPLAdditions) cplUnderlyingError]
- GCC_except_table1011
- GCC_except_table1013
- GCC_except_table1186
- GCC_except_table1235
- GCC_except_table1239
- GCC_except_table1244
- GCC_except_table1246
- GCC_except_table1256
- GCC_except_table1263
- GCC_except_table1266
- GCC_except_table1269
- GCC_except_table1275
- GCC_except_table1277
- GCC_except_table1358
- GCC_except_table140
- GCC_except_table1444
- GCC_except_table148
- GCC_except_table150
- GCC_except_table161
- GCC_except_table168
- GCC_except_table183
- GCC_except_table1992
- GCC_except_table207
- GCC_except_table2099
- GCC_except_table21
- GCC_except_table2107
- GCC_except_table2148
- GCC_except_table222
- GCC_except_table2236
- GCC_except_table2243
- GCC_except_table228
- GCC_except_table231
- GCC_except_table233
- GCC_except_table235
- GCC_except_table2386
- GCC_except_table2479
- GCC_except_table26
- GCC_except_table2715
- GCC_except_table2717
- GCC_except_table2803
- GCC_except_table2813
- GCC_except_table2869
- GCC_except_table2871
- GCC_except_table2991
- GCC_except_table3015
- GCC_except_table3092
- GCC_except_table3096
- GCC_except_table3098
- GCC_except_table3100
- GCC_except_table3104
- GCC_except_table3222
- GCC_except_table324
- GCC_except_table3269
- GCC_except_table3513
- GCC_except_table3582
- GCC_except_table3586
- GCC_except_table3588
- GCC_except_table3597
- GCC_except_table374
- GCC_except_table383
- GCC_except_table3877
- GCC_except_table3907
- GCC_except_table3934
- GCC_except_table3951
- GCC_except_table3958
- GCC_except_table3966
- GCC_except_table3968
- GCC_except_table3982
- GCC_except_table3984
- GCC_except_table3987
- GCC_except_table4320
- GCC_except_table4364
- GCC_except_table4454
- GCC_except_table446
- GCC_except_table4464
- GCC_except_table450
- GCC_except_table4521
- GCC_except_table4524
- GCC_except_table4699
- GCC_except_table4707
- GCC_except_table478
- GCC_except_table4787
- GCC_except_table4791
- GCC_except_table4797
- GCC_except_table4804
- GCC_except_table481
- GCC_except_table4819
- GCC_except_table4820
- GCC_except_table4826
- GCC_except_table4870
- GCC_except_table4878
- GCC_except_table49
- GCC_except_table4938
- GCC_except_table4940
- GCC_except_table4942
- GCC_except_table4954
- GCC_except_table498
- GCC_except_table499
- GCC_except_table508
- GCC_except_table5096
- GCC_except_table5138
- GCC_except_table5147
- GCC_except_table5148
- GCC_except_table5207
- GCC_except_table5210
- GCC_except_table526
- GCC_except_table5290
- GCC_except_table5292
- GCC_except_table5327
- GCC_except_table535
- GCC_except_table5493
- GCC_except_table5521
- GCC_except_table5563
- GCC_except_table5583
- GCC_except_table5609
- GCC_except_table5620
- GCC_except_table5641
- GCC_except_table5661
- GCC_except_table5665
- GCC_except_table5691
- GCC_except_table5723
- GCC_except_table5763
- GCC_except_table5824
- GCC_except_table5865
- GCC_except_table5878
- GCC_except_table5889
- GCC_except_table5896
- GCC_except_table5949
- GCC_except_table6074
- GCC_except_table6087
- GCC_except_table6090
- GCC_except_table638
- GCC_except_table644
- GCC_except_table6570
- GCC_except_table6609
- GCC_except_table6613
- GCC_except_table6615
- GCC_except_table6630
- GCC_except_table6636
- GCC_except_table6644
- GCC_except_table6654
- GCC_except_table6662
- GCC_except_table6665
- GCC_except_table6685
- GCC_except_table6692
- GCC_except_table6715
- GCC_except_table675
- GCC_except_table6750
- GCC_except_table6781
- GCC_except_table679
- GCC_except_table6812
- GCC_except_table6815
- GCC_except_table6817
- GCC_except_table6819
- GCC_except_table682
- GCC_except_table684
- GCC_except_table6850
- GCC_except_table687
- GCC_except_table689
- GCC_except_table6905
- GCC_except_table693
- GCC_except_table695
- GCC_except_table704
- GCC_except_table7051
- GCC_except_table706
- GCC_except_table7073
- GCC_except_table708
- GCC_except_table710
- GCC_except_table7103
- GCC_except_table712
- GCC_except_table714
- GCC_except_table716
- GCC_except_table718
- GCC_except_table720
- GCC_except_table722
- GCC_except_table724
- GCC_except_table726
- GCC_except_table7282
- GCC_except_table7291
- GCC_except_table7296
- GCC_except_table7312
- GCC_except_table7326
- GCC_except_table733
- GCC_except_table7336
- GCC_except_table7341
- GCC_except_table735
- GCC_except_table737
- GCC_except_table739
- GCC_except_table741
- GCC_except_table7423
- GCC_except_table750
- GCC_except_table752
- GCC_except_table7521
- GCC_except_table7530
- GCC_except_table754
- GCC_except_table756
- GCC_except_table758
- GCC_except_table7586
- GCC_except_table7612
- GCC_except_table7634
- GCC_except_table7642
- GCC_except_table7664
- GCC_except_table7674
- GCC_except_table778
- GCC_except_table784
- GCC_except_table802
- GCC_except_table814
- GCC_except_table907
- GCC_except_table993
- _CFRelease
- _CFUserNotificationCreate
- _CFUserNotificationReceiveResponse
- _CPLAppBundleIdentifierForContainerIdentifier
- _CPLContainerIdentifierForLibraryIdentifier
- _CPLSharedCollectionPrefixForTracking
- _OBJC_CLASS_$_CPLBrokenScope
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSURLQueryItem
- _OBJC_IVAR_$_CPLBeforeUploadCheckItems._items
- _OBJC_IVAR_$_CPLBrokenScope._engineLibrary
- _OBJC_IVAR_$_CPLBrokenScope._engineScope
- _OBJC_IVAR_$_CPLBrokenScope._internal
- _OBJC_IVAR_$_CPLBrokenScope._lastShownAlertDate
- _OBJC_IVAR_$_CPLBrokenScope._queue
- _OBJC_IVAR_$_CPLBrokenScope._shouldShowAlertToUser
- _OBJC_IVAR_$_CPLEngineLibrary._clientLibraryBaseURL
- _OBJC_IVAR_$_CPLEngineLibrary._cloudLibraryResourceStorageURL
- _OBJC_IVAR_$_CPLEngineLibrary._cloudLibraryStateStorageURL
- _OBJC_IVAR_$_CPLEngineLibrary._libraryIdentifier
- _OBJC_IVAR_$_CPLEngineLibrary._libraryOptions
- _OBJC_IVAR_$_CPLEngineLibrary._mainScopeIdentifier
- _OBJC_IVAR_$_CPLEngineMultiscopeSyncTask._currentTaskQueue
- _OBJC_IVAR_$_CPLEngineSystemMonitor._allowBackgroundOperationsBoost
- _OBJC_IVAR_$_CPLEngineSystemMonitor._allowOperationsBoost
- _OBJC_IVAR_$_CPLExtractedBatch._mutableUntrustableScopedIndentifiers
- _OBJC_IVAR_$_CPLLibraryManager._clientLibraryBaseURL
- _OBJC_IVAR_$_CPLLibraryManager._cloudLibraryResourceStorageURL
- _OBJC_IVAR_$_CPLLibraryManager._cloudLibraryStateStorageURL
- _OBJC_IVAR_$_CPLLibraryManager._libraryOptions
- _OBJC_IVAR_$_CPLLibraryManager._mainScopeIdentifier
- _OBJC_IVAR_$_CPLSyncSession._rescheduler
- _OBJC_IVAR_$_CPLSyncSessionBlockedState._rescheduler
- _OBJC_IVAR_$_CPLTransportUpdateScopeTask._deleteTask
- _OBJC_IVAR_$_CPLTransportUpdateScopeTask._updateTask
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._acquireReschedulerTask
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._derivativesSizeReportTimer
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._derivativesSizeToReport
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesCancellationHandler
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesChange
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesDeferredHandler
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesLastFractionCompleted
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesProgress
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._generateDerivativesTotalSize
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._resetStrategy
- _OBJC_IVAR_$_CPLUploadPushedChangesTask._shouldCheckAssetsWithServerWhenOverQuota
- _OBJC_METACLASS_$_CPLBrokenScope
- _OUTLINED_FUNCTION_126
- _OUTLINED_FUNCTION_127
- _OUTLINED_FUNCTION_128
- _OUTLINED_FUNCTION_129
- _OUTLINED_FUNCTION_130
- _OUTLINED_FUNCTION_131
- _OUTLINED_FUNCTION_132
- _OUTLINED_FUNCTION_133
- _OUTLINED_FUNCTION_134
- __ClassesForInitialQueries
- __OBJC_$_CLASS_METHODS_CPLLibraryShareScopeChange(DefaultsSupport|CPLNSCoding)
- __OBJC_$_CLASS_METHODS_CPLReactChange(CPLIDMapping|CPLPlaceholderRecord)
- __OBJC_$_CLASS_METHODS_CPLTextCommentChange(CPLIDMapping|CPLPlaceholderRecord)
- __OBJC_$_INSTANCE_METHODS_CPLBrokenScope
- __OBJC_$_INSTANCE_METHODS_CPLCommentChange
- __OBJC_$_INSTANCE_METHODS_CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask)
- __OBJC_$_INSTANCE_METHODS_CPLReactChange(CPLIDMapping|CPLPlaceholderRecord)
- __OBJC_$_INSTANCE_METHODS_CPLSyncSession
- __OBJC_$_INSTANCE_METHODS_CPLTextCommentChange(CPLIDMapping|CPLPlaceholderRecord)
- __OBJC_$_INSTANCE_VARIABLES_CPLBrokenScope
- __OBJC_$_PROP_LIST_CPLSyncSession
- __OBJC_CLASS_PROTOCOLS_$_CPLEngineForceSyncTask(CPLEngineSyncManagerForcedTask)
- __OBJC_CLASS_PROTOCOLS_$_CPLLibraryShareScopeChange(DefaultsSupport|CPLNSCoding)
- __OBJC_CLASS_PROTOCOLS_$_CPLSyncSession
- __OBJC_CLASS_RO_$_CPLBrokenScope
- __OBJC_METACLASS_RO_$_CPLBrokenScope
- ___105-[CPLLibraryManager startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.418
- ___110-[CPLLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.332
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.64
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.70
- ___112-[CPLEngineDerivativesCache generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.71
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.45
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.49
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke.60
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.54
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_2.61
- ___113-[CPLEngineDerivativesCache _generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:]_block_invoke_3.62
- ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.60
- ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.63
- ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke.65
- ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke_2.61
- ___114-[CPLScopeUpdateScopeTask _updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:]_block_invoke_2.64
- ___115-[CPLLibraryManager removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:]_block_invoke.423
- ___115-[CPLProxyLibraryManager beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:]_block_invoke.324
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke.146
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_2
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_2.154
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_3
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_3.155
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_4
- ___116-[CPLUploadPushedChangesTask _generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:]_block_invoke_5
- ___120-[CPLLibraryManager getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:]_block_invoke.338
- ___122-[CPLLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.508
- ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke.371
- ___127-[CPLProxyLibraryManager fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:]_block_invoke_2.372
- ___136-[CPLScopeUpdateScopeTask _updateScopeWithNewScopeType:updatedScopeChange:updatedFlags:oldTransportScope:session:updatedTransportScope:]_block_invoke.56
- ___155-[CPLLibraryManager initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:]_block_invoke
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.173
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.180
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.182
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.183
- ___160-[CPLEngineResourceDownloadQueue _downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:]_block_invoke.185
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.206
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.208
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.207
- ___163-[CPLEngineResourceDownloadQueue _realDownloadTaskForLocalResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.209
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.196
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.198
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.201
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.202
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke.204
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.203
- ___165-[CPLEngineResourceDownloadQueue _resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:]_block_invoke_2.205
- ___29-[CPLSyncSession rescheduler]_block_invoke
- ___33-[CPLBrokenScope showAlertToUser]_block_invoke
- ___33-[CPLSyncSession setRescheduler:]_block_invoke
- ___35+[CPLFingerprintScheme supportsEPP]_block_invoke
- ___36-[CPLEngineLibrary startSyncSession]_block_invoke.51
- ___36-[CPLEngineLibrary startSyncSession]_block_invoke.52
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.44
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.49
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke.55
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.50
- ___36-[CPLPushSessionTracker computeDiff]_block_invoke_2.58
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.120
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.121
- ___37-[CPLStatus hasSomeSharedCollections]_block_invoke
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke.9
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_2.14
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_3.15
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_6
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_7
- ___37-[CPLTransportUpdateScopeTask launch]_block_invoke_8
- ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.193
- ___38-[CPLEngineForceSyncTask reallyCancel]_block_invoke
- ___38-[CPLEngineForceSyncTask reallyLaunch]_block_invoke
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.91
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.93
- ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke.151
- ___41-[CPLStatus setHasSomeSharedCollections:]_block_invoke
- ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.79
- ___42-[CPLEngineLibrary performBlockOnLibrary:]_block_invoke.80
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.153
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke.154
- ___42-[CPLEngineScheduler _prepareFirstSession]_block_invoke_2.155
- ___42-[CPLLibraryManager discardCurrentSession]_block_invoke.297
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.270
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.271
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.277
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.278
- ___42-[CPLProxyLibraryManager _setupConnection]_block_invoke.279
- ___42-[CPLScopeUpdateScopeTask _getLibraryInfo]_block_invoke.67
- ___43-[CPLRecordChange propertiesForChangeType:]_block_invoke.159
- ___43-[CPLSyncSession needsToAcquireRescheduler]_block_invoke
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.281
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.284
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.288
- ___45+[CPLFingerprintScheme supportsEPPAutoEnable]_block_invoke
- ___45+[CPLLibraryManager mappingForLibraryOptions]_block_invoke
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.204
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.208
- ___47-[CPLLibraryManager openWithCompletionHandler:]_block_invoke.211
- ___47-[CPLScopeUpdateScopeTask _fetchTransportScope]_block_invoke.69
- ___47-[CPLScopeUpdateScopeTask _fetchTransportScope]_block_invoke_2
- ___47-[CPLScopeUpdateScopeTask _fetchTransportScope]_block_invoke_2.70
- ___47-[CPLScopeUpdateScopeTask _fetchTransportScope]_block_invoke_3
- ___47-[CPLScopeUpdateScopeTask _fetchTransportScope]_block_invoke_3.71
- ___47-[NSObject(CPLCodingProxy) cplClearProperties:]_block_invoke.132
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.290
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.291
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.292
- ___49-[CPLProxyLibraryManager _dispatchBlockWhenOpen:]_block_invoke.295
- ___50+[CPLArchiver displayableDictionaryForDictionary:]_block_invoke.1705
- ___50+[CPLLibraryManager descriptionForLibraryOptions:]_block_invoke
- ___50-[CPLProxyLibraryManager _dropConnectionCompletly]_block_invoke
- ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.341
- ___51-[CPLLibraryManager createScope:completionHandler:]_block_invoke.348
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.70
- ___52-[CPLEngineSyncManager _launchForcedTaskIfNecessary]_block_invoke.275
- ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke.231
- ___52-[CPLEngineSyncManager resetTransportUserIdentifier]_block_invoke_2.234
- ___52-[CPLEngineSystemMonitor openWithCompletionHandler:]_block_invoke.14
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.303
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.305
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.306
- ___52-[CPLProxyLibraryManager openWithCompletionHandler:]_block_invoke.cold.1
- ___53+[CPLLibraryManager _reverseMappingForLibraryOptions]_block_invoke
- ___53+[CPLLibraryManager _reverseMappingForLibraryOptions]_block_invoke_2
- ___53-[CPLProxyLibraryManager closeWithCompletionHandler:]_block_invoke.307
- ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.98
- ___54-[CPLEngineSystemMonitor canBoostBackgroundOperations]_block_invoke
- ___54-[CPLLibraryManager forceBackupWithCompletionHandler:]_block_invoke.493
- ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_2.47
- ___54-[CPLProcessStagedScopesScopeTask _startActualCleanup]_block_invoke_3.48
- ___55+[CPLResource resourceTypesThatCountAgainstiCloudQuota]_block_invoke
- ___55-[CPLEngineLibrary attachObject:withCompletionHandler:]_block_invoke.66
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.134
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.137
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.135
- ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.22
- ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.25
- ___55-[CPLPushSessionTracker computeExpandedBatchWithError:]_block_invoke.33
- ___55-[CPLSyncSessionPredictor removePredictedValueForType:]_block_invoke.63
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.167
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.174
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.176
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.177
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.178
- ___56-[CPLCallObserver initWithObject:selector:functionName:]_block_invoke
- ___56-[CPLEngineStore _closeAndDeactivate:completionHandler:]_block_invoke.328
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke.286
- ___56-[CPLEngineSyncManager _setupTaskWithCompletionHandler:]_block_invoke_2.288
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.116
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.117
- ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.144
- ___56-[CPLUploadComputeStatesScopeTask _dropAllComputeStates]_block_invoke.58
- ___56-[CPLUploadComputeStatesScopeTask _uploadExtractedBatch]_block_invoke.9
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.107
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.115
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.121
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.127
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.133
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.139
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.146
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.151
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.157
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.163
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.169
- ___57+[CPLEngineSyncManager stepForState:syncManager:session:]_block_invoke.175
- ___57-[CPLEngineSyncManager setSyncSessionShouldBeForeground:]_block_invoke.242
- ___57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke.436
- ___57-[CPLLibraryManager acceptSharedScope:completionHandler:]_block_invoke_2
- ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.40
- ___57-[CPLUploadComputeStatesScopeTask _getNextBatchAndUpload]_block_invoke.46
- ___57-[CPLUploadPushedChangesTask _uploadBatchWithFetchCache:]_block_invoke.100
- ___58-[CPLEngineLibrary _requestUpdateOfMainScopeFromTransport]_block_invoke.44
- ___58-[CPLEngineSystemMonitor _permanentDataOverrideHasChanged]_block_invoke.210
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.216
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.217
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke.218
- ___58-[CPLLibraryManager _closeDeactivating:completionHandler:]_block_invoke_2.219
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.308
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.309
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke.311
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.310
- ___58-[CPLProxyLibraryManager deactivateWithCompletionHandler:]_block_invoke_2.312
- ___58-[CPLProxyLibraryManager noteClientIsInForegroundQuietly:]_block_invoke.342
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.27
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke.29
- ___58-[CPLUploadComputeStatesScopeTask _requestMissingPayloads]_block_invoke_2.28
- ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.95
- ___59-[CPLEngineLibrary provideCloudResource:completionHandler:]_block_invoke.96
- ___59-[CPLEngineResourceDownloadQueue initWithEngineStore:name:]_block_invoke.132
- ___59-[CPLLibraryManager updateShareForScope:completionHandler:]_block_invoke.350
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.105
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.106
- ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.200
- ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke.89
- ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke_2.90
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.22
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.30
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.50
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke.52
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke_2.31
- ___61-[CPLUploadPushedChangesTask _checkPrioritiesWithFetchCache:]_block_invoke_2.53
- ___62-[CPLProxyLibraryManager acceptSharedScope:completionHandler:]_block_invoke
- ___62-[CPLProxyLibraryManager acceptSharedScope:completionHandler:]_block_invoke_2
- ___62-[CPLProxyLibraryManager acceptSharedScope:completionHandler:]_block_invoke_3
- ___62-[CPLProxyLibraryManager acceptSharedScope:completionHandler:]_block_invoke_4
- ___62-[CPLProxyLibraryManager acceptSharedScope:completionHandler:]_block_invoke_5
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.118
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.120
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.121
- ___62-[CPLSyncSessionPredictor updatePredictionWithValuesAndTypes:]_block_invoke.60
- ___64-[CPLEngineQuarantinedRecords _quarantineRejectedRecords:error:]_block_invoke.42
- ___64-[CPLEngineQuarantinedRecords _quarantineRejectedRecords:error:]_block_invoke.47
- ___65-[CPLLibraryManager sharedLibraryRampCheckWithCompletionHandler:]_block_invoke.427
- ___66-[CPLLibraryManager refreshScopeWithIdentifier:completionHandler:]_block_invoke.365
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.193
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke.196
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.194
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_2.197
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.195
- ___67-[CPLEngineLibrary performMaintenanceCleanupWithCompletionHandler:]_block_invoke_3.198
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.133
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.134
- ___67-[CPLEngineScheduler _noteSyncSession:failedDuringPhase:withError:]_block_invoke.135
- ___67-[CPLEngineSystemMonitor getStatusDictionaryWithCompletionHandler:]_block_invoke.128
- ___67-[CPLEngineSystemMonitor getStatusDictionaryWithCompletionHandler:]_block_invoke.142
- ___67-[CPLProxyLibraryManager getStatusForComponents:completionHandler:]_block_invoke
- ___67-[CPLProxyLibraryManager getStatusForComponents:completionHandler:]_block_invoke_2
- ___67-[CPLProxyLibraryManager getStatusForComponents:completionHandler:]_block_invoke_2.cold.1
- ___67-[CPLProxyLibraryManager getStatusForComponents:completionHandler:]_block_invoke_3
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.112
- ___68-[CPLEngineScheduler _handleResetAnchorWithError:completionHandler:]_block_invoke.119
- ___68-[CPLLibraryManager fetchSharedScopeFromShareURL:completionHandler:]_block_invoke.432
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.76
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.81
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke.82
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_2.83
- ___68-[CPLUploadPushedChangesTask _extractBatchWithTransaction:andStore:]_block_invoke_3.84
- ___68-[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]_block_invoke
- ___68-[CPLUploadPushedChangesTask _finishReportingDerivativesIsNecessary]_block_invoke_2
- ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.52
- ___69-[CPLProcessStagedScopesScopeTask _checkDestinationAndProcessCleanup]_block_invoke.61
- ___70-[CPLScopeUpdateScopeTask _markScopeAsDeletedAndSucceedTaskWithFlags:]_block_invoke.41
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.105
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.106
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.111
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.117
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.112
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_2.118
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.115
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_3.119
- ___71-[CPLEngineLibrary requestClientToPushAllChangesWithCompletionHandler:]_block_invoke_4.116
- ___72-[CPLLibraryManager deleteScopeWithIdentifier:forced:completionHandler:]_block_invoke.361
- ___72-[CPLLibraryManager requestClientToPushAllChangesWithCompletionHandler:]_block_invoke.497
- ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke.55
- ___72-[CPLUploadComputeStatesScopeTask _discardExtractedBatchAndGetNextBatch]_block_invoke_2.57
- ___74-[CPLEngineScheduler _handleResetGlobalAnchorWithError:completionHandler:]_block_invoke.123
- ___74-[CPLLibraryManager fetchExistingSharedLibraryScopeWithCompletionHandler:]_block_invoke.440
- ___76-[CPLEngineLibrary provideRecordWithCloudScopeIdentifier:completionHandler:]_block_invoke.94
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_2
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_3
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_4
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_5
- ___76-[CPLEngineLibrary(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke_6
- ___76-[CPLLibraryManager queryUserDetailsForShareParticipants:completionHandler:]_block_invoke.445
- ___76-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:]_block_invoke
- ___76-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:]_block_invoke.10
- ___76-[CPLRecordStorageView(CPLClientCacheView) compactedBatchFromExpandedBatch:]_block_invoke.8
- ___77-[CPLLibraryManager(CPLManagement) getStatusForComponents:completionHandler:]_block_invoke
- ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke
- ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke_2
- ___77-[CPLUploadPushedChangesTask _installGenerateDerivativesCancellationHandler:]_block_invoke_3
- ___77-[CPLUploadPushedChangesTask observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___77-[NSObject(CPLCodingProxy) _cplCopyProperties:fromOtherObject:withCopyBlock:]_block_invoke.140
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.159
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke.166
- ___78-[CPLEngineLibrary forceBackupWithActivity:forceClientPush:completionHandler:]_block_invoke_2.163
- ___78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke
- ___78-[CPLLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.448
- ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke.66
- ___78-[CPLUploadComputeStatesScopeTask _uploadComputeStatesTaskDidFinishWithError:]_block_invoke_2.67
- ___79-[CPLEngineLibrary provideScopeChangeForScopeWithIdentifier:completionHandler:]_block_invoke.93
- ___79-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:completionHandler:]_block_invoke
- ___79-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:completionHandler:]_block_invoke_2
- ___79-[CPLEngineLibrary(CPLManagement) _fillStatus:forComponents:completionHandler:]_block_invoke_3
- ___79-[CPLLibraryManager checkHasBackgroundDownloadOperationsWithCompletionHandler:]_block_invoke.470
- ___80-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:withError:]_block_invoke
- ___80-[CPLEngineCloudCache cloudChangeBatchFromBatch:usingMapping:isFinal:withError:]_block_invoke.35
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.146
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.149
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke.153
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.147
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_2.154
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.148
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_3.155
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_4.156
- ___80-[CPLEngineLibrary requestScopesWithIdentifiersToBeActivated:completionHandler:]_block_invoke_5.157
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.126
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.138
- ___82-[CPLLibraryManager rampingRequestForResourceType:numRequested:completionHandler:]_block_invoke.342
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke.351
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke_2
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke_2.cold.1
- ___83-[CPLProxyLibraryManager forceSynchronizingScopeWithIdentifiers:completionHandler:]_block_invoke_3
- ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.302
- ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke.89
- ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_2.90
- ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_3.91
- ___85-[CPLEngineLibrary providePayloadForComputeStates:inFolderWithURL:completionHandler:]_block_invoke_4.92
- ___86-[CPLBrokenScope _showAlertWithMessage:readMoreURL:createRadarURL:showsRecoverButton:]_block_invoke
- ___86-[CPLBrokenScope _showAlertWithMessage:readMoreURL:createRadarURL:showsRecoverButton:]_block_invoke_2
- ___86-[CPLLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.344
- ___87-[CPLLibraryManager requestClientToPullAllChangesInScopeIdentifiers:completionHandler:]_block_invoke.501
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.170
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.181
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke.187
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.171
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.176
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.182
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_2.188
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_3.178
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_3.185
- ___88-[CPLEngineLibrary forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:]_block_invoke_4.179
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.123
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.129
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke.137
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.124
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.130
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_2.138
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.125
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.136
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_3.139
- ___88-[CPLEngineLibrary requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:]_block_invoke_4.140
- ___90-[CPLUploadPushedChangesTask _generateNeededDerivativesWithFetchCache:fingerprintContext:]_block_invoke
- ___90-[CPLUploadPushedChangesTask _generateNeededDerivativesWithFetchCache:fingerprintContext:]_block_invoke_2
- ___90-[CPLUploadPushedChangesTask _generateNeededDerivativesWithFetchCache:fingerprintContext:]_block_invoke_3
- ___91-[CPLProxyLibraryManager beginInMemoryDownloadOfResource:clientBundleID:completionHandler:]_block_invoke.332
- ___92-[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]_block_invoke
- ___92-[CPLUploadPushedChangesTask _generatingDerivativesForChange:fractionCompleted:chunkLength:]_block_invoke_2
- ___Block_byref_object_copy_.10061
- ___Block_byref_object_copy_.1013
- ___Block_byref_object_copy_.11294
- ___Block_byref_object_copy_.11589
- ___Block_byref_object_copy_.1181
- ___Block_byref_object_copy_.12362
- ___Block_byref_object_copy_.13218
- ___Block_byref_object_copy_.1344
- ___Block_byref_object_copy_.13805
- ___Block_byref_object_copy_.14136
- ___Block_byref_object_copy_.14322
- ___Block_byref_object_copy_.15151
- ___Block_byref_object_copy_.15762
- ___Block_byref_object_copy_.16486
- ___Block_byref_object_copy_.16809
- ___Block_byref_object_copy_.17283
- ___Block_byref_object_copy_.1734
- ___Block_byref_object_copy_.17889
- ___Block_byref_object_copy_.18717
- ___Block_byref_object_copy_.20183
- ___Block_byref_object_copy_.20322
- ___Block_byref_object_copy_.2046
- ___Block_byref_object_copy_.20812
- ___Block_byref_object_copy_.21397
- ___Block_byref_object_copy_.21883
- ___Block_byref_object_copy_.22218
- ___Block_byref_object_copy_.23224
- ___Block_byref_object_copy_.23527
- ___Block_byref_object_copy_.24331
- ___Block_byref_object_copy_.2535
- ___Block_byref_object_copy_.2613
- ___Block_byref_object_copy_.2902
- ___Block_byref_object_copy_.3256
- ___Block_byref_object_copy_.344
- ___Block_byref_object_copy_.5794
- ___Block_byref_object_copy_.6497
- ___Block_byref_object_copy_.6664
- ___Block_byref_object_copy_.677
- ___Block_byref_object_copy_.7322
- ___Block_byref_object_copy_.7661
- ___Block_byref_object_copy_.7961
- ___Block_byref_object_copy_.8399
- ___Block_byref_object_copy_.883
- ___Block_byref_object_copy_.9815
- ___Block_byref_object_dispose_.10062
- ___Block_byref_object_dispose_.1014
- ___Block_byref_object_dispose_.11295
- ___Block_byref_object_dispose_.11590
- ___Block_byref_object_dispose_.1182
- ___Block_byref_object_dispose_.12363
- ___Block_byref_object_dispose_.13219
- ___Block_byref_object_dispose_.1345
- ___Block_byref_object_dispose_.13806
- ___Block_byref_object_dispose_.14137
- ___Block_byref_object_dispose_.14323
- ___Block_byref_object_dispose_.15152
- ___Block_byref_object_dispose_.15763
- ___Block_byref_object_dispose_.16487
- ___Block_byref_object_dispose_.16810
- ___Block_byref_object_dispose_.17284
- ___Block_byref_object_dispose_.1735
- ___Block_byref_object_dispose_.17890
- ___Block_byref_object_dispose_.18718
- ___Block_byref_object_dispose_.20184
- ___Block_byref_object_dispose_.20323
- ___Block_byref_object_dispose_.2047
- ___Block_byref_object_dispose_.20813
- ___Block_byref_object_dispose_.21398
- ___Block_byref_object_dispose_.21884
- ___Block_byref_object_dispose_.22219
- ___Block_byref_object_dispose_.23225
- ___Block_byref_object_dispose_.23528
- ___Block_byref_object_dispose_.24332
- ___Block_byref_object_dispose_.2536
- ___Block_byref_object_dispose_.2614
- ___Block_byref_object_dispose_.2903
- ___Block_byref_object_dispose_.3257
- ___Block_byref_object_dispose_.345
- ___Block_byref_object_dispose_.5795
- ___Block_byref_object_dispose_.6498
- ___Block_byref_object_dispose_.6665
- ___Block_byref_object_dispose_.678
- ___Block_byref_object_dispose_.7323
- ___Block_byref_object_dispose_.7662
- ___Block_byref_object_dispose_.7962
- ___Block_byref_object_dispose_.8400
- ___Block_byref_object_dispose_.884
- ___Block_byref_object_dispose_.9816
- ___CPLConfigurationOSLogDomain.19546
- ___CPLConfigurationOSLogDomain.onceToken.19552
- ___CPLConfigurationOSLogDomain.result.19554
- ___CPLSchedulerOSLogDomain.7603
- ___CPLSchedulerOSLogDomain.onceToken.7604
- ___CPLSchedulerOSLogDomain.result.7605
- ___CPLSessionOSLogDomain.16354
- ___CPLSessionOSLogDomain.18278
- ___CPLSessionOSLogDomain.22806
- ___CPLSessionOSLogDomain.onceToken.16356
- ___CPLSessionOSLogDomain.onceToken.18283
- ___CPLSessionOSLogDomain.onceToken.22808
- ___CPLSessionOSLogDomain.result.16357
- ___CPLSessionOSLogDomain.result.18284
- ___CPLSessionOSLogDomain.result.22810
- ___CPLStorageOSLogDomain.11262
- ___CPLStorageOSLogDomain.11347
- ___CPLStorageOSLogDomain.17857
- ___CPLStorageOSLogDomain.202
- ___CPLStorageOSLogDomain.2026
- ___CPLStorageOSLogDomain.20302
- ___CPLStorageOSLogDomain.21548
- ___CPLStorageOSLogDomain.22205
- ___CPLStorageOSLogDomain.22453
- ___CPLStorageOSLogDomain.505
- ___CPLStorageOSLogDomain.6248
- ___CPLStorageOSLogDomain.7910
- ___CPLStorageOSLogDomain.8668
- ___CPLStorageOSLogDomain.909
- ___CPLStorageOSLogDomain.9104
- ___CPLStorageOSLogDomain.9270
- ___CPLStorageOSLogDomain.9463
- ___CPLStorageOSLogDomain.onceToken.11273
- ___CPLStorageOSLogDomain.onceToken.11350
- ___CPLStorageOSLogDomain.onceToken.14673
- ___CPLStorageOSLogDomain.onceToken.17859
- ___CPLStorageOSLogDomain.onceToken.2028
- ___CPLStorageOSLogDomain.onceToken.20304
- ___CPLStorageOSLogDomain.onceToken.204
- ___CPLStorageOSLogDomain.onceToken.20582
- ___CPLStorageOSLogDomain.onceToken.21552
- ___CPLStorageOSLogDomain.onceToken.22210
- ___CPLStorageOSLogDomain.onceToken.22461
- ___CPLStorageOSLogDomain.onceToken.507
- ___CPLStorageOSLogDomain.onceToken.6250
- ___CPLStorageOSLogDomain.onceToken.7912
- ___CPLStorageOSLogDomain.onceToken.8676
- ___CPLStorageOSLogDomain.onceToken.9110
- ___CPLStorageOSLogDomain.onceToken.915
- ___CPLStorageOSLogDomain.onceToken.9272
- ___CPLStorageOSLogDomain.onceToken.9465
- ___CPLStorageOSLogDomain.result.11275
- ___CPLStorageOSLogDomain.result.11352
- ___CPLStorageOSLogDomain.result.14675
- ___CPLStorageOSLogDomain.result.17861
- ___CPLStorageOSLogDomain.result.2030
- ___CPLStorageOSLogDomain.result.20306
- ___CPLStorageOSLogDomain.result.20583
- ___CPLStorageOSLogDomain.result.206
- ___CPLStorageOSLogDomain.result.21554
- ___CPLStorageOSLogDomain.result.22212
- ___CPLStorageOSLogDomain.result.22463
- ___CPLStorageOSLogDomain.result.509
- ___CPLStorageOSLogDomain.result.6252
- ___CPLStorageOSLogDomain.result.7913
- ___CPLStorageOSLogDomain.result.8677
- ___CPLStorageOSLogDomain.result.9112
- ___CPLStorageOSLogDomain.result.917
- ___CPLStorageOSLogDomain.result.9273
- ___CPLStorageOSLogDomain.result.9466
- ___CPLStoreOSLogDomain.3044
- ___CPLStoreOSLogDomain.onceToken.3045
- ___CPLStoreOSLogDomain.result.3046
- ___CPLTaskOSLogDomain.11535
- ___CPLTaskOSLogDomain.1342
- ___CPLTaskOSLogDomain.14105
- ___CPLTaskOSLogDomain.14578
- ___CPLTaskOSLogDomain.15651
- ___CPLTaskOSLogDomain.17193
- ___CPLTaskOSLogDomain.21344
- ___CPLTaskOSLogDomain.23151
- ___CPLTaskOSLogDomain.24287
- ___CPLTaskOSLogDomain.2598
- ___CPLTaskOSLogDomain.5478
- ___CPLTaskOSLogDomain.619
- ___CPLTaskOSLogDomain.7241
- ___CPLTaskOSLogDomain.onceToken.11570
- ___CPLTaskOSLogDomain.onceToken.1357
- ___CPLTaskOSLogDomain.onceToken.14107
- ___CPLTaskOSLogDomain.onceToken.14580
- ___CPLTaskOSLogDomain.onceToken.15663
- ___CPLTaskOSLogDomain.onceToken.17200
- ___CPLTaskOSLogDomain.onceToken.21386
- ___CPLTaskOSLogDomain.onceToken.23162
- ___CPLTaskOSLogDomain.onceToken.24295
- ___CPLTaskOSLogDomain.onceToken.2600
- ___CPLTaskOSLogDomain.onceToken.5485
- ___CPLTaskOSLogDomain.onceToken.622
- ___CPLTaskOSLogDomain.onceToken.7256
- ___CPLTaskOSLogDomain.result.11572
- ___CPLTaskOSLogDomain.result.1358
- ___CPLTaskOSLogDomain.result.14109
- ___CPLTaskOSLogDomain.result.14582
- ___CPLTaskOSLogDomain.result.15664
- ___CPLTaskOSLogDomain.result.17201
- ___CPLTaskOSLogDomain.result.21387
- ___CPLTaskOSLogDomain.result.23163
- ___CPLTaskOSLogDomain.result.24296
- ___CPLTaskOSLogDomain.result.2602
- ___CPLTaskOSLogDomain.result.5487
- ___CPLTaskOSLogDomain.result.624
- ___CPLTaskOSLogDomain.result.7258
- ____CPLFeedbackRecordClassForClass_block_invoke.28
- ____CPLGetAccountDSID_block_invoke.130
- ____CPLGetAccountDSID_block_invoke_2.136
- _____CPLConfigurationOSLogDomain_block_invoke.19557
- _____CPLSchedulerOSLogDomain_block_invoke.7607
- _____CPLSessionOSLogDomain_block_invoke.16359
- _____CPLSessionOSLogDomain_block_invoke.18286
- _____CPLSessionOSLogDomain_block_invoke.22813
- _____CPLStorageOSLogDomain_block_invoke.11278
- _____CPLStorageOSLogDomain_block_invoke.11355
- _____CPLStorageOSLogDomain_block_invoke.14680
- _____CPLStorageOSLogDomain_block_invoke.17864
- _____CPLStorageOSLogDomain_block_invoke.20309
- _____CPLStorageOSLogDomain_block_invoke.2033
- _____CPLStorageOSLogDomain_block_invoke.20589
- _____CPLStorageOSLogDomain_block_invoke.209
- _____CPLStorageOSLogDomain_block_invoke.21557
- _____CPLStorageOSLogDomain_block_invoke.22215
- _____CPLStorageOSLogDomain_block_invoke.22466
- _____CPLStorageOSLogDomain_block_invoke.512
- _____CPLStorageOSLogDomain_block_invoke.6255
- _____CPLStorageOSLogDomain_block_invoke.7915
- _____CPLStorageOSLogDomain_block_invoke.8679
- _____CPLStorageOSLogDomain_block_invoke.9115
- _____CPLStorageOSLogDomain_block_invoke.920
- _____CPLStorageOSLogDomain_block_invoke.9275
- _____CPLStorageOSLogDomain_block_invoke.9468
- _____CPLStoreOSLogDomain_block_invoke.3048
- _____CPLTaskOSLogDomain_block_invoke.11575
- _____CPLTaskOSLogDomain_block_invoke.1360
- _____CPLTaskOSLogDomain_block_invoke.14112
- _____CPLTaskOSLogDomain_block_invoke.14585
- _____CPLTaskOSLogDomain_block_invoke.15666
- _____CPLTaskOSLogDomain_block_invoke.17203
- _____CPLTaskOSLogDomain_block_invoke.21389
- _____CPLTaskOSLogDomain_block_invoke.23165
- _____CPLTaskOSLogDomain_block_invoke.24298
- _____CPLTaskOSLogDomain_block_invoke.2605
- _____CPLTaskOSLogDomain_block_invoke.5490
- _____CPLTaskOSLogDomain_block_invoke.627
- _____CPLTaskOSLogDomain_block_invoke.7261
- ____connectedLibraryManagerRegisterQueue_block_invoke
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96r104r_e49_v32?0"CPLRecordChange"8"NSArray"16"NSError"24ls32l8r96l8r104l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96r104r_e5_v8?0ls32l8s40l8s48l8s56l8r96l8r104l8s64l8s72l8s80l8s88l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs104r112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s96l8s56l8s64l8s72l8r104l8s80l8r112l8s88l8
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88bs96bs104r112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s88l8s56l8s64l8r104l8s72l8r112l8s80l8s96l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112bs120r128r_e5_v8?0ls32l8s40l8s112l8s48l8s56l8s64l8s72l8s80l8s88l8r120l8s96l8r128l8s104l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r_e5_v8?0lr120l8s32l8s40l8r128l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
- ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s104bs112bs120r128r_e5_v8?0ls32l8s40l8s104l8s48l8s56l8s64l8s72l8s80l8r120l8s88l8r128l8s96l8s112l8
- ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s_e67_"CPLActiveDownloadQueue"24?0Q8"CPLResourceTransferTaskOptions"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8
- ___block_descriptor_40_e8_32s_e31_B32?0"CPLBrokenScope"8Q16^B24ls32l8
- ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e47_v24?0"CPLEngineSchedulerBlocker"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e66_v48?0"NSError"8"NSString"16"NSString"24"NSString"32"NSURL"40ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e66_v48?0"NSError"8"NSString"16"NSString"24"NSString"32"NSURL"40ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e36_v24?0"CPLScopeChange"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"CPLRecordChange"8"CPLRecordChange"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e29_v16?0"CPLScopedIdentifier"8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48bs_e98_v96?0"NSError"8"NSDictionary"16Q24Q32Q40Q48Q56"NSString"64"NSString"72"NSString"80"NSURL"88ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v24?0"_CPLResourcesMutableArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56r64r_e5_B8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e25_v16?0"CPLCallObserver"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e67_"CPLActiveDownloadQueue"24?0Q8"CPLResourceTransferTaskOptions"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.101
- ___block_literal_global.101.14581
- ___block_literal_global.10166
- ___block_literal_global.1039
- ___block_literal_global.1042
- ___block_literal_global.10482
- ___block_literal_global.105.19069
- ___block_literal_global.1053
- ___block_literal_global.106
- ___block_literal_global.10881
- ___block_literal_global.110.21066
- ___block_literal_global.11120
- ___block_literal_global.11274
- ___block_literal_global.11351
- ___block_literal_global.11571
- ___block_literal_global.117
- ___block_literal_global.1185
- ___block_literal_global.12.8039
- ___block_literal_global.123
- ___block_literal_global.12498
- ___block_literal_global.126
- ___block_literal_global.127
- ___block_literal_global.12738
- ___block_literal_global.128.24455
- ___block_literal_global.13
- ___block_literal_global.13239
- ___block_literal_global.136
- ___block_literal_global.138
- ___block_literal_global.1398
- ___block_literal_global.14.14616
- ___block_literal_global.14108
- ___block_literal_global.142
- ___block_literal_global.142.21070
- ___block_literal_global.14370
- ___block_literal_global.146
- ___block_literal_global.14615
- ___block_literal_global.14674
- ___block_literal_global.148
- ___block_literal_global.1481
- ___block_literal_global.14837
- ___block_literal_global.153
- ___block_literal_global.15364
- ___block_literal_global.15384
- ___block_literal_global.154
- ___block_literal_global.15449
- ___block_literal_global.156
- ___block_literal_global.1561
- ___block_literal_global.15673
- ___block_literal_global.159.21071
- ___block_literal_global.16.15658
- ___block_literal_global.16209
- ___block_literal_global.16424
- ___block_literal_global.165
- ___block_literal_global.1687
- ___block_literal_global.16988
- ___block_literal_global.1702
- ___block_literal_global.171
- ___block_literal_global.171.21072
- ___block_literal_global.1722
- ___block_literal_global.1724
- ___block_literal_global.1729
- ___block_literal_global.17305
- ___block_literal_global.1731
- ___block_literal_global.1732
- ___block_literal_global.1734
- ___block_literal_global.1736
- ___block_literal_global.1738
- ___block_literal_global.1740
- ___block_literal_global.1742
- ___block_literal_global.1744
- ___block_literal_global.1746
- ___block_literal_global.1748
- ___block_literal_global.1750
- ___block_literal_global.1752
- ___block_literal_global.1754
- ___block_literal_global.1756
- ___block_literal_global.1758
- ___block_literal_global.1760
- ___block_literal_global.1762
- ___block_literal_global.1764
- ___block_literal_global.17654
- ___block_literal_global.1774
- ___block_literal_global.1776
- ___block_literal_global.1784
- ___block_literal_global.17860
- ___block_literal_global.1794
- ___block_literal_global.1799
- ___block_literal_global.18
- ___block_literal_global.1801
- ___block_literal_global.18296
- ___block_literal_global.18467
- ___block_literal_global.18605
- ___block_literal_global.1899
- ___block_literal_global.190
- ___block_literal_global.19183
- ___block_literal_global.195
- ___block_literal_global.1955
- ___block_literal_global.19553
- ___block_literal_global.1961
- ___block_literal_global.19937
- ___block_literal_global.200
- ___block_literal_global.2029
- ___block_literal_global.20305
- ___block_literal_global.20469
- ___block_literal_global.205
- ___block_literal_global.20585
- ___block_literal_global.210
- ___block_literal_global.21062
- ___block_literal_global.21404
- ___block_literal_global.21553
- ___block_literal_global.21727
- ___block_literal_global.219
- ___block_literal_global.220
- ___block_literal_global.222
- ___block_literal_global.22211
- ___block_literal_global.22462
- ___block_literal_global.225
- ___block_literal_global.22622
- ___block_literal_global.22809
- ___block_literal_global.22964
- ___block_literal_global.2300
- ___block_literal_global.23220
- ___block_literal_global.23835
- ___block_literal_global.23971
- ___block_literal_global.24.14324
- ___block_literal_global.24043
- ___block_literal_global.243
- ___block_literal_global.24479
- ___block_literal_global.24593
- ___block_literal_global.24712
- ___block_literal_global.2476
- ___block_literal_global.24897
- ___block_literal_global.249
- ___block_literal_global.2534
- ___block_literal_global.259
- ___block_literal_global.2601
- ___block_literal_global.264
- ___block_literal_global.27.16445
- ___block_literal_global.275
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.2956
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.3023
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.31
- ___block_literal_global.310.12349
- ___block_literal_global.312
- ___block_literal_global.312.7512
- ___block_literal_global.32.22590
- ___block_literal_global.3285
- ___block_literal_global.33.7372
- ___block_literal_global.336
- ___block_literal_global.34.10058
- ___block_literal_global.34.2473
- ___block_literal_global.340
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.349
- ___block_literal_global.3558
- ___block_literal_global.356
- ___block_literal_global.368
- ___block_literal_global.37.10801
- ___block_literal_global.3798
- ___block_literal_global.4034
- ___block_literal_global.42.8046
- ___block_literal_global.4471
- ___block_literal_global.451
- ___block_literal_global.459
- ___block_literal_global.4608
- ___block_literal_global.4820
- ___block_literal_global.483
- ___block_literal_global.49
- ___block_literal_global.5.24606
- ___block_literal_global.50.7363
- ___block_literal_global.508
- ___block_literal_global.5266
- ___block_literal_global.532
- ___block_literal_global.5343
- ___block_literal_global.535
- ___block_literal_global.539
- ___block_literal_global.54.5240
- ___block_literal_global.542
- ___block_literal_global.5486
- ___block_literal_global.5627
- ___block_literal_global.57.8050
- ___block_literal_global.588
- ___block_literal_global.59
- ___block_literal_global.591
- ___block_literal_global.6.15671
- ___block_literal_global.61
- ___block_literal_global.6163
- ___block_literal_global.623
- ___block_literal_global.6251
- ___block_literal_global.6473
- ___block_literal_global.6768
- ___block_literal_global.677
- ___block_literal_global.680
- ___block_literal_global.683
- ___block_literal_global.72.16946
- ___block_literal_global.7257
- ___block_literal_global.7371
- ___block_literal_global.749
- ___block_literal_global.750
- ___block_literal_global.753
- ___block_literal_global.756
- ___block_literal_global.77.16204
- ___block_literal_global.7727
- ___block_literal_global.8036
- ___block_literal_global.859
- ___block_literal_global.86
- ___block_literal_global.8794
- ___block_literal_global.9004
- ___block_literal_global.91
- ___block_literal_global.9111
- ___block_literal_global.916
- ___block_literal_global.9209
- ___block_literal_global.93.19074
- ___block_literal_global.93.7794
- ___block_literal_global.95
- ___block_literal_global.9514
- ___block_literal_global.9686
- ___block_literal_global.9956
- ___cpl_dispatch_async_block_invoke.10142
- ___cpl_dispatch_async_block_invoke.11531
- ___cpl_dispatch_async_block_invoke.12177
- ___cpl_dispatch_async_block_invoke.1362
- ___cpl_dispatch_async_block_invoke.14117
- ___cpl_dispatch_async_block_invoke.14494
- ___cpl_dispatch_async_block_invoke.14571
- ___cpl_dispatch_async_block_invoke.15747
- ___cpl_dispatch_async_block_invoke.16766
- ___cpl_dispatch_async_block_invoke.17260
- ___cpl_dispatch_async_block_invoke.17605
- ___cpl_dispatch_async_block_invoke.18103
- ___cpl_dispatch_async_block_invoke.1813
- ___cpl_dispatch_async_block_invoke.18601
- ___cpl_dispatch_async_block_invoke.19532
- ___cpl_dispatch_async_block_invoke.20802
- ___cpl_dispatch_async_block_invoke.21342
- ___cpl_dispatch_async_block_invoke.21735
- ___cpl_dispatch_async_block_invoke.22966
- ___cpl_dispatch_async_block_invoke.23168
- ___cpl_dispatch_async_block_invoke.24340
- ___cpl_dispatch_async_block_invoke.2951
- ___cpl_dispatch_async_block_invoke.6708
- ___cpl_dispatch_async_block_invoke.682
- ___cpl_dispatch_async_block_invoke.7239
- ___cpl_dispatch_async_block_invoke.7508
- ___cpl_dispatch_async_block_invoke.7922
- ___cpl_dispatch_async_block_invoke.9799
- __connectedLibraryManagerRegisterQueue
- __connectedLibraryManagerRegisterQueue.cold.1
- __connectedLibraryManagerRegisterQueue.onceToken
- __connectedLibraryManagerRegisterQueue.queue
- __connectedLibraryManagers_unprotected
- __doProtected:.onceToken.15383
- __doProtected:.onceToken.22963
- __doProtected:.queue.22965
- __os_log_fault_impl
- __reverseMappingForLibraryOptions.onceToken
- __reverseMappingForLibraryOptions.reverseMapping
- __statusDidChange.12380
- _computeExpandedBatchWithError:.onceToken.24
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.19093
- _cplAdditionalSecureClassesForProperty:.additionalClasses.123
- _cplAdditionalSecureClassesForProperty:.additionalClasses.156
- _cplAdditionalSecureClassesForProperty:.onceToken.124
- _cplAdditionalSecureClassesForProperty:.onceToken.152
- _cplAdditionalSecureClassesForProperty:.onceToken.157
- _initWithCPLArchiver:.onceToken.1958
- _initWithCPLArchiver:.stringClass.1959
- _initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:.onceToken
- _initWithCoder:.logOnceToken.20471
- _initWithCoder:.onceToken.103
- _initWithCoder:.onceToken.10825
- _initWithCoder:.onceToken.14369
- _initWithCoder:.onceToken.18295
- _initWithCoder:.onceToken.20468
- _initWithCoder:.onceToken.22621
- _initWithCoder:.onceToken.24896
- _initWithCoder:.onceToken.5239
- _initWithCoder:.onceToken.5342
- _initWithCoder:.onceToken.6468
- _initWithCoder:.onceToken.74
- _initWithCoder:.onceToken.84
- _initWithCoder:.onceToken.91
- _initWithCoder:.pushContextsClasses.22623
- _initWithCoder:.stringClass.104
- _initWithCoder:.stringClass.10826
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlertTopMostKey
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
- _kCFUserNotificationOtherButtonTitleKey
- _objc_msgSend$_addAllTransportScopesForScope:scopes:allowsTentativeTransportScope:useStagingScopeIfNecessary:error:
- _objc_msgSend$_addTransportScopeForScope:scopes:allowsTentativeTransportScope:useStagingScopeIfNecessary:error:
- _objc_msgSend$_cacheKeyForReferenceResource:adjustments:includePosterFrame:
- _objc_msgSend$_cachedResourcesForReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_checkGeneratedResources:error:
- _objc_msgSend$_checkResource:name:error:
- _objc_msgSend$_checkTransportScopeForScopeIdentifier:hasConcreteScope:error:
- _objc_msgSend$_cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_copyResourceChangeFromChange:toChange:fingerprintScheme:error:
- _objc_msgSend$_createCacheFolderIfNecessary
- _objc_msgSend$_discardGenerateDerivativesProgress
- _objc_msgSend$_dropConnectionCompletly
- _objc_msgSend$_dropConnectionCompletlyLocked
- _objc_msgSend$_fillStatus:forComponents:completionHandler:
- _objc_msgSend$_finalFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_finishReportingDerivativesIsNecessary
- _objc_msgSend$_folderNameForReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:
- _objc_msgSend$_generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:
- _objc_msgSend$_generatingDerivativesForChange:fractionCompleted:chunkLength:
- _objc_msgSend$_indexOfCurrentClassForInitialQueriesForScope:
- _objc_msgSend$_installGenerateDerivativesCancellationHandler:
- _objc_msgSend$_isUnsupportedFormatError:
- _objc_msgSend$_markUploadedTasksDidFinishWithError:transaction:error:
- _objc_msgSend$_minimalDateForFirstSync
- _objc_msgSend$_noteGeneratedResources:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_pathToFirstSynchronizationMarker
- _objc_msgSend$_popNextBatchAndContinue
- _objc_msgSend$_resetFirstSynchronizationMarker
- _objc_msgSend$_reverseMappingForLibraryOptions
- _objc_msgSend$_showAlertWithMessage:readMoreURL:createRadarURL:showsRecoverButton:
- _objc_msgSend$_tempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:
- _objc_msgSend$_updateChange:fromOldChange:withResources:excludeImages:
- _objc_msgSend$_writeFirstSynchronizationMarker
- _objc_msgSend$ackownledgeRecordWithScopedIdentifier:error:
- _objc_msgSend$acquireReschedulerTaskWithCompletionHandler:
- _objc_msgSend$alertMessage
- _objc_msgSend$alternateRecoverDescription
- _objc_msgSend$blockWriteTransactionsWithCompletionHandler:
- _objc_msgSend$brokenMessage
- _objc_msgSend$brokenTitle
- _objc_msgSend$canBoostBackgroundOperations
- _objc_msgSend$canBoostOperations
- _objc_msgSend$checkScopeIdentifier:
- _objc_msgSend$componentsWithString:
- _objc_msgSend$cplUnderlyingError
- _objc_msgSend$createGroupForAcceptingLibraryShare
- _objc_msgSend$createGroupForAcceptingMomentShare
- _objc_msgSend$createGroupForFetchingLibraryShare
- _objc_msgSend$createGroupForFetchingMomentShare
- _objc_msgSend$createGroupForPublishingLibraryShare
- _objc_msgSend$createGroupForPublishingMomentShare
- _objc_msgSend$createGroupForThumbnailPrefetch
- _objc_msgSend$createRadarButtonTitle
- _objc_msgSend$createRadarURL
- _objc_msgSend$defaultFlags
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$dropPersistedInitialSyncSession
- _objc_msgSend$findPersistedInitialSyncSession:completionHandler:
- _objc_msgSend$forceSyncForScopeIdentifiers:reply:
- _objc_msgSend$forceSynchronizingScopeWithIdentifiers:completionHandler:
- _objc_msgSend$getStatusForComponents:completionHandler:
- _objc_msgSend$hasEngineRecoveryMechanism
- _objc_msgSend$hasSomeSharedCollections
- _objc_msgSend$initForManagementWithLibraryIdentifier:
- _objc_msgSend$initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:
- _objc_msgSend$initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:options:
- _objc_msgSend$initWithComponents:handler:
- _objc_msgSend$initWithObject:selector:functionName:
- _objc_msgSend$internalRecoveryInstructions
- _objc_msgSend$isInLessThanTimeInterval:
- _objc_msgSend$needsToAcquireRescheduler
- _objc_msgSend$numberWithUnsignedLong:
- _objc_msgSend$openLibraryWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:completionHandler:
- _objc_msgSend$openURL:configuration:completionHandler:
- _objc_msgSend$popNextBatchWithError:
- _objc_msgSend$queryItemWithName:value:
- _objc_msgSend$radarDescription
- _objc_msgSend$radarTitle
- _objc_msgSend$readMoreButtonTitle
- _objc_msgSend$readMoreURL
- _objc_msgSend$reallyCancel
- _objc_msgSend$reallyLaunch
- _objc_msgSend$recoverButtonTitle
- _objc_msgSend$recoverUsingEngineWithCompletionHandler:
- _objc_msgSend$rescheduler
- _objc_msgSend$serverSupportsDeletedByUserIdentifier
- _objc_msgSend$serverSupportsLastViewedDate
- _objc_msgSend$serverSupportsSharedLibrarySharingState
- _objc_msgSend$setHasSomeSharedCollections:
- _objc_msgSend$setQueryItems:
- _objc_msgSend$shouldAutoactivateScopeWithIdentifier:scopeType:
- _objc_msgSend$shouldProcessScope:inTransaction:
- _objc_msgSend$shouldShowAlertToUser
- _objc_msgSend$shouldStartTaskInTransaction:
- _objc_msgSend$showAlertToUser
- _objc_msgSend$updateLastSuccessfullSyncDate:
- _objc_release_x10
- _propertiesForChangeType:.onceToken.15224
- _propertiesForChangeType:.onceToken.19107
- _propertiesForChangeType:.onceToken.193
- _propertiesForChangeType:.onceToken.23970
- _propertiesForChangeType:.properties.23972
- _supportsEPP.onceToken
- _supportsEPP.result
- _supportsEPPAutoEnable.onceToken
- _supportsEPPAutoEnable.result
CStrings:
+ "\n\t\t\t"
+ "\n  - "
+ "\n  - %@"
+ "\n%lu attached object(s) at %@ (%@):\n\t%@"
+ "\nEnabled feature data classes: %@"
+ "\nNo attached objects at %@ (%@)"
+ "\nShared Collection feature is disabled"
+ "\nShared library feature flag is disabled"
+ "\nTurbo mode%s: expires %@"
+ "\nTurbo mode: expired %@"
+ "\nTurbo mode: forced"
+ "\nconfiguration update: %@"
+ "\nlast forced tasks:"
+ "\nstatus:\n\t%@"
+ " (blocked)"
+ " - "
+ " - allows access requests"
+ " - anonymous access"
+ " - blocked"
+ " - client sync"
+ " - expiringState: %@, expiryDate: %@, viewingMode: %@"
+ " - expiringState: %@, viewingMode: %@"
+ " - public: %@"
+ " [proxy]"
+ " bypassing limits"
+ " owner"
+ " turbo"
+ "$"
+ "%0.1f%%"
+ "%@ %{public}@"
+ "%@ %{public}@ - %@"
+ "%@ %{public}@ - %@ %0.0f%%"
+ "%@ %{public}@ - %@ (ignored)"
+ "%@ (%@) should be ignored"
+ "%@ (%i)"
+ "%@ (unkn.)"
+ "%@ - %@ %@%@"
+ "%@ - cancelled"
+ "%@ called but there is not upload going on"
+ "%@ called for mismatched registrations"
+ "%@ called with mismatched registration type"
+ "%@ called with nil parameters"
+ "%@ called without a boundary key"
+ "%@ called without an owner"
+ "%@ called without libraryIdentifier"
+ "%@ can't be disable for this engine"
+ "%@ failed to clear all permanent errors %@: %@"
+ "%@ failed to refresh observed event for %@: %@"
+ "%@ failed to register %@: %@"
+ "%@ failed to reregister observers: %@"
+ "%@ failed to set test permanent error %@: %@"
+ "%@ failed to unregister %@: %@"
+ "%@ failed to update registration for %@: %@"
+ "%@ for %@"
+ "%@ for %@: %@"
+ "%@ for %@: %@ - %@"
+ "%@ has active %lu sub-caches and can't discard its cache yet: %{public}@"
+ "%@ has been invalidated a long time ago, will try re-opening one"
+ "%@ has been invalidated, will try re-opening one"
+ "%@ has both asset and post identifiers (mutually exclusive)"
+ "%@ has neither asset nor post identifier"
+ "%@ has permanent error"
+ "%@ in %@"
+ "%@ in %@ for %@"
+ "%@ is not a proxy on server, dropping delete"
+ "%@ is not allowed for this engine"
+ "%@ might be ready for %{public}@ - will try opening"
+ "%@ quality"
+ "%@ should not be called if nil"
+ "%@ should not be used in all records mode"
+ "%@ should not be used in all scopes mode"
+ "%@ tries to start while %@ is launched"
+ "%@ trying to finish an unknown subtask"
+ "%@ trying to run more than one subtask at the same time"
+ "%@ will skip %@ - reason: %@"
+ "%@%@\n\t\t\t%@"
+ "%@(%@)"
+ "%@.%i"
+ "%@.%ld"
+ "%@.%ld '%@'"
+ "%@:"
+ "%@: %@ - %@"
+ "%lu changes"
+ "%lu records"
+ "%lu scopes"
+ "%lu statuses"
+ "%lu statuses, %lu progresses, %s"
+ "%{public}@ might be ready for %@ - will retry opening if current opening fails"
+ "%{public}@ might be ready for %@ but we are already opened - pinging library manager"
+ "-- <%@ %@> is already missing in cache"
+ "-- <%@ %@> is missing in cache, forcing delete as it is unquarantining the record"
+ ".cpl_resumable_marker.plist"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLDirectUploadTask.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineForceSyncTask.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineUIObservationCenter.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLGenerateDerivativesSubtask.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIObservedSource.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIRecordObservedSource.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIScopeObservedSource.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUISyncActivityObservedSource.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIUploadProgressHub.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesAccumulator.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesTask.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLBase.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryParameters.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSchemaFilter.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLTransportContainerConfiguration.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIObserver.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIRecordObserver.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIScopeObserver.m"
+ "<%@ %p %@ %@>"
+ "<%@ %p %@ - %@>"
+ "<%@ for %@ at %@ %@ (%@)>"
+ "<%@ for %@ at %@ (%@)>"
+ "<%@: %p safeFilenames:%lu>"
+ "<no date>"
+ "?4"
+ "@16@?0@\"CPLScopedIdentifier\"8"
+ "Additional requested scope %@ has permanent error - rejecting"
+ "Additional requested scope %@ is an invalid scope: flags are %@"
+ "Analysis Download High Priority (Initial Sync)"
+ "Asked to launch %@ from %@ but %@ is running - cancelling %@"
+ "Asked to launch %@ from %@ but sync is blocked because of %{public}@ - cancelling %@"
+ "Asked to rewind %@ to %@ but %@ is running"
+ "Auto-disabling %@"
+ "Auto-enabling %@"
+ "Automatically renaming %{public}@ to %@"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "B32@?0@\"<CPLBrokenScope>\"8Q16^B24"
+ "Bypassing background scheduling"
+ "CPL"
+ "CPLAutoEnableCollectionSharesFeatureDataclass"
+ "CPLDropAllAssetsInDirectUpload"
+ "CPLEnableNTimeURLInSharedCollection"
+ "CPLInstantlyDeferDerivativeGeneration"
+ "CPLLogResumableDerivativeGeneration"
+ "CPLSchema-%@"
+ "CPLServerSupportsProxyConflictResolution"
+ "CPLTurboMode"
+ "CPLTurboModeExpirationDate"
+ "CPLUploadFastNetworkThreshold"
+ "CPLUploadSlowNetworkThreshold"
+ "CPLUseSandboxFor"
+ "Calling %@ on %{public}@ with an invalid registration %@"
+ "Calling %@ on an unknown observed type %@"
+ "Calling %@ on an unknown observed type %{public}@"
+ "Can use turbo mode: %@"
+ "Can't disable feature options %@ in state %@"
+ "Can't enable feature options %@ in state %@"
+ "Can't map cloud \"postScopedIdentifier\" (%@) of %@"
+ "Can't map cloud \"postScopedIdentifier\" in %@"
+ "Can't map local \"postScopedIdentifier\" (%@) of %@"
+ "Can't map local \"postScopedIdentifier\" in %@"
+ "Can't set feature options %@ in state %@"
+ "Cancelling discretionary %@ because turbo mode has been enabled"
+ "Cancelling non-discretionary %@ because turbo mode has been disabled"
+ "Carry"
+ "Client is asking to download %@ but scope is inactive"
+ "Client is promoting %@ to %@ - deleting the previous scope"
+ "Client is trying to push %@ over %@"
+ "Client is trying to update %@ as a readonly participant"
+ "Client is trying to update a %@ with a %@"
+ "Client is trying to update keyAssetIdentifier on %@ from %@ to %@ as a participant"
+ "Client is trying to update thumbnailImageData on %@ as a participant"
+ "Client is trying to update title on %@ from %@ to %@ as a participant"
+ "Client pushed a comment but we need the asset too %@: %@"
+ "Client pushed a comment but we need the post too %@: %@"
+ "Client pushed a delete to an already deleted record: %@"
+ "Client pushed a record to an invalid scope - %@: %@"
+ "Closed %{public}@ for %@"
+ "Closing %{public}@ for %@"
+ "Closing %{public}@ for %@ immediately after opening"
+ "CloudPhotoLibrary-910.14.107"
+ "Container configuration has changed for %{public}@ - will need to refetch the boundary key"
+ "Container used to instantiate engine %{public}@ is incompatible with stored container %{public}@"
+ "Container used to instantiate engine %{public}@ mismatches with stored container %{public}@ - fixing engine"
+ "Continuing %@ after it failed for %@ with error: %@"
+ "Created new derivatives folder at '%@'"
+ "Creating %@ with %@"
+ "Declining %@ from %@"
+ "Defaults is preventing"
+ "Delegate for %@ has not been set"
+ "DeleteProxyRecords"
+ "Deleted(Post)"
+ "Derivatives Low Priority (Initial Sync)"
+ "Disabling %{public}@ in %{public}@"
+ "Discretionary %@ has been deferred but turbo mode is now enabled - relaunch it"
+ "Dispatching disconnect event to %@"
+ "Dispatching observed event %@ to %@"
+ "Enabling %{public}@ in %{public}@"
+ "Enabling expiring turbo mode %{public}@"
+ "Error enumerating %@: %@"
+ "Estimating the network is fast enough - will order assets by date"
+ "Estimating the network might be too slow - will order assets by size"
+ "Failed to find %@.plist in %@"
+ "Failed to find local change for uploaded %@"
+ "Failed to load schema definition from %@: %@"
+ "Failed to open %{public}@ for %@ - will wait to retry: %@"
+ "Failed to remove participants from share %{public}@: %@"
+ "Failed to remove resumable marker at: %@"
+ "Failed to request scope update for %@: %@"
+ "Failed to serialize %@: %@"
+ "Failed to store last sync date for %@"
+ "Failed to store permanent error for %@: %@"
+ "Failed to write resumable marker to: %@"
+ "Feature option %@ enabled at opening time"
+ "Feature option %@ is enabled which should not be"
+ "Feature option %{public}@ is enabled which should not be - wiping store"
+ "Fetch Asset Export ID High Priority"
+ "Fetch Resource Reference High Priority"
+ "Forcing refresh for %@ with %@"
+ "Forcing refresh for %@ with %@ changed - will refresh with registration change"
+ "Found existing derivatives folder at %@ but missing marker file. Creating a fresh folder"
+ "Found resumable marker file in: %@"
+ "G"
+ "Generating derivatives for %{public}@ failed (took %.2fs): %@"
+ "Generating derivatives for %{public}@ succeeded (took %.2fs)"
+ "INIT"
+ "Ignoring transport scope update error for %@: %@"
+ "Informing background scheduler of significant work beginning"
+ "Informing background scheduler of significant work ending"
+ "Invalid class '%@' for ignorable properties"
+ "Invalid manager %@"
+ "Invalid parameter clientLibraryBaseURL"
+ "Invalid parameter cloudLibraryResourceStorageURL"
+ "Invalid parameter cloudLibraryStateStorageURL"
+ "Invalid parameter libraryIdentifier"
+ "Invalid parameter mainScopeIdentifier"
+ "Invalid parameter parameters"
+ "Invalid parameter transportContainerConfiguration"
+ "Invalid plist from coder: %@"
+ "Invalid scope for %@"
+ "Invalid supported class '%@'"
+ "Invalid upload type %ld"
+ "Last event should not be nil here"
+ "Launching %@ for %lu scopes"
+ "Launching %@ for %lu scopes (ignored %lu)"
+ "Missing pull UUID in %@"
+ "MobileSlideShow"
+ "NSUserDefaults *_CPLSharedDefaultsForTurboMode(void)"
+ "New(Post)"
+ "NotDeleted(Post)"
+ "Notifying %lu record statuses have changed (%s)"
+ "Notifying %lu record statuses have changed (disconnected)"
+ "Notifying sync activity progress outside of a sync activity"
+ "Observed event for %@ changed to %@ - will refresh observed source with registration change"
+ "Observed event for %@ with %@ changed"
+ "Observed event for %@ with %@ was fetched externally"
+ "Observed source for %@ did disconnect"
+ "On expensive network. Will download resource in background"
+ "Opening library received downgraded options (from %@ to %@)"
+ "Options used to instantiate engine %{public}@ mismatches with stored options %{public}@ - fixing engine"
+ "Pinging %{public}@ for %@ library manager in force refresh"
+ "Production"
+ "Pull queue has been emptied before applying pulled %@: client will have to pull again"
+ "Push repository for %{public}@ contains changes but we are allowing local conflict resolution when over-limit. Will allow mingling."
+ "Refreshing observed event for %@"
+ "Registering %@ with %@"
+ "Registration for %@ changed to %@"
+ "Removed unsafe file: %@"
+ "Removing %@ from %@ and keeping %@ (%@)"
+ "Removing just-in-case from %@ as it has been associated with a backgroundScheduler"
+ "Requesting unknown source %@"
+ "Rescheduling discretionary %@ because turbo mode has been enabled"
+ "Rescheduling non-discretionary %@ because turbo mode has been disabled"
+ "Reusing existing derivatives folder at %@"
+ "Setting initial library options to %{public}@"
+ "Start upload (%@): %{public}@"
+ "Starting %@ with %@"
+ "Starting a scoped sync activity outside of a sync activity"
+ "Starting a sync activity for 2 scope identifiers %@ then %@"
+ "Starting a sync activity while already in a sync activity"
+ "Status for %@ (owner) took too long and returned:\n%@"
+ "Status for %@ took too long and returned:\n%@"
+ "Stopping %@ with %@"
+ "Stopping a sync activity for unknown scope identifier %@"
+ "Stopping a sync activity while idle"
+ "Stopping scoped sync activity outside of a sync activity"
+ "Store will need to be wiped - reason: %{public}@"
+ "Successfully removed participants %{public}@ from share %{public}@"
+ "Task"
+ "TestSharedCollection-SilentMigration-"
+ "Thumbmails Low Priority (Initial Sync)"
+ "Transport scope delete for %@ failed with error - will consider the delete successful: %@"
+ "Transport scope delete for %@ failed with permanent error - will consider the delete successful: %@"
+ "Trying to access defaults for %@ but this process is not allowed"
+ "Trying to create sub-cache %@ twice"
+ "Trying to decline a share while the library is not open"
+ "Trying to open %@ twice, opening status: %d"
+ "Trying to re-open connection after ping"
+ "Trying to refresh %@ but failed to get updated statuses: %@"
+ "Trying to refresh observed event for unregistered %@"
+ "Trying to remove a partial change from push repository: %@"
+ "Trying to remove participant from share %{public}@ while the library is not open"
+ "Trying to remove participant from share while the library is not open"
+ "Trying to report progress for unknown scope identifier %@"
+ "Trying to start %@ twice"
+ "Trying to start a sync activity twice %@ then %@"
+ "Trying to stop %@ but it has not been started yet"
+ "Trying to stop an unknown sync activity %@"
+ "Trying to update registration for unregistered %@"
+ "Trying to upload %{public}@ while the library is not open"
+ "UI status for %lu records have changed: %{public}@"
+ "UI status for %lu scopes have changed: %{public}@"
+ "UI status for all records have changed"
+ "UI status for all records within %lu scopes have changed: %{public}@"
+ "UI status for all scopes have changed"
+ "UI synchronizing status for %{public}@ changed to %@"
+ "Unable to remove existing derivatives folder missing marker file at %@. Error: %@"
+ "Unknown expiring state (%ld)"
+ "Unknown migration state (%ld)"
+ "Unknown viewingMode (%ld)"
+ "Unregistering %@"
+ "Updating engine parameters to %@"
+ "Updating registration for %@ to %@"
+ "Upload for %{public}@ failed because the scope is over %@"
+ "Upload for %{public}@ failed because the scope is over %@. Retrying with over-quota strategy"
+ "Upload for %{public}@ failed because the scope is over %@. Will still continue synchronizing other scopes"
+ "Upload for %{public}@ failed because the scope is over %@. Will stop forced sync"
+ "Upload for %{public}@ failed with permanent error - will check %lu scopes: %@"
+ "Upload progress (%@): %{public}@"
+ "Upload progress (final): finished"
+ "Uploading batch with QOS %@%@: %@"
+ "Waiting for sync manager to finish previous force sync %@ before launching pending %@"
+ "Will bypass background scheduling"
+ "Will bypass background scheduling for %@"
+ "Will check assets of %@ only against cloud cache when over-%@"
+ "Will check assets of %@ with server when over-%@"
+ "Will upload batch in background"
+ "Wrote resumable marker with %lu safe files to: %@"
+ "[%@ %@ %@ %@ %@ %@]"
+ "[%@ (%lu participants)"
+ "[%{public}@] Checking before uploading directly: %{public}@"
+ "[%{public}@] Clearing engine derivatives cache because of disk pressure before direct upload"
+ "[%{public}@] Failed to check %lu records: %@"
+ "[%{public}@] Failed to commit directly uploaded batch %@: %@"
+ "[%{public}@] Failed to upload directly %@: %@"
+ "[%{public}@] Found %lu/%lu records on server (rules: %{public}@) in %.2fs - cache: %{public}@"
+ "[%{public}@] Ignoring %{public}@ change type in %@: unsupported in direct upload"
+ "[%{public}@] Ignoring container relations in %@: unsupported in direct upload"
+ "[%{public}@] No change to upload from %@"
+ "[%{public}@] Successfully uploaded %@ in %.2fs"
+ "[%{public}@] Trying to upload a batch for an unknown scope %{public}@: %@"
+ "[%{public}@] Trying to upload a batch for an unknown scope: %@"
+ "[%{public}@] Trying to upload a batch with different scopes: %@"
+ "[%{public}@] Trying to upload a batch with missing or invalid transport scope %{public}@: %@\nerror: %@"
+ "[%{public}@] Trying to upload a batch with missing or invalid transport scope: %@\nerror: %@"
+ "[%{public}@] Trying to upload records for %@ with permanent error"
+ "[%{public}@] Uploaded local batch directly: %@"
+ "[%{public}@] Uploading directly %@"
+ "[%{public}@] Will need to upload %@ but no file was provided by client"
+ "[%{public}@] Won't upload %@ as it can't be translated to the cloud yet: %@"
+ "[<placeholder> %@ %@ %@ %@]"
+ "[Container: %@]"
+ "[session #%lu%@%@%s]"
+ "__nouser__"
+ "aBID"
+ "access blocked"
+ "access denied"
+ "access requested"
+ "accountPartitionType"
+ "activity"
+ "allowedResources"
+ "allowsAccessRequests"
+ "allowsAnonymousPublicAccess"
+ "already deleted or inexistent"
+ "analysis-initial-sync"
+ "asset has been dropped"
+ "assetBatchIdentifier"
+ "background session"
+ "backup"
+ "busyState: %ld"
+ "bypassing background scheduling"
+ "checking records"
+ "ckCT"
+ "ckMT"
+ "client sync"
+ "client.session.pull.update"
+ "clientLibraryBasePath"
+ "cloudLibraryResourceStoragePath"
+ "cloudLibraryStateStoragePath"
+ "collection-shares"
+ "com.apple.cpl.derivatives"
+ "com.apple.cpl.libraryisready"
+ "com.apple.cpl.observationcenter"
+ "com.apple.cpl.transportupdate"
+ "com.apple.photos.applibraries.prototyping"
+ "com.apple.photos.asc.e2ee"
+ "com.apple.photos.cloud"
+ "commenter"
+ "container"
+ "contributor"
+ "creationTimestamp"
+ "custom schema for %@"
+ "database has been marked as deactivated"
+ "defaults asks to drop asset"
+ "delete"
+ "delete: %@"
+ "derivatives.resumable"
+ "direct upload"
+ "download"
+ "download: %@"
+ "droppedResources"
+ "empty status"
+ "engine.generatederivatives"
+ "engine.observationcenter"
+ "engine.syncmanager.direct-upload.task"
+ "epp"
+ "expiring"
+ "featureVersion"
+ "featureVersion: %ld"
+ "fetch-export-id"
+ "fetch-reference"
+ "final"
+ "finished"
+ "force-download"
+ "force-sync"
+ "force-sync-with-push"
+ "forced sync"
+ "fromInitialDownload"
+ "full photos schema"
+ "good"
+ "iCPL"
+ "identifier: %@\npath: %@"
+ "idle"
+ "ignoreProperties"
+ "in-memory-resource-download"
+ "in-progress"
+ "indet."
+ "initial"
+ "initial-accept"
+ "invalid flags for %@: %@"
+ "isPlaceholder"
+ "isPo"
+ "isPostComment"
+ "last sync"
+ "lastSync"
+ "lastSync: %@"
+ "library.parameters"
+ "library.parameters.container"
+ "limit"
+ "linkquality"
+ "low data"
+ "low power"
+ "manatee"
+ "mgtS"
+ "migrationState"
+ "minimal"
+ "moderate"
+ "modificationTimestamp"
+ "moment-shares"
+ "nTimeURL"
+ "needs-upload"
+ "no changes"
+ "no recovery"
+ "no transport scope"
+ "not supported"
+ "observation test is already started"
+ "observation test is already stopped"
+ "observation test started"
+ "observation test stopped"
+ "observation-test"
+ "observationcenter"
+ "observer-manager"
+ "observers"
+ "optimize-initial-sync"
+ "over-limit"
+ "overLimit"
+ "overLimit: %@"
+ "overQuota: %@"
+ "permanent"
+ "permanent error"
+ "permanent error date"
+ "permanentError"
+ "permanentError: %@"
+ "plist"
+ "post"
+ "postIdentifier"
+ "process"
+ "process: %@"
+ "proxy delete of a non-proxy record"
+ "proxyBestResourceType"
+ "proxyExpectedMasterIdentifier"
+ "proxyExpectedVideoDuration"
+ "proxyExpirationDate"
+ "proxyState"
+ "public-website"
+ "pullUUID"
+ "pxBR"
+ "pxEx"
+ "pxMI"
+ "pxSt"
+ "pxVD"
+ "q16@?0@\"NSString\"8"
+ "quota"
+ "rat"
+ "rating"
+ "reactText"
+ "registration"
+ "related record has been dropped"
+ "resetSync"
+ "resetSync: %@"
+ "resource-download"
+ "resource-upload"
+ "rtxt"
+ "running"
+ "sandbox"
+ "scope has a permanent error"
+ "scope has permanent error"
+ "scope is inactive"
+ "scope is unknown"
+ "scopeChange"
+ "server-has-changes"
+ "sharedLibraryExit"
+ "sharedLibraryExit: %ld"
+ "sharedLibraryOverLimit"
+ "sharedLibraryOverLimit: %@"
+ "sharedLibraryOverQuota"
+ "sharedLibraryOverQuota: %@"
+ "start-observation-test"
+ "started"
+ "stop-observation-test"
+ "stopped"
+ "store is blocked since %@ - reason: %@"
+ "subscriptionDate"
+ "supportedRecordClasses"
+ "sync"
+ "sync: %@"
+ "syncActivity"
+ "synchronizing scope list: disabled\n"
+ "testing schema for %@"
+ "took too long"
+ "transfer"
+ "turbo mode flags: %@"
+ "uLVD"
+ "ui.observer"
+ "ui.observer.manager"
+ "ui.observer.records"
+ "ui.observer.records.source"
+ "ui.observer.scopes"
+ "ui.observer.scopes.source"
+ "ui.observer.syncactivity.source"
+ "unarchived"
+ "unblocked"
+ "unknown %ld"
+ "unknown-%ld"
+ "upload: %@"
+ "uploading %lu records%s"
+ "uploading changes"
+ "uploading-progress"
+ "userLastViewedNotificationDate"
+ "v16@?0@\"<CPLEngineTransportTask>\"8"
+ "v16@?0@\"<CPLUIObserverPrivateDelegate>\"8"
+ "v16@?0@\"CPLGenerateDerivativesSubtask\"8"
+ "v16@?0@\"CPLUIObservedEvent\"8"
+ "v16@?0@\"CPLUIObservedSource\"8"
+ "v16@?0@\"CPLUIRecordObservedSource\"8"
+ "v16@?0@\"CPLUIScopeObservedSource\"8"
+ "v16@?0@\"CPLUISyncActivityObservedSource\"8"
+ "v16@?0@\"CPLUITestObservedSource\"8"
+ "v20@?0@\"NSString\"8I16"
+ "v24@?0@\"CPLChangeBatch\"8@\"NSError\"16"
+ "v24@?0@\"CPLEngineScope\"8@\"NSString\"16"
+ "v24@?0@\"CPLUIObserverAndRegistration\"8^B16"
+ "v24@?0q8^B16"
+ "v28@?0@\"CPLScopedIdentifier\"8@\"NSNumber\"16B24"
+ "v32@?0@\"NSArray\"8@\"CPLPartialDerivativesGenerationResult\"16@\"NSError\"24"
+ "v32@?0@\"NSError\"8@\"NSString\"16@\"CPLLibraryParameters\"24"
+ "v32@?0@\"NSString\"8@\"CPLUIScopeStatus\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSUUID\"8@\"CPLUIObserverAndRegistration\"16^B24"
+ "v32@?0@\"_CPLResourcesMutableArray\"8@\"CPLPartialDerivativesGenerationResult\"16@\"NSError\"24"
+ "v80@?0@\"NSError\"8@\"NSDictionary\"16Q24Q32Q40Q48Q56@\"NSString\"64@\"CPLLibraryParameters\"72"
+ "verifying"
+ "waiting"
+ "zoneish"
+ "\x81"
+ "\xe1"
+ "\xf01"
+ "\xf0Ta"
+ "\xf0\xc1"
+ "\xf0\xf0Q"
+ "\xf0\xf1"
- "\n\t%lu attached object(s) at %@ (%@):\n\t\t%@"
- "\n\tNo attached objects at %@ (%@)"
- "\n\tShared Collection feature is disabled"
- "\n\tShared library feature is disabled"
- "\n\tconfiguration update: %@"
- "\n\tstatus:\n\t\t%@"
- "\n\nTo clean-up library, run the following command:\n%@"
- "\nlast forced syncs:"
- "#16@0:8"
- "#24@0:8#16"
- "#24@0:8@16"
- "#24@0:8q16"
- "#32@0:8@16@24"
- "%@\n\n%@"
- "%@\n\nremaining scope is: %@"
- "%@ has been invalidated a long time, will try re-opening one"
- "%@ has no asset identifier"
- "%@ is inactive and needs to be refreshed"
- "%@ is staged and needs to be cleaned-up but %@ is not usable"
- "%@ should not be a broken scope"
- "%@:\n\t%@\n\t%@"
- "(?=\"status\"{?=\"unknown\"b1\"quarantined\"b1\"resetting\"b1\"uploaded\"b1\"waitingForUpload\"b1\"uploading\"b1\"waitingForUpdate\"b1\"updating\"b1\"confirmed\"b1\"shared\"b1}\"packedStatus\"I)"
- "-- <%@ %@> is already missing in cache but forcing delete as it is unquarantining the record"
- "-- <%@ %@> is already missing in cache. Ignoring delete"
- ".cxx_destruct"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBrokenScope.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesAccumulator.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/cloudphotolibrary/Engine/Upload Compute State Phase/CPLUploadComputeStatesTask.m"
- "630691"
- ":16@0:8"
- "?1"
- "@"
- "@\"<CPLAbstractObject>\""
- "@\"<CPLBatchExtractionStrategyStorage>\""
- "@\"<CPLBeforeUploadCheckItemsProvider>\""
- "@\"<CPLConfigurationFetcherDelegate>\""
- "@\"<CPLEngineAcquireReschedulerTask>\""
- "@\"<CPLEngineForceSyncTaskDelegate>\""
- "@\"<CPLEngineIDMapping>\""
- "@\"<CPLEngineLibraryOwner>\""
- "@\"<CPLEngineLibrarySupervisor>\""
- "@\"<CPLEngineStoreUserIdentifier>\""
- "@\"<CPLEngineStoreUserIdentifier>\"16@0:8"
- "@\"<CPLEngineSyncManagerForcedTask>\""
- "@\"<CPLEngineSyncTaskDelegate>\""
- "@\"<CPLEngineTransportCleanupStagedScopeTask>\""
- "@\"<CPLEngineTransportDeleteTransportScopeTask>\""
- "@\"<CPLEngineTransportDownloadBatchTask>\""
- "@\"<CPLEngineTransportFetchRecordsTask>\""
- "@\"<CPLEngineTransportFetchScopeListChangesTask>\""
- "@\"<CPLEngineTransportFetchTransportScopeTask>\""
- "@\"<CPLEngineTransportFixUpSparseRecordTask>\""
- "@\"<CPLEngineTransportGetCurrentSyncAnchorTask>\""
- "@\"<CPLEngineTransportGetScopeInfoTask>\""
- "@\"<CPLEngineTransportGroup>\""
- "@\"<CPLEngineTransportQueryTask>\""
- "@\"<CPLEngineTransportReshareRecordsTask>\""
- "@\"<CPLEngineTransportResourcesDownloadTask>\""
- "@\"<CPLEngineTransportSendFeedbackTask>\""
- "@\"<CPLEngineTransportSetupTask>\""
- "@\"<CPLEngineTransportTask>\""
- "@\"<CPLEngineTransportUpdateContributorsTask>\""
- "@\"<CPLEngineTransportUpdateTransportScopeTask>\""
- "@\"<CPLEngineTransportUploadBatchTask>\""
- "@\"<CPLEngineTransportUploadComputeStatesTask>\""
- "@\"<CPLFileWatcherDelegate>\""
- "@\"<CPLLibraryManagerDelegate>\""
- "@\"<CPLLibraryManagerForceSyncDelegate>\""
- "@\"<CPLLibraryManagerOwner>\""
- "@\"<CPLNetworkWatcherDelegate>\""
- "@\"<CPLRecordComputeStateDelegate>\""
- "@\"<CPLResourceProgressDelegate>\""
- "@\"<CPLSharedRecordMerger>\""
- "@\"<CPLSharedRecordPropertyMapping>\""
- "@\"<CPLStatusDelegate>\""
- "@\"<CPLSyncSessionConfiguration>\""
- "@\"<CPLSyncSessionRescheduler>\""
- "@\"<CPLSyncSessionRuntimeCharacteristics>\""
- "@\"<CPLSyncThroughputReporterDelegate>\""
- "@\"<CPLTransportScopeTranslator>\""
- "@\"<NSFastEnumeration>\""
- "@\"<NSFastEnumeration>\"24@0:8@\"NSString\"16"
- "@\"<NSFastEnumeration>\"32@0:8#16@\"CPLScopedIdentifier\"24"
- "@\"<NSFastEnumeration>\"32@0:8#16@\"NSString\"24"
- "@\"<NSFastEnumeration>\"36@0:8#16@\"NSString\"24B32"
- "@\"<NSFastEnumeration>\"40@0:8#16@\"NSString\"24Q32"
- "@\"<NSSecureCoding>\"40@0:8@\"NSXPCConnection\"16@\"NSXPCCoder\"24@32"
- "@\"<_CPLScheduledOverrideDelegate>\""
- "@\"CLLocation\""
- "@\"CPLAdjustments\""
- "@\"CPLBackgroundActivity\""
- "@\"CPLBatchExtractionStep\""
- "@\"CPLBatchExtractionStrategy\""
- "@\"CPLBeforeUploadCheckItems\""
- "@\"CPLChangeBatch\""
- "@\"CPLChangeSession\""
- "@\"CPLChangeStorage\""
- "@\"CPLConfiguration\""
- "@\"CPLConfigurationDictionary\""
- "@\"CPLConfigurationFetcher\""
- "@\"CPLContainerRelation\""
- "@\"CPLDerivativesFilter\""
- "@\"CPLDiffTracker\""
- "@\"CPLEngineChangePipe\""
- "@\"CPLEngineCloudCache\""
- "@\"CPLEngineDerivativesCache\""
- "@\"CPLEngineFeedbackManager\""
- "@\"CPLEngineFileStorage\""
- "@\"CPLEngineIDMapping\""
- "@\"CPLEngineIgnoredRecords\""
- "@\"CPLEngineLibrary\""
- "@\"CPLEngineOutgoingResources\""
- "@\"CPLEnginePendingRecordChecks\""
- "@\"CPLEnginePushRepository\""
- "@\"CPLEngineQuarantinedRecords\""
- "@\"CPLEngineRecordComputeStatePushQueue\""
- "@\"CPLEngineRemappedRecords\""
- "@\"CPLEngineResourceDownloadQueue\""
- "@\"CPLEngineResourceStorage\""
- "@\"CPLEngineRevertRecords\""
- "@\"CPLEngineScheduler\""
- "@\"CPLEngineSchedulerBlocker\""
- "@\"CPLEngineScope\""
- "@\"CPLEngineScopeCleanupTasks\""
- "@\"CPLEngineScopeStorage\""
- "@\"CPLEngineScopedTask\""
- "@\"CPLEngineStatusCenter\""
- "@\"CPLEngineStore\""
- "@\"CPLEngineStoreTransaction\""
- "@\"CPLEngineSyncManager\""
- "@\"CPLEngineSyncTask\""
- "@\"CPLEngineSystemMonitor\""
- "@\"CPLEngineTransientRepository\""
- "@\"CPLEngineTransientRepositoryBatchStorage\""
- "@\"CPLEngineTransport\""
- "@\"CPLEngineWriteTransactionBlocker\""
- "@\"CPLFeatureVersionHistory\""
- "@\"CPLFingerprintContext\""
- "@\"CPLFingerprintContext\"16@0:8"
- "@\"CPLFingerprintScheme\""
- "@\"CPLFingerprintSchemeV1\""
- "@\"CPLFingerprintSchemeV2\""
- "@\"CPLLibraryInfo\""
- "@\"CPLLibraryManager\""
- "@\"CPLLibraryState\""
- "@\"CPLMemoryAssetFlag\""
- "@\"CPLMemoryAssetList\""
- "@\"CPLMetrics\""
- "@\"CPLMomentShare\""
- "@\"CPLNetworkState\""
- "@\"CPLNetworkWatcher\""
- "@\"CPLPlaceAnnotation\""
- "@\"CPLPlaceholderRecord\""
- "@\"CPLPlatformObject\""
- "@\"CPLPlatformObject\"16@0:8"
- "@\"CPLProxyLibraryManager\""
- "@\"CPLPushChangeTasks\""
- "@\"CPLRecordChange\""
- "@\"CPLRecordChange\"24@0:8@\"CPLScopedIdentifier\"16"
- "@\"CPLRecordChangeDiffTracker\""
- "@\"CPLRecordPushContext\""
- "@\"CPLRecordStorageView\""
- "@\"CPLRecordTarget\""
- "@\"CPLRecordTargetMapping\""
- "@\"CPLRecordView\""
- "@\"CPLRejectedRecords\""
- "@\"CPLResetTracker\""
- "@\"CPLResource\""
- "@\"CPLResourceIdentity\""
- "@\"CPLResourceTransferTaskOptions\""
- "@\"CPLResourceTypeSet\""
- "@\"CPLResourceTypeSet\"24@0:8@\"CPLRecordChange\"16"
- "@\"CPLScopeChange\""
- "@\"CPLScopeFilter\""
- "@\"CPLScopeUpdateScopeTask\""
- "@\"CPLScopedIdentifier\""
- "@\"CPLScopedIdentifier\"24@0:8@\"CPLScopedIdentifier\"16"
- "@\"CPLScopedIdentifier\"32@0:8@\"CPLScopedIdentifier\"16^B24"
- "@\"CPLScopedIdentifier\"52@0:8@\"CPLScopedIdentifier\"16@\"CPLScopedIdentifier\"24B32Q36^@44"
- "@\"CPLServerFeedbackMessage\""
- "@\"CPLShare\""
- "@\"CPLStatus\""
- "@\"CPLSuggestionAssetFlag\""
- "@\"CPLSuggestionRecordList\""
- "@\"CPLSyncSession\""
- "@\"CPLSyncSessionPrediction\""
- "@\"CPLSyncSessionPredictor\""
- "@\"CPLSyncSessionThroughputMetrics\""
- "@\"CPLSyncStep\""
- "@\"CPLSyncThroughputReporter\""
- "@\"CPLSyncThroughputReporter\"24@0:8@\"NSString\"16"
- "@\"CPLTransaction\""
- "@\"CPLTransportScopeMapping\""
- "@\"CPLUploadComputeStatesAccumulator\""
- "@\"CPLUploadPushedChangesTask\""
- "@\"NSArray\""
- "@\"NSByteCountFormatter\""
- "@\"NSCountedSet\""
- "@\"NSData\""
- "@\"NSData\"24@0:8@16"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSEnumerator\""
- "@\"NSError\""
- "@\"NSError\"16@0:8"
- "@\"NSFormatter\""
- "@\"NSHashTable\""
- "@\"NSIndexSet\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_nw_path>\""
- "@\"NSObject<OS_nw_path_monitor>\""
- "@\"NSPersonNameComponents\""
- "@\"NSProgress\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"CPLLibraryManager\"16"
- "@\"NSThread\""
- "@\"NSURL\""
- "@\"NSURL\"40@0:8@\"CPLResource\"16@\"CPLResource\"24^@32"
- "@\"NSURLSession\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"Protocol\""
- "@\"Protocol\"16@0:8"
- "@\"RadiosPreferences\""
- "@\"_CPLEngineScopeCache\""
- "@\"_CPLPruneRequestCounter\""
- "@\"_CPLWeakLibraryManager\""
- "@116@0:8@16@24@32@40@48@56@64@72q80B88Q92Q100@108"
- "@120@0:8@16Q24@32{?={?=qiIq}{?=qiIq}}40@88@96@104@?112"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"CPLEngineScope\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSData\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^B16"
- "@24@0:8^Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8#16B24"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8B16:20"
- "@28@0:8B16@?20"
- "@28@0:8i16^@20"
- "@32@0:8#16@24"
- "@32@0:8:16@24"
- "@32@0:8:16^@24"
- "@32@0:8@16#24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16B24B28"
- "@32@0:8@16Q24"
- "@32@0:8@16^#24"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@32@0:8@16q24"
- "@32@0:8@?16@?24"
- "@32@0:8Q16@24"
- "@32@0:8Q16B24B28"
- "@32@0:8Q16Q24"
- "@32@0:8Q16^@24"
- "@32@0:8q16@24"
- "@32@0:8q16^q24"
- "@36@0:8#16@24B32"
- "@36@0:8@16#24B32"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@36@0:8@16B24@?28"
- "@36@0:8Q16B24Q28"
- "@40@0:8#16@24@32"
- "@40@0:8#16@24Q32"
- "@40@0:8:16@24@32"
- "@40@0:8@16:24@32"
- "@40@0:8@16@24#32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24d32"
- "@40@0:8@16@24q32"
- "@40@0:8@16@?24@?32"
- "@40@0:8@16B24B28@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16^B24^B32"
- "@40@0:8@16d24@32"
- "@40@0:8@16q24Q32"
- "@40@0:8@?16@?24@?32"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16Q24@32"
- "@40@0:8Q16Q24@?32"
- "@40@0:8q16@24*32"
- "@40@0:8q16@24@32"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16@24B32^@36"
- "@44@0:8@16B24@28@36"
- "@44@0:8B16@20@28@36"
- "@48@0:8#16@24#32@40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24@?32@?40"
- "@48@0:8@16@24d32@40"
- "@48@0:8@16@24d32^@40"
- "@48@0:8@16Q24^@32@40"
- "@48@0:8Q16@24Q32@40"
- "@48@0:8Q16@24^#32^@40"
- "@48@0:8Q16@24^@32^@40"
- "@48@0:8q16@24@32*40"
- "@48@0:8q16@24@32@40"
- "@48@0:8q16Q24@32Q40"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16@24B32Q36^@44"
- "@56@0:8@16#24@32@40Q48"
- "@56@0:8@16@24@32@40#48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40@?48"
- "@56@0:8@16@24@32@40Q48"
- "@56@0:8@16Q24^@32Q40@48"
- "@56@0:8@16q24q32@40^@48"
- "@56@0:8Q16@24@32@40@48"
- "@56@0:8Q16@24^@32^@40^@48"
- "@56@0:8Q16Q24Q32Q40^@48"
- "@56@0:8q16@24@32@40*48"
- "@64@0:8@16#24@32@40@?48@?56"
- "@64@0:8@16@24@32#40Q48^?56"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40@48@?56"
- "@64@0:8@16@24@32@40@48Q56"
- "@64@0:8@16@24@32@40@?48@?56"
- "@64@0:8@16@24@32q40q48@?56"
- "@64@0:8@16@24q32Q40@48@56"
- "@68@0:8@16Q24B32Q36Q44q52@?60"
- "@68@0:8^@16^@24^@32^B40B48@52^@60"
- "@72@0:8@16@24@32@40@48@56@?64"
- "@72@0:8@16@24@32@40@?48@?56@?64"
- "@80@0:8@16@24@32@?40@?48@?56@?64@?72"
- "@80@0:8@16@24@32q40q48@56@64@?72"
- "@80@0:8Q16Q24{?={?=qiIq}{?=qiIq}}32"
- "@84@0:8Q16Q24B32{?={?=qiIq}{?=qiIq}}36"
- "@?"
- "@?16@0:8"
- "@?24@0:8:16"
- "@?24@0:8Q16"
- "@?<v@?@\"<CPLEngineSyncManagerForcedTask>\"@\"NSError\">16@0:8"
- "A"
- "Additional requested scope %{public}@ is invalid scope: flags are %@"
- "Automatically prevented"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"CPLResource\"16"
- "B24@0:8@\"CPLScopedIdentifier\"16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B28@0:8B16^@20"
- "B32@0:8@\"CPLRecordChange\"16^@24"
- "B32@0:8@\"CPLScopedIdentifier\"16^@24"
- "B32@0:8@\"CPLUploadPushedChangesTask\"16@\"CPLEngineStoreTransaction\"24"
- "B32@0:8@\"NSString\"16#24"
- "B32@0:8@16#24"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8@16^B24"
- "B32@0:8@16d24"
- "B32@0:8@16q24"
- "B32@0:8@?16^@24"
- "B32@0:8Q16@24"
- "B32@0:8Q16Q24"
- "B32@0:8Q16^@24"
- "B32@0:8^@16@24"
- "B32@0:8^@16^@24"
- "B32@0:8^Q16@24"
- "B32@0:8q16@24"
- "B32@?0@\"CPLBrokenScope\"8Q16^B24"
- "B36@0:8@16B24^@28"
- "B36@0:8B16@20^@28"
- "B36@0:8B16^Q20^@28"
- "B40@0:8#16@24^@32"
- "B40@0:8@16#24^@32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@24^B32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^?24^@32"
- "B40@0:8@16^@24^@32"
- "B40@0:8@16^@24^B32"
- "B40@0:8@16^B24^@32"
- "B40@0:8@16q24@32"
- "B40@0:8@16q24^@32"
- "B40@0:8Q16@24^@32"
- "B40@0:8Q16^Q24^@32"
- "B40@0:8^@16^B24@32"
- "B40@0:8^B16^Q24^@32"
- "B40@0:8d16@24^@32"
- "B40@0:8o^@16@24o^@32"
- "B40@0:8o^@16Q24^@32"
- "B40@0:8q16@24^@32"
- "B44@0:8@16#24B32^@36"
- "B44@0:8@16@24B32^@36"
- "B44@0:8@16B24Q28^@36"
- "B44@0:8@16B24^B28^@36"
- "B44@0:8@16B24^Q28^@36"
- "B44@0:8@16Q24B32^@36"
- "B44@0:8B16q20@28^@36"
- "B44@0:8Q16^Q24B32^@36"
- "B48@0:8@\"CPLUploadPushedChangesTask\"16^@24^B32@\"CPLEngineStoreTransaction\"40"
- "B48@0:8@16#24@32^@40"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24@32@?40"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24B32B36^@40"
- "B48@0:8@16@24^B32^@40"
- "B48@0:8@16@24q32^@40"
- "B48@0:8@16Q24@32Q40"
- "B48@0:8@16Q24Q32^@40"
- "B48@0:8@16Q24^B32^@40"
- "B48@0:8@16^@24^B32@40"
- "B48@0:8@16q24@32^@40"
- "B48@0:8@16q24^B32^@40"
- "B48@0:8Q16Q24@32^@40"
- "B48@0:8^@16@24Q32^@40"
- "B48@0:8q16@24Q32^@40"
- "B48@0:8q16q24^q32^@40"
- "B52@0:8@\"CPLScopedIdentifier\"16@\"CPLScopedIdentifier\"24B32Q36^@44"
- "B52@0:8@16@24B32Q36^@44"
- "B52@0:8@16@24B32^B36^@44"
- "B52@0:8@16B24#28@36^@44"
- "B56@0:8@16@24@32@?40^@48"
- "B56@0:8@16@24B32B36^B40^@48"
- "B56@0:8@16@24Q32Q40@48"
- "B56@0:8@16@24^B32^@40^@48"
- "B56@0:8@16Q24^B32^Q40^@48"
- "B56@0:8^@16^@24@32@40@48"
- "B72@0:8@16@24@32@40^@48@?56^@64"
- "B88@0:8@16@24#32@40@48@56@64@72^@80"
- "Broken scope detected: %@\n%@"
- "Button pressed is %@"
- "CPLAbstractObject"
- "CPLAccountFlags"
- "CPLActiveDownloadQueue"
- "CPLAdditions"
- "CPLAdjustments"
- "CPLAlbumChange"
- "CPLAllowBackgroundOperationsBoost"
- "CPLAllowCancellingDerivativesGeneration"
- "CPLAllowDeferringDerivativesGeneration"
- "CPLAllowOperationsBoost"
- "CPLArchiver"
- "CPLAssetChange"
- "CPLAssetKeywordSortDescriptor"
- "CPLBackgroundActivity"
- "CPLBackgroundDownloadsTask"
- "CPLBatchExtractionStep"
- "CPLBatchExtractionStrategy"
- "CPLBatchExtractionStrategyStorage"
- "CPLBatteryMonitor"
- "CPLBatteryMonitorDelegate"
- "CPLBeforeUploadCheckItem"
- "CPLBeforeUploadCheckItems"
- "CPLBeforeUploadCheckItemsProvider"
- "CPLBrokenScope"
- "CPLByClassExtractionStep"
- "CPLCallObserver"
- "CPLChangeBatch"
- "CPLChangeBatchChangeStorage"
- "CPLChangeSession"
- "CPLChangeSessionContext"
- "CPLChangeSessionImplementation"
- "CPLChangeSessionUpdate"
- "CPLChangeStorage"
- "CPLChangedRecordStorageView"
- "CPLChangedRecordView"
- "CPLCleanupTask"
- "CPLClientCacheBaseView"
- "CPLClientCacheRecordView"
- "CPLClientCacheView"
- "CPLClientLibraryManagerProtocol"
- "CPLCloudCacheBaseView"
- "CPLCodingPropertyEntry"
- "CPLCodingProxy"
- "CPLCollectionShareScopeChange"
- "CPLCommentChange"
- "CPLConfiguration"
- "CPLConfigurationDictionary"
- "CPLConfigurationFetcher"
- "CPLConfigurationFetcherDelegate"
- "CPLContainerChange"
- "CPLContainerRelation"
- "CPLContainerRelationChange"
- "CPLCopying"
- "CPLDaemonLibraryManagerMinimalProtocol"
- "CPLDaemonLibraryManagerProtocol"
- "CPLDateFormatter"
- "CPLDeleteChainedRecordExtractionStep"
- "CPLDerivativesFilter"
- "CPLDerivativesGenerationStatistics"
- "CPLDiffTracker"
- "CPLDropAllRecordsExtractionStep"
- "CPLDropDerivativesRecipe"
- "CPLEngineBackupSyncTask"
- "CPLEngineBlocker"
- "CPLEngineChangePipe"
- "CPLEngineCloudCache"
- "CPLEngineComponent"
- "CPLEngineComponentEnumerator"
- "CPLEngineDequeueObserver"
- "CPLEngineDerivativesCache"
- "CPLEngineDownloadSyncTask"
- "CPLEngineFeedbackManager"
- "CPLEngineFileStorage"
- "CPLEngineForceProcessingStagedScopesTask"
- "CPLEngineForceSyncTask"
- "CPLEngineForceSyncTaskDelegate"
- "CPLEngineIDMapping"
- "CPLEngineIgnoredRecords"
- "CPLEngineLibrary"
- "CPLEngineMultiscopeSyncTask"
- "CPLEngineOutgoingResources"
- "CPLEnginePendingRecordChecks"
- "CPLEnginePushRepository"
- "CPLEngineQuarantinedRecords"
- "CPLEngineRecordComputeStatePushQueue"
- "CPLEngineRemappedRecords"
- "CPLEngineResourceDownloadQueue"
- "CPLEngineResourceDownloadTask"
- "CPLEngineResourceStorage"
- "CPLEngineResourceUploadTask"
- "CPLEngineRevertRecords"
- "CPLEngineScheduler"
- "CPLEngineSchedulerBlocker"
- "CPLEngineScope"
- "CPLEngineScopeCleanupTasks"
- "CPLEngineScopeFlagsUpdate"
- "CPLEngineScopeStatusFormatter"
- "CPLEngineScopeStorage"
- "CPLEngineScopedTask"
- "CPLEngineStatusCenter"
- "CPLEngineStorage"
- "CPLEngineStorageViews"
- "CPLEngineStore"
- "CPLEngineStoreTransaction"
- "CPLEngineSyncManager"
- "CPLEngineSyncManagerForcedTask"
- "CPLEngineSyncTask"
- "CPLEngineSyncTaskDelegate"
- "CPLEngineSystemMonitor"
- "CPLEngineTransientRepository"
- "CPLEngineTransientRepositoryBatchStorage"
- "CPLEngineTransientRepositoryObserver"
- "CPLEngineTransport"
- "CPLEngineWriteTransactionBlocker"
- "CPLErrors"
- "CPLExpungeableResourceState"
- "CPLExtractedBatch"
- "CPLFaceAnalysis"
- "CPLFaceAnalysisReference"
- "CPLFaceCropChange"
- "CPLFaceInstance"
- "CPLFeature"
- "CPLFeatureVersionHistory"
- "CPLFeedbackMessage"
- "CPLFileStorageItem"
- "CPLFileWatcher"
- "CPLFingerprintContext"
- "CPLFingerprintScheme"
- "CPLFingerprintSchemeInvalid"
- "CPLFingerprintSchemeV1"
- "CPLFingerprintSchemeV2"
- "CPLForceEPPSupport"
- "CPLForceSyncTask"
- "CPLHardcodedFingerprintSchemeV2"
- "CPLIDMapping"
- "CPLIgnoredRecord"
- "CPLInMemoryResourceDownloadTask"
- "CPLInfoFeedbackMessage"
- "CPLInvalidBatchStorage"
- "CPLItemChange"
- "CPLLibraryInfo"
- "CPLLibraryManager"
- "CPLLibraryManagerDelegate"
- "CPLLibraryManagerImplementation"
- "CPLLibraryScopeChange"
- "CPLLibraryShareScopeChange"
- "CPLLibraryState"
- "CPLManagement"
- "CPLMapEnumerator"
- "CPLMasterChange"
- "CPLMemoryAsset"
- "CPLMemoryAssetFlag"
- "CPLMemoryAssetList"
- "CPLMemoryChange"
- "CPLMetrics"
- "CPLMingleChangesScopeTask"
- "CPLMingleChangesTask"
- "CPLMingleUtility"
- "CPLMomentShare"
- "CPLMomentShareFeature"
- "CPLMomentShareParticipant"
- "CPLMomentSharePreviewData"
- "CPLMomentShareScopeChange"
- "CPLNSCoding"
- "CPLNetworkIndicator"
- "CPLNetworkState"
- "CPLNetworkWatcher"
- "CPLNetworkWatcherDelegate"
- "CPLNewAssetExtractionStep"
- "CPLNewChainedRecordExtractionStep"
- "CPLPersonChange"
- "CPLPersonReference"
- "CPLPlaceAnnotation"
- "CPLPlaceholderRecord"
- "CPLPlatform"
- "CPLPlatformImplementation"
- "CPLPlatformObject"
- "CPLPowerAssertion"
- "CPLPredictionDateFormatter"
- "CPLPreventAssetTrashAndDeleteGatekeeper"
- "CPLProcessStagedScopesScopeTask"
- "CPLProcessStagedScopesTask"
- "CPLProposeBrokenScopeRecovery"
- "CPLProxyForceSyncTask"
- "CPLProxyImplementation"
- "CPLProxyLibraryManager"
- "CPLProxyLibraryManagerOutstandingInvocation"
- "CPLProxyLibraryManagerSyncOutstandingInvocation"
- "CPLProxyPullSession"
- "CPLProxyPushSession"
- "CPLProxyResourceTransferTask"
- "CPLProxySession"
- "CPLPullChangeSession"
- "CPLPullChangeSessionImplementation"
- "CPLPullFromTransportScopeTask"
- "CPLPullFromTransportTask"
- "CPLPullScopesTask"
- "CPLPullSessionRevertRecords"
- "CPLPullSessionScopesAcknowledgement"
- "CPLPullSessionUpdate"
- "CPLPushChangeSession"
- "CPLPushChangeSessionImplementation"
- "CPLPushChangeTasks"
- "CPLPushPullGatekeeper"
- "CPLPushRepositoryStorage"
- "CPLPushSessionTracker"
- "CPLPushSessionUpdate"
- "CPLPushToTransportScopeTask"
- "CPLPushToTransportSyncStep"
- "CPLPushToTransportTask"
- "CPLQuarantineFeedbackMessage"
- "CPLRampingRequest"
- "CPLRampingRequestResource"
- "CPLRampingResponse"
- "CPLRampingResponseResource"
- "CPLReactChange"
- "CPLRecordChange"
- "CPLRecordChangeDiffTracker"
- "CPLRecordComputeState"
- "CPLRecordComputeStateValidator"
- "CPLRecordComputeStateVersion"
- "CPLRecordPushContext"
- "CPLRecordStatus"
- "CPLRecordStorageView"
- "CPLRecordTarget"
- "CPLRecordTargetMapping"
- "CPLRecordView"
- "CPLRecordViewExtensions"
- "CPLReference"
- "CPLRejectedRecords"
- "CPLResetFeedbackMessage"
- "CPLResetReason"
- "CPLResetTracker"
- "CPLReshareScopeTask"
- "CPLReshareTask"
- "CPLResource"
- "CPLResourceIdentity"
- "CPLResourceIdentityImplementation"
- "CPLResourceTransferTask"
- "CPLResourceTransferTaskOptions"
- "CPLResourceTypeSet"
- "CPLSafeArchiving"
- "CPLScopeChange"
- "CPLScopeFilter"
- "CPLScopeStatusCounts"
- "CPLScopeUpdateScopeTask"
- "CPLScopeUpdateTask"
- "CPLScopedIdentifier"
- "CPLSerializedFeedbackMessage"
- "CPLServerFeedbackKeyAndValue"
- "CPLServerFeedbackMessage"
- "CPLServerFeedbackRequest"
- "CPLServerFeedbackResponse"
- "CPLSettingFeedbackMessage"
- "CPLShare"
- "CPLShareParticipant"
- "CPLSharedBatchStorage"
- "CPLSharedRecordMerger"
- "CPLSharedRecordPropertyMapping"
- "CPLSharedRemapFixUpTask"
- "CPLSharedSimplePropertyMapping"
- "CPLSimpleMergeHelper"
- "CPLSimpleMerger"
- "CPLSimpleRecordTargetMapping"
- "CPLSimpleRecordView"
- "CPLSimpleTaskSyncStep"
- "CPLSocialGroupChange"
- "CPLSocialGroupPerson"
- "CPLSocialGroupPersonList"
- "CPLStagingScopeChange"
- "CPLStatus"
- "CPLStatusDelegate"
- "CPLSuggestionAsset"
- "CPLSuggestionAssetFlag"
- "CPLSuggestionChange"
- "CPLSuggestionMemory"
- "CPLSuggestionPerson"
- "CPLSuggestionRecordList"
- "CPLSyncAnchorDescription"
- "CPLSyncIndicator"
- "CPLSyncSession"
- "CPLSyncSessionBlockedState"
- "CPLSyncSessionConfiguration"
- "CPLSyncSessionPrediction"
- "CPLSyncSessionPredictor"
- "CPLSyncSessionPredictorObserver"
- "CPLSyncSessionThroughputMetrics"
- "CPLSyncSessionThroughputReporting"
- "CPLSyncStep"
- "CPLSyncThroughputReporter"
- "CPLSyncThroughputReporterDelegate"
- "CPLTestFeedbackMessage"
- "CPLTextCommentChange"
- "CPLTransaction"
- "CPLTransferSpeedFormatter"
- "CPLTransientRepositoryStorage"
- "CPLTransportScopeMapping"
- "CPLTransportScopeTranslator"
- "CPLTransportUpdateScopeTask"
- "CPLTransportUpdateTask"
- "CPLTrashedAssetExtractionStep"
- "CPLUnacknowledgedChangeStorage"
- "CPLUnionEnumerator"
- "CPLUploadComputeStatesAccumulator"
- "CPLUploadComputeStatesScopeTask"
- "CPLUploadComputeStatesTask"
- "CPLUploadPushedChangesTask"
- "CPLUploadPushedChangesTaskDelegate"
- "Changing extraction strategy from %@ to %@"
- "Classification"
- "Clean-up For Me"
- "Client failed to properly re-enable %@ - will do it directly"
- "Client pushed a delete to an already deleted record: %@ - ignoring"
- "Client pushed a record to an invalid scope: %@"
- "CloudPhotoLibrary-852.0.102"
- "ComponentID"
- "ComponentName"
- "ComponentVersion"
- "Could not create user notification for broken scope %@: %d"
- "Create Radar"
- "Creating %@ in %@ (storage: %@/resources: %@)"
- "DefaultsSupport"
- "Description"
- "Disabling initial queries for %@ after a reset of sync anchor"
- "E"
- "EPPAutoEnable"
- "EPPCapable"
- "ExtensionIdentifiers"
- "FIFOQueue"
- "Failed to auto-enable %@: %@"
- "Failed to clean-up library"
- "Failed to clean-up: %@"
- "I"
- "I16@0:8"
- "Informing transport of significant work beginning"
- "Informing transport of significant work ending"
- "Launching %@ for %ld scopes"
- "Launching %@ for %ld scopes (ignored %ld)"
- "Library has been cleaned up successfully."
- "Library has broken scope %@ (%@)"
- "Library has remains of shared library and must be cleaned before synchronization can continue."
- "Library has unsupported scopes and must be cleaned before synchronization can continue."
- "NSCoding"
- "NSCopying"
- "NSFastEnumeration"
- "NSObject"
- "NSSecureCoding"
- "NSXPCConnectionDelegate"
- "Not Applicable"
- "OK"
- "Other Bug"
- "Photos Backend iCloud"
- "Q16@0:8"
- "Q24@0:8@\"NSString\"16"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q24@0:8d16"
- "Q32@0:8@16#24"
- "Q32@0:8@16^@24"
- "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
- "RadiosPreferencesDelegate"
- "Read More"
- "Removing just-in-case from %@ as it has been associated with a rescheduler"
- "Reproducibility"
- "S16@0:8"
- "Set up reset sync download transport group for %@ to %@"
- "Set up reset sync upload transport group for %@ to %@"
- "StringAsReason:"
- "SystemBudgetOverride"
- "T#,&,N,V_derivativeGeneratorClass"
- "T#,R"
- "T#,R,N"
- "T#,R,N,V_changeClass"
- "T#,R,N,V_extractionClass"
- "T#,R,N,V_recordClass"
- "T#,R,N,V_relatedRecordClass"
- "T#,R,N,V_taskClass"
- "T:,N,V_propertyGetter"
- "T:,N,V_propertySetter"
- "T@\"<CPLAbstractObject>\",R,W,N,V_abstractObject"
- "T@\"<CPLBatchExtractionStrategyStorage>\",R,N,V_storage"
- "T@\"<CPLBatchExtractionStrategyStorage>\",R,W,N,V_storage"
- "T@\"<CPLBatteryMonitorDelegate>\",W,N"
- "T@\"<CPLBeforeUploadCheckItemsProvider>\",R,N,V_provider"
- "T@\"<CPLConfigurationFetcherDelegate>\",R,W,N,V_delegate"
- "T@\"<CPLEngineForceSyncTaskDelegate>\",W,N,V_delegate"
- "T@\"<CPLEngineIDMapping>\",R,N,V_idMapping"
- "T@\"<CPLEngineLibraryOwner>\",W,N,V_owner"
- "T@\"<CPLEngineLibrarySupervisor>\",&,N,V_supervisor"
- "T@\"<CPLEngineStoreUserIdentifier>\",&,N"
- "T@\"<CPLEngineStoreUserIdentifier>\",&,N,V_transportUserIdentifier"
- "T@\"<CPLEngineSyncTaskDelegate>\",&,V_delegate"
- "T@\"<CPLEngineTransportGroup>\",R,N,V_storedTransportGroup"
- "T@\"<CPLEngineTransportResourcesDownloadTask>\",W,N,V_transportTask"
- "T@\"<CPLEngineTransportTask>\",&,N,V_transportTask"
- "T@\"<CPLFileWatcherDelegate>\",W,N,V_delegate"
- "T@\"<CPLLibraryManagerDelegate>\",W,N,V_delegate"
- "T@\"<CPLLibraryManagerForceSyncDelegate>\",W,N,V_forceSyncDelegate"
- "T@\"<CPLLibraryManagerOwner>\",W,N,V_owner"
- "T@\"<CPLNetworkWatcherDelegate>\",W,N,V_delegate"
- "T@\"<CPLRecordComputeStateDelegate>\",W,N,V_recordComputeStateDelegate"
- "T@\"<CPLResourceProgressDelegate>\",W,N,V_resourceProgressDelegate"
- "T@\"<CPLSharedRecordMerger>\",R,N,V_merger"
- "T@\"<CPLSharedRecordPropertyMapping>\",R,N"
- "T@\"<CPLSharedRecordPropertyMapping>\",R,N,V_mapping"
- "T@\"<CPLStatusDelegate>\",W,N,V_delegate"
- "T@\"<CPLSyncSessionConfiguration>\",R,N"
- "T@\"<CPLSyncSessionRescheduler>\",&,N,V_rescheduler"
- "T@\"<CPLSyncSessionRescheduler>\",R,N,V_rescheduler"
- "T@\"<CPLSyncSessionRuntimeCharacteristics>\",R"
- "T@\"<CPLSyncSessionRuntimeCharacteristics>\",R,V_runtimeCharacteristics"
- "T@\"<CPLSyncThroughputReporterDelegate>\",W,N,V_delegate"
- "T@\"<CPLTransportScopeTranslator>\",R,N,V_translator"
- "T@\"<CPLUploadPushedChangesTaskDelegate>\",&,D"
- "T@\"<NSFastEnumeration>\",R,N"
- "T@\"<_CPLScheduledOverrideDelegate>\",W,N,V_delegate"
- "T@\"CLLocation\",&,N,V_location"
- "T@\"CPLAccountFlags\",R,N"
- "T@\"CPLAdjustments\",&,N,V_adjustments"
- "T@\"CPLBackgroundActivity\",&,N"
- "T@\"CPLBackgroundActivity\",&,N,V_detachedActivity"
- "T@\"CPLBatchExtractionStrategy\",&,N"
- "T@\"CPLBeforeUploadCheckItems\",R,W,N,V_items"
- "T@\"CPLChangeBatch\",R,N"
- "T@\"CPLChangeBatch\",R,N,V_batch"
- "T@\"CPLChangeBatch\",R,N,V_clientBatch"
- "T@\"CPLChangeBatch\",R,N,V_cloudBatch"
- "T@\"CPLChangeBatch\",R,N,V_diffBatch"
- "T@\"CPLChangeBatch\",R,N,V_diffedBatch"
- "T@\"CPLChangeBatch\",R,N,V_expandedBatch"
- "T@\"CPLChangeBatch\",R,N,V_incomingBatch"
- "T@\"CPLChangeBatch\",R,N,V_originalBatch"
- "T@\"CPLChangeBatch\",R,N,V_revertedChangesBatch"
- "T@\"CPLChangeBatch\",R,N,V_scopesChangeBatch"
- "T@\"CPLChangeStorage\",R,N,V_changeStorage"
- "T@\"CPLConfiguration\",R,N"
- "T@\"CPLConfiguration\",R,N,V_configuration"
- "T@\"CPLConfigurationDictionary\",R"
- "T@\"CPLContainerRelation\",&,N,V_relation"
- "T@\"CPLEngineChangePipe\",R,N,V_pullQueue"
- "T@\"CPLEngineCloudCache\",R,N,V_cloudCache"
- "T@\"CPLEngineDerivativesCache\",R,N,V_derivativesCache"
- "T@\"CPLEngineFeedbackManager\",R,N,V_feedback"
- "T@\"CPLEngineFileStorage\",R,N,V_fileStorage"
- "T@\"CPLEngineIDMapping\",R,N,V_idMapping"
- "T@\"CPLEngineIgnoredRecords\",R,N,V_ignoredRecords"
- "T@\"CPLEngineLibrary\",&,N,V_engineLibrary"
- "T@\"CPLEngineLibrary\",R,N"
- "T@\"CPLEngineLibrary\",R,N,V_engineLibrary"
- "T@\"CPLEngineLibrary\",R,W,N,V_engineLibrary"
- "T@\"CPLEngineOutgoingResources\",R,N,V_outgoingResources"
- "T@\"CPLEnginePendingRecordChecks\",R,N,V_pendingRecordChecks"
- "T@\"CPLEnginePushRepository\",R,N,V_pushRepository"
- "T@\"CPLEngineQuarantinedRecords\",R,N,V_quarantinedRecords"
- "T@\"CPLEngineRecordComputeStatePushQueue\",R,N,V_recordComputeStatePushQueue"
- "T@\"CPLEngineRemappedRecords\",R,N,V_remappedRecords"
- "T@\"CPLEngineResourceDownloadQueue\",R,N,V_downloadQueue"
- "T@\"CPLEngineResourceStorage\",R,N,V_resourceStorage"
- "T@\"CPLEngineRevertRecords\",R,N,V_revertRecords"
- "T@\"CPLEngineScheduler\",R,N,V_scheduler"
- "T@\"CPLEngineScheduler\",R,W,N,V_scheduler"
- "T@\"CPLEngineSchedulerBlocker\",R,N,V_schedulerBlocker"
- "T@\"CPLEngineScope\",&,N,V_scope"
- "T@\"CPLEngineScope\",R,N,V_engineScope"
- "T@\"CPLEngineScope\",R,N,V_scope"
- "T@\"CPLEngineScope\",R,N,V_sharedScope"
- "T@\"CPLEngineScopeCleanupTasks\",R,N,V_cleanupTasks"
- "T@\"CPLEngineScopeStorage\",R,N,V_scopes"
- "T@\"CPLEngineStatusCenter\",R,N,V_statusCenter"
- "T@\"CPLEngineStore\",R,N"
- "T@\"CPLEngineStore\",R,N,V_engineStore"
- "T@\"CPLEngineStore\",R,N,V_store"
- "T@\"CPLEngineStore\",R,W,N,V_store"
- "T@\"CPLEngineStoreTransaction\",R,N"
- "T@\"CPLEngineSyncManager\",R,N,V_syncManager"
- "T@\"CPLEngineSyncTask\",R,N,V_currentTask"
- "T@\"CPLEngineSystemMonitor\",R,N,V_systemMonitor"
- "T@\"CPLEngineTransientRepository\",R,N,V_transientPullRepository"
- "T@\"CPLEngineTransientRepository\",R,N,V_transientRepository"
- "T@\"CPLEngineTransport\",R,N,V_transport"
- "T@\"CPLEngineWriteTransactionBlocker\",&,N,V_blocker"
- "T@\"CPLEngineWriteTransactionBlocker\",R,N,V_writeTransactionBlocker"
- "T@\"CPLFaceAnalysisReference\",C,N"
- "T@\"CPLFeatureVersionHistory\",&,N,V_featureVersionHistory"
- "T@\"CPLFingerprintContext\",&"
- "T@\"CPLFingerprintContext\",R"
- "T@\"CPLFingerprintContext\",R,N"
- "T@\"CPLFingerprintContext\",R,N,V_fingerprintContext"
- "T@\"CPLFingerprintScheme\",R,N"
- "T@\"CPLFingerprintSchemeV1\",R,N"
- "T@\"CPLFingerprintSchemeV1\",R,V_mmcsv1FingerprintScheme"
- "T@\"CPLFingerprintSchemeV2\",R,V_mmcsv2FingerprintScheme"
- "T@\"CPLHardcodedFingerprintSchemeV2\",R"
- "T@\"CPLLibraryInfo\",&,N,V_libraryInfo"
- "T@\"CPLLibraryManager\",R,N,V_libraryManager"
- "T@\"CPLLibraryManager\",W,V_weakLibraryManager"
- "T@\"CPLLibraryState\",&,N,V_libraryState"
- "T@\"CPLMemoryAssetFlag\",&,N,V_assetFlag"
- "T@\"CPLMemoryAssetList\",C,N,V_assetList"
- "T@\"CPLMemoryAssetList\",C,N,V_customUserAssetList"
- "T@\"CPLMomentShare\",&,N,V_momentShare"
- "T@\"CPLNetworkState\",R,N,V_networkState"
- "T@\"CPLPlaceAnnotation\",&,N,V_placeAnnotation"
- "T@\"CPLPlaceholderRecord\",R,N"
- "T@\"CPLPlaceholderRecord\",R,N,V_cloudRecord"
- "T@\"CPLPlatformObject\",R,N"
- "T@\"CPLPlatformObject\",R,N,V_platformObject"
- "T@\"CPLProxyLibraryManager\",&,N,V_proxyLibraryManager"
- "T@\"CPLPushChangeTasks\",R,N,V_pushChangeTasks"
- "T@\"CPLRecordChange\",R,N"
- "T@\"CPLRecordChange\",R,N,V_change"
- "T@\"CPLRecordChange\",R,N,V_cloudRecord"
- "T@\"CPLRecordChange\",R,N,V_record"
- "T@\"CPLRecordStatus\",R,N"
- "T@\"CPLRecordStorageView\",R,N,V_baseStorageView"
- "T@\"CPLRecordStorageView\",R,N,V_transactionClientCacheView"
- "T@\"CPLRecordTarget\",R,N"
- "T@\"CPLRecordTarget\",R,N,V_target"
- "T@\"CPLRecordTargetMapping\",R,N,V_targetMapping"
- "T@\"CPLRecordView\",R,N,V_baseRecordView"
- "T@\"CPLResetTracker\",&,N,V_resetTracker"
- "T@\"CPLResetTracker\",R"
- "T@\"CPLResource\",&,N,V_adjustmentData"
- "T@\"CPLResource\",&,N,V_cloudResource"
- "T@\"CPLResource\",&,N,V_finalResource"
- "T@\"CPLResource\",R,N,V_cloudResource"
- "T@\"CPLResource\",R,N,V_resource"
- "T@\"CPLResource\",R,N,V_sourceResource"
- "T@\"CPLResourceIdentity\",&,N,V_identity"
- "T@\"CPLResourceIdentity\",R,N,V_identity"
- "T@\"CPLResourceTransferTaskOptions\",C,N"
- "T@\"CPLScopeChange\",C,N,V_stagedScopeChange"
- "T@\"CPLScopeFilter\",&,N,V_filter"
- "T@\"CPLScopeFilter\",R,N,V_scopeFilter"
- "T@\"CPLScopedIdentifier\",C,D,N"
- "T@\"CPLScopedIdentifier\",C,N,V_itemScopedIdentifier"
- "T@\"CPLScopedIdentifier\",C,N,V_resourceCopyFromScopedIdentifier"
- "T@\"CPLScopedIdentifier\",C,N,V_scopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N"
- "T@\"CPLScopedIdentifier\",R,N,V_itemScopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_otherScopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_privateCloudScopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_proposedPrivateScopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_realCloudScopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_scopedIdentifier"
- "T@\"CPLScopedIdentifier\",R,N,V_sharedCloudScopedIdentifier"
- "T@\"CPLServerFeedbackMessage\",R,N"
- "T@\"CPLServerFeedbackMessage\",R,N,V_serverMessage"
- "T@\"CPLShare\",&,N,V_share"
- "T@\"CPLShareParticipant\",R,N"
- "T@\"CPLSocialGroupPersonList\",&,N"
- "T@\"CPLStatus\",R,N"
- "T@\"CPLSuggestionAssetFlag\",&,N,V_assetFlag"
- "T@\"CPLSuggestionRecordList\",C,N,V_recordList"
- "T@\"CPLSyncSession\",R,N,V_session"
- "T@\"CPLSyncSession\",R,N,V_syncSession"
- "T@\"CPLSyncSessionPrediction\",R,V_currentPrediction"
- "T@\"CPLSyncSessionPredictor\",R,N,V_predictor"
- "T@\"CPLSyncSessionThroughputMetrics\",&,N,V_metrics"
- "T@\"CPLTransportScopeMapping\",&,N,V_transportScopeMapping"
- "T@\"CPLTransportScopeMapping\",R,N,V_transactionTransportScopeMapping"
- "T@\"CPLTransportScopeMapping\",R,N,V_transportScopeMapping"
- "T@\"CPLUploadPushedChangesTask\",R,V_currentSubtask"
- "T@\"NSArray\",C,N"
- "T@\"NSArray\",C,N,V_containerRelations"
- "T@\"NSArray\",C,N,V_expungeableResourceStates"
- "T@\"NSArray\",C,N,V_keywords"
- "T@\"NSArray\",C,N,V_participants"
- "T@\"NSArray\",C,N,V_people"
- "T@\"NSArray\",C,N,V_resources"
- "T@\"NSArray\",C,N,V_sharingContributorUserIdentifiers"
- "T@\"NSArray\",C,N,V_updateSharingContributorUserIdentifiers"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,C,N,V_resetReasons"
- "T@\"NSArray\",R,C,N,V_scopeIdentifiers"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_addedRecords"
- "T@\"NSArray\",R,N,V_deletedRecordScopedIdentifiers"
- "T@\"NSArray\",R,N,V_derivativeTypes"
- "T@\"NSArray\",R,N,V_revertedChanges"
- "T@\"NSArray\",R,N,V_updatedRecords"
- "T@\"NSByteCountFormatter\",R,N,V_byteCountFormatter"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_actionData"
- "T@\"NSData\",&,N,V_adjustedMediaMetaData"
- "T@\"NSData\",&,N,V_assetMovieData"
- "T@\"NSData\",&,N,V_finalData"
- "T@\"NSData\",&,N,V_mediaMetaData"
- "T@\"NSData\",&,N,V_simpleAdjustmentData"
- "T@\"NSData\",C"
- "T@\"NSData\",C,N"
- "T@\"NSData\",C,N,V_accountFlagsData"
- "T@\"NSData\",C,N,V_actionData"
- "T@\"NSData\",C,N,V_assetListPredicate"
- "T@\"NSData\",C,N,V_blacklistedFeature"
- "T@\"NSData\",C,N,V_contactDescriptor"
- "T@\"NSData\",C,N,V_facesData"
- "T@\"NSData\",C,N,V_featuresData"
- "T@\"NSData\",C,N,V_graphData"
- "T@\"NSData\",C,N,V_movieData"
- "T@\"NSData\",C,N,V_personsData"
- "T@\"NSData\",C,N,V_previewData"
- "T@\"NSData\",C,N,V_previewImageData"
- "T@\"NSData\",C,N,V_projectData"
- "T@\"NSData\",C,N,V_projectPreviewImageData"
- "T@\"NSData\",C,N,V_recordChangeData"
- "T@\"NSData\",C,N,V_resourceData"
- "T@\"NSData\",C,N,V_rewindAnchorsPerSharingScopesData"
- "T@\"NSData\",C,N,V_sharingRecordChangeData"
- "T@\"NSData\",C,N,V_stagedTransportScope"
- "T@\"NSData\",C,N,V_thumbnailImageData"
- "T@\"NSData\",C,N,V_transportShare"
- "T@\"NSData\",C,N,V_userDefinedRules"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,N,V_boundaryKey"
- "T@\"NSData\",R,N,V_transportScope"
- "T@\"NSDate\",&,N,V_computeStateLastUpdatedDate"
- "T@\"NSDate\",&,N,V_creationDate"
- "T@\"NSDate\",&,N,V_lastViewedDate"
- "T@\"NSDate\",&,N,V_startTime"
- "T@\"NSDate\",C,D,N"
- "T@\"NSDate\",C,N"
- "T@\"NSDate\",C,N,V_activationDate"
- "T@\"NSDate\",C,N,V_addedDate"
- "T@\"NSDate\",C,N,V_adjustmentTimestamp"
- "T@\"NSDate\",C,N,V_assetDate"
- "T@\"NSDate\",C,N,V_commentDate"
- "T@\"NSDate\",C,N,V_creationDate"
- "T@\"NSDate\",C,N,V_dateDeleted"
- "T@\"NSDate\",C,N,V_deleteDate"
- "T@\"NSDate\",C,N,V_disabledDate"
- "T@\"NSDate\",C,N,V_endDate"
- "T@\"NSDate\",C,N,V_expiryDate"
- "T@\"NSDate\",C,N,V_expungeDate"
- "T@\"NSDate\",C,N,V_expungedDate"
- "T@\"NSDate\",C,N,V_importDate"
- "T@\"NSDate\",C,N,V_lastSharedDate"
- "T@\"NSDate\",C,N,V_now"
- "T@\"NSDate\",C,N,V_recordModificationDate"
- "T@\"NSDate\",C,N,V_relevantUntilDate"
- "T@\"NSDate\",C,N,V_startDate"
- "T@\"NSDate\",C,N,V_userModificationDate"
- "T@\"NSDate\",C,N,V_userViewedParticipantTrashNotificationDate"
- "T@\"NSDate\",C,V_throttlingDate"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,C,N,V_date"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSDate\",R,N,V_endDate"
- "T@\"NSDate\",R,N,V_expectedDate"
- "T@\"NSDate\",R,N,V_ignoredDate"
- "T@\"NSDate\",R,N,V_lastAccessDate"
- "T@\"NSDate\",R,N,V_lastUpdateDate"
- "T@\"NSDate\",R,N,V_lastUpdatedDate"
- "T@\"NSDate\",R,N,V_proposedRescheduleDate"
- "T@\"NSDate\",R,N,V_queuedDate"
- "T@\"NSDictionary\",&,N,V_errors"
- "T@\"NSDictionary\",C,N"
- "T@\"NSDictionary\",C,N,V_assetCounts"
- "T@\"NSDictionary\",C,N,V_extraProperties"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_countPerFlags"
- "T@\"NSDictionary\",R,N,V_info"
- "T@\"NSDictionary\",R,N,V_pushContexts"
- "T@\"NSDictionary\",R,N,V_recordWithStatusChangesToNotify"
- "T@\"NSError\",&,N,V_finalError"
- "T@\"NSError\",C,N,V_error"
- "T@\"NSError\",R,N"
- "T@\"NSError\",R,N,V_statusError"
- "T@\"NSMutableArray\",&,N,V_assets"
- "T@\"NSMutableArray\",&,N,V_curatedAssetIdentifiers"
- "T@\"NSMutableArray\",&,N,V_faceInstances"
- "T@\"NSMutableArray\",&,N,V_keysAndValues"
- "T@\"NSMutableArray\",&,N,V_memorys"
- "T@\"NSMutableArray\",&,N,V_messages"
- "T@\"NSMutableArray\",&,N,V_persons"
- "T@\"NSMutableArray\",&,N,V_petFaceInstances"
- "T@\"NSMutableArray\",&,N,V_previewImageDatas"
- "T@\"NSMutableArray\",&,N,V_rejectedPersonIdentifiers"
- "T@\"NSMutableArray\",&,N,V_requests"
- "T@\"NSMutableArray\",&,N,V_responses"
- "T@\"NSMutableArray\",&,N,V_torsoFaceInstances"
- "T@\"NSNumber\",C,N,V_featureCompatibleVersion"
- "T@\"NSNumber\",C,N,V_placeLevel"
- "T@\"NSNumber\",C,N,V_timeZoneOffset"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",W,N,V_delegateQueue"
- "T@\"NSObject<OS_nw_path>\",R,N,V_networkPath"
- "T@\"NSPersonNameComponents\",C,N,V_nameComponents"
- "T@\"NSProgress\",R,N,V_sessionProgress"
- "T@\"NSSet\",&,N,V_propertyClasses"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_deletedScopeIdentifiers"
- "T@\"NSSet\",R,N,V_differingProperties"
- "T@\"NSSet\",R,N,V_excludedScopeIdentifiers"
- "T@\"NSSet\",R,N,V_includedScopeIdentifiers"
- "T@\"NSSet\",R,N,V_scopeIdentifiersExcludedFromPushToTransport"
- "T@\"NSSet\",R,N,V_unquarantinedRecordScopedIdentifiers"
- "T@\"NSString\",&,N,V_assetIdentifier"
- "T@\"NSString\",&,N,V_clientBundleID"
- "T@\"NSString\",&,N,V_computeStateAdjustmentFingerprint"
- "T@\"NSString\",&,N,V_computeStateVersion"
- "T@\"NSString\",&,N,V_context"
- "T@\"NSString\",&,N,V_cropRectString"
- "T@\"NSString\",&,N,V_customTitle"
- "T@\"NSString\",&,N,V_key"
- "T@\"NSString\",&,N,V_keyAssetIdentifier"
- "T@\"NSString\",&,N,V_masterIdentifier"
- "T@\"NSString\",&,N,V_memoryIdentifier"
- "T@\"NSString\",&,N,V_personIdentifier"
- "T@\"NSString\",&,N,V_resource"
- "T@\"NSString\",&,N,V_value"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_accessibilityDescription"
- "T@\"NSString\",C,N,V_adjustedMediaMetaDataType"
- "T@\"NSString\",C,N,V_adjustmentCompoundVersion"
- "T@\"NSString\",C,N,V_adjustmentCreatorCode"
- "T@\"NSString\",C,N,V_adjustmentType"
- "T@\"NSString\",C,N,V_assetIdentifier"
- "T@\"NSString\",C,N,V_burstIdentifier"
- "T@\"NSString\",C,N,V_caption"
- "T@\"NSString\",C,N,V_clientCacheIdentifier"
- "T@\"NSString\",C,N,V_codec"
- "T@\"NSString\",C,N,V_commentText"
- "T@\"NSString\",C,N,V_containerIdentifier"
- "T@\"NSString\",C,N,V_contributorUserIdentifier"
- "T@\"NSString\",C,N,V_creatorCode"
- "T@\"NSString\",C,N,V_deletedByUserIdentifier"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_effectiveClientBundleIdentifier"
- "T@\"NSString\",C,N,V_email"
- "T@\"NSString\",C,N,V_extendedDescription"
- "T@\"NSString\",C,N,V_facesAdjustmentsFingerprint"
- "T@\"NSString\",C,N,V_fileStorageIdentifier"
- "T@\"NSString\",C,N,V_fileUTI"
- "T@\"NSString\",C,N,V_filename"
- "T@\"NSString\",C,N,V_fingerPrint"
- "T@\"NSString\",C,N,V_fullName"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_importGroupIdentifier"
- "T@\"NSString\",C,N,V_importedByBundleIdentifier"
- "T@\"NSString\",C,N,V_importedByDisplayName"
- "T@\"NSString\",C,N,V_itemIdentifier"
- "T@\"NSString\",C,N,V_itemType"
- "T@\"NSString\",C,N,V_masterIdentifier"
- "T@\"NSString\",C,N,V_mediaGroupIdentifier"
- "T@\"NSString\",C,N,V_mediaMetaDataType"
- "T@\"NSString\",C,N,V_mergeTargetPersonIdentifier"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_originatingFingerprint"
- "T@\"NSString\",C,N,V_originatingScopeIdentifier"
- "T@\"NSString\",C,N,V_otherAdjustmentsFingerprint"
- "T@\"NSString\",C,N,V_parentIdentifier"
- "T@\"NSString\",C,N,V_participantID"
- "T@\"NSString\",C,N,V_personIdentifier"
- "T@\"NSString\",C,N,V_phoneNumber"
- "T@\"NSString\",C,N,V_placeName"
- "T@\"NSString\",C,N,V_problematicFormerSharedScopeIdentifier"
- "T@\"NSString\",C,N,V_projectDocumentType"
- "T@\"NSString\",C,N,V_realIdentifier"
- "T@\"NSString\",C,N,V_rejectedPersonIdentifier"
- "T@\"NSString\",C,N,V_sharingRecordIdentifier"
- "T@\"NSString\",C,N,V_sharingScopeIdentifier"
- "T@\"NSString\",C,N,V_similarToOriginalAdjustmentsFingerprint"
- "T@\"NSString\",C,N,V_stableHash"
- "T@\"NSString\",C,N,V_stagingScopeIdentifier"
- "T@\"NSString\",C,N,V_structName"
- "T@\"NSString\",C,N,V_subtitle"
- "T@\"NSString\",C,N,V_suffix"
- "T@\"NSString\",C,N,V_syndicationIdentifier"
- "T@\"NSString\",C,N,V_taskIdentifier"
- "T@\"NSString\",C,N,V_timeZoneName"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",C,N,V_transportIdentifier"
- "T@\"NSString\",C,N,V_userIdentifier"
- "T@\"NSString\",C,N,V_userOverride"
- "T@\"NSString\",C,V_phaseDescription"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_libraryIdentifier"
- "T@\"NSString\",R,C,N,V_libraryVersion"
- "T@\"NSString\",R,C,N,V_mainScopeIdentifier"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_queryDescription"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSString\",R,C,N,V_scopeIdentifier"
- "T@\"NSString\",R,C,N,V_strategyName"
- "T@\"NSString\",R,C,N,V_taskIdentifier"
- "T@\"NSString\",R,C,N,V_uuid"
- "T@\"NSString\",R,C,V_identifier"
- "T@\"NSString\",R,C,V_scopeIdentifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_adjustmentFingerprint"
- "T@\"NSString\",R,N,V_classDescription"
- "T@\"NSString\",R,N,V_clientCacheIdentifier"
- "T@\"NSString\",R,N,V_endPoint"
- "T@\"NSString\",R,N,V_feedbackType"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_libraryIdentifier"
- "T@\"NSString\",R,N,V_mainScopeIdentifier"
- "T@\"NSString\",R,N,V_metricsIdentifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_ownerIdentifier"
- "T@\"NSString\",R,N,V_reason"
- "T@\"NSString\",R,N,V_refreshIntervalKey"
- "T@\"NSString\",R,N,V_relatedIdentifier"
- "T@\"NSString\",R,N,V_resetType"
- "T@\"NSString\",R,N,V_scopeIdentifier"
- "T@\"NSString\",R,N,V_sessionIdentifier"
- "T@\"NSString\",R,N,V_settingName"
- "T@\"NSString\",R,N,V_statusKey"
- "T@\"NSString\",R,N,V_testMessage"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSString\",R,N,V_updateIntervalKey"
- "T@\"NSString\",R,N,V_uploadIdentifier"
- "T@\"NSString\",R,N,V_uti"
- "T@\"NSString\",R,N,V_uuid"
- "T@\"NSString\",R,N,V_value"
- "T@\"NSString\",R,N,V_version"
- "T@\"NSString\",R,N,V_zeroByteFileFingerprint"
- "T@\"NSString\",R,V_currentClosingComponentName"
- "T@\"NSURL\",C,N,V_URL"
- "T@\"NSURL\",C,N,V_fileURL"
- "T@\"NSURL\",C,N,V_shareURL"
- "T@\"NSURL\",R,C,N,V_cacheURL"
- "T@\"NSURL\",R,C,N,V_clientLibraryBaseURL"
- "T@\"NSURL\",R,C,N,V_cloudLibraryResourceStorageURL"
- "T@\"NSURL\",R,C,N,V_cloudLibraryStateStorageURL"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_baseURL"
- "T@\"NSURL\",R,N,V_configurationURL"
- "T@\"NSURL\",R,N,V_fileURL"
- "T@\"NSURL\",R,N,V_incomingDownloadFolderURL"
- "T@\"NSURL\",R,N,V_tempFolderURL"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@,&,N,V_archiveCursor"
- "T@,R,C,N"
- "T@,R,N"
- "T@?,C,N"
- "T@?,C,N,V_block"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_configurationDictionaryUniquifier"
- "T@?,C,N,V_requiredStateObserverBlock"
- "T@?,C,N,V_shouldBackOffOnErrorBlock"
- "T@?,C,N,V_taskDidFinishWithErrorBlock"
- "T@?,R,C,N,V_cancelHandler"
- "T@?,R,C,N,V_changePipeDidRemoveChanges"
- "T@?,R,C,N,V_clientDidAcknowledgeBatchBlock"
- "T@?,R,C,N,V_clientWillAcknowledgeBatchBlock"
- "T@?,R,C,N,V_completionHandler"
- "T@?,R,C,N,V_didStartHandler"
- "T@?,R,C,N,V_launchHandler"
- "T@?,R,C,N,V_progressHandler"
- "T@?,R,N,V_groupConstructor"
- "T@?,R,N,V_mapBlock"
- "TB"
- "TB,GisCancelled,S_setCancelled:,V_cancelled"
- "TB,N"
- "TB,N,GisActivated,V_activated"
- "TB,N,GisAvailable,V_available"
- "TB,N,GisBackgroundTask,V_backgroundTask"
- "TB,N,GisCancelledByEngine,V_cancelledByEngine"
- "TB,N,GisConfirmed"
- "TB,N,GisDisabled,V_disabled"
- "TB,N,GisFavorite,V_favorite"
- "TB,N,GisFull,V_full"
- "TB,N,GisHidden,V_hidden"
- "TB,N,GisHighPriority"
- "TB,N,GisInMemoryRequest,V_inMemoryRequest"
- "TB,N,GisKeyAsset,V_keyAsset"
- "TB,N,GisKeyFace"
- "TB,N,GisKeychainCDPEnabled"
- "TB,N,GisManual"
- "TB,N,GisQuarantined"
- "TB,N,GisReadOnly,V_readOnly"
- "TB,N,GisRejected,V_rejected"
- "TB,N,GisResetting"
- "TB,N,GisShared"
- "TB,N,GisUnknown"
- "TB,N,GisUpdating"
- "TB,N,GisUpgradeSuggestedToAccessAllPhotos"
- "TB,N,GisUploaded"
- "TB,N,GisUploading"
- "TB,N,GisWaitingForUpdate"
- "TB,N,GisWaitingForUpload"
- "TB,N,GisWalrusEnabled"
- "TB,N,V_albumSortAscending"
- "TB,N,V_allowed"
- "TB,N,V_bypassForceSyncLimitations"
- "TB,N,V_canGenerateDerivative"
- "TB,N,V_completed"
- "TB,N,V_defaultHEVC"
- "TB,N,V_deleteImmediately"
- "TB,N,V_didFinish"
- "TB,N,V_didStart"
- "TB,N,V_disableFeedback"
- "TB,N,V_forceSync"
- "TB,N,V_foreground"
- "TB,N,V_hasEPPAssets"
- "TB,N,V_hasiCloudAccount"
- "TB,N,V_highPriority"
- "TB,N,V_inExpunged"
- "TB,N,V_inTrash"
- "TB,N,V_isCurated"
- "TB,N,V_isCurrentUser"
- "TB,N,V_isCustomUserAsset"
- "TB,N,V_isExtendedCurated"
- "TB,N,V_isKeyAsset"
- "TB,N,V_isMovieCurated"
- "TB,N,V_isRepresentative"
- "TB,N,V_isUserCurated"
- "TB,N,V_keepOriginals"
- "TB,N,V_serverRecordIsCorrupted"
- "TB,N,V_shouldCheckFilesForUpload"
- "TB,N,V_shouldCheckOverQuotaChangesWithServer"
- "TB,N,V_shouldCompareAllProperties"
- "TB,N,V_shouldConsiderRequestingMoreTime"
- "TB,N,V_shouldHaveRequestedMoreTime"
- "TB,N,V_shouldRequestMoreTime"
- "TB,N,V_shouldTryToMingleImmediately"
- "TB,N,V_tentative"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisBlocked,V_blocked"
- "TB,R,N,GisCancelled,V_cancelled"
- "TB,R,N,GisCellular"
- "TB,R,N,GisCellularRestricted"
- "TB,R,N,GisCellularRestricted,V_cellularRestricted"
- "TB,R,N,GisConnected"
- "TB,R,N,GisConnectedToNetwork"
- "TB,R,N,GisConstrained"
- "TB,R,N,GisDetached"
- "TB,R,N,GisDisabled"
- "TB,R,N,GisEmpty"
- "TB,R,N,GisFIFOQueue,V_FIFOQueue"
- "TB,R,N,GisForStableHash"
- "TB,R,N,GisInAirplaneMode"
- "TB,R,N,GisInAirplaneMode,V_inAirplaneMode"
- "TB,R,N,GisInternal,V_internal"
- "TB,R,N,GisMarkedForDelete,V_markedForDelete"
- "TB,R,N,GisNoneState"
- "TB,R,N,GisOriginal,V_original"
- "TB,R,N,GisStale"
- "TB,R,N,GisValid"
- "TB,R,N,V_applyHasBeenSuccessful"
- "TB,R,N,V_batchCanLowerQuota"
- "TB,R,N,V_containerHasBeenWiped"
- "TB,R,N,V_diffHasBeenSuccessful"
- "TB,R,N,V_diffedBatchCanLowerQuota"
- "TB,R,N,V_expandHasBeenSuccessful"
- "TB,R,N,V_forDisplay"
- "TB,R,N,V_hasDroppedSomeResources"
- "TB,R,N,V_hasStagingScopes"
- "TB,R,N,V_highPriority"
- "TB,R,N,V_isAppLibrary"
- "TB,R,N,V_isAsset"
- "TB,R,N,V_isSystemLibrary"
- "TB,R,N,V_isTrashedOrDeletedAsset"
- "TB,R,N,V_libraryIsCorrupted"
- "TB,R,N,V_objectsAreTotallyDifferent"
- "TB,R,N,V_shouldBeCreatedDynamically"
- "TB,R,N,V_shouldBeTemporarilyNonDiscretionary"
- "TB,R,N,V_shouldBypassCaches"
- "TB,R,N,V_shouldCheckEPPCapability"
- "TB,R,N,V_shouldRescheduleASyncSession"
- "TB,R,N,V_shouldShowAlertToUser"
- "TB,R,N,V_syncHasBeenRequested"
- "TB,R,N,V_useFinal"
- "TB,R,V_allowsLocalConflictResolution"
- "TB,R,V_allowsLocalConflictResolutionWhenOverQuota"
- "TB,R,V_isComputeStateTaskUploadEnabled"
- "TB,R,V_shouldSyncScopeList"
- "TB,R,V_usesMMCSv2AsDefault"
- "TB,V_isJustInCaseSession"
- "TI,N,V_detectionType"
- "TI,N,V_faceState"
- "TI,N,V_feature"
- "TI,N,V_nameSource"
- "TI,N,V_type"
- "TI,N,V_version"
- "TQ,N"
- "TQ,N,S_setState:,V_state"
- "TQ,N,V_adjustmentRenderTypes"
- "TQ,N,V_adjustmentSourceType"
- "TQ,N,V_albumSortType"
- "TQ,N,V_albumType"
- "TQ,N,V_assetHDRType"
- "TQ,N,V_assetSubtype"
- "TQ,N,V_burstFlags"
- "TQ,N,V_changeType"
- "TQ,N,V_expungedState"
- "TQ,N,V_fileSize"
- "TQ,N,V_fullSizeJPEGSource"
- "TQ,N,V_maximumCountOfRecordsInBatches"
- "TQ,N,V_maximumRecordCountPerBatch"
- "TQ,N,V_originalChoice"
- "TQ,N,V_position"
- "TQ,N,V_pullTaskItem"
- "TQ,N,V_resourceType"
- "TQ,N,V_sourceResourceType"
- "TQ,N,V_state"
- "TQ,N,V_taskIdentifierForQueue"
- "TQ,N,V_totalCount"
- "TQ,N,V_videoComplementVisibilityState"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_budget"
- "TQ,R,N,V_changeType"
- "TQ,R,N,V_countOfSharingRecords"
- "TQ,R,N,V_countOfUnsharingRecords"
- "TQ,R,N,V_generation"
- "TQ,R,N,V_ignoredRecordCount"
- "TQ,R,N,V_intent"
- "TQ,R,N,V_libraryOptions"
- "TQ,R,N,V_majorVersion"
- "TQ,R,N,V_maxBatchSize"
- "TQ,R,N,V_maximumBatchSize"
- "TQ,R,N,V_maximumConcurrentTransportTasks"
- "TQ,R,N,V_maximumCount"
- "TQ,R,N,V_maximumPayloadRequestsBatchSize"
- "TQ,R,N,V_numberOfImagesToUpload"
- "TQ,R,N,V_numberOfOtherItemsToUpload"
- "TQ,R,N,V_numberOfVideosToUpload"
- "TQ,R,N,V_priority"
- "TQ,R,N,V_pushRepositoryPriority"
- "TQ,R,N,V_reason"
- "TQ,R,N,V_requiredStateAtEndOfSyncSession"
- "TQ,R,N,V_resourceSize"
- "TQ,R,N,V_sequenceNumber"
- "TQ,R,N,V_sizeOfOriginalResourcesToUpload"
- "TQ,R,N,V_sizeOfResourcesToUpload"
- "TQ,R,N,V_sourceResourceType"
- "TQ,R,N,V_stage"
- "TQ,R,N,V_status"
- "TQ,R,N,V_type"
- "TQ,R,V_currentState"
- "TS,N,V_notificationState"
- "TS,N,V_state"
- "TS,N,V_subtype"
- "TS,N,V_trashedReason"
- "TS,N,V_type"
- "T^?,N,V_propertyGetterIMP"
- "T^?,N,V_propertySetterIMP"
- "T^{objc_ivar=},N,V_ivar"
- "Tc,N,V_propertyType"
- "Td,N"
- "Td,N,V_bodyCenterX"
- "Td,N,V_bodyCenterY"
- "Td,N,V_bodyHeight"
- "Td,N,V_bodyWidth"
- "Td,N,V_centerX"
- "Td,N,V_centerY"
- "Td,N,V_score"
- "Td,N,V_size"
- "Td,R"
- "Td,R,N"
- "Td,R,N,V_minRefreshInterval"
- "Td,R,N,V_minUpdateInterval"
- "Tf,N,V_progress"
- "Tf,R,N"
- "Ti,N,V_reason"
- "Title"
- "Tq,N"
- "Tq,N,V_acceptanceStatus"
- "Tq,N,V_assetCount"
- "Tq,N,V_assetSortOrder"
- "Tq,N,V_busyState"
- "Tq,N,V_category"
- "Tq,N,V_cloudIndex"
- "Tq,N,V_customRenderedValue"
- "Tq,N,V_duration"
- "Tq,N,V_exitRetentionPolicy"
- "Tq,N,V_exitSource"
- "Tq,N,V_exitType"
- "Tq,N,V_faceCropType"
- "Tq,N,V_facesVersion"
- "Tq,N,V_graphVersion"
- "Tq,N,V_localIndex"
- "Tq,N,V_manualSortOrder"
- "Tq,N,V_notificationState"
- "Tq,N,V_numRequested"
- "Tq,N,V_orientation"
- "Tq,N,V_originalOrientation"
- "Tq,N,V_permission"
- "Tq,N,V_personType"
- "Tq,N,V_photosCount"
- "Tq,N,V_playCount"
- "Tq,N,V_position"
- "Tq,N,V_promisedAssetCount"
- "Tq,N,V_promisedPhotosCount"
- "Tq,N,V_promisedVideosCount"
- "Tq,N,V_publicPermission"
- "Tq,N,V_retryAfterMillis"
- "Tq,N,V_role"
- "Tq,N,V_scopeType"
- "Tq,N,V_shareCount"
- "Tq,N,V_sharedLibrarySharingState"
- "Tq,N,V_stableIndex"
- "Tq,N,V_stagedScopeFlags"
- "Tq,N,V_subcategory"
- "Tq,N,V_userActionOptions"
- "Tq,N,V_verifiedType"
- "Tq,N,V_version"
- "Tq,N,V_videoComplementDurationTimescale"
- "Tq,N,V_videoComplementDurationValue"
- "Tq,N,V_videoComplementImageDisplayTimescale"
- "Tq,N,V_videoComplementImageDisplayValue"
- "Tq,N,V_videosCount"
- "Tq,N,V_viewCount"
- "Tq,R"
- "Tq,R,N"
- "Tq,R,N,V_coalescingInterval"
- "Tq,R,N,V_currentFeatureVersion"
- "Tq,R,N,V_flags"
- "Tq,R,N,V_ruleGroup"
- "Tq,R,N,V_ruleGroups"
- "Tq,R,N,V_scopeType"
- "Tq,R,N,V_targetState"
- "Tq,R,N,V_updatedFlagsMask"
- "Tq,R,V_maximumComputeStatesToUploadPerBatch"
- "Trying to open %@ twice"
- "Ts,N,V_detectionType"
- "Ts,N,V_importedBy"
- "Ts,N,V_mode"
- "Ts,N,V_status"
- "Ts,N,V_type"
- "Ts,N,V_verifiedType"
- "Ts,N,V_videoFrameRate"
- "Ts,N,V_viewPresentation"
- "T{?={?=qiIq}{?=qiIq}},N,V_timeRange"
- "T{CGSize=dd},N,V_imageDimensions"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "URLForResource:withExtension:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unexpected implementation library identifier. Found '%@', expected '%@'"
- "Unknown scoped identifier in %@"
- "Upload for %{public}@ failed because the scope is over quota"
- "Upload for %{public}@ failed because the scope is over quota. Retrying with over-quota strategy"
- "Upload for %{public}@ failed because the scope is over quota. Will still continue synchronizing other scopes"
- "Upload for %{public}@ failed because the scope is over quota. Will stop forced sync"
- "Vv16@0:8"
- "Waiting for response to message: %@"
- "Waiting for sync manager to drop previous force sync %@ before launching pending %@"
- "Will boost operations when possible"
- "Will boost operations, including background, when possible"
- "Will check assets of %@ only against cloud cache when over-quota"
- "Will check assets of %@ with server when over-quota"
- "[%@ %@ %@ %@ %@]"
- "[%@ (%lu participants) %s]"
- "[%@ (public: %@) %s]"
- "[2@?]"
- "[<redacted> %@ %@ %@]"
- "[session #%lu%@%@]"
- "^?"
- "^?16@0:8"
- "^@"
- "^^v16@0:8"
- "^v"
- "^v24@0:8@16"
- "^v24@0:8^Q16"
- "^{_NSZone=}16@0:8"
- "^{network_usage_policy_client_s=}"
- "^{objc_ivar=}"
- "^{objc_ivar=}16@0:8"
- "_CPLEngineScopeCache"
- "_CPLEngineScopeDatesStack"
- "_CPLEngineStoreBatchedTransaction"
- "_CPLEngineSyncLastError"
- "_CPLForcedTaskHistory"
- "_CPLOptimisticIDMapping"
- "_CPLPruneRequestCounter"
- "_CPLResourcesMutableArray"
- "_CPLScheduledOverride"
- "_CPLScheduledOverrideDelegate"
- "_CPLSyncSessionPredictionType"
- "_CPLTimingStatistic"
- "_CPLTransientStatus"
- "_CPLWeakLibraryManager"
- "_FIFOQueue"
- "_URL"
- "__setError:"
- "_aClass"
- "_abstractClassToImplementation"
- "_abstractObject"
- "_acceptanceStatus"
- "_accessibilityDescription"
- "_accountFlagsData"
- "_acknowledgeContributorUpdatesAndContinue:"
- "_acknownledgeFixUpTasks:"
- "_acquireReschedulerTask"
- "_actionData"
- "_activateSharedScopeIfPresentWithError:"
- "_activated"
- "_activationDate"
- "_activeQueuesStatusAtEnqueingTime"
- "_activeTransferTaskCount"
- "_addAdditionalRecord:"
- "_addAllTransportScopesForScope:scopes:allowsTentativeTransportScope:useStagingScopeIfNecessary:error:"
- "_addChange:resultBatch:changesPerScopedIdentifier:changesPerClass:"
- "_addCleanupBlock:"
- "_addIdentityToUncommittedFiles:"
- "_addPartnerScope:scopes:"
- "_addPropertyAttributeMapToPropertyMapLocked:"
- "_addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
- "_addRelatedRecordWithScopedIdentifierToAdditionalRecords:provider:error:"
- "_addRuleToUserDefaults:"
- "_addSubscriberForCategory:usingPublishingHandler:"
- "_addTransportScopeForScope:scopes:allowsTentativeTransportScope:useStagingScopeIfNecessary:error:"
- "_addedDate"
- "_addedRecords"
- "_additionalDescription"
- "_additionalRecords"
- "_additionalScopeFilter"
- "_adjustedMediaMetaData"
- "_adjustedMediaMetaDataType"
- "_adjustmentCompoundVersion"
- "_adjustmentCreatorCode"
- "_adjustmentData"
- "_adjustmentFingerprint"
- "_adjustmentRenderTypes"
- "_adjustmentSourceType"
- "_adjustmentTimestamp"
- "_adjustmentType"
- "_adjustments"
- "_advanceToNextStateLockedMinimalState:"
- "_albumSortAscending"
- "_albumSortType"
- "_albumType"
- "_allChangesMatchingChangeType:enumerator:"
- "_allComponentsIncludingPlatformObjects:respondingToSelector:"
- "_allHighPriorityQueues"
- "_allLowPriorityQueues"
- "_allPartnerScopeIdentifiersNeedingToPullChanges"
- "_allQueues"
- "_allScopedIdentifierInCollection:withScopeIdentifier:"
- "_allowBackgroundOperationsBoost"
- "_allowOperationsBoost"
- "_allowed"
- "_allowsJustInCaseSessions"
- "_allowsLocalConflictResolution"
- "_allowsLocalConflictResolutionWhenOverQuota"
- "_allowsMinglingChangeWithScopedIdentifier"
- "_alreadyProcessedChanges"
- "_alreadySeenMasterScopedIdentifiers"
- "_anchorToVersion"
- "_appendBatchToStorage:alreadyMingled:countOfAssetChanges:error:"
- "_appendMessage:"
- "_appendMessages:"
- "_applyAndDiscardPendingUpdate:error:"
- "_applyHasBeenSuccessful"
- "_applyMingledBatch:scope:forStore:onPutBatchInPullQueue:error:"
- "_applyPendingUpdate:error:"
- "_applyingChangeSessionUpdate"
- "_archive"
- "_archiveCursor"
- "_arrayDescriptionForFlags:remainingFlags:"
- "_assetCount"
- "_assetCounts"
- "_assetCountsToUpdate"
- "_assetDate"
- "_assetFlag"
- "_assetHDRType"
- "_assetIdentifier"
- "_assetList"
- "_assetListPredicate"
- "_assetMovieData"
- "_assetSortOrder"
- "_assetSubtype"
- "_assets"
- "_assetsWithResourcesToUpload"
- "_attachedDiffTracker"
- "_attachedObjects"
- "_attemptScheduleRecoveryOverride:withReason:"
- "_automaticallyFixBadPrivateAsset"
- "_available"
- "_backOff"
- "_backgroundDownloadTaskIdentifier"
- "_backgroundTask"
- "_backoffRetryingConnectionDate"
- "_badError"
- "_baseRecordView"
- "_baseScopeFilter"
- "_baseStorageView"
- "_baseTypesBits"
- "_baseURL"
- "_batch"
- "_batchCanLowerQuota"
- "_batchCount"
- "_batchEnumerator"
- "_batchStorage"
- "_batchToCommit"
- "_batchedLocalComputeStatesNeedingPayload"
- "_batchedTransactionDequeueIsScheduled"
- "_batchedTransactions"
- "_batchedTransactionsQueue"
- "_beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
- "_beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
- "_bestCancellableHighPriorityQueues"
- "_bestCancellableLowPriorityQueues"
- "_blacklistedFeature"
- "_block"
- "_blockWaiters"
- "_blocked"
- "_blockedElements"
- "_blockedReasons"
- "_blocker"
- "_blocking"
- "_blockingElements"
- "_blockingLock"
- "_blocksToDispatchWhenLibraryAttaches"
- "_bodyCenterX"
- "_bodyCenterY"
- "_bodyHeight"
- "_bodyWidth"
- "_boostPriority"
- "_boundaryKey"
- "_brokenScopes"
- "_brokenScopesLock"
- "_budget"
- "_bumpIgnoredDatesOfRecords:hasResharedSomeRecords:"
- "_bumpIgnoredDatesOfRejectedRecords:"
- "_bumpPushRepositoryPriority:reason:"
- "_burstFlags"
- "_burstIdentifier"
- "_busyState"
- "_bypassForceSyncLimitations"
- "_byteCountFormatter"
- "_cacheKeyForReferenceResource:adjustments:includePosterFrame:"
- "_cacheMappingURL"
- "_cacheScope:"
- "_cacheURL"
- "_cachedLastQuarantineCountReportDate"
- "_cachedRealResourceSizeInStorage"
- "_cachedResourcesForReferenceResource:adjustment:includePosterFrame:"
- "_calculateEstimatedBatchSize"
- "_callDescription"
- "_canGenerateDerivative"
- "_canHaveActivatedScope:libraryOptions:error:"
- "_canRead"
- "_canUseOverQuotaRule"
- "_canWrite"
- "_cancelAllTasks"
- "_cancelAllTasksForSetup"
- "_cancelBlockWhenLibraryAttaches:"
- "_cancelCount"
- "_cancelHandler"
- "_cancelled"
- "_cancelledByEngine"
- "_cancellerBlocks"
- "_capacity"
- "_caption"
- "_category"
- "_cellularRestricted"
- "_centerX"
- "_centerY"
- "_change"
- "_changeCanConflict:"
- "_changeClass"
- "_changePipeDidRemoveChanges"
- "_changeStorage"
- "_changeType"
- "_changedKeys"
- "_changesPerScopedIdentifier"
- "_changesWithMissingIDMapping"
- "_changesWithResourceChanges"
- "_checkDestinationAndProcessCleanup"
- "_checkDestinationTask"
- "_checkExtraRecords"
- "_checkExtraRecordsWithScopedIdentifiers:"
- "_checkForRecordExistence"
- "_checkForegroundAtLaunchForForcedTask"
- "_checkGeneratedResources:error:"
- "_checkItems"
- "_checkPrioritiesWithFetchCache:"
- "_checkRecordsTask"
- "_checkResource:name:error:"
- "_checkServerFeatureVersionWithCompletionHandler:"
- "_checkShouldHandleBatchInTransaction:"
- "_checkSuperWasCalled"
- "_checkSyncManagerPriorityBoost"
- "_checkTransportScopeForScopeIdentifier:hasConcreteScope:error:"
- "_checked"
- "_classDescription"
- "_cleanTempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:"
- "_cleanupBlocks"
- "_cleanupSharingFlags"
- "_cleanupStagedScopeInTransaction:store:"
- "_cleanupTask"
- "_cleanupTasks"
- "_clearAndCreateTempFolderIfNecessaryWithError:"
- "_clearScopeCache"
- "_clearSomeScopeMightHaveToBePulledByClient"
- "_clearUploadBatch"
- "_clientBatch"
- "_clientBundleID"
- "_clientCacheIdentifier"
- "_clientDidAcknowledgeBatchBlock"
- "_clientLibraryBaseURL"
- "_clientWillAcknowledgeBatchBlock"
- "_closeAndDeactivate:completionHandler:"
- "_closeDeactivating:completionHandler:"
- "_closeNextComponent:deactivate:lastError:completionHandler:"
- "_closed"
- "_closingCompletionHandler"
- "_closingQueue"
- "_cloudBatch"
- "_cloudCache"
- "_cloudCacheInStore:"
- "_cloudComputeStatesNeedingPayload"
- "_cloudComputeStatesToUpload"
- "_cloudIndex"
- "_cloudLibraryResourceStorageURL"
- "_cloudLibraryStateStorageURL"
- "_cloudRecord"
- "_cloudResource"
- "_cloudResourceForLocalResource:cloudRecord:target:shouldNotTrustCaches:allowUnsafeClientCache:allowBypassingAllCaches:transportScopeMapping:error:"
- "_cloudScopedIdentifiersToUploadResourceTaskErrors"
- "_coalescingInterval"
- "_codec"
- "_commentDate"
- "_commentText"
- "_commitTasks"
- "_commitWriteTransaction:commitError:"
- "_compactStorageIncludeOriginals:desiredFreeSpace:error:"
- "_completeBackgroundDownloadForResource:error:withTransaction:"
- "_completed"
- "_completionHandler"
- "_completionHandlers"
- "_components"
- "_computeNextStep"
- "_computeStateAdjustmentFingerprint"
- "_computeStateLastUpdatedDate"
- "_computeStateVersion"
- "_computeStatesAccumulator"
- "_computeSummariesIfNecessary"
- "_concreteScopeMapping"
- "_configuration"
- "_configurationDictionary"
- "_configurationDictionaryUniquifier"
- "_configurationDidChange"
- "_configurationFetcher"
- "_configurationFileURL"
- "_configurationURL"
- "_connection"
- "_contactDescriptor"
- "_containerHasBeenWiped"
- "_containerIdentifier"
- "_containerRelations"
- "_context"
- "_contributorUserIdentifier"
- "_contributorsUpdatesInTransaction:"
- "_copyDerivatives:count:ifMatchingResourceType:fromRecord:inResourcePerType:"
- "_copyResourceChangeFromChange:toChange:fingerprintScheme:error:"
- "_correctPrivateScopedIdentifierForSharedScopedIdentifier:currentPrivateScopedIdentifier:"
- "_countOfComputeStatesPutAside"
- "_countOfDroppedComputeStates"
- "_countOfFinishedDownloadTasksSinceLastReport"
- "_countOfProvidedComputeStates"
- "_countOfPulledAssets"
- "_countOfPushedChanges"
- "_countOfRequestedComputeStates"
- "_countOfSharingRecords"
- "_countOfUnsharingRecords"
- "_countPerFlags"
- "_coveredScopes"
- "_cplCopyProperties:fromOtherObject:withCopyBlock:"
- "_cplDecodeBoolForKey:"
- "_cplDecodeCharForKey:"
- "_cplPropertyAttributeMap"
- "_cplReinflatedUserInfoForXPCDidChange:"
- "_cplSafeUserInfoForXPCDidChange:"
- "_crashMarkerURL"
- "_createCacheFolderIfNecessary"
- "_createScopeFromScopeChange:error:"
- "_createSignatureGenerator"
- "_createTestMemoryWithAssets:"
- "_createTestSocialGroupWithPersons:"
- "_createTestSuggestionWithKeyAssets:representativeAssets:"
- "_creationDate"
- "_creatorCode"
- "_cropRectString"
- "_curatedAssetIdentifiers"
- "_currentBatchOfComputeStatesNeedingPayload"
- "_currentChangeSessionToken"
- "_currentCleanupScopeIndex"
- "_currentClosingComponentName"
- "_currentEnumerator"
- "_currentEnumeratorMutationsPtr"
- "_currentFeatureVersion"
- "_currentForcedTask"
- "_currentGeneration"
- "_currentGeneratorIndex"
- "_currentIntentIndex"
- "_currentPrediction"
- "_currentQueryClass"
- "_currentRequestGeneration"
- "_currentScope"
- "_currentScopeChange"
- "_currentSession"
- "_currentState"
- "_currentStep"
- "_currentStrategy"
- "_currentSubtask"
- "_currentSubtaskLock"
- "_currentSyncState"
- "_currentTask"
- "_currentTaskKey"
- "_currentTaskLock"
- "_currentTaskQueue"
- "_currentThread"
- "_currentTransaction"
- "_customRenderedValue"
- "_customTitle"
- "_customUserAssetList"
- "_cutoffDate"
- "_date"
- "_dateDeleted"
- "_deactivated"
- "_dedupeConfigurationDictionary"
- "_defaultHEVC"
- "_deferDate"
- "_deferredCancel"
- "_delayedFirstSyncBecauseOfRapidLaunch"
- "_delayedGeneratedDerivativesCalls"
- "_delegate"
- "_delegateQueue"
- "_delegationProtocol"
- "_delegationSelector"
- "_deleteDate"
- "_deleteGeneratedResourcesAfterError:"
- "_deleteImmediately"
- "_deleteInitialSyncMarkerWithError:"
- "_deleteStagingScopeIfNecessary"
- "_deleteTask"
- "_deleteTempFolderForPayloads"
- "_deletedByUserIdentifier"
- "_deletedRecordScopedIdentifiers"
- "_deletedScopeCount"
- "_deletedScopeIdentifiers"
- "_dequeueFromPendingRecordChecksIfNecessary:error:"
- "_dequeueObservers"
- "_derivativeGeneratorClass"
- "_derivativeTypes"
- "_derivativesCache"
- "_derivativesFilter"
- "_derivativesSizeReportTimer"
- "_derivativesSizeToReport"
- "_descriptionForChangeType:isSparseFullChange:onlyUploadNewResources:"
- "_descriptionForSetupTasks"
- "_descriptionForStoredResponse:recordType:"
- "_descriptionFromTasksByType:"
- "_descriptionRedacted:"
- "_descriptionSuffix"
- "_destinationScope"
- "_destinationScopeChange"
- "_destinationTransportScope"
- "_detachedActivity"
- "_detectionType"
- "_didCacheRealResourceSizeInStorage"
- "_didExtractOneBatch"
- "_didFinish"
- "_didFinishSetupTaskWithError:shouldStop:"
- "_didFinishTaskWithKey:error:cancelled:"
- "_didLogShouldStashMasterRecords"
- "_didNotifySchedulerPullQueueIsFullOnce"
- "_didOpenComponent:error:"
- "_didStart"
- "_didStartHandler"
- "_didStartTaskWithKey:recordCount:"
- "_didUploadSomeComputeStates"
- "_didWriteFirstSyncMarker"
- "_diffBatch"
- "_diffHasBeenSuccessful"
- "_diffTracker"
- "_diffedBatch"
- "_diffedBatchCanLowerQuota"
- "_differingProperties"
- "_dirty"
- "_disableConfigurationFetching"
- "_disableFastRelaunchProtection"
- "_disableFeedback"
- "_disableRetryAfterLocked"
- "_disableSchedulerForForcedTaskIfNecessary"
- "_disableSynchronizationBecauseContainerHasBeenWipedLocked"
- "_disableSynchronizationWithReasonLocked:"
- "_disabled"
- "_disabledDate"
- "_disabledFeatures"
- "_disabledSchedulerForForcedTask"
- "_disablingMinglingCount"
- "_disablingReasons"
- "_discardCurrentSubtask"
- "_discardExtractedBatchAndGetNextBatch"
- "_discardGenerateDerivativesProgress"
- "_discardPendingForcedTasksWithError:"
- "_discardUnacknowledgedBatchOnTransactionFail"
- "_discardUploadedExtractedBatch:error:"
- "_discarded"
- "_dispatchAfter:block:"
- "_dispatchBlockWhenOpen:"
- "_dispatchFailedDownloadTaskForResource:options:proposedTaskIdentifier:withError:withCompletionHandler:"
- "_dispatchFailedForceSyncTaskForScopeIdentifiers:withError:withCompletionHandler:"
- "_dispatchFailedInMemoryDownloadTaskForResource:withError:withCompletionHandler:"
- "_dispatchNextSyncTask"
- "_dispatchSyncTask:"
- "_displayName"
- "_displayableArrayForArray:"
- "_displayableObjectForObject:"
- "_doOneIteration"
- "_doProtected:"
- "_doesScopeContributeToGlobalStatus:"
- "_dontDelayChangeSessionUpdate"
- "_downloadLock"
- "_downloadQueue"
- "_downloadTask"
- "_downloadTask:didFinishWithErrorLocked:"
- "_downloadTasks"
- "_dropAllComputeStates"
- "_dropChangeWithReason:"
- "_dropConnectionCompletly"
- "_dropConnectionCompletlyLocked"
- "_dropCurrentTask"
- "_dropDerivativeRulesFromUserDefaults"
- "_dropLocalComputeStates:"
- "_dropReason"
- "_dropSharingScopeIdentifier:error:"
- "_dropTransactionClientCacheView"
- "_dropVoucherForTaskWithIdentifier:"
- "_duration"
- "_earliestDate"
- "_effectiveClientBundleIdentifier"
- "_email"
- "_enableSynchronizationWithReasonLocked:"
- "_endDate"
- "_endPoint"
- "_endTaskError"
- "_endTime"
- "_engineLibrary"
- "_engineScope"
- "_engineStore"
- "_enqueueTasksLocked"
- "_enumerateDropDerivativeRules:ofType:withBlock:"
- "_enumerator"
- "_error"
- "_errorCount"
- "_errorDescription"
- "_errors"
- "_estimatedBatchSize"
- "_excludeScopeFromMingling"
- "_excludeScopes"
- "_excludedScopeIdentifiers"
- "_excludedScopes"
- "_exitRetentionPolicy"
- "_exitSource"
- "_exitType"
- "_exitingUserIdentifiers"
- "_expandHasBeenSuccessful"
- "_expandedBatch"
- "_expectedDate"
- "_expirationDateStorageKey"
- "_expirationDateStorageKeyForBudget:"
- "_expiryDate"
- "_expungeDate"
- "_expungeableResourceStates"
- "_expungedDate"
- "_expungedState"
- "_extendedDescription"
- "_extraProperties"
- "_extraTypeBits"
- "_extractAndMingleAssetsIfPossibleFromBatch:inTransaction:"
- "_extractAndMinglePersonsIfPossibleFromBatch:inTransaction:"
- "_extractAndUploadOneBatch"
- "_extractionClass"
- "_extractionStrategy"
- "_faceCropType"
- "_faceInstances"
- "_faceState"
- "_facesAdjustmentsFingerprint"
- "_facesData"
- "_facesVersion"
- "_failedDownloadedResourcesCount"
- "_failedStatsPerResourceType"
- "_fakeSession"
- "_favorite"
- "_feature"
- "_featureCompatibleVersion"
- "_featureVersionHistory"
- "_featuresData"
- "_feedback"
- "_feedbackMessagesURL"
- "_feedbackType"
- "_fetchBoundaryKeyIfNecessaryWithSource:completionHandler:"
- "_fetchBoundaryKeyIfNecessaryWithSourceLocked:completionHandler:"
- "_fetchChangesTask"
- "_fetchInitialSyncAnchor"
- "_fetchInitialSyncAnchorTask"
- "_fetchRecordsTask"
- "_fetchRewindSyncAnchorsInScopes:startSyncAnchor:error:"
- "_fetchRules"
- "_fetchTransportScope"
- "_fetchedTransportScope"
- "_fileSize"
- "_fileStorage"
- "_fileStorageIdentifier"
- "_fileURL"
- "_fileUTI"
- "_filename"
- "_filesToCommit"
- "_filesToDelete"
- "_fillStatus:"
- "_fillStatus:forComponents:completionHandler:"
- "_fillStatus:withClientCacheRecordView:cloudCacheRecord:isConfirmed:isStaged:isInIDMapping:"
- "_fillStatusArray:forComponents:completionHandler:"
- "_filter"
- "_filteredBatchByStashingRecordsIfNecessary:error:"
- "_finalData"
- "_finalError"
- "_finalFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:"
- "_finalListOfPartnerScopesNeedingToPullChanges"
- "_finalResource"
- "_fingerPrint"
- "_fingerprintContext"
- "_fingerprintScheme"
- "_finishMingling"
- "_finishReportingDerivativesIsNecessary"
- "_finishTaskLocked"
- "_finishTransaction"
- "_finishWithError:"
- "_finished"
- "_firstTryOpeningLibrary"
- "_fixGlobalStatus"
- "_fixUpPrivateRecordsPointingToRemappedSharedRecords:"
- "_fixUpTask"
- "_fixupIdentity:fileURL:data:error:"
- "_fixupRemappedRecordsAndReturnBestCloudScopedIdentifierFromRemappedScopedIdentifiers:fallback:"
- "_flags"
- "_folderNameForReferenceResource:adjustment:includePosterFrame:"
- "_forAdditionalRecordRule:check:error:"
- "_forCPL"
- "_forDisplay"
- "_forManagement"
- "_forRule:check:error:"
- "_forWrite"
- "_forceClientToPullScopeIfNecessary:error:"
- "_forceCloseWithCompletionHandler:"
- "_forceRefreshWatchingNode"
- "_forceSync"
- "_forceSyncDelegate"
- "_forceSyncManagerPriorityBoost"
- "_forceSyncTasks"
- "_forcedSetupTask"
- "_forcedTaskDidFinishWithError:"
- "_forcedTaskHistory"
- "_foreground"
- "_foregroundCalls"
- "_foregroundCallsHaveBeenQuiet"
- "_formatter"
- "_foundRecords"
- "_full"
- "_fullName"
- "_fullRecords"
- "_fullSizeJPEGSource"
- "_functionName"
- "_generateDerivativesCancellationHandler"
- "_generateDerivativesChange"
- "_generateDerivativesDeferredHandler"
- "_generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:"
- "_generateDerivativesForNextRecord:usingDerivativesCache:fetchCache:fingerprintContext:"
- "_generateDerivativesLastFractionCompleted"
- "_generateDerivativesProgress"
- "_generateDerivativesTotalSize"
- "_generateNeededDerivativesWithFetchCache:fingerprintContext:"
- "_generatingDerivativesForChange:fractionCompleted:chunkLength:"
- "_generation"
- "_generatorArray"
- "_getCellularPolicyWithClient:"
- "_getLibraryInfo"
- "_getMappedIdentifiersForIdentifiers:inAreLocalIdentifiers:completionHandler:"
- "_getMappedScopedIdentifiersForScopedIdentifiers:inAreLocalIdentifiers:completionHandler:"
- "_getNextBatchAndUpload"
- "_getResourceTypesToDownload:"
- "_getTargetDictionaryForChangeType:"
- "_graphData"
- "_graphVersion"
- "_groupConstructor"
- "_handleChangedOrNewScopes:deletedScopeIdentifiers:newScopeListSyncAnchor:"
- "_handleException:"
- "_handleFinalScopeListSyncAnchor:error:"
- "_handleNewBatchFromChanges:newSyncAnchor:inTransaction:"
- "_handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:"
- "_handleNewBatchFromQuery:newCursor:inTransaction:"
- "_handleNewBatchFromQuery:queryClass:newCursor:"
- "_handleResetAnchorWithError:completionHandler:"
- "_handleResetClientCacheWithError:completionHandler:"
- "_handleResetCloudCacheWithError:completionHandler:"
- "_handleResetGlobalAnchorWithError:completionHandler:"
- "_handledDisabledFeaturesForScopeIfNecessary:type:error:"
- "_handler"
- "_has"
- "_hasCachedResultOfServerCheck"
- "_hasCachedShouldCheckResourcesAhead"
- "_hasCachedSummaries"
- "_hasCachedTotalAssetCountForScope"
- "_hasChanges"
- "_hasDroppedSomeResources"
- "_hasEPPAssets"
- "_hasFetchedBoundaryKey"
- "_hasFetchedInitialSyncAnchor"
- "_hasFinishedTask"
- "_hasNotifiedClientOfChangesToPull"
- "_hasOverridenBudgets"
- "_hasPermanentDataOverride"
- "_hasProcessedStagedScopes"
- "_hasPushedSomeChanges"
- "_hasResetQueue"
- "_hasScheduledPullFromTransport"
- "_hasSeenSomeChanges"
- "_hasSetupBatteryMonitor"
- "_hasStagingScopes"
- "_hasUpdatedDisabledFeatures"
- "_hasUploadedOneBatch"
- "_hasiCloudAccount"
- "_hidden"
- "_highPriority"
- "_highPriorityQueuePerResourceTypeAndTransferIntent"
- "_holdTestAssertions"
- "_idMapping"
- "_identifier"
- "_identitiesToCommit"
- "_identitiesToDelete"
- "_identity"
- "_identityForIdentifier:"
- "_ignoreNewBatches"
- "_ignoreNewChanges"
- "_ignoredDate"
- "_ignoredRecord"
- "_ignoredRecordCount"
- "_ignoredRecords"
- "_imageDimensions"
- "_importDate"
- "_importGroupIdentifier"
- "_importedBy"
- "_importedByBundleIdentifier"
- "_importedByDisplayName"
- "_inAirplaneMode"
- "_inExpunged"
- "_inMemoryDownloadTasks"
- "_inMemoryRequest"
- "_inTrash"
- "_includeScopeInMingling"
- "_includedScopeIdentifiers"
- "_incomingBatch"
- "_incomingBatchRecordPerScopedIdentifiers"
- "_incomingDownloadFolderCreationDate"
- "_incomingDownloadFolderURL"
- "_indexOfCurrentClassForInitialQueriesForScope:"
- "_inflightTransferTasksCount"
- "_info"
- "_initLock"
- "_initWithRecords:"
- "_initialScopeChange"
- "_initialSyncAnchor"
- "_initializeSmallKeyMapping"
- "_installGenerateDerivativesCancellationHandler:"
- "_intent"
- "_intentsToDownload"
- "_intermediateStatuses"
- "_internal"
- "_intervalForRetry"
- "_invalidAttachedObjects"
- "_invalidCloudCacheErrorWithInvalidRecord:method:"
- "_invalidFingerprintForSelector:withError:"
- "_invalidScopeIdentifiers"
- "_invalidTransportScopes"
- "_invokeOutstandingInvocationsWithTaskIdentifier:"
- "_invokeSyncOutstandingInvocationsWithTaskIdentifier:"
- "_isAppLibrary"
- "_isAsset"
- "_isComputeStateTaskUploadEnabled"
- "_isCurated"
- "_isCurrentUser"
- "_isCustomUserAsset"
- "_isDoingInitialMingling"
- "_isErrorCountingForARetry:"
- "_isExtendedCurated"
- "_isFaceStateBitSet:"
- "_isGeneratingDerivatives"
- "_isJustInCaseSession"
- "_isKeyAsset"
- "_isMMCSv2"
- "_isMovieCurated"
- "_isOverridingForeground"
- "_isPrimarySharedLibrary"
- "_isRepresentative"
- "_isRestrictedPath:policies:"
- "_isSparseFullChange"
- "_isSystemLibrary"
- "_isTrashedOrDeletedAsset"
- "_isUnsupportedFormatError:"
- "_isUpdatingDisabledFeatures"
- "_isUserCurated"
- "_isUsingOverQuotaStrategy"
- "_isValidDropDerivativeRecipeWithUTI:sourceType:derivativeTypes:changeType:"
- "_isValidSharingScope:forScopeIdentifier:"
- "_isValidSharingScopeIdentifier:scopeType:forScopeIdentifier:"
- "_itemIdentifier"
- "_itemScopedIdentifier"
- "_itemType"
- "_items"
- "_itemsPtr"
- "_itemsToReinject"
- "_ivar"
- "_justInCaseSessionIsPossible"
- "_keepIgnoredRecord:shadowingRecord:inScope:error:"
- "_keepOriginals"
- "_keepSessionInformation:"
- "_key"
- "_keyAsset"
- "_keyAssetIdentifier"
- "_keysAndValues"
- "_keywords"
- "_killed"
- "_kindOfWorkReporters"
- "_knownRecords"
- "_lastAccessDate"
- "_lastApproximativeUploadRate"
- "_lastAttemptDate"
- "_lastChangeDateForPhaseDescription"
- "_lastComputeStateDownloadRequestDate"
- "_lastComputeStateDownloadRequestDateLock"
- "_lastDate"
- "_lastError"
- "_lastErrors"
- "_lastInvalidRecordScopedIdentifiers"
- "_lastInvalidRecordsDate"
- "_lastReportedProgress"
- "_lastRequestDate"
- "_lastRequestGeneration"
- "_lastScopeIdentifiersExcludedFromPushToTransport"
- "_lastScopeIdentifiersExludedFromMingling"
- "_lastSessionInformation"
- "_lastSessionWasDeferredBecauseOfTimeButDidNotRequestMoreTime"
- "_lastSharedDate"
- "_lastShownAlertDate"
- "_lastStrategyName"
- "_lastSuccessfulSyncSessionDate"
- "_lastSyncSessionDateCausedByForeground"
- "_lastSyncSessionDescription"
- "_lastSyncSessionEndDate"
- "_lastSyncSessionStartDate"
- "_lastTransferTaskBurstDate"
- "_lastTransferTasksBurstCount"
- "_lastUpdateDate"
- "_lastUpdatedDate"
- "_lastUploadRateUpdateDate"
- "_lastViewedDate"
- "_launch"
- "_launchFetchChangesFromSyncAnchor:"
- "_launchForceSetupTask"
- "_launchForcedTaskIfNecessary"
- "_launchHandler"
- "_launchNecessaryDownloadTasksWithTransaction:"
- "_launchNextQueryTask"
- "_launchPullTasksAndDisableQueries:"
- "_launchQueryForClass:cursor:"
- "_launchSetupTask"
- "_launchSubTask:subIdentifier:"
- "_launchTaskForNextScope"
- "_libraryIdentifier"
- "_libraryInfo"
- "_libraryIsCorrupted"
- "_libraryManager"
- "_libraryObject"
- "_libraryOptions"
- "_libraryState"
- "_libraryVersion"
- "_load"
- "_loadIfNecessary"
- "_loadResetEvents"
- "_localComputeStatesToUpload"
- "_localIndex"
- "_localResources"
- "_localScopedIdentifier"
- "_location"
- "_lock"
- "_logDomain"
- "_logKilled"
- "_loggedForThisStep"
- "_lookForStagingScopeTask"
- "_lookForStagingScopeWithIdentifier:transportScope:"
- "_lowPriorityQueuePerResourceTypeAndTransferIntent"
- "_mainScopeIdentifier"
- "_majorVersion"
- "_manualSortOrder"
- "_mapBlock"
- "_mappedUnscopedIdentifiersFromScopedIdentifiers:"
- "_mapping"
- "_markConnectionAsInvalid"
- "_markScopeAsDeletedAndSucceedTaskWithFlags:"
- "_markScopeAsFeatureDisabledWithFlags:"
- "_markScopeHasBadTransportScopeWithError:"
- "_markUploadedTasksDidFinishWithError:transaction:error:"
- "_markedForDelete"
- "_markerURLForTrackAllStoresAndDeletes"
- "_masterIdentifier"
- "_maxBatchSize"
- "_maximumBatchSize"
- "_maximumComputeStatesToUploadPerBatch"
- "_maximumConcurrentTransportTasks"
- "_maximumCount"
- "_maximumCountOfRecordsInBatches"
- "_maximumPayloadRequestsBatchSize"
- "_maximumRecordCountPerBatch"
- "_mediaGroupIdentifier"
- "_mediaMetaData"
- "_mediaMetaDataType"
- "_memoryIdentifier"
- "_memorys"
- "_mergeTargetPersonIdentifier"
- "_mergedRecordWithPrivateChange:sharedScopedIdentifier:"
- "_mergedRecordWithSharedChange:target:"
- "_merger"
- "_mergerWithConflictsForStore:conflictingScopeIdentifiers:"
- "_mergerWithNoConflictsForStore:"
- "_messages"
- "_messagesSending"
- "_messagesToSend"
- "_metrics"
- "_metricsFileURL"
- "_metricsIdentifier"
- "_metricsObserver"
- "_minRefreshInterval"
- "_minUpdateInterval"
- "_mingleOtherChanges"
- "_mingleRemappings"
- "_mingleSharedRemappings"
- "_minglingCount"
- "_minglingHasBeenReset"
- "_minimalDateForFirstSync"
- "_minimumBatteryLevelForAutoOverrideEnergyBudget"
- "_mmcsv1FingerprintScheme"
- "_mmcsv2FingerprintScheme"
- "_mode"
- "_modifiedScopeCount"
- "_modifyingBudgetOverride"
- "_momentShare"
- "_monitor"
- "_mostRecentScopeStatusCountsDidChangeNotificationDate"
- "_movieData"
- "_mustConsiderOtherPriorities"
- "_mutablePushContexts"
- "_mutableTasksByType"
- "_mutableUntrustableScopedIndentifiers"
- "_name"
- "_nameComponents"
- "_nameSource"
- "_needsToGenerateImageDerivatives"
- "_needsToGenerateVideoComplementDerivatives"
- "_needsToNotifySchedulerPullQueueIsFull"
- "_needsToUpdateLastSyncDate"
- "_networkPath"
- "_networkPolicyClient"
- "_networkState"
- "_newBudgetsToOverride"
- "_newBudgetsToStopOverriding"
- "_newRejectedCount"
- "_newRejectedRecords"
- "_newScopeCount"
- "_nextSession"
- "_nextSessionIsJustInCase"
- "_nextSessionShouldRequestMoreTime"
- "_nodeInode"
- "_nodeSource"
- "_nonAssetsWithResourcesToUpload"
- "_noteBatchWasAddedInPullQueue:fromBatch:transaction:"
- "_noteGeneratedResources:haveBeenGeneratedForReferenceResource:adjustment:includePosterFrame:"
- "_notePartnerScopesNeedingToPullChanges:scopes:inTransaction:"
- "_noteRelatedRecordShouldBeShared"
- "_noteServerIsUnavailableWithErrorLocked:reason:"
- "_noteSignificantEvent"
- "_noteSuccessfulUpdateInTransaction:"
- "_noteSyncSession:failedDuringPhase:withError:"
- "_noteSyncSessionNeededFromState:minimumDelay:"
- "_noteSyncSessionNeededFromState:proposedScheduleDate:"
- "_noteSyncSessionNeededFromStateDontRewindImmediately:"
- "_notificationState"
- "_notifyAttachedObjectsThatPushRepositoryFlagsCountsHaveChanged"
- "_notifyQueue"
- "_notifyQueueRemovedChanges"
- "_notifySchedulerPullQueueIsFull"
- "_notifySchedulerPullQueueIsFullInTransaction:"
- "_notifySchedulerPullQueueIsFullNowIfNecessary"
- "_notifyScopeObserversForScope:flagsUpdate:"
- "_notifyToken"
- "_now"
- "_numRequested"
- "_numberOfImagesToUpload"
- "_numberOfOtherItemsToUpload"
- "_numberOfVideosToUpload"
- "_objectIsClass"
- "_objectsAreTotallyDifferent"
- "_observers"
- "_openNextComponent:completionHandler:"
- "_opened"
- "_openingError"
- "_openingStatus"
- "_optimisticIDMapping"
- "_options"
- "_orientation"
- "_original"
- "_originalBatch"
- "_originalChoice"
- "_originalOrientation"
- "_originatingFingerprint"
- "_originatingScopeIdentifier"
- "_otherAdjustmentsFingerprint"
- "_otherRewindSyncAnchors"
- "_otherScopedIdentifier"
- "_otherScopedIdentifierForCloudScopedIdentifier:sharedScoped:"
- "_outgoingResources"
- "_outgoingUploadFolderURL"
- "_outstandingInvocations"
- "_outstandingInvocationsCount"
- "_overrideBudgetsIfNeeded"
- "_overrideDataSystemBudgetPermanently"
- "_overrideReasonKey"
- "_owner"
- "_ownerIdentifier"
- "_parentIdentifier"
- "_parentMetricsIdentifier"
- "_parentSource"
- "_participantID"
- "_participants"
- "_partnerScopes"
- "_pathToFirstSynchronizationMarker"
- "_pendingBlocksAfterOpening"
- "_pendingChangeSessionCompletionHandler"
- "_pendingChangeSessionToken"
- "_pendingDeletedTransientStatuses"
- "_pendingForcedTasks"
- "_pendingRecordChecks"
- "_pendingRequiredFirstState"
- "_pendingTracker"
- "_pendingTransientStatuses"
- "_pendingUpdateInterval"
- "_pendingUpdateQueue"
- "_pendingUpdateTimer"
- "_people"
- "_perTransactionRemappedScopedIdentifiers"
- "_performAdditionalChecksWithNewScopeType:updatedScopeChange:updatedFlags:oldTransportScope:updatedTransportScope:completionHandler:"
- "_performBarrierTransaction:withBlock:"
- "_performBlockWhenLibraryAttaches:"
- "_performBlockWithLibrary:enumerateAttachedObjects:"
- "_performPendingBlockForWhenLibraryAttaches"
- "_performTransaction:withBlock:"
- "_performWriteTransactionByPassBlocker:WithBlock:completionHandler:"
- "_permanentDataOverrideHasChanged"
- "_permission"
- "_persistedScopedIdentifiers"
- "_personIdentifier"
- "_personType"
- "_persons"
- "_personsData"
- "_petFaceInstances"
- "_phaseDescription"
- "_phaseDescriptionLock"
- "_phoneNumber"
- "_photosCount"
- "_pingRequestToPushAllChanges"
- "_placeAnnotation"
- "_placeLevel"
- "_placeName"
- "_platformObject"
- "_playCount"
- "_popContext"
- "_popNextBatchAndContinue"
- "_position"
- "_possibleStagedScopes"
- "_predictions"
- "_predictor"
- "_preemptingCount"
- "_prepareFirstSession"
- "_prepareNextEnumeratorWithState:"
- "_prepareTransportGroupForOneBatch"
- "_prepareUploadBatch"
- "_preparedUploadResourceTasks"
- "_preparingFirstSessionStartDate"
- "_preventObserving"
- "_previewData"
- "_previewImageData"
- "_previewImageDatas"
- "_previousItemsPtrLength"
- "_previousResultValuesCount"
- "_previousResultValuesLength"
- "_previousScopeChange"
- "_primaryScope"
- "_prioritizeNonDerivatives"
- "_priority"
- "_privateCloudScopedIdentifier"
- "_privateScopedIdentifierForSharedScopedIdentifier:"
- "_problematicFormerSharedScopeIdentifier"
- "_progress"
- "_progressHandler"
- "_projectData"
- "_projectDocumentType"
- "_projectPreviewImageData"
- "_promisedAssetCount"
- "_promisedPhotosCount"
- "_promisedVideosCount"
- "_propertiesPerClass"
- "_propertyClasses"
- "_propertyGetter"
- "_propertyGetterIMP"
- "_propertySetter"
- "_propertySetterIMP"
- "_propertyType"
- "_proposedKey"
- "_proposedPrivateScopedIdentifier"
- "_proposedRescheduleDate"
- "_proposedScheduleDate"
- "_protectAgainstFastRelaunch"
- "_provider"
- "_proxyLibraryManager"
- "_pruneRequests"
- "_pruneStatsQueue"
- "_publicPermission"
- "_pullQueue"
- "_pullTaskItem"
- "_purgeabilityCheckRequests"
- "_pushChangeTasks"
- "_pushContext"
- "_pushContexts"
- "_pushObservers"
- "_pushRepository"
- "_pushRepositoryPriority"
- "_pushTaskDidFinishWithError:"
- "_quarantineMessages"
- "_quarantineRejectedRecords:error:"
- "_quarantinedRecords"
- "_query"
- "_queryDescription"
- "_queryTask"
- "_queue"
- "_queuedDate"
- "_radiosPreferences"
- "_readOnly"
- "_realChangeFromChange:comparedToStoredRecord:changeType:"
- "_realCloudScopedIdentifier"
- "_realConnection"
- "_realConnectionLock"
- "_realIDMapping"
- "_realIdentifier"
- "_realScopeIdentifiersFromScopeIdentifiers:"
- "_reallyCancelled"
- "_reallyHideNetworkIndicatorForBundleWithIdentifierLocked:"
- "_reallyHideSyncIndicator"
- "_reallyLaunched"
- "_reallyNoteServerHasChangesLocked"
- "_reallyNotifySchedulerPullQueueIsFull"
- "_reallyOpenWithCompletionHandler:"
- "_reallyPerformBatchedTransactionsLocked"
- "_reallySchedulePendingUpdateApply"
- "_reallySendFeedbackToServer"
- "_reallyShowNetworkIndicatorForBundleWithIdentifierLocked:"
- "_reallyShowSyncIndicator"
- "_reallyStartSyncSession:"
- "_reallyUnschedulePendingUpdateApply"
- "_reallyUnscheduleSession"
- "_reason"
- "_reasons"
- "_reasonsToOverrideSystemBudget"
- "_record"
- "_recordChangeData"
- "_recordClass"
- "_recordComputeStateDelegate"
- "_recordComputeStatePushQueue"
- "_recordCount"
- "_recordExistsOnServer"
- "_recordKnownByCloudCache"
- "_recordList"
- "_recordModificationDate"
- "_recordOnServer"
- "_recordWithStatusChangesToNotify"
- "_records"
- "_recordsToFetch"
- "_recoverFromCrashWithRecoveryHandler:error:"
- "_redactedPath"
- "_reenableSchedulerForForcedTaskIfNecessary"
- "_reenqueueExtractedBatchWithRejectedRecords:extractedBatch:error:"
- "_refreshIntervalKey"
- "_registerReasonLocked:"
- "_rejected"
- "_rejectedCount"
- "_rejectedPersonIdentifier"
- "_rejectedPersonIdentifiers"
- "_rejectedRecords"
- "_rejectedRecordsHasChanges"
- "_relatedIdentifier"
- "_relatedRecordClass"
- "_relatedRecordShouldBeShared"
- "_relation"
- "_relaunchFetchChangesFromOtherRewindSyncAnchors"
- "_releaseAssertion"
- "_releaseDirty"
- "_relevantUntilDate"
- "_remainingGenerators"
- "_remainingStoragesToCleanup"
- "_remapScopedIdentifier:to:class:inBatch:store:idMapping:cloudCache:remappedRecords:error:"
- "_remapSharedRecord:target:"
- "_remappedRecords"
- "_removeBrokenScope:"
- "_removeIdentityFromUncommittedFiles:"
- "_removeScopedIdentifiersFromSet:withScopeIdentifier:"
- "_removeStatusesInDictionary:withScopeIdentifier:"
- "_removeTransactionOnCurrentThread:"
- "_reportDownloadedTasks"
- "_reportQuarantineCountIfNecessaryWithLastReportDate:"
- "_reportTimer"
- "_requestMissingPayloads"
- "_requestMissingPayloadsProgress"
- "_requestUpdateOfMainScopeFromTransport"
- "_requests"
- "_requiredFirstState"
- "_requiredStateAtEndOfSyncSession"
- "_requiredStateObserverBlock"
- "_rescheduler"
- "_resetCompleteSyncStateForScope:error:"
- "_resetCompleteSyncStateIncludingIDMappingWithCause:scope:error:"
- "_resetCompleteSyncStateWithCause:scope:error:"
- "_resetEvents"
- "_resetEventsDescriptions"
- "_resetEventsJSON"
- "_resetEventsURL"
- "_resetFirstSynchronizationMarker"
- "_resetGlobalStateWithError:"
- "_resetGlobalsForMainScope"
- "_resetLocalSyncStateForScope:error:"
- "_resetLocalSyncStateWithCause:scope:date:error:"
- "_resetPriority"
- "_resetReasons"
- "_resetStrategy"
- "_resetSyncAnchorWithCause:scope:error:"
- "_resetTracker"
- "_resetType"
- "_reshareTask"
- "_resource"
- "_resourceCopyFromScopedIdentifier"
- "_resourceData"
- "_resourceIdentitiesFromChange:"
- "_resourcePerResourceType"
- "_resourceProgressDelegate"
- "_resourceSize"
- "_resourceSizeIsCalculated"
- "_resourceStorage"
- "_resourceStorageCopyTaskForResource:taskIdentifier:cloudResource:ofRecord:target:didStartHandler:progressHandler:completionHandler:"
- "_resourceType"
- "_resources"
- "_resourcesPerType"
- "_resourcesToGenerateImageDerivatives"
- "_resourcesToGenerateVideoComplementDerivatives"
- "_resourcesToUpload"
- "_responses"
- "_restartSyncSessionFromStateLocked:session:cancelIfNecessary:"
- "_resultValues"
- "_retainAssertion"
- "_retryAfterMillis"
- "_retryImmediately"
- "_retryingFetchingTransportScope"
- "_reverseMappingForLibraryOptions"
- "_revertRecords"
- "_revertedChanges"
- "_revertedChangesBatch"
- "_rewindAnchorsPerSharingScopesData"
- "_rewindFeatureVersion"
- "_rewindSyncAnchor"
- "_role"
- "_rootObject"
- "_ruleGroup"
- "_ruleGroups"
- "_rulesForOtherRecordFetches"
- "_rulesForRecordFetch"
- "_runtimeCharacteristics"
- "_save"
- "_scheduleAScopeUpdate"
- "_scheduleATransportUpdate"
- "_scheduleBatchedTransactionsLocked"
- "_scheduleDisabledFeatureUpdateOnWriteSuccess"
- "_scheduleEndWithTimeInterval:"
- "_scheduleNextSyncSession"
- "_schedulePendingUpdateApply"
- "_schedulePendingUpdateApplyOnWriteSuccess"
- "_schedulePullFromClient"
- "_schedulePullFromTransport"
- "_schedulePushHighPriorityToTransportChangeTypes"
- "_schedulePushToTransportChangeTypes"
- "_scheduleSetupOnWriteSuccess"
- "_scheduledOverrides"
- "_scheduler"
- "_schedulerBlocker"
- "_scope"
- "_scopeByCloudIndex"
- "_scopeByLocalIndex"
- "_scopeByStableIndex"
- "_scopeCache"
- "_scopeChangeToBePulledByClientForScope:"
- "_scopeFilter"
- "_scopeIdentifier"
- "_scopeIdentifiers"
- "_scopeIdentifiersBeingCreated"
- "_scopeIdentifiersExcludedFromMingling"
- "_scopeIdentifiersExcludedFromPushToTransport"
- "_scopeIndex"
- "_scopeMapping"
- "_scopeObservers"
- "_scopeType"
- "_scopeWithIdentifier:"
- "_scopedIdentifier"
- "_scopedIdentifiersWithUnknownTargets"
- "_scopes"
- "_scopesChangeBatch"
- "_scopesToRemoveFromBrokenScopes"
- "_score"
- "_selector"
- "_sendFeedbackToServerIfNecessary"
- "_sendQuarantineFeedbackWithRecordClass:reason:"
- "_sendTask"
- "_sentBatchTimeInterval"
- "_sequenceNumber"
- "_serverFeatureCompatibleVersionToUpdate"
- "_serverMessage"
- "_serverRecordIsCorrupted"
- "_serverResourcesMatches:"
- "_session"
- "_sessionIdentifier"
- "_sessionInformation"
- "_sessionLock"
- "_sessionProgress"
- "_setAdditionalRecords:"
- "_setBackgroundDownloadTaskIdentifier:"
- "_setCancelled:"
- "_setChangeType:"
- "_setCurrentClosingComponentName:"
- "_setCurrentSession:"
- "_setCurrentTask:"
- "_setError"
- "_setFaceStateBit:fromBoolValue:"
- "_setIgnoredRecord:"
- "_setLibraryVersion:"
- "_setObjectInStatus:forKey:"
- "_setOfScopeIdentifiersFromEnumeration:"
- "_setPushContext:"
- "_setQueue:"
- "_setRecordKnownByCloudCache:"
- "_setRecords:"
- "_setRequiredFirstState:"
- "_setScopeType:forScope:error:"
- "_setSharingScopeIdentifier:"
- "_setSharingScopeIdentifier:error:"
- "_setShouldNotTrustCloudCache:"
- "_setSizeOfResourcesToUpload:sizeOfOriginalResourcesToUpload:numberOfImages:numberOfVideos:numberOfOtherItems:"
- "_setState:"
- "_setStatus:andError:"
- "_setStatusFromDictionary:"
- "_setTarget:forRecordWithScopedIdentifier:isUpdate:"
- "_setTransactionOnCurrentThread:"
- "_setTransportUserIdentifier:"
- "_settingName"
- "_setupConnection"
- "_setupIsDone"
- "_setupTask"
- "_setupTaskWithCompletionHandler:"
- "_share"
- "_shareCount"
- "_shareURL"
- "_sharedCloudScopedIdentifier"
- "_sharedDeleteFromDelete:"
- "_sharedLibrarySharingState"
- "_sharedRecordAsPrivateRecord:target:"
- "_sharedScope"
- "_sharingContributorUserIdentifiers"
- "_sharingRecordChangeData"
- "_sharingRecordIdentifier"
- "_sharingScopeIdentifier"
- "_shouldAssertOnFingerprinting"
- "_shouldBackOffOnErrorBlock"
- "_shouldBeCreatedDynamically"
- "_shouldBeTemporarilyNonDiscretionary"
- "_shouldBypassCaches"
- "_shouldChangeSyncManagerPriorityBoost"
- "_shouldCheckAssetsWithServerWhenOverQuota"
- "_shouldCheckEPPCapability"
- "_shouldCheckFilesForUpload"
- "_shouldCheckOverQuotaChangesWithServer"
- "_shouldCheckResourcesAhead"
- "_shouldCompareAllProperties"
- "_shouldConsiderRequestingMoreTime"
- "_shouldCreateTempFolder"
- "_shouldDeletePrivateRecordWithNaturalPrivateScopedIdentifier:correctPrivateScopedIdentifier:cloudCache:transientPullRepository:"
- "_shouldEnableScopeListSyncOnWriteSuccess"
- "_shouldFilterDefaultValuesForNewProperties"
- "_shouldHaveRequestedMoreTime"
- "_shouldNotTrustCloudCache"
- "_shouldNotTrustCloudCacheAfterError:"
- "_shouldNoteServerHasChanges"
- "_shouldOnlyUploadNewResources"
- "_shouldRequestABackgroundDownloadSyncPhase"
- "_shouldRequestACleanupToScheduler"
- "_shouldRequestMoreTime"
- "_shouldRescheduleASyncSession"
- "_shouldResetGlobalsForMainScope"
- "_shouldResetPlatformTrackAllStoresAndDeletes"
- "_shouldRestartSessionFromState"
- "_shouldSetupEstimatedSize"
- "_shouldShowAlertToUser"
- "_shouldStashMasterRecords"
- "_shouldStashRecordsIfNecessary"
- "_shouldStop"
- "_shouldStoreInitialSyncAnchor"
- "_shouldSyncScopeList"
- "_shouldSyncScopeListQueue"
- "_shouldSyncScopeListWithOptions:"
- "_shouldTriggerCompleteResetSyncAfterDisabledFeaturesUpdate"
- "_shouldTriggerResetSyncAfterDisabledFeaturesUpdate"
- "_shouldTryToMingleImmediately"
- "_shouldUpdateDisabledFeatures"
- "_shouldUpdateGlobalStatusAtEndOfTransaction"
- "_shouldUploadBatchesWithDropReason:shouldQuarantineRecords:inTransaction:"
- "_showAlertWithMessage:readMoreURL:createRadarURL:showsRecoverButton:"
- "_significantWorkCalls"
- "_similarToOriginalAdjustmentsFingerprint"
- "_simpleAdjustmentData"
- "_simpleDescription"
- "_size"
- "_sizeOfOriginalResourcesToUpload"
- "_sizeOfResourcesToUpload"
- "_sizeOfResourcesToUploadIsSet"
- "_skipInfoForAssetChange"
- "_skipInfoForMasterChange"
- "_someScopeMightHaveToBePulledByClient"
- "_sourceResource"
- "_sourceResourceType"
- "_stableHash"
- "_stableIndex"
- "_stage"
- "_stagedScopeChange"
- "_stagedScopeFlags"
- "_stagedTransportScope"
- "_stagingScope"
- "_stagingScopeIdentifier"
- "_stagingTransportScope"
- "_startActualCleanup"
- "_startDate"
- "_startOfDerivativesGeneration"
- "_startOfIteration"
- "_startOverridingBudget:reason:"
- "_startRequiredSyncSession:"
- "_startSyncSession:withMinimalPhase:rewind:"
- "_startTime"
- "_startWaitingForBatch"
- "_startWatchingNode"
- "_startWatchingParent"
- "_startWatchingPermanentDataOverride"
- "_state"
- "_stateProgressDates"
- "_status"
- "_statusCenter"
- "_statusClient"
- "_statusDidChange"
- "_statusError"
- "_statusFileURL"
- "_statusFromCachesWithRecordScopedIdentifier:"
- "_statusKey"
- "_stepEnumerator"
- "_steps"
- "_stopError"
- "_stopOverridingBudget:reason:"
- "_stopPreparingFirstSession"
- "_stopWatchingNode"
- "_stopWatchingParent"
- "_stopWatchingPermanentDataOverride"
- "_storage"
- "_storageDescription"
- "_storageScopeType"
- "_storages"
- "_store"
- "_storeChangeSessionUpdate:error:"
- "_storeInitialSyncAnchorIfNecessaryInTransaction:"
- "_storeReasonsLocked"
- "_storeResetEvent:scopeIdentifier:date:cause:"
- "_storeResetEvent:scopeIdentifier:date:pending:cause:"
- "_storeRewindSyncAnchors:inScopes:error:"
- "_storeVoucher:forTaskWithIdentifier:"
- "_storedClientRecords"
- "_storedCloudRecords"
- "_storedDisabledFeatures"
- "_storedTransportGroup"
- "_strategyName"
- "_structName"
- "_subcategory"
- "_subtitle"
- "_subtype"
- "_successSize"
- "_successStatsPerResourceType"
- "_successfullyDownloadedResourcesCount"
- "_suffix"
- "_superWasCalled"
- "_supervisor"
- "_supportsBudgetOverride"
- "_syncAnchorsOfPartnerScopesThatMightNeedToPullChanges"
- "_syncHasBeenRequested"
- "_syncManager"
- "_syncManagerPriorityBoost"
- "_syncOutstandingInvocations"
- "_syncOutstandingInvocationsCount"
- "_syncSession"
- "_syncSessionIsPossible"
- "_syncStatus"
- "_syncTaskEnumerator"
- "_syndicationIdentifier"
- "_synthesizedRecord"
- "_systemBudgetForBudgetKey:"
- "_systemMonitor"
- "_target"
- "_targetForPrivateScopedIdentifier:"
- "_targetForSharedScopedIdentifier:"
- "_targetMapping"
- "_targetState"
- "_targetWithRecord:cloudScopedIdentifier:trustRecordChangeData:"
- "_targetWithShareableRecord:cloudScopedIdentifier:otherScopedIdentifier:sharedScope:trustRecordChangeData:"
- "_targets"
- "_targetsFromOtherScopedIdentifier"
- "_taskClass"
- "_taskCountLock"
- "_taskDidFinishWithErrorBlock"
- "_taskIdentifier"
- "_taskIdentifierForQueue"
- "_taskItem"
- "_taskStartDate"
- "_tasksByType"
- "_tempFolderIndex"
- "_tempFolderURL"
- "_tempFolderURLForGeneratedResourcesWithReferenceResource:adjustment:includePosterFrame:"
- "_tentative"
- "_testKey:value:completionHandler:"
- "_testMessage"
- "_throttlingDate"
- "_throughputReporter"
- "_throughputReporterLock"
- "_thumbnailImageData"
- "_timeRange"
- "_timeZoneName"
- "_timeZoneOffset"
- "_timer"
- "_timerForPushRepositoryFlagsCountsHaveChanged"
- "_timingStatisticQueue"
- "_timingStatisticStatuses"
- "_timingStatistics"
- "_title"
- "_torsoFaceInstances"
- "_totalAssetCount"
- "_totalAssetCountForScope"
- "_totalAssetCountHasBeenCalculated"
- "_totalCount"
- "_trackAllStoresAndDeletesUntilEndOfTransaction"
- "_trackingChangeType"
- "_transactionClientCacheView"
- "_transactionClientCacheViewHasPushRepository"
- "_transactionDidFinish"
- "_transactionDuringItemsPreparation"
- "_transactionNewPredictions"
- "_transactionStartDate"
- "_transactionTransportScopeMapping"
- "_transactionWillBeginOnThread:"
- "_transferIgnoredRecordToTransientPullRepository:error:"
- "_transferTasks"
- "_transferTasksBurstCount"
- "_transientPullRepository"
- "_transientPullRepositoryInStore:"
- "_transientRepository"
- "_transientStatuses"
- "_translator"
- "_transport"
- "_transportGroup"
- "_transportIdentifier"
- "_transportScope"
- "_transportScopes"
- "_transportShare"
- "_transportTask"
- "_transportTaskCount"
- "_transportTaskDidFinish:"
- "_transportTasks"
- "_transportUserIdentifier"
- "_transportUserIdentifierLock"
- "_trashedReason"
- "_tryCreatingCacheFolder"
- "_type"
- "_unacknowledgedBatch"
- "_unarchiving"
- "_unavailabilityLimitDate"
- "_unavailabilityReason"
- "_unblock"
- "_unblockOnceElements"
- "_uncommittedFiles"
- "_unionEnumerationWithPrivateRecordEnumeratorGenerator:sharedRecordGenerator:"
- "_unquarantinedRecordScopedIdentifiers"
- "_unscheduleNextSyncSession"
- "_unschedulePendingUpdateApply"
- "_unschedulePendingUpdateApplyOnWriteSuccess"
- "_unscopedIdentifier"
- "_unstashRecordsForScope:"
- "_untrustableScopedIdentifiers"
- "_unwatchPredictor"
- "_updateActiveDownloadTaskCount"
- "_updateAirplaneMode"
- "_updateBatteryWithBatteryEntry:"
- "_updateCellularPolicy:"
- "_updateCellularPolicyFromPolicies:"
- "_updateChange:fromOldChange:withResources:excludeImages:"
- "_updateComputeSyncUploadMetricsWithError:"
- "_updateConfigurationDictionary:"
- "_updateConfigurationWithFetchData:fetchError:fetchURL:fromConfigurationDictionary:"
- "_updateContributors:"
- "_updateContributorsTask"
- "_updateFingerprintContext"
- "_updateGlobalStatusWithScopeChange:forScope:"
- "_updateInterval"
- "_updateIntervalKey"
- "_updateLastFeatureVersionAndRelaunchFetchChangesFromSyncAnchor:"
- "_updateLastSyncDateIfNecessaryLocked"
- "_updateNetworkState:"
- "_updateOverridingForeground"
- "_updatePrediction:"
- "_updatePrivateScopedIdentifierForUnknownTarget:"
- "_updateQuotaStrategyAfterSuccessInTransaction:"
- "_updateScopeChangeForPrimaryScopeRelatedToSharingScopeWithIdentifier:completionHandler:"
- "_updateScopeWithNewScopeType:scope:updatedScopeChange:updatedFlags:oldTransportScope:updatedTransportScope:shouldUpdateTransportScope:store:transport:session:inTransaction:"
- "_updateScopeWithNewScopeType:updatedScopeChange:updatedFlags:oldTransportScope:session:updatedTransportScope:"
- "_updateSharingContributorUserIdentifiers"
- "_updateShouldSyncScopeList:"
- "_updateTask"
- "_updateTotalAssetCountWithAssetCounts:"
- "_updateTransportScope"
- "_updateWatchingNode"
- "_updatedFlagsMask"
- "_updatedRecords"
- "_updatedResourcesPerType"
- "_updatedScopedIdentifiers"
- "_uploadChangesWithPriority:maxBatchSize:"
- "_uploadComputeStatesTask"
- "_uploadComputeStatesTaskDidFinishWithError:"
- "_uploadExtractedBatch"
- "_uploadIdentifier"
- "_uploadRateQueue"
- "_uploadResourceTasks"
- "_uploadTask"
- "_uploadTask:didFinishWithError:"
- "_uploadTaskDidFinishWithError:"
- "_uploadTaskDidStartForResource:withTaskIdentifier:"
- "_uploadTasks"
- "_useCourtesyMingling"
- "_useFinal"
- "_userActionOptions"
- "_userDefinedRules"
- "_userIdentifier"
- "_userModificationDate"
- "_userOverride"
- "_userViewedParticipantTrashNotificationDate"
- "_usesMMCSv2AsDefault"
- "_uti"
- "_uuid"
- "_validCloudIndexes"
- "_validLocalIndexes"
- "_validScopeIdentifiers"
- "_value"
- "_verifiedType"
- "_version"
- "_versionHistory"
- "_versionToAnchor"
- "_videoComplementDurationTimescale"
- "_videoComplementDurationValue"
- "_videoComplementImageDisplayTimescale"
- "_videoComplementImageDisplayValue"
- "_videoComplementVisibilityState"
- "_videoFrameRate"
- "_videosCount"
- "_viewCount"
- "_viewPresentation"
- "_volumeURL"
- "_vouchersPerTaskIdentifier"
- "_wasBusy"
- "_watchOrUnwatchPredictorIfNecessary"
- "_watchPredictor"
- "_watcher"
- "_watchingPredictor"
- "_weakLibraryManager"
- "_weakSelf"
- "_willNeedToAccessScopeWithIdentifier:error:"
- "_willNeedToAccessScopeWithIdentifier:primaryScope:error:"
- "_willOpenComponent:"
- "_withSystemBudgetOverride:"
- "_withVoucherForTaskWithIdentifier:do:"
- "_writeFirstSynchronizationMarker"
- "_writeInitialSyncMarkerForDate:error:"
- "_writeTransactionBlocker"
- "_zeroByteFileFingerprint"
- "_zeroByteFileFingerprintOnce"
- "aa_personID"
- "aa_primaryAppleAccount"
- "absoluteString"
- "abstractObject"
- "acceptMomentShare:completionHandler:"
- "acceptSharedScope:completionHandler:"
- "acceptTaskForSharedScope:completionHandler:"
- "acceptanceStatus"
- "accountFlagsData"
- "acknowledgeChangeBatch:withCompletionHandler:"
- "acknowledgeChangedStatus:hasBeenDeleted:error:"
- "acknowledgeChangedStatuses:"
- "acknowledgeChangedStatuses:error:"
- "acknowledgeContributorsUpdates:error:"
- "acknowledgeNewClientRecord:withScopedIdentifier:"
- "ackownledgeRecordWithScopedIdentifier:error:"
- "acquireReschedulerTaskWithCompletionHandler:"
- "activateScope:error:"
- "activateScopeWithIdentifier:completionHandler:"
- "activated"
- "activationDateForScope:"
- "activityState"
- "addAddEventForRecordWithLocalScopedIdentifier:direction:error:"
- "addAdditionalRecordWithScopedIdentifierToUploadBatch:"
- "addAsset:"
- "addBarrierBlock:"
- "addBrokenScope:"
- "addChange:fromStorage:"
- "addCleanupBlock:"
- "addCleanupTaskForScopeWithIndex:scopeIdentifier:scopeType:error:"
- "addCleanupTasksForScope:error:"
- "addCloudScopedIdentifier:forLocalScopedIdentifier:isFinal:direction:error:"
- "addCompletedWorkBytesCount:kindOfWork:"
- "addCompletedWorkItemCount:"
- "addCompletedWorkItemCount:kindOfWork:"
- "addComputeState:discardedFileStorageIdentifier:error:"
- "addComputeState:error:"
- "addConcreteScope:forScope:"
- "addCountOfPulledAssets:"
- "addCuratedAssetIdentifiers:"
- "addDeferHandler:"
- "addDeleteEventForRecordWithLocalScopedIdentifier:direction:error:"
- "addDeleteFlagToFileAtURL:error:"
- "addDequeueObserver:"
- "addDequeueObserverWithDequeueSignalBlock:"
- "addDropDerivativesRecipe:writeToUserDefaults:withCompletionHandler:"
- "addEntriesFromDictionary:"
- "addExitingUserIdentifiers:"
- "addFace:"
- "addFaceInstances:"
- "addIgnoredRecord:ignoredDate:otherScopeIndex:error:"
- "addIndex:"
- "addInfoToLog:"
- "addKeysAndValues:"
- "addKnownTarget:forRecordWithScopedIdentifier:"
- "addLocalComputeStateToUpload:cloudComputeState:"
- "addMemory:"
- "addMessages:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addObserverForName:object:queue:usingBlock:"
- "addPartnerScope:mostCurrentSyncAnchor:"
- "addPerson:"
- "addPetFaceInstances:"
- "addPreviewImageData:"
- "addPushObserver:withIdentifier:"
- "addPushPullGatekeeper:error:"
- "addQuarantinedRecordWithScopedIdentifier:recordClass:reason:error:"
- "addQuarantinedRecordWithScopedIdentifier:related:recordClass:reason:error:"
- "addRecord:"
- "addRecord:isFinal:error:"
- "addRecordsFromBatch:"
- "addRecordsToRevertWithLocalScopedIdentifier:class:error:"
- "addRejectedPersonIdentifiers:"
- "addRemappedRecordWithScopedIdentifier:realScopedIdentifier:error:"
- "addRequest:"
- "addResource:"
- "addResourceType:"
- "addResponse:"
- "addRewindSyncAnchor:forScope:error:"
- "addScopeFlagsObserver:withIdentifier:"
- "addScopeWithIdentifier:scopeType:error:"
- "addServerDropDerivativesRecipe:"
- "addServerDropDerivativesRecipes:"
- "addStatus:error:"
- "addStatusChangesForRecordsWithScopedIdentifiers:persist:"
- "addSubscriberUsingPublishingHandler:"
- "addSyncAnchor:forFeatureVersion:"
- "addTask:forRecordWithScopedIdentifier:"
- "addTorsoFaceInstances:"
- "addTransferTask:"
- "addTransportScope:forScope:"
- "addTransportScopeForScope:scopes:allowsTentativeTransportScope:useStagingScopeIfNecessary:error:"
- "addTransportScopeForScopeIdentifier:scopes:useStagingScopeIfNecessary:error:"
- "addTransportTask:"
- "addedRecords"
- "additionalRecordWithScopedIdentifier:"
- "adjustmentSimpleDescription"
- "airplaneMode"
- "airplaneModeChanged"
- "alertMessage"
- "alertTitle"
- "allChangeBatches"
- "allChangesWithClass:relatedScopedIdentifier:"
- "allChangesWithClass:scopeIdentifier:changeType:"
- "allChangesWithClass:scopeIdentifier:trashed:"
- "allChangesWithClass:secondaryScopedIdentifier:"
- "allChangesWithScopeIdentifier:"
- "allKeys"
- "allLibraryOptionsDescriptions"
- "allNonDeletedChangesWithClass:scopeIdentifier:"
- "allObjects"
- "allRecordsIsFinal:"
- "allRelatedScopedIdentifiers"
- "allResources"
- "allResourcesAreAvailable"
- "allScopeIdentifiersIncludeInactive:"
- "allStatusChanges"
- "allTargetScopedIdentifiers"
- "allTransferTasks"
- "allUnmingledChangesWithClass:relatedScopedIdentifier:"
- "allUnmingledChangesWithClass:scopeIdentifier:"
- "allUnmingledChangesWithScopeIdentifier:"
- "allUnmingledDeletedChangesWithClass:scopeIdentifier:"
- "allUnmingledNonDeletedChangesWithClass:scopeIdentifier:"
- "allValues"
- "allocWithZone:"
- "allowOperationBoot"
- "allowing operations boost"
- "allowing operations boost (including background)"
- "allowsAssetsWithResourcesButNoAdjustments"
- "allowsBackgroundDispatch"
- "allowsForcedTaskQueuing"
- "allowsKeyedCoding"
- "allowsLocalConflictResolution"
- "allowsLocalConflictResolutionWhenOverQuota"
- "allowsStreaming"
- "allowsToOnlyUploadNewResources"
- "allowsUnsafeClientCache"
- "alternateRecoverDescription"
- "altitude"
- "alwaysCreateEPPMomentShares"
- "anyObject"
- "appendBatch:alreadyMingled:countOfAssetChanges:error:"
- "appendBatch:alreadyMingled:error:"
- "appendChangeBatch:error:"
- "appendFormat:"
- "appendLocalResources:forItemWithCloudScopedIdentifier:"
- "appendString:"
- "applyBatch:isFinal:direction:withError:"
- "applyChange:"
- "applyChange:copyPropertiesToFinalChange:forChangeType:direction:diffTracker:"
- "applyChangeType:fromChange:"
- "applyHasBeenSuccessful"
- "applyPreviousChangeSessionUpdateWithExpectedLibraryVersion:error:"
- "applyShareRemapFixUpTasks:scope:store:onPutBatchInPullQueue:error:"
- "applyToStore:error:"
- "approximativeResourcesUploadRate"
- "archiveArrayOfCPLDropDerivativeRecipes:"
- "archiveCursor"
- "archivedDataWithRootObject:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "archivedDataWithRootObject:usingBlock:"
- "archivedPropertyList"
- "archivedPropertyListWithRootObject:"
- "archivedPropertyListWithRootObject:usingBlock:"
- "archiverContext"
- "areObjectsDifferentOnProperty:"
- "areObjectsDifferentOnProperty:changeType:"
- "areSomeUsersExiting"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayDescription"
- "arrayForKey:"
- "arrayWithContentsOfURL:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "asPlist"
- "asRecordView"
- "asShareParticipant"
- "asString"
- "assertCanRead"
- "assertCanWrite"
- "assertNoUnacknowledgedChanges"
- "assetAtIndex:"
- "assetCount"
- "assetScopedIdentifier"
- "assetType"
- "assets"
- "assetsCount"
- "associateCloudResource:ofRecord:"
- "attachComputeStates:completionHandler:"
- "attachDiffTracker:"
- "attachObject:withCompletionHandler:"
- "attachedDiffTracker"
- "autorelease"
- "availableExitSources"
- "availableResourceSizeForUploadIdentifier:"
- "availableResourceTypesToUploadForChange:"
- "availableRetentionPolicies"
- "awakeFromStorage"
- "backgroundDownloadDidFailForResource:"
- "backgroundDownloadDidFinishForResource:"
- "backgroundTask"
- "base64EncodedStringWithOptions:"
- "baseDerivativeResourceType"
- "baseRecordView"
- "baseStorageView"
- "baseURL"
- "baseVideoComplemenentResourceType"
- "batchCanLowerQuota"
- "batchStorageForScope:"
- "batchToUpload"
- "batteryLevelDidChangeWithLevel:"
- "becomeCurrentWithPendingUnitCount:"
- "beginChangeSession:withLibraryVersion:resetTracker:error:"
- "beginChangeSessionWithSessionToken:completionHandler:"
- "beginClientWork:"
- "beginCreatingScopeWithIdentifier:"
- "beginDownloadForResource:clientBundleID:highPriority:completionHandler:"
- "beginDownloadForResource:clientBundleID:highPriority:proposedTaskIdentifier:completionHandler:"
- "beginDownloadForResource:clientBundleID:intent:proposedTaskIdentifier:completionHandler:"
- "beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:completionHandler:"
- "beginDownloadForResource:clientBundleID:options:proposedTaskIdentifier:reply:"
- "beginDownloadForResource:highPriority:completionHandler:"
- "beginExtractingBatch"
- "beginInMemoryDownloadOfResource:clientBundleID:completionHandler:"
- "beginInMemoryDownloadOfResource:clientBundleID:reply:"
- "beginKindOfWork:"
- "beginPullChangeSessionWithKnownLibraryVersion:completionHandler:"
- "beginPullChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
- "beginPullSessionWithKnownLibraryVersion:context:completionHandler:"
- "beginPushChangeSessionWithKnownLibraryVersion:completionHandler:"
- "beginPushChangeSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
- "beginPushSessionWithKnownLibraryVersion:context:completionHandler:"
- "beginSessionForProxy:knownVersion:context:completionHandler:"
- "beginSessionWithKnownLibraryVersion:context:completionHandler:"
- "beginSessionWithKnownLibraryVersion:resetTracker:completionHandler:"
- "beginTransactionWithIdentifier:description:keepPower:"
- "bestErrorForUnderlyingError:"
- "bestFileNameForResource"
- "block"
- "blockAllSyncSessionsWithReason:onlyIfBlocked:block:"
- "blockEngineElement:"
- "blockEngineWithReason:onlyIfBlocked:block:"
- "blockWriteTransactionsWithCompletionHandler:"
- "blocker"
- "boolForKey:"
- "boolValue"
- "boostPriorityForScopeWithIdentifier:completionHandler:"
- "boundaryKey"
- "boundaryKeyDescription"
- "brokenMessage"
- "brokenScopes"
- "brokenTitle"
- "budget"
- "budgetOverrideReasonStorageKeyForBudget:"
- "bumpCloudIndexForScopeWithIdentifier:error:"
- "bumpLocalIndexForScopeWithIdentifier:error:"
- "bumpRejectedRecords:error:"
- "bumpStableIndexForScopeWithIdentifier:error:"
- "bundleForClass:"
- "busyStateForScope:"
- "bypassForceSyncLimitations"
- "byteCountFormatter"
- "bytes"
- "c16@0:8"
- "c24@0:8@16"
- "cacheScope:forScopeStorage:"
- "cacheURL"
- "cacheValidCloudIndexes:"
- "cacheValidLocalIndexes:"
- "cachedRecordWithScopedIdentifier:"
- "callDidFinish"
- "canActivateScope:error:"
- "canBoostBackgroundOperations"
- "canBoostOperations"
- "canGenerateImageDerivativesFromUTI:"
- "canLowerQuota"
- "canMatchSignatureToFingerprint"
- "canRead"
- "canUseNetwork"
- "canWrite"
- "cancel"
- "cancel:"
- "cancelAllTasks:"
- "cancelAndBlockAllSyncSessionsWithReason:block:"
- "cancelBlockedTasksIncludingBackground:"
- "cancelCurrentSyncSession"
- "cancelDownloadTask:"
- "cancelHandler"
- "cancelIfBlocked"
- "cancelScheduledForcedTaskForLaunch:"
- "cancelSyncTask:"
- "cancelSyncTaskWithIdentifier:"
- "cancelTask"
- "cancelTask:"
- "cancelTaskWithIdentifier:"
- "cancelledByEngine"
- "cellularRestricted"
- "change"
- "changeClass"
- "changeForType:"
- "changeIsOnlyAddingResourcesToRecord:addedResources:"
- "changePipeDidRemoveChanges"
- "changeRecordTypeFromShortDescription:"
- "changeStorage"
- "changeWithScopedIdentifier:"
- "changesWithRelatedScopedIdentifier:class:"
- "characterAtIndex:"
- "check"
- "checkBatchWithFoundRecords:error:"
- "checkBeforeUploadWithError:"
- "checkDefaultValueBlockForPropertyWithSelector:"
- "checkExpectedLibraryVersion:error:"
- "checkFileSizeForIdentity:"
- "checkHasBackgroundDownloadOperationsWithCompletionHandler:"
- "checkInBatchStorage:error:"
- "checkInitialSyncMarker"
- "checkIsEmpty"
- "checkOutBatchStorageWithPriority:error:"
- "checkPushedChange:"
- "checkResourcesAreSafeToPrune:checkServerIfNecessary:completionHandler:"
- "checkScopeIdentifier:"
- "checkScopeIsValidInTransaction:"
- "class"
- "classDescription"
- "classForCoder"
- "classForKeyedArchiver"
- "classForQuarantinedRecordWithScopedIdentifier:"
- "classForStoredClassName:forCPLArchiver:"
- "classNameOfRecordsForInitialQueryForScope:"
- "classOfRecordsForInitialQueryForScope:"
- "classesForSelector:argumentIndex:ofReply:"
- "cleanupAfterExtractingBatch"
- "cleanupStagedScope:stagingScope:destinationScope:transportScopeMapping:progressHandler:completionHandler:"
- "cleanupStepHasMore:deletedCount:error:"
- "cleanupWithError:"
- "clearAllPushPullGatekeepersWithError:"
- "clearAllQuotaFlagsForMainScopeWithReason:error:"
- "clearAssets"
- "clearChangeType:"
- "clearCuratedAssetIdentifiers"
- "clearFaceInstances"
- "clearIdentifiers"
- "clearKeysAndValues"
- "clearMemorys"
- "clearMessages"
- "clearPersons"
- "clearPetFaceInstances"
- "clearPreviewImageDatas"
- "clearRejectedPersonIdentifiers"
- "clearRequests"
- "clearResponses"
- "clearState"
- "clearTorsoFaceInstances"
- "clearTransportGroupsForScope:error:"
- "clientAcknowledgedScopeChanges:error:"
- "clientAppBundleIdentifier"
- "clientBatch"
- "clientBundleID"
- "clientCacheBaseViewIDMappingForStore:"
- "clientCanPushScopeChange:"
- "clientDidAcknowledgeBatchBlock"
- "clientFeatureCompatibleVersion"
- "clientIsPushingChanges"
- "clientLibraryBaseURL"
- "clientNeedsToPullTaskForScope:"
- "clientProtocolInterface"
- "clientWillAcknowledgeBatchBlock"
- "closeAndDeactivate:completionHandler:"
- "closeFile"
- "closeLibraryWithCompletionHandler:"
- "closeWithCompletionHandler:"
- "closeWithError:"
- "cloudBatch"
- "cloudCacheGetDescriptionForRecordWithScopedIdentifier:completionHandler:"
- "cloudCacheGetDescriptionForRecordWithScopedIdentifier:related:completionHandler:"
- "cloudChangeBatchFromBatch:usingMapping:isFinal:withError:"
- "cloudComputeStatesToUpload"
- "cloudLibraryResourceStorageURL"
- "cloudLibraryStateStorageURL"
- "cloudRecord"
- "cloudResource"
- "cloudResourceForLocalResource:cloudRecord:target:shouldNotTrustCaches:allowUnsafeClientCache:transportScopeMapping:error:"
- "cloudScopedIdentifierForLocalScopedIdentifier:isFinal:"
- "coalescingInterval"
- "code"
- "com.apple.PhotoLibraryServices.PhotosDiagnostics"
- "com.apple.cpl.brokenscope"
- "com.apple.cpl.connectedlibrarymanagers"
- "com.apple.cpl.multiscopetask.currenttask"
- "com.apple.warnalert"
- "commitChangeBatch:completionHandler:"
- "commitChangeBatch:withCompletionHandler:"
- "commitChangeBatch:withUnderlyingCompletionHandler:"
- "commitFileWithIdentifier:error:"
- "commitFileWithIdentity:error:"
- "commitStagedChangesForScopeWithIdentifier:error:"
- "commitSyncAnchorForScope:error:"
- "compactChangeBatchesWithError:"
- "compactFileCacheWithCompletionHandler:"
- "compactStorage:"
- "compactStorageIncludeOriginals:error:"
- "compactWithError:"
- "compactedBatchFromExpandedBatch:"
- "compactedChangeWithRelatedChanges:isOnlyChange:fullRecord:usingStorageView:"
- "compare:"
- "compareObject:toObject:"
- "completionHandler"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "componentsWithString:"
- "computeDiff"
- "computeExpandedBatchWithError:"
- "computeStatesToUploadWithScopeIdentifier:localState:maximumCount:"
- "concreteScopeForScopeWithIdentifier:"
- "concreteScopeFromTransportScope:"
- "configurationDictionary"
- "configurationDictionaryUniquifier"
- "configurationFetcher:didUpdateConfigurationDictionary:configurationHasChanged:"
- "configurationURL"
- "configureDirectTransportTask:"
- "confirmAllRecordsWithError:"
- "confirmed"
- "conformsToProtocol:"
- "conformsToType:"
- "connectWithCompletionHandler:"
- "connection:handleInvocation:isReply:"
- "constrained"
- "containerDescription"
- "containerRelationChangesComparedToRelationEnumerator:error:"
- "containerScopedIdentifier"
- "containsIndex:"
- "containsObject:"
- "containsResourceType:"
- "containsTask:"
- "containsValueForKey:"
- "contributorsUpdatesForScopeWithIdentifier:maxCount:"
- "coordinate"
- "copy"
- "copyAddingFileURL:"
- "copyChangeType:"
- "copyConfigurationDictionaryWithUpdatedDate"
- "copyConfigurationDictionaryWithUpdatedKey:value:"
- "copyContextWithPriority:"
- "copyContextWithUploadIdentifier:"
- "copyDerivatives:count:avoidResourceType:fromRecord:inResourcePerType:"
- "copyDerivativesFromRecordIfPossible:"
- "copyPropertyBlockForDirection:"
- "copyTo:"
- "copyWithScopeType:"
- "copyWithZone:"
- "corruptionInfo"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForKey:"
- "countForObject:"
- "countOfAssetsWithResourcesToUpload"
- "countOfChangesInScopeWithIdentifier:"
- "countOfCloudComputeStatesToUpload"
- "countOfComputeStates"
- "countOfOriginalImages"
- "countOfOriginalOthers"
- "countOfOriginalVideos"
- "countOfQuarantinedRecords"
- "countOfQuarantinedRecordsInScopeWithIdentifier:"
- "countOfQueuedBatches"
- "countOfQueuedDownloadTasks"
- "countOfRecordsAcknowledgedByClientWithRelatedScopedIdentifier:class:"
- "countOfRecordsWithRelatedScopedIdentifier:class:"
- "countOfResourceTypes"
- "countOfSharingRecords"
- "countOfTransferTasks"
- "countOfTransferTasksInTransportTasks"
- "countOfTransportTasks"
- "countOfUncommittedFiles"
- "countOfUnmingledRecords"
- "countOfUnsharingRecords"
- "countPerFlags"
- "countPerFlagsForScopeWithIdentifier:"
- "course"
- "cplAdditionalSecureClassesForProperty:"
- "cplAllPropertyNames"
- "cplClearProperties:"
- "cplCopyItemAtURL:toURL:error:"
- "cplCopyProperties:fromObject:withCopyBlock:"
- "cplCopyPropertiesFromObject:withCopyBlock:"
- "cplDebugDescription"
- "cplDecodeBoolForKey:"
- "cplDecodeCharForKey:"
- "cplDecodePropertiesFromCoder:"
- "cplDeepCopy"
- "cplDumpProperties"
- "cplEncodePropertiesWithCoder:"
- "cplErrorCausedBySharedSyncForError:"
- "cplErrorWithCode:description:"
- "cplErrorWithCode:description:arguments:"
- "cplErrorWithCode:underlyingError:description:"
- "cplErrorWithCode:underlyingError:description:arguments:"
- "cplErrorWithCode:underlyingError:userInfo:description:"
- "cplErrorWithCode:underlyingError:userInfo:description:arguments:"
- "cplFileExistsAtURL:"
- "cplFullDescription"
- "cplHash"
- "cplIsEqual:"
- "cplIsEqual:withEqualityBlock:"
- "cplIsFileDoesNotExistError:"
- "cplIsFileExistsError:"
- "cplMoveItemAtURL:toURL:error:"
- "cplProperties:areEqualToPropertiesOf:diffTracker:withEqualityBlock:"
- "cplProperties:areEqualToPropertiesOf:withEqualityBlock:"
- "cplQueryCursorDescription"
- "cplQueryCursorSimpleDescription"
- "cplReinflatedErrorForXPC"
- "cplReturnCode"
- "cplSafeErrorForXPC"
- "cplShareParticipantUserIdentifier"
- "cplShortDomainDescription"
- "cplShouldGenerateDerivatives"
- "cplShouldIgnorePropertyForCoding:"
- "cplShouldIgnorePropertyForEquality:"
- "cplSpecialHash"
- "cplSpecialIsEqual:"
- "cplStringByAppendingPathExtension:fallbackExtension:"
- "cplSyncAnchorDescription"
- "cplSyncAnchorSimpleDescription"
- "cplUnderlyingError"
- "cplUnderlyingPOSIXError"
- "cpl_archivedDataWithRootObject:"
- "cpl_redactedShareURL"
- "cpl_safeUnarchiveObjectWithData:class:"
- "cpl_safeUnarchiveObjectWithData:classes:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createGroupForAcceptingLibraryShare"
- "createGroupForAcceptingMomentShare"
- "createGroupForAnalysisDownload"
- "createGroupForBackgroundDownloadsOfResourceType:transferIntent:transport:"
- "createGroupForChangeDownload"
- "createGroupForChangeUpload"
- "createGroupForCleanupLibrary"
- "createGroupForComputeStateDownloadOnDemand"
- "createGroupForComputeStateDownloadPrefetch"
- "createGroupForComputeStateUpload"
- "createGroupForDownloadWithIntent:priority:"
- "createGroupForExitSharedLibrary"
- "createGroupForFeedback"
- "createGroupForFetchScopeListChanges"
- "createGroupForFetchingExistingSharedScope"
- "createGroupForFetchingLibraryShare"
- "createGroupForFetchingMomentShare"
- "createGroupForFixUpTasks"
- "createGroupForInitialDownload"
- "createGroupForInitialUpload"
- "createGroupForKeepOriginalsPrefetch"
- "createGroupForLibraryStateCheck"
- "createGroupForMemoriesPrefetch"
- "createGroupForMovieStreamingWithIntent:"
- "createGroupForNonDerivativePrefetch"
- "createGroupForPrefetch"
- "createGroupForPruningCheck"
- "createGroupForPublishingLibraryShare"
- "createGroupForPublishingMomentShare"
- "createGroupForQueryUserIdentities"
- "createGroupForRecoveryDownload"
- "createGroupForResetSync"
- "createGroupForReshare"
- "createGroupForResourcesDownload"
- "createGroupForSetup"
- "createGroupForSharedLibraryRampCheck"
- "createGroupForStagedScopeCleanup"
- "createGroupForThumbnailPrefetch"
- "createGroupForThumbnailsDownload"
- "createGroupForTransportScopeDelete"
- "createGroupForTransportScopeRefresh"
- "createGroupForTransportScopeUpdate"
- "createGroupForWidgetPrefetch"
- "createGroupForWidgetResourcesDownload"
- "createIncomingDownloadFolderIfNecessaryWithError:"
- "createNewClientCacheIdentifier"
- "createNewLibraryVersion"
- "createNewTempDownloadFolderWithError:"
- "createOwnedLibraryShareScopeWithShare:title:completionHandler:"
- "createRadarButtonTitle"
- "createRadarURL"
- "createScope:completionHandler:"
- "createScopeTaskForScope:completionHandler:"
- "createScopeWithIdentifier:scopeType:flags:transportScope:error:"
- "createSessionContext"
- "createStoragesDynamically:error:"
- "createTempDestinationURLForResource:error:"
- "createTempUploadFolderWithError:"
- "curatedAssetIdentifiersAtIndex:"
- "curatedAssetIdentifiersCount"
- "curatedAssetIdentifiersType"
- "currentActivity"
- "currentBudgetOverrideTimeIntervalExpiryDateStorageKeyForBudget:"
- "currentBudgetOverrideTimeIntervalStorageKeyForBudget:"
- "currentClosingComponentName"
- "currentFeatureVersion"
- "currentHandler"
- "currentPlatform"
- "currentPrediction"
- "currentReasonDescriptions"
- "currentSession"
- "currentSessionInformation"
- "currentState"
- "currentStepDescription"
- "currentSubtask"
- "currentTask"
- "currentThread"
- "currentTracker"
- "currentTransaction"
- "currentUserParticipant"
- "cutoffDate"
- "d16@0:8"
- "d24@0:8@16"
- "d24@0:8Q16"
- "d32@0:8Q16Q24"
- "d32@0:8d16@24"
- "daemonProtocolInterface"
- "dataClassType"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithPropertyList:format:options:error:"
- "dateByAddingTimeInterval:"
- "dateFromString:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "deactivateLibraryWithCompletionHandler:"
- "deactivateScope:error:"
- "deactivateScopeWithIdentifier:completionHandler:"
- "deactivateWithCompletionHandler:"
- "dealloc"
- "decodeArrayOfObjCType:count:at:"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeBytesForKey:returnedLength:"
- "decodeBytesWithReturnedLength:"
- "decodeCMTimeRangeForKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObject"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePointForKey:"
- "decodePropertyList"
- "decodePropertyListForKey:"
- "decodeRectForKey:"
- "decodeSizeForKey:"
- "decodeValuesOfObjCTypes:"
- "defaultAccountEPPCapabilityInUniverseName:"
- "defaultCenter"
- "defaultFlags"
- "defaultMMCSv1FingerprintScheme"
- "defaultManager"
- "defaultOptions"
- "defaultPlatform"
- "defaultTimeZone"
- "defaultWorkspace"
- "deferWithBlock:"
- "delegate"
- "delegateQueue"
- "deleteAllChangeBatchesWithError:"
- "deleteAllChangesWithError:"
- "deleteAllChangesWithScopeFilter:error:"
- "deleteAllRecordsForScopeWithIdentifier:error:"
- "deleteChangeWithScopedIdentifier:discardedUploadIdentifier:error:"
- "deleteCleanupTaskForScopeWithIndex:error:"
- "deleteDateForScope:"
- "deleteDynamicallyCreatedStorages:error:"
- "deleteFileWithIdentifier:error:"
- "deleteFileWithIdentity:error:"
- "deleteFileWithIdentity:includingOriginal:error:"
- "deleteImmediately"
- "deleteIncomingDownloadFolderWithError:"
- "deleteMingledRecordsForScopeWithIdentifier:error:"
- "deleteRecordWithScopedIdentifier:isFinal:error:"
- "deleteRecordsForScopeIndex:discardedFileStorageIdentifiers:maxCount:deletedCount:error:"
- "deleteRecordsForScopeIndex:maxCount:deletedCount:discardedResources:error:"
- "deleteRecordsForScopeIndex:maxCount:deletedCount:discardedUploadIdentifiers:error:"
- "deleteRecordsForScopeIndex:maxCount:deletedCount:error:"
- "deleteRecordsToRevertFromBatch:error:"
- "deleteRecordsToRevertWithLocalScopedIdentifier:error:"
- "deleteResources:checkServerIfNecessary:completionHandler:"
- "deleteResourcesIfSafe:completionHandler:"
- "deleteResourcesToUploadWithUploadIdentifier:error:"
- "deleteScopeWithIdentifier:completionHandler:"
- "deleteScopeWithIdentifier:error:"
- "deleteScopeWithIdentifier:forced:completionHandler:"
- "deleteSharingFlagsWithMaxCount:deletedCount:error:"
- "deleteTempUploadFolderWithError:"
- "deleteTransportScope:scope:completionHandler:"
- "deletedRecordIdentifiers"
- "deletedRecordScopedIdentifiers"
- "deletedScopeIdentifiers"
- "dequeueBatchOfTransferTasksDequeuedSize:"
- "dequeueCloudScopedIdentifiersToCheck:error:"
- "dequeueLastTransportTask"
- "dequeueNextBackgroundDownloadTasksForResourceType:andIntent:maximumSize:maximumCount:error:"
- "dequeueOrder"
- "derivativeGenerationThreshold"
- "derivativeGeneratorClass"
- "derivativeTypes"
- "derivativesCache"
- "descriptionForAcceptanceStatus:"
- "descriptionForAccountEPPCapability:"
- "descriptionForBudget:"
- "descriptionForBudgets:"
- "descriptionForBusyState:"
- "descriptionForChangeType:"
- "descriptionForDirection:"
- "descriptionForExitSource:"
- "descriptionForExitState:"
- "descriptionForExitType:"
- "descriptionForFlags:"
- "descriptionForIntent:"
- "descriptionForIntentPriority:"
- "descriptionForLibraryOptions:"
- "descriptionForPermission:"
- "descriptionForProvideContentResult:"
- "descriptionForResourceType:"
- "descriptionForRole:"
- "descriptionForScopeType:"
- "descriptionForState:"
- "descriptionForSupportedFeatureCompatibleVersion:"
- "descriptionForTargetState:"
- "descriptionForTaskType:"
- "descriptionForTasks"
- "descriptionForTransportScope:"
- "descriptionWithNoScopeIndex"
- "descriptionWithNow:"
- "descriptionWithScopeIdentifier:identifier:"
- "detachObject:withCompletionHandler:"
- "detached"
- "detachedActivity"
- "detachedSyncSessionWithScheduler:configuration:scopeFilter:"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "didDropSomeRecordsForScope:"
- "didEndGeneratingDerivatives"
- "didFinish"
- "didFinishSyncSession"
- "didFinishTask:withError:shouldStop:"
- "didMoveToState:"
- "didProcessStagedScope:"
- "didProgress:userInfo:forState:"
- "didStart"
- "didStartHandler"
- "didUseOverQuotaStrategy"
- "diffBatch"
- "diffHasBeenSuccessful"
- "diffedBatch"
- "diffedBatchCanLowerQuota"
- "differingProperties"
- "disableBoundaryKeyFetching"
- "disableConfigurationFetching"
- "disableFeatureInStore:error:"
- "disableFeedback"
- "disableInitialQueriesForScope:error:"
- "disableInvalidFingerprintScheme"
- "disableMainScopeWithCompletionHandler:"
- "disableMingling"
- "disableOverQuotaRule"
- "disablePrimaryScopeWithError:"
- "disableSleep"
- "disableSynchronizationIfBlockedWithReason:completionHandler:"
- "disableSynchronizationWithReason:"
- "disabledDateForScope:"
- "discardAllRetainedFileURLsWithError:"
- "discardCache"
- "discardChangeWithScopedIdentifier:error:"
- "discardCurrentSession"
- "discardFromStore:error:"
- "discardNotificationForRecordWithScopedIdentifier:error:"
- "discardStagedChangesForScopeWithIdentifier:error:"
- "discardStagedChangesWithScopeFilter:error:"
- "discardStagedSyncAnchorForScope:error:"
- "discardStagedSyncAnchorWithScopeFilter:error:"
- "discardTentativeResetReason:"
- "discardTracker:"
- "discardTransportUserIdentifier"
- "discardUncommittedFileWithIdentifier:error:"
- "discardUncommittedFileWithIdentity:error:"
- "discardedError"
- "diskPressureState"
- "dispatchAsyncWithCurrentSubtask:"
- "dispatchBlockWhenLibraryIsOpen:"
- "dispatchForcedTaskBlock:"
- "dispatchSyncBlock:"
- "displayableDictionaryForDictionary:"
- "displayableNameForEngineLibrary:"
- "displayableNameForLibraryManager:"
- "displayablePropertyListWithRootObject:"
- "distantFuture"
- "distantPast"
- "do:"
- "doRead:"
- "doScopesNeedMetadataSync:"
- "doWrite:error:"
- "doesScopeAllowCourtesyMingling:"
- "doesScopeNeedToBePulledByClient:"
- "doesScopeNeedToPullChangesFromTransport:"
- "doesScopeNeedToPushChangesToTransport:"
- "doesScopeNeedToUpdateTransport:"
- "doesScopeNeedToUploadComputeState:"
- "doesScopeSupportToBePulledByClient:"
- "domain"
- "dontAutoRetry"
- "dontBatchTransactions"
- "doubleForKey:"
- "doubleValue"
- "downloadBatchTaskForSyncAnchor:scope:transportScopeMapping:currentScopeChange:progressHandler:completionHandler:"
- "downloadComputeStatesWithScopedIdentifiers:scope:sharedScope:targetStorageURL:transportScopeMapping:completionHandler:"
- "downloadDidFinishForResourceTransferTask:finalResource:withError:"
- "downloadDidProgress:forResourceTransferTask:"
- "downloadDidStartForResourceTransferTask:"
- "downloadTaskForLocalResource:clientBundleID:options:proposedTaskIdentifier:didStartHandler:progressHandler:completionHandler:"
- "downloadTasks"
- "downloadTransportGroupForScope:"
- "dropChangeWithReason:"
- "dropExpectedDate"
- "dropGeneratingDerivativesIfPossibleWithRecordOnServer:error:"
- "dropPersistedInitialSyncSession"
- "dropResourceChangeWithReason:"
- "dropResourceForUpload:error:"
- "dropSharingChangeWithReason:"
- "dropSharingScopeIdentifier:"
- "dropUnacknowledgedBatch"
- "earlierDate:"
- "earliestReasonDate"
- "effectiveClientBundleIdentifier"
- "effectiveResourceSizeToUploadForUploadIdentifier:"
- "effectiveResourceSizeToUploadUsingStorage:"
- "emergencyClose"
- "empty"
- "enableFeatureInStore:error:"
- "enableMainScopeWithCompletionHandler:"
- "enableMingling"
- "enablePrimaryScopeWithError:"
- "enableSleep"
- "enableSynchronizationWithReason:"
- "encodeArrayOfObjCType:count:at:"
- "encodeBool:forKey:"
- "encodeBycopyObject:"
- "encodeByrefObject:"
- "encodeBytes:length:"
- "encodeBytes:length:forKey:"
- "encodeCMTimeRange:forKey:"
- "encodeConditionalObject:"
- "encodeConditionalObject:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:"
- "encodeObject:forKey:"
- "encodePoint:forKey:"
- "encodePropertyList:"
- "encodeRect:forKey:"
- "encodeRootObject:"
- "encodeSize:forKey:"
- "encodeValuesOfObjCTypes:"
- "encodeWithCoder:"
- "endChangeSessionWithSessionToken:"
- "endClientWork:"
- "endCreatingScopeWithIdentifier:"
- "endKindOfWork:"
- "endPoint"
- "endTrackingWork"
- "endTransaction"
- "endTransactionWithIdentifier:"
- "engineDidOpen:"
- "engineIsClosing"
- "engineLibrary"
- "engineLibrary:didDownloadResourceInBackground:"
- "engineLibrary:didFailBackgroundDownloadOfResource:"
- "engineLibrary:didStartUploadTask:"
- "engineLibrary:getStatusDictionaryWithCompletionHandler:"
- "engineLibrary:getStatusWithCompletionHandler:"
- "engineLibrary:noteClientIsInForeground:"
- "engineLibrary:provideLocalResource:recordClass:completionHandler:"
- "engineLibrary:providePayloadForComputeStates:inFolderWithURL:completionHandler:"
- "engineLibrary:pushAllChangesWithCompletionHandler:"
- "engineLibrary:sizeOfResourcesToUploadDidChangeToSize:sizeOfOriginalResourcesToUpload:numberOfImages:numberOfVideos:numberOfOtherItems:"
- "engineLibrary:uploadTask:didFinishWithError:"
- "engineLibrary:uploadTask:didProgress:"
- "engineLibraryDidCompleteInitialSyncOfMainScope:"
- "engineLibraryHasChangesInPullQueue:"
- "engineLibraryHasStatusChanges:"
- "engineLibraryNeedsInitialDownloadOfMainScope:"
- "engineScope"
- "engineStore"
- "engineWillClose:"
- "enqueueBackgroundDownloadTaskForResource:intent:downloading:error:"
- "enqueueCloudScopedIdentifiersToCheck:error:"
- "enqueuedOrStoredRecordWithLocalScopedIdentifier:"
- "enumerateChangeTypesForChangeType:block:"
- "enumerateConcreteScopesWithBlock:"
- "enumerateDiffWithBlock:"
- "enumerateDropDerivativeRulesWithBlock:"
- "enumerateHistoryWithBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratePushContextsWithBlock:"
- "enumerateRecordsAndReasonsUsingBlock:"
- "enumerateResourceTypesWithBlock:"
- "enumerateScopedTasksWithBlock:"
- "enumerateScopesForTaskInTransaction:"
- "enumerateSystemBudgets:withBlock:"
- "enumerateTargetsWithBlock:"
- "enumerateTasksWithBlock:"
- "enumerateUnknownTargetsWithBlock:"
- "enumerateUpdatedTargetsWithBlock:"
- "enumerateUploadedComputeStateWithBlock:"
- "enumeratorForDeletedStagedScopes"
- "enumeratorForDownloadedResources"
- "enumeratorForScopesIncludeInactive:"
- "enumeratorForScopesNeedingToBePulledByClientWithMaximumCount:"
- "enumeratorForScopesNeedingToPullChangesFromTransport"
- "enumeratorForScopesNeedingToPushChangesToTransport"
- "enumeratorForScopesNeedingToPushHighPriorityChangesToTransport"
- "enumeratorForScopesNeedingToUpdateTransport"
- "enumeratorForScopesNeedingToUploadComputeState"
- "enumeratorForScopesNeedingUpdateFromTransport"
- "enumeratorForScopesWithMingling"
- "ephemeralSessionConfiguration"
- "equalityBlockForDirection:"
- "errorWithDomain:code:userInfo:"
- "errorsForIdentifiers:error:"
- "estimatedBatchSize"
- "estimatedCountOfRemainingRecordsDuringSharedLibraryExit"
- "estimatedRecordSize"
- "estimatedRemainingTime"
- "estimatedResourceSize"
- "estimatedResourceUploadSize"
- "estimatedUploadResourceSize"
- "exceptionWithName:reason:userInfo:"
- "excludeScopeIdentifierFromMingling:"
- "excludeScopeIdentifierFromPushToTransport:"
- "excludedScopeIdentifiers"
- "executePostOpenWithError:"
- "exitRetentionPolicy"
- "exitSource"
- "exitState"
- "exitType"
- "expandHasBeenSuccessful"
- "expandedBatch"
- "expectedDate"
- "expiryDate"
- "extensionForFileUTI:"
- "extractBatch:maximumResourceSize:error:"
- "extractInitialDownloadBatch:shouldConsiderRecordFilter:"
- "extractToBatch:maximumCount:maximumResourceSize:error:"
- "extractionClass"
- "extractionStrategy"
- "f16@0:8"
- "f24@0:8@16"
- "f28@0:8@16f24"
- "faceInstancesAtIndex:"
- "faceInstancesCount"
- "faceInstancesType"
- "failOnPushingChangesTimeout"
- "failedTaskForResource:error:completionHandler:"
- "feature is enabled"
- "featureVersionForSyncAnchor:"
- "featureVersionHistory"
- "featureWithName:"
- "feedbackType"
- "fetchCache"
- "fetchComputeStatesForRecordsWithScopedIdentifiers:validator:onDemand:completionHandler:"
- "fetchComputeStatesForRecordsWithScopedIdentifiers:validator:shouldDecrypt:onDemand:completionHandler:"
- "fetchConfigurationDictionary:"
- "fetchConfigurationDictionary:completionHandler:"
- "fetchExistingSharedLibraryScopeTaskWithCompletionHandler:"
- "fetchExistingSharedLibraryScopeWithCompletionHandler:"
- "fetchMomentShareFromShareURL:completionHandler:"
- "fetchRecordsTaskForRecordsWithScopedIdentifiers:targetMapping:transportScopeMapping:completionHandler:"
- "fetchRules"
- "fetchScopeListChangesForScopeListSyncAnchor:progressHandler:completionHandler:"
- "fetchSharedScopeFromShareURL:completionHandler:"
- "fetchTaskForScopeWithShareURL:completionHandler:"
- "fetchTransportScopeForScope:transportScope:completionHandler:"
- "fileDescriptor"
- "fileEnumerator"
- "fileEnumeratorIncludingPropertiesForKeys:errorHandler:"
- "fileExistsAtPath:"
- "fileHandleForReadingFromURL:error:"
- "fileSizeForComputeStatePayloadFileURL:error:"
- "fileStorage"
- "fileSystemRepresentation"
- "fileUTIForExtension:"
- "fileWatcherFileDidAppear:"
- "fileWatcherFileDidDisappear:"
- "filter"
- "filterForExcludedScopeIdentifiers:"
- "filterForIncludedScopeIdentifiers:"
- "filterOnScopeIdentifier:"
- "filterScopeChangeFromBatch"
- "filteredArrayUsingPredicate:"
- "finalData"
- "finalError"
- "finalResource"
- "finalStatus"
- "finalizeSessionWithCompletionHandler:"
- "finalizeWithCompletionHandler:"
- "findPersistedInitialSyncSession:completionHandler:"
- "fingerPrintForData:error:"
- "fingerPrintForFD:error:"
- "fingerPrintForFileAtURL:error:"
- "fingerprintContext"
- "fingerprintContextIfKnown"
- "fingerprintSchemeDescription"
- "fingerprintSchemeForFingerprint:"
- "fingerprintSchemeForMasterIdentifier:"
- "fingerprintSchemeForNewMasterAsset"
- "fingerprintSchemeForSignature:"
- "fingerprintSchemeForStableHash"
- "fingerprintSchemeWithContext:"
- "finishWithData:error:"
- "firstAvailableCloudScopedIdentifierForProposedCloudScopedIdentifier:"
- "firstIndex"
- "firstMatchInString:options:range:"
- "firstObject"
- "fixUpSparseRecordsTaskWithTasks:transportScopeMapping:completionHandler:"
- "flagsDescriptionMapping"
- "flagsForScope:"
- "floatValue"
- "forBackup"
- "forDisplay"
- "forDownload"
- "forStableHash"
- "forceApplyPendingChangeSessionUpdateWithError:"
- "forceBackupWithActivity:forceClientPush:completionHandler:"
- "forceBackupWithCompletionHandler:"
- "forceInitialDownloadWithActivity:scopeIdentifiers:completionHandler:"
- "forceLoad"
- "forceScopeIndexOnAllRecordsTo:"
- "forceStartSyncSession:withMinimalPhase:"
- "forceSync"
- "forceSyncDelegate"
- "forceSyncDidFinishForTask:withErrors:"
- "forceSyncForScopeIdentifiers:reply:"
- "forceSyncTaskHasBeenCancelled:"
- "forceSyncTaskHasBeenLaunched:"
- "forceSynchronizingScopeWithIdentifiers:completionHandler:"
- "forcedTaskPriority"
- "forcingProcessedStagedScopes"
- "foreground"
- "formatStatusDictionary:forScopeWithIdentifier:appendString:appendTopLevelStatus:appendLineStatus:"
- "freeDiskSpaceSize"
- "full"
- "fullChangeTypeForFullRecord"
- "fullDescriptionForObject:"
- "generateDerivativeResourcesFromInputResource:withAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrameForVideo:completionHandler:"
- "generateDerivativesForChange:derivativesFilter:fingerprintScheme:completionHandler:"
- "generation"
- "generationDuration"
- "getAllResourceTypesToDownload:"
- "getAllResourceTypesToDownloadPrioritizeNonDerivatives:"
- "getBackgroundSchedulingStatusDictionaryWithCompletionHandler:"
- "getBackgroundSchedulingStatusWithCompletionHandler:"
- "getBytes:length:"
- "getBytes:range:"
- "getChangeBatchWithCompletionHandler:"
- "getChangedStatusesWithCompletionHandler:"
- "getCloudCacheForRecordWithScopedIdentifier:completionHandler:"
- "getCloudCacheRecordsWithLocalScopedIdentifiers:desiredProperties:completionHandler:"
- "getCloudIdentifiersForLocalIdentifiers:completionHandler:"
- "getCloudScopedIdentifiersForLocalScopedIdentifiers:completionHandler:"
- "getCommittedRecord:stagedRecord:forScopedIdentifier:"
- "getCurrentRequiredStateWithCompletionHandler:"
- "getCurrentSyncAnchorWithTransportScope:scope:previousScopeChange:completionHandler:"
- "getListOfComponentsWithCompletionHandler:"
- "getLocalIdentifiersForCloudIdentifiers:completionHandler:"
- "getLocalScopedIdentifiersForCloudScopedIdentifiers:completionHandler:"
- "getMappedScopedIdentifiersForScopedIdentifiers:inAreLocalIdentifiers:completionHandler:"
- "getNewGeneration:error:"
- "getProposedStagingScopeIdentifier:stagingTransportScope:forScope:transportScope:transportUserIdentifier:"
- "getRelatedScopedIdentifier:forRecordWithScopedIdentifier:"
- "getResourceValue:forKey:error:"
- "getResourcesForItemWithScopedIdentifier:completionHandler:"
- "getScopeInfoWithTransportScope:scope:previousScopeChange:completionHandler:"
- "getScopeStatusCountsForScopeWithIdentifier:completionHandler:"
- "getStatusArrayForComponents:completionHandler:"
- "getStatusDictionaryWithCompletionHandler:"
- "getStatusForComponents:completionHandler:"
- "getStatusForPendingRecordsSharedToScopeWithIdentifier:maximumCount:completionHandler:"
- "getStatusForRecordsWithIdentifiers:completionHandler:"
- "getStatusForRecordsWithScopedIdentifiers:completionHandler:"
- "getStatusWithCompletionHandler:"
- "getStatusesForScopesWithIdentifiers:includeStorages:completionHandler:"
- "getStoredChangeType:forRecordWithScopedIdentifier:"
- "getStreamingURLForResource:intent:hints:clientBundleID:completionHandler:"
- "getStreamingURLForResource:intent:hints:completionHandler:"
- "getStreamingURLForResource:intent:hints:timeRange:clientBundleID:completionHandler:"
- "getStreamingURLOrMediaMakerDataForResource:intent:hints:timeRange:clientBundleID:completionHandler:"
- "getStreamingURLTaskForResource:intent:hints:timeRange:target:transportScopeMapping:clientBundleID:completionHandler:"
- "getSystemBudgetsWithCompletionHandler is not implemented"
- "getSystemBudgetsWithCompletionHandler:"
- "getTargetsForRecordsWithScopedIdentifiers:completionHandler:"
- "goodConditionsDescription"
- "groupConstructor"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleNextComponent"
- "handleScopeWhenFeatureIsDisabled:scopeType:store:error:"
- "hasAScheduledSyncSession"
- "hasActionData"
- "hasActiveOrQueuedBackgroundDownloadOperations"
- "hasAllowed"
- "hasAnyChangeWithRelatedScopedIdentifier:"
- "hasAnyRecordWithRelatedScopedIdentifier:"
- "hasAssetCountOnServer"
- "hasAssetFlag"
- "hasAssetIdentifier"
- "hasAssetMovieData"
- "hasBatteryBudget"
- "hasBodyCenterX"
- "hasBodyCenterY"
- "hasBodyHeight"
- "hasBodyWidth"
- "hasBrokenScopes"
- "hasCellularBudget"
- "hasCenterX"
- "hasCenterY"
- "hasChangeType:"
- "hasChangeWithScopedIdentifier:"
- "hasChangesInScopeWithIdentifier:"
- "hasChangesWithPriorityGreaterThanPriority:inScopeWithIdentifier:"
- "hasChangesWithPriorityLowerThanPriority:inScopeWithIdentifier:"
- "hasChangesWithRelatedScopedIdentifier:class:"
- "hasChangesWithScopeFilter:"
- "hasCleanupTasks"
- "hasClientRecordWithLocalScopedIdentifier:"
- "hasCloudRecordWithLocalScopedIdentifier:"
- "hasCompleted"
- "hasConcreteScopeForScopeWithIdentifier:"
- "hasContext"
- "hasCrashMarker"
- "hasCropRectString"
- "hasDefaultHEVC"
- "hasDequeueObservers"
- "hasDetectionType"
- "hasDroppedSomeResources"
- "hasEPPAssets"
- "hasEngineRecoveryMechanism"
- "hasEnoughPower"
- "hasEnoughPowerForAutomaticOverride"
- "hasEnqueuedComputeStatesToUpload"
- "hasError"
- "hasFaceState"
- "hasFeature"
- "hasFileWithIdentifier:"
- "hasFileWithIdentity:"
- "hasFinishedAFullSyncForScope:"
- "hasFinishedInitialDownload"
- "hasFinishedInitialDownloadForScope:"
- "hasFinishedInitialSyncForScope:"
- "hasFlagUpdates"
- "hasHeavyResourceUsage"
- "hasIsCurated"
- "hasIsCustomUserAsset"
- "hasIsExtendedCurated"
- "hasIsKeyAsset"
- "hasIsMovieCurated"
- "hasIsRepresentative"
- "hasIsUserCurated"
- "hasKey"
- "hasKeyAssetIdentifier"
- "hasLowBatteryLevel"
- "hasMasterIdentifier"
- "hasMemoryIdentifier"
- "hasMingledRecordsForScopeWithIdentifier:"
- "hasModerateThermalPressure"
- "hasNameSource"
- "hasNumRequested"
- "hasOnlyMingledRecordsWithScopeIdentifier:"
- "hasPendingChangeSessionUpdate"
- "hasPendingIdentifiers"
- "hasPendingResetSync"
- "hasPersonIdentifier"
- "hasPoorNetworkQuality"
- "hasPoorSystemConditions"
- "hasPrefix:"
- "hasPriorityBoostForResourceType:"
- "hasProblematicFormerSharedScope"
- "hasPushChangeTasks"
- "hasQueuedBatches"
- "hasReason"
- "hasReasons"
- "hasRecordAcknowledgedByClientWithScopedIdentifier:"
- "hasRecordWithScopedIdentifier:"
- "hasRecordsToCheckWithScopeIdentifier:"
- "hasRequestedRecordFetch"
- "hasResource"
- "hasResource:"
- "hasRetryAfterMillis"
- "hasScopeFetchedInitialSyncAnchor:"
- "hasScopeFlagsObservers"
- "hasScopesNeedingToPullChangesFromTransport"
- "hasScopesNeedingToPushChangesToTransport"
- "hasScopesNeedingToPushHighPriorityChangesToTransport"
- "hasScopesNeedingToUpdateTransport"
- "hasScopesNeedingToUploadComputeState"
- "hasSize"
- "hasSomeChangeInScopesWithIdentifiers:"
- "hasSomeChangeWithScopeFilter:"
- "hasSomeChangeWithScopedIdentifier:"
- "hasSomeComputeStateWithFileStorageIdentifier:"
- "hasStagedSyncAnchorForScope:"
- "hasStagedSyncAnchors"
- "hasStagingScopes"
- "hasStashedChangesForScopeWithIdentifier:"
- "hasStashedRecordWithScopedIdentifier:"
- "hasStatusChanges"
- "hasStoredChangeSessionUpdate"
- "hasSuffix:"
- "hasTasks"
- "hasThermalPressure"
- "hasType"
- "hasUnacknowledgedChanges"
- "hasUnknownTargets"
- "hasUnmingledChanges"
- "hasUnmingledChangesForScope:"
- "hasUnmingledNonStashedRecordsForScopeWithIdentifier:"
- "hasUnmingledOrStashedRecordsWithScopeFilter:"
- "hasUpdatedTargets"
- "hasValidSystemBudget"
- "hasValidTimeRange"
- "hasValue"
- "hasVersion"
- "hasiCloudAccount"
- "hideNetworkIndicatorForBundleWithIdentifier:"
- "hideSyncIndicator"
- "highPriority"
- "horizontalAccuracy"
- "host"
- "https://at.apple.com/icpl-unsupported-scopes"
- "i16@0:8"
- "i24@0:8@16"
- "iCloud Photo Library"
- "identifier: %@\n\tpath: %@"
- "identityForStorage"
- "identityForStorageName:"
- "identityFromStoredIdentity:"
- "ignoredDate"
- "ignoredRecordCount"
- "ignoredRecordWithScopedIdentifier:"
- "ignoredRecordsBeforeDate:scopeIdentifier:maximumCount:"
- "implementationClassForAbstractClass:"
- "inMemoryDownloadDidFinishForResourceTransferTask:data:withError:"
- "inMemoryDownloadTaskForResource:record:target:transportScopeMapping:clientBundleID:completionHandler:"
- "inMemoryRequest"
- "includeScopeIdentifierInMingling:"
- "includeScopeIdentifierInPushToTransport:"
- "includedScopeIdentifiers"
- "incomingBatch"
- "incomingDownloadFolderURL"
- "incorrectMachineStateErrorWithReason:"
- "incorrectParametersErrorForParameter:"
- "incrementCountForKey:"
- "indexForCloudScopeIdentifier:"
- "indexForLocalScopeIdentifier:"
- "indexGreaterThanIndex:"
- "indexOfObject:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "indexesOfObjectsPassingTest:"
- "init"
- "initEmpty"
- "initFileURLWithPath:isDirectory:"
- "initForLightweightUsageWithLibraryIdentifier:"
- "initForMMCSv2:"
- "initForManagement"
- "initForManagementWithLibraryIdentifier:"
- "initForWrite:store:identifier:description:"
- "initInMainScopeWithIdentifier:"
- "initRelativeToScopedIdentifier:identifier:"
- "initWithAbstractObject:"
- "initWithArchive:rootClass:"
- "initWithArray:"
- "initWithBase64EncodedString:options:"
- "initWithBaseURL:"
- "initWithBatch:name:"
- "initWithBatch:targetMapping:ruleGroups:pushRepositoryPriority:fingerprintContext:provider:"
- "initWithBoundaryKey:"
- "initWithBudget:withReason:queue:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCPLArchiver:"
- "initWithCString:encoding:"
- "initWithCacheURL:"
- "initWithCapacity:"
- "initWithCapacity:maximumPayloadRequestsBatchSize:"
- "initWithCategory:parentMetrics:"
- "initWithCategory:parentReport:"
- "initWithChange:checkItems:"
- "initWithChange:overRecordView:"
- "initWithChangeStorage:overStorageView:"
- "initWithClass:reason:libraryIdentifier:"
- "initWithClientDidAcknowledgeBatchBlock:"
- "initWithClientLibraryBaseURL:"
- "initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:"
- "initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:"
- "initWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:options:"
- "initWithClientLibraryBaseURL:configurationURL:minUpdateInterval:updateIntervalKey:"
- "initWithClientLibraryBaseURL:minUpdateInterval:updateIntervalKey:"
- "initWithClientLibraryBaseURLForCPLEngine:"
- "initWithClientWillAcknowledgeBatchBlock:clientDidAcknowledgeBatchBlock:changePipeDidRemoveChanges:"
- "initWithCloudCache:useFinal:"
- "initWithCoder:"
- "initWithComponents:handler:"
- "initWithConfiguration:refreshIntervalKey:minRefreshInterval:lastUpdateDate:"
- "initWithConfigurationName:refreshIntervalKey:minRefreshInterval:"
- "initWithConfigurationURL:delegate:queue:"
- "initWithContentsOfURL:"
- "initWithContentsOfURL:encoding:error:"
- "initWithContentsOfURL:error:"
- "initWithContentsOfURL:options:error:"
- "initWithContentsOfURL:refreshIntervalKey:minRefreshInterval:error:"
- "initWithCurrentFeatureVersion:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithData:refreshIntervalKey:minRefreshInterval:error:"
- "initWithDate:reason:"
- "initWithDequeueSignalBlock:"
- "initWithDictionary:"
- "initWithDictionaryRepresentation:"
- "initWithDomain:code:userInfo:"
- "initWithEmail:"
- "initWithEngineLibrary:"
- "initWithEngineLibrary:delegate:"
- "initWithEngineLibrary:session:"
- "initWithEngineLibrary:session:clientCacheIdentifier:scope:transportScope:"
- "initWithEngineLibrary:session:clientCacheIdentifier:scope:transportScope:storedTransportGroup:sharedScope:transportScopeMapping:ruleGroup:highPriority:maxBatchSize:pushRepositoryPriority:pushRepository:"
- "initWithEngineScope:engineLibrary:"
- "initWithEngineStore:"
- "initWithEngineStore:name:"
- "initWithEnumerator:"
- "initWithEnumerator:map:"
- "initWithEnumeratorGenerators:"
- "initWithEnumerators:"
- "initWithExcludedScopeIdentifiers:"
- "initWithFileURL:"
- "initWithFileURL:delegate:queue:"
- "initWithFileURL:name:ownerIdentifier:delegate:queue:"
- "initWithFingerprintSchemeV1:fingerprintSchemeV2:"
- "initWithFlags:"
- "initWithFlagsCounts:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithHighPriority:"
- "initWithIDMapping:"
- "initWithIdentifier:"
- "initWithIdentifier:description:keepPower:"
- "initWithIdentity:original:markedForDelete:lastAccessDate:"
- "initWithIncludedScopeIdentifiers:"
- "initWithIncomingBatch:store:error:"
- "initWithIndex:"
- "initWithIndexesInRange:"
- "initWithInfo:libraryIdentifier:"
- "initWithIntent:bypassCaches:priority:"
- "initWithIntent:priority:"
- "initWithIntent:priority:bypassCaches:timeRange:"
- "initWithIntent:priority:timeRange:"
- "initWithItemScopedIdentifier:fileStorageIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:"
- "initWithItemScopedIdentifier:version:fileURL:adjustmentFingerprint:lastUpdatedDate:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithLibraryIdentifier:"
- "initWithLibraryManager:"
- "initWithLocalScopedIdentifier:cloudRecord:idMapping:"
- "initWithMachServiceName:options:"
- "initWithMajorVersion:stage:"
- "initWithMapping:"
- "initWithMergeBlock:"
- "initWithMessage:"
- "initWithName:storage:scopeIdentifier:steps:"
- "initWithName:type:FIFOQueue:maximumBatchSize:maximumConcurrentTransportTasks:coalescingInterval:groupConstructor:"
- "initWithNetworkPath:cellularRestricted:inAirplaneMode:"
- "initWithObject:selector:functionName:"
- "initWithObjects:"
- "initWithObjects:count:"
- "initWithParticipantID:"
- "initWithPattern:options:error:"
- "initWithPhoneNumber:"
- "initWithPlist:"
- "initWithPredictedValuesAndTypes:"
- "initWithPushRepository:"
- "initWithPushSessionTracker:error:"
- "initWithQueue:"
- "initWithReason:scheduler:"
- "initWithRecord:"
- "initWithRecord:generation:"
- "initWithRecord:generation:date:"
- "initWithRecord:ignoredDate:"
- "initWithRecordClass:scopedIdentifier:relatedRecordClass:relatedIdentifier:"
- "initWithRecords:"
- "initWithRescheduler:blocked:syncHasBeenRequested:runtimeCharacteristics:"
- "initWithResetReasons:"
- "initWithResetType:reason:uuid:libraryIdentifier:"
- "initWithResource:taskIdentifier:"
- "initWithResource:taskIdentifier:launchHandler:completionHandler:"
- "initWithResource:taskIdentifier:target:launchHandler:cancelHandler:didStartHandler:progressHandler:completionHandler:"
- "initWithResourceIdentity:itemScopedIdentifier:resourceType:"
- "initWithResources:"
- "initWithRootObject:forDisplay:"
- "initWithRootObject:forDisplay:block:"
- "initWithScopeChange:"
- "initWithScopeIdentifier:identifier:"
- "initWithScopeIdentifier:identifier:scopeIndex:"
- "initWithScopeIdentifier:scopeType:"
- "initWithScopeIdentifier:type:"
- "initWithScopeIdentifiers:"
- "initWithScopeIdentifiers:engineLibrary:filter:delegate:"
- "initWithScopedIdentifier:"
- "initWithScopedIdentifier:otherScopedIdentifier:targetState:"
- "initWithSequenceNumber:expectedDate:scheduler:configuration:scopeFilter:"
- "initWithSerializedString:"
- "initWithSet:"
- "initWithSetting:value:libraryIdentifier:"
- "initWithShareParticipant:"
- "initWithSharedCloudScopedIdentifier:realCloudScopedIdentifier:privateCloudScopedIdentifier:proposedPrivateScopedIdentifier:recordClass:"
- "initWithSourceResource:"
- "initWithSourceResourceType:uti:changeType:droppingDerivativeTypes:"
- "initWithStorage:class:classDescription:scopeIdentifier:maximumCount:"
- "initWithStorage:scopeIdentifier:"
- "initWithStorage:scopeIdentifier:description:class:maximumCount:query:"
- "initWithStorage:scopeIdentifier:maximumCount:"
- "initWithStore:"
- "initWithStore:expandedClientBatch:expandedCloudBatch:"
- "initWithStore:revertedChangesBatch:"
- "initWithStore:scopesChangeBatch:"
- "initWithString:"
- "initWithStringRepresentation:defaultScopeIdentifier:"
- "initWithSuiteName:"
- "initWithSyncManager:syncSession:"
- "initWithSyncManager:syncSession:highPriority:"
- "initWithSyncManager:syncSession:taskClass:"
- "initWithTestMessage:libraryIdentifier:"
- "initWithTimeIntervalSinceReferenceDate:"
- "initWithTitle:statusKey:"
- "initWithTrackingChangeTypeMask:"
- "initWithTransientRepository:"
- "initWithTransientRepository:scope:"
- "initWithTransientRepository:scope:sharedScope:merger:"
- "initWithTranslator:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initWithUTF8String:"
- "initWithUUIDString:"
- "initWithUnblockBlock:"
- "initWithUploadIdentifier:flags:priority:"
- "initWithUserIdentifier:"
- "initWithUserIdentifier:participantID:phoneNumber:email:"
- "initWithWriteTransactionBlocker:schedulerBlocker:"
- "initialDownloadDateForScope:"
- "initialMetadataDownloadDateForScope:"
- "initialMetadataQueriesDateForScope:"
- "initialMingleDateForScope:"
- "initialSyncAnchorForScope:"
- "initialSyncDateForScope:"
- "initialize"
- "insertObject:atIndex:"
- "instancesRespondToSelector:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "intentsToBackgroundDownload"
- "interfaceWithProtocol:"
- "internal"
- "internalRecoveryInstructions"
- "intersectionWithSet:"
- "intersectsWithSet:"
- "invalid flags for additional scope: %@"
- "invalidClientCacheErrorWithReason:"
- "invalidCloudCacheErrorWithReason:"
- "invalidDaemonErrorWithConnectionError:"
- "invalidFingerprintScheme"
- "invalidRecordIdentifiers"
- "invalidRecordScopedIdentifiers"
- "invalidScopeErrorWithScopeIdentifier:"
- "invalidScopeErrorWithScopeIndex:"
- "invalidScopeErrorWithScopedIdentifier:"
- "invalidate"
- "invalidateAndCancel"
- "invoke"
- "involvedProcesses"
- "isActivated"
- "isAdjustedResourceType:"
- "isAfterDate:"
- "isAlive"
- "isAppLibrary"
- "isAsset"
- "isAssetChange"
- "isAvailable"
- "isBackgroundTask"
- "isBeforeDate:"
- "isBlocked"
- "isBlockedByLowPowerMode"
- "isBlockedBySnapshot"
- "isBudgetTypeSupportedForProgressiveOverriding:withReason:"
- "isCPLEncryptionError"
- "isCPLError"
- "isCPLErrorWithCode:"
- "isCPLOperationCancelledError"
- "isCPLOperationDeferredError"
- "isCPLThrottlingError"
- "isCancelled"
- "isCancelledByEngine"
- "isCellular"
- "isCellularRestricted"
- "isClientInForeground"
- "isClientInSyncWithClientCache"
- "isCloudRecordWithScopedIdentifierShared:"
- "isCompatibleWithFingerprintScheme:"
- "isComputeStateTaskUploadEnabled"
- "isComputeStateValid:"
- "isConfirmed"
- "isConnected"
- "isConnectedToNetwork"
- "isConstrained"
- "isConstrainedNetwork"
- "isCurrentUser"
- "isCurrentUserExiting"
- "isDataBudgetOverriden"
- "isDelete"
- "isDerivativeResourceType:"
- "isDetached"
- "isDisabled"
- "isDynamic"
- "isDynamicFingerprint:"
- "isEPPRecord"
- "isEmpty"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToSet:"
- "isEqualToString:"
- "isFIFOQueue"
- "isFavorite"
- "isFeatureDisabled:"
- "isFileURL"
- "isForStableHash"
- "isForeground"
- "isForegroundOperationForIntent:"
- "isForegroundOperationForIntent:priority:"
- "isFull"
- "isFullRecord"
- "isFunctionallyEqual:"
- "isHidden"
- "isHighPriority"
- "isHighPriorityForIntent:"
- "isHighPriorityForIntent:priority:"
- "isInACPLShare"
- "isInAirplaneMode"
- "isInLessThanTimeInterval:"
- "isInMemoryRequest"
- "isInMoreThanTimeInverval:"
- "isInScopeWithIdentifier:"
- "isInternal"
- "isJustInCaseSession"
- "isKeyFace"
- "isKeychainCDPEnabled"
- "isKindOfClass:"
- "isLibraryClosed"
- "isLibraryManagerForEngineLibrary:"
- "isLibraryShare"
- "isMMCSv1Fingerprint:"
- "isMMCSv1Signature:"
- "isMMCSv2"
- "isMMCSv2Fingerprint:"
- "isMMCSv2Signature:"
- "isManual"
- "isMarkedForDelete"
- "isMasterChange"
- "isMemberOfClass:"
- "isMinglingEnabled"
- "isMovieUTI:"
- "isNetworkConnected"
- "isNetworkConstrained"
- "isNewTransportScope:compatibleWithOldTransportScope:"
- "isNonDerivativeResourceType:"
- "isNoneState"
- "isOnCellularOrUnknown"
- "isOriginal"
- "isPetDetectionType"
- "isProxy"
- "isQuarantined"
- "isReadOnly"
- "isRecordWithScopedIdentifierQuarantined:"
- "isRecordWithScopedIdentifierRemapped:"
- "isRecordWithScopedIdentifierStashed:"
- "isRejected"
- "isResetting"
- "isResourceDynamic:"
- "isResourceTypeAGeneratedDerivative:"
- "isScopeChange"
- "isScopeValidInTransaction:"
- "isShared"
- "isSharedInScopeWithIdentifier:"
- "isSparseFullChange"
- "isStableHash:"
- "isStale"
- "isSubclassOfClass:"
- "isSynchronizationDisabledWithReasonError:"
- "isSystemLibrary"
- "isTorsoOnly"
- "isTrackedForUpload"
- "isTransientDerivativeGenerationError:"
- "isTrashedOrDeletedAsset"
- "isUnknown"
- "isUnsupportedOriginalFormatError:"
- "isUpdating"
- "isUpgradeSuggestedToAccessAllPhotos"
- "isUploaded"
- "isUploading"
- "isUserWithIdentifierExiting:"
- "isValid"
- "isValidFingerprint:"
- "isValidMMCSV2Signature:"
- "isValidSignature:"
- "isWaitingForUpdate"
- "isWaitingForUpload"
- "isWalrusEnabled"
- "itemShouldBeReinjectedInPushRepository:"
- "itemWillDropResourceChange:"
- "itemWithScopedIdentifier:"
- "items"
- "itemsToReinject"
- "ivar"
- "ivarAddrForObject:"
- "ivarValueForObject:"
- "keepOriginals"
- "keepUnacknowledgedBatch:"
- "keyAssetScopedIdentifier"
- "keyFace"
- "keysAndValuesAtIndex:"
- "keysAndValuesCount"
- "kickOffSyncSession"
- "knownCloudRecordWithScopedIdentifier:"
- "knowsClientRecordWithScopedIdentifier:"
- "largeResourceSizeThreshold"
- "largestResourceSize"
- "lastAccessDate"
- "lastDateOfClearedPushRepositoryForScope:"
- "lastDateOfCompletedPullFromTransportForScope:"
- "lastError"
- "lastErrorUnlocked"
- "lastObject"
- "lastPathComponent"
- "lastQuarantineCountReportDate"
- "lastScopeChangeUpdateDateForScope:"
- "lastSuccessfulSyncDate"
- "lastUpdateDate"
- "laterDate:"
- "launch"
- "launchHandler"
- "launchNecessaryTasks"
- "launchTask"
- "launchTransportTask:"
- "launchTransportTask:withTransportGroup:"
- "legacyIntent"
- "length"
- "lengthOfBytesUsingEncoding:"
- "libraryClosedError"
- "libraryCreationDate"
- "libraryDoesNotAutoOpenError"
- "libraryIdentifierDescription"
- "libraryInfo"
- "libraryIsCorrupted"
- "libraryManager"
- "libraryManager:backgroundDownloadDidFailForResource:"
- "libraryManager:backgroundDownloadDidFinishForResource:"
- "libraryManager:didFinishForceSyncTask:withErrors:"
- "libraryManager:downloadDidFinishForResourceTransferTask:finalResource:withError:"
- "libraryManager:downloadDidProgress:forResourceTransferTask:"
- "libraryManager:downloadDidStartForResourceTransferTask:"
- "libraryManager:inMemoryDownloadDidFinishForResourceTransferTask:data:withError:"
- "libraryManager:provideLocalResource:recordClass:completionHandler:"
- "libraryManager:providePayloadForComputeStates:inFolderWithURL:completionHandler:"
- "libraryManager:pushAllChangesWithCompletionHandler:"
- "libraryManager:uploadDidFinishForResourceTransferTask:withError:"
- "libraryManager:uploadDidProgress:forResourceTransferTask:"
- "libraryManager:uploadDidStartForResourceTransferTask:"
- "libraryManagerDidChangeConfiguration:"
- "libraryManagerDidStartSynchronization:"
- "libraryManagerDidUpdateSizeOfResourcesToUploadToSize:sizeOfOriginalResourcesToUpload:numberOfImages:numberOfVideos:numberOfOtherItems:"
- "libraryManagerDidUpdateStatusWithProperties:"
- "libraryManagerHasBeenReplaced"
- "libraryManagerHasChangesToPull"
- "libraryManagerHasChangesToPull:"
- "libraryManagerHasStatusChanges"
- "libraryManagerHasStatusChanges:"
- "libraryManagerStatusDidChange:"
- "libraryState"
- "likelyResetDate"
- "likelyResetReasonWithImmediateReason:"
- "localChangeBatchFromCloudBatch:usingMapping:withError:"
- "localComputeStatesToDropAfterClientProvidedPayloadForLocalComputeStates:"
- "localResourceForCloudResource:recordClass:"
- "localResourceOfType:forItemWithCloudScopedIdentifier:"
- "localScopedIdentifier"
- "localScopedIdentifierForCloudScopedIdentifier:isFinal:"
- "localScopedIdentifierForCloudScopedIdentifierIncludeRemappedRecords:"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "lock"
- "longLongValue"
- "lowercaseString"
- "mainBundle"
- "mainScopeSupportsSharingScopeWithIdentifier:"
- "majorVersion"
- "makeChildReportForCategory:"
- "makeObjectsPerformSelector:"
- "makeSiblingReportForCategory:"
- "makeThroughputReporterForCategory:"
- "mapBlock"
- "mapping"
- "mappingExitSources"
- "mappingForExitState"
- "mappingForExitType"
- "mappingForLibraryOptions"
- "mappingForScopeBusyStateDescription"
- "mappingForScopeTypeDescription"
- "mappingRetentionPolicies"
- "markAllPendingIdentifiersForScopeWithIdentifier:asFinalWithError:"
- "markAsCorrupted"
- "markAsSparseFullChange"
- "markAttachedObjectAsInvalid:"
- "markBackgroundDownloadTaskForResourceAsSuceeded:error:"
- "markBackgroundDownloadTaskForResourceAsSuceeded:taskIdentifier:error:"
- "markDatabaseAsDeactivatedWithError:"
- "markForDeleteFileWithIdentity:error:"
- "markInitialQueryIsDoneForRecordsOfClass:forScope:error:"
- "markLibraryManagerAsInvalid"
- "markToOnlyUploadNewResources"
- "markUnmingledChangeWithScopedIdentifierAsMingled:error:"
- "markedForDelete"
- "masterScopedIdentifier"
- "matchesConfigurationDictionary:"
- "maxBatchSize"
- "maxInlineDataSize"
- "maxPixelSizeForResourceType:"
- "maximumAccountEPPCapability"
- "maximumAlbumsPerBatch"
- "maximumBatchSize"
- "maximumComputeStatesToUploadPerBatch"
- "maximumConcurrentTransportTasks"
- "maximumCount"
- "maximumCountOfRecordsInBatches"
- "maximumPayloadRequestsBatchSize"
- "maximumRecordCountPerBatch"
- "maximumResourceDownloadSizeForResourceType:"
- "maximumResourceSizePerBatchForRemainingTime:"
- "maximumSignificantTimeInterval"
- "memoryAtIndex:"
- "memoryType"
- "memorys"
- "memorysCount"
- "mergeConflictsWithError:"
- "mergeFrom:"
- "mergeRecord:isSharedRecord:inPrivateRecord:"
- "mergeRecordChangeWithNewRecordChange:direction:"
- "mergeTargetPersonScopedIdentifier"
- "mergerForBatch:error:"
- "mergingFlags:previousFlags:changeType:"
- "messagesAtIndex:"
- "messagesCount"
- "messagesForPlistRepresentation:"
- "metrics"
- "metricsDescription"
- "metricsIdentifier"
- "mightDropSomeDerivativesForSourceType:forChangeType:"
- "minRefreshInterval"
- "minUpdateInterval"
- "mingleChangeBatch:scope:forStore:onPutBatchInPullQueue:error:"
- "mingleRemappedBatch:scope:forStore:onPutBatchInPullQueue:error:"
- "mingleSharedRemappedBatch:scope:sharedScope:forStore:fixUpTasks:onPutBatchInPullQueue:error:"
- "minglingStrategyWithStorage:coveringScopeIdentifier:maximumBatchSize:"
- "minimumPriorityForChangesInScopeWithIdentifier:"
- "minimumPriorityForLocalConflictResolution"
- "minimumRecordCountPerBatch"
- "minusSet:"
- "missingError"
- "mmcsv1FingerprintScheme"
- "mmcsv2FingerprintScheme"
- "mode"
- "momentShareParticipantsFromParticipants:"
- "mostCurrentChangesSyncAnchorForScope:"
- "moveItemAtURL:toURL:error:"
- "moveTasksToBackground"
- "mutableCopy"
- "nameComponents"
- "needsToAcquireRescheduler"
- "needsToGenerateDerivatives"
- "needsToSetScopeIdentifier"
- "networkPath"
- "networkState"
- "new"
- "newChangeWithScopedIdentifier:changeType:"
- "newChangeWithType:"
- "newClientCacheViewUsesPushRepository:"
- "newDeleteChangeWithScopedIdentifier:"
- "newDeleteScopeChangeWithScopeIdentifier:type:"
- "newEmptyPushContext"
- "newPlatformImplementationForObject:"
- "newPushContextForChange:overStoredRecord:initialUpload:"
- "newRecord"
- "newRecordInScopeWithIdentifier:"
- "newRecordWithScopedIdentifier:"
- "newScopeChangeInferClassWithScopeIdentifier:type:"
- "newScopeChangeWithAutomaticScopeIdentifierForScopeType:"
- "newScopeChangeWithScopeIdentifier:type:"
- "newScopedTaskWithScope:session:transportScope:clientCacheIdentifier:"
- "newTask"
- "newTaskIdentifier"
- "newTransactionWithIdentifier:description:keepPower:"
- "nextBatch"
- "nextBatchOfRecordsToCheckWithScopeIdentifier:"
- "nextBatchOfRecordsToRevert"
- "nextBatchOfRemappedRecordsInScope:maximumCount:"
- "nextCleanupTaskScopeIndexOfType:"
- "nextObject"
- "nextOverrideTimeIntervalForSystemBudgets:"
- "nextTimeIntervalForOverridingBudget:withReason:"
- "nextTimeIntervalToUseGivenCurrent:expiryDate:"
- "nonPrivateFingerprintScheme"
- "noneState"
- "normalizeBoundaryKey:"
- "normalizedExpungeableResourceStatesFromExpungeableResourceStates:"
- "normalizedResourcesFromResources:resourcePerResourceType:"
- "notImplementedError"
- "noteActiveQueuesStatusAtEnqueingTime:"
- "noteBlockedStateHasChanged:"
- "noteClientIsBeginningSignificantWork"
- "noteClientIsEndingSignificantWork"
- "noteClientIsInBackground"
- "noteClientIsInForeground"
- "noteClientIsInForegroundQuietly:"
- "noteClientIsInSyncWithClientCache"
- "noteClientIsNotInSyncWithClientCache"
- "noteClientNeedsToPull"
- "noteClientNeedsToPullIfNecessary"
- "noteClientReceivedNotificationOfServerChanges"
- "noteComputeStateDownloadRequest"
- "noteContainerHasBeenWiped"
- "noteDidCheckAssetWithServerWhenOverQuotaForScope:error:"
- "noteInvalidRecordScopedIdentifiersInPushSession:"
- "noteMainScopeHasBeenActivated"
- "noteNetworkStateDidChange"
- "noteObjectAreTotallyDifferent"
- "noteObjectsDifferOnProperty:"
- "noteOtherResetEvent:cause:"
- "notePruningRequestForResource:realPrune:successful:"
- "notePruningRequestForResource:realPrune:successful:prunedSize:"
- "notePushRepositoryStoredSomeChanges"
- "noteQuotaHasChanged"
- "noteRequestForResource:successful:prunedSize:"
- "noteResetSyncFinished"
- "noteResourceDownloadQueueIsFull"
- "noteScopeListNeedsUpdate"
- "noteScopeNeedsToPullFromTransport"
- "noteScopeNeedsToPushHighPriorityToTransport"
- "noteScopeNeedsToPushToTransport"
- "noteScopeNeedsToPushToTransportWithChangeTypes:"
- "noteScopeNeedsToUploadComputeState"
- "noteScopeNeedsUpdate"
- "noteServerHasChanges"
- "noteServerIsUnavailableWithError:"
- "noteServerMightBeAvailableNow"
- "noteStateDidProgress:"
- "noteStoreNeedsCleanup"
- "noteStoreNeedsSetup"
- "noteStoreNeedsToUpdateDisabledFeatures"
- "noteSyncSession:failedDuringPhase:withError:"
- "noteSyncSession:failedWithError:"
- "noteSyncSession:stateWillBeAttempted:"
- "noteSyncSessionInformation:"
- "noteSyncSessionInformation:arguments:"
- "noteSyncSessionMovedToState:"
- "noteSyncSessionSucceeded:"
- "noteTaskHasBeenPreempted"
- "noteTransportNeedsUpdate"
- "notifyAttachedObjectsHasStatusChanges"
- "notifyAttachedObjectsPullQueueIsFull"
- "notifyAttachedObjectsResourceDidDownloadInBackground:"
- "notifyAttachedObjectsResourceDidFailBackgroundDownloadOfResource:"
- "notifyAttachedObjectsSizeOfResourcesToUploadDidChangeToSize:sizeOfOriginalResourcesToUpload:numberOfImages:numberOfVideos:numberOfOtherItems:"
- "notifyAttachedObjectsThatPushRepositoryFlagsCountsHaveChanged"
- "notifyAttachedObjectsUploadTask:didFinishWithError:"
- "notifyAttachedObjectsUploadTask:didProgress:"
- "notifyAttachedObjectsUploadTaskDidStart:"
- "notifyClientDidAcknowledgeBatch:"
- "notifyClientOfStatusChangesIfNecessaryWithError:"
- "notifyClientOfStore:ofStatusChanges:error:"
- "notifyClientWillAcknowledgeBatch:"
- "notifyStatusForRecordHasChanged:persist:error:"
- "notifyStatusForRecordViewHasChanged:persist:error:"
- "notifyStatusForRecordWithScopedIdentifierHasChanged:recordClass:persist:error:"
- "null"
- "numberOfImagesToUpload"
- "numberOfOtherItemsToUpload"
- "numberOfVideosToUpload"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAreTotallyDifferent"
- "objectsForKeys:notFoundMarker:"
- "observeAsyncCallOn:selector:block:"
- "observeAsyncCallWithFunction:block:"
- "observeSyncCallOn:selector:block:"
- "observeSyncCallWithFunction:block:"
- "observeValueForKeyPath:ofObject:change:context:"
- "onlyAddedResources"
- "openLibraryWithClientLibraryBaseURL:cloudLibraryStateStorageURL:cloudLibraryResourceStorageURL:libraryIdentifier:mainScopeIdentifier:options:completionHandler:"
- "openURL:configuration:completionHandler:"
- "openWithCompletionHandler:"
- "openWithError:"
- "openWithFileRecoveryHandler:error:"
- "openWithRecoveryHandler:error:"
- "operationCancelledError"
- "optionsForLegacyIntent:"
- "optionsFromDescription:"
- "orPredicateWithSubpredicates:"
- "orderedClassesForChanges"
- "orderedClassesForChangesForLargeSync"
- "orderedClassesForDelete"
- "original"
- "originalBatch"
- "originalResourceSize"
- "originatingScopeIdentifier"
- "otherScopedIdentifier"
- "overQuotaStrategyWithStorage:coveringScopeIdentifier:"
- "ownerIdentifier"
- "ownerIsCurrentUser"
- "ownerNameForEngineLibrary:"
- "parentScopedIdentifier"
- "participantID"
- "pathComponents"
- "pathExtension"
- "pendingRecordChangeForClientCacheWithLocalScopedIdentifier:"
- "performAsCurrentWithPendingUnitCount:usingBlock:"
- "performBarrier"
- "performBarrierTransaction:withBlock:"
- "performBatchedWriteTransactionBarrier"
- "performBatchedWriteTransactionBarrierWithCompletionBlock:"
- "performBatchedWriteTransactionWithBlock:completionHandler:"
- "performBlockOnLibrary:"
- "performMaintenanceCleanupWithCompletionHandler:"
- "performMaintenanceWithError:"
- "performPostUpgradeMigrationsWithError:"
- "performReadTransaction:withBlock:"
- "performReadTransactionWithBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUpgradeWithError:"
- "performWriteTransaction:withBlock:completionHandler:"
- "performWriteTransactionByPassBlocker:withBlock:completionHandler:"
- "performWriteTransactionWithBlock:completionHandler:"
- "permission"
- "personAtIndex:"
- "personScopedIdentifier"
- "personsCount"
- "petFaceInstancesAtIndex:"
- "petFaceInstancesCount"
- "petFaceInstancesType"
- "phaseDescription"
- "phaseDescriptionLastChangeDate:"
- "phoneNumber"
- "photosCount"
- "placeholderRecord"
- "platformImplementationProtocol"
- "platformObject"
- "plistArchiveWithCPLArchiver:"
- "plistDescription"
- "plistRepresentationForMessages:"
- "pointerDescription"
- "popChangeBatch:error:"
- "popChangeBatchOfRemappedRecords:scope:maximumCount:error:"
- "popCloudScopedIdentifiersToCheck:otherScopeIndex:maxCount:deletedCount:error:"
- "popNextBatchOfLocalComputeStatesNeedingPayload"
- "popNextBatchWithError:"
- "popSessionInformation"
- "posixErrorForURL:"
- "posixErrorForURL:errorCode:"
- "postNotificationName:object:"
- "powerAssertionStatus"
- "powerStatus"
- "powerStatusPlist"
- "predicateMatchingDynamicFingerprintForKey:"
- "predicateWithBlock:"
- "predicateWithFormat:"
- "predictSyncSessionValue:ofType:"
- "predictedDateForType:"
- "predictedValueForType:"
- "predictor"
- "predictor:changedPrediction:"
- "preferredFilenameExtension"
- "prepareAndLaunchSyncTask:"
- "prepareAndLaunchSyncTaskUnlocked:"
- "prepareBatchBeforeUploadWithError:"
- "prepareForClose"
- "prepareForStorage"
- "prepareWithError:"
- "prettyDescriptionWithAnchorDesciptionBlock:"
- "preventDelegateWithDelegationClass:selector:"
- "preventWipeErrorWithReason:preventedByUser:"
- "previewData"
- "previewImageDataAtIndex:"
- "previewImageDataType"
- "previewImageDatas"
- "previewImageDatasCount"
- "primaryScope"
- "privateCloudScopedIdentifier"
- "problematicFormerSharedScopeIdentifier"
- "processInfo"
- "processName"
- "processesInvolvedInSyncSessions"
- "progressForTask:progress:"
- "progressHandler"
- "progressWithTotalUnitCount:"
- "promisedAssetCount"
- "promisedPhotosCount"
- "promisedVideosCount"
- "propertiesDescription"
- "propertiesForChangeType:"
- "propertyClasses"
- "propertyGetter"
- "propertyGetterIMP"
- "propertyListWithData:options:format:error:"
- "propertyMapping"
- "propertySetter"
- "propertySetterIMP"
- "propertyType"
- "proposedCloudScopedIdentifier"
- "proposedLocalScopedIdentifier"
- "proposedPrivateScopedIdentifier"
- "proposedRescheduleDate"
- "proposedScopedIdentifierForItemScopedIdentifier:"
- "provideCloudResource:completionHandler:"
- "provideLocalResource:recordClassString:completionHandler:"
- "providePayloadForComputeStates:inFolderWithURL:completionHandler:"
- "provideRecordWithCloudScopeIdentifier:completionHandler:"
- "provideScopeChangeForScopeWithIdentifier:completionHandler:"
- "provider"
- "providesEnhancedPrivacy"
- "proxyLibraryManager"
- "proxyWithErrorHandler:"
- "publicPermission"
- "publishMomentShare:completionHandler:"
- "publishResource:completionHandler:"
- "pullFromTransportTaskForScope:"
- "pushAllChangesWithCompletionHandler:"
- "pushChangeTasks"
- "pushContextAddingUploadIdentifier"
- "pushContextMergingFlags:changeType:uploadIdentifier:priority:"
- "pushContextsFromStoredUploadIdentifiers:"
- "pushContextsFromStoredUploadIdentifiersInCoder:key:"
- "pushPullGatekeepers"
- "pushRepositoryIsFull"
- "pushRepositoryPriority"
- "pushToTransportTaskForScope:"
- "q16@0:8"
- "q24@0:8@\"<CPLReference>\"16"
- "q24@0:8@16"
- "q24@0:8q16"
- "q32@0:8@16@24"
- "q40@0:8q16q24Q32"
- "qualityOfServiceForForcedTasks"
- "qualityOfServiceForSyncSessions"
- "quarantineRetryCount"
- "quarantined"
- "queryDescription"
- "queryItemWithName:value:"
- "queryTaskForCursor:class:scope:transportScopeMapping:progressHandler:completionHandler:"
- "queryUserDetailsForShareParticipants:completionHandler:"
- "queryUserDetailsTaskForParticipants:completionHandler:"
- "queryUserIdentitiesWithParticipants:completionHandler:"
- "queue"
- "queuedDate"
- "r*32@0:8@16^Q24"
- "radarDescription"
- "radarTitle"
- "rampingRequestForResourceType:numRequested:completionHandler:"
- "rampingRequestTaskForResourceType:numRequested:completionHandler:"
- "rangeAtIndex:"
- "rangeOfString:"
- "rangeOfString:options:range:"
- "readFrom:"
- "readMoreButtonTitle"
- "readMoreURL"
- "readOnly"
- "readOnlyError"
- "realCloudScopedIdentifier"
- "realRecordChangeFromRecordChange:direction:newRecord:"
- "realRecordChangeFromRecordChange:direction:newRecord:changeType:diffTracker:"
- "realRecordChangeFromRecordChange:direction:newRecord:diffTracker:"
- "realResourceSize"
- "realScopedIdentifier"
- "realScopedIdentifierForRemappedScopedIdentifier:"
- "realStableHash"
- "realUploadResourceSize"
- "reallyCancel"
- "reallyLaunch"
- "reallyUpdatedResources"
- "reasonAsString:"
- "reasonDescriptionWithNow:"
- "record"
- "recordAcknowledgedByClientWithScopedIdentifier:"
- "recordClass"
- "recordComputeStateDelegate"
- "recordForStatusWithScopedIdentifier:"
- "recordFromTransportWithScopedIdentifier:"
- "recordViewForStatusWithScopedIdentifier:"
- "recordViewWithScopedIdentifier:"
- "recordViewsWithRelatedScopedIdentifier:class:"
- "recordWithScopedIdentifier:"
- "recordWithScopedIdentifier:isConfirmed:isStaged:"
- "recordWithScopedIdentifier:isFinal:"
- "recordWithScopedIdentifier:isFinal:isConfirmed:"
- "recordWithStatusChangesToNotify"
- "recordsAcknowledgedByClientWithRelatedScopedIdentifier:class:"
- "recordsNeedingGeneratedDerivatives"
- "recordsOfClass:isFinal:"
- "recordsToFetch"
- "recordsWithRelatedScopedIdentifier:class:isFinal:"
- "recordsWithRelatedScopedIdentifier:isFinal:"
- "recoverButtonTitle"
- "recoverUsingEngineWithCompletionHandler:"
- "redactedDescription"
- "reenqueueBackgroundDownloadTaskForResource:bumpRetryCount:didDiscard:error:"
- "reenqueueBackgroundDownloadTaskForResource:taskIdentifier:bumpRetryCount:didDiscard:error:"
- "refetchFromDisk"
- "refresh"
- "refreshBoundaryKeyWithSource:completionHandler:"
- "refreshInterval"
- "refreshIntervalKey"
- "refreshScopeWithIdentifier:completionHandler:"
- "registerLikelyResetReason:"
- "registerLikelyResetReason:arguments:"
- "registerStorage:"
- "registerTentativeResetReasonIfCrashing:"
- "reinjectChange:dequeueOrder:discardedUploadIdentifier:overwrittenRecord:error:"
- "reinjectChange:dequeueOrder:overwrittenRecord:error:"
- "reinjectChange:priority:error:"
- "reinjectChangeWithReason:"
- "reinjectExtractedBatch:overwrittenRecordIdentifiers:error:"
- "rejectChangeWithReason:error:"
- "rejectedDescriptions"
- "rejectedPersonIdentifiersAtIndex:"
- "rejectedPersonIdentifiersCount"
- "rejectedPersonIdentifiersType"
- "rejectsTheSameRecordsAs:"
- "relatedIdentifier"
- "relatedRecordClass"
- "relatedRelationshipIsWeak"
- "relatedScopedIdentifier"
- "relatedScopedIdentifierForRecordWithScopedIdentifier:"
- "relatedScopedIdentifierForRecordWithScopedIdentifier:isFinal:"
- "relationToContainerWithIdentifier:"
- "relationWithItemScopedIdentifier:containerIdentifier:"
- "release"
- "releaseFileURL:error:"
- "releaseFileURL:forComputeState:error:"
- "releaseFileURL:forResource:error:"
- "releaseIdentity:lastReference:isTrackedOriginal:error:"
- "remainingClassesForInitialQueryForScope:"
- "remapAllRecordsWithPreviousScopedIdentifier:newScopedIdentifier:error:"
- "remappedDeletes"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllBackgroundDownloadTasksForItemWithScopedIdentifier:error:"
- "removeAllObjects"
- "removeAllTransferTasks"
- "removeBackgroundDownloadTaskForResource:error:"
- "removeBackgroundDownloadTaskForResource:taskIdentifier:error:"
- "removeBrokenScope:"
- "removeCachedResourceValueForKey:"
- "removeChange:error:"
- "removeComputeState:error:"
- "removeComputeStateWithLocalScopedIdentifier:version:adjustmentFingerprint:discardedFileStorageIdentifier:error:"
- "removeComputeStateWithLocalScopedIdentifier:version:adjustmentFingerprint:error:"
- "removeDeferHandler:"
- "removeDequeueObserver:"
- "removeIndex:"
- "removeItemAtURL:error:"
- "removeLastObject"
- "removeMappingForCloudScopedIdentifier:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObjectsForKeys:"
- "removeObjectsInArray:"
- "removeObjectsInRange:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "removeObserver:name:object:"
- "removeParticipantInSharedLibraryTaskFromSharedScope:transportScope:share:retentionPolicy:exitSource:userIdentifiersToRemove:participantIDsToRemove:completionHandler:"
- "removeParticipants:fromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:"
- "removePendingParticipantIDs:"
- "removePredictedValueForType:"
- "removePushObserverWithIdentifier:"
- "removeQuarantinedRecordWithScopedIdentifier:notify:error:"
- "removeQuarantinedRecordWithScopedIdentifier:removed:error:"
- "removeRecordWithScopedIdentifier:"
- "removeRecordWithScopedIdentifier:error:"
- "removeRejectedRecordsWithScopedIdentifiers:"
- "removeRelatedRecordsFromQuarantineWithError:"
- "removeRemappedRecordWithScopedIdentifier:error:"
- "removeResourceType:"
- "removeScopeFlagsObserverWithIdentifier:"
- "removeTransferTask:"
- "removeTransportTask:"
- "replaceObjectAtIndex:withObject:"
- "replaceOccurrencesOfString:withString:options:range:"
- "replacementObjectForCoder:"
- "replacementObjectForXPCConnection:encoder:object:"
- "reportEndOfResetWithUUID:reason:"
- "reportFetchChangesRewindToFeatureVersion:"
- "reportLibraryCorrupted"
- "reportMessage:"
- "reportMessages:"
- "reportMiscInformation:"
- "reportQuarantineCountIfNecessary"
- "reportRadar:"
- "reportResetType:reason:uuid:"
- "reportSetting:hasBeenEnabled:"
- "reportSetting:hasBeenSetToValue:"
- "reportThroughputWorkForMetrics:itemCount:done:"
- "reportUnsuccessfulSync"
- "requestAtIndex:"
- "requestAttachedLibrary"
- "requestClientToPullAllChangesInScopeIdentifiers:completionHandler:"
- "requestClientToPullAllChangesWithScopeIdentifiers:completionHandler:"
- "requestClientToPushAllChangesWithCompletionHandler:"
- "requestDisabledFeaturesUpdate"
- "requestFetchForRule:error:"
- "requestFetchOfRecordWithScopedIdentifier:forItem:rule:error:"
- "requestFetchOfRecordWithScopedIdentifier:forRule:error:"
- "requestPayloadForLocalComputeState:cloudComputeState:"
- "requestScopesWithIdentifiersToBeActivated:completionHandler:"
- "requestSyncStateAtEndOfSyncSession:reschedule:"
- "requestSyncStateAtEndOfSyncSession:reschedule:proposedRescheduleDate:"
- "requestType"
- "requestWithURL:"
- "requestsCount"
- "requiredStateAtEndOfSyncSession"
- "requiredStateObserverBlock"
- "requiresStableHashForResourceType:"
- "rescheduler"
- "resetAllFinalCloudIdentifiersForScopeWithIdentifier:error:"
- "resetAllTransientStatuses"
- "resetBackoffInterval"
- "resetCacheWithOption:completionHandler:"
- "resetCacheWithOption:reason:completionHandler:"
- "resetCloudRecordsForScopeWithIdentifier:error:"
- "resetCompleteSyncStateForScope:error:"
- "resetCompleteSyncStateIncludingIDMappingForScope:error:"
- "resetCompleteSyncStateIncludingIDMappingWithCause:error:"
- "resetCompleteSyncStateWithCause:error:"
- "resetConditionallyFromNewIncomingChange:"
- "resetDequeuedBackgroundDownloadTasksWithError:"
- "resetDidCheckAssetWithServerWhenOverQuotaForScope:error:"
- "resetDisabledOverQuotaRule"
- "resetHeuristics"
- "resetInitialSyncAnchorForScope:error:"
- "resetLocalRecordsForScopeWithIdentifier:error:"
- "resetLocalSyncStateForScope:error:"
- "resetLocalSyncStateWithCause:date:error:"
- "resetLocalSyncStateWithCause:error:"
- "resetMetrics"
- "resetMingledRecordsWithScopeFilter:error:"
- "resetNoteClientNeedsToPull"
- "resetPriorityForScopeWithIdentifier:maxCount:hasMore:error:"
- "resetReasons"
- "resetRejectedRecordsWithError:"
- "resetStableRecordsForScopeWithIdentifier:error:"
- "resetStatus"
- "resetSyncAnchorForScope:error:"
- "resetSyncAnchorWithCause:error:"
- "resetSyncStateForScope:error:"
- "resetTransientRepositoryForScopeWithIdentifier:error:"
- "resetTransientStatusesWithScopeIdentifier:"
- "resetTransportUserIdentifier"
- "resetWithError:"
- "resetting"
- "reshareRecordsTaskWithRecords:sourceScope:destinationScope:transportScopeMapping:completionHandler:"
- "resignCurrent"
- "resolveLocalScopedIdentifiersForCloudScopedIdentifiers:completionHandler:"
- "resourceChangeWillOnlyChangeDerivatives:"
- "resourceCheckTaskForResources:targetMapping:transportScopeMapping:completionHandler:"
- "resourceForType:"
- "resourceIdentitiesForRecordWithLocalScopedIdentifier:"
- "resourceOfType:forRecordWithScopedIdentifier:record:error:"
- "resourceOfType:forRecordWithScopedIdentifier:record:target:error:"
- "resourceOfType:forRecordWithScopedIdentifier:recordClass:error:"
- "resourcePerType"
- "resourceProgressDelegate"
- "resourceScopedIdentifier"
- "resourceSize"
- "resourceStorage"
- "resourceTypeFromShortDescription:"
- "resourceTypeSupportsResourceExpunge:"
- "resourceTypeTrackedForUpload:"
- "resourceTypesThatCountAgainstiCloudQuota"
- "resourceTypesToUploadForChange:"
- "resourceTypesToUploadForUploadIdentifier:"
- "resourcesDescription"
- "resourcesDownloadTaskWithCompletionHandler:"
- "resourcesToUpload"
- "resourcesToUploadForUploadIdentifier:"
- "respondsToSelector:"
- "responseAtIndex:"
- "responseType"
- "responses"
- "responsesCount"
- "restoreRelationshipsFromFullRecord:"
- "resume"
- "retain"
- "retainCount"
- "retainCountForIdentity:"
- "retainFileURLForComputeState:error:"
- "retainFileURLForIdentifier:error:"
- "retainFileURLForIdentity:resourceType:error:"
- "retainFileURLForResource:error:"
- "retainIdentity:isTrackedOriginal:error:"
- "reverseObjectEnumerator"
- "revertedChanges"
- "revertedChangesBatch"
- "revertedPlaceholderRecordsEnumerator"
- "rewindAnchorsPerSharingScopes"
- "rewindSyncAnchorsForScope:"
- "rootObject"
- "ruleGroup"
- "ruleGroups"
- "runWithNoSyncSession"
- "runWithinSyncSession:"
- "runtimeCharacteristics"
- "s16@0:8"
- "safeFilename"
- "scheduleEndFromPersistedOverride"
- "scheduleEndOfOverride"
- "scheduleForcedTaskForLaunch:"
- "scheduleNextSyncSessionAtDate:"
- "schedulePersistedSyncSessionIfAvailableWithCompletionHandler:"
- "scheduledOverrideDidEnd:"
- "schedulerBlocker"
- "schedulerShouldStartSyncSessionMovingToForeground:currentSession:"
- "scheme"
- "scopeChangeClassForType:"
- "scopeChangeForScope:"
- "scopeChangesNeedingToBePulledByClientWithMaximumCount:"
- "scopeFilter"
- "scopeFilterInTransaction:"
- "scopeForScopeIdentifier:"
- "scopeForSharingScope:"
- "scopeIdentifier:hasIgnoredRecordsBeforeDate:"
- "scopeIdentifierForCloudScopeIndex:"
- "scopeIdentifierForLocalScopeIndex:"
- "scopeIdentifierToAutomaticallyExcludeFromMingling"
- "scopeIdentifiers"
- "scopeIdentifiersExcludedFromMingling"
- "scopeIdentifiersExcludedFromPushToTransport"
- "scopeIdentifiersForQuarantine"
- "scopeIndexes"
- "scopeListSyncAnchor"
- "scopeNameForTransportScope:"
- "scopeStorage:didDropSharingScopeIdentifier:"
- "scopeStorage:didStoreSharingScopeIdentifier:"
- "scopeStorage:didUpdateScopeChange:forScope:"
- "scopeTypeDescriptionForScopeType:"
- "scopeUpdateTaskDidFinishSuccessfully:"
- "scopeWithCloudIndex:"
- "scopeWithCloudScopeIndex:"
- "scopeWithIdentifier:"
- "scopeWithLocalIndex:"
- "scopeWithLocalScopeIndex:"
- "scopeWithStableIndex:"
- "scopeWithTypeHasQuota:"
- "scopedIdentifierAddingScopeIndexForScopedIdentifier:"
- "scopedIdentifierForCloudScopedIdentifier:"
- "scopedIdentifierForLocalScopedIdentifier:"
- "scopedIdentifierWithString:includeScopeIndex:"
- "scopedIdentifierWithString:includeScopeIndex:defaultScopeIdentifier:"
- "scopedIdentifiersForChangesWithFlag:forScopeWithIdentifier:"
- "scopedIdentifiersForMapping"
- "scopedIdentifiersFromArrayOfUnknownIdentifiers:"
- "scopedIdentifiersFromDictionaryOfUnknownIdentifiers:"
- "scopedIdentifiersFromSetOfUnknownIdentifiers:"
- "scopedIdentifiersRemappedToScopedIdentifier:"
- "scopesChangeBatch"
- "scopesForTask"
- "secondaryIdentifier"
- "secondaryRelationshipIsWeak"
- "secondaryScopedIdentifier"
- "selector"
- "self"
- "sendFeedbackTaskForMessages:completionHandler:"
- "sendFeedbackToServerIfNecessary"
- "separatorForStatusKey:"
- "sequenceNumber"
- "serializedString"
- "serverMessage"
- "serverSupportsAssetSortOrder"
- "serverSupportsComputeState"
- "serverSupportsDeletedByUserIdentifier"
- "serverSupportsDetectionType"
- "serverSupportsGraphPeopleHome"
- "serverSupportsLastViewedDate"
- "serverSupportsLibraryShareSettingsRecordSyncing"
- "serverSupportsLibraryShareSettingsUserViewedParticipantTrashNotificationDateSyncing"
- "serverSupportsMergeTargetRef"
- "serverSupportsSharedLibrarySharingState"
- "serverSupportsVision"
- "session"
- "sessionHasBeenDeferredError"
- "sessionIdentifier"
- "sessionIsDone"
- "sessionProgress"
- "sessionWillStart"
- "sessionWithConfiguration:"
- "sessionWontHappen"
- "setAcceptanceStatus:"
- "setAccessibilityDescription:"
- "setAccountEPPCapability:"
- "setAccountFlagsData:"
- "setActionData:"
- "setActivated:"
- "setActivationDate:"
- "setAddedDate:"
- "setAdjustedMediaMetaData:"
- "setAdjustedMediaMetaDataType:"
- "setAdjustmentCompoundVersion:"
- "setAdjustmentCreatorCode:"
- "setAdjustmentData:"
- "setAdjustmentRenderTypes:"
- "setAdjustmentSourceType:"
- "setAdjustmentTimestamp:"
- "setAdjustmentType:"
- "setAdjustments:"
- "setAlbumSortAscending:"
- "setAlbumSortType:"
- "setAlbumType:"
- "setAllScopesHasChangesToPullFromTransportWithError:"
- "setAllowed:"
- "setAllowsAssetsWithResourcesButNoAdjustments:"
- "setAllowsFetchCache:"
- "setAllowsLocalConflictResolutionWhenOverQuota:"
- "setArchiveCursor:"
- "setAssetCount:"
- "setAssetCounts:"
- "setAssetDate:"
- "setAssetFlag:"
- "setAssetHDRType:"
- "setAssetIdentifier:"
- "setAssetList:"
- "setAssetListPredicate:"
- "setAssetMovieData:"
- "setAssetScopedIdentifier:"
- "setAssetSortOrder:"
- "setAssetSubtype:"
- "setAssets:"
- "setAttributes:ofItemAtPath:error:"
- "setAvailable:"
- "setBackgroundTask:"
- "setBlacklistedFeature:"
- "setBlock:"
- "setBlocker:"
- "setBodyCenterX:"
- "setBodyCenterY:"
- "setBodyHeight:"
- "setBodyWidth:"
- "setBool:forKey:"
- "setBoostPriority:"
- "setBoundaryKey:"
- "setBurstFlags:"
- "setBurstIdentifier:"
- "setBusyState:"
- "setByAddingObject:"
- "setByAddingObjectsFromSet:"
- "setBypassForceSyncLimitations:"
- "setCanGenerateDerivative:"
- "setCancellationHandler:"
- "setCancelledByEngine:"
- "setCaption:"
- "setCategory:"
- "setCenterX:"
- "setCenterY:"
- "setChangeType:"
- "setClassNameOfRecordsForInitialQuery:forScope:error:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientBundleID:"
- "setClientCacheIdentifier:"
- "setCloudAssetCountPerType:updateCheckDate:"
- "setCloudIndex:"
- "setCloudResource:"
- "setCloudScopeIndexOnChange:"
- "setCodec:"
- "setCommentDate:"
- "setCommentText:"
- "setCompleted:"
- "setCompletedUnitCount:"
- "setCompletionHandler:"
- "setComputeStateAdjustmentFingerprint:"
- "setComputeStateLastUpdatedDate:"
- "setComputeStateVersion:"
- "setConfigurationDictionaryUniquifier:"
- "setConfirmed:"
- "setConnectedToNetwork:cellularIsRestricted:inAirplaneMode:"
- "setContactDescriptor:"
- "setContactMatchingDictionary:"
- "setContainerHasBeenWiped:"
- "setContainerIdentifier:"
- "setContainerRelations:"
- "setContainerScopedIdentifier:"
- "setContext:"
- "setContributorUserIdentifier:"
- "setCountStyle:"
- "setCreationDate:"
- "setCreatorCode:"
- "setCropRectString:"
- "setCuratedAssetIdentifiers:"
- "setCustomRenderedValue:"
- "setCustomTitle:"
- "setCustomUserAssetList:"
- "setDateDeleted:"
- "setDateFormat:"
- "setDefaultHEVC:"
- "setDefaultPlatform:"
- "setDelegate:"
- "setDelegateQueue:"
- "setDeleteDate:"
- "setDeleteDate:forScope:error:"
- "setDeleteImmediately:"
- "setDeletedByUserIdentifier:"
- "setDerivativeGeneratorClass:"
- "setDetachedActivity:"
- "setDetectionType:"
- "setDidDropSomeRecordsForScope:error:"
- "setDidFinish:"
- "setDidStart:"
- "setDisableFeedback:"
- "setDisableInvalidFingerprintScheme:"
- "setDisableOverQuotaRule:"
- "setDisabled:"
- "setDisabledDate:"
- "setDisabledDate:forScope:error:"
- "setDisabledFeatures:"
- "setDisplayName:"
- "setDontAutoRetry:"
- "setDontBatchTransactions:"
- "setDownloadTasks:"
- "setDuration:"
- "setEffectiveClientBundleIdentifier:"
- "setEmail:"
- "setEndDate:"
- "setEngineLibrary:"
- "setError:"
- "setErrorForSyncSession:"
- "setErrorForSyncSessionUnlocked:"
- "setErrors:"
- "setEstimatedCountOfRemainingRecordsDuringSharedLibraryExit:"
- "setExitDeleteTime:"
- "setExitRetentionPolicy:"
- "setExitSource:"
- "setExitType:"
- "setExitingUserIdentifiers:"
- "setExpiryDate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExpungeDate:"
- "setExpungeableResourceStates:"
- "setExpungedDate:"
- "setExpungedState:"
- "setExtendedDescription:"
- "setExtraProperties:"
- "setExtractionStrategy:"
- "setFaceCropType:"
- "setFaceInstances:"
- "setFaceState:"
- "setFaces:"
- "setFacesAdjustmentsFingerprint:"
- "setFacesData:"
- "setFacesVersion:"
- "setFailOnPushingChangesTimeout:"
- "setFavorite:"
- "setFeature:"
- "setFeatureCompatibleVersion:"
- "setFeatureVersionHistory:"
- "setFeaturesData:"
- "setFetchCache:"
- "setFileSize:"
- "setFileStorageIdentifier:"
- "setFileURL:"
- "setFileUTI:"
- "setFilename:"
- "setFilter:"
- "setFinalCloudScopedIdentifier:forPendingCloudScopedIdentifier:error:"
- "setFinalData:"
- "setFinalError:"
- "setFinalResource:"
- "setFingerPrint:"
- "setForceSync:"
- "setForceSyncDelegate:"
- "setForcedTask:"
- "setForeground:"
- "setFull:"
- "setFullName:"
- "setFullSizeJPEGSource:"
- "setGraphData:"
- "setGraphVersion:"
- "setHasAllowed:"
- "setHasBodyCenterX:"
- "setHasBodyCenterY:"
- "setHasBodyHeight:"
- "setHasBodyWidth:"
- "setHasCellularBudget:hasBatteryBudget:hasLowBatteryLevel:isConstrainedNetwork:isBlockedByLowPowerMode:hasHeavyResourceUsage:hasPoorNetworkQuality:hasModerateThermalPressure:hasThermalPressure:hasPoorSystemConditions:isBudgetValid:blockedReason:unBlockedReason:"
- "setHasCenterX:"
- "setHasCenterY:"
- "setHasChangesToProcess:"
- "setHasCompleted:"
- "setHasDefaultHEVC:"
- "setHasDetectionType:"
- "setHasEPPAssets:"
- "setHasEnoughPower:"
- "setHasFaceState:"
- "setHasFeature:"
- "setHasFetchedInitialSyncAnchor:forScope:error:"
- "setHasFinishedInitialDownloadForScope:error:"
- "setHasIsCurated:"
- "setHasIsCustomUserAsset:"
- "setHasIsExtendedCurated:"
- "setHasIsKeyAsset:"
- "setHasIsMovieCurated:"
- "setHasIsRepresentative:"
- "setHasIsUserCurated:"
- "setHasNameSource:"
- "setHasNumRequested:"
- "setHasReason:"
- "setHasRetryAfterMillis:"
- "setHasSize:"
- "setHasSomeSharedCollections:"
- "setHasType:"
- "setHasUpdatedScope:fromTransportWithError:"
- "setHasVersion:"
- "setHasiCloudAccount:"
- "setHidden:"
- "setHighPriority:"
- "setHighPriorityBackground:"
- "setHost:"
- "setICloudLibraryClientIsNotAuthenticated:"
- "setICloudLibraryClientVersionTooOld:"
- "setICloudLibraryExists:"
- "setICloudLibraryHasBeenWiped:"
- "setIdentifier:"
- "setIdentity:"
- "setIgnoredDate:forRecordWithScopedIdentifier:error:"
- "setImageDimensions:"
- "setImportDate:"
- "setImportGroupIdentifier:"
- "setImportedBy:"
- "setImportedByBundleIdentifier:"
- "setImportedByDisplayName:"
- "setInExpunged:"
- "setInMemoryRequest:"
- "setInTrash:"
- "setInitialDownloadDate:"
- "setInitialDownloadDate:forScope:error:"
- "setInitialSyncAnchor:forScope:error:"
- "setInitialSyncDate:"
- "setIntent:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsComputeStateTaskUploadEnabled:"
- "setIsCurated:"
- "setIsCurrentUser:"
- "setIsCustomUserAsset:"
- "setIsExceedingQuota:"
- "setIsExceedingSharedLibraryQuota:"
- "setIsExtendedCurated:"
- "setIsJustInCaseSession:"
- "setIsKeyAsset:"
- "setIsMovieCurated:"
- "setIsRepresentative:"
- "setIsStuckInExitForSharedLibrary:"
- "setIsUserCurated:"
- "setItemIdentifier:"
- "setItemScopedIdentifier:"
- "setItemType:"
- "setIvar:"
- "setIvarValue:forObject:"
- "setKeepOriginals:"
- "setKey:"
- "setKeyAsset:"
- "setKeyAssetIdentifier:"
- "setKeyAssetScopedIdentifier:"
- "setKeyFace:"
- "setKeychainCDPEnabled:"
- "setKeysAndValues:"
- "setKeywords:"
- "setLastCompletePrefetchDate:"
- "setLastPruneDate:"
- "setLastSharedDate:"
- "setLastSuccessfulSyncDate:"
- "setLastViewedDate:"
- "setLibraryInfo:"
- "setLibraryState:"
- "setLocalIndex:"
- "setLocalScopeIndexOnChange:"
- "setLocale:"
- "setLocation:"
- "setLowDiskSpace:veryLowDiskSpace:"
- "setManual:"
- "setManualSortOrder:"
- "setMasterIdentifier:"
- "setMasterScopedIdentifier:"
- "setMaximumAlbumsPerBatch:"
- "setMaximumCountOfRecordsInBatches:"
- "setMaximumRecordCountPerBatch:"
- "setMediaGroupIdentifier:"
- "setMediaMetaData:"
- "setMediaMetaDataType:"
- "setMemoryIdentifier:"
- "setMemorys:"
- "setMergeTargetPersonIdentifier:"
- "setMergeTargetPersonScopedIdentifier:"
- "setMessages:"
- "setMetrics:"
- "setMinimumPriorityForLocalConflictResolution:"
- "setMode:"
- "setMomentShare:"
- "setMovieData:"
- "setName:"
- "setNameComponents:"
- "setNameSource:"
- "setNotificationState:"
- "setNow:"
- "setNumRequested:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOrientation:"
- "setOriginalChoice:"
- "setOriginalOrientation:"
- "setOriginatingFingerprint:"
- "setOriginatingScopeIdentifier:"
- "setOtherAdjustmentsFingerprint:"
- "setOwner:"
- "setParentIdentifier:"
- "setParentScopedIdentifier:"
- "setParticipantID:"
- "setParticipants:"
- "setPath:"
- "setPeople:"
- "setPermission:"
- "setPersonData:"
- "setPersonIdentifier:"
- "setPersonScopedIdentifier:"
- "setPersonType:"
- "setPersons:"
- "setPersonsData:"
- "setPetFaceInstances:"
- "setPhaseDescription:"
- "setPhoneNumber:"
- "setPhotosCount:"
- "setPlaceAnnotation:"
- "setPlaceLevel:"
- "setPlaceName:"
- "setPlatformImplementation:forClass:"
- "setPlayCount:"
- "setPosition:"
- "setPreviewData:"
- "setPreviewImageData:"
- "setPreviewImageDatas:"
- "setProblematicFormerSharedScopeIdentifier:"
- "setProgress:"
- "setProjectData:"
- "setProjectDocumentType:"
- "setProjectPreviewImageData:"
- "setPromisedAssetCount:"
- "setPromisedPhotosCount:"
- "setPromisedVideosCount:"
- "setPropertyClasses:"
- "setPropertyGetter:"
- "setPropertyGetterIMP:"
- "setPropertySetter:"
- "setPropertySetterIMP:"
- "setPropertyType:"
- "setProxyImplementationForPlatform:"
- "setProxyLibraryManager:"
- "setPublicPermission:"
- "setPullFromTransportExpirationInterval:scope:error:"
- "setPullTaskItem:"
- "setQuarantined:"
- "setQueryItems:"
- "setReadOnly:"
- "setRealIdentifier:"
- "setReason:"
- "setRecordChangeData:"
- "setRecordComputeStateDelegate:"
- "setRecordList:"
- "setRecordModificationDate:"
- "setRejected:"
- "setRejectedPersonIdentifier:"
- "setRejectedPersonIdentifiers:"
- "setRelatedIdentifier:"
- "setRelation:"
- "setRelevantUntilDate:"
- "setRemoteObjectInterface:"
- "setRequests:"
- "setRequiredStateObserverBlock:"
- "setRescheduler:"
- "setResetTracker:"
- "setResetting:"
- "setResource:"
- "setResourceCopyFromScopedIdentifier:"
- "setResourceData:"
- "setResourceProgressDelegate:"
- "setResourceType:"
- "setResources:"
- "setResponses:"
- "setRetryAfterMillis:"
- "setRewindAnchorsPerSharingScopes:"
- "setRewindAnchorsPerSharingScopesData:"
- "setRole:"
- "setRoughCPLDownloadEstimatedSize:"
- "setRoughCPLRecordCount:"
- "setRoughCPLUploadEstimatedSize:"
- "setScheme:"
- "setScope:"
- "setScope:hasCompletedClientNeedsToPullTask:error:"
- "setScope:hasCompletedInitialMinglingWithError:"
- "setScope:hasCompletedPullFromTransportTask:error:"
- "setScope:hasCompletedPushToTransportTask:error:"
- "setScope:hasCompletedTransportUpdate:error:"
- "setScope:hasCompletedUploadComputeStateTask:error:"
- "setScopeHasChangesToPullFromTransport:error:"
- "setScopeHasChangesToPushToTransport:changeTypes:error:"
- "setScopeHasChangesToPushToTransport:error:"
- "setScopeIdentifierToAutomaticallyExcludeFromMingling:"
- "setScopeIndex:"
- "setScopeNeedsToBePulledByClient:error:"
- "setScopeNeedsToUpdateTransport:error:"
- "setScopeNeedsToUploadComputeState:error:"
- "setScopeNeedsUpdateFromTransport:error:"
- "setScopeType:"
- "setScopeType:forScope:error:"
- "setScopedIdentifier:"
- "setScore:"
- "setSecondaryIdentifier:"
- "setServerFeatureCompatibleVersion:"
- "setServerRecordIsCorrupted:"
- "setShare:"
- "setShareCount:"
- "setShareURL:"
- "setShared:"
- "setSharedContext:"
- "setSharedLibrarySharingState:"
- "setSharedScope:"
- "setSharingContributorUserIdentifiers:"
- "setSharingRecordChangeData:"
- "setSharingRecordIdentifier:"
- "setSharingRecordScopedIdentifier:"
- "setSharingScopeIdentifier:"
- "setShouldBackOffOnErrorBlock:"
- "setShouldCheckFilesForUpload:"
- "setShouldCheckOverQuotaChangesWithServer:"
- "setShouldCompareAllProperties:"
- "setShouldConsiderRequestingMoreTime:"
- "setShouldCreateScopeIfNecessary:"
- "setShouldFilterDefaultValuesForNewProperties:"
- "setShouldHaveRequestedMoreTime:"
- "setShouldIgnoreLowDiskSpace:"
- "setShouldOverride:forSystemBudgets:"
- "setShouldOverrideSystemBudgetsForSyncSession:"
- "setShouldRequestMoreTime:"
- "setShouldTryToMingleImmediately:"
- "setShouldUpdateDisabledFeaturesWithError:"
- "setSimilarToOriginalAdjustmentsFingerprint:"
- "setSimpleAdjustmentData:"
- "setSize:"
- "setSourceResourceType:"
- "setStableHash:"
- "setStableIndex:"
- "setStagedScopeChange:"
- "setStagedScopeFlags:"
- "setStagedTransportScope:"
- "setStagingScopeIdentifier:"
- "setStartDate:"
- "setStartTime:"
- "setState:"
- "setStatus:"
- "setStructName:"
- "setSubcategory:"
- "setSubtitle:"
- "setSubtype:"
- "setSuffix:"
- "setSupervisor:"
- "setSyncAnchor:forScope:error:"
- "setSyncSessionShouldBeForeground:"
- "setSyndicationIdentifier:"
- "setTarget:forRecordWithScopedIdentifier:"
- "setTaskActivity:"
- "setTaskDidFinishWithErrorBlock:"
- "setTaskIdentifier:"
- "setTaskIdentifierForQueue:"
- "setTentative:"
- "setThrottlingDate:"
- "setThroughputReporter:"
- "setThumbnailImageData:"
- "setTimeRange:"
- "setTimeToWaitForClientToActivateScopes:"
- "setTimeToWaitForClientToPullChanges:"
- "setTimeToWaitForClientToPushChanges:"
- "setTimeToWaitForLibrary:"
- "setTimeZoneName:"
- "setTimeZoneOffset:"
- "setTitle:"
- "setTorsoFaceInstances:"
- "setTotalCount:"
- "setTrackAllStoresAndDeletes:"
- "setTrackAllStoresAndDeletesUntilEndOfTransaction:"
- "setTransportGroup:"
- "setTransportIdentifier:"
- "setTransportScope:"
- "setTransportScope:forScope:error:"
- "setTransportScopeMapping:"
- "setTransportShare:"
- "setTransportTask:"
- "setTransportUserIdentifier:"
- "setTrashedReason:"
- "setType:"
- "setURL:"
- "setUnknown:"
- "setUpdateSharingContributorUserIdentifiers:"
- "setUpdating:"
- "setUpgradeSuggestedToAccessAllPhotos:"
- "setUploaded:"
- "setUploading:"
- "setUserActionOptions:"
- "setUserDefinedRules:"
- "setUserIdentifier:"
- "setUserModificationDate:"
- "setUserOverride:"
- "setUserViewedParticipantTrashNotificationDate:"
- "setValue:"
- "setValue:forFlag:"
- "setValue:forFlag:forScope:error:"
- "setValue:forKey:"
- "setVerifiedType:"
- "setVersion:"
- "setVideoComplementDurationTimescale:"
- "setVideoComplementDurationValue:"
- "setVideoComplementImageDisplayTimescale:"
- "setVideoComplementImageDisplayValue:"
- "setVideoComplementVisibilityState:"
- "setVideoFrameRate:"
- "setVideosCount:"
- "setViewCount:"
- "setViewPresentation:"
- "setWaitingForUpdate:"
- "setWaitingForUpload:"
- "setWalrusEnabled:"
- "setWeakLibraryManager:"
- "setWithObject:"
- "setWithObjects:"
- "settingName"
- "setupAnchorResetTransportGroupForScope:error:"
- "setupCloudScopedIdentifier:forLocalScopedIdentifier:isFinal:direction:error:"
- "setupFingerprintContextForTests"
- "setupInitialSyncTransportGroupsForScope:error:"
- "setupResetSyncTransportGroupForScope:error:"
- "setupTaskUpdateDisabledFeatures:completionHandler:"
- "setupWithConfiguration:"
- "share"
- "shareParticipantsFromMomentShareParticipants:"
- "shareURL"
- "shared"
- "sharedCloudScopedIdentifier"
- "sharedContext"
- "sharedInstance"
- "sharedLibraryRampCheckWithCompletionHandler:"
- "sharedLibraryServerRampTaskWithCompletionHandler:"
- "sharedScope"
- "sharingRecordScopedIdentifier"
- "sharingScopeForScope:"
- "shortDescription"
- "shortDescriptionForResourceChangeRecordType:"
- "shortDescriptionForResourceType:"
- "shortDescriptionForState:"
- "shouldAlwaysUpdateScopeInfoWhenPossible"
- "shouldApplyPropertiesWithSelector:"
- "shouldAutoActivateScopeWithType:"
- "shouldAutoactivateScopeWithIdentifier:scopeType:"
- "shouldBackOffOnErrorBlock"
- "shouldBeCreatedDynamically"
- "shouldBeDiscretionary"
- "shouldBeTemporarilyNonDiscretionary"
- "shouldBypassCaches"
- "shouldCancelSyncSessionTryingToUploadChange:"
- "shouldCheckAssetsWithServerWhenOverQuotaForScope:"
- "shouldCheckEPPCapability"
- "shouldCheckFilesForUpload"
- "shouldCheckOverQuotaChangesWithServer"
- "shouldCoalesceServerChangesNotification"
- "shouldCompareAllProperties"
- "shouldConsiderRequestingMoreTime"
- "shouldContinueAfterError:fromTask:"
- "shouldDefer"
- "shouldDisableEPP"
- "shouldDisableScopeWhenFeatureIsDisabled:"
- "shouldDropAllUploadsForScope:dropReason:shouldQuarantineRecords:"
- "shouldDropDerivativeWithDropDerivativeRecipe:"
- "shouldFilterDefaultValuesForNewProperties"
- "shouldGenerateDerivatives"
- "shouldHaveRequestedMoreTime"
- "shouldIgnoreDefaultsCPLKey:"
- "shouldIgnoreLowDiskSpace"
- "shouldIgnoreResourceTypeOnUpload:"
- "shouldIgnoreScopeWithIdentifier:"
- "shouldIncludeInStatus"
- "shouldKeepDeleteChange:forRecordWithScopedIdentifier:"
- "shouldKeepPower"
- "shouldOnlyUploadNewResources"
- "shouldProcessScope:inTransaction:"
- "shouldReallyQuarantineRecord"
- "shouldRequestMoreTime"
- "shouldRescheduleASyncSession"
- "shouldResetExceedingQuotaOnSuccessfulUpload"
- "shouldResetFromThisStepWithIncomingChange:"
- "shouldRetryDownloadOnError:"
- "shouldRevertRecordWithLocalScopedIdentifier:"
- "shouldShowAlertToUser"
- "shouldShowBackgroundSchedulingStatusInTransport"
- "shouldSkipScopesWithMissingTransportScope"
- "shouldStartSyncSessionFromState:"
- "shouldStartTaskInTransaction:"
- "shouldSyncScopeList"
- "shouldTrackAdditionalInitialSyncDatesForScope:"
- "shouldTryToMingleImmediately"
- "shouldUpdateDisabledFeatures"
- "shouldUpdatePropertyOnPrivateRecord:recordClass:"
- "shouldUpdatePropertyOnSharedRecord:recordClass:"
- "shouldUploadResource:"
- "shouldUploadToOtherRecord"
- "shouldUseEncryptedPropertiesIfPossible"
- "showAlertToUser"
- "showNetworkIndicatorForBundleWithIdentifier:"
- "showSyncIndicator"
- "signal"
- "simpleDescription"
- "simpleDescriptionForScopeListSyncAnchor:"
- "simpleDescriptionForSyncAnchor:"
- "sizeOfOriginalResourcesToUpload"
- "sizeOfResourcesToUpload"
- "sizeOfResourcesToUploadDidChangeForLibraryManager:"
- "sortBatchWithError:"
- "sortUsingSelector:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingDescriptors:"
- "sortedArrayUsingSelector:"
- "sortedKeywordsForKeywordSet:"
- "sourceResource"
- "speed"
- "stableScopeIndexForScopeIdentifier:"
- "stage"
- "stagedScopeChange"
- "stagedScopeFlags"
- "stagedTransportScope"
- "stagingScopeForScope:"
- "stagingScopeIdentifier"
- "stale"
- "standardUserDefaults"
- "startAutomaticOverridingSystemBudgets:"
- "startDate"
- "startExitFromSharedScopeWithIdentifier:retentionPolicy:exitSource:completionHandler:"
- "startExitTaskFromSharedScope:transportScope:share:retentionPolicy:exitSource:completionHandler:"
- "startMonitoringPowerEvents"
- "startOverridingSystemBudgets:reason:"
- "startOverridingSystemBudgetsForClient:"
- "startRequiredSyncSessionNow:"
- "startSyncSession"
- "startSyncSession:withMinimalPhase:rewind:"
- "startTrackingUpdates"
- "startTrackingWork"
- "startVacuumWithCompletionHandler:"
- "startWatching"
- "stashChange:error:"
- "stashChangeWithScopedIdentifier:error:"
- "stateDescriptionForState:"
- "statusChanges"
- "statusChangesMaximumCount:"
- "statusDescription"
- "statusDictionary"
- "statusDictionaryForScope:"
- "statusDidChange:"
- "statusError"
- "statusForRecordWithScopedIdentifier:"
- "statusKey"
- "statusPerScopeIndex"
- "statusesForRecordsWithIdentifiers:"
- "statusesForRecordsWithScopedIdentifiers:"
- "stepForState:syncManager:session:"
- "stepsDescription"
- "stop"
- "stopAutomaticOverridingSystemBudgets:"
- "stopOverridingSystemBudgets:reason:"
- "stopOverridingSystemBudgetsForClient:"
- "stopVacuum"
- "stopWatching"
- "storage"
- "storageDescription"
- "storageForStatusInStore:"
- "storageNameForFingerPrint:fileUTI:bucket:"
- "storageNames"
- "storeActivationDate:forScope:error:"
- "storeBusyState:forScope:error:"
- "storeChange:pushContext:discardedUploadIdentifier:error:"
- "storeChange:pushContext:error:"
- "storeChangeSessionUpdate:error:"
- "storeClientCacheIdentifier:error:"
- "storeClientIsInSyncWithClientCacheWithError:"
- "storeClientIsNotInSyncWithClientCacheWithError:"
- "storeData:identifier:needsCommit:error:"
- "storeData:identity:isOriginal:needsCommit:error:"
- "storeData:identity:isOriginal:needsCommit:onNewFile:error:"
- "storeDerivativesFilter:error:"
- "storeDisabledFeatures:error:"
- "storeDownloadTransportGroup:forScope:error:"
- "storeDownloadedResource:atURL:error:"
- "storeExtractedBatch:error:"
- "storeFileAtURL:identifier:moveIfPossible:needsCommit:error:"
- "storeFileAtURL:identity:isOriginal:moveIfPossible:needsCommit:error:"
- "storeFileAtURL:identity:isOriginal:moveIfPossible:needsCommit:onNewFile:error:"
- "storeInitialMetadataDownloadDate:forScope:error:"
- "storeInitialMetadataQueriesDate:forScope:error:"
- "storeInitialMingleDate:forScope:error:"
- "storeLastDateOfClearedPushRepository:forScope:error:"
- "storeLastQuarantineCountReportDate:error:"
- "storeLibraryVersion:withError:"
- "storePushPullGatekeepers:error:"
- "storeResourceCopyForUpload:error:"
- "storeResourceForUpload:shouldCheckResource:error:"
- "storeResourceToUpload:withUploadIdentifier:error:"
- "storeResourcesToUpload:withUploadIdentifier:shouldCheckResources:error:"
- "storeRewindSyncAnchors:forScope:error:"
- "storeScopeChange:forScope:error:"
- "storeScopeChange:forScope:scopeChangeHasBeenUpdated:error:"
- "storeScopeListSyncAnchor:error:"
- "storeSharingScopeIdentifier:"
- "storeSupervisorInfo:forScope:error:"
- "storeSupportedFeatureVersionInLastSync:forScope:error:"
- "storeTransientSyncAnchor:forScope:error:"
- "storeUnretainedData:identifier:error:"
- "storeUnretainedData:identity:isOriginal:error:"
- "storeUnretainedFileAtURL:identifier:error:"
- "storeUnretainedFileAtURL:identity:isOriginal:error:"
- "storeUploadTransportGroup:forScope:error:"
- "storeUserIdentifier:error:"
- "storeVersionHasChanged"
- "storedChangeSessionUpdate"
- "storedClassNameForCPLArchiver:"
- "storedClientRecordWithLocalScopedIdentifier:"
- "storedCloudRecordWithLocalScopedIdentifier:"
- "storedExtractedBatch"
- "storedTransportGroup"
- "strategyName"
- "stringByAbbreviatingWithTildeInPath"
- "stringByAppendingFormat:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringForObjectValue:"
- "stringForTimeInterval:"
- "stringForTimeIntervalAgo:now:"
- "stringForTimeIntervalNumber:now:"
- "stringFromByteCount:countStyle:"
- "stringFromDate:"
- "stringFromDateAgo:now:"
- "stringRepresentation"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "strongToStrongObjectsMapTable"
- "structName"
- "subarrayWithRange:"
- "subdataWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "suffix"
- "summaryDescription"
- "supervisor"
- "supervisorInfoForScope:"
- "supportedChangeTypes"
- "supportedFeatureCompatibleVersion"
- "supportedFeatureVersionInLastSyncForScope:"
- "supportedFeatureVersionIsMostRecentForScope:"
- "supportsActivationOfScopeWithType:"
- "supportsCollectionShare"
- "supportsDeletion"
- "supportsDirectDeletion"
- "supportsDirectMinglingForScopeWithType:"
- "supportsEPP"
- "supportsEPPAutoEnable"
- "supportsRecordModificationDate"
- "supportsResourceType:"
- "supportsResources"
- "supportsSecureCoding"
- "supportsSharing"
- "supportsSharingScopeWithIdentifier:forScopeWithIdentifier:"
- "supportsSharingScopedIdentifier"
- "supportsStagingScopeForScopeWithType:"
- "syncAnchorForFeatureVersion:"
- "syncAnchorForScope:"
- "syncAnchorForScope:isCommitted:"
- "syncHasBeenRequested"
- "syncManager"
- "syncSession"
- "syncSessionDidFailWithError:"
- "syncSessionDidSucceed"
- "syncSessionRequestedImmediateRuntime"
- "syncSessionShouldRequestMoreTime"
- "syncStatus"
- "synchronize"
- "synchronizing scope list: enabled\n"
- "synthesizedRecord"
- "systemMonitor"
- "takeStatisticsSnapshotSinceDate:completionHandler:"
- "tap-to-radar://new"
- "target"
- "targetDescriptions"
- "targetForRecordWithCloudScopedIdentifier:"
- "targetForRecordWithCloudScopedIdentifier:trustRecordChangeData:"
- "targetForRecordWithOtherScopedIdentifier:"
- "targetForRecordWithScopedIdentifier:"
- "targetForRecordWithSharedCloudScopedIdentifier:"
- "targetForRecordWithSharedCloudScopedIdentifier:trustRecordChangeData:"
- "targetMapping"
- "targetScopedIdentifiers"
- "targetState"
- "task:checkScopeIsValidInTransaction:"
- "task:didFinishWithError:"
- "task:didProgress:userInfo:"
- "task:noteSuccessfulUpdateInTransaction:"
- "task:shouldRetryImmediatelyInTransaction:"
- "task:shouldUploadBatchesWithDropReason:shouldQuarantineRecords:inTransaction:"
- "taskActivity"
- "taskClass"
- "taskDidFinishWithError:"
- "taskDidFinishWithErrorBlock"
- "taskDidProgress:userInfo:"
- "taskIdentifier"
- "taskIdentifierForQueue"
- "taskWithEngineLibrary:session:"
- "tearDownWithCompletionHandler:"
- "tempFolderURL"
- "tentative"
- "tentativeConcreteScopeForScope:"
- "testKey:value:completionHandler:"
- "testKey:value:didHandle:result:error:"
- "testMessage"
- "threadDictionary"
- "throughputReporter:addedItemCount:"
- "throughputReporterDidFinish:"
- "thumbnailImageData"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSincePredictedDateForType:"
- "timeIntervalSinceReferenceDate"
- "timeToWaitForClientToActivateScopes"
- "timeToWaitForClientToPullChanges"
- "timeToWaitForClientToPushChanges"
- "timeToWaitForLibrary"
- "tooManyOpenedEnginesError"
- "torsoFaceInstancesAtIndex:"
- "torsoFaceInstancesCount"
- "torsoFaceInstancesType"
- "totalAssetCountOnServer"
- "totalCount"
- "totalOriginalResourceSize"
- "totalResourceSize"
- "totalUnitCount"
- "trackAllStoresAndDeletes"
- "trackAllStoresAndDeletesUntilEndOfTransaction"
- "transactionClientCacheView"
- "transactionCount"
- "transactionDidFinish"
- "transactionTransportScopeMapping"
- "transactions"
- "transientRepository"
- "transientRepository:didResetMingledRecordsForScopesWithFiler:"
- "transientSyncAnchorForScope:"
- "translateToClientChangeUsingIDMapping:error:"
- "translateToClientRecordUsingIDMapping:"
- "translateToCloudChangeUsingIDMapping:error:"
- "translateToCloudRecordUsingIDMapping:"
- "translateToScopeChangeWithScopeType:"
- "translator"
- "transportErrorFromTransportError:"
- "transportGroupClass"
- "transportHasRecordWithScopedIdentifier:"
- "transportIdentifier"
- "transportScope"
- "transportScopeForScope:"
- "transportScopeForUpgradeFromScopeName:"
- "transportScopeFromConcreteScope:"
- "transportScopeMapping"
- "transportTask"
- "transportUpdateTaskForScope:"
- "transportUserIdentifier"
- "tryToFreeDiskSpace:actuallyFreedSpace:error:"
- "tryToFreeDiskSpace:actuallyFreedSpace:includeOriginals:error:"
- "typeWithFilenameExtension:"
- "typeWithIdentifier:"
- "unableToDeserializeRecordInStorage:"
- "unableToSerializeRecordError:inStorage:"
- "unacknowledgedChangeWithLocalScopedIdentifier:"
- "unarchiveArrayOfCPLDropDerivativeRecipesFrom:"
- "unarchiveObjectWithData:ofClass:"
- "unarchivedObjectOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unarchivedObjectWithPropertyList:ofClass:"
- "unblock"
- "unblockEngineElement:"
- "unblockEngineElementOnce:"
- "unblockSyncSessionWithReason:"
- "underlyingErrorWithReason:"
- "unionSet:"
- "unkn. status"
- "unknownError"
- "unknownPrimaryScope"
- "unknownTargetScopedIdentifiers"
- "unlock"
- "unmingledChangeWithScopedIdentifier:"
- "unquarantinedRecordScopedIdentifiers"
- "unsafeResources:withError:realPrune:resourceStorage:"
- "unsafeResources:withError:resourceStorage:"
- "unschedulePersistedSyncSession"
- "unscheduleSyncSession:"
- "unscopedIdentifiersFromArrayOfScopedIdentifiers:"
- "unscopedIdentifiersFromDictionaryOfScopedIdentifiers:"
- "unscopedIdentifiersFromSetOfScopedIdentifiers:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unstashRecordsForScopeWithIdentifier:maxCount:hasMore:unstashedCount:error:"
- "updateAccountFlagsData:"
- "updateApproximativeUploadRate:"
- "updateAssetCountsFromServer:"
- "updateBlockedMetrics:syncRequested:runtimeCharacteristics:"
- "updateComputeSyncMetrics:silentDecryptionFailed:error:"
- "updateConfigurationDictionary:"
- "updateContributorsTaskWithSharedScope:contributorsUpdates:transportScopeMapping:completionHandler:"
- "updateDisabledFeatures:"
- "updateDisabledFeatures:didReset:error:"
- "updateDiskPressureState"
- "updateFileURLForComputeState:discardedFileStorageIdentifier:hasUpdated:error:"
- "updateFileURLForComputeState:error:"
- "updateFinalRecord:confirmed:error:"
- "updateFlags:"
- "updateFlags:forScope:error:"
- "updateFlags:withFlagsValue:"
- "updateInitialDownloadDate:"
- "updateInitialSyncDate:"
- "updateInitialSyncTransportGroupEstimatedSize:assetCount:forScope:error:"
- "updateIntervalKey"
- "updateLastSuccessfullSyncDate:"
- "updateLibraryOptions:error:"
- "updateLocalStateForComputeState:newLocalState:error:"
- "updatePredictedDate:forType:"
- "updatePredictedValue:forType:"
- "updatePrediction:"
- "updatePredictionWithValuesAndTypes:"
- "updatePredictionsWithDerivativesStatistics:"
- "updatePushRepositoryPriorityWithRecordOnServer:"
- "updateScopeChange:"
- "updateScopeFilter:"
- "updateScopeFromScopeChange:direction:didHaveChanges:"
- "updateScopeIdentifier:"
- "updateScopeWithChange:error:"
- "updateScopeWithNewScopeType:scope:updatedScopeChange:updatedFlags:oldTransportScope:updatedTransportScope:shouldUpdateTransportScope:store:transport:session:inTransaction:"
- "updateShareForScope:completionHandler:"
- "updateShareTaskForScope:transportScope:completionHandler:"
- "updateStagedRecord:error:"
- "updateStoredTargetsFromTargetMapping:"
- "updateSyncSessionPrediction:"
- "updateTimingStatisticForKey:duration:recordCount:error:cancelled:"
- "updateTransportScope:scope:scopeChange:completionHandler:"
- "updateWithAccountEPPCapability:source:"
- "updateWithDuration:recordCount:error:cancelled:"
- "updateWithStatus:configuration:"
- "updateWithTransportScopeMapping:"
- "updatedFlagsFromFlags:"
- "updatedFlagsMask"
- "updatedPredictionRemovingValueForType:"
- "updatedPredictionWithValuesAndTypes:"
- "updatedProperties"
- "updatedRecords"
- "updatedScopeFilter:"
- "updatedTargetScopedIdentifiers"
- "updatedTargets"
- "updatedTargetsDescription"
- "updatedTransportScope"
- "updating"
- "upgradeFlags:fromTransportScope:"
- "upgradeScopesWithNewLibraryOptions:error:"
- "uploadBatchTaskForBatch:scope:targetMapping:transportScopeMapping:progressHandler:completionHandler:"
- "uploadComputeStateTaskForScope:"
- "uploadComputeStates:scope:sharedScope:targetMapping:transportScopeMapping:knownRecords:completionHandler:"
- "uploadDidStartForResource:withResourceTransferTask:"
- "uploadIdentifier"
- "uploadIdentifierForChange:"
- "uploadOfResource:didFinishForResourceTransferTask:withError:"
- "uploadOfResource:didProgress:forResourceTransferTask:"
- "uploadTransportGroupForScope:"
- "uploaded"
- "uppercaseString"
- "useCloudPhotoDaemonImplementation"
- "useFinal"
- "userIdentifier"
- "userIdentifierClass"
- "userInfo"
- "userOverride"
- "userViewedParticipantTrashNotificationDate"
- "usesFakeDerivatives"
- "usesMMCSv2AsDefault"
- "usualStrategyWithStorage:coveringScopeIdentifier:"
- "v104@0:8@\"CPLResource\"16Q24@\"NSDictionary\"32{?={?=qiIq}{?=qiIq}}40@\"NSString\"88@?<v@?@\"NSURL\"@\"NSData\"@\"NSDate\"@\"NSString\"@\"NSError\">96"
- "v104@0:8@16Q24@32{?={?=qiIq}{?=qiIq}}40@88@?96"
- "v104@0:8q16@24@32@40@48@56@?64@72@80@88@96"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8c16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v20@0:8s16"
- "v24@0:8#16"
- "v24@0:8:16"
- "v24@0:8@\"<CPLEngineStoreUserIdentifier>\"16"
- "v24@0:8@\"CPLEngineForceSyncTask\"16"
- "v24@0:8@\"CPLLibraryManager\"16"
- "v24@0:8@\"CPLResource\"16"
- "v24@0:8@\"CPLStatus\"16"
- "v24@0:8@\"CPLSyncThroughputReporter\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"_CPLScheduledOverride\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"<CPLEngineSyncManagerForcedTask>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"CPLScopeChange\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"CPLChangeBatch\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSURL\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8B16B20"
- "v24@0:8I16B20"
- "v24@0:8Q16"
- "v24@0:8^?16"
- "v24@0:8^{?=Q^@^Q[5Q]}16"
- "v24@0:8^{network_usage_policy_client_s=}16"
- "v24@0:8^{objc_ivar=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8r*16"
- "v24@0:8r^^Q16"
- "v24@?0@\"_CPLResourcesMutableArray\"8@\"NSError\"16"
- "v28@0:8@\"NSArray\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16f24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8B16B20B24"
- "v28@0:8B16Q20"
- "v28@0:8B16q20"
- "v28@0:8Q16B24"
- "v28@0:8f16@\"NSString\"20"
- "v28@0:8f16@20"
- "v28@0:8i16@20"
- "v32@0:8#16#24"
- "v32@0:8#16@24"
- "v32@0:8@\"CPLChangeBatch\"16@?<v@?@\"NSError\"@\"NSString\">24"
- "v32@0:8@\"CPLChangeBatch\"16@?<v@?@\"NSError\"Q@\"CPLPushChangeTasks\"@\"NSString\">24"
- "v32@0:8@\"CPLEngineSyncTask\"16@\"NSError\"24"
- "v32@0:8@\"CPLEngineTransientRepository\"16@\"CPLScopeFilter\"24"
- "v32@0:8@\"CPLLibraryManager\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"CPLNetworkWatcher\"16@\"CPLNetworkState\"24"
- "v32@0:8@\"CPLResource\"16@\"NSString\"24"
- "v32@0:8@\"CPLResource\"16@?<v@?@\"CPLResource\"Q>24"
- "v32@0:8@\"CPLScopeChange\"16@?<v@?@\"CPLScopeChange\"@\"NSError\">24"
- "v32@0:8@\"CPLScopeChange\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"CPLScopedIdentifier\"16@?<v@?@\"CPLRecordChange\"Q>24"
- "v32@0:8@\"CPLScopedIdentifier\"16@?<v@?@\"NSError\"@\"NSArray\">24"
- "v32@0:8@\"CPLSyncSessionPredictor\"16@\"CPLSyncSessionPrediction\"24"
- "v32@0:8@\"CPLSyncThroughputReporter\"16Q24"
- "v32@0:8@\"CPLUploadPushedChangesTask\"16@\"CPLEngineStoreTransaction\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"CPLForceSyncTask\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"CPLScopeChange\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"CPLScopeChange\"Q>24"
- "v32@0:8@\"NSString\"16@?<v@?@\"CPLScopeStatusCounts\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"CPLScopeChange\"@\"NSError\">24"
- "v32@0:8@16*24"
- "v32@0:8@16:24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8@?16@24"
- "v32@0:8@?16@?24"
- "v32@0:8B16B20@24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16Q24"
- "v32@0:8Q16d24"
- "v32@0:8^@16@?24"
- "v32@0:8d16@24"
- "v32@0:8d16@?24"
- "v32@0:8q16@24"
- "v32@0:8q16q24"
- "v32@0:8r^v16Q24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@\"CPLConfigurationFetcher\"16@\"CPLConfigurationDictionary\"24B32"
- "v36@0:8@\"CPLDropDerivativesRecipe\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"CPLEngineSyncTask\"16f24@\"NSDictionary\"28"
- "v36@0:8@\"CPLRecordChange\"16B24@\"CPLRecordChange\"28"
- "v36@0:8@\"CPLResource\"16f24@\"NSString\"28"
- "v36@0:8@\"CPLScopedIdentifier\"16B24@?<v@?@@@\"NSError\">28"
- "v36@0:8@\"CPLSyncSessionThroughputMetrics\"16Q24B32"
- "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSDictionary\">28"
- "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSXPCConnection\"16@\"NSInvocation\"24B32"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16B24Q28"
- "v36@0:8@16Q24B32"
- "v36@0:8@16f24@28"
- "v36@0:8Q16B24@28"
- "v36@0:8q16B24@28"
- "v40@0:8@\"CPLResource\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"CPLResource\"16@\"NSString\"24@?<v@?@\"CPLResource\"Q>32"
- "v40@0:8@\"CPLResource\"16@\"NSString\"24@?<v@?@\"CPLResourceTransferTask\">32"
- "v40@0:8@\"CPLResource\"16@\"NSString\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"CPLChangeSessionContext\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"CPLResource\"24@\"NSError\"32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@\"NSError\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@16#24@32"
- "v40@0:8@16:24@?32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28Q32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16Q24^B32"
- "v40@0:8@16d24Q32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?BQ@\"NSError\">32"
- "v40@0:8^@16^@24@32"
- "v40@0:8d16Q24B32B36"
- "v40@0:8r*16Q24@32"
- "v40@0:8r*16Q24^v32"
- "v40@0:8r*16Q24r^v32"
- "v40@0:8{CGPoint=dd}16@32"
- "v40@0:8{CGSize=dd}16@32"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24@28@?36"
- "v44@0:8^@16@24@32B40"
- "v48@0:8@\"CPLLibraryManager\"16@\"CPLResource\"24#32@?<v@?@\"CPLResource\"Q>40"
- "v48@0:8@\"NSArray\"16@\"CPLRecordComputeStateValidator\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16q24q32@?<v@?@\"CPLLibraryShareScopeChange\"@\"NSError\">40"
- "v48@0:8@16@24#32@?40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24B32B36@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16d24Q32B40B44"
- "v48@0:8@16q24q32@?40"
- "v48@?0@\"NSError\"8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSURL\"40"
- "v52@0:8@16@24@32B40@44"
- "v52@0:8@16@24@32B40B44B48"
- "v52@0:8@16@24B32@36@?44"
- "v52@0:8^Q16i24Q28@36@44"
- "v56@0:8@\"CPLResource\"16@\"NSString\"24@\"CPLResourceTransferTaskOptions\"32@\"NSString\"40@?<v@?@\"CPLResourceTransferTask\">48"
- "v56@0:8@\"CPLResource\"16@\"NSString\"24@\"CPLResourceTransferTaskOptions\"32@\"NSString\"40@?<v@?@\"NSString\">48"
- "v56@0:8@\"NSArray\"16@\"NSString\"24q32q40@?<v@?@\"CPLLibraryShareScopeChange\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@?32@?40@?48"
- "v56@0:8@16@24Q32@40@?48"
- "v56@0:8@16@24q32q40@?48"
- "v56@0:8@16Q24@32@40@?48"
- "v56@0:8Q16Q24Q32Q40Q48"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "v64@0:8q16@24@32@40@48@56"
- "v64@0:8q16@24@32@40@48@?56"
- "v64@0:8{?={?=qiIq}{?=qiIq}}16"
- "v72@0:8@\"NSURL\"16@\"NSURL\"24@\"NSURL\"32@\"NSString\"40@\"NSString\"48Q56@?<v@?@\"NSError\"@\"NSDictionary\"QQQQQ@\"NSString\"@\"NSString\"@\"NSString\"@\"NSURL\">64"
- "v72@0:8@16@24@32@40@48Q56@?64"
- "v76@0:8B16B20B24B28B32B36B40B44B48B52B56q60q68"
- "v96@?0@\"NSError\"8@\"NSDictionary\"16Q24Q32Q40Q48Q56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSURL\"88"
- "valid"
- "validCloudIndexes"
- "validCloudScopeIndexes"
- "validElements"
- "validLocalIndexes"
- "validLocalScopeIndexes"
- "validateChangeWithError:"
- "validateFullRecord"
- "validateRecordForTracker:"
- "valueForFlag:"
- "valueForFlag:forScope:"
- "valueForKey:"
- "versionMismatchError"
- "verticalAccuracy"
- "videosCount"
- "waitForEngineElementToBeBlocked:timeout:"
- "waitUntilDate:"
- "waitingForUpdate"
- "waitingForUpload"
- "watcher:stateDidChangeToNetworkState:"
- "weakLibraryManager"
- "weakObjectsHashTable"
- "whenItWillStartDescription"
- "whitespaceAndNewlineCharacterSet"
- "willBeginPushSession"
- "willGenerateReport"
- "willNeedToAccessRecordWithScopedIdentifier:error:"
- "willRunEngineElement:"
- "willStartSyncSession"
- "willUploadCloudResource:localResource:error:"
- "willUploadCloudResource:localResource:forItem:error:"
- "willUploadSomeResources"
- "wipeStoreAtNextOpeningWithReason:completionBlock:"
- "wiping database because it has been marked as deactivated"
- "withThroughputReporter:"
- "withTrackerForChangeType:block:"
- "writeInitialSyncMarker:"
- "writeTo:"
- "writeToURL:atomically:"
- "writeToURL:atomically:encoding:error:"
- "writeToURL:error:"
- "writeToURL:options:error:"
- "writeTransactionBlocker"
- "writeTransactionDidFail"
- "writeTransactionDidSucceed"
- "zeroByteFileFingerprint"
- "{?=\"bodyCenterX\"b1\"bodyCenterY\"b1\"bodyHeight\"b1\"bodyWidth\"b1\"centerX\"b1\"centerY\"b1\"size\"b1\"detectionType\"b1\"faceState\"b1\"nameSource\"b1}"
- "{?=\"completed\"b1}"
- "{?=\"feature\"b1\"type\"b1}"
- "{?=\"isCurated\"b1\"isCustomUserAsset\"b1\"isExtendedCurated\"b1\"isKeyAsset\"b1\"isMovieCurated\"b1\"isRepresentative\"b1\"isUserCurated\"b1}"
- "{?=\"isKeyAsset\"b1\"isRepresentative\"b1}"
- "{?=\"numRequested\"b1}"
- "{?=\"retryAfterMillis\"b1\"allowed\"b1}"
- "{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}"
- "{?=\"version\"b1\"reason\"b1\"defaultHEVC\"b1}"
- "{?=\"version\"b1}"
- "{?={?=qiIq}{?=qiIq}}16@0:8"
- "{CGPoint=dd}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@16"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\xa1"
- "\xb1"
- "\xd1"
- "\xf0tQ"
- "\xf0\x91"
- "\xf0\xe1"
- "\xf0\xf01"

```
