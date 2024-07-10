## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore`

```diff

-3097.0.148.0.1
-  __TEXT.__text: 0x3218d8
-  __TEXT.__auth_stubs: 0x1a20
-  __TEXT.__objc_methlist: 0x165e8
-  __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x77630
-  __TEXT.__oslogstring: 0x3a1fd
-  __TEXT.__gcc_except_tab: 0x184b8
+3097.0.187.0.4
+  __TEXT.__text: 0x3245fc
+  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__objc_methlist: 0x16700
+  __TEXT.__const: 0x4c8
+  __TEXT.__cstring: 0x77ec0
+  __TEXT.__oslogstring: 0x3a43e
+  __TEXT.__gcc_except_tab: 0x18488
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x8790
-  __TEXT.__objc_classname: 0x2328
-  __TEXT.__objc_methname: 0x3ce7a
-  __TEXT.__objc_methtype: 0x7572
-  __TEXT.__objc_stubs: 0x29f20
-  __DATA_CONST.__got: 0x1640
+  __TEXT.__unwind_info: 0x8800
+  __TEXT.__objc_classname: 0x2364
+  __TEXT.__objc_methname: 0x3d440
+  __TEXT.__objc_methtype: 0x7730
+  __TEXT.__objc_stubs: 0x2a260
+  __DATA_CONST.__got: 0x1670
   __DATA_CONST.__const: 0x1b90
-  __DATA_CONST.__objc_classlist: 0x8e8
+  __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd020
+  __DATA_CONST.__objc_selrefs: 0xd150
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7d8
+  __DATA_CONST.__objc_superrefs: 0x7e0
   __DATA_CONST.__objc_arraydata: 0xf20
-  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x9f28
-  __AUTH_CONST.__cfstring: 0x210e0
-  __AUTH_CONST.__objc_const: 0x39050
-  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__const: 0x9fe8
+  __AUTH_CONST.__cfstring: 0x21640
+  __AUTH_CONST.__objc_const: 0x39768
+  __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x5910
+  __AUTH.__objc_data: 0x5960
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0x1d14
-  __DATA.__data: 0x20c8
+  __DATA.__objc_ivar: 0x1d44
+  __DATA.__data: 0x2128
   __DATA.__bss: 0x560
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
+  - /System/Library/PrivateFrameworks/C2.framework/Versions/A/C2
   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12507
-  Symbols:   27053
-  CStrings:  7214
+  Functions: 12544
+  Symbols:   27161
+  CStrings:  7266
 
Symbols:
+ +[BRCloudTelemetryTTRDecisionRequest requestWithSenderID:ruleID:completionHandler:]
+ +[CKPackage(BRCAdvancedDataProtectionAdditions) br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:error:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) _appLibraryByName:db:]
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) _loadClientStateFromDB:].cold.5
+ -[BRCAccountSessionFPFS(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:]
+ -[BRCClientState _prepareToSaveStateData]
+ -[BRCClientState _stateToData]
+ -[BRCClientState _stateToData].cold.1
+ -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]
+ -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:].cold.1
+ -[BRCClientState initWithDictionary:clientStateData:]
+ -[BRCDocumentItem shouldBeGreedy].cold.2
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
+ -[BRCServerChangesApplier _handleServerItemBRAliasIfNeeded:li:jobID:zone:diffs:].cold.2
+ -[BRCThrottleBase isBlocking]
+ -[BRCUserDefaults idsDecisionServiceURL]
+ -[BRCUserDefaults useIDSDecisionService]
+ -[BRCUserNotification showErrorVolumeNotSupportedWithReason:]
+ -[BRCXPCClient _getCloudDocsUnsupportedError].cold.1
+ -[BRCXPCClient _getCloudDocsUnsupportedError].cold.2
+ -[BRCXPCRegularIPCsClient validateCloudDocsSupportedWithReply:].cold.1
+ -[BRCloudTelemetryTTRDecisionRequest .cxx_destruct]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:_taskIsWaitingForConnection:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:_willRetryBackgroundDataTask:withError:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:dataTask:didReceiveData:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:dataTask:didReceiveResponse:completionHandler:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:_conditionalRequirementsChanged:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:_willSendRequestForEstablishedConnection:completionHandler:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:didCompleteWithError:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:didCompleteWithError:].cold.1
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:needNewBodyStream:]
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:needNewBodyStream:].cold.1
+ -[BRCloudTelemetryTTRDecisionRequest URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]
+ -[BRCloudTelemetryTTRDecisionRequest _initWithSenderID:ruleID:completionHandler:]
+ -[BRCloudTelemetryTTRDecisionRequest networkingDelegate]
+ -[BRCloudTelemetryTTRDecisionRequest resume]
+ -[BRCloudTelemetryTTRDecisionRequest resume].cold.1
+ -[BRCloudTelemetryTTRDecisionRequest setNetworkingDelegate:]
+ -[BRFetchRecordsOperation .cxx_destruct]
+ -[BRFetchRecordsOperation init]
+ -[BRFetchRecordsOperation setFetchRecordsCompletionBlock:]
+ -[NSError(BRCAdditions) brc_ckPartialErrorsByItemID]
+ -[NSError(BRCAdditions) brc_isCloudKitShouldBeUsingEnhancedDrivePrivacyWithFieldName:]
+ BRCGetAccountDSIDForMobileDocsRoot.cold.1
+ GCC_except_table139
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table278
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
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._apsConnection
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._apsQueue
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._completionHandler
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._dataTask
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._decisonServerURL
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._networkingDelegate
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._publicToken
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._responseBody
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._ruleID
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._senderID
+ OBJC_IVAR_$_BRCloudTelemetryTTRDecisionRequest._useDecisionServer
+ OBJC_IVAR_$_BRFetchRecordsOperation._fetchRecordsCompletionBlock
+ _APSConnectionOverrideNamedDelegatePort
+ _OBJC_CLASS_$_BRCloudTelemetryTTRDecisionRequest
+ _OBJC_CLASS_$_BRFetchRecordsOperation
+ _OBJC_CLASS_$_C2RequestManager
+ _OBJC_CLASS_$_C2RequestOptions
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_METACLASS_$_BRCloudTelemetryTTRDecisionRequest
+ _OBJC_METACLASS_$_BRFetchRecordsOperation
+ _OBJC_METACLASS_$_CKFetchRecordsOperation
+ __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.476
+ __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.476.cold.1
+ __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.480
+ __109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.782
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.236
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.236.cold.1
+ __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.240
+ __117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.433
+ __117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.436
+ __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16
+ __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16.cold.1
+ __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16.cold.2
+ __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.23
+ __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.23.cold.1
+ __22-[_BRCOperation start]_block_invoke.95
+ __22-[_BRCOperation start]_block_invoke.95.cold.1
+ __39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.105
+ __43-[_BRCOperation completedWithResult:error:]_block_invoke.114
+ __43-[_BRCOperation completedWithResult:error:]_block_invoke.115
+ __45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.368
+ __45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.368.cold.1
+ __46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.507
+ __46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.381
+ __47-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke.2
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.1
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.2
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.3
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.4
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.5
+ __48-[BRCAccountWaitOperation _accountChangeHandler]_block_invoke.25.cold.6
+ __48-[BRCXPCRegularIPCsClient willAcceptShareAtURL:]_block_invoke.798
+ __48-[BRCXPCRegularIPCsClient willAcceptShareAtURL:]_block_invoke.798.cold.1
+ __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.241
+ __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.241.cold.1
+ __53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.578
+ __54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.465
+ __54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.466
+ __54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.496
+ __54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.499
+ __54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.448
+ __55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.856
+ __55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.857
+ __56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.415
+ __56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.418
+ __56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.803
+ __56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.803.cold.1
+ __56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.313
+ __56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.319
+ __56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.322
+ __57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.393
+ __57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.396
+ __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.538
+ __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.538.cold.1
+ __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.548
+ __58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.477
+ __58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.478
+ __58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.495
+ __58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.495.cold.1
+ __60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.743
+ __60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.743.cold.1
+ __62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.732
+ __63-[BRCXPCRegularIPCsClient _t_getEntitlementsForBundleID:reply:]_block_invoke.844
+ __64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.447
+ __65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.338
+ __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.790
+ __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.790.cold.1
+ __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.790.cold.2
+ __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.791
+ __66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.746
+ __66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.748
+ __67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.794
+ __67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.483
+ __67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.483.cold.1
+ __68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.373
+ __69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.342
+ __69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.467
+ __70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.123
+ __71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.851
+ __71-[BRCXPCRegularIPCsClient _t_getEntitledContainerIDsForBundleID:reply:]_block_invoke.847
+ __71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.786
+ __72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.735
+ __72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.725
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.34
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.36
+ __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.35
+ __73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.468
+ __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.457.cold.1
+ __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.460
+ __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.460.cold.1
+ __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.461
+ __73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.802
+ __73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.419
+ __73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.434
+ __73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.690
+ __73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.692
+ __74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.755
+ __74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.757
+ __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.449
+ __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.449.cold.1
+ __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.449.cold.2
+ __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.452
+ __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.452.cold.1
+ __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.749
+ __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.750
+ __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.754
+ __76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.741
+ __76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.741.cold.1
+ __76-[BRCXPCRegularIPCsClient iCloudDesktopSettingsChangedWithAttributes:reply:]_block_invoke.366
+ __76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.687
+ __76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.730
+ __77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.473
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26.cold.1
+ __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.26.cold.2
+ __80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.675
+ __80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.365
+ __80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.500
+ __80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.501
+ __81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.778
+ __81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.689
+ __81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.780
+ __81-[BRCloudTelemetryTTRDecisionRequest _initWithSenderID:ruleID:completionHandler:]_block_invoke.cold.1
+ __84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.603
+ __84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.609
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.582
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.582.cold.1
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.582.cold.2
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.582.cold.3
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.586
+ __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.600
+ __84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.784
+ __85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.536
+ __85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.537
+ __86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.610
+ __86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.616
+ __87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.330
+ __87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.333
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.338
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.338.cold.1
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.342
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.342.cold.1
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355.cold.1
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.355.cold.2
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.356
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.cold.1
+ __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2.cold.2
+ __88-[BRCXPCRegularIPCsClient _getPublishedURLForLocalItem:forStreaming:requestedTTL:reply:]_block_invoke.621
+ __88-[BRCXPCRegularIPCsClient _getPublishedURLForLocalItem:forStreaming:requestedTTL:reply:]_block_invoke.625
+ __88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.694
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.699
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.700
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.701
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.706
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.717
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.718
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.719
+ __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.713
+ __91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.770
+ __93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.398
+ __93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.401
+ __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.405
+ __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.406
+ __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.408
+ __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.821
+ __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.825
+ __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.835
+ __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.841
+ __OBJC_$_CLASS_METHODS_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_$_INSTANCE_METHODS_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_$_INSTANCE_METHODS_BRFetchRecordsOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_$_INSTANCE_VARIABLES_BRFetchRecordsOperation
+ __OBJC_$_PROP_LIST_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_C2RequestDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_C2RequestDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_C2RequestDelegate
+ __OBJC_$_PROTOCOL_REFS_C2RequestDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_CLASS_RO_$_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_CLASS_RO_$_BRFetchRecordsOperation
+ __OBJC_LABEL_PROTOCOL_$_C2RequestDelegate
+ __OBJC_METACLASS_RO_$_BRCloudTelemetryTTRDecisionRequest
+ __OBJC_METACLASS_RO_$_BRFetchRecordsOperation
+ __OBJC_PROTOCOL_$_C2RequestDelegate
+ ___31-[BRFetchRecordsOperation init]_block_invoke
+ ___61-[BRCUserNotification showErrorVolumeNotSupportedWithReason:]_block_invoke
+ ___70-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]_block_invoke
+ ___81-[BRCloudTelemetryTTRDecisionRequest _initWithSenderID:ruleID:completionHandler:]_block_invoke
+ ___84-[BRCDownloadContent _stageWithDownloadStager:manifest:package:xattrsPackage:error:]_block_invoke
+ ___88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96s_e23_v16?0"PQLConnection"8l
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e32_v28?0"NSArray"8B16"NSError"20l
+ ___block_descriptor_41_e8_32s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e57_v36?0"BRCDocumentItem"8"BRCServerItem"16"NSData"24B32l
+ ___block_descriptor_92_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ __block_literal_global.1771
+ __block_literal_global.1783
+ __block_literal_global.1949
+ __block_literal_global.2129
+ __block_literal_global.2164
+ __block_literal_global.2175
+ __block_literal_global.219
+ __block_literal_global.231
+ __block_literal_global.2440
+ __block_literal_global.2455
+ __block_literal_global.2540
+ __block_literal_global.280
+ __block_literal_global.2818
+ __block_literal_global.2883
+ __block_literal_global.320
+ __block_literal_global.345
+ __block_literal_global.359
+ __block_literal_global.432
+ __block_literal_global.443
+ __block_literal_global.448
+ __block_literal_global.465
+ __block_literal_global.482
+ __block_literal_global.487
+ __block_literal_global.492
+ __block_literal_global.497
+ __block_literal_global.502
+ __block_literal_global.507
+ __block_literal_global.512
+ __block_literal_global.517
+ __block_literal_global.525
+ __block_literal_global.530
+ __block_literal_global.535
+ __block_literal_global.796
+ _br_update_tables_32_000
+ _objc_msgSend$_appLibraryByName:db:
+ _objc_msgSend$_createStructureRecordForParentItem
+ _objc_msgSend$_createStructureRecordWithRecordID:serverItem:
+ _objc_msgSend$_initWithSenderID:ruleID:completionHandler:
+ _objc_msgSend$_prepareToSaveStateData
+ _objc_msgSend$_saltChildRecordFields:serverItem:basehashSalt:
+ _objc_msgSend$_stateToData
+ _objc_msgSend$appendData:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:error:
+ _objc_msgSend$br_isExcludedFromSyncInFPFSIsFile:
+ _objc_msgSend$br_setIOPolicy:type:forBlock:
+ _objc_msgSend$brc_ckPartialErrorsByItemID
+ _objc_msgSend$brc_isCloudKitShouldBeUsingEnhancedDrivePrivacyWithFieldName:
+ _objc_msgSend$checkDomainsCanBeStored:onVolumeAtURL:unsupportedReason:error:
+ _objc_msgSend$createDataTaskWithRequest:options:delegate:sessionHandle:
+ _objc_msgSend$hasStateChangesAndClearSaveStatusWithResultingState:
+ _objc_msgSend$idsDecisionServiceURL
+ _objc_msgSend$initWithDictionary:clientStateData:
+ _objc_msgSend$initWithParentItem:sessionContext:
+ _objc_msgSend$networkingDelegate
+ _objc_msgSend$newAppLibraryFromPQLResultSet:version:
+ _objc_msgSend$recordIDs
+ _objc_msgSend$requestWithSenderID:ruleID:completionHandler:
+ _objc_msgSend$response
+ _objc_msgSend$setCanSyncDownBeforeRetry:
+ _objc_msgSend$setHTTPBody:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setNetworkingDelegate:
+ _objc_msgSend$setTlsPinning:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$set_allowsExpensiveAccess:
+ _objc_msgSend$set_appleIDContextSessionIdentifier:
+ _objc_msgSend$showErrorVolumeNotSupportedWithReason:
+ _objc_msgSend$statusCode
+ _objc_msgSend$useIDSDecisionService
+ _objc_msgSend$valueForHTTPHeaderField:
- +[BRCAccountSessionFPFS(BRCDatabaseManager) upgradeOfflineDB:serverTruth:session:error:].cold.2
- +[CKPackage(BRCAdvancedDataProtectionAdditions) br_clonedPackageWithRecordID:databaseScope:fieldName:boundaryKey:signature:error:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) _createSharedAppLibrary:]
- -[BRCAccountSessionFPFS(BRCDatabaseManager) newAppLibraryFromPQLResultSet:version:error:]
- -[BRCClientState initWithDictionary:]
- -[BRCClientZone(BRCBaseHashSaltAdditions) childBaseSaltForItemID:].cold.2
- -[BRCConstantThrottle incrementRetryCount:]
- -[BRCConstantThrottle initWithName:andRetryBackoff:]
- -[BRCConstantThrottle nsecsToNextRetry:now:increment:]
- -[BRCConstantThrottle nsecsToNextRetry:retryCount:now:]
- -[BRCConstantThrottle reset]
- -[BRCFSUploader _handleCollaborationUploadError:recordID:clientZone:reply:].cold.1
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
- __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.467
- __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.467.cold.1
- __100-[BRCAccountSessionFPFS(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.471
- __109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.779
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.237
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.237.cold.1
- __116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.241
- __117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.424
- __117-[BRCAccountSessionFPFS(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.427
- __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.14.cold.2
- __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.21
- __188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.21.cold.1
- __22-[_BRCOperation start]_block_invoke.92
- __22-[_BRCOperation start]_block_invoke.92.cold.1
- __39-[BRCXPCClient _setupAppLibrary:error:]_block_invoke.101
- __43-[_BRCOperation completedWithResult:error:]_block_invoke.111
- __43-[_BRCOperation completedWithResult:error:]_block_invoke.112
- __45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.364
- __45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.364.cold.1
- __46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.503
- __46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.377
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
- __48-[BRCXPCRegularIPCsClient willAcceptShareAtURL:]_block_invoke.795
- __48-[BRCXPCRegularIPCsClient willAcceptShareAtURL:]_block_invoke.795.cold.1
- __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.242
- __51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.242.cold.1
- __53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.575
- __54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.461
- __54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.462
- __54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.492
- __54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.495
- __54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.444
- __55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.853
- __55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.854
- __56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.411
- __56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.414
- __56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.800
- __56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.800.cold.1
- __56-[BRCXPCRegularIPCsClient presyncContainerWithID:reply:]_block_invoke.309
- __56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.315
- __56-[BRCXPCRegularIPCsClient updateContainerMetadataForID:]_block_invoke.318
- __57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.389
- __57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.392
- __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.534
- __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.534.cold.1
- __58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.542
- __58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.473
- __58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.474
- __58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.491
- __58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.491.cold.1
- __60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.740
- __60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.740.cold.1
- __62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.729
- __63-[BRCXPCRegularIPCsClient _t_getEntitlementsForBundleID:reply:]_block_invoke.841
- __64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.443
- __65-[BRCXPCRegularIPCsClient getItemUpdateSenderWithReceiver:reply:]_block_invoke.334
- __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.787
- __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.787.cold.1
- __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.787.cold.2
- __65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.788
- __66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.742
- __66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.743
- __67-[BRCXPCRegularIPCsClient _presentAcceptDialogsWithMetadata:reply:]_block_invoke.791
- __67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.479
- __67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.479.cold.1
- __68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.369
- __69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.338
- __69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.463
- __70-[_BRCOperation addSubOperation:overrideContext:allowsCellularAccess:]_block_invoke.120
- __71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.848
- __71-[BRCXPCRegularIPCsClient _t_getEntitledContainerIDsForBundleID:reply:]_block_invoke.844
- __71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.783
- __72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.732
- __72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.722
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.35
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke.37
- __73-[BRCSyncUpOperation _performPCSChainOperationIfNecessaryWithCompletion:]_block_invoke_2.36
- __73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.464
- __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.453
- __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.453.cold.1
- __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.456
- __73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.456.cold.1
- __73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.799
- __73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.415
- __73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.430
- __73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.687
- __73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.689
- __74-[BRCSyncUpOperation _performModifyRecordsOrBatchOperationWithCompletion:]_block_invoke.45.cold.8
- __74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.752
- __74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.754
- __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.445
- __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.445.cold.1
- __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.445.cold.2
- __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.448
- __75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.448.cold.1
- __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.746
- __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.747
- __75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.751
- __76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.738
- __76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.738.cold.1
- __76-[BRCXPCRegularIPCsClient iCloudDesktopSettingsChangedWithAttributes:reply:]_block_invoke.362
- __76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.684
- __76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.727
- __77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.469
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.27.cold.1
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.27.cold.2
- __80-[BRCSyncUpOperation _performMetadataSaltingOperationIfNecessaryWithCompletion:]_block_invoke.28
- __80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.672
- __80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.361
- __80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.496
- __80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.497
- __81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.775
- __81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.686
- __81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.777
- __84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.600
- __84-[BRCXPCRegularIPCsClient enumerateAllFoldersWithSortOrder:offset:limit:completion:]_block_invoke.606
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.579
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.579.cold.1
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.579.cold.2
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.579.cold.3
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.583
- __84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.597
- __84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.781
- __85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.532
- __85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.533
- __86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.607
- __86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.613
- __87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.326
- __87-[BRCXPCRegularIPCsClient deleteAllContentsOfContainerID:onClient:onServer:wait:reply:]_block_invoke.329
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.328
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.328.cold.1
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.332
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.332.cold.1
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.345
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.345.cold.1
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.345.cold.2
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.346
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.350
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.350.cold.1
- __88-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke.350.cold.2
- __88-[BRCXPCRegularIPCsClient _getPublishedURLForLocalItem:forStreaming:requestedTTL:reply:]_block_invoke.618
- __88-[BRCXPCRegularIPCsClient _getPublishedURLForLocalItem:forStreaming:requestedTTL:reply:]_block_invoke.622
- __88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.691
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.694
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.695
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.696
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.703
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.709
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.714
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.716
- __90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.710
- __91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.767
- __93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.393
- __93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.394
- __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.400
- __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.401
- __94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.402
- __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.818
- __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.822
- __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.832
- __95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.838
- __OBJC_$_INSTANCE_METHODS_BRCConstantThrottle
- __OBJC_$_INSTANCE_VARIABLES_BRCConstantThrottle
- __OBJC_CLASS_RO_$_BRCConstantThrottle
- __OBJC_METACLASS_RO_$_BRCConstantThrottle
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs_e17_v16?0"NSError"8l
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112s_e23_v16?0"PQLConnection"8l
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40w_e23_v16?0"PQLConnection"8l
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e79_v52?0"BRCDocumentItem"8"BRCServerItem"16"NSData"24"NSData"32"NSData"40B48l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
- __block_literal_global.1777
- __block_literal_global.1789
- __block_literal_global.1955
- __block_literal_global.2135
- __block_literal_global.2176
- __block_literal_global.2181
- __block_literal_global.232
- __block_literal_global.234
- __block_literal_global.236
- __block_literal_global.2446
- __block_literal_global.2461
- __block_literal_global.2546
- __block_literal_global.2824
- __block_literal_global.2880
- __block_literal_global.304
- __block_literal_global.346
- __block_literal_global.349
- __block_literal_global.423
- __block_literal_global.434
- __block_literal_global.439
- __block_literal_global.456
- __block_literal_global.473
- __block_literal_global.478
- __block_literal_global.483
- __block_literal_global.488
- __block_literal_global.493
- __block_literal_global.498
- __block_literal_global.503
- __block_literal_global.508
- __block_literal_global.516
- __block_literal_global.521
- __block_literal_global.526
- __block_literal_global.793
- _fpfs_path_is_safe_save_temp_file_ext
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
- _objc_msgSend$newAppLibraryFromPQLResultSet:version:error:
- _setiopolicy_np
CStrings:
+ " next-try:%!@(MISSING) ago"
+ "-[BRCAccountSessionFPFS(BRCDatabaseManager) _finishClientTruthConnectionSetupWithError:]_block_invoke_2"
+ "-[BRCClientState _stateToData]"
+ "-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]"
+ "-[BRCDownloadContent _stageWithDownloadStager:manifest:package:xattrsPackage:error:]_block_invoke"
+ "-[BRCSaltingBatchOperation _createStructureRecordForParentItem]"
+ "-[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:]"
+ "-[BRCSaltingBatchOperation _saltChildRecordFields:serverItem:basehashSalt:]"
+ "-[BRCSaltingBatchOperation initWithParentItem:sessionContext:]"
+ "-[BRCXPCClient _getCloudDocsUnsupportedError]"
+ "-[BRCloudTelemetryTTRDecisionRequest URLSession:task:didCompleteWithError:]"
+ "-[BRCloudTelemetryTTRDecisionRequest URLSession:task:needNewBodyStream:]"
+ "-[BRCloudTelemetryTTRDecisionRequest _initWithSenderID:ruleID:completionHandler:]_block_invoke"
+ "-[BRCloudTelemetryTTRDecisionRequest resume]"
+ "-[BRFetchRecordsOperation init]_block_invoke"
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
+ "Accept"
+ "BRCGetAccountDSIDForMobileDocsRoot"
+ "BRCloudTelemetryTTRDecisionRequest not initialized correctly"
+ "Content-Type"
+ "Empty response body"
+ "Error while unarchiving client state %!@(MISSING)"
+ "Failed building request body JSON"
+ "Failed creating C2 DataTask"
+ "Failed encoding public APS token"
+ "Failed initializing C2RequestOptions"
+ "Failed initializing NSMutableURLRequest"
+ "HTTP request failed: %!l(MISSING)d"
+ "ICLOUD_DRIVE_VOLUME_NOT_SUPPORTED_ALERT_TITLE"
+ "ICLOUD_DRIVE_VOLUME_NOT_SUPPORTED_NON_APFS_ALERT_MESSAGE"
+ "ICLOUD_DRIVE_VOLUME_NOT_SUPPORTED_NON_LOCAL_ALERT_MESSAGE"
+ "ICLOUD_DRIVE_VOLUME_NOT_SUPPORTED_OK_BUTTON"
+ "Invalid response Content-Type"
+ "Invalid response body"
+ "Invalid response type"
+ "Missing response Content-Type"
+ "Missing show TTR info"
+ "POST"
+ "PUSH_TOKEN_BASE_64"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid FROM app_libraries WHERE app_library_name = %!@(MISSING)"
+ "SELECT rowid, app_library_name, app_library_plist, zone_rowid, child_basehash_salt, salting_state FROM app_libraries WHERE app_library_name = %!@(MISSING)"
+ "Unexpected empty response from service"
+ "Unexpected error while converting client state to data!"
+ "Unexpected show TTR info type"
+ "Unexpected show TTR reason"
+ "X-Apple-Request-UUID"
+ "X-Apple-Splunk-Hint"
+ "application/json"
+ "br_update_tables_32_000"
+ "com.apple.rtctaptoradar"
+ "com.apple.rtctaptoradar.pushtokenprovider"
+ "data scope"
+ "force"
+ "https://support.ess.apple.com/WebObjects/SupportService.woa/internal/checkTapToRadarDecision"
+ "ruleId"
+ "senderId"
+ "showTTR"
+ "tapToRadarDeviceLookupIdentifier"
+ "ttr.force"
+ "ttr.ids.decision.service.url"
+ "ttr.use.ids.decision.service"
+ "unsupportedReason"
+ "v24@?0B8B12@\"NSError\"16"
+ "v28@?0@\"NSArray\"8B16@\"NSError\"20"
+ "v36@?0@\"BRCDocumentItem\"8@\"BRCServerItem\"16@\"NSData\"24B32"
- " not"
- "-[BRCAccountWaitOperation initWithCKContainer:]_block_invoke"
- "-[BRCDownloadContent _stageWithDownloadStager:manifest:package:xattrsPackage:error:]"
- "-[BRCSaltingBatchOperation _createStructureRecordForRootItem]"
- "-[BRCSaltingBatchOperation _createStructureRecordWithRecordID:serverItem:basehashSalt:]"
- "-[BRCSaltingBatchOperation initWithRootItem:sessionContext:]"
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
- "account-waiter-error-retry-backoff"
- "account-waiter-refetch-pacer"
- "account-waiter-refresh-delay"
- "com.apple.bird.account-waiter-refresh-queue"
- "n't"
- "v52@?0@\"BRCDocumentItem\"8@\"BRCServerItem\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40B48"

```
