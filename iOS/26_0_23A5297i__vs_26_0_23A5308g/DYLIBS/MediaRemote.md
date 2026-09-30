## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.100.108.0.0
-  __TEXT.__text: 0x2ebbb4
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x2a990
+4025.100.115.1.0
+  __TEXT.__text: 0x2eda28
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0x2abc0
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2b68d
-  __TEXT.__oslogstring: 0xd869
-  __TEXT.__gcc_except_tab: 0x6330
+  __TEXT.__cstring: 0x2b7e6
+  __TEXT.__oslogstring: 0xd871
+  __TEXT.__gcc_except_tab: 0x63ac
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xb040
-  __TEXT.__objc_classname: 0x4cd3
-  __TEXT.__objc_methname: 0x4c59c
-  __TEXT.__objc_methtype: 0x8ed3
-  __TEXT.__objc_stubs: 0x27b40
-  __DATA_CONST.__got: 0x1430
+  __TEXT.__unwind_info: 0xb0f0
+  __TEXT.__objc_classname: 0x4d07
+  __TEXT.__objc_methname: 0x4cae2
+  __TEXT.__objc_methtype: 0x8f16
+  __TEXT.__objc_stubs: 0x27ee0
+  __DATA_CONST.__got: 0x1438
   __DATA_CONST.__const: 0xae40
-  __DATA_CONST.__objc_classlist: 0x1178
+  __DATA_CONST.__objc_classlist: 0x1180
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xecd8
+  __DATA_CONST.__objc_selrefs: 0xede0
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xfb0
+  __DATA_CONST.__objc_superrefs: 0xfb8
   __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__auth_got: 0xb78
+  __AUTH_CONST.__auth_got: 0xb80
   __AUTH_CONST.__const: 0x3020
-  __AUTH_CONST.__cfstring: 0x22e20
-  __AUTH_CONST.__objc_const: 0x44fd8
+  __AUTH_CONST.__cfstring: 0x22fc0
+  __AUTH_CONST.__objc_const: 0x45448
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8020
+  __AUTH.__objc_data: 0x8200
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x3198
-  __DATA.__data: 0x1c20
-  __DATA.__bss: 0x890
+  __DATA.__objc_ivar: 0x31d8
+  __DATA.__data: 0x1c80
+  __DATA.__bss: 0x850
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2e90
+  __DATA_DIRTY.__objc_data: 0x2d00
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__bss: 0x4e0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F0A30DD-6A02-39F1-A318-C68493FF1AC6
-  Functions: 19964
-  Symbols:   54793
-  CStrings:  24139
+  UUID: 6E03B864-37D2-3E17-AB0D-C3BCCB5E2365
+  Functions: 20020
+  Symbols:   54972
+  CStrings:  24229
 
