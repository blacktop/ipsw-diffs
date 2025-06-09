## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0x9fcd8
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x76cc
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1485d
-  __TEXT.__oslogstring: 0xb941
-  __TEXT.__gcc_except_tab: 0x750
+2422.0.15.0.2
+  __TEXT.__text: 0xa3ce8
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0x794c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x150ba
+  __TEXT.__oslogstring: 0xc4b3
+  __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x16e0
-  __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0x14c53
-  __TEXT.__objc_methtype: 0xf66
-  __TEXT.__objc_stubs: 0xe3a0
+  __TEXT.__unwind_info: 0x1770
+  __TEXT.__objc_classname: 0x702
+  __TEXT.__objc_methname: 0x1566c
+  __TEXT.__objc_methtype: 0xf9a
+  __TEXT.__objc_stubs: 0xe820
   __DATA_CONST.__got: 0x888
-  __DATA_CONST.__const: 0x2260
+  __DATA_CONST.__const: 0x2308
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4210
+  __DATA_CONST.__objc_selrefs: 0x43c8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x12340
-  __AUTH_CONST.__objc_const: 0xa190
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x12920
+  __AUTH_CONST.__objc_const: 0xa550
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x944
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x990
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E2545C7-0D53-3729-A1D9-5B597A1AFE9E
-  Functions: 2936
-  Symbols:   9947
-  CStrings:  8690
+  UUID: 580ADE56-3BB2-31F4-8CFD-5C779B7A0700
+  Functions: 3008
+  Symbols:   10168
+  CStrings:  8931
 
