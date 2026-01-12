## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.80.3.0.0
-  __TEXT.__text: 0xb813c
+950.80.5.0.0
+  __TEXT.__text: 0xb8a28
   __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0xb28c
+  __TEXT.__objc_methlist: 0xb30c
   __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x23146
-  __TEXT.__gcc_except_tab: 0x13cc
+  __TEXT.__cstring: 0x23487
+  __TEXT.__gcc_except_tab: 0x13e0
   __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3380
+  __TEXT.__unwind_info: 0x3390
   __TEXT.__objc_classname: 0xf4b
-  __TEXT.__objc_methname: 0x19e6e
+  __TEXT.__objc_methname: 0x1a04a
   __TEXT.__objc_methtype: 0x34fb
-  __TEXT.__objc_stubs: 0x14ee0
-  __DATA_CONST.__got: 0xdc8
-  __DATA_CONST.__const: 0x2a08
+  __TEXT.__objc_stubs: 0x15000
+  __DATA_CONST.__got: 0xde0
+  __DATA_CONST.__const: 0x2a58
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5fe0
+  __DATA_CONST.__objc_selrefs: 0x6028
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x147c0
-  __AUTH_CONST.__objc_const: 0x16080
+  __AUTH_CONST.__cfstring: 0x14940
+  __AUTH_CONST.__objc_const: 0x16120
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1108
-  __DATA.__objc_ivar: 0x9c0
+  __DATA.__objc_ivar: 0x9cc
   __DATA.__data: 0xe98
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x1658

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F39229DF-7E30-3A2A-BA42-E56261E5CA12
-  Functions: 4626
-  Symbols:   15368
-  CStrings:  10733
+  UUID: 45871A40-A143-32EF-9517-20D620524E66
+  Functions: 4639
+  Symbols:   15411
+  CStrings:  10776
 
