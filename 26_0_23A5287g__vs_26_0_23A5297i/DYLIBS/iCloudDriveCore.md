## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4210.0.0.0.1
-  __TEXT.__text: 0x30bd6c
+4250.0.0.0.2
+  __TEXT.__text: 0x30d05c
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x19dec
+  __TEXT.__objc_methlist: 0x19ee4
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7cf1a
-  __TEXT.__oslogstring: 0x3bd93
-  __TEXT.__gcc_except_tab: 0x1a240
+  __TEXT.__cstring: 0x7d0bd
+  __TEXT.__oslogstring: 0x3be6c
+  __TEXT.__gcc_except_tab: 0x1a21c
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9e40
-  __TEXT.__objc_classname: 0x2a75
-  __TEXT.__objc_methname: 0x43a09
-  __TEXT.__objc_methtype: 0x8edb
-  __TEXT.__objc_stubs: 0x2ea20
-  __DATA_CONST.__got: 0x16e0
-  __DATA_CONST.__const: 0x9578
-  __DATA_CONST.__objc_classlist: 0xa40
+  __TEXT.__unwind_info: 0x9ea0
+  __TEXT.__objc_classname: 0x2a7e
+  __TEXT.__objc_methname: 0x43d35
+  __TEXT.__objc_methtype: 0x8f19
+  __TEXT.__objc_stubs: 0x2ec80
+  __DATA_CONST.__got: 0x16f8
+  __DATA_CONST.__const: 0x95c8
+  __DATA_CONST.__objc_classlist: 0xa48
   __DATA_CONST.__objc_catlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x290
+  __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe4c8
+  __DATA_CONST.__objc_selrefs: 0xe560
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x8f8
+  __DATA_CONST.__objc_superrefs: 0x908
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x2b78
-  __AUTH_CONST.__cfstring: 0x22620
-  __AUTH_CONST.__objc_const: 0x3ce10
-  __AUTH_CONST.__objc_intobj: 0xb88
+  __AUTH_CONST.__const: 0x2b58
+  __AUTH_CONST.__cfstring: 0x22760
+  __AUTH_CONST.__objc_const: 0x3ccd0
+  __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x27b0
+  __AUTH.__objc_data: 0x2800
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f3c
-  __DATA.__data: 0x27a0
-  __DATA.__bss: 0x230
+  __DATA.__objc_ivar: 0x1f58
+  __DATA.__data: 0x2740
+  __DATA.__bss: 0x238
   __DATA_DIRTY.__objc_data: 0x3ed0
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x3f0
+  __DATA_DIRTY.__bss: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9F64FC81-9904-3B94-99DC-DE2D12CFB8B8
-  Functions: 13490
-  Symbols:   43921
-  CStrings:  27513
+  UUID: CE464469-C3BA-3BB2-AE86-E0E25BA0DABF
+  Functions: 13515
+  Symbols:   44008
+  CStrings:  27564
 
