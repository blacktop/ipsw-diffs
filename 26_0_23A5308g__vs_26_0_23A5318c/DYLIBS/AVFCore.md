## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2360.77.2.0.0
-  __TEXT.__text: 0x1b00d0
+2360.79.1.1.0
+  __TEXT.__text: 0x1b00dc
   __TEXT.__auth_stubs: 0x3bf0
-  __TEXT.__objc_methlist: 0x1aeec
-  __TEXT.__cstring: 0x23b46
+  __TEXT.__objc_methlist: 0x1afa4
+  __TEXT.__cstring: 0x23be6
   __TEXT.__const: 0x1dd0
-  __TEXT.__gcc_except_tab: 0x6954
-  __TEXT.__oslogstring: 0x3c3a
+  __TEXT.__gcc_except_tab: 0x6920
+  __TEXT.__oslogstring: 0x3c56
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x415
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x94c0
-  __TEXT.__objc_classname: 0x5e8b
-  __TEXT.__objc_methname: 0x35ff1
-  __TEXT.__objc_methtype: 0x9d77
-  __TEXT.__objc_stubs: 0x208c0
-  __DATA_CONST.__got: 0x4638
-  __DATA_CONST.__const: 0x55a0
-  __DATA_CONST.__objc_classlist: 0x1188
+  __TEXT.__unwind_info: 0x94c8
+  __TEXT.__objc_classname: 0x5ee3
+  __TEXT.__objc_methname: 0x360fa
+  __TEXT.__objc_methtype: 0x9da9
+  __TEXT.__objc_stubs: 0x209e0
+  __DATA_CONST.__got: 0x4630
+  __DATA_CONST.__const: 0x5578
+  __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab70
+  __DATA_CONST.__objc_selrefs: 0xabb0
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xcd8
+  __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x298
   __AUTH_CONST.__auth_got: 0x1e08
   __AUTH_CONST.__const: 0x1118
   __AUTH_CONST.__cfstring: 0x18de0
-  __AUTH_CONST.__objc_const: 0x30570
+  __AUTH_CONST.__objc_const: 0x30780
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x7970
+  __AUTH.__objc_data: 0x7a10
   __AUTH.__data: 0x1f8
-  __DATA.__objc_ivar: 0x2558
+  __DATA.__objc_ivar: 0x2574
   __DATA.__data: 0x1800
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x180
   __DATA.__bss: 0x13f0
   __DATA_DIRTY.__objc_data: 0x3660
   __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__common: 0x1a0
   __DATA_DIRTY.__bss: 0x1a0
-  __DATA_DIRTY.__common: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A74980A1-D779-3CF7-9510-2ACCD26591B5
-  Functions: 11353
-  Symbols:   38797
-  CStrings:  16704
+  UUID: CBAC2580-8195-3D71-AB19-402562833D2F
+  Functions: 11360
+  Symbols:   38838
+  CStrings:  16725
 