Symbols:
+ +[SUSpace _hasUnentitledSpaceSet]
+ +[SUSpace _performCacheDeleteForOptionalPSUS:downloadOptions:completion:]
+ +[SUSpace makeRoomForUpdate:downloadOptions:completion:]
+ -[SUDescriptor preSUStagingCacheDeleteLevel]
+ -[SUDescriptor setPreSUStagingCacheDeleteLevel:]
+ -[SUDownloadOptions additionalInfo]
+ -[SUDownloadOptions maxPreSUStagingOptionalSize]
+ -[SUDownloadOptions setAdditionalInfo:]
+ -[SUDownloadOptions setMaxPreSUStagingOptionalSize:]
+ -[SUPolicyDownload additionalOptions]
+ -[SUPreferences psusCacheDeleteLevel]
+ GCC_except_table58
+ _OBJC_IVAR_$_SUDescriptor._preSUStagingCacheDeleteLevel
+ _OBJC_IVAR_$_SUDownloadOptions._additionalInfo
+ _OBJC_IVAR_$_SUDownloadOptions._maxPreSUStagingOptionalSize
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_2
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_3
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_4
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_5
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_6
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_7
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_8
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_9
+ ___73+[SUSpace _performCacheDeleteForOptionalPSUS:downloadOptions:completion:]_block_invoke
+ ___73+[SUSpace _performCacheDeleteForOptionalPSUS:downloadOptions:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s_e8_Q16?0Q8ls32l8
+ ___block_descriptor_68_e8_32s40bs48bs_e23_v28?0B8Q12"NSError"20ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls32l8s40l8s48l8r56l8
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountPurgedKey
+ _kSUCoreControllerPreSUStagingCacheDeleteAmountRequestedKey
+ _kSUCoreControllerPreSUStagingEffectiveCacheDeleteLevelKey
+ _objc_msgSend$_hasUnentitledSpaceSet
+ _objc_msgSend$_performCacheDeleteForOptionalPSUS:downloadOptions:completion:
+ _objc_msgSend$additionalInfo
+ _objc_msgSend$additionalOptions
+ _objc_msgSend$cacheDeletePurge:fromBasePath:cacheDeleteUrgency:completion:
+ _objc_msgSend$getFreeSpace:
+ _objc_msgSend$makeRoomForUpdate:downloadOptions:completion:
+ _objc_msgSend$preSUStagingCacheDeleteLevel
+ _objc_msgSend$psusCacheDeleteLevel
+ _objc_msgSend$setAdditionalInfo:
+ _objc_msgSend$setPreSUStagingCacheDeleteLevel:
- +[SUSpace maxPreSUStagingOptionalSpaceForUpdate:]
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_2
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_3
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_4
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_5
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_6
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_7
- ___40+[SUSpace makeRoomForUpdate:completion:]_block_invoke_8
- ___block_descriptor_64_e8_32s40bs48r_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls32l8s40l8r48l8
- _objc_msgSend$maxPreSUStagingOptionalSpaceForUpdate:
- _objc_msgSend$spaceOverrideMaxPSUSOptionalSize
CStrings:
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            PreSUStagingCacheDeleteLevel: %d\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
+ "!#"
+ "%s: unable to get reserve space info, Error: [%ld] %@"
+ "+[SUSpace _hasUnentitledSpaceSet]"
+ "+[SUSpace _performCacheDeleteForOptionalPSUS:downloadOptions:completion:]"
+ "+[SUSpace _performCacheDeleteForOptionalPSUS:downloadOptions:completion:]_block_invoke_2"
+ "+[SUSpace makeRoomForUpdate:downloadOptions:completion:]"
+ "+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_3"
+ "+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_6"
+ "/private/var/"
+ "CACHE_DELETE_UNENTITLED_RESERVATION"
+ "Q16@?0Q8"
+ "SUPsusCacheDeleteLevel"
+ "T@\"NSMutableDictionary\",&,N,V_additionalInfo"
+ "Ti,N,V_preSUStagingCacheDeleteLevel"
+ "Tq,N,V_maxPreSUStagingOptionalSize"
+ "[PREFERENCES] using cache delete urgency override %d"
+ "_additionalInfo"
+ "_hasUnentitledSpaceSet"
+ "_maxPreSUStagingOptionalSize"
+ "_performCacheDeleteForOptionalPSUS:downloadOptions:completion:"
+ "_preSUStagingCacheDeleteLevel"
+ "additionalInfo"
+ "cacheDeletePurge:fromBasePath:cacheDeleteUrgency:completion:"
+ "free space after cleanup: %.2lf GB"
+ "freeSpace = %.2lf GB, totalNeededSpace = %.2lf GB (unavailable for psus = %.2lf GB)"
+ "getFreeSpace:"
+ "makeRoomForUpdate:downloadOptions:completion:"
+ "no need to perform cache-delete for psus or compute maxPreSUStagingOptionalSize"
+ "no psus optional assets - no need to make room"
+ "not performing cache delete for optional psus: already have enough free space"
+ "not performing cache delete for optional psus: urgency = %d"
+ "performed cache delete (%d), requesting: %.2lf GB, purged: %.2lf GB"
+ "performing cache delete (%d), requesting: %.2lf GB"
+ "preSUStagingCacheDeleteLevel"
+ "psusCacheDeleteLevel"
+ "setAdditionalInfo:"
+ "setPreSUStagingCacheDeleteLevel:"
+ "the cache delete level allowed for optional psus"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
- "+[SUSpace makeRoomForUpdate:completion:]"
- "+[SUSpace makeRoomForUpdate:completion:]_block_invoke_3"
- "+[SUSpace makeRoomForUpdate:completion:]_block_invoke_5"
- "+[SUSpace maxPreSUStagingOptionalSpaceForUpdate:]"
- "[%@] availableFreeSpace:%lld, totalSpaceNeededIncludingBuffer(buffer:5%%):%lld, allowedSpaceForOptionalAssets:%lld"
- "[PREFERENCES] using space overrides"
- "maxPreSUStagingOptionalSpaceForUpdate:"
- "no optional assets to stage for %@"
- "no update provided"

```
