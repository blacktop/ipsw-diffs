## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-  __TEXT.__text: 0x31e084
-  __TEXT.__objc_methlist: 0x2b73c
+  __TEXT.__text: 0x31e514
+  __TEXT.__objc_methlist: 0x2b7ac
   __TEXT.__const: 0x5c0
-  __TEXT.__cstring: 0x2c324
-  __TEXT.__oslogstring: 0xcdc9
-  __TEXT.__gcc_except_tab: 0x5c34
+  __TEXT.__cstring: 0x2c444
+  __TEXT.__oslogstring: 0xd205
+  __TEXT.__gcc_except_tab: 0x582c
   __TEXT.__dlopen_cstrs: 0x40b
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xb1c0
+  __TEXT.__unwind_info: 0xb168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b30
+  __DATA_CONST.__const: 0x4b40
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf058
+  __DATA_CONST.__objc_selrefs: 0xf090
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xff0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x1408
-  __AUTH_CONST.__const: 0xa3e0
-  __AUTH_CONST.__cfstring: 0x23a40
-  __AUTH_CONST.__objc_const: 0x46378
+  __DATA_CONST.__got: 0x1418
+  __AUTH_CONST.__const: 0xa410
+  __AUTH_CONST.__cfstring: 0x23ca0
+  __AUTH_CONST.__objc_const: 0x46468
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xa90
-  __AUTH.__objc_data: 0x82a0
-  __DATA.__objc_ivar: 0x32c4
+  __AUTH.__objc_data: 0x8430
+  __DATA.__objc_ivar: 0x32d0
   __DATA.__data: 0x1a40
