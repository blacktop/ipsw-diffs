## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

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
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2450.67.3.0.0
-  __TEXT.__text: 0x20cdc0
-  __TEXT.__objc_methlist: 0x1bbcc
+2450.71.1.0.0
+  __TEXT.__text: 0x20f1bc
+  __TEXT.__objc_methlist: 0x1bd54
   __TEXT.__const: 0x201c
-  __TEXT.__gcc_except_tab: 0xab1c
-  __TEXT.__cstring: 0x343fb
-  __TEXT.__oslogstring: 0x1ce8f
+  __TEXT.__gcc_except_tab: 0xabbc
+  __TEXT.__cstring: 0x3496b
+  __TEXT.__oslogstring: 0x1d21d
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x41a
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xa468
+  __TEXT.__unwind_info: 0xa4e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x34d0
-  __DATA_CONST.__objc_classlist: 0x1238
+  __DATA_CONST.__const: 0x34f8
+  __DATA_CONST.__objc_classlist: 0x1258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb0f8
+  __DATA_CONST.__objc_selrefs: 0xb138
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xd70
+  __DATA_CONST.__objc_superrefs: 0xd88
   __DATA_CONST.__objc_arraydata: 0x308
-  __DATA_CONST.__got: 0x4660
-  __AUTH_CONST.__const: 0x3c30
-  __AUTH_CONST.__cfstring: 0x1aea0
-  __AUTH_CONST.__objc_const: 0x32390
+  __DATA_CONST.__got: 0x4688
+  __AUTH_CONST.__const: 0x3c70
+  __AUTH_CONST.__cfstring: 0x1b080
+  __AUTH_CONST.__objc_const: 0x32790
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1e58
-  __AUTH.__objc_data: 0x8e10
+  __AUTH_CONST.__auth_got: 0x1e60
+  __AUTH.__objc_data: 0x8f50
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x277c
+  __DATA.__objc_ivar: 0x279c
   __DATA.__data: 0x1700
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x430
-  __DATA.__bss: 0x1360
+  __DATA.__bss: 0x1370
   __DATA_DIRTY.__objc_data: 0x28a0
   __DATA_DIRTY.__common: 0x2e0
   __DATA_DIRTY.__bss: 0x1b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12380
