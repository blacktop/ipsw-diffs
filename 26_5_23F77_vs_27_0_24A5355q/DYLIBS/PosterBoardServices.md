## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-304.5.4.102.0
-  __TEXT.__text: 0x4cdf8
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x3d5c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x4bbc
-  __TEXT.__gcc_except_tab: 0x80c
-  __TEXT.__oslogstring: 0x2759
-  __TEXT.__dlopen_cstrs: 0x2a6
-  __TEXT.__unwind_info: 0x1188
-  __TEXT.__objc_classname: 0x89a
-  __TEXT.__objc_methname: 0xab3c
-  __TEXT.__objc_methtype: 0x1c8b
-  __TEXT.__objc_stubs: 0x63c0
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x1280
-  __DATA_CONST.__objc_classlist: 0x220
+341.0.3.0.0
+  __TEXT.__text: 0x7da28
+  __TEXT.__objc_methlist: 0x52b8
+  __TEXT.__const: 0xb18
+  __TEXT.__cstring: 0x6a9b
+  __TEXT.__gcc_except_tab: 0xfec
+  __TEXT.__oslogstring: 0x37ae
+  __TEXT.__dlopen_cstrs: 0x2f6
+  __TEXT.__swift5_typeref: 0x466
+  __TEXT.__constg_swiftt: 0x1b0
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_reflstr: 0x1c9
+  __TEXT.__swift5_fieldmd: 0x1d4
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x1b30
+  __TEXT.__eh_frame: 0x590
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c50
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fd8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x548
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x37e0
-  __AUTH_CONST.__objc_const: 0xc3e8
+  __DATA_CONST.__objc_selrefs: 0x2bc8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__got: 0x720
+  __AUTH_CONST.__const: 0x8a8
+  __AUTH_CONST.__cfstring: 0x4a20
+  __AUTH_CONST.__objc_const: 0x10920
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x438
-  __DATA.__data: 0x5c0
-  __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x90
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH.__objc_data: 0x10c0
+  __AUTH.__data: 0x128
+  __DATA.__objc_ivar: 0x5c0
+  __DATA.__data: 0xc80
+  __DATA.__bss: 0xcc0
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12FE9A27-6AB2-3E9D-9535-4BC782845C7B
-  Functions: 1813
-  Symbols:   6407
-  CStrings:  2996
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 66BB1E5D-9992-37BA-95BB-863E3BCBB9E4
+  Functions: 2688
+  Symbols:   8482
+  CStrings:  1683
 
