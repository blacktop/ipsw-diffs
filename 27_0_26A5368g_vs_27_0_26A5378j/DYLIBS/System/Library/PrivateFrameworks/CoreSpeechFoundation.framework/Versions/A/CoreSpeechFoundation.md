## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-  __TEXT.__text: 0xc7398
-  __TEXT.__objc_methlist: 0xd470
+  __TEXT.__text: 0xc8cd4
+  __TEXT.__objc_methlist: 0xd5b8
   __TEXT.__const: 0xb18
   __TEXT.__dlopen_cstrs: 0x18c
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_typeref: 0x19d
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x1545b
+  __TEXT.__cstring: 0x1576d
   __TEXT.__swift5_reflstr: 0x174
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_fieldmd: 0x174
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3b10
-  __TEXT.__oslogstring: 0xfd92
-  __TEXT.__unwind_info: 0x3940
+  __TEXT.__gcc_except_tab: 0x3c08
+  __TEXT.__oslogstring: 0x10172
+  __TEXT.__unwind_info: 0x39b0
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf68
-  __DATA_CONST.__objc_classlist: 0x748
+  __DATA_CONST.__const: 0xf90
+  __DATA_CONST.__objc_classlist: 0x750
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x70a8
+  __DATA_CONST.__objc_selrefs: 0x7190
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x548
+  __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x1e0
-  __DATA_CONST.__got: 0xc40
-  __AUTH_CONST.__const: 0x39b0
-  __AUTH_CONST.__cfstring: 0x91e0
-  __AUTH_CONST.__objc_const: 0x14830
+  __DATA_CONST.__got: 0xc58
+  __AUTH_CONST.__const: 0x3a30
+  __AUTH_CONST.__cfstring: 0x9280
+  __AUTH_CONST.__objc_const: 0x14a38
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xec8
-  __AUTH.__objc_data: 0x1938
+  __AUTH.__objc_data: 0x1c8
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xd64
-  __DATA.__data: 0x17f0
-  __DATA.__bss: 0xa40
-  __DATA_DIRTY.__objc_data: 0x3050
-  __DATA_DIRTY.__data: 0x308
-  __DATA_DIRTY.__bss: 0x558
+  __DATA.__objc_ivar: 0xd7c
+  __DATA.__data: 0x1848
+  __DATA.__bss: 0x9a0
+  __DATA_DIRTY.__objc_data: 0x4810
+  __DATA_DIRTY.__data: 0x310
+  __DATA_DIRTY.__bss: 0x610
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5171
-  Symbols:   12288
-  CStrings:  4699
+  Functions: 5204
+  Symbols:   12380
+  CStrings:  4736
 
