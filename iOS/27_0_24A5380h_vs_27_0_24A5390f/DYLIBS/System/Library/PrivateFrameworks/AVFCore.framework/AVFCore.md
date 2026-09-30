## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2450.67.3.0.0
-  __TEXT.__text: 0x21d068
+2450.71.1.11.1
+  __TEXT.__text: 0x21f614
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1bed4
-  __TEXT.__cstring: 0x35323
+  __TEXT.__objc_methlist: 0x1c044
+  __TEXT.__cstring: 0x35853
   __TEXT.__const: 0x1f38
-  __TEXT.__gcc_except_tab: 0xb348
-  __TEXT.__oslogstring: 0x20ab9
+  __TEXT.__gcc_except_tab: 0xb3e4
+  __TEXT.__oslogstring: 0x20fac
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x40d

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xa6a8
+  __TEXT.__unwind_info: 0xa738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b58
-  __DATA_CONST.__objc_classlist: 0x1218
+  __DATA_CONST.__const: 0x5b80
+  __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb528
+  __DATA_CONST.__objc_selrefs: 0xb570
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xd50
+  __DATA_CONST.__objc_superrefs: 0xd68
   __DATA_CONST.__objc_arraydata: 0x310
-  __DATA_CONST.__got: 0x4820
-  __AUTH_CONST.__const: 0x1218
-  __AUTH_CONST.__cfstring: 0x1a920
-  __AUTH_CONST.__objc_const: 0x32598
+  __DATA_CONST.__got: 0x4848
+  __AUTH_CONST.__const: 0x1258
+  __AUTH_CONST.__cfstring: 0x1aae0
+  __AUTH_CONST.__objc_const: 0x32998
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2070
-  __AUTH.__objc_data: 0x8d48
+  __AUTH_CONST.__auth_got: 0x2078
+  __AUTH.__objc_data: 0x8e88
   __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x27bc
+  __DATA.__objc_ivar: 0x27dc
   __DATA.__data: 0x189c
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x450
-  __DATA.__bss: 0x13d0
+  __DATA.__bss: 0x13e0
   __DATA_DIRTY.__objc_data: 0x2828
   __DATA_DIRTY.__common: 0x2e0
   __DATA_DIRTY.__bss: 0x211

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12570
-  Symbols:   28296
-  CStrings:  6500
+  Functions: 12623
+  Symbols:   28392
+  CStrings:  6533
 
