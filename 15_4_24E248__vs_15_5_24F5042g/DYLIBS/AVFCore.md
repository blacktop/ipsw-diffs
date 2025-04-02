## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

```diff

-2320.19.1.0.0
-  __TEXT.__text: 0x1b7298
-  __TEXT.__auth_stubs: 0x36b0
-  __TEXT.__objc_methlist: 0x1d6a4
-  __TEXT.__const: 0x268
-  __TEXT.__gcc_except_tab: 0x456c
-  __TEXT.__cstring: 0x27703
-  __TEXT.__oslogstring: 0x77dc
+2330.3.1.0.0
+  __TEXT.__text: 0x214290
+  __TEXT.__auth_stubs: 0x3770
+  __TEXT.__objc_methlist: 0x1d6b4
+  __TEXT.__const: 0x360
+  __TEXT.__gcc_except_tab: 0x4fcc
+  __TEXT.__cstring: 0x36c44
+  __TEXT.__oslogstring: 0x1f86b
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x8fe0
+  __TEXT.__unwind_info: 0x92a8
   __TEXT.__objc_classname: 0x6770
-  __TEXT.__objc_methname: 0x37081
-  __TEXT.__objc_methtype: 0xaf6e
-  __TEXT.__objc_stubs: 0x20ca0
-  __DATA_CONST.__got: 0x4c40
-  __DATA_CONST.__const: 0x3530
+  __TEXT.__objc_methname: 0x3713f
+  __TEXT.__objc_methtype: 0xaf91
+  __TEXT.__objc_stubs: 0x20e20
+  __DATA_CONST.__got: 0x4c48
+  __DATA_CONST.__const: 0x3558
   __DATA_CONST.__objc_classlist: 0x1310
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xada8
+  __DATA_CONST.__objc_selrefs: 0xade8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xdd8
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x1b68
+  __AUTH_CONST.__auth_got: 0x1bc8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x3a60
-  __AUTH_CONST.__cfstring: 0x19d60
-  __AUTH_CONST.__objc_const: 0x35340
+  __AUTH_CONST.__const: 0x3a80
+  __AUTH_CONST.__cfstring: 0x1a300
+  __AUTH_CONST.__objc_const: 0x35380
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH.__objc_data: 0x27b0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x2604
-  __DATA.__data: 0x1bc0
+  __DATA.__objc_ivar: 0x260c
+  __DATA.__data: 0x1be0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x430
-  __DATA.__common: 0x300
+  __DATA.__common: 0x6e0
+  __DATA.__bss: 0x448
   __DATA_DIRTY.__objc_data: 0x96f0
   __DATA_DIRTY.__data: 0xb8
   __DATA_DIRTY.__bss: 0x80

   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11688
-  Symbols:   28880
-  CStrings:  14203
+  Functions: 11833
+  Symbols:   29133
+  CStrings:  16362
 
Symbols:
+ -[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:].cold.2
+ -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler].cold.2
+ -[AVAssetWriterWritingHelper encryptionScheme].cold.1
+ -[AVAssetWriterWritingHelper encryptionScheme].cold.2
+ -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.1
+ -[AVAssetWriterWritingHelper storageSpacePreallocationSize].cold.2
+ -[AVCoordinatedPlaybackSuspension _setinterstitialSuspension:]
+ -[AVPlayerLayer _compactDescription]
+ -[AVSampleBufferAudioRenderer init].cold.1
+ AVTelemetryGenerateID.cold.1
+ AVTelemetryLogHandle.cold.1
+ AVTelemetryLogHandle.emitter
+ AVTelemetryLogHandle.onceToken
+ GCC_except_table106
+ GCC_except_table113
+ GCC_except_table119
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table149
+ GCC_except_table154
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table196
+ GCC_except_table88
+ GCC_except_table97
+ OBJC_IVAR_$_AVCoordinatedPlaybackSuspension._interstitialSuspension
+ OBJC_IVAR_$_AVSampleBufferVideoRenderer._enqueuedFramesForLoggingOnly
+ _AVBacktraceAsString
+ _AVBacktraceAsStringWithMaxFrames
+ _AVTelemetryLogHandle
+ _CMSampleBufferGetPresentationTimeStamp
+ _FigDebugIsInternalBuild
+ _FigPlaybackRateChangeReasonGetDescription
+ _FigSignalErrorAt3
+ _NSStringFromRect
+ _NSStringFromSize
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
+ __103+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]_block_invoke.27
+ __104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke.202
+ __104-[AVDelegatingPlaybackCoordinator transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:]_block_invoke.106
+ __106+[AVAssetWriterWritingHelper finishWritingDelegateOperationWithAssetWriter:andFigAssetWriter:andDelegate:]_block_invoke.552
+ __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165
+ __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165.cold.1
+ __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.165.cold.2
+ __114-[AVAssetResourceLoader _performDelegateCallbackSynchronouslyIfCurrentDelegateQueueIsQueue:delegateCallbackBlock:]_block_invoke.199
+ __122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.158
+ __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke.1173
+ __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke_2.1174
+ __130-[AVContentKeySession(AVContentKeySessionPrivateUtilities) _invokeDelegateCallbackWithBlock:synchronouslyWhenDelegateQueueIsNULL:]_block_invoke.638
+ __143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke.146
+ __146-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke.cold.1
+ __188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.155
+ __188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.157
+ __188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.161
+ __21-[AVPlayerLayer init]_block_invoke.100
+ __21-[AVPlayerLayer init]_block_invoke.103
+ __22-[AVPlayer _addLayer:]_block_invoke.590
+ __22-[AVPlayer _addLayer:]_block_invoke.591
+ __26-[AVPlayerItem _setAsset:]_block_invoke.521
+ __30-[AVPlayerItemTrack isEnabled]_block_invoke.44
+ __31-[AVPlayerItem _updateTimebase]_block_invoke.595
+ __31-[AVPlayerItem _updateTimebase]_block_invoke_2.596
+ __32-[AVPlayerItemTrack setEnabled:]_block_invoke.45
+ __34-[AVPlayer setExpectedAssetTypes:]_block_invoke.498
+ __34-[AVPlayerItem _attachToFigPlayer]_block_invoke.480
+ __35-[AVPlayer _addPlayerCaptionLayer:]_block_invoke.587
+ __35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.272
+ __36-[AVPlayerItem setVideoComposition:]_block_invoke.638
+ __39-[AVPlayerCaptionLayer layoutSublayers]_block_invoke.18
+ __39-[AVPlayerItemTrack setVideoFieldMode:]_block_invoke.58
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.234
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.236
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.243
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.250
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke_2.239
+ __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke_2.246
+ __41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke.563
+ __42-[AVPlayerCaptionLayer _interstitialLayer]_block_invoke.55
+ __45-[AVPlayer replaceCurrentItemWithPlayerItem:]_block_invoke.517
+ __46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke.73
+ __46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke.276
+ __48-[AVCaptionRenderer captionSceneChangesInRange:]_block_invoke.35
+ __51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke.541
+ __52-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke.58
+ __53-[AVPlayerItem _addInterstitialEventCollectorLocked:]_block_invoke.687
+ __53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke.471
+ __53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_2.472
+ __56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke.276
+ __57-[AVPlayerPlaybackCoordinator setFigPlaybackCoordinator:]_block_invoke.249
+ __58-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevel]_block_invoke.48
+ __59-[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:]_block_invoke.34
+ __60-[AVPlayerItem _ensureAssetWithFigPlaybackItemWithTrackIDs:]_block_invoke.522
+ __62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.523
+ __62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke.180
+ __63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1010
+ __63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke.278
+ __63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.190
+ __63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.196
+ __64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke.101
+ __67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke.103
+ __67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke.82
+ __67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke.512
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.453
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.457
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.463
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.477
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.484
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.489
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.478
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.485
+ __67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke.257
+ __67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.232
+ __67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.233
+ __67-[AVSampleBufferGeneratorBatch makeDataReadyWithCompletionHandler:]_block_invoke.113
+ __69-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]_block_invoke.624
+ __70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.163
+ __71-[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:]_block_invoke.202
+ __71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.45
+ __71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.46
+ __74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke.912
+ __74-[AVDelegatingPlaybackCoordinator setSuspensionReasonsThatTriggerWaiting:]_block_invoke.126
+ __77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke.558
+ __78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.28
+ __78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.29
+ __79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke.56
+ __79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.122
+ __79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.125
+ __81-[AVSampleBufferVideoRenderer _computeSampleBufferEnqueueingInfoForSampleBuffer:]_block_invoke.131
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.76
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.91
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.92
+ __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.139
+ __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.149
+ __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.152
+ __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.140
+ __84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke.311
+ __87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.588
+ __87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.589
+ __88+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]_block_invoke.139
+ __90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke.358
+ __90-[AVDelegatingPlaybackCoordinator setParticipantLimit:forWaitingOutSuspensionsWithReason:]_block_invoke.122
+ __91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke.1027
+ __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1456
+ __97-[AVContentKeySession makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:]_block_invoke.537
+ __AVSampleBufferVideoOutput_figVCAvailableImmediate_block_invoke.68
+ __Block_byref_object_copy_.106
+ __Block_byref_object_copy_.153
+ __Block_byref_object_dispose_.107
+ __Block_byref_object_dispose_.154
+ __CMBlockBufferAsString
+ __DefaultRuneLocale
+ ___AVTelemetryLogHandle_block_invoke
+ ___block_descriptor_56_e8_32o40r_e26_v32?0"AVCaption"8Q16^B24l
+ ___block_descriptor_60_e8_32o40o48o_e31_^{OpaqueFigRoutingContext=}8?0l
+ ___block_descriptor_64_e8_32o40o48b56w_e24_v16?0"NSNotification"8l
+ ___copy_helper_block_e8_32o40o48b56w
+ ___destroy_helper_block_e8_32o40o48b56w
+ ___maskrune
+ __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1152
+ __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1156
+ __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1157
+ __avplayer_fpNotificationCallback_block_invoke.1166
+ __avplayer_fpNotificationCallback_block_invoke.1171
+ __avplayer_fpNotificationCallback_block_invoke.1173
+ __avplayer_fpNotificationCallback_block_invoke.1179
+ __avplayer_fpNotificationCallback_block_invoke.1181
+ __avplayer_fpNotificationCallback_block_invoke.1184
+ __avplayer_fpNotificationCallback_block_invoke.1185
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1464
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1484
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1490
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1492
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1496
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1500
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1507
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1508
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1509
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1513
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1514
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1518
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1519
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1525
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1526
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1530
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1531
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1532
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1539
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1515
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1520
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1527
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1516
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1528
+ __avplayeritem_fpItemNotificationCallback_block_invoke_4.1517
+ __block_literal_global.1041
+ __block_literal_global.1043
+ __block_literal_global.110
+ __block_literal_global.139
+ __block_literal_global.141
+ __block_literal_global.144
+ __block_literal_global.200
+ __block_literal_global.203
+ __block_literal_global.228
+ __block_literal_global.238
+ __block_literal_global.245
+ __block_literal_global.296
+ __block_literal_global.310
+ __block_literal_global.356
+ __block_literal_global.359
+ __block_literal_global.397
+ __block_literal_global.404
+ __block_literal_global.428
+ __block_literal_global.441
+ __block_literal_global.446
+ __block_literal_global.450
+ __block_literal_global.462
+ __block_literal_global.517
+ __block_literal_global.529
+ __block_literal_global.545
+ __block_literal_global.546
+ __block_literal_global.575
+ __block_literal_global.578
+ __block_literal_global.595
+ __block_literal_global.669
+ __block_literal_global.679
+ __block_literal_global.692
+ __block_literal_global.867
+ __handleFigAssetCollectionNotification_block_invoke.73
+ __handleFigAssetLoadingNotification_block_invoke.526
+ __handleFigAssetTrackNotification_block_invoke.460
+ __os_signpost_emit_with_name_impl
+ _backtrace
+ _backtrace_symbols
+ _figVideoQueueDidDropBelowLowWaterLevel.didDropBelowLowWaterLevelCountForLoggingOnly
+ _gAVAssetCacheTrace
+ _gAVAssetCollectionInspectorLoaderTrace
+ _gAVAssetCollectionTrace
+ _gAVAssetCustomURLTrace
+ _gAVAssetDownloadSessionTrace
+ _gAVAssetDownloadStorageManagerTrace
+ _gAVAssetExportSessionTrace
+ _gAVAssetImageGeneratorTrace
+ _gAVAssetInspectorTrace
+ _gAVAssetReaderOutputTrace
+ _gAVAssetResourceLoaderTrace
+ _gAVAssetTrace
+ _gAVAssetTrackInspectorTrace
+ _gAVAssetVariantTrace
+ _gAVAssetWriterInputAnnotationAdaptorTrace
+ _gAVAssetWriterInputMetadataAdaptorTrace
+ _gAVAssetWriterInputTrace
+ _gAVAssetWriterTrace
+ _gAVAsynchronousKeyValueLoadingTrace
+ _gAVCallbackContextRegistryTrace
+ _gAVCaptionRendererTrace
+ _gAVCompositionTrace
+ _gAVCoreImageFilterCustomVideoCompositorTrace
+ _gAVCustomCompositorTrace
+ _gAVDataDelegateTrace
+ _gAVDelegateUtilitiesTrace
+ _gAVFigObjectInspectorTrace
+ _gAVFileSystemUtilitiesTrace
+ _gAVKVODispatcherTrace
+ _gAVLoggingIdentifierTrace
+ _gAVMediaFileSegmenterTrace
+ _gAVMediaSelectionGroupTrace
+ _gAVMetadataItemTrace
+ _gAVMovieTrace
+ _gAVOperationTrace
+ _gAVPixelBufferAttributeMediator
+ _gAVPlatformUtilitiesTrace
+ _gAVPlayerCaptionLayer
+ _gAVPlayerItemLegibleOutputTrace
+ _gAVPlayerItemMediaDataCollectorTrace
+ _gAVPlayerItemMetadataCollector
+ _gAVPlayerItemMetadataOutputTrace
+ _gAVPlayerItemOutputTrace
+ _gAVPlayerItemRenderedLegibleOutputTrace
+ _gAVPlayerItemSampleBufferOutputTrace
+ _gAVPlayerLayerTrace
+ _gAVPlayerLooperTrace
+ _gAVPlayerOutputTrace
+ _gAVQueuePlayerTrace
+ _gAVSampleBufferAudioRendererTrace
+ _gAVSampleBufferDisplayLayerTrace
+ _gAVSampleBufferGeneratorTrace
+ _gAVSampleBufferRenderSynchronizerTrace
+ _gAVSampleBufferVideoOutputTrace
+ _gAVSampleCursorTrace
+ _gAVScheduledAudioParameters
+ _gAVStreamDataParserTrace
+ _gAVStreamSessionParserTrace
+ _gAVTimebaseObserverTrace
+ _gAVTimedMetadataGroupTrace
+ _gAVUtilitiesTrace
+ _gScheduledParameterRampTrace
+ _objc_msgSend$_compactDescription
+ _objc_msgSend$_setinterstitialSuspension:
+ _objc_msgSend$colorSpace
+ _objc_msgSend$end
+ _objc_msgSend$endProposingNewTime:
+ _objc_msgSend$externalContentProtectionStatus
+ _objc_msgSend$frame
+ _objc_msgSend$isHostApplicationInForeground
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$setBorderColor:
+ _objc_msgSend$setBorderWidth:
+ _objc_msgSend$subarrayWithRange:
+ _os_log_create
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _stringWithValidatedFormat
+ _stringWithValidatedFormatArg2
+ _stringWithValidatedFormatString
+ setBounds:.oldRect.0
+ setBounds:.oldRect.1
+ setBounds:.oldRect.2
+ setBounds:.oldRect.3
- +[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:].cold.1
- +[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:].cold.1
- -[AVSampleBufferAudioRenderer setOutputContext:].cold.1
- -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.4
- GCC_except_table102
- GCC_except_table105
- GCC_except_table111
- GCC_except_table133
- GCC_except_table137
- GCC_except_table148
- GCC_except_table158
- GCC_except_table160
- GCC_except_table162
- GCC_except_table169
- GCC_except_table198
- GCC_except_table51
- GCC_except_table92
- _FigSignalErrorAt
- __103+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]_block_invoke.23
- __104-[AVDelegatingPlaybackCoordinator transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:]_block_invoke.105
- __106+[AVAssetWriterWritingHelper finishWritingDelegateOperationWithAssetWriter:andFigAssetWriter:andDelegate:]_block_invoke.548
- __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156
- __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.1
- __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.2
- __114-[AVAssetResourceLoader _performDelegateCallbackSynchronouslyIfCurrentDelegateQueueIsQueue:delegateCallbackBlock:]_block_invoke.189
- __122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.118
- __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke.1153
- __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke_2.1154
- __130-[AVContentKeySession(AVContentKeySessionPrivateUtilities) _invokeDelegateCallbackWithBlock:synchronouslyWhenDelegateQueueIsNULL:]_block_invoke.620
- __188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.151
- __188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke.156
- __21-[AVPlayerLayer init]_block_invoke.83
- __21-[AVPlayerLayer init]_block_invoke.86
- __26-[AVPlayerItem _setAsset:]_block_invoke.513
- __30-[AVPlayerItemTrack isEnabled]_block_invoke.42
- __32-[AVPlayerItemTrack setEnabled:]_block_invoke.43
- __34-[AVPlayerItem _attachToFigPlayer]_block_invoke.472
- __35-[AVPlayer _addPlayerCaptionLayer:]_block_invoke.578
- __35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.234
- __36-[AVPlayerItem setVideoComposition:]_block_invoke.623
- __39-[AVPlayerCaptionLayer layoutSublayers]_block_invoke.10
- __39-[AVPlayerItemTrack setVideoFieldMode:]_block_invoke.56
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.201
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.203
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.210
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke.217
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke_2.206
- __39-[AVPlayerLayer _startObservingPlayer:]_block_invoke_2.213
- __45-[AVPlayer replaceCurrentItemWithPlayerItem:]_block_invoke.511
- __48-[AVCaptionRenderer captionSceneChangesInRange:]_block_invoke.29
- __51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke.533
- __52-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke.42
- __53-[AVPlayerItem _addInterstitialEventCollectorLocked:]_block_invoke.667
- __57-[AVPlayerPlaybackCoordinator setFigPlaybackCoordinator:]_block_invoke.245
- __58-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevel]_block_invoke.31
- __59-[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:]_block_invoke.28
- __60-[AVPlayerItem _ensureAssetWithFigPlaybackItemWithTrackIDs:]_block_invoke.514
- __62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.517
- __63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.150
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.459
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.480
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.485
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.460
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.481
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.464
- __67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke.229
- __67-[AVSampleBufferGeneratorBatch makeDataReadyWithCompletionHandler:]_block_invoke.109
- __69-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]_block_invoke.612
- __70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.123
- __71-[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:]_block_invoke.194
- __71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.37
- __74-[AVDelegatingPlaybackCoordinator setSuspensionReasonsThatTriggerWaiting:]_block_invoke.125
- __78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.24
- __78+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]_block_invoke.25
- __79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.96
- __81-[AVSampleBufferVideoRenderer _computeSampleBufferEnqueueingInfoForSampleBuffer:]_block_invoke.102
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.87
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.72
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.88
- __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.108
- __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.112
- __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.115
- __82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.109
- __87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.579
- __88+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]_block_invoke.135
- __90-[AVDelegatingPlaybackCoordinator setParticipantLimit:forWaitingOutSuspensionsWithReason:]_block_invoke.121
- __91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke.1014
- __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1433
- __97-[AVContentKeySession makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:]_block_invoke.522
- __AVSampleBufferVideoOutput_figVCAvailableImmediate_block_invoke.64
- __Block_byref_object_copy_.102
- __Block_byref_object_copy_.11
- __Block_byref_object_copy_.116
- __Block_byref_object_dispose_.103
- __Block_byref_object_dispose_.117
- __Block_byref_object_dispose_.12
- ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke_2
- ___143-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke_2
- ___188-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke_2
- ___22-[AVPlayer _addLayer:]_block_invoke_2
- ___22-[AVPlayer _addLayer:]_block_invoke_3
- ___31-[AVPlayerItem _updateTimebase]_block_invoke_5
- ___31-[AVPlayerItem _updateTimebase]_block_invoke_6
- ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke_3
- ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke_2
- ___42-[AVPlayerCaptionLayer _interstitialLayer]_block_invoke_2
- ___46-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke_2
- ___46-[AVPlayerPlaybackCoordinator _endSuspension:]_block_invoke_2
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_3
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_4
- ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3
- ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke_2
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke_2
- ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke_2
- ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_2
- ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke_2
- ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_2
- ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke_4
- ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_3
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6
- ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke_2
- ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_2
- ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke_2
- ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke_2
- ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_3
- ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke_2
- ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_3
- ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_3
- ___90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke_2
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_2
- ___avplayer_fpNotificationCallback_block_invoke_4
- ___avplayer_fpNotificationCallback_block_invoke_5
- ___avplayer_fpNotificationCallback_block_invoke_6
- ___avplayeritem_fpItemNotificationCallback_block_invoke_10
- ___avplayeritem_fpItemNotificationCallback_block_invoke_11
- ___avplayeritem_fpItemNotificationCallback_block_invoke_12
- ___avplayeritem_fpItemNotificationCallback_block_invoke_7
- ___avplayeritem_fpItemNotificationCallback_block_invoke_8
- ___avplayeritem_fpItemNotificationCallback_block_invoke_9
- ___block_descriptor_48_e8_32o40b_e24_v16?0"NSNotification"8l
- ___block_descriptor_48_e8_32r_e26_v32?0"AVCaption"8Q16^B24l
- ___block_descriptor_52_e8_32o40o_e31_^{OpaqueFigRoutingContext=}8?0l
- ___handleFigAssetCollectionNotification_block_invoke_2
- ___handleFigAssetTrackNotification_block_invoke_2
- __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1136
- __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1137
- __avplayer_fpNotificationCallback_block_invoke.1155
- __avplayer_fpNotificationCallback_block_invoke.1160
- __avplayer_fpNotificationCallback_block_invoke_2.1157
- __avplayer_fpNotificationCallback_block_invoke_2.1161
- __avplayeritem_fpItemNotificationCallback_block_invoke.1455
- __avplayeritem_fpItemNotificationCallback_block_invoke.1478
- __avplayeritem_fpItemNotificationCallback_block_invoke_10.1490
- __avplayeritem_fpItemNotificationCallback_block_invoke_11.1491
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1456
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1479
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1460
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1480
- __avplayeritem_fpItemNotificationCallback_block_invoke_4.1464
- __avplayeritem_fpItemNotificationCallback_block_invoke_4.1484
- __avplayeritem_fpItemNotificationCallback_block_invoke_5.1471
- __avplayeritem_fpItemNotificationCallback_block_invoke_5.1485
- __avplayeritem_fpItemNotificationCallback_block_invoke_6.1472
- __avplayeritem_fpItemNotificationCallback_block_invoke_6.1486
- __avplayeritem_fpItemNotificationCallback_block_invoke_7.1473
- __avplayeritem_fpItemNotificationCallback_block_invoke_7.1487
- __avplayeritem_fpItemNotificationCallback_block_invoke_8.1477
- __avplayeritem_fpItemNotificationCallback_block_invoke_8.1488
- __avplayeritem_fpItemNotificationCallback_block_invoke_9.1489
- __block_literal_global.101
- __block_literal_global.1029
- __block_literal_global.1031
- __block_literal_global.106
- __block_literal_global.109
- __block_literal_global.112
- __block_literal_global.195
- __block_literal_global.196
- __block_literal_global.199
- __block_literal_global.205
- __block_literal_global.212
- __block_literal_global.255
- __block_literal_global.306
- __block_literal_global.350
- __block_literal_global.353
- __block_literal_global.391
- __block_literal_global.399
- __block_literal_global.423
- __block_literal_global.436
- __block_literal_global.440
- __block_literal_global.444
- __block_literal_global.449
- __block_literal_global.475
- __block_literal_global.528
- __block_literal_global.537
- __block_literal_global.541
- __block_literal_global.566
- __block_literal_global.569
- __block_literal_global.583
- __block_literal_global.653
- __block_literal_global.659
- __block_literal_global.688
- __block_literal_global.860
- __handleFigAssetLoadingNotification_block_invoke.525
CStrings:
+ "\n\t\"%@\""
+ " "
+ "%02x"
+ "%c"
+ "%d bytes [ %@ ] [ %@ ]"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "(OSStatus)error.code"
+ "*** SHOULD NOT receive kFigAssetNotification_PropertyRevised / kFigStdAssetProperty_Duration notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
+ "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigAssetTrackProperty_EditSegmentData notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
+ "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigStdTrackProperty_TimeRange notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
+ "+[AVAnnotationRepresentation _annotationRepresentationWithPropertyList:binaryData:]"
+ "+[AVAssetTrackInspector assetTrackInspectorWithAsset:trackID:trackIndex:]"
+ "+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke"
+ "+[AVContentKeySession copyDefaultSecureStopManagerForAppIdentifier:storageDirectoryAtURL:]"
+ "+[AVDataAsset _getFigAssetCreationOptionsFromDataAssetInitializationOptions:figAssetCreationFlags:]"
+ "+[AVExternalPlaybackMonitor longFormVideoExternalPlaybackMonitor]"
+ "+[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]"
+ "+[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]"
+ "+[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]"
+ "+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
+ "+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]"
+ "+[AVMetadataItemFilterForSharing addIdentifier:toWhitelistDictionary:]"
+ "+[AVOperation(ArrayOfOperations) statusOfOperations:error:]"
+ "+[AVOutputContext defaultOutputContextImplClass]"
+ "+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:]"
+ "+[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors]"
+ "+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2"
+ "+[AVPlayer _createFigPlayerWithType:options:player:]"
+ "+[AVPlayer availableHDRModes]"
+ "+[AVPlayer fireAvailableHDRModesDidChangeNotification]"
+ "+[AVPlayer fireEligibleForHDRPlaybackDidChangeNotification]"
+ "+[AVPlayerItem _createFigPlaybackItemForFigPlayer:asset:URL:flags:options:playbackItem:]"
+ "+[AVPlayerLayer _swapSublayersBetweenPlayerLayer:andPlayerLayer:]"
+ "+[AVRoutingSessionManager longFormVideoRoutingSessionManager]"
+ "+[AVStreamDataParser(AVStreamDataParser_FigManifold) _createBlockBufferUsingNSData:withOffset:withLength:]"
+ "+[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:]"
+ "+[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:]"
+ "+[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) removePendingExpiredSessionReports:withAppIdentifier:]"
+ "+[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:]"
+ "+[AVURLAsset _avfValidationPlist]_block_invoke"
+ "+[AVURLAsset _getFigAssetCreationOptionsFromURLAssetInitializationOptions:assetLoggingIdentifier:figAssetCreationFlags:error:]"
+ ", associatedLayer %p"
+ ", is in playback mode"
+ ", player %p"
+ "- creating video queue failed previously"
+ "-[AVAVAudioSettingsAudioOutputSettings getAudioStreamBasicDescription:forAudioFileTypeID:sourceFormatDescription:]"
+ "-[AVAnnotation getJSONData:representationBinaryDataBindings:]"
+ "-[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:]"
+ "-[AVAsset mediaSelectionGroupForPropertyList:mediaSelectionOption:]"
+ "-[AVAsset(AVAssetChapterInspection) _chapterMetadataGroupsBestMatchingPreferredLanguages:containingItemsWithCommonKeys:]"
+ "-[AVAssetCollection cancelLoading]"
+ "-[AVAssetCollection(AVAssetCollection_Internal) initWithURL:options:]"
+ "-[AVAssetCollectionInspectorLoader _loadStatusForProperty:returningError:]"
+ "-[AVAssetCollectionInspectorLoader _loadingQOnly_figCollection]"
+ "-[AVAssetCollectionInspectorLoader loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke"
+ "-[AVAssetCollectionInspectorLoader statusOfValueForKey:error:]_block_invoke"
+ "-[AVAssetCustomURLBridgeForNSURLProtocol _cancelPendingRequests]"
+ "-[AVAssetDownloadContentConfiguration _createFigContentConfigForEnvironmentalCondition:]"
+ "-[AVAssetDownloadSession initWithAsset:mediaSelections:destinationURL:options:]"
+ "-[AVAssetDownloadSession initWithDownloadToken:]"
+ "-[AVAssetDownloadSession initWithURL:destinationURL:options:]"
+ "-[AVAssetDownloadSession pause]_block_invoke"
+ "-[AVAssetDownloadSession start]"
+ "-[AVAssetDownloadSession stop]_block_invoke"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCacheOnDispatchQueue]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCache]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _readyForInspection]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:options:]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setupFigClientObjectAsync:]_block_invoke_2"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueueFirstTime]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueue]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _verifyDownloadConfigurationForAssetType]"
+ "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) ensureProgressTimerIsRunningOnQueueWithError:]_block_invoke"
+ "-[AVAssetDownloadStorageManager setStorageManagementPolicy:forURL:]"
+ "-[AVAssetDownloadStorageManager storageManagementPolicyForURL:]_block_invoke"
+ "-[AVAssetExportSession initWithAsset:presetName:]"
+ "-[AVAssetExportSession setFileLengthLimit:]"
+ "-[AVAssetExportSession setMaximizePowerEfficiency:]"
+ "-[AVAssetImageGenerator _didGenerateCGImage:]"
+ "-[AVAssetImageGenerator _ensureFigAssetImageGeneratorAllowingSynchronousPropertyLoad:error:]"
+ "-[AVAssetImageGenerator _failedToGenerateCGImage:]"
+ "-[AVAssetImageGenerator cancelAllCGImageGeneration]"
+ "-[AVAssetImageGenerator copyCGImageAtTime:actualTime:error:]"
+ "-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]"
+ "-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke"
+ "-[AVAssetLoggingIdentifier init]"
+ "-[AVAssetMediaSelectionGroup _mediaSelectionOptionWithPropertyList:matchToMediaSelectionArray:]"
+ "-[AVAssetReaderOutput copyNextSampleBuffer]"
+ "-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke"
+ "-[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:]"
+ "-[AVAssetResourceLoadingDataRequest respondWithData:]"
+ "-[AVAssetResourceLoadingRequest _appendToCachedData:]"
+ "-[AVAssetResourceLoadingRequest _appendToCachedData:]_block_invoke"
+ "-[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:]"
+ "-[AVAssetResourceLoadingRequest _sendFinishLoadingToCustomURLHandlerWithError:]"
+ "-[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler]"
+ "-[AVAssetResourceLoadingRequest finishLoadingWithError:]"
+ "-[AVAssetResourceLoadingRequest finishLoading]"
+ "-[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:]"
+ "-[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:]"
+ "-[AVAssetWriter addInput:]"
+ "-[AVAssetWriter addInputGroup:]"
+ "-[AVAssetWriter cancelWriting]"
+ "-[AVAssetWriter endSessionAtSourceTime:]"
+ "-[AVAssetWriter finishWritingWithCompletionHandler:]"
+ "-[AVAssetWriter finishWriting]"
+ "-[AVAssetWriter flushSegment]"
+ "-[AVAssetWriter flush]"
+ "-[AVAssetWriter startSessionAtSourceTime:]"
+ "-[AVAssetWriter startWriting]"
+ "-[AVAssetWriterFinishWritingHelper _finishWritingOperationsDidFinish]"
+ "-[AVAssetWriterFinishWritingHelper initWithConfigurationState:finishWritingOperations:figAssetWriterCallbackContextToken:figAssetWriter:]_block_invoke"
+ "-[AVAssetWriterInput _prepareToFinishWritingReturningError:]"
+ "-[AVAssetWriterInput _setHelper:]_block_invoke"
+ "-[AVAssetWriterInput appendSampleBuffer:]"
+ "-[AVAssetWriterInput markAsFinished]"
+ "-[AVAssetWriterInput markCurrentPassAsFinished]"
+ "-[AVAssetWriterInput requestMediaDataWhenReadyOnQueue:usingBlock:]"
+ "-[AVAssetWriterInput respondToEachPassDescriptionOnQueue:usingBlock:]"
+ "-[AVAssetWriterInputAnnotationAdaptor appendAnnotation:]"
+ "-[AVAssetWriterInputFigAssetWriterEndPassOperation _notifyWhetherMorePassesAreNeeded:timeRanges:forTrackWithID:]"
+ "-[AVAssetWriterInputFigAssetWriterEndPassOperation dealloc]"
+ "-[AVAssetWriterInputFigAssetWriterEndPassOperation start]"
+ "-[AVAssetWriterInputInterPassAnalysisHelper startPassAnalysis]_block_invoke"
+ "-[AVAssetWriterInputMediaDataRequester requestMediaDataIfNecessary]"
+ "-[AVAssetWriterInputMetadataAdaptor appendTimedMetadataGroup:]"
+ "-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]"
+ "-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke"
+ "-[AVAssetWriterInputTerminalHelper appendCaption:error:]"
+ "-[AVAssetWriterInputTerminalHelper appendCaptionGroup:error:]"
+ "-[AVAssetWriterInputTerminalHelper appendPixelBuffer:withPresentationTime:]"
+ "-[AVAssetWriterInputTerminalHelper appendSampleBuffer:error:]"
+ "-[AVAssetWriterInputTerminalHelper appendTaggedPixelBufferGroup:withPresentationTime:]"
+ "-[AVAssetWriterInputWritingHelper appendCaption:error:]"
+ "-[AVAssetWriterInputWritingHelper appendCaptionGroup:error:]"
+ "-[AVAssetWriterInputWritingHelper appendPixelBuffer:withPresentationTime:]"
+ "-[AVAssetWriterInputWritingHelper appendSampleBuffer:error:]"
+ "-[AVAssetWriterInputWritingHelper appendTaggedPixelBufferGroup:withPresentationTime:]"
+ "-[AVAssetWriterInputWritingHelper observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVAssetWriterInputWritingHelper transitionToAndReturnTerminalHelperWithTerminalStatus:]"
+ "-[AVAssetWriterWritingHelper cancelWriting]"
+ "-[AVAssetWriterWritingHelper encryptionScheme]"
+ "-[AVAssetWriterWritingHelper figEncryptionConfigDictionary]"
+ "-[AVAssetWriterWritingHelper finishWritingWithCompletionHandler:]_block_invoke"
+ "-[AVAssetWriterWritingHelper finishWriting]_block_invoke"
+ "-[AVAssetWriterWritingHelper initWithConfigurationState:assetWriter:error:]"
+ "-[AVAssetWriterWritingHelper storageSpacePreallocationSize]"
+ "-[AVAsynchronousCIImageFilteringRequest finishWithError:]"
+ "-[AVAsynchronousCIImageFilteringRequest finishWithImage:context:]"
+ "-[AVAsynchronousCIImageFilteringRequest sourceImage]"
+ "-[AVBlockOperation cancel]"
+ "-[AVBlockOperation start]"
+ "-[AVCallbackContextRegistry registerCallbackContextObject:]_block_invoke"
+ "-[AVCallbackContextRegistry unregisterCallbackContextForToken:]_block_invoke"
+ "-[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession]"
+ "-[AVCaptionRenderer buildFigCaptionArrayFromAVCaptionArrayAndSubmitToRenderSession]_block_invoke"
+ "-[AVCaptionRenderer captionSceneChangesInRange:]"
+ "-[AVCaptionRenderer init]"
+ "-[AVCaptionRenderer renderInContext:atTime:]"
+ "-[AVCaptionRenderer teardownFigCDS]"
+ "-[AVCaptionRenderer teardownFigCaptionClient]"
+ "-[AVClientBlockKVONotifier cancelCallbacks]"
+ "-[AVClientBlockKVONotifier dealloc]"
+ "-[AVClientBlockKVONotifier start]"
+ "-[AVComposition _initWithComposition:]"
+ "-[AVComposition mutableCopyWithZone:]"
+ "-[AVCompositionTrackReaderInspector segments]"
+ "-[AVContentKeyReportGroup _associateRequestWithGroupWithRequestID:error:]"
+ "-[AVContentKeyReportGroup _destroyContentKeyGroupWithError:]"
+ "-[AVContentKeyReportGroup cryptorOptionsForIdentifier:initializationData:formatDescription:hlsMethod:]"
+ "-[AVContentKeyReportGroup failProcessingContentKeyRequestWithIdentifier:initializationData:error:]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:]_block_invoke"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) configureAppIdentifier:]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) copyCryptorForCryptKeyAttributes:]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) createProtectorSessionIdentifierIfNecessary]_block_invoke"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) externalProtectionStatusForCryptor:withDisplays:]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) hasProtector]"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) copyCryptorForIdentifier:initializationData:]_block_invoke"
+ "-[AVContentKeyReportGroup(AVContentKeyReportGroup_Internal) createCryptorIfNecessaryForIdentifier:initializationData:formatDescription:hlsMethod:error:]_block_invoke"
+ "-[AVContentKeyRequest _processContentKeyResponse:renewalDate:initializationVector:error:]"
+ "-[AVContentKeyRequest _processContentKeyResponseError:]"
+ "-[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus]"
+ "-[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:]"
+ "-[AVContentKeySession externalProtectionStateChangedCallbackWithBoss:keySpecifier:]_block_invoke"
+ "-[AVContentKeySession(AVContentKeyRequestSupport) contentKeyRequestDidProduceContentKey:]_block_invoke"
+ "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequest:toDelegateWithCallbackSelector:]"
+ "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequestWithPreloadingRequestOptions:identifier:initializationData:providesPersistableKey:]"
+ "-[AVContentKeySession(AVContentKeyRequestSupport) issueContentKeyRequests:forInitializationData:]"
+ "-[AVContentKeySession(AVContentKeySession_Internal) createAndInstallCustomURLHandlerForAsset:outHandler:]"
+ "-[AVContentKeySession(AVContentKeySession_Internal) issueContentKeyRequestForInitializationData:]"
+ "-[AVContentKeySession(FigContentKeyBoss) _processContentKeyRequestWithIdentifier:encryptionMethod:supportedProtocolVersions:options:groupID:error:]"
+ "-[AVCoordinatedPlaybackSuspension initWithCoordinator:reason:]"
+ "-[AVCoreImageFilterCustomVideoCompositor cancelAllPendingVideoCompositionRequests]"
+ "-[AVCoreImageFilterCustomVideoCompositor renderContextChanged:]"
+ "-[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:]"
+ "-[AVCustomVideoCompositorSession commitCustomVideoCompositorPropertiesAndReturnError:]"
+ "-[AVCustomVideoCompositorSession initWithVideoComposition:]"
+ "-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:]_block_invoke"
+ "-[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _customCompositorFigPropertyDidChange]_block_invoke"
+ "-[AVDateRangeMetadataGroup(AVDateRangeMetadataGroup_Local) _extractPropertiesFromTaggedRangeMetadataDictionary:]"
+ "-[AVDelegatingPlaybackCoordinator _endSuspension:]"
+ "-[AVDelegatingPlaybackCoordinator _endSuspension:proposingNewTime:]"
+ "-[AVDelegatingPlaybackCoordinator _setWaitingPolicies:]"
+ "-[AVDelegatingPlaybackCoordinator applyFigPauseSnapsToMediaTimeOfOriginator]_block_invoke"
+ "-[AVDelegatingPlaybackCoordinator beginSuspensionForReason:]"
+ "-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]"
+ "-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke"
+ "-[AVDelegatingPlaybackCoordinator participantForIdentifier:]_block_invoke"
+ "-[AVExternalPlaybackMonitor dealloc]"
+ "-[AVExternalPlaybackMonitor isAirPlayVideoActive]"
+ "-[AVExternalPlaybackMonitor isAirPlayVideoPlaying]"
+ "-[AVFigAssetInspector _localizedMediaSelectionOptionDisplayNames]"
+ "-[AVFigAssetInspector variants]"
+ "-[AVFigAssetInspectorLoader _loadStatusForProperty:figAsset:error:]"
+ "-[AVFigAssetInspectorLoader _statusOfValueForKey:error:firstNonLoadedDependencyKey:]"
+ "-[AVFigAssetTrackInspector _initWithAsset:trackID:trackIndex:]"
+ "-[AVFigAssetTrackInspector _invokeCompletionHandlerForLoadingBatches:]"
+ "-[AVFigAssetTrackInspector _loadStatusForFigAssetTrackProperty:error:]"
+ "-[AVFigAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:]"
+ "-[AVFigAssetWriterFinishWritingAsyncOperation cancel]"
+ "-[AVFigAssetWriterFinishWritingAsyncOperation didEnterTerminalState]"
+ "-[AVFigAssetWriterFinishWritingAsyncOperation didReceiveFigAssetWriterNotificationWithSuccess:error:]"
+ "-[AVFigAssetWriterFinishWritingAsyncOperation start]"
+ "-[AVFigAssetWriterTrack _refreshAboveHighWaterLevel]_block_invoke"
+ "-[AVFigAssetWriterTrack endPassWithCompletionHandler:]"
+ "-[AVFigAssetWriterTrack setFormatDescriptions:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]_block_invoke"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:]"
+ "-[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl connectedPairedDevices]"
+ "-[AVFigEndpointOutputDeviceImpl deviceSubType]"
+ "-[AVFigEndpointOutputDeviceImpl deviceType]"
+ "-[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]"
+ "-[AVFigEndpointOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigEndpointOutputDeviceImpl isInEar]"
+ "-[AVFigEndpointOutputDeviceImpl isInUseByPairedDevice]"
+ "-[AVFigEndpointOutputDeviceImpl supportsDataOverACLProtocol]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _finishedWithPrompt]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _endpointDescriptorChanged]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _routePresentChanged]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification addPeerToHomeGroup:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:]"
+ "-[AVFigRoutingContextCommandOutputDeviceConfigurationModification stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup]"
+ "-[AVFigRoutingContextOutputContextImpl _canMuteDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _canSetMasterVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _canUseForRoutingContextDidChangeForRoutingContextWIthID:]"
+ "-[AVFigRoutingContextOutputContextImpl _createSelectRouteOptionsForSetOutputDeviceOptions:]"
+ "-[AVFigRoutingContextOutputContextImpl _currentRouteChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _groupConfigurationChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _masterVolumeControlTypeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _masterVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _muteDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _remoteControlChannelAvailabilityChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:]"
+ "-[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]"
+ "-[AVFigRoutingContextOutputContextImpl _serverConnectionDied]"
+ "-[AVFigRoutingContextOutputContextImpl _systemPickerVideoRouteChanged]"
+ "-[AVFigRoutingContextOutputContextImpl addOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl associatedAudioDeviceID]"
+ "-[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:]"
+ "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]"
+ "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]_block_invoke"
+ "-[AVFigRoutingContextOutputContextImpl outputDevice]"
+ "-[AVFigRoutingContextOutputContextImpl removeOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:]"
+ "-[AVFigRoutingContextRouteChangeOperation _routeChangeComplete]"
+ "-[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:]"
+ "-[AVFigRoutingContextRouteChangeOperation _routeChangeStartedWithID:]_block_invoke"
+ "-[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]"
+ "-[AVFigRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]_block_invoke"
+ "-[AVFigRoutingContextRouteChangeOperation start]"
+ "-[AVKVODispatcher observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVKeyPathDependency _reactToSecondLevelPropertyChange:]"
+ "-[AVKeyPathDependency _reactToTopLevelPropertyChange:]"
+ "-[AVKeyPathDependency _reactToTopLevelPropertyChange:]_block_invoke"
+ "-[AVKeyPathDependency _startObservingSecondLevelPropertyOnNewCurrentValueForTopLevelDependencyProperty:]"
+ "-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke"
+ "-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_2"
+ "-[AVManagedAssetCache enableAutomaticCacheSizeManagement]"
+ "-[AVManagedAssetCache initWithURL:enableCRABSCache:enableHLSCache:]"
+ "-[AVManagedAssetCache removeEntryForKey:]"
+ "-[AVManagedAssetCache setMaxEntrySize:]"
+ "-[AVManagedAssetCache setMaxSize:]"
+ "-[AVMapPublisher subscribeRequestingInitialValue:block:]_block_invoke"
+ "-[AVMediaFileSegmenter _createFigMediaFileSegmenterAndBeginSegmenting]_block_invoke"
+ "-[AVMediaFileSegmenter _handleFigMediaFileSegmenterNotification:payload:]"
+ "-[AVMediaFileSegmenter _transitionToStatus:error:]"
+ "-[AVMediaFileSegmenter dealloc]"
+ "-[AVMetadataItem(AVMetadataItem_Local) _extractPropertiesFromDictionary:]"
+ "-[AVMetadataItem(AVMetadataItem_Local) _valueFromCFType:]"
+ "-[AVMovie _initWithFigAsset:]"
+ "-[AVMovie _initWithFigError:userInfo:]"
+ "-[AVMovie _initWithFormatReader:URL:data:options:]"
+ "-[AVMovie initWithData:options:]"
+ "-[AVMovie initWithURL:options:]"
+ "-[AVMovie init]"
+ "-[AVMutableComposition _addMutableTrackWithMediaType:preferredTrackID:fireKVO:]"
+ "-[AVMutableComposition _removeTrack:fireKVO:]"
+ "-[AVMutableComposition insertEmptyTimeRange:]"
+ "-[AVMutableComposition insertTimeRange:ofAsset:atTime:error:]"
+ "-[AVMutableComposition mutableTrackCompatibleWithTrack:]"
+ "-[AVMutableComposition removeTimeRange:]"
+ "-[AVMutableComposition scaleTimeRange:toDuration:]"
+ "-[AVMutableCompositionTrack _insertEmptyTimeRange:fireKVO:]"
+ "-[AVMutableCompositionTrack _insertTimeRange:ofTrack:atTime:fireKVO:error:]"
+ "-[AVMutableCompositionTrack _removeTimeRange:fireKVO:]"
+ "-[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:]"
+ "-[AVMutableCompositionTrack scaleTimeRange:toDuration:]"
+ "-[AVMutableCompositionTrack setSegments:]"
+ "-[AVMutableCompositionTrack validateTrackSegments:error:]"
+ "-[AVMutableMovie _initWithFormatReader:URL:data:options:]"
+ "-[AVMutableMovie initWithData:options:error:]"
+ "-[AVMutableMovie initWithSettingsFromMovie:options:error:]"
+ "-[AVMutableMovie initWithURL:options:error:]"
+ "-[AVMutableMovie setPreferredTransform:]"
+ "-[AVMutableMovieTrack setAlternateGroupID:]"
+ "-[AVMutableMovieTrack setLayer:]"
+ "-[AVMutableMovieTrack setPreferredTransform:]"
+ "-[AVNotificationSubscription cancel]"
+ "-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:]"
+ "-[AVNotificationSubscription initWithObject:notificationName:callbackBlock:]_block_invoke"
+ "-[AVOccasionalTimebaseObserver _effectiveRateChanged]"
+ "-[AVOccasionalTimebaseObserver _fireBlock]"
+ "-[AVOccasionalTimebaseObserver _resetNextFireTime]"
+ "-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]"
+ "-[AVOnceTimebaseObserver _fireBlock]"
+ "-[AVOnceTimebaseObserver _resetNextFireTime]_block_invoke"
+ "-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]"
+ "-[AVOperation _setStatus:error:resultingStatus:failureReason:]_block_invoke"
+ "-[AVOperation didEnterTerminalState]"
+ "-[AVOperation evaluateDependenciesAndMarkAsExecuting]"
+ "-[AVOperation markAsCancelled]"
+ "-[AVOperation markAsCompleted]"
+ "-[AVOperation markAsFailedWithError:]"
+ "-[AVOutputContext ID]"
+ "-[AVOutputContext encodeWithCoder:]"
+ "-[AVOutputContext initWithCoder:]"
+ "-[AVOutputContext initWithOutputContextImpl:]"
+ "-[AVOutputContext outputContextImpl:didExpireWithReplacement:]"
+ "-[AVOutputContext outputDevice]"
+ "-[AVOutputContext outputDevices]"
+ "-[AVOutputContextDestinationChange _setStatus:cancellationReason:]"
+ "-[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:]"
+ "-[AVOutputDevice openCommunicationChannelWithOptions:completionHandler:]"
+ "-[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:]"
+ "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]"
+ "-[AVOutputDeviceAuthorizationSession setDelegate:]"
+ "-[AVOutputDeviceDiscoverySession availableOutputDevices]"
+ "-[AVOutputDeviceDiscoverySession devicePresenceDetected]"
+ "-[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:]"
+ "-[AVOutputDeviceDiscoverySession setTargetAudioSession:]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices recentlyUsedDevices]"
+ "-[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:]"
+ "-[AVOutputDeviceGroup outputDevices]"
+ "-[AVOutputDeviceHID initWithUUID:screenUUID:endpoint:]"
+ "-[AVOutputDeviceIcon initWithDict:]"
+ "-[AVOutputDeviceScreenBorrowToken initWithEndpoint:client:reason:]"
+ "-[AVOutputDeviceScreenInfo initWithDict:]"
+ "-[AVOutputDeviceTurnByTurnToken dealloc]"
+ "-[AVOutputDeviceTurnByTurnToken initWithEndpoint:]"
+ "-[AVOutputDeviceViewAreaInfo initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:]"
+ "-[AVPeriodicTimebaseObserver _effectiveRateChanged]"
+ "-[AVPeriodicTimebaseObserver _fireBlockForTime:]"
+ "-[AVPeriodicTimebaseObserver _handleTimeDiscontinuity]"
+ "-[AVPeriodicTimebaseObserver _resetNextFireTime]"
+ "-[AVPlayer _addLayer:]"
+ "-[AVPlayer _addLayer:]_block_invoke"
+ "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]"
+ "-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke"
+ "-[AVPlayer _attachVideoLayersToFigPlayer]"
+ "-[AVPlayer _closedCaptionLayers]"
+ "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]"
+ "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke"
+ "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2"
+ "-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4"
+ "-[AVPlayer _detachVideoLayersFromFigPlayer:]"
+ "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]"
+ "-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke"
+ "-[AVPlayer _handleSetRate:withVolumeRampDuration:playImmediately:rateChangeReason:affectsCoordinatedPlayback:]_block_invoke"
+ "-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_2"
+ "-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]"
+ "-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]"
+ "-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]"
+ "-[AVPlayer _updateDecoderPixelBufferAttributes:onFigPlayer:]"
+ "-[AVPlayer _videoLayers]"
+ "-[AVPlayer prepareItem:withCompletionHandler:]"
+ "-[AVPlayer removeTimeObserver:]"
+ "-[AVPlayer seekToDate:completionHandler:]"
+ "-[AVPlayer seekToTime:completionHandler:]"
+ "-[AVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:]"
+ "-[AVPlayer setAudiovisualBackgroundPlaybackPolicy:]"
+ "-[AVPlayer setDefaultRate:]"
+ "-[AVPlayer setExpectedAssetTypes:]"
+ "-[AVPlayer setExpectedAssetTypes:]_block_invoke_2"
+ "-[AVPlayer setExternalPlaybackVideoGravity:]"
+ "-[AVPlayer setOutputContext:]"
+ "-[AVPlayer setPlayerRole:synchronously:]"
+ "-[AVPlayer setResourceConservationLevelWhilePaused:]"
+ "-[AVPlayer setShouldReduceResourceUsage:]"
+ "-[AVPlayer(AVPlayerAdvanceWithOverlap) _setSupportsAdvanceTimeForOverlappedPlayback:]"
+ "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]_block_invoke"
+ "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _hasCurrentInterstitialEvent]"
+ "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _linkAndSyncAudioSessionWithInterstitialPlayer:]"
+ "-[AVPlayer(AVPlayerPIPSupport) setBackgroundPIPAuthorizationToken:]"
+ "-[AVPlayer(AVPlayerSpeedRamp) setSupportsSpeedRamps:]"
+ "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]"
+ "-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke"
+ "-[AVPlayer(PlaybackCoordination) _ensureFigPlaybackCoordinatorIsConnected]"
+ "-[AVPlayerCaptionLayer _interstitialLayer]"
+ "-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke"
+ "-[AVPlayerCaptionLayer _startObservingPlayer:]"
+ "-[AVPlayerCaptionLayer _stopObservingPlayer:]"
+ "-[AVPlayerCaptionLayer layoutSublayers]"
+ "-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke"
+ "-[AVPlayerCaptionLayer setBounds:]"
+ "-[AVPlayerCaptionLayer setCaptionContentInsets:]"
+ "-[AVPlayerCaptionLayer setPlayer:]"
+ "-[AVPlayerCaptionLayer setValue:forKeyPath:]"
+ "-[AVPlayerConnection addItemToPlayQueueAfterPlaybackItemOfItem:]"
+ "-[AVPlayerItem _addToPlayQueueOfFigPlayerOfPlayer:afterFigPlaybackItemOfItem:]"
+ "-[AVPlayerItem _applyCurrentVideoComposition]"
+ "-[AVPlayerItem _applyMediaSelectionOptions]_block_invoke"
+ "-[AVPlayerItem _attachToFigPlayer]"
+ "-[AVPlayerItem _attachToPlayer:]"
+ "-[AVPlayerItem _cancelPendingSeekAndRegisterSeekID:withCompletionHandler:]"
+ "-[AVPlayerItem _changeStatusToFailedWithError:]"
+ "-[AVPlayerItem _configurePlaybackItemAndReturnError:]"
+ "-[AVPlayerItem _currentMediaSelectionFromFigSelectedMediaArray:]"
+ "-[AVPlayerItem _invokeReadyForEnqueueingHandlers]"
+ "-[AVPlayerItem _makeReadyForEnqueueingWithCompletionHandler:]"
+ "-[AVPlayerItem _postSeekCompletionNotificationWithSeekID:andResult:]"
+ "-[AVPlayerItem _presentationSize]"
+ "-[AVPlayerItem _seekToTime:toleranceBefore:toleranceAfter:seekID:completionHandler:]"
+ "-[AVPlayerItem _selectMediaOption:inMediaSelectionGroup:]"
+ "-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]"
+ "-[AVPlayerItem _setAudioProcessingEffectsAccordingToInputParameters:forTrackID:]"
+ "-[AVPlayerItem _setCurrentMediaSelection:]"
+ "-[AVPlayerItem _setVideoCompositionInstructions:]"
+ "-[AVPlayerItem _tracks]"
+ "-[AVPlayerItem _unregisterInvokeAndReleasePendingSeekCompletionHandlerForSeekID:finished:]"
+ "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]"
+ "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]_block_invoke"
+ "-[AVPlayerItem _updateTimebase]_block_invoke_2"
+ "-[AVPlayerItem currentMediaSelection]"
+ "-[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:]"
+ "-[AVPlayerItem seekToDate:completionHandler:]"
+ "-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]_block_invoke"
+ "-[AVPlayerItem(AVPlayerItemOutputs) _evaluateMetadataOutputs]_block_invoke"
+ "-[AVPlayerItem(AVPlayerItemVideoEnhancement) setVideoEnhancementMode:]"
+ "-[AVPlayerItemLegibleOutput _pushAttributedStrings:andSampleBuffers:atItemTime:]_block_invoke"
+ "-[AVPlayerItemLegibleOutput _signalFlush]"
+ "-[AVPlayerItemLegibleOutput _signalFlush]_block_invoke"
+ "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _pushTimedMetadataGroups:fromPlayerItemTrack:]_block_invoke_3"
+ "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke"
+ "-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_2"
+ "-[AVPlayerItemOutput _itemTimeForHostTimeAsCMTime:]"
+ "-[AVPlayerItemRenderedLegibleOutput _pushRenderedCaptionImages:atItemTime:]_block_invoke"
+ "-[AVPlayerItemRenderedLegibleOutput _signalFlush]"
+ "-[AVPlayerItemRenderedLegibleOutput _signalFlush]_block_invoke"
+ "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke"
+ "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke_2"
+ "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:]_block_invoke"
+ "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:]_block_invoke_2"
+ "-[AVPlayerItemSampleBufferOutput copyNextSampleBufferForTrackID:flags:]"
+ "-[AVPlayerItemTrack setVideoFieldMode:]"
+ "-[AVPlayerItemTrack(AVPlayerItemOutputs) addOutput:]"
+ "-[AVPlayerItemTrack(AVPlayerItemOutputs) removeOutput:]"
+ "-[AVPlayerItemVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:]"
+ "-[AVPlayerItemVideoOutput _dispatchOutputMediaDataWillChange]_block_invoke"
+ "-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed]"
+ "-[AVPlayerItemVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke"
+ "-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeAsSoonAsPossible]_block_invoke"
+ "-[AVPlayerItemVideoOutput requestNotificationOfMediaDataChangeWithAdvanceInterval:]_block_invoke"
+ "-[AVPlayerItemVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:]"
+ "-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:]"
+ "-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:]_block_invoke"
+ "-[AVPlayerLayer _displaySize]"
+ "-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:]"
+ "-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:]_block_invoke"
+ "-[AVPlayerLayer _forceLayout]"
+ "-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke"
+ "-[AVPlayerLayer _handleNonForcedSubtitleDisplayDidChange:player:]_block_invoke"
+ "-[AVPlayerLayer _interstitialLayer]"
+ "-[AVPlayerLayer _leavePIPModeForLayer:]"
+ "-[AVPlayerLayer _notifyPlayerOfDisplaySize]"
+ "-[AVPlayerLayer _percentCoverageRelativeToRootLayer]"
+ "-[AVPlayerLayer _restoreClientLayers:intoMaskLayer:]"
+ "-[AVPlayerLayer _setPlayer:forPIP:]"
+ "-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke"
+ "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]"
+ "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke"
+ "-[AVPlayerLayer _setSublayersForPIP:]"
+ "-[AVPlayerLayer _startObservingPlayer:]"
+ "-[AVPlayerLayer _stopObservingPlayer:]"
+ "-[AVPlayerLayer _updateReadyForDisplayForPlayerCurrentItem]_block_invoke"
+ "-[AVPlayerLayer addSublayer:]"
+ "-[AVPlayerLayer copyDisplayedPixelBuffer]"
+ "-[AVPlayerLayer init]"
+ "-[AVPlayerLayer insertSublayer:above:]"
+ "-[AVPlayerLayer insertSublayer:atIndex:]"
+ "-[AVPlayerLayer insertSublayer:below:]"
+ "-[AVPlayerLayer layerDidBecomeVisible:]"
+ "-[AVPlayerLayer layoutSublayers]"
+ "-[AVPlayerLayer layoutSublayers]_block_invoke"
+ "-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke"
+ "-[AVPlayerLayer pixelBufferAttributes]"
+ "-[AVPlayerLayer removeFromSuperlayer]"
+ "-[AVPlayerLayer replaceSublayer:with:]"
+ "-[AVPlayerLayer setBounds:]"
+ "-[AVPlayerLayer setForScrubbingOnly:]"
+ "-[AVPlayerLayer setLanczosFilterDownscaleFactor:]"
+ "-[AVPlayerLayer setLegibleContentInsets:]"
+ "-[AVPlayerLayer setSublayers:]"
+ "-[AVPlayerLoggingIdentifier init]"
+ "-[AVPlayerLooper _calculateNumberOfCopiesNeeded]"
+ "-[AVPlayerLooper _changeStatusToFailedWithError:]"
+ "-[AVPlayerLooper _changeStatusToFailedWithError:]_block_invoke"
+ "-[AVPlayerLooper _setupLoopingReturningError:]"
+ "-[AVPlayerLooper _setupLoopingReturningError:]_block_invoke"
+ "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]"
+ "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]_block_invoke"
+ "-[AVPlayerLooper initWithPlayer:templateItem:timeRange:existingItemsOrdering:]_block_invoke_2"
+ "-[AVPlayerLooper observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke"
+ "-[AVPlayerPlaybackCoordinator _applyIntegratedTimelineSeek:]"
+ "-[AVPlayerPlaybackCoordinator _convertToMediaTimeForTime:withNetworkTime:rate:]"
+ "-[AVPlayerPlaybackCoordinator _endSuspension:]"
+ "-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]"
+ "-[AVPlayerPlaybackCoordinator _reactToNewDelegate]"
+ "-[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectations]"
+ "-[AVPlayerPlaybackCoordinator _setIntegratedTimelineCreatingNew:]"
+ "-[AVPlayerPlaybackCoordinator _setInterstitialActive:]"
+ "-[AVPlayerPlaybackCoordinator _synchronizeWorkOnPlayerQueue:]"
+ "-[AVPlayerPlaybackCoordinator _updateCoordinationMediumDelegateOnFigPlaybackCoordinator]"
+ "-[AVPlayerPlaybackCoordinator _updateLocalParticipantUUIDOnFigPlaybackCoordinator:]_block_invoke"
+ "-[AVPlayerPlaybackCoordinator _updateParticipantStateOnFigPlaybackCoordinatorForItemWithIdentifier:]"
+ "-[AVPlayerPlaybackCoordinator _updatePauseSnapsToMediaTimeOfOriginatorOnFigPlaybackCoordinator]_block_invoke"
+ "-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:]"
+ "-[AVPlayerPlaybackCoordinator _updateWaitingPoliciesOnFigPlaybackCoordinator:]"
+ "-[AVPlayerPlaybackCoordinator beginSuspensionForReason:]"
+ "-[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:]"
+ "-[AVPlayerPlaybackCoordinator participantForIdentifier:]_block_invoke"
+ "-[AVPlayerRateState rateStateBySettingRate:nameForLogging:]"
+ "-[AVPlayerRateState rateStateByUpdatingBasedOnFigPlayer:hasCurrentItem:hasCurrentInterstitialEvent:nameForLogging:]"
+ "-[AVPlayerRateState rateStateByUpdatingBasedOnPresenceOfCurrentInterstitialEvent:nameForLogging:]"
+ "-[AVPlayerVideoOutput _attachToPlayer:exceptionReason:]_block_invoke"
+ "-[AVPlayerVideoOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue]"
+ "-[AVPlayerVideoOutput _handleVideoReceiverActiveConfigurationChanged:]"
+ "-[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:]"
+ "-[AVPlayerVideoOutput hasNewTaggedBufferGroupForHostTime:]"
+ "-[AVPropertyValuePublisher subscribeRequestingInitialValue:block:]"
+ "-[AVPropertyValuePublisher subscribeRequestingInitialValue:block:]_block_invoke"
+ "-[AVQueuePlayer insertItem:afterItem:]"
+ "-[AVQueuePlayer removeAllItems]"
+ "-[AVQueuePlayer removeItem:]"
+ "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) canOverlapPlaybackFromPlayerItem:toPlayerItem:]"
+ "-[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation _routeConfigUpdateWithID:endedWithReason:]"
+ "-[AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation start]"
+ "-[AVRouteDetector _updateMultipleRoutesDetected]"
+ "-[AVRouteDetector _updateRouteDetectionEnabled]"
+ "-[AVRoutingSessionManager allLikelyDestinations]"
+ "-[AVRoutingSessionManager currentRoutingSession]"
+ "-[AVRoutingSessionManager dealloc]"
+ "-[AVRoutingSessionManager likelyExternalDestinations]"
+ "-[AVRoutingSessionManager prefersLikelyDestinationsOverCurrentRoutingSession]"
+ "-[AVSampleBufferAudioRenderer _installNotificationHandlers]"
+ "-[AVSampleBufferAudioRenderer _transitionToStatus:error:]"
+ "-[AVSampleBufferAudioRenderer _uninstallNotificationHandlers]"
+ "-[AVSampleBufferAudioRenderer allowedAudioSpatializationFormats]"
+ "-[AVSampleBufferAudioRenderer audioOutputDeviceUniqueID]"
+ "-[AVSampleBufferAudioRenderer audioTapProcessor]"
+ "-[AVSampleBufferAudioRenderer audioTimePitchAlgorithm]"
+ "-[AVSampleBufferAudioRenderer copyFigSampleBufferAudioRenderer:]"
+ "-[AVSampleBufferAudioRenderer dealloc]"
+ "-[AVSampleBufferAudioRenderer enqueueSampleBuffer:]"
+ "-[AVSampleBufferAudioRenderer error]"
+ "-[AVSampleBufferAudioRenderer flushFromSourceTime:completionHandler:]"
+ "-[AVSampleBufferAudioRenderer flush]"
+ "-[AVSampleBufferAudioRenderer init]"
+ "-[AVSampleBufferAudioRenderer isMuted]"
+ "-[AVSampleBufferAudioRenderer isReadyForMoreMediaData]"
+ "-[AVSampleBufferAudioRenderer outputContext]"
+ "-[AVSampleBufferAudioRenderer requestMediaDataWhenReadyOnQueue:usingBlock:]"
+ "-[AVSampleBufferAudioRenderer scheduledAudioParameters]"
+ "-[AVSampleBufferAudioRenderer setAllowedAudioSpatializationFormats:]"
+ "-[AVSampleBufferAudioRenderer setAudioOutputDeviceUniqueID:]"
+ "-[AVSampleBufferAudioRenderer setAudioTapProcessor:]"
+ "-[AVSampleBufferAudioRenderer setAudioTimePitchAlgorithm:]"
+ "-[AVSampleBufferAudioRenderer setIsUnaccompaniedByVisuals:]"
+ "-[AVSampleBufferAudioRenderer setMuted:]"
+ "-[AVSampleBufferAudioRenderer setOutputContext:]"
+ "-[AVSampleBufferAudioRenderer setRenderSynchronizer:error:]"
+ "-[AVSampleBufferAudioRenderer setScheduledAudioParameters:]"
+ "-[AVSampleBufferAudioRenderer setVolume:]"
+ "-[AVSampleBufferAudioRenderer status]"
+ "-[AVSampleBufferAudioRenderer stopRequestingMediaData]"
+ "-[AVSampleBufferAudioRenderer timebase]"
+ "-[AVSampleBufferAudioRenderer volume]"
+ "-[AVSampleBufferAudioRendererLoggingIdentifier init]"
+ "-[AVSampleBufferDisplayLayer _updateLayerTreeGeometryWithVideoGravity:presentationSize:videoGravityShouldTriggerAnimation:]_block_invoke"
+ "-[AVSampleBufferDisplayLayer dealloc]"
+ "-[AVSampleBufferDisplayLayer init]"
+ "-[AVSampleBufferDisplayLayer layerDidBecomeVisible:]"
+ "-[AVSampleBufferDisplayLayer layoutSublayers]"
+ "-[AVSampleBufferDisplayLayer setBounds:]"
+ "-[AVSampleBufferDisplayLayer videoRect]"
+ "-[AVSampleBufferDisplayLayer(AVSampleBufferDisplayLayerQueueManagement) enqueueSampleBuffer:]"
+ "-[AVSampleBufferRenderSynchronizer _setRate:time:atHostTime:]"
+ "-[AVSampleBufferRenderSynchronizer dealloc]"
+ "-[AVSampleBufferRenderSynchronizer init]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]_block_invoke"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _scheduleTimedRendererRemovalAtTime:atTime:withClientCompletionHandler:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) addRenderer:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _canAddRendererInternal:error:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererRestrictions) _rendererConfigurationIsValid:]"
+ "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerTimeObservation) removeTimeObserver:]"
+ "-[AVSampleBufferVideoOutput _configureWithVideoQueue:]"
+ "-[AVSampleBufferVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:]"
+ "-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed]"
+ "-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed]_block_invoke"
+ "-[AVSampleBufferVideoOutput copyLastPixelBuffer:]"
+ "-[AVSampleBufferVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:]"
+ "-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]"
+ "-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]"
+ "-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke"
+ "-[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:]"
+ "-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]"
+ "-[AVSampleBufferVideoRenderer _flushComplete]"
+ "-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]"
+ "-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke"
+ "-[AVSampleBufferVideoRenderer _setOutputObscuredDueToInsufficientExternalProtection:]"
+ "-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]"
+ "-[AVSampleBufferVideoRenderer addSampleBufferDisplayLayer:]"
+ "-[AVSampleBufferVideoRenderer addVideoTarget:]"
+ "-[AVSampleBufferVideoRenderer createVideoQueue:]"
+ "-[AVSampleBufferVideoRenderer dealloc]"
+ "-[AVSampleBufferVideoRenderer enqueueSampleBuffer:]"
+ "-[AVSampleBufferVideoRenderer enqueueSampleBuffer:bufferEnqueueingInfo:]"
+ "-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]"
+ "-[AVSampleBufferVideoRenderer requestMediaDataWhenReadyOnQueue:usingBlock:]"
+ "-[AVSampleBufferVideoRenderer setControlTimebase:]"
+ "-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]"
+ "-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]_block_invoke"
+ "-[AVSampleBufferVideoRenderer setRenderSynchronizer:error:]"
+ "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) addOutput:]"
+ "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) copyDisplayedPixelBuffer]"
+ "-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererOutputs) removeOutput:]"
+ "-[AVSampleBufferVideoRenderer(PowerOptimization) expectMinimumUpcomingSampleBufferPresentationTime:]"
+ "-[AVSampleCursor createSampleBufferForCurrentSampleReturningError:]"
+ "-[AVSampleCursor createSampleBufferFromCurrentSampleToEndCursor:error:]"
+ "-[AVSampleCursor stepByDecodeTime:wasPinned:]"
+ "-[AVSampleCursor stepByPresentationTime:wasPinned:]"
+ "-[AVScheduledAudioParameters initWithPropertyList:]"
+ "-[AVScheduledAudioParameters(AVScheduledAudioParameters_Internal) _setRamp:]"
+ "-[AVScheduledFloatValueRamp _interpolatedValueAtTime:]"
+ "-[AVSinkSubscriber cancel]"
+ "-[AVSpecifiedLoggingIdentifier initWithSpecifiedName:]"
+ "-[AVStreamDataParser _appendStreamData:withFlags:]"
+ "-[AVStreamDataParser _createAssetIfNecessary]"
+ "-[AVStreamDataParser dealloc]"
+ "-[AVStreamDataParser init]"
+ "-[AVStreamDataParser providePendingMediaData]"
+ "-[AVStreamDataParser setShouldProvideMediaData:forTrackID:]"
+ "-[AVStreamDataParser(AVStreamDataParserSandboxedParsing) setPreferSandboxedParsing:]_block_invoke"
+ "-[AVStreamDataParser(AVStreamDataParser_ContentKeySessionDelegate) contentKeySession:didProvideContentKeyRequest:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:discoveredNewTrackID:mediaType:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:pushedSampleBuffer:trackID:flags:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:trackDidEnd:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifoldAllNewTracksReady:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _registerForFigManifoldCallbacksForTrackID:]"
+ "-[AVStreamDataParser(AVStreamDataParser_FigManifold) _unregisterForFigManifoldCallbacksForTrackID:]"
+ "-[AVStreamSession addStreamDataParser:]_block_invoke"
+ "-[AVStreamSession dealloc]"
+ "-[AVStreamSession expire]"
+ "-[AVStreamSession initWithStorageDirectoryAtURL:]"
+ "-[AVStreamSession init]"
+ "-[AVStreamSession removeStreamDataParser:]_block_invoke"
+ "-[AVStreamSession(AVStreamSession_Internal) figCPEProtector:]_block_invoke"
+ "-[AVStreamSession(AVStreamSession_Internal) setAppIdentifier:]_block_invoke"
+ "-[AVStreamSession(AVStreamSession_Internal) setFigCPEProtectorSessionIdentifier:]_block_invoke"
+ "-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke"
+ "-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:]_block_invoke_2"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]_block_invoke"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:]"
+ "-[AVTimebaseObserver _finishInitializationWithTimerEventHandler:]"
+ "-[AVTrackReaderInspector _initWithAsset:trackID:trackIndex:]"
+ "-[AVURLAsset _ensureAssetDownloadCache]_block_invoke"
+ "-[AVURLAsset initWithFigCreationOptions:options:figAssetCreationOptions:figAssetCreationFlags:]"
+ "-[AVURLAsset initWithURL:options:]"
+ "-[AVURLAsset(AVURLAssetContentKeyEligibilityInternal) _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:]"
+ "-[AVURLAsset(AVURLAssetURLHandlingInternal) _resourceLoaderWithRemoteHandlerContext:]_block_invoke"
+ "-[AVVideoComposition _copyFigVideoCompositor:andSession:recyclingSession:forFigRemaker:error:]"
+ "-[AVVideoComposition init]"
+ "-[AVVideoCompositionInstruction dictionaryRepresentation]"
+ "-[AVVideoCompositionRenderContext newPixelBuffer]_block_invoke"
+ "-[AVVideoCompositionRenderContext(Internal) initWithFigVideoCompositor:clientRequiredPixelBufferAttributes:videoComposition:pixelBufferPool:]"
+ "-[AVVideoCompositionRenderContext(Internal) pixelBufferPool]"
+ "-[AVVideoOutputSpecification setOutputSettings:forTagCollection:]"
+ "-[AVWeakReferencingDelegateStorage setDelegate:queue:]"
+ "-[AVWeaklyObservedObjectClientBlockKVONotifier cancelCallbacks]"
+ "-[AVWeaklyObservedObjectClientBlockKVONotifier start]"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
+ "/AppleInternal/Library/BuildRoots/625b24dd-0881-11f0-9501-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"
+ "<<<< AVAnnotation >>>> %s: Annotation failed to create formatted date from %@."
+ "<<<< AVAnnotation >>>> %s: Failed to create AVAnnotation: %@"
+ "<<<< AVAnnotation >>>> %s: Unknown annotation representation type: %@"
+ "<<<< AVAnnotation >>>> %s: Unknown annotation representation version %@."
+ "<<<< AVAnnotation >>>> %s: Unknown annotation version %@."
+ "<<<< AVAsset >>>>"
+ "<<<< AVAsset >>>> %s: %@ <%p> FigAssetCopyAssetWithDownloadToken for downloadToken %llu returned %d"
+ "<<<< AVAsset >>>> %s: %@ Created %p"
+ "<<<< AVAsset >>>> %s: %@ Received notification for %@"
+ "<<<< AVAsset >>>> %s: %@ creating AVFigAssetInspectorLoader"
+ "<<<< AVAsset >>>> %s: %@ failed to create AVFigAssetInspectorLoader"
+ "<<<< AVAsset >>>> %s: %s"
+ "<<<< AVAsset >>>> %s: *** Could not canonicalize language: %@. ***"
+ "<<<< AVAsset >>>> %s: *** MediaValidator.plist was not loaded for this platform! Defaulting to no video support. ***"
+ "<<<< AVAsset >>>> %s: <%p> called for property list %@, mediaSelectionOptionOut = <%p>"
+ "<<<< AVAsset >>>> %s: <%p> resolved to group %@ and option %@"
+ "<<<< AVAsset >>>> %s: AVURLAssetHTTPHeaderFieldsKey must be a dictionary"
+ "<<<< AVAsset >>>> %s: Cannot create AVAssetDownloadCache when an AVManagedAssetCache is already present."
+ "<<<< AVAsset >>>> %s: _URLAsset->resourceLoader was unexpectedly non-nil"
+ "<<<< AVAsset >>>> %s: asset created with AVAssetPrefersSandboxedParsingOptionKey"
+ "<<<< AVAsset >>>> %s: asset created with AVAssetRequiresInProcessOperationKey"
+ "<<<< AVAsset >>>> %s: creating AVAssetInspectorLoader"
+ "<<<< AVAsset >>>> %s: using custom AVAssetInspectorLoader"
+ "<<<< AVAssetCache >>>> %s: Enabling AutomaticCacheSizeManagement"
+ "<<<< AVAssetCache >>>> %s: Initialized with URL %@"
+ "<<<< AVAssetCache >>>> %s: Remove entry with key = %@"
+ "<<<< AVAssetCache >>>> %s: Set maxEntrySize = %lld"
+ "<<<< AVAssetCache >>>> %s: Set maxSize = %lld"
+ "<<<< AVAssetCollection >>>> %s: [super init] failed"
+ "<<<< AVAssetCollection >>>> %s: cancelLoading"
+ "<<<< AVAssetCollection >>>> %s: init AVAssetCollectionInternal alloc or init failed"
+ "<<<< AVAssetCollection >>>> %s: init with URL \"%@\""
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: FigAssetCollectionFactoryCreateCollectionWithURL \"%@\" failed (%ld)"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: FigAssetGetStatusOfValueForProperty for property <%@> returned %ld and load error %ld"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: dispatching completion handler [%p]"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: got notification <%@> for batchID %@"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: invoked with unrecognized key %@"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: loading batch [%p] has count of %d on entry"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: loading batch [%p] has count of %d on exit with %@"
+ "<<<< AVAssetCollectionInspectorLoader >>>> %s: storing loading batch [%p] with %@"
+ "<<<< AVAssetCustomURL >>>> %s: cancelling abandoned AVNSURLProtocolRequest %p"
+ "<<<< AVAssetDownloadSession >>>>"
+ "<<<< AVAssetDownloadSession >>>> %s: %p downloaded %lld / %lld"
+ "<<<< AVAssetDownloadSession >>>> %s: Failed to download to destination - %@"
+ "<<<< AVAssetDownloadSession >>>> %s: Failed to load property %@ - %@"
+ "<<<< AVAssetDownloadSession >>>> %s: Failed to make ready for inspection - %@"
+ "<<<< AVAssetDownloadSession >>>> %s: Failed to prime cache - %@"
+ "<<<< AVAssetDownloadSession >>>> %s: Failed to start - %@"
+ "<<<< AVAssetDownloadSession >>>> %s: Must initialize AVAssetDownloadSession with initWithAsset:destinationURL:options: for streaming assets."
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Called"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Called with %lld"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Called with asset:%@ destinationURL:%@"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Download %s"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Download from %@ to %@"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] FigAssetCreateWithURL for URL <%@> returned %d"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Going from paused to start download"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Pause download"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Priming cache with download token %@"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Start download"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] Stop download"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@ payload %@"
+ "<<<< AVAssetDownloadSession >>>> %s: [%p] loaded assetType:[%s] loadingStatus:%d error:%@"
+ "<<<< AVAssetDownloadStorageManager >>>> %s: Set storageManagementPolicy %@ for asset at URL %@"
+ "<<<< AVAssetDownloadStorageManager >>>> %s: StorageManagementPolicy for asset at URL %@ is  %@ "
+ "<<<< AVAssetExportSession >>>> %s: Could not create fig export session. err=%d"
+ "<<<< AVAssetExportSession >>>> %s: fileLengthLimit: %lld"
+ "<<<< AVAssetExportSession >>>> %s: maximize power efficiency %s"
+ "<<<< AVAssetExportSession >>>> %s: no asset, no presetName, or no export settings => nil: asset=%@, presetName=%@"
+ "<<<< AVAssetExportSession >>>> %s: no export session => nil"
+ "<<<< AVAssetImageGenerator >>>> %s: Creating FigAssetImageGenerator from FigAsset"
+ "<<<< AVAssetImageGenerator >>>> %s: called"
+ "<<<< AVAssetImageGenerator >>>> %s: calling FigAssetImageGeneratorCopyCGImageAtTime time %.3f options %@"
+ "<<<< AVAssetImageGenerator >>>> %s: calling FigAssetImageGeneratorRequestCGImageAtTimeAsync time %.3f options %@"
+ "<<<< AVAssetImageGenerator >>>> %s: calling handler with cancelled status"
+ "<<<< AVAssetImageGenerator >>>> %s: calling handler with failed status, error %@"
+ "<<<< AVAssetImageGenerator >>>> %s: calling handler with failed status, error %d"
+ "<<<< AVAssetImageGenerator >>>> %s: calling handler with succeeded status, actualTime %.3f"
+ "<<<< AVAssetImageGenerator >>>> %s: composition => using AVAssetReader"
+ "<<<< AVAssetImageGenerator >>>> %s: no FigAssetImageGenerator instance!"
+ "<<<< AVAssetImageGenerator >>>> %s: not a composition => using FigAssetImageGenerator"
+ "<<<< AVAssetInspector >>>> %s: %p cannot create AVAssetVariant for %@"
+ "<<<< AVAssetInspector >>>> %s: The collection of localized media selection option display names for key \"%@\" has class %@ instead of NSDictionary"
+ "<<<< AVAssetInspector >>>> %s: The top-level object for localized media selection option display names has class %@ instead of NSDictionary"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> FigAssetGetStatusOfValueForProperty for property <%@> returned %d and load error %d - %@"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> dispatching completion handler [%p]"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> got notification <%@>"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> got notification <%@> for batchID %@"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> invoking completion handler [%p] immediately"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> loadValuesAsynchronouslyForKeys:%@ keysForCollectionKeys:%@ completionHandler:<%p>"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> loading batch [%p] has count of %d on entry"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> loading batch [%p] has count of %d on exit with %@"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> status requested for key %@ after loading was canceled"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> storing completion handler [%p] for later invocation"
+ "<<<< AVAssetInspectorLoader >>>> %s: <%p> storing loading batch [%p] with %@"
+ "<<<< AVAssetInspectorLoader >>>> %s: FigAssetCreateWithURL for URL <%@> returned %d"
+ "<<<< AVAssetInspectorLoader >>>> %s: Received %@ from %p (payload: %@)"
+ "<<<< AVAssetReaderOutput >>>> %s: %p received %@"
+ "<<<< AVAssetReaderOutput >>>> %s: %p received %@, extractionID=%d"
+ "<<<< AVAssetReaderOutput >>>> %s: FigAssetReaderExtractAndRetainNextSampleBuffer returned %d, extractionComplete=%d, sampleBuffer=%p, self=%p"
+ "<<<< AVAssetResourceLoader >>>>"
+ "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoader delegate does not respond to selector %@"
+ "<<<< AVAssetResourceLoader >>>> %s: AVAssetResourceLoaderDelegate for AVAssetResourceLoader %@ is gone"
+ "<<<< AVAssetResourceLoader >>>> %s: [AVAssetResourceLoadingRequest finishLoading] is called for a content key request while an AVContentKeySession instance is attached to AVURLAsset. Generating event"
+ "<<<< AVAssetResourceLoader >>>> %s: cached data has grown to length %lld for %@"
+ "<<<< AVAssetResourceLoader >>>> %s: caching data for current offset %lld of length %lld that was provided to %@"
+ "<<<< AVAssetResourceLoader >>>> %s: called on %@"
+ "<<<< AVAssetResourceLoader >>>> %s: called with error %@ on %@"
+ "<<<< AVAssetResourceLoader >>>> %s: called with handlingClient: %@, handler: %@, requestInfo: <%p>, requestID %llu"
+ "<<<< AVAssetResourceLoader >>>> %s: data for current offset %lld of length %lld provided to %@"
+ "<<<< AVAssetResourceLoader >>>> %s: swallowing finishLoading for cancelled request %@"
+ "<<<< AVAssetResourceLoader >>>> %s: swallowing sendData with data of len %lu for cancelled request %@"
+ "<<<< AVAssetResourceLoader >>>> %s: swallowing sendResponseInfo for cancelled request %@"
+ "<<<< AVAssetTrackInspector >>>> %s: Created track inspector of class %@ "
+ "<<<< AVAssetTrackInspector >>>> %s: FigAssetTrackGetStatusOfValueForProperty for property <%@> returned %d and load error %d - %@"
+ "<<<< AVAssetTrackInspector >>>> %s: FigAssetTrackLoadValuesAsyncForProperties for properties %@ returned %d with loaded == %@ and batchID == %d"
+ "<<<< AVAssetTrackInspector >>>> %s: [%p] called"
+ "<<<< AVAssetTrackInspector >>>> %s: can't get FigAssetTrack; invalid trackID and negative trackIndex"
+ "<<<< AVAssetTrackInspector >>>> %s: can't get FigTrackReader; invalid trackID and negative trackIndex"
+ "<<<< AVAssetTrackInspector >>>> %s: dispatching completion handler [%p]"
+ "<<<< AVAssetTrackInspector >>>> %s: got notification <%@> for batchID %@"
+ "<<<< AVAssetTrackInspector >>>> %s: loading batch [%p] has count of %d on entry"
+ "<<<< AVAssetTrackInspector >>>> %s: loading batch [%p] has count of %d on exit with %@"
+ "<<<< AVAssetTrackInspector >>>> %s: storing completion handler [%p] for later invocation"
+ "<<<< AVAssetTrackInspector >>>> %s: storing loading batch [%p] with %@"
+ "<<<< AVAssetWriter >>>> %s: \"Transition to terminal status\" operation invoked"
+ "<<<< AVAssetWriter >>>> %s: -[NSFileManager removeItemAtURL:] failed: %s"
+ "<<<< AVAssetWriter >>>> %s: Calling FigAssetWriterFinish"
+ "<<<< AVAssetWriter >>>> %s: Can not get encryption scheme for '%c%c%c%c'"
+ "<<<< AVAssetWriter >>>> %s: Encryption schemes '%c%c%c%c' and '%c%c%c%c' do not match."
+ "<<<< AVAssetWriter >>>> %s: Error serializing encryption config data to JSON: %s"
+ "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinish failed: %d"
+ "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinishAsync failed: %d"
+ "<<<< AVAssetWriter >>>> %s: FigAssetWriterFinishAsync showed cancellation (self=%p)"
+ "<<<< AVAssetWriter >>>> %s: Invalid ContentKeySystem: %@"
+ "<<<< AVAssetWriter >>>> %s: Invalidating FigAssetWriter, to ensure that audio files are finalized properly"
+ "<<<< AVAssetWriter >>>> %s: No NSError on failure to prepare for writing, input %p"
+ "<<<< AVAssetWriter >>>> %s: No keyIdentifier"
+ "<<<< AVAssetWriter >>>> %s: Storage Space Preallocation Size %lld File System Free Size %lld"
+ "<<<< AVAssetWriter >>>> %s: Unexpected terminal status %d"
+ "<<<< AVAssetWriter >>>> %s: _figAssetWriter is nil"
+ "<<<< AVAssetWriter >>>> %s: attributes is nil with error:%s."
+ "<<<< AVAssetWriter >>>> %s: called (self=%p)"
+ "<<<< AVAssetWriter >>>> %s: called with payload %@"
+ "<<<< AVAssetWriter >>>> %s: called, self=%p"
+ "<<<< AVAssetWriter >>>> %s: called, success=%d, error=%@ (self=%p)"
+ "<<<< AVAssetWriter >>>> %s: calling FigAssetWriterFinishAsync (self=%p)"
+ "<<<< AVAssetWriter >>>> %s: calling completion handler"
+ "<<<< AVAssetWriter >>>> %s: freeSizeNum is nil."
+ "<<<< AVAssetWriter >>>> %s: freeSizeNum is not NSNumber."
+ "<<<< AVAssetWriter >>>> %s: invalid file extension in outputURL"
+ "<<<< AVAssetWriterInput >>>> %s: Calling FigAssetWriterEndPass"
+ "<<<< AVAssetWriterInput >>>> %s: Client exited request block"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaption: fail with error %@"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaption: return NO due to input already having transitioned to terminal status"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaptionGroup: fail with error %@"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendCaptionGroup: return NO due to input already having transitioned to terminal status"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendPixelBuffer: fail with error %@"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendPixelBuffer: return NO due to input already having transitioned to terminal status"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendSampleBuffer: fail with error %@"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendSampleBuffer: return NO due to input already having transitioned to terminal status"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendTaggedPixelBufferGroup: fail with error %@"
+ "<<<< AVAssetWriterInput >>>> %s: Client will see -appendTaggedPixelBufferGroup: return NO due to input already having transitioned to terminal status"
+ "<<<< AVAssetWriterInput >>>> %s: Dispatching request block because previous request block invocation returned before filling the buffer queue or marking input finished (delegate = %@)"
+ "<<<< AVAssetWriterInput >>>> %s: Dispatching request block one extra time, to make sure client sees the failure"
+ "<<<< AVAssetWriterInput >>>> %s: FigAssetWriterIsTrackQueueAboveHighWaterLevel returned %d (self=%p)"
+ "<<<< AVAssetWriterInput >>>> %s: Informing pass description responder to respond to initial pass description"
+ "<<<< AVAssetWriterInput >>>> %s: Invoking request block normally"
+ "<<<< AVAssetWriterInput >>>> %s: Not responding to initial pass description, per helper %@"
+ "<<<< AVAssetWriterInput >>>> %s: Received kFigAssetWriterNotification_PassFinished"
+ "<<<< AVAssetWriterInput >>>> %s: Transitioning to terminal status %d (self = %p)"
+ "<<<< AVAssetWriterInput >>>> %s: We thought we might want to invoke the request block, but we are not actually going to"
+ "<<<< AVAssetWriterInput >>>> %s: called (keyPath=%@, object=%@, change=%@, contect=%p)"
+ "<<<< AVAssetWriterInput >>>> %s: called (self = %p)"
+ "<<<< AVAssetWriterInput >>>> %s: called (self=%p)"
+ "<<<< AVAssetWriterInput >>>> %s: called (self=%p, queue=%p, block=%p)"
+ "<<<< AVAssetWriterInput >>>> %s: called (self=%p, trackID=%d)"
+ "<<<< AVAssetWriterInput >>>> %s: called, old=%@ new=%@"
+ "<<<< AVAssetWriterInput >>>> %s: called, self=%p"
+ "<<<< AVAssetWriterInput >>>> %s: did invoke per-pass block (self=%p)"
+ "<<<< AVAssetWriterInput >>>> %s: end pass operation succeeded, nextPassDescription=%@"
+ "<<<< AVAssetWriterInput >>>> %s: registering for kFigAssetWriterNotification_PassFinished on FigAssetWriter %p"
+ "<<<< AVAssetWriterInput >>>> %s: setting kFigFormatWriterTrackProperty_FormatDescriptionArray to %@"
+ "<<<< AVAssetWriterInput >>>> %s: unregistering from kFigAssetWriterNotification_PassFinished"
+ "<<<< AVAssetWriterInput >>>> %s: will invoke per-pass block (self=%p)"
+ "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Error creating metadata item: %@"
+ "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Error serializing JSON: %@"
+ "<<<< AVAssetWriterInputAnnotationAdaptor >>>> %s: Unrecognized asset writer status %d"
+ "<<<< AVAssetWriterInputMetadataAdaptor >>>> %s: Unrecognized asset writer status %d"
+ "<<<< AVCallbackContextRegistry >>>> %s: registering observer %p (token %p), new observer count %d (self=%p)"
+ "<<<< AVCallbackContextRegistry >>>> %s: unregistering callback context token %p, new observer count %d (self=%p)"
+ "<<<< AVCaptionRenderer >>>> %s: *** failed to start renderer ***"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> %s render started"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> *** FigCaptionCreate() returned %d"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request returned %d caption scenes"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> -captionSceneChangesInRange: request started"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> -renderInContext:atTime: called with bounds equal to CGRectNull"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session returned %d"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> finish setting session with FigCaptions"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> preparing to set session after converting AVCaptions to FigCaptions array"
+ "<<<< AVCaptionRenderer >>>> %s: <%p> start setting session with %ld FigCaptions"
+ "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCDSSessionSetTime returned error %d"
+ "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCDSSessionUpdateCGContext returned error %d"
+ "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientSetTime returned error %d"
+ "<<<< AVCaptionRenderer >>>> %s: @<%p> *** FigCaptionClientUpdateCGContext returned error %d"
+ "<<<< AVCaptionRenderer >>>> %s: FigCDSSessionStop() returned %d"
+ "<<<< AVCaptionRenderer >>>> %s: FigCaptionClientStop() returned %d"
+ "<<<< AVComposition >>>> %s: AVAsset with nil _absoluteURL and NULL _mutableComposition"
+ "<<<< AVComposition >>>> %s: [%p] called"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p asset: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p mediaType: %@ preferredTrackID: %d"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackAssetURL: %@ trackID: %d"
+ "<<<< AVComposition >>>> %s: [%p] called mutableComposition: %p track: %p trackID: %d"
+ "<<<< AVContentKeySession >>>>"
+ "<<<< AVContentKeySession >>>> %s: %@ failed to process content key request for identifier %@ and initialization data %@ due to %@"
+ "<<<< AVContentKeySession >>>> %s: %p Ignore produced contentKey (%@) because content key session is expired"
+ "<<<< AVContentKeySession >>>> %s: %p creating cryptor using sinfs"
+ "<<<< AVContentKeySession >>>> %s: %p failed to issue content key request because delegate's already gone"
+ "<<<< AVContentKeySession >>>> %s: %p failed to issue content key request due to an internal error"
+ "<<<< AVContentKeySession >>>> %s: %p initializing content key request with identifier %@ and initialization data %@"
+ "<<<< AVContentKeySession >>>> %s: Invalid key system used in AVContentKeySystem"
+ "<<<< AVContentKeySession >>>> %s: badly formatted key request init data (encoded sinf not UTF8)"
+ "<<<< AVContentKeySession >>>> %s: badly formatted key request init data (encoded sinf not base64)"
+ "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@"
+ "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptKeyIdentifier: %@, updatedPersistentKey: %@"
+ "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptorUUID: %@, cryptorRequestID: %llu"
+ "<<<< AVContentKeySession >>>> %s: called with callbackClient: %@, cryptorUUID: %@, cryptorRequestID: %llu, keyResponseError: %@"
+ "<<<< AVContentKeySession >>>> %s: called with handlingClient: %@, handler: %@, requestInfo: %@, requestID %llu"
+ "<<<< AVContentKeySession >>>> %s: failed to copy default secure stop manager due to error: %d"
+ "<<<< AVContentKeySession >>>> %s: protection status changed to: %ld"
+ "<<<< AVContentKeySession >>>> %s: setting authorizationToken failed due to err=%d"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: CIImage %@ (colorSpace %@) already has a CVPixelBuffer %@ (attachments %@)"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with CIImage %@"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with error %@"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: called with request %@"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: cancelling begin"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: cancelling done"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: rendered CIImage %@ (colorSpace %@) to CVPixelBuffer %@ (attachments %@)"
+ "<<<< AVCoreImageFilterCustomVideoCompositor >>>> %s: source CIImage %@ (colorSpace %@) from CVPixelBuffer %@ (attachments %@)"
+ "<<<< AVCustomCompositor >>>> %s: canConformColorOfSourceFrames %d"
+ "<<<< AVCustomCompositor >>>> %s: creating instance of \"%@\""
+ "<<<< AVCustomCompositor >>>> %s: initializing new render context (videoCompositionDidChange %d"
+ "<<<< AVCustomCompositor >>>> %s: render context no longer suitable, need to create a new one"
+ "<<<< AVCustomCompositor >>>> %s: src pixel buffer attributes %@"
+ "<<<< AVCustomCompositor >>>> %s: videoComposition %p"
+ "<<<< AVDataDelegateAsset >>>> %s: %p Available length = %lld, at offset %lld\n"
+ "<<<< AVDataDelegateAsset >>>> %s: AVAssetByteStreamCreateWithAsset: created a bytestream %p, of size = %lu\n"
+ "<<<< AVDataDelegateAsset >>>> %s: AVAssetByteStreamFinalize on %p\n"
+ "<<<< AVDataDelegateAsset >>>> %s: AVAssetByteStreamRead failed with error: %@\n"
+ "<<<< AVDataDelegateAsset >>>> %s: AVAssetByteStreamRead: offset = %lld, num = %lu\n"
+ "<<<< AVDataDelegateAsset >>>> %s: AVAssetByteStreamReadAndCreateBlockBuffer failed with error: %@\n"
+ "<<<< AVDelegateUtilities >>>> %s: Dispatching to queue %p"
+ "<<<< AVDelegateUtilities >>>> %s: Invoking delegate callback synchronously"
+ "<<<< AVDelegateUtilities >>>> %s: called (delegateStorage = %@, expectedDelegateQueue = %p, delegateCallbackBlock = %p)"
+ "<<<< AVDelegateUtilities >>>> %s: called (newDelegate=%@, newDelegateQueue=%p"
+ "<<<< AVDelegateUtilities >>>> %s: current delegate: %@, current delegate queue: %p"
+ "<<<< AVError >>>> %s: Could not load localized description for %@ %ld (%@)"
+ "<<<< AVError >>>> %s: Could not load localized failure reason for %@ %ld (%@)"
+ "<<<< AVError >>>> %s: Could not load localized recovery suggestion for %@ %ld (%@)"
+ "<<<< AVError >>>> %s: Could not load localized recovery suggestion or failure reason for %@ %ld (%@)"
+ "<<<< AVError >>>> %s: Invalid format string '%@', error %@, %@ %ld (%@)"
+ "<<<< AVExternalPlaybackMonitor >>>> %s: called"
+ "<<<< AVExternalPlaybackMonitor >>>> %s: called (self=%p)"
+ "<<<< AVExternalPlaybackMonitor >>>> %s: returning %@"
+ "<<<< AVExternalPlaybackMonitor >>>> %s: returning %d (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Assuming route change with ID %@ corresponds to the route change we just initiated"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (notificationName=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVErrorIncorrectPassword, since we do not know whether it was a PIN or password"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVErrorUnknown, since we have no more detailed error information"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using value %d for %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (routingContext=%@, configuratorBlock=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, deviceName=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, password=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peer=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peerID=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, rejectOtherConnections=%d)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because it does not match the expected ID %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because we have not yet executed the route change operation"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we already received a route change started notification"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we have not yet executed the route change operation"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring non-terminal route config update reason %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring route change ID %@ because it does not match the expected ID %@"
+ "<<<< AVFileSystemUtilities >>>> %s: Failed to remove temporary file at %@: %@"
+ "<<<< AVKVODispatcher >>>> %s: %p no longer observing %@ with observer %@, for key path %@, and context %p"
+ "<<<< AVKVODispatcher >>>> %s: %p observing %@ with observer %@, for key path %@, options %d, and context %p"
+ "<<<< AVKVODispatcher >>>> %s: Calling -didChange for %@.%@, in response to second-level property change (self=%p)"
+ "<<<< AVKVODispatcher >>>> %s: Calling -willChange for %@.%@, in response to second-level property change (self=%p)"
+ "<<<< AVKVODispatcher >>>> %s: Calling -willChange for %@.%@, in response to top-level property change (self=%p)"
+ "<<<< AVKVODispatcher >>>> %s: Registering for %@ (self = %@)"
+ "<<<< AVKVODispatcher >>>> %s: called (self=%p, keyPath=%@, object=%@, change=%@, context=%p)"
+ "<<<< AVKVODispatcher >>>> %s: cancelling second-level observation"
+ "<<<< AVLoggingIdentifier >>>> %s: Identifier string is %@"
+ "<<<< AVLoggingIdentifier >>>> %s: nil specifiedName"
+ "<<<< AVMediaFileSegmenter >>>> %s: %p"
+ "<<<< AVMediaFileSegmenter >>>> %s: %p , notification_name %@"
+ "<<<< AVMediaFileSegmenter >>>> %s: %p err=%d"
+ "<<<< AVMediaFileSegmenter >>>> %s: %p newStatus is %@"
+ "<<<< AVMediaFileSegmenter >>>> %s: unexpected notification: %@"
+ "<<<< AVMediaSelectionGroup >>>> %s: *** Could not canonicalize language: %@. ***"
+ "<<<< AVMediaSelectionGroup >>>> %s: <%p> called with property list %@"
+ "<<<< AVMediaSelectionGroup >>>> %s: <%p> resolved to option %@"
+ "<<<< AVMediaSelectionGroup >>>> %s: Invalid format string '%@', error %@"
+ "<<<< AVMetadataItem >>>>"
+ "<<<< AVMetadataItem >>>> %s: *** Could not canonicalize language: %@. ***"
+ "<<<< AVMetadataItem >>>> %s: <%p> completed asynchronous loading of lazily-loaded metadata value"
+ "<<<< AVMetadataItem >>>> %s: <%p> initiating asynchronous loading of lazily-loaded metadata value"
+ "<<<< AVMetadataItem >>>> %s: Identifier value %@ must be an instance of NSString"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_ConformingDataTypes must be an instance of NSArray"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DataLength must be an instance of NSNumber"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DataTypeNamespace must be an instance of NSString"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Date must be an instance of NSDate"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_DiscoveryTimestamp must be an instance of NSDate"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Duration must be an instance of CFDictionary"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_ExtendedLanguageTag must be an instance of NSString"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Key must conform to NSObject and NSCopying"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Keyspace must be an instance of NSString"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_LanguageCode must be an instance of NSString or of NSNumber"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Locale must be an instance of NSLocale"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_PreferredStorageLocation must be an instance of NSString"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Timestamp must be an instance of CFDictionary"
+ "<<<< AVMetadataItem >>>> %s: Value %@ for kFigMetadataItemProperty_Value must be CMBoxedMetadata or conform to NSObject and NSCopying"
+ "<<<< AVMetadataItem >>>> %s: Value %p does not conform to NSObject and/or NSCopying"
+ "<<<< AVMetadataItem >>>> %s: key not found %@"
+ "<<<< AVMetadataItem >>>> %s: keyspace not found %@"
+ "<<<< AVMovie >>>> %s: AVMovie %p, AVAssetInspectorLoader %p"
+ "<<<< AVMovie >>>> %s: AVMutableMovie %p failed initialization with error %@"
+ "<<<< AVMovie >>>> %s: AVMutableMovie %p, FigMutableMovie %p, FigAsset %p, FigFormatReader %p"
+ "<<<< AVMovie >>>> %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
+ "<<<< AVOperation >>>> %s: Client block cancelled with status %d (self=%p)"
+ "<<<< AVOperation >>>> %s: Got unrecognized status %d"
+ "<<<< AVOperation >>>> %s: Ignoring attempt to cancel before execution has begun.  The expectation is that the implementation will notice the cancelled state as part of normal execution"
+ "<<<< AVOperation >>>> %s: advancing status from %d to %d (self=%p)"
+ "<<<< AVOperation >>>> %s: already cancelled (self=%p)"
+ "<<<< AVOperation >>>> %s: called (self=%@)"
+ "<<<< AVOperation >>>> %s: called (self=%@, error=%@)"
+ "<<<< AVOperation >>>> %s: called (self=%p)"
+ "<<<< AVOperation >>>> %s: called (self=%p, name=%@)"
+ "<<<< AVOperation >>>> %s: ignoring attempt to move from terminal status %d to status %d"
+ "<<<< AVOperation >>>> %s: marking as cancelled due to cancellation of dependency (self=%@)"
+ "<<<< AVOperation >>>> %s: marking as failed due to previous failure in dependency (self=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying all audio contexts not supported!"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying system remote display context not supported!"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for endpoint %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for route descriptor %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopyPredictedSelectedRouteDescriptor yielded %@ (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded %@NULL endpoint (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded endpoint %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptor yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptors yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoutes yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Listener should be the shared endpoint agent queue"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: No comm channel found for ID %@, synthesizing one for the delegate (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Output context exists with associated remote output device"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Storing new outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Trying comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using pre-existing outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevice=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevices=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, agent=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, commChannelUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, contextUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, data=%@, commChannelUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevice=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevices=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeUpdateID=%@, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContext=%@, routingContextCreator=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContextID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_AssociatedAudioDevice = %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_ContextUUID = %@ (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: operation finished"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: returning %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: using clientPID %d"
+ "<<<< AVOutputContext >>>> %s: Defaulting to AVOutputContext impl %@"
+ "<<<< AVOutputContext >>>> %s: Received notification %@"
+ "<<<< AVOutputContext >>>> %s: called (self=%p)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, channel=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, data=%@, channel=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, replacementImpl=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, status=%d)"
+ "<<<< AVOutputContext >>>> %s: contextID = %@"
+ "<<<< AVOutputContext >>>> %s: outputDevice = %@"
+ "<<<< AVOutputContext >>>> %s: outputDevices = %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerGetMuteOfEndpointWithID (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' has value: %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' not supported"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: RouteUID %@ or RouteName %@ is nil, can't construct description."
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized head-tracked spatial audio mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  Only a subset of possible device types can be communicated by FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover connected paired devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover detailed device subtype for most devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get DataOverACL information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get isInEar information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, figEndpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p client %@ reason %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>>"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Listener should be the output device route discoverer queue"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Using value %d for %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, routeDescriptor=%@)"
+ "<<<< AVOutputDevice >>>> %s: No Output Context to add to!"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, request=%@, requestImpl=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, status=%d, error=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, uniqueID=%@, routeDescriptor=%@, pinMode=%d, reason=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Received notification %@"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p, delegate=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: self=%p, impl=%@, replacementImpl=%@"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: Unrecognized event type: %@"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No AVOutputDevice to connect to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No System Remote Pool to add to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No comm channel found for ID %@ for device %@, synthesizing one for the delegate."
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Removing comm channel UUID %@ for device with ID %@"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: initialized (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Unsupported device feature combination %d"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%@, class=%@, deviceFeatures=%u)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AvailableRoutes = %@ (err=%d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Available output devices: %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Cannot set targetAudioSession on macOS"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Posting %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (targetAudioSession=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: otherDevices = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: recentlyUsedDevices = %@"
+ "<<<< AVOutputDeviceGroup >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceGroup >>>> %s: outputDevices = %@"
+ "<<<< AVOutputDeviceHID >>>> %s: called (uuid=%@, screenUUID=%@ endpoint=%p)"
+ "<<<< AVOutputDeviceIcon >>>> %s: called (dict=%@)"
+ "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (dict=%@)"
+ "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (viewArea=%@, transitionControl=%{BOOL}u, supportsFocusTransfer=%{BOOL}u, statusBarEdge=%@, safeArea=%@)"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ %{public}@ updating transport control state cache for item identifier %@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ Converted to media time: original time %f, adjusted media time %f, host time adjustment (%f-%f)"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new control state."
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle new participant state."
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator is NULL when trying to handle replacement participant state."
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ FigPlaybackCoordinator updating %d control states."
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ Posting AVPlaybackCoordinatorItemIdentifierForCoordinatedPlaybackDidChangeNotification in response to delegate change"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ Setting integrated timeline"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ beginning suspension with reason %@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ current pending seek id %d, seek time %f"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p proposing new time %f"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline only contains primary segment. Bypassing integrated seek to %f"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline seek at %f current time at %f, applied : %d"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ interstitial is active : %d"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ playback coordinator is suspended. Skipping seek to %f"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ resetting group timeline expectation"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator with UUID %@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ setting coordinationMediumDelegate:%p on playback coordinator, but NULL figPlaybackCoordinator"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ setting waiting policies %@ on playback coordinator"
+ "<<<< AVPlaybackCoordinator >>>> %s: <AVPlaybackCoordinator: %@> failed to dispatch work async onto player queue with err: %d, synchronizing locally"
+ "<<<< AVPlaybackCoordinator >>>> %s: Could not create FigTimelineCoordinatorSuspensionRef"
+ "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator gave a participantID which is not present in otherParticipants"
+ "<<<< AVPlaybackCoordinator >>>> %s: States aren't distinguishable. Assuming state from the outside is better."
+ "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for DidIssueCommandToFigPlayer notification, with payload = %@)"
+ "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
+ "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
+ "<<<< AVPlayer >>>> %s: %@ (self = %p) (layer = %p)"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) _detachVideoLayersFromFigPlayer _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) attach video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) not updating video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) and its closedCaptionLayer(%p)"
+ "<<<< AVPlayer >>>> %s: %@ AVPlayerLayer(%p) is adding videoLayer(%p), closedCaptionLayer(%p), and subtitleLayer(%p) sublayers"
+ "<<<< AVPlayer >>>> %s: %@ Did update status to %d (self=%p)"
+ "<<<< AVPlayer >>>> %s: %@ Dispatching FigPlayer copy property block (self=%p) to a background queue if necessary"
+ "<<<< AVPlayer >>>> %s: %@ NULL FigPlayerInterstitialCoordinator"
+ "<<<< AVPlayer >>>> %s: %@ New current item: %@ %@ (self = %@)"
+ "<<<< AVPlayer >>>> %s: %@ Trying to set picker id : %@"
+ "<<<< AVPlayer >>>> %s: %@ Will update status (self=%p)"
+ "<<<< AVPlayer >>>> %s: %@ _setUsesLegacyAutomaticWaitingBehavior: %s"
+ "<<<< AVPlayer >>>> %s: %@ attached video layer array with %lu layers on FigPlayer"
+ "<<<< AVPlayer >>>> %s: %@ called (self = %@)"
+ "<<<< AVPlayer >>>> %s: %@ called (self = %@, inNotificationName = %@)"
+ "<<<< AVPlayer >>>> %s: %@ called (self = %@, inNotificationName = %@, inNotificationPayload = %@)"
+ "<<<< AVPlayer >>>> %s: %@ called (self = %p, new current item = %@)"
+ "<<<< AVPlayer >>>> %s: %@ called (self = <%p>) Warning: Value ignored."
+ "<<<< AVPlayer >>>> %s: %@ called (self = <%p>, time observer = <%p>)"
+ "<<<< AVPlayer >>>> %s: %@ called (self=%p)"
+ "<<<< AVPlayer >>>> %s: %@ called. Rate changed from [%f] -> [%f], changed because %s\n%@"
+ "<<<< AVPlayer >>>> %s: %@ called. oldReason %@ newReason %@ for timeControlStatus %d to %d"
+ "<<<< AVPlayer >>>> %s: %@ called. set to [%f]"
+ "<<<< AVPlayer >>>> %s: %@ cannot copy displayed pixel buffer, figPlayer is NULL"
+ "<<<< AVPlayer >>>> %s: %@ current interstitial event %@"
+ "<<<< AVPlayer >>>> %s: %@ detached video layer array from FigPlayer"
+ "<<<< AVPlayer >>>> %s: %@ dispatched (self = %@, inNotificationName = %@)"
+ "<<<< AVPlayer >>>> %s: %@ dispatching (self = %p)"
+ "<<<< AVPlayer >>>> %s: %@ failed to copy currently displayed pixel buffer although no error"
+ "<<<< AVPlayer >>>> %s: %@ inferred time control status: %d (waiting reason: %@)"
+ "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_CurrentItemDidChange (self = %@, FigPlaybackItem = %p"
+ "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_CurrentItemDidChange due to AddTo/RemoveFrom-PlayQueue. No need to advance current item to match Fig"
+ "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_MutedDidChange (self = %@ value [%d])"
+ "<<<< AVPlayer >>>> %s: %@ kFigPlayerNotification_VolumeDidChange (self = %@, value [%f])"
+ "<<<< AVPlayer >>>> %s: %@ kFigPlayerProperty_PlaybackState is %@"
+ "<<<< AVPlayer >>>> %s: %@ maximumLayerDisplaySize = %@ (self = %p)"
+ "<<<< AVPlayer >>>> %s: %@ not updating video layers, despite adding layer %p (self=%@)"
+ "<<<< AVPlayer >>>> %s: %@ player <%p> failed to create fig sub item (error: %@)"
+ "<<<< AVPlayer >>>> %s: %@ received %@ (payload: %@)"
+ "<<<< AVPlayer >>>> %s: %@ received updated %@. Rate changed from [%f] -> [%f], changed because %s\n%@"
+ "<<<< AVPlayer >>>> %s: %@ removed %@ %@, now have %@"
+ "<<<< AVPlayer >>>> %s: %@ setting from %d to %d"
+ "<<<< AVPlayer >>>> %s: %@ setting rate to %f"
+ "<<<< AVPlayer >>>> %s: %@ setting to %d"
+ "<<<< AVPlayer >>>> %s: %@ setting up FigPlayer <%p>"
+ "<<<< AVPlayer >>>> %s: %@ updating video layers due to adding layer %p (self=%@)"
+ "<<<< AVPlayer >>>> %s: %s"
+ "<<<< AVPlayer >>>> %s: AVPlayer %@ setShouldWaitForVideoTarget to %d"
+ "<<<< AVPlayer >>>> %s: Coordinator player disabled"
+ "<<<< AVPlayer >>>> %s: Creating instance of %s"
+ "<<<< AVPlayer >>>> %s: Directly set kFigPlayerProperty_ShouldWaitForVideoTarget on FigPlayer %@"
+ "<<<< AVPlayer >>>> %s: Dispatching FigPlayer configuration block (self=%p) to state dispatch queue"
+ "<<<< AVPlayer >>>> %s: Error inserting item: %@"
+ "<<<< AVPlayer >>>> %s: Error replacing current item: %@"
+ "<<<< AVPlayer >>>> %s: Failed adding playback item of %@ to play queue immediately (self = %@), will remove item"
+ "<<<< AVPlayer >>>> %s: Handling removal of item %@ (self = %@)"
+ "<<<< AVPlayer >>>> %s: No figPlayer found, cannot set picker id"
+ "<<<< AVPlayer >>>> %s: Player role %@ set synchronously before we had a fig player."
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerAudiovisualBackgroundPlaybackPolicyDidChangeNotification for policy change"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerAvailableHDRModesDidChangeNotification"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerBackgroundPIPAuthorizationTokenDidChangeNotification for token change"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerCurrentItemDidChangeNotification with reason %@"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerEligibleForHDRPlaybackDidChangeNotification"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerInterstitialPlayerDidChangeNotification"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerPlaybackWasInterruptedNotification"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerRateDidChangeNotification for status change"
+ "<<<< AVPlayer >>>> %s: Posting AVPlayerRateDidChangeNotification with payload %@"
+ "<<<< AVPlayer >>>> %s: Set ShouldWaitForVideoTarget as creation option or right after creation of player %@"
+ "<<<< AVPlayer >>>> %s: Surrogate player enabled = %d"
+ "<<<< AVPlayer >>>> %s: The FigPlaybackItem that posted ItemBecameCurrent has already been removed from the queue; fall back to identifying the current item using FigPlayerCopyPlayQueueItem"
+ "<<<< AVPlayer >>>> %s: Unrecognized player role %@"
+ "<<<< AVPlayer >>>> %s: availableHDRModes returning %d"
+ "<<<< AVPlayer >>>> %s: called (asset=%p)"
+ "<<<< AVPlayer >>>> %s: called on <%@>. Setting attributes on decoder to:\n\t<%@>"
+ "<<<< AVPlayer >>>> %s: closedCaptionLayers array snapshot:%@"
+ "<<<< AVPlayer >>>> %s: connect fig playback coordinator"
+ "<<<< AVPlayer >>>> %s: current event %@ %f"
+ "<<<< AVPlayer >>>> %s: dispatching call to -_applyPlayQueueChangesToFigPlayerWithCompletionHandler: (self=%p)"
+ "<<<< AVPlayer >>>> %s: fig playback coordinator already connected clientRequested"
+ "<<<< AVPlayer >>>> %s: figplayer creation failed [%d]"
+ "<<<< AVPlayer >>>> %s: interstitial is active %d"
+ "<<<< AVPlayer >>>> %s: now have %@"
+ "<<<< AVPlayer >>>> %s: removed current item, now have %@"
+ "<<<< AVPlayer >>>> %s: replaced local interstitialEventCoordinator %p with remote %p"
+ "<<<< AVPlayer >>>> %s: sawFileType = %d, sawStreamingType = %d"
+ "<<<< AVPlayer >>>> %s: seekToDate called without any attached item"
+ "<<<< AVPlayer >>>> %s: seekToTime called without any attached item"
+ "<<<< AVPlayer >>>> %s: setExpectedAssetTypes %@"
+ "<<<< AVPlayer >>>> %s: setting to %@"
+ "<<<< AVPlayer >>>> %s: underlying FigPlayer did neither implement SetRateWithOptions nor SetRateWithFade. Fall back to SetRate"
+ "<<<< AVPlayer >>>> %s: underlying FigPlayer did not implement SetRateWithOptions. Fall back to SetRateWithFade"
+ "<<<< AVPlayer >>>> %s: videoLayers array snapshot:%@"
+ "<<<< AVPlayerCaptionLayer >>>> %s: <%p> %@ closed caption layer"
+ "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Did cancel all observation of old player"
+ "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
+ "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
+ "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Observing isDisplayingClosedCaptions on player %p"
+ "<<<< AVPlayerCaptionLayer >>>> %s: Called (self=%p)"
+ "<<<< AVPlayerCaptionLayer >>>> %s: Called (self=%p, bounds=%@)"
+ "<<<< AVPlayerCaptionLayer >>>> %s: Setting interstitialLayer %p visibility to %d and primary (subtitle/closedcaption) layer %p/%p visibility to %d"
+ "<<<< AVPlayerCaptionLayer >>>> %s: Setting legibleContentInsets received from client. left = %f, right = %f, top = %f, bottom = %f"
+ "<<<< AVPlayerCaptionLayer >>>> %s: Updated CC bounds with cached legibleContentInsets. left = %f, right = %f, top = %f, bottom = %f"
+ "<<<< AVPlayerCaptionLayer >>>> %s: called (keyPath=%@, object=%@, change=%@, context=%p"
+ "<<<< AVPlayerCaptionLayer >>>> %s: called (keyPath=%@, value=%@"
+ "<<<< AVPlayerCaptionLayer >>>> %s: creating interstitialLayer %p for primary playerCaptionLayer %p"
+ "<<<< AVPlayerCaptionLayer >>>> %s: old player=%p, new player=%p"
+ "<<<< AVPlayerInterstitialEventMonitor >>>> %s:  Unrecognized notification: %@"
+ "<<<< AVPlayerItem >>>> %s:  %@: set video composition properties: %@"
+ "<<<< AVPlayerItem >>>> %s: %@ <%p> returning %@"
+ "<<<< AVPlayerItem >>>> %s: %@ <%p> with asset <%p> called for media selection group %@"
+ "<<<< AVPlayerItem >>>> %s: %@ <%p> with asset <%p> called for media selection option %@ in group %@"
+ "<<<< AVPlayerItem >>>> %s: %@ AVPlayerItem <%p> created with asset at URL [%@], automatically loaded asset keys %@"
+ "<<<< AVPlayerItem >>>> %s: %@ Adding playback item of %p to play queue immediately (player = %@)"
+ "<<<< AVPlayerItem >>>> %s: %@ CPEProtector already ready"
+ "<<<< AVPlayerItem >>>> %s: %@ Chosen tracks changed"
+ "<<<< AVPlayerItem >>>> %s: %@ CurrentSelectedMediaArray not in payload or nil."
+ "<<<< AVPlayerItem >>>> %s: %@ Display non-forced subtitles changed"
+ "<<<< AVPlayerItem >>>> %s: %@ ExternalProtectionRequiredForPlayback changed"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> became the FigPlayer's current item"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> reached timeToPauseBuffering"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> reached timeToPausePlayback"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> stopped being the FigPlayer's current item"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItem <%p> was removed from the FigPlayer's item queue"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSeekToDate() failed for initial date"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSeekToDateWithID() failed"
+ "<<<< AVPlayerItem >>>> %s: %@ FigPlaybackItemSetProperty() failed with %d for initial estimated date"
+ "<<<< AVPlayerItem >>>> %s: %@ Ignore nil/empty audioProcessingEffects"
+ "<<<< AVPlayerItem >>>> %s: %@ Item <%p> Seek to time %1.3f with tolerance <%1.3f, %1.3f>"
+ "<<<< AVPlayerItem >>>> %s: %@ Item <%p> avoided synchronous FigAsset/FigAssetTrack property fetch while formulating currentMediaSelection"
+ "<<<< AVPlayerItem >>>> %s: %@ Item <%p> is fetching TrackIDArray"
+ "<<<< AVPlayerItem >>>> %s: %@ Item <%p> is fetching its dimensions"
+ "<<<< AVPlayerItem >>>> %s: %@ NewRecommendedTimeOffsetFromLive: %@"
+ "<<<< AVPlayerItem >>>> %s: %@ Requesting automatic loading of FigAsset properties %@"
+ "<<<< AVPlayerItem >>>> %s: %@ Requesting automatic loading of FigAssetTrack properties %@"
+ "<<<< AVPlayerItem >>>> %s: %@ Using seek ID %d"
+ "<<<< AVPlayerItem >>>> %s: %@ alternate stream changed"
+ "<<<< AVPlayerItem >>>> %s: %@ basics already ready"
+ "<<<< AVPlayerItem >>>> %s: %@ called (self = %p)"
+ "<<<< AVPlayerItem >>>> %s: %@ called (self = %p) attaching player %p weak ref %p"
+ "<<<< AVPlayerItem >>>> %s: %@ called (self = %p) to invoke %d handlers"
+ "<<<< AVPlayerItem >>>> %s: %@ called (self=%p, option=%@, group=%@)"
+ "<<<< AVPlayerItem >>>> %s: %@ dimensions changed to %@"
+ "<<<< AVPlayerItem >>>> %s: %@ initialSamples already ready"
+ "<<<< AVPlayerItem >>>> %s: %@ item (self = %p) already attached to a different player, new weak ref %p old weak ref %p"
+ "<<<< AVPlayerItem >>>> %s: %@ item (self = %p) already attached to same player, new weak ref %p old weak ref %p"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> AllowedSpatialization changed"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> SpatialAudioRenderingChange: %@"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> SpatialAudioRenderingChange: default, no payload"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> failed to become ready for %@ (error: %@)"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> failed to create fig sub item (error: %@)"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasEnabledAudio changed"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasEnabledVideo changed"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> hasVideo changed to YES"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> ready for inspection of %@"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> ready for playback"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> set can and step flags"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> status changing to AVPlayerItemStatusFailed with error %@"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> status changing to AVPlayerItemStatusReadyToPlay"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> updateStatusToReadyToPlay:%d"
+ "<<<< AVPlayerItem >>>> %s: %@ item <%p> updateStatusToReadyToPlay:%d complete"
+ "<<<< AVPlayerItem >>>> %s: %@ item selected media options changed"
+ "<<<< AVPlayerItem >>>> %s: %@ loaded ranges changed"
+ "<<<< AVPlayerItem >>>> %s: %@ playback buffer Full: NO"
+ "<<<< AVPlayerItem >>>> %s: %@ playback buffer empty: NO"
+ "<<<< AVPlayerItem >>>> %s: %@ playback stalled"
+ "<<<< AVPlayerItem >>>> %s: %@ reset cinematicAudioEffectParameters"
+ "<<<< AVPlayerItem >>>> %s: %@ reset sweepFilterConfiguration"
+ "<<<< AVPlayerItem >>>> %s: %@ seekable ranges changed"
+ "<<<< AVPlayerItem >>>> %s: %@ setting video composition instructions to %@"
+ "<<<< AVPlayerItem >>>> %s: %@ stream buffer empty: YES"
+ "<<<< AVPlayerItem >>>> %s: %@ stream buffer full: YES"
+ "<<<< AVPlayerItem >>>> %s: %@ stream likely to keep up: NO"
+ "<<<< AVPlayerItem >>>> %s: %@ stream likely to keep up: YES"
+ "<<<< AVPlayerItem >>>> %s: Calling FigPlayerAddToPlayQueue (item = %@ %@, previous item = %@ %@, FigPlaybackItem = %p)"
+ "<<<< AVPlayerItem >>>> %s: Copying completion handler for later invocation in response to readiness notifications"
+ "<<<< AVPlayerItem >>>> %s: Either everything necessary is already ready, or making it all ready has failed"
+ "<<<< AVPlayerItem >>>> %s: Failed to allocate videoCompositionProperties"
+ "<<<< AVPlayerItem >>>> %s: Failed to set kFigPlaybackItemProperty_MetadataOutputsDictionary"
+ "<<<< AVPlayerItem >>>> %s: Invoking completion handler for cancelled seek %d"
+ "<<<< AVPlayerItem >>>> %s: Invoking seek completion handler for seek id %d"
+ "<<<< AVPlayerItem >>>> %s: Neither applied nor cached media option. Selection will be discarded."
+ "<<<< AVPlayerItem >>>> %s: Not calling FigPlayerAddToPlayQueue because item's status is the failure status (item = %@ %@, previous item = %@ %@, FigPlaybackItem = %p)"
+ "<<<< AVPlayerItem >>>> %s: Posting %@ for seekID %d"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemDidPlayToEndTimeNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemFailedToPlayToEndTimeNotification with error %@"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemMediaSelectionDidChangeNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemNewAccessLogEntryNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemNewErrorLogEntryNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemPlaybackStalledNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimeJumpedNotification"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimeJumpedNotification for seek with originator"
+ "<<<< AVPlayerItem >>>> %s: Posting AVPlayerItemTimebaseChangedNotification"
+ "<<<< AVPlayerItem >>>> %s: Unknown AVAudioMixEffectParameters type."
+ "<<<< AVPlayerItem >>>> %s: Video Enhancement mode is not valid"
+ "<<<< AVPlayerItem >>>> %s: We have neither a FigAsset, URL, nor FigFormatReader, so cannot create a FigPlaybackItem"
+ "<<<< AVPlayerItem >>>> %s: can't create looping timebase! item will not loop."
+ "<<<< AVPlayerItem >>>> %s: self %@: setting interstitial time ranges to %@"
+ "<<<< AVPlayerItemLegibleOutput >>>> %s: Invoking legible delegate %p with %d attributed string(s) and %d native sample(s) at time %f:%@"
+ "<<<< AVPlayerItemLegibleOutput >>>> %s: Notifying delegate of a flush"
+ "<<<< AVPlayerItemLegibleOutput >>>> %s: called"
+ "<<<< AVPlayerItemMetadataOutput >>>> %s: Invoking metadata delegate %p with %@ dictionary from %@ item track"
+ "<<<< AVPlayerItemMetadataOutput >>>> %s: Notifying delegate of a flush"
+ "<<<< AVPlayerItemMetadataOutput >>>> %s: metadata output flushed"
+ "<<<< AVPlayerItemOutput >>>> %s:  Error: requestNotificationOfMediaDataChangeAsSoonAsPossible was valid when requesting requestNotificationOfMediaDataChangeWithAdvanceInterval. requestNotificationOfMediaDataChangeAsSoonAsPossible has been deactivated"
+ "<<<< AVPlayerItemOutput >>>> %s:  Error: requestNotificationOfMediaDataChangeWithAdvanceInterval was valid when requesting requestNotificationOfMediaDataChangeAsSoonAsPossible. requestNotificationOfMediaDataChangeWithAdvanceInterval is deactivated"
+ "<<<< AVPlayerItemOutput >>>> %s: Dispatching -outputSequenceWasFlushed:"
+ "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextCopyImageForTime did not provide a imageOriginalTimeOut value. Bailing."
+ "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextCreate failed: %d"
+ "<<<< AVPlayerItemOutput >>>> %s: FigVisualContextSetImageAvailableSequentialCallback failed: %d"
+ "<<<< AVPlayerItemOutput >>>> %s: Sending -outputMediaDataWillChange: to delegate"
+ "<<<< AVPlayerItemOutput >>>> %s: Sending -outputSequenceWasFlushed: to delegate"
+ "<<<< AVPlayerItemOutput >>>> %s: Unable to convert host time stamp to item time. Client sees kCMTimeInvalid."
+ "<<<< AVPlayerItemOutput >>>> %s: Unable to copy next image from visual context. Bailing."
+ "<<<< AVPlayerItemOutput >>>> %s: scheduled wakeup for now"
+ "<<<< AVPlayerItemOutput >>>> %s: scheduled wakeup in %.3f s"
+ "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: Invoking rendered legible delegate %p with %d caption image(s) at time %f"
+ "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: Notifying delegate of a flush"
+ "<<<< AVPlayerItemRenderedLegibleOutput >>>> %s: called"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p received %@, extractionID=%d"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p: wrong trackID %d (right trackID is %d)"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputMediaDataAvailable:trackID:"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputSequenceWasFlushed:trackID:"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: FigPlaybackItemExtractAndRetainNextSampleBuffer returned %d, sampleBuffer=%p, self=%p"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: No delegate"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputMediaDataAvailable:trackID: to delegate"
+ "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputSequenceWasFlushed:trackID: to delegate"
+ "<<<< AVPlayerItemTrack >>>> %s: attached output %@ with extractionID %d"
+ "<<<< AVPlayerItemTrack >>>> %s: removed output %@"
+ "<<<< AVPlayerItemTrack >>>> %s: stateDispatchQueue is NULL"
+ "<<<< AVPlayerLayer >>>> %s:  <%p> Hiding video layer since the presentation size for player %p is 0x0"
+ "<<<< AVPlayerLayer >>>> %s: %@ AVPlayerLayer's net flip status does match CoreAnimation default"
+ "<<<< AVPlayerLayer >>>> %s: %@ AVPlayerLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
+ "<<<< AVPlayerLayer >>>> %s: %@ already in PIP mode but will use %p instead of %p"
+ "<<<< AVPlayerLayer >>>> %s: %@ became PIP'ed"
+ "<<<< AVPlayerLayer >>>> %s: %@ commence player <%p> observation"
+ "<<<< AVPlayerLayer >>>> %s: %@ entering PIP mode using %p"
+ "<<<< AVPlayerLayer >>>> %s: %@ frame is { %f, %f }"
+ "<<<< AVPlayerLayer >>>> %s: %@ leaving PIP mode"
+ "<<<< AVPlayerLayer >>>> %s: %@ left PIP mode"
+ "<<<< AVPlayerLayer >>>> %s: %@ resign player <%p> observation over currentItem.presentationSize"
+ "<<<< AVPlayerLayer >>>> %s: %@ setting player to <%p> forPIP:%d"
+ "<<<< AVPlayerLayer >>>> %s: %@ setting self on player <%p>"
+ "<<<< AVPlayerLayer >>>> %s: %@ showing interstitial layer [%@], call interstitialLayer copyDisplayedPixelBuffer"
+ "<<<< AVPlayerLayer >>>> %s: %@ visibility became NO"
+ "<<<< AVPlayerLayer >>>> %s: %@ visibility became YES"
+ "<<<< AVPlayerLayer >>>> %s: %p notifying player %p about new display size %@"
+ "<<<< AVPlayerLayer >>>> %s: <%p> %@ closed caption layer"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Did cancel all observation of old player"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Hiding video layer since the presentation size is 0x0"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Regardless of the state of PIP the layer is in, removeFromSuperLayer is always allowed"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Restoring client layer %@ with indexPath %@"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Setting closed caption layer bounds to %@"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Unhiding video layer since the presentation size for player %p is { %f, %f }"
+ "<<<< AVPlayerLayer >>>> %s: <%p> Using box filter downscale"
+ "<<<< AVPlayerLayer >>>> %s: <%p> called"
+ "<<<< AVPlayerLayer >>>> %s: <%p> finished"
+ "<<<< AVPlayerLayer >>>> %s: <%p> setting new sublayers: videoLayer(%p), closedCaptionLayer(%p), subtitleLayer(%p), interstitialLayers = %@"
+ "<<<< AVPlayerLayer >>>> %s: <%p> size needs no update using cached value { %f, %f }"
+ "<<<< AVPlayerLayer >>>> %s: <%p> size needs update from { %f, %f } to { %f, %f } (force=%s)"
+ "<<<< AVPlayerLayer >>>> %s: Called (self=%p)"
+ "<<<< AVPlayerLayer >>>> %s: Called (self=%p, bounds=%@)"
+ "<<<< AVPlayerLayer >>>> %s: Cannot add sublayer while PIP is active"
+ "<<<< AVPlayerLayer >>>> %s: Cannot insert sublayer while PIP is active"
+ "<<<< AVPlayerLayer >>>> %s: Cannot replace sublayer while PIP is active"
+ "<<<< AVPlayerLayer >>>> %s: Cannot set sublayers while PIP is active"
+ "<<<< AVPlayerLayer >>>> %s: Display Size is %f x %f scale is %f"
+ "<<<< AVPlayerLayer >>>> %s: Error in traversing layer tree"
+ "<<<< AVPlayerLayer >>>> %s: Scheduling interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d (delayed to %f, now %f)"
+ "<<<< AVPlayerLayer >>>> %s: Setting interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d"
+ "<<<< AVPlayerLayer >>>> %s: Setting legibleContentInsets received from client. left = %f, right = %f, top = %f, bottom = %f"
+ "<<<< AVPlayerLayer >>>> %s: Setting readyForDisplay to NO due to detaching from player %@ (self=%p)"
+ "<<<< AVPlayerLayer >>>> %s: Storing client layer %@ with indexPath %@"
+ "<<<< AVPlayerLayer >>>> %s: Updated CC bounds with cached legibleContentInsets. left = %f, right = %f, top = %f, bottom = %f"
+ "<<<< AVPlayerLayer >>>> %s: called (keyPath=%@, object=%@, change=%@, context=%p"
+ "<<<< AVPlayerLayer >>>> %s: called (self=%p)"
+ "<<<< AVPlayerLayer >>>> %s: called (self=%p, item=%p, readyForDisplay=%d)"
+ "<<<< AVPlayerLayer >>>> %s: creating interstitialLayer %p for primary playerLayer %p"
+ "<<<< AVPlayerLayer >>>> %s: displaySize is %f x %f rootSize is %f x %f percentage %f"
+ "<<<< AVPlayerLayer >>>> %s: player layer %p <-> player layer %p"
+ "<<<< AVPlayerLayer >>>> %s: requesting the pixelBufferAttributes property on a presentation layer is invalid"
+ "<<<< AVPlayerLayer >>>> %s: scalingFactor(%d) is not between 2 and 8"
+ "<<<< AVPlayerLayer >>>> %s: setting forScrubbingOnly = %d"
+ "<<<< AVPlayerLayer >>>> %s: sync to player (self=%p, player=%p)"
+ "<<<< AVPlayerLooper >>>> %s: AVPlayerLooperInternal allocation failed"
+ "<<<< AVPlayerLooper >>>> %s: Already in Failed state so not updating error"
+ "<<<< AVPlayerLooper >>>> %s: Can't loop with 0 item copies"
+ "<<<< AVPlayerLooper >>>> %s: Change to Failed status with error %@"
+ "<<<< AVPlayerLooper >>>> %s: Changing player's action-at-end to Advance"
+ "<<<< AVPlayerLooper >>>> %s: Couldn't load asset duration. Change status to Failed"
+ "<<<< AVPlayerLooper >>>> %s: Couldn't set up for looping. Change status to Failed"
+ "<<<< AVPlayerLooper >>>> %s: Create with player %p and item %p"
+ "<<<< AVPlayerLooper >>>> %s: End KVO setup"
+ "<<<< AVPlayerLooper >>>> %s: Failed to allocate item copy"
+ "<<<< AVPlayerLooper >>>> %s: In Failed or cancelled state so cannot advance to Ready"
+ "<<<< AVPlayerLooper >>>> %s: Loop duration is less than minimum so capped number of copies to %d"
+ "<<<< AVPlayerLooper >>>> %s: Loop item duration is %1.3f"
+ "<<<< AVPlayerLooper >>>> %s: Loop time range end is past item duration"
+ "<<<< AVPlayerLooper >>>> %s: Loop time range starts past item duration"
+ "<<<< AVPlayerLooper >>>> %s: Looping item duration is 0. Can't loop"
+ "<<<< AVPlayerLooper >>>> %s: Looping item(%p) failed to become ready so disabling looping"
+ "<<<< AVPlayerLooper >>>> %s: Looping turned off and not waiting for looping copy to finish so ignoring"
+ "<<<< AVPlayerLooper >>>> %s: Need %d copies for looping"
+ "<<<< AVPlayerLooper >>>> %s: Need to create %d item copies"
+ "<<<< AVPlayerLooper >>>> %s: Pausing player (current rate: %1.1f) during set up"
+ "<<<< AVPlayerLooper >>>> %s: Restoring player rate(%1.1f)"
+ "<<<< AVPlayerLooper >>>> %s: The minimum number of copies (%d) is sufficient for looping"
+ "<<<< AVPlayerLooper >>>> %s: Time range duration is %1.3f"
+ "<<<< AVPlayerLooper >>>> %s: Unknown context(%p). Ignoring"
+ "<<<< AVPlayerLooper >>>> %s: Using loop duration of %1.3f"
+ "<<<< AVPlayerLooper >>>> %s: [%p]Disabling looping since item(%p) failed to play to end with error %@"
+ "<<<< AVPlayerLooper >>>> %s: ivarAccessQueue allocation failed"
+ "<<<< AVPlayerLooper >>>> %s: loopingItemCopies allocation failed"
+ "<<<< AVPlayerLooper >>>> %s: observeValueForKeyPath:ofObject:change:context: called for %@"
+ "<<<< AVPlayerOutput >>>>"
+ "<<<< AVPlayerOutput >>>> %s: (%p) (%@)"
+ "<<<< AVPlayerOutput >>>> %s: (%p) Buffer group for hostTime %.3f is equal to the last vended buffer group, therefore there is not a new buffer group for this time"
+ "<<<< AVPlayerOutput >>>> %s: (%p) Cannot sample while fvr is NULL, ensure you have attached this output to a valid AVPlayer"
+ "<<<< AVPlayerOutput >>>> %s: (%p) Failed to get buffer group for host time %.3f with error %d"
+ "<<<< AVPlayerOutput >>>> %s: (%p) No buffer group was available for hostTime %.3f"
+ "<<<< AVPlayerOutput >>>> %s: (%p) Received configuration with itemIdentifier %@ and could not find source item"
+ "<<<< AVPlayerOutput >>>> %s: AVPlayerVideoOutput<%p> cannot be attached to more than one player at a time, already attached to player %@"
+ "<<<< AVPlayerOutput >>>> %s: Failed to create and configure FVR with error: %d"
+ "<<<< AVPlayerOutput >>>> %s: FigVideoReceiverSetActiveConfigurationChangedHandler failed with error: %d"
+ "<<<< AVPlayerOutput >>>> %s: Received invalid preset %d"
+ "<<<< AVPlayerOutput >>>> %s: unable to attach to player, received error %d when attempting to create and configure fvr/fvt pair"
+ "<<<< AVPubSub >>>> %s:  called for %@"
+ "<<<< AVPubSub >>>> %s: Adding observer for %@ in %@"
+ "<<<< AVPubSub >>>> %s: Calling subscriber block because %@ fired for %@"
+ "<<<< AVPubSub >>>> %s: Calling subscriber block for %@"
+ "<<<< AVPubSub >>>> %s: Calling subscriber block from output publisher for %@"
+ "<<<< AVPubSub >>>> %s: Calling subscriber block with initial value for %@"
+ "<<<< AVPubSub >>>> %s: Calling subscriber block with nil publisher for %@"
+ "<<<< AVPubSub >>>> %s: Not publishing stale value to subscriber block for %@"
+ "<<<< AVPubSub >>>> %s: Notification observer calling callback in %@"
+ "<<<< AVPubSub >>>> %s: Removing observer in %@"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO because the multichannel audio strategy permits exclusive passthrough"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since AirPlay Video is active"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since Buffered AirPlay is active"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since action-at-end is NOT advance"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since one of items is HLS"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item doesn't have audio track"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item's number of tracks is not 1"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item doesn't have audio track"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item's number of tracks is not 1"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. YES"
+ "<<<< AVQueuePlayer >>>> %s: called (self = %@)"
+ "<<<< AVQueuePlayer >>>> %s: called (self = %@, item = %@)"
+ "<<<< AVQueuePlayer >>>> %s: called (self = %@, item = %@, afterItem = %@"
+ "<<<< AVRouteDetector >>>> %s: AirPlay device discovery disabled."
+ "<<<< AVRouteDetector >>>> %s: AirPlay device discovery enabled."
+ "<<<< AVRouteDetector >>>> %s: AirPlay devices present: %d"
+ "<<<< AVRouteDetector >>>> %s: Custom routes present: %d"
+ "<<<< AVRouteDetector >>>> %s: Posting AVRouteDetectorMultipleRoutesDetectedDidChangeNotification."
+ "<<<< AVRoutingSessionManager >>>> %s: Returning %@"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %d (self=%p)"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: Failed to create FigSampleBufferAudioRenderer: %@"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p]"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] Transitioning to status: %d"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called:"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %1.3f"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %@"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %d"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %lu"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: %p"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] called: content is now marked as %s"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] created"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] found contextUUID : %@"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] setting routing context id : %@"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: [%p] trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: adding notification listener to %p with listener %p"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: called"
+ "<<<< AVSampleBufferAudioRenderer >>>> %s: removing notification listener to %p with listener %p"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p]"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] %@, on thread %@"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Hiding contentLayer because bounds is CGSizeZero"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] No formatDescription found in sampleBuffer"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Setting position(%d,%d), bounds(%dx%d), transform scale(%.3fx%.3f), offset(%d,%d)"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] Unhiding contentLayer because bounds is nonzero"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] bounds: %@"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p] videoRect: %@"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: [%p], on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Cleaning-up renderer %p for synchronizerInternal %p"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: Failed to create FigSampleBufferRenderSynchronizer: %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] %p, on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Error adding an AudioRenderer to the FigSynchronizer: %d"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Failed to add Renderer %@; error returned from _addRenderer: %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Setting self as render synchronizer on renderer (%p) failed"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Too many audio renderers"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Trying to add a renderer (%p) to same synchronizer"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] Trying to add multiple audio renderers when disallowed"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] adding renderer %p, on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] called for renderer %p; time: %1.3f"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] created (internal: %p)"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] invalidated old scheduled removal of renderer %p"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] old once observer already fired before we could invalidate it (renderer: %p)"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] rate: %1.3f; time: %1.3f; hostTime: %1.3f; fig error: %d"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] releasing on main thread avsbdl %p, on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] removalBlock called; weakToSelf: %p; weakToRenderer: %p"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] retaining avsbdl %p, on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p] successfully scheduled removal of renderer %p at time %1.3f"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: [%p], on thread %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called (center=%@, listener=%p, name=%@, object=%p, payload=%@)"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: called (self = <%p>, time observer = <%p>)"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: error: %@"
+ "<<<< AVSampleBufferRenderSynchronizer >>>> %s: unknown renderer: %p"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: Dispatching -outputSequenceWasFlushed:"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArray failed: %d"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: FigVideoQueueSetProperty for kFigVideoQueueProperty_VisualContextArrayOptions failed: %d"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCopyImageForTime did not provide a imageOriginalTimeOut value. Bailing."
+ "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextCreate failed: %d"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: FigVisualContextSetImageAvailableImmediateCallback failed: %d"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: Sending -outputSequenceWasFlushed: to delegate"
+ "<<<< AVSampleBufferVideoOutput >>>> %s: Unable to copy next image from visual context. Bailing."
+ "<<<< AVSampleBufferVideoOutput >>>> %s: copyPixelBufferForSourceTime requestTime %1.3f pb %p time %1.3f"
+ "<<<< AVSampleBufferVideoRenderer >>>>"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: Unable to set expectMinimumUpcomingSampleBufferPresentationTime because minimumUpcomingPresentationTime is not numeric"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %@], on thread %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Enqueue sample buffer failed error %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Failed to copy currently displayed pixel buffer although no error"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received complete decode for preroll"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received external protection status changed to \"%@\""
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received flush complete"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received lost decoder state error"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received video queue did drop below low water level"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Received video queue failed with error %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Setting %d video targets."
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p] Setting display layer %p"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, %p], on thread %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p, exit layerQueue block, on thread %@]"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p]"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Adding %p"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Calling completion handler with %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Calling completion handler with success"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to copy currently displayed pixel buffer as there is no video queue"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to create AVSBVR error %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed to create video queue error %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Failed with error %d at %s"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] FigVideoQueueFlush returned error %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Flush completed but no pending callback block found"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Flush returned err=%d. Recreating FigVideoQueue. %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Ignoring enqueueSampleBuffer because status is failed"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] No formatDescription found in sampleBuffer"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] No pending preroll callback"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Output obscured = %@, post notification: %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Received video queue decode error \"%@\""
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] RemoveDisplayedImage=%s, handler=%p, on thread %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Removing %p"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Setting %p, returning %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Skip stale callback, requestId (%d) != pendingPrerollRequestID (%d)"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Total frames enqueued since last flush %d"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] UpcomingPTSExpectation is enabled, but enqueuePTS:%.3f is smaller than expectedMinimumUpcomingPTS:%.3f"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Visibility changed to %s, post notification: %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] readyForDisplay changed (%@), post notification: %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] releasing %p on main thread, on thread %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] timebase %@"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p], on thread %@"
+ "<<<< AVSampleCursor >>>> %s: FigSampleCursorCreateSampleBuffer failed (%d)"
+ "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetDecodeTimeStamp failed (%d)"
+ "<<<< AVSampleCursor >>>> %s: FigSampleCursorGetPresentationTimeStamp failed (%d)"
+ "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByDecodeTime failed (%d)"
+ "<<<< AVSampleCursor >>>> %s: FigSampleCursorStepByPresentationTime failed (%d)"
+ "<<<< AVScheduledAudioParameters >>>> %s: not a valid scheduled ramp class"
+ "<<<< AVScheduledParameterRamp >>>> %s: Unknown ramp mode: %d"
+ "<<<< AVStreamDataParser >>>>"
+ "<<<< AVStreamDataParser >>>> %s: Exception when creating default key session: %@"
+ "<<<< AVStreamDataParser >>>> %s: Expected NSData or NSArray, ignoring unexpected \"%@\""
+ "<<<< AVStreamDataParser >>>> %s: Expected NSData sinf, ignoring unexpected \"%@\""
+ "<<<< AVStreamDataParser >>>> %s: abandoning manifold initialization after %ld bytes (max %ld bytes)"
+ "<<<< AVStreamDataParser >>>> %s: appending stream data (flags 0x%x) %@"
+ "<<<< AVStreamDataParser >>>> %s: changing manifold type not permitted during AVStreamDataParser session"
+ "<<<< AVStreamDataParser >>>> %s: created a FigManifold"
+ "<<<< AVStreamDataParser >>>> %s: dealloc"
+ "<<<< AVStreamDataParser >>>> %s: failed to create CMBlockBuffer for %d bytes with data at %p and offset %d, status = %d"
+ "<<<< AVStreamDataParser >>>> %s: init"
+ "<<<< AVStreamDataParser >>>> %s: manifold all new tracks ready, building inspection-only asset"
+ "<<<< AVStreamDataParser >>>> %s: manifold discovered trackID %ld, mediaType %@, remembered for AllNewTracksReady"
+ "<<<< AVStreamDataParser >>>> %s: manifold error %d, track %d, %@"
+ "<<<< AVStreamDataParser >>>> %s: manifold sent PTS %1.5f %d bytes, %@/%@, track %d, flags %d"
+ "<<<< AVStreamDataParser >>>> %s: need delegate to implement streamDataParser:didProvideContentKeyRequestInitializationData:forTrackID:"
+ "<<<< AVStreamDataParser >>>> %s: need more data to sniff"
+ "<<<< AVStreamDataParser >>>> %s: new AVStreamDataAsset using manifold's FigAsset"
+ "<<<< AVStreamDataParser >>>> %s: new AVStreamDataAsset with tracks %@"
+ "<<<< AVStreamDataParser >>>> %s: no asset yet so caching sample buffer (now cached %d bytes, %.3f seconds)"
+ "<<<< AVStreamDataParser >>>> %s: no manifold, sniffing data to initialize one..."
+ "<<<< AVStreamDataParser >>>> %s: providePendingMediaData"
+ "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because trackID %d ended"
+ "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because trackID %ld got a new format description"
+ "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset because we've not got a CMFormatDescription for trackID %d"
+ "<<<< AVStreamDataParser >>>> %s: rebuilding AVStreamDataAsset with additional trackID %d"
+ "<<<< AVStreamDataParser >>>> %s: registering for manifold callbacks from trackID %d"
+ "<<<< AVStreamDataParser >>>> %s: set preferSandboxedParsing to %d"
+ "<<<< AVStreamDataParser >>>> %s: setShouldProvideMediaData:forTrackId:%d, not providing media for %@"
+ "<<<< AVStreamDataParser >>>> %s: shouldProvideMediaDataForTrackID said no, ignoring media for trackID %d"
+ "<<<< AVStreamDataParser >>>> %s: sniffing stream data (flags 0x%x) %@"
+ "<<<< AVStreamDataParser >>>> %s: switching manifold"
+ "<<<< AVStreamDataParser >>>> %s: trackID %ld got a new format description, remembered for AllNewTracksReady"
+ "<<<< AVStreamDataParser >>>> %s: trackID %ld is not encrypted or using unsupported encryption. Removing the cached decryptor for this track."
+ "<<<< AVStreamDataParser >>>> %s: trackID %ld is using supported encryption"
+ "<<<< AVStreamDataParser >>>> %s: unregistering for manifold callbacks from trackID %d"
+ "<<<< AVStreamSession >>>> %s: added parser %@, now have: %@"
+ "<<<< AVStreamSession >>>> %s: appIdentifier %@ = %@"
+ "<<<< AVStreamSession >>>> %s: appIdentifier %@, removing %@"
+ "<<<< AVStreamSession >>>> %s: created CPEProtector"
+ "<<<< AVStreamSession >>>> %s: dealloc"
+ "<<<< AVStreamSession >>>> %s: expiring internal content key session %@"
+ "<<<< AVStreamSession >>>> %s: failed to set storage URL %@, status %d"
+ "<<<< AVStreamSession >>>> %s: init"
+ "<<<< AVStreamSession >>>> %s: init with %@"
+ "<<<< AVStreamSession >>>> %s: removed parser %@, now have %@"
+ "<<<< AVStreamSession >>>> %s: unexpected setAppIdentifier %p (currently %p)"
+ "<<<< AVStreamSession >>>> %s: unexpected setFigCPEProtectorSessionIdentifier %p (currently %p)"
+ "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> created for firing time [%1.3f]"
+ "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> firing for firing time [%1.3f] at current time [%1.3f]"
+ "<<<< AVTimebaseObserver >>>> %s: Absolute timebase observer <%p> with source <%p> at current time [%f] nextfire [%f]"
+ "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> Firing at current time [%1.3f]"
+ "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> created with timebase %p and fire times: %@"
+ "<<<< AVTimebaseObserver >>>> %s: Occasional timebase observer <%p> with source <%p> at current time [%f] nextfire [%f]"
+ "<<<< AVTimebaseObserver >>>> %s: Periodic Observer <%p> Jumped to time [%f]"
+ "<<<< AVTimebaseObserver >>>> %s: Periodic Observer <%p>: Detected stop time jump to the last time where rate fell to zero and have winnowed this event"
+ "<<<< AVTimebaseObserver >>>> %s: Playback direction did change. Resetting timer"
+ "<<<< AVTimebaseObserver >>>> %s: Playback resumed. Observe immediate."
+ "<<<< AVTimebaseObserver >>>> %s: Playback stopped. Observe immediate."
+ "<<<< AVTimebaseObserver >>>> %s: Timebase observer invalidated, ignoring notification"
+ "<<<< AVTimebaseObserver >>>> %s: Timebase returned non-numeric time (%lld/%d/%#x/%lld)) so setting to kCMTimeZero"
+ "<<<< AVTimebaseObserver >>>> %s: Timebase returned time with non-zero epoch(%lld) so setting to kCMTimeZero"
+ "<<<< AVTimebaseObserver >>>> %s: Timebase returned time(%@)"
+ "<<<< AVTimebaseObserver >>>> %s: Timebase returned time(%@), clamped from time(%@)"
+ "<<<< AVTimebaseObserver >>>> %s: after applying offset %@, nextIntervalTime is now %@"
+ "<<<< AVTimebaseObserver >>>> %s: engage timebase <%p> notifications for <%p>"
+ "<<<< AVTimebaseObserver >>>> %s: firing at time == %@"
+ "<<<< AVTimebaseObserver >>>> %s: rescheduling after non-periodic firing near time == %@"
+ "<<<< AVTimebaseObserver >>>> %s: rescheduling after periodic firing at time == %@"
+ "<<<< AVTimebaseObserver >>>> %s: scheduling for == %@"
+ "<<<< AVTimebaseObserver >>>> %s: timebase rate change from [%f] to [%f]"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Class must be an instance of NSString"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Cue must be an instance of NSString"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_DiscoveryTimestamp must be an instance of NSDate"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_Duration must be an instance of NSNumber"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_ID must be an instance of NSString"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_MetadataArray must be an instance of NSArray"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_ModificationTimestamp must be an instance of NSDate"
+ "<<<< AVTimedMetadataGroup >>>> %s: Value %@ for kFigPlaybackItemTaggedRangeMetadataKey_StartDate must be an instance of NSDate"
+ "<<<< AVUtilities >>>> %s: called (queue=%p, currentQueue=%p, dispatch_get_main_queue()=%p, NSThread isMainThread=%d)"
+ "<<<< AVUtilities >>>> %s: dispatching block to queue"
+ "<<<< AVUtilities >>>> %s: dispatching to background queue"
+ "<<<< AVUtilities >>>> %s: running block synchronously"
+ "<<<< AVVideoComposition >>>> %s: Unknown video compositor name for FigRemaker: %@"
+ "<<<< AVVideoComposition >>>> %s: Using video compositor: %@"
+ "<<<< AVVideoComposition >>>> %s: dictionaryRepresentation only accepts RGB color space for backgroundColor"
+ "<AVPlayerLayer %p%@%@%@>"
+ "@\"AVCoordinatedPlaybackSuspension\""
+ "AV Perf - Begin: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
+ "AV Perf - End: enableTelemetry=YES intervalName=%{public,signpost.telemetry:string1}sisMainThread=%{public,signpost.telemetry:number1}d"
+ "AVAsset.m"
+ "AVAssetByteStreamCreateWithAsset"
+ "AVAssetByteStreamFinalize"
+ "AVAssetByteStreamGetAvailableLengthAtOffset"
+ "AVAssetByteStreamRead"
+ "AVAssetByteStreamReadAndCreateBlockBuffer"
+ "AVAssetDownloadConfiguration.m"
+ "AVAssetDownloadSession.m"
+ "AVAssetReaderOutputCaptionAdaptor.m"
+ "AVAssetResourceLoader.m"
+ "AVAssetWriterFigAssetWriterHandleCompletedNotification"
+ "AVAssetWriterFigAssetWriterHandleFailedNotification"
+ "AVAssetWriterInputFigAssetWriterEndPassOperationPassFinished"
+ "AVCanWriteFilesToDirectoryAtURL"
+ "AVCompositionTrack.m"
+ "AVContentKeySession.m"
+ "AVDefaultRoutingContextFactory"
+ "AVEnsureNotOnMainThread"
+ "AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImpl.m"
+ "AVFigRouteDescriptorOutputDeviceImplCanSetEndpointVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange"
+ "AVFigRouteDiscovererAvailableRoutesChanged"
+ "AVFigRouteDiscovererEndpointDescriptorChanged"
+ "AVFigRouteDiscovererRoutePresentChanged"
+ "AVFigRoutingContextRouteChangeOperationRouteChangeComplete"
+ "AVLocalizedError"
+ "AVLocalizedStringFromTableWithLocaleWithBundleIdentifier"
+ "AVMediaFileSegmenterStatusCancelled"
+ "AVMediaFileSegmenterStatusCompleted"
+ "AVMediaFileSegmenterStatusFailed"
+ "AVMediaFileSegmenterStatusSegmenting"
+ "AVMediaFileSegmenterStatusUnknown"
+ "AVMetadataItem.m"
+ "AVMetadataItemMakeDataFromBoxedMetadata"
+ "AVOperationStatusResolveOldAndNew"
+ "AVOutputContextUsesRouteConfigUpdatedNotification"
+ "AVOutputDeviceCopyFigModeForSpatialAudioMode"
+ "AVOutputDeviceDescriptionsFromFigDescriptions"
+ "AVOutputDeviceGetFigEndpoint"
+ "AVOutputDeviceGetFigRouteDescriptor"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode"
+ "AVOutputDeviceImplIsMutedForEndpointID"
+ "AVPerfTelemetry"
+ "AVPerformDelegateCallbackSynchronouslyForDelegateStorageIfCurrentDelegateQueueIsQueueElseDispatchToCurrentDelegateQueue"
+ "AVPlayerCaptionLayer <%p>"
+ "AVPlayerGetFigPlayerTypeForAsset"
+ "AVPlayerItem addOutput"
+ "AVPlayerItem audioMix"
+ "AVPlayerItem currentMediaSelection"
+ "AVPlayerItem customVideoCompositor"
+ "AVPlayerItem initWithAsset"
+ "AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys"
+ "AVPlayerItem outputs"
+ "AVPlayerItem removeOutput"
+ "AVPlayerItem selectMediaOption:inMediaSelectionGroup"
+ "AVPlayerItem selectMediaOption:mediaSelectionOption:mediaSelectionGroup"
+ "AVPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup"
+ "AVPlayerItem setAudioMix"
+ "AVPlayerItem setVideoComposition"
+ "AVPlayerItem stepByCount"
+ "AVPlayerItem videoComposition"
+ "AVPlayerItemTrack assetTrack"
+ "AVPlayerItemVideoOutput_figVCSequentialAvailableCallback_block_invoke_3"
+ "AVPlayerItemVideoOutput_timebaseNotificationCallback_block_invoke"
+ "AVPlayerLayer <%p>"
+ "AVPlayerLayer <%p> (closedCaptionLayer)"
+ "AVPlayerLayer <%p> (videoLayer)"
+ "AVPlayerLayerFilterClientLayersFromLayerWithIndexPath"
+ "AVPlayerOutput.m"
+ "AVSBAR init failed with err=%d at %s. Please file a radar to AVFoundation|All and relate to rdar://problem/59801501"
+ "AVSBVR failed with error %d at %s."
+ "AVSampleBufferDisplayLayer <%p>"
+ "AVSampleBufferDisplayLayer <%p> (content layer)"
+ "AVSampleBufferRenderSynchronizer init"
+ "AVSampleBufferVideoRenderer.m"
+ "AVSerializeOnQueueAsyncIfNecessary"
+ "AVStreamDataParser.m"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData"
+ "AVTimebaseObserver_figTimebaseGetTime"
+ "AVTimebaseObserver_timebaseNotificationCallback_block_invoke"
+ "CDS"
+ "CMTagCollectionCreateWithVideoOutputPreset"
+ "Could not set KeyResponseReceived state on cryptor."
+ "Cryptor is not available to create key request."
+ "FVQSetProperty(ControlTimebase)"
+ "FVQSetProperty(DisplayLayer)"
+ "Failed on init"
+ "Failed to allocate CFMutableDictionary"
+ "Failed to allocate buffer for FigBoxedMetadata -> CFData conversion"
+ "Failed to prepare cryptor"
+ "Failed to set video target array on video queue."
+ "FigCaptionClient"
+ "FigPlayer_File"
+ "FigPlayer_Stream"
+ "FigSBARAirPlayCreate()"
+ "FigSBARCreateWithOptions()"
+ "FigSBARRoutingSessionCreate()"
+ "FigSubtitleCALayer"
+ "FigVideoQueueCreate"
+ "FigVideoQueueStart"
+ "Hiding"
+ "InternalPerfTelemetry"
+ "Invalid asset track"
+ "N/A"
+ "NOT visible"
+ "NULL"
+ "NULL figAsset"
+ "NULL handlerServerXPCEndpoint"
+ "No FCKS available"
+ "No endpoint found for route descriptor"
+ "Received invalid preset"
+ "Showing"
+ "The AVSampleBufferDisplayLayer's content layer is nil."
+ "Trying to create AVAssetDownloadContentConfiguration with an invalid AVAssetVariantQualifier"
+ "Visible"
+ "_avplLoopingItemFailedToPlayToEndTimeNotificationHandler"
+ "_compactDescription"
+ "_enqueueSingleSampleBufferStatic"
+ "_enqueuedFramesForLoggingOnly"
+ "_figManifoldError"
+ "_figVideoQueueCompletedDecodeForPreroll"
+ "_figVideoQueueDecodeError"
+ "_figVideoQueueDidDropBelowLowWaterLevel"
+ "_figVideoQueueExternalProtectionStatusChanged"
+ "_figVideoQueueFailed"
+ "_figVideoQueueFlushComplete"
+ "_figVideoQueueLostDecoderState"
+ "_interstitialSuspension"
+ "_sampleDescriptionExtensionAtomForKey"
+ "_setinterstitialSuspension:"
+ "addSampleBufferDisplayLayer failed to set content layer"
+ "aig_trace"
+ "appendCaptionGroupToQueue"
+ "assetTrackNotificationHandler"
+ "assetinspector_trace"
+ "assetreaderoutput_trace"
+ "assettrackinspector_trace"
+ "assetwriter_trace"
+ "assetwriterinput_trace"
+ "assetwriterinputannotationadaptor_trace"
+ "assetwriterinputmetadataadaptor_trace"
+ "audio only (UnaccompaniedByVisuals)"
+ "audiovisual"
+ "avAssetDownloadSession_figAssetNotificationCallback"
+ "avAssetDownloadSession_figPlaybackItemNotificationCallback"
+ "avasset_trace"
+ "avassetcache_trace"
+ "avassetcollection_trace"
+ "avassetcollectioninspectorloader_trace"
+ "avassetresourceloader_trace"
+ "avassetstoragemanager_trace"
+ "avasynchronouskeyvalueloading_trace"
+ "avcaptionrenderer_trace"
+ "avcc_trace"
+ "avcifilter_trace"
+ "avckrg_externalProtectionStateChangedCallback"
+ "avckrg_keyResponseErrorCallback"
+ "avckrg_keyResponseSuccessfullyProcessedCallback"
+ "avckrg_persistentKeyUpdatedCallback"
+ "avckrg_secureStopDidFinalizeRecordCallback"
+ "avcks_decodeInitializationDataAndCopyInformation"
+ "avdatadelegateasset_trace"
+ "avexport_trace"
+ "avloggingidentifier_trace"
+ "avmediaselectiongroup_trace"
+ "avmetadataitem_trace"
+ "avmovie_trace"
+ "avoperation_trace"
+ "avpixelbufferattributemediator_trace"
+ "avplayer_fpInterstitialCoordinatorNotificationCallback"
+ "avplayer_fpNotificationCallback"
+ "avplayer_fpNotificationCallback_block_invoke"
+ "avplayer_playbackcoordinator_SetPlaybackCoordinatorInterstitialActive"
+ "avplayercaptionlayer_trace"
+ "avplayerinterstitialeventmonitor_fpNotificationCallback"
+ "avplayeritem_fpItemNotificationCallback_block_invoke"
+ "avplayeritem_fpItemNotificationCallback_block_invoke_2"
+ "avplayeritem_fpItemNotificationCallback_block_invoke_3"
+ "avplayeritem_fpItemNotificationCallback_block_invoke_4"
+ "avplayeritem_fpItemNotificationCallback_block_invoke_7"
+ "avplayeritemlegibleoutput_trace"
+ "avplayeritemmediadatacollector_trace"
+ "avplayeritemmetadatacollector_trace"
+ "avplayeritemmetadataoutput_trace"
+ "avplayeritemoutput_trace"
+ "avplayeritemrenderedlegibleoutput_trace"
+ "avplayerlayer_trace"
+ "avplayerlooper_trace"
+ "avplayeroutput_trace"
+ "avqueueplayer_trace"
+ "avrendersynchronize_cleanUpAllAddedRenderers"
+ "avrendersynchronize_performRendererRemoval"
+ "avrendersynchronizer_timebaseRateChanged"
+ "avsamplebufferaudiorenderer_trace"
+ "avsamplebufferdisplaylayer_trace"
+ "avsamplebuffergenerator_trace"
+ "avsamplebufferoutput_trace"
+ "avsamplebufferrendersynchronizer_trace"
+ "avsamplebuffervideooutput_trace"
+ "avsamplecursor_trace"
+ "avsegmenter_trace"
+ "avstreamdataparser_trace"
+ "avstreamseassion_trace"
+ "avtimebaseobserver_trace"
+ "avtimedmetadatagroup_trace"
+ "avurlasset_setupGuts"
+ "avutilities_trace"
+ "badly formatted PSSH data"
+ "badly formatted key request init data - codecType not valid"
+ "badly formatted key request init data - containerType not valid"
+ "badly formatted key request init data - mediaType not valid"
+ "badly formatted key request init data - sinf array not found"
+ "bail error check"
+ "basics"
+ "boss NULL"
+ "ccr_trace"
+ "cmTimebaseNotificationCallback_TimeJumped"
+ "colorSpace"
+ "completed"
+ "composition_trace"
+ "could not create trackDecryptor"
+ "createFigAsset"
+ "creationOptions NULL"
+ "cryptor is NULL"
+ "customURLAuthHandlerHandleRequestCallback"
+ "customURLAuthHandlerRequestCancelled"
+ "customURLHandlerHandleRequestCallback"
+ "customURLHandlerRequestCancelled"
+ "delegateutils_trace"
+ "download_trace"
+ "expected initialization data to be a JSON dictionary containing an array of SINF data"
+ "failed to alloc content key request"
+ "failed to convert initializationData to a JSON object"
+ "failed to query records due to an internal error"
+ "failed to remove records due to an internal error"
+ "failure"
+ "figAsset already set"
+ "figAssetReaderDecodeError"
+ "figAssetReaderFailed"
+ "figAssetReaderSampleBufferDidBecomeAvailable"
+ "figLoaderNotificationHandler"
+ "figPlaybackItemTrackResetSampleBufferExtraction"
+ "figPlaybackItemTrackSampleBufferDidBecomeAvailable"
+ "filesystemutilities_trace"
+ "frame"
+ "handleAndReflectFigAssetNotification"
+ "handleFigAssetCollectionNotification"
+ "handleFigAssetCollectionNotification_block_invoke"
+ "handleFigAssetTrackNotification"
+ "handleFigAssetTrackNotification_block_invoke"
+ "hlsvariant_trace"
+ "init timebases"
+ "inspection"
+ "inspector_trace"
+ "install note handlers"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMTagCollectionError_ParamErr"
+ "kFigBaseObjectError_ParamErr"
+ "kFigCPEError_InvalidState"
+ "kFigContentKeyBossError_AllocationFailed"
+ "kFigMetadataReaderError_AllocationFailed"
+ "kFigRouteDiscovererError_InvalidParameter"
+ "kFigSSMError_InvalidState"
+ "key request has not succeeded. value not available."
+ "kvodispatcher_trace"
+ "mismatched handler"
+ "nil reference"
+ "no figAsset"
+ "non-"
+ "non-NULL"
+ "not an AVAssetResourceLoader"
+ "not an AVAssetResourceLoaderRemoteHandlerContext"
+ "not an AVContentKeyReportGroup"
+ "not an AVContentKeySession"
+ "not spatial"
+ "pathWithComponents:"
+ "platformutilities_trace"
+ "playback"
+ "return nil AVSBAR"
+ "scheduledaudioparameters_trace"
+ "self.figAsset NULL"
+ "setBorderColor:"
+ "setBorderWidth:"
+ "stringWithValidatedFormat"
+ "stringWithValidatedFormatArg2"
+ "stringWithValidatedFormatInteger"
+ "stringWithValidatedFormatString"
+ "subarrayWithRange:"
+ "visible"
+ "yes"
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"

```
