## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-3600.70.47.0.0
-  __TEXT.__text: 0xc5430
-  __TEXT.__objc_methlist: 0xd7a0
+3605.23.1.0.0
+  __TEXT.__text: 0xc6be4
+  __TEXT.__objc_methlist: 0xd8c0
   __TEXT.__const: 0xb38
   __TEXT.__dlopen_cstrs: 0x18c
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_typeref: 0x19d
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x158af
+  __TEXT.__cstring: 0x15b32
   __TEXT.__swift5_reflstr: 0x174
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_fieldmd: 0x180
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3c08
-  __TEXT.__oslogstring: 0x1027f
-  __TEXT.__unwind_info: 0x4720
+  __TEXT.__gcc_except_tab: 0x3c64
+  __TEXT.__oslogstring: 0x1043c
+  __TEXT.__unwind_info: 0x4790
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__objc_classlist: 0x760
+  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x208
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7258
+  __DATA_CONST.__objc_selrefs: 0x72d8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x1e0
-  __DATA_CONST.__got: 0xc58
-  __AUTH_CONST.__const: 0x3a50
-  __AUTH_CONST.__cfstring: 0x92e0
-  __AUTH_CONST.__objc_const: 0x14d18
+  __DATA_CONST.__got: 0xc60
+  __AUTH_CONST.__const: 0x3ac0
+  __AUTH_CONST.__cfstring: 0x9740
+  __AUTH_CONST.__objc_const: 0x14eb8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xec8
-  __AUTH.__objc_data: 0x268
+  __AUTH.__objc_data: 0x2b8
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x18a8
+  __DATA.__objc_ivar: 0xd9c
+  __DATA.__data: 0x1908
   __DATA_DIRTY.__objc_data: 0x4810
   __DATA_DIRTY.__data: 0x310
-  __DATA_DIRTY.__bss: 0x600
+  __DATA_DIRTY.__bss: 0x610
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5229
-  Symbols:   12060
-  CStrings:  3575
+  Functions: 5259
+  Symbols:   12125
+  CStrings:  3614
 
