## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4024.400.1.0.0
-  __TEXT.__text: 0x2bc660
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_methlist: 0x27e34
-  __TEXT.__const: 0x568
-  __TEXT.__cstring: 0x2a673
-  __TEXT.__oslogstring: 0xce41
-  __TEXT.__gcc_except_tab: 0x6308
+4024.510.36.1.0
+  __TEXT.__text: 0x2c23c8
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x293c0
+  __TEXT.__const: 0x570
+  __TEXT.__cstring: 0x2a798
+  __TEXT.__oslogstring: 0xd28d
+  __TEXT.__gcc_except_tab: 0x6348
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa7a0
-  __TEXT.__objc_classname: 0x4a09
-  __TEXT.__objc_methname: 0x485fe
-  __TEXT.__objc_methtype: 0x8a73
-  __TEXT.__objc_stubs: 0x25ea0
-  __DATA_CONST.__got: 0x1278
-  __DATA_CONST.__const: 0xa2e8
-  __DATA_CONST.__objc_classlist: 0x1110
+  __TEXT.__unwind_info: 0xa990
+  __TEXT.__objc_classname: 0x4a18
+  __TEXT.__objc_methname: 0x48f42
+  __TEXT.__objc_methtype: 0x8a97
+  __TEXT.__objc_stubs: 0x26280
+  __DATA_CONST.__got: 0x12a0
+  __DATA_CONST.__const: 0xa528
+  __DATA_CONST.__objc_classlist: 0x1118
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde40
+  __DATA_CONST.__objc_selrefs: 0xe350
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xf58
   __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__auth_got: 0xb38
+  __AUTH_CONST.__auth_got: 0xb20
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0x20300
-  __AUTH_CONST.__objc_const: 0x45138
+  __AUTH_CONST.__const: 0x31e0
+  __AUTH_CONST.__cfstring: 0x20460
+  __AUTH_CONST.__objc_const: 0x42e80
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x7850
-  __AUTH.__data: 0x108
-  __DATA.__objc_ivar: 0x2ffc
-  __DATA.__data: 0x1a88
-  __DATA.__bss: 0x878
+  __AUTH.__objc_data: 0x78a0
+  __AUTH.__data: 0x160
+  __DATA.__objc_ivar: 0x3020
+  __DATA.__data: 0x1a90
+  __DATA.__bss: 0x8b0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x228
-  __DATA_DIRTY.__bss: 0x6d0
+  __DATA_DIRTY.__data: 0x1b0
+  __DATA_DIRTY.__bss: 0x6d8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18827
-  Symbols:   22410
-  CStrings:  18949
+  Functions: 19482
+  Symbols:   23304
+  CStrings:  19054
 
