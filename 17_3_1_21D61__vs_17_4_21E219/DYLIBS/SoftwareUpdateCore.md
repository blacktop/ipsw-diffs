## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-1856.80.3.0.1
-  __TEXT.__text: 0xf54a0
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x6660
-  __TEXT.__cstring: 0x115b5
-  __TEXT.__oslogstring: 0xa819
-  __TEXT.__gcc_except_tab: 0x68c
+1856.100.79.0.3
+  __TEXT.__text: 0xf7574
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x6710
+  __TEXT.__cstring: 0x11c06
+  __TEXT.__oslogstring: 0xabb7
+  __TEXT.__gcc_except_tab: 0x698
   __TEXT.__const: 0x48
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x18f0
-  __TEXT.__objc_classname: 0x657
-  __TEXT.__objc_methname: 0x11ec8
-  __TEXT.__objc_methtype: 0xd9b
-  __TEXT.__objc_stubs: 0xcb60
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x1c00
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__unwind_info: 0x1948
+  __TEXT.__objc_classname: 0x66a
+  __TEXT.__objc_methname: 0x122a4
+  __TEXT.__objc_methtype: 0xdd5
+  __TEXT.__objc_stubs: 0xcd40
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x1c28
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7b18
-  __DATA_CONST.__objc_selrefs: 0x39f8
+  __DATA_CONST.__objc_const: 0x7c20
+  __DATA_CONST.__objc_selrefs: 0x3aa8
+  __DATA_CONST.__objc_classrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__cfstring: 0x10160
-  __AUTH_CONST.__objc_const: 0x1df8
-  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x10340
+  __AUTH_CONST.__objc_const: 0x1e40
+  __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x348
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_classrefs: 0x390
-  __DATA.__objc_superrefs: 0x1a8
-  __DATA.__objc_ivar: 0x830
+  __AUTH_CONST.__auth_got: 0x358
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x840
   __DATA.__data: 0x300
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA087088-C90E-3BFB-B314-AD4606A1F567
-  Functions: 2554
-  Symbols:   8672
-  CStrings:  7670
+  UUID: DD9DFA0D-CB8B-30E4-A49A-5400D5D9B612
+  Functions: 2577
+  Symbols:   8749
+  CStrings:  7761
 
