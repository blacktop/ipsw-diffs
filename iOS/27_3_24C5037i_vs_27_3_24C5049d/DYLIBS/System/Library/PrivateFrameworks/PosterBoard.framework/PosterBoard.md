## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-355.3.7.0.0
-  __TEXT.__text: 0x28db94
-  __TEXT.__objc_methlist: 0xf53c
-  __TEXT.__const: 0x8834
-  __TEXT.__gcc_except_tab: 0x4ffc
-  __TEXT.__cstring: 0x14a45
-  __TEXT.__oslogstring: 0x20c2a
+355.3.12.0.0
+  __TEXT.__text: 0x29da24
+  __TEXT.__objc_methlist: 0xf91c
+  __TEXT.__const: 0x8994
+  __TEXT.__gcc_except_tab: 0x51e8
+  __TEXT.__cstring: 0x14e55
+  __TEXT.__oslogstring: 0x217fa
   __TEXT.__dlopen_cstrs: 0x2c6
   __TEXT.__ustring: 0xe
-  __TEXT.__swift5_typeref: 0x983a
-  __TEXT.__constg_swiftt: 0x6dd8
+  __TEXT.__swift5_typeref: 0x98de
+  __TEXT.__constg_swiftt: 0x7030
   __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x553d
-  __TEXT.__swift5_fieldmd: 0x3660
+  __TEXT.__swift5_reflstr: 0x569d
+  __TEXT.__swift5_fieldmd: 0x3750
   __TEXT.__swift5_assocty: 0x690
-  __TEXT.__swift5_proto: 0x2a0
-  __TEXT.__swift5_types: 0x27c
-  __TEXT.__swift5_capture: 0x2a24
-  __TEXT.__swift5_protos: 0x68
+  __TEXT.__swift5_proto: 0x2a8
+  __TEXT.__swift5_types: 0x284
+  __TEXT.__swift5_capture: 0x2fc8
+  __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0xec
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9bb8
+  __TEXT.__unwind_info: 0x9e28
   __TEXT.__eh_frame: 0x1d78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x53e8
-  __DATA_CONST.__objc_classlist: 0x780
-  __DATA_CONST.__objc_catlist: 0x100
+  __DATA_CONST.__const: 0x5578
+  __DATA_CONST.__objc_classlist: 0x790
+  __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x6f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa048
+  __DATA_CONST.__objc_selrefs: 0xa2b0
   __DATA_CONST.__objc_protorefs: 0x2e0
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x160
-  __DATA_CONST.__got: 0x1eb8
-  __AUTH_CONST.__const: 0xa4d0
-  __AUTH_CONST.__cfstring: 0xc5e0
-  __AUTH_CONST.__objc_const: 0x42620
+  __DATA_CONST.__got: 0x1ee0
+  __AUTH_CONST.__const: 0xb068
+  __AUTH_CONST.__cfstring: 0xc8c0
+  __AUTH_CONST.__objc_const: 0x42bd8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2580
-  __AUTH.__objc_data: 0x4018
+  __AUTH_CONST.__auth_got: 0x2598
+  __AUTH.__objc_data: 0x40b8
   __AUTH.__data: 0x1260
-  __DATA.__objc_ivar: 0x10e8
-  __DATA.__data: 0x6b80
-  __DATA.__common: 0x168
-  __DATA_DIRTY.__objc_data: 0x7250
-  __DATA_DIRTY.__data: 0x1560
+  __DATA.__objc_ivar: 0x1128
+  __DATA.__data: 0x6bf0
+  __DATA.__common: 0x170
+  __DATA_DIRTY.__objc_data: 0x7450
+  __DATA_DIRTY.__data: 0x1588
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x1560
-  __DATA_DIRTY.__common: 0x158
+  __DATA_DIRTY.__bss: 0x1530
+  __DATA_DIRTY.__common: 0x148
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11789
-  Symbols:   11408
-  CStrings:  4136
+  Functions: 12059
+  Symbols:   11572
+  CStrings:  4206
 
