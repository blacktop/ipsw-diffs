## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x222a0
+890.61.4.11.2
+  __TEXT.__text: 0x23e24
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x127c
-  __TEXT.__cstring: 0x7f3f
+  __TEXT.__objc_methlist: 0x13c4
+  __TEXT.__cstring: 0x85ec
   __TEXT.__const: 0x52
   __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__unwind_info: 0xa38
-  __TEXT.__objc_classname: 0x1cd
-  __TEXT.__objc_methname: 0x4888
-  __TEXT.__objc_methtype: 0xe6a
-  __TEXT.__objc_stubs: 0x3240
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x808
+  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__objc_classname: 0x248
+  __TEXT.__objc_methname: 0x4e69
+  __TEXT.__objc_methtype: 0x112c
+  __TEXT.__objc_stubs: 0x3480
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__const: 0x888
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1170
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x390
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x1fa8
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x21a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x258
-  __DATA.__data: 0x3e0
+  __DATA.__objc_ivar: 0x284
+  __DATA.__data: 0x500
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC3D91F3-B414-3648-878A-6FBD7D7B37FE
-  Functions: 860
-  Symbols:   2981
-  CStrings:  1850
+  UUID: AF542C43-6BAD-3153-8FF4-A331A362265C
+  Functions: 894
+  Symbols:   3113
+  CStrings:  1946
 
