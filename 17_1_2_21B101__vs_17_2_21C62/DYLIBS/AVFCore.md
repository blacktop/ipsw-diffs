## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2215.13.4.0.0
-  __TEXT.__text: 0x18c3e0
-  __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x180e0
-  __TEXT.__cstring: 0x22064
+2220.14.1.0.0
+  __TEXT.__text: 0x18d390
+  __TEXT.__auth_stubs: 0x3200
+  __TEXT.__objc_methlist: 0x182e0
+  __TEXT.__cstring: 0x223d9
   __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x40e0
-  __TEXT.__oslogstring: 0x75a5
+  __TEXT.__gcc_except_tab: 0x40a8
+  __TEXT.__oslogstring: 0x75e2
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x7f7c
-  __TEXT.__objc_classname: 0x59c9
-  __TEXT.__objc_methname: 0x2ffb8
-  __TEXT.__objc_methtype: 0x977d
-  __TEXT.__objc_stubs: 0x1d9c0
-  __DATA_CONST.__got: 0x3a58
-  __DATA_CONST.__const: 0x5138
-  __DATA_CONST.__objc_classlist: 0xff0
+  __TEXT.__unwind_info: 0x7fb0
+  __TEXT.__objc_classname: 0x5a2f
+  __TEXT.__objc_methname: 0x3037c
+  __TEXT.__objc_methtype: 0x98e8
+  __TEXT.__objc_stubs: 0x1dba0
+  __DATA_CONST.__got: 0x3a98
+  __DATA_CONST.__const: 0x5260
+  __DATA_CONST.__objc_classlist: 0x1008
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x253c0
-  __DATA_CONST.__objc_selrefs: 0x9808
+  __DATA_CONST.__objc_const: 0x25560
+  __DATA_CONST.__objc_selrefs: 0x98b8
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__objc_const: 0xa550
-  __AUTH_CONST.__cfstring: 0x161c0
+  __AUTH_CONST.__objc_const: 0xa670
+  __AUTH_CONST.__cfstring: 0x16340
   __AUTH_CONST.__const: 0xc38
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__auth_got: 0x1900
-  __AUTH.__objc_data: 0x61d0
+  __AUTH_CONST.__auth_got: 0x1910
+  __AUTH.__objc_data: 0x62c0
   __AUTH.__data: 0x138
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1128
-  __DATA.__objc_superrefs: 0xb18
-  __DATA.__objc_ivar: 0x2130
+  __DATA.__objc_classrefs: 0x1140
+  __DATA.__objc_superrefs: 0xb30
+  __DATA.__objc_ivar: 0x213c
   __DATA.__data: 0x1db8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x1a8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9969
-  Symbols:   34958
-  CStrings:  12373
+  Functions: 10007
+  Symbols:   35095
+  CStrings:  12425
 
