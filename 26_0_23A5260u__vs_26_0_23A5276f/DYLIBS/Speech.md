## Speech

> `/System/Library/Frameworks/Speech.framework/Speech`

```diff

-3500.86.2.1.1
-  __TEXT.__text: 0x1cdaf4
-  __TEXT.__auth_stubs: 0x2b40
-  __TEXT.__objc_methlist: 0x458c
-  __TEXT.__const: 0xc818
-  __TEXT.__cstring: 0xa6aa
-  __TEXT.__constg_swiftt: 0x4428
-  __TEXT.__swift5_typeref: 0x62b8
+3500.93.1.0.0
+  __TEXT.__text: 0x1d0dd4
+  __TEXT.__auth_stubs: 0x2ba0
+  __TEXT.__objc_methlist: 0x45d4
+  __TEXT.__const: 0xc858
+  __TEXT.__cstring: 0xa851
+  __TEXT.__constg_swiftt: 0x4430
+  __TEXT.__swift5_typeref: 0x62ac
   __TEXT.__swift5_reflstr: 0x4575
   __TEXT.__swift5_fieldmd: 0x39cc
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x9c0
   __TEXT.__swift5_proto: 0x864
   __TEXT.__swift5_types: 0x358
-  __TEXT.__oslogstring: 0x3ef8
-  __TEXT.__swift5_capture: 0x26cc
+  __TEXT.__oslogstring: 0x3f77
+  __TEXT.__swift5_capture: 0x26c4
   __TEXT.__swift5_acfuncs: 0x564
-  __TEXT.__swift_as_entry: 0x9d8
-  __TEXT.__swift_as_ret: 0x9dc
+  __TEXT.__swift_as_entry: 0x9fc
+  __TEXT.__swift_as_ret: 0xa0c
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x868
-  __TEXT.__unwind_info: 0x8a28
-  __TEXT.__eh_frame: 0x11d10
+  __TEXT.__unwind_info: 0x8ae8
+  __TEXT.__eh_frame: 0x120c0
   __TEXT.__objc_classname: 0xadc
-  __TEXT.__objc_methname: 0xe159
+  __TEXT.__objc_methname: 0xe23e
   __TEXT.__objc_methtype: 0x2a3d
-  __TEXT.__objc_stubs: 0x4e00
+  __TEXT.__objc_stubs: 0x4e60
   __DATA_CONST.__got: 0xd70
-  __DATA_CONST.__const: 0x1440
+  __DATA_CONST.__const: 0x1428
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b88
+  __DATA_CONST.__objc_selrefs: 0x2bb8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x15b0
-  __AUTH_CONST.__const: 0xbc70
-  __AUTH_CONST.__cfstring: 0x3e00
-  __AUTH_CONST.__objc_const: 0xccf0
+  __AUTH_CONST.__auth_got: 0x15e0
+  __AUTH_CONST.__const: 0xbcb0
+  __AUTH_CONST.__cfstring: 0x3f20
+  __AUTH_CONST.__objc_const: 0xcd20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x1540
   __AUTH.__data: 0x2990
-  __DATA.__objc_ivar: 0x570
+  __DATA.__objc_ivar: 0x574
   __DATA.__data: 0x3988
   __DATA.__common: 0x300
-  __DATA.__bss: 0xdc70
+  __DATA.__bss: 0xdc80
   __DATA_DIRTY.__objc_data: 0xf08
   __DATA_DIRTY.__data: 0x2b18
-  __DATA_DIRTY.__bss: 0x4e0
+  __DATA_DIRTY.__bss: 0x4d9
   __DATA_DIRTY.__common: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics
   - /System/Library/PrivateFrameworks/AlgorithmsInternal.framework/AlgorithmsInternal
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EBFA006F-55AB-32F8-AC4F-EF905AAF5183
-  Functions: 12605
-  Symbols:   14448
-  CStrings:  4423
+  UUID: 228E4992-6BA6-3B90-8985-33E7C279C186
+  Functions: 12658
+  Symbols:   14554
+  CStrings:  4455
 
Symbols:
+ +[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:]
+ +[SFPersonaManager isCurrentPersonaDefault]
+ +[SFUtilities hasSPIAccess]
+ +[SFUtilities sandboxExtensionsForCustomLmConfig:]
+ -[SFSpeechLanguageModelConfiguration initWithLanguageModel:vocabulary:weight:]
+ -[SFSpeechLanguageModelConfiguration weight]
+ GCC_except_table1032
+ GCC_except_table1057
+ GCC_except_table1060
+ GCC_except_table1143
+ GCC_except_table1164
+ GCC_except_table1350
+ GCC_except_table1359
+ GCC_except_table1365
+ GCC_except_table1378
+ GCC_except_table1379
+ GCC_except_table1380
+ GCC_except_table1381
+ GCC_except_table1382
+ GCC_except_table1385
+ GCC_except_table267
+ GCC_except_table396
+ GCC_except_table400
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table424
+ GCC_except_table444
+ GCC_except_table470
+ GCC_except_table474
+ GCC_except_table511
+ GCC_except_table759
+ GCC_except_table864
+ GCC_except_table898
+ GCC_except_table906
+ GCC_except_table908
+ GCC_except_table910
+ GCC_except_table919
+ GCC_except_table960
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _OBJC_IVAR_$_SFSpeechLanguageModelConfiguration._weight
+ _OUTLINED_FUNCTION_634
+ _OUTLINED_FUNCTION_635
+ _OUTLINED_FUNCTION_636
+ _OUTLINED_FUNCTION_637
+ _OUTLINED_FUNCTION_638
+ _OUTLINED_FUNCTION_639
+ _OUTLINED_FUNCTION_640
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ ___27+[SFUtilities hasSPIAccess]_block_invoke
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.510
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.511
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke_2.508
+ ___72-[SFSpeechRecognitionTask dictationConnection:speechRecognitionDidFail:]_block_invoke
+ ___81-[SFSpeechRecognitionTask localSpeechRecognitionClient:speechRecognitionDidFail:]_block_invoke
+ ___97+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_.1557
+ ___Block_byref_object_copy_.1718
+ ___Block_byref_object_copy_.1839
+ ___Block_byref_object_copy_.2165
+ ___Block_byref_object_copy_.2428
+ ___Block_byref_object_copy_.3034
+ ___Block_byref_object_copy_.658
+ ___Block_byref_object_dispose_.1558
+ ___Block_byref_object_dispose_.1719
+ ___Block_byref_object_dispose_.1840
+ ___Block_byref_object_dispose_.2166
+ ___Block_byref_object_dispose_.2429
+ ___Block_byref_object_dispose_.3035
+ ___Block_byref_object_dispose_.659
+ ___block_literal_global.1580
+ ___block_literal_global.1737
+ ___block_literal_global.2116
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.2460
+ ___block_literal_global.2836
+ ___block_literal_global.3087
+ ___block_literal_global.360
+ ___block_literal_global.381
+ ___block_literal_global.399
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.436
+ ___block_literal_global.444
+ ___block_literal_global.459
+ ___block_literal_global.460
+ ___block_literal_global.720
+ ___block_literal_global.964
+ _block_copy_helper.104
+ _block_copy_helper.110
+ _block_copy_helper.115
+ _block_copy_helper.122
+ _block_copy_helper.134
+ _block_copy_helper.140
+ _block_copy_helper.152
+ _block_copy_helper.158
+ _block_copy_helper.166
+ _block_copy_helper.175
+ _block_copy_helper.181
+ _block_copy_helper.196
+ _block_copy_helper.208
+ _block_copy_helper.215
+ _block_copy_helper.23
+ _block_copy_helper.242
+ _block_copy_helper.253
+ _block_copy_helper.264
+ _block_copy_helper.275
+ _block_copy_helper.28
+ _block_copy_helper.282
+ _block_copy_helper.298
+ _block_copy_helper.309
+ _block_copy_helper.326
+ _block_copy_helper.33
+ _block_copy_helper.343
+ _block_copy_helper.350
+ _block_copy_helper.366
+ _block_copy_helper.377
+ _block_copy_helper.387
+ _block_copy_helper.39
+ _block_copy_helper.394
+ _block_copy_helper.410
+ _block_copy_helper.42
+ _block_copy_helper.422
+ _block_copy_helper.432
+ _block_copy_helper.439
+ _block_copy_helper.455
+ _block_copy_helper.466
+ _block_copy_helper.477
+ _block_copy_helper.488
+ _block_copy_helper.499
+ _block_copy_helper.510
+ _block_copy_helper.521
+ _block_copy_helper.532
+ _block_copy_helper.542
+ _block_copy_helper.549
+ _block_copy_helper.56
+ _block_copy_helper.566
+ _block_copy_helper.577
+ _block_copy_helper.588
+ _block_copy_helper.599
+ _block_copy_helper.610
+ _block_copy_helper.617
+ _block_copy_helper.62
+ _block_copy_helper.633
+ _block_copy_helper.644
+ _block_copy_helper.655
+ _block_copy_helper.666
+ _block_copy_helper.677
+ _block_copy_helper.687
+ _block_copy_helper.69
+ _block_copy_helper.694
+ _block_copy_helper.710
+ _block_copy_helper.721
+ _block_copy_helper.732
+ _block_copy_helper.743
+ _block_copy_helper.75
+ _block_copy_helper.754
+ _block_copy_helper.765
+ _block_copy_helper.776
+ _block_copy_helper.788
+ _block_copy_helper.80
+ _block_copy_helper.82
+ _block_copy_helper.86
+ _block_copy_helper.88
+ _block_copy_helper.92
+ _block_copy_helper.98
+ _block_descriptor.100
+ _block_descriptor.106
+ _block_descriptor.112
+ _block_descriptor.117
+ _block_descriptor.124
+ _block_descriptor.136
+ _block_descriptor.142
+ _block_descriptor.154
+ _block_descriptor.160
+ _block_descriptor.168
+ _block_descriptor.177
+ _block_descriptor.183
+ _block_descriptor.198
+ _block_descriptor.210
+ _block_descriptor.217
+ _block_descriptor.244
+ _block_descriptor.25
+ _block_descriptor.255
+ _block_descriptor.266
+ _block_descriptor.277
+ _block_descriptor.284
+ _block_descriptor.30
+ _block_descriptor.300
+ _block_descriptor.311
+ _block_descriptor.328
+ _block_descriptor.345
+ _block_descriptor.35
+ _block_descriptor.352
+ _block_descriptor.368
+ _block_descriptor.379
+ _block_descriptor.389
+ _block_descriptor.396
+ _block_descriptor.41
+ _block_descriptor.412
+ _block_descriptor.424
+ _block_descriptor.434
+ _block_descriptor.44
+ _block_descriptor.441
+ _block_descriptor.457
+ _block_descriptor.468
+ _block_descriptor.479
+ _block_descriptor.490
+ _block_descriptor.501
+ _block_descriptor.512
+ _block_descriptor.523
+ _block_descriptor.534
+ _block_descriptor.544
+ _block_descriptor.551
+ _block_descriptor.568
+ _block_descriptor.579
+ _block_descriptor.58
+ _block_descriptor.590
+ _block_descriptor.601
+ _block_descriptor.612
+ _block_descriptor.619
+ _block_descriptor.635
+ _block_descriptor.64
+ _block_descriptor.646
+ _block_descriptor.657
+ _block_descriptor.668
+ _block_descriptor.679
+ _block_descriptor.689
+ _block_descriptor.696
+ _block_descriptor.71
+ _block_descriptor.712
+ _block_descriptor.723
+ _block_descriptor.734
+ _block_descriptor.745
+ _block_descriptor.756
+ _block_descriptor.767
+ _block_descriptor.77
+ _block_descriptor.778
+ _block_descriptor.790
+ _block_descriptor.82
+ _block_descriptor.84
+ _block_descriptor.88
+ _block_descriptor.90
+ _block_descriptor.94
+ _block_destroy_helper.105
+ _block_destroy_helper.111
+ _block_destroy_helper.116
+ _block_destroy_helper.123
+ _block_destroy_helper.135
+ _block_destroy_helper.141
+ _block_destroy_helper.153
+ _block_destroy_helper.159
+ _block_destroy_helper.167
+ _block_destroy_helper.176
+ _block_destroy_helper.182
+ _block_destroy_helper.197
+ _block_destroy_helper.209
+ _block_destroy_helper.216
+ _block_destroy_helper.24
+ _block_destroy_helper.243
+ _block_destroy_helper.254
+ _block_destroy_helper.265
+ _block_destroy_helper.276
+ _block_destroy_helper.283
+ _block_destroy_helper.29
+ _block_destroy_helper.299
+ _block_destroy_helper.310
+ _block_destroy_helper.327
+ _block_destroy_helper.34
+ _block_destroy_helper.344
+ _block_destroy_helper.351
+ _block_destroy_helper.367
+ _block_destroy_helper.378
+ _block_destroy_helper.388
+ _block_destroy_helper.395
+ _block_destroy_helper.40
+ _block_destroy_helper.411
+ _block_destroy_helper.423
+ _block_destroy_helper.43
+ _block_destroy_helper.433
+ _block_destroy_helper.440
+ _block_destroy_helper.456
+ _block_destroy_helper.467
+ _block_destroy_helper.478
+ _block_destroy_helper.489
+ _block_destroy_helper.500
+ _block_destroy_helper.511
+ _block_destroy_helper.522
+ _block_destroy_helper.533
+ _block_destroy_helper.543
+ _block_destroy_helper.550
+ _block_destroy_helper.567
+ _block_destroy_helper.57
+ _block_destroy_helper.578
+ _block_destroy_helper.589
+ _block_destroy_helper.600
+ _block_destroy_helper.611
+ _block_destroy_helper.618
+ _block_destroy_helper.63
+ _block_destroy_helper.634
+ _block_destroy_helper.645
+ _block_destroy_helper.656
+ _block_destroy_helper.667
+ _block_destroy_helper.678
+ _block_destroy_helper.688
+ _block_destroy_helper.695
+ _block_destroy_helper.70
+ _block_destroy_helper.711
+ _block_destroy_helper.722
+ _block_destroy_helper.733
+ _block_destroy_helper.744
+ _block_destroy_helper.755
+ _block_destroy_helper.76
+ _block_destroy_helper.766
+ _block_destroy_helper.777
+ _block_destroy_helper.789
+ _block_destroy_helper.81
+ _block_destroy_helper.83
+ _block_destroy_helper.87
+ _block_destroy_helper.89
+ _block_destroy_helper.93
+ _block_destroy_helper.99
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC011NormalizingE0CAFVGSciHPyHC.34
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC09DictationE0CAFVGSciHPyHC.50
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC0E0CAFVGSciHPyHC.47
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC0dE0CAFVGSciHPyHC.33
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC011NormalizingE0CAFVGSciHPyHC.33
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC09DictationE0CAFVGSciHPyHC.49
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC0E0CAFVGSciHPyHC.46
+ _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC0dE0CAFVGSciHPyHC.32
+ _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC011NormalizingE0CAFVGGSciHPyHC.35
+ _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC09DictationE0CAFVGGSciHPyHC.51
+ _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC0E0CAFVGGSciHPyHC.48
+ _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC0dE0CAFVGGSciHPyHC.34
+ _hasSPIAccess.hasAccess
+ _hasSPIAccess.onceToken
+ _kSFCoreAnalyticsAssetTypeKey
+ _objc_msgSend$initWithLanguageModel:vocabulary:weight:
+ _objc_msgSend$unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:
+ _objc_msgSend$weight
+ _objectdestroy.164Tm
+ _objectdestroy.170Tm
+ _objectdestroy.173Tm
+ _objectdestroy.340Tm
+ _objectdestroy.49Tm
+ _sSupportedLocaleIdentifiers.938
+ _sSupportedLocales.962
+ _sharedInstance.onceToken.1944
+ _sharedInstance.sharedManager.1945
- GCC_except_table1025
- GCC_except_table1049
- GCC_except_table1052
- GCC_except_table1135
- GCC_except_table1156
- GCC_except_table1342
- GCC_except_table1347
- GCC_except_table1351
- GCC_except_table1357
- GCC_except_table1369
- GCC_except_table1370
- GCC_except_table1372
- GCC_except_table1373
- GCC_except_table1374
- GCC_except_table266
- GCC_except_table395
- GCC_except_table399
- GCC_except_table401
- GCC_except_table403
- GCC_except_table405
- GCC_except_table408
- GCC_except_table415
- GCC_except_table418
- GCC_except_table423
- GCC_except_table443
- GCC_except_table467
- GCC_except_table471
- GCC_except_table508
- GCC_except_table756
- GCC_except_table861
- GCC_except_table895
- GCC_except_table903
- GCC_except_table905
- GCC_except_table907
- GCC_except_table916
- GCC_except_table956
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.504
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.508
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke_2.505
- ___67-[SFSpeechRecognitionTask handleSpeechRecognitionDidFailWithError:]_block_invoke
- ___79+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:]_block_invoke
- ___Block_byref_object_copy_.1567
- ___Block_byref_object_copy_.1721
- ___Block_byref_object_copy_.1842
- ___Block_byref_object_copy_.2159
- ___Block_byref_object_copy_.2421
- ___Block_byref_object_copy_.3030
- ___Block_byref_object_copy_.664
- ___Block_byref_object_dispose_.1568
- ___Block_byref_object_dispose_.1722
- ___Block_byref_object_dispose_.1843
- ___Block_byref_object_dispose_.2160
- ___Block_byref_object_dispose_.2422
- ___Block_byref_object_dispose_.3031
- ___Block_byref_object_dispose_.665
- ___block_literal_global.1583
- ___block_literal_global.1740
- ___block_literal_global.2111
- ___block_literal_global.226
- ___block_literal_global.228
- ___block_literal_global.2455
- ___block_literal_global.2835
- ___block_literal_global.3082
- ___block_literal_global.354
- ___block_literal_global.375
- ___block_literal_global.393
- ___block_literal_global.430
- ___block_literal_global.430.2129
- ___block_literal_global.432
- ___block_literal_global.438
- ___block_literal_global.454
- ___block_literal_global.730
- ___block_literal_global.977
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Speech
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Speech
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Speech
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Speech
- _block_copy_helper.103
- _block_copy_helper.108
- _block_copy_helper.114
- _block_copy_helper.121
- _block_copy_helper.133
- _block_copy_helper.139
- _block_copy_helper.145
- _block_copy_helper.157
- _block_copy_helper.165
- _block_copy_helper.180
- _block_copy_helper.19
- _block_copy_helper.195
- _block_copy_helper.207
- _block_copy_helper.21
- _block_copy_helper.230
- _block_copy_helper.241
- _block_copy_helper.25
- _block_copy_helper.252
- _block_copy_helper.263
- _block_copy_helper.274
- _block_copy_helper.281
- _block_copy_helper.297
- _block_copy_helper.308
- _block_copy_helper.318
- _block_copy_helper.32
- _block_copy_helper.325
- _block_copy_helper.342
- _block_copy_helper.349
- _block_copy_helper.365
- _block_copy_helper.376
- _block_copy_helper.38
- _block_copy_helper.386
- _block_copy_helper.393
- _block_copy_helper.409
- _block_copy_helper.41
- _block_copy_helper.421
- _block_copy_helper.431
- _block_copy_helper.438
- _block_copy_helper.454
- _block_copy_helper.465
- _block_copy_helper.476
- _block_copy_helper.48
- _block_copy_helper.487
- _block_copy_helper.498
- _block_copy_helper.509
- _block_copy_helper.520
- _block_copy_helper.531
- _block_copy_helper.541
- _block_copy_helper.548
- _block_copy_helper.55
- _block_copy_helper.565
- _block_copy_helper.576
- _block_copy_helper.587
- _block_copy_helper.598
- _block_copy_helper.609
- _block_copy_helper.61
- _block_copy_helper.616
- _block_copy_helper.632
- _block_copy_helper.643
- _block_copy_helper.654
- _block_copy_helper.665
- _block_copy_helper.676
- _block_copy_helper.686
- _block_copy_helper.693
- _block_copy_helper.709
- _block_copy_helper.720
- _block_copy_helper.73
- _block_copy_helper.731
- _block_copy_helper.742
- _block_copy_helper.753
- _block_copy_helper.764
- _block_copy_helper.775
- _block_copy_helper.787
- _block_copy_helper.79
- _block_copy_helper.81
- _block_copy_helper.85
- _block_copy_helper.87
- _block_copy_helper.91
- _block_copy_helper.97
- _block_descriptor.105
- _block_descriptor.110
- _block_descriptor.116
- _block_descriptor.123
- _block_descriptor.135
- _block_descriptor.141
- _block_descriptor.147
- _block_descriptor.159
- _block_descriptor.167
- _block_descriptor.182
- _block_descriptor.197
- _block_descriptor.209
- _block_descriptor.21
- _block_descriptor.23
- _block_descriptor.232
- _block_descriptor.243
- _block_descriptor.254
- _block_descriptor.265
- _block_descriptor.27
- _block_descriptor.276
- _block_descriptor.283
- _block_descriptor.299
- _block_descriptor.310
- _block_descriptor.320
- _block_descriptor.327
- _block_descriptor.34
- _block_descriptor.344
- _block_descriptor.351
- _block_descriptor.367
- _block_descriptor.378
- _block_descriptor.388
- _block_descriptor.395
- _block_descriptor.40
- _block_descriptor.411
- _block_descriptor.423
- _block_descriptor.43
- _block_descriptor.433
- _block_descriptor.440
- _block_descriptor.456
- _block_descriptor.467
- _block_descriptor.478
- _block_descriptor.489
- _block_descriptor.50
- _block_descriptor.500
- _block_descriptor.511
- _block_descriptor.522
- _block_descriptor.533
- _block_descriptor.543
- _block_descriptor.550
- _block_descriptor.567
- _block_descriptor.57
- _block_descriptor.578
- _block_descriptor.589
- _block_descriptor.600
- _block_descriptor.611
- _block_descriptor.618
- _block_descriptor.63
- _block_descriptor.634
- _block_descriptor.645
- _block_descriptor.656
- _block_descriptor.667
- _block_descriptor.678
- _block_descriptor.688
- _block_descriptor.695
- _block_descriptor.711
- _block_descriptor.722
- _block_descriptor.733
- _block_descriptor.744
- _block_descriptor.75
- _block_descriptor.755
- _block_descriptor.766
- _block_descriptor.777
- _block_descriptor.789
- _block_descriptor.81
- _block_descriptor.83
- _block_descriptor.87
- _block_descriptor.89
- _block_descriptor.93
- _block_descriptor.99
- _block_destroy_helper.104
- _block_destroy_helper.109
- _block_destroy_helper.115
- _block_destroy_helper.122
- _block_destroy_helper.134
- _block_destroy_helper.140
- _block_destroy_helper.146
- _block_destroy_helper.158
- _block_destroy_helper.166
- _block_destroy_helper.181
- _block_destroy_helper.196
- _block_destroy_helper.20
- _block_destroy_helper.208
- _block_destroy_helper.22
- _block_destroy_helper.231
- _block_destroy_helper.242
- _block_destroy_helper.253
- _block_destroy_helper.26
- _block_destroy_helper.264
- _block_destroy_helper.275
- _block_destroy_helper.282
- _block_destroy_helper.298
- _block_destroy_helper.309
- _block_destroy_helper.319
- _block_destroy_helper.326
- _block_destroy_helper.33
- _block_destroy_helper.343
- _block_destroy_helper.350
- _block_destroy_helper.366
- _block_destroy_helper.377
- _block_destroy_helper.387
- _block_destroy_helper.39
- _block_destroy_helper.394
- _block_destroy_helper.410
- _block_destroy_helper.42
- _block_destroy_helper.422
- _block_destroy_helper.432
- _block_destroy_helper.439
- _block_destroy_helper.455
- _block_destroy_helper.466
- _block_destroy_helper.477
- _block_destroy_helper.488
- _block_destroy_helper.49
- _block_destroy_helper.499
- _block_destroy_helper.510
- _block_destroy_helper.521
- _block_destroy_helper.532
- _block_destroy_helper.542
- _block_destroy_helper.549
- _block_destroy_helper.56
- _block_destroy_helper.566
- _block_destroy_helper.577
- _block_destroy_helper.588
- _block_destroy_helper.599
- _block_destroy_helper.610
- _block_destroy_helper.617
- _block_destroy_helper.62
- _block_destroy_helper.633
- _block_destroy_helper.644
- _block_destroy_helper.655
- _block_destroy_helper.666
- _block_destroy_helper.677
- _block_destroy_helper.687
- _block_destroy_helper.694
- _block_destroy_helper.710
- _block_destroy_helper.721
- _block_destroy_helper.732
- _block_destroy_helper.74
- _block_destroy_helper.743
- _block_destroy_helper.754
- _block_destroy_helper.765
- _block_destroy_helper.776
- _block_destroy_helper.788
- _block_destroy_helper.80
- _block_destroy_helper.82
- _block_destroy_helper.86
- _block_destroy_helper.88
- _block_destroy_helper.92
- _block_destroy_helper.98
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC011NormalizingE0CAFVGSciHPyHC.33
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC09DictationE0CAFVGSciHPyHC.49
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC0E0CAFVGSciHPyHC.46
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC18MultisegmentResultVs5Error_pGAC0dE0CAFVGSciHPyHC.32
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC011NormalizingE0CAFVGSciHPyHC.32
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC09DictationE0CAFVGSciHPyHC.48
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC0E0CAFVGSciHPyHC.45
- _get_witness_table s16AsyncMapSequenceVyScsy6Speech17TranscriberCommonC6ResultVs5Error_pGAC0dE0CAFVGSciHPyHC.31
- _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC011NormalizingE0CAFVGGSciHPyHC.34
- _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC09DictationE0CAFVGGSciHPyHC.50
- _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC0E0CAFVGGSciHPyHC.47
- _get_witness_table s16AsyncMapSequenceVyScsySDySS6Speech17TranscriberCommonC18MultisegmentResultVGs5Error_pGSDySSAC0dE0CAFVGGSciHPyHC.33
- _objectdestroy.163Tm
- _objectdestroy.169Tm
- _objectdestroy.172Tm
- _objectdestroy.339Tm
- _sSupportedLocaleIdentifiers.951
- _sSupportedLocales.975
- _sharedInstance.onceToken.1941
- _sharedInstance.sharedManager.1942
- _symbolic _____XDXMT 6Speech14AssetInventoryC
CStrings:
+ "%s %@ cached container for persona: %@"
+ "%s %@ container for persona: %@"
+ "%s MUX: Failed to resolve container, url cannot be nil."
+ "+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:]"
+ "+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:]_block_invoke"
+ "-[SFSpeechProfileContainerManager containerForPersona:]_block_invoke"
+ "-[SFSpeechRecognitionTask handleSpeechRecognitionDidFailWithError:]"
+ "Cannot use modules with unallocated locales "
+ "Content hints may only include one custom language model configuration"
+ "Custom configuration weight not within [0.0,1.0]: illegal value %@"
+ "Failed to initialize"
+ "Found"
+ "Initialized"
+ "No"
+ "T@\"NSNumber\",R,C,N,V_weight"
+ "Weight must be in range [0.0,1.0]"
+ "_weight"
+ "com.apple.assistant.dictation.prerecorded"
+ "hasSPIAccess"
+ "initWithLanguageModel:vocabulary:weight:"
+ "isCurrentPersonaDefault"
+ "sandboxExtensionsForCustomLmConfig:"
+ "unsubscribeFromAssetWithConfig:regionId:subscriberId:completionHandler:"
+ "weight"
- "+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:]"
- "+[SFEntitledAssetManager unsubscribeFromAssetWithConfig:regionId:subscriberId:]_block_invoke"
- "-[SFSpeechRecognitionTask handleSpeechRecognitionDidFailWithError:]_block_invoke"

```
