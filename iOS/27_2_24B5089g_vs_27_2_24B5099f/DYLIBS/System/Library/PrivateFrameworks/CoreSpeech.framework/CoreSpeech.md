## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0x146630
+3605.31.3.0.0
+  __TEXT.__text: 0x1478e8
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14eb4
+  __TEXT.__objc_methlist: 0x14fcc
   __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x3270
-  __TEXT.__cstring: 0x28db4
-  __TEXT.__oslogstring: 0x2022c
-  __TEXT.__unwind_info: 0x6260
+  __TEXT.__gcc_except_tab: 0x32e8
+  __TEXT.__cstring: 0x28ef4
+  __TEXT.__oslogstring: 0x2047d
+  __TEXT.__unwind_info: 0x62c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4230
+  __DATA_CONST.__const: 0x4300
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xae18
+  __DATA_CONST.__objc_selrefs: 0xaee8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x1b38
+  __DATA_CONST.__got: 0x1b48
   __AUTH_CONST.__const: 0x1e20
-  __AUTH_CONST.__cfstring: 0x9620
-  __AUTH_CONST.__objc_const: 0x21380
+  __AUTH_CONST.__cfstring: 0x9640
+  __AUTH_CONST.__objc_const: 0x214f8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x9a8

   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0xda0
   __AUTH.__objc_data: 0x3c50
-  __DATA.__objc_ivar: 0x199c
+  __DATA.__objc_ivar: 0x19bc
   __DATA.__data: 0x3a14
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1770

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8147
-  Symbols:   14188
-  CStrings:  5597
+  Functions: 8182
+  Symbols:   14234
+  CStrings:  5612
 
