## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2340.10.1.0.0
-  __TEXT.__text: 0x2227ac
-  __TEXT.__auth_stubs: 0x39d0
-  __TEXT.__objc_methlist: 0x1d874
-  __TEXT.__cstring: 0x37092
-  __TEXT.__const: 0x368
-  __TEXT.__gcc_except_tab: 0x5398
-  __TEXT.__oslogstring: 0x21575
+2340.12.2.0.0
+  __TEXT.__text: 0x1bf638
+  __TEXT.__auth_stubs: 0x3920
+  __TEXT.__objc_methlist: 0x1d86c
+  __TEXT.__cstring: 0x2709a
+  __TEXT.__const: 0x278
+  __TEXT.__gcc_except_tab: 0x48e8
+  __TEXT.__oslogstring: 0x7be6
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x9230
+  __TEXT.__unwind_info: 0x8f90
   __TEXT.__objc_classname: 0x6798
-  __TEXT.__objc_methname: 0x3744e
+  __TEXT.__objc_methname: 0x373ca
   __TEXT.__objc_methtype: 0xadef
-  __TEXT.__objc_stubs: 0x21bc0
+  __TEXT.__objc_stubs: 0x21ae0
   __DATA_CONST.__got: 0x4c90
-  __DATA_CONST.__const: 0x5be8
+  __DATA_CONST.__const: 0x5b98
   __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf90
+  __DATA_CONST.__objc_selrefs: 0xaf60
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xda0
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__auth_got: 0x1cf8
-  __AUTH_CONST.__const: 0xf58
-  __AUTH_CONST.__cfstring: 0x197c0
-  __AUTH_CONST.__objc_const: 0x35438
+  __AUTH_CONST.__auth_got: 0x1ca0
+  __AUTH_CONST.__const: 0xf38
+  __AUTH_CONST.__cfstring: 0x19300
+  __AUTH_CONST.__objc_const: 0x35418
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7a30
   __AUTH.__data: 0x150
-  __DATA.__objc_ivar: 0x2630
-  __DATA.__data: 0x1ca8
+  __DATA.__objc_ivar: 0x262c
+  __DATA.__data: 0x1c88
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x450
-  __DATA.__bss: 0x3b0
+  __DATA.__bss: 0x3a8
+  __DATA.__common: 0x1c0
   __DATA_DIRTY.__objc_data: 0x4330
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0x2e0
-  __DATA_DIRTY.__bss: 0x1b1
+  __DATA_DIRTY.__bss: 0x1a1
+  __DATA_DIRTY.__common: 0x1c0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 026CB1F2-8755-313E-9A88-FD916626B2A9
-  Functions: 11929
-  Symbols:   41353
-  CStrings:  19733
+  UUID: 8BFF82D6-2656-37E9-A540-AE9BD705D67D
+  Functions: 11760
+  Symbols:   40870
+  CStrings:  17403
 