Symbols:
+ +[AVPlayerItemAudioTrackInfo playerItemTrackInfoForTrack:]
+ -[AVPlayerItem _setClientCaresAboutOverlappedPlayback]
+ -[AVPlayerItem(AVPlayerItemTrackInfoCaching) _audioChannelCountForTrack:]
+ -[AVPlayerItem(AVPlayerItemTrackInfoCaching) _cacheTrackInformation]
+ -[AVPlayerItemAudioTrackInfo hash]
+ -[AVPlayerItemAudioTrackInfo init]
+ -[AVPlayerItemAudioTrackInfo isEqual:]
+ -[AVPlayerItemAudioTrackInfo setChannelCount:]
+ -[AVPlayerItemAudioTrackInfoCache channelCountForTrack:]
+ -[AVPlayerItemAudioTrackInfoCache contains:]
+ -[AVPlayerItemAudioTrackInfoCache dealloc]
+ -[AVPlayerItemAudioTrackInfoCache init]
+ -[AVPlayerItemAudioTrackInfoCache store:]
+ -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _getChannelCountInFirstAudioTrackForItem:]
+ -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _updateCurrentOverlapStateGiven:hasStateChanged:]
+ GCC_except_table1004
+ GCC_except_table1006
+ GCC_except_table1017
+ GCC_except_table1021
+ GCC_except_table1025
+ GCC_except_table1029
+ GCC_except_table1034
+ GCC_except_table1036
+ GCC_except_table1039
+ GCC_except_table1043
+ GCC_except_table1045
+ GCC_except_table1051
+ GCC_except_table1055
+ GCC_except_table1059
+ GCC_except_table1063
+ GCC_except_table1069
+ GCC_except_table1073
+ GCC_except_table1076
+ GCC_except_table1081
+ GCC_except_table1085
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table204
+ GCC_except_table211
+ GCC_except_table225
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table247
+ GCC_except_table260
+ GCC_except_table282
+ GCC_except_table284
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table323
+ GCC_except_table343
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table368
+ GCC_except_table374
+ GCC_except_table380
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table400
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table416
+ GCC_except_table422
+ GCC_except_table424
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table452
+ GCC_except_table457
+ GCC_except_table469
+ GCC_except_table473
+ GCC_except_table476
+ GCC_except_table485
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table506
+ GCC_except_table508
+ GCC_except_table514
+ GCC_except_table516
+ GCC_except_table518
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table526
+ GCC_except_table528
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table541
+ GCC_except_table543
+ GCC_except_table548
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table559
+ GCC_except_table565
+ GCC_except_table569
+ GCC_except_table573
+ GCC_except_table574
+ GCC_except_table579
+ GCC_except_table581
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table587
+ GCC_except_table593
+ GCC_except_table601
+ GCC_except_table603
+ GCC_except_table605
+ GCC_except_table609
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table617
+ GCC_except_table619
+ GCC_except_table623
+ GCC_except_table625
+ GCC_except_table627
+ GCC_except_table634
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table643
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table651
+ GCC_except_table654
+ GCC_except_table656
+ GCC_except_table662
+ GCC_except_table666
+ GCC_except_table668
+ GCC_except_table670
+ GCC_except_table674
+ GCC_except_table675
+ GCC_except_table684
+ GCC_except_table686
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table693
+ GCC_except_table701
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table712
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table726
+ GCC_except_table730
+ GCC_except_table732
+ GCC_except_table734
+ GCC_except_table736
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table746
+ GCC_except_table747
+ GCC_except_table749
+ GCC_except_table751
+ GCC_except_table759
+ GCC_except_table761
+ GCC_except_table763
+ GCC_except_table765
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table778
+ GCC_except_table780
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table789
+ GCC_except_table791
+ GCC_except_table797
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table814
+ GCC_except_table818
+ GCC_except_table819
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table851
+ GCC_except_table853
+ GCC_except_table859
+ GCC_except_table866
+ GCC_except_table873
+ GCC_except_table876
+ GCC_except_table881
+ GCC_except_table884
+ GCC_except_table890
+ GCC_except_table892
+ GCC_except_table894
+ GCC_except_table896
+ GCC_except_table898
+ GCC_except_table900
+ GCC_except_table903
+ GCC_except_table912
+ GCC_except_table924
+ GCC_except_table942
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table948
+ GCC_except_table966
+ GCC_except_table976
+ GCC_except_table980
+ GCC_except_table987
+ GCC_except_table991
+ GCC_except_table994
+ GCC_except_table997
+ GCC_except_table999
+ _OBJC_CLASS_$_AVPlayerItemAudioTrackInfo
+ _OBJC_CLASS_$_AVPlayerItemAudioTrackInfoCache
+ _OBJC_IVAR_$_AVPlayerItemAudioTrackInfo.channelCount
+ _OBJC_IVAR_$_AVPlayerItemAudioTrackInfo.trackID
+ _OBJC_IVAR_$_AVPlayerItemAudioTrackInfoCache.availableTracks
+ _OBJC_IVAR_$_AVPlayerItemAudioTrackInfoCache.mutex
+ _OBJC_IVAR_$_AVPlayerItemInternal.audioTrackCache
+ _OBJC_IVAR_$_AVPlayerItemInternal.clientCaresAboutOverlappedPlayback
+ _OBJC_IVAR_$_AVQueuePlayerInternal.isOverlapCurrentlyAllowed
+ _OBJC_IVAR_$_AVQueuePlayerInternal.ivarMutex
+ _OBJC_METACLASS_$_AVPlayerItemAudioTrackInfo
+ _OBJC_METACLASS_$_AVPlayerItemAudioTrackInfoCache
+ __OBJC_$_CLASS_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching)
+ __OBJC_$_CLASS_METHODS_AVPlayerItemAudioTrackInfo
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItemAudioTrackInfo
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItemAudioTrackInfoCache
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerItemAudioTrackInfo
+ __OBJC_$_INSTANCE_VARIABLES_AVPlayerItemAudioTrackInfoCache
+ __OBJC_CLASS_PROTOCOLS_$_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching)
+ __OBJC_CLASS_RO_$_AVPlayerItemAudioTrackInfo
+ __OBJC_CLASS_RO_$_AVPlayerItemAudioTrackInfoCache
+ __OBJC_METACLASS_RO_$_AVPlayerItemAudioTrackInfo
+ __OBJC_METACLASS_RO_$_AVPlayerItemAudioTrackInfoCache
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1147
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1144
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1240
+ ___block_literal_global.131
+ ___block_literal_global.1388
+ ___block_literal_global.139
+ ___block_literal_global.142
+ ___block_literal_global.1424
+ ___block_literal_global.1450
+ ___block_literal_global.232
+ ___block_literal_global.238
+ ___block_literal_global.241
+ ___block_literal_global.278
+ ___block_literal_global.540
+ ___block_literal_global.568
+ ___block_literal_global.751
+ ___block_literal_global.760
+ ___block_literal_global.952
+ _gAVPlayerLayerTrace
+ _objc_msgSend$_audioChannelCountForTrack:
+ _objc_msgSend$_cacheTrackInformation
+ _objc_msgSend$_getChannelCountInFirstAudioTrackForItem:
+ _objc_msgSend$_setClientCaresAboutOverlappedPlayback
+ _objc_msgSend$_updateCurrentOverlapStateGiven:hasStateChanged:
+ _objc_msgSend$channelCountForTrack:
+ _objc_msgSend$contains:
+ _objc_msgSend$playerItemTrackInfoForTrack:
+ _objc_msgSend$setChannelCount:
+ _objc_msgSend$store:
+ _objc_msgSend$supportsAdvanceTimeForOverlappedPlayback
- -[AVPlayer _addListenersToInterstitialCoordinator:]
- -[AVPlayer _removeListenersFromInterstitialCoordinator:]
- GCC_except_table1003
- GCC_except_table1005
- GCC_except_table1016
- GCC_except_table1020
- GCC_except_table1024
- GCC_except_table1028
- GCC_except_table1033
- GCC_except_table1035
- GCC_except_table1038
- GCC_except_table1042
- GCC_except_table1044
- GCC_except_table1050
- GCC_except_table1054
- GCC_except_table1058
- GCC_except_table1062
- GCC_except_table1068
- GCC_except_table1072
- GCC_except_table1075
- GCC_except_table1080
- GCC_except_table1084
- GCC_except_table164
- GCC_except_table173
- GCC_except_table210
- GCC_except_table230
- GCC_except_table235
- GCC_except_table252
- GCC_except_table266
- GCC_except_table273
- GCC_except_table275
- GCC_except_table283
- GCC_except_table289
- GCC_except_table297
- GCC_except_table299
- GCC_except_table305
- GCC_except_table307
- GCC_except_table315
- GCC_except_table322
- GCC_except_table327
- GCC_except_table348
- GCC_except_table357
- GCC_except_table365
- GCC_except_table373
- GCC_except_table379
- GCC_except_table385
- GCC_except_table391
- GCC_except_table397
- GCC_except_table399
- GCC_except_table406
- GCC_except_table415
- GCC_except_table421
- GCC_except_table423
- GCC_except_table429
- GCC_except_table431
- GCC_except_table433
- GCC_except_table439
- GCC_except_table445
- GCC_except_table449
- GCC_except_table450
- GCC_except_table456
- GCC_except_table468
- GCC_except_table475
- GCC_except_table477
- GCC_except_table479
- GCC_except_table488
- GCC_except_table489
- GCC_except_table493
- GCC_except_table494
- GCC_except_table496
- GCC_except_table500
- GCC_except_table502
- GCC_except_table505
- GCC_except_table507
- GCC_except_table513
- GCC_except_table515
- GCC_except_table517
- GCC_except_table521
- GCC_except_table523
- GCC_except_table525
- GCC_except_table527
- GCC_except_table529
- GCC_except_table530
- GCC_except_table534
- GCC_except_table536
- GCC_except_table540
- GCC_except_table542
- GCC_except_table545
- GCC_except_table547
- GCC_except_table552
- GCC_except_table556
- GCC_except_table558
- GCC_except_table562
- GCC_except_table567
- GCC_except_table575
- GCC_except_table576
- GCC_except_table578
- GCC_except_table580
- GCC_except_table582
- GCC_except_table584
- GCC_except_table589
- GCC_except_table594
- GCC_except_table600
- GCC_except_table602
- GCC_except_table604
- GCC_except_table610
- GCC_except_table612
- GCC_except_table616
- GCC_except_table620
- GCC_except_table622
- GCC_except_table624
- GCC_except_table626
- GCC_except_table630
- GCC_except_table633
- GCC_except_table635
- GCC_except_table642
- GCC_except_table646
- GCC_except_table650
- GCC_except_table652
- GCC_except_table657
- GCC_except_table659
- GCC_except_table664
- GCC_except_table665
- GCC_except_table667
- GCC_except_table669
- GCC_except_table671
- GCC_except_table676
- GCC_except_table682
- GCC_except_table683
- GCC_except_table685
- GCC_except_table687
- GCC_except_table690
- GCC_except_table692
- GCC_except_table694
- GCC_except_table695
- GCC_except_table703
- GCC_except_table709
- GCC_except_table711
- GCC_except_table713
- GCC_except_table715
- GCC_except_table719
- GCC_except_table723
- GCC_except_table725
- GCC_except_table729
- GCC_except_table731
- GCC_except_table735
- GCC_except_table740
- GCC_except_table744
- GCC_except_table745
- GCC_except_table750
- GCC_except_table752
- GCC_except_table753
- GCC_except_table758
- GCC_except_table760
- GCC_except_table764
- GCC_except_table769
- GCC_except_table771
- GCC_except_table772
- GCC_except_table781
- GCC_except_table782
- GCC_except_table786
- GCC_except_table788
- GCC_except_table793
- GCC_except_table796
- GCC_except_table802
- GCC_except_table804
- GCC_except_table806
- GCC_except_table813
- GCC_except_table817
- GCC_except_table822
- GCC_except_table827
- GCC_except_table833
- GCC_except_table839
- GCC_except_table841
- GCC_except_table846
- GCC_except_table850
- GCC_except_table852
- GCC_except_table858
- GCC_except_table865
- GCC_except_table872
- GCC_except_table875
- GCC_except_table880
- GCC_except_table882
- GCC_except_table889
- GCC_except_table891
- GCC_except_table893
- GCC_except_table895
- GCC_except_table897
- GCC_except_table899
- GCC_except_table902
- GCC_except_table911
- GCC_except_table922
- GCC_except_table941
- GCC_except_table943
- GCC_except_table945
- GCC_except_table947
- GCC_except_table965
- GCC_except_table975
- GCC_except_table979
- GCC_except_table986
- GCC_except_table989
- GCC_except_table993
- GCC_except_table996
- GCC_except_table998
- _OBJC_IVAR_$_AVQueuePlayerInternal.canOverlapConditionState
- __OBJC_$_CLASS_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal)
- __OBJC_$_INSTANCE_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal)
- __OBJC_CLASS_PROTOCOLS_$_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal)
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1150
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1147
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1242
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_2
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_3
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4
- ___block_descriptor_57_e8_32o40o48o_e49_"AVPlayerRateState"20?0"AVPlayerRateState"8B16ls32l8s40l8s48l8
- ___block_literal_global.127
- ___block_literal_global.135
- ___block_literal_global.138
- ___block_literal_global.1390
- ___block_literal_global.1426
- ___block_literal_global.1452
- ___block_literal_global.228
- ___block_literal_global.234
- ___block_literal_global.237
- ___block_literal_global.274
- ___block_literal_global.536
- ___block_literal_global.564
- ___block_literal_global.747
- ___block_literal_global.756
- ___block_literal_global.955
- _avplayer_fpInterstitialCoordinatorNotificationCallback
- _getAudioChannelCountForFirstEnabledTrack
- _kFigPlayerInterstitialNotification_CurrentEventChangePrimaryPlaybackState
- _objc_msgSend$_addListenersToInterstitialCoordinator:
- _objc_msgSend$_removeListenersFromInterstitialCoordinator:
CStrings:
+ "-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:]_block_invoke_3"
+ "<<<< AVPlayerLayer >>>> %s: Setting interstitialLayer %p visibility to %d and primary (mask) layer %p visibility to %d"
+ "@\"AVPlayerItemAudioTrackInfoCache\""
+ "AVPlayerItemAudioTrackInfo"
+ "AVPlayerItemAudioTrackInfoCache"
+ "AVPlayerItemTrackInfoCaching"
+ "NO but channel count for one of the Buffered AirPlay items is unknown"
+ "NO since the player queue does not have enough items left"
+ "YES buffered airplay has matching multi channel tracks"
+ "YES buffered airplay has matching stereo or mono tracks"
+ "_audioChannelCountForTrack:"
+ "_cacheTrackInformation"
+ "_getChannelCountInFirstAudioTrackForItem:"
+ "_setClientCaresAboutOverlappedPlayback"
+ "_updateCurrentOverlapStateGiven:hasStateChanged:"
+ "audioTrackCache"
+ "availableTracks"
+ "avplayerlayer_trace"
+ "channelCountForTrack:"
+ "clientCaresAboutOverlappedPlayback"
+ "contains:"
+ "i28@0:8i16^B20"
+ "isOverlapCurrentlyAllowed"
+ "ivarMutex"
+ "mutex"
+ "playerItemTrackInfoForTrack:"
+ "setChannelCount:"
+ "store:"
- "<<<< AVPlayer >>>> %s: %{public}@ no change to timeControlStatus or reasonForWaitingToPlay"
- "YES buffered airplay has matching channel count"
- "_addListenersToInterstitialCoordinator:"
- "_removeListenersFromInterstitialCoordinator:"
- "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke"
- "avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke_4"
- "canOverlapConditionState"

```
