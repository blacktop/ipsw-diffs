## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3510.3.1.0.0
-  __TEXT.__text: 0xc3450
+3515.5.1.0.0
+  __TEXT.__text: 0xc34e4
   __TEXT.__auth_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xc690
+  __TEXT.__objc_methlist: 0xc698
   __TEXT.__const: 0x808
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x1540e
+  __TEXT.__cstring: 0x15422
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__gcc_except_tab: 0x41ac
-  __TEXT.__oslogstring: 0xf8f4
-  __TEXT.__unwind_info: 0x3670
+  __TEXT.__oslogstring: 0xf8f2
+  __TEXT.__unwind_info: 0x3678
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_classname: 0x1c26
-  __TEXT.__objc_methname: 0x20d10
+  __TEXT.__objc_methname: 0x20d4a
   __TEXT.__objc_methtype: 0x44a6
-  __TEXT.__objc_stubs: 0x10f80
+  __TEXT.__objc_stubs: 0x10fa0
   __DATA_CONST.__got: 0xf90
   __DATA_CONST.__const: 0x26b0
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ba0
+  __DATA_CONST.__objc_selrefs: 0x6ba8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x198

   __AUTH.__objc_data: 0x1988
   __DATA.__objc_ivar: 0xcbc
   __DATA.__data: 0x1478
-  __DATA.__bss: 0x918
+  __DATA.__bss: 0x8a8
   __DATA_DIRTY.__objc_data: 0x2ba0
   __DATA_DIRTY.__data: 0x2d0
-  __DATA_DIRTY.__bss: 0x3d8
+  __DATA_DIRTY.__bss: 0x448
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AFF13ABA-6162-39C9-8C8C-C93F7216C4AB
-  Functions: 4783
-  Symbols:   16236
-  CStrings:  10181
+  UUID: 4DF7E8DA-DE14-3145-B4F5-01C5F92AF957
+  Functions: 4784
+  Symbols:   16239
+  CStrings:  10182
 