Symbols:
+ -[AVSampleBufferAudioRenderer setOutputContext:].cold.1
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.4
+ GCC_except_table148
+ GCC_except_table158
+ GCC_except_table169
+ GCC_except_table94
+ _FigSignalErrorAt
+ ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke_2
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.1
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.2
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
+ ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke_2
+ ___46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke_2
+ ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_3
+ ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_4
+ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2
+ ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.499
+ ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke_2
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke_2
+ ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke_2
+ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_3
+ ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_3
+ ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke_4
+ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_3
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.459
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.463
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.471
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.472
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.479
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.480
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.482
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1064
+ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_3
+ ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_4
+ ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_5
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
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1061
+ ___Block_byref_object_copy_.102
+ ___Block_byref_object_copy_.11
+ ___Block_byref_object_copy_.91
+ ___Block_byref_object_dispose_.103
+ ___Block_byref_object_dispose_.12
+ ___Block_byref_object_dispose_.92
+ ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4
+ ___avplayer_fpNotificationCallback_block_invoke_10
+ ___avplayer_fpNotificationCallback_block_invoke_11
+ ___avplayer_fpNotificationCallback_block_invoke_12
+ ___avplayer_fpNotificationCallback_block_invoke_13
+ ___avplayer_fpNotificationCallback_block_invoke_14
+ ___avplayer_fpNotificationCallback_block_invoke_5
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
+ ___block_descriptor_52_e8_32o40o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8
+ ___block_literal_global.1043
+ ___block_literal_global.1045
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.115
+ ___block_literal_global.118
+ ___block_literal_global.1273
+ ___block_literal_global.131
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.199
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.238
+ ___block_literal_global.303
+ ___block_literal_global.344
+ ___block_literal_global.347
+ ___block_literal_global.385
+ ___block_literal_global.390
+ ___block_literal_global.414
+ ___block_literal_global.427
+ ___block_literal_global.431
+ ___block_literal_global.442
+ ___block_literal_global.475
+ ___block_literal_global.532
+ ___block_literal_global.533
+ ___block_literal_global.544
+ ___block_literal_global.547
+ ___block_literal_global.632
+ ___block_literal_global.638
+ ___block_literal_global.736
+ ___block_literal_global.874
+ ___block_literal_global.883
+ ___figEndpointNotificationCallback_block_invoke_2
+ ___figEndpointNotificationCallback_block_invoke_3
+ ___handleFigAssetLoadingNotification_block_invoke.529
+ ___handleFigAssetTrackNotification_block_invoke_2
- -[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:].cold.2
- -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler].cold.2
- -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.1
- -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.2
- -[AVPlayerLayer _compactDescription]
- GCC_except_table110
- GCC_except_table149
- GCC_except_table165
- GCC_except_table172
- _AVBacktraceAsString
- _AVBacktraceAsStringWithMaxFrames
- _AVTelemetryGenerateID.cold.1
- _AVTelemetryLogHandle
- _AVTelemetryLogHandle.cold.1
- _AVTelemetryLogHandle.emitter
- _AVTelemetryLogHandle.onceToken
- _CMSampleBufferGetPresentationTimeStamp
- _FigDebugIsInternalBuild
- _FigPlaybackRateChangeReasonGetDescription
- _FigSignalErrorAt3
- _NSStringFromRect
- _NSStringFromSize
- _OBJC_IVAR_$_AVSampleBufferVideoRenderer._enqueuedFramesForLoggingOnly
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- __CMBlockBufferAsString
- ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke.201
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165.cold.1
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165.cold.2
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.429
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.430
- ___122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.135
- ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke.170
- ___146-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke.cold.1
- ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.152
- ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_2.154
- ___21-[AVPlayerLayer init]_block_invoke.108
- ___22-[AVPlayer _addLayer:]_block_invoke.570
- ___22-[AVPlayer _addLayer:]_block_invoke.571
- ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke.432
- ___31-[AVPlayerItem _updateTimebase]_block_invoke.587
- ___31-[AVPlayerItem _updateTimebase]_block_invoke_2.588
- ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke.495
- ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.261
- ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke.537
- ___42-[AVPlayerCaptionLayer _interstitialLayer]_block_invoke.50
- ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke.71
- ___46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke.261
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke.474
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_2.475
- ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke.267
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.920
- ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.509
- ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke.151
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1098
- ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke.263
- ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.159
- ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke.99
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.108
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.109
- ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke.82
- ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke.507
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.449
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.453
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.466
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.478
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.487
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.490
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.470
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.479
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.488
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1084
- ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke.246
- ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.234
- ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.235
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke.922
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2.923
- ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.136
- ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.40
- ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.41
- ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke.908
- ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke.549
- ___78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.28
- ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke.56
- ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.115
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.71
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.74
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.89
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.128
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.129
- ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke.308
- ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.569
- ___90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke.364
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1081
- ___AVTelemetryLogHandle_block_invoke
- ___Block_byref_object_copy_.106
- ___Block_byref_object_copy_.130
- ___Block_byref_object_dispose_.107
- ___Block_byref_object_dispose_.131
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1276
- ___avplayer_fpNotificationCallback_block_invoke.1290
- ___avplayer_fpNotificationCallback_block_invoke.1293
- ___avplayer_fpNotificationCallback_block_invoke.1295
- ___avplayer_fpNotificationCallback_block_invoke.1306
- ___avplayer_fpNotificationCallback_block_invoke.1310
- ___avplayer_fpNotificationCallback_block_invoke_2.1296
- ___avplayer_fpNotificationCallback_block_invoke_2.1307
- ___avplayer_fpNotificationCallback_block_invoke_3.1300
- ___avplayer_fpNotificationCallback_block_invoke_3.1308
- ___avplayer_fpNotificationCallback_block_invoke_4.1309
- ___avplayer_iapdNotificationCallback_block_invoke.1312
- ___avplayer_iapdNotificationCallback_block_invoke.1313
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1454
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1474
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1479
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1480
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1484
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1488
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1495
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1496
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1497
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1501
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1502
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1508
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1514
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1515
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1519
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1520
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1521
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1528
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1503
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1509
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1516
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1504
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1517
- ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1505
- ___avplayeritem_fpItemNotificationCallback_block_invoke_5.1506
- ___block_descriptor_48_e8_32o40b_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32o40r_e26_v32?0"AVCaption"8Q16^B24ls32l8r40l8
- ___block_descriptor_60_e8_32o40o48o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32o40o48b56w_e24_v16?0"NSNotification"8ls32l8w56l8s48l8s40l8
- ___block_descriptor_64_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_96_e8_32o40o48o56o64o72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8r88l8
- ___block_literal_global.1055
- ___block_literal_global.1057
- ___block_literal_global.109
- ___block_literal_global.1316
- ___block_literal_global.137
- ___block_literal_global.140
- ___block_literal_global.148
- ___block_literal_global.151
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.233
- ___block_literal_global.239
- ___block_literal_global.242
- ___block_literal_global.281
- ___block_literal_global.307
- ___block_literal_global.353
- ___block_literal_global.391
- ___block_literal_global.395
- ___block_literal_global.419
- ___block_literal_global.432
- ___block_literal_global.441
- ___block_literal_global.455
- ___block_literal_global.519
- ___block_literal_global.538
- ___block_literal_global.539
- ___block_literal_global.560
- ___block_literal_global.573
- ___block_literal_global.648
- ___block_literal_global.658
- ___block_literal_global.740
- ___block_literal_global.85
- ___block_literal_global.881
- ___block_literal_global.899
- ___figEndpointNotificationCallback_block_invoke.325
- ___figEndpointNotificationCallback_block_invoke.330
- ___handleFigAssetLoadingNotification_block_invoke.528
- ___handleFigAssetTrackNotification_block_invoke.453
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
- _gAVPlatformUtilitiesTrace
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
- _gAVQueuePlayerTrace
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
- _gAVUtilitiesTrace
- _gScheduledParameterRampTrace
- _objc_msgSend$_compactDescription
- _objc_msgSend$colorSpace
- _objc_msgSend$externalContentProtectionStatus
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$setBorderColor:
- _objc_msgSend$setBorderWidth:
- _objc_msgSend$subarrayWithRange:
- _os_log_create
- _os_signpost_enabled
- _os_signpost_id_generate
- _setBounds:.oldRect.0
- _setBounds:.oldRect.1
- _setBounds:.oldRect.2
- _setBounds:.oldRect.3
- _stringWithValidatedFormat
- _stringWithValidatedFormatArg2
- _stringWithValidatedFormatString
Functions (modified):
~ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc] : 532 -> 252
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:] : 820 -> 292
~ -[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:] : 492 -> 180
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:] : 636 -> 360
~ _OUTLINED_FUNCTION_3 : 36 -> 16
~ -[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:] : 1400 -> 1124
~ -[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:] : 908 -> 596
~ _OUTLINED_FUNCTION_0 : 40 -> 68
~ _OUTLINED_FUNCTION_0 : 72 -> 32
~ _OUTLINED_FUNCTION_0 : 52 -> 32
~ -[AVFigCommChannelUUIDCommunicationChannelManager initWithRoutingContext:] : 332 -> 328
~ -[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:] : 656 -> 372
~ -[AVClientBlockKVONotifier start] : 424 -> 76
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:] : 852 -> 268
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:] : 412 -> 212
~ _AVFigRouteDiscovererAvailableRoutesChanged : 364 -> 68
~ -[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:] : 376 -> 92
~ -[AVOutputContext initWithOutputContextImpl:] : 444 -> 172
~ -[AVOutputDeviceDiscoverySession availableOutputDevices] : 416 -> 120
~ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices] : 364 -> 60
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject] : 1304 -> 524
~ +[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors] : 436 -> 108
~ _AVOutputContextUsesRouteConfigUpdatedNotification : 416 -> 72
~ _AVDefaultRoutingContextFactory : 412 -> 84
~ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:] : 448 -> 184
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:] : 1148 -> 916
~ _AVOutputDeviceDescriptionsFromFigDescriptions : 744 -> 520
~ -[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory] : 376 -> 108
~ _AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode : 408 -> 164
~ ___59-[AVCallbackContextRegistry registerCallbackContextObject:]_block_invoke : 460 -> 112
~ _AVLocalizedError : 4160 -> 2196
~ -[AVMetadataItem(AVMetadataItem_Local) _extractPropertiesFromDictionary:] : 5304 -> 1968
~ -[AVMetadataItem(AVMetadataItem_Local) _valueFromCFType:] : 1216 -> 996
~ +[AVMetadataItem initialize] : 132 -> 12
~ +[AVExecutionEnvironment initialize] : 132 -> 12
~ -[AVWeakReferencingDelegateStorage setDelegate:queue:] : 576 -> 264
~ -[AVFigRoutingContextOutputContextImpl routingContextUUID] : 896 -> 528
~ +[AVCallbackContextRegistry initialize] : 124 -> 68
~ +[AVWeakReferencingDelegateStorage initialize] : 132 -> 12
~ -[AVResourceReclamationController(AVResourceReclamation) permitReclamationWhileSuspended] : 684 -> 400
~ -[AVFigAssetInspectorLoader loadValuesAsynchronouslyForKeys:keysForCollectionKeys:completionHandler:] : 3972 -> 3008
~ _handleFigAssetLoadingNotification : 1164 -> 632
~ -[AVFigAssetInspectorLoader _invokeCompletionHandlerForLoadingBatches:] : 1404 -> 1160
~ ___61-[AVPlayerItem(AVPlayerItemOutputs) _evaluateMetadataOutputs]_block_invoke : 668 -> 464
~ -[AVOutputContext ID] : 336 -> 4
~ -[AVPixelBufferAttributeMediator init] : 220 -> 160
~ -[AVPlayerLoggingIdentifier init] : 532 -> 184
~ -[AVPlayerLooper _setupLoopingReturningError:] : 3680 -> 1748
~ -[AVQueuePlayer insertItem:afterItem:] : 468 -> 172
~ -[AVPlayerLooper _calculateNumberOfCopiesNeeded] : 1920 -> 292
~ -[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:] : 1012 -> 820
~ ___51-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke : 584 -> 240
~ -[AVPlayerLayer layoutSublayers] : 1172 -> 664
~ -[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:] : 512 -> 208
~ _AVSerializeOnQueueAsyncIfNecessary : 948 -> 144
~ -[AVPlayerLayer _notifyPlayerOfDisplaySize] : 388 -> 40
~ -[AVPlayerLayer _displaySize] : 592 -> 260
~ -[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers] : 448 -> 120
~ ___71-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:]_block_invoke : 828 -> 196
~ ___32-[AVPlayerLayer layoutSublayers]_block_invoke : 1936 -> 600
~ -[AVPlayer _closedCaptionLayers] : 548 -> 244
~ ___67-[AVPlayer(AVPlayerMultitaskSupport) _layerForegroundStateChanged:]_block_invoke : 640 -> 144
~ ___64-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke : 552 -> 88
~ -[AVPlayer(PlaybackCoordination) _ensureFigPlaybackCoordinatorIsConnected] : 1040 -> 548
~ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke : 488 -> 172
~ ___67-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoLayersAreAttached]_block_invoke : 504 -> 200
~ ___avplayeritem_fpItemNotificationCallback_block_invoke_2 : 20 -> 32
~ -[AVPlayerItem _configurePlaybackItemAndReturnError:] : 3448 -> 2380
~ -[AVPlayerItem videoComposition] : 372 -> 72
~ -[AVPlayerItem setAudioMix:] : 548 -> 240
~ -[AVPlayerItem setVideoComposition:] : 828 -> 468
~ -[AVPlayerItem initWithAsset:] : 504 -> 212
~ -[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:] : 2236 -> 1628
~ -[AVPlayerItem audioMix] : 556 -> 248
~ _AVTelemetryGenerateID : 68 -> 8
~ -[AVSpecifiedLoggingIdentifier initWithSpecifiedName:] : 992 -> 456
~ -[AVPlayerItem(AVPlayerItemVideoEnhancement) setVideoEnhancementMode:] : 540 -> 280
~ -[AVKVODispatcher observeValueForKeyPath:ofObject:change:context:] : 416 -> 80
~ -[AVKeyPathDependency _reactToSecondLevelPropertyChange:] : 688 -> 176
~ -[AVKeyPathDependency _reactToTopLevelPropertyChange:] : 524 -> 244
~ -[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:] : 1304 -> 760
~ ___59-[AVPlayerItem _updateItemIdentifierForCoordinatedPlayback]_block_invoke : 1160 -> 916
~ -[AVPlayer _setCurrentItem:] : 792 -> 536
~ _AVOutputDeviceImplIsMutedForEndpointID : 468 -> 168
~ ___76-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:]_block_invoke : 392 -> 104
~ ___66-[AVPropertyValuePublisher subscribeRequestingInitialValue:block:]_block_invoke : 416 -> 84
~ -[AVPropertyValuePublisher subscribeRequestingInitialValue:block:] : 664 -> 288
~ ___67-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke_2 : 716 -> 200
~ ___56-[AVMapPublisher subscribeRequestingInitialValue:block:]_block_invoke : 396 -> 88
~ ___67-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke : 668 -> 380
~ ___78-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]_block_invoke_2 : 588 -> 128
~ ___110-[AVPlayer _handleSetRate:withVolumeRampDuration:playImmediately:rateChangeReason:affectsCoordinatedPlayback:]_block_invoke : 1332 -> 912
~ -[AVPlayerItem _seekToTime:toleranceBefore:toleranceAfter:seekID:completionHandler:] : 3056 -> 2320
~ ___31-[AVPlayerItem _updateTimebase]_block_invoke_2 : 1060 -> 796
~ -[AVFigAssetInspectorLoader _statusOfValueForKey:error:firstNonLoadedDependencyKey:] : 1212 -> 940
~ -[AVFigAssetInspectorLoader _loadStatusForProperty:figAsset:error:] : 612 -> 268
~ ___handleFigAssetLoadingNotification_block_invoke : 1836 -> 720
~ +[AVURLAsset _getFigAssetCreationOptionsFromURLAssetInitializationOptions:assetLoggingIdentifier:figAssetCreationFlags:error:] : 5376 -> 4748
~ -[AVPlayerItem(AVPlayerItemOutputs) addOutput:] : 884 -> 568
~ -[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:] : 900 -> 604
~ -[AVPlayerRateState rateStateByUpdatingBasedOnPresenceOfCurrentInterstitialEvent:nameForLogging:] : 520 -> 172
~ -[AVPlayer setAudiovisualBackgroundPlaybackPolicy:] : 520 -> 240
~ -[AVPlayerLayer _notifyPlayerOfLayerForegroundStateChange] : 796 -> 212
~ -[AVPlayerLayer _currentWindowSceneIsForeground] : 676 -> 128
~ -[AVPlayer _updateDecoderPixelBufferAttributes:onFigPlayer:] : 472 -> 180
~ -[AVPlayerLayer pixelBufferAttributes] : 520 -> 232
~ -[AVPlayerLayer init] : 2196 -> 1352
~ -[AVPlayerLayer _currentWindowSceneIsForegroundDefault] : 408 -> 68
~ -[AVPlayerLayer addSublayer:] : 396 -> 140
~ ___54-[AVKeyPathDependency _reactToTopLevelPropertyChange:]_block_invoke : 400 -> 124
~ -[AVKeyPathDependency _startObservingSecondLevelPropertyOnNewCurrentValueForTopLevelDependencyProperty:] : 420 -> 124
~ -[AVWeaklyObservedObjectClientBlockKVONotifier start] : 456 -> 104
~ +[AVFigObjectInspector initialize] : 132 -> 12
~ _handleAndReflectFigAssetNotification : 760 -> 524
~ _AVPlayerGetFigPlayerTypeForAsset : 568 -> 304
~ _AVLoadValueAsynchronously : 128 -> 204
~ _AVLoadValuesAsynchronously : 204 -> 116
~ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_2 : 16 -> 64
~ -[AVPlayerItem selectMediaOption:inMediaSelectionGroup:] : 1044 -> 496
~ -[AVMediaSelectionGroup init] : 204 -> 148
~ -[AVFigAssetInspector _localizedMediaSelectionOptionDisplayNames] : 800 -> 400
~ ___43-[AVPlayerItem _applyMediaSelectionOptions]_block_invoke : 356 -> 108
~ ___56-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]_block_invoke : 392 -> 92
~ ___avplayeritem_fpItemNotificationCallback_block_invoke_3 : 52 -> 20
~ +[AVQueuePlayer initialize] : 140 -> 12
~ _avplayer_fpNotificationCallback : 516 -> 208
~ -[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:] : 1288 -> 672
~ ___avplayer_fpNotificationCallback_block_invoke : 9100 -> 5312
~ -[AVPlayer(AVPlayerInterstitialSupport_Internal) _hasCurrentInterstitialEvent] : 1028 -> 196
~ -[AVPlayerItem _attachToPlayer:] : 1140 -> 276
~ -[AVURLAsset initWithURL:options:] : 428 -> 96
~ -[AVAsset init] : 272 -> 216
~ -[AVFigAssetInspector initWithFigAsset:] : 220 -> 160
~ -[AVAssetTrackInspector _initWithAsset:trackID:trackIndex:] : 192 -> 132
~ -[AVPlayerItem _addToPlayQueueOfFigPlayerOfPlayer:afterFigPlaybackItemOfItem:] : 756 -> 192
~ -[AVPlayerItem _attachToFigPlayer] : 2424 -> 2108
~ -[AVPlayer _itemIsReadyToPlay:] : 184 -> 172
~ -[AVPlayerConnection addItemToPlayQueueAfterPlaybackItemOfItem:] : 1204 -> 564
~ -[AVPlayerItemMediaDataCollector init] : 228 -> 172
~ -[AVFigAssetInspectorLoader initWithURL:figAssetCreationFlags:figAssetCreationOptions:avAssetInitializationOptions:forAsset:figErr:] : 648 -> 344
~ -[AVPlayerLayer setBounds:] : 492 -> 160
~ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5 : 52 -> 20
~ +[AVMovie initialize] : 132 -> 12
~ ___22-[AVPlayer _addLayer:]_block_invoke : 540 -> 208
~ -[AVPlayerLayer _setPlayer:forPIP:] : 1672 -> 656
~ -[AVPlayer(AVPlayerSupportForMediaPlayer) _updateConnectionToSecondScreen] : 668 -> 428
~ -[AVPlayer(AVPlayerMultitaskSupport) _hasAssociatedAVPlayerLayerInPIPMode] : 500 -> 240
~ -[AVPlayer _addLayer:] : 1140 -> 812
~ ___65-[AVPlayerLayer _handleNonForcedSubtitleDisplayDidChange:player:]_block_invoke : 464 -> 104
~ -[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:] : 548 -> 184
~ ___AVPlayerItemVideoOutput_figVCSequentialAvailableCallback_block_invoke_3 : 524 -> 168
~ _AVPerformDelegateCallbackSynchronouslyForDelegateStorageIfCurrentDelegateQueueIsQueueElseDispatchToCurrentDelegateQueue : 1276 -> 216
~ ___61-[AVPlayerItemVideoOutput _dispatchOutputMediaDataWillChange]_block_invoke : 352 -> 96
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl targetAudioSession] : 544 -> 252
~ -[AVPlayerItemOutput _itemTimeForHostTimeAsCMTime:] : 396 -> 136
~ +[AVKeyPathDependency initialize] : 132 -> 12
~ -[AVPlayerItemOutput init] : 296 -> 240
~ -[AVPlayerLayer _stopObservingPlayer:] : 796 -> 232
~ -[AVPlayer(AVPlayerInterstitialSupport_Internal) _linkAndSyncAudioSessionWithInterstitialPlayer:] : 716 -> 504
~ -[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:] : 1232 -> 696
~ +[AVPlayer _createFigPlayerWithType:options:player:] : 948 -> 276
~ _AVEnsureNotOnMainThread : 628 -> 120
~ -[AVResourceReclamationEventObserverToken initWithDetails:] : 392 -> 92
~ +[AVPlayerItemSampleBufferOutput initialize] : 132 -> 12
~ -[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:] : 884 -> 572
~ -[AVTimebaseObserver initWithTimebase:queue:] : 404 -> 344
~ -[AVTimebaseObserver _finishInitializationWithTimerEventHandler:] : 512 -> 216
~ -[AVApplicationStateMonitor init] : 936 -> 592
~ ___avplayeritem_fpItemNotificationCallback_block_invoke : 18988 -> 8252
~ -[AVPlayerItem _unregisterInvokeAndReleasePendingSeekCompletionHandlerForSeekID:finished:] : 536 -> 236
~ -[AVPlayerItem _invokeReadyForEnqueueingHandlers] : 584 -> 296
~ ___79-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeAsSoonAsPossible]_block_invoke : 372 -> 68
~ ___115-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]_block_invoke : 752 -> 140
~ +[AVPlayerLooper initialize] : 132 -> 12
~ -[AVPlayerItemVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:] : 748 -> 364
~ -[AVPlayerLayer _interstitialLayer] : 668 -> 360
~ -[AVAssetLoggingIdentifier init] : 536 -> 188
~ -[AVPlayer _attachVideoLayersToFigPlayer] : 828 -> 532
~ -[AVPlayer _videoLayers] : 548 -> 244
~ +[AVComposition initialize] : 132 -> 12
~ -[AVPlayer(AVPlayerAdvanceWithOverlap) _setSupportsAdvanceTimeForOverlappedPlayback:] : 500 -> 172
~ -[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:] : 1620 -> 880
~ -[AVPlayerItem _presentationSize] : 584 -> 248
~ ___AVPlayerItemVideoOutput_timebaseNotificationCallback_block_invoke : 628 -> 256
~ -[AVPlayerLayer _percentCoverageRelativeToRootLayer] : 480 -> 124
~ -[AVPlayerLayer _setShowInterstitialInstead:afterDelay:] : 840 -> 460
~ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_2 : 28 -> 276
~ -[AVPlayerLayer setLanczosFilterDownscaleFactor:] : 428 -> 144
~ -[AVPlayerLayer copyDisplayedPixelBuffer] : 632 -> 296
~ +[AVPlayerLayer _swapSublayersBetweenPlayerLayer:andPlayerLayer:] : 424 -> 140
~ -[AVPlayerLayer _enterSecondScreenModeRedirectingVideoToLayer:] : 404 -> 140
~ ___63-[AVPlayerLayer _enterSecondScreenModeRedirectingVideoToLayer:]_block_invoke : 436 -> 128
~ -[AVPlayerLayer _leaveSecondScreenModeForLayer:] : 692 -> 160
~ -[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:] : 520 -> 224
~ ___54-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:]_block_invoke : 784 -> 224
~ -[AVPlayerLayer _leavePIPModeForLayer:] : 736 -> 204
~ -[AVPlayerLayer _forceLayout] : 340 -> 8
~ -[AVPlayerLayer _restoreClientLayers:intoMaskLayer:] : 952 -> 456
~ -[AVPlayerLayer setSublayers:] : 340 -> 84
~ -[AVPlayerLayer insertSublayer:atIndex:] : 348 -> 100
~ -[AVPlayerLayer insertSublayer:below:] : 348 -> 100
~ -[AVPlayerLayer insertSublayer:above:] : 348 -> 100
~ -[AVPlayerLayer replaceSublayer:with:] : 348 -> 100
~ -[AVPlayerLayer _windowSceneDidEnterBackground] : 352 -> 24
~ -[AVPlayerLayer _windowSceneWillEnterForeground] : 356 -> 28
~ __avplLoopingItemFailedToPlayToEndTimeNotificationHandler : 448 -> 148
~ ___49-[AVPlayerLooper _changeStatusToFailedWithError:]_block_invoke : 364 -> 92
~ -[AVAssetVariant(SecureCoding) initWithCoder:] : 344 -> 288
~ -[AVAssetVariant(Internal) initWithFigAlternate:] : 172 -> 112
~ -[AVAssetVariantQualifier initWithVariant:] : 148 -> 88
~ -[AVAssetVariantQualifier(SecureCoding) initWithCoder:] : 276 -> 220
~ -[AVAssetVariantQualifierWithPredicate initWithFigAssetVariantQualifierWithPredicate:] : 304 -> 244
~ -[AVAssetVariantQualifierWithPredicate(SecureCoding) initWithCoder:] : 564 -> 508
~ -[AVAssetVariantQualifierForMinimumInKeyPath initWithFigAssetVariantQualifierForMinimumInKeyPath:] : 288 -> 228
~ -[AVAssetVariantQualifierForMinimumInKeyPath(SecureCoding) initWithCoder:] : 288 -> 232
~ -[AVAssetVariantQualifierForMaximumInKeyPath initWithFigAssetVariantQualifierForMaximumInKeyPath:] : 288 -> 228
~ -[AVAssetVariantQualifierForMaximumInKeyPath(SecureCoding) initWithCoder:] : 288 -> 232
~ -[AVAssetVariantPresentationWidthPredicate initWithPresentationWidth:operatorType:] : 224 -> 168
~ -[AVAssetVariantPresentationHeightPredicate initWithPresentationHeight:operatorType:] : 224 -> 168
~ ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_2 : 616 -> 296
~ ___33+[AVURLAsset _avfValidationPlist]_block_invoke : 424 -> 164
~ -[AVURLAsset initWithFigCreationOptions:options:figAssetCreationOptions:figAssetCreationFlags:] : 436 -> 112
~ ___39-[AVURLAsset _ensureAssetDownloadCache]_block_invoke : 364 -> 100
~ ___85-[AVURLAsset(AVURLAssetURLHandlingInternal) _resourceLoaderWithRemoteHandlerContext:]_block_invoke : 384 -> 124
~ -[AVAssetImageGenerator copyCGImageAtTime:actualTime:error:] : 1668 -> 524
~ -[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:] : 940 -> 480
~ -[AVAssetImageGenerator cancelAllCGImageGeneration] : 436 -> 180
~ ___36-[AVAssetImageGenerator _serverDied]_block_invoke : 680 -> 448
~ _avplayer_iapdNotificationCallback : 620 -> 308
~ ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke : 456 -> 160
~ -[AVPlayer _advanceToNextItem] : 736 -> 500
~ -[AVPlayer prepareItem:withCompletionHandler:] : 568 -> 256
~ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2 : 20 -> 3980
~ -[AVPlayer setExpectedAssetTypes:] : 492 -> 200
~ ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke_2 : 520 -> 220
~ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke : 568 -> 328
~ -[AVPlayer setDefaultRate:] : 464 -> 124
~ -[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:] : 700 -> 344
~ -[AVPlayer seekToDate:completionHandler:] : 420 -> 112
~ -[AVPlayer seekToTime:completionHandler:] : 432 -> 168
~ -[AVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:] : 440 -> 188
~ -[AVPlayer _userVolume] : 640 -> 360
~ -[AVPlayer setResourceConservationLevelWhilePaused:] : 616 -> 288
~ -[AVPlayer setPlayerRole:synchronously:] : 1268 -> 540
~ -[AVPlayer setOutputContext:] : 860 -> 352
~ -[AVPlayer removeTimeObserver:] : 504 -> 196
~ -[AVPlayer _detachVideoLayersFromFigPlayer:] : 472 -> 160
~ ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_3 : 644 -> 228
~ _avplayer_fpInterstitialCoordinatorNotificationCallback : 516 -> 208
~ +[AVPlayer fireAvailableHDRModesDidChangeNotification] : 348 -> 88
~ +[AVPlayer fireEligibleForHDRPlaybackDidChangeNotification] : 348 -> 88
~ +[AVPlayer availableHDRModes] : 388 -> 104
~ -[AVPlayer(AVPlayerMultitaskSupport) _canContinuePlaybackInBackgrounBasedOnAudiovisualBackgroundPlaybackPolicy:] : 932 -> 68
~ -[AVPlayer(AVPlayerMultitaskSupport) _shouldDetachVideoLayersFromFigPlayer] : 1176 -> 108
~ -[AVPlayer(AVPlayerMultitaskSupport) _acquireBackgroundAssertion] : 732 -> 216
~ -[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:] : 400 -> 120
~ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke : 468 -> 196
~ -[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:] : 320 -> 4
~ ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2 : 164 -> 156
~ ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_3 : 1100 -> 200
~ -[AVPlayer(AVPlayerMultitaskSupport) _willEnterForeground:] : 416 -> 144
~ -[AVPlayer(AVPlayerPIPSupport) setBackgroundPIPAuthorizationToken:] : 520 -> 240
~ -[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:] : 540 -> 220
~ ___102-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]_block_invoke : 660 -> 364
~ -[AVPlayerRateState rateStateByUpdatingBasedOnFigPlayer:hasCurrentItem:hasCurrentInterstitialEvent:nameForLogging:] : 860 -> 320
~ -[AVPlayer(AVPlayerSpeedRamp) setSupportsSpeedRamps:] : 500 -> 172
~ ___avplayer_iapdNotificationCallback_block_invoke : 752 -> 180
~ _avplayer_playbackcoordinator_SetPlaybackCoordinatorInterstitialActive : 360 -> 56
~ _OUTLINED_FUNCTION_1 : 40 -> 52
~ _avplayerinterstitialeventmonitor_fpNotificationCallback : 856 -> 600
~ -[AVPlayerItem _changeStatusToFailedWithError:] : 788 -> 480
~ _cmTimebaseNotificationCallback_TimeJumped : 380 -> 112
~ -[AVPlayerItem _cancelPendingSeekAndRegisterSeekID:withCompletionHandler:] : 476 -> 244
~ -[AVPlayerItem _postSeekCompletionNotificationWithSeekID:andResult:] : 476 -> 176
~ -[AVPlayerItem seekToDate:completionHandler:] : 584 -> 292
~ -[AVPlayerItem stepByCount:] : 532 -> 252
~ -[AVPlayerItem _setAudioProcessingEffectsAccordingToInputParameters:forTrackID:] : 848 -> 604
~ -[AVPlayerItem _setVideoCompositionInstructions:] : 504 -> 184
~ -[AVPlayerItem customVideoCompositor] : 376 -> 76
~ -[AVPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup:] : 1032 -> 496
~ -[AVPlayerItem _setCurrentMediaSelection:] : 540 -> 260
~ -[AVPlayerItem(AVPlayerItemOutputs) outputs] : 556 -> 248
~ -[AVSampleBufferAudioRendererLoggingIdentifier init] : 532 -> 184
~ -[AVPlayerItemTrack(AVPlayerItemOutputs) addOutput:] : 832 -> 584
~ -[AVPlayerItemTrack(AVPlayerItemOutputs) removeOutput:] : 488 -> 232
~ ___61+[AVAssetDownloadStorageManager sharedDownloadStorageManager]_block_invoke : 104 -> 36
~ -[AVAssetDownloadStorageManager setStorageManagementPolicy:forURL:] : 792 -> 500
~ -[AVQueuePlayer removeItem:] : 356 -> 4
~ -[AVQueuePlayer removeAllItems] : 332 -> 4
~ -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) canOverlapPlaybackFromPlayerItem:toPlayerItem:] : 2400 -> 436
~ -[AVOutputDeviceDiscoverySession setTargetAudioSession:] : 352 -> 56
~ -[AVOutputDeviceDiscoverySession devicePresenceDetected] : 364 -> 40
~ -[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:] : 376 -> 92
~ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:] : 1796 -> 1304
~ -[AVComposition _initWithComposition:] : 744 -> 468
~ -[AVComposition mutableCopyWithZone:] : 360 -> 64
~ -[AVMutableCompositionTrack _insertEmptyTimeRange:fireKVO:] : 696 -> 300
~ -[AVMutableCompositionTrack _removeTimeRange:fireKVO:] : 696 -> 300
~ -[AVMutableCompositionTrack scaleTimeRange:toDuration:] : 760 -> 324
~ _OUTLINED_FUNCTION_1 : 76 -> 72
~ -[AVSampleCursor stepByDecodeTime:wasPinned:] : 1112 -> 596
~ -[AVSampleCursor stepByPresentationTime:wasPinned:] : 1112 -> 596
~ -[AVSampleCursor createSampleBufferForCurrentSampleReturningError:] : 496 -> 216
~ -[AVSampleCursor createSampleBufferFromCurrentSampleToEndCursor:error:] : 516 -> 244
~ -[AVNotificationSubscription cancel] : 616 -> 100
~ -[AVSinkSubscriber cancel] : 388 -> 104
~ +[AVAssetReaderOutput initialize] : 132 -> 12
~ _figAssetReaderSampleBufferDidBecomeAvailable : 428 -> 108
~ _figAssetReaderDecodeError : 372 -> 68
~ _figAssetReaderFailed : 372 -> 68
~ _figAssetReaderServerConnectionDied : 372 -> 68
~ -[AVAssetReaderOutput copyNextSampleBuffer] : 1024 -> 472
~ +[AVAssetWriter initialize] : 132 -> 12
~ -[AVAssetWriter addInputGroup:] : 436 -> 136
~ -[AVAssetWriter startWriting] : 352 -> 56
~ -[AVAssetWriter startSessionAtSourceTime:] : 460 -> 156
~ -[AVAssetWriter endSessionAtSourceTime:] : 460 -> 156
~ -[AVAssetWriter finishWriting] : 352 -> 56
~ -[AVAssetWriter finishWritingWithCompletionHandler:] : 436 -> 136
~ -[AVAssetWriter flush] : 336 -> 40
~ -[AVAssetWriter flushSegment] : 572 -> 284
~ _AVAssetWriterFigAssetWriterHandleServerDiedNotification : 360 -> 68
~ _AVAssetWriterFigAssetWriterHandleCompletedNotification : 360 -> 68
~ _AVAssetWriterFigAssetWriterHandleFailedNotification : 496 -> 216
~ -[AVAssetWriterWritingHelper initWithConfigurationState:assetWriter:error:] : 5780 -> 5144
~ -[AVAssetWriterWritingHelper cancelWriting] : 708 -> 400
~ ___43-[AVAssetWriterWritingHelper finishWriting]_block_invoke : 808 -> 316
~ ___65-[AVAssetWriterWritingHelper finishWritingWithCompletionHandler:]_block_invoke : 328 -> 16
~ ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke : 424 -> 140
~ -[AVAssetWriterFinishWritingHelper _finishWritingOperationsDidFinish] : 468 -> 176
~ -[AVFigAssetWriterFinishWritingAsyncOperation start] : 1188 -> 272
~ -[AVFigAssetWriterFinishWritingAsyncOperation cancel] : 360 -> 76
~ -[AVFigAssetWriterFinishWritingAsyncOperation didEnterTerminalState] : 684 -> 188
~ -[AVFigAssetWriterFinishWritingAsyncOperation didReceiveFigAssetWriterNotificationWithSuccess:error:] : 388 -> 16
~ _AVTimebaseObserver_figTimebaseGetTime : 1380 -> 204
~ -[AVPeriodicTimebaseObserver _fireBlockForTime:] : 436 -> 84
~ -[AVPeriodicTimebaseObserver _handleTimeDiscontinuity] : 820 -> 272
~ -[AVOccasionalTimebaseObserver _fireBlock] : 400 -> 36
~ -[AVOccasionalTimebaseObserver _effectiveRateChanged] : 648 -> 144
~ -[AVOnceTimebaseObserver _fireBlock] : 496 -> 128
~ ___44-[AVOnceTimebaseObserver _resetNextFireTime]_block_invoke : 692 -> 288
~ ___AVTimebaseObserver_timebaseNotificationCallback_block_invoke : 416 -> 140
~ -[AVPlayerItemMetadataCollector initWithIdentifiers:classifyingLabels:] : 292 -> 236
~ -[AVRoutingSessionManager dealloc] : 496 -> 208
~ -[AVRoutingSessionManager likelyExternalDestinations] : 1540 -> 308
~ -[AVRoutingSession dealloc] : 384 -> 96
~ -[AVRoutingSession establishedAutomaticallyFromLikelyDestination] : 1012 -> 252
~ -[AVRoutingSessionDestination dealloc] : 384 -> 96
~ -[AVRoutingSessionDestination outputDeviceDescriptions] : 668 -> 136
~ -[AVRoutingSessionDestination probability] : 608 -> 64
~ -[AVRoutingSessionDestination providesExternalVideoPlayback] : 616 -> 72
~ -[AVAssetWriterInput _prepareToFinishWritingReturningError:] : 352 -> 56
~ -[AVAssetWriterInput requestMediaDataWhenReadyOnQueue:usingBlock:] : 472 -> 180
~ -[AVAssetWriterInput appendSampleBuffer:] : 1064 -> 556
~ -[AVAssetWriterInput markAsFinished] : 440 -> 156
~ -[AVAssetWriterInputWritingHelper observeValueForKeyPath:ofObject:change:context:] : 676 -> 308
~ -[AVAssetWriterInputWritingHelper appendSampleBuffer:error:] : 512 -> 224
~ -[AVAssetWriterInputWritingHelper appendPixelBuffer:withPresentationTime:] : 728 -> 208
~ -[AVAssetWriterInputWritingHelper appendTaggedPixelBufferGroup:withPresentationTime:] : 728 -> 208
~ -[AVAssetWriterInputWritingHelper appendCaption:error:] : 700 -> 180
~ -[AVAssetWriterInputWritingHelper appendCaptionGroup:error:] : 700 -> 180
~ -[AVAssetWriterInputWritingHelper transitionToAndReturnTerminalHelperWithTerminalStatus:] : 656 -> 144
~ ___62-[AVAssetWriterInputInterPassAnalysisHelper startPassAnalysis]_block_invoke : 528 -> 212
~ -[AVAssetWriterInputTerminalHelper appendSampleBuffer:error:] : 540 -> 8
~ -[AVAssetWriterInputTerminalHelper appendPixelBuffer:withPresentationTime:] : 540 -> 8
~ -[AVAssetWriterInputTerminalHelper appendTaggedPixelBufferGroup:withPresentationTime:] : 540 -> 8
~ -[AVAssetWriterInputTerminalHelper appendCaption:error:] : 540 -> 8
~ -[AVAssetWriterInputTerminalHelper appendCaptionGroup:error:] : 540 -> 8
~ ___52-[AVFigAssetWriterTrack _refreshAboveHighWaterLevel]_block_invoke : 476 -> 172
~ -[AVFigAssetWriterTrack endPassWithCompletionHandler:] : 504 -> 220
~ -[AVFigAssetWriterTrack setFormatDescriptions:] : 480 -> 208
~ -[AVAssetWriterInputMediaDataRequester requestMediaDataIfNecessary] : 1128 -> 200
~ -[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:] : 420 -> 116
~ ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke : 532 -> 252
~ -[AVAssetWriterInputFigAssetWriterEndPassOperation dealloc] : 388 -> 104
~ _AVAssetWriterInputFigAssetWriterEndPassOperationPassFinished : 580 -> 308
~ -[AVAssetWriterInputFigAssetWriterEndPassOperation _notifyWhetherMorePassesAreNeeded:timeRanges:forTrackWithID:] : 688 -> 168
~ -[AVVideoComposition init] : 644 -> 364
~ -[AVVideoComposition _copyFigVideoCompositor:andSession:recyclingSession:forFigRemaker:error:] : 664 -> 372
~ -[AVAssetExportSession initWithAsset:presetName:] : 1076 -> 308
~ -[AVAssetExportSession setFileLengthLimit:] : 448 -> 176
~ -[AVAssetExportSession setMaximizePowerEfficiency:] : 400 -> 52
~ -[AVDelegatingPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession] : 652 -> 308
~ -[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:] : 1968 -> 1744
~ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke : 584 -> 312
~ ___60-[AVDelegatingPlaybackCoordinator participantForIdentifier:]_block_invoke : 448 -> 184
~ -[AVDelegatingPlaybackCoordinator beginSuspensionForReason:] : 416 -> 112
~ -[AVDelegatingPlaybackCoordinator _endSuspension:] : 364 -> 20
~ -[AVDelegatingPlaybackCoordinator _endSuspension:proposingNewTime:] : 432 -> 68
~ ___76-[AVDelegatingPlaybackCoordinator applyFigPauseSnapsToMediaTimeOfOriginator]_block_invoke : 456 -> 124
~ _avqsbar_figRendererServerDied : 392 -> 100
~ -[AVSampleBufferAudioRenderer setOutputContext:] : 600 -> 116
~ -[AVSampleBufferAudioRenderer dealloc] : 640 -> 356
~ -[AVSampleBufferAudioRenderer _transitionToStatus:error:] : 488 -> 196
~ -[AVSampleBufferAudioRenderer setAudioOutputDeviceUniqueID:] : 444 -> 116
~ -[AVSampleBufferAudioRenderer audioOutputDeviceUniqueID] : 336 -> 12
~ -[AVSampleBufferAudioRenderer setAudioTimePitchAlgorithm:] : 444 -> 116
~ -[AVSampleBufferAudioRenderer audioTapProcessor] : 332 -> 12
~ -[AVSampleBufferAudioRenderer allowedAudioSpatializationFormats] : 332 -> 12
~ -[AVSampleBufferAudioRenderer volume] : 332 -> 12
~ -[AVSampleBufferAudioRenderer isMuted] : 332 -> 12
~ -[AVSampleBufferAudioRenderer timebase] : 344 -> 52
~ -[AVSampleBufferAudioRenderer setRenderSynchronizer:error:] : 844 -> 300
~ -[AVSampleBufferAudioRenderer setSTSLabel:] : 468 -> 176
~ -[AVSampleBufferAudioRenderer flush] : 452 -> 180
~ -[AVSampleBufferAudioRenderer isReadyForMoreMediaData] : 456 -> 160
~ -[AVSampleBufferAudioRenderer requestMediaDataWhenReadyOnQueue:usingBlock:] : 572 -> 288
~ -[AVSampleBufferAudioRenderer stopRequestingMediaData] : 372 -> 108
~ _OUTLINED_FUNCTION_4 : 32 -> 12
~ -[AVOutputDeviceGroup outputDevices] : 340 -> 8
~ ___112-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _pushTimedMetadataGroups:fromPlayerItemTrack:]_block_invoke_3 : 620 -> 308
~ ___64+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2 : 396 -> 124
~ -[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:] : 604 -> 272
~ -[AVResourceReclamationEvent dealloc] : 376 -> 76
~ -[AVResourceReclamationEventObserverToken dealloc] : 384 -> 80
~ -[AVResourceReclamationAssertion initWithDetails:] : 392 -> 92
~ -[AVResourceReclamationAssertion dealloc] : 384 -> 80
~ -[AVExternalPlaybackMonitor dealloc] : 496 -> 208
~ -[AVSampleBufferVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:] : 800 -> 384
~ -[AVSampleBufferVideoOutput init] : 232 -> 176
~ -[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed] : 400 -> 120
~ ___62-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke : 352 -> 96
~ _OUTLINED_FUNCTION_5 : 16 -> 12
~ ___75-[AVPlayerItemRenderedLegibleOutput _pushRenderedCaptionImages:atItemTime:]_block_invoke : 448 -> 96
~ -[AVPlayerItemRenderedLegibleOutput _signalFlush] : 404 -> 124
~ ___49-[AVPlayerItemRenderedLegibleOutput _signalFlush]_block_invoke : 348 -> 92
~ _AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange : 392 -> 104
~ _AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange : 392 -> 104
~ _AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange : 392 -> 104
~ _AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange : 392 -> 104
~ -[AVFigRouteDescriptorOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:] : 636 -> 372
~ -[AVFigRouteDescriptorOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:] : 636 -> 372
~ _AVOutputDeviceGetFigRouteDescriptor : 444 -> 136
~ -[AVVideoOutputSpecification setOutputSettings:forTagCollection:] : 568 -> 220
~ -[AVPlayerVideoOutput initWithSpecification:] : 248 -> 192
~ -[AVPlayerVideoOutput _handleVideoReceiverActiveConfigurationChanged:] : 596 -> 300
~ -[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:] : 592 -> 292
~ _CMTagCollectionCreateWithVideoOutputPreset : 512 -> 260
~ _figPlaybackItemTrackSampleBufferDidBecomeAvailable : 460 -> 140
~ _figPlaybackItemTrackResetSampleBufferExtraction : 460 -> 140
~ -[AVPlayerItemSampleBufferOutput copyNextSampleBufferForTrackID:flags:] : 1032 -> 240
~ ___109-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:]_block_invoke_2 : 712 -> 108
~ ___103-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke_2 : 712 -> 108
~ _AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange : 428 -> 132
~ -[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:] : 644 -> 184
~ -[AVFigEndpointOutputDeviceImpl deviceType] : 428 -> 140
~ -[AVFigEndpointOutputDeviceImpl deviceSubType] : 360 -> 84
~ -[AVFigEndpointOutputDeviceImpl isAppleAccessory] : 412 -> 100
~ -[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:] : 412 -> 96
~ -[AVFigEndpointOutputDeviceImpl _volumeForEndpointDidChange:forRoomID:] : 652 -> 380
~ -[AVFigEndpointOutputDeviceImpl _mutedDidChangeForEndpointWithID:] : 636 -> 372
~ -[AVFigEndpointOutputDeviceImpl _canMuteDidChangeForEndpointWithID:] : 636 -> 372
~ -[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:] : 412 -> 96
~ -[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:] : 428 -> 112
~ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:] : 528 -> 236
~ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:] : 500 -> 204
~ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:] : 508 -> 208
~ _AVOutputDeviceGetFigEndpoint : 412 -> 96
~ -[AVOutputDeviceTurnByTurnToken initWithEndpoint:] : 536 -> 236
~ -[AVOutputDeviceTurnByTurnToken dealloc] : 500 -> 212
~ -[AVOutputDeviceScreenBorrowToken initWithEndpoint:client:reason:] : 584 -> 280
~ -[AVAssetCustomURLBridgeForNSURLProtocol _cancelPendingRequests] : 520 -> 288
~ -[AVApplicationStateMonitor _didEnterBackground:] : 324 -> 8
~ -[AVApplicationStateMonitor _willEnterForeground:] : 324 -> 8
~ -[AVOutputContext encodeWithCoder:] : 404 -> 116
~ -[AVOutputContext outputDevice] : 360 -> 56
~ -[AVOutputContext outputContextImplOutgoingCommunicationChannelDidBecomeAvailable:] : 812 -> 556
~ -[AVOutputContext outputContextImpl:didExpireWithReplacement:] : 696 -> 372
~ -[AVOutputContextDestinationChange _setStatus:cancellationReason:] : 448 -> 124
~ ___66+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2 : 392 -> 120
~ _AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData : 480 -> 168
~ _AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel : 428 -> 132
~ -[AVFormatReaderInspector initWithFormatReader:] : 168 -> 108
~ -[AVScheduledAudioParameters init] : 172 -> 112
~ +[AVOperation initialize] : 132 -> 12
~ -[AVOperation didEnterTerminalState] : 324 -> 4
~ -[AVOperation markAsCompleted] : 440 -> 152
~ -[AVOperation markAsFailedWithError:] : 452 -> 152
~ -[AVOperation markAsCancelled] : 440 -> 152
~ +[AVOperation(ArrayOfOperations) statusOfOperations:error:] : 616 -> 392
~ -[AVBlockOperation cancel] : 384 -> 56
~ -[AVTrackReaderInspector _initWithAsset:trackID:trackIndex:] : 784 -> 528
~ _handleFigAssetNotification : 472 -> 180
~ -[AVFigAssetTrackInspector _loadStatusForFigAssetTrackProperty:error:] : 628 -> 296
~ -[AVFigAssetTrackInspector _invokeCompletionHandlerForLoadingBatches:] : 564 -> 276
~ ___handleFigAssetTrackNotification_block_invoke : 696 -> 100
~ _AVLocalizedStringFromTableWithLocaleWithBundleIdentifier : 492 -> 248
~ -[AVPlayerCaptionLayer init] : 412 -> 292
~ -[AVPlayerCaptionLayer layoutSublayers] : 1008 -> 436
~ -[AVPlayerCaptionLayer setBounds:] : 488 -> 152
~ -[AVPlayerCaptionLayer setPlayer:] : 492 -> 188
~ -[AVPlayerCaptionLayer _startObservingPlayer:] : 568 -> 260
~ -[AVPlayerCaptionLayer _stopObservingPlayer:] : 528 -> 300
~ -[AVPlayerCaptionLayer setValue:forKeyPath:] : 528 -> 232
~ -[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:] : 780 -> 428
~ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke : 464 -> 56
~ -[AVPlayerCaptionLayer setCaptionContentInsets:] : 644 -> 332
~ -[AVPlayerCaptionLayer _interstitialLayer] : 800 -> 496
~ ___52-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke_2 : 560 -> 216
~ -[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:] : 372 -> 20
~ -[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:] : 372 -> 20
~ -[AVFigRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:] : 440 -> 148
~ -[AVFigRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:] : 596 -> 304
~ _AVFigRoutingContextRouteChangeOperationRouteChangeComplete : 360 -> 68
~ -[AVFigRoutingContextRouteChangeOperation start] : 524 -> 240
~ -[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:] : 440 -> 124
~ ___69-[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:]_block_invoke : 784 -> 92
~ -[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:] : 1156 -> 404
~ ___78-[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]_block_invoke : 584 -> 96
~ -[AVFigRoutingContextRouteChangeOperation _routeChangeComplete] : 552 -> 256
~ -[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation start] : 432 -> 172
~ -[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation _routeConfigUpdateWithID:endedWithReason:] : 1232 -> 272
~ ___63-[AVCallbackContextRegistry unregisterCallbackContextForToken:]_block_invoke : 408 -> 64
~ +[AVMetadataGroup initialize] : 132 -> 12
~ -[AVManagedAssetCache initWithURL:enableCRABSCache:enableHLSCache:] : 536 -> 188
~ -[AVManagedAssetCache setMaxSize:] : 380 -> 92
~ -[AVManagedAssetCache setMaxEntrySize:] : 380 -> 92
~ -[AVManagedAssetCache enableAutomaticCacheSizeManagement] : 348 -> 68
~ -[AVManagedAssetCache removeEntryForKey:] : 364 -> 72
~ -[AVCaptionRenderer init] : 820 -> 220
~ -[AVCaptionRenderer captionSceneChangesInRange:] : 916 -> 384
~ -[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession] : 1324 -> 304
~ -[AVCaptionRenderer teardownFigCaptionClient] : 376 -> 72
~ -[AVCaptionRenderer teardownFigCDS] : 376 -> 72
~ -[AVMediaSelectionOption _updateDisplayNameWithLocale:fallingBackToMatchingUndeterminedAndMultilingual:context:] : 2472 -> 2724
~ -[AVAVAudioSettingsAudioOutputSettings getAudioStreamBasicDescription:forAudioFileTypeID:sourceFormatDescription:] : 3580 -> 2192
~ _AVMediaStatePurgePostMediaStateWasPurgedNotificationForObject : 408 -> 4
~ -[AVCoordinatedPlaybackSuspension initWithCoordinator:reason:] : 492 -> 240
~ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke : 608 -> 332
~ -[AVPlayerPlaybackCoordinator _setInterstitialActive:] : 656 -> 336
~ -[AVPlayerPlaybackCoordinator _reactToNewDelegate] : 372 -> 88
~ -[AVPlayerPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession] : 676 -> 324
~ ___56-[AVPlayerPlaybackCoordinator participantForIdentifier:]_block_invoke : 448 -> 184
~ -[AVPlayerPlaybackCoordinator _updateCoordinationMediumDelegateOnFigPlaybackCoordinator] : 452 -> 88
~ -[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:] : 444 -> 152
~ -[AVPlayerPlaybackCoordinator _updateParticipantStateOnFigPlaybackCoordinatorForItemWithIdentifier:] : 444 -> 152
~ -[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:] : 528 -> 236
~ -[AVPlayerPlaybackCoordinator _synchronizeWorkOnPlayerQueue:] : 424 -> 168
~ -[AVPlayerPlaybackCoordinator _endSuspension:] : 556 -> 256
~ -[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:] : 620 -> 276
~ -[AVPlayerPlaybackCoordinator _updateWaitingPoliciesOnFigPlaybackCoordinator:] : 472 -> 184
~ ___95-[AVPlayerPlaybackCoordinator _updatePauseSnapsToMediaTimeOfOriginatorOnFigPlaybackCoordinator]_block_invoke : 536 -> 236
~ -[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectations] : 716 -> 232
~ _OUTLINED_FUNCTION_2 : 20 -> 12
~ -[AVAssetDownloadSession _common_init] : 236 -> 180
~ -[AVAssetDownloadSession initWithURL:destinationURL:options:] : 2528 -> 1988
~ -[AVAssetDownloadSession initWithDownloadToken:] : 580 -> 292
~ -[AVAssetDownloadSession initWithAsset:mediaSelections:destinationURL:options:] : 808 -> 504
~ -[AVAssetDownloadSession start] : 572 -> 276
~ ___31-[AVAssetDownloadSession pause]_block_invoke : 620 -> 320
~ ___30-[AVAssetDownloadSession stop]_block_invoke : 620 -> 320
~ ___101-[AVAssetDownloadSession(AVAssetDownloadSession_Local) ensureProgressTimerIsRunningOnQueueWithError:]_block_invoke : 416 -> 84
~ ___83-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setupFigClientObjectAsync:]_block_invoke_2 : 600 -> 232
~ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueue] : 696 -> 408
~ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCacheOnDispatchQueue] : 796 -> 272
~ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCache] : 772 -> 220
~ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _readyForInspection] : 384 -> 84
~ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _verifyDownloadConfigurationForAssetType] : 540 -> 288
~ _avAssetDownloadSession_figAssetNotificationCallback : 1360 -> 460
~ _avAssetDownloadSession_figPlaybackItemNotificationCallback : 1032 -> 496
~ -[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed] : 408 -> 128
~ ___60-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke : 352 -> 96
~ -[AVSampleBufferVideoRenderer setControlTimebase:] : 632 -> 320
~ -[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:] : 1124 -> 544
~ -[AVSampleBufferVideoRenderer createVideoQueue:] : 556 -> 112
~ -[AVSampleBufferVideoRenderer _setOutputObscuredDueToInsufficientExternalProtection:] : 836 -> 236
~ -[AVSampleBufferVideoRenderer init] : 2324 -> 1176
~ -[AVSampleBufferVideoRenderer setDisplayLayerVisibility:] : 484 -> 120
~ ___57-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]_block_invoke : 1176 -> 272
~ -[AVSampleBufferVideoRenderer setSTSLabel:] : 484 -> 172
~ -[AVSampleBufferVideoRenderer setReadyForDisplayWithoutKVO:] : 848 -> 568
~ -[AVSampleBufferVideoRenderer removeDisplayLayer] : 468 -> 144
~ -[AVSampleBufferVideoRenderer enqueueSampleBuffer:] : 696 -> 408
~ -[AVSampleBufferVideoRenderer enqueueSampleBuffer:bufferEnqueueingInfo:] : 1192 -> 488
~ __enqueueSingleSampleBufferStatic : 144 -> 52
~ -[AVSampleBufferVideoRenderer _flushComplete] : 532 -> 252
~ -[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:] : 672 -> 316
~ -[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:] : 616 -> 296
~ ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke : 564 -> 52
~ -[AVSampleBufferVideoRenderer requestMediaDataWhenReadyOnQueue:usingBlock:] : 604 -> 304
~ -[AVSampleBufferVideoRenderer addSampleBufferDisplayLayer:] : 1072 -> 412
~ -[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:] : 812 -> 420
~ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke : 448 -> 132
~ -[AVSampleBufferVideoRenderer(PowerOptimization) expectMinimumUpcomingSampleBufferPresentationTime:] : 664 -> 400
~ -[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) addOutput:] : 596 -> 292
~ -[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) removeOutput:] : 592 -> 288
~ -[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) copyDisplayedPixelBuffer] : 556 -> 268
~ ___91-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) copyDisplayedPixelBuffer]_block_invoke : 768 -> 540
~ __figVideoQueueDidDropBelowLowWaterLevel : 444 -> 68
~ __figVideoQueueDecodeError : 808 -> 540
~ __figVideoQueueFlushComplete : 368 -> 68
~ __figVideoQueueCompletedDecodeForPreroll : 436 -> 144
~ __figVideoQueueExternalProtectionStatusChanged : 672 -> 308
~ __figVideoQueueFailed : 472 -> 172
~ __figVideoQueueServerConnectionDied : 404 -> 100
~ __figVideoQueueServerDependencyLost : 404 -> 100
~ __figVideoQueueLostDecoderState : 360 -> 72
~ _OUTLINED_FUNCTION_4 : 28 -> 12
~ -[AVSampleBufferDisplayLayer init] : 936 -> 316
~ -[AVSampleBufferDisplayLayer dealloc] : 500 -> 180
~ -[AVSampleBufferDisplayLayer setBounds:] : 516 -> 76
~ -[AVSampleBufferDisplayLayer layoutSublayers] : 696 -> 400
~ -[AVSampleBufferDisplayLayer layerDidBecomeVisible:] : 440 -> 88
~ -[AVSampleBufferDisplayLayer videoRect] : 764 -> 420
~ -[AVSampleBufferDisplayLayer setSTSLabel:] : 512 -> 160
~ ___42-[AVSampleBufferDisplayLayer setSTSLabel:]_block_invoke : 1032 -> 212
~ -[AVSampleBufferDisplayLayer(AVSampleBufferDisplayLayerQueueManagement) enqueueSampleBuffer:] : 424 -> 148
~ _customURLHandlerHandleRequestCallback : 524 -> 224
~ _customURLHandlerRequestCancelled : 472 -> 164
~ _customURLAuthHandlerHandleRequestCallback : 548 -> 236
~ _customURLAuthHandlerRequestCancelled : 472 -> 164
~ -[AVAssetResourceLoadingDataRequest respondWithData:] : 508 -> 196
~ -[AVAssetResourceLoadingRequest _appendToCachedData:] : 472 -> 120
~ ___53-[AVAssetResourceLoadingRequest _appendToCachedData:]_block_invoke : 452 -> 128
~ -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler] : 388 -> 228
~ -[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:] : 404 -> 76
~ -[AVAssetResourceLoadingRequest _sendFinishLoadingToCustomURLHandlerWithError:] : 592 -> 276
~ -[AVAssetResourceLoadingRequest finishLoading] : 828 -> 372
~ -[AVAssetResourceLoadingRequest finishLoadingWithError:] : 488 -> 212
~ _AVCanWriteFilesToDirectoryAtURL : 668 -> 332
~ -[AVSampleBufferRenderSynchronizer init] : 1576 -> 548
~ _avrendersynchronizer_timebaseRateChanged : 416 -> 68
~ -[AVSampleBufferRenderSynchronizer dealloc] : 1032 -> 516
~ ___49+[AVSampleBufferRenderSynchronizer _makeSTSLabel]_block_invoke : 412 -> 68
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:] : 1092 -> 524
~ ___107-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]_block_invoke_3 : 476 -> 192
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) addRenderer:] : 1168 -> 592
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:] : 576 -> 252
~ ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke : 828 -> 280
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _scheduleTimedRendererRemovalAtTime:atTime:withClientCompletionHandler:] : 1580 -> 304
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _canAddRendererInternal:error:] : 724 -> 232
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _rendererConfigurationIsValid:] : 420 -> 132
~ -[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerTimeObservation) removeTimeObserver:] : 476 -> 180
~ +[AVPlayerItemLegibleOutput initialize] : 132 -> 12
~ ___80-[AVPlayerItemLegibleOutput _pushAttributedStrings:andSampleBuffers:atItemTime:]_block_invoke : 688 -> 108
~ -[AVPlayerItemLegibleOutput _signalFlush] : 408 -> 128
~ ___41-[AVPlayerItemLegibleOutput _signalFlush]_block_invoke : 352 -> 96
~ _AVFigRouteDiscovererRoutePresentChanged : 340 -> 68
~ _AVFigRouteDiscovererEndpointDescriptorChanged : 340 -> 68
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setTargetAudioSession:] : 504 -> 228
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _routePresentChanged] : 344 -> 56
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _endpointDescriptorChanged] : 344 -> 56
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied] : 388 -> 92
~ _OUTLINED_FUNCTION_4 : 16 -> 48
~ -[AVScheduledFloatValueRamp _interpolatedValueAtTime:] : 664 -> 372
~ -[AVAsynchronousCIImageFilteringRequest finishWithImage:context:] : 1152 -> 432
~ -[AVAsynchronousCIImageFilteringRequest finishWithError:] : 372 -> 84
~ +[AVCoreImageFilterCustomVideoCompositor initialize] : 132 -> 12
~ -[AVCoreImageFilterCustomVideoCompositor renderContextChanged:] : 396 -> 116
~ -[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:] : 788 -> 524
~ -[AVCoreImageFilterCustomVideoCompositor cancelAllPendingVideoCompositionRequests] : 552 -> 76
~ -[AVExternalDeviceHID initWithExternalDeviceAndHIDDictionary:hidDictionary:] : 532 -> 236
~ -[AVExternalDeviceIcon initWithDictionary:] : 688 -> 404
~ -[AVExternalDeviceScreenBorrowToken initWithExternalDevice:client:reason:] : 576 -> 272
~ -[AVExternalDeviceScreenBorrowToken dealloc] : 548 -> 244
~ -[AVExternalDeviceTurnByTurnToken initWithExternalDevice:] : 512 -> 220
~ -[AVExternalDeviceTurnByTurnToken dealloc] : 500 -> 212
~ -[AVExternalDevice init] : 196 -> 140
~ -[AVExternalDevice screenIDs] : 520 -> 296
~ -[AVExternalDevice screenInputCapabilities] : 572 -> 348
~ -[AVExternalDevice screenPrimaryInputDevices] : 564 -> 340
~ ___38-[AVExternalDevice externalDeviceHIDs]_block_invoke : 584 -> 344
~ _figEndpointNotificationCallback : 1368 -> 888
~ -[AVCustomVideoCompositorSession initWithVideoComposition:] : 1156 -> 588
~ -[AVCustomVideoCompositorSession commitCustomVideoCompositorPropertiesAndReturnError:] : 1560 -> 1068
~ ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_2 : 580 -> 300
~ ___123-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _customCompositorFigPropertyDidChange]_block_invoke : 356 -> 76
~ -[AVClientBlockKVONotifier dealloc] : 488 -> 156
~ -[AVWeaklyObservedObjectClientBlockKVONotifier cancelCallbacks] : 444 -> 120
~ ___49-[AVVideoCompositionRenderContext newPixelBuffer]_block_invoke : 708 -> 388
~ -[AVVideoCompositionRenderContext(Internal) initWithFigVideoCompositor:clientRequiredPixelBufferAttributes:videoComposition:pixelBufferPool:] : 3616 -> 1044
~ -[AVVideoCompositionRenderContext(Internal) pixelBufferPool] : 944 -> 644
~ +[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext] : 424 -> 164
~ +[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls] : 572 -> 316
~ ___72-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]_block_invoke : 680 -> 232
~ -[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:] : 596 -> 268
~ -[AVFigRoutingContextOutputContextImpl _currentRouteChanged] : 348 -> 60
~ -[AVFigRoutingContextOutputContextImpl _groupConfigurationChanged] : 360 -> 72
~ -[AVFigRoutingContextOutputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:] : 804 -> 524
~ -[AVFigRoutingContextOutputContextImpl _systemPickerVideoRouteChanged] : 344 -> 56
~ -[AVFigRoutingContextOutputContextImpl associatedAudioDeviceID] : 724 -> 184
~ -[AVFigRoutingContextOutputContextImpl _createSelectRouteOptionsForSetOutputDeviceOptions:] : 1272 -> 968
~ -[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:] : 428 -> 124
~ -[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:] : 752 -> 480
~ -[AVFigRoutingContextOutputContextImpl removeOutputDevice:options:completionHandler:] : 760 -> 488
~ -[AVFigRoutingContextOutputContextImpl _canUseForRoutingContextDidChangeForRoutingContextWIthID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _masterVolumeDidChangeForRoutingContextWithID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _canSetMasterVolumeDidChangeForRoutingContextWithID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _canMuteDidChangeForRoutingContextWithID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _muteDidChangeForRoutingContextWithID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _masterVolumeControlTypeDidChangeForRoutingContextWithID:] : 392 -> 96
~ -[AVFigRoutingContextOutputContextImpl _serverConnectionDied] : 416 -> 144
~ -[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel] : 1100 -> 600
~ ___79-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke : 736 -> 232
~ -[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:] : 608 -> 280
~ -[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:] : 592 -> 272
~ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:] : 776 -> 260
~ ___119-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke : 356 -> 84
~ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:] : 728 -> 480
~ ___120-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ ___119-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:] : 536 -> 220
~ ___124-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:] : 776 -> 260
~ ___126-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke : 356 -> 84
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:] : 728 -> 480
~ ___127-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ ___126-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:] : 536 -> 220
~ ___131-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke : 344 -> 68
~ _AVOutputContextManagerServerConnectionDied : 588 -> 384
~ -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:] : 680 -> 368
~ _OUTLINED_FUNCTION_14 : 52 -> 12
~ _OUTLINED_FUNCTION_15 : 32 -> 12
~ _OUTLINED_FUNCTION_23 : 44 -> 28
~ -[AVMovie init] : 944 -> 616
~ -[AVMovie initWithURL:options:] : 836 -> 512
~ -[AVMovie initWithData:options:] : 1064 -> 752
~ -[AVMovie _initWithFigAsset:] : 544 -> 216
~ -[AVMovie _initWithFormatReader:URL:data:options:] : 884 -> 548
~ -[AVMovie _initWithFigError:userInfo:] : 584 -> 244
~ -[AVMutableMovie initWithURL:options:error:] : 1348 -> 744
~ -[AVMutableMovie initWithSettingsFromMovie:options:error:] : 1164 -> 564
~ -[AVMutableMovie setPreferredTransform:] : 500 -> 216
~ -[AVContentKeyRequest initWithContentKeySession:reportGroup:identifier:contentIdentifier:keyIDFromInitializationData:initializationData:preloadingRequestOptions:providesPersistableKey:] : 1020 -> 924
~ -[AVContentKeyRequest initWithContentKeySession:reportGroup:customURLHandler:identifier:requestInfo:requestID:providesPersistableKey:isRenewalRequest:] : 952 -> 900
~ -[AVContentKeyRequest initWithContentKeySession:contentKeyBoss:useContentKeyBoss:keySpecifier:initializationData:keyIDFromInitializationData:contentIdentifier:isRenewalRequest:requestID:providesPersistableKey:preloadingRequestOptions:identifier:supportsOfflineKey:] : 596 -> 544
~ +[AVContentKeySession copyDefaultSecureStopManagerForAppIdentifier:storageDirectoryAtURL:] : 476 -> 188
~ ___83-[AVContentKeySession externalProtectionStateChangedCallbackWithBoss:keySpecifier:]_block_invoke : 520 -> 236
~ -[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequests:forInitializationData:] : 960 -> 488
~ -[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequest:toDelegateWithCallbackSelector:] : 692 -> 216
~ ___89-[AVContentKeySession(AVContentKeyRequestSupport) contentKeyRequestDidProduceContentKey:]_block_invoke : 404 -> 400
~ ___89-[AVContentKeySession(AVContentKeyRequestSupport) contentKeyRequestDidProduceContentKey:]_block_invoke_2 : 652 -> 392
~ -[AVContentKeySession(AVContentKeySession_Internal) issueContentKeyRequestForInitializationData:] : 664 -> 384
~ _customURLHandlerHandleRequestCallback : 500 -> 192
~ -[AVContentKeyReportGroup failProcessingContentKeyRequestWithIdentifier:initializationData:error:] : 440 -> 156
~ _avckrg_keyResponseErrorCallback : 456 -> 148
~ _avckrg_keyResponseSuccessfullyProcessedCallback : 440 -> 132
~ _avckrg_persistentKeyUpdatedCallback : 436 -> 132
~ _avckrg_secureStopDidFinalizeRecordCallback : 396 -> 108
~ _avckrg_externalProtectionStateChangedCallback : 404 -> 124
~ -[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:] : 536 -> 240
~ _OUTLINED_FUNCTION_16 : 28 -> 36
~ _OUTLINED_FUNCTION_17 : 12 -> 36
~ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:] : 408 -> 104
~ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:] : 404 -> 64
~ -[AVRouteDetector _updateMultipleRoutesDetected] : 1112 -> 324
~ -[AVRouteDetector _updateRouteDetectionEnabled] : 1912 -> 556
~ ___47-[AVRouteDetector _updateRouteDetectionEnabled]_block_invoke : 620 -> 120
~ -[AVStreamDataParser init] : 416 -> 84
~ -[AVStreamDataParser dealloc] : 508 -> 232
~ -[AVStreamDataParser providePendingMediaData] : 488 -> 232
~ -[AVStreamDataParser setShouldProvideMediaData:forTrackID:] : 604 -> 400
~ -[AVStreamDataParser _createAssetIfNecessary] : 1168 -> 708
~ +[AVStreamDataParser(AVStreamDataParser_FigManifold) _createBlockBufferUsingNSData:withOffset:withLength:] : 428 -> 72
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:pushedSampleBuffer:trackID:flags:] : 2020 -> 952
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:] : 3708 -> 1892
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _registerForFigManifoldCallbacksForTrackID:] : 456 -> 196
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _unregisterForFigManifoldCallbacksForTrackID:] : 452 -> 176
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifoldAllNewTracksReady:] : 320 -> 4
~ __figManifoldError : 352 -> 8
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _createFigManifoldWithBlockBuffer:manifold:] : 400 -> 120
~ -[AVStreamDataParser(AVStreamDataParser_ContentKeySessionDelegate) contentKeySession:didProvideContentKeyRequest:] : 452 -> 160
~ ___84-[AVStreamDataParser(AVStreamDataParserSandboxedParsing) setPreferSandboxedParsing:]_block_invoke : 416 -> 92
~ -[AVMetadataItem(AVMetadataItem_Local) _valueFromCFType:].cold.1 : 112 -> 56
~ _appendCaptionGroupToQueue.cold.1 : 124 -> 72
~ -[AVURLAsset(AVURLAssetContentKeyEligibilityInternal) _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:] : 1080 -> 1028
~ -[AVAssetImageGenerator _ensureFigAssetImageGeneratorAllowingSynchronousPropertyLoad:error:] : 816 -> 536
~ -[AVOutputDeviceHID setInputMode:] : 468 -> 508
~ -[AVPlayer _removeItem:] : 720 -> 536
~ -[AVPlayerItem _applyCurrentVideoComposition] : 1300 -> 792
~ ___63-[AVAssetDownloadStorageManager storageManagementPolicyForURL:]_block_invoke : 436 -> 136
~ -[AVMutableComposition insertEmptyTimeRange:] : 492 -> 264
~ -[AVMutableComposition removeTimeRange:] : 492 -> 264
~ -[AVMutableComposition scaleTimeRange:toDuration:] : 768 -> 388
~ -[AVMutableComposition _addMutableTrackWithMediaType:preferredTrackID:fireKVO:] : 608 -> 344
~ -[AVMutableComposition _removeTrack:fireKVO:] : 660 -> 408
~ -[AVMutableComposition mutableTrackCompatibleWithTrack:] : 960 -> 508
~ -[AVMutableCompositionTrack setSegments:] : 756 -> 540
~ -[AVMutableCompositionTrack _insertTimeRange:ofTrack:atTime:fireKVO:error:] : 1128 -> 612
~ -[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:].cold.1 : 160 -> 80
~ +[AVRoutingSessionManager longFormVideoRoutingSessionManager] : 440 -> 116
~ -[AVRoutingSessionManager initWithFigRoutingSessionManager:] : 536 -> 256
~ _AVRoutingSessionManagerGetLikelyDestinationsFromFig : 596 -> 312
~ -[AVRoutingSession destination] : 556 -> 204
~ -[AVSampleBufferAudioRenderer _installNotificationHandlers] : 492 -> 276
~ -[AVSampleBufferAudioRenderer _uninstallNotificationHandlers] : 432 -> 232
~ -[AVSampleBufferAudioRenderer setAudioTapProcessor:] : 372 -> 232
~ -[AVSampleBufferAudioRenderer setVolume:] : 496 -> 240
~ -[AVSampleBufferAudioRenderer setMuted:] : 396 -> 216
~ -[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:] : 432 -> 120
~ _AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImplHandleEvent : 696 -> 488
~ -[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:] : 480 -> 180
~ +[AVExternalPlaybackMonitor longFormVideoExternalPlaybackMonitor] : 536 -> 116
~ -[AVExternalPlaybackMonitor initWithFigRoutingSessionManager:] : 688 -> 256
~ _AVResetMediaServices.cold.1 : 112 -> 8
~ _AVResetMediaServices.cold.2 : 112 -> 8
~ -[AVOutputDeviceFrecentsReader initWithFrecentsFilePath:error:] : 740 -> 780
~ -[AVOutputDeviceAuthorizedPeer initWithID:publicKey:hasAdministratorPrivileges:] : 192 -> 180
~ -[AVFigRouteDescriptorOutputDeviceImpl _withEndpoint:] : 960 -> 892
~ -[AVFigRouteDescriptorOutputDeviceImpl setCurrentBluetoothListeningMode:error:] : 864 -> 860
~ -[AVOutputDeviceViewAreaInfo initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:] : 476 -> 164
~ -[AVOutputDeviceScreenInfo initWithDict:] : 1388 -> 1168
~ -[AVOutputContext initWithCoder:] : 444 -> 188
~ -[AVFigAssetInspector variants] : 524 -> 212
~ -[AVOutputDeviceIcon initWithDict:] : 688 -> 396
~ -[AVCaptionRenderer renderInContext:atTime:] : 904 -> 248
~ -[AVPlayerPlaybackCoordinator _setIntegratedTimelineCreatingNew:] : 460 -> 192
~ -[AVSampleBufferVideoRenderer setRenderSynchronizer:error:] : 856 -> 220
~ _customURLHandlerRequestCancelled.cold.2 : 108 -> 4
~ -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler].cold.1 : 764 -> 756
~ -[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:].cold.1 : 212 -> 224
~ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied].cold.1 : 284 -> 288
~ -[AVAsynchronousCIImageFilteringRequest finishWithImage:context:].cold.2 : 68 -> 80
~ +[AVFigRoutingContextOutputContextImpl platformDependentScreenOrVideoContext] : 308 -> 304
~ -[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:] : 440 -> 160
~ -[AVFigRoutingContextOutputContextImpl _routeConfigUpdateStartedWithID:] : 164 -> 160
~ +[AVFigRoutingContextOutputContextImpl resetOutputDeviceForAllOutputContexts] : 372 -> 432
~ -[AVFigRoutingContextOutputContextImpl _remoteControlChannelAvailabilityChanged] : 448 -> 220
~ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:] : 584 -> 208
~ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:] : 420 -> 204
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:] : 548 -> 212
~ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:] : 420 -> 204
~ -[AVContentKeySession processContentKeyRequestForTransportStreamWithCodecType:initializationData:groupID:options:] : 296 -> 292
~ -[AVContentKeySession(AVContentKeySession_Internal) _handleRequest:withRequestID:fromHandler:willHandleRequest:] : 1068 -> 1084
~ ___152-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) createCryptorIfNecessaryForIdentifier:initializationData:formatDescription:hlsMethod:error:]_block_invoke : 392 -> 304
~ ___105-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) copyCryptorForIdentifier:initializationData:]_block_invoke : 316 -> 232
~ -[AVContentKeyRequest initWithContentKeySession:reportGroup:identifier:contentIdentifier:keyIDFromInitializationData:initializationData:preloadingRequestOptions:providesPersistableKey:].cold.1 : 124 -> 60
~ +[AVContentKeySession(AVContentKeySessionPendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:].cold.1 : 108 -> 8
~ _avckrg_secureStopDidFinalizeRecordCallback.cold.1 : 108 -> 8
~ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:] : 676 -> 392
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:trackDidEnd:] : 532 -> 260
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:discoveredNewTrackID:mediaType:] : 664 -> 304
~ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.1 : 152 -> 76

