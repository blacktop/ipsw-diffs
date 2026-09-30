## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

```diff

-  __TEXT.__text: 0x209ba8
-  __TEXT.__objc_methlist: 0x1b98c
-  __TEXT.__const: 0x1ffc
-  __TEXT.__gcc_except_tab: 0xa960
-  __TEXT.__cstring: 0x33fdb
-  __TEXT.__oslogstring: 0x1c87c
+  __TEXT.__text: 0x20cdc0
+  __TEXT.__objc_methlist: 0x1bbcc
+  __TEXT.__const: 0x201c
+  __TEXT.__gcc_except_tab: 0xab1c
+  __TEXT.__cstring: 0x343fb
+  __TEXT.__oslogstring: 0x1ce8f
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x41a
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xa3b0
+  __TEXT.__unwind_info: 0xa468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x34b8
-  __DATA_CONST.__objc_classlist: 0x1230
+  __DATA_CONST.__const: 0x34d0
+  __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xafb8
+  __DATA_CONST.__objc_selrefs: 0xb0f8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xd68
+  __DATA_CONST.__objc_superrefs: 0xd70
   __DATA_CONST.__objc_arraydata: 0x308
-  __DATA_CONST.__got: 0x45f0
-  __AUTH_CONST.__const: 0x3bd0
-  __AUTH_CONST.__cfstring: 0x1ae20
-  __AUTH_CONST.__objc_const: 0x31de0
+  __DATA_CONST.__got: 0x4660
+  __AUTH_CONST.__const: 0x3c30
+  __AUTH_CONST.__cfstring: 0x1aea0
+  __AUTH_CONST.__objc_const: 0x32390
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1e20
-  __AUTH.__objc_data: 0x7fb0
-  __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x2708
-  __DATA.__data: 0x16a0
+  __AUTH_CONST.__auth_got: 0x1e58
+  __AUTH.__objc_data: 0x8e10
+  __AUTH.__data: 0x1e8
+  __DATA.__objc_ivar: 0x277c
+  __DATA.__data: 0x1700
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x440
-  __DATA.__bss: 0x13b0
-  __DATA_DIRTY.__objc_data: 0x36b0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0x2b0
-  __DATA_DIRTY.__bss: 0x160
+  __DATA.__common: 0x430
+  __DATA.__bss: 0x1360
+  __DATA_DIRTY.__objc_data: 0x28a0
+  __DATA_DIRTY.__common: 0x2e0
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
+  - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport
   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12315
-  Symbols:   29708
-  CStrings:  9663
+  Functions: 12380
+  Symbols:   29868
+  CStrings:  9705
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ +[AVAssetWritingPlannerTrackSegmentState fromDictionary:mediaType:error:]
+ +[AVSystemMuteObserver initialize]
+ -[AVAssetTrackPlan requiresCompression]
+ -[AVAssetTrackPlanExecutor aspFrequency]
+ -[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]
+ -[AVAssetTrackPlanExecutor mediaSubType]
+ -[AVAssetTrackPlanExecutor requiresCompression]
+ -[AVAssetTrackPlanExecutor segmentFlushDuration]
+ -[AVAssetTrackPlanExecutor segmentOverlapDuration]
+ -[AVAssetTrackPlanExecutor trackPlan]
+ -[AVAssetVideoTrackPlan requiresCompression]
+ -[AVAssetVideoTrackPlan videoCodec]
+ -[AVAssetWritingPlannerIncrementalState allSegmentsCompleted]
+ -[AVAssetWritingPlannerIncrementalState setAllSegmentsCompleted:]
+ -[AVAssetWritingPlannerTrackSegmentState flushDuration]
+ -[AVAssetWritingPlannerTrackSegmentState mediaType]
+ -[AVAssetWritingPlannerTrackSegmentState overlapDuration]
+ -[AVAssetWritingPlannerTrackSegmentState requiresCompression]
+ -[AVAssetWritingPlannerTrackSegmentState setFlushDuration:]
+ -[AVAssetWritingPlannerTrackSegmentState setMediaType:]
+ -[AVAssetWritingPlannerTrackSegmentState setOverlapDuration:]
+ -[AVAssetWritingPlannerTrackSegmentState setRequiresCompression:]
+ -[AVAssetWritingPlannerTrackState audioCodecType]
+ -[AVAssetWritingPlannerTrackState loudnessMeasurementCompleted]
+ -[AVAssetWritingPlannerTrackState measuredLoudnessMagicCookie]
+ -[AVAssetWritingPlannerTrackState requiresCompression]
+ -[AVAssetWritingPlannerTrackState setAudioCodecType:]
+ -[AVAssetWritingPlannerTrackState setLoudnessMeasurementCompleted:]
+ -[AVAssetWritingPlannerTrackState setMeasuredLoudnessMagicCookie:]
+ -[AVAssetWritingPlannerTrackState setRequiresCompression:]
+ -[AVPlayer _maximumAVPlayerLayerDisplaySize_invokeOnMainQueue]
+ -[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]
+ -[AVPlayer(AVPlayerLegibleFallback) endUserTurnedOffSubtitles]
+ -[AVPlayer(AVPlayerLegibleFallback) isOverridingCaptionDisplayTypeWhileMuted]
+ -[AVPlayer(AVPlayerSystemMute) _isEffectivelyMuted]
+ -[AVPlayer(AVPlayerSystemMute) systemMuteDidChange:]
+ -[AVPlayerLayer _displaySize_invokeOnMainQueue]
+ -[AVPlayerLayer _percentCoverageRelativeToRootLayer_invokeOnMainQueue]
+ -[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererForUnitTests) _unitTest_simulateLostDecoderState]
+ -[AVSystemMuteObserver .cxx_destruct]
+ -[AVSystemMuteObserver _evaluate]
+ -[AVSystemMuteObserver _notifyDelegateOfChange]
+ -[AVSystemMuteObserver _readMacOSStateInto:coreAudio:]
+ -[AVSystemMuteObserver _rebindCoreAudioListenersToCurrentDevice]
+ -[AVSystemMuteObserver _refreshCachedCaptionsOnMutePreferenceEnabled]
+ -[AVSystemMuteObserver _startObservingAccessibility]
+ -[AVSystemMuteObserver _startObservingOnMacOS]
+ -[AVSystemMuteObserver _stopObservingOnMacOS]
+ -[AVSystemMuteObserver dealloc]
+ -[AVSystemMuteObserver delegate]
+ -[AVSystemMuteObserver init]
+ -[AVSystemMuteObserver isCaptionsOnMutePreferenceEnabled]
+ -[AVSystemMuteObserver isSystemMuted]
+ -[AVSystemMuteObserver setDelegate:]
+ -[AVSystemMuteObserver startObservingWithDelegate:]
+ -[AVSystemMuteObserver stopObserving]
+ GCC_except_table156
+ GCC_except_table176
+ GCC_except_table233
+ GCC_except_table374
+ GCC_except_table379
+ GCC_except_table393
+ GCC_except_table405
+ GCC_except_table433
+ GCC_except_table435
+ GCC_except_table442
+ GCC_except_table445
+ GCC_except_table447
+ GCC_except_table449
+ GCC_except_table453
+ GCC_except_table455
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table468
+ GCC_except_table475
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table488
+ GCC_except_table505
+ GCC_except_table523
+ GCC_except_table528
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table547
+ GCC_except_table562
+ GCC_except_table566
+ GCC_except_table568
+ GCC_except_table596
+ GCC_except_table600
+ GCC_except_table604
+ GCC_except_table623
+ GCC_except_table629
+ GCC_except_table636
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table662
+ GCC_except_table668
+ GCC_except_table680
+ GCC_except_table684
+ GCC_except_table709
+ GCC_except_table711
+ GCC_except_table713
+ GCC_except_table717
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table741
+ GCC_except_table745
+ GCC_except_table749
+ GCC_except_table780
+ GCC_except_table785
+ GCC_except_table787
+ OBJC_IVAR_$_AVAssetTrackPlanExecutor._aspFrequency
+ OBJC_IVAR_$_AVAssetTrackPlanExecutor._segmentFlushDuration
+ OBJC_IVAR_$_AVAssetTrackPlanExecutor._segmentOverlapDuration
+ OBJC_IVAR_$_AVAssetWritingPlannerIncrementalState._allSegmentsCompleted
+ OBJC_IVAR_$_AVAssetWritingPlannerProgress._apacTrackIDs
+ OBJC_IVAR_$_AVAssetWritingPlannerProgress._loudnessCompletedTrackIDs
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._flushDuration
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._mediaType
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._overlapDuration
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._requiresCompression
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackState._audioCodecType
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackState._loudnessMeasurementCompleted
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackState._measuredLoudnessMagicCookie
+ OBJC_IVAR_$_AVAssetWritingPlannerTrackState._requiresCompression
+ OBJC_IVAR_$_AVPlayerInternal.lastCaptionAppearanceDisplayTypeOverride
+ OBJC_IVAR_$_AVPlayerInternal.muteOverrideSuppressedUntilUnmute
+ OBJC_IVAR_$_AVPlayerInternal.systemMute
+ OBJC_IVAR_$_AVSampleBufferDisplayLayer._initFailureError
+ OBJC_IVAR_$_AVSystemMuteObserver._cachedCaptionsOnMutePreferenceEnabled
+ OBJC_IVAR_$_AVSystemMuteObserver._captionsOnMutePreferenceNotifyToken
+ OBJC_IVAR_$_AVSystemMuteObserver._coreAudioCurrentDeviceID
+ OBJC_IVAR_$_AVSystemMuteObserver._coreAudioMuteListener
+ OBJC_IVAR_$_AVSystemMuteObserver._coreAudioRouteListener
+ OBJC_IVAR_$_AVSystemMuteObserver._coreAudioVolumeListener
+ OBJC_IVAR_$_AVSystemMuteObserver._delegate
+ OBJC_IVAR_$_AVSystemMuteObserver._observing
+ OBJC_IVAR_$_AVSystemMuteObserver._outputContextCanSetVolumeToken
+ OBJC_IVAR_$_AVSystemMuteObserver._outputContextOutputDevicesToken
+ OBJC_IVAR_$_AVSystemMuteObserver._outputContextVolumeToken
+ OBJC_IVAR_$_AVSystemMuteObserver._serialQueue
+ OBJC_IVAR_$_AVSystemMuteObserver._sharedOutputContext
+ OBJC_IVAR_$_AVSystemMuteObserver._systemMuted
+ _AVOutputContextCanSetVolumeDidChangeNotification
+ _AVOutputContextOutputDevicesDidChangeNotification
+ _AVOutputContextVolumeDidChangeNotification
+ _AudioObjectAddPropertyListenerBlock
+ _AudioObjectGetPropertyData
+ _AudioObjectHasProperty
+ _AudioObjectRemovePropertyListenerBlock
+ _OBJC_CLASS_$_AVSystemMuteObserver
+ _OBJC_METACLASS_$_AVSystemMuteObserver
+ __283-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]_block_invoke
+ __46-[AVSystemMuteObserver _startObservingOnMacOS]_block_invoke
+ __51-[AVPlayer _evaluateDisplaySizeOfAllAttachedLayers]_block_invoke
+ __80-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]_block_invoke
+ __AVSystemMuteObserverCopyDefaultOutputDeviceID
+ __AVSystemMuteObserverRemoveAndReleaseNotificationToken
+ __AXSAutomaticSubtitlesShowWhenMuted
+ __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
+ __OBJC_$_CLASS_METHODS_AVSystemMuteObserver
+ __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
+ __OBJC_$_INSTANCE_METHODS_AVSystemMuteObserver
+ __OBJC_$_INSTANCE_VARIABLES_AVSystemMuteObserver
+ __OBJC_$_PROP_LIST_AVSystemMuteObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVSystemMuteObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVSystemMuteObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_AVSystemMuteObserverDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
+ __OBJC_CLASS_RO_$_AVSystemMuteObserver
+ __OBJC_LABEL_PROTOCOL_$_AVSystemMuteObserverDelegate
+ __OBJC_METACLASS_RO_$_AVSystemMuteObserver
+ __OBJC_PROTOCOL_$_AVSystemMuteObserverDelegate
+ ___283-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]_block_invoke
+ ___30-[AVChapterMetadataItem value]_block_invoke
+ ___36-[AVChapterMetadataItem description]_block_invoke
+ ___37-[AVSystemMuteObserver stopObserving]_block_invoke
+ ___40-[AVChapterMetadataItem _takeValueFrom:]_block_invoke
+ ___46-[AVSystemMuteObserver _startObservingOnMacOS]_block_invoke
+ ___51-[AVSystemMuteObserver startObservingWithDelegate:]_block_invoke
+ ___52-[AVSystemMuteObserver _startObservingAccessibility]_block_invoke
+ ___62-[AVPlayer(AVPlayerLegibleFallback) endUserTurnedOffSubtitles]_block_invoke
+ ___77-[AVPlayer(AVPlayerLegibleFallback) isOverridingCaptionDisplayTypeWhileMuted]_block_invoke
+ ___80-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]_block_invoke
+ ___80-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e44_v20?0I8r^{AudioObjectPropertyAddress=III}12l
+ ___block_descriptor_40_e8_32w_e8_v12?0i8l
+ _gAVSystemMuteObserverTrace
+ _kAXSAutomaticSubtitlesShowWhenMutedEnabledNotification
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$_displaySize_invokeOnMainQueue
+ _objc_msgSend$_evaluate
+ _objc_msgSend$_isEffectivelyMuted
+ _objc_msgSend$_maximumAVPlayerLayerDisplaySize_invokeOnMainQueue
+ _objc_msgSend$_notifyDelegateOfChange
+ _objc_msgSend$_readMacOSStateInto:coreAudio:
+ _objc_msgSend$_rebindCoreAudioListenersToCurrentDevice
+ _objc_msgSend$_refreshCachedCaptionsOnMutePreferenceEnabled
+ _objc_msgSend$_startObservingAccessibility
+ _objc_msgSend$_startObservingOnMacOS
+ _objc_msgSend$_stopObservingOnMacOS
+ _objc_msgSend$_updateCaptionAppearanceDisplayTypeOverride
+ _objc_msgSend$allSegmentsCompleted
+ _objc_msgSend$callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:
+ _objc_msgSend$canSetVolume
+ _objc_msgSend$defaultSharedOutputContext
+ _objc_msgSend$fromDictionary:mediaType:error:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$isCaptionsOnMutePreferenceEnabled
+ _objc_msgSend$isOverridingCaptionDisplayTypeWhileMuted
+ _objc_msgSend$isSystemMuted
+ _objc_msgSend$mediaSubType
+ _objc_msgSend$overlapDuration
+ _objc_msgSend$requiresCompression
+ _objc_msgSend$segmentFlushDuration
+ _objc_msgSend$segmentOverlapDuration
+ _objc_msgSend$setAllSegmentsCompleted:
+ _objc_msgSend$setAudioCodecType:
+ _objc_msgSend$setRequiresCompression:
+ _objc_msgSend$startObservingWithDelegate:
+ _objc_msgSend$stopObserving
+ _objc_msgSend$systemMuteDidChange:
+ _objc_msgSend$videoCodec
- +[AVAssetWritingPlannerTrackSegmentState fromDictionary:error:]
- -[AVAssetTrackPlan requiresVideoCompression]
- -[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]
- -[AVAssetTrackPlanExecutor requiresVideoCompression]
- -[AVAssetVideoTrackPlan requiresVideoCompression]
- -[AVAssetWritingPlannerTrackSegmentState requiresVideoCompression]
- -[AVAssetWritingPlannerTrackSegmentState setRequiresVideoCompression:]
- -[AVAssetWritingPlannerTrackState requiresVideoCompression]
- -[AVAssetWritingPlannerTrackState setRequiresVideoCompression:]
- -[AVPlayer _maximumAVPlayerLayerDisplaySize]
- -[AVPlayerLayer _displaySize]
- -[AVPlayerLayer _percentCoverageRelativeToRootLayer]
- GCC_except_table175
- GCC_except_table232
- GCC_except_table373
- GCC_except_table378
- GCC_except_table390
- GCC_except_table394
- GCC_except_table411
- GCC_except_table414
- GCC_except_table418
- GCC_except_table427
- GCC_except_table429
- GCC_except_table432
- GCC_except_table441
- GCC_except_table450
- GCC_except_table452
- GCC_except_table466
- GCC_except_table471
- GCC_except_table474
- GCC_except_table477
- GCC_except_table481
- GCC_except_table483
- GCC_except_table491
- GCC_except_table496
- GCC_except_table501
- GCC_except_table508
- GCC_except_table526
- GCC_except_table529
- GCC_except_table535
- GCC_except_table540
- GCC_except_table542
- GCC_except_table550
- GCC_except_table553
- GCC_except_table557
- GCC_except_table563
- GCC_except_table577
- GCC_except_table579
- GCC_except_table593
- GCC_except_table603
- GCC_except_table607
- GCC_except_table610
- GCC_except_table612
- GCC_except_table621
- GCC_except_table626
- GCC_except_table642
- GCC_except_table644
- GCC_except_table649
- GCC_except_table657
- GCC_except_table659
- GCC_except_table665
- GCC_except_table667
- GCC_except_table674
- GCC_except_table687
- GCC_except_table691
- GCC_except_table701
- GCC_except_table703
- GCC_except_table705
- GCC_except_table718
- GCC_except_table722
- GCC_except_table729
- GCC_except_table730
- GCC_except_table739
- GCC_except_table758
- GCC_except_table763
- GCC_except_table772
- GCC_except_table775
- OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._requiresFrameCount
- OBJC_IVAR_$_AVAssetWritingPlannerTrackSegmentState._requiresVideoCompression
- OBJC_IVAR_$_AVAssetWritingPlannerTrackState._requiresVideoCompression
- __216-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]_block_invoke
- __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- ___216-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]_block_invoke
- ___77-[AVPlayer(AVPlayerLegibleFallback) setCaptionAppearanceDisplayTypeOverride:]_block_invoke_2
- _objc_msgSend$_displaySize
- _objc_msgSend$_maximumAVPlayerLayerDisplaySize
- _objc_msgSend$callWritingSegmentCallbackForTrack:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:
- _objc_msgSend$requiresVideoCompression
- _objc_msgSend$setRequiresVideoCompression:
CStrings:
+ "+[AVAssetWritingPlannerTrackSegmentState fromDictionary:mediaType:error:]"
+ "-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]"
+ "-[AVAssetWritingPlanner buildAssemblyComposition:]"
+ "-[AVPlayer(AVPlayerLegibleFallback) _updateCaptionAppearanceDisplayTypeOverride]"
+ "-[AVPlayer(AVPlayerLegibleFallback) endUserTurnedOffSubtitles]"
+ "-[AVPlayerLayer _displaySize_invokeOnMainQueue]"
+ "-[AVPlayerLayer _percentCoverageRelativeToRootLayer_invokeOnMainQueue]"
+ "-[AVSystemMuteObserver _evaluate]"
+ "-[AVSystemMuteObserver _refreshCachedCaptionsOnMutePreferenceEnabled]"
+ "-[AVSystemMuteObserver _startObservingAccessibility]"
+ "-[AVSystemMuteObserver _startObservingAccessibility]_block_invoke"
+ "-[AVSystemMuteObserver _startObservingOnMacOS]"
+ "-[AVSystemMuteObserver _startObservingOnMacOS]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
+ "<<<< AVAssetWritingPlanner >>>> %s: Failed to construct assemblyComposition"
+ "<<<< AVAssetWritingPlanner >>>> %s: Failed to load track from track segment output URL"
+ "<<<< AVAssetWritingPlanner >>>> %s: _requiresCompression (%d) from savedState does not match _requiresCompression (%d) from current state"
+ "<<<< AVAssetWritingPlanner >>>> %s: segment mediaType from saved state (%@) does not match current segment's mediaType (%@)"
+ "<<<< AVAssetWritingPlanner >>>> %s: segmentFileTimeRange %1.3f - %1.3f --> outputTrackTime %1.3f"
+ "<<<< AVAssetWritingPlanner >>>> %s: trackPlanExecutor %@"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> cleared muteOverrideSuppressedUntilUnmute on unmute"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> effectivelyMuted=%d playerMuted=%d captionsOnMuteEnabled=%d muteOverrideSuppressed=%d effectiveOverride=%ld"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> endUserTurnedOffSubtitles; suppressing mute override until next mute"
+ "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> notifying player %p about new display size"
+ "<<<< AVSystemMuteObserver >>>> %s: AVOutputContext unavailable, skipping"
+ "<<<< AVSystemMuteObserver >>>> %s: CoreAudio mute fired"
+ "<<<< AVSystemMuteObserver >>>> %s: CoreAudio route/restart fired"
+ "<<<< AVSystemMuteObserver >>>> %s: CoreAudio volume fired"
+ "<<<< AVSystemMuteObserver >>>> %s: cachedCaptionsOnMutePreferenceEnabled=%d"
+ "<<<< AVSystemMuteObserver >>>> %s: kAXSAutomaticSubtitlesShowWhenMutedEnabledNotification"
+ "<<<< AVSystemMuteObserver >>>> %s: mute status: AVSystemController=%s, (tvOS MASystemMute=%s), (macOS outputContext=%s, coreAudio=%s)"
+ "<<<< AVSystemMuteObserver >>>> %s: notification: %{public}@"
+ "<<<< AVSystemMuteObserver >>>> %s: notify_register_dispatch failed for AX captions-on-mute pref (status=%u)"
+ "<<<< AVSystemMuteObserver >>>> %s: systemMuted changed -> %d"
+ "AllSegmentsCompleted"
+ "AudioCodecType"
+ "AudioCodecType not found in dictionary"
+ "Media type is not supported.  Expect AVMediaTypeVideo or AVMediaTypeAuxiliaryPicture."
+ "NoSignal"
+ "NotMuted"
+ "RequiresCompression"
+ "RequiresCompression not found in dictionary"
+ "audioCodecType is not NSString"
+ "avsystemmuteobserver_trace"
+ "com.apple.avplayer.systemMuteObserver"
+ "requiresCompression not found from dictionary"
+ "requiresCompressionNumber is not NSNumber"
+ "segmentConfigurations must only contain AVPlannedSegmentConfiguration or AVPlannedVideoSegmentConfiguration objects"
+ "v20@?0I8r^{AudioObjectPropertyAddress=III}12"
- "+[AVAssetWritingPlannerTrackSegmentState fromDictionary:error:]"
- "-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:]"
- "-[AVPlayerLayer _displaySize]"
- "-[AVPlayerLayer _percentCoverageRelativeToRootLayer]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fbOomY/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
- "<<<< AVAssetWritingPlanner >>>> %s: _requiresVideoCompression (%d) from savedState does not match _requiresVideoCompression (%d) from current state"
- "<<<< AVPlayerLayer >>>> %s: <%{public}@|%p> notifying player %p about new display size %@"
- "RequiresVideoCompression"
- "RequiresVideoCompression not found in dictionary"
- "requiresVideoCompression not found from dictionary"
- "requiresVideoCompressionNumber is not NSNumber"

```
