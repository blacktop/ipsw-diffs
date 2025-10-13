## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-302.100.0.0.0
-  __TEXT.__text: 0x821b0
+304.1.2.100.0
+  __TEXT.__text: 0x82d08
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xa274
-  __TEXT.__const: 0x828
-  __TEXT.__cstring: 0x7c60
-  __TEXT.__oslogstring: 0x46dc
-  __TEXT.__gcc_except_tab: 0x1238
+  __TEXT.__objc_methlist: 0xa254
+  __TEXT.__const: 0x838
+  __TEXT.__cstring: 0x7e20
+  __TEXT.__oslogstring: 0x4797
+  __TEXT.__gcc_except_tab: 0xf54
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x2c58
-  __TEXT.__objc_classname: 0x15fe
-  __TEXT.__objc_methname: 0x181a4
-  __TEXT.__objc_methtype: 0x415f
-  __TEXT.__objc_stubs: 0x120a0
-  __DATA_CONST.__got: 0x948
-  __DATA_CONST.__const: 0x28e8
+  __TEXT.__unwind_info: 0x2ba0
+  __TEXT.__objc_classname: 0x1600
+  __TEXT.__objc_methname: 0x182c1
+  __TEXT.__objc_methtype: 0x41b2
+  __TEXT.__objc_stubs: 0x12060
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__const: 0x2960
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5480
+  __DATA_CONST.__objc_selrefs: 0x5458
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x858
   __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x6440
-  __AUTH_CONST.__objc_const: 0x1cc98
+  __AUTH_CONST.__cfstring: 0x6480
+  __AUTH_CONST.__objc_const: 0x1ccd8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x1b8
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xa6c
+  __DATA.__objc_ivar: 0xa74
   __DATA.__data: 0x18e0
-  __DATA.__bss: 0x438
+  __DATA.__bss: 0x448
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E59C96B5-DCF4-34C6-89BB-D3956FB4F640
-  Functions: 4032
-  Symbols:   13908
-  CStrings:  6610
+  UUID: F0BFCA97-9D31-315E-9189-C065CEACFDBC
+  Functions: 4045
+  Symbols:   13915
+  CStrings:  6628
 
