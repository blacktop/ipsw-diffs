## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2475.13.1.1.0
-  __TEXT.__text: 0x1bd580
+2485.5.1.0.0
+  __TEXT.__text: 0x1be790
   __TEXT.__delay_helper: 0x1bc
-  __TEXT.__objc_methlist: 0x1c2fc
-  __TEXT.__cstring: 0x26f53
-  __TEXT.__gcc_except_tab: 0xa044
+  __TEXT.__objc_methlist: 0x1c3c4
+  __TEXT.__cstring: 0x27203
+  __TEXT.__gcc_except_tab: 0xa16c
   __TEXT.__const: 0x1e48
-  __TEXT.__oslogstring: 0x5128
+  __TEXT.__oslogstring: 0x50ad
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x40d

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0xc508
+  __TEXT.__unwind_info: 0xc5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5be0
+  __DATA_CONST.__const: 0x5c68
   __DATA_CONST.__objc_classlist: 0x1240
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb6b8
+  __DATA_CONST.__objc_selrefs: 0xb730
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xd70
-  __DATA_CONST.__objc_arraydata: 0x310
-  __DATA_CONST.__got: 0x4850
-  __AUTH_CONST.__const: 0x1258
-  __AUTH_CONST.__cfstring: 0x1a6a0
-  __AUTH_CONST.__objc_const: 0x32bd8
+  __DATA_CONST.__objc_arraydata: 0x368
+  __DATA_CONST.__got: 0x4870
+  __AUTH_CONST.__const: 0x1278
+  __AUTH_CONST.__cfstring: 0x1a8e0
+  __AUTH_CONST.__objc_const: 0x32d08
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH_CONST.__objc_arrayobj: 0x360
+  __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2040
+  __AUTH_CONST.__auth_got: 0x2050
   __AUTH.__objc_data: 0x81e0
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x27fc
+  __DATA.__objc_ivar: 0x2810
   __DATA.__data: 0x184c
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1e0
   __DATA_DIRTY.__objc_data: 0x3520
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x1e0
-  __DATA_DIRTY.__bss: 0x1e9
+  __DATA_DIRTY.__bss: 0x1f9
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12122
-  Symbols:   23984
-  CStrings:  4304
+  Functions: 12159
+  Symbols:   24052
+  CStrings:  4322
 
