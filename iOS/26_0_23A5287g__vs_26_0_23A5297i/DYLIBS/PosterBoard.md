## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-283.101.0.0.0
-  __TEXT.__text: 0x197394
-  __TEXT.__auth_stubs: 0x29d0
-  __TEXT.__objc_methlist: 0xc3b0
-  __TEXT.__const: 0x2684
-  __TEXT.__gcc_except_tab: 0x44e8
-  __TEXT.__cstring: 0x1406b
-  __TEXT.__oslogstring: 0x12a12
+286.101.0.0.0
+  __TEXT.__text: 0x199228
+  __TEXT.__auth_stubs: 0x2a20
+  __TEXT.__objc_methlist: 0xc410
+  __TEXT.__const: 0x2674
+  __TEXT.__gcc_except_tab: 0x45bc
+  __TEXT.__cstring: 0x1439b
+  __TEXT.__oslogstring: 0x12d12
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
-  __TEXT.__swift5_typeref: 0x2234
-  __TEXT.__constg_swiftt: 0x3c04
+  __TEXT.__swift5_typeref: 0x223c
+  __TEXT.__constg_swiftt: 0x3c1c
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x29db
-  __TEXT.__swift5_fieldmd: 0x1820
+  __TEXT.__swift5_reflstr: 0x2a0b
+  __TEXT.__swift5_fieldmd: 0x182c
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0xe0
   __TEXT.__swift5_types: 0x130
-  __TEXT.__swift5_capture: 0x1378
+  __TEXT.__swift5_capture: 0x1384
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x4c98
+  __TEXT.__unwind_info: 0x4d08
   __TEXT.__eh_frame: 0x958
-  __TEXT.__objc_classname: 0x206d
-  __TEXT.__objc_methname: 0x296a0
-  __TEXT.__objc_methtype: 0x8c16
-  __TEXT.__objc_stubs: 0x17c80
-  __DATA_CONST.__got: 0x14c0
-  __DATA_CONST.__const: 0x46e0
+  __TEXT.__objc_classname: 0x207e
+  __TEXT.__objc_methname: 0x29920
+  __TEXT.__objc_methtype: 0x8c3c
+  __TEXT.__objc_stubs: 0x17f40
+  __DATA_CONST.__got: 0x14c8
+  __DATA_CONST.__const: 0x4780
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x580
+  __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8438
-  __DATA_CONST.__objc_protorefs: 0x210
+  __DATA_CONST.__objc_selrefs: 0x84b0
+  __DATA_CONST.__objc_protorefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x14f8
-  __AUTH_CONST.__const: 0x5ae0
-  __AUTH_CONST.__cfstring: 0x9a00
-  __AUTH_CONST.__objc_const: 0x2c788
+  __AUTH_CONST.__auth_got: 0x1520
+  __AUTH_CONST.__const: 0x5b68
+  __AUTH_CONST.__cfstring: 0x9c20
+  __AUTH_CONST.__objc_const: 0x2c8a8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x1ec0
   __AUTH.__data: 0x490
-  __DATA.__objc_ivar: 0xe04
-  __DATA.__data: 0x3b78
-  __DATA.__bss: 0x920
+  __DATA.__objc_ivar: 0xe14
+  __DATA.__data: 0x3bd8
+  __DATA.__bss: 0x930
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x6140
-  __DATA_DIRTY.__data: 0x1258
+  __DATA_DIRTY.__objc_data: 0x6160
+  __DATA_DIRTY.__data: 0x1288
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xf68
   __DATA_DIRTY.__common: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0141BCE-FADF-3D01-8C75-E4FED5913D9F
-  Functions: 7265
-  Symbols:   19180
-  CStrings:  11089
+  UUID: 91ED0BE9-22E6-3283-8B86-278F65DB6F18
+  Functions: 7288
+  Symbols:   19278
+  CStrings:  11158
 
