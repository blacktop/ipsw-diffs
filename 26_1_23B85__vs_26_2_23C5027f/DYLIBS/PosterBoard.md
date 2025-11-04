## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-304.1.3.105.0
-  __TEXT.__text: 0x19f27c
+304.2.3.101.0
+  __TEXT.__text: 0x1a1f58
   __TEXT.__auth_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0xc4d0
-  __TEXT.__const: 0x29b4
-  __TEXT.__gcc_except_tab: 0x49dc
-  __TEXT.__cstring: 0x14a3b
-  __TEXT.__oslogstring: 0x13d12
+  __TEXT.__objc_methlist: 0xc590
+  __TEXT.__const: 0x29c4
+  __TEXT.__gcc_except_tab: 0x4b08
+  __TEXT.__cstring: 0x14e1b
+  __TEXT.__oslogstring: 0x14482
   __TEXT.__dlopen_cstrs: 0x26e
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x223c

   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x4e48
+  __TEXT.__unwind_info: 0x4ea8
   __TEXT.__eh_frame: 0x960
-  __TEXT.__objc_classname: 0x2127
-  __TEXT.__objc_methname: 0x2a009
-  __TEXT.__objc_methtype: 0x8c8e
-  __TEXT.__objc_stubs: 0x18600
-  __DATA_CONST.__got: 0x1530
-  __DATA_CONST.__const: 0x48d0
+  __TEXT.__objc_classname: 0x2132
+  __TEXT.__objc_methname: 0x2a266
+  __TEXT.__objc_methtype: 0x8ca7
+  __TEXT.__objc_stubs: 0x187c0
+  __DATA_CONST.__got: 0x1538
+  __DATA_CONST.__const: 0x4990
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x598
+  __DATA_CONST.__objc_protolist: 0x5a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8608
+  __DATA_CONST.__objc_selrefs: 0x8670
   __DATA_CONST.__objc_protorefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x1530
-  __AUTH_CONST.__const: 0x5c60
-  __AUTH_CONST.__cfstring: 0xa160
-  __AUTH_CONST.__objc_const: 0x2cba8
+  __AUTH_CONST.__const: 0x5d00
+  __AUTH_CONST.__cfstring: 0xa460
+  __AUTH_CONST.__objc_const: 0x2da68
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x190

   __AUTH.__objc_data: 0x1f60
   __AUTH.__data: 0x490
   __DATA.__objc_ivar: 0xe28
-  __DATA.__data: 0x3de0
+  __DATA.__data: 0x3e40
   __DATA.__bss: 0x830
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x61e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DBC3AE01-DA5A-382A-ABDA-511FF1736220
-  Functions: 7362
-  Symbols:   19559
-  CStrings:  11383
+  UUID: A14358A1-5002-31A5-A54D-ABC3EB2AE150
+  Functions: 7398
+  Symbols:   19706
+  CStrings:  11474
 
