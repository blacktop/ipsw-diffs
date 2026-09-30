## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.0.71.0.1
-  __TEXT.__text: 0xa50e8
+2422.0.80.0.0
+  __TEXT.__text: 0xa5364
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x79d4
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x15345
-  __TEXT.__oslogstring: 0xc548
+  __TEXT.__cstring: 0x15366
+  __TEXT.__oslogstring: 0xc570
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x1770

   __TEXT.__objc_methname: 0x158f6
   __TEXT.__objc_methtype: 0xfcc
   __TEXT.__objc_stubs: 0xe960
-  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__got: 0x928
   __DATA_CONST.__const: 0x2310
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12b60
+  __AUTH_CONST.__cfstring: 0x12b80
   __AUTH_CONST.__objc_const: 0xa710
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x9a8
   __DATA.__data: 0x360
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xcd0
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF2E3BF8-C5AB-3A74-95BB-EF18491E87DE
+  UUID: DDDAB96A-DD8D-3F7D-A8E5-4591C25F2011
   Functions: 3020
-  Symbols:   10233
-  CStrings:  8998
+  Symbols:   10236
+  CStrings:  9000
 
Symbols:
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
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.554
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.555
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.560
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.568
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1091
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1095
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1102
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1152
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1153
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.463
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.517
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.572
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
+ _kSUCoreControllerPreSUStagingMaxSizeKey
+ _kUSCoreControllerSoftwareUpdateReserveRequestedSizeKey
+ _kUSCoreControllerSoftwareUpdateReserveSizeKey
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
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.551
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.552
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.557
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.565
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1088
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1092
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1099
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1149
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1150
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.460
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.514
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.566
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
Functions:
~ -[SUCoreScan actionDeterminePSUSAssetsSuccess:error:] : 1092 -> 1332
~ +[SUCoreEventAugmenter augmentEvent:withDescriptor:specifyAlternateUpdate:] : 1048 -> 1316
~ +[SUCoreSpace getFreeSpaceAvailableForSoftwareUpdate:] : 1432 -> 1560
CStrings:
+ "CACHE_DELETE_ENTITLED_RESERVATION_FREE"
+ "CACHE_DELETE_UNENTITLED_RESERVATION"
+ "[SPACE] Entitled secured space is taken into account, sharedFreeSpace= %llu, entitledFreeSpace= %llu, freeSpaceAvailableForSoftwareUpdate= %llu"
- "CACHE_DELETE_ENTITLED_RESERVATION_SECURED"
- "[SPACE] Entitled secured space is taken into account, sharedFreeSpace= %llu, entitledSecuredSpace= %llu"

```
