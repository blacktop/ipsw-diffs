## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x24d98
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x13c4
-  __TEXT.__cstring: 0x878f
-  __TEXT.__const: 0x52
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__objc_classname: 0x248
-  __TEXT.__objc_methname: 0x4fac
-  __TEXT.__objc_methtype: 0x112c
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x7d8
-  __DATA_CONST.__const: 0x890
+980.58.1.11.1
+  __TEXT.__text: 0x267f0
+  __TEXT.__objc_methlist: 0x1464
+  __TEXT.__cstring: 0x8d67
+  __TEXT.__const: 0x82
+  __TEXT.__oslogstring: 0x424
+  __TEXT.__gcc_except_tab: 0x528
+  __TEXT.__unwind_info: 0xb18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12b0
+  __DATA_CONST.__objc_selrefs: 0x1350
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x878
   __AUTH_CONST.__const: 0x390
-  __AUTH_CONST.__cfstring: 0x1820
-  __AUTH_CONST.__objc_const: 0x21a8
+  __AUTH_CONST.__cfstring: 0x18e0
+  __AUTH_CONST.__objc_const: 0x2298
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0x500
+  __DATA.__objc_ivar: 0x298
+  __DATA.__data: 0x560
   __DATA.__bss: 0x4c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EDD5BD3-A80B-3AD6-A4BB-D5D096D4893E
-  Functions: 922
-  Symbols:   3204
-  CStrings:  1967
+  UUID: 34720DA7-F6BC-306C-9CA2-0623754EC4B4
+  Functions: 956
+  Symbols:   3372
+  CStrings:  1055
 