Symbols:
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._groupUIDOverride
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._uidOverride
+ OBJC_IVAR_$__MRAVOutputDeviceDescriptorProtobuf._alternateTransportType
+ OBJC_IVAR_$__MRCommandInfoProtobuf._playbackSessionRequirements
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._delegateAccountData
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._delegateAccountDataType
+ OBJC_IVAR_$__MRContentItemMetadataProtobuf._subtitleShort
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._destinationCommandInfo
+ OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._destinationPlayerPath
+ OBJC_IVAR_$__MRSendCommandResultProtobuf._error
+ _MRMediaRemoteCommandRequiresNowPlayingItemValidation
+ _MRMediaRemoteGetProactiveRecommendedPlayer
+ _MRMediaRemotePlaybackSessionIsMigrationPossible
+ _MRMediaRemotePlaybackSessionMigrateFromOriginToOrigin
+ _MRMediaRemoteProactiveRecommendedPlayerDidChangeNotification
+ _MRMediaRemoteProactiveRecommendedPlayerReasonUserInfoKey
+ _MROutputDeviceIsAVOutputDeviceLocalWithDeviceInfo
+ _MRUserSettingsSystemVolumeCapabilitiesOverrideDidChange
+ _MRUserSettingsSystemVolumeOverrideDidChange
+ _MSVAutoBugCaptureDomainMediaRemote
+ _NSDebugDescriptionErrorKey
+ __UTTypeAppleTV
+ __UTTypeHomePod
+ _kMRMediaRemoteCommandInfoPlaybackSessionRequirements
+ _kMRMediaRemoteOptionDelegateAccountData
+ _kMRMediaRemoteOptionDelegateAccountDataType
- OBJC_IVAR_$_MRAVConcreteOutputDevice._MACAddress
- OBJC_IVAR_$_MRAVConcreteOutputDevice._accessSerialQueue
- OBJC_IVAR_$_MRAVConcreteOutputDevice._airPlayGroupID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._firmwareVersion
- OBJC_IVAR_$_MRAVConcreteOutputDevice._logicalDeviceID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._modelID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._modelSpecificInfo
- OBJC_IVAR_$_MRAVConcreteOutputDevice._nearbyObject
- OBJC_IVAR_$_MRAVConcreteOutputDevice._overrideGroupID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._overrideUID
- OBJC_IVAR_$_MRAVConcreteOutputDevice._playingPairedDeviceName
- OBJC_IVAR_$_MRAVConcreteOutputDevice._uid
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._has
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._length
- OBJC_IVAR_$__MRPlaybackSessionRequestProtobuf._location
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
- _MRUserSettingsForceEnableCECVolumeDidChange
- _fmod
- _fmodf
- _objc_release_x2
CStrings:
+ "\x01\x14\x11\x11!"
+ "\x01\x15"
+ "\x01x\x13\x12\x14\x18"
+ "\x02\x1b"
+ "\x02#\x13\x11"
+ "\x03%"
+ "\x05\x13\x12%\x1c\x11"
+ "%@\n  designatedGroupLeader = %@\n  isLocalDeviceDesignatedGroupLeader = %@\n  outputContextSupportsVolumeControl = %@\n  localVolume = %lf\n  localVolumeCapabilities = %@\n  localVolumeMute = %u\n  OutputContext = %@\n"
+ "%@ -> %@  will not work with AVOD sourced from Discovery"
+ "%@ -> %lf will not work with AVOD sourced from Discovery"
+ "%@ -> %u will not work with AVOD sourced from Discovery"
+ "%@ outputContextSupportsVolumeControl = %@ localVolume = %lf, localVolumeCapabilities = %@ localVolumeMute = %u"
+ "%{public}@"
+ "05ac:110"
+ "76,4363"
+ "76,8223"
+ "<%@: source=%@, identifier=%@, title=%@, artist=%@, playbackIdentifier=%@ intentHasArt=%@, artLoaded=%@, artSize: %ld>"
+ "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@>"
+ "<%@:%p multipleBuiltIn = %s>"
+ "@\"MRCommandInfo\""
+ "@\"MRRateLimiter\""
+ "@28@0:8B16q20"
+ "@32@0:8@?16@?24"
+ "@36@0:8@16B24Q28"
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
+ "Excessive PlayerPathInvalidationhandlers"
+ "Failed to find symbol with model: %{public}@ variant options: %lu error: %{public}@ symbol:%{public}@"
+ "Failed to resolve destination player path"
+ "Failed to resolve player path, but did not receive an error: sourcePlayerPath=%@"
+ "Failed to resolve source player path"
+ "MRMediaRemoteProactiveRecommendedPlayerDidChangeNotification"
+ "MRMediaRemoteProactiveRecommendedPlayerReasonUserInfoKey"
+ "MRUserSettingsSystemVolumeCapabilitiesOverrideDidChange"
+ "MRUserSettingsSystemVolumeOverrideDidChange"
+ "Mute"
+ "No suggestion found for playback identifier"
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
+ "T@\"NSString\",R,N,V_playbackIdentifier"
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
+ "[OutputContext] setOutputDevices took %lf seconds"
+ "_MRPSMRecipe"
+ "_activeRouteIDsChangedCallback"
+ "_alternateTransportType"
+ "_artworkOnly"
+ "_avOutputContextLock"
+ "_callOutQueue"
+ "_canSetVolume"
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
+ "_playbackIdentifier"
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
+ "initWithErrorCode:"
+ "initWithIntent:playbackIdentifier:"
+ "initWithMultipleBuiltInDevices:sourceType:"
+ "isArtworkOnly"
+ "isB515CDevice"
+ "isB825Device"
+ "isHomePodMiniDevice"
+ "isLocalDeviceAirPlayActive"
+ "isLocalDeviceAirPlayActiveCallback"
+ "isPreferredClusterLeader"
+ "itemID"
+ "kMRMediaRemoteCommandInfoPlaybackSessionRequirements"
+ "kMRMediaRemoteOptionDelegateAccountData"
+ "kMRMediaRemoteOptionDelegateAccountDataType"
+ "legacySetPlaybackSessionWithSessionType:"
+ "loggingQueue"
+ "msv_compactDescription"
+ "notPossibleWithError:"
+ "oneShotSetPlaybackSessionWithCommandInfo:"
+ "outputDevicesForUID:"
+ "pauseOutputDeviceUIDs.xpcInterface"
+ "performWithPlaybackIdentifier:completion:"
+ "playSuggestionWithPlaybackIdentifier:completion:"
+ "playSuggestionWithPlaybackIdentifier:onDeviceWithUID:completion:"
+ "playbackIdentifier"
+ "playbackSessionRequirements"
+ "proactiveRecommendedPlayerInterval"
+ "replyQueue"
+ "sendQueue"
+ "setActiveRouteIDsChangedCallback:"
+ "setAlternateTransportType:"
+ "setArtworkOnly:"
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
+ "v24@?0@\"MRMediaSuggestion\"8@\"NSError\"16"
+ "v24@?0@\"MRPlayerPath\"8@\"NSString\"16"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"NSError\"24"
+ "v32@?0@\"MRPlayerPath\"8@\"MRPlayerPath\"16@\"_MRPSMRecipe\"24"
+ "v32@?0Q8@\"MRAVEndpoint\"16@?<v@?@\"NSError\">24"
+ "void _MRPSMDetermineRecipe(MRPlayerPath *__strong, MROrigin *__strong, __strong dispatch_queue_t, void (^__strong)(MRPlayerPath *__strong, MRPlayerPath *__strong, _MRPSMRecipe *__strong))"
+ "watchIntentionalRouting"
+ "watch_intentional_routing"
+ "\x8f\t$\x13\x11\x11\"\x12\x15"
+ "\xf01\x11\x13\"\x113"
+ "\xf0\xd1"
+ "\xf0\xf0\xcf\x0f\nb\""
+ "\xf1\x12\x13\x18\x16\x12!%\x11\x125\x12\x13\x11\x11"
- "\x01\x12"
- "\x01\x14\x13"
- "\x01x\x13\x12\x15\x17"
- "\x02#\x13"
- "\x03$"
- "\x04\x13\x12%\x1c\x11"
- "\x04\x14\x15"
- "%@\n  designatedGroupLeader = %@\n  isLocalDeviceDesignatedGroupLeader = %@\n  outputContextSupportsVolumeControl = %@\n  AVSystemController.localVolume = %lf\n  AVSystemController.volumeCapabilities = %@\n  AVSystemController.localVolumeMute = %u\n  OutputContext = %@\n"
- "%@ -> %u"
- "%@ options do not match. source=%@ currentType=%@ destination=%@ supportedTypes=%@"
- "%@ outputContextSupportsVolumeControl = %@ (ignoreThis: localVolume = %lf, local volume capabilities = %@ localVolumeMute = %u)"
- "%@OutputDevicesInGroup"
- "-[MRAVOutputContext isVolumeControlAvailable]"
- "/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction"
- "<%@: source=%@, identifier=%@, title=%@, artist=%@, intentHasArt=%@, artLoaded=%@, artSize: %ld>"
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
- "T@\"MRAVOutputDeviceSourceInfo\",&,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSString\",C,N,V_airPlayGroupID"
- "T@\"NSString\",C,N,V_parentGroupIdentifier"
- "T@\"NSString\",C,N,V_primaryID"
- "T@\"NSString\",R,N,V_routingContextUID"
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
- "[AVEndpoint] Failed to select playback category on auxiliary context. %{public}@"
- "[ConcreteOutputContext] Ignoring request to attempt logical device recovery because APSync API is enabled."
- "[ConcreteOutputContext] ProvidesVolumeFeatures did change to %{BOOL}u, capabilities: %{public}@  for context: %{public}@ - %{public}@"
- "[MRNowPlayingOriginClientRequests] %{public}@ UpdatingCache: deviceInfo %{public}@"
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
- "initWithRoutingContextUID:multipleBuiltInDevices:"
- "isB520Device"
- "isHomeTheaterB520Device"
- "jsonClientUIDs"
- "lastBootUUID"
- "personalDeviceState"
- "receivesLongFormAudioFromLocalDevice"
- "recentGroupSessionParticipantsPepper"
- "setAVOutputDevice:"
- "setConnectedClientAuditTokens:"
- "setExpectedClientAuditTokens:"
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
- "\x8f\a$\x13\x11\x11\"\x12\x15"
- "\xf01\x11\x13!\x113"
- "\xf0\xe1"
- "\xf0\xf0\xcf\x0f\tb\""
- "\xf1\x12\x13\x18\x16\x12!%\x11\x125\x12\x12\x11\x11"

```
