## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-296.100.0.0.0
-  __TEXT.__text: 0x19c580
-  __TEXT.__auth_stubs: 0x2a10
-  __TEXT.__objc_methlist: 0xc4c0
+302.100.0.0.0
+  __TEXT.__text: 0x19e128
+  __TEXT.__auth_stubs: 0x2a40
+  __TEXT.__objc_methlist: 0xc4d0
   __TEXT.__const: 0x2664
-  __TEXT.__gcc_except_tab: 0x465c
-  __TEXT.__cstring: 0x1498b
-  __TEXT.__oslogstring: 0x13b52
+  __TEXT.__gcc_except_tab: 0x49dc
+  __TEXT.__cstring: 0x14a3b
+  __TEXT.__oslogstring: 0x13d12
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x223c
-  __TEXT.__constg_swiftt: 0x3c04
+  __TEXT.__constg_swiftt: 0x3c0c
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_reflstr: 0x29db
   __TEXT.__swift5_fieldmd: 0x1820

   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x4d38
+  __TEXT.__unwind_info: 0x4e30
   __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0x2127
-  __TEXT.__objc_methname: 0x29e0e
-  __TEXT.__objc_methtype: 0x8c85
-  __TEXT.__objc_stubs: 0x18440
-  __DATA_CONST.__got: 0x1518
-  __DATA_CONST.__const: 0x4800
+  __TEXT.__objc_methname: 0x2a009
+  __TEXT.__objc_methtype: 0x8c8e
+  __TEXT.__objc_stubs: 0x18600
+  __DATA_CONST.__got: 0x1530
+  __DATA_CONST.__const: 0x48d0
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x598
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8598
+  __DATA_CONST.__objc_selrefs: 0x8608
   __DATA_CONST.__objc_protorefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x1518
-  __AUTH_CONST.__const: 0x5c80
-  __AUTH_CONST.__cfstring: 0xa0e0
-  __AUTH_CONST.__objc_const: 0x2cbb0
+  __AUTH_CONST.__auth_got: 0x1530
+  __AUTH_CONST.__const: 0x5c60
+  __AUTH_CONST.__cfstring: 0xa160
+  __AUTH_CONST.__objc_const: 0x2cba8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x2000
+  __AUTH.__objc_data: 0x1f60
   __AUTH.__data: 0x490
-  __DATA.__objc_ivar: 0xe20
+  __DATA.__objc_ivar: 0xe28
   __DATA.__data: 0x3c18
-  __DATA.__bss: 0x8c0
+  __DATA.__bss: 0x830
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x6140
+  __DATA_DIRTY.__objc_data: 0x61e8
   __DATA_DIRTY.__data: 0x1298
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x1038
+  __DATA_DIRTY.__bss: 0x10c8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3A9A6558-ABB4-3CB2-B749-F43CB367483C
-  Functions: 7340
-  Symbols:   19465
-  CStrings:  11348
+  UUID: 3FF0BB4A-6A42-332A-A864-DA372011D0D0
+  Functions: 7364
+  Symbols:   19559
+  CStrings:  11383
 
