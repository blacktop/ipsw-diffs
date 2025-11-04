## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2390.10.1.0.0
-  __TEXT.__text: 0x1b1268
-  __TEXT.__auth_stubs: 0x3c00
-  __TEXT.__objc_methlist: 0x1aff4
-  __TEXT.__cstring: 0x24166
-  __TEXT.__const: 0x1e38
-  __TEXT.__gcc_except_tab: 0x6958
-  __TEXT.__oslogstring: 0x3c9a
+2395.3.2.0.0
+  __TEXT.__text: 0x1b20cc
+  __TEXT.__auth_stubs: 0x3c70
+  __TEXT.__objc_methlist: 0x1b044
+  __TEXT.__cstring: 0x242c6
+  __TEXT.__const: 0x1e48
+  __TEXT.__gcc_except_tab: 0x6998
+  __TEXT.__oslogstring: 0x3fad
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x415
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x94f8
+  __TEXT.__unwind_info: 0x9530
   __TEXT.__objc_classname: 0x5f08
-  __TEXT.__objc_methname: 0x3629a
-  __TEXT.__objc_methtype: 0x9dc3
-  __TEXT.__objc_stubs: 0x20a60
-  __DATA_CONST.__got: 0x4658
+  __TEXT.__objc_methname: 0x363be
+  __TEXT.__objc_methtype: 0x9df5
+  __TEXT.__objc_stubs: 0x20b40
+  __DATA_CONST.__got: 0x4660
   __DATA_CONST.__const: 0x56b8
   __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xabe8
+  __DATA_CONST.__objc_selrefs: 0xac18
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x308
-  __AUTH_CONST.__auth_got: 0x1e10
+  __AUTH_CONST.__auth_got: 0x1e48
   __AUTH_CONST.__const: 0x1118
-  __AUTH_CONST.__cfstring: 0x190e0
-  __AUTH_CONST.__objc_const: 0x307e0
+  __AUTH_CONST.__cfstring: 0x19140
+  __AUTH_CONST.__objc_const: 0x30830
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x7a10
   __AUTH.__data: 0x1f8
-  __DATA.__objc_ivar: 0x257c
+  __DATA.__objc_ivar: 0x2584
   __DATA.__data: 0x1800
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x160

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E70BFBC7-DE41-3B5B-BB94-F6484E89F4B6
-  Functions: 11376
-  Symbols:   38909
-  CStrings:  16786
+  UUID: 3E81AA9A-EA87-31CB-A8B3-04CF6D0526CB
+  Functions: 11387
+  Symbols:   38949
+  CStrings:  16810
 
