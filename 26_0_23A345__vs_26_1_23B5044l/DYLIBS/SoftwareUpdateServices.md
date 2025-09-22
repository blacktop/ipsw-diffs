## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.2.1.0.0
-  __TEXT.__text: 0xaf05c
+950.40.24.0.0
+  __TEXT.__text: 0xaf8f8
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xac24
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x212ea
-  __TEXT.__gcc_except_tab: 0xff0
+  __TEXT.__objc_methlist: 0xac7c
+  __TEXT.__const: 0x308
+  __TEXT.__cstring: 0x213cc
+  __TEXT.__gcc_except_tab: 0x1028
   __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3150
-  __TEXT.__objc_classname: 0xf05
-  __TEXT.__objc_methname: 0x18c0b
-  __TEXT.__objc_methtype: 0x344d
-  __TEXT.__objc_stubs: 0x14200
+  __TEXT.__unwind_info: 0x3178
+  __TEXT.__objc_classname: 0xf08
+  __TEXT.__objc_methname: 0x18d6e
+  __TEXT.__objc_methtype: 0x3450
+  __TEXT.__objc_stubs: 0x142c0
   __DATA_CONST.__got: 0xd98
-  __DATA_CONST.__const: 0x2900
+  __DATA_CONST.__const: 0x29a0
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5bf8
+  __DATA_CONST.__objc_selrefs: 0x5c28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x12fc0
-  __AUTH_CONST.__objc_const: 0x157e0
+  __AUTH_CONST.__cfstring: 0x13060
+  __AUTH_CONST.__objc_const: 0x15880
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x950
+  __DATA.__objc_ivar: 0x95c
   __DATA.__data: 0xe98
   __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x1658

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7CF8224F-B45D-3EFD-B08F-6380B5C6C824
-  Functions: 4463
-  Symbols:   14818
-  CStrings:  10121
+  UUID: 6BDCA87E-8F21-3D51-9E90-7B94DE695524
+  Functions: 4475
+  Symbols:   14855
+  CStrings:  10144
 
