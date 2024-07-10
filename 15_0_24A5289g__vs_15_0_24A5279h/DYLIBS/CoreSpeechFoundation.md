## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-3400.145.2.0.0
-  __TEXT.__text: 0xa5d7c
-  __TEXT.__auth_stubs: 0x1a70
-  __TEXT.__objc_methlist: 0x9c58
+3400.139.2.0.0
+  __TEXT.__text: 0xa5630
+  __TEXT.__auth_stubs: 0x1a50
+  __TEXT.__objc_methlist: 0x9c10
   __TEXT.__const: 0x7e0
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__cstring: 0x10efb
+  __TEXT.__cstring: 0x10e01
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__gcc_except_tab: 0x28b8
-  __TEXT.__oslogstring: 0xbb77
+  __TEXT.__gcc_except_tab: 0x28ac
+  __TEXT.__oslogstring: 0xbb61
   __TEXT.__dlopen_cstrs: 0xc6
-  __TEXT.__unwind_info: 0x2b78
+  __TEXT.__unwind_info: 0x2b60
   __TEXT.__eh_frame: 0xe8
   __TEXT.__objc_classname: 0x1748
-  __TEXT.__objc_methname: 0x1c900
-  __TEXT.__objc_methtype: 0x3ce2
-  __TEXT.__objc_stubs: 0xe820
-  __DATA_CONST.__got: 0xac8
+  __TEXT.__objc_methname: 0x1c77b
+  __TEXT.__objc_methtype: 0x3cdf
+  __TEXT.__objc_stubs: 0xe7c0
+  __DATA_CONST.__got: 0xac0
   __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cc8
+  __DATA_CONST.__objc_selrefs: 0x5c90
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0xd50
+  __AUTH_CONST.__auth_got: 0xd40
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x2df0
-  __AUTH_CONST.__cfstring: 0x7960
+  __AUTH_CONST.__const: 0x2dd0
+  __AUTH_CONST.__cfstring: 0x78c0
   __AUTH_CONST.__objc_const: 0x11718
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x300

   __AUTH.__data: 0x2d0
   __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0xe08
-  __DATA.__bss: 0xb88
+  __DATA.__bss: 0xb78
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4116
-  Symbols:   9891
-  CStrings:  1911
+  Functions: 4109
+  Symbols:   9875
+  CStrings:  1904
 
