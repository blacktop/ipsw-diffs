## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.410.1.0.0
-  __TEXT.__text: 0x2f4480
+4025.510.35.1.0
+  __TEXT.__text: 0x314648
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x2b0a0
-  __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2bdb2
-  __TEXT.__oslogstring: 0xdbca
-  __TEXT.__gcc_except_tab: 0x66a0
+  __TEXT.__objc_methlist: 0x2b430
+  __TEXT.__const: 0x5f0
+  __TEXT.__cstring: 0x2bfdc
+  __TEXT.__oslogstring: 0xdc7a
+  __TEXT.__gcc_except_tab: 0x63b4
   __TEXT.__dlopen_cstrs: 0x514
-  __TEXT.__ustring: 0x796
-  __TEXT.__unwind_info: 0xb2b0
-  __TEXT.__objc_classname: 0x4dad
-  __TEXT.__objc_methname: 0x4d504
-  __TEXT.__objc_methtype: 0x90b9
-  __TEXT.__objc_stubs: 0x28460
-  __DATA_CONST.__got: 0x1440
-  __DATA_CONST.__const: 0xb200
-  __DATA_CONST.__objc_classlist: 0x11a8
+  __TEXT.__ustring: 0x7b8
+  __TEXT.__unwind_info: 0xcc28
+  __TEXT.__objc_classname: 0x4e1c
+  __TEXT.__objc_methname: 0x4dabe
+  __TEXT.__objc_methtype: 0x913a
+  __TEXT.__objc_stubs: 0x28780
+  __DATA_CONST.__got: 0x1450
+  __DATA_CONST.__const: 0xb2f8
+  __DATA_CONST.__objc_classlist: 0x11b8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x260
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf010
+  __DATA_CONST.__objc_selrefs: 0xf138
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xfd0
+  __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
-  __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0x232e0
-  __AUTH_CONST.__objc_const: 0x45ca0
+  __AUTH_CONST.__const: 0x3120
+  __AUTH_CONST.__cfstring: 0x234e0
+  __AUTH_CONST.__objc_const: 0x46188
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8390
+  __AUTH.__objc_data: 0x8340
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x3234
-  __DATA.__data: 0x1ce0
-  __DATA.__bss: 0x870
+  __DATA.__objc_ivar: 0x3268
+  __DATA.__data: 0x1d40
+  __DATA.__bss: 0x818
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2d00
+  __DATA_DIRTY.__objc_data: 0x2df0
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x500
+  __DATA_DIRTY.__bss: 0x580
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70A8F362-ACCE-309F-9082-880F8D25F3D6
-  Functions: 20166
-  Symbols:   55370
-  CStrings:  24409
+  UUID: 734A53CF-F9B2-35B7-85F4-85B745E71592
+  Functions: 20441
+  Symbols:   56242
+  CStrings:  24515
 