Symbols:
+ -[SUAutoInstallManager _queue_setFailedToAutoInstallError:]
+ -[SUAutoInstallManager setFailedToAutoInstallError:]
+ -[SUDownloadOptions _clientIsLivabilityd]
+ -[SUManagerCore coreDescriptorForBuildVersion:versionExtra:isSplombo:]
+ -[SUManagerEngine _updatePolicyFactoryMetricEventFields:updateUUID:cleanupLevel:]
+ -[SUManagerEngineDownloadDescriptor cleanupLevel]
+ -[SUManagerEngineDownloadDescriptor initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:cleanupLevel:]
+ -[SUManagerEngineDownloadDescriptor setCleanupLevel:]
+ -[SUServerConfigurationManager stateQueue]
+ -[SUState failedToAutoInstallError]
+ -[SUState lastSpaceCleanupLevel]
+ -[SUState setFailedToAutoInstallError:]
+ -[SUState setLastSpaceCleanupLevel:]
+ OBJC_IVAR_$_SUState._failedToAutoInstallError
+ OBJC_IVAR_$_SUState._lastSpaceCleanupLevel
+ _OBJC_IVAR_$_SUAutoInstallManager._failedToAutoInstallError
+ _OBJC_IVAR_$_SUManagerEngineDownloadDescriptor._cleanupLevel
+ ___32-[SUState lastSpaceCleanupLevel]_block_invoke
+ ___35-[SUState failedToAutoInstallError]_block_invoke
+ ___36-[SUState setLastSpaceCleanupLevel:]_block_invoke
+ ___39-[SUState setFailedToAutoInstallError:]_block_invoke
+ ___52-[SUAutoInstallManager setFailedToAutoInstallError:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e23_v28?0B8Q12"NSError"20lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e20_v20?0B8"NSError"12ls40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e23_v24?0B8i12"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48r56r_e23_v28?0B8Q12"NSError"20lr48l8s40l8r56l8s32l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e17_v16?0"NSError"8ls48l8s32l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e23_v24?0B8i12"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r_e23_v28?0B8Q12"NSError"20lr56l8s48l8r64l8s32l8s40l8
+ ___block_literal_global.574
+ _objc_msgSend$_clientIsLivabilityd
+ _objc_msgSend$_queue_setFailedToAutoInstallError:
+ _objc_msgSend$_updatePolicyFactoryMetricEventFields:updateUUID:cleanupLevel:
+ _objc_msgSend$cleanupLevel
+ _objc_msgSend$coreDescriptorForBuildVersion:versionExtra:isSplombo:
+ _objc_msgSend$failedToAutoInstallError
+ _objc_msgSend$initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:cleanupLevel:
+ _objc_msgSend$lastSpaceCleanupLevel
+ _objc_msgSend$setCleanupLevel:
+ _objc_msgSend$setFailedToAutoInstallError:
+ _objc_msgSend$setLastSpaceCleanupLevel:
- -[SUAutoInstallManager _queue_setFailedToInstallError:]
- -[SUAutoInstallManager setFailedToInstallError:]
- -[SUManagerCore coreDescriptorForBuildVersion:versionExtra:]
- -[SUManagerEngine _updatePolicyFactoryMetricEventFields:updateUUID:]
- -[SUManagerEngineDownloadDescriptor initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:]
- _OBJC_IVAR_$_SUAutoInstallManager._failedToInstallError
- ___48-[SUAutoInstallManager setFailedToInstallError:]_block_invoke
- ___block_descriptor_56_e8_32s40bs_e41_v24?0"SUSpaceCheckResults"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r_e23_v28?0B8Q12"NSError"20ls40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56r_e23_v28?0B8Q12"NSError"20ls48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.573
- _objc_msgSend$_queue_setFailedToInstallError:
- _objc_msgSend$_updatePolicyFactoryMetricEventFields:updateUUID:
- _objc_msgSend$coreDescriptorForBuildVersion:versionExtra:
- _objc_msgSend$initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:
- _objc_msgSend$setFailedToInstallError:
CStrings:
+ "@88@0:8@16@24@32@40@48@56@64q72@80"
+ "Ignore the install-in-progress error and return a success"
+ "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@            \nLastSpaceCleanupLevel: %@"
+ "LastSpaceCleanupLevel"
+ "SUFailedToAutoInstallError"
+ "T@\"NSError\",&,N,V_failedToAutoInstallError"
+ "T@\"NSNumber\",&,N,V_cleanupLevel"
+ "T@\"NSNumber\",&,N,V_lastSpaceCleanupLevel"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_stateQueue"
+ "[Auto download] Beta: Downloading every 1 day"
+ "[Internal Only]\nHelps verify our ability to offload Apple Intelligence on low-disk space devices. We are asking you to consent to offloading Apple Intelligence. Offloading should immediately disable some Apple Intelligence features while on the current OS. If this fails, you will be prompted to file a radar."
+ "[makeRoom] result = %d, cleanupLevel = %d, error = %@"
+ "_cleanupLevel"
+ "_clientIsLivabilityd"
+ "_failedToAutoInstallError"
+ "_failedToAutoInstallError changed from %@ to %@"
+ "_lastSpaceCleanupLevel"
+ "_queue_setFailedToAutoInstallError:"
+ "_updatePolicyFactoryMetricEventFields:updateUUID:cleanupLevel:"
+ "asset:%@ releaseDate:%@ sessionID:%@ scanOptions:%@ downloadOptions:%@ installTonightConfig:%@ atPhase:%@ cleanupLevel:%@, coreDescriptor:%@"
+ "cleanupLevel"
+ "com.apple.livabilityd"
+ "coreDescriptorForBuildVersion:versionExtra:isSplombo:"
+ "failedToAutoInstallError"
+ "initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:cleanupLevel:"
+ "lastSpaceCleanupLevel"
+ "setCleanupLevel:"
+ "setFailedToAutoInstallError:"
+ "setLastSpaceCleanupLevel:"
+ "stateQueue"
+ "v24@?0B8i12@\"NSError\"16"
- "@80@0:8@16@24@32@40@48@56@64q72"
- "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@"
- "[Auto download] Customer: Downloading every 5 days"
- "[Intenral Only]\nTo help verify our ability to offload Apple Intelligence for users on low-disk space devices. We are asking you to consent to offloading Apple Intelligence. Offloading should immediately disable some Apple Intelligence features while on the current OS. If this fails, you will be prompted to file a radar."
- "[makeRoom] result = %d, error = %@"
- "_failedToInstallError"
- "_failedToInstallError changed from %@ to %@"
- "_queue_setFailedToInstallError:"
- "_updatePolicyFactoryMetricEventFields:updateUUID:"
- "asset:%@ releaseDate:%@ sessionID:%@ scanOptions:%@ downloadOptions:%@ installTonightConfig:%@ atPhase:%@, coreDescriptor:%@"
- "coreDescriptorForBuildVersion:versionExtra:"
- "initWithAsset:releaseDate:sessionID:scanOptions:downloadOptions:installTonightConfig:coreDescriptor:downloadAtPhase:"
- "rollbackCompleted:withError::"
- "setFailedToInstallError:"

```
