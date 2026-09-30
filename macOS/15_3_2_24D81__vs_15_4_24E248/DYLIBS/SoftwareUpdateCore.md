## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0xa8a34
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x6c7c
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x1393f
-  __TEXT.__oslogstring: 0xa95e
-  __TEXT.__gcc_except_tab: 0x6c8
-  __TEXT.__unwind_info: 0x15b8
-  __TEXT.__objc_classname: 0x6d3
-  __TEXT.__objc_methname: 0x137ed
-  __TEXT.__objc_methtype: 0xe92
-  __TEXT.__objc_stubs: 0xd4a0
+2171.101.1.0.0
+  __TEXT.__text: 0xaa8e8
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x7294
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x14222
+  __TEXT.__oslogstring: 0xac7f
+  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__unwind_info: 0x15d0
+  __TEXT.__objc_classname: 0x6d5
+  __TEXT.__objc_methname: 0x13fd7
+  __TEXT.__objc_methtype: 0xec2
+  __TEXT.__objc_stubs: 0xd780
   __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x1350
+  __DATA_CONST.__const: 0x13b0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3da0
+  __DATA_CONST.__objc_selrefs: 0x3f00
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x1190
-  __AUTH_CONST.__cfstring: 0x11b40
-  __AUTH_CONST.__objc_const: 0xa370
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x1220
+  __AUTH_CONST.__cfstring: 0x11e80
+  __AUTH_CONST.__objc_const: 0x9cb0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x8cc
+  __DATA.__objc_ivar: 0x8f4
   __DATA.__data: 0x360
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C16836E-B1F5-3693-A7A0-D34C5D884607
-  Functions: 2815
-  Symbols:   6609
-  CStrings:  8314
+  UUID: 4ECA6D26-AD23-34CB-8125-ED81861B5571
+  Functions: 2847
+  Symbols:   6701
+  CStrings:  8442
 