Symbols:
+ +[CKOperationGroup(BRAdditions) br_primeMMCSCache]
+ -[BRCAccountSession(BRCDatabaseManager) _isCZMAccountBasedOnCloudDocsPlistState]
+ -[BRCAccountSession(BRCDatabaseManager) _updateDomain:withUserInfo:error:]
+ -[BRCAccountSession(BRCDatabaseManager) _updateDomain:withUserInfo:error:].cold.1
+ -[BRCAccountSession(BRCDatabaseManager) accountStartedSchedulingCZM]
+ -[BRCAutoBugCaptureReporter .cxx_destruct]
+ -[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:]
+ -[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:].cold.1
+ -[BRCAutoBugCaptureReporter _init]
+ -[BRCClientDatabaseFacade fetchAppLibraryPlist:]
+ -[BRCClientState dataPendingSave]
+ -[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]
+ -[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.1
+ -[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.2
+ -[BRCClientZone locateContentRecordIfNecessaryForItem:isUserWaiting:maxOperationBackoff:]
+ -[BRCClientZone scheduleSyncDownForOOBModifyRecordsAckForItemID:]
+ -[BRCDeviceConfiguration _primeMMCSCacheWithFacade:]
+ -[BRCLocalItem isMarkedForOOBSync]
+ -[BRCLocateRecordOperation itemMarkedForOOBSync:]
+ -[BRCPrimeMMCSCacheOperation .cxx_destruct]
+ -[BRCPrimeMMCSCacheOperation initWithExistingContentsURL:item:sessionContext:]
+ -[BRCPrimeMMCSCacheOperation main]
+ -[BRCPrimeMMCSCacheOperation main].cold.1
+ -[BRCPrimeMMCSCacheOperation shouldRetryForError:]
+ -[BRCServerPersistedState _dataPendingSave]
+ -[BRCServerPersistedState _stateToData].cold.1
+ -[BRCUserDefaults applyNonDocumentsOnLocateRecord]
+ -[BRCUserDefaults populateFPDomainExperimentID]
+ -[BRCUserDefaults shouldPrimeMMCSCacheBeforeDownloadWithAccountFacade:]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _createFileProvidingRequestOperationOfFileObject:existingContents:localItem:etagIfLoser:etagToDownload:progress:options:reply:].cold.4
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]
+ GCC_except_table129
+ GCC_except_table156
+ GCC_except_table162
+ GCC_except_table182
+ GCC_except_table188
+ GCC_except_table249
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table268
+ GCC_except_table325
+ GCC_except_table357
+ GCC_except_table417
+ GCC_except_table422
+ GCC_except_table569
+ _NSFileProviderUserInfoExperimentIDKey
+ _OBJC_CLASS_$_BRCPrimeMMCSCacheOperation
+ _OBJC_CLASS_$_BRCloudDocsHelper
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_IVAR_$_BRCAutoBugCaptureReporter._reporterOperationRejectedThrottle
+ _OBJC_IVAR_$_BRCAutoBugCaptureReporter._reporterOperationRejectedThrottlePeriod
+ _OBJC_IVAR_$_BRCLocateRecordOperation._itemID
+ _OBJC_IVAR_$_BRCLocateRecordOperation._itemMarkedForOOBSyncWhileRunning
+ _OBJC_IVAR_$_BRCPrimeMMCSCacheOperation._boundaryKey
+ _OBJC_IVAR_$_BRCPrimeMMCSCacheOperation._existingContents
+ _OBJC_IVAR_$_BRCPrimeMMCSCacheOperation._record
+ _OBJC_METACLASS_$_BRCPrimeMMCSCacheOperation
+ _OBJC_METACLASS_$_BRCloudDocsHelper
+ __OBJC_$_INSTANCE_METHODS_BRCPrimeMMCSCacheOperation
+ __OBJC_$_INSTANCE_VARIABLES_BRCAutoBugCaptureReporter
+ __OBJC_$_INSTANCE_VARIABLES_BRCPrimeMMCSCacheOperation
+ __OBJC_$_PROP_LIST_BRCPrimeMMCSCacheOperation
+ __OBJC_CLASS_PROTOCOLS_$_BRCPrimeMMCSCacheOperation
+ __OBJC_CLASS_RO_$_BRCPrimeMMCSCacheOperation
+ __OBJC_METACLASS_RO_$_BRCPrimeMMCSCacheOperation
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.160
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.160.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.128
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.110
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.110.cold.1
+ ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.112
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.134
+ ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.134.cold.1
+ ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.142
+ ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.652
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100.cold.1
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.100.cold.2
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.105
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.105.cold.1
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.107
+ ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.107.cold.1
+ ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.137
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.354
+ ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.355
+ ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke
+ ___123-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke.140
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.191
+ ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.114
+ ___33-[BRCClientState dataPendingSave]_block_invoke
+ ___34-[BRCPrimeMMCSCacheOperation main]_block_invoke
+ ___34-[BRCPrimeMMCSCacheOperation main]_block_invoke.cold.1
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.335
+ ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.335.cold.1
+ ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.458
+ ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.344
+ ___51-[BRCLocateRecordOperation finishWithResult:error:]_block_invoke
+ ___51-[BRCLocateRecordOperation finishWithResult:error:]_block_invoke_2
+ ___51-[BRCLocateRecordOperation finishWithResult:error:]_block_invoke_3
+ ___51-[BRCLocateRecordOperation finishWithResult:error:]_block_invoke_4
+ ___51-[BRCLocateRecordOperation finishWithResult:error:]_block_invoke_5
+ ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.508
+ ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.412
+ ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.452
+ ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.442
+ ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.442.cold.1
+ ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.399
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.723
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.727
+ ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.370
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.674
+ ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.674.cold.1
+ ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.354
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.470
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.470.cold.1
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.477
+ ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.479
+ ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.421
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440
+ ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.440.cold.1
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.620
+ ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.620.cold.1
+ ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.615
+ ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.398
+ ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.672
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.668.cold.1
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.668.cold.2
+ ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.669
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.623
+ ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.625
+ ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.123
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.429
+ ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.429.cold.1
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke.81
+ ___68-[BRCAccountSession(BRCZoneMigration) scheduleZoneMovesToCloudDocs:]_block_invoke_2.82
+ ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.337
+ ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.320
+ ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.413
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.656
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.659
+ ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.659.cold.1
+ ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.718
+ ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.664
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.115
+ ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.119
+ ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.616
+ ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.610
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.189
+ ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.414
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.406.cold.1
+ ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.407
+ ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.673
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.371
+ ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.387
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.585
+ ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.587
+ ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.193
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.629
+ ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.631
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.400.cold.2
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401
+ ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.401.cold.1
+ ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.627
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.618
+ ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.618.cold.1
+ ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.582
+ ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.613
+ ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.418
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.154
+ ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.357
+ ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.573
+ ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.333
+ ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.454
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.648
+ ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.584
+ ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.650
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.1
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.2
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.510.cold.3
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.514
+ ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.524
+ ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.711
+ ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.654
+ ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.469
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.176
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.182
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.150
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.525
+ ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.527
+ ___87-[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke
+ ___87-[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke_2
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.120
+ ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.122
+ ___88-[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:]_block_invoke
+ ___88-[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:]_block_invoke.cold.1
+ ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.589
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke.94
+ ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.136
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.156
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.163
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.596
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.599
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.601
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.606
+ ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.602
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.157
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.183
+ ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.640
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.144
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.144.cold.1
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.139
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.149
+ ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.360
+ ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.686
+ ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.364
+ ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.446
+ ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.446.cold.1
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.699
+ ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.707
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.152
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.397
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.397.cold.1
+ ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.401
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.168
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.138
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e34_v24?0"BRCLocalItem"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56w_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8w56l8s40l8s48l8
+ ___block_literal_global.117
+ ___block_literal_global.162
+ ___block_literal_global.353
+ ___block_literal_global.370
+ ___block_literal_global.387
+ ___block_literal_global.403
+ ___block_literal_global.413
+ ___block_literal_global.418
+ ___block_literal_global.423
+ ___block_literal_global.428
+ ___block_literal_global.433
+ ___block_literal_global.438
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.456
+ ___block_literal_global.661
+ ___block_literal_global.683
+ _objc_msgSend$_captureLogsForOperationType:ofSubtype:withContext:timeout:
+ _objc_msgSend$_dataPendingSave
+ _objc_msgSend$_isCZMAccountBasedOnCloudDocsPlistState
+ _objc_msgSend$_locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:
+ _objc_msgSend$_primeMMCSCacheWithFacade:
+ _objc_msgSend$_refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:
+ _objc_msgSend$_updateDomain:withUserInfo:error:
+ _objc_msgSend$accountStartedSchedulingCZM
+ _objc_msgSend$appProtectionHidden
+ _objc_msgSend$applicationState
+ _objc_msgSend$applyNonDocumentsOnLocateRecord
+ _objc_msgSend$br_primeMMCSCache
+ _objc_msgSend$dataPendingSave
+ _objc_msgSend$fetchAppLibraryPlist:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithExistingContentsURL:item:sessionContext:
+ _objc_msgSend$isMarkedForOOBSync
+ _objc_msgSend$itemMarkedForOOBSync:
+ _objc_msgSend$locateContentRecordIfNecessaryForItem:isUserWaiting:maxOperationBackoff:
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$populateFPDomainExperimentID
+ _objc_msgSend$queryFastPathsForPrimaryPersona:
+ _objc_msgSend$scheduleSyncDownForOOBModifyRecordsAckForItemID:
+ _objc_msgSend$shouldPrimeMMCSCacheBeforeDownloadWithAccountFacade:
+ _objc_msgSend$snapshotWithSignature:delay:events:payload:actions:reply:
+ _scheduleZoneMovesToCloudDocs:.onceToken
- -[BRCAccountSession(BRCDatabaseManager) _decorateUserInfoForFPFSDomain:panicOnDomainIDMismatch:withError:].cold.1
- -[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:].cold.1
- -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]
- -[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:].cold.1
- -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]
- -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.1
- -[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:].cold.2
- -[BRCClientZone scheduleSyncDownForOOBModifyRecordsAck]
- -[BRCServerPersistedState _hasStateChangesWithResultingState:]
- -[BRCServerPersistedState _hasStateChangesWithResultingState:].cold.1
- -[BRCSyncUpOperation prepareWithMaxCost:retryAfter:].cold.9
- GCC_except_table115
- GCC_except_table140
- GCC_except_table148
- GCC_except_table152
- GCC_except_table163
- GCC_except_table178
- GCC_except_table179
- GCC_except_table205
- GCC_except_table212
- GCC_except_table242
- GCC_except_table248
- GCC_except_table254
- GCC_except_table258
- GCC_except_table262
- GCC_except_table267
- GCC_except_table271
- GCC_except_table277
- GCC_except_table281
- GCC_except_table318
- GCC_except_table324
- GCC_except_table356
- GCC_except_table358
- GCC_except_table385
- GCC_except_table414
- GCC_except_table416
- GCC_except_table566
- _OBJC_CLASS_$_LSBundleProxy
- __OBJC_$_PROP_LIST_BRDaemonCloudDocsHelper
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRCloudDocsHelper
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRCloudDocsHelper
- __OBJC_$_PROTOCOL_REFS_BRCloudDocsHelper
- __OBJC_CLASS_PROTOCOLS_$_BRDaemonCloudDocsHelper
- __OBJC_LABEL_PROTOCOL_$_BRCloudDocsHelper
- __OBJC_PROTOCOL_$_BRCloudDocsHelper
- ___103-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke
- ___103-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.140
- ___103-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.141
- ___103-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.142
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.161
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.161.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) capabilityWhenTryingToReparentItemIdentifier:toNewParent:reply:]_block_invoke.127
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.109
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.109.cold.1
- ___105-[BRCXPCRegularIPCsClient(FPFSAdditions) deleteItemWithIdentifier:baseVersion:options:completionHandler:]_block_invoke.111
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.133
- ___107-[BRCXPCRegularIPCsClient(FPFSAdditions) getPublishedURLForItemIdentifier:forStreaming:requestedTTL:reply:]_block_invoke.133.cold.1
- ___108-[BRCXPCRegularIPCsClient(FPFSAdditions) _fetchLatestContentRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke.144
- ___109-[BRCXPCRegularIPCsClient startOperation:toProcessSubitemsWithItemID:maxSubsharesFailures:processType:reply:]_block_invoke.651
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.103
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.103.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.106
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.106.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.99
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.99.cold.1
- ___109-[BRCXPCRegularIPCsClient(FPFSAdditions) startDownloadFileObject:existingContents:options:etagIfLoser:reply:]_block_invoke.99.cold.2
- ___110-[BRCXPCRegularIPCsClient(FPFSAdditions) setiWorkPublishingInfoForItemIdentifier:isForPublish:readonly:reply:]_block_invoke.136
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke.348
- ___113-[BRCAccountSession(BRCDatabaseManager) initializeOfflineDatabaseWhileUpgrading:loadClientState:forDBDump:error:]_block_invoke_2.349
- ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.192
- ___130-[BRCXPCRegularIPCsClient(FPFSAdditions) modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:]_block_invoke.112
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.334
- ___45-[BRCXPCRegularIPCsClient getContainersByID:]_block_invoke.334.cold.1
- ___46-[BRCXPCRegularIPCsClient getSyncState:reply:]_block_invoke.457
- ___46-[BRCXPCRegularIPCsClient resetBudgets:reply:]_block_invoke.343
- ___53-[BRCXPCRegularIPCsClient currentNotifRankWithReply:]_block_invoke.507
- ___54-[BRCXPCRegularIPCsClient forceSyncContainerID:reply:]_block_invoke.410
- ___54-[BRCXPCRegularIPCsClient getContainersNeedingUpload:]_block_invoke.450
- ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.441
- ___54-[BRCXPCRegularIPCsClient userVerifiedTermsWithReply:]_block_invoke.441.cold.1
- ___54-[BRCXPCRegularIPCsClient zoneNameForContainer:reply:]_block_invoke.398
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.722
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.726
- ___56-[BRCXPCRegularIPCsClient dumpCoordinationInfoTo:reply:]_block_invoke.368
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.673
- ___56-[BRCXPCRegularIPCsClient keepDataLocalOnSignOut:reply:]_block_invoke.673.cold.1
- ___57-[BRCXPCRegularIPCsClient printStatus:containerID:reply:]_block_invoke.352
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.469
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.469.cold.1
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.476
- ___58-[BRCXPCRegularIPCsClient resolveBookmarkDataToURL:reply:]_block_invoke.478
- ___58-[BRCXPCRegularIPCsClient resumeSyncConsistencyWithReply:]_block_invoke.419
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.439
- ___58-[BRCXPCRegularIPCsClient updateAccountDisplayName:reply:]_block_invoke.439.cold.1
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.619
- ___60-[BRCXPCRegularIPCsClient createSharingInfoForItemID:reply:]_block_invoke.619.cold.1
- ___62-[BRCXPCRegularIPCsClient copyCurrentUserIdentifierWithReply:]_block_invoke.614
- ___64-[BRCXPCRegularIPCsClient healthStatusStringForContainer:reply:]_block_invoke.397
- ___65-[BRCXPCRegularIPCsClient _handleAcceptingCKShareMetadata:reply:]_block_invoke.671
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.667
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.667.cold.1
- ___65-[BRCXPCRegularIPCsClient getShareOptionsOfItemIdentifier:reply:]_block_invoke.667.cold.2
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.621
- ___66-[BRCXPCRegularIPCsClient startOperation:toSaveSharingInfo:reply:]_block_invoke.624
- ___66-[BRCXPCRegularIPCsClient(FPFSAdditions) notifyReimportCompleted:]_block_invoke.122
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428
- ___67-[BRCXPCRegularIPCsClient createAccountWithACAccountID:dsid:reply:]_block_invoke.428.cold.1
- ___68-[BRCXPCRegularIPCsClient getContainerForMangledID:personaID:reply:]_block_invoke.336
- ___69-[BRCXPCRegularIPCsClient getTotalApplicationDocumentUsageWithReply:]_block_invoke.319
- ___69-[BRCXPCRegularIPCsClient iWorkForceSyncContainerID:ownedByMe:reply:]_block_invoke.412
- ___70-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]_block_invoke
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.655
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.657
- ___70-[BRCXPCRegularIPCsClient startOperation:toAutoAcceptShareLink:reply:]_block_invoke.657.cold.1
- ___71-[BRCXPCRegularIPCsClient _t_extractMetadataForAllContainersWithReply:]_block_invoke.717
- ___71-[BRCXPCRegularIPCsClient startOperation:toCopyShareURLForShare:reply:]_block_invoke.663
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.114
- ___71-[BRCXPCRegularIPCsClient(FPFSAdditions) reimportItemIdentifier:reply:]_block_invoke.118
- ___72-[BRCXPCRegularIPCsClient copyCurrentUserNameAndDisplayHandleWithReply:]_block_invoke.615
- ___72-[BRCXPCRegularIPCsClient startOperation:toCopyAvailableQuotaWithReply:]_block_invoke.609
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.190
- ___73-[BRCXPCRegularIPCsClient computePurgeableSpaceForAllUrgenciesWithReply:]_block_invoke.413
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.404
- ___73-[BRCXPCRegularIPCsClient forceSyncWithBarrierContainerID:timeout:reply:]_block_invoke.404.cold.1
- ___73-[BRCXPCRegularIPCsClient handleCloudKitShareMetadata:completionHandler:]_block_invoke.672
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.370
- ___73-[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:]_block_invoke.386
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.584
- ___73-[BRCXPCRegularIPCsClient startOperation:toCopyShortTokenOfItemID:reply:]_block_invoke.586
- ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.194
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.628
- ___74-[BRCXPCRegularIPCsClient startOperation:toLookupShareParticipants:reply:]_block_invoke.630
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.399
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.399.cold.1
- ___75-[BRCXPCRegularIPCsClient forceSyncZoneHealthWithBarrierWithTimeout:reply:]_block_invoke.399.cold.2
- ___75-[BRCXPCRegularIPCsClient startOperation:toUnshareShare:forceDelete:reply:]_block_invoke.625
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.617
- ___76-[BRCXPCRegularIPCsClient copyCollaborationIdentifierForFileObjectID:reply:]_block_invoke.617.cold.1
- ___76-[BRCXPCRegularIPCsClient startOperation:toCopySharingInfoWithItemID:reply:]_block_invoke.581
- ___76-[BRCXPCRegularIPCsClient startOperation:toUploadAllFilesInContainer:reply:]_block_invoke.612
- ___77-[BRCXPCRegularIPCsClient launchSyncConsistencyChecksWithContainerIDs:reply:]_block_invoke.417
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.156
- ___79-[BRCXPCRegularIPCsClient printShareRequests:personaID:isPending:asJSON:reply:]_block_invoke.354
- ___80-[BRCXPCRegularIPCsClient _startOperation:toCopySharingInfoWithLocalItem:reply:]_block_invoke.572
- ___80-[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:]_block_invoke.332
- ___80-[BRCXPCRegularIPCsClient setMigrationStatus:forDSID:shouldUpdateAccount:reply:]_block_invoke.452
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopyParticipantTokenWithItemID:reply:]_block_invoke.647
- ___81-[BRCXPCRegularIPCsClient startOperation:toCopySharingAccessTokenOfItemID:reply:]_block_invoke.583
- ___81-[BRCXPCRegularIPCsClient startOperation:toPrepFolderForSharingWithItemID:reply:]_block_invoke.649
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.509
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.509.cold.1
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.509.cold.2
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.509.cold.3
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.513
- ___84-[BRCXPCRegularIPCsClient enumerateItemsInFolder:sortOrder:offset:limit:completion:]_block_invoke.523
- ___84-[BRCXPCRegularIPCsClient getEnhancedDrivePrivacyStatusForContainer:onServer:reply:]_block_invoke.709
- ___84-[BRCXPCRegularIPCsClient startOperation:toAcceptShareLink:skipAcceptDialogs:reply:]_block_invoke.653
- ___85-[BRCXPCRegularIPCsClient resolveFileObjectIDsToContentRecordIDsForThumbnails:reply:]_block_invoke.467
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.177
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.183
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.152
- ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke
- ___86-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]_block_invoke_2
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.524
- ___86-[BRCXPCRegularIPCsClient enumerateWorkingSetChangesFromChangeToken:limit:completion:]_block_invoke.526
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.119
- ___87-[BRCXPCRegularIPCsClient(FPFSAdditions) enumerateTrashItemsFromRank:limit:completion:]_block_invoke.121
- ___88-[BRCXPCRegularIPCsClient startOperation:toCopySharingWebAuthTokenForContainerID:reply:]_block_invoke.588
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) generateSmallItemThumbnailForFileObject:reply:]_block_invoke.93
- ___88-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingInfoForItemIdentifier:reply:]_block_invoke.135
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.157
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.164
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.591
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.598
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.600
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke.603
- ___90-[BRCXPCRegularIPCsClient startOperation:toCopyDocumentURLForRecordID:syncIfNeeded:reply:]_block_invoke_2.601
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.158
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.185
- ___91-[BRCXPCRegularIPCsClient startOperation:toModifyRecordAccessWithItemID:allowAccess:reply:]_block_invoke.639
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.146
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.146.cold.1
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkNeedsShareMigrateForItemIdentifier:reply:]_block_invoke.138
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.151
- ___93-[BRCXPCRegularIPCsClient dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:]_block_invoke.357
- ___94-[BRCXPCRegularIPCsClient _doesAnyRecordExistInContainerMetadataRecordName:completionHandler:]_block_invoke.685
- ___94-[BRCXPCRegularIPCsClient dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:]_block_invoke.360
- ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.445
- ___95-[BRCXPCRegularIPCsClient accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:]_block_invoke.445.cold.1
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.698
- ___95-[BRCXPCRegularIPCsClient setEnhancedDrivePrivacyEnabled:forContainer:onServer:onClient:reply:]_block_invoke.706
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.154
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.391
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.391.cold.1
- ___96-[BRCAccountSession(BRCDatabaseManager) backupDatabaseToURL:includeServer:doNotObfuscate:error:]_block_invoke.395
- ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke
- ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14
- ___97-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke.14.cold.1
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.169
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getiWorkPublishingBadgingStatusForItemIdentifier:reply:]_block_invoke.137
- ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e25_v16?0"BRCBGSystemTask"8lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s56l8s40l8s48l8
- ___block_literal_global.163
- ___block_literal_global.2
- ___block_literal_global.347
- ___block_literal_global.356
- ___block_literal_global.364
- ___block_literal_global.381
- ___block_literal_global.397
- ___block_literal_global.402
- ___block_literal_global.407
- ___block_literal_global.412
- ___block_literal_global.417
- ___block_literal_global.422
- ___block_literal_global.427
- ___block_literal_global.432
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.445
- ___block_literal_global.447
- ___block_literal_global.450
- ___block_literal_global.660
- ___block_literal_global.682
- _captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:.onceToken
- _captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:.reporterOperationRejectedThrottle
- _captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:.reporterOperationRejectedThrottlePeriod
- _objc_msgSend$_hasStateChangesWithResultingState:
- _objc_msgSend$bundleProxyForIdentifier:
- _objc_msgSend$bundleURL
- _objc_msgSend$hasStateChangesAndClearSaveStatusWithResultingState:
- _objc_msgSend$locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:
- _objc_msgSend$snapshotWithSignature:duration:events:payload:actions:reply:
CStrings:
+ "-[BRCAccountSession(BRCDatabaseManager) _updateDomain:withUserInfo:error:]"
+ "-[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:]"
+ "-[BRCAutoBugCaptureReporter _captureLogsForOperationType:ofSubtype:withContext:timeout:]_block_invoke"
+ "-[BRCClientZone _locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]"
+ "-[BRCPrimeMMCSCacheOperation main]"
+ "-[BRCPrimeMMCSCacheOperation main]_block_invoke"
+ "-[BRCServerPersistedState _stateToData]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:]_block_invoke"
+ "@\"BRCLRUDictionary\""
+ "@\"FPSandboxingURLWrapper\""
+ "@\"NSDictionary\"24@0:8@\"NSString\"16"
+ "BRCPrimeMMCSCacheOperation"
+ "Operation already finished"
+ "PRIME_CACHE"
+ "Prime MMCS Cache"
+ "SELECT app_library_plist FROM app_libraries WHERE app_library_name = %@"
+ "Unexpected error while converting server state to data!"
+ "[CRIT] Assertion failed: sop.metrics.MMCSMetrics.bytesUploaded == 0%@"
+ "[DEBUG] AppLibrary %@ added to a new zone. Mark as listed all + pristine for doc%@"
+ "[DEBUG] Application record: %@, error: %@%@"
+ "[DEBUG] Completed priming mmcs cache for %@ (uploaded %lu) - %@%@"
+ "[DEBUG] Priming MMCS cache before download for %@%@"
+ "[DEBUG] Starting to prime mmcs cache record %@%@"
+ "[DEBUG] Target application seems missing or hidden%@"
+ "[DEBUG] ┏%llx Printing open requests for access%@"
+ "[ERROR] Waiting for snapshotWithSignature timed out%@"
+ "[WARNING] do not open the app%@"
+ "_captureLogsForOperationType:ofSubtype:withContext:timeout:"
+ "_dataPendingSave"
+ "_existingContents"
+ "_isCZMAccountBasedOnCloudDocsPlistState"
+ "_itemMarkedForOOBSyncWhileRunning"
+ "_locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:"
+ "_primeMMCSCacheWithFacade:"
+ "_refreshLatestRevisionAndSharingStateForItemIdentifier:retryOnApplyFailure:reply:"
+ "_reporterOperationRejectedThrottle"
+ "_reporterOperationRejectedThrottlePeriod"
+ "_updateDomain:withUserInfo:error:"
+ "accountStartedSchedulingCZM"
+ "appProtectionHidden"
+ "applicationState"
+ "applyNonDocumentsOnLocateRecord"
+ "br_primeMMCSCache"
+ "dataPendingSave"
+ "download.prime-mmcs-cache"
+ "download.prime-mmcs-cache-ramp"
+ "fetchAppLibraryPlist:"
+ "fpfs.populate.fp.domain.experiment.id"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithExistingContentsURL:item:sessionContext:"
+ "isMarkedForOOBSync"
+ "itemMarkedForOOBSync:"
+ "locateContentRecordIfNecessaryForItem:isUserWaiting:maxOperationBackoff:"
+ "objectForKey:ofClass:"
+ "populateFPDomainExperimentID"
+ "prime-cache-"
+ "queryFastPathsForPrimaryPersona:"
+ "scheduleSyncDownForOOBModifyRecordsAckForItemID:"
+ "shouldPrimeMMCSCacheBeforeDownloadWithAccountFacade:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "sync.locate-records.apply-non-documents"
+ "v48@0:8@16@24@32d40"
- "-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]"
- "-[BRCAutoBugCaptureReporter captureLogsForOperationType:ofSubtype:withContext:waitForCompletion:]_block_invoke"
- "-[BRCClientState hasStateChangesAndClearSaveStatusWithResultingState:]"
- "-[BRCClientZone locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:]"
- "-[BRCServerPersistedState _hasStateChangesWithResultingState:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) _refreshLatestRevisionAndSharingStateForItemIdentifier:reply:]_block_invoke"
- "@\"NSDictionary\"32@0:8@\"NSString\"16^@24"
- "BRCloudDocsHelper"
- "[CRIT] Assertion failed: data%@"
- "[CRIT] Assertion failed: items.count == 1%@"
- "[DEBUG] AppLibrary %@ added to a new zone. Mark as listed all + prisitine for doc%@"
- "[DEBUG] Application proxy: %@, proxy.bundleURL = %@%@"
- "[DEBUG] Target application seems missing%@"
- "[DEBUG] ┏%llx Printing open reqests for access%@"
- "[WARNING] do not open Pages%@"
- "_hasStateChangesWithResultingState:"
- "bundleProxyForIdentifier:"
- "bundleURL"
- "hasStateChangesAndClearSaveStatusWithResultingState:"
- "locateRecordIfNecessaryForRecordID:isUserWaiting:maxOperationBackoff:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"

```
