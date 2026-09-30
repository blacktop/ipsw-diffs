## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.60.8.0.0
-  __TEXT.__text: 0xa5c2c
+2422.60.14.0.2
+  __TEXT.__text: 0xa5c40
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x7a8c
   __TEXT.__const: 0x150

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3370B81-8645-3E20-AFEA-28C0180FEFE6
+  UUID: 8A8BF124-FE49-3867-85CE-87531EB57692
   Functions: 3036
-  Symbols:   10296
+  Symbols:   10297
   CStrings:  9041
 
Symbols:
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.651
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.654
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.655
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.658
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.374
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.389
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.400
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.402
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.990
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1077
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1064
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1062
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1117
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121.cold.1
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1109
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110.cold.1
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1088
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1101
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102.cold.1
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.575
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.576
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.569
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.577
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1103
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1107
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1114
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1164
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1165
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.485
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.538
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.581
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.344
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.548
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.351
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.354
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.356
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.338
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.343
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.353
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.624
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.625
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.628
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.631
+ ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.343
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.391
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.474
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.480
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.486
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.492
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.498
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.504
+ ___block_literal_global.340
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.410
+ ___block_literal_global.413
+ ___block_literal_global.470
+ ___block_literal_global.476
+ ___block_literal_global.482
+ ___block_literal_global.488
+ ___block_literal_global.494
+ ___block_literal_global.500
+ ___block_literal_global.506
+ ___block_literal_global.541
+ ___block_literal_global.551
+ ___block_literal_global.572
+ ___block_literal_global.580
+ ___block_literal_global.583
+ ___block_literal_global.630
+ ___block_literal_global.653
+ ___block_literal_global.657
+ ___chkstk_darwin
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.642
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.645
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.646
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.649
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.365
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.380
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.391
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.393
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.981
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1068
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1055
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1053
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1108
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112.cold.1
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1100
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101.cold.1
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1079
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1092
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093.cold.1
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.566
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.567
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.560
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.568
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1094
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1098
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1105
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1155
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1156
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.476
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.529
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.572
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.335
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.539
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.342
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.345
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.347
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.329
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.334
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.335
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.615
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.616
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.619
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.622
- ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.334
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.382
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.465
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.471
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.477
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.483
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.489
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.495
- ___block_literal_global.331
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.343
- ___block_literal_global.392
- ___block_literal_global.404
- ___block_literal_global.461
- ___block_literal_global.467
- ___block_literal_global.473
- ___block_literal_global.479
- ___block_literal_global.485
- ___block_literal_global.491
- ___block_literal_global.497
- ___block_literal_global.532
- ___block_literal_global.542
- ___block_literal_global.563
- ___block_literal_global.571
- ___block_literal_global.574
- ___block_literal_global.621
- ___block_literal_global.644
- ___block_literal_global.648
Functions:
~ +[SUCoreUpdate _generateStateTable] : 42496 -> 42516

```
