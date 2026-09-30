## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4140.0.0.502.2
-  __TEXT.__text: 0x3012d0
+4204.0.0.502.1
+  __TEXT.__text: 0x30ba78
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x19cbc
-  __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x7c88f
-  __TEXT.__oslogstring: 0x3b08a
-  __TEXT.__gcc_except_tab: 0x19be4
+  __TEXT.__objc_methlist: 0x19ddc
+  __TEXT.__const: 0x500
+  __TEXT.__cstring: 0x7ceb4
+  __TEXT.__oslogstring: 0x3bd5e
+  __TEXT.__gcc_except_tab: 0x1a210
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9d48
-  __TEXT.__objc_classname: 0x2a39
-  __TEXT.__objc_methname: 0x4360e
-  __TEXT.__objc_methtype: 0x8eae
-  __TEXT.__objc_stubs: 0x2e700
-  __DATA_CONST.__got: 0x16b0
-  __DATA_CONST.__const: 0x9510
-  __DATA_CONST.__objc_classlist: 0xa38
+  __TEXT.__unwind_info: 0x9df8
+  __TEXT.__objc_classname: 0x2a75
+  __TEXT.__objc_methname: 0x4399d
+  __TEXT.__objc_methtype: 0x8edb
+  __TEXT.__objc_stubs: 0x2e9e0
+  __DATA_CONST.__got: 0x16d8
+  __DATA_CONST.__const: 0x9578
+  __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe3f8
+  __DATA_CONST.__objc_selrefs: 0xe4b8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x900
-  __DATA_CONST.__objc_arraydata: 0xe00
+  __DATA_CONST.__objc_superrefs: 0x8f8
+  __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x2b28
-  __AUTH_CONST.__cfstring: 0x22300
-  __AUTH_CONST.__objc_const: 0x3cbe8
-  __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__const: 0x2b78
+  __AUTH_CONST.__cfstring: 0x22600
+  __AUTH_CONST.__objc_const: 0x3cdc0
+  __AUTH_CONST.__objc_intobj: 0xb88
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x2760
+  __AUTH.__objc_data: 0x27b0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f18
+  __DATA.__objc_ivar: 0x1f34
   __DATA.__data: 0x27a0
   __DATA.__bss: 0x230
   __DATA_DIRTY.__objc_data: 0x3ed0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
-  - /System/Library/Frameworks/NotificationCenter.framework/NotificationCenter
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D13C512C-B339-3464-BDC1-99F9A0A7FA49
-  Functions: 13437
-  Symbols:   43711
-  CStrings:  27368
+  UUID: A7BD327E-EA34-3CF2-A59D-8A991E288189
+  Functions: 13488
+  Symbols:   43912
+  CStrings:  27505
 
