## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0xcbbd4
-  __TEXT.__objc_methlist: 0xd988
+3600.70.47.0.0
+  __TEXT.__text: 0xcbf6c
+  __TEXT.__objc_methlist: 0xd9d8
   __TEXT.__const: 0xfe8
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x1671a
+  __TEXT.__cstring: 0x16841
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x3cec
-  __TEXT.__oslogstring: 0x11931
-  __TEXT.__unwind_info: 0x3c20
+  __TEXT.__oslogstring: 0x11a3e
+  __TEXT.__unwind_info: 0x3e10
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x74d0
+  __DATA_CONST.__objc_selrefs: 0x7500
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x1c8
   __DATA_CONST.__got: 0x1038
-  __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0x9580
-  __AUTH_CONST.__objc_const: 0x14dd0
+  __AUTH_CONST.__const: 0x1b00
+  __AUTH_CONST.__cfstring: 0x95c0
+  __AUTH_CONST.__objc_const: 0x14e50
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x4b0

   __AUTH_CONST.__objc_floatobj: 0x1a0
   __AUTH_CONST.__auth_got: 0xfc0
   __AUTH.__objc_data: 0x1c8
-  __DATA.__objc_ivar: 0xd90
+  __DATA.__objc_ivar: 0xd9c
   __DATA.__data: 0x1a00
-  __DATA.__bss: 0x1580
+  __DATA.__bss: 0x1588
   __DATA_DIRTY.__objc_data: 0x47c0
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x608
+  __DATA_DIRTY.__bss: 0x610
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5236
-  Symbols:   12197
-  CStrings:  3741
+  Functions: 5244
+  Symbols:   12215
+  CStrings:  3750
 