Symbols:
+ -[MRAVConcreteOutputDevice representsUGLSender]
+ -[MRAVDistantOutputDevice representsUGLSender]
+ -[MRAVOutputDevice representsUGLSender]
+ -[MRDeviceInfo isPersonalDevice]
+ -[MRPlaybackSessionMigrateRequest _onlock_findEventWithID:]
+ -[MRRollingWindowActivityTracker .cxx_destruct]
+ -[MRRollingWindowActivityTracker _onQueue_scheduleThresholdTimer]
+ -[MRRollingWindowActivityTracker _onQueue_thresholdReached]
+ -[MRRollingWindowActivityTracker _onQueue_timeRemainingUntilThreshold]
+ -[MRRollingWindowActivityTracker _onQueue_timeSpentInWindow]
+ -[MRRollingWindowActivityTracker activityName]
+ -[MRRollingWindowActivityTracker dealloc]
+ -[MRRollingWindowActivityTracker debugDescription]
+ -[MRRollingWindowActivityTracker description]
+ -[MRRollingWindowActivityTracker enabledPeriods]
+ -[MRRollingWindowActivityTracker enabledSince]
+ -[MRRollingWindowActivityTracker handler]
+ -[MRRollingWindowActivityTracker initWithActivityName:maxAllowedTime:windowDuration:handler:]
+ -[MRRollingWindowActivityTracker isRunning]
+ -[MRRollingWindowActivityTracker maxAllowedTime]
+ -[MRRollingWindowActivityTracker mostRecentContext]
+ -[MRRollingWindowActivityTracker queue]
+ -[MRRollingWindowActivityTracker setEnabledPeriods:]
+ -[MRRollingWindowActivityTracker setEnabledSince:]
+ -[MRRollingWindowActivityTracker setHandler:]
+ -[MRRollingWindowActivityTracker setMostRecentContext:]
+ -[MRRollingWindowActivityTracker setQueue:]
+ -[MRRollingWindowActivityTracker setThresholdTimer:]
+ -[MRRollingWindowActivityTracker startActivityTrackingWithContext:]
+ -[MRRollingWindowActivityTracker startActivityTracking]
+ -[MRRollingWindowActivityTracker stopActivityTracking]
+ -[MRRollingWindowActivityTracker thresholdTimer]
+ -[MRRollingWindowActivityTracker timeRemainingUntilThreshold]
+ -[MRRollingWindowActivityTracker timeSpentInWindow]
+ -[MRRollingWindowActivityTracker windowDuration]
+ -[MRUserSettings persistantDiscoveryModeDetectionDuration]
+ -[MRUserSettings persistantDiscoveryModeDetectionWindowDuration]
+ -[MRV2NowPlayingControllerOperationQueue dispatchQueue]
+ -[MRV2NowPlayingControllerOperationQueue initWithDispatchQueue:]
+ -[MRV2NowPlayingControllerOperationQueue isInvalidated]
+ -[_MRAVOutputDeviceDescriptorProtobuf hasRepresentsUGLSender]
+ -[_MRAVOutputDeviceDescriptorProtobuf representsUGLSender]
+ -[_MRAVOutputDeviceDescriptorProtobuf setHasRepresentsUGLSender:]
+ -[_MRAVOutputDeviceDescriptorProtobuf setRepresentsUGLSender:]
+ GCC_except_table119
+ GCC_except_table131
+ OBJC_IVAR_$__MRAVOutputDeviceDescriptorProtobuf._representsUGLSender
+ _OBJC_CLASS_$_MRRollingWindowActivityTracker
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._discoveryTracker
+ _OBJC_IVAR_$_MRAVDistantRoutingDiscoverySession._discoveryTracker
+ _OBJC_IVAR_$_MRAVExternalRoutingDiscoverySession._discoveryTracker
+ _OBJC_IVAR_$_MRAVOutputDevice._representsUGLSender
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._activityName
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._enabledPeriods
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._enabledSince
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._handler
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._maxAllowedTime
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._mostRecentContext
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._queue
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._running
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._thresholdTimer
+ _OBJC_IVAR_$_MRRollingWindowActivityTracker._windowDuration
+ _OBJC_IVAR_$_MRV2NowPlayingControllerOperationQueue._dispatchQueue
+ _OBJC_METACLASS_$_MRRollingWindowActivityTracker
+ __OBJC_$_INSTANCE_METHODS_MRRollingWindowActivityTracker
+ __OBJC_$_INSTANCE_VARIABLES_MRRollingWindowActivityTracker
+ __OBJC_$_PROP_LIST_MRRollingWindowActivityTracker
+ __OBJC_$_PROP_LIST_MRV2NowPlayingControllerOperationQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRActivityTracker
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRActivityTracker
+ __OBJC_$_PROTOCOL_REFS_MRActivityTracker
+ __OBJC_CLASS_PROTOCOLS_$_MRRollingWindowActivityTracker
+ __OBJC_CLASS_RO_$_MRRollingWindowActivityTracker
+ __OBJC_LABEL_PROTOCOL_$_MRActivityTracker
+ __OBJC_METACLASS_RO_$_MRRollingWindowActivityTracker
+ __OBJC_PROTOCOL_$_MRActivityTracker
+ ___43-[MRRollingWindowActivityTracker isRunning]_block_invoke
+ ___51-[MRRollingWindowActivityTracker mostRecentContext]_block_invoke
+ ___51-[MRRollingWindowActivityTracker timeSpentInWindow]_block_invoke
+ ___54-[MRRollingWindowActivityTracker stopActivityTracking]_block_invoke
+ ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.91
+ ___58-[MRUserSettings persistantDiscoveryModeDetectionDuration]_block_invoke
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.93
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.93.cold.1
+ ___60-[MRAVDistantRoutingDiscoverySession initWithConfiguration:]_block_invoke_2
+ ___61-[MRAVConcreteRoutingDiscoverySession initWithConfiguration:]_block_invoke_3
+ ___61-[MRAVExternalRoutingDiscoverySession initWithConfiguration:]_block_invoke_3
+ ___61-[MRRollingWindowActivityTracker timeRemainingUntilThreshold]_block_invoke
+ ___64-[MRUserSettings persistantDiscoveryModeDetectionWindowDuration]_block_invoke
+ ___65-[MRRollingWindowActivityTracker _onQueue_scheduleThresholdTimer]_block_invoke
+ ___67-[MRRollingWindowActivityTracker startActivityTrackingWithContext:]_block_invoke
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.95
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.96
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.97
+ ___78-[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:]_block_invoke_4
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.44
+ ____MRHandlePlaybackQueueRequest_block_invoke.88
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.456
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.457
+ ____onQueue_MRHandlePlaybackQueueRequest_block_invoke_2
+ ___block_descriptor_49_e8_32s40s_e5_B8?0ls32l8s40l8
+ ___block_literal_global.104
+ ___block_literal_global.121
+ ___block_literal_global.251
+ ___block_literal_global.255
+ ___block_literal_global.454
+ ___block_literal_global.46
+ _objc_msgSend$_onQueue_scheduleThresholdTimer
+ _objc_msgSend$_onQueue_thresholdReached
+ _objc_msgSend$_onQueue_timeRemainingUntilThreshold
+ _objc_msgSend$_onQueue_timeSpentInWindow
+ _objc_msgSend$activityName
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$deleteCharactersInRange:
+ _objc_msgSend$enabledPeriods
+ _objc_msgSend$enabledSince
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithActivityName:maxAllowedTime:windowDuration:handler:
+ _objc_msgSend$initWithDispatchQueue:
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$maxAllowedTime
+ _objc_msgSend$mostRecentContext
+ _objc_msgSend$persistantDiscoveryModeDetectionDuration
+ _objc_msgSend$persistantDiscoveryModeDetectionWindowDuration
+ _objc_msgSend$representsUGLSender
+ _objc_msgSend$setEnabledSince:
+ _objc_msgSend$setMostRecentContext:
+ _objc_msgSend$setRepresentsUGLSender:
+ _objc_msgSend$setThresholdTimer:
+ _objc_msgSend$startActivityTracking
+ _objc_msgSend$startActivityTrackingWithContext:
+ _objc_msgSend$stopActivityTracking
+ _objc_msgSend$thresholdTimer
+ _objc_msgSend$timeRemainingUntilThreshold
+ _objc_msgSend$timeSpentInWindow
+ _objc_msgSend$windowDuration
+ _os_unfair_lock_assert_owner
+ _persistantDiscoveryModeDetectionDuration.__interval
+ _persistantDiscoveryModeDetectionDuration.__once
+ _persistantDiscoveryModeDetectionWindowDuration.__interval
+ _persistantDiscoveryModeDetectionWindowDuration.__once
- -[MRPlaybackSessionMigrateRequest findEventWithID:]
- -[MRV2NowPlayingControllerOperationQueue initWithQueue:]
- GCC_except_table112
- GCC_except_table121
- ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.80
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.82
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.82.cold.1
- ___68-[MRV2NowPlayingController _handlePlaybackQueueChangedNotification:]_block_invoke_2
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.84
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.85
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.86
- ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.35
- ____MRHandlePlaybackQueueRequest_block_invoke.89
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.453
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.454
- ____onQueue_MRHandlePlaybackQueueRequest_block_invoke.77
- ____onQueue_MRHandlePlaybackQueueRequest_block_invoke.cold.1
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
- ___block_literal_global.111
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.451
- ___block_literal_global.94
CStrings:
+ "  discoveryTracker=%@\n"
+ " UGL-sender"
+ "%@\n%@ %@"
+ "<%@: %p> (%@)\n  discoveryMode = %@ (%lf seconds ago)\n  routingContext = %@\n  outputDevices = %@\n  endpoints = %@\n  hostedRoutingConnectionDidInitialize = %@\n  discoveryTracker = %@\n  connection = %@ (%lf seconds ago)\n}>"
+ "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@%@%@%@>"
+ "<%@:%p name=%@, tracking=%u, timeSpent=%lf/%lf, remaining=%lf, window=%lf, context=%@>"
+ "@\"<MRActivityTracker>\""
+ "@48@0:8@16d24d32@?40"
+ "Concrete.%@"
+ "Distant.%@"
+ "External.%@"
+ "IsRepresentingUGLSender"
+ "MRActivityTracker"
+ "MRRollingWindowActivityTracker"
+ "MediaServerDeath"
+ "T@\"MSVTimer\",&,N,V_thresholdTimer"
+ "T@\"NSDate\",&,N,V_enabledSince"
+ "T@\"NSMutableArray\",&,N,V_enabledPeriods"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dispatchQueue"
+ "T@\"NSString\",R,N,V_activityName"
+ "T@,&,N,V_mostRecentContext"
+ "TB,N,V_representsUGLSender"
+ "TB,R,N,GisInvalidated"
+ "TB,R,N,GisPersonalDevice"
+ "TB,R,N,GisRunning"
+ "TB,R,N,V_representsUGLSender"
+ "Td,R,N,V_maxAllowedTime"
+ "Td,R,N,V_windowDuration"
+ "[MRAVConcreteOutputDevice] GroupID mismatch on %@:%@: %@ -> %@"
+ "[MRActivityTracker] Start: %@ "
+ "[MRActivityTracker] Stop: %@ "
+ "[MRActivityTracker] Treshold Reached: %@ with context %@"
+ "_activityName"
+ "_discoveryTracker"
+ "_enabledPeriods"
+ "_enabledSince"
+ "_maxAllowedTime"
+ "_mostRecentContext"
+ "_onQueue_scheduleThresholdTimer"
+ "_onQueue_thresholdReached"
+ "_onQueue_timeRemainingUntilThreshold"
+ "_onQueue_timeSpentInWindow"
+ "_representsUGLSender"
+ "_running"
+ "_thresholdTimer"
+ "_windowDuration"
+ "activityName"
+ "dateByAddingTimeInterval:"
+ "deleteCharactersInRange:"
+ "enabledPeriods"
+ "enabledSince"
+ "hasRepresentsUGLSender"
+ "hasSuffix:"
+ "initWithActivityName:maxAllowedTime:windowDuration:handler:"
+ "initWithDispatchQueue:"
+ "isInvalidated"
+ "isPersonalDevice"
+ "maxAllowedTime"
+ "mostRecentContext"
+ "persistantDiscoveryModeDetectionDuration"
+ "persistantDiscoveryModeDetectionWindowDuration"
+ "personalDevice"
+ "representsUGLSender"
+ "running"
+ "setEnabledPeriods:"
+ "setEnabledSince:"
+ "setHasRepresentsUGLSender:"
+ "setMostRecentContext:"
+ "setRepresentsUGLSender:"
+ "setThresholdTimer:"
+ "startActivityTracking"
+ "startActivityTrackingWithContext:"
+ "stopActivityTracking"
+ "thresholdTimer"
+ "timeRemainingUntilThreshold"
+ "timeSpentInWindow"
+ "windowDuration"
+ "{?=\"batteryLevel\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceSubType\"b1\"deviceType\"b1\"distance\"b1\"hostDeviceClass\"b1\"transportType\"b1\"volume\"b1\"volumeCapabilities\"b1\"allowsHeadTrackedSpatialAudio\"b1\"canAccessAppleMusic\"b1\"canAccessRemoteAssets\"b1\"canAccessiCloudMusicLibrary\"b1\"canFetchMediaDataFromSender\"b1\"canPlayEncryptedProgressiveDownloadAssets\"b1\"canRelayCommunicationChannel\"b1\"conversationDetectionEnabled\"b1\"deviceIsPlaying\"b1\"discoveredOnSameInfra\"b1\"engageOnClusterActivate\"b1\"groupContainsGroupLeader\"b1\"isAddedToHomeKit\"b1\"isAirPlayReceiverSessionActive\"b1\"isAppleAccessory\"b1\"isClusterLeader\"b1\"isDeviceGroupable\"b1\"isGroupLeader\"b1\"isGroupable\"b1\"isHeadTrackedSpatialAudioActive\"b1\"isLocalDevice\"b1\"isPickedOnPairedDevice\"b1\"isProxyGroupPlayer\"b1\"isRemoteControllable\"b1\"isVolumeControlAvailable\"b1\"parentGroupContainsDiscoverableLeader\"b1\"pickable\"b1\"presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets\"b1\"producesLowFidelityAudio\"b1\"representsUGLSender\"b1\"requiresAuthorization\"b1\"shouldForceRemoteControlabillity\"b1\"supportsBluetoothSharing\"b1\"supportsBufferedAirPlay\"b1\"supportsConversationDetection\"b1\"supportsExternalScreen\"b1\"supportsHAP\"b1\"supportsHeadTrackedSpatialAudio\"b1\"supportsMultiplayer\"b1\"supportsRapport\"b1\"supportsRapportRemoteControlTransport\"b1\"supportsSharePlayHandoff\"b1\"usingJSONProtocol\"b1\"volumeMuted\"b1\"wasDiscoveredInCache\"b1}"
- "%@\n%@"
- "<%@: %p> (%@)\n  discoveryMode = %@ (%lf seconds ago)\n  routingContext = %@\n  outputDevices = %@\n  endpoints = %@\n  hostedRoutingConnectionDidInitialize = %@\n  connection = %@ (%lf seconds ago)\n}>"
- "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@%@%@>"
- "[MRAVConcreteOutputDevice] GroupID mismatch: %@ -> %@"
- "[MRPlaybackQueueServiceClient] Responding to playbackQueueRequest %{public}@ for path %{public}@ with error %{public}@"
- "{?=\"batteryLevel\"b1\"clusterType\"b1\"configuredClusterSize\"b1\"deviceSubType\"b1\"deviceType\"b1\"distance\"b1\"hostDeviceClass\"b1\"transportType\"b1\"volume\"b1\"volumeCapabilities\"b1\"allowsHeadTrackedSpatialAudio\"b1\"canAccessAppleMusic\"b1\"canAccessRemoteAssets\"b1\"canAccessiCloudMusicLibrary\"b1\"canFetchMediaDataFromSender\"b1\"canPlayEncryptedProgressiveDownloadAssets\"b1\"canRelayCommunicationChannel\"b1\"conversationDetectionEnabled\"b1\"deviceIsPlaying\"b1\"discoveredOnSameInfra\"b1\"engageOnClusterActivate\"b1\"groupContainsGroupLeader\"b1\"isAddedToHomeKit\"b1\"isAirPlayReceiverSessionActive\"b1\"isAppleAccessory\"b1\"isClusterLeader\"b1\"isDeviceGroupable\"b1\"isGroupLeader\"b1\"isGroupable\"b1\"isHeadTrackedSpatialAudioActive\"b1\"isLocalDevice\"b1\"isPickedOnPairedDevice\"b1\"isProxyGroupPlayer\"b1\"isRemoteControllable\"b1\"isVolumeControlAvailable\"b1\"parentGroupContainsDiscoverableLeader\"b1\"pickable\"b1\"presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets\"b1\"producesLowFidelityAudio\"b1\"requiresAuthorization\"b1\"shouldForceRemoteControlabillity\"b1\"supportsBluetoothSharing\"b1\"supportsBufferedAirPlay\"b1\"supportsConversationDetection\"b1\"supportsExternalScreen\"b1\"supportsHAP\"b1\"supportsHeadTrackedSpatialAudio\"b1\"supportsMultiplayer\"b1\"supportsRapport\"b1\"supportsRapportRemoteControlTransport\"b1\"supportsSharePlayHandoff\"b1\"usingJSONProtocol\"b1\"volumeMuted\"b1\"wasDiscoveredInCache\"b1}"

```
