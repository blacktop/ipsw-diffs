## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2171.100.132.0.0
-  __TEXT.__text: 0x9e174
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x75c4
+2171.100.143.0.0
+  __TEXT.__text: 0x9e7a0
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x7654
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x145b7
-  __TEXT.__oslogstring: 0xb52c
+  __TEXT.__cstring: 0x1477d
+  __TEXT.__oslogstring: 0xb67c
   __TEXT.__gcc_except_tab: 0x6e0
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x16b0
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0x1470d
+  __TEXT.__objc_methname: 0x149f5
   __TEXT.__objc_methtype: 0xf19
-  __TEXT.__objc_stubs: 0xe1a0
+  __TEXT.__objc_stubs: 0xe2a0
   __DATA_CONST.__got: 0x870
-  __DATA_CONST.__const: 0x21e0
+  __DATA_CONST.__const: 0x2200
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4178
+  __DATA_CONST.__objc_selrefs: 0x41b8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x121c0
-  __AUTH_CONST.__objc_const: 0xa030
+  __AUTH_CONST.__cfstring: 0x12260
+  __AUTH_CONST.__objc_const: 0xa130
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x92c
+  __DATA.__objc_ivar: 0x93c
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2907
-  Symbols:   3878
-  CStrings:  6327
+  Functions: 2919
+  Symbols:   3893
+  CStrings:  6352
 