Symbols:
+ +[PBUIURLBackedSnapshotSource buildCacheIdentifierForURL:]
+ -[PBUIPosterHomeViewController _didFinishRotating]
+ -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]
+ -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:].cold.1
+ -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:].cold.2
+ -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:].cold.3
+ -[PBUIPosterVariantViewController _scheduleSnapshotIfNeeded:].cold.2
+ -[PBUIPosterVariantViewController isSnapshotting]
+ -[PBUIPosterViewController activeVariantForPosterComponent:]
+ -[PBUIPosterWallpaperRemoteViewController activeVariantForPosterComponent:]
+ -[PBUIPosterWallpaperViewController activeVariantForPosterComponent:]
+ -[PBUIURLBackedSnapshotSource _lock_encoderForSnapshot]
+ -[PBUIURLBackedSnapshotSource _lock_loadColorStatisticsWithError:]
+ -[PBUIURLBackedSnapshotSource _lock_loadInterfaceOrientation:]
+ -[PBUIURLBackedSnapshotSource _lock_loadSnapshotImageWithError:]
+ -[PBUIURLBackedSnapshotSource _lock_loadSnapshotMetadataWithError:]
+ -[PBUIURLBackedSnapshotSource _lock_removeOnDiskSnapshotWithError:]
+ -[PBUIURLBackedSnapshotSource _lock_snapshotMetadata]
+ -[PBUIURLBackedSnapshotSource _lock_storeColorStatistics:error:]
+ -[PBUIURLBackedSnapshotSource _lock_storeSnapshot:error:]
+ -[PBUIURLBackedSnapshotSource _lock_storeSnapshot:error:].cold.1
+ -[PBUIURLBackedSnapshotSource _lock_storeSnapshotFromURL:error:]
+ -[PBUIURLBackedSnapshotSource _lock_storeSnapshotFromURL:error:].cold.1
+ -[PBUIURLBackedSnapshotSource _lock_storeSnapshotMetadata:error:]
+ -[PBUIURLBackedSnapshotSource updateFromPathProvider:].cold.1
+ -[PBUIURLBackedSnapshotSource updateFromPathProvider:].cold.2
+ -[PBUIURLBackedSnapshotSource updateFromPathProvider:].cold.3
+ -[PBUIURLBackedSnapshotSource updatePosterPreferredProminentColor:error:].cold.1
+ -[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:]
+ GCC_except_table104
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table155
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table39
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table65
+ GCC_except_table88
+ _BSInterfaceOrientationIsValid
+ _NSLocalizedDescriptionKey
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_cacheIdentifier
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_contentColorStatistics
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_derivedProminentPosterColor
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_deviceOrientation
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_imageEncoder
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_interfaceOrientation
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_legibilitySettings
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_posterPreferredProminentColor
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_snapshot
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_snapshotColorStatisticsURL
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_snapshotMetadata
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_snapshotMetadataURL
+ _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._lock_snapshotURL
+ _PBUIColorSamplingQueue
+ _PBUIColorSamplingQueue.cold.1
+ __OBJC_$_CLASS_METHODS_PBUIURLBackedSnapshotSource
+ ___111-[PBUIPosterVariantViewController postprocessNewSnapshot:orSnapshotBundle:colorStatistics:metadata:completion:]_block_invoke_2
+ ___39-[PBUIURLBackedSnapshotSource snapshot]_block_invoke
+ ___54-[PBUIURLBackedSnapshotSource updateFromPathProvider:]_block_invoke
+ ___54-[PBUIURLBackedSnapshotSource updateFromPathProvider:]_block_invoke.11
+ ___56-[PBUIURLBackedSnapshotSource invalidateCurrentSnapshot]_block_invoke
+ ___56-[PBUIURLBackedSnapshotSource invalidateCurrentSnapshot]_block_invoke.12
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke.87
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.88
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.88.cold.1
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.88.cold.2
+ ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_5
+ ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_5.cold.1
+ ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.44
+ ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.44.cold.1
+ ___69-[PBUIPosterHomeViewController noteWillRotateToInterfaceOrientation:]_block_invoke_2
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.160
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.161
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.162
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.165
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.169
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.178
+ ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke.120
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke.cold.1
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke_2
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke_3
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke_4
+ ___95-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:attemptNumber:]_block_invoke_5
+ ___98-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:]_block_invoke
+ ___98-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:]_block_invoke_2
+ ___98-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:]_block_invoke_3
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72w_e41_v24?0"_EXExtensionProcess"8"NSError"16lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.534
+ ___getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientationSymbolLoc_block_invoke
+ ___getPUIPosterSnapshotBundleInfoKeyInterfaceOrientationSymbolLoc_block_invoke
+ _getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientation
+ _getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientation.cold.1
+ _getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientationSymbolLoc
+ _getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientationSymbolLoc.ptr
+ _getPUIPosterSnapshotBundleInfoKeyInterfaceOrientation
+ _getPUIPosterSnapshotBundleInfoKeyInterfaceOrientation.cold.1
+ _getPUIPosterSnapshotBundleInfoKeyInterfaceOrientationSymbolLoc
+ _getPUIPosterSnapshotBundleInfoKeyInterfaceOrientationSymbolLoc.ptr
+ _objc_msgSend$_didFinishRotating
+ _objc_msgSend$_lock_encoderForSnapshot
+ _objc_msgSend$_lock_loadColorStatisticsWithError:
+ _objc_msgSend$_lock_loadInterfaceOrientation:
+ _objc_msgSend$_lock_loadSnapshotImageWithError:
+ _objc_msgSend$_lock_loadSnapshotMetadataWithError:
+ _objc_msgSend$_lock_removeOnDiskSnapshotWithError:
+ _objc_msgSend$_lock_snapshotMetadata
+ _objc_msgSend$_lock_storeColorStatistics:error:
+ _objc_msgSend$_lock_storeSnapshot:error:
+ _objc_msgSend$_lock_storeSnapshotFromURL:error:
+ _objc_msgSend$_lock_storeSnapshotMetadata:error:
+ _objc_msgSend$_prepareFauxExternalSceneFromScene:completion:attemptNumber:
+ _objc_msgSend$activeVariantForPosterComponent:
+ _objc_msgSend$bs_isAppearingOrAppeared
+ _objc_msgSend$buildCacheIdentifierForURL:
+ _objc_msgSend$isSnapshotting
+ _objc_msgSend$pf_sha256Hash
+ _objc_msgSend$setSnapshotDeviceOrientation:forURL:
+ _objc_msgSend$setSnapshotInterfaceOrientation:forURL:
+ _objc_msgSend$setSnapshotSource:
+ _objc_msgSend$snapshotSource:failedToReadColorStatisticsAtURL:error:
+ _objc_msgSend$updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:
- -[PBUIFixedReplicaSourceProvider setIdentifier:]
- -[PBUIPosterHomeViewController noteDidRotateToInterfaceOrientation:]
- -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:].cold.1
- -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:].cold.2
- -[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:].cold.3
- -[PBUIPosterVariantViewController _snapshotScene:completion:].cold.1
- -[PBUIURLBackedSnapshotSource buildCacheIdentifier]
- -[PBUIURLBackedSnapshotSource colorStatisticsDidChange:]
- -[PBUIURLBackedSnapshotSource encoderForSnapshot]
- -[PBUIURLBackedSnapshotSource initWithPathProvider:format:delegate:]
- -[PBUIURLBackedSnapshotSource initWithSnapshotURL:colorStatisticsURL:metadataURL:format:delegate:]
- -[PBUIURLBackedSnapshotSource notifyObserversIfNeeded]
- -[PBUIURLBackedSnapshotSource notifyObservers]
- -[PBUIURLBackedSnapshotSource performBatchUpdates:]
- -[PBUIURLBackedSnapshotSource readColorStatisticsFromDisk]
- -[PBUIURLBackedSnapshotSource readFromDiskWithError:]
- -[PBUIURLBackedSnapshotSource readMetadataFromDisk]
- -[PBUIURLBackedSnapshotSource removeOnDiskSnapshotWithError:]
- -[PBUIURLBackedSnapshotSource saveColorStatistics]
- -[PBUIURLBackedSnapshotSource setLegibilitySettings:]
- -[PBUIURLBackedSnapshotSource setSnapshotColorStatisticsURL:]
- -[PBUIURLBackedSnapshotSource setSnapshotMetadataURL:]
- -[PBUIURLBackedSnapshotSource setSnapshotURL:]
- -[PBUIURLBackedSnapshotSource setupSnapshotSourceForSnapshotURL:snapshotColorStatisticsURL:snapshotMetadataURL:]
- -[PBUIURLBackedSnapshotSource updateColorStatisticsWith:]
- -[PBUIURLBackedSnapshotSource updateFromDisk]
- -[PBUIURLBackedSnapshotSource updateMetadataWith:error:]
- -[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]
- GCC_except_table10
- GCC_except_table113
- GCC_except_table116
- GCC_except_table118
- GCC_except_table121
- GCC_except_table123
- GCC_except_table125
- GCC_except_table134
- GCC_except_table144
- GCC_except_table147
- GCC_except_table154
- GCC_except_table156
- GCC_except_table18
- GCC_except_table24
- GCC_except_table31
- GCC_except_table32
- GCC_except_table35
- GCC_except_table41
- GCC_except_table59
- _BSDispatchQueueCreateSerial
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._cacheIdentifier
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._contentColorStatistics
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._isDirty
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._isFrozen
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._legibilitySettings
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._needsColorSettingsUpdate
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshot
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshotColorStatisticsURL
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshotImageWriteQueue
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshotMetadata
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshotMetadataURL
- _OBJC_IVAR_$_PBUIURLBackedSnapshotSource._snapshotURL
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.17
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.cold.1
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.cold.2
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.cold.3
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.cold.4
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke.cold.5
- ___103-[PBUIURLBackedSnapshotSource updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:]_block_invoke_2
- ___112-[PBUIURLBackedSnapshotSource setupSnapshotSourceForSnapshotURL:snapshotColorStatisticsURL:snapshotMetadataURL:]_block_invoke
- ___54-[PBUIURLBackedSnapshotSource notifyObserversIfNeeded]_block_invoke
- ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke.96
- ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97
- ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97.cold.1
- ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97.cold.2
- ___61-[PBUIPosterVariantViewController _snapshotScene:completion:]_block_invoke_4.cold.1
- ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.53
- ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.53.cold.1
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.154
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.155
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.156
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.159
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.163
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.172
- ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke.114
- ___81-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:]_block_invoke
- ___81-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:]_block_invoke.cold.1
- ___81-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:]_block_invoke_2
- ___81-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:]_block_invoke_3
- ___81-[PBUIPosterVariantViewController _prepareFauxExternalSceneFromScene:completion:]_block_invoke_4
- ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e41_v24?0"_EXExtensionProcess"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.543
- _objc_msgSend$addColorStatisticsObserver:
- _objc_msgSend$animateWithDuration:animations:
- _objc_msgSend$buildCacheIdentifier
- _objc_msgSend$createFileAtPath:contents:attributes:
- _objc_msgSend$encoderForSnapshot
- _objc_msgSend$initWithPathProvider:format:delegate:
- _objc_msgSend$initWithSnapshotURL:colorStatisticsURL:metadataURL:format:delegate:
- _objc_msgSend$notifyObservers
- _objc_msgSend$notifyObserversIfNeeded
- _objc_msgSend$performBatchUpdates:
- _objc_msgSend$pui_cacheIdentifier
- _objc_msgSend$readColorStatisticsFromDisk
- _objc_msgSend$readFromDiskWithError:
- _objc_msgSend$readMetadataFromDisk
- _objc_msgSend$removeOnDiskSnapshotWithError:
- _objc_msgSend$saveColorStatistics
- _objc_msgSend$setSnapshotColorStatisticsURL:
- _objc_msgSend$setSnapshotMetadataURL:
- _objc_msgSend$setSnapshotURL:
- _objc_msgSend$stringByAppendingFormat:
- _objc_msgSend$updateColorStatisticsWith:
- _objc_msgSend$updateFromDisk
- _objc_msgSend$updateMetadataWith:error:
- _objc_msgSend$updateWithColorBoxes:
- _objc_msgSend$updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:
CStrings:
+ "%@-%@-(%@)"
+ "@\"PUIImageEncoder\""
+ "Could not read snapshot color statistics: %{public}@"
+ "Could not read snapshot metadata: %{public}@"
+ "Could not read snapshot: %{public}@"
+ "Failed to boot up extension instance for faux external scene preparation after %lu attempts: %@"
+ "Failed to create UIImage from snapshot file"
+ "Failed to load UIImage from snapshot file"
+ "Oct  8 2025 23:04:29"
+ "PBUISnapshotErrorDomain"
+ "PUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientation"
+ "PUIPosterSnapshotBundleInfoKeyInterfaceOrientation"
+ "T@\"NSDictionary\",R,C,N,V_lock_snapshotMetadata"
+ "T@\"NSString\",C,N,V_lock_cacheIdentifier"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"NSURL\",R,N,V_lock_snapshotColorStatisticsURL"
+ "T@\"NSURL\",R,N,V_lock_snapshotMetadataURL"
+ "T@\"NSURL\",R,N,V_lock_snapshotURL"
+ "T@\"PUIColorStatistics\",R,C,N,V_lock_contentColorStatistics"
+ "T@\"UIColor\",R,C,N,V_lock_derivedProminentPosterColor"
+ "T@\"UIColor\",R,C,N,V_lock_posterPreferredProminentColor"
+ "T@\"UIImage\",&,N,V_lock_snapshot"
+ "T@\"_UILegibilitySettings\",R,C,N,V_lock_legibilitySettings"
+ "[%{public}@] will not schedule snapshot unless is active variant, and we are not: %{public}@"
+ "_didFinishRotating"
+ "_lock"
+ "_lock_cacheIdentifier"
+ "_lock_contentColorStatistics"
+ "_lock_derivedProminentPosterColor"
+ "_lock_deviceOrientation"
+ "_lock_encoderForSnapshot"
+ "_lock_imageEncoder"
+ "_lock_interfaceOrientation"
+ "_lock_legibilitySettings"
+ "_lock_loadColorStatisticsWithError:"
+ "_lock_loadInterfaceOrientation:"
+ "_lock_loadSnapshotImageWithError:"
+ "_lock_loadSnapshotMetadataWithError:"
+ "_lock_posterPreferredProminentColor"
+ "_lock_removeOnDiskSnapshotWithError:"
+ "_lock_snapshot"
+ "_lock_snapshotColorStatisticsURL"
+ "_lock_snapshotMetadata"
+ "_lock_snapshotMetadataURL"
+ "_lock_snapshotURL"
+ "_lock_storeColorStatistics:error:"
+ "_lock_storeSnapshot:error:"
+ "_lock_storeSnapshotFromURL:error:"
+ "_lock_storeSnapshotMetadata:error:"
+ "_prepareFauxExternalSceneFromScene:completion:attemptNumber:"
+ "activeVariantForPosterComponent:"
+ "bs_isAppearingOrAppeared"
+ "buildCacheIdentifierForURL:"
+ "isSnapshotting"
+ "moved to active variant"
+ "moving to inactive variant"
+ "need snapshot"
+ "pf_sha256Hash"
+ "q24@0:8@\"<PBUIPosterComponent>\"16"
+ "rotating to %lu"
+ "rotation complete"
+ "setSnapshotDeviceOrientation:forURL:"
+ "setSnapshotInterfaceOrientation:forURL:"
+ "tried to write snapshot bundle image; failed with error: %{public}@"
+ "typeof (((typeof (PUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientation) (*)(void))0)()) getPUIPosterSnapshotBundleInfoKeyDeviceInterfaceOrientation(void)"
+ "typeof (((typeof (PUIPosterSnapshotBundleInfoKeyInterfaceOrientation) (*)(void))0)()) getPUIPosterSnapshotBundleInfoKeyInterfaceOrientation(void)"
+ "updatePosterPreferredProminentColor failed for error: %{public}@"
+ "updatePosterPreferredProminentColor ran successfully."
+ "updateWithImage:orImageAtURL:contentColorStatistics:metadata:error:"
+ "v40@0:8@16@?24Q32"
+ "v56@0:8@16@24@32@40o^@48"
+ "\xf1"
- "%@ (%@)"
- "@24@0:8o^@16"
- "Failed to boot up extension instance for faux external scene preparation: %@"
- "Poster scene is not ready for snapshotting (not suspended)."
- "Sep 29 2025 20:56:45"
- "T@\"NSDictionary\",R,C,N,V_snapshotMetadata"
- "T@\"NSURL\",R,N,V_snapshotColorStatisticsURL"
- "T@\"NSURL\",R,N,V_snapshotMetadataURL"
- "T@\"NSURL\",R,N,V_snapshotURL"
- "T@\"PUIColorStatistics\",R,C,N,V_contentColorStatistics"
- "T@\"_UILegibilitySettings\",R,C,N,V_legibilitySettings"
- "["
- "]-[%@]"
- "_contentColorStatistics"
- "_isDirty"
- "_isFrozen"
- "_needsColorSettingsUpdate"
- "_snapshotColorStatisticsURL"
- "_snapshotImageWriteQueue"
- "_snapshotMetadata"
- "_snapshotMetadataURL"
- "_snapshotURL"
- "addColorStatisticsObserver:"
- "animateWithDuration:animations:"
- "buildCacheIdentifier"
- "caches were updated"
- "com.apple.PaperBoardUI.snapshotImageWriteQueue"
- "createFileAtPath:contents:attributes:"
- "did rotate to new interface orientation"
- "encoderForSnapshot"
- "initWithPathProvider:format:delegate:"
- "initWithSnapshotURL:colorStatisticsURL:metadataURL:format:delegate:"
- "notifyObservers"
- "notifyObserversIfNeeded"
- "performBatchUpdates:"
- "pui_cacheIdentifier"
- "readColorStatisticsFromDisk"
- "readFromDiskWithError:"
- "readMetadataFromDisk"
- "removeOnDiskSnapshotWithError:"
- "saveColorStatistics"
- "setSnapshotColorStatisticsURL:"
- "setSnapshotMetadataURL:"
- "setSnapshotURL:"
- "setupSnapshotSourceForSnapshotURL:snapshotColorStatisticsURL:snapshotMetadataURL:"
- "snapshot bundle file copy failed; will fallback to encoder"
- "stringByAppendingFormat:"
- "tried to use copy on snapshot bundle image; failed with error: %{public}@"
- "tried to use read image; failed with error: %{public}@"
- "tried to use read newImage; failed with error: %{public}@"
- "updateColorStatisticsWith:"
- "updateFromDisk"
- "updateMetadataWith:error:"
- "updateWithColorBoxes:"
- "updateWithImage:orImageAtURL:contentColorStatistics:metadata:completion:"
- "\x91"

```