Symbols:
+ +[AVPlayerItemVideoOutput(AVPlayerItemVideoOutput_UnitTestOnly) _setImageAvailableCallbackAfterPromotionTestHook:]
+ +[AVURLAsset(AVURLAssetConnectionPrewarming) setUpConnectionForURL:options:completionHandler:]
+ -[AVPlayer appliesLoudnessAdjustmentsAutomatically]
+ -[AVPlayer setAppliesLoudnessAdjustmentsAutomatically:]
+ -[AVPlayerItem _updateContentLibraryLoudnessTargetOnFigPlaybackItem]
+ -[AVPlayerItem _updateContentTypeForLoudnessControlOnFigPlaybackItem]
+ -[AVPlayerItem _updateLoudnessControlModeOnFigPlaybackItem]
+ -[AVPlayerItem prefersAudioVideoVariants]
+ -[AVPlayerItem setPrefersAudioVideoVariants:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) allowedAudioSpatializationFormats]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) audioMix]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) audioTimePitchAlgorithm]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) isAudioSpatializationAllowed]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) setAllowedAudioSpatializationFormats:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioMix:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioSpatializationAllowed:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioTimePitchAlgorithm:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing_Private) audioTapProcessor]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing_Private) loudnessInfo]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing_Private) resetAudioBufferedAhead]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing_Private) setAudioTapProcessor:]
+ -[AVPlayerItem(AVPlayerItemAudioProcessing_Private) setLoudnessInfo:]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) contentLibraryLoudnessTarget]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) contentTypeForLoudnessControl]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) loudnessControlMode]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) setContentLibraryLoudnessTarget:]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) setContentTypeForLoudnessControl:]
+ -[AVPlayerItem(AVPlayerItemLoudnessControl) setLoudnessControlMode:]
+ GCC_except_table1001
+ GCC_except_table1003
+ GCC_except_table1014
+ GCC_except_table1032
+ GCC_except_table1037
+ GCC_except_table1039
+ GCC_except_table1041
+ GCC_except_table1042
+ GCC_except_table1043
+ GCC_except_table1046
+ GCC_except_table1051
+ GCC_except_table1055
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1073
+ GCC_except_table1077
+ GCC_except_table1082
+ GCC_except_table1086
+ GCC_except_table1087
+ GCC_except_table1089
+ GCC_except_table1091
+ GCC_except_table1095
+ GCC_except_table1098
+ GCC_except_table1101
+ GCC_except_table1108
+ GCC_except_table1112
+ GCC_except_table1116
+ GCC_except_table1120
+ GCC_except_table1125
+ GCC_except_table1130
+ GCC_except_table1134
+ GCC_except_table1137
+ GCC_except_table1142
+ GCC_except_table1144
+ GCC_except_table1147
+ GCC_except_table1148
+ GCC_except_table1155
+ GCC_except_table282
+ GCC_except_table285
+ GCC_except_table291
+ GCC_except_table304
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table323
+ GCC_except_table334
+ GCC_except_table341
+ GCC_except_table347
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table365
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table384
+ GCC_except_table387
+ GCC_except_table402
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table426
+ GCC_except_table436
+ GCC_except_table439
+ GCC_except_table452
+ GCC_except_table458
+ GCC_except_table465
+ GCC_except_table467
+ GCC_except_table470
+ GCC_except_table479
+ GCC_except_table483
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table537
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table549
+ GCC_except_table552
+ GCC_except_table560
+ GCC_except_table565
+ GCC_except_table568
+ GCC_except_table576
+ GCC_except_table588
+ GCC_except_table593
+ GCC_except_table599
+ GCC_except_table606
+ GCC_except_table615
+ GCC_except_table617
+ GCC_except_table620
+ GCC_except_table621
+ GCC_except_table624
+ GCC_except_table628
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table643
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table651
+ GCC_except_table653
+ GCC_except_table655
+ GCC_except_table657
+ GCC_except_table658
+ GCC_except_table660
+ GCC_except_table663
+ GCC_except_table668
+ GCC_except_table670
+ GCC_except_table674
+ GCC_except_table676
+ GCC_except_table686
+ GCC_except_table687
+ GCC_except_table691
+ GCC_except_table693
+ GCC_except_table704
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table720
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table726
+ GCC_except_table739
+ GCC_except_table741
+ GCC_except_table744
+ GCC_except_table746
+ GCC_except_table756
+ GCC_except_table760
+ GCC_except_table761
+ GCC_except_table766
+ GCC_except_table772
+ GCC_except_table775
+ GCC_except_table783
+ GCC_except_table786
+ GCC_except_table788
+ GCC_except_table802
+ GCC_except_table804
+ GCC_except_table813
+ GCC_except_table815
+ GCC_except_table817
+ GCC_except_table819
+ GCC_except_table831
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table844
+ GCC_except_table847
+ GCC_except_table855
+ GCC_except_table858
+ GCC_except_table864
+ GCC_except_table867
+ GCC_except_table868
+ GCC_except_table871
+ GCC_except_table879
+ GCC_except_table881
+ GCC_except_table895
+ GCC_except_table907
+ GCC_except_table911
+ GCC_except_table915
+ GCC_except_table926
+ GCC_except_table930
+ GCC_except_table934
+ GCC_except_table936
+ GCC_except_table947
+ GCC_except_table948
+ GCC_except_table952
+ GCC_except_table959
+ GCC_except_table960
+ GCC_except_table978
+ GCC_except_table982
+ GCC_except_table984
+ GCC_except_table986
+ GCC_except_table988
+ GCC_except_table990
+ GCC_except_table992
+ GCC_except_table997
+ GCC_except_table999
+ _AVLoudnessControlModeAdvertisement
+ _AVLoudnessControlModeUseItemMeasurement
+ _AVLoudnessControlModeUseSequenceMeasurement
+ _AVMetadataIdentifierISOUserDataAudioStreamLoudness
+ _AVMetadataIdentifierISOUserDataContentTypeForLoudnessControl
+ _AVMetadataIdentifierQuickTimeUserDataAudioStreamLoudness
+ _AVMetadataIdentifierQuickTimeUserDataContentTypeForLoudnessControl
+ _AVPlayerItemVideoOutputReleaseContext
+ _AVQuickTimeContentTypeForLoudnessControlAlarm
+ _AVQuickTimeContentTypeForLoudnessControlAudiobookPodcastOrRadioProgram
+ _AVQuickTimeContentTypeForLoudnessControlDeviceCaptureOrUserGenerated
+ _AVQuickTimeContentTypeForLoudnessControlLiveAudiovisualProduction
+ _AVQuickTimeContentTypeForLoudnessControlMusic
+ _AVQuickTimeContentTypeForLoudnessControlOnDemandAudiovisualProduction
+ _AVQuickTimeContentTypeForLoudnessControlOtherSystemSound
+ _AVQuickTimeContentTypeForLoudnessControlRingtone
+ _AVQuickTimeContentTypeForLoudnessControlSynthesizedSpeech
+ _AVQuickTimeContentTypeForLoudnessControlToCTLCContentType
+ _AVQuickTimeContentTypeForLoudnessControlUserInterfaceFeedback
+ _FigAssetRemoteSetUpConnectionForURLAsync
+ _OBJC_IVAR_$_AVPlayerInternal.appliesLoudnessAdjustmentsAutomatically
+ _OBJC_IVAR_$_AVPlayerItemInternal.contentLibraryLoudnessTarget
+ _OBJC_IVAR_$_AVPlayerItemInternal.contentTypeForLoudnessControl
+ _OBJC_IVAR_$_AVPlayerItemInternal.loudnessControlMode
+ _OBJC_IVAR_$_AVPlayerItemInternal.prefersAudioVideoVariants
+ __OBJC_$_CLASS_METHODS_AVPlayerItem(AVPlayerItemAudioProcessing|AVPlayerItemAudioProcessing_Private|AVPlayerItemLoudnessControl|AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
+ __OBJC_$_CLASS_METHODS_AVPlayerItemVideoOutput(AVPlayerItemVideoOutput_UnitTestOnly)
+ __OBJC_$_CLASS_METHODS_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset|AVURLAssetConnectionPrewarming)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItem(AVPlayerItemAudioProcessing|AVPlayerItemAudioProcessing_Private|AVPlayerItemLoudnessControl|AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
+ __OBJC_$_INSTANCE_METHODS_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset|AVURLAssetConnectionPrewarming)
+ __OBJC_CLASS_PROTOCOLS_$_AVPlayerItem(AVPlayerItemAudioProcessing|AVPlayerItemAudioProcessing_Private|AVPlayerItemLoudnessControl|AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
+ __OBJC_CLASS_PROTOCOLS_$_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset|AVURLAssetConnectionPrewarming)
+ ___41-[AVPlayerItem prefersAudioVideoVariants]_block_invoke
+ ___45-[AVPlayerItem setPrefersAudioVideoVariants:]_block_invoke
+ ___45-[AVPlayerItem setPrefersAudioVideoVariants:]_block_invoke_2
+ ___51-[AVPlayer appliesLoudnessAdjustmentsAutomatically]_block_invoke
+ ___53-[AVPlayerItem(AVPlayerItemAudioProcessing) audioMix]_block_invoke
+ ___55-[AVPlayer setAppliesLoudnessAdjustmentsAutomatically:]_block_invoke
+ ___55-[AVPlayer setAppliesLoudnessAdjustmentsAutomatically:]_block_invoke_2
+ ___57-[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioMix:]_block_invoke
+ ___57-[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioMix:]_block_invoke_2
+ ___59-[AVPlayerItem _updateLoudnessControlModeOnFigPlaybackItem]_block_invoke
+ ___64-[AVPlayerItem(AVPlayerItemLoudnessControl) loudnessControlMode]_block_invoke
+ ___65-[AVPlayerItem(AVPlayerItemAudioProcessing_Private) loudnessInfo]_block_invoke
+ ___68-[AVPlayerItem _updateContentLibraryLoudnessTargetOnFigPlaybackItem]_block_invoke
+ ___68-[AVPlayerItem(AVPlayerItemAudioProcessing) audioTimePitchAlgorithm]_block_invoke
+ ___68-[AVPlayerItem(AVPlayerItemLoudnessControl) setLoudnessControlMode:]_block_invoke
+ ___69-[AVPlayerItem _updateContentTypeForLoudnessControlOnFigPlaybackItem]_block_invoke
+ ___69-[AVPlayerItem(AVPlayerItemAudioProcessing_Private) setLoudnessInfo:]_block_invoke
+ ___70-[AVPlayerItem(AVPlayerItemAudioProcessing_Private) audioTapProcessor]_block_invoke
+ ___72-[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioTimePitchAlgorithm:]_block_invoke
+ ___73-[AVPlayerItem(AVPlayerItemAudioProcessing) isAudioSpatializationAllowed]_block_invoke
+ ___73-[AVPlayerItem(AVPlayerItemLoudnessControl) contentLibraryLoudnessTarget]_block_invoke
+ ___74-[AVPlayerItem(AVPlayerItemLoudnessControl) contentTypeForLoudnessControl]_block_invoke
+ ___75-[AVPlayerItem(AVPlayerItemAudioProcessing) setAudioSpatializationAllowed:]_block_invoke
+ ___76-[AVPlayerItem(AVPlayerItemAudioProcessing_Private) resetAudioBufferedAhead]_block_invoke
+ ___77-[AVPlayerItem(AVPlayerItemLoudnessControl) setContentLibraryLoudnessTarget:]_block_invoke
+ ___78-[AVPlayerItem(AVPlayerItemAudioProcessing) allowedAudioSpatializationFormats]_block_invoke
+ ___78-[AVPlayerItem(AVPlayerItemLoudnessControl) setContentTypeForLoudnessControl:]_block_invoke
+ ___82-[AVPlayerItem(AVPlayerItemAudioProcessing) setAllowedAudioSpatializationFormats:]_block_invoke
+ ___94+[AVURLAsset(AVURLAssetConnectionPrewarming) setUpConnectionForURL:options:completionHandler:]_block_invoke
+ ___94+[AVURLAsset(AVURLAssetConnectionPrewarming) setUpConnectionForURL:options:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32b_e8_v12?0i8ls32l8
+ ___getSetUpConnectionCompletionQueue_block_invoke
+ _dispatch_async_f
+ _kFigPlaybackItemProperty_ContentLibraryLoudnessTarget
+ _kFigPlaybackItemProperty_ContentTypeForLoudnessControl
+ _kFigPlaybackItemProperty_LoudnessControlMode
+ _kFigPlaybackItemProperty_PrefersAudioVideoVariants
+ _kFigPlayerProperty_AppliesLoudnessAdjustmentsAutomatically
+ _sImageAvailableCallbackAfterPromotionTestHook
- -[AVPlayerItem allowedAudioSpatializationFormats]
- -[AVPlayerItem audioMix]
- -[AVPlayerItem audioTapProcessor]
- -[AVPlayerItem audioTimePitchAlgorithm]
- -[AVPlayerItem isAudioSpatializationAllowed]
- -[AVPlayerItem loudnessInfo]
- -[AVPlayerItem resetAudioBufferedAhead]
- -[AVPlayerItem setAllowedAudioSpatializationFormats:]
- -[AVPlayerItem setAudioMix:]
- -[AVPlayerItem setAudioSpatializationAllowed:]
- -[AVPlayerItem setAudioTapProcessor:]
- -[AVPlayerItem setAudioTimePitchAlgorithm:]
- -[AVPlayerItem setLoudnessInfo:]
- GCC_except_table1006
- GCC_except_table1012
- GCC_except_table1017
- GCC_except_table1019
- GCC_except_table1021
- GCC_except_table1022
- GCC_except_table1023
- GCC_except_table1029
- GCC_except_table1031
- GCC_except_table1035
- GCC_except_table1036
- GCC_except_table1038
- GCC_except_table1053
- GCC_except_table1057
- GCC_except_table1062
- GCC_except_table1066
- GCC_except_table1067
- GCC_except_table1071
- GCC_except_table1072
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1078
- GCC_except_table1081
- GCC_except_table1084
- GCC_except_table1088
- GCC_except_table1100
- GCC_except_table1105
- GCC_except_table1107
- GCC_except_table1110
- GCC_except_table1114
- GCC_except_table1117
- GCC_except_table1122
- GCC_except_table1128
- GCC_except_table1135
- GCC_except_table280
- GCC_except_table286
- GCC_except_table290
- GCC_except_table294
- GCC_except_table302
- GCC_except_table309
- GCC_except_table318
- GCC_except_table325
- GCC_except_table329
- GCC_except_table342
- GCC_except_table349
- GCC_except_table352
- GCC_except_table360
- GCC_except_table361
- GCC_except_table369
- GCC_except_table375
- GCC_except_table377
- GCC_except_table381
- GCC_except_table392
- GCC_except_table410
- GCC_except_table411
- GCC_except_table413
- GCC_except_table425
- GCC_except_table431
- GCC_except_table433
- GCC_except_table434
- GCC_except_table447
- GCC_except_table449
- GCC_except_table450
- GCC_except_table461
- GCC_except_table462
- GCC_except_table471
- GCC_except_table478
- GCC_except_table492
- GCC_except_table493
- GCC_except_table496
- GCC_except_table501
- GCC_except_table504
- GCC_except_table507
- GCC_except_table510
- GCC_except_table518
- GCC_except_table521
- GCC_except_table523
- GCC_except_table529
- GCC_except_table535
- GCC_except_table540
- GCC_except_table545
- GCC_except_table548
- GCC_except_table550
- GCC_except_table551
- GCC_except_table556
- GCC_except_table557
- GCC_except_table558
- GCC_except_table569
- GCC_except_table570
- GCC_except_table573
- GCC_except_table582
- GCC_except_table584
- GCC_except_table594
- GCC_except_table600
- GCC_except_table604
- GCC_except_table608
- GCC_except_table613
- GCC_except_table625
- GCC_except_table627
- GCC_except_table633
- GCC_except_table642
- GCC_except_table644
- GCC_except_table645
- GCC_except_table648
- GCC_except_table650
- GCC_except_table662
- GCC_except_table665
- GCC_except_table677
- GCC_except_table678
- GCC_except_table679
- GCC_except_table682
- GCC_except_table684
- GCC_except_table688
- GCC_except_table697
- GCC_except_table701
- GCC_except_table713
- GCC_except_table715
- GCC_except_table729
- GCC_except_table730
- GCC_except_table734
- GCC_except_table743
- GCC_except_table749
- GCC_except_table752
- GCC_except_table757
- GCC_except_table758
- GCC_except_table765
- GCC_except_table771
- GCC_except_table773
- GCC_except_table779
- GCC_except_table781
- GCC_except_table792
- GCC_except_table805
- GCC_except_table816
- GCC_except_table818
- GCC_except_table821
- GCC_except_table822
- GCC_except_table824
- GCC_except_table826
- GCC_except_table842
- GCC_except_table843
- GCC_except_table845
- GCC_except_table846
- GCC_except_table849
- GCC_except_table861
- GCC_except_table862
- GCC_except_table863
- GCC_except_table866
- GCC_except_table870
- GCC_except_table884
- GCC_except_table886
- GCC_except_table896
- GCC_except_table900
- GCC_except_table908
- GCC_except_table912
- GCC_except_table914
- GCC_except_table916
- GCC_except_table927
- GCC_except_table940
- GCC_except_table958
- GCC_except_table962
- GCC_except_table964
- GCC_except_table966
- GCC_except_table968
- GCC_except_table970
- GCC_except_table972
- GCC_except_table974
- GCC_except_table977
- GCC_except_table979
- GCC_except_table981
- GCC_except_table983
- __OBJC_$_CLASS_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
- __OBJC_$_CLASS_METHODS_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset)
- __OBJC_$_INSTANCE_METHODS_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
- __OBJC_$_INSTANCE_METHODS_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset)
- __OBJC_CLASS_PROTOCOLS_$_AVPlayerItem(AVPlayerItemCustomMediaSelectionScheme|AVPlayerItemCustomMediaSelectionScheme_Private|AVPlayerItemProtectedContent|AVPlayerItemProtectedContentPrivate|AVPlayerItemLogging|AVPlayerItemSupportForMediaPlayer|AVPlayerItemOutputs|AVPlayerItemMediaDataCollectors|AVPlayerItemServiceIdentifier_Private|LegibleOutputSupport|MetadataOutputSupport|RenderedLegibleOutputSupport|SwiftMedia|AVPlayerItemAVKit|AVPlayerItemHaptics|AVPlayerItemVideoEnhancement|AVPlayerInterstitialSupport|AVPlayerItemIntegratedTimelineSupport|AVIntegrityChecking|AVPlayerItemSpeedRamp|AVPlayerItemSpeedRampInternal|AVMetricEventStreamPublisherInternal|AVPlayerItemTrackInfoCaching|fixFaultyTFDT165791136)
- __OBJC_CLASS_PROTOCOLS_$_AVURLAsset(AVAssetCache|AVURLAssetCache_Private|AVAssetVariantInspection|AVURLAssetURLHandlingInternal|AVURLAssetURLHandling|AVURLAssetInstanceIdentiferMapping|AVURLAssetContentKeyEligibility|AVURLAssetContentKeyEligibilityInternal|AVURLAssetCustomURLHandling|NSItemProvider|AVAssetSerializableCreationOptionsSupport|AVNSURLSessionAsset)
- ___24-[AVPlayerItem audioMix]_block_invoke
- ___28-[AVPlayerItem loudnessInfo]_block_invoke
- ___28-[AVPlayerItem setAudioMix:]_block_invoke
- ___28-[AVPlayerItem setAudioMix:]_block_invoke_2
- ___32-[AVPlayerItem setLoudnessInfo:]_block_invoke
- ___33-[AVPlayerItem audioTapProcessor]_block_invoke
- ___39-[AVPlayerItem audioTimePitchAlgorithm]_block_invoke
- ___39-[AVPlayerItem resetAudioBufferedAhead]_block_invoke
- ___43-[AVPlayerItem setAudioTimePitchAlgorithm:]_block_invoke
- ___43-[AVPlayerItem suppressesAudioOnlyVariants]_block_invoke
- ___44-[AVPlayerItem isAudioSpatializationAllowed]_block_invoke
- ___46-[AVPlayerItem setAudioSpatializationAllowed:]_block_invoke
- ___47-[AVPlayerItem setSuppressesAudioOnlyVariants:]_block_invoke
- ___47-[AVPlayerItem setSuppressesAudioOnlyVariants:]_block_invoke_2
- ___49-[AVPlayerItem allowedAudioSpatializationFormats]_block_invoke
- ___53-[AVPlayerItem setAllowedAudioSpatializationFormats:]_block_invoke
- ___block_descriptor_57_e8_32o40r48r_e5_v8?0ls32l8r40l8r48l8
- _kFigPlaybackItemProperty_SuppressesAudioOnlyVariants
CStrings:
+ "Advertisement"
+ "QTContentTypeForLoudnessControlAlarm"
+ "QTContentTypeForLoudnessControlAudiobookPodcastOrRadioProgram"
+ "QTContentTypeForLoudnessControlDeviceCaptureOrUserGenerated"
+ "QTContentTypeForLoudnessControlLiveAudiovisualProduction"
+ "QTContentTypeForLoudnessControlMusic"
+ "QTContentTypeForLoudnessControlOnDemandAudiovisualProduction"
+ "QTContentTypeForLoudnessControlOtherSystemSound"
+ "QTContentTypeForLoudnessControlRingtone"
+ "QTContentTypeForLoudnessControlSynthesizedSpeech"
+ "QTContentTypeForLoudnessControlUserInterfaceFeedback"
+ "UseItemMeasurement"
+ "UseSequenceMeasurement"
+ "appliesLoudnessAdjustmentsAutomatically"
+ "com.apple.avfoundation.avurlasset.setupconnectioncompletion"
+ "udta/ctlc"
+ "udta/ludt"
+ "uiso/ctlc"
+ "uiso/ludt"
- "<<<< AVSampleBufferVideoRenderer >>>> %s: <%{public}@|%p> Waking a suspended Swift enqueue because a flush is now required"
```
