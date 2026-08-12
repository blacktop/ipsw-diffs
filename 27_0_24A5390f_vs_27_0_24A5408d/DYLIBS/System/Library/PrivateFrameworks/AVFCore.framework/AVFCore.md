## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2450.71.1.11.1
-  __TEXT.__text: 0x21f614
+2450.75.1.0.0
+  __TEXT.__text: 0x1c9894
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1c044
-  __TEXT.__cstring: 0x35853
-  __TEXT.__const: 0x1f38
-  __TEXT.__gcc_except_tab: 0xb3e4
-  __TEXT.__oslogstring: 0x20fac
+  __TEXT.__objc_methlist: 0x1c114
+  __TEXT.__cstring: 0x26da3
+  __TEXT.__gcc_except_tab: 0x9fec
+  __TEXT.__const: 0x1e48
+  __TEXT.__oslogstring: 0x50d7
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x40d

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xa738
+  __TEXT.__unwind_info: 0xa4e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b80
+  __DATA_CONST.__const: 0x5b90
   __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb570
+  __DATA_CONST.__objc_selrefs: 0xb5a0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xd68
   __DATA_CONST.__objc_arraydata: 0x310
-  __DATA_CONST.__got: 0x4848
+  __DATA_CONST.__got: 0x4850
   __AUTH_CONST.__const: 0x1258
-  __AUTH_CONST.__cfstring: 0x1aae0
-  __AUTH_CONST.__objc_const: 0x32998
+  __AUTH_CONST.__cfstring: 0x1a640
+  __AUTH_CONST.__objc_const: 0x329b8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2078
+  __AUTH_CONST.__auth_got: 0x2040
   __AUTH.__objc_data: 0x8e88
   __AUTH.__data: 0x1f0
   __DATA.__objc_ivar: 0x27dc
-  __DATA.__data: 0x189c
+  __DATA.__data: 0x183c
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x450
-  __DATA.__bss: 0x13e0
+  __DATA.__common: 0x1e0
+  __DATA.__bss: 0x1410
   __DATA_DIRTY.__objc_data: 0x2828
-  __DATA_DIRTY.__common: 0x2e0
-  __DATA_DIRTY.__bss: 0x211
+  __DATA_DIRTY.__common: 0x1e0
+  __DATA_DIRTY.__bss: 0x1e1
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12623
-  Symbols:   28392
-  CStrings:  6533
+  Functions: 12078
+  Symbols:   28360
+  CStrings:  4299
 
