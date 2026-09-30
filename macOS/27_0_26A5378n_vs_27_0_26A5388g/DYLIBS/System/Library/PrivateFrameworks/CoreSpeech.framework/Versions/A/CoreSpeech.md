## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.70.20.4.1
-  __TEXT.__text: 0x13ba54
+3600.70.32.0.0
+  __TEXT.__text: 0x13bc94
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x13bd8
+  __TEXT.__objc_methlist: 0x13c38
   __TEXT.__const: 0x40c
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x30a4
   __TEXT.__cstring: 0x25071
-  __TEXT.__oslogstring: 0x1db84
+  __TEXT.__oslogstring: 0x1dbf4
   __TEXT.__unwind_info: 0x4a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x4a8
+  __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xa3b8
+  __DATA_CONST.__objc_selrefs: 0xa3f0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x1868
-  __AUTH_CONST.__const: 0x5830
+  __DATA_CONST.__got: 0x1870
+  __AUTH_CONST.__const: 0x5800
   __AUTH_CONST.__cfstring: 0x9120
-  __AUTH_CONST.__objc_const: 0x1f328
+  __AUTH_CONST.__objc_const: 0x1f3c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x900

   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xc10
+  __AUTH_CONST.__auth_got: 0xc18
   __AUTH.__objc_data: 0x39d0
-  __DATA.__objc_ivar: 0x17cc
-  __DATA.__data: 0x3774
+  __DATA.__objc_ivar: 0x17d4
+  __DATA.__data: 0x37d4
   __DATA.__bss: 0x5d0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x16d0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7682
-  Symbols:   16938
-  CStrings:  5133
+  Functions: 7688
+  Symbols:   16957
+  CStrings:  5135
 