Sections:
~ __TEXT.__const : content changed
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
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]
+ +[CSPhraseSpotterEnabledMonitor sharedInstance]
+ -[CSAudioPowerProvider _minimumIOBufferDurationForInputSampleRate:]
+ -[CSAudioPowerProvider _startStandardPath]
+ -[CSAudioPowerProvider configureForRecordRoute:preferUseSelfTap:]
+ -[CSAudioProvider _currentHALDeviceUID]
+ -[CSAudioRecorder _decoderForAudioStreamHandleId:]
+ -[CSAudioRecorder _removeDecoderForAudioStreamHandleId:]
+ -[CSAudioRecorder opusDecoders]
+ -[CSAudioRecorder setOpusDecoders:]
+ -[CSAudioStopStreamOption blockAttending]
+ -[CSAudioStopStreamOption initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:blockAttending:]
+ -[CSAudioStopStreamOption initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:blockAttending:]
+ -[CSFPreferences selfTapIOBufferDurationOverride]
+ -[CSMicUsageReporter lastReportedDeviceUID]
+ -[CSMicUsageReporter micCurrentlyReported]
+ -[CSMicUsageReporter reportMicUsage:deviceUID:]
+ -[CSMicUsageReporter setLastReportedDeviceUID:]
+ -[CSMicUsageReporter setMicCurrentlyReported:]
+ -[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]
+ -[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]
+ -[CSPhraseSpotterEnabledMonitor _notifyObserver:withEnabled:]
+ -[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]
+ -[CSPhraseSpotterEnabledMonitor _startMonitoringWithQueue:]
+ -[CSPhraseSpotterEnabledMonitor _stopMonitoring]
+ -[CSPhraseSpotterEnabledMonitor init]
+ -[CSPhraseSpotterEnabledMonitor isEnabled]
+ GCC_except_table1008
+ GCC_except_table1009
+ GCC_except_table1010
+ GCC_except_table1024
+ GCC_except_table1094
+ GCC_except_table1096
+ GCC_except_table1097
+ GCC_except_table1107
+ GCC_except_table1414
+ GCC_except_table1443
+ GCC_except_table1525
+ GCC_except_table1526
+ GCC_except_table1527
+ GCC_except_table1529
+ GCC_except_table1530
+ GCC_except_table1533
+ GCC_except_table1549
+ GCC_except_table1552
+ GCC_except_table1555
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1559
+ GCC_except_table1563
+ GCC_except_table1740
+ GCC_except_table1953
+ GCC_except_table1955
+ GCC_except_table1956
+ GCC_except_table1963
+ GCC_except_table1964
+ GCC_except_table1972
+ GCC_except_table1978
+ GCC_except_table1980
+ GCC_except_table1981
+ GCC_except_table2047
+ GCC_except_table2052
+ GCC_except_table2110
+ GCC_except_table2161
+ GCC_except_table2162
+ GCC_except_table2164
+ GCC_except_table2165
+ GCC_except_table2171
+ GCC_except_table2182
+ GCC_except_table2195
+ GCC_except_table2238
+ GCC_except_table2256
+ GCC_except_table2335
+ GCC_except_table2433
+ GCC_except_table2470
+ GCC_except_table2626
+ GCC_except_table2630
+ GCC_except_table2706
+ GCC_except_table2719
+ GCC_except_table2741
+ GCC_except_table2748
+ GCC_except_table2750
+ GCC_except_table2768
+ GCC_except_table2789
+ GCC_except_table2830
+ GCC_except_table2892
+ GCC_except_table2894
+ GCC_except_table2895
+ GCC_except_table3059
+ GCC_except_table3198
+ GCC_except_table3206
+ GCC_except_table3216
+ GCC_except_table3225
+ GCC_except_table3228
+ GCC_except_table3230
+ GCC_except_table3231
+ GCC_except_table3270
+ GCC_except_table3276
+ GCC_except_table3323
+ GCC_except_table3416
+ GCC_except_table3428
+ GCC_except_table3434
+ GCC_except_table3441
+ GCC_except_table3474
+ GCC_except_table3475
+ GCC_except_table3477
+ GCC_except_table3502
+ GCC_except_table3515
+ GCC_except_table3675
+ GCC_except_table3735
+ GCC_except_table3749
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3825
+ GCC_except_table3826
+ GCC_except_table3828
+ GCC_except_table3831
+ GCC_except_table3832
+ GCC_except_table3853
+ GCC_except_table3855
+ GCC_except_table3859
+ GCC_except_table3860
+ GCC_except_table3864
+ GCC_except_table3913
+ GCC_except_table3934
+ GCC_except_table3955
+ GCC_except_table3956
+ GCC_except_table3957
+ GCC_except_table3958
+ GCC_except_table4057
+ GCC_except_table4060
+ GCC_except_table4061
+ GCC_except_table4062
+ GCC_except_table4069
+ GCC_except_table4072
+ GCC_except_table4075
+ GCC_except_table4078
+ GCC_except_table4079
+ GCC_except_table4085
+ GCC_except_table4091
+ GCC_except_table4103
+ GCC_except_table4108
+ GCC_except_table4109
+ GCC_except_table4112
+ GCC_except_table4114
+ GCC_except_table4115
+ GCC_except_table4118
+ GCC_except_table4119
+ GCC_except_table4120
+ GCC_except_table4122
+ GCC_except_table4123
+ GCC_except_table4125
+ GCC_except_table4126
+ GCC_except_table4127
+ GCC_except_table4128
+ GCC_except_table4156
+ GCC_except_table4206
+ GCC_except_table4212
+ GCC_except_table4267
+ GCC_except_table4268
+ GCC_except_table4275
+ GCC_except_table4303
+ GCC_except_table4305
+ GCC_except_table4306
+ GCC_except_table4307
+ GCC_except_table4309
+ GCC_except_table4328
+ GCC_except_table4337
+ GCC_except_table4339
+ GCC_except_table4340
+ GCC_except_table4341
+ GCC_except_table4342
+ GCC_except_table4343
+ GCC_except_table4344
+ GCC_except_table4347
+ GCC_except_table4349
+ GCC_except_table4350
+ GCC_except_table4351
+ GCC_except_table4352
+ GCC_except_table4353
+ GCC_except_table4354
+ GCC_except_table4356
+ GCC_except_table4363
+ GCC_except_table4365
+ GCC_except_table4374
+ GCC_except_table4387
+ GCC_except_table4388
+ GCC_except_table4390
+ GCC_except_table4391
+ GCC_except_table4393
+ GCC_except_table4395
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4404
+ GCC_except_table4406
+ GCC_except_table4410
+ GCC_except_table4411
+ GCC_except_table4441
+ GCC_except_table4553
+ GCC_except_table4560
+ GCC_except_table4643
+ GCC_except_table4704
+ GCC_except_table4714
+ GCC_except_table4762
+ GCC_except_table4763
+ GCC_except_table4764
+ GCC_except_table4766
+ GCC_except_table4767
+ GCC_except_table4770
+ GCC_except_table4771
+ GCC_except_table4774
+ GCC_except_table4776
+ GCC_except_table4778
+ GCC_except_table4779
+ GCC_except_table4817
+ GCC_except_table4883
+ GCC_except_table4888
+ GCC_except_table4929
+ GCC_except_table4995
+ GCC_except_table893
+ GCC_except_table902
+ GCC_except_table964
+ GCC_except_table965
+ GCC_except_table972
+ GCC_except_table987
+ GCC_except_table988
+ GCC_except_table994
+ GCC_except_table999
+ OBJC_IVAR_$_CSAudioPowerProvider._audioEngine
+ OBJC_IVAR_$_CSAudioPowerProvider._sinkNode
+ OBJC_IVAR_$_CSAudioStopStreamOption._blockAttending
+ OBJC_IVAR_$_CSMicUsageReporter._lastReportedDeviceUID
+ OBJC_IVAR_$_CSMicUsageReporter._micCurrentlyReported
+ OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._isPhraseSpotterEnabled
+ OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._notifyToken
+ _AVAudioEngineConfigurationChangeNotification
+ _OBJC_CLASS_$_AVAudioSinkNode
+ _OBJC_CLASS_$_CSPhraseSpotterEnabledMonitor
+ _OBJC_METACLASS_$_CSPhraseSpotterEnabledMonitor
+ __47-[CSMicUsageReporter reportMicUsage:deviceUID:]_block_invoke
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
+ ___37-[CSAudioPowerProvider _startSelfTap]_block_invoke
+ ___47+[CSPhraseSpotterEnabledMonitor sharedInstance]_block_invoke
+ ___47-[CSMicUsageReporter reportMicUsage:deviceUID:]_block_invoke
+ ___79-[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]_block_invoke
+ ___83+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]_block_invoke
+ ___block_descriptor_41_e8_32s_e69_"STMediaStatusDomainMicrophoneRecordingAttribution"16?0"NSString"8l
+ ___block_descriptor_58_e8_32s40s48s_e40_v16?0"STMutableMediaStatusDomainData"8l
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_80_e100_i28?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20l
+ ___getSTMediaStatusDomainMicrophoneDescriptorClass_block_invoke
+ ___getSTMediaStatusDomainMicrophoneRecordingAttributionClass_block_invoke
+ _getSTMediaStatusDomainMicrophoneDescriptorClass
+ _getSTMediaStatusDomainMicrophoneRecordingAttributionClass
+ _kCSPhraseSpotterEnabledDidChangeDarwinNotification
+ _objc_msgSend$CSPhraseSpotterEnabledMonitor:didReceiveEnabled:
+ _objc_msgSend$_checkPhraseSpotterEnabled
+ _objc_msgSend$_currentHALDeviceUID
+ _objc_msgSend$_decoderForAudioStreamHandleId:
+ _objc_msgSend$_didReceivePhraseSpotterSettingChangedInQueue:
+ _objc_msgSend$_phraseSpotterEnabledDidChange
+ _objc_msgSend$_removeDecoderForAudioStreamHandleId:
+ _objc_msgSend$_startStandardPath
+ _objc_msgSend$addMicrophoneAttribution:
+ _objc_msgSend$channelCount
+ _objc_msgSend$connect:to:format:error:
+ _objc_msgSend$detachNode:
+ _objc_msgSend$initWithMicrophoneDescriptor:activityAttribution:maximumHistoryAccessed:
+ _objc_msgSend$initWithMicrophoneIdentifier:
+ _objc_msgSend$initWithReceiverBlock:
+ _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:blockAttending:
+ _objc_msgSend$inputNode
+ _objc_msgSend$isBuiltInRecordRoute:
+ _objc_msgSend$opusDecoders
+ _objc_msgSend$outputFormatForBus:
+ _objc_msgSend$phraseSpotterEnabled
+ _objc_msgSend$recordedAudioAvailableAt:requestId:filenamePostfix:completion:
+ _objc_msgSend$removeMicrophoneAttribution:
+ _objc_msgSend$reportMicUsage:deviceUID:
+ _objc_msgSend$setOpusDecoders:
+ getSTMediaStatusDomainMicrophoneDescriptorClass.softClass
+ getSTMediaStatusDomainMicrophoneRecordingAttributionClass.softClass
- -[CSAudioPowerProvider configureForRecordRoute:]
- -[CSMicUsageReporter micUsageAttribute]
- -[CSMicUsageReporter setMicUsageAttribute:]
- GCC_except_table1002
- GCC_except_table1020
- GCC_except_table1088
- GCC_except_table1095
- GCC_except_table1402
- GCC_except_table1431
- GCC_except_table1509
- GCC_except_table1513
- GCC_except_table1514
- GCC_except_table1515
- GCC_except_table1516
- GCC_except_table1517
- GCC_except_table1518
- GCC_except_table1519
- GCC_except_table1520
- GCC_except_table1537
- GCC_except_table1539
- GCC_except_table1545
- GCC_except_table1547
- GCC_except_table1728
- GCC_except_table1941
- GCC_except_table1942
- GCC_except_table1943
- GCC_except_table1944
- GCC_except_table1948
- GCC_except_table1951
- GCC_except_table1952
- GCC_except_table1968
- GCC_except_table1969
- GCC_except_table2035
- GCC_except_table2040
- GCC_except_table2098
- GCC_except_table2149
- GCC_except_table2150
- GCC_except_table2152
- GCC_except_table2153
- GCC_except_table2159
- GCC_except_table2170
- GCC_except_table2183
- GCC_except_table2226
- GCC_except_table2244
- GCC_except_table2323
- GCC_except_table2421
- GCC_except_table2458
- GCC_except_table2602
- GCC_except_table2606
- GCC_except_table2682
- GCC_except_table2693
- GCC_except_table2695
- GCC_except_table2700
- GCC_except_table2702
- GCC_except_table2744
- GCC_except_table2765
- GCC_except_table2805
- GCC_except_table2867
- GCC_except_table2869
- GCC_except_table2870
- GCC_except_table3033
- GCC_except_table3172
- GCC_except_table3180
- GCC_except_table3190
- GCC_except_table3199
- GCC_except_table3202
- GCC_except_table3204
- GCC_except_table3205
- GCC_except_table3244
- GCC_except_table3250
- GCC_except_table3297
- GCC_except_table3390
- GCC_except_table3402
- GCC_except_table3408
- GCC_except_table3415
- GCC_except_table3424
- GCC_except_table3448
- GCC_except_table3449
- GCC_except_table3451
- GCC_except_table3489
- GCC_except_table3649
- GCC_except_table3709
- GCC_except_table3723
- GCC_except_table3765
- GCC_except_table3766
- GCC_except_table3799
- GCC_except_table3800
- GCC_except_table3802
- GCC_except_table3805
- GCC_except_table3806
- GCC_except_table3807
- GCC_except_table3827
- GCC_except_table3829
- GCC_except_table3834
- GCC_except_table3835
- GCC_except_table3838
- GCC_except_table3908
- GCC_except_table3929
- GCC_except_table3930
- GCC_except_table3931
- GCC_except_table3932
- GCC_except_table4019
- GCC_except_table4020
- GCC_except_table4031
- GCC_except_table4033
- GCC_except_table4034
- GCC_except_table4035
- GCC_except_table4036
- GCC_except_table4039
- GCC_except_table4040
- GCC_except_table4043
- GCC_except_table4044
- GCC_except_table4049
- GCC_except_table4050
- GCC_except_table4051
- GCC_except_table4052
- GCC_except_table4053
- GCC_except_table4056
- GCC_except_table4068
- GCC_except_table4083
- GCC_except_table4086
- GCC_except_table4088
- GCC_except_table4089
- GCC_except_table4093
- GCC_except_table4099
- GCC_except_table4100
- GCC_except_table4101
- GCC_except_table4129
- GCC_except_table4177
- GCC_except_table4183
- GCC_except_table4238
- GCC_except_table4239
- GCC_except_table4246
- GCC_except_table4247
- GCC_except_table4248
- GCC_except_table4249
- GCC_except_table4251
- GCC_except_table4252
- GCC_except_table4274
- GCC_except_table4282
- GCC_except_table4283
- GCC_except_table4284
- GCC_except_table4285
- GCC_except_table4286
- GCC_except_table4287
- GCC_except_table4299
- GCC_except_table4308
- GCC_except_table4318
- GCC_except_table4320
- GCC_except_table4321
- GCC_except_table4322
- GCC_except_table4323
- GCC_except_table4324
- GCC_except_table4325
- GCC_except_table4327
- GCC_except_table4329
- GCC_except_table4330
- GCC_except_table4332
- GCC_except_table4334
- GCC_except_table4336
- GCC_except_table4338
- GCC_except_table4362
- GCC_except_table4364
- GCC_except_table4366
- GCC_except_table4368
- GCC_except_table4375
- GCC_except_table4377
- GCC_except_table4381
- GCC_except_table4382
- GCC_except_table4412
- GCC_except_table4524
- GCC_except_table4531
- GCC_except_table4613
- GCC_except_table4674
- GCC_except_table4684
- GCC_except_table4732
- GCC_except_table4733
- GCC_except_table4734
- GCC_except_table4736
- GCC_except_table4737
- GCC_except_table4742
- GCC_except_table4744
- GCC_except_table4745
- GCC_except_table4746
- GCC_except_table4784
- GCC_except_table4850
- GCC_except_table4855
- GCC_except_table4896
- GCC_except_table4962
- GCC_except_table889
- GCC_except_table898
- GCC_except_table960
- GCC_except_table961
- GCC_except_table968
- GCC_except_table983
- GCC_except_table984
- GCC_except_table985
- GCC_except_table990
- GCC_except_table991
- GCC_except_table992
- OBJC_IVAR_$_CSMicUsageReporter._micUsageAttribute
- __37-[CSMicUsageReporter reportMicUsage:]_block_invoke
- ___37-[CSMicUsageReporter reportMicUsage:]_block_invoke
- ___72+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:]_block_invoke
- ___block_descriptor_40_e8_32s_e40_v16?0"STMutableMediaStatusDomainData"8l
- _objc_msgSend$reportMicUsage:
CStrings:
+ "%s AVAudioEngine configuration changed, tap paused"
+ "%s AVAudioEngine returned -10868, ignoring (non-fatal)"
+ "%s Audio tap started via AVAudioSinkNode (sampleRate=%.0f)"
+ "%s Audio tap stopped"
+ "%s CSAudioProvider[%{public}@]:HAL device UID unavailable for mic usage reporting"
+ "%s Failed to configure audio engine, Low latency Siri waveform animation will not function : %{public}@"
+ "%s Failed to create CSAudioDecoder for stream %{public}lu"
+ "%s Failed to get valid inputFormat from audio engine, Low latency Siri waveform animation will not function"
+ "%s Failed to start AVAudioEngine: %{public}@"
+ "%s Input node format: sampleRate=%.0f channels=%u"
+ "%s No Opus decoder available for stream %{public}lu, dropping packet"
+ "%s PhraseSpotter enabled = %{public}@"
+ "%s PhraseSpotter is already %{public}@, received duplicated notification!"
+ "%s Reporting Mic Usage : %d device : %{public}@"
+ "%s deactivate called but tap not running, skipping"
+ "%s starting of self tap has failed, Siri waveform animation will falling back to standard power meter path"
+ "(none)"
+ "+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:completion:]_block_invoke"
+ ", blockAttending:%d"
+ "-[CSAudioPowerProvider _handleAudioEngineConfigChange:]"
+ "-[CSAudioPowerProvider _startSelfTap]"
+ "-[CSAudioPowerProvider configureForRecordRoute:preferUseSelfTap:]"
+ "-[CSAudioPowerProvider deactivate]"
+ "-[CSAudioProvider _currentHALDeviceUID]"
+ "-[CSAudioRecorder _decoderForAudioStreamHandleId:]"
+ "-[CSMicUsageReporter reportMicUsage:deviceUID:]_block_invoke"
+ "-[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]"
+ "-[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]"
+ "@\"STMediaStatusDomainMicrophoneRecordingAttribution\"16@?0@\"NSString\"8"
+ "STMediaStatusDomainMicrophoneDescriptor"
+ "STMediaStatusDomainMicrophoneRecordingAttribution"
+ "blockAttending"
+ "dictation"
+ "i28@?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20"
+ "kVTPreferencesPhraseSpotterEnabledDidChangeDarwinNotification"
+ "override_iobuffer_duration"
+ "\xf0!"
- "%s Reporting Mic Usage : %d"
- "+[CSFTTRAudioLogger recordedAudioAvailableAt:requestId:filenamePostfix:]_block_invoke"
- "-[CSAudioPowerProvider configureForRecordRoute:]"
- "-[CSMicUsageReporter reportMicUsage:]_block_invoke"
- "\xf01"

```
