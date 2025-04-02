## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0xb6774
+3405.20.3.0.0
+  __TEXT.__text: 0xb6e74
   __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_methlist: 0xb860
+  __TEXT.__objc_methlist: 0xb8c0
   __TEXT.__const: 0x848
   __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x12e3e
+  __TEXT.__cstring: 0x12eaf
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x317c
-  __TEXT.__oslogstring: 0xcd41
-  __TEXT.__unwind_info: 0x30d0
+  __TEXT.__gcc_except_tab: 0x31fc
+  __TEXT.__oslogstring: 0xcd7a
+  __TEXT.__unwind_info: 0x3100
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x1a75
-  __TEXT.__objc_methname: 0x1ef62
-  __TEXT.__objc_methtype: 0x42f2
-  __TEXT.__objc_stubs: 0xf9c0
+  __TEXT.__objc_classname: 0x1a52
+  __TEXT.__objc_methname: 0x1f041
+  __TEXT.__objc_methtype: 0x42ce
+  __TEXT.__objc_stubs: 0xfa60
   __DATA_CONST.__got: 0xba0
-  __DATA_CONST.__const: 0xe40
+  __DATA_CONST.__const: 0xe70
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x65a8
+  __DATA_CONST.__objc_selrefs: 0x65d8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xde8
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x3190
-  __AUTH_CONST.__cfstring: 0x8640
-  __AUTH_CONST.__objc_const: 0x12160
+  __AUTH_CONST.__const: 0x31b0
+  __AUTH_CONST.__cfstring: 0x8680
+  __AUTH_CONST.__objc_const: 0x12170
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
   __AUTH.__objc_data: 0x4258
   __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0xbfc
-  __DATA.__data: 0x1300
-  __DATA.__bss: 0xc28
+  __DATA.__objc_ivar: 0xc00
+  __DATA.__data: 0x12a8
+  __DATA.__bss: 0xc30
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4510
-  Symbols:   10858
-  CStrings:  8388
+  Functions: 4518
+  Symbols:   10873
+  CStrings:  8400
 
