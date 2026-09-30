## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4250.0.0.0.2
-  __TEXT.__text: 0x30d05c
+4257.0.20.0.2
+  __TEXT.__text: 0x30e32c
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x19ee4
+  __TEXT.__objc_methlist: 0x1a02c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d0bd
-  __TEXT.__oslogstring: 0x3be6c
-  __TEXT.__gcc_except_tab: 0x1a21c
+  __TEXT.__cstring: 0x7d152
+  __TEXT.__oslogstring: 0x3bf5b
+  __TEXT.__gcc_except_tab: 0x1a3ac
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9ea0
-  __TEXT.__objc_classname: 0x2a7e
-  __TEXT.__objc_methname: 0x43d35
-  __TEXT.__objc_methtype: 0x8f19
-  __TEXT.__objc_stubs: 0x2ec80
+  __TEXT.__unwind_info: 0x9f00
+  __TEXT.__objc_classname: 0x2a9d
+  __TEXT.__objc_methname: 0x441aa
+  __TEXT.__objc_methtype: 0x8fc6
+  __TEXT.__objc_stubs: 0x2ee40
   __DATA_CONST.__got: 0x16f8
   __DATA_CONST.__const: 0x95c8
-  __DATA_CONST.__objc_classlist: 0xa48
+  __DATA_CONST.__objc_classlist: 0xa50
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe560
+  __DATA_CONST.__objc_selrefs: 0xe5f8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x908
+  __DATA_CONST.__objc_superrefs: 0x910
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x2b58
-  __AUTH_CONST.__cfstring: 0x22760
-  __AUTH_CONST.__objc_const: 0x3ccd0
+  __AUTH_CONST.__const: 0x2b78
+  __AUTH_CONST.__cfstring: 0x22860
+  __AUTH_CONST.__objc_const: 0x3cfa0
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x2800
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1f58
+  __DATA.__objc_ivar: 0x1f84
   __DATA.__data: 0x2740
