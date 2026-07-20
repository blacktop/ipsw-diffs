## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.70.20.4.1
-  __TEXT.__text: 0xc8cd4
-  __TEXT.__objc_methlist: 0xd5b8
-  __TEXT.__const: 0xb18
+3600.70.32.0.0
+  __TEXT.__text: 0xc8edc
+  __TEXT.__objc_methlist: 0xd740
+  __TEXT.__const: 0xb38
   __TEXT.__dlopen_cstrs: 0x18c
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_typeref: 0x19d

   __TEXT.__cstring: 0x1576d
   __TEXT.__swift5_reflstr: 0x174
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_fieldmd: 0x174
+  __TEXT.__swift5_fieldmd: 0x180
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x3c08
   __TEXT.__oslogstring: 0x10172
-  __TEXT.__unwind_info: 0x39b0
+  __TEXT.__unwind_info: 0x39d0
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__objc_classlist: 0x750
+  __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7190
+  __DATA_CONST.__objc_selrefs: 0x7220
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x1e0
   __DATA_CONST.__got: 0xc58
   __AUTH_CONST.__const: 0x3a30
   __AUTH_CONST.__cfstring: 0x9280
-  __AUTH_CONST.__objc_const: 0x14a38
+  __AUTH_CONST.__objc_const: 0x14c98
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xec8
-  __AUTH.__objc_data: 0x1c8
+  __AUTH.__objc_data: 0x268
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xd7c
-  __DATA.__data: 0x1848
-  __DATA.__bss: 0x9a0
+  __DATA.__objc_ivar: 0xd80
+  __DATA.__data: 0x18a8
+  __DATA.__bss: 0x9b0
   __DATA_DIRTY.__objc_data: 0x4810
   __DATA_DIRTY.__data: 0x310
-  __DATA_DIRTY.__bss: 0x610
+  __DATA_DIRTY.__bss: 0x600
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5204
-  Symbols:   12003
+  Functions: 5220
+  Symbols:   12041
   CStrings:  3565
 