Symbols:
+ +[CSExclaveMessageHandlingFactory exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:]
+ +[CSUtils shouldDisableSpeakerRecognition]
+ -[CSAudioRecorder _recordDeviceInfoWithStreamHandleId:]
+ -[CSExclaveRecordClient adBlockerReset]
+ -[CSExclaveRecordClient deinitializeSecondPass]
+ -[CSFAudioRecordDeviceInfo initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:isNarrowBand:]
+ -[CSFAudioRecordDeviceInfo isNarrowBand]
+ -[CSLaunchAgentXPCClient _disconnect]
+ -[CSLaunchAgentXPCClient adBlockerReset]
+ -[CSLaunchAgentXPCClient deinitializeSecondPass]
+ -[CSLaunchAgentXPCClient macUserSessionMonitor:sessionActive:]
+ -[CSLaunchAgentXPCClient recordDeviceInfoWithStreamHandleId:]
+ GCC_except_table1017
+ GCC_except_table1024
+ GCC_except_table1302
+ GCC_except_table1331
+ GCC_except_table1420
+ GCC_except_table1425
+ GCC_except_table1427
+ GCC_except_table1430
+ GCC_except_table1596
+ GCC_except_table1812
+ GCC_except_table1813
+ GCC_except_table1814
+ GCC_except_table1823
+ GCC_except_table1826
+ GCC_except_table1832
+ GCC_except_table1838
+ GCC_except_table1840
+ GCC_except_table1841
+ GCC_except_table1905
+ GCC_except_table1910
+ GCC_except_table1982
+ GCC_except_table2023
+ GCC_except_table2025
+ GCC_except_table2026
+ GCC_except_table2033
+ GCC_except_table2034
+ GCC_except_table2043
+ GCC_except_table2056
+ GCC_except_table2099
+ GCC_except_table2168
+ GCC_except_table2265
+ GCC_except_table2302
+ GCC_except_table2442
+ GCC_except_table3155
+ GCC_except_table3180
+ GCC_except_table3216
+ GCC_except_table3239
+ GCC_except_table3252
+ GCC_except_table3385
+ GCC_except_table3445
+ GCC_except_table3459
+ GCC_except_table3502
+ GCC_except_table3536
+ GCC_except_table3538
+ GCC_except_table3543
+ GCC_except_table3563
+ GCC_except_table3566
+ GCC_except_table3570
+ GCC_except_table3572
+ GCC_except_table3605
+ GCC_except_table3610
+ GCC_except_table3667
+ GCC_except_table3715
+ GCC_except_table3721
+ GCC_except_table3777
+ GCC_except_table3787
+ GCC_except_table3790
+ GCC_except_table3817
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3831
+ GCC_except_table3845
+ GCC_except_table3846
+ GCC_except_table3852
+ GCC_except_table3853
+ GCC_except_table3855
+ GCC_except_table3856
+ GCC_except_table3859
+ GCC_except_table3867
+ GCC_except_table3874
+ GCC_except_table3890
+ GCC_except_table3891
+ GCC_except_table3893
+ GCC_except_table3895
+ GCC_except_table3897
+ GCC_except_table3904
+ GCC_except_table3906
+ GCC_except_table3910
+ GCC_except_table3911
+ GCC_except_table3941
+ GCC_except_table3945
+ GCC_except_table4045
+ GCC_except_table4052
+ GCC_except_table4094
+ GCC_except_table4152
+ GCC_except_table4222
+ GCC_except_table4234
+ GCC_except_table4239
+ GCC_except_table4274
+ GCC_except_table4340
+ GCC_except_table814
+ GCC_except_table824
+ GCC_except_table895
+ GCC_except_table902
+ GCC_except_table919
+ GCC_except_table927
+ GCC_except_table931
+ GCC_except_table936
+ GCC_except_table940
+ GCC_except_table949
+ OBJC_IVAR_$_CSFAudioRecordDeviceInfo._isNarrowBand
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.176
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.177
+ __24-[CSAudioProvider start]_block_invoke.51
+ __24-[CSAudioProvider start]_block_invoke.53
+ __37-[CSLaunchAgentXPCClient _disconnect]_block_invoke.19
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.132
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.137
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.142
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.146
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.138
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.143
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.144
+ __54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.96
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.125
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.126
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.129
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.102
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.103
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.105
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.111
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.114
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.115
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.99
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.106
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.116
+ __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.182
+ __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.124
+ __64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke.81
+ __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.164
+ __Block_byref_object_copy_.11456
+ __Block_byref_object_copy_.11848
+ __Block_byref_object_copy_.12138
+ __Block_byref_object_copy_.12390
+ __Block_byref_object_copy_.12884
+ __Block_byref_object_copy_.13393
+ __Block_byref_object_copy_.13475
+ __Block_byref_object_copy_.14180
+ __Block_byref_object_copy_.2193
+ __Block_byref_object_copy_.2588
+ __Block_byref_object_copy_.3310
+ __Block_byref_object_copy_.4512
+ __Block_byref_object_copy_.4705
+ __Block_byref_object_copy_.5461
+ __Block_byref_object_copy_.5525
+ __Block_byref_object_copy_.7462
+ __Block_byref_object_copy_.7709
+ __Block_byref_object_copy_.8868
+ __Block_byref_object_dispose_.11457
+ __Block_byref_object_dispose_.11849
+ __Block_byref_object_dispose_.12139
+ __Block_byref_object_dispose_.12391
+ __Block_byref_object_dispose_.12885
+ __Block_byref_object_dispose_.13394
+ __Block_byref_object_dispose_.13476
+ __Block_byref_object_dispose_.14181
+ __Block_byref_object_dispose_.2194
+ __Block_byref_object_dispose_.2589
+ __Block_byref_object_dispose_.3311
+ __Block_byref_object_dispose_.4513
+ __Block_byref_object_dispose_.4706
+ __Block_byref_object_dispose_.5462
+ __Block_byref_object_dispose_.5526
+ __Block_byref_object_dispose_.7463
+ __Block_byref_object_dispose_.7710
+ __Block_byref_object_dispose_.8869
+ ___37-[CSLaunchAgentXPCClient _disconnect]_block_invoke
+ ___61-[CSLaunchAgentXPCClient recordDeviceInfoWithStreamHandleId:]_block_invoke
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ __block_literal_global.10564
+ __block_literal_global.10678
+ __block_literal_global.10805
+ __block_literal_global.10919
+ __block_literal_global.10956
+ __block_literal_global.1126
+ __block_literal_global.11501
+ __block_literal_global.11958
+ __block_literal_global.12241
+ __block_literal_global.12482
+ __block_literal_global.1258
+ __block_literal_global.12788
+ __block_literal_global.13147
+ __block_literal_global.13278
+ __block_literal_global.13417
+ __block_literal_global.13673
+ __block_literal_global.13746
+ __block_literal_global.14012
+ __block_literal_global.14206
+ __block_literal_global.1508
+ __block_literal_global.1540
+ __block_literal_global.156.7843
+ __block_literal_global.1568
+ __block_literal_global.1614
+ __block_literal_global.1682
+ __block_literal_global.21.11945
+ __block_literal_global.2179
+ __block_literal_global.2290
+ __block_literal_global.2336
+ __block_literal_global.2375
+ __block_literal_global.2606
+ __block_literal_global.2714
+ __block_literal_global.2758
+ __block_literal_global.2795
+ __block_literal_global.3068
+ __block_literal_global.3222
+ __block_literal_global.3332
+ __block_literal_global.349.7758
+ __block_literal_global.3620
+ __block_literal_global.3702
+ __block_literal_global.402
+ __block_literal_global.4540
+ __block_literal_global.4673
+ __block_literal_global.4723
+ __block_literal_global.502
+ __block_literal_global.5229
+ __block_literal_global.5312
+ __block_literal_global.5537
+ __block_literal_global.636
+ __block_literal_global.67.7186
+ __block_literal_global.7243
+ __block_literal_global.8573
+ __block_literal_global.8642
+ __block_literal_global.8901
+ __block_literal_global.903
+ __block_literal_global.9204
+ __block_literal_global.9331
+ __block_literal_global.9442
+ __block_literal_global.9718
+ _handleAudioCallbackDelegate:.heartbeat
+ _kXPCEncodeKeyIsNarrowBand
+ _objc_msgSend$_disconnect
+ _objc_msgSend$_recordDeviceInfoWithStreamHandleId:
+ _objc_msgSend$adBlockerReset
+ _objc_msgSend$deinitializeSecondPass
+ _objc_msgSend$initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:isNarrowBand:
+ _objc_msgSend$recordDeviceInfoWithStreamHandleId:
+ sharedInstance._sharedInstance.10565
+ sharedInstance._sharedInstance.10957
+ sharedInstance._sharedInstance.1127
+ sharedInstance._sharedInstance.13279
+ sharedInstance._sharedInstance.13674
+ sharedInstance._sharedInstance.13747
+ sharedInstance._sharedInstance.4674
+ sharedInstance._sharedInstance.5230
+ sharedInstance._sharedInstance.7244
+ sharedInstance._sharedInstance.9719
+ sharedInstance.onceToken.10563
+ sharedInstance.onceToken.10677
+ sharedInstance.onceToken.10955
+ sharedInstance.onceToken.1125
+ sharedInstance.onceToken.12240
+ sharedInstance.onceToken.13277
+ sharedInstance.onceToken.13672
+ sharedInstance.onceToken.13745
+ sharedInstance.onceToken.14011
+ sharedInstance.onceToken.14205
+ sharedInstance.onceToken.1539
+ sharedInstance.onceToken.1613
+ sharedInstance.onceToken.1681
+ sharedInstance.onceToken.2289
+ sharedInstance.onceToken.2335
+ sharedInstance.onceToken.2374
+ sharedInstance.onceToken.2605
+ sharedInstance.onceToken.3331
+ sharedInstance.onceToken.3701
+ sharedInstance.onceToken.4539
+ sharedInstance.onceToken.4672
+ sharedInstance.onceToken.4722
+ sharedInstance.onceToken.501
+ sharedInstance.onceToken.5228
+ sharedInstance.onceToken.635
+ sharedInstance.onceToken.7242
+ sharedInstance.onceToken.8641
+ sharedInstance.onceToken.9203
+ sharedInstance.onceToken.9330
+ sharedInstance.onceToken.9441
+ sharedInstance.onceToken.9717
+ sharedInstance.sharedInstance.10679
+ sharedInstance.sharedInstance.12242
+ sharedInstance.sharedInstance.14013
+ sharedInstance.sharedInstance.14207
+ sharedInstance.sharedInstance.2291
+ sharedInstance.sharedInstance.2376
+ sharedInstance.sharedInstance.2607
+ sharedInstance.sharedInstance.3333
+ sharedInstance.sharedInstance.3703
+ sharedInstance.sharedInstance.4724
+ sharedInstance.sharedInstance.503
+ sharedInstance.sharedInstance.637
+ sharedInstance.sharedInstance.8643
+ sharedInstance.sharedInstance.9332
+ sharedInstance.sharedInstance.9443
+ sharedLogger.onceToken.12787
+ sharedLogger.onceToken.2713
+ sharedLogger.shared.12789
+ sharedManager.onceToken.13416
+ sharedMonitor.onceToken.5311
+ sharedMonitor.sharedMonitor.5313
- +[CSExclaveMessageHandlingFactory exclaveSecondPassVoiceTriggerAnalyzer]
- -[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
- -[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
- -[CSFAudioRecordDeviceInfo initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:]
- GCC_except_table1016
- GCC_except_table1023
- GCC_except_table1300
- GCC_except_table1329
- GCC_except_table1416
- GCC_except_table1418
- GCC_except_table1419
- GCC_except_table1421
- GCC_except_table1592
- GCC_except_table1808
- GCC_except_table1809
- GCC_except_table1810
- GCC_except_table1811
- GCC_except_table1818
- GCC_except_table1828
- GCC_except_table1834
- GCC_except_table1836
- GCC_except_table1837
- GCC_except_table1901
- GCC_except_table1906
- GCC_except_table1978
- GCC_except_table2018
- GCC_except_table2019
- GCC_except_table2021
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2039
- GCC_except_table2052
- GCC_except_table2095
- GCC_except_table2164
- GCC_except_table2261
- GCC_except_table2298
- GCC_except_table2434
- GCC_except_table3154
- GCC_except_table3179
- GCC_except_table3212
- GCC_except_table3238
- GCC_except_table3251
- GCC_except_table3384
- GCC_except_table3444
- GCC_except_table3458
- GCC_except_table3500
- GCC_except_table3534
- GCC_except_table3537
- GCC_except_table3540
- GCC_except_table3562
- GCC_except_table3565
- GCC_except_table3567
- GCC_except_table3571
- GCC_except_table3604
- GCC_except_table3606
- GCC_except_table3666
- GCC_except_table3714
- GCC_except_table3720
- GCC_except_table3775
- GCC_except_table3783
- GCC_except_table3788
- GCC_except_table3810
- GCC_except_table3811
- GCC_except_table3813
- GCC_except_table3827
- GCC_except_table3838
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3842
- GCC_except_table3850
- GCC_except_table3857
- GCC_except_table3861
- GCC_except_table3879
- GCC_except_table3880
- GCC_except_table3882
- GCC_except_table3883
- GCC_except_table3885
- GCC_except_table3889
- GCC_except_table3898
- GCC_except_table3902
- GCC_except_table3903
- GCC_except_table3933
- GCC_except_table3937
- GCC_except_table4037
- GCC_except_table4044
- GCC_except_table4086
- GCC_except_table4144
- GCC_except_table4214
- GCC_except_table4226
- GCC_except_table4231
- GCC_except_table4266
- GCC_except_table4332
- GCC_except_table813
- GCC_except_table823
- GCC_except_table893
- GCC_except_table901
- GCC_except_table916
- GCC_except_table922
- GCC_except_table928
- GCC_except_table933
- GCC_except_table937
- GCC_except_table948
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.183
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.184
- __24-[CSAudioProvider start]_block_invoke.58
- __24-[CSAudioProvider start]_block_invoke.60
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.139
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.144
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.149
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.153
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.145
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.150
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.151
- __54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.103
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.132
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.133
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.136
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.106
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.116
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.117
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.119
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.121
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.122
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.125
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.113
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.123
- __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.189
- __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.131
- __64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke.88
- __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.171
- __Block_byref_object_copy_.11444
- __Block_byref_object_copy_.11825
- __Block_byref_object_copy_.12107
- __Block_byref_object_copy_.12359
- __Block_byref_object_copy_.12848
- __Block_byref_object_copy_.13348
- __Block_byref_object_copy_.13430
- __Block_byref_object_copy_.14136
- __Block_byref_object_copy_.2186
- __Block_byref_object_copy_.2581
- __Block_byref_object_copy_.3315
- __Block_byref_object_copy_.4508
- __Block_byref_object_copy_.4701
- __Block_byref_object_copy_.5460
- __Block_byref_object_copy_.5524
- __Block_byref_object_copy_.7448
- __Block_byref_object_copy_.7707
- __Block_byref_object_copy_.8858
- __Block_byref_object_dispose_.11445
- __Block_byref_object_dispose_.11826
- __Block_byref_object_dispose_.12108
- __Block_byref_object_dispose_.12360
- __Block_byref_object_dispose_.12849
- __Block_byref_object_dispose_.13349
- __Block_byref_object_dispose_.13431
- __Block_byref_object_dispose_.14137
- __Block_byref_object_dispose_.2187
- __Block_byref_object_dispose_.2582
- __Block_byref_object_dispose_.3316
- __Block_byref_object_dispose_.4509
- __Block_byref_object_dispose_.4702
- __Block_byref_object_dispose_.5461
- __Block_byref_object_dispose_.5525
- __Block_byref_object_dispose_.7449
- __Block_byref_object_dispose_.7708
- __Block_byref_object_dispose_.8859
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSystemDaemonStateMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemDaemonStateMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_CSSystemDaemonStateMonitorDelegate
- __OBJC_LABEL_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
- __OBJC_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
- ___70-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
- ___81-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
- ___83-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke_2
- __block_literal_global.10551
- __block_literal_global.10665
- __block_literal_global.10792
- __block_literal_global.10906
- __block_literal_global.10943
- __block_literal_global.1119
- __block_literal_global.11489
- __block_literal_global.11926
- __block_literal_global.12210
- __block_literal_global.12451
- __block_literal_global.1251
- __block_literal_global.12757
- __block_literal_global.13102
- __block_literal_global.13233
- __block_literal_global.13372
- __block_literal_global.13628
- __block_literal_global.13701
- __block_literal_global.13968
- __block_literal_global.14162
- __block_literal_global.1501
- __block_literal_global.1533
- __block_literal_global.156.7842
- __block_literal_global.1561
- __block_literal_global.1607
- __block_literal_global.1675
- __block_literal_global.2172
- __block_literal_global.2283
- __block_literal_global.2329
- __block_literal_global.2368
- __block_literal_global.2599
- __block_literal_global.2707
- __block_literal_global.2751
- __block_literal_global.2788
- __block_literal_global.3073
- __block_literal_global.3227
- __block_literal_global.3337
- __block_literal_global.349.7756
- __block_literal_global.3619
- __block_literal_global.3701
- __block_literal_global.401
- __block_literal_global.4536
- __block_literal_global.4669
- __block_literal_global.4719
- __block_literal_global.496
- __block_literal_global.5228
- __block_literal_global.5311
- __block_literal_global.5536
- __block_literal_global.629
- __block_literal_global.67.7187
- __block_literal_global.7244
- __block_literal_global.8574
- __block_literal_global.8643
- __block_literal_global.8891
- __block_literal_global.896
- __block_literal_global.9194
- __block_literal_global.9324
- __block_literal_global.9435
- __block_literal_global.9713
- _objc_msgSend$initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:
- sharedInstance._sharedInstance.10552
- sharedInstance._sharedInstance.10944
- sharedInstance._sharedInstance.1120
- sharedInstance._sharedInstance.13234
- sharedInstance._sharedInstance.13629
- sharedInstance._sharedInstance.13702
- sharedInstance._sharedInstance.4670
- sharedInstance._sharedInstance.5229
- sharedInstance._sharedInstance.7245
- sharedInstance._sharedInstance.9714
- sharedInstance.onceToken.10550
- sharedInstance.onceToken.10664
- sharedInstance.onceToken.10942
- sharedInstance.onceToken.1118
- sharedInstance.onceToken.12209
- sharedInstance.onceToken.13232
- sharedInstance.onceToken.13627
- sharedInstance.onceToken.13700
- sharedInstance.onceToken.13967
- sharedInstance.onceToken.14161
- sharedInstance.onceToken.1532
- sharedInstance.onceToken.1606
- sharedInstance.onceToken.1674
- sharedInstance.onceToken.2282
- sharedInstance.onceToken.2328
- sharedInstance.onceToken.2367
- sharedInstance.onceToken.2598
- sharedInstance.onceToken.3336
- sharedInstance.onceToken.3700
- sharedInstance.onceToken.4535
- sharedInstance.onceToken.4668
- sharedInstance.onceToken.4718
- sharedInstance.onceToken.495
- sharedInstance.onceToken.5227
- sharedInstance.onceToken.628
- sharedInstance.onceToken.7243
- sharedInstance.onceToken.8642
- sharedInstance.onceToken.9193
- sharedInstance.onceToken.9323
- sharedInstance.onceToken.9434
- sharedInstance.onceToken.9712
- sharedInstance.sharedInstance.10666
- sharedInstance.sharedInstance.12211
- sharedInstance.sharedInstance.13969
- sharedInstance.sharedInstance.14163
- sharedInstance.sharedInstance.2284
- sharedInstance.sharedInstance.2369
- sharedInstance.sharedInstance.2600
- sharedInstance.sharedInstance.3338
- sharedInstance.sharedInstance.3702
- sharedInstance.sharedInstance.4720
- sharedInstance.sharedInstance.497
- sharedInstance.sharedInstance.630
- sharedInstance.sharedInstance.8644
- sharedInstance.sharedInstance.9325
- sharedInstance.sharedInstance.9436
- sharedLogger.onceToken.12756
- sharedLogger.onceToken.2706
- sharedLogger.shared.12758
- sharedManager.onceToken.13371
- sharedMonitor.onceToken.5310
- sharedMonitor.sharedMonitor.5312
CStrings:
+ "%@ {route = %@, isRemoteDevice = %d, remoteDeviceUID = %@, remoteDeviceProductIdentifier = %@, remoteDeviceUIDString = %@, halDeviceUID = %@, isNarrowBand = %d}"
+ "%s Launch Agent received audioCallBack from systemDaemon, heartbeat = %{public}lld, for streamId: %{public}lu"
+ "%s Not allowed to initialize new xpcConnection when current user is inactive"
+ "%s Notify Mac User session %@"
+ "%s stopAudioStream successfully? %d"
+ "-[CSAudioRecorder _recordDeviceInfoWithStreamHandleId:]"
+ "-[CSLaunchAgentXPCClient _disconnect]_block_invoke"
+ "-[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:]"
+ "-[CSLaunchAgentXPCClient adBlockerReset]"
+ "-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]"
+ "-[CSLaunchAgentXPCClient recordDeviceInfoWithStreamHandleId:]"
+ "-[CSMacUserSessionMonitor _notifySessionActive:]"
+ "@64@0:8@16B24@28@36@44@52B60"
+ "TB,R,N,V_isNarrowBand"
+ "_disconnect"
+ "_isNarrowBand"
+ "_recordDeviceInfoWithStreamHandleId:"
+ "adBlockerReset"
+ "deinitializeSecondPass"
+ "exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:"
+ "inactive"
+ "initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:isNarrowBand:"
+ "recordDeviceInfoWithStreamHandleId:"
+ "shouldDisableSpeakerRecognition"
- "%@ {route = %@, isRemoteDevice = %d, remoteDeviceUID = %@, remoteDeviceProductIdentifier = %@, remoteDeviceUIDString = %@, halDeviceUID = %@}"
- "%s CSAudioProvider[%{public}@]:corespeechd_system crashed"
- "%s CSAudioProvider[%{public}@]:corespeechd_system recovered from crash"
- "%s LaunchAgentXPCAudioProvidingDelegate messageType : %{public}lld"
- "-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]"
- "-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]"
- "-[CSAudioRecorder recordDeviceInfoWithStreamHandleId:recordDeviceIndicator:]"
- "-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke"
- "@60@0:8@16B24@28@36@44@52"
- "CSSystemDaemonStateMonitorDelegate"
- "exclaveSecondPassVoiceTriggerAnalyzer"
- "initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:halDeviceUID:"
- "v24@0:8@\"CSSystemDaemonStateMonitor\"16"

```
