## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-4024.400.1.0.0
-  __TEXT.__text: 0x2d7160
-  __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x272dc
-  __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0x29114
-  __TEXT.__oslogstring: 0xb5ab
-  __TEXT.__gcc_except_tab: 0x58d8
+4024.540.1.0.0
+  __TEXT.__text: 0x2dc578
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x28424
+  __TEXT.__const: 0x4f8
+  __TEXT.__cstring: 0x2923b
+  __TEXT.__oslogstring: 0xbb14
+  __TEXT.__gcc_except_tab: 0x5900
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa480
-  __TEXT.__objc_classname: 0x4825
-  __TEXT.__objc_methname: 0x4607a
-  __TEXT.__objc_methtype: 0x8561
-  __TEXT.__objc_stubs: 0x242c0
-  __DATA_CONST.__got: 0x1200
-  __DATA_CONST.__const: 0x4108
-  __DATA_CONST.__objc_classlist: 0x10c0
+  __TEXT.__unwind_info: 0xa600
+  __TEXT.__objc_classname: 0x4884
+  __TEXT.__objc_methname: 0x468b2
+  __TEXT.__objc_methtype: 0x85f3
+  __TEXT.__objc_stubs: 0x24660
+  __DATA_CONST.__got: 0x1228
+  __DATA_CONST.__const: 0x41b8
+  __DATA_CONST.__objc_classlist: 0x10c8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd688
+  __DATA_CONST.__objc_selrefs: 0xdb98
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xf18
   __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__auth_got: 0x9f0
-  __AUTH_CONST.__const: 0x9190
-  __AUTH_CONST.__cfstring: 0x1f9a0
-  __AUTH_CONST.__objc_const: 0x43518
+  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__const: 0x9410
+  __AUTH_CONST.__cfstring: 0x1fb20
+  __AUTH_CONST.__objc_const: 0x41770
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4150
+  __AUTH.__objc_data: 0x41a0
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2f14
-  __DATA.__data: 0x17e8
-  __DATA.__bss: 0x9b0
+  __DATA.__objc_ivar: 0x2f2c
+  __DATA.__data: 0x1850
+  __DATA.__bss: 0xa20
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x6630
-  __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__data: 0x158
+  __DATA_DIRTY.__bss: 0x388
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2E27E9A8-3000-3B19-A4D8-93C22ED1B700
-  Functions: 18441
-  Symbols:   33829
-  CStrings:  22301
+  UUID: A1B1E677-76E6-3ED8-9E57-CC8A22EC339D
+  Functions: 19044
+  Symbols:   34740
+  CStrings:  22417
 
