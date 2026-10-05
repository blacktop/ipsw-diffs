## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0xc9bc4
-  __TEXT.__objc_methlist: 0xdb18
-  __TEXT.__const: 0xfe8
+3605.31.3.0.0
+  __TEXT.__text: 0xcb278
+  __TEXT.__objc_methlist: 0xdcb0
+  __TEXT.__const: 0xff8
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x16b38
+  __TEXT.__cstring: 0x16c54
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3d24
-  __TEXT.__oslogstring: 0x11c58
-  __TEXT.__unwind_info: 0x4ac8
+  __TEXT.__gcc_except_tab: 0x3d30
+  __TEXT.__oslogstring: 0x11e8b
+  __TEXT.__unwind_info: 0x4b28
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28c8
-  __DATA_CONST.__objc_classlist: 0x750
+  __DATA_CONST.__const: 0x2920
+  __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7590
+  __DATA_CONST.__objc_selrefs: 0x7680
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x1040
+  __DATA_CONST.__got: 0x1048
   __AUTH_CONST.__const: 0x1b40
-  __AUTH_CONST.__cfstring: 0x9a60
-  __AUTH_CONST.__objc_const: 0x15018
+  __AUTH_CONST.__cfstring: 0x9a80
+  __AUTH_CONST.__objc_const: 0x15270
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH_CONST.__auth_got: 0xfc0
+  __AUTH_CONST.__auth_got: 0xfc8
   __AUTH.__objc_data: 0x218
-  __DATA.__objc_ivar: 0xdb0
+  __DATA.__objc_ivar: 0xdd4
   __DATA.__data: 0x1a60
-  __DATA_DIRTY.__objc_data: 0x47c0
+  __DATA_DIRTY.__objc_data: 0x4810
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x608
+  __DATA_DIRTY.__bss: 0x660
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5276
-  Symbols:   9902
-  CStrings:  3793
+  Functions: 5311
+  Symbols:   9961
+  CStrings:  3810
 
