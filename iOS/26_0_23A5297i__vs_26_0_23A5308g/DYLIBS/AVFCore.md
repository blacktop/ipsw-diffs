## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2360.73.1.11.1
-  __TEXT.__text: 0x2083c4
-  __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_methlist: 0x1aed4
-  __TEXT.__cstring: 0x31576
-  __TEXT.__const: 0x1ed0
-  __TEXT.__gcc_except_tab: 0x7a24
-  __TEXT.__oslogstring: 0x1bec8
+2360.77.2.0.0
+  __TEXT.__text: 0x1b00d0
+  __TEXT.__auth_stubs: 0x3bf0
+  __TEXT.__objc_methlist: 0x1aeec
+  __TEXT.__cstring: 0x23b46
+  __TEXT.__const: 0x1dd0
+  __TEXT.__gcc_except_tab: 0x6954
+  __TEXT.__oslogstring: 0x3c3a
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x415
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x9698
-  __TEXT.__objc_classname: 0x5e8c
-  __TEXT.__objc_methname: 0x35f73
-  __TEXT.__objc_methtype: 0x9cf7
-  __TEXT.__objc_stubs: 0x20900
-  __DATA_CONST.__got: 0x45a0
+  __TEXT.__unwind_info: 0x94c0
+  __TEXT.__objc_classname: 0x5e8b
+  __TEXT.__objc_methname: 0x35ff1
+  __TEXT.__objc_methtype: 0x9d77
+  __TEXT.__objc_stubs: 0x208c0
+  __DATA_CONST.__got: 0x4638
   __DATA_CONST.__const: 0x55a0
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab88
+  __DATA_CONST.__objc_selrefs: 0xab70
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xcd8
   __DATA_CONST.__objc_arraydata: 0x298
-  __AUTH_CONST.__auth_got: 0x1e50
-  __AUTH_CONST.__const: 0x1138
-  __AUTH_CONST.__cfstring: 0x192a0
-  __AUTH_CONST.__objc_const: 0x30550
+  __AUTH_CONST.__auth_got: 0x1e08
+  __AUTH_CONST.__const: 0x1118
+  __AUTH_CONST.__cfstring: 0x18de0
+  __AUTH_CONST.__objc_const: 0x30570
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7970
-  __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x2554
-  __DATA.__data: 0x1830
+  __AUTH.__data: 0x1f8
+  __DATA.__objc_ivar: 0x2558
+  __DATA.__data: 0x1800
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x440
-  __DATA.__bss: 0x1400
+  __DATA.__common: 0x180
+  __DATA.__bss: 0x13f0
   __DATA_DIRTY.__objc_data: 0x3660
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0x270
   __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__common: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C9D0A792-8EB8-3FFF-9A1D-1F80E9C4F9E9
-  Functions: 11447
-  Symbols:   39065
-  CStrings:  18828
+  UUID: A74980A1-D779-3CF7-9510-2ACCD26591B5
+  Functions: 11353
+  Symbols:   38797
+  CStrings:  16704
 