Symbols:
+ -[PBFApplicationStateMonitor isForeground]
+ -[PBFComplicationSnapshotRequest cacheIdentifier]
+ -[PBFComplicationSnapshotService _buildAndExecuteComplicationSnapshotterForRequest:]
+ -[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:trimCache:]
+ -[PBFComplicationSnapshotService init].cold.1
+ -[PBFComplicationSnapshotter _main_kickoffHostViewController:attempt:]
+ -[PBFComplicationSnapshotter _main_kickoffHostViewController:attempt:].cold.1
+ -[PBFComplicationSnapshotter _main_kickoffHostViewController:attempt:].cold.2
+ -[PBFComplicationSnapshotter _startAttempt:previousError:]
+ -[PBFFocusPosterSelectionViewController viewDidDisappear:]
+ -[PBFFocusPosterSelectionViewController viewWillAppear:]
+ -[PBFGalleryConfiguration trimComplicationsCache]
+ -[PBFPosterAssetViewController _updateSnapshotBundleRequestsForActiveDisplayContext]
+ -[PBFPosterExtensionDataStore applicationStateMonitor]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_fixComplicationLayout]
+ -[PBFPosterGalleryAssetHelper _invalidateAllHistogramCache]
+ -[PBFPosterGalleryAssetHelper _invalidateHistogramCacheForPosterPreview:]
+ -[PBFPosterGalleryAssetHelper _updateHistogramCacheIfNeeded]
+ -[PBFPosterGalleryAssetHelper _updateHydrationStateIfNeeded].cold.4
+ -[PBFPosterGalleryAssetHelper _updateHydrationStateIfNeeded].cold.5
+ -[PBFPosterGalleryAssetHelper _updateHydrationStateIfNeeded].cold.6
+ -[PBFPosterGalleryPreviewViewController editingExtensionInstance]
+ -[PBFPosterGalleryPreviewViewController setEditingExtensionInstance:]
+ -[PBFPosterSnapshotManager _lock_cleanupAfterRequest:shouldTerminateProcess:]
+ -[PBFPosterSnapshotManager _lock_cleanupAfterRequest:shouldTerminateProcess:].cold.1
+ -[PBFPosterSnapshotManager _lock_cleanupAfterRequest:shouldTerminateProcess:].cold.2
+ -[_PBFPosterSceneViewController setDisplayContext:animationSettings:fence:]
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table16
+ GCC_except_table467
+ GCC_except_table487
+ GCC_except_table524
+ GCC_except_table527
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table67
+ GCC_except_table81
+ _OBJC_IVAR_$_PBFComplicationSnapshotRequest._cacheIdentifier
+ _OBJC_IVAR_$_PBFComplicationSnapshotService._complicationImageCache
+ _OBJC_IVAR_$_PBFComplicationSnapshotService._lock_finishedRequestToFuture
+ _OBJC_IVAR_$_PBFComplicationSnapshotService._lock_inflightRequestToFuture
+ _OBJC_IVAR_$_PBFFocusPosterSelectionViewController._state
+ _OBJC_IVAR_$_PBFPosterGalleryAssetHelper._displayContextHistogramCache
+ _OBJC_IVAR_$_PBFPosterGalleryAssetHelper._previewsRequiringHistogramCacheInvalidation
+ _OBJC_IVAR_$_PBFPosterGalleryPreviewViewController._editingExtensionInstance
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_preventKickCount
+ _OBJC_IVAR_$__PBFGalleryCollectionViewController._editingPresentationState
+ _PF_IS_PAD_DEVICE
+ _PRSceneViewControllerAdditionalInfoKeyEditingNewPosterFromConfiguration
+ __OBJC_$_PROP_LIST_PBFPosterSnapshotContext.241
+ __OBJC_$_PROTOCOL_REFS__UIMorphable
+ __OBJC_LABEL_PROTOCOL_$__UIMorphable
+ __OBJC_PROTOCOL_$__UIMorphable
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.885
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.891
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.887
+ ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.618
+ ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.627
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.345
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.346
+ ___111-[PBFFocusPosterSelectionViewController initWithActivityUUID:activityIdentifier:galleryDataProvider:dataStore:]_block_invoke.138
+ ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.648
+ ___113-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_performNecessaryMigrationsForDataStoreAtURL:shouldForce:error:]_block_invoke.175
+ ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.817
+ ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.867
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.559
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.560
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.765
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.772
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.777
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.789
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.791
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.780
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.790
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.793
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.797
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.801
+ ___133-[PBFPosterGalleryDataProvider fetchComplicationPreviewImagesForPreview:complicationSnapshotReceivedHandler:errorHandler:completion:]_block_invoke_3
+ ___133-[PBFPosterGalleryDataProvider fetchComplicationPreviewImagesForPreview:complicationSnapshotReceivedHandler:errorHandler:completion:]_block_invoke_3.cold.1
+ ___155-[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]_block_invoke.552
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.935
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.936
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.943
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.944.cold.1
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.948
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.953
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.963
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.949
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.954
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.965
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.950
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.958
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.966
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.959
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.970
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.971
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.897
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.899
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.847
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.847.cold.1
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.850
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.857
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.858
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.860
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.859
+ ___38-[PBFComplicationSnapshotService init]_block_invoke
+ ___43-[PBFPosterSnapshotCoordinator cacheFuture]_block_invoke
+ ___43-[PBFPosterSnapshotCoordinator cacheFuture]_block_invoke_2
+ ___43-[PBFPosterSnapshotCoordinator cacheFuture]_block_invoke_3
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke.110
+ ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke_6
+ ___58-[PBFComplicationSnapshotter _startAttempt:previousError:]_block_invoke
+ ___58-[PBFComplicationSnapshotter _startAttempt:previousError:]_block_invoke.47
+ ___58-[PBFComplicationSnapshotter _startAttempt:previousError:]_block_invoke_2
+ ___66-[PBFFocusPosterSelectionViewController _reloadDataWithAnimation:]_block_invoke.201
+ ___70-[PBFComplicationSnapshotter _main_kickoffHostViewController:attempt:]_block_invoke
+ ___70-[PBFComplicationSnapshotter _main_kickoffHostViewController:attempt:]_block_invoke_2
+ ___72-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_fixComplicationLayout]_block_invoke
+ ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.668
+ ___78-[PBFPosterSnapshotManager _lock_teardownAssertionsAndSnapshottersIfNecessary]_block_invoke_2.cold.1
+ ___78-[PBFPosterSnapshotManager _lock_teardownAssertionsAndSnapshottersIfNecessary]_block_invoke_2.cold.2
+ ___79-[PBFPosterAssetViewController _updateSnapshotBundleRequestsForDisplayContexts]_block_invoke
+ ___80-[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:trimCache:]_block_invoke
+ ___80-[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:trimCache:]_block_invoke_2
+ ___80-[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:trimCache:]_block_invoke_3
+ ___84-[PBFPosterAssetViewController _updateSnapshotBundleRequestsForActiveDisplayContext]_block_invoke
+ ___84-[PBFPosterAssetViewController _updateSnapshotBundleRequestsForActiveDisplayContext]_block_invoke_2
+ ___90-[PBFPosterGalleryPreviewComplicationContentView prepareComplicationPreviewWithGenerator:]_block_invoke_5
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.302
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.312
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.306
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.313
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.311
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.311.cold.1
+ ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.697
+ ___Block_byref_object_copy_.275
+ ___Block_byref_object_copy_.848
+ ___Block_byref_object_dispose_.276
+ ___Block_byref_object_dispose_.849
+ ___block_descriptor_32_e40_16?0"PBFComplicationSnapshotRequest"8l
+ ___block_descriptor_40_e8_32w_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40s_e56_{?={?=QQQQ}{?=QQQQ}{?=QQQQ}}16?0"<PBFDisplayContext>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e29_v24?0"UIImage"8"NSError"16ls40l8s32l8s48l8
+ ___block_descriptor_56_e8_32s40r_e55_v32?0"PBFPosterSnapshotRequest"8"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"UIImage"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e18_v16?0"INIntent"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e34_v16?0"PBFPosterSnapshotRequest"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e29_v24?0"UIImage"8"NSError"16ls32l8w40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e47_v24?0"PRSPosterSnapshotResponse"8"NSError"16ls32l8s48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
+ ___block_literal_global.122
+ ___block_literal_global.133
+ ___block_literal_global.147
+ ___block_literal_global.149
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.174
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.275
+ ___block_literal_global.286
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.349
+ ___block_literal_global.383
+ ___block_literal_global.389
+ ___block_literal_global.434
+ ___block_literal_global.443
+ ___block_literal_global.454
+ ___block_literal_global.455
+ ___block_literal_global.467
+ ___block_literal_global.47
+ ___block_literal_global.487
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.620
+ ___block_literal_global.651
+ ___block_literal_global.678
+ ___block_literal_global.680
+ ___block_literal_global.748
+ ___block_literal_global.753
+ ___block_literal_global.764
+ ___block_literal_global.774
+ ___block_literal_global.779
+ ___block_literal_global.880
+ ___block_literal_global.896
+ ___block_literal_global.914
+ ___block_literal_global.939
+ ___block_literal_global.96
+ _block_copy_helper.104
+ _block_copy_helper.114
+ _block_copy_helper.120
+ _block_copy_helper.157
+ _block_copy_helper.164
+ _block_copy_helper.171
+ _block_copy_helper.394
+ _block_copy_helper.398
+ _block_copy_helper.405
+ _block_copy_helper.414
+ _block_copy_helper.421
+ _block_copy_helper.425
+ _block_copy_helper.429
+ _block_copy_helper.433
+ _block_copy_helper.437
+ _block_copy_helper.441
+ _block_copy_helper.445
+ _block_copy_helper.451
+ _block_copy_helper.472
+ _block_copy_helper.479
+ _block_copy_helper.486
+ _block_copy_helper.493
+ _block_copy_helper.500
+ _block_copy_helper.508
+ _block_copy_helper.539
+ _block_copy_helper.549
+ _block_copy_helper.555
+ _block_copy_helper.561
+ _block_copy_helper.568
+ _block_copy_helper.575
+ _block_copy_helper.582
+ _block_copy_helper.589
+ _block_copy_helper.59
+ _block_copy_helper.596
+ _block_copy_helper.600
+ _block_copy_helper.622
+ _block_copy_helper.632
+ _block_copy_helper.638
+ _block_copy_helper.645
+ _block_copy_helper.65
+ _block_copy_helper.652
+ _block_copy_helper.661
+ _block_copy_helper.667
+ _block_copy_helper.673
+ _block_copy_helper.71
+ _block_copy_helper.714
+ _block_copy_helper.77
+ _block_copy_helper.94
+ _block_descriptor.106
+ _block_descriptor.116
+ _block_descriptor.122
+ _block_descriptor.159
+ _block_descriptor.166
+ _block_descriptor.173
+ _block_descriptor.396
+ _block_descriptor.400
+ _block_descriptor.407
+ _block_descriptor.416
+ _block_descriptor.423
+ _block_descriptor.427
+ _block_descriptor.431
+ _block_descriptor.435
+ _block_descriptor.439
+ _block_descriptor.443
+ _block_descriptor.447
+ _block_descriptor.453
+ _block_descriptor.474
+ _block_descriptor.481
+ _block_descriptor.488
+ _block_descriptor.495
+ _block_descriptor.502
+ _block_descriptor.510
+ _block_descriptor.541
+ _block_descriptor.551
+ _block_descriptor.557
+ _block_descriptor.563
+ _block_descriptor.570
+ _block_descriptor.577
+ _block_descriptor.584
+ _block_descriptor.591
+ _block_descriptor.598
+ _block_descriptor.602
+ _block_descriptor.61
+ _block_descriptor.624
+ _block_descriptor.634
+ _block_descriptor.640
+ _block_descriptor.647
+ _block_descriptor.654
+ _block_descriptor.663
+ _block_descriptor.669
+ _block_descriptor.67
+ _block_descriptor.675
+ _block_descriptor.716
+ _block_descriptor.73
+ _block_descriptor.79
+ _block_descriptor.96
+ _block_destroy_helper.105
+ _block_destroy_helper.115
+ _block_destroy_helper.121
+ _block_destroy_helper.158
+ _block_destroy_helper.165
+ _block_destroy_helper.172
+ _block_destroy_helper.395
+ _block_destroy_helper.399
+ _block_destroy_helper.406
+ _block_destroy_helper.415
+ _block_destroy_helper.422
+ _block_destroy_helper.426
+ _block_destroy_helper.430
+ _block_destroy_helper.434
+ _block_destroy_helper.438
+ _block_destroy_helper.442
+ _block_destroy_helper.446
+ _block_destroy_helper.452
+ _block_destroy_helper.473
+ _block_destroy_helper.480
+ _block_destroy_helper.487
+ _block_destroy_helper.494
+ _block_destroy_helper.501
+ _block_destroy_helper.509
+ _block_destroy_helper.540
+ _block_destroy_helper.550
+ _block_destroy_helper.556
+ _block_destroy_helper.562
+ _block_destroy_helper.569
+ _block_destroy_helper.576
+ _block_destroy_helper.583
+ _block_destroy_helper.590
+ _block_destroy_helper.597
+ _block_destroy_helper.60
+ _block_destroy_helper.601
+ _block_destroy_helper.623
+ _block_destroy_helper.633
+ _block_destroy_helper.639
+ _block_destroy_helper.646
+ _block_destroy_helper.653
+ _block_destroy_helper.66
+ _block_destroy_helper.662
+ _block_destroy_helper.668
+ _block_destroy_helper.674
+ _block_destroy_helper.715
+ _block_destroy_helper.72
+ _block_destroy_helper.78
+ _block_destroy_helper.95
+ _init.complicationSnapshotServiceDefaultImageCache
+ _init.onceToken
+ _objc_getAssociatedObject
+ _objc_msgSend$_buildAndExecuteComplicationSnapshotterForRequest:
+ _objc_msgSend$_invalidateAllHistogramCache
+ _objc_msgSend$_invalidateHistogramCacheForPosterPreview:
+ _objc_msgSend$_lock_cleanupAfterRequest:shouldTerminateProcess:
+ _objc_msgSend$_lock_fixComplicationLayout
+ _objc_msgSend$_lock_trimCachedSnapshotsToRequests:trimCache:
+ _objc_msgSend$_main_kickoffHostViewController:attempt:
+ _objc_msgSend$_startAttempt:previousError:
+ _objc_msgSend$_toWindowOrientation
+ _objc_msgSend$_updateHistogramCacheIfNeeded
+ _objc_msgSend$_updateSnapshotBundleRequestsForActiveDisplayContext
+ _objc_msgSend$addSuccessBlock:scheduler:
+ _objc_msgSend$applicationStateMonitor
+ _objc_msgSend$cacheIdentifier
+ _objc_msgSend$complicationSnapshotRequests
+ _objc_msgSend$destinationForSQLiteCacheAtURL:clientAuditToken:error:
+ _objc_msgSend$getValue:size:
+ _objc_msgSend$imageForKey:
+ _objc_msgSend$isForeground
+ _objc_msgSend$pf_UUIDFromArbitraryString:
+ _objc_msgSend$pf_sha256Hash
+ _objc_msgSend$pui_imageHasNoContent
+ _objc_msgSend$removeImageForKey:
+ _objc_msgSend$setComplicationLayout:
+ _objc_msgSend$setComplicationsUseBottomLayout:
+ _objc_msgSend$setDisplayContext:animationSettings:fence:
+ _objc_msgSend$setEditingExtensionInstance:
+ _objc_msgSend$setImage:forKey:
+ _objc_msgSend$setVisibility:
+ _objc_msgSend$terminateWithExplanation:error:
+ _objc_msgSend$trimCachedSnapshotsToRequests:
+ _objc_msgSend$trimComplicationsCache
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_setAssociatedObject
+ _objectdestroy.155Tm
+ _objectdestroy.162Tm
+ _objectdestroy.392Tm
+ _objectdestroy.69Tm
+ _objectdestroy.705Tm
+ _objectdestroy.86Tm
+ _symbolic _____Sg 5UIKit23_UILiquidMorphAnimationC
- -[PBFComplicationSnapshotService _lock_appendReceivedBlock:errorBlock:forRequest:]
- -[PBFComplicationSnapshotService _lock_preparedComplicationSnapshotForRequest:]
- -[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:]
- -[PBFComplicationSnapshotService complicationSnapshotForRequest:]
- -[PBFComplicationSnapshotter _main_kickoffHostViewController:]
- -[PBFComplicationSnapshotter _main_kickoffHostViewController:].cold.1
- -[PBFComplicationSnapshotter _main_kickoffHostViewController:].cold.2
- -[PBFComplicationSnapshotterOperation attempt]
- -[PBFComplicationSnapshotterOperation maxNumberOfAttempts]
- -[PBFComplicationSnapshotterOperation setAttempt:]
- -[PBFComplicationSnapshotterOperation setMaxNumberOfAttempts:]
- -[PBFPosterGalleryPreviewViewController presentConfiguratorForPreview:fromView:]
- -[PBFPosterGalleryPreviewViewController presentRendererForPreview:fromView:]
- -[PBFPosterSnapshotCoordinator _lock_cacheFuture]
- -[PBFPosterSnapshotManager _lock_cleanupAfterRequest:]
- -[PBFPosterSnapshotManager _setupMemoryPressureTracking]
- GCC_except_table11
- GCC_except_table116
- GCC_except_table117
- GCC_except_table136
- GCC_except_table137
- GCC_except_table138
- GCC_except_table38
- GCC_except_table44
- GCC_except_table463
- GCC_except_table484
- GCC_except_table522
- GCC_except_table525
- GCC_except_table54
- _OBJC_IVAR_$_PBFComplicationSnapshotService._lock_requestToResult
- _OBJC_IVAR_$_PBFComplicationSnapshotService._lock_requestToSnapshotErrorHandlers
- _OBJC_IVAR_$_PBFComplicationSnapshotService._lock_requestToSnapshotReceivedHandlers
- _OBJC_IVAR_$_PBFComplicationSnapshotterOperation._attempt
- _OBJC_IVAR_$_PBFComplicationSnapshotterOperation._maxNumberOfAttempts
- _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_maxNumberOfRunningSnapshotters
- __OBJC_$_PROP_LIST_PBFPosterSnapshotContext.242
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.881
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.887
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.883
- ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.614
- ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.623
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.341
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.342
- ___111-[PBFFocusPosterSelectionViewController initWithActivityUUID:activityIdentifier:galleryDataProvider:dataStore:]_block_invoke.134
- ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.644
- ___113-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_performNecessaryMigrationsForDataStoreAtURL:shouldForce:error:]_block_invoke.165
- ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.813
- ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.863
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.555
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.556
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.757
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.768
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.773
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.785
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.787
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.776
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.786
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.789
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.793
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.797
- ___133-[PBFPosterGalleryDataProvider fetchComplicationPreviewImagesForPreview:complicationSnapshotReceivedHandler:errorHandler:completion:]_block_invoke_2.cold.1
- ___155-[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]_block_invoke.548
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.931
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.932
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.939
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.940
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.940.cold.1
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.949
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.959
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.945
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.950
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.961
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.946
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.954
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.962
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.955
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.966
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.967
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.893
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.895
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.843
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.843.cold.1
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.846
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.853
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.854
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.856
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.855
- ___35-[PBFComplicationSnapshotter start]_block_invoke
- ___35-[PBFComplicationSnapshotter start]_block_invoke.9
- ___35-[PBFComplicationSnapshotter start]_block_invoke_2
- ___49-[PBFPosterSnapshotCoordinator _lock_cacheFuture]_block_invoke
- ___49-[PBFPosterSnapshotCoordinator _lock_cacheFuture]_block_invoke_2
- ___49-[PBFPosterSnapshotCoordinator _lock_cacheFuture]_block_invoke_3
- ___54-[PBFPosterSnapshotManager _lock_kickoffNextOperation]_block_invoke.108
- ___62-[PBFComplicationSnapshotter _main_kickoffHostViewController:]_block_invoke
- ___66-[PBFFocusPosterSelectionViewController _reloadDataWithAnimation:]_block_invoke.193
- ___70-[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:]_block_invoke
- ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.664
- ___82-[PBFComplicationSnapshotService _lock_appendReceivedBlock:errorBlock:forRequest:]_block_invoke
- ___82-[PBFComplicationSnapshotService _lock_appendReceivedBlock:errorBlock:forRequest:]_block_invoke_2
- ___83-[PBFComplicationSnapshotService _fireCompletionHandlersForRequest:snapshot:error:]_block_invoke
- ___83-[PBFComplicationSnapshotService _fireCompletionHandlersForRequest:snapshot:error:]_block_invoke_2
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.298
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.308
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.302
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.309
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.307
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_3.307.cold.1
- ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.693
- ___Block_byref_object_copy_.271
- ___Block_byref_object_copy_.844
- ___Block_byref_object_dispose_.272
- ___Block_byref_object_dispose_.845
- ___block_descriptor_40_e8_32s_e45_B16?0"PBFComplicationSnapshotterOperation"8ls32l8
- ___block_descriptor_40_e8_32s_e56_{?={?=QQQQ}{?=QQQQ}{?=QQQQ}}16?0"<PBFDisplayContext>"8ls32l8
- ___block_descriptor_48_e8_32s40s_e18_v16?0"INIntent"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e34_v16?0"PBFPosterSnapshotRequest"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e29_v24?0"UIImage"8"NSError"16ls32l8w40l8
- ___block_descriptor_48_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e47_v24?0"PRSPosterSnapshotResponse"8"NSError"16ls32l8s40l8r48l8
- ___block_literal_global.120
- ___block_literal_global.137
- ___block_literal_global.139
- ___block_literal_global.141
- ___block_literal_global.150
- ___block_literal_global.164
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.256
- ___block_literal_global.257
- ___block_literal_global.259
- ___block_literal_global.270
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.345
- ___block_literal_global.379
- ___block_literal_global.380
- ___block_literal_global.425
- ___block_literal_global.439
- ___block_literal_global.442
- ___block_literal_global.450
- ___block_literal_global.463
- ___block_literal_global.48
- ___block_literal_global.483
- ___block_literal_global.611
- ___block_literal_global.613
- ___block_literal_global.616
- ___block_literal_global.647
- ___block_literal_global.672
- ___block_literal_global.674
- ___block_literal_global.744
- ___block_literal_global.749
- ___block_literal_global.760
- ___block_literal_global.770
- ___block_literal_global.775
- ___block_literal_global.876
- ___block_literal_global.892
- ___block_literal_global.910
- ___block_literal_global.935
- _block_copy_helper.103
- _block_copy_helper.113
- _block_copy_helper.126
- _block_copy_helper.132
- _block_copy_helper.138
- _block_copy_helper.144
- _block_copy_helper.150
- _block_copy_helper.156
- _block_copy_helper.163
- _block_copy_helper.170
- _block_copy_helper.391
- _block_copy_helper.395
- _block_copy_helper.402
- _block_copy_helper.411
- _block_copy_helper.418
- _block_copy_helper.422
- _block_copy_helper.426
- _block_copy_helper.430
- _block_copy_helper.434
- _block_copy_helper.438
- _block_copy_helper.442
- _block_copy_helper.448
- _block_copy_helper.469
- _block_copy_helper.476
- _block_copy_helper.483
- _block_copy_helper.490
- _block_copy_helper.497
- _block_copy_helper.505
- _block_copy_helper.536
- _block_copy_helper.546
- _block_copy_helper.552
- _block_copy_helper.558
- _block_copy_helper.565
- _block_copy_helper.572
- _block_copy_helper.579
- _block_copy_helper.586
- _block_copy_helper.593
- _block_copy_helper.597
- _block_copy_helper.613
- _block_copy_helper.629
- _block_copy_helper.635
- _block_copy_helper.642
- _block_copy_helper.649
- _block_copy_helper.658
- _block_copy_helper.664
- _block_copy_helper.670
- _block_copy_helper.70
- _block_copy_helper.711
- _block_copy_helper.76
- _block_copy_helper.93
- _block_descriptor.105
- _block_descriptor.115
- _block_descriptor.128
- _block_descriptor.134
- _block_descriptor.140
- _block_descriptor.146
- _block_descriptor.152
- _block_descriptor.158
- _block_descriptor.165
- _block_descriptor.172
- _block_descriptor.393
- _block_descriptor.397
- _block_descriptor.404
- _block_descriptor.413
- _block_descriptor.420
- _block_descriptor.424
- _block_descriptor.428
- _block_descriptor.432
- _block_descriptor.436
- _block_descriptor.440
- _block_descriptor.444
- _block_descriptor.450
- _block_descriptor.471
- _block_descriptor.478
- _block_descriptor.485
- _block_descriptor.492
- _block_descriptor.499
- _block_descriptor.507
- _block_descriptor.538
- _block_descriptor.548
- _block_descriptor.554
- _block_descriptor.560
- _block_descriptor.567
- _block_descriptor.574
- _block_descriptor.581
- _block_descriptor.588
- _block_descriptor.595
- _block_descriptor.599
- _block_descriptor.615
- _block_descriptor.631
- _block_descriptor.637
- _block_descriptor.644
- _block_descriptor.651
- _block_descriptor.660
- _block_descriptor.666
- _block_descriptor.672
- _block_descriptor.713
- _block_descriptor.72
- _block_descriptor.78
- _block_descriptor.95
- _block_destroy_helper.104
- _block_destroy_helper.114
- _block_destroy_helper.127
- _block_destroy_helper.133
- _block_destroy_helper.139
- _block_destroy_helper.145
- _block_destroy_helper.151
- _block_destroy_helper.157
- _block_destroy_helper.164
- _block_destroy_helper.171
- _block_destroy_helper.392
- _block_destroy_helper.396
- _block_destroy_helper.403
- _block_destroy_helper.412
- _block_destroy_helper.419
- _block_destroy_helper.423
- _block_destroy_helper.427
- _block_destroy_helper.431
- _block_destroy_helper.435
- _block_destroy_helper.439
- _block_destroy_helper.443
- _block_destroy_helper.449
- _block_destroy_helper.470
- _block_destroy_helper.477
- _block_destroy_helper.484
- _block_destroy_helper.491
- _block_destroy_helper.498
- _block_destroy_helper.506
- _block_destroy_helper.537
- _block_destroy_helper.547
- _block_destroy_helper.553
- _block_destroy_helper.559
- _block_destroy_helper.566
- _block_destroy_helper.573
- _block_destroy_helper.580
- _block_destroy_helper.587
- _block_destroy_helper.594
- _block_destroy_helper.598
- _block_destroy_helper.614
- _block_destroy_helper.630
- _block_destroy_helper.636
- _block_destroy_helper.643
- _block_destroy_helper.650
- _block_destroy_helper.659
- _block_destroy_helper.665
- _block_destroy_helper.671
- _block_destroy_helper.71
- _block_destroy_helper.712
- _block_destroy_helper.77
- _block_destroy_helper.94
- _objc_msgSend$_lock_appendReceivedBlock:errorBlock:forRequest:
- _objc_msgSend$_lock_cacheFuture
- _objc_msgSend$_lock_cleanupAfterRequest:
- _objc_msgSend$_lock_preparedComplicationSnapshotForRequest:
- _objc_msgSend$_lock_trimCachedSnapshotsToRequests:
- _objc_msgSend$_main_kickoffHostViewController:
- _objc_msgSend$_setupMemoryPressureTracking
- _objc_msgSend$appendInteger:withName:
- _objc_msgSend$attempt
- _objc_msgSend$destinationForCache:clientAuditToken:error:
- _objc_msgSend$initWithProvider:contents:configurableOptions:
- _objectdestroy.154Tm
- _objectdestroy.161Tm
- _objectdestroy.389Tm
- _objectdestroy.702Tm
- _objectdestroy.74Tm
- _objectdestroy.85Tm
CStrings:
+ "$__lazy_storage_$_morphAnimation"
+ "%@-%@-%@-%lld-%lu"
+ "%@-%lu"
+ "(%p) _updateHydrationStateIfNeeded; staying in %{public}@ due to ongoing BACKGROUND active display context hydration"
+ "(%p) _updateHydrationStateIfNeeded; staying in %{public}@ due to ongoing active display context hydration"
+ "(%{public}@) Starting complication snapshotter attempt %lu"
+ "@\"BSUIMappedImageCache\""
+ "@16@?0@\"PBFComplicationSnapshotRequest\"8"
+ "Aegir Config needs fixing for complicationsUseBottomLayout = YES UUID:%@"
+ "BACKGROUND"
+ "Checking current locale: %{public}@ vs stashed locale: %{public}@"
+ "Client Snapshot"
+ "Complication migration error creating new version of configuration: %@"
+ "Complication migration error storing updated configuredProperties: %@"
+ "ComplicationSnapshotServiceDefaultCache"
+ "FOREGROUND"
+ "Focus Poster Selection View Controller"
+ "LuckComplicationMigrationCompleted"
+ "PBFPosterGalleryAssetHydrationStateBackgroundHydration"
+ "PBFPosterGalleryAssetHydrationStateForegroundHydration"
+ "Post complication location migration"
+ "PosterGalleryEditing"
+ "Running complication location migration to fix configurations that have invalid bottom complications: %@"
+ "T@\"NSString\",R,C,N,V_cacheIdentifier"
+ "T@\"PBFApplicationStateMonitor\",R,N,V_applicationStateMonitor"
+ "T@\"PFPosterExtensionInstance\",&,N,V_editingExtensionInstance"
+ "We have no gallery and no stashed locale identifier; Treating locale as unchanged"
+ "_UIMorphable"
+ "_buildAndExecuteComplicationSnapshotterForRequest:"
+ "_cacheIdentifier"
+ "_complicationImageCache"
+ "_displayContextHistogramCache"
+ "_editingExtensionInstance"
+ "_editingPresentationState"
+ "_invalidateAllHistogramCache"
+ "_invalidateHistogramCacheForPosterPreview:"
+ "_lock_cleanupAfterRequest:shouldTerminateProcess:"
+ "_lock_finishedRequestToFuture"
+ "_lock_fixComplicationLayout"
+ "_lock_inflightRequestToFuture"
+ "_lock_preventKickCount"
+ "_lock_trimCachedSnapshotsToRequests:trimCache:"
+ "_main_kickoffHostViewController:attempt:"
+ "_previewsRequiringHistogramCacheInvalidation"
+ "_startAttempt:previousError:"
+ "_toWindowOrientation"
+ "_updateHistogramCacheIfNeeded"
+ "_updateSnapshotBundleRequestsForActiveDisplayContext"
+ "cacheIdentifier"
+ "chrono generated a snapshot with no content"
+ "com.apple.NanoUniverse.AegirProxyApp.AegirPoster"
+ "destinationForSQLiteCacheAtURL:clientAuditToken:error:"
+ "editingExtensionInstance"
+ "exceeded max retry"
+ "failed to terminate snapshot instance with error: %{public}@"
+ "getValue:size:"
+ "hasTriedBeforeKey"
+ "imageForKey:"
+ "isForeground"
+ "outstanding active display context BACKGROUND hydration; transitioning back to initial hydration state to finish those up"
+ "pf_UUIDFromArbitraryString:"
+ "pf_sha256Hash"
+ "prefersFlatImageLayers"
+ "process failed to complete snapshot"
+ "pui_imageHasNoContent"
+ "removeImageForKey:"
+ "setComplicationLayout:"
+ "setComplicationsUseBottomLayout:"
+ "setDisplayContext:animationSettings:fence:"
+ "setEditingExtensionInstance:"
+ "setImage:forKey:"
+ "setPrefersFlatImageLayers:"
+ "snapshot manager operating %{public}@; %lu max snapshotters w/ %lu max snapshotters per provider w/ queue currently of %lu and %lu active snapshotters"
+ "spinning up snapshot manager assertions..."
+ "successfully terminated snapshot process instance following error"
+ "tearing down snapshot manager assertions..."
+ "terminateWithExplanation:error:"
+ "terminating for gallery reuse"
+ "trimComplicationsCache"
+ "v32@0:8Q16@24"
+ "v32@?0@\"PBFPosterSnapshotRequest\"8@\"NSDictionary\"16^B24"
+ "valueWithBytes:objCType:"
+ "{?={?=QQQQ}{?=QQQQ}{?=QQQQ}}"
+ "\xf01"
+ "\xf0\xf0\xf0B"
- "\f!"
- "(%{public}@) Starting complication snapshotter"
- "B16@?0@\"PBFComplicationSnapshotterOperation\"8"
- "PBFPosterGalleryAssetHydrationStateInitialHydration"
- "Tq,N,V_attempt"
- "Tq,N,V_maxNumberOfAttempts"
- "_attempt"
- "_lock_appendReceivedBlock:errorBlock:forRequest:"
- "_lock_cacheFuture"
- "_lock_cleanupAfterRequest:"
- "_lock_maxNumberOfRunningSnapshotters"
- "_lock_preparedComplicationSnapshotForRequest:"
- "_lock_requestToResult"
- "_lock_requestToSnapshotErrorHandlers"
- "_lock_requestToSnapshotReceivedHandlers"
- "_lock_trimCachedSnapshotsToRequests:"
- "_main_kickoffHostViewController:"
- "_maxNumberOfAttempts"
- "_setupMemoryPressureTracking"
- "appendInteger:withName:"
- "attempt"
- "cannot present configurator for preview %@ due to invalid lookup info : path=%@ processIdentity=%@"
- "cannot present renderer for preview %@ due to invalid lookup info : path=%@ processIdentity=%@"
- "complicationSnapshotForRequest:"
- "destinationForCache:clientAuditToken:error:"
- "maxNumberOfAttempts"
- "presentConfiguratorForPreview:fromView:"
- "presentRendererForPreview:fromView:"
- "setAttempt:"
- "setMaxNumberOfAttempts:"
- "\xf0!"
- "\xf0\xf0\xf02"

```
