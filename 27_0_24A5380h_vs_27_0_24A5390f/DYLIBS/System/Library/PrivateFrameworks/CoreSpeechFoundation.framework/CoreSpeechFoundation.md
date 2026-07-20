## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

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
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.70.20.1.1
-  __TEXT.__text: 0xcbb14
-  __TEXT.__objc_methlist: 0xd808
-  __TEXT.__const: 0xfc8
+3600.70.32.0.0
+  __TEXT.__text: 0xcbbd4
+  __TEXT.__objc_methlist: 0xd988
+  __TEXT.__const: 0xfe8
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc

   __TEXT.__cstring: 0x1671a
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_fieldmd: 0x244
+  __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x3cec
   __TEXT.__oslogstring: 0x11931
-  __TEXT.__unwind_info: 0x3c00
+  __TEXT.__unwind_info: 0x3c20
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2840
-  __DATA_CONST.__objc_classlist: 0x738
+  __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7440
+  __DATA_CONST.__objc_selrefs: 0x74d0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x560
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x1c8
   __DATA_CONST.__got: 0x1038
   __AUTH_CONST.__const: 0x1ae0
   __AUTH_CONST.__cfstring: 0x9580
-  __AUTH_CONST.__objc_const: 0x14b70
+  __AUTH_CONST.__objc_const: 0x14dd0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x4b0

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xfc0
-  __AUTH.__objc_data: 0x128
-  __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x19a0
-  __DATA.__bss: 0x1568
+  __AUTH.__objc_data: 0x1c8
+  __DATA.__objc_ivar: 0xd90
+  __DATA.__data: 0x1a00
+  __DATA.__bss: 0x1580
   __DATA_DIRTY.__objc_data: 0x47c0
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x618
+  __DATA_DIRTY.__bss: 0x608
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5222
-  Symbols:   12159
+  Functions: 5236
+  Symbols:   12197
   CStrings:  3741
 
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
+ GCC_except_table1341
+ GCC_except_table1370
+ GCC_except_table1448
+ GCC_except_table1452
+ GCC_except_table1453
+ GCC_except_table1456
+ GCC_except_table1457
+ GCC_except_table1458
+ GCC_except_table1459
+ GCC_except_table1471
+ GCC_except_table1476
+ GCC_except_table1478
+ GCC_except_table1479
+ GCC_except_table1482
+ GCC_except_table1483
+ GCC_except_table1484
+ GCC_except_table1490
+ GCC_except_table1502
+ GCC_except_table1896
+ GCC_except_table1897
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1904
+ GCC_except_table1908
+ GCC_except_table1916
+ GCC_except_table1923
+ GCC_except_table1926
+ GCC_except_table1941
+ GCC_except_table1947
+ GCC_except_table2035
+ GCC_except_table2040
+ GCC_except_table2098
+ GCC_except_table2108
+ GCC_except_table2150
+ GCC_except_table2151
+ GCC_except_table2153
+ GCC_except_table2154
+ GCC_except_table2160
+ GCC_except_table2171
+ GCC_except_table2178
+ GCC_except_table2221
+ GCC_except_table2239
+ GCC_except_table2318
+ GCC_except_table2428
+ GCC_except_table2463
+ GCC_except_table2619
+ GCC_except_table2623
+ GCC_except_table2702
+ GCC_except_table2713
+ GCC_except_table2715
+ GCC_except_table2720
+ GCC_except_table2722
+ GCC_except_table2735
+ GCC_except_table2742
+ GCC_except_table2744
+ GCC_except_table2762
+ GCC_except_table2783
+ GCC_except_table2821
+ GCC_except_table2878
+ GCC_except_table2880
+ GCC_except_table2881
+ GCC_except_table302
+ GCC_except_table3044
+ GCC_except_table3192
+ GCC_except_table3210
+ GCC_except_table3214
+ GCC_except_table3216
+ GCC_except_table3217
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table3253
+ GCC_except_table3259
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table332
+ GCC_except_table3320
+ GCC_except_table3324
+ GCC_except_table335
+ GCC_except_table3391
+ GCC_except_table3402
+ GCC_except_table3411
+ GCC_except_table3434
+ GCC_except_table3435
+ GCC_except_table3436
+ GCC_except_table3437
+ GCC_except_table3462
+ GCC_except_table3475
+ GCC_except_table3634
+ GCC_except_table3694
+ GCC_except_table3708
+ GCC_except_table3750
+ GCC_except_table3751
+ GCC_except_table3780
+ GCC_except_table3781
+ GCC_except_table3783
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3811
+ GCC_except_table3813
+ GCC_except_table3817
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3822
+ GCC_except_table3847
+ GCC_except_table3873
+ GCC_except_table389
+ GCC_except_table3894
+ GCC_except_table3914
+ GCC_except_table3915
+ GCC_except_table3916
+ GCC_except_table3917
+ GCC_except_table3927
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table4018
+ GCC_except_table4019
+ GCC_except_table4033
+ GCC_except_table4037
+ GCC_except_table4040
+ GCC_except_table4041
+ GCC_except_table4044
+ GCC_except_table4046
+ GCC_except_table4052
+ GCC_except_table4061
+ GCC_except_table4074
+ GCC_except_table4075
+ GCC_except_table4076
+ GCC_except_table4078
+ GCC_except_table4079
+ GCC_except_table4080
+ GCC_except_table4082
+ GCC_except_table4083
+ GCC_except_table4085
+ GCC_except_table4086
+ GCC_except_table4087
+ GCC_except_table4088
+ GCC_except_table4116
+ GCC_except_table4166
+ GCC_except_table4170
+ GCC_except_table4220
+ GCC_except_table4221
+ GCC_except_table4228
+ GCC_except_table4229
+ GCC_except_table4230
+ GCC_except_table4231
+ GCC_except_table4233
+ GCC_except_table4234
+ GCC_except_table4255
+ GCC_except_table4257
+ GCC_except_table4258
+ GCC_except_table4259
+ GCC_except_table4261
+ GCC_except_table4262
+ GCC_except_table4263
+ GCC_except_table4265
+ GCC_except_table4266
+ GCC_except_table4267
+ GCC_except_table4268
+ GCC_except_table4291
+ GCC_except_table4293
+ GCC_except_table4296
+ GCC_except_table4302
+ GCC_except_table4304
+ GCC_except_table4305
+ GCC_except_table4306
+ GCC_except_table4308
+ GCC_except_table4311
+ GCC_except_table4313
+ GCC_except_table4315
+ GCC_except_table4317
+ GCC_except_table4319
+ GCC_except_table4339
+ GCC_except_table4342
+ GCC_except_table4343
+ GCC_except_table4347
+ GCC_except_table4348
+ GCC_except_table4349
+ GCC_except_table4354
+ GCC_except_table4356
+ GCC_except_table4360
+ GCC_except_table4361
+ GCC_except_table4391
+ GCC_except_table4503
+ GCC_except_table4510
+ GCC_except_table4593
+ GCC_except_table4660
+ GCC_except_table4670
+ GCC_except_table4728
+ GCC_except_table4730
+ GCC_except_table4731
+ GCC_except_table4732
+ GCC_except_table4733
+ GCC_except_table4734
+ GCC_except_table4735
+ GCC_except_table4738
+ GCC_except_table4740
+ GCC_except_table4742
+ GCC_except_table4743
+ GCC_except_table4781
+ GCC_except_table4847
+ GCC_except_table4852
+ GCC_except_table4893
+ GCC_except_table4959
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table536
+ GCC_except_table573
+ GCC_except_table576
+ GCC_except_table581
+ GCC_except_table599
+ GCC_except_table667
+ GCC_except_table671
+ GCC_except_table676
+ GCC_except_table678
+ GCC_except_table841
+ GCC_except_table848
+ GCC_except_table911
+ GCC_except_table912
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table943
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table947
+ GCC_except_table948
+ GCC_except_table951
+ GCC_except_table952
+ GCC_except_table953
+ GCC_except_table955
+ GCC_except_table957
+ GCC_except_table971
+ _CSIsWatchWithPHS
+ _OBJC_CLASS_$_CSOdeonStateMonitor
+ _OBJC_CLASS_$_CSRemoteAudioController
+ _OBJC_IVAR_$_CSRemoteAudioController._delegate
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
- GCC_except_table1325
- GCC_except_table1354
- GCC_except_table1432
- GCC_except_table1436
- GCC_except_table1437
- GCC_except_table1438
- GCC_except_table1439
- GCC_except_table1440
- GCC_except_table1441
- GCC_except_table1442
- GCC_except_table1443
- GCC_except_table1444
- GCC_except_table1451
- GCC_except_table1462
- GCC_except_table1463
- GCC_except_table1466
- GCC_except_table1468
- GCC_except_table1474
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1884
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1892
- GCC_except_table1894
- GCC_except_table1909
- GCC_except_table1931
- GCC_except_table2019
- GCC_except_table2024
- GCC_except_table2082
- GCC_except_table2092
- GCC_except_table2134
- GCC_except_table2135
- GCC_except_table2137
- GCC_except_table2138
- GCC_except_table2144
- GCC_except_table2155
- GCC_except_table2162
- GCC_except_table2205
- GCC_except_table2223
- GCC_except_table2302
- GCC_except_table2412
- GCC_except_table2447
- GCC_except_table2603
- GCC_except_table2607
- GCC_except_table2686
- GCC_except_table2697
- GCC_except_table2699
- GCC_except_table2704
- GCC_except_table2706
- GCC_except_table2719
- GCC_except_table2726
- GCC_except_table2728
- GCC_except_table2746
- GCC_except_table2767
- GCC_except_table2805
- GCC_except_table2862
- GCC_except_table2864
- GCC_except_table2865
- GCC_except_table287
- GCC_except_table3028
- GCC_except_table307
- GCC_except_table309
- GCC_except_table310
- GCC_except_table311
- GCC_except_table312
- GCC_except_table3168
- GCC_except_table317
- GCC_except_table3176
- GCC_except_table3194
- GCC_except_table3198
- GCC_except_table320
- GCC_except_table3201
- GCC_except_table3237
- GCC_except_table3243
- GCC_except_table3304
- GCC_except_table3308
- GCC_except_table3363
- GCC_except_table3375
- GCC_except_table3386
- GCC_except_table3418
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3446
- GCC_except_table3459
- GCC_except_table3618
- GCC_except_table3678
- GCC_except_table3692
- GCC_except_table3734
- GCC_except_table3735
- GCC_except_table374
- GCC_except_table3764
- GCC_except_table3765
- GCC_except_table3767
- GCC_except_table3770
- GCC_except_table3771
- GCC_except_table3772
- GCC_except_table378
- GCC_except_table379
- GCC_except_table3795
- GCC_except_table3797
- GCC_except_table380
- GCC_except_table3801
- GCC_except_table3802
- GCC_except_table3803
- GCC_except_table3806
- GCC_except_table381
- GCC_except_table382
- GCC_except_table3831
- GCC_except_table3857
- GCC_except_table3878
- GCC_except_table3898
- GCC_except_table3899
- GCC_except_table3900
- GCC_except_table3901
- GCC_except_table3911
- GCC_except_table4002
- GCC_except_table4003
- GCC_except_table4012
- GCC_except_table4014
- GCC_except_table4015
- GCC_except_table4016
- GCC_except_table4017
- GCC_except_table4020
- GCC_except_table4021
- GCC_except_table4024
- GCC_except_table4025
- GCC_except_table4026
- GCC_except_table4027
- GCC_except_table4029
- GCC_except_table4035
- GCC_except_table4050
- GCC_except_table4054
- GCC_except_table4055
- GCC_except_table4060
- GCC_except_table4062
- GCC_except_table4069
- GCC_except_table4072
- GCC_except_table4100
- GCC_except_table4150
- GCC_except_table4154
- GCC_except_table4204
- GCC_except_table4205
- GCC_except_table4212
- GCC_except_table4213
- GCC_except_table4214
- GCC_except_table4215
- GCC_except_table4217
- GCC_except_table4218
- GCC_except_table4239
- GCC_except_table4241
- GCC_except_table4242
- GCC_except_table4243
- GCC_except_table4245
- GCC_except_table4246
- GCC_except_table4247
- GCC_except_table4248
- GCC_except_table4249
- GCC_except_table4250
- GCC_except_table4251
- GCC_except_table4252
- GCC_except_table4273
- GCC_except_table4275
- GCC_except_table4276
- GCC_except_table4277
- GCC_except_table4278
- GCC_except_table4279
- GCC_except_table4281
- GCC_except_table4283
- GCC_except_table4285
- GCC_except_table4286
- GCC_except_table4287
- GCC_except_table4288
- GCC_except_table4290
- GCC_except_table4323
- GCC_except_table4324
- GCC_except_table4327
- GCC_except_table4329
- GCC_except_table4331
- GCC_except_table4332
- GCC_except_table4333
- GCC_except_table4338
- GCC_except_table4344
- GCC_except_table4375
- GCC_except_table4487
- GCC_except_table4494
- GCC_except_table4577
- GCC_except_table4644
- GCC_except_table4654
- GCC_except_table4710
- GCC_except_table4711
- GCC_except_table4712
- GCC_except_table4714
- GCC_except_table4715
- GCC_except_table4716
- GCC_except_table4717
- GCC_except_table4718
- GCC_except_table4719
- GCC_except_table4722
- GCC_except_table4724
- GCC_except_table4765
- GCC_except_table4831
- GCC_except_table4836
- GCC_except_table487
- GCC_except_table4877
- GCC_except_table488
- GCC_except_table4943
- GCC_except_table521
- GCC_except_table558
- GCC_except_table561
- GCC_except_table566
- GCC_except_table584
- GCC_except_table652
- GCC_except_table656
- GCC_except_table661
- GCC_except_table663
- GCC_except_table826
- GCC_except_table833
- GCC_except_table896
- GCC_except_table897
- GCC_except_table904
- GCC_except_table920
- GCC_except_table921
- GCC_except_table925
- GCC_except_table926
- GCC_except_table927
- GCC_except_table928
- GCC_except_table929
- GCC_except_table931
- GCC_except_table932
- GCC_except_table933
- GCC_except_table937
- GCC_except_table938
- __OBJC_$_CLASS_METHODS_CSUtils(Security|AudioDevice|Json|machXPC|RecordContext|LanguageCode|AudioHardware|Directory|Bitset|NSXPC)
```