Symbols:
+ -[AVAsynchronousVideoCompositionRequest _validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:reportingObject:reportingSelector:]
+ -[AVPlayerInterstitialEventController _resetPlaybackCoordinatorTimelineExpectations]
+ -[AVPlayerInterstitialEventMonitor _setCachedCurrentEvent:]
+ -[AVPlayerInterstitialEventMonitor _updateCachedCurrentEvent]
+ -[AVPlayerItem _applyCurrentAudioTapProcessorOnFigPlaybackItem]
+ -[AVPlayerItem _setItemAudioTapProcessor:fromAudioMixContext:]
+ -[AVPlayerItemIntegratedTimeline _shouldIssueCachedSeek:]
+ -[AVPlayerPlaybackCoordinator _ensureIntegratedTimelineIsEstablished]
+ -[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectationsForIdentifier:]
+ -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _canOverlapPlaybackFromPlayerItem:toPlayerItem:]
+ -[AVSampleBufferAudioRenderer setOutputContext:].cold.1
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.4
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table150
+ GCC_except_table158
+ GCC_except_table189
+ GCC_except_table804
+ _FigObjectRecordMethodCallsForObject
+ _FigSignalErrorAtGM
+ _OBJC_IVAR_$_AVPlayerInterstitialEventMonitor._cachedCurrentEvent
+ _OBJC_IVAR_$_AVPlayerInterstitialEventMonitor._ivarQueue
+ _OBJC_IVAR_$_AVPlayerItemInternal.audioTapProcessorSetIsPending
+ _OBJC_IVAR_$_AVPlayerItemInternal.audioTapProcessorWasSetFromAudioMix
+ ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke_2
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.174
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.174.cold.1
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.174.cold.2
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_3
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_4
+ ___122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke_2
+ ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke_2
+ ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_3
+ ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_4
+ ___21-[AVPlayerLayer init]_block_invoke_5
+ ___22-[AVPlayer _addLayer:]_block_invoke_2
+ ___22-[AVPlayer _addLayer:]_block_invoke_3
+ ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke_2
+ ___31-[AVPlayerItem _updateTimebase]_block_invoke_5
+ ___31-[AVPlayerItem _updateTimebase]_block_invoke_6
+ ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke_3
+ ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke_3
+ ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke_2
+ ___42-[AVPlayerCaptionLayer _interstitialLayer]_block_invoke_2
+ ___44-[AVPlayerLayer _addObserversForVideoLayer:]_block_invoke_2
+ ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke_2
+ ___46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke_2
+ ___48-[AVPlayerInterstitialEventMonitor currentEvent]_block_invoke
+ ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_3
+ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_3
+ ___59-[AVPlayerInterstitialEventMonitor _setCachedCurrentEvent:]_block_invoke
+ ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.518
+ ___62-[AVPlayerItem _setItemAudioTapProcessor:fromAudioMixContext:]_block_invoke
+ ___62-[AVPlayerItem _setItemAudioTapProcessor:fromAudioMixContext:]_block_invoke_2
+ ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke_2
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke_2
+ ___63-[AVPlayerItem _applyCurrentAudioTapProcessorOnFigPlaybackItem]_block_invoke
+ ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke_2
+ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_3
+ ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_3
+ ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke_4
+ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_3
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.478
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.482
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.490
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.491
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.498
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.499
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.501
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1150
+ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_3
+ ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke_2
+ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_3
+ ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke_2
+ ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke_2
+ ___78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.24
+ ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_3
+ ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke_3
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_5
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_6
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_7
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_5
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_6
+ ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_3
+ ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_4
+ ___90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke_2
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1147
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1242
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_4
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_5
+ ___Block_byref_object_copy_.102
+ ___Block_byref_object_copy_.107
+ ___Block_byref_object_copy_.11
+ ___Block_byref_object_dispose_.103
+ ___Block_byref_object_dispose_.108
+ ___Block_byref_object_dispose_.12
+ ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4
+ ___avplayer_fpNotificationCallback_block_invoke_10
+ ___avplayer_fpNotificationCallback_block_invoke_11
+ ___avplayer_fpNotificationCallback_block_invoke_12
+ ___avplayer_fpNotificationCallback_block_invoke_13
+ ___avplayer_fpNotificationCallback_block_invoke_14
+ ___avplayer_fpNotificationCallback_block_invoke_15
+ ___avplayer_fpNotificationCallback_block_invoke_6
+ ___avplayer_fpNotificationCallback_block_invoke_7
+ ___avplayer_fpNotificationCallback_block_invoke_8
+ ___avplayer_fpNotificationCallback_block_invoke_9
+ ___avplayer_iapdNotificationCallback_block_invoke_3
+ ___avplayer_iapdNotificationCallback_block_invoke_4
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_10
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_11
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_12
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_13
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_14
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_15
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_16
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_17
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_18
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_19
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_20
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_21
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_22
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_23
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_24
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_25
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_26
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_27
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_28
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_29
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_30
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_31
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_7
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_8
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_9
+ ___block_descriptor_48_e8_32o40b_e24_v16?0"NSNotification"8ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e8_v16?08ls40l8s32l8
+ ___block_descriptor_48_e8_32r_e26_v32?0"AVCaption"8Q16^B24lr32l8
+ ___block_descriptor_56_e8_32o40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_57_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_literal_global.105
+ ___block_literal_global.1070
+ ___block_literal_global.1072
+ ___block_literal_global.127
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.1390
+ ___block_literal_global.1426
+ ___block_literal_global.1452
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.228
+ ___block_literal_global.234
+ ___block_literal_global.237
+ ___block_literal_global.304
+ ___block_literal_global.391
+ ___block_literal_global.415
+ ___block_literal_global.428
+ ___block_literal_global.436
+ ___block_literal_global.457
+ ___block_literal_global.536
+ ___block_literal_global.541
+ ___block_literal_global.564
+ ___block_literal_global.587
+ ___block_literal_global.590
+ ___block_literal_global.605
+ ___block_literal_global.74
+ ___block_literal_global.746
+ ___block_literal_global.747
+ ___block_literal_global.756
+ ___block_literal_global.887
+ ___block_literal_global.955
+ ___figEndpointNotificationCallback_block_invoke_2
+ ___figEndpointNotificationCallback_block_invoke_3
+ ___handleFigAssetLoadingNotification_block_invoke.538
+ ___handleFigAssetTrackNotification_block_invoke_2
+ __canOverlapReasonStr
+ _fig_log_get_emitter
+ _kCVImageBufferSidebandVideoPropertiesLookupIDKey
+ _kFigObjMethodCalls_AVSampleBufferDisplayLayer_dealloc
+ _kFigObjMethodCalls_AVSampleBufferDisplayLayer_init
+ _kFigObjMethodCalls_AVSampleBufferDisplayLayer_layerDidBecomeVisible_notVisible
+ _kFigObjMethodCalls_AVSampleBufferDisplayLayer_layerDidBecomeVisible_visible
+ _kFigObjMethodCalls_AVSampleBufferRenderSynchronizer__createOnceTimebaseObserverForRemovalOfRenderer_release
+ _kFigObjMethodCalls_AVSampleBufferRenderSynchronizer__createOnceTimebaseObserverForRemovalOfRenderer_retain
+ _kFigObjMethodCalls_AVSampleBufferRenderSynchronizer_avrendersynchronize_electRenderer
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer__setContentLayerOnFigVideoQueue
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_dealloc
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_flushWithRemovalOfDisplayedImage
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_init
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_removeDisplayLayer
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_setDisplayLayerVisibility_notVisible
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_setDisplayLayerVisibility_visible
+ _kFigObjMethodCalls_AVSampleBufferVideoRenderer_setRenderSynchronizer
+ _kFigPlaybackItemNotification_CoordinationIdentifierChanged
+ _kFigPlaybackItemParameter_CoordinationIdentifier
+ _kVTCGImageCreationKey_PrefersStandardDynamicRange
+ _objc_msgSend$_applyCurrentAudioTapProcessorOnFigPlaybackItem
+ _objc_msgSend$_canOverlapPlaybackFromPlayerItem:toPlayerItem:
+ _objc_msgSend$_coordinationIdentifier
+ _objc_msgSend$_ensureIntegratedTimelineIsEstablished
+ _objc_msgSend$_resetGroupTimelineExpectationsForIdentifier:
+ _objc_msgSend$_resetPlaybackCoordinatorTimelineExpectations
+ _objc_msgSend$_setCachedCurrentEvent:
+ _objc_msgSend$_setItemAudioTapProcessor:fromAudioMixContext:
+ _objc_msgSend$_shouldIssueCachedSeek:
+ _objc_msgSend$_updateCachedCurrentEvent
+ _objc_msgSend$_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:reportingObject:reportingSelector:
+ _objc_msgSend$dynamicRangePolicy
- -[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:].cold.2
- -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler].cold.2
- -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.1
- -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.2
- -[AVAsynchronousVideoCompositionRequest _validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:]
- -[AVPlayerItem _updateAudioTapProcessorOnFigPlaybackItem]
- -[AVPlayerItem audioTapProcessorWasSet]
- -[AVPlayerLayer _compactDescription]
- -[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectations]
- -[AVPlayerPlaybackCoordinator _setIntegratedTimelineCreatingNew:]
- -[AVPlayerPlaybackCoordinator integratedTimeline]
- -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:]
- GCC_except_table153
- GCC_except_table159
- GCC_except_table172
- GCC_except_table179
- GCC_except_table211
- GCC_except_table95
- _AVBacktraceAsString
- _AVBacktraceAsStringWithMaxFrames
- _AVTelemetryGenerateID.cold.1
- _AVTelemetryLogHandle
- _AVTelemetryLogHandle.cold.1
- _AVTelemetryLogHandle.emitter
- _AVTelemetryLogHandle.onceToken
- _CMSampleBufferGetPresentationTimeStamp
- _FigDebugIsInternalBuild
- _FigParticipantStateDictionaryGetStateLoggingIdentifier
- _FigPlaybackRateChangeReasonGetDescription
- _FigSignalErrorAt3
- _NSStringFromRect
- _NSStringFromSize
- _OBJC_IVAR_$_AVPlayerItemInternal.audioTapProcessorWasSet
- _OBJC_IVAR_$_AVPlayerPlaybackCoordinator._integratedTimeline
- _OBJC_IVAR_$_AVSampleBufferVideoRenderer._enqueuedFramesForLoggingOnly
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- __CMBlockBufferAsString
- ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke.201
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.181
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.181.cold.1
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.181.cold.2
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.457
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.458
- ___122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.150
- ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke.184
- ___146-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke.cold.1
- ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.156
- ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_2.158
- ___21-[AVPlayerLayer init]_block_invoke.129
- ___22-[AVPlayer _addLayer:]_block_invoke.616
- ___22-[AVPlayer _addLayer:]_block_invoke.617
- ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke.460
- ___31-[AVPlayerItem _updateTimebase]_block_invoke.658
- ___31-[AVPlayerItem _updateTimebase]_block_invoke_2.659
- ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke.512
- ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.296
- ___37-[AVPlayerItem setAudioTapProcessor:]_block_invoke
- ___39-[AVPlayerItem audioTapProcessorWasSet]_block_invoke
- ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke.569
- ___42-[AVPlayerCaptionLayer _interstitialLayer]_block_invoke.80
- ___44-[AVPlayerLayer _addObserversForVideoLayer:]_block_invoke.86
- ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke.72
- ___46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke.272
- ___49-[AVPlayerPlaybackCoordinator integratedTimeline]_block_invoke
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke.511
- ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke.310
- ___57-[AVPlayerItem _updateAudioTapProcessorOnFigPlaybackItem]_block_invoke
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.993
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.994
- ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.526
- ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke.166
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1186
- ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke.274
- ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.174
- ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke.99
- ___65-[AVPlayerPlaybackCoordinator _setIntegratedTimelineCreatingNew:]_block_invoke
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.108
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.109
- ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke.82
- ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke.524
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.469
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.470
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.483
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.495
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.504
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.507
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.487
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.496
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.505
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1172
- ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke.281
- ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.242
- ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.243
- ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.151
- ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.70
- ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.71
- ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke.914
- ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke.554
- ___78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.28
- ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke.56
- ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.130
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.71
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.74
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.89
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.143
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.144
- ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke.309
- ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.610
- ___90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke.367
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1169
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1271
- ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke.996
- ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2.997
- ___AVTelemetryLogHandle_block_invoke
- ___Block_byref_object_copy_.106
- ___Block_byref_object_copy_.145
- ___Block_byref_object_dispose_.107
- ___Block_byref_object_dispose_.146
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1428
- ___avplayer_fpNotificationCallback_block_invoke.1442
- ___avplayer_fpNotificationCallback_block_invoke.1445
- ___avplayer_fpNotificationCallback_block_invoke.1448
- ___avplayer_fpNotificationCallback_block_invoke.1458
- ___avplayer_fpNotificationCallback_block_invoke.1466
- ___avplayer_fpNotificationCallback_block_invoke_2.1449
- ___avplayer_fpNotificationCallback_block_invoke_2.1462
- ___avplayer_fpNotificationCallback_block_invoke_3.1453
- ___avplayer_fpNotificationCallback_block_invoke_3.1463
- ___avplayer_fpNotificationCallback_block_invoke_4.1464
- ___avplayer_iapdNotificationCallback_block_invoke.1468
- ___avplayer_iapdNotificationCallback_block_invoke.1469
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1617
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1637
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1639
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1640
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1641
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1642
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1646
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1647
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1648
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1649
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1650
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1651
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1656
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1662
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1663
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1667
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1668
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1669
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1676
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1652
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1657
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1664
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1653
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1665
- ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1654
- ___block_descriptor_48_e8_32o40b_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32o40r_e26_v32?0"AVCaption"8Q16^B24ls32l8r40l8
- ___block_descriptor_64_e8_32o40o48b56w_e24_v16?0"NSNotification"8ls32l8w56l8s48l8s40l8
- ___block_descriptor_72_e8_32o40o48o56r64r_e29_v24?0"NSArray"8"NSError"16lr56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_96_e8_32o40o48o56o64o72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8r88l8
- ___block_literal_global.1078
- ___block_literal_global.1080
- ___block_literal_global.109
- ___block_literal_global.1419
- ___block_literal_global.1472
- ___block_literal_global.1498
- ___block_literal_global.163
- ___block_literal_global.171
- ___block_literal_global.174
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.268
- ___block_literal_global.277
- ___block_literal_global.308
- ___block_literal_global.329
- ___block_literal_global.396
- ___block_literal_global.420
- ___block_literal_global.433
- ___block_literal_global.442
- ___block_literal_global.470
- ___block_literal_global.540
- ___block_literal_global.570
- ___block_literal_global.592
- ___block_literal_global.598
- ___block_literal_global.601
- ___block_literal_global.622
- ___block_literal_global.750
- ___block_literal_global.762
- ___block_literal_global.775
- ___block_literal_global.85
- ___block_literal_global.894
- ___block_literal_global.972
- ___figEndpointNotificationCallback_block_invoke.325
- ___figEndpointNotificationCallback_block_invoke.330
- ___handleFigAssetLoadingNotification_block_invoke.537
- ___handleFigAssetTrackNotification_block_invoke.468
- __figVideoQueueDidDropBelowLowWaterLevel.didDropBelowLowWaterLevelCountForLoggingOnly
- __os_signpost_emit_with_name_impl
- _backtrace
- _backtrace_symbols
- _gAVAssetCacheTrace
- _gAVAssetCustomURLTrace
- _gAVAssetDownloadSessionTrace
- _gAVAssetDownloadStorageManagerTrace
- _gAVAssetExportSessionTrace
- _gAVAssetImageGeneratorTrace
- _gAVAssetInspectorTrace
- _gAVAssetPlannerTrace
- _gAVAssetReaderOutputTrace
- _gAVAssetResourceLoaderTrace
- _gAVAssetTrace
- _gAVAssetTrackInspectorTrace
- _gAVAssetVariantTrace
- _gAVAssetWriterInputAnnotationAdaptorTrace
- _gAVAssetWriterInputMetadataAdaptorTrace
- _gAVAssetWriterInputTrace
- _gAVAssetWriterTrace
- _gAVAsynchronousKeyValueLoadingTrace
- _gAVCallbackContextRegistryTrace
- _gAVCaptionRendererTrace
- _gAVCompositionTrace
- _gAVCoreImageFilterCustomVideoCompositorTrace
- _gAVCustomCompositorTrace
- _gAVDelegateUtilitiesTrace
- _gAVExternalDeviceTrace
- _gAVFigObjectInspectorTrace
- _gAVFileSystemUtilitiesTrace
- _gAVKVODispatcherTrace
- _gAVLoggingIdentifierTrace
- _gAVMediaSelectionGroupTrace
- _gAVMediaStatePurge
- _gAVMetadataItemTrace
- _gAVMovieTrace
- _gAVOperationTrace
- _gAVPixelBufferAttributeMediator
- _gAVPlayerCaptionLayer
- _gAVPlayerItemLegibleOutputTrace
- _gAVPlayerItemMediaDataCollectorTrace
- _gAVPlayerItemMetadataCollector
- _gAVPlayerItemMetadataOutputTrace
- _gAVPlayerItemOutputTrace
- _gAVPlayerItemRenderedLegibleOutputTrace
- _gAVPlayerItemSampleBufferOutputTrace
- _gAVPlayerLayerTrace
- _gAVPlayerLooperTrace
- _gAVPlayerOutputTrace
- _gAVSampleBufferAudioRendererTrace
- _gAVSampleBufferDisplayLayerTrace
- _gAVSampleBufferGeneratorTrace
- _gAVSampleBufferRenderSynchronizerTrace
- _gAVSampleBufferVideoOutputTrace
- _gAVSampleCursorTrace
- _gAVScheduledAudioParameters
- _gAVStreamDataParserTrace
- _gAVTimebaseObserverTrace
- _gAVTimedMetadataGroupTrace
- _gAVUXMDisplayManager
- _gAVUtilitiesTrace
- _gScheduledParameterRampTrace
- _objc_msgSend$_canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:
- _objc_msgSend$_compactDescription
- _objc_msgSend$_resetGroupTimelineExpectations
- _objc_msgSend$_setIntegratedTimelineCreatingNew:
- _objc_msgSend$_updateAudioTapProcessorOnFigPlaybackItem
- _objc_msgSend$_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:
- _objc_msgSend$audioTapProcessorWasSet
- _objc_msgSend$colorSpace
- _objc_msgSend$copyVideoReceiver
- _objc_msgSend$externalContentProtectionStatus
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$setBorderColor:
- _objc_msgSend$setBorderWidth:
- _objc_msgSend$subarrayWithRange:
- _os_signpost_enabled
- _os_signpost_id_generate
- _setBounds:.oldRect.0
- _setBounds:.oldRect.1
- _setBounds:.oldRect.2
- _setBounds:.oldRect.3
- _stringWithValidatedFormat
- _stringWithValidatedFormatArg2
- _stringWithValidatedFormatString
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "-[AVPlayerItemIntegratedTimeline _issueCachedSeekIfNecessary]"
+ "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) canOverlapPlaybackFromPlayerItem:toPlayerItem:]"
+ "<<<< AVPlayerItemIntegratedTimeline >>>> %s: %p skip issuing cached seek %d at time %f with options %@"
+ "<<<< AVQueuePlayer >>>> %s: %p %{public}@. %s, can %{public}@ overlap %{public}@? %{public}s, triggered by %{public}@"
+ "<<<< AVQueuePlayer >>>> %s: %p %{public}@. Y->N, not enough items left, triggered by %{public}@"
+ "<<<< AVQueuePlayer >>>> %s: %p %{public}@: can %{public}@ overlap %{public}@? %{public}s"
+ "@\"AVPlayerInterstitialEvent\""
+ "AVVideoComposition has empty spatialVideoConfigurations. Expect composed tagged buffers having no spatial video configuration attachments"
+ "AVVideoComposition has non-empty spatialVideoConfigurations. Expect each pixel buffer in composed tagged buffers to have spatial video configuration attachments. Try call AVAsynchronousVideoCompositionRequest.attach(_:to:) on each pixel buffer before calling finish(withComposedTaggedBuffers:)"
+ "AVVideoComposition has non-empty spatialVideoConfigurations. Expect spatial video configuration attached to the pixel buffers in composed tagged buffers to equal to that from the AVVideoComposition's spatialVideoConfigurations"
+ "C24@0:8^{__CFDictionary=}16"
+ "Expect all pixel buffers in the composed tagged buffers having the same spatial video configuration attachments."
+ "N->Y"
+ "NO because the multichannel audio strategy permits exclusive passthrough"
+ "NO since AirPlay Video is active"
+ "NO since Buffered AirPlay is active and SenderSideMixing is not enabled"
+ "NO since HLS outro is multi channel and intro is stereo or mono"
+ "NO since HLS outro is stereo or mono and intro is multi channel"
+ "NO since action-at-end is NOT advance"
+ "NO since one of items is HLS and advance time for overlap is not enabled"
+ "NO since the first item is file based and doesn't have an audio track"
+ "NO since the first item is file based and its number of tracks is not 1"
+ "NO since the second item is file based and doesn't have an audio track"
+ "NO since the second item is file based and its number of tracks is not 1"
+ "Y->N"
+ "YES buffered airplay has matching channel count"
+ "YES but channel count for one of the Buffered AirPlay items is unknown"
+ "_applyCurrentAudioTapProcessorOnFigPlaybackItem"
+ "_cachedCurrentEvent"
+ "_canOverlapPlaybackFromPlayerItem:toPlayerItem:"
+ "_ensureIntegratedTimelineIsEstablished"
+ "_resetGroupTimelineExpectationsForIdentifier:"
+ "_resetPlaybackCoordinatorTimelineExpectations"
+ "_setCachedCurrentEvent:"
+ "_setItemAudioTapProcessor:fromAudioMixContext:"
+ "_shouldIssueCachedSeek:"
+ "_updateCachedCurrentEvent"
+ "_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:reportingObject:reportingSelector:"
+ "audioTapProcessorSetIsPending"
+ "audioTapProcessorWasSetFromAudioMix"
+ "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4"
+ "avplayer_fpNotificationCallback_block_invoke_15"
+ "calling attachSpatialVideoConfiguration:toPixelBuffer is illegal when AVVideoComposition's spatialVideoConfigurations is empty or nil"
+ "com.apple.avplayerinterstitialeventmonitor.ivars"
+ "v28@0:8^{opaqueMTAudioProcessingTap=}16B24"
+ "v40@0:8^{OpaqueCMTaggedBufferGroup=}16@24:32"
- "\n\t\"%@\""
- " "
- "%02x"
- "%c"
- "%d bytes [ %@ ] [ %@ ]"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "'SessionName' is missing in the session PList file"
- "(OSStatus)error.code"
- "*** SHOULD NOT receive kFigAssetNotification_PropertyRevised / kFigStdAssetProperty_Duration notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigAssetTrackProperty_EditSegmentData notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigStdTrackProperty_TimeRange notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "+[AVAnnotationRepresentation _annotationRepresentationWithPropertyList:binaryData:]"
- "+[AVAssetPlannerIncrementalState fromDictionary:error:]"
- "+[AVAssetPlannerTrackSegmentState fromDictionary:error:]"
- "+[AVAssetPlannerTrackState fromDictionary:error:]"
- "+[AVAssetTrackInspector assetTrackInspectorWithAsset:trackID:trackIndex:]"
- "+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke"
- "+[AVContentKeySession copyDefaultSecureStopManagerForAppIdentifier:storageDirectoryAtURL:]"
- "+[AVDataAsset _getFigAssetCreationOptionsFromDataAssetInitializationOptions:figAssetCreationFlags:]"
- "+[AVExternalPlaybackMonitor longFormVideoExternalPlaybackMonitor]"
- "+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
- "+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
- "+[AVMetadataItemFilterForSharing addIdentifier:toAllowListDictionary:]"
- "+[AVOperation(ArrayOfOperations) statusOfOperations:error:]"
- "+[AVPlayer availableHDRModes]"
- "+[AVPlayer fireAvailableHDRModesDidChangeNotification]"
- "+[AVPlayer fireEligibleForHDRPlaybackDidChangeNotification]"
- "+[AVPlayerItem _createFigPlaybackItemForFigPlayer:asset:URL:flags:options:playbackItem:]"
- "+[AVPlayerLayer _swapSublayersBetweenPlayerLayer:andPlayerLayer:]"
- "+[AVSampleBufferRenderSynchronizer _makeSTSLabel]"
- "+[AVSampleBufferRenderSynchronizer _makeSTSLabel]_block_invoke"
- "+[AVStreamDataParser(AVStreamDataParser_FigManifold) _createBlockBufferUsingNSData:withOffset:withLength:]"
- "+[AVURLAsset _avfValidationPlist]_block_invoke"
- "+[AVURLAsset _getFigAssetCreationOptionsFromURLAssetInitializationOptions:assetLoggingIdentifier:figAssetCreationFlags:error:]"
- ", associatedLayer %p"
- ", is a scrubbingLayer"
- ", is in playback mode"
- ", player %p"
- "- creating video queue failed previously"
- "-[AVAVAudioSettingsAudioOutputSettings getAudioStreamBasicDescription:forAudioFileTypeID:sourceFormatDescription:]"
- "-[AVAnnotation getJSONData:representationBinaryDataBindings:]"
- "-[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:]"
- "-[AVApplicationStateMonitor _didEnterBackground:]"
- "-[AVApplicationStateMonitor _willEnterForeground:]"
- "-[AVApplicationStateMonitor init]"
- "-[AVAsset mediaSelectionGroupForPropertyList:mediaSelectionOption:]"
- "-[AVAsset(AVAssetChapterInspection) _chapterMetadataGroupsBestMatchingPreferredLanguages:containingItemsWithCommonKeys:]"
- "-[AVAssetCustomURLBridgeForNSURLProtocol _cancelPendingRequests]"
- "-[AVAssetDownloadContentConfiguration _createFigContentConfigForEnvironmentalCondition:]"
- "-[AVAssetDownloadSession initWithAsset:mediaSelections:destinationURL:options:]"
- "-[AVAssetDownloadSession initWithDownloadToken:]"
- "-[AVAssetDownloadSession initWithURL:destinationURL:options:]"
- "-[AVAssetDownloadSession pause]_block_invoke"
- "-[AVAssetDownloadSession start]"
- "-[AVAssetDownloadSession stop]_block_invoke"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCacheOnDispatchQueue]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCache]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _readyForInspection]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:options:]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setupFigClientObjectAsync:]_block_invoke_2"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueueFirstTime]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueue]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _verifyDownloadConfigurationForAssetType]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) ensureProgressTimerIsRunningOnQueueWithError:]_block_invoke"
- "-[AVAssetDownloadStorageManager setStorageManagementPolicy:forURL:]"
- "-[AVAssetDownloadStorageManager storageManagementPolicyForURL:]_block_invoke"
- "-[AVAssetExportSession initWithAsset:presetName:]"
- "-[AVAssetExportSession initWithAsset:presetName:resumableSessionName:directoryForTemporaryFiles:]"
- "-[AVAssetExportSession setFileLengthLimit:]"
- "-[AVAssetExportSession setMaximizePowerEfficiency:]"
- "-[AVAssetImageGenerator _didGenerateCGImage:]"
- "-[AVAssetImageGenerator _ensureFigAssetImageGeneratorAllowingSynchronousPropertyLoad:error:]"
- "-[AVAssetImageGenerator _failedToGenerateCGImage:]"
- "-[AVAssetImageGenerator _serverDied]_block_invoke"
- "-[AVAssetImageGenerator cancelAllCGImageGeneration]"
- "-[AVAssetImageGenerator copyCGImageAtTime:actualTime:error:]"
- "-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]"
- "-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke"
- "-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_4"
- "-[AVAssetMediaSelectionGroup _mediaSelectionOptionWithPropertyList:matchToMediaSelectionArray:]"
- "-[AVAssetPlanner buildAssemblyComposition:]_block_invoke"
- "-[AVAssetPlanner planTrack:withSegmentsGeneratedBy:]"
- "-[AVAssetPlannerIncrementalState resumableBy:]"
- "-[AVAssetPlannerTrackSegmentState resumableBy:]"
- "-[AVAssetPlannerTrackState resumableBy:]"
- "-[AVAssetReaderOutput copyNextSampleBuffer]"
- "-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke"
- "-[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:]"
- "-[AVAssetResourceLoadingDataRequest respondWithData:]"
- "-[AVAssetResourceLoadingRequest _appendToCachedData:]"
- "-[AVAssetResourceLoadingRequest _appendToCachedData:]_block_invoke"
- "-[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:]"
- "-[AVAssetResourceLoadingRequest _sendFinishLoadingToCustomURLHandlerWithError:]"
- "-[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler]"
- "-[AVAssetResourceLoadingRequest finishLoadingWithError:]"
- "-[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:]"
- "-[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:]"
- "-[AVAssetWriter addInput:]"
- "-[AVAssetWriter addInputGroup:]"
- "-[AVAssetWriter cancelWriting]"
- "-[AVAssetWriter endSessionAtSourceTime:]"
- "-[AVAssetWriter finishWritingWithCompletionHandler:]"
- "-[AVAssetWriter finishWriting]"
- "-[AVAssetWriter flushSegment]"
- "-[AVAssetWriter flush]"
- "-[AVAssetWriter startSessionAtSourceTime:]"
- "-[AVAssetWriter startWriting]"
- "-[AVAssetWriterFinishWritingHelper _finishWritingOperationsDidFinish]"
- "-[AVAssetWriterFinishWritingHelper initWithConfigurationState:finishWritingOperations:figAssetWriterCallbackContextToken:figAssetWriter:figAssetWriterIsRemote:]_block_invoke"
- "-[AVAssetWriterInput _prepareToFinishWritingReturningError:]"
- "-[AVAssetWriterInput _setHelper:]_block_invoke"
- "-[AVAssetWriterInput appendSampleBuffer:]"
- "-[AVAssetWriterInput markAsFinished]"
- "-[AVAssetWriterInput markCurrentPassAsFinished]"
- "-[AVAssetWriterInput requestMediaDataWhenReadyOnQueue:usingBlock:]"
- "-[AVAssetWriterInput respondToEachPassDescriptionOnQueue:usingBlock:]"
- "-[AVAssetWriterInputAnnotationAdaptor appendAnnotation:]"
- "-[AVAssetWriterInputFigAssetWriterEndPassOperation _notifyWhetherMorePassesAreNeeded:timeRanges:forTrackWithID:]"
- "-[AVAssetWriterInputFigAssetWriterEndPassOperation dealloc]"
- "-[AVAssetWriterInputFigAssetWriterEndPassOperation start]"
- "-[AVAssetWriterInputInterPassAnalysisHelper startPassAnalysis]_block_invoke"
- "-[AVAssetWriterInputMediaDataRequester requestMediaDataIfNecessary]"
- "-[AVAssetWriterInputMetadataAdaptor appendTimedMetadataGroup:]"
- "-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]"
- "-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke"
- "-[AVAssetWriterInputTerminalHelper appendCaption:error:]"
- "-[AVAssetWriterInputTerminalHelper appendCaptionGroup:error:]"
- "-[AVAssetWriterInputTerminalHelper appendPixelBuffer:withPresentationTime:]"
- "-[AVAssetWriterInputTerminalHelper appendSampleBuffer:error:]"
- "-[AVAssetWriterInputTerminalHelper appendTaggedPixelBufferGroup:withPresentationTime:]"
- "-[AVAssetWriterInputWritingHelper appendCaption:error:]"
- "-[AVAssetWriterInputWritingHelper appendCaptionGroup:error:]"
- "-[AVAssetWriterInputWritingHelper appendPixelBuffer:withPresentationTime:]"
- "-[AVAssetWriterInputWritingHelper appendSampleBuffer:error:]"
- "-[AVAssetWriterInputWritingHelper appendTaggedPixelBufferGroup:withPresentationTime:]"
- "-[AVAssetWriterInputWritingHelper observeValueForKeyPath:ofObject:change:context:]"
- "-[AVAssetWriterInputWritingHelper transitionToAndReturnTerminalHelperWithTerminalStatus:]"
- "-[AVAssetWriterWritingHelper cancelWriting]"
- "-[AVAssetWriterWritingHelper finishWritingWithCompletionHandler:]_block_invoke"
- "-[AVAssetWriterWritingHelper finishWriting]_block_invoke"
- "-[AVAssetWriterWritingHelper initWithConfigurationState:assetWriter:error:]"
- "-[AVAssetWriterWritingHelper storageSpacePreallocationSize]"
- "-[AVAsynchronousCIImageFilteringRequest finishWithError:]"
- "-[AVAsynchronousCIImageFilteringRequest finishWithImage:context:]"
- "-[AVAsynchronousCIImageFilteringRequest sourceImage]"
- "-[AVBlockOperation cancel]"
- "-[AVBlockOperation start]"
- "-[AVCallbackContextRegistry registerCallbackContextObject:]_block_invoke"
- "-[AVCallbackContextRegistry unregisterCallbackContextForToken:]_block_invoke"
- "-[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession]"
- "-[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession]_block_invoke"
- "-[AVCaptionRenderer captionSceneChangesInRange:]"
- "-[AVCaptionRenderer init]"
- "-[AVCaptionRenderer renderInContext:atTime:]"
- "-[AVCaptionRenderer teardownFigCaptionClient]"
- "-[AVClientBlockKVONotifier cancelCallbacks]"
- "-[AVClientBlockKVONotifier dealloc]"
- "-[AVClientBlockKVONotifier start]"
- "-[AVCommonLoggingIdentifier initWithIdentifierSuffix:prefixlength:]"
- "-[AVComposition _initWithComposition:]"
- "-[AVComposition mutableCopyWithZone:]"
- "-[AVCompositionTrackReaderInspector segments]"
- "-[AVContentKeyReportGroup _associateRequestWithGroupWithRequestID:error:]"
- "-[AVContentKeyReportGroup _destroyContentKeyGroupWithError:]"
- "-[AVContentKeyReportGroup cryptorOptionsForIdentifier:initializationData:formatDescription:hlsMethod:]"
- "-[AVContentKeyReportGroup failProcessingContentKeyRequestWithIdentifier:initializationData:error:]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:]_block_invoke"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) configureAppIdentifier:]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) copyCryptorForCryptKeyAttributes:]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) createProtectorSessionIdentifierIfNecessary]_block_invoke"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) externalProtectionStatusForCryptor:withDisplays:]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) hasProtector]"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) copyCryptorForIdentifier:initializationData:]_block_invoke"
- "-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) createCryptorIfNecessaryForIdentifier:initializationData:formatDescription:hlsMethod:error:]_block_invoke"
- "-[AVContentKeyRequest _processContentKeyResponse:renewalDate:initializationVector:error:]"
- "-[AVContentKeyRequest _processContentKeyResponseError:]"
- "-[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus]"
- "-[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:]"
- "-[AVContentKeySession externalProtectionStateChangedCallbackWithBoss:keySpecifier:]_block_invoke"
- "-[AVContentKeySession(AVContentKeyRequestSupport) contentKeyRequestDidProduceContentKey:]_block_invoke"
- "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequest:toDelegateWithCallbackSelector:]"
- "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequestWithPreloadingRequestOptions:identifier:initializationData:providesPersistableKey:]"
- "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequests:forInitializationData:]"
- "-[AVContentKeySession(AVContentKeySession_Internal) createAndInstallCustomURLHandlerForAsset:outHandler:]"
- "-[AVContentKeySession(AVContentKeySession_Internal) issueContentKeyRequestForInitializationData:]"
- "-[AVContentKeySession(FigContentKeyBoss) _processContentKeyRequestWithIdentifier:encryptionMethod:supportedProtocolVersions:options:groupID:error:]"
- "-[AVCoordinatedPlaybackSuspension initWithCoordinator:reason:]"
- "-[AVCoreImageFilterCustomVideoCompositor cancelAllPendingVideoCompositionRequests]"
- "-[AVCoreImageFilterCustomVideoCompositor renderContextChanged:]"
- "-[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:]"
- "-[AVCustomVideoCompositorSession commitCustomVideoCompositorPropertiesAndReturnError:]"
- "-[AVCustomVideoCompositorSession initWithVideoComposition:]"
- "-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_2"
- "-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _customCompositorFigPropertyDidChange]_block_invoke"
- "-[AVDateRangeMetadataGroup(AVDateRangeMetadataGroup_Local) _extractPropertiesFromTaggedRangeMetadataDictionary:]"
- "-[AVDelegatingPlaybackCoordinator _endSuspension:]"
- "-[AVDelegatingPlaybackCoordinator _endSuspension:proposingNewTime:]"
- "-[AVDelegatingPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession]"
- "-[AVDelegatingPlaybackCoordinator _setWaitingPolicies:]"
- "-[AVDelegatingPlaybackCoordinator applyFigPauseSnapsToMediaTimeOfOriginator]_block_invoke"
- "-[AVDelegatingPlaybackCoordinator beginSuspensionForReason:]"
- "-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]"
- "-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke"
- "-[AVDelegatingPlaybackCoordinator participantForIdentifier:]_block_invoke"
- "-[AVExternalDevice _figEndpointPropertyValueForKey:]"
- "-[AVExternalDevice externalDeviceHIDs]_block_invoke"
- "-[AVExternalDevice screenIDs]"
- "-[AVExternalDevice screenInputCapabilities]"
- "-[AVExternalDevice screenPrimaryInputDevices]"
- "-[AVExternalDeviceHID _figEndpointHIDInputMode]"
- "-[AVExternalDeviceHID initWithExternalDeviceAndHIDDictionary:hidDictionary:]"
- "-[AVExternalDeviceHID setInputMode:]"
- "-[AVExternalDeviceIcon initWithDictionary:]"
- "-[AVExternalDeviceScreenBorrowToken dealloc]"
- "-[AVExternalDeviceScreenBorrowToken initWithExternalDevice:client:reason:]"
- "-[AVExternalDeviceTurnByTurnToken dealloc]"
- "-[AVExternalDeviceTurnByTurnToken initWithExternalDevice:]"
- "-[AVExternalPlaybackMonitor dealloc]"
- "-[AVExternalPlaybackMonitor initWithFigRoutingSessionManager:]"
- "-[AVExternalPlaybackMonitor isAirPlayVideoActive]"
- "-[AVExternalPlaybackMonitor isAirPlayVideoPlaying]"
- "-[AVFigAssetInspector _localizedMediaSelectionOptionDisplayNames]"
- "-[AVFigAssetInspector variants]"
- "-[AVFigAssetInspectorLoader _loadStatusForProperty:figAsset:error:]"
- "-[AVFigAssetInspectorLoader _statusOfValueForKey:error:firstNonLoadedDependencyKey:]"
- "-[AVFigAssetTrackInspector _initWithAsset:trackID:trackIndex:]"
- "-[AVFigAssetTrackInspector _invokeCompletionHandlerForLoadingBatches:]"
- "-[AVFigAssetTrackInspector _loadStatusForFigAssetTrackProperty:error:]"
- "-[AVFigAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:]"
- "-[AVFigAssetWriterFinishWritingAsyncOperation cancel]"
- "-[AVFigAssetWriterFinishWritingAsyncOperation didEnterTerminalState]"
- "-[AVFigAssetWriterFinishWritingAsyncOperation didReceiveFigAssetWriterNotificationWithSuccess:error:]"
- "-[AVFigAssetWriterFinishWritingAsyncOperation start]"
- "-[AVFigAssetWriterTrack _refreshAboveHighWaterLevel]_block_invoke"
- "-[AVFigAssetWriterTrack endPassWithCompletionHandler:]"
- "-[AVFigAssetWriterTrack setFormatDescriptions:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification addPeerToHomeGroup:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup]"
- "-[AVFigRoutingContextRouteChangeOperation _routeChangeComplete]"
- "-[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:]"
- "-[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:]_block_invoke"
- "-[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]"
- "-[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]_block_invoke"
- "-[AVFigRoutingContextRouteChangeOperation start]"
- "-[AVKVODispatcher observeValueForKeyPath:ofObject:change:context:]"
- "-[AVKeyPathDependency _reactToSecondLevelPropertyChange:]"
- "-[AVKeyPathDependency _reactToTopLevelPropertyChange:]"
- "-[AVKeyPathDependency _reactToTopLevelPropertyChange:]_block_invoke"
- "-[AVKeyPathDependency _startObservingSecondLevelPropertyOnNewCurrentValueForTopLevelDependencyProperty:]"
- "-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke"
- "-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_2"
- "-[AVManagedAssetCache enableAutomaticCacheSizeManagement]"
- "-[AVManagedAssetCache initWithURL:enableCRABSCache:enableHLSCache:]"
- "-[AVManagedAssetCache removeEntryForKey:]"
- "-[AVManagedAssetCache setMaxEntrySize:]"
- "-[AVManagedAssetCache setMaxSize:]"
- "-[AVMapPublisher subscribeRequestingInitialValue:block:]_block_invoke"
- "-[AVMetadataItem(AVMetadataItem_Local) _extractPropertiesFromDictionary:]"
- "-[AVMetadataItem(AVMetadataItem_Local) _valueFromCFType:]"
- "-[AVMovie _initWithFigAsset:]"
- "-[AVMovie _initWithFigError:userInfo:]"
- "-[AVMovie _initWithFormatReader:URL:data:options:]"
- "-[AVMovie initWithData:options:]"
- "-[AVMovie initWithURL:options:]"
- "-[AVMovie init]"
- "-[AVMutableComposition _addMutableTrackWithMediaType:preferredTrackID:fireKVO:]"
- "-[AVMutableComposition _removeTrack:fireKVO:]"
- "-[AVMutableComposition insertEmptyTimeRange:]"
- "-[AVMutableComposition insertTimeRange:ofAsset:atTime:error:]"
- "-[AVMutableComposition mutableTrackCompatibleWithTrack:]"
- "-[AVMutableComposition removeTimeRange:]"
- "-[AVMutableComposition scaleTimeRange:toDuration:]"
- "-[AVMutableCompositionTrack _insertEmptyTimeRange:fireKVO:]"
- "-[AVMutableCompositionTrack _insertTimeRange:ofTrack:atTime:fireKVO:error:]"
- "-[AVMutableCompositionTrack _removeTimeRange:fireKVO:]"
- "-[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:]"
- "-[AVMutableCompositionTrack scaleTimeRange:toDuration:]"
- "-[AVMutableCompositionTrack setSegments:]"
- "-[AVMutableCompositionTrack validateTrackSegments:error:]"
- "-[AVMutableMovie _initWithFormatReader:URL:data:options:]"
- "-[AVMutableMovie initWithData:options:error:]"
- "-[AVMutableMovie initWithSettingsFromMovie:options:error:]"
- "-[AVMutableMovie initWithURL:options:error:]"
- "-[AVMutableMovie setPreferredTransform:]"
- "-[AVMutableMovieTrack setAlternateGroupID:]"
- "-[AVMutableMovieTrack setLayer:]"
- "-[AVMutableMovieTrack setPreferredTransform:]"
- "-[AVNotificationSubscription cancel]"
- "-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:]"
- "-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:]_block_invoke"
- "-[AVOccasionalTimebaseObserver _effectiveRateChanged]"
- "-[AVOccasionalTimebaseObserver _fireBlock]"
- "-[AVOccasionalTimebaseObserver _resetNextFireTime]"
- "-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]"
- "-[AVOnceTimebaseObserver _fireBlock]"
- "-[AVOnceTimebaseObserver _resetNextFireTime]_block_invoke"
- "-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]"
- "-[AVOperation _setStatus:error:resultingStatus:failureReason:]_block_invoke"
- "-[AVOperation didEnterTerminalState]"
- "-[AVOperation evaluateDependenciesAndMarkAsExecuting]"
- "-[AVOperation markAsCancelled]"
- "-[AVOperation markAsCompleted]"
- "-[AVOperation markAsFailedWithError:]"
- "-[AVPeriodicTimebaseObserver _effectiveRateChanged]"
- "-[AVPeriodicTimebaseObserver _fireBlockForTime:]"
- "-[AVPeriodicTimebaseObserver _handleTimeDiscontinuity]"
- "-[AVPeriodicTimebaseObserver _resetNextFireTime]"
- "-[AVPlaybackCoordinationMedium _updateLowestInUseDefaultItemIdentifier]_block_invoke"
- "-[AVPlaybackCoordinationMedium _updateTransportControlState:forIdentifier:]_block_invoke"
- "-[AVPlaybackCoordinationMedium areAllCoordinatorsSuspendedForReason:]"
- "-[AVPlaybackCoordinationMedium connectPlaybackCoordinator:]"
- "-[AVPlaybackCoordinationMedium disconnectPlaybackCoordinatorWithIdentifier:]"
- "-[AVPlaybackCoordinationMedium endSuspensionOnAllCoordinatorsWithReason:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastLocalParticipantStateDictionary:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]_block_invoke"
- "-[AVPlayer _addLayer:]"
- "-[AVPlayer _addLayer:]_block_invoke"
- "-[AVPlayer _addVideoLayer:]"
- "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]"
- "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke"
- "-[AVPlayer _closedCaptionLayers]"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6"
- "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]"
- "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke"
- "-[AVPlayer _handleSetRate:withVolumeRampDuration:playImmediately:rateChangeReason:affectsCoordinatedPlayback:]_block_invoke"
- "-[AVPlayer _itemIsReadyToPlay:]_block_invoke"
- "-[AVPlayer _reevaluateVideoLayersAndTargetsForPresentationState:withCompletionHandler:]"
- "-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_3"
- "-[AVPlayer _removeVideoLayer:]"
- "-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]"
- "-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]"
- "-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]"
- "-[AVPlayer _updateDecoderPixelBufferAttributes:onFigPlayer:]"
- "-[AVPlayer _updatePixelBufferAttributesForLayer:]"
- "-[AVPlayer _userVolume]"
- "-[AVPlayer _videoLayers]"
- "-[AVPlayer prepareItem:withCompletionHandler:]"
- "-[AVPlayer removeTimeObserver:]"
- "-[AVPlayer seekToDate:completionHandler:]"
- "-[AVPlayer seekToTime:completionHandler:]"
- "-[AVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:]"
- "-[AVPlayer setAudiovisualBackgroundPlaybackPolicy:]"
- "-[AVPlayer setDefaultRate:]"
- "-[AVPlayer setExpectedAssetTypes:]"
- "-[AVPlayer setExpectedAssetTypes:]_block_invoke_2"
- "-[AVPlayer setOutputContext:]"
- "-[AVPlayer setPlayerRole:synchronously:]"
- "-[AVPlayer setResourceConservationLevelWhilePaused:]"
- "-[AVPlayer setShouldReduceResourceUsage:]"
- "-[AVPlayer(AVPlayerAdvanceWithOverlap) _setSupportsAdvanceTimeForOverlappedPlayback:]"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]_block_invoke"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _hasCurrentInterstitialEvent]"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _linkAndSyncAudioSessionWithInterstitialPlayer:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _acquireBackgroundAssertion]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _applicationHasExternallyDisplayedAVPlayerLayerAndIsUnderDeviceLock]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _canContinuePlaybackInBackgrounBasedOnAudiovisualBackgroundPlaybackPolicy:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_3"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:withCompletionHandler:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoDestinationsAreAttached]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _hasAssociatedAVPlayerLayerInPIPMode]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _itemOkayToPlayWhileTransitioningToBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _layerForegroundStateChanged:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _shouldDetachVideoLayersFromFigPlayer]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _willEnterForeground:]"
- "-[AVPlayer(AVPlayerPIPSupport) setBackgroundPIPAuthorizationToken:]"
- "-[AVPlayer(AVPlayerSpeedRamp) canPlaySpeedRamp]"
- "-[AVPlayer(AVPlayerSpeedRamp) setSupportsSpeedRamps:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _resumePlayback:error:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _updateConnectionToSecondScreen]"
- "-[AVPlayer(FigVideoTargetSupport) addVideoTarget:]"
- "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]"
- "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke"
- "-[AVPlayer(PlaybackCoordination) _addCoordinatedPlaybackSuspensionWithReasonOnQueue:]"
- "-[AVPlayer(PlaybackCoordination) _ensureFigPlaybackCoordinatorIsConnected]"
- "-[AVPlayer(PlaybackCoordination) _removeCoordinatedPlaybackSuspensionWithReasonOnQueue:requiringSuspensionEnd:]"
- "-[AVPlayerCaptionLayer _interstitialLayer]"
- "-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke"
- "-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke_2"
- "-[AVPlayerCaptionLayer _startObservingPlayer:]"
- "-[AVPlayerCaptionLayer _stopObservingPlayer:]"
- "-[AVPlayerCaptionLayer layoutSublayers]"
- "-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]"
- "-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke"
- "-[AVPlayerCaptionLayer setBounds:]"
- "-[AVPlayerCaptionLayer setCaptionContentInsets:]"
- "-[AVPlayerCaptionLayer setPlayer:]"
- "-[AVPlayerCaptionLayer setValue:forKeyPath:]"
- "-[AVPlayerConnection addItemToPlayQueueAfterPlaybackItemOfItem:]"
- "-[AVPlayerItem _addToPlayQueueOfFigPlayerOfPlayer:afterFigPlaybackItemOfItem:]"
- "-[AVPlayerItem _applyCurrentVideoComposition]"
- "-[AVPlayerItem _applyMediaSelectionOptions]_block_invoke"
- "-[AVPlayerItem _attachToFigPlayer]"
- "-[AVPlayerItem _attachToPlayer:]"
- "-[AVPlayerItem _cancelPendingSeekAndRegisterSeekID:withCompletionHandler:]"
- "-[AVPlayerItem _changeStatusToFailedWithError:]"
- "-[AVPlayerItem _configurePlaybackItemAndReturnError:]"
- "-[AVPlayerItem _currentMediaSelectionFromFigSelectedMediaArray:]"
- "-[AVPlayerItem _invokeReadyForEnqueueingHandlers]"
- "-[AVPlayerItem _makeReadyForEnqueueingWithCompletionHandler:]"
- "-[AVPlayerItem _postSeekCompletionNotificationWithSeekID:andResult:]"
- "-[AVPlayerItem _presentationSize]"
- "-[AVPlayerItem _seekToTime:toleranceBefore:toleranceAfter:seekID:completionHandler:]"
- "-[AVPlayerItem _selectMediaOption:inMediaSelectionGroup:]"
- "-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]"
- "-[AVPlayerItem _setAudioProcessingEffectsAccordingToInputParameters:forTrackID:]"
- "-[AVPlayerItem _setCurrentMediaSelection:]"
- "-[AVPlayerItem _setVideoCompositionInstructions:]"
- "-[AVPlayerItem _tracks]"
- "-[AVPlayerItem _unregisterInvokeAndReleasePendingSeekCompletionHandlerForSeekID:finished:]"
- "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]"
- "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]_block_invoke"
- "-[AVPlayerItem _updateTimebase]_block_invoke_2"
- "-[AVPlayerItem currentMediaSelection]"
- "-[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:]"
- "-[AVPlayerItem seekToDate:completionHandler:]"
- "-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]_block_invoke"
- "-[AVPlayerItem setAdvanceTimeForOverlappedPlayback:]"
- "-[AVPlayerItem(AVPlayerItemOutputs) _evaluateMetadataOutputs]_block_invoke"
- "-[AVPlayerItem(AVPlayerItemVideoEnhancement) setVideoEnhancementMode:]"
- "-[AVPlayerItemLegibleOutput _pushAttributedStrings:andSampleBuffers:atItemTime:]_block_invoke"
- "-[AVPlayerItemLegibleOutput _signalFlush]"
- "-[AVPlayerItemLegibleOutput _signalFlush]_block_invoke"
- "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _pushTimedMetadataGroups:fromPlayerItemTrack:]_block_invoke_3"
- "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke"
- "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_2"
- "-[AVPlayerItemOutput _itemTimeForHostTimeAsCMTime:]"
- "-[AVPlayerItemRenderedLegibleOutput _pushRenderedCaptionImages:atItemTime:]_block_invoke"
- "-[AVPlayerItemRenderedLegibleOutput _signalFlush]"
- "-[AVPlayerItemRenderedLegibleOutput _signalFlush]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke_2"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:]_block_invoke_2"
- "-[AVPlayerItemSampleBufferOutput copyNextSampleBufferForTrackID:flags:]"
- "-[AVPlayerItemTrack(AVPlayerItemOutputs) addOutput:]"
- "-[AVPlayerItemTrack(AVPlayerItemOutputs) removeOutput:]"
- "-[AVPlayerItemVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:]"
- "-[AVPlayerItemVideoOutput _dispatchOutputMediaDataWillChange]_block_invoke"
- "-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed]"
- "-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke"
- "-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeAsSoonAsPossible]_block_invoke"
- "-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeWithAdvanceInterval:]_block_invoke"
- "-[AVPlayerItemVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:]"
- "-[AVPlayerLayer _addObserversForVideoLayer:]"
- "-[AVPlayerLayer _addObserversForVideoLayer:]_block_invoke"
- "-[AVPlayerLayer _applyPresentationSizeChange:andForceUpdate:]"
- "-[AVPlayerLayer _applyPresentationSizeChange:andForceUpdate:]_block_invoke"
- "-[AVPlayerLayer _currentWindowSceneIsForegroundDefault]"
- "-[AVPlayerLayer _currentWindowSceneIsForeground]"
- "-[AVPlayerLayer _displaySize]"
- "-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:]"
- "-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:]_block_invoke"
- "-[AVPlayerLayer _enterSecondScreenModeRedirectingVideoToLayer:]"
- "-[AVPlayerLayer _enterSecondScreenModeRedirectingVideoToLayer:]_block_invoke"
- "-[AVPlayerLayer _forceLayout]"
- "-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke"
- "-[AVPlayerLayer _handleNonForcedSubtitleDisplayDidChange:player:]_block_invoke"
- "-[AVPlayerLayer _interstitialLayer]"
- "-[AVPlayerLayer _leavePIPModeForLayer:]"
- "-[AVPlayerLayer _leaveSecondScreenModeForLayer:]"
- "-[AVPlayerLayer _notifyPlayerOfDisplaySize]"
- "-[AVPlayerLayer _notifyPlayerOfLayerForegroundStateChange]"
- "-[AVPlayerLayer _percentCoverageRelativeToRootLayer]"
- "-[AVPlayerLayer _presentationSize]"
- "-[AVPlayerLayer _restoreClientLayers:intoMaskLayer:]"
- "-[AVPlayerLayer _setIsPartOfForegroundScene:]_block_invoke"
- "-[AVPlayerLayer _setPlayer:forPIP:]"
- "-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke"
- "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]"
- "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke"
- "-[AVPlayerLayer _setSublayersForPIP:updateReadyForDisplay:]"
- "-[AVPlayerLayer _startObservingPlayer:]"
- "-[AVPlayerLayer _stopObservingPlayer:]"
- "-[AVPlayerLayer _updatePreferredDynamicRangeWithAnimation:]_block_invoke"
- "-[AVPlayerLayer _updateReadyForDisplayForPlayerCurrentItemAndForceKVO:]_block_invoke"
- "-[AVPlayerLayer _updateReadyForDisplayOnMainQueue:skipInformingParent:forceKVO:]"
- "-[AVPlayerLayer _windowSceneDidEnterBackground]"
- "-[AVPlayerLayer _windowSceneWillEnterForeground]"
- "-[AVPlayerLayer addSublayer:]"
- "-[AVPlayerLayer copyDisplayedPixelBuffer]"
- "-[AVPlayerLayer init]"
- "-[AVPlayerLayer init]_block_invoke"
- "-[AVPlayerLayer insertSublayer:above:]"
- "-[AVPlayerLayer insertSublayer:atIndex:]"
- "-[AVPlayerLayer insertSublayer:below:]"
- "-[AVPlayerLayer layerDidBecomeVisible:]"
- "-[AVPlayerLayer layoutSublayers]"
- "-[AVPlayerLayer layoutSublayers]_block_invoke"
- "-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]"
- "-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke"
- "-[AVPlayerLayer pixelBufferAttributes]"
- "-[AVPlayerLayer removeFromSuperlayer]"
- "-[AVPlayerLayer replaceSublayer:with:]"
- "-[AVPlayerLayer setBounds:]"
- "-[AVPlayerLayer setForScrubbingOnly:]"
- "-[AVPlayerLayer setLanczosFilterDownscaleFactor:]"
- "-[AVPlayerLayer setLegibleContentInsets:]"
- "-[AVPlayerLayer setSublayers:]"
- "-[AVPlayerLooper _calculateNumberOfCopiesNeeded]"
- "-[AVPlayerLooper _changeStatusToFailedWithError:]"
- "-[AVPlayerLooper _changeStatusToFailedWithError:]_block_invoke"
- "-[AVPlayerLooper _setupLoopingReturningError:]"
- "-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke"
- "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]"
- "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]_block_invoke"
- "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]_block_invoke_2"
- "-[AVPlayerLooper observeValueForKeyPath:ofObject:change:context:]"
- "-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke"
- "-[AVPlayerPlaybackCoordinator _applyIntegratedTimelineSeek:]"
- "-[AVPlayerPlaybackCoordinator _convertToMediaTimeForTime:withNetworkTime:rate:]"
- "-[AVPlayerPlaybackCoordinator _endSuspension:]"
- "-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]"
- "-[AVPlayerPlaybackCoordinator _endSuspensionWithReason:]"
- "-[AVPlayerPlaybackCoordinator _hasRemovedSuspensionReason:currentReasons:newReasons:]"
- "-[AVPlayerPlaybackCoordinator _reactToNewDelegate]"
- "-[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectations]"
- "-[AVPlayerPlaybackCoordinator _setIntegratedTimelineCreatingNew:]"
- "-[AVPlayerPlaybackCoordinator _setInterstitialActive:]"
- "-[AVPlayerPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession]"
- "-[AVPlayerPlaybackCoordinator _synchronizeWorkOnPlayerQueue:]"
- "-[AVPlayerPlaybackCoordinator _updateCoordinationMediumDelegateOnFigPlaybackCoordinator]"
- "-[AVPlayerPlaybackCoordinator _updateLocalParticipantUUIDOnFigPlaybackCoordinator:]_block_invoke"
- "-[AVPlayerPlaybackCoordinator _updateParticipantStateOnFigPlaybackCoordinatorForItemWithIdentifier:]"
- "-[AVPlayerPlaybackCoordinator _updatePauseSnapsToMediaTimeOfOriginatorOnFigPlaybackCoordinator]_block_invoke"
- "-[AVPlayerPlaybackCoordinator _updateSuspensionsForNewSuspensionReasons:]"
- "-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:]"
- "-[AVPlayerPlaybackCoordinator _updateWaitingPoliciesOnFigPlaybackCoordinator:]"
- "-[AVPlayerPlaybackCoordinator beginSuspensionForReason:]"
- "-[AVPlayerPlaybackCoordinator coordinateUsingCoordinationMedium:error:]"
- "-[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:]"
- "-[AVPlayerPlaybackCoordinator participantForIdentifier:]_block_invoke"
- "-[AVPlayerPlaybackCoordinator setDefaultItemIdentifierCounter:postingNotification:]"
- "-[AVPlayerPlaybackCoordinator setFigPlaybackCoordinator:]_block_invoke"
- "-[AVPlayerRateState rateStateBySettingRate:nameForLogging:]"
- "-[AVPlayerRateState rateStateByUpdatingBasedOnFigPlayer:hasCurrentItem:hasCurrentInterstitialEvent:nameForLogging:]"
- "-[AVPlayerRateState rateStateByUpdatingBasedOnPresenceOfCurrentInterstitialEvent:nameForLogging:]"
- "-[AVPlayerVideoOutput _attachToPlayer:exceptionReason:]_block_invoke"
- "-[AVPlayerVideoOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue]"
- "-[AVPlayerVideoOutput _handleVideoReceiverActiveConfigurationChanged:]"
- "-[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:]"
- "-[AVPlayerVideoOutput hasNewTaggedBufferGroupForHostTime:]"
- "-[AVPropertyValuePublisher subscribeRequestingInitialValue:block:]"
- "-[AVPropertyValuePublisher subscribeRequestingInitialValue:block:]_block_invoke"
- "-[AVQueuePlayer insertItem:afterItem:]"
- "-[AVQueuePlayer removeAllItems]"
- "-[AVQueuePlayer removeItem:]"
- "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:]"
- "-[AVQueuePlayer(AVPlayerItemPreBuffering) setItemsToPrebuffer:]"
- "-[AVResourceReclamationAssertion dealloc]"
- "-[AVResourceReclamationAssertion initWithDetails:]"
- "-[AVResourceReclamationController(AVResourceReclamation) permitReclamationWhileSuspended]"
- "-[AVResourceReclamationEvent dealloc]"
- "-[AVResourceReclamationEventObserverToken dealloc]"
- "-[AVResourceReclamationEventObserverToken initWithDetails:]"
- "-[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation _routeConfigUpdateWithID:endedWithReason:]"
- "-[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation start]"
- "-[AVRouteDetector _updateMultipleRoutesDetected]"
- "-[AVRouteDetector _updateRouteDetectionEnabled]"
- "-[AVRouteDetector _updateRouteDetectionEnabled]_block_invoke"
- "-[AVSampleBufferAudioRenderer _installNotificationHandlers]"
- "-[AVSampleBufferAudioRenderer _transitionToStatus:error:]"
- "-[AVSampleBufferAudioRenderer _uninstallNotificationHandlers]"
- "-[AVSampleBufferAudioRenderer allowedAudioSpatializationFormats]"
- "-[AVSampleBufferAudioRenderer audioOutputDeviceUniqueID]"
- "-[AVSampleBufferAudioRenderer audioTapProcessor]"
- "-[AVSampleBufferAudioRenderer audioTimePitchAlgorithm]"
- "-[AVSampleBufferAudioRenderer copyFigSampleBufferAudioRenderer:]"
- "-[AVSampleBufferAudioRenderer dealloc]"
- "-[AVSampleBufferAudioRenderer enqueueSampleBuffer:]"
- "-[AVSampleBufferAudioRenderer error]"
- "-[AVSampleBufferAudioRenderer flushFromSourceTime:completionHandler:]"
- "-[AVSampleBufferAudioRenderer flush]"
- "-[AVSampleBufferAudioRenderer init]"
- "-[AVSampleBufferAudioRenderer isMuted]"
- "-[AVSampleBufferAudioRenderer isReadyForMoreMediaData]"
- "-[AVSampleBufferAudioRenderer outputContext]"
- "-[AVSampleBufferAudioRenderer requestMediaDataWhenReadyOnQueue:usingBlock:]"
- "-[AVSampleBufferAudioRenderer setAllowedAudioSpatializationFormats:]"
- "-[AVSampleBufferAudioRenderer setAudioOutputDeviceUniqueID:]"
- "-[AVSampleBufferAudioRenderer setAudioTapProcessor:]"
- "-[AVSampleBufferAudioRenderer setAudioTimePitchAlgorithm:]"
- "-[AVSampleBufferAudioRenderer setMuted:]"
- "-[AVSampleBufferAudioRenderer setOutputContext:]"
- "-[AVSampleBufferAudioRenderer setRenderSynchronizer:error:]"
- "-[AVSampleBufferAudioRenderer setSTSLabel:]"
- "-[AVSampleBufferAudioRenderer setVolume:]"
- "-[AVSampleBufferAudioRenderer status]"
- "-[AVSampleBufferAudioRenderer stopRequestingMediaData]"
- "-[AVSampleBufferAudioRenderer timebase]"
- "-[AVSampleBufferAudioRenderer volume]"
- "-[AVSampleBufferDisplayLayer _updateLayerTreeGeometryWithVideoGravity:presentationSize:videoGravityShouldTriggerAnimation:]_block_invoke"
- "-[AVSampleBufferDisplayLayer dealloc]"
- "-[AVSampleBufferDisplayLayer init]"
- "-[AVSampleBufferDisplayLayer layerDidBecomeVisible:]"
- "-[AVSampleBufferDisplayLayer layoutSublayers]"
- "-[AVSampleBufferDisplayLayer setBounds:]"
- "-[AVSampleBufferDisplayLayer setSTSLabel:]"
- "-[AVSampleBufferDisplayLayer setSTSLabel:]_block_invoke"
- "-[AVSampleBufferDisplayLayer videoRect]"
- "-[AVSampleBufferDisplayLayer(AVSampleBufferDisplayLayerOutput) setOverridesPreferredDynamicRangeForVideo:]"
- "-[AVSampleBufferDisplayLayer(AVSampleBufferDisplayLayerQueueManagement) enqueueSampleBuffer:]"
- "-[AVSampleBufferRenderSynchronizer _setRate:time:atHostTime:]"
- "-[AVSampleBufferRenderSynchronizer dealloc]"
- "-[AVSampleBufferRenderSynchronizer init]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]_block_invoke_3"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _scheduleTimedRendererRemovalAtTime:atTime:withClientCompletionHandler:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) addRenderer:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _canAddRendererInternal:error:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _rendererConfigurationIsValid:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerTimeObservation) removeTimeObserver:]"
- "-[AVSampleBufferVideoOutput _configureWithVideoQueue:]"
- "-[AVSampleBufferVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:]"
- "-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed]"
- "-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke"
- "-[AVSampleBufferVideoOutput copyLastPixelBuffer:]"
- "-[AVSampleBufferVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:]"
- "-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]"
- "-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]"
- "-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke"
- "-[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:]"
- "-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]"
- "-[AVSampleBufferVideoRenderer _flushComplete]"
- "-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]"
- "-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke"
- "-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_2"
- "-[AVSampleBufferVideoRenderer _setOutputObscuredDueToInsufficientExternalProtection:]"
- "-[AVSampleBufferVideoRenderer _updatePreferredDynamicRange]"
- "-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]"
- "-[AVSampleBufferVideoRenderer addSampleBufferDisplayLayer:]"
- "-[AVSampleBufferVideoRenderer addVideoTarget:]"
- "-[AVSampleBufferVideoRenderer createVideoQueue:]"
- "-[AVSampleBufferVideoRenderer enqueueSampleBuffer:]"
- "-[AVSampleBufferVideoRenderer enqueueSampleBuffer:bufferEnqueueingInfo:]"
- "-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]"
- "-[AVSampleBufferVideoRenderer removeDisplayLayer]"
- "-[AVSampleBufferVideoRenderer requestMediaDataWhenReadyOnQueue:usingBlock:]"
- "-[AVSampleBufferVideoRenderer setControlTimebase:]"
- "-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]"
- "-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]_block_invoke"
- "-[AVSampleBufferVideoRenderer setRenderSynchronizer:error:]"
- "-[AVSampleBufferVideoRenderer setSTSLabel:]"
- "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) addOutput:]"
- "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) copyDisplayedPixelBuffer]"
- "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) removeOutput:]"
- "-[AVSampleBufferVideoRenderer(PowerOptimization) expectMinimumUpcomingSampleBufferPresentationTime:]"
- "-[AVSampleCursor createSampleBufferForCurrentSampleReturningError:]"
- "-[AVSampleCursor createSampleBufferFromCurrentSampleToEndCursor:error:]"
- "-[AVSampleCursor stepByDecodeTime:wasPinned:]"
- "-[AVSampleCursor stepByPresentationTime:wasPinned:]"
- "-[AVScheduledAudioParameters initWithPropertyList:]"
- "-[AVScheduledAudioParameters(AVScheduledAudioParameters_Internal) _setRamp:]"
- "-[AVScheduledFloatValueRamp _interpolatedValueAtTime:]"
- "-[AVSinkSubscriber cancel]"
- "-[AVSpecifiedLoggingIdentifier initWithSpecifiedName:]"
- "-[AVStreamDataParser _appendStreamData:withFlags:]"
- "-[AVStreamDataParser _createAssetIfNecessary]"
- "-[AVStreamDataParser dealloc]"
- "-[AVStreamDataParser init]"
- "-[AVStreamDataParser providePendingMediaData]"
- "-[AVStreamDataParser setShouldProvideMediaData:forTrackID:]"
- "-[AVStreamDataParser(AVStreamDataParserSandboxedParsing) setPreferSandboxedParsing:]_block_invoke"
- "-[AVStreamDataParser(AVStreamDataParser_ContentKeySessionDelegate) contentKeySession:didProvideContentKeyRequest:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _createFigManifoldWithBlockBuffer:manifold:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:discoveredNewTrackID:mediaType:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:pushedSampleBuffer:trackID:flags:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:trackDidEnd:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifoldAllNewTracksReady:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _registerForFigManifoldCallbacksForTrackID:]"
- "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _unregisterForFigManifoldCallbacksForTrackID:]"
- "-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke"
- "-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke_2"
- "-[AVTimebaseObserver _finishInitializationWithTimerEventHandler:]"
- "-[AVTrackReaderInspector _initWithAsset:trackID:trackIndex:]"
- "-[AVURLAsset _ensureAssetDownloadCache]_block_invoke"
- "-[AVURLAsset initWithFigCreationOptions:options:figAssetCreationOptions:figAssetCreationFlags:]"
- "-[AVURLAsset initWithURL:options:]"
- "-[AVURLAsset(AVURLAssetContentKeyEligibilityInternal) _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:]"
- "-[AVURLAsset(AVURLAssetURLHandlingInternal) _resourceLoaderWithRemoteHandlerContext:]_block_invoke"
- "-[AVVideoComposition _copyFigVideoCompositor:andSession:recyclingSession:forFigRemaker:error:]"
- "-[AVVideoComposition init]"
- "-[AVVideoCompositionInstruction dictionaryRepresentation]"
- "-[AVVideoCompositionRenderContext newPixelBuffer]_block_invoke"
- "-[AVVideoCompositionRenderContext(Internal) initWithFigVideoCompositor:clientRequiredPixelBufferAttributes:videoComposition:pixelBufferPool:]"
- "-[AVVideoCompositionRenderContext(Internal) pixelBufferPool]"
- "-[AVVideoOutputSpecification setOutputSettings:forTagCollection:]"
- "-[AVWeakReferencingDelegateStorage setDelegate:queue:]"
- "-[AVWeaklyObservedObjectClientBlockKVONotifier cancelCallbacks]"
- "-[AVWeaklyObservedObjectClientBlockKVONotifier start]"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: %@ Setting IsExpanseMediaSession %s on AVAudioSession error %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
- "/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
- "<<<< AVAnnotation >>>> %s: Annotation failed to create formatted date from %@."
- "<<<< AVAnnotation >>>> %s: Failed to create AVAnnotation: %@"
- "<<<< AVAnnotation >>>> %s: Unknown annotation representation type: %@"
- "<<<< AVAnnotation >>>> %s: Unknown annotation representation version %@."
- "<<<< AVAnnotation >>>> %s: Unknown annotation version %@."
- "<<<< AVApplicationStateMonitor >>>> %s: <%@>. isRunning %d, hasForegroundVisibility %d appIsInForeground %d, processIsViewService %d"
- "<<<< AVApplicationStateMonitor >>>> %s: called"
- "<<<< AVAsset >>>> %s: %@ <%p> FigAssetCopyAssetWithDownloadToken for downloadToken %llu returned %d"
- "<<<< AVAsset >>>> %s: %@ Created %p"
- "<<<< AVAsset >>>> %s: %@ Received notification for %@"
- "<<<< AVAsset >>>> %s: %@ creating AVFigAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: %@ failed to create AVFigAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: %@ received ServerStatePurged with identifier 0x%llx"
- "<<<< AVAsset >>>> %s: %s"
- "<<<< AVAsset >>>> %s: *** Could not canonicalize language: %@. ***"
- "<<<< AVAsset >>>> %s: *** MediaValidator.plist was not loaded for this platform! Defaulting to no video support. ***"
- "<<<< AVAsset >>>> %s: <%p> called for property list %@, mediaSelectionOptionOut = <%p>"
- "<<<< AVAsset >>>> %s: <%p> resolved to group %@ and option %@"
- "<<<< AVAsset >>>> %s: AVURLAssetHTTPHeaderFieldsKey must be a dictionary"
- "<<<< AVAsset >>>> %s: Cannot create AVAssetDownloadCache when an AVManagedAssetCache is already present."
- "<<<< AVAsset >>>> %s: _URLAsset->resourceLoader was unexpectedly non-nil"
- "<<<< AVAsset >>>> %s: asset created with AVAssetPrefersSandboxedParsingOptionKey"
- "<<<< AVAsset >>>> %s: asset created with AVAssetRequiresInProcessOperationKey"
- "<<<< AVAsset >>>> %s: creating AVAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: using custom AVAssetInspectorLoader"
- "<<<< AVAssetCache >>>> %s: Enabling AutomaticCacheSizeManagement"
- "<<<< AVAssetCache >>>> %s: Initialized with URL %@"
- "<<<< AVAssetCache >>>> %s: Remove entry with key = %@"
- "<<<< AVAssetCache >>>> %s: Set maxEntrySize = %lld"
- "<<<< AVAssetCache >>>> %s: Set maxSize = %lld"
- "<<<< AVAssetCustomURL >>>> %s: cancelling abandoned AVNSURLProtocolRequest %p"
- "<<<< AVAssetDownloadSession >>>> %s: %p downloaded %lld / %lld"
- "<<<< AVAssetDownloadSession >>>> %s: Failed because server connection died - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Failed to download to destination - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Failed to load property %@ - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Failed to make ready for inspection - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Failed to prime cache - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Failed to start - %@"
- "<<<< AVAssetDownloadSession >>>> %s: Must initialize AVAssetDownloadSession with initWithAsset:destinationURL:options: for streaming assets."
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Called"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Called with %lld"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Called with asset:%@ destinationURL:%@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Download %s"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Download from %@ to %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] FigAssetCreateWithURL for URL <%@> returned %d"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Going from paused to start download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Pause download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Priming cache with download token %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Start download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Stop download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@ payload %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] loaded assetType:[%s] loadingStatus:%d error:%@"
- "<<<< AVAssetDownloadStorageManager >>>> %s: Set storageManagementPolicy %@ for asset at URL %@"
- "<<<< AVAssetDownloadStorageManager >>>> %s: StorageManagementPolicy for asset at URL %@ is  %@ "
- "<<<< AVAssetExportSession >>>> %s: Could not create fig export session. err=%d"
- "<<<< AVAssetExportSession >>>> %s: directoryForTemporaryFiles must be non-nil for this initializer"
- "<<<< AVAssetExportSession >>>> %s: fileLengthLimit: %lld"
- "<<<< AVAssetExportSession >>>> %s: maximize power efficiency %s"
- "<<<< AVAssetExportSession >>>> %s: no asset, no presetName, or no export settings => nil: asset=%@, presetName=%@"
- "<<<< AVAssetExportSession >>>> %s: no export session => nil"
- "<<<< AVAssetExportSession >>>> %s: resumableSessionName must be non-nil for this initializer"
- "<<<< AVAssetImageGenerator >>>> %s: Creating FigAssetImageGenerator from FigAsset"
- "<<<< AVAssetImageGenerator >>>> %s: called"
- "<<<< AVAssetImageGenerator >>>> %s: calling FigAssetImageGeneratorCopyCGImageAtTime time %.3f options %@"
- "<<<< AVAssetImageGenerator >>>> %s: calling FigAssetImageGeneratorRequestCGImageAtTimeAsync time %.3f options %@"
- "<<<< AVAssetImageGenerator >>>> %s: calling handler with cancelled status"
- "<<<< AVAssetImageGenerator >>>> %s: calling handler with error 'mediaserverd died'"
- "<<<< AVAssetImageGenerator >>>> %s: calling handler with failed status, error %@"
- "<<<< AVAssetImageGenerator >>>> %s: calling handler with failed status, error %d"
- "<<<< AVAssetImageGenerator >>>> %s: calling handler with succeeded status, actualTime %.3f"
- "<<<< AVAssetImageGenerator >>>> %s: composition => using AVAssetReader"
- "<<<< AVAssetImageGenerator >>>> %s: no FigAssetImageGenerator instance!"
- "<<<< AVAssetImageGenerator >>>> %s: not a composition => using FigAssetImageGenerator"
- "<<<< AVAssetInspector >>>> %s: %p cannot create AVAssetVariant for %@"
- "<<<< AVAssetInspector >>>> %s: The collection of localized media selection option display names for key \"%@\" has class %@ instead of NSDictionary"
- "<<<< AVAssetInspector >>>> %s: The top-level object for localized media selection option display names has class %@ instead of NSDictionary"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> FigAssetGetStatusOfValueForProperty for property <%@> returned %d and load error %d - %@"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> dispatching completion handler [%p]"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> got notification <%@>"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> got notification <%@> for batchID %@"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> invoking completion handler [%p] immediately"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> loadValuesAsynchronouslyForKeys:%@ keysForCollectionKeys:%@ completionHandler:<%p>"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> loading batch [%p] has count of %d on entry"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> loading batch [%p] has count of %d on exit with %@"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> status requested for key %@ after loading was canceled"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> storing completion handler [%p] for later invocation"
- "<<<< AVAssetInspectorLoader >>>> %s: <%p> storing loading batch [%p] with %@"
- "<<<< AVAssetInspectorLoader >>>> %s: FigAssetCreateWithURL for URL <%@> returned %d"
- "<<<< AVAssetInspectorLoader >>>> %s: Received %@ from %p (payload: %@)"
- "<<<< AVAssetPlanner >>>> %s: Cannot resume from savedSegmentState for segment at index %ld"
- "<<<< AVAssetPlanner >>>> %s: Cannot resume from savedTrackState for track at index %d"
- "<<<< AVAssetPlanner >>>> %s: Found multiple %@ tracks in client written segment file %@. Expect one and only one track"
- "<<<< AVAssetPlanner >>>> %s: SessionName from savedState (%@) does not match current session name (%@)"
- "<<<< AVAssetPlanner >>>> %s: Track count from savedState (%d) does not match current session track count (%d)"
- "<<<< AVAssetPlanner >>>> %s: _requiresVideoCompression (%d) from savedState does not match _requiresVideoCompression (%d) from current state"
- "<<<< AVAssetPlanner >>>> %s: mediaType %@ from savedState does not match current mediaType %@"
- "<<<< AVAssetPlanner >>>> %s: segment count (%ld) from savedState does not match segment count (%ld) in current state"
- "<<<< AVAssetPlanner >>>> %s: segment frameCount from saved state (%ld) does not match current segment's frameCount (%ld)"
- "<<<< AVAssetPlanner >>>> %s: segment time range from saved state (start = %1.3f, duration = %1.3f) does not match current segment time range (start = %1.3f, duration = %1.3f"
- "<<<< AVAssetPlanner >>>> %s: segmentURL from savedState (%@) does not match current segment URL (%@)"
- "<<<< AVAssetPlanner >>>> %s: trackID (%d) from savedState does not match current trackID (%d)"
- "<<<< AVAssetReaderOutput >>>> %s: %p received %@"
- "<<<< AVAssetReaderOutput >>>> %s: %p received %@, extractionID=%d"
- "<<<< AVAssetReaderOutput >>>> %s: FigAssetReader has told us to wait until the sample buffer is ready.  Blocking until we get a notification"
- "<<<< AVAssetReaderOutput >>>> %s: FigAssetReaderExtractAndRetainNextSampleBuffer returned %d, extractionComplete=%d, sampleBuffer=%p, self=%p"
- "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoader delegate does not respond to selector %@"
- "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoaderDelegate for AVAssetResourceLoader %@ is gone"
- "<<<< AVAssetResourceLoader >>>> %s: cached data has grown to length %lld for %@"
- "<<<< AVAssetResourceLoader >>>> %s: caching data for current offset %lld of length %lld that was provided to %@"
- "<<<< AVAssetResourceLoader >>>> %s: called on %@"
- "<<<< AVAssetResourceLoader >>>> %s: called with error %@ on %@"
- "<<<< AVAssetResourceLoader >>>> %s: called with handlingClient: %@, handler: %@, requestInfo: <%p>, requestID %llu"
- "<<<< AVAssetResourceLoader >>>> %s: data for current offset %lld of length %lld provided to %@"
- "<<<< AVAssetResourceLoader >>>> %s: swallowing finishLoading for cancelled request %@"
- "<<<< AVAssetResourceLoader >>>> %s: swallowing sendData with data of len %lu for cancelled request %@"
- "<<<< AVAssetResourceLoader >>>> %s: swallowing sendResponseInfo for cancelled request %@"
- "<<<< AVAssetTrackInspector >>>> %s: Created track inspector of class %@ "
- "<<<< AVAssetTrackInspector >>>> %s: FigAssetTrackGetStatusOfValueForProperty for property <%@> returned %d and load error %d - %@"
- "<<<< AVAssetTrackInspector >>>> %s: FigAssetTrackLoadValuesAsyncForProperties for properties %@ returned %d with loaded == %@ and batchID == %d"
- "<<<< AVAssetTrackInspector >>>> %s: [%p] called"
- "<<<< AVAssetTrackInspector >>>> %s: can't get FigAssetTrack; invalid trackID and negative trackIndex"
- "<<<< AVAssetTrackInspector >>>> %s: can't get FigTrackReader; invalid trackID and negative trackIndex"
- "<<<< AVAssetTrackInspector >>>> %s: dispatching completion handler [%p]"
- "<<<< AVAssetTrackInspector >>>> %s: got notification <%@>"
- "<<<< AVAssetTrackInspector >>>> %s: got notification <%@> for batchID %@"
- "<<<< AVAssetTrackInspector >>>> %s: loading batch [%p] has count of %d on entry"
- "<<<< AVAssetTrackInspector >>>> %s: loading batch [%p] has count of %d on exit with %@"
- "<<<< AVAssetTrackInspector >>>> %s: storing completion handler [%p] for later invocation"
- "<<<< AVAssetTrackInspector >>>> %s: storing loading batch [%p] with %@"
- "<<<< AVAssetWriter >>>> %s: \"Transition to terminal status\" operation invoked"
- "<<<< AVAssetWriter >>>> %s: -[NSFileManager removeItemAtURL:] failed: %s"
- "<<<< AVAssetWriter >>>> %s: AVAssetWriter will use %s FigAssetWriter"
- "<<<< AVAssetWriter >>>> %s: Calling FigAssetWriterFinish"
- "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinish failed: %d"
- "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinishAsync failed: %d"
- "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinishAsync showed cancellation (self=%p)"
- "<<<< AVAssetWriter >>>> %s: Invalidating FigAssetWriter, to ensure that audio files are finalized properly"
- "<<<< AVAssetWriter >>>> %s: No NSError on failure to prepare for writing, input %p"
- "<<<< AVAssetWriter >>>> %s: Storage Space Preallocation Size %lld File System Free Size %lld"
- "<<<< AVAssetWriter >>>> %s: Unexpected terminal status %d"
- "<<<< AVAssetWriter >>>> %s: _figAssetWriter is nil"
- "<<<< AVAssetWriter >>>> %s: attributes is nil with error:%s."
- "<<<< AVAssetWriter >>>> %s: called (self=%p)"
- "<<<< AVAssetWriter >>>> %s: called with payload %@"
- "<<<< AVAssetWriter >>>> %s: called, self=%p"
- "<<<< AVAssetWriter >>>> %s: called, success=%d, error=%@ (self=%p)"
- "<<<< AVAssetWriter >>>> %s: calling FigAssetWriterFinishAsync (self=%p)"
- "<<<< AVAssetWriter >>>> %s: calling completion handler"
- "<<<< AVAssetWriter >>>> %s: freeSizeNum is nil."
- "<<<< AVAssetWriter >>>> %s: freeSizeNum is not NSNumber."
- "<<<< AVAssetWriter >>>> %s: invalid file extension in outputURL"
- "<<<< AVAssetWriterInput >>>> %s: Calling FigAssetWriterEndPass"
- "<<<< AVAssetWriterInput >>>> %s: Client exited request block"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaption: fail with error %@"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaption: return NO due to input already having transitioned to terminal status"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaptionGroup: fail with error %@"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaptionGroup: return NO due to input already having transitioned to terminal status"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendPixelBuffer: fail with error %@"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendPixelBuffer: return NO due to input already having transitioned to terminal status"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendSampleBuffer: fail with error %@"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendSampleBuffer: return NO due to input already having transitioned to terminal status"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendTaggedPixelBufferGroup: fail with error %@"
- "<<<< AVAssetWriterInput >>>> %s: Client will see -appendTaggedPixelBufferGroup: return NO due to input already having transitioned to terminal status"
- "<<<< AVAssetWriterInput >>>> %s: Dispatching request block because previous request block invocation returned before filling the buffer queue or marking input finished (delegate = %@)"
- "<<<< AVAssetWriterInput >>>> %s: Dispatching request block one extra time, to make sure client sees the failure"
- "<<<< AVAssetWriterInput >>>> %s: FigAssetWriterIsTrackQueueAboveHighWaterLevel returned %d (self=%p)"
- "<<<< AVAssetWriterInput >>>> %s: Informing pass description responder to respond to initial pass description"
- "<<<< AVAssetWriterInput >>>> %s: Invoking request block normally"
- "<<<< AVAssetWriterInput >>>> %s: Not responding to initial pass description, per helper %@"
- "<<<< AVAssetWriterInput >>>> %s: Received kFigAssetWriterNotification_PassFinished"
- "<<<< AVAssetWriterInput >>>> %s: Transitioning to terminal status %d (self = %p)"
- "<<<< AVAssetWriterInput >>>> %s: We thought we might want to invoke the request block, but we are not actually going to"
- "<<<< AVAssetWriterInput >>>> %s: called (keyPath=%@, object=%@, change=%@, contect=%p)"
- "<<<< AVAssetWriterInput >>>> %s: called (self = %p)"
- "<<<< AVAssetWriterInput >>>> %s: called (self=%p)"
- "<<<< AVAssetWriterInput >>>> %s: called (self=%p, queue=%p, block=%p)"
- "<<<< AVAssetWriterInput >>>> %s: called (self=%p, trackID=%d)"
- "<<<< AVAssetWriterInput >>>> %s: called, old=%@ new=%@"
- "<<<< AVAssetWriterInput >>>> %s: called, self=%p"
- "<<<< AVAssetWriterInput >>>> %s: did invoke per-pass block (self=%p)"
- "<<<< AVAssetWriterInput >>>> %s: end pass operation succeeded, nextPassDescription=%@"
- "<<<< AVAssetWriterInput >>>> %s: registering for kFigAssetWriterNotification_PassFinished on FigAssetWriter %p"
- "<<<< AVAssetWriterInput >>>> %s: setting kFigFormatWriterTrackProperty_FormatDescriptionArray to %@"
- "<<<< AVAssetWriterInput >>>> %s: unregistering from kFigAssetWriterNotification_PassFinished"
- "<<<< AVAssetWriterInput >>>> %s: will invoke per-pass block (self=%p)"
- "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Error creating metadata item: %@"
- "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Error serializing JSON: %@"
- "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Unrecognized asset writer status %d"
- "<<<< AVAssetWriterInputMetadataAdaptor >>>> %s: Unrecognized asset writer status %d"
- "<<<< AVCallbackContextRegistry >>>> %s: registering observer %p (token %p), new observer count %d (self=%p)"
- "<<<< AVCallbackContextRegistry >>>> %s: unregistering callback context token %p, new observer count %d (self=%p)"
- "<<<< AVCaptionRenderer >>>> %s: *** failed to start renderer ***"
- "<<<< AVCaptionRenderer >>>> %s: <%p> *** FigCaptionCreate() returned %d"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request returned %d caption scenes"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request started"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -renderInContext:atTime: called with bounds equal to CGRectNull"
- "<<<< AVCaptionRenderer >>>> %s: <%p> FigCaptionClient render started"
- "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session returned %d"
- "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session with FigCaptions"
- "<<<< AVCaptionRenderer >>>> %s: <%p> preparing to set session after converting AVCaptions to FigCaptions array"
- "<<<< AVCaptionRenderer >>>> %s: <%p> start setting session with %ld FigCaptions"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientSetTime returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientUpdateCGContext returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: FigCaptionClientStop() returned %d"
- "<<<< AVComposition >>>> %s: AVAsset with nil _absoluteURL and NULL _mutableComposition"
- "<<<< AVComposition >>>> %s: [%p] called"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p asset: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p mediaType: %@ preferredTrackID: %d"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackAssetURL: %@ trackID: %d"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackID: %d"
- "<<<< AVContentKeySession >>>> %s: %@ failed to process content key request for identifier %@ and initialization data %@ due to %@"
- "<<<< AVContentKeySession >>>> %s: %p Ignore produced contentKey (%@) because content key session is expired"
- "<<<< AVContentKeySession >>>> %s: %p creating cryptor using sinfs"
- "<<<< AVContentKeySession >>>> %s: %p failed to issue content key request because delegate's already gone"
- "<<<< AVContentKeySession >>>> %s: %p failed to issue content key request due to an internal error"
- "<<<< AVContentKeySession >>>> %s: %p initializing content key request with identifier %@ and initialization data %@"
- "<<<< AVContentKeySession >>>> %s: Invalid key system used in AVContentKeySystem"
- "<<<< AVContentKeySession >>>> %s: badly formatted key request init data (encoded sinf not UTF8)"
- "<<<< AVContentKeySession >>>> %s: badly formatted key request init data (encoded sinf not base64)"
- "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@"
- "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptKeyIdentifier: %@, updatedPersistentKey: %@"
- "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptorUUID: %@, cryptorRequestID: %llu"
- "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptorUUID: %@, cryptorRequestID: %llu, keyResponseError: %@"
- "<<<< AVContentKeySession >>>> %s: called with handlingClient: %@, handler: %@, requestInfo: %@, requestID %llu"
- "<<<< AVContentKeySession >>>> %s: failed to copy default secure stop manager due to error: %d"
- "<<<< AVContentKeySession >>>> %s: protection status changed to: %ld"
- "<<<< AVContentKeySession >>>> %s: setting authorizationToken failed due to err=%d"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: CIImage %@ (colorSpace %@) already has a CVPixelBuffer %@ (attachments %@)"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with CIImage %@"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with error %@"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with request %@"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: cancelling begin"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: cancelling done"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: rendered CIImage %@ (colorSpace %@) to CVPixelBuffer %@ (attachments %@)"
- "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: source CIImage %@ (colorSpace %@) from CVPixelBuffer %@ (attachments %@)"
- "<<<< AVCustomCompositor >>>> %s: canConformColorOfSourceFrames %d"
- "<<<< AVCustomCompositor >>>> %s: creating instance of \"%@\""
- "<<<< AVCustomCompositor >>>> %s: initializing new render context (videoCompositionDidChange %d"
- "<<<< AVCustomCompositor >>>> %s: render context no longer suitable, need to create a new one"
- "<<<< AVCustomCompositor >>>> %s: src pixel buffer attributes %@"
- "<<<< AVCustomCompositor >>>> %s: videoComposition %p"
- "<<<< AVDelegateUtilities >>>> %s: Dispatching to queue %p"
- "<<<< AVDelegateUtilities >>>> %s: Invoking delegate callback synchronously"
- "<<<< AVDelegateUtilities >>>> %s: called (delegateStorage = %@, expectedDelegateQueue = %p, delegateCallbackBlock = %p)"
- "<<<< AVDelegateUtilities >>>> %s: called (newDelegate=%@, newDelegateQueue=%p"
- "<<<< AVDelegateUtilities >>>> %s: current delegate: %@, current delegate queue: %p"
- "<<<< AVError >>>> %s: Could not load localized description for %@ %ld (%@)"
- "<<<< AVError >>>> %s: Could not load localized description for %@ %ld (%@) (%@)"
- "<<<< AVError >>>> %s: Could not load localized failure reason for %@ %ld (%@)"
- "<<<< AVError >>>> %s: Could not load localized failure reason for %@ %ld (%@) (%@)"
- "<<<< AVError >>>> %s: Could not load localized recovery suggestion for %@ %ld (%@)"
- "<<<< AVError >>>> %s: Could not load localized recovery suggestion or failure reason for %@ %ld (%@)"
- "<<<< AVError >>>> %s: Invalid format string '%@', error %@, %@ %ld (%@)"
- "<<<< AVExternalDevice >>>> %s: Endpoint HID Setting inputMode to %@"
- "<<<< AVExternalDevice >>>> %s: Endpoint HID input mode: %@"
- "<<<< AVExternalDevice >>>> %s: Endpoint capabilities: %@"
- "<<<< AVExternalDevice >>>> %s: Endpoint property '%@' has value: %@"
- "<<<< AVExternalDevice >>>> %s: Endpoint property '%@' not supported"
- "<<<< AVExternalDevice >>>> %s: Endpoint screen IDs: %@"
- "<<<< AVExternalDevice >>>> %s: Failed because server connection died - %@"
- "<<<< AVExternalDevice >>>> %s: Invalid Siri Requested Action: %@"
- "<<<< AVExternalDevice >>>> %s: adding endpointDeviceHID: %@"
- "<<<< AVExternalDevice >>>> %s: called with dictionary %@"
- "<<<< AVExternalDevice >>>> %s: called with externalDevice %p"
- "<<<< AVExternalDevice >>>> %s: called with externalDevice %p client %@ reason %@"
- "<<<< AVExternalDevice >>>> %s: called with externalDevice %p hidDictionary %@"
- "<<<< AVExternalPlaybackMonitor >>>> %s: FigRoutingSessionManagerGetAirPlayVideoActive returned %d (self=%p)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: FigRoutingSessionManagerGetAirPlayVideoPlaying returned %d (self=%p)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: FigRoutingSessionManagerResilientRemoteCopyLongFormVideoManager returned %@"
- "<<<< AVExternalPlaybackMonitor >>>> %s: called"
- "<<<< AVExternalPlaybackMonitor >>>> %s: called (monitor=%p, inNotifyingObject=%p, inNotificationPayload=%@)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: called (self=%p)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: called (self=%p, figRoutingSessionManager=%@)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: returning %@"
- "<<<< AVExternalPlaybackMonitor >>>> %s: returning %@ (self=%p)"
- "<<<< AVExternalPlaybackMonitor >>>> %s: returning %d (self=%p)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Assuming route change with ID %@ corresponds to the route change we just initiated"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Called (notificationName=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@, reason=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVErrorIncorrectPassword, since we do not know whether it was a PIN or password"
- "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVErrorUnknown, since we have no more detailed error information"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (routingContext=%@, configuratorBlock=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, deviceName=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, password=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peer=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peerID=%@)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, rejectOtherConnections=%d)"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because it does not match the expected ID %@"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because we have not yet executed the route change operation"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we already received a route change started notification"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we have not yet executed the route change operation"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring non-terminal route config update reason %@"
- "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring route change ID %@ because it does not match the expected ID %@"
- "<<<< AVFileSystemUtilities >>>> %s: Failed to remove temporary file at %@: %@"
- "<<<< AVKVODispatcher >>>> %s: %p no longer observing %@ with observer %@, for key path %@, and context %p"
- "<<<< AVKVODispatcher >>>> %s: %p observing %@ with observer %@, for key path %@, options %d, and context %p"
- "<<<< AVKVODispatcher >>>> %s: Calling -didChange for %@.%@, in response to second-level property change (self=%p)"
- "<<<< AVKVODispatcher >>>> %s: Calling -willChange for %@.%@, in response to second-level property change (self=%p)"
- "<<<< AVKVODispatcher >>>> %s: Calling -willChange for %@.%@, in response to top-level property change (self=%p)"
- "<<<< AVKVODispatcher >>>> %s: Registering for %@ (self = %@)"
- "<<<< AVKVODispatcher >>>> %s: called (self=%p, keyPath=%@, object=%@, change=%@, context=%p)"
- "<<<< AVKVODispatcher >>>> %s: cancelling second-level observation"
- "<<<< AVLoggingIdentifier >>>> %s: Identifier string is %@"
- "<<<< AVLoggingIdentifier >>>> %s: nil specifiedName"
- "<<<< AVMediaSelectionGroup >>>> %s: *** Could not canonicalize language: %@. ***"
- "<<<< AVMediaSelectionGroup >>>> %s: <%p> called with property list %@"
- "<<<< AVMediaSelectionGroup >>>> %s: <%p> resolved to option %@"
- "<<<< AVMediaSelectionGroup >>>> %s: Invalid format string '%@', error %@"
- "<<<< AVMediaStatePurge >>>> %s: object=%@ identifier=%@, skip sending AVMediaStateWasPurgedNotification"
- "<<<< AVMetadataItem >>>> %s: *** Could not canonicalize language: %@. ***"
- "<<<< AVMetadataItem >>>> %s: <%p> completed asynchronous loading of lazily-loaded metadata value"
- "<<<< AVMetadataItem >>>> %s: <%p> initiating asynchronous loading of lazily-loaded metadata value"
- "<<<< AVMetadataItem >>>> %s: Identifier value %@ must be an instance of NSString"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_ConformingDataTypes must be an instance of NSArray"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DataLength must be an instance of NSNumber"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DataTypeNamespace must be an instance of NSString"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Date must be an instance of NSDate"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DiscoveryTimestamp must be an instance of NSDate"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Duration must be an instance of CFDictionary"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_ExtendedLanguageTag must be an instance of NSString"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Key must conform to NSObject and NSCopying"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Keyspace must be an instance of NSString"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_LanguageCode must be an instance of NSString or of NSNumber"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Locale must be an instance of NSLocale"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_PreferredStorageLocation must be an instance of NSString"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Timestamp must be an instance of CFDictionary"
- "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Value must be CMBoxedMetadata or conform to NSObject and NSCopying"
- "<<<< AVMetadataItem >>>> %s: Value %p does not conform to NSObject and/or NSCopying"
- "<<<< AVMetadataItem >>>> %s: key not found %@"
- "<<<< AVMetadataItem >>>> %s: keyspace not found %@"
- "<<<< AVMovie >>>> %s: AVMovie %p, AVAssetInspectorLoader %p"
- "<<<< AVMovie >>>> %s: AVMutableMovie %p failed initialization with error %@"
- "<<<< AVMovie >>>> %s: AVMutableMovie %p, FigMutableMovie %p, FigAsset %p, FigFormatReader %p"
- "<<<< AVMovie >>>> %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
- "<<<< AVOperation >>>> %s: Client block cancelled with status %d (self=%p)"
- "<<<< AVOperation >>>> %s: Got unrecognized status %d"
- "<<<< AVOperation >>>> %s: Ignoring attempt to cancel before execution has begun.  The expectation is that the implementation will notice the cancelled state as part of normal execution"
- "<<<< AVOperation >>>> %s: advancing status from %d to %d (self=%p)"
- "<<<< AVOperation >>>> %s: already cancelled (self=%p)"
- "<<<< AVOperation >>>> %s: called (self=%@)"
- "<<<< AVOperation >>>> %s: called (self=%@, error=%@)"
- "<<<< AVOperation >>>> %s: called (self=%p)"
- "<<<< AVOperation >>>> %s: called (self=%p, name=%@)"
- "<<<< AVOperation >>>> %s: ignoring attempt to move from terminal status %d to status %d"
- "<<<< AVOperation >>>> %s: marking as cancelled due to cancellation of dependency (self=%@)"
- "<<<< AVOperation >>>> %s: marking as failed due to previous failure in dependency (self=%@)"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ all playback coordinators %s suspended for reason %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ broadcasting participant state dictionary %@ received from coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ broadcasting transport control state dictionary %@ for item identifier %@ received from coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ connect playback coordinator %@ to coordination medium"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ current transport control state dictionary %@ for item identifier %@ for coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ disconnect playback coordinator with identifier %@ from coordination medium"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ ending suspensions with reason %@ on all playback coordinators"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has equal lamport timestamp %@ from originator with larger UUID. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has higher lamport timestamp %@. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has lower lamport timestamp %@. should NOT update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ no existing transport control state. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ reloading transport control state dictionary %@ for item identifier %@ for coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ setting coordinator %@, participant %@ as initiator for identifer %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ signalling condition for item identifier %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ skipping update to transport control state %@ for item identifier %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ updating lowest in-use item identifier to %d"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ updating transport control state for item identifier %@ from %@ to %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ waiting for initiator to send transport control state for identifer %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ waiting to satisfy condition for identifier %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ updating transport control state cache for item identifier %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Converted to media time: original time %f, adjusted media time %f, host time adjustment (%f-%f)"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new control state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new participant state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle replacement participant state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator skipping updating control states."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator updating %d control states."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Posting AVPlaybackCoordinatorItemIdentifierForCoordinatedPlaybackDidChangeNotification in response to coordination medium change"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Posting AVPlaybackCoordinatorItemIdentifierForCoordinatedPlaybackDidChangeNotification in response to delegate change"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Setting IsExpanseMediaSession %s on AVAudioSession error %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Setting integrated timeline"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ beginning suspension with reason %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ caching group timeline reset"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ current pending seek id %d, seek time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p proposing new time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension with reason %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline only contains primary segment. Bypassing integrated seek to %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline seek at %f current time at %f, applied : %d"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ interstitial is active : %d"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ playback coordinator is suspended. Skipping seek to %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ resetting group timeline expectation"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator with UUID %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator, but NULL figPlaybackCoordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting waiting policies %@ on playback coordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ suspension reason %@ has been removed"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ update based on suspension reason changes from current %@ to new %@"
- "<<<< AVPlaybackCoordinator >>>> %s: <AVPlaybackCoordinator: %@> failed to dispatch work async onto player queue with err: %d, synchronizing locally"
- "<<<< AVPlaybackCoordinator >>>> %s: Could not create FigTimelineCoordinatorSuspensionRef"
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator gave a participantID which is not present in otherParticipants"
- "<<<< AVPlaybackCoordinator >>>> %s: States aren't distinguishable. Assuming state from the outside is better."
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for DidIssueCommandToFigPlayer notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "<<<< AVPlayer >>>> %s: %@ (self = %p) (layer = %p)"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) Adding coordinated playback suspension with reason %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) Pausing item since cannot transition to background _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) Removing coordinated playback suspension with reason %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) attach video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) issue _reevaluateVideoLayersAndTargetsForPresentationState w/ DetachAllOutputs _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d, _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) not updating video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip _reevaluateVideoLayersAndTargetsForPresentationState  _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip attach video layers _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) w/ DetachLayersKeepingVideoTargetsAttached _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: has no layers or no figPlayer. Nothing to attach/detach for iapd"
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer do hold. Attaching."
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer don't hold. Detaching."
- "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) and its closedCaptionLayer(%p)"
- "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) is adding videoLayer(%p), closedCaptionLayer(%p), and subtitleLayer(%p) sublayers"
- "<<<< AVPlayer >>>> %s: %@ Did update status to %d (self=%p)"
- "<<<< AVPlayer >>>> %s: %@ Dispatching FigPlayer copy property block (self=%p) to a background queue if necessary"
- "<<<< AVPlayer >>>> %s: %@ Extended mode is active"
- "<<<< AVPlayer >>>> %s: %@ Host application is in foreground with foreground video output"
- "<<<< AVPlayer >>>> %s: %@ NULL FigPlayerInterstitialCoordinator"
- "<<<< AVPlayer >>>> %s: %@ New current item: %@ %@ (self = %@)"
- "<<<< AVPlayer >>>> %s: %@ PIP mode is active"
- "<<<< AVPlayer >>>> %s: %@ Should Detach: [%@]"
- "<<<< AVPlayer >>>> %s: %@ Trying to set picker id : %@"
- "<<<< AVPlayer >>>> %s: %@ Under device lock and has external display active"
- "<<<< AVPlayer >>>> %s: %@ Will update status (self=%p)"
- "<<<< AVPlayer >>>> %s: %@ _setUsesLegacyAutomaticWaitingBehavior: %s"
- "<<<< AVPlayer >>>> %s: %@ called (self = %@)"
- "<<<< AVPlayer >>>> %s: %@ called (self = %@, inNotificationName = %@)"
- "<<<< AVPlayer >>>> %s: %@ called (self = %@, inNotificationName = %@, inNotificationPayload = %@)"
- "<<<< AVPlayer >>>> %s: %@ called (self = %@, notification = %@)"
- "<<<< AVPlayer >>>> %s: %@ called (self = %p, new current item = %@)"
- "<<<< AVPlayer >>>> %s: %@ called (self = <%p>, time observer = <%p>)"
- "<<<< AVPlayer >>>> %s: %@ called (self=%p)"
- "<<<< AVPlayer >>>> %s: %@ called. Rate changed from [%f] -> [%f], changed because %s\n%@"
- "<<<< AVPlayer >>>> %s: %@ called. Set rate to 1.0 because %s\n%@"
- "<<<< AVPlayer >>>> %s: %@ called. oldReason %@ newReason %@ for timeControlStatus %d to %d"
- "<<<< AVPlayer >>>> %s: %@ called. set to [%f]"
- "<<<< AVPlayer >>>> %s: %@ cannot copy displayed pixel buffer, figPlayer is NULL"
- "<<<< AVPlayer >>>> %s: %@ current interstitial event %@"
- "<<<< AVPlayer >>>> %s: %@ dispatched (self = %@, inNotificationName = %@)"
- "<<<< AVPlayer >>>> %s: %@ dispatching (self = %p)"
- "<<<< AVPlayer >>>> %s: %@ failed to copy currently displayed pixel buffer although no error"
- "<<<< AVPlayer >>>> %s: %@ failed to take background assertion with err %@"
- "<<<< AVPlayer >>>> %s: %@ got background assertion"
- "<<<< AVPlayer >>>> %s: %@ has foreground layers, attaching video objects"
- "<<<< AVPlayer >>>> %s: %@ has no more foreground video objects left, detaching video layers"
- "<<<< AVPlayer >>>> %s: %@ inferred time control status: %d (waiting reason: %@)"
- "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_CurrentItemDidChange (self = %@, FigPlaybackItem = %p"
- "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_CurrentItemDidChange due to AddTo/RemoveFrom-PlayQueue. No need to advance current item to match Fig"
- "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_MutedDidChange (self = %@ value [%d])"
- "<<<< AVPlayer >>>> %s: %@ kFigPlayerProperty_PlaybackState is %@"
- "<<<< AVPlayer >>>> %s: %@ maximumLayerDisplaySize = %@ (self = %p)"
- "<<<< AVPlayer >>>> %s: %@ not updating video layers, despite adding layer %p (self=%@)"
- "<<<< AVPlayer >>>> %s: %@ player <%p> failed to create fig sub item (error: %@)"
- "<<<< AVPlayer >>>> %s: %@ received %@ (payload: %@)"
- "<<<< AVPlayer >>>> %s: %@ received ServerStatePurged with identifier 0x%llx"
- "<<<< AVPlayer >>>> %s: %@ received updated %@. Rate changed from [%f] -> [%f], changed because %s\n%@"
- "<<<< AVPlayer >>>> %s: %@ releasing background assertion after finishing suspension"
- "<<<< AVPlayer >>>> %s: %@ removed %@ %@, now have %@"
- "<<<< AVPlayer >>>> %s: %@ setting from %d to %d"
- "<<<< AVPlayer >>>> %s: %@ setting rate to %f"
- "<<<< AVPlayer >>>> %s: %@ setting to %d"
- "<<<< AVPlayer >>>> %s: %@ setting up FigPlayer <%p>"
- "<<<< AVPlayer >>>> %s: %@ updating video layers due to adding layer %p (self=%@)"
- "<<<< AVPlayer >>>> %s: %@: isConnectedToPhysicalSecondScreen changed %d"
- "<<<< AVPlayer >>>> %s: %p %@. NO since Buffered AirPlay is active and it does not support speed ramps"
- "<<<< AVPlayer >>>> %s: %p %@. NO since supportsSpeedRamps is NO"
- "<<<< AVPlayer >>>> %s: %p %@. YES"
- "<<<< AVPlayer >>>> %s: %s"
- "<<<< AVPlayer >>>> %s: (%p) nil videoLayer for playerLayer %p, cannot update pixel buffer attributes"
- "<<<< AVPlayer >>>> %s: <%p|%@> attached video layer array with %lu layers on FigPlayer"
- "<<<< AVPlayer >>>> %s: <%p|%@> attaching videoTargets (%@) for presentationStateChange: %d"
- "<<<< AVPlayer >>>> %s: <%p|%@> detached video targets and layers from FigPlayer"
- "<<<< AVPlayer >>>> %s: AVPlayer %@ setShouldWaitForVideoTarget to %d"
- "<<<< AVPlayer >>>> %s: Cannot add NULL videoTarget"
- "<<<< AVPlayer >>>> %s: Directly set kFigPlayerProperty_ShouldWaitForVideoTarget on FigPlayer %@"
- "<<<< AVPlayer >>>> %s: Dispatching FigPlayer configuration block (self=%p) to state dispatch queue"
- "<<<< AVPlayer >>>> %s: Error inserting item: %@"
- "<<<< AVPlayer >>>> %s: Error replacing current item: %@"
- "<<<< AVPlayer >>>> %s: Failed adding playback item of %@ to play queue immediately (self = %@), will remove item"
- "<<<< AVPlayer >>>> %s: Found non-LCD CAContext so externally displayed"
- "<<<< AVPlayer >>>> %s: Handling removal of item %@ (self = %@)"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as an associated AVPlayerLayer is in PIP mode"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ CarPlay is active ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ IAP extended mode is active ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ MMP SPI says so ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ No associated video layers ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ No enabled video ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ Under device lock and playing to external display ]"
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background reason: [ policy set to %d ] "
- "<<<< AVPlayer >>>> %s: Item <%@ %@> can continue to play with Player <%@ %@> as the application transitions to background: %d"
- "<<<< AVPlayer >>>> %s: Item <%@ %p> Pausing since cannot transition to background"
- "<<<< AVPlayer >>>> %s: Item <%@ %p> Unable to evaluate if okay to play while transition to background. Will reevaluate when ReadyToPlay"
- "<<<< AVPlayer >>>> %s: Item <%p> Now ReadyToPlay. Reevaluating if okay to play while transition to background."
- "<<<< AVPlayer >>>> %s: Item <%p> Reevaluation complete. Not okay to play while transition to background. Pausing."
- "<<<< AVPlayer >>>> %s: No figPlayer found, cannot set picker id"
- "<<<< AVPlayer >>>> %s: Not suspended under lock"
- "<<<< AVPlayer >>>> %s: Obtaining volume for category [%@]"
- "<<<< AVPlayer >>>> %s: Player <%@ %@> audiovisual background policy set to Automatic, use coordinator other participant count %d, connected to local medium %d to decide"
- "<<<< AVPlayer >>>> %s: Player <%@ %@> audiovisual background policy set to ContinuesIfPossible"
- "<<<< AVPlayer >>>> %s: Player <%@ %@> audiovisual background policy set to Pauses"
- "<<<< AVPlayer >>>> %s: Player role %@ set synchronously before we had a fig player."
- "<<<< AVPlayer >>>> %s: Posting AVPlayerAudiovisualBackgroundPlaybackPolicyDidChangeNotification for policy change"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerAvailableHDRModesDidChangeNotification"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerBackgroundPIPAuthorizationTokenDidChangeNotification for token change"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerCurrentItemDidChangeNotification with reason %@"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerEligibleForHDRPlaybackDidChangeNotification"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerInterstitialPlayerDidChangeNotification"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerPlaybackWasInterruptedNotification"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerRateDidChangeNotification for status change"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerRateDidChangeNotification with payload %@"
- "<<<< AVPlayer >>>> %s: Posting _AVPlayer_VolumeDidChangeNotification with payload %@"
- "<<<< AVPlayer >>>> %s: Returning hasAVPlayerLayerInPIPMode: %s"
- "<<<< AVPlayer >>>> %s: Set ShouldWaitForVideoTarget as creation option or right after creation of player %@"
- "<<<< AVPlayer >>>> %s: The FigPlaybackItem that posted ItemBecameCurrent has already been removed from the queue; fall back to identifying the current item using FigPlayerCopyPlayQueueItem"
- "<<<< AVPlayer >>>> %s: Unrecognized player role %@"
- "<<<< AVPlayer >>>> %s: availableHDRModes returning %d"
- "<<<< AVPlayer >>>> %s: called"
- "<<<< AVPlayer >>>> %s: called (asset=%p)"
- "<<<< AVPlayer >>>> %s: called on <%@>. Setting attributes on decoder to:\n\t<%@>"
- "<<<< AVPlayer >>>> %s: closedCaptionLayers array snapshot:%@"
- "<<<< AVPlayer >>>> %s: connect fig playback coordinator"
- "<<<< AVPlayer >>>> %s: current event %@ %f"
- "<<<< AVPlayer >>>> %s: dispatching call to -_applyPlayQueueChangesToFigPlayerWithCompletionHandler: (self=%p)"
- "<<<< AVPlayer >>>> %s: expected 'CurrentIsBufferedAirPlayActive' in notification payload"
- "<<<< AVPlayer >>>> %s: fig playback coordinator already connected clientRequested"
- "<<<< AVPlayer >>>> %s: figplayer creation failed [%d]"
- "<<<< AVPlayer >>>> %s: interstitial is active %d"
- "<<<< AVPlayer >>>> %s: isExternalPlaybackActive is YES"
- "<<<< AVPlayer >>>> %s: now have %@"
- "<<<< AVPlayer >>>> %s: removed current item, now have %@"
- "<<<< AVPlayer >>>> %s: replaced local interstitialEventCoordinator %p with remote %p"
- "<<<< AVPlayer >>>> %s: sawFileType = %d, sawStreamingType = %d"
- "<<<< AVPlayer >>>> %s: scheduling _didFinishSuspension block"
- "<<<< AVPlayer >>>> %s: seekToDate called without any attached item"
- "<<<< AVPlayer >>>> %s: seekToTime called without any attached item"
- "<<<< AVPlayer >>>> %s: setExpectedAssetTypes %@"
- "<<<< AVPlayer >>>> %s: setting to %@"
- "<<<< AVPlayer >>>> %s: skipping _didFinishSuspension, invalidating assertion immediately"
- "<<<< AVPlayer >>>> %s: synthesizing _didFinishSuspension notification"
- "<<<< AVPlayer >>>> %s: underlying FigPlayer did neither implement SetRateWithOptions nor SetRateWithFade. Fall back to SetRate"
- "<<<< AVPlayer >>>> %s: underlying FigPlayer did not implement SetRateWithOptions. Fall back to SetRateWithFade"
- "<<<< AVPlayer >>>> %s: video layers are still attached"
- "<<<< AVPlayer >>>> %s: videoLayers array snapshot:%@"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> %@ closed caption layer"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Did cancel all observation of old player"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Observing isDisplayingClosedCaptions on player %p"
- "<<<< AVPlayerCaptionLayer >>>> %s: Called (self=%p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: Called (self=%p, bounds=%@)"
- "<<<< AVPlayerCaptionLayer >>>> %s: Setting interstitialLayer %p visibility to %d and primary (subtitle/closedcaption) layer %p/%p visibility to %d"
- "<<<< AVPlayerCaptionLayer >>>> %s: Setting legibleContentInsets received from client. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerCaptionLayer >>>> %s: Updated CC bounds with cached legibleContentInsets. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerCaptionLayer >>>> %s: _subtitleLayer(%p) clear"
- "<<<< AVPlayerCaptionLayer >>>> %s: called (keyPath=%@, object=%@, change=%@, context=%p"
- "<<<< AVPlayerCaptionLayer >>>> %s: called (keyPath=%@, value=%@"
- "<<<< AVPlayerCaptionLayer >>>> %s: creating interstitialLayer %p for primary playerCaptionLayer %p"
- "<<<< AVPlayerCaptionLayer >>>> %s: old player=%p, new player=%p"
- "<<<< AVPlayerInterstitialEventMonitor >>>> %s:  Unrecognized notification: %@"
- "<<<< AVPlayerItem >>>> %s:  %@: set video composition properties: %@"
- "<<<< AVPlayerItem >>>> %s: %@ <%p> returning %@"
- "<<<< AVPlayerItem >>>> %s: %@ <%p> with asset <%p> called for media selection group %@"
- "<<<< AVPlayerItem >>>> %s: %@ <%p> with asset <%p> called for media selection option %@ in group %@"
- "<<<< AVPlayerItem >>>> %s: %@ AVPlayerItem <%p> created with asset at URL [%@], automatically loaded asset keys %@"
- "<<<< AVPlayerItem >>>> %s: %@ Adding playback item of %p to play queue immediately (player = %@)"
- "<<<< AVPlayerItem >>>> %s: %@ CPEProtector already ready"
- "<<<< AVPlayerItem >>>> %s: %@ Chosen tracks changed"
- "<<<< AVPlayerItem >>>> %s: %@ CurrentSelectedMediaArray not in payload or nil."
- "<<<< AVPlayerItem >>>> %s: %@ Display non-forced subtitles changed"
- "<<<< AVPlayerItem >>>> %s: %@ ExternalProtectionRequiredForPlayback changed"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> became the FigPlayer's current item"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> reached timeToPauseBuffering"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> reached timeToPausePlayback"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> stopped being the FigPlayer's current item"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> was removed from the FigPlayer's item queue"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSeekToDate() failed for initial date"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSeekToDateWithID() failed"
- "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSetProperty() failed with %d for initial estimated date"
- "<<<< AVPlayerItem >>>> %s: %@ Ignore nil/empty audioProcessingEffects"
- "<<<< AVPlayerItem >>>> %s: %@ Item <%p> Seek to time %1.3f with tolerance <%1.3f, %1.3f>"
- "<<<< AVPlayerItem >>>> %s: %@ Item <%p> avoided synchronous FigAsset/FigAssetTrack property fetch while formulating currentMediaSelection"
- "<<<< AVPlayerItem >>>> %s: %@ Item <%p> is fetching TrackIDArray"
- "<<<< AVPlayerItem >>>> %s: %@ Item <%p> is fetching its dimensions"
- "<<<< AVPlayerItem >>>> %s: %@ NewRecommendedTimeOffsetFromLive: %@"
- "<<<< AVPlayerItem >>>> %s: %@ Requesting automatic loading of FigAsset properties %@"
- "<<<< AVPlayerItem >>>> %s: %@ Requesting automatic loading of FigAssetTrack properties %@"
- "<<<< AVPlayerItem >>>> %s: %@ Using seek ID %d"
- "<<<< AVPlayerItem >>>> %s: %@ alternate stream changed"
- "<<<< AVPlayerItem >>>> %s: %@ basics already ready"
- "<<<< AVPlayerItem >>>> %s: %@ called (self = %p)"
- "<<<< AVPlayerItem >>>> %s: %@ called (self = %p) attaching player %p weak ref %p"
- "<<<< AVPlayerItem >>>> %s: %@ called (self = %p) to invoke %d handlers"
- "<<<< AVPlayerItem >>>> %s: %@ called (self=%p, option=%@, group=%@)"
- "<<<< AVPlayerItem >>>> %s: %@ dimensions changed to %@"
- "<<<< AVPlayerItem >>>> %s: %@ initialSamples already ready"
- "<<<< AVPlayerItem >>>> %s: %@ item (self = %p) already attached to a different player, new weak ref %p old weak ref %p"
- "<<<< AVPlayerItem >>>> %s: %@ item (self = %p) already attached to same player, new weak ref %p old weak ref %p"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> AllowedSpatialization changed"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> SpatialAudioRenderingChange: %@"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> SpatialAudioRenderingChange: default, no payload"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> failed to become ready for %@ (error: %@)"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> failed to create fig sub item (error: %@)"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasEnabledAudio changed"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasEnabledVideo changed"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasVideo changed to YES"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> ready for inspection of %@"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> ready for playback"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> set can and step flags"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> status changing to AVPlayerItemStatusFailed with error %@"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> status changing to AVPlayerItemStatusReadyToPlay"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> updateStatusToReadyToPlay:%d"
- "<<<< AVPlayerItem >>>> %s: %@ item <%p> updateStatusToReadyToPlay:%d complete"
- "<<<< AVPlayerItem >>>> %s: %@ item selected media options changed"
- "<<<< AVPlayerItem >>>> %s: %@ loaded ranges changed"
- "<<<< AVPlayerItem >>>> %s: %@ playback buffer Full: NO"
- "<<<< AVPlayerItem >>>> %s: %@ playback buffer empty: NO"
- "<<<< AVPlayerItem >>>> %s: %@ playback stalled"
- "<<<< AVPlayerItem >>>> %s: %@ received ServerStatePurged with identifier 0x%llx"
- "<<<< AVPlayerItem >>>> %s: %@ reset cinematicAudioEffectParameters"
- "<<<< AVPlayerItem >>>> %s: %@ reset sweepFilterConfiguration"
- "<<<< AVPlayerItem >>>> %s: %@ seekable ranges changed"
- "<<<< AVPlayerItem >>>> %s: %@ setting video composition instructions to %@"
- "<<<< AVPlayerItem >>>> %s: %@ stream buffer empty: YES"
- "<<<< AVPlayerItem >>>> %s: %@ stream buffer full: YES"
- "<<<< AVPlayerItem >>>> %s: %@ stream likely to keep up: NO"
- "<<<< AVPlayerItem >>>> %s: %@ stream likely to keep up: YES"
- "<<<< AVPlayerItem >>>> %s: %{public}@ advanceTime %.3f"
- "<<<< AVPlayerItem >>>> %s: %{public}@ tracks changed, %@, %@"
- "<<<< AVPlayerItem >>>> %s: Calling FigPlayerAddToPlayQueue (item = %@ %@, previous item = %@ %@, FigPlaybackItem = %p)"
- "<<<< AVPlayerItem >>>> %s: Copying completion handler for later invocation in response to readiness notifications"
- "<<<< AVPlayerItem >>>> %s: Either everything necessary is already ready, or making it all ready has failed"
- "<<<< AVPlayerItem >>>> %s: Failed to allocate videoCompositionProperties"
- "<<<< AVPlayerItem >>>> %s: Failed to set kFigPlaybackItemProperty_MetadataOutputsDictionary"
- "<<<< AVPlayerItem >>>> %s: Invoking completion handler for cancelled seek %d"
- "<<<< AVPlayerItem >>>> %s: Invoking seek completion handler for seek id %d"
- "<<<< AVPlayerItem >>>> %s: Neither applied nor cached media option. Selection will be discarded."
- "<<<< AVPlayerItem >>>> %s: Not calling FigPlayerAddToPlayQueue because item's status is the failure status (item = %@ %@, previous item = %@ %@, FigPlaybackItem = %p)"
- "<<<< AVPlayerItem >>>> %s: Posting %@ for seekID %d"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemDidPlayToEndTimeNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemFailedToPlayToEndTimeNotification with error %@"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemMediaSelectionDidChangeNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemNewAccessLogEntryNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemNewErrorLogEntryNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemPlaybackStalledNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimeJumpedNotification"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimeJumpedNotification for seek with originator"
- "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimebaseChangedNotification"
- "<<<< AVPlayerItem >>>> %s: Unknown AVAudioMixEffectParameters type."
- "<<<< AVPlayerItem >>>> %s: Video Enhancement mode is not valid"
- "<<<< AVPlayerItem >>>> %s: We have neither a FigAsset, URL, nor FigFormatReader, so cannot create a FigPlaybackItem"
- "<<<< AVPlayerItem >>>> %s: can't create looping timebase! item will not loop."
- "<<<< AVPlayerItem >>>> %s: self %@: setting interstitial time ranges to %@"
- "<<<< AVPlayerItemLegibleOutput >>>> %s: Invoking legible delegate %p with %d attributed string(s) and %d native sample(s) at time %f:%@"
- "<<<< AVPlayerItemLegibleOutput >>>> %s: Notifying delegate of a flush"
- "<<<< AVPlayerItemLegibleOutput >>>> %s: called"
- "<<<< AVPlayerItemMetadataOutput >>>> %s: Invoking metadata delegate %p with %@ dictionary from %@ item track"
- "<<<< AVPlayerItemMetadataOutput >>>> %s: Notifying delegate of a flush"
- "<<<< AVPlayerItemMetadataOutput >>>> %s: metadata output flushed"
- "<<<< AVPlayerItemOutput >>>> %s:  Error: requestNotificationOfMediaDataChangeAsSoonAsPossible was valid when requesting requestNotificationOfMediaDataChangeWithAdvanceInterval. requestNotificationOfMediaDataChangeAsSoonAsPossible has been deactivated"
- "<<<< AVPlayerItemOutput >>>> %s:  Error: requestNotificationOfMediaDataChangeWithAdvanceInterval was valid when requesting requestNotificationOfMediaDataChangeAsSoonAsPossible. requestNotificationOfMediaDataChangeWithAdvanceInterval is deactivated"
- "<<<< AVPlayerItemOutput >>>> %s: Dispatching -outputSequenceWasFlushed:"
- "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextCopyImageForTime did not provide a imageOriginalTimeOut value. Bailing."
- "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextCreate failed: %d"
- "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextSetImageAvailableSequentialCallback failed: %d"
- "<<<< AVPlayerItemOutput >>>> %s: Sending -outputMediaDataWillChange: to delegate"
- "<<<< AVPlayerItemOutput >>>> %s: Sending -outputSequenceWasFlushed: to delegate"
- "<<<< AVPlayerItemOutput >>>> %s: Unable to convert host time stamp to item time. Client sees kCMTimeInvalid."
- "<<<< AVPlayerItemOutput >>>> %s: Unable to copy next image from visual context. Bailing."
- "<<<< AVPlayerItemOutput >>>> %s: scheduled wakeup for now"
- "<<<< AVPlayerItemOutput >>>> %s: scheduled wakeup in %.3f s"
- "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: Invoking rendered legible delegate %p with %d caption image(s) at time %f"
- "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: Notifying delegate of a flush"
- "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: called"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p received %@, extractionID=%d"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p: wrong trackID %d (right trackID is %d)"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputMediaDataAvailable:trackID:"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputSequenceWasFlushed:trackID:"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: FigPlaybackItemExtractAndRetainNextSampleBuffer returned %d, sampleBuffer=%p, self=%p"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: No delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputMediaDataAvailable:trackID: to delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputSequenceWasFlushed:trackID: to delegate"
- "<<<< AVPlayerItemTrack >>>> %s: attached output %@ with extractionID %d"
- "<<<< AVPlayerItemTrack >>>> %s: removed output %@"
- "<<<< AVPlayerLayer >>>> %s:  <%p> Hiding video layer since the presentation size for player %p is 0x0"
- "<<<< AVPlayerLayer >>>> %s: %@ AVPlayerLayer's net flip status does match CoreAnimation default"
- "<<<< AVPlayerLayer >>>> %s: %@ AVPlayerLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
- "<<<< AVPlayerLayer >>>> %s: %@ _updatePreferredDynamicRange(%@) withAnimation(%@)"
- "<<<< AVPlayerLayer >>>> %s: %@ already in PIP mode but will use %p instead of %p"
- "<<<< AVPlayerLayer >>>> %s: %@ became PIP'ed"
- "<<<< AVPlayerLayer >>>> %s: %@ commence player <%p> observation"
- "<<<< AVPlayerLayer >>>> %s: %@ entering PIP mode using %p"
- "<<<< AVPlayerLayer >>>> %s: %@ entering second screen mode using %p"
- "<<<< AVPlayerLayer >>>> %s: %@ frame is { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: %@ leaving PIP mode"
- "<<<< AVPlayerLayer >>>> %s: %@ leaving second screen mode"
- "<<<< AVPlayerLayer >>>> %s: %@ left PIP mode"
- "<<<< AVPlayerLayer >>>> %s: %@ left second screen mode"
- "<<<< AVPlayerLayer >>>> %s: %@ resign player <%p> observation over currentItem.presentationSize"
- "<<<< AVPlayerLayer >>>> %s: %@ setting player to <%p> forPIP:%d"
- "<<<< AVPlayerLayer >>>> %s: %@ setting self on player <%p>"
- "<<<< AVPlayerLayer >>>> %s: %@ showing interstitial layer [%@], call interstitialLayer copyDisplayedPixelBuffer"
- "<<<< AVPlayerLayer >>>> %s: %@ visibility became NO"
- "<<<< AVPlayerLayer >>>> %s: %@ visibility became YES"
- "<<<< AVPlayerLayer >>>> %s: %p check should notify player _playerLayer->lastWindowSceneEvent > None (%d), isVisible (%d), _isPartOfForegroundScene (%d)"
- "<<<< AVPlayerLayer >>>> %s: %p got window scene in state %ld"
- "<<<< AVPlayerLayer >>>> %s: %p notifying player %p about new display size %@"
- "<<<< AVPlayerLayer >>>> %s: %p skip notifying player as isVisible (%d) !=  _isPartOfForegroundScene"
- "<<<< AVPlayerLayer >>>> %s: (%p) called  IsReadyForDisplayDidChange videoLayer %@"
- "<<<< AVPlayerLayer >>>> %s: (%p) called PresentationSizeDidChange videoLayer %@"
- "<<<< AVPlayerLayer >>>> %s: (%p) called w/ videoLayer %@, videoReceiver %p"
- "<<<< AVPlayerLayer >>>> %s: (%p) either NULL player or videoLayer, returning CGSizeZero"
- "<<<< AVPlayerLayer >>>> %s: (%p) presentationSize={ .width=%.3f, .height=%.3f }"
- "<<<< AVPlayerLayer >>>> %s: <%p> %@ closed caption layer"
- "<<<< AVPlayerLayer >>>> %s: <%p> Did cancel all observation of old player"
- "<<<< AVPlayerLayer >>>> %s: <%p> Hiding video layer since the presentation size is 0x0"
- "<<<< AVPlayerLayer >>>> %s: <%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerLayer >>>> %s: <%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerLayer >>>> %s: <%p> Regardless of the state of PIP the layer is in, removeFromSuperLayer is always allowed"
- "<<<< AVPlayerLayer >>>> %s: <%p> Restoring client layer %@ with indexPath %@"
- "<<<< AVPlayerLayer >>>> %s: <%p> Setting closed caption layer bounds to %@"
- "<<<< AVPlayerLayer >>>> %s: <%p> Unhiding video layer since the presentation size for player %p is { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: <%p> Using box filter downscale"
- "<<<< AVPlayerLayer >>>> %s: <%p> called"
- "<<<< AVPlayerLayer >>>> %s: <%p> finished"
- "<<<< AVPlayerLayer >>>> %s: <%p> layer active state changed to %d"
- "<<<< AVPlayerLayer >>>> %s: <%p> return default based on last window scene event %d"
- "<<<< AVPlayerLayer >>>> %s: <%p> setting new sublayers: videoLayer(%p), closedCaptionLayer(%p), subtitleLayer(%p), interstitialLayers = %@"
- "<<<< AVPlayerLayer >>>> %s: <%p> size needs no update using cached value { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: <%p> size needs update from { %f, %f } to { %f, %f } (force=%s)"
- "<<<< AVPlayerLayer >>>> %s: AVPlayerLayer already connected to second screen"
- "<<<< AVPlayerLayer >>>> %s: AVPlayerLayer underlying video layer changed.  Will update dynamic range"
- "<<<< AVPlayerLayer >>>> %s: Called (self=%p) presentationSize={ .width = %.3f, .height = %.3f } forceUpdate: %s"
- "<<<< AVPlayerLayer >>>> %s: Called (self=%p, bounds=%@)"
- "<<<< AVPlayerLayer >>>> %s: Cannot add sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot insert sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot replace sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot set sublayers while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Display Size is %f x %f scale is %f"
- "<<<< AVPlayerLayer >>>> %s: Error in traversing layer tree"
- "<<<< AVPlayerLayer >>>> %s: Performance hud enabled (self=%p, hud=%p)"
- "<<<< AVPlayerLayer >>>> %s: Scheduling interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d (delayed to %f, now %f)"
- "<<<< AVPlayerLayer >>>> %s: Setting interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d"
- "<<<< AVPlayerLayer >>>> %s: Setting legibleContentInsets received from client. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerLayer >>>> %s: Setting readyForDisplay to NO due to detaching from player %@ (self=%p)"
- "<<<< AVPlayerLayer >>>> %s: Storing client layer %@ with indexPath %@"
- "<<<< AVPlayerLayer >>>> %s: Updated CC bounds with cached legibleContentInsets. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerLayer >>>> %s: Window scene containing layer <%p> did enter background"
- "<<<< AVPlayerLayer >>>> %s: Window scene containing layer <%p> will enter foreground"
- "<<<< AVPlayerLayer >>>> %s: called (keyPath=%@, object=%@, change=%@, context=%p"
- "<<<< AVPlayerLayer >>>> %s: called (self=%p)"
- "<<<< AVPlayerLayer >>>> %s: called (self=%p, isReadyForDisplay=%s"
- "<<<< AVPlayerLayer >>>> %s: called (self=%p, item=%p, videoLayer=%p readyForDisplay=%d)"
- "<<<< AVPlayerLayer >>>> %s: creating interstitialLayer %p for primary playerLayer %p"
- "<<<< AVPlayerLayer >>>> %s: displaySize is %f x %f rootSize is %f x %f percentage %f"
- "<<<< AVPlayerLayer >>>> %s: no window scene in _currentWindowSceneIsForeground <%p> , return default %d"
- "<<<< AVPlayerLayer >>>> %s: player layer %p <-> player layer %p"
- "<<<< AVPlayerLayer >>>> %s: requesting the pixelBufferAttributes property on a presentation layer is invalid"
- "<<<< AVPlayerLayer >>>> %s: scalingFactor(%d) is not between 2 and 8"
- "<<<< AVPlayerLayer >>>> %s: setting forScrubbingOnly = %d"
- "<<<< AVPlayerLayer >>>> %s: sync to player (self=%p, player=%p)"
- "<<<< AVPlayerLooper >>>> %s: AVPlayerLooperInternal allocation failed"
- "<<<< AVPlayerLooper >>>> %s: Already in Failed state so not updating error"
- "<<<< AVPlayerLooper >>>> %s: Can't loop with 0 item copies"
- "<<<< AVPlayerLooper >>>> %s: Change to Failed status with error %@"
- "<<<< AVPlayerLooper >>>> %s: Changing player's action-at-end to Advance"
- "<<<< AVPlayerLooper >>>> %s: Couldn't load asset duration. Change status to Failed"
- "<<<< AVPlayerLooper >>>> %s: Couldn't set up for looping. Change status to Failed"
- "<<<< AVPlayerLooper >>>> %s: Create with player %p and item %p"
- "<<<< AVPlayerLooper >>>> %s: End KVO setup"
- "<<<< AVPlayerLooper >>>> %s: Failed to allocate item copy"
- "<<<< AVPlayerLooper >>>> %s: In Failed or cancelled state so cannot advance to Ready"
- "<<<< AVPlayerLooper >>>> %s: Loop duration is less than minimum so capped number of copies to %d"
- "<<<< AVPlayerLooper >>>> %s: Loop item duration is %1.3f"
- "<<<< AVPlayerLooper >>>> %s: Loop time range end is past item duration"
- "<<<< AVPlayerLooper >>>> %s: Loop time range starts past item duration"
- "<<<< AVPlayerLooper >>>> %s: Looping item duration is 0. Can't loop"
- "<<<< AVPlayerLooper >>>> %s: Looping item(%p) failed to become ready so disabling looping"
- "<<<< AVPlayerLooper >>>> %s: Looping turned off and not waiting for looping copy to finish so ignoring"
- "<<<< AVPlayerLooper >>>> %s: Need %d copies for looping"
- "<<<< AVPlayerLooper >>>> %s: Need to create %d item copies"
- "<<<< AVPlayerLooper >>>> %s: Pausing player (current rate: %1.1f) during set up"
- "<<<< AVPlayerLooper >>>> %s: Restoring player rate(%1.1f)"
- "<<<< AVPlayerLooper >>>> %s: The minimum number of copies (%d) is sufficient for looping"
- "<<<< AVPlayerLooper >>>> %s: Time range duration is %1.3f"
- "<<<< AVPlayerLooper >>>> %s: Unknown context(%p). Ignoring"
- "<<<< AVPlayerLooper >>>> %s: Using loop duration of %1.3f"
- "<<<< AVPlayerLooper >>>> %s: [%p]Disabling looping since item(%p) failed to play to end with error %@"
- "<<<< AVPlayerLooper >>>> %s: ivarAccessQueue allocation failed"
- "<<<< AVPlayerLooper >>>> %s: loopingItemCopies allocation failed"
- "<<<< AVPlayerLooper >>>> %s: observeValueForKeyPath:ofObject:change:context: called for %@"
- "<<<< AVPlayerOutput >>>> %s: (%p) (%@)"
- "<<<< AVPlayerOutput >>>> %s: (%p) Buffer group for hostTime %.3f is equal to the last vended buffer group, therefore there is not a new buffer group for this time"
- "<<<< AVPlayerOutput >>>> %s: (%p) Cannot sample while fvr is NULL, ensure you have attached this output to a valid AVPlayer"
- "<<<< AVPlayerOutput >>>> %s: (%p) Failed to get buffer group for host time %.3f with error %d"
- "<<<< AVPlayerOutput >>>> %s: (%p) No buffer group was available for hostTime %.3f"
- "<<<< AVPlayerOutput >>>> %s: (%p) Received configuration with itemIdentifier %@ and could not find source item"
- "<<<< AVPlayerOutput >>>> %s: AVPlayerVideoOutput<%p> cannot be attached to more than one player at a time, already attached to player %@"
- "<<<< AVPlayerOutput >>>> %s: Failed to create and configure FVR with error: %d"
- "<<<< AVPlayerOutput >>>> %s: FigVideoReceiverSetActiveConfigurationChangedHandler failed with error: %d"
- "<<<< AVPlayerOutput >>>> %s: Received invalid preset %d"
- "<<<< AVPlayerOutput >>>> %s: unable to attach to player, received error %d when attempting to create and configure fvr/fvt pair"
- "<<<< AVPubSub >>>> %s:  called for %@"
- "<<<< AVPubSub >>>> %s: Adding observer for %@ in %@"
- "<<<< AVPubSub >>>> %s: Calling subscriber block because %@ fired for %@"
- "<<<< AVPubSub >>>> %s: Calling subscriber block for %@"
- "<<<< AVPubSub >>>> %s: Calling subscriber block from output publisher for %@"
- "<<<< AVPubSub >>>> %s: Calling subscriber block with initial value for %@"
- "<<<< AVPubSub >>>> %s: Calling subscriber block with nil publisher for %@"
- "<<<< AVPubSub >>>> %s: Not publishing stale value to subscriber block for %@"
- "<<<< AVPubSub >>>> %s: Notification observer calling callback in %@"
- "<<<< AVPubSub >>>> %s: Removing observer in %@"
- "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, %d channels"
- "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, no decodable format"
- "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, no format description"
- "<<<< AVQueuePlayer >>>> %s: %p %@. %s, reason %@, from %@ to %@"
- "<<<< AVQueuePlayer >>>> %s: %p %@. Y>N, reason %@, not enough items left"
- "<<<< AVQueuePlayer >>>> %s: %p %@. ignoring since buffered airplay is enabled but first 2 items are not ready for inspection"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. %{public}@ to %{public}@. YES"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. %{public}@ to %{public}@. YES, channel count match"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO because the multichannel audio strategy permits exclusive passthrough"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since %{public}@ has %d channels and %{public}@ has %d channels"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since AirPlay Video is active"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since Buffered AirPlay is active and SenderSideMixing is not enabled"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since action-at-end is NOT advance"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since one of items is HLS"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the first item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the first item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the second item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the second item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. YES, but %{public}@ channel count %d, %{public}@ channel count %d"
- "<<<< AVQueuePlayer >>>> %s: called (self %@ #items %d)"
- "<<<< AVQueuePlayer >>>> %s: called (self = %@)"
- "<<<< AVQueuePlayer >>>> %s: called (self = %@, item = %@)"
- "<<<< AVQueuePlayer >>>> %s: called (self = %@, item = %@, afterItem = %@"
- "<<<< AVResourceReclamationController >>>> %s: %p eventIdentifier=%@"
- "<<<< AVResourceReclamationController >>>> %s: skip registering for purge notification as its already registered"
- "<<<< AVRouteDetector >>>> %s: AirPlay device discovery disabled."
- "<<<< AVRouteDetector >>>> %s: AirPlay device discovery enabled."
- "<<<< AVRouteDetector >>>> %s: AirPlay devices present: %d"
- "<<<< AVRouteDetector >>>> %s: Creating DADiscoverySession failed with error: %@"
- "<<<< AVRouteDetector >>>> %s: Custom route discovery disabled."
- "<<<< AVRouteDetector >>>> %s: Custom route discovery enabled."
- "<<<< AVRouteDetector >>>> %s: Custom routes present: %d"
- "<<<< AVRouteDetector >>>> %s: Posting AVRouteDetectorMultipleRoutesDetectedDidChangeNotification."
- "<<<< AVRouteDetector >>>> %s: Received DAEventTypeDevicesPresentChanged. Devices present: %d"
- "<<<< AVRouteDetector >>>> %s: Received custom route discovery event, but AVRouteDetector.detectsCustomRoutes has since been disabled. Ignoring event."
- "<<<< AVSampleBufferAudioRenderer >>>> %s: Failed to create FigSampleBufferAudioRenderer: %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p]"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] Transitioning to status: %d"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %1.3f"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %d"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %lu"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %p"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] created"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] found contextUUID : %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] setting routing context id : %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
- "<<<< AVSampleBufferAudioRenderer >>>> %s: adding notification listener to %p with listener %p"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: called"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: got notification %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: removing notification listener to %p with listener %p"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ %p AVSampleBufferDisplayLayer's net flip status does match CoreAnimation default"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ %p AVSampleBufferDisplayLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ AVSBDL entering PiP, setting preferredDynamicRange"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ AVSBDL exiting PiP, setting preferredDynamicRange"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Created layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Hiding contentLayer because bounds is CGSizeZero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ New label \"%@\", Current label \"%@\", Layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Removing label from layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Setting label \"%@\" on layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Setting position(%d,%d), bounds(%dx%d), transform scale(%.3fx%.3f), offset(%d,%d)"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Unhiding contentLayer because bounds is nonzero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ Visibility [%@], on thread %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ bounds: %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ called"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ on thread %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ videoRect: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Cleaning-up renderer %p for synchronizerInternal %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Error adding an AudioRenderer to the FigSynchronizer: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Failed to add Renderer %@; error returned from _addRenderer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Failed to create FigSampleBufferRenderSynchronizer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Selecting AVSBDL=%p that already contains a label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Selecting AVSBVR=%p with label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Setting STSLabel %@ on renderer=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Setting new STSLabel on AVSBDL=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Setting self as render synchronizer on renderer (%p) failed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Too many audio renderers"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Trying to add a renderer (%p) to same synchronizer"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Trying to add multiple audio renderers when disallowed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ Was tracking AVSBDL=%p, switching to AVSBVR=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ [%p], on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ adding renderer %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ called"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ called (center=%@, listener=%p, name=%@, object=%p, payload=%@)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ called (time observer = <%p>)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ called for renderer %p; time: %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ created (internal: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ error: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ invalidated old scheduled removal of renderer %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ old once observer already fired before we could invalidate it (renderer: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ rate: %1.3f; time: %1.3f; hostTime: %1.3f; fig error: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ releasing on main thread avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ removalBlock called; weakToSelf: %p; weakToRenderer: %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ retaining avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ successfully scheduled removal of renderer %p at time %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: %{public}@ unknown renderer: %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: NOT creating STS Label because SpatialAudioExperience FF set"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Render synchronizer %s participate in STS -- thank you for setting \"defaults write com.apple.avfoundation rendersynchronizer_sts_label -bool %s\""
- "<<<< AVSampleBufferVideoOutput >>>> %s: Dispatching -outputSequenceWasFlushed:"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArray failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArrayOptions failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCopyImageForTime did not provide a imageOriginalTimeOut value. Bailing."
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCreate failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextSetImageAvailableImmediateCallback failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: Sending -outputSequenceWasFlushed: to delegate"
- "<<<< AVSampleBufferVideoOutput >>>> %s: Unable to copy next image from visual context. Bailing."
- "<<<< AVSampleBufferVideoOutput >>>> %s: copyPixelBufferForSourceTime requestTime %1.3f pb %p time %1.3f"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Adding %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Calling completion handler with %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Calling completion handler with success"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Failed to copy currently displayed pixel buffer as there is no video queue"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Failed to create AVSBVR error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Failed to create video queue error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Failed with error %d at %s"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ FigVideoQueueFlush returned error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Flush completed but no pending callback block found"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Flush returned err=%d. Recreating FigVideoQueue. %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Ignoring enqueueSampleBuffer because status is failed"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ No pending preroll callback"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Output obscured = %@, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Received complete decode for preroll [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Received external protection status changed [%p] to \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Received flush complete [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Received video queue decode error \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Received video queue did drop below low water level [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ RemoveDisplayedImage=%s, handler=%p, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Removing %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Setting %@, posting AVSampleBufferSTSLabelDidChangeNotification"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Setting %p, returning %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Skip stale callback, requestId (%d) != pendingPrerollRequestID (%d)"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Total frames enqueued since last flush %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Unable to set expectMinimumUpcomingSampleBufferPresentationTime because minimumUpcomingPresentationTime is not numeric"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ UpcomingPTSExpectation is enabled, but enqueuePTS:%.3f is smaller than expectedMinimumUpcomingPTS:%.3f"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ VideoQueue [%p] Setting %d video targets."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ VideoQueue [%p] Setting display layer %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ VideoQueue [%p] on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Visibility [%@] on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ Visibility changed to %s, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Enqueue sample buffer failed error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Failed to copy currently displayed pixel buffer although no error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Received lost decoder state error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Received server connection died with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Received server dependency lost with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ [%p] Received video queue failed with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ _updatePreferredDynamicRange(%@)"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ exit layerQueue block, on thread [%@]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ readyForDisplay changed (%@), post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ releasing %p on main thread, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: %{public}@ timebase %@"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorCreateSampleBuffer failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetDecodeTimeStamp failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetPresentationTimeStamp failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByDecodeTime failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByPresentationTime failed (%d)"
- "<<<< AVScheduledAudioParameters >>>> %s: not a valid scheduled ramp class"
- "<<<< AVScheduledParameterRamp >>>> %s: Unknown ramp mode: %d"
- "<<<< AVStreamDataParser >>>> %s: Exception when creating default key session: %@"
- "<<<< AVStreamDataParser >>>> %s: Expected NSData or NSArray, ignoring unexpected \"%@\""
- "<<<< AVStreamDataParser >>>> %s: Expected NSData sinf, ignoring unexpected \"%@\""
- "<<<< AVStreamDataParser >>>> %s: abandoning manifold initialization after %ld bytes (max %ld bytes)"
- "<<<< AVStreamDataParser >>>> %s: appending stream data (flags 0x%x) %@"
- "<<<< AVStreamDataParser >>>> %s: changing manifold type not permitted during AVStreamDataParser session"
- "<<<< AVStreamDataParser >>>> %s: create sandboxed parser for blockbuffer"
- "<<<< AVStreamDataParser >>>> %s: created a FigManifold"
- "<<<< AVStreamDataParser >>>> %s: dealloc"
- "<<<< AVStreamDataParser >>>> %s: failed to create CMBlockBuffer for %d bytes with data at %p and offset %d, status = %d"
- "<<<< AVStreamDataParser >>>> %s: init"
- "<<<< AVStreamDataParser >>>> %s: manifold all new tracks ready, building inspection-only asset"
- "<<<< AVStreamDataParser >>>> %s: manifold discovered trackID %ld, mediaType %@, remembered for AllNewTracksReady"
- "<<<< AVStreamDataParser >>>> %s: manifold error %d, track %d, %@"
- "<<<< AVStreamDataParser >>>> %s: manifold sent PTS %1.5f %d bytes, %@/%@, track %d, flags %d"
- "<<<< AVStreamDataParser >>>> %s: need delegate to implement streamDataParser:didProvideContentKeyRequestInitializationData:forTrackID:"
- "<<<< AVStreamDataParser >>>> %s: need more data to sniff"
- "<<<< AVStreamDataParser >>>> %s: new AVStreamDataAsset using manifold's FigAsset"
- "<<<< AVStreamDataParser >>>> %s: new AVStreamDataAsset with tracks %@"
- "<<<< AVStreamDataParser >>>> %s: no asset yet so caching sample buffer (now cached %d bytes, %.3f seconds)"
- "<<<< AVStreamDataParser >>>> %s: no manifold, sniffing data to initialize one..."
- "<<<< AVStreamDataParser >>>> %s: providePendingMediaData"
- "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because trackID %d ended"
- "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because trackID %ld got a new format description"
- "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because we've not got a CMFormatDescription for trackID %d"
- "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset with additional trackID %d"
- "<<<< AVStreamDataParser >>>> %s: registering for manifold callbacks from trackID %d"
- "<<<< AVStreamDataParser >>>> %s: set preferSandboxedParsing to %d"
- "<<<< AVStreamDataParser >>>> %s: setShouldProvideMediaData:forTrackId:%d, not providing media for %@"
- "<<<< AVStreamDataParser >>>> %s: shouldProvideMediaDataForTrackID said no, ignoring media for trackID %d"
- "<<<< AVStreamDataParser >>>> %s: sniffing stream data (flags 0x%x) %@"
- "<<<< AVStreamDataParser >>>> %s: switching manifold"
- "<<<< AVStreamDataParser >>>> %s: trackID %ld got a new format description, remembered for AllNewTracksReady"
- "<<<< AVStreamDataParser >>>> %s: trackID %ld is not encrypted or using unsupported encryption. Removing the cached decryptor for this track."
- "<<<< AVStreamDataParser >>>> %s: trackID %ld is using supported encryption"
- "<<<< AVStreamDataParser >>>> %s: unregistering for manifold callbacks from trackID %d"
- "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> created for firing time [%1.3f]"
- "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> firing for firing time [%1.3f] at current time [%1.3f]"
- "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> with source <%p> at current time [%f] nextfire [%f]"
- "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> Firing at current time [%1.3f]"
- "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> created with timebase %p and fire times: %@"
- "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> with source <%p> at current time [%f] nextfire [%f]"
- "<<<< AVTimebaseObserver >>>> %s: Periodic Observer <%p> Jumped to time [%f]"
- "<<<< AVTimebaseObserver >>>> %s: Periodic Observer <%p>: Detected stop time jump to the last time where rate fell to zero and have winnowed this event"
- "<<<< AVTimebaseObserver >>>> %s: Playback direction did change. Resetting timer"
- "<<<< AVTimebaseObserver >>>> %s: Playback resumed. Observe immediate."
- "<<<< AVTimebaseObserver >>>> %s: Playback stopped. Observe immediate."
- "<<<< AVTimebaseObserver >>>> %s: Timebase observer invalidated, ignoring notification"
- "<<<< AVTimebaseObserver >>>> %s: Timebase returned non-numeric time (%lld/%d/%#x/%lld)) so setting to kCMTimeZero"
- "<<<< AVTimebaseObserver >>>> %s: Timebase returned time with non-zero epoch(%lld) so setting to kCMTimeZero"
- "<<<< AVTimebaseObserver >>>> %s: Timebase returned time(%@)"
- "<<<< AVTimebaseObserver >>>> %s: Timebase returned time(%@), clamped from time(%@)"
- "<<<< AVTimebaseObserver >>>> %s: after applying offset %@, nextIntervalTime is now %@"
- "<<<< AVTimebaseObserver >>>> %s: engage timebase <%p> notifications for <%p>"
- "<<<< AVTimebaseObserver >>>> %s: firing at time == %@"
- "<<<< AVTimebaseObserver >>>> %s: rescheduling after non-periodic firing near time == %@"
- "<<<< AVTimebaseObserver >>>> %s: rescheduling after periodic firing at time == %@"
- "<<<< AVTimebaseObserver >>>> %s: scheduling for == %@"
- "<<<< AVTimebaseObserver >>>> %s: timebase rate change from [%f] to [%f]"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Class must be an instance of NSString"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Cue must be an instance of NSString"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_DiscoveryTimestamp must be an instance of NSDate"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Duration must be an instance of NSNumber"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_ID must be an instance of NSString"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_MetadataArray must be an instance of NSArray"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_ModificationTimestamp must be an instance of NSDate"
- "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_StartDate must be an instance of NSDate"
- "<<<< AVUtilities >>>> %s: called (queue=%p, currentQueue=%p, dispatch_get_main_queue()=%p, NSThread isMainThread=%d)"
- "<<<< AVUtilities >>>> %s: dispatching block to queue"
- "<<<< AVUtilities >>>> %s: dispatching to background queue"
- "<<<< AVUtilities >>>> %s: running block synchronously"
- "<<<< AVVideoComposition >>>> %s: Unknown video compositor name for FigRemaker: %@"
- "<<<< AVVideoComposition >>>> %s: Using video compositor: %@"
- "<<<< AVVideoComposition >>>> %s: dictionaryRepresentation only accepts RGB color space for backgroundColor"
- "<AVPlayerLayer %p%@%@%@%@>"
- "AV Perf - Begin: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
- "AV Perf - End: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
- "AVAsset.m"
- "AVAssetDownloadConfiguration.m"
- "AVAssetDownloadSession.m"
- "AVAssetPlanner.m"
- "AVAssetReaderOutputCaptionAdaptor.m"
- "AVAssetResourceLoader.m"
- "AVAssetWriterFigAssetWriterHandleCompletedNotification"
- "AVAssetWriterFigAssetWriterHandleFailedNotification"
- "AVAssetWriterFigAssetWriterHandleServerDiedNotification"
- "AVAssetWriterInputFigAssetWriterEndPassOperationPassFinished"
- "AVCanWriteFilesToDirectoryAtURL"
- "AVCompositionTrack.m"
- "AVContentKeySession.m"
- "AVEnsureNotOnMainThread"
- "AVErrorAssetPlannerSessionAlreadyStarted"
- "AVErrorAssetPlannerStateFileInvalidValue"
- "AVErrorAssetPlannerTrackAlreadyPlanned"
- "AVErrorAutoWhiteBalanceNotLocked"
- "AVFigRoutingContextRouteChangeOperationRouteChangeComplete"
- "AVLocalizedError"
- "AVLocalizedStringFromTableWithLocaleWithBundleIdentifier"
- "AVMediaStatePurgePostMediaStateWasPurgedNotificationForObject"
- "AVMetadataItem.m"
- "AVMetadataItemMakeDataFromBoxedMetadata"
- "AVOperationStatusResolveOldAndNew"
- "AVPerfTelemetry"
- "AVPerformDelegateCallbackSynchronouslyForDelegateStorageIfCurrentDelegateQueueIsQueueElseDispatchToCurrentDelegateQueue"
- "AVPlaybackCoordinator.m"
- "AVPlayerCaptionLayer <%p>"
- "AVPlayerGetFigPlayerTypeForAsset"
- "AVPlayerItem addOutput"
- "AVPlayerItem audioMix"
- "AVPlayerItem currentMediaSelection"
- "AVPlayerItem currentTime"
- "AVPlayerItem customVideoCompositor"
- "AVPlayerItem initWithAsset"
- "AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys"
- "AVPlayerItem outputs"
- "AVPlayerItem removeOutput"
- "AVPlayerItem selectMediaOption:inMediaSelectionGroup"
- "AVPlayerItem selectMediaOption:mediaSelectionOption:mediaSelectionGroup"
- "AVPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup"
- "AVPlayerItem setAudioMix"
- "AVPlayerItem setVideoComposition"
- "AVPlayerItem stepByCount"
- "AVPlayerItem videoComposition"
- "AVPlayerItemTrack assetTrack"
- "AVPlayerItemVideoOutput_figVCSequentialAvailableCallback_block_invoke_3"
- "AVPlayerItemVideoOutput_timebaseNotificationCallback_block_invoke"
- "AVPlayerLayer <%p>"
- "AVPlayerLayer <%p> (closedCaptionLayer)"
- "AVPlayerLayer <%p> (videoLayer)"
- "AVPlayerLayerFilterClientLayersFromLayerWithIndexPath"
- "AVPlayerOutput.m"
- "AVResetMediaServices"
- "AVSBVR failed with error %d at %s."
- "AVSampleBufferDisplayLayer <%p>"
- "AVSampleBufferDisplayLayer <%p> (content layer)"
- "AVSampleBufferRenderSynchronizer init"
- "AVSampleBufferVideoRenderer.m"
- "AVSerializeOnQueueAsyncIfNecessary"
- "AVStreamDataParser.m"
- "AVTimebaseObserver_figTimebaseGetTime"
- "AVTimebaseObserver_timebaseNotificationCallback_block_invoke"
- "AVUtilities.m"
- "An AVAssetTrackPlan for the same assemblyTrackID is already added to the planner"
- "AuxilaryVideoAttachmentsLookup"
- "B36@0:8@16@24B32"
- "CMTagCollectionCreateWithVideoOutputPreset"
- "CodecType not found in dictionary"
- "Could not set KeyResponseReceived state on cryptor."
- "Cryptor is not available to create key request."
- "FVQSetProperty(ControlTimebase)"
- "FVQSetProperty(DisplayLayer)"
- "Failed on init"
- "Failed to allocate CFMutableDictionary"
- "Failed to allocate buffer for FigBoxedMetadata -> CFData conversion"
- "Failed to connect to coordination medium"
- "Failed to create a segment from dictionary"
- "Failed to get queue"
- "Failed to load trackState from dictionary"
- "Failed to prepare cryptor"
- "Failed to set video target array on video queue."
- "FigSubtitleCALayer"
- "FigUseVideoReceiverForCALayer is YES, videoLayer should have a videoTarget"
- "FigVideoQueueCreate"
- "FigVideoQueueStart"
- "FrameCount <= 0 from dictionary"
- "HasCompleted not found from dictionary"
- "Hiding"
- "InternalPerfTelemetry"
- "Invalid asset track"
- "Invalid timeRange from dictionary"
- "MediaType not found in dictionary"
- "N>Y"
- "NOT visible"
- "NULL"
- "NULL figAsset"
- "NULL handlerServerXPCEndpoint"
- "NULL segmentURL from dictionary"
- "Names count is 0?"
- "No FCKS available"
- "Not allowed to add track plan after writing has started"
- "Received invalid preset"
- "RequiresVideoCompression not found in dictionary"
- "Segments not found in dictionary"
- "Showing"
- "The AVSampleBufferDisplayLayer's content layer is nil."
- "TimeRange from dictionary <= 0"
- "TimeRange from dictionary has a non-numeric duration"
- "TimeRange from dictionary has a non-numeric start"
- "TrackID is invalid in dictionary"
- "TrackID not found in dictionary"
- "Trying to create AVAssetDownloadContentConfiguration with an invalid AVAssetVariantQualifier"
- "Visible"
- "WILL"
- "WILL NOT"
- "Y>N"
- "_avplLoopingItemFailedToPlayToEndTimeNotificationHandler"
- "_canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:"
- "_compactDescription"
- "_enqueueSingleSampleBufferStatic"
- "_enqueuedFramesForLoggingOnly"
- "_figManifoldError"
- "_figVideoQueueCompletedDecodeForPreroll"
- "_figVideoQueueDecodeError"
- "_figVideoQueueDidDropBelowLowWaterLevel"
- "_figVideoQueueExternalProtectionStatusChanged"
- "_figVideoQueueFailed"
- "_figVideoQueueFlushComplete"
- "_figVideoQueueLostDecoderState"
- "_figVideoQueueServerConnectionDied"
- "_figVideoQueueServerDependencyLost"
- "_resetGroupTimelineExpectations"
- "_sampleDescriptionExtensionAtomForKey"
- "_setIntegratedTimelineCreatingNew:"
- "_updateAudioTapProcessorOnFigPlaybackItem"
- "_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:"
- "addSampleBufferDisplayLayer failed to set content layer"
- "aig_trace"
- "appendCaptionGroupToQueue"
- "are"
- "are NOT"
- "assetTrackNotificationHandler"
- "assetinspector_trace"
- "assetplanner_trace"
- "assetreaderoutput_trace"
- "assettrackinspector_trace"
- "assetwriter_trace"
- "assetwriterinput_trace"
- "assetwriterinputannotationadaptor_trace"
- "assetwriterinputmetadataadaptor_trace"
- "audioTapProcessorWasSet"
- "avAssetDownloadSession_figAssetNotificationCallback"
- "avAssetDownloadSession_figPlaybackItemNotificationCallback"
- "avasset_trace"
- "avassetcache_trace"
- "avassetresourceloader_trace"
- "avassetstoragemanager_trace"
- "avasynchronouskeyvalueloading_trace"
- "avcaptionrenderer_trace"
- "avcc_trace"
- "avcifilter_trace"
- "avckrg_externalProtectionStateChangedCallback"
- "avckrg_keyResponseErrorCallback"
- "avckrg_keyResponseSuccessfullyProcessedCallback"
- "avckrg_persistentKeyUpdatedCallback"
- "avckrg_secureStopDidFinalizeRecordCallback"
- "avcks_decodeInitializationDataAndCopyInformation"
- "avexport_trace"
- "avloggingidentifier_trace"
- "avmediaselectiongroup_trace"
- "avmediastatepurge_trace"
- "avmetadataitem_trace"
- "avmovie_trace"
- "avoperation_trace"
- "avpixelbufferattributemediator_trace"
- "avplayer_fpInterstitialCoordinatorNotificationCallback"
- "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_3"
- "avplayer_fpNotificationCallback"
- "avplayer_fpNotificationCallback_block_invoke"
- "avplayer_fpNotificationCallback_block_invoke_2"
- "avplayer_fpNotificationCallback_block_invoke_4"
- "avplayer_fpNotificationCallback_block_invoke_5"
- "avplayer_fpNotificationCallback_block_invoke_6"
- "avplayer_iapdNotificationCallback"
- "avplayer_iapdNotificationCallback_block_invoke"
- "avplayer_iapdNotificationCallback_block_invoke_2"
- "avplayer_playbackcoordinator_SetPlaybackCoordinatorInterstitialActive"
- "avplayercaptionlayer_trace"
- "avplayerinterstitialeventmonitor_fpNotificationCallback"
- "avplayeritem_fpItemNotificationCallback_block_invoke"
- "avplayeritem_fpItemNotificationCallback_block_invoke_2"
- "avplayeritem_fpItemNotificationCallback_block_invoke_3"
- "avplayeritem_fpItemNotificationCallback_block_invoke_4"
- "avplayeritem_fpItemNotificationCallback_block_invoke_5"
- "avplayeritem_fpItemNotificationCallback_block_invoke_7"
- "avplayeritemlegibleoutput_trace"
- "avplayeritemmediadatacollector_trace"
- "avplayeritemmetadatacollector_trace"
- "avplayeritemmetadataoutput_trace"
- "avplayeritemoutput_trace"
- "avplayeritemrenderedlegibleoutput_trace"
- "avplayerlayer_trace"
- "avplayerlooper_trace"
- "avplayeroutput_trace"
- "avqsbar_figRendererServerDied"
- "avrendersynchronize_cleanUpAllAddedRenderers"
- "avrendersynchronize_electRendererForSTSAndSendLabelToAudioRenderers"
- "avrendersynchronize_performRendererRemoval"
- "avrendersynchronizer_timebaseRateChanged"
- "avsamplebufferaudiorenderer_trace"
- "avsamplebufferdisplaylayer_trace"
- "avsamplebuffergenerator_trace"
- "avsamplebufferoutput_trace"
- "avsamplebufferrendersynchronizer_trace"
- "avsamplebuffervideooutput_trace"
- "avsamplecursor_trace"
- "avstreamdataparser_trace"
- "avtimebaseobserver_trace"
- "avtimedmetadatagroup_trace"
- "avurlasset_setupGuts"
- "avutilities_trace"
- "avuxm_trace"
- "badly formatted PSSH data"
- "badly formatted key request init data - codecType not valid"
- "badly formatted key request init data - containerType not valid"
- "badly formatted key request init data - mediaType not valid"
- "badly formatted key request init data - sinf array not found"
- "bail error check"
- "basics"
- "boss NULL"
- "calling attachSpatialVideoConfiguration:toPixelBuffer is illegal when AVVideoComposition's spatialVideoConfigurations is nil"
- "ccr_trace"
- "cmTimebaseNotificationCallback_TimeJumped"
- "codecType is not NSString"
- "colorSpace"
- "completed"
- "composition_trace"
- "copyVideoReceiver"
- "could not create trackDecryptor"
- "createFigAsset"
- "creationOptions NULL"
- "cryptor is NULL"
- "customURLAuthHandlerHandleRequestCallback"
- "customURLAuthHandlerRequestCancelled"
- "customURLHandlerHandleRequestCallback"
- "customURLHandlerRequestCancelled"
- "delegateutils_trace"
- "download_trace"
- "expected initialization data to be a JSON dictionary containing an array of SINF data"
- "externaldevice_trace"
- "failed to alloc content key request"
- "failed to convert initializationData to a JSON object"
- "failed to query records due to an internal error"
- "failed to remove records due to an internal error"
- "failure"
- "false"
- "figAsset already set"
- "figAssetReaderDecodeError"
- "figAssetReaderFailed"
- "figAssetReaderSampleBufferDidBecomeAvailable"
- "figAssetReaderServerConnectionDied"
- "figEndpointNotificationCallback"
- "figLoaderNotificationHandler"
- "figPlaybackItemTrackResetSampleBufferExtraction"
- "figPlaybackItemTrackSampleBufferDidBecomeAvailable"
- "file"
- "filesystemutilities_trace"
- "frameCountNumber is not NSNumber"
- "frameCountNumber not found from dictionary"
- "getAudioChannelCountForFirstEnabledTrack"
- "handleFigAssetNotification"
- "handleFigAssetTrackNotification"
- "handleFigAssetTrackNotification_block_invoke"
- "hasCompletedNumber is not NSNumber"
- "hlsvariant_trace"
- "in-process"
- "inspection"
- "inspector_trace"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kCMTagCollectionError_ParamErr"
- "kFigCPEError_InvalidState"
- "kFigContentKeyBossError_AllocationFailed"
- "kFigMetadataReaderError_AllocationFailed"
- "kFigPlayerError_InternalError"
- "kFigSSMError_InvalidState"
- "key request has not succeeded. value not available."
- "kvodispatcher_trace"
- "lastCompletedSegmentFinalHDRMetadataGenerationState is not NSDictionary"
- "mediaType is not NSString"
- "mismatched handler"
- "nil reference"
- "no figAsset"
- "non-NULL"
- "not an AVAssetResourceLoader"
- "not an AVAssetResourceLoaderRemoteHandlerContext"
- "not an AVContentKeyReportGroup"
- "not an AVContentKeySession"
- "not spatial"
- "pathWithComponents:"
- "playback"
- "remote"
- "requiresFrameCountNumber is not NSNumber"
- "requiresVideoCompressionNumber is not NSNumber"
- "scheduledaudioparameters_trace"
- "segmentsAsDictionaries is not NSArray"
- "self.figAsset NULL"
- "sessionName is not NSString"
- "setBorderColor:"
- "setBorderWidth:"
- "stringWithValidatedFormat"
- "stringWithValidatedFormatArg2"
- "stringWithValidatedFormatInteger"
- "stringWithValidatedFormatString"
- "subarrayWithRange:"
- "taggedBufferGroup contains pixel buffers associated with different spatial configurations."
- "taggedBufferGroup contains pixel buffers associated with spatial configurations, but AVVideoComposition's spatialVideoConfigurations is nil"
- "timeRangeDictionary is not NSDictionary"
- "trackIDNumber is not NSNumber"
- "true"
- "visible"
- "yes"

```