Symbols:
+ +[CSAudioStreamHoldRequestOption defaultOptionWithTimeout:requestExclaveAudio:]
+ +[CSConfig inputRecordingDurationInSecsAttentive]
+ +[CSFModelConfigDecoder purgeCachedConfigs]
+ +[CSFModelConfigDecoder(Test) cachedConfigPathsForTesting]
+ +[CSUtils allowAttentiveRingBufferSize]
+ +[CSUtils supportEarlyRecordingStartNotification]
+ -[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]
+ -[CSAudioProvider _anyPowerMeterLockNeedsBoost12dB]
+ -[CSAudioProvider _clientIdentityQualifiesForPowerMeter:]
+ -[CSAudioProvider _forceReleaseAllPowerMeterLocks]
+ -[CSAudioProvider _forceReleasePowerMeterLockFrom:]
+ -[CSAudioProvider _setStreamStateStreamingForTesting]
+ -[CSAudioProvider exfiltratingStreamHolderCountLock]
+ -[CSAudioProvider exfiltratingStreamHolderCount]
+ -[CSAudioProvider hasPowerMeterLock]
+ -[CSAudioProvider isLinwoodEnabledForPowerMeter]
+ -[CSAudioProvider powerMeterLocks]
+ -[CSAudioProvider powerMeterNeedsBoost12dB]
+ -[CSAudioProvider setExfiltratingStreamHolderCount:]
+ -[CSAudioProvider setExfiltratingStreamHolderCountLock:]
+ -[CSAudioProvider setHasPowerMeterLock:]
+ -[CSAudioProvider setIsLinwoodEnabledForPowerMeter:]
+ -[CSAudioProvider setPowerMeterLocks:]
+ -[CSAudioProvider setPowerMeterNeedsBoost12dB:]
+ -[CSAudioProviderPowerMeterLock initWithClientIdentity:needsBoost12dB:]
+ -[CSAudioProviderPowerMeterLock needsBoost12dB]
+ -[CSAudioRecordContext canCreateContinuousConversationProfile]
+ -[CSAudioStreamHoldRequestOption initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:requestExclaveAudio:]
+ -[CSAudioStreamHoldRequestOption requestExclaveAudio]
+ -[CSAudioStreamHolding initWithName:clientIdentity:requestExclaveAudio:]
+ -[CSAudioStreamHolding requestExclaveAudio]
+ -[CSEventMonitor _removeObserverOnQueue:]
+ GCC_except_table1356
+ GCC_except_table1387
+ GCC_except_table1474
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1477
+ GCC_except_table1478
+ GCC_except_table1479
+ GCC_except_table1480
+ GCC_except_table1488
+ GCC_except_table1491
+ GCC_except_table1499
+ GCC_except_table1503
+ GCC_except_table1505
+ GCC_except_table1507
+ GCC_except_table1511
+ GCC_except_table1523
+ GCC_except_table1919
+ GCC_except_table1920
+ GCC_except_table1926
+ GCC_except_table1929
+ GCC_except_table1932
+ GCC_except_table1938
+ GCC_except_table1945
+ GCC_except_table1947
+ GCC_except_table1948
+ GCC_except_table1963
+ GCC_except_table1969
+ GCC_except_table2057
+ GCC_except_table2062
+ GCC_except_table2125
+ GCC_except_table2137
+ GCC_except_table2179
+ GCC_except_table2180
+ GCC_except_table2182
+ GCC_except_table2183
+ GCC_except_table2189
+ GCC_except_table2200
+ GCC_except_table2207
+ GCC_except_table2250
+ GCC_except_table2268
+ GCC_except_table2349
+ GCC_except_table2461
+ GCC_except_table2496
+ GCC_except_table262
+ GCC_except_table2667
+ GCC_except_table2671
+ GCC_except_table274
+ GCC_except_table2750
+ GCC_except_table2761
+ GCC_except_table2768
+ GCC_except_table2770
+ GCC_except_table2790
+ GCC_except_table2792
+ GCC_except_table2810
+ GCC_except_table2831
+ GCC_except_table2877
+ GCC_except_table2934
+ GCC_except_table2936
+ GCC_except_table2937
+ GCC_except_table306
+ GCC_except_table3099
+ GCC_except_table3240
+ GCC_except_table3248
+ GCC_except_table3256
+ GCC_except_table3266
+ GCC_except_table3270
+ GCC_except_table3272
+ GCC_except_table3273
+ GCC_except_table330
+ GCC_except_table3309
+ GCC_except_table331
+ GCC_except_table3315
+ GCC_except_table332
+ GCC_except_table337
+ GCC_except_table3376
+ GCC_except_table3380
+ GCC_except_table340
+ GCC_except_table3447
+ GCC_except_table3451
+ GCC_except_table3458
+ GCC_except_table3470
+ GCC_except_table3494
+ GCC_except_table3495
+ GCC_except_table3496
+ GCC_except_table3497
+ GCC_except_table3522
+ GCC_except_table3535
+ GCC_except_table3705
+ GCC_except_table3765
+ GCC_except_table3779
+ GCC_except_table3821
+ GCC_except_table3851
+ GCC_except_table3852
+ GCC_except_table3857
+ GCC_except_table3858
+ GCC_except_table3859
+ GCC_except_table3882
+ GCC_except_table3884
+ GCC_except_table3888
+ GCC_except_table3889
+ GCC_except_table3890
+ GCC_except_table3895
+ GCC_except_table3921
+ GCC_except_table3947
+ GCC_except_table3968
+ GCC_except_table3988
+ GCC_except_table3989
+ GCC_except_table399
+ GCC_except_table3990
+ GCC_except_table3991
+ GCC_except_table400
+ GCC_except_table4001
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table4092
+ GCC_except_table4093
+ GCC_except_table4104
+ GCC_except_table4107
+ GCC_except_table4111
+ GCC_except_table4116
+ GCC_except_table4120
+ GCC_except_table4132
+ GCC_except_table4133
+ GCC_except_table4135
+ GCC_except_table4137
+ GCC_except_table4138
+ GCC_except_table4140
+ GCC_except_table4141
+ GCC_except_table4144
+ GCC_except_table4145
+ GCC_except_table4148
+ GCC_except_table4149
+ GCC_except_table4150
+ GCC_except_table4152
+ GCC_except_table4153
+ GCC_except_table4154
+ GCC_except_table4156
+ GCC_except_table4157
+ GCC_except_table4159
+ GCC_except_table4160
+ GCC_except_table4161
+ GCC_except_table4162
+ GCC_except_table4190
+ GCC_except_table4240
+ GCC_except_table4244
+ GCC_except_table4296
+ GCC_except_table4309
+ GCC_except_table4330
+ GCC_except_table4338
+ GCC_except_table4340
+ GCC_except_table4364
+ GCC_except_table4367
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4370
+ GCC_except_table4371
+ GCC_except_table4372
+ GCC_except_table4374
+ GCC_except_table4376
+ GCC_except_table4377
+ GCC_except_table4378
+ GCC_except_table4381
+ GCC_except_table4386
+ GCC_except_table4390
+ GCC_except_table4392
+ GCC_except_table4414
+ GCC_except_table4415
+ GCC_except_table4417
+ GCC_except_table4418
+ GCC_except_table4420
+ GCC_except_table4422
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4429
+ GCC_except_table4435
+ GCC_except_table4436
+ GCC_except_table4466
+ GCC_except_table4578
+ GCC_except_table4585
+ GCC_except_table4668
+ GCC_except_table4735
+ GCC_except_table4745
+ GCC_except_table4801
+ GCC_except_table4802
+ GCC_except_table4803
+ GCC_except_table4805
+ GCC_except_table4806
+ GCC_except_table4807
+ GCC_except_table4808
+ GCC_except_table4809
+ GCC_except_table4810
+ GCC_except_table4812
+ GCC_except_table4813
+ GCC_except_table4815
+ GCC_except_table4817
+ GCC_except_table4818
+ GCC_except_table4820
+ GCC_except_table4856
+ GCC_except_table4922
+ GCC_except_table4927
+ GCC_except_table4968
+ GCC_except_table5034
+ GCC_except_table507
+ GCC_except_table508
+ GCC_except_table541
+ GCC_except_table578
+ GCC_except_table581
+ GCC_except_table586
+ GCC_except_table604
+ GCC_except_table676
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table846
+ GCC_except_table853
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table924
+ GCC_except_table939
+ GCC_except_table940
+ GCC_except_table946
+ GCC_except_table951
+ GCC_except_table960
+ GCC_except_table961
+ GCC_except_table962
+ GCC_except_table976
+ _OBJC_CLASS_$_CSAudioProviderPowerMeterLock
+ _OBJC_IVAR_$_CSAudioProvider._exfiltratingStreamHolderCount
+ _OBJC_IVAR_$_CSAudioProvider._exfiltratingStreamHolderCountLock
+ _OBJC_IVAR_$_CSAudioProvider._hasPowerMeterLock
+ _OBJC_IVAR_$_CSAudioProvider._isLinwoodEnabledForPowerMeter
+ _OBJC_IVAR_$_CSAudioProvider._powerMeterLocks
+ _OBJC_IVAR_$_CSAudioProvider._powerMeterNeedsBoost12dB
+ _OBJC_IVAR_$_CSAudioProviderPowerMeterLock._needsBoost12dB
+ _OBJC_IVAR_$_CSAudioStreamHoldRequestOption._requestExclaveAudio
+ _OBJC_IVAR_$_CSAudioStreamHolding._requestExclaveAudio
+ _OBJC_METACLASS_$_CSAudioProviderPowerMeterLock
+ __OBJC_$_CLASS_METHODS_CSFModelConfigDecoder(Test)
+ __OBJC_$_INSTANCE_METHODS_CSAudioProviderPowerMeterLock
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioProviderPowerMeterLock
+ __OBJC_$_PROP_LIST_CSAudioProviderPowerMeterLock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionProviding
+ __OBJC_CLASS_RO_$_CSAudioProviderPowerMeterLock
+ __OBJC_METACLASS_RO_$_CSAudioProviderPowerMeterLock
+ ___50-[CSAudioProvider _forceReleaseAllPowerMeterLocks]_block_invoke
+ ___51-[CSAudioProvider _forceReleasePowerMeterLockFrom:]_block_invoke
+ ___68-[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]_block_invoke
+ ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_51_e8_32s40s_e5_v8?0ls32l8s40l8
+ _kCSEventMonitorQueueKey
+ _sConfigCache
+ _sConfigCacheLock
+ _sConfigStamp
+ _stat
- GCC_except_table1350
- GCC_except_table1381
- GCC_except_table1461
- GCC_except_table1465
- GCC_except_table1466
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table1470
- GCC_except_table1471
- GCC_except_table1481
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1490
- GCC_except_table1493
- GCC_except_table1496
- GCC_except_table1498
- GCC_except_table1516
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1912
- GCC_except_table1913
- GCC_except_table1914
- GCC_except_table1924
- GCC_except_table1937
- GCC_except_table1939
- GCC_except_table1940
- GCC_except_table1955
- GCC_except_table1961
- GCC_except_table2049
- GCC_except_table2054
- GCC_except_table2117
- GCC_except_table2129
- GCC_except_table2171
- GCC_except_table2172
- GCC_except_table2174
- GCC_except_table2175
- GCC_except_table2181
- GCC_except_table2192
- GCC_except_table2199
- GCC_except_table2242
- GCC_except_table2260
- GCC_except_table2339
- GCC_except_table2449
- GCC_except_table2484
- GCC_except_table260
- GCC_except_table2640
- GCC_except_table2644
- GCC_except_table272
- GCC_except_table2723
- GCC_except_table2734
- GCC_except_table2736
- GCC_except_table2741
- GCC_except_table2743
- GCC_except_table2756
- GCC_except_table2765
- GCC_except_table2804
- GCC_except_table2842
- GCC_except_table2899
- GCC_except_table2901
- GCC_except_table2902
- GCC_except_table302
- GCC_except_table3064
- GCC_except_table3205
- GCC_except_table3213
- GCC_except_table322
- GCC_except_table3221
- GCC_except_table3231
- GCC_except_table3235
- GCC_except_table3237
- GCC_except_table3238
- GCC_except_table324
- GCC_except_table327
- GCC_except_table3274
- GCC_except_table3280
- GCC_except_table333
- GCC_except_table3341
- GCC_except_table3345
- GCC_except_table336
- GCC_except_table3400
- GCC_except_table3412
- GCC_except_table3416
- GCC_except_table3423
- GCC_except_table3459
- GCC_except_table3460
- GCC_except_table3461
- GCC_except_table3462
- GCC_except_table3487
- GCC_except_table3500
- GCC_except_table3670
- GCC_except_table3730
- GCC_except_table3744
- GCC_except_table3786
- GCC_except_table3787
- GCC_except_table3816
- GCC_except_table3817
- GCC_except_table3819
- GCC_except_table3823
- GCC_except_table3824
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table3853
- GCC_except_table3855
- GCC_except_table3860
- GCC_except_table3886
- GCC_except_table390
- GCC_except_table3912
- GCC_except_table3933
- GCC_except_table395
- GCC_except_table3953
- GCC_except_table3954
- GCC_except_table3955
- GCC_except_table3956
- GCC_except_table396
- GCC_except_table3966
- GCC_except_table397
- GCC_except_table4057
- GCC_except_table4058
- GCC_except_table4067
- GCC_except_table4069
- GCC_except_table4070
- GCC_except_table4071
- GCC_except_table4072
- GCC_except_table4075
- GCC_except_table4076
- GCC_except_table4079
- GCC_except_table4080
- GCC_except_table4081
- GCC_except_table4082
- GCC_except_table4083
- GCC_except_table4084
- GCC_except_table4085
- GCC_except_table4086
- GCC_except_table4087
- GCC_except_table4090
- GCC_except_table4091
- GCC_except_table4097
- GCC_except_table4098
- GCC_except_table4100
- GCC_except_table4103
- GCC_except_table4109
- GCC_except_table4113
- GCC_except_table4124
- GCC_except_table4127
- GCC_except_table4155
- GCC_except_table4205
- GCC_except_table4209
- GCC_except_table4260
- GCC_except_table4261
- GCC_except_table4268
- GCC_except_table4269
- GCC_except_table4270
- GCC_except_table4271
- GCC_except_table4273
- GCC_except_table4274
- GCC_except_table4297
- GCC_except_table4298
- GCC_except_table4299
- GCC_except_table4301
- GCC_except_table4302
- GCC_except_table4307
- GCC_except_table4320
- GCC_except_table4329
- GCC_except_table4331
- GCC_except_table4335
- GCC_except_table4344
- GCC_except_table4345
- GCC_except_table4346
- GCC_except_table4348
- GCC_except_table4350
- GCC_except_table4351
- GCC_except_table4353
- GCC_except_table4357
- GCC_except_table4359
- GCC_except_table4382
- GCC_except_table4387
- GCC_except_table4389
- GCC_except_table4396
- GCC_except_table4400
- GCC_except_table4543
- GCC_except_table4550
- GCC_except_table4633
- GCC_except_table4700
- GCC_except_table4710
- GCC_except_table4766
- GCC_except_table4767
- GCC_except_table4768
- GCC_except_table4770
- GCC_except_table4771
- GCC_except_table4772
- GCC_except_table4773
- GCC_except_table4774
- GCC_except_table4775
- GCC_except_table4777
- GCC_except_table4778
- GCC_except_table4780
- GCC_except_table4782
- GCC_except_table4783
- GCC_except_table4785
- GCC_except_table4821
- GCC_except_table4887
- GCC_except_table4892
- GCC_except_table4933
- GCC_except_table4999
- GCC_except_table503
- GCC_except_table504
- GCC_except_table537
- GCC_except_table574
- GCC_except_table577
- GCC_except_table582
- GCC_except_table600
- GCC_except_table668
- GCC_except_table677
- GCC_except_table679
- GCC_except_table842
- GCC_except_table849
- GCC_except_table912
- GCC_except_table913
- GCC_except_table920
- GCC_except_table935
- GCC_except_table936
- GCC_except_table937
- GCC_except_table942
- GCC_except_table943
- GCC_except_table944
- GCC_except_table954
- GCC_except_table972
- __OBJC_$_CLASS_METHODS_CSFModelConfigDecoder
CStrings:
+ "%ld.%09ld:%lld"
+ "%s Acquiring power meter lock from : %{public}@ %@"
+ "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream from %{public}@ for %{public}.2f secs, requestExclaveAudio = %{public}s"
+ "%s CSAudioProvider[%{public}@]:Remaining audio stream holder requesting audio exfiltration: %{public}lu stream holders"
+ "%s Cached decoded model config %{public}@ (%{public}lu top-level keys, %{public}lu cached)"
+ "%s ERR: could not decode model config %{public}@: %{public}@"
+ "%s ERR: could not read model config %{public}@"
+ "%s ERR: model config %{public}@ is %{public}@, expected a dictionary"
+ "%s Force releasing all %tu power meter locks"
+ "%s Purged %{public}lu cached model config(s)"
+ "%s RecordSettings received from AVVC: %@"
+ "%s Releasing power meter lock from : %{public}@"
+ "+[CSFModelConfigDecoder purgeCachedConfigs]"
+ "-[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]"
+ "-[CSAudioProvider _forceReleaseAllPowerMeterLocks]"
+ "-[CSAudioProvider _forceReleasePowerMeterLockFrom:]"
+ "-[CSAudioRecorder recordSettingsWithStreamHandleId:]"
+ "SiriRecordStartAlert"
+ "startAlertBehavior=%ld"
+ "\xf0\"1"
- "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream from %{public}@ for %{public}.2f secs"
- "%s ERR: metaData is nil, defaulting to NO for %{public}@"
- "%s ERR: read metafile %{public}@ failed with %{public}@ - defaulting to NO"
```