Symbols:
+ _kSUAssetDeviceCompatibilityNotificationBodyKey
+ _kSUAssetDeviceCompatibilityNotificationTitleKey
+ _kSUAssetSecurityAdvisoryNotificationBodyKey
+ _kSUAssetSecurityAdvisoryNotificationTitleKey
- _CacheDeleteCopyAvailableSpaceForVolume
CStrings:
+ "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n     securityAdvisoryNotificationTitle: %@\n      securityAdvisoryNotificationBody: %@\n  deviceCompatibilityNotificationTitle: %@\n   deviceCompatibilityNotificationBody: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n<<<]"
+ "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n    securityAdvisoryNotificationTitleString: %@\n     securityAdvisoryNotificationBodyString: %@\n deviceCompatibilityNotificationTitleString: %@\n  deviceCompatibilityNotificationBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n<<<]"
+ "\x1f\n\x15"
+ "DeviceCompatibilityNotificationBodyString"
+ "DeviceCompatibilityNotificationTitleString"
+ "SecurityAdvisoryNotificationBodyString"
+ "SecurityAdvisoryNotificationTitleString"
+ "SimulatedDeviceCompatibilityNotificationBodyString"
+ "SimulatedDeviceCompatibilityNotificationTitleString"
+ "SimulatedSecurityAdvisoryNotificationBodyString"
+ "SimulatedSecurityAdvisoryNotificationTitleString"
+ "T@\"NSString\",&,V_deviceCompatibilityNotificationBodyString"
+ "T@\"NSString\",&,V_deviceCompatibilityNotificationTitleString"
+ "T@\"NSString\",&,V_securityAdvisoryNotificationBodyString"
+ "T@\"NSString\",&,V_securityAdvisoryNotificationTitleString"
+ "[DOCUMENTATION] Unable to load deviceCompatibilityNotificationBodyString: %{public}@"
+ "[DOCUMENTATION] Unable to load deviceCompatibilityNotificationTitleString: %{public}@"
+ "[DOCUMENTATION] Unable to load securityAdvisoryNotificationBodyString: %{public}@"
+ "[DOCUMENTATION] Unable to load securityAdvisoryNotificationTitleString: %{public}@"
+ "_deviceCompatibilityNotificationBodyString"
+ "_deviceCompatibilityNotificationTitleString"
+ "_securityAdvisoryNotificationBodyString"
+ "_securityAdvisoryNotificationTitleString"
+ "deviceCompatibilityNotificationBodyString"
+ "deviceCompatibilityNotificationTitleString"
+ "securityAdvisoryNotificationBodyString"
+ "securityAdvisoryNotificationTitleString"
+ "setDeviceCompatibilityNotificationBodyString:"
+ "setDeviceCompatibilityNotificationTitleString:"
+ "setSecurityAdvisoryNotificationBodyString:"
+ "setSecurityAdvisoryNotificationTitleString:"
- "\n[>>>\n                        descriptorType: %@\n                descriptorAudienceType: %@\n                   preferredUpdateType: %@\n               humanReadableUpdateName: %@\n              humanReadableUpdateTitle: %@\n            humanReadableUpdateVersion: %@\n             humanReadableMoreInfoLink: %@\n                   notificationEnabled: %@\n               notificationTitleString: %@\n                notificationBodyString: %@\n              recommendedUpdateEnabled: %@\n           recommendedUpdateApplicable: %@\n       updateNotificationFrequencyDays: %@\n         recommendedUpdateMinOSVersion: %@\n         recommendedUpdateMaxOSVersion: %@\n          recommendedUpdateTitleString: %@\n      recommendedUpdateAlertBodyString: %@\n             mandatoryUpdateBodyString: %@\n                            updateType: %@\n                               assetID: %@\n               softwareUpdateAssetType: %@\n                documentationAssetType: %@\n         softwareUpdateAssetAbsoluteID: %@\n          documentationAssetAbsoluteID: %@\n            softwareUpdateAssetPurpose: %@\n             documentationAssetPurpose: %@\n                promoteAlternateUpdate: %@\n          enableAlternateAssetAudience: %@\n            alternateAssetAudienceUUID: %@\n                     assetAudienceUUID: %@\n                         uniqueBuildID: %@\n                             trainName: %@\n                        productVersion: %@\n                   productBuildVersion: %@\n                   productVersionExtra: %@\n                     productSystemName: %@\n                           releaseType: %@\n                             publisher: %@\n                        restoreVersion: %@\n             targetUpdateBridgeVersion: %@\n                targetUpdateSFRVersion: %@\n                           releaseDate: %@\n                     prerequisiteBuild: %@\n                 prerequisiteOSVersion: %@\n                      supportedDevices: %@\n                       fullReplacement: %@\n                          downloadSize: %llu\n                        unarchivedSize: %llu\n                        msuPrepareSize: %llu\n                       preparationSize: %llu\n                      installationSize: %llu\n            minimumSystemPartitionSize: %llu\n                totalRequiredFreeSpace: %llu\n                   streamingZipCapable: %@\n                systemPartitionPadding: %@\n                psusRequiredAssetsSize: %llu\n                psusOptionalAssetsSize: %llu\n                        suDownloadSize:%llu\n                            enablePSUS: %@\n           enablePSUSForOptionalAssets: %@\n     autoDownloadAllowableOverCellular: %@\n         downloadAllowableOverCellular: %@\n                          downloadable: %@\n              disableSiriVoiceDeletion: %@\n                       disableCDLevel4: %@\n                    disableAppDemotion: %@\n                   disableMASuspension: %@\n                 disableInstallTonight: %@\n                 forcePasscodeRequired: %@\n                           rampEnabled: %@\n                      granularlyRamped: %@\n                      mdmDelayInterval: %llu\n                     autoUpdateEnabled: %@\n                      hideInstallAlert: %@\n                    containsSFRContent: %@\n                  installAlertInterval: %llu\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %llu\n       autoDownloadOnBatteryMinBattery: %llu\n                        disableSplombo: %@\n                         setupCritical: %@\n              criticalCellularOverride: %@\n                  criticalOutOfBoxOnly: %@\n                    lastEmergencyBuild: %@\n                lastEmergencyOSVersion: %@\n               mandatoryUpdateEligible: %@\n             mandatoryUpdateVersionMin: %@\n             mandatoryUpdateVersionMax: %@\n               mandatoryUpdateOptional: %@\nmandatoryUpdateRestrictedToOutOfTheBox: %@\n                  oneShotBuddyDisabled: %@\n            oneShotBuddyDisabledBuilds: %@\n                        criticalUpdate: %@\n                           productType: %@\n                      autoInstallDelay: %llu\n                           notifyAfter: %@\n                  minimumBridgeVersion: %@\n                 disableRosettaUpdates: %@\n              disableRecoveryOSUpdates: %@\n         requireInstallAssistantUpdate: %@\n                             sepDigest: %@\n                         sepTBMDigests: %@\n                            rsepDigest: %@\n                        rsepTBMDigests: %@\n                       documentationID: %@\n                         documentation: %@\n                     softwareUpdateURL: %@\n                           measurement: %@\n                  measurementAlgorithm: %@\n                      bundleAttributes: %@\n                             splatOnly: %@\n                      semiSplatEnabled: %@\n                 semiSplatMustQuitApps: %@\n                               revoked: %@\n                   semiSplatRestartNow: %@\n             associatedSplatDescriptor: %@\n   disableSecurityAdvisoryNotification: %@\ndisableDeviceCompatibilityNotification: %@\n                alignediOSMajorVersion: %@\n<<<]"
- "\n[>>>\n                        releaseNotesSummary: %@\n                               releaseNotes: %@\n                           licenseAgreement: %@\n                    humanReadableUpdateName: %@\n                   humanReadableUpdateTitle: %@\n                 humanReadableUpdateVersion: %@\n                  humanReadableMoreInfoLink: %@\n                        notificationEnabled: %@\n                    notificationTitleString: %@\n                     notificationBodyString: %@\n                   recommendedUpdateEnabled: %@\n                recommendedUpdateApplicable: %@\n recommendedUpdateNotificationFrequencyDays: %@\n              recommendedUpdateMinOSVersion: %@\n              recommendedUpdateMaxOSVersion: %@\n               recommendedUpdateTitleString: %@\n           recommendedUpdateAlertBodyString: %@\n                  mandatoryUpdateBodyString: %@\n                             productVersion: %@\n                                 slaVersion: %@\n                             localBundleURL: %@\n                             serverAssetURL: %@\n                     serverAssetMeasurement: %@\n                       serverAssetAlgorithm: %@\n                                   language: %@\n                releaseNotesSummaryFileName: %@\n                       releaseNotesFileName: %@\n                   licenseAgreementFileName: %@\n                    preferencesIconFileName: %@\n<<<]"
- "\x1f\x06\x15"
- "check for available space failed (error reported by cache delete for basePath=%@)"
- "check for available space failed (unable to determine available space through cache delete for basePath=%@)"
- "check for available space failed (unable to determine volume name from basePath=%@)"

```