Symbols:
+ -[CSSiriLauncher setShouldIgnoreLocalVoiceTriggerActivation:]
+ -[CSSiriLauncher shouldIgnoreLocalVoiceTriggerActivation]
+ -[CSSpeechManager _startRemoteAudioControllerIfNeeded]
+ -[CSSpeechManager remoteAudioController:didChangeReadiness:]
+ -[CSSpeechManager remoteAudioController]
+ -[CSSpeechManager setRemoteAudioController:]
+ GCC_except_table2291
+ GCC_except_table2336
+ GCC_except_table2341
+ GCC_except_table2348
+ GCC_except_table2366
+ GCC_except_table2396
+ GCC_except_table2501
+ GCC_except_table2560
+ GCC_except_table2572
+ GCC_except_table2603
+ GCC_except_table2628
+ GCC_except_table2639
+ GCC_except_table2674
+ GCC_except_table2675
+ GCC_except_table2676
+ GCC_except_table2681
+ GCC_except_table2691
+ GCC_except_table2692
+ GCC_except_table2701
+ GCC_except_table2707
+ GCC_except_table2709
+ GCC_except_table2710
+ GCC_except_table2738
+ GCC_except_table3006
+ GCC_except_table3080
+ GCC_except_table3117
+ GCC_except_table3144
+ GCC_except_table3147
+ GCC_except_table3150
+ GCC_except_table3181
+ GCC_except_table3241
+ GCC_except_table3435
+ GCC_except_table3461
+ GCC_except_table3523
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3554
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table3567
+ GCC_except_table3570
+ GCC_except_table3587
+ GCC_except_table3592
+ GCC_except_table3594
+ GCC_except_table3602
+ GCC_except_table3605
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3616
+ GCC_except_table3621
+ GCC_except_table3622
+ GCC_except_table3623
+ GCC_except_table3624
+ GCC_except_table3730
+ GCC_except_table3754
+ GCC_except_table3820
+ GCC_except_table3836
+ GCC_except_table3857
+ GCC_except_table3949
+ GCC_except_table4202
+ GCC_except_table4255
+ GCC_except_table4256
+ GCC_except_table4260
+ GCC_except_table4263
+ GCC_except_table4267
+ GCC_except_table4292
+ GCC_except_table4351
+ GCC_except_table4706
+ GCC_except_table4866
+ GCC_except_table4876
+ GCC_except_table4900
+ GCC_except_table4920
+ GCC_except_table5004
+ GCC_except_table5018
+ GCC_except_table5027
+ GCC_except_table5042
+ GCC_except_table5044
+ GCC_except_table5047
+ GCC_except_table5055
+ GCC_except_table5065
+ GCC_except_table5067
+ GCC_except_table5085
+ GCC_except_table5092
+ GCC_except_table5101
+ GCC_except_table5104
+ GCC_except_table5105
+ GCC_except_table5106
+ GCC_except_table5113
+ GCC_except_table5118
+ GCC_except_table5121
+ GCC_except_table5122
+ GCC_except_table5126
+ GCC_except_table5141
+ GCC_except_table5267
+ GCC_except_table5297
+ GCC_except_table5300
+ GCC_except_table5390
+ GCC_except_table5404
+ GCC_except_table5411
+ GCC_except_table5433
+ GCC_except_table5437
+ GCC_except_table5447
+ GCC_except_table5697
+ GCC_except_table5730
+ GCC_except_table5735
+ GCC_except_table5772
+ GCC_except_table5781
+ GCC_except_table5811
+ GCC_except_table5891
+ GCC_except_table6113
+ GCC_except_table6121
+ GCC_except_table6141
+ GCC_except_table6146
+ GCC_except_table6255
+ GCC_except_table6325
+ GCC_except_table6347
+ GCC_except_table6348
+ GCC_except_table6358
+ GCC_except_table6359
+ GCC_except_table6371
+ GCC_except_table6402
+ GCC_except_table6413
+ GCC_except_table6418
+ GCC_except_table6423
+ GCC_except_table6455
+ GCC_except_table6537
+ GCC_except_table6563
+ GCC_except_table6574
+ GCC_except_table6577
+ GCC_except_table6600
+ GCC_except_table6612
+ GCC_except_table6776
+ GCC_except_table6812
+ GCC_except_table6863
+ GCC_except_table6918
+ GCC_except_table6941
+ GCC_except_table6982
+ GCC_except_table6992
+ GCC_except_table7002
+ GCC_except_table7043
+ GCC_except_table7050
+ GCC_except_table7071
+ GCC_except_table7120
+ GCC_except_table7211
+ GCC_except_table7212
+ GCC_except_table7213
+ GCC_except_table7215
+ GCC_except_table7220
+ GCC_except_table7284
+ GCC_except_table7338
+ GCC_except_table7341
+ GCC_except_table7355
+ GCC_except_table7392
+ GCC_except_table7524
+ OBJC_IVAR_$_CSSiriLauncher._shouldIgnoreLocalVoiceTriggerActivation
+ OBJC_IVAR_$_CSSpeechManager._remoteAudioController
+ _CSIsWatchWithPHS
+ _OBJC_CLASS_$_CSRemoteAudioController
+ __OBJC_$_INSTANCE_VARIABLES_CSSiriLauncher
+ __OBJC_$_PROP_LIST_CSSiriLauncher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSRemoteAudioControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSRemoteAudioControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSRemoteAudioControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSRemoteAudioControllerDelegate
+ __OBJC_PROTOCOL_$_CSRemoteAudioControllerDelegate
+ _objc_msgSend$_startRemoteAudioControllerIfNeeded
+ _objc_msgSend$initWithProviderSelector:
+ _objc_msgSend$setShouldIgnoreLocalVoiceTriggerActivation:
- GCC_except_table2289
- GCC_except_table2334
- GCC_except_table2339
- GCC_except_table2346
- GCC_except_table2364
- GCC_except_table2392
- GCC_except_table2497
- GCC_except_table2556
- GCC_except_table2568
- GCC_except_table2599
- GCC_except_table2624
- GCC_except_table2635
- GCC_except_table2669
- GCC_except_table2670
- GCC_except_table2671
- GCC_except_table2672
- GCC_except_table2680
- GCC_except_table2683
- GCC_except_table2697
- GCC_except_table2703
- GCC_except_table2705
- GCC_except_table2706
- GCC_except_table2734
- GCC_except_table3002
- GCC_except_table3076
- GCC_except_table3113
- GCC_except_table3140
- GCC_except_table3143
- GCC_except_table3146
- GCC_except_table3177
- GCC_except_table3237
- GCC_except_table3431
- GCC_except_table3457
- GCC_except_table3519
- GCC_except_table3520
- GCC_except_table3522
- GCC_except_table3540
- GCC_except_table3542
- GCC_except_table3555
- GCC_except_table3563
- GCC_except_table3566
- GCC_except_table3573
- GCC_except_table3575
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3595
- GCC_except_table3596
- GCC_except_table3598
- GCC_except_table3612
- GCC_except_table3617
- GCC_except_table3618
- GCC_except_table3619
- GCC_except_table3620
- GCC_except_table3726
- GCC_except_table3750
- GCC_except_table3816
- GCC_except_table3832
- GCC_except_table3853
- GCC_except_table3945
- GCC_except_table4196
- GCC_except_table4249
- GCC_except_table4250
- GCC_except_table4254
- GCC_except_table4257
- GCC_except_table4261
- GCC_except_table4286
- GCC_except_table4339
- GCC_except_table4700
- GCC_except_table4860
- GCC_except_table4870
- GCC_except_table4894
- GCC_except_table4914
- GCC_except_table4998
- GCC_except_table5012
- GCC_except_table5021
- GCC_except_table5030
- GCC_except_table5038
- GCC_except_table5041
- GCC_except_table5049
- GCC_except_table5053
- GCC_except_table5061
- GCC_except_table5079
- GCC_except_table5086
- GCC_except_table5091
- GCC_except_table5093
- GCC_except_table5095
- GCC_except_table5098
- GCC_except_table5100
- GCC_except_table5107
- GCC_except_table5108
- GCC_except_table5112
- GCC_except_table5116
- GCC_except_table5135
- GCC_except_table5261
- GCC_except_table5291
- GCC_except_table5294
- GCC_except_table5384
- GCC_except_table5398
- GCC_except_table5405
- GCC_except_table5427
- GCC_except_table5431
- GCC_except_table5441
- GCC_except_table5685
- GCC_except_table5724
- GCC_except_table5729
- GCC_except_table5766
- GCC_except_table5775
- GCC_except_table5805
- GCC_except_table5885
- GCC_except_table6107
- GCC_except_table6115
- GCC_except_table6135
- GCC_except_table6140
- GCC_except_table6249
- GCC_except_table6319
- GCC_except_table6341
- GCC_except_table6342
- GCC_except_table6352
- GCC_except_table6353
- GCC_except_table6365
- GCC_except_table6396
- GCC_except_table6407
- GCC_except_table6412
- GCC_except_table6417
- GCC_except_table6449
- GCC_except_table6531
- GCC_except_table6557
- GCC_except_table6568
- GCC_except_table6571
- GCC_except_table6594
- GCC_except_table6606
- GCC_except_table6770
- GCC_except_table6806
- GCC_except_table6857
- GCC_except_table6912
- GCC_except_table6935
- GCC_except_table6976
- GCC_except_table6986
- GCC_except_table6996
- GCC_except_table7037
- GCC_except_table7044
- GCC_except_table7065
- GCC_except_table7114
- GCC_except_table7205
- GCC_except_table7206
- GCC_except_table7207
- GCC_except_table7208
- GCC_except_table7209
- GCC_except_table7278
- GCC_except_table7326
- GCC_except_table7335
- GCC_except_table7343
- GCC_except_table7374
- GCC_except_table7518
- ___block_descriptor_48_e8_32s40w_e11_v20?0B8Q12l
CStrings:
+ "%s scdaContext = %@"
+ "%s voiceTriggerInfo[\"%@\"] was not set, scdaContext will not have a value for this property."
```