Symbols:
+ -[CSAudioRecordContext handoffInvocationTypeFromTriggerPhrase]
+ -[CSAudioRecordContext remoteDeviceInvocationType]
+ -[CSAudioRecordContext setRemoteDeviceInvocationType:]
+ -[CSAudioStartStreamOption originatingDeviceSupportsAlwaysListeningHeySiri]
+ -[CSAudioStartStreamOption setOriginatingDeviceSupportsAlwaysListeningHeySiri:]
+ -[CSVoiceTriggerUserSelectedPhrase _localeSupportsMultiPhrase]
+ GCC_except_table1343
+ GCC_except_table1374
+ GCC_except_table1461
+ GCC_except_table1462
+ GCC_except_table1463
+ GCC_except_table1464
+ GCC_except_table1465
+ GCC_except_table1472
+ GCC_except_table1475
+ GCC_except_table1481
+ GCC_except_table1487
+ GCC_except_table1488
+ GCC_except_table1489
+ GCC_except_table1491
+ GCC_except_table1495
+ GCC_except_table1507
+ GCC_except_table1901
+ GCC_except_table1902
+ GCC_except_table1903
+ GCC_except_table1905
+ GCC_except_table1909
+ GCC_except_table1912
+ GCC_except_table1913
+ GCC_except_table1915
+ GCC_except_table1921
+ GCC_except_table1928
+ GCC_except_table1930
+ GCC_except_table1931
+ GCC_except_table1946
+ GCC_except_table1952
+ GCC_except_table2045
+ GCC_except_table2105
+ GCC_except_table2115
+ GCC_except_table2157
+ GCC_except_table2158
+ GCC_except_table2161
+ GCC_except_table2167
+ GCC_except_table2185
+ GCC_except_table2228
+ GCC_except_table2246
+ GCC_except_table2325
+ GCC_except_table2435
+ GCC_except_table2470
+ GCC_except_table2626
+ GCC_except_table2630
+ GCC_except_table2709
+ GCC_except_table2727
+ GCC_except_table2729
+ GCC_except_table2749
+ GCC_except_table2751
+ GCC_except_table2769
+ GCC_except_table2790
+ GCC_except_table2828
+ GCC_except_table2885
+ GCC_except_table2887
+ GCC_except_table2888
+ GCC_except_table3051
+ GCC_except_table3191
+ GCC_except_table3199
+ GCC_except_table3207
+ GCC_except_table3221
+ GCC_except_table3223
+ GCC_except_table3224
+ GCC_except_table3260
+ GCC_except_table3266
+ GCC_except_table3327
+ GCC_except_table3331
+ GCC_except_table3386
+ GCC_except_table3398
+ GCC_except_table3409
+ GCC_except_table3418
+ GCC_except_table3441
+ GCC_except_table3442
+ GCC_except_table3443
+ GCC_except_table3444
+ GCC_except_table3469
+ GCC_except_table3482
+ GCC_except_table3641
+ GCC_except_table3701
+ GCC_except_table3715
+ GCC_except_table3757
+ GCC_except_table3758
+ GCC_except_table3790
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3820
+ GCC_except_table3824
+ GCC_except_table3825
+ GCC_except_table3826
+ GCC_except_table3829
+ GCC_except_table3854
+ GCC_except_table3880
+ GCC_except_table3901
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table3923
+ GCC_except_table3924
+ GCC_except_table3934
+ GCC_except_table4025
+ GCC_except_table4026
+ GCC_except_table4035
+ GCC_except_table4038
+ GCC_except_table4039
+ GCC_except_table4049
+ GCC_except_table4050
+ GCC_except_table4053
+ GCC_except_table4054
+ GCC_except_table4055
+ GCC_except_table4065
+ GCC_except_table4068
+ GCC_except_table4073
+ GCC_except_table4077
+ GCC_except_table4081
+ GCC_except_table4089
+ GCC_except_table4090
+ GCC_except_table4092
+ GCC_except_table4093
+ GCC_except_table4094
+ GCC_except_table4095
+ GCC_except_table4123
+ GCC_except_table4173
+ GCC_except_table4177
+ GCC_except_table4236
+ GCC_except_table4237
+ GCC_except_table4238
+ GCC_except_table4239
+ GCC_except_table4241
+ GCC_except_table4242
+ GCC_except_table4269
+ GCC_except_table4270
+ GCC_except_table4271
+ GCC_except_table4272
+ GCC_except_table4273
+ GCC_except_table4274
+ GCC_except_table4275
+ GCC_except_table4276
+ GCC_except_table4288
+ GCC_except_table4300
+ GCC_except_table4307
+ GCC_except_table4309
+ GCC_except_table4312
+ GCC_except_table4314
+ GCC_except_table4316
+ GCC_except_table4318
+ GCC_except_table4321
+ GCC_except_table4323
+ GCC_except_table4325
+ GCC_except_table4327
+ GCC_except_table4334
+ GCC_except_table4350
+ GCC_except_table4351
+ GCC_except_table4353
+ GCC_except_table4355
+ GCC_except_table4357
+ GCC_except_table4362
+ GCC_except_table4364
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4399
+ GCC_except_table4511
+ GCC_except_table4518
+ GCC_except_table4601
+ GCC_except_table4668
+ GCC_except_table4678
+ GCC_except_table4736
+ GCC_except_table4739
+ GCC_except_table4741
+ GCC_except_table4746
+ GCC_except_table4748
+ GCC_except_table4750
+ GCC_except_table4751
+ GCC_except_table4789
+ GCC_except_table4855
+ GCC_except_table4860
+ GCC_except_table4901
+ GCC_except_table4967
+ _CSDeviceSupportsAlwaysListeningHeySiri
+ _CSDeviceSupportsAlwaysListeningHeySiri.onceToken
+ _CSDeviceSupportsAlwaysListeningHeySiri.supportsALHS
+ _OBJC_IVAR_$_CSAudioPowerProvider._pendingSelfTapStart
+ _OBJC_IVAR_$_CSAudioRecordContext._remoteDeviceInvocationType
+ _OBJC_IVAR_$_CSAudioStartStreamOption._originatingDeviceSupportsAlwaysListeningHeySiri
+ ___CSDeviceSupportsAlwaysListeningHeySiri_block_invoke
+ _objc_msgSend$_localeSupportsMultiPhrase
+ _objc_msgSend$remoteDeviceInvocationType
+ _objc_msgSend$setOriginatingDeviceSupportsAlwaysListeningHeySiri:
+ _objc_msgSend$setRemoteDeviceInvocationType:
+ _objc_msgSend$supportsMphForLanguageCode:
- GCC_except_table1341
- GCC_except_table1370
- GCC_except_table1448
- GCC_except_table1452
- GCC_except_table1454
- GCC_except_table1455
- GCC_except_table1456
- GCC_except_table1467
- GCC_except_table1470
- GCC_except_table1471
- GCC_except_table1478
- GCC_except_table1479
- GCC_except_table1482
- GCC_except_table1486
- GCC_except_table1490
- GCC_except_table1502
- GCC_except_table1896
- GCC_except_table1897
- GCC_except_table1898
- GCC_except_table1899
- GCC_except_table1900
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1910
- GCC_except_table1916
- GCC_except_table1923
- GCC_except_table1925
- GCC_except_table1926
- GCC_except_table1941
- GCC_except_table1947
- GCC_except_table2035
- GCC_except_table2098
- GCC_except_table2108
- GCC_except_table2150
- GCC_except_table2151
- GCC_except_table2153
- GCC_except_table2154
- GCC_except_table2171
- GCC_except_table2221
- GCC_except_table2239
- GCC_except_table2318
- GCC_except_table2428
- GCC_except_table2463
- GCC_except_table2619
- GCC_except_table2623
- GCC_except_table2702
- GCC_except_table2713
- GCC_except_table2715
- GCC_except_table2735
- GCC_except_table2744
- GCC_except_table2762
- GCC_except_table2783
- GCC_except_table2821
- GCC_except_table2878
- GCC_except_table2880
- GCC_except_table2881
- GCC_except_table3044
- GCC_except_table3184
- GCC_except_table3192
- GCC_except_table3200
- GCC_except_table3210
- GCC_except_table3214
- GCC_except_table3216
- GCC_except_table3253
- GCC_except_table3259
- GCC_except_table3320
- GCC_except_table3324
- GCC_except_table3379
- GCC_except_table3391
- GCC_except_table3395
- GCC_except_table3411
- GCC_except_table3434
- GCC_except_table3435
- GCC_except_table3436
- GCC_except_table3437
- GCC_except_table3462
- GCC_except_table3475
- GCC_except_table3634
- GCC_except_table3694
- GCC_except_table3708
- GCC_except_table3750
- GCC_except_table3751
- GCC_except_table3780
- GCC_except_table3781
- GCC_except_table3783
- GCC_except_table3786
- GCC_except_table3811
- GCC_except_table3813
- GCC_except_table3817
- GCC_except_table3819
- GCC_except_table3822
- GCC_except_table3847
- GCC_except_table3873
- GCC_except_table3894
- GCC_except_table3914
- GCC_except_table3915
- GCC_except_table3916
- GCC_except_table3917
- GCC_except_table3927
- GCC_except_table4018
- GCC_except_table4019
- GCC_except_table4028
- GCC_except_table4030
- GCC_except_table4031
- GCC_except_table4032
- GCC_except_table4033
- GCC_except_table4036
- GCC_except_table4041
- GCC_except_table4042
- GCC_except_table4045
- GCC_except_table4046
- GCC_except_table4061
- GCC_except_table4063
- GCC_except_table4064
- GCC_except_table4067
- GCC_except_table4075
- GCC_except_table4076
- GCC_except_table4079
- GCC_except_table4080
- GCC_except_table4088
- GCC_except_table4116
- GCC_except_table4166
- GCC_except_table4170
- GCC_except_table4220
- GCC_except_table4221
- GCC_except_table4230
- GCC_except_table4231
- GCC_except_table4233
- GCC_except_table4234
- GCC_except_table4255
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table4259
- GCC_except_table4261
- GCC_except_table4262
- GCC_except_table4264
- GCC_except_table4268
- GCC_except_table4280
- GCC_except_table4289
- GCC_except_table4291
- GCC_except_table4292
- GCC_except_table4293
- GCC_except_table4294
- GCC_except_table4295
- GCC_except_table4296
- GCC_except_table4306
- GCC_except_table4308
- GCC_except_table4315
- GCC_except_table4317
- GCC_except_table4326
- GCC_except_table4339
- GCC_except_table4340
- GCC_except_table4342
- GCC_except_table4343
- GCC_except_table4345
- GCC_except_table4349
- GCC_except_table4354
- GCC_except_table4360
- GCC_except_table4361
- GCC_except_table4391
- GCC_except_table4503
- GCC_except_table4510
- GCC_except_table4593
- GCC_except_table4660
- GCC_except_table4670
- GCC_except_table4726
- GCC_except_table4727
- GCC_except_table4728
- GCC_except_table4730
- GCC_except_table4731
- GCC_except_table4732
- GCC_except_table4733
- GCC_except_table4781
- GCC_except_table4847
- GCC_except_table4852
- GCC_except_table4893
- GCC_except_table4959
CStrings:
+ "%s Deferring SelfTap start for route '%{public}@' until first audio packet"
+ "%s User selected multiphrase but current Siri language does not support the compact trigger; treating as HS only"
+ "%s deactivate called before first audio packet, canceling deferred SelfTap start"
+ "-[CSAudioPowerProvider processAudioChunk:]"
+ "-[CSVoiceTriggerUserSelectedPhrase _isMultiPhrase:]"
+ "DeviceSupportsAlwaysListeningHeySiri"
+ "[originatingDeviceSupportsAlwaysListeningHeySiri = %d]"
+ "originatingDeviceSupportsAlwaysListeningHeySiri"
+ "recordType[%@] deviceId[%@] turnIdentifier[%@] alwaysUseBuiltInMic[%d] isRequestDuringActiveCall[%d] triggerEventInfo[%@] spokenNotification [%d] isTriggerless [%d] speechEvent [%ld] remoteDeviceInvocationType [%ld]"
+ "remoteDeviceInvocationType"
- "recordType[%@] deviceId[%@] turnIdentifier[%@] alwaysUseBuiltInMic[%d] isRequestDuringActiveCall[%d] triggerEventInfo[%@] spokenNotification [%d] isTriggerless [%d] speechEvent [%ld]"
```
