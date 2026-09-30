## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore`

```diff

-2422.80.7.0.0
-  __TEXT.__text: 0xb0f4c
+2422.80.7.0.1
+  __TEXT.__text: 0xb1270
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x765c
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x14b38
-  __TEXT.__oslogstring: 0xb5a6
+  __TEXT.__objc_methlist: 0x767c
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x14b94
+  __TEXT.__oslogstring: 0xb5b9
   __TEXT.__gcc_except_tab: 0x744
-  __TEXT.__unwind_info: 0x1680
+  __TEXT.__unwind_info: 0x1688
   __TEXT.__objc_classname: 0x711
-  __TEXT.__objc_methname: 0x14e9f
+  __TEXT.__objc_methname: 0x14f49
   __TEXT.__objc_methtype: 0xf5e
-  __TEXT.__objc_stubs: 0xde40
-  __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0x1450
+  __TEXT.__objc_stubs: 0xdea0
+  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4190
+  __DATA_CONST.__objc_selrefs: 0x41b0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x12c0
-  __AUTH_CONST.__cfstring: 0x12660
-  __AUTH_CONST.__objc_const: 0xa458
+  __AUTH_CONST.__cfstring: 0x126a0
+  __AUTH_CONST.__objc_const: 0xa488
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x978
+  __DATA.__objc_ivar: 0x97c
   __DATA.__data: 0x360
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xd20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67EC3F91-4470-3037-ABF0-0A6B03671F99
-  Functions: 2952
-  Symbols:   6949
-  CStrings:  8759
+  UUID: E04004BB-2FC1-33E4-A961-1056F55B2523
+  Functions: 2955
+  Symbols:   6962
+  CStrings:  8769
 
Symbols:
+ +[SUCoreSpace getFreeSpace:]
+ -[SUCoreDescriptor preSUStagingCacheDeleteLevel]
+ -[SUCoreDescriptor setPreSUStagingCacheDeleteLevel:]
+ OBJC_IVAR_$_SUCoreDescriptor._preSUStagingCacheDeleteLevel
+ _KSUAssetPreSUStagingCacheDeleteLevelKey
+ __39-[SUCoreMobileAsset _reportDownloaded:]_block_invoke.1220
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1097
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1101
+ __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1108
+ __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1158
+ __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1159
+ __63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.495
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountPurgedKey
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountRequestedKey
+ _kSUCoreControllerPreSUStagingCacheDeleteLevelKey
+ _kSUCoreControllerPreSUStagingEffectiveCacheDeleteLevelKey
+ _kSUCoreControllerPreSUStagingMaxOptionalSizeKey
+ _objc_msgSend$getFreeSpace:
+ _objc_msgSend$preSUStagingCacheDeleteLevel
+ _objc_msgSend$safeIntForKey:defaultValue:
- __39-[SUCoreMobileAsset _reportDownloaded:]_block_invoke.1217
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1094
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1098
- __53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1105
- __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1155
- __54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1156
- __63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.496
CStrings:
+ "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n           preSUStagingCacheDeleteLevel: %d\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"
+ "PSUSCacheDeleteLevel"
+ "PreSUStageCacheDeleteLevel"
+ "Ti,N,V_preSUStagingCacheDeleteLevel"
+ "[SPACE] unable to stat volume for path: '%{public}@' (%{public}s)"
+ "_preSUStagingCacheDeleteLevel"
+ "getFreeSpace:"
+ "preSUStagingCacheDeleteLevel"
+ "safeIntForKey:defaultValue:"
+ "setPreSUStagingCacheDeleteLevel:"
- "                             enablePSUS: %@\n            enablePSUSForOptionalAssets: %@\n    minFreeSpacePostStageOptionalAssets: %llu\n      autoDownloadAllowableOverCellular: %@\n          downloadAllowableOverCellular: %@\n                           downloadable: %@\n               disableSiriVoiceDeletion: %@\n                        disableCDLevel4: %@\n                     disableAppDemotion: %@\n                    disableMASuspension: %@\n                  disableInstallTonight: %@\n                  forcePasscodeRequired: %@\n                            rampEnabled: %@\n                       granularlyRamped: %@\n                       mdmDelayInterval: %llu\n                      autoUpdateEnabled: %@\n                       hideInstallAlert: %@\n                     containsSFRContent: %@\n                   installAlertInterval: %llu\n             allowAutoDownloadOnBattery: %@\n             autoDownloadOnBatteryDelay: %llu\n        autoDownloadOnBatteryMinBattery: %llu\n                         disableSplombo: %@\n                          setupCritical: %@\n               criticalCellularOverride: %@\n                   criticalOutOfBoxOnly: %@\n                     lastEmergencyBuild: %@\n                 lastEmergencyOSVersion: %@\n                mandatoryUpdateEligible: %@\n              mandatoryUpdateVersionMin: %@\n              mandatoryUpdateVersionMax: %@\n                mandatoryUpdateOptional: %@\n mandatoryUpdateRestrictedToOutOfTheBox: %@\n                   oneShotBuddyDisabled: %@\n             oneShotBuddyDisabledBuilds: %@\n"
- "unable to stat volume: %{public}s : %{public}s"

```