Symbols:
+ +[NSUserDefaults(PBFUtilities) _pbf_migrationStateKeys]
+ +[NSUserDefaults(PBFUtilities) pbf_migrationState]
+ +[NSUserDefaults(PBFUtilities) pbf_resetMigrationState]
+ +[PBFPosterRoleCoordinator posterCollectionForRole:storage:sortedPosterUUIDs:posterForUUID:error:]
+ +[PBFPosterStoreSeed _gatedSeedWithGlue:outcome:reason:error:]
+ +[PBFPosterStoreSeed _readSeedForBaseURL:outcome:reason:error:]
+ +[PBFPosterStoreSeed seedWithGlue:outcome:]
+ -[PBFDataStoreArchiveAdjudicator importArchiveData:name:error:]
+ -[PBFPosterExtensionDataStore _concludeAmbientConfigurationMigrationAfterPass:]
+ -[PBFPosterExtensionDataStore _galleryConfigurationForRole:]
+ -[PBFPosterExtensionDataStore _isGalleryWorkEnabledForRole:]
+ -[PBFPosterExtensionDataStore _publishLockScreenPosterCollection:]
+ -[PBFPosterExtensionDataStore _rolesWithGalleryWorkEnabled]
+ -[PBFPosterExtensionDataStore _stateLock_setGalleryConfiguration:forRole:]
+ -[PBFPosterExtensionDataStore _stateLock_setSwitcherConfiguration:]
+ -[PBFPosterExtensionDataStore _test_setAmbientDefaults:]
+ -[PBFPosterExtensionDataStore _test_setGalleryController:forRole:]
+ -[PBFPosterExtensionDataStore publishedLockScreenGalleryConfiguration]
+ -[PBFPosterExtensionDataStore publishedLockScreenPosterCollection]
+ -[PBFPosterExtensionDataStore publishedSwitcherConfiguration]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _baseDataStoreURL:logsMigrationStatus:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _currentDataStoreReadyMarker]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _dataStoreReadyMarkerAtBaseURL:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _dataStoreReadyMarkerURLForBaseURL:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _leanBaseDataStoreURL]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_cancelDataStoreForLanguageChange]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_publishLoadedDataStore]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_unpublishLoadedDataStore]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_updatePinnedDisplays:embeddedDisplayContext:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue blockingDataStore]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue loadDataStoreWithCompletion:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue loadedDataStore]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:fetchAmbientPosterDiagnosticsWithCompletion:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:fetchMigrationStateWithCompletion:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:importArchivedDataStoreData:named:completion:]
+ -[PBFPosterExtensionDataStoreXPCServiceGlue server:restoreArchivedDataStoreNamed:backupExistingDataStore:resetMigrationState:completion:]
+ -[PBFPosterModelStoreCoordinator setSkipsMigrationSupplementCreation:]
+ -[PBFPosterModelStoreCoordinator skipsMigrationSupplementCreation]
+ -[PBFPosterSnapshotDefinition disallowsFilesystemCompression]
+ -[PBFPosterSnapshotManager _compressBundleAtURL:qos:thenCompletePUIRequest:imageURL:snapshotBundle:path:compressorForTesting:]
+ -[PBFPosterSnapshotManager _findReplacementForRemovedBundleOfPUIRequest:path:removedReservation:completion:]
+ -[PBFPosterSnapshotManager _finishCompressionOfPUIRequest:imageURL:snapshotBundle:path:]
+ -[PBFPosterSnapshotManager _lock_beginCompressingPUIRequest:bundleURL:qos:]
+ -[PBFPosterSnapshotManager _lock_cachedReservations:serveAllPUIRequests:]
+ -[PBFPosterSnapshotManager _lock_completeCompressedPUIRequest:imageURL:snapshotBundle:path:replacementReservation:]
+ -[PBFPosterSnapshotManager _lock_completePUIRequest:withImageURL:snapshotBundle:path:]
+ -[PBFPosterSnapshotManager _lock_compressionQoSForPUIRequest:]
+ -[PBFPosterSnapshotManager _lock_countInProgressContextsOfRequest:forTracker:]
+ -[PBFPosterSnapshotManager _lock_endCompressingPUIRequest:]
+ -[PBFPosterSnapshotManager _lock_hasSnapshotWorkInFlightForIdentity:]
+ -[PBFPosterSnapshotManager _lock_isPosterVisibleAtPath:]
+ -[PBFPosterSnapshotManager _lock_isRenderingOrCompressingAnyContextOfRequest:]
+ -[PBFPosterSnapshotManager _lock_isRenderingOrCompressingSnapshotContext:forIdentity:]
+ -[PBFPosterSnapshotManager _lock_noteCompletedPBFRequestsForPUIRequest:]
+ -[PBFPosterSnapshotManager _lock_raiseCompressionOfPUIRequestIfNeeded:]
+ -[PBFPosterSnapshotManager _lock_releasePrewarmAssertionIfIdle]
+ -[PBFPosterSnapshotManager _lock_sendRaiseForCompression:]
+ -[PBFPosterSnapshotManager _puiRequestTracker:matchesServerIdentity:displayContext:definition:]
+ -[PBFPosterSnapshotManager _submitSnapshotRequest:fulfilledReservations:completion:]
+ -[PBFPosterSnapshotManager _test_setBundleCompressionRaiser:]
+ -[PBFPosterSnapshotManager _test_setBundleCompressor:]
+ -[PBFPosterSnapshotPBFRequestTracker addCountedInProgressContext:]
+ -[PBFPosterSnapshotPBFRequestTracker hasCountedInProgressContexts]
+ -[PBFPosterSnapshotPBFRequestTracker takeCountedInProgressContexts]
+ -[PBFPosterStoreSeed .cxx_destruct]
+ -[PBFPosterStoreSeed _initWithSwitcherConfiguration:collection:]
+ -[PBFPosterStoreSeed lockScreenPosterCollection]
+ -[PBFPosterStoreSeed switcherConfiguration]
+ -[PFServerPosterPath(PBFUtilities) pbf_proactiveGalleryItemOptions]
+ -[PRMutablePosterTitleStyleConfiguration(PBFAdditions) pbf_applyGalleryOptions:]
+ -[PRPosterTitleStyleConfiguration(PBFAdditions) pbf_effectiveCompactTimeFontWithExtensionBundleURL:forRole:displayContext:]
+ -[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl initWithURL:options:skipsPragmas:error:]
+ -[_PBFPosterSnapshotCompression .cxx_destruct]
+ -[_PBFPosterSnapshotCompression bundleURL]
+ -[_PBFPosterSnapshotCompression initWithBundleURL:qos:]
+ -[_PBFPosterSnapshotCompression qos]
+ -[_PBFPosterSnapshotCompression setQos:]
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table123
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table145
+ GCC_except_table155
+ GCC_except_table166
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table199
+ GCC_except_table231
+ GCC_except_table265
+ GCC_except_table275
+ GCC_except_table362
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table393
+ GCC_except_table407
+ GCC_except_table418
+ GCC_except_table441
+ GCC_except_table451
+ GCC_except_table457
+ GCC_except_table460
+ GCC_except_table477
+ GCC_except_table493
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table497
+ GCC_except_table64
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table90
+ GCC_except_table98
+ _CSQuickActionsLayoutUsesSideButtons
+ _OBJC_CLASS_$_CSProminentButtonsView
+ _OBJC_CLASS_$_PBFPosterStoreSeed
+ _OBJC_CLASS_$_PRSPosterGalleryItemOptions
+ _OBJC_CLASS_$_PRSwitcherConfiguration
+ _OBJC_CLASS_$__PBFPosterSnapshotCompression
+ _OBJC_IVAR_$_PBFPosterExtensionDataStore._ambientDefaults
+ _OBJC_IVAR_$_PBFPosterExtensionDataStore._publishedLock
+ _OBJC_IVAR_$_PBFPosterExtensionDataStore._publishedLock_lockScreenPosterCollection
+ _OBJC_IVAR_$_PBFPosterExtensionDataStore._publishedLock_roleToGalleryConfiguration
+ _OBJC_IVAR_$_PBFPosterExtensionDataStore._publishedLock_switcherConfiguration
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreXPCServiceGlue._loaderQueue
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreXPCServiceGlue._lock_holdsLoadedDataStore
+ _OBJC_IVAR_$_PBFPosterExtensionDataStoreXPCServiceGlue._monitorLock_loadedDataStore
+ _OBJC_IVAR_$_PBFPosterModelStoreCoordinator._skipsMigrationSupplementCreation
+ _OBJC_IVAR_$_PBFPosterSnapshotDefinition._disallowsFilesystemCompression
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_bundleCompressionRaiserForTesting
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_bundleCompressorForTesting
+ _OBJC_IVAR_$_PBFPosterSnapshotManager._lock_compressionsByPUIRequest
+ _OBJC_IVAR_$_PBFPosterSnapshotPBFRequestTracker._lock_countedInProgressContexts
+ _OBJC_IVAR_$_PBFPosterStoreSeed._lockScreenPosterCollection
+ _OBJC_IVAR_$_PBFPosterStoreSeed._switcherConfiguration
+ _OBJC_IVAR_$__PBFPosterSnapshotCompression._bundleURL
+ _OBJC_IVAR_$__PBFPosterSnapshotCompression._qos
+ _OBJC_METACLASS_$_PBFPosterStoreSeed
+ _OBJC_METACLASS_$__PBFPosterSnapshotCompression
+ _PBFLogKeyForPath
+ _PUIAFSCCompressBundleAtURLWithQoS
+ _PUIAFSCPrefaultFileIfCompressed
+ _PUIAFSCRaiseBundleCompressionQoS
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PRMutablePosterTitleStyleConfiguration_$_PBFAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PRPosterTitleStyleConfiguration_$_PBFAdditions
+ __OBJC_$_CATEGORY_PRMutablePosterTitleStyleConfiguration_$_PBFAdditions
+ __OBJC_$_CATEGORY_PRPosterTitleStyleConfiguration_$_PBFAdditions
+ __OBJC_$_CLASS_METHODS_PBFPosterStoreSeed
+ __OBJC_$_INSTANCE_METHODS_PBFPosterStoreSeed
+ __OBJC_$_INSTANCE_METHODS__PBFPosterSnapshotCompression
+ __OBJC_$_INSTANCE_VARIABLES_PBFPosterStoreSeed
+ __OBJC_$_INSTANCE_VARIABLES__PBFPosterSnapshotCompression
+ __OBJC_$_PROP_LIST_PBFPosterStoreSeed
+ __OBJC_$_PROP_LIST__PBFPosterSnapshotCompression
+ __OBJC_CLASS_RO_$_PBFPosterStoreSeed
+ __OBJC_CLASS_RO_$__PBFPosterSnapshotCompression
+ __OBJC_METACLASS_RO_$_PBFPosterStoreSeed
+ __OBJC_METACLASS_RO_$__PBFPosterSnapshotCompression
+ ___108-[PBFPosterSnapshotManager _findReplacementForRemovedBundleOfPUIRequest:path:removedReservation:completion:]_block_invoke
+ ___126-[PBFPosterSnapshotManager _compressBundleAtURL:qos:thenCompletePUIRequest:imageURL:snapshotBundle:path:compressorForTesting:]_block_invoke
+ ___48-[PBFPosterSnapshotManager snapshotsForRequest:]_block_invoke_2
+ ___59-[PBFPosterExtensionDataStore _rolesWithGalleryWorkEnabled]_block_invoke
+ ___63+[PBFPosterStoreSeed _readSeedForBaseURL:outcome:reason:error:]_block_invoke
+ ___67-[PBFPosterExtensionDataStoreXPCServiceGlue _updatePinnedDisplays:]_block_invoke_2
+ ___70-[PBFPosterExtensionDataStore _hasPendingProactiveSnapshotRefreshWork]_block_invoke
+ ___73-[PBFPosterExtensionDataStoreXPCServiceGlue loadDataStoreWithCompletion:]_block_invoke
+ ___74-[PBFPosterSnapshotManager _enqueueSnapshotForRequestIfNeeded:completion:]_block_invoke_4
+ ___84-[PBFPosterSnapshotManager _submitSnapshotRequest:fulfilledReservations:completion:]_block_invoke
+ ___84-[PBFPosterSnapshotManager _submitSnapshotRequest:fulfilledReservations:completion:]_block_invoke_2
+ ___88-[PBFPosterSnapshotManager _finishCompressionOfPUIRequest:imageURL:snapshotBundle:path:]_block_invoke
+ ___95-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_updatePinnedDisplays:embeddedDisplayContext:]_block_invoke
+ ___98+[PBFPosterRoleCoordinator posterCollectionForRole:storage:sortedPosterUUIDs:posterForUUID:error:]_block_invoke
+ ___98+[PBFPosterRoleCoordinator posterCollectionForRole:storage:sortedPosterUUIDs:posterForUUID:error:]_block_invoke_2
+ ___98+[PBFPosterRoleCoordinator posterCollectionForRole:storage:sortedPosterUUIDs:posterForUUID:error:]_block_invoke_3
+ ___98+[PBFPosterRoleCoordinator posterCollectionForRole:storage:sortedPosterUUIDs:posterForUUID:error:]_block_invoke_4
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e52_"PRPosterConfiguration"24?0"NSUUID"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32w_e71_v32?0"PBFPosterSnapshotContext"8"PBFPosterSnapshotReservation"16^B24lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e16_16?0"NSUUID"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e26_"NSString"16?0"NSUUID"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e52_"PRPosterConfiguration"24?0"NSUUID"8"NSString"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e71_v32?0"PBFPosterSnapshotContext"8"PBFPosterSnapshotReservation"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e66_v32?0"PBFPosterSnapshotContext"8"PUIPosterSnapshotBundle"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e67_v32?0"PBFPosterSnapshotContext"8"PUIPosterSnapshotRequest"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e38_v16?0"PBFPosterSnapshotReservation"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56w64w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8w64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72w_e20_v24?0Q8"NSError"16ls32l8w72l8s40l8s48l8s56l8s64l8
+ ___swift_closure_destructor.116Tm
+ ___swift_closure_destructor.122Tm
+ ___swift_closure_destructor.151Tm
+ ___swift_closure_destructor.153Tm
+ ___swift_closure_destructor.158Tm
+ ___swift_closure_destructor.166Tm
+ ___swift_closure_destructor.168Tm
+ ___swift_closure_destructor.210Tm
+ ___swift_closure_destructor.467Tm
+ ___swift_closure_destructor.477Tm
+ ___swift_closure_destructor.48Tm
+ ___swift_closure_destructor.502Tm
+ ___swift_closure_destructor.55Tm
+ ___swift_closure_destructor.672Tm
+ ___swift_closure_destructor.798Tm
+ ___swift_closure_destructor.91Tm
+ ___swift_closure_destructor.94Tm
+ _dispatch_queue_attr_make_with_qos_class
+ _kCBTelemetryTriggers_block_invoke.uuid_str
+ _kPBFDataStoreReadyMarkerFileName_block_invoke.timerSource
+ _os_unfair_recursive_lock_lock
+ _symbolic $s11PosterBoard0A17StoreDataProviderP
+ _symbolic Say______pGSg So17PBFDisplayContextP
+ _symbolic SayyycG
+ _symbolic Shy_____G So36PRPosterSnapshotDefinitionIdentifiera
+ _symbolic So18PRPosterCollectionCSg
+ _symbolic So23PRSwitcherConfigurationCSg
+ _symbolic So24PBFGenericDisplayContextC
+ _symbolic So27PBFPosterExtensionDataStoreCSg
+ _symbolic _____ 11PosterBoard010LockScreenA18CollectionViewCellC16LiveAdaptiveTimeV
+ _symbolic _____ 11PosterBoard0A28RackCollectionViewControllerC18CenteredCardAnchor33_D5DF376170FC49163D52DD3549B6CC17LLO
+ _symbolic _____Sg 11PosterBoard010LockScreenA18CollectionViewCellC16LiveAdaptiveTimeV
+ _symbolic _____Sg 11PosterBoard0A28RackCollectionViewControllerC18CenteredCardAnchor33_D5DF376170FC49163D52DD3549B6CC17LLO
+ _symbolic _____SgXw 11PosterBoard0A5StoreC
+ _symbolic _____SgXwz_Xx 11PosterBoard0A5StoreC
+ _symbolic ______p 11PosterBoard0A17StoreDataProviderP
+ _symbolic _____yyycG s23_ContiguousArrayStorageC
+ _type_layout_string 11PosterBoard010LockScreenA18CollectionViewCellC16LiveAdaptiveTimeV
+ _type_layout_string 11PosterBoard0A28RackCollectionViewControllerC18CenteredCardAnchor33_D5DF376170FC49163D52DD3549B6CC17LLO
- -[PBFPosterExtensionDataStoreXPCServiceGlue _lock_updatePinnedDisplays:]
- -[PBFPosterExtensionDataStoreXPCServiceGlue server:restoreArchivedDataStoreNamed:backupExistingDataStore:completion:]
- -[PRPosterTitleStyleConfiguration(PBFCompactTimeFont) pbf_effectiveCompactTimeFontWithExtensionBundleURL:forRole:displayContext:]
- -[_PBFPosterExtensionDataStoreSQLiteDatabaseImpl initWithURL:options:error:]
- GCC_except_table108
- GCC_except_table120
- GCC_except_table121
- GCC_except_table127
- GCC_except_table143
- GCC_except_table153
- GCC_except_table158
- GCC_except_table160
- GCC_except_table164
- GCC_except_table177
- GCC_except_table178
- GCC_except_table181
- GCC_except_table184
- GCC_except_table187
- GCC_except_table229
- GCC_except_table256
- GCC_except_table266
- GCC_except_table349
- GCC_except_table356
- GCC_except_table358
- GCC_except_table380
- GCC_except_table394
- GCC_except_table405
- GCC_except_table428
- GCC_except_table438
- GCC_except_table443
- GCC_except_table446
- GCC_except_table463
- GCC_except_table480
- GCC_except_table481
- GCC_except_table482
- GCC_except_table484
- GCC_except_table93
- GCC_except_table97
- _OBJC_IVAR_$_PBFPosterExtensionDataStore._stateLock_roleToGalleryConfiguration
- _OBJC_IVAR_$_PBFPosterExtensionDataStore._stateLock_switcherConfiguration
- _PBFPosterExtensionDataStoreDidTearDownNotification_block_invoke.timerSource
- _PUIAFSCEnqueueCompressionForURL
- __OBJC_$_CATEGORY_INSTANCE_METHODS_PRPosterTitleStyleConfiguration_$_PBFCompactTimeFont
- __OBJC_$_CATEGORY_PRPosterTitleStyleConfiguration_$_PBFCompactTimeFont
- ___48-[PBFPosterExtensionStoreCoordinator invalidate]_block_invoke
- ___62-[PBFPosterSnapshotManager _submitSnapshotRequest:completion:]_block_invoke
- ___64-[PBFPosterRoleCoordinator buildNewPosterCollectionFromStorage:]_block_invoke_2
- ___72-[PBFPosterExtensionDataStoreXPCServiceGlue _lock_updatePinnedDisplays:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e67_v32?0"PBFPosterSnapshotContext"8"PUIPosterSnapshotRequest"16^B24ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s_e47_v32?0"NSString"8"PBFGalleryController"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56w64w_e17_v16?0"NSArray"8lw56l8s32l8s40l8w64l8s48l8
- ___swift_closure_destructor.133Tm
- ___swift_closure_destructor.136Tm
- ___swift_closure_destructor.145Tm
- ___swift_closure_destructor.152Tm
- ___swift_closure_destructor.408Tm
- ___swift_closure_destructor.45Tm
- ___swift_closure_destructor.607Tm
- ___swift_closure_destructor.739Tm
- ___swift_closure_destructor.82Tm
- ___swift_closure_destructor.85Tm
- ___swift_closure_destructor.88Tm
- _kCoreBrightnessDisplayInfoDisplayBuiltIn_block_invoke.uuid_str
- _os_unfair_recursive_lock_lock_with_options
- _symbolic So23PRSwitcherConfigurationC
- _symbolic So41PBFPosterExtensionDataStoreXPCServiceGlueC
- _symbolic _____11orientation______6heightt So22UIInterfaceOrientationV 12CoreGraphics7CGFloatV
CStrings:
+ "![self publishedSwitcherConfiguration]"
+ "%@ phase %@ skipped; gallery work disabled"
+ "%@|%lu"
+ "'%@' is not a data store archive name."
+ "(%{public}@) phase %{public}@ bail asking for new gallery; gallery work is disabled for every role"
+ "(%{public}@) phase %{public}@ gallery work is disabled for every role; nothing to snapshot"
+ "(%{public}s) Skipping gallery update for role %{public}@; gallery work is disabled, reason: %{public}@"
+ "(_stateLock_buildSwitcherConfigurationWithContext...) Can't build switcher configuration yet: role setup hasn't run"
+ "-[PBFPosterExtensionDataStoreXPCServiceGlue _baseDataStoreURL:logsMigrationStatus:]"
+ "@\"NSString\"16@?0@\"NSUUID\"8"
+ "@\"PRPosterConfiguration\"24@?0@\"NSUUID\"8@\"NSString\"16"
+ "AFSC completing %{public}@ with the snapshot that replaced its removed bundle"
+ "AFSC compressed %lu file(s) for %{public}@ in %.1fms; completing"
+ "AFSC compressed nothing for %{public}@ in %.1fms; completing"
+ "AFSC failed for %{public}@ after compressing %lu file(s) in %.1fms; completing with what is on disk: %{public}@"
+ "AFSC finished for %{public}@ after its requests were cancelled; dropping it"
+ "AFSC finished for %{public}@ after the manager was invalidated; failing %lu waiter(s)"
+ "AFSC finished for %{public}@ but its bundle is gone: %{public}@"
+ "AFSC finished for %{public}@, which wasn't compressing"
+ "AFSC found nothing to replace the removed bundle of %{public}@; completing with an error: %{public}@"
+ "AFSC has no snapshot cache to replace the removed bundle of %{public}@; completing with an error"
+ "AFSC raising the compression of %{public}@ to QoS %#x for a request that joined it"
+ "AFSC skipped for %{public}@: definition %{public}@ disallows filesystem compression"
+ "AFSC skipped for %{public}@: the snapshot bundle has no URL"
+ "An archived data store named '%@' already exists."
+ "CreateAFaceShuffle"
+ "DataStoreReadyMarker"
+ "Failed to find path, provider or index for configuring poster pair: %@"
+ "Gallery controller requested snapshot prewarm for role %{public}@, but gallery work is disabled; deferring snapshot work; newlyAdded=%{BOOL}u"
+ "Gallery work is disabled for role %{public}@. Not pushing descriptors to proactive."
+ "Imported archived data store %{public}@ (%lu bytes)"
+ "Index LRU entry points to a bundle that is gone: %{public}@"
+ "PosterBoard.PosterStore"
+ "PosterStore dropped deletion of %s: no live configuration"
+ "PosterStore dropped home poster %@: no data store"
+ "PosterStore dropped persist of %@: no data store"
+ "PosterStore dropped selection of %s: no live configuration"
+ "PosterStore dropped update of %s: no live configuration"
+ "PosterStore has no data store"
+ "PosterStore off-main load failed; keeping the seed or placeholder"
+ "PosterStore seed: base URL raised: %{public}@"
+ "PosterStore seed: outcome=%ld reason=%{public}@ error=%{public}@/%ld posters=%lu"
+ "PosterStoreSeedInFlight"
+ "Refresh-if-necessary for role '%{public}@' (%{public}@): gallery work is disabled, no-op"
+ "Removing the ready marker raised: %{public}@"
+ "Resetting migration state for restored data store %{public}@: %{public}@"
+ "StandBy user setting at launch: ambient gallery work %{public}@"
+ "The snapshot bundle was removed while it was being compressed."
+ "[_migrateConfigurations] Could not finalize the ambient configuration migration on its own: %{public}@"
+ "[_migrateConfigurations] Firing postersMigrated event with %lu configurations (%lu requested, anyFailed: %{BOOL}u)"
+ "[_migrateConfigurations] Not firing postersMigrated (no migration requests); bailing."
+ "[_migrateConfigurations] Raised while concluding the ambient configuration migration: %{public}@"
+ "[_migrateConfigurations] Setting ambientMigrationVersion to %ld directly; finalizing did not."
+ "[performConfigurationMigrations] Marking %{public}@ as migrated to version %ld even though %lu configuration(s) failed; failed configurations are left unmigrated and will not be retried"
+ "[performConfigurationMigrations] Out of migration budget (%.1fs left, need %.0fs); could NOT finish configuration %{public}@ for %{public}@ — leaving it unmigrated"
+ "ambientConfigurationVersion"
+ "blockingDataStore: build failed: %{public}@"
+ "breaker not armed"
+ "cancelRequests: PUI request %{public}@ is orphaned while its bundle compresses; dropping it when that ends"
+ "com.apple.PosterBoard.PBFPosterExtensionDataStoreXPCServiceGlue.loader"
+ "conclude ambient configuration migration"
+ "disabled"
+ "disallowsFilesystemCompression"
+ "enabled"
+ "gallery work disabled; snapshot prewarm requested (reason: %@)"
+ "isActive"
+ "keeping snapshot manager assertions while %lu bundle(s) compress"
+ "marker from another build"
+ "no marker"
+ "no posters"
+ "no selection"
+ "off for this build"
+ "read died in this boot"
+ "selection not listed"
+ "snapshotsForRequest: a render or compression started during the cache read for request %{public}@; the enqueue path will finish it"
+ "torn down during read"
+ "v16@?0@\"PBFPosterSnapshotReservation\"8"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@?0@\"PBFPosterSnapshotContext\"8@\"PBFPosterSnapshotReservation\"16^B24"
+ "v32@?0@\"PBFPosterSnapshotContext\"8@\"PUIPosterSnapshotBundle\"16^B24"
- "!_stateLock_switcherConfiguration"
- "-[PBFPosterExtensionDataStoreXPCServiceGlue _baseDataStoreURL:]"
- "<%p> [_enqueueSnapshotForRequestIfNeeded]: [remainingRequests count]: %lu. [request identifier]: %@"
- "Failed to find path or provider for configuring poster pair: %@"
- "[_migrateConfigurations] Firing postersMigrated event with %lu configurations"
- "[_migrateConfigurations] Not firing postersMigrated (%lu requested, %lu migrated, anyFailed: %{BOOL}u); bailing."
- "[performConfigurationMigrations] NOT marking %{public}@ as migrated to version %ld; at least one configuration failed and will be retried on the next migration"
- "[performConfigurationMigrations] Out of migration budget (%.1fs left, need %.0fs); could NOT finish configuration %{public}@ for %{public}@ — will retry next migration"
- "_lock_teardownDataStore: applicationRootNode cancel raised: %{public}@"
- "_lock_teardownDataStore: applicationStateMonitor invalidate raised: %{public}@"
```