Symbols:
+ +[SUCoreDDMUtilities _forceSupervision]
+ +[SUCoreDDMUtilities postNotificationOfType:]
+ +[SUCoreDDMUtilities postNotificationOfType:description:]
+ +[SUCoreDDMUtilities sharedLogger]
+ +[SUCoreSpace _checkMinimumRequiredSpace:purgingFromBase:userInitiated:totalRequiredFreeSpace:freeSpaceAvailable:checkAvailableSpaceTransaction:withCompletionQueue:completion:]
+ -[SUCoreDescriptor allowAutoDownloadOnBattery]
+ -[SUCoreDescriptor autoDownloadOnBatteryDelay]
+ -[SUCoreDescriptor autoDownloadOnBatteryMinBattery]
+ -[SUCoreDescriptor granularlyRamped]
+ -[SUCoreDescriptor installAlertInterval]
+ -[SUCoreDescriptor setAllowAutoDownloadOnBattery:]
+ -[SUCoreDescriptor setAutoDownloadOnBatteryDelay:]
+ -[SUCoreDescriptor setAutoDownloadOnBatteryMinBattery:]
+ -[SUCoreDescriptor setGranularlyRamped:]
+ -[SUCoreDescriptor setInstallAlertInterval:]
+ -[SUCorePolicyDDMConfiguration removeAllInvalidDeclarationsReturningInvalid]
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table18
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_SUCoreDDMUtilities
+ _OBJC_IVAR_$_SUCoreDescriptor._allowAutoDownloadOnBattery
+ _OBJC_IVAR_$_SUCoreDescriptor._autoDownloadOnBatteryDelay
+ _OBJC_IVAR_$_SUCoreDescriptor._autoDownloadOnBatteryMinBattery
+ _OBJC_IVAR_$_SUCoreDescriptor._granularlyRamped
+ _OBJC_IVAR_$_SUCoreDescriptor._installAlertInterval
+ _OBJC_METACLASS_$_SUCoreDDMUtilities
+ _SUCoreStringForDDMStatusNotificationType
+ __OBJC_$_CLASS_METHODS_SUCoreDDMUtilities
+ __OBJC_CLASS_RO_$_SUCoreDDMUtilities
+ __OBJC_METACLASS_RO_$_SUCoreDDMUtilities
+ ___103+[SUCoreSpace cacheDeletePurge:fromBasePath:cacheDeleteUrgency:timeout:withCompletionQueue:completion:]_block_invoke.136
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.579
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.582
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.583
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.586
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.77
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.329
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.340
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.342
+ ___176+[SUCoreSpace _checkMinimumRequiredSpace:purgingFromBase:userInitiated:totalRequiredFreeSpace:freeSpaceAvailable:checkAvailableSpaceTransaction:withCompletionQueue:completion:]_block_invoke
+ ___176+[SUCoreSpace _checkMinimumRequiredSpace:purgingFromBase:userInitiated:totalRequiredFreeSpace:freeSpaceAvailable:checkAvailableSpaceTransaction:withCompletionQueue:completion:]_block_invoke_2
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.930
+ ___34+[SUCoreDDMUtilities sharedLogger]_block_invoke
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1017
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1004
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1002
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1057
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1061
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1049
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1050
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1028
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1041
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1042
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.509
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.517
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.980
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.984
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.991
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1041
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1042
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.482
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.484
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.284
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.488
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.292
+ ___76-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarationsReturningInvalid]_block_invoke
+ ___76-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarationsReturningInvalid]_block_invoke_2
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.552
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.553
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.556
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.559
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.100
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.426
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.432
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.438
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.444
+ ___block_descriptor_64_e8_32s40r48r56r_e39_v32?0"NSString"8"NSDictionary"16^B24lr40l8s32l8r48l8r56l8
+ ___block_literal_global.265
+ ___block_literal_global.267
+ ___block_literal_global.341
+ ___block_literal_global.350
+ ___block_literal_global.353
+ ___block_literal_global.428
+ ___block_literal_global.434
+ ___block_literal_global.440
+ ___block_literal_global.446
+ ___block_literal_global.481
+ ___block_literal_global.491
+ ___block_literal_global.512
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.558
+ ___block_literal_global.581
+ ___block_literal_global.585
+ ___os_log_helper_16_0_3_8_0_8_0_8_0
+ ___os_log_helper_16_2_2_8_32_4_0
+ ___os_log_helper_16_2_2_8_32_8_64
+ ___os_log_helper_16_2_3_8_32_8_64_8_64
+ ___os_log_helper_16_2_4_8_64_8_64_4_0_8_0
+ __unnamed_array_storage.715
+ __unnamed_array_storage.727
+ __unnamed_array_storage.748
+ _kSUAssetAllowAutoDownloadOnBatteryKey
+ _kSUAssetAutoDownloadOnBatteryDelayKey
+ _kSUAssetAutoDownloadOnBatteryMinBatteryKey
+ _kSUAssetGranularlyRampedKey
+ _kSUAssetInstallAlertIntervalKey
+ _kSUCoreControllerMandatoryUpdateEligibleKey
+ _kSUCoreControllerMandatoryUpdateOptionalKey
+ _notify_post
+ _objc_msgSend$_checkMinimumRequiredSpace:purgingFromBase:userInitiated:totalRequiredFreeSpace:freeSpaceAvailable:checkAvailableSpaceTransaction:withCompletionQueue:completion:
+ _objc_msgSend$allowAutoDownloadOnBattery
+ _objc_msgSend$autoDownloadOnBatteryDelay
+ _objc_msgSend$autoDownloadOnBatteryMinBattery
+ _objc_msgSend$bundleID
+ _objc_msgSend$granularlyRamped
+ _objc_msgSend$installAlertInterval
+ _objc_msgSend$postNotificationOfType:description:
+ _objc_msgSend$purgeableReason
+ _objc_msgSend$purgeableType
+ _objc_msgSend$purgedApps
+ _objc_msgSend$removeAllInvalidDeclarationsReturningInvalid
+ _objc_msgSend$staticDiskUsage
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _sharedLogger.logger
+ _sharedLogger.loggerOnce
- -[SUCoreDDMDeclaration logger]
- -[SUCoreDDMDeclaration setLogger:]
- GCC_except_table16
- GCC_except_table19
- GCC_except_table21
- _OBJC_IVAR_$_SUCoreDDMDeclaration._logger
- ___103+[SUCoreSpace cacheDeletePurge:fromBasePath:cacheDeleteUrgency:timeout:withCompletionQueue:completion:]_block_invoke.141
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.555
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.558
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.559
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.562
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.74
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.75
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke_2.76
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.305
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.316
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.318
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.906
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.993
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.980
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.978
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1033
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1037
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1025
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1026
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1004
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1017
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1018
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.485
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.493
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.941
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.945
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.952
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1002
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1003
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.458
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.460
- ___60-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarations]_block_invoke
- ___60-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarations]_block_invoke_2
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.260
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.464
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.268
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.528
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.529
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.532
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.535
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.105
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.390
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.396
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.402
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.408
- ___block_descriptor_72_e8_32s40s48s56r64r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.317
- ___block_literal_global.326
- ___block_literal_global.329
- ___block_literal_global.386
- ___block_literal_global.392
- ___block_literal_global.398
- ___block_literal_global.404
- ___block_literal_global.457
- ___block_literal_global.467
- ___block_literal_global.488
- ___block_literal_global.496
- ___block_literal_global.499
- ___block_literal_global.534
- ___block_literal_global.557
- ___block_literal_global.561
- __unnamed_array_storage.676
- __unnamed_array_storage.688
- __unnamed_array_storage.709
CStrings:
+ "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n<<<]"
+ "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n           granularlyRamped: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n       installAlertInterval: %llu\n allowAutoDownloadOnBattery: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n<<<]"
+ "\x18"
+ "%s: %@"
+ "%s: %@ is (likely) good to go!"
+ "%s: %@ is a duplicate of %@, don't add it"
+ "%s: %@ is no longer valid, removing"
+ "%s: %@ is no longer valid; removing it..."
+ "%s: Adding %@"
+ "%s: Failed to create persisted path; fall back to '%@'"
+ "%s: Failed to load persisted state"
+ "%s: Loaded persisted state"
+ "%s: Past-due declaration: enforced install date is in the past (%@)"
+ "%s: Posting %{public}@ for %{public}@"
+ "%s: Removed %d invalid declarations"
+ "%s: Sorted DDM declarations: %@"
+ "%s: Unable to read corrupted software update state file.  Exception: %@"
+ "%s: forceSupervision is set"
+ "+[SUCoreDDMUtilities _forceSupervision]"
+ "+[SUCoreDDMUtilities postNotificationOfType:description:]"
+ "+[SUCorePolicyDDMConfiguration declarationFromAllDeclarations:]"
+ "-[SUCoreDDMDeclaration isValidDeclarationWithReason:]"
+ "-[SUCorePolicyDDMConfiguration addDeclaration:withKey:returningError:]_block_invoke"
+ "-[SUCorePolicyDDMConfiguration addDeclaration:withKey:returningError:]_block_invoke_2"
+ "-[SUCorePolicyDDMConfiguration allDeclarations]_block_invoke"
+ "-[SUCorePolicyDDMConfiguration initWithStatePersistencePath:]"
+ "-[SUCorePolicyDDMConfiguration initWithStatePersistencePath:]_block_invoke"
+ "-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarationsReturningInvalid]_block_invoke"
+ "-[SUCorePolicyDDMConfiguration removeAllInvalidDeclarationsReturningInvalid]_block_invoke_2"
+ "<?xml version=\"1.0\" encoding=\"UTF-8\"?>     <!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">     <plist version=\"1.0\">     <dict>         <key>MobileAssetNewPath</key>         <string></string>     </dict>     </plist>"
+ "AllowAutoDownloadOnBattery"
+ "AllowAutoDownloadOnBatteryDelay"
+ "AutoDownloadOnBatteryDelay"
+ "AutoDownloadOnBatteryMinBattery"
+ "BO\x04QV\x1f\x06"
+ "Failure"
+ "ForceSupervision"
+ "GranularlyRamped"
+ "InstallAlertInterval"
+ "InstallReason"
+ "InstallState"
+ "MobileAssetNewPath"
+ "NIL"
+ "Pending"
+ "SUCoreDDMUtilities"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_allowAutoDownloadOnBattery"
+ "TB,N,V_granularlyRamped"
+ "TQ,N,V_autoDownloadOnBatteryDelay"
+ "TQ,N,V_autoDownloadOnBatteryMinBattery"
+ "TQ,N,V_installAlertInterval"
+ "[SPACE] After cache delete: need %llu total: had %llu free space, was able to free up %llu after cache delete (enough space to install update)"
+ "[SPACE] After cache delete: need %llu total: had %llu free space, was able to free up %llu after cache delete.  Not enough space to install update."
+ "[SPACE] App Offload callback: %@"
+ "[SPACE] App Offload callback: number of purgedApps: %d"
+ "[SPACE] App Offload callback: purged size %lld bytes"
+ "[SPACE] App Offload purged app bundleID: '%@'; reason: '%@'; purgeableType: '%d'; diskUsage: '%lld'"
+ "[SPACE] Checking available space from base path %@.  Required free space: %lld"
+ "[SU Documentation Preview] Error creating plist: %@"
+ "[SU Documentation Preview] Invalid Update path: %@"
+ "[SU Documentation Preview] New Local Bundle: %@"
+ "[SU Documentation Preview] Overriding documentation assets with custom path"
+ "[SU Documentation Preview] Plist not found... creating a default plist"
+ "[SU Documentation Preview] Unable to find alternate local bundle URL"
+ "_allowAutoDownloadOnBattery"
+ "_autoDownloadOnBatteryDelay"
+ "_autoDownloadOnBatteryMinBattery"
+ "_checkMinimumRequiredSpace:purgingFromBase:userInitiated:totalRequiredFreeSpace:freeSpaceAvailable:checkAvailableSpaceTransaction:withCompletionQueue:completion:"
+ "_forceSupervision"
+ "_granularlyRamped"
+ "_installAlertInterval"
+ "allowAutoDownloadOnBattery"
+ "autoDownloadOnBatteryDelay"
+ "autoDownloadOnBatteryMinBattery"
+ "bundleID"
+ "com.apple.sucore.ddm"
+ "granularlyRamped"
+ "installAlertInterval"
+ "postNotificationOfType:"
+ "postNotificationOfType:description:"
+ "purgeableReason"
+ "purgeableType"
+ "purgedApps"
+ "removeAllInvalidDeclarationsReturningInvalid"
+ "setAllowAutoDownloadOnBattery:"
+ "setAutoDownloadOnBatteryDelay:"
+ "setAutoDownloadOnBatteryMinBattery:"
+ "setGranularlyRamped:"
+ "setInstallAlertInterval:"
+ "staticDiskUsage"
+ "v20@0:8S16"
+ "v28@0:8S16@20"
+ "v76@0:8Q16@24B32Q36Q44@52@60@?68"
+ "valueForKey:"
+ "writeToFile:atomically:encoding:error:"
- "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n<<<]"
- "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n<<<]"
- "\x19"
- "%@ is (likely) good to go!"
- "%@ is a duplicate of %@, don't add it"
- "%@ is no longer valid, removing"
- "%@ is no longer valid; removing it..."
- "Adding %@"
- "BO\x04Q&\x1f\x06"
- "Failed to create persisted path; fall back to '%@'"
- "Failed to load persisted state"
- "Loaded persisted state"
- "Past-due declaration: enforced install date is in the past (%@)"
- "Removed %d invalid declarations"
- "Sorted DDM declarations: %@"
- "Unable to read corrupted software update state file.  Exception: %@"
- "[SPACE] App Offload purged %lld bytes"
- "[SPACE] total disk space available: need %llu total, was able to free up %llu [after cache delete] (enough space to install update)"

```