Symbols:
+ +[NSError(PRSAdditions) prs_entitlementFailureErrorWithFile:line:entitlement:]
+ +[NSError(PRSAdditions) prs_entitlementFailureErrorWithFile:line:entitlement:].cold.1
+ +[PRSHostConfigurationEntry entryWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:]
+ +[PRSLockScreenColorConfigurationCache sharedCache]
+ +[PRSLockScreenColorConfigurationCache sharedCache].cold.1
+ +[PRSPosterChannel new]
+ +[PRSPosterChannelConfiguration backdropChannelConfigurationForURL:error:]
+ +[PRSPosterChannelConfiguration channelConfigurationForURL:role:error:]
+ +[PRSPosterChannelConfiguration incomingCallChannelConfigurationForURL:error:]
+ +[PRSPosterChannelContext backdropContextWithUserInfo:]
+ +[PRSPosterChannelContext contextWithRole:userInfo:]
+ +[PRSPosterChannelContext incomingCallContextWithUserInfo:]
+ +[PRSPosterChannelContext supportsSecureCoding]
+ +[PRSPosterChannelContext userInfoPersistenceClasses]
+ +[PRSPosterChannelController new]
+ +[PRSPosterChannelGalleryCoordinator new]
+ +[PRSPosterChannelModelCoordinator new]
+ +[PRSPosterConfigurationFinalizer finalizedConfigurationForAttributes:error:]
+ +[PRSPosterConfigurationFinalizer finalizedConfigurationForAttributes:withConfiguredProperties:error:]
+ +[PRSPosterConfigurationFinalizer finalizerErrorWithCode:underlyingError:]
+ +[PRSPosterGallery new]
+ +[PRSWallpaperDisplayPin supportsBSXPCSecureCoding]
+ +[PRSWallpaperDisplayPin supportsSecureCoding]
+ +[_PRSPosterChannelModelMutator new]
+ -[PRSDisplayInfo displayConfiguration]
+ -[PRSDisplayInfo frame]
+ -[PRSDisplayInfo initWithBSXPCCoder:].cold.1
+ -[PRSDisplayInfo initWithCoder:].cold.1
+ -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:displayConfiguration:]
+ -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:displayConfiguration:].cold.1
+ -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:]
+ -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:].cold.1
+ -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:].cold.2
+ -[PRSHostConfigurationEntry migratedConfigurationMatchingMask]
+ -[PRSHostConfigurationEntry setMigratedConfigurationMatchingMask:]
+ -[PRSLockScreenColorConfigurationCache .cxx_destruct]
+ -[PRSLockScreenColorConfigurationCache _osVersionMatchesXattr]
+ -[PRSLockScreenColorConfigurationCache _readEpochFromXattr]
+ -[PRSLockScreenColorConfigurationCache _schemaVersionMatchesXattr]
+ -[PRSLockScreenColorConfigurationCache cachedConfigurationsWithError:]
+ -[PRSLockScreenColorConfigurationCache initWithCachePath:]
+ -[PRSLockScreenColorConfigurationCache init]
+ -[PRSPosterChannel .cxx_destruct]
+ -[PRSPosterChannel _extensionProvider]
+ -[PRSPosterChannel _lock_buildReaper]
+ -[PRSPosterChannel _lock_currentGallery]
+ -[PRSPosterChannel _lock_currentPosterConfiguration]
+ -[PRSPosterChannel _lock_state]
+ -[PRSPosterChannel _notifyObserversDidInvalidate]
+ -[PRSPosterChannel _notifyObserversDidUpdateContext:]
+ -[PRSPosterChannel _notifyObserversDidUpdateGallery:]
+ -[PRSPosterChannel _notifyObserversDidUpdatePoster:]
+ -[PRSPosterChannel _notifyObserversWillInvalidate]
+ -[PRSPosterChannel _notifyObserversWillUpdateContext]
+ -[PRSPosterChannel _notifyObserversWillUpdateGallery]
+ -[PRSPosterChannel _notifyObserversWillUpdatePoster]
+ -[PRSPosterChannel addChannelObserver:]
+ -[PRSPosterChannel appendDescriptionToFormatter:]
+ -[PRSPosterChannel applyUpdater:error:]
+ -[PRSPosterChannel channelContext]
+ -[PRSPosterChannel channelIdentifier]
+ -[PRSPosterChannel coordinateWithRemoveChannelBlock:]
+ -[PRSPosterChannel coordinator:didUpdateContext:]
+ -[PRSPosterChannel coordinator:didUpdateDescriptors:galleryMetadata:]
+ -[PRSPosterChannel coordinator:didUpdatePoster:]
+ -[PRSPosterChannel coordinatorDidInvalidate:]
+ -[PRSPosterChannel coordinatorWillInvalidate:]
+ -[PRSPosterChannel coordinatorWillUpdateContext:]
+ -[PRSPosterChannel coordinatorWillUpdateDescriptors:]
+ -[PRSPosterChannel coordinatorWillUpdatePoster:]
+ -[PRSPosterChannel copyWithZone:]
+ -[PRSPosterChannel creationDate]
+ -[PRSPosterChannel currentGallery]
+ -[PRSPosterChannel description]
+ -[PRSPosterChannel descriptorsForState:]
+ -[PRSPosterChannel extensionInstanceForReason:outError:]
+ -[PRSPosterChannel extensionInstanceForReason:outError:].cold.1
+ -[PRSPosterChannel hash]
+ -[PRSPosterChannel ingestUpdatedDescriptors:forState:galleryMetadata:policy:error:]
+ -[PRSPosterChannel ingestUpdatedDescriptors:forState:policy:error:]
+ -[PRSPosterChannel initWithModelCoordinator:state:error:]
+ -[PRSPosterChannel initWithModelCoordinator:state:error:].cold.1
+ -[PRSPosterChannel initWithModelCoordinator:state:error:].cold.2
+ -[PRSPosterChannel init]
+ -[PRSPosterChannel invalidate]
+ -[PRSPosterChannel lastModifiedDate]
+ -[PRSPosterChannel pooledExtensionInstanceWithError:]
+ -[PRSPosterChannel posterConfiguration]
+ -[PRSPosterChannel reapEverything]
+ -[PRSPosterChannel reapStaleSnapshots]
+ -[PRSPosterChannel reapStaleSnapshots].cold.1
+ -[PRSPosterChannel reapStaleStateOmittingLast:error:]
+ -[PRSPosterChannel relinquishExtensionInstanceForReason:]
+ -[PRSPosterChannel relinquishExtensionInstanceForReason:].cold.1
+ -[PRSPosterChannel relinquishExtensionInstanceForReason:].cold.2
+ -[PRSPosterChannel relinquishPooledExtensionInstance:]
+ -[PRSPosterChannel relinquishPooledExtensionInstance:].cold.1
+ -[PRSPosterChannel removeChannelObserver:]
+ -[PRSPosterChannel setStateCoordinator:]
+ -[PRSPosterChannel stateCoordinator]
+ -[PRSPosterChannel state]
+ -[PRSPosterChannel updateGalleryWithCompletion:]
+ -[PRSPosterChannel updateGalleryWithFetchOptions:]
+ -[PRSPosterChannel updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:]
+ -[PRSPosterChannel updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:completion:]
+ -[PRSPosterChannel updateGallery]
+ -[PRSPosterChannel version]
+ -[PRSPosterChannelConfiguration .cxx_destruct]
+ -[PRSPosterChannelConfiguration URL]
+ -[PRSPosterChannelConfiguration fileManager]
+ -[PRSPosterChannelConfiguration initWithURL:role:error:]
+ -[PRSPosterChannelConfiguration reapOptions]
+ -[PRSPosterChannelConfiguration role]
+ -[PRSPosterChannelConfiguration setReapOptions:]
+ -[PRSPosterChannelContext .cxx_destruct]
+ -[PRSPosterChannelContext _validateUserInfo:badKeys:]
+ -[PRSPosterChannelContext contextByUpdatingUserInfo:]
+ -[PRSPosterChannelContext copyWithZone:]
+ -[PRSPosterChannelContext description]
+ -[PRSPosterChannelContext encodeWithCoder:]
+ -[PRSPosterChannelContext hash]
+ -[PRSPosterChannelContext initWithCoder:]
+ -[PRSPosterChannelContext initWithRole:userInfo:]
+ -[PRSPosterChannelContext initWithRole:userInfo:].cold.1
+ -[PRSPosterChannelContext isEqual:]
+ -[PRSPosterChannelContext role]
+ -[PRSPosterChannelContext userInfo]
+ -[PRSPosterChannelController .cxx_destruct]
+ -[PRSPosterChannelController _fireObserversRespondingToSelector:handler:]
+ -[PRSPosterChannelController addChannelControllerObserver:]
+ -[PRSPosterChannelController addChannelControllerObserver:].cold.1
+ -[PRSPosterChannelController channel:didUpdateGallery:]
+ -[PRSPosterChannelController channelForIdentifier:]
+ -[PRSPosterChannelController channelForIdentifier:completion:]
+ -[PRSPosterChannelController channelForIdentifierIfImmediatelyAvailable:]
+ -[PRSPosterChannelController channelForIdentifierIfImmediatelyAvailable:error:]
+ -[PRSPosterChannelController channelForUUIDFuture]
+ -[PRSPosterChannelController channelFutureForIdentifier:]
+ -[PRSPosterChannelController channelFutureForIdentifier:].cold.1
+ -[PRSPosterChannelController channelsFuture]
+ -[PRSPosterChannelController channelsIfImmediatelyAvailableWithError:]
+ -[PRSPosterChannelController channelsWithCompletion:]
+ -[PRSPosterChannelController channels]
+ -[PRSPosterChannelController configuration]
+ -[PRSPosterChannelController createChannelWithIdentifier:updater:]
+ -[PRSPosterChannelController createChannelWithIdentifier:updater:].cold.1
+ -[PRSPosterChannelController createChannelWithIdentifier:updater:completion:]
+ -[PRSPosterChannelController createModelCoordinatorWithConfiguration:extensionProvider:]
+ -[PRSPosterChannelController handleDidAddChannel:]
+ -[PRSPosterChannelController handleDidRemoveChannel:]
+ -[PRSPosterChannelController handleDidUpdateChannel:]
+ -[PRSPosterChannelController handleWillAddChannel:]
+ -[PRSPosterChannelController handleWillRemoveChannel:]
+ -[PRSPosterChannelController handleWillUpdateChannel:]
+ -[PRSPosterChannelController initWithConfiguration:]
+ -[PRSPosterChannelController initWithConfiguration:].cold.1
+ -[PRSPosterChannelController init]
+ -[PRSPosterChannelController reapEverythingForChannel:]
+ -[PRSPosterChannelController reapEverythingForChannel:].cold.1
+ -[PRSPosterChannelController reapEverythingForChannel:completion:]
+ -[PRSPosterChannelController reapStaleSnapshotsForChannel:]
+ -[PRSPosterChannelController reapStaleSnapshotsForChannel:].cold.1
+ -[PRSPosterChannelController reapStaleSnapshotsForChannel:completion:]
+ -[PRSPosterChannelController reapStaleStateForChannel:completion:]
+ -[PRSPosterChannelController reapStaleStateForChannel:omittingLast:]
+ -[PRSPosterChannelController reapStaleStateForChannel:omittingLast:].cold.1
+ -[PRSPosterChannelController reapStaleStateForChannel:omittingLast:completion:]
+ -[PRSPosterChannelController removeChannel:]
+ -[PRSPosterChannelController removeChannel:completion:]
+ -[PRSPosterChannelController removeChannelControllerObserver:]
+ -[PRSPosterChannelController removeChannelControllerObserver:].cold.1
+ -[PRSPosterChannelController removeChannelWithFuture:]
+ -[PRSPosterChannelController removeChannelWithFuture:].cold.1
+ -[PRSPosterChannelController updateChannel:updater:]
+ -[PRSPosterChannelController updateChannel:updater:].cold.1
+ -[PRSPosterChannelController updateChannel:updater:].cold.2
+ -[PRSPosterChannelController updateChannel:updater:completion:]
+ -[PRSPosterChannelGalleryCoordinator .cxx_destruct]
+ -[PRSPosterChannelGalleryCoordinator _enqueueChannel:fetchOptions:]
+ -[PRSPosterChannelGalleryCoordinator _executeNextTask]
+ -[PRSPosterChannelGalleryCoordinator cancelGalleryFetchForChannelIdentifier:]
+ -[PRSPosterChannelGalleryCoordinator cancelGalleryFetchForChannelIdentifier:].cold.1
+ -[PRSPosterChannelGalleryCoordinator dealloc]
+ -[PRSPosterChannelGalleryCoordinator extensionProvider]
+ -[PRSPosterChannelGalleryCoordinator fetchGalleryForChannel:]
+ -[PRSPosterChannelGalleryCoordinator fetchGalleryForChannel:options:]
+ -[PRSPosterChannelGalleryCoordinator fetchGalleryForChannel:options:].cold.1
+ -[PRSPosterChannelGalleryCoordinator initWithExtensionProvider:]
+ -[PRSPosterChannelGalleryCoordinator initWithExtensionProvider:].cold.1
+ -[PRSPosterChannelGalleryCoordinator init]
+ -[PRSPosterChannelGalleryCoordinator instanceProvider]
+ -[PRSPosterChannelGalleryCoordinator invalidate]
+ -[PRSPosterChannelGalleryCoordinator logPrefix]
+ -[PRSPosterChannelGalleryCoordinator setLogPrefix:]
+ -[PRSPosterChannelGalleryFetchOptions .cxx_destruct]
+ -[PRSPosterChannelGalleryFetchOptions extensionIdentifiers]
+ -[PRSPosterChannelGalleryFetchOptions policy]
+ -[PRSPosterChannelGalleryFetchOptions setExtensionIdentifiers:]
+ -[PRSPosterChannelGalleryFetchOptions setPolicy:]
+ -[PRSPosterChannelGalleryFetchOptions setUpdateSessionInfoProvider:]
+ -[PRSPosterChannelGalleryFetchOptions updateSessionInfoProvider]
+ -[PRSPosterChannelModelCoordinator .cxx_destruct]
+ -[PRSPosterChannelModelCoordinator URL]
+ -[PRSPosterChannelModelCoordinator accessModel:reason:error:]
+ -[PRSPosterChannelModelCoordinator acquireInUseAssertionWithReason:]
+ -[PRSPosterChannelModelCoordinator channelClass]
+ -[PRSPosterChannelModelCoordinator channelPersistenceURLEndpoint]
+ -[PRSPosterChannelModelCoordinator channelPersistenceURLForChannelIdentifier:]
+ -[PRSPosterChannelModelCoordinator channelPersistenceURL]
+ -[PRSPosterChannelModelCoordinator createChannelInstanceWithState:error:]
+ -[PRSPosterChannelModelCoordinator databaseURL]
+ -[PRSPosterChannelModelCoordinator dealloc]
+ -[PRSPosterChannelModelCoordinator extensionProvider]
+ -[PRSPosterChannelModelCoordinator fileManager]
+ -[PRSPosterChannelModelCoordinator fileSystemEndpointForChannelIdentifier:]
+ -[PRSPosterChannelModelCoordinator fileSystemEndpointForChannelIdentifier:].cold.1
+ -[PRSPosterChannelModelCoordinator hash]
+ -[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]
+ -[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.1
+ -[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.2
+ -[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.3
+ -[PRSPosterChannelModelCoordinator init]
+ -[PRSPosterChannelModelCoordinator logPrefix]
+ -[PRSPosterChannelModelCoordinator mutateModel:reason:error:]
+ -[PRSPosterChannelModelCoordinator role]
+ -[PRSPosterChannelModelCoordinator schemaManager]
+ -[PRSPosterChannelModelCoordinator updateGalleryForChannel:fetchOptions:]
+ -[PRSPosterConfiguration(PRSUtilities) prs_posterProvider]
+ -[PRSPosterGallery .cxx_destruct]
+ -[PRSPosterGallery context]
+ -[PRSPosterGallery creationDate]
+ -[PRSPosterGallery description]
+ -[PRSPosterGallery descriptorsForProvider:]
+ -[PRSPosterGallery descriptors]
+ -[PRSPosterGallery initWithContext:descriptors:metadata:]
+ -[PRSPosterGallery init]
+ -[PRSPosterGallery isEqual:]
+ -[PRSPosterGallery isEqualToGallery:]
+ -[PRSPosterGallery providers]
+ -[PRSPosterSnapshotCollection description]
+ -[PRSPosterSnapshotCollection initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayConfiguration:]
+ -[PRSPosterSnapshotCollection initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayConfiguration:salientContentRectangle:]
+ -[PRSPosterSnapshotCollection snapshotDisplayConfiguration]
+ -[PRSPosterUpdateSessionInfo exceptionalReason]
+ -[PRSPosterUpdateSessionInfo isExceptionalUpdate]
+ -[PRSPosterUpdateSessionInfo setExceptionalReason:]
+ -[PRSPosterUpdater synchronouslyApplyUpdates:error:]
+ -[PRSServer dealloc]
+ -[PRSServer fetchGalleryForRole:completion:]
+ -[PRSServer forceUpdatePosterPath:updates:completion:]
+ -[PRSServer generatePlatformReferenceSnapshotsWithCompletion:]
+ -[PRSServer notePosterConfigurationUnderlyingModelDidChange:completion:]
+ -[PRSServer pushPosterGalleryUpdate:forRole:completion:]
+ -[PRSServer queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]
+ -[PRSServer requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]
+ -[PRSServer requestLockScreenHomeScreenColorConfigurations:]
+ -[PRSServer retrieveGalleryForRole:completion:]
+ -[PRSServer runMigration:migrationDescriptor:completion:].cold.1
+ -[PRSService _cachedLockScreenColorConfigurations]
+ -[PRSService _cachedLockScreenColorConfigurations].cold.1
+ -[PRSService _cachedLockScreenColorConfigurations].cold.2
+ -[PRSService fetchGalleryForRole:completion:]
+ -[PRSService fetchGalleryForRole:completion:].cold.1
+ -[PRSService fetchLockScreenHomeScreenColorConfigurations:completion:]
+ -[PRSService fetchLockScreenHomeScreenColorConfigurations:completion:].cold.1
+ -[PRSService forceUpdatePosterPath:updates:error:]
+ -[PRSService generatePlatformReferenceSnapshotsWithCompletion:]
+ -[PRSService generatePlatformReferenceSnapshotsWithCompletion:].cold.1
+ -[PRSService pushPosterGalleryUpdate:forRole:completion:]
+ -[PRSService pushPosterGalleryUpdate:forRole:completion:].cold.1
+ -[PRSService pushPosterGalleryUpdate:forRole:completion:].cold.2
+ -[PRSService queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]
+ -[PRSService queuePosterDescriptorUpdateForExtension:sessionInfo:completion:].cold.1
+ -[PRSService requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]
+ -[PRSService requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:].cold.1
+ -[PRSService requestLockScreenHomeScreenColorConfigurations:]
+ -[PRSService requestLockScreenHomeScreenColorConfigurations:].cold.1
+ -[PRSService retrieveGalleryForRole:completion:]
+ -[PRSService retrieveGalleryForRole:completion:].cold.1
+ -[PRSWallpaperDisplayPin .cxx_destruct]
+ -[PRSWallpaperDisplayPin description]
+ -[PRSWallpaperDisplayPin displayConfiguration]
+ -[PRSWallpaperDisplayPin displayIdentity]
+ -[PRSWallpaperDisplayPin encodeWithBSXPCCoder:]
+ -[PRSWallpaperDisplayPin encodeWithCoder:]
+ -[PRSWallpaperDisplayPin hash]
+ -[PRSWallpaperDisplayPin initWithBSXPCCoder:]
+ -[PRSWallpaperDisplayPin initWithBSXPCCoder:].cold.1
+ -[PRSWallpaperDisplayPin initWithBSXPCCoder:].cold.2
+ -[PRSWallpaperDisplayPin initWithBSXPCCoder:].cold.3
+ -[PRSWallpaperDisplayPin initWithCoder:]
+ -[PRSWallpaperDisplayPin initWithCoder:].cold.1
+ -[PRSWallpaperDisplayPin initWithCoder:].cold.2
+ -[PRSWallpaperDisplayPin initWithCoder:].cold.3
+ -[PRSWallpaperDisplayPin initWithFBSDisplayConfiguration:type:]
+ -[PRSWallpaperDisplayPin initWithFBSDisplayConfiguration:type:].cold.1
+ -[PRSWallpaperDisplayPin initWithFBSDisplayIdentity:type:]
+ -[PRSWallpaperDisplayPin initWithFBSDisplayIdentity:type:].cold.1
+ -[PRSWallpaperDisplayPin isEqual:]
+ -[PRSWallpaperDisplayPin type]
+ -[PRSWallpaperObserverConfiguration pinnedDisplay]
+ -[PRSWallpaperObserverConfiguration setPinnedDisplay:]
+ -[PRSWallpaperPublisher pinnedDisplays]
+ -[_PRSPosterChannelModelMutator .cxx_destruct]
+ -[_PRSPosterChannelModelMutator channelStateForIdentifier:error:]
+ -[_PRSPosterChannelModelMutator createChannelWithIdentifier:updater:error:]
+ -[_PRSPosterChannelModelMutator dealloc]
+ -[_PRSPosterChannelModelMutator extensionProvider]
+ -[_PRSPosterChannelModelMutator galleryProcessor]
+ -[_PRSPosterChannelModelMutator initWithModelCoordinator:error:]
+ -[_PRSPosterChannelModelMutator initWithModelCoordinator:error:].cold.1
+ -[_PRSPosterChannelModelMutator init]
+ -[_PRSPosterChannelModelMutator invalidate]
+ -[_PRSPosterChannelModelMutator keyedArchiver]
+ -[_PRSPosterChannelModelMutator knownChannelIdentifiersWithError:]
+ -[_PRSPosterChannelModelMutator knownChannelStatesWithError:]
+ -[_PRSPosterChannelModelMutator modelCoordinator]
+ -[_PRSPosterChannelModelMutator reapEverythingForChannel:]
+ -[_PRSPosterChannelModelMutator reapStaleSnapshotsForChannel:]
+ -[_PRSPosterChannelModelMutator reapStaleStateForChannel:omittingLast:error:]
+ -[_PRSPosterChannelModelMutator removeChannelWithIdentifier:error:]
+ -[_PRSPosterChannelModelMutator updateChannel:updater:error:]
+ -[_PRSPosterChannelUpdateDescriptorsTask .cxx_destruct]
+ -[_PRSPosterChannelUpdateDescriptorsTask _cleanup]
+ -[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]
+ -[_PRSPosterChannelUpdateDescriptorsTask _executionTimedOut:]
+ -[_PRSPosterChannelUpdateDescriptorsTask _finishWithResult:attempt:error:]
+ -[_PRSPosterChannelUpdateDescriptorsTask _lock_cleanup]
+ -[_PRSPosterChannelUpdateDescriptorsTask _lock_finishWithResult:attempt:error:]
+ -[_PRSPosterChannelUpdateDescriptorsTask cancelWithReason:]
+ -[_PRSPosterChannelUpdateDescriptorsTask channel:didUpdateContext:]
+ -[_PRSPosterChannelUpdateDescriptorsTask channelWillInvalidate:]
+ -[_PRSPosterChannelUpdateDescriptorsTask channelWillUpdateContext:]
+ -[_PRSPosterChannelUpdateDescriptorsTask channel]
+ -[_PRSPosterChannelUpdateDescriptorsTask dealloc]
+ -[_PRSPosterChannelUpdateDescriptorsTask execute]
+ -[_PRSPosterChannelUpdateDescriptorsTask extensionProvider]
+ -[_PRSPosterChannelUpdateDescriptorsTask fetchOptions]
+ -[_PRSPosterChannelUpdateDescriptorsTask initWithChannel:fetchOptions:extensionProvider:extensionInstanceProvider:invalidationSignal:schedulerProvider:]
+ -[_PRSPosterChannelUpdateDescriptorsTask init]
+ -[_PRSPosterChannelUpdateDescriptorsTask instanceProvider]
+ -[_PRSPosterChannelUpdateDescriptorsTask invalidate]
+ -[_PRSPosterChannelUpdateDescriptorsTask invalidationSignal]
+ -[_PRSPosterChannelUpdateDescriptorsTask promise]
+ -[_PRSPosterChannelUpdateDescriptorsTask schedulerProvider]
+ -[_PRSPosterChannelUpdaterImpl .cxx_destruct]
+ -[_PRSPosterChannelUpdaterImpl channelContext]
+ -[_PRSPosterChannelUpdaterImpl posterConfiguration]
+ -[_PRSPosterChannelUpdaterImpl setChannelContext:]
+ -[_PRSPosterChannelUpdaterImpl setPosterConfiguration:]
+ -[_PRSPosterProvider .cxx_destruct]
+ -[_PRSPosterProvider bundleIdentifier]
+ -[_PRSPosterProvider hash]
+ -[_PRSPosterProvider initWithProviderBundleIdentifier:]
+ -[_PRSPosterProvider isEqual:]
+ -[_PRSPosterProvider localizedDisplayNameForLocale:]
+ -[_PRSPosterProvider localizedDisplayName]
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table52
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table79
+ GCC_except_table8
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._UUIDToStateCoordinator
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._baseURL
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._channelsEndpoint
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._extensionProvider
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._galleryProcessor
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._keyedArchiver
+ OBJC_IVAR_$__PRSPosterChannelModelMutator._role
+ _BSDispatchQueueCreateSerial
+ _BSInterfaceOrientationIsLandscape
+ _BSSizeSwap
+ _CGRectZero
+ _CHANNEL_LOG_PREFIX
+ _NSURLFileResourceIdentifierKey
+ _NSURLIsExcludedFromBackupKey
+ _NSURLTotalFileAllocatedSizeKey
+ _OBJC_CLASS_$_BSAtomicSignal
+ _OBJC_CLASS_$_BSCompoundAssertion
+ _OBJC_CLASS_$_BSDescriptionStream
+ _OBJC_CLASS_$_BSMutableOrderedDictionary
+ _OBJC_CLASS_$_FBSDisplayConfiguration
+ _OBJC_CLASS_$_FBSDisplayMonitor
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_PFFileSystemEndpoint
+ _OBJC_CLASS_$_PFFileSystemSchemaManager
+ _OBJC_CLASS_$_PFFileSystemStagedURL
+ _OBJC_CLASS_$_PFOSUnfairLock
+ _OBJC_CLASS_$_PFPosterExtensionInstanceProvider
+ _OBJC_CLASS_$_PFSQLiteKeyedArchiver
+ _OBJC_CLASS_$_PFTScheduler
+ _OBJC_CLASS_$_PFTSchedulerProvider
+ _OBJC_CLASS_$_PRSLockScreenColorConfigurationCache
+ _OBJC_CLASS_$_PRSPosterChannel
+ _OBJC_CLASS_$_PRSPosterChannelConfiguration
+ _OBJC_CLASS_$_PRSPosterChannelContext
+ _OBJC_CLASS_$_PRSPosterChannelController
+ _OBJC_CLASS_$_PRSPosterChannelGalleryCoordinator
+ _OBJC_CLASS_$_PRSPosterChannelGalleryFetchOptions
+ _OBJC_CLASS_$_PRSPosterChannelModelCoordinator
+ _OBJC_CLASS_$_PRSPosterChannelReaper
+ _OBJC_CLASS_$_PRSPosterChannelState
+ _OBJC_CLASS_$_PRSPosterConfigurationFinalizer
+ _OBJC_CLASS_$_PRSPosterGallery
+ _OBJC_CLASS_$_PRSPosterGalleryMetadata
+ _OBJC_CLASS_$_PRSWallpaperDisplayPin
+ _OBJC_CLASS_$__PRSPosterChannelModelMutator
+ _OBJC_CLASS_$__PRSPosterChannelUpdateDescriptorsTask
+ _OBJC_CLASS_$__PRSPosterChannelUpdaterImpl
+ _OBJC_CLASS_$__PRSPosterProvider
+ _OBJC_CLASS_$__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ _OBJC_CLASS_$__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ _OBJC_IVAR_$_PRSDisplayInfo._displayConfiguration
+ _OBJC_IVAR_$_PRSHostConfigurationEntry._migratedConfigurationMatchingMask
+ _OBJC_IVAR_$_PRSLockScreenColorConfigurationCache._cachePath
+ _OBJC_IVAR_$_PRSLockScreenColorConfigurationCache._lock
+ _OBJC_IVAR_$_PRSLockScreenColorConfigurationCache._lock_cachedConfigurations
+ _OBJC_IVAR_$_PRSLockScreenColorConfigurationCache._lock_lastEpoch
+ _OBJC_IVAR_$_PRSPosterChannel._channelIdentifier
+ _OBJC_IVAR_$_PRSPosterChannel._completionScheduler
+ _OBJC_IVAR_$_PRSPosterChannel._invalidationSignal
+ _OBJC_IVAR_$_PRSPosterChannel._lock
+ _OBJC_IVAR_$_PRSPosterChannel._lock_currentGallery
+ _OBJC_IVAR_$_PRSPosterChannel._lock_currentPosterConfiguration
+ _OBJC_IVAR_$_PRSPosterChannel._lock_isBeingRemoved
+ _OBJC_IVAR_$_PRSPosterChannel._lock_observers
+ _OBJC_IVAR_$_PRSPosterChannel._lock_state
+ _OBJC_IVAR_$_PRSPosterChannel._modelCoordinator
+ _OBJC_IVAR_$_PRSPosterChannel._observerQueue
+ _OBJC_IVAR_$_PRSPosterChannel._stateCoordinator
+ _OBJC_IVAR_$_PRSPosterChannelConfiguration._URL
+ _OBJC_IVAR_$_PRSPosterChannelConfiguration._fileManager
+ _OBJC_IVAR_$_PRSPosterChannelConfiguration._reapOptions
+ _OBJC_IVAR_$_PRSPosterChannelConfiguration._role
+ _OBJC_IVAR_$_PRSPosterChannelContext._role
+ _OBJC_IVAR_$_PRSPosterChannelContext._userInfo
+ _OBJC_IVAR_$_PRSPosterChannelController._channelForUUIDFuture
+ _OBJC_IVAR_$_PRSPosterChannelController._completionScheduler
+ _OBJC_IVAR_$_PRSPosterChannelController._configuration
+ _OBJC_IVAR_$_PRSPosterChannelController._extensionProvider
+ _OBJC_IVAR_$_PRSPosterChannelController._lock
+ _OBJC_IVAR_$_PRSPosterChannelController._lock_observers
+ _OBJC_IVAR_$_PRSPosterChannelController._modelCoordinator
+ _OBJC_IVAR_$_PRSPosterChannelController._modelCoordinatorScheduler
+ _OBJC_IVAR_$_PRSPosterChannelController._modelCoordinatorScheduler_channelForUUID
+ _OBJC_IVAR_$_PRSPosterChannelController._observerQueue
+ _OBJC_IVAR_$_PRSPosterChannelController._reapOptions
+ _OBJC_IVAR_$_PRSPosterChannelController._reapScheduler
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._activeFinishAssertion
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._activeTask
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._channelUUIDToTaskQueue
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._extensionProvider
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._instanceProvider
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._invalidationSignal
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._logPrefix
+ _OBJC_IVAR_$_PRSPosterChannelGalleryCoordinator._scheduler
+ _OBJC_IVAR_$_PRSPosterChannelGalleryFetchOptions._extensionIdentifiers
+ _OBJC_IVAR_$_PRSPosterChannelGalleryFetchOptions._policy
+ _OBJC_IVAR_$_PRSPosterChannelGalleryFetchOptions._updateSessionInfoProvider
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._URL
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._channelPersistenceURLEndpoint
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._databaseURL
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._extensionProvider
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._fileManager
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._fileResourceIdentifier
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._inUseAssertionProvider
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._logPrefix
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._modelLock
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._modelLock_modelMutator
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._role
+ _OBJC_IVAR_$_PRSPosterChannelModelCoordinator._schemaManager
+ _OBJC_IVAR_$_PRSPosterGallery._context
+ _OBJC_IVAR_$_PRSPosterGallery._descriptors
+ _OBJC_IVAR_$_PRSPosterGallery._metadata
+ _OBJC_IVAR_$_PRSPosterGallery._providersByBundleIdentifier
+ _OBJC_IVAR_$_PRSPosterSnapshotCollection._snapshotDisplayConfiguration
+ _OBJC_IVAR_$_PRSPosterUpdateSessionInfo._exceptionalReason
+ _OBJC_IVAR_$_PRSWallpaperClient._entitledForHostStorageSandboxExtension
+ _OBJC_IVAR_$_PRSWallpaperClient._pinnedDisplay
+ _OBJC_IVAR_$_PRSWallpaperDisplayPin._displayConfiguration
+ _OBJC_IVAR_$_PRSWallpaperDisplayPin._displayIdentity
+ _OBJC_IVAR_$_PRSWallpaperDisplayPin._type
+ _OBJC_IVAR_$_PRSWallpaperObserver._conn_pinnedDisplay
+ _OBJC_IVAR_$_PRSWallpaperObserverConfiguration._pinnedDisplay
+ _OBJC_IVAR_$_PRSWallpaperPublisher._lock_pinnedDisplays
+ _OBJC_IVAR_$__PRSPosterChannelModelMutator._modelCoordinator
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._channel
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._extensionProvider
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._fetchOptions
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._instanceProvider
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._invalidationSignal
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._lock
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._lock_cancelled
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._lock_executionInstance
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._lock_finished
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._lock_underlyingPromise
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._promise
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._schedulerProvider
+ _OBJC_IVAR_$__PRSPosterChannelUpdateDescriptorsTask._spunupExtensionInstanceFuture
+ _OBJC_IVAR_$__PRSPosterChannelUpdaterImpl._channelContext
+ _OBJC_IVAR_$__PRSPosterChannelUpdaterImpl._posterConfiguration
+ _OBJC_IVAR_$__PRSPosterProvider._bundleIdentifier
+ _OBJC_IVAR_$__PRSPosterProvider._extensionRecordFuture
+ _OBJC_METACLASS_$_PRSLockScreenColorConfigurationCache
+ _OBJC_METACLASS_$_PRSPosterChannel
+ _OBJC_METACLASS_$_PRSPosterChannelConfiguration
+ _OBJC_METACLASS_$_PRSPosterChannelContext
+ _OBJC_METACLASS_$_PRSPosterChannelController
+ _OBJC_METACLASS_$_PRSPosterChannelGalleryCoordinator
+ _OBJC_METACLASS_$_PRSPosterChannelGalleryFetchOptions
+ _OBJC_METACLASS_$_PRSPosterChannelModelCoordinator
+ _OBJC_METACLASS_$_PRSPosterChannelReaper
+ _OBJC_METACLASS_$_PRSPosterChannelState
+ _OBJC_METACLASS_$_PRSPosterConfigurationFinalizer
+ _OBJC_METACLASS_$_PRSPosterGallery
+ _OBJC_METACLASS_$_PRSPosterGalleryMetadata
+ _OBJC_METACLASS_$_PRSWallpaperDisplayPin
+ _OBJC_METACLASS_$__PRSPosterChannelModelMutator
+ _OBJC_METACLASS_$__PRSPosterChannelUpdateDescriptorsTask
+ _OBJC_METACLASS_$__PRSPosterChannelUpdaterImpl
+ _OBJC_METACLASS_$__PRSPosterProvider
+ _OBJC_METACLASS_$__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ _OBJC_METACLASS_$__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ _PFCurrentDeviceClass
+ _PFFileProtectionNoneAttributes
+ _PFPathComponent_DescriptorIdentifier
+ _PFPosterRoleBackdrop
+ _PFPosterRoleIncomingCall
+ _PFServerPosterTypeToDirectoryName
+ _PRSExceptionalUpdateReasonClientSPI
+ _PRSExceptionalUpdateReasonDayZero
+ _PRSExceptionalUpdateReasonNeverFeature
+ _PRSExceptionalUpdateReasonUserInitiated
+ _PRSLogChannels
+ _PRSLogChannels.__logObj
+ _PRSLogChannels.cold.1
+ _PRSLogChannels.onceToken
+ _PRSLogColorConfigCache
+ _PRSLogColorConfigCache.__logObj
+ _PRSLogColorConfigCache.cold.1
+ _PRSLogColorConfigCache.onceToken
+ _PRSLogServer
+ _PRSLogServer.__logObj
+ _PRSLogServer.cold.1
+ _PRSLogServer.onceToken
+ _PRSPosterConfigurationFinalizerErrorDomain
+ _PRSServerMutateConfigurationHostStorageEntitlement
+ __CLASS_METHODS_PRSPosterChannelState
+ __CLASS_METHODS_PRSPosterGalleryMetadata
+ __CLASS_METHODS__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __CLASS_PROPERTIES_PRSPosterChannelState
+ __CLASS_PROPERTIES_PRSPosterGalleryMetadata
+ __DATA_PRSPosterChannelReaper
+ __DATA_PRSPosterChannelState
+ __DATA_PRSPosterGalleryMetadata
+ __DATA__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ __DATA__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __INSTANCE_METHODS_PRSPosterChannelReaper
+ __INSTANCE_METHODS_PRSPosterChannelState
+ __INSTANCE_METHODS_PRSPosterGalleryMetadata
+ __INSTANCE_METHODS__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __IVARS_PRSPosterChannelReaper
+ __IVARS_PRSPosterChannelState
+ __IVARS_PRSPosterGalleryMetadata
+ __IVARS__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ __IVARS__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __METACLASS_DATA_PRSPosterChannelReaper
+ __METACLASS_DATA_PRSPosterChannelState
+ __METACLASS_DATA_PRSPosterGalleryMetadata
+ __METACLASS_DATA__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ __METACLASS_DATA__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __NSIsNSCFConstantString
+ __OBJC_$_CLASS_METHODS_PRSLockScreenColorConfigurationCache
+ __OBJC_$_CLASS_METHODS_PRSPosterChannel
+ __OBJC_$_CLASS_METHODS_PRSPosterChannelConfiguration
+ __OBJC_$_CLASS_METHODS_PRSPosterChannelContext
+ __OBJC_$_CLASS_METHODS_PRSPosterChannelController
+ __OBJC_$_CLASS_METHODS_PRSPosterChannelGalleryCoordinator
+ __OBJC_$_CLASS_METHODS_PRSPosterChannelModelCoordinator
+ __OBJC_$_CLASS_METHODS_PRSPosterConfigurationFinalizer
+ __OBJC_$_CLASS_METHODS_PRSPosterGallery
+ __OBJC_$_CLASS_METHODS_PRSWallpaperDisplayPin
+ __OBJC_$_CLASS_METHODS__PRSPosterChannelModelMutator
+ __OBJC_$_CLASS_PROP_LIST_PRSPosterChannelContext
+ __OBJC_$_CLASS_PROP_LIST_PRSWallpaperDisplayPin
+ __OBJC_$_INSTANCE_METHODS_PRSLockScreenColorConfigurationCache
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannel
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelConfiguration
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelContext
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelController
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelGalleryCoordinator
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelGalleryFetchOptions
+ __OBJC_$_INSTANCE_METHODS_PRSPosterChannelModelCoordinator
+ __OBJC_$_INSTANCE_METHODS_PRSPosterConfiguration(PRSUtilities)
+ __OBJC_$_INSTANCE_METHODS_PRSPosterGallery
+ __OBJC_$_INSTANCE_METHODS_PRSWallpaperDisplayPin
+ __OBJC_$_INSTANCE_METHODS__PRSPosterChannelModelMutator
+ __OBJC_$_INSTANCE_METHODS__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_$_INSTANCE_METHODS__PRSPosterChannelUpdaterImpl
+ __OBJC_$_INSTANCE_METHODS__PRSPosterProvider
+ __OBJC_$_INSTANCE_METHODS__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator(PosterBoardServices)
+ __OBJC_$_INSTANCE_VARIABLES_PRSLockScreenColorConfigurationCache
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannel
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelContext
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelController
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelGalleryCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelGalleryFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterChannelModelCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterGallery
+ __OBJC_$_INSTANCE_VARIABLES_PRSWallpaperDisplayPin
+ __OBJC_$_INSTANCE_VARIABLES__PRSPosterChannelModelMutator
+ __OBJC_$_INSTANCE_VARIABLES__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_$_INSTANCE_VARIABLES__PRSPosterChannelUpdaterImpl
+ __OBJC_$_INSTANCE_VARIABLES__PRSPosterProvider
+ __OBJC_$_PROP_LIST_PRSPosterChannel
+ __OBJC_$_PROP_LIST_PRSPosterChannelConfiguration
+ __OBJC_$_PROP_LIST_PRSPosterChannelConfiguring
+ __OBJC_$_PROP_LIST_PRSPosterChannelContext
+ __OBJC_$_PROP_LIST_PRSPosterChannelController
+ __OBJC_$_PROP_LIST_PRSPosterChannelGalleryCoordinator
+ __OBJC_$_PROP_LIST_PRSPosterChannelGalleryFetchOptions
+ __OBJC_$_PROP_LIST_PRSPosterChannelModelCoordinator
+ __OBJC_$_PROP_LIST_PRSPosterChannelModelMutating
+ __OBJC_$_PROP_LIST_PRSPosterChannelUpdater
+ __OBJC_$_PROP_LIST_PRSPosterGallery
+ __OBJC_$_PROP_LIST_PRSPosterProvider
+ __OBJC_$_PROP_LIST_PRSWallpaperDisplayPin
+ __OBJC_$_PROP_LIST__PRSPosterChannelModelMutator
+ __OBJC_$_PROP_LIST__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_$_PROP_LIST__PRSPosterChannelUpdaterImpl
+ __OBJC_$_PROP_LIST__PRSPosterProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionStreamable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PRSPosterChannelConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PRSPosterChannelObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterChannelConfiguring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterChannelModelAccessing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterChannelModelMutating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterChannelUpdater
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRSPosterProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionStreamable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterChannelConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterChannelModelAccessing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterChannelModelMutating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterChannelObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterChannelUpdater
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRSPosterProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __OBJC_$_PROTOCOL_REFS_BSDescriptionStreamable
+ __OBJC_$_PROTOCOL_REFS_PRSPosterChannelConfiguring
+ __OBJC_$_PROTOCOL_REFS_PRSPosterChannelModelAccessing
+ __OBJC_$_PROTOCOL_REFS_PRSPosterChannelModelMutating
+ __OBJC_$_PROTOCOL_REFS_PRSPosterChannelUpdater
+ __OBJC_$_PROTOCOL_REFS_PRSPosterProvider
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannel
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannelConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannelContext
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannelController
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannelGalleryCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterChannelModelCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_PRSWallpaperDisplayPin
+ __OBJC_CLASS_PROTOCOLS_$__PRSPosterChannelModelMutator
+ __OBJC_CLASS_PROTOCOLS_$__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_CLASS_PROTOCOLS_$__PRSPosterChannelUpdaterImpl
+ __OBJC_CLASS_PROTOCOLS_$__PRSPosterProvider
+ __OBJC_CLASS_PROTOCOLS_$__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator(PosterBoardServices)
+ __OBJC_CLASS_RO_$_PRSLockScreenColorConfigurationCache
+ __OBJC_CLASS_RO_$_PRSPosterChannel
+ __OBJC_CLASS_RO_$_PRSPosterChannelConfiguration
+ __OBJC_CLASS_RO_$_PRSPosterChannelContext
+ __OBJC_CLASS_RO_$_PRSPosterChannelController
+ __OBJC_CLASS_RO_$_PRSPosterChannelGalleryCoordinator
+ __OBJC_CLASS_RO_$_PRSPosterChannelGalleryFetchOptions
+ __OBJC_CLASS_RO_$_PRSPosterChannelModelCoordinator
+ __OBJC_CLASS_RO_$_PRSPosterConfigurationFinalizer
+ __OBJC_CLASS_RO_$_PRSPosterGallery
+ __OBJC_CLASS_RO_$_PRSWallpaperDisplayPin
+ __OBJC_CLASS_RO_$__PRSPosterChannelModelMutator
+ __OBJC_CLASS_RO_$__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_CLASS_RO_$__PRSPosterChannelUpdaterImpl
+ __OBJC_CLASS_RO_$__PRSPosterProvider
+ __OBJC_LABEL_PROTOCOL_$_BSDescriptionStreamable
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterChannelConfiguring
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterChannelModelAccessing
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterChannelModelMutating
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterChannelObserver
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterChannelUpdater
+ __OBJC_LABEL_PROTOCOL_$_PRSPosterProvider
+ __OBJC_LABEL_PROTOCOL_$__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __OBJC_METACLASS_RO_$_PRSLockScreenColorConfigurationCache
+ __OBJC_METACLASS_RO_$_PRSPosterChannel
+ __OBJC_METACLASS_RO_$_PRSPosterChannelConfiguration
+ __OBJC_METACLASS_RO_$_PRSPosterChannelContext
+ __OBJC_METACLASS_RO_$_PRSPosterChannelController
+ __OBJC_METACLASS_RO_$_PRSPosterChannelGalleryCoordinator
+ __OBJC_METACLASS_RO_$_PRSPosterChannelGalleryFetchOptions
+ __OBJC_METACLASS_RO_$_PRSPosterChannelModelCoordinator
+ __OBJC_METACLASS_RO_$_PRSPosterConfigurationFinalizer
+ __OBJC_METACLASS_RO_$_PRSPosterGallery
+ __OBJC_METACLASS_RO_$_PRSWallpaperDisplayPin
+ __OBJC_METACLASS_RO_$__PRSPosterChannelModelMutator
+ __OBJC_METACLASS_RO_$__PRSPosterChannelUpdateDescriptorsTask
+ __OBJC_METACLASS_RO_$__PRSPosterChannelUpdaterImpl
+ __OBJC_METACLASS_RO_$__PRSPosterProvider
+ __OBJC_PROTOCOL_$_BSDescriptionStreamable
+ __OBJC_PROTOCOL_$_PRSPosterChannelConfiguring
+ __OBJC_PROTOCOL_$_PRSPosterChannelModelAccessing
+ __OBJC_PROTOCOL_$_PRSPosterChannelModelMutating
+ __OBJC_PROTOCOL_$_PRSPosterChannelObserver
+ __OBJC_PROTOCOL_$_PRSPosterChannelUpdater
+ __OBJC_PROTOCOL_$_PRSPosterProvider
+ __OBJC_PROTOCOL_$__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __PROPERTIES_PRSPosterChannelReaper
+ __PROPERTIES_PRSPosterChannelState
+ __PROPERTIES_PRSPosterGalleryMetadata
+ __PROPERTIES__TtC19PosterBoardServices32PRSPosterChannelStateCoordinator
+ __PROPERTIES__TtC19PosterBoardServices42PRSPosterChannelStateCoordinatorTransition
+ __PROTOCOLS_PRSPosterChannelState
+ __PROTOCOLS_PRSPosterChannelState.2
+ __PROTOCOLS_PRSPosterGalleryMetadata
+ __PROTOCOLS_PRSPosterGalleryMetadata.2
+ __PROTOCOL_INSTANCE_METHODS__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __PROTOCOL_METHOD_TYPES__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ __PROTOCOL__TtP19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_
+ ___100-[PRSService requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]_block_invoke
+ ___100-[PRSService requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]_block_invoke.cold.1
+ ___102-[PRSPosterChannel updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:completion:]_block_invoke
+ ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.36
+ ___152-[_PRSPosterChannelUpdateDescriptorsTask initWithChannel:fetchOptions:extensionProvider:extensionInstanceProvider:invalidationSignal:schedulerProvider:]_block_invoke
+ ___152-[_PRSPosterChannelUpdateDescriptorsTask initWithChannel:fetchOptions:extensionProvider:extensionInstanceProvider:invalidationSignal:schedulerProvider:]_block_invoke_2
+ ___152-[_PRSPosterChannelUpdateDescriptorsTask initWithChannel:fetchOptions:extensionProvider:extensionInstanceProvider:invalidationSignal:schedulerProvider:]_block_invoke_3
+ ___18-[PRSService init]_block_invoke.11
+ ___18-[PRSService init]_block_invoke.11.cold.1
+ ___31-[PRSPosterChannel description]_block_invoke
+ ___39-[PRSPosterChannel addChannelObserver:]_block_invoke
+ ___42-[PRSPosterChannel removeChannelObserver:]_block_invoke
+ ___44-[PRSPosterChannelController channelsFuture]_block_invoke
+ ___44-[PRSServer fetchGalleryForRole:completion:]_block_invoke
+ ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.27
+ ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.27.cold.1
+ ___45-[PRSService fetchGalleryForRole:completion:]_block_invoke
+ ___45-[PRSService fetchGalleryForRole:completion:]_block_invoke.cold.1
+ ___47-[PRSServer retrieveGalleryForRole:completion:]_block_invoke
+ ___48-[PRSServer fetchAvailableExtensionIdentifiers:]_block_invoke
+ ___48-[PRSService retrieveGalleryForRole:completion:]_block_invoke
+ ___48-[PRSService retrieveGalleryForRole:completion:]_block_invoke.cold.1
+ ___49-[PRSPosterChannel _notifyObserversDidInvalidate]_block_invoke
+ ___49-[PRSPosterChannel _notifyObserversDidInvalidate]_block_invoke_2
+ ___49-[_PRSPosterChannelUpdateDescriptorsTask execute]_block_invoke
+ ___50-[PRSPosterChannel _notifyObserversWillInvalidate]_block_invoke
+ ___50-[PRSPosterChannel _notifyObserversWillInvalidate]_block_invoke_2
+ ___50-[PRSPosterChannelController handleDidAddChannel:]_block_invoke
+ ___50-[PRSService forceUpdatePosterPath:updates:error:]_block_invoke
+ ___50-[PRSService forceUpdatePosterPath:updates:error:]_block_invoke.cold.1
+ ___50-[PRSService forceUpdatePosterPath:updates:error:]_block_invoke.cold.2
+ ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.179
+ ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.180
+ ___51+[PRSLockScreenColorConfigurationCache sharedCache]_block_invoke
+ ___51-[PRSPosterChannelController handleWillAddChannel:]_block_invoke
+ ___52-[PRSPosterChannel _notifyObserversDidUpdatePoster:]_block_invoke
+ ___52-[PRSPosterChannel _notifyObserversDidUpdatePoster:]_block_invoke_2
+ ___52-[PRSPosterChannel _notifyObserversWillUpdatePoster]_block_invoke
+ ___52-[PRSPosterChannel _notifyObserversWillUpdatePoster]_block_invoke_2
+ ___52-[PRSPosterChannelController initWithConfiguration:]_block_invoke
+ ___52-[PRSPosterChannelController initWithConfiguration:]_block_invoke.98
+ ___52-[PRSPosterChannelController initWithConfiguration:]_block_invoke_2
+ ___52-[PRSPosterChannelController initWithConfiguration:]_block_invoke_3
+ ___52-[PRSPosterChannelController initWithConfiguration:]_block_invoke_4
+ ___52-[PRSPosterChannelController updateChannel:updater:]_block_invoke
+ ___52-[PRSPosterChannelController updateChannel:updater:]_block_invoke_2
+ ___53-[PRSPosterChannel _notifyObserversDidUpdateContext:]_block_invoke
+ ___53-[PRSPosterChannel _notifyObserversDidUpdateContext:]_block_invoke_2
+ ___53-[PRSPosterChannel _notifyObserversDidUpdateGallery:]_block_invoke
+ ___53-[PRSPosterChannel _notifyObserversDidUpdateGallery:]_block_invoke_2
+ ___53-[PRSPosterChannel _notifyObserversWillUpdateContext]_block_invoke
+ ___53-[PRSPosterChannel _notifyObserversWillUpdateContext]_block_invoke_2
+ ___53-[PRSPosterChannel _notifyObserversWillUpdateGallery]_block_invoke
+ ___53-[PRSPosterChannel _notifyObserversWillUpdateGallery]_block_invoke_2
+ ___53-[PRSPosterChannel coordinateWithRemoveChannelBlock:]_block_invoke
+ ___53-[PRSPosterChannel coordinateWithRemoveChannelBlock:]_block_invoke_2
+ ___53-[PRSPosterChannelContext _validateUserInfo:badKeys:]_block_invoke
+ ___53-[PRSPosterChannelController channelsWithCompletion:]_block_invoke
+ ___53-[PRSPosterChannelController handleDidRemoveChannel:]_block_invoke
+ ___53-[PRSPosterChannelController handleDidUpdateChannel:]_block_invoke
+ ___54-[PRSPosterChannelController handleWillRemoveChannel:]_block_invoke
+ ___54-[PRSPosterChannelController handleWillUpdateChannel:]_block_invoke
+ ___54-[PRSPosterChannelController removeChannelWithFuture:]_block_invoke
+ ___54-[PRSPosterChannelController removeChannelWithFuture:]_block_invoke_2
+ ___54-[PRSPosterChannelController removeChannelWithFuture:]_block_invoke_3
+ ___54-[PRSPosterChannelGalleryCoordinator _executeNextTask]_block_invoke
+ ___54-[PRSPosterChannelGalleryCoordinator _executeNextTask]_block_invoke_2
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke.165
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke.165.cold.1
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke_2
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke_3
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke_4
+ ___55-[PRSPosterChannelController reapEverythingForChannel:]_block_invoke_4.cold.1
+ ___55-[PRSPosterChannelController removeChannel:completion:]_block_invoke
+ ___55-[PRSServer listener:didReceiveConnection:withContext:]_block_invoke.11
+ ___55-[_PRSPosterChannelUpdateDescriptorsTask _lock_cleanup]_block_invoke
+ ___55-[_PRSPosterProvider initWithProviderBundleIdentifier:]_block_invoke
+ ___56-[PRSServer pushPosterGalleryUpdate:forRole:completion:]_block_invoke
+ ___57-[PRSPosterChannelController channelFutureForIdentifier:]_block_invoke
+ ___57-[PRSService pushPosterGalleryUpdate:forRole:completion:]_block_invoke
+ ___57-[PRSService pushPosterGalleryUpdate:forRole:completion:]_block_invoke.cold.1
+ ___59-[PRSPosterChannelController addChannelControllerObserver:]_block_invoke
+ ___59-[PRSPosterChannelController reapStaleSnapshotsForChannel:]_block_invoke
+ ___59-[PRSPosterChannelController reapStaleSnapshotsForChannel:]_block_invoke_2
+ ___59-[_PRSPosterChannelUpdateDescriptorsTask cancelWithReason:]_block_invoke
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke.167
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke_2
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke_3
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke_4
+ ___60-[_PRSPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke_5
+ ___61-[PRSService requestLockScreenHomeScreenColorConfigurations:]_block_invoke
+ ___61-[PRSService requestLockScreenHomeScreenColorConfigurations:]_block_invoke.cold.1
+ ___61-[_PRSPosterChannelModelMutator knownChannelStatesWithError:]_block_invoke
+ ___62-[PRSPosterChannelController channelForIdentifier:completion:]_block_invoke
+ ___62-[PRSPosterChannelController removeChannelControllerObserver:]_block_invoke
+ ___62-[PRSService notePosterConfigurationUnderlyingModelDidChange:]_block_invoke
+ ___62-[PRSService notePosterConfigurationUnderlyingModelDidChange:]_block_invoke.cold.1
+ ___62-[PRSService notePosterConfigurationUnderlyingModelDidChange:]_block_invoke.cold.2
+ ___63-[PRSPosterChannelController updateChannel:updater:completion:]_block_invoke
+ ___63-[PRSService generatePlatformReferenceSnapshotsWithCompletion:]_block_invoke
+ ___63-[PRSService generatePlatformReferenceSnapshotsWithCompletion:]_block_invoke.cold.1
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.168
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.168.cold.1
+ ___66-[PRSPosterChannelController createChannelWithIdentifier:updater:]_block_invoke
+ ___66-[PRSPosterChannelController createChannelWithIdentifier:updater:]_block_invoke_2
+ ___66-[PRSPosterChannelController reapEverythingForChannel:completion:]_block_invoke
+ ___67-[_PRSPosterChannelUpdateDescriptorsTask channel:didUpdateContext:]_block_invoke
+ ___67-[_PRSPosterChannelUpdateDescriptorsTask channelWillUpdateContext:]_block_invoke
+ ___68-[PRSPosterChannelController reapStaleStateForChannel:omittingLast:]_block_invoke
+ ___68-[PRSPosterChannelController reapStaleStateForChannel:omittingLast:]_block_invoke_2
+ ___70-[PRSPosterChannelController reapStaleSnapshotsForChannel:completion:]_block_invoke
+ ___70-[PRSService fetchLockScreenHomeScreenColorConfigurations:completion:]_block_invoke
+ ___70-[PRSService fetchLockScreenHomeScreenColorConfigurations:completion:]_block_invoke.cold.1
+ ___73-[PRSPosterChannelController _fireObserversRespondingToSelector:handler:]_block_invoke
+ ___73-[PRSPosterChannelController _fireObserversRespondingToSelector:handler:]_block_invoke_2
+ ___73-[PRSPosterChannelModelCoordinator updateGalleryForChannel:fetchOptions:]_block_invoke
+ ___73-[PRSPosterChannelModelCoordinator updateGalleryForChannel:fetchOptions:]_block_invoke_2
+ ___73-[PRSPosterChannelModelCoordinator updateGalleryForChannel:fetchOptions:]_block_invoke_3
+ ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.19
+ ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.42
+ ___76-[PRSServer queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]_block_invoke
+ ___77-[PRSPosterChannelController createChannelWithIdentifier:updater:completion:]_block_invoke
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.164
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.166
+ ___77-[PRSService queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]_block_invoke
+ ___77-[PRSService queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]_block_invoke.cold.1
+ ___79-[PRSPosterChannelController reapStaleStateForChannel:omittingLast:completion:]_block_invoke
+ ___83-[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]_block_invoke
+ ___83-[PRSPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]_block_invoke_2
+ ___96-[PRSExternalSystemService fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:]_block_invoke.cold.7
+ ___99-[PRSServer requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]_block_invoke
+ ___99-[PRSServer requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]_block_invoke.30
+ ___PRSLogChannels_block_invoke
+ ___PRSLogColorConfigCache_block_invoke
+ ___PRSLogServer_block_invoke
+ ___allModelCoordinators
+ ___block_descriptor_32_e16_v16?0"NSNull"8l
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e35_"<PFTFuture>"16?0"NSDictionary"8l
+ ___block_descriptor_32_e48_v16?0"_PRSPosterChannelUpdateDescriptorsTask"8l
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSSet"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSNull"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e38_v24?0"PRSPosterChannel"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e38_v24?0"PRSPosterGallery"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e46_v24?0"<PRSPosterChannelModelAccessing>"8^16lr32l8
+ ___block_descriptor_40_e8_32s_e16_16?0"NSUUID"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e26_v16?0"PRSPosterChannel"8ls32l8
+ ___block_descriptor_40_e8_32s_e26_v16?0"PRSPosterGallery"8ls32l8
+ ___block_descriptor_40_e8_32s_e27_B16?0"PFPosterExtension"8ls32l8
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_v16?0"<PRSPosterChannelObserver>"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_v16?0"PRSPosterChannelController"8ls32l8
+ ___block_descriptor_40_e8_32s_e45_v24?0"<PRSPosterChannelModelMutating>"8^16ls32l8
+ ___block_descriptor_40_e8_32s_e48_v16?0"_PRSPosterChannelUpdateDescriptorsTask"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e9_16?0^8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"PRSPosterGallery"8lw32l8
+ ___block_descriptor_40_e8_32w_e36_v16?0"<BSCompoundAssertionState>"8lw32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40w_e16_"PFTFuture"8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e21_v24?0q8"NSString"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e45_v24?0"<PRSPosterChannelModelMutating>"8^16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_v16?0"<PRSPosterChannelObserver>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v24?0"PFPosterExtensionInstance"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e45_v24?0"<PRSPosterChannelModelMutating>"8^16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e46_v16?0"<PRSPosterChannelControllerObserver>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e9_16?0^8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s_e36_v16?0"PRSPosterChannelController"8ls32l8
+ ___block_descriptor_48_e8_32s_e45_v24?0"<PRSPosterChannelModelMutating>"8^16ls32l8
+ ___block_descriptor_53_e8_32s40s_e25_v16?0"<BSXPCEncoding>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e48_v16?0"_PRSPosterChannelUpdateDescriptorsTask"8lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40bs_e40_v32?0"NSURL"8"NSNumber"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e45_v24?0"<PRSPosterChannelModelMutating>"8^16lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e52_"<PFTFuture>"16?0"PRSPosterDescriptorCollection"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e9_16?0^8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e16_"PFTFuture"8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e28_"<PFTFuture>"16?0"NSSet"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.15
+ ___block_literal_global.159
+ ___block_literal_global.16
+ ___block_literal_global.164
+ ___block_literal_global.167
+ ___block_literal_global.19
+ ___block_literal_global.22
+ ___block_literal_global.32
+ ___block_literal_global.354
+ ___block_literal_global.44
+ ___block_literal_global.6
+ ___chkstk_darwin
+ ___getPRPosterPathModelObjectCacheClass_block_invoke
+ ___getPRPosterPathModelObjectCacheClass_block_invoke.cold.1
+ ___getPRPosterPathUtilitiesClass_block_invoke.cold.2
+ ___swift_allocate_value_buffer
+ ___swift_closure_destructor
+ ___swift_closure_destructor.19
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy17_8
+ ___swift_memcpy4_4
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __os_signpost_emit_with_name_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_PosterBoardServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_PosterBoardServices
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance SC11PFErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC11PFErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC11PFErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
+ _associated conformance SC11PFErrorCodeLeVSHSCSQ
+ _associated conformance So11PFErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So11PFErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
+ _associated conformance So16NSURLResourceKeyaSHSCSQ
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So18NSFileAttributeKeyaSHSCSQ
+ _associated conformance So18NSFileAttributeKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So18NSFileAttributeKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _bzero
+ _flat unique 19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegate_p
+ _getPRPosterPathModelObjectCacheClass.softClass
+ _get_enum_tag_for_layout_string 19PosterBoardServices42PRSPosterChannelStateCoordinatorTransitionC0defgH5ErrorO
+ _getxattr
+ _initWithChannelConfiguration:extensionProvider:.onceToken
+ _kPFErrorDomain
+ _kPRSWallpaperConnectionContext_pinnedDisplay
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URL
+ _objc_msgSend$_cachedLockScreenColorConfigurations
+ _objc_msgSend$_channelIdentifier
+ _objc_msgSend$_cleanup
+ _objc_msgSend$_creationDate
+ _objc_msgSend$_enqueueChannel:fetchOptions:
+ _objc_msgSend$_executeNextTask
+ _objc_msgSend$_executeWithState:
+ _objc_msgSend$_extensionProvider
+ _objc_msgSend$_finishWithResult:attempt:error:
+ _objc_msgSend$_fireObserversRespondingToSelector:handler:
+ _objc_msgSend$_lastModifiedDate
+ _objc_msgSend$_lock_buildReaper
+ _objc_msgSend$_lock_cleanup
+ _objc_msgSend$_lock_currentGallery
+ _objc_msgSend$_lock_currentPosterConfiguration
+ _objc_msgSend$_lock_finishWithResult:attempt:error:
+ _objc_msgSend$_lock_state
+ _objc_msgSend$_notifyObserversDidInvalidate
+ _objc_msgSend$_notifyObserversDidUpdateContext:
+ _objc_msgSend$_notifyObserversDidUpdateGallery:
+ _objc_msgSend$_notifyObserversDidUpdatePoster:
+ _objc_msgSend$_notifyObserversWillInvalidate
+ _objc_msgSend$_notifyObserversWillUpdateContext
+ _objc_msgSend$_notifyObserversWillUpdateGallery
+ _objc_msgSend$_notifyObserversWillUpdatePoster
+ _objc_msgSend$_osVersionMatchesXattr
+ _objc_msgSend$_readEpochFromXattr
+ _objc_msgSend$_schemaVersionMatchesXattr
+ _objc_msgSend$_validateUserInfo:badKeys:
+ _objc_msgSend$accessModel:reason:error:
+ _objc_msgSend$acquireForReason:
+ _objc_msgSend$acquireInUseAssertionWithReason:
+ _objc_msgSend$acquireInstanceForExtension:reason:error:
+ _objc_msgSend$acquireInstanceForExtensionWithIdentifier:error:
+ _objc_msgSend$acquireInstanceForExtensionWithIdentifier:reason:error:
+ _objc_msgSend$addChannelObserver:
+ _objc_msgSend$addCompletionBlock:scheduler:
+ _objc_msgSend$addFailureBlock:
+ _objc_msgSend$addedPosters
+ _objc_msgSend$allValues
+ _objc_msgSend$appendDescriptionToFormatter:
+ _objc_msgSend$appendProem:block:
+ _objc_msgSend$appendUnsignedInteger:withName:
+ _objc_msgSend$applyUpdater:error:
+ _objc_msgSend$archiveObjectUsingNSKeyedArchiver:toEndpoint:
+ _objc_msgSend$areCollectionsEqual
+ _objc_msgSend$assertNotOwner
+ _objc_msgSend$assertionWithIdentifier:stateDidChangeHandler:
+ _objc_msgSend$attributes
+ _objc_msgSend$backgroundScheduler
+ _objc_msgSend$baseURL
+ _objc_msgSend$bs_array
+ _objc_msgSend$bs_each:
+ _objc_msgSend$cachedConfigurationsWithError:
+ _objc_msgSend$cancel
+ _objc_msgSend$cancelGalleryFetchForChannelIdentifier:
+ _objc_msgSend$cancelWithReason:
+ _objc_msgSend$channel
+ _objc_msgSend$channel:didUpdateContext:
+ _objc_msgSend$channel:didUpdateGallery:
+ _objc_msgSend$channel:didUpdatePoster:
+ _objc_msgSend$channelClass
+ _objc_msgSend$channelConfigurationForURL:role:error:
+ _objc_msgSend$channelContext
+ _objc_msgSend$channelController:didAddChannel:
+ _objc_msgSend$channelController:didRemoveChannel:
+ _objc_msgSend$channelController:didUpdateChannel:
+ _objc_msgSend$channelController:willAddChannel:
+ _objc_msgSend$channelController:willRemoveChannel:
+ _objc_msgSend$channelController:willUpdateChannel:
+ _objc_msgSend$channelDidInvalidate:
+ _objc_msgSend$channelForUUIDFuture
+ _objc_msgSend$channelFutureForIdentifier:
+ _objc_msgSend$channelIdentifier
+ _objc_msgSend$channelPersistenceURLEndpoint
+ _objc_msgSend$channelVersion
+ _objc_msgSend$channelWillInvalidate:
+ _objc_msgSend$channelWillUpdateContext:
+ _objc_msgSend$channelWillUpdateGallery:
+ _objc_msgSend$channelWillUpdatePoster:
+ _objc_msgSend$channelsFuture
+ _objc_msgSend$collectionForPostersMatchingRoles:
+ _objc_msgSend$collectionForProvider:
+ _objc_msgSend$commitStagedURLs:destinationURL:error:
+ _objc_msgSend$commitStagedURLs:destinationURL:stagingURL:fileManager:error:
+ _objc_msgSend$commitStagedURLs:destinationURLsForSwap:stagingURLsForSwap:stagingURL:fileManager:error:
+ _objc_msgSend$commitStateTransitionAndReturnError:
+ _objc_msgSend$configurationForIdentity:
+ _objc_msgSend$context
+ _objc_msgSend$contextWithRole:userInfo:
+ _objc_msgSend$coordinateWithRemoveChannelBlock:
+ _objc_msgSend$coordinator:didUpdateContext:
+ _objc_msgSend$coordinator:didUpdateDescriptors:galleryMetadata:
+ _objc_msgSend$coordinator:didUpdatePoster:
+ _objc_msgSend$coordinatorDidInvalidate:
+ _objc_msgSend$coordinatorWillInvalidate:
+ _objc_msgSend$coordinatorWillUpdateContext:
+ _objc_msgSend$coordinatorWillUpdateDescriptors:
+ _objc_msgSend$coordinatorWillUpdatePoster:
+ _objc_msgSend$copyContentsOfPath:error:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$copyPath:toEndpoint:
+ _objc_msgSend$copyURL:toEndpoint:
+ _objc_msgSend$createChannelInstanceWithState:error:
+ _objc_msgSend$createChannelWithIdentifier:updater:
+ _objc_msgSend$createChannelWithIdentifier:updater:error:
+ _objc_msgSend$createModelCoordinatorWithConfiguration:extensionProvider:
+ _objc_msgSend$creationDate
+ _objc_msgSend$currentPosterConfiguration
+ _objc_msgSend$currentState
+ _objc_msgSend$databaseURL
+ _objc_msgSend$deleteEndpoint:error:
+ _objc_msgSend$description
+ _objc_msgSend$descriptorIdentityWithProvider:identifier:role:posterUUID:version:
+ _objc_msgSend$descriptors
+ _objc_msgSend$descriptorsForState:
+ _objc_msgSend$displayIdentity
+ _objc_msgSend$distantPast
+ _objc_msgSend$endPointByAppendingEndpoint:
+ _objc_msgSend$endPointByAppendingRelativePathComponents:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumeratorForEndpoint:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$execute
+ _objc_msgSend$extendHostStorageReadWriteAccessToAuditToken:error:
+ _objc_msgSend$extension
+ _objc_msgSend$extensionIdentifiers
+ _objc_msgSend$extensionProvider
+ _objc_msgSend$fetchGalleryForChannel:options:
+ _objc_msgSend$fetchGalleryForRole:completion:
+ _objc_msgSend$fileManager
+ _objc_msgSend$fileSystemEndpointForChannelIdentifier:
+ _objc_msgSend$fileSystemSchemaManager
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$finalState
+ _objc_msgSend$finalizedConfigurationForAttributes:error:
+ _objc_msgSend$finalizedConfigurationForAttributes:withConfiguredProperties:error:
+ _objc_msgSend$finalizerErrorWithCode:underlyingError:
+ _objc_msgSend$finishWithError:
+ _objc_msgSend$flatMap:continuationScheduler:
+ _objc_msgSend$forceUpdatePosterPath:updates:completion:
+ _objc_msgSend$forceUpdatePosterPath:updates:error:
+ _objc_msgSend$futureWithBlock:
+ _objc_msgSend$futureWithBlock:scheduler:
+ _objc_msgSend$futureWithError:
+ _objc_msgSend$galleryMetadataForState:
+ _objc_msgSend$galleryProcessor
+ _objc_msgSend$generatePlatformReferenceSnapshotsWithCompletion:
+ _objc_msgSend$globalAsyncScheduler
+ _objc_msgSend$handleDidAddChannel:
+ _objc_msgSend$handleDidRemoveChannel:
+ _objc_msgSend$handleDidUpdateChannel:
+ _objc_msgSend$handleWillAddChannel:
+ _objc_msgSend$handleWillRemoveChannel:
+ _objc_msgSend$handleWillUpdateChannel:
+ _objc_msgSend$hasBeenSignalled
+ _objc_msgSend$hashTableWithOptions:
+ _objc_msgSend$incomingConfigurationIdentityWithProvider:role:posterUUID:version:supplement:
+ _objc_msgSend$ingestUpdatedDescriptors:forState:galleryMetadata:policy:error:
+ _objc_msgSend$ingestUpdatedDescriptors:forState:withMetadata:withPolicy:error:
+ _objc_msgSend$initWithBaseURL:fileManager:
+ _objc_msgSend$initWithBundleIdentifier:error:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithCachePath:
+ _objc_msgSend$initWithChannel:fetchOptions:extensionProvider:extensionInstanceProvider:invalidationSignal:schedulerProvider:
+ _objc_msgSend$initWithChannelConfiguration:extensionProvider:
+ _objc_msgSend$initWithChannelIdentifier:channelVersion:posterVersion:channelContext:posterConfigurationIdentity:creationDate:lastModifiedDate:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithCollection:otherCollection:
+ _objc_msgSend$initWithContext:descriptors:metadata:
+ _objc_msgSend$initWithCreationDate:
+ _objc_msgSend$initWithDatabaseURL:error:
+ _objc_msgSend$initWithDefaultInstanceIdentifier:
+ _objc_msgSend$initWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:
+ _objc_msgSend$initWithExtensionProvider:
+ _objc_msgSend$initWithFBSDisplayConfiguration:type:
+ _objc_msgSend$initWithFBSDisplayIdentity:type:
+ _objc_msgSend$initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:displayConfiguration:
+ _objc_msgSend$initWithLockIdentifier:
+ _objc_msgSend$initWithModelCoordinator:channelIdentifier:error:
+ _objc_msgSend$initWithModelCoordinator:currentState:currentPosterConfiguration:currentGallery:snapshotCache:
+ _objc_msgSend$initWithModelCoordinator:error:
+ _objc_msgSend$initWithModelCoordinator:state:error:
+ _objc_msgSend$initWithPath:
+ _objc_msgSend$initWithPath:extensionIdentifier:
+ _objc_msgSend$initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayConfiguration:
+ _objc_msgSend$initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayConfiguration:salientContentRectangle:
+ _objc_msgSend$initWithProviderBundleIdentifier:
+ _objc_msgSend$initWithRelativePathComponents:
+ _objc_msgSend$initWithRelativePathComponents:attributes:resourceValues:
+ _objc_msgSend$initWithRole:userInfo:
+ _objc_msgSend$initWithURL:role:error:
+ _objc_msgSend$initialTransitionForModelCoordinatorWithModelCoordinator:channelIdentifier:updater:error:
+ _objc_msgSend$instancePool
+ _objc_msgSend$invalidateModelObjectCacheForPath:
+ _objc_msgSend$isActive
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToGallery:
+ _objc_msgSend$isFinished
+ _objc_msgSend$isReadableFileAtPath:
+ _objc_msgSend$join:
+ _objc_msgSend$knownChannelIdentifiersWithError:
+ _objc_msgSend$knownChannelStatesWithError:
+ _objc_msgSend$knownPosterExtensions
+ _objc_msgSend$lastModifiedDate
+ _objc_msgSend$lazyFutureWithBlock:
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedNameWithPreferredLocalizations:
+ _objc_msgSend$lock
+ _objc_msgSend$logPrefix
+ _objc_msgSend$mainConfiguration
+ _objc_msgSend$member:
+ _objc_msgSend$migratedConfigurationMatchingMask
+ _objc_msgSend$mutateModel:reason:error:
+ _objc_msgSend$nextObject
+ _objc_msgSend$notePosterConfigurationUnderlyingModelDidChange:completion:
+ _objc_msgSend$now
+ _objc_msgSend$operatingSystemVersionString
+ _objc_msgSend$operationQueueSchedulerWithMaxConcurrentOperationCount:qualityOfService:name:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$performBlock:
+ _objc_msgSend$performBlockWhileCapturingWeak:performBlock:
+ _objc_msgSend$performSelector:withObject:afterDelay:
+ _objc_msgSend$pf_UUIDFromArbitraryString:
+ _objc_msgSend$pf_cleanupDirectoryAtURL:duration:cancellationFlag:completion:
+ _objc_msgSend$pf_description
+ _objc_msgSend$pf_eachRespondingToSelector:performBlock:
+ _objc_msgSend$pf_errorWithCode:
+ _objc_msgSend$pf_hexadecimalEncodedString
+ _objc_msgSend$pf_isDirectory
+ _objc_msgSend$pf_isReachable
+ _objc_msgSend$pf_isReadable
+ _objc_msgSend$pf_isWritable
+ _objc_msgSend$pf_posterKitContainerTrashURL
+ _objc_msgSend$pf_setExcludedFromBackup:error:
+ _objc_msgSend$pf_setPurgable:afterDate:error:
+ _objc_msgSend$pf_temporaryDirectoryURL
+ _objc_msgSend$pf_temporaryDirectoryURLWithBasenamePrefix:error:
+ _objc_msgSend$pinnedDisplay
+ _objc_msgSend$policy
+ _objc_msgSend$posterConfigurationIdentity
+ _objc_msgSend$posterExtensionBundleIdentifier
+ _objc_msgSend$posterVersion
+ _objc_msgSend$postersAtURL:error:
+ _objc_msgSend$postersByProvider
+ _objc_msgSend$pr_updateDescriptors:sessionInfo:
+ _objc_msgSend$prepareFileSystemForEndpoints:error:
+ _objc_msgSend$promise
+ _objc_msgSend$providerWithBackgroundConcurrencyLimit:
+ _objc_msgSend$prs_entitlementFailureErrorWithFile:line:entitlement:
+ _objc_msgSend$prs_posterProvider
+ _objc_msgSend$pushPosterGalleryUpdate:forRole:completion:
+ _objc_msgSend$queuePosterDescriptorUpdateForExtension:sessionInfo:completion:
+ _objc_msgSend$reapEverything
+ _objc_msgSend$reapEverythingForChannel:
+ _objc_msgSend$reapOptions
+ _objc_msgSend$reapStaleSnapshots
+ _objc_msgSend$reapStaleSnapshotsForChannel:
+ _objc_msgSend$reapStaleStateForChannel:omittingLast:
+ _objc_msgSend$reapStaleStateForChannel:omittingLast:completion:
+ _objc_msgSend$reapStaleStateForChannel:omittingLast:error:
+ _objc_msgSend$reapStaleStateOmittingLast:
+ _objc_msgSend$reapStaleStateOmittingLast:error:
+ _objc_msgSend$relinquishExtensionInstance:
+ _objc_msgSend$relinquishExtensionInstance:reason:
+ _objc_msgSend$relinquishExtensionInstanceWithIdentifier:reason:
+ _objc_msgSend$remoteToken
+ _objc_msgSend$removeChannel:completion:
+ _objc_msgSend$removeChannelObserver:
+ _objc_msgSend$removeChannelWithFuture:
+ _objc_msgSend$removeChannelWithIdentifier:error:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removedPosters
+ _objc_msgSend$requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:
+ _objc_msgSend$requestLockScreenHomeScreenColorConfigurations:
+ _objc_msgSend$resolveEndpoint:
+ _objc_msgSend$result:
+ _objc_msgSend$retrieveGalleryForRole:completion:
+ _objc_msgSend$rootChannelURLEndpoint
+ _objc_msgSend$schemaManager
+ _objc_msgSend$serialDispatchQueueSchedulerWithName:qualityOfService:
+ _objc_msgSend$server:fetchGalleryForRole:completion:
+ _objc_msgSend$server:forceUpdatePosterPath:updates:completion:
+ _objc_msgSend$server:generatePlatformReferenceSnapshotsWithCompletion:
+ _objc_msgSend$server:notePosterConfigurationUnderlyingModelDidChange:completion:
+ _objc_msgSend$server:pushPosterGalleryUpdate:forRole:completion:
+ _objc_msgSend$server:queuePosterDescriptorUpdateForExtension:sessionInfo:completion:
+ _objc_msgSend$server:requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:
+ _objc_msgSend$server:retrieveGalleryForRole:completion:
+ _objc_msgSend$setAllowsUnknownDisplays:
+ _objc_msgSend$setChannelContext:
+ _objc_msgSend$setClass:forClassName:
+ _objc_msgSend$setClassName:forClass:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setCountStyle:
+ _objc_msgSend$setExtensionIdentifiers:
+ _objc_msgSend$setMigratedConfigurationMatchingMask:
+ _objc_msgSend$setPolicy:
+ _objc_msgSend$setPosterConfiguration:
+ _objc_msgSend$setSupportedRoles:
+ _objc_msgSend$setUpdateSessionInfoProvider:
+ _objc_msgSend$setupPersistenceForPathContainerURL:error:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$signal
+ _objc_msgSend$signingIdentifier
+ _objc_msgSend$stageCreateEndpoint:
+ _objc_msgSend$start
+ _objc_msgSend$startWithImmediateQueryExecution:
+ _objc_msgSend$state
+ _objc_msgSend$stringForObjectValue:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$supplementURL
+ _objc_msgSend$supportedRoles
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$unlock
+ _objc_msgSend$updateChannel:updater:
+ _objc_msgSend$updateChannel:updater:error:
+ _objc_msgSend$updateGalleryForChannel:fetchOptions:
+ _objc_msgSend$updateGalleryWithFetchOptions:
+ _objc_msgSend$updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:
+ _objc_msgSend$updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:completion:
+ _objc_msgSend$updateSessionInfoForExtensionIdentifier:
+ _objc_msgSend$updateSessionInfoProvider
+ _objc_msgSend$updatedPosters
+ _objc_msgSend$userInfo
+ _objc_msgSend$userInfoPersistenceClasses
+ _objc_msgSend$userInterfaceStyle
+ _objc_msgSend$wallpaperPublisherDidUpdatePinnedDisplays:
+ _objc_msgSend$weakObjectsHashTable
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_terminate
+ _os_signpost_enabled
+ _sharedCache.onceToken
+ _sharedCache.sharedCache
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_coroFrameAlloc
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $s19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegateP
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic SS6reason_t
+ _symbolic SS9parameter_t
+ _symbolic SaySo21PFFileSystemStagedURLCG
+ _symbolic Sb
+ _symbolic Si
+ _symbolic So20PFFileSystemEndpointC
+ _symbolic So21PRSPosterChannelStateC
+ _symbolic So21PRSPosterChannelStateCSg
+ _symbolic So22PRSPosterChannelReaperC
+ _symbolic So25PFFileSystemSchemaManagerC
+ _symbolic So32PRSPosterChannelModelCoordinatorC
+ _symbolic So7NSErrorC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 19PosterBoardServices32PRSPosterChannelStateCoordinatorC
+ _symbolic _____ 19PosterBoardServices32PRSPosterChannelStateCoordinatorC0defG5ErrorO
+ _symbolic _____ 19PosterBoardServices42PRSPosterChannelStateCoordinatorTransitionC
+ _symbolic _____ 19PosterBoardServices42PRSPosterChannelStateCoordinatorTransitionC0defgH5ErrorO
+ _symbolic _____ SC11PFErrorCodeLeV
+ _symbolic _____ So11PFErrorCodeV
+ _symbolic _____ So16NSURLResourceKeya
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So18NSFileAttributeKeya
+ _symbolic _____ s6UInt32V
+ _symbolic _____17channelIdentifier_t 10Foundation4UUIDV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic ______pSgXw 19PosterBoardServices40PRSPosterChannelStateCoordinatorDelegateP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo20PFFileSystemEndpointCG s11_SetStorageC
+ _symbolic _____ySuG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____yytG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yyt_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic ySo21PRSPosterChannelStateCSg07initialC0_AB05finalC0So20PFFileSystemEndpointC04rootB11URLEndpointSo0fG13SchemaManagerC06schemaL0t_tKcSg
+ _symbolic ypSg
+ _type_layout_string 19PosterBoardServices42PRSPosterChannelStateCoordinatorTransitionC0defgH5ErrorO
+ _type_layout_string SC11PFErrorCodeLeV
+ _type_layout_string So16os_unfair_lock_sV
+ _type_layout_string So18NSFileAttributeKeya
- +[NSError(PRSAdditions) prs_entitlementFailureErrorWithFile:line:]
- -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:]
- -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:].cold.1
- -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:].cold.1
- -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:].cold.2
- -[PRSServer fetchGallery:]
- -[PRSServer notePosterConfigurationUnderlyingModelDidChange:]
- -[PRSServer pushPosterGalleryUpdate:completion:]
- -[PRSServer retrieveGallery:]
- -[PRSService fetchGallery:].cold.1
- -[PRSService pushPosterGalleryUpdate:completion:].cold.1
- -[PRSService pushPosterGalleryUpdate:completion:].cold.2
- -[PRSService retrieveGallery:].cold.1
- GCC_except_table50
- GCC_except_table68
- GCC_except_table69
- GCC_except_table77
- GCC_except_table88
- GCC_except_table89
- GCC_except_table90
- GCC_except_table91
- GCC_except_table92
- GCC_except_table93
- GCC_except_table94
- GCC_except_table95
- GCC_except_table96
- GCC_except_table97
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- __OBJC_$_INSTANCE_METHODS_PRSPosterConfiguration
- ___103-[PRSServer createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:]_block_invoke.21
- ___18-[PRSService init]_block_invoke.8
- ___18-[PRSService init]_block_invoke.8.cold.1
- ___26-[PRSServer fetchGallery:]_block_invoke
- ___27-[PRSService fetchGallery:]_block_invoke
- ___27-[PRSService fetchGallery:]_block_invoke.cold.1
- ___29-[PRSServer retrieveGallery:]_block_invoke
- ___30-[PRSService retrieveGallery:]_block_invoke
- ___30-[PRSService retrieveGallery:]_block_invoke.cold.1
- ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.24
- ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke.24.cold.1
- ___48-[PRSServer pushPosterGalleryUpdate:completion:]_block_invoke
- ___49-[PRSService pushPosterGalleryUpdate:completion:]_block_invoke
- ___49-[PRSService pushPosterGalleryUpdate:completion:]_block_invoke.cold.1
- ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.174
- ___50-[PRSWallpaperObserver activateWithConfiguration:]_block_invoke.175
- ___55-[PRSServer listener:didReceiveConnection:withContext:]_block_invoke.9
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.156
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.156.cold.1
- ___73-[PRSServer refreshPosterDescriptorsForExtension:sessionInfo:completion:]_block_invoke.17
- ___75-[PRSServer refreshPosterConfigurationMatchingUUID:sessionInfo:completion:]_block_invoke.26
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.152
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.154
- ___block_descriptor_52_e8_32s40s_e25_v16?0"<BSXPCEncoding>"8ls32l8s40l8
- ___block_literal_global.12
- ___block_literal_global.21
- ___block_literal_global.23
- ___block_literal_global.28
- ___block_literal_global.3
- ___block_literal_global.348
- ___block_literal_global.53
- ___block_literal_global.56
- _objc_msgSend$auditToken
- _objc_msgSend$connectedScenes
- _objc_msgSend$fetchGallery:
- _objc_msgSend$initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:
- _objc_msgSend$initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:
- _objc_msgSend$name
- _objc_msgSend$pf_temporaryDirectoryURLWithBasenamePrefix:
- _objc_msgSend$prs_entitlementFailureErrorWithFile:line:
- _objc_msgSend$pushPosterGalleryUpdate:completion:
- _objc_msgSend$remoteProcess
- _objc_msgSend$retrieveGallery:
- _objc_msgSend$server:fetchGallery:
- _objc_msgSend$server:notePosterConfigurationUnderlyingModelDidChange:
- _objc_msgSend$server:pushPosterGalleryUpdate:completion:
- _objc_msgSend$server:retrieveGallery:
CStrings:
+ ""
+ "\f"
+ " - (channelIdentifier: "
+ " - (creationDate: "
+ "%@-%@"
+ "%@-CompletionQueue"
+ "%@-ModelCoordinatorQueue"
+ "%@-ObserverQueue"
+ "%@-ReapQueue"
+ "%@:%@-CompletionQueue"
+ "%@:%@-ObserverQueue"
+ "%s Elapsed time: %f seconds"
+ "%s Elapsed time: %f seconds."
+ "%s commit non-staged updates"
+ "%s commit staged updates"
+ "%s copying [%s (%s), %s (%s)] to staging"
+ "%s creating %s"
+ "%s error encountered while preparing staging: %s"
+ "%s error encountered while reaping unexpected url: %s"
+ "%s error encountered while reaping: %s"
+ "%s error executing state transition: %s"
+ "%s error processing descriptors for provider '%s': %s"
+ "%s error: %s"
+ "%s nothing to reap at %s"
+ "%s pid=%d signingID=%{public}@"
+ "%s prepareStateTransitionStagingURL"
+ "%s processing descriptors for provider '%s': %@"
+ "%s reaped %s"
+ "%s reaping unexpected url for reason '%s': %s"
+ "%s rejected: pid=%d signingID=%{public}@ hasEntitlement=%d"
+ "%s trying to reap %s"
+ "%{public}@ %{public}@"
+ "%{public}@ Relinquish extensionInstance for reason %{public}@: %{public}@"
+ "%{public}@ execution timed out: %{public}lu"
+ "%{public}@ finish task with result: %{public}@, error: %{public}@"
+ "(1) precheck"
+ "(2) setup"
+ "(3) fire up some extensions, get descriptors"
+ "(4a) finish updates"
+ "(4b) make sure we're not invalidated"
+ "(5) build gallery metadata"
+ "(6) ingest updates"
+ "(7) get updated descriptors"
+ "(8) cleanup"
+ "(9) finish"
+ ", channelContext: "
+ ", channelVersion: "
+ ", creationDate: "
+ ", lastModifiedDate: "
+ ", posterConfigurationIdentity: "
+ ", posterVersion: "
+ "-[PRSServer commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:]"
+ "-[PRSServer deleteHostConfigurationForRole:completion:]"
+ "-[PRSServer exportArchivedDataStoreNamed:completion:]"
+ "-[PRSServer exportCurrentDataStoreToURL:options:sandboxToken:error:]"
+ "-[PRSServer fetchContentCutoutBoundsForPosterConfiguration:orientation:completion:]"
+ "-[PRSServer fetchContentObstructionBoundsForPosterConfiguration:orientation:completion:]"
+ "-[PRSServer fetchExtendedContentCutoutBoundsForOrientation:completion:]"
+ "-[PRSServer fetchFocusUUIDForConfiguration:completion:]"
+ "-[PRSServer fetchGalleryForRole:completion:]"
+ "-[PRSServer fetchLimitedOcclusionBoundsForPosterConfiguration:orientation:completion:]"
+ "-[PRSServer fetchMaximalContentCutoutBoundsForOrientation:completion:]"
+ "-[PRSServer fetchObscurableBoundsForPosterConfiguration:orientation:completion:]"
+ "-[PRSServer fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:]"
+ "-[PRSServer forceUpdatePosterPath:updates:completion:]"
+ "-[PRSServer generatePlatformReferenceSnapshotsWithCompletion:]"
+ "-[PRSServer notePosterConfigurationUnderlyingModelDidChange:completion:]"
+ "-[PRSServer pushPosterGalleryUpdate:forRole:completion:]"
+ "-[PRSServer queuePosterDescriptorUpdateForExtension:sessionInfo:completion:]"
+ "-[PRSServer refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:]"
+ "-[PRSServer removeAllFocusConfigurationsMatchingFocusUUID:completion:]"
+ "-[PRSServer requestImmediateDescriptorUpdateForExtension:exceptionalReason:sessionInfo:completion:]"
+ "-[PRSServer requestLockScreenHomeScreenColorConfigurations:]"
+ "-[PRSServer retrieveGalleryForRole:completion:]"
+ "-[PRSServer setHostConfiguration:forRole:completion:]"
+ "-[PRSServer updatePosterConfigurationsFromHostForRole:completion:]"
+ "/private/var/mobile/Library/SpringBoard/LockScreenColorConfigurations.plist"
+ "<%@:%p, role: %@, userInfo: %@>"
+ "<%{public}@:%p> failed to extend host storage access to %{public}@: %{public}@"
+ "<%{public}s:%{public}@> %{public}s did not provide any updates."
+ "<%{public}s:%{public}@> Failed to prepare file system for snapshot cache: %@"
+ "<PRSPosterChannelControlling:%@:%@>"
+ "@\"<PFTFuture>\"16@?0@\"NSDictionary\"8"
+ "@\"<PFTFuture>\"16@?0@\"NSSet\"8"
+ "@\"<PFTFuture>\"16@?0@\"PRSPosterDescriptorCollection\"8"
+ "@\"PFTFuture\"8@?0"
+ "@16@?0@\"NSUUID\"8"
+ "@16@?0^@8"
+ "About to be removed."
+ "Adding Connection: %{public}@ pid=%d signingID=%{public}@"
+ "Archive data preview: %s"
+ "B16@?0@\"PFPosterExtension\"8"
+ "Cache schema version mismatch"
+ "Cannot relinquish extension instance for reason %{public}@, because Poster Configuration Extension Identifier was nil"
+ "Channel %@ is not owned by this controller and it is an outrage for you to ask for it."
+ "Channel %@ w/ identifier already exists"
+ "Channel identifier '%@' does not exist."
+ "Channel reap failed; skipping trash cleanup. Underlying error: %{public}@"
+ "Channel state coordinator is nil for %{public}@"
+ "ChannelVersionTransition-"
+ "Channels"
+ "Class getPRPosterPathModelObjectCacheClass(void)_block_invoke"
+ "Cleanup"
+ "ClientSPI"
+ "ColorConfigCache"
+ "CommitTransition"
+ "Contents"
+ "DG"
+ "Dark"
+ "Data"
+ "DayZero"
+ "Encountered invalid gallery creation date. Returning [NSDate distantPast]."
+ "Entitlement failure at %{public}@: missing entitlement %{public}@"
+ "Epoch 0 is invalid or xattr missing"
+ "Error unarchiving gallery metadata: %s"
+ "ExecuteTransition"
+ "ExecuteWithState-V%lu"
+ "ExecutionTimedOut"
+ "Failed to load channel %{public}@: %{public}@"
+ "File system location does not exist for URL %@: %@"
+ "FinishWithResult-V%lu"
+ "Gallery processor was invalidated."
+ "High"
+ "InUseAssertionProvider"
+ "IngestUpdatedDescriptors"
+ "Invalidated"
+ "Invalidated."
+ "Landscape"
+ "Light"
+ "Model access failed with exception: %@"
+ "NeverFeature"
+ "Nil removal block."
+ "No channel exists for %@"
+ "Normal"
+ "OS version mismatch or file missing"
+ "PFPosterRoleIsValid(role)"
+ "PRPosterPathModelObjectCache"
+ "PRSColorConfigCache_Read"
+ "PRSDisplayInfo initWithBSXPCCoder: exception decoding displayConfiguration: %{public}@"
+ "PRSDisplayInfo initWithCoder: exception decoding displayConfiguration: %{public}@"
+ "PRSHostContext init: exception reading bounds/scale for screen %lu: %{public}@"
+ "PRSHostContext init: exception reading displayConfiguration for screen %lu: %{public}@"
+ "PRSHostContext init: exception resolving orientation for screen %lu: %{public}@"
+ "PRSHostContext init: skipping screen %lu — no valid orientation"
+ "PRSHostContext init: unexpected exception processing screen: %{public}@"
+ "PRSLockScreenColorConfigurationCache"
+ "PRSLockScreenColorConfigurationCache: loaded %lu configurations at epoch %llu"
+ "PRSPosterChannel.m"
+ "PRSPosterChannelContext"
+ "PRSPosterChannelContext.m"
+ "PRSPosterChannelController is invalid"
+ "PRSPosterChannelController.m"
+ "PRSPosterChannelGalleryCoordinator invalidation"
+ "PRSPosterChannelGalleryCoordinator-%@"
+ "PRSPosterChannelGalleryCoordinator.m"
+ "PRSPosterChannelIngestUpdatedDescriptors"
+ "PRSPosterChannelModelCoordinator"
+ "PRSPosterChannelModelCoordinator.m"
+ "PRSPosterChannelState"
+ "PRSPosterConfigurationFinalizer.m"
+ "PRSPosterConfigurationFinalizerErrorDomain"
+ "PRSPosterGalleryMetadata"
+ "PRSServer accepted connection: %{public}@ pid=%d signingID=%{public}@ hasEntitlement=%d"
+ "PRSServer received connection invalidation: %{public}@ pid=%d signingID=%{public}@"
+ "PRSServer rejected connection: %{public}@ pid=%d signingID=%{public}@ hasEntitlement=%d"
+ "PRSServerErrorDomain"
+ "PRSWallpaperDisplayPin initWithBSXPCCoder: exception decoding displayConfiguration: %{public}@"
+ "PRSWallpaperDisplayPin initWithBSXPCCoder: exception decoding displayIdentity: %{public}@"
+ "PRSWallpaperDisplayPin initWithBSXPCCoder: failed to decode - no displayIdentity or displayConfiguration found"
+ "PRSWallpaperDisplayPin initWithCoder: exception decoding displayConfiguration: %{public}@"
+ "PRSWallpaperDisplayPin initWithCoder: exception decoding displayIdentity: %{public}@"
+ "PRSWallpaperDisplayPin initWithCoder: failed to decode - no displayIdentity or displayConfiguration found"
+ "PRSWallpaperDisplayPin.m"
+ "PRUISPosterChannelContext"
+ "PRUISPosterChannelState"
+ "PRUISPosterGalleryMetadata"
+ "Passed Role is not supported by this platform."
+ "Passed URL is a file; PRSPosterChannelConfiguration necessitates directory."
+ "Passed URL is not readable; PRSPosterChannelConfiguration necessitates a directory that can be read by this process."
+ "Passed URL is not readwrite; PRSPosterChannelConfiguration necessitates a readwrite directory."
+ "Poster Configuration Extension Identifier was nil"
+ "PosterBoardServices.PRSPosterChannelReaper"
+ "PosterBoardServices.PRSPosterChannelState"
+ "PosterBoardServices.PRSPosterChannelStateCoordinator"
+ "PosterBoardServices.PRSPosterChannelStateCoordinatorTransition"
+ "PosterBoardServices.PRSPosterGalleryMetadata"
+ "PosterBoardUIServices.PRUISPosterChannelContext"
+ "PosterBoardUIServices.PRUISPosterChannelState"
+ "PosterBoardUIServices.PRUISPosterGalleryMetadata"
+ "PrepareStateTransitionStagingURL"
+ "Removing Connection: %{public}@ pid=%d signingID=%{public}@"
+ "Role is incorrect for this channel"
+ "Server"
+ "State transition could not be created for UUID %@"
+ "StateCoordinator"
+ "StateCoordinatorTransition"
+ "Trash cleanup after channel reap failed: %{public}@"
+ "URL is not readable"
+ "URL is not writable"
+ "Unable to create channel for identifier %@"
+ "Unable to instantiate model provider"
+ "Undefined"
+ "Unknown exception during unarchive"
+ "Unspecified"
+ "UpdateDescriptorsTask"
+ "UserInitiated"
+ "[%@][%@][%@][%@]"
+ "[ReapOnChannelUpdate][GalleryUpdate] Reaping stale data from channel identifier %{public}@"
+ "[ReapOnChannelUpdate][StateUpdate] Reaping stale data from channel identifier %{public}@"
+ "[ReapOnStartup] Reaping stale data from channel identifier %{public}@"
+ "_cachedLockScreenColorConfigurations: cache file readable but load failed (%{public}@)"
+ "_cachedLockScreenColorConfigurations: cache hit (%lu configs)"
+ "_displayConfiguration"
+ "_displayIdentity"
+ "_migratedConfigurationMatchingMask"
+ "badKeys"
+ "begin"
+ "cache hit epoch=%llu"
+ "cannot proceed with execution"
+ "channel"
+ "channel already exists; cannot create anew"
+ "channel was invalidated"
+ "channel was updated before descriptors were ingested."
+ "channelConfiguration"
+ "channelDB.sqlite"
+ "channelDescriptorVersions"
+ "channelDescriptors"
+ "channelIdentifier"
+ "channelInfo.plist"
+ "channelPosterVersions"
+ "channelStatesWithError"
+ "com.apple.posterboard.cache.epoch"
+ "com.apple.posterboard.cache.osversion"
+ "com.apple.posterboard.cache.schemaversion"
+ "com.apple.posterboardservices.data-store.mutateConfigurationHostStorage"
+ "createChannelWithIdentifier"
+ "creationDate"
+ "descriptors"
+ "deserialized %lu configs"
+ "displayIdentity"
+ "end"
+ "end at execution phase: %@"
+ "entitlement"
+ "er"
+ "exceptionalReason must be an NSString"
+ "extensionProvider"
+ "fetchLockScreenWallpaperForRequest: Error creating temporary directory: %{public}@"
+ "file read failed"
+ "finished pre-checks, proceed with execution"
+ "force RPC failed on %{public}@: %{public}@"
+ "force RPC reply received on %{public}@"
+ "forceUpdatePosterPath: nil path"
+ "galleryMetadata.plist"
+ "galleryProcessor returned nil future"
+ "in progress"
+ "init()"
+ "invalid epoch"
+ "lastModifiedDate"
+ "migratedConfigurationMatchingMask"
+ "modelCoordinator"
+ "no known poster extensions, exiting early with an empty gallery"
+ "not a valid version number"
+ "observer"
+ "os version mismatch"
+ "pinnedDisplay"
+ "pooledExtensionInstance"
+ "posterConfigurationIdentity"
+ "provided userInfo was not using Foundation classes for persistence."
+ "reapEverything"
+ "reapStaleSnapshots"
+ "reapStaleSnapshots called on base PRSPosterChannel (no snapshots to reap). This is expected for daemon usage."
+ "reapStaleState"
+ "reason"
+ "received ERROR reply to %{public}@ on %{public}@: %{public}@"
+ "removeChannel"
+ "schema version mismatch"
+ "service channel gallery fetch"
+ "signingIdentifier"
+ "snapshotDisplayConfiguration"
+ "state"
+ "task cancelled with reason: %@"
+ "task execution did timeout"
+ "timedout"
+ "traitCollection"
+ "transition has invalid channel identifier for final state"
+ "transition has invalid channel identifier for initial state"
+ "unarchive exception"
+ "unarchive failed"
+ "unknown error occured"
+ "update descriptors task was cancelled"
+ "updateChannel"
+ "updater"
+ "v16@?0@\"<BSCompoundAssertionState>\"8"
+ "v16@?0@\"<PRSPosterChannelControllerObserver>\"8"
+ "v16@?0@\"<PRSPosterChannelObserver>\"8"
+ "v16@?0@\"NSNull\"8"
+ "v16@?0@\"PRSPosterChannel\"8"
+ "v16@?0@\"PRSPosterChannelController\"8"
+ "v16@?0@\"PRSPosterGallery\"8"
+ "v16@?0@\"_PRSPosterChannelUpdateDescriptorsTask\"8"
+ "v24@?0@\"<PRSPosterChannelModelAccessing>\"8^@16"
+ "v24@?0@\"<PRSPosterChannelModelMutating>\"8^@16"
+ "v24@?0@\"NSNull\"8@\"NSError\"16"
+ "v24@?0@\"PFPosterExtensionInstance\"8^B16"
+ "v24@?0@\"PRSPosterChannel\"8@\"NSError\"16"
+ "v24@?0@\"PRSPosterGallery\"8@\"NSError\"16"
+ "v24@?0@8@\"NSError\"16"
+ "v24@?0q8@\"NSString\"16"
+ "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
+ "v32@?0@\"NSURL\"8@\"NSNumber\"16@\"NSError\"24"
+ "v32@?0@8@16^B24"
+ "void PRSLogIncomingMethodCall(const char *)"
- "#16@0:8"
- "-[PRSServer fetchGallery:]"
- "-[PRSServer notePosterConfigurationUnderlyingModelDidChange:]"
- "-[PRSServer pushPosterGalleryUpdate:completion:]"
- "-[PRSServer retrieveGallery:]"
- ".cxx_destruct"
- "@"
- "@\"<BSInvalidatable>\""
- "@\"<PRSServerDelegate>\""
- "@\"<PRSWallpaperObserving>\""
- "@\"<PRSWallpaperPublisherDelegate>\""
- "@\"BSAuditToken\""
- "@\"BSAuditToken\"24@0:8o^@16"
- "@\"BSColor\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSServiceConnection<BSServiceConnectionClient>\""
- "@\"BSServiceConnection<BSServiceConnectionHost>\""
- "@\"BSServiceConnectionListener\""
- "@\"FBSDisplayIdentity\""
- "@\"INIntent\""
- "@\"IOSurface\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSFileManager\""
- "@\"NSLocale\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSOrderedSet\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"PFPosterArchiver\""
- "@\"PFPosterPath\""
- "@\"PFPosterPath\"16@0:8"
- "@\"PFServerPosterIdentity\""
- "@\"PFServerPosterPath\""
- "@\"PRSActivePosterConfiguration\"32@0:8@\"NSString\"16o^@24"
- "@\"PRSCodableImage\""
- "@\"PRSDisplayInfo\""
- "@\"PRSHostContext\""
- "@\"PRSPosterConfiguration\""
- "@\"PRSPosterGalleryItemOptions\""
- "@\"PRSPosterGallerySuggestedComplication\""
- "@\"PRSPosterRoleActivePosterObserver\""
- "@\"PRSPosterRoleCollectionObserver\""
- "@\"PRSPosterSnapshot\""
- "@\"PRSPosterUpdate\""
- "@\"PRSPosterUpdateColorPayload\""
- "@\"PRSPosterUpdatePayload\""
- "@\"PRSPosterUpdateSessionInfo\""
- "@\"PRSService\""
- "@\"PRSWallpaperLocationStateObserver\""
- "@\"PRSWallpaperPublisher\""
- "@\"PRSWallpaperSnapshotObserver\""
- "@\"RBSAssertion\""
- "@\"WFWallpaperConfiguration\""
- "@104@0:8@16@24d32q40q48q56@64{CGRect={CGPoint=dd}{CGSize=dd}}72"
- "@112@0:8@16@24@32B40B44q48@56@64@72B80B84q88q96B104B108"
- "@160@0:8@16@24@32@40@48@56@64@72@80@88@96q104@112@120@128@136B144B148q152"
- "@168@0:8@16@24@32@40@48@56@64@72@80@88@96@104q112@120@128@136@144B152B156q160"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8o^@16"
- "@24@0:8q16"
- "@24@0:8r^@16"
- "@28@0:8@16B24"
- "@28@0:8r*16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16o^@24"
- "@32@0:8Q16@24"
- "@32@0:8^{CGImage=}16o^@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24o^@32"
- "@40@0:8@16@24q32"
- "@40@0:8@16d24o^@32"
- "@40@0:8@16q24Q32"
- "@40@0:8@16q24o^@32"
- "@40@0:8Q16@24@32"
- "@40@0:8^{CGImage=}16d24o^@32"
- "@40@0:8q16@24@32"
- "@40@0:8q16q24Q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16q24@32o^@40"
- "@48@0:8@16q24Q32q40"
- "@48@0:8q16q24Q32q40"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40q48"
- "@56@0:8@16@24d32q40q48"
- "@56@0:8@16Q24Q32@40Q48"
- "@56@0:8@16q24q32Q40Q48"
- "@56@0:8q16q24Q32q40@48"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40Q48@56"
- "@64@0:8@16@24@32q40@48q56"
- "@64@0:8@16q24@32@40q48q56"
- "@64@0:8@16q24q32Q40d48Q56"
- "@72@0:8@16@24@32@40Q48Q56@64"
- "@72@0:8@16@24d32q40q48q56@64"
- "@72@0:8@16q24q32Q40d48q56Q64"
- "@76@0:8@16q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64B72"
- "@80@0:8q16@24@32@40@48@56@64@72"
- "@88@0:8q16@24@32@40@48@56@64@72@80"
- "@?"
- "@?16@0:8"
- "Adding Connection: %{public}@"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<CHSWidgetPersonality>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16o^@24"
- "B40@0:8q16@24@32"
- "BSDescriptionProviding"
- "BSInvalidatable"
- "BSServiceConnectionListenerDelegate"
- "BSXPCSecureCoding"
- "CGImage"
- "CHSWidgetPersonality"
- "DF"
- "Deprecated"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "PFPosterContents"
- "PRSActivePosterConfiguration"
- "PRSAdditions"
- "PRSBehaviorAggregator"
- "PRSClientToServerInterface"
- "PRSCodableImage"
- "PRSControl"
- "PRSDataStoreArchiveConfiguration"
- "PRSDisplayInfo"
- "PRSExternalSystemService"
- "PRSGadget"
- "PRSHostConfiguration"
- "PRSHostConfigurationEntry"
- "PRSHostContext"
- "PRSMigrationDescriptor"
- "PRSMutableDataStoreArchiveConfiguration"
- "PRSMutableMigrationDescriptor"
- "PRSMutablePosterConfiguration"
- "PRSMutablePosterDescriptor"
- "PRSPosterArchiver"
- "PRSPosterCollection"
- "PRSPosterConfigurationAttributes"
- "PRSPosterConfigurationCacheProvider"
- "PRSPosterConfigurationCacheProviding"
- "PRSPosterConfigurationCollection"
- "PRSPosterDescriptorCollection"
- "PRSPosterDescriptorCollectionDiff"
- "PRSPosterGalleryItem"
- "PRSPosterGalleryItemOptions"
- "PRSPosterGalleryItemPrototype"
- "PRSPosterGalleryLayout"
- "PRSPosterGalleryLayoutDataStore"
- "PRSPosterGallerySection"
- "PRSPosterGallerySuggestedComplication"
- "PRSPosterIconConfiguration"
- "PRSPosterRoleActivePosterObserver"
- "PRSPosterRoleActivePosterObserverState"
- "PRSPosterRoleCollectionObserver"
- "PRSPosterRoleCollectionObserverUpdate"
- "PRSPosterSnapshot"
- "PRSPosterSnapshotCollection"
- "PRSPosterSnapshotRequest"
- "PRSPosterSnapshotResponse"
- "PRSPosterStaticDescriptorCollection"
- "PRSPosterUpdateComplicationPayload"
- "PRSPosterUpdateDiscreteStylePayload"
- "PRSPosterUpdateHomeScreenAppearancePayload"
- "PRSPosterUpdatePayload"
- "PRSPosterUpdatePropertyListPayload"
- "PRSPosterUpdateResult"
- "PRSPosterUpdateTristatePayload"
- "PRSPosterUpdater"
- "PRSRoleActivePosterObserverUpdate"
- "PRSServer"
- "PRSServer received connection invalidation: %{public}@"
- "PRSServer received connection: %{public}@"
- "PRSServer rejected connection: %{public}@"
- "PRSService"
- "PRSWallpaperClient"
- "PRSWallpaperLocationStateObserver"
- "PRSWallpaperObserver"
- "PRSWallpaperObserverInitializing"
- "PRSWallpaperObserverPathUpdate"
- "PRSWallpaperObserverSnapshotUpdate"
- "PRSWallpaperObserverState"
- "PRSWallpaperObserverTransition"
- "PRSWallpaperObserving"
- "PRSWallpaperPublisher"
- "PRSWallpaperSnapshotObserver"
- "Q"
- "Q16@0:8"
- "Removing Connection: %{public}@"
- "T#,R"
- "T@\"<PRSServerDelegate>\",W,N,V_delegate"
- "T@\"<PRSWallpaperPublisherDelegate>\",&,D,N"
- "T@\"BSAuditToken\",R,N,V_auditToken"
- "T@\"BSColor\",C,D,N"
- "T@\"BSColor\",C,N,V_homeScreenTintColor"
- "T@\"BSColor\",R,C,N,V_titleColor"
- "T@\"BSColor\",R,N,V_accentColor"
- "T@\"BSColor\",R,N,V_color"
- "T@\"FBSDisplayIdentity\",R,N,V_snapshotDisplayIdentity"
- "T@\"INIntent\",&,N,V_intent"
- "T@\"INIntent\",R,N,V_intent"
- "T@\"IOSurface\",R,N"
- "T@\"NSArray\",C,N,V_entries"
- "T@\"NSArray\",R,C,N,V_complications"
- "T@\"NSArray\",R,C,N,V_connectedDisplays"
- "T@\"NSArray\",R,C,N,V_items"
- "T@\"NSArray\",R,C,N,V_landscapeComplications"
- "T@\"NSArray\",R,C,N,V_modularComplications"
- "T@\"NSArray\",R,C,N,V_modularLandscapeComplications"
- "T@\"NSArray\",R,C,N,V_sections"
- "T@\"NSArray\",R,C,N,V_snapshots"
- "T@\"NSArray\",R,C,N,V_suggestionDescriptors"
- "T@\"NSArray\",R,N,V_complications"
- "T@\"NSArray\",R,N,V_posterCollection"
- "T@\"NSArray\",R,N,V_suggestions"
- "T@\"NSData\",&,N"
- "T@\"NSData\",R,C,N,V_propertyListData"
- "T@\"NSDictionary\",&,N,V_assetURLs"
- "T@\"NSDictionary\",&,N,V_context"
- "T@\"NSDictionary\",&,N,V_userInfo"
- "T@\"NSDictionary\",C,D,N"
- "T@\"NSDictionary\",C,N,V_homeScreenIconStyleVariantsForStyles"
- "T@\"NSDictionary\",R,C,N,V_requestOptions"
- "T@\"NSDictionary\",R,N,V_ambientWidgets"
- "T@\"NSError\",R,C,N,V_error"
- "T@\"NSLocale\",R,N,V_locale"
- "T@\"NSNumber\",C,D,N,GisHomeScreenDim"
- "T@\"NSNumber\",C,N,GisHomeScreenDim,V_homeScreenDim"
- "T@\"NSNumber\",R,N,V_alpha"
- "T@\"NSNumber\",R,N,V_luminance"
- "T@\"NSNumber\",R,N,V_modeSemanticType"
- "T@\"NSNumber\",R,N,V_saturation"
- "T@\"NSNumber\",R,N,V_tristate"
- "T@\"NSNumber\",R,N,V_variation"
- "T@\"NSOrderedSet\",R,N,V_posterCollection"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_roles"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N,V_containerBundleIdentifier"
- "T@\"NSString\",C,N,V_descriptorID"
- "T@\"NSString\",C,N,V_extensionBundleIdentifier"
- "T@\"NSString\",C,N,V_extensionID"
- "T@\"NSString\",C,N,V_homeScreenIconSize"
- "T@\"NSString\",C,N,V_homeScreenIconStyle"
- "T@\"NSString\",C,N,V_homeScreenIconStyleVariant"
- "T@\"NSString\",C,N,V_homeScreenIconTintSource"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_kind"
- "T@\"NSString\",C,N,V_uniqueIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,D,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_associatedAppBundleIdentifier"
- "T@\"NSString\",R,C,N,V_containerBundleIdentifier"
- "T@\"NSString\",R,C,N,V_descriptiveTextLocalizationKey"
- "T@\"NSString\",R,C,N,V_descriptorIdentifier"
- "T@\"NSString\",R,C,N,V_displayNameLocalizationKey"
- "T@\"NSString\",R,C,N,V_extensionBundleIdentifier"
- "T@\"NSString\",R,C,N,V_focusModeUUID"
- "T@\"NSString\",R,C,N,V_hardwareIdentifier"
- "T@\"NSString\",R,C,N,V_homeProviderIdentifier"
- "T@\"NSString\",R,C,N,V_hostApplicationIdentifier"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_kind"
- "T@\"NSString\",R,C,N,V_localizedDescriptiveText"
- "T@\"NSString\",R,C,N,V_localizedDisplayName"
- "T@\"NSString\",R,C,N,V_localizedSubtitle"
- "T@\"NSString\",R,C,N,V_localizedTitle"
- "T@\"NSString\",R,C,N,V_modeUUID"
- "T@\"NSString\",R,C,N,V_spokenNameLocalizationKey"
- "T@\"NSString\",R,C,N,V_symbolColorName"
- "T@\"NSString\",R,C,N,V_symbolImageName"
- "T@\"NSString\",R,C,N,V_titleFontName"
- "T@\"NSString\",R,C,N,V_unityDescription"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_descriptorIdentifier"
- "T@\"NSString\",R,N,V_extensionIdentifier"
- "T@\"NSString\",R,N,V_role"
- "T@\"NSString\",R,N,V_snapshotType"
- "T@\"NSURL\",R,C,D,N"
- "T@\"NSURL\",R,C,N,V_identifierURL"
- "T@\"NSURL\",R,C,N,V_providerURL"
- "T@\"NSURL\",R,N"
- "T@\"NSUUID\",C,N,V_posterUUID"
- "T@\"NSUUID\",R,C,N,V_posterUUID"
- "T@\"NSUUID\",R,N"
- "T@\"PFPosterPath\",R,N"
- "T@\"PFPosterPath\",R,N,V_path"
- "T@\"PFServerPosterIdentity\",&,N,V_identity"
- "T@\"PFServerPosterPath\",&,N,V_path"
- "T@\"PFServerPosterPath\",R,N,V_activePath"
- "T@\"PFServerPosterPath\",R,N,V_homeScreenConfigurationPath"
- "T@\"PFServerPosterPath\",R,N,V_path"
- "T@\"PFServerPosterPath\",R,N,V_switcherConfigurationPath"
- "T@\"PRSBehaviorAggregator\",R,N"
- "T@\"PRSCodableImage\",R,N,V_codableImage"
- "T@\"PRSDisplayInfo\",R,N,V_primaryDisplayInfo"
- "T@\"PRSHostContext\",&,N,V_hostContext"
- "T@\"PRSPosterConfiguration\",R,N,V_activeHome"
- "T@\"PRSPosterConfiguration\",R,N,V_activeLock"
- "T@\"PRSPosterConfiguration\",R,N,V_activePoster"
- "T@\"PRSPosterConfiguration\",R,N,V_homeScreenPosterConfiguration"
- "T@\"PRSPosterConfiguration\",R,N,V_lockScreenPosterConfiguration"
- "T@\"PRSPosterConfiguration\",R,N,V_posterConfiguration"
- "T@\"PRSPosterConfiguration\",R,N,V_selectedHome"
- "T@\"PRSPosterConfiguration\",R,N,V_selectedLock"
- "T@\"PRSPosterDescriptorCollection\",R,D,N"
- "T@\"PRSPosterGalleryItemOptions\",R,C,N,V_galleryOptions"
- "T@\"PRSPosterGallerySuggestedComplication\",R,C,N,V_inlineComplication"
- "T@\"PRSPosterGallerySuggestedComplication\",R,C,N,V_subtitleComplication"
- "T@\"PRSPosterRoleActivePosterObserver\",&,N,V_activePosterRoleObserver"
- "T@\"PRSPosterRoleCollectionObserver\",&,N,V_postersCollectionRoleObserver"
- "T@\"PRSPosterSnapshot\",R,N,V_floatingLayerSnapshot"
- "T@\"PRSPosterSnapshot\",R,N,V_primaryLayersSnapshot"
- "T@\"PRSPosterUpdate\",R,C,N,V_update"
- "T@\"PRSPosterUpdateColorPayload\",R,C,N,V_gradientColorAppearance"
- "T@\"PRSPosterUpdateColorPayload\",R,C,N,V_solidColorAppearance"
- "T@\"PRSPosterUpdatePayload\",R,N,V_payload"
- "T@\"PRSPosterUpdateSessionInfo\",R,N,V_homeProviderUpdateSessionInfo"
- "T@\"PRSPosterUpdateSessionInfo\",R,N,V_switcherProviderUpdateSessionInfo"
- "T@\"PRSWallpaperLocationStateObserver\",&,N,V_locationStateObserver"
- "T@\"PRSWallpaperSnapshotObserver\",&,N,V_snapshotObserver"
- "T@\"WFWallpaperConfiguration\",&,N,V_shortcutsWallpaperConfiguration"
- "T@,R,C,D,N"
- "T@,R,C,N,V_initialValue"
- "T@,R,C,N,V_propertyListRoot"
- "T@?,C,N,V_handler"
- "T@?,C,V_handler"
- "TB,D,N"
- "TB,N,V_needsSandboxExtensions"
- "TB,N,V_reapNonLatestEntries"
- "TB,N,V_stripContentsOfConfigurations"
- "TB,N,V_stripDescriptors"
- "TB,N,V_stripScreenshots"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisBlankTemplate,V_blankTemplate"
- "TB,R,N,GisEmpty"
- "TB,R,N,GisHero,V_hero"
- "TB,R,N,GisOnlyEligibleForMadeForFocusSection,V_onlyEligibleForMadeForFocusSection"
- "TB,R,N,V_allowsSystemSuggestedComplications"
- "TB,R,N,V_allowsSystemSuggestedComplicationsInLandscape"
- "TB,R,N,V_isMainDisplay"
- "TB,R,N,V_isOffloaded"
- "TB,R,N,V_needsSandboxExtensions"
- "TB,R,N,V_shouldShowAsShuffleStack"
- "TQ,N,V_changed"
- "TQ,N,V_controlType"
- "TQ,N,V_family"
- "TQ,N,V_locations"
- "TQ,R"
- "TQ,R,D,N"
- "TQ,R,N,V_maxCount"
- "TQ,R,N,V_options"
- "TQ,R,N,V_size"
- "TQ,R,N,V_supplementalVersion"
- "TQ,R,N,V_type"
- "TQ,R,N,V_updatedAppearanceType"
- "TQ,R,N,V_variant"
- "TQ,R,N,V_version"
- "T^{CGImage=},R,N"
- "Td,N,V_imageScaleRelativeToScreen"
- "Td,R,N,V_imageScaleRelativeToScreen"
- "Td,R,N,V_pointScale"
- "Td,R,N,V_scale"
- "Td,R,N,V_snapshotScale"
- "Tq,R,D,N"
- "Tq,R,N,V_accessibilityContrast"
- "Tq,R,N,V_configurationType"
- "Tq,R,N,V_featuredConfidenceLevel"
- "Tq,R,N,V_focus"
- "Tq,R,N,V_imageOrientation"
- "Tq,R,N,V_interfaceOrientation"
- "Tq,R,N,V_interfaceStyle"
- "Tq,R,N,V_layoutType"
- "Tq,R,N,V_orientation"
- "Tq,R,N,V_photoSubtype"
- "Tq,R,N,V_source"
- "Tq,R,N,V_type"
- "Tq,R,N,V_userInterfaceStyle"
- "Tq,R,N,V_variant"
- "Tq,R,N,V_widgetFamily"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_salientContentRectangle"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "URLByResolvingSymlinksInPath"
- "URLByStandardizingPath"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@\"NSArray<__PRSPosterRoleCollectionObserverUpdate__>\"16"
- "Vv24@0:8@\"NSArray<__PRSRoleActivePosterObserverUpdate__>\"16"
- "Vv24@0:8@\"NSArray<__PRSWallpaperObserverPathUpdate__>\"16"
- "Vv24@0:8@\"NSArray<__PRSWallpaperObserverSnapshotUpdate__>\"16"
- "Vv24@0:8@\"NSUUID\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"ATXFaceGalleryConfiguration\"@\"NSDate\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSArray<__NSString__>\"@\"NSArray<__NSString__>\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSArray<__NSString__>\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSSet<__NSString__>\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv28@0:8B16@?20"
- "Vv32@0:8@\"ATXFaceGalleryConfiguration\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSArray<__NSUUID__>\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSData\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
- "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSValue\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"PFServerPosterPath\"@\"PFServerPosterPath\"@\"NSError\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"NSUUID\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
- "Vv32@0:8@\"PFServerPosterPath\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
- "Vv32@0:8@\"PRSHostContext\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"PRSPosterSnapshotRequest\"16@?<v@?@\"PRSPosterSnapshotResponse\"@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "Vv32@0:8q16@?24"
- "Vv36@0:8@16B24@?28"
- "Vv36@0:8B16@20@?28"
- "Vv40@0:8@\"NSArray<__PRSWallpaperObserverPathUpdate__>\"16@\"NSArray<__PRSRoleActivePosterObserverUpdate__>\"24@\"PRSPosterRoleCollectionObserverUpdate\"32"
- "Vv40@0:8@\"NSNumber\"16@\"PRSMigrationDescriptor\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"PRSDataStoreArchiveConfiguration\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16@\"NSArray<__PRSPosterUpdate__>\"24@?<v@?@\"PFServerPosterPath\"@\"NSArray<__PRSPosterUpdateResult__>\"@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">32"
- "Vv40@0:8@\"NSUUID\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"PFServerPosterPath\"@\"NSError\">32"
- "Vv40@0:8@\"PRSHostConfiguration\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSArray<__PRSPosterUpdate__>\"24@?<v@?@\"PFServerPosterPath\"@\"NSArray<__PRSPosterUpdateResult__>\"@\"NSError\">32"
- "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSNumber\"24@?<v@?@\"NSArray<__NSValue__>\"@\"NSError\">32"
- "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSNumber\"24@?<v@?@\"NSValue\"@\"NSError\">32"
- "Vv40@0:8@\"PRSPosterSnapshotCollection\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@16@24@32"
- "Vv40@0:8@16@24@?32"
- "Vv40@0:8@16q24@?32"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"PFServerPosterPath\"@\"NSError\">40"
- "Vv48@0:8@\"NSString\"16@\"PFSandboxExtendedURL\"24@\"NSString\"32@?<v@?@\"NSURL\"@\"NSError\">40"
- "Vv48@0:8@16@24@32@?40"
- "[4@\"PFServerPosterIdentity\"]"
- "[4@\"PFServerPosterPath\"]"
- "[4Q]"
- "[4d]"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{CGImage=}24@0:8^@16"
- "^{CGImage=}32@0:8@16o^@24"
- "^{_NSZone=}16@0:8"
- "_accessibilityContrast"
- "_activeHome"
- "_activeLock"
- "_activePath"
- "_activePoster"
- "_activePosterObservedRoles"
- "_activePosterRoleObserver"
- "_active_observedDescription"
- "_allowsSystemSuggestedComplications"
- "_allowsSystemSuggestedComplicationsInLandscape"
- "_ambientWidgets"
- "_assetSandboxHandles"
- "_assetSandboxTokens"
- "_assetURLs"
- "_associatedAppBundleIdentifier"
- "_baseURL"
- "_bitmapSourceData"
- "_blankTemplate"
- "_cachedImage"
- "_changeVersions"
- "_changed"
- "_codableImage"
- "_conn_activePosterRoles"
- "_conn_configurationByIdentity"
- "_conn_identityLocations"
- "_conn_knownPostersCollection"
- "_conn_knownPostersCollectionRole"
- "_conn_posterUUIDToSuggestions"
- "_conn_roleToActivePosterConfiguration"
- "_connection"
- "_connectionListener"
- "_connections"
- "_containerBundleIdentifier"
- "_context"
- "_controlType"
- "_delegate"
- "_description"
- "_descriptiveTextLocalizationKey"
- "_descriptorIdentifier"
- "_displayNameLocalizationKey"
- "_explanation"
- "_extensionBundleIdentifier"
- "_extensionIdentifier"
- "_family"
- "_featuredConfidenceLevel"
- "_fileManager"
- "_floatingLayerSnapshot"
- "_focus"
- "_focusModeUUID"
- "_galleryOptions"
- "_handler"
- "_hero"
- "_homeURL"
- "_identifier"
- "_identifierURL"
- "_identity"
- "_imageScaleRelativeToScreen"
- "_init"
- "_initWithChanged:"
- "_initWithPath:"
- "_initWithPath:extensionIdentifier:posterUUID:providerURL:version:supplementalVersion:fileManager:"
- "_initWithProvider:type:role:posterUUID:version:supplement:descriptorIdentifier:"
- "_initWithSelectedLock:selectedHome:activeLock:activeHome:"
- "_initWithUpdateType:payload:"
- "_initWithWeakPath:"
- "_initialValue"
- "_initializeClient:"
- "_initializeClient:withKnownIdentities:knownRoles:knownCollection:"
- "_initialized"
- "_inlineComplication"
- "_intent"
- "_interfaceStyle"
- "_isOffloaded"
- "_items"
- "_kind"
- "_landscapeComplications"
- "_lastKnownPosterCollection"
- "_lastPaths"
- "_layoutType"
- "_listener"
- "_locale"
- "_localizedDescriptiveText"
- "_localizedDisplayName"
- "_localizedSubtitle"
- "_localizedTitle"
- "_locationStateObserver"
- "_locations"
- "_lock"
- "_lockURL"
- "_lock_activateClientsIfNeeded"
- "_lock_activated"
- "_lock_buildActivePosterObserverUpdatesForClient:updatedRoles:clientSpecificSuggestionsToPosterUUID:"
- "_lock_buildPosterCollectionUpdatesForClient:role:updatedPosterCollection:"
- "_lock_changeVersionTimestamps"
- "_lock_changeVersions"
- "_lock_clientActivated"
- "_lock_clientInvalidated"
- "_lock_clients"
- "_lock_connection"
- "_lock_delegate"
- "_lock_descriptionIfInvalidPaths:"
- "_lock_initialLocationStateUpdateWasSent"
- "_lock_initialUpdateAssertion"
- "_lock_invalidate"
- "_lock_invalidated"
- "_lock_issuePosterCollectionUpdate:"
- "_lock_issueUpdateForRoles:suggestionsToPosterUUID:"
- "_lock_noteChanged:"
- "_lock_noteSnapshotUpdateForPath:snapshotType:"
- "_lock_pathHandler"
- "_lock_paths"
- "_lock_posterUUIDToSuggestionDescriptorPaths"
- "_lock_readAtURL:"
- "_lock_removeAtURL:"
- "_lock_roleActivePosterObserver"
- "_lock_rolePosterCollectionObserver"
- "_lock_roleToPath"
- "_lock_roleToPosterCollections"
- "_lock_sendStateToClient:"
- "_lock_setupSharedWorkspaceIfNeeded"
- "_lock_snapshotHandler"
- "_lock_writeData:atURL:"
- "_maxCount"
- "_modeSemanticType"
- "_modeUUID"
- "_modularComplications"
- "_modularLandscapeComplications"
- "_needsSandboxExtensions"
- "_observed"
- "_observingPathChanges"
- "_observingRoleActivePostersChanges"
- "_observingRolePosterCollectionChanges"
- "_observingRolePosterCollectionChangesNeedsSandboxExtension"
- "_observingSnapshotChanges"
- "_onlyEligibleForMadeForFocusSection"
- "_options"
- "_pathValidityExtension"
- "_photoSubtype"
- "_populateInterfaceOrientationFromSurfacesIfPossible"
- "_populateSalientContentRectFromSurfacesIfPossible"
- "_posterCollection"
- "_posterCollectionChangesRole"
- "_postersCollectionRoleObserver"
- "_primaryLayersSnapshot"
- "_propertyListRoot"
- "_providerURL"
- "_proxy"
- "_publisher"
- "_queue"
- "_queue_addConnection:"
- "_queue_removeConnection:"
- "_reapNonLatestEntries"
- "_refreshPosterDescriptorsForExtension:sessionInfo:completion:"
- "_representation"
- "_roleActivePosterObservedRolesNeedsSandboxExtension"
- "_roleToState"
- "_roles"
- "_salientContentRectangle"
- "_scale"
- "_sections"
- "_selectConfigurationAndRefreshSnapshot:completion:"
- "_selectedHome"
- "_selectedLock"
- "_service"
- "_serviceConnection"
- "_serviceInterfaceWithError:"
- "_shortcutsWallpaperConfiguration"
- "_shortcutsWallpaperConfigurationSandboxHandle"
- "_shortcutsWallpaperConfigurationSandboxToken"
- "_shouldShowAsShuffleStack"
- "_snapshotDisplayIdentity"
- "_snapshotObserver"
- "_snapshotScale"
- "_snapshotType"
- "_snapshots"
- "_source"
- "_sourceImage"
- "_spokenNameLocalizationKey"
- "_stripContentsOfConfigurations"
- "_stripDescriptors"
- "_stripScreenshots"
- "_subtitleComplication"
- "_suggestionDescriptors"
- "_suggestions"
- "_supplementalVersion"
- "_surface"
- "_symbolColorName"
- "_symbolImageName"
- "_titleColor"
- "_titleFontName"
- "_underlyingArchiver"
- "_uniqueIdentifier"
- "_unityDescription"
- "_url"
- "_validateRequestOptionsOrAbort:"
- "_version"
- "_weakPath"
- "_widgetFamily"
- "abortWithMessage:"
- "acquireWithInvalidationHandler:"
- "activate"
- "activateWithConfiguration:"
- "activeHome"
- "activeLock"
- "activePosterRoleObserver"
- "addIndex:"
- "addObject:"
- "addObjectsFromArray:"
- "addSuccessBlock:andFailureBlock:"
- "allKeys"
- "allObjects"
- "allocWithZone:"
- "allowsSystemSuggestedComplications"
- "allowsSystemSuggestedComplicationsInLandscape"
- "alpha"
- "appendArraySection:withName:skipIfEmpty:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:ifEqualTo:"
- "appendFloat:withName:"
- "appendFormat:"
- "appendInt64:withName:"
- "appendInteger:"
- "appendInteger:counterpart:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendRect:withName:"
- "appendString:"
- "appendString:counterpart:"
- "appendString:withName:"
- "applyUpdateLocally:error:"
- "applyUpdates:error:"
- "applyUpdatesLocally:error:"
- "archiveConfiguration:error:"
- "archiveConfiguration:format:error:"
- "archivePath:format:error:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetDirectory"
- "assetURL"
- "assetURLs"
- "associateConfigurationMatchingUUID:focusModeActivityUUID:completion:"
- "associatedAppBundleIdentifier"
- "attachmentForKey:"
- "attributeWithDomain:name:"
- "auditToken"
- "augmentDownloadablePosterMetadataForApp:bundleURL:bundleIdentifierOverride:completion:"
- "augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:"
- "autorelease"
- "boolValue"
- "bounds"
- "bs_encodeRepresentation:value:withCoder:"
- "bs_filter:"
- "bs_map:"
- "bs_mapNoNulls:"
- "bs_safeAddObject:"
- "bs_safeObjectForKey:ofType:"
- "bs_secureEncoded"
- "build"
- "buildCGImageWithError:"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bundleID"
- "bundleIdentifier"
- "canUpdatesBeAppliedLocally:"
- "caseInsensitiveCompare:"
- "changed"
- "characterSetWithCharactersInString:"
- "checkResourceIsReachableAndReturnError:"
- "class"
- "clearMigrationFlags:"
- "cliOptions"
- "code"
- "color"
- "commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:"
- "compare:options:"
- "complications"
- "componentsJoinedByString:"
- "configurationIdentityWithProvider:identifier:role:posterUUID:version:supplement:"
- "configurationType"
- "configurationWithHandler:"
- "configureConnection:"
- "conformsToProtocol:"
- "connectedDisplays"
- "connectionWithEndpoint:"
- "connectionWithEndpoint:clientContextBuilder:"
- "containerURL"
- "containsObject:"
- "containsValueForKey:"
- "contaminateRequestOptions:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "contentsURL"
- "controlIdentity"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:"
- "createCGImageFromCPBitmapData:error:"
- "createCGImageFromData:error:"
- "createCGImageFromURL:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createLockScreenPhotosPosterWithImageAtURL:selectLockScreenPoster:completion:"
- "createLockScreenPhotosPosterWithImageAtURL:selectedLockScreenPoster:"
- "createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:completion:"
- "createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:"
- "currentContext"
- "currentHandler"
- "currentLocale"
- "d"
- "d16@0:8"
- "data"
- "dataContainerURL"
- "dataRepresentationForImage:error:"
- "dataStoreArchiveConfigurationFromArgs:"
- "dataStoreContainerDirectoryPath"
- "dataUsingEncoding:"
- "dataWithContentsOfURL:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeCGRectForKey:"
- "decodeCollectionOfClass:containingClass:forKey:"
- "decodeDictionaryOfClass:forKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeDoubleForKey:"
- "decodeFromPersistableRepresentation:error:"
- "decodeFromPersistableRepresentation:expectedContainerIdentifier:error:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeStringForKey:"
- "decodeUInt64ForKey:"
- "decodeXPCObjectOfType:forKey:"
- "defaultConfiguredPropertiesForRole:"
- "defaultManager"
- "delegate"
- "deleteArchivedDataStoreNamed:completion:"
- "deleteDataStoreWithCompletion:"
- "deleteHostConfigurationForRole:completion:"
- "deletePosterConfigurationsMatchingUUID:completion:"
- "deletePosterDescriptorsForExtension:completion:"
- "deleteSnapshotsWithCompletion:"
- "deleteTransientDataWithCompletion:"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "descriptiveTextLocalizationKey"
- "descriptorIdentifier"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "displayNameLocalizationKey"
- "doesNotRecognizeSelector:"
- "doubleValue"
- "empty"
- "encodeBool:forKey:"
- "encodeCGRect:forKey:"
- "encodeCollection:forKey:"
- "encodeDictionary:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeRepresentation:value:withCoder:"
- "encodeUInt64:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "endpointForMachName:service:instance:"
- "ensurePosterExtensionAvailable:completion:"
- "entryWithExtensionID:descriptorID:"
- "entryWithExtensionID:descriptorID:posterUUID:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "expectedContainerIdentifier"
- "exportArchivedDataStoreNamed:completion:"
- "exportCurrentDataStoreToURL:options:sandboxToken:error:"
- "exportPosterConfigurationMatchingUUID:completion:"
- "extendContentsReadAccessToAuditToken:error:"
- "extendValidityForReason:"
- "extensionIdentifier"
- "failWithError:"
- "failedUpdateResultForUpdate:error:"
- "featuredConfidenceLevel"
- "fetchActiveConfiguration:"
- "fetchActivePosterConfiguration:"
- "fetchActivePosterForRole:completion:"
- "fetchActivePosterForRole:error:"
- "fetchArchivedDataStoreNamesWithCompletion:"
- "fetchAssociatedHomeScreenPosterConfigurationUUID:completion:"
- "fetchAvailableExtensionIdentifiers:"
- "fetchChargerIdentifierRelationshipsWithCompletion:"
- "fetchContentCutoutBoundsForActivePosterWithOrientation:completionHandler:"
- "fetchContentCutoutBoundsForPosterConfiguration:orientation:completion:"
- "fetchContentCutoutBoundsForPosterConfiguration:orientation:completionHandler:"
- "fetchContentObstructionBoundsForActivePosterWithOrientation:completionHandler:"
- "fetchContentObstructionBoundsForPosterConfiguration:orientation:completion:"
- "fetchContentObstructionBoundsForPosterConfiguration:orientation:completionHandler:"
- "fetchDownloadablePosterAppsWithCompletion:"
- "fetchEligibleConfigurationsWithCompletion:"
- "fetchExtendedContentCutoutBoundsForOrientation:completion:"
- "fetchExtendedContentCutoutBoundsForOrientation:completionHandler:"
- "fetchExtensionAuditTokenWithError:"
- "fetchExtensionIdentifiersWithCompletion:"
- "fetchFocusUUIDForConfiguration:completion:"
- "fetchGallery:"
- "fetchHomeScreenWallpaperForOrientation:completion:"
- "fetchHomeScreenWallpaperWithCompletion:"
- "fetchLimitedOcclusionBoundsForPosterConfiguration:orientation:completion:"
- "fetchLimitedOcclusionBoundsForPosterConfiguration:orientation:completionHandler:"
- "fetchLockScreenHomeScreenColorConfigurations:"
- "fetchLockScreenWallpaperForOrientation:completion:"
- "fetchLockScreenWallpaperForRequest:checkLockScreenPoster:completion:"
- "fetchLockScreenWallpaperForType:variant:options:orientation:completion:"
- "fetchLockScreenWallpaperWithCompletion:"
- "fetchMaximalContentCutoutBoundsForOrientation:completion:"
- "fetchMaximalContentCutoutBoundsForOrientation:completionHandler:"
- "fetchObscurableBoundsForPosterConfiguration:orientation:completion:"
- "fetchObscurableBoundsForPosterConfiguration:orientation:completionHandler:"
- "fetchPosterConfigurations:"
- "fetchPosterConfigurationsForExtension:completion:"
- "fetchPosterConfigurationsForRole:completion:"
- "fetchPosterDescriptorsForExtension:completion:"
- "fetchPosterFocusSnapshotsWithRequest:completion:"
- "fetchPosterSnapshotsWithRequest:completion:"
- "fetchRuntimeAssertionState:"
- "fetchSelectedConfiguration:"
- "fetchSelectedPosterForRole:completion:"
- "fetchStaticPosterDescriptorsForExtension:completion:"
- "fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:"
- "fileSystemRepresentation"
- "fileURLWithPath:isDirectory:"
- "finishWithResult:"
- "finishWithResult:error:"
- "firstObject"
- "flatMap:"
- "focus"
- "focusModeUUID"
- "formatForDataAtURL:"
- "future"
- "futureWithResult:"
- "galleryOptions"
- "gatherDataFreshnessState:"
- "getResourceValue:forKey:error:"
- "gradientColorAppearance"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handler"
- "hasEntitlement:"
- "hasPrefix:"
- "hash"
- "height"
- "homeProviderIdentifier"
- "homeProviderUpdateSessionInfo"
- "homeScreenConfigurationPath"
- "homeScreenPosterConfiguration"
- "hostApplicationIdentifier"
- "hostConfigurationWithConfigurationEntries:"
- "hostContext"
- "hostContextWithCompletion:"
- "identifierURL"
- "identity"
- "ignoreExtension:completion:"
- "imageOrientation"
- "imageScaleRelativeToScreen"
- "importPosterConfigurationFromArchiveData:completion:"
- "importPosterConfigurationFromArchivedData:completion:"
- "indexOfObject:"
- "ingestSnapshotCollection:forPosterConfiguration:completion:"
- "ingestSnapshotCollection:forPosterConfigurationUUID:completion:"
- "init"
- "initFromSourceData:scale:error:"
- "initFromURL:scale:error:"
- "initWithAmbientWidgets:"
- "initWithArray:copyItems:"
- "initWithAuditToken:primaryDisplay:connectedDisplays:hostApplicationIdentifier:userInterfaceStyle:"
- "initWithBSXPCCoder:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCGImage:scale:error:"
- "initWithCachingReason:"
- "initWithCodableImage:"
- "initWithCodableImage:imageOrientation:switcherConfigurationPath:homeScreenConfigurationPath:variant:configurationType:"
- "initWithCoder:"
- "initWithCollection:otherCollection:"
- "initWithColor:"
- "initWithComplications:"
- "initWithConfiguration:"
- "initWithConfiguration:variantType:options:"
- "initWithConfiguration:variantType:options:orientation:"
- "initWithConfigurationAttributes:"
- "initWithConfigurationEntries:"
- "initWithConfigurationType:variantType:options:"
- "initWithConfigurationType:variantType:options:orientation:"
- "initWithConfigurationType:variantType:options:orientation:requestOptions:"
- "initWithContentsOfURL:options:error:"
- "initWithData:encoding:"
- "initWithDescriptor:variantType:options:"
- "initWithDictionary:copyItems:"
- "initWithDomain:code:userInfo:"
- "initWithExplanation:"
- "initWithExplanation:target:attributes:"
- "initWithExtensionBundleIdentifier:containerBundleIdentifier:deviceIdentifier:"
- "initWithExtensionBundleIdentifier:kind:containerBundleIdentifier:widgetFamily:intent:source:"
- "initWithExtensionID:descriptorID:"
- "initWithExtensionID:descriptorID:posterUUID:"
- "initWithExtensionIdentity:kind:family:intent:activityIdentifier:"
- "initWithExtensionIdentity:kind:intent:"
- "initWithFileManager:"
- "initWithFileManager:unarchivingContainerURL:"
- "initWithFocusModeUUID:configurationType:variant:options:imageScaleRelativeToScreen:maxCount:"
- "initWithFocusModeUUID:configurationType:variant:options:imageScaleRelativeToScreen:orientation:maxCount:"
- "initWithFocusModeUUID:configurationType:variant:options:maxCount:"
- "initWithFocusModeUUID:maxCount:"
- "initWithFocusPosterRequest:"
- "initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:"
- "initWithIOSurface:"
- "initWithIOSurface:imageOrientation:switcherConfigurationPath:homeScreenConfigurationPath:variant:configurationType:"
- "initWithIOSurface:scale:error:"
- "initWithIdentifier:"
- "initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:containerBundleIdentifier:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:localizedDisplayName:localizedSubtitle:titleFontName:titleColor:subtitleComplication:layoutType:modeSemanticType:modeUUID:complications:landscapeComplications:blankTemplate:shouldShowAsShuffleStack:source:"
- "initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:localizedDisplayName:localizedSubtitle:titleFontName:titleColor:subtitleComplication:layoutType:modeSemanticType:modeUUID:complications:landscapeComplications:blankTemplate:shouldShowAsShuffleStack:source:"
- "initWithIdentifier:extensionBundleIdentifier:containerBundleIdentifier:galleryOptions:"
- "initWithLockScreenPosterConfiguration:homeScreenPosterConfiguration:"
- "initWithModularComplications:modularLandscapeComplications:inlineComplication:allowsSystemSuggestedComplications:allowsSystemSuggestedComplicationsInLandscape:featuredConfidenceLevel:displayNameLocalizationKey:spokenNameLocalizationKey:descriptiveTextLocalizationKey:hero:shouldShowAsShuffleStack:photoSubtype:focus:onlyEligibleForMadeForFocusSection:isOffloaded:"
- "initWithPFPosterArchiver:"
- "initWithPath:"
- "initWithPath:extensionIdentifier:"
- "initWithPath:requestOptions:"
- "initWithPath:snapshotType:"
- "initWithPoster:type:variant:accentColor:size:"
- "initWithPosterBoardRepresentation:"
- "initWithPosterRequest:"
- "initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:"
- "initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:"
- "initWithPrimaryLayersSnapshot:floatingLayerSnapshot:snapshotScale:interfaceStyle:accessibilityContrast:interfaceOrientation:displayIdentity:salientContentRectangle:"
- "initWithProactiveRepresentation:"
- "initWithPropertyList:"
- "initWithPropertyListData:"
- "initWithRole:"
- "initWithRole:activePath:suggestionDescriptors:"
- "initWithRole:activePoster:suggestions:"
- "initWithRole:needsSandboxExtensions:"
- "initWithRole:posterCollection:"
- "initWithRoles:"
- "initWithRoles:needsSandboxExtensions:"
- "initWithSections:locale:"
- "initWithSections:locale:source:"
- "initWithSet:"
- "initWithSnapshots:"
- "initWithState:"
- "initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:associatedAppBundleIdentifier:symbolImageName:symbolColorName:unityDescription:items:"
- "initWithType:localizedTitle:localizedSubtitle:localizedDescriptiveText:symbolImageName:symbolColorName:unityDescription:items:"
- "initWithTypeRecord:destinationOptions:addImageOptions:"
- "initWithURL:extensionIdentifier:configurationUUID:role:version:supplementalVersion:"
- "initWithURL:location:legibilityBlur:smartCrop:usePreview:"
- "initWithUTF8String:"
- "initWithUUIDString:"
- "initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:controlType:intent:"
- "initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:family:intent:"
- "initWithUniqueIdentifier:kind:extensionBundleIdentifier:containerBundleIdentifier:intent:"
- "initWithUpdate:"
- "initWithUpdatedAppearanceType:"
- "initWithUpdatedAppearanceType:gradientColorAppearance:"
- "initWithUpdatedAppearanceType:solidColorAppearance:"
- "initWithUpdatedAppearanceType:updateHomePoster:homeProviderIdentifier:"
- "initWithUpdatedAppearanceType:updateSwitcherPoster:"
- "initWithVariation:saturation:luminance:alpha:"
- "initialValue"
- "initializePosterCollectionForRoles:"
- "initializeRoles:suggestions:"
- "initializeWithKnownIdentities:knownRoles:knownCollection:"
- "initializeWithPaths:recentlyChanged:"
- "inlineComplication"
- "installAllPosterAppsWithCompletion:"
- "instanceURL"
- "integerValue"
- "intentReference"
- "interfaceWithIdentifier:"
- "invalidate"
- "invalidateDataStoreWithCompletion:"
- "invertedSet"
- "isBlankTemplate"
- "isEmpty"
- "isEqual"
- "isEqual:"
- "isEqualRepresentation:"
- "isEqualToAttributes:"
- "isEqualToDictionary:"
- "isEqualToPersistable:"
- "isEqualToPosterIconConfiguration:"
- "isEqualToString:"
- "isExtensionIdentifierEqual:"
- "isHero"
- "isHomeScreenDim"
- "isIdentifierURLEqual:"
- "isInvalid"
- "isKindOfClass:"
- "isMainDisplay"
- "isMemberOfClass:"
- "isNewerVersionOfIdentity:"
- "isOffloaded"
- "isOnlyEligibleForMadeForFocusSection"
- "isPersistable"
- "isPosterUUIDEqual:"
- "isProxy"
- "isRoleEqual:"
- "isServerPosterPath"
- "isSharedIPad"
- "isSupplementalVersionEqual:"
- "isValid"
- "isVersionEqual:"
- "issuePosterCollectionUpdate:"
- "issueUpdateForRoles:suggestions:"
- "issueUpdateForSuggestions:"
- "issueUpdatedState:"
- "itemOptionsWithDictionaryRepresentation:error:"
- "items"
- "keyEnumerator"
- "landscapeComplications"
- "lastActiveHomePoster"
- "lastActiveLockPoster"
- "lastIndex"
- "lastObject"
- "lastPathComponent"
- "layoutType"
- "legibilityBlur"
- "length"
- "lhsCollection"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "loadConfiguredPropertiesForPath:error:"
- "loadFromURL:error:"
- "loadUserInfoWithError:"
- "locale"
- "localeIdentifier"
- "localizedDescription"
- "localizedDescriptiveText"
- "localizedDisplayName"
- "localizedSubtitle"
- "localizedTitle"
- "location"
- "locationStateObserver"
- "locations"
- "lockScreenPosterConfiguration"
- "luminance"
- "mainBundle"
- "mainIdentity"
- "makeWithOther:"
- "matchesPersonality:"
- "maxCount"
- "modeSemanticType"
- "modeUUID"
- "modularComplications"
- "modularLandscapeComplications"
- "mutableConfiguration"
- "mutableConfigurationWithProvider:descriptorIdentifier:role:"
- "mutableConfigurationWithRole:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "mutableDescriptorWithIdentifier:"
- "mutableDescriptorWithIdentifier:role:"
- "mutableDescriptors"
- "name"
- "new"
- "newBundleIdentifierForOldBundleIdentifier:"
- "notePosterConfigurationUnderlyingModelDidChange:"
- "noteSnapshotUpdateForPath:snapshotType:"
- "notifyActiveChargerIdentifierDidUpdate:completion:"
- "notifyAvailableFocusModesDidChange:completion:"
- "notifyFocusModeDidChange:completion:"
- "notifyInitialUpdatesComplete"
- "notifyPosterBoardOfApplicationUpdatesWithCompletion:"
- "notifyRoleActivePosterUpdates:"
- "notifyRolePosterCollectionUpdates:"
- "notifySnapshotUpdates:"
- "notifyWallpaperUpdates:"
- "null"
- "nullPayload"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "options"
- "optionsBySettingIsOffloaded:"
- "orderedSetWithArray:"
- "orientation"
- "overnightUpdate:completion:"
- "overnightUpdateWithCompletion:"
- "pathExtension"
- "pathWithContainerURL:identity:"
- "pathWithProviderURL:identity:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistableRepresentationWithError:"
- "pf_descriptorIdentifierURLForType:identifierURL:"
- "pf_posterPathIdentifierURLProviderURL:type:posterUUID:"
- "pf_posterPathInstanceURLForVersionsURL:version:"
- "pf_posterPathSupplementContainerURLForInstanceURL:"
- "pf_posterPathTypeURLForProviderURL:type:"
- "pf_posterPathVersionsURLForIdentifierURL:"
- "pf_roleIdentifierURLForType:identifierURL:"
- "pf_sanitizeWithAllowedKeyClasses:allowedValueClasses:"
- "pf_secureDecodedFromData:classReplacementMap:"
- "pf_temporaryDirectoryURLWithBasenamePrefix:"
- "photoSubtype"
- "pid"
- "pointScale"
- "posterBoardRepresentation"
- "posterCollection"
- "posterConfiguration"
- "posterUpdateAmbientConfigurationForCreation:deletion:editingBehavior:supportedDataLayout:"
- "posterUpdateAmbientWidgets:"
- "posterUpdateAssociateWithChargerIdentifier:"
- "posterUpdateComplications:"
- "posterUpdateDisassociateFromChargerIdentifier:"
- "posterUpdateHomeScreenAppearance:"
- "posterUpdateHomeScreenAppearanceDimWithValue:"
- "posterUpdateHomeScreenColor:"
- "posterUpdateHomeScreenGradient:"
- "posterUpdateHomeScreenIconTintSource:"
- "posterUpdateHomeScreenIconUserInterfaceStyle:"
- "posterUpdateHomeScreenIconUserInterfaceStyleVariant:"
- "posterUpdateHomeScreenPosterLegibilityBlurWithValue:"
- "posterUpdateHomeScreenPosterProvider:sessionInfo:"
- "posterUpdateHomeScreenPosterWithImageAtURL:"
- "posterUpdateHomeScreenSuggestedTintColor:"
- "posterUpdateHomeScreenTintForColor:"
- "posterUpdateHomeScreenTintWithVariation:saturation:luminance:"
- "posterUpdateHomeScreenTintWithVariation:saturation:luminance:alpha:"
- "posterUpdateInlineComplication:"
- "posterUpdateLegibilityBlurWithValue:"
- "posterUpdateLockScreenPosterWithImageAtURL:"
- "posterUpdateMirroredHomeScreenLegibilityBlurWithValue:"
- "posterUpdatePosterWithSessionInfo:"
- "posterUpdateShouldUseLargeHomeScreenIcons:"
- "posterUpdateSidebarComplications:"
- "posterUpdateUserInfo:"
- "posterUpdateUserSelectedHomeScreenIconStyleVariantsForTypes:"
- "posterUpdatesForDecoratedSessionInfo:"
- "posterUpdatesForWFWallpaperConfiguration:"
- "posterUpdatesForWFWallpaperConfiguration:sessionInfo:"
- "posters"
- "postersAtProviderURL:type:fileManager:error:"
- "postersAtURL:error:"
- "postersCollectionRoleObserver"
- "prewarm:completion:"
- "prewarmWithCompletion:"
- "primaryDisplayInfo"
- "proactiveRepresentation"
- "processDisallowsAppleArchive"
- "processInfo"
- "processName"
- "propertyList:isValidForFormat:"
- "propertyListData"
- "propertyListWithData:options:format:error:"
- "protocolForProtocol:"
- "provider"
- "providerBundleIdentifier"
- "providerURL"
- "prs_entitlementFailureErrorWithFile:line:"
- "prs_errorWithCode:"
- "prs_errorWithCode:underlyingError:userInfo:"
- "prs_errorWithCode:userInfo:"
- "prs_isPosterSnapshot"
- "pushPosterGalleryUpdate:completion:"
- "pushToProactiveWithCompletion:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "rangeOfCharacterFromSet:"
- "rangeOfString:"
- "rawValue"
- "refersToIdenticalImageFrom:"
- "refreshPosterConfiguration:completion:"
- "refreshPosterConfiguration:sessionInfo:completion:"
- "refreshPosterConfigurationMatchingUUID:sessionInfo:completion:"
- "refreshPosterDescriptorsForExtension:completion:"
- "refreshPosterDescriptorsForExtension:sessionInfo:completion:"
- "refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:"
- "refreshSnapshotForPosterConfiguration:completion:"
- "refreshSnapshotForPosterConfigurationMatchUUID:completion:"
- "refreshSnapshotForPosterConfigurationMatchingUUID:completion:"
- "refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:"
- "release"
- "remoteAssertionTarget"
- "remoteProcess"
- "remoteTarget"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "removeAllFocusConfigurationsMatchingFocusUUID:completion:"
- "removeAllIndexes"
- "removeAllObjects"
- "removeCaches"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "replaceCharactersInRange:withString:"
- "requestOptions"
- "requestedValue"
- "resetLockScreenWallpapersToImageAtURL:completion:"
- "resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:"
- "resetRole:completion:"
- "resolveAddImageOptionsForImage:"
- "resolveDestinationOptionsForImage:"
- "respondsToSelector:"
- "restoreArchivedDataStoreNamed:backupExistingDataStore:completion:"
- "retain"
- "retainCount"
- "retrieveGallery:"
- "rhsCollection"
- "runMigration:completion:"
- "runMigration:migrationDescriptor:completion:"
- "sandboxExtendedURLForURL:options:auditToken:error:"
- "sanitizeRequestOptions:"
- "saturation"
- "screens"
- "sections"
- "selectedHome"
- "selectedLock"
- "self"
- "server:associateConfigurationMatchingUUID:focusModeActivityUUID:completion:"
- "server:augmentDownloadablePosterMetadataForApp:sandboxExtendedBundleURL:bundleIdentifierOverride:completion:"
- "server:clearMigrationFlags:"
- "server:commitSuggestionsForConfigurationMatchingUUID:selectSuggestionDescriptorUUID:completion:"
- "server:createPosterConfigurationForProviderIdentifier:posterDescriptorIdentifier:role:completion:"
- "server:deleteArchivedDataStoreNamed:completion:"
- "server:deleteDataStoreWithCompletion:"
- "server:deleteHostConfigurationForRole:completion:"
- "server:deletePosterConfigurationsMatchingUUID:completion:"
- "server:deletePosterDescriptorsForExtension:completion:"
- "server:deleteSnapshotsWithCompletion:"
- "server:deleteTransientDataWithCompletion:"
- "server:ensurePosterExtensionAvailable:completion:"
- "server:exportArchivedDataStoreNamed:completion:"
- "server:exportCurrentDataStoreToURL:options:sandboxToken:error:"
- "server:exportPosterConfigurationMatchingUUID:completion:"
- "server:fetchActivePosterForRole:completion:"
- "server:fetchActivePosterForRole:error:"
- "server:fetchArchivedDataStoreNamesWithCompletion:"
- "server:fetchAssociatedHomeScreenPosterConfigurationUUID:completion:"
- "server:fetchAvailableExtensionIdentifiers:"
- "server:fetchChargerIdentifierRelationshipsWithCompletion:"
- "server:fetchContentCutoutBoundsForPosterConfiguration:orientation:completion:"
- "server:fetchContentObstructionBoundsForPosterConfiguration:orientation:completion:"
- "server:fetchDownloadablePosterAppsWithCompletion:"
- "server:fetchExtendedContentCutoutBoundsForOrientation:completion:"
- "server:fetchExtensionIdentifiersWithCompletion:"
- "server:fetchFocusUUIDForConfiguration:completion:"
- "server:fetchGallery:"
- "server:fetchLimitedOcclusionBoundsForPosterConfiguration:orientation:completion:"
- "server:fetchLockScreenHomeScreenColorConfigurations:"
- "server:fetchMaximalContentCutoutBoundsForOrientation:completion:"
- "server:fetchObscurableBoundsForPosterConfiguration:orientation:completion:"
- "server:fetchPosterConfigurationsForExtension:completion:"
- "server:fetchPosterConfigurationsForRole:completion:"
- "server:fetchPosterDescriptorsForExtension:completion:"
- "server:fetchPosterSnapshotsWithRequest:completion:"
- "server:fetchRuntimeAssertionState:"
- "server:fetchSelectedPosterForRole:completion:"
- "server:fetchStaticPosterDescriptorsForExtension:completion:"
- "server:fetchSuggestionDescriptorsForConfigurationMatchingUUID:completion:"
- "server:gatherDataFreshnessState:"
- "server:ignoreExtension:completion:"
- "server:importPosterConfigurationFromArchiveData:completion:"
- "server:ingestSnapshotCollection:forPosterConfigurationUUID:completion:"
- "server:installAllPosterAppsWithCompletion:"
- "server:invalidateDataStoreWithCompletion:"
- "server:notePosterConfigurationUnderlyingModelDidChange:"
- "server:notifyActiveChargerIdentifierDidUpdate:completion:"
- "server:notifyAvailableFocusModesDidChange:completion:"
- "server:notifyFocusModeDidChange:completion:"
- "server:notifyPosterBoardOfApplicationUpdatesWithCompletion:"
- "server:overnightUpdate:completion:"
- "server:prewarm:completion:"
- "server:pushPosterGalleryUpdate:completion:"
- "server:pushToProactiveWithCompletion:"
- "server:refreshPosterConfigurationMatchingUUID:sessionInfo:completion:"
- "server:refreshPosterDescriptorsForExtension:sessionInfo:completion:"
- "server:refreshSnapshotForGalleryItemsMatchingDescriptorIdentifier:extensionIdentifier:completion:"
- "server:refreshSnapshotForPosterConfigurationMatchUUID:completion:"
- "server:refreshSuggestionDescriptorsForConfigurationMatchingUUID:sessionInfo:completion:"
- "server:removeAllFocusConfigurationsMatchingFocusUUID:completion:"
- "server:resetRole:completion:"
- "server:restoreArchivedDataStoreNamed:backupExistingDataStore:completion:"
- "server:retrieveGallery:"
- "server:runMigration:migrationDescriptor:completion:"
- "server:setHostConfiguration:forRole:completion:"
- "server:stashCurrentDataStoreWithName:options:completion:"
- "server:triggerMessedUpDataProtectionWithCompletion:"
- "server:unignoreExtension:completion:"
- "server:uninstallAllPosterAppsWithCompletion:"
- "server:updatePosterConfiguration:updates:completion:"
- "server:updatePosterConfigurationMatchingUUID:updates:completion:"
- "server:updatePosterConfigurationsFromHostForRole:completion:"
- "server:updateToSelectedConfigurationMatchingUUID:role:from:completion:"
- "serverIdentity"
- "serverUUID"
- "service"
- "set"
- "setActivationHandler:"
- "setActivePosterRoleObserver:"
- "setAllowsSystemSuggestedComplications:"
- "setAllowsSystemSuggestedComplicationsInLandscape:"
- "setAssetURLs:"
- "setAssociatedAppBundleIdentifier:"
- "setBlankTemplate:"
- "setChanged:"
- "setClient:"
- "setClientMessagingExpectation:"
- "setComplications:"
- "setContainerBundleIdentifier:"
- "setContext:"
- "setControlType:"
- "setDelegate:"
- "setDescriptiveTextLocalizationKey:"
- "setDescriptorID:"
- "setDescriptorIdentifier:"
- "setDisplayNameLocalizationKey:"
- "setDomain:"
- "setEntries:"
- "setExtensionBundleIdentifier:"
- "setExtensionID:"
- "setFamily:"
- "setFeaturedConfidenceLevel:"
- "setFocus:"
- "setHandler:"
- "setHero:"
- "setHomeScreenDim:"
- "setHomeScreenIconSize:"
- "setHomeScreenIconStyle:"
- "setHomeScreenIconStyleVariant:"
- "setHomeScreenIconStyleVariantsForStyles:"
- "setHomeScreenIconTintSource:"
- "setHomeScreenTintColor:"
- "setHostConfiguration:forRole:completion:"
- "setHostContext:"
- "setIdentifier:"
- "setIdentity:"
- "setImage:"
- "setImageScaleRelativeToScreen:"
- "setInlineComplication:"
- "setIntent:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsOffloaded:"
- "setItems:"
- "setKind:"
- "setLandscapeComplications:"
- "setLastActiveHomePoster:"
- "setLastActiveLockPoster:"
- "setLayoutType:"
- "setLocale:"
- "setLocalizedDescriptiveText:"
- "setLocalizedDisplayName:"
- "setLocalizedSubtitle:"
- "setLocalizedTitle:"
- "setLocationStateObserver:"
- "setLocations:"
- "setModeSemanticType:"
- "setModeUUID:"
- "setModularComplications:"
- "setModularLandscapeComplications:"
- "setNeedsSandboxExtensions:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOnlyEligibleForMadeForFocusSection:"
- "setPath:"
- "setPhotoSubtype:"
- "setPosterUUID:"
- "setPostersCollectionRoleObserver:"
- "setQueue:"
- "setReapNonLatestEntries:"
- "setSections:"
- "setServer:"
- "setService:"
- "setServiceQuality:"
- "setShortcutsWallpaperConfiguration:"
- "setShouldShowAsShuffleStack:"
- "setSnapshotObserver:"
- "setSource:"
- "setSpokenNameLocalizationKey:"
- "setStripContentsOfConfigurations:"
- "setStripDescriptors:"
- "setStripScreenshots:"
- "setSubtitleComplication:"
- "setSymbolColorName:"
- "setSymbolImageName:"
- "setTargetQueue:"
- "setTitleColor:"
- "setTitleFontName:"
- "setType:"
- "setUniqueIdentifier:"
- "setUnityDescription:"
- "setUserInfo:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "sharedApplication"
- "sharedDirectoryURL"
- "sharedInstance"
- "sharedManager"
- "sharedResourcesDirectoryURL"
- "shortcutsWallpaperConfiguration"
- "shouldShowAsShuffleStack"
- "shouldUseSharedDataStore"
- "snapshotObserver"
- "snapshotType"
- "snapshotURLs"
- "solidColorAppearance"
- "sortedArrayUsingComparator:"
- "source"
- "specificType"
- "spokenNameLocalizationKey"
- "standardizedURL"
- "startAccessingSecurityScopedResource"
- "stashCurrentDataStoreWithName:options:completion:"
- "stateForRole:"
- "stopAccessingSecurityScopedResource"
- "storeConfiguredPropertiesForPath:configuredProperties:error:"
- "storeUserInfo:error:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringValue"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "substringWithRange:"
- "subtitleComplication"
- "successfulUpdateResultForUpdate:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "suggestedComplicationWithDictionaryRepresentation:error:"
- "superclass"
- "supplement"
- "supplementalVersion"
- "supportsBSXPCSecureCoding"
- "supportsPosterCustomization"
- "supportsSecureCoding"
- "surfaceCreatingIfNecessary:"
- "switcherConfigurationPath"
- "switcherProviderUpdateSessionInfo"
- "symbolColorName"
- "symbolImageName"
- "temporaryDescriptorPathWithIdentifier:role:"
- "temporaryPathForRole:"
- "temporaryServerPathForProvider:descriptorIdentifier:role:"
- "terminate"
- "titleColor"
- "titleFontName"
- "tokenForCurrentProcess"
- "triggerMessedUpDataProtectionWithCompletion:"
- "tristate"
- "typeIdentifier"
- "unarchiveConfigurationAtURL:error:"
- "unarchiveConfigurationAtURL:format:error:"
- "unarchiveConfigurationFromData:error:"
- "unarchiveConfigurationFromData:format:error:"
- "unarchivePathAtURL:format:error:"
- "unarchivePathFromData:format:error:"
- "unignoreExtension:completion:"
- "uninstallAllPosterAppsWithCompletion:"
- "unionSet:"
- "unityDescription"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateHomeScreenImageForLockScreenPoster:withImageAtURL:selectLockPoster:completion:"
- "updateLockScreenPhotosPoster:withImageAtURL:selectLockScreenPoster:completion:"
- "updateNecessitatesPosterUpdate"
- "updatePaths:"
- "updatePosterConfiguration:update:completion:"
- "updatePosterConfiguration:updates:completion:"
- "updatePosterConfigurationMatchingUUID:updates:completion:"
- "updatePosterConfigurationsFromHostForRole:completion:"
- "updatePosterMatchingUUID:withConfiguration:completion:"
- "updateSelectedForRoleIdentifier:newlySelectedConfiguration:completion:"
- "updateToSelectedConfiguration:completion:"
- "updateToSelectedConfiguration:role:completion:"
- "updateToSelectedConfigurationMatchingUUID:completion:"
- "updateToSelectedConfigurationMatchingUUID:role:completion:"
- "updateToSelectedPosterMatchingUUID:role:completion:"
- "updatedAppearanceType"
- "updatedValue"
- "updaterForPath:"
- "userInfo"
- "userInitiated"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray<__PRSPosterIconConfiguration__>\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8^{CGImage=}16"
- "v24@0:8d16"
- "v24@0:8r^@16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v32@0:8r^@16Q24"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8q16@24@32"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"NSURL\"16@\"PRSDataStoreArchiveConfiguration\"24@\"NSData\"32o^@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32o^@40"
- "v56@0:8q16q24Q32q40@?48"
- "validOptions"
- "validatePoster:"
- "valueForKey:"
- "variantType"
- "variation"
- "version"
- "wallpaperPublisherDidReceiveObserverConnection"
- "widgetFamily"
- "width"
- "wrappedIOSurface"
- "writePNGToURL:error:"
- "writeToURL:options:error:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
