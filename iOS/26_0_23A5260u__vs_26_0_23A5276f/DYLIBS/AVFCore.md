## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2360.61.4.11.1
-  __TEXT.__text: 0x20334c
-  __TEXT.__auth_stubs: 0x3cb0
-  __TEXT.__objc_methlist: 0x1abdc
-  __TEXT.__cstring: 0x30ecc
-  __TEXT.__const: 0x1f88
-  __TEXT.__gcc_except_tab: 0x798c
-  __TEXT.__oslogstring: 0x1b6f5
+2360.66.3.0.0
+  __TEXT.__text: 0x20536c
+  __TEXT.__auth_stubs: 0x3cd0
+  __TEXT.__objc_methlist: 0x1acf4
+  __TEXT.__cstring: 0x31136
+  __TEXT.__const: 0x1ed0
+  __TEXT.__gcc_except_tab: 0x79f0
+  __TEXT.__oslogstring: 0x1b8f6
   __TEXT.__ustring: 0x18
-  __TEXT.__swift5_typeref: 0x4cf
-  __TEXT.__constg_swiftt: 0x354
-  __TEXT.__swift5_reflstr: 0x12a
-  __TEXT.__swift5_fieldmd: 0x1f4
+  __TEXT.__swift5_typeref: 0x415
+  __TEXT.__constg_swiftt: 0x290
   __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_reflstr: 0x9c
+  __TEXT.__swift5_fieldmd: 0x17c
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x9378
-  __TEXT.__objc_classname: 0x5e31
-  __TEXT.__objc_methname: 0x3570e
-  __TEXT.__objc_methtype: 0x9cbf
-  __TEXT.__objc_stubs: 0x204a0
-  __DATA_CONST.__got: 0x4530
-  __DATA_CONST.__const: 0x5540
+  __TEXT.__unwind_info: 0x93a0
+  __TEXT.__objc_classname: 0x5e38
+  __TEXT.__objc_methname: 0x359d7
+  __TEXT.__objc_methtype: 0x9cc9
+  __TEXT.__objc_stubs: 0x205c0
+  __DATA_CONST.__got: 0x4560
+  __DATA_CONST.__const: 0x5578
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa40
+  __DATA_CONST.__objc_selrefs: 0xaab0
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xcc0
+  __DATA_CONST.__objc_superrefs: 0xcc8
   __DATA_CONST.__objc_arraydata: 0x298
-  __AUTH_CONST.__auth_got: 0x1e68
-  __AUTH_CONST.__const: 0x1098
-  __AUTH_CONST.__cfstring: 0x19040
-  __AUTH_CONST.__objc_const: 0x300d8
+  __AUTH_CONST.__auth_got: 0x1e78
+  __AUTH_CONST.__const: 0x1118
+  __AUTH_CONST.__cfstring: 0x191a0
+  __AUTH_CONST.__objc_const: 0x30288
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x79d8
+  __AUTH.__objc_data: 0x78d0
   __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x24fc
-  __DATA.__data: 0x18a8
+  __DATA.__objc_ivar: 0x2524
+  __DATA.__data: 0x1890
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x420
-  __DATA.__bss: 0x1410
-  __DATA_DIRTY.__objc_data: 0x36b0
+  __DATA.__bss: 0x13f0
+  __DATA_DIRTY.__objc_data: 0x3660
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x270
   __DATA_DIRTY.__bss: 0x1a0

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B78BEC21-EBC9-37AE-BF91-A72FEDD08D85
-  Functions: 11375
-  Symbols:   38829
-  CStrings:  18688
+  UUID: 83311825-417A-33E7-BA32-6E5C0C1301E8
+  Functions: 11401
+  Symbols:   38920
+  CStrings:  18738
 