Symbols:
+ +[MRAVEndpoint(Intent_Grouping) addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
+ +[MRAVEndpoint(Intent_Grouping) moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
+ +[MRAVEndpoint(Intent_Grouping) pauseOutputDeviceUIDs:behavior:details:queue:completion:]
+ +[MRAVEndpoint(Intent_Grouping) pauseOutputDeviceUIDs:details:queue:completion:]
+ +[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]
+ +[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.1
+ +[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.2
+ +[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]
+ +[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]
+ +[MRAVEndpoint(Intent_Volume) changeVolume:action:outputDeviceUIDs:timeout:details:completion:]
+ +[MRAVEndpoint(Intent_Volume) volumeCapabilitiesForOutputDeviceUID:timeout:details:completion:]
+ +[MRAVEndpoint(Intent_Volume) volumeForOutputDeviceUID:timeout:details:completion:]
+ +[MRAVOutputDevice alternativeLocalDeviceUIDPlaceholder]
+ +[MRAVOutputDevice localDeviceUIDPlaceholder]
+ +[MRAppEntityPath supportsSecureCoding]
+ +[_MRContentItemMetadataProtobuf entityPathsType]
+ -[MRAVOutputContext dealloc]
+ -[MRAVOutputContext init]
+ -[MRAVReconnaissanceSession beginSearchWithTimeout:endpointsAndMissingOutputDevicesCompletion:]
+ -[MRAVRoutingDiscoverySessionWrapper _shouldNotify]
+ -[MRAppEntityPath .cxx_destruct]
+ -[MRAppEntityPath bundleIdentifier]
+ -[MRAppEntityPath copyWithZone:]
+ -[MRAppEntityPath description]
+ -[MRAppEntityPath encodeWithCoder:]
+ -[MRAppEntityPath hash]
+ -[MRAppEntityPath initWithBundleIdentifier:typeIdentifier:instanceIdentifier:]
+ -[MRAppEntityPath initWithCoder:]
+ -[MRAppEntityPath initWithProtobuf:]
+ -[MRAppEntityPath instanceIdentifier]
+ -[MRAppEntityPath isEqual:]
+ -[MRAppEntityPath protobuf]
+ -[MRAppEntityPath setBundleIdentifier:]
+ -[MRAppEntityPath setInstanceIdentifier:]
+ -[MRAppEntityPath setTypeIdentifier:]
+ -[MRAppEntityPath typeIdentifier]
+ -[MRContentItemMetadata entityPaths]
+ -[MRContentItemMetadata setEntityPaths:]
+ -[MRExternalOutputContextDataSource initializeVolumeCapabilitiesForLegacyClients]
+ -[MRExternalOutputContextDataSource initializeVolumeCapabilitiesForLegacyClients].cold.1
+ -[MRGroupTopologyModificationRequest outputDevicesUIDsString]
+ -[MRMediaRemoteService activeCallIdentifierDidChange:]
+ -[MRMediaRemoteService callAgent]
+ -[MRMediaRemoteService handleAgentMessage:]
+ -[MRMediaRemoteService handleGetNumberOfActiveCallsMessage:]
+ -[MRMediaRemoteService hasRegisteredAgents]
+ -[MRMediaRemoteService registerCallAgent:queue:]
+ -[MRMediaRemoteService setCallAgent:]
+ -[MRMediaRemoteService setHasRegisteredAgents:]
+ -[MROutputContextController initVolume]
+ -[MRRollingWindowActivityTracker _onQueue_stopActivityTracking]
+ -[MRRollingWindowActivityTracker initWithActivityName:maxAllowedTime:windowDuration:repeats:handler:]
+ -[MRRollingWindowActivityTracker repeats]
+ -[MRSharedSettings supportNowPlayingDrivenAgent]
+ -[MRUserSettings nowPlayingAppStackFailedCanBeNowPlayingInterval]
+ -[_MRAppEntityPathProtobuf .cxx_destruct]
+ -[_MRAppEntityPathProtobuf bundleIdentifier]
+ -[_MRAppEntityPathProtobuf copyTo:]
+ -[_MRAppEntityPathProtobuf copyWithZone:]
+ -[_MRAppEntityPathProtobuf description]
+ -[_MRAppEntityPathProtobuf dictionaryRepresentation]
+ -[_MRAppEntityPathProtobuf hasBundleIdentifier]
+ -[_MRAppEntityPathProtobuf hasInstanceIdentifier]
+ -[_MRAppEntityPathProtobuf hasTypeIdentifier]
+ -[_MRAppEntityPathProtobuf hash]
+ -[_MRAppEntityPathProtobuf instanceIdentifier]
+ -[_MRAppEntityPathProtobuf isEqual:]
+ -[_MRAppEntityPathProtobuf mergeFrom:]
+ -[_MRAppEntityPathProtobuf readFrom:]
+ -[_MRAppEntityPathProtobuf setBundleIdentifier:]
+ -[_MRAppEntityPathProtobuf setInstanceIdentifier:]
+ -[_MRAppEntityPathProtobuf setTypeIdentifier:]
+ -[_MRAppEntityPathProtobuf typeIdentifier]
+ -[_MRAppEntityPathProtobuf writeTo:]
+ -[_MRCommandOptionsProtobuf hasUserActionTimestamp]
+ -[_MRCommandOptionsProtobuf setHasUserActionTimestamp:]
+ -[_MRCommandOptionsProtobuf setUserActionTimestamp:]
+ -[_MRCommandOptionsProtobuf userActionTimestamp]
+ -[_MRContentItemMetadataProtobuf addEntityPaths:]
+ -[_MRContentItemMetadataProtobuf clearEntityPaths]
+ -[_MRContentItemMetadataProtobuf entityPathsAtIndex:]
+ -[_MRContentItemMetadataProtobuf entityPathsCount]
+ -[_MRContentItemMetadataProtobuf entityPaths]
+ -[_MRContentItemMetadataProtobuf setEntityPaths:]
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table88
+ OBJC_IVAR_$__MRAppEntityPathProtobuf._bundleIdentifier
+ OBJC_IVAR_$__MRAppEntityPathProtobuf._instanceIdentifier
+ OBJC_IVAR_$__MRAppEntityPathProtobuf._typeIdentifier
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._userActionTimestamp
+ OBJC_IVAR_$__MRContentItemMetadataProtobuf._entityPaths
+ _MRAVEndpointResolveOutputDeviceUID
+ _MRAVEndpointResolveOutputDeviceUIDs
+ _MRMediaRemoteRegisterAgentHandlers
+ _MRMediaRemoteServiceNotifyAgentAvailable
+ _OBJC_CLASS_$_MRAppEntityPath
+ _OBJC_CLASS_$__MRAppEntityPathProtobuf
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._reloadCoalescingSource
+ _OBJC_IVAR_$_MRAVOutputContext._reloadCoalescingSource
+ _OBJC_IVAR_$_MRAppEntityPath._bundleIdentifier
+ _OBJC_IVAR_$_MRAppEntityPath._instanceIdentifier
+ _OBJC_IVAR_$_MRAppEntityPath._typeIdentifier
+ _OBJC_IVAR_$_MRContentItemMetadata._entityPaths
+ _OBJC_IVAR_$_MRMediaRemoteService._callAgent
+ _OBJC_IVAR_$_MRMediaRemoteService._hasRegisteredAgents
+ _OBJC_IVAR_$_MROutputContextController._initializationGroup
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._repeats
+ _OBJC_METACLASS_$_MRAppEntityPath
+ _OBJC_METACLASS_$__MRAppEntityPathProtobuf
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ __MRAVEndpointGetIntentServiceReplyDispatchQueue
+ __MRAVEndpointGetIntentServiceReplyDispatchQueue.cold.1
+ __MRAVEndpointGetIntentServiceReplyDispatchQueue.onceToken
+ __MRAVEndpointGetIntentServiceReplyDispatchQueue.queue
+ __MRAppEntityPathProtobufReadFrom
+ __OBJC_$_CLASS_METHODS_MRAVEndpoint(Deprecated|Intent_Playback|Intent_Grouping|Intent_Volume)
+ __OBJC_$_CLASS_METHODS_MRAppEntityPath
+ __OBJC_$_CLASS_PROP_LIST_MRAppEntityPath
+ __OBJC_$_INSTANCE_METHODS_MRAVEndpoint(Deprecated|Intent_Playback|Intent_Grouping|Intent_Volume)
+ __OBJC_$_INSTANCE_METHODS_MRAppEntityPath
+ __OBJC_$_INSTANCE_METHODS__MRAppEntityPathProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRAppEntityPath
+ __OBJC_$_INSTANCE_VARIABLES__MRAppEntityPathProtobuf
+ __OBJC_$_PROP_LIST_MRAppEntityPath
+ __OBJC_$_PROP_LIST__MRAppEntityPathProtobuf
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRCallAgentDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRCallAgentDelegate
+ __OBJC_$_PROTOCOL_REFS_MRCallAgentDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MRAppEntityPath
+ __OBJC_CLASS_PROTOCOLS_$_MRMediaRemoteService
+ __OBJC_CLASS_PROTOCOLS_$__MRAppEntityPathProtobuf
+ __OBJC_CLASS_RO_$_MRAppEntityPath
+ __OBJC_CLASS_RO_$__MRAppEntityPathProtobuf
+ __OBJC_LABEL_PROTOCOL_$_MRCallAgentDelegate
+ __OBJC_METACLASS_RO_$_MRAppEntityPath
+ __OBJC_METACLASS_RO_$__MRAppEntityPathProtobuf
+ __OBJC_PROTOCOL_$_MRCallAgentDelegate
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.617
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.619
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.624
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.631
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.620
+ ___120+[MRAVEndpoint(Intent_Grouping) addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
+ ___121+[MRAVEndpoint(Intent_Grouping) moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
+ ___122+[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke
+ ___122+[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.69
+ ___122+[MRAVEndpoint(Intent_Playback) prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.cold.1
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.597
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.606
+ ___123+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke
+ ___123+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.32
+ ___123+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.cold.1
+ ___123+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke_2
+ ___139+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke
+ ___139+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.44
+ ___139+[MRAVEndpoint(Intent_Playback) sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.cold.1
+ ___25-[MRAVOutputContext init]_block_invoke
+ ___39-[MROutputContextController initVolume]_block_invoke
+ ___39-[MROutputContextController initVolume]_block_invoke.306
+ ___39-[MROutputContextController initVolume]_block_invoke.308
+ ___39-[MROutputContextController initVolume]_block_invoke.310
+ ___42-[MRContentItemMetadata initWithProtobuf:]_block_invoke_2
+ ___43-[MRMediaRemoteService handleAgentMessage:]_block_invoke
+ ___46-[MRContentItemMetadata protobufWithEncoding:]_block_invoke_2
+ ___49-[MRContentItemMetadata dictionaryRepresentation]_block_invoke_2
+ ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.470
+ ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.414
+ ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.51
+ ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.53
+ ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.417
+ ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.502
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.511
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.403
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.403.cold.1
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.404
+ ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.415
+ ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.421
+ ___64-[MRAVRoutingDiscoverySessionWrapper addEndpointsAddedCallback:]_block_invoke
+ ___64-[MRAVRoutingDiscoverySessionWrapper addEndpointsAddedCallback:]_block_invoke_2
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.390
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.390.cold.1
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.391
+ ___65-[MRUserSettings nowPlayingAppStackFailedCanBeNowPlayingInterval]_block_invoke
+ ___65-[MRUserSettings nowPlayingAppStackFailedCanBeNowPlayingInterval]_block_invoke.cold.1
+ ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.28
+ ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsChangedCallback:]_block_invoke
+ ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsChangedCallback:]_block_invoke_2
+ ___66-[MRAVRoutingDiscoverySessionWrapper addEndpointsRemovedCallback:]_block_invoke
+ ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.58
+ ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.63
+ ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.66
+ ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.558
+ ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.551
+ ___67-[MRAVRoutingDiscoverySessionWrapper addEndpointsModifiedCallback:]_block_invoke
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.397.cold.1
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.399
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.402
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.402.cold.1
+ ___68-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesAddedCallback:]_block_invoke_2
+ ___68-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesAddedCallback:]_block_invoke_3
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.384.cold.1
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.386
+ ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.416
+ ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.420
+ ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.583
+ ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesChangedCallback:]_block_invoke_2
+ ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesChangedCallback:]_block_invoke_3
+ ___70-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesRemovedCallback:]_block_invoke_2
+ ___71-[MRAVRoutingDiscoverySessionWrapper addOutputDevicesModifiedCallback:]_block_invoke_2
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.568
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.569
+ ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.460
+ ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.488
+ ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.478
+ ___83+[MRAVEndpoint(Intent_Volume) volumeForOutputDeviceUID:timeout:details:completion:]_block_invoke
+ ___83+[MRAVEndpoint(Intent_Volume) volumeForOutputDeviceUID:timeout:details:completion:]_block_invoke.104
+ ___83+[MRAVEndpoint(Intent_Volume) volumeForOutputDeviceUID:timeout:details:completion:]_block_invoke.cold.1
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke.117
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_2.121
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_3.122
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_4.135
+ ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_5.137
+ ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.579
+ ___89+[MRAVEndpoint(Intent_Grouping) pauseOutputDeviceUIDs:behavior:details:queue:completion:]_block_invoke
+ ___89+[MRAVEndpoint(Intent_Grouping) pauseOutputDeviceUIDs:behavior:details:queue:completion:]_block_invoke.82
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.40
+ ___95+[MRAVEndpoint(Intent_Volume) changeVolume:action:outputDeviceUIDs:timeout:details:completion:]_block_invoke
+ ___95+[MRAVEndpoint(Intent_Volume) changeVolume:action:outputDeviceUIDs:timeout:details:completion:]_block_invoke.113
+ ___95+[MRAVEndpoint(Intent_Volume) changeVolume:action:outputDeviceUIDs:timeout:details:completion:]_block_invoke.cold.1
+ ___95+[MRAVEndpoint(Intent_Volume) volumeCapabilitiesForOutputDeviceUID:timeout:details:completion:]_block_invoke
+ ___95+[MRAVEndpoint(Intent_Volume) volumeCapabilitiesForOutputDeviceUID:timeout:details:completion:]_block_invoke.98
+ ___95+[MRAVEndpoint(Intent_Volume) volumeCapabilitiesForOutputDeviceUID:timeout:details:completion:]_block_invoke.cold.1
+ ___95-[MRAVReconnaissanceSession beginSearchWithTimeout:endpointsAndMissingOutputDevicesCompletion:]_block_invoke
+ ___95-[MRAVReconnaissanceSession beginSearchWithTimeout:endpointsAndMissingOutputDevicesCompletion:]_block_invoke_2
+ ___95-[MRAVReconnaissanceSession beginSearchWithTimeout:endpointsAndMissingOutputDevicesCompletion:]_block_invoke_3
+ ___MRAVEndpointResolveOutputDeviceUIDs_block_invoke
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.336
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.340
+ ____MRAVEndpointGetIntentServiceReplyDispatchQueue_block_invoke
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.106
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.106.cold.1
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.107
+ ____MRHandlePlaybackQueueRequest_block_invoke.98
+ ____MRSetNowPlayingInfo_block_invoke.44
+ ____MRSetNowPlayingInfo_block_invoke_2.48
+ ___block_descriptor_32_e35_"NSString"16?0"MRAppEntityPath"8l
+ ___block_descriptor_32_e51_"MRAppEntityPath"16?0"_MRAppEntityPathProtobuf"8l
+ ___block_descriptor_32_e51_"_MRAppEntityPathProtobuf"16?0"MRAppEntityPath"8l
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e63_v40?0"NSDictionary"8"NSArray"16"MRAVEndpoint"24"NSError"32ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0I8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0f8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.133
+ ___block_literal_global.138
+ ___block_literal_global.185
+ ___block_literal_global.196
+ ___block_literal_global.199
+ ___block_literal_global.224
+ ___block_literal_global.232
+ ___block_literal_global.237
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.260
+ ___block_literal_global.262
+ ___block_literal_global.302
+ ___block_literal_global.319
+ ___block_literal_global.324
+ ___block_literal_global.336
+ ___block_literal_global.349
+ ___block_literal_global.490
+ ___block_literal_global.492
+ ___block_literal_global.518
+ ___block_literal_global.612
+ ___block_literal_global.62
+ ___block_literal_global.68
+ __dispatch_source_type_data_or
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_merge_data
+ _dispatch_source_set_event_handler
+ _kMRMediaRemoteOptionUserActionTimestamp
+ _nowPlayingAppStackFailedCanBeNowPlayingInterval.__interval
+ _nowPlayingAppStackFailedCanBeNowPlayingInterval.__once
+ _objc_msgSend$_onQueue_stopActivityTracking
+ _objc_msgSend$_shouldNotify
+ _objc_msgSend$addEntityPaths:
+ _objc_msgSend$alternativeLocalDeviceUIDPlaceholder
+ _objc_msgSend$callAgent
+ _objc_msgSend$calloutQueue
+ _objc_msgSend$carPlayBannersEnabled
+ _objc_msgSend$clearEntityPaths
+ _objc_msgSend$entityPaths
+ _objc_msgSend$entityPathsAtIndex:
+ _objc_msgSend$entityPathsCount
+ _objc_msgSend$handleAgentMessage:
+ _objc_msgSend$handleGetNumberOfActiveCallsMessage:
+ _objc_msgSend$hasRegisteredAgents
+ _objc_msgSend$initWithActivityName:maxAllowedTime:windowDuration:repeats:handler:
+ _objc_msgSend$initWithBundleIdentifier:typeIdentifier:instanceIdentifier:
+ _objc_msgSend$instanceIdentifier
+ _objc_msgSend$localDeviceUIDPlaceholder
+ _objc_msgSend$numberOfActiveCalls
+ _objc_msgSend$outputDevicesUIDsString
+ _objc_msgSend$pauseOutputDeviceUIDs:behavior:details:queue:completion:
+ _objc_msgSend$registerCallAgent:queue:
+ _objc_msgSend$repeats
+ _objc_msgSend$setCallAgent:
+ _objc_msgSend$setEntityPaths:
+ _objc_msgSend$setHasRegisteredAgents:
+ _objc_msgSend$setTypeIdentifier:
+ _objc_msgSend$typeIdentifier
+ _objc_release_x2
- +[MRAVEndpoint addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
- +[MRAVEndpoint moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]
- +[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]
- +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]
- +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.1
- +[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:].cold.2
- +[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]
- +[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]
- -[MRExternalOutputContextDataSource initializeVolumeCapabilitiesForLegacyCleints]
- -[MRExternalOutputContextDataSource initializeVolumeCapabilitiesForLegacyCleints].cold.1
- -[MROutputContextController _inititalizeVolume]
- -[MROutputContextController setLocalVolume:].cold.3
- -[MROutputContextController setLocalVolumeMuted:].cold.3
- -[MRRollingWindowActivityTracker initWithActivityName:maxAllowedTime:windowDuration:handler:]
- GCC_except_table303
- GCC_except_table334
- _MRMediaRemoteAgentNotifyCallChanged
- _MRMediaRemoteAgentSetEndpoint
- _MRMediaRemoteServiceAgentNotifyCallChanged
- _MRMediaRemoteServiceSetAgentEndpoint
- _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._reloadRateLimiter
- _OBJC_IVAR_$_MRMediaRemoteService.agentEndpoint
- __MRDeviceClassFromMGDeviceClass
- __OBJC_$_CLASS_METHODS_MRAVEndpoint
- __OBJC_$_INSTANCE_METHODS_MRAVEndpoint(Deprecated)
- ___103+[MRAVEndpoint addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
- ___104+[MRAVEndpoint moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:]_block_invoke
- ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke
- ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.626
- ___105+[MRAVEndpoint prepareGroupForPlaybackWithOutputDeviceUIDs:forBundleID:timeout:details:queue:completion:]_block_invoke.cold.1
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.656
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.658
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.663
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.670
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.659
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.597
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke.cold.1
- ___106+[MRAVEndpoint sendCommand:withOptions:toEachEndpointContainingOutputDeviceUIDs:timeout:queue:completion:]_block_invoke_2
- ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke
- ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.608
- ___122+[MRAVEndpoint sendCommand:withOptions:toNewEndpointContainingOutputDeviceUIDs:nowPlayingClient:timeout:queue:completion:]_block_invoke.cold.1
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.639
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.646
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.306
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.308
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.310
- ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.473
- ___54-[MRAVConcreteRoutingDiscoverySession _scheduleReload]_block_invoke
- ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.412
- ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.49
- ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.52
- ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.415
- ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.505
- ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.514
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.401
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.401.cold.1
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.402
- ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.413
- ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.419
- ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke
- ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.588
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.388
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.388.cold.1
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.389
- ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.26
- ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.60
- ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.65
- ___66-[MRNowPlayingPlayerClient setSupportedCommands:queue:completion:]_block_invoke.68
- ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.561
- ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.554
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.395
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.395.cold.1
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.400
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.400.cold.1
- ___68-[MRAVEndpoint modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke.cold.1
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.382
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.382.cold.1
- ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.414
- ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.418
- ___70+[MRAVEndpoint findMyGroupLeaderWithTimeout:details:queue:completion:]_block_invoke.612
- ___70-[MRAVOutputContext _scheduleOutputContextDeviceDidChangeNotification]_block_invoke
- ___71-[MRAVOutputContext _scheduleOutputContextDevicesDidChangeNotification]_block_invoke
- ___74-[MRAVOutputContextModification modifyWithOutputContext:queue:completion:]_block_invoke.cold.1
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.571
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:completion:]_block_invoke.572
- ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.466
- ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.491
- ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.481
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke.119
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_2.123
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_3.124
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_4.137
- ___83-[MRNowPlayingPlayerClient _handePlaybackSessionMigrateRequest:request:completion:]_block_invoke_5.139
- ___84+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:details:queue:groupUIDCompletion:]_block_invoke.582
- ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.44
- ___MRGroupSessionJoinSessionWithToken_block_invoke.334
- ___MRGroupSessionJoinSessionWithToken_block_invoke.338
- ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.108
- ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.108.cold.1
- ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.109
- ____MRHandlePlaybackQueueRequest_block_invoke.100
- ____MRServiceHandleAgentMessage_block_invoke
- ____MRSetNowPlayingInfo_block_invoke.46
- ____MRSetNowPlayingInfo_block_invoke_2.50
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_84_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.154
- ___block_literal_global.173
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.230
- ___block_literal_global.233
- ___block_literal_global.242
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.264
- ___block_literal_global.276
- ___block_literal_global.312
- ___block_literal_global.35
- ___block_literal_global.46
- ___block_literal_global.493
- ___block_literal_global.495
- ___block_literal_global.521
- ___block_literal_global.601
- ___block_literal_global.610
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithActivityName:maxAllowedTime:windowDuration:handler:
- _objc_msgSend$sharedSystemAudioLocalEndpoint
- _objc_msgSend$update
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "@\"<MRCallAgent>\""
+ "@\"MRAppEntityPath\"16@?0@\"_MRAppEntityPathProtobuf\"8"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSString\"16@?0@\"MRAppEntityPath\"8"
+ "@\"_MRAppEntityPathProtobuf\"16@?0@\"MRAppEntityPath\"8"
+ "@52@0:8@16d24d32B40@?44"
+ "Agent"
+ "Decrease"
+ "Endpoint.ModifyTopology"
+ "Increase"
+ "Intent_Grouping"
+ "Intent_Playback"
+ "Intent_Volume"
+ "MRAVEndpoint+Intent.m"
+ "MRAVEndpoint.changeVolume"
+ "MRAVEndpoint.pauseOutputDeviceUIDs"
+ "MRAVEndpoint.volumeCapabilitiesForOutputDeviceUID"
+ "MRAVEndpoint.volumeForOutputDeviceUID"
+ "MRAppEntityPath"
+ "MRCallAgentDelegate"
+ "ModifyOutputContext.xpcInterface"
+ "PauseOrRemoveFromGroup"
+ "T@\"<MRCallAgent>\",W,N,V_callAgent"
+ "T@\"NSArray\",C,N,V_entityPaths"
+ "T@\"NSMutableArray\",&,N,V_entityPaths"
+ "T@\"NSString\",&,N,V_typeIdentifier"
+ "T@\"NSString\",C,N,V_instanceIdentifier"
+ "T@\"NSString\",C,N,V_typeIdentifier"
+ "T@\"_MRAppEntityPathProtobuf\",R,N"
+ "TB,N,V_hasRegisteredAgents"
+ "TB,R,N,V_repeats"
+ "Td,N,V_userActionTimestamp"
+ "UIDs=(%@), behavior=%@"
+ "Z"
+ "[ExternalRoutingDiscoverySession] %@ - Discovery mode changed to: %@"
+ "[MRActivityTracker] Threshold Reached: %@ with context %@"
+ "_MRAppEntityPathProtobuf"
+ "_callAgent"
+ "_entityPaths"
+ "_hasRegisteredAgents"
+ "_initializationGroup"
+ "_onQueue_stopActivityTracking"
+ "_reloadCoalescingSource"
+ "_repeats"
+ "_shouldNotify"
+ "_typeIdentifier"
+ "_userActionTimestamp"
+ "activeCallIdentifierDidChange:"
+ "addEntityPaths:"
+ "alternativeLocalDeviceUIDPlaceholder"
+ "beginSearchWithTimeout:endpointsAndMissingOutputDevicesCompletion:"
+ "behavior"
+ "bid"
+ "callAgent"
+ "changeVolume:action:outputDeviceUIDs:timeout:details:completion:"
+ "clearEntityPaths"
+ "com.apple.MediaRemote.MRAVEndpoint+Intent.reply.serialQueue"
+ "entityPaths"
+ "entityPathsAtIndex:"
+ "entityPathsCount"
+ "entityPathsType"
+ "handleAgentMessage:"
+ "handleGetNumberOfActiveCallsMessage:"
+ "hasRegisteredAgents"
+ "hasTypeIdentifier"
+ "hasUserActionTimestamp"
+ "iid"
+ "initWithActivityName:maxAllowedTime:windowDuration:repeats:handler:"
+ "initWithBundleIdentifier:typeIdentifier:instanceIdentifier:"
+ "initializeVolumeCapabilitiesForLegacyClients"
+ "kMRMediaRemoteOptionUserActionTimestamp"
+ "localDeviceUIDPlaceholder"
+ "nowPlayingAppStackFailedCanBeNowPlayingInterval"
+ "now_playing_agent"
+ "numberOfActiveCalls"
+ "outputDevicesUIDsString"
+ "pauseOutputDeviceUIDs:behavior:details:queue:completion:"
+ "registerCallAgent:queue:"
+ "repeats"
+ "setCallAgent:"
+ "setEntityPaths:"
+ "setHasRegisteredAgents:"
+ "setHasUserActionTimestamp:"
+ "setTypeIdentifier:"
+ "setUserActionTimestamp:"
+ "supportNowPlayingDrivenAgent"
+ "tid"
+ "type=%@, outputDeviceUIDs=%@"
+ "typeIdentifier"
+ "userActionTimestamp"
+ "v56@0:8@16Q24@32@40@?48"
+ "v60@0:8f16Q20@28d36@44@?52"
+ "volume=%lf, action=%@, outputDeviceUIDs=%@"
+ "volumeAction"
+ "volumeCapabilitiesForOutputDeviceUID:timeout:details:completion:"
+ "volumeForOutputDeviceUID:timeout:details:completion:"
+ "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"referencePosition\"b1\"sleepTimerTime\"b1\"trackID\"b1\"userActionTimestamp\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"enhanceDialogueActive\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
+ "【 %@ ❯ %@ ❯ %@ 】"
+ "\xf1"
- "@\"MRRateLimiter\""
- "@48@0:8@16d24d32@?40"
- "Endpoint.volumeControlCapabilitiesForOutputDeviceUID"
- "[MRActivityTracker] Treshold Reached: %@ with context %@"
- "_reloadRateLimiter"
- "agentEndpoint"
- "concreteDiscoverySession.rateLimiter"
- "initWithActivityName:maxAllowedTime:windowDuration:handler:"
- "initializeVolumeCapabilitiesForLegacyCleints"
- "j"
- "motion_on_lock_screen"
- "pauseOutputDeviceUIDs"
- "r^{?=^v^?}"
- "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"referencePosition\"b1\"sleepTimerTime\"b1\"trackID\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"enhanceDialogueActive\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"

```
