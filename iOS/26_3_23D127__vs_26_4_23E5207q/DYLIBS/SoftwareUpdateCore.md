## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.80.9.0.2
-  __TEXT.__text: 0xaa7e8
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x7b84
-  __TEXT.__const: 0x192
-  __TEXT.__cstring: 0x154aa
-  __TEXT.__oslogstring: 0xc7a3
-  __TEXT.__gcc_except_tab: 0x758
+2422.100.179.0.3
+  __TEXT.__text: 0xb71e8
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x7bbc
+  __TEXT.__const: 0x1c2
+  __TEXT.__cstring: 0x1552d
+  __TEXT.__oslogstring: 0xc7b3
+  __TEXT.__gcc_except_tab: 0x754
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x43
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x17f8
-  __TEXT.__objc_classname: 0x778
-  __TEXT.__objc_methname: 0x15c85
+  __TEXT.__unwind_info: 0x2038
+  __TEXT.__objc_classname: 0x7da
+  __TEXT.__objc_methname: 0x15d63
   __TEXT.__objc_methtype: 0xff8
-  __TEXT.__objc_stubs: 0xec20
+  __TEXT.__objc_stubs: 0xece0
   __DATA_CONST.__got: 0xa80
   __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4508
+  __DATA_CONST.__objc_selrefs: 0x4530
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x12c60
-  __AUTH_CONST.__objc_const: 0xaba0
+  __AUTH_CONST.__cfstring: 0x12d00
+  __AUTH_CONST.__objc_const: 0xac10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x750
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x9d0
+  __DATA.__objc_ivar: 0x9d8
   __DATA.__data: 0x398
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 057D9CA4-11EE-371C-B934-8787DA6B3963
-  Functions: 3084
-  Symbols:   10604
-  CStrings:  9078
+  UUID: 77A1B021-120B-3296-82A0-D584059902F6
+  Functions: 3101
+  Symbols:   10656
+  CStrings:  9095
 