Symbols:
+ +[PBFGenericDisplayContext mainScreenDisplayContextsForKnownOrientationsAndUserInterfaceStyles:]
+ -[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]
+ -[PBFPosterExtensionDataStore overnightUpdate:completion:]
+ -[PBFPosterExtensionDataStore prewarm:completion:]
+ -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:]
+ -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:].cold.1
+ -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:].cold.2
+ -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:].cold.3
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:overnightUpdate:completion:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:prewarm:completion:]
+ -[PBFPosterSnapshotCoordinator cacheFuture].cold.1
+ -[PBFPosterSnapshotManager enqueueRequest:completion:]
+ -[_PBFGalleryCollectionViewController _rotationAssertionStateDidChange:]
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table166
+ GCC_except_table211
+ GCC_except_table238
+ GCC_except_table319
+ GCC_except_table326
+ GCC_except_table328
+ GCC_except_table349
+ GCC_except_table360
+ GCC_except_table378
+ GCC_except_table388
+ GCC_except_table402
+ GCC_except_table417
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table475
+ GCC_except_table493
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table83
+ GCC_except_table89
+ _CASupportsFeature
+ _CGImageGetOrientation
+ _OBJC_CLASS_$_PFLRUCache
+ _OBJC_CLASS_$_PFTCancellationToken
+ _OBJC_IVAR_$_PBFPosterSnapshotCoordinator._snapshotBundleLRUCache
+ _OBJC_IVAR_$__PBFGalleryCollectionViewController._rotationAssertion
+ _PBF_RDAR_159393603
+ _PUIImageOrientationForCGImageOrientation
+ _UIApplicationDidReceiveMemoryWarningNotification
+ __OBJC_$_PROP_LIST_PBFPosterSnapshotContext.272
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.908
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.914
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.910
+ ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.641
+ ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.650
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.368
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.369
+ ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.671
+ ___112-[PBFPosterExtensionDataStoreXPCServiceGlue server:refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.362
+ ___112-[PBFPosterExtensionDataStoreXPCServiceGlue server:refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.362.cold.1
+ ___112-[PBFPosterExtensionDataStoreXPCServiceGlue server:refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.362.cold.2
+ ___112-[PBFPosterExtensionDataStoreXPCServiceGlue server:refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke_2
+ ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.840
+ ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.890
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.583
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.584
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_6
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.788
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.795
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.800
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.812
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.814
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.803
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.813
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.816
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.820
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.824
+ ___137-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:]_block_invoke
+ ___137-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:]_block_invoke_2
+ ___137-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:]_block_invoke_3
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.210
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.222
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.222.cold.1
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.1
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.2
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.3
+ ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.230
+ ___155-[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]_block_invoke.574
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1006
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.974
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.975
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.982
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.983.cold.1
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.987
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.996
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1008
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.992
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.997
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1001
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1009
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.993
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1002
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1013
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.1014
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.920
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.922
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.870
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.870.cold.1
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.873
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.880
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.881
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.883
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.882
+ ___43-[PBFPosterSnapshotCoordinator cacheFuture]_block_invoke.10
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke.150
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_2.152
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_3.154
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_3.cold.1
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_3.cold.2
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_3.cold.3
+ ___54-[PBFPosterSnapshotManager enqueueRequest:completion:]_block_invoke
+ ___54-[PBFPosterSnapshotManager enqueueRequest:completion:]_block_invoke_2
+ ___57-[PBFPosterSnapshotCoordinator snapshotBundleForContext:]_block_invoke_2
+ ___57-[PBFPosterSnapshotCoordinator snapshotBundleForContext:]_block_invoke_3
+ ___61-[_PBFGalleryCollectionViewController noteEditingWillDismiss]_block_invoke
+ ___63-[PBFPosterSnapshotCoordinator ingestSnapshotsFromCoordinator:]_block_invoke.16
+ ___63-[PBFPosterSnapshotCoordinator ingestSnapshotsFromCoordinator:]_block_invoke.16.cold.1
+ ___68-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:]_block_invoke
+ ___68-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:]_block_invoke_2
+ ___72-[_PBFGalleryCollectionViewController _rotationAssertionStateDidChange:]_block_invoke
+ ___75-[PBFPosterExtensionDataStore _executeCleanupOfServerPosterIdentity:error:]_block_invoke.969
+ ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.691
+ ___90-[_PBFGalleryCollectionViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_4
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.300
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.325
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.335
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.329
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.336
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.334
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.334.cold.1
+ ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.720
+ ___96+[PBFGenericDisplayContext mainScreenDisplayContextsForKnownOrientationsAndUserInterfaceStyles:]_block_invoke
+ ___97-[PBFPosterSnapshotManager snapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]_block_invoke
+ ___Block_byref_object_copy_.298
+ ___Block_byref_object_copy_.871
+ ___Block_byref_object_dispose_.299
+ ___Block_byref_object_dispose_.872
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e5_q8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e12_v24?0Q8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e41_v32?0"PBFGenericDisplayContext"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e46_"<PFTFuture>"16?0"PUIPosterSnapshotBundle"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e20_v24?08"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e48_v24?0"PUIPosterSnapshotterResult"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e40_v24?0"PFServerPosterPath"8"NSError"16ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.140
+ ___block_literal_global.286
+ ___block_literal_global.366
+ ___block_literal_global.372
+ ___block_literal_global.414
+ ___block_literal_global.420
+ ___block_literal_global.423
+ ___block_literal_global.435
+ ___block_literal_global.469
+ ___block_literal_global.477
+ ___block_literal_global.490
+ ___block_literal_global.510
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.643
+ ___block_literal_global.674
+ ___block_literal_global.701
+ ___block_literal_global.703
+ ___block_literal_global.771
+ ___block_literal_global.776
+ ___block_literal_global.787
+ ___block_literal_global.797
+ ___block_literal_global.802
+ ___block_literal_global.903
+ ___block_literal_global.919
+ ___block_literal_global.937
+ ___block_literal_global.978
+ _block_copy_helper.140
+ _block_copy_helper.149
+ _block_copy_helper.160
+ _block_copy_helper.170
+ _block_copy_helper.181
+ _block_copy_helper.231
+ _block_copy_helper.242
+ _block_copy_helper.248
+ _block_copy_helper.270
+ _block_descriptor.142
+ _block_descriptor.151
+ _block_descriptor.162
+ _block_descriptor.172
+ _block_descriptor.183
+ _block_descriptor.233
+ _block_descriptor.244
+ _block_descriptor.250
+ _block_descriptor.272
+ _block_destroy_helper.141
+ _block_destroy_helper.150
+ _block_destroy_helper.161
+ _block_destroy_helper.171
+ _block_destroy_helper.182
+ _block_destroy_helper.232
+ _block_destroy_helper.243
+ _block_destroy_helper.249
+ _block_destroy_helper.271
+ _objc_msgSend$_fromWindowOrientation
+ _objc_msgSend$_rotationAssertionStateDidChange:
+ _objc_msgSend$canonicalLocaleIdentifierFromString:
+ _objc_msgSend$connectedDisplays
+ _objc_msgSend$executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:
+ _objc_msgSend$hostContext
+ _objc_msgSend$imageWithCGImage:scale:orientation:
+ _objc_msgSend$indexSetWithIndex:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$mainScreenDisplayContextsForKnownOrientationsAndUserInterfaceStyles:
+ _objc_msgSend$orderedSetWithCapacity:
+ _objc_msgSend$overnightUpdate:completion:
+ _objc_msgSend$prewarm:completion:
+ _objc_msgSend$primaryDisplayInfo
+ _objc_msgSend$refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:
+ _objc_msgSend$snapshotDefinitionIdentifier
+ _objc_msgSend$snapshotRequestForConfiguration:context:
+ _objc_msgSend$tokenWithCancellationBlock:
- -[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]
- -[PBFPosterExtensionDataStore overnightUpdateWithCompletion:]
- -[PBFPosterExtensionDataStore prewarmWithCompletion:]
- -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:].cold.1
- -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:].cold.2
- -[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:].cold.3
- -[PBFPosterExtensionDataStoreXPCServiceGlue server:overnightUpdateWithCompletion:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue server:prewarmWithCompletion:]
- -[PBFPosterSnapshotManager _loadReservationsForDefinitionForRequest:]
- -[PBFPosterSnapshotManager _loadReservationsForDefinitionForRequest:].cold.1
- GCC_except_table111
- GCC_except_table122
- GCC_except_table131
- GCC_except_table132
- GCC_except_table133
- GCC_except_table160
- GCC_except_table208
- GCC_except_table235
- GCC_except_table316
- GCC_except_table323
- GCC_except_table325
- GCC_except_table346
- GCC_except_table357
- GCC_except_table375
- GCC_except_table385
- GCC_except_table399
- GCC_except_table414
- GCC_except_table469
- GCC_except_table470
- GCC_except_table471
- GCC_except_table490
- GCC_except_table491
- GCC_except_table492
- GCC_except_table529
- GCC_except_table530
- GCC_except_table67
- GCC_except_table68
- GCC_except_table87
- __OBJC_$_PROP_LIST_PBFPosterSnapshotContext.260
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.904
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.910
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.906
- ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.637
- ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.646
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.365
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.366
- ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.667
- ___121-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:]_block_invoke
- ___121-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:]_block_invoke_2
- ___121-[PBFPosterExtensionDataStore refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:]_block_invoke_3
- ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.836
- ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.886
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.578
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.579
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.210
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.222
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.222.cold.1
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.1
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.2
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.225.cold.3
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.230
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.780
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.791
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.796
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.808
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.810
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.799
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.809
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.812
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.816
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.820
- ___155-[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]_block_invoke.571
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1002
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.970
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.971
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.978
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.979
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.979.cold.1
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.992
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1004
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.988
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.993
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1005
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.989
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.997
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1009
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.998
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.1010
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.916
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.918
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.866
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.866.cold.1
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.869
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.876
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.877
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.879
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.878
- ___43-[PBFPosterSnapshotCoordinator cacheFuture]_block_invoke.6
- ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_4
- ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_5
- ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_6
- ___63-[PBFPosterSnapshotCoordinator ingestSnapshotsFromCoordinator:]_block_invoke.12
- ___63-[PBFPosterSnapshotCoordinator ingestSnapshotsFromCoordinator:]_block_invoke.12.cold.1
- ___75-[PBFPosterExtensionDataStore _executeCleanupOfServerPosterIdentity:error:]_block_invoke.965
- ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.687
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.322
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.332
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.326
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.333
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.331
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.331.cold.1
- ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.716
- ___Block_byref_object_copy_.296
- ___Block_byref_object_copy_.867
- ___Block_byref_object_dispose_.297
- ___Block_byref_object_dispose_.868
- ___block_descriptor_32_e51_"<PFTFuture>"16?0"PUIPosterSnapshotSQLiteCache"8l
- ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40s48s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e48_v24?0"PUIPosterSnapshotterResult"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e40_v24?0"PFServerPosterPath"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.128
- ___block_literal_global.152
- ___block_literal_global.285
- ___block_literal_global.364
- ___block_literal_global.369
- ___block_literal_global.403
- ___block_literal_global.418
- ___block_literal_global.421
- ___block_literal_global.427
- ___block_literal_global.463
- ___block_literal_global.474
- ___block_literal_global.487
- ___block_literal_global.507
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.639
- ___block_literal_global.670
- ___block_literal_global.695
- ___block_literal_global.697
- ___block_literal_global.767
- ___block_literal_global.772
- ___block_literal_global.783
- ___block_literal_global.793
- ___block_literal_global.798
- ___block_literal_global.899
- ___block_literal_global.915
- ___block_literal_global.933
- ___block_literal_global.974
- _block_copy_helper.148
- _block_copy_helper.169
- _block_copy_helper.180
- _block_copy_helper.219
- _block_copy_helper.230
- _block_copy_helper.241
- _block_copy_helper.258
- _block_copy_helper.269
- _block_descriptor.150
- _block_descriptor.171
- _block_descriptor.182
- _block_descriptor.221
- _block_descriptor.232
- _block_descriptor.243
- _block_descriptor.260
- _block_descriptor.271
- _block_destroy_helper.149
- _block_destroy_helper.170
- _block_destroy_helper.181
- _block_destroy_helper.220
- _block_destroy_helper.231
- _block_destroy_helper.242
- _block_destroy_helper.259
- _block_destroy_helper.270
- _objc_msgSend$executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$overnightUpdateWithCompletion:
- _objc_msgSend$prewarmWithCompletion:
CStrings:
+ "(%p) Gallery orientation changed - hiding live poster previews before rotating"
+ "(%p) Gallery rotation transitions complete - resuming live asset helper"
+ "(%{public}@) finished with no errors"
+ "<SnapshotCoordinator-%{public}@-%{public}@> cache future finished"
+ "@\"PFLRUCache\""
+ "@32@0:8@16@?24"
+ "Duplicate completion callback received for snapshot request. Ignoring."
+ "Failed to refresh snapshots for %@: %{public}@"
+ "Snapshot request failed for definition %@: %@"
+ "Snapshot succeeded but imageURL was nil for definition: %@"
+ "Snapshot succeeded but the resulting imageURL was nil."
+ "Successfully refreshed snapshots poster reload for %@"
+ "Will refresh snapshots for %@"
+ "_fromWindowOrientation"
+ "_rotationAssertion"
+ "_rotationAssertionStateDidChange:"
+ "_snapshotBundleLRUCache"
+ "cancellation token"
+ "canonicalLocaleIdentifierFromString:"
+ "connectedDisplays"
+ "enqueueRequest:completion:"
+ "executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:"
+ "executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:completion:"
+ "galleryRotationAssertion"
+ "hostContext"
+ "imageWithCGImage:scale:orientation:"
+ "indexSetWithIndex:"
+ "initWithCapacity:"
+ "mainScreenDisplayContextsForKnownOrientationsAndUserInterfaceStyles:"
+ "orderedSetWithCapacity:"
+ "overnightUpdate:completion:"
+ "prewarm:completion:"
+ "primaryDisplayInfo"
+ "q8@?0"
+ "refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:completion:"
+ "server:overnightUpdate:completion:"
+ "server:prewarm:completion:"
+ "setFlipsHorizontalAxis:"
+ "snapshotBundleForContext"
+ "snapshotDefinitionIdentifier"
+ "tokenWithCancellationBlock:"
+ "v32@?0@\"PBFGenericDisplayContext\"8Q16^B24"
+ "v40@0:8@\"PRSServer\"16@\"PRSHostContext\"24@?<v@?@\"NSError\">32"
+ "v68@0:8@16@24q32Q40q48B56@?60"
+ "viewWillTransitionToSize"
- "(%{public}@) finished wih no errors"
- "<SnapshotCoordinator-%{public}@-%{public}@> cache future finished successfully"
- "@\"UIImage\"40@0:8@\"PBFPosterSnapshotRequest\"16@\"PBFPosterSnapshotDefinition\"24o^@32"
- "INCONGRUENT HEIGHTS: adaptive=%f configured=%f"
- "_loadReservationsForDefinitionForRequest:"
- "executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:"
- "imageURL was nil"
- "imageWithCGImage:"
- "overnightUpdateWithCompletion:"
- "prewarmWithCompletion:"
- "server:overnightUpdateWithCompletion:"
- "server:prewarmWithCompletion:"
- "skipping reservation; had error: %{public}@"
- "v60@0:8@16q24Q32q40B48@?52"

```