Symbols:
+ +[AVPlayer _defaultActionAtItemEnd]
+ +[AVQueuePlayer _defaultActionAtItemEnd]
+ -[AVAssetWriterFigAssetWriterNotificationHandler _handleDiskReserveThresholdExhaustedNotification]
+ -[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:]
+ -[AVAudioMixProcessingEffectScheduledParameterEvent dealloc]
+ -[AVPlayer _addFPListeners]
+ -[AVPlayer _updateIsBufferedAirPlayActive:]
+ -[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]
+ -[AVPlayerItem performanceData]
+ -[AVPlayerTransitionPlan .cxx_destruct]
+ -[AVPlayerTransitionPlan incomingItemParameters]
+ -[AVPlayerTransitionPlan init]
+ -[AVPlayerTransitionPlan outgoingItemParameters]
+ -[AVPlayerTransitionPlanIncomingItemParameters applyToAVPlayerItem:]
+ -[AVPlayerTransitionPlanIncomingItemParameters init]
+ -[AVPlayerTransitionPlanIncomingItemParameters seekTime]
+ -[AVPlayerTransitionPlanIncomingItemParameters setSeekTime:]
+ -[AVPlayerTransitionPlanItemParameters .cxx_destruct]
+ -[AVPlayerTransitionPlanItemParameters applyToAVPlayerItem:]
+ -[AVPlayerTransitionPlanItemParameters audioMix]
+ -[AVPlayerTransitionPlanItemParameters setAudioMix:]
+ -[AVPlayerTransitionPlanItemParameters setSpeedRamp:]
+ -[AVPlayerTransitionPlanItemParameters speedRamp]
+ -[AVPlayerTransitionPlanOutgoingItemParameters advanceTimeForOverlappedPlayback]
+ -[AVPlayerTransitionPlanOutgoingItemParameters applyToAVPlayerItem:]
+ -[AVPlayerTransitionPlanOutgoingItemParameters forwardPlaybackEndTime]
+ -[AVPlayerTransitionPlanOutgoingItemParameters init]
+ -[AVPlayerTransitionPlanOutgoingItemParameters overlappedPlaybackEndTime]
+ -[AVPlayerTransitionPlanOutgoingItemParameters setAdvanceTimeForOverlappedPlayback:]
+ -[AVPlayerTransitionPlanOutgoingItemParameters setForwardPlaybackEndTime:]
+ -[AVPlayerTransitionPlanOutgoingItemParameters setOverlappedPlaybackEndTime:]
+ -[AVSystemMuteObserver _evaluateOnSerialQueue]
+ GCC_except_table1006
+ GCC_except_table1012
+ GCC_except_table1017
+ GCC_except_table1019
+ GCC_except_table1023
+ GCC_except_table1026
+ GCC_except_table1029
+ GCC_except_table1031
+ GCC_except_table1036
+ GCC_except_table1038
+ GCC_except_table1049
+ GCC_except_table1053
+ GCC_except_table1057
+ GCC_except_table1062
+ GCC_except_table1067
+ GCC_except_table1069
+ GCC_except_table1072
+ GCC_except_table1076
+ GCC_except_table1078
+ GCC_except_table1081
+ GCC_except_table1084
+ GCC_except_table1088
+ GCC_except_table1092
+ GCC_except_table1096
+ GCC_except_table1100
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table1110
+ GCC_except_table1114
+ GCC_except_table1117
+ GCC_except_table1122
+ GCC_except_table1124
+ GCC_except_table1128
+ GCC_except_table1135
+ GCC_except_table1184
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table156
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table246
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table262
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table297
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table313
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table324
+ GCC_except_table333
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table356
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table400
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table421
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table437
+ GCC_except_table440
+ GCC_except_table443
+ GCC_except_table445
+ GCC_except_table448
+ GCC_except_table457
+ GCC_except_table469
+ GCC_except_table475
+ GCC_except_table478
+ GCC_except_table481
+ GCC_except_table500
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table513
+ GCC_except_table516
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table533
+ GCC_except_table536
+ GCC_except_table540
+ GCC_except_table542
+ GCC_except_table546
+ GCC_except_table551
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table564
+ GCC_except_table565
+ GCC_except_table570
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table584
+ GCC_except_table586
+ GCC_except_table590
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table602
+ GCC_except_table606
+ GCC_except_table608
+ GCC_except_table611
+ GCC_except_table622
+ GCC_except_table627
+ GCC_except_table630
+ GCC_except_table631
+ GCC_except_table646
+ GCC_except_table650
+ GCC_except_table659
+ GCC_except_table661
+ GCC_except_table662
+ GCC_except_table665
+ GCC_except_table667
+ GCC_except_table677
+ GCC_except_table683
+ GCC_except_table687
+ GCC_except_table690
+ GCC_except_table691
+ GCC_except_table695
+ GCC_except_table703
+ GCC_except_table706
+ GCC_except_table710
+ GCC_except_table715
+ GCC_except_table719
+ GCC_except_table729
+ GCC_except_table735
+ GCC_except_table737
+ GCC_except_table740
+ GCC_except_table745
+ GCC_except_table747
+ GCC_except_table749
+ GCC_except_table753
+ GCC_except_table758
+ GCC_except_table763
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table774
+ GCC_except_table779
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table790
+ GCC_except_table792
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table807
+ GCC_except_table812
+ GCC_except_table814
+ GCC_except_table816
+ GCC_except_table819
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table830
+ GCC_except_table831
+ GCC_except_table839
+ GCC_except_table843
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table851
+ GCC_except_table854
+ GCC_except_table863
+ GCC_except_table867
+ GCC_except_table869
+ GCC_except_table872
+ GCC_except_table874
+ GCC_except_table879
+ GCC_except_table882
+ GCC_except_table884
+ GCC_except_table887
+ GCC_except_table890
+ GCC_except_table894
+ GCC_except_table897
+ GCC_except_table900
+ GCC_except_table906
+ GCC_except_table908
+ GCC_except_table910
+ GCC_except_table912
+ GCC_except_table914
+ GCC_except_table916
+ GCC_except_table919
+ GCC_except_table928
+ GCC_except_table932
+ GCC_except_table940
+ GCC_except_table958
+ GCC_except_table962
+ GCC_except_table964
+ GCC_except_table966
+ GCC_except_table968
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table974
+ GCC_except_table977
+ GCC_except_table979
+ GCC_except_table981
+ GCC_except_table983
+ GCC_except_table994
+ _AVAssetWriterFigAssetWriterHandleDiskReserveThresholdExhaustedNotification
+ _AVPlannerEncoderSupportsResumable
+ _AVPlannerEncoderTemporarilyUnavailableError.sError
+ _AVPlannerEncoderTemporarilyUnavailableError.sOnce
+ _AVPlayerTransitionPlanCommitErrorPartialApplicationKey
+ _AVPlayerTransitionPlanCommitErrorRequiresCleanup
+ _OBJC_CLASS_$_AVPlayerTransitionPlan
+ _OBJC_CLASS_$_AVPlayerTransitionPlanIncomingItemParameters
+ _OBJC_CLASS_$_AVPlayerTransitionPlanItemParameters
+ _OBJC_CLASS_$_AVPlayerTransitionPlanOutgoingItemParameters
+ _OBJC_IVAR_$_AVPlayerInternal.bufferedAirPlayActiveNotifiedSinceSubscribe
+ _OBJC_IVAR_$_AVPlayerTransitionPlan._incomingItemParameters
+ _OBJC_IVAR_$_AVPlayerTransitionPlan._outgoingItemParameters
+ _OBJC_IVAR_$_AVPlayerTransitionPlanIncomingItemParameters._seekTime
+ _OBJC_IVAR_$_AVPlayerTransitionPlanItemParameters._audioMix
+ _OBJC_IVAR_$_AVPlayerTransitionPlanItemParameters._speedRamp
+ _OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._advanceTimeForOverlappedPlayback
+ _OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._forwardPlaybackEndTime
+ _OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._overlappedPlaybackEndTime
+ _OBJC_METACLASS_$_AVPlayerTransitionPlan
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanIncomingItemParameters
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanItemParameters
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanOutgoingItemParameters
+ _OUTLINED_FUNCTION_143
+ _OUTLINED_FUNCTION_144
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_146
+ __AXSAutomaticSubtitlesShowWhenLanguageMismatch
+ __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
+ __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerTransitionPlan
+ __OBJC_$_INSTANCE_METHODS_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_$_INSTANCE_METHODS_AVPlayerTransitionPlanItemParameters
+ __OBJC_$_INSTANCE_METHODS_AVPlayerTransitionPlanOutgoingItemParameters
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerTransitionPlan
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerTransitionPlanItemParameters
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerTransitionPlanOutgoingItemParameters
+ __OBJC_$_PROP_LIST_AVPlayerTransitionPlan
+ __OBJC_$_PROP_LIST_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_$_PROP_LIST_AVPlayerTransitionPlanItemParameters
+ __OBJC_$_PROP_LIST_AVPlayerTransitionPlanOutgoingItemParameters
+ __OBJC_CLASS_PROTOCOLS_$_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlan
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanItemParameters
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanOutgoingItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlan
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanOutgoingItemParameters
+ ___16-[AVPlayer init]_block_invoke
+ ___16-[AVPlayer init]_block_invoke_2
+ ___16-[AVPlayer init]_block_invoke_3
+ ___16-[AVPlayer init]_block_invoke_4
+ ___16-[AVPlayer init]_block_invoke_5
+ ___16-[AVPlayer init]_block_invoke_6
+ ___33-[AVSystemMuteObserver _evaluate]_block_invoke
+ ___43-[AVPlayer _updateIsBufferedAirPlayActive:]_block_invoke
+ ___43-[AVPlayer _updateIsBufferedAirPlayActive:]_block_invoke_2
+ ___68-[AVPlayerTransitionPlanIncomingItemParameters applyToAVPlayerItem:]_block_invoke
+ ___89-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:]_block_invoke
+ ___89-[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]_block_invoke
+ ___AVPlannerEncoderTemporarilyUnavailableError_block_invoke
+ ___block_descriptor_32_e8_v12?0B8l
+ _kFigAssetWriterNotification_DiskReserveThresholdExhausted
+ _kFigPlaybackItemProperty_PerformanceDictionary
+ _kFigPlaybackItemProperty_SuppressAudioRendering
+ _objc_msgSend$_defaultActionAtItemEnd
+ _objc_msgSend$_evaluateOnSerialQueue
+ _objc_msgSend$_handleDiskReserveThresholdExhaustedNotification
+ _objc_msgSend$_makeFinishWritingOperationsWithDiskFullErrorLastOperation:
+ _objc_msgSend$_updateIsBufferedAirPlayActive:
+ _objc_msgSend$applyToAVPlayerItem:
+ _objc_msgSend$incomingItemParameters
+ _objc_msgSend$outgoingItemParameters
+ _objc_msgSend$seekTime
+ _objc_msgSend$setAllowsLegibleFallbackForAllAudibleMediaSelections:
+ _objc_msgSend$setSpeedRamp:
+ _objc_msgSend$speedRamp
- -[AVPlayer _addFPListenersForFigPlayer:]
- -[AVPlayer initWithActionAtItemEnd:]
- -[AVQueuePlayer _defaultActionAtItemEnd]
- GCC_except_table1005
- GCC_except_table1011
- GCC_except_table1016
- GCC_except_table1018
- GCC_except_table1020
- GCC_except_table1025
- GCC_except_table1028
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1037
- GCC_except_table1048
- GCC_except_table1052
- GCC_except_table1056
- GCC_except_table1061
- GCC_except_table1065
- GCC_except_table1068
- GCC_except_table1070
- GCC_except_table1074
- GCC_except_table1077
- GCC_except_table1080
- GCC_except_table1083
- GCC_except_table1087
- GCC_except_table1091
- GCC_except_table1095
- GCC_except_table1099
- GCC_except_table1103
- GCC_except_table1106
- GCC_except_table1109
- GCC_except_table1113
- GCC_except_table1116
- GCC_except_table1121
- GCC_except_table1123
- GCC_except_table1126
- GCC_except_table1134
- GCC_except_table1183
- GCC_except_table132
- GCC_except_table137
- GCC_except_table154
- GCC_except_table184
- GCC_except_table186
- GCC_except_table221
- GCC_except_table226
- GCC_except_table234
- GCC_except_table238
- GCC_except_table239
- GCC_except_table242
- GCC_except_table254
- GCC_except_table256
- GCC_except_table259
- GCC_except_table261
- GCC_except_table266
- GCC_except_table268
- GCC_except_table270
- GCC_except_table273
- GCC_except_table275
- GCC_except_table277
- GCC_except_table278
- GCC_except_table280
- GCC_except_table288
- GCC_except_table291
- GCC_except_table296
- GCC_except_table302
- GCC_except_table307
- GCC_except_table310
- GCC_except_table312
- GCC_except_table318
- GCC_except_table320
- GCC_except_table322
- GCC_except_table326
- GCC_except_table332
- GCC_except_table335
- GCC_except_table337
- GCC_except_table341
- GCC_except_table342
- GCC_except_table344
- GCC_except_table352
- GCC_except_table353
- GCC_except_table355
- GCC_except_table357
- GCC_except_table361
- GCC_except_table362
- GCC_except_table365
- GCC_except_table370
- GCC_except_table374
- GCC_except_table381
- GCC_except_table387
- GCC_except_table389
- GCC_except_table393
- GCC_except_table396
- GCC_except_table399
- GCC_except_table401
- GCC_except_table402
- GCC_except_table404
- GCC_except_table413
- GCC_except_table414
- GCC_except_table417
- GCC_except_table420
- GCC_except_table422
- GCC_except_table425
- GCC_except_table426
- GCC_except_table430
- GCC_except_table434
- GCC_except_table439
- GCC_except_table441
- GCC_except_table442
- GCC_except_table444
- GCC_except_table446
- GCC_except_table450
- GCC_except_table456
- GCC_except_table463
- GCC_except_table464
- GCC_except_table466
- GCC_except_table479
- GCC_except_table501
- GCC_except_table506
- GCC_except_table510
- GCC_except_table515
- GCC_except_table520
- GCC_except_table522
- GCC_except_table528
- GCC_except_table530
- GCC_except_table532
- GCC_except_table534
- GCC_except_table538
- GCC_except_table541
- GCC_except_table544
- GCC_except_table547
- GCC_except_table549
- GCC_except_table552
- GCC_except_table557
- GCC_except_table559
- GCC_except_table563
- GCC_except_table567
- GCC_except_table571
- GCC_except_table576
- GCC_except_table578
- GCC_except_table585
- GCC_except_table587
- GCC_except_table591
- GCC_except_table595
- GCC_except_table596
- GCC_except_table603
- GCC_except_table624
- GCC_except_table628
- GCC_except_table632
- GCC_except_table633
- GCC_except_table634
- GCC_except_table637
- GCC_except_table655
- GCC_except_table660
- GCC_except_table663
- GCC_except_table666
- GCC_except_table668
- GCC_except_table671
- GCC_except_table676
- GCC_except_table678
- GCC_except_table680
- GCC_except_table684
- GCC_except_table686
- GCC_except_table688
- GCC_except_table693
- GCC_except_table697
- GCC_except_table702
- GCC_except_table705
- GCC_except_table707
- GCC_except_table708
- GCC_except_table714
- GCC_except_table717
- GCC_except_table721
- GCC_except_table722
- GCC_except_table723
- GCC_except_table730
- GCC_except_table736
- GCC_except_table739
- GCC_except_table741
- GCC_except_table742
- GCC_except_table744
- GCC_except_table746
- GCC_except_table751
- GCC_except_table754
- GCC_except_table756
- GCC_except_table769
- GCC_except_table772
- GCC_except_table781
- GCC_except_table784
- GCC_except_table786
- GCC_except_table791
- GCC_except_table794
- GCC_except_table797
- GCC_except_table799
- GCC_except_table801
- GCC_except_table805
- GCC_except_table808
- GCC_except_table813
- GCC_except_table817
- GCC_except_table820
- GCC_except_table822
- GCC_except_table824
- GCC_except_table825
- GCC_except_table836
- GCC_except_table837
- GCC_except_table840
- GCC_except_table845
- GCC_except_table848
- GCC_except_table850
- GCC_except_table853
- GCC_except_table862
- GCC_except_table865
- GCC_except_table868
- GCC_except_table871
- GCC_except_table873
- GCC_except_table875
- GCC_except_table880
- GCC_except_table885
- GCC_except_table888
- GCC_except_table891
- GCC_except_table895
- GCC_except_table898
- GCC_except_table905
- GCC_except_table907
- GCC_except_table909
- GCC_except_table911
- GCC_except_table913
- GCC_except_table915
- GCC_except_table918
- GCC_except_table926
- GCC_except_table931
- GCC_except_table938
- GCC_except_table957
- GCC_except_table961
- GCC_except_table963
- GCC_except_table965
- GCC_except_table967
- GCC_except_table969
- GCC_except_table971
- GCC_except_table973
- GCC_except_table976
- GCC_except_table978
- GCC_except_table980
- GCC_except_table982
- GCC_except_table993
- _OBJC_IVAR_$_AVAssetTrackPlanExecutor._encoderSupportedProperties
- __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- __OBJC_CLASS_PROTOCOLS_$_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke_2
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke_3
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke_4
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke_5
- _objc_msgSend$_addFPListenersForFigPlayer:
- _objc_msgSend$initWithActionAtItemEnd:
CStrings:
+ "-[AVAssetWriterHelper isProVideoStorageSupported]"
+ "-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:]_block_invoke"
+ "-[AVAssetWriterWritingHelper didReceiveFigAssetWriterNotificationWithSuccess:error:]"
+ "-[AVMetadataItem(AVMetadataItemTypeCoercion) dataValue]"
+ "-[AVPlayer init]"
+ "-[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]_block_invoke"
+ "-[AVSystemMuteObserver _evaluateOnSerialQueue]"
+ "<<<< AVAssetWriter >>>> %s: (%p) Disk reserve exhausted. Initiating graceful finish with error."
+ "<<<< AVAssetWriter >>>> %s: (%p) success=%d error=%@"
+ "<<<< AVAssetWriter >>>> %s: ProVideoStorage, early stop error operation executing — reporting failure with %@"
+ "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported by system"
+ "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported when output file is on external storage"
+ "<<<< AVAssetWriter >>>> %s: returning NO because pro video storage is unsupported without output URL"
+ "<<<< AVAssetWriter >>>> %s: returning YES"
+ "<<<< AVMetadataItem >>>> %s: AVMetadataItem dataValue: dropping malformed NSData %p (length=%lu, bytes=NULL)"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> Beginning committing plan from outgoing item %@ to incoming item %@ (advanceTimeForOverlappedPlayback %1.3f)"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> Completed committing plan from outgoing item %@ to incoming item %@"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> Player deallocated"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> Unable to read reconciled version of IsBufferedAirPlayActive, err %d"
+ "<<<< AVPlayer >>>> %s: <%{public}@|%p> reconciling IsBufferedAirPlayActive across the read/subscribe window: latest=%d"
+ "AVAssetWriterFigAssetWriterHandleDiskReserveThresholdExhaustedNotification"
+ "AVErrorNotEnoughSpaceForProVideoStorageReplenishment"
+ "AVErrorTransitionPlanInvalidConfiguration"
+ "AVErrorTransitionPlanItemsNotInExpectedQueueOrder"
+ "AVPlayerTransitionPlanCommitErrorPartialApplication"
+ "Attempt to set UsesProVideoStorage to YES when isProVideoStorageSupported returns NO."
+ "Cannot call createResumableCompressionSessionWithAllocator more than once."
+ "Cannot call resumableAssetWriterInputWithMediaType more than once."
+ "Recording stopped because the disk reserve threshold was exhausted"
+ "Report early stop error (ProVideoStorage threshold exhausted)"
+ "advanceTimeForOverlappedPlayback must be <= overlappedPlaybackEndTime"
+ "commitTransitionPlan: requires AVQueuePlayer"
+ "incomingItem has no FigPlaybackItem; cannot commit"
+ "incomingItem must be the next item after outgoingItem in the queue"
+ "outgoingItem and incomingItem must both be in the player's queue"
+ "player has no FigPlayer; cannot commit"
- "-[AVPlayer initWithActionAtItemEnd:]"
- "-[AVSystemMuteObserver _evaluate]"
- "Cannot use the virtual capture card"
```