Symbols:
+ -[APRKMediaPlayer _handleCurrentEventSkippedNotification:]
+ -[APRKMediaPlayer _handleCurrentEventSkippedNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentEventSkippedNotification:].cold.2
+ -[APRKMediaPlayer _handleSeekDidCompleteNotification:].cold.3
+ -[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:]
+ -[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:].cold.1
+ -[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:].cold.2
+ -[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:].cold.3
+ -[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:].cold.4
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.10
+ -[APRKMediaPlayer integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:]
+ -[APRKMediaPlayer integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:].cold.1
+ -[APRKMediaPlayer localParticipantUUIDForPlaybackCoordinator:]
+ -[APRKMediaPlayer localParticipantUUIDForPlaybackCoordinator:].cold.1
+ -[APRKMediaPlayer playbackCoordinator:broadcastLocalParticipantStateDictionary:]
+ -[APRKMediaPlayer playbackCoordinator:broadcastLocalParticipantStateDictionary:].cold.1
+ -[APRKMediaPlayer playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:]
+ -[APRKMediaPlayer playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:].cold.1
+ -[APRKMediaPlayer playbackCoordinator:identifierForPlayerItem:]
+ -[APRKMediaPlayer playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]
+ -[APRKMediaPlayer setCompleteIntegratedTimelineSeekBlock:]
+ -[APRKMediaPlayer setCurrentInterstitialEventID:]
+ -[APRKMediaPlayer setInterstitialEventControllerForInterstitialPlayer:]
+ -[APRKMediaPlayer setPendingIntegratedTimelineSeekID:]
+ -[APRKStreamRenderer isProtectedMirroring]
+ -[APRKStreamRenderer setIsProtectedMirroring:]
+ -[APRKStreamRenderingManager serverPropertyForKey:]
+ -[APRKStreamRenderingManager setForwardFrameUserData:]
+ -[APRKStreamRenderingManager setServerProperty:forKey:]
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table46
+ GCC_except_table58
+ GCC_except_table71
+ GCC_except_table83
+ GCC_except_table91
+ _APRKVideoFrameUserDataAttachment
+ _APSSettingsIsFeatureEnabled
+ _AVPlayerInterstitialEventMonitorCurrentEventSkippedEventKey
+ _AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification
+ _CMTimeCopyDescription
+ _OBJC_CLASS_$_AVPlayerInterstitialEventController
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_APRKMediaPlayer._cachedTimeToPausePlayback
+ _OBJC_IVAR_$_APRKMediaPlayer._completeIntegratedTimelineSeek
+ _OBJC_IVAR_$_APRKMediaPlayer._interstitialEventControllerForInterstitialPlayer
+ _OBJC_IVAR_$_APRKMediaPlayer._interstitialEventControllerForPrimaryPlayer
+ _OBJC_IVAR_$_APRKMediaPlayer._localParticipantID
+ _OBJC_IVAR_$_APRKMediaPlayer._pendingIntegratedTimelineSeekID
+ _OBJC_IVAR_$_APRKMediaPlayer._pendingIntegratedTimelineSeekIDMap
+ _OBJC_IVAR_$_APRKMediaPlayer._playbackCoordinator
+ _OBJC_IVAR_$_APRKStreamRenderer._initializeTransform
+ _OBJC_IVAR_$_APRKStreamRenderer._isProtectedMirroring
+ _OBJC_IVAR_$_APRKStreamRenderingManager._serverProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVPlaybackCoordinationMediumDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVPlayerPlaybackCoordinatorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVPlaybackCoordinationMediumDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVPlayerPlaybackCoordinatorDelegate
+ __OBJC_$_PROTOCOL_REFS_AVPlaybackCoordinationMediumDelegate
+ __OBJC_$_PROTOCOL_REFS_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_$_PROTOCOL_REFS_AVPlayerPlaybackCoordinatorDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVPlaybackCoordinationMediumDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVPlayerPlaybackCoordinatorDelegate
+ __OBJC_PROTOCOL_$_AVPlaybackCoordinationMediumDelegate
+ __OBJC_PROTOCOL_$_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_PROTOCOL_$_AVPlayerPlaybackCoordinatorDelegate
+ ___102-[APRKMediaPlayer playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:]_block_invoke
+ ___42-[APRKStreamRenderer isProtectedMirroring]_block_invoke
+ ___46-[APRKStreamRenderer setIsProtectedMirroring:]_block_invoke
+ ___58-[APRKMediaPlayer _handleCurrentEventSkippedNotification:]_block_invoke
+ ___66-[APRKMediaPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.8
+ ___79-[APRKMediaPlayer initWithP2PWiFiSupport:isInterstitialPlayer:playerSessionID:]_block_invoke
+ ___80-[APRKMediaPlayer playbackCoordinator:broadcastLocalParticipantStateDictionary:]_block_invoke
+ ___82-[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPausePlaybackNotification:]_block_invoke.cold.1
+ ___97-[APRKMediaPlayer integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:]_block_invoke
+ ___block_descriptor_132_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_40_e8_32w_e11_v16?0i8B12lw32l8
+ ___block_descriptor_53_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.107
+ ___block_literal_global.116
+ ___block_literal_global.119
+ ___block_literal_global.12
+ ___block_literal_global.122
+ ___block_literal_global.15
+ ___block_literal_global.77
+ ___block_literal_global.9
+ ___block_literal_global.97
+ _kAPReceiverUIControllerParam_IsProtectedMirroring
+ _kAPReceiverUIControllerParam_ShouldForwardLayer
+ _kCFNull
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackStateKey_Item
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackStateKey_State
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackStateType_LocalParticipant
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackStateType_TransportControl
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackState_Type
+ _kFigEndpointPlaybackSessionEventType_IntendedSeek
+ _kFigEndpointPlaybackSessionEventType_SkipInterstitial
+ _kFigEndpointPlaybackSessionKey_CurrentInterstitialEventSkippableLabel
+ _kFigEndpointPlaybackSessionKey_CurrentInterstitialEventSkippableState
+ _kFigEndpointPlaybackSessionKey_InterstitialEventID
+ _kFigEndpointPlaybackSessionKey_Rate
+ _kFigEndpointPlaybackSessionKey_SeekID
+ _kFigEndpointPlaybackSessionKey_SeekTime
+ _kFigEndpointPlaybackSessionKey_ToleranceAfter
+ _kFigEndpointPlaybackSessionKey_ToleranceBefore
+ _kFigEndpointPlaybackSessionProxiedProperty_MediaCharacteristicsForPreferredCustomMediaSelectionSchemes
+ _kFigPlaybackItemParameter_SeekID
+ _objc_msgSend$_processPlaybackCoordinationMediumWithDictionary:
+ _objc_msgSend$accessLogArray
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$errorLogArray
+ _objc_msgSend$handleNewParticipantStateDictionary:
+ _objc_msgSend$handleNewTransportControlStateDictionary:
+ _objc_msgSend$integratedTimeline
+ _objc_msgSend$interstitialEventControllerWithPrimaryPlayer:
+ _objc_msgSend$noteSeekID:didFinish:
+ _objc_msgSend$playbackCoordinator
+ _objc_msgSend$serverPropertyForKey:
+ _objc_msgSend$setCompleteIntegratedTimelineSeekBlock:
+ _objc_msgSend$setCoordinationMediumDelegate:
+ _objc_msgSend$setCurrentInterstitialEventID:
+ _objc_msgSend$setCurrentRemoteEventSkippableState:withLabel:
+ _objc_msgSend$setInterstitialEventControllerForInterstitialPlayer:
+ _objc_msgSend$setIsProtectedMirroring:
+ _objc_msgSend$setPendingIntegratedTimelineSeekID:
+ _objc_msgSend$setSeekDelegate:
+ _objc_msgSend$setServerProperty:forKey:
- -[APRKStreamRenderingManager _setPTPClockEnabled:].cold.1
- -[APRKStreamRenderingManager setDemoModeEnabled:].cold.1
- -[APRKStreamRenderingManager setForcePermissionDialog:].cold.1
- -[APRKStreamRenderingManager setSupportsSenderUIEvents:].cold.1
- GCC_except_table102
- GCC_except_table117
- GCC_except_table119
- GCC_except_table53
- GCC_except_table68
- GCC_except_table80
- GCC_except_table88
- GCC_except_table99
- _CFObjectGetPropertyInt64Sync
- _CFObjectSetProperty
- ___block_descriptor_80_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_literal_global.103
- ___block_literal_global.11
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.118
- ___block_literal_global.123
- ___block_literal_global.14
- ___block_literal_global.73
- ___block_literal_global.8
- ___block_literal_global.93
- _objc_msgSend$_accessLogArray
- _objc_msgSend$_errorLogArray
CStrings:
+ " time: "
+ " toleranceAfter:\t"
+ " toleranceBefore:\t"
+ "%s - Event which generated this notification is no longer playing, ignoring"
+ "%s - seek delegate called while no item is currently being played, stopping"
+ "-[APRKMediaPlayer _handleCurrentEventSkippedNotification:]"
+ "-[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPausePlaybackNotification:]_block_invoke"
+ "-[APRKMediaPlayer _processPlaybackCoordinationMediumWithDictionary:]"
+ "-[APRKMediaPlayer integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:]"
+ "-[APRKMediaPlayer localParticipantUUIDForPlaybackCoordinator:]"
+ "-[APRKMediaPlayer playbackCoordinator:broadcastLocalParticipantStateDictionary:]"
+ "-[APRKMediaPlayer playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:]"
+ "-[APRKMediaPlayer playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]"
+ "-[APRKStreamRenderer setIsProtectedMirroring:]"
+ "-[APRKStreamRenderingManager setServerProperty:forKey:]"
+ "890.61.4.11.2"
+ "@\"AVPlayerInterstitialEventController\""
+ "@\"AVPlayerPlaybackCoordinator\""
+ "@\"NSArray\"32@0:8@\"AVPlayerPlaybackCoordinator\"16@\"AVPlayerItem\"24"
+ "@\"NSString\"32@0:8@\"AVPlayerPlaybackCoordinator\"16@\"AVPlayerItem\"24"
+ "@\"NSUUID\"24@0:8@\"AVPlaybackCoordinator\"16"
+ "@?"
+ "APRKMediaPlayerObservationContextPlayerRate: oldRate:%.2f, newRate:%.2f, _isInTrickPlay = %d _lastNonZeroRate=%.2f isInterstitalPlayer = %s"
+ "AVPlaybackCoordinationMediumDelegate"
+ "AVPlayerItemIntegratedTimelineSeekDelegate"
+ "AVPlayerPlaybackCoordinatorDelegate"
+ "CoordinatedAirPlayVideo"
+ "FVDFrameUserData"
+ "GetPlaybackInfo for %s item %@, Duration: %f, Position: %f, PlaybackState: %@, isWaitingToSetRateFromSenderAfterSeek: %s"
+ "Handling %@ notification for %s item: %@ player: %@"
+ "Handling %@ notification for event %@: player: %@"
+ "Ignoring skippableState set property - no relevant interstitialEventController"
+ "Incoming PlaybackCoordinationMedium from sender, name: %@, state = %@"
+ "Integrated timeline seek %d delegate on player %@ with data: {%s%@%s%@%s%@ }"
+ "Integrated timeline seekID %d has been confirmed as %s"
+ "Invalid PlaybackCoordinationMedium message."
+ "NULL PlaybackCoordinator"
+ "Payload from handling %@ notification: %@"
+ "PlaybackCoordinationMedium: broadcastLocalParticipantStateDictionary, participantState = %@"
+ "PlaybackCoordinationMedium: broadcastTransportControlStateDictionary, transportControlState = %@"
+ "PlaybackCoordinationMedium: localParticipantUUIDForPlaybackCoordinator, return localParticipantID = %@"
+ "PlaybackCoordinationMedium: reloadTransportControlStateForItemWithIdentifier coordinator = %p, identifier = %@"
+ "Protected mirroring set to %s for renderer %{ptr}."
+ "Q\xf0\xc1"
+ "Sent rate changed notif dict: %@"
+ "Server property %@ is set to %@"
+ "Setting %s player skippableState: %d skippableLabel: %@"
+ "^v24@0:8^{__CFString=}16"
+ "_cachedTimeToPausePlayback"
+ "_completeIntegratedTimelineSeek"
+ "_handleCurrentEventSkippedNotification:"
+ "_initializeTransform"
+ "_interstitialEventControllerForInterstitialPlayer"
+ "_interstitialEventControllerForPrimaryPlayer"
+ "_isProtectedMirroring"
+ "_localParticipantID"
+ "_pendingIntegratedTimelineSeekID"
+ "_pendingIntegratedTimelineSeekIDMap"
+ "_playbackCoordinator"
+ "_processPlaybackCoordinationMediumWithDictionary:"
+ "_serverProperties"
+ "accessLogArray"
+ "autoupdatingCurrentLocale"
+ "cancelled"
+ "completed"
+ "errorLogArray"
+ "forwardFrameUserData"
+ "handleNewParticipantStateDictionary:"
+ "handleNewTransportControlStateDictionary:"
+ "integratedTimeline"
+ "integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:"
+ "integratedTimeline:willSeekToTime:currentTime:"
+ "interstitial"
+ "interstitialEventControllerWithPrimaryPlayer:"
+ "isProtectedMirroring"
+ "localParticipantUUIDForPlaybackCoordinator:"
+ "name is nil, doing nothing."
+ "noteSeekID:didFinish:"
+ "playbackCoordinationMedium"
+ "playbackCoordinator"
+ "playbackCoordinator:broadcastLocalParticipantStateDictionary:"
+ "playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:"
+ "playbackCoordinator:identifierForPlayerItem:"
+ "playbackCoordinator:interstitialTimeRangesForPlayerItem:"
+ "playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:"
+ "primary"
+ "rateChanged"
+ "serverPropertyForKey:"
+ "setCompleteIntegratedTimelineSeekBlock:"
+ "setCoordinationMediumDelegate:"
+ "setCurrentInterstitialEventID:"
+ "setCurrentRemoteEventSkippableState:withLabel:"
+ "setForwardFrameUserData:"
+ "setInterstitialEventControllerForInterstitialPlayer:"
+ "setIsProtectedMirroring:"
+ "setPendingIntegratedTimelineSeekID:"
+ "setSeekDelegate:"
+ "setServerProperty:forKey:"
+ "state is nil, doing nothing."
+ "systemLanguageCode"
+ "v100@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
+ "v100@0:8@16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
+ "v16@?0i8B12"
+ "v32@0:8@\"AVPlaybackCoordinator\"16@\"NSDictionary\"24"
+ "v32@0:8^v16^{__CFString=}24"
+ "v40@0:8@\"AVPlaybackCoordinator\"16@\"NSDictionary\"24@\"NSString\"32"
+ "v40@0:8@\"AVPlaybackCoordinator\"16@\"NSString\"24@?<v@?>32"
+ "v40@0:8@16@24@?32"
+ "v72@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24{?=qiIq}48"
+ "v72@0:8@16{?=qiIq}24{?=qiIq}48"
+ "\xf0a"
- "-[APRKStreamRenderingManager _setPTPClockEnabled:]"
- "-[APRKStreamRenderingManager demoModeEnabled]"
- "-[APRKStreamRenderingManager setDemoModeEnabled:]"
- "-[APRKStreamRenderingManager setForcePermissionDialog:]"
- "-[APRKStreamRenderingManager setSupportsSenderUIEvents:]"
- "-[APRKStreamRenderingManager supportsSenderUIEvents]"
- "860.7.1"
- "APRKMediaPlayerObservationContextPlayerRate: oldRate:%.2f, newRate:%.2f, _isInTrickPlay = %d _lastNonZeroRate=%.2f"
- "Demo mode is %s."
- "Error in getting AirPlay Screen Demo Mode preference value: %i"
- "Error in getting AirPlay supports sender UI events preference value: %i"
- "Force permission got %s."
- "GetPlaybackInfo for item %@, Duration: %f, Position: %f, PlaybackState: %@, isWaitingToSetRateFromSenderAfterSeek: %s"
- "PTP clock got %s."
- "Receiver supports sender UI events: %s."
- "Setting force permissions to %s."
- "_accessLogArray"
- "_errorLogArray"
- "shouldForwardLayer"
- "\xf0Q"

```