-  __DATA.__bss: 0x8f0
+  __DATA.__bss: 0x868
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2ee0
+  __DATA_DIRTY.__objc_data: 0x2d50
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x4f8
+  __DATA_DIRTY.__bss: 0x5a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20575
-  Symbols:   37336
-  CStrings:  10918
+  Functions: 20569
+  Symbols:   37350
+  CStrings:  10968
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[MRIRRoute _parsedCandidateIdentifier:]
+ -[MRAVConcreteRoutingDiscoverySession _maybeScheduleReload]
+ -[MRAVConcreteRoutingDiscoverySession setAlwaysAllowUpdates:]
+ -[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:details:queue:completion:]
+ -[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:details:queue:completion:]
+ -[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]
+ -[MRAVRoutingDiscoverySession clientAlwaysAllowUpdatesStates]
+ -[MRAVRoutingDiscoverySession setClientAlwaysAllowUpdatesStates:]
+ -[MRAVRoutingDiscoverySessionWrapper _addCallbacksForSession:]
+ -[MRAVRoutingDiscoverySessionWrapper _currentVisibleEndpointsForSession:]
+ -[MRAVRoutingDiscoverySessionWrapper _currentVisibleOutputDevicesForSession:]
+ -[MRAVRoutingDiscoverySessionWrapper _removeCallbacksForSession:]
+ -[MRAVRoutingDiscoverySessionWrapper reevaluateAlwaysAllowUpdatesForSession:]
+ -[MRIRRoute candidateIdentifier]
+ -[MRIRRoute protocolIdentifier]
+ -[MRIRRoute setProtocolIdentifier:]
+ -[MRStaticRouteBannerRequest protocolName]
+ -[MRStaticRouteBannerRequest protocolUID]
+ -[MRStaticRouteBannerRequest setProtocolName:]
+ -[MRStaticRouteBannerRequest setProtocolUID:]
+ -[MRUserSettings companionRemoteControlServiceConnectionDelay]
+ -[MRUserSettings externalDeviceArtificialConnectionDelay]
+ -[MRUserSettings remoteSessionDefaultAssertionInterval]
+ GCC_except_table113
+ GCC_except_table139
+ OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._outputDevicesCacheStale
+ OBJC_IVAR_$_MRAVRoutingDiscoverySession._clientAlwaysAllowUpdatesStates
+ OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._endpointsAwaitingInitialFire
+ OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._endpointsCallbackToken
+ OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._outputDevicesAwaitingInitialFire
+ OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._outputDevicesCallbackToken
+ OBJC_IVAR_$_MRIRRoute._protocolIdentifier
+ OBJC_IVAR_$_MRStaticRouteBannerRequest._protocolName
+ OBJC_IVAR_$_MRStaticRouteBannerRequest._protocolUID
+ _MRMediaRemoteRouteStatusErrorDomain
+ __100-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:details:queue:completion:]_block_invoke
+ __102-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:details:queue:completion:]_block_invoke
+ __105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke
+ __58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke
+ ___100-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:details:queue:completion:]_block_invoke
+ ___102-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:details:queue:completion:]_block_invoke
+ ___102-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:details:queue:completion:]_block_invoke_2
+ ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke
+ ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_2
+ ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_3
+ ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_4
+ ___49-[MRAVRoutingDiscoverySession alwaysAllowUpdates]_block_invoke
+ ___53-[MRAVRoutingDiscoverySession setAlwaysAllowUpdates:]_block_invoke
+ ___55-[MRUserSettings remoteSessionDefaultAssertionInterval]_block_invoke
+ ___57-[MRUserSettings externalDeviceArtificialConnectionDelay]_block_invoke
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_2
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_3
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_4
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_5
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_6
+ ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_7
+ ___59-[MRAVConcreteRoutingDiscoverySession _maybeScheduleReload]_block_invoke
+ ___59-[MRAVConcreteRoutingDiscoverySession _maybeScheduleReload]_block_invoke_2
+ ___60-[MRAVRoutingDiscoverySessionWrapper setAlwaysAllowUpdates:]_block_invoke
+ ___62-[MRAVRoutingDiscoverySessionWrapper _addCallbacksForSession:]_block_invoke
+ ___62-[MRAVRoutingDiscoverySessionWrapper _addCallbacksForSession:]_block_invoke_2
+ ___62-[MRUserSettings companionRemoteControlServiceConnectionDelay]_block_invoke
+ ___block_descriptor_160_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
+ ___block_descriptor_40_e8_32w_e8_v16?08l
+ ___block_descriptor_48_e8_32s40s_e31_v32?08?<v?"NSArray">16^B24l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32l
+ ___copy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r
+ ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r
+ _kMRMediaRemotePushTokensUserInfoKey
+ _objc_msgSend$_addCallbacksForSession:
+ _objc_msgSend$_currentVisibleEndpointsForSession:
+ _objc_msgSend$_currentVisibleOutputDevicesForSession:
+ _objc_msgSend$_maybeScheduleReload
+ _objc_msgSend$_parsedCandidateIdentifier:
+ _objc_msgSend$_removeCallbacksForSession:
+ _objc_msgSend$airplayProtocolUID
+ _objc_msgSend$clientAlwaysAllowUpdatesStates
+ _objc_msgSend$protocolIdentifier
+ _objc_msgSend$reevaluateAlwaysAllowUpdatesForSession:
+ _objc_msgSend$searchEndpointsForGroupUID:timeout:details:queue:completion:
+ _objc_msgSend$searchEndpointsWithPredicate:timeout:details:queue:completion:
+ _objc_msgSend$searchOutputDevices:protocolUID:timeout:details:queue:completion:
+ _objc_msgSend$setCarCount:
+ _objc_msgSend$setDesktopCount:
+ _objc_msgSend$setGamingConsoleCount:
+ _objc_msgSend$setLaptopCount:
+ _objc_msgSend$setPhoneCount:
+ _objc_msgSend$setProtocolIdentifier:
+ _objc_msgSend$setTabletCount:
+ _objc_msgSend$setWearableCount:
+ _objc_msgSend$setWebCount:
+ companionRemoteControlServiceConnectionDelay.__interval
+ companionRemoteControlServiceConnectionDelay.__once
+ externalDeviceArtificialConnectionDelay.__interval
+ externalDeviceArtificialConnectionDelay.__once
+ remoteSessionDefaultAssertionInterval.__interval
+ remoteSessionDefaultAssertionInterval.__once
- -[MRAVConcreteRoutingDiscoverySession routingContextUID]
- -[MRAVConcreteRoutingDiscoverySession setRoutingContextUID:]
- -[MRAVConcreteRoutingDiscoverySession setTargetAudioSessionID:]
- -[MRAVConcreteRoutingDiscoverySession targetAudioSessionID]
- -[MRAVRoutingDiscoverySessionWrapper transferCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferEndpointsAddedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferEndpointsChangedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferEndpointsModifiedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferEndpointsRemovedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesAddedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesChangedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesModifiedCallbacksFromSession:toSession:]
- -[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesRemovedCallbacksFromSession:toSession:]
- -[MRUserSettings externalDeviceArtificalConnectionDelay]
- -[MRUserSettings remoteSessionGracePeriodDuration]
- GCC_except_table101
- GCC_except_table108
- GCC_except_table82
- OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._clientProvidedTargetAudioSessionID
- OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._routingContextUID
- OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._targetAudioSessionID
- OBJC_IVAR_$_MRAVRoutingDiscoverySession._alwaysAllowUpdates
- OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._endpointsTokensMap
- OBJC_IVAR_$_MRAVRoutingDiscoverySessionWrapper._outputDevicesTokensMap
- __101-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:reason:queue:completion:]_block_invoke
- __101-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:reason:queue:completion:]_block_invoke_2
- __92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke
- __92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke_2
- __99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke
- ___101-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:reason:queue:completion:]_block_invoke
- ___101-[MRAVLightweightReconnaissanceSession searchEndpointsWithPredicate:timeout:reason:queue:completion:]_block_invoke_2
- ___56-[MRAVConcreteRoutingDiscoverySession routingContextUID]_block_invoke
- ___56-[MRUserSettings externalDeviceArtificalConnectionDelay]_block_invoke
- ___60-[MRAVConcreteRoutingDiscoverySession setRoutingContextUID:]_block_invoke
- ___64-[MRAVRoutingDiscoverySessionWrapper addEndpointsAddedCallback:]_block_invoke_2
- ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsChangedCallback:]_block_invoke_2
- ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsRemovedCallback:]_block_invoke
- ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsRemovedCallback:]_block_invoke_2
- ___67-[MRAVRoutingDiscoverySessionWrapper addEndpointsModifiedCallback:]_block_invoke
- ___67-[MRAVRoutingDiscoverySessionWrapper addEndpointsModifiedCallback:]_block_invoke_2
- ___68-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesAddedCallback:]_block_invoke_2
- ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesChangedCallback:]_block_invoke_2
- ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesRemovedCallback:]_block_invoke
- ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesRemovedCallback:]_block_invoke_2
- ___71-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesModifiedCallback:]_block_invoke
- ___71-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesModifiedCallback:]_block_invoke_2
- ___91-[MRAVRoutingDiscoverySessionWrapper transferEndpointsAddedCallbacksFromSession:toSession:]_block_invoke
- ___91-[MRAVRoutingDiscoverySessionWrapper transferEndpointsAddedCallbacksFromSession:toSession:]_block_invoke_2
- ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke
- ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke_2
- ___93-[MRAVRoutingDiscoverySessionWrapper transferEndpointsChangedCallbacksFromSession:toSession:]_block_invoke
- ___93-[MRAVRoutingDiscoverySessionWrapper transferEndpointsChangedCallbacksFromSession:toSession:]_block_invoke_2
- ___93-[MRAVRoutingDiscoverySessionWrapper transferEndpointsRemovedCallbacksFromSession:toSession:]_block_invoke
- ___93-[MRAVRoutingDiscoverySessionWrapper transferEndpointsRemovedCallbacksFromSession:toSession:]_block_invoke_2
- ___94-[MRAVRoutingDiscoverySessionWrapper transferEndpointsModifiedCallbacksFromSession:toSession:]_block_invoke
- ___94-[MRAVRoutingDiscoverySessionWrapper transferEndpointsModifiedCallbacksFromSession:toSession:]_block_invoke_2
- ___95-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesAddedCallbacksFromSession:toSession:]_block_invoke
- ___95-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesAddedCallbacksFromSession:toSession:]_block_invoke_2
- ___97-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesChangedCallbacksFromSession:toSession:]_block_invoke
- ___97-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesChangedCallbacksFromSession:toSession:]_block_invoke_2
- ___97-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesRemovedCallbacksFromSession:toSession:]_block_invoke
- ___97-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesRemovedCallbacksFromSession:toSession:]_block_invoke_2
- ___98-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesModifiedCallbacksFromSession:toSession:]_block_invoke
- ___98-[MRAVRoutingDiscoverySessionWrapper transferOutputDevicesModifiedCallbacksFromSession:toSession:]_block_invoke_2
- ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32l
- ___block_descriptor_64_e8_32s40s48bs56r_e34_v24?0"MRAVEndpoint"8"NSError"16l
- ___block_descriptor_96_e8_32r40r48r56r64r72r80r88r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
- ___copy_helper_block_e8_32r40r48r56r64r72r80r88r
- ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r
- _objc_msgSend$transferCallbacksFromSession:toSession:
- _objc_msgSend$transferEndpointsAddedCallbacksFromSession:toSession:
- _objc_msgSend$transferEndpointsChangedCallbacksFromSession:toSession:
- _objc_msgSend$transferEndpointsModifiedCallbacksFromSession:toSession:
- _objc_msgSend$transferEndpointsRemovedCallbacksFromSession:toSession:
- _objc_msgSend$transferOutputDevicesAddedCallbacksFromSession:toSession:
- _objc_msgSend$transferOutputDevicesChangedCallbacksFromSession:toSession:
- _objc_msgSend$transferOutputDevicesModifiedCallbacksFromSession:toSession:
- _objc_msgSend$transferOutputDevicesRemovedCallbacksFromSession:toSession:
- externalDeviceArtificalConnectionDelay.__interval
- externalDeviceArtificalConnectionDelay.__once
CStrings:
+ " protocolName: %@"
+ " protocolUID: %@"
+ "%@%@\n%@ %@ %@"
+ "%ld bytes"
+ "MRMediaRemoteRouteStatusErrorDomain"
+ "O"
+ "Received Notification %@"
+ "Update: %{public}@<%{public}@> audio session found %lu non-RC / custom-protocol devices, completing without RC discovery"
+ "Update: %{public}@<%{public}@> audio session found no legacy / custom-protocol devices, falling back to RemoteControl discovery"
+ "[ExternalRoutingDiscoverySession] Destination not yet ready. Enqueuing discoveryMode change..."
+ "[MRAVVolumeClientEndpoint] ResolvedOutputDevices: %{public}@"
+ "[MRNowPlayingPushTokenManager]   token key: %{public}@ (%ld bytes)"
+ "[MRNowPlayingPushTokenManager] _handleTokensDidChange: delivering token to observer for %{public}@ (%ld bytes)"
+ "[MRNowPlayingPushTokenManager] _handleTokensDidChange: no token for observer %{public}@"
+ "[MRNowPlayingPushTokenManager] _handleTokensDidChange: notifying %ld observer(s)"
+ "[MRNowPlayingPushTokenManager] _handleTokensDidChange: received %ld token(s)"
+ "[MRNowPlayingPushTokenManager] observeUpdateTokenUpdatesForSessionID: %{public}@"
+ "[MRNowPlayingPushTokenManager] observeUpdateTokenUpdatesForSessionID: %{public}@ - delivering initial token (%ld bytes)"
+ "[MRNowPlayingPushTokenManager] observeUpdateTokenUpdatesForSessionID: %{public}@ - no initial token, refreshing from daemon"
+ "[MRNowPlayingPushTokenManager] updateTokenForSessionID: %{public}@ -> %{public}@"
+ "car: %lu;"
+ "companionRemoteControlServiceConnectionDelay"
+ "desktop: %lu;"
+ "externalDeviceArtificialConnectionDelay"
+ "gamingConsole: %lu;"
+ "kMRMediaRemotePushTokensUserInfoKey"
+ "laptop: %lu;"
+ "nil"
+ "phone: %lu;"
+ "pn"
+ "protocolIdentifier"
+ "puid"
+ "remoteSessionDefaultAssertionInterval"
+ "routeIdentifier"
+ "searchEndpointsWithPredicate"
+ "tablet: %lu;"
+ "v16@?0@8"
+ "wearable: %lu;"
+ "web: %lu;"
- "%@%@\n%@ %@"
- "MRAVLightweightReconnaissanceSession.searchOutputDevices-%@"
- "Receieved Notification %@"
- "RemoteSessionGracePeriodDuration"
- "[MRAVRoutingDiscoverySessionWrapper] <%p> Transferring callbacks from: %{public}@ to: %{public}@"
- "[MRAVVolumeClientEndpoint] ResolvedOutputDevices: %@"
- "externalDeviceArtificalConnectionDelay"
- "now_playing_agent"

```