Symbols:
+ +[CSUtils supportBeepCanceller:]
+ -[CSAudioPreprocessor initWithSampleRate:withNumberOfChannels:]
+ AudioConverterFillComplexBuffer_BlockInvoke.6167
+ GCC_except_table1221
+ GCC_except_table1317
+ GCC_except_table1494
+ GCC_except_table1694
+ GCC_except_table1701
+ GCC_except_table1704
+ GCC_except_table1708
+ GCC_except_table1715
+ GCC_except_table1721
+ GCC_except_table1723
+ GCC_except_table1772
+ GCC_except_table1867
+ GCC_except_table1870
+ GCC_except_table1877
+ GCC_except_table1886
+ GCC_except_table1898
+ GCC_except_table1941
+ GCC_except_table2065
+ GCC_except_table2102
+ GCC_except_table2238
+ GCC_except_table2242
+ GCC_except_table2310
+ GCC_except_table2321
+ GCC_except_table2328
+ GCC_except_table2345
+ GCC_except_table2352
+ GCC_except_table2372
+ GCC_except_table2393
+ GCC_except_table2489
+ GCC_except_table2491
+ GCC_except_table2619
+ GCC_except_table2730
+ GCC_except_table2748
+ GCC_except_table2757
+ GCC_except_table2760
+ GCC_except_table2762
+ GCC_except_table2763
+ GCC_except_table2767
+ GCC_except_table2787
+ GCC_except_table2828
+ GCC_except_table2929
+ GCC_except_table2960
+ GCC_except_table2961
+ GCC_except_table2962
+ GCC_except_table2963
+ GCC_except_table2986
+ GCC_except_table3145
+ GCC_except_table3205
+ GCC_except_table3219
+ GCC_except_table3250
+ GCC_except_table3251
+ GCC_except_table3253
+ GCC_except_table3256
+ GCC_except_table3257
+ GCC_except_table3299
+ GCC_except_table3300
+ GCC_except_table3301
+ GCC_except_table3302
+ GCC_except_table3303
+ GCC_except_table3394
+ GCC_except_table3399
+ GCC_except_table3454
+ GCC_except_table3455
+ GCC_except_table3464
+ GCC_except_table3465
+ GCC_except_table3467
+ GCC_except_table3468
+ GCC_except_table3477
+ GCC_except_table3478
+ GCC_except_table3480
+ GCC_except_table3481
+ GCC_except_table3483
+ GCC_except_table3487
+ GCC_except_table3496
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3531
+ GCC_except_table3535
+ GCC_except_table3636
+ GCC_except_table3685
+ GCC_except_table3743
+ GCC_except_table3812
+ GCC_except_table3829
+ GCC_except_table3928
+ GCC_except_table957
+ GCC_except_table964
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.170
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.171
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.126
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.131
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.136
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.140
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.132
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.137
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.138
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.120
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.123
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.110
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.113
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.111
+ __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.176
+ __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.118
+ __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.158
+ __88-[CSVoiceTriggerAlwaysOnProcessor disableVoiceTriggerOnAlwaysOnProcessorWithCompletion:]_block_invoke.15
+ __93-[CSVoiceTriggerAlwaysOnProcessor enableVoiceTriggerOnAlwaysOnProcessorWithAsset:completion:]_block_invoke.11
+ __93-[CSVoiceTriggerAlwaysOnProcessor enableVoiceTriggerOnAlwaysOnProcessorWithAsset:completion:]_block_invoke.13
+ __Block_byref_object_copy_.10280
+ __Block_byref_object_copy_.10654
+ __Block_byref_object_copy_.10903
+ __Block_byref_object_copy_.11201
+ __Block_byref_object_copy_.11700
+ __Block_byref_object_copy_.11780
+ __Block_byref_object_copy_.12473
+ __Block_byref_object_copy_.3082
+ __Block_byref_object_copy_.4140
+ __Block_byref_object_copy_.4333
+ __Block_byref_object_copy_.4968
+ __Block_byref_object_copy_.5369
+ __Block_byref_object_copy_.6633
+ __Block_byref_object_copy_.7175
+ __Block_byref_object_copy_.7884
+ __Block_byref_object_dispose_.10281
+ __Block_byref_object_dispose_.10655
+ __Block_byref_object_dispose_.10904
+ __Block_byref_object_dispose_.11202
+ __Block_byref_object_dispose_.11701
+ __Block_byref_object_dispose_.11781
+ __Block_byref_object_dispose_.12474
+ __Block_byref_object_dispose_.3083
+ __Block_byref_object_dispose_.4141
+ __Block_byref_object_dispose_.4334
+ __Block_byref_object_dispose_.4969
+ __Block_byref_object_dispose_.5370
+ __Block_byref_object_dispose_.6634
+ __Block_byref_object_dispose_.7176
+ __Block_byref_object_dispose_.7885
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8l
+ ___block_descriptor_61_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32s40b48r
+ ___copy_helper_block_e8_32s40s48b56r64w
+ ___copy_helper_block_e8_32s40s48s56b64r
+ ___destroy_helper_block_e8_32s40s48s56r64w
+ __block_literal_global.103
+ __block_literal_global.10318
+ __block_literal_global.10754
+ __block_literal_global.108
+ __block_literal_global.10993
+ __block_literal_global.11110
+ __block_literal_global.113
+ __block_literal_global.11454
+ __block_literal_global.11585
+ __block_literal_global.11723
+ __block_literal_global.11977
+ __block_literal_global.12049
+ __block_literal_global.12317
+ __block_literal_global.12500
+ __block_literal_global.146
+ __block_literal_global.148
+ __block_literal_global.150
+ __block_literal_global.153.6986
+ __block_literal_global.164.6983
+ __block_literal_global.167
+ __block_literal_global.169
+ __block_literal_global.171
+ __block_literal_global.174
+ __block_literal_global.189
+ __block_literal_global.232
+ __block_literal_global.240.6958
+ __block_literal_global.2522
+ __block_literal_global.2548
+ __block_literal_global.2585
+ __block_literal_global.2837
+ __block_literal_global.2994
+ __block_literal_global.3104
+ __block_literal_global.3350
+ __block_literal_global.3395
+ __block_literal_global.3617
+ __block_literal_global.38.7070
+ __block_literal_global.380
+ __block_literal_global.4168
+ __block_literal_global.4301
+ __block_literal_global.4351
+ __block_literal_global.4837
+ __block_literal_global.52
+ __block_literal_global.5574
+ __block_literal_global.5684
+ __block_literal_global.5887
+ __block_literal_global.5904
+ __block_literal_global.5992
+ __block_literal_global.6097
+ __block_literal_global.61
+ __block_literal_global.6133
+ __block_literal_global.63
+ __block_literal_global.6415
+ __block_literal_global.65
+ __block_literal_global.7091
+ __block_literal_global.73
+ __block_literal_global.7372
+ __block_literal_global.7484
+ __block_literal_global.7510
+ __block_literal_global.7656
+ __block_literal_global.7727
+ __block_literal_global.7916
+ __block_literal_global.8211
+ __block_literal_global.8392
+ __block_literal_global.8503
+ __block_literal_global.87
+ __block_literal_global.8774
+ __block_literal_global.9517
+ __block_literal_global.9611
+ __block_literal_global.9683
+ __block_literal_global.9794
+ __block_literal_global.98
+ __block_literal_global.9831
+ _objc_msgSend$initWithSampleRate:withNumberOfChannels:
+ _objc_msgSend$supportBeepCanceller:
+ sharedInstance._sharedInstance.11586
+ sharedInstance._sharedInstance.11978
+ sharedInstance._sharedInstance.12050
+ sharedInstance._sharedInstance.3618
+ sharedInstance._sharedInstance.4302
+ sharedInstance._sharedInstance.4838
+ sharedInstance._sharedInstance.5575
+ sharedInstance._sharedInstance.6098
+ sharedInstance._sharedInstance.6416
+ sharedInstance._sharedInstance.8775
+ sharedInstance._sharedInstance.9518
+ sharedInstance._sharedInstance.9832
+ sharedInstance.onceToken.10753
+ sharedInstance.onceToken.11584
+ sharedInstance.onceToken.11976
+ sharedInstance.onceToken.12048
+ sharedInstance.onceToken.12316
+ sharedInstance.onceToken.12499
+ sharedInstance.onceToken.3103
+ sharedInstance.onceToken.3394
+ sharedInstance.onceToken.3616
+ sharedInstance.onceToken.4167
+ sharedInstance.onceToken.4300
+ sharedInstance.onceToken.4350
+ sharedInstance.onceToken.4836
+ sharedInstance.onceToken.5573
+ sharedInstance.onceToken.5886
+ sharedInstance.onceToken.6096
+ sharedInstance.onceToken.6414
+ sharedInstance.onceToken.7371
+ sharedInstance.onceToken.7509
+ sharedInstance.onceToken.7726
+ sharedInstance.onceToken.8210
+ sharedInstance.onceToken.8391
+ sharedInstance.onceToken.8502
+ sharedInstance.onceToken.8773
+ sharedInstance.onceToken.9516
+ sharedInstance.onceToken.9610
+ sharedInstance.onceToken.9830
+ sharedInstance.sharedInstance.10755
+ sharedInstance.sharedInstance.12318
+ sharedInstance.sharedInstance.12501
+ sharedInstance.sharedInstance.3105
+ sharedInstance.sharedInstance.3396
+ sharedInstance.sharedInstance.4352
+ sharedInstance.sharedInstance.7373
+ sharedInstance.sharedInstance.7511
+ sharedInstance.sharedInstance.7728
+ sharedInstance.sharedInstance.8393
+ sharedInstance.sharedInstance.8504
+ sharedInstance.sharedInstance.9612
+ sharedInstance.sharedManager.5888
+ sharedLogger.onceToken.11109
+ sharedLogger.onceToken.2521
+ sharedLogger.onceToken.5683
+ sharedLogger.onceToken.5903
+ sharedLogger.shared.11111
+ sharedManager.onceToken.11722
+ sharedPreferences.onceToken.7483
- +[CSUtils supportBeepCanceller:recordType:]
- +[CSUtils(Directory) loggingFilePathWithDirectory:requestId:token:postfix:]
- -[CSAudioPreprocessor initWithSampleRate:withNumberOfChannels:recordType:]
- -[CSFAudioMetricsSelfLogger logMHAssistantDaemonAudioSessionActivationFailedWithInsufficientPriority:activeSessionDisplayIDs:audioSessionCategory:audioSessionMode:]
- -[CSFPreferences checkAOPConfigurationWatchDog]
- -[CSFPreferences clearAOPConfigurationWatchDog]
- -[CSFPreferences isSpeechStudyLoggingEnabled]
- -[CSFPreferences setAOPConfigurationWatchDog]
- AudioConverterFillComplexBuffer_BlockInvoke.6174
- GCC_except_table1222
- GCC_except_table1320
- GCC_except_table1495
- GCC_except_table1698
- GCC_except_table1702
- GCC_except_table1706
- GCC_except_table1710
- GCC_except_table1716
- GCC_except_table1722
- GCC_except_table1725
- GCC_except_table1773
- GCC_except_table1869
- GCC_except_table1872
- GCC_except_table1878
- GCC_except_table1887
- GCC_except_table1900
- GCC_except_table1943
- GCC_except_table2067
- GCC_except_table2104
- GCC_except_table2240
- GCC_except_table2244
- GCC_except_table2312
- GCC_except_table2325
- GCC_except_table2332
- GCC_except_table2347
- GCC_except_table2356
- GCC_except_table2374
- GCC_except_table2395
- GCC_except_table2494
- GCC_except_table2495
- GCC_except_table2627
- GCC_except_table2746
- GCC_except_table2756
- GCC_except_table2765
- GCC_except_table2768
- GCC_except_table2770
- GCC_except_table2771
- GCC_except_table2775
- GCC_except_table2795
- GCC_except_table2836
- GCC_except_table2937
- GCC_except_table2969
- GCC_except_table2970
- GCC_except_table2971
- GCC_except_table2972
- GCC_except_table2994
- GCC_except_table3153
- GCC_except_table3213
- GCC_except_table3227
- GCC_except_table3259
- GCC_except_table3261
- GCC_except_table3264
- GCC_except_table3265
- GCC_except_table3266
- GCC_except_table3307
- GCC_except_table3308
- GCC_except_table3309
- GCC_except_table3310
- GCC_except_table3311
- GCC_except_table3402
- GCC_except_table3408
- GCC_except_table3470
- GCC_except_table3471
- GCC_except_table3472
- GCC_except_table3473
- GCC_except_table3475
- GCC_except_table3476
- GCC_except_table3488
- GCC_except_table3489
- GCC_except_table3491
- GCC_except_table3493
- GCC_except_table3495
- GCC_except_table3502
- GCC_except_table3504
- GCC_except_table3508
- GCC_except_table3509
- GCC_except_table3539
- GCC_except_table3543
- GCC_except_table3650
- GCC_except_table3692
- GCC_except_table3750
- GCC_except_table3819
- GCC_except_table3836
- GCC_except_table3935
- GCC_except_table958
- GCC_except_table965
- _CFPreferencesAppValueIsForced
- _CFPreferencesGetAppBooleanValue
- _OBJC_CLASS_$_MHSchemaMHAssistantDaemonAudioRecordingFailureInsufficientPriority
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.169
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.170
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.125
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.130
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.135
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.139
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.131
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.136
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.137
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.118
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.122
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.108
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.112
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.110
- __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.175
- __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.117
- __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.157
- __88-[CSVoiceTriggerAlwaysOnProcessor disableVoiceTriggerOnAlwaysOnProcessorWithCompletion:]_block_invoke.20
- __93-[CSVoiceTriggerAlwaysOnProcessor enableVoiceTriggerOnAlwaysOnProcessorWithAsset:completion:]_block_invoke.16
- __93-[CSVoiceTriggerAlwaysOnProcessor enableVoiceTriggerOnAlwaysOnProcessorWithAsset:completion:]_block_invoke.18
- __Block_byref_object_copy_.10286
- __Block_byref_object_copy_.10660
- __Block_byref_object_copy_.10909
- __Block_byref_object_copy_.11209
- __Block_byref_object_copy_.11712
- __Block_byref_object_copy_.11792
- __Block_byref_object_copy_.12485
- __Block_byref_object_copy_.3087
- __Block_byref_object_copy_.4150
- __Block_byref_object_copy_.4344
- __Block_byref_object_copy_.4976
- __Block_byref_object_copy_.5374
- __Block_byref_object_copy_.6637
- __Block_byref_object_copy_.7179
- __Block_byref_object_copy_.7890
- __Block_byref_object_dispose_.10287
- __Block_byref_object_dispose_.10661
- __Block_byref_object_dispose_.10910
- __Block_byref_object_dispose_.11210
- __Block_byref_object_dispose_.11713
- __Block_byref_object_dispose_.11793
- __Block_byref_object_dispose_.12486
- __Block_byref_object_dispose_.3088
- __Block_byref_object_dispose_.4151
- __Block_byref_object_dispose_.4345
- __Block_byref_object_dispose_.4977
- __Block_byref_object_dispose_.5375
- __Block_byref_object_dispose_.6638
- __Block_byref_object_dispose_.7180
- __Block_byref_object_dispose_.7891
- ___45-[CSFPreferences isSpeechStudyLoggingEnabled]_block_invoke
- ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8l
- ___block_descriptor_69_e8_32s40s48s56s_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56bs64r72w_e17_v16?0"NSError"8l
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e17_v16?0"NSError"8l
- ___copy_helper_block_e8_32s40s48b56r
- ___copy_helper_block_e8_32s40s48s56b64r72w
- ___copy_helper_block_e8_32s40s48s56s64b72r
- ___destroy_helper_block_e8_32s40s48s56s64r72w
- __block_literal_global.10324
- __block_literal_global.104
- __block_literal_global.10760
- __block_literal_global.109
- __block_literal_global.10999
- __block_literal_global.11117
- __block_literal_global.114
- __block_literal_global.11466
- __block_literal_global.11597
- __block_literal_global.11735
- __block_literal_global.119
- __block_literal_global.11989
- __block_literal_global.12061
- __block_literal_global.12329
- __block_literal_global.12512
- __block_literal_global.152
- __block_literal_global.154
- __block_literal_global.156
- __block_literal_global.165
- __block_literal_global.170
- __block_literal_global.173
- __block_literal_global.175
- __block_literal_global.177
- __block_literal_global.180
- __block_literal_global.195
- __block_literal_global.244
- __block_literal_global.246
- __block_literal_global.2532
- __block_literal_global.2558
- __block_literal_global.2595
- __block_literal_global.2844
- __block_literal_global.2999
- __block_literal_global.3109
- __block_literal_global.3356
- __block_literal_global.3401
- __block_literal_global.3623
- __block_literal_global.38.7074
- __block_literal_global.387
- __block_literal_global.4178
- __block_literal_global.4312
- __block_literal_global.4362
- __block_literal_global.4845
- __block_literal_global.514
- __block_literal_global.5582
- __block_literal_global.5692
- __block_literal_global.58
- __block_literal_global.5894
- __block_literal_global.5911
- __block_literal_global.5999
- __block_literal_global.6104
- __block_literal_global.6140
- __block_literal_global.6424
- __block_literal_global.67.6367
- __block_literal_global.7095
- __block_literal_global.7376
- __block_literal_global.7488
- __block_literal_global.75
- __block_literal_global.7514
- __block_literal_global.7661
- __block_literal_global.77
- __block_literal_global.7731
- __block_literal_global.79
- __block_literal_global.7923
- __block_literal_global.8221
- __block_literal_global.8402
- __block_literal_global.8513
- __block_literal_global.8781
- __block_literal_global.93
- __block_literal_global.9524
- __block_literal_global.9618
- __block_literal_global.9690
- __block_literal_global.9801
- __block_literal_global.9838
- _objc_msgSend$clearAOPConfigurationWatchDog
- _objc_msgSend$initWithSampleRate:withNumberOfChannels:recordType:
- _objc_msgSend$setAOPConfigurationWatchDog
- _objc_msgSend$setAssistantDaemonAudioRecordingFailureInsufficientPriority:
- _objc_msgSend$supportBeepCanceller:recordType:
- isSpeechStudyLoggingEnabled.enabled
- isSpeechStudyLoggingEnabled.onceToken
- sharedInstance._sharedInstance.11598
- sharedInstance._sharedInstance.11990
- sharedInstance._sharedInstance.12062
- sharedInstance._sharedInstance.3624
- sharedInstance._sharedInstance.4313
- sharedInstance._sharedInstance.4846
- sharedInstance._sharedInstance.5583
- sharedInstance._sharedInstance.6105
- sharedInstance._sharedInstance.6425
- sharedInstance._sharedInstance.8782
- sharedInstance._sharedInstance.9525
- sharedInstance._sharedInstance.9839
- sharedInstance.onceToken.10759
- sharedInstance.onceToken.11596
- sharedInstance.onceToken.11988
- sharedInstance.onceToken.12060
- sharedInstance.onceToken.12328
- sharedInstance.onceToken.12511
- sharedInstance.onceToken.3108
- sharedInstance.onceToken.3400
- sharedInstance.onceToken.3622
- sharedInstance.onceToken.4177
- sharedInstance.onceToken.4311
- sharedInstance.onceToken.4361
- sharedInstance.onceToken.4844
- sharedInstance.onceToken.5581
- sharedInstance.onceToken.5893
- sharedInstance.onceToken.6103
- sharedInstance.onceToken.6423
- sharedInstance.onceToken.7375
- sharedInstance.onceToken.7513
- sharedInstance.onceToken.7730
- sharedInstance.onceToken.8220
- sharedInstance.onceToken.8401
- sharedInstance.onceToken.8512
- sharedInstance.onceToken.8780
- sharedInstance.onceToken.9523
- sharedInstance.onceToken.9617
- sharedInstance.onceToken.9837
- sharedInstance.sharedInstance.10761
- sharedInstance.sharedInstance.12330
- sharedInstance.sharedInstance.12513
- sharedInstance.sharedInstance.3110
- sharedInstance.sharedInstance.3402
- sharedInstance.sharedInstance.4363
- sharedInstance.sharedInstance.7377
- sharedInstance.sharedInstance.7515
- sharedInstance.sharedInstance.7732
- sharedInstance.sharedInstance.8403
- sharedInstance.sharedInstance.8514
- sharedInstance.sharedInstance.9619
- sharedInstance.sharedManager.5895
- sharedLogger.onceToken.11116
- sharedLogger.onceToken.2531
- sharedLogger.onceToken.5691
- sharedLogger.onceToken.5910
- sharedLogger.shared.11118
- sharedManager.onceToken.11734
- sharedPreferences.onceToken.7487
CStrings:
- "+[CSUtils(Directory) loggingFilePathWithDirectory:requestId:token:postfix:]"
- "-[CSFPreferences isSpeechStudyLoggingEnabled]"
- "AOP Configuration Transaction"
- "AOPConfigurationWatchDog"
- "Profanity Allowed"
- "SpeechStudy Logging Enabled"
- "com.apple.ironwood.support"

```