Symbols:
+ -[APRKMediaPlayer _attemptToSetCachedSelectedMediaArrayForItem:]
+ -[APRKMediaPlayer _attemptToSetCachedSelectedMediaArrayForItem:].cold.1
+ -[APRKMediaPlayer _attemptToSetCachedSelectedMediaArrayForItem:].cold.2
+ -[APRKMediaPlayer _handleCurrentPlayerItemNewErrorLogEntryNotification:]
+ -[APRKMediaPlayer _handleCurrentPlayerItemNewErrorLogEntryNotification:].cold.1
+ -[APRKMediaPlayer _handleCurrentPlayerItemReachedTimeToPauseBufferingNotification:].cold.3
+ -[APRKMediaPlayer _refreshCachedAccessLogForPlayerItem:]
+ -[APRKMediaPlayer _refreshCachedErrorLogForPlayerItem:]
+ -[APRKMediaPlayer _setPropertyWithDictionary:].cold.11
+ -[APRKMediaPlayer _subscribeForMetricEvents:forItem:]
+ -[APRKMediaPlayer publisher:didReceiveEvent:]
+ -[APRKMediaPlayer publisher:didReceiveEvent:].cold.1
+ -[APRKMediaPlayer publisher:didReceiveEvent:].cold.2
+ -[APRKMediaPlayer publisher:didReceiveEvent:].cold.3
+ -[APRKMediaPlayer serializeMetricEvent:]
+ -[APRKMediaPlayer serializeMetricEvent:].cold.1
+ -[APRKMediaPlayer serializeMetricEvent:].cold.2
+ -[APRKPlayerItem cachedAccessLogArray]
+ -[APRKPlayerItem cachedErrorLogArray]
+ -[APRKPlayerItem cachedSelectedMediaArray]
+ -[APRKPlayerItem sentReachedTimeToPauseBuffering]
+ -[APRKPlayerItem setCachedAccessLogArray:]
+ -[APRKPlayerItem setCachedErrorLogArray:]
+ -[APRKPlayerItem setCachedSelectedMediaArray:]
+ -[APRKPlayerItem setSentReachedTimeToPauseBuffering:]
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.11
+ -[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:].cold.12
+ -[APRKStreamRenderingManager dealloc]
+ -[APRKStreamRenderingManager setDisableAPM2:]
+ GCC_except_table0
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table11
+ GCC_except_table119
+ GCC_except_table139
+ GCC_except_table19
+ GCC_except_table47
+ GCC_except_table60
+ GCC_except_table73
+ GCC_except_table85
+ GCC_except_table94
+ _APGetSignpostsLogHandle
+ _AVPlayerItemNewErrorLogEntryNotification
+ _CFArrayCreate
+ _CFDataCreate
+ _CFDateCreate
+ _CFDictionaryCreate
+ _CFStringCreateWithCString
+ _CFUUIDCreateFromUUIDBytes
+ _CFUUIDCreateString
+ _CMTimeRangeMakeFromDictionary
+ _FigCFDictionarySetBoolean
+ _FigCFDictionarySetInt64
+ _FigCFDictionarySetValue
+ _FigSimpleMutexCreate
+ _FigSimpleMutexDestroy
+ _FigSimpleMutexLock
+ _FigSimpleMutexUnlock
+ _NSStringFromClass
+ _OBJC_CLASS_$_AVMetricEventStream
+ _OBJC_IVAR_$_APRKMediaPlayer._eventStream
+ _OBJC_IVAR_$_APRKPlayerItem._cachedAccessLogArray
+ _OBJC_IVAR_$_APRKPlayerItem._cachedErrorLogArray
+ _OBJC_IVAR_$_APRKPlayerItem._cachedSelectedMediaArray
+ _OBJC_IVAR_$_APRKPlayerItem._sentReachedTimeToPauseBuffering
+ _OBJC_IVAR_$_APRKStreamRenderingManager._disableAPM2
+ _OBJC_IVAR_$_APRKStreamRenderingManager._serverPropertiesMutex
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ __HandleUIControllerNotifications
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVMetricEventStreamSubscriber
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVMetricEventStreamSubscriber
+ __OBJC_LABEL_PROTOCOL_$_AVMetricEventStreamSubscriber
+ __OBJC_PROTOCOL_$_AVMetricEventStreamSubscriber
+ ___29-[APRKPlayerItem naturalSize]_block_invoke
+ ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke.193
+ ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke.195
+ ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke.195.cold.1
+ ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_2.194
+ ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_2.196
+ ___45-[APRKPlayerItem enabledStateForTrackWithID:]_block_invoke.cold.1
+ ___49-[APRKPlayerItem setEnabledState:forTrackWithID:]_block_invoke
+ ___49-[APRKPlayerItem setEnabledState:forTrackWithID:]_block_invoke.cold.1
+ ___55-[APRKMediaPlayer _refreshCachedErrorLogForPlayerItem:]_block_invoke
+ ___55-[APRKMediaPlayer _refreshCachedErrorLogForPlayerItem:]_block_invoke_2
+ ___56-[APRKMediaPlayer _refreshCachedAccessLogForPlayerItem:]_block_invoke
+ ___56-[APRKMediaPlayer _refreshCachedAccessLogForPlayerItem:]_block_invoke_2
+ ___73-[APRKMediaPlayer _handleCurrentPlayerItemNewAccessLogEntryNotification:]_block_invoke_2
+ ____HandleUIControllerNotifications_block_invoke
+ ____HandleUIControllerNotifications_block_invoke_2
+ ___block_descriptor_48_e8_32r_e36_B24?0Q8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_48_e8_32s40s_e30_v16?0"AVPlayerItemErrorLog"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e31_v16?0"AVPlayerItemAccessLog"8ls32l8s40l8
+ ___block_descriptor_53_e8_32s40s_e34_v24?0"AVAssetTrack"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_60_e8_32s40s48r_e34_v24?0"AVAssetTrack"8"NSError"16lr48l8s32l8s40l8
+ ___block_literal_global.129
+ ___helper_copyCFObjectFromXPCObject_block_invoke
+ ___helper_copyCFObjectFromXPCObject_block_invoke_2
+ __os_signpost_emit_with_name_impl
+ __xpc_type_array
+ __xpc_type_bool
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_dictionary
+ __xpc_type_double
+ __xpc_type_int64
+ __xpc_type_null
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _free
+ _helper_copyCFObjectFromXPCObject
+ _helper_copyCFObjectFromXPCObject.cold.1
+ _kCFAbsoluteTimeIntervalSince1970
+ _kFigEndpointPlaybackSessionEventType_MetricEvent
+ _kFigEndpointPlaybackSessionKey_MetricEventsToSubscribe
+ _kFigEndpointPlaybackSessionKey_SnapBehavior
+ _kFigEndpointPlaybackSessionMetricEvent_ClassName
+ _kFigEndpointPlaybackSessionProxiedProperty_InterstitialEventItemTimeOffset
+ _kFigEndpointPlaybackSessionProxiedProperty_MetricEventsToSubscribe
+ _malloc_type_calloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_attemptToSetCachedSelectedMediaArrayForItem:
+ _objc_msgSend$_refreshCachedAccessLogForPlayerItem:
+ _objc_msgSend$_refreshCachedErrorLogForPlayerItem:
+ _objc_msgSend$_setAssociatedWithAirPlaySession:
+ _objc_msgSend$_subscribeForMetricEvents:forItem:
+ _objc_msgSend$addPublisher:
+ _objc_msgSend$cachedAccessLogArray
+ _objc_msgSend$cachedErrorLogArray
+ _objc_msgSend$cachedSelectedMediaArray
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$eventStream
+ _objc_msgSend$fetchAccessLogWithCompletionHandler:
+ _objc_msgSend$fetchErrorLogWithCompletionHandler:
+ _objc_msgSend$loadTracksWithMediaType:completionHandler:
+ _objc_msgSend$loggingIdentifier
+ _objc_msgSend$seekToTime:toleranceBefore:toleranceAfter:seekID:options:
+ _objc_msgSend$sentReachedTimeToPauseBuffering
+ _objc_msgSend$serializeMetricEvent:
+ _objc_msgSend$serializedEvent
+ _objc_msgSend$setCachedAccessLogArray:
+ _objc_msgSend$setCachedErrorLogArray:
+ _objc_msgSend$setCachedSelectedMediaArray:
+ _objc_msgSend$setInterstitialEventItemTimeOffset:
+ _objc_msgSend$setSentReachedTimeToPauseBuffering:
+ _objc_msgSend$setSubscriber:queue:
+ _objc_msgSend$subscribeToAllMetricEvents
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _xpc_array_apply
+ _xpc_array_get_count
+ _xpc_bool_get_value
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ _xpc_date_get_value
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_count
+ _xpc_double_get_value
+ _xpc_get_type
+ _xpc_int64_get_value
+ _xpc_string_get_string_ptr
+ _xpc_type_get_name
+ _xpc_uint64_get_value
+ _xpc_uuid_get_bytes
- -[APRKMediaPlayer _attemptToSetSelectedMediaArray:]
- -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.1
- -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.2
- -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.3
- -[APRKMediaPlayer _attemptToSetSelectedMediaArray:].cold.4
- -[APRKPlayerItem playbackAccessLog]
- -[APRKPlayerItem playbackErrorLog]
- -[APRKStreamRenderer setDeferLayerRendering:]
- -[APRKStreamRenderingManager _setPTPClockEnabled:]
- GCC_except_table103
- GCC_except_table106
- GCC_except_table123
- GCC_except_table46
- GCC_except_table59
- GCC_except_table71
- GCC_except_table8
- GCC_except_table83
- GCC_except_table92
- _OBJC_IVAR_$_APRKMediaPlayer._cachedSelectedMediaArray
- _OBJC_IVAR_$_APRKStreamRenderer._deferLayerRendering
- __HandleClearScreen
- ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_4
- ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_5
- ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_6
- ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_6.cold.1
- ___39-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_7
- ___45-[APRKStreamRenderer setDeferLayerRendering:]_block_invoke
- ___66-[APRKStreamRenderer processStartScreenPresentationWithSessionID:]_block_invoke_2.cold.1
- ____HandleClearScreen_block_invoke
- ____HandleClearScreen_block_invoke_2
- ___block_descriptor_48_e8_32s40r_e34_v24?0"AVAssetTrack"8"NSError"16lr40l8s32l8
- ___block_literal_global.125
- _objc_msgSend$_attemptToSetSelectedMediaArray:
- _objc_msgSend$accessLog
- _objc_msgSend$errorLog
- _objc_msgSend$playbackAccessLog
- _objc_msgSend$playbackErrorLog
- _objc_msgSend$trackWithTrackID:
- _objc_msgSend$tracksWithMediaType:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "%s - cannot convert serializes event %@ to data"
+ "%s - cannot get xpc_dict from event %@"
+ "%s - cannot serialize event %@"
+ "%s - cfDict is NULL or not a dictionary"
+ "%s - got AVMetricEvent %@ from publisher %@ : "
+ "%s - publisher has wrong type %@"
+ "%s - unsupported type: %s"
+ "-[APRKMediaPlayer _attemptToSetCachedSelectedMediaArrayForItem:]"
+ "-[APRKMediaPlayer _handleCurrentPlayerItemNewErrorLogEntryNotification:]"
+ "-[APRKMediaPlayer _seekWithDictionary:]_block_invoke"
+ "-[APRKMediaPlayer publisher:didReceiveEvent:]"
+ "-[APRKMediaPlayer serializeMetricEvent:]"
+ "-[APRKPlayerItem enabledStateForTrackWithID:]_block_invoke"
+ "-[APRKPlayerItem naturalSize]"
+ "-[APRKPlayerItem naturalSize]_block_invoke"
+ "-[APRKPlayerItem setEnabledState:forTrackWithID:]"
+ "-[APRKPlayerItem setEnabledState:forTrackWithID:]_block_invoke"
+ "980.58.1.11.1"
+ "???"
+ "AP_TYPE_CONVERSION_A3592112-48A5-46C2-B215-A7C8058E99ED"
+ "AirPlayVideoCreatePlayer"
+ "AirPlayVideoItemSeekBegin"
+ "AirPlayVideoItemSeekEnd"
+ "AirPlayVideoPlayerContentKeyRequest"
+ "AirPlayVideoPlayerContentKeyResponse"
+ "AirPlayVideoPlayerCurrentItemChange"
+ "AirPlayVideoPlayerInsertItem"
+ "AirPlayVideoPlayerRateChange"
+ "AirPlayVideoPlayerRemoveItem"
+ "AirPlayVideoPlayerStateChange"
+ "AirPlayVideoPlayerUnhandledURLRequest"
+ "AirPlayVideoPlayerUnhandledURLResponse"
+ "Attempted to set selectedMediaArray but item %@ was not ready to play, postponing."
+ "Attempted to set selectedMediaArray for item %@ but array is nil. Bailing out."
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Boolean uiController_isAllowedToProceed(UIControllerRef, CFStringRef, CFStringRef)"
+ "CFTypeRef helper_copyCFObjectFromXPCObject(__strong xpc_object_t)"
+ "Created interstitial player"
+ "Created player"
+ "Disabling PTP clock on iOS receiver."
+ "Failed to load track %d for item %@: %@"
+ "Failed to load video tracks for item %@: %@"
+ "Handling content key response. ID %@"
+ "Handling custom URL response. ID %d"
+ "Handling insertPlayQueueItem. player %@ UUID %@"
+ "Handling removePlayQueueItem. player %@ UUID %@"
+ "Handling seekToDate. item %@ date %@"
+ "Handling seekToTime. item %@ seekID %d time %f seekOptions %lu"
+ "Handling setRate. player %@ rate %f"
+ "Inserting play queue item. UUID %@"
+ "InterstitialEventItemTimeOffset set to %@"
+ "Item = %@. SelectedMediaArray property set to %@."
+ "Item = %@: Selecting MediaPresentationLanguage %@"
+ "Item = %@: Selecting MediaPresentationSetting %@"
+ "Item = %@: Setting option = %@ for group = %@"
+ "Item already posted reachedTimeToPauseBufferingNotification. Ignoring"
+ "Loading tracks with media type timed out for item %@"
+ "OSStatus uiController_showPIN(UIControllerRef, CFStringRef, uint64_t, CFStringRef)"
+ "PTP clock enabled on iOS receiver via defaults write override."
+ "Player status stopped"
+ "Q\xf0\xb1"
+ "Received currentItemChanged. previousItem %@ currentItem %@ reason %@"
+ "Received playbackStateChanged. player %@ status %li"
+ "Received seekDidComplete. item %@ seekID %d time %f"
+ "Removing play queue item. UUID %@"
+ "Sending content key request. ID %@"
+ "Sending custom URL request. ID %d"
+ "disableAPM2"
+ "enableReceiverPTPClock"
+ "null"
+ "serializedXPC"
+ "uint64"
+ "v16@?0@\"AVPlayerItemAccessLog\"8"
+ "v16@?0@\"AVPlayerItemErrorLog\"8"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "void _HandleUIControllerNotifications(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "\xf0q"
- "#16@0:8"
- "-[APRKMediaPlayer _attemptToSetSelectedMediaArray:]"
- "-[APRKMediaPlayer _seekWithDictionary:]_block_invoke_6"
- ".cxx_destruct"
- "950.7.1"
- "@\"<APRKContentKeyHelperDelegate>\""
- "@\"<APRKMediaPlayerMessagingDelegate>\""
- "@\"<APRKResourceLoaderHelperDelegate>\""
- "@\"<APRKStreamRendererDelegate>\""
- "@\"<APRKStreamRendererSampleBufferDelegate>\""
- "@\"<APRKStreamRenderingManagerDelegate>\""
- "@\"<AirPlayReceiverUIDelegate>\""
- "@\"<CAAction>\"32@0:8@\"CALayer\"16@\"NSString\"24"
- "@\"<NSObject>\""
- "@\"APRKContentKeyHelper\""
- "@\"APRKMediaPlayer\""
- "@\"APRKMetadata\""
- "@\"APRKResourceLoaderHelper\""
- "@\"APRKStreamRecorder\""
- "@\"AVContentKeySession\""
- "@\"AVPlayerInterstitialEventController\""
- "@\"AVPlayerPlaybackCoordinator\""
- "@\"AVQueuePlayer\""
- "@\"AVSampleBufferAudioRenderer\""
- "@\"AVSampleBufferRenderSynchronizer\""
- "@\"AWDLActivator\""
- "@\"CALayer\""
- "@\"NSArray\""
- "@\"NSArray\"32@0:8@\"AVPlayerPlaybackCoordinator\"16@\"AVPlayerItem\"24"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"AVPlayerPlaybackCoordinator\"16@\"AVPlayerItem\"24"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSUUID\"24@0:8@\"AVPlaybackCoordinator\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@24@0:8r^{sockaddr=CC[14c]}16"
- "@28@0:8@16i24"
- "@28@0:8B16B20i24"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^{OpaqueAPReceiverUIController=}32"
- "@44@0:8@16@24^{OpaqueAPReceiverUIController=}32B40"
- "@48@0:8@16@24@32@40"
- "@?"
- "APRKContentKeyHelper"
- "APRKContentKeyHelperDelegate"
- "APRKMediaPlayer"
- "APRKMediaPlayerMessagingDelegate"
- "APRKMetadata"
- "APRKPlayerItem"
- "APRKReachability"
- "APRKResourceLoaderHelper"
- "APRKResourceLoaderHelperDelegate"
- "APRKStreamRecorder"
- "APRKStreamRenderer"
- "APRKStreamRenderingManager"
- "APRKUtilities"
- "AVAssetResourceLoaderDelegate"
- "AVContentKeySessionDelegate"
- "AVPlaybackCoordinationMediumDelegate"
- "AVPlayerItemIntegratedTimelineSeekDelegate"
- "AVPlayerItemMetadataCollectorPushDelegate"
- "AVPlayerPlaybackCoordinatorDelegate"
- "AWDLActivator"
- "Attempted to set selectedMediaArray but array is nil. Bailing out."
- "Attempted to set selectedMediaArray but item was not ready to play, postponing."
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^{opaqueCMSampleBuffer=}16"
- "B28@0:8@16i24"
- "B28@0:8i16@20"
- "B32@0:8@\"AVAssetResourceLoader\"16@\"AVAssetResourceLoadingRequest\"24"
- "B32@0:8@\"AVAssetResourceLoader\"16@\"AVAssetResourceRenewalRequest\"24"
- "B32@0:8@\"AVAssetResourceLoader\"16@\"NSURLAuthenticationChallenge\"24"
- "B32@0:8@16@24"
- "B32@0:8Q16^@24"
- "B40@0:8@\"AVContentKeySession\"16@\"AVContentKeyRequest\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "Boolean uiController_isAllowedToProceed(UIControllerRef, const char *, CFStringRef)"
- "CALayerDelegate"
- "CMTimeRangeValue"
- "CMTimeValue"
- "HUDLayer"
- "I"
- "I16@0:8"
- "NSObject"
- "OSStatus uiController_showPIN(UIControllerRef, const char *, uint64_t, const char *)"
- "Q16@0:8"
- "Q24@0:8Q16"
- "Q\xf0\xc1"
- "SelectedMediaArray property set to %@."
- "Selecting MediaPresentationLanguage %@"
- "Selecting MediaPresentationSetting %@"
- "Setting option = %@ for group = %@"
- "T#,R"
- "T@\"<APRKContentKeyHelperDelegate>\",W,N,V_delegate"
- "T@\"<APRKMediaPlayerMessagingDelegate>\",W,N"
- "T@\"<APRKResourceLoaderHelperDelegate>\",W,N,V_delegate"
- "T@\"<APRKStreamRendererDelegate>\",W,N,V_delegate"
- "T@\"<APRKStreamRenderingManagerDelegate>\",W,N,V_delegate"
- "T@\"APRKMetadata\",&,N,V_currentItemMetadata"
- "T@\"AVPlayerItem\",R,N"
- "T@\"AVQueuePlayer\",R,N"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_UUIDString"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_album"
- "T@\"NSString\",R,C,N,V_artist"
- "T@\"NSString\",R,C,N,V_artworkDataInBase64"
- "T@\"NSString\",R,C,N,V_artworkMIMEType"
- "T@\"NSString\",R,C,N,V_managedClientName"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"NSUUID\",R,C,N,V_uniqueID"
- "TB,N"
- "TB,N,V_autoRotateLayerFollowingClientRotation"
- "TB,N,V_forwardsFPSSecureStopData"
- "TB,N,V_isAudioOnly"
- "TB,N,V_isMirroringAudioStreamPaused"
- "TB,N,V_supportRemoteControl"
- "TB,R,N"
- "TB,R,N,V_expectsSecureStop"
- "TB,R,N,V_isInterstitialPlayer"
- "TQ,N,V_concurrentPlaybackPolicy"
- "TQ,N,V_maxNumberOfConcurrentSessions"
- "TQ,N,V_preemptionPolicy"
- "TQ,R"
- "TQ,R,N,V_streamRendererMode"
- "TQ,R,N,V_supportedModesMask"
- "Ti,R,N,V_playerSessionID"
- "Tq,N,V_actionAtItemEnd"
- "Tq,R,N,V_totalTrackCount"
- "Tq,R,N,V_trackNumber"
- "T{?=qiIq},N,V_startPosition"
- "T{CGSize=dd},R,N"
- "URL"
- "URLByAppendingPathComponent:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDFromItemDictionary:"
- "UUIDOnlyDictionaryRepresentation"
- "UUIDString"
- "Vv16@0:8"
- "^v24@0:8^{__CFString=}16"
- "^{AirPlayReceiverServerPrivate=}"
- "^{BonjourBrowser=}"
- "^{OpaqueAPReceiverFairPlayHelper=}"
- "^{OpaqueAPSNetworkAddress=}"
- "^{OpaqueAPSNetworkClock=}"
- "^{OpaqueFigAssetWriter=}"
- "^{OpaqueFigCFWeakReferenceHolder=}"
- "^{OpaqueFigVideoQueue=}"
- "^{_NSZone=}16@0:8"
- "^{__CFString=}24@0:8Q16"
- "^{__SCNetworkReachability=}"
- "^{opaqueCMFormatDescription=}"
- "_SSLPropertiesforTLSInfo:"
- "_UUIDString"
- "_actionAtItemEnd"
- "_activeContentKeyRequests"
- "_activeResourceLoadingRequests"
- "_addPendingSeekID:withMessage:forItem:ignoreSeekCompletion:"
- "_addPermittedClient:"
- "_airPlayReceiverUIDelegate"
- "_airPlayVideoVersionSupport"
- "_album"
- "_altAdvertisingEnabled"
- "_appIDData"
- "_artist"
- "_artworkDataInBase64"
- "_artworkMIMEType"
- "_assetWriter"
- "_assistedModeEnabled"
- "_attemptToSetSelectedMediaArray:"
- "_audioRenderer"
- "_audioSessionCount"
- "_audioSessionMode"
- "_audioTrackID"
- "_autoRotateLayerFollowingClientRotation"
- "_awdlActivator"
- "_backingUIControllerWeakRef"
- "_browser"
- "_cachedSSLProperties"
- "_cachedSelectedMediaArray"
- "_cachedSetRateAndAnchor"
- "_cachedTimeToPausePlayback"
- "_canRecord"
- "_cleanupInternalPlayer"
- "_cleanupPreviousRecordingIfExisting"
- "_completeIntegratedTimelineSeek"
- "_concurrentPlaybackPolicy"
- "_contentKeyHelper"
- "_contentKeySession"
- "_contentKeySessionQueue"
- "_contentLocation"
- "_currentInterstitialEventID"
- "_currentItemMetadata"
- "_currentItemUUID"
- "_currentPlaybackInfoDictionary"
- "_currentRecordingURL"
- "_currentTransform"
- "_currentVideoPlaybackVersion"
- "_currentVideoSessionID"
- "_customDisplayHDRModeFromPrefsWithDefault:"
- "_customDisplaySize"
- "_customDisplaySizeFromPrefsWithDefault:"
- "_customDisplaySizeMax"
- "_customDisplaySizeMaxFromPrefsWithDefault:"
- "_debugLayer"
- "_deferLayerRendering"
- "_delegate"
- "_delegateQueue"
- "_demoDeviceInfo"
- "_disableAutoResumeAfterSeek"
- "_displayHDRMode"
- "_enableMixingMediaAudio"
- "_enqueueSampleBufferForRecording:isAudioSBuf:"
- "_enqueueVideoFrameForRendering:"
- "_ensembleInfo"
- "_ensureFairPlayHelper"
- "_ensureFigVideoQueue"
- "_ensureInternalPlayerFor:"
- "_ensureInterstitialPlayerFor:"
- "_expectsSecureStop"
- "_figPlaybackStateStringFrom:"
- "_figVideoQueue"
- "_figVideoQueueNotifObserver"
- "_fixedIPContentLocationFromURLString:error:"
- "_forcePermissionDialog"
- "_formatDesc"
- "_forwardsFPSSecureStopData"
- "_fpHelper"
- "_frontPlayerItem"
- "_getHDRModeString:"
- "_getPropertyWithDictionary:"
- "_handleCurrentEventSkippedNotification:"
- "_handleCurrentItemChangedNotification:"
- "_handleCurrentItemFailedToPlayToEndNotification:"
- "_handleCurrentItemPlaybackStalledNotification:"
- "_handleCurrentItemPlayedToEndNotification:"
- "_handleCurrentPlayerItemMediaSelectionDidChangeNotification:"
- "_handleCurrentPlayerItemNewAccessLogEntryNotification:"
- "_handleCurrentPlayerItemReachedTimeToPauseBufferingNotification:"
- "_handleCurrentPlayerItemReachedTimeToPausePlaybackNotification:"
- "_handleSeekDidCompleteNotification:"
- "_handleTimeJumpedNotification:"
- "_headersDictionary"
- "_initPermittedClients"
- "_initializeTransform"
- "_insertPlayQueueItemWithDictionary:"
- "_internalPlaybackState"
- "_interstitialEventControllerForInterstitialPlayer"
- "_interstitialEventControllerForPrimaryPlayer"
- "_interstitialEvents"
- "_interstitialPlayer"
- "_isAudioActive"
- "_isAudioOnly"
- "_isFirstSetRateReceived"
- "_isInTrickPlay"
- "_isInterestedInDateRange"
- "_isInterstitialPlayer"
- "_isInvalidated"
- "_isMirroringAudioStreamPaused"
- "_isMirroringVideoStreamPaused"
- "_isP2PWiFiSession"
- "_isPermittedClient:"
- "_isProtectedMirroring"
- "_isRotatedTransform:"
- "_isScreenCleared"
- "_isStopping"
- "_isWaitingToSetRateFromSenderAfterSeek"
- "_isWiredLink"
- "_isolationQueue"
- "_lastNonZeroRate"
- "_lastPTS"
- "_lastReportedDateRanges"
- "_lastVideoSampleBufferSize"
- "_localParticipantID"
- "_managedClientName"
- "_maxNumberOfConcurrentSessions"
- "_messageQueue"
- "_messagingDelegate"
- "_mirroringLayer"
- "_mirroringNeedsKeyFrame"
- "_noteCurrentRemoteInterstitialEvent:"
- "_noteRemoteInterstitialEvents:forItem:"
- "_optimizeAudioRenderingLatency"
- "_outOfBandAlternateTracks"
- "_passwordString"
- "_pausePlayerIfNeededForState:"
- "_pendingIntegratedTimelineSeekID"
- "_pendingIntegratedTimelineSeekIDMap"
- "_pendingSenderSeekMessages"
- "_performContentKeyRequest:isRenewalRequest:"
- "_performStartRecordingWithOutputURL:"
- "_performStopRecording"
- "_performUIControllerActionWithBlock:"
- "_permissionEnabled"
- "_permissionGrantPeriod"
- "_permissionGrantTimer"
- "_permissionTimeout"
- "_permittedClients"
- "_permittedClientsQueue"
- "_playbackCoordinator"
- "_player"
- "_playerItemForUUID:"
- "_playerSessionID"
- "_preemptionPolicy"
- "_presentationVideoSize"
- "_previousItemUUID"
- "_primaryMediaCharacteristic"
- "_processAuthorizeItemWithDictionary:"
- "_processMessageWithDictionaryInternal:"
- "_processPlaybackCoordinationMediumWithDictionary:"
- "_processPlaybackInfoRequestWithDictionary:"
- "_processStreamingKeyWithDictionary:"
- "_processUnhandledURLWithDictionary:"
- "_queue"
- "_rateBeforeTrickPlay"
- "_reachabilityRef"
- "_receiverNetworkClock"
- "_receiverSupportsMirroring"
- "_recordSampleBuffer:toTrackWithID:"
- "_recorder"
- "_recorderKeyFrameTimer"
- "_recorderNeedsKeyFrame"
- "_recordingStartTime"
- "_registerForFigVideoQueueNotifications"
- "_registerNotificationHandlersAndInsertPlayerItem:afterItem:"
- "_registerNotificationHandlersForPlayer"
- "_removePendingSeekID:forItem:"
- "_removePlayQueueItemWithDictionary:"
- "_rendererAudioBufferQueue"
- "_rendererForUniqueIDInternal:"
- "_rendererStateUpdateQueue"
- "_rendererVideoBufferQueue"
- "_renderersArray"
- "_requestIDCnt"
- "_resourceLoaderHelper"
- "_resourceLoaderQueue"
- "_sampleBufferDelegate"
- "_sampleBufferRepresentsKeyFrame:"
- "_screenSessionCount"
- "_seekRequestMessageForSeekID:forItem:"
- "_seekWithDictionary:"
- "_sendUpstreamErrorMessageWithError:"
- "_sendUpstreamMessageWithDictionary:"
- "_sendUpstreamPlaybackStateMessageWithPlaybackStateString:stoppedBecauseInterrupted:"
- "_serializeTimeRanges:"
- "_server"
- "_serverProperties"
- "_sessionReceiverAddr"
- "_setInterstitialPlayer:"
- "_setPTPClockEnabled:"
- "_setPropertyWithDictionary:"
- "_setRandomPassword"
- "_setRateWithDictionary:"
- "_shouldFlip:"
- "_shouldForwardLayers"
- "_shouldIgnoreSeekCompletionForSeekID:forItem:"
- "_shouldRecordFrames"
- "_sourceRect"
- "_stallCount"
- "_startDate"
- "_startPosition"
- "_startReceiverServerWithSupportedModesMask:"
- "_startTime"
- "_stopInternal"
- "_stopWithDictionary:"
- "_streamRendererMode"
- "_supportRemoteControl"
- "_supportedModesMask"
- "_synchronizer"
- "_timedMetadataFromAVTimedMetadata:"
- "_timer"
- "_title"
- "_totalTrackCount"
- "_trackNumber"
- "_transform"
- "_uniqueID"
- "_unregisterForFigVideoQueueNotifications"
- "_unregisterNotificationHandlersAndRemovePlayerItem:"
- "_unregisterNotificationHandlersForPlayer"
- "_updateAudioSessionMode:"
- "_updatePlaybackStateWithState:stoppedBecauseInterrupted:shouldSendUpstreamMessage:"
- "_updateStreamingMode"
- "_useCALayerForMirroring"
- "_useUniqueClientName"
- "_usesHomeKitIntegration"
- "_videoSessionCount"
- "_videoTrackID"
- "absoluteString"
- "accessLog"
- "accessLogArray"
- "actionAtItemEnd"
- "actionForLayer:forKey:"
- "activeRenderers"
- "activeRenderersCount"
- "addContentKeyRecipient:"
- "addDateRangeCollectorToItem:"
- "addEntriesFromDictionary:"
- "addMediaDataCollector:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addRenderer:"
- "airPlayVideoVersionSupport"
- "airplayUIGetProperty:qualifier:error:"
- "airplayUIPerform:inputParams:outputParams:"
- "airplayUISetProperty:qualifier:value:"
- "airplayUIStartVideo:outputParams:"
- "airplayUIStopVideo:"
- "airplayUIUpdateAudioMetaData:"
- "airplayUIUpdateAudioProgress:duration:"
- "album"
- "allClientNames"
- "allKeys"
- "allKeysForObject:"
- "allRenderers"
- "altAdvertisingEnabled"
- "array"
- "arrayWithObject:"
- "artist"
- "artworkDataInBase64"
- "artworkMIMEType"
- "asset"
- "assetTrack"
- "assistedInfoForAWDL"
- "assistedInfoForDiscovery"
- "assistedInfoForIPAddress:"
- "assistedInfoForMode:options:"
- "assistedModeEnabled"
- "audioSessionCount"
- "autoRotateLayerFollowingClientRotation"
- "autorelease"
- "autoupdatingCurrentLocale"
- "availableLanguages"
- "backingAVQueuePlayer"
- "backingMediaPlayer"
- "base64EncodedStringWithOptions:"
- "baseDictionaryForResponseToRequestWithDictionary:"
- "baseDictionaryForUpstreamMessageWithType:"
- "begin"
- "boolValue"
- "cStringUsingEncoding:"
- "canRecord"
- "class"
- "commit"
- "concurrentPlaybackPolicy"
- "conformsToProtocol:"
- "connectionRequired"
- "containsObject:"
- "containsString:"
- "contentInformationRequest"
- "contentKeyHelper:didGenerateSecureStopRecordPayload:"
- "contentKeyHelper:wantsToPerformContentKeyRequestWithDictionary:"
- "contentKeyResponseWithFairPlayStreamingKeyResponseData:renewalDate:"
- "contentKeySession:contentKeyRequest:didFailWithError:"
- "contentKeySession:contentKeyRequestDidSucceed:"
- "contentKeySession:didProvideContentKeyRequest:"
- "contentKeySession:didProvideContentKeyRequests:forInitializationData:"
- "contentKeySession:didProvidePersistableContentKeyRequest:"
- "contentKeySession:didProvideRenewingContentKeyRequest:"
- "contentKeySession:didUpdatePersistableContentKey:forContentKeyIdentifier:"
- "contentKeySession:externalProtectionStatusDidChangeForContentKey:"
- "contentKeySession:shouldRetryContentKeyRequest:reason:"
- "contentKeySessionContentProtectionSessionIdentifierDidChange:"
- "contentKeySessionDidGenerateExpiredSessionReport:"
- "contentKeySessionWithKeySystem:storageDirectoryAtURL:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createStreamRendererWithUniqueID:clientName:UIController:"
- "currentDate"
- "currentEstimatedDate"
- "currentEvent"
- "currentItem"
- "currentMediaSelection"
- "currentReachabilityStatus"
- "currentTime"
- "currentVideoPlaybackVersion"
- "currentVideoSessionID"
- "customMediaSelectionScheme"
- "dataRequest"
- "dataWithBytes:length:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "delegateQueue"
- "demoDeviceInfo"
- "demoModeEnabled"
- "description"
- "dictionary"
- "dictionaryForError:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeStreamRendererModeTo:forRenderer:"
- "didChangeValueForKey:"
- "didStartStreamingWithRenderer:"
- "didStopStreamingWithRenderer:"
- "didUpdateMetadata:forRenderer:"
- "displayLayer:"
- "doubleValue"
- "drawLayer:inContext:"
- "enableMixingMediaAudio"
- "enabledStateForTrackWithID:"
- "enqueueSampleBuffer:"
- "ensembleInfo"
- "ensureUniqueClientName:"
- "enumerateObjectsUsingBlock:"
- "errorLog"
- "errorLogArray"
- "errorWithDomain:code:userInfo:"
- "expectsSecureStop"
- "extendedLanguageTag"
- "extraAttributes"
- "f"
- "f16@0:8"
- "fileExistsAtPath:isDirectory:"
- "finalizeRecording"
- "finishLoading"
- "finishLoadingWithError:"
- "firstObject"
- "floatValue"
- "forcePINRefresh"
- "forgetAllActiveContentKeyRequests"
- "forgetAllActiveResourceLoadingRequests"
- "forwardsFPSSecureStopData"
- "getAdvertisingAccessMode"
- "getAppHasSetAdvertisingAccessModeEntitlement"
- "handleNewParticipantStateDictionary:"
- "handleNewTransportControlStateDictionary:"
- "handleSenderUIEvent:forRenderer:"
- "hasMediaCharacteristic:"
- "hash"
- "host"
- "i16@0:8"
- "i24@0:8@16"
- "i24@0:8Q16"
- "i24@0:8^{opaqueCMSampleBuffer=}16"
- "i28@0:8^{opaqueCMSampleBuffer=}16B24"
- "i28@0:8^{opaqueCMSampleBuffer=}16i24"
- "identifier"
- "init"
- "initWithAsset:"
- "initWithCapacity:"
- "initWithDictionary:"
- "initWithDictionary:resourceLoaderHelper:contentKeyHelper:options:"
- "initWithDomain:code:userInfo:"
- "initWithIdentifiers:classifyingLabels:"
- "initWithP2PWiFiSupport:isInterstitialPlayer:playerSessionID:"
- "initWithSpecifiedName:"
- "initWithURL:options:"
- "initWithURL:statusCode:HTTPVersion:headerFields:"
- "initWithUniqueID:clientName:UIController:useCALayerForMirroring:"
- "insertItem:afterItem:"
- "intValue"
- "integerValue"
- "integratedTimeline"
- "integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:"
- "integratedTimeline:willSeekToTime:currentTime:"
- "interstitialEventControllerWithPrimaryPlayer:"
- "invalidate"
- "isActive"
- "isAirPlayReceiverSupported"
- "isAllowedToProceedForClientWithName:clientID:"
- "isAudioOnly"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isHandlingContentKeyRequestWithURLString:"
- "isInterstitialPlayer"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMirroringAudioStreamPaused"
- "isMirroringVideoStreamPaused"
- "isP2PWiFi"
- "isPaused"
- "isPlaybackBufferEmpty"
- "isPlaybackBufferFull"
- "isPlaybackLikelyToKeepUp"
- "isProtectedMirroring"
- "isProxy"
- "isReadyForMoreMediaData"
- "isRecording"
- "isWiredLink"
- "items"
- "keySpace"
- "layer"
- "layerWillDraw:"
- "layoutSublayers"
- "layoutSublayersOfLayer:"
- "length"
- "listeningForAlternateBonjourBrowsing"
- "loadTrackWithTrackID:completionHandler:"
- "loadValuesAsynchronouslyForKeys:completionHandler:"
- "localParticipantUUIDForPlaybackCoordinator:"
- "localeIdentifier"
- "longValue"
- "makeNowPlayingRenderer"
- "makeSeekID"
- "makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:"
- "managedClientName"
- "maxNumberOfConcurrentSessions"
- "mediaCharacteristic"
- "mediaCharacteristicsOfPreferredCustomMediaSelectionSchemes"
- "mediaDataCollectors"
- "mediaPlayer"
- "mediaPlayer:didGenerateFPSSecureStopRecordPayload:"
- "mediaPlayer:wantsToPostNotification:withPayload:"
- "mediaPlayer:wantsToSendUpstreamMessageWithDictionary:"
- "mediaPlayerNeedsTLSInfo:"
- "mediaSelectionGroupForMediaCharacteristic:"
- "mediaSelectionGroupForPropertyList:mediaSelectionOption:"
- "messagingDelegate"
- "metadataCollector:didCollectDateRangeMetadataGroups:indexesOfNewGroups:indexesOfModifiedGroups:"
- "mirroringLayer"
- "mirroringVolume"
- "mutableCopy"
- "naturalSize"
- "networkStatusForFlags:"
- "noteSeekID:didFinish:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "object"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "optimizeAudioRenderingLatency"
- "outOfBandAlternateTracks"
- "path"
- "pause"
- "pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permissionTimeout"
- "playbackCoordinator"
- "playbackCoordinator:broadcastLocalParticipantStateDictionary:"
- "playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:"
- "playbackCoordinator:identifierForPlayerItem:"
- "playbackCoordinator:interstitialTimeRangesForPlayerItem:"
- "playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:"
- "player"
- "playerSessionID"
- "port"
- "postNotificationName:object:"
- "postVideoV1EventWithType:params:"
- "preemptionPolicy"
- "processAudioSampleBuffer:"
- "processContentKeyResponse:"
- "processHideGlobalPasscodePromptRequest"
- "processHidePasscodePromptRequest"
- "processMessageWithIDAndDictionaryAsync:messageSessionID:"
- "processMessageWithIDAndDictionarySync:messageSessionID:"
- "processSenderUIEvent:"
- "processShowGlobalPasscodePromptRequest:withClientName:"
- "processShowPasscodePromptRequest:"
- "processStartAudioSessionRequestWithSessionID:isScreenAudio:"
- "processStartScreenPresentationWithSessionID:"
- "processStartVideoPlaybackRequestWithWithSessionID:version:"
- "processStopAudioSessionRequestWithSessionID:"
- "processStopScreenPresentationWithSessionID:"
- "processStopVideoPlaybackRequestWithSessionID:"
- "processStreamingKeyRequestWithDictionary:withCompletionBlock:"
- "processTLSInfoDictionary:"
- "processUnhandledURLResponseWithDictionary:error:"
- "processVideoSampleBuffer:"
- "propertyList"
- "propertyListWithData:options:format:error:"
- "q"
- "q16@0:8"
- "q20@0:8I16"
- "reachabilityForInternetConnection"
- "reachabilityWithAddress:"
- "reachabilityWithHostName:"
- "recordAudioSampleBuffer:"
- "recordVideoSampleBuffer:"
- "recordingSessionDidFailForRenderer:"
- "registerAVURLAsset:"
- "release"
- "removeAllObjects"
- "removeContentKeyRecipient:"
- "removeItem:"
- "removeItemAtPath:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "removeObserver:forKeyPath:context:"
- "removeObserver:name:object:"
- "removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:"
- "removeRenderer:atTime:completionHandler:"
- "removeRendererWithUniqueID:"
- "renderer:didOutputAudioSampleBuffer:"
- "renderer:didOutputVideoSampleBuffer:"
- "rendererForUniqueID:"
- "requestWithURL:"
- "resourceLoader"
- "resourceLoader:didCancelAuthenticationChallenge:"
- "resourceLoader:didCancelLoadingRequest:"
- "resourceLoader:shouldWaitForLoadingOfRequestedResource:"
- "resourceLoader:shouldWaitForRenewalOfRequestedResource:"
- "resourceLoader:shouldWaitForResponseToAuthenticationChallenge:"
- "resourceLoaderHelper:wantsToPerformUnhandledURLRequestWithDictionary:forRequestID:"
- "respondWithData:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "s16@0:8"
- "sampleBufferDelegate"
- "scheme"
- "screenSessionCount"
- "secureStopURL"
- "seekToDate:completionHandler:"
- "seekToTime:toleranceBefore:toleranceAfter:seekID:"
- "selectMediaOption:inMediaSelectionGroup:"
- "selectMediaPresentationLanguage:forMediaSelectionGroup:"
- "selectMediaPresentationSetting:forMediaSelectionGroup:"
- "selectedMediaArray"
- "selectedMediaArrayForItem:"
- "selectedMediaOptionInMediaSelectionGroup:"
- "selectors"
- "self"
- "serializableRepresentation"
- "serverPropertyForKey:"
- "setActionAtItemEnd:"
- "setAdvertisingAccessMode:withError:"
- "setAllowedCommonMediaClientDataKeys:"
- "setAllowsExternalPlayback:"
- "setAltAdvertisingEnabled:"
- "setAssistedModeEnabled:"
- "setAutoRotateLayerFollowingClientRotation:"
- "setAutomaticallyHandlesInterstitialEvents:"
- "setBounds:"
- "setCanRecord:"
- "setCompleteIntegratedTimelineSeekBlock:"
- "setConcurrentPlaybackPolicy:"
- "setContentType:"
- "setCoordinationMediumDelegate:"
- "setCurrentInterstitialEventID:"
- "setCurrentItemMetadata:"
- "setCurrentRemoteEventSkippableState:withLabel:"
- "setCustomDisplaySizeMax:"
- "setDefaultRate:"
- "setDeferLayerRendering:"
- "setDelegate:"
- "setDelegate:queue:"
- "setDelegateQueue:"
- "setDemoDeviceInfo:"
- "setDemoModeEnabled:"
- "setDisableActions:"
- "setDisplayHDRMode:"
- "setEnableMixingMediaAudio:"
- "setEnabled:"
- "setEnabledState:forTrackWithID:"
- "setEnsembleInfo:"
- "setForcePermissionDialog:"
- "setForwardFrameUserData:"
- "setForwardPlaybackEndTime:"
- "setForwardsFPSSecureStopData:"
- "setInitialDate:"
- "setInterstitialEventControllerForInterstitialPlayer:"
- "setIsAudioOnly:"
- "setIsMirroringAudioStreamPaused:"
- "setIsMirroringVideoStreamPaused:"
- "setIsP2PWiFi:"
- "setIsPaused:"
- "setIsProtectedMirroring:"
- "setIsWiredLink:"
- "setListeningForAlternateBonjourBrowsing:"
- "setLoggingIdentifier:"
- "setMaxNumberOfConcurrentSessions:"
- "setMessagingDelegate:"
- "setMirroringVolume:"
- "setMuted:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptimizeAudioRenderingLatency:"
- "setPendingIntegratedTimelineSeekID:"
- "setPermissionTimeout:"
- "setPosition:"
- "setPreemptionPolicy:"
- "setPreferCoordinatedPlaybackBehavior:"
- "setRate:"
- "setRate:time:"
- "setRate:time:atHostTime:options:"
- "setReceiverNetworkClock:"
- "setRedirect:"
- "setRenewalDate:"
- "setResponse:"
- "setRestrictions:"
- "setReversePlaybackEndTime:"
- "setSampleBufferDelegate:"
- "setServerProperty:forKey:"
- "setSessionReceiverAddress:"
- "setShouldForwardLayers:"
- "setSnapTimeToPausePlayback:"
- "setStartDate:"
- "setStartPosition:"
- "setSublayerTransform:"
- "setSupportRemoteControl:"
- "setSupportsSenderUIEvents:"
- "setTextStyleRules:"
- "setTextStyleRulesUsingArray:"
- "setTimeToPauseBuffering:"
- "setTimeToPausePlayback:"
- "setUUIDString:"
- "setUseCALayerForMirroring:"
- "setUsesHomeKitIntegration:"
- "setValue:forKey:"
- "setVideoV1Delegate:withDelegateQueue:"
- "setVolume:"
- "settings"
- "sharedInstance"
- "shouldAskPermissionWithRequestID:forClientWithName:withCompletionBlock:"
- "shouldCancelPermissionRequestWithRequestID:"
- "shouldDelegateToInterstitialPlayerForMessageAndID:sessionID:"
- "shouldForwardLayers"
- "shouldHideGlobalPasscode"
- "shouldHidePasscodePromptForRenderer:"
- "shouldShowGlobalPasscodeWithString:withClientName:"
- "shouldShowPasscodePromptWithString:forRenderer:"
- "startDate"
- "startNotifier"
- "startPosition"
- "startReceiverServer"
- "startReceiverServerWithSupportedRenderingModes:"
- "startRecordingAtURL:"
- "startRecordingWithOutputURL:"
- "startWithMaxDuration:"
- "statusOfValueForKey:error:"
- "stopNotifier"
- "stopReceiverServer"
- "stopRecording"
- "stopWithCompletionBlock:"
- "streamRendererMode"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportRemoteControl"
- "supportedModesMask"
- "systemSupportsWiFiUDM"
- "temporaryDirectory"
- "textStyleRuleWithTextMarkupAttributes:"
- "timeIntervalSinceReferenceDate"
- "title"
- "totalTrackCount"
- "trackNumber"
- "trackWithTrackID:"
- "tracks"
- "tracksWithMediaType:"
- "uniqueID"
- "unregisterAVURLAsset:"
- "updateDisplayInfo"
- "updateMedatataWithDictionary:"
- "useCALayerForMirroring"
- "usePTPClock"
- "userInfo"
- "usesHomeKitIntegration"
- "v100@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
- "v100@0:8@16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"APRKMediaPlayer\"16"
- "v24@0:8@\"AVContentKeySession\"16"
- "v24@0:8@\"CALayer\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16i20"
- "v24@0:8I16B20"
- "v24@0:8Q16"
- "v24@0:8^{OpaqueAPSNetworkAddress=}16"
- "v24@0:8^{OpaqueAPSNetworkClock=}16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8I16Q20"
- "v28@0:8i16@20"
- "v32@0:8@\"APRKContentKeyHelper\"16@\"NSDictionary\"24"
- "v32@0:8@\"APRKMediaPlayer\"16@\"NSDictionary\"24"
- "v32@0:8@\"AVAssetResourceLoader\"16@\"AVAssetResourceLoadingRequest\"24"
- "v32@0:8@\"AVAssetResourceLoader\"16@\"NSURLAuthenticationChallenge\"24"
- "v32@0:8@\"AVContentKeySession\"16@\"AVContentKey\"24"
- "v32@0:8@\"AVContentKeySession\"16@\"AVContentKeyRequest\"24"
- "v32@0:8@\"AVContentKeySession\"16@\"AVPersistableContentKeyRequest\"24"
- "v32@0:8@\"AVPlaybackCoordinator\"16@\"NSDictionary\"24"
- "v32@0:8@\"CALayer\"16^{CGContext=}24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^@24"
- "v32@0:8@16^{CGContext=}24"
- "v32@0:8^v16^{__CFString=}24"
- "v32@0:8q16B24B28"
- "v32@0:8r*16^{__CFDictionary=}24"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8@\"APRKMediaPlayer\"16@\"NSString\"24@32"
- "v40@0:8@\"APRKResourceLoaderHelper\"16@\"NSDictionary\"24@\"NSNumber\"32"
- "v40@0:8@\"AVContentKeySession\"16@\"AVContentKeyRequest\"24@\"NSError\"32"
- "v40@0:8@\"AVContentKeySession\"16@\"NSArray\"24@\"NSData\"32"
- "v40@0:8@\"AVContentKeySession\"16@\"NSData\"24@32"
- "v40@0:8@\"AVPlaybackCoordinator\"16@\"NSDictionary\"24@\"NSString\"32"
- "v40@0:8@\"AVPlaybackCoordinator\"16@\"NSString\"24@?<v@?>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8i16@20@28B36"
- "v40@0:8{?=qiIq}16"
- "v48@0:8@\"AVPlayerItemMetadataCollector\"16@\"NSArray\"24@\"NSIndexSet\"32@\"NSIndexSet\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32^v40"
- "v72@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24{?=qiIq}48"
- "v72@0:8@16{?=qiIq}24{?=qiIq}48"
- "valueForKey:"
- "valueWithCMTime:"
- "videoFrameSize"
- "videoLayerOrientationDidChangeTo:forRenderer:"
- "videoLayerSizeDidChangeTo:forRenderer:"
- "videoQueuePerformanceDictionary"
- "videoSessionCount"
- "videoStreamIsCleared:forRenderer:"
- "void _HandleClearScreen(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
- "volume"
- "willChangeValueForKey:"
- "zone"
- "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
- "{?=\"width\"i\"height\"i}"
- "{?=qiIq}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "\xf0a"

```
