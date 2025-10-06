## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-140.39.0.0.0
-  __TEXT.__text: 0x1a6618
-  __TEXT.__auth_stubs: 0x2a90
-  __TEXT.__objc_methlist: 0xa604
+140.120.0.0.0
+  __TEXT.__text: 0x1a9a10
+  __TEXT.__auth_stubs: 0x2ab0
+  __TEXT.__objc_methlist: 0xa62c
   __TEXT.__const: 0x2184
-  __TEXT.__gcc_except_tab: 0x28f4
-  __TEXT.__cstring: 0x15f9b
-  __TEXT.__oslogstring: 0x120ea
+  __TEXT.__gcc_except_tab: 0x3050
+  __TEXT.__cstring: 0x1634b
+  __TEXT.__oslogstring: 0x1225a
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
-  __TEXT.__swift5_typeref: 0x1e2e
+  __TEXT.__swift5_typeref: 0x1e5e
   __TEXT.__constg_swiftt: 0x36b4
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x271b

   __TEXT.__swift5_types: 0x10c
   __TEXT.__swift5_capture: 0x1160
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x5504
-  __TEXT.__eh_frame: 0x8d8
-  __TEXT.__objc_classname: 0x22f7
-  __TEXT.__objc_methname: 0x28d6d
-  __TEXT.__objc_methtype: 0x84dd
-  __TEXT.__objc_stubs: 0x171c0
+  __TEXT.__unwind_info: 0x5584
+  __TEXT.__eh_frame: 0x8f8
+  __TEXT.__objc_classname: 0x23b4
+  __TEXT.__objc_methname: 0x28e47
+  __TEXT.__objc_methtype: 0x85a8
+  __TEXT.__objc_stubs: 0x17220
   __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x4660
-  __DATA_CONST.__objc_classlist: 0x660
+  __DATA_CONST.__const: 0x47a8
+  __DATA_CONST.__objc_classlist: 0x668
   __DATA_CONST.__objc_catlist: 0x118
-  __DATA_CONST.__objc_protolist: 0x530
+  __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2d248
-  __DATA_CONST.__objc_selrefs: 0x76d8
+  __DATA_CONST.__objc_const: 0x2d508
+  __DATA_CONST.__objc_selrefs: 0x76e8
+  __DATA_CONST.__objc_protorefs: 0x1f8
+  __DATA_CONST.__objc_classrefs: 0xda0
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__cfstring: 0xa8e0
+  __AUTH_CONST.__cfstring: 0xa900
   __AUTH_CONST.__objc_const: 0x4308
-  __AUTH_CONST.__const: 0x5f00
+  __AUTH_CONST.__const: 0x5f40
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1558
-  __AUTH.__objc_data: 0x3390
-  __AUTH.__data: 0x7d8
-  __DATA.__objc_protorefs: 0x1f8
-  __DATA.__objc_classrefs: 0xd98
-  __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0xf4c
+  __AUTH_CONST.__auth_got: 0x1568
+  __AUTH.__objc_data: 0x2408
+  __AUTH.__data: 0x4b0
+  __DATA.__objc_ivar: 0xf60
   __DATA.__objc_data: 0x150
-  __DATA.__data: 0x3f80
-  __DATA.__bss: 0x12e0
-  __DATA.__common: 0xc8
-  __DATA_DIRTY.__objc_data: 0x4c88
-  __DATA_DIRTY.__data: 0x4a8
+  __DATA.__data: 0x3b70
+  __DATA.__bss: 0x1010
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x5c60
+  __DATA_DIRTY.__data: 0xed0
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x3d8
-  __DATA_DIRTY.__common: 0x20
+  __DATA_DIRTY.__bss: 0x6c8
+  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ADD6DB42-9712-3266-99D2-C2D8DC5C8958
-  Functions: 7830
-  Symbols:   20054
-  CStrings:  11379
+  UUID: 6FD12013-2E26-32E5-B1D2-2E5ADE8621C2
+  Functions: 7856
+  Symbols:   20124
+  CStrings:  11433
 
