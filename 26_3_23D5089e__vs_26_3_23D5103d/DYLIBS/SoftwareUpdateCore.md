## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.80.7.0.0
-  __TEXT.__text: 0xa5c40
+2422.80.7.0.1
+  __TEXT.__text: 0xa5f58
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x7a8c
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x15428
-  __TEXT.__oslogstring: 0xc64e
+  __TEXT.__objc_methlist: 0x7ab4
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x15484
+  __TEXT.__oslogstring: 0xc661
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x1780
+  __TEXT.__unwind_info: 0x1790
   __TEXT.__objc_classname: 0x73b
-  __TEXT.__objc_methname: 0x15afa
+  __TEXT.__objc_methname: 0x15ba4
   __TEXT.__objc_methtype: 0xff8
-  __TEXT.__objc_stubs: 0xeae0
-  __DATA_CONST.__got: 0x940
-  __DATA_CONST.__const: 0x2318
+  __TEXT.__objc_stubs: 0xeb40
+  __DATA_CONST.__got: 0x968
+  __DATA_CONST.__const: 0x2320
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44a0
+  __DATA_CONST.__objc_selrefs: 0x44c0
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12c60
-  __AUTH_CONST.__objc_const: 0xa8d8
+  __AUTH_CONST.__cfstring: 0x12ca0
+  __AUTH_CONST.__objc_const: 0xa908
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x9c0
+  __DATA.__objc_ivar: 0x9c4
   __DATA.__data: 0x360
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 624A062E-2B83-317C-B370-88AB8183D130
-  Functions: 3036
-  Symbols:   10297
-  CStrings:  9041
+  UUID: F3C4DB06-08AF-3CDB-8C5D-FD301D83DC41
+  Functions: 3039
+  Symbols:   10313
+  CStrings:  9051
 
Symbols:
+ +[SUCoreSpace getFreeSpace:]
+ -[SUCoreDescriptor preSUStagingCacheDeleteLevel]
+ -[SUCoreDescriptor setPreSUStagingCacheDeleteLevel:]
+ _KSUAssetPreSUStagingCacheDeleteLevelKey
+ _OBJC_IVAR_$_SUCoreDescriptor._preSUStagingCacheDeleteLevel
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1097
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1101
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1108
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1158
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1159
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.571
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountPurgedKey
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountRequestedKey
+ _kSUCoreControllerPreSUStagingCacheDeleteLevelKey
+ _kSUCoreControllerPreSUStagingEffectiveCacheDeleteLevelKey
+ _kSUCoreControllerPreSUStagingMaxOptionalSizeKey
+ _objc_msgSend$getFreeSpace:
+ _objc_msgSend$preSUStagingCacheDeleteLevel
+ _objc_msgSend$safeIntForKey:defaultValue:
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1094
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1098
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1105
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1155
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1156
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.572
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