Functions (added):
+ ___21-[AVPlayerLayer init]_block_invoke_5
+ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke_2
+ ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke_3
+ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3
+ ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke_2
+ ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_3
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_6
+ ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke_2
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.480
+ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_3
+ ___22-[AVPlayer _addLayer:]_block_invoke_2
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2
+ ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_5
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke_2
+ ___avplayer_iapdNotificationCallback_block_invoke_3
+ ___avplayer_iapdNotificationCallback_block_invoke_4
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_13
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_29
+ -[AVRoutingSessionManager currentRoutingSession]
+ -[AVRoutingSessionManager prefersLikelyDestinationsOverCurrentRoutingSession]
+ ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_3
+ -[AVSampleBufferAudioRenderer outputContext]
+ ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_3
+ -[AVExternalPlaybackMonitor isAirPlayVideoActive]
+ -[AVExternalPlaybackMonitor isAirPlayVideoPlaying]
+ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_3
+ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_3
+ ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke_2
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]
+ -[AVExternalDeviceHID _figEndpointHIDInputMode]
+ -[AVExternalDeviceHID setInputMode:]
+ -[AVExternalDevice _figEndpointPropertyValueForKey:]
+ -[AVAssetWriterWritingHelper storageSpacePreallocationSize]
+ -[AVSampleBufferAudioRenderer setOutputContext:].cold.1
+ -[AVMutableMovieTrack setPreferredTransform:]
+ -[AVMutableMovieTrack setLayer:]
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.4