Symbols:
+ -[PBFComplicationSnapshotService _lock_trimCachedSnapshotsToRequests:]
+ -[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]
+ -[PBFPosterExtensionDataStore assertionManager:identityIsNowMarkedAsInUse:]
+ -[PBFPosterExtensionDataStore assertionManager:identityIsNowMarkedAsNOTInUse:]
+ -[PBFPosterExtensionDataStore assertionManager:identityIsNowMarkedAsNOTInUse:].cold.1
+ -[PBFPosterExtensionDataStoreAssertionManager _notifyObserversOfNewAssertions:newlyNotInUseAssertions:]
+ -[PBFPosterExtensionDataStoreAssertionManager _notifyObserversOfUpdatedController:]
+ -[PBFPosterExtensionDataStoreAssertionManager executeTransaction:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _localeDidChange:].cold.1
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _localeDidChange:].cold.2
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _mutateDataStoreState:error:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _postDidTearDownNotification]
+ -[PBFPosterGalleryPreviewViewController forwardAppearanceNotificationName:]
+ -[PBFPosterRoleCoordinator finalizeChangesWithChangeHandler:outEvents:error:].cold.3
+ -[PBFPosterRoleCoordinator finalizeChangesWithChangeHandler:outEvents:error:].cold.4
+ -[PBFPosterRoleCoordinator finalizeChangesWithChangeHandler:outEvents:error:].cold.5
+ -[PBFPosterSnapshotManager cancelRequestedSnapshotsForIdentity:]
+ -[PBFPosterSnapshotManager cancelRequestedSnapshotsForIdentity:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController .cxx_destruct]
+ -[_PBFPosterExtensionDataStoreAssertionController _appendAssertion:forIdentity:]
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_appendAssertion:forIdentity:]
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_appendAssertion:forIdentity:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_appendAssertion:forIdentity:].cold.2
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_appendAssertion:forIdentity:].cold.3
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_removeAssertion:forIdentity:]
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_removeAssertion:forIdentity:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_removeAssertion:forIdentity:].cold.2
+ -[_PBFPosterExtensionDataStoreAssertionController _internalLock_removeAssertion:forIdentity:].cold.3
+ -[_PBFPosterExtensionDataStoreAssertionController _numberOfInUseAssertionsForIdentity:]
+ -[_PBFPosterExtensionDataStoreAssertionController _removeAssertion:forIdentity:]
+ -[_PBFPosterExtensionDataStoreAssertionController _removeAssertion:forIdentity:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController _removeAssertion:forIdentity:].cold.2
+ -[_PBFPosterExtensionDataStoreAssertionController acquireInUseAssertionForIdentity:reason:]
+ -[_PBFPosterExtensionDataStoreAssertionController acquireInUseAssertionForIdentity:reason:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController description]
+ -[_PBFPosterExtensionDataStoreAssertionController inUseAssertionsByIdentity]
+ -[_PBFPosterExtensionDataStoreAssertionController inUsePosterPathIdentitiesForReason:]
+ -[_PBFPosterExtensionDataStoreAssertionController initWithController:]
+ -[_PBFPosterExtensionDataStoreAssertionController init]
+ -[_PBFPosterExtensionDataStoreAssertionController invalidateInUseAssertionForIdentity:reason:]
+ -[_PBFPosterExtensionDataStoreAssertionController invalidateInUseAssertionForIdentity:reason:].cold.1
+ -[_PBFPosterExtensionDataStoreAssertionController invalidate]
+ -[_PBFPosterExtensionDataStoreAssertionController numberOfAssertionsForReason:]
+ GCC_except_table110
+ GCC_except_table128
+ GCC_except_table148
+ GCC_except_table193
+ GCC_except_table221
+ GCC_except_table273
+ GCC_except_table308
+ GCC_except_table315
+ GCC_except_table317
+ GCC_except_table335
+ GCC_except_table363
+ GCC_except_table372
+ GCC_except_table381
+ GCC_except_table395
+ GCC_except_table43
+ GCC_except_table53
+ GCC_except_table63
+ GCC_except_table72
+ GCC_except_table96
+ _OBJC_CLASS_$__PBFPosterExtensionDataStoreAssertionController
+ _OBJC_IVAR_$_PBFComplicationSnapshotService._invalidationFlag
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._controller
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._invalidationFlag
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._txFlag
+ _OBJC_IVAR_$_PBFPosterRoleCoordinator._invalidationSignal
+ _OBJC_IVAR_$__PBFPosterExtensionDataStoreAssertionController._internalLock
+ _OBJC_IVAR_$__PBFPosterExtensionDataStoreAssertionController._internalLock_inUseAssertionsByIdentity
+ _OBJC_IVAR_$__PBFPosterExtensionDataStoreAssertionController._internalLock_invalidated
+ _OBJC_METACLASS_$__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_$_INSTANCE_METHODS__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_$_INSTANCE_VARIABLES__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_$_PROP_LIST__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPosterExtensionDataStoreAssertionControlling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPosterExtensionDataStoreAssertionIntrospection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PREditingAppearanceNotificationForwarding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBFPosterExtensionDataStoreAssertionControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBFPosterExtensionDataStoreAssertionIntrospection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PREditingAppearanceNotificationForwarding
+ __OBJC_$_PROTOCOL_REFS_PBFPosterExtensionDataStoreAssertionControlling
+ __OBJC_$_PROTOCOL_REFS_PBFPosterExtensionDataStoreAssertionIntrospection
+ __OBJC_$_PROTOCOL_REFS_PREditingAppearanceNotificationForwarding
+ __OBJC_CLASS_PROTOCOLS_$__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_CLASS_RO_$__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_LABEL_PROTOCOL_$_PBFPosterExtensionDataStoreAssertionControlling
+ __OBJC_LABEL_PROTOCOL_$_PBFPosterExtensionDataStoreAssertionIntrospection
+ __OBJC_LABEL_PROTOCOL_$_PREditingAppearanceNotificationForwarding
+ __OBJC_METACLASS_RO_$__PBFPosterExtensionDataStoreAssertionController
+ __OBJC_PROTOCOL_$_PBFPosterExtensionDataStoreAssertionControlling
+ __OBJC_PROTOCOL_$_PBFPosterExtensionDataStoreAssertionIntrospection
+ __OBJC_PROTOCOL_$_PREditingAppearanceNotificationForwarding
+ ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.656
+ ___103-[PBFPosterExtensionDataStoreAssertionManager _notifyObserversOfNewAssertions:newlyNotInUseAssertions:]_block_invoke
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.350
+ ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.351
+ ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.677
+ ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke.255
+ ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_2.263
+ ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_3.264
+ ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_4.265
+ ___113-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_performNecessaryMigrationsForDataStoreAtURL:shouldForce:error:]_block_invoke.146
+ ___115-[PBFPosterExtensionDataStore _stateLock_setupPathAssertionsAndUpdateActivePosterFromDiff:roleCoordinator:context:]_block_invoke_8
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke.188
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke.193
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.192
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.192.cold.1
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.196
+ ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.196.cold.1
+ ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.849
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.595
+ ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.596
+ ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.219
+ ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.219.cold.1
+ ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.219.cold.2
+ ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.219.cold.3
+ ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.221
+ ___139-[PBFComplicationSnapshotService fetchComplicationSnapshotsForRequests:complicationSnapshotReceivedHandler:errorHandler:completionHandler:]_block_invoke_2
+ ___139-[PBFComplicationSnapshotService fetchComplicationSnapshotsForRequests:complicationSnapshotReceivedHandler:errorHandler:completionHandler:]_block_invoke_3
+ ___139-[PBFComplicationSnapshotService fetchComplicationSnapshotsForRequests:complicationSnapshotReceivedHandler:errorHandler:completionHandler:]_block_invoke_4
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.791
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.795
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.802
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.805
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.819
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.821
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.808
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.820
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.823
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.827
+ ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.831
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.157
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.161
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.164
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.162
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.162.cold.1
+ ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.170
+ ___154-[PBFPosterExtensionDataStore _stateLock_pushUpdateNotificationsForRole:diff:previouslyActiveConfiguration:newActiveConfiguration:options:reason:context:]_block_invoke.691
+ ___155-[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:]_block_invoke
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.945
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.946
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.951
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.952
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.952.cold.1
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.956
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.964
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.975
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.960
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.965
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.977
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.961
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.978
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.979
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.980
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.908
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.910
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.873
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.880
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.881
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.883
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.882
+ ___35-[PBFPosterSnapshotter _main_start]_block_invoke.196
+ ___35-[PBFPosterSnapshotter _main_start]_block_invoke.201
+ ___41-[PBFPosterExtensionDataStore invalidate]_block_invoke_2
+ ___41-[PBFPosterExtensionDataStore invalidate]_block_invoke_3
+ ___44-[PBFComplicationSnapshotService invalidate]_block_invoke_2
+ ___47-[PBFPosterSnapshotter _cleanupWithCompletion:]_block_invoke.231
+ ___49-[PBFGalleryController updateGallery:completion:]_block_invoke.139
+ ___51-[PBFModalRootViewController dataStoreDidTearDown:]_block_invoke.174
+ ___54-[PBFPosterExtensionReloadDescriptorsOperation _setup]_block_invoke.116
+ ___54-[PBFPosterExtensionReloadDescriptorsOperation _setup]_block_invoke.116.cold.1
+ ___56-[PBFPosterExtensionReloadConfigurationOperation _setup]_block_invoke.152
+ ___56-[PBFPosterExtensionReloadConfigurationOperation _setup]_block_invoke.152.cold.1
+ ___58-[PBFPosterRoleProcessor _executeTransaction:block:error:]_block_invoke.147
+ ___58-[PBFPosterRoleProcessor _executeTransaction:block:error:]_block_invoke.147.cold.1
+ ___62-[_PBFPosterExtensionDataStoreAssertionController description]_block_invoke
+ ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.173
+ ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.176
+ ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.178
+ ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.178.cold.1
+ ___66-[PBFPosterSnapshotManager _assertionLock_evaluateInUseAssertions]_block_invoke.173
+ ___66-[PBFPosterSnapshotManager _assertionLock_evaluateInUseAssertions]_block_invoke_2.174
+ ___68-[PBFAmbientRoleCoordinator notifyEventWasReceived:changes:storage:]_block_invoke_2
+ ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.78
+ ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.78.cold.1
+ ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.81
+ ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.243
+ ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.245
+ ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.254
+ ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke_2.246
+ ___75-[PBFPosterGalleryPreviewViewController forwardAppearanceNotificationName:]_block_invoke
+ ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.700
+ ___76-[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl validateDatabaseWithError:]_block_invoke.248
+ ___78-[PBFPosterExtensionDataStore assertionManager:identityIsNowMarkedAsNOTInUse:]_block_invoke
+ ___89-[PBFPosterExtensionDataStore deletePosterDescriptorsForExtensionBundleIdentifier:error:]_block_invoke.250
+ ___91-[PBFPosterExtensionDataStore _stateLock_cleanupStaleSnapshotsNotWithinGallery:completion:]_block_invoke.912
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.302
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.307
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.306
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.306.cold.1
+ ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.308
+ ___91-[_PBFPosterExtensionDataStoreAssertionController acquireInUseAssertionForIdentity:reason:]_block_invoke
+ ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.728
+ ___93-[_PBFPosterExtensionDataStoreAssertionController _internalLock_appendAssertion:forIdentity:]_block_invoke
+ ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.93
+ ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.96
+ ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.98
+ ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.98.cold.1
+ ___Block_byref_object_copy_.165
+ ___Block_byref_object_copy_.272
+ ___Block_byref_object_copy_.871
+ ___Block_byref_object_dispose_.166
+ ___Block_byref_object_dispose_.273
+ ___Block_byref_object_dispose_.872
+ ____PBFPosterRoleCoordinatorSynchronizeAttribute_block_invoke.375
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112s_e59_B16?0"<PBFPosterExtensionDataStoreAssertionControlling>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_32_e26_B16?0"UIViewController"8l
+ ___block_descriptor_32_e27_v16?0"BSSimpleAssertion"8l
+ ___block_descriptor_32_e51_q24?0"PRPosterDescriptor"8"PRPosterDescriptor"16l
+ ___block_descriptor_32_e54_v32?0"NSString"8"<PBFPosterRoleCoordinating>"16^B24l
+ ___block_descriptor_48_e8_32s40bs_e52_v24?0"PBFComplicationSnapshotRequest"8"UIImage"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e31_v16?0"PRPosterConfiguration"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e68_v24?0"PBFPosterExtensionReloadConfigurationOperation"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e52_v24?0"PBFComplicationSnapshotRequest"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e67_v24?0"<PBFPosterExtensionDataStoreAssertionManagerObserver>"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72r_e68_v32?0"PBFPosterConfigurationUpdateResult"8"NSArray"16"NSError"24ls48l8s32l8s40l8r56l8r64l8r72l8
+ ___block_literal_global.102
+ ___block_literal_global.114
+ ___block_literal_global.120
+ ___block_literal_global.127
+ ___block_literal_global.129
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.145
+ ___block_literal_global.175
+ ___block_literal_global.207
+ ___block_literal_global.215
+ ___block_literal_global.230
+ ___block_literal_global.249
+ ___block_literal_global.262
+ ___block_literal_global.265
+ ___block_literal_global.270
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.288
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.381
+ ___block_literal_global.394
+ ___block_literal_global.400
+ ___block_literal_global.501
+ ___block_literal_global.526
+ ___block_literal_global.644
+ ___block_literal_global.646
+ ___block_literal_global.649
+ ___block_literal_global.680
+ ___block_literal_global.708
+ ___block_literal_global.710
+ ___block_literal_global.712
+ ___block_literal_global.737
+ ___block_literal_global.778
+ ___block_literal_global.783
+ ___block_literal_global.794
+ ___block_literal_global.80
+ ___block_literal_global.804
+ ___block_literal_global.807
+ ___block_literal_global.833
+ ___block_literal_global.835
+ ___block_literal_global.84
+ ___block_literal_global.907
+ ___block_literal_global.96
+ ___block_literal_global.99
+ __unnamed_array_storage.189
+ __unnamed_array_storage.780
+ __unnamed_array_storage.785
+ _block_copy_helper.368
+ _block_copy_helper.37
+ _block_copy_helper.372
+ _block_copy_helper.379
+ _block_copy_helper.388
+ _block_copy_helper.395
+ _block_copy_helper.399
+ _block_copy_helper.403
+ _block_copy_helper.407
+ _block_copy_helper.411
+ _block_copy_helper.415
+ _block_copy_helper.419
+ _block_copy_helper.425
+ _block_copy_helper.43
+ _block_copy_helper.446
+ _block_copy_helper.453
+ _block_copy_helper.460
+ _block_copy_helper.467
+ _block_copy_helper.475
+ _block_copy_helper.506
+ _block_copy_helper.516
+ _block_copy_helper.522
+ _block_copy_helper.528
+ _block_copy_helper.535
+ _block_copy_helper.542
+ _block_copy_helper.549
+ _block_copy_helper.55
+ _block_copy_helper.553
+ _block_copy_helper.559
+ _block_copy_helper.575
+ _block_copy_helper.578
+ _block_copy_helper.584
+ _block_copy_helper.591
+ _block_copy_helper.597
+ _block_copy_helper.604
+ _block_copy_helper.61
+ _block_copy_helper.611
+ _block_copy_helper.624
+ _block_copy_helper.630
+ _block_copy_helper.636
+ _block_copy_helper.663
+ _block_descriptor.370
+ _block_descriptor.374
+ _block_descriptor.381
+ _block_descriptor.39
+ _block_descriptor.390
+ _block_descriptor.397
+ _block_descriptor.401
+ _block_descriptor.405
+ _block_descriptor.409
+ _block_descriptor.413
+ _block_descriptor.417
+ _block_descriptor.421
+ _block_descriptor.427
+ _block_descriptor.448
+ _block_descriptor.45
+ _block_descriptor.455
+ _block_descriptor.462
+ _block_descriptor.469
+ _block_descriptor.477
+ _block_descriptor.508
+ _block_descriptor.518
+ _block_descriptor.524
+ _block_descriptor.530
+ _block_descriptor.537
+ _block_descriptor.544
+ _block_descriptor.551
+ _block_descriptor.555
+ _block_descriptor.561
+ _block_descriptor.57
+ _block_descriptor.577
+ _block_descriptor.580
+ _block_descriptor.586
+ _block_descriptor.593
+ _block_descriptor.599
+ _block_descriptor.606
+ _block_descriptor.613
+ _block_descriptor.626
+ _block_descriptor.63
+ _block_descriptor.632
+ _block_descriptor.638
+ _block_descriptor.665
+ _block_destroy_helper.369
+ _block_destroy_helper.373
+ _block_destroy_helper.38
+ _block_destroy_helper.380
+ _block_destroy_helper.389
+ _block_destroy_helper.396
+ _block_destroy_helper.400
+ _block_destroy_helper.404
+ _block_destroy_helper.408
+ _block_destroy_helper.412
+ _block_destroy_helper.416
+ _block_destroy_helper.420
+ _block_destroy_helper.426
+ _block_destroy_helper.44
+ _block_destroy_helper.447
+ _block_destroy_helper.454
+ _block_destroy_helper.461
+ _block_destroy_helper.468
+ _block_destroy_helper.476
+ _block_destroy_helper.507
+ _block_destroy_helper.517
+ _block_destroy_helper.523
+ _block_destroy_helper.529
+ _block_destroy_helper.536
+ _block_destroy_helper.543
+ _block_destroy_helper.550
+ _block_destroy_helper.554
+ _block_destroy_helper.56
+ _block_destroy_helper.560
+ _block_destroy_helper.576
+ _block_destroy_helper.579
+ _block_destroy_helper.585
+ _block_destroy_helper.592
+ _block_destroy_helper.598
+ _block_destroy_helper.605
+ _block_destroy_helper.612
+ _block_destroy_helper.62
+ _block_destroy_helper.625
+ _block_destroy_helper.631
+ _block_destroy_helper.637
+ _block_destroy_helper.664
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.653
+ _objc_msgSend$_appendAssertion:forIdentity:
+ _objc_msgSend$_internalLock_appendAssertion:forIdentity:
+ _objc_msgSend$_internalLock_removeAssertion:forIdentity:
+ _objc_msgSend$_lock_trimCachedSnapshotsToRequests:
+ _objc_msgSend$_mutateDataStoreState:error:
+ _objc_msgSend$_notifyObserversOfNewAssertions:newlyNotInUseAssertions:
+ _objc_msgSend$_notifyObserversOfUpdatedController:
+ _objc_msgSend$_postDidTearDownNotification
+ _objc_msgSend$_stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:
+ _objc_msgSend$acquireInUseAssertionForIdentity:reason:
+ _objc_msgSend$assertionManager:identityIsNowMarkedAsInUse:
+ _objc_msgSend$assertionManager:identityIsNowMarkedAsNOTInUse:
+ _objc_msgSend$cancelRequestedSnapshotsForIdentity:
+ _objc_msgSend$childViewControllers
+ _objc_msgSend$displayOrder
+ _objc_msgSend$executeTransaction:
+ _objc_msgSend$inUseAssertionsByIdentity
+ _objc_msgSend$initWithController:
+ _objc_msgSend$invalidateInUseAssertionForIdentity:reason:
+ _objc_msgSend$orderedSet
+ _objc_msgSend$stablePersistenceIdentifier
+ _symbolic SaySo18ATXFaceGalleryItemCG
+ _symbolic SaySo6UIViewCG
+ _symbolic SaySo9PRSWidgetCG
- +[PBFApplicationStateMonitor sharedInstance]
- -[PBFModalRootViewController _presentedEditingSceneViewController]
- -[PBFPosterExtensionDataStore _stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:error:]
- -[PBFPosterExtensionDataStore assertionManager:pathIsNowMarkedAsNOTInUse:]
- -[PBFPosterExtensionDataStore assertionManager:pathIsNowMarkedAsNOTInUse:].cold.1
- -[PBFPosterExtensionDataStore assertionManager:pathIsNowMarkedInUse:]
- -[PBFPosterExtensionDataStoreAssertionManager _appendAssertion:forServerPosterPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:].cold.1
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:].cold.2
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:].cold.3
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:].cold.4
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:].cold.5
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_numberOfInUseAssertionsForPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:].cold.1
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:].cold.2
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:].cold.3
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:].cold.4
- -[PBFPosterExtensionDataStoreAssertionManager _internalLock_removeAssertion:forServerPosterPath:].cold.5
- -[PBFPosterExtensionDataStoreAssertionManager _invalidateInUseAssertion:forServerPosterPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _numberOfInUseAssertionsForPath:]
- -[PBFPosterExtensionDataStoreAssertionManager _removeAssertion:forServerPosterPath:]
- -[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:]
- -[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:].cold.1
- -[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:].cold.2
- -[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:].cold.3
- -[PBFPosterExtensionDataStoreAssertionManager description]
- -[PBFPosterExtensionDataStoreAssertionManager inUseAssertionForIdentity:reason:]
- -[PBFPosterExtensionDataStoreAssertionManager inUseAssertionForIdentity:reason:].cold.1
- -[PBFPosterExtensionDataStoreAssertionManager inUseAssertionForIdentity:reason:].cold.2
- -[PBFPosterExtensionDataStoreAssertionManager inUseAssertionForIdentity:reason:].cold.3
- -[PBFPosterExtensionDataStoreAssertionManager inUseAssertionForPath:reason:]
- -[PBFPosterExtensionDataStoreAssertionManager isPosterInUse:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue _deleteDataStoreWithCompletion:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue _deleteSnapshots]
- -[PBFPosterExtensionDataStoreXPCServiceGlue _deleteTransientData:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue _teardownDataStoreWithCompletion:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue _triggerMessedUpDataProtectionWithCompletion:]
- -[PBFPosterSnapshotManager cancelRequestedSnapshotsForPath:]
- -[PBFPosterSnapshotManager cancelRequestedSnapshotsForPath:].cold.1
- -[PBFPosterSnapshotManager cancelRequestedSnapshotsForPath:].cold.2
- GCC_except_table108
- GCC_except_table125
- GCC_except_table142
- GCC_except_table189
- GCC_except_table217
- GCC_except_table269
- GCC_except_table304
- GCC_except_table311
- GCC_except_table313
- GCC_except_table331
- GCC_except_table359
- GCC_except_table368
- GCC_except_table377
- GCC_except_table391
- GCC_except_table41
- GCC_except_table51
- GCC_except_table61
- GCC_except_table70
- GCC_except_table94
- _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._internalLock
- _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._internalLock_inUseAssertionsByIdentity
- _OBJC_IVAR_$_PBFPosterExtensionDataStoreAssertionManager._internalLock_invalidated
- __OBJC_$_CLASS_METHODS_PBFApplicationStateMonitor
- ___103-[PBFPosterExtensionDataStore _stateLock_updateDataStoreForSwitcherConfiguration:options:reason:error:]_block_invoke.638
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.346
- ___110-[PBFPosterExtensionDataStore _stateLock_applyUpdatesAndIngestConfiguration:toPath:powerLogReason:completion:]_block_invoke.347
- ___111-[PBFPosterExtensionDataStore _stateLock_executeDataStoreUpdateWithChanges:diffs:options:reason:context:error:]_block_invoke.668
- ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke.253
- ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_2.261
- ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_3.262
- ___112-[PBFPosterRoleCoordinator _ingestIncomingPosterConfiguration:change:currentCollection:storage:outEvents:error:]_block_invoke_4.263
- ___113-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_performNecessaryMigrationsForDataStoreAtURL:shouldForce:error:]_block_invoke.148
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke.187
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke.192
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.191
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.191.cold.1
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.195
- ___116-[PBFGalleryController _stateLock_enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:sessionId:completion:]_block_invoke_2.195.cold.1
- ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.840
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke.586
- ___126-[PBFPosterExtensionDataStore _stateLock_enqueueRefreshPosterConfigurationMatchingUUID:sessionInfo:powerLogReason:completion:]_block_invoke_2.587
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.214
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.214.cold.1
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.214.cold.2
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.214.cold.3
- ___128-[PBFPosterExtensionDataStore executeUpdate:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke.216
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.782
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.786
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.793
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.796
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.810
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.812
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.799
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.811
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.814
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.818
- ___150-[PBFPosterExtensionDataStore _stateLock_updateExtensionsFrom:toExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.822
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.156
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.160
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke.162
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.161
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.161.cold.1
- ___153-[PBFModalRootViewController _standaloneEditingSceneViewController:userDidDismissWithAction:updatedConfiguration:updatedConfiguredProperties:completion:]_block_invoke_2.169
- ___154-[PBFPosterExtensionDataStore _stateLock_pushUpdateNotificationsForRole:diff:previouslyActiveConfiguration:newActiveConfiguration:options:reason:context:]_block_invoke.682
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.936
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.937
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.942
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.943
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.943.cold.1
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.947
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.955
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.966
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.951
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.956
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.968
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.952
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.960
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.961
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.971
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.899
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.901
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.864
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.871
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.872
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.874
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.873
- ___35-[PBFPosterSnapshotter _main_start]_block_invoke.195
- ___35-[PBFPosterSnapshotter _main_start]_block_invoke.200
- ___44+[PBFApplicationStateMonitor sharedInstance]_block_invoke
- ___47-[PBFPosterSnapshotter _cleanupWithCompletion:]_block_invoke.230
- ___49-[PBFGalleryController updateGallery:completion:]_block_invoke.138
- ___51-[PBFModalRootViewController dataStoreDidTearDown:]_block_invoke.173
- ___54-[PBFPosterExtensionReloadDescriptorsOperation _setup]_block_invoke.115
- ___54-[PBFPosterExtensionReloadDescriptorsOperation _setup]_block_invoke.115.cold.1
- ___56-[PBFPosterExtensionReloadConfigurationOperation _setup]_block_invoke.151
- ___56-[PBFPosterExtensionReloadConfigurationOperation _setup]_block_invoke.151.cold.1
- ___58-[PBFPosterExtensionDataStoreAssertionManager description]_block_invoke
- ___58-[PBFPosterRoleProcessor _executeTransaction:block:error:]_block_invoke.146
- ___58-[PBFPosterRoleProcessor _executeTransaction:block:error:]_block_invoke.146.cold.1
- ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.171
- ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.175
- ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.177
- ___66-[PBFGalleryController _stateLock_executeEnqueuedPushToProactive:]_block_invoke.177.cold.1
- ___66-[PBFPosterSnapshotManager _assertionLock_evaluateInUseAssertions]_block_invoke.172
- ___66-[PBFPosterSnapshotManager _assertionLock_evaluateInUseAssertions]_block_invoke_2.173
- ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.80
- ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.80.cold.1
- ___69-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_runLegacyMigration]_block_invoke.83
- ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.242
- ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.244
- ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke.253
- ___72-[PBFPosterSnapshotter _processOutstandingSnapshotDefinitionsWithScene:]_block_invoke_2.245
- ___74-[PBFPosterExtensionDataStore assertionManager:pathIsNowMarkedAsNOTInUse:]_block_invoke
- ___76-[PBFPosterExtensionDataStore _stateLock_processEvents:roles:context:error:]_block_invoke.691
- ___76-[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl validateDatabaseWithError:]_block_invoke.247
- ___78-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_teardownDataStoreWithError:]_block_invoke
- ___83-[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:]_block_invoke
- ___83-[PBFPosterExtensionDataStoreAssertionManager acquireInUseAssertionForPath:reason:]_block_invoke_2
- ___89-[PBFPosterExtensionDataStore deletePosterDescriptorsForExtensionBundleIdentifier:error:]_block_invoke.245
- ___91-[PBFPosterExtensionDataStore _stateLock_cleanupStaleSnapshotsNotWithinGallery:completion:]_block_invoke.903
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.298
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke.303
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.302
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.302.cold.1
- ___91-[PBFPosterExtensionDataStore _stateLock_fetchPosterSnapshotsWithClientRequest:completion:]_block_invoke_2.304
- ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.719
- ___93-[PBFPosterExtensionDataStoreAssertionManager _invalidateInUseAssertion:forServerPosterPath:]_block_invoke
- ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.92
- ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.94
- ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.97
- ___95-[PBFGalleryController enqueueGalleryConfigurationUpdateWithOptions:powerLogReason:completion:]_block_invoke.97.cold.1
- ___97-[PBFPosterExtensionDataStoreAssertionManager _internalLock_appendAssertion:forServerPosterPath:]_block_invoke
- ___Block_byref_object_copy_.164
- ___Block_byref_object_copy_.267
- ___Block_byref_object_copy_.862
- ___Block_byref_object_dispose_.165
- ___Block_byref_object_dispose_.268
- ___Block_byref_object_dispose_.863
- ____PBFPosterRoleCoordinatorSynchronizeAttribute_block_invoke.371
- ___block_descriptor_48_e8_32s40s_e67_v24?0"<PBFPosterExtensionDataStoreAssertionManagerObserver>"8^B16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e68_v32?0"PBFPosterConfigurationUpdateResult"8"NSArray"16"NSError"24ls56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e31_v16?0"PRPosterConfiguration"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.104
- ___block_literal_global.124
- ___block_literal_global.126
- ___block_literal_global.132
- ___block_literal_global.139
- ___block_literal_global.147
- ___block_literal_global.206
- ___block_literal_global.214
- ___block_literal_global.232
- ___block_literal_global.247
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.264
- ___block_literal_global.266
- ___block_literal_global.278
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.350
- ___block_literal_global.372
- ___block_literal_global.379
- ___block_literal_global.399
- ___block_literal_global.491
- ___block_literal_global.516
- ___block_literal_global.635
- ___block_literal_global.637
- ___block_literal_global.640
- ___block_literal_global.672
- ___block_literal_global.699
- ___block_literal_global.701
- ___block_literal_global.703
- ___block_literal_global.728
- ___block_literal_global.769
- ___block_literal_global.774
- ___block_literal_global.785
- ___block_literal_global.79
- ___block_literal_global.795
- ___block_literal_global.798
- ___block_literal_global.82
- ___block_literal_global.824
- ___block_literal_global.826
- ___block_literal_global.86
- ___block_literal_global.898
- ___block_literal_global.98
- __unnamed_array_storage.188
- __unnamed_array_storage.771
- __unnamed_array_storage.776
- _block_copy_helper.369
- _block_copy_helper.373
- _block_copy_helper.380
- _block_copy_helper.389
- _block_copy_helper.396
- _block_copy_helper.400
- _block_copy_helper.404
- _block_copy_helper.408
- _block_copy_helper.412
- _block_copy_helper.416
- _block_copy_helper.420
- _block_copy_helper.426
- _block_copy_helper.447
- _block_copy_helper.454
- _block_copy_helper.461
- _block_copy_helper.468
- _block_copy_helper.476
- _block_copy_helper.507
- _block_copy_helper.517
- _block_copy_helper.523
- _block_copy_helper.529
- _block_copy_helper.536
- _block_copy_helper.543
- _block_copy_helper.550
- _block_copy_helper.554
- _block_copy_helper.560
- _block_copy_helper.576
- _block_copy_helper.579
- _block_copy_helper.585
- _block_copy_helper.592
- _block_copy_helper.598
- _block_copy_helper.605
- _block_copy_helper.612
- _block_copy_helper.625
- _block_copy_helper.631
- _block_copy_helper.637
- _block_copy_helper.664
- _block_descriptor.371
- _block_descriptor.375
- _block_descriptor.382
- _block_descriptor.391
- _block_descriptor.398
- _block_descriptor.402
- _block_descriptor.406
- _block_descriptor.410
- _block_descriptor.414
- _block_descriptor.418
- _block_descriptor.422
- _block_descriptor.428
- _block_descriptor.449
- _block_descriptor.456
- _block_descriptor.463
- _block_descriptor.470
- _block_descriptor.478
- _block_descriptor.509
- _block_descriptor.519
- _block_descriptor.525
- _block_descriptor.531
- _block_descriptor.538
- _block_descriptor.545
- _block_descriptor.552
- _block_descriptor.556
- _block_descriptor.562
- _block_descriptor.578
- _block_descriptor.581
- _block_descriptor.587
- _block_descriptor.594
- _block_descriptor.600
- _block_descriptor.607
- _block_descriptor.614
- _block_descriptor.627
- _block_descriptor.633
- _block_descriptor.639
- _block_descriptor.666
- _block_destroy_helper.370
- _block_destroy_helper.374
- _block_destroy_helper.381
- _block_destroy_helper.390
- _block_destroy_helper.397
- _block_destroy_helper.401
- _block_destroy_helper.405
- _block_destroy_helper.409
- _block_destroy_helper.413
- _block_destroy_helper.417
- _block_destroy_helper.421
- _block_destroy_helper.427
- _block_destroy_helper.448
- _block_destroy_helper.455
- _block_destroy_helper.462
- _block_destroy_helper.469
- _block_destroy_helper.477
- _block_destroy_helper.508
- _block_destroy_helper.518
- _block_destroy_helper.524
- _block_destroy_helper.530
- _block_destroy_helper.537
- _block_destroy_helper.544
- _block_destroy_helper.551
- _block_destroy_helper.555
- _block_destroy_helper.561
- _block_destroy_helper.577
- _block_destroy_helper.580
- _block_destroy_helper.586
- _block_destroy_helper.593
- _block_destroy_helper.599
- _block_destroy_helper.606
- _block_destroy_helper.613
- _block_destroy_helper.626
- _block_destroy_helper.632
- _block_destroy_helper.638
- _block_destroy_helper.665
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.654
- _objc_msgSend$_appendAssertion:forServerPosterPath:
- _objc_msgSend$_deleteDataStoreWithCompletion:
- _objc_msgSend$_deleteTransientData:
- _objc_msgSend$_internalLock_appendAssertion:forServerPosterPath:
- _objc_msgSend$_internalLock_numberOfInUseAssertionsForPath:
- _objc_msgSend$_internalLock_removeAssertion:forServerPosterPath:
- _objc_msgSend$_invalidateInUseAssertion:forServerPosterPath:
- _objc_msgSend$_numberOfInUseAssertionsForPath:
- _objc_msgSend$_presentedEditingSceneViewController
- _objc_msgSend$_removeAssertion:forServerPosterPath:
- _objc_msgSend$_stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:error:
- _objc_msgSend$_triggerMessedUpDataProtectionWithCompletion:
- _objc_msgSend$acquireInUseAssertionForPath:reason:
- _objc_msgSend$assertionManager:pathIsNowMarkedAsNOTInUse:
- _objc_msgSend$assertionManager:pathIsNowMarkedInUse:
- _objc_msgSend$cancelRequestedSnapshotsForPath:
- _objc_msgSend$inUseAssertionForIdentity:reason:
- _objc_msgSend$inUseAssertionForPath:reason:
- _swift_setDeallocating
- _symbolic _____y_____G s23_ContiguousArrayStorageC So45PRPosterHomeScreenConfigurationAppearanceTypeV
CStrings:
+ "\x11'\x13\"\x11"
+ "\x13\x12"
+ "(null provider)"
+ "-[PBFPosterExtensionDataStoreXPCServiceGlue _mutateDataStoreState:error:]"
+ "@\"BSAtomicSignal\""
+ "@\"NSSet\"24@0:8@\"NSString\"16"
+ "@\"PRUpdatingService\"24@0:8o^@16"
+ "@\"_PBFPosterExtensionDataStoreAssertionController\""
+ "@68@0:8@16@24B32@36q44@52o^@60"
+ "B16@?0@\"<PBFPosterExtensionDataStoreAssertionControlling>\"8"
+ "B16@?0@\"UIViewController\"8"
+ "B24@0:8@?16"
+ "B32@0:8@\"PRSServerPosterIdentity\"16@\"NSString\"24"
+ "B32@0:8Q16o^@24"
+ "Division by zero"
+ "Division results in an overflow"
+ "Forwarding %{public}@ appearance notification to child view controller: %{public}@"
+ "Forwarding appearance notification %{public}@ to presented view controller: %{public}@"
+ "Insufficient space allocated to copy string contents"
+ "PBFPosterExtensionDataStoreAssertionControlling"
+ "PBFPosterExtensionDataStoreAssertionIntrospection"
+ "PREditingAppearanceNotificationForwarding"
+ "Reaping data store"
+ "Reaping snapshots"
+ "Reaping transient data (all? %{BOOL}u"
+ "Role %{public}@ had no changes... moving on..."
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<SBLeafIconDataSource>\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSAttributedString\",?,C,N"
+ "T@\"NSAttributedString\",?,C,N,V_attributedPosterTitle"
+ "T@\"NSMapTable\",R,C,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,C,N,V_posterDescription"
+ "T@\"NSString\",?,C,N,V_posterTitle"
+ "T@\"NSString\",?,R,C"
+ "T@\"SBIcon\",?,R,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"UIWindow\",?,&,N"
+ "T@\"_UILegibilitySettings\",?,&,N"
+ "T@?,?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisDropping"
+ "TB,?,N,GisEditing"
+ "TB,?,N,GisOverlapping"
+ "TB,?,N,GisShowingContextMenu"
+ "TB,?,N,GisUserInteractionEnabled"
+ "TB,?,R,N"
+ "TQ,?,N"
+ "Td,?,N"
+ "Td,?,R,N"
+ "T{CGPoint=dd},?,R,N"
+ "T{SBIconApproximateLayoutPosition=QQ},?,N"
+ "T{UIEdgeInsets=dddd},?,R,N"
+ "Unable to build up a new extension instance to service applying updates"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "[%{public}@] Correcting unselected poster has failed."
+ "[%{public}@] unable to ascertain new selected poster for role."
+ "[_localeDidChange] dataStore bringup error: %{public}@"
+ "[_localeDidChange] dataStore bringup suceeded"
+ "[_localeDidChange] dataStore teardown succeeded"
+ "[_localeDidChange] dataStore teardownError: %{public}@"
+ "[inUseAssocPosterPathIdentitiesForReason containsObject:[[inUseHomeScreenConfiguration _path] serverIdentity]]"
+ "[inUsePosterPathIdentitiesForReason containsObject:[[inUseSwitcherConfiguration _path] serverIdentity]]"
+ "_PBFPosterExtensionDataStoreAssertionController"
+ "_appendAssertion:forIdentity:"
+ "_controller"
+ "_internalLock_appendAssertion:forIdentity:"
+ "_internalLock_removeAssertion:forIdentity:"
+ "_invalidationSignal"
+ "_lock_trimCachedSnapshotsToRequests:"
+ "_mutateDataStoreState:error:"
+ "_notifyObserversOfNewAssertions:newlyNotInUseAssertions:"
+ "_notifyObserversOfUpdatedController:"
+ "_numberOfInUseAssertionsForIdentity:"
+ "_postDidTearDownNotification"
+ "_removeAssertion:forIdentity:"
+ "_stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:assetUpdater:error:"
+ "_txFlag"
+ "acquireInUseAssertionForIdentity:reason:"
+ "assertionManager:identityIsNowMarkedAsInUse:"
+ "assertionManager:identityIsNowMarkedAsNOTInUse:"
+ "cancelRequestedSnapshotsForIdentity:"
+ "childViewControllers"
+ "displayOrder"
+ "executeTransaction:"
+ "inUseAssertionsByIdentity"
+ "initWithController:"
+ "invalid Collection: less than 'count' elements in collection"
+ "invalidateInUseAssertionForIdentity:reason:"
+ "isActiveReason"
+ "isScrollAnimating"
+ "orderedSet"
+ "q24@0:8@\"NSString\"16"
+ "stablePersistenceIdentifier"
+ "v32@0:8@\"PBFPosterExtensionDataStoreAssertionManager\"16@\"PRSServerPosterIdentity\"24"
+ "\xf2"
- "\x11'\x17\x11"
- "\x12\x12"
- "@\"PRUpdatingService\"24@0:8^@16"
- "@60@0:8@16@24B32@36q44o^@52"
- "BSSimpleAssertion"
- "Deleting data store"
- "Forwarding appearance notification to PREditingSceneViewController: %{public}@"
- "PRSServerPosterIdentity"
- "T@\"<SBLeafIconDataSource>\",R,N"
- "T@\"NSAttributedString\",C,N"
- "T@\"NSAttributedString\",C,N,V_attributedPosterTitle"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_posterDescription"
- "T@\"NSString\",C,N,V_posterTitle"
- "T@\"SBIcon\",R,N"
- "T@\"UIWindow\",&,N"
- "T@\"_UILegibilitySettings\",&,N"
- "T@?,C,N"
- "TB,N,GisDropping"
- "TB,N,GisEditing"
- "TB,N,GisOverlapping"
- "TB,N,GisShowingContextMenu"
- "TB,N,GisUserInteractionEnabled"
- "TQ,N"
- "Tearing down data store for deletion of snapshots"
- "Tearing down data store for transient info deletion (should delete all transient info? %{BOOL}u"
- "T{CGPoint=dd},R,N"
- "T{SBIconApproximateLayoutPosition=QQ},N"
- "[_assertionManager inUseAssertionForPath:(PRSServerPosterPath *)[inUseHomeScreenConfiguration _path] reason:assocPostersInUseAssertionReason] != nil"
- "[_assertionManager inUseAssertionForPath:(PRSServerPosterPath *)[inUseSwitcherConfiguration _path] reason:orderedPostersInUseAssertionReason] != nil"
- "[_bs_assert_object isKindOfClass:BSSimpleAssertionClass]"
- "[_bs_assert_object isKindOfClass:PRSServerPosterIdentityClass]"
- "_appendAssertion:forServerPosterPath:"
- "_deleteDataStoreWithCompletion:"
- "_deleteSnapshots"
- "_deleteTransientData:"
- "_internalLock_appendAssertion:forServerPosterPath:"
- "_internalLock_numberOfInUseAssertionsForPath:"
- "_internalLock_removeAssertion:forServerPosterPath:"
- "_invalidateInUseAssertion:forServerPosterPath:"
- "_isAnimatingScroll"
- "_numberOfInUseAssertionsForPath:"
- "_presentedEditingSceneViewController"
- "_removeAssertion:forServerPosterPath:"
- "_stateLock_prepareReloadConfigurationOperationForExtension:path:locationInUse:sessionInfo:powerLogReason:error:"
- "_teardownDataStoreWithCompletion:"
- "_triggerMessedUpDataProtectionWithCompletion:"
- "a"
- "acquireInUseAssertionForPath:reason:"
- "assertionManager:pathIsNowMarkedAsNOTInUse:"
- "assertionManager:pathIsNowMarkedInUse:"
- "cancelRequestedSnapshotsForPath:"
- "inUseAssertionForIdentity:reason:"
- "inUseAssertionForPath:reason:"
- "isPosterInUse:"
- "v32@0:8@\"PBFPosterExtensionDataStoreAssertionManager\"16@\"PRSServerPosterPath\"24"

```
