## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3304.82.8.1.2
-  __TEXT.__text: 0x7fbe0
+3305.27.1.0.0
+  __TEXT.__text: 0x80904
   __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x7a38
+  __TEXT.__objc_methlist: 0x7ac8
   __TEXT.__const: 0x388
-  __TEXT.__gcc_except_tab: 0x1a70
-  __TEXT.__cstring: 0xcdf5
-  __TEXT.__oslogstring: 0x9b4f
+  __TEXT.__gcc_except_tab: 0x1a84
+  __TEXT.__cstring: 0xd025
+  __TEXT.__oslogstring: 0x9c3b
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0x2148
+  __TEXT.__unwind_info: 0x215c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x112e
-  __TEXT.__objc_methname: 0x17f49
-  __TEXT.__objc_methtype: 0x3521
-  __TEXT.__objc_stubs: 0xcca0
+  __TEXT.__objc_methname: 0x18129
+  __TEXT.__objc_methtype: 0x3524
+  __TEXT.__objc_stubs: 0xcd60
   __DATA_CONST.__got: 0x308
   __DATA_CONST.__const: 0x14e8
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xcba0
-  __DATA_CONST.__objc_selrefs: 0x4e80
+  __DATA_CONST.__objc_const: 0xcbb0
+  __DATA_CONST.__objc_selrefs: 0x4ee8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x7b0
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__const: 0xe60
+  __AUTH_CONST.__const: 0xea0
   __AUTH_CONST.__objc_const: 0x34e0
-  __AUTH_CONST.__cfstring: 0x63a0
+  __AUTH_CONST.__cfstring: 0x6480
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x150
   __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x1310
+  __AUTH.__objc_data: 0x10e0
   __DATA.__objc_ivar: 0x918
-  __DATA.__data: 0xc28
-  __DATA.__common: 0x8
-  __DATA.__bss: 0x530
-  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA.__data: 0xc50
+  __DATA.__bss: 0x4b0
+  __DATA_DIRTY.__objc_data: 0x19f0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__bss: 0x2f8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8264FD18-4F6B-37B5-9C8C-0DB1FB33CDAB
-  Functions: 3138
-  Symbols:   11010
-  CStrings:  7099
+  UUID: 9BB25532-10A2-3300-8F68-65A6042733C7
+  Functions: 3154
+  Symbols:   11054
+  CStrings:  7142
 
