## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3605.32.1.0.0
-  __TEXT.__text: 0x148048
-  __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14ffc
+3610.11.1.0.0
+  __TEXT.__text: 0x148954
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_methlist: 0x150ec
   __TEXT.__const: 0x45c
-  __TEXT.__dlopen_cstrs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x32e8
-  __TEXT.__cstring: 0x28f4c
-  __TEXT.__oslogstring: 0x2063d
-  __TEXT.__unwind_info: 0x62e0
+  __TEXT.__dlopen_cstrs: 0x197
+  __TEXT.__gcc_except_tab: 0x32f0
+  __TEXT.__cstring: 0x28faa
+  __TEXT.__oslogstring: 0x20a17
+  __TEXT.__unwind_info: 0x6310
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4330
+  __DATA_CONST.__const: 0x4348
   __DATA_CONST.__objc_classlist: 0x868
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x4e0
+  __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xaef8
+  __DATA_CONST.__objc_selrefs: 0xaf80
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x1b58
-  __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x9640
-  __AUTH_CONST.__objc_const: 0x21588
+  __DATA_CONST.__got: 0x1b60
+  __AUTH_CONST.__const: 0x1ea0
+  __AUTH_CONST.__cfstring: 0x9680
+  __AUTH_CONST.__objc_const: 0x21630
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__lazy_load_got: 0x8
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_floatobj: 0x4f0
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x3ca0
-  __DATA.__objc_ivar: 0x19bc
-  __DATA.__data: 0x3a14
+  __DATA.__objc_ivar: 0x19c8
+  __DATA.__data: 0x3a74
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8190
-  Symbols:   14246
-  CStrings:  5618
+  Functions: 8206
+  Symbols:   14275
+  CStrings:  5626
 