Symbols:
+ -[AVPlaybackCoordinationMedium _lockedSeeksEnabled]
+ -[AVPlaybackCoordinationMedium attachVideoTargetsForSynchronization:videoTargets:]
+ -[AVPlaybackCoordinationMedium startCoordinatingVideoTargetsForSynchronization]
+ -[AVPlayer _attachVideoLayersAndTargetsToCoordinationMedium]
+ -[AVPlayer _setupVideoLayersAndTargetsForPresentationStateWithCoordinationMedium:]
+ -[AVPlayerPlaybackCoordinator localParticipantUUIDString]
+ GCC_except_table117
+ GCC_except_table138
+ GCC_except_table195
+ GCC_except_table205
+ GCC_except_table210
+ GCC_except_table393
+ GCC_except_table401
+ GCC_except_table405
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table433
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table456
+ GCC_except_table468
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table488
+ GCC_except_table493
+ GCC_except_table500
+ GCC_except_table529
+ GCC_except_table534
+ GCC_except_table542
+ GCC_except_table562
+ GCC_except_table567
+ GCC_except_table575
+ GCC_except_table580
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table589
+ GCC_except_table604
+ GCC_except_table612
+ GCC_except_table616
+ GCC_except_table620
+ GCC_except_table622
+ GCC_except_table626
+ GCC_except_table630
+ GCC_except_table642
+ GCC_except_table646
+ GCC_except_table652
+ GCC_except_table657
+ GCC_except_table659
+ GCC_except_table664
+ GCC_except_table669
+ GCC_except_table671
+ GCC_except_table676
+ GCC_except_table682
+ GCC_except_table687
+ GCC_except_table692
+ GCC_except_table694
+ GCC_except_table703
+ GCC_except_table711
+ GCC_except_table715
+ GCC_except_table723
+ GCC_except_table725
+ GCC_except_table729
+ GCC_except_table740
+ GCC_except_table744
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table764
+ GCC_except_table769
+ GCC_except_table771
+ GCC_except_table781
+ GCC_except_table788
+ GCC_except_table793
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table846
+ _FigParticipantStateDictionaryGetStateLoggingIdentifier
+ _FigTimelineStateDictionaryGetStateVideoTargetSynchronizationIdentifier
+ _FigVideoTargetConfigurationSynchronizerAbortCurrentSynchronization
+ _FigVideoTargetConfigurationSynchronizerCoordinateAndCopySynchronizationID
+ _FigVideoTargetConfigurationSynchronizerCopyCurrentSynchronizationID
+ _FigVideoTargetConfigurationSynchronizerCreate
+ _FigVideoTargetConfigurationSynchronizerUpdateTargets
+ _OBJC_IVAR_$_AVHUDStringGenerator._currentDate
+ _OBJC_IVAR_$_AVPlaybackCoordinationMedium._videoTargetsSynchronizer
+ ___57-[AVPlayerPlaybackCoordinator localParticipantUUIDString]_block_invoke
+ ___60-[AVPlayer _attachVideoLayersAndTargetsToCoordinationMedium]_block_invoke
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1149
+ ___79-[AVPlaybackCoordinationMedium startCoordinatingVideoTargetsForSynchronization]_block_invoke
+ ___82-[AVPlaybackCoordinationMedium attachVideoTargetsForSynchronization:videoTargets:]_block_invoke
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1146
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1242
+ ___block_literal_global.1390
+ ___block_literal_global.1426
+ ___block_literal_global.1452
+ ___block_literal_global.954
+ _kFigPlaybackItemSetTimeOption_VideoTargetSynchronizationIdentifier
+ _objc_msgSend$_attachVideoLayersAndTargetsToCoordinationMedium
+ _objc_msgSend$_lockedSeeksEnabled
+ _objc_msgSend$_setupVideoLayersAndTargetsForPresentationStateWithCoordinationMedium:
+ _objc_msgSend$attachVideoTargetsForSynchronization:videoTargets:
+ _objc_msgSend$currentDate
+ _objc_msgSend$localParticipantUUIDString
+ _objc_msgSend$startCoordinatingVideoTargetsForSynchronization
- GCC_except_table136
- GCC_except_table189
- GCC_except_table203
- GCC_except_table37
- GCC_except_table390
- GCC_except_table402
- GCC_except_table409
- GCC_except_table411
- GCC_except_table435
- GCC_except_table437
- GCC_except_table444
- GCC_except_table453
- GCC_except_table457
- GCC_except_table462
- GCC_except_table471
- GCC_except_table485
- GCC_except_table539
- GCC_except_table543
- GCC_except_table550
- GCC_except_table554
- GCC_except_table564
- GCC_except_table569
- GCC_except_table574
- GCC_except_table581
- GCC_except_table592
- GCC_except_table609
- GCC_except_table617
- GCC_except_table619
- GCC_except_table623
- GCC_except_table637
- GCC_except_table639
- GCC_except_table643
- GCC_except_table649
- GCC_except_table654
- GCC_except_table656
- GCC_except_table661
- GCC_except_table673
- GCC_except_table675
- GCC_except_table677
- GCC_except_table679
- GCC_except_table689
- GCC_except_table693
- GCC_except_table700
- GCC_except_table705
- GCC_except_table707
- GCC_except_table712
- GCC_except_table722
- GCC_except_table734
- GCC_except_table741
- GCC_except_table747
- GCC_except_table749
- GCC_except_table751
- GCC_except_table763
- GCC_except_table768
- GCC_except_table770
- GCC_except_table778
- GCC_except_table780
- GCC_except_table785
- GCC_except_table790
- GCC_except_table819
- GCC_except_table824
- GCC_except_table826
- GCC_except_table831
- GCC_except_table843
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1147
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1144
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1240
- ___block_literal_global.1388
- ___block_literal_global.1424
- ___block_literal_global.1450
- ___block_literal_global.429
- ___block_literal_global.952
CStrings:
+ "-[AVPlaybackCoordinationMedium _updateTransportControlState:forIdentifier:]_block_invoke"
+ "-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastLocalParticipantStateDictionary:]"
+ "-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:]"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ broadcasting participant state dictionary %{public}@ received from coordinator %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ broadcasting transport control state dictionary %{public}@ for item identifier %@ received from coordinator %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ skipping update to transport control state %{public}@ for item identifier %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ updating transport control state for item identifier %@ from %{public}@ to %{public}@ with vtsid: %@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ broadcast participant state %{public}@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ broadcast transport control state %{public}@"
+ "<<<< AVPlaybackCoordinator >>>> %s: %@ reload transport control state"
+ "^{OpaqueFigVideoTargetConfigurationSynchronizer=}"
+ "_attachVideoLayersAndTargetsToCoordinationMedium"
+ "_lockedSeeksEnabled"
+ "_setupVideoLayersAndTargetsForPresentationStateWithCoordinationMedium:"
+ "_videoTargetsSynchronizer"
+ "attachVideoTargetsForSynchronization:videoTargets:"
+ "current date:%@\n"
+ "localParticipantUUIDString"
+ "locked_seek"
+ "startCoordinatingVideoTargetsForSynchronization"
+ "yyyy-MM-dd'T'HH:mm:ss.SSS"

```