Symbols:
+ -[CSEndpointDelayReporter analytics]
+ -[CSEndpointDelayReporter selfLoggingStream]
+ -[CSEndpointDelayReporter setAnalytics:]
+ -[CSEndpointDelayReporter setSelfLoggingStream:]
+ -[CSSiriAudioActivationInfo myriadElectionIdentity]
+ -[CSSiriSpeechRecorder _playStopAlertWithError:]
+ -[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]
+ -[CSSiriSpeechRecorder electionLedger]
+ -[CSSiriSpeechRecorder setElectionLedger:]
+ -[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]
+ -[CSSpeechController _invalidateRecordSessionActivationState]
+ -[CSSpeechController _noteAudioSessionActivatedForRecord:]
+ -[CSSpeechController _notifyDelegateDidStartRecordingSuccessfully:error:]
+ -[CSSpeechController didActivateAudioSessionForRecord]
+ -[CSSpeechController prefetchedAudioDeviceInfo]
+ -[CSSpeechController setDidActivateAudioSessionForRecord:]
+ -[CSSpeechController setPrefetchedAudioDeviceInfo:]
+ -[CSVoiceTriggerSecondPass requestExclaveAudio]
+ -[CSVoiceTriggerSecondPass setRequestExclaveAudio:]
+ -[CSXPCClient _sendMessageAndReplySync:reply:error:]
+ -[CSXPCClient activateAudioSessionWithReason:dynamicAttribute:bundleID:audioDeviceInfo:error:]
+ GCC_except_table1274
+ GCC_except_table1286
+ GCC_except_table1492
+ GCC_except_table1564
+ GCC_except_table1607
+ GCC_except_table1621
+ GCC_except_table1649
+ GCC_except_table1665
+ GCC_except_table1668
+ GCC_except_table1698
+ GCC_except_table178
+ GCC_except_table1798
+ GCC_except_table1800
+ GCC_except_table1806
+ GCC_except_table1866
+ GCC_except_table1892
+ GCC_except_table1898
+ GCC_except_table1979
+ GCC_except_table1999
+ GCC_except_table202
+ GCC_except_table2115
+ GCC_except_table2264
+ GCC_except_table2294
+ GCC_except_table2297
+ GCC_except_table2300
+ GCC_except_table2305
+ GCC_except_table2317
+ GCC_except_table2322
+ GCC_except_table2325
+ GCC_except_table2417
+ GCC_except_table2423
+ GCC_except_table246
+ GCC_except_table2463
+ GCC_except_table2470
+ GCC_except_table2488
+ GCC_except_table2521
+ GCC_except_table254
+ GCC_except_table2624
+ GCC_except_table267
+ GCC_except_table2683
+ GCC_except_table2695
+ GCC_except_table270
+ GCC_except_table2726
+ GCC_except_table2751
+ GCC_except_table2762
+ GCC_except_table2797
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table2804
+ GCC_except_table2814
+ GCC_except_table2815
+ GCC_except_table2824
+ GCC_except_table2830
+ GCC_except_table2832
+ GCC_except_table2833
+ GCC_except_table2903
+ GCC_except_table3173
+ GCC_except_table3252
+ GCC_except_table3305
+ GCC_except_table3327
+ GCC_except_table3330
+ GCC_except_table3333
+ GCC_except_table3364
+ GCC_except_table3424
+ GCC_except_table3597
+ GCC_except_table3623
+ GCC_except_table3651
+ GCC_except_table3686
+ GCC_except_table3687
+ GCC_except_table3689
+ GCC_except_table3691
+ GCC_except_table3709
+ GCC_except_table3711
+ GCC_except_table3713
+ GCC_except_table3717
+ GCC_except_table3719
+ GCC_except_table3722
+ GCC_except_table3733
+ GCC_except_table3743
+ GCC_except_table3751
+ GCC_except_table3754
+ GCC_except_table3755
+ GCC_except_table3756
+ GCC_except_table3759
+ GCC_except_table376
+ GCC_except_table3760
+ GCC_except_table3762
+ GCC_except_table3763
+ GCC_except_table3765
+ GCC_except_table3777
+ GCC_except_table3782
+ GCC_except_table3783
+ GCC_except_table3784
+ GCC_except_table3785
+ GCC_except_table3926
+ GCC_except_table3950
+ GCC_except_table4032
+ GCC_except_table4053
+ GCC_except_table4145
+ GCC_except_table4397
+ GCC_except_table4468
+ GCC_except_table4469
+ GCC_except_table4473
+ GCC_except_table4476
+ GCC_except_table4480
+ GCC_except_table449
+ GCC_except_table4505
+ GCC_except_table4508
+ GCC_except_table4561
+ GCC_except_table4567
+ GCC_except_table4637
+ GCC_except_table4842
+ GCC_except_table4849
+ GCC_except_table4856
+ GCC_except_table4862
+ GCC_except_table4945
+ GCC_except_table5105
+ GCC_except_table5115
+ GCC_except_table5139
+ GCC_except_table5159
+ GCC_except_table5242
+ GCC_except_table5256
+ GCC_except_table5265
+ GCC_except_table5272
+ GCC_except_table5278
+ GCC_except_table5283
+ GCC_except_table5291
+ GCC_except_table5297
+ GCC_except_table5310
+ GCC_except_table5316
+ GCC_except_table5334
+ GCC_except_table5335
+ GCC_except_table5336
+ GCC_except_table5337
+ GCC_except_table5339
+ GCC_except_table5340
+ GCC_except_table5341
+ GCC_except_table5342
+ GCC_except_table5343
+ GCC_except_table5345
+ GCC_except_table5346
+ GCC_except_table5349
+ GCC_except_table5364
+ GCC_except_table5395
+ GCC_except_table5452
+ GCC_except_table5456
+ GCC_except_table547
+ GCC_except_table5510
+ GCC_except_table5540
+ GCC_except_table5543
+ GCC_except_table5633
+ GCC_except_table5647
+ GCC_except_table5654
+ GCC_except_table5666
+ GCC_except_table5670
+ GCC_except_table5680
+ GCC_except_table572
+ GCC_except_table578
+ GCC_except_table579
+ GCC_except_table583
+ GCC_except_table5909
+ GCC_except_table5942
+ GCC_except_table5947
+ GCC_except_table5984
+ GCC_except_table5993
+ GCC_except_table6023
+ GCC_except_table604
+ GCC_except_table605
+ GCC_except_table6097
+ GCC_except_table611
+ GCC_except_table6239
+ GCC_except_table6344
+ GCC_except_table6352
+ GCC_except_table637
+ GCC_except_table6372
+ GCC_except_table6377
+ GCC_except_table6483
+ GCC_except_table6538
+ GCC_except_table6618
+ GCC_except_table6640
+ GCC_except_table6641
+ GCC_except_table6651
+ GCC_except_table6652
+ GCC_except_table6664
+ GCC_except_table6706
+ GCC_except_table6711
+ GCC_except_table6716
+ GCC_except_table6744
+ GCC_except_table6816
+ GCC_except_table6828
+ GCC_except_table6851
+ GCC_except_table6862
+ GCC_except_table6865
+ GCC_except_table6888
+ GCC_except_table690
+ GCC_except_table6900
+ GCC_except_table6947
+ GCC_except_table710
+ GCC_except_table7197
+ GCC_except_table7233
+ GCC_except_table7306
+ GCC_except_table7360
+ GCC_except_table7383
+ GCC_except_table7419
+ GCC_except_table7438
+ GCC_except_table7449
+ GCC_except_table7593
+ GCC_except_table7601
+ GCC_except_table768
+ GCC_except_table7717
+ GCC_except_table7718
+ GCC_except_table7719
+ GCC_except_table772
+ GCC_except_table7720
+ GCC_except_table7721
+ GCC_except_table7726
+ GCC_except_table777
+ GCC_except_table7789
+ GCC_except_table7835
+ GCC_except_table7843
+ GCC_except_table7849
+ GCC_except_table7874
+ GCC_except_table7880
+ GCC_except_table7886
+ GCC_except_table8024
+ GCC_except_table943
+ GCC_except_table955
+ GCC_except_table958
+ _OBJC_CLASS_$_CSFModelConfigDecoder
+ _OBJC_CLASS_$_SCDAElectionLedger
+ _OBJC_IVAR_$_CSEndpointDelayReporter._analytics
+ _OBJC_IVAR_$_CSEndpointDelayReporter._selfLoggingStream
+ _OBJC_IVAR_$_CSSiriAudioActivationInfo._myriadElectionIdentity
+ _OBJC_IVAR_$_CSSiriSpeechRecorder._electionLedgerOverride
+ _OBJC_IVAR_$_CSSiriSpeechRecordingContext._electionIdentity
+ _OBJC_IVAR_$_CSSpeechController._didActivateAudioSessionForRecord
+ _OBJC_IVAR_$_CSSpeechController._prefetchedAudioDeviceInfo
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPass._requestExclaveAudio
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionProviding
+ ___41-[CSSpeechController releaseAudioSession]_block_invoke_2
+ ___42-[CSSpeechController releaseAudioSession:]_block_invoke_2
+ ___52-[CSXPCClient _sendMessageAndReplySync:reply:error:]_block_invoke
+ ___58-[CSSpeechController _noteAudioSessionActivatedForRecord:]_block_invoke
+ ___70-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke
+ ___70-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke_2
+ ___79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke
+ ___79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke_2
+ ___79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e32_v20?0B8"SCDAElectionOutcome"12ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_49_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_59_e8_32s40r_e20_v20?0B8"NSError"12ls32l8r40l8
+ ___block_descriptor_68_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- GCC_except_table1272
- GCC_except_table1284
- GCC_except_table1490
- GCC_except_table1562
- GCC_except_table1617
- GCC_except_table1641
- GCC_except_table1661
- GCC_except_table1664
- GCC_except_table1694
- GCC_except_table176
- GCC_except_table1792
- GCC_except_table1794
- GCC_except_table1802
- GCC_except_table1862
- GCC_except_table1888
- GCC_except_table1894
- GCC_except_table1975
- GCC_except_table1995
- GCC_except_table200
- GCC_except_table2111
- GCC_except_table2260
- GCC_except_table2290
- GCC_except_table2293
- GCC_except_table2296
- GCC_except_table2301
- GCC_except_table2313
- GCC_except_table2318
- GCC_except_table2321
- GCC_except_table2413
- GCC_except_table2419
- GCC_except_table244
- GCC_except_table2459
- GCC_except_table2462
- GCC_except_table2484
- GCC_except_table2517
- GCC_except_table252
- GCC_except_table2620
- GCC_except_table265
- GCC_except_table2679
- GCC_except_table268
- GCC_except_table2691
- GCC_except_table2722
- GCC_except_table2747
- GCC_except_table2758
- GCC_except_table2792
- GCC_except_table2793
- GCC_except_table2794
- GCC_except_table2795
- GCC_except_table2803
- GCC_except_table2806
- GCC_except_table2820
- GCC_except_table2826
- GCC_except_table2828
- GCC_except_table2829
- GCC_except_table2899
- GCC_except_table3165
- GCC_except_table3243
- GCC_except_table3280
- GCC_except_table3313
- GCC_except_table3316
- GCC_except_table3319
- GCC_except_table3350
- GCC_except_table3410
- GCC_except_table3583
- GCC_except_table3609
- GCC_except_table3637
- GCC_except_table3671
- GCC_except_table3672
- GCC_except_table3674
- GCC_except_table3676
- GCC_except_table3692
- GCC_except_table3694
- GCC_except_table3696
- GCC_except_table3698
- GCC_except_table3700
- GCC_except_table3702
- GCC_except_table3704
- GCC_except_table3718
- GCC_except_table3724
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3732
- GCC_except_table3734
- GCC_except_table3735
- GCC_except_table3736
- GCC_except_table3737
- GCC_except_table374
- GCC_except_table3740
- GCC_except_table3744
- GCC_except_table3746
- GCC_except_table3748
- GCC_except_table3753
- GCC_except_table3767
- GCC_except_table3910
- GCC_except_table3934
- GCC_except_table4000
- GCC_except_table4037
- GCC_except_table4129
- GCC_except_table4381
- GCC_except_table4452
- GCC_except_table4453
- GCC_except_table4457
- GCC_except_table4460
- GCC_except_table4464
- GCC_except_table447
- GCC_except_table4489
- GCC_except_table4492
- GCC_except_table4545
- GCC_except_table4551
- GCC_except_table4621
- GCC_except_table4825
- GCC_except_table4832
- GCC_except_table4839
- GCC_except_table4845
- GCC_except_table4928
- GCC_except_table5088
- GCC_except_table5098
- GCC_except_table5122
- GCC_except_table5142
- GCC_except_table5225
- GCC_except_table5239
- GCC_except_table5248
- GCC_except_table5255
- GCC_except_table5261
- GCC_except_table5263
- GCC_except_table5266
- GCC_except_table5274
- GCC_except_table5276
- GCC_except_table5282
- GCC_except_table5294
- GCC_except_table5306
- GCC_except_table5313
- GCC_except_table5315
- GCC_except_table5317
- GCC_except_table5318
- GCC_except_table5319
- GCC_except_table5320
- GCC_except_table5322
- GCC_except_table5324
- GCC_except_table5325
- GCC_except_table5326
- GCC_except_table5329
- GCC_except_table5378
- GCC_except_table5435
- GCC_except_table5439
- GCC_except_table545
- GCC_except_table5493
- GCC_except_table5523
- GCC_except_table5526
- GCC_except_table5616
- GCC_except_table5630
- GCC_except_table5637
- GCC_except_table5649
- GCC_except_table5653
- GCC_except_table5663
- GCC_except_table570
- GCC_except_table575
- GCC_except_table576
- GCC_except_table581
- GCC_except_table5892
- GCC_except_table5925
- GCC_except_table5930
- GCC_except_table5967
- GCC_except_table5976
- GCC_except_table6006
- GCC_except_table601
- GCC_except_table602
- GCC_except_table6076
- GCC_except_table609
- GCC_except_table6218
- GCC_except_table6323
- GCC_except_table6331
- GCC_except_table635
- GCC_except_table6351
- GCC_except_table6356
- GCC_except_table6462
- GCC_except_table6517
- GCC_except_table6597
- GCC_except_table6619
- GCC_except_table6620
- GCC_except_table6630
- GCC_except_table6631
- GCC_except_table6643
- GCC_except_table6674
- GCC_except_table6685
- GCC_except_table6690
- GCC_except_table6723
- GCC_except_table6795
- GCC_except_table6807
- GCC_except_table6830
- GCC_except_table6841
- GCC_except_table6844
- GCC_except_table6867
- GCC_except_table6879
- GCC_except_table688
- GCC_except_table6926
- GCC_except_table708
- GCC_except_table7176
- GCC_except_table7212
- GCC_except_table7285
- GCC_except_table7339
- GCC_except_table7362
- GCC_except_table7403
- GCC_except_table7414
- GCC_except_table7558
- GCC_except_table7566
- GCC_except_table764
- GCC_except_table7682
- GCC_except_table7683
- GCC_except_table7684
- GCC_except_table7685
- GCC_except_table7686
- GCC_except_table7691
- GCC_except_table770
- GCC_except_table775
- GCC_except_table7754
- GCC_except_table7800
- GCC_except_table7808
- GCC_except_table7814
- GCC_except_table7839
- GCC_except_table7845
- GCC_except_table7851
- GCC_except_table7989
- GCC_except_table941
- GCC_except_table953
- GCC_except_table956
- ___45-[CSXPCClient sendMessageAndReplySync:error:]_block_invoke
- ___58-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]_block_invoke
- ___block_descriptor_58_e8_32s40r_e20_v20?0B8"NSError"12ls32l8r40l8
- ___block_descriptor_67_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
CStrings:
+ "%s Audio session activated for record, audioDeviceInfo = %{public}@"
+ "%s Audio session was already activated for record, skipping activation in startRecording"
+ "%s Audio stream failed to start after reporting didStartRecording early, will report didStop : %{public}@"
+ "%s Audio stream started, didStartRecording was already reported early"
+ "%s BTLE Myriad loss; not playing speech stop alert"
+ "%s BTLE recorder is gone; not playing speech stop alert"
+ "%s BTLE request was cancelled; not playing speech stop alert"
+ "%s BTLE speech controller began waiting for Myriad decision (identity %@)"
+ "%s Invalidating cached record session activation state"
+ "%s Reporting didStartRecording early, ahead of the audio stream start"
+ "%s isSiriMode=%d, speechEvent=%ld, wasRequestCancelled=%d, shouldSuppressAlert=%d, recordRoute=%@"
+ "%s stop alert: didWin=%d, withError=%d, recordRoute=%@"
+ "-[CSSiriSpeechRecorder _playStopAlertWithError:]"
+ "-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke"
+ "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke"
+ "-[CSSpeechController _invalidateRecordSessionActivationState]"
+ "-[CSSpeechController _noteAudioSessionActivatedForRecord:]_block_invoke"
+ "-[CSSpeechController _notifyDelegateDidStartRecordingSuccessfully:error:]"
+ "Recording stop alert"
+ "requestAudioDeviceInfo"
+ "v20@?0B8@\"SCDAElectionOutcome\"12"
+ "\xa5"
+ "\xf03"
- "%s BTLE Myriad Not explicitly playing speech stop alert"
- "%s BTLE speech controller began waiting for Myriad decision"
- "%s isSiriMode=%d, speechEvent=%ld, wasRequestCancelled=%d, shouldSuppressAlert=%d, isMonitoringMyriadEvents=%d, didMyriadWin=%d, recordRoute=%@"
- "-[CSEndpointAnalyzerBase getHybridEndpointerConfigForAsset:]"
- "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]"
- "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]_block_invoke"
- "\xa3"
- "\xf0#"
```
