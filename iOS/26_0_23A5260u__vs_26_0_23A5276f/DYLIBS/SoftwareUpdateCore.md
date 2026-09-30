## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.0.15.0.2
-  __TEXT.__text: 0xa3ce8
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x794c
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x150ba
-  __TEXT.__oslogstring: 0xc4b3
+2422.0.31.502.1
+  __TEXT.__text: 0xa41b4
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_methlist: 0x7974
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x150de
+  __TEXT.__oslogstring: 0xc4a1
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x1770
-  __TEXT.__objc_classname: 0x702
-  __TEXT.__objc_methname: 0x1566c
-  __TEXT.__objc_methtype: 0xf9a
-  __TEXT.__objc_stubs: 0xe820
-  __DATA_CONST.__got: 0x888
-  __DATA_CONST.__const: 0x2308
+  __TEXT.__objc_classname: 0x703
+  __TEXT.__objc_methname: 0x1574e
+  __TEXT.__objc_methtype: 0xfbc
+  __TEXT.__objc_stubs: 0xe860
+  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__const: 0x22e8
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43c8
+  __DATA_CONST.__objc_selrefs: 0x43e8
   __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __AUTH_CONST.__auth_got: 0x498
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12920
-  __AUTH_CONST.__objc_const: 0xa550
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__cfstring: 0x12a20
+  __AUTH_CONST.__objc_const: 0xa5b0
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x990
+  __DATA.__objc_ivar: 0x998
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 580ADE56-3BB2-31F4-8CFD-5C779B7A0700
-  Functions: 3008
-  Symbols:   10168
-  CStrings:  8931
+  UUID: F1689F75-C371-36D4-A38C-04F7801F4BDF
+  Functions: 3011
+  Symbols:   10175
+  CStrings:  8954
 
