## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4024.610.2.0.0
-  __TEXT.__text: 0x2c4080
-  __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x292f0
-  __TEXT.__const: 0x570
-  __TEXT.__cstring: 0x2a967
-  __TEXT.__oslogstring: 0xd422
-  __TEXT.__gcc_except_tab: 0x63c4
-  __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa998
-  __TEXT.__objc_classname: 0x4a5c
-  __TEXT.__objc_methname: 0x49124
-  __TEXT.__objc_methtype: 0x8b60
-  __TEXT.__objc_stubs: 0x26320
-  __DATA_CONST.__got: 0x1298
-  __DATA_CONST.__const: 0xa580
-  __DATA_CONST.__objc_classlist: 0x1118
+4025.110.87.2.0
+  __TEXT.__text: 0x2e5128
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_methlist: 0x2a380
+  __TEXT.__const: 0x590
+  __TEXT.__cstring: 0x2b12b
+  __TEXT.__oslogstring: 0xd831
+  __TEXT.__gcc_except_tab: 0x6208
+  __TEXT.__dlopen_cstrs: 0x514
+  __TEXT.__ustring: 0x7a2
+  __TEXT.__unwind_info: 0xaae8
+  __TEXT.__objc_classname: 0x4c34
+  __TEXT.__objc_methname: 0x4b4ec
+  __TEXT.__objc_methtype: 0x8e62
+  __TEXT.__objc_stubs: 0x27320
+  __DATA_CONST.__got: 0x1420
+  __DATA_CONST.__const: 0xac20
+  __DATA_CONST.__objc_classlist: 0x1160
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe370
+  __DATA_CONST.__objc_selrefs: 0xe9f8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xf58
-  __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__auth_got: 0xb20
-  __AUTH_CONST.__const: 0x3220
-  __AUTH_CONST.__cfstring: 0x20640
-  __AUTH_CONST.__objc_const: 0x43080
-  __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_arrayobj: 0x150
+  __DATA_CONST.__objc_superrefs: 0xf98
+  __DATA_CONST.__objc_arraydata: 0x260
+  __AUTH_CONST.__auth_got: 0xb78
+  __AUTH_CONST.__const: 0x3020
+  __AUTH_CONST.__cfstring: 0x227a0
+  __AUTH_CONST.__objc_const: 0x44808
+  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x78a0
-  __AUTH.__data: 0x170
-  __DATA.__objc_ivar: 0x3034
-  __DATA.__data: 0x1b50
-  __DATA.__bss: 0x8c0
+  __AUTH.__objc_data: 0x7f30
+  __AUTH.__data: 0x10
+  __DATA.__objc_ivar: 0x3148
+  __DATA.__data: 0x1c20
+  __DATA.__bss: 0x8a0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x6e0
+  __DATA_DIRTY.__objc_data: 0x2e90
+  __DATA_DIRTY.__data: 0x48
+  __DATA_DIRTY.__bss: 0x480
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C551EFA6-D535-34AF-8813-22DF0AE28D75
-  Functions: 19478
-  Symbols:   53740
-  CStrings:  23145
+  UUID: 1DA234DB-EE8F-319D-96F4-D642689799AD
+  Functions: 19786
+  Symbols:   54318
+  CStrings:  23887
 