Symbols:
+ +[CSAudioConsumingStateMonitor sharedInstance]
+ +[CSAudioStartStreamOption getRecordingStartTime:useMachContinuousTime:]
+ +[CSAudioStartStreamOption getRecordingStartTime:useMachContinuousTime:isVoiceTriggered:voiceTriggerInfo:useVoiceTriggerStartTime:]
+ +[CSUtils isAudioBufferPoolEnabled]
+ +[CSUtils isBargeInDisabled]
+ +[CSUtils isContinuousConversationDisabledInSiriX]
+ +[CSUtils isPerceptionBasedSpeakerChangeDetectionEnabled]
+ +[CSUtils(AudioDevice) isCarPlayRecordRoute:]
+ +[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]
+ +[CSUtils(Directory) clearLogFilesInDirectory:matchingPatterns:exceedNumber:]
+ +[CSUtils(Directory) clearLogFilesInDirectorySync:matchingPatterns:exceedNumber:outError:]
+ -[CSAudioConsumingStateMonitor _setAudioConsumingActive:]
+ -[CSAudioConsumingStateMonitor _startMonitoringWithQueue:]
+ -[CSAudioConsumingStateMonitor _stopMonitoring]
+ -[CSAudioConsumingStateMonitor init]
+ -[CSAudioConsumingStateMonitor isAudioConsumingSessionActive]
+ -[CSAudioConsumingStateMonitor notifyAudioConsumingSessionDidStart]
+ -[CSAudioConsumingStateMonitor notifyAudioConsumingSessionDidStop]
+ -[CSAudioRecordContext isInitialRequest]
+ -[CSAudioSpectralMeter setNormalizationEnabled:]
+ -[CSExclaveRecordClient skipProcessingRaiseToSpeakAOE:]
+ GCC_except_table1005
+ GCC_except_table1013
+ GCC_except_table1017
+ GCC_except_table1022
+ GCC_except_table1026
+ GCC_except_table1040
+ GCC_except_table1110
+ GCC_except_table1113
+ GCC_except_table1123
+ GCC_except_table1439
+ GCC_except_table1470
+ GCC_except_table1555
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1558
+ GCC_except_table1559
+ GCC_except_table1560
+ GCC_except_table1562
+ GCC_except_table1574
+ GCC_except_table1579
+ GCC_except_table1581
+ GCC_except_table1582
+ GCC_except_table1585
+ GCC_except_table1586
+ GCC_except_table1587
+ GCC_except_table1589
+ GCC_except_table1593
+ GCC_except_table1770
+ GCC_except_table1983
+ GCC_except_table1986
+ GCC_except_table1990
+ GCC_except_table1994
+ GCC_except_table1996
+ GCC_except_table2008
+ GCC_except_table2010
+ GCC_except_table2011
+ GCC_except_table2077
+ GCC_except_table2082
+ GCC_except_table2145
+ GCC_except_table2198
+ GCC_except_table2199
+ GCC_except_table2201
+ GCC_except_table2202
+ GCC_except_table2208
+ GCC_except_table2219
+ GCC_except_table2232
+ GCC_except_table2275
+ GCC_except_table2293
+ GCC_except_table2372
+ GCC_except_table2470
+ GCC_except_table2507
+ GCC_except_table2663
+ GCC_except_table2667
+ GCC_except_table2743
+ GCC_except_table2754
+ GCC_except_table2756
+ GCC_except_table2761
+ GCC_except_table2763
+ GCC_except_table2778
+ GCC_except_table2785
+ GCC_except_table2787
+ GCC_except_table2805
+ GCC_except_table2826
+ GCC_except_table2867
+ GCC_except_table2929
+ GCC_except_table2931
+ GCC_except_table2932
+ GCC_except_table3095
+ GCC_except_table3235
+ GCC_except_table3243
+ GCC_except_table3253
+ GCC_except_table3262
+ GCC_except_table3265
+ GCC_except_table3267
+ GCC_except_table3268
+ GCC_except_table3307
+ GCC_except_table3313
+ GCC_except_table3360
+ GCC_except_table3453
+ GCC_except_table3471
+ GCC_except_table3478
+ GCC_except_table3490
+ GCC_except_table3515
+ GCC_except_table3516
+ GCC_except_table3517
+ GCC_except_table3518
+ GCC_except_table3543
+ GCC_except_table3556
+ GCC_except_table3726
+ GCC_except_table3786
+ GCC_except_table3800
+ GCC_except_table3842
+ GCC_except_table3843
+ GCC_except_table3876
+ GCC_except_table3882
+ GCC_except_table3904
+ GCC_except_table3906
+ GCC_except_table3910
+ GCC_except_table3912
+ GCC_except_table3917
+ GCC_except_table3941
+ GCC_except_table3967
+ GCC_except_table3988
+ GCC_except_table4009
+ GCC_except_table4010
+ GCC_except_table4011
+ GCC_except_table4012
+ GCC_except_table410
+ GCC_except_table4111
+ GCC_except_table4113
+ GCC_except_table4114
+ GCC_except_table4119
+ GCC_except_table4123
+ GCC_except_table4124
+ GCC_except_table4125
+ GCC_except_table4129
+ GCC_except_table4130
+ GCC_except_table4131
+ GCC_except_table4145
+ GCC_except_table4148
+ GCC_except_table415
+ GCC_except_table4156
+ GCC_except_table4157
+ GCC_except_table4162
+ GCC_except_table4163
+ GCC_except_table4166
+ GCC_except_table4168
+ GCC_except_table4169
+ GCC_except_table4172
+ GCC_except_table4173
+ GCC_except_table4174
+ GCC_except_table4176
+ GCC_except_table4177
+ GCC_except_table4179
+ GCC_except_table418
+ GCC_except_table4181
+ GCC_except_table4182
+ GCC_except_table4210
+ GCC_except_table4260
+ GCC_except_table4266
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4333
+ GCC_except_table4358
+ GCC_except_table4360
+ GCC_except_table4361
+ GCC_except_table4371
+ GCC_except_table4394
+ GCC_except_table4395
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4398
+ GCC_except_table4400
+ GCC_except_table4402
+ GCC_except_table4404
+ GCC_except_table4405
+ GCC_except_table4406
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4409
+ GCC_except_table4411
+ GCC_except_table4414
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table4445
+ GCC_except_table4446
+ GCC_except_table4448
+ GCC_except_table4450
+ GCC_except_table4451
+ GCC_except_table4452
+ GCC_except_table4459
+ GCC_except_table4461
+ GCC_except_table4465
+ GCC_except_table4496
+ GCC_except_table4608
+ GCC_except_table4615
+ GCC_except_table465
+ GCC_except_table4698
+ GCC_except_table473
+ GCC_except_table4759
+ GCC_except_table4769
+ GCC_except_table4817
+ GCC_except_table4818
+ GCC_except_table4819
+ GCC_except_table4821
+ GCC_except_table4822
+ GCC_except_table4825
+ GCC_except_table4826
+ GCC_except_table4828
+ GCC_except_table4829
+ GCC_except_table4831
+ GCC_except_table4833
+ GCC_except_table4834
+ GCC_except_table4836
+ GCC_except_table4872
+ GCC_except_table4938
+ GCC_except_table4943
+ GCC_except_table4984
+ GCC_except_table5050
+ GCC_except_table578
+ GCC_except_table581
+ GCC_except_table616
+ GCC_except_table738
+ GCC_except_table742
+ GCC_except_table744
+ GCC_except_table747
+ GCC_except_table753
+ GCC_except_table909
+ GCC_except_table918
+ GCC_except_table981
+ GCC_except_table988
+ OBJC_IVAR_$_CSAudioConsumingStateMonitor._audioConsumingActive
+ OBJC_IVAR_$_CSAudioConsumingStateMonitor._lock
+ OBJC_IVAR_$_CSAudioPowerProvider._cachedSelfTapIOBufferDurationOverride
+ OBJC_IVAR_$_CSAudioPowerProvider._spectralNormalizationEnabled
+ _CSAudioPoolCleanup
+ _CSAudioPoolDataWithBytes
+ _CSSupportsCompanionRuntime
+ _OBJC_CLASS_$_CSAudioConsumingStateMonitor
+ _OBJC_METACLASS_$_CSAudioConsumingStateMonitor
+ __87+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]_block_invoke
+ __OBJC_$_CLASS_METHODS_CSAudioConsumingStateMonitor
+ __OBJC_$_INSTANCE_METHODS_CSAudioConsumingStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioConsumingStateMonitor
+ __OBJC_$_PROP_LIST_CSAudioConsumingStateMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConsumingStateMonitorProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConsumingStateMonitorProviding
+ __OBJC_$_PROTOCOL_REFS_CSAudioConsumingStateMonitorProviding
+ __OBJC_CLASS_PROTOCOLS_$_CSAudioConsumingStateMonitor
+ __OBJC_CLASS_RO_$_CSAudioConsumingStateMonitor
+ __OBJC_LABEL_PROTOCOL_$_CSAudioConsumingStateMonitorProviding
+ __OBJC_METACLASS_RO_$_CSAudioConsumingStateMonitor
+ __OBJC_PROTOCOL_$_CSAudioConsumingStateMonitorProviding
+ __ZN24CSAudioSpectralMeterImpl14_processWindowEPf
+ __ZN24CSAudioSpectralMeterImpl18resetNormalizationEv
+ __ZN24CSAudioSpectralMeterImpl23setNormalizationEnabledEb
+ ___46+[CSAudioConsumingStateMonitor sharedInstance]_block_invoke
+ ___50+[CSUtils isContinuousConversationDisabledInSiriX]_block_invoke
+ ___57-[CSAudioConsumingStateMonitor _setAudioConsumingActive:]_block_invoke
+ ___77+[CSUtils(Directory) clearLogFilesInDirectory:matchingPatterns:exceedNumber:]_block_invoke
+ ___87+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]_block_invoke
+ ____ensurePools_block_invoke
+ ___block_descriptor_40_e8_32s_e25_q24?0"NSURL"8"NSURL"16l
+ _ensurePools.onceToken
+ _objc_msgSend$_clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:
+ _objc_msgSend$_setAudioConsumingActive:
+ _objc_msgSend$absoluteHostTimeToContinuousHostTime:
+ _objc_msgSend$audioConsumingStateMonitor:didChangeActive:
+ _objc_msgSend$cleanup
+ _objc_msgSend$clearLogFilesInDirectory:matchingPatterns:exceedNumber:
+ _objc_msgSend$distantPast
+ _objc_msgSend$getRecordingStartTime:useMachContinuousTime:isVoiceTriggered:voiceTriggerInfo:useVoiceTriggerStartTime:
+ _objc_msgSend$isAudioBufferPoolEnabled
+ _objc_msgSend$isCarPlayRecordRoute:
+ _objc_msgSend$isRequestFromSpokenNotification
+ _objc_msgSend$selfTapIOBufferDurationOverride
+ _objc_msgSend$setNormalizationEnabled:
+ _objc_msgSend$skipProcessingRaiseToSpeakAOE:
+ _sLargePool
+ _sSmallPool
+ isContinuousConversationDisabledInSiriX.onceToken
- +[CSUtils isSiriDSPTurnedOn]
- +[CSUtils(Directory) clearLogFilesInDirectory:matchingPattern:exceedNumber:]
- GCC_except_table1002
- GCC_except_table1008
- GCC_except_table1014
- GCC_except_table1019
- GCC_except_table1023
- GCC_except_table1039
- GCC_except_table1109
- GCC_except_table1111
- GCC_except_table1122
- GCC_except_table1432
- GCC_except_table1463
- GCC_except_table1542
- GCC_except_table1546
- GCC_except_table1547
- GCC_except_table1548
- GCC_except_table1549
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1553
- GCC_except_table1564
- GCC_except_table1565
- GCC_except_table1572
- GCC_except_table1576
- GCC_except_table1577
- GCC_except_table1578
- GCC_except_table1580
- GCC_except_table1584
- GCC_except_table1761
- GCC_except_table1974
- GCC_except_table1975
- GCC_except_table1976
- GCC_except_table1977
- GCC_except_table1981
- GCC_except_table1987
- GCC_except_table1999
- GCC_except_table2001
- GCC_except_table2068
- GCC_except_table2073
- GCC_except_table2133
- GCC_except_table2184
- GCC_except_table2185
- GCC_except_table2187
- GCC_except_table2188
- GCC_except_table2194
- GCC_except_table2205
- GCC_except_table2218
- GCC_except_table2261
- GCC_except_table2279
- GCC_except_table2358
- GCC_except_table2456
- GCC_except_table2493
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table2729
- GCC_except_table2740
- GCC_except_table2742
- GCC_except_table2747
- GCC_except_table2749
- GCC_except_table2764
- GCC_except_table2771
- GCC_except_table2773
- GCC_except_table2791
- GCC_except_table2812
- GCC_except_table2853
- GCC_except_table2915
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table3082
- GCC_except_table3222
- GCC_except_table3230
- GCC_except_table3240
- GCC_except_table3249
- GCC_except_table3252
- GCC_except_table3254
- GCC_except_table3255
- GCC_except_table3294
- GCC_except_table3300
- GCC_except_table3347
- GCC_except_table3440
- GCC_except_table3452
- GCC_except_table3458
- GCC_except_table3474
- GCC_except_table3498
- GCC_except_table3499
- GCC_except_table3500
- GCC_except_table3501
- GCC_except_table3526
- GCC_except_table3539
- GCC_except_table3699
- GCC_except_table3759
- GCC_except_table3773
- GCC_except_table3815
- GCC_except_table3816
- GCC_except_table3849
- GCC_except_table3850
- GCC_except_table3852
- GCC_except_table3855
- GCC_except_table3856
- GCC_except_table3857
- GCC_except_table3885
- GCC_except_table3888
- GCC_except_table3937
- GCC_except_table3958
- GCC_except_table3979
- GCC_except_table3980
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table4069
- GCC_except_table407
- GCC_except_table4070
- GCC_except_table4081
- GCC_except_table4083
- GCC_except_table4084
- GCC_except_table4085
- GCC_except_table4086
- GCC_except_table4089
- GCC_except_table4090
- GCC_except_table4093
- GCC_except_table4094
- GCC_except_table4095
- GCC_except_table4096
- GCC_except_table4101
- GCC_except_table4102
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table4109
- GCC_except_table4118
- GCC_except_table4121
- GCC_except_table4127
- GCC_except_table4138
- GCC_except_table414
- GCC_except_table4142
- GCC_except_table4143
- GCC_except_table4144
- GCC_except_table4147
- GCC_except_table4149
- GCC_except_table4152
- GCC_except_table417
- GCC_except_table4230
- GCC_except_table4236
- GCC_except_table4292
- GCC_except_table4293
- GCC_except_table4300
- GCC_except_table4301
- GCC_except_table4302
- GCC_except_table4303
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4328
- GCC_except_table4334
- GCC_except_table4337
- GCC_except_table4338
- GCC_except_table4339
- GCC_except_table4340
- GCC_except_table4341
- GCC_except_table4353
- GCC_except_table4372
- GCC_except_table4374
- GCC_except_table4375
- GCC_except_table4376
- GCC_except_table4377
- GCC_except_table4378
- GCC_except_table4379
- GCC_except_table4381
- GCC_except_table4384
- GCC_except_table4386
- GCC_except_table4388
- GCC_except_table4390
- GCC_except_table4412
- GCC_except_table4415
- GCC_except_table4421
- GCC_except_table4431
- GCC_except_table4435
- GCC_except_table4436
- GCC_except_table4578
- GCC_except_table4585
- GCC_except_table464
- GCC_except_table4668
- GCC_except_table468
- GCC_except_table4729
- GCC_except_table4739
- GCC_except_table4787
- GCC_except_table4788
- GCC_except_table4789
- GCC_except_table4791
- GCC_except_table4792
- GCC_except_table4795
- GCC_except_table4796
- GCC_except_table4799
- GCC_except_table4801
- GCC_except_table4803
- GCC_except_table4804
- GCC_except_table4842
- GCC_except_table4908
- GCC_except_table4913
- GCC_except_table4954
- GCC_except_table5020
- GCC_except_table577
- GCC_except_table580
- GCC_except_table615
- GCC_except_table737
- GCC_except_table741
- GCC_except_table743
- GCC_except_table746
- GCC_except_table752
- GCC_except_table908
- GCC_except_table917
- GCC_except_table979
- GCC_except_table987
- ___47-[CSFPreferences setVoiceProfileRepairPrompted]_block_invoke
- ___76+[CSUtils(Directory) clearLogFilesInDirectory:matchingPattern:exceedNumber:]_block_invoke
- _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
- _objc_msgSend$connect:to:format:
- isAudioStreamProvidingEnabled.result
- setVoiceProfileRepairPrompted.onceToken
CStrings:
+ "%s #output_stream Failed to connect source node to main mixer: %@"
+ "%s Acquiring listening mic indicator lock from : %{public}@ %@"
+ "%s Acquiring recordModeLock from : %{public}@"
+ "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream from %{public}@ for %{public}.2f secs"
+ "%s Clearing listening mic indicator lock property, locks = %tu"
+ "%s Could not read directory %{public}@: %{public}@"
+ "%s Force releasing all %tu listening mic indicator locks"
+ "%s Releasing listening mic indicator lock from : %{public}@"
+ "%s Releasing listening mic indicator lock from : %{public}@ UUID = %@"
+ "%s Releasing listening mic indicator lock from = %{public}@"
+ "%s Releasing recordModeLock from : %{public}@"
+ "%s Releasing recordModeLock from : %{public}@ UUID = %@"
+ "%s Setting listening mic indicator lock property, locks = %tu"
+ "%s Spectral meter normalization enabled (CarPlay path)"
+ "%s Updating audio device info : recordRoute[%{public}@] deviceId[%{public}@] isRemoteDevice[%d]"
+ "+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]"
+ "-[CSAudioProvider _forceReleaseAllListeningMicIndicatorLocks]"
+ "IntutiveConvAudioCapture"
+ "IntutiveConvAudioCaptureHolding"
+ "LOCALE_ACW_SA"
+ "LOCALE_AFB_AE"
+ "LOCALE_AJP_JO"
+ "LOCALE_AJP_PS"
+ "LOCALE_APC_LB"
+ "LOCALE_APC_SY"
+ "LOCALE_ARS_SA"
+ "LOCALE_ARZ_EG"
+ "LOCALE_AZ_AZ"
+ "LOCALE_BE_BY"
+ "LOCALE_BG_BG"
+ "LOCALE_BN_IN"
+ "LOCALE_ET_EE"
+ "LOCALE_GU_IN"
+ "LOCALE_HI_LATN"
+ "LOCALE_IS_IS"
+ "LOCALE_KN_IN"
+ "LOCALE_ML_IN"
+ "LOCALE_MR_IN"
+ "LOCALE_PA_IN"
+ "LOCALE_SL_SI"
+ "LOCALE_SR_RS"
+ "LOCALE_TA_IN"
+ "LOCALE_TE_IN"
+ "LOCALE_UR_IN"
+ "LOCALE_UZ_UZ"
+ "LocalAttendingInitiator"
+ "LocalAttendingInitiatorHolding"
+ "NotHeld"
+ "OpportuneSpeakListener"
+ "OpportuneSpeakListenerHolding"
+ "SiriHolding"
+ "VoiceTriggerTraining"
- "%s Acquiring listening mic indicator lock from : %d %@"
- "%s Acquiring recordModeLock from : %d"
- "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream for %{public}f"
- "%s Clearing listening mic indicator lock property"
- "%s Releasing listening mic indicator lock UUID = %@"
- "%s Releasing listening mic indicator lock from : %d"
- "%s Releasing listening mic indicator lock from = %d"
- "%s Releasing recordModeLock from : %d"
- "%s Releasing recordModeLock lock UUID = %@"
- "%s Setting listening mic indicator lock property"
- "Conclaves"
- "com_apple_audiomxd_conclave"
- "support_audio_streaming"
```
