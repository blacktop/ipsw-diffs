## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-  __TEXT.__text: 0xcab8c
-  __TEXT.__objc_methlist: 0xd6e8
-  __TEXT.__const: 0xfb8
+  __TEXT.__text: 0xcbb14
+  __TEXT.__objc_methlist: 0xd808
+  __TEXT.__const: 0xfc8
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x165b7
+  __TEXT.__cstring: 0x1671a
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x244
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3c24
-  __TEXT.__oslogstring: 0x1149f
-  __TEXT.__unwind_info: 0x3bc0
+  __TEXT.__gcc_except_tab: 0x3cec
+  __TEXT.__oslogstring: 0x11931
+  __TEXT.__unwind_info: 0x3c00
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2810
-  __DATA_CONST.__objc_classlist: 0x730
+  __DATA_CONST.__const: 0x2840
+  __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x210
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7398
+  __DATA_CONST.__objc_selrefs: 0x7440
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x1030
-  __AUTH_CONST.__const: 0x1ac0
-  __AUTH_CONST.__cfstring: 0x9500
-  __AUTH_CONST.__objc_const: 0x149d8
+  __DATA_CONST.__got: 0x1038
+  __AUTH_CONST.__const: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x9580
+  __AUTH_CONST.__objc_const: 0x14b70
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x4b0

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xfc0
-  __AUTH.__objc_data: 0x1938
-  __DATA.__objc_ivar: 0xd80
-  __DATA.__data: 0x1948
-  __DATA.__bss: 0x1638
-  __DATA_DIRTY.__objc_data: 0x2f60
-  __DATA_DIRTY.__data: 0x2e0
-  __DATA_DIRTY.__bss: 0x540
+  __AUTH.__objc_data: 0x128
+  __DATA.__objc_ivar: 0xd8c
+  __DATA.__data: 0x19a0
+  __DATA.__bss: 0x1568
+  __DATA_DIRTY.__objc_data: 0x47c0
+  __DATA_DIRTY.__data: 0x2e8
+  __DATA_DIRTY.__bss: 0x618
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5198
-  Symbols:   17352
-  CStrings:  4909
+  Functions: 5222
+  Symbols:   17443
+  CStrings:  4936
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
Symbols:
+ +[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]
+ +[CSPhraseSpotterEnabledMonitor sharedInstance]
+ -[CSAudioPowerProvider _minimumIOBufferDurationForInputSampleRate:]
+ -[CSAudioPowerProvider _startStandardPath]
+ -[CSAudioPowerProvider configureForRecordRoute:preferUseSelfTap:]
+ -[CSAudioRecorder _decoderForAudioStreamHandleId:]
+ -[CSAudioRecorder _removeDecoderForAudioStreamHandleId:]
+ -[CSAudioRecorder opusDecoders]
+ -[CSAudioRecorder setOpusDecoders:]
+ -[CSAudioStopStreamOption blockAttending]
+ -[CSAudioStopStreamOption initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:blockAttending:]
+ -[CSAudioStopStreamOption initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:blockAttending:]
+ -[CSFPreferences selfTapIOBufferDurationOverride]
+ -[CSMicUsageReporter reportMicUsage:deviceUID:]
+ -[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]
+ -[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]
+ -[CSPhraseSpotterEnabledMonitor _notifyObserver:withEnabled:]
+ -[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]
+ -[CSPhraseSpotterEnabledMonitor _startMonitoringWithQueue:]
+ -[CSPhraseSpotterEnabledMonitor _stopMonitoring]
+ -[CSPhraseSpotterEnabledMonitor init]
+ -[CSPhraseSpotterEnabledMonitor isEnabled]
+ GCC_except_table1325
+ GCC_except_table1354
+ GCC_except_table1440
+ GCC_except_table1441
+ GCC_except_table1442
+ GCC_except_table1443
+ GCC_except_table1444
+ GCC_except_table1451
+ GCC_except_table1454
+ GCC_except_table1460
+ GCC_except_table1466
+ GCC_except_table1467
+ GCC_except_table1468
+ GCC_except_table1470
+ GCC_except_table1474
+ GCC_except_table1486
+ GCC_except_table1880
+ GCC_except_table1881
+ GCC_except_table1882
+ GCC_except_table1884
+ GCC_except_table1888
+ GCC_except_table1891
+ GCC_except_table1892
+ GCC_except_table1894
+ GCC_except_table1900
+ GCC_except_table1907
+ GCC_except_table1909
+ GCC_except_table1910
+ GCC_except_table1925
+ GCC_except_table1931
+ GCC_except_table2024
+ GCC_except_table2082
+ GCC_except_table2092
+ GCC_except_table2134
+ GCC_except_table2135
+ GCC_except_table2137
+ GCC_except_table2138
+ GCC_except_table2144
+ GCC_except_table2155
+ GCC_except_table2162
+ GCC_except_table2205
+ GCC_except_table2223
+ GCC_except_table2302
+ GCC_except_table2412
+ GCC_except_table2447
+ GCC_except_table2603
+ GCC_except_table2607
+ GCC_except_table2686
+ GCC_except_table2697
+ GCC_except_table2699
+ GCC_except_table2704
+ GCC_except_table2706
+ GCC_except_table2719
+ GCC_except_table2726
+ GCC_except_table2728
+ GCC_except_table2746
+ GCC_except_table2767
+ GCC_except_table2805
+ GCC_except_table2862
+ GCC_except_table2864
+ GCC_except_table2865
+ GCC_except_table3028
+ GCC_except_table3168
+ GCC_except_table3184
+ GCC_except_table3194
+ GCC_except_table3198
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3237
+ GCC_except_table3243
+ GCC_except_table3304
+ GCC_except_table3308
+ GCC_except_table3363
+ GCC_except_table3375
+ GCC_except_table3379
+ GCC_except_table3386
+ GCC_except_table3395
+ GCC_except_table3418
+ GCC_except_table3419
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3446
+ GCC_except_table3459
+ GCC_except_table3618
+ GCC_except_table3678
+ GCC_except_table3692
+ GCC_except_table3734
+ GCC_except_table3735
+ GCC_except_table3764
+ GCC_except_table3765
+ GCC_except_table3767
+ GCC_except_table3770
+ GCC_except_table3771
+ GCC_except_table3772
+ GCC_except_table3795
+ GCC_except_table3797
+ GCC_except_table3801
+ GCC_except_table3802
+ GCC_except_table3803
+ GCC_except_table3806
+ GCC_except_table3831
+ GCC_except_table3857
+ GCC_except_table3878
+ GCC_except_table3898
+ GCC_except_table3899
+ GCC_except_table3900
+ GCC_except_table3901
+ GCC_except_table3911
+ GCC_except_table4015
+ GCC_except_table4016
+ GCC_except_table4020
+ GCC_except_table4021
+ GCC_except_table4026
+ GCC_except_table4028
+ GCC_except_table4031
+ GCC_except_table4035
+ GCC_except_table4043
+ GCC_except_table4047
+ GCC_except_table4050
+ GCC_except_table4055
+ GCC_except_table4058
+ GCC_except_table4059
+ GCC_except_table4060
+ GCC_except_table4062
+ GCC_except_table4063
+ GCC_except_table4064
+ GCC_except_table4066
+ GCC_except_table4067
+ GCC_except_table4069
+ GCC_except_table4070
+ GCC_except_table4071
+ GCC_except_table4072
+ GCC_except_table4100
+ GCC_except_table4150
+ GCC_except_table4154
+ GCC_except_table4204
+ GCC_except_table4205
+ GCC_except_table4212
+ GCC_except_table4213
+ GCC_except_table4214
+ GCC_except_table4215
+ GCC_except_table4217
+ GCC_except_table4239
+ GCC_except_table4241
+ GCC_except_table4242
+ GCC_except_table4245
+ GCC_except_table4246
+ GCC_except_table4247
+ GCC_except_table4248
+ GCC_except_table4249
+ GCC_except_table4250
+ GCC_except_table4251
+ GCC_except_table4275
+ GCC_except_table4277
+ GCC_except_table4279
+ GCC_except_table4281
+ GCC_except_table4283
+ GCC_except_table4285
+ GCC_except_table4286
+ GCC_except_table4287
+ GCC_except_table4288
+ GCC_except_table4290
+ GCC_except_table4292
+ GCC_except_table4294
+ GCC_except_table4295
+ GCC_except_table4297
+ GCC_except_table4299
+ GCC_except_table4301
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4329
+ GCC_except_table4331
+ GCC_except_table4332
+ GCC_except_table4333
+ GCC_except_table4338
+ GCC_except_table4340
+ GCC_except_table4344
+ GCC_except_table4345
+ GCC_except_table4375
+ GCC_except_table4487
+ GCC_except_table4494
+ GCC_except_table4577
+ GCC_except_table4644
+ GCC_except_table4654
+ GCC_except_table4710
+ GCC_except_table4711
+ GCC_except_table4712
+ GCC_except_table4714
+ GCC_except_table4715
+ GCC_except_table4716
+ GCC_except_table4717
+ GCC_except_table4718
+ GCC_except_table4719
+ GCC_except_table4722
+ GCC_except_table4724
+ GCC_except_table4726
+ GCC_except_table4727
+ GCC_except_table4765
+ GCC_except_table4831
+ GCC_except_table4836
+ GCC_except_table4877
+ GCC_except_table4943
+ GCC_except_table826
+ GCC_except_table833
+ GCC_except_table896
+ GCC_except_table897
+ GCC_except_table904
+ GCC_except_table919
+ GCC_except_table920
+ GCC_except_table926
+ GCC_except_table931
+ GCC_except_table940
+ GCC_except_table941
+ GCC_except_table942
+ GCC_except_table956
+ _OBJC_CLASS_$_CSPhraseSpotterEnabledMonitor
+ _OBJC_IVAR_$_CSAudioStopStreamOption._blockAttending
+ _OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._isPhraseSpotterEnabled
+ _OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._notifyToken
+ _OBJC_METACLASS_$_CSPhraseSpotterEnabledMonitor
+ __OBJC_$_CLASS_METHODS_CSPhraseSpotterEnabledMonitor
+ __OBJC_$_INSTANCE_METHODS_CSPhraseSpotterEnabledMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CSPhraseSpotterEnabledMonitor
+ __OBJC_$_PROP_LIST_CSPhraseSpotterEnabledMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhraseSpotterEnabledMonitorProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhraseSpotterEnabledMonitorProviding
+ __OBJC_$_PROTOCOL_REFS_CSPhraseSpotterEnabledMonitorProviding
+ __OBJC_CLASS_PROTOCOLS_$_CSPhraseSpotterEnabledMonitor
+ __OBJC_CLASS_RO_$_CSPhraseSpotterEnabledMonitor
+ __OBJC_LABEL_PROTOCOL_$_CSPhraseSpotterEnabledMonitorProviding
+ __OBJC_METACLASS_RO_$_CSPhraseSpotterEnabledMonitor
+ __OBJC_PROTOCOL_$_CSPhraseSpotterEnabledMonitorProviding
+ __PhraseSpotterEnabledDidChange
+ ___47+[CSPhraseSpotterEnabledMonitor sharedInstance]_block_invoke
+ ___79-[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]_block_invoke
+ ___83+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]_block_invoke
+ ___block_descriptor_64_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ _kCSPhraseSpotterEnabledDidChangeDarwinNotification
+ _objc_msgSend$CSPhraseSpotterEnabledMonitor:didReceiveEnabled:
+ _objc_msgSend$IOBufferDuration
+ _objc_msgSend$_checkPhraseSpotterEnabled
+ _objc_msgSend$_decoderForAudioStreamHandleId:
+ _objc_msgSend$_didReceivePhraseSpotterSettingChangedInQueue:
+ _objc_msgSend$_minimumIOBufferDurationForInputSampleRate:
+ _objc_msgSend$_phraseSpotterEnabledDidChange
+ _objc_msgSend$_removeDecoderForAudioStreamHandleId:
+ _objc_msgSend$_startStandardPath
+ _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:blockAttending:
+ _objc_msgSend$isBuiltInRecordRoute:
+ _objc_msgSend$opusDecoders
+ _objc_msgSend$phraseSpotterEnabled
+ _objc_msgSend$recordedAudioAvailableAt:requestId:filenamePostfix:completion:
+ _objc_msgSend$reportMicUsage:deviceUID:
+ _objc_msgSend$selfTapIOBufferDurationOverride
+ _objc_msgSend$setActive:error:
+ _objc_msgSend$setOpusDecoders:
+ _objc_msgSend$setPreferredIOBufferDuration:error:
+ _objc_msgSend$setPreferredInputSampleRate:error:
+ _objc_msgSend$setPrefersLowPowerMicrophone:error:
- -[CSAudioPowerProvider configureForRecordRoute:]
- GCC_except_table1320
- GCC_except_table1349
- GCC_except_table1427
- GCC_except_table1431
- GCC_except_table1433
- GCC_except_table1434
- GCC_except_table1435
- GCC_except_table1446
- GCC_except_table1449
- GCC_except_table1450
- GCC_except_table1457
- GCC_except_table1458
- GCC_except_table1461
- GCC_except_table1465
- GCC_except_table1469
- GCC_except_table1481
- GCC_except_table1875
- GCC_except_table1876
- GCC_except_table1877
- GCC_except_table1878
- GCC_except_table1879
- GCC_except_table1886
- GCC_except_table1887
- GCC_except_table1889
- GCC_except_table1895
- GCC_except_table1902
- GCC_except_table1904
- GCC_except_table1905
- GCC_except_table1920
- GCC_except_table1926
- GCC_except_table2014
- GCC_except_table2077
- GCC_except_table2087
- GCC_except_table2129
- GCC_except_table2130
- GCC_except_table2132
- GCC_except_table2133
- GCC_except_table2139
- GCC_except_table2150
- GCC_except_table2157
- GCC_except_table2200
- GCC_except_table2218
- GCC_except_table2297
- GCC_except_table2407
- GCC_except_table2442
- GCC_except_table2586
- GCC_except_table2590
- GCC_except_table2669
- GCC_except_table2680
- GCC_except_table2682
- GCC_except_table2687
- GCC_except_table2689
- GCC_except_table2702
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2729
- GCC_except_table2750
- GCC_except_table2788
- GCC_except_table2845
- GCC_except_table2847
- GCC_except_table2848
- GCC_except_table3010
- GCC_except_table3150
- GCC_except_table3158
- GCC_except_table3166
- GCC_except_table3180
- GCC_except_table3182
- GCC_except_table3183
- GCC_except_table3219
- GCC_except_table3225
- GCC_except_table3286
- GCC_except_table3290
- GCC_except_table3345
- GCC_except_table3357
- GCC_except_table3361
- GCC_except_table3368
- GCC_except_table3377
- GCC_except_table3400
- GCC_except_table3401
- GCC_except_table3402
- GCC_except_table3403
- GCC_except_table3428
- GCC_except_table3441
- GCC_except_table3600
- GCC_except_table3660
- GCC_except_table3674
- GCC_except_table3716
- GCC_except_table3717
- GCC_except_table3746
- GCC_except_table3747
- GCC_except_table3749
- GCC_except_table3752
- GCC_except_table3753
- GCC_except_table3754
- GCC_except_table3777
- GCC_except_table3779
- GCC_except_table3783
- GCC_except_table3784
- GCC_except_table3785
- GCC_except_table3788
- GCC_except_table3813
- GCC_except_table3839
- GCC_except_table3860
- GCC_except_table3880
- GCC_except_table3881
- GCC_except_table3882
- GCC_except_table3883
- GCC_except_table3893
- GCC_except_table3984
- GCC_except_table3985
- GCC_except_table3994
- GCC_except_table3996
- GCC_except_table3997
- GCC_except_table3998
- GCC_except_table3999
- GCC_except_table4006
- GCC_except_table4007
- GCC_except_table4008
- GCC_except_table4009
- GCC_except_table4010
- GCC_except_table4011
- GCC_except_table4013
- GCC_except_table4018
- GCC_except_table4033
- GCC_except_table4037
- GCC_except_table4040
- GCC_except_table4041
- GCC_except_table4044
- GCC_except_table4046
- GCC_except_table4049
- GCC_except_table4052
- GCC_except_table4053
- GCC_except_table4081
- GCC_except_table4129
- GCC_except_table4133
- GCC_except_table4183
- GCC_except_table4184
- GCC_except_table4191
- GCC_except_table4192
- GCC_except_table4193
- GCC_except_table4194
- GCC_except_table4196
- GCC_except_table4197
- GCC_except_table4220
- GCC_except_table4221
- GCC_except_table4222
- GCC_except_table4224
- GCC_except_table4225
- GCC_except_table4226
- GCC_except_table4227
- GCC_except_table4228
- GCC_except_table4229
- GCC_except_table4230
- GCC_except_table4231
- GCC_except_table4254
- GCC_except_table4255
- GCC_except_table4256
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table4259
- GCC_except_table4260
- GCC_except_table4262
- GCC_except_table4265
- GCC_except_table4266
- GCC_except_table4267
- GCC_except_table4268
- GCC_except_table4269
- GCC_except_table4271
- GCC_except_table4274
- GCC_except_table4282
- GCC_except_table4302
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4308
- GCC_except_table4311
- GCC_except_table4312
- GCC_except_table4317
- GCC_except_table4319
- GCC_except_table4354
- GCC_except_table4466
- GCC_except_table4473
- GCC_except_table4555
- GCC_except_table4622
- GCC_except_table4632
- GCC_except_table4688
- GCC_except_table4689
- GCC_except_table4690
- GCC_except_table4692
- GCC_except_table4693
- GCC_except_table4694
- GCC_except_table4695
- GCC_except_table4696
- GCC_except_table4697
- GCC_except_table4699
- GCC_except_table4701
- GCC_except_table4702
- GCC_except_table4703
- GCC_except_table4741
- GCC_except_table4807
- GCC_except_table4812
- GCC_except_table4853
- GCC_except_table4919
- GCC_except_table822
- GCC_except_table829
- GCC_except_table892
- GCC_except_table893
- GCC_except_table900
- GCC_except_table915
- GCC_except_table916
- GCC_except_table917
- GCC_except_table922
- GCC_except_table923
- GCC_except_table924
- GCC_except_table934
- GCC_except_table952
- ___72+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:]_block_invoke
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
CStrings:
+ " (from override)"
+ "%s Failed to activate audio session: %{public}@. Low latency Siri waveform animation will not function."
+ "%s Failed to bump IOBufferDuration to %.3fms: %{public}@"
+ "%s Failed to configure audio engine, Low latency Siri waveform animation will not function : %{public}@"
+ "%s Failed to create CSAudioDecoder for stream %{public}lu"
+ "%s Failed to get valid inputFormat from audio engine, Low latency Siri waveform animation will not function"
+ "%s Failed to set audio session category: %{public}@. Low latency Siri waveform animation will not function."
+ "%s Failed to set preferredIOBufferDuration=%.3fms: %{public}@"
+ "%s Failed to set preferredInputSampleRate=%.0f: %{public}@"
+ "%s Failed to set prefersLowPowerMicrophone: %{public}@. Siri waveform animation may not function correctly."
+ "%s Hardware sampleRate=%.0fHz; current IOBufferDuration=%.3fms below spectral minimum %.3fms — bumping."
+ "%s No Opus decoder available for stream %{public}lu, dropping packet"
+ "%s PhraseSpotter enabled = %{public}@"
+ "%s PhraseSpotter is already %{public}@, received duplicated notification!"
+ "%s Set preferredIOBufferDuration=%.3fms%{public}s"
+ "%s preferredIOBufferDuration=%.3fms is below spectral minimum %.3fms (windowSize=%lu @ %.0fHz analysis rate) — spectrum may not produce output."
+ "%s starting of self tap has failed, Siri waveform animation will falling back to standard power meter path"
+ "+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]_block_invoke"
+ ", blockAttending:%d"
+ "-[CSAudioPowerProvider configureForRecordRoute:preferUseSelfTap:]"
+ "-[CSAudioRecorder _decoderForAudioStreamHandleId:]"
+ "-[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]"
+ "-[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]"
+ "blockAttending"
+ "dictation"
+ "kVTPreferencesPhraseSpotterEnabledDidChangeDarwinNotification"
+ "override_iobuffer_duration"
+ "\xf0!"
- "%s Failed to activate audio session: %{public}@. Siri waveform animation will not function."
- "%s Failed to set audio session category: %{public}@. Siri waveform animation will not function."
- "+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:]_block_invoke"
- "-[CSAudioPowerProvider configureForRecordRoute:]"
- "\xf01"

```