Symbols:
+ +[NSUserDefaults(PBFUtilities) pbf_completedPosterBundleIdentifierMigrations]
+ +[NSUserDefaults(PBFUtilities) pbf_setCompletedPosterBundleIdentifierMigrations:]
+ -[LSPropertyList(PBFAdditions) pbf_hasPosterBundleIdentifierMigrationMetadata]
+ -[LSPropertyList(PBFAdditions) pbf_oldBundleIdentifiersForPosterMigration]
+ -[PBFGalleryConfiguration _createPosterPreviewForItem:section:posterDescriptorLookupInfo:]
+ -[PBFGalleryConfiguration _createPosterPreviewForItem:section:posterDescriptorLookupInfo:].cold.1
+ -[PBFGalleryConfiguration enumeratePosterPreviews:]
+ -[PBFGalleryConfiguration itemForUniqueIdentifier:]
+ -[PBFGalleryConfiguration posterPreviewsForSectionWithIdentifier:]
+ -[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]
+ -[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:]
+ -[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:].cold.1
+ -[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:].cold.2
+ -[PBFPosterExtensionDataStoreMigrator performPosterBundleIdentifierMigrationIfNeeded:]
+ -[PBFPosterGalleryDataProvider itemForUniqueIdentifier:]
+ -[PBFPosterGalleryDataProvider itemForUniqueIdentifier]
+ -[PBFPosterGalleryDataProvider items]
+ -[PBFPosterGalleryDataProvider posterPreviewForUniqueIdentifier:]
+ -[PBFPosterGalleryDataProvider posterPreviewsForSectionWithIdentifier:]
+ -[PBFPosterGalleryDataProvider setItemForUniqueIdentifier:]
+ -[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl renameBundleProvider:toBundleProvider:error:]
+ -[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl renameBundleProvider:toBundleProvider:error:].cold.1
+ -[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl renameBundleProvider:toBundleProvider:error:].cold.2
+ GCC_except_table101
+ GCC_except_table110
+ GCC_except_table237
+ GCC_except_table318
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table348
+ GCC_except_table359
+ GCC_except_table377
+ GCC_except_table387
+ GCC_except_table401
+ GCC_except_table416
+ GCC_except_table471
+ GCC_except_table492
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table86
+ _OBJC_IVAR_$_PBFPosterGalleryDataProvider._itemForUniqueIdentifier
+ _PBFPosterBundleIdentifierMigrationCompletedKey
+ __OBJC_$_PROP_LIST_PBFPreview
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPreview
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBFPreview
+ __OBJC_$_PROTOCOL_REFS_PBFPreview
+ __OBJC_LABEL_PROTOCOL_$_PBFPreview
+ __OBJC_PROTOCOL_$_PBFPreview
+ __PBFExtensionStoreCoordinatorForURLAndBundleIdentifier
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.965
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.971
+ ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.967
+ ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.897
+ ___122-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:]_block_invoke
+ ___122-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:]_block_invoke.74
+ ___122-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:]_block_invoke.74.cold.1
+ ___122-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:]_block_invoke.cold.1
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.103
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.109
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.111
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.112
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.112.cold.1
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.97
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.97.cold.1
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.97.cold.2
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.97.cold.3
+ ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.97.cold.4
+ ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.947
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.841
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.845
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.852
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.857
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.869
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.871
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.860
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.870
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.873
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.877
+ ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.881
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1031
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1032
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1039
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1040
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1040.cold.1
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1044
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1053
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1063
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1049
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1054
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1065
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1050
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1058
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1066
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1059
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1070
+ ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.1071
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.977
+ ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.979
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.927
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.927.cold.1
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.930
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.937
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.938
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.940
+ ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.939
+ ___37-[PBFPosterGalleryDataProvider items]_block_invoke
+ ___51-[PBFGalleryConfiguration enumeratePosterPreviews:]_block_invoke
+ ___51-[PBFGalleryConfiguration enumeratePosterPreviews:]_block_invoke_2
+ ___55-[PBFGalleryConfiguration complicationSnapshotRequests]_block_invoke_2
+ ___60-[PBFGalleryConfiguration posterSnapshotRequestsForContext:]_block_invoke_2
+ ___66-[PBFGalleryConfiguration posterPreviewsForSectionWithIdentifier:]_block_invoke
+ ___71-[PBFPosterGalleryDataProvider posterPreviewsForSectionWithIdentifier:]_block_invoke
+ ___74-[LSPropertyList(PBFAdditions) pbf_oldBundleIdentifiersForPosterMigration]_block_invoke
+ ___75-[PBFPosterExtensionDataStore _executeCleanupOfServerPosterIdentity:error:]_block_invoke.1026
+ ___86-[PBFPosterExtensionDataStoreMigrator performPosterBundleIdentifierMigrationIfNeeded:]_block_invoke
+ ___86-[PBFPosterExtensionDataStoreMigrator performPosterBundleIdentifierMigrationIfNeeded:]_block_invoke.cold.1
+ ___90-[PBFGalleryConfiguration _createPosterPreviewForItem:section:posterDescriptorLookupInfo:]_block_invoke
+ ___90-[PBFGalleryConfiguration _createPosterPreviewForItem:section:posterDescriptorLookupInfo:]_block_invoke_2
+ ___90-[PBFGalleryConfiguration _createPosterPreviewForItem:section:posterDescriptorLookupInfo:]_block_invoke_3
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.1
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.2
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.3
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.4
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.5
+ ___91-[PBFPosterExtensionDataStoreMigrator _performBundleIdentifierMigrationWithRequests:error:]_block_invoke.cold.6
+ ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.777
+ ___Block_byref_object_copy_.928
+ ___Block_byref_object_dispose_.929
+ ___block_descriptor_32_e22_16?0"<PBFPreview>"8l
+ ___block_descriptor_32_e8_16?08l
+ ___block_descriptor_40_e8_32s_e29_v32?0"<PBFPreview>"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e50_v32?0"NSObject<NSCopying>"8"<PBFPreview>"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e44_v32?0"NSString"8"PFPosterExtension"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_v32?0"NSObject<NSCopying>"8"<PBFPreview>"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e34_v32?0"NSString"8"NSArray"16^B24ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e90_B16?0"<PBFPosterExtensionDataStorageMutating><PBFPosterExtensionDataStorageRetrieving>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1035
+ ___block_literal_global.107
+ ___block_literal_global.113
+ ___block_literal_global.128
+ ___block_literal_global.133
+ ___block_literal_global.134
+ ___block_literal_global.154
+ ___block_literal_global.221
+ ___block_literal_global.254
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.313
+ ___block_literal_global.417
+ ___block_literal_global.828
+ ___block_literal_global.833
+ ___block_literal_global.844
+ ___block_literal_global.854
+ ___block_literal_global.859
+ ___block_literal_global.94
+ ___block_literal_global.96
+ ___block_literal_global.960
+ ___block_literal_global.976
+ ___block_literal_global.994
+ _kPRPosterBundleIdentifierMigrationKey
+ _objc_msgSend$_createPosterPreviewForItem:section:posterDescriptorLookupInfo:
+ _objc_msgSend$_performBundleIdentifierMigrationWithRequests:error:
+ _objc_msgSend$_performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:
+ _objc_msgSend$enumeratePosterPreviews:
+ _objc_msgSend$extensionsForIdentifier
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$itemForUniqueIdentifier
+ _objc_msgSend$itemForUniqueIdentifier:
+ _objc_msgSend$pbf_completedPosterBundleIdentifierMigrations
+ _objc_msgSend$pbf_hasPosterBundleIdentifierMigrationMetadata
+ _objc_msgSend$pbf_oldBundleIdentifiersForPosterMigration
+ _objc_msgSend$pbf_setCompletedPosterBundleIdentifierMigrations:
+ _objc_msgSend$performPosterBundleIdentifierMigrationIfNeeded:
+ _objc_msgSend$pf_replaceURL:withURL:error:
+ _objc_msgSend$posterPreviewForUniqueIdentifier:
+ _objc_msgSend$posterPreviewsForSectionWithIdentifier:
+ _objc_msgSend$renameBundleProvider:toBundleProvider:error:
+ _objc_msgSend$setItemForUniqueIdentifier:
- -[PBFGalleryConfiguration enumeratePreviews:]
- -[PBFGalleryConfiguration previewForItem:section:].cold.1
- -[PBFPosterGalleryDataProvider posterPreviewForPosterUniqueIdentifier]
- -[PBFPosterGalleryDataProvider previewForPreviewUniqueIdentifier:]
- -[PBFPosterGalleryDataProvider setPosterPreviewForPosterUniqueIdentifier:]
- GCC_except_table103
- GCC_except_table238
- GCC_except_table319
- GCC_except_table326
- GCC_except_table328
- GCC_except_table349
- GCC_except_table360
- GCC_except_table378
- GCC_except_table388
- GCC_except_table402
- GCC_except_table417
- GCC_except_table475
- GCC_except_table495
- GCC_except_table532
- GCC_except_table535
- GCC_except_table536
- _OBJC_IVAR_$_PBFPosterGalleryDataProvider._posterPreviewForPosterUniqueIdentifier
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.908
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke.914
- ___101-[PBFPosterExtensionDataStore _stateLock_pushPosterDescriptorsToProactiveForReason:force:completion:]_block_invoke_2.910
- ___122-[PBFPosterExtensionDataStore _stateLock_updateDescriptorsFromStaticDescriptorsForExtensionBundleIdentifier:reason:error:]_block_invoke.840
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.44
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.44.cold.1
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.44.cold.2
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.44.cold.3
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.44.cold.4
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.50
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.57
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.59
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.60
- ___123+[PBFPosterExtensionDataStoreMigrator migrateDataStoreAtBaseURL:fromVersion:toVersion:cleanupAfterMigrationSucceeds:error:]_block_invoke.60.cold.1
- ___123-[PBFPosterExtensionDataStore _stateLock_deletePosterDescriptorsForExtensionBundleIdentifier:waitForPushToProactive:error:]_block_invoke.890
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.784
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.788
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.795
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.800
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.812
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke.814
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.803
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.813
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_2.816
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_3.820
- ___133-[PBFPosterExtensionDataStore _stateLock_updateExtensions:refreshDescriptors:powerLogReason:galleryUpdateOptions:queuedUpOperations:]_block_invoke_4.824
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.1006
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.974
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.975
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.982
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.983
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.983.cold.1
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.987
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke.996
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.1008
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.992
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_2.997
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1001
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.1009
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_3.993
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1002
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_4.1013
- ___156-[PBFPosterExtensionDataStore buildPrewarmPlanWithIdentifier:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:prewarmDisplayContext:]_block_invoke_5.1014
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.920
- ___159-[PBFPosterExtensionDataStore _stateLock_updateGalleryWithSuggestedLayout:descriptorsByExtensionBundleIdentifier:staticDescriptorsByExtensionBundleIdentifier:]_block_invoke.922
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.870
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.870.cold.1
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.873
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.880
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.881
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke.883
- ___181-[PBFPosterExtensionDataStore _stateLock_enqueueReloadDescriptorsOperationForExtensionBundleIdentifier:reason:powerLogReason:postEnqueueGalleryUpdateOptions:sessionInfo:completion:]_block_invoke_2.882
- ___45-[PBFGalleryConfiguration enumeratePreviews:]_block_invoke
- ___45-[PBFGalleryConfiguration enumeratePreviews:]_block_invoke_2
- ___50-[PBFGalleryConfiguration previewForItem:section:]_block_invoke
- ___50-[PBFGalleryConfiguration previewForItem:section:]_block_invoke_2
- ___50-[PBFGalleryConfiguration previewForItem:section:]_block_invoke_3
- ___69-[PBFPosterExtensionDataStore _stateLock_initialRoleCoordinatorSetup]_block_invoke_2
- ___69-[PBFPosterExtensionDataStore _stateLock_initialRoleCoordinatorSetup]_block_invoke_2.cold.1
- ___75-[PBFPosterExtensionDataStore _executeCleanupOfServerPosterIdentity:error:]_block_invoke.969
- ___93-[PBFPosterExtensionDataStore fetchPosterSuggestionsForFocusModeWithUUID:context:completion:]_block_invoke.720
- ___Block_byref_object_copy_.871
- ___Block_byref_object_dispose_.872
- ___block_descriptor_40_e8_32s_e35_v32?0"<PBFPosterPreview>"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e56_v32?0"NSObject<NSCopying>"8"<PBFPosterPreview>"16^B24ls32l8
- ___block_descriptor_48_e8_32s40s_e56_v32?0"NSObject<NSCopying>"8"<PBFPosterPreview>"16^B24ls32l8s40l8
- ___block_literal_global.207
- ___block_literal_global.253
- ___block_literal_global.267
- ___block_literal_global.272
- ___block_literal_global.295
- ___block_literal_global.402
- ___block_literal_global.41
- ___block_literal_global.47
- ___block_literal_global.771
- ___block_literal_global.776
- ___block_literal_global.787
- ___block_literal_global.797
- ___block_literal_global.802
- ___block_literal_global.903
- ___block_literal_global.919
- ___block_literal_global.937
- ___block_literal_global.978
- _objc_msgSend$enumeratePreviews:
- _objc_msgSend$posterPreviewForPosterUniqueIdentifier
- _objc_msgSend$previewForPreviewUniqueIdentifier:
- _objc_msgSend$setPosterPreviewForPosterUniqueIdentifier:
CStrings:
+ ":newProvider"
+ ":oldProvider"
+ "@16@?0@\"<PBFPreview>\"8"
+ "@16@?0@8"
+ "Already migrated bundle ID for %{public}@ - skipping"
+ "B56@0:8@16@24@32Q40o^@48"
+ "Cannot verify new extension directory state for %@ - potential data loss risk"
+ "Cannot verify old extension directory state for %@ - potential data loss risk"
+ "CompletedPosterBundleIdentifierMigrations"
+ "Copying Extensions directory to temp location %{public}@ for migration"
+ "Extension %{public}@ has migration metadata but Info.plist missing old bundle identifiers - skipping"
+ "Failed to check if new extension directory exists at %{public}@: %{public}@"
+ "Failed to check if old extension directory exists at %{public}@: %{public}@"
+ "Failed to cleanup temp directory at %{public}@: %{public}@"
+ "Failed to copy Extensions directory to temp directory: %{public}@"
+ "Failed to create extension store coordinator to mark migration completion for %{public}@"
+ "Failed to create temp directory structure: %{public}@"
+ "Failed to read configurations directory for new extension %{public}@: %{public}@"
+ "Failed to remove empty extension directory at %{public}@ for new extension %{public}@ before migration: %{public}@"
+ "Failed to rename %{public}@ to %{public}@ in temp directory: %{public}@"
+ "Failed to replace current Extensions directory with migrated version: %{public}@"
+ "Failed to update posters in database from %{public}@ to %{public}@: %{public}@"
+ "Found %lu extensions requiring bundle ID migration"
+ "Marked bundle ID migration as completed for %{public}@"
+ "Marked bundle ID migration as completed for %{public}@ (no old data to migrate)"
+ "Multiple old extension directories exist"
+ "New extension directory %@ already exists with poster data"
+ "No poster bundle ID migrations needed - extensions already migrated or no old data found on disk"
+ "No poster bundle ID migrations needed - no extensions requesting migration"
+ "No poster extensions found during bundle ID migration - this should never happen"
+ "OldBundleIdentifiers"
+ "PBFPreview"
+ "Poster bundle ID migration conflict: Multiple old bundle IDs have data on disk - %{public}@ and %{public}@"
+ "Poster bundle ID migration conflict: New extension directory at %{public}@ already exists with %lu configuration(s)"
+ "Poster bundle ID migration conflict: both %{public}@ and %{public}@ claim old bundle ID %{public}@"
+ "Poster bundle ID migration conflict: multiple extensions claim old bundle ID %@"
+ "PosterBundleIdentifierMigrationCompleted"
+ "PosterBundleIdentifierMigrationStaging"
+ "Removed empty extension directory at %{public}@ for new extension %{public}@ to allow migration from old data"
+ "SELECT providerId from poster WHERE UUID = :posterUUID;"
+ "Scheduled migration for %{public}@ from old bundle ID: %{public}@"
+ "Successfully completed bundle ID migration for %{public}@"
+ "T@\"NSMutableDictionary\",&,N,V_itemForUniqueIdentifier"
+ "T@\"NSSet\",C,N,Spbf_setCompletedPosterBundleIdentifierMigrations:"
+ "TESTING"
+ "UPDATE poster SET providerId = :newProvider WHERE providerId = :oldProvider;"
+ "URL: %{public}@ wasMigrationJustPerformed: %{BOOL}u -- bundle ID migration failed: %{public}@"
+ "_createPosterPreviewForItem:section:posterDescriptorLookupInfo:"
+ "_itemForUniqueIdentifier"
+ "_performBundleIdentifierMigrationWithRequests:error:"
+ "_performBundleIdentifierMigrations:extensionContainerURL:baseURL:currVersion:error:"
+ "com.apple.Posters.WeatherPosterApp.WeatherPoster"
+ "conflictingNewBundleID1"
+ "conflictingNewBundleID2"
+ "conflictingOldBundleID"
+ "enumeratePosterPreviews:"
+ "existingConfigurationCount"
+ "extensionsForIdentifier"
+ "fileURLWithPathComponents:"
+ "firstOldBundleID"
+ "isEqual:ignoringModifications:"
+ "itemForUniqueIdentifier"
+ "itemForUniqueIdentifier:"
+ "newBundleIdentifier"
+ "newProvider"
+ "oldProvider"
+ "pbf_completedPosterBundleIdentifierMigrations"
+ "pbf_hasPosterBundleIdentifierMigrationMetadata"
+ "pbf_oldBundleIdentifiersForPosterMigration"
+ "pbf_setCompletedPosterBundleIdentifierMigrations:"
+ "performPosterBundleIdentifierMigrationIfNeeded:"
+ "pf_replaceURL:withURL:error:"
+ "posterPreviewsForSectionWithIdentifier:"
+ "renameBundleProvider:toBundleProvider:error:"
+ "secondOldBundleID"
+ "setItemForUniqueIdentifier:"
+ "v32@?0@\"<PBFPreview>\"8Q16^B24"
+ "v32@?0@\"NSObject<NSCopying>\"8@\"<PBFPreview>\"16^B24"
+ "v32@?0@\"NSString\"8@\"PFPosterExtension\"16^B24"
+ "{?=\"itemSizeForType\"[6{CGSize=\"width\"d\"height\"d}]\"sectionContentInsets\"[6{NSDirectionalEdgeInsets=\"top\"d\"leading\"d\"bottom\"d\"trailing\"d}]\"standardSpacing\"d\"groupSpacing\"d}"
+ "{?=[6{CGSize=dd}][6{NSDirectionalEdgeInsets=dddd}]dd}24@0:8@16"
+ "\xf0\xf0\xf0\xa2"
- "Cleaned up orphaned poster SUCCEEDED  %{public}@"
- "Cleaning up orphaned poster configuration %{public}@ failed: %{public}@"
- "Found orphaned %{public}@ poster configuration: %lu"
- "SELECT providerID from poster WHERE UUID = :posterUUID;"
- "T@\"NSMutableDictionary\",&,N,V_posterPreviewForPosterUniqueIdentifier"
- "_posterPreviewForPosterUniqueIdentifier"
- "enumeratePreviews:"
- "isEqual:ignoringVariation:"
- "posterPreviewForPosterUniqueIdentifier"
- "previewForPreviewUniqueIdentifier:"
- "setPosterPreviewForPosterUniqueIdentifier:"
- "v32@?0@\"NSObject<NSCopying>\"8@\"<PBFPosterPreview>\"16^B24"
- "{?=\"itemSizeForType\"[5{CGSize=\"width\"d\"height\"d}]\"sectionContentInsets\"[5{NSDirectionalEdgeInsets=\"top\"d\"leading\"d\"bottom\"d\"trailing\"d}]\"standardSpacing\"d\"groupSpacing\"d}"
- "{?=[5{CGSize=dd}][5{NSDirectionalEdgeInsets=dddd}]dd}24@0:8@16"
- "\xf0\xf0\xf0B"

```