Symbols:
+ +[CSOdeonStateMonitor sharedInstance]
+ +[CSUtils(RMS) rmsLinearGainForData:isFloat:]
+ -[CSOdeonStateMonitor _startMonitoringWithQueue:]
+ -[CSOdeonStateMonitor _stopMonitoring]
+ -[CSOdeonStateMonitor init]
+ -[CSOdeonStateMonitor isOdeonMediaGroup]
+ -[CSOdeonStateMonitor odeonSourceIdsIdentifier]
+ -[CSOdeonStateMonitor snapshotIsOdeonMediaGroup:sourceIdsIdentifier:]
+ -[CSRemoteAudioController .cxx_destruct]
+ -[CSRemoteAudioController delegate]
+ -[CSRemoteAudioController initWithProviderSelector:]
+ -[CSRemoteAudioController setDelegate:]
+ -[CSRemoteAudioController start]
+ -[CSRemoteAudioController stop]
+ -[CSRemoteAudioController voiceTriggerDidDetectKeyword:deviceId:]
+ GCC_except_table1002
+ GCC_except_table1003
+ GCC_except_table1011
+ GCC_except_table1012
+ GCC_except_table1014
+ GCC_except_table1015
+ GCC_except_table1016
+ GCC_except_table1019
+ GCC_except_table1020
+ GCC_except_table1021
+ GCC_except_table1023
+ GCC_except_table1025
+ GCC_except_table1039
+ GCC_except_table1109
+ GCC_except_table1111
+ GCC_except_table1112
+ GCC_except_table1122
+ GCC_except_table1430
+ GCC_except_table1459
+ GCC_except_table1537
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1545
+ GCC_except_table1546
+ GCC_except_table1547
+ GCC_except_table1548
+ GCC_except_table1560
+ GCC_except_table1565
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1571
+ GCC_except_table1572
+ GCC_except_table1573
+ GCC_except_table1575
+ GCC_except_table1579
+ GCC_except_table1756
+ GCC_except_table1969
+ GCC_except_table1970
+ GCC_except_table1971
+ GCC_except_table1976
+ GCC_except_table1979
+ GCC_except_table1982
+ GCC_except_table1988
+ GCC_except_table1994
+ GCC_except_table1996
+ GCC_except_table1997
+ GCC_except_table2063
+ GCC_except_table2068
+ GCC_except_table2126
+ GCC_except_table2177
+ GCC_except_table2178
+ GCC_except_table2180
+ GCC_except_table2181
+ GCC_except_table2187
+ GCC_except_table2198
+ GCC_except_table2211
+ GCC_except_table2254
+ GCC_except_table2272
+ GCC_except_table2351
+ GCC_except_table2449
+ GCC_except_table2486
+ GCC_except_table2642
+ GCC_except_table2646
+ GCC_except_table2722
+ GCC_except_table2733
+ GCC_except_table2735
+ GCC_except_table2740
+ GCC_except_table2742
+ GCC_except_table2757
+ GCC_except_table2764
+ GCC_except_table2766
+ GCC_except_table2784
+ GCC_except_table2805
+ GCC_except_table2846
+ GCC_except_table2908
+ GCC_except_table2910
+ GCC_except_table2911
+ GCC_except_table3075
+ GCC_except_table3214
+ GCC_except_table3222
+ GCC_except_table3232
+ GCC_except_table3241
+ GCC_except_table3244
+ GCC_except_table3246
+ GCC_except_table3247
+ GCC_except_table3286
+ GCC_except_table3292
+ GCC_except_table3339
+ GCC_except_table3432
+ GCC_except_table3444
+ GCC_except_table3457
+ GCC_except_table3466
+ GCC_except_table3490
+ GCC_except_table3491
+ GCC_except_table3492
+ GCC_except_table3493
+ GCC_except_table3518
+ GCC_except_table3531
+ GCC_except_table3691
+ GCC_except_table3751
+ GCC_except_table3765
+ GCC_except_table3807
+ GCC_except_table3808
+ GCC_except_table384
+ GCC_except_table3841
+ GCC_except_table3842
+ GCC_except_table3844
+ GCC_except_table3847
+ GCC_except_table3848
+ GCC_except_table3849
+ GCC_except_table3869
+ GCC_except_table3871
+ GCC_except_table3875
+ GCC_except_table3876
+ GCC_except_table3877
+ GCC_except_table3880
+ GCC_except_table3903
+ GCC_except_table3929
+ GCC_except_table3950
+ GCC_except_table3971
+ GCC_except_table3972
+ GCC_except_table3973
+ GCC_except_table3974
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table4073
+ GCC_except_table408
+ GCC_except_table4081
+ GCC_except_table4086
+ GCC_except_table4087
+ GCC_except_table4088
+ GCC_except_table409
+ GCC_except_table4093
+ GCC_except_table4095
+ GCC_except_table4098
+ GCC_except_table4101
+ GCC_except_table4107
+ GCC_except_table4110
+ GCC_except_table4113
+ GCC_except_table4124
+ GCC_except_table4130
+ GCC_except_table4131
+ GCC_except_table4134
+ GCC_except_table4135
+ GCC_except_table4136
+ GCC_except_table4138
+ GCC_except_table4139
+ GCC_except_table414
+ GCC_except_table4141
+ GCC_except_table4142
+ GCC_except_table4143
+ GCC_except_table4144
+ GCC_except_table417
+ GCC_except_table4172
+ GCC_except_table4222
+ GCC_except_table4228
+ GCC_except_table4283
+ GCC_except_table4284
+ GCC_except_table4291
+ GCC_except_table4292
+ GCC_except_table4293
+ GCC_except_table4294
+ GCC_except_table4296
+ GCC_except_table4297
+ GCC_except_table4319
+ GCC_except_table4321
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4325
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4329
+ GCC_except_table4330
+ GCC_except_table4331
+ GCC_except_table4332
+ GCC_except_table4355
+ GCC_except_table4357
+ GCC_except_table4360
+ GCC_except_table4366
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4370
+ GCC_except_table4372
+ GCC_except_table4375
+ GCC_except_table4377
+ GCC_except_table4379
+ GCC_except_table4381
+ GCC_except_table4383
+ GCC_except_table4403
+ GCC_except_table4407
+ GCC_except_table4409
+ GCC_except_table4412
+ GCC_except_table4413
+ GCC_except_table4420
+ GCC_except_table4422
+ GCC_except_table4426
+ GCC_except_table4427
+ GCC_except_table4457
+ GCC_except_table4569
+ GCC_except_table4576
+ GCC_except_table464
+ GCC_except_table4659
+ GCC_except_table468
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table472
+ GCC_except_table4720
+ GCC_except_table4730
+ GCC_except_table4780
+ GCC_except_table4782
+ GCC_except_table4783
+ GCC_except_table4786
+ GCC_except_table4787
+ GCC_except_table4790
+ GCC_except_table4792
+ GCC_except_table4794
+ GCC_except_table4795
+ GCC_except_table4833
+ GCC_except_table4899
+ GCC_except_table4904
+ GCC_except_table4945
+ GCC_except_table5011
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table615
+ GCC_except_table741
+ GCC_except_table743
+ GCC_except_table746
+ GCC_except_table752
+ GCC_except_table908
+ GCC_except_table917
+ GCC_except_table979
+ GCC_except_table980
+ OBJC_IVAR_$_CSRemoteAudioController._delegate
+ _CSIsWatchWithPHS
+ _OBJC_CLASS_$_CSOdeonStateMonitor
+ _OBJC_CLASS_$_CSRemoteAudioController
+ _OBJC_METACLASS_$_CSOdeonStateMonitor
+ _OBJC_METACLASS_$_CSRemoteAudioController
+ __OBJC_$_CLASS_METHODS_CSOdeonStateMonitor
+ __OBJC_$_CLASS_METHODS_CSUtils(RMS|Security|AudioDevice|Json|machXPC|RecordContext|LanguageCode|AudioHardware|Directory|Bitset|NSXPC)
+ __OBJC_$_INSTANCE_METHODS_CSOdeonStateMonitor
+ __OBJC_$_INSTANCE_METHODS_CSRemoteAudioController
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoteAudioController
+ __OBJC_$_PROP_LIST_CSOdeonStateMonitor
+ __OBJC_$_PROP_LIST_CSRemoteAudioController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CSRemoteAudioController
+ __OBJC_CLASS_RO_$_CSOdeonStateMonitor
+ __OBJC_CLASS_RO_$_CSRemoteAudioController
+ __OBJC_LABEL_PROTOCOL_$_CSVoiceTriggerDelegate
+ __OBJC_METACLASS_RO_$_CSOdeonStateMonitor
+ __OBJC_METACLASS_RO_$_CSRemoteAudioController
+ __OBJC_PROTOCOL_$_CSVoiceTriggerDelegate
- GCC_except_table1000
- GCC_except_table1001
- GCC_except_table1005
- GCC_except_table1006
- GCC_except_table1094
- GCC_except_table1096
- GCC_except_table1097
- GCC_except_table1107
- GCC_except_table1414
- GCC_except_table1443
- GCC_except_table1521
- GCC_except_table1525
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1529
- GCC_except_table1530
- GCC_except_table1531
- GCC_except_table1532
- GCC_except_table1533
- GCC_except_table1540
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1555
- GCC_except_table1557
- GCC_except_table1563
- GCC_except_table1740
- GCC_except_table1953
- GCC_except_table1954
- GCC_except_table1955
- GCC_except_table1956
- GCC_except_table1960
- GCC_except_table1963
- GCC_except_table1964
- GCC_except_table1966
- GCC_except_table1978
- GCC_except_table1981
- GCC_except_table2047
- GCC_except_table2052
- GCC_except_table2110
- GCC_except_table2161
- GCC_except_table2162
- GCC_except_table2164
- GCC_except_table2165
- GCC_except_table2171
- GCC_except_table2182
- GCC_except_table2195
- GCC_except_table2238
- GCC_except_table2256
- GCC_except_table2335
- GCC_except_table2433
- GCC_except_table2470
- GCC_except_table2626
- GCC_except_table2630
- GCC_except_table2706
- GCC_except_table2717
- GCC_except_table2719
- GCC_except_table2724
- GCC_except_table2726
- GCC_except_table2741
- GCC_except_table2748
- GCC_except_table2750
- GCC_except_table2768
- GCC_except_table2789
- GCC_except_table2830
- GCC_except_table2892
- GCC_except_table2894
- GCC_except_table2895
- GCC_except_table3059
- GCC_except_table3198
- GCC_except_table3206
- GCC_except_table3216
- GCC_except_table3225
- GCC_except_table3228
- GCC_except_table3230
- GCC_except_table3231
- GCC_except_table3270
- GCC_except_table3276
- GCC_except_table3323
- GCC_except_table3416
- GCC_except_table3428
- GCC_except_table3434
- GCC_except_table3441
- GCC_except_table3474
- GCC_except_table3475
- GCC_except_table3476
- GCC_except_table3477
- GCC_except_table3502
- GCC_except_table3515
- GCC_except_table3675
- GCC_except_table369
- GCC_except_table3735
- GCC_except_table3749
- GCC_except_table3791
- GCC_except_table3792
- GCC_except_table3825
- GCC_except_table3826
- GCC_except_table3828
- GCC_except_table3831
- GCC_except_table3832
- GCC_except_table3833
- GCC_except_table3853
- GCC_except_table3855
- GCC_except_table3859
- GCC_except_table3860
- GCC_except_table3861
- GCC_except_table3864
- GCC_except_table3887
- GCC_except_table389
- GCC_except_table391
- GCC_except_table3913
- GCC_except_table392
- GCC_except_table393
- GCC_except_table3934
- GCC_except_table394
- GCC_except_table3955
- GCC_except_table3956
- GCC_except_table3957
- GCC_except_table3958
- GCC_except_table399
- GCC_except_table402
- GCC_except_table4045
- GCC_except_table4046
- GCC_except_table4057
- GCC_except_table4059
- GCC_except_table4060
- GCC_except_table4065
- GCC_except_table4066
- GCC_except_table4069
- GCC_except_table4070
- GCC_except_table4071
- GCC_except_table4072
- GCC_except_table4079
- GCC_except_table4096
- GCC_except_table4097
- GCC_except_table4102
- GCC_except_table4103
- GCC_except_table4109
- GCC_except_table4114
- GCC_except_table4115
- GCC_except_table4120
- GCC_except_table4122
- GCC_except_table4123
- GCC_except_table4126
- GCC_except_table4127
- GCC_except_table4156
- GCC_except_table4206
- GCC_except_table4212
- GCC_except_table4267
- GCC_except_table4268
- GCC_except_table4275
- GCC_except_table4276
- GCC_except_table4277
- GCC_except_table4278
- GCC_except_table4280
- GCC_except_table4281
- GCC_except_table4303
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4307
- GCC_except_table4309
- GCC_except_table4310
- GCC_except_table4311
- GCC_except_table4312
- GCC_except_table4313
- GCC_except_table4314
- GCC_except_table4315
- GCC_except_table4316
- GCC_except_table4337
- GCC_except_table4339
- GCC_except_table4340
- GCC_except_table4341
- GCC_except_table4342
- GCC_except_table4343
- GCC_except_table4345
- GCC_except_table4347
- GCC_except_table4349
- GCC_except_table4350
- GCC_except_table4351
- GCC_except_table4352
- GCC_except_table4354
- GCC_except_table4387
- GCC_except_table4388
- GCC_except_table4391
- GCC_except_table4393
- GCC_except_table4395
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table4410
- GCC_except_table4441
- GCC_except_table449
- GCC_except_table453
- GCC_except_table454
- GCC_except_table455
- GCC_except_table4553
- GCC_except_table456
- GCC_except_table4560
- GCC_except_table457
- GCC_except_table4643
- GCC_except_table4704
- GCC_except_table4714
- GCC_except_table4762
- GCC_except_table4763
- GCC_except_table4764
- GCC_except_table4766
- GCC_except_table4767
- GCC_except_table4770
- GCC_except_table4771
- GCC_except_table4774
- GCC_except_table4776
- GCC_except_table4817
- GCC_except_table4883
- GCC_except_table4888
- GCC_except_table4929
- GCC_except_table4995
- GCC_except_table562
- GCC_except_table565
- GCC_except_table600
- GCC_except_table722
- GCC_except_table726
- GCC_except_table728
- GCC_except_table731
- GCC_except_table893
- GCC_except_table902
- GCC_except_table964
- GCC_except_table965
- GCC_except_table972
- GCC_except_table988
- GCC_except_table989
- GCC_except_table993
- GCC_except_table994
- GCC_except_table995
- GCC_except_table996
- GCC_except_table997
- GCC_except_table999
- __OBJC_$_CLASS_METHODS_CSUtils(Security|AudioDevice|Json|machXPC|RecordContext|LanguageCode|AudioHardware|Directory|Bitset|NSXPC)
```