Symbols:
+ -[AVAsset _authoredMediaSelectionGroupDictionaries]
+ -[AVAsset _availableMediaCharacteristicsWithMediaSelectionOptionsIncludingExtendedOptions:]
+ -[AVAsset _mediaSelectionGroupForMediaCharacteristic:extended:]
+ -[AVAsset _mediaSelectionGroupForPropertyList:extended:mediaSelectionOption:]
+ -[AVAsset authoredMediaSelectionGroupForMediaCharacteristic:]
+ -[AVAsset availableMediaCharacteristicsWithAuthoredMediaSelectionOptions]
+ -[AVAsset mediaSelectionGroupForPropertyList:extended:mediaSelectionOption:]
+ -[AVAssetInspector _authoredMediaSelectionGroupDictionaries]
+ -[AVAssetTrack transportStreamPID]
+ -[AVAssetTrackInspector transportStreamPID]
+ -[AVComposition _authoredMediaSelectionGroupDictionaries]
+ -[AVFigAssetInspector _authoredMediaSelectionGroupDictionaries]
+ -[AVPlayer _isAirPlaySenderActive]
+ -[AVSampleBufferVideoRenderer triggerReportForError:description:]
+ -[AVStreamDataAsset copyAssetWithAdditionalTrackID:mediaType:languageCode:transportStreamPID:]
+ -[AVStreamDataAsset languageCodeForTrackID:]
+ -[AVStreamDataAsset transportStreamPIDForTrackID:]
+ -[AVStreamDataAssetTrackInspector languageCode]
+ -[AVStreamDataAssetTrackInspector transportStreamPID]
+ GCC_except_table104
+ GCC_except_table110
+ GCC_except_table132
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table172
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table242
+ GCC_except_table259
+ GCC_except_table329
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table344
+ GCC_except_table349
+ GCC_except_table360
+ GCC_except_table368
+ GCC_except_table370
+ GCC_except_table374
+ GCC_except_table381
+ GCC_except_table396
+ GCC_except_table410
+ GCC_except_table420
+ GCC_except_table430
+ GCC_except_table433
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table471
+ GCC_except_table479
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table514
+ GCC_except_table557
+ GCC_except_table566
+ GCC_except_table581
+ GCC_except_table585
+ GCC_except_table595
+ GCC_except_table603
+ GCC_except_table612
+ GCC_except_table617
+ GCC_except_table621
+ GCC_except_table623
+ GCC_except_table632
+ GCC_except_table636
+ GCC_except_table640
+ GCC_except_table642
+ GCC_except_table648
+ GCC_except_table654
+ GCC_except_table660
+ GCC_except_table663
+ GCC_except_table676
+ GCC_except_table678
+ GCC_except_table680
+ GCC_except_table686
+ GCC_except_table688
+ GCC_except_table693
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table720
+ GCC_except_table730
+ GCC_except_table732
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table746
+ GCC_except_table761
+ GCC_except_table769
+ GCC_except_table783
+ GCC_except_table791
+ GCC_except_table793
+ GCC_except_table805
+ GCC_except_table808
+ GCC_except_table810
+ GCC_except_table820
+ GCC_except_table822
+ GCC_except_table824
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table840
+ GCC_except_table844
+ GCC_except_table848
+ GCC_except_table85
+ GCC_except_table868
+ GCC_except_table873
+ GCC_except_table880
+ GCC_except_table883
+ GCC_except_table885
+ GCC_except_table97
+ _AVPlayerInitializeIAPD.onceToken
+ _FigSignalErrorAtGM
+ _OBJC_IVAR_$_AVStreamDataParserInternal._hintForStartTime
+ ___104-[AVAssetResourceLoader _performDelegateSelector:withObject:representingNewRequest:key:fallbackHandler:]_block_invoke_2
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_3
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_4
+ ___110-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:pauseAllowed:]_block_invoke_4
+ ___110-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:pauseAllowed:]_block_invoke_5
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
+ ___49-[AVPlayerCaptionLayer stopShowingCaptionPreview]_block_invoke_2
+ ___51-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke_2
+ ___51-[AVSampleBufferVideoRenderer enqueueSampleBuffer:]_block_invoke_3
+ ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke_3
+ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3
+ ___57-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]_block_invoke_3
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_3
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_4
+ ___62-[AVPlayerItem _setItemAudioTapProcessor:fromAudioMixContext:]_block_invoke_2
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke_2
+ ___63-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke_3
+ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke_2
+ ___64-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:]_block_invoke_2
+ ___64-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___67-[AVCurrentMediaSelectionCache clientSelectedOrEmptyMediaSelection]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_2
+ ___67-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:]_block_invoke_3
+ ___67-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:]_block_invoke_4
+ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke_3
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_8
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_9
+ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_2
+ ___67-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:]_block_invoke_3
+ ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke_2
+ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___71-[AVPlayerCaptionLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_3
+ ___74-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:]_block_invoke_2
+ ___77+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke_2
+ ___79-[AVPlayerItemMetadataOutput(AVPlayerItemMetadataOutput_Internal) _signalFlush]_block_invoke_3
+ ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke_3
+ ___80-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]_block_invoke_3
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_5
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_6
+ ___82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_7
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_6
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_7
+ ___84-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]_block_invoke_3
+ ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_4
+ ___90-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke_2
+ ___92-[AVPlayer(AVPlayerVideoDisplaySleepPrevention) setPreventsDisplaySleepDuringVideoPlayback:]_block_invoke_2
+ ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_2
+ ___avplayer_fpNotificationCallback_block_invoke_10
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
+ ___block_descriptor_56_e8_32o40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___figEndpointNotificationCallback_block_invoke_2
+ ___figEndpointNotificationCallback_block_invoke_3
+ ___handleFigAssetTrackNotification_block_invoke_2
+ __attachToFigPlayer.sMetricRetrievalOnceToken
+ __attachToFigPlayer.sMetricRetrievalQueue
+ __makeSTSLabel.onceToken
+ __makeSTSLabel.sRunningLabelID
+ _fig_log_get_emitter
+ _kBlockedBundleIdentifiers
+ _kFigManifoldTrackProperty_LanguageCode
+ _kFigManifoldTrackProperty_TransportStreamPID
+ _objc_msgSend$_authoredMediaSelectionGroupDictionaries
+ _objc_msgSend$_availableMediaCharacteristicsWithMediaSelectionOptionsIncludingExtendedOptions:
+ _objc_msgSend$_isAirPlaySenderActive
+ _objc_msgSend$_mediaSelectionGroupForMediaCharacteristic:extended:
+ _objc_msgSend$_mediaSelectionGroupForPropertyList:extended:mediaSelectionOption:
+ _objc_msgSend$copyAssetWithAdditionalTrackID:mediaType:languageCode:transportStreamPID:
+ _objc_msgSend$languageCodeForTrackID:
+ _objc_msgSend$transportStreamPID
+ _objc_msgSend$transportStreamPIDForTrackID:
+ _objc_msgSend$triggerReportForError:description:
+ _plannerRTCKeyDescriptors
+ _sAVPlayerIAPDReadWriteQueue
+ _sParticipatesInSTS
- -[AVPlayerLayer _compactDescription]
- -[AVStreamDataAsset copyAssetWithAdditionalTrackID:mediaType:]
- GCC_except_table106
- GCC_except_table1184
- GCC_except_table131
- GCC_except_table141
- GCC_except_table145
- GCC_except_table149
- GCC_except_table159
- GCC_except_table160
- GCC_except_table163
- GCC_except_table169
- GCC_except_table178
- GCC_except_table183
- GCC_except_table201
- GCC_except_table235
- GCC_except_table323
- GCC_except_table338
- GCC_except_table340
- GCC_except_table343
- GCC_except_table347
- GCC_except_table350
- GCC_except_table367
- GCC_except_table369
- GCC_except_table375
- GCC_except_table377
- GCC_except_table384
- GCC_except_table390
- GCC_except_table395
- GCC_except_table407
- GCC_except_table411
- GCC_except_table419
- GCC_except_table423
- GCC_except_table428
- GCC_except_table431
- GCC_except_table436
- GCC_except_table447
- GCC_except_table452
- GCC_except_table458
- GCC_except_table467
- GCC_except_table469
- GCC_except_table472
- GCC_except_table476
- GCC_except_table482
- GCC_except_table498
- GCC_except_table504
- GCC_except_table512
- GCC_except_table517
- GCC_except_table525
- GCC_except_table560
- GCC_except_table565
- GCC_except_table568
- GCC_except_table579
- GCC_except_table582
- GCC_except_table588
- GCC_except_table593
- GCC_except_table598
- GCC_except_table601
- GCC_except_table604
- GCC_except_table606
- GCC_except_table609
- GCC_except_table613
- GCC_except_table615
- GCC_except_table620
- GCC_except_table622
- GCC_except_table641
- GCC_except_table643
- GCC_except_table647
- GCC_except_table649
- GCC_except_table653
- GCC_except_table659
- GCC_except_table675
- GCC_except_table687
- GCC_except_table691
- GCC_except_table698
- GCC_except_table706
- GCC_except_table710
- GCC_except_table724
- GCC_except_table727
- GCC_except_table733
- GCC_except_table747
- GCC_except_table760
- GCC_except_table762
- GCC_except_table766
- GCC_except_table775
- GCC_except_table778
- GCC_except_table787
- GCC_except_table790
- GCC_except_table802
- GCC_except_table804
- GCC_except_table811
- GCC_except_table815
- GCC_except_table819
- GCC_except_table826
- GCC_except_table830
- GCC_except_table833
- GCC_except_table839
- GCC_except_table842
- GCC_except_table847
- GCC_except_table859
- GCC_except_table867
- GCC_except_table877
- GCC_except_table879
- GCC_except_table881
- GCC_except_table884
- _AVAssetExportSessionResumptionFailureReasonIncompatiblePreset
- _AVBacktraceAsString
- _AVBacktraceAsStringWithMaxFrames
- _CMSampleBufferGetNumSamples
- _CMSampleBufferGetPresentationTimeStamp
- _FigDebugIsInternalBuild
- _FigPlaybackRateChangeReasonGetDescription
- _FigSignalErrorAt3
- _NSStringFromRect
- _NSStringFromSize
- _OBJC_IVAR_$_AVSampleBufferVideoRenderer._enqueuedFramesForLoggingOnly
- _OUTLINED_FUNCTION_100
- _OUTLINED_FUNCTION_101
- _OUTLINED_FUNCTION_102
- _OUTLINED_FUNCTION_103
- _OUTLINED_FUNCTION_104
- _OUTLINED_FUNCTION_105
- _OUTLINED_FUNCTION_106
- _OUTLINED_FUNCTION_107
- _OUTLINED_FUNCTION_108
- _OUTLINED_FUNCTION_109
- _OUTLINED_FUNCTION_110
- _OUTLINED_FUNCTION_111
- _OUTLINED_FUNCTION_112
- _OUTLINED_FUNCTION_113
- _OUTLINED_FUNCTION_114
- _OUTLINED_FUNCTION_115
- _OUTLINED_FUNCTION_116
- _OUTLINED_FUNCTION_117
- _OUTLINED_FUNCTION_118
- _OUTLINED_FUNCTION_119
- _OUTLINED_FUNCTION_120
- _OUTLINED_FUNCTION_121
- _OUTLINED_FUNCTION_122
- _OUTLINED_FUNCTION_123
- _OUTLINED_FUNCTION_124
- _OUTLINED_FUNCTION_125
- _OUTLINED_FUNCTION_126
- _OUTLINED_FUNCTION_127
- _OUTLINED_FUNCTION_128
- _OUTLINED_FUNCTION_129
- _OUTLINED_FUNCTION_130
- _OUTLINED_FUNCTION_131
- _OUTLINED_FUNCTION_132
- _OUTLINED_FUNCTION_133
- _OUTLINED_FUNCTION_134
- _OUTLINED_FUNCTION_135
- _OUTLINED_FUNCTION_136
- _OUTLINED_FUNCTION_137
- _OUTLINED_FUNCTION_138
- _OUTLINED_FUNCTION_139
- _OUTLINED_FUNCTION_140
- _OUTLINED_FUNCTION_141
- _OUTLINED_FUNCTION_142
- _OUTLINED_FUNCTION_143
- _OUTLINED_FUNCTION_144
- _OUTLINED_FUNCTION_145
- _OUTLINED_FUNCTION_146
- _OUTLINED_FUNCTION_64
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_67
- _OUTLINED_FUNCTION_68
- _OUTLINED_FUNCTION_69
- _OUTLINED_FUNCTION_70
- _OUTLINED_FUNCTION_71
- _OUTLINED_FUNCTION_72
- _OUTLINED_FUNCTION_73
- _OUTLINED_FUNCTION_74
- _OUTLINED_FUNCTION_75
- _OUTLINED_FUNCTION_76
- _OUTLINED_FUNCTION_77
- _OUTLINED_FUNCTION_78
- _OUTLINED_FUNCTION_79
- _OUTLINED_FUNCTION_80
- _OUTLINED_FUNCTION_81
- _OUTLINED_FUNCTION_82
- _OUTLINED_FUNCTION_83
- _OUTLINED_FUNCTION_84
- _OUTLINED_FUNCTION_85
- _OUTLINED_FUNCTION_86
- _OUTLINED_FUNCTION_87
- _OUTLINED_FUNCTION_88
- _OUTLINED_FUNCTION_89
- _OUTLINED_FUNCTION_90
- _OUTLINED_FUNCTION_91
- _OUTLINED_FUNCTION_92
- _OUTLINED_FUNCTION_93
- _OUTLINED_FUNCTION_94
- _OUTLINED_FUNCTION_95
- _OUTLINED_FUNCTION_96
- _OUTLINED_FUNCTION_97
- _OUTLINED_FUNCTION_98
- _OUTLINED_FUNCTION_99
- __CMBlockBufferAsString
- ___block_descriptor_48_e8_32o40b_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32o40r_e26_v32?0"AVCaption"8Q16^B24ls32l8r40l8
- ___block_descriptor_57_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32o40o48b56w_e24_v16?0"NSNotification"8ls32l8w56l8s48l8s40l8
- ___block_descriptor_72_e8_32o40o48o56r64r_e29_v24?0"NSArray"8"NSError"16lr56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_96_e8_32o40o48o56o64o72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8r88l8
- __figVideoQueueDidDropBelowLowWaterLevel.didDropBelowLowWaterLevelCountForLoggingOnly
- _backtrace
- _backtrace_symbols
- _gAVActivityProgressClientTrace
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
- _gAVPlayerCaptionLayer
- _gAVPlayerItemLegibleOutputTrace
- _gAVPlayerItemMediaDataCollectorTrace
- _gAVPlayerItemMetadataCollector
- _gAVPlayerItemMetadataOutputTrace
- _gAVPlayerItemOutputTrace
- _gAVPlayerItemRenderedLegibleOutputTrace
- _gAVPlayerItemSampleBufferOutputTrace
- _gAVPlayerLooperTrace
- _gAVPlayerOutputTrace
- _gAVSampleBufferDisplayLayerTrace
- _gAVSampleBufferGeneratorTrace
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
- _objc_msgSend$copyAssetWithAdditionalTrackID:mediaType:
- _objc_msgSend$externalContentProtectionStatus
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$setBorderColor:
- _objc_msgSend$setBorderWidth:
- _objc_msgSend$subarrayWithRange:
- _plannerRTCKeys
- _setBounds:.oldRect
- _stringWithValidatedFormat
- _stringWithValidatedFormatArg2
- _stringWithValidatedFormatString
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "addSampleBufferDisplayLayer failed to set content layer"
+ "availableMediaCharacteristicsWithAuthoredMediaSelectionOptions"
+ "avplayer_fpNotificationCallback_block_invoke_11"
+ "com.apple.itunesstored"
+ "init"
+ "transportStreamPID"
- "\n\t\"%@\""
- " "
- "%02x"
- "%c"
- "%d bytes [ %@ ] [ %@ ]"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "(OSStatus)error.code"
- "*** SHOULD NOT receive kFigAssetNotification_PropertyRevised / kFigStdAssetProperty_Duration notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigAssetTrackProperty_EditSegmentData notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "*** SHOULD NOT receive kFigAssetTrackNotification_PropertyRevised / kFigStdTrackProperty_TimeRange notification from %s, if you see this message please file a radar with logs and repro steps and assign it to AVFoundation ***"
- "+[AVAnnotationRepresentation _annotationRepresentationWithPropertyList:binaryData:]"
- "+[AVAssetTrackInspector assetTrackInspectorWithAsset:trackID:trackIndex:]"
- "+[AVAssetWriterWritingHelper finalStepWorkaroundOperationWithFigAssetWriter:]_block_invoke"
- "+[AVAssetWritingPlannerIncrementalState fromDictionary:error:]"
- "+[AVAssetWritingPlannerTrackSegmentState fromDictionary:mediaType:error:]"
- "+[AVAssetWritingPlannerTrackState fromDictionary:error:]"
- "+[AVCaptionRenderer(AVCaptionRenderer_CaptionPreview) captionPreviewForProfileID:extendedLanguageTag:renderSize:]"
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
- "-1"
- "-[AVAVAudioSettingsAudioOutputSettings getAudioStreamBasicDescription:forAudioFileTypeID:sourceFormatDescription:]"
- "-[AVActivityProgressClient activateConnection]"
- "-[AVActivityProgressClient activateConnection]_block_invoke_2"
- "-[AVActivityProgressClient cancelActivities:]"
- "-[AVActivityProgressClient endActivityForTaskID:]"
- "-[AVActivityProgressClient failActivityForTaskID:]"
- "-[AVActivityProgressClient init]"
- "-[AVActivityProgressClient postActivityEvent:forIdentifier:]"
- "-[AVActivityProgressClient startProgressActivity:taskID:bundleID:name:description:imageUTI:]"
- "-[AVActivityProgressClient updateActivityName:description:forTaskID:]"
- "-[AVActivityProgressClient updateProgress:forTaskID:]"
- "-[AVAnnotation getJSONData:representationBinaryDataBindings:]"
- "-[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:]"
- "-[AVApplicationStateMonitor _didEnterBackground:]"
- "-[AVApplicationStateMonitor _willEnterForeground:]"
- "-[AVApplicationStateMonitor init]"
- "-[AVAsset mediaSelectionGroupForPropertyList:mediaSelectionOption:]"
- "-[AVAsset(AVAssetChapterInspection) _chapterMetadataGroupsBestMatchingPreferredLanguages:containingItemsWithCommonKeys:]"
- "-[AVAssetCustomURLBridgeForNSURLProtocol _cancelPendingRequests]"
- "-[AVAssetDownloadCache variantsForMediaSelection:]"
- "-[AVAssetDownloadContentConfiguration _createFigContentConfigForEnvironmentalCondition:]"
- "-[AVAssetDownloadLiveActivity _firePendingFinalizeForBundleID:]"
- "-[AVAssetDownloadLiveActivity _initInternal]"
- "-[AVAssetDownloadLiveActivity _isBundleIDBlocked:]"
- "-[AVAssetDownloadLiveActivity _loadConfiguration]"
- "-[AVAssetDownloadLiveActivity _unsafeRouteTerminalForClientState:]"
- "-[AVAssetDownloadLiveActivity _unsafeUpdateActivityTitleAndSubtitleForClientState:]"
- "-[AVAssetDownloadLiveActivity _unsafeUpdateProgressForClientState:]"
- "-[AVAssetDownloadLiveActivity _waitForConfig]"
- "-[AVAssetDownloadLiveActivity notifyProgress:]"
- "-[AVAssetDownloadSession _registerWithLiveActivityManager]"
- "-[AVAssetDownloadSession _stopUnderlyingDownload]_block_invoke"
- "-[AVAssetDownloadSession cancelFromLiveActivity]"
- "-[AVAssetDownloadSession initWithAsset:mediaSelections:destinationURL:options:]"
- "-[AVAssetDownloadSession initWithDownloadToken:]"
- "-[AVAssetDownloadSession initWithURL:destinationURL:options:]"
- "-[AVAssetDownloadSession pause]_block_invoke"
- "-[AVAssetDownloadSession start]"
- "-[AVAssetDownloadSession stop]"
- "-[AVAssetDownloadSession stop]_block_invoke"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCacheOnDispatchQueue]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _primeCache]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _readyForInspection]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:options:]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setupFigClientObjectAsync:]_block_invoke_2"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueueFirstTime]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueue]"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke"
- "-[AVAssetDownloadSession(AVAssetDownloadSession_Local) _transitionToTerminalStatus:error:]_block_invoke_2"
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
- "-[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:]"
- "-[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:]"
- "-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]"
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
- "-[AVAssetWriterHelper isProVideoStorageSupported]"
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
- "-[AVAssetWriterInputWritingHelper _checkIfClientSetProResRAWRequiredMetadataReturningError:]"
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
- "-[AVAssetWritingPlanner buildAssemblyComposition:]"
- "-[AVAssetWritingPlanner buildAssemblyComposition:]_block_invoke"
- "-[AVAssetWritingPlanner makeIncrementalStateByResumptionOrStartFresh:]"
- "-[AVAssetWritingPlanner saveIncrementalState:]"
- "-[AVAssetWritingPlannerIncrementalState resumableBy:]"
- "-[AVAssetWritingPlannerTrackSegmentState resumableBy:]"
- "-[AVAssetWritingPlannerTrackState resumableBy:]"
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
- "-[AVCurrentMediaSelectionCache clientSelectedOrEmptyMediaSelection]"
- "-[AVCurrentMediaSelectionCache updateCurrentMediaSelection:]"
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
- "-[AVMetadataItem(AVMetadataItemTypeCoercion) dataValue]"
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
- "-[AVPlannedVideoSegmentWritingRequest createResumableCompressionSessionWithAllocator:width:height:codecType:encoderSpecification:sourceImageBufferAttributes:compressedDataAllocator:outputCallback:outputCallbackRefCon:returningError:]"
- "-[AVPlaybackCoordinationMedium _removeUnusedTransportControlStates]_block_invoke"
- "-[AVPlaybackCoordinationMedium _updateLowestInUseDefaultItemIdentifier]_block_invoke"
- "-[AVPlaybackCoordinationMedium _updateMixedAssetTypesStatus]"
- "-[AVPlaybackCoordinationMedium _updateMixedAssetTypesStatus]_block_invoke_2"
- "-[AVPlaybackCoordinationMedium areAllCoordinatorsSuspendedForReason:]"
- "-[AVPlaybackCoordinationMedium connectPlaybackCoordinator:]"
- "-[AVPlaybackCoordinationMedium disconnectPlaybackCoordinatorWithIdentifier:]"
- "-[AVPlaybackCoordinationMedium endSuspensionOnAllCoordinatorsWithReason:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]"
- "-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]_block_invoke"
- "-[AVPlayer _addLayer:]"
- "-[AVPlayer _addLayer:]_block_invoke"
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
- "-[AVPlayer _removeAllItemsFromFigPlayer:]"
- "-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke_3"
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
- "-[AVPlayer(AVPlayerAudioSessionParticipant) setDisconnectedFromSystemAudio:completionHandler:]_block_invoke"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]_block_invoke"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _hasCurrentInterstitialEvent]"
- "-[AVPlayer(AVPlayerInterstitialSupport_Internal) _linkAndSyncAudioSessionWithInterstitialPlayer:]"
- "-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]"
- "-[AVPlayer(AVPlayerLegibleFallback) endUserTurnedOffSubtitles]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _acquireBackgroundAssertion]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _applicationHasExternallyDisplayedAVPlayerLayerAndIsUnderDeviceLock]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _canContinuePlaybackInBackgrounBasedOnAudiovisualBackgroundPlaybackPolicy:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:pauseAllowed:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:pauseAllowed:]_block_invoke_2"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:pauseAllowed:]_block_invoke_3"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:withCompletionHandler:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoDestinationsAreAttached]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _hasAssociatedAVPlayerLayerInPIPMode]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _invalidateBackgroundAssertionOnQueue]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _itemOkayToPlayWhileTransitioningToBackground:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _layerForegroundStateChanged:]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _shouldDetachVideoLayersFromFigPlayer]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _willEnterForeground:]"
- "-[AVPlayer(AVPlayerPIPSupport) setBackgroundPIPAuthorizationToken:]"
- "-[AVPlayer(AVPlayerSpeedRamp) canPlaySpeedRamp]"
- "-[AVPlayer(AVPlayerSpeedRamp) setSupportsSpeedRamps:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _resumePlayback:error:]"
- "-[AVPlayer(AVPlayerSupportForMediaPlayer) _updateConnectionToSecondScreen]"
- "-[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]_block_invoke"
- "-[AVPlayer(AVPlayerVideoDisplaySleepPrevention) setPreventsDisplaySleepDuringVideoPlayback:]"
- "-[AVPlayer(FigVideoTargetSupport) _interstitialVideoDestinationForPrimary:]"
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
- "-[AVPlayerCaptionLayer setCaptionPreviewProfileID:position:text:]_block_invoke"
- "-[AVPlayerCaptionLayer setPlayer:]"
- "-[AVPlayerCaptionLayer setValue:forKeyPath:]"
- "-[AVPlayerCaptionLayer stopShowingCaptionPreview]"
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
- "-[AVPlayerItem _informObserversAboutAvailabilityOfCurrentMediaSelection]"
- "-[AVPlayerItem _invokeReadyForEnqueueingHandlers]"
- "-[AVPlayerItem _makeReadyForEnqueueingWithCompletionHandler:]"
- "-[AVPlayerItem _postSeekCompletionNotificationWithSeekID:andResult:]"
- "-[AVPlayerItem _presentationSize]"
- "-[AVPlayerItem _seekToTime:toleranceBefore:toleranceAfter:seekID:options:completionHandler:]"
- "-[AVPlayerItem _selectMediaOption:inMediaSelectionGroup:]"
- "-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]"
- "-[AVPlayerItem _setAudioProcessingEffectsAccordingToInputParameters:forTrackID:]"
- "-[AVPlayerItem _setCurrentMediaSelection:]"
- "-[AVPlayerItem _setItemAudioTapProcessor:fromAudioMixContext:]"
- "-[AVPlayerItem _setVideoCompositionInstructions:]"
- "-[AVPlayerItem _tracks]"
- "-[AVPlayerItem _unregisterInvokeAndReleasePendingSeekCompletionHandlerForSeekID:finished:]"
- "-[AVPlayerItem _updateAssetParsedTimeRange:]"
- "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]"
- "-[AVPlayerItem _updateCanPlayAndCanStepPropertiesWhenReadyToPlayWithNotificationPayload:updateStatusToReadyToPlay:]_block_invoke"
- "-[AVPlayerItem _updateCoordinationOffsetOnQueueForCoordinator:playbackItem:]"
- "-[AVPlayerItem _updateInterstitialTimeRangesOnQueueForCoordinator:playbackItem:]"
- "-[AVPlayerItem _updateTimebase]_block_invoke_2"
- "-[AVPlayerItem currentMediaSelection]"
- "-[AVPlayerItem seekToDate:completionHandler:]"
- "-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]_block_invoke"
- "-[AVPlayerItem selectedMediaOptionInMediaSelectionGroup:]"
- "-[AVPlayerItem setAdvanceTimeForOverlappedPlayback:]"
- "-[AVPlayerItem(AVPlayerItemOutputs) _evaluateMetadataOutputs]_block_invoke"
- "-[AVPlayerItem(AVPlayerItemTrackInfoCaching) _cacheTrackInformation]"
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
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemDidBecomeAvailable:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderDidBecomeAvailableForItem:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderResetOutput:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderResetOutput:]_block_invoke_2"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:]_block_invoke_2"
- "-[AVPlayerItemSampleBufferOutput _notifyOutputMediaDataAvailableForTrackID:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput _setFigPlaybackItem:]"
- "-[AVPlayerItemSampleBufferOutput copyNextSampleBufferForTrackID:flags:]"
- "-[AVPlayerItemSampleBufferOutput copyNextSampleBufferWithFlags:]_block_invoke"
- "-[AVPlayerItemSampleBufferOutput requestMediaDataForTimeRange:]_block_invoke"
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
- "-[AVPlayerLayer _applyPresentationSizeChange:andForceUpdate:]"
- "-[AVPlayerLayer _applyPresentationSizeChange:andForceUpdate:]_block_invoke"
- "-[AVPlayerLayer _currentWindowSceneIsForegroundDefault]"
- "-[AVPlayerLayer _currentWindowSceneIsForeground]"
- "-[AVPlayerLayer _displaySize_invokeOnMainQueue]"
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
- "-[AVPlayerLayer _percentCoverageRelativeToRootLayer_invokeOnMainQueue]"
- "-[AVPlayerLayer _presentationSize]"
- "-[AVPlayerLayer _restoreClientLayers:intoMaskLayer:]"
- "-[AVPlayerLayer _setIsPartOfForegroundScene:]_block_invoke"
- "-[AVPlayerLayer _setPlayer:forPIP:]"
- "-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke"
- "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]"
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
- "-[AVPlayerLayer setCaptionPreviewProfileID:position:text:]_block_invoke"
- "-[AVPlayerLayer setForScrubbingOnly:]"
- "-[AVPlayerLayer setLanczosFilterDownscaleFactor:]"
- "-[AVPlayerLayer setLegibleContentInsets:]"
- "-[AVPlayerLayer setSublayers:]"
- "-[AVPlayerLayer stopShowingCaptionPreview]"
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
- "-[AVPlayerPlaybackCoordinator _endSuspension:]"
- "-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:]_block_invoke_2"
- "-[AVPlayerPlaybackCoordinator _endSuspensionWithReason:]"
- "-[AVPlayerPlaybackCoordinator _hasRemovedSuspensionReason:currentReasons:newReasons:]"
- "-[AVPlayerPlaybackCoordinator _reactToNewDelegate]"
- "-[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectationsForIdentifier:]"
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
- "-[AVPlayerPlaybackCoordinator coordinationOffsetForPlayerItem:]"
- "-[AVPlayerPlaybackCoordinator handleNewParticipantStateDictionary:]"
- "-[AVPlayerPlaybackCoordinator handleNewTransportControlStateDictionary:]"
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
- "-[AVQueuePlayer(AVPlayerItemPreBuffering) setItemsToPrebuffer:]"
- "-[AVResourceReclamationAssertion dealloc]"
- "-[AVResourceReclamationAssertion initWithDetails:]"
- "-[AVResourceReclamationController(AVResourceReclamation) permitReclamationWhileSuspended]"
- "-[AVResourceReclamationEvent dealloc]"
- "-[AVResourceReclamationEventObserverToken dealloc]"
- "-[AVResourceReclamationEventObserverToken initWithDetails:]"
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
- "-[AVSampleBufferAudioRenderer setRenderSynchronizer:error:]"
- "-[AVSampleBufferAudioRenderer setSTSLabel:]"
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
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _addRenderer:error:]_block_invoke_3"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _createOnceTimebaseObserverForRemovalOfRenderer:atTime:]_block_invoke"
- "-[AVSampleBufferRenderSynchronizer(AVSampleBufferRenderSynchronizerRendererManagement) _scheduleTimedRendererRemovalAtTime:atTime:withClientCompletionHandler:]"
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
- "-[AVSampleBufferVideoRenderer _setOutputObscuredDueToInsufficientExternalProtection:]"
- "-[AVSampleBufferVideoRenderer _setUpFigVideoQueueControlTimebase:]_block_invoke"
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
- "-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:]_block_invoke_2"
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
- "-[AVSystemMuteObserver _evaluateOnSerialQueue]"
- "-[AVSystemMuteObserver _refreshCachedCaptionsOnMutePreferenceEnabled]"
- "-[AVSystemMuteObserver _startObservingAccessibility]"
- "-[AVSystemMuteObserver _startObservingAccessibility]_block_invoke"
- "-[AVSystemMuteObserver _startObservingOnIPhoneFamily]"
- "-[AVSystemMuteObserver _startObservingOnIPhoneFamily]_block_invoke"
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
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: %@ Setting IsExpanseMediaSession %s on AVAudioSession error %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
- "<<<< AVActivityProgressClient >>>> %s: ActivityProgressUI connection invalidated"
- "<<<< AVActivityProgressClient >>>> %s: BoardServices framework not available"
- "<<<< AVActivityProgressClient >>>> %s: Dropping endActivityForTaskID %s — ActivityProgressUI server unavailable; activity may remain on screen"
- "<<<< AVActivityProgressClient >>>> %s: Dropping handleActivityEvent (event=%ld) for taskID %s — ActivityProgressUI server unavailable"
- "<<<< AVActivityProgressClient >>>> %s: Dropping startProgressActivity for taskID %s bundleID '%s' — ActivityProgressUI server unavailable"
- "<<<< AVActivityProgressClient >>>> %s: Dropping updateActivityName for taskID %s — ActivityProgressUI server unavailable"
- "<<<< AVActivityProgressClient >>>> %s: Dropping updateProgress for taskID %s — ActivityProgressUI server unavailable"
- "<<<< AVActivityProgressClient >>>> %s: Ended activity %@"
- "<<<< AVActivityProgressClient >>>> %s: Failed to create BSServiceConnection to ActivityProgressUI"
- "<<<< AVActivityProgressClient >>>> %s: Failed to create RBSDomainAttribute for BasicAngelIPC"
- "<<<< AVActivityProgressClient >>>> %s: Failed to get remote target for ActivityProgressUI service"
- "<<<< AVActivityProgressClient >>>> %s: Marking activity %@ as failed"
- "<<<< AVActivityProgressClient >>>> %s: Received cancellation request for %lu activities"
- "<<<< AVActivityProgressClient >>>> %s: Remote target does not conform to APKActivityProgressUIServer protocol"
- "<<<< AVActivityProgressClient >>>> %s: Started activity %@ for bundle '%@' with name '%@'"
- "<<<< AVActivityProgressClient >>>> %s: Successfully established connection to ActivityProgressUI service"
- "<<<< AVActivityProgressClient >>>> %s: Updated activity name for %@: '%@'"
- "<<<< AVActivityProgressClient >>>> %s: Updated progress for activity %@: %lld/%lld"
- "<<<< AVAnnotation >>>> %s: Annotation failed to create formatted date from %@."
- "<<<< AVAnnotation >>>> %s: Failed to create AVAnnotation: %@"
- "<<<< AVAnnotation >>>> %s: Unknown annotation representation type: %@"
- "<<<< AVAnnotation >>>> %s: Unknown annotation representation version %@."
- "<<<< AVAnnotation >>>> %s: Unknown annotation version %@."
- "<<<< AVApplicationStateMonitor >>>> %s: <%@>. isRunning %d, hasForegroundVisibility %d appIsInForeground %d, processIsViewService %d"
- "<<<< AVApplicationStateMonitor >>>> %s: called"
- "<<<< AVAsset >>>> %s: *** MediaValidator.plist was not loaded for this platform! Defaulting to no video support. ***"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> %s"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> *** Could not canonicalize language: %@. ***"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> Cannot create AVAssetDownloadCache when an AVManagedAssetCache is already present."
- "<<<< AVAsset >>>> %s: <%{public}@|%p> Created"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> FigAssetCopyAssetWithDownloadToken for downloadToken %llu returned %d"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> Received notification for %@"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> _URLAsset->resourceLoader was unexpectedly non-nil"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> called for property list %@, mediaSelectionOptionOut = <%p>"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> creating AVAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> creating AVFigAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> failed to create AVFigAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> received ServerStatePurged with identifier 0x%llx"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> resolved to group %@ and option %@"
- "<<<< AVAsset >>>> %s: <%{public}@|%p> using custom AVAssetInspectorLoader"
- "<<<< AVAsset >>>> %s: AVURLAssetHTTPHeaderFieldsKey must be a dictionary"
- "<<<< AVAsset >>>> %s: asset created with AVAssetPrefersSandboxedParsingOptionKey"
- "<<<< AVAsset >>>> %s: asset created with AVAssetRequiresInProcessOperationKey"
- "<<<< AVAssetCache >>>> %s: %p cannot create AVAssetVariant for %@"
- "<<<< AVAssetCache >>>> %s: Enabling AutomaticCacheSizeManagement"
- "<<<< AVAssetCache >>>> %s: Initialized with URL %@"
- "<<<< AVAssetCache >>>> %s: Remove entry with key = %@"
- "<<<< AVAssetCache >>>> %s: Set maxEntrySize = %lld"
- "<<<< AVAssetCache >>>> %s: Set maxSize = %lld"
- "<<<< AVAssetCustomURL >>>> %s: cancelling abandoned AVNSURLProtocolRequest %p"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: AVActivityProgressClient not available - Live Activity support disabled"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Bundle identifier '%@' is blocked from Live Activity"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Cancelling %lu download sessions for activity %@"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Cooldown elapsed for '%@' (cooldownMS=%lld); ending activity silently"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Creating new client state and activity for '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Download %@ already registered for client %@"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Download %@ not found in activeDownloads for client %@"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Ending activity %@ for '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Failed to generate activity ID for bundle '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: FigAssetDownloaderCopyLiveActivityConfiguration failed (err=%d); using default cooldownMS=%lld"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Found existing client state for '%@', adding to existing activity"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Handling activity cancellation for %lu activities"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Holding activity for '%@' at 100%% for %lld ms before ending (%ld completed, %ld failed, %ld will-retry)"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Live Activity configuration loaded: cooldownMS=%lld"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: No bundle identifier for session %p"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: No bundle identifier for session %p during unregister"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: No client state found for bundleID '%@' during unregister"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Starting new activity with ID %@ for bundle '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Still %lu active downloads for '%@', updating progress"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Terminal completion for '%@' (%ld completed, %ld failed, %ld will-retry); ending"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Terminal for '%@' with no tracked items; dismissing"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Timed out waiting for Live Activity configuration; proceeding with defaults"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Unreachable: progress update called with empty client state for '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Updated progress for '%@': %lld/%lld (%ld active, %ld completed, %ld failed, %ld will-retry)"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: Updated title/subtitle for '%@': '%@' / '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Progress update: %lld/%lld for bundle '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Registration complete for bundle '%@'"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping Live Activity registration because bundle '%@' is disabled"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping Live Activity registration for client %@ \t\tbecause Live Activity is disabled for this download"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping progress update - Live Activity not enabled"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping progress update - download is discretionary"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping unregister - Live Activity not enabled"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Skipping unregister - download is discretionary"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: [%p] Unregistering download for bundle '%@' (terminalStatus=%ld, willRetry=%d, error=%@ [%ld])"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: invalid state (clientState=%p activityProgress=%p)"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: registerDownload called with nil session"
- "<<<< AVAssetDownloadLiveActivity >>>> %s: unregisterDownload called with nil session"
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
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Re-registering Live Activity (resumed)"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Registering download with Live Activity manager"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Start download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Stop download"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Unregistering Live Activity (paused)"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Unregistering download from Live Activity manager (client cancelled)"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] Unregistering download from Live Activity manager (terminalStatus=%ld, error=%@ [%ld])"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] called with notification name %@ payload %@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] cancelling download from Live Activity"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] loaded assetType:[%s] loadingStatus:%d error:%@"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] stopping FigAssetDownloader"
- "<<<< AVAssetDownloadSession >>>> %s: [%p] stopping FigPlaybackItem download"
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
- "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported by system"
- "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported when output file is on external storage"
- "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported without output URL"
- "<<<< AVAssetWriter >>>> %s: returning YES"
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
- "<<<< AVAssetWriterInput >>>> %s: The required metadata for ProResRAW movie are not set. Missing movie level metadata keys {%@}."
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
- "<<<< AVAssetWritingPlanner >>>> %s: Cannot resume from savedSegmentState for segment at index %ld"
- "<<<< AVAssetWritingPlanner >>>> %s: Cannot resume from savedTrackState for assembly track ID %d"
- "<<<< AVAssetWritingPlanner >>>> %s: Failed to construct assemblyComposition"
- "<<<< AVAssetWritingPlanner >>>> %s: Failed to delete segment file at %@: %@"
- "<<<< AVAssetWritingPlanner >>>> %s: Failed to load track from track segment output URL"
- "<<<< AVAssetWritingPlanner >>>> %s: Found multiple %@ tracks in client written segment file %@. Expect one and only one track"
- "<<<< AVAssetWritingPlanner >>>> %s: Track count from savedState (%d) does not match current session track count (%d)"
- "<<<< AVAssetWritingPlanner >>>> %s: _requiresCompression (%d) from savedState does not match _requiresCompression (%d) from current state"
- "<<<< AVAssetWritingPlanner >>>> %s: mediaType %@ from savedState does not match current mediaType %@"
- "<<<< AVAssetWritingPlanner >>>> %s: restored state = %@"
- "<<<< AVAssetWritingPlanner >>>> %s: restored state file = %@"
- "<<<< AVAssetWritingPlanner >>>> %s: saved state = %@"
- "<<<< AVAssetWritingPlanner >>>> %s: saved state file = %@"
- "<<<< AVAssetWritingPlanner >>>> %s: segment count (%ld) from savedState does not match segment count (%ld) in current state"
- "<<<< AVAssetWritingPlanner >>>> %s: segment frameCount from saved state (%ld) does not match current segment's frameCount (%ld)"
- "<<<< AVAssetWritingPlanner >>>> %s: segment mediaType from saved state (%@) does not match current segment's mediaType (%@)"
- "<<<< AVAssetWritingPlanner >>>> %s: segment requiresCompression from saved state (%d) does not match current segment's requiresCompression (%d)"
- "<<<< AVAssetWritingPlanner >>>> %s: segment time range from saved state (start = %1.3f, duration = %1.3f) does not match current segment time range (start = %1.3f, duration = %1.3f"
- "<<<< AVAssetWritingPlanner >>>> %s: segmentFileTimeRange %1.3f - %1.3f --> outputTrackTime %1.3f"
- "<<<< AVAssetWritingPlanner >>>> %s: segmentURL from savedState (%@) does not match current segment URL (%@)"
- "<<<< AVAssetWritingPlanner >>>> %s: temporary file URL = %@"
- "<<<< AVAssetWritingPlanner >>>> %s: trackID (%d) from savedState does not match current trackID (%d)"
- "<<<< AVAssetWritingPlanner >>>> %s: trackPlanExecutor %@"
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
- "<<<< AVCaptionRenderer >>>> %s: FigCoreTextSubtitleRendererCreate failed with error %d"
- "<<<< AVCaptionRenderer >>>> %s: FigSubtitleRendererCreateAttributedStringForCaptionPreview failed with error %d"
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
- "<<<< AVFileSystemUtilities >>>> %s: Called by client that is not an app"
- "<<<< AVFileSystemUtilities >>>> %s: Error getting resource value: %@"
- "<<<< AVFileSystemUtilities >>>> %s: Failed to remove temporary file at %@: %@"
- "<<<< AVFileSystemUtilities >>>> %s: No container found: %s"
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
- "<<<< AVMetadataItem >>>> %s: AVMetadataItem dataValue: dropping malformed NSData %p (length=%lu, bytes=NULL)"
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
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ %s HLS and file-based assets"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ all playback coordinators %s suspended for reason %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ asset %@ streaming status not yet loaded, deferring mixed asset type check"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ connect playback coordinator %@ to coordination medium"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ current transport control state dictionary %@ for item identifier %@ for coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ disconnect playback coordinator with identifier %@ from coordination medium"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ ending suspensions with reason %@ on all playback coordinators"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has different sync ID %@. should not update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has equal lamport timestamp %@ from originator with larger UUID. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has higher lamport timestamp %@. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ new transport control state has lower lamport timestamp %@. should NOT update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ no existing transport control state. should update"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ not updating participants with %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ reloading transport control state dictionary %{public}@ for item identifier %@ for coordinator %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ removing unused item identifier %@ from transport control states"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ setting coordinator %@, participant %@ as initiator for identifer %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ signalling condition for item identifier %@"
- "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ updating lowest in-use item identifier to %d"
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
- "<<<< AVPlaybackCoordinator >>>> %s: %@ beginning suspension with reason %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ caching group timeline reset"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ coordinationOffset %f is non-numeric. setting to 0"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ coordinator is suspended. Not resetting"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ current pending seek id %d, seek time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension %p proposing new time %f"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ ending suspension with reason %@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ handling new participant state %{public}@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ handling new transport control state %{public}@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ integrated timeline is nil. Bypassing integrated seek to %f"
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
- "<<<< AVPlaybackCoordinator >>>> %s: %@ updating with participant state %{public}@"
- "<<<< AVPlaybackCoordinator >>>> %s: %@ updating with transport control state %{public}@"
- "<<<< AVPlaybackCoordinator >>>> %s: <AVPlaybackCoordinator: %@> failed to dispatch work async onto player queue with err: %d, synchronizing locally"
- "<<<< AVPlaybackCoordinator >>>> %s: Could not create FigTimelineCoordinatorSuspensionRef"
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator gave a participantID which is not present in otherParticipants"
- "<<<< AVPlaybackCoordinator >>>> %s: States aren't distinguishable. Assuming state from the outside is better."
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for DidIssueCommandToFigPlayer notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "<<<< AVPlaybackCoordinator >>>> %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "<<<< AVPlayer >>>> %s: %@ called. oldReason %@ newReason %@ for timeControlStatus %d to %d"
- "<<<< AVPlayer >>>> %s: %@ inferred time control status: %d (waiting reason: %@)"
- "<<<< AVPlayer >>>> %s: %@ kFigPlayerProperty_PlaybackState is %@"
- "<<<< AVPlayer >>>> %s: %@ setting rate to %f"
- "<<<< AVPlayer >>>> %s: (%p) nil primaryVideoDestination"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> %s"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> (layer = %p)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayer has no layers or no figPlayer. Nothing to attach/detach for iapd"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayer iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer do hold. Attaching."
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayer iapd extended mode has changed. Conditions to maintain videoLayer->figPlayer don't hold. Detaching."
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayer setShouldWaitForVideoTarget to %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayerLayer(%p) and its closedCaptionLayer(%p)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> AVPlayerLayer(%p) is adding videoLayer(%p), closedCaptionLayer(%p), and subtitleLayer(%p) sublayers"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Adding coordinated playback suspension with reason %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Beginning committing plan from outgoing item %@ to incoming item %@ (advanceTimeForOverlappedPlayback %1.3f)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Cannot add NULL videoTarget"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Completed committing plan from outgoing item %@ to incoming item %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Did update status to %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Directly set kFigPlayerProperty_ShouldWaitForVideoTarget on FigPlayer"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Dispatching FigPlayer configuration block to state dispatch queue"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Dispatching FigPlayer copy property block to a background queue if necessary"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Error inserting item: %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Error replacing current item: %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Extended mode is active"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Failed adding playback item of %@ to play queue immediately, will remove item"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Failed to remove all items from fig player, err %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Found non-LCD CAContext so externally displayed"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Handling removal of item %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Host application is in foreground with foreground video output"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as an associated AVPlayerLayer is in PIP mode"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ CarPlay is active ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ IAP extended mode is active ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ MMP SPI says so ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ No associated video layers ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ No enabled video ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ Under device lock and playing to external display ]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background reason: [ policy set to %d ] "
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %@> can continue to play as the application transitions to background: %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %p> Pausing since cannot transition to background"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%@ %p> Unable to evaluate if okay to play while transition to background. Will reevaluate when ReadyToPlay"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%p> Now ReadyToPlay. Reevaluating if okay to play while transition to background."
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Item <%p> Reevaluation complete. Not okay to play while transition to background. Pausing."
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> NO since Buffered AirPlay is active and it does not support speed ramps"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> NO since supportsSpeedRamps is NO"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> New current item: %@ %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> No figPlayer found, cannot set picker id"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Not suspended under lock"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Obtaining volume for category [%@]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> PIP mode is active"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Pausing item since cannot transition to background _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Player audiovisual background policy set to Automatic, use coordinator other participant count %d, connected to local medium %d to decide"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Player audiovisual background policy set to ContinuesIfPossible"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Player audiovisual background policy set to Pauses"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Player role %@ set synchronously before we had a fig player."
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerAudiovisualBackgroundPlaybackPolicyDidChangeNotification for policy change"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerBackgroundPIPAuthorizationTokenDidChangeNotification for token change"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerCurrentItemDidChangeNotification with reason %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerInterstitialPlayerDidChangeNotification"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerPlaybackWasInterruptedNotification"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerRateDidChangeNotification for status change"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting AVPlayerRateDidChangeNotification with payload %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Posting _AVPlayer_VolumeDidChangeNotification with payload %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> RBS unavailable, unable to take background assertion"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Removing coordinated playback suspension with reason %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Returning hasAVPlayerLayerInPIPMode: %s"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Set ShouldWaitForVideoTarget as creation option or right after creation of player"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Setting attributes on decoder to:\n\t<%@>"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Should Detach: [%@]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Trying to set picker id : %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Unable to read reconciled version of IsBufferedAirPlayActive, err %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Under device lock and has external display active"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Unrecognized player role %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> Will update status"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> YES"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> _setUsesLegacyAutomaticWaitingBehavior: %s"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> attach video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> attaching videoDestinations (%@) for presentationStateChange: %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called (current item being set = %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called (inNotificationName = %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called (inNotificationName = %@, inNotificationPayload = %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called (notification = %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called (time observer = <%p>)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called. Rate changed from [%f] -> [%f], changed because %s\n%@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called. Set rate to 1.0 because %s\n%@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> called. set to [%f]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> cannot copy displayed pixel buffer, figPlayer is NULL"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> cleared muteOverrideSuppressedUntilUnmute on unmute"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> closedCaptionLayers array snapshot:%@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> connect fig playback coordinator"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> current interstitial event (cached): %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> detached video targets and layers from FigPlayer"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> dispatched (inNotificationName = %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> dispatching"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> dispatching call to -_applyPlayQueueChangesToFigPlayerWithCompletionHandler"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> effectivelyMuted=%d playerMuted=%d captionsOnMuteEnabled=%d muteOverrideSuppressed=%d effectiveOverride=%ld"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> endUserTurnedOffSubtitles; suppressing mute override until next mute"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> expected 'CurrentIsBufferedAirPlayActive' in notification payload"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> failed to copy currently displayed pixel buffer although no error"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> failed to take background assertion with err %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> fig playback coordinator already connected clientRequested"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> figplayer creation failed [%d]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> got background assertion"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> has foreground layers, attaching video objects"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> has no more foreground video objects left, detaching video layers"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> interstitial is active %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> invalidating existing background assertion"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> isConnectedToPhysicalSecondScreen changed %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> isExternalPlaybackActive is YES"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> issue _reevaluateVideoLayersAndTargetsForPresentationState w/ DetachAllOutputs _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d, _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> kFigPlayerNotification_CurrentItemDidChange (FigPlaybackItem = %p)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> kFigPlayerNotification_MutedDidChange (value [%d])"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> kFigPlayerNotification_ParticipatesInAudioSessionDidChange (FigPlayer participates [%d], disconnected [%d])"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> maximumLayerDisplaySize = %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> nil videoLayer for playerLayer %p, cannot update pixel buffer attributes"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> not updating video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> not updating video layers, despite adding layer %p"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> now have %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> player failed to create fig sub item (error: %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> received %@ (payload: %@)"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> received ServerStatePurged with identifier 0x%llx"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> received updated %@. Rate changed from [%f] -> [%f], changed because %s\n%@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> reconciling IsBufferedAirPlayActive across the read/subscribe window: latest=%d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> releasing background assertion after finishing suspension"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> removed %@ %@, now have %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> removed %@ %@, now have @[]"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> removed current item, now have %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> replaced local interstitialEventCoordinator %p with remote %p"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> sawFileType = %d, sawStreamingType = %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> scheduling _didFinishSuspension block"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> seekToDate called without any attached item"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> seekToTime called without any attached item"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setDisconnectedFromSystemAudio: FigPlayerSetProperty failed with error %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setExpectedAssetTypes %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setting from %d to %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setting preventsDisplaySleepDuringVideoPlayback=%s"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setting to %@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setting to %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> setting up FigPlayer <%p>"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> skip _reevaluateVideoLayersAndTargetsForPresentationState  _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> skip attach video layers _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> skipping _didFinishSuspension, invalidating assertion immediately"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> synthesizing _didFinishSuspension notification"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> underlying FigPlayer did neither implement SetRateWithOptions nor SetRateWithFade. Fall back to SetRate"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> underlying FigPlayer did not implement SetRateWithOptions. Fall back to SetRateWithFade"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> updating video layers due to adding layer %p"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> video layers are still attached"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> videoLayers array snapshot:%@"
- "<<<< AVPlayer >>>> %s: <%{public}@|%p> w/ DetachLayersKeepingVideoTargetsAttached _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerAvailableHDRModesDidChangeNotification"
- "<<<< AVPlayer >>>> %s: Posting AVPlayerEligibleForHDRPlaybackDidChangeNotification"
- "<<<< AVPlayer >>>> %s: availableHDRModes returning %d"
- "<<<< AVPlayer >>>> %s: called (asset=%p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> %@ closed caption layer"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Did cancel all observation of old player"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> Observing isDisplayingClosedCaptions on player %p"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> setCaptionPreviewProfileID: subtitleLayer=%p subtitlePreviewLayer=%p closedCaptionLayer=%p"
- "<<<< AVPlayerCaptionLayer >>>> %s: <%p> stopShowingCaptionPreview: subtitleLayer=%p subtitlePreviewLayer=%p closedCaptionLayer=%p"
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
- "<<<< AVPlayerItem >>>> %s: %@ unsupported for item with %ld tracks"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> %@ parsed time range changed start=%0.3f duration=%0.3f"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> <MTAudioProcessingTapRef %p> from %s"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> AVPlayerItem %p deallocated while a pending seek is still in progress; leaking completion handler. Use -cancelPendingSeeks to deallocate an AVPlayerItem safely while a seek operation is still pending."
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Adding playback item to play queue immediately (player = %@)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> AllowedSpatialization changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> CPEProtector already ready"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Calling FigPlayerAddToPlayQueue (previous item = %@ %@, FigPlaybackItem = %p)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Chosen tracks changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Copying completion handler for later invocation in response to readiness notifications"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> CurrentSelectedMediaArray not in payload or nil."
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Display non-forced subtitles changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Either everything necessary is already ready, or making it all ready has failed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> ExternalProtectionRequiredForPlayback changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItem <%p> became the FigPlayer's current item"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItem <%p> reached timeToPauseBuffering"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItem <%p> reached timeToPausePlayback"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItem <%p> stopped being the FigPlayer's current item"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItem <%p> was removed from the FigPlayer's item queue"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItemSeekToDate() failed for initial date"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItemSeekToDateWithID() failed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> FigPlaybackItemSetProperty() failed with %d for initial estimated date"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Ignore nil/empty audioProcessingEffects"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Invoking completion handler for cancelled seek %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Invoking seek completion handler for seek id %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> NewRecommendedTimeOffsetFromLive: %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Not calling FigPlayerAddToPlayQueue because item's status is the failure status (previous item = %@ %@, FigPlaybackItem = %p)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting %@ for seekID %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemDidPlayToEndTimeNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemFailedToPlayToEndTimeNotification with error %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemMediaSelectionDidChangeNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemNewAccessLogEntryNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemNewErrorLogEntryNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemPlaybackStalledNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemTimeJumpedNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemTimeJumpedNotification for seek with originator"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Posting AVPlayerItemTimebaseChangedNotification"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Requesting automatic loading of FigAsset properties %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Requesting automatic loading of FigAssetTrack properties %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> SLOW PATH - NO CACHE"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Seek to time %1.3f with tolerance <%1.3f, %1.3f>"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> SpatialAudioRenderingChange: %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> SpatialAudioRenderingChange: default, no payload"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> Using seek ID %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> advanceTime %.3f"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> already attached to a different player, new weak ref %p old weak ref %p"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> already attached to same player, new weak ref %p old weak ref %p"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> alternate stream changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> attaching player %p weak ref %p"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> avoided synchronous FigAsset/FigAssetTrack property fetch while formulating currentMediaSelection"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> basics already ready"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> called"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> called (option=%@, group=%@)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> coordinationIdentifier changed to %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> created with asset at URL [%@], automatically loaded asset keys %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> dimensions changed to %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> failed to become ready for %@ (error: %@)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> failed to create fig sub item (error: %@)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> fetching its dimensions"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> hasEnabledAudio changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> hasEnabledVideo changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> hasVideo changed to YES"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> initialSamples already ready"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> inspected %d, cached %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> invoke %d handlers"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> is fetching TrackIDArray"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> item selected media options changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> loaded ranges changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> playback buffer Full: NO"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> playback buffer empty: NO"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> playback stalled"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> ready for inspection of %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> ready for playback"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> received ServerStatePurged with identifier 0x%llx"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> reset cinematicAudioEffectParameters"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> reset sweepFilterConfiguration"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> seekable ranges changed"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> set can and step flags"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> set video composition properties: %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> setting coordination offset to %f"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> setting interstitial time ranges to %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> setting video composition instructions to %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> status changing to AVPlayerItemStatusFailed with error %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> status changing to AVPlayerItemStatusReadyToPlay"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> stream buffer empty: YES"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> stream buffer full: YES"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> stream likely to keep up: NO"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> stream likely to keep up: YES"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> track id %d, channel count %u, isDerivedFromMultiChannelAudioTrack %d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> track id %d, no channel count (formatDescription=%s)"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> tracks changed, %@, %@, %s"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> updateStatusToReadyToPlay:%d"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> updateStatusToReadyToPlay:%d complete"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> with asset <%p> called for media selection group %@"
- "<<<< AVPlayerItem >>>> %s: <%{public}@|%p> with asset <%p> called for media selection option %@ in group %@"
- "<<<< AVPlayerItem >>>> %s: Failed to allocate videoCompositionProperties"
- "<<<< AVPlayerItem >>>> %s: Failed to set kFigPlaybackItemProperty_MetadataOutputsDictionary"
- "<<<< AVPlayerItem >>>> %s: Neither applied nor cached media option. Selection will be discarded."
- "<<<< AVPlayerItem >>>> %s: Unknown AVAudioMixEffectParameters type."
- "<<<< AVPlayerItem >>>> %s: Video Enhancement mode is not valid"
- "<<<< AVPlayerItem >>>> %s: We have neither a FigAsset, URL, nor FigFormatReader, so cannot create a FigPlaybackItem"
- "<<<< AVPlayerItem >>>> %s: can't create looping timebase! item will not loop."
- "<<<< AVPlayerItemCurrentMediaSelectionCache >>>> %s: %@"
- "<<<< AVPlayerItemCurrentMediaSelectionCache >>>> %s: SLOW PATH - NO CACHE"
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
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s:  returning sbuf %p pts %1.3f numSamples %d flags %d"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p Called setFigPlaybackItem with item %@ current item %@,"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p applying pending time range request"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p received %@"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p received %@,"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p received %@, extractionID=%d"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p storing pending time range request"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: %p: wrong trackID %d (right trackID is %d)"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputMediaDataAvailable:trackID:"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Delegate does not implement -outputSequenceWasRestarted: or -outputSequenceWasFlushed:trackID:"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: FigPlaybackItemExtractAndRetainNextSampleBuffer returned %d, sampleBuffer=%p, self=%p"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: No delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Samples already available in the provider. Issuing callback."
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputMediaDataAvailable: to delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputMediaDataAvailable:trackID: to delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputSequenceWasFlushed:trackID: to delegate"
- "<<<< AVPlayerItemSampleBufferOutput >>>> %s: Sending -outputSequenceWasRestarted: to delegate"
- "<<<< AVPlayerItemTrack >>>> %s: attached output %@ with extractionID %d"
- "<<<< AVPlayerItemTrack >>>> %s: removed output %@"
- "<<<< AVPlayerLayer >>>> %s: <%p> setCaptionPreviewProfileID: subtitleLayer=%p subtitlePreviewLayer=%p maskLayer=%p"
- "<<<< AVPlayerLayer >>>> %s: <%p> stopShowingCaptionPreview: subtitleLayer=%p subtitlePreviewLayer=%p maskLayer=%p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ AVPlayerLayer's net flip status does match CoreAnimation default"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ AVPlayerLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ _updatePreferredDynamicRange(%@) withAnimation(%@)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ already in PIP mode but will use %p instead of %p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ became PIP'ed"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ closed caption layer"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ commence player <%p> observation"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ entering PIP mode using %p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ entering second screen mode using %p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ frame is { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ leaving PIP mode"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ leaving second screen mode"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ left PIP mode"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ left second screen mode"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ resign player <%p> observation over currentItem.presentationSize"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ setting self on player <%p>"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ showing interstitial layer [%@], call interstitialLayer copyDisplayedPixelBuffer"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ visibility became NO"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> %@ visibility became YES"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> (%p) either NULL player or videoLayer, returning CGSizeZero"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> (%p) presentationSize={ .width=%.3f, .height=%.3f }"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> AVPlayerLayer already connected to second screen"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> AVPlayerLayer underlying video layer changed.  Will update dynamic range"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Called (bounds=%@)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Called presentationSize={ .width = %.3f, .height = %.3f } forceUpdate: %s"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Cannot add sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Cannot insert sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Cannot replace sublayer while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Cannot set sublayers while PIP is active"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Did cancel all observation of old player"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Display Size is %f x %f scale is %f"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Error in traversing layer tree"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Hiding video layer since the presentation size for player %p is 0x0"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Hiding video layer since the presentation size is 0x0"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Not applying new value of AVPlayer.currentItem.nonForcedSubtitleDisplayEnabled for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Not applying new value of AVPlayer.isDisplayingClosedCaptions for player %p not currently being observed (expected %p)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Performance hud enabled (hud=%p)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Regardless of the state of PIP the layer is in, removeFromSuperLayer is always allowed"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Restoring client layer %@ with indexPath %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Scheduling interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d (delayed to %f, now %f)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Setting closed caption layer bounds to %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Setting legibleContentInsets received from client. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Setting readyForDisplay to NO due to detaching from player %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Unhiding video layer since the presentation size for player %p is { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Updated CC bounds with cached legibleContentInsets. left = %f, right = %f, top = %f, bottom = %f"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Using box filter downscale"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Window scene containing layer did enter background"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> Window scene containing layer will enter foreground"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called  IsReadyForDisplayDidChange videoLayer %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called (item=%p, videoLayer=%p readyForDisplay=%d)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called (keyPath=%@, object=%@, change=%@, context=%p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called PresentationSizeDidChange videoLayer %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called isReadyForDisplay=%s"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> called w/ videoLayer %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> check should notify player _playerLayer->lastWindowSceneEvent > None (%d), isVisible (%d), _isPartOfForegroundScene (%d)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> creating interstitialLayer %p for primary playerLayer %p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> displaySize is %f x %f rootSize is %f x %f percentage %f"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> finished"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> got window scene in state %ld"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> layer active state changed to %d"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> no window scene in _currentWindowSceneIsForeground, return default %d"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> notifying player %p about new display size"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> player layer %p <-> player layer %p"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> requesting the pixelBufferAttributes property on a presentation layer is invalid"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> return default based on last window scene event %d"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> scalingFactor(%d) is not between 2 and 8"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> setting forScrubbingOnly = %d"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> setting new sublayers: videoLayer(%p), closedCaptionLayer(%p), subtitleLayer(%p), interstitialLayers = %@"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> setting player from <%{public}@|%p> to <%{public}@|%p> forPIP:%d"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> size needs no update using cached value { %f, %f }"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> size needs update from { %f, %f } to { %f, %f } (force=%s)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> skip notifying player as isVisible (%d) !=  _isPartOfForegroundScene"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> sync to player (player=%p)"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> updated isReadyForDisplay=%s"
- "<<<< AVPlayerLayer >>>> %s: Storing client layer %@ with indexPath %@"
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
- "<<<< AVQueuePlayer >>>> %s: <%{public}@|%p> called"
- "<<<< AVQueuePlayer >>>> %s: <%{public}@|%p> called (#items %d)"
- "<<<< AVQueuePlayer >>>> %s: <%{public}@|%p> called (item = %@)"
- "<<<< AVQueuePlayer >>>> %s: <%{public}@|%p> called (item = %@, afterItem = %@"
- "<<<< AVQueuePlayer >>>> %s: <%{public}@|%p> ignoring since buffered airplay is enabled but first 2 items are not ready for inspection"
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
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> Notification received: name=%@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> Notification received: name=%@ (flushed automatically at time=%1.3f)"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> Transitioning to status: %d"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> adding notification listener to %p with listener %p"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> called"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> called: %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> called: %lu"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> called: %p"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> created"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> found contextUUID : %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> got notification %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> removing notification listener to %p with listener %p"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> setting routing context id : %@"
- "<<<< AVSampleBufferAudioRenderer >>>> %s: <%{public}@|%p> trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
- "<<<< AVSampleBufferAudioRenderer >>>> %s: Failed to create FigSampleBufferAudioRenderer: %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> %p AVSampleBufferDisplayLayer's net flip status does match CoreAnimation default"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> %p AVSampleBufferDisplayLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> AVSBDL entering PiP, setting preferredDynamicRange"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> AVSBDL exiting PiP, setting preferredDynamicRange"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Created layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Hiding contentLayer because bounds is CGSizeZero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> New label \"%@\", Current label \"%@\", Layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Removing label from layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Setting label \"%@\" on layer %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Setting position(%d,%d), bounds(%dx%d), transform scale(%.3fx%.3f), offset(%d,%d)"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Unhiding contentLayer because bounds is nonzero"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> Visibility [%@], on thread %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> bounds: %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> called"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> on thread %@"
- "<<<< AVSampleBufferDisplayLayer >>>> %s: <%{public}@|%p> videoRect: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Cleaning-up renderer %p for synchronizerInternal %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Error adding an AudioRenderer to the FigSynchronizer: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Failed to add Renderer %@; error returned from _addRenderer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Failed to create FigSampleBufferRenderSynchronizer: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Selecting AVSBDL=%p that already contains a label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Selecting AVSBVR=%p with label"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Setting STSLabel %@ on renderer=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Setting new STSLabel on AVSBDL=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Setting self as render synchronizer on renderer (%p) failed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Too many audio renderers"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Trying to add a renderer (%p) to same synchronizer"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Trying to add multiple audio renderers when disallowed"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> Was tracking AVSBDL=%p, switching to AVSBVR=%p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> [%p], on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> adding renderer %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> called (center=%@, listener=%p, name=%@, object=%p, payload=%@)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> called (time observer = <%p>)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> called for renderer %p; time: %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> created (internal: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> error: %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> invalidated old scheduled removal of renderer %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> old once observer already fired before we could invalidate it (renderer: %p)"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> rate: %1.3f; time: %1.3f; hostTime: %1.3f; fig error: %d"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> releasing on main thread avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> removalBlock called; weakToSelf: %p; weakToRenderer: %p"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> retaining avsbdl %p, on thread %@"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> successfully scheduled removal of renderer %p at time %1.3f"
- "<<<< AVSampleBufferRenderSynchronizer >>>> %s: <%{public}@|%p> unknown renderer: %p"
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
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Adding %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Calling completion handler with %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Calling completion handler with success"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Failed to copy currently displayed pixel buffer as there is no video queue"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Failed to create AVSBVR error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Failed to create video queue error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Failed with error %d at %s"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> FigVideoQueueFlush returned error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Flush completed but no pending callback block found"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Flush returned err=%d. Recreating FigVideoQueue. %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Ignoring enqueueSampleBuffer because status is failed"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> No formatDescription found in sampleBuffer"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> No pending preroll callback"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Output obscured = %@, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Received complete decode for preroll [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Received external protection status changed [%p] to \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Received flush complete [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Received video queue decode error \"%@\""
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Received video queue did drop below low water level [%p]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> RemoveDisplayedImage=%s, handler=%p, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Removing %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Setting %@, posting AVSampleBufferSTSLabelDidChangeNotification"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Setting %p, returning %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Skip stale callback, requestId (%d) != pendingPrerollRequestID (%d)"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Total frames enqueued since last flush %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Trying to add to a synchronizer (%p) when we already are added to a synchronizer (%p)."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Unable to set expectMinimumUpcomingSampleBufferPresentationTime because minimumUpcomingPresentationTime is not numeric"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> UpcomingPTSExpectation is enabled, but enqueuePTS:%.3f is smaller than expectedMinimumUpcomingPTS:%.3f"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> VideoQueue [%p] Setting %d video destinations."
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> VideoQueue [%p] Setting display layer %p"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> VideoQueue [%p] Setting video destination array %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> VideoQueue [%p] on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Visibility [%@] on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Visibility changed to %s, post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Enqueue sample buffer failed error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Failed to copy currently displayed pixel buffer although no error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Received lost decoder state error"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Received server connection died with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Received server dependency lost with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> [%p] Received video queue failed with error %d"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> _updatePreferredDynamicRange(%@)"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> exit layerQueue block, on thread [%@]"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> readyForDisplay changed (%@), post notification: %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> releasing %p on main thread, on thread %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> timebase %@"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: addSampleBufferDisplayLayer failed to set content layer with error %d"
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
- "<<<< AVSystemMuteObserver >>>> %s: AVSystemController unavailable; cannot observe system volume/mute. AVSystemController class=%p"
- "<<<< AVSystemMuteObserver >>>> %s: Audio notification: %{public}@"
- "<<<< AVSystemMuteObserver >>>> %s: cachedCaptionsOnMutePreferenceEnabled=%d"
- "<<<< AVSystemMuteObserver >>>> %s: kAXSAutomaticSubtitlesShowWhenMutedEnabledNotification"
- "<<<< AVSystemMuteObserver >>>> %s: mute status: AVSystemController=%s, (tvOS MASystemMute=%s), (macOS outputContext=%s, coreAudio=%s)"
- "<<<< AVSystemMuteObserver >>>> %s: notify_register_dispatch failed for AX captions-on-mute pref (status=%u)"
- "<<<< AVSystemMuteObserver >>>> %s: systemMuted changed -> %d"
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
- "AVActivityProgressClient.m"
- "AVAsset.m"
- "AVAssetDownloadConfiguration.m"
- "AVAssetDownloadSession.m"
- "AVAssetReaderOutputCaptionAdaptor.m"
- "AVAssetResourceLoader.m"
- "AVAssetWriterFigAssetWriterHandleCompletedNotification"
- "AVAssetWriterFigAssetWriterHandleDiskReserveThresholdExhaustedNotification"
- "AVAssetWriterFigAssetWriterHandleFailedNotification"
- "AVAssetWriterFigAssetWriterHandleServerDiedNotification"
- "AVAssetWriterInputFigAssetWriterEndPassOperationPassFinished"
- "AVAssetWritingPlanner.m"
- "AVCanWriteFilesToDirectoryAtURL"
- "AVCompositionTrack.m"
- "AVContentKeySession.m"
- "AVEnsureNotOnMainThread"
- "AVErrorAssetWritingPlannerStateFileInvalidValue"
- "AVIsURLIsAllowableExternalOrCacheDeleteDirectory"
- "AVIsURLOnInternalVolume"
- "AVLocalizedError"
- "AVLocalizedStringFromTableWithLocaleWithBundleIdentifier"
- "AVMediaStatePurgePostMediaStateWasPurgedNotificationForObject"
- "AVMetadataItem.m"
- "AVMetadataItemMakeDataFromBoxedMetadata"
- "AVOperationStatusResolveOldAndNew"
- "AVPerformDelegateCallbackSynchronouslyForDelegateStorageIfCurrentDelegateQueueIsQueueElseDispatchToCurrentDelegateQueue"
- "AVPlaybackCoordinator.m"
- "AVPlayerCaptionLayer <%p>"
- "AVPlayerGetFigPlayerTypeForAsset"
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
- "AVSampleBufferVideoRenderer.m"
- "AVSerializeOnQueueAsyncIfNecessary"
- "AVStreamDataParser.m"
- "AVTimebaseObserver_figTimebaseGetTime"
- "AVTimebaseObserver_timebaseNotificationCallback_block_invoke"
- "AVUtilities.m"
- "AVVideoOutputSettings.m"
- "AudioCodecType not found in dictionary"
- "CACHE VALID"
- "CALayer (Caption Preview only)"
- "CALayer (Preview only)"
- "CMTagCollectionCreateWithVideoOutputPreset"
- "CodecType not found in dictionary"
- "Could not set KeyResponseReceived state on cryptor."
- "Cryptor is not available to create key request."
- "Failed allocating VTCompressionSession"
- "Failed on init"
- "Failed setting resumable compressionSession properties"
- "Failed to allocate CFMutableDictionary"
- "Failed to allocate buffer for FigBoxedMetadata -> CFData conversion"
- "Failed to connect to coordination medium"
- "Failed to create a segment from dictionary"
- "Failed to get queue"
- "Failed to load ActivityProgressKit"
- "Failed to load BSMutableServiceInterface"
- "Failed to load BSObjCProtocol"
- "Failed to load BSServiceConnection"
- "Failed to load BSServiceConnectionEndpoint"
- "Failed to load BSServiceQuality"
- "Failed to load RBSDomainAttribute"
- "Failed to load trackState from dictionary"
- "Failed to prepare cryptor"
- "FigSubtitleCALayer"
- "FrameCount <= 0 from dictionary"
- "HasCompleted not found from dictionary"
- "Hiding"
- "Incompatible preset"
- "Invalid asset track"
- "Invalid timeRange from dictionary"
- "MediaType not found in dictionary"
- "Missing SoftwareBuild in planner state"
- "NO CACHE"
- "NOT visible"
- "NULL"
- "NULL figAsset"
- "NULL handlerServerXPCEndpoint"
- "NULL segmentURL from dictionary"
- "Names count is 0?"
- "No FCKS available"
- "NoSignal"
- "NotMuted"
- "Received invalid preset"
- "RequiresCompression not found in dictionary"
- "SecTaskCreateFromSelf failed"
- "Segments not found in dictionary"
- "Set avplayer_trace=3 for backtrace"
- "Showing"
- "The AVSampleBufferDisplayLayer's content layer and video destination are nil."
- "TimeRange from dictionary <= 0"
- "TimeRange from dictionary has a non-numeric duration"
- "TimeRange from dictionary has a non-numeric start"
- "TrackID is invalid in dictionary"
- "TrackID not found in dictionary"
- "Trying to create AVAssetDownloadContentConfiguration with an invalid AVAssetVariantQualifier"
- "Visible"
- "WILL"
- "WILL NOT"
- "YES => (missing audio edit list detected)"
- "_avplLoopingItemFailedToPlayToEndTimeNotificationHandler"
- "_enqueueSingleSampleBufferStatic"
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
- "activityprogress_trace"
- "aig_trace"
- "appendCaptionGroupToQueue"
- "are"
- "are NOT"
- "assetTrackNotificationHandler"
- "assetinspector_trace"
- "assetreaderoutput_trace"
- "assettrackinspector_trace"
- "assetwriter_trace"
- "assetwriterinput_trace"
- "assetwriterinputannotationadaptor_trace"
- "assetwriterinputmetadataadaptor_trace"
- "audioCodecType is not NSString"
- "audiomix"
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
- "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_2"
- "avplayer_fpNotificationCallback"
- "avplayer_fpNotificationCallback_block_invoke_2"
- "avplayer_fpNotificationCallback_block_invoke_3"
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
- "avplayeritem_fpItemNotificationCallback_block_invoke_5"
- "avplayeritem_fpItemNotificationCallback_block_invoke_7"
- "avplayeritemlegibleoutput_trace"
- "avplayeritemmediadatacollector_trace"
- "avplayeritemmetadatacollector_trace"
- "avplayeritemmetadataoutput_trace"
- "avplayeritemoutput_trace"
- "avplayeritemrenderedlegibleoutput_trace"
- "avplayerlooper_trace"
- "avplayeroutput_trace"
- "avqsbar_figRendererNowBelowLowWaterLevelNotificationHandler"
- "avqsbar_figRendererRebuildCouldBenefitFidelityNotificationHandler"
- "avqsbar_figRendererServerDied"
- "avqsbar_figRendererWasFlushedAutomaticallyNotificationHandler"
- "avrendersynchronize_cleanUpAllAddedRenderers"
- "avrendersynchronize_electRendererForSTSAndSendLabelToAudioRenderers"
- "avrendersynchronize_performRendererRemoval"
- "avrendersynchronizer_timebaseRateChanged"
- "avsamplebufferdisplaylayer_trace"
- "avsamplebuffergenerator_trace"
- "avsamplebufferoutput_trace"
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
- "codecType is not NSString"
- "completed"
- "composition_trace"
- "copyInternalFigSampleBufferRenderSynchronizer failed."
- "could not create trackDecryptor"
- "createFigAsset"
- "creationOptions NULL"
- "cryptor is NULL"
- "currentProcessHasTrueBooleanEntitlement"
- "customURLAuthHandlerHandleRequestCallback"
- "customURLAuthHandlerRequestCancelled"
- "customURLHandlerHandleRequestCallback"
- "customURLHandlerRequestCancelled"
- "delegateutils_trace"
- "download_trace"
- "err"
- "expected initialization data to be a JSON dictionary containing an array of SINF data"
- "externaldevice_trace"
- "failed"
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
- "figPlaybackItemSampleBufferProviderAvailable"
- "figPlaybackItemSampleBufferProviderDataAvailable"
- "figPlaybackItemSampleBufferProviderResetOutput"
- "figPlaybackItemTrackResetSampleBufferExtraction"
- "figPlaybackItemTrackSampleBufferDidBecomeAvailable"
- "file"
- "filesystemutilities_trace"
- "frameCountNumber is not NSNumber"
- "frameCountNumber not found from dictionary"
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
- "kFigAssetDownloaderError_AllocationFailed"
- "kFigCPEError_InvalidState"
- "kFigContentKeyBossError_AllocationFailed"
- "kFigMetadataReaderError_AllocationFailed"
- "kFigSSMError_InvalidState"
- "key request has not succeeded. value not available."
- "kvodispatcher_trace"
- "lastCompletedSegmentFinalClientState is not NSData"
- "lastCompletedSegmentFinalCompressionSessionState is not NSDictionary"
- "mediaType is not NSString"
- "mismatched handler"
- "mixed"
- "nil reference"
- "no figAsset"
- "non-NULL"
- "not an AVAssetResourceLoader"
- "not an AVAssetResourceLoaderRemoteHandlerContext"
- "not an AVContentKeyReportGroup"
- "not an AVContentKeySession"
- "not mixed"
- "not spatial"
- "playback"
- "present"
- "remote"
- "requiresCompression not found from dictionary"
- "requiresCompressionNumber is not NSNumber"
- "scheduledaudioparameters_trace"
- "segmentsAsDictionaries is not NSArray"
- "self.figAsset NULL"
- "spi"
- "stringWithValidatedFormat"
- "stringWithValidatedFormatArg2"
- "stringWithValidatedFormatInteger"
- "stringWithValidatedFormatString"
- "timeRangeDictionary is not NSDictionary"
- "trackIDNumber is not NSNumber"
- "true"
- "visible"
- "yes"
```