Symbols:
+ +[MRAVEndpoint addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
+ +[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]
+ +[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]
+ +[MRAVEndpoint moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
+ +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]
+ +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.1
+ +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.2
+ +[MRAVLocalEndpoint sharedSystemAudioLocalEndpoint]
+ +[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:localDeviceInfo:]
+ +[MRArtwork generateArtworkDataWithSize:]
+ +[MRContentItem animatedArtworkItemIdentifierFromSourceIdentifier:]
+ +[MRLocalVolumeHUDPresentationRequest localVolumeHUDPresentationRequest]
+ +[MRUIControllerProvider volumeHUDController]
+ +[MRVolumeHUDPresentationRequest supportsSecureCoding]
+ +[_MRContentItemProtobuf animatedArtworkPreviewFramesType]
+ +[_MRContentItemProtobuf animatedArtworksType]
+ +[_MRContentItemProtobuf availableAnimatedArtworkFormatsType]
+ +[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkAssetURLFormatsType]
+ +[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkPreviewFrameFormatsType]
+ +[_MRPlaybackSessionMigrateRequestEventProtobuf eventsType]
+ -[MRAVConcreteOutputDevice discoveredDeviceIsPlaying]
+ -[MRAVConcreteOutputDevice isCarPlayVideoActive]
+ -[MRAVConcreteOutputDevice isCarPlayVideoAllowed]
+ -[MRAVConcreteOutputDevice setCarPlayVideoActive:completion:]
+ -[MRAVConcreteOutputDevice wasDiscoveredInCache]
+ -[MRAVConcreteRoutingDiscoverySession _loadDefaults]
+ -[MRAVConcreteRoutingDiscoverySession allowList]
+ -[MRAVConcreteRoutingDiscoverySession denyList]
+ -[MRAVConcreteRoutingDiscoverySession observeValueForKeyPath:ofObject:change:context:]
+ -[MRAVConcreteRoutingDiscoverySession userDefaults]
+ -[MRAVDistantOutputDevice discoveredDeviceIsPlaying]
+ -[MRAVDistantOutputDevice distantOutputDeviceRepresentation]
+ -[MRAVDistantOutputDevice wasDiscoveredInCache]
+ -[MRAVEndpoint canStartNativePlayback]
+ -[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]
+ -[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]
+ -[MRAVEndpoint discoveredIsPlaying]
+ -[MRAVEndpoint discoveredOutputDevices]
+ -[MRAVEndpoint isCarPlayVideoActive]
+ -[MRAVEndpoint isCarPlayVideoAllowed]
+ -[MRAVEndpoint isGroupLeaderGroupable]
+ -[MRAVEndpoint isMyDiscoverableUndiscoverableGroupLeader]
+ -[MRAVEndpoint isMyGroupLeader]
+ -[MRAVEndpoint requestMicrophoneConnection:completion:]
+ -[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]
+ -[MRAVEndpoint setCarPlayVideoActive:completion:]
+ -[MRAVLightweightReconnaissanceSession _discoverySessionForFeature:]
+ -[MRAVLightweightReconnaissanceSession cachedDiscoveryEnabled]
+ -[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]
+ -[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:].cold.1
+ -[MRAVLightweightReconnaissanceSession setCachedDiscoveryEnabled:]
+ -[MRAVLocalEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]
+ -[MRAVLocalEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]
+ -[MRAVLocalEndpoint setCarPlayVideoActive:completion:]
+ -[MRAVOutputDevice clusterMemberID]
+ -[MRAVOutputDevice discoveredDeviceIsPlaying]
+ -[MRAVOutputDevice distantOutputDeviceRepresentation]
+ -[MRAVOutputDevice isCarPlayVideoActive]
+ -[MRAVOutputDevice isCarPlayVideoAllowed]
+ -[MRAVOutputDevice isNonRemoteControllableAirPlayDevice]
+ -[MRAVOutputDevice isStudioDisplay]
+ -[MRAVOutputDevice setCarPlayVideoActive:completion:]
+ -[MRAVOutputDevice wasDiscoveredInCache]
+ -[MRAVReconnaissanceSession cachedDiscoveryEnabled]
+ -[MRAVReconnaissanceSession initWithOutputDeviceGroupUID:features:details:]
+ -[MRAVReconnaissanceSession initWithOutputDeviceUIDs:features:details:]
+ -[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupUID:features:details:]
+ -[MRAVReconnaissanceSession setCachedDiscoveryEnabled:]
+ -[MRAVReconnaissanceSession setTargetAudioSessionID:]
+ -[MRAVReconnaissanceSession targetAudioSessionID]
+ -[MRAVRoutingDiscoverySession _shouldLogChanges]
+ -[MRAVRoutingDiscoverySession cachedDiscoveryEnabled]
+ -[MRAVRoutingDiscoverySession setCachedDiscoveryEnabled:]
+ -[MRAVRoutingDiscoverySessionConfiguration cachedDiscoveryEnabled]
+ -[MRAVRoutingDiscoverySessionConfiguration setCachedDiscoveryEnabled:]
+ -[MRAVRoutingDiscoverySessionWrapper setCachedDiscoveryEnabled:]
+ -[MRActiveRoutesObserver _handleActiveSystemEndpointDidAddOutputDevice:]
+ -[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]
+ -[MRActiveRoutesObserver activeEndpointSnapshot]
+ -[MRActiveRoutesObserver deviceRemovedSnapshot]
+ -[MRActiveRoutesObserver deviceRemovedWaitIntervalTimer]
+ -[MRActiveRoutesObserver deviceRemovedWaitInterval]
+ -[MRActiveRoutesObserver setActiveEndpointSnapshot:]
+ -[MRActiveRoutesObserver setDeviceRemovedSnapshot:]
+ -[MRActiveRoutesObserver setDeviceRemovedWaitInterval:]
+ -[MRActiveRoutesObserver setDeviceRemovedWaitIntervalTimer:]
+ -[MRActiveRoutesObserverOutputDeviceRemovedSnapshot .cxx_destruct]
+ -[MRActiveRoutesObserverOutputDeviceRemovedSnapshot date]
+ -[MRActiveRoutesObserverOutputDeviceRemovedSnapshot endpoint]
+ -[MRActiveRoutesObserverOutputDeviceRemovedSnapshot setDate:]
+ -[MRActiveRoutesObserverOutputDeviceRemovedSnapshot setEndpoint:]
+ -[MRAnimatedArtwork .cxx_destruct]
+ -[MRAnimatedArtwork assetFileURL]
+ -[MRAnimatedArtwork initWithAssetFileURL:]
+ -[MRAnimatedArtwork initWithProtobuf:]
+ -[MRAnimatedArtwork initWithProtobuf:].cold.1
+ -[MRAnimatedArtwork protobufWithFormat:]
+ -[MRAnimatedArtwork protobufWithFormat:].cold.1
+ -[MRConcreteEndpoint _handleDeviceInfoDidChangeNotification:]
+ -[MRContentItem animatedArtworkPreviewFrames]
+ -[MRContentItem animatedArtworks]
+ -[MRContentItem availableAnimatedArtworkFormats]
+ -[MRContentItem setAnimatedArtworkPreviewFrames:]
+ -[MRContentItem setAnimatedArtworks:]
+ -[MRContentItem setAvailableAnimatedArtworkFormats:]
+ -[MRDeviceInfo hasParentGroupSupportsGroupCohesion]
+ -[MRDeviceInfo parentGroupSupportsGroupCohesion]
+ -[MRDeviceInfo setHasParentGroupSupportsGroupCohesion:]
+ -[MRDeviceInfo setParentGroupSupportsGroupCohesion:]
+ -[MRDeviceInfo(MRProtocolMessageLoggerAdditions) effectiveIdentifer]
+ -[MRDeviceInfo(MRProtocolMessageLoggerAdditions) effectiveName]
+ -[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]
+ -[MRDistantExternalDevice lastConnectionError]
+ -[MRDistantExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]
+ -[MRExpanseManager canAddTelevisionWithRouteIdentifierToSession:]
+ -[MRExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]
+ -[MRExternalDevice externalOutputContext]
+ -[MRExternalDevice lastConnectionError]
+ -[MRExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]
+ -[MRExternalOutputContextDataSource externalOutputContextRepresentation]
+ -[MRExternalOutputContextDataSource initWithUniqueIdentifier:outputDevices:volume:capabilities:muted:]
+ -[MRGroupComposition copyWithZone:]
+ -[MRGroupComposition localizedGroupCompositionForDeviceClass:modelID:]
+ -[MRGroupComposition localizedGroupComposition]
+ -[MRGroupSessionToken _groupSessionComponentsWithScheme:host:]
+ -[MRGroupSessionToken joinContinuitySingURLString]
+ -[MRGroupTopologyModificationRequest requiresAuthorizationHandling]
+ -[MRGroupTopologyModificationRequest setShouldWaitForUpdatedOutputDevices:]
+ -[MRGroupTopologyModificationRequest shouldWaitForUpdatedOutputDevices]
+ -[MRMediaRemoteService startSystemGroupSession]
+ -[MRMediaRemoteService stopSystemGroupSession]
+ -[MRMicrophoneConnectionRequestMessage .cxx_destruct]
+ -[MRMicrophoneConnectionRequestMessage details]
+ -[MRMicrophoneConnectionRequestMessage initWithDetails:rapportIdentifier:]
+ -[MRMicrophoneConnectionRequestMessage rapportIdentifier]
+ -[MRMicrophoneConnectionRequestMessage setDetails:]
+ -[MRMicrophoneConnectionRequestMessage setRapportIdentifier:]
+ -[MRMicrophoneConnectionRequestMessage type]
+ -[MRMicrophoneConnectionResponseMessage .cxx_destruct]
+ -[MRMicrophoneConnectionResponseMessage initWithPairingData:rapportIdentifier:]
+ -[MRMicrophoneConnectionResponseMessage initWithResult:rapportIdentifier:]
+ -[MRMicrophoneConnectionResponseMessage pairingData]
+ -[MRMicrophoneConnectionResponseMessage rapportIdentifier]
+ -[MRMicrophoneConnectionResponseMessage result]
+ -[MRMicrophoneConnectionResponseMessage setPairingData:]
+ -[MRMicrophoneConnectionResponseMessage setRapportIdentifier:]
+ -[MRMicrophoneConnectionResponseMessage type]
+ -[MRNowPlayingAnimatedArtwork .cxx_destruct]
+ -[MRNowPlayingAnimatedArtwork artworkAssetFileURLWithSize:completion:]
+ -[MRNowPlayingAnimatedArtwork initWithPreviewFrameDataRequestHandler:artworkAssetFileURLRequestHandler:]
+ -[MRNowPlayingAnimatedArtwork previewFrameDataWithSize:completion:]
+ -[MRNowPlayingAudioFormatContentInfo bestAvailableAudioFormat].cold.1
+ -[MRNowPlayingAudioFormatContentInfo bestAvailableAudioFormat].cold.2
+ -[MRNowPlayingControllerHelper controller:repeatModeDidChangeFrom:to:]
+ -[MRNowPlayingControllerHelper controller:shuffleModeDidChangeFrom:to:]
+ -[MRNowPlayingControllerHelper repeatModeDidChange]
+ -[MRNowPlayingControllerHelper setRepeatModeDidChange:]
+ -[MRNowPlayingControllerHelper setShuffleModeDidChange:]
+ -[MRNowPlayingControllerHelper shuffleModeDidChange]
+ -[MRNowPlayingOriginClient playbackSessionMigrateFinalizeCallback]
+ -[MRNowPlayingOriginClient setPlaybackSessionMigrateFinalizeCallback:]
+ -[MRNowPlayingPlayerClient nowPlayingAnimatedArtworkForFormat:]
+ -[MRNowPlayingPlayerClient nowPlayingAnimatedArtworkFormats]
+ -[MRNowPlayingPlayerClient nowPlayingArtworkID]
+ -[MRNowPlayingPlayerClient setNowPlayingAnimatedArtwork:forFormat:]
+ -[MRNowPlayingPlayerClient setNowPlayingArtworkID:]
+ -[MRNowPlayingPlayerClientCallbacks animatedArtworkCallbacks]
+ -[MRNowPlayingPlayerClientCallbacks playbackSessionMigrateFinalizeCallback]
+ -[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]
+ -[MRNowPlayingPlayerClientCallbacks setPlaybackSessionMigrateFinalizeCallback:]
+ -[MRNowPlayingPlayerResponse _mostRelevantItem]
+ -[MROrigin debugDescription]
+ -[MROutputContextController isVolumeMuted]
+ -[MROutputContextController modifyTopologyWithRequest:completion:]
+ -[MROutputContextDataSource externalOutputContextRepresentation]
+ -[MRPlaybackQueueRequest requestedAnimatedArtworkAssetURLFormats]
+ -[MRPlaybackQueueRequest requestedAnimatedArtworkPreviewFrameFormats]
+ -[MRPlaybackQueueRequest setRequestedAnimatedArtworkAssetURLFormats:]
+ -[MRPlaybackQueueRequest setRequestedAnimatedArtworkPreviewFrameFormats:]
+ -[MRPlaybackSessionMigrateEndMessage initWithRequest:error:setPlaybackSessionCommandStatus:playerPath:]
+ -[MRPlaybackSessionMigrateEndMessage setPlaybackSessionCommandStatus]
+ -[MRPlaybackSessionMigrateRequest _findEventWithID:inEvents:]
+ -[MRPlaybackSessionMigrateRequest _getLastEventIfActiveInEvents:]
+ -[MRPlaybackSessionMigrateRequest addEventInput:withKey:toEventID:]
+ -[MRPlaybackSessionMigrateRequest addEventOutput:withKey:toEventID:]
+ -[MRPlaybackSessionMigrateRequest backfillSignpostsForEvent:]
+ -[MRPlaybackSessionMigrateRequest endEventWithID:]
+ -[MRPlaybackSessionMigrateRequest endEventWithID:error:]
+ -[MRPlaybackSessionMigrateRequest endEventWithID:error:].cold.1
+ -[MRPlaybackSessionMigrateRequest endEventWithID:error:].cold.2
+ -[MRPlaybackSessionMigrateRequest eventsDictionary:]
+ -[MRPlaybackSessionMigrateRequest finalize].cold.1
+ -[MRPlaybackSessionMigrateRequest finalize].cold.2
+ -[MRPlaybackSessionMigrateRequest findEventWithID:]
+ -[MRPlaybackSessionMigrateRequest fullReport]
+ -[MRPlaybackSessionMigrateRequest printEvents:dateFormatter:timeElapsed:depth:]
+ -[MRPlaybackSessionMigrateRequest recipeType]
+ -[MRPlaybackSessionMigrateRequest reportDictionary]
+ -[MRPlaybackSessionMigrateRequest setPlaybackSessionCommandStatus]
+ -[MRPlaybackSessionMigrateRequest setRecipeType:]
+ -[MRPlaybackSessionMigrateRequest setSetPlaybackSessionCommandStatus:]
+ -[MRPlaybackSessionMigrateRequest startEvent:role:]
+ -[MRPlaybackSessionMigrateRequest startEvent:role:].cold.1
+ -[MRPlaybackSessionMigrateRequest symbolForEventName:isStart:]
+ -[MRPlaybackSessionMigrateRequest updateError:]
+ -[MRPlaybackSessionResponseMessage .cxx_destruct]
+ -[MRPlaybackSessionResponseMessage initWithPlaybackSession:request:]
+ -[MRPlaybackSessionResponseMessage request]
+ -[MRPlaybackSessionResponseMessage setRequest:]
+ -[MRPlayer debugDescription]
+ -[MRPlayerPath debugDescription]
+ -[MRRequestDetails initChildWithParent:reason:]
+ -[MRRequestDetails initWithRequestID:surface:initiator:reason:userInitiated:originatingBundleID:]
+ -[MRRequestDetails initWithSurface:initiator:reason:]
+ -[MRRequestDetails operationID]
+ -[MRRequestDetails setSurface:]
+ -[MRRequestDetails surface]
+ -[MRSharedSettings supportSystemGroupSession]
+ -[MRUIController presentVolumeHUDWithRequest:]
+ -[MRUIController setPreferredState:forBundleIdentifier:]
+ -[MRUserSettings carPlayBannersEnabled]
+ -[MRUserSettings disableAWDLRoutes]
+ -[MRUserSettings disableDUGLDuringAirPlayVideo]
+ -[MRUserSettings groupSessionAutoApproveParticipantsForAppleTV]
+ -[MRUserSettings groupSessionJoinRequestAssertionDuration]
+ -[MRUserSettings microphoneConnectionTimeout]
+ -[MRUserSettings supportBluehop]
+ -[MRUserSettings supportDiscoveryCaching]
+ -[MRUserSettings supportUGL]
+ -[MRVolumeHUDPresentationRequest encodeWithCoder:]
+ -[MRVolumeHUDPresentationRequest initWithCoder:]
+ -[NSArray(MRAVRoutingDiscoverySessionWrapperAdditions) nonCachedResults]
+ -[NSArray(MRAVRoutingDiscoverySessionWrapperAdditions) resultsFromConfiguration:]
+ -[NSError(MRAdditions) initWithMRError:description:underlyingErrors:]
+ -[_MRAVOutputDeviceDescriptorProtobuf deviceIsPlaying]
+ -[_MRAVOutputDeviceDescriptorProtobuf hasDeviceIsPlaying]
+ -[_MRAVOutputDeviceDescriptorProtobuf hasWasDiscoveredInCache]
+ -[_MRAVOutputDeviceDescriptorProtobuf setDeviceIsPlaying:]
+ -[_MRAVOutputDeviceDescriptorProtobuf setHasDeviceIsPlaying:]
+ -[_MRAVOutputDeviceDescriptorProtobuf setHasWasDiscoveredInCache:]
+ -[_MRAVOutputDeviceDescriptorProtobuf setWasDiscoveredInCache:]
+ -[_MRAVOutputDeviceDescriptorProtobuf wasDiscoveredInCache]
+ -[_MRAnimatedArtworkProtobuf .cxx_destruct]
+ -[_MRAnimatedArtworkProtobuf assetFileURLData]
+ -[_MRAnimatedArtworkProtobuf copyTo:]
+ -[_MRAnimatedArtworkProtobuf copyWithZone:]
+ -[_MRAnimatedArtworkProtobuf description]
+ -[_MRAnimatedArtworkProtobuf dictionaryRepresentation]
+ -[_MRAnimatedArtworkProtobuf hasAssetFileURLData]
+ -[_MRAnimatedArtworkProtobuf hasType]
+ -[_MRAnimatedArtworkProtobuf hash]
+ -[_MRAnimatedArtworkProtobuf isEqual:]
+ -[_MRAnimatedArtworkProtobuf mergeFrom:]
+ -[_MRAnimatedArtworkProtobuf readFrom:]
+ -[_MRAnimatedArtworkProtobuf setAssetFileURLData:]
+ -[_MRAnimatedArtworkProtobuf setType:]
+ -[_MRAnimatedArtworkProtobuf type]
+ -[_MRAnimatedArtworkProtobuf writeTo:]
+ -[_MRCommandInfoProtobuf addExtendedSupportedRate:]
+ -[_MRCommandInfoProtobuf clearExtendedSupportedRates]
+ -[_MRCommandInfoProtobuf extendedSupportedRateAtIndex:]
+ -[_MRCommandInfoProtobuf extendedSupportedRatesCount]
+ -[_MRCommandInfoProtobuf extendedSupportedRates]
+ -[_MRCommandInfoProtobuf hasTransitionStyle]
+ -[_MRCommandInfoProtobuf setExtendedSupportedRates:count:]
+ -[_MRCommandInfoProtobuf setHasTransitionStyle:]
+ -[_MRCommandInfoProtobuf setTransitionStyle:]
+ -[_MRCommandInfoProtobuf transitionStyle]
+ -[_MRCommandOptionsProtobuf enhanceDialogueActive]
+ -[_MRCommandOptionsProtobuf hasEnhanceDialogueActive]
+ -[_MRCommandOptionsProtobuf setEnhanceDialogueActive:]
+ -[_MRCommandOptionsProtobuf setHasEnhanceDialogueActive:]
+ -[_MRContentItemProtobuf addAnimatedArtworkPreviewFrames:]
+ -[_MRContentItemProtobuf addAnimatedArtworks:]
+ -[_MRContentItemProtobuf addAvailableAnimatedArtworkFormats:]
+ -[_MRContentItemProtobuf animatedArtworkPreviewFramesAtIndex:]
+ -[_MRContentItemProtobuf animatedArtworkPreviewFramesCount]
+ -[_MRContentItemProtobuf animatedArtworkPreviewFrames]
+ -[_MRContentItemProtobuf animatedArtworksAtIndex:]
+ -[_MRContentItemProtobuf animatedArtworksCount]
+ -[_MRContentItemProtobuf animatedArtworks]
+ -[_MRContentItemProtobuf availableAnimatedArtworkFormatsAtIndex:]
+ -[_MRContentItemProtobuf availableAnimatedArtworkFormatsCount]
+ -[_MRContentItemProtobuf availableAnimatedArtworkFormats]
+ -[_MRContentItemProtobuf clearAnimatedArtworkPreviewFrames]
+ -[_MRContentItemProtobuf clearAnimatedArtworks]
+ -[_MRContentItemProtobuf clearAvailableAnimatedArtworkFormats]
+ -[_MRContentItemProtobuf setAnimatedArtworkPreviewFrames:]
+ -[_MRContentItemProtobuf setAnimatedArtworks:]
+ -[_MRContentItemProtobuf setAvailableAnimatedArtworkFormats:]
+ -[_MRDeviceInfoMessageProtobuf hasParentGroupSupportsGroupCohesion]
+ -[_MRDeviceInfoMessageProtobuf parentGroupSupportsGroupCohesion]
+ -[_MRDeviceInfoMessageProtobuf setHasParentGroupSupportsGroupCohesion:]
+ -[_MRDeviceInfoMessageProtobuf setParentGroupSupportsGroupCohesion:]
+ -[_MRDiscoverySessionConfigurationProtobuf cachedDiscoveryEnabled]
+ -[_MRDiscoverySessionConfigurationProtobuf hasCachedDiscoveryEnabled]
+ -[_MRDiscoverySessionConfigurationProtobuf setCachedDiscoveryEnabled:]
+ -[_MRDiscoverySessionConfigurationProtobuf setHasCachedDiscoveryEnabled:]
+ -[_MRErrorProtobuf debugMessage]
+ -[_MRErrorProtobuf hasDebugMessage]
+ -[_MRErrorProtobuf hasUserInfo]
+ -[_MRErrorProtobuf setDebugMessage:]
+ -[_MRErrorProtobuf setUserInfo:]
+ -[_MRErrorProtobuf userInfo]
+ -[_MRGroupTopologyModificationRequestProtobuf hasShouldWaitForUpdatedOutputDevices]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasShouldWaitForUpdatedOutputDevices:]
+ -[_MRGroupTopologyModificationRequestProtobuf setShouldWaitForUpdatedOutputDevices:]
+ -[_MRGroupTopologyModificationRequestProtobuf shouldWaitForUpdatedOutputDevices]
+ -[_MRMediaRemoteMessageProtobuf hasMicrophoneConnectionRequestMessage]
+ -[_MRMediaRemoteMessageProtobuf hasMicrophoneConnectionResponseMessage]
+ -[_MRMediaRemoteMessageProtobuf microphoneConnectionRequestMessage]
+ -[_MRMediaRemoteMessageProtobuf microphoneConnectionResponseMessage]
+ -[_MRMediaRemoteMessageProtobuf setMicrophoneConnectionRequestMessage:]
+ -[_MRMediaRemoteMessageProtobuf setMicrophoneConnectionResponseMessage:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf .cxx_destruct]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf copyTo:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf copyWithZone:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf description]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf details]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf dictionaryRepresentation]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf hasDetails]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf hasRapportIdentifier]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf hash]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf isEqual:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf mergeFrom:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf rapportIdentifier]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf readFrom:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf setDetails:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf setRapportIdentifier:]
+ -[_MRMicrophoneConnectionRequestMessageProtobuf writeTo:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf .cxx_destruct]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf StringAsResult:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf copyTo:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf copyWithZone:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf description]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf dictionaryRepresentation]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf hasPairingData]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf hasRapportIdentifier]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf hasResult]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf hash]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf isEqual:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf mergeFrom:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf pairingData]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf rapportIdentifier]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf readFrom:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf resultAsString:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf result]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf setHasResult:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf setPairingData:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf setRapportIdentifier:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf setResult:]
+ -[_MRMicrophoneConnectionResponseMessageProtobuf writeTo:]
+ -[_MRPlaybackQueueRequestProtobuf addRequestedAnimatedArtworkAssetURLFormats:]
+ -[_MRPlaybackQueueRequestProtobuf addRequestedAnimatedArtworkPreviewFrameFormats:]
+ -[_MRPlaybackQueueRequestProtobuf clearRequestedAnimatedArtworkAssetURLFormats]
+ -[_MRPlaybackQueueRequestProtobuf clearRequestedAnimatedArtworkPreviewFrameFormats]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkAssetURLFormatsAtIndex:]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkAssetURLFormatsCount]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkAssetURLFormats]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkPreviewFrameFormatsAtIndex:]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkPreviewFrameFormatsCount]
+ -[_MRPlaybackQueueRequestProtobuf requestedAnimatedArtworkPreviewFrameFormats]
+ -[_MRPlaybackQueueRequestProtobuf setRequestedAnimatedArtworkAssetURLFormats:]
+ -[_MRPlaybackQueueRequestProtobuf setRequestedAnimatedArtworkPreviewFrameFormats:]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf error]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf hasError]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf hasSetPlaybackSessionCommandStatus]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf setError:]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf setPlaybackSessionCommandStatus]
+ -[_MRPlaybackSessionMigrateEndMessageProtobuf setSetPlaybackSessionCommandStatus:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf StringAsRole:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf addEvents:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf clearEvents]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf error]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf eventsAtIndex:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf eventsCount]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf events]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf hasError]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf hasIdentifier]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf hasInput]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf hasOutput]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf hasRole]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf identifier]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf input]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf output]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf roleAsString:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf role]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setError:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setEvents:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setHasIdentifier:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setHasRole:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setIdentifier:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setInput:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setOutput:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf setRole:]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf(MRAdditions) mr_error]
+ -[_MRPlaybackSessionMigrateRequestEventProtobuf(MRAdditions) reportName]
+ -[_MRPlaybackSessionMigrateRequestProtobuf StringAsRecipeType:]
+ -[_MRPlaybackSessionMigrateRequestProtobuf hasRecipeType]
+ -[_MRPlaybackSessionMigrateRequestProtobuf hasSetPlaybackSessionCommandStatus]
+ -[_MRPlaybackSessionMigrateRequestProtobuf recipeTypeAsString:]
+ -[_MRPlaybackSessionMigrateRequestProtobuf recipeType]
+ -[_MRPlaybackSessionMigrateRequestProtobuf setHasRecipeType:]
+ -[_MRPlaybackSessionMigrateRequestProtobuf setPlaybackSessionCommandStatus]
+ -[_MRPlaybackSessionMigrateRequestProtobuf setRecipeType:]
+ -[_MRPlaybackSessionMigrateRequestProtobuf setSetPlaybackSessionCommandStatus:]
+ -[_MRPlaybackSessionResponseMessageProtobuf hasRequest]
+ -[_MRPlaybackSessionResponseMessageProtobuf request]
+ -[_MRPlaybackSessionResponseMessageProtobuf setRequest:]
+ -[_MRRequestDetailsProtobuf hasOperationID]
+ -[_MRRequestDetailsProtobuf hasSurface]
+ -[_MRRequestDetailsProtobuf operationID]
+ -[_MRRequestDetailsProtobuf setOperationID:]
+ -[_MRRequestDetailsProtobuf setSurface:]
+ -[_MRRequestDetailsProtobuf surface]
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table214
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table299
+ GCC_except_table328
+ GCC_except_table53
+ OBJC_IVAR_$__MRAVOutputDeviceDescriptorProtobuf._deviceIsPlaying
+ OBJC_IVAR_$__MRAVOutputDeviceDescriptorProtobuf._wasDiscoveredInCache
+ OBJC_IVAR_$__MRAnimatedArtworkProtobuf._assetFileURLData
+ OBJC_IVAR_$__MRAnimatedArtworkProtobuf._type
+ OBJC_IVAR_$__MRCommandInfoProtobuf._extendedSupportedRates
+ OBJC_IVAR_$__MRCommandInfoProtobuf._transitionStyle
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._enhanceDialogueActive
+ OBJC_IVAR_$__MRContentItemProtobuf._animatedArtworkPreviewFrames
+ OBJC_IVAR_$__MRContentItemProtobuf._animatedArtworks
+ OBJC_IVAR_$__MRContentItemProtobuf._availableAnimatedArtworkFormats
+ OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._parentGroupSupportsGroupCohesion
+ OBJC_IVAR_$__MRDiscoverySessionConfigurationProtobuf._cachedDiscoveryEnabled
+ OBJC_IVAR_$__MRErrorProtobuf._debugMessage
+ OBJC_IVAR_$__MRErrorProtobuf._userInfo
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._shouldWaitForUpdatedOutputDevices
+ OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._microphoneConnectionRequestMessage
+ OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._microphoneConnectionResponseMessage
+ OBJC_IVAR_$__MRMicrophoneConnectionRequestMessageProtobuf._details
+ OBJC_IVAR_$__MRMicrophoneConnectionRequestMessageProtobuf._rapportIdentifier
+ OBJC_IVAR_$__MRMicrophoneConnectionResponseMessageProtobuf._has
+ OBJC_IVAR_$__MRMicrophoneConnectionResponseMessageProtobuf._pairingData
+ OBJC_IVAR_$__MRMicrophoneConnectionResponseMessageProtobuf._rapportIdentifier
+ OBJC_IVAR_$__MRMicrophoneConnectionResponseMessageProtobuf._result
+ OBJC_IVAR_$__MRPlaybackQueueRequestProtobuf._requestedAnimatedArtworkAssetURLFormats
+ OBJC_IVAR_$__MRPlaybackQueueRequestProtobuf._requestedAnimatedArtworkPreviewFrameFormats
+ OBJC_IVAR_$__MRPlaybackSessionMigrateEndMessageProtobuf._error
+ OBJC_IVAR_$__MRPlaybackSessionMigrateEndMessageProtobuf._setPlaybackSessionCommandStatus
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._error
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._events
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._identifier
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._input
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._output
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._role
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestProtobuf._recipeType
+ OBJC_IVAR_$__MRPlaybackSessionMigrateRequestProtobuf._setPlaybackSessionCommandStatus
+ OBJC_IVAR_$__MRPlaybackSessionResponseMessageProtobuf._request
+ OBJC_IVAR_$__MRRequestDetailsProtobuf._operationID
+ OBJC_IVAR_$__MRRequestDetailsProtobuf._surface
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionMediaServicesWereLostNotification
+ _AVAudioSessionRoutingContextChangeNotification
+ _AVOutputContextCanSetVolumeDidChangeNotification
+ _AVOutputContextDestinationChangeInitiatedNotification
+ _AVOutputContextDestinationChangePreviousDeviceIDsKey
+ _AVOutputContextDestinationChangeReasonIdleDisconnect
+ _AVOutputContextDestinationChangeReasonKey
+ _AVOutputContextOutputDeviceDidChangeNotification
+ _AVOutputContextOutputDevicesDidChangeNotification
+ _AVOutputContextPredictedOutputDeviceDidChangeNotification
+ _AVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification
+ _AVOutputContextTypeAudio
+ _AVOutputContextTypeSharedAudioPresentation
+ _AVOutputContextTypeSharedSystemAudio
+ _AVOutputContextTypeSharedSystemScreen
+ _AVOutputContextVolumeControlTypeDidChangeNotification
+ _AVOutputDeviceActivatedClusterMembersRoomIDKey
+ _AVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification
+ _AVOutputDeviceBatteryLevelCaseKey
+ _AVOutputDeviceBatteryLevelLeftKey
+ _AVOutputDeviceBatteryLevelRightKey
+ _AVOutputDeviceBluetoothAlternateTransportTypeDefault
+ _AVOutputDeviceCanMuteDidChangeNotification
+ _AVOutputDeviceCanSetVolumeDidChangeNotification
+ _AVOutputDeviceCommunicationChannelControlTypeDirect
+ _AVOutputDeviceCommunicationChannelControlTypeRelayed
+ _AVOutputDeviceCommunicationChannelDataDestinationMediaRemote
+ _AVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped
+ _AVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired
+ _AVOutputDeviceCommunicationChannelOptionControlType
+ _AVOutputDeviceCommunicationChannelOptionCorrelationID
+ _AVOutputDeviceCommunicationChannelOptionInitiator
+ _AVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate
+ _AVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification
+ _AVOutputDeviceMutedDidChangeNotification
+ _AVOutputDeviceVolumeControlTypeDidChangeNotification
+ _AVOutputDeviceVolumeDidChangeNotification
+ _AirPlaySupportLibrary
+ _AirPlaySupportLibrary.cold.1
+ _AirPlaySupportLibraryCore.frameworkLibrary
+ _AudioFormatGetProperty
+ _BiomeLibraryLibraryCore.frameworkLibrary
+ _BiomeStreamsLibraryCore.frameworkLibrary
+ _CFAllocatorAllocateTyped
+ _CFDataCreateMutable
+ _CGBitmapContextCreateImage
+ _CGColorSpaceCreateDeviceRGB
+ _CGImageDestinationAddImage
+ _CoreUtilsLibraryCore.frameworkLibrary
+ _FrontBoardServicesLibrary
+ _FrontBoardServicesLibrary.cold.1
+ _FrontBoardServicesLibraryCore.frameworkLibrary
+ _IntentsCoreLibraryCore.frameworkLibrary
+ _IntentsLibrary
+ _IntentsLibrary.cold.1
+ _IntentsLibraryCore.frameworkLibrary
+ _MRAVEndpointCarPlayVideoIsActiveDidChangeNotification
+ _MRAVEndpointCarPlayVideoIsAllowedDidChangeNotification
+ _MRAVOutputDeviceB282ModelID
+ _MRAVOutputDeviceB312ModelID
+ _MRAVOutputDeviceB352ModelID
+ _MRAVOutputDeviceB364ModelID
+ _MRAVOutputDeviceB372ModelID
+ _MRAVOutputDeviceB419ModelID
+ _MRAVOutputDeviceB443ModelID
+ _MRAVOutputDeviceB444ModelID
+ _MRAVOutputDeviceB494ModelID
+ _MRAVOutputDeviceB498ModelID
+ _MRAVOutputDeviceB507ModelID
+ _MRAVOutputDeviceB607ModelID
+ _MRAVOutputDeviceStudioDisplayModelID
+ _MRAddRequestDetailsToXPCMessage
+ _MRAudioOutputDeviceDiscoverySessionAllowListContext
+ _MRAudioOutputDeviceDiscoverySessionDenyListContext
+ _MRCSurfaceAmbient
+ _MRCSurfaceMirrorModule
+ _MRCSurfaceVolumeCC
+ _MRCSurfaceVolumeLockScreen
+ _MRComputeBaseRouteUIDWithDefaultSuffixes
+ _MRComputeBaseRouteUIDWithSuffixes
+ _MRComputeClusterMemberID
+ _MRContentItemAnimatedArtworkFormatSquare
+ _MRContentItemAnimatedArtworkFormatTall
+ _MRConvertTimestampToMachAbsoluteTime
+ _MRCopyPossibleRouteUIDSuffixes
+ _MRCopyPossibleRouteUIDSuffixes.cold.1
+ _MRCopyPossibleRouteUIDSuffixes.onceToken
+ _MRCopyPossibleRouteUIDSuffixes.suffixes
+ _MRDeviceSupportsSystemAperture.cold.1
+ _MREqualPlayerPaths
+ _MRLogCategoryMediaControl
+ _MRLogCategoryMediaControl.cold.1
+ _MRLogCategoryMediaControl.log
+ _MRLogCategoryMediaControl.onceToken
+ _MRMediaRemoteDidUnregisterForNowPlayingNotification
+ _MRMediaRemoteGetCommandDescription
+ _MRMediaRemoteParentGroupSupportsGroupCohesion
+ _MRMediaRemotePlaybackSessionIsMigrationPossibleForPlayer
+ _MRMediaRemotePlaybackSessionRequestWithResponse
+ _MRMediaRemotePlaybackSessionSetMigrateFinalizeCallback
+ _MRMediaRemotePlaybackSessionSetMigrateFinalizeCallbackForOrigin
+ _MRMediaRemoteSendPlaybackSessionMigrateFinalize
+ _MRMediaRemoteServiceCopyDeviceInfo.entitlementOnceToken
+ _MRMediaRemoteServiceCopyDeviceInfo.entitlements
+ _MRMediaRemoteServiceCreateGroupWithDevices
+ _MRMediaRemoteServiceCreateGroupWithDevices.cold.1
+ _MRPlaybackSessionMigrateFallbackReasonCopyDescription
+ _MRPlaybackSessionMigrateFallbackReasonStatus
+ _MRRequestDetailsInitiatorAirPlaySessionController
+ _MRRequestDetailsInitiatorIntent
+ _MRRequestDetailsInitiatorSystemEndpointHelper
+ _MRRequestDetailsInitiatorVolumeSlider
+ _MRServiceClientPlaybackSessionMigrateFinalizeCallback
+ _MSVGetDeviceProductType
+ _MSVHasherSharedSeed
+ _MSVNanoIDCreateWithCharacters
+ _MSVNanoIDNoSimilarCharacters
+ _MediaExperienceLibrary
+ _MediaExperienceLibrary.cold.1
+ _MediaExperienceLibraryCore.frameworkLibrary
+ _MobileKeyBagLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_AVOutputContext
+ _OBJC_CLASS_$_AVOutputDevice
+ _OBJC_CLASS_$_AVOutputDeviceDiscoverySession
+ _OBJC_CLASS_$_AVPairedDevice
+ _OBJC_CLASS_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ _OBJC_CLASS_$_MRAnimatedArtwork
+ _OBJC_CLASS_$_MRLocalVolumeHUDPresentationRequest
+ _OBJC_CLASS_$_MRMicrophoneConnectionRequestMessage
+ _OBJC_CLASS_$_MRMicrophoneConnectionResponseMessage
+ _OBJC_CLASS_$_MRNowPlayingAnimatedArtwork
+ _OBJC_CLASS_$_MRVolumeHUDPresentationRequest
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSSecurityScopedURLWrapper
+ _OBJC_CLASS_$__MRAnimatedArtworkProtobuf
+ _OBJC_CLASS_$__MRMicrophoneConnectionRequestMessageProtobuf
+ _OBJC_CLASS_$__MRMicrophoneConnectionResponseMessageProtobuf
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._allowList
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._denyList
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._userDefaults
+ _OBJC_IVAR_$_MRAVLightweightReconnaissanceSession._cachedDiscoveryEnabled
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._cachedDiscoveryEnabled
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySessionConfiguration._cachedDiscoveryEnabled
+ _OBJC_IVAR_$_MRActiveRoutesObserver._activeEndpointSnapshot
+ _OBJC_IVAR_$_MRActiveRoutesObserver._deviceRemovedSnapshot
+ _OBJC_IVAR_$_MRActiveRoutesObserver._deviceRemovedWaitInterval
+ _OBJC_IVAR_$_MRActiveRoutesObserver._deviceRemovedWaitIntervalTimer
+ _OBJC_IVAR_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot._date
+ _OBJC_IVAR_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot._endpoint
+ _OBJC_IVAR_$_MRAnimatedArtwork._assetFileURLWrapper
+ _OBJC_IVAR_$_MRContentItem._animatedArtworkPreviewFrames
+ _OBJC_IVAR_$_MRContentItem._animatedArtworks
+ _OBJC_IVAR_$_MRContentItem._availableAnimatedArtworkFormats
+ _OBJC_IVAR_$_MRDeviceInfo._hasParentGroupSupportsGroupCohesion
+ _OBJC_IVAR_$_MRDeviceInfo._parentGroupSupportsGroupCohesion
+ _OBJC_IVAR_$_MRDistantExternalDevice._lastConnectionError
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._shouldWaitForUpdatedOutputDevices
+ _OBJC_IVAR_$_MRMicrophoneConnectionRequestMessage._details
+ _OBJC_IVAR_$_MRMicrophoneConnectionRequestMessage._rapportIdentifier
+ _OBJC_IVAR_$_MRMicrophoneConnectionResponseMessage._pairingData
+ _OBJC_IVAR_$_MRMicrophoneConnectionResponseMessage._rapportIdentifier
+ _OBJC_IVAR_$_MRNowPlayingAnimatedArtwork._artworkAssetFileURLRequestHandler
+ _OBJC_IVAR_$_MRNowPlayingAnimatedArtwork._previewFrameDataRequestHandler
+ _OBJC_IVAR_$_MRNowPlayingControllerHelper._repeatModeDidChange
+ _OBJC_IVAR_$_MRNowPlayingControllerHelper._shuffleModeDidChange
+ _OBJC_IVAR_$_MRNowPlayingOriginClient._playbackSessionMigrateFinalizeCallback
+ _OBJC_IVAR_$_MRNowPlayingPlayerClient._nowPlayingAnimatedArtwork
+ _OBJC_IVAR_$_MRNowPlayingPlayerClient._nowPlayingArtworkID
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._animatedArtworkCallbacks
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._animatedArtworkToken
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._playbackSessionMigrateFinalizeCallback
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._requestedAnimatedArtworkAssetURLFormats
+ _OBJC_IVAR_$_MRPlaybackQueueRequest._requestedAnimatedArtworkPreviewFrameFormats
+ _OBJC_IVAR_$_MRPlaybackSessionMigrateRequest._finalized
+ _OBJC_IVAR_$_MRPlaybackSessionMigrateRequest._lock
+ _OBJC_IVAR_$_MRPlaybackSessionResponseMessage._request
+ _OBJC_IVAR_$_MRRequestDetails._operationID
+ _OBJC_IVAR_$_MRRequestDetails._surface
+ _OBJC_METACLASS_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ _OBJC_METACLASS_$_MRAnimatedArtwork
+ _OBJC_METACLASS_$_MRLocalVolumeHUDPresentationRequest
+ _OBJC_METACLASS_$_MRMicrophoneConnectionRequestMessage
+ _OBJC_METACLASS_$_MRMicrophoneConnectionResponseMessage
+ _OBJC_METACLASS_$_MRNowPlayingAnimatedArtwork
+ _OBJC_METACLASS_$_MRVolumeHUDPresentationRequest
+ _OBJC_METACLASS_$__MRAnimatedArtworkProtobuf
+ _OBJC_METACLASS_$__MRMicrophoneConnectionRequestMessageProtobuf
+ _OBJC_METACLASS_$__MRMicrophoneConnectionResponseMessageProtobuf
+ _OUTLINED_FUNCTION_40
+ _PowerLogLibraryCore.frameworkLibrary
+ _SpringBoardServicesLibraryCore.frameworkLibrary
+ _TelephonyUtilitiesLibrary
+ _TelephonyUtilitiesLibrary.cold.1
+ _TelephonyUtilitiesLibraryCore.frameworkLibrary
+ _UTTypeJPEG
+ __FirstErrorEvent
+ __MRAnimatedArtworkProtobufReadFrom
+ __MRLogCategoryDefault
+ __MRLogCategoryMirroringView
+ __MRMicrophoneConnectionRequestMessageProtobufReadFrom
+ __MRMicrophoneConnectionResponseMessageProtobufReadFrom
+ __MRNowPlayingInfoAnimatedArtworkIdentifierKeyForFormat
+ __MRNowPlayingSupportedAnimatedArtworkFormats
+ __MRNowPlayingSupportedAnimatedArtworkFormats.all
+ __MRNowPlayingSupportedAnimatedArtworkFormats.cold.1
+ __MRNowPlayingSupportedAnimatedArtworkFormats.onceToken
+ __MRProtoUtilsProtoValueFromPlistType.cold.2
+ __MSV_XXH_XXH32_update
+ __MSV_XXH_XXH64_update
+ __OBJC_$_CATEGORY_NSArray_$_MRAVRoutingDiscoverySessionWrapperAdditions
+ __OBJC_$_CLASS_METHODS_MRLocalVolumeHUDPresentationRequest
+ __OBJC_$_CLASS_METHODS_MRVolumeHUDPresentationRequest
+ __OBJC_$_CLASS_METHODS__MRPlaybackSessionMigrateRequestEventProtobuf
+ __OBJC_$_CLASS_PROP_LIST_MRAVLocalEndpoint
+ __OBJC_$_CLASS_PROP_LIST_MRVolumeHUDPresentationRequest
+ __OBJC_$_INSTANCE_METHODS_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ __OBJC_$_INSTANCE_METHODS_MRAnimatedArtwork
+ __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions|MRProtocolMessageLoggerAdditions)
+ __OBJC_$_INSTANCE_METHODS_MRMicrophoneConnectionRequestMessage
+ __OBJC_$_INSTANCE_METHODS_MRMicrophoneConnectionResponseMessage
+ __OBJC_$_INSTANCE_METHODS_MRNowPlayingAnimatedArtwork
+ __OBJC_$_INSTANCE_METHODS_MRVolumeHUDPresentationRequest
+ __OBJC_$_INSTANCE_METHODS_NSArray(MRAVRoutingDiscoverySessionWrapperAdditions|MRAVAdditions|MRCommandInfoAdditions|MRAdditionsFormatting|MRAdditions)
+ __OBJC_$_INSTANCE_METHODS__MRAnimatedArtworkProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRAVLightweightReconnaissanceSession
+ __OBJC_$_INSTANCE_VARIABLES_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_MRAnimatedArtwork
+ __OBJC_$_INSTANCE_VARIABLES_MRMicrophoneConnectionRequestMessage
+ __OBJC_$_INSTANCE_VARIABLES_MRMicrophoneConnectionResponseMessage
+ __OBJC_$_INSTANCE_VARIABLES_MRNowPlayingAnimatedArtwork
+ __OBJC_$_INSTANCE_VARIABLES_MRPlaybackSessionResponseMessage
+ __OBJC_$_INSTANCE_VARIABLES__MRAnimatedArtworkProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_$_PROP_LIST_MRAVLightweightReconnaissanceSession
+ __OBJC_$_PROP_LIST_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ __OBJC_$_PROP_LIST_MRAnimatedArtwork
+ __OBJC_$_PROP_LIST_MRMicrophoneConnectionRequestMessage
+ __OBJC_$_PROP_LIST_MRMicrophoneConnectionResponseMessage
+ __OBJC_$_PROP_LIST__MRAnimatedArtworkProtobuf
+ __OBJC_$_PROP_LIST__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_$_PROP_LIST__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRVolumeUIControllable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRVolumeUIServerXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRVolumeUIControllable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRVolumeUIServerXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_MRVolumeUIControllable
+ __OBJC_$_PROTOCOL_REFS_MRVolumeUIServerXPCProtocol
+ __OBJC_CLASS_PROTOCOLS_$_MRVolumeHUDPresentationRequest
+ __OBJC_CLASS_PROTOCOLS_$__MRAnimatedArtworkProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_CLASS_RO_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ __OBJC_CLASS_RO_$_MRAnimatedArtwork
+ __OBJC_CLASS_RO_$_MRLocalVolumeHUDPresentationRequest
+ __OBJC_CLASS_RO_$_MRMicrophoneConnectionRequestMessage
+ __OBJC_CLASS_RO_$_MRMicrophoneConnectionResponseMessage
+ __OBJC_CLASS_RO_$_MRNowPlayingAnimatedArtwork
+ __OBJC_CLASS_RO_$_MRVolumeHUDPresentationRequest
+ __OBJC_CLASS_RO_$__MRAnimatedArtworkProtobuf
+ __OBJC_CLASS_RO_$__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_CLASS_RO_$__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_LABEL_PROTOCOL_$_MRVolumeUIControllable
+ __OBJC_LABEL_PROTOCOL_$_MRVolumeUIServerXPCProtocol
+ __OBJC_METACLASS_RO_$_MRActiveRoutesObserverOutputDeviceRemovedSnapshot
+ __OBJC_METACLASS_RO_$_MRAnimatedArtwork
+ __OBJC_METACLASS_RO_$_MRLocalVolumeHUDPresentationRequest
+ __OBJC_METACLASS_RO_$_MRMicrophoneConnectionRequestMessage
+ __OBJC_METACLASS_RO_$_MRMicrophoneConnectionResponseMessage
+ __OBJC_METACLASS_RO_$_MRNowPlayingAnimatedArtwork
+ __OBJC_METACLASS_RO_$_MRVolumeHUDPresentationRequest
+ __OBJC_METACLASS_RO_$__MRAnimatedArtworkProtobuf
+ __OBJC_METACLASS_RO_$__MRMicrophoneConnectionRequestMessageProtobuf
+ __OBJC_METACLASS_RO_$__MRMicrophoneConnectionResponseMessageProtobuf
+ __OBJC_PROTOCOL_$_MRVolumeUIControllable
+ __OBJC_PROTOCOL_$_MRVolumeUIServerXPCProtocol
+ ___102-[MRExternalOutputContextDataSource initWithUniqueIdentifier:outputDevices:volume:capabilities:muted:]_block_invoke
+ ___102-[MRQHONowPlayingController _onQueue_requestAndUpdateArtworkForContentItems:forPlayerPath:withReason:]_block_invoke.38
+ ___103+[MRAVEndpoint addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
+ ___103-[MRAVLightweightReconnaissanceSession searchEndpointsForCompanionWithTimeout:reason:queue:completion:]_block_invoke.109
+ ___104+[MRAVEndpoint moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
+ ___104-[MRAVLightweightReconnaissanceSession searchForLogicalOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.130
+ ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke
+ ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.624
+ ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.cold.1
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.654
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.656
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.661
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.668
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.657
+ ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.595
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForMyGroupLeaderWithTimeout:reason:queue:completion:]_block_invoke.147
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.79
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke.178
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke.189
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke_2
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke_2.190
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke_3
+ ___109-[MRAVLightweightReconnaissanceSession searchEndpointsForRoutingContextUID:timeout:details:queue:completion:]_block_invoke.142
+ ___112-[MRAVLightweightReconnaissanceSession searchEndpointsForLeaderOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.113
+ ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.606
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.637
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.644
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.277
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.278
+ ___143-[MROutputContextController _onSerialQueue_performOperationForOutputDeviceUID:withCapabilities:systemOperation:deviceOperation:groupOperation:]_block_invoke
+ ___143-[MROutputContextController _onSerialQueue_performOperationForOutputDeviceUID:withCapabilities:systemOperation:deviceOperation:groupOperation:]_block_invoke_2
+ ___25-[MRMediaControls _reset]_block_invoke.70
+ ___25-[MRUIController dealloc]_block_invoke.64
+ ___25-[MRUIController dealloc]_block_invoke.67
+ ___25-[MRUIController dealloc]_block_invoke.70
+ ___31-[MRAVEndpoint isMyGroupLeader]_block_invoke
+ ___31-[MRUIController _restoreState]_block_invoke.55
+ ___31-[MRUIController xpcConnection]_block_invoke.172
+ ___35-[MRPowerLogger logEvent:withInfo:]_block_invoke.cold.1
+ ___35-[MRUserSettings disableAWDLRoutes]_block_invoke
+ ___36-[MRAVEndpoint isCarPlayVideoActive]_block_invoke
+ ___37-[MRAVEndpoint isCarPlayVideoAllowed]_block_invoke
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.222
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.223
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke.226
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.228
+ ___39-[MRUserSettings carPlayBannersEnabled]_block_invoke
+ ___42-[MROutputContextController isVolumeMuted]_block_invoke
+ ___45-[MRUserSettings microphoneConnectionTimeout]_block_invoke
+ ___46-[MRDistantExternalDevice lastConnectionError]_block_invoke
+ ___47-[MRMediaRemoteServiceClient _resumeConnection]_block_invoke.43
+ ___47-[MRNowPlayingPlayerClient nowPlayingArtworkID]_block_invoke
+ ___47-[MROutputContextController _inititalizeVolume]_block_invoke.306
+ ___47-[MROutputContextController _inititalizeVolume]_block_invoke.308
+ ___47-[MROutputContextController _inititalizeVolume]_block_invoke.310
+ ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.218
+ ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.296
+ ___51-[MRNowPlayingPlayerClient setNowPlayingArtworkID:]_block_invoke
+ ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.471
+ ___54-[MRAVLocalEndpoint setCarPlayVideoActive:completion:]_block_invoke
+ ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.412
+ ___56+[MRNowPlayingController performRequest:withCompletion:]_block_invoke.269
+ ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.415
+ ___56-[MRUIController setPreferredState:forBundleIdentifier:]_block_invoke
+ ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.503
+ ___60-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload]_block_invoke
+ ___60-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload]_block_invoke_2
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.512
+ ___60-[MRNowPlayingPlayerClient nowPlayingAnimatedArtworkFormats]_block_invoke
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.401
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.401.cold.1
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.402
+ ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.413
+ ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.419
+ ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.586
+ ___63-[MRNowPlayingClient _avSessionMediaServicesResetNotification:]_block_invoke.cold.1
+ ___63-[MRNowPlayingPlayerClient nowPlayingAnimatedArtworkForFormat:]_block_invoke
+ ___64-[MRAVEndpoint requestGroupSessionWithDetails:queue:completion:]_block_invoke.431
+ ___64-[MRActiveRoutesObserver _onWorkerQueue_reevaluateWithEndpoint:]_block_invoke
+ ___64-[MRActiveRoutesObserver _onWorkerQueue_reevaluateWithEndpoint:]_block_invoke.cold.1
+ ___65+[MRAVLocalEndpoint sharedLocalEndpointForRoutingContextWithUID:]_block_invoke.10
+ ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.300
+ ___65-[MRExpanseManager canAddTelevisionWithRouteIdentifierToSession:]_block_invoke
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.388
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.388.cold.1
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.389
+ ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.261
+ ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.305
+ ___66-[MRNowPlayingOriginClient playbackSessionMigrateFinalizeCallback]_block_invoke
+ ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.60
+ ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.68
+ ___66-[MROutputContextController modifyTopologyWithRequest:completion:]_block_invoke
+ ___66-[MROutputContextController modifyTopologyWithRequest:completion:]_block_invoke_2
+ ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.559
+ ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.552
+ ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.298
+ ___67-[MRNowPlayingPlayerClient setNowPlayingAnimatedArtwork:forFormat:]_block_invoke
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.395
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.395.cold.1
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.397
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.400
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.400.cold.1
+ ___68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.37
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.385
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.393
+ ___68-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesAddedCallback:]_block_invoke
+ ___68-[MRNowPlayingController sendCommand:options:appOptions:completion:]_block_invoke.283
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.382
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.382.cold.1
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.384
+ ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.414
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.306
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.307
+ ___69-[MRQHONowPlayingController _handlePlaybackQueueChangedNotification:]_block_invoke.96
+ ___69-[MRQHONowPlayingController _handlePlaybackStateChangedNotification:]_block_invoke.106
+ ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.418
+ ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.610
+ ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesChangedCallback:]_block_invoke
+ ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesRemovedCallback:]_block_invoke
+ ___70-[MRNowPlayingOriginClient setPlaybackSessionMigrateFinalizeCallback:]_block_invoke
+ ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.444
+ ___71-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesModifiedCallback:]_block_invoke
+ ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke
+ ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke.437
+ ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke.cold.1
+ ___72-[MRAVEndpoint requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke_2
+ ___72-[MRActiveRoutesObserver _handleActiveSystemEndpointDidAddOutputDevice:]_block_invoke
+ ___72-[NSArray(MRAVRoutingDiscoverySessionWrapperAdditions) nonCachedResults]_block_invoke
+ ___73-[MRQHONowPlayingController _handleSupportedCommandsChangedNotification:]_block_invoke.107
+ ___74-[MRNowPlayingClient enqueueCommand:options:playerPath:commandCompletion:]_block_invoke.306
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke.53
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke_2
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke_2.54
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke_3
+ ___75-[MRNowPlayingPlayerClientCallbacks playbackSessionMigrateFinalizeCallback]_block_invoke
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.569
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.570
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.cold.1
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_2
+ ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.464
+ ___77+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:localDeviceInfo:]_block_invoke
+ ___77+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:localDeviceInfo:]_block_invoke_2
+ ___77+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:localDeviceInfo:]_block_invoke_3
+ ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.489
+ ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.299
+ ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.479
+ ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.303
+ ___79-[MRNowPlayingPlayerClientCallbacks setPlaybackSessionMigrateFinalizeCallback:]_block_invoke
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.211
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.221
+ ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.230
+ ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.304
+ ___81-[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke
+ ___81-[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_2
+ ___81-[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_3
+ ___81-[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_4
+ ___81-[MRAVConcreteOutputContext modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_5
+ ___81-[MRQHONowPlayingController _loadNowPlayingStateForUID:client:player:completion:]_block_invoke.17
+ ___81-[MRQHONowPlayingController _loadNowPlayingStateForUID:client:player:completion:]_block_invoke.17.cold.1
+ ___82-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke
+ ___82-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_2
+ ___82-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_3
+ ___82-[MRAVOutputContextEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke
+ ___82-[MRAVOutputContextEndpoint _modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke_2
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.250
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.254
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.263
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.270
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.304
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.322
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.340
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.350
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.369
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.255
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.277
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.305
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.315
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.329
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.353
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.380
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.284
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.330
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.356
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.287
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.358
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.291
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.359
+ ___83-[MRDistantExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke
+ ___83-[MRDistantExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke_2
+ ___83-[MRDistantExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke_3
+ ___83-[MRDistantExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]_block_invoke_4
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke.119
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_2.123
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_3.124
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_4.137
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_5.139
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke_2
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke_3
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke_4
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke_5
+ ___83-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoAnimatedArtworkCallback:]_block_invoke_6
+ ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke
+ ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.580
+ ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.cold.1
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.203
+ ___86+[MRNowPlayingController sendCommand:toDestination:options:appOptions:withCompletion:]_block_invoke.275
+ ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.19
+ ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.19.cold.1
+ ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.19.cold.2
+ ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.19.cold.3
+ ___90-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke
+ ___90-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke_2
+ ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.286
+ ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.302
+ ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.295
+ ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke.158
+ ___92-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupUID:features:details:]_block_invoke
+ ___92-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupUID:features:details:]_block_invoke_2
+ ___92-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupUID:features:details:]_block_invoke_3
+ ___92-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupUID:features:details:]_block_invoke_4
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.35
+ ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.291
+ ___93-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke
+ ___93-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_2
+ ___93-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_3
+ ___93-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke_4
+ ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.120
+ ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.126
+ ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.102
+ ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.94
+ ___AirPlaySupportLibraryCore_block_invoke
+ ___BiomeLibraryLibraryCore_block_invoke
+ ___BiomeStreamsLibraryCore_block_invoke
+ ___CoreUtilsLibraryCore_block_invoke
+ ___FrontBoardServicesLibraryCore_block_invoke
+ ___IntentsCoreLibraryCore_block_invoke
+ ___IntentsLibraryCore_block_invoke
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.114
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.143
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.143.cold.1
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.153
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.160
+ ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.96
+ ___MRAnalyticsSendEvent_block_invoke.383
+ ___MRCopyPossibleRouteUIDSuffixes_block_invoke
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.334
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.338
+ ___MRLogCategoryMediaControl_block_invoke
+ ___MRMediaRemoteGetClientProperties_block_invoke.553
+ ___MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.594
+ ___MRMediaRemoteGetPlayerProperties_block_invoke.584
+ ___MRMediaRemotePlaybackSessionIsMigrationPossibleForPlayer_block_invoke
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke.19
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke_2
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke_2.22
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke_2.cold.1
+ ___MRMediaRemotePlaybackSessionRequestWithResponse_block_invoke_3
+ ___MRMediaRemoteSendPlaybackSessionMigrateFinalize_block_invoke
+ ___MRMediaRemoteSendPlaybackSessionMigrateFinalize_block_invoke.cold.1
+ ___MRMediaRemoteServiceCopyDeviceInfo_block_invoke
+ ___MRMediaRemoteServiceCreateGroupWithDevices_block_invoke
+ ___MRMediaRemoteSetPlaybackStateForPlayerWithTimestamp_block_invoke.612
+ ___MRServiceClientPlaybackSessionCallback_block_invoke
+ ___MRServiceClientPlaybackSessionMigrateFinalizeCallback_block_invoke
+ ___MediaExperienceLibraryCore_block_invoke
+ ___MobileKeyBagLibraryCore_block_invoke
+ ___PowerLogLibraryCore_block_invoke
+ ___SpringBoardServicesLibraryCore_block_invoke
+ ___TelephonyUtilitiesLibraryCore_block_invoke
+ ____MRHandlePlaybackQueueRequest_block_invoke.89
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.444
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.445
+ ____MRNowPlayingSupportedAnimatedArtworkFormats_block_invoke
+ ____MRPSMPerformLegacyMigration_block_invoke.134
+ ____MRPSMPerformLegacyMigration_block_invoke_2.138
+ ____MRPSMPerformLegacyMigration_block_invoke_3.139
+ ____MRPSMPerformLegacyMigration_block_invoke_4.140
+ ____MRSetNowPlayingInfo_block_invoke.46
+ ____MRSetNowPlayingInfo_block_invoke_2.50
+ ____onQueue_MRHandlePlaybackQueueRequest_block_invoke.77
+ ____onQueue_MRHandlePlaybackQueueRequest_block_invoke.cold.1
+ ____onQueue_MRInvokeClientAssetCallbacks_block_invoke_10
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_32_e34_B16?0"MRAVConcreteOutputDevice"8l
+ ___block_descriptor_32_e44_"MRAVOutputDevice"16?0"MRAVOutputDevice"8l
+ ___block_descriptor_40_e8_32s_e28_"NSString"16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_B16?0"TUNearbyDeviceHandle"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_B16?0"MRAVConcreteOutputDevice"8ls32l8
+ ___block_descriptor_40_e8_32s_e45_B16?0"_MRAVOutputDeviceDescriptorProtobuf"8ls32l8
+ ___block_descriptor_40_e8_32s_e54_v24?0"MRPlaybackSessionResponseMessage"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e61_v24?0"MRPlaybackSessionMigrateResponseMessage"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSArray"8ls32l8w40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e18_B16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e35_v32?0^v8^v16?<v?^{__CFError=}>24lw40l8s32l8
+ ___block_descriptor_52_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e20_v16?0^{__CFError=}8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e23_v20?0I8^{__CFArray=}12ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e24_v24?0^v8^{__CFError=}16ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e25_v16?0"MRCommandResult"8ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e32_v16?0"<MRAVDiscoverySession>"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e61_v24?0"MRPlaybackSessionMigrateResponseMessage"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40bs48bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40bs48r_e24_v24?0^v8^{__CFError=}16lr48l8s32l8s40l8
+ ___block_descriptor_60_e8_32s40bs48r_e8_v12?0I8lr48l8s32l8s40l8
+ ___block_descriptor_60_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48bs_e24_v24?0^v8^{__CFError=}16ls32l8s48l8s40l8
+ ___block_descriptor_60_e8_32s40s48bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32ls32l8s40l8s48l8
+ ___block_descriptor_60_e8_32s40s48bs_e61_v24?0"MRPlaybackSessionMigrateResponseMessage"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e54_v24?0"MRPlaybackSessionResponseMessage"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e53_v24?0"MRPlaybackSessionMigrateRequest"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e61_v24?0"MRPlaybackSessionMigrateResponseMessage"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"MRPlayerPath"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e24_v16?0?<v?"NSError">8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e24_v16?0?<v?"NSError">8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e15_v16?0"NSURL"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40bs48bs56r_e20_v24?0q8"NSError"16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_68_e8_32s40s48bs56r_e54_v24?0"MRPlaybackSessionResponseMessage"8"NSError"16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e54_v24?0"MRPlaybackSessionResponseMessage"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56bs64bs_e43_v32?0"MROrigin"8"MROrigin"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_76_e8_32s40s48s56bs64bs_e53_v24?0"MRPlaybackSessionMigrateRequest"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e24_v24?0^v8^{__CFError=}16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e24_v24?0^v8^{__CFError=}16ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e17_v16?0"NSError"8ls32l8r64l8s40l8r72l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e52_v24?0"NSString"8?<v?"MRAVEndpoint""NSError">16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_84_e8_32s40s48s56bs64bs72bs_e30_v24?0"NSString"8"NSError"16ls32l8s56l8s40l8s48l8s64l8s72l8
+ ___block_descriptor_84_e8_32s40s48s56bs64bs72w_e17_v16?0"NSError"8lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_84_e8_32s40s48s56s64s72bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_84_e8_32s40s48s56s64s72bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.102
+ ___block_literal_global.109
+ ___block_literal_global.115
+ ___block_literal_global.124
+ ___block_literal_global.155
+ ___block_literal_global.162
+ ___block_literal_global.163
+ ___block_literal_global.174
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.186
+ ___block_literal_global.190
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.200
+ ___block_literal_global.223
+ ___block_literal_global.230
+ ___block_literal_global.235
+ ___block_literal_global.240
+ ___block_literal_global.262
+ ___block_literal_global.274
+ ___block_literal_global.280
+ ___block_literal_global.299
+ ___block_literal_global.307
+ ___block_literal_global.325
+ ___block_literal_global.33
+ ___block_literal_global.343
+ ___block_literal_global.35
+ ___block_literal_global.352
+ ___block_literal_global.355
+ ___block_literal_global.36
+ ___block_literal_global.361
+ ___block_literal_global.371
+ ___block_literal_global.379
+ ___block_literal_global.39
+ ___block_literal_global.395
+ ___block_literal_global.442
+ ___block_literal_global.491
+ ___block_literal_global.493
+ ___block_literal_global.5
+ ___block_literal_global.519
+ ___block_literal_global.580
+ ___block_literal_global.582
+ ___block_literal_global.583
+ ___block_literal_global.59
+ ___block_literal_global.599
+ ___block_literal_global.63
+ ___block_literal_global.645
+ ___block_literal_global.72
+ ___block_literal_global.75
+ ___getAPSCopyDefaultGroupUUIDSymbolLoc_block_invoke
+ ___getAPSParseGroupIDSymbolLoc_block_invoke
+ ___getAVSystemControllerClass_block_invoke
+ ___getAVSystemControllerClass_block_invoke.cold.1
+ ___getAVSystemController_CanBeNowPlayingAppAttributeSymbolLoc_block_invoke
+ ___getAVSystemController_ServerConnectionDiedNotificationSymbolLoc_block_invoke
+ ___getAVSystemController_SubscribeToNotificationsAttributeSymbolLoc_block_invoke
+ ___getBMPublisherOptionsClass_block_invoke
+ ___getBMPublisherOptionsClass_block_invoke.cold.1
+ ___getBMPublisherOptionsClass_block_invoke.cold.2
+ ___getBiomeLibrarySymbolLoc_block_invoke
+ ___getBiomeLibrarySymbolLoc_block_invoke.cold.1
+ ___getCURunLoopThreadClass_block_invoke
+ ___getCURunLoopThreadClass_block_invoke.cold.1
+ ___getCURunLoopThreadClass_block_invoke.cold.2
+ ___getFBSDisplayLayoutMonitorClass_block_invoke
+ ___getFBSDisplayLayoutMonitorClass_block_invoke.cold.1
+ ___getFBSDisplayLayoutMonitorConfigurationClass_block_invoke
+ ___getFBSDisplayLayoutMonitorConfigurationClass_block_invoke.cold.1
+ ___getINCExtensionConnectionClass_block_invoke
+ ___getINCExtensionConnectionClass_block_invoke.cold.1
+ ___getINCExtensionConnectionClass_block_invoke.cold.2
+ ___getINInteractionClass_block_invoke
+ ___getINInteractionClass_block_invoke.cold.1
+ ___getINMediaItemClass_block_invoke
+ ___getINMediaItemClass_block_invoke.cold.1
+ ___getINPlayMediaIntentClass_block_invoke
+ ___getINPlayMediaIntentClass_block_invoke.cold.1
+ ___getINPlayMediaIntentResponseClass_block_invoke
+ ___getINPlayMediaIntentResponseClass_block_invoke.cold.1
+ ___getINPrivatePlayMediaIntentDataClass_block_invoke
+ ___getINPrivatePlayMediaIntentDataClass_block_invoke.cold.1
+ ___getINSchemaClass_block_invoke
+ ___getINSchemaClass_block_invoke.cold.1
+ ___getMKBDeviceUnlockedSinceBootSymbolLoc_block_invoke
+ ___getMKBDeviceUnlockedSinceBootSymbolLoc_block_invoke.cold.1
+ ___getPLLogRegisteredEventSymbolLoc_block_invoke
+ ___getPLLogRegisteredEventSymbolLoc_block_invoke.cold.1
+ ___getSBSIsSystemApertureAvailableSymbolLoc_block_invoke
+ ___getSBSIsSystemApertureAvailableSymbolLoc_block_invoke.cold.1
+ ___getTUConversationManagerClass_block_invoke
+ ___getTUConversationManagerClass_block_invoke.cold.1
+ ___getTUNearbyDeviceHandleClass_block_invoke
+ ___getTUNearbyDeviceHandleClass_block_invoke.cold.1
+ ___getTUNeighborhoodActivityConduitClass_block_invoke
+ ___getTUNeighborhoodActivityConduitClass_block_invoke.cold.1
+ ___getkMXSession_SourceFormatInfoKey_BestAvailableContentType_AtmosSymbolLoc_block_invoke
+ ___getkMXSession_SourceFormatInfoKey_BestAvailableContentType_MultichannelSymbolLoc_block_invoke
+ __onSerialQueue_performOperationForOutputDeviceUID:withCapabilities:systemOperation:deviceOperation:groupOperation:.onceToken
+ __sl_dlopen
+ _audit_stringAirPlaySupport
+ _audit_stringBiomeLibrary
+ _audit_stringBiomeStreams
+ _audit_stringCoreUtils
+ _audit_stringFrontBoardServices
+ _audit_stringIntents
+ _audit_stringIntentsCore
+ _audit_stringMediaExperience
+ _audit_stringMobileKeyBag
+ _audit_stringPowerLog
+ _audit_stringSpringBoardServices
+ _audit_stringTelephonyUtilities
+ _carPlayBannersEnabled.__value
+ _carPlayBannersEnabled.onceToken
+ _disableAWDLRoutes.__value
+ _disableAWDLRoutes.onceToken
+ _dlerror
+ _getAPSCopyDefaultGroupUUIDSymbolLoc.ptr
+ _getAPSParseGroupIDSymbolLoc.ptr
+ _getAVSystemControllerClass.softClass
+ _getAVSystemController_CanBeNowPlayingAppAttribute.cold.1
+ _getAVSystemController_CanBeNowPlayingAppAttributeSymbolLoc.ptr
+ _getAVSystemController_ServerConnectionDiedNotification.cold.1
+ _getAVSystemController_ServerConnectionDiedNotificationSymbolLoc.ptr
+ _getAVSystemController_SubscribeToNotificationsAttribute.cold.1
+ _getAVSystemController_SubscribeToNotificationsAttributeSymbolLoc.ptr
+ _getBMPublisherOptionsClass.softClass
+ _getBiomeLibrarySymbolLoc.ptr
+ _getCURunLoopThreadClass.softClass
+ _getFBSDisplayLayoutMonitorClass.softClass
+ _getFBSDisplayLayoutMonitorConfigurationClass.softClass
+ _getINCExtensionConnectionClass.softClass
+ _getINInteractionClass.softClass
+ _getINMediaItemClass.softClass
+ _getINPlayMediaIntentClass.softClass
+ _getINPlayMediaIntentResponseClass.softClass
+ _getINPrivatePlayMediaIntentDataClass.softClass
+ _getINSchemaClass.softClass
+ _getMKBDeviceUnlockedSinceBootSymbolLoc.ptr
+ _getPLLogRegisteredEventSymbolLoc.ptr
+ _getSBSIsSystemApertureAvailableSymbolLoc.ptr
+ _getTUConversationManagerClass.softClass
+ _getTUNearbyDeviceHandleClass.softClass
+ _getTUNeighborhoodActivityConduitClass.softClass
+ _getkMXSession_SourceFormatInfoKey_BestAvailableContentType_AtmosSymbolLoc.ptr
+ _getkMXSession_SourceFormatInfoKey_BestAvailableContentType_MultichannelSymbolLoc.ptr
+ _kMREventGroupSessionAutoApproveReasonAppleTV
+ _kMRMediaRemoteCommandInfoExtendedSupportedPlaybackRates
+ _kMRMediaRemoteCommandInfoTransitionStyle
+ _kMRMediaRemoteNowPlayingInfoSquareAnimatedArtwork
+ _kMRMediaRemoteNowPlayingInfoSquareAnimatedArtworkIdentifier
+ _kMRMediaRemoteNowPlayingInfoTallAnimatedArtwork
+ _kMRMediaRemoteNowPlayingInfoTallAnimatedArtworkIdentifier
+ _kMRMediaRemoteOptionEnhanceDialogueActive
+ _kMRMigrateInitiatorModernPicker
+ _mach_continuous_time
+ _microphoneConnectionTimeout.__once
+ _microphoneConnectionTimeout.__timeout
+ _objc_msgSend$_computeActiveRouteIDsFromEndpoint:localDeviceInfo:
+ _objc_msgSend$_groupSessionComponentsWithScheme:host:
+ _objc_msgSend$_loadDefaults
+ _objc_msgSend$_mostRelevantItem
+ _objc_msgSend$_setError
+ _objc_msgSend$_shouldLogChanges
+ _objc_msgSend$activeEndpointSnapshot
+ _objc_msgSend$addAnimatedArtworkPreviewFrames:
+ _objc_msgSend$addAnimatedArtworks:
+ _objc_msgSend$addAvailableAnimatedArtworkFormats:
+ _objc_msgSend$addEventInput:withKey:toEventID:
+ _objc_msgSend$addEventOutput:withKey:toEventID:
+ _objc_msgSend$addExtendedSupportedRate:
+ _objc_msgSend$addRequestedAnimatedArtworkAssetURLFormats:
+ _objc_msgSend$addRequestedAnimatedArtworkPreviewFrameFormats:
+ _objc_msgSend$animatedArtworkCallbacks
+ _objc_msgSend$animatedArtworkPreviewFrames
+ _objc_msgSend$animatedArtworkPreviewFramesAtIndex:
+ _objc_msgSend$animatedArtworkPreviewFramesCount
+ _objc_msgSend$animatedArtworks
+ _objc_msgSend$animatedArtworksAtIndex:
+ _objc_msgSend$animatedArtworksCount
+ _objc_msgSend$artworkAssetFileURLWithSize:completion:
+ _objc_msgSend$assetFileURLData
+ _objc_msgSend$availableAnimatedArtworkFormats
+ _objc_msgSend$availableAnimatedArtworkFormatsAtIndex:
+ _objc_msgSend$availableAnimatedArtworkFormatsCount
+ _objc_msgSend$cachedDiscoveryEnabled
+ _objc_msgSend$canAddTelevisionWithRouteIdentifierToSession:
+ _objc_msgSend$clearAnimatedArtworkPreviewFrames
+ _objc_msgSend$clearAnimatedArtworks
+ _objc_msgSend$clearAvailableAnimatedArtworkFormats
+ _objc_msgSend$clearExtendedSupportedRates
+ _objc_msgSend$clearRequestedAnimatedArtworkAssetURLFormats
+ _objc_msgSend$clearRequestedAnimatedArtworkPreviewFrameFormats
+ _objc_msgSend$createEndpointWithOutputDeviceUIDs:details:queue:completion:
+ _objc_msgSend$createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:
+ _objc_msgSend$createHostedEndpointWithOutputDeviceUIDs:details:completion:
+ _objc_msgSend$createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:
+ _objc_msgSend$createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:
+ _objc_msgSend$debugMessage
+ _objc_msgSend$deviceIsPlaying
+ _objc_msgSend$deviceRemovedSnapshot
+ _objc_msgSend$deviceRemovedWaitInterval
+ _objc_msgSend$disableAWDLRoutes
+ _objc_msgSend$discoveredDeviceIsPlaying
+ _objc_msgSend$discoveredOutputDevices
+ _objc_msgSend$effectiveIdentifer
+ _objc_msgSend$effectiveName
+ _objc_msgSend$endEventWithID:
+ _objc_msgSend$endEventWithID:error:
+ _objc_msgSend$extendedSupportedRateAtIndex:
+ _objc_msgSend$extendedSupportedRatesCount
+ _objc_msgSend$hasAssetFileURLData
+ _objc_msgSend$hasEndTimestamp
+ _objc_msgSend$hasInput
+ _objc_msgSend$hasOutput
+ _objc_msgSend$hasParentGroupSupportsGroupCohesion
+ _objc_msgSend$hasTransitionStyle
+ _objc_msgSend$initWithAssetFileURL:
+ _objc_msgSend$initWithMRError:description:underlyingErrors:
+ _objc_msgSend$initWithOrigin:bundleIdentifier:player:
+ _objc_msgSend$initWithOutputDeviceGroupUID:features:details:
+ _objc_msgSend$initWithOutputDeviceUIDs:features:details:
+ _objc_msgSend$initWithPlaybackSession:request:
+ _objc_msgSend$initWithRequest:error:setPlaybackSessionCommandStatus:playerPath:
+ _objc_msgSend$initWithRequestID:surface:initiator:reason:userInitiated:originatingBundleID:
+ _objc_msgSend$initWithURL:readonly:
+ _objc_msgSend$initWithUniqueIdentifier:outputDevices:volume:capabilities:muted:
+ _objc_msgSend$input
+ _objc_msgSend$isCached
+ _objc_msgSend$isCarPlayVideoActive
+ _objc_msgSend$isCarPlayVideoAllowed
+ _objc_msgSend$isEquivalentToDeviceHandle:
+ _objc_msgSend$isFileURL
+ _objc_msgSend$isMyGroupLeader
+ _objc_msgSend$isNonRemoteControllableAirPlayDevice
+ _objc_msgSend$isPrimaryLocalDevice
+ _objc_msgSend$isStudioDisplay
+ _objc_msgSend$isWebKit
+ _objc_msgSend$localizedGroupComposition
+ _objc_msgSend$localizedGroupCompositionForDeviceClass:modelID:
+ _objc_msgSend$microphoneConnectionRequestMessage
+ _objc_msgSend$microphoneConnectionResponseMessage
+ _objc_msgSend$mr_error
+ _objc_msgSend$msv_treeDescription
+ _objc_msgSend$nearbyTVDeviceHandles
+ _objc_msgSend$nonCachedResults
+ _objc_msgSend$nowPlayingAnimatedArtworkForFormat:
+ _objc_msgSend$nowPlayingAnimatedArtworkFormats
+ _objc_msgSend$nowPlayingArtworkID
+ _objc_msgSend$operationID
+ _objc_msgSend$output
+ _objc_msgSend$parentGroupSupportsGroupCohesion
+ _objc_msgSend$playbackSessionMigrateFinalizeCallback
+ _objc_msgSend$position
+ _objc_msgSend$presentVolumeHUDWithRequest:
+ _objc_msgSend$previewFrameDataWithSize:completion:
+ _objc_msgSend$protobufWithFormat:
+ _objc_msgSend$recipeType
+ _objc_msgSend$registerNowPlayingInfoAnimatedArtworkCallback:
+ _objc_msgSend$reportName
+ _objc_msgSend$requestMicrophoneConnectionWithDetails:completion:
+ _objc_msgSend$requestMicrophoneConnectionWithDetails:queue:completion:
+ _objc_msgSend$requestedAnimatedArtworkAssetURLFormats
+ _objc_msgSend$requestedAnimatedArtworkAssetURLFormatsAtIndex:
+ _objc_msgSend$requestedAnimatedArtworkAssetURLFormatsCount
+ _objc_msgSend$requestedAnimatedArtworkPreviewFrameFormats
+ _objc_msgSend$requestedAnimatedArtworkPreviewFrameFormatsAtIndex:
+ _objc_msgSend$requestedAnimatedArtworkPreviewFrameFormatsCount
+ _objc_msgSend$result
+ _objc_msgSend$resultsFromConfiguration:
+ _objc_msgSend$scheme
+ _objc_msgSend$setAnimatedArtworkPreviewFrames:
+ _objc_msgSend$setAnimatedArtworks:
+ _objc_msgSend$setAssetFileURLData:
+ _objc_msgSend$setAvailableAnimatedArtworkFormats:
+ _objc_msgSend$setCachedDiscoveryEnabled:
+ _objc_msgSend$setCarPlayVideoActive:completion:
+ _objc_msgSend$setCarPlayVideoActive:completionHandler:
+ _objc_msgSend$setDebugMessage:
+ _objc_msgSend$setDeviceIsPlaying:
+ _objc_msgSend$setDeviceRemovedWaitInterval:
+ _objc_msgSend$setHasParentGroupSupportsGroupCohesion:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setInput:
+ _objc_msgSend$setMicrophoneConnectionRequestMessage:
+ _objc_msgSend$setMicrophoneConnectionResponseMessage:
+ _objc_msgSend$setNowPlayingAnimatedArtwork:forFormat:
+ _objc_msgSend$setNowPlayingArtworkID:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setOperationID:
+ _objc_msgSend$setOutput:
+ _objc_msgSend$setParentGroupSupportsGroupCohesion:
+ _objc_msgSend$setPlaybackSessionCommandStatus
+ _objc_msgSend$setPlaybackSessionMigrateFinalizeCallback:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setPreferredState:forBundleIdentifier:reply:
+ _objc_msgSend$setRecipeType:
+ _objc_msgSend$setRequestedAnimatedArtworkAssetURLFormats:
+ _objc_msgSend$setRequestedAnimatedArtworkPreviewFrameFormats:
+ _objc_msgSend$setResult:
+ _objc_msgSend$setRole:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setSetPlaybackSessionCommandStatus:
+ _objc_msgSend$setShouldWaitForUpdatedOutputDevices:
+ _objc_msgSend$setSurface:
+ _objc_msgSend$setWasDiscoveredInCache:
+ _objc_msgSend$shouldWaitForUpdatedOutputDevices
+ _objc_msgSend$startEvent:role:
+ _objc_msgSend$stringFromByteCount:
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$supportDiscoveryCaching
+ _objc_msgSend$supportsNativeThirdPartyApps
+ _objc_msgSend$surface
+ _objc_msgSend$transitionStyle
+ _objc_msgSend$url
+ _objc_msgSend$wasDiscoveredInCache
+ _os_signpost_id_generate
+ _soft_APSParseGroupID
+ _soft_APSParseGroupID.cold.1
+ _soft_BiomeLibrary
+ _soft_BiomeLibrary.cold.1
- +[MRAVConcreteEndpoint errorWithChangeResult:outputDevice:]
- +[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]
- +[MRAVRoutingDiscoverySession discoverySessionWithEndpointFeatures:enableThrottling:]
- +[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]
- -[MRAVConcreteEndpoint .cxx_destruct]
- -[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVConcreteEndpoint handleVolumeCapabilityChangedNotification:]
- -[MRAVConcreteEndpoint handleVolumeChangedNotification:]
- -[MRAVConcreteEndpoint initWithDesignatedGroupLeader:outputDevices:]
- -[MRAVConcreteEndpoint initWithOutputDeviceGroup:groupLeader:outputDevices:]
- -[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]
- -[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]
- -[MRAVConcreteEndpoint registerVolumeNotifications]
- -[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVConcreteEndpoint setExternalDevice:]
- -[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]
- -[MRAVConcreteEndpoint setOutputDevices:initiator:withReplyQueue:completion:]
- -[MRAVConcreteEndpoint volumeForOutputDevice:error:]
- -[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]
- -[MRAVConcreteOutputContext attemptLogicalDeviceRecovery].cold.1
- -[MRAVConcreteOutputContext attemptLogicalDeviceRecovery].cold.2
- -[MRAVDistantEndpoint _externalOutputContext]
- -[MRAVDistantRoutingDiscoverySession _shouldAddLocalEndpoint]
- -[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]
- -[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:].cold.1
- -[MRAVOutputDevice isJ327Device]
- -[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]
- -[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:]
- -[MRAVRoutingDiscoverySession populatesExternalDevice]
- -[MRAVRoutingDiscoverySession setPopulatesExternalDevice:]
- -[MRAVRoutingDiscoverySessionConfiguration populatesExternalDevice]
- -[MRAVRoutingDiscoverySessionConfiguration setPopulatesExternalDevice:]
- -[MRAVRoutingDiscoverySessionWrapper setPopulatesExternalDevice:]
- -[MRActiveRoutesObserver _handleActiveSystemEndpointOutputDevicesDidChange:]
- -[MRConcreteEndpoint isConnected]
- -[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]
- -[MRExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]
- -[MRExternalDevice setOutputDevicesRemovedCallback:withQueue:]
- -[MRExternalDevice setOutputDevicesUpdatedCallback:withQueue:]
- -[MRExternalDeviceTransport allowedPlayerPaths]
- -[MROutputContextDataSource isVolumeMuted]
- -[MROutputContextDataSource outputDevices]
- -[MROutputContextDataSource uniqueIdentifier]
- -[MROutputContextDataSource volumeControlCapabilities]
- -[MROutputContextDataSource volume]
- -[MRPlaybackSessionMigrateEndMessage initWithRequest:error:playerPath:]
- -[MRPlaybackSessionMigrateRequest endEvent:]
- -[MRPlaybackSessionMigrateRequest endEvent:withError:]
- -[MRPlaybackSessionMigrateRequest startEvent:]
- -[MRPlaybackSessionResponseMessage initWithPlaybackSession:]
- -[MRPlayer dictionaryRepresentation]
- -[MRUserSettings preferRoutesMatchingMediaType]
- -[MRUserSettings showRouteRecommendationsOutsideApps]
- -[MRUserSettings sourceRecommendationsPlattersFromIR]
- -[MRUserSettings supportNativeToAirPlayASERetargetting]
- -[MRUserSettings undoUnusedAutoRoutes]
- -[MRUserSettings watchIntentionalRouting]
- -[_MRPlaybackSessionMigrateRequestEventProtobuf duration]
- -[_MRPlaybackSessionMigrateRequestEventProtobuf hasDuration]
- -[_MRPlaybackSessionMigrateRequestEventProtobuf setDuration:]
- -[_MRPlaybackSessionMigrateRequestEventProtobuf setHasDuration:]
- -[_MRPlaybackSessionMigrateRequestEventProtobuf(MRAdditions) error]
- GCC_except_table100
- GCC_except_table115
- GCC_except_table121
- GCC_except_table131
- GCC_except_table139
- GCC_except_table141
- GCC_except_table142
- GCC_except_table153
- GCC_except_table155
- GCC_except_table189
- GCC_except_table192
- GCC_except_table197
- GCC_except_table226
- GCC_except_table227
- GCC_except_table296
- GCC_except_table297
- GCC_except_table83
- GCC_except_table88
- GCC_except_table98
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- OBJC_IVAR_$__MRPlaybackSessionMigrateRequestEventProtobuf._duration
- _AVAudioSessionCategoryPlaybackFunction
- _AVAudioSessionFunction
- _AVAudioSessionMediaServicesWereLostNotificationFunction
- _AVAudioSessionRoutingContextChangeNotificationFunction
- _AVFoundationLibrary.sLib
- _AVFoundationLibrary.sOnce
- _AVOutputContextCanSetVolumeDidChangeNotificationFunction
- _AVOutputContextDestinationChangeInitiatedNotificationFunction
- _AVOutputContextDestinationChangePreviousDeviceIDsKeyFunction
- _AVOutputContextDestinationChangeReasonIdleDisconnectFunction
- _AVOutputContextDestinationChangeReasonKeyFunction
- _AVOutputContextFunction
- _AVOutputContextOutputDeviceDidChangeNotificationFunction
- _AVOutputContextOutputDevicesDidChangeNotificationFunction
- _AVOutputContextPredictedOutputDeviceDidChangeNotificationFunction
- _AVOutputContextPredictedOutputDevicesDidChangeNotificationFunction
- _AVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotificationFunction
- _AVOutputContextTypeAudioFunction
- _AVOutputContextTypeSharedAudioPresentationFunction
- _AVOutputContextTypeSharedSystemAudioFunction
- _AVOutputContextTypeSharedSystemScreenFunction
- _AVOutputContextVolumeControlTypeDidChangeNotificationFunction
- _AVOutputDeviceActivatedClusterMembersRoomIDKeyFunction
- _AVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotificationFunction
- _AVOutputDeviceBatteryLevelCaseKeyFunction
- _AVOutputDeviceBatteryLevelLeftKeyFunction
- _AVOutputDeviceBatteryLevelRightKeyFunction
- _AVOutputDeviceCanMuteDidChangeNotificationFunction
- _AVOutputDeviceCanSetVolumeDidChangeNotificationFunction
- _AVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotificationFunction
- _AVOutputDeviceClusterMemberVolumeDidChangeNotificationFunction
- _AVOutputDeviceCommunicationChannelControlTypeDirectFunction
- _AVOutputDeviceCommunicationChannelControlTypeRelayedFunction
- _AVOutputDeviceCommunicationChannelDataDestinationMediaRemoteFunction
- _AVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkippedFunction
- _AVOutputDeviceCommunicationChannelOptionCancelIfAuthRequiredFunction
- _AVOutputDeviceCommunicationChannelOptionControlTypeFunction
- _AVOutputDeviceCommunicationChannelOptionCorrelationIDFunction
- _AVOutputDeviceCommunicationChannelOptionInitiatorFunction
- _AVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegateFunction
- _AVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotificationFunction
- _AVOutputDeviceDiscoverySessionFunction
- _AVOutputDeviceFunction
- _AVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequiredFunction
- _AVOutputDeviceGroupAddOutputDeviceOptionInitiatorFunction
- _AVOutputDeviceGroupRemoveOutputDeviceOptionInitiatorFunction
- _AVOutputDeviceGroupVolumeControlTypeDidChangeNotificationFunction
- _AVOutputDeviceGroupVolumeDidChangeNotificationFunction
- _AVOutputDeviceMutedDidChangeNotificationFunction
- _AVOutputDeviceVolumeControlTypeDidChangeNotificationFunction
- _AVOutputDeviceVolumeDidChangeNotificationFunction
- _AVPairedDeviceFunction
- _AVSystemControllerFunction
- _AVSystemController_CanBeNowPlayingAppAttributeFunction
- _AVSystemController_ServerConnectionDiedNotificationFunction
- _AVSystemController_SubscribeToNotificationsAttributeFunction
- _AirPlaySupportLibrary.sLib
- _AirPlaySupportLibrary.sOnce
- _BMPublisherOptionsFunction
- _BiomeLibraryLibrary.sLib
- _BiomeLibraryLibrary.sOnce
- _BiomeStreamsLibrary.sLib
- _BiomeStreamsLibrary.sOnce
- _CFAllocatorAllocate
- _CURunLoopThreadFunction
- _CoreUtilsLibrary.sLib
- _CoreUtilsLibrary.sOnce
- _FBSDisplayLayoutMonitorConfigurationFunction
- _FBSDisplayLayoutMonitorFunction
- _FrontBoardServicesLibrary.sLib
- _FrontBoardServicesLibrary.sOnce
- _INCExtensionConnectionFunction
- _INInteractionFunction
- _INMediaItemFunction
- _INPlayMediaIntentFunction
- _INPlayMediaIntentResponseFunction
- _INPrivatePlayMediaIntentDataFunction
- _INSchemaFunction
- _IntentsCoreLibrary.sLib
- _IntentsCoreLibrary.sOnce
- _IntentsLibrary.sLib
- _IntentsLibrary.sOnce
- _MRAVOutputDeviceJ327ModelID
- _MRMediaRemoteServiceCreateGroupWithDevicesLeaderOptions
- _MRMediaRemoteServiceCreateGroupWithDevicesLeaderOptions.cold.1
- _MRServiceClientPlaybackSessionMigrateEndCallback
- _MSVProcessIsUsingRoots
- _MediaExperienceLibrary.sLib
- _MediaExperienceLibrary.sOnce
- _MobileKeyBagLibrary.sLib
- _MobileKeyBagLibrary.sOnce
- _OBJC_CLASS_$_MRAVConcreteEndpoint
- _OBJC_IVAR_$_MRAVConcreteEndpoint._outputDeviceGroup
- _OBJC_IVAR_$_MRAVRoutingDiscoverySession._populatesExternalDevice
- _OBJC_IVAR_$_MRAVRoutingDiscoverySessionConfiguration._populatesExternalDevice
- _OBJC_IVAR_$_MRExternalDeviceTransport._allowedPlayerPaths
- _OBJC_IVAR_$_MROutputContextDataSource._outputDevices
- _OBJC_IVAR_$_MROutputContextDataSource._uniqueIdentifier
- _OBJC_IVAR_$_MROutputContextDataSource._volume
- _OBJC_IVAR_$_MROutputContextDataSource._volumeControlCapabilities
- _OBJC_IVAR_$_MROutputContextDataSource._volumeMuted
- _OBJC_METACLASS_$_MRAVConcreteEndpoint
- _PowerLogLibrary.sLib
- _PowerLogLibrary.sOnce
- _SpringBoardServicesLibrary.sLib
- _SpringBoardServicesLibrary.sOnce
- _TUConversationManagerFunction
- _TUNearbyDeviceHandleFunction
- _TUNeighborhoodActivityConduitFunction
- _TelephonyUtilitiesLibrary.sLib
- _TelephonyUtilitiesLibrary.sOnce
- __MRMediaRemotePlaybackSessionRequest
- __OBJC_$_CATEGORY_NSArray_$_MRAVAdditions
- __OBJC_$_CLASS_METHODS_MRAVConcreteEndpoint
- __OBJC_$_INSTANCE_METHODS_MRAVConcreteEndpoint
- __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions)
- __OBJC_$_INSTANCE_METHODS_NSArray(MRAVAdditions|MRCommandInfoAdditions|MRAdditionsFormatting|MRAdditions)
- __OBJC_$_INSTANCE_VARIABLES_MRAVConcreteEndpoint
- __OBJC_CLASS_RO_$_MRAVConcreteEndpoint
- __OBJC_METACLASS_RO_$_MRAVConcreteEndpoint
- ___102-[MRQHONowPlayingController _onQueue_requestAndUpdateArtworkForContentItems:forPlayerPath:withReason:]_block_invoke.36
- ___103-[MRAVLightweightReconnaissanceSession searchEndpointsForCompanionWithTimeout:reason:queue:completion:]_block_invoke.111
- ___104-[MRAVLightweightReconnaissanceSession searchForLogicalOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.132
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.613
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.615
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.620
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.627
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.616
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.567
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.171
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.181
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke_2
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke_2.182
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke_3
- ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForMyGroupLeaderWithTimeout:reason:queue:completion:]_block_invoke.149
- ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.80
- ___109-[MRAVLightweightReconnaissanceSession searchEndpointsForRoutingContextUID:timeout:details:queue:completion:]_block_invoke.144
- ___112-[MRAVLightweightReconnaissanceSession searchEndpointsForLeaderOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.115
- ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.578
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.596
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.603
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.274
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.275
- ___25-[MRMediaControls _reset]_block_invoke.69
- ___25-[MRUIController dealloc]_block_invoke.63
- ___25-[MRUIController dealloc]_block_invoke.66
- ___25-[MRUIController dealloc]_block_invoke.69
- ___31-[MRUIController _restoreState]_block_invoke.54
- ___31-[MRUIController xpcConnection]_block_invoke.165
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.219
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.220
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke.223
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.225
- ___41-[MRPlaybackSessionMigrateRequest report]_block_invoke
- ___47-[MRMediaRemoteServiceClient _resumeConnection]_block_invoke.44
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.290
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.292
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.294
- ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.215
- ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.292
- ___51-[MRPlaybackSessionMigrateRequest analyticsPayload]_block_invoke_2
- ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.452
- ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.403
- ___56+[MRNowPlayingController performRequest:withCompletion:]_block_invoke.268
- ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.406
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.66
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.66.cold.1
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.66.cold.2
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.66.cold.3
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.67
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.72
- ___57-[MRAVConcreteOutputContext attemptLogicalDeviceRecovery]_block_invoke.72.cold.1
- ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.480
- ___60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke
- ___60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke.56
- ___60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke_2
- ___60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke_2.cold.1
- ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.489
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.392
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.392.cold.1
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.393
- ___61+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]_block_invoke
- ___61+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]_block_invoke_2
- ___61+[MRActiveRoutesObserver _computeActiveRouteIDsFromEndpoint:]_block_invoke_3
- ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.404
- ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.410
- ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.558
- ___64-[MRAVEndpoint requestGroupSessionWithDetails:queue:completion:]_block_invoke.414
- ___65+[MRAVLocalEndpoint sharedLocalEndpointForRoutingContextWithUID:]_block_invoke.4
- ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.296
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.379
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.379.cold.1
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.380
- ___66-[MRAVConcreteEndpoint handleVolumeCapabilityChangedNotification:]_block_invoke
- ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.258
- ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.301
- ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.58
- ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.62
- ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.536
- ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.529
- ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.294
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.386
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.386.cold.1
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.388
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.391
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.391.cold.1
- ___68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.36
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.370
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.378
- ___68-[MRNowPlayingController sendCommand:options:appOptions:completion:]_block_invoke.282
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.373
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.373.cold.1
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.375
- ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.405
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.302
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.303
- ___69-[MRQHONowPlayingController _handlePlaybackQueueChangedNotification:]_block_invoke.95
- ___69-[MRQHONowPlayingController _handlePlaybackStateChangedNotification:]_block_invoke.105
- ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.409
- ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.582
- ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.424
- ___73-[MRQHONowPlayingController _handleSupportedCommandsChangedNotification:]_block_invoke.106
- ___74-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke
- ___74-[MRAVEndpoint createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke_2
- ___74-[MRNowPlayingClient enqueueCommand:options:playerPath:commandCompletion:]_block_invoke.302
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.543
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.544
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.548
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.cold.1
- ___76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke
- ___76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke_2
- ___76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke_2.cold.1
- ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.445
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.29
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.33
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.cold.1
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke_2
- ___77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke_3
- ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.473
- ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.295
- ___79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke
- ___79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.62
- ___79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke_2
- ___79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke_2.cold.1
- ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.463
- ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.299
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.42
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.cold.1
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke_2
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke_3
- ___80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke_4
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.203
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.213
- ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.222
- ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.300
- ___81-[MRQHONowPlayingController _loadNowPlayingStateForUID:client:player:completion:]_block_invoke.16
- ___81-[MRQHONowPlayingController _loadNowPlayingStateForUID:client:player:completion:]_block_invoke.16.cold.1
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.242
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.246
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.255
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.262
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.289
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.293
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.329
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.339
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.358
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.247
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.266
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.294
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.304
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.318
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.342
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.365
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.273
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.319
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.345
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.276
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.347
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.277
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.348
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke.104
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_2.108
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_3.109
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_4.119
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_5.121
- ___85-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke
- ___85-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke_2
- ___85-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke_3
- ___85-[MRDistantExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]_block_invoke_4
- ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.195
- ___86+[MRNowPlayingController sendCommand:toDestination:options:appOptions:withCompletion:]_block_invoke.274
- ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.18
- ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.18.cold.1
- ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.18.cold.2
- ___86-[MRQHONowPlayingController _loadNowPlayingStateForEndpoint:client:player:completion:]_block_invoke.18.cold.3
- ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.282
- ___91-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:]_block_invoke
- ___91-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:]_block_invoke_2
- ___91-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:]_block_invoke_3
- ___91-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:]_block_invoke_4
- ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.298
- ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.291
- ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke.157
- ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.287
- ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.124
- ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.128
- ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.104
- ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.96
- ___AVFoundationLibrary_block_invoke
- ___AirPlaySupportLibrary_block_invoke
- ___BiomeLibraryLibrary_block_invoke
- ___BiomeStreamsLibrary_block_invoke
- ___CoreUtilsLibrary_block_invoke
- ___FrontBoardServicesLibrary_block_invoke
- ___IntentsCoreLibrary_block_invoke
- ___IntentsLibrary_block_invoke
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.113
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.142
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.142.cold.1
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.152
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.159
- ___MRAVEndpointModifyOutputDevicesInGroup_block_invoke.95
- ___MRAnalyticsSendEvent_block_invoke.381
- ___MRGroupSessionJoinSessionWithToken_block_invoke.325
- ___MRGroupSessionJoinSessionWithToken_block_invoke.329
- ___MRMediaRemoteGetClientProperties_block_invoke.538
- ___MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.579
- ___MRMediaRemoteGetPlayerProperties_block_invoke.569
- ___MRMediaRemotePlaybackSessionIsMigrationPossible_block_invoke
- ___MRMediaRemoteServiceCreateGroupWithDevicesLeaderOptions_block_invoke
- ___MRMediaRemoteSetPlaybackStateForPlayerWithTimestamp_block_invoke.597
- ___MRServiceClientPlaybackSessionMigrateBeginCallback_block_invoke_2
- ___MRServiceClientPlaybackSessionMigrateEndCallback_block_invoke
- ___MRServiceClientPlaybackSessionMigrateEndCallback_block_invoke_2
- ___MediaExperienceLibrary_block_invoke
- ___MobileKeyBagLibrary_block_invoke
- ___PowerLogLibrary_block_invoke
- ___SpringBoardServicesLibrary_block_invoke
- ___TelephonyUtilitiesLibrary_block_invoke
- ____MRHandlePlaybackQueueRequest_block_invoke.55
- ____MRLoadContentItemAssets_block_invoke
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.426
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.427
- ____MRMediaRemotePlaybackSessionRequest_block_invoke
- ____MRMediaRemotePlaybackSessionRequest_block_invoke.19
- ____MRMediaRemotePlaybackSessionRequest_block_invoke_2
- ____MRMediaRemotePlaybackSessionRequest_block_invoke_2.22
- ____MRMediaRemotePlaybackSessionRequest_block_invoke_2.cold.1
- ____MRMediaRemotePlaybackSessionRequest_block_invoke_3
- ____MRPSMPerformLegacyMigration_block_invoke.112
- ____MRPSMPerformLegacyMigration_block_invoke_2.116
- ____MRPSMPerformLegacyMigration_block_invoke_3.117
- ____MRPSMPerformLegacyMigration_block_invoke_4.118
- ____onClientQueue_MRInvokeClientCallback_block_invoke_3
- ____onQueue_MRHandlePlaybackQueueRequest_block_invoke_2
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
- ___block_descriptor_32_e20_v16?0^{__CFError=}8l
- ___block_descriptor_32_e55_16?0"_MRPlaybackSessionMigrateRequestEventProtobuf"8l
- ___block_descriptor_40_e8_32bs_e39_v24?0"MRPlaybackSession"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e41_B32?0"MRAVConcreteOutputDevice"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e23_v20?0I8^{__CFArray=}12ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e33_v32?0"MRAVOutputDevice"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e20_v16?0^{__CFError=}8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40bs48r_e24_v24?0^v8^{__CFError=}16lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e24_v24?0^v8^{__CFError=}16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e40_v16?0"AVOutputDeviceDiscoverySession"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40bs48r_e8_v12?0I8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e24_v24?0^v8^{__CFError=}16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e46_v32?0"NSArray"8"MRAVEndpoint"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_64_e8_32s40bs48bs56r_e20_v24?0q8"NSError"16ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_e8_32s40s48bs56r_e24_v24?0^v8^{__CFError=}16ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e24_v24?0^v8^{__CFError=}16ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e24_v24?0^v8^{__CFError=}16ls56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e46_v32?0"NSArray"8"MRAVEndpoint"16"NSError"24ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56r_e51_v16?0"AVOutputDeviceGroupMembershipChangeResult"8lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e43_v32?0"MROrigin"8"MROrigin"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e53_v24?0"MRPlaybackSessionMigrateRequest"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v16?0^{__CFError=}8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e39_v24?0"MRPlaybackSession"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e24_v16?0?<v?"NSError">8ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s_e52_v24?0"NSString"8?<v?"MRAVEndpoint""NSError">16ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72bs_e30_v24?0"NSString"8"NSError"16ls32l8s56l8s40l8s48l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72w_e17_v16?0"NSError"8lw72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e20_v20?0I8"NSError"12ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e20_v20?0f8"NSError"12ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e20_v16?0^{__CFError=}8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_92_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.101
- ___block_literal_global.112
- ___block_literal_global.116
- ___block_literal_global.118
- ___block_literal_global.150
- ___block_literal_global.157
- ___block_literal_global.161
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.185
- ___block_literal_global.19
- ___block_literal_global.193
- ___block_literal_global.198
- ___block_literal_global.207
- ___block_literal_global.212
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.228
- ___block_literal_global.231
- ___block_literal_global.24
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.270
- ___block_literal_global.278
- ___block_literal_global.287
- ___block_literal_global.296
- ___block_literal_global.306
- ___block_literal_global.332
- ___block_literal_global.341
- ___block_literal_global.344
- ___block_literal_global.350
- ___block_literal_global.360
- ___block_literal_global.369
- ___block_literal_global.373
- ___block_literal_global.377
- ___block_literal_global.38
- ___block_literal_global.380
- ___block_literal_global.4
- ___block_literal_global.424
- ___block_literal_global.496
- ___block_literal_global.53
- ___block_literal_global.559
- ___block_literal_global.562
- ___block_literal_global.571
- ___block_literal_global.58
- ___block_literal_global.60
- ___block_literal_global.601
- ___block_literal_global.613
- ___block_literal_global.619
- ___block_literal_global.62
- ___block_literal_global.679
- ___block_literal_global.68
- ___block_literal_global.74
- _classAVAudioSession
- _classAVOutputContext
- _classAVOutputDevice
- _classAVOutputDeviceDiscoverySession
- _classAVPairedDevice
- _classAVSystemController
- _classBMPublisherOptions
- _classCURunLoopThread
- _classFBSDisplayLayoutMonitor
- _classFBSDisplayLayoutMonitorConfiguration
- _classINCExtensionConnection
- _classINInteraction
- _classINMediaItem
- _classINPlayMediaIntent
- _classINPlayMediaIntentResponse
- _classINPrivatePlayMediaIntentData
- _classINSchema
- _classTUConversationManager
- _classTUNearbyDeviceHandle
- _classTUNeighborhoodActivityConduit
- _constantValAVAudioSessionCategoryPlayback
- _constantValAVAudioSessionMediaServicesWereLostNotification
- _constantValAVAudioSessionRoutingContextChangeNotification
- _constantValAVOutputContextCanSetVolumeDidChangeNotification
- _constantValAVOutputContextDestinationChangeInitiatedNotification
- _constantValAVOutputContextDestinationChangePreviousDeviceIDsKey
- _constantValAVOutputContextDestinationChangeReasonIdleDisconnect
- _constantValAVOutputContextDestinationChangeReasonKey
- _constantValAVOutputContextOutputDeviceDidChangeNotification
- _constantValAVOutputContextOutputDevicesDidChangeNotification
- _constantValAVOutputContextPredictedOutputDeviceDidChangeNotification
- _constantValAVOutputContextPredictedOutputDevicesDidChangeNotification
- _constantValAVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification
- _constantValAVOutputContextTypeAudio
- _constantValAVOutputContextTypeSharedAudioPresentation
- _constantValAVOutputContextTypeSharedSystemAudio
- _constantValAVOutputContextTypeSharedSystemScreen
- _constantValAVOutputContextVolumeControlTypeDidChangeNotification
- _constantValAVOutputDeviceActivatedClusterMembersRoomIDKey
- _constantValAVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification
- _constantValAVOutputDeviceBatteryLevelCaseKey
- _constantValAVOutputDeviceBatteryLevelLeftKey
- _constantValAVOutputDeviceBatteryLevelRightKey
- _constantValAVOutputDeviceCanMuteDidChangeNotification
- _constantValAVOutputDeviceCanSetVolumeDidChangeNotification
- _constantValAVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification
- _constantValAVOutputDeviceClusterMemberVolumeDidChangeNotification
- _constantValAVOutputDeviceCommunicationChannelControlTypeDirect
- _constantValAVOutputDeviceCommunicationChannelControlTypeRelayed
- _constantValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
- _constantValAVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped
- _constantValAVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired
- _constantValAVOutputDeviceCommunicationChannelOptionControlType
- _constantValAVOutputDeviceCommunicationChannelOptionCorrelationID
- _constantValAVOutputDeviceCommunicationChannelOptionInitiator
- _constantValAVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate
- _constantValAVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification
- _constantValAVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired
- _constantValAVOutputDeviceGroupAddOutputDeviceOptionInitiator
- _constantValAVOutputDeviceGroupRemoveOutputDeviceOptionInitiator
- _constantValAVOutputDeviceGroupVolumeControlTypeDidChangeNotification
- _constantValAVOutputDeviceGroupVolumeDidChangeNotification
- _constantValAVOutputDeviceMutedDidChangeNotification
- _constantValAVOutputDeviceVolumeControlTypeDidChangeNotification
- _constantValAVOutputDeviceVolumeDidChangeNotification
- _constantValAVSystemController_CanBeNowPlayingAppAttribute
- _constantValAVSystemController_ServerConnectionDiedNotification
- _constantValAVSystemController_SubscribeToNotificationsAttribute
- _constantValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Atmos
- _constantValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Multichannel
- _getAVAudioSessionCategoryPlayback
- _getAVAudioSessionClass
- _getAVAudioSessionMediaServicesWereLostNotification
- _getAVAudioSessionRoutingContextChangeNotification
- _getAVOutputContextCanSetVolumeDidChangeNotification
- _getAVOutputContextClass
- _getAVOutputContextDestinationChangeInitiatedNotification
- _getAVOutputContextDestinationChangePreviousDeviceIDsKey
- _getAVOutputContextDestinationChangeReasonIdleDisconnect
- _getAVOutputContextDestinationChangeReasonKey
- _getAVOutputContextOutputDeviceDidChangeNotification
- _getAVOutputContextOutputDevicesDidChangeNotification
- _getAVOutputContextPredictedOutputDeviceDidChangeNotification
- _getAVOutputContextPredictedOutputDevicesDidChangeNotification
- _getAVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification
- _getAVOutputContextTypeAudio
- _getAVOutputContextTypeSharedAudioPresentation
- _getAVOutputContextTypeSharedSystemAudio
- _getAVOutputContextTypeSharedSystemScreen
- _getAVOutputContextVolumeControlTypeDidChangeNotification
- _getAVOutputDeviceActivatedClusterMembersRoomIDKey
- _getAVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification
- _getAVOutputDeviceCanMuteDidChangeNotification
- _getAVOutputDeviceCanSetVolumeDidChangeNotification
- _getAVOutputDeviceClass
- _getAVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification
- _getAVOutputDeviceClusterMemberVolumeDidChangeNotification
- _getAVOutputDeviceCommunicationChannelControlTypeDirect
- _getAVOutputDeviceCommunicationChannelControlTypeRelayed
- _getAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
- _getAVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped
- _getAVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired
- _getAVOutputDeviceCommunicationChannelOptionControlType
- _getAVOutputDeviceCommunicationChannelOptionCorrelationID
- _getAVOutputDeviceCommunicationChannelOptionInitiator
- _getAVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate
- _getAVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification
- _getAVOutputDeviceDiscoverySessionClass
- _getAVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired
- _getAVOutputDeviceGroupAddOutputDeviceOptionInitiator
- _getAVOutputDeviceGroupRemoveOutputDeviceOptionInitiator
- _getAVOutputDeviceGroupVolumeControlTypeDidChangeNotification
- _getAVOutputDeviceGroupVolumeDidChangeNotification
- _getAVOutputDeviceMutedDidChangeNotification
- _getAVOutputDeviceVolumeControlTypeDidChangeNotification
- _getAVOutputDeviceVolumeDidChangeNotification
- _getAVPairedDeviceClass
- _getCURunLoopThreadClass
- _getFBSDisplayLayoutMonitorClass
- _getFBSDisplayLayoutMonitorConfigurationClass
- _getINCExtensionConnectionClass
- _getINMediaItemClass
- _getINPlayMediaIntentResponseClass
- _getINPrivatePlayMediaIntentDataClass
- _getINSchemaClass
- _getTUConversationManagerClass
- _getTUNeighborhoodActivityConduitClass
- _getkMXSession_SourceFormatInfoKey_BestAvailableContentType_Atmos
- _getkMXSession_SourceFormatInfoKey_BestAvailableContentType_Multichannel
- _initAPSCopyDefaultGroupUUID
- _initAPSCopyDefaultGroupUUID.cold.1
- _initAPSParseGroupID
- _initAPSParseGroupID.cold.1
- _initAVAudioSession
- _initAVAudioSession.cold.1
- _initAVOutputContext
- _initAVOutputContext.cold.1
- _initAVOutputDevice
- _initAVOutputDevice.cold.1
- _initAVOutputDeviceDiscoverySession
- _initAVOutputDeviceDiscoverySession.cold.1
- _initAVPairedDevice
- _initAVPairedDevice.cold.1
- _initAVSystemController
- _initAVSystemController.cold.1
- _initAudioFormatGetProperty
- _initAudioFormatGetProperty.cold.1
- _initBMPublisherOptions
- _initBMPublisherOptions.cold.1
- _initBiomeLibrary
- _initBiomeLibrary.cold.1
- _initCURunLoopThread
- _initCURunLoopThread.cold.1
- _initFBSDisplayLayoutMonitor
- _initFBSDisplayLayoutMonitor.cold.1
- _initFBSDisplayLayoutMonitorConfiguration
- _initFBSDisplayLayoutMonitorConfiguration.cold.1
- _initINCExtensionConnection
- _initINCExtensionConnection.cold.1
- _initINInteraction
- _initINInteraction.cold.1
- _initINMediaItem
- _initINMediaItem.cold.1
- _initINPlayMediaIntent
- _initINPlayMediaIntent.cold.1
- _initINPlayMediaIntentResponse
- _initINPlayMediaIntentResponse.cold.1
- _initINPrivatePlayMediaIntentData
- _initINPrivatePlayMediaIntentData.cold.1
- _initINSchema
- _initINSchema.cold.1
- _initMKBDeviceUnlockedSinceBoot
- _initMKBDeviceUnlockedSinceBoot.cold.1
- _initPLLogRegisteredEvent
- _initPLLogRegisteredEvent.cold.1
- _initSBSIsSystemApertureAvailable
- _initSBSIsSystemApertureAvailable.cold.1
- _initTUConversationManager
- _initTUConversationManager.cold.1
- _initTUNearbyDeviceHandle
- _initTUNearbyDeviceHandle.cold.1
- _initTUNeighborhoodActivityConduit
- _initTUNeighborhoodActivityConduit.cold.1
- _initValAVAudioSessionCategoryPlayback
- _initValAVAudioSessionCategoryPlayback.cold.1
- _initValAVAudioSessionMediaServicesWereLostNotification
- _initValAVAudioSessionMediaServicesWereLostNotification.cold.1
- _initValAVAudioSessionRoutingContextChangeNotification
- _initValAVAudioSessionRoutingContextChangeNotification.cold.1
- _initValAVOutputContextCanSetVolumeDidChangeNotification
- _initValAVOutputContextCanSetVolumeDidChangeNotification.cold.1
- _initValAVOutputContextDestinationChangeInitiatedNotification
- _initValAVOutputContextDestinationChangeInitiatedNotification.cold.1
- _initValAVOutputContextDestinationChangePreviousDeviceIDsKey
- _initValAVOutputContextDestinationChangePreviousDeviceIDsKey.cold.1
- _initValAVOutputContextDestinationChangeReasonIdleDisconnect
- _initValAVOutputContextDestinationChangeReasonIdleDisconnect.cold.1
- _initValAVOutputContextDestinationChangeReasonKey
- _initValAVOutputContextDestinationChangeReasonKey.cold.1
- _initValAVOutputContextOutputDeviceDidChangeNotification
- _initValAVOutputContextOutputDeviceDidChangeNotification.cold.1
- _initValAVOutputContextOutputDevicesDidChangeNotification
- _initValAVOutputContextOutputDevicesDidChangeNotification.cold.1
- _initValAVOutputContextPredictedOutputDeviceDidChangeNotification
- _initValAVOutputContextPredictedOutputDeviceDidChangeNotification.cold.1
- _initValAVOutputContextPredictedOutputDevicesDidChangeNotification
- _initValAVOutputContextPredictedOutputDevicesDidChangeNotification.cold.1
- _initValAVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification
- _initValAVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification.cold.1
- _initValAVOutputContextTypeAudio
- _initValAVOutputContextTypeAudio.cold.1
- _initValAVOutputContextTypeSharedAudioPresentation
- _initValAVOutputContextTypeSharedAudioPresentation.cold.1
- _initValAVOutputContextTypeSharedSystemAudio
- _initValAVOutputContextTypeSharedSystemAudio.cold.1
- _initValAVOutputContextTypeSharedSystemScreen
- _initValAVOutputContextTypeSharedSystemScreen.cold.1
- _initValAVOutputContextVolumeControlTypeDidChangeNotification
- _initValAVOutputContextVolumeControlTypeDidChangeNotification.cold.1
- _initValAVOutputDeviceActivatedClusterMembersRoomIDKey
- _initValAVOutputDeviceActivatedClusterMembersRoomIDKey.cold.1
- _initValAVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification
- _initValAVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification.cold.1
- _initValAVOutputDeviceBatteryLevelCaseKey
- _initValAVOutputDeviceBatteryLevelCaseKey.cold.1
- _initValAVOutputDeviceBatteryLevelLeftKey
- _initValAVOutputDeviceBatteryLevelLeftKey.cold.1
- _initValAVOutputDeviceBatteryLevelRightKey
- _initValAVOutputDeviceBatteryLevelRightKey.cold.1
- _initValAVOutputDeviceCanMuteDidChangeNotification
- _initValAVOutputDeviceCanMuteDidChangeNotification.cold.1
- _initValAVOutputDeviceCanSetVolumeDidChangeNotification
- _initValAVOutputDeviceCanSetVolumeDidChangeNotification.cold.1
- _initValAVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification
- _initValAVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification.cold.1
- _initValAVOutputDeviceClusterMemberVolumeDidChangeNotification
- _initValAVOutputDeviceClusterMemberVolumeDidChangeNotification.cold.1
- _initValAVOutputDeviceCommunicationChannelControlTypeDirect
- _initValAVOutputDeviceCommunicationChannelControlTypeDirect.cold.1
- _initValAVOutputDeviceCommunicationChannelControlTypeRelayed
- _initValAVOutputDeviceCommunicationChannelControlTypeRelayed.cold.1
- _initValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
- _initValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote.cold.1
- _initValAVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped
- _initValAVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped.cold.1
- _initValAVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired
- _initValAVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired.cold.1
- _initValAVOutputDeviceCommunicationChannelOptionControlType
- _initValAVOutputDeviceCommunicationChannelOptionControlType.cold.1
- _initValAVOutputDeviceCommunicationChannelOptionCorrelationID
- _initValAVOutputDeviceCommunicationChannelOptionCorrelationID.cold.1
- _initValAVOutputDeviceCommunicationChannelOptionInitiator
- _initValAVOutputDeviceCommunicationChannelOptionInitiator.cold.1
- _initValAVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate
- _initValAVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate.cold.1
- _initValAVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification
- _initValAVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification.cold.1
- _initValAVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired
- _initValAVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired.cold.1
- _initValAVOutputDeviceGroupAddOutputDeviceOptionInitiator
- _initValAVOutputDeviceGroupAddOutputDeviceOptionInitiator.cold.1
- _initValAVOutputDeviceGroupRemoveOutputDeviceOptionInitiator
- _initValAVOutputDeviceGroupRemoveOutputDeviceOptionInitiator.cold.1
- _initValAVOutputDeviceGroupVolumeControlTypeDidChangeNotification
- _initValAVOutputDeviceGroupVolumeControlTypeDidChangeNotification.cold.1
- _initValAVOutputDeviceGroupVolumeDidChangeNotification
- _initValAVOutputDeviceGroupVolumeDidChangeNotification.cold.1
- _initValAVOutputDeviceMutedDidChangeNotification
- _initValAVOutputDeviceMutedDidChangeNotification.cold.1
- _initValAVOutputDeviceVolumeControlTypeDidChangeNotification
- _initValAVOutputDeviceVolumeControlTypeDidChangeNotification.cold.1
- _initValAVOutputDeviceVolumeDidChangeNotification
- _initValAVOutputDeviceVolumeDidChangeNotification.cold.1
- _initValAVSystemController_CanBeNowPlayingAppAttribute
- _initValAVSystemController_CanBeNowPlayingAppAttribute.cold.1
- _initValAVSystemController_ServerConnectionDiedNotification
- _initValAVSystemController_ServerConnectionDiedNotification.cold.1
- _initValAVSystemController_SubscribeToNotificationsAttribute
- _initValAVSystemController_SubscribeToNotificationsAttribute.cold.1
- _initValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Atmos
- _initValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Atmos.cold.1
- _initValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Multichannel
- _initValkMXSession_SourceFormatInfoKey_BestAvailableContentType_Multichannel.cold.1
- _kMXSession_SourceFormatInfoKey_BestAvailableContentType_AtmosFunction
- _kMXSession_SourceFormatInfoKey_BestAvailableContentType_MultichannelFunction
- _objc_msgSend$_computeActiveRouteIDsFromEndpoint:
- _objc_msgSend$_shouldAddLocalEndpoint
- _objc_msgSend$activeEndpoint
- _objc_msgSend$addOutputDevice:withOptions:completionHandler:
- _objc_msgSend$cancellationReason
- _objc_msgSend$createEndpointWithOutputDeviceUIDs:options:queue:completion:
- _objc_msgSend$createHostedEndpointWithOutputDeviceUIDs:completion:
- _objc_msgSend$createHostedEndpointWithOutputDeviceUIDs:queue:completion:
- _objc_msgSend$discoverySessionWithEndpointFeatures:enableThrottling:
- _objc_msgSend$enableThrottling
- _objc_msgSend$endEvent:
- _objc_msgSend$endEvent:withError:
- _objc_msgSend$errorWithChangeResult:outputDevice:
- _objc_msgSend$initWithOutputDeviceUIDs:outputDeviceGroupID:features:
- _objc_msgSend$initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:
- _objc_msgSend$initWithPlaybackSession:
- _objc_msgSend$initWithRequest:error:playerPath:
- _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
- _objc_msgSend$isJ327Device
- _objc_msgSend$lastPlayingDate
- _objc_msgSend$objectsAtIndexes:
- _objc_msgSend$playbackSessionMigrateEndCallback
- _objc_msgSend$populatesExternalDevice
- _objc_msgSend$removeOutputDevice:withOptions:completionHandler:
- _objc_msgSend$report
- _objc_msgSend$setEnableThrottling:
- _objc_msgSend$setPopulatesExternalDevice:
- _objc_msgSend$setWantsEndpointChangeNotifications:
- _objc_msgSend$startEvent:
- _objc_msgSend$volumeForOutputDevice:error:
- _softLinkAPSCopyDefaultGroupUUID
- _softLinkAPSParseGroupID
- _softLinkAudioFormatGetProperty
- _softLinkBiomeLibrary
- _softLinkMKBDeviceUnlockedSinceBoot
- _softLinkPLLogRegisteredEvent
- _softLinkSBSIsSystemApertureAvailable
CStrings:
+ "\x02%"
+ "\x02% "
+ "\x100 "
+ "\x160 "
+ "    playerPath = %@\n    player = %@\n    supportedCommands = %@\n    nowPlayingInfo = %@\n    nowPlayingArtwork = %@\n    nowPlayingAnimatedArtwork = %@\n    playbackState = %@\n    playbackStateDate= %@\n    playbackQueue = %@\n    capabilities = %ld\n    triggerInvalidation = %@\n    invalidatationTimestamp = %lf\n    cachedContentItemUpdates = %@\n    pictureInPictureEnabled = %@\n    activeRequestDate = %@\n    canBeNowPlaying = %@\n    canBeNowPlayingTimestamp = %@\n    homeUserIdentifiers = %@"
+ " (%d)"
+ " cached"
+ " code=%@"
+ " customData.length=%ld"
+ " customDataType=%@"
+ " dialog=%@"
+ " error=%@"
+ " infra"
+ " type=Code"
+ " type=Custom"
+ " type=Dialog"
+ " type=Error"
+ " type=Unknown"
+ "%"
+ "%@          %@%@          %@"
+ "%@ (%@)"
+ "%@:%@:%@"
+ "%@=%@"
+ "%@MigrationFailure"
+ "%s"
+ "%{public, signpost.description:begin_time}llu,name=%{public}@"
+ "%{public, signpost.description:end_time}llu,name=%{public}@"
+ "(Proxy)"
+ "-[MRAVOutputDevice discoveredDeviceIsPlaying]"
+ "-[MRAVOutputDevice wasDiscoveredInCache]"
+ "-[MRExternalDevice createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:]"
+ "-[MRExternalDevice externalOutputContext]"
+ "-[MRExternalDevice lastConnectionError]"
+ "-[MRExternalDevice requestMicrophoneConnectionWithDetails:queue:completion:]"
+ "/AAPF[%ld]"
+ "/AAU[%ld]"
+ "76,8195"
+ "76,8197"
+ "76,8198"
+ "76,8201"
+ "76,8203"
+ "76,8204"
+ "76,8205"
+ "76,8208"
+ "76,8209"
+ "76,8210"
+ "76,8214"
+ "76,8221"
+ "<%@: %p"
+ "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@%@%@>"
+ "@\"MRActiveRoutesObserverOutputDeviceRemovedSnapshot\""
+ "@\"MRPlaybackSessionMigrateRequest\""
+ "@\"NSSecurityScopedURLWrapper\""
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@\"_MRMicrophoneConnectionRequestMessageProtobuf\""
+ "@\"_MRMicrophoneConnectionResponseMessageProtobuf\""
+ "@\"_MRSendCommandResultStatusProtobuf\""
+ "@32@0:8{CGSize=dd}16"
+ "@44@0:8@16@24f32I36B40"
+ "@60@0:8@16@24@32@40B48@52"
+ "AVDiscoverySession"
+ "AddOutputDevices"
+ "Aggregate"
+ "AirPlaySessionController"
+ "Ambient"
+ "Apply"
+ "Attempt to add event inputs after finalized report"
+ "Attempt to add event outputs after finalized report"
+ "Attempt to end event after finalized report"
+ "Attempt to finalize more than once"
+ "Attempt to start event after finalized report"
+ "B16@?0@\"MRAVConcreteOutputDevice\"8"
+ "B16@?0@\"TUNearbyDeviceHandle\"8"
+ "B16@?0@\"_MRAVOutputDeviceDescriptorProtobuf\"8"
+ "BOOL soft_SBSIsSystemApertureAvailable(void)"
+ "BlessApp"
+ "Callback does not exist for: %@"
+ "Cannot obtain hash from unknown hasher algorithm"
+ "CarPlayBannersEnabled"
+ "Class getAVSystemControllerClass(void)_block_invoke"
+ "Class getBMPublisherOptionsClass(void)_block_invoke"
+ "Class getCURunLoopThreadClass(void)_block_invoke"
+ "Class getFBSDisplayLayoutMonitorClass(void)_block_invoke"
+ "Class getFBSDisplayLayoutMonitorConfigurationClass(void)_block_invoke"
+ "Class getINCExtensionConnectionClass(void)_block_invoke"
+ "Class getINInteractionClass(void)_block_invoke"
+ "Class getINMediaItemClass(void)_block_invoke"
+ "Class getINPlayMediaIntentClass(void)_block_invoke"
+ "Class getINPlayMediaIntentResponseClass(void)_block_invoke"
+ "Class getINPrivatePlayMediaIntentDataClass(void)_block_invoke"
+ "Class getINSchemaClass(void)_block_invoke"
+ "Class getTUConversationManagerClass(void)_block_invoke"
+ "Class getTUNearbyDeviceHandleClass(void)_block_invoke"
+ "Class getTUNeighborhoodActivityConduitClass(void)_block_invoke"
+ "ClearSourceQueue"
+ "Connect"
+ "ContinuitySing"
+ "CoordinatePlayback"
+ "Could not build animated artwork from protobuf %@ in content item %@"
+ "CreateSecondaryEndpoint"
+ "Destination"
+ "DetermineRecipe"
+ "DiscoverDestinationEndpoint"
+ "Endpoint.createHostedEndpointWithOutputDeviceUIDs.endpoint"
+ "Endpoint.createHostedEndpointWithOutputDeviceUIDs.groupUID"
+ "EnhanceDialogue"
+ "Epilogue"
+ "Error archiving MRAnimatedArtwork data into protobuf: %@"
+ "Error initializing MRAnimatedArtwork from protobuf: %@"
+ "Error while attempting to decode JSON migrationReport: %@"
+ "ExpanseMigration"
+ "FAULT: No type for animated artwork preview frame protobuf %@ in content item %@"
+ "FAULT: No type for animated artwork protobuf %@ in content item %@"
+ "Finalize"
+ "GetPlaybackQueue"
+ "GetPlaybackSession"
+ "GetPlaybackState"
+ "GroupSessionJoinRequestAssertionDuration"
+ "HH:mm:ss.SSSXX"
+ "Hijacked"
+ "I28@0:8@16i24"
+ "InApp"
+ "InterruptBestStreamIfNecessary"
+ "InvalidRequest"
+ "LaunchApp"
+ "Legacy"
+ "MRAVEndpoint.createEndpointWithOutputDeviceUIDs"
+ "MRAVEndpointCarPlayVideoIsActiveDidChangeNotification"
+ "MRAVEndpointCarPlayVideoIsAllowedDidChangeNotification"
+ "MRAVLightweightReconnaissanceSession.searchEndpointsForMyGroupLeader-%@"
+ "MRAVLightweightReconnaissanceSession.searchForOutputDevicesWithCategories"
+ "MRAVLightweightReconnaissanceSession.searchOutputDevices-%@"
+ "MRAVRoutingDiscoverySessionWrapperAdditions"
+ "MRActiveRoutesObserverOutputDeviceRemovedSnapshot"
+ "MRAnimatedArtwork"
+ "MRContentItemAnimatedArtworkFormatSquare"
+ "MRContentItemAnimatedArtworkFormatTall"
+ "MRExpanseManager.m"
+ "MRFrontBoardServicesImports.h"
+ "MRIDSCompanionConnection.m"
+ "MRLocalVolumeHUDPresentationRequest"
+ "MRMediaRemoteUnregisterForNowPlayingNotifications"
+ "MRMediaSuggestionRequestResponse.m"
+ "MRMicrophoneConnectionRequestMessage"
+ "MRMicrophoneConnectionResponseMessage"
+ "MRNowPlayingAnimatedArtwork"
+ "MRNowPlayingAudioFormatContentInfo.m"
+ "MRPlaybackSessionMigrateRequest.m"
+ "MRPowerLogger.m"
+ "MRProtocolMessageLoggerAdditions"
+ "MRSiriIntentImports.h"
+ "MRUIControllers.m"
+ "MRVolumeHUDPresentationRequest"
+ "MRVolumeUIControllable"
+ "MRVolumeUIServerXPCProtocol"
+ "MicrophoneConnectionRequest"
+ "MicrophoneConnectionResponse"
+ "MicrophoneConnectionTimeout"
+ "MigrateProximity"
+ "MirrorModule"
+ "MirroringView"
+ "ModifyTopology"
+ "MultipleRequestsNotSupported"
+ "NSString *getAVSystemController_CanBeNowPlayingAppAttribute(void)"
+ "NSString *getAVSystemController_ServerConnectionDiedNotification(void)"
+ "NSString *getAVSystemController_SubscribeToNotificationsAttribute(void)"
+ "NSString *getkMXSession_SourceFormatInfoKey_BestAvailableContentType_Atmos(void)"
+ "NSString *getkMXSession_SourceFormatInfoKey_BestAvailableContentType_Multichannel(void)"
+ "NSUInteger _MSVHashGetHash(MSVHash)"
+ "NeedsGuestPairing"
+ "No CarPlay output device is available"
+ "NoSuitableDeviceAvailable"
+ "NotPossible"
+ "OSStatus soft_APSCopyDefaultGroupUUID(CFStringRef *)"
+ "OSStatus soft_APSParseGroupID(CFStringRef, CFStringRef *, CFStringRef *, CFStringRef *, CFStringRef *)"
+ "OneShot"
+ "Operation not implemented in %@"
+ "OutputContext.supportsVolume=YES with only localDevice"
+ "OutputDevice"
+ "Partially resolved player path missing bundleID: destinationPlayerPath=%@"
+ "Partially resolved player path missing origin: destinationPlayerPath=%@"
+ "PlayItemInQueue"
+ "PlayerCommandFailed (The app itself reported failure)"
+ "Preamble"
+ "Prepare"
+ "QHO"
+ "ReceiverDeviceIsPlaying"
+ "Receptionist"
+ "ResetOutputContext"
+ "ResolveDestination"
+ "ResolveSource"
+ "RouteToDevice"
+ "Seek"
+ "SendPause"
+ "SendPlaybackSession"
+ "SetActiveItem"
+ "SetOutputDevice"
+ "SetOutputDevices"
+ "SetRate"
+ "SetVolumeFailed"
+ "Source"
+ "StringAsRecipeType:"
+ "StringAsResult:"
+ "StringAsRole:"
+ "Studio Display Audio Control"
+ "SystemEndpointHelper"
+ "SystemGroupSession"
+ "T@\"MRAVDistantEndpoint\",&,N,V_activeEndpointSnapshot"
+ "T@\"MRAVDistantEndpoint\",&,N,V_endpoint"
+ "T@\"MRAVDistantOutputDevice\",R,N"
+ "T@\"MRAVLocalEndpoint\",R,N"
+ "T@\"MRActiveRoutesObserverOutputDeviceRemovedSnapshot\",&,N,V_deviceRemovedSnapshot"
+ "T@\"MRExternalOutputContextDataSource\",R,D,N"
+ "T@\"MRExternalOutputContextDataSource\",R,N"
+ "T@\"MRPlaybackSessionMigrateRequest\",&,N,V_request"
+ "T@\"MRSendCommandResultStatus\",&,N"
+ "T@\"MRSendCommandResultStatus\",R,N"
+ "T@\"MSVMultiCallback\",R,N,V_animatedArtworkCallbacks"
+ "T@\"MSVTimer\",&,N,V_deviceRemovedWaitIntervalTimer"
+ "T@\"NSArray\",&,N,V_availableAnimatedArtworkFormats"
+ "T@\"NSArray\",C,N,V_requestedAnimatedArtworkAssetURLFormats"
+ "T@\"NSArray\",C,N,V_requestedAnimatedArtworkPreviewFrameFormats"
+ "T@\"NSArray\",R,N,V_allowList"
+ "T@\"NSArray\",R,N,V_denyList"
+ "T@\"NSData\",&,N,V_assetFileURLData"
+ "T@\"NSDictionary\",&,N,V_animatedArtworkPreviewFrames"
+ "T@\"NSDictionary\",&,N,V_animatedArtworks"
+ "T@\"NSMutableArray\",&,N,V_animatedArtworkPreviewFrames"
+ "T@\"NSMutableArray\",&,N,V_animatedArtworks"
+ "T@\"NSMutableArray\",&,N,V_availableAnimatedArtworkFormats"
+ "T@\"NSMutableArray\",&,N,V_requestedAnimatedArtworkAssetURLFormats"
+ "T@\"NSMutableArray\",&,N,V_requestedAnimatedArtworkPreviewFrameFormats"
+ "T@\"NSString\",&,N,V_debugMessage"
+ "T@\"NSString\",&,N,V_operationID"
+ "T@\"NSString\",&,N,V_surface"
+ "T@\"NSString\",C,N,V_surface"
+ "T@\"NSString\",R,C,N,V_operationID"
+ "T@\"NSString\",R,D,N"
+ "T@\"NSURL\",R,N"
+ "T@\"NSUserDefaults\",R,N,V_userDefaults"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_input"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_output"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_userInfo"
+ "T@\"_MRMicrophoneConnectionRequestMessageProtobuf\",&,N,V_microphoneConnectionRequestMessage"
+ "T@\"_MRMicrophoneConnectionResponseMessageProtobuf\",&,N,V_microphoneConnectionResponseMessage"
+ "T@\"_MRSendCommandResultStatusProtobuf\",&,N,V_setPlaybackSessionCommandStatus"
+ "T@?,C,N,V_repeatModeDidChange"
+ "T@?,C,N,V_shuffleModeDidChange"
+ "TB,N,V_cachedDiscoveryEnabled"
+ "TB,N,V_deviceIsPlaying"
+ "TB,N,V_enhanceDialogueActive"
+ "TB,N,V_hasParentGroupSupportsGroupCohesion"
+ "TB,N,V_parentGroupSupportsGroupCohesion"
+ "TB,N,V_shouldWaitForUpdatedOutputDevices"
+ "TB,N,V_wasDiscoveredInCache"
+ "TB,R,D,N,GisVolumeMuted"
+ "TI,N,V_identifier"
+ "Td,N,V_deviceRemovedWaitInterval"
+ "Tf,R,D,N"
+ "Ti,N"
+ "Ti,N,V_recipeType"
+ "Ti,N,V_result"
+ "Ti,N,V_role"
+ "Ti,N,V_transitionStyle"
+ "ToggleTransitions"
+ "UIDs=(%@), bundleID=%@"
+ "Unable to find class %s"
+ "Unexpected groupUID in formed endpoint. Expected: %@, got: %@"
+ "VerifyPlayer"
+ "VolumeCC"
+ "VolumeLockScreen"
+ "VolumeSlider"
+ "WHAInstantDiscovery_Caching"
+ "[%@<%@:%p>] "
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot Added: %@"
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot: ActiveRouteIDs update ignored due to snapshot %lf seconds ago"
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot: removed due to airPlayActive + !parentGroupSupportsGroupCohesion"
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot: removed due to airPlayActive + parentGroupSupportsGroupCohesion + leaderDeviceInfo"
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot: removed due to deviceRemovedWaitInterval"
+ "[MRActiveRoutesObserver] DeviceRemovedSnapshot: removed due to new activeEndpoint"
+ "[MRActiveRoutesObserver] Snapshot Added %@ -> %@"
+ "[MRActiveRoutesObserver] Snapshot Init: %@"
+ "[MRActiveRoutesObserver] Snapshot Removed %@ -> %@"
+ "[MRGroupSession] [tokenForJoinURLString] URL doesn't have group session host domain: %{public}@"
+ "[MRNowPlayingPlayerClientRequests] %{public}@ UpdatingCache: clearing animated artworks for %@"
+ "[MRPlaybackQueueServiceClient] Responding to playbackQueueRequest %{public}@ for path %{public}@ with error %{public}@"
+ "[MRQHONPC] %{public}@ Unable to discover endpoint."
+ "[MRQHONPC] <%{public}@ : %p> processing PlaybackQueueDidChangeNotification."
+ "[MRQHONPC] <%{public}@> Artwork cache hit for content item %{public}@, artwork %{public}@."
+ "[MRQHONPC] <%{public}@> Begin loading data."
+ "[MRQHONPC] <%{public}@> Begin loading updates."
+ "[MRQHONPC] <%{public}@> Begin resolving endpoint."
+ "[MRQHONPC] <%{public}@> Begin resolving player path for endpoint %{public}@."
+ "[MRQHONPC] <%{public}@> Deallocating."
+ "[MRQHONPC] <%{public}@> End loading data. Response: %@."
+ "[MRQHONPC] <%{public}@> End loading updates."
+ "[MRQHONPC] <%{public}@> Error creating player path %{public}@."
+ "[MRQHONPC] <%{public}@> Error fetching artwork for content item %{public}@. Error: %{public}@."
+ "[MRQHONPC] <%{public}@> Error loading data %{public}@."
+ "[MRQHONPC] <%{public}@> Error resolving player path %{public}@."
+ "[MRQHONPC] <%{public}@> Player path is not resolved. There may be no now playing application."
+ "[MRQHONPC] <%{public}@> Resolved to Endpoint: %{public}@."
+ "[MRQHONPC] <%{public}@> Resolved to player path: %@."
+ "[MRQHONPC] <%{public}@> _requestAndUpdateArtworkForContentItems because %{public}@."
+ "[MRQHONPC] <%{public}@> deferring PlaybackQueueContentItemsChangedNotification for content items %{public}@ because we are requesting a new playback queue."
+ "[MRQHONPC] <%{public}@> downloading artwork for content item %{public}@, artwork %{public}@."
+ "[MRQHONPC] <%{public}@> ignoring PlaybackQueueContentItemsArtworkChangedNotification for content items %{public}@ "
+ "[MRQHONPC] <%{public}@> processing PlaybackQueueContentItemsArtworkChangedNotification for content items %{public}@."
+ "[MRQHONPC] <%{public}@> processing PlaybackQueueContentItemsChangedNotification for content items %{public}@."
+ "[MRQHONPC] <%{public}@> processing PlaybackStateDidChangeNotification with new PlaybackState %{public}@."
+ "[MRQHONPC] <%{public}@> processing SupportedCommandsDidChangeNotification."
+ "[MRQHONPC] <%{public}@> reloading due to ASE change."
+ "[MRQHONPC] <%{public}@> reloading due to change in endpoint. Current endpoint: %{public}@. New endpoint: %{public}@."
+ "[MRQHONPC] <%{public}@> reloading due to player path invalidation."
+ "[MRQHONPC] <%{public}@> requesting artwork for content item %{public}@, artwork %{public}@."
+ "[MRQHONPC] <%{public}@> updated artwork cache with %{public}@."
+ "[MRQHONPC] <%{public}@> updated artwork for content items %{public}@."
+ "[MRQHONPC] <%{public}@> updated content items %{public}@."
+ "[MRQHONPC] Failed to retrieve player last playing date with error: %{public}@"
+ "[NowPlayingInfo] Setting nowPlayingInfo artwork (id: %{public}@): %@"
+ "[ProximityProvider] Adding device %{public}@."
+ "[ProximityProvider] Begin providing for device %{public}@ (%@)."
+ "[ProximityProvider] Begin providing for device %{public}@, but device is not prepared, so must defer initial provide."
+ "[ProximityProvider] Cannot provide because no result has been calculated yet for device %{public}@ (%@)."
+ "[ProximityProvider] Device %{public}@ prepare failed with error %@."
+ "[ProximityProvider] End providing for device %{public}@ (%@)."
+ "[ProximityProvider] Failed to persist artwork data for device %{public}@. Error: %@."
+ "[ProximityProvider] No result for device %{public}@, error: %{public}@"
+ "[ProximityProvider] Removing device %{public}@ (%@)."
+ "[ProximityProvider] Result for device %{public}@ (%@):\n%@"
+ "[ProximityProvider] migrateForDevice<%{public}@> beginning for device %{public}@"
+ "[ProximityProvider] migrateForDevice<%{public}@> completed for device %{public}@ with error: %{public}@"
+ "[QHO:%@] event with id=%{sonic:fourCC}d count not be ended [not found]"
+ "[_MRValueProtobuf] _MRProtoUtilsProtoValueFromPlistType: plistType=%@ is not a plist type"
+ "_MRAnimatedArtworkProtobuf"
+ "_MRMicrophoneConnectionRequestMessageProtobuf"
+ "_MRMicrophoneConnectionResponseMessageProtobuf"
+ "_activeEndpointSnapshot"
+ "_allowList"
+ "_animatedArtworkCallbacks"
+ "_animatedArtworkPreviewFrames"
+ "_animatedArtworkToken"
+ "_animatedArtworks"
+ "_artworkAssetFileURLRequestHandler"
+ "_assetFileURLData"
+ "_assetFileURLWrapper"
+ "_availableAnimatedArtworkFormats"
+ "_cachedDiscoveryEnabled"
+ "_computeActiveRouteIDsFromEndpoint:localDeviceInfo:"
+ "_debugMessage"
+ "_denyList"
+ "_deviceIsPlaying"
+ "_deviceRemovedSnapshot"
+ "_deviceRemovedWaitInterval"
+ "_deviceRemovedWaitIntervalTimer"
+ "_enhanceDialogueActive"
+ "_extendedSupportedRates"
+ "_finalized"
+ "_groupSessionComponentsWithScheme:host:"
+ "_handleActiveSystemEndpointDidAddOutputDevice:"
+ "_handleActiveSystemEndpointDidRemoveOutputDevice:"
+ "_hasParentGroupSupportsGroupCohesion"
+ "_input"
+ "_lastConnectionError"
+ "_loadDefaults"
+ "_microphoneConnectionRequestMessage"
+ "_microphoneConnectionResponseMessage"
+ "_mostRelevantItem"
+ "_nowPlayingAnimatedArtwork"
+ "_nowPlayingArtworkID"
+ "_operationID"
+ "_output"
+ "_parentGroupSupportsGroupCohesion"
+ "_playbackSessionMigrateFinalizeCallback"
+ "_previewFrameDataRequestHandler"
+ "_recipeType"
+ "_repeatModeDidChange"
+ "_requestedAnimatedArtworkAssetURLFormats"
+ "_requestedAnimatedArtworkPreviewFrameFormats"
+ "_setError"
+ "_setPlaybackSessionCommandStatus"
+ "_shouldLogChanges"
+ "_shouldWaitForUpdatedOutputDevices"
+ "_shuffleModeDidChange"
+ "_surface"
+ "_transitionStyle"
+ "_wasDiscoveredInCache"
+ "activeEndpointSnapshot"
+ "addAnimatedArtworkPreviewFrames:"
+ "addAnimatedArtworks:"
+ "addAvailableAnimatedArtworkFormats:"
+ "addEventInput:withKey:toEventID:"
+ "addEventOutput:withKey:toEventID:"
+ "addExtendedSupportedRate:"
+ "addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:"
+ "addRequestedAnimatedArtworkAssetURLFormats:"
+ "addRequestedAnimatedArtworkPreviewFrameFormats:"
+ "alignments"
+ "allowList"
+ "animated artwork"
+ "animatedArtworkCallbacks"
+ "animatedArtworkItemIdentifierFromSourceIdentifier:"
+ "animatedArtworkPreviewFrames"
+ "animatedArtworkPreviewFramesAtIndex:"
+ "animatedArtworkPreviewFramesCount"
+ "animatedArtworkPreviewFramesType"
+ "animatedArtwork_%@"
+ "animatedArtworks"
+ "animatedArtworksAtIndex:"
+ "animatedArtworksCount"
+ "animatedArtworksType"
+ "artwork formats"
+ "artworkAssetFileURLWithSize:completion:"
+ "assetFileURL"
+ "assetFileURLData"
+ "audio-outputdevice-allowlist"
+ "audio-outputdevice-denylist"
+ "availableAnimatedArtworkFormats"
+ "availableAnimatedArtworkFormatsAtIndex:"
+ "availableAnimatedArtworkFormatsCount"
+ "availableAnimatedArtworkFormatsType"
+ "cachedDiscoveryEnabled"
+ "canAddTelevisionWithRouteIdentifierToSession:"
+ "canStartNativePlayback"
+ "carPlayBannersEnabled"
+ "clearAnimatedArtworkPreviewFrames"
+ "clearAnimatedArtworks"
+ "clearAvailableAnimatedArtworkFormats"
+ "clearExtendedSupportedRates"
+ "clearRequestedAnimatedArtworkAssetURLFormats"
+ "clearRequestedAnimatedArtworkPreviewFrameFormats"
+ "clusterMemberID"
+ "com.apple.TVAirPlay"
+ "com.apple.airtunesd"
+ "com.apple.mediacontrol"
+ "com.apple.mediaremote.device-info"
+ "conversationManager:didChangeConversationAdvertisement:"
+ "conversationManager:localParticipantClusterDidChangeForConversation:"
+ "conversationManager:localParticipantClusterDidChangeForConversation:fromOldConversation:"
+ "conversationManager:nearbySharePlayToggledForConversation:"
+ "conversationManager:nearbySharePlayToggledForConversation:fromOldConversation:"
+ "createEndpointWithOutputDeviceUIDs.endpoint"
+ "createEndpointWithOutputDeviceUIDs.groupID"
+ "createEndpointWithOutputDeviceUIDs:details:queue:completion:"
+ "createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:"
+ "createHostedEndpointWithOutputDeviceUIDs:details:completion:"
+ "createHostedEndpointWithOutputDeviceUIDs:details:queue:completion:"
+ "createHostedEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:"
+ "debugMessage"
+ "denyList"
+ "deviceIsPlaying"
+ "deviceRemovedSnapshot"
+ "deviceRemovedWaitInterval"
+ "deviceRemovedWaitIntervalTimer"
+ "disableAWDLRoutes"
+ "disableDUGLDuringAirPlayVideo"
+ "discoveredDeviceIsPlaying"
+ "discoveredIsPlaying"
+ "discoveredOutputDevices"
+ "distantOutputDeviceRepresentation"
+ "effectiveIdentifer"
+ "effectiveName"
+ "endEventWithID:"
+ "endEventWithID:error:"
+ "enhanceDialogueActive"
+ "extendedSupportedRate"
+ "extendedSupportedRateAtIndex:"
+ "extendedSupportedRates"
+ "extendedSupportedRatesCount"
+ "externalOutputContextRepresentation"
+ "formatted artwork"
+ "generateArtworkDataWithSize:"
+ "groupSessionAutoApproveParticipantsForAppleTV"
+ "groupSessionJoinRequestAssertionDuration"
+ "hasAssetFileURLData"
+ "hasCachedDiscoveryEnabled"
+ "hasDebugMessage"
+ "hasDeviceIsPlaying"
+ "hasEnhanceDialogueActive"
+ "hasInput"
+ "hasMicrophoneConnectionRequestMessage"
+ "hasMicrophoneConnectionResponseMessage"
+ "hasOperationID"
+ "hasOutput"
+ "hasParentGroupSupportsGroupCohesion"
+ "hasRapportIdentifier"
+ "hasRecipeType"
+ "hasResult"
+ "hasRole"
+ "hasSetPlaybackSessionCommandStatus"
+ "hasShouldWaitForUpdatedOutputDevices"
+ "hasSurface"
+ "hasTransitionStyle"
+ "hasWasDiscoveredInCache"
+ "https"
+ "id<BMRootLibrary> soft_BiomeLibrary(void)"
+ "initChildWithParent:reason:"
+ "initWithAssetFileURL:"
+ "initWithDetails:rapportIdentifier:"
+ "initWithMRError:description:underlyingErrors:"
+ "initWithOutputDeviceGroupUID:features:details:"
+ "initWithOutputDeviceUIDs:features:details:"
+ "initWithPairingData:rapportIdentifier:"
+ "initWithPlaybackSession:request:"
+ "initWithPreviewFrameDataRequestHandler:artworkAssetFileURLRequestHandler:"
+ "initWithRequest:error:setPlaybackSessionCommandStatus:playerPath:"
+ "initWithRequestID:surface:initiator:reason:userInitiated:originatingBundleID:"
+ "initWithResult:rapportIdentifier:"
+ "initWithSurface:initiator:reason:"
+ "initWithURL:readonly:"
+ "initWithUniqueIdentifier:outputDevices:volume:capabilities:muted:"
+ "input"
+ "inputs"
+ "int soft_MKBDeviceUnlockedSinceBoot(void)"
+ "interruptBestStreamIfNecessary"
+ "isCached"
+ "isCarPlayVideoActive"
+ "isCarPlayVideoAllowed"
+ "isEquivalentToDeviceHandle:"
+ "isFileURL"
+ "isGroupLeaderGroupable"
+ "isMyDiscoverableUndiscoverableGroupLeader"
+ "isMyGroupLeader"
+ "isNonRemoteControllableAirPlayDevice"
+ "isStudioDisplay"
+ "joinContinuitySingURLString"
+ "kMRMediaRemoteCommandInfoExtendedSupportedPlaybackRates"
+ "kMRMediaRemoteCommandInfoTransitionStyle"
+ "kMRMediaRemoteNowPlayingInfoSquareAnimatedArtwork"
+ "kMRMediaRemoteNowPlayingInfoSquareAnimatedArtworkIdentifier"
+ "kMRMediaRemoteNowPlayingInfoTallAnimatedArtwork"
+ "kMRMediaRemoteNowPlayingInfoTallAnimatedArtworkIdentifier"
+ "kMRMediaRemoteOptionEnhanceDialogueActive"
+ "language options"
+ "lastConnectionError"
+ "localVolumeHUDPresentationRequest"
+ "localizedGroupComposition"
+ "localizedGroupCompositionForDeviceClass:modelID:"
+ "microphoneConnectionRequestMessage"
+ "microphoneConnectionResponseMessage"
+ "microphoneConnectionTimeout"
+ "migrationReport"
+ "motion_on_lock_screen"
+ "moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:"
+ "mr_error"
+ "msv_treeDescription"
+ "nearbyTVDeviceHandles"
+ "nonCachedResults"
+ "nowPlayingAnimatedArtworkForFormat:"
+ "nowPlayingAnimatedArtworkFormats"
+ "nowPlayingArtworkID"
+ "operationID"
+ "output"
+ "outputDeviceUIDs.count > 0"
+ "outputs"
+ "papika"
+ "parentGroupSupportsGroupCohesion"
+ "performMigrationToOutputDevices"
+ "playbackSessionMigrateFinalizeCallback"
+ "position"
+ "prepareGroupForPlaybackWithOutputDeviceUIDs"
+ "prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:"
+ "presentVolumeHUDWithRequest:"
+ "previewFrameDataWithSize:completion:"
+ "protobufWithFormat:"
+ "recipeType"
+ "recipeTypeAsString:"
+ "registerNowPlayingInfoAnimatedArtworkCallback:"
+ "repeatModeDidChange"
+ "reportName"
+ "requestID=%@ duration=%f failedPlayingAudio=%d"
+ "requestMicrophoneConnection"
+ "requestMicrophoneConnection:completion:"
+ "requestMicrophoneConnectionWithDetails:completion:"
+ "requestMicrophoneConnectionWithDetails:queue:completion:"
+ "requestedAnimatedArtworkAssetURLFormats"
+ "requestedAnimatedArtworkAssetURLFormatsAtIndex:"
+ "requestedAnimatedArtworkAssetURLFormatsCount"
+ "requestedAnimatedArtworkAssetURLFormatsType"
+ "requestedAnimatedArtworkPreviewFrameFormats"
+ "requestedAnimatedArtworkPreviewFrameFormatsAtIndex:"
+ "requestedAnimatedArtworkPreviewFrameFormatsCount"
+ "requestedAnimatedArtworkPreviewFrameFormatsType"
+ "requiresAuthorizationHandling"
+ "resultAsString:"
+ "resultsFromConfiguration:"
+ "roleAsString:"
+ "scheme"
+ "searchForOutputDevices:categories:timeout:details:queue:completion:"
+ "sendPlaybackSessionMigrateFinalize"
+ "setActiveEndpointSnapshot:"
+ "setAnimatedArtworkPreviewFrames:"
+ "setAnimatedArtworks:"
+ "setAssetFileURLData:"
+ "setAvailableAnimatedArtworkFormats:"
+ "setCachedDiscoveryEnabled:"
+ "setCarPlayVideoActive:completion:"
+ "setCarPlayVideoActive:completionHandler:"
+ "setDebugMessage:"
+ "setDeviceIsPlaying:"
+ "setDeviceRemovedSnapshot:"
+ "setDeviceRemovedWaitInterval:"
+ "setDeviceRemovedWaitIntervalTimer:"
+ "setEnhanceDialogueActive:"
+ "setExtendedSupportedRates:count:"
+ "setHasCachedDiscoveryEnabled:"
+ "setHasDeviceIsPlaying:"
+ "setHasEnhanceDialogueActive:"
+ "setHasParentGroupSupportsGroupCohesion:"
+ "setHasRecipeType:"
+ "setHasResult:"
+ "setHasRole:"
+ "setHasShouldWaitForUpdatedOutputDevices:"
+ "setHasTransitionStyle:"
+ "setHasWasDiscoveredInCache:"
+ "setInput:"
+ "setMicrophoneConnectionRequestMessage:"
+ "setMicrophoneConnectionResponseMessage:"
+ "setNowPlayingAnimatedArtwork:forFormat:"
+ "setNowPlayingArtworkID:"
+ "setObject:atIndexedSubscript:"
+ "setOperationID:"
+ "setOutput:"
+ "setParentGroupSupportsGroupCohesion:"
+ "setPlaybackSessionCommandStatus"
+ "setPlaybackSessionMigrateFinalizeCallback:"
+ "setPosition:"
+ "setPreferredState:forBundleIdentifier:"
+ "setPreferredState:forBundleIdentifier:reply:"
+ "setRecipeType:"
+ "setRepeatModeDidChange:"
+ "setRequestedAnimatedArtworkAssetURLFormats:"
+ "setRequestedAnimatedArtworkPreviewFrameFormats:"
+ "setResult:"
+ "setRole:"
+ "setScheme:"
+ "setSetPlaybackSessionCommandStatus:"
+ "setShouldWaitForUpdatedOutputDevices:"
+ "setShuffleModeDidChange:"
+ "setSurface:"
+ "setTransitionStyle:"
+ "setWasDiscoveredInCache:"
+ "sf"
+ "sharedSystemAudioLocalEndpoint"
+ "shouldWaitForUpdatedOutputDevices"
+ "shouldWaitForUpdatedOutputDevices/"
+ "shuffleModeDidChange"
+ "size"
+ "snapshot.endpoint.isLocalEndpoint"
+ "softlink:r:path:/System/Library/Frameworks/Intents.framework/Intents"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport"
+ "softlink:r:path:/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary"
+ "softlink:r:path:/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils"
+ "softlink:r:path:/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities"
+ "startEvent:role:"
+ "startSystemGroupSession"
+ "stopSystemGroupSession"
+ "stringFromByteCount:"
+ "stringWithCapacity:"
+ "supportBluehop"
+ "supportDiscoveryCaching"
+ "supportSystemGroupSession"
+ "supportUGL"
+ "surface"
+ "tlla"
+ "transitionStyle"
+ "ugl"
+ "v16@?0@\"<MRAVDiscoverySession>\"8"
+ "v16@?0@\"NSData\"8"
+ "v16@?0@\"NSURL\"8"
+ "v24@0:8@\"MRVolumeHUDPresentationRequest\"16"
+ "v28@0:8B16@?20"
+ "v32@0:8@\"MRRequestDetails\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"TUConversationManager\"16@\"TUConversationActivityAdvertisement\"24"
+ "v32@0:8q16@\"NSString\"24"
+ "v36@0:8@16@24I32"
+ "v40@0:8@\"NSArray\"16@\"MRRequestDetails\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8q16@\"NSString\"24@?<v@?>32"
+ "v40@0:8{CGSize=dd}16@?32"
+ "void *AirPlaySupportLibrary(void)"
+ "void *BiomeLibraryLibrary(void)"
+ "void *BiomeStreamsLibrary(void)"
+ "void *CoreUtilsLibrary(void)"
+ "void *FrontBoardServicesLibrary(void)"
+ "void *IntentsCoreLibrary(void)"
+ "void *IntentsLibrary(void)"
+ "void *MediaExperienceLibrary(void)"
+ "void *MobileKeyBagLibrary(void)"
+ "void *PowerLogLibrary(void)"
+ "void *SpringBoardServicesLibrary(void)"
+ "void *TelephonyUtilitiesLibrary(void)"
+ "void MRMediaRemoteServiceCreateGroupWithDevices(MRMediaRemoteServiceRef, CFArrayRef, MRRequestDetails *__strong, __strong dispatch_queue_t, void (^__strong)(NSString *__strong, NSError *__strong))"
+ "void _MRLoadContentItemAssets(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, MRPlaybackQueue *__strong, __strong dispatch_queue_t, void (^__strong)(NSError *__strong))"
+ "void _MRPSMDetermineRecipe(MRPlayerPath *__strong, MROrigin *__strong, MRPlaybackSessionMigrateRequest *__strong, __strong dispatch_queue_t, void (^__strong)(MRPlayerPath *__strong, MRPlayerPath *__strong, _MRPSMRecipe *__strong))"
+ "void _MSVHasherAppend32(MSVHasher * _Nonnull, uint32_t)"
+ "void _MSVHasherAppend64(MSVHasher * _Nonnull, uint64_t)"
+ "void _onClientQueue_MRInvokeClientCallback(MRNowPlayingPlayerClient *__strong, __strong MRPlaybackQueueDataSourceContentItemAssetCallback, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, __strong dispatch_queue_t, void (^__strong)(NSError *__strong))"
+ "void _onQueue_MRInvokeClientAssetCallbacks(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, __strong dispatch_queue_t, void (^__strong)(NSArray<NSError *> *__strong))"
+ "void _onQueue_MRInvokeClientCallbacks(MRNowPlayingPlayerClient *__strong, NSArray<MSVCallback *> *__strong, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, _Bool, NSString *__strong, __strong dispatch_queue_t, void (^__strong)(NSError *__strong))"
+ "void _onQueue_MRLoadContentItemAssets(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, NSArray<id> *__strong, __strong dispatch_queue_t, void (^__strong)(NSError *__strong))"
+ "void soft_PLLogRegisteredEvent(PLClientID, CFStringRef, CFDictionaryRef, CFArrayRef)"
+ "volumeHUDController"
+ "wagoneer"
+ "wasDiscoveredInCache"
+ "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"referencePosition\"b1\"sleepTimerTime\"b1\"trackID\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"enhanceDialogueActive\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
+ "{?=\"batteryLevel\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceSubType\"b1\"deviceType\"b1\"distance\"b1\"hostDeviceClass\"b1\"transportType\"b1\"volume\"b1\"volumeCapabilities\"b1\"allowsHeadTrackedSpatialAudio\"b1\"canAccessAppleMusic\"b1\"canAccessRemoteAssets\"b1\"canAccessiCloudMusicLibrary\"b1\"canFetchMediaDataFromSender\"b1\"canPlayEncryptedProgressiveDownloadAssets\"b1\"canRelayCommunicationChannel\"b1\"conversationDetectionEnabled\"b1\"deviceIsPlaying\"b1\"discoveredOnSameInfra\"b1\"engageOnClusterActivate\"b1\"groupContainsGroupLeader\"b1\"isAddedToHomeKit\"b1\"isAirPlayReceiverSessionActive\"b1\"isAppleAccessory\"b1\"isClusterLeader\"b1\"isDeviceGroupable\"b1\"isGroupLeader\"b1\"isGroupable\"b1\"isHeadTrackedSpatialAudioActive\"b1\"isLocalDevice\"b1\"isPickedOnPairedDevice\"b1\"isProxyGroupPlayer\"b1\"isRemoteControllable\"b1\"isVolumeControlAvailable\"b1\"parentGroupContainsDiscoverableLeader\"b1\"pickable\"b1\"presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets\"b1\"producesLowFidelityAudio\"b1\"requiresAuthorization\"b1\"shouldForceRemoteControlabillity\"b1\"supportsBluetoothSharing\"b1\"supportsBufferedAirPlay\"b1\"supportsConversationDetection\"b1\"supportsExternalScreen\"b1\"supportsHAP\"b1\"supportsHeadTrackedSpatialAudio\"b1\"supportsMultiplayer\"b1\"supportsRapport\"b1\"supportsRapportRemoteControlTransport\"b1\"supportsSharePlayHandoff\"b1\"usingJSONProtocol\"b1\"volumeMuted\"b1\"wasDiscoveredInCache\"b1}"
+ "{?=\"endTimestamp\"b1\"errorCode\"b1\"startTimestamp\"b1\"identifier\"b1\"role\"b1}"
+ "{?=\"features\"b1\"targetSessionID\"b1\"alwaysAllowUpdates\"b1\"cachedDiscoveryEnabled\"b1\"enableThrottling\"b1\"populatesExternalDevice\"b1}"
+ "{?=\"playbackPosition\"b1\"playbackRate\"b1\"destinationTypes\"b1\"endpointOptions\"b1\"originatorType\"b1\"playbackState\"b1\"playerOptions\"b1\"recipeType\"b1\"allowFadeTransition\"b1}"
+ "{?=\"protocolVersion\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceClass\"b1\"lastKnownClusterType\"b1\"lastSupportedMessageType\"b1\"logicalDeviceCount\"b1\"preferredEncoding\"b1\"sharedQueueVersion\"b1\"allowsPairing\"b1\"connected\"b1\"groupContainsDiscoverableGroupLeader\"b1\"isAirplayActive\"b1\"isClusterAware\"b1\"isClusterLeader\"b1\"isEligibleForHostingGroupSessionExcludingAcknowledgements\"b1\"isGroupLeader\"b1\"isProxyGroupPlayer\"b1\"parentGroupContainsDiscoverableGroupLeader\"b1\"parentGroupSupportsGroupCohesion\"b1\"supportsACL\"b1\"supportsExtendedMotion\"b1\"supportsMultiplayer\"b1\"supportsOutputContextSync\"b1\"supportsSharedQueue\"b1\"supportsSystemPairing\"b1\"tightlySyncedGroup\"b1}"
+ "{?=\"result\"b1}"
+ "{?=\"sleepTimerFireDate\"b1\"sleepTimerTime\"b1\"canScrub\"b1\"command\"b1\"currentQueueEndAction\"b1\"disabledReason\"b1\"maximumRating\"b1\"minimumRating\"b1\"numAvailableSkips\"b1\"preferredPlaybackRate\"b1\"presentationStyle\"b1\"repeatMode\"b1\"shuffleMode\"b1\"skipFrequency\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"transitionStyle\"b1\"upNextItemCount\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"active\"b1\"enabled\"b1\"supportsReferencePosition\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
+ "{?=\"type\"b1\"fadeAudio\"b1\"muteUntilFinished\"b1\"shouldClearPredictedRoutes\"b1\"shouldModifyPredictedRoutes\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"shouldWaitForUpdatedOutputDevices\"b1\"suppressErrorDialog\"b1}"
+ "\xc0\xdb!\xde"
+ "\xc0\xdb\"\xde"
+ "\xc0\xdbN\xdc"
+ "\xc0\xdbO\xdc"
+ "\xc0\xdb\\\xde "
+ "\xc0ە\xde"
+ "\xc0ۖ\xde"
+ "\xc0ۗ\xde"
+ "\xc0ۘ\xde"
+ "\xc0۬\xdf "
+ "\xc0\xdb\xd5\xde"
+ "\xc0\xdb\xd6\xde"
+ "\xc0\xdb\xea\xdc "
+ "\xc1\xdb\a\xdf"
+ "\xc1\xdb\b\xdf"
+ "\xc1\xdb%\xdc "
+ "\xc1\xdb*\xde "
+ "\xc1\xdbb\xdc "
+ "\xc1\xdbl\xde "
+ "\xc1ۈ\xdf"
+ "\xc1ۉ\xdf"
+ "\xc1ۊ\xdd"
+ "\xc1ۋ\xdd"
+ "\xc1ی\xdc"
+ "\xc1ۍ\xdc"
+ "\xc1ێ\xdc"
+ "\xc1ۏ\xdc"
+ "\xc1ے\xdc"
+ "\xc1ۓ\xdc"
+ "\xc1\xdb\xd2\xdc "
+ "\xc1\xdb\xe2\xdf "
+ "\xc2\xdbI\xdf"
+ "\xc2\xdbQ\xdd"
+ "\xc2\xdbR\xdd"
+ "\xc2ۥ\xdc"
+ "\xc2ۦ\xdc"
+ "\xc2\xdb\xe0\xde"
+ "\xc2\xdb\xe1\xde"
+ "\xc3\xdb9\xde"
+ "\xc3\xdb:\xde"
+ "\xc3\xdbM\xdf "
+ "\xc3ۅ\xde"
+ "\xc3ۆ\xde"
+ "\xc3۟\xdd"
+ "\xc3۠\xdd"
+ "\xc3ۡ\xdd"
+ "\xc3ۢ\xdd"
+ "\xc3\xdb\xc8\xdd"
+ "\xc3\xdb\xc9\xdd"
+ "\xc3\xdb\xd6\xdd"
+ "\xc3\xdb\xd7\xdd"
+ "\xc3\xdb\xeb\xde"
+ "\xc3\xdb\xec\xde"
+ "\xc4۸\xde "
+ "\xc4\xdb\xc8\xdd"
+ "\xc4\xdb\xc9\xdd"
+ "\xc4\xdb\xed\xdd"
+ "\xc4\xdb\xee\xdd"
+ "\xc5\xdb\x1c\xdc"
+ "\xc5ێ\xdf"
+ "\xc5ۏ\xdf"
+ "\xc5\xdb\xc1\xde"
+ "\xc5\xdb\xc2\xde"
+ "\xc5\xdb\xc3\xde"
+ "\xc5\xdb\xc4\xde"
+ "\xc5\xdb\xf3\xde"
+ "\xc5\xdb\xf4\xde"
+ "\xc5\xdb\xf5\xde"
+ "\xc5\xdb\xf6\xde"
+ "\xc5\xdb\xf7\xde"
+ "\xc5\xdb\xf8\xde"
+ "\xc6\xdb\xce\xdc"
+ "\xc6\xdb\xcf\xdc"
+ "\xc7\xdb!\xdf"
+ "\xc7\xdb\"\xdf"
+ "\xc7\xdbF\xdc "
+ "\xc7\xdb\xd4\xdd"
+ "\xc7\xdb\xd5\xdd"
+ "\xc8\xdb"
+ "\xc8\xdbk\xdd "
+ "\xc8\xdb\xc4\xdd"
+ "\xc8\xdb\xcb\xdc"
+ "\xc8\xdb\xcc\xdc"
+ "\xc9\xdbL\xdf"
+ "\xc9\xdbM\xdf"
+ "\xc9۳\xde"
+ "\xc9۴\xde"
+ "\xc9۷\xdf"
+ "\xc9\xdb\xd1\xde"
+ "\xc9\xdb\xd2\xde"
- "    playerPath = %@\n    player = %@\n    supportedCommands = %@\n    nowPlayingInfo = %@\n    nowPlayingArtwork = %@\n    playbackState = %@\n    playbackStateDate= %@\n    playbackQueue = %@\n    capabilities = %ld\n    triggerInvalidation = %@\n    invalidatationTimestamp = %lf\n    cachedContentItemUpdates = %@\n    pictureInPictureEnabled = %@\n    activeRequestDate = %@\n    canBeNowPlaying = %@\n    canBeNowPlayingTimestamp = %@\n    homeUserIdentifiers = %@"
- "  Error: %@\n"
- " %@: %.4f seconds\n"
- "%@(%@)"
- "%@: %@\n"
- "-%d"
- "----------------------------------\n"
- "-[MRAVEndpoint _externalOutputContext]"
- "-[MRAVEndpoint isConnected]"
- "-[MRExternalDevice createHostedEndpointWithOutputDeviceUIDs:queue:completion:]"
- "-[MRExternalDevice setOutputDevicesRemovedCallback:withQueue:]"
- "-[MRExternalDevice setOutputDevicesUpdatedCallback:withQueue:]"
- "/System/Library/Frameworks/AVFoundation.framework/AVFoundation"
- "/System/Library/Frameworks/Intents.framework/Intents"
- "/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport"
- "/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary"
- "/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams"
- "/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils"
- "/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices"
- "/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore"
- "/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience"
- "/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
- "/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog"
- "/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
- "/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities"
- ":LH"
- "<%@ %p {\n   code=%@\n   type=%@\n   commandError=%@\n   %@%@}>"
- "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@>"
- "<origin:%@:%d%@>"
- "@\"AVOutputDeviceGroup\""
- "@16@?0@\"_MRPlaybackSessionMigrateRequestEventProtobuf\"8"
- "@24@0:8I16B20"
- "@36@0:8@16@24I32"
- "@44@0:8@16@24I32@36"
- "AVAudioSession"
- "AVAudioSessionCategoryPlayback"
- "AVAudioSessionRoutingContextChangeNotification"
- "AVOutputContext"
- "AVOutputContextCanSetVolumeDidChangeNotification"
- "AVOutputContextDestinationChangeInitiatedNotification"
- "AVOutputContextDestinationChangePreviousDeviceIDsKey"
- "AVOutputContextDestinationChangeReasonIdleDisconnect"
- "AVOutputContextDestinationChangeReasonKey"
- "AVOutputContextOutputDeviceDidChangeNotification"
- "AVOutputContextOutputDevicesDidChangeNotification"
- "AVOutputContextPredictedOutputDeviceDidChangeNotification"
- "AVOutputContextPredictedOutputDevicesDidChangeNotification"
- "AVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification"
- "AVOutputContextTypeAudio"
- "AVOutputContextTypeSharedAudioPresentation"
- "AVOutputContextTypeSharedSystemAudio"
- "AVOutputContextTypeSharedSystemScreen"
- "AVOutputContextVolumeControlTypeDidChangeNotification"
- "AVOutputDevice"
- "AVOutputDeviceActivatedClusterMembersRoomIDKey"
- "AVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification"
- "AVOutputDeviceBatteryLevelCaseKey"
- "AVOutputDeviceBatteryLevelLeftKey"
- "AVOutputDeviceBatteryLevelRightKey"
- "AVOutputDeviceCanMuteDidChangeNotification"
- "AVOutputDeviceCanSetVolumeDidChangeNotification"
- "AVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification"
- "AVOutputDeviceClusterMemberVolumeDidChangeNotification"
- "AVOutputDeviceCommunicationChannelControlTypeDirect"
- "AVOutputDeviceCommunicationChannelControlTypeRelayed"
- "AVOutputDeviceCommunicationChannelDataDestinationMediaRemote"
- "AVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped"
- "AVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired"
- "AVOutputDeviceCommunicationChannelOptionControlType"
- "AVOutputDeviceCommunicationChannelOptionCorrelationID"
- "AVOutputDeviceCommunicationChannelOptionInitiator"
- "AVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate"
- "AVOutputDeviceDiscoverySession"
- "AVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification"
- "AVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired"
- "AVOutputDeviceGroupAddOutputDeviceOptionInitiator"
- "AVOutputDeviceGroupRemoveOutputDeviceOptionInitiator"
- "AVOutputDeviceGroupVolumeControlTypeDidChangeNotification"
- "AVOutputDeviceGroupVolumeDidChangeNotification"
- "AVOutputDeviceMutedDidChangeNotification"
- "AVOutputDeviceVolumeControlTypeDidChangeNotification"
- "AVOutputDeviceVolumeDidChangeNotification"
- "AVPairedDevice"
- "Attempted to create MRAVConcreteEndpoint without using AVOutputDeviceGroup. Use MRConcreteEndpoint instead."
- "AudioFormatGetProperty"
- "B32@?0@\"MRAVConcreteOutputDevice\"8Q16^B24"
- "Can only attempt to recover logical devices for shared audio presentation contexts."
- "Endpoint.volumeCapabilities"
- "Endpoint.volumeForOutputDeviceUID"
- "Events:\n"
- "Existing devices in endpoint %@"
- "Final devices in endpoint %@"
- "Identifier: %@\n"
- "L"
- "MRAVConcreteEndpoint"
- "MRAVConcreteEndpoint.m"
- "MRXPC_ENDPOINT_LEADER_OPTIONS_KEY"
- "Partially resolved player path mising bundleID: destinationPlayerPath=%@"
- "Partially resolved player path mising origin: destinationPlayerPath=%@"
- "ReconSession"
- "StatusTypeCode"
- "StatusTypeCustom"
- "StatusTypeDialog"
- "StatusTypeError"
- "StatusTypeUnknown"
- "T@\"NSArray\",R,N,V_allowedPlayerPaths"
- "T@\"NSString\",R,N,V_uniqueIdentifier"
- "TB,R,N,GisVolumeMuted,V_volumeMuted"
- "TI,R,N,V_volumeControlCapabilities"
- "Tf,R,N,V_volume"
- "[%@]"
- "[%@] "
- "[ConcreteOutputContext] Beginning reconnaissance session to find missing logical device components: %{public}@"
- "[ConcreteOutputContext] Did not find any incomplete logical devices."
- "[ConcreteOutputContext] Failed to add missing logical device components to output context. %{public}@"
- "[ConcreteOutputContext] Failed to find any remaining logical device components to add."
- "[ConcreteOutputContext] Failed to find missing logical device components: %{public}@ -- found devices %{public}@"
- "[ConcreteOutputContext] Ignoring request to attempt logical device recovery on HomePod."
- "[ConcreteOutputContext] Ignoring request to attempt logical device recovery since attempt is already in progress."
- "[ConcreteOutputContext] Logical Devices: %{public}@. Existing devices: %{public}@."
- "[ConcreteOutputContext] Successfully recovered missing logical devices: %ld"
- "[MRAVConcreteEndpoint] Volume - %{public}@ - Device volume capabilities updated: %{public}@ - %{public}@"
- "[MRAVConcreteEndpoint] Volume - %{public}@ - Endpoint volume updated: %{public}f - %{public}@"
- "[MRAVConcreteEndpoint] Volume - %{public}@ - Group volume capabilities updated: %{public}@ - %{public}@"
- "[MRAVConcreteEndpoint] Volume - %{public}@ - Output device volume updated: %{public}f - %{public}@"
- "[MRGroupSession] [tokenForJoinURLString] URL doesn't have music domain: %{public}@"
- "[MRQHONPC] %@ Unable to discover endpoint."
- "[MRQHONPC] <%@ : %p> processing PlaybackQueueDidChangeNotification."
- "[MRQHONPC] <%@> Artwork cache hit for content item %@, artwork %@."
- "[MRQHONPC] <%@> Begin loading data."
- "[MRQHONPC] <%@> Begin loading updates."
- "[MRQHONPC] <%@> Begin resolving endpoint."
- "[MRQHONPC] <%@> Begin resolving player path for endpoint %@."
- "[MRQHONPC] <%@> Deallocating."
- "[MRQHONPC] <%@> End loading data. Response: %@."
- "[MRQHONPC] <%@> End loading updates."
- "[MRQHONPC] <%@> Error creating player path %@."
- "[MRQHONPC] <%@> Error fetching artwork for content item %@. Error: %@."
- "[MRQHONPC] <%@> Error loading data %@."
- "[MRQHONPC] <%@> Error resolving player path %@."
- "[MRQHONPC] <%@> Player path is not resolved. There may be no now playing application."
- "[MRQHONPC] <%@> Resolved to Endpoint: %@."
- "[MRQHONPC] <%@> Resolved to player path: %@."
- "[MRQHONPC] <%@> _requestAndUpdateArtworkForContentItems because %@."
- "[MRQHONPC] <%@> deferring PlaybackQueueContentItemsChangedNotification for content items %@ because we are requesting a new playback queue."
- "[MRQHONPC] <%@> downloading artwork for content item %@, artwork %@."
- "[MRQHONPC] <%@> ignoring PlaybackQueueContentItemsArtworkChangedNotification for content items %@ "
- "[MRQHONPC] <%@> processing PlaybackQueueContentItemsArtworkChangedNotification for content items %@."
- "[MRQHONPC] <%@> processing PlaybackQueueContentItemsChangedNotification for content items %@."
- "[MRQHONPC] <%@> processing PlaybackStateDidChangeNotification with new PlaybackState %@."
- "[MRQHONPC] <%@> processing SupportedCommandsDidChangeNotification."
- "[MRQHONPC] <%@> reloading due to ASE change."
- "[MRQHONPC] <%@> reloading due to change in endpoint. Current endpoint: %@. New endpoint: %@."
- "[MRQHONPC] <%@> reloading due to player path invalidation."
- "[MRQHONPC] <%@> requesting artwork for content item %@, artwork %@."
- "[MRQHONPC] <%@> updated artwork cache with %@."
- "[MRQHONPC] <%@> updated artwork for content items %@."
- "[MRQHONPC] <%@> updated content items %@."
- "[MRQHONPC] Failed to retrieve player last playing date with error: %@"
- "[NowPlayingInfo] Setting nowPlayingInfo artwork: %@"
- "[ProximityProvider] Adding device %@."
- "[ProximityProvider] Begin providing for device %@ (%@)."
- "[ProximityProvider] Begin providing for device %@, but device is not prepared, so must defer initial provide."
- "[ProximityProvider] Cannot provide because no result has been calculated yet for device %@ (%@)."
- "[ProximityProvider] Device %@ prepare failed with error %@."
- "[ProximityProvider] End providing for device %@ (%@)."
- "[ProximityProvider] Failed to persist artwork data for device %@. Error: %@."
- "[ProximityProvider] No result for device %@, error: %@"
- "[ProximityProvider] Removing device %@ (%@)."
- "[ProximityProvider] Result for device %@ (%@):\n%@"
- "[ProximityProvider] migrateForDevice<%@> beginning for device %@"
- "[ProximityProvider] migrateForDevice<%@> completed for device %@ with error: %@"
- "_allowedPlayerPaths"
- "_computeActiveRouteIDsFromEndpoint:"
- "_handleActiveSystemEndpointOutputDevicesDidChange:"
- "_outputDeviceGroup"
- "_shouldAddLocalEndpoint"
- "_volumeControlCapabilities"
- "addOutputDevice:withOptions:completionHandler:"
- "addOutputDevices"
- "addOutputDevices:APSync"
- "allowedPlayerPaths"
- "attemptLogicalDeviceRecovery"
- "beginPlaybackSessionMigration"
- "cancellationReason"
- "cilantro_auto_undo_auto_route"
- "cilantro_cta"
- "cilantro_delta_banner"
- "cilantro_everywhere"
- "cilantro_rse"
- "coordinatePlayback"
- "createEndpointWithOutputDeviceUIDs"
- "createEndpointWithOutputDeviceUIDs:options:queue:completion:"
- "createHostedEndpoint"
- "createHostedEndpointWithOutputDeviceUIDs:completion:"
- "createSecondaryEndpoint"
- "deviceUID=%@, endpoint=%@"
- "devices=%@ from endpoint=%@"
- "devices=%@ to endpoint=%@"
- "discoverySessionWithEndpointFeatures:enableThrottling:"
- "endEvent:"
- "endEvent:withError:"
- "endPlaybackSessionMigration"
- "errorWithChangeResult:outputDevice:"
- "expanseMigration"
- "fadeOutSource"
- "getPlaybackQueue"
- "getPlaybackState"
- "handleVolumeCapabilityChangedNotification:"
- "handleVolumeChangedNotification:"
- "https://music.apple.com"
- "initWithDesignatedGroupLeader:outputDevices:"
- "initWithOutputDeviceGroup:groupLeader:outputDevices:"
- "initWithOutputDeviceUIDs:outputDeviceGroupID:features:"
- "initWithOutputDeviceUIDs:outputDeviceGroupID:features:details:"
- "initWithPlaybackSession:"
- "initWithRequest:error:playerPath:"
- "initWithURL:resolvingAgainstBaseURL:"
- "isJ327Device"
- "j327"
- "leader UID: %@"
- "migrateProximity"
- "objectsAtIndexes:"
- "origin-%@-%ld/client-%@/player-%@"
- "outputDeviceVolume:APSync"
- "playItemInQueue"
- "playerPath = %@\n"
- "preferRoutesMatchingMediaType"
- "registerVolumeNotifications"
- "removeOutputDevice:withOptions:completionHandler:"
- "removeOutputDevices"
- "removeOutputDevices:APSync"
- "requestFadeInOnDestination"
- "resolvedPlayerPath = %@\n"
- "routeToDevice"
- "search"
- "searchForOutputDevices:categories:timeout:reason:queue:completion:"
- "setOutputDevice"
- "setOutputDeviceVolume:APSync"
- "setOutputDevices"
- "setOutputDevicesRemovedCallback:withQueue:"
- "setOutputDevicesUpdatedCallback:withQueue:"
- "setRate"
- "setVolume on %@"
- "showRouteRecommendationsOutsideApps"
- "sourceRecommendationsPlattersFromIR"
- "startEvent:"
- "supportNativeToAirPlayASERetargetting"
- "undoUnusedAutoRoutes"
- "v16@?0@\"AVOutputDeviceDiscoverySession\"8"
- "v16@?0@\"AVOutputDeviceGroupMembershipChangeResult\"8"
- "v24@?0@\"MRPlaybackSession\"8@\"NSError\"16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@?0@\"MRAVOutputDevice\"8Q16^B24"
- "v48@0:8@16Q24@32@?40"
- "void MRMediaRemoteServiceCreateGroupWithDevicesLeaderOptions(MRMediaRemoteServiceRef, CFArrayRef, __strong dispatch_queue_t, MRGroupLeaderSelectionAdditionalOptions, void (^__strong)(NSString *__strong, NSError *__strong))"
- "void _MRLoadContentItemAssets(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, MRPlaybackQueue *__strong, __strong dispatch_queue_t, __strong dispatch_block_t)"
- "void _MRPSMDetermineRecipe(MRPlayerPath *__strong, MROrigin *__strong, __strong dispatch_queue_t, void (^__strong)(MRPlayerPath *__strong, MRPlayerPath *__strong, _MRPSMRecipe *__strong))"
- "void _onClientQueue_MRInvokeClientCallback(MRNowPlayingPlayerClient *__strong, __strong MRPlaybackQueueDataSourceContentItemAssetCallback, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, __strong dispatch_queue_t, __strong MRPlaybackQueueDataSourceContentItemAssetCallbackCompletion)"
- "void _onQueue_MRInvokeClientAssetCallbacks(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, __strong dispatch_queue_t, __strong MRPlaybackQueueDataSourceContentItemAssetCallbackCompletion)"
- "void _onQueue_MRInvokeClientCallbacks(MRNowPlayingPlayerClient *__strong, NSArray<MSVCallback *> *__strong, MRPlaybackQueueRequest *__strong, MRContentItem *__strong, _Bool, __strong dispatch_queue_t, __strong MRPlaybackQueueDataSourceContentItemAssetCallbackCompletion)"
- "void _onQueue_MRLoadContentItemAssets(MRNowPlayingPlayerClient *__strong, MRPlaybackQueueRequest *__strong, NSArray<id> *__strong, __strong dispatch_queue_t, __strong dispatch_block_t)"
- "volume: %f"
- "volume=%f, deviceUID=%@, endpoint=%@"
- "volumeControlCapabilities:APSync"
- "volumeForOutputDevice:error:"
- "watchIntentionalRouting"
- "watch_intentional_routing"
- "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"referencePosition\"b1\"sleepTimerTime\"b1\"trackID\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
- "{?=\"batteryLevel\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceSubType\"b1\"deviceType\"b1\"distance\"b1\"hostDeviceClass\"b1\"transportType\"b1\"volume\"b1\"volumeCapabilities\"b1\"allowsHeadTrackedSpatialAudio\"b1\"canAccessAppleMusic\"b1\"canAccessRemoteAssets\"b1\"canAccessiCloudMusicLibrary\"b1\"canFetchMediaDataFromSender\"b1\"canPlayEncryptedProgressiveDownloadAssets\"b1\"canRelayCommunicationChannel\"b1\"conversationDetectionEnabled\"b1\"discoveredOnSameInfra\"b1\"engageOnClusterActivate\"b1\"groupContainsGroupLeader\"b1\"isAddedToHomeKit\"b1\"isAirPlayReceiverSessionActive\"b1\"isAppleAccessory\"b1\"isClusterLeader\"b1\"isDeviceGroupable\"b1\"isGroupLeader\"b1\"isGroupable\"b1\"isHeadTrackedSpatialAudioActive\"b1\"isLocalDevice\"b1\"isPickedOnPairedDevice\"b1\"isProxyGroupPlayer\"b1\"isRemoteControllable\"b1\"isVolumeControlAvailable\"b1\"parentGroupContainsDiscoverableLeader\"b1\"pickable\"b1\"presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets\"b1\"producesLowFidelityAudio\"b1\"requiresAuthorization\"b1\"shouldForceRemoteControlabillity\"b1\"supportsBluetoothSharing\"b1\"supportsBufferedAirPlay\"b1\"supportsConversationDetection\"b1\"supportsExternalScreen\"b1\"supportsHAP\"b1\"supportsHeadTrackedSpatialAudio\"b1\"supportsMultiplayer\"b1\"supportsRapport\"b1\"supportsRapportRemoteControlTransport\"b1\"supportsSharePlayHandoff\"b1\"usingJSONProtocol\"b1\"volumeMuted\"b1}"
- "{?=\"duration\"b1\"endTimestamp\"b1\"errorCode\"b1\"startTimestamp\"b1}"
- "{?=\"features\"b1\"targetSessionID\"b1\"alwaysAllowUpdates\"b1\"enableThrottling\"b1\"populatesExternalDevice\"b1}"
- "{?=\"playbackPosition\"b1\"playbackRate\"b1\"destinationTypes\"b1\"endpointOptions\"b1\"originatorType\"b1\"playbackState\"b1\"playerOptions\"b1\"allowFadeTransition\"b1}"
- "{?=\"protocolVersion\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceClass\"b1\"lastKnownClusterType\"b1\"lastSupportedMessageType\"b1\"logicalDeviceCount\"b1\"preferredEncoding\"b1\"sharedQueueVersion\"b1\"allowsPairing\"b1\"connected\"b1\"groupContainsDiscoverableGroupLeader\"b1\"isAirplayActive\"b1\"isClusterAware\"b1\"isClusterLeader\"b1\"isEligibleForHostingGroupSessionExcludingAcknowledgements\"b1\"isGroupLeader\"b1\"isProxyGroupPlayer\"b1\"parentGroupContainsDiscoverableGroupLeader\"b1\"supportsACL\"b1\"supportsExtendedMotion\"b1\"supportsMultiplayer\"b1\"supportsOutputContextSync\"b1\"supportsSharedQueue\"b1\"supportsSystemPairing\"b1\"tightlySyncedGroup\"b1}"
- "{?=\"sleepTimerFireDate\"b1\"sleepTimerTime\"b1\"canScrub\"b1\"command\"b1\"currentQueueEndAction\"b1\"disabledReason\"b1\"maximumRating\"b1\"minimumRating\"b1\"numAvailableSkips\"b1\"preferredPlaybackRate\"b1\"presentationStyle\"b1\"repeatMode\"b1\"shuffleMode\"b1\"skipFrequency\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"upNextItemCount\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"active\"b1\"enabled\"b1\"supportsReferencePosition\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
- "{?=\"type\"b1\"fadeAudio\"b1\"muteUntilFinished\"b1\"shouldClearPredictedRoutes\"b1\"shouldModifyPredictedRoutes\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"

```