Symbols:
+ +[MRAVConcreteOutputContext sharedAudioPresentationContext].cold.1
+ +[MRAVConcreteOutputContext sharedSystemAudioContext].cold.1
+ +[MRAVConcreteOutputContext sharedSystemScreenContext].cold.1
+ +[MRAVDistantEndpoint externalDeviceFactory].cold.1
+ +[MRAVEndpoint _notificationSerialQueue].cold.1
+ +[MRAVEndpoint _notifyDidAddOutputDevice:endpoint:].cold.1
+ +[MRAVEndpoint _notifyDidChangeOutputDevice:endpoint:].cold.1
+ +[MRAVEndpoint _notifyDidRemoveOutputDevice:endpoint:].cold.1
+ +[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:].cold.1
+ +[MRAVLocalEndpoint sharedLocalEndpointForRoutingContextWithUID:].cold.1
+ +[MRAVOutputContext notificationQueue].cold.1
+ +[MRAVOutputDevice localDeviceLocalizedName].cold.1
+ +[MRAVRoutingDiscoverySession discoverySessionFactories].cold.1
+ +[MRAVRoutingDiscoverySession loggingQueue]
+ +[MRAVRoutingDiscoverySession loggingQueue].cold.1
+ +[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:].cold.1
+ +[MRActiveRoutesObserver fetchActiveRouteIDsWithCompletion:].cold.1
+ +[MRArtwork processRequestsExternalArtworkValidation].cold.1
+ +[MRClientApplicationConnectionManager sharedManager].cold.1
+ +[MRClientDiagnosticsDataSource sharedDataSource].cold.1
+ +[MRCompanionLinkClient sharedCompanionLinkClient].cold.1
+ +[MRCompanionLinkClient sharedIDSCompanionLinkClient].cold.1
+ +[MRCoreUtilsSystemPairingSession globalPairingQueue].cold.1
+ +[MRCoreUtilsSystemPairingSession systemPairingAvailable].cold.1
+ +[MRDestinationResolverDependencies defaultDependencies].cold.1
+ +[MRDeviceIdentifierSymbolProvider currentDeviceRoutingSymbolName].cold.1
+ +[MRDeviceIdentifierSymbolProvider sharedProvider].cold.1
+ +[MRDeviceInfoRequest cachedDeviceInfoForOrigin:].cold.1
+ +[MRDeviceInfoRequest deviceInfoForUID:queue:completion:].cold.1
+ +[MRDistantExternalDevice _notificationSerialQueue].cold.1
+ +[MRExpanseManager sharedManager].cold.1
+ +[MRExternalDeviceManager sharedManager].cold.1
+ +[MRGroupComposition homePodHomeTheaterCompositionWithHomePodModelIdentifier:]
+ +[MRGroupComposition homePodStereoPairCompositionWithModelIdentifier:]
+ +[MRGroupSessionRequestManager sharedManager].cold.1
+ +[MRGroupSymbolProvider symbolNameForType:fillVariant:]
+ +[MRGroupSymbolProvider symbolNameForType:fillVariant:otherVariantOptions:]
+ +[MRIDSCompanionConnection sharedManager].cold.1
+ +[MRIRRoute routeWithEndpoint:].cold.1
+ +[MRMediaRemoteServiceClient sharedServiceClient].cold.1
+ +[MRNotificationClient nowPlayingNotifications].cold.1
+ +[MRNowPlayingController performRequest:withCompletion:].cold.1
+ +[MRNowPlayingOriginClientManager sharedManager].cold.1
+ +[MROutputContextController sharedOutputContextController].cold.1
+ +[MROutputContextDataSource _notificationSerialQueue].cold.1
+ +[MRPlayer defaultPlayer].cold.1
+ +[MRPlayerPath localPlayerPath].cold.1
+ +[MRPowerLogger sharedLogger].cold.1
+ +[MRProtocolMessageLogger sharedLogger].cold.1
+ +[MRRapportTransport userDefaults].cold.1
+ +[MRRemoteControl sharedRemoteControl].cold.1
+ +[MRRestrictedCommandClientsManager sharedManager].cold.1
+ +[MRSharedSettings currentSettings].cold.1
+ +[MRSystemMediaBundles _allSystemMediaBundles].cold.1
+ +[MRSystemMediaBundles isBundleID:systemMediaBundle:].cold.1
+ +[MRSystemMediaBundles isBundleID:systemMediaBundle:].cold.2
+ +[MRSystemMediaBundles isBundleID:systemMediaBundle:].cold.3
+ +[MRSystemMediaBundles isBundleID:systemMediaBundle:].cold.4
+ +[MRSystemMediaBundles isBundleID:systemMediaBundle:].cold.5
+ +[MRSystemMediaBundles isProcessNameAirPlayReceiver:].cold.1
+ +[MRUserSettings currentSettings].cold.1
+ +[MRVVIClient sharedClient].cold.1
+ +[MRVirtualOutputContextManager sharedManager].cold.1
+ +[_MRPSMRecipe legacySetPlaybackSessionWithSessionType:]
+ +[_MRPSMRecipe notPossibleWithError:]
+ +[_MRPSMRecipe oneShotSetPlaybackSessionWithCommandInfo:]
+ -[MRAVConcreteOutputContext _handleOutputContextCanSetVolumeDidChangeNotification:]
+ -[MRAVConcreteOutputContext _handleOutputContextVolumeControlTypeDidChangeNotification:]
+ -[MRAVConcreteOutputContext _registerNotificationsForOutputContext:]
+ -[MRAVConcreteOutputContext setAvOutputContext:].cold.1
+ -[MRAVConcreteOutputDevice _loadLocalOverrides]
+ -[MRAVConcreteOutputDevice alternateTransportType]
+ -[MRAVConcreteOutputDevice initWithAVOutputDevice:sourceInfo:].cold.1
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:].cold.1
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_fetchOutputDevicesFromDiscoverySession:]
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_fetchOutputDevicesFromDiscoverySession:].cold.1
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reloadAvailableOutputDevices]
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload]
+ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload].cold.1
+ -[MRAVDistantOutputDevice alternateTransportType]
+ -[MRAVEndpoint _prepareToMigrateToEndpoint:queue:completion:].cold.1
+ -[MRAVEndpoint canMigrateToEndpoint:queue:completion:].cold.1
+ -[MRAVEndpoint modifyTopologyWithRequest:withReplyQueue:completion:].cold.1
+ -[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:].cold.1
+ -[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:].cold.1
+ -[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:].cold.2
+ -[MRAVEndpointObserver _handleEndpointsDidChange:].cold.1
+ -[MRAVEndpointObserver _reevaluateEndpoint].cold.1
+ -[MRAVExternalRoutingDiscoverySession initWithConfiguration:].cold.1
+ -[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:].cold.1
+ -[MRAVLightweightReconnaissanceSession searchEndpointsForRoutingContextUID:timeout:details:queue:completion:].cold.1
+ -[MRAVLightweightReconnaissanceSession searchEndpointsForString:timeout:reason:queue:completion:].cold.1
+ -[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:].cold.1
+ -[MRAVLocalEndpoint audioDiscoverySession].cold.1
+ -[MRAVLocalEndpoint groupSessionEligibilityMonitor].cold.1
+ -[MRAVOutputContext _notifyChangesInOutputDevicesWithAdded:removed:updated:previous:newDevices:].cold.1
+ -[MRAVOutputContext _notifyChangesInOutputDevicesWithAdded:removed:updated:previous:newDevices:].cold.2
+ -[MRAVOutputContext _reloadWithOutputDevices:].cold.2
+ -[MRAVOutputContext setOutputDevices:].cold.1
+ -[MRAVOutputDevice alternateTransportType]
+ -[MRAVOutputDevice isB515CDevice]
+ -[MRAVOutputDevice isB825Device]
+ -[MRAVOutputDevice isHomePodMiniDevice]
+ -[MRAVOutputDeviceSourceInfo initWithMultipleBuiltInDevices:sourceType:]
+ -[MRAVOutputDeviceSourceInfo sourceType]
+ -[MRAVOutputDeviceTransport initWithOutputDevice:groupID:connectionType:].cold.1
+ -[MRAVReconnaissanceSession _onQueue_beginSearchWithTimeout:].cold.1
+ -[MRAVReconnaissanceSession _onQueue_beginSearchWithTimeout:].cold.2
+ -[MRAVReconnaissanceSession _onQueue_beginSearchWithTimeout:].cold.3
+ -[MRAVReconnaissanceSession _onQueue_beginSearchWithTimeout:].cold.4
+ -[MRAVReconnaissanceSession _onQueue_processSearchLoop].cold.1
+ -[MRAVReconnaissanceSession _onQueue_processSearchLoop].cold.2
+ -[MRAVReconnaissanceSession _onQueue_processSearchLoop].cold.3
+ -[MRAVRoomOutputDevice adjustVolume:details:].cold.1
+ -[MRAVRoomOutputDevice initWithOutputDevice:memberOutputDevices:].cold.1
+ -[MRAVRoomOutputDevice initWithOutputDevice:memberOutputDevices:].cold.2
+ -[MRAVRoomOutputDevice setVolumeMuted:details:].cold.1
+ -[MRAVRoutingClientController initWithMediaRemoteService:].cold.1
+ -[MRAVRoutingDiscoverySession notifyAvailableEndpointsChanged:discoveredEndpoints:].cold.1
+ -[MRAVXPCPipeTransport initWithOutputDevice:pipeEndpoint:].cold.1
+ -[MRAVXPCPipeTransport initWithOutputDevice:pipeEndpoint:].cold.2
+ -[MRActiveRoutesObserver _handleActiveDeviceInfoDidChange:]
+ -[MRActiveRoutesObserver _onWorkerQueue_reevaluateAPA]
+ -[MRActiveRoutesObserver _onWorkerQueue_reevaluateASE]
+ -[MRActiveRoutesObserver _reevaluateAPA]
+ -[MRActiveRoutesObserver _reevaluateASE]
+ -[MRActiveRoutesObserver activeRouteIDsChangedCallback]
+ -[MRActiveRoutesObserver initWithActiveRouteIDsChangedCallback:isLocalDeviceAirplayActiveChangedCallback:]
+ -[MRActiveRoutesObserver isLocalDeviceAirPlayActiveCallback]
+ -[MRActiveRoutesObserver isLocalDeviceAirPlayActive]
+ -[MRActiveRoutesObserver setActiveRouteIDsChangedCallback:]
+ -[MRActiveRoutesObserver setIsLocalDeviceAirPlayActive:]
+ -[MRActiveRoutesObserver setIsLocalDeviceAirPlayActiveCallback:]
+ -[MRAirPlayTransportConnection transportTypeForTransport:]
+ -[MRAudioDataBlock _parseBuffer:].cold.1
+ -[MRAudioDataBlock _parseBuffer:].cold.2
+ -[MRCommandResult initWithErrorCode:]
+ -[MRConcreteEndpoint initWithDesignatedGroupLeader:outputDevices:preferredSuffix:connectionType:].cold.1
+ -[MRConcreteEndpoint initWithDesignatedGroupLeader:outputDevices:preferredSuffix:connectionType:].cold.2
+ -[MRConcreteEndpoint initWithDesignatedGroupLeader:outputDevices:preferredSuffix:connectionType:].cold.3
+ -[MRContentItemMetadata setSubtitleShort:]
+ -[MRContentItemMetadata subtitleShort]
+ -[MRContentItemRequest initWithCoder:].cold.1
+ -[MRContentItemRequest initWithCoder:].cold.2
+ -[MRContentItemRequest initWithCoder:].cold.3
+ -[MRContentItemRequest initWithCoder:].cold.4
+ -[MRContentItemRequest initWithItem:request:].cold.1
+ -[MRContentItemRequest initWithItem:request:].cold.2
+ -[MRDestination initWithOutputContextUID:].cold.1
+ -[MRDeviceInfo(MRDeviceInfoOutputDeviceAdditions) deviceSubtype]
+ -[MRDeviceInfoMessage supportedProtocolMessages].cold.1
+ -[MRDistantExternalDevice connectWithOptions:userInfo:completion:].cold.2
+ -[MRDistantExternalDevice setExternalOutputContext:].cold.1
+ -[MRExternalClientConnection initWithConnection:replyQueue:]
+ -[MRExternalDeviceController initWithBonjourServiceType:].cold.1
+ -[MRExternalDeviceTransportConnection dataSource]
+ -[MRExternalDeviceTransportConnection initWithDataSource:]
+ -[MRExternalDeviceTransportConnection setDataSource:]
+ -[MRExternalDeviceTransportConnection transportType]
+ -[MRExternalJSONClientConnection initWithConnection:replyQueue:]
+ -[MRExternalOutputContextDataSource initializeVolumeCapabilitiesForLegacyCleints].cold.1
+ -[MRGroupComposition addHomePodWithModelIdentifier:]
+ -[MRGroupComposition earPodCount]
+ -[MRGroupComposition setEarPodCount:]
+ -[MRIDSClientConnection initWithConnection:replyQueue:]
+ -[MRIDSCompanionTransportConnection transportTypeForTransport:]
+ -[MRLegacySendHIDEventMessage initWithHIDEvent:].cold.1
+ -[MRNotificationClient _processAlwaysNeedsNowPlayingNotifications].cold.1
+ -[MRNotificationServiceClient _handlePlayerIsPlayingDidChangeNotification:].cold.1
+ -[MRNotificationServiceClient _handlePlayerPlaybackStateDidChangeNotification:].cold.1
+ -[MRNotificationServiceClient _processNeedsNonPlayerPathBasedNotificationsForBackwardCompatabilitySupport].cold.1
+ -[MRNowPlayingAudioFormatController faceTimeBundleSet].cold.1
+ -[MRNowPlayingClient initWithPlayerPath:].cold.1
+ -[MRNowPlayingClient initWithPlayerPath:].cold.2
+ -[MRNowPlayingClient initWithPlayerPath:].cold.3
+ -[MRNowPlayingClient initWithPlayerPath:].cold.4
+ -[MRNowPlayingClientRequests handleClientPropertiesRequestWithCompletion:].cold.1
+ -[MRNowPlayingClientRequests initWithPlayerPath:].cold.1
+ -[MRNowPlayingClientRequests initWithPlayerPath:].cold.2
+ -[MRNowPlayingControllerConfiguration isArtworkOnly]
+ -[MRNowPlayingControllerConfiguration setArtworkOnly:]
+ -[MRNowPlayingOriginClientManager _createOriginClientForPlayerPath:routingContextID:].cold.1
+ -[MRNowPlayingOriginClientManager createCustomOriginClientForOrigin:routingContextID:].cold.1
+ -[MRNowPlayingOriginClientManager existingOriginClientForPlayerPath:].cold.1
+ -[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:queue:completion:].cold.1
+ -[MRNowPlayingOriginClientManager removeOrigin:].cold.1
+ -[MRNowPlayingOriginClientManager removeOriginRequests:].cold.1
+ -[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:].cold.1
+ -[MRNowPlayingOriginClientRequests handleDeviceInfoRequestWithCompletion:].cold.1
+ -[MRNowPlayingOriginClientRequests handleLastPlayingDateRequestWithCompletion:].cold.1
+ -[MRNowPlayingOriginClientRequests handleVolumeCapabilitiesRequestWithCompletion:].cold.1
+ -[MRNowPlayingOriginClientRequests handleVolumeRequestWithCompletion:].cold.1
+ -[MRNowPlayingOriginClientRequests initWithOrigin:].cold.1
+ -[MRNowPlayingPlayerClient addPendingPlaybackSessionMigrateEvent:].cold.1
+ -[MRNowPlayingPlayerClient addPendingPlaybackSessionMigrateEvent:].cold.2
+ -[MRNowPlayingPlayerClient addPendingRequest:].cold.1
+ -[MRNowPlayingPlayerClient addPendingRequest:].cold.2
+ -[MRNowPlayingPlayerClient initWithPlayerPath:].cold.1
+ -[MRNowPlayingPlayerClient removePendingPlaybackSessionMigrateEvent:].cold.1
+ -[MRNowPlayingPlayerClient removePendingPlaybackSessionMigrateEvent:].cold.2
+ -[MRNowPlayingPlayerClient startCachingContentItemUpdatesForItem:forPendingRequest:].cold.1
+ -[MRNowPlayingPlayerClient startCachingContentItemUpdatesForItem:forPendingRequest:].cold.2
+ -[MRNowPlayingPlayerClient updatePlaybackQueueWithCachedUpdates:forPendingRequest:].cold.1
+ -[MRNowPlayingPlayerClient updatePlaybackQueueWithCachedUpdates:forPendingRequest:].cold.2
+ -[MRNowPlayingPlayerClientCallbacks initWithPlayerPath:queue:].cold.1
+ -[MRNowPlayingPlayerClientCallbacks initWithPlayerPath:queue:].cold.2
+ -[MRNowPlayingPlayerClientRequests handlePlaybackStateRequestWithCompletion:].cold.1
+ -[MRNowPlayingPlayerClientRequests handlePlayerPropertiesRequestWithCompletion:].cold.1
+ -[MRNowPlayingPlayerClientRequests handleSupportedCommandsRequestWithCompletion:].cold.1
+ -[MRNowPlayingPlayerClientRequests initWithPlayerPath:].cold.1
+ -[MRNowPlayingRequest nowPlayingPlayerPathOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestClientPropertiesOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestLastPlayingDateOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingInfoOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingItemArtworkOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingItemLanguageOptionsOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingItemMetadataOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestPlaybackRateOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestPlaybackStateOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestProxiableSupportedCommandsOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestShuffleAndRepeatModeOnQueue:completion:].cold.1
+ -[MRNowPlayingRequest requestSupportedCommandsOnQueue:completion:].cold.1
+ -[MRNowPlayingSessionServiceClient _handleCreatePlayerForOrigin:deviceInfo:completion:].cold.1
+ -[MROptimisticState initWithInitialState:expectedState:timeout:queue:timeoutHandler:].cold.1
+ -[MROutputContextController setLocalVolume:].cold.2
+ -[MROutputContextController setLocalVolume:].cold.3
+ -[MROutputContextController setLocalVolumeControlCapabilities:].cold.2
+ -[MROutputContextController setLocalVolumeControlCapabilities:].cold.3
+ -[MROutputContextController setLocalVolumeControlCapabilities:].cold.4
+ -[MROutputContextController setLocalVolumeMuted:].cold.2
+ -[MROutputContextController setLocalVolumeMuted:].cold.3
+ -[MROutputContextDataSource outputDevicesForUID:]
+ -[MRPlaybackQueue contentItemWithOffset:].cold.1
+ -[MRPlaybackQueueClient initWithQueue:].cold.1
+ -[MRPlaybackQueueSubscriptionController restoreStateFromController:].cold.1
+ -[MRPlaybackQueueSubscriptionController restoreStateFromController:].cold.2
+ -[MRPlaybackSessionRequest destinationCommandInfo]
+ -[MRPlaybackSessionRequest destinationPlayerPath]
+ -[MRPlaybackSessionRequest setDestinationCommandInfo:]
+ -[MRPlaybackSessionRequest setDestinationPlayerPath:]
+ -[MRPlayer initWithData:].cold.1
+ -[MRPlayerPath initWithOrigin:client:player:].cold.1
+ -[MRPlayerPath initWithOrigin:client:player:].cold.2
+ -[MRPlayerPath initWithOrigin:client:player:].cold.3
+ -[MRPlayerPath playerPathByRedirectingToOrigin:].cold.1
+ -[MRPlayerPath setClient:].cold.1
+ -[MRPlayerPath setOrigin:].cold.1
+ -[MRPlayerPath setPlayer:].cold.1
+ -[MRProtocolClientConnection _processMessage:].cold.1
+ -[MRProtocolClientConnection _sendMessage:reply:].cold.1
+ -[MRProtocolClientConnection _sendMessage:timeout:reply:]
+ -[MRProtocolClientConnection initWithConnection:replyQueue:]
+ -[MRProtocolClientConnection initWithConnection:replyQueue:].cold.1
+ -[MRProtocolClientConnection replyQueue]
+ -[MRProtocolClientConnection sendQueue]
+ -[MRProtocolClientConnection setSendQueue:]
+ -[MRProtocolMessage protobufData].cold.1
+ -[MRRapportTransportConnection transportTypeForTransport:]
+ -[MRRateLimiter _notify]
+ -[MRRateLimiter initWithInterval:name:queue:block:].cold.1
+ -[MRRateLimiter initWithInterval:name:queue:block:].cold.2
+ -[MRRateLimiter initWithInterval:name:queue:block:].cold.3
+ -[MRRateLimiter initWithInterval:name:queue:block:].cold.4
+ -[MRRemoteArtwork initWithArtworkURLString:templateData:].cold.1
+ -[MRSharedSettings afterRoutingCompleteTimeout]
+ -[MRStreamTransportConnection initWithInputStream:outputStream:dataSource:]
+ -[MRTelevisionController externalDeviceController:didDiscoverDevice:].cold.1
+ -[MRTelevisionController externalDeviceController:didRemoveDevice:].cold.1
+ -[MRTransactionDestination packetsFromMessage:completion:].cold.3
+ -[MRTransactionDestination packetsFromMessage:completion:].cold.4
+ -[MRTransactionPacket initWithData:forKey:].cold.1
+ -[MRTransactionPacket initWithPackets:].cold.1
+ -[MRTransactionPacket initWithPackets:].cold.2
+ -[MRTransactionPacket initWithProtobuf:].cold.1
+ -[MRTransactionPacket isWriteComplete].cold.1
+ -[MRTransactionPacket protobuf].cold.1
+ -[MRTransactionPacket protobuf].cold.2
+ -[MRTransactionPacket writeComplete].cold.1
+ -[MRTransactionPacket writeComplete].cold.2
+ -[MRTransactionPacketAccumulator mergePacket:].cold.1
+ -[MRTransactionSource _processMessage:].cold.4
+ -[MRUserSettings afterRoutingCompleteTimeout]
+ -[MRUserSettings groupSessionBoopAdvertisementEnabled].cold.1
+ -[MRUserSettings groupSessionDelayedInitializationEnabled]
+ -[MRUserSettings hasSystemVolumeCapabilitiesOverride]
+ -[MRUserSettings observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[MRUserSettings proactiveRecommendedPlayerInterval]
+ -[MRUserSettings supportProactiveRecommendedPlayer]
+ -[MRUserSettings systemVolumeCapabilitiesOverride]
+ -[MRUserSettings systemVolumeOverride]
+ -[MRUserSettings watchIntentionalRouting]
+ -[MRV2NowPlayingController _configureReloadTimerForError:].cold.1
+ -[MRV2NowPlayingController _loadNowPlayingStateForConfiguration:requestID:completion:].cold.1
+ -[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:].cold.1
+ -[MRV2NowPlayingController initWithConfiguration:].cold.1
+ -[MRXPCConnection initWithConnection:queue:defaultReplyQueue:].cold.1
+ -[MRXPCConnection sendMessage:queue:reply:].cold.1
+ -[_MRAVOutputDeviceDescriptorProtobuf alternateTransportType]
+ -[_MRAVOutputDeviceDescriptorProtobuf hasAlternateTransportType]
+ -[_MRAVOutputDeviceDescriptorProtobuf setAlternateTransportType:]
+ -[_MRCommandInfoProtobuf hasPlaybackSessionRequirements]
+ -[_MRCommandInfoProtobuf playbackSessionRequirements]
+ -[_MRCommandInfoProtobuf setPlaybackSessionRequirements:]
+ -[_MRCommandOptionsProtobuf delegateAccountDataType]
+ -[_MRCommandOptionsProtobuf delegateAccountData]
+ -[_MRCommandOptionsProtobuf hasDelegateAccountDataType]
+ -[_MRCommandOptionsProtobuf hasDelegateAccountData]
+ -[_MRCommandOptionsProtobuf setDelegateAccountData:]
+ -[_MRCommandOptionsProtobuf setDelegateAccountDataType:]
+ -[_MRContentItemMetadataProtobuf hasSubtitleShort]
+ -[_MRContentItemMetadataProtobuf setSubtitleShort:]
+ -[_MRContentItemMetadataProtobuf subtitleShort]
+ -[_MRPSMRecipe .cxx_destruct]
+ -[_MRPSMRecipe destinationSetPlaybackSessionCommandInfo]
+ -[_MRPSMRecipe error]
+ -[_MRPSMRecipe playbackSessionType]
+ -[_MRPSMRecipe setType:]
+ -[_MRPSMRecipe type]
+ -[_MRPlaybackSessionRequestProtobuf destinationCommandInfo]
+ -[_MRPlaybackSessionRequestProtobuf destinationPlayerPath]
+ -[_MRPlaybackSessionRequestProtobuf hasDestinationCommandInfo]
+ -[_MRPlaybackSessionRequestProtobuf hasDestinationPlayerPath]
+ -[_MRPlaybackSessionRequestProtobuf setDestinationCommandInfo:]
+ -[_MRPlaybackSessionRequestProtobuf setDestinationPlayerPath:]
+ -[_MRSendCommandResultProtobuf error]
+ -[_MRSendCommandResultProtobuf hasError]
+ -[_MRSendCommandResultProtobuf setError:]
+ -[_MRTelevisionControllerBlockCallback initWithCallbackBlock:queue:].cold.1
+ -[_MRTelevisionControllerBlockCallback initWithCallbackBlock:queue:].cold.2
+ GCC_except_table118
+ GCC_except_table205
+ GCC_except_table308
+ GCC_except_table75
+ GCC_except_table87
+ MRAVEndpointResolveActiveSystemEndpointWithTimeout.cold.1
+ MRActiveEndpointTypeForCurrentApplication.cold.1
+ MRAddPlayerPathToUserInfo.cold.1
+ MRAddPlayerPathToXPCMessage.cold.1
+ MRAnalyticsCompositionForEndpoint.cold.1
+ MRAnalyticsCompositionForLocalDevice.cold.1
+ MRAnalyticsSendEvent.cold.1
+ MRApplicationConnectionGetMessageQueue.cold.1
+ MRApplicationConnectionGetQueue.cold.1
+ MRContentItemCreate.cold.1
+ MRContentItemMerge.cold.2
+ MRContentItemSetAlbumArtistName.cold.1
+ MRContentItemSetAlbumName.cold.1
+ MRContentItemSetAlbumYear.cold.1
+ MRContentItemSetArtworkIdentifier.cold.1
+ MRContentItemSetArtworkMIMEType.cold.1
+ MRContentItemSetBrandIdentifier.cold.1
+ MRContentItemSetClassicalWork.cold.1
+ MRContentItemSetCollectionIdentifier.cold.1
+ MRContentItemSetComposer.cold.1
+ MRContentItemSetContentIdentifier.cold.1
+ MRContentItemSetDirectorName.cold.1
+ MRContentItemSetDurationStringLocalizationKey.cold.1
+ MRContentItemSetGenre.cold.1
+ MRContentItemSetLocalizedContentRating.cold.1
+ MRContentItemSetLocalizedDurationString.cold.1
+ MRContentItemSetProfileIdentifier.cold.1
+ MRContentItemSetRadioStationName.cold.1
+ MRContentItemSetRadioStationString.cold.1
+ MRContentItemSetSeriesName.cold.1
+ MRContentItemSetServiceIdentifier.cold.1
+ MRContentItemSetSubtitle.cold.1
+ MRContentItemSetTitle.cold.1
+ MRContentItemSetTrackArtistName.cold.1
+ MRCopyRegisteredTransactionDescriptions.cold.1
+ MRDiagnosticCreate.cold.1
+ MRDiagnosticCreate.cold.2
+ MRExternalDeviceConnect.cold.1
+ MRExternalDeviceConnectEx.cold.1
+ MRExternalDeviceCopyCustomOrigin.cold.1
+ MRExternalDeviceCopyDeviceInfo.cold.1
+ MRExternalDeviceCopyHostName.cold.1
+ MRExternalDeviceCopyName.cold.1
+ MRExternalDeviceCopySystemBuildVersion.cold.1
+ MRExternalDeviceCopyUniqueIdentifier.cold.1
+ MRExternalDeviceDeletePairedDevice.cold.1
+ MRExternalDeviceDisconnect.cold.1
+ MRExternalDeviceGetConnectionState.cold.1
+ MRExternalDeviceGetNetworkPort.cold.1
+ MRExternalDeviceGetOutputDeviceUIDVolume.cold.1
+ MRExternalDeviceGetPairedDevices.cold.1
+ MRExternalDeviceIsConnected.cold.1
+ MRExternalDeviceIsPairingAllowed.cold.1
+ MRExternalDevicePing.cold.1
+ MRExternalDevicePing.cold.2
+ MRExternalDeviceRequestOutputContextModification.cold.1
+ MRExternalDeviceSendButtonEvent.cold.1
+ MRExternalDeviceSendCustomData.cold.1
+ MRExternalDeviceSendCustomData.cold.2
+ MRExternalDeviceSendCustomData.cold.3
+ MRExternalDeviceSetConnectionStateCallback.cold.1
+ MRExternalDeviceSetCustomDataCallback.cold.1
+ MRExternalDeviceSetNameCallback.cold.1
+ MRExternalDeviceSetOutputDeviceUIDVolume.cold.1
+ MRExternalDeviceSetPairingAllowedCallback.cold.1
+ MRExternalDeviceSetPairingCallback.cold.1
+ MRExternalDeviceSetVolumeChangedCallback.cold.1
+ MRExternalDeviceSetWantsNowPlayingArtworkUpdates.cold.1
+ MRExternalDeviceSetWantsNowPlayingUpdates.cold.1
+ MRExternalDeviceSetWantsOutputDeviceUpdates.cold.1
+ MRExternalDeviceSetWantsVolumeUpdates.cold.1
+ MRGroupSessionSubsystemGetNotificationQueue.cold.1
+ MRGroupSessionSubsystemGetQueue.cold.1
+ MRGroupSessionTokenCreateWithInvitationData.cold.1
+ MRInvalidateTransactions.cold.1
+ MRIsObjectOfClass.cold.1
+ MRLogCategoryConnections.cold.1
+ MRLogCategoryDiscovery.cold.1
+ MRLogCategoryDiscoveryOversize.cold.1
+ MRLogCategoryDiscoveryUpdates.cold.1
+ MRLogCategoryMigrationOversize.cold.1
+ MRLogCategoryOutputContextUpdates.cold.1
+ MRMediaRemoteApplicationIsAirPlayReceiver.cold.1
+ MRMediaRemoteApplicationIsSystemAppleTVApplication.cold.1
+ MRMediaRemoteApplicationIsSystemBooksApplication.cold.1
+ MRMediaRemoteApplicationIsSystemClassicalRoomApplication.cold.1
+ MRMediaRemoteApplicationIsSystemMediaApplication.cold.1
+ MRMediaRemoteApplicationIsSystemPodcastApplication.cold.1
+ MRMediaRemoteApplicationSupportsBrowsableContent.cold.1
+ MRMediaRemoteBundle.bundle
+ MRMediaRemoteBundle.cold.1
+ MRMediaRemoteBundle.onceToken
+ MRMediaRemoteCopyAirPlayGroupUID.cold.1
+ MRMediaRemoteCopyDeviceUID.cold.1
+ MRMediaRemoteCopyGroupUID.cold.1
+ MRMediaRemoteCopyLocalAirPlayReceiverClusterType.cold.1
+ MRMediaRemoteCopyLocalAirPlaySenderDefaultGroupIdentity.cold.1
+ MRMediaRemoteCopyLocalClusterID.cold.1
+ MRMediaRemoteCopyLocalClusterLeaderIdentity.cold.1
+ MRMediaRemoteCopySenderDefaultGroupUID.cold.1
+ MRMediaRemoteCopySystemMediaApplicationDefaultSupportedCommands.cold.1
+ MRMediaRemoteCopyVirtualOutputDevices.cold.1
+ MRMediaRemoteCurrentApplicationIsAirPlayReceiver.cold.1
+ MRMediaRemoteGetClientProperties.cold.1
+ MRMediaRemoteGetIsGroupLeader.cold.1
+ MRMediaRemoteGetSavedAVRoutePassword.cold.1
+ MRMediaRemoteGetSavedAVRoutePassword.cold.2
+ MRMediaRemoteNowPlayingGetResolvedPlayerPathIsLocal.cold.1
+ MRMediaRemoteNowPlayingGetResolvedPlayerPathIsLocal.cold.2
+ MRMediaRemoteNowPlayingGetResolvedPlayerPathIsLocalSync.cold.1
+ MRMediaRemoteNowPlayingPlayerPathCreateError.cold.1
+ MRMediaRemoteRequestAirPlayGroupUID.cold.1
+ MRMediaRemoteRequestDeviceUID.cold.1
+ MRMediaRemoteRequestDeviceUID.cold.2
+ MRMediaRemoteRequestDeviceUID.cold.3
+ MRMediaRemoteRequestGroupUID.cold.1
+ MRMediaRemoteRequestIsGroupLeader.cold.1
+ MRMediaRemoteRequestIsGroupLeader.cold.2
+ MRMediaRemoteRequestIsGroupLeader.cold.3
+ MRMediaRemoteRequestSenderDefaultGroupUID.cold.1
+ MRMediaRemoteSendErrorFromError.cold.1
+ MRMediaRemoteSendErrorFromError.cold.2
+ MRMediaRemoteServiceBeginActivity.cold.1
+ MRMediaRemoteServiceCopyDeviceInfo.cold.2
+ MRMediaRemoteServiceCopyVirtualOutputDevices.cold.1
+ MRMediaRemoteServiceCreateDirectEndpointForDevices.cold.1
+ MRMediaRemoteServiceCreateGroupWithDevicesLeaderOptions.cold.1
+ MRMediaRemoteServiceCreateHostedEndpointForDevices.cold.1
+ MRMediaRemoteServiceDidInvalidateNotification_block_invoke.onceToken
+ MRMediaRemoteServiceEndActivity.cold.1
+ MRMediaRemoteServiceGroupDevicesAndSendCommand.cold.1
+ MRMediaRemoteServicePredictGroupLeader.cold.1
+ MRMediaRemoteServiceRemoveFromParentGroup.cold.1
+ MRMediaRemoteServiceSetPickedRouteVolumeControlCapabilities.cold.1
+ MRMediaRemoteServiceSetRecentAVOutputDeviceUID.cold.1
+ MRMediaRemoteServiceSetSavedAVRoutePassword.cold.1
+ MRMediaRemoteServiceUnpickAirPlayAVRoutes.cold.1
+ MRMediaRemoteServiceVirtualVoiceSetRecordingState.cold.1
+ MRMediaRemoteSetClientProperties.cold.1
+ MRMediaRemoteSetNowPlayingInfoForPlayer.cold.3
+ MRMediaRemoteSetPlayerProperties.cold.1
+ MRMediaRemoteUpdateClientProperties.cold.1
+ MRMediaRemoteUpdatePlayerProperties.cold.1
+ MRMusicHandoffSessionGetQueue.cold.1
+ MRNowPlayingClientAppendBundleIdentifier.cold.1
+ MRNowPlayingClientCopy.cold.1
+ MRNowPlayingClientCopyBundleIdentifierExtendedHierarchy.cold.1
+ MRNowPlayingClientCopyBundleIdentifierHierarchy.cold.1
+ MRNowPlayingClientCreateExternalRepresentation.cold.1
+ MRNowPlayingClientCreateSkeletonFrom.cold.1
+ MRNowPlayingClientEqualToClient.cold.1
+ MRNowPlayingClientEqualToClient.cold.2
+ MRNowPlayingClientGetBundleIdentifier.cold.1
+ MRNowPlayingClientGetHasAuxillaryProperties.cold.1
+ MRNowPlayingClientGetNowPlayingVisibility.cold.1
+ MRNowPlayingClientGetParentAppBundleIdentifier.cold.1
+ MRNowPlayingClientGetProcessIdentifier.cold.1
+ MRNowPlayingClientGetTintColor.cold.1
+ MRNowPlayingClientGetUserIdentifier.cold.1
+ MRNowPlayingClientMerge.cold.1
+ MRNowPlayingClientMerge.cold.2
+ MRNowPlayingClientSetBundleIdentifier.cold.1
+ MRNowPlayingClientSetNowPlayingVisibility.cold.1
+ MRNowPlayingClientSetParentAppBundleIdentifier.cold.1
+ MRNowPlayingClientSetProcessIdentifier.cold.1
+ MRNowPlayingClientSetTintColor.cold.1
+ MRNowPlayingClientSetUserIdentifier.cold.1
+ MRNowPlayingPlayerCopy.cold.1
+ MRNowPlayingPlayerCreateSkeletonFrom.cold.1
+ MRNowPlayingPlayerEqualToPlayer.cold.1
+ MRNowPlayingPlayerEqualToPlayer.cold.2
+ MRNowPlayingPlayerGetAudioSessionType.cold.1
+ MRNowPlayingPlayerGetDisplayName.cold.1
+ MRNowPlayingPlayerGetHasAuxillaryProperties.cold.1
+ MRNowPlayingPlayerGetIdentifier.cold.1
+ MRNowPlayingPlayerMerge.cold.1
+ MRNowPlayingPlayerMerge.cold.2
+ MRNowPlayingPlayerPathClientEqualToPlayerPathClient.cold.1
+ MRNowPlayingPlayerPathClientEqualToPlayerPathClient.cold.2
+ MRNowPlayingPlayerPathCopy.cold.1
+ MRNowPlayingPlayerPathCopyStringRepresentation.cold.1
+ MRNowPlayingPlayerPathCreateExternalRepresentation.cold.1
+ MRNowPlayingPlayerPathCreateSkeletonFrom.cold.1
+ MRNowPlayingPlayerPathEqualToPlayerPath.cold.1
+ MRNowPlayingPlayerPathEqualToPlayerPath.cold.2
+ MRNowPlayingPlayerPathGetClient.cold.1
+ MRNowPlayingPlayerPathGetIsResolved.cold.1
+ MRNowPlayingPlayerPathGetOrigin.cold.1
+ MRNowPlayingPlayerPathGetPlayer.cold.1
+ MRNowPlayingPlayerPathIsLocal.cold.1
+ MRNowPlayingPlayerPathResolveExternalDevicePlayerPath.cold.1
+ MRNowPlayingPlayerPathSetClient.cold.1
+ MRNowPlayingPlayerPathSetClient.cold.2
+ MRNowPlayingPlayerPathSetOrigin.cold.1
+ MRNowPlayingPlayerPathSetOrigin.cold.2
+ MRNowPlayingPlayerPathSetPlayer.cold.1
+ MRNowPlayingPlayerPathSetPlayer.cold.2
+ MRNowPlayingPlayerSetAudioSessionType.cold.1
+ MRNowPlayingPlayerSetDisplayName.cold.1
+ MRNowPlayingPlayerSetIdentifier.cold.1
+ MRNowPlayingSessionManagerIsSilentPrimary.cold.1
+ MRNowPlayingSessionManagerLocalDeviceRoutingContextID.cold.1
+ MRNowPlayingSessionManagerStartSession.cold.1
+ MRNowPlayingSessionManagerStopSession.cold.1
+ MROriginCopy.cold.1
+ MROriginCreateSkeletonFrom.cold.1
+ MROriginEqualToOrigin.cold.1
+ MROriginEqualToOrigin.cold.2
+ MROriginGetDisplayName.cold.1
+ MROriginGetOriginType.cold.1
+ MROriginGetUniqueIdentifier.cold.1
+ MROriginIsLocalOrigin.cold.1
+ MRPairedDeviceMerge.cold.1
+ MRPairedDeviceMerge.cold.2
+ MRPlaybackQueueRequestContainsNonDefaultAssets.cold.1
+ MRPlaybackQueueRequestCopy.cold.1
+ MRPlaybackQueueRequestCopyDescription.cold.1
+ MRPlaybackQueueRequestCopyWithCurrentState.cold.1
+ MRPlaybackQueueRequestCopyWithRange.cold.1
+ MRPlaybackQueueRequestCreateAssetsFrom.cold.1
+ MRPlaybackQueueRequestCreateExternalRepresentation.cold.1
+ MRPlaybackQueueRequestCreateMergedRequest.cold.1
+ MRPlaybackQueueRequestCreateSkeletonFrom.cold.1
+ MRPlaybackQueueRequestGetArtworkHeight.cold.1
+ MRPlaybackQueueRequestGetArtworkWidth.cold.1
+ MRPlaybackQueueRequestGetIncludeArtwork.cold.1
+ MRPlaybackQueueRequestGetIncludeInfo.cold.1
+ MRPlaybackQueueRequestGetIncludeLanguageOptions.cold.1
+ MRPlaybackQueueRequestGetIncludeLyrics.cold.1
+ MRPlaybackQueueRequestGetIncludeMetadata.cold.1
+ MRPlaybackQueueRequestGetIncludeSections.cold.1
+ MRPlaybackQueueRequestGetIsLegacyNowPlayingInfoRequest.cold.1
+ MRPlaybackQueueRequestGetLabel.cold.1
+ MRPlaybackQueueRequestGetRange.cold.1
+ MRPlaybackQueueRequestGetRequestID.cold.1
+ MRPlaybackQueueRequestGetRequestedIdentifiers.cold.1
+ MRPlaybackQueueRequestHasRange.cold.1
+ MRPlaybackQueueRequestIsExactMatch.cold.1
+ MRPlaybackQueueRequestIsExactMatch.cold.2
+ MRPlaybackQueueRequestMatch.cold.1
+ MRPlaybackQueueRequestMatch.cold.2
+ MRPlaybackQueueRequestMerge.cold.1
+ MRPlaybackQueueRequestMerge.cold.2
+ MRPlaybackQueueRequestRangeContainsNowPlayingItem.cold.1
+ MRPlaybackQueueRequestSetIncludeAlignments.cold.1
+ MRPlaybackQueueRequestSetIncludeArtwork.cold.1
+ MRPlaybackQueueRequestSetIncludeInfo.cold.1
+ MRPlaybackQueueRequestSetIncludeLanguageOptions.cold.1
+ MRPlaybackQueueRequestSetIsLegacyNowPlayingInfoRequest.cold.1
+ MRPlaybackQueueRequestSetLabel.cold.1
+ MRPlaybackQueueRequestSetRequestID.cold.1
+ MRPlaybackQueueRequestShouldRequestItem.cold.1
+ MRPlaybackQueueRequestShouldRequestItemNotConsideringMetadata.cold.1
+ MRProcessIsAirPlayDaemon.cold.1
+ MRProcessIsHomePodCannedDemo.cold.1
+ MRProcessIsMediaRemoteDaemon.cold.1
+ MRProcessIsMediaServerDaemon.cold.1
+ MRProcessIsUIService.cold.1
+ MRRegisterTransaction.cold.1
+ MRServiceClientPlaybackQueueRequestCallback.cold.1
+ MRServiceClientPlaybackQueueRequestCallback.cold.2
+ MRSupportsSystemUIActivities.cold.1
+ MRTelevisionGetCurrentRTISourceSession.cold.1
+ MRTelevisionGetCurrentRTISourceSession.cold.2
+ MRTelevisionGetCurrentRTISourceSession.cold.3
+ MRTelevisionGetCurrentRTISourceSession.cold.4
+ MRTelevisionGetCurrentTextEditingSession.cold.1
+ MRTelevisionGetCurrentTextEditingSession.cold.2
+ MRTelevisionGetCurrentTextEditingSession.cold.3
+ MRTelevisionGetCurrentTextEditingSession.cold.4
+ MRTelevisionGetGameControllerInputMode.cold.1
+ MRTelevisionGetGameControllerInputMode.cold.2
+ MRTelevisionGetHiliteMode.cold.1
+ MRTelevisionGetHiliteMode.cold.2
+ MRTelevisionProcessVirtualVoiceInputAudioData.cold.1
+ MRTelevisionProcessVirtualVoiceInputAudioData.cold.2
+ MRTelevisionRegisterGameController.cold.1
+ MRTelevisionRegisterGameController.cold.2
+ MRTelevisionRegisterGameController.cold.3
+ MRTelevisionRegisterGameControllerWithProperties.cold.1
+ MRTelevisionRegisterGameControllerWithProperties.cold.2
+ MRTelevisionRegisterGameControllerWithProperties.cold.3
+ MRTelevisionRegisterGameControllerWithProperties.cold.4
+ MRTelevisionRegisterGameControllerWithProperties.cold.5
+ MRTelevisionRegisterVirtualTouchDevice.cold.1
+ MRTelevisionRegisterVirtualTouchDevice.cold.2
+ MRTelevisionRegisterVirtualTouchDevice.cold.3
+ MRTelevisionRegisterVirtualTouchDevice.cold.4
+ MRTelevisionRegisterVirtualVoiceInputDevice.cold.1
+ MRTelevisionRegisterVirtualVoiceInputDevice.cold.2
+ MRTelevisionRegisterVirtualVoiceInputDevice.cold.3
+ MRTelevisionRegisterVirtualVoiceInputDevice.cold.4
+ MRTelevisionRequestHiliteModeExit.cold.1
+ MRTelevisionRequestHiliteModeExit.cold.2
+ MRTelevisionSendGameControllerEvent.cold.1
+ MRTelevisionSendGameControllerEvent.cold.2
+ MRTelevisionSendGameControllerEventV2.cold.1
+ MRTelevisionSendGameControllerEventV2.cold.2
+ MRTelevisionSendGameControllerEventV2.cold.3
+ MRTelevisionSendGameControllerEventV2.cold.4
+ MRTelevisionSendHIDEvent.cold.1
+ MRTelevisionSendHIDEvent.cold.2
+ MRTelevisionSendVirtualTouchEvent.cold.1
+ MRTelevisionSendVirtualTouchEvent.cold.2
+ MRTelevisionServiceGetEndpoint.cold.1
+ MRTelevisionServiceSetCustomDataCallback.cold.1
+ MRTelevisionSetGameControllerInputModeCallback.cold.1
+ MRTelevisionSetGameControllerInputModeCallback.cold.2
+ MRTelevisionSetGameControllerPropertiesCallback.cold.1
+ MRTelevisionSetGameControllerPropertiesCallback.cold.2
+ MRTelevisionSetHiliteModeCallback.cold.1
+ MRTelevisionSetHiliteModeCallback.cold.2
+ MRTelevisionSetRTICallback.cold.1
+ MRTelevisionSetRTICallback.cold.2
+ MRTelevisionSetTextEditingCallback.cold.1
+ MRTelevisionSetTextEditingCallback.cold.2
+ MRTelevisionSetVoiceRecordingStateCallback.cold.1
+ MRTelevisionSetVoiceRecordingStateCallback.cold.2
+ MRTelevisionTextEditingClearText.cold.1
+ MRTelevisionTextEditingClearText.cold.2
+ MRTelevisionTextEditingDeleteBackward.cold.1
+ MRTelevisionTextEditingDeleteBackward.cold.2
+ MRTelevisionTextEditingInsert.cold.1
+ MRTelevisionTextEditingInsert.cold.2
+ MRTelevisionTextEditingSetText.cold.1
+ MRTelevisionTextEditingSetText.cold.2
+ MRTelevisionUnregisterGameController.cold.1
+ MRTelevisionUnregisterGameController.cold.2
+ MRTelevisionWake.cold.1
+ MRTelevisionWake.cold.2
+ MRTimeUtilitiesGetProcessorTimeScale.cold.1
+ MRTimeUtilsGetCurrentNanoseconds.cold.1
+ MRVirtualVoiceInputDeviceDescriptorSetDefaultAudioFormat.cold.1
+ MRVirtualVoiceInputDeviceDescriptorSetSupportedFormats.cold.1
+ OBJC_IVAR_$_MRAVConcreteOutputContext._avOutputContextLock
+ OBJC_IVAR_$_MRAVConcreteOutputContext._canSetVolume
+ OBJC_IVAR_$_MRAVConcreteOutputContext._effectiveVolumeCapabilities
+ OBJC_IVAR_$_MRAVConcreteOutputContext._supportsVolumeControl
+ OBJC_IVAR_$_MRAVConcreteOutputContext._volumeControlType
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._groupUIDOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._uidOverride
+ OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._reloadRateLimiter
+ OBJC_IVAR_$_MRAVOutputDevice._alternateTransportType
+ OBJC_IVAR_$_MRAVOutputDeviceSourceInfo._sourceType
+ OBJC_IVAR_$_MRActiveRoutesObserver._activeRouteIDsChangedCallback
+ OBJC_IVAR_$_MRActiveRoutesObserver._isLocalDeviceAirPlayActiveCallback
+ OBJC_IVAR_$_MRActiveRoutesObserver._localDeviceAirPlayActive
+ OBJC_IVAR_$_MRContentItemMetadata._subtitleShort
+ OBJC_IVAR_$_MRExternalDeviceTransportConnection._dataSource
+ OBJC_IVAR_$_MRGroupComposition._earPodCount
+ OBJC_IVAR_$_MRNowPlayingControllerConfiguration._artworkOnly
+ OBJC_IVAR_$_MRNowPlayingOriginClientRequests._callOutQueue
+ OBJC_IVAR_$_MRNowPlayingOriginClientRequests._deviceInfoLock
+ OBJC_IVAR_$_MRPlaybackSessionRequest._destinationCommandInfo
+ OBJC_IVAR_$_MRPlaybackSessionRequest._destinationPlayerPath
+ OBJC_IVAR_$_MRProtocolClientConnection._replyQueue
+ OBJC_IVAR_$_MRProtocolClientConnection._sendQueue
+ OBJC_IVAR_$__MRAVOutputDeviceDescriptorProtobuf._alternateTransportType
+ OBJC_IVAR_$__MRCommandInfoProtobuf._playbackSessionRequirements
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._delegateAccountData
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._delegateAccountDataType
+ OBJC_IVAR_$__MRContentItemMetadataProtobuf._subtitleShort
+ OBJC_IVAR_$__MRPSMRecipe._destinationSetPlaybackSessionCommandInfo
+ OBJC_IVAR_$__MRPSMRecipe._error
+ OBJC_IVAR_$__MRPSMRecipe._playbackSessionType
+ OBJC_IVAR_$__MRPSMRecipe._type
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._destinationCommandInfo
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._destinationPlayerPath
+ OBJC_IVAR_$__MRSendCommandResultProtobuf._error
+ _AVOutputDeviceCommunicationChannelDataDestinationMediaRemoteFunction
+ _MRAVOutputDeviceB238ModelIDPrefix
+ _MRAVOutputDeviceB515CModelID
+ _MRAVOutputDeviceB515CWiredModelID
+ _MRAVOutputDeviceB520ModelIDPrefix
+ _MRAVOutputDeviceB620ModelIDPrefix
+ _MRAVOutputDeviceB825ModelID
+ _MRCUPSHideSetupCodeCallback.cold.1
+ _MRCUPSPromptForSetupCodeCallback.cold.1
+ _MRCUPSShowSetupCodeCallback.cold.1
+ _MRGroupSessionMediaAccountHostingStateToString
+ _MRHandlePlaybackQueueRequest.cold.2
+ _MRHandlePlaybackQueueRequest.cold.3
+ _MRHandlePlaybackQueueRequest.cold.4
+ _MRHandlePlaybackQueueRequest.cold.5
+ _MRLoadContentItemAssets.cold.1
+ _MRLoadContentItemAssets.cold.2
+ _MRLoadContentItemAssets.cold.3
+ _MRLogForCategory.cold.2
+ _MRMediaRemoteCommandOptionsSerialization.cold.1
+ _MRMediaRemoteCommandRequiresNowPlayingItemValidation
+ _MRMediaRemoteGetDeviceUIDWithRetryIntervals.cold.2
+ _MRMediaRemoteGetProactiveRecommendedPlayer
+ _MRMediaRemotePlaybackSessionIsMigrationPossible
+ _MRMediaRemotePlaybackSessionMigrateFromOriginToOrigin
+ _MRMediaRemoteProactiveRecommendedPlayerDidChangeNotification
+ _MRMediaRemoteProactiveRecommendedPlayerReasonUserInfoKey
+ _MRMediaRemoteServiceGetProactiveRecommendedPlayer
+ _MRNowPlayingInfoDictionaryKeyToProtobufKeyMapping.cold.1
+ _MRNowPlayingInfoSerialization.cold.1
+ _MROutputDeviceIsAVOutputDeviceLocalWithDeviceInfo
+ _MRPSMDetermineRecipe.cold.1
+ _MRProtoUtilsPlistTypeFromProtoValue.cold.1
+ _MRProtoUtilsProtoDictionaryFromNSDictionary.cold.1
+ _MRProtoUtilsProtoValueFromPlistType.cold.1
+ _MRRequestPlaybackQueue.cold.1
+ _MRRequestPlaybackQueue.cold.2
+ _MRRequestPlaybackQueue.cold.3
+ _MRResolveAndRequestPlaybackQueue.cold.1
+ _MRResolveAndRequestPlaybackQueue.cold.2
+ _MRTypeAuditCreateNumberFromString.cold.1
+ _MRTypeAuditDictionaryApplierFunction.cold.1
+ _MRUserSettingsSystemVolumeCapabilitiesDidChangeContext
+ _MRUserSettingsSystemVolumeCapabilitiesOverrideDidChange
+ _MRUserSettingsSystemVolumeDidChangeContext
+ _MRUserSettingsSystemVolumeOverrideDidChange
+ _MSVAutoBugCaptureDomainMediaRemote
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$__MRPSMRecipe
+ _OBJC_METACLASS_$__MRPSMRecipe
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.712
+ __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.716
+ __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.717
+ __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.726
+ __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.733
+ __106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.657
+ __122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.670
+ __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.690
+ __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.697
+ __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.702
+ __122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.280
+ __122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.292
+ __39-[MRDistantExternalDevice customOrigin]_block_invoke.233
+ __39-[MRDistantExternalDevice customOrigin]_block_invoke_2.235
+ __41-[MRLegacyController setupExternalDevice]_block_invoke.11
+ __46-[MRTransactionPacketAccumulator mergePacket:]_block_invoke.cold.1
+ __46-[MRXPCConnection addCustomXPCHandler:forKey:]_block_invoke.cold.1
+ __47-[MRAVConcreteOutputDevice _loadLocalOverrides]_block_invoke.15
+ __47-[MROutputContextController _inititalizeVolume]_block_invoke.317
+ __47-[MROutputContextController _inititalizeVolume]_block_invoke.321
+ __47-[MROutputContextController _inititalizeVolume]_block_invoke.325
+ __47-[MRV2NowPlayingController beginLoadingUpdates]_block_invoke.cold.1
+ __48-[MRAVDistantEndpoint setDistantExternalDevice:]_block_invoke.cold.1
+ __48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.341
+ __52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.499
+ __52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.503
+ __52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.506.cold.1
+ __52-[MRNowPlayingSessionServiceClient initWithService:]_block_invoke.cold.1
+ __53-[MRCoreUtilsPairingSession deleteIdentityWithError:]_block_invoke.cold.1
+ __54-[MRUserSettings nowPlayingAppStackFailedPlayInterval]_block_invoke.cold.1
+ __57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.537
+ __57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.543
+ __57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.546.cold.1
+ __57-[MRProtocolClientConnection _sendMessage:timeout:reply:]_block_invoke.33
+ __57-[MRProtocolClientConnection _sendMessage:timeout:reply:]_block_invoke.59
+ __58-[MRNowPlayingPlayerClient resolveCommandOptions:options:]_block_invoke.cold.1
+ __60+[MRActiveRoutesObserver fetchActiveRouteIDsWithCompletion:]_block_invoke.31
+ __60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke.58
+ __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.554
+ __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.555
+ __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.562
+ __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_2.563
+ __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.11
+ __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.12
+ __61-[MRDistantExternalDevice setHostedExternalDeviceConnection:]_block_invoke.162.cold.1
+ __61-[MROutputContextController _onSerialQueue_localOutputDevice]_block_invoke.310
+ __61-[MROutputContextController _onSerialQueue_localOutputDevice]_block_invoke.cold.1
+ __63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.644
+ __63-[MRMediaRemoteServiceClient addPlayerPathInvalidationHandler:]_block_invoke.94
+ __63-[MRMediaRemoteServiceClient addPlayerPathInvalidationHandler:]_block_invoke.cold.1
+ __64-[MRAVRoutingDiscoverySession logEndpointsChanged:oldEndpoints:]_block_invoke.143
+ __64-[MRAVRoutingDiscoverySession logEndpointsChanged:oldEndpoints:]_block_invoke_2.144
+ __64-[MRAVRoutingDiscoverySession logEndpointsChanged:oldEndpoints:]_block_invoke_3.147
+ __65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.349
+ __66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.270
+ __66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.273
+ __66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.358
+ __66-[MRExternalOutputContextDataSource updateVolume:outputDeviceUID:]_block_invoke.167
+ __66-[MROutputContextController adjustVolume:outputDeviceUID:details:]_block_invoke.276
+ __67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.618
+ __67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.611
+ __67-[MRAVEndpoint removeOutputDeviceFromParentGroup:queue:completion:]_block_invoke.cold.1
+ __67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.345
+ __68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.39
+ __68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.42
+ __69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.359
+ __69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.360
+ __70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.674
+ __70-[MRAVOutputContext _compareOutputDeviceList:withNewOutputDeviceList:]_block_invoke.cold.1
+ __71-[MRNowPlayingOriginClient _prepareToRestoreClientStateWithCompletion:]_block_invoke_2.cold.1
+ __72-[MRAVRoutingDiscoverySession logOutputDevicesChanged:oldOutputDevices:]_block_invoke.125
+ __72-[MRAVRoutingDiscoverySession logOutputDevicesChanged:oldOutputDevices:]_block_invoke_2.126
+ __72-[MRAVRoutingDiscoverySession logOutputDevicesChanged:oldOutputDevices:]_block_invoke_3.129
+ __74-[MRNowPlayingOriginClientRequests handleDeviceInfoRequestWithCompletion:]_block_invoke.27
+ __75-[MRDistantExternalDevice requestGroupSessionWithDetails:queue:completion:]_block_invoke.299
+ __75-[MRDistantExternalDevice requestGroupSessionWithDetails:queue:completion:]_block_invoke_2.300
+ __76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.625
+ __76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.632
+ __76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke.79
+ __76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke.79.cold.1
+ __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.29
+ __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.33
+ __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.36
+ __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.37
+ __77-[MRAVEndpoint _setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.cold.1
+ __77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.525
+ __77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.346
+ __78-[MRAVEndpoint _muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.cold.1
+ __79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.67
+ __79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.513
+ __79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.352
+ __80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.44
+ __80-[MRAVEndpoint _adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.cold.1
+ __80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.355
+ __83-[MRNowPlayingPlayerClientRequests _handleEnqueuedPlaybackQueueRequest:completion:]_block_invoke.cold.1
+ __86-[MRV2NowPlayingController _requestPlaybackQueueArtworkForIdentifiers:operationQueue:]_block_invoke_2.cold.1
+ __90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.310
+ __91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.351
+ __91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.327
+ __91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.330
+ __93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.318
+ __93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.321
+ __96-[MRAVOutputContext _notifyChangesInOutputDevicesWithAdded:removed:updated:previous:newDevices:]_block_invoke.153
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.101
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.105
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.121
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.150
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.150.cold.1
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.160
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.172
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.178
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.180
+ __MRAVEndpointModifyOutputDevicesInGroup_block_invoke_2.cold.1
+ __MRAnalyticsTrackTopologyChangeEvent_block_invoke.cold.1
+ __MRDictionaryCalculateDeltas_block_invoke.507
+ __MRMediaRemoteGetClientProperties_block_invoke.539
+ __MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.586
+ __MRMediaRemoteGetPlayerProperties_block_invoke.570
+ __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke.26
+ __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke.30
+ __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.27
+ __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.31
+ __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.31.cold.1
+ __MRMediaRemotePlaybackSessionMigrateForOriginWithRequest_block_invoke_2.cold.1
+ __MRMediaRemoteRequestDeviceUID_block_invoke.422
+ __MRMediaRemoteRequestIsGroupLeader_block_invoke.437
+ __MRMediaRemoteSetWantsWakingNowPlayingNotifications_block_invoke.605
+ __MRNowPlayingSessionManagerStartSession_block_invoke.cold.2
+ __MRPSMDetermineRecipe
+ __MRPSMPerformLegacyMigration
+ __MRPSMPerformOneShotMigration
+ __MRServiceClientRemotePlayerPathCommandCallback_block_invoke.118
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS__MRPSMRecipe
+ __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions|MRDeviceInfoOutputDeviceAdditions)
+ __OBJC_$_INSTANCE_METHODS__MRPSMRecipe
+ __OBJC_$_INSTANCE_VARIABLES__MRPSMRecipe
+ __OBJC_$_PROP_LIST__MRPSMRecipe
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRExternalDeviceTransportConnectionDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRExternalDeviceTransportConnectionDataSource
+ __OBJC_$_PROTOCOL_REFS_MRExternalDeviceTransportConnectionDataSource
+ __OBJC_CLASS_PROTOCOLS_$_MRRapportTransportConnection
+ __OBJC_CLASS_RO_$__MRPSMRecipe
+ __OBJC_LABEL_PROTOCOL_$_MRExternalDeviceTransportConnectionDataSource
+ __OBJC_METACLASS_RO_$__MRPSMRecipe
+ __OBJC_PROTOCOL_$_MRExternalDeviceTransportConnectionDataSource
+ __UTTypeAppleTV
+ __UTTypeHomePod
+ ___23-[MRRateLimiter update]_block_invoke
+ ___23-[MRRateLimiter update]_block_invoke_2
+ ___35-[MRUserSettings sonicMusicEnabled]_block_invoke
+ ___38-[MRUserSettings sonicPodcastsEnabled]_block_invoke
+ ___38-[MRUserSettings systemVolumeOverride]_block_invoke
+ ___40-[MRActiveRoutesObserver _reevaluateAPA]_block_invoke
+ ___40-[MRActiveRoutesObserver _reevaluateASE]_block_invoke
+ ___42-[MRUserSettings supportLastPlayingDevice]_block_invoke
+ ___43+[MRAVRoutingDiscoverySession loggingQueue]_block_invoke
+ ___46-[MRUserSettings shouldConnectToLocalEndpoint]_block_invoke
+ ___47-[MRAVConcreteOutputDevice _loadLocalOverrides]_block_invoke
+ ___49-[MROutputContextDataSource outputDevicesForUID:]_block_invoke
+ ___50-[MRAVConcreteOutputContext supportsVolumeControl]_block_invoke
+ ___50-[MRUserSettings systemVolumeCapabilitiesOverride]_block_invoke
+ ___51-[MRNowPlayingOriginClientRequests initWithOrigin:]_block_invoke
+ ___54-[MRAVConcreteRoutingDiscoverySession _scheduleReload]_block_invoke
+ ___54-[MRActiveRoutesObserver _onWorkerQueue_reevaluateASE]_block_invoke
+ ___57-[MRProtocolClientConnection _sendMessage:timeout:reply:]_block_invoke
+ ___57-[MRProtocolClientConnection _sendMessage:timeout:reply:]_block_invoke_2
+ ___60-[MRProtocolClientConnection initWithConnection:replyQueue:]_block_invoke
+ ___61-[MRAVConcreteRoutingDiscoverySession initWithConfiguration:]_block_invoke
+ ___64-[MRAVRoutingDiscoverySession logEndpointsChanged:oldEndpoints:]_block_invoke_4
+ ___64-[MRActiveRoutesObserver initWithActiveRouteIDsChangedCallback:]_block_invoke
+ ___68+[MRAVOutputDeviceSymbolProvider compositionForClusterOutputDevice:]_block_invoke
+ ___68+[MRAVOutputDeviceSymbolProvider compositionForClusterOutputDevice:]_block_invoke_2
+ ___70-[MROutputContextController _handleOutputDeviceDidChangeNotification:]_block_invoke_2
+ ___70-[MROutputContextController _handleOutputDevicesReloadedNotification:]_block_invoke
+ ___72-[MRAVRoutingDiscoverySession logOutputDevicesChanged:oldOutputDevices:]_block_invoke_4
+ ___81-[MRDeviceInfoOutputDevice initWithDeviceInfo:fallbackOutputDevice:forExporting:]_block_invoke
+ ___83-[MRAVConcreteOutputContext _handleOutputContextCanSetVolumeDidChangeNotification:]_block_invoke
+ ___85-[MRAVConcreteOutputContext _handleOutputContextSupportsVolumeDidChangeNotification:]_block_invoke
+ ___88-[MRAVConcreteOutputContext _handleOutputContextVolumeControlTypeDidChangeNotification:]_block_invoke
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke_2
+ ___MRMediaRemoteBundle_block_invoke
+ ___MRMediaRemoteCommandOptionsSerialization_block_invoke_2.cold.1
+ ___MRMediaRemoteCommandOptionsSerialization_block_invoke_3.cold.1
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.427
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.430
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.430.cold.1
+ ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.431
+ ___MRMediaRemoteGetProactiveRecommendedPlayer_block_invoke
+ ___MRMediaRemotePlaybackSessionIsMigrationPossible_block_invoke
+ ___MRMediaRemotePlaybackSessionMigrateForOriginWithRequest_block_invoke
+ ___MRMediaRemotePlaybackSessionMigrateForOriginWithRequest_block_invoke_2
+ ___MRMediaRemotePlaybackSessionMigrateFromOriginToOrigin_block_invoke
+ ___MRMediaRemoteServiceGetProactiveRecommendedPlayer_block_invoke
+ ___MRPSMDetermineRecipe_block_invoke.235
+ ___MRPSMDetermineRecipe_block_invoke.239
+ ___MRPSMDetermineRecipe_block_invoke_2.236
+ ___MRPSMPerformLegacyMigration_block_invoke.106
+ ___MRPSMPerformLegacyMigration_block_invoke.122
+ ___MRPSMPerformLegacyMigration_block_invoke.125
+ ___MRPSMPerformLegacyMigration_block_invoke.128
+ ___MRPSMPerformLegacyMigration_block_invoke.132
+ ___MRPSMPerformLegacyMigration_block_invoke.140
+ ___MRPSMPerformLegacyMigration_block_invoke.148
+ ___MRPSMPerformLegacyMigration_block_invoke.160
+ ___MRPSMPerformLegacyMigration_block_invoke.168
+ ___MRPSMPerformLegacyMigration_block_invoke_2.107
+ ___MRPSMPerformLegacyMigration_block_invoke_2.133
+ ___MRPSMPerformLegacyMigration_block_invoke_2.144
+ ___MRPSMPerformLegacyMigration_block_invoke_2.156
+ ___MRPSMPerformLegacyMigration_block_invoke_2.165
+ ___MRPSMPerformLegacyMigration_block_invoke_2.165.cold.1
+ ___MRPSMPerformLegacyMigration_block_invoke_2.172
+ ___MRPSMPerformLegacyMigration_block_invoke_3.111
+ ___MRPSMPerformLegacyMigration_block_invoke_3.137
+ ___MRPSMPerformLegacyMigration_block_invoke_3.173
+ ___MRPSMPerformLegacyMigration_block_invoke_4.112
+ ___MRPSMPerformLegacyMigration_block_invoke_4.174
+ ___MRPSMPerformLegacyMigration_block_invoke_5.113
+ ___MRPSMPerformLegacyMigration_block_invoke_6.118
+ ___MRPSMPerformLegacyMigration_block_invoke_7.119
+ ___MRPSMPerformLegacyMigration_block_invoke_8.120
+ ___MRPSMPerformOneShotMigration_block_invoke.74
+ ___MRPSMPerformOneShotMigration_block_invoke.78
+ ___MRPSMPerformOneShotMigration_block_invoke.85
+ ___MRPSMPerformOneShotMigration_block_invoke.93
+ ___MRPSMPerformOneShotMigration_block_invoke_2.75
+ ___MRPSMPerformOneShotMigration_block_invoke_2.82
+ ___MRPSMPerformOneShotMigration_block_invoke_2.89
+ ___MRPSMPerformOneShotMigration_block_invoke_2.94
+ ___MRServiceClientOriginCommandCallback_block_invoke.54.cold.1
+ ___MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.73.cold.1
+ ___MRServiceClientRemoteResolvedPlayerPathCommandCallbacks_block_invoke.93
+ ___MRServiceClientRemoteResolvedPlayerPathCommandCallbacks_block_invoke_2.94
+ ___MRServiceClientRemoteResolvedPlayerPathCommandCallbacks_block_invoke_3.98
+ ____MRPSMDetermineRecipe_block_invoke
+ ____MRPSMDetermineRecipe_block_invoke_2
+ ____MRPSMDetermineRecipe_block_invoke_3
+ ____MRPSMPerformLegacyMigration_block_invoke
+ ____MRPSMPerformLegacyMigration_block_invoke_2
+ ____MRPSMPerformLegacyMigration_block_invoke_3
+ ____MRPSMPerformLegacyMigration_block_invoke_4
+ ____MRPSMPerformLegacyMigration_block_invoke_5
+ ____MRPSMPerformLegacyMigration_block_invoke_6
+ ____MRPSMPerformLegacyMigration_block_invoke_7
+ ____MRPSMPerformLegacyMigration_block_invoke_8
+ ____MRPSMPerformOneShotMigration_block_invoke
+ ____MRPSMPerformOneShotMigration_block_invoke_2
+ ____MRPSMPerformOneShotMigration_block_invoke_3
+ ___block_descriptor_104_e8_32s40s48bs56r64r72r80r88r96r_e5_v8?0l
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s_e19_"NSDictionary"8?0l
+ ___block_descriptor_32_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_40_e8_32bs_e35_v24?0"MRPlayerPath"8"NSString"16l
+ ___block_descriptor_40_e8_32bs_e51_v32?0"MRPlayerPath"8"MRPlayerPath"16"NSError"24l
+ ___block_descriptor_40_e8_32bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24l
+ ___block_descriptor_40_e8_32s_e24_16?0"AVOutputDevice"8l
+ ___block_descriptor_41_e8_32s_e26_16?0"MRAVOutputDevice"8l
+ ___block_descriptor_48_e8_32bs40bs_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"MRDeviceInfo"8"NSError"16l
+ ___block_descriptor_56_e8_32s40r48r_e35_v24?0^{__CFArray=}8^{__CFError=}16l
+ ___block_descriptor_62_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e44_v32?0Q8"MRAVEndpoint"16?<v?"NSError">24l
+ ___block_descriptor_65_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_68_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_72_e8_32bs40bs48r56r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e69_v32?0"AVOutputDeviceCommunicationChannel"8"NSError"16"NSString"24l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e56_v32?0"MRPlayerPath"8"MRPlayerPath"16"_MRPSMRecipe"24l
+ ___block_descriptor_72_e8_32s40s48s56s64r_e24_v16?0?<v?"NSError">8l
+ ___block_descriptor_72_e8_32s40s48s56s_e52_v24?0"NSString"8?<v?"MRAVEndpoint""NSError">16l
+ ___block_descriptor_84_e8_32s40s48s56s64bs_e17_v16?0"NSError"8l
+ ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e36_v24?0"AVOutputDevice"8"NSError"16l
+ ___block_descriptor_96_e8_32r40r48r56r64r72r80r88r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e34_v24?0"MRAVEndpoint"8"NSError"16l
+ ___copy_helper_block_e8_32b40b48r56r
+ ___copy_helper_block_e8_32b40r
+ ___copy_helper_block_e8_32r40r48r56r64r72r80r88r
+ ___copy_helper_block_e8_32s40s48b56r64r72r80r88r96r
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r
+ __block_literal_global.128
+ __block_literal_global.132
+ __block_literal_global.133
+ __block_literal_global.136
+ __block_literal_global.139
+ __block_literal_global.142
+ __block_literal_global.149
+ __block_literal_global.151
+ __block_literal_global.189
+ __block_literal_global.195
+ __block_literal_global.198
+ __block_literal_global.204
+ __block_literal_global.209
+ __block_literal_global.220
+ __block_literal_global.228
+ __block_literal_global.231
+ __block_literal_global.233
+ __block_literal_global.249
+ __block_literal_global.278
+ __block_literal_global.304
+ __block_literal_global.312
+ __block_literal_global.425
+ __block_literal_global.500
+ __block_literal_global.503
+ __block_literal_global.545
+ __block_literal_global.548
+ __block_literal_global.570
+ __block_literal_global.661
+ __block_literal_global.684
+ __block_literal_global.97
+ _constantValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
+ _getAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
+ _initValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote
+ _kMRMediaRemoteCommandInfoPlaybackSessionRequirements
+ _kMRMediaRemoteOptionDelegateAccountData
+ _kMRMediaRemoteOptionDelegateAccountDataType
+ _objc_msgSend$_notify
+ _objc_msgSend$_onReloadQueue_createOutputDevicesFromAVOutputDevices:
+ _objc_msgSend$_onReloadQueue_fetchOutputDevicesFromDiscoverySession:
+ _objc_msgSend$_onReloadQueue_reload
+ _objc_msgSend$_onReloadQueue_reloadAvailableOutputDevices
+ _objc_msgSend$_onWorkerQueue_reevaluateAPA
+ _objc_msgSend$_onWorkerQueue_reevaluateASE
+ _objc_msgSend$_reevaluateAPA
+ _objc_msgSend$_reevaluateASE
+ _objc_msgSend$activeRouteIDsChangedCallback
+ _objc_msgSend$addHomePodWithModelIdentifier:
+ _objc_msgSend$afterRoutingCompleteTimeout
+ _objc_msgSend$alternateTransportType
+ _objc_msgSend$dataSource
+ _objc_msgSend$destinationCommandInfo
+ _objc_msgSend$destinationSetPlaybackSessionCommandInfo
+ _objc_msgSend$earPodCount
+ _objc_msgSend$groupSessionDelayedInitializationEnabled
+ _objc_msgSend$hasPlaybackSessionRequirements
+ _objc_msgSend$homePodHomeTheaterCompositionWithHomePodModelIdentifier:
+ _objc_msgSend$homePodStereoPairCompositionWithModelIdentifier:
+ _objc_msgSend$initWithActiveRouteIDsChangedCallback:isLocalDeviceAirplayActiveChangedCallback:
+ _objc_msgSend$initWithInputStream:outputStream:dataSource:
+ _objc_msgSend$initWithMultipleBuiltInDevices:sourceType:
+ _objc_msgSend$isArtworkOnly
+ _objc_msgSend$isB515CDevice
+ _objc_msgSend$isB825Device
+ _objc_msgSend$isLocalDeviceAirPlayActiveCallback
+ _objc_msgSend$legacySetPlaybackSessionWithSessionType:
+ _objc_msgSend$loggingQueue
+ _objc_msgSend$msv_compactDescription
+ _objc_msgSend$notPossibleWithError:
+ _objc_msgSend$oneShotSetPlaybackSessionWithCommandInfo:
+ _objc_msgSend$openCommunicationChannelToDestination:options:completionHandler:
+ _objc_msgSend$outputDevicesForUID:
+ _objc_msgSend$playbackSessionRequirements
+ _objc_msgSend$playbackSessionType
+ _objc_msgSend$replyQueue
+ _objc_msgSend$sendQueue
+ _objc_msgSend$setActiveRouteIDsChangedCallback:
+ _objc_msgSend$setAlternateTransportType:
+ _objc_msgSend$setClusterCompositions:
+ _objc_msgSend$setDelegateAccountData:
+ _objc_msgSend$setDelegateAccountDataType:
+ _objc_msgSend$setDestinationCommandInfo:
+ _objc_msgSend$setEarPodCount:
+ _objc_msgSend$setHasIsLocalDevice:
+ _objc_msgSend$setIsLocalDeviceAirPlayActive:
+ _objc_msgSend$setIsLocalDeviceAirPlayActiveCallback:
+ _objc_msgSend$setPlaybackSessionRequirements:
+ _objc_msgSend$setSubtitleShort:
+ _objc_msgSend$sourceType
+ _objc_msgSend$subtitleShort
+ _objc_msgSend$symbolNameForType:fillVariant:
+ _objc_msgSend$symbolNameForType:fillVariant:otherVariantOptions:
+ _objc_msgSend$transportTypeForTransport:
+ _objc_msgSend$update
+ _onClientQueue_MRCreatePlaybackQueueForOffset.cold.1
+ _onClientQueue_MRCreateSectionsForRequest.cold.1
+ _onClientQueue_MRCreateSectionsForRequest.cold.2
+ _onClientQueue_MRCreateSectionsForRequest.cold.3
+ _onClientQueue_MRCreateSectionsForRequest.cold.4
+ _onClientQueue_MRInvokeClientCallback.cold.1
+ _onClientQueue_MRInvokeClientCallback.cold.2
+ _onClientQueue_MRInvokeClientCallback.cold.3
+ _onClientQueue_MRInvokeClientCallback.cold.4
+ _onClientQueue_MRInvokeClientCallback.cold.5
+ _onClientQueue_MRInvokeClientCallback.cold.6
+ _onQueue_MRCreatePlaybackQueueForIdentifier.cold.1
+ _onQueue_MRCreatePlaybackQueueForOffset.cold.1
+ _onQueue_MRCreatePlaybackQueueForRequest.cold.1
+ _onQueue_MRCreateSectionsForRequest.cold.1
+ _onQueue_MRCreateSectionsForRequest.cold.2
+ _onQueue_MRCreateSectionsForRequest.cold.3
+ _onQueue_MRHandlePlaybackQueueRequest.cold.1
+ _onQueue_MRHandlePlaybackQueueRequest.cold.2
+ _onQueue_MRHandlePlaybackQueueRequest.cold.3
+ _onQueue_MRHandlePlaybackQueueRequest.cold.4
+ _onQueue_MRInvokeClientAssetCallbacks.cold.2
+ _onQueue_MRInvokeClientAssetCallbacks.cold.3
+ _onQueue_MRInvokeClientAssetCallbacks.cold.4
+ _onQueue_MRInvokeClientCallbacks.cold.2
+ _onQueue_MRInvokeClientCallbacks.cold.3
+ _onQueue_MRInvokeClientCallbacks.cold.4
+ _onQueue_MRInvokeClientCallbacks.cold.5
+ _onQueue_MRInvokeClientCallbacks.cold.6
+ _onQueue_MRLoadContentItemAssets.cold.1
+ _onQueue_MRLoadContentItemAssets.cold.2
+ initAPSCopyDefaultGroupUUID.cold.1
+ initAPSParseGroupID.cold.1
+ initAVAudioSession.cold.1
+ initAVOutputContext.cold.1
+ initAVOutputDevice.cold.1
+ initAVOutputDeviceDiscoverySession.cold.1
+ initAVPairedDevice.cold.1
+ initCURunLoopThread.cold.1
+ initFBSDisplayLayoutMonitor.cold.1
+ initFBSDisplayLayoutMonitorConfiguration.cold.1
+ initMKBDeviceUnlockedSinceBoot.cold.1
+ initPLLogRegisteredEvent.cold.1
+ initTUConversationManager.cold.1
+ initValAVAudioSessionRoutingContextChangeNotification.cold.1
+ initValAVOutputContextCanSetVolumeDidChangeNotification.cold.1
+ initValAVOutputContextDestinationChangeInitiatedNotification.cold.1
+ initValAVOutputContextDestinationChangePreviousDeviceIDsKey.cold.1
+ initValAVOutputContextDestinationChangeReasonIdleDisconnect.cold.1
+ initValAVOutputContextDestinationChangeReasonKey.cold.1
+ initValAVOutputContextOutputDeviceDidChangeNotification.cold.1
+ initValAVOutputContextOutputDevicesDidChangeNotification.cold.1
+ initValAVOutputContextPredictedOutputDeviceDidChangeNotification.cold.1
+ initValAVOutputContextPredictedOutputDevicesDidChangeNotification.cold.1
+ initValAVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification.cold.1
+ initValAVOutputContextTypeSharedAudioPresentation.cold.1
+ initValAVOutputContextTypeSharedSystemAudio.cold.1
+ initValAVOutputContextTypeSharedSystemScreen.cold.1
+ initValAVOutputContextVolumeControlTypeDidChangeNotification.cold.1
+ initValAVOutputDeviceActivatedClusterMembersRoomIDKey.cold.1
+ initValAVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification.cold.1
+ initValAVOutputDeviceBatteryLevelCaseKey.cold.1
+ initValAVOutputDeviceBatteryLevelLeftKey.cold.1
+ initValAVOutputDeviceBatteryLevelRightKey.cold.1
+ initValAVOutputDeviceCanMuteDidChangeNotification.cold.1
+ initValAVOutputDeviceCanSetVolumeDidChangeNotification.cold.1
+ initValAVOutputDeviceClusterMemberVolumeControlTypeDidChangeNotification.cold.1
+ initValAVOutputDeviceClusterMemberVolumeDidChangeNotification.cold.1
+ initValAVOutputDeviceCommunicationChannelControlTypeDirect.cold.1
+ initValAVOutputDeviceCommunicationChannelControlTypeRelayed.cold.1
+ initValAVOutputDeviceCommunicationChannelDataDestinationMediaRemote.cold.1
+ initValAVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped.cold.1
+ initValAVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired.cold.1
+ initValAVOutputDeviceCommunicationChannelOptionControlType.cold.1
+ initValAVOutputDeviceCommunicationChannelOptionCorrelationID.cold.1
+ initValAVOutputDeviceCommunicationChannelOptionInitiator.cold.1
+ initValAVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate.cold.1
+ initValAVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification.cold.1
+ initValAVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired.cold.1
+ initValAVOutputDeviceGroupAddOutputDeviceOptionInitiator.cold.1
+ initValAVOutputDeviceGroupRemoveOutputDeviceOptionInitiator.cold.1
+ initValAVOutputDeviceGroupVolumeControlTypeDidChangeNotification.cold.1
+ initValAVOutputDeviceGroupVolumeDidChangeNotification.cold.1
+ initValAVOutputDeviceMutedDidChangeNotification.cold.1
+ initValAVOutputDeviceVolumeControlTypeDidChangeNotification.cold.1
+ initValAVOutputDeviceVolumeDidChangeNotification.cold.1
+ initWithConnection:replyQueue:.__onceToken
+ initWithConnection:replyQueue:.__queue
+ initWithOrigin:.__queue
+ initWithOrigin:.onceToken
+ loggingQueue.onceToken
+ loggingQueue.queue
+ shouldConnectToLocalEndpoint.__value
+ shouldConnectToLocalEndpoint.onceToken
+ sonicMusicEnabled.__value
+ sonicMusicEnabled.onceToken
+ sonicPodcastsEnabled.__value
+ sonicPodcastsEnabled.onceToken
+ supportLastPlayingDevice.__value
+ supportLastPlayingDevice.onceToken
+ systemVolumeCapabilitiesOverride.onceToken
+ systemVolumeOverride.onceToken
- +[MRAVClusterController getClusterLeaderUID]
- +[MRAVClusterController getClusterType]
- +[MRAVClusterController getClusterUID]
- -[MRAVConcreteOutputContext _registerNotifications]
- -[MRAVConcreteOutputContext isVolumeControlAvailable]
- -[MRAVConcreteOutputContext setIsVolumeControlAvailable:]
- -[MRAVConcreteOutputDevice _onQueue_nearbyObject]
- -[MRAVConcreteOutputDevice _onqueue_clearCachedAVOutputDeviceProperties]
- -[MRAVConcreteOutputDevice distance]
- -[MRAVConcreteOutputDevice setAVOutputDevice:]
- -[MRAVConcreteOutputDevice setAirPlayGroupID:]
- -[MRAVConcreteOutputDevice setSourceInfo:]
- -[MRAVConcreteRoutingDiscoverySession _availableOutputDevicesDidChangeNotification:].cold.1
- -[MRAVConcreteRoutingDiscoverySession _onQueue_reloadAvailableOutputDevices]
- -[MRAVConcreteRoutingDiscoverySession _onQueue_reloadAvailableOutputDevices].cold.1
- -[MRAVConcreteRoutingDiscoverySession _onQueue_reload]
- -[MRAVConcreteRoutingDiscoverySession _scheduleAvailableOutputDevicesReload]
- -[MRAVOutputDevice distance]
- -[MRAVOutputDevice isB520Device]
- -[MRAVOutputDevice isHomeTheaterB520Device]
- -[MRAVOutputDevice setAirPlayGroupID:]
- -[MRAVOutputDevice setParentGroupIdentifier:]
- -[MRAVOutputDevice setPrimaryID:]
- -[MRAVOutputDeviceSourceInfo .cxx_destruct]
- -[MRAVOutputDeviceSourceInfo initWithRoutingContextUID:multipleBuiltInDevices:]
- -[MRAVOutputDeviceSourceInfo routingContextUID]
- -[MRActiveRoutesObserver _onWorkerQueue_reevaluate]
- -[MRActiveRoutesObserver _reevaluate]
- -[MRActiveRoutesObserver callback]
- -[MRActiveRoutesObserver setCallback:]
- -[MRDeviceInfoOutputDevice .cxx_destruct]
- -[MRDeviceInfoOutputDevice airPlayGroupID]
- -[MRDeviceInfoOutputDevice avOutputDevice]
- -[MRDeviceInfoOutputDevice canAccessAppleMusic]
- -[MRDeviceInfoOutputDevice canAccessRemoteAssets]
- -[MRDeviceInfoOutputDevice canAccessiCloudMusicLibrary]
- -[MRDeviceInfoOutputDevice clusterCompositionMembers]
- -[MRDeviceInfoOutputDevice clusterCompositionOutputDevices]
- -[MRDeviceInfoOutputDevice clusterComposition]
- -[MRDeviceInfoOutputDevice clusterType]
- -[MRDeviceInfoOutputDevice configuredClusterSize]
- -[MRDeviceInfoOutputDevice deviceInfo]
- -[MRDeviceInfoOutputDevice deviceSubtype]
- -[MRDeviceInfoOutputDevice deviceType]
- -[MRDeviceInfoOutputDevice exporting]
- -[MRDeviceInfoOutputDevice fallbackOutputDevice]
- -[MRDeviceInfoOutputDevice groupContainsGroupLeader]
- -[MRDeviceInfoOutputDevice hostDeviceClass]
- -[MRDeviceInfoOutputDevice isAirPlayReceiverSessionActive]
- -[MRDeviceInfoOutputDevice isGroupLeader]
- -[MRDeviceInfoOutputDevice isGroupable]
- -[MRDeviceInfoOutputDevice isLocalDevice]
- -[MRDeviceInfoOutputDevice isProxyGroupPlayer]
- -[MRDeviceInfoOutputDevice isRemoteControllable]
- -[MRDeviceInfoOutputDevice isVolumeMuted]
- -[MRDeviceInfoOutputDevice logicalDeviceID]
- -[MRDeviceInfoOutputDevice modelID]
- -[MRDeviceInfoOutputDevice name]
- -[MRDeviceInfoOutputDevice parentGroupContainsDiscoverableLeader]
- -[MRDeviceInfoOutputDevice parentGroupIdentifier]
- -[MRDeviceInfoOutputDevice setExporting:]
- -[MRDeviceInfoOutputDevice setFallbackOutputDevice:]
- -[MRDeviceInfoOutputDevice supportsBufferedAirPlay]
- -[MRDeviceInfoOutputDevice supportsMultiplayer]
- -[MRDeviceInfoOutputDevice uid]
- -[MRDeviceInfoOutputDevice volumeCapabilities]
- -[MRDeviceInfoOutputDevice volume]
- -[MRExternalClientConnection initWithConnection:queue:]
- -[MRExternalDeviceTransportConnection init]
- -[MRExternalJSONClientConnection initWithConnection:queue:]
- -[MRIDSClientConnection initWithConnection:queue:]
- -[MROutputContextDataSource notifyOutputDeviceAdded:].cold.1
- -[MROutputContextDataSource notifyOutputDeviceAdded:].cold.2
- -[MROutputContextDataSource notifyOutputDeviceChanged:].cold.1
- -[MROutputContextDataSource notifyOutputDeviceChanged:].cold.2
- -[MROutputContextDataSource notifyOutputDeviceRemoved:].cold.1
- -[MROutputContextDataSource notifyOutputDeviceRemoved:].cold.2
- -[MROutputContextDataSource notifyVolumeCapabilitiesDidChange:outputDevice:].cold.1
- -[MROutputContextDataSource notifyVolumeCapabilitiesDidChange:outputDevice:].cold.2
- -[MROutputContextDataSource notifyVolumeDidChange:outputDevice:].cold.1
- -[MROutputContextDataSource notifyVolumeMutedDidChange:outputDevice:].cold.1
- -[MROutputContextDataSource outputDeviceForUID:]
- -[MRPlaybackSessionRequest hasLength]
- -[MRPlaybackSessionRequest hasLocation]
- -[MRPlaybackSessionRequest initWithIdentifier:range:]
- -[MRPlaybackSessionRequest length]
- -[MRPlaybackSessionRequest location]
- -[MRPlaybackSessionRequest range]
- -[MRPlaybackSessionRequest setHasLength:]
- -[MRPlaybackSessionRequest setHasLocation:]
- -[MRPlaybackSessionRequest setLength:]
- -[MRPlaybackSessionRequest setLocation:]
- -[MRProtocolClientConnection initWithConnection:queue:]
- -[MRProtocolClientConnection queue]
- -[MRRateLimiter _updateAlreadyOnQueue:]
- -[MRStreamTransportConnection initWithInputStream:outputStream:]
- -[MRUserSettings allowAllClientUIConnections]
- -[MRUserSettings connectedClientAuditTokens]
- -[MRUserSettings defaultSupportedCommandsDataForClient:]
- -[MRUserSettings defaultSupportedCommandsData]
- -[MRUserSettings disablePairedDeviceActiveEndpointSync]
- -[MRUserSettings expectedClientAuditTokens]
- -[MRUserSettings forceEnableCECVolume]
- -[MRUserSettings groupSessionASEAssertionEnabled]
- -[MRUserSettings jsonClientUIDs]
- -[MRUserSettings lastBootUUID]
- -[MRUserSettings localLastPlayingDate]
- -[MRUserSettings localPlaybackState]
- -[MRUserSettings personalDeviceState]
- -[MRUserSettings recentGroupSessionParticipantsPepper]
- -[MRUserSettings setConnectedClientAuditTokens:]
- -[MRUserSettings setExpectedClientAuditTokens:]
- -[MRUserSettings setLastBootUUID:]
- -[MRUserSettings setLocalLastPlayingDate:]
- -[MRUserSettings setLocalPlaybackState:]
- -[MRUserSettings setPersonalDeviceState:]
- -[MRUserSettings shouldInitializeGenericBonjourService]
- -[MRUserSettings shouldInitializeTelevisionBonjourService]
- -[MRUserSettings updateDefaultSupportedCommandsData:forClient:]
- -[MRUserSettings useAPSyncAPI]
- -[MRUserSettings useDebugAVRouteWithoutVolumeControl]
- -[MRUserSettings useRSEForProximity]
- -[_MRPlaybackSessionRequestProtobuf hasLength]
- -[_MRPlaybackSessionRequestProtobuf hasLocation]
- -[_MRPlaybackSessionRequestProtobuf length]
- -[_MRPlaybackSessionRequestProtobuf location]
- -[_MRPlaybackSessionRequestProtobuf setHasLength:]
- -[_MRPlaybackSessionRequestProtobuf setHasLocation:]
- -[_MRPlaybackSessionRequestProtobuf setLength:]
- -[_MRPlaybackSessionRequestProtobuf setLocation:]
- GCC_except_table113
- GCC_except_table203
- GCC_except_table306
- GCC_except_table80
- GCC_except_table91
- GCC_except_table99
- NearbyInteractionLibrary.sLib
- NearbyInteractionLibrary.sOnce
- OBJC_IVAR_$_MRAVConcreteOutputContext._isVolumeControlAvailable
- OBJC_IVAR_$_MRAVConcreteOutputDevice._MACAddress
- OBJC_IVAR_$_MRAVConcreteOutputDevice._accessSerialQueue
- OBJC_IVAR_$_MRAVConcreteOutputDevice._airPlayGroupID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._clusterComposition
- OBJC_IVAR_$_MRAVConcreteOutputDevice._firmwareVersion
- OBJC_IVAR_$_MRAVConcreteOutputDevice._logicalDeviceID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._modelID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._modelSpecificInfo
- OBJC_IVAR_$_MRAVConcreteOutputDevice._nearbyObject
- OBJC_IVAR_$_MRAVConcreteOutputDevice._overrideGroupID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._overrideUID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._playingPairedDeviceName
- OBJC_IVAR_$_MRAVConcreteOutputDevice._uid
- OBJC_IVAR_$_MRAVOutputDevice._distance
- OBJC_IVAR_$_MRAVOutputDevice._primaryID
- OBJC_IVAR_$_MRAVOutputDeviceSourceInfo._routingContextUID
- OBJC_IVAR_$_MRActiveRoutesObserver._callback
- OBJC_IVAR_$_MRDeviceInfoOutputDevice._deviceInfo
- OBJC_IVAR_$_MRDeviceInfoOutputDevice._exporting
- OBJC_IVAR_$_MRDeviceInfoOutputDevice._fallbackOutputDevice
- OBJC_IVAR_$_MRPlaybackSessionRequest._hasLength
- OBJC_IVAR_$_MRPlaybackSessionRequest._hasLocation
- OBJC_IVAR_$_MRPlaybackSessionRequest._length
- OBJC_IVAR_$_MRPlaybackSessionRequest._location
- OBJC_IVAR_$_MRProtocolClientConnection._queue
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._has
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._length
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._location
- _MRAVOutputDeviceB238ModelID
- _MRAVOutputDeviceB620ModelID
- _MRMediaRemotePlaybackSessionMigrate
- _MRMediaRemotePlaybackSessionMigrateForOrigin
- _MRMediaRemotePlaybackSessionMigrateForPlayer
- _MRMediaRemotePlaybackSessionMigrateWithRequest
- _MRMediaRemotePlaybackSessionRequestSupportedType
- _MRMediaRemotePlaybackSessionRequestSupportedTypeForOrigin
- _MRPlaybackSessionMigrateCopyCorrespondingPlayerPath
- _MRPlaybackSessionMigrateCopyCurrentTypes
- _MRPlaybackSessionMigrateCopySupportedTypeMatch
- _MRPlaybackSessionMigrateCopySupportedTypes
- _MRPlaybackSessionRequestCopyDescription
- _MRPlaybackSessionRequestCreate
- _MRPlaybackSessionRequestCreateExternalRepresentation
- _MRPlaybackSessionRequestCreateFromExternalRepresentation
- _MRUserSettingsForceEnableCECContext
- _MRUserSettingsForceEnableCECVolumeDidChange
- _NINearbyObjectFunction
- __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.715
- __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.719
- __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.723
- __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.729
- __105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.736
- __106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.660
- __122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.673
- __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.693
- __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.700
- __122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.705
- __122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.281
- __122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.293
- __39-[MRDistantExternalDevice customOrigin]_block_invoke.234
- __39-[MRDistantExternalDevice customOrigin]_block_invoke_2.236
- __39-[MRRateLimiter _updateAlreadyOnQueue:]_block_invoke.59
- __41-[MRLegacyController setupExternalDevice]_block_invoke.13
- __47-[MROutputContextController _inititalizeVolume]_block_invoke.314
- __47-[MROutputContextController _inititalizeVolume]_block_invoke.318
- __47-[MROutputContextController _inititalizeVolume]_block_invoke.322
- __48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.342
- __52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.502
- __52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.509
- __56-[MRProtocolClientConnection sendMessage:timeout:reply:]_block_invoke.53
- __57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.540
- __57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.549
- __60+[MRActiveRoutesObserver fetchActiveRouteIDsWithCompletion:]_block_invoke.26
- __60-[MRAVConcreteEndpoint outputDeviceVolume:queue:completion:]_block_invoke.64
- __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.557
- __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.558
- __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.565
- __60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_2.566
- __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.7
- __61-[MRAVConcreteRoutingDiscoverySession availableOutputDevices]_block_invoke.8
- __61-[MROutputContextController _onSerialQueue_localOutputDevice]_block_invoke.307
- __63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.647
- __63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.cold.1
- __65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.350
- __66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.271
- __66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.274
- __66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.359
- __66-[MRExternalOutputContextDataSource updateVolume:outputDeviceUID:]_block_invoke.164
- __66-[MROutputContextController adjustVolume:outputDeviceUID:details:]_block_invoke.273
- __67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.621
- __67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.614
- __67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.346
- __68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.35
- __68+[MRActiveRoutesObserver fetchActiveEndpointOnQueue:withCompletion:]_block_invoke.38
- __69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.360
- __69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.361
- __70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.677
- __75-[MRDistantExternalDevice requestGroupSessionWithDetails:queue:completion:]_block_invoke.300
- __75-[MRDistantExternalDevice requestGroupSessionWithDetails:queue:completion:]_block_invoke_2.301
- __76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.631
- __76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.635
- __76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke.85
- __76-[MRAVConcreteEndpoint setOutputDeviceVolume:outputDevice:queue:completion:]_block_invoke.85.cold.1
- __76-[MRAVConcreteRoutingDiscoverySession _onQueue_reloadAvailableOutputDevices]_block_invoke.14
- __76-[MRAVConcreteRoutingDiscoverySession _scheduleAvailableOutputDevicesReload]_block_invoke.cold.1
- __76-[MRAVConcreteRoutingDiscoverySession _scheduleAvailableOutputDevicesReload]_block_invoke.cold.2
- __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.35
- __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.39
- __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.42
- __77-[MRAVConcreteEndpoint addOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.43
- __77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.531
- __77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.347
- __79-[MRAVConcreteEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.73
- __79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.516
- __79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.353
- __80-[MRAVConcreteEndpoint removeOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.50
- __80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.356
- __90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.312
- __91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.352
- __91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.328
- __91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.331
- __93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.319
- __93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.322
- __96-[MRAVOutputContext _notifyChangesInOutputDevicesWithAdded:removed:updated:previous:newDevices:]_block_invoke.152
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.106
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.138
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.138.cold.1
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.148
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.152
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.156
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.156.cold.1
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.163
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.170
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.175
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.176
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.95
- __MRAVEndpointModifyOutputDevicesInGroup_block_invoke.99
- __MRDictionaryCalculateDeltas_block_invoke.489
- __MRMediaRemoteGetClientProperties_block_invoke.533
- __MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.577
- __MRMediaRemoteGetPlayerProperties_block_invoke.564
- __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke.218
- __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke.224
- __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.219
- __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.225
- __MRMediaRemotePlaybackSessionMigrateForDevice_block_invoke_2.225.cold.1
- __MRMediaRemotePlaybackSessionMigrateForOrigin
- __MRMediaRemotePlaybackSessionMigrateForPlayer
- __MRMediaRemotePlaybackSessionRequestSupportedType
- __MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke.74
- __MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke_2.75
- __MRMediaRemoteRequestDeviceUID_block_invoke.404
- __MRMediaRemoteRequestIsGroupLeader_block_invoke.419
- __MRMediaRemoteSetWantsWakingNowPlayingNotifications_block_invoke.596
- __MRServiceClientRemotePlayerPathCommandCallback_block_invoke.109
- __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions)
- __OBJC_$_INSTANCE_VARIABLES_MRDeviceInfoOutputDevice
- __OBJC_$_PROP_LIST_MRDeviceInfoOutputDevice
- ___31-[MRAVConcreteOutputDevice uid]_block_invoke
- ___32-[MRAVConcreteOutputDevice name]_block_invoke
- ___34-[MRAVConcreteOutputDevice volume]_block_invoke
- ___35-[MRAVConcreteOutputDevice modelID]_block_invoke
- ___36-[MRAVConcreteOutputDevice distance]_block_invoke
- ___36-[MRAVConcreteOutputDevice dnsNames]_block_invoke
- ___37-[MRActiveRoutesObserver _reevaluate]_block_invoke
- ___38-[MRAVConcreteOutputDevice MACAddress]_block_invoke
- ___38-[MRAVConcreteOutputDevice deviceType]_block_invoke
- ___38-[MRAVConcreteOutputDevice sourceInfo]_block_invoke
- ___38-[MRUserSettings forceEnableCECVolume]_block_invoke
- ___39-[MRAVConcreteOutputDevice bluetoothID]_block_invoke
- ___39-[MRAVConcreteOutputDevice clusterType]_block_invoke
- ___39-[MRAVConcreteOutputDevice isGroupable]_block_invoke
- ___39-[MRAVConcreteOutputDevice supportsHAP]_block_invoke
- ___39-[MRAVConcreteOutputDevice tightSyncID]_block_invoke
- ___39-[MRRateLimiter _updateAlreadyOnQueue:]_block_invoke
- ___40-[MRAVConcreteOutputContext description]_block_invoke
- ___40-[MRAVConcreteOutputDevice batteryLevel]_block_invoke
- ___41-[MRAVConcreteOutputDevice deviceSubtype]_block_invoke
- ___41-[MRAVConcreteOutputDevice isGroupLeader]_block_invoke
- ___41-[MRAVConcreteOutputDevice isLocalDevice]_block_invoke
- ___42-[MRAVConcreteOutputDevice airPlayGroupID]_block_invoke
- ___42-[MRAVConcreteOutputDevice avOutputDevice]_block_invoke
- ___42-[MRAVConcreteOutputDevice setSourceInfo:]_block_invoke
- ___43-[MRAVConcreteOutputDevice firmwareVersion]_block_invoke
- ___43-[MRAVConcreteOutputDevice hasBatteryLevel]_block_invoke
- ___43-[MRAVConcreteOutputDevice supportsRapport]_block_invoke
- ___44-[MRAVConcreteOutputContext avOutputContext]_block_invoke
- ___44-[MRAVConcreteOutputDevice isAddedToHomeKit]_block_invoke
- ___44-[MRAVConcreteOutputDevice isAppleAccessory]_block_invoke
- ___45-[MRAVConcreteOutputDevice isDeviceGroupable]_block_invoke
- ___45-[MRAVConcreteOutputDevice modelSpecificInfo]_block_invoke
- ___46-[MRAVConcreteOutputDevice clusterComposition]_block_invoke_2
- ___46-[MRAVConcreteOutputDevice isProxyGroupPlayer]_block_invoke
- ___46-[MRAVConcreteOutputDevice setAVOutputDevice:]_block_invoke
- ___46-[MRAVConcreteOutputDevice setAirPlayGroupID:]_block_invoke
- ___46-[MRAVConcreteOutputDevice volumeCapabilities]_block_invoke
- ___46-[MRDeviceInfoOutputDevice clusterComposition]_block_invoke
- ___46-[MRNowPlayingOriginClientRequests deviceInfo]_block_invoke
- ___47-[MRAVConcreteOutputDevice canAccessAppleMusic]_block_invoke
- ___47-[MRAVConcreteOutputDevice supportsMultiplayer]_block_invoke
- ___48-[MRAVConcreteOutputDevice deviceEnclosureColor]_block_invoke
- ___48-[MRAVConcreteOutputDevice isRemoteControllable]_block_invoke
- ___49-[MRAVConcreteOutputDevice adjustVolume:details:]_block_invoke
- ___49-[MRAVConcreteOutputDevice canAccessRemoteAssets]_block_invoke
- ___49-[MRAVConcreteOutputDevice configuredClusterSize]_block_invoke
- ___49-[MRAVConcreteOutputDevice discoveredOnSameInfra]_block_invoke
- ___49-[MRAVConcreteOutputDevice parentGroupIdentifier]_block_invoke
- ___49-[MRAVConcreteOutputDevice requiresAuthorization]_block_invoke
- ___50-[MRAVConcreteOutputDevice isPickedOnPairedDevice]_block_invoke
- ___50-[MRAVConcreteOutputDevice supportsExternalScreen]_block_invoke
- ___50-[MRNowPlayingOriginClientRequests setDeviceInfo:]_block_invoke
- ___51-[MRAVConcreteOutputDevice playingPairedDeviceName]_block_invoke
- ___51-[MRAVConcreteOutputDevice supportsBufferedAirPlay]_block_invoke
- ___51-[MRActiveRoutesObserver _onWorkerQueue_reevaluate]_block_invoke
- ___52-[MRAVConcreteOutputDevice groupContainsGroupLeader]_block_invoke
- ___52-[MRAVConcreteOutputDevice producesLowFidelityAudio]_block_invoke
- ___52-[MRAVConcreteOutputDevice supportsBluetoothSharing]_block_invoke
- ___52-[MRAVConcreteOutputDevice supportsSharePlayHandoff]_block_invoke
- ___53-[MRDeviceInfoOutputDevice clusterCompositionMembers]_block_invoke
- ___54-[MRUserSettings recentGroupSessionParticipantsPepper]_block_invoke
- ___55-[MRAVConcreteOutputDevice canAccessiCloudMusicLibrary]_block_invoke
- ___55-[MRAVConcreteOutputDevice canFetchMediaDataFromSender]_block_invoke
- ___55-[MRAVConcreteOutputDevice headTrackedSpatialAudioMode]_block_invoke
- ___56-[MRAVConcreteOutputDevice canRelayCommunicationChannel]_block_invoke
- ___57-[MRAVConcreteOutputDevice allowsHeadTrackedSpatialAudio]_block_invoke
- ___57-[MRAVConcreteOutputDevice currentBluetoothListeningMode]_block_invoke
- ___57-[MRAVConcreteOutputDevice supportsConversationDetection]_block_invoke
- ___58-[MRAVConcreteOutputDevice isActivatedForContinuityScreen]_block_invoke
- ___58-[MRAVConcreteOutputDevice isAirPlayReceiverSessionActive]_block_invoke
- ___58-[MRAVConcreteOutputDevice isConversationDetectionEnabled]_block_invoke
- ___59-[MRAVConcreteOutputDevice isHeadTrackedSpatialAudioActive]_block_invoke
- ___59-[MRAVConcreteOutputDevice supportsHeadTrackedSpatialAudio]_block_invoke
- ___59-[MRDeviceInfoOutputDevice clusterCompositionOutputDevices]_block_invoke
- ___60-[MRAVConcreteOutputDevice availableBluetoothListeningModes]_block_invoke
- ___65-[MRAVConcreteOutputDevice parentGroupContainsDiscoverableLeader]_block_invoke
- ___65-[MRAVConcreteOutputDevice setHeadTrackedSpatialAudioMode:error:]_block_invoke
- ___65-[MRAVConcreteOutputDevice supportsRapportRemoteControlTransport]_block_invoke
- ___66-[MRAVConcreteOutputDevice setConversationDetectionEnabled:error:]_block_invoke
- ___67-[MRAVConcreteOutputDevice setAllowsHeadTrackedSpatialAudio:error:]_block_invoke
- ___67-[MRAVConcreteOutputDevice setCurrentBluetoothListeningMode:error:]_block_invoke
- ___69-[MRAVConcreteOutputDevice canPlayEncryptedProgressiveDownloadAssets]_block_invoke
- ___74-[MRNowPlayingOriginClientRequests handleDeviceInfoRequestWithCompletion:]_block_invoke_2
- ___76-[MRAVConcreteRoutingDiscoverySession _onQueue_reloadAvailableOutputDevices]_block_invoke
- ___76-[MRAVConcreteRoutingDiscoverySession _onQueue_reloadAvailableOutputDevices]_block_invoke_2
- ___76-[MRAVConcreteRoutingDiscoverySession _scheduleAvailableOutputDevicesReload]_block_invoke
- ___91-[MRAVConcreteOutputDevice presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets]_block_invoke
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.409
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.412
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.412.cold.1
- ___MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.413
- ___MRMediaRemotePlaybackSessionMigrateForOrigin_block_invoke_2.cold.1
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.102
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.112
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.124
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.131
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.136
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.139
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.142
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.145
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.154
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.162
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.174
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.182
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.96
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke.99
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.100
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.106
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.116
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.125
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.132
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.146
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.158
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.170
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.179
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.179.cold.1
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2.186
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_3.120
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_3.130
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_3.150
- ___MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_3.187
- ___MRMediaRemotePlaybackSessionMigrateWithRequest_block_invoke
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke.49
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke.51
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke.56
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke_2
- ___MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke_3
- ___MRPlaybackSessionMigrateCopySupportedTypeMatch_block_invoke
- ___NearbyInteractionLibrary_block_invoke
- ____MRMediaRemotePlaybackSessionMigrateForOrigin_block_invoke
- ____MRMediaRemotePlaybackSessionMigrateForOrigin_block_invoke_2
- ____MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke
- ____MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_2
- ____MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_3
- ____MRMediaRemotePlaybackSessionMigrateForPlayer_block_invoke_4
- ____MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke
- ____MRMediaRemotePlaybackSessionRequestSupportedType_block_invoke_2
- ___block_descriptor_104_e8_32r40r48r56r64r72r80r88r96r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
- ___block_descriptor_40_e8_32bs_e44_v40?0^v8^v16^{__CFString=}24^{__CFError=}32l
- ___block_descriptor_40_e8_32s_e22_16?0"MRDeviceInfo"8l
- ___block_descriptor_48_e8_32s40bs_e64_v40?0"MRPlayerPath"8"MRPlayerPath"16"NSString"24"NSError"32l
- ___block_descriptor_48_e8_32s40r_e34_v24?0"MRDeviceInfo"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e35_v24?0^{__CFArray=}8^{__CFError=}16l
- ___block_descriptor_48_e8_32s40s_e24_16?0"AVOutputDevice"8l
- ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e46_v24?0"NSArray"8?<v?"NSArray""NSError">16l
- ___block_descriptor_57_e8_32s40r48r_e5_v8?0l
- ___block_descriptor_64_e8_32s40r48r56r_e69_v32?0"AVOutputDeviceCommunicationChannel"8"NSError"16"NSString"24l
- ___block_descriptor_64_e8_32s40s48s56s_e52_v24?0"NSString"8?<v?"MRAVEndpoint""NSError">16l
- ___block_descriptor_64_e8_32s40s48s56s_e56_v40?0Q8"MRAVEndpoint"16"NSArray"24?<v?"NSError">32l
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e20_v16?0^{__CFError=}8l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e44_v40?0^v8^v16^{__CFString=}24^{__CFError=}32l
- ___block_descriptor_80_e8_32bs40bs48r56r64r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48bs56r64r72r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e36_v24?0"AVOutputDevice"8"NSError"16l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e34_v24?0"MRAVEndpoint"8"NSError"16l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e46_v32?0"MRAVEndpoint"8"NSArray"16"NSError"24l
- ___block_descriptor_98_e8_32s40s48s56s64s72s_e19_"NSDictionary"8?0l
- ___copy_helper_block_e8_32b40b48r56r64r
- ___copy_helper_block_e8_32b40r48r
- ___copy_helper_block_e8_32r40r48r56r64r72r80r88r96r
- ___copy_helper_block_e8_32s40r48r56r
- ___copy_helper_block_e8_32s40s48b56r64r72r
- ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r96r
- ___destroy_helper_block_e8_32s40r48r56r
- __block_literal_global.116
- __block_literal_global.127
- __block_literal_global.135
- __block_literal_global.174
- __block_literal_global.184
- __block_literal_global.186
- __block_literal_global.191
- __block_literal_global.194
- __block_literal_global.203
- __block_literal_global.208
- __block_literal_global.217
- __block_literal_global.224
- __block_literal_global.227
- __block_literal_global.229
- __block_literal_global.230
- __block_literal_global.234
- __block_literal_global.248
- __block_literal_global.277
- __block_literal_global.301
- __block_literal_global.306
- __block_literal_global.407
- __block_literal_global.482
- __block_literal_global.485
- __block_literal_global.527
- __block_literal_global.530
- __block_literal_global.573
- __block_literal_global.664
- __block_literal_global.687
- __block_literal_global.91
- _classNINearbyObject
- _fmod
- _fmodf
- _getAVOutputDeviceBatteryLevelCaseKey
- _getAVOutputDeviceBatteryLevelLeftKey
- _getAVOutputDeviceBatteryLevelRightKey
- _getNINearbyObjectClass
- _initNINearbyObject
- _objc_msgSend$_onQueue_reload
- _objc_msgSend$_onQueue_reloadAvailableOutputDevices
- _objc_msgSend$_onWorkerQueue_reevaluate
- _objc_msgSend$_reevaluate
- _objc_msgSend$_scheduleAvailableOutputDevicesReload
- _objc_msgSend$_updateAlreadyOnQueue:
- _objc_msgSend$defaultSupportedCommandsData
- _objc_msgSend$disablePairedDeviceActiveEndpointSync
- _objc_msgSend$exporting
- _objc_msgSend$getClusterLeaderUID
- _objc_msgSend$getClusterType
- _objc_msgSend$getClusterUID
- _objc_msgSend$homePodHomeTheaterComposition
- _objc_msgSend$homePodMiniHomeTheaterComposition
- _objc_msgSend$homePodMiniStereoPairComposition
- _objc_msgSend$homePodStereoPairComposition
- _objc_msgSend$initWithIdentifier:type:
- _objc_msgSend$initWithInputStream:outputStream:
- _objc_msgSend$initWithRoutingContextUID:multipleBuiltInDevices:
- _objc_msgSend$isB520Device
- _objc_msgSend$isHomeTheaterB520Device
- _objc_msgSend$openCommunicationChannelWithOptions:completionHandler:
- _objc_msgSend$receivesLongFormAudioFromLocalDevice
- _objc_msgSend$registerVolumeNotifications
- _objc_msgSend$setDistance:
- _objc_msgSend$setInteger:forKey:
- _objc_msgSend$setMuted:
- _objc_msgSend$stringForKey:
- _reloadOutputContext.__once
- _reloadOutputContext.__queue
- forceEnableCECVolume.onceToken
- recentGroupSessionParticipantsPepper.onceToken
- recentGroupSessionParticipantsPepper.pepper
CStrings:
+ "%@\n  designatedGroupLeader = %@\n  isLocalDeviceDesignatedGroupLeader = %@\n  outputContextSupportsVolumeControl = %@\n  localVolume = %lf\n  localVolumeCapabilities = %@\n  localVolumeMute = %u\n  OutputContext = %@\n"
+ "%@ -> %@  will not work with AVOD sourced from Discovery"
+ "%@ -> %lf will not work with AVOD sourced from Discovery"
+ "%@ -> %u will not work with AVOD sourced from Discovery"
+ "%@ outputContextSupportsVolumeControl = %@ localVolume = %lf, localVolumeCapabilities = %@ localVolumeMute = %u"
+ "%{public}@"
+ "05ac:110"
+ "76,4363"
+ "76,8223"
+ "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@>"
+ "<%@:%p multipleBuiltIn = %s>"
+ "@\"<MRExternalDeviceTransportConnectionDataSource>\""
+ "@\"MRCommandInfo\""
+ "@\"MRRateLimiter\""
+ "@28@0:8B16q20"
+ "@32@0:8@?16@?24"
+ "@36@0:8@16B24Q28"
+ "AVOutputDevice.openCommunicationChannelWithOptions<%@> -> %@"
+ "AVOutputDeviceCommunicationChannelDataDestinationMediaRemote"
+ "Absolute"
+ "AddOutputDevices.xpcInterface"
+ "AddOutputDevicesInGroup"
+ "AddOutputDevicesInGroup.fetchGroupLeader"
+ "Adjustment"
+ "AfterRoutingCompleteTimout"
+ "AudioAccessory1,"
+ "AudioAccessory5,"
+ "AudioAccessory5,1"
+ "AudioAccessory6,"
+ "CurrentTypes.insersect(SupportedTypes) is empty currentTypes=%@ supportedTypes=%@"
+ "DelegateAccount"
+ "Destination.setPlaybackSession.options[supportedTypes] is empty"
+ "DuplicateCommandContextID"
+ "Excessive PlayerPathInvalidationhandlers"
+ "Failed to find symbol with model: %{public}@ variant options: %lu error: %{public}@ symbol:%{public}@"
+ "Failed to resolve destination player path"
+ "Failed to resolve player path, but did not receive an error: sourcePlayerPath=%@"
+ "Failed to resolve source player path"
+ "MRDeviceInfoOutputDeviceAdditions"
+ "MRExternalDeviceTransportConnectionDataSource"
+ "MRMediaRemoteProactiveRecommendedPlayerDidChangeNotification"
+ "MRMediaRemoteProactiveRecommendedPlayerReasonUserInfoKey"
+ "MRUserSettingsSystemVolumeCapabilitiesOverrideDidChange"
+ "MRUserSettingsSystemVolumeOverrideDidChange"
+ "Mute"
+ "NewPlayerUsedInstead"
+ "OneShotQHO"
+ "Partially resolved player path mising bundleID: destinationPlayerPath=%@"
+ "Partially resolved player path mising origin: destinationPlayerPath=%@"
+ "PlayerPath"
+ "Relative"
+ "RemoveOutputDevices.xpcInterface"
+ "RemoveOutputDevicesInGroup"
+ "RemoveOutputDevicesInGroup.fetchGroupLeader"
+ "SetOutputDevices.xpcInterface"
+ "SetOutputDevicesInGroup"
+ "SetOutputDevicesInGroup.fetchGroupLeader"
+ "Source.setPlaybackSession.options[currentTypes] is empty"
+ "SystemVolumeCapabilitiesOverride"
+ "SystemVolumeOverride"
+ "T@\"<MRExternalDeviceTransportConnectionDataSource>\",W,N,V_dataSource"
+ "T@\"AVOutputDevice\",R,N"
+ "T@\"MRAVOutputDeviceSourceInfo\",R,N"
+ "T@\"MRCommandInfo\",R,N,V_destinationSetPlaybackSessionCommandInfo"
+ "T@\"MRPlayerPath\",C,N,V_destinationPlayerPath"
+ "T@\"NSData\",&,N,V_delegateAccountData"
+ "T@\"NSDictionary\",C,N,V_destinationCommandInfo"
+ "T@\"NSError\",R,C,N,V_error"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_sendQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_replyQueue"
+ "T@\"NSString\",&,N,V_alternateTransportType"
+ "T@\"NSString\",&,N,V_delegateAccountDataType"
+ "T@\"NSString\",&,N,V_subtitleShort"
+ "T@\"NSString\",C,N,V_subtitleShort"
+ "T@\"NSString\",R,C,N,V_playbackSessionType"
+ "T@\"NSString\",R,N,V_airPlayGroupID"
+ "T@\"NSString\",R,N,V_alternateTransportType"
+ "T@\"NSString\",R,N,V_parentGroupIdentifier"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_destinationCommandInfo"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_playbackSessionRequirements"
+ "T@?,C,N,V_activeRouteIDsChangedCallback"
+ "T@?,C,N,V_isLocalDeviceAirPlayActiveCallback"
+ "TB,N,GisArtworkOnly,V_artworkOnly"
+ "TQ,N,V_earPodCount"
+ "Tq,R,N,V_sourceType"
+ "UnknownOutputDevicesInGroup"
+ "UnknownOutputDevicesInGroup.fetchGroupLeader"
+ "[AVDiscoverySession] CreateOutputDevicesFromAVOutputDevices took %lf seconds"
+ "[AVDiscoverySession] NotifyOutputDevicesChanged took %lf seconds"
+ "[AVDiscoverySession] Querying AVDiscoverySession.availableOutputDevices took %lf seconds"
+ "[ConcreteOutputContext] CanSetVolume did change: supportsVolumeControl=%{BOOL}u, canSetVolume=%{BOOL}u, volumeControlType=%{public}@, effectiveVolumeCapabilities=%{public}@ for context: %{public}@ - %{public}@"
+ "[ConcreteOutputContext] SupportsVolumeControl did change: supportsVolumeControl=%{BOOL}u, canSetVolume=%{BOOL}u, volumeControlType=%{public}@, effectiveVolumeCapabilities=%{public}@ for context: %{public}@ - %{public}@"
+ "[ConcreteOutputContext] VolumeControlType did change: supportsVolumeControl=%{BOOL}u, canSetVolume=%{BOOL}u, volumeControlType=%{public}@, effectiveVolumeCapabilities=%{public}@ for context: %{public}@ - %{public}@"
+ "[MRActiveRoutesObserver] LocalDeviceAirPlayActive -> %u"
+ "[MRNowPlayingOriginClientManager] RemoveOrigin: Could not find originClient for origin %{public}@"
+ "[MRNowPlayingOriginClient] Creating %@ for origin %@"
+ "[MRNowPlayingOriginClient] Destroying %@ for origin %@"
+ "[MRNowPlayingOriginClient] Nil routingContext. Not creating %@ for origin %@"
+ "[MRV2NowPlayingController] <%@> ignoring artwork request failure because configuration needs other data"
+ "[OutputContext] CompareOutputDeviceList took %lf seconds"
+ "[OutputContext] NotifyChanges took %lf seconds"
+ "[OutputContext] Observed added localOutputDevice %{public}@ for context: %{public}@"
+ "[OutputContext] Observed added outputDevice %{public}@ for context: %{public}@"
+ "[OutputContext] Observed removed localOutputDevice %{public}@ for context: %{public}@"
+ "[OutputContext] Observed removed outputDevice %{public}@ for context: %{public}@"
+ "[OutputContext] setOutputDevices took %lf seconds"
+ "_MRPSMRecipe"
+ "_activeRouteIDsChangedCallback"
+ "_alternateTransportType"
+ "_artworkOnly"
+ "_avOutputContextLock"
+ "_callOutQueue"
+ "_canSetVolume"
+ "_dataSource"
+ "_delegateAccountData"
+ "_delegateAccountDataType"
+ "_destinationCommandInfo"
+ "_destinationSetPlaybackSessionCommandInfo"
+ "_deviceInfoLock"
+ "_earPodCount"
+ "_effectiveVolumeCapabilities"
+ "_groupUIDOverride"
+ "_handleActiveDeviceInfoDidChange:"
+ "_handleOutputContextCanSetVolumeDidChangeNotification:"
+ "_handleOutputContextVolumeControlTypeDidChangeNotification:"
+ "_isLocalDeviceAirPlayActiveCallback"
+ "_loadLocalOverrides"
+ "_localDeviceAirPlayActive"
+ "_notify"
+ "_onReloadQueue_createOutputDevicesFromAVOutputDevices:"
+ "_onReloadQueue_fetchOutputDevicesFromDiscoverySession:"
+ "_onReloadQueue_reload"
+ "_onReloadQueue_reloadAvailableOutputDevices"
+ "_onWorkerQueue_reevaluateAPA"
+ "_onWorkerQueue_reevaluateASE"
+ "_playbackSessionRequirements"
+ "_reevaluateAPA"
+ "_reevaluateASE"
+ "_reloadRateLimiter"
+ "_replyQueue"
+ "_sendQueue"
+ "_sourceType"
+ "_subtitleShort"
+ "_supportsVolumeControl"
+ "_uidOverride"
+ "_volumeControlType"
+ "activeRouteIDsChangedCallback"
+ "addHomePodWithModelIdentifier:"
+ "afterRoutingCompleteTimeout"
+ "alternateTransportType"
+ "artworkOnly"
+ "com.apple.mediaremote.MRNowPlayingOriginClientRequests.calloutQueue"
+ "com.apple.mediaremote.discoverySession.loggingQueue"
+ "com.apple.mediaremote.protocolClientConnection.sendQueue"
+ "concreteDiscoverySession.rateLimiter"
+ "dataSource"
+ "delegateAccountData"
+ "delegateAccountDataType"
+ "destinationCommandInfo"
+ "destinationSetPlaybackSessionCommandInfo"
+ "earPodCount"
+ "earPodCount: %lu;"
+ "earpods"
+ "failed to get device info for source"
+ "failed to get supported commands for destination"
+ "failed to get supported commands for source"
+ "groupSessionDelayedInitializationEnabled"
+ "has no transcript alignments"
+ "hasAlternateTransportType"
+ "hasDelegateAccountData"
+ "hasDelegateAccountDataType"
+ "hasDestinationCommandInfo"
+ "hasPlaybackSessionRequirements"
+ "hasSubtitleShort"
+ "hasSystemVolumeCapabilitiesOverride"
+ "hifispeaker.and.appletv.fill"
+ "homePodHomeTheaterCompositionWithHomePodModelIdentifier:"
+ "homePodStereoPairCompositionWithModelIdentifier:"
+ "initWithActiveRouteIDsChangedCallback:isLocalDeviceAirplayActiveChangedCallback:"
+ "initWithConnection:replyQueue:"
+ "initWithDataSource:"
+ "initWithErrorCode:"
+ "initWithInputStream:outputStream:dataSource:"
+ "initWithMultipleBuiltInDevices:sourceType:"
+ "isArtworkOnly"
+ "isB515CDevice"
+ "isB825Device"
+ "isHomePodMiniDevice"
+ "isLocalDeviceAirPlayActive"
+ "isLocalDeviceAirPlayActiveCallback"
+ "isPreferredClusterLeader"
+ "kMRMediaRemoteCommandInfoPlaybackSessionRequirements"
+ "kMRMediaRemoteOptionDelegateAccountData"
+ "kMRMediaRemoteOptionDelegateAccountDataType"
+ "legacySetPlaybackSessionWithSessionType:"
+ "loggingQueue"
+ "msv_compactDescription"
+ "notPossibleWithError:"
+ "oneShotSetPlaybackSessionWithCommandInfo:"
+ "openCommunicationChannelToDestination:options:completionHandler:"
+ "outputDevicesForUID:"
+ "pauseOutputDeviceUIDs.xpcInterface"
+ "playbackSessionRequirements"
+ "proactiveRecommendedPlayerInterval"
+ "q24@0:8@\"MRExternalDeviceTransportConnection\"16"
+ "q24@0:8@16"
+ "replyQueue"
+ "sendQueue"
+ "setActiveRouteIDsChangedCallback:"
+ "setAlternateTransportType:"
+ "setArtworkOnly:"
+ "setDataSource:"
+ "setDelegateAccountData:"
+ "setDelegateAccountDataType:"
+ "setDestinationCommandInfo:"
+ "setEarPodCount:"
+ "setIsLocalDeviceAirPlayActive:"
+ "setIsLocalDeviceAirPlayActiveCallback:"
+ "setPlaybackSessionRequirements:"
+ "setSendQueue:"
+ "setSubtitleShort:"
+ "sourceType"
+ "subtitleShort"
+ "supportProactiveRecommendedPlayer"
+ "symbolNameForType:fillVariant:"
+ "symbolNameForType:fillVariant:otherVariantOptions:"
+ "systemVolumeCapabilitiesOverride"
+ "systemVolumeOverride"
+ "transportTypeForTransport:"
+ "v24@?0@\"MRPlayerPath\"8@\"NSString\"16"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"NSError\"24"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"_MRPSMRecipe\"24"
+ "v32@?0Q8@\"MRAVEndpoint\"16@?<v@?@\"NSError\">24"
+ "void _MRPSMDetermineRecipe(MRPlayerPath *__strong, MROrigin *__strong, __strong dispatch_queue_t, void (^__strong)(MRPlayerPath *__strong, MRPlayerPath *__strong, _MRPSMRecipe *__strong))"
+ "watchIntentionalRouting"
+ "watch_intentional_routing"
+ "\xf0\xd1"
- "%@\n  designatedGroupLeader = %@\n  isLocalDeviceDesignatedGroupLeader = %@\n  outputContextSupportsVolumeControl = %@\n  AVSystemController.localVolume = %lf\n  AVSystemController.volumeCapabilities = %@\n  AVSystemController.localVolumeMute = %u\n  OutputContext = %@\n"
- "%@ -> %u"
- "%@ options do not match. source=%@ currentType=%@ destination=%@ supportedTypes=%@"
- "%@ outputContextSupportsVolumeControl = %@ (ignoreThis: localVolume = %lf, local volume capabilities = %@ localVolumeMute = %u)"
- "%@OutputDevicesInGroup"
- "-[MRAVOutputContext isVolumeControlAvailable]"
- "/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction"
- "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@>"
- "<%@:%p routingContextUID = %@, multipleBuiltIn = %s>"
- "@\"NINearbyObject\""
- "AllowAllClientUIConnections"
- "Attempted to initialize local endpoint from AVOutputDeviceGroup. Use MRAVLocalEndpoint instead."
- "AudioAccessory6"
- "ConcreteOutputContext.setVolumeMuted"
- "ConcreteOutputDevice.setVolumeMuted"
- "ConnectedClientAuditTokens"
- "ConnectedClientPIDs"
- "DefaultSupportedCommands"
- "ExpectedClientAuditTokens"
- "ExpectedClientPIDs"
- "ForceEnableCECVolume"
- "GroupSessionASEAssertionEnabled"
- "JSONClientUIDs"
- "LastBootUUID"
- "LastPlayingDate"
- "LocalPlaybackState"
- "MRNowPlayingPlayerPathRef MRPlaybackSessionMigrateCopyCorrespondingPlayerPath(MRNowPlayingPlayerPathRef, MROriginRef)"
- "MRUserSettingsForceEnableCECVolumeDidChange"
- "MRVolumeControlCapabilitiesAbsolute"
- "MRVolumeControlCapabilitiesAdjustment"
- "MRVolumeControlCapabilitiesMute"
- "MRVolumeControlCapabilitiesNone"
- "MRVolumeControlCapabilitiesRelative"
- "NINearbyObject"
- "Non resolved playerPath"
- "PersonalDeviceState"
- "RecentGroupSessionParticipantsPepper"
- "SerializedNIRangingData"
- "ShouldInitializeGenericBonjourService"
- "ShouldInitializeTVBonjourService"
- "SupportedCommands do not allow migration because %@"
- "T@\"AVOutputDevice\",&,N,SsetAVOutputDevice:"
- "T@\"MRAVOutputDevice\",&,N,V_fallbackOutputDevice"
- "T@\"MRAVOutputDeviceSourceInfo\",&,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSString\",C,N,V_airPlayGroupID"
- "T@\"NSString\",C,N,V_parentGroupIdentifier"
- "T@\"NSString\",C,N,V_primaryID"
- "T@\"NSString\",R,N,V_routingContextUID"
- "TB,N,V_exporting"
- "TQ,N,V_length"
- "TQ,N,V_location"
- "Tf,R,N,V_distance"
- "Timedout after %lf seconds trying discover audioOutputDevices. Discovered=%@, Requested=%@"
- "UseDebugAVRouteWithoutVolumeControl"
- "[AVDiscoverySession] Dispatching to reloadQueue took %lf seconds"
- "[AVDiscoverySession] Output devices did change notification received. Reloading available endpoints and output devices. %{public}@"
- "[AVDiscoverySession] Querying AVDiscoverySession time took %lf seconds"
- "[AVDiscoverySession] ReloadQueue priority degrated from %u -> %u"
- "[AVEndpoint] Error occurred while discovering devices %{public}@: %{public}@"
- "[ConcreteOutputContext] ProvidesVolumeFeatures did change to %{BOOL}u, capabilities: %{public}@  for context: %{public}@ - %{public}@"
- "[MRNowPlayingOriginClientRequests] %{public}@ UpdatingCache: deviceInfo %{public}@"
- "[OutputContext] Added localOutputDevice %{public}@ for context: %{public}@"
- "[OutputContext] Added outputDevice %{public}@ for context: %{public}@"
- "[OutputContext] Removed localOutputDevice %{public}@ for context: %{public}@"
- "[OutputContext] Removed outputDevice %{public}@ for context: %{public}@"
- "_exporting"
- "_fallbackOutputDevice"
- "_nearbyObject"
- "_onQueue_reload"
- "_onQueue_reloadAvailableOutputDevices"
- "_onWorkerQueue_reevaluate"
- "_overrideGroupID"
- "_overrideUID"
- "_primaryID"
- "_reevaluate"
- "_scheduleAvailableOutputDevicesReload"
- "_updateAlreadyOnQueue:"
- "actualNumberOfDevices"
- "allowAllClientUIConnections"
- "appletv.fill"
- "connectedClientAuditTokens"
- "defaultSupportedCommandsData"
- "defaultSupportedCommandsDataForClient:"
- "destination %@ does not support %@ (source currentTypes = %@)"
- "destinationPlayerPath %@ was resolved to %@"
- "disablePairedDeviceActiveEndpointSync"
- "disable_ase_sync"
- "expectedClientAuditTokens"
- "exporting"
- "fallbackOutputDevice"
- "fetchOutputDevices"
- "forceEnableCECVolume"
- "getClusterLeaderUID"
- "getClusterType"
- "getClusterUID"
- "groupSessionASEAssertionEnabled"
- "hifispeaker.and.appletv"
- "homepod.2.fill"
- "homepod.and.appletv.fill"
- "homepod.and.homepodmini.fill"
- "homepod.fill"
- "homepodmini.2.fill"
- "homepodmini.and.appletv.fill"
- "homepodmini.fill"
- "initWithConnection:queue:"
- "initWithIdentifier:range:"
- "initWithInputStream:outputStream:"
- "initWithRoutingContextUID:multipleBuiltInDevices:"
- "isB520Device"
- "isHomeTheaterB520Device"
- "jsonClientUIDs"
- "lastBootUUID"
- "openCommunicationChannelWithOptions:completionHandler:"
- "personalDeviceState"
- "receivesLongFormAudioFromLocalDevice"
- "recentGroupSessionParticipantsPepper"
- "setAVOutputDevice:"
- "setConnectedClientAuditTokens:"
- "setExpectedClientAuditTokens:"
- "setExporting:"
- "setFallbackOutputDevice:"
- "setInteger:forKey:"
- "setLastBootUUID:"
- "setLocalLastPlayingDate:"
- "setLocalPlaybackState:"
- "setMuted:"
- "setPersonalDeviceState:"
- "setPrimaryID:"
- "shouldInitializeGenericBonjourService"
- "shouldInitializeTelevisionBonjourService"
- "source %@ does not support %@ (destination supportedTypes = %@)"
- "sourcePlayerPath %@ was resolved to %@. Likely there is no now playing app?"
- "stringForKey:"
- "updateDefaultSupportedCommandsData:forClient:"
- "useAPSyncAPI"
- "useDebugAVRouteWithoutVolumeControl"
- "useRSEForProximity"
- "v24@?0@\"NSArray\"8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v32@?0@\"MRAVEndpoint\"8@\"NSArray\"16@\"NSError\"24"
- "v40@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"NSString\"24@\"NSError\"32"
- "v40@?0Q8@\"MRAVEndpoint\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@?0^v8^v16^{__CFString=}24^{__CFError=}32"
- "void _MRMediaRemotePlaybackSessionRequestSupportedType(MRPlayerPath *__strong, MRPlayerPath *__strong, __strong dispatch_queue_t, void (^__strong)(NSString *__strong, NSError *__strong))"
- "{?=\"length\"b1\"location\"b1}"
- "\xf0\xe1"

```