Functions (removed):
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_31
- ___handleFigAssetLoadingNotification_block_invoke.528
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2
- -[AVPlayer _insertItem:afterItem:]
- _avurlasset_setupGuts
- -[AVFigAssetTrackInspector _initWithAsset:trackID:trackIndex:]
- _figLoaderNotificationHandler
- -[AVPlayerItemVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:]
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke
- -[AVAsset mediaSelectionGroupForPropertyList:mediaSelectionOption:]
- _OUTLINED_FUNCTION_25
- ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_4
- _assetTrackNotificationHandler
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.449
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.470
- -[AVPlayer replaceCurrentItemWithPlayerItem:]
- -[AVPlayer _copyDisplayedPixelBuffer:]
- -[AVPlayer(AVPlayerMultitaskSupport) _applicationHasExternallyDisplayedAVPlayerLayerAndIsUnderDeviceLock]
- -[AVPlayer(AVPlayerMultitaskSupport) _itemOkayToPlayWhileTransitioningToBackground:]
- -[AVPlayer(AVPlayerSupportForMediaPlayer) _resumePlayback:error:]
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1098
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke
- ___avplayer_iapdNotificationCallback_block_invoke.1313
- -[AVPlayerItem _makeReadyForEnqueueingWithCompletionHandler:]
- -[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]
- -[AVPlayerItem _currentMediaSelectionFromFigSelectedMediaArray:]
- ___avplayeritem_fpItemNotificationCallback_block_invoke_5.1506
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_6
- -[AVMutableComposition insertTimeRange:ofAsset:atTime:error:]
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- -[AVMutableCompositionTrack validateTrackSegments:error:]
- -[AVAssetWriterWritingHelper storageSpacePreallocationSize]
- _OUTLINED_FUNCTION_2
- -[AVPeriodicTimebaseObserver _resetNextFireTime]
- [4 functions removed in block]
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- -[AVAssetWriterInput respondToEachPassDescriptionOnQueue:usingBlock:]
- ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke.908
- -[AVVideoCompositionInstruction dictionaryRepresentation]
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.109
- ___99-[AVDelegatingPlaybackCoordinator _updateTransportControlStateDictionaryWithTransportControlState:]_block_invoke
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_8
- [4 functions removed in block]
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_17
- -[AVOutputDevice openCommunicationChannelToDestination:options:completionHandler:]
- -[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]
- ___86-[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke
- _OUTLINED_FUNCTION_5
- sub_1954ed018
- ___146-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke
- -[AVPlayerVideoOutput hasNewTaggedBufferGroupForHostTime:]
- ___55-[AVPlayerVideoOutput _attachToPlayer:exceptionReason:]_block_invoke
- -[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]
- -[AVFigEndpointOutputDeviceImpl connectedPairedDevices]
- sub_1954f5714
- -[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]
- ___79-[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke
- -[AVOutputContext outputContextImpl:didCloseCommunicationChannel:]
- -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- -[AVMutableMovieTrack setAlternateGroupID:]
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_7
- [3 functions removed in block]
- -[AVScheduledAudioParameters initWithPropertyList:]
- -[AVScheduledAudioParameters(AVScheduledAudioParameters_Internal) _setRamp:]
- ___Block_byref_object_copy_.15
- ___62-[AVOperation _setStatus:error:resultingStatus:failureReason:]_block_invoke
- -[AVFigAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:]
- _OUTLINED_FUNCTION_1
- _AVRouteConfigUpdatedFigRoutingContextRouteChangeOperationRouteConfigUpdated
- -[AVDateRangeMetadataGroup(AVDateRangeMetadataGroup_Local) _extractPropertiesFromTaggedRangeMetadataDictionary:]
- [3 functions removed in block]
- -[AVAssetDownloadContentConfiguration _createFigContentConfigForEnvironmentalCondition:]
- ___57-[AVPlayerPlaybackCoordinator setFigPlaybackCoordinator:]_block_invoke_2
- ___95-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryWithTransportControlState:]_block_invoke
- [4 functions removed in block]
- ___83-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeWithAdvanceInterval:]_block_invoke
- ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.115
- ___72-[AVSampleBufferVideoRenderer enqueueSampleBuffer:bufferEnqueueingInfo:]_block_invoke
- -[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke
- _OUTLINED_FUNCTION_5
- ___123-[AVSampleBufferDisplayLayer _updateLayerTreeGeometryWithVideoGravity:presentationSize:videoGravityShouldTriggerAnimation:]_block_invoke
- -[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:]
- ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke.201
- _avrendersynchronize_electRendererForSTSAndSendLabelToAudioRenderers
- -[AVAssetWriterInputAnnotationAdaptor appendAnnotation:]
- _OUTLINED_FUNCTION_1
- -[AVFigCommChannelUUIDCommunicationChannelManager openCommunicationChannelWithOptions:error:]
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_25
- [3 functions removed in block]
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_39
- -[AVMutableMovie initWithData:options:error:]
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_15
- [6 functions removed in block]
- [5 functions removed in block]
- -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _showAuthPromptWithUniqueID:routeDescriptor:pinMode:reason:]
- -[AVStreamDataParser _appendStreamData:withFlags:]
- _OUTLINED_FUNCTION_4
- _avplayer_iapdNotificationCallback.cold.1
- -[AVRoutingSessionDestination initWithFigRoutingSessionDestination:]
- -[AVPlayerVideoOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue]
- -[AVOutputContext outputContextImplDidChangeGlobalOutputDeviceConfiguration:].cold.1
- -[AVPlayerPlaybackCoordinator _applyIntegratedTimelineSeek:]
- -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:options:]
- -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueueFirstTime]
- [3 functions removed in block]
- [4 functions removed in block]
- -[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:].cold.1
- -[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:].cold.1
- +[AVOutputContext(AVAudioSession) preferredOutputDevicesForAudioSession:]
- -[AVExternalDeviceHID setInputMode:]
- +[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]
- -[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]
- -[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]
- -[AVContentKeyRequest _handleKeyResponseError:]
- -[AVContentKeyRequest ensureCryptorWithFormatDescription:error:]
- -[AVContentKeyRequest _finishLoadingCustomURLRequestWithResponseData:renewalDate:]
- [5 functions removed in block]
- -[AVContentKeySession(AVContentKeySession_Internal) createAndInstallCustomURLHandlerForAsset:outHandler:]
- -[AVContentKeyReportGroup cryptorOptionsForIdentifier:initializationData:formatDescription:hlsMethod:]
- [3 functions removed in block]
- [6 functions removed in block]
- -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus].cold.4
- [8 functions removed in block]
- [7 functions removed in block]
CStrings:
+ "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4"
+ "avplayer_fpNotificationCallback_block_invoke_14"
- "\n\t\"%@\""
- " "
- "%02x"
- "%c"
- "%d bytes [ %@ ] [ %@ ]"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "(Fig)"
- "(OSStatus)error.code"
- "*** SHOULD NOT receive kFigAssetNotification_PropertyRevised / kFigStdAssetProperty_Duration notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigAssetTrackProperty_EditSegmentData notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigStdTrackProperty_TimeRange notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "+[AVAnnotationRepresentation _annotationRepresentationWithPropertyList:binaryData:]"
- "+[AVAssetTrackInspector assetTrackInspectorWithAsset:trackID:trackIndex:]"
- "+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke"
- "+[AVContentKeySession copyDefaultSecureStopManagerForAppIdentifier:storageDirectoryAtURL:]"
- "+[AVDataAsset _getFigAssetCreationOptionsFromDataAssetInitializationOptions:figAssetCreationFlags:]"
- "+[AVExternalPlaybackMonitor longFormVideoExternalPlaybackMonitor]"
- "+[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]"
- "+[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]"
- "+[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]"
- "+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
- "+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
- "+[AVMetadataItemFilterForSharing addIdentifier:toWhitelistDictionary:]"
- "+[AVOperation(ArrayOfOperations) statusOfOperations:error:]"
- "+[AVOutputContext defaultOutputContextImplClass]"
- "+[AVOutputContext(AVAudioSession) preferredOutputDevicesForAudioSession:]"
- "+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2"
- "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:]"
- "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:]"
- "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:]"
- "+[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors]"
- "+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2"
- "+[AVPlayer _createFigPlayerWithType:options:player:]"
- "+[AVPlayer availableHDRModes]"
- "+[AVPlayer fireAvailableHDRModesDidChangeNotification]"
- "+[AVPlayer fireEligibleForHDRPlaybackDidChangeNotification]"
- "+[AVPlayerItem _createFigPlaybackItemForFigPlayer:asset:URL:flags:options:playbackItem:]"
- "+[AVPlayerLayer _swapSublayersBetweenPlayerLayer:andPlayerLayer:]"
- "+[AVRoutingSessionManager longFormVideoRoutingSessionManager]"
- "+[AVSampleBufferRenderSynchronizer _makeSTSLabel]_block_invoke"
- "+[AVStreamDataParser(AVStreamDataParser_FigManifold) _createBlockBufferUsingNSData:withOffset:withLength:]"
- "+[AVURLAsset _avfValidationPlist]_block_invoke"
- "+[AVURLAsset _getFigAssetCreationOptionsFromURLAssetInitializationOptions:assetLoggingIdentifier:figAssetCreationFlags:error:]"
- ", associatedLayer %p"
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
- "-[AVAssetLoggingIdentifier init]"
- "-[AVAssetMediaSelectionGroup _mediaSelectionOptionWithPropertyList:matchToMediaSelectionArray:]"
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
- "-[AVAssetResourceLoadingRequest finishLoading]"
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
- "-[AVAssetWriterFinishWritingHelper initWithConfigurationState:finishWritingOperations:figAssetWriterCallbackContextToken:figAssetWriter:]_block_invoke"
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
- "-[AVCaptionRenderer teardownFigCDS]"
- "-[AVCaptionRenderer teardownFigCaptionClient]"
- "-[AVClientBlockKVONotifier cancelCallbacks]"
- "-[AVClientBlockKVONotifier dealloc]"
- "-[AVClientBlockKVONotifier start]"
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
- "-[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]"
- "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]"
- "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]_block_invoke"
- "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]"
- "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
- "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]"
- "-[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]"
- "-[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:]"
- "-[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:]"
- "-[AVFigEndpointOutputDeviceImpl connectedPairedDevices]"
- "-[AVFigEndpointOutputDeviceImpl deviceSubType]"
- "-[AVFigEndpointOutputDeviceImpl deviceType]"
- "-[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]"
- "-[AVFigEndpointOutputDeviceImpl isAppleAccessory]"
- "-[AVFigEndpointOutputDeviceImpl isInEar]"
- "-[AVFigEndpointOutputDeviceImpl isInUseByPairedDevice]"
- "-[AVFigEndpointOutputDeviceImpl supportsDataOverACLProtocol]"
- "-[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]"
- "-[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]"
- "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _finishedWithPrompt]"
- "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:]"
- "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:]"
- "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
- "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
- "-[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
- "-[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _endpointDescriptorChanged]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _routePresentChanged]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setTargetAudioSession:]"
- "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl targetAudioSession]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification addPeerToHomeGroup:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:]"
- "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup]"
- "-[AVFigRoutingContextOutputContextImpl _canMuteDidChangeForRoutingContextWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _canSetMasterVolumeDidChangeForRoutingContextWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _canUseForRoutingContextDidChangeForRoutingContextWIthID:]"
- "-[AVFigRoutingContextOutputContextImpl _createSelectRouteOptionsForSetOutputDeviceOptions:]"
- "-[AVFigRoutingContextOutputContextImpl _currentRouteChanged]"
- "-[AVFigRoutingContextOutputContextImpl _groupConfigurationChanged]"
- "-[AVFigRoutingContextOutputContextImpl _masterVolumeControlTypeDidChangeForRoutingContextWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _masterVolumeDidChangeForRoutingContextWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _muteDidChangeForRoutingContextWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _remoteControlChannelAvailabilityChanged]"
- "-[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:]"
- "-[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:]"
- "-[AVFigRoutingContextOutputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]"
- "-[AVFigRoutingContextOutputContextImpl _serverConnectionDied]"
- "-[AVFigRoutingContextOutputContextImpl _systemPickerVideoRouteChanged]"
- "-[AVFigRoutingContextOutputContextImpl addOutputDevice:options:completionHandler:]"
- "-[AVFigRoutingContextOutputContextImpl associatedAudioDeviceID]"
- "-[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:]"
- "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]"
- "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]_block_invoke"
- "-[AVFigRoutingContextOutputContextImpl outputDevice]"
- "-[AVFigRoutingContextOutputContextImpl removeOutputDevice:options:completionHandler:]"
- "-[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:]"
- "-[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:]"
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
- "-[AVOutputContext ID]"
- "-[AVOutputContext encodeWithCoder:]"
- "-[AVOutputContext initWithCoder:]"
- "-[AVOutputContext initWithOutputContextImpl:]"
- "-[AVOutputContext outputContextImpl:didExpireWithReplacement:]"
- "-[AVOutputContext outputDevice]"
- "-[AVOutputContext outputDevices]"
- "-[AVOutputContext predictedOutputDevice]"
- "-[AVOutputContextDestinationChange _setStatus:cancellationReason:]"
- "-[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:]"
- "-[AVOutputDevice openCommunicationChannelWithOptions:completionHandler:]"
- "-[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:]"
- "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]"
- "-[AVOutputDeviceAuthorizationSession setDelegate:]"
- "-[AVOutputDeviceDiscoverySession availableOutputDevices]"
- "-[AVOutputDeviceDiscoverySession devicePresenceDetected]"
- "-[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:]"
- "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:]"
- "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:]"
- "-[AVOutputDeviceDiscoverySession setTargetAudioSession:]"
- "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices]"
- "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices recentlyUsedDevices]"
- "-[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:]"
- "-[AVOutputDeviceGroup outputDevices]"
- "-[AVOutputDeviceHID initWithUUID:screenUUID:endpoint:]"
- "-[AVOutputDeviceIcon initWithDict:]"
- "-[AVOutputDeviceScreenBorrowToken initWithEndpoint:client:reason:]"
- "-[AVOutputDeviceScreenInfo initWithDict:]"
- "-[AVOutputDeviceTurnByTurnToken dealloc]"
- "-[AVOutputDeviceTurnByTurnToken initWithEndpoint:]"
- "-[AVOutputDeviceViewAreaInfo initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:]"
- "-[AVPeriodicTimebaseObserver _effectiveRateChanged]"
- "-[AVPeriodicTimebaseObserver _fireBlockForTime:]"
- "-[AVPeriodicTimebaseObserver _handleTimeDiscontinuity]"
- "-[AVPeriodicTimebaseObserver _resetNextFireTime]"
- "-[AVPlayer _addLayer:]"
- "-[AVPlayer _addLayer:]_block_invoke"
- "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]"
- "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke"
- "-[AVPlayer _attachVideoLayersToFigPlayer]"
- "-[AVPlayer _closedCaptionLayers]"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3"
- "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6"
- "-[AVPlayer _detachVideoLayersFromFigPlayer:]"
- "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]"
- "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke"
- "-[AVPlayer _handleSetRate:withVolumeRampDuration:playImmediately:rateChangeReason:affectsCoordinatedPlayback:]_block_invoke"
- "-[AVPlayer _itemIsReadyToPlay:]_block_invoke"
- "-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_3"
- "-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]"
- "-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]"
- "-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]"
- "-[AVPlayer _updateDecoderPixelBufferAttributes:onFigPlayer:]"
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
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_3"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoLayersAreAttached]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _hasAssociatedAVPlayerLayerInPIPMode]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _itemOkayToPlayWhileTransitioningToBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _layerForegroundStateChanged:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _shouldDetachVideoLayersFromFigPlayer]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _willEnterForeground:]"
- "-[AVPlayer(AVPlayerPIPSupport) setBackgroundPIPAuthorizationToken:]"
- "-[AVPlayer(AVPlayerSpeedRamp) setSupportsSpeedRamps:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _resumePlayback:error:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _updateConnectionToSecondScreen]"
- "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]"
- "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke"
- "-[AVPlayer(PlaybackCoordination) _ensureFigPlaybackCoordinatorIsConnected]"
- "-[AVPlayerCaptionLayer _interstitialLayer]"
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
- "-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:]"
- "-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:]_block_invoke"
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
- "-[AVPlayerLayer _restoreClientLayers:intoMaskLayer:]"
- "-[AVPlayerLayer _setIsPartOfForegroundScene:]_block_invoke"
- "-[AVPlayerLayer _setPlayer:forPIP:]"
- "-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke"
- "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]"
- "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke"
- "-[AVPlayerLayer _setSublayersForPIP:]"
- "-[AVPlayerLayer _startObservingPlayer:]"
- "-[AVPlayerLayer _stopObservingPlayer:]"
- "-[AVPlayerLayer _updateReadyForDisplayForPlayerCurrentItem]_block_invoke"
- "-[AVPlayerLayer _windowSceneDidEnterBackground]"
- "-[AVPlayerLayer _windowSceneWillEnterForeground]"
- "-[AVPlayerLayer addSublayer:]"
- "-[AVPlayerLayer copyDisplayedPixelBuffer]"
- "-[AVPlayerLayer init]"
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
- "-[AVPlayerLoggingIdentifier init]"
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
- "-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:]"
- "-[AVPlayerPlaybackCoordinator _updateWaitingPoliciesOnFigPlaybackCoordinator:]"
- "-[AVPlayerPlaybackCoordinator beginSuspensionForReason:]"
- "-[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:]"
- "-[AVPlayerPlaybackCoordinator participantForIdentifier:]_block_invoke"
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
- "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) canOverlapPlaybackFromPlayerItem:toPlayerItem:]"
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
- "-[AVRoutingSession dealloc]"
- "-[AVRoutingSession destination]"
- "-[AVRoutingSession establishedAutomaticallyFromLikelyDestination]"
- "-[AVRoutingSession initWithFigRoutingSession:]"
- "-[AVRoutingSessionDestination dealloc]"
- "-[AVRoutingSessionDestination initWithFigRoutingSessionDestination:]"
- "-[AVRoutingSessionDestination outputDeviceDescriptions]"
- "-[AVRoutingSessionDestination probability]"
- "-[AVRoutingSessionDestination providesExternalVideoPlayback]"
- "-[AVRoutingSessionManager allLikelyDestinations]"
- "-[AVRoutingSessionManager currentRoutingSession]"
- "-[AVRoutingSessionManager dealloc]"
- "-[AVRoutingSessionManager initWithFigRoutingSessionManager:]"
- "-[AVRoutingSessionManager likelyExternalDestinations]"
- "-[AVRoutingSessionManager prefersLikelyDestinationsOverCurrentRoutingSession]"
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
- "-[AVSampleBufferAudioRendererLoggingIdentifier init]"
- "-[AVSampleBufferDisplayLayer _updateLayerTreeGeometryWithVideoGravity:presentationSize:videoGravityShouldTriggerAnimation:]_block_invoke"
- "-[AVSampleBufferDisplayLayer dealloc]"
- "-[AVSampleBufferDisplayLayer init]"
- "-[AVSampleBufferDisplayLayer layerDidBecomeVisible:]"
- "-[AVSampleBufferDisplayLayer layoutSublayers]"
- "-[AVSampleBufferDisplayLayer setBounds:]"
- "-[AVSampleBufferDisplayLayer setSTSLabel:]"
- "-[AVSampleBufferDisplayLayer setSTSLabel:]_block_invoke"
- "-[AVSampleBufferDisplayLayer videoRect]"
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
- "-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]"
- "-[AVSampleBufferVideoRenderer addSampleBufferDisplayLayer:]"
- "-[AVSampleBufferVideoRenderer addVideoTarget:]"
- "-[AVSampleBufferVideoRenderer createVideoQueue:]"
- "-[AVSampleBufferVideoRenderer dealloc]"
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
- "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]_block_invoke"
- "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc]"
- "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:]"
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
- "<<<< AVAsset >>>>"
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
- "<<<< AVAssetDownloadSession >>>>"
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
- "<<<< AVAssetExportSession >>>> %s: fileLengthLimit: %lld"
- "<<<< AVAssetExportSession >>>> %s: maximize power efficiency %s"
- "<<<< AVAssetExportSession >>>> %s: no asset, no presetName, or no export settings => nil: asset=%@, presetName=%@"
- "<<<< AVAssetExportSession >>>> %s: no export session => nil"
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
- "<<<< AVAssetReaderOutput >>>> %s: %p received %@"
- "<<<< AVAssetReaderOutput >>>> %s: %p received %@, extractionID=%d"
- "<<<< AVAssetReaderOutput >>>> %s: FigAssetReader has told us to wait until the sample buffer is ready.  Blocking until we get a notification"
- "<<<< AVAssetReaderOutput >>>> %s: FigAssetReaderExtractAndRetainNextSampleBuffer returned %d, extractionComplete=%d, sampleBuffer=%p, self=%p"
- "<<<< AVAssetResourceLoader >>>>"
- "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoader delegate does not respond to selector %@"
- "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoaderDelegate for AVAssetResourceLoader %@ is gone"
- "<<<< AVAssetResourceLoader >>>> %s: [AVAssetResourceLoadingRequest finishLoading] is called for a content key request while an AVContentKeySession instance is attached to AVURLAsset. Generating event"
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
- "<<<< AVCaptionRenderer >>>> %s: <%p> %s render started"
- "<<<< AVCaptionRenderer >>>> %s: <%p> *** FigCaptionCreate() returned %d"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request returned %d caption scenes"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request started"
- "<<<< AVCaptionRenderer >>>> %s: <%p> -renderInContext:atTime: called with bounds equal to CGRectNull"
- "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session returned %d"
- "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session with FigCaptions"
- "<<<< AVCaptionRenderer >>>> %s: <%p> preparing to set session after converting AVCaptions to FigCaptions array"
- "<<<< AVCaptionRenderer >>>> %s: <%p> start setting session with %ld FigCaptions"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCDSSessionSetTime returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCDSSessionUpdateCGContext returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientSetTime returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientUpdateCGContext returned error %d"
- "<<<< AVCaptionRenderer >>>> %s: FigCDSSessionStop() returned %d"
- "<<<< AVCaptionRenderer >>>> %s: FigCaptionClientStop() returned %d"
- "<<<< AVComposition >>>> %s: AVAsset with nil _absoluteURL and NULL _mutableComposition"
- "<<<< AVComposition >>>> %s: [%p] called"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p asset: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p mediaType: %@ preferredTrackID: %d"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackAssetURL: %@ trackID: %d"
- "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackID: %d"
- "<<<< AVContentKeySession >>>>"
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
- "<<<< AVFigRoutingContextUtilities >>>> %s: Using value %d for %@"
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
- "<<<< AVMetadataItem >>>>"
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
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying all audio contexts not supported!"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying system remote display context not supported!"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for endpoint %@"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for route descriptor %@"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopyPredictedSelectedRouteDescriptor yielded %@ (err=%d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded %@NULL endpoint (err=%d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded endpoint %@ (err: %d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptor yielded %@ (err: %d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptors yielded %@ (err: %d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoutes yielded %@ (err: %d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Listener should be the shared endpoint agent queue"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: No comm channel found for ID %@, synthesizing one for the delegate (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Output context exists with associated remote output device"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Storing new outgoing communication channel (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Trying comm channel ID %@ (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using comm channel ID %@ (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using pre-existing outgoing communication channel (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevice=%@, options=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevices=%@, options=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, agent=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, commChannelUUID=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, contextUUID=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, data=%@, commChannelUUID=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, options=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevice=%@, options=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevices=%@, options=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, reason=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@, reason=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeUpdateID=%@, reason=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContext=%@, routingContextCreator=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContextID=%@)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_AssociatedAudioDevice = %@ (err: %d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_ContextUUID = %@ (err=%d)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: operation finished"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: returning %@ (self=%p)"
- "<<<< AVOutputContext (FigRoutingContext) >>>> %s: using clientPID %d"
- "<<<< AVOutputContext >>>> %s: Defaulting to AVOutputContext impl %@"
- "<<<< AVOutputContext >>>> %s: Received notification %@"
- "<<<< AVOutputContext >>>> %s: called (self=%p)"
- "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@)"
- "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, channel=%@)"
- "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, data=%@, channel=%@)"
- "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, replacementImpl=%@)"
- "<<<< AVOutputContext >>>> %s: called (self=%p, status=%d)"
- "<<<< AVOutputContext >>>> %s: contextID = %@"
- "<<<< AVOutputContext >>>> %s: outputDevice = %@"
- "<<<< AVOutputContext >>>> %s: outputDevices = %@"
- "<<<< AVOutputContext >>>> %s: predictedOutputDevice = %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerGetMuteOfEndpointWithID (endpointID=%{private}@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' has value: %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' not supported"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: GAPA feature not enabled"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Operations finished with status %d, error %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: RouteUID %@ or RouteName %@ is nil, can't construct description."
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized head-tracked spatial audio mode %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized mode %@"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  Only a subset of possible device types can be communicated by FigEndpoint"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover connected paired devices from FigEndpoint"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover detailed device subtype for most devices from FigEndpoint"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get DataOverACL information from FigEndpoint"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get isInEar information from FigEndpoint"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpoint=%@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpointID=%@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, figEndpoint=%@)"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p"
- "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p client %@ reason %@"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>>"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Listener should be the output device route discoverer queue"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Operations finished with status %d, error %@"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Using value %d for %@"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (endpointID=%@)"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
- "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, routeDescriptor=%@)"
- "<<<< AVOutputDevice >>>> %s: No Output Context to add to!"
- "<<<< AVOutputDevice >>>> %s: called (self=%p, impl=%@)"
- "<<<< AVOutputDevice >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
- "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p)"
- "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, request=%@, requestImpl=%@)"
- "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, status=%d, error=%@)"
- "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, uniqueID=%@, routeDescriptor=%@, pinMode=%d, reason=%@)"
- "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Received notification %@"
- "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p)"
- "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p, delegate=%@)"
- "<<<< AVOutputDeviceAuthorizationSession >>>> %s: self=%p, impl=%@, replacementImpl=%@"
- "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: Unrecognized event type: %@"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No AVOutputDevice to connect to!"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No System Remote Pool to add to!"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No comm channel found for ID %@ for device %@, synthesizing one for the delegate."
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Removing comm channel UUID %@ for device with ID %@"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p)"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
- "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: initialized (self=%p)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@ (err: %d)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting kFigRouteDiscovererProperty_AudioSessionID to %@"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Unsupported device feature combination %d"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%@, class=%@, deviceFeatures=%u)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AudioSessionID = %@ (err=%d)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AvailableRoutes = %@ (err=%d)"
- "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: Available output devices: %@"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: Posting %@"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: Returning %@"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (targetAudioSession=%@)"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: otherDevices = %@"
- "<<<< AVOutputDeviceDiscoverySession >>>> %s: recentlyUsedDevices = %@"
- "<<<< AVOutputDeviceGroup >>>> %s: called (self=%p, impl=%@)"
- "<<<< AVOutputDeviceGroup >>>> %s: outputDevices = %@"
- "<<<< AVOutputDeviceHID >>>> %s: called (uuid=%@, screenUUID=%@ endpoint=%p)"
- "<<<< AVOutputDeviceIcon >>>> %s: called (dict=%@)"
- "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (dict=%@)"
- "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (viewArea=%@, transitionControl=%{BOOL}u, supportsFocusTransfer=%{BOOL}u, statusBarEdge=%@, safeArea=%@)"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ updating transport control state cache for item identifier %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Converted to media time: original time %f, adjusted media time %f, host time adjustment (%f-%f)"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new control state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new participant state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle replacement participant state."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator skipping updating control states."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator updating %d control states."
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Posting AVPlaybackCoordinatorItemIdentifierForCoordinatedPlaybackDidChangeNotification in response to delegate change"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Setting IsExpanseMediaSession %s on AVAudioSession error %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ Setting integrated timeline"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ beginning suspension with reason %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ caching group timeline reset"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ current pending seek id %d, seek time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p proposing new time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline only contains primary segment. Bypassing integrated seek to %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline seek at %f current time at %f, applied : %d"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ interstitial is active : %d"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ playback coordinator is suspended. Skipping seek to %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ resetting group timeline expectation"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator with UUID %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator, but NULL figPlaybackCoordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ setting waiting policies %@ on playback coordinator"
- "<<<< AVPlaybackCoordinator >>>> %s: <AVPlaybackCoordinator: %@> failed to dispatch work async onto player queue with err: %d, synchronizing locally"
- "<<<< AVPlaybackCoordinator >>>> %s: Could not create FigTimelineCoordinatorSuspensionRef"
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator gave a participantID which is not present in otherParticipants"
- "<<<< AVPlaybackCoordinator >>>> %s: States aren't distinguishable. Assuming state from the outside is better."
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for DidIssueCommandToFigPlayer notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "<<<< AVPlayer >>>> %s: %@ (self = %p) (layer = %p)"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) Pausing item since cannot transition to background _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) _detachVideoLayersFromFigPlayer _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) attach video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) issue _detachVideoLayersFromFigPlayer _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d, _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) not updating video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip _detachVideoLayersFromFigPlayer  _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip attach video layers _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: has no layers or no figPlayer. Nothing to attach/detach for iapd"
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer do hold. Attaching."
- "<<<< AVPlayer >>>> %s: %@ AVPlayer <%p>: iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer don't hold. Detaching."
- "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) and its closedCaptionLayer(%p)"
- "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) is adding videoLayer(%p), closedCaptionLayer(%p), and subtitleLayer(%p) sublayers"
- "<<<< AVPlayer >>>> %s: %@ Did update status to %d (self=%p)"
- "<<<< AVPlayer >>>> %s: %@ Dispatching FigPlayer copy property block (self=%p) to a background queue if necessary"
- "<<<< AVPlayer >>>> %s: %@ Extended mode is active"
- "<<<< AVPlayer >>>> %s: %@ Host application is in foreground with foreground layers"
- "<<<< AVPlayer >>>> %s: %@ NULL FigPlayerInterstitialCoordinator"
- "<<<< AVPlayer >>>> %s: %@ New current item: %@ %@ (self = %@)"
- "<<<< AVPlayer >>>> %s: %@ PIP mode is active"
- "<<<< AVPlayer >>>> %s: %@ Should Detach: [%@]"
- "<<<< AVPlayer >>>> %s: %@ Trying to set picker id : %@"
- "<<<< AVPlayer >>>> %s: %@ Under device lock and has external display active"
- "<<<< AVPlayer >>>> %s: %@ Will update status (self=%p)"
- "<<<< AVPlayer >>>> %s: %@ _setUsesLegacyAutomaticWaitingBehavior: %s"
- "<<<< AVPlayer >>>> %s: %@ attached video layer array with %lu layers on FigPlayer"
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
- "<<<< AVPlayer >>>> %s: %@ detached video layer array from FigPlayer"
- "<<<< AVPlayer >>>> %s: %@ dispatched (self = %@, inNotificationName = %@)"
- "<<<< AVPlayer >>>> %s: %@ dispatching (self = %p)"
- "<<<< AVPlayer >>>> %s: %@ failed to copy currently displayed pixel buffer although no error"
- "<<<< AVPlayer >>>> %s: %@ failed to take background assertion with err %@"
- "<<<< AVPlayer >>>> %s: %@ got background assertion"
- "<<<< AVPlayer >>>> %s: %@ has foreground layers, attaching video layers"
- "<<<< AVPlayer >>>> %s: %@ has no more foreground layers left, detaching video layers"
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
- "<<<< AVPlayer >>>> %s: %@ releasing background assertion"
- "<<<< AVPlayer >>>> %s: %@ removed %@ %@, now have %@"
- "<<<< AVPlayer >>>> %s: %@ setting from %d to %d"
- "<<<< AVPlayer >>>> %s: %@ setting rate to %f"
- "<<<< AVPlayer >>>> %s: %@ setting to %d"
- "<<<< AVPlayer >>>> %s: %@ setting up FigPlayer <%p>"
- "<<<< AVPlayer >>>> %s: %@ updating video layers due to adding layer %p (self=%@)"
- "<<<< AVPlayer >>>> %s: %@: isConnectedToPhysicalSecondScreen changed %d"
- "<<<< AVPlayer >>>> %s: %s"
- "<<<< AVPlayer >>>> %s: AVPlayer %@ setShouldWaitForVideoTarget to %d"
- "<<<< AVPlayer >>>> %s: Coordinator player disabled"
- "<<<< AVPlayer >>>> %s: Creating instance of %s"
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
- "<<<< AVPlayer >>>> %s: Player <%@ %@> audiovisual background policy set to Automatic, use coordinator other participant count %d to decide"
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
- "<<<< AVPlayer >>>> %s: Surrogate player enabled = %d"
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
- "<<<< AVPlayer >>>> %s: skipping _didFinishSuspension"
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
- "<<<< AVPlayerLayer >>>> %s: Called (self=%p)"
- "<<<< AVPlayerLayer >>>> %s: Called (self=%p, bounds=%@)"
- "<<<< AVPlayerLayer >>>> %s: Cannot add sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot insert sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot replace sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Cannot set sublayers while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: Display Size is %f x %f scale is %f"
- "<<<< AVPlayerLayer >>>> %s: Error in traversing layer tree"
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
- "<<<< AVPlayerLayer >>>> %s: called (self=%p, item=%p, readyForDisplay=%d)"
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
- "<<<< AVPlayerOutput >>>>"
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
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO because the multichannel audio strategy permits exclusive passthrough"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since AirPlay Video is active"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since Buffered AirPlay is active"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since action-at-end is NOT advance"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since one of items is HLS"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: %p %@. YES"
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
- "<<<< AVRoutingSessionManager >>>> %s: All likely external destinations %@ (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: External destination confidence %f below threshold %f, clearing array (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: Fetched %d from %@ (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: Returning %@"
- "<<<< AVRoutingSessionManager >>>> %s: Sum of external destination confidence: %f (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: called"
- "<<<< AVRoutingSessionManager >>>> %s: called (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSession=%@)"
- "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionDestination=%@)"
- "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionManager=%@)"
- "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (err: %d)"
- "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from FigRoutingSession (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: kFigRoutingSessionProperty_EstablishedAutomaticallyFromLikelyDestination = %@"
- "<<<< AVRoutingSessionManager >>>> %s: returning %@ (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: returning %d"
- "<<<< AVRoutingSessionManager >>>> %s: returning %d (self=%p)"
- "<<<< AVRoutingSessionManager >>>> %s: returning %f (self=%p)"
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
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p]"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] %@, on thread %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Created layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Hiding contentLayer because bounds is CGSizeZero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] New label \"%@\", Current label \"%@\", Layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Removing label from layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Setting label \"%@\" on layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Setting position(%d,%d), bounds(%dx%d), transform scale(%.3fx%.3f), offset(%d,%d)"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Unhiding contentLayer because bounds is nonzero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] bounds: %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] videoRect: %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p], on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Cleaning-up renderer %p for synchronizerInternal %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Failed to create FigSampleBufferRenderSynchronizer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Render synchronizer %s participate in STS -- thank you for setting \"defaults write com.apple.avfoundation rendersynchronizer_sts_label -bool %s\""
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Selecting AVSBDL=%p that already contains a label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Selecting AVSBVR=%p with label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Setting STSLabel %@ on renderer=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Setting new STSLabel on AVSBDL=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Was tracking AVSBDL=%p, switching to AVSBVR=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Error adding an AudioRenderer to the FigSynchronizer: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Failed to add Renderer %@; error returned from _addRenderer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Setting self as render synchronizer on renderer (%p) failed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Too many audio renderers"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Trying to add a renderer (%p) to same synchronizer"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Trying to add multiple audio renderers when disallowed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] adding renderer %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] called for renderer %p; time: %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] created (internal: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] invalidated old scheduled removal of renderer %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] old once observer already fired before we could invalidate it (renderer: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] rate: %1.3f; time: %1.3f; hostTime: %1.3f; fig error: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] releasing on main thread avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] removalBlock called; weakToSelf: %p; weakToRenderer: %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] retaining avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] successfully scheduled removal of renderer %p at time %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p], on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called (center=%@, listener=%p, name=%@, object=%p, payload=%@)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called (self = <%p>, time observer = <%p>)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: error: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: unknown renderer: %p"
- "<<<< AVSampleBufferVideoOutput >>>> %s: Dispatching -outputSequenceWasFlushed:"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArray failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArrayOptions failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCopyImageForTime did not provide a imageOriginalTimeOut value. Bailing."
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCreate failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextSetImageAvailableImmediateCallback failed: %d"
- "<<<< AVSampleBufferVideoOutput >>>> %s: Sending -outputSequenceWasFlushed: to delegate"
- "<<<< AVSampleBufferVideoOutput >>>> %s: Unable to copy next image from visual context. Bailing."
- "<<<< AVSampleBufferVideoOutput >>>> %s: copyPixelBufferForSourceTime requestTime %1.3f pb %p time %1.3f"
- "<<<< AVSampleBufferVideoRenderer >>>>"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: Unable to set expectMinimumUpcomingSampleBufferPresentationTime because minimumUpcomingPresentationTime is not numeric"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %@], on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Enqueue sample buffer failed error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Failed to copy currently displayed pixel buffer although no error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received complete decode for preroll"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received external protection status changed to \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received flush complete"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received lost decoder state error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received server connection died with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received server dependency lost with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received video queue did drop below low water level"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received video queue failed with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Setting %d video targets."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Setting display layer %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p], on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, exit layerQueue block, on thread %@]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Adding %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Calling completion handler with %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Calling completion handler with success"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to copy currently displayed pixel buffer as there is no video queue"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to create AVSBVR error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to create video queue error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed with error %d at %s"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] FigVideoQueueFlush returned error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Flush completed but no pending callback block found"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Flush returned err=%d. Recreating FigVideoQueue. %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Ignoring enqueueSampleBuffer because status is failed"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] No pending preroll callback"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Output obscured = %@, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Received video queue decode error \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] RemoveDisplayedImage=%s, handler=%p, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Removing %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Setting %@, posting AVSampleBufferSTSLabelDidChangeNotification"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Setting %p, returning %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Skip stale callback, requestId (%d) != pendingPrerollRequestID (%d)"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Total frames enqueued since last flush %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] UpcomingPTSExpectation is enabled, but enqueuePTS:%.3f is smaller than expectedMinimumUpcomingPTS:%.3f"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Visibility changed to %s, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] readyForDisplay changed (%@), post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] releasing %p on main thread, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] timebase %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p], on thread %@"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorCreateSampleBuffer failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetDecodeTimeStamp failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetPresentationTimeStamp failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByDecodeTime failed (%d)"
- "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByPresentationTime failed (%d)"
- "<<<< AVScheduledAudioParameters >>>> %s: not a valid scheduled ramp class"
- "<<<< AVScheduledParameterRamp >>>> %s: Unknown ramp mode: %d"
- "<<<< AVStreamDataParser >>>>"
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
- "<<<< AVUtilities >>>>"
- "<<<< AVUtilities >>>> %s: called (queue=%p, currentQueue=%p, dispatch_get_main_queue()=%p, NSThread isMainThread=%d)"
- "<<<< AVUtilities >>>> %s: dispatching block to queue"
- "<<<< AVUtilities >>>> %s: dispatching to background queue"
- "<<<< AVUtilities >>>> %s: running block synchronously"
- "<<<< AVVideoComposition >>>> %s: Unknown video compositor name for FigRemaker: %@"
- "<<<< AVVideoComposition >>>> %s: Using video compositor: %@"
- "<<<< AVVideoComposition >>>> %s: dictionaryRepresentation only accepts RGB color space for backgroundColor"
- "<AVPlayerLayer %p%@%@%@>"
- "AV Perf - Begin: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
- "AV Perf - End: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
- "AVAsset.m"
- "AVAssetDownloadConfiguration.m"
- "AVAssetDownloadSession.m"
- "AVAssetReaderOutputCaptionAdaptor.m"
- "AVAssetResourceLoader.m"
- "AVAssetWriterFigAssetWriterHandleCompletedNotification"
- "AVAssetWriterFigAssetWriterHandleFailedNotification"
- "AVAssetWriterFigAssetWriterHandleServerDiedNotification"
- "AVAssetWriterInputFigAssetWriterEndPassOperationPassFinished"
- "AVCanWriteFilesToDirectoryAtURL"
- "AVCompositionTrack.m"
- "AVContentKeySession.m"
- "AVDefaultRoutingContextFactory"
- "AVEnsureNotOnMainThread"
- "AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange"
- "AVFigRouteDescriptorOutputDeviceImpl.m"
- "AVFigRouteDescriptorOutputDeviceImplCanSetEndpointVolumeDidChange"
- "AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange"
- "AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange"
- "AVFigRouteDescriptorOutputDeviceImplEndpointRoomVolumeDidChange"
- "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange"
- "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange"
- "AVFigRouteDiscovererAvailableRoutesChanged"
- "AVFigRouteDiscovererEndpointDescriptorChanged"
- "AVFigRouteDiscovererRoutePresentChanged"
- "AVFigRoutingContextRouteChangeOperationRouteChangeComplete"
- "AVLocalizedError"
- "AVLocalizedStringFromTableWithLocaleWithBundleIdentifier"
- "AVMediaStatePurgePostMediaStateWasPurgedNotificationForObject"
- "AVMetadataItem.m"
- "AVMetadataItemMakeDataFromBoxedMetadata"
- "AVOperationStatusResolveOldAndNew"
- "AVOutputContextUsesRouteConfigUpdatedNotification"
- "AVOutputDeviceCopyFigModeForSpatialAudioMode"
- "AVOutputDeviceDescriptionsFromFigDescriptions"
- "AVOutputDeviceGetFigEndpoint"
- "AVOutputDeviceGetFigRouteDescriptor"
- "AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode"
- "AVOutputDeviceImplIsMutedForEndpointID"
- "AVPerfTelemetry"
- "AVPerformDelegateCallbackSynchronouslyForDelegateStorageIfCurrentDelegateQueueIsQueueElseDispatchToCurrentDelegateQueue"
- "AVPlayerCaptionLayer <%p>"
- "AVPlayerGetFigPlayerTypeForAsset"
- "AVPlayerItem addOutput"
- "AVPlayerItem audioMix"
- "AVPlayerItem currentMediaSelection"
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
- "AVRoutingSessionManagerGetLikelyDestinationsFromFig"
- "AVSBVR failed with error %d at %s."
- "AVSampleBufferDisplayLayer <%p>"
- "AVSampleBufferDisplayLayer <%p> (content layer)"
- "AVSampleBufferRenderSynchronizer init"
- "AVSampleBufferVideoRenderer.m"
- "AVSerializeOnQueueAsyncIfNecessary"
- "AVStreamDataParser.m"
- "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel"
- "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData"
- "AVTimebaseObserver_figTimebaseGetTime"
- "AVTimebaseObserver_timebaseNotificationCallback_block_invoke"
- "AVUtilities.m"
- "CDS"
- "CMTagCollectionCreateWithVideoOutputPreset"
- "Could not set KeyResponseReceived state on cryptor."
- "Cryptor is not available to create key request."
- "FVQSetProperty(ControlTimebase)"
- "FVQSetProperty(DisplayLayer)"
- "Failed on init"
- "Failed to allocate CFMutableDictionary"
- "Failed to allocate buffer for FigBoxedMetadata -> CFData conversion"
- "Failed to get queue"
- "Failed to prepare cryptor"
- "Failed to set video target array on video queue."
- "FigCaptionClient"
- "FigPlayer_File"
- "FigPlayer_Stream"
- "FigSubtitleCALayer"
- "FigVideoQueueCreate"
- "FigVideoQueueStart"
- "Hiding"
- "InternalPerfTelemetry"
- "Invalid asset track"
- "NOT visible"
- "NULL"
- "NULL figAsset"
- "NULL handlerServerXPCEndpoint"
- "Names count is 0?"
- "No FCKS available"
- "No endpoint found for route descriptor"
- "Received invalid preset"
- "Showing"
- "The AVSampleBufferDisplayLayer's content layer is nil."
- "Trying to create AVAssetDownloadContentConfiguration with an invalid AVAssetVariantQualifier"
- "Visible"
- "WILL"
- "WILL NOT"
- "_avplLoopingItemFailedToPlayToEndTimeNotificationHandler"
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
- "_sampleDescriptionExtensionAtomForKey"
- "addSampleBufferDisplayLayer failed to set content layer"
- "aig_trace"
- "appendCaptionGroupToQueue"
- "assetTrackNotificationHandler"
- "assetinspector_trace"
- "assetreaderoutput_trace"
- "assettrackinspector_trace"
- "assetwriter_trace"
- "assetwriterinput_trace"
- "assetwriterinputannotationadaptor_trace"
- "assetwriterinputmetadataadaptor_trace"
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
- "avplayeritem_fpItemNotificationCallback_block_invoke_6"
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
- "avqueueplayer_trace"
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
- "badly formatted PSSH data"
- "badly formatted key request init data - codecType not valid"
- "badly formatted key request init data - containerType not valid"
- "badly formatted key request init data - mediaType not valid"
- "badly formatted key request init data - sinf array not found"
- "bail error check"
- "basics"
- "boss NULL"
- "ccr_trace"
- "cmTimebaseNotificationCallback_TimeJumped"
- "colorSpace"
- "completed"
- "composition_trace"
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
- "handleFigAssetNotification"
- "handleFigAssetTrackNotification"
- "handleFigAssetTrackNotification_block_invoke"
- "hlsvariant_trace"
- "inspection"
- "inspector_trace"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kCMTagCollectionError_ParamErr"
- "kFigBaseObjectError_ParamErr"
- "kFigCPEError_InvalidState"
- "kFigContentKeyBossError_AllocationFailed"
- "kFigMetadataReaderError_AllocationFailed"
- "kFigRouteDiscovererError_InvalidParameter"
- "kFigSSMError_InvalidState"
- "key request has not succeeded. value not available."
- "kvodispatcher_trace"
- "mismatched handler"
- "nil reference"
- "no figAsset"
- "non-"
- "non-NULL"
- "not an AVAssetResourceLoader"
- "not an AVAssetResourceLoaderRemoteHandlerContext"
- "not an AVContentKeyReportGroup"
- "not an AVContentKeySession"
- "not spatial"
- "pathWithComponents:"
- "platformutilities_trace"
- "playback"
- "scheduledaudioparameters_trace"
- "self.figAsset NULL"
- "setBorderColor:"
- "setBorderWidth:"
- "stringWithValidatedFormat"
- "stringWithValidatedFormatArg2"
- "stringWithValidatedFormatInteger"
- "stringWithValidatedFormatString"
- "subarrayWithRange:"
- "true"
- "visible"
- "yes"

```