Symbols:
+ +[AVPlayerTaggedBufferOutput taggedBufferOutputWithVideoOutput:]
+ -[AVPlayer(AVPlayerOutputSupport) setVideoOutput:]
+ -[AVPlayer(AVPlayerOutputSupport) videoOutput]
+ -[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]
+ -[AVPlayerItem _updateReportingValuesOnFigPlaybackItem]
+ -[AVPlayerItem _updateReportingValuesProperty:forKey:]
+ -[AVPlayerItem identifier]
+ -[AVPlayerItem setReportingValueWithNumber:forKey:]
+ -[AVPlayerItem setReportingValueWithString:forKey:]
+ -[AVPlayerItemErrorLogEvent allHTTPResponseHeaderFields]
+ -[AVPlayerTaggedBufferOutput initWithVideoOutput:]
+ -[AVPlayerTaggedBufferOutput init]
+ -[AVPlayerTaggedBufferOutput realOutput]
+ -[AVPlayerVideoOutput .cxx_destruct]
+ -[AVPlayerVideoOutput _attachToPlayer:exceptionReason:]
+ -[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]
+ -[AVPlayerVideoOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue]
+ -[AVPlayerVideoOutput _detachFromPlayer:]
+ -[AVPlayerVideoOutput _playerItemWithIdentifier:]
+ -[AVPlayerVideoOutput _setResourceLifeCycleHandler:]
+ -[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:]
+ -[AVPlayerVideoOutput _setupWithOutputSpecification:exceptionReasonOut:]
+ -[AVPlayerVideoOutput attachedPlayer]
+ -[AVPlayerVideoOutput copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:]
+ -[AVPlayerVideoOutput dealloc]
+ -[AVPlayerVideoOutput hasNewTaggedBufferGroupForHostTime:]
+ -[AVPlayerVideoOutput initWithSpecification:]
+ -[AVPlayerVideoOutput resourceLifeCycleHandler]
+ -[AVPlayerVideoOutputConfiguration .cxx_destruct]
+ -[AVPlayerVideoOutputConfiguration activationTime]
+ -[AVPlayerVideoOutputConfiguration copy]
+ -[AVPlayerVideoOutputConfiguration dataChannelDescriptions]
+ -[AVPlayerVideoOutputConfiguration dealloc]
+ -[AVPlayerVideoOutputConfiguration initWithSourcePlayerItem:dataChannelDescriptions:activationTime:]
+ -[AVPlayerVideoOutputConfiguration setActivationTime:]
+ -[AVPlayerVideoOutputConfiguration setDataChannelDescriptions:]
+ -[AVPlayerVideoOutputConfiguration setSourcePlayerItem:]
+ -[AVPlayerVideoOutputConfiguration sourcePlayerItem]
+ -[AVTaggedVideoOutputSpecification realSpecification]
+ -[AVVideoOutputSpecification copyWithZone:]
+ -[AVVideoOutputSpecification dealloc]
+ -[AVVideoOutputSpecification defaultPixelBufferAttributes]
+ -[AVVideoOutputSpecification initWithTagCollections:]
+ -[AVVideoOutputSpecification init]
+ -[AVVideoOutputSpecification pixelBufferAttributesForTagCollection:]
+ -[AVVideoOutputSpecification preferredTagCollections]
+ -[AVVideoOutputSpecification setDefaultPixelBufferAttributes:]
+ -[AVVideoOutputSpecification setOutputPixelBufferAttributes:forTagCollection:]
+ GCC_except_table102
+ GCC_except_table140
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table187
+ GCC_except_table194
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table224
+ GCC_except_table230
+ GCC_except_table243
+ GCC_except_table267
+ GCC_except_table275
+ GCC_except_table283
+ GCC_except_table299
+ GCC_except_table306
+ GCC_except_table326
+ GCC_except_table334
+ GCC_except_table351
+ GCC_except_table357
+ GCC_except_table363
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table395
+ GCC_except_table401
+ GCC_except_table403
+ GCC_except_table411
+ GCC_except_table417
+ GCC_except_table425
+ GCC_except_table433
+ GCC_except_table445
+ GCC_except_table448
+ GCC_except_table466
+ GCC_except_table470
+ GCC_except_table478
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table491
+ GCC_except_table493
+ GCC_except_table499
+ GCC_except_table501
+ GCC_except_table521
+ GCC_except_table526
+ GCC_except_table528
+ GCC_except_table532
+ GCC_except_table534
+ GCC_except_table548
+ GCC_except_table552
+ GCC_except_table554
+ GCC_except_table558
+ GCC_except_table562
+ GCC_except_table570
+ GCC_except_table580
+ GCC_except_table588
+ GCC_except_table609
+ GCC_except_table611
+ GCC_except_table622
+ GCC_except_table626
+ GCC_except_table637
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table643
+ GCC_except_table645
+ GCC_except_table648
+ GCC_except_table653
+ GCC_except_table655
+ GCC_except_table658
+ GCC_except_table661
+ GCC_except_table666
+ GCC_except_table674
+ GCC_except_table679
+ GCC_except_table688
+ GCC_except_table694
+ GCC_except_table700
+ GCC_except_table701
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table713
+ GCC_except_table721
+ GCC_except_table732
+ GCC_except_table734
+ GCC_except_table736
+ GCC_except_table742
+ GCC_except_table748
+ GCC_except_table758
+ GCC_except_table762
+ GCC_except_table764
+ GCC_except_table766
+ GCC_except_table772
+ GCC_except_table787
+ GCC_except_table791
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table815
+ GCC_except_table817
+ GCC_except_table823
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table849
+ GCC_except_table877
+ GCC_except_table879
+ GCC_except_table881
+ GCC_except_table897
+ GCC_except_table907
+ GCC_except_table914
+ GCC_except_table918
+ GCC_except_table926
+ GCC_except_table931
+ GCC_except_table933
+ GCC_except_table941
+ GCC_except_table949
+ GCC_except_table959
+ GCC_except_table96
+ GCC_except_table963
+ GCC_except_table965
+ GCC_except_table969
+ _AVErrorFailedDependenciesKey
+ _AVMetadataIdentifierQuickTimeMetadataFullFrameRatePlaybackIntent
+ _AVMetadataIdentifierQuickTimeMetadataSpatialLowMotion
+ _AVMetadataQuickTimeMetadataKeyFullFrameRatePlaybackIntent
+ _AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished
+ _AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey
+ _AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished
+ _CMTagCollectionCreate
+ _CMTagCollectionCreateWithVideoOutputPreset
+ _OBJC_CLASS_$_AVPlayerVideoOutput
+ _OBJC_CLASS_$_AVPlayerVideoOutputConfiguration
+ _OBJC_CLASS_$_AVVideoOutputSpecification
+ _OBJC_IVAR_$_AVPlayerInternal.taggedBufferOutput
+ _OBJC_IVAR_$_AVPlayerInternal.videoOutput
+ _OBJC_IVAR_$_AVPlayerItemInternal.reportingValues
+ _OBJC_IVAR_$_AVPlayerItemInternal.uniqueInstanceIdentifier
+ _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._realOutput
+ _OBJC_IVAR_$_AVPlayerVideoOutput._iVarAccessQueue
+ _OBJC_IVAR_$_AVPlayerVideoOutput._outputSpecification
+ _OBJC_IVAR_$_AVPlayerVideoOutput._receiverState
+ _OBJC_IVAR_$_AVPlayerVideoOutput._resourceLifeCycleHandler
+ _OBJC_IVAR_$_AVPlayerVideoOutputConfiguration._activationTime
+ _OBJC_IVAR_$_AVPlayerVideoOutputConfiguration._dataChannelDescriptions
+ _OBJC_IVAR_$_AVPlayerVideoOutputConfiguration._sourcePlayerItem
+ _OBJC_IVAR_$_AVTaggedVideoOutputSpecification._realSpecification
+ _OBJC_IVAR_$_AVVideoOutputSpecification._defaultPixelBufferAttributes
+ _OBJC_IVAR_$_AVVideoOutputSpecification._tagCollectionPixelBufferAttributesMapping
+ _OBJC_IVAR_$_AVVideoOutputSpecification._tagCollections
+ _OBJC_METACLASS_$_AVPlayerVideoOutput
+ _OBJC_METACLASS_$_AVPlayerVideoOutputConfiguration
+ _OBJC_METACLASS_$_AVVideoOutputSpecification
+ __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|FigVideoTargetSupport_Internal|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap)
+ __OBJC_$_CLASS_METHODS_AVPlayerTaggedBufferOutput
+ __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|FigVideoTargetSupport_Internal|AVPlayerTaggedBufferOutputSupport|AVPlayerOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerVideoOutput
+ __OBJC_$_INSTANCE_METHODS_AVPlayerVideoOutputConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVVideoOutputSpecification
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerVideoOutput
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerVideoOutputConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVVideoOutputSpecification
+ __OBJC_$_PROP_LIST_AVPlayerVideoOutputConfiguration
+ __OBJC_$_PROP_LIST_AVVideoOutputSpecification
+ __OBJC_CLASS_PROTOCOLS_$_AVVideoOutputSpecification
+ __OBJC_CLASS_RO_$_AVPlayerVideoOutput
+ __OBJC_CLASS_RO_$_AVPlayerVideoOutputConfiguration
+ __OBJC_CLASS_RO_$_AVVideoOutputSpecification
+ __OBJC_METACLASS_RO_$_AVPlayerVideoOutput
+ __OBJC_METACLASS_RO_$_AVPlayerVideoOutputConfiguration
+ __OBJC_METACLASS_RO_$_AVVideoOutputSpecification
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.413
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.414
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.415
+ ___146-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke
+ ___26-[AVPlayerItem identifier]_block_invoke
+ ___37-[AVPlayerVideoOutput attachedPlayer]_block_invoke
+ ___41-[AVPlayerVideoOutput _detachFromPlayer:]_block_invoke
+ ___46-[AVPlayer(AVPlayerOutputSupport) videoOutput]_block_invoke
+ ___47-[AVPlayerVideoOutput resourceLifeCycleHandler]_block_invoke
+ ___52-[AVPlayerVideoOutput _setResourceLifeCycleHandler:]_block_invoke
+ ___54-[AVPlayerItem _updateReportingValuesProperty:forKey:]_block_invoke
+ ___55-[AVPlayerItem _updateReportingValuesOnFigPlaybackItem]_block_invoke
+ ___55-[AVPlayerItem _updateReportingValuesOnFigPlaybackItem]_block_invoke_2
+ ___55-[AVPlayerVideoOutput _attachToPlayer:exceptionReason:]_block_invoke
+ ___56-[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:]_block_invoke
+ ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.487
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.447
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.451
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.459
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.460
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.467
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.468
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.470
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1046
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1043
+ ___91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke
+ ___91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke_2
+ ___Block_byref_object_copy_.79
+ ___Block_byref_object_dispose_.80
+ ___block_descriptor_113_e8_32o40o48r56r64r72r80r_e5_v8?0ls32l8r48l8s40l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_40_e8_32w_e121_v64?0^{OpaqueFigVideoReceiver=}8{FigVideoReceiverConfigurationInfo=^{__CFString}^{__CFArray}^{__CFDictionary}{?=qiIq}}16lw32l8
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40o48r56r64r_e5_v8?0ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32o40r48r56r64r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8
+ ___block_literal_global.1239
+ ___block_literal_global.321
+ ___block_literal_global.340
+ ___block_literal_global.350
+ ___block_literal_global.378
+ ___block_literal_global.411
+ ___block_literal_global.416
+ ___block_literal_global.535
+ ___block_literal_global.545
+ ___block_literal_global.606
+ ___block_literal_global.612
+ ___block_literal_global.865
+ ___handleFigAssetLoadingNotification_block_invoke.526
+ __unnamed_array_storage.643
+ _kCMTagMediaTypeVideo
+ _kCMTagPackingTypeNone
+ _kCMTagProjectionTypeRectangular
+ _kCMTagStereoLeftAndRightEye
+ _kCMTagStereoNone
+ _kFigErrorLogKey_AllHTTPResponseHeaderFields
+ _kFigPlaybackItemOptionKey_UniqueInstanceIdentifier
+ _kFigPlaybackItemProperty_ClientReportingValues
+ _objc_msgSend$_attachToPlayer:exceptionReason:
+ _objc_msgSend$_copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:
+ _objc_msgSend$_playerItemWithIdentifier:
+ _objc_msgSend$_setResourceLifeCycleHandler:
+ _objc_msgSend$_setUpVideoReceiverEventHandlers:
+ _objc_msgSend$_setupWithOutputSpecification:exceptionReasonOut:
+ _objc_msgSend$_updateReportingValuesOnFigPlaybackItem
+ _objc_msgSend$_updateReportingValuesProperty:forKey:
+ _objc_msgSend$copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:
+ _objc_msgSend$defaultPixelBufferAttributes
+ _objc_msgSend$hasNewTaggedBufferGroupForHostTime:
+ _objc_msgSend$initWithSourcePlayerItem:dataChannelDescriptions:activationTime:
+ _objc_msgSend$initWithSpecification:
+ _objc_msgSend$initWithVideoOutput:
+ _objc_msgSend$realOutput
+ _objc_msgSend$realSpecification
+ _objc_msgSend$setDefaultPixelBufferAttributes:
+ _objc_msgSend$setVideoOutput:withOwningTaggedBufferOutput:
+ _objc_msgSend$videoOutput
+ _objc_retain_x9
- -[AVPlayerTaggedBufferOutput .cxx_destruct]
- -[AVPlayerTaggedBufferOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue]
- -[AVPlayerTaggedBufferOutput _setupWithTaggedOutputSpecification:exceptionReasonOut:]
- -[AVPlayerTaggedBufferOutput lastSeenTaggedBufferGroup]
- -[AVPlayerTaggedBufferOutput resourceLifeCycleHandler]
- -[AVPlayerTaggedBufferOutput setLastSeenTaggedBufferGroup:]
- -[AVTaggedVideoOutputSpecification copyWithZone:]
- -[AVTaggedVideoOutputSpecification init]
- -[AVTaggedVideoOutputSpecification pixelBufferAttributesForTagCollection:]
- -[AVTaggedVideoOutputSpecification setupWithTagCollections:exceptionReasonOut:]
- GCC_except_table100
- GCC_except_table109
- GCC_except_table149
- GCC_except_table153
- GCC_except_table160
- GCC_except_table172
- GCC_except_table178
- GCC_except_table183
- GCC_except_table190
- GCC_except_table206
- GCC_except_table217
- GCC_except_table228
- GCC_except_table234
- GCC_except_table248
- GCC_except_table255
- GCC_except_table263
- GCC_except_table271
- GCC_except_table295
- GCC_except_table304
- GCC_except_table309
- GCC_except_table324
- GCC_except_table330
- GCC_except_table342
- GCC_except_table348
- GCC_except_table354
- GCC_except_table360
- GCC_except_table366
- GCC_except_table372
- GCC_except_table374
- GCC_except_table380
- GCC_except_table386
- GCC_except_table392
- GCC_except_table394
- GCC_except_table400
- GCC_except_table408
- GCC_except_table410
- GCC_except_table416
- GCC_except_table422
- GCC_except_table424
- GCC_except_table436
- GCC_except_table439
- GCC_except_table457
- GCC_except_table461
- GCC_except_table469
- GCC_except_table474
- GCC_except_table480
- GCC_except_table482
- GCC_except_table484
- GCC_except_table490
- GCC_except_table492
- GCC_except_table497
- GCC_except_table514
- GCC_except_table519
- GCC_except_table525
- GCC_except_table531
- GCC_except_table539
- GCC_except_table543
- GCC_except_table545
- GCC_except_table551
- GCC_except_table553
- GCC_except_table559
- GCC_except_table561
- GCC_except_table567
- GCC_except_table569
- GCC_except_table571
- GCC_except_table577
- GCC_except_table579
- GCC_except_table600
- GCC_except_table606
- GCC_except_table617
- GCC_except_table628
- GCC_except_table638
- GCC_except_table640
- GCC_except_table644
- GCC_except_table647
- GCC_except_table650
- GCC_except_table652
- GCC_except_table654
- GCC_except_table657
- GCC_except_table662
- GCC_except_table667
- GCC_except_table673
- GCC_except_table682
- GCC_except_table689
- GCC_except_table697
- GCC_except_table698
- GCC_except_table70
- GCC_except_table702
- GCC_except_table704
- GCC_except_table712
- GCC_except_table720
- GCC_except_table725
- GCC_except_table726
- GCC_except_table727
- GCC_except_table733
- GCC_except_table739
- GCC_except_table749
- GCC_except_table753
- GCC_except_table755
- GCC_except_table757
- GCC_except_table763
- GCC_except_table769
- GCC_except_table782
- GCC_except_table796
- GCC_except_table798
- GCC_except_table806
- GCC_except_table808
- GCC_except_table814
- GCC_except_table821
- GCC_except_table827
- GCC_except_table829
- GCC_except_table840
- GCC_except_table868
- GCC_except_table870
- GCC_except_table872
- GCC_except_table888
- GCC_except_table896
- GCC_except_table898
- GCC_except_table909
- GCC_except_table915
- GCC_except_table917
- GCC_except_table922
- GCC_except_table932
- GCC_except_table936
- GCC_except_table940
- GCC_except_table947
- GCC_except_table950
- GCC_except_table960
- _OBJC_IVAR_$_AVPlayerInternal.taggedBufferOutputs
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._ivarAccessQueue
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._lastSeenTaggedBufferGroup
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._outputSpecification
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._playerWeakReference
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._resourceLifeCycleHandler
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._stateQueue
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._videoReceiver
- _OBJC_IVAR_$_AVPlayerTaggedBufferOutput._videoTarget
- _OBJC_IVAR_$_AVTaggedVideoOutputSpecification._defaultPixelBufferAttrbiutes
- _OBJC_IVAR_$_AVTaggedVideoOutputSpecification._ivarAccessQueue
- _OBJC_IVAR_$_AVTaggedVideoOutputSpecification._tagCollectionPixelBufferAttributesMapping
- _OBJC_IVAR_$_AVTaggedVideoOutputSpecification._tagCollections
- __OBJC_$_CLASS_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|FigVideoTargetSupport_Internal|AVPlayerTaggedBufferOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap)
- __OBJC_$_INSTANCE_METHODS_AVPlayer(AVPlayerVideoDisplaySleepPrevention|AVPlayerAutomaticBackgroundPrevention|AVPlayerProtectedContentPrivate|AVPlayer_PIPSupport|AVPlayerAudioPlaybackRateLimits|AVPlayerMultitaskSupport|AVPlayerSupportForMediaPlayer|AVPlayerPixelBufferPoolSharing|AVPlayerFormatRestrictions|AVPlayerAutomaticMediaSelection|AVPlayerAutomaticMediaSelectionPrivate|AVPlayerAudioDeviceSupport|AVPlayerOutOfBandTextTrackRendering|AVPlayerMultichannelAudioStrategy|AVPlayerCaptionStrategySelection|AVPlayerAudioSessionParticipant|AVPlayerVideoDecoderGPUSupport|AVPlayerLoggingIdentifier|AVPlayerAutoPauseOnRouteRemoval|AVPlayerImplicitInterruption|AVPlayerSTSLabel|AVPlayerPIPSupport|FigVideoTargetSupport|FigVideoTargetSupport_Internal|AVPlayerTaggedBufferOutputSupport|AVPlayerInterstitialSupport_Internal|PlaybackCoordination|AVPlayerLegibleFallback|AVIntegrityChecking|AVPlayerAdvanceWithOverlap)
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.410
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.411
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.412
- ___46-[AVPlayerTaggedBufferOutput _attachToPlayer:]_block_invoke
- ___48-[AVPlayerTaggedBufferOutput _detachFromPlayer:]_block_invoke
- ___48-[AVPlayerTaggedBufferOutput _detachFromPlayer:]_block_invoke_2
- ___54-[AVPlayerTaggedBufferOutput resourceLifeCycleHandler]_block_invoke
- ___55-[AVPlayerTaggedBufferOutput lastSeenTaggedBufferGroup]_block_invoke
- ___59-[AVPlayerTaggedBufferOutput _setResourceLifeCycleHandler:]_block_invoke
- ___59-[AVPlayerTaggedBufferOutput setLastSeenTaggedBufferGroup:]_block_invoke
- ___59-[AVTaggedVideoOutputSpecification preferredTagCollections]_block_invoke
- ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.484
- ___64-[AVTaggedVideoOutputSpecification defaultPixelBufferAttributes]_block_invoke
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.444
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.448
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.456
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.457
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.464
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.465
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.467
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1043
- ___68-[AVTaggedVideoOutputSpecification setDefaultPixelBufferAttributes:]_block_invoke
- ___69-[AVPlayer(AVPlayerTaggedBufferOutputSupport) addTaggedBufferOutput:]_block_invoke
- ___72-[AVPlayer(AVPlayerTaggedBufferOutputSupport) removeTaggedBufferOutput:]_block_invoke
- ___73-[AVPlayer(FigVideoTargetSupport) setActiveVideoTargetsForInterstitials:]_block_invoke
- ___74-[AVTaggedVideoOutputSpecification pixelBufferAttributesForTagCollection:]_block_invoke
- ___84-[AVTaggedVideoOutputSpecification setOutputPixelBufferAttributes:forTagCollection:]_block_invoke
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1040
- ___block_literal_global.1227
- ___block_literal_global.320
- ___block_literal_global.334
- ___block_literal_global.349
- ___block_literal_global.375
- ___block_literal_global.402
- ___block_literal_global.407
- ___block_literal_global.528
- ___block_literal_global.542
- ___block_literal_global.597
- ___block_literal_global.603
- ___block_literal_global.862
- ___handleFigAssetLoadingNotification_block_invoke.525
- __unnamed_array_storage.634
- _objc_msgSend$_setupWithTaggedOutputSpecification:exceptionReasonOut:
- _objc_msgSend$lastSeenTaggedBufferGroup
- _objc_msgSend$setLastSeenTaggedBufferGroup:
- _objc_msgSend$setupWithTagCollections:exceptionReasonOut:
CStrings:
+ "-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:]_block_invoke"
+ "<<<< AVPlayerOutput >>>> %s: Provided host time is not valid"
+ "@\"AVPlayerTaggedBufferOutput\""
+ "@\"AVPlayerVideoOutput\""
+ "@\"AVVideoOutputSpecification\""
+ "@56@0:8@16@24{?=qiIq}32"
+ "AVErrorFailedDependenciesKey"
+ "AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished"
+ "AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey"
+ "AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished"
+ "AVPlayerOutputSupport"
+ "AVPlayerVideoOutput"
+ "AVPlayerVideoOutput can only attach to a single AVPlayer at a time"
+ "AVPlayerVideoOutput: Received malformed outputSpecification"
+ "AVPlayerVideoOutput: outputSpecification cannot be nil."
+ "AVPlayerVideoOutputConfiguration"
+ "AVVideoOutputSpecification"
+ "Currently only one video output is supported at a time"
+ "PreemptivePortConnection"
+ "T@\"AVPlayerItem\",W,N,V_sourcePlayerItem"
+ "T@\"AVPlayerVideoOutput\",N"
+ "T@\"NSArray\",C,N,V_dataChannelDescriptions"
+ "This output is already attached to a player, and AVPlayerVideoOutput cannot be attached to more than one player at a time"
+ "T{?=qiIq},N,V_activationTime"
+ "Value is not a number."
+ "Value is not a string."
+ "^{OpaqueCMTaggedBufferGroup=}56@0:8{?=qiIq}16^{?=qiIq}40^@48"
+ "^{OpaqueCMTaggedBufferGroup=}68@0:8{?=qiIq}16B40^{?=qiIq}44^@52^^{OpaqueCMTaggedBufferGroup}60"
+ "_activationTime"
+ "_attachToPlayer:exceptionReason:"
+ "_copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:"
+ "_dataChannelDescriptions"
+ "_defaultPixelBufferAttributes"
+ "_iVarAccessQueue"
+ "_playerItemWithIdentifier:"
+ "_realOutput"
+ "_realSpecification"
+ "_receiverState"
+ "_setUpVideoReceiverEventHandlers:"
+ "_setupWithOutputSpecification:exceptionReasonOut:"
+ "_sourcePlayerItem"
+ "_updateReportingValuesOnFigPlaybackItem"
+ "_updateReportingValuesProperty:forKey:"
+ "activationTime"
+ "allHTTPResponseHeaderFields"
+ "attachedPlayer"
+ "com.apple.avfoundation.avplayervideooutput.ivars"
+ "com.apple.avfoundation.avplayervideooutput.state"
+ "com.apple.quicktime.full-frame-rate-playback-intent"
+ "copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:"
+ "dataChannelDescriptions"
+ "description=AVFoundation_AVFCore-2220.14.1"
+ "i24@0:8^{OpaqueFigVideoReceiver=}16"
+ "initWithSourcePlayerItem:dataChannelDescriptions:activationTime:"
+ "initWithVideoOutput:"
+ "mdta/com.apple.quicktime.full-frame-rate-playback-intent"
+ "mdta/com.apple.quicktime.spatial.low-motion"
+ "realOutput"
+ "realSpecification"
+ "reportingValues"
+ "setActivationTime:"
+ "setDataChannelDescriptions:"
+ "setReportingValueWithNumber:forKey:"
+ "setReportingValueWithString:forKey:"
+ "setSourcePlayerItem:"
+ "setVideoOutput:"
+ "setVideoOutput:withOwningTaggedBufferOutput:"
+ "sourcePlayerItem"
+ "taggedBufferOutput"
+ "taggedBufferOutputWithVideoOutput:"
+ "uniqueInstanceIdentifier"
+ "v64@?0^{OpaqueFigVideoReceiver=}8{FigVideoReceiverConfigurationInfo=^{__CFString}^{__CFArray}^{__CFDictionary}{?=qiIq}}16"
+ "videoOutput"
+ "{?=\"stateQueue\"@\"NSObject<OS_dispatch_queue>\"\"weakPlayer\"@\"AVPlayer\"\"videoTarget\"^{OpaqueFigVideoTarget}\"videoReceiver\"^{OpaqueFigVideoReceiver}\"lastSeenTaggedBufferGroup\"^{OpaqueCMTaggedBufferGroup}\"activeConfiguration\"@\"AVPlayerVideoOutputConfiguration\"}"
- "@\"AVTaggedVideoOutputSpecification\""
- "AVPlayerTaggedBufferOutput ivar access queue"
- "AVPlayerTaggedBufferOutput state queue"
- "AVPlayerTaggedBufferOutput: Received malformed taggedOutputSpecification"
- "AVPlayerTaggedBufferOutput: taggedOutputSpecification cannot be nil."
- "Cannot attach an output that is already attached or nil"
- "^{OpaqueCMTaggedBufferGroup=}"
- "^{OpaqueCMTaggedBufferGroup=}16@0:8"
- "^{OpaqueFigVideoReceiver=}"
- "^{OpaqueFigVideoTarget=}"
- "_defaultPixelBufferAttrbiutes"
- "_lastSeenTaggedBufferGroup"
- "_playerWeakReference"
- "_setupWithTaggedOutputSpecification:exceptionReasonOut:"
- "_videoReceiver"
- "_videoTarget"
- "com.apple.avtaggedvideooutputspecification.ivars"
- "description=AVFoundation_AVFCore-2215.13.4"
- "lastSeenTaggedBufferGroup"
- "setLastSeenTaggedBufferGroup:"
- "setupWithTagCollections:exceptionReasonOut:"
- "v24@0:8^{OpaqueCMTaggedBufferGroup=}16"

```
