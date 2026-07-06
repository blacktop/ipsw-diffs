## PosterBoard

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterBoard.framework/Versions/A/PosterBoard`

```diff

-  __TEXT.__text: 0x1be0b0
-  __TEXT.__objc_methlist: 0xc4f4
-  __TEXT.__const: 0x55c4
-  __TEXT.__gcc_except_tab: 0x3f4c
-  __TEXT.__cstring: 0x1128e
-  __TEXT.__oslogstring: 0x18222
-  __TEXT.__ustring: 0x62
+  __TEXT.__text: 0x1c0720
+  __TEXT.__objc_methlist: 0xc64c
+  __TEXT.__const: 0x55b4
+  __TEXT.__gcc_except_tab: 0x3f14
+  __TEXT.__cstring: 0x1152e
+  __TEXT.__oslogstring: 0x18ba2
   __TEXT.__dlopen_cstrs: 0x150
+  __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x5bbc
   __TEXT.__constg_swiftt: 0x4014
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_reflstr: 0x2dc5
-  __TEXT.__swift5_fieldmd: 0x20d8
+  __TEXT.__swift5_fieldmd: 0x20e4
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_proto: 0x1ac
   __TEXT.__swift5_types: 0x1b8

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0x51e8
+  __TEXT.__unwind_info: 0x5258
   __TEXT.__eh_frame: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x47a0
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x500
+  __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f68
+  __DATA_CONST.__objc_selrefs: 0x8000
   __DATA_CONST.__objc_protorefs: 0x208
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x120
-  __DATA_CONST.__got: 0x18c0
-  __AUTH_CONST.__const: 0x5498
-  __AUTH_CONST.__cfstring: 0xafe0
-  __AUTH_CONST.__objc_const: 0x2e6b0
+  __DATA_CONST.__got: 0x18e8
+  __AUTH_CONST.__const: 0x54b8
+  __AUTH_CONST.__cfstring: 0xb200
+  __AUTH_CONST.__objc_const: 0x2ec10
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f18
-  __AUTH.__objc_data: 0x2ac0
-  __AUTH.__data: 0xb20
-  __DATA.__objc_ivar: 0xe40
-  __DATA.__data: 0x49d0
-  __DATA.__bss: 0x2788
-  __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0x4e20
-  __DATA_DIRTY.__data: 0xb10
-  __DATA_DIRTY.__bss: 0x1020
-  __DATA_DIRTY.__common: 0x28
+  __AUTH_CONST.__auth_got: 0x1f20
+  __AUTH.__objc_data: 0x29d0
+  __AUTH.__data: 0xa70
+  __DATA.__objc_ivar: 0xe60
+  __DATA.__data: 0x4980
+  __DATA.__bss: 0x2728
+  __DATA.__common: 0xa0
+  __DATA_DIRTY.__objc_data: 0x4f68
+  __DATA_DIRTY.__data: 0xc60
+  __DATA_DIRTY.__bss: 0x10a0
+  __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8120
-  Symbols:   15693
-  CStrings:  4722
+  Functions: 8152
+  Symbols:   15782
+  CStrings:  4778
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[PBFGenericDisplayContext _embeddedDisplayContext]
+ +[PBFGenericDisplayContext augmentDisplayContexts:forRole:userInterfaceStyles:]
+ +[PBFGenericDisplayContext defaultPinnedDisplayContexts]
+ +[PBFGenericDisplayContext displayConfigurationsByType]
+ +[PBFGenericDisplayContext displayContextFromFBSDisplayConfiguration:]
+ +[PBFGenericDisplayContext embeddedDisplayConfiguration]
+ -[PBFGalleryController _notifyGalleryControllerDidRequestSnapshotRefreshForReason:]
+ -[PBFGalleryViewController initWithNibName:bundle:]
+ -[PBFGenericDisplayContext _lock_displayContextPersistenceIdentifier]
+ -[PBFGenericDisplayContext _lock_hash]
+ -[PBFPendingProactiveSnapshotRefreshPersistence .cxx_destruct]
+ -[PBFPendingProactiveSnapshotRefreshPersistence initWithUserDefaults:]
+ -[PBFPendingProactiveSnapshotRefreshPersistence init]
+ -[PBFPendingProactiveSnapshotRefreshPersistence roles]
+ -[PBFPendingProactiveSnapshotRefreshPersistence setRoles:]
+ -[PBFPosterExtensionDataStore _addPendingProactiveSnapshotRefreshRole:reason:]
+ -[PBFPosterExtensionDataStore _hasPendingProactiveSnapshotRefreshWork]
+ -[PBFPosterExtensionDataStore _kickGallerySnapshotRefreshForRole:powerLogReason:completion:]
+ -[PBFPosterExtensionDataStore _kickGallerySnapshotRefreshFromPendingProactiveRequestsIfNecessary:powerLogReason:context:]
+ -[PBFPosterExtensionDataStore _removePendingProactiveSnapshotRefreshRole:reason:]
+ -[PBFPosterExtensionDataStore _stateLock_savePendingProactiveSnapshotRefreshRoles]
+ -[PBFPosterExtensionDataStore _test_buildSwitcherConfigurationWithContext:]
+ -[PBFPosterExtensionDataStore _test_clearPendingProactiveSnapshotRefreshRoles]
+ -[PBFPosterExtensionDataStore _test_pendingProactiveSnapshotRefreshRoles]
+ -[PBFPosterExtensionDataStore _test_setGalleryConfiguration:forRole:]
+ -[PBFPosterExtensionDataStore _test_setHasBeenUnlockedSinceBoot:]
+ -[PBFPosterExtensionDataStore _test_setIsPrewarming:]
+ -[PBFPosterExtensionDataStore _test_setLastPrewarmRun:]
+ -[PBFPosterExtensionDataStore _test_setPendingProactiveSnapshotRefreshPersistence:]
+ -[PBFPosterExtensionDataStore galleryControllerDidRequestSnapshotRefresh:powerLogReason:]
+ -[PBFPosterGalleryPreviewViewController initWithRole:]
+ -[PBFPosterGalleryPreviewViewController role]
+ -[_PBFGalleryCollectionViewController initWithCollectionViewLayout:role:]
+ -[_PBFGalleryCollectionViewController role]
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table129
+ GCC_except_table140
+ GCC_except_table150
+ GCC_except_table161
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table223
+ GCC_except_table257
+ GCC_except_table340
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table369
+ GCC_except_table382
+ GCC_except_table411
+ GCC_except_table425
+ GCC_except_table442
+ GCC_except_table443
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table55
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table88
+ OBJC_IVAR_$_PBFGalleryViewController._role
+ OBJC_IVAR_$_PBFGenericDisplayContext._lock
+ OBJC_IVAR_$_PBFPendingProactiveSnapshotRefreshPersistence._userDefaults
+ OBJC_IVAR_$_PBFPosterExtensionDataStore._pendingProactiveSnapshotRefreshPersistence
+ OBJC_IVAR_$_PBFPosterExtensionDataStore._stateLock_drainingProactiveSnapshotRefreshRoles
+ OBJC_IVAR_$_PBFPosterExtensionDataStore._stateLock_pendingProactiveSnapshotRefreshRoles
+ OBJC_IVAR_$_PBFPosterGalleryPreviewViewController._role
+ OBJC_IVAR_$__PBFGalleryCollectionViewController._role
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_PBFPendingProactiveSnapshotRefreshPersistence
+ _OBJC_METACLASS_$_PBFPendingProactiveSnapshotRefreshPersistence
+ _PBFSnapshotDefinitionEnumerateSupportedOrientationsForCurrentDeviceClassAndRole
+ _PBFSnapshotDefinitionEnumerateSupportedOrientationsForDeviceClassAndRole
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole.onceToken
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole.padSupportedOrientations
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole.phoneAmbientSupportedOrientations
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole.phoneSupportedOrientations
+ _PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole.tvSupportedOrientations
+ __92-[PBFPosterExtensionDataStore _kickGallerySnapshotRefreshForRole:powerLogReason:completion:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_$_INSTANCE_VARIABLES_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_$_PROP_LIST_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_$_PROP_LIST_PBFPendingProactiveSnapshotRefreshPersisting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBFPendingProactiveSnapshotRefreshPersisting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PBFPendingProactiveSnapshotRefreshPersisting
+ __OBJC_$_PROTOCOL_REFS_PBFPendingProactiveSnapshotRefreshPersisting
+ __OBJC_CLASS_PROTOCOLS_$_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_CLASS_RO_$_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_LABEL_PROTOCOL_$_PBFPendingProactiveSnapshotRefreshPersisting
+ __OBJC_METACLASS_RO_$_PBFPendingProactiveSnapshotRefreshPersistence
+ __OBJC_PROTOCOL_$_PBFPendingProactiveSnapshotRefreshPersisting
+ __PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole
+ ___55+[PBFGenericDisplayContext displayConfigurationsByType]_block_invoke
+ ___73-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:role:]_block_invoke
+ ___73-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:role:]_block_invoke_2
+ ___79+[PBFGenericDisplayContext augmentDisplayContexts:forRole:userInterfaceStyles:]_block_invoke
+ ___92-[PBFPosterExtensionDataStore _kickGallerySnapshotRefreshForRole:powerLogReason:completion:]_block_invoke
+ ___92-[PBFPosterExtensionDataStore _kickGallerySnapshotRefreshForRole:powerLogReason:completion:]_block_invoke_2
+ ___PBFSnapshotDefinitionEnumerateSupportedOrientationsForDeviceClassAndRole_block_invoke
+ ____PBFSnapshotDefinitionSupportedOrientationsForDeviceClassAndRole_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96w_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8w96l8s88l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96w_e33_v16?0"PBFGalleryConfiguration"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8w96l8s88l8
+ ___block_descriptor_48_e8_32s40s_e5_q8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e17_v16?0"NSError"8lw72l8s32l8s40l8s48l8s56l8s64l8
+ __swift_closure_destructor.137Tm
+ __swift_closure_destructor.226Tm
+ _objc_msgSend$_addPendingProactiveSnapshotRefreshRole:reason:
+ _objc_msgSend$_embeddedDisplayContext
+ _objc_msgSend$_hasPendingProactiveSnapshotRefreshWork
+ _objc_msgSend$_kickGallerySnapshotRefreshForRole:powerLogReason:completion:
+ _objc_msgSend$_kickGallerySnapshotRefreshFromPendingProactiveRequestsIfNecessary:powerLogReason:context:
+ _objc_msgSend$_lock_displayContextPersistenceIdentifier
+ _objc_msgSend$_lock_hash
+ _objc_msgSend$_notifyGalleryControllerDidRequestSnapshotRefreshForReason:
+ _objc_msgSend$_removePendingProactiveSnapshotRefreshRole:reason:
+ _objc_msgSend$_stateLock_savePendingProactiveSnapshotRefreshRoles
+ _objc_msgSend$augmentDisplayContexts:forRole:userInterfaceStyles:
+ _objc_msgSend$defaultPinnedDisplayContexts
+ _objc_msgSend$displayConfigurationsByType
+ _objc_msgSend$displayContextFromFBSDisplayConfiguration:
+ _objc_msgSend$embeddedDisplayConfiguration
+ _objc_msgSend$galleryControllerDidRequestSnapshotRefresh:powerLogReason:
+ _objc_msgSend$initWithCollectionViewLayout:role:
+ _objc_msgSend$initWithDataProvider:role:
+ _objc_msgSend$initWithRole:
+ _objc_msgSend$initWithUserDefaults:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$roles
+ _objc_msgSend$setRoles:
+ _type_layout_string So12PRPosterRolea
+ displayConfigurationsByType.configurationsByType
+ displayConfigurationsByType.lock
+ displayConfigurationsByType.onceToken
- -[PBFGalleryController _notifyGalleryControllerDidRequestSnapshotRefresh]
- -[PBFPosterExtensionDataStore _buildSwitcherConfigurationWithContext:]
- -[PBFPosterExtensionDataStore galleryControllerDidRequestSnapshotRefresh:]
- -[PBFPosterExtensionDataStore pbf_test_setGalleryConfiguration:forRole:]
- -[PBFPosterExtensionDataStore pbf_test_setHasBeenUnlockedSinceBoot:]
- -[PBFPosterExtensionDataStore pbf_test_setLastPrewarmRun:]
- -[PBFPosterGalleryPreviewViewController initWithNibName:bundle:]
- -[_PBFGalleryCollectionViewController initWithCollectionViewLayout:]
- GCC_except_table1
- GCC_except_table123
- GCC_except_table134
- GCC_except_table142
- GCC_except_table145
- GCC_except_table157
- GCC_except_table174
- GCC_except_table177
- GCC_except_table219
- GCC_except_table252
- GCC_except_table330
- GCC_except_table337
- GCC_except_table339
- GCC_except_table362
- GCC_except_table375
- GCC_except_table404
- GCC_except_table418
- GCC_except_table435
- GCC_except_table57
- GCC_except_table63
- GCC_except_table67
- _PBFSnapshotDefinitionEnumerateSupportedOrientationsForCurrentDeviceClass
- _PBFSnapshotDefinitionEnumerateSupportedOrientationsForDeviceClass
- _PBFSnapshotDefinitionSupportedOrientationForDeviceClass
- _PBFSnapshotDefinitionSupportedOrientationForDeviceClass.onceToken
- _PBFSnapshotDefinitionSupportedOrientationForDeviceClass.padSupportedOrientations
- _PBFSnapshotDefinitionSupportedOrientationForDeviceClass.phoneSupportedOrientations
- _PBFSnapshotDefinitionSupportedOrientationForDeviceClass.tvSupportedOrientations
- __140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke_2
- __74-[PBFPosterExtensionDataStore galleryControllerDidRequestSnapshotRefresh:]_block_invoke
- __PBFSnapshotDefinitionSupportedOrientationForDeviceClass
- ___140-[PBFPosterExtensionDataStore executeUpdate:hostContext:refreshStrategy:galleryUpdateOptions:powerLogReason:cleanupOldResources:completion:]_block_invoke_2
- ___154-[PBFPosterExtensionDataStore _stateLock_pushUpdateNotificationsForRole:diff:previouslyActiveConfiguration:newActiveConfiguration:options:reason:context:]_block_invoke_4
- ___189-[PBFPosterExtensionDataStore _processGalleryItemRequestsMatchingDescriptorIdentifier:extensionIdentifier:displayContexts:role:loadFromCacheIfAvailable:intention:powerLogReason:completion:]_block_invoke_3
- ___68-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:]_block_invoke
- ___68-[_PBFGalleryCollectionViewController initWithCollectionViewLayout:]_block_invoke_2
- ___74-[PBFPosterExtensionDataStore galleryControllerDidRequestSnapshotRefresh:]_block_invoke
- ___83-[PBFPosterExtensionDataStore importPosterConfigurationFromArchiveData:completion:]_block_invoke_2
- ___89-[PBFPosterExtensionDataStore refreshSnapshotForPosterConfigurationMatchUUID:completion:]_block_invoke_4
- ___PBFSnapshotDefinitionEnumerateSupportedOrientationsForDeviceClass_block_invoke
- ____PBFSnapshotDefinitionSupportedOrientationForDeviceClass_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8s40l8s48l8r56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e33_v16?0"PBFGalleryConfiguration"8ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8s64l8s72l8r88l8s80l8
- __swift_closure_destructor.136Tm
- __swift_closure_destructor.225Tm
- _objc_msgSend$_notifyGalleryControllerDidRequestSnapshotRefresh
- _objc_msgSend$displayContextForDisplayIdentifier:
- _objc_msgSend$galleryControllerDidRequestSnapshotRefresh:
- _objc_msgSend$galleryPrewarmPolicy
- _objc_msgSend$initWithDataProvider:
- _objc_msgSend$maxPerSectionToPrewarm
- _objc_msgSend$maxTotalItemsToPrewarm
- _objc_msgSend$skipFirstSection
- _type_layout_string So36PRPosterSnapshotDefinitionIdentifiera
CStrings:
+ "%@ phase %@ no requests to fan out"
+ "%@ phase %@ snapshot fanout success"
+ "(%{public}@) data is fresh, but pending proactive snapshot-refresh roles exist; proceeding so the deferred work can run"
+ "(%{public}@) phase %{public}@ role %{public}@ galleryConfiguration has %lu sections, %lu display contexts to process"
+ "(%{public}@) phase %{public}@ role %{public}@ no snapshot requests to prewarm - all fulfilled or none generated"
+ "(%{public}@) phase %{public}@ role %{public}@ prewarmSnapshotsForRequests completed successfully for %lu requests"
+ "(%{public}@) phase %{public}@ role %{public}@ prewarmSnapshotsForRequests completed with error: %{public}@"
+ "(%{public}@) phase %{public}@ role %{public}@ prewarming gallery snapshots: %lu total requests"
+ "Added pending proactive snapshot refresh for role %{public}@ — reason: %{public}@"
+ "Failed to prewarm gallery snapshots for role %{public}@: exceeded prewarm time; invalidating runtime assertion."
+ "Found %lu role(s) with deferred proactive snapshot refresh from previous session: %{public}@"
+ "Gallery controller requested snapshot prewarm for role: %{public}@ (reason: %{public}@)"
+ "PBFPendingProactiveSnapshotRefreshPersistence.m"
+ "PBFPendingProactiveSnapshotRefreshRoles"
+ "Proactive gallery push for role %{public}@; midPrewarm=%{BOOL}u withinPostPrewarmWindow=%{BOOL}u — proceeding with snapshot fanout."
+ "Proactive gallery push for role %{public}@; not mid-prewarm and outside %.0fs post-prewarm window (last prewarm: %{public}@) — deferring snapshot work; newlyAdded=%{BOOL}u"
+ "Refresh-if-necessary for role '%{public}@' (%{public}@): pending=%{BOOL}u alreadyDraining=%{BOOL}u → %{public}@"
+ "Removed pending proactive snapshot refresh for role %{public}@ — reason: %{public}@"
+ "Snapshot fanout exceeded 120s; timed out."
+ "Unable to determine display configurations; bailing"
+ "[%{public}@] Gallery updated; triggering snapshot refresh for gallery items (reason: %{public}@)"
+ "[_checkIfLanguageChangeOccurred] current=%{public}@ vs stashed=%{public}@ -> languageChanged=%d"
+ "[_checkIfLanguageChangeOccurred] no stashed locale identifier; recovering a baseline from the newest usable gallery layout"
+ "[_checkIfLanguageChangeOccurred] sticky pbf_snapshotsLocaleDidChange flag is set; reporting languageChanged=YES"
+ "[_localeDidChange] 1s elapsed without clean exit; force path: xpc_transaction_try_exit_clean() then exit(0)."
+ "[_localeDidChange] Calling xpc_transaction_exit_clean() (armed 1s force-exit fallback)..."
+ "[_localeDidChange] LANGUAGE CHANGE detected (stashed=%{public}@ -> current=%{public}@); tearing down: invalidate dataModel XPC server + cancel data store, then xpc_transaction_exit_clean() to relaunch."
+ "[_localeDidChange] cancelling long-running data store work (acquiring service _lock)..."
+ "[_localeDidChange] data store cancelled; service _lock released."
+ "[_localeDidChange] dataModel XPC server invalidated."
+ "[_localeDidChange] invalidating dataModel XPC server (_server=%{public}@)..."
+ "[_localeDidChange] language unchanged (current=%{public}@ == stashed=%{public}@); NOT tearing down the dataModel XPC server."
+ "[_localeDidChange] notification received: current=%{public}@ stashed=%{public}@ stickyDidChangeFlag=%d -> languageChangeOccurred=%d"
+ "[_localeDidChange] xpc_transaction_exit_clean() RETURNED without exiting (process not yet quiescent); awaiting quiescence or the 1s force-exit timer."
+ "display context could not be hydrated"
+ "displayConfigurationsByType"
+ "displayContextForDisplayIdentifier: no configuration for display identity %{public}@"
+ "displayContextForPRSDisplayInfo: invalid frame %{public}@"
+ "displayContextForWallpaperDisplayPin: no configuration for display identity %{public}@"
+ "displayContextForWallpaperDisplayPin: pin carries neither a configuration nor a display identity"
+ "displayContextFromFBSDisplayConfiguration: invalid geometry referenceBounds=%{public}@ frame=%{public}@ scale=%f"
+ "drain already in flight, no-op"
+ "draining deferred proactive snapshot fanout"
+ "enterPosterSwitcher"
+ "enterPosterSwitcherForRole:'%{public}@' — gallery has %lu items across %lu sections; EMPTY → kicking prewarm"
+ "enterPosterSwitcherForRole:'%{public}@' — gallery has %lu items across %lu sections; populated → checking for deferred proactive snapshot fanout"
+ "kickoff: Provider %{public}@ at capacity (%lu active, cap %lu, visible=%d) — skipping %{public}@"
+ "no pending fanout, no-op"
+ "persistence"
+ "proactive push deferred (lastPrewarmRun=%@)"
+ "role != nil"
+ "snapshot fanout success"
+ "snapshots for %@ cannot be updated until display contexts are available"
+ "unable to ascertain display context for prewarm"
+ "userDefaults"
+ "\xf0\xf0\xf0\xc2"
- "(%{public}@) phase %{public}@ galleryConfiguration has %lu sections, %lu display contexts to process"
- "(%{public}@) phase %{public}@ prewarming gallery snapshots: %lu total requests"
- "Checking current locale: %{public}@ vs stashed locale: %{public}@"
- "EMPTY → kicking prewarm"
- "Gallery controller requested snapshot prewarm for role: %{public}@"
- "Role %{public}@ exceeded prewarm time; invalidating runtime assertion."
- "[%{public}@] Gallery updated; triggering snapshot refresh for gallery items"
- "[_localeDidChange] Calling xpc_transaction_exit_clean()"
- "[_localeDidChange] Locale changes did occur; cancelling long running operation and preparing for xpc_transaction_exit_clean()"
- "[_localeDidChange] Second time calling xpc_transaction_exit_clean()"
- "[_localeDidChange] XPC server invalidated, data store cancelled long running.  Calling xpc_transaction_exit_clean()"
- "displayContextForPRSDisplayInfo: displayContextForDisplayConfiguration returned nil, falling back to scalar construction"
- "enterPosterSwitcherForRole:'%{public}@' — gallery has %lu items across %lu sections; %{public}@"
- "kickoff: Provider %{public}@ at capacity (%lu active), skipping non-visible poster"
- "kickoff: Visible poster %{public}@ bypassing per-provider capacity limit"
- "populated → no-op"
- "prewarmGallerySnapshotRequestsForDisplayContext: %lu total sections, %lu sections for prewarm (skipFirst: %{BOOL}d), maxPerSection: %lu, maxTotal: %lu"
- "prewarmGallerySnapshotRequestsForDisplayContext: reached maxItemsToPrewarm (%lu), stopping early"
- "\xf0\xf0\xf0\xb2"

```
