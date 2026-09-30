## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0xb7a28
+2422.160.4.0.0
+  __TEXT.__text: 0xb7ae0
   __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x7c34
-  __TEXT.__const: 0x1c2
-  __TEXT.__cstring: 0x1569d
+  __TEXT.__objc_methlist: 0x7c4c
+  __TEXT.__const: 0x1d2
+  __TEXT.__cstring: 0x156fd
   __TEXT.__oslogstring: 0xc843
   __TEXT.__gcc_except_tab: 0x754
   __TEXT.__dlopen_cstrs: 0x41

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x2038
   __TEXT.__objc_classname: 0x7da
-  __TEXT.__objc_methname: 0x15e99
+  __TEXT.__objc_methname: 0x15ee1
   __TEXT.__objc_methtype: 0xff8
-  __TEXT.__objc_stubs: 0xee20
+  __TEXT.__objc_stubs: 0xee40
   __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x23d8
+  __DATA_CONST.__const: 0x23e0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4580
+  __DATA_CONST.__objc_selrefs: 0x4590
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x12e20
-  __AUTH_CONST.__objc_const: 0xac80
+  __AUTH_CONST.__cfstring: 0x12e40
+  __AUTH_CONST.__objc_const: 0xacb0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x750
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x9e0
+  __DATA.__objc_ivar: 0x9e4
   __DATA.__data: 0x398
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FFE28579-A55A-30FA-8F96-B31B74C242D2
-  Functions: 3109
-  Symbols:   10690
-  CStrings:  9130
+  UUID: B5B7F90D-1982-32A0-9EFC-B84E6F0A79CB
+  Functions: 3111
+  Symbols:   10697
+  CStrings:  9136
 
Symbols:
+ -[SUCoreDescriptor badgingEnabled]
+ -[SUCoreDescriptor setBadgingEnabled:]
+ _OBJC_IVAR_$_SUCoreDescriptor._badgingEnabled
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1151
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1155
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1162
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1212
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1213
+ _kSUAssetBadgingEnabledKey
+ _objc_msgSend$badgingEnabled
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1148
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1152
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1159
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1209
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1210
Functions:
~ -[SUCoreDescriptor initWithSUAsset:releaseDate:prepareSize:snapshotPrepareSize:applySize:snapshotApplySize:defaultValues:] : 5808 -> 5856
~ -[SUCoreDescriptor initWithUpdateBrainPath:updateBundlePath:bundleAttributes:descriptorType:] : 1760 -> 1764
~ -[SUCoreDescriptor initSemiSplatDescriptor] : 1280 -> 1284
~ -[SUCoreDescriptor initWithCoder:] : 5088 -> 5108
~ -[SUCoreDescriptor encodeWithCoder:] : 4808 -> 4836
~ -[SUCoreDescriptor description] : 4560 -> 4588
~ -[SUCoreDescriptor overviewWithMaxValueLength:providingSubstitutionMap:] : 2856 -> 2892
- -[SUCoreDescriptor setSetupCritical:]
+ -[SUCoreDescriptor setSetupCritical:]
- -[SUCoreDescriptor setLastEmergencyBuild:]
+ -[SUCoreDescriptor lastEmergencyBuild]
+ -[SUCoreDescriptor setLastEmergencyOSVersion:]
+ -[SUCoreDescriptor mandatoryUpdateVersionMin]
CStrings:
+ "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateLabel: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n     psusRequiredAssetsSize: %llu\n     psusOptionalAssetsSize: %llu\n             suDownloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n             badgingEnabled: %@\n           granularlyRamped: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n       installAlertInterval: %llu\n allowAutoDownloadOnBattery: %@\n             disableSplombo: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n  associatedSplatDescriptor: %@\n<<<]"
+ "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n           preSUStagingCacheDeleteLevel: %d\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                         badgingEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"
+ "BadgingEnabled"
+ "TB,N,V_badgingEnabled"
+ "_badgingEnabled"
+ "badgingEnabled"
+ "setBadgingEnabled:"
- "\n[>>>\n             descriptorType: %@\n     descriptorAudienceType: %@\n        preferredUpdateType: %@\n    humanReadableUpdateName: %@\n   humanReadableUpdateLabel: %@\n   humanReadableUpdateTitle: %@\n humanReadableUpdateVersion: %@\n  humanReadableMoreInfoLink: %@\n                 updateType: %@\n             productVersion: %@\n        productBuildVersion: %@\n             restoreVersion: %@\n  targetUpdateBridgeVersion: %@\n     targetUpdateSFRVersion: %@\n                releaseType: %@\n                releaseDate: %@\n          prerequisiteBuild: %@\n      prerequisiteOSVersion: %@\n               downloadSize: %llu\n     psusRequiredAssetsSize: %llu\n     psusOptionalAssetsSize: %llu\n             suDownloadSize: %llu\n             unarchivedSize: %llu\n            preparationSize: %llu\n           installationSize: %llu\n     totalRequiredFreeSpace: %llu\n                rampEnabled: %@\n           granularlyRamped: %@\n           mdmDelayInterval: %llu\n          autoUpdateEnabled: %@\n           hideInstallAlert: %@\n         containsSFRContent: %@\n       installAlertInterval: %llu\n allowAutoDownloadOnBattery: %@\n             disableSplombo: %@\n              setupCritical: %@\n            documentationID: %@\n          softwareUpdateURL: %@\n                measurement: %@\n       measurementAlgorithm: %@\n                  splatOnly: %@\n           semiSplatEnabled: %@\n                    revoked: %@\n  associatedSplatDescriptor: %@\n<<<]"
- "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n           preSUStagingCacheDeleteLevel: %d\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"

```