Symbols:
+ +[MAAutoAsset(SUCoreBorderMAAutoAsset) _generateSimulatedResults:bytes:huge:]
+ -[SUCoreDescriptor initWithSUAsset:releaseDate:prepareSize:snapshotPrepareSize:applySize:snapshotApplySize:defaultValues:]
+ -[SUCoreDescriptor installationSnapshotSize]
+ -[SUCoreDescriptor preSUStagingMaxSize]
+ -[SUCoreDescriptor setInstallationSnapshotSize:]
+ -[SUCoreDescriptor setPreSUStagingMaxSize:]
+ GCC_except_table70
+ GCC_except_table77
+ _KSUAssetPreSUStagingMaxSizeKey
+ _MSUAssetCalculateApplySizes
+ _OBJC_IVAR_$_SUCoreDescriptor._installationSnapshotSize
+ _OBJC_IVAR_$_SUCoreDescriptor._preSUStagingMaxSize
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.645
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.646
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.649
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.365
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.380
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.391
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.393
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.981
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1068
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1055
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1053
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1108
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112.cold.1
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1100
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101.cold.1
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1079
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1092
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093.cold.1
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.519
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.520
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.560
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.568
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1088
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1092
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1099
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1149
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1150
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.449
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.569
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.335
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.539
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.345
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.347
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.329
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.334
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.335
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.344
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.615
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.619
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.622
+ ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.334
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.382
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.465
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.471
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.477
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.483
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.489
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.495
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.392
+ ___block_literal_global.404
+ ___block_literal_global.461
+ ___block_literal_global.467
+ ___block_literal_global.473
+ ___block_literal_global.479
+ ___block_literal_global.485
+ ___block_literal_global.491
+ ___block_literal_global.497
+ ___block_literal_global.532
+ ___block_literal_global.542
+ ___block_literal_global.563
+ ___block_literal_global.574
+ ___block_literal_global.621
+ ___block_literal_global.644
+ ___block_literal_global.648
+ _kMobileSoftwareUpdatePreSUStagingMaxSizeKey
+ _objc_msgSend$_generateSimulatedResults:bytes:huge:
+ _objc_msgSend$initWithSUAsset:releaseDate:prepareSize:snapshotPrepareSize:applySize:snapshotApplySize:defaultValues:
+ _objc_msgSend$installationSnapshotSize
+ _objc_msgSend$preSUStagingMaxSize
- +[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]
- -[SUCoreDescriptor initWithSUAsset:releaseDate:prepareSize:applySize:defaultValues:]
- GCC_except_table69
- GCC_except_table76
- _MSUAssetCalculateApplySize
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.639
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.643
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.646
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.362
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.377
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.388
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.390
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.978
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1065
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1052
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1050
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1105
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1109
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1109.cold.1
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1097
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1098
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1098.cold.1
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1076
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1089
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1090
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1090.cold.1
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.516
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.517
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.557
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.565
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1082
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1086
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1093
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1143
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1144
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.446
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.566
- ___66+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]_block_invoke
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.332
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.536
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.339
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.344
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.326
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.331
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.332
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.341
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.612
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.613
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.619
- ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.331
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.379
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.462
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.468
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.474
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.480
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.486
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.492
- ___block_descriptor_40_e8_32s_e23_v28?0B8Q12"NSError"20ls32l8
- ___block_literal_global.328
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.340
- ___block_literal_global.389
- ___block_literal_global.398
- ___block_literal_global.458
- ___block_literal_global.464
- ___block_literal_global.470
- ___block_literal_global.476
- ___block_literal_global.482
- ___block_literal_global.488
- ___block_literal_global.494
- ___block_literal_global.529
- ___block_literal_global.539
- ___block_literal_global.560
- ___block_literal_global.568
- ___block_literal_global.618
- ___block_literal_global.641
- ___block_literal_global.645
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_msgSend$_tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:
- _objc_msgSend$initWithSUAsset:releaseDate:prepareSize:applySize:defaultValues:
CStrings:
+ "           centeralizedPurgeableFactor: %lu\n                 pluginPurgeableFactor: %lu\n                       maxReserveSpace: %llu\n               unentitledReserveAmount: %llu\n              installationSnapshotSize: %llu\n<<<]"
+ "%{public}@ Ignore PSUS assets because required=%llu, optional=%llu, max=%llu"
+ "%{public}@ Using PSUS max size from preferences: %llu"
+ "%{public}@ [PreSUStaging] optional asset to stage: %{public}@"
+ "%{public}@ [PreSUStaging] required asset to stage: %{public}@"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "EncodedUIv2"
+ "InstallationSnapshotSize"
+ "Override descriptor attribute installationSnapshotSize with %{public}@"
+ "Override descriptor attribute msuSnapshotPrepareSize with %{public}@"
+ "PSUSMaxSize"
+ "PreSUStagingMaxSize"
+ "T@\"SUCorePolicy\",&,V_scanPolicy"
+ "TQ,N,V_installationSnapshotSize"
+ "TQ,N,V_preSUStagingMaxSize"
+ "_generateSimulatedResults:bytes:huge:"
+ "_installationSnapshotSize"
+ "_preSUStagingMaxSize"
+ "huge"
+ "initWithSUAsset:releaseDate:prepareSize:snapshotPrepareSize:applySize:snapshotApplySize:defaultValues:"
+ "installationSnapshotSize"
+ "optional-asset1-v2"
+ "optional-asset2-v2"
+ "preSUStagingMaxSize"
+ "required-asset1-v2"
+ "required-asset2-v2"
+ "setInstallationSnapshotSize:"
+ "setPreSUStagingMaxSize:"
+ "v36@0:8^@16^@24B32"
- "           centeralizedPurgeableFactor: %lu\n                 pluginPurgeableFactor: %lu\n                       maxReserveSpace: %llu\n               unentitledReserveAmount: %llu\n<<<]"
- "+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]"
- "+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]_block_invoke"
- "EncodedUI"
- "T@\"SUCorePolicy\",&,N,V_scanPolicy"
- "[SPACE] %s: Failed to release reserved space from the update volume, error: %@, amountPurged: %llu"
- "[SPACE] %s: Releasing space from the update volume, updateVolumeReserveSpaceToRelease: %llu"
- "[SPACE] %s: Successfully released reserved space from the update volume, amountPurged: %llu"
- "[SPACE] %s: Update volume doesn't have any reserved space."
- "[SPACE] Timeout waiting for CD to release reserved space, amount: %llu"
- "_tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:"
- "initWithSUAsset:releaseDate:prepareSize:applySize:defaultValues:"
- "v32@0:8Q16@24"

```