Symbols:
+ -[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:withEvent:]
+ -[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:withEvent:]
+ -[CSLaunchAgentXPCClient _sendMsgHandlingFinishReplyWithEvent:]
+ GCC_except_table4061
+ GCC_except_table4070
+ GCC_except_table4078
+ GCC_except_table4085
+ GCC_except_table4087
+ GCC_except_table4090
+ GCC_except_table4092
+ GCC_except_table4094
+ GCC_except_table4097
+ GCC_except_table4104
+ GCC_except_table4118
+ GCC_except_table4121
+ GCC_except_table4123
+ GCC_except_table4127
+ GCC_except_table4132
+ GCC_except_table4134
+ GCC_except_table4139
+ GCC_except_table4169
+ GCC_except_table4173
+ GCC_except_table4273
+ GCC_except_table4280
+ GCC_except_table4326
+ GCC_except_table4390
+ GCC_except_table4473
+ GCC_except_table4485
+ GCC_except_table4490
+ GCC_except_table4531
+ GCC_except_table4597
+ _AudioConverterFillComplexBuffer_BlockInvoke.7327
+ ___50-[CSUAFDownloadMonitor _startMonitoringWithQueue:]_block_invoke.284
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.331
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2.332
+ ___Block_byref_object_copy_.12694
+ ___Block_byref_object_copy_.13097
+ ___Block_byref_object_copy_.13394
+ ___Block_byref_object_copy_.13642
+ ___Block_byref_object_copy_.1382
+ ___Block_byref_object_copy_.14141
+ ___Block_byref_object_copy_.14714
+ ___Block_byref_object_copy_.14843
+ ___Block_byref_object_copy_.15711
+ ___Block_byref_object_copy_.1663
+ ___Block_byref_object_copy_.2229
+ ___Block_byref_object_copy_.2649
+ ___Block_byref_object_copy_.3410
+ ___Block_byref_object_copy_.4734
+ ___Block_byref_object_copy_.4955
+ ___Block_byref_object_copy_.5798
+ ___Block_byref_object_copy_.6208
+ ___Block_byref_object_copy_.7920
+ ___Block_byref_object_copy_.8202
+ ___Block_byref_object_copy_.8648
+ ___Block_byref_object_copy_.9407
+ ___Block_byref_object_dispose_.12695
+ ___Block_byref_object_dispose_.13098
+ ___Block_byref_object_dispose_.13395
+ ___Block_byref_object_dispose_.13643
+ ___Block_byref_object_dispose_.1383
+ ___Block_byref_object_dispose_.14142
+ ___Block_byref_object_dispose_.14715
+ ___Block_byref_object_dispose_.14844
+ ___Block_byref_object_dispose_.15712
+ ___Block_byref_object_dispose_.1664
+ ___Block_byref_object_dispose_.2230
+ ___Block_byref_object_dispose_.2650
+ ___Block_byref_object_dispose_.3411
+ ___Block_byref_object_dispose_.4735
+ ___Block_byref_object_dispose_.4956
+ ___Block_byref_object_dispose_.5799
+ ___Block_byref_object_dispose_.6209
+ ___Block_byref_object_dispose_.7921
+ ___Block_byref_object_dispose_.8203
+ ___Block_byref_object_dispose_.8649
+ ___Block_byref_object_dispose_.9408
+ ___block_literal_global.10285
+ ___block_literal_global.10382
+ ___block_literal_global.1105
+ ___block_literal_global.11256
+ ___block_literal_global.11461
+ ___block_literal_global.11616
+ ___block_literal_global.11833
+ ___block_literal_global.11870
+ ___block_literal_global.12740
+ ___block_literal_global.13208
+ ___block_literal_global.1330
+ ___block_literal_global.13495
+ ___block_literal_global.13741
+ ___block_literal_global.1400
+ ___block_literal_global.14047
+ ___block_literal_global.14433
+ ___block_literal_global.14535
+ ___block_literal_global.14591
+ ___block_literal_global.14738
+ ___block_literal_global.14986
+ ___block_literal_global.15079
+ ___block_literal_global.15168
+ ___block_literal_global.1522
+ ___block_literal_global.15498
+ ___block_literal_global.1550
+ ___block_literal_global.15736
+ ___block_literal_global.1577
+ ___block_literal_global.1621
+ ___block_literal_global.1692
+ ___block_literal_global.178.8335
+ ___block_literal_global.183.8329
+ ___block_literal_global.20.13193
+ ___block_literal_global.2246
+ ___block_literal_global.2342
+ ___block_literal_global.2398
+ ___block_literal_global.2590
+ ___block_literal_global.2665
+ ___block_literal_global.2777
+ ___block_literal_global.2826
+ ___block_literal_global.3138
+ ___block_literal_global.320.8253
+ ___block_literal_global.3322
+ ___block_literal_global.3430
+ ___block_literal_global.3730
+ ___block_literal_global.3884
+ ___block_literal_global.4155
+ ___block_literal_global.44.8431
+ ___block_literal_global.458.8201
+ ___block_literal_global.4762
+ ___block_literal_global.49.8429
+ ___block_literal_global.4923
+ ___block_literal_global.4971
+ ___block_literal_global.5566
+ ___block_literal_global.5650
+ ___block_literal_global.6430
+ ___block_literal_global.6577
+ ___block_literal_global.6645
+ ___block_literal_global.6702
+ ___block_literal_global.6819
+ ___block_literal_global.6837
+ ___block_literal_global.7032
+ ___block_literal_global.7095
+ ___block_literal_global.7155
+ ___block_literal_global.7256
+ ___block_literal_global.7292
+ ___block_literal_global.7575
+ ___block_literal_global.8455
+ ___block_literal_global.8476
+ ___block_literal_global.8531
+ ___block_literal_global.864
+ ___block_literal_global.8933
+ ___block_literal_global.8995
+ ___block_literal_global.9142
+ ___block_literal_global.9199
+ ___block_literal_global.9434
+ ___block_literal_global.9741
+ ___block_literal_global.975
+ ___block_literal_global.9872
+ ___block_literal_global.9980
+ __handleAudioCallbackDelegate:withEvent:.heartbeat
+ _objc_msgSend$_handleAudioCallbackDelegate:withEvent:
+ _objc_msgSend$_handleAudioProvidingDelegateMessageBody:withEvent:
+ _objc_msgSend$_sendMsgHandlingFinishReplyWithEvent:
+ _sharedHandler.onceToken.12739
+ _sharedHandler.sharedHandler.12741
+ _sharedInstance._sharedInstance.10383
+ _sharedInstance._sharedInstance.11257
+ _sharedInstance._sharedInstance.11871
+ _sharedInstance._sharedInstance.14536
+ _sharedInstance._sharedInstance.14592
+ _sharedInstance._sharedInstance.15080
+ _sharedInstance._sharedInstance.15169
+ _sharedInstance._sharedInstance.4156
+ _sharedInstance._sharedInstance.4924
+ _sharedInstance._sharedInstance.5567
+ _sharedInstance._sharedInstance.6431
+ _sharedInstance._sharedInstance.7033
+ _sharedInstance._sharedInstance.7257
+ _sharedInstance._sharedInstance.7576
+ _sharedInstance._sharedInstance.865
+ _sharedInstance._sharedInstance.976
+ _sharedInstance.onceToken.10381
+ _sharedInstance.onceToken.11255
+ _sharedInstance.onceToken.11460
+ _sharedInstance.onceToken.11869
+ _sharedInstance.onceToken.1329
+ _sharedInstance.onceToken.13494
+ _sharedInstance.onceToken.14534
+ _sharedInstance.onceToken.14590
+ _sharedInstance.onceToken.14985
+ _sharedInstance.onceToken.15078
+ _sharedInstance.onceToken.15167
+ _sharedInstance.onceToken.1549
+ _sharedInstance.onceToken.15497
+ _sharedInstance.onceToken.15735
+ _sharedInstance.onceToken.1620
+ _sharedInstance.onceToken.1691
+ _sharedInstance.onceToken.2341
+ _sharedInstance.onceToken.2397
+ _sharedInstance.onceToken.2664
+ _sharedInstance.onceToken.3429
+ _sharedInstance.onceToken.3883
+ _sharedInstance.onceToken.4154
+ _sharedInstance.onceToken.4761
+ _sharedInstance.onceToken.4922
+ _sharedInstance.onceToken.4970
+ _sharedInstance.onceToken.5565
+ _sharedInstance.onceToken.6429
+ _sharedInstance.onceToken.6576
+ _sharedInstance.onceToken.6818
+ _sharedInstance.onceToken.7031
+ _sharedInstance.onceToken.7255
+ _sharedInstance.onceToken.7574
+ _sharedInstance.onceToken.8475
+ _sharedInstance.onceToken.8530
+ _sharedInstance.onceToken.863
+ _sharedInstance.onceToken.8994
+ _sharedInstance.onceToken.9198
+ _sharedInstance.onceToken.974
+ _sharedInstance.onceToken.9740
+ _sharedInstance.onceToken.9871
+ _sharedInstance.onceToken.9979
+ _sharedInstance.sharedInstance.11462
+ _sharedInstance.sharedInstance.1331
+ _sharedInstance.sharedInstance.13496
+ _sharedInstance.sharedInstance.14987
+ _sharedInstance.sharedInstance.15499
+ _sharedInstance.sharedInstance.15737
+ _sharedInstance.sharedInstance.2343
+ _sharedInstance.sharedInstance.2399
+ _sharedInstance.sharedInstance.2666
+ _sharedInstance.sharedInstance.3431
+ _sharedInstance.sharedInstance.3885
+ _sharedInstance.sharedInstance.4972
+ _sharedInstance.sharedInstance.6578
+ _sharedInstance.sharedInstance.8477
+ _sharedInstance.sharedInstance.8996
+ _sharedInstance.sharedInstance.9200
+ _sharedInstance.sharedInstance.9873
+ _sharedInstance.sharedInstance.9981
+ _sharedInstance.sharedManager.6820
+ _sharedInstance.sharedManager.8532
+ _sharedLogger.onceToken.14046
+ _sharedLogger.onceToken.2776
+ _sharedLogger.onceToken.6644
+ _sharedLogger.onceToken.6836
+ _sharedLogger.shared.14048
+ _sharedManager.onceToken.14737
+ _sharedManager.onceToken.3321
+ _sharedManager.sharedManager.14739
+ _sharedMonitor.onceToken.5649
+ _sharedMonitor.sharedMonitor.5651
+ _sharedPreferences.onceToken.8932
- -[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:]
- -[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:]
- GCC_except_table4060
- GCC_except_table4069
- GCC_except_table4071
- GCC_except_table4079
- GCC_except_table4086
- GCC_except_table4088
- GCC_except_table4091
- GCC_except_table4093
- GCC_except_table4095
- GCC_except_table4103
- GCC_except_table4116
- GCC_except_table4119
- GCC_except_table4122
- GCC_except_table4124
- GCC_except_table4131
- GCC_except_table4133
- GCC_except_table4137
- GCC_except_table4168
- GCC_except_table4172
- GCC_except_table4272
- GCC_except_table4279
- GCC_except_table4325
- GCC_except_table4389
- GCC_except_table4472
- GCC_except_table4484
- GCC_except_table4489
- GCC_except_table4530
- GCC_except_table4596
- _AudioConverterFillComplexBuffer_BlockInvoke.7325
- ___50-[CSUAFDownloadMonitor _startMonitoringWithQueue:]_block_invoke.293
- ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.340
- ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2.341
- ___Block_byref_object_copy_.12690
- ___Block_byref_object_copy_.13092
- ___Block_byref_object_copy_.13389
- ___Block_byref_object_copy_.13637
- ___Block_byref_object_copy_.1380
- ___Block_byref_object_copy_.14136
- ___Block_byref_object_copy_.14709
- ___Block_byref_object_copy_.14838
- ___Block_byref_object_copy_.15706
- ___Block_byref_object_copy_.1661
- ___Block_byref_object_copy_.2225
- ___Block_byref_object_copy_.2645
- ___Block_byref_object_copy_.3409
- ___Block_byref_object_copy_.4733
- ___Block_byref_object_copy_.4954
- ___Block_byref_object_copy_.5797
- ___Block_byref_object_copy_.6207
- ___Block_byref_object_copy_.7919
- ___Block_byref_object_copy_.8199
- ___Block_byref_object_copy_.8649
- ___Block_byref_object_copy_.9408
- ___Block_byref_object_dispose_.12691
- ___Block_byref_object_dispose_.13093
- ___Block_byref_object_dispose_.13390
- ___Block_byref_object_dispose_.13638
- ___Block_byref_object_dispose_.1381
- ___Block_byref_object_dispose_.14137
- ___Block_byref_object_dispose_.14710
- ___Block_byref_object_dispose_.14839
- ___Block_byref_object_dispose_.15707
- ___Block_byref_object_dispose_.1662
- ___Block_byref_object_dispose_.2226
- ___Block_byref_object_dispose_.2646
- ___Block_byref_object_dispose_.3410
- ___Block_byref_object_dispose_.4734
- ___Block_byref_object_dispose_.4955
- ___Block_byref_object_dispose_.5798
- ___Block_byref_object_dispose_.6208
- ___Block_byref_object_dispose_.7920
- ___Block_byref_object_dispose_.8200
- ___Block_byref_object_dispose_.8650
- ___Block_byref_object_dispose_.9409
- ___block_literal_global.10286
- ___block_literal_global.10383
- ___block_literal_global.1103
- ___block_literal_global.11253
- ___block_literal_global.11458
- ___block_literal_global.11613
- ___block_literal_global.11830
- ___block_literal_global.11867
- ___block_literal_global.12736
- ___block_literal_global.13203
- ___block_literal_global.1328
- ___block_literal_global.13490
- ___block_literal_global.13736
- ___block_literal_global.1398
- ___block_literal_global.14042
- ___block_literal_global.14428
- ___block_literal_global.14530
- ___block_literal_global.14586
- ___block_literal_global.14733
- ___block_literal_global.14981
- ___block_literal_global.15074
- ___block_literal_global.15163
- ___block_literal_global.1520
- ___block_literal_global.1548
- ___block_literal_global.15493
- ___block_literal_global.15731
- ___block_literal_global.1575
- ___block_literal_global.1619
- ___block_literal_global.1690
- ___block_literal_global.178.8336
- ___block_literal_global.183.8330
- ___block_literal_global.20.13188
- ___block_literal_global.2242
- ___block_literal_global.2338
- ___block_literal_global.2394
- ___block_literal_global.2586
- ___block_literal_global.2661
- ___block_literal_global.2773
- ___block_literal_global.2822
- ___block_literal_global.3137
- ___block_literal_global.320.8247
- ___block_literal_global.3321
- ___block_literal_global.3429
- ___block_literal_global.3729
- ___block_literal_global.3883
- ___block_literal_global.4154
- ___block_literal_global.44.8432
- ___block_literal_global.458.8198
- ___block_literal_global.4761
- ___block_literal_global.49.8430
- ___block_literal_global.4922
- ___block_literal_global.4970
- ___block_literal_global.5565
- ___block_literal_global.5649
- ___block_literal_global.6429
- ___block_literal_global.6576
- ___block_literal_global.6644
- ___block_literal_global.6701
- ___block_literal_global.6817
- ___block_literal_global.6835
- ___block_literal_global.7030
- ___block_literal_global.7093
- ___block_literal_global.7153
- ___block_literal_global.7254
- ___block_literal_global.7290
- ___block_literal_global.7573
- ___block_literal_global.8456
- ___block_literal_global.8477
- ___block_literal_global.8532
- ___block_literal_global.862
- ___block_literal_global.8934
- ___block_literal_global.8996
- ___block_literal_global.9143
- ___block_literal_global.9200
- ___block_literal_global.9435
- ___block_literal_global.973
- ___block_literal_global.9742
- ___block_literal_global.9873
- ___block_literal_global.9981
- __handleAudioCallbackDelegate:.heartbeat
- _objc_msgSend$_handleAudioCallbackDelegate:
- _objc_msgSend$_handleAudioProvidingDelegateMessageBody:
- _sharedHandler.onceToken.12735
- _sharedHandler.sharedHandler.12737
- _sharedInstance._sharedInstance.10384
- _sharedInstance._sharedInstance.11254
- _sharedInstance._sharedInstance.11868
- _sharedInstance._sharedInstance.14531
- _sharedInstance._sharedInstance.14587
- _sharedInstance._sharedInstance.15075
- _sharedInstance._sharedInstance.15164
- _sharedInstance._sharedInstance.4155
- _sharedInstance._sharedInstance.4923
- _sharedInstance._sharedInstance.5566
- _sharedInstance._sharedInstance.6430
- _sharedInstance._sharedInstance.7031
- _sharedInstance._sharedInstance.7255
- _sharedInstance._sharedInstance.7574
- _sharedInstance._sharedInstance.863
- _sharedInstance._sharedInstance.974
- _sharedInstance.onceToken.10382
- _sharedInstance.onceToken.11252
- _sharedInstance.onceToken.11457
- _sharedInstance.onceToken.11866
- _sharedInstance.onceToken.1327
- _sharedInstance.onceToken.13489
- _sharedInstance.onceToken.14529
- _sharedInstance.onceToken.14585
- _sharedInstance.onceToken.14980
- _sharedInstance.onceToken.15073
- _sharedInstance.onceToken.15162
- _sharedInstance.onceToken.1547
- _sharedInstance.onceToken.15492
- _sharedInstance.onceToken.15730
- _sharedInstance.onceToken.1618
- _sharedInstance.onceToken.1689
- _sharedInstance.onceToken.2337
- _sharedInstance.onceToken.2393
- _sharedInstance.onceToken.2660
- _sharedInstance.onceToken.3428
- _sharedInstance.onceToken.3882
- _sharedInstance.onceToken.4153
- _sharedInstance.onceToken.4760
- _sharedInstance.onceToken.4921
- _sharedInstance.onceToken.4969
- _sharedInstance.onceToken.5564
- _sharedInstance.onceToken.6428
- _sharedInstance.onceToken.6575
- _sharedInstance.onceToken.6816
- _sharedInstance.onceToken.7029
- _sharedInstance.onceToken.7253
- _sharedInstance.onceToken.7572
- _sharedInstance.onceToken.8476
- _sharedInstance.onceToken.8531
- _sharedInstance.onceToken.861
- _sharedInstance.onceToken.8995
- _sharedInstance.onceToken.9199
- _sharedInstance.onceToken.972
- _sharedInstance.onceToken.9741
- _sharedInstance.onceToken.9872
- _sharedInstance.onceToken.9980
- _sharedInstance.sharedInstance.11459
- _sharedInstance.sharedInstance.1329
- _sharedInstance.sharedInstance.13491
- _sharedInstance.sharedInstance.14982
- _sharedInstance.sharedInstance.15494
- _sharedInstance.sharedInstance.15732
- _sharedInstance.sharedInstance.2339
- _sharedInstance.sharedInstance.2395
- _sharedInstance.sharedInstance.2662
- _sharedInstance.sharedInstance.3430
- _sharedInstance.sharedInstance.3884
- _sharedInstance.sharedInstance.4971
- _sharedInstance.sharedInstance.6577
- _sharedInstance.sharedInstance.8478
- _sharedInstance.sharedInstance.8997
- _sharedInstance.sharedInstance.9201
- _sharedInstance.sharedInstance.9874
- _sharedInstance.sharedInstance.9982
- _sharedInstance.sharedManager.6818
- _sharedInstance.sharedManager.8533
- _sharedLogger.onceToken.14041
- _sharedLogger.onceToken.2772
- _sharedLogger.onceToken.6643
- _sharedLogger.onceToken.6834
- _sharedLogger.shared.14043
- _sharedManager.onceToken.14732
- _sharedManager.onceToken.3320
- _sharedManager.sharedManager.14734
- _sharedMonitor.onceToken.5648
- _sharedMonitor.sharedMonitor.5650
- _sharedPreferences.onceToken.8933
CStrings:
+ "%s Cannot handle nil event"
+ "-[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:withEvent:]"
+ "-[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:withEvent:]"
+ "_handleAudioCallbackDelegate:withEvent:"
+ "_handleAudioProvidingDelegateMessageBody:withEvent:"
+ "_sendMsgHandlingFinishReplyWithEvent:"
- "%s Cannot handle nil message"
- "-[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:]"
- "-[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:]"
- "_handleAudioCallbackDelegate:"
- "_handleAudioProvidingDelegateMessageBody:"

```