Symbols:
+ +[AVMetadataItemFilterForSharing addIdentifier:toAllowListDictionary:]
+ +[AVMetadataItemFilterForSharing addKeySpace:key:toAllowListDictionary:]
+ +[AVMetricMediaRendition supportsSecureCoding]
+ -[AVMetadataItemFilter allowList]
+ -[AVMetadataItemFilterForSharing allowList]
+ -[AVMetadataItemFilterForSharing allowList].cold.1
+ -[AVMetricHLSMediaSegmentRequestEvent initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:segmentDuration:mediaResourceRequestEvent:]
+ -[AVMetricHLSMediaSegmentRequestEvent segmentDuration]
+ -[AVMetricMediaRendition URL]
+ -[AVMetricMediaRendition dealloc]
+ -[AVMetricMediaRendition debugDescription]
+ -[AVMetricMediaRendition encodeWithCoder:]
+ -[AVMetricMediaRendition initWithCoder:]
+ -[AVMetricMediaRendition initWithStableID:URL:]
+ -[AVMetricMediaRendition stableID]
+ -[AVMetricPlayerItemVariantSwitchEvent audioRendition]
+ -[AVMetricPlayerItemVariantSwitchEvent initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:didSucceed:]
+ -[AVMetricPlayerItemVariantSwitchEvent subtitleRendition]
+ -[AVMetricPlayerItemVariantSwitchEvent videoRendition]
+ -[AVMetricPlayerItemVariantSwitchStartEvent audioRendition]
+ -[AVMetricPlayerItemVariantSwitchStartEvent initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:]
+ -[AVMetricPlayerItemVariantSwitchStartEvent subtitleRendition]
+ -[AVMetricPlayerItemVariantSwitchStartEvent videoRendition]
+ -[AVPlayer _allClientAndVideoLayerVideoTargets]
+ -[AVPlayer _hasForegroundVideoDestinations]
+ -[AVPlayer _hasVideoDestinations]
+ -[AVPlayer _reevaluateVideoLayersAndTargetsForPresentationState:withCompletionHandler:]
+ -[AVPlayer _shouldAttachVideoDestinationsToFigPlayerOnStateQueue]
+ -[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]
+ -[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspension]
+ -[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:withCompletionHandler:]
+ -[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoDestinationsAreAttached]
+ -[AVPlayer(FigVideoTargetSupport) _updateVideoTargetsOnFigPlayer:withCompletionHandler:]
+ -[AVPlayerItem audioTapProcessorWasSet]
+ -[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:]
+ -[AVSampleBufferVideoRenderer setVideoLayerGeometryFlipped:]
+ -[AVSampleBufferVideoRenderer(PowerOptimization) recommendedPixelBufferAttributes]
+ GCC_except_table1004
+ GCC_except_table1015
+ GCC_except_table1019
+ GCC_except_table1023
+ GCC_except_table1027
+ GCC_except_table1034
+ GCC_except_table1037
+ GCC_except_table1043
+ GCC_except_table1049
+ GCC_except_table1053
+ GCC_except_table1057
+ GCC_except_table1061
+ GCC_except_table1069
+ GCC_except_table1072
+ GCC_except_table1077
+ GCC_except_table1081
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table141
+ GCC_except_table152
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table392
+ GCC_except_table400
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table440
+ GCC_except_table452
+ GCC_except_table456
+ GCC_except_table465
+ GCC_except_table467
+ GCC_except_table476
+ GCC_except_table479
+ GCC_except_table481
+ GCC_except_table490
+ GCC_except_table502
+ GCC_except_table531
+ GCC_except_table536
+ GCC_except_table548
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table586
+ GCC_except_table588
+ GCC_except_table597
+ GCC_except_table606
+ GCC_except_table624
+ GCC_except_table628
+ GCC_except_table642
+ GCC_except_table648
+ GCC_except_table654
+ GCC_except_table659
+ GCC_except_table671
+ GCC_except_table673
+ GCC_except_table680
+ GCC_except_table696
+ GCC_except_table698
+ GCC_except_table705
+ GCC_except_table710
+ GCC_except_table713
+ GCC_except_table717
+ GCC_except_table725
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table745
+ GCC_except_table751
+ GCC_except_table753
+ GCC_except_table755
+ GCC_except_table767
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table774
+ GCC_except_table782
+ GCC_except_table784
+ GCC_except_table794
+ GCC_except_table805
+ GCC_except_table816
+ GCC_except_table818
+ GCC_except_table823
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table835
+ GCC_except_table851
+ GCC_except_table857
+ GCC_except_table864
+ GCC_except_table871
+ GCC_except_table874
+ GCC_except_table881
+ GCC_except_table882
+ GCC_except_table898
+ GCC_except_table901
+ GCC_except_table910
+ GCC_except_table921
+ GCC_except_table922
+ GCC_except_table946
+ GCC_except_table964
+ GCC_except_table97
+ GCC_except_table974
+ GCC_except_table978
+ GCC_except_table985
+ GCC_except_table988
+ GCC_except_table989
+ GCC_except_table992
+ GCC_except_table997
+ _AVPlayerItemGaplessInfoOverrideHEAACPrimingEditListKey
+ _OBJC_CLASS_$_AVMetricMediaRendition
+ _OBJC_CLASS_$_AVPlayerItemObservationRegistrar
+ _OBJC_CLASS_$_AVPlayerItemTrackObservationRegistrar
+ _OBJC_CLASS_$_AVPlayerObservationRegistrar
+ _OBJC_CLASS_$_AVQueuePlayerObservationRegistrar
+ _OBJC_IVAR_$_AVMetricEventStream._weakSelf
+ _OBJC_IVAR_$_AVMetricHLSMediaSegmentRequestEvent._segmentDuration
+ _OBJC_IVAR_$_AVMetricMediaRendition._stableID
+ _OBJC_IVAR_$_AVMetricMediaRendition._url
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchEvent._audioRendition
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchEvent._subtitleRendition
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchEvent._videoRendition
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._audioRendition
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._subtitleRendition
+ _OBJC_IVAR_$_AVMetricPlayerItemVariantSwitchStartEvent._videoRendition
+ _OBJC_IVAR_$_AVPlayerItemInternal.audioTapProcessorWasSet
+ _OBJC_METACLASS_$_AVMetricMediaRendition
+ _OBJC_METACLASS_$_AVPlayerItemObservationRegistrar
+ _OBJC_METACLASS_$_AVPlayerItemTrackObservationRegistrar
+ _OBJC_METACLASS_$_AVPlayerObservationRegistrar
+ _OBJC_METACLASS_$_AVQueuePlayerObservationRegistrar
+ __DATA_AVPlayerItemObservationRegistrar
+ __DATA_AVPlayerItemTrackObservationRegistrar
+ __DATA_AVPlayerObservationRegistrar
+ __DATA_AVQueuePlayerObservationRegistrar
+ __INSTANCE_METHODS_AVPlayerItemObservationRegistrar
+ __INSTANCE_METHODS_AVPlayerItemTrackObservationRegistrar
+ __INSTANCE_METHODS_AVPlayerObservationRegistrar
+ __INSTANCE_METHODS_AVQueuePlayerObservationRegistrar
+ __IVARS_AVPlayerItemObservationRegistrar
+ __IVARS_AVPlayerItemTrackObservationRegistrar
+ __IVARS_AVPlayerObservationRegistrar
+ __IVARS_AVQueuePlayerObservationRegistrar
+ __METACLASS_DATA_AVPlayerItemObservationRegistrar
+ __METACLASS_DATA_AVPlayerItemTrackObservationRegistrar
+ __METACLASS_DATA_AVPlayerObservationRegistrar
+ __METACLASS_DATA_AVQueuePlayerObservationRegistrar
+ __OBJC_$_CLASS_METHODS_AVMetricMediaRendition
+ __OBJC_$_CLASS_PROP_LIST_AVMetricMediaRendition
+ __OBJC_$_INSTANCE_METHODS_AVMetricMediaRendition
+ __OBJC_$_INSTANCE_VARIABLES_AVMetricMediaRendition
+ __OBJC_$_PROP_LIST_AVMetricMediaRendition
+ __OBJC_CLASS_PROTOCOLS_$_AVMetricMediaRendition
+ __OBJC_CLASS_RO_$_AVMetricMediaRendition
+ __OBJC_METACLASS_RO_$_AVMetricMediaRendition
+ ___101-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:]_block_invoke
+ ___101-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:]_block_invoke_2
+ ___122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.150
+ ___31-[AVPlayerItem _updateTimebase]_block_invoke.658
+ ___31-[AVPlayerItem _updateTimebase]_block_invoke_2.659
+ ___33-[AVPlayer _hasVideoDestinations]_block_invoke
+ ___33-[AVPlayer _hasVideoDestinations]_block_invoke_2
+ ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.296
+ ___39-[AVPlayerItem audioTapProcessorWasSet]_block_invoke
+ ___43-[AVMetadataItemFilterForSharing allowList]_block_invoke
+ ___43-[AVPlayer _hasForegroundVideoDestinations]_block_invoke
+ ___43-[AVPlayer _hasForegroundVideoDestinations]_block_invoke_2
+ ___47-[AVPlayer _allClientAndVideoLayerVideoTargets]_block_invoke
+ ___47-[AVPlayer _allClientAndVideoLayerVideoTargets]_block_invoke_2
+ ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke.511
+ ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke.310
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.995
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.996
+ ___60-[AVSampleBufferVideoRenderer setVideoLayerGeometryFlipped:]_block_invoke
+ ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke.166
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1188
+ ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.174
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1174
+ ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke.281
+ ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.151
+ ___73-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoDestinationsAreAttached]_block_invoke
+ ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.130
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.143
+ ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.144
+ ___82-[AVSampleBufferVideoRenderer(PowerOptimization) recommendedPixelBufferAttributes]_block_invoke
+ ___88-[AVPlayer(FigVideoTargetSupport) _updateVideoTargetsOnFigPlayer:withCompletionHandler:]_block_invoke
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1171
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1270
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke.998
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2.999
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_3
+ ___Block_byref_object_copy_.145
+ ___Block_byref_object_dispose_.146
+ ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1427
+ ___avplayer_fpNotificationCallback_block_invoke.1444
+ ___avplayer_fpNotificationCallback_block_invoke.1447
+ ___avplayer_fpNotificationCallback_block_invoke.1457
+ ___avplayer_fpNotificationCallback_block_invoke.1465
+ ___avplayer_fpNotificationCallback_block_invoke_2.1448
+ ___avplayer_fpNotificationCallback_block_invoke_2.1461
+ ___avplayer_fpNotificationCallback_block_invoke_3.1452
+ ___avplayer_fpNotificationCallback_block_invoke_3.1462
+ ___avplayer_fpNotificationCallback_block_invoke_4.1463
+ ___avplayer_iapdNotificationCallback_block_invoke.1467
+ ___avplayer_iapdNotificationCallback_block_invoke.1468
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1614
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1636
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1637
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1638
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1644
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1645
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1646
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1647
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1653
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1659
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1664
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1665
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1666
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1673
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1648
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1654
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1661
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1649
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1662
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1650
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_5.1651
+ ___block_descriptor_48_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_65_e8_32o40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_literal_global.1078
+ ___block_literal_global.1080
+ ___block_literal_global.1418
+ ___block_literal_global.1471
+ ___block_literal_global.1499
+ ___block_literal_global.163
+ ___block_literal_global.174
+ ___block_literal_global.268
+ ___block_literal_global.277
+ ___block_literal_global.329
+ ___block_literal_global.570
+ ___block_literal_global.590
+ ___block_literal_global.761
+ ___block_literal_global.774
+ ___block_literal_global.974
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_memcpy32_8
+ ___swift_project_boxed_opaque_existential_0
+ ___unnamed_2
+ _allowList.onceToken
+ _allowList.sAllowList
+ _kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey
+ _kFigAssetExportSessionProperty_MetadataItemFilterAllowList
+ _kFigAssetOptionKey_AllowListQUIC
+ _kFigPlaybackItem_PlaybackProperties_OverrideHEAACPrimingEditList
+ _objc_msgSend$_allClientAndVideoLayerVideoTargets
+ _objc_msgSend$_detachVideoDestinationsForSuspension
+ _objc_msgSend$_detachVideoDestinationsForSuspensionWithCompletionHandler:
+ _objc_msgSend$_didFinishSuspension:withCompletionHandler:
+ _objc_msgSend$_ensureVideoDestinationsAreAttached
+ _objc_msgSend$_hasForegroundVideoDestinations
+ _objc_msgSend$_hasVideoDestinations
+ _objc_msgSend$_reevaluateVideoLayersAndTargetsForPresentationState:withCompletionHandler:
+ _objc_msgSend$_refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:
+ _objc_msgSend$_shouldAttachVideoDestinationsToFigPlayerOnStateQueue
+ _objc_msgSend$_updateVideoTargetsOnFigPlayer:withCompletionHandler:
+ _objc_msgSend$addIdentifier:toAllowListDictionary:
+ _objc_msgSend$addKeySpace:key:toAllowListDictionary:
+ _objc_msgSend$allowList
+ _objc_msgSend$audioTapProcessorWasSet
+ _objc_msgSend$initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:
+ _objc_msgSend$initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:didSucceed:
+ _objc_msgSend$initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:segmentDuration:mediaResourceRequestEvent:
+ _objc_msgSend$initWithStableID:URL:
+ _objc_msgSend$setInitialDate:
+ _objc_msgSend$setVideoLayerGeometryFlipped:
+ _swift_allocBox
+ _swift_dynamicCast
+ _swift_getDynamicType
+ _swift_getObjCClassFromMetadata
+ _symbolic _____ 7AVFCore27ObservationRegistrarWrapperV
+ _symbolic _____Sg 11Observation0A9RegistrarV
+ _symbolic y______xtYbc 11Observation0A9RegistrarV
+ _symbolic yp
+ _type_layout_string 11Observation10ObservableRzs8SendableRzl7AVFCore19RegistrarOperationsVyxG
+ _type_layout_string 7AVFCore27ObservationRegistrarWrapperV
- +[AVMetadataItemFilterForSharing addIdentifier:toWhitelistDictionary:]
- +[AVMetadataItemFilterForSharing addKeySpace:key:toWhitelistDictionary:]
- -[AVMetadataItemFilter whitelist]
- -[AVMetadataItemFilterForSharing whitelist]
- -[AVMetadataItemFilterForSharing whitelist].cold.1
- -[AVMetricHLSMediaSegmentRequestEvent initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:]
- -[AVMetricPlayerItemVariantSwitchEvent initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:didSucceed:]
- -[AVMetricPlayerItemVariantSwitchStartEvent initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:]
- -[AVPlayer _allVideoTargets]
- -[AVPlayer _checkIfShouldAttachOutputsToFigPlayerOnStateQueue]
- -[AVPlayer _hasForegroundLayers]
- -[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]
- -[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:]
- -[AVPlayer(FigVideoTargetSupport) _updateVideoTargetOnFigPlayer:synchronously:]
- -[AVSampleBufferDisplayLayer(AVSampleBufferDisplayLayerOutput) setIgnoresPreferredDynamicRange:]
- -[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevel]
- GCC_except_table1000
- GCC_except_table1013
- GCC_except_table1017
- GCC_except_table1021
- GCC_except_table1025
- GCC_except_table1030
- GCC_except_table1035
- GCC_except_table1039
- GCC_except_table1047
- GCC_except_table105
- GCC_except_table1051
- GCC_except_table1055
- GCC_except_table1059
- GCC_except_table1065
- GCC_except_table1070
- GCC_except_table1075
- GCC_except_table1079
- GCC_except_table136
- GCC_except_table150
- GCC_except_table159
- GCC_except_table168
- GCC_except_table176
- GCC_except_table387
- GCC_except_table395
- GCC_except_table407
- GCC_except_table428
- GCC_except_table433
- GCC_except_table444
- GCC_except_table455
- GCC_except_table460
- GCC_except_table463
- GCC_except_table469
- GCC_except_table472
- GCC_except_table483
- GCC_except_table521
- GCC_except_table534
- GCC_except_table538
- GCC_except_table545
- GCC_except_table554
- GCC_except_table567
- GCC_except_table572
- GCC_except_table576
- GCC_except_table578
- GCC_except_table587
- GCC_except_table596
- GCC_except_table604
- GCC_except_table608
- GCC_except_table612
- GCC_except_table651
- GCC_except_table656
- GCC_except_table663
- GCC_except_table670
- GCC_except_table674
- GCC_except_table679
- GCC_except_table683
- GCC_except_table685
- GCC_except_table687
- GCC_except_table701
- GCC_except_table702
- GCC_except_table706
- GCC_except_table716
- GCC_except_table719
- GCC_except_table740
- GCC_except_table742
- GCC_except_table754
- GCC_except_table756
- GCC_except_table761
- GCC_except_table773
- GCC_except_table778
- GCC_except_table783
- GCC_except_table807
- GCC_except_table810
- GCC_except_table814
- GCC_except_table817
- GCC_except_table819
- GCC_except_table822
- GCC_except_table824
- GCC_except_table836
- GCC_except_table855
- GCC_except_table862
- GCC_except_table869
- GCC_except_table872
- GCC_except_table877
- GCC_except_table88
- GCC_except_table880
- GCC_except_table886
- GCC_except_table899
- GCC_except_table908
- GCC_except_table919
- GCC_except_table920
- GCC_except_table938
- GCC_except_table962
- GCC_except_table972
- GCC_except_table976
- GCC_except_table983
- GCC_except_table986
- GCC_except_table987
- GCC_except_table990
- GCC_except_table993
- _OBJC_CLASS_$_AVURLAssetTrack
- _OBJC_CLASS_$__TtC7AVFCore28AVPlayerObservationRegistrar
- _OBJC_CLASS_$__TtC7AVFCore32AVPlayerItemObservationRegistrar
- _OBJC_CLASS_$__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- _OBJC_CLASS_$__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- _OBJC_IVAR_$_AVMetricEventStream._publishers
- _OBJC_METACLASS_$_AVURLAssetTrack
- _OBJC_METACLASS_$__TtC7AVFCore28AVPlayerObservationRegistrar
- _OBJC_METACLASS_$__TtC7AVFCore32AVPlayerItemObservationRegistrar
- _OBJC_METACLASS_$__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- _OBJC_METACLASS_$__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- __DATA__TtC7AVFCore28AVPlayerObservationRegistrar
- __DATA__TtC7AVFCore32AVPlayerItemObservationRegistrar
- __DATA__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- __DATA__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- __INSTANCE_METHODS__TtC7AVFCore28AVPlayerObservationRegistrar
- __INSTANCE_METHODS__TtC7AVFCore32AVPlayerItemObservationRegistrar
- __INSTANCE_METHODS__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- __INSTANCE_METHODS__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- __IVARS__TtC7AVFCore28AVPlayerObservationRegistrar
- __IVARS__TtC7AVFCore32AVPlayerItemObservationRegistrar
- __IVARS__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- __IVARS__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- __METACLASS_DATA__TtC7AVFCore28AVPlayerObservationRegistrar
- __METACLASS_DATA__TtC7AVFCore32AVPlayerItemObservationRegistrar
- __METACLASS_DATA__TtC7AVFCore33AVQueuePlayerObservationRegistrar
- __METACLASS_DATA__TtC7AVFCore37AVPlayerItemTrackObservationRegistrar
- __OBJC_CLASS_RO_$_AVURLAssetTrack
- __OBJC_METACLASS_RO_$_AVURLAssetTrack
- ___122-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:]_block_invoke.146
- ___28-[AVPlayer _allVideoTargets]_block_invoke
- ___31-[AVPlayerItem _updateTimebase]_block_invoke.654
- ___31-[AVPlayerItem _updateTimebase]_block_invoke_2.655
- ___35-[AVPlayerLayer _setPlayer:forPIP:]_block_invoke.293
- ___43-[AVMetadataItemFilterForSharing whitelist]_block_invoke
- ___53-[AVPlayerItem _configurePlaybackItemAndReturnError:]_block_invoke.507
- ___56-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke.307
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.992
- ___58-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevel]_block_invoke
- ___58-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevel]_block_invoke_2
- ___62-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue]_block_invoke.162
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1182
- ___63-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:]_block_invoke.170
- ___67-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoLayersAreAttached]_block_invoke
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1168
- ___67-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:]_block_invoke.278
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke.994
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2.995
- ___69-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_3
- ___70-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:]_block_invoke.147
- ___79-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:]_block_invoke.126
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke.139
- ___82-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:]_block_invoke_2.140
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1165
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1264
- ___Block_byref_object_copy_.141
- ___Block_byref_object_dispose_.142
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1421
- ___avplayer_fpNotificationCallback_block_invoke.1435
- ___avplayer_fpNotificationCallback_block_invoke.1438
- ___avplayer_fpNotificationCallback_block_invoke.1451
- ___avplayer_fpNotificationCallback_block_invoke.1459
- ___avplayer_fpNotificationCallback_block_invoke_2.1442
- ___avplayer_fpNotificationCallback_block_invoke_2.1455
- ___avplayer_fpNotificationCallback_block_invoke_3.1446
- ___avplayer_fpNotificationCallback_block_invoke_3.1456
- ___avplayer_fpNotificationCallback_block_invoke_4.1457
- ___avplayer_iapdNotificationCallback_block_invoke.1461
- ___avplayer_iapdNotificationCallback_block_invoke.1462
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1610
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1630
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1632
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1633
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1635
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1640
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1641
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1642
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1649
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1655
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1656
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1661
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1662
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1669
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1644
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1650
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1657
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1645
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1658
- ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1646
- ___avplayeritem_fpItemNotificationCallback_block_invoke_5.1647
- ___block_literal_global.1079
- ___block_literal_global.1081
- ___block_literal_global.1412
- ___block_literal_global.1465
- ___block_literal_global.1493
- ___block_literal_global.160
- ___block_literal_global.168
- ___block_literal_global.265
- ___block_literal_global.271
- ___block_literal_global.323
- ___block_literal_global.566
- ___block_literal_global.584
- ___block_literal_global.757
- ___block_literal_global.770
- ___block_literal_global.971
- ___unnamed_1
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AVFCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AVFCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AVFCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AVFCore
- _kFigAssetExportSessionProperty_MetadataItemFilterWhitelist
- _kFigAssetOptionKey_WhitelistQUIC
- _objc_msgSend$_allVideoTargets
- _objc_msgSend$_checkIfShouldAttachOutputsToFigPlayerOnStateQueue
- _objc_msgSend$_detachVideoLayersForSuspension
- _objc_msgSend$_hasForegroundLayers
- _objc_msgSend$_updateVideoTargetOnFigPlayer:synchronously:
- _objc_msgSend$addIdentifier:toWhitelistDictionary:
- _objc_msgSend$addKeySpace:key:toWhitelistDictionary:
- _objc_msgSend$initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:
- _objc_msgSend$initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:didSucceed:
- _objc_msgSend$initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:
- _objc_msgSend$setOverridesPreferredDynamicRangeForVideo:
- _objc_msgSend$whitelist
- _swift_getObjectType
- _swift_getSingletonMetadata
- _swift_initStackObject
- _swift_setDeallocating
- _swift_updateClassMetadata2
- _symbolic SDySS_____ySo12AVPlayerItemCGG 7AVFCore19RegistrarOperationsV
- _symbolic SDySS_____ySo17AVPlayerItemTrackCGG 7AVFCore19RegistrarOperationsV
- _symbolic SDySS_____ySo8AVPlayerCGG 7AVFCore19RegistrarOperationsV
- _symbolic SS______ySo13AVQueuePlayerCGt 7AVFCore19RegistrarOperationsV
- _symbolic So8NSObjectC
- _symbolic _____ 11Observation0A9RegistrarV
- _symbolic _____ 7AVFCore28AVPlayerObservationRegistrarC
- _symbolic _____ 7AVFCore32AVPlayerItemObservationRegistrarC
- _symbolic _____ 7AVFCore33AVQueuePlayerObservationRegistrarC
- _symbolic _____ 7AVFCore37AVPlayerItemTrackObservationRegistrarC
- _symbolic _____ySS______ySo13AVQueuePlayerCGtG s23_ContiguousArrayStorageC 7AVFCore19RegistrarOperationsV
- _symbolic y______xtc 11Observation0A9RegistrarV
- _type_layout_string 11Observation10ObservableRzl7AVFCore19RegistrarOperationsVyxG
- _whitelist.onceToken
- _whitelist.sWhitelist
CStrings:
+ " type in AVObservationRegistrar._registrar"
+ "+[AVMetadataItemFilterForSharing addIdentifier:toAllowListDictionary:]"
+ ", is a scrubbingLayer"
+ "-[AVPlayer _reevaluateVideoLayersAndTargetsForPresentationState:withCompletionHandler:]"
+ "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke"
+ "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2"
+ "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_3"
+ "-[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:withCompletionHandler:]"
+ "-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoDestinationsAreAttached]_block_invoke"
+ "-[AVPlayerCaptionLayer _setShowInterstitialInstead:]_block_invoke"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) Pausing item since cannot transition to background _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) attach video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) issue _reevaluateVideoLayersAndTargetsForPresentationState w/ DetachAllOutputs _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d, _hasAssociatedAVPlayerLayerInPIPMode %d"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) not updating video layers _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) skip _reevaluateVideoLayersAndTargetsForPresentationState  _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) skip attach video layers _hostApplicationInForeground %d _hasForegroundVideoDestinations %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
+ "<<<< AVPlayer >>>> %s: %@ (self=%p) w/ DetachLayersKeepingVideoTargetsAttached _hostApplicationInForeground %@ _hasForegroundVideoDestinations %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
+ "<<<< AVPlayer >>>> %s: %@ Host application is in foreground with foreground video output"
+ "<<<< AVPlayer >>>> %s: %@ has foreground layers, attaching video objects"
+ "<<<< AVPlayer >>>> %s: %@ has no more foreground video objects left, detaching video layers"
+ "<<<< AVPlayer >>>> %s: %@ releasing background assertion after finishing suspension"
+ "<<<< AVPlayer >>>> %s: skipping _didFinishSuspension, invalidating assertion immediately"
+ "<<<< AVPlayerCaptionLayer >>>> %s: _subtitleLayer(%p) clear"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ %p AVSampleBufferDisplayLayer's net flip status does match CoreAnimation default"
+ "<<<< AVSampleBufferDisplayLayer >>>> %s: %{public}@ %p AVSampleBufferDisplayLayer's net flip status does not match CoreAnimation default; adding a flip at videoLayer"
+ "<AVMetricHLSMediaSegmentRequestEvent:%p %@ indexFileURL:%@ isMapSegment:%d mediaType:%@ segmentDuration:%f mediaResourceRequestEvent:%@>"
+ "<AVMetricMediaRendition:%p stableID:%@ URL:%@>"
+ "<AVMetricPlayerItemVariantSwitchEvent:%p %@ fromVariant:%@ toVariant:%@ videoRendition:%@ audioRendition:%@ subtitleRendition:%@ loadedTimeRanges:%@ didSucceed:%d>"
+ "<AVMetricPlayerItemVariantSwitchStartEvent:%p %@ fromVariant:%@ toVariant:%@ videoRendition:%@ audioRendition:%@ subtitleRendition:%@ loadedTimeRanges:%@>"
+ "<AVPlayerLayer %p%@%@%@%@>"
+ "@\"AVMetricMediaRendition\""
+ "@\"AVPlayerItemObservationRegistrar\""
+ "@\"AVPlayerItemTrackObservationRegistrar\""
+ "@\"AVPlayerObservationRegistrar\""
+ "@\"AVQueuePlayerObservationRegistrar\""
+ "@104@0:8@16{?=qiIq}24@48@56@64@72@80@88@96"
+ "@108@0:8@16{?=qiIq}24@48@56@64@72@80@88@96B104"
+ "@108@0:8@16{?=qiIq}24@48@56{_NSRange=QQ}64B80@84d92@100"
+ "AVFCore/ObservationUtilities.swift"
+ "AVMetricMediaRendition"
+ "AVPlayerItemObservationRegistrar"
+ "AVPlayerItemTrackObservationRegistrar"
+ "AVPlayerLayer <%p> (scrubber)"
+ "AVPlayerObservationRegistrar"
+ "AVQueuePlayerObservationRegistrar"
+ "Fatal error"
+ "OverrideHEAACPrimingEditList"
+ "T@\"AVMetricMediaRendition\",R"
+ "Unexpectedly found "
+ "VideoLayerGeometryFlipped"
+ "_allClientAndVideoLayerVideoTargets"
+ "_audioRendition"
+ "_detachVideoDestinationsForSuspension"
+ "_detachVideoDestinationsForSuspensionWithCompletionHandler:"
+ "_didFinishSuspension:withCompletionHandler:"
+ "_ensureVideoDestinationsAreAttached"
+ "_hasForegroundVideoDestinations"
+ "_hasVideoDestinations"
+ "_reevaluateVideoLayersAndTargetsForPresentationState:withCompletionHandler:"
+ "_refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:"
+ "_segmentDuration"
+ "_shouldAttachVideoDestinationsToFigPlayerOnStateQueue"
+ "_stableID"
+ "_subtitleRendition"
+ "_updateVideoTargetsOnFigPlayer:withCompletionHandler:"
+ "_videoRendition"
+ "addIdentifier:toAllowListDictionary:"
+ "addKeySpace:key:toAllowListDictionary:"
+ "allowList"
+ "audioRendition"
+ "audioTapProcessorWasSet"
+ "i32@0:8q16@?24"
+ "initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:"
+ "initWithDate:mediaTime:sessionID:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:didSucceed:"
+ "initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:segmentDuration:mediaResourceRequestEvent:"
+ "initWithStableID:URL:"
+ "recommendedPixelBufferAttributes"
+ "renditionURL"
+ "segmentDuration"
+ "setVideoLayerGeometryFlipped:"
+ "stableID"
+ "subtitleRendition"
+ "videoRendition"
- "+[AVMetadataItemFilterForSharing addIdentifier:toWhitelistDictionary:]"
- "-[AVPlayer _reevaluateVideoLayersAndTargetsForPresentationState:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_2"
- "-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoLayersForSuspension]_block_invoke_3"
- "-[AVPlayer(AVPlayerMultitaskSupport) _didFinishSuspension:]"
- "-[AVPlayer(AVPlayerMultitaskSupport) _ensureVideoLayersAreAttached]_block_invoke"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) Pausing item since cannot transition to background _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) attach video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) issue _reevaluateVideoLayersAndTargetsForPresentationState w/ DetachAllOutputs _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d, _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) not updating video layers _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip _reevaluateVideoLayersAndTargetsForPresentationState  _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) skip attach video layers _hostApplicationInForeground %d _hasForegroundLayers %d _isVideoPlaybackAllowedWhileInBackground %d _hasAssociatedAVPlayerLayerInPIPMode %d"
- "<<<< AVPlayer >>>> %s: %@ (self=%p) w/ DetachLayersKeepingVideoTargetsAttached _hostApplicationInForeground %@ _hasForegroundLayers %@ _isVideoPlaybackAllowedWhileInBackground %@ _hasAssociatedAVPlayerLayerInPIPMode %@"
- "<<<< AVPlayer >>>> %s: %@ Host application is in foreground with foreground layers"
- "<<<< AVPlayer >>>> %s: %@ has foreground layers, attaching video layers"
- "<<<< AVPlayer >>>> %s: %@ has no more foreground layers left, detaching video layers"
- "<<<< AVPlayer >>>> %s: %@ releasing background assertion"
- "<<<< AVPlayer >>>> %s: skipping _didFinishSuspension"
- "<AVMetricHLSMediaSegmentRequestEvent:%p %@ indexFileURL:%@ isMapSegment:%d mediaType:%@ mediaResourceRequestEvent:%@>"
- "<AVMetricPlayerItemVariantSwitchEvent:%p %@ fromVariant:%@ toVariant:%@ loadedTimeRanges:%@ didSucceed:%d>"
- "<AVMetricPlayerItemVariantSwitchStartEvent:%p %@ fromVariant:%@ toVariant:%@ loadedTimeRanges:%@>"
- "<AVPlayerLayer %p%@%@%@>"
- "@\"_TtC7AVFCore28AVPlayerObservationRegistrar\""
- "@\"_TtC7AVFCore32AVPlayerItemObservationRegistrar\""
- "@\"_TtC7AVFCore33AVQueuePlayerObservationRegistrar\""
- "@\"_TtC7AVFCore37AVPlayerItemTrackObservationRegistrar\""
- "@100@0:8@16{?=qiIq}24@48@56{_NSRange=QQ}64B80@84@92"
- "@80@0:8@16{?=qiIq}24@48@56@64@72"
- "@84@0:8@16{?=qiIq}24@48@56@64@72B80"
- "AVURLAssetTrack"
- "_TtC7AVFCore28AVPlayerObservationRegistrar"
- "_TtC7AVFCore32AVPlayerItemObservationRegistrar"
- "_TtC7AVFCore33AVQueuePlayerObservationRegistrar"
- "_TtC7AVFCore37AVPlayerItemTrackObservationRegistrar"
- "_allVideoTargets"
- "_checkIfShouldAttachOutputsToFigPlayerOnStateQueue"
- "_detachVideoLayersForSuspension"
- "_hasForegroundLayers"
- "_publishers"
- "_updateVideoTargetOnFigPlayer:synchronously:"
- "addIdentifier:toWhitelistDictionary:"
- "addKeySpace:key:toWhitelistDictionary:"
- "initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:"
- "initWithDate:mediaTime:sessionID:fromVariant:toVariant:loadedTimeRanges:didSucceed:"
- "initWithDate:mediaTime:sessionID:indexFileURL:byteRange:isMapSegment:mediaType:mediaResourceRequestEvent:"
- "registrationOperationsForString"
- "setIgnoresPreferredDynamicRange:"
- "whitelist"

```