Symbols:
+ +[BRCAppLibrary didListItemID:sessionContext:]
+ -[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:].cold.2
+ -[BRCAppLibrary resumeQueryBasedSyncIfNecessary]
+ -[BRCAppLibrary resumeQueryBasedSyncIfNecessary].cold.1
+ -[BRCAppLibrary scheduleFullLibraryContentsFetch].cold.2
+ -[BRCBounceIncident .cxx_destruct]
+ -[BRCBounceIncident bounceReason]
+ -[BRCBounceIncident description]
+ -[BRCBounceIncident itemID]
+ -[BRCBounceIncident lastEditorDeviceName]
+ -[BRCBounceIncident setBounceReason:]
+ -[BRCBounceIncident setItemID:]
+ -[BRCBounceIncident setLastEditorDeviceName:]
+ -[BRCBouncingAnalyzer handleBounceIncidentDuringApplyWithServerItem:bounceReason:]
+ -[BRCBouncingAnalyzer handleBounceIncidentDuringApplyWithServerItem:bounceReason:].cold.1
+ -[BRCBouncingAnalyzer initWithSessionContext:]
+ -[BRCBouncingAnalyzer startBouncingIncidentBatch]
+ -[BRCBouncingAnalyzer startBouncingIncidentBatch].cold.1
+ -[BRCBouncingAnalyzer stopBouncingIncidentBatch]
+ -[BRCBouncingAnalyzer stopBouncingIncidentBatch].cold.1
+ -[BRCCollaborationUploadOperation main].cold.2
+ -[BRCContainerScheduler _hasMetadataToSyncUpToContainerMetadata]
+ -[BRCContainerScheduler _markContainerMetadataNeedsSyncUp]
+ -[BRCContainerScheduler _markContainerMetadataNeedsSyncUp].cold.1
+ -[BRCContainerScheduler recoverAndReportMissingJobs]
+ -[BRCDeadlineSource signalWithDeadline:extend:]
+ -[BRCFileUnlinker initWithCacheDirPath:]
+ -[BRCServerZone setStateBits:].cold.1
+ -[BRCSharingAcceptFlowOperation _isAccountRestricted_step].cold.3
+ -[BRCSharingAcceptFlowOperation _openiWorkAppPreemptively_step].cold.3
+ -[BRCStageRegistry _purgeAllUploadsWithIncludeActiveItems:].cold.2
+ -[BRCStageRegistry markUploadActiveForStageID:]
+ -[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:additionalDevices:triggerRootCause:]
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:].cold.1
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:]
+ -[BRCTapToRadarManager requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]
+ -[BRCUserDefaults containerMetadataSyncUpDelay]
+ -[BRCUserDefaults containerMetadataSyncUpMaxDelay]
+ -[BRCUserDefaults dbIntegrityCheckContainerMetadataSyncUpJob]
+ -[BRCXPCRegularIPCsClient _t_getContainerMetadataForContainerID:reply:]
+ -[BRCXPCRegularIPCsClient _t_getContainerMetadataForContainerID:reply:].cold.1
+ -[BRFieldContentSignature(BRAdditions) ignoreSignaturesAreEquivalentButContentIsDifferent]
+ -[CKShare(BRCUserNotificationRequestAccessAdditions) inferParticipantPermissions]
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table186
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table207
+ GCC_except_table220
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table257
+ GCC_except_table445
+ GCC_except_table459
+ GCC_except_table466
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table480
+ GCC_except_table565
+ GCC_except_table77
+ _BRCMigrateLegacyUbiquityRoot
+ _BRCMigrateLegacyUbiquityRoot.cold.1
+ _BRCMigrateLegacyUbiquityRoot.cold.2
+ _BRCMigrateLegacyUbiquityRoot.cold.3
+ _BRCMigrateLegacyUbiquityRoot.cold.4
+ _BRCMigrateLegacyUbiquityRoot.cold.5
+ _BRCMigrateLegacyUbiquityRoot.cold.6
+ _BRCRootIsOwnedByUbd
+ _BRCRootIsOwnedByUbd.cold.1
+ _BRCRootIsOwnedByUbd.cold.2
+ _BRCTouchRootMergeWitness
+ _BRUbiquitousDefaultMangledContainerID
+ _NSFilePosixPermissions
+ _NSURLCreationDateKey
+ _NSURLIsHiddenKey
+ _OBJC_CLASS_$_BRCBounceIncident
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_IVAR_$_BRCBounceIncident._bounceReason
+ _OBJC_IVAR_$_BRCBounceIncident._itemID
+ _OBJC_IVAR_$_BRCBounceIncident._lastEditorDeviceName
+ _OBJC_IVAR_$_BRCBouncingAnalyzer._bounceIncidentsInBatch
+ _OBJC_IVAR_$_BRCBouncingAnalyzer._bouncingIncidentBatchStarted
+ _OBJC_IVAR_$_BRCBouncingAnalyzer._dbFacade
+ _OBJC_IVAR_$_BRCContainerScheduler._containerMetadataSyncUpMaxDeadline
+ _OBJC_IVAR_$_BRCSharingAcceptFlowOperation._appBundleID
+ _OBJC_METACLASS_$_BRCBounceIncident
+ __OBJC_$_CLASS_METHODS_BRCAppLibrary
+ __OBJC_$_INSTANCE_METHODS_BRCBounceIncident
+ __OBJC_$_INSTANCE_METHODS_CKShare(BRCSerializationAdditions|BRCUserNotificationRequestAccessAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_BRCBounceIncident
+ __OBJC_$_PROP_LIST_BRCBounceIncident
+ __OBJC_CLASS_RO_$_BRCBounceIncident
+ __OBJC_METACLASS_RO_$_BRCBounceIncident
+ ___100-[BRCDownloadContent _getDesiredPackageIndicesUsingReader:savedContentsURL:package:itemCount:error:]_block_invoke
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.80
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.80.cold.1
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.103
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.103.cold.1
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.105
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.107
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.112
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.112.cold.1
+ ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.218
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.191
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.192
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.193
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.193.cold.1
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.194
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.14
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.14.cold.1
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.16
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.16.cold.1
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.16.cold.2
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.26
+ ___206-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke.26.cold.1
+ ___25-[BRCFSUploader schedule]_block_invoke.156
+ ___26-[BRCAccountSession close]_block_invoke.295
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.317
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.317.cold.1
+ ___40-[BRCFileUnlinker initWithCacheDirPath:]_block_invoke
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.262
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.266
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.279
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.265
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.265.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.267
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.267.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.271
+ ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.129
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.326.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.329
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.351
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.351.cold.1
+ ___46-[BRCFSUploader rescheduleJobsPendingCellular]_block_invoke.115
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke.142
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke_2
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke_2.cold.1
+ ___48-[BRCBouncingAnalyzer stopBouncingIncidentBatch]_block_invoke
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.351
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.356
+ ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.514
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.259
+ ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.171
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.242
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.256
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.102
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.104
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.110
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.79.cold.1
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.81
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.103
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.103.cold.1
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.108
+ ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.112
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133.cold.1
+ ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.133.cold.2
+ ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.726
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.434.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.434.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.435
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.169
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.169.cold.1
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.170
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.170.cold.1
+ ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.192
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.430
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.430.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.432
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.433
+ ___59-[BRCContainerScheduler _syncScheduleForContainersMetadata]_block_invoke.cold.1
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.364
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.365
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.138
+ ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.138.cold.1
+ ___64-[BRCContainerScheduler _hasMetadataToSyncUpToContainerMetadata]_block_invoke
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.212
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.213
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.381
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.437
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.445
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.453
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.453.cold.1
+ ___71-[BRCXPCRegularIPCsClient _t_getContainerMetadataForContainerID:reply:]_block_invoke
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.735
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.739
+ ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.737
+ ___80-[BRCAccountSession _recoverAndReportStateIntegrityWithCompletion:recoveryTask:]_block_invoke_17
+ ___81-[BRCDocumentItem(BRCFPFSAdditions) _reIngestFromFileProviderWithIsFirstAttempt:]_block_invoke.22
+ ___81-[CKShare(BRCUserNotificationRequestAccessAdditions) inferParticipantPermissions]_block_invoke
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.357
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.357.cold.1
+ ___88-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]_block_invoke
+ ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.72
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.289
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.295
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.295.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.296
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.293
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.293.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.297
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.667
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.667.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671.cold.1
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.671.cold.2
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.673
+ ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.674
+ ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.229
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs_e20_v20?0B8"NSError"12ls96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104bs_e17_v16?0"NSError"8ls104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e28_B16?0"CKShareParticipant"8l
+ ___block_descriptor_32_e30_24?0"BRCBounceIncident"8Q16l
+ ___block_descriptor_40_e8_32s_e34_B32?0"NSString"8"NSString"16Q24ls32l8
+ ___block_descriptor_41_e8_32s_e34_B32?0"NSString"8"NSString"16Q24ls32l8
+ ___block_descriptor_48_e8_32s40s_e69_v32?0"CKUserIdentityLookupInfo"8"CKShareParticipant"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40s48r_e23_B16?0"PQLConnection"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e8_i12?0i8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s_e23_B16?0"BRCAppLibrary"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72r_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr56l8s32l8s40l8r64l8r72l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56r64w72w80w_e22_v16?0"BGSystemTask"8ls32l8w64l8w72l8w80l8s40l8r56l8s48l8
+ ___block_literal_global.1604
+ ___block_literal_global.173
+ ___block_literal_global.1756
+ ___block_literal_global.1768
+ ___block_literal_global.1939
+ ___block_literal_global.196
+ ___block_literal_global.2121
+ ___block_literal_global.2162
+ ___block_literal_global.2167
+ ___block_literal_global.236
+ ___block_literal_global.243
+ ___block_literal_global.2431
+ ___block_literal_global.2447
+ ___block_literal_global.246
+ ___block_literal_global.251
+ ___block_literal_global.2532
+ ___block_literal_global.258
+ ___block_literal_global.2870
+ ___block_literal_global.297
+ ___block_literal_global.304
+ ___block_literal_global.316
+ ___block_literal_global.328
+ ___block_literal_global.362
+ ___block_literal_global.489
+ ___block_literal_global.70
+ ___block_literal_global.760
+ ___block_literal_global.84
+ ___block_literal_global.934
+ ___block_literal_global.95
+ ___block_literal_global.99
+ _objc_msgSend$_hasMetadataToSyncUpToContainerMetadata
+ _objc_msgSend$_markContainerMetadataNeedsSyncUp
+ _objc_msgSend$br_all_of:
+ _objc_msgSend$br_filenameSafeFileSystemRepresentation
+ _objc_msgSend$br_newReadableFileSizeStringFromBytesCount:
+ _objc_msgSend$br_pathSafeFileSystemRepresentation
+ _objc_msgSend$brc_errorDocumentWithFilename:size:isTooLargeToUpload:localizedDescription:
+ _objc_msgSend$bytesDownloaded
+ _objc_msgSend$bytesFulfilledByPeers
+ _objc_msgSend$bytesFulfilledLocally
+ _objc_msgSend$cloneFileURL:toUploadStageID:liveStageFilename:error:
+ _objc_msgSend$computedProperties
+ _objc_msgSend$containerMetadataSyncUpDelay
+ _objc_msgSend$containerMetadataSyncUpMaxDelay
+ _objc_msgSend$dbIntegrityCheckContainerMetadataSyncUpJob
+ _objc_msgSend$didListItemID:sessionContext:
+ _objc_msgSend$handleBounceIncidentDuringApplyWithServerItem:bounceReason:
+ _objc_msgSend$ignoreSignaturesAreEquivalentButContentIsDifferent
+ _objc_msgSend$inferParticipantPermissions
+ _objc_msgSend$initWithCacheDirPath:
+ _objc_msgSend$markUploadActiveForStageID:
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$recoverAndReportMissingJobs
+ _objc_msgSend$requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:
+ _objc_msgSend$requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:
+ _objc_msgSend$requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:
+ _objc_msgSend$resumeQueryBasedSyncIfNecessary
+ _objc_msgSend$setBounceReason:
+ _objc_msgSend$setDeviceIDs:
+ _objc_msgSend$signalWithDeadline:extend:
+ _objc_msgSend$startBouncingIncidentBatch
+ _objc_msgSend$stopBouncingIncidentBatch
+ _objc_msgSend$writeToURL:atomically:
- -[BRCAppLibrary scheduleContainerMetadataSyncUp].cold.1
- -[BRCBouncingAnalyzer initWithTapToRadarManager:analyticsReporter:]
- -[BRCFileUnlinker _moveOldUnlinkDir]
- -[BRCFileUnlinker init]
- -[BRCFileUnlinker init].cold.1
- -[BRCPrivateServerZone activateWithClientZone:offline:]
- -[BRCStageRegistry _garbageCollectUploads]
- -[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:]
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:].cold.1
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:]
- -[BRCTapToRadarManager requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]
- -[BRCUserDefaults migrationQueryMaxOperationCount]
- GCC_except_table134
- GCC_except_table166
- GCC_except_table174
- GCC_except_table175
- GCC_except_table198
- GCC_except_table199
- GCC_except_table226
- GCC_except_table230
- GCC_except_table251
- GCC_except_table328
- GCC_except_table460
- GCC_except_table467
- GCC_except_table468
- GCC_except_table478
- GCC_except_table563
- _OBJC_IVAR_$_BRCSyncContext._migrationQueryOperationsQueue
- __OBJC_$_CATEGORY_INSTANCE_METHODS_CKShare_$_BRCSerializationAdditions
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.76
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.76.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.101
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.97
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.97.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.99
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.215
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.185
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.186
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.187
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.187.cold.1
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.188
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.14
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.14.cold.1
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16.cold.1
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.16.cold.2
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.26
- ___188-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke.26.cold.1
- ___23-[BRCFileUnlinker init]_block_invoke
- ___25-[BRCFSUploader schedule]_block_invoke.147
- ___26-[BRCAccountSession close]_block_invoke.292
- ___31-[BRCContainerScheduler resume]_block_invoke_2
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.314
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.314.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.259
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.260
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.276
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.262
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.262.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.264
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.264.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.268
- ___43-[BRCStageRegistry _removeUnusedXattrBlobs]_block_invoke.128
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.316
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.316.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.316.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.316.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.316.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.1
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.348
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.348.cold.1
- ___46-[BRCFSUploader rescheduleJobsPendingCellular]_block_invoke.106
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.348
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.355
- ___49-[BRCSyncHealthReport generateReportWithSession:]_block_invoke.511
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.251
- ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.168
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.238
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.238.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.238.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.238.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.238.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.252
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.252.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.252.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.252.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.252.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.239
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.246.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.253
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.101
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.103
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.109
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke.80
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.102
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.102.cold.1
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.107
- ___53-[BRCListDirectoryContentsOperation _scheduleQueryOp]_block_invoke_2.111
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.134
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.134.cold.1
- ___54-[BRCSyncContext forceContainerForegroundForDuration:]_block_invoke.134.cold.2
- ___55-[BRCPrivateServerZone activateWithClientZone:offline:]_block_invoke
- ___55-[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:]_block_invoke.723
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.433
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.433.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.433.cold.2
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.166
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.166.cold.1
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.167
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.167.cold.1
- ___58-[BRCRecursiveListDirectoryContentsOperation listNextItem]_block_invoke.191
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.429
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.429.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.431
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.432
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.361
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.362
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.139
- ___63-[BRCSyncContext _armForegroundGraceTimerForClientDescription:]_block_invoke.139.cold.1
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.204
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.205
- ___65-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke.cold.1
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.378
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.435
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.443
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.452
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.452.cold.1
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.732
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke.736
- ___76+[BRCSyncConsistencyReport generateReportWithSession:mangledIDs:completion:]_block_invoke_2.734
- ___77-[BRCContainerScheduler didChangeSyncStatusForContainerMetadataForContainer:]_block_invoke.cold.1
- ___79-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]_block_invoke
- ___81-[BRCDocumentItem(BRCFPFSAdditions) _reIngestFromFileProviderWithIsFirstAttempt:]_block_invoke.24
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.354
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.354.cold.1
- ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.68
- ___94-[BRCContainerMetadataSyncUpOperation _containerMetadataRecordsToSaveWithBatchSize:requestID:]_block_invoke_2.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.281
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.287
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.287.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.288
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.285
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.285.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.289
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.664
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.664.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.665
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.668.cold.1
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.668.cold.2
- ___95+[BRCItemCountMismatchReport generateReportForSharedFolder:qualityOfService:completionHandler:]_block_invoke.670
- ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.221
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs_e20_v20?0B8"NSError"12ls88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs_e17_v16?0"NSError"8ls96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_40_e8_32s_e27_B24?0"BRFileObjectID"8Q16ls32l8
- ___block_descriptor_40_e8_32s_e69_v32?0"CKUserIdentityLookupInfo"8"CKShareParticipant"16"NSError"24ls32l8
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r40l8
- ___block_descriptor_56_e8_32s_e23_B16?0"BRCAppLibrary"8ls32l8
- ___block_descriptor_57_e8_32s40s48r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16ls32l8s40l8r48l8
- ___block_descriptor_65_e8_32s40s48r56r_e88_i24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr48l8s32l8s40l8r56l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72r_e47_v24?0"NSFileProviderItemVersion"8"NSError"16lr48l8r56l8s32l8r64l8r72l8s40l8
- ___block_descriptor_96_e8_32s40s48s56s64r72w80w88w_e22_v16?0"BGSystemTask"8ls32l8w72l8w80l8w88l8s40l8s48l8r64l8s56l8
- ___block_literal_global.127
- ___block_literal_global.1598
- ___block_literal_global.170
- ___block_literal_global.1750
- ___block_literal_global.1762
- ___block_literal_global.177
- ___block_literal_global.1933
- ___block_literal_global.2115
- ___block_literal_global.2150
- ___block_literal_global.2161
- ___block_literal_global.240
- ___block_literal_global.241
- ___block_literal_global.2428
- ___block_literal_global.2444
- ___block_literal_global.2529
- ___block_literal_global.255
- ___block_literal_global.2864
- ___block_literal_global.294
- ___block_literal_global.301
- ___block_literal_global.313
- ___block_literal_global.325
- ___block_literal_global.359
- ___block_literal_global.481
- ___block_literal_global.757
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.87
- ___block_literal_global.931
- _objc_msgSend$_garbageCollectUploads
- _objc_msgSend$_moveOldUnlinkDir
- _objc_msgSend$br_safeFileSystemRepresentation
- _objc_msgSend$brc_errorDocumentWithFilename:size:isTooLargeToUpload:
- _objc_msgSend$cloneURLToLiveStage:liveStageFilename:error:
- _objc_msgSend$internalDaemonContainerPath
- _objc_msgSend$migrationQueryMaxOperationCount
- _objc_msgSend$requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:
- _objc_msgSend$requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:
- _objc_msgSend$requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:
CStrings:
+ "-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]"
+ "-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke_2"
+ "-[BRCAppLibrary setContainerMetadataNeedsSyncUp:]"
+ "-[BRCBouncingAnalyzer handleBounceIncidentDuringApplyWithServerItem:bounceReason:]"
+ "-[BRCBouncingAnalyzer startBouncingIncidentBatch]"
+ "-[BRCBouncingAnalyzer stopBouncingIncidentBatch]"
+ "-[BRCContainerScheduler _markContainerMetadataNeedsSyncUp]"
+ "-[BRCContainerScheduler recoverAndReportMissingJobs]"
+ "-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]"
+ "-[BRCStageRegistry(FPFSAdditions) cloneFileURL:toUploadStageID:liveStageFilename:error:]_block_invoke"
+ "-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]"
+ "-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient _t_getContainerMetadataForContainerID:reply:]"
+ "-[BRCXPCRegularIPCsClient _t_getContainerMetadataForContainerID:reply:]_block_invoke"
+ ".do-not-delete"
+ ".icloud-drive.do-not-delete"
+ ".ubd"
+ "@24@?0@\"BRCBounceIncident\"8Q16"
+ "Application Support/Ubiquity"
+ "B16@?0@\"CKShareParticipant\"8"
+ "B32@?0@\"NSString\"8@\"NSString\"16Q24"
+ "BRCBounceIncident"
+ "BRCMigrateLegacyUbiquityRoot"
+ "BRCRootIsOwnedByUbd"
+ "BRCTouchRootMergeWitness"
+ "BRCUserNotificationRequestAccessAdditions"
+ "BRCValidateDirAt"
+ "BouncedItem"
+ "Caches/com.apple.bird"
+ "Caches/com.apple.ubd"
+ "ICLOUD_DRIVE_DOCUMENT_TOO_LARGE_TO_UPLOAD"
+ "Item ID: %@, Bounce reason: %@, Last Editor Device Name: %@"
+ "Items got bounced"
+ "Logs/CrashReporter/DiagnosticLogs/Ubiquity"
+ "SELECT ci.rowid FROM client_items AS ci LEFT JOIN client_uploads AS cu ON ci.rowid = cu.throttle_id WHERE ci.item_localsyncupstate = 3 AND ci.item_localsyncupstate != 0 AND ci.item_type IN (1, 6) AND ci.item_state IN (0) AND IFNULL(cu.throttle_state, 0) = 0"
+ "SELECT ci.rowid, ci.zone_rowid, ci.item_id, ci.item_creator_id, ci.item_sharing_options, ci.item_side_car_ckinfo, ci.item_parent_zone_rowid, ci.item_localsyncupstate, ci.item_local_diffs, ci.item_notifs_rank, ci.app_library_rowid, ci.item_min_supported_os_rowid, ci.item_user_visible, ci.item_stat_ckinfo, ci.item_state, ci.item_type, ci.item_mode, ci.item_birthtime, ci.item_lastusedtime, ci.item_favoriterank,ci.item_parent_id, ci.item_filename, ci.item_hidden_ext, ci.item_finder_tags, ci.item_xattr_signature, ci.item_trash_put_back_path, ci.item_trash_put_back_parent_id, ci.item_alias_target, ci.item_creator, ci.item_processing_stamp, ci.item_bouncedname, ci.item_scope, ci.item_local_change_count, ci.item_old_version_identifier, ci.fp_creation_item_identifier, ci.version_name, ci.version_ckinfo, ci.version_mtime, ci.version_size, ci.version_thumb_size, ci.version_thumb_signature, ci.version_content_signature, ci.version_xattr_signature, ci.version_edited_since_shared, ci.version_device, ci.version_conflict_loser_etags, ci.version_quarantine_info, ci.version_uploaded_assets, ci.version_upload_error, ci.version_old_zone_item_id, ci.version_old_zone_rowid, ci.version_local_change_count, ci.version_old_version_identifier, ci.item_live_conflict_loser_etags, ci.item_file_id, ci.item_generation FROM client_items AS ci LEFT JOIN client_sync_up AS su ON su.throttle_id = ci.rowid AND su.zone_rowid = ci.zone_rowid LEFT JOIN client_uploads AS cu ON cu.throttle_id = ci.rowid AND cu.zone_rowid = ci.zone_rowid WHERE ci.item_localsyncupstate = 3 AND ci.item_localsyncupstate != 0 AND ci.item_type IN (1, 6) AND (IFNULL(cu.throttle_state, 0) = 0 OR (cu.throttle_state = 31 AND IFNULL(su.throttle_state, 0) = 0))"
+ "SELECT csu.throttle_id, csu.last_try_stamp, li.zone_rowid FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND csu.throttle_state != 0  AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
+ "Ti,N,V_bounceReason"
+ "T{?=Q*iB},R,N,V_logSections"
+ "[Bouncing] some items got bounced on latest update"
+ "[CRIT] Assertion failed: !_bouncingIncidentBatchStarted%@"
+ "[CRIT] Assertion failed: _appBundleID%@"
+ "[CRIT] Assertion failed: _bouncingIncidentBatchStarted%@"
+ "[CRIT] Assertion failed: _symlinkContent%@"
+ "[CRIT] UNREACHABLE: Failed removing root folder from the wrong account%@"
+ "[CRIT] UNREACHABLE: Failed to remove mobile documents directory not belonging to us%@"
+ "[CRIT] We own both the root and had an old one renamed away\nWe have purged the old one, and will now reset%@"
+ "[DEBUG] %@ - Finished records in op %@ (%lu downloaded, %lld locally, %lld from peers), Error: %@%@"
+ "[DEBUG] %@ is no longer full sync because of a non delta sync operation%@"
+ "[DEBUG] %s dir at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[DEBUG] AppLibrary %@ added to a new zone. Mark as listed all + prisitine for doc%@"
+ "[DEBUG] Applibrary %@ already listed docs but still did not complete listing trash.%@"
+ "[DEBUG] Purged %lld bytes%@"
+ "[DEBUG] Starting the upload operation for record %@%@"
+ "[DEBUG] We should not allow conflicts, set plugin fields for record: %@%@"
+ "[DEBUG] We should resume QBS for %@%@"
+ "[DEBUG] already syncing container-metadata: %@%@"
+ "[DEBUG] container-metadata needs sync up for %@ changed to %s%@"
+ "[DEBUG] container-metadata still have things to sync up%@"
+ "[DEBUG] done fetching recents and favorites for: %@%@"
+ "[DEBUG] fixing applibrary delegate to %@%@"
+ "[DEBUG] marking container-metadata needs-sync-up with deadline: %lld%@"
+ "[DEBUG] preparing to sync up %@ in operation %@%@"
+ "[DEBUG] root has a .ubd folder: deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[DEBUG] root has accountString %@%@"
+ "[DEBUG] ┏%llx deleting root folder%@"
+ "[DEBUG] ┏%llx deleting ubd's support files%@"
+ "[DEBUG] ┏%llx migrating legacy ubiquity root%@"
+ "[ERROR] Failed to create root at %@ - %@%@"
+ "[ERROR] Unable to create directory \"%@\": %@%@"
+ "[ERROR] Unable to set mtime & hidden on \"%@\": %@%@"
+ "[ERROR] can't fstat (%d, '%@') %{errno}d%@"
+ "[ERROR] can't fstat (%d, '%@') after mkdir %{errno}d%@"
+ "[ERROR] can't lstat '%@' %{errno}d%@"
+ "[ERROR] can't open (%d, '%@') %{errno}d%@"
+ "[ERROR] can't open (%d, '%@') after mkdir %{errno}d%@"
+ "[ERROR] can't open root '%@' %{errno}d%@"
+ "[ERROR] failed chmod at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x %{errno}d%@"
+ "[ERROR] failed renaming root back from '%@' to '%@' %{errno}d%@"
+ "[ERROR] mkdirat(%d, '%@') %{errno}d%@"
+ "[ERROR] nonexistent container %@%@"
+ "[ERROR] not a directory at (%d, '%@') after mkdir deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[ERROR] not a directory at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[ERROR] unexpected permissions at (%d, '%@') deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[ERROR] unexpected uid != %u at (%d, '%@')deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[NOTICE] found our root at '%@' deviceID:%u fileID:%llu mode:%c%c%c%c%c%c%c%c%c%c nlink:%u uid:%u gid:%u atime:%lu mtime:%lu ctime:%lu size:%llu flags:0x%x%@"
+ "[NOTICE] listed %lu edited items from the cloud for %@\n%@"
+ "[NOTICE] migrating root from accountString %@ to %@%@"
+ "[NOTICE] moved '%@' back to '%@'%@"
+ "[NOTICE] tagging root with accountString %@%@"
+ "[WARNING] container-metadata has things to sync-up but it is not marked as needs-sync-up%@"
+ "[WARNING] invalid symlink content: %@%@"
+ "_appBundleID"
+ "_bounceIncidentsInBatch"
+ "_bounceReason"
+ "_bouncingIncidentBatchStarted"
+ "_containerMetadataSyncUpMaxDeadline"
+ "_hasMetadataToSyncUpToContainerMetadata"
+ "_markContainerMetadataNeedsSyncUp"
+ "_t_getContainerMetadataForContainerID:reply:"
+ "_unlinkUbiquitySupportFiles"
+ "bounceReason"
+ "br_all_of:"
+ "br_filenameSafeFileSystemRepresentation"
+ "br_newReadableFileSizeStringFromBytesCount:"
+ "br_pathSafeFileSystemRepresentation"
+ "brc_errorDocumentWithFilename:size:isTooLargeToUpload:localizedDescription:"
+ "bytesDownloaded"
+ "bytesFulfilledByPeers"
+ "bytesFulfilledLocally"
+ "cloneFileURL:toUploadStageID:liveStageFilename:error:"
+ "computedProperties"
+ "com~apple~Keynote/Documents/Recovered Data"
+ "com~apple~Keynote/Documents/Recovered Data.folder"
+ "com~apple~Numbers/Documents/Recovered Data"
+ "com~apple~Numbers/Documents/Recovered Data.folder"
+ "com~apple~Pages/Documents/Recovered Data"
+ "com~apple~Pages/Documents/Recovered Data.folder"
+ "containerMetadataSyncUpDelay"
+ "containerMetadataSyncUpMaxDelay"
+ "created"
+ "cu-%@"
+ "db.integrity-check.container-metadata-sync-up"
+ "dbIntegrityCheckContainerMetadataSyncUpJob"
+ "didListItemID:sessionContext:"
+ "found"
+ "full scan on TELEMETRY_FAILURE_COUNTS_TABLE"
+ "handleBounceIncidentDuringApplyWithServerItem:bounceReason:"
+ "ignoreSignaturesAreEquivalentButContentIsDifferent"
+ "inferParticipantPermissions"
+ "initWithCacheDirPath:"
+ "markUploadActiveForStageID:"
+ "orderedSetWithArray:"
+ "rdar://151131525"
+ "recoverAndReportMissingJobs"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:additionalDevices:triggerRootCause:"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:"
+ "requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:"
+ "requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:additionalDevices:completionHandler:"
+ "resumeQueryBasedSyncIfNecessary"
+ "setBounceReason:"
+ "setDeviceIDs:"
+ "signalWithDeadline:extend:"
+ "some items got bounced on latest update"
+ "some items got bounced on latest update:\n%@"
+ "startBouncingIncidentBatch"
+ "stopBouncingIncidentBatch"
+ "sync.container-metadata-sync-up-delay"
+ "sync.container-metadata-sync-up-max-delay"
+ "v100@0:8@16@24@32@40q48@56@64B72@76@84@92"
+ "v108@0:8@16@24@32@40q48@56@64B72@76@84@92@?100"
+ "v28@0:8q16B24"
+ "v76@0:8@16@24@32@40B48@52@60@68"
+ "v84@0:8@16@24@32@40B48@52@60@68@?76"
+ "writeToURL:atomically:"
+ "{?=\"sectionID\"Q\"function\"*\"line\"i\"ignorePersona\"B}"
+ "{?=Q*iB}16@0:8"
- "-[BRCAppLibrary scheduleContainerMetadataSyncUp]"
- "-[BRCContainerScheduler didChangeSyncStatusForContainerMetadataForContainer:]_block_invoke"
- "-[BRCFileUnlinker init]"
- "-[BRCStageRegistry _garbageCollectUploadsIncludingActiveUploads:]_block_invoke"
- "-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]"
- "-[BRCStageRegistry(FPFSAdditions) cloneURLToLiveStage:liveStageFilename:error:]_block_invoke"
- "-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]"
- "-[BRCTapToRadarManager requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:]_block_invoke"
- "B24@?0@\"BRFileObjectID\"8Q16"
- "SELECT ci.rowid FROM client_items AS ci LEFT JOIN client_uploads AS cu ON ci.rowid = cu.throttle_id WHERE ci.item_localsyncupstate = 3 AND ci.item_type IN (1, 6) AND ci.item_state IN (0) AND IFNULL(cu.throttle_state, 0) = 0"
- "SELECT ci.rowid, ci.zone_rowid, ci.item_id, ci.item_creator_id, ci.item_sharing_options, ci.item_side_car_ckinfo, ci.item_parent_zone_rowid, ci.item_localsyncupstate, ci.item_local_diffs, ci.item_notifs_rank, ci.app_library_rowid, ci.item_min_supported_os_rowid, ci.item_user_visible, ci.item_stat_ckinfo, ci.item_state, ci.item_type, ci.item_mode, ci.item_birthtime, ci.item_lastusedtime, ci.item_favoriterank,ci.item_parent_id, ci.item_filename, ci.item_hidden_ext, ci.item_finder_tags, ci.item_xattr_signature, ci.item_trash_put_back_path, ci.item_trash_put_back_parent_id, ci.item_alias_target, ci.item_creator, ci.item_processing_stamp, ci.item_bouncedname, ci.item_scope, ci.item_local_change_count, ci.item_old_version_identifier, ci.fp_creation_item_identifier, ci.version_name, ci.version_ckinfo, ci.version_mtime, ci.version_size, ci.version_thumb_size, ci.version_thumb_signature, ci.version_content_signature, ci.version_xattr_signature, ci.version_edited_since_shared, ci.version_device, ci.version_conflict_loser_etags, ci.version_quarantine_info, ci.version_uploaded_assets, ci.version_upload_error, ci.version_old_zone_item_id, ci.version_old_zone_rowid, ci.version_local_change_count, ci.version_old_version_identifier, ci.item_live_conflict_loser_etags, ci.item_file_id, ci.item_generation FROM client_items AS ci LEFT JOIN client_sync_up AS su ON su.throttle_id = ci.rowid AND su.zone_rowid = ci.zone_rowid LEFT JOIN client_uploads AS cu ON cu.throttle_id = ci.rowid AND cu.zone_rowid = ci.zone_rowid WHERE ci.item_localsyncupstate = 3 AND ci.item_type IN (1, 6) AND (IFNULL(cu.throttle_state, 0) = 0 OR (cu.throttle_state = 31 AND IFNULL(su.throttle_state, 0) = 0))"
- "SELECT csu.throttle_id, csu.last_try_stamp, li.zone_rowid FROM client_sync_up AS csu INNER JOIN client_items AS li ON csu.throttle_id = li.rowid WHERE csu.last_try_stamp > 0 AND csu.last_try_stamp < %lld AND csu.retry_count = 0 AND csu.throttle_state IN (1,50) AND NOT item_id_is_documents(li.item_id) AND li.item_localsyncupstate = 4"
- "T{?=Q*i},R,N,V_logSections"
- "[CRIT] Assertion failed: _symlinkContent.fileSystemRepresentation != nil%@"
- "[CRIT] Assertion failed: baseDaemonContainerPath%@"
- "[DEBUG] %@ - Finished records: %@, Error: %@%@"
- "[DEBUG] Starting the upload operation%@"
- "[DEBUG] already syncing container-metadata%@"
- "[DEBUG] container-metadata needs sync up for %@%@"
- "[DEBUG] marking container-metadata needs-sync-up%@"
- "[DEBUG] preparing to sync up %@%@"
- "[DEBUG] removing staged file for upload: %@%@"
- "[ERROR] nonexistant container %@%@"
- "_garbageCollectUploads"
- "_migrationQueryOperationsQueue"
- "_moveOldUnlinkDir"
- "br_safeFileSystemRepresentation"
- "brc_errorDocumentWithFilename:size:isTooLargeToUpload:"
- "cloneURLToLiveStage:liveStageFilename:error:"
- "cu_%@"
- "initWithTapToRadarManager:analyticsReporter:"
- "internalDaemonContainerPath"
- "migrationQueryMaxOperationCount"
- "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:"
- "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:"
- "requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:"
- "requestTapToRadarWithTitle:description:keywords:attachments:sendFullLog:displayReason:triggerRootCause:completionHandler:"
- "sync.migration-query.max-operation-count"
- "v100@0:8@16@24@32@40q48@56@64B72@76@84@?92"
- "v68@0:8@16@24@32@40B48@52@60"
- "v76@0:8@16@24@32@40B48@52@60@?68"
- "v92@0:8@16@24@32@40q48@56@64B72@76@84"
- "{?=\"sectionID\"Q\"function\"*\"line\"i}"
- "{?=Q*i}16@0:8"

```