Symbols:
+ +[CSMyriadPHash getTriggerAudioForVoiceTriggerInfo:withHostTime:writeFile:]
+ +[CSSiriAudioActivationInfo _isLinwoodEnabledAndAvailable]
+ +[CSSpeechController continuousVoiceTriggerActivationUserInfo:]
+ -[CSAsset(SpeakerRecognition) _firstNumberForKey:inSectionKeys:]
+ -[CSAsset(SpeakerRecognition) _numberForKey:inSection:]
+ -[CSAsset(SpeakerRecognition) inRequestSegmentSpkrIdScoreThresholdForSelfPlatform:servingPlatform:recordRoute:]
+ -[CSAttSiriAttentionAssetsStatusProvider _fetchCurrentAssetStatus]
+ -[CSAttSiriAttentionAssetsStatusProvider assetHandler]
+ -[CSAttSiriAttentionAssetsStatusProvider initWithDelegate:]
+ -[CSAttSiriAttentionAssetsStatusProvider initWithMitigationAssetHandler:delegate:]
+ -[CSAttSiriAttentionAssetsStatusProvider setAssetHandler:]
+ -[CSBuiltInVoiceTrigger _isLinwoodEnabledAndAvailable]
+ -[CSBuiltInVoiceTrigger _shouldRequestExclaveAudioWithProvider:]
+ -[CSBuiltInVoiceTrigger isListeningWithActiveCallContext]
+ -[CSBuiltInVoiceTrigger linwoodEnabledAndAvailableMonitor:didReceiveEnabledAndAvailable:]
+ -[CSBuiltInVoiceTrigger setIsListeningWithActiveCallContext:]
+ -[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]
+ -[CSDeviceSelectionNotifier _shouldDonateTriggerAudioSlice]
+ -[CSSiriAudioActivationInfo _canPrewarmForCrownHold]
+ -[CSSiriSpeechRecorder setServerAudioSentByClient:]
+ -[CSVoiceTriggerSecondPass _isLinwoodEnabledAndAvailable]
+ -[CSVoiceTriggerSecondPass _secondPassChannelForFirstPassChannel:channelSelectionScores:isLinwoodEnabledAndAvailable:]
+ GCC_except_table1281
+ GCC_except_table1293
+ GCC_except_table1499
+ GCC_except_table1571
+ GCC_except_table1614
+ GCC_except_table1628
+ GCC_except_table1652
+ GCC_except_table1656
+ GCC_except_table1672
+ GCC_except_table1675
+ GCC_except_table1705
+ GCC_except_table1803
+ GCC_except_table1805
+ GCC_except_table1807
+ GCC_except_table1813
+ GCC_except_table1873
+ GCC_except_table1899
+ GCC_except_table1905
+ GCC_except_table1986
+ GCC_except_table2006
+ GCC_except_table2122
+ GCC_except_table2271
+ GCC_except_table2301
+ GCC_except_table2304
+ GCC_except_table2307
+ GCC_except_table2312
+ GCC_except_table2324
+ GCC_except_table2329
+ GCC_except_table2332
+ GCC_except_table2424
+ GCC_except_table2430
+ GCC_except_table2473
+ GCC_except_table2477
+ GCC_except_table2495
+ GCC_except_table2528
+ GCC_except_table2639
+ GCC_except_table269
+ GCC_except_table2698
+ GCC_except_table2710
+ GCC_except_table272
+ GCC_except_table2741
+ GCC_except_table2766
+ GCC_except_table2777
+ GCC_except_table2811
+ GCC_except_table2813
+ GCC_except_table2814
+ GCC_except_table2825
+ GCC_except_table2826
+ GCC_except_table2829
+ GCC_except_table2830
+ GCC_except_table2839
+ GCC_except_table2845
+ GCC_except_table2847
+ GCC_except_table2848
+ GCC_except_table2918
+ GCC_except_table3188
+ GCC_except_table3267
+ GCC_except_table3306
+ GCC_except_table3320
+ GCC_except_table333
+ GCC_except_table3342
+ GCC_except_table3345
+ GCC_except_table3348
+ GCC_except_table3381
+ GCC_except_table3441
+ GCC_except_table3615
+ GCC_except_table3641
+ GCC_except_table3669
+ GCC_except_table3704
+ GCC_except_table3705
+ GCC_except_table3707
+ GCC_except_table3709
+ GCC_except_table3729
+ GCC_except_table3731
+ GCC_except_table3733
+ GCC_except_table3735
+ GCC_except_table3737
+ GCC_except_table3740
+ GCC_except_table3748
+ GCC_except_table3761
+ GCC_except_table3765
+ GCC_except_table3772
+ GCC_except_table3778
+ GCC_except_table3779
+ GCC_except_table3780
+ GCC_except_table3781
+ GCC_except_table3783
+ GCC_except_table3784
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3795
+ GCC_except_table3800
+ GCC_except_table3801
+ GCC_except_table3802
+ GCC_except_table3803
+ GCC_except_table383
+ GCC_except_table3944
+ GCC_except_table3968
+ GCC_except_table4034
+ GCC_except_table4050
+ GCC_except_table4071
+ GCC_except_table4163
+ GCC_except_table4415
+ GCC_except_table4486
+ GCC_except_table4487
+ GCC_except_table4491
+ GCC_except_table4494
+ GCC_except_table4498
+ GCC_except_table4523
+ GCC_except_table4526
+ GCC_except_table456
+ GCC_except_table4579
+ GCC_except_table4585
+ GCC_except_table4859
+ GCC_except_table4866
+ GCC_except_table4873
+ GCC_except_table4879
+ GCC_except_table4962
+ GCC_except_table5125
+ GCC_except_table5135
+ GCC_except_table5159
+ GCC_except_table5179
+ GCC_except_table5262
+ GCC_except_table5276
+ GCC_except_table5285
+ GCC_except_table5292
+ GCC_except_table5298
+ GCC_except_table5300
+ GCC_except_table5303
+ GCC_except_table5311
+ GCC_except_table5313
+ GCC_except_table5317
+ GCC_except_table5330
+ GCC_except_table5352
+ GCC_except_table5356
+ GCC_except_table5359
+ GCC_except_table5360
+ GCC_except_table5361
+ GCC_except_table5362
+ GCC_except_table5363
+ GCC_except_table5365
+ GCC_except_table5366
+ GCC_except_table5367
+ GCC_except_table5369
+ GCC_except_table5384
+ GCC_except_table5415
+ GCC_except_table5472
+ GCC_except_table5476
+ GCC_except_table5530
+ GCC_except_table554
+ GCC_except_table5560
+ GCC_except_table5563
+ GCC_except_table5653
+ GCC_except_table5667
+ GCC_except_table5686
+ GCC_except_table5690
+ GCC_except_table5700
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table590
+ GCC_except_table5931
+ GCC_except_table5964
+ GCC_except_table5969
+ GCC_except_table6007
+ GCC_except_table6016
+ GCC_except_table6046
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table6120
+ GCC_except_table618
+ GCC_except_table6262
+ GCC_except_table6367
+ GCC_except_table6375
+ GCC_except_table6395
+ GCC_except_table6400
+ GCC_except_table644
+ GCC_except_table6506
+ GCC_except_table6561
+ GCC_except_table6641
+ GCC_except_table6663
+ GCC_except_table6664
+ GCC_except_table6674
+ GCC_except_table6675
+ GCC_except_table6687
+ GCC_except_table6718
+ GCC_except_table6729
+ GCC_except_table6734
+ GCC_except_table6739
+ GCC_except_table6767
+ GCC_except_table6839
+ GCC_except_table6851
+ GCC_except_table6874
+ GCC_except_table6885
+ GCC_except_table6888
+ GCC_except_table6911
+ GCC_except_table6923
+ GCC_except_table697
+ GCC_except_table6970
+ GCC_except_table717
+ GCC_except_table7220
+ GCC_except_table7256
+ GCC_except_table7329
+ GCC_except_table7383
+ GCC_except_table7406
+ GCC_except_table7442
+ GCC_except_table7461
+ GCC_except_table7472
+ GCC_except_table7617
+ GCC_except_table7625
+ GCC_except_table773
+ GCC_except_table7741
+ GCC_except_table7742
+ GCC_except_table7743
+ GCC_except_table7744
+ GCC_except_table7745
+ GCC_except_table775
+ GCC_except_table7750
+ GCC_except_table779
+ GCC_except_table7813
+ GCC_except_table784
+ GCC_except_table7859
+ GCC_except_table7867
+ GCC_except_table7873
+ GCC_except_table7898
+ GCC_except_table7904
+ GCC_except_table7910
+ GCC_except_table8048
+ GCC_except_table950
+ GCC_except_table962
+ GCC_except_table965
+ _AFIsLinwoodEnabledAndAvailable
+ _OBJC_CLASS_$_CSCompanionRuntimeThresholdKeys
+ _OBJC_CLASS_$_CSLinwoodEnabledAndAvailableMonitor
+ _OBJC_CLASS_$_DeviceSelectionTriggerAudio
+ _OBJC_CLASS_$_DeviceSelectionTriggerAudio$lazyGOT
+ _OBJC_CLASS_$_DeviceSelectionTriggerAudio$lazyGOT$loadHelper_x8
+ _OBJC_IVAR_$_CSAttSiriAttentionAssetsStatusProvider._assetHandler
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._isListeningWithActiveCallContext
+ _OBJC_IVAR_$_CSSiriSpeechRecorder._serverAudioSentByClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLinwoodEnabledAndAvailableMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLinwoodEnabledAndAvailableMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSLinwoodEnabledAndAvailableMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSLinwoodEnabledAndAvailableMonitorDelegate
+ __OBJC_PROTOCOL_$_CSLinwoodEnabledAndAvailableMonitorDelegate
+ ___63+[CSSpeechController continuousVoiceTriggerActivationUserInfo:]_block_invoke
+ ___66-[CSAttSiriAttentionAssetsStatusProvider _fetchCurrentAssetStatus]_block_invoke
+ ___70-[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]_block_invoke
+ ___89-[CSBuiltInVoiceTrigger linwoodEnabledAndAvailableMonitor:didReceiveEnabledAndAvailable:]_block_invoke
+ ___block_descriptor_48_e8_32s_e31_v16?0"<SCDAContextMutating>"8ls32l8
- +[CSMyriadPHash _generateFingerPrintFromVoiceTriggerInfo:audioHostTime:usingGenerator:]
- +[CSMyriadPHash generateFingerprintForVoiceTriggerInfo:forTime:]
- -[CSBuiltInVoiceTrigger _stopListening]
- -[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]
- GCC_except_table1274
- GCC_except_table1286
- GCC_except_table1492
- GCC_except_table1564
- GCC_except_table1607
- GCC_except_table1621
- GCC_except_table1645
- GCC_except_table1649
- GCC_except_table1665
- GCC_except_table1668
- GCC_except_table1698
- GCC_except_table1796
- GCC_except_table1798
- GCC_except_table1800
- GCC_except_table1806
- GCC_except_table1866
- GCC_except_table1892
- GCC_except_table1898
- GCC_except_table1979
- GCC_except_table1999
- GCC_except_table2115
- GCC_except_table2264
- GCC_except_table2294
- GCC_except_table2297
- GCC_except_table2300
- GCC_except_table2305
- GCC_except_table2317
- GCC_except_table2322
- GCC_except_table2325
- GCC_except_table2417
- GCC_except_table2423
- GCC_except_table2463
- GCC_except_table2466
- GCC_except_table2488
- GCC_except_table2521
- GCC_except_table2632
- GCC_except_table267
- GCC_except_table2691
- GCC_except_table270
- GCC_except_table2703
- GCC_except_table2734
- GCC_except_table2759
- GCC_except_table2770
- GCC_except_table2804
- GCC_except_table2805
- GCC_except_table2806
- GCC_except_table2807
- GCC_except_table2808
- GCC_except_table2818
- GCC_except_table2823
- GCC_except_table2832
- GCC_except_table2838
- GCC_except_table2840
- GCC_except_table2841
- GCC_except_table2911
- GCC_except_table3181
- GCC_except_table3260
- GCC_except_table3299
- GCC_except_table3313
- GCC_except_table3335
- GCC_except_table3338
- GCC_except_table3341
- GCC_except_table3372
- GCC_except_table3432
- GCC_except_table3605
- GCC_except_table3631
- GCC_except_table3659
- GCC_except_table3694
- GCC_except_table3695
- GCC_except_table3697
- GCC_except_table3699
- GCC_except_table3715
- GCC_except_table3717
- GCC_except_table3719
- GCC_except_table3721
- GCC_except_table3723
- GCC_except_table3730
- GCC_except_table3738
- GCC_except_table3741
- GCC_except_table3747
- GCC_except_table3749
- GCC_except_table3753
- GCC_except_table3755
- GCC_except_table3758
- GCC_except_table376
- GCC_except_table3760
- GCC_except_table3762
- GCC_except_table3764
- GCC_except_table3771
- GCC_except_table3776
- GCC_except_table3785
- GCC_except_table3790
- GCC_except_table3791
- GCC_except_table3792
- GCC_except_table3793
- GCC_except_table3934
- GCC_except_table3958
- GCC_except_table4024
- GCC_except_table4040
- GCC_except_table4061
- GCC_except_table4153
- GCC_except_table4405
- GCC_except_table4476
- GCC_except_table4477
- GCC_except_table4481
- GCC_except_table4484
- GCC_except_table4488
- GCC_except_table449
- GCC_except_table4513
- GCC_except_table4516
- GCC_except_table4569
- GCC_except_table4575
- GCC_except_table4645
- GCC_except_table4850
- GCC_except_table4857
- GCC_except_table4864
- GCC_except_table4870
- GCC_except_table4953
- GCC_except_table5113
- GCC_except_table5123
- GCC_except_table5147
- GCC_except_table5167
- GCC_except_table5250
- GCC_except_table5264
- GCC_except_table5273
- GCC_except_table5280
- GCC_except_table5286
- GCC_except_table5288
- GCC_except_table5291
- GCC_except_table5299
- GCC_except_table5301
- GCC_except_table5305
- GCC_except_table5307
- GCC_except_table5318
- GCC_except_table5324
- GCC_except_table5338
- GCC_except_table5340
- GCC_except_table5342
- GCC_except_table5344
- GCC_except_table5345
- GCC_except_table5347
- GCC_except_table5349
- GCC_except_table5351
- GCC_except_table5353
- GCC_except_table5372
- GCC_except_table5403
- GCC_except_table5460
- GCC_except_table5464
- GCC_except_table547
- GCC_except_table5518
- GCC_except_table5548
- GCC_except_table5551
- GCC_except_table5641
- GCC_except_table5655
- GCC_except_table5662
- GCC_except_table5678
- GCC_except_table5688
- GCC_except_table572
- GCC_except_table577
- GCC_except_table578
- GCC_except_table583
- GCC_except_table5917
- GCC_except_table5950
- GCC_except_table5955
- GCC_except_table5992
- GCC_except_table6001
- GCC_except_table603
- GCC_except_table6031
- GCC_except_table604
- GCC_except_table605
- GCC_except_table6105
- GCC_except_table6247
- GCC_except_table6352
- GCC_except_table6360
- GCC_except_table637
- GCC_except_table6380
- GCC_except_table6385
- GCC_except_table6491
- GCC_except_table6546
- GCC_except_table6626
- GCC_except_table6648
- GCC_except_table6649
- GCC_except_table6659
- GCC_except_table6660
- GCC_except_table6672
- GCC_except_table6703
- GCC_except_table6714
- GCC_except_table6719
- GCC_except_table6724
- GCC_except_table6752
- GCC_except_table6824
- GCC_except_table6836
- GCC_except_table6859
- GCC_except_table6870
- GCC_except_table6873
- GCC_except_table6896
- GCC_except_table690
- GCC_except_table6908
- GCC_except_table6955
- GCC_except_table710
- GCC_except_table7205
- GCC_except_table7241
- GCC_except_table7314
- GCC_except_table7368
- GCC_except_table7391
- GCC_except_table7427
- GCC_except_table7446
- GCC_except_table7457
- GCC_except_table7601
- GCC_except_table7609
- GCC_except_table766
- GCC_except_table768
- GCC_except_table772
- GCC_except_table7725
- GCC_except_table7726
- GCC_except_table7727
- GCC_except_table7728
- GCC_except_table7729
- GCC_except_table7734
- GCC_except_table777
- GCC_except_table7797
- GCC_except_table7843
- GCC_except_table7851
- GCC_except_table7857
- GCC_except_table7882
- GCC_except_table7888
- GCC_except_table7894
- GCC_except_table8032
- GCC_except_table943
- GCC_except_table955
- GCC_except_table958
- _ShazamKitLibraryCore.frameworkLibrary
- ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke
- ___67-[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]_block_invoke
- ___73-[CSAttSiriAttentionAssetsStatusProvider initWithMitigationAssetHandler:]_block_invoke
- ___ShazamKitLibraryCore_block_invoke
- ___getSHSignatureGeneratorClass_block_invoke
- _getSHSignatureGeneratorClass.softClass
- _kVTEIInputLatency
CStrings:
+ "%@/%@%-@ch%d-mct%llu.pcm.wav"
+ "%s #deviceSelection AToA Failed to get trigger audio buffer"
+ "%s #deviceSelection AToA exclave trigger; no slice is donated on this build"
+ "%s #deviceSelection AToA trigger audio chunk is empty; no slice to donate"
+ "%s #deviceSelection AToA trigger audio has no buffer timestamp; it cannot be ordered"
+ "%s #deviceSelection AToA trigger audio slice has no samples; nothing donated"
+ "%s #deviceSelection Error - no audio chunk for trigger audio slice, channel: %@"
+ "%s #deviceSelection Trigger audio buffer too short for %lu samples; slice will start at 0"
+ "%s #deviceSelection Trigger audio slice: %lu samples, format: %@, channel: %@"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:First pass selected channel %{public}tu, using channel %{public}tu for second pass"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:No first pass score for allowed channels 0x%{public}llx, using first pass channel %{public}tu"
+ "%s Device Selection Feature or AToA (Audio Time of Arrival) disabled, returning"
+ "%s Donated trigger audio slice (%@, at: %llu) successfully"
+ "%s Failed to donate trigger audio slice: %@"
+ "%s Failed to save trigger audio slice to file %{public}@"
+ "%s Linwood enabled and available changed to %{public}@, first pass channels 0x%{public}llx -> 0x%{public}llx. Apply the current voice trigger asset again."
+ "%s Linwood enabled and available changed to %{public}@, first pass channels 0x%{public}llx do not change"
+ "%s Trigger Audio length %lu, format: %@"
+ "%s Using %{public}@=%{public}@ from section %{public}@"
+ "%s Wrote trigger audio slice as a PCM WAV file: %@"
+ "+[CSMyriadPHash getTriggerAudioForVoiceTriggerInfo:withHostTime:writeFile:]"
+ "-[CSAsset(SpeakerRecognition) _firstNumberForKey:inSectionKeys:]"
+ "-[CSAttSiriAttentionAssetsStatusProvider initWithMitigationAssetHandler:delegate:]"
+ "-[CSBuiltInVoiceTrigger linwoodEnabledAndAvailableMonitor:didReceiveEnabledAndAvailable:]_block_invoke"
+ "-[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]"
+ "-[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]_block_invoke"
+ "-[CSVoiceTriggerSecondPass _secondPassChannelForFirstPassChannel:channelSelectionScores:isLinwoodEnabledAndAvailable:]"
+ "2"
+ "CSSpeechRecordSettingsKey_serverAudioSentByClient"
+ "TriggerAudioSlice-"
+ "float32"
+ "int16"
- "%@/%@%@.pcm.wav"
- "%s #deviceSelection Error - no audio chunk for channel: %@"
- "%s #deviceSelection Error appending buffer to generator: %@"
- "%s #deviceSelection configured to grab maximum of %f seconds of audio"
- "%s #deviceSelection signature duration == 0.0, skipping"
- "%s Donated fingerprint (%@, at: %llu) successfully"
- "%s Failed to donate fingerprint: %@"
- "%s Failed to save shazam signature chunk to file %{public}@"
- "%s Fingerprint duration = %f Signature len = %d channel = %@"
- "%s Signature length %lu"
- "%s Wrote the fingerprint audio buffer as a PCM WAV file: %@"
- "+[CSMyriadPHash _generateFingerPrintFromVoiceTriggerInfo:audioHostTime:usingGenerator:]"
- "+[CSMyriadPHash generateFingerprintForVoiceTriggerInfo:forTime:]"
- "-[CSAttSiriAttentionAssetsStatusProvider initWithMitigationAssetHandler:]"
- "-[CSBuiltInVoiceTrigger _stopListening]"
- "-[CSBuiltInVoiceTrigger _stopListening]_block_invoke"
- "-[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]"
- "-[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]_block_invoke"
- "CSMyriadPHash_Test.h"
- "Class getSHSignatureGeneratorClass(void)_block_invoke"
- "SHSignatureGenerator"
- "ShazamPCM-"
- "softlink:r:path:/System/Library/Frameworks/ShazamKit.framework/ShazamKit"
- "void *ShazamKitLibrary(void)"
```