Symbols:
+ +[SUCoreConfigServer allowedServerKeys].cold.1
+ +[SUCoreConfigServer allowedServerProjects].cold.1
+ +[SUCoreConfigServer sharedServerSettings].cold.1
+ +[SUCoreDDMUtilities sharedLogger].cold.1
+ +[SUCoreMobileAsset mapMobileAssetErrorIndications].cold.1
+ +[SUCorePolicyDDMConfiguration sharedInstance].cold.1
+ +[SUCorePower sharedPowerManager].cold.1
+ +[SUCoreSpace _issuePurgeCompletion:withCompletionQueue:haveEnoughSpace:amountPurged:error:transaction:transactionName:]
+ +[SUCoreSpace _issuePurgeableCompletion:withCompletionQueue:haveEnoughSpace:amountPurgeable:error:transaction:transactionName:]
+ +[SUCoreSpace mobileAssetEstimateEvictable:completionQueue:completion:]
+ +[SUCoreSpace mobileAssetEstimateEvictable:completionQueue:completion:].cold.1
+ +[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]
+ +[SUCoreSpace mobileAssetSuspend:completionQueue:completion:]
+ +[SUCoreSpace sharedSpaceManager].cold.1
+ +[SUCoreXPCActivityManager sharedInstance].cold.1
+ -[SUCoreConfigServer scheduledActivityName].cold.1
+ -[SUCoreDescriptor alignediOSMajorVersion]
+ -[SUCoreDescriptor deviceCompatibilityNotificationBodyString]
+ -[SUCoreDescriptor deviceCompatibilityNotificationTitleString]
+ -[SUCoreDescriptor disableDeviceCompatibilityNotification]
+ -[SUCoreDescriptor disableMASuspension]
+ -[SUCoreDescriptor disableSecurityAdvisoryNotification]
+ -[SUCoreDescriptor securityAdvisoryNotificationBodyString]
+ -[SUCoreDescriptor securityAdvisoryNotificationTitleString]
+ -[SUCoreDescriptor setDisableMASuspension:]
+ -[SUCoreDevice(SUCoreDeviceExtended) rootVolumeUUID].cold.1
+ -[SUCoreDocumentation deviceCompatibilityNotificationBodyString]
+ -[SUCoreDocumentation deviceCompatibilityNotificationTitleString]
+ -[SUCoreDocumentation securityAdvisoryNotificationBodyString]
+ -[SUCoreDocumentation securityAdvisoryNotificationTitleString]
+ -[SUCoreDocumentation setDeviceCompatibilityNotificationBodyString:]
+ -[SUCoreDocumentation setDeviceCompatibilityNotificationTitleString:]
+ -[SUCoreDocumentation setSecurityAdvisoryNotificationBodyString:]
+ -[SUCoreDocumentation setSecurityAdvisoryNotificationTitleString:]
+ -[SUCoreMSU initWithDelegate:withCallbackQueue:].cold.1
+ -[SUCorePolicy isSupervisedAndRequestingInvalidOS:]
+ -[SUCorePolicySoftwareUpdateDownload maxPreSUStagingOptionalSize]
+ -[SUCorePolicySoftwareUpdateDownload setMaxPreSUStagingOptionalSize:]
+ -[SUCoreUpdateDownloader _prepareForDownloading]
+ -[SUCoreUpdateDownloader maxAllowedPreSUStagingOptionalSize]
+ -[SUCoreUpdateDownloader setMaxAllowedPreSUStagingOptionalSize:]
+ OBJC_IVAR_$_SUCoreDescriptor._alignediOSMajorVersion
+ OBJC_IVAR_$_SUCoreDescriptor._disableDeviceCompatibilityNotification
+ OBJC_IVAR_$_SUCoreDescriptor._disableMASuspension
+ OBJC_IVAR_$_SUCoreDescriptor._disableSecurityAdvisoryNotification
+ OBJC_IVAR_$_SUCoreDocumentation._deviceCompatibilityNotificationBodyString
+ OBJC_IVAR_$_SUCoreDocumentation._deviceCompatibilityNotificationTitleString
+ OBJC_IVAR_$_SUCoreDocumentation._securityAdvisoryNotificationBodyString
+ OBJC_IVAR_$_SUCoreDocumentation._securityAdvisoryNotificationTitleString
+ OBJC_IVAR_$_SUCorePolicySoftwareUpdateDownload._maxPreSUStagingOptionalSize
+ OBJC_IVAR_$_SUCoreUpdateDownloader._maxAllowedPreSUStagingOptionalSize
+ __129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.356
+ __39-[SUCoreMobileAsset _reportDownloaded:]_block_invoke.1184
+ __51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.516
+ __51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.517
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1061
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1065
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1072
+ __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1122
+ __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1123
+ __57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.443
+ __63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.482
+ __96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.375
+ ___120+[SUCoreSpace _issuePurgeCompletion:withCompletionQueue:haveEnoughSpace:amountPurged:error:transaction:transactionName:]_block_invoke
+ ___127+[SUCoreSpace _issuePurgeableCompletion:withCompletionQueue:haveEnoughSpace:amountPurgeable:error:transaction:transactionName:]_block_invoke
+ ___61+[SUCoreSpace mobileAssetSuspend:completionQueue:completion:]_block_invoke
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke
+ ___71+[SUCoreSpace mobileAssetEstimateEvictable:completionQueue:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0l
+ _kSUAssetAlignediOSMajorVersionKey
+ _kSUAssetDeviceCompatibilityNotificationBodyKey
+ _kSUAssetDeviceCompatibilityNotificationTitleKey
+ _kSUAssetDisableDeviceCompatibilityNotificationKey
+ _kSUAssetDisableSecurityAdvisoryNotificationKey
+ _kSUAssetSUDisableMASuspensionKey
+ _kSUAssetSecurityAdvisoryNotificationBodyKey
+ _kSUAssetSecurityAdvisoryNotificationTitleKey
+ _kSUCoreDDMSoftwareUpdateStatusDidChangeNotificationValueTargetLocalDateTime
+ _kSU_M_MobileAssetEstimateEvictable
+ _kSU_M_MobileAssetResume
+ _kSU_M_MobileAssetSuspend
+ _objc_msgSend$_issuePurgeCompletion:withCompletionQueue:haveEnoughSpace:amountPurged:error:transaction:transactionName:
+ _objc_msgSend$_issuePurgeableCompletion:withCompletionQueue:haveEnoughSpace:amountPurgeable:error:transaction:transactionName:
+ _objc_msgSend$_prepareForDownloading
+ _objc_msgSend$alignediOSMajorVersion
+ _objc_msgSend$deviceCompatibilityNotificationBodyString
+ _objc_msgSend$deviceCompatibilityNotificationTitleString
+ _objc_msgSend$disableDeviceCompatibilityNotification
+ _objc_msgSend$disableMASuspension
+ _objc_msgSend$disableSecurityAdvisoryNotification
+ _objc_msgSend$estimateEvictableBytesForSoftwareUpdateWithCompletion:
+ _objc_msgSend$isSupervisedAndRequestingInvalidOS:
+ _objc_msgSend$maxAllowedPreSUStagingOptionalSize
+ _objc_msgSend$maxPreSUStagingOptionalSize
+ _objc_msgSend$resumeFromSoftwareUpdateWithCompletion:
+ _objc_msgSend$securityAdvisoryNotificationBodyString
+ _objc_msgSend$securityAdvisoryNotificationTitleString
+ _objc_msgSend$setDeviceCompatibilityNotificationBodyString:
+ _objc_msgSend$setDeviceCompatibilityNotificationTitleString:
+ _objc_msgSend$setMaxAllowedPreSUStagingOptionalSize:
+ _objc_msgSend$setMaxPreSUStagingOptionalSize:
+ _objc_msgSend$setSecurityAdvisoryNotificationBodyString:
+ _objc_msgSend$setSecurityAdvisoryNotificationTitleString:
+ _objc_msgSend$suspendForSoftwareUpdateWithNeededBytes:completion:
- _CacheDeleteCopyAvailableSpaceForVolume
- _OUTLINED_FUNCTION_6
- __103+[SUCoreSpace cacheDeletePurge:fromBasePath:cacheDeleteUrgency:timeout:withCompletionQueue:completion:]_block_invoke.135
- __129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.74
- __39-[SUCoreMobileAsset _reportDownloaded:]_block_invoke.1157
- __51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.509
- __51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.510
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1034
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1038
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1045
- __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1095
- __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1096
- __57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.444
- __96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.99
- ___135+[SUCoreSpace checkPurgeableSpaceCacheDelete:fromBasePath:cacheDeleteUrgency:timeout:additionalOptions:withCompletionQueue:completion:]_block_invoke
- ___block_descriptor_65_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
CStrings:
+ "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n     securityAdvisoryNotificationTitle: %@\n      securityAdvisoryNotificationBody: %@\n  deviceCompatibilityNotificationTitle: %@\n   deviceCompatibilityNotificationBody: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n<<<]"
+ "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n    securityAdvisoryNotificationTitleString: %@\n     securityAdvisoryNotificationBodyString: %@\n deviceCompatibilityNotificationTitleString: %@\n  deviceCompatibilityNotificationBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n<<<]"
+ "%{public}@ %s is called with policy:%{public}@"
+ "+[SUCoreSpace mobileAssetEstimateEvictable:completionQueue:completion:]"
+ "+[SUCoreSpace mobileAssetEstimateEvictable:completionQueue:completion:]_block_invoke"
+ "+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]"
+ "+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke"
+ "+[SUCoreSpace mobileAssetSuspend:completionQueue:completion:]"
+ "+[SUCoreSpace mobileAssetSuspend:completionQueue:completion:]_block_invoke"
+ "-[SUCoreScan alterCurrentPolicy:]"
+ "-[SUCoreScan checkForAvailableMajorMinorUpdatesWithPolicy:completion:]"
+ "-[SUCoreScan checkForAvailableSlowReleaseUpdatesWithPolicy:completion:]"
+ "-[SUCoreScan checkForAvailableUpdateWithPolicy:completion:]"
+ "-[SUCoreScan collectDocumentationMetadataWithPolicy:descriptor:downloadDocumentation:completion:]"
+ "-[SUCoreScan locateAvailableUpdateWithPolicy:completion:]"
+ "-[SUCoreScan verifyLatestAvailableWithPolicy:descriptor:completion:]"
+ "1.0.3"
+ "AlignediOSMajorVersion"
+ "DeviceCompatibilityNotificationBodyString"
+ "DeviceCompatibilityNotificationTitleString"
+ "DisableDeviceCompatibilityNotification"
+ "DisableMASuspension"
+ "DisableSecurityAdvisoryNotification"
+ "Failed to estimate evictable bytes"
+ "Invalid global settings declaration: attempt to set automatically install OS updates to 'Allowed' while automatically download is 'AlwaysOff'"
+ "Invalid global settings declaration: attempt to set automatically install OS updates to 'AlwaysOn' while automatically download is 'Allowed'"
+ "Invalid global settings declaration: attempt to set automatically install OS updates to 'AlwaysOn' while automatically download is 'AlwaysOff'"
+ "MaxPSUSOptionalSize"
+ "MobileAssetEstimateEvictable"
+ "MobileAssetResume"
+ "MobileAssetSuspend"
+ "OptionalAssetSizeAllowed"
+ "RealityDevice"
+ "SUCorePolicySoftwareUpdateDownload(specifiedFields:0x%llX|skipPhase:%@|allowsCellular:%@|discretionary:%@|disableUI:%@|requiresPowerPluggedIn:%@|downloadTimeoutSecs:%d|requiresInexpensiveAccess:%@|maxPreSUStagingOptionalSize:%lld|additionalOptions:%@)"
+ "SUDisableMASuspension"
+ "SecurityAdvisoryNotificationBodyString"
+ "SecurityAdvisoryNotificationTitleString"
+ "SimulatedDeviceCompatibilityNotificationBodyString"
+ "SimulatedDeviceCompatibilityNotificationTitleString"
+ "SimulatedSecurityAdvisoryNotificationBodyString"
+ "SimulatedSecurityAdvisoryNotificationTitleString"
+ "T@\"NSNumber\",R,&,N,V_alignediOSMajorVersion"
+ "T@\"NSString\",&,V_deviceCompatibilityNotificationBodyString"
+ "T@\"NSString\",&,V_deviceCompatibilityNotificationTitleString"
+ "T@\"NSString\",&,V_securityAdvisoryNotificationBodyString"
+ "T@\"NSString\",&,V_securityAdvisoryNotificationTitleString"
+ "TB,N,V_disableMASuspension"
+ "TB,R,N,V_disableDeviceCompatibilityNotification"
+ "TB,R,N,V_disableSecurityAdvisoryNotification"
+ "TQ,N,V_maxAllowedPreSUStagingOptionalSize"
+ "Tq,N,V_maxPreSUStagingOptionalSize"
+ "[DOCUMENTATION] Unable to load deviceCompatibilityNotificationBodyString: %{public}@"
+ "[DOCUMENTATION] Unable to load deviceCompatibilityNotificationTitleString: %{public}@"
+ "[DOCUMENTATION] Unable to load securityAdvisoryNotificationBodyString: %{public}@"
+ "[DOCUMENTATION] Unable to load securityAdvisoryNotificationTitleString: %{public}@"
+ "[PreSUStaging] staging assets with attributes: %@"
+ "[PreSUStaging] staging optional assets is disabled because no space is allowed"
+ "[PreSUStaging] using maxAllowedPreSUStagingOptionalSize = %llu"
+ "[SPACE] %s called with no completion"
+ "[SPACE] %s: MA estimated evictable bytes: success = %d, evictableBytes = %llu, error = %{public}@"
+ "[SPACE] %s: MA resumed: success = %d, error = %{public}@"
+ "[SPACE] %s: MA suspended: success = %d, error = %{public}@"
+ "[SPACE] %s: requesting MA to estimate evictable bytes: bytesNeeded = %llu"
+ "[SPACE] %s: requesting MA to resume"
+ "[SPACE] %s: requesting MA to suspend: bytesNeeded = %llu"
+ "_alignediOSMajorVersion"
+ "_deviceCompatibilityNotificationBodyString"
+ "_deviceCompatibilityNotificationTitleString"
+ "_disableDeviceCompatibilityNotification"
+ "_disableMASuspension"
+ "_disableSecurityAdvisoryNotification"
+ "_issuePurgeCompletion:withCompletionQueue:haveEnoughSpace:amountPurged:error:transaction:transactionName:"
+ "_issuePurgeableCompletion:withCompletionQueue:haveEnoughSpace:amountPurgeable:error:transaction:transactionName:"
+ "_maxAllowedPreSUStagingOptionalSize"
+ "_maxPreSUStagingOptionalSize"
+ "_prepareForDownloading"
+ "_securityAdvisoryNotificationBodyString"
+ "_securityAdvisoryNotificationTitleString"
+ "alignediOSMajorVersion"
+ "deviceCompatibilityNotificationBodyString"
+ "deviceCompatibilityNotificationTitleString"
+ "disableDeviceCompatibilityNotification"
+ "disableMASuspension"
+ "disableSecurityAdvisoryNotification"
+ "estimateEvictableBytesForSoftwareUpdateWithCompletion:"
+ "isSupervisedAndRequestingInvalidOS:"
+ "maxAllowedPreSUStagingOptionalSize"
+ "maxPreSUStagingOptionalSize"
+ "mobileAssetEstimateEvictable:completionQueue:completion:"
+ "mobileAssetResumeWithCompletionQueue:completion:"
+ "mobileAssetSuspend:completionQueue:completion:"
+ "neededBytes=%llu; evictableBytes=%llu"
+ "policy is valid by default"
+ "resumeFromSoftwareUpdateWithCompletion:"
+ "securityAdvisoryNotificationBodyString"
+ "securityAdvisoryNotificationTitleString"
+ "setDeviceCompatibilityNotificationBodyString:"
+ "setDeviceCompatibilityNotificationTitleString:"
+ "setDisableMASuspension:"
+ "setMaxAllowedPreSUStagingOptionalSize:"
+ "setMaxPreSUStagingOptionalSize:"
+ "setSecurityAdvisoryNotificationBodyString:"
+ "setSecurityAdvisoryNotificationTitleString:"
+ "space.MobileAssetEstimateEvictable"
+ "space.MobileAssetSuspend"
+ "suspendForSoftwareUpdateWithNeededBytes:completion:"
+ "target-local-date-time"
+ "v20@?0B8@\"NSError\"12"
+ "v40@0:8Q16@24@?32"
+ "v68@0:8@?16@24B32Q36@44@52@60"
+ "|maxPSUSOptSize=%lld"
- "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n              associatedSplatDescriptor: %@\n<<<]"
- "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n<<<]"
- "1.0.2"
- "Invalid global settings declaration: attempt to set automatically download OS updates to true while automatically check is false"
- "Invalid global settings declaration: attempt to set automatically install OS updates to true while automatically check is false"
- "Invalid global settings declaration: attempt to set automatically install OS updates to true while automatically download is false"
- "SUCorePolicySoftwareUpdateDownload(specifiedFields:0x%llX|skipPhase:%@|allowsCellular:%@|discretionary:%@|disableUI:%@|requiresPowerPluggedIn:%@|downloadTimeoutSecs:%d|requiresInexpensiveAccess:%@|additionalOptions:%@)"
- "check for available space failed (error reported by cache delete for basePath=%@)"
- "check for available space failed (unable to determine available space through cache delete for basePath=%@)"
- "check for available space failed (unable to determine volume name from basePath=%@)"

```