-  __DATA.__bss: 0x238
-  __DATA_DIRTY.__objc_data: 0x3ed0
+  __DATA.__bss: 0x208
+  __DATA_DIRTY.__objc_data: 0x3f20
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x3d8
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CE464469-C3BA-3BB2-AE86-E0E25BA0DABF
-  Functions: 13515
-  Symbols:   44008
-  CStrings:  27564
+  UUID: 17557ABD-3C90-3D12-ADD7-85FB1008D3D7
+  Functions: 13544
+  Symbols:   44086
+  CStrings:  27629
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newMissingPushEventWithNumberOutOfSync:zonesType:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newMissingPushEventWithZonesOutOfSync:zonesType:zonesWithNoRealChanges:]
+ -[BRCAccountSession close].cold.30
+ -[BRCAccountSession periodicSyncInvestigation]
+ -[BRCClientDatabaseFacade getAssetRanksForFileItemsInPackage:]
+ -[BRCContainerMetadataSyncDownOperation performAfterFetchingRecordChanges:].cold.1
+ -[BRCContainerScheduler haveZonesThatNeedsOrInSyncDown]
+ -[BRCDeviceConfiguration initWithAccountFacade:]
+ -[BRCDeviceConfiguration init]
+ -[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:]
+ -[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:].cold.1
+ -[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:].cold.2
+ -[BRCPackageItem setContentSignature:]
+ -[BRCPeriodicSyncInvestigation .cxx_destruct]
+ -[BRCPeriodicSyncInvestigation _shouldCompleteInvestigation]
+ -[BRCPeriodicSyncInvestigation addEditingDevice:]
+ -[BRCPeriodicSyncInvestigation addZoneWithNoRealChanges:]
+ -[BRCPeriodicSyncInvestigation analyticsReporter]
+ -[BRCPeriodicSyncInvestigation close]
+ -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessaryWithOldSyncState:newSyncState:]
+ -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary]
+ -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary].cold.1
+ -[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary].cold.2
+ -[BRCPeriodicSyncInvestigation containerScheduler]
+ -[BRCPeriodicSyncInvestigation editingDevices]
+ -[BRCPeriodicSyncInvestigation initWithZoneAppRetriver:containerScheduler:tapToRadarManager:analyticsReporter:]
+ -[BRCPeriodicSyncInvestigation investigationStarted]
+ -[BRCPeriodicSyncInvestigation setZonesOutOfSync:zonesType:]
+ -[BRCPeriodicSyncInvestigation startInvestigation]
+ -[BRCPeriodicSyncInvestigation startInvestigation].cold.1
+ -[BRCPeriodicSyncInvestigation tapToRadarManager]
+ -[BRCPeriodicSyncInvestigation zoneAppRetriever]
+ -[BRCPeriodicSyncInvestigation zonesOutOfSync]
+ -[BRCPeriodicSyncInvestigation zonesType]
+ -[BRCPeriodicSyncInvestigation zonesWithNoRealChanges]
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:]
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.1
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.2
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.3
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.4
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.5
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.6
+ -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:].cold.7
+ -[BRCSideCarSyncDownOperation _createSyncDownOperation].cold.1
+ -[BRCUserDefaults shouldPerformPeriodicSyncInvestigation]
+ -[BRCZoneHealthCheckOperation main].cold.2
+ GCC_except_table330
+ GCC_except_table570
+ _OBJC_CLASS_$_BRCPeriodicSyncInvestigation
+ _OBJC_IVAR_$_BRCAccountSession._periodicSyncInvestigation
+ _OBJC_IVAR_$_BRCDeviceConfiguration._accountFacade
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._analyticsReporter
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._containerScheduler
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._editingDevices
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._investigationStarted
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._tapToRadarManager
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._zoneAppRetriever
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._zonesOutOfSync
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._zonesType
+ _OBJC_IVAR_$_BRCPeriodicSyncInvestigation._zonesWithNoRealChanges
+ _OBJC_METACLASS_$_BRCPeriodicSyncInvestigation
+ __OBJC_$_INSTANCE_METHODS_BRCPeriodicSyncInvestigation
+ __OBJC_$_INSTANCE_VARIABLES_BRCPeriodicSyncInvestigation
+ __OBJC_$_PROP_LIST_BRCPeriodicSyncInvestigation
+ __OBJC_CLASS_RO_$_BRCPeriodicSyncInvestigation
+ __OBJC_METACLASS_RO_$_BRCPeriodicSyncInvestigation
+ ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.219
+ ___22-[_BRCOperation _main]_block_invoke.cold.1
+ ___26-[BRCAccountSession close]_block_invoke.296
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.18
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.18.cold.1
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.18.cold.2
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.20
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.22
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.24
+ ___35-[BRCZoneHealthCheckOperation main]_block_invoke.24.cold.1
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.318
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.318.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.264
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.267
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.280
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.266
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.266.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.268
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.268.cold.1
+ ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.272
+ ___41-[BRCServerZone deactivateFromClientZone]_block_invoke
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.201
+ ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.201.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.320.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.327
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.327.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.352
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.352.cold.1
+ ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.172
+ ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.175
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.242.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.246
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.256.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.260
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.243
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.1
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.2
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.3
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.250.cold.4
+ ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.257
+ ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.35
+ ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.37
+ ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.13
+ ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.13.cold.1
+ ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.13.cold.2
+ ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.13.cold.3
+ ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.15
+ ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.48
+ ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.48.cold.1
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.39
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.39.cold.1
+ ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.41
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.25
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.29
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.29.cold.1
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.29.cold.2
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.29.cold.3
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.31
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.33.cold.1
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.40
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.41
+ ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke_2.44
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.366
+ ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.53
+ ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.56
+ ___60-[BRCPeriodicSyncInvestigation _shouldCompleteInvestigation]_block_invoke
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.189
+ ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.192
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.382
+ ___66-[BRCFetchRecordSubResourcesOperation saveRecordsWithQueryCursor:]_block_invoke.61
+ ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.161
+ ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.178
+ ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.179
+ ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingAssetContents:]_block_invoke.31
+ ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingRecordChanges:]_block_invoke.18
+ ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingRecordChanges:]_block_invoke.21
+ ___83-[BRCContainerMetadataSyncDownOperation _completedWithServerChangeToken:requestID:]_block_invoke.37
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.358
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.358.cold.1
+ ___block_descriptor_121_e8_32s40s48s56s64bs72r80r88w_e17_v16?0"NSError"8lw88l8s32l8s40l8r72l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72bs80r88r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8s72l8r88l8
+ ___block_descriptor_56_e8_32s40r48r_e40_v32?0"CKRecordZoneID"8"NSError"16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e45_v32?0"CKRecordZoneID"8"CKRecordZone"16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e33_v24?0"CKRecordID"8"NSString"16ls32l8s40l8r48l8
+ ___block_descriptor_65_e8_32s40s48s56r_e18_v16?0"CKRecord"8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_80_e8_32s40r48w_e33_v24?0"CKRecordID"8"NSString"16lw48l8s32l8r40l8
+ ___block_descriptor_81_e8_32s40r48r_e18_v16?0"CKRecord"8lr40l8s32l8r48l8
+ ___block_descriptor_81_e8_32s40r48w_e18_v16?0"CKRecord"8lw48l8r40l8s32l8
+ ___block_descriptor_89_e8_32s40s48r56r_e17_v16?0"NSError"8lr48l8s32l8s40l8r56l8
+ ___block_descriptor_97_e8_32s40s48bs56r64r_e17_v16?0"NSError"8lr56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_97_e8_32s40s48s56r64w_e45_v32?0"CKRecord"8"CKRecordID"16"NSError"24lw64l8s32l8s40l8r56l8s48l8
+ ___block_literal_global.163
+ ___block_literal_global.245
+ ___block_literal_global.252
+ ___block_literal_global.259
+ ___block_literal_global.2873
+ ___block_literal_global.298
+ ___block_literal_global.317
+ ___block_literal_global.329
+ ___block_literal_global.363
+ ___block_literal_global.490
+ ___block_literal_global.942
+ _objc_msgSend$_finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:
+ _objc_msgSend$_shouldCompleteInvestigation
+ _objc_msgSend$addEditingDevice:
+ _objc_msgSend$addZoneWithNoRealChanges:
+ _objc_msgSend$assetRank
+ _objc_msgSend$completeInvestigationIfNecessary
+ _objc_msgSend$completeInvestigationIfNecessaryWithOldSyncState:newSyncState:
+ _objc_msgSend$countOfIndexesInRange:
+ _objc_msgSend$getAssetRanksForFileItemsInPackage:
+ _objc_msgSend$haveZonesThatNeedsOrInSyncDown
+ _objc_msgSend$initWithAccountFacade:
+ _objc_msgSend$initWithZoneAppRetriver:containerScheduler:tapToRadarManager:analyticsReporter:
+ _objc_msgSend$newMissingPushEventWithNumberOutOfSync:zonesType:
+ _objc_msgSend$newMissingPushEventWithZonesOutOfSync:zonesType:zonesWithNoRealChanges:
+ _objc_msgSend$periodicSyncInvestigation
+ _objc_msgSend$requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:
+ _objc_msgSend$scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:
+ _objc_msgSend$setZonesOutOfSync:zonesType:
+ _objc_msgSend$shouldPerformPeriodicSyncInvestigation
+ _objc_msgSend$startInvestigation
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newMissingPushEventWithNumberOutOfSync:]
- +[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]
- -[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:error:]
- -[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:error:].cold.1
- -[BRCFetchRecordSubResourcesOperation finishWithResult:error:].cold.5
- -[BRCPackageItem initWithPBItem:forLocalItem:]
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:]
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.1
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.2
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.3
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.4
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.5
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.6
- -[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:].cold.7
- -[BRCSyncContext cancelWiFiOnlyOperationsIfNeeded].cold.1
- GCC_except_table164
- GCC_except_table445
- GCC_except_table569
- GCC_except_table76
- ___120-[BRCAccountSession _recoverContentPolicyIfNecessaryForItemID:appLibrary:isAppLibraryRoot:isDocumentsFolder:completion:]_block_invoke.218
- ___26-[BRCAccountSession close]_block_invoke.295
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.17
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.17.cold.1
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.17.cold.2
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.19
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.21
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.23
- ___35-[BRCZoneHealthCheckOperation main]_block_invoke.23.cold.1
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.317
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.317.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.262
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.266
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke.279
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.265
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.265.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.267
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_2.267.cold.1
- ___41-[BRCAccountSession _fixupItemsAtStartup]_block_invoke_3.271
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.200
- ___43-[BRCAccountSession _reportBasehashSalting]_block_invoke.200.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.319.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.326
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.326.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.329
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.351
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.351.cold.1
- ___48-[BRCAccountSession openWithError:pushWorkloop:]_block_invoke.171
- ___53-[BRCAccountSession _pcsChainAllItemsWithSystemTask:]_block_invoke.174
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.241.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.245
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.255.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke.259
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.242
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.1
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.2
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.3
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.249.cold.4
- ___53-[BRCAccountSession _registerBackgroundXPCActivities]_block_invoke_2.256
- ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.45
- ___55-[BRCPackageItem(DatabaseMethods) saveToDBWithSession:]_block_invoke.47
- ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.12
- ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.12.cold.1
- ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.12.cold.2
- ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.12.cold.3
- ___55-[BRCSideCarSyncDownOperation _createSyncDownOperation]_block_invoke.14
- ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.42
- ___58-[BRCFetchRecordSubResourcesOperation _scheduleXattrFetch]_block_invoke.42.cold.1
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.33
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.33.cold.1
- ___59-[BRCFetchRecordSubResourcesOperation _scheduleDeserialize]_block_invoke.35
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.18
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.22
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.22.cold.1
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.22.cold.2
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.22.cold.3
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.24
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.26
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.26.cold.1
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke.34
- ___59-[BRCSyncDownOperation _performAfterFetchingRecordChanges:]_block_invoke_2.37
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.364
- ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.47
- ___60-[BRCFetchRecordSubResourcesOperation _prepareToSaveRecords]_block_invoke.50
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.188
- ___61-[BRCAccountSession _saltPartiallySaltedItemsWithSystemTask:]_block_invoke.191
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.381
- ___66-[BRCFetchRecordSubResourcesOperation saveRecordsWithQueryCursor:]_block_invoke.55
- ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke.175
- ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.176
- ___71-[BRCAccountSession(FPFSAdditions) _sendFPFSImportStatusTelemetryEvent]_block_invoke_2.cold.2
- ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingAssetContents:]_block_invoke.30
- ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingRecordChanges:]_block_invoke.17
- ___75-[BRCContainerMetadataSyncDownOperation performAfterFetchingRecordChanges:]_block_invoke.20
- ___83-[BRCContainerMetadataSyncDownOperation _completedWithServerChangeToken:requestID:]_block_invoke.36
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.357
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.357.cold.1
- ___86+[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]_block_invoke
- ___86+[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]_block_invoke.cold.1
- ___86+[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]_block_invoke.cold.2
- ___block_descriptor_112_e8_32s40s48s56s64bs72r80w_e17_v16?0"NSError"8lw80l8s32l8s40l8r72l8s48l8s56l8s64l8
- ___block_descriptor_112_e8_32s40s48s56s64s72bs80r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
- ___block_descriptor_48_e8_32s40r_e40_v32?0"CKRecordZoneID"8"NSError"16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e45_v32?0"CKRecordZoneID"8"CKRecordZone"16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e18_v16?0"CKRecord"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e33_v24?0"CKRecordID"8"NSString"16ls32l8s40l8
- ___block_descriptor_72_e8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
- ___block_descriptor_72_e8_32s40r_e18_v16?0"CKRecord"8ls32l8r40l8
- ___block_descriptor_72_e8_32s40w_e18_v16?0"CKRecord"8lw40l8s32l8
- ___block_descriptor_72_e8_32s40w_e33_v24?0"CKRecordID"8"NSString"16lw40l8s32l8
- ___block_descriptor_80_e8_32s40s48w_e45_v32?0"CKRecord"8"CKRecordID"16"NSError"24lw48l8s32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e12_v24?0Q8^B16ls32l8r64l8r72l8r80l8s40l8s48l8s56l8
- ___block_literal_global.236
- ___block_literal_global.251
- ___block_literal_global.258
- ___block_literal_global.2870
- ___block_literal_global.297
- ___block_literal_global.304
- ___block_literal_global.316
- ___block_literal_global.328
- ___block_literal_global.489
- ___block_literal_global.934
- _objc_msgSend$_finishPackageUploadWithRecord:item:stageID:error:
- _objc_msgSend$hasXattrs
- _objc_msgSend$item
- _objc_msgSend$newMissingPushEventWithNumberOutOfSync:
- _objc_msgSend$scheduleSyncDownIfNeededForZoneID:zoneIfAny:
- _objc_msgSend$updateSignaturesForFilesInItem:fromCKPackage:error:
CStrings:
+ " Please collect sysdiagnose from these devices if you own them: %@.\n"
+ " operation cancelled."
+ " periodic sync."
+ "%lu zone(s) with no real changes."
+ "-[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:]"
+ "-[BRCPeriodicSyncInvestigation completeInvestigationIfNecessary]"
+ "-[BRCPeriodicSyncInvestigation startInvestigation]"
+ "-[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:]"
+ "-[BRCSideCarSyncDownOperation _createSyncDownOperation]"
+ "-[_BRCOperation _main]_block_invoke"
+ "@\"BRCPeriodicSyncInvestigation\""
+ "@\"BRCPeriodicSyncInvestigation\"16@0:8"
+ "@\"NSIndexSet\"24@0:8@\"BRCDocumentItem\"16"
+ "@24@0:8I16I20"
+ "@28@0:8S16C20S24"
+ "B40@0:8@16@24^C32"
+ "BRCPeriodicSyncInvestigation"
+ "Found zones not synced with the server"
+ "Found zones not synced with the server.\n%@%@"
+ "INSERT INTO client_pkg_upload_items (item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode) VALUES (%llu, %@, %u, %llu, %llu, %@, %@, %llu, %@, %llu, %u)"
+ "MISSING_PUSH_V2"
+ "SELECT asset_rank  FROM client_pkg_upload_items  WHERE item_rowid = %llu AND item_type = %d"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode  FROM client_pkg_upload_items  ORDER BY item_rowid, rel_path"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY asset_rank"
+ "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY rel_path"
+ "T@\"<BRCZoneAppRetriever>\",R,N,V_zoneAppRetriever"
+ "T@\"BRCPeriodicSyncInvestigation\",R,N"
+ "T@\"BRCPeriodicSyncInvestigation\",R,N,V_periodicSyncInvestigation"
+ "T@\"BRCTapToRadarManager\",R,N,V_tapToRadarManager"
+ "T@\"NSMutableSet\",R,N,V_editingDevices"
+ "T@\"NSMutableSet\",R,N,V_zonesWithNoRealChanges"
+ "TB,R,N,V_investigationStarted"
+ "TC,R,N,V_zonesType"
+ "TS,R,N,V_zonesOutOfSync"
+ "[DEBUG] %@ %@ finished record fetcher.%@%@"
+ "[DEBUG] Received notification response %@ for request %@%@"
+ "[DEBUG] These are the editing devices: %@%@"
+ "[DEBUG] These are the zones with no real changes: %@%@"
+ "[DEBUG] This is a periodic sync%@"
+ "[DEBUG] starting main %@%@"
+ "[DEBUG] starting periodic sync investigation%@"
+ "[DEBUG] ┏%llx closing _periodicSyncInvestigation...%@"
+ "[ERROR] Couldn't add %@ to checksummer - error %@%@"
+ "[ERROR] Couldn't get CKPackageItem for index %lld with error %@%@"
+ "[INFO] ┣%llx %@ fetch record changes operation for %@ from token %@. %@%@"
+ "[NOTICE] Request for diagnostic collection returned with error: %@%@"
+ "[NOTICE] Triggering TTR due to stuck migration%@"
+ "[NOTICE] Triggering request for diagnostic collection from file provider%@"
+ "[Periodic Sync] Found zones not synced with the server"
+ "_editingDevices"
+ "_finishPackageUploadWithRecord:item:stageID:packageChecksummer:error:"
+ "_investigationStarted"
+ "_periodicSyncInvestigation"
+ "_shouldCompleteInvestigation"
+ "_zonesOutOfSync"
+ "_zonesType"
+ "_zonesWithNoRealChanges"
+ "addEditingDevice:"
+ "addZoneWithNoRealChanges:"
+ "completeInvestigationIfNecessary"
+ "completeInvestigationIfNecessaryWithOldSyncState:newSyncState:"
+ "countOfIndexesInRange:"
+ "editingDevices"
+ "getAssetRanksForFileItemsInPackage:"
+ "haveZonesThatNeedsOrInSyncDown"
+ "initWithAccountFacade:"
+ "initWithZoneAppRetriver:containerScheduler:tapToRadarManager:analyticsReporter:"
+ "investigationStarted"
+ "newMissingPushEventWithNumberOutOfSync:zonesType:"
+ "newMissingPushEventWithZonesOutOfSync:zonesType:zonesWithNoRealChanges:"
+ "periodicSyncInvestigation"
+ "requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:"
+ "scheduleSyncDownIfNeededForZoneID:zoneIfAny:zoneType:"
+ "setZonesOutOfSync:zonesType:"
+ "shouldPerformPeriodicSyncInvestigation"
+ "startInvestigation"
+ "sync.should-perform-periodic-sync-investigations"
+ "v24@0:8S16C20"
+ "zonesOutOfSync"
+ "zonesType"
+ "zonesWithNoRealChanges"
- "+[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]"
- "+[BRCPackageItem(DatabaseMethods) updateSignaturesForFilesInItem:fromCKPackage:error:]_block_invoke"
- "-[BRCFSUploader _finishPackageUploadWithRecord:item:stageID:error:]"
- "-[BRCPeriodicSyncOperation scheduleSyncDownIfNeededForZoneID:zoneIfAny:]"
- "-[BRCSyncContext cancelWiFiOnlyOperationsIfNeeded]"
- "INSERT INTO client_pkg_upload_items (item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode) VALUES (%llu, %@, %u, %llu, %llu, %@, %@, %llu, %@, %@, %llu, %u)"
- "SELECT asset_rank, generation  FROM client_pkg_upload_items WHERE item_rowid = %llu AND item_type = %d"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode  FROM client_pkg_upload_items  ORDER BY item_rowid, rel_path"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY asset_rank"
- "SELECT item_rowid, rel_path, item_type, asset_rank, file_id, quarantine_info, xattr_signature, mtime, signature_or_link, generation, size, mode FROM client_pkg_upload_items WHERE item_rowid = %llu ORDER BY rel_path"
- "UPDATE client_pkg_upload_items SET signature_or_link = %@ WHERE item_rowid = %llu AND asset_rank = %ld"
- "[CRIT] UNREACHABLE: updating asset signature should work%@"
- "[CRIT] UNREACHABLE: wrong number of items in package. pkg [%@] assetRanks [%lu]%@"
- "[DEBUG] %@ finished record fetcher%@"
- "[DEBUG] Failing updates of signatures for item %@ because pkg item with rank %lu changed%@"
- "[DEBUG] Learning signature for rank %ld, signature:%@, asset %@%@"
- "[DEBUG] Received notificaiton respose %@ for request %@%@"
- "[DEBUG] Triggering TTR due to stuck migration%@"
- "[INFO] ┣%llx %@ fetch record changes operation for %@ from token %@%@"
- "_finishPackageUploadWithRecord:item:stageID:error:"
- "initWithPBItem:forLocalItem:"
- "newMissingPushEventWithNumberOutOfSync:"
- "scheduleSyncDownIfNeededForZoneID:zoneIfAny:"
- "updateSignaturesForFilesInItem:fromCKPackage:error:"

```
