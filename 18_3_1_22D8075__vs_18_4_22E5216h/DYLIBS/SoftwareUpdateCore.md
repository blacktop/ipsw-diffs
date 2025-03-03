## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x9d470
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x7054
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x13e9a
-  __TEXT.__oslogstring: 0xb35b
-  __TEXT.__gcc_except_tab: 0x6d4
+2171.100.132.0.0
+  __TEXT.__text: 0x9e174
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x75c4
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x145b7
+  __TEXT.__oslogstring: 0xb52c
+  __TEXT.__gcc_except_tab: 0x6e0
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x16b0
-  __TEXT.__objc_classname: 0x6fe
-  __TEXT.__objc_methname: 0x142d1
-  __TEXT.__objc_methtype: 0xf04
-  __TEXT.__objc_stubs: 0xe000
+  __TEXT.__objc_classname: 0x700
+  __TEXT.__objc_methname: 0x1470d
+  __TEXT.__objc_methtype: 0xf19
+  __TEXT.__objc_stubs: 0xe1a0
   __DATA_CONST.__got: 0x870
-  __DATA_CONST.__const: 0x2150
+  __DATA_CONST.__const: 0x21e0
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4068
+  __DATA_CONST.__objc_selrefs: 0x4178
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x11f20
-  __AUTH_CONST.__objc_const: 0xa7f0
+  __AUTH_CONST.__cfstring: 0x121c0
+  __AUTH_CONST.__objc_const: 0xa030
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x914
+  __DATA.__objc_ivar: 0x92c
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2891
-  Symbols:   3842
-  CStrings:  6253
+  Functions: 2907
+  Symbols:   3878
+  CStrings:  6327
 
Symbols:
+ _kSUAssetAlignediOSMajorVersionKey
+ _kSUAssetDisableDeviceCompatibilityNotificationKey
+ _kSUAssetDisableSecurityAdvisoryNotificationKey
+ _kSUAssetSUDisableMASuspensionKey
+ _kSUCoreDDMSoftwareUpdateStatusDidChangeNotificationValueTargetLocalDateTime
+ _kSU_M_MobileAssetEstimateEvictable
+ _kSU_M_MobileAssetResume
+ _kSU_M_MobileAssetSuspend
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n<<<]"
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
+ "RO\x05A\x87\x1f\b"
+ "RealityDevice"
+ "SUCorePolicySoftwareUpdateDownload(specifiedFields:0x%llX|skipPhase:%@|allowsCellular:%@|discretionary:%@|disableUI:%@|requiresPowerPluggedIn:%@|downloadTimeoutSecs:%d|requiresInexpensiveAccess:%@|maxPreSUStagingOptionalSize:%lld|additionalOptions:%@)"
+ "SUDisableMASuspension"
+ "T@\"NSNumber\",R,&,N,V_alignediOSMajorVersion"
+ "TB,N,V_disableMASuspension"
+ "TB,R,N,V_disableDeviceCompatibilityNotification"
+ "TB,R,N,V_disableSecurityAdvisoryNotification"
+ "TQ,N,V_maxAllowedPreSUStagingOptionalSize"
+ "Tq,N,V_maxPreSUStagingOptionalSize"
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
+ "_disableDeviceCompatibilityNotification"
+ "_disableMASuspension"
+ "_disableSecurityAdvisoryNotification"
+ "_issuePurgeCompletion:withCompletionQueue:haveEnoughSpace:amountPurged:error:transaction:transactionName:"
+ "_issuePurgeableCompletion:withCompletionQueue:haveEnoughSpace:amountPurgeable:error:transaction:transactionName:"
+ "_maxAllowedPreSUStagingOptionalSize"
+ "_maxPreSUStagingOptionalSize"
+ "_prepareForDownloading"
+ "alignediOSMajorVersion"
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
+ "setDisableMASuspension:"
+ "setMaxAllowedPreSUStagingOptionalSize:"
+ "setMaxPreSUStagingOptionalSize:"
+ "space.MobileAssetEstimateEvictable"
+ "space.MobileAssetSuspend"
+ "suspendForSoftwareUpdateWithNeededBytes:completion:"
+ "target-local-date-time"
+ "v20@?0B8@\"NSError\"12"
+ "v40@0:8Q16@24@?32"
+ "v68@0:8@?16@24B32Q36@44@52@60"
+ "|maxPSUSOptSize=%lld"
- "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n              associatedSplatDescriptor: %@\n<<<]"
- "1.0.2"
- "Invalid global settings declaration: attempt to set automatically download OS updates to true while automatically check is false"
- "Invalid global settings declaration: attempt to set automatically install OS updates to true while automatically check is false"
- "Invalid global settings declaration: attempt to set automatically install OS updates to true while automatically download is false"
- "RO\x05A\x87\x1f\a"
- "SUCorePolicySoftwareUpdateDownload(specifiedFields:0x%llX|skipPhase:%@|allowsCellular:%@|discretionary:%@|disableUI:%@|requiresPowerPluggedIn:%@|downloadTimeoutSecs:%d|requiresInexpensiveAccess:%@|additionalOptions:%@)"
- "_issueAppOffloadPurgeCompetion:withCompletionQueue:result:spacePurged:error:releasingTransaction:"
- "_issueSpacePurgeableCompetion:withCompletionQueue:result:spacePurgeable:error:releasingTransaction:"
- "v60@0:8@?16@24B32q36@44@52"

```