Symbols:
+ +[SUCorePolicyExtensionCompanionCompatibility sharedInstance]
+ +[SUCorePolicyExtensionCompanionCompatibility sharedInstance].cold.1
+ +[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]
+ +[SUCoreSpace cacheDeleteDisableReserveSpace]
+ +[SUCoreSpace cacheDeleteGetReserveSpace:withError:]
+ +[SUCoreSpace cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:]
+ +[SUCoreSpace cacheDeletePauseReserveSpace:withPurpose:]
+ +[SUCoreSpace cacheDeleteResumeReserveSpace]
+ +[SUCoreSpace cacheDeleteSetReserveSpace:systemGrowthMarginSize:]
+ +[SUCoreSpace cacheDeleteSetReserveSpaceWithInfo:]
+ +[SUCoreSpace getFreeSpaceAvailableForSoftwareUpdate:]
+ +[SUCoreSpace getVolumeUsedSpace:]
+ -[SUCoreDescriptor centeralizedPurgeableFactor]
+ -[SUCoreDescriptor disableReserveSpace]
+ -[SUCoreDescriptor maxReserveSpace]
+ -[SUCoreDescriptor msuSnapshotPrepareSize]
+ -[SUCoreDescriptor pluginPurgeableFactor]
+ -[SUCoreDescriptor safariUpdateContentBundleURL]
+ -[SUCoreDescriptor setCenteralizedPurgeableFactor:]
+ -[SUCoreDescriptor setDisableReserveSpace:]
+ -[SUCoreDescriptor setMaxReserveSpace:]
+ -[SUCoreDescriptor setMsuSnapshotPrepareSize:]
+ -[SUCoreDescriptor setPluginPurgeableFactor:]
+ -[SUCoreDescriptor setUnentitledReserveAmount:]
+ -[SUCoreDescriptor snapshotPreparationSize]
+ -[SUCoreDescriptor totalRequiredFreeSpaceHelper:]
+ -[SUCoreDescriptor totalSnapshotRequiredFreeSpace]
+ -[SUCoreDescriptor unentitledReserveAmount]
+ -[SUCoreDocumentation safariUpdateContentBundleURL]
+ -[SUCoreDocumentation setSafariUpdateContentBundleURL:]
+ -[SUCorePolicy reserveSpaceSizeOverride]
+ -[SUCorePolicy setReserveSpaceSizeOverride:]
+ -[SUCorePolicy setSystemGrowthMarginOverride:]
+ -[SUCorePolicy setUseReserveSpace:]
+ -[SUCorePolicy systemGrowthMarginOverride]
+ -[SUCorePolicy useReserveSpace]
+ -[SUCorePolicyExtensionCompanionCompatibility allowSameVersionUpdates]
+ -[SUCorePolicyExtensionCompanionCompatibility assetOutOfCompatibilityRange]
+ -[SUCorePolicyExtensionCompanionCompatibility buildVersion]
+ -[SUCorePolicyExtensionCompanionCompatibility extendMSUApplyOptions:]
+ -[SUCorePolicyExtensionCompanionCompatibility logger]
+ -[SUCorePolicyExtensionCompanionCompatibility operationsQueue]
+ -[SUCorePolicyExtensionCompanionCompatibility preferFullReplacement]
+ -[SUCorePolicyExtensionCompanionCompatibility setAllowSameVersionUpdates:]
+ -[SUCorePolicyExtensionCompanionCompatibility setBuildVersion:]
+ -[SUCorePolicyExtensionCompanionCompatibility setCompatibilityVersionRange:maxCompatibilityVersion:]
+ -[SUCorePolicyExtensionCompanionCompatibility setPreferFullReplacement:]
+ -[SUCorePolicyExtensionCompanionCompatibility setSuAssetDownloadOptions:]
+ -[SUCorePolicyExtensionCompanionCompatibility suAssetDownloadOptions]
+ -[SUCoreScan _decideReserveSpace:]
+ -[SUCoreScan actionPerformReserveSpace:]
+ -[SUCoreSpace entitledSpaceDisabled]
+ -[SUCoreSpace reserveSpacePaused]
+ -[SUCoreSpace setEntitledSpaceDisabled:]
+ -[SUCoreSpace setReserveSpacePaused:]
+ GCC_except_table100
+ _CacheDeleteDisableReserveSpace
+ _CacheDeleteGetReserveSpace
+ _CacheDeletePauseReserveSpaceMonitoring
+ _CacheDeleteSetEntitledAndUnentitledReservation
+ _CacheDeleteSetEntitledReservation
+ _CacheDeleteSetReserveSpaceWithInfo
+ _MSUAssetCalculatePrepareSizes
+ _OBJC_IVAR_$_SUCoreDescriptor._centeralizedPurgeableFactor
+ _OBJC_IVAR_$_SUCoreDescriptor._disableReserveSpace
+ _OBJC_IVAR_$_SUCoreDescriptor._maxReserveSpace
+ _OBJC_IVAR_$_SUCoreDescriptor._msuSnapshotPrepareSize
+ _OBJC_IVAR_$_SUCoreDescriptor._pluginPurgeableFactor
+ _OBJC_IVAR_$_SUCoreDescriptor._unentitledReserveAmount
+ _OBJC_IVAR_$_SUCoreDocumentation._safariUpdateContentBundleURL
+ _OBJC_IVAR_$_SUCorePolicy._reserveSpaceSizeOverride
+ _OBJC_IVAR_$_SUCorePolicy._systemGrowthMarginOverride
+ _OBJC_IVAR_$_SUCorePolicy._useReserveSpace
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._allowSameVersionUpdates
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._assetOutOfCompatibilityRange
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._buildVersion
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._logger
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._operationsQueue
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._preferFullReplacement
+ _OBJC_IVAR_$_SUCorePolicyExtensionCompanionCompatibility._suAssetDownloadOptions
+ _OBJC_IVAR_$_SUCoreSpace._entitledSpaceDisabled
+ _OBJC_IVAR_$_SUCoreSpace._reserveSpacePaused
+ ___100-[SUCorePolicyExtensionCompanionCompatibility setCompatibilityVersionRange:maxCompatibilityVersion:]_block_invoke
+ ___100-[SUCorePolicyExtensionCompanionCompatibility setCompatibilityVersionRange:maxCompatibilityVersion:]_block_invoke.cold.1
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.639
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.642
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.643
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.646
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.362
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.377
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.388
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.390
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.978
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1065
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1052
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1050
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1105
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1109
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1109.cold.1
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1097
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1098
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1098.cold.1
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1076
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1089
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1090
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1090.cold.1
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.516
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.517
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.557
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.565
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1082
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1086
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1093
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1143
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1144
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.530.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.532.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.446
+ ___61+[SUCorePolicyExtensionCompanionCompatibility sharedInstance]_block_invoke
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.566
+ ___66+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]_block_invoke
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.332
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.536
+ ___72-[SUCorePolicyExtensionCompanionCompatibility setPreferFullReplacement:]_block_invoke
+ ___73-[SUCorePolicyExtensionCompanionCompatibility setSuAssetDownloadOptions:]_block_invoke
+ ___74-[SUCorePolicyExtensionCompanionCompatibility setAllowSameVersionUpdates:]_block_invoke
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.342
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.344
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.326
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.331
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.332
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.341
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke_2
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke_3
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke_4
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.612
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.613
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.616
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.619
+ ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.331
+ ___90-[SUCorePolicyExtensionCompanionCompatibility extendMASoftwareUpdateAssetDownloadOptions:]_block_invoke
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.379
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.462
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.468
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.474
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.480
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.486
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.492
+ ___block_descriptor_40_e8_32s_e23_v28?0B8Q12"NSError"20ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.328
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.340
+ ___block_literal_global.389
+ ___block_literal_global.401
+ ___block_literal_global.458
+ ___block_literal_global.464
+ ___block_literal_global.470
+ ___block_literal_global.476
+ ___block_literal_global.482
+ ___block_literal_global.488
+ ___block_literal_global.494
+ ___block_literal_global.529
+ ___block_literal_global.539
+ ___block_literal_global.560
+ ___block_literal_global.571
+ ___block_literal_global.618
+ ___block_literal_global.641
+ ___block_literal_global.645
+ __os_feature_enabled_impl
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _kCompanionCompatExtensionAllowsCellularAccess
+ _kCompanionCompatExtensionDownloadIsDiscretionary
+ _kCompanionCompatExtensionRequiresPowerPluggedIn
+ _kCompanionCompatExtensionResourceTimeout
+ _kSUAssetSUCenteralizedPurgeableFactor
+ _kSUAssetSUDisableReserveSpace
+ _kSUAssetSUMaxReserveSpace
+ _kSUAssetSUPluginPurgeableFactor
+ _kSUAssetSUUnentitledReserveAmount
+ _kSU_M_CacheDeleteSetReserveSpace
+ _objc_msgSend$_decideReserveSpace:
+ _objc_msgSend$_tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:
+ _objc_msgSend$actionPerformReserveSpace:
+ _objc_msgSend$allowSameVersionUpdates
+ _objc_msgSend$assetOutOfCompatibilityRange
+ _objc_msgSend$cacheDeleteGetReserveSpace:withError:
+ _objc_msgSend$cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:
+ _objc_msgSend$cacheDeleteSetReserveSpaceWithInfo:
+ _objc_msgSend$centeralizedPurgeableFactor
+ _objc_msgSend$disableReserveSpace
+ _objc_msgSend$entitledSpaceDisabled
+ _objc_msgSend$getFreeSpaceAvailableForSoftwareUpdate:
+ _objc_msgSend$getVolumeUsedSpace:
+ _objc_msgSend$longValue
+ _objc_msgSend$maxReserveSpace
+ _objc_msgSend$msuSnapshotPrepareSize
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$operationsQueue
+ _objc_msgSend$pluginPurgeableFactor
+ _objc_msgSend$preferFullReplacement
+ _objc_msgSend$reserveSpacePaused
+ _objc_msgSend$reserveSpaceSizeOverride
+ _objc_msgSend$safariUpdateContentBundleURL
+ _objc_msgSend$safeULForKey:
+ _objc_msgSend$safeULForKey:defaultValue:
+ _objc_msgSend$setEntitledSpaceDisabled:
+ _objc_msgSend$setReserveSpacePaused:
+ _objc_msgSend$setSafariUpdateContentBundleURL:
+ _objc_msgSend$setTaskDescription:
+ _objc_msgSend$setUseReserveSpace:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$snapshotPreparationSize
+ _objc_msgSend$suAssetDownloadOptions
+ _objc_msgSend$systemGrowthMarginOverride
+ _objc_msgSend$totalRequiredFreeSpaceHelper:
+ _objc_msgSend$totalSnapshotRequiredFreeSpace
+ _objc_msgSend$unentitledReserveAmount
+ _objc_msgSend$useReserveSpace
- GCC_except_table98
- _MSUAssetCalculatePrepareSize
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.633
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.636
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.637
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.640
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.359
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.374
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.385
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.387
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.975
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1062
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1049
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1047
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1102
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1106
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1106.cold.1
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1094
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1095
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1095.cold.1
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1073
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1086
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1087
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1087.cold.1
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.513
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.514
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.554
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.562
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1064
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1068
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1075
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1125
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1126
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.527
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.527.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.529
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.529.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.443
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.508
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.329
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.533
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.336
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.341
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.606
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.607
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.610
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.613
- ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.328
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.376
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.459
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.465
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.471
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.477
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.483
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.489
- ___block_literal_global.325
- ___block_literal_global.330
- ___block_literal_global.386
- ___block_literal_global.395
- ___block_literal_global.455
- ___block_literal_global.461
- ___block_literal_global.467
- ___block_literal_global.473
- ___block_literal_global.479
- ___block_literal_global.485
- ___block_literal_global.491
- ___block_literal_global.526
- ___block_literal_global.536
- ___block_literal_global.557
- ___block_literal_global.565
- ___block_literal_global.612
- ___block_literal_global.635
- ___block_literal_global.639
- _objc_msgSend$setMaxCompatibility:
- _objc_msgSend$setMinCompatibility:
CStrings:
+ "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n     securityAdvisoryNotificationTitle: %@\n      securityAdvisoryNotificationBody: %@\n  deviceCompatibilityNotificationTitle: %@\n   deviceCompatibilityNotificationBody: %@\n          safariUpdateContentBundleURL: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                msuSnapshotPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                   disableReserveSpace: %@\n                        suDownloadSize: %llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n"
+ "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n    securityAdvisoryNotificationTitleString: %@\n     securityAdvisoryNotificationBodyString: %@\n deviceCompatibilityNotificationTitleString: %@\n  deviceCompatibilityNotificationBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n               safariUpdateContentBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n                    encodedUIBundleFileName: %@\n<<<]"
+ "\n[>>>\n    SubPolicies(specifiedUsedPolicies:0x%llX)\n%@    AssetTypes(softwareUpdateAssetType:%@|documentationAssetType:%@)\n    Versions(prerequisiteBuildVersion:%@|prerequisiteProductVersion:%@|prerequisiteRestoreVersion:%@|targetRestoreVersion:%@|installedSFRVersion:%@)\n    Device(deviceClass:%@|hwModelStr:%@|productType:%@|releaseType:%@|isInternal:%@)\n    Config(restrictToFull:%@|allowSameVersion:%@|background:%@|allowsCellular:%@|checkAvailableSpace:%@|useReserveSpace:%@|cacheDeleteUrgency:%@|userAgentString:%@|userInitiated:%@|skipVolumeSealing:%@|qualityOfService:%@)\n    Target(targetVolumeUUID:%@|updateVolumePath:%@)\n    Preflight(performPreflightEncryptedCheck:%@|performPreflightSnapshotCheck:%@|updateBrainLocationOverride:%@)\n    Personalization(SSOToken:%@|personalizedManifestRootsPath:%@|personalizationServerURL:%@|proxyHostName:%@|proxyPortNumber:%@)\n    Authentication(localAuthenticationContext:%@|downloadAuthorizationHeader:%@|localAuthenticationUserID:%@|mdmBootstrapToken:%@)\n    BridgeOS(bridgeOSIgnoreMinimumVersionCheck:%@|bridgeOSDownloadDirectory:%@|enableEmbeddedOSInstall:%@|enableBridgeOSInstall:%@|enableOSPersonalization:%@)\n    Metrics(updateMetricEventFields:%@|updateMetricContext:%@\n    Defaults(defaultDescriptorValues:%@|assetAudienceUUID:%@|alternateAssetAudienceUUID:%@|disableAlternateUpdate:%@|disableSplombo:%@|mobileAssetPurposeOverride:%@)\n    PSUS(enable:%@|enableForOptionalAssets:%@)\n    Extensions(%@)\n<<<]"
+ "           centeralizedPurgeableFactor: %lu\n                 pluginPurgeableFactor: %lu\n                       maxReserveSpace: %llu\n               unentitledReserveAmount: %llu\n<<<]"
+ "%{public}@ Asset for build %@ is within compatibility range"
+ "%{public}@ Extending download options with overrides: %@"
+ "%{public}@ Found %lu potential assets after filtering on build version"
+ "%{public}@ Found asset for build %@ for a device with no companion"
+ "%{public}@ Found asset for build %@ which does not require a companion update"
+ "%{public}@ Found asset for build %@ which requires a companion update"
+ "%{public}@ Found asset for build %@ with CompatibilityVersion = %{public}@"
+ "%{public}@ No SoftwareUpdate assets found"
+ "%{public}@ Not extending download options since no overrides set"
+ "%{public}@ Performing compatibility version filtering on remaining %lu assets"
+ "%{public}@ Updating to same OS version is *NOT* allowed"
+ "%{public}@ Updating to same OS version is allowed"
+ "%{public}@ starting asset filtering, starting with %lu assets"
+ "+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]"
+ "+[SUCoreSpace _tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:]_block_invoke"
+ "+[SUCoreSpace cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:]"
+ "+[SUCoreSpace cacheDeleteResumeReserveSpace]"
+ "+[SUCoreSpace cacheDeleteSetReserveSpaceWithInfo:]"
+ "-[SUCoreScan actionPerformReserveSpace:]"
+ "AllowsSameVersionUpdates"
+ "AssetOutOfCompatibilityRange"
+ "CACHE_DELETE_ENTITLED_RESERVATION"
+ "CACHE_DELETE_ENTITLED_RESERVATION_SECURED"
+ "CACHE_DELETE_EXPECTED_SYSTEM_GROWTH_AMOUNT"
+ "CACHE_DELETE_EXTRA_SHARED_FREE"
+ "CACHE_DELETE_FACTOR_FOR_CENTRALIZED_PURGEABLE"
+ "CACHE_DELETE_FACTOR_FOR_PLUGIN_PURGEABLE"
+ "CACHE_DELETE_MAX_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RELEASE_SPACE"
+ "CACHE_DELETE_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RESERVE_SPACE_FILESYSTEM_AMOUNT"
+ "CACHE_DELETE_UNENTITLED_CD_THRESHOLD"
+ "CacheDeleteSetReserveSpace"
+ "CenteralizedPurgeableFactor"
+ "ClearingToEnlargeEntitledSpace"
+ "CompanionCompatPolicyExt"
+ "DisableReserveSpace"
+ "Disabled"
+ "DownloadAllowedOverCellular"
+ "DownloadIsDiscretionary"
+ "DownloadRequiresPowerPluggedIn"
+ "EXISTS"
+ "Incorrect arguments passed to setCompatibilityVersionRange: minCompatibilityVersion: %@ maxCompatibilityVersion: %@"
+ "MSUSnapshotPrepareSize"
+ "MaxReserveSpace"
+ "NA"
+ "PerformReserveSpace"
+ "PluginPurgeableFactor"
+ "PreallocatedSpace"
+ "PreferFullReplacement"
+ "Q20@0:8B16"
+ "Q24@0:8@16"
+ "RESERVE_SPACE_PERFORMED"
+ "ReserveSpace"
+ "ResourceTimeout"
+ "ResumeReserveSpace"
+ "SUAssetDownloadOptions"
+ "SUCenteralizedPurgeableFactor"
+ "SUDisableReserveSpace"
+ "SUMaxReserveSpace"
+ "SUPluginPurgeableFactor"
+ "SUUnentitledReserveAmount"
+ "SafariUpdateContentBundleURL"
+ "SafariWhatsNew"
+ "SimulatedSafariUpdateContentBundleURL"
+ "SoftwareUpdate"
+ "T@\"NSDictionary\",&,N,V_suAssetDownloadOptions"
+ "T@\"NSNumber\",&,N,V_reserveSpaceSizeOverride"
+ "T@\"NSNumber\",&,N,V_systemGrowthMarginOverride"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_operationsQueue"
+ "T@\"NSString\",&,N,V_buildVersion"
+ "T@\"NSURL\",&,V_safariUpdateContentBundleURL"
+ "T@\"NSURL\",R,&,N"
+ "T@\"SUCoreLog\",R,&,N,V_logger"
+ "TB,N,V_allowSameVersionUpdates"
+ "TB,N,V_disableReserveSpace"
+ "TB,N,V_entitledSpaceDisabled"
+ "TB,N,V_preferFullReplacement"
+ "TB,N,V_reserveSpacePaused"
+ "TB,N,V_useReserveSpace"
+ "TB,R,N,V_assetOutOfCompatibilityRange"
+ "TQ,N,V_centeralizedPurgeableFactor"
+ "TQ,N,V_maxReserveSpace"
+ "TQ,N,V_msuSnapshotPrepareSize"
+ "TQ,N,V_pluginPurgeableFactor"
+ "TQ,N,V_unentitledReserveAmount"
+ "TQ,R,N"
+ "UnentitledReserveAmount"
+ "UseReserveSpace"
+ "[DOCUMENTATION] Unable to load safariUpdateContentBundleURL: %{public}@"
+ "[Prealloc Space] %s, isReserveSpaceDisabled: %@, anyUpdateIsIncremental: %@, shouldUseReserveSpace: %@"
+ "[SPACE] %s: APFS entitled space is %@"
+ "[SPACE] %s: Failed to release reserved space from the update volume, error: %@, amountPurged: %llu"
+ "[SPACE] %s: Releasing space from the update volume, updateVolumeReserveSpaceToRelease: %llu"
+ "[SPACE] %s: Successfully released reserved space from the update volume, amountPurged: %llu"
+ "[SPACE] %s: Update volume doesn't have any reserved space."
+ "[SPACE] %s: resuming CacheDelete purgeable monitor"
+ "[SPACE] %s: trying to resume reserve space while the monitor is not paused"
+ "[SPACE] %s: trying to set reserve space while in paused state, %{public}@"
+ "[SPACE] Calculating Free space using statfs"
+ "[SPACE] Checking reserved space in the update volume from CacheDelete"
+ "[SPACE] Clearing APFS entitled reserve space because we got a bigger space to reserve, existingEntitledSpace:%@, entitledSpace:%@"
+ "[SPACE] Disabling reserve space"
+ "[SPACE] Entitled secured space is empty, let's deduct the unentitled threshold from the shared space, sharedFreeSpace= %llu, unentitledThreshold= %llu, freeSpaceAvilableForSoftwareUpdate= %llu"
+ "[SPACE] Entitled secured space is taken into account, sharedFreeSpace= %llu, entitledSecuredSpace= %llu"
+ "[SPACE] Invalid reserved type"
+ "[SPACE] Pause cache delete reserve space monitoring"
+ "[SPACE] Pause cache delete reserve space monitoring and set entitled reservation, existingEntitledSpace:%llu entitledSpace:%@ with purpose:%@"
+ "[SPACE] Timeout waiting for CD to release reserved space, amount: %llu"
+ "[SPACE] Unable to get reserve space info from cache delete, Error: %@"
+ "[SPACE] Unable to get reserve space, error: %@"
+ "[SPACE] entitled space is already disabled, return sharedFreeSpace as available for software update. sharedFreeSpace= %llu"
+ "[SPACE] free space is less than unentitled threshold, disable setting entitled space for software update. sharedFreeSpace= %llu, unentitledThreshold= %llu, freeSpaceAvilableForSoftwareUpdate= %llu"
+ "[SPACE] reserved space is enough, skip checking for purgeable content"
+ "[SPACE] unentitled threshold from CD is 0!"
+ "_allowSameVersionUpdates"
+ "_assetOutOfCompatibilityRange"
+ "_buildVersion"
+ "_centeralizedPurgeableFactor"
+ "_decideReserveSpace:"
+ "_disableReserveSpace"
+ "_entitledSpaceDisabled"
+ "_maxReserveSpace"
+ "_msuSnapshotPrepareSize"
+ "_operationsQueue"
+ "_pluginPurgeableFactor"
+ "_preferFullReplacement"
+ "_reserveSpacePaused"
+ "_reserveSpaceSizeOverride"
+ "_safariUpdateContentBundleURL"
+ "_suAssetDownloadOptions"
+ "_systemGrowthMarginOverride"
+ "_tryReleaseSpaceFromUpdateVolume:reservedSpaceInfo:"
+ "_unentitledReserveAmount"
+ "_useReserveSpace"
+ "actionPerformReserveSpace:"
+ "allowSameVersionUpdates"
+ "assetOutOfCompatibilityRange"
+ "cacheDeleteDisableReserveSpace"
+ "cacheDeleteGetReserveSpace:withError:"
+ "cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:"
+ "cacheDeletePauseReserveSpace:withPurpose:"
+ "cacheDeleteResumeReserveSpace"
+ "cacheDeleteSetReserveSpace:systemGrowthMarginSize:"
+ "cacheDeleteSetReserveSpaceWithInfo:"
+ "centeralizedPurgeableFactor"
+ "check for available space failed, basePath=%@"
+ "com.apple.SUCore:totalRequired"
+ "com.apple.sucore.policyExtensionCompanionCompatibilityQueue"
+ "disableReserveSpace"
+ "entitledSpaceDisabled"
+ "getFreeSpaceAvailableForSoftwareUpdate:"
+ "getVolumeUsedSpace:"
+ "longValue"
+ "maxReserveSpace"
+ "msuSnapshotPrepareSize"
+ "not CFDictionaryRef"
+ "numberWithUnsignedLong:"
+ "operationsQueue"
+ "pluginPurgeableFactor"
+ "preferFullReplacement"
+ "q32@0:8^@16^@24"
+ "reserveSpacePaused"
+ "reserveSpaceSizeOverride"
+ "result provided by CacheDeleteGetReserveSpace is %@ - ignored"
+ "safariUpdateContentBundleURL"
+ "safeULForKey:"
+ "safeULForKey:defaultValue:"
+ "setAllowSameVersionUpdates:"
+ "setBuildVersion:"
+ "setCenteralizedPurgeableFactor:"
+ "setCompatibilityVersionRange:maxCompatibilityVersion:"
+ "setDisableReserveSpace:"
+ "setEntitledSpaceDisabled:"
+ "setMaxReserveSpace:"
+ "setMsuSnapshotPrepareSize:"
+ "setPluginPurgeableFactor:"
+ "setPreferFullReplacement:"
+ "setReserveSpacePaused:"
+ "setReserveSpaceSizeOverride:"
+ "setSafariUpdateContentBundleURL:"
+ "setSuAssetDownloadOptions:"
+ "setSystemGrowthMarginOverride:"
+ "setTaskDescription:"
+ "setUnentitledReserveAmount:"
+ "setUseReserveSpace:"
+ "setValue:forKey:"
+ "snapshotPreparationSize"
+ "suAssetDownloadOptions"
+ "systemGrowthMarginOverride"
+ "totalRequiredFreeSpaceHelper:"
+ "totalSnapshotRequiredFreeSpace"
+ "unable to stat volume: %s : %s"
+ "unentitledReserveAmount"
+ "useReserveSpace"
+ "v32@0:8Q16@24"
+ "|allowSameVersionUpdates=%@|preferFullReplacement=%@"
- "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n     securityAdvisoryNotificationTitle: %@\n      securityAdvisoryNotificationBody: %@\n  deviceCompatibilityNotificationTitle: %@\n   deviceCompatibilityNotificationBody: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n<<<]"
- "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n    securityAdvisoryNotificationTitleString: %@\n     securityAdvisoryNotificationBodyString: %@\n deviceCompatibilityNotificationTitleString: %@\n  deviceCompatibilityNotificationBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n                    encodedUIBundleFileName: %@\n<<<]"
- "\n[>>>\n    SubPolicies(specifiedUsedPolicies:0x%llX)\n%@    AssetTypes(softwareUpdateAssetType:%@|documentationAssetType:%@)\n    Versions(prerequisiteBuildVersion:%@|prerequisiteProductVersion:%@|prerequisiteRestoreVersion:%@|targetRestoreVersion:%@|installedSFRVersion:%@)\n    Device(deviceClass:%@|hwModelStr:%@|productType:%@|releaseType:%@|isInternal:%@)\n    Config(restrictToFull:%@|allowSameVersion:%@|background:%@|allowsCellular:%@|checkAvailableSpace:%@|cacheDeleteUrgency:%@|userAgentString:%@|userInitiated:%@|skipVolumeSealing:%@|qualityOfService:%@)\n    Target(targetVolumeUUID:%@|updateVolumePath:%@)\n    Preflight(performPreflightEncryptedCheck:%@|performPreflightSnapshotCheck:%@|updateBrainLocationOverride:%@)\n    Personalization(SSOToken:%@|personalizedManifestRootsPath:%@|personalizationServerURL:%@|proxyHostName:%@|proxyPortNumber:%@)\n    Authentication(localAuthenticationContext:%@|downloadAuthorizationHeader:%@|localAuthenticationUserID:%@|mdmBootstrapToken:%@)\n    BridgeOS(bridgeOSIgnoreMinimumVersionCheck:%@|bridgeOSDownloadDirectory:%@|enableEmbeddedOSInstall:%@|enableBridgeOSInstall:%@|enableOSPersonalization:%@)\n    Metrics(updateMetricEventFields:%@|updateMetricContext:%@\n    Defaults(defaultDescriptorValues:%@|assetAudienceUUID:%@|alternateAssetAudienceUUID:%@|disableAlternateUpdate:%@|disableSplombo:%@|mobileAssetPurposeOverride:%@)\n    PSUS(enable:%@|enableForOptionalAssets:%@)\n    Extensions(%@)\n<<<]"
- "%@(minCompatibility:%@|maxCompatibility:%@)"
- "%{public}@ assetCompatibilityVersion=%lu, compatible=%{public}@"
- "%{public}@ found %lu assets that meet the compatibility requirement of %lu:%lu"
- "%{public}@ starting compatibility version filtering, starting with %lu assets"

```