Symbols:
+ -[SUCoreDescriptor humanReadableUpdateLabel]
+ -[SUCoreDescriptor rosettaDeprecated]
+ -[SUCoreDocumentationDataManager setSupportCanarySplat:]
+ -[SUCoreDocumentationDataManager stashVersionForSplatBuild:productVersionExtra:]
+ -[SUCoreDocumentationDataManager supportCanarySplat]
+ GCC_except_table15
+ GCC_except_table7
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC15_createReporter26AppleIntelligenceReporting05EventK0CSgyFZTf4d_n
+ _OBJC_IVAR_$_SUCoreDescriptor._rosettaDeprecated
+ _OBJC_IVAR_$_SUCoreDocumentationDataManager._supportCanarySplat
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.690
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.693
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.694
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.697
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.413
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.428
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.439
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.441
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.1029
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1116
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1103
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1101
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1156
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1160
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1160.cold.1
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1148
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1149
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1149.cold.1
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1127
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1140
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1141
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1141.cold.1
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.618
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.619
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.608
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.616
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1148
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1152
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1159
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1209
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1210
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.581
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.581.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.583
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.583.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.528
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.581
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.619
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.383
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.587
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.390
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.393
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.395
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.377
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.382
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.383
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.392
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.663
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.664
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.667
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.670
+ ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.382
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.430
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.513
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.519
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.525
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.531
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.537
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.543
+ ___block_literal_global.379
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.391
+ ___block_literal_global.440
+ ___block_literal_global.449
+ ___block_literal_global.452
+ ___block_literal_global.509
+ ___block_literal_global.515
+ ___block_literal_global.521
+ ___block_literal_global.527
+ ___block_literal_global.533
+ ___block_literal_global.539
+ ___block_literal_global.545
+ ___block_literal_global.590
+ ___block_literal_global.611
+ ___block_literal_global.619
+ ___block_literal_global.622
+ ___block_literal_global.669
+ ___block_literal_global.692
+ ___block_literal_global.696
+ _kSUAssetRosettaDeprecatedKey
+ _objc_msgSend$errors
+ _objc_msgSend$humanReadableUpdateLabel
+ _objc_msgSend$psusOpType
+ _objc_msgSend$rosettaDeprecated
+ _objc_msgSend$stashVersionForSplatBuild:productVersionExtra:
+ _objc_msgSend$supportCanarySplat
+ _objc_release_x2
- GCC_except_table12
- GCC_except_table14
- GCC_except_table6
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.651
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.654
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.655
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.658
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.374
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.389
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.400
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.402
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.990
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1077
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1064
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1062
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1117
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121.cold.1
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1109
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110.cold.1
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1088
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1101
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102.cold.1
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.579
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.580
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.569
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.577
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1106
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1110
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1117
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1167
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1168
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.489
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.542
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.580
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.344
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.548
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.351
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.354
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.356
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.338
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.343
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.344
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.353
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.624
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.625
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.628
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.631
- ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.343
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.391
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.474
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.480
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.486
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.492
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.498
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.504
- ___block_literal_global.340
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.352
- ___block_literal_global.401
- ___block_literal_global.410
- ___block_literal_global.413
- ___block_literal_global.470
- ___block_literal_global.476
- ___block_literal_global.482
- ___block_literal_global.488
- ___block_literal_global.494
- ___block_literal_global.500
- ___block_literal_global.506
- ___block_literal_global.541
- ___block_literal_global.551
- ___block_literal_global.572
- ___block_literal_global.583
- ___block_literal_global.630
- ___block_literal_global.653
- ___block_literal_global.657
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_SoftwareUpdateCore
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "\n [>>>\n                         descriptorType: %@\n                 descriptorAudienceType: %@\n                    preferredUpdateType: %@\n                humanReadableUpdateName: %@\n               humanReadableUpdateLabel: %@\n               humanReadableUpdateTitle: %@\n             humanReadableUpdateVersion: %@\n              humanReadableMoreInfoLink: %@\n                    notificationEnabled: %@\n                notificationTitleString: %@\n                 notificationBodyString: %@\n               recommendedUpdateEnabled: %@\n            recommendedUpdateApplicable: %@\n        updateNotificationFrequencyDays: %@\n          recommendedUpdateMinOSVersion: %@\n          recommendedUpdateMaxOSVersion: %@\n           recommendedUpdateTitleString: %@\n       recommendedUpdateAlertBodyString: %@\n              mandatoryUpdateBodyString: %@\n      securityAdvisoryNotificationTitle: %@\n       securityAdvisoryNotificationBody: %@\n   deviceCompatibilityNotificationTitle: %@\n    deviceCompatibilityNotificationBody: %@\n           safariUpdateContentBundleURL: %@\n                             updateType: %@\n                                assetID: %@\n                softwareUpdateAssetType: %@\n                 documentationAssetType: %@\n          softwareUpdateAssetAbsoluteID: %@\n           documentationAssetAbsoluteID: %@\n             softwareUpdateAssetPurpose: %@\n              documentationAssetPurpose: %@\n"
+ "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateLabel: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n     psusRequiredAssetsSize: %llu\n     psusOptionalAssetsSize: %llu\n             suDownloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n           granularlyRamped: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n       installAlertInterval: %llu\n allowAutoDownloadOnBattery: %@\n             disableSplombo: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n  associatedSplatDescriptor: %@\n<<<]"
+ " "
+ "                         criticalUpdate: %@\n                            productType: %@\n                       autoInstallDelay: %llu\n                            notifyAfter: %@\n                   minimumBridgeVersion: %@\n                  disableRosettaUpdates: %@\n               disableRecoveryOSUpdates: %@\n                      rosettaDeprecated: %@\n          requireInstallAssistantUpdate: %@\n                              sepDigest: %@\n                          sepTBMDigests: %@\n                             rsepDigest: %@\n                         rsepTBMDigests: %@\n                        documentationID: %@\n                          documentation: %@\n                      softwareUpdateURL: %@\n                            measurement: %@\n                   measurementAlgorithm: %@\n                       bundleAttributes: %@\n                              splatOnly: %@\n                       semiSplatEnabled: %@\n                  semiSplatMustQuitApps: %@\n                                revoked: %@\n                    semiSplatRestartNow: %@\n              associatedSplatDescriptor: %@\n    disableSecurityAdvisoryNotification: %@\n disableDeviceCompatibilityNotification: %@\n                 alignediOSMajorVersion: %@\n"
+ "%@_%@"
+ "MobileAssetPurposeOverride"
+ "RosettaDeprecated"
+ "SUCoreDocumentationDataManager(%@|supportCanarySplat=%@)"
+ "TB,R,N,V_rosettaDeprecated"
+ "TB,V_supportCanarySplat"
+ "[SUCoreDocumentationDataManager] Documentation data already stashed for build version %{public}@"
+ "[SUCoreDocumentationDataManager] Failed to create evict stash directories: %{public}@"
+ "_rosettaDeprecated"
+ "_supportCanarySplat"
+ "humanReadableUpdateLabel"
+ "rosettaDeprecated"
+ "setSupportCanarySplat:"
+ "stashVersionForSplatBuild:productVersionExtra:"
+ "supportCanarySplat"
+ "|mobileAssetPurposeOverride=%@"
- "\n [>>>\n                         descriptorType: %@\n                 descriptorAudienceType: %@\n                    preferredUpdateType: %@\n                humanReadableUpdateName: %@\n               humanReadableUpdateTitle: %@\n             humanReadableUpdateVersion: %@\n              humanReadableMoreInfoLink: %@\n                    notificationEnabled: %@\n                notificationTitleString: %@\n                 notificationBodyString: %@\n               recommendedUpdateEnabled: %@\n            recommendedUpdateApplicable: %@\n        updateNotificationFrequencyDays: %@\n          recommendedUpdateMinOSVersion: %@\n          recommendedUpdateMaxOSVersion: %@\n           recommendedUpdateTitleString: %@\n       recommendedUpdateAlertBodyString: %@\n              mandatoryUpdateBodyString: %@\n      securityAdvisoryNotificationTitle: %@\n       securityAdvisoryNotificationBody: %@\n   deviceCompatibilityNotificationTitle: %@\n    deviceCompatibilityNotificationBody: %@\n           safariUpdateContentBundleURL: %@\n                             updateType: %@\n                                assetID: %@\n                softwareUpdateAssetType: %@\n                 documentationAssetType: %@\n          softwareUpdateAssetAbsoluteID: %@\n           documentationAssetAbsoluteID: %@\n             softwareUpdateAssetPurpose: %@\n              documentationAssetPurpose: %@\n"
- "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n     psusRequiredAssetsSize: %llu\n     psusOptionalAssetsSize: %llu\n             suDownloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n           granularlyRamped: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n       installAlertInterval: %llu\n allowAutoDownloadOnBattery: %@\n             disableSplombo: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n  associatedSplatDescriptor: %@\n<<<]"
- "                         criticalUpdate: %@\n                            productType: %@\n                       autoInstallDelay: %llu\n                            notifyAfter: %@\n                   minimumBridgeVersion: %@\n                  disableRosettaUpdates: %@\n               disableRecoveryOSUpdates: %@\n          requireInstallAssistantUpdate: %@\n                              sepDigest: %@\n                          sepTBMDigests: %@\n                             rsepDigest: %@\n                         rsepTBMDigests: %@\n                        documentationID: %@\n                          documentation: %@\n                      softwareUpdateURL: %@\n                            measurement: %@\n                   measurementAlgorithm: %@\n                       bundleAttributes: %@\n                              splatOnly: %@\n                       semiSplatEnabled: %@\n                  semiSplatMustQuitApps: %@\n                                revoked: %@\n                    semiSplatRestartNow: %@\n              associatedSplatDescriptor: %@\n    disableSecurityAdvisoryNotification: %@\n disableDeviceCompatibilityNotification: %@\n                 alignediOSMajorVersion: %@\n"
- "SUCoreDocumentationDataManager(%@)"
- "[SUCoreDocumentationDataManager] Documentation data already stashed for build version %@"
- "[SUCoreDocumentationDataManager] Failed to create evict stash directories: %@"

```