Symbols:
+ +[CSConfig exclaveHALInputNumChannelsWithDSP]
+ +[CSConfig exclaveHALInputNumChannelsWithoutDSP]
+ +[CSUtils isFirstPassSourceTypeRingtoneWithVTEI:]
+ +[CSUtils isSiriDSPTurnedOn]
+ +[CSUtils isVoiceTriggerFromExclaveWithVTEI:]
+ -[CSAudioTimeConverterPool defaultExclaveConverter]
+ -[CSAudioTimeConverterPool exclaveTimeConverter]
+ -[CSAudioTimeConverterPool setExclaveTimeConverter:]
+ -[CSExclaveRecordClient configAOPVoiceTrigger]
+ -[CSExclaveRecordClient fetchAOPVoiceTriggerResult:]
+ -[CSExclaveRecordClient startSecondPassVoiceTriggerWithFirstPassSource:phsEnabled:supportMultiPhrase:]
+ -[CSFPreferences enableExclaveAudioInjection:]
+ -[CSFPreferences exclaveAudioInjectionEnabled]
+ GCC_except_table1301
+ GCC_except_table1302
+ GCC_except_table1305
+ GCC_except_table1310
+ GCC_except_table1313
+ GCC_except_table1314
+ GCC_except_table1317
+ GCC_except_table1318
+ GCC_except_table1319
+ GCC_except_table1330
+ GCC_except_table1334
+ GCC_except_table1339
+ GCC_except_table1341
+ GCC_except_table1342
+ GCC_except_table1355
+ GCC_except_table140
+ GCC_except_table1413
+ GCC_except_table1476
+ GCC_except_table1508
+ GCC_except_table1509
+ GCC_except_table1513
+ GCC_except_table1520
+ GCC_except_table1521
+ GCC_except_table1612
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table1742
+ GCC_except_table1746
+ GCC_except_table1817
+ GCC_except_table1828
+ GCC_except_table1830
+ GCC_except_table1835
+ GCC_except_table1837
+ GCC_except_table1850
+ GCC_except_table1857
+ GCC_except_table1859
+ GCC_except_table1877
+ GCC_except_table1898
+ GCC_except_table1989
+ GCC_except_table1991
+ GCC_except_table1992
+ GCC_except_table2110
+ GCC_except_table2231
+ GCC_except_table2246
+ GCC_except_table2251
+ GCC_except_table2253
+ GCC_except_table2255
+ GCC_except_table2259
+ GCC_except_table2279
+ GCC_except_table2334
+ GCC_except_table2338
+ GCC_except_table2407
+ GCC_except_table2437
+ GCC_except_table2438
+ GCC_except_table2439
+ GCC_except_table2440
+ GCC_except_table2462
+ GCC_except_table2525
+ GCC_except_table258
+ GCC_except_table2594
+ GCC_except_table2595
+ GCC_except_table2597
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table261
+ GCC_except_table266
+ GCC_except_table2716
+ GCC_except_table2717
+ GCC_except_table2725
+ GCC_except_table2730
+ GCC_except_table2739
+ GCC_except_table2742
+ GCC_except_table2743
+ GCC_except_table2747
+ GCC_except_table2748
+ GCC_except_table2749
+ GCC_except_table2754
+ GCC_except_table2756
+ GCC_except_table2760
+ GCC_except_table2761
+ GCC_except_table2779
+ GCC_except_table2783
+ GCC_except_table2876
+ GCC_except_table2883
+ GCC_except_table2925
+ GCC_except_table2978
+ GCC_except_table2983
+ GCC_except_table3029
+ GCC_except_table3118
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table494
+ GCC_except_table501
+ GCC_except_table546
+ GCC_except_table548
+ GCC_except_table555
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table577
+ GCC_except_table582
+ GCC_except_table589
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table601
+ GCC_except_table875
+ GCC_except_table972
+ GCC_except_table981
+ GCC_except_table983
+ GCC_except_table985
+ GCC_except_table986
+ GCC_except_table987
+ GCC_except_table998
+ _AudioConverterFillComplexBuffer_BlockInvoke.4014
+ _OBJC_IVAR_$_CSAudioTimeConverterPool._exclaveTimeConverter
+ __CSNotBackedupPreferencesValueForKeyFromRoot
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5490
+ __OBJC_$_PROP_LIST_NSObject.1263
+ __OBJC_$_PROP_LIST_NSObject.1399
+ __OBJC_$_PROP_LIST_NSObject.2239
+ __OBJC_$_PROP_LIST_NSObject.2696
+ __OBJC_$_PROP_LIST_NSObject.3111
+ __OBJC_$_PROP_LIST_NSObject.4156
+ __OBJC_$_PROP_LIST_NSObject.4499
+ __OBJC_$_PROP_LIST_NSObject.5336
+ __OBJC_$_PROP_LIST_NSObject.5947
+ __OBJC_$_PROP_LIST_NSObject.6227
+ __OBJC_$_PROP_LIST_NSObject.7060
+ __OBJC_$_PROP_LIST_NSObject.7446
+ __OBJC_$_PROP_LIST_NSObject.8338
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5491
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.8339
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.5948
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFModelComputeBackend.7061
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5492
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2001
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2381
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3506
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.530
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5493
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6871
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8727
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1264
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1400
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2240
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2697
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3112
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4157
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4500
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5337
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5949
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6228
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7062
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7447
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8340
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.5950
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1265
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1401
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2241
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2698
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3113
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4158
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4501
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5338
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5951
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6229
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7063
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7448
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8341
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.8342
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.5952
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFModelComputeBackend.7064
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5494
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2002
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2382
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3507
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.531
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5495
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6872
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8728
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1266
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1402
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2242
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2699
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3114
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4159
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4502
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5339
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5953
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6230
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7065
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7449
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8343
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5496
+ __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.8344
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.5954
+ __OBJC_$_PROTOCOL_REFS_CSFModelComputeBackend.7066
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5497
+ ___24-[CSAudioProvider start]_block_invoke.52
+ ___28+[CSUtils isExclaveHardware]_block_invoke
+ ___46-[CSFPreferences exclaveAudioInjectionEnabled]_block_invoke
+ ___51-[CSAudioTimeConverterPool defaultExclaveConverter]_block_invoke
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.105
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.110
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.113
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.99
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.106
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.111
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.112
+ ___54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.79
+ ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.98
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.80
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.83
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.86
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.91
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.94
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.84
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.92
+ ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.135
+ ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.125
+ ___Block_byref_object_copy_.1250
+ ___Block_byref_object_copy_.1427
+ ___Block_byref_object_copy_.1895
+ ___Block_byref_object_copy_.2586
+ ___Block_byref_object_copy_.2712
+ ___Block_byref_object_copy_.3310
+ ___Block_byref_object_copy_.4378
+ ___Block_byref_object_copy_.4889
+ ___Block_byref_object_copy_.5544
+ ___Block_byref_object_copy_.7385
+ ___Block_byref_object_copy_.7589
+ ___Block_byref_object_copy_.7843
+ ___Block_byref_object_copy_.8213
+ ___Block_byref_object_copy_.8293
+ ___Block_byref_object_copy_.847
+ ___Block_byref_object_copy_.8867
+ ___Block_byref_object_dispose_.1251
+ ___Block_byref_object_dispose_.1428
+ ___Block_byref_object_dispose_.1896
+ ___Block_byref_object_dispose_.2587
+ ___Block_byref_object_dispose_.2713
+ ___Block_byref_object_dispose_.3311
+ ___Block_byref_object_dispose_.4379
+ ___Block_byref_object_dispose_.4890
+ ___Block_byref_object_dispose_.5545
+ ___Block_byref_object_dispose_.7386
+ ___Block_byref_object_dispose_.7590
+ ___Block_byref_object_dispose_.7844
+ ___Block_byref_object_dispose_.8214
+ ___Block_byref_object_dispose_.8294
+ ___Block_byref_object_dispose_.848
+ ___Block_byref_object_dispose_.8868
+ ___block_literal_global.1247
+ ___block_literal_global.1301
+ ___block_literal_global.1435
+ ___block_literal_global.146
+ ___block_literal_global.1512
+ ___block_literal_global.1543
+ ___block_literal_global.1752
+ ___block_literal_global.1915
+ ___block_literal_global.2084
+ ___block_literal_global.2200
+ ___block_literal_global.253
+ ___block_literal_global.2613
+ ___block_literal_global.2736
+ ___block_literal_global.307
+ ___block_literal_global.334
+ ___block_literal_global.345
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.3827
+ ___block_literal_global.394
+ ___block_literal_global.396
+ ___block_literal_global.3980
+ ___block_literal_global.419
+ ___block_literal_global.421
+ ___block_literal_global.432
+ ___block_literal_global.432.4690
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.450
+ ___block_literal_global.454
+ ___block_literal_global.461
+ ___block_literal_global.466
+ ___block_literal_global.471
+ ___block_literal_global.474
+ ___block_literal_global.476
+ ___block_literal_global.4805
+ ___block_literal_global.485
+ ___block_literal_global.486
+ ___block_literal_global.495
+ ___block_literal_global.500
+ ___block_literal_global.502
+ ___block_literal_global.506
+ ___block_literal_global.513
+ ___block_literal_global.5163
+ ___block_literal_global.5224
+ ___block_literal_global.525
+ ___block_literal_global.530
+ ___block_literal_global.5307
+ ___block_literal_global.5348
+ ___block_literal_global.535
+ ___block_literal_global.5397
+ ___block_literal_global.540
+ ___block_literal_global.548
+ ___block_literal_global.5569
+ ___block_literal_global.572
+ ___block_literal_global.576
+ ___block_literal_global.578
+ ___block_literal_global.580
+ ___block_literal_global.5806
+ ___block_literal_global.583
+ ___block_literal_global.589
+ ___block_literal_global.591
+ ___block_literal_global.594
+ ___block_literal_global.596
+ ___block_literal_global.599
+ ___block_literal_global.614
+ ___block_literal_global.645
+ ___block_literal_global.654
+ ___block_literal_global.656
+ ___block_literal_global.659
+ ___block_literal_global.756
+ ___block_literal_global.7682
+ ___block_literal_global.779
+ ___block_literal_global.794
+ ___block_literal_global.8094
+ ___block_literal_global.822
+ ___block_literal_global.8236
+ ___block_literal_global.8440
+ ___block_literal_global.8556
+ ___block_literal_global.874
+ ___block_literal_global.8891
+ __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat.554
+ __unnamed_array_storage.635
+ __unnamed_array_storage.7001
+ __unnamed_array_storage.8085
+ _exclaveAudioInjectionEnabled.enabled
+ _exclaveAudioInjectionEnabled.onceToken
+ _isExclaveHardware.isExclaveHardware
+ _isExclaveHardware.onceToken
+ _objc_msgSend$configAOPVoiceTrigger
+ _objc_msgSend$defaultExclaveConverter
+ _objc_msgSend$exclaveHALInputNumChannelsWithDSP
+ _objc_msgSend$exclaveHALInputNumChannelsWithoutDSP
+ _objc_msgSend$fetchAOPVoiceTriggerResult:
+ _objc_msgSend$isSiriDSPTurnedOn
+ _objc_msgSend$prepare:
+ _objc_msgSend$startSecondPassVoiceTriggerWithFirstPassSource:pHSEnabled:supportMultiPhrase:
+ _sharedInstance.onceToken.1300
+ _sharedInstance.onceToken.1434
+ _sharedInstance.onceToken.145
+ _sharedInstance.onceToken.1914
+ _sharedInstance.onceToken.2199
+ _sharedInstance.onceToken.2612
+ _sharedInstance.onceToken.2735
+ _sharedInstance.onceToken.5223
+ _sharedInstance.onceToken.5347
+ _sharedInstance.onceToken.5396
+ _sharedInstance.onceToken.5805
+ _sharedInstance.onceToken.821
+ _sharedInstance.onceToken.8439
+ _sharedInstance.onceToken.8555
+ _sharedInstance.onceToken.873
+ _sharedInstance.onceToken.8890
+ _sharedInstance.sharedInstance.1302
+ _sharedInstance.sharedInstance.1436
+ _sharedInstance.sharedInstance.147
+ _sharedInstance.sharedInstance.1916
+ _sharedInstance.sharedInstance.2201
+ _sharedInstance.sharedInstance.2737
+ _sharedInstance.sharedInstance.5225
+ _sharedInstance.sharedInstance.5349
+ _sharedInstance.sharedInstance.5398
+ _sharedInstance.sharedInstance.8441
+ _sharedInstance.sharedInstance.8892
+ _sharedLogger.onceToken.1511
+ _sharedLogger.onceToken.3826
+ _sharedPreferences.onceToken.5162
- -[CSExclaveRecordClient startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:]
- GCC_except_table1291
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1294
- GCC_except_table1295
- GCC_except_table1299
- GCC_except_table1300
- GCC_except_table1307
- GCC_except_table1308
- GCC_except_table1320
- GCC_except_table1324
- GCC_except_table1329
- GCC_except_table1331
- GCC_except_table1332
- GCC_except_table1345
- GCC_except_table136
- GCC_except_table1403
- GCC_except_table1466
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1501
- GCC_except_table1503
- GCC_except_table1510
- GCC_except_table1600
- GCC_except_table162
- GCC_except_table163
- GCC_except_table164
- GCC_except_table165
- GCC_except_table1730
- GCC_except_table1734
- GCC_except_table1805
- GCC_except_table1816
- GCC_except_table1818
- GCC_except_table1823
- GCC_except_table1825
- GCC_except_table1838
- GCC_except_table1845
- GCC_except_table1847
- GCC_except_table1865
- GCC_except_table1886
- GCC_except_table1977
- GCC_except_table1979
- GCC_except_table1980
- GCC_except_table2098
- GCC_except_table2207
- GCC_except_table2215
- GCC_except_table2230
- GCC_except_table2235
- GCC_except_table2237
- GCC_except_table2243
- GCC_except_table2263
- GCC_except_table2318
- GCC_except_table2322
- GCC_except_table2391
- GCC_except_table2421
- GCC_except_table2422
- GCC_except_table2423
- GCC_except_table2424
- GCC_except_table2446
- GCC_except_table2509
- GCC_except_table254
- GCC_except_table2569
- GCC_except_table257
- GCC_except_table2578
- GCC_except_table2579
- GCC_except_table2581
- GCC_except_table2584
- GCC_except_table2586
- GCC_except_table262
- GCC_except_table2700
- GCC_except_table2701
- GCC_except_table2708
- GCC_except_table2709
- GCC_except_table2710
- GCC_except_table2711
- GCC_except_table2713
- GCC_except_table2714
- GCC_except_table2723
- GCC_except_table2731
- GCC_except_table2732
- GCC_except_table2733
- GCC_except_table2738
- GCC_except_table2744
- GCC_except_table2763
- GCC_except_table2767
- GCC_except_table2860
- GCC_except_table2867
- GCC_except_table2909
- GCC_except_table2946
- GCC_except_table2967
- GCC_except_table3013
- GCC_except_table3102
- GCC_except_table331
- GCC_except_table337
- GCC_except_table342
- GCC_except_table344
- GCC_except_table490
- GCC_except_table497
- GCC_except_table542
- GCC_except_table544
- GCC_except_table551
- GCC_except_table566
- GCC_except_table567
- GCC_except_table568
- GCC_except_table573
- GCC_except_table574
- GCC_except_table575
- GCC_except_table585
- GCC_except_table597
- GCC_except_table867
- GCC_except_table964
- GCC_except_table973
- GCC_except_table975
- GCC_except_table976
- GCC_except_table977
- GCC_except_table988
- _AudioConverterFillComplexBuffer_BlockInvoke.3977
- _OBJC_IVAR_$_CSEventMonitor._observersChangeLock
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.5561
- __OBJC_$_PROP_LIST_NSObject.1258
- __OBJC_$_PROP_LIST_NSObject.1395
- __OBJC_$_PROP_LIST_NSObject.2188
- __OBJC_$_PROP_LIST_NSObject.2647
- __OBJC_$_PROP_LIST_NSObject.3061
- __OBJC_$_PROP_LIST_NSObject.4119
- __OBJC_$_PROP_LIST_NSObject.4553
- __OBJC_$_PROP_LIST_NSObject.5407
- __OBJC_$_PROP_LIST_NSObject.6032
- __OBJC_$_PROP_LIST_NSObject.6312
- __OBJC_$_PROP_LIST_NSObject.7149
- __OBJC_$_PROP_LIST_NSObject.7536
- __OBJC_$_PROP_LIST_NSObject.8430
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.5562
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.8431
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.6033
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFModelComputeBackend.7150
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.5563
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1953
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2330
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3464
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.523
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5564
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.6960
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.8821
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1259
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1396
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2189
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2648
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3062
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4120
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4554
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5408
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6034
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7151
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7537
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8432
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.6035
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1260
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1397
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2190
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2649
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3063
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4121
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4555
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5409
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6036
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6314
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7152
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7538
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8433
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.8434
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.6037
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSFModelComputeBackend.7153
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.5565
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1954
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2331
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3465
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.524
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5566
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.6961
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.8822
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1261
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1398
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2191
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2650
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3064
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4122
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4556
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5410
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6038
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6315
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7154
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7539
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8435
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.5567
- __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.8436
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.6039
- __OBJC_$_PROTOCOL_REFS_CSFModelComputeBackend.7155
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.5568
- ___24-[CSAudioProvider start]_block_invoke.53
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.104
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.109
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.112
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.98
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.105
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.110
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.111
- ___54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.80
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.96
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.82
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.84
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.93
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.85
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.91
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_3
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_4
- ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.134
- ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.124
- ___Block_byref_object_copy_.1246
- ___Block_byref_object_copy_.1423
- ___Block_byref_object_copy_.1861
- ___Block_byref_object_copy_.2537
- ___Block_byref_object_copy_.2663
- ___Block_byref_object_copy_.3260
- ___Block_byref_object_copy_.4408
- ___Block_byref_object_copy_.4964
- ___Block_byref_object_copy_.5616
- ___Block_byref_object_copy_.7475
- ___Block_byref_object_copy_.7680
- ___Block_byref_object_copy_.7933
- ___Block_byref_object_copy_.8305
- ___Block_byref_object_copy_.838
- ___Block_byref_object_copy_.8385
- ___Block_byref_object_copy_.8959
- ___Block_byref_object_dispose_.1247
- ___Block_byref_object_dispose_.1424
- ___Block_byref_object_dispose_.1862
- ___Block_byref_object_dispose_.2538
- ___Block_byref_object_dispose_.2664
- ___Block_byref_object_dispose_.3261
- ___Block_byref_object_dispose_.4409
- ___Block_byref_object_dispose_.4965
- ___Block_byref_object_dispose_.5617
- ___Block_byref_object_dispose_.7476
- ___Block_byref_object_dispose_.7681
- ___Block_byref_object_dispose_.7934
- ___Block_byref_object_dispose_.8306
- ___Block_byref_object_dispose_.8386
- ___Block_byref_object_dispose_.839
- ___Block_byref_object_dispose_.8960
- ___block_literal_global.102
- ___block_literal_global.107
- ___block_literal_global.112
- ___block_literal_global.117
- ___block_literal_global.1243
- ___block_literal_global.1297
- ___block_literal_global.1432
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.1509
- ___block_literal_global.153
- ___block_literal_global.1540
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.166
- ___block_literal_global.168
- ___block_literal_global.171
- ___block_literal_global.1710
- ___block_literal_global.173
- ___block_literal_global.176
- ___block_literal_global.1881
- ___block_literal_global.191
- ___block_literal_global.20
- ___block_literal_global.2033
- ___block_literal_global.2149
- ___block_literal_global.22
- ___block_literal_global.222
- ___block_literal_global.227.4776
- ___block_literal_global.229
- ___block_literal_global.2564
- ___block_literal_global.2687
- ___block_literal_global.27
- ___block_literal_global.287
- ___block_literal_global.319
- ___block_literal_global.335
- ___block_literal_global.354
- ___block_literal_global.364
- ___block_literal_global.376
- ___block_literal_global.3790
- ___block_literal_global.38
- ___block_literal_global.384
- ___block_literal_global.391
- ___block_literal_global.3943
- ___block_literal_global.399
- ___block_literal_global.415
- ___block_literal_global.422
- ___block_literal_global.429
- ___block_literal_global.43
- ___block_literal_global.464
- ___block_literal_global.48
- ___block_literal_global.480
- ___block_literal_global.4880
- ___block_literal_global.5238
- ___block_literal_global.5299
- ___block_literal_global.53
- ___block_literal_global.5378
- ___block_literal_global.541
- ___block_literal_global.5419
- ___block_literal_global.5468
- ___block_literal_global.5641
- ___block_literal_global.5891
- ___block_literal_global.63
- ___block_literal_global.72
- ___block_literal_global.747
- ___block_literal_global.77
- ___block_literal_global.770
- ___block_literal_global.7772
- ___block_literal_global.79
- ___block_literal_global.813
- ___block_literal_global.8186
- ___block_literal_global.83
- ___block_literal_global.8328
- ___block_literal_global.8531
- ___block_literal_global.8647
- ___block_literal_global.865
- ___block_literal_global.8983
- ___block_literal_global.9
- ___block_literal_global.90
- __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat.539
- __unnamed_array_storage.212
- __unnamed_array_storage.7090
- __unnamed_array_storage.8177
- _objc_msgSend$prepare
- _objc_msgSend$startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:
- _sharedInstance.onceToken.1296
- _sharedInstance.onceToken.1431
- _sharedInstance.onceToken.146
- _sharedInstance.onceToken.1880
- _sharedInstance.onceToken.2148
- _sharedInstance.onceToken.2563
- _sharedInstance.onceToken.2686
- _sharedInstance.onceToken.5298
- _sharedInstance.onceToken.5418
- _sharedInstance.onceToken.5467
- _sharedInstance.onceToken.5890
- _sharedInstance.onceToken.812
- _sharedInstance.onceToken.8530
- _sharedInstance.onceToken.864
- _sharedInstance.onceToken.8646
- _sharedInstance.onceToken.8982
- _sharedInstance.sharedInstance.1298
- _sharedInstance.sharedInstance.1433
- _sharedInstance.sharedInstance.148
- _sharedInstance.sharedInstance.1882
- _sharedInstance.sharedInstance.2150
- _sharedInstance.sharedInstance.2688
- _sharedInstance.sharedInstance.5300
- _sharedInstance.sharedInstance.5420
- _sharedInstance.sharedInstance.5469
- _sharedInstance.sharedInstance.8532
- _sharedInstance.sharedInstance.8984
- _sharedLogger.onceToken.1508
- _sharedLogger.onceToken.3789
- _sharedPreferences.onceToken.5237
CStrings:
+ "%s Exclave Audio Injection is only available on internal builds"
+ "%s Failed to config AOP VoiceTrigger"
+ "%s Set LastFetchedExclaveAudioSampleCount = %llu"
+ "%s isExclaveCapable: %{public}@, isExclaveDriverAvailableHardwarePlatform: %{public}@"
+ "+[CSUtils isExclaveHardware]_block_invoke"
+ "-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2"
+ "-[CSExclaveRecordClient configAOPVoiceTrigger]"
+ "-[CSExclaveRecordClient fetchAOPVoiceTriggerResult:]"
+ "-[CSFPreferences enableExclaveAudioInjection:]"
+ "-[CSFPreferences exclaveAudioInjectionEnabled]_block_invoke"
+ "ApplicationProcessorExclave"
+ "ApplicationProcessorExclaveWithConnectedCall"
+ "ApplicationProcessorExclaveWithRingtone"
+ "AudioHAL"
+ "BuiltInAlwaysOnProcessorExclave"
+ "Conclaves"
+ "Exclave Audio Injection Enabled"
+ "ExclaveCapability"
+ "Load_ADM_DSP_Lib"
+ "T@\"CSAudioTimeConverter\",&,N,V_exclaveTimeConverter"
+ "_exclaveTimeConverter"
+ "com_apple_audiomxd_conclave"
+ "com_apple_corespeechd_conclave"
+ "configAOPVoiceTrigger"
+ "defaultExclaveConverter"
+ "enableExclaveAudioInjection:"
+ "exclaveAudioInjectionEnabled"
+ "exclaveHALInputNumChannelsWithDSP"
+ "exclaveHALInputNumChannelsWithoutDSP"
+ "exclaveTimeConverter"
+ "fetchAOPVoiceTriggerResult:"
+ "isFirstPassSourceTypeRingtoneWithVTEI:"
+ "isSiriDSPTurnedOn"
+ "isVoiceTriggerFromExclaveWithVTEI:"
+ "prepare:"
+ "setExclaveTimeConverter:"
+ "startSecondPassVoiceTriggerWithFirstPassSource:pHSEnabled:supportMultiPhrase:"
+ "startSecondPassVoiceTriggerWithFirstPassSource:phsEnabled:supportMultiPhrase:"
+ "support_medina"
+ "t8132"
+ "v32@0:8Q16B24B28"
- "-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_4"
- "_observersChangeLock"
- "prepare"
- "startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:"
- "v24@0:8B16B20"

```