-  Symbols:   28003
-  CStrings:  6266
+  Functions: 12423
+  Symbols:   28094
+  CStrings:  6294
 
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
+ AVPlannerEncoderTemporarilyUnavailableError.sError
+ AVPlannerEncoderTemporarilyUnavailableError.sOnce
+ GCC_except_table1005
+ GCC_except_table1007
+ GCC_except_table1009
+ GCC_except_table1011
+ GCC_except_table1013
+ GCC_except_table1016
+ GCC_except_table1018
+ GCC_except_table1020
+ GCC_except_table1022
+ GCC_except_table1033
+ GCC_except_table1045
+ GCC_except_table1051
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1062
+ GCC_except_table1065
+ GCC_except_table1068
+ GCC_except_table1070
+ GCC_except_table1082
+ GCC_except_table1086
+ GCC_except_table1090
+ GCC_except_table1095
+ GCC_except_table1099
+ GCC_except_table1101
+ GCC_except_table1104
+ GCC_except_table1107
+ GCC_except_table1111
+ GCC_except_table1115
+ GCC_except_table1119
+ GCC_except_table1123
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1133
+ GCC_except_table1137
+ GCC_except_table1139
+ GCC_except_table1144
+ GCC_except_table1146
+ GCC_except_table1150
+ GCC_except_table1159
+ GCC_except_table1212
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table203
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table260
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table279
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table299
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table319
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table331
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table342
+ GCC_except_table347
+ GCC_except_table350
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table370
+ GCC_except_table372
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table399
+ GCC_except_table408
+ GCC_except_table411
+ GCC_except_table414
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table423
+ GCC_except_table425
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table436
+ GCC_except_table438
+ GCC_except_table439
+ GCC_except_table441
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table460
+ GCC_except_table461
+ GCC_except_table469
+ GCC_except_table471
+ GCC_except_table474
+ GCC_except_table477
+ GCC_except_table481
+ GCC_except_table485
+ GCC_except_table490
+ GCC_except_table495
+ GCC_except_table500
+ GCC_except_table508
+ GCC_except_table526
+ GCC_except_table529
+ GCC_except_table539
+ GCC_except_table540
+ GCC_except_table542
+ GCC_except_table545
+ GCC_except_table549
+ GCC_except_table553
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table559
+ GCC_except_table572
+ GCC_except_table574
+ GCC_except_table577
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table588
+ GCC_except_table590
+ GCC_except_table603
+ GCC_except_table606
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table616
+ GCC_except_table618
+ GCC_except_table621
+ GCC_except_table626
+ GCC_except_table628
+ GCC_except_table631
+ GCC_except_table634
+ GCC_except_table635
+ GCC_except_table640
+ GCC_except_table642
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table658
+ GCC_except_table661
+ GCC_except_table665
+ GCC_except_table666
+ GCC_except_table672
+ GCC_except_table674
+ GCC_except_table676
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table687
+ GCC_except_table691
+ GCC_except_table693
+ GCC_except_table695
+ GCC_except_table696
+ GCC_except_table699
+ GCC_except_table700
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table712
+ GCC_except_table716
+ GCC_except_table726
+ GCC_except_table727
+ GCC_except_table729
+ GCC_except_table731
+ GCC_except_table739
+ GCC_except_table747
+ GCC_except_table751
+ GCC_except_table755
+ GCC_except_table757
+ GCC_except_table761
+ GCC_except_table763
+ GCC_except_table766
+ GCC_except_table771
+ GCC_except_table775
+ GCC_except_table779
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table789
+ GCC_except_table791
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table800
+ GCC_except_table802
+ GCC_except_table805
+ GCC_except_table808
+ GCC_except_table811
+ GCC_except_table815
+ GCC_except_table818
+ GCC_except_table822
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table829
+ GCC_except_table832
+ GCC_except_table835
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table855
+ GCC_except_table869
+ GCC_except_table871
+ GCC_except_table874
+ GCC_except_table877
+ GCC_except_table879
+ GCC_except_table88
+ GCC_except_table882
+ GCC_except_table889
+ GCC_except_table891
+ GCC_except_table894
+ GCC_except_table897
+ GCC_except_table900
+ GCC_except_table902
+ GCC_except_table904
+ GCC_except_table906
+ GCC_except_table910
+ GCC_except_table915
+ GCC_except_table918
+ GCC_except_table922
+ GCC_except_table925
+ GCC_except_table928
+ GCC_except_table934
+ GCC_except_table936
+ GCC_except_table938
+ GCC_except_table940
+ GCC_except_table944
+ GCC_except_table948
+ GCC_except_table951
+ GCC_except_table963
+ GCC_except_table965
+ GCC_except_table971
+ GCC_except_table975
+ GCC_except_table978
+ GCC_except_table987
+ OBJC_IVAR_$_AVPlayerInternal.bufferedAirPlayActiveNotifiedSinceSubscribe
+ OBJC_IVAR_$_AVPlayerTransitionPlan._incomingItemParameters
+ OBJC_IVAR_$_AVPlayerTransitionPlan._outgoingItemParameters
+ OBJC_IVAR_$_AVPlayerTransitionPlanIncomingItemParameters._seekTime
+ OBJC_IVAR_$_AVPlayerTransitionPlanItemParameters._audioMix
+ OBJC_IVAR_$_AVPlayerTransitionPlanItemParameters._speedRamp
+ OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._advanceTimeForOverlappedPlayback
+ OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._forwardPlaybackEndTime
+ OBJC_IVAR_$_AVPlayerTransitionPlanOutgoingItemParameters._overlappedPlaybackEndTime
+ _AVAssetWriterFigAssetWriterHandleDiskReserveThresholdExhaustedNotification
+ _AVPlannerEncoderSupportsResumable
+ _AVPlayerTransitionPlanCommitErrorPartialApplicationKey
+ _AVPlayerTransitionPlanCommitErrorRequiresCleanup
+ _OBJC_CLASS_$_AVPlayerTransitionPlan
+ _OBJC_CLASS_$_AVPlayerTransitionPlanIncomingItemParameters
+ _OBJC_CLASS_$_AVPlayerTransitionPlanItemParameters
+ _OBJC_CLASS_$_AVPlayerTransitionPlanOutgoingItemParameters
+ _OBJC_METACLASS_$_AVPlayerTransitionPlan
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanIncomingItemParameters
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanItemParameters
+ _OBJC_METACLASS_$_AVPlayerTransitionPlanOutgoingItemParameters
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ __16-[AVPlayer init]_block_invoke
+ __43-[AVPlayer _updateIsBufferedAirPlayActive:]_block_invoke
+ __AXSAutomaticSubtitlesShowWhenLanguageMismatch
+ __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
+ __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
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
+ __OBJC_CLASS_PROTOCOLS_$_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation|AVPlayerTransitionPlan)
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlan
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanItemParameters
+ __OBJC_CLASS_RO_$_AVPlayerTransitionPlanOutgoingItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlan
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanIncomingItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanItemParameters
+ __OBJC_METACLASS_RO_$_AVPlayerTransitionPlanOutgoingItemParameters
+ ___16-[AVPlayer init]_block_invoke
+ ___43-[AVPlayer _updateIsBufferedAirPlayActive:]_block_invoke
+ ___51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke_2
+ ___68-[AVPlayerTransitionPlanIncomingItemParameters applyToAVPlayerItem:]_block_invoke
+ ___89-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:]_block_invoke
+ ___89-[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]_block_invoke
+ ___AVPlannerEncoderTemporarilyUnavailableError_block_invoke
+ ___block_descriptor_32_e8_v12?0B8l
+ _kFigAssetWriterNotification_DiskReserveThresholdExhausted
+ _kFigPlaybackItemProperty_PerformanceDictionary
+ _kFigPlaybackItemProperty_SuppressAudioRendering
+ _objc_msgSend$_defaultActionAtItemEnd
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
- GCC_except_table1004
- GCC_except_table1006
- GCC_except_table1008
- GCC_except_table1010
- GCC_except_table1012
- GCC_except_table1015
- GCC_except_table1017
- GCC_except_table1019
- GCC_except_table1021
- GCC_except_table1032
- GCC_except_table1044
- GCC_except_table1050
- GCC_except_table1055
- GCC_except_table1057
- GCC_except_table1059
- GCC_except_table1064
- GCC_except_table1067
- GCC_except_table1069
- GCC_except_table1081
- GCC_except_table1085
- GCC_except_table1089
- GCC_except_table1094
- GCC_except_table1097
- GCC_except_table1100
- GCC_except_table1103
- GCC_except_table1106
- GCC_except_table1110
- GCC_except_table1114
- GCC_except_table1118
- GCC_except_table1122
- GCC_except_table1126
- GCC_except_table1129
- GCC_except_table1132
- GCC_except_table1136
- GCC_except_table1138
- GCC_except_table1143
- GCC_except_table1145
- GCC_except_table1148
- GCC_except_table1158
- GCC_except_table1211
- GCC_except_table137
- GCC_except_table158
- GCC_except_table172
- GCC_except_table197
- GCC_except_table209
- GCC_except_table231
- GCC_except_table234
- GCC_except_table236
- GCC_except_table237
- GCC_except_table241
- GCC_except_table245
- GCC_except_table249
- GCC_except_table253
- GCC_except_table256
- GCC_except_table257
- GCC_except_table258
- GCC_except_table264
- GCC_except_table268
- GCC_except_table271
- GCC_except_table273
- GCC_except_table275
- GCC_except_table278
- GCC_except_table282
- GCC_except_table285
- GCC_except_table287
- GCC_except_table289
- GCC_except_table292
- GCC_except_table297
- GCC_except_table300
- GCC_except_table302
- GCC_except_table305
- GCC_except_table307
- GCC_except_table308
- GCC_except_table310
- GCC_except_table312
- GCC_except_table315
- GCC_except_table324
- GCC_except_table326
- GCC_except_table329
- GCC_except_table332
- GCC_except_table334
- GCC_except_table337
- GCC_except_table340
- GCC_except_table349
- GCC_except_table351
- GCC_except_table353
- GCC_except_table358
- GCC_except_table360
- GCC_except_table364
- GCC_except_table369
- GCC_except_table371
- GCC_except_table379
- GCC_except_table381
- GCC_except_table384
- GCC_except_table389
- GCC_except_table391
- GCC_except_table392
- GCC_except_table395
- GCC_except_table404
- GCC_except_table407
- GCC_except_table410
- GCC_except_table412
- GCC_except_table413
- GCC_except_table415
- GCC_except_table416
- GCC_except_table424
- GCC_except_table428
- GCC_except_table430
- GCC_except_table431
- GCC_except_table433
- GCC_except_table440
- GCC_except_table442
- GCC_except_table443
- GCC_except_table445
- GCC_except_table446
- GCC_except_table454
- GCC_except_table456
- GCC_except_table462
- GCC_except_table467
- GCC_except_table470
- GCC_except_table472
- GCC_except_table475
- GCC_except_table476
- GCC_except_table482
- GCC_except_table487
- GCC_except_table492
- GCC_except_table497
- GCC_except_table502
- GCC_except_table523
- GCC_except_table524
- GCC_except_table527
- GCC_except_table530
- GCC_except_table532
- GCC_except_table541
- GCC_except_table546
- GCC_except_table548
- GCC_except_table551
- GCC_except_table554
- GCC_except_table556
- GCC_except_table558
- GCC_except_table573
- GCC_except_table575
- GCC_except_table578
- GCC_except_table580
- GCC_except_table583
- GCC_except_table589
- GCC_except_table594
- GCC_except_table597
- GCC_except_table605
- GCC_except_table608
- GCC_except_table611
- GCC_except_table619
- GCC_except_table622
- GCC_except_table624
- GCC_except_table625
- GCC_except_table627
- GCC_except_table636
- GCC_except_table641
- GCC_except_table645
- GCC_except_table647
- GCC_except_table648
- GCC_except_table650
- GCC_except_table660
- GCC_except_table662
- GCC_except_table663
- GCC_except_table669
- GCC_except_table675
- GCC_except_table677
- GCC_except_table680
- GCC_except_table681
- GCC_except_table684
- GCC_except_table689
- GCC_except_table692
- GCC_except_table694
- GCC_except_table697
- GCC_except_table702
- GCC_except_table704
- GCC_except_table706
- GCC_except_table713
- GCC_except_table724
- GCC_except_table728
- GCC_except_table732
- GCC_except_table733
- GCC_except_table737
- GCC_except_table740
- GCC_except_table743
- GCC_except_table749
- GCC_except_table753
- GCC_except_table756
- GCC_except_table759
- GCC_except_table762
- GCC_except_table765
- GCC_except_table768
- GCC_except_table770
- GCC_except_table773
- GCC_except_table777
- GCC_except_table780
- GCC_except_table782
- GCC_except_table785
- GCC_except_table787
- GCC_except_table792
- GCC_except_table795
- GCC_except_table798
- GCC_except_table801
- GCC_except_table804
- GCC_except_table807
- GCC_except_table810
- GCC_except_table814
- GCC_except_table817
- GCC_except_table820
- GCC_except_table823
- GCC_except_table825
- GCC_except_table828
- GCC_except_table831
- GCC_except_table834
- GCC_except_table837
- GCC_except_table839
- GCC_except_table841
- GCC_except_table846
- GCC_except_table848
- GCC_except_table854
- GCC_except_table868
- GCC_except_table870
- GCC_except_table873
- GCC_except_table876
- GCC_except_table878
- GCC_except_table881
- GCC_except_table887
- GCC_except_table890
- GCC_except_table893
- GCC_except_table896
- GCC_except_table899
- GCC_except_table901
- GCC_except_table903
- GCC_except_table905
- GCC_except_table909
- GCC_except_table913
- GCC_except_table916
- GCC_except_table919
- GCC_except_table92
- GCC_except_table923
- GCC_except_table926
- GCC_except_table933
- GCC_except_table935
- GCC_except_table937
- GCC_except_table939
- GCC_except_table943
- GCC_except_table947
- GCC_except_table950
- GCC_except_table962
- GCC_except_table964
- GCC_except_table969
- GCC_except_table974
- GCC_except_table977
- GCC_except_table985
- OBJC_IVAR_$_AVAssetTrackPlanExecutor._encoderSupportedProperties
- __51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke
- __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- __OBJC_CLASS_PROTOCOLS_$_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAllowsCaptureOfClearKeyVideo|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerSTSLabel|AVPlayerPIPSupport|AVPlayerSystemMute|FigVideoTargetSupport|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerResourceArbitrationSupport|AVPlayerRoutingPlaybackArbitrationSupport|AVPlayerLegibleFallback|AVPlayerAdvanceWithOverlap|AVPlayer_OverlapPlaybackConditions|AVPlayerSpeedRamp|AVPlayer_ForTestingOnly|AVPlayerLocalCoplayback|AVPlayerAudioSubmixTapping|AVPlayerObservation|AVPlayer_Observation)
- ___36-[AVPlayer initWithActionAtItemEnd:]_block_invoke
- _objc_msgSend$_addFPListenersForFigPlayer:
- _objc_msgSend$initWithActionAtItemEnd:
CStrings:
+ "-[AVAssetWriterWritingHelper _makeFinishWritingOperationsWithDiskFullErrorLastOperation:]_block_invoke"
+ "-[AVAssetWriterWritingHelper didReceiveFigAssetWriterNotificationWithSuccess:error:]"
+ "-[AVMetadataItem(AVMetadataItemTypeCoercion) dataValue]"
+ "-[AVPlayer init]"
+ "-[AVPlayer(AVPlayerTransitionPlan) commitTransitionPlan:outgoingItem:incomingItem:error:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XbVmRt/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
+ "<<<< AVAssetWriter >>>> %s: (%p) Disk reserve exhausted. Initiating graceful finish with error."
+ "<<<< AVAssetWriter >>>> %s: (%p) success=%d error=%@"
+ "<<<< AVAssetWriter >>>> %s: ProVideoStorage, early stop error operation executing — reporting failure with %@"
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
+ "An AVSampleBufferAudioRenderer, configured to request more media data via requestMediaDataWhenReadyOnQueue:usingBlock:, was released without first having been messaged stopRequestingMediaData."
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVAssetTrack.m %s: %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d timeRange.start: %.3f timeRange.duration: %.3f duration: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVCompositionTrack.m %s: [%p] called mutableComposition: %p destTrackID: %d track: %p timeRange.start: %.3f timeRange.duration: %.3f startTime: %.3f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> beginning suspension with reason %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> ending figSuspension %p proposing new time %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting pauseSnapsToMediaTimeOfOrginator:%@ on playback coordinator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: <%p> setting waiting policies %@ on playback coordinator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Error creating timeline coordinator: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator gave a participantID which is not present in otherParticipants"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming state from the outside is better."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for DidIssueCommandToTimelineControl notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for ParticipantsChanged notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: called (self = %@, for SuspensionReasonsChanged notification, with payload = %@)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: skipping updating transport control state cache since the lamport timestamp for the update is older or the update is not authoritative"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: updating transport control state cache for item identifier %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Alternate group ID value passed to setAlternateGroupID: is too large."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: CFNumberCreate returned a NULL number."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: FigCreate3x3MatrixArrayFromCGAffineTransform returned a NULL matrix."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVMovieTrack.m %s: Layer value passed to setLayer: is too large."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: CVPixelBufferPoolCreatePixelBufferWithAuxAttributes failed (error %d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: Failed to resolve pixel buffer attributes (error %d), required client attributes %@, desired destination attributes %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: initializing"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_BlendingTransferFunction = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredAttributes = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredColorPrimaries = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredTransferFunction = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_DestinationPixelBufferDesiredYCbCrMatrix = %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_HighQualityRendering = %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderDimensions = %d %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderEdgeProcessingPixels = %f %f %f %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderPixelAspectRatio = %d %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/AVVideoCompositionRenderContext.m %s: kFigVideoCompositorProperty_RenderScale = %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Invalid source format flags - not one of the supported lossless bit depths"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVAudioOutputSettings.m %s: Need to either provide fully-formed dictionary or source format description"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.w5Cum4/Sources/AVFoundation_AVFCore/Fig/Utilities/AVBundleResources.m %s: AVLocalizedStringFromTableWithLocaleWithBundleIdentifier unable to find a localized string; returning an empty string"
- "\xf1"
```
