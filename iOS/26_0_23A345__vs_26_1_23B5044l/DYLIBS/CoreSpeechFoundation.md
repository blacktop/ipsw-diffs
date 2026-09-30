## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3500.122.2.0.0
-  __TEXT.__text: 0xc1718
-  __TEXT.__auth_stubs: 0x1eb0
-  __TEXT.__objc_methlist: 0xc4b8
+3505.14.3.0.0
+  __TEXT.__text: 0xc3478
+  __TEXT.__auth_stubs: 0x1ec0
+  __TEXT.__objc_methlist: 0xc690
   __TEXT.__const: 0x7f8
-  __TEXT.__dlopen_cstrs: 0x1ee
+  __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x151e9
+  __TEXT.__cstring: 0x15411
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x4138
-  __TEXT.__oslogstring: 0xf7f2
-  __TEXT.__unwind_info: 0x35f8
+  __TEXT.__gcc_except_tab: 0x413c
+  __TEXT.__oslogstring: 0xf8f4
+  __TEXT.__unwind_info: 0x3670
   __TEXT.__eh_frame: 0xe0
-  __TEXT.__objc_classname: 0x1bb8
-  __TEXT.__objc_methname: 0x20b95
-  __TEXT.__objc_methtype: 0x43cb
-  __TEXT.__objc_stubs: 0x10e00
-  __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__const: 0x2670
-  __DATA_CONST.__objc_classlist: 0x6c0
+  __TEXT.__objc_classname: 0x1c26
+  __TEXT.__objc_methname: 0x20d10
+  __TEXT.__objc_methtype: 0x4482
+  __TEXT.__objc_stubs: 0x10f80
+  __DATA_CONST.__got: 0xf90
+  __DATA_CONST.__const: 0x26d8
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x1a8
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b28
+  __DATA_CONST.__objc_selrefs: 0x6ba0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0xf70
-  __AUTH_CONST.__const: 0x1630
-  __AUTH_CONST.__cfstring: 0x8e00
-  __AUTH_CONST.__objc_const: 0x13040
+  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__const: 0x1670
+  __AUTH_CONST.__cfstring: 0x8f20
+  __AUTH_CONST.__objc_const: 0x13418
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH.__objc_data: 0x1898
-  __DATA.__objc_ivar: 0xca8
-  __DATA.__data: 0x1408
-  __DATA.__bss: 0x8b8
+  __AUTH.__objc_data: 0x1988
+  __DATA.__objc_ivar: 0xcbc
+  __DATA.__data: 0x1470
+  __DATA.__bss: 0x910
   __DATA_DIRTY.__objc_data: 0x2ba0
   __DATA_DIRTY.__data: 0x2d8
-  __DATA_DIRTY.__bss: 0x400
+  __DATA_DIRTY.__bss: 0x3e8
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EEFC6D7C-21A1-35EB-B862-F4C3A7A4A231
-  Functions: 4745
-  Symbols:   16097
-  CStrings:  10120
+  UUID: 5A84A455-5642-3F71-978E-DD6889E34767
+  Functions: 4786
+  Symbols:   16241
+  CStrings:  10178
 
Symbols:
+ +[CSAsset supportsSecureCoding]
+ +[CSRemoteAssetManagerDarwinExclave sharedManager]
+ +[CSRemoteAssetManagerFactory remoteAssetManager]
+ +[CSUtils needRetrainingForExclaveOnly]
+ -[CSAsset encodeWithCoder:]
+ -[CSAsset initWithCoder:]
+ -[CSAudioProvider audioRecorderSensorInvalidated:]
+ -[CSFPreferences useExclaveFastStart]
+ -[CSRemoteAssetCache .cxx_destruct]
+ -[CSRemoteAssetCache asset]
+ -[CSRemoteAssetCache initWithAsset:languageCode:]
+ -[CSRemoteAssetCache languageCode]
+ -[CSRemoteAssetManagerDarwinExclave .cxx_destruct]
+ -[CSRemoteAssetManagerDarwinExclave _languageCode]
+ -[CSRemoteAssetManagerDarwinExclave addObserver:forAssetType:]
+ -[CSRemoteAssetManagerDarwinExclave assetConfigVersionForAssetType:]
+ -[CSRemoteAssetManagerDarwinExclave assetForCurrentLanguageOfType:]
+ -[CSRemoteAssetManagerDarwinExclave assetHashForAssetType:]
+ -[CSRemoteAssetManagerDarwinExclave exclaveAssetsController]
+ -[CSRemoteAssetManagerDarwinExclave initWithExclaveAssetsController:]
+ -[CSRemoteAssetManagerDarwinExclave init]
+ -[CSRemoteAssetManagerDarwinExclave languageCode]
+ -[CSRemoteAssetManagerDarwinExclave removeObserver:forAssetType:]
+ -[CSRemoteAssetManagerDarwinExclave resourcePathForAssetType:]
+ -[CSRemoteAssetManagerDarwinExclave setExclaveAssetsController:]
+ -[CSRemoteAssetManagerDarwinExclave setLanguageCode:resourcePath:configVersion:assetHash:assetType:]
+ GCC_except_table1276
+ GCC_except_table1305
+ GCC_except_table1378
+ GCC_except_table1382
+ GCC_except_table1384
+ GCC_except_table1385
+ GCC_except_table1386
+ GCC_except_table1387
+ GCC_except_table1388
+ GCC_except_table1389
+ GCC_except_table1395
+ GCC_except_table1398
+ GCC_except_table1400
+ GCC_except_table1401
+ GCC_except_table1403
+ GCC_except_table1404
+ GCC_except_table1405
+ GCC_except_table1407
+ GCC_except_table1410
+ GCC_except_table1422
+ GCC_except_table1820
+ GCC_except_table1821
+ GCC_except_table1822
+ GCC_except_table1823
+ GCC_except_table1824
+ GCC_except_table1828
+ GCC_except_table1831
+ GCC_except_table1835
+ GCC_except_table1841
+ GCC_except_table1848
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1865
+ GCC_except_table1871
+ GCC_except_table1961
+ GCC_except_table1966
+ GCC_except_table2018
+ GCC_except_table2028
+ GCC_except_table2068
+ GCC_except_table2069
+ GCC_except_table2071
+ GCC_except_table2072
+ GCC_except_table2078
+ GCC_except_table2087
+ GCC_except_table2094
+ GCC_except_table2137
+ GCC_except_table2210
+ GCC_except_table2320
+ GCC_except_table2355
+ GCC_except_table2497
+ GCC_except_table2501
+ GCC_except_table2574
+ GCC_except_table2585
+ GCC_except_table2587
+ GCC_except_table2592
+ GCC_except_table2594
+ GCC_except_table2607
+ GCC_except_table2616
+ GCC_except_table2634
+ GCC_except_table2655
+ GCC_except_table2693
+ GCC_except_table2750
+ GCC_except_table2752
+ GCC_except_table2753
+ GCC_except_table2896
+ GCC_except_table3033
+ GCC_except_table3041
+ GCC_except_table3049
+ GCC_except_table3056
+ GCC_except_table3060
+ GCC_except_table3062
+ GCC_except_table3063
+ GCC_except_table3086
+ GCC_except_table3142
+ GCC_except_table3146
+ GCC_except_table3201
+ GCC_except_table3224
+ GCC_except_table3255
+ GCC_except_table3256
+ GCC_except_table3257
+ GCC_except_table3258
+ GCC_except_table3281
+ GCC_except_table3294
+ GCC_except_table3453
+ GCC_except_table3513
+ GCC_except_table3569
+ GCC_except_table3570
+ GCC_except_table3599
+ GCC_except_table3600
+ GCC_except_table3602
+ GCC_except_table3605
+ GCC_except_table3606
+ GCC_except_table3607
+ GCC_except_table3630
+ GCC_except_table3633
+ GCC_except_table3638
+ GCC_except_table3639
+ GCC_except_table3641
+ GCC_except_table3654
+ GCC_except_table3680
+ GCC_except_table3704
+ GCC_except_table3706
+ GCC_except_table3707
+ GCC_except_table3708
+ GCC_except_table3709
+ GCC_except_table3719
+ GCC_except_table3806
+ GCC_except_table3817
+ GCC_except_table3828
+ GCC_except_table3833
+ GCC_except_table3834
+ GCC_except_table3835
+ GCC_except_table3838
+ GCC_except_table3839
+ GCC_except_table3845
+ GCC_except_table3846
+ GCC_except_table3848
+ GCC_except_table3850
+ GCC_except_table3851
+ GCC_except_table3853
+ GCC_except_table3854
+ GCC_except_table3858
+ GCC_except_table3861
+ GCC_except_table3862
+ GCC_except_table3863
+ GCC_except_table3865
+ GCC_except_table3866
+ GCC_except_table3867
+ GCC_except_table3869
+ GCC_except_table3870
+ GCC_except_table3872
+ GCC_except_table3873
+ GCC_except_table3874
+ GCC_except_table3875
+ GCC_except_table3901
+ GCC_except_table3949
+ GCC_except_table3953
+ GCC_except_table4011
+ GCC_except_table4012
+ GCC_except_table4013
+ GCC_except_table4014
+ GCC_except_table4017
+ GCC_except_table4042
+ GCC_except_table4043
+ GCC_except_table4045
+ GCC_except_table4046
+ GCC_except_table4049
+ GCC_except_table4060
+ GCC_except_table4072
+ GCC_except_table4073
+ GCC_except_table4074
+ GCC_except_table4077
+ GCC_except_table4080
+ GCC_except_table4082
+ GCC_except_table4088
+ GCC_except_table4091
+ GCC_except_table4094
+ GCC_except_table4098
+ GCC_except_table4099
+ GCC_except_table4106
+ GCC_except_table4119
+ GCC_except_table4120
+ GCC_except_table4122
+ GCC_except_table4123
+ GCC_except_table4125
+ GCC_except_table4128
+ GCC_except_table4129
+ GCC_except_table4134
+ GCC_except_table4136
+ GCC_except_table4140
+ GCC_except_table4141
+ GCC_except_table4171
+ GCC_except_table4175
+ GCC_except_table4275
+ GCC_except_table4282
+ GCC_except_table4328
+ GCC_except_table4392
+ GCC_except_table4475
+ GCC_except_table4487
+ GCC_except_table4533
+ GCC_except_table4599
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table513
+ GCC_except_table542
+ GCC_except_table545
+ GCC_except_table550
+ GCC_except_table635
+ GCC_except_table638
+ GCC_except_table641
+ GCC_except_table642
+ GCC_except_table801
+ GCC_except_table808
+ GCC_except_table871
+ GCC_except_table872
+ GCC_except_table894
+ GCC_except_table895
+ GCC_except_table896
+ GCC_except_table900
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table903
+ GCC_except_table904
+ GCC_except_table906
+ GCC_except_table907
+ GCC_except_table908
+ GCC_except_table911
+ GCC_except_table912
+ GCC_except_table913
+ GCC_except_table915
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table931
+ _AudioConverterFillComplexBuffer_BlockInvoke.7322
+ _CoreSpeechUtilsLibraryCore
+ _CoreSpeechUtilsLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_CSRemoteAssetCache
+ _OBJC_CLASS_$_CSRemoteAssetManagerDarwinExclave
+ _OBJC_CLASS_$_CSRemoteAssetManagerFactory
+ _OBJC_IVAR_$_CSRemoteAssetCache._asset
+ _OBJC_IVAR_$_CSRemoteAssetCache._languageCode
+ _OBJC_IVAR_$_CSRemoteAssetManagerDarwinExclave._assetCache
+ _OBJC_IVAR_$_CSRemoteAssetManagerDarwinExclave._exclaveAssetsController
+ _OBJC_IVAR_$_CSRemoteAssetManagerDarwinExclave._observers
+ _OBJC_IVAR_$_CSRemoteAssetManagerDarwinExclave._queue
+ _OBJC_METACLASS_$_CSRemoteAssetCache
+ _OBJC_METACLASS_$_CSRemoteAssetManagerDarwinExclave
+ _OBJC_METACLASS_$_CSRemoteAssetManagerFactory
+ __OBJC_$_CLASS_METHODS_CSRemoteAssetManagerDarwinExclave
+ __OBJC_$_CLASS_METHODS_CSRemoteAssetManagerFactory
+ __OBJC_$_CLASS_PROP_LIST_CSAsset
+ __OBJC_$_INSTANCE_METHODS_CSRemoteAssetCache
+ __OBJC_$_INSTANCE_METHODS_CSRemoteAssetManagerDarwinExclave
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoteAssetCache
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoteAssetManagerDarwinExclave
+ __OBJC_$_PROP_LIST_CSRemoteAssetCache
+ __OBJC_$_PROP_LIST_CSRemoteAssetManagerDarwinExclave
+ __OBJC_$_PROTOCOL_CLASS_METHODS_CSRemoteAssetManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSRemoteAssetManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSRemoteAssetManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_CSRemoteAssetManagerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_CSAsset
+ __OBJC_CLASS_PROTOCOLS_$_CSRemoteAssetManager
+ __OBJC_CLASS_PROTOCOLS_$_CSRemoteAssetManagerDarwinExclave
+ __OBJC_CLASS_RO_$_CSRemoteAssetCache
+ __OBJC_CLASS_RO_$_CSRemoteAssetManagerDarwinExclave
+ __OBJC_CLASS_RO_$_CSRemoteAssetManagerFactory
+ __OBJC_LABEL_PROTOCOL_$_CSRemoteAssetManagerProtocol
+ __OBJC_METACLASS_RO_$_CSRemoteAssetCache
+ __OBJC_METACLASS_RO_$_CSRemoteAssetManagerDarwinExclave
+ __OBJC_METACLASS_RO_$_CSRemoteAssetManagerFactory
+ __OBJC_PROTOCOL_$_CSRemoteAssetManagerProtocol
+ ___100-[CSRemoteAssetManagerDarwinExclave setLanguageCode:resourcePath:configVersion:assetHash:assetType:]_block_invoke
+ ___37-[CSFPreferences useExclaveFastStart]_block_invoke
+ ___49-[CSRemoteAssetManagerDarwinExclave languageCode]_block_invoke
+ ___50+[CSRemoteAssetManagerDarwinExclave sharedManager]_block_invoke
+ ___50-[CSAudioProvider audioRecorderSensorInvalidated:]_block_invoke
+ ___59-[CSRemoteAssetManagerDarwinExclave assetHashForAssetType:]_block_invoke
+ ___62-[CSRemoteAssetManagerDarwinExclave addObserver:forAssetType:]_block_invoke
+ ___62-[CSRemoteAssetManagerDarwinExclave resourcePathForAssetType:]_block_invoke
+ ___65-[CSRemoteAssetManagerDarwinExclave removeObserver:forAssetType:]_block_invoke
+ ___67-[CSRemoteAssetManagerDarwinExclave assetForCurrentLanguageOfType:]_block_invoke
+ ___67-[CSRemoteAssetManagerDarwinExclave assetForCurrentLanguageOfType:]_block_invoke.23
+ ___68-[CSRemoteAssetManagerDarwinExclave assetConfigVersionForAssetType:]_block_invoke
+ ___Block_byref_object_copy_.12698
+ ___Block_byref_object_copy_.13099
+ ___Block_byref_object_copy_.13395
+ ___Block_byref_object_copy_.13643
+ ___Block_byref_object_copy_.1382
+ ___Block_byref_object_copy_.14142
+ ___Block_byref_object_copy_.14714
+ ___Block_byref_object_copy_.14843
+ ___Block_byref_object_copy_.15711
+ ___Block_byref_object_copy_.1665
+ ___Block_byref_object_copy_.2230
+ ___Block_byref_object_copy_.2649
+ ___Block_byref_object_copy_.3413
+ ___Block_byref_object_copy_.4733
+ ___Block_byref_object_copy_.4954
+ ___Block_byref_object_copy_.5794
+ ___Block_byref_object_copy_.6204
+ ___Block_byref_object_copy_.7919
+ ___Block_byref_object_copy_.8201
+ ___Block_byref_object_copy_.8651
+ ___Block_byref_object_copy_.9409
+ ___Block_byref_object_dispose_.12699
+ ___Block_byref_object_dispose_.13100
+ ___Block_byref_object_dispose_.13396
+ ___Block_byref_object_dispose_.13644
+ ___Block_byref_object_dispose_.1383
+ ___Block_byref_object_dispose_.14143
+ ___Block_byref_object_dispose_.14715
+ ___Block_byref_object_dispose_.14844
+ ___Block_byref_object_dispose_.15712
+ ___Block_byref_object_dispose_.1666
+ ___Block_byref_object_dispose_.2231
+ ___Block_byref_object_dispose_.2650
+ ___Block_byref_object_dispose_.3414
+ ___Block_byref_object_dispose_.4734
+ ___Block_byref_object_dispose_.4955
+ ___Block_byref_object_dispose_.5795
+ ___Block_byref_object_dispose_.6205
+ ___Block_byref_object_dispose_.7920
+ ___Block_byref_object_dispose_.8202
+ ___Block_byref_object_dispose_.8652
+ ___Block_byref_object_dispose_.9410
+ ___CoreSpeechUtilsLibraryCore_block_invoke
+ ___block_descriptor_64_e8_32s40r48w_e8_v16?0Q8lw48l8s32l8r40l8
+ ___block_descriptor_72_e8_32s40s48r56w_e5_v8?0ls32l8s40l8r48l8w56l8
+ ___block_literal_global.10287
+ ___block_literal_global.10384
+ ___block_literal_global.11259
+ ___block_literal_global.11464
+ ___block_literal_global.11619
+ ___block_literal_global.11837
+ ___block_literal_global.11874
+ ___block_literal_global.12744
+ ___block_literal_global.13210
+ ___block_literal_global.1330
+ ___block_literal_global.13496
+ ___block_literal_global.13742
+ ___block_literal_global.1400
+ ___block_literal_global.14048
+ ___block_literal_global.144
+ ___block_literal_global.14433
+ ___block_literal_global.14535
+ ___block_literal_global.14591
+ ___block_literal_global.149
+ ___block_literal_global.14986
+ ___block_literal_global.15079
+ ___block_literal_global.15168
+ ___block_literal_global.1522
+ ___block_literal_global.154
+ ___block_literal_global.15498
+ ___block_literal_global.1550
+ ___block_literal_global.15736
+ ___block_literal_global.1577
+ ___block_literal_global.1621
+ ___block_literal_global.167
+ ___block_literal_global.1693
+ ___block_literal_global.178.8335
+ ___block_literal_global.183.8329
+ ___block_literal_global.20.13195
+ ___block_literal_global.2247
+ ___block_literal_global.2343
+ ___block_literal_global.2399
+ ___block_literal_global.248
+ ___block_literal_global.259
+ ___block_literal_global.2590
+ ___block_literal_global.264
+ ___block_literal_global.2665
+ ___block_literal_global.269
+ ___block_literal_global.271.8271
+ ___block_literal_global.2777
+ ___block_literal_global.279
+ ___block_literal_global.2826
+ ___block_literal_global.30
+ ___block_literal_global.3141
+ ___block_literal_global.315
+ ___block_literal_global.320.8252
+ ___block_literal_global.325
+ ___block_literal_global.330
+ ___block_literal_global.3325
+ ___block_literal_global.3433
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.36
+ ___block_literal_global.363
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.3730
+ ___block_literal_global.3884
+ ___block_literal_global.397
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.409
+ ___block_literal_global.4153
+ ___block_literal_global.417
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.437
+ ___block_literal_global.44.8434
+ ___block_literal_global.445
+ ___block_literal_global.450
+ ___block_literal_global.458.8200
+ ___block_literal_global.463
+ ___block_literal_global.468
+ ___block_literal_global.473
+ ___block_literal_global.4761
+ ___block_literal_global.478
+ ___block_literal_global.489
+ ___block_literal_global.49.8432
+ ___block_literal_global.4922
+ ___block_literal_global.494
+ ___block_literal_global.4970
+ ___block_literal_global.499
+ ___block_literal_global.514
+ ___block_literal_global.519
+ ___block_literal_global.530
+ ___block_literal_global.535
+ ___block_literal_global.54
+ ___block_literal_global.546
+ ___block_literal_global.554
+ ___block_literal_global.5562
+ ___block_literal_global.559
+ ___block_literal_global.5646
+ ___block_literal_global.6426
+ ___block_literal_global.6573
+ ___block_literal_global.6641
+ ___block_literal_global.6698
+ ___block_literal_global.6814
+ ___block_literal_global.6832
+ ___block_literal_global.7027
+ ___block_literal_global.7090
+ ___block_literal_global.7150
+ ___block_literal_global.7251
+ ___block_literal_global.7287
+ ___block_literal_global.7572
+ ___block_literal_global.8458
+ ___block_literal_global.8479
+ ___block_literal_global.8534
+ ___block_literal_global.8936
+ ___block_literal_global.8998
+ ___block_literal_global.9144
+ ___block_literal_global.9201
+ ___block_literal_global.9436
+ ___block_literal_global.9743
+ ___block_literal_global.9874
+ ___block_literal_global.9982
+ ___getSecureAssetTypeUtilsClass_block_invoke
+ ___getSecureAssetsPreinstalledBundleClass_block_invoke
+ _audit_stringCoreSpeechUtils
+ _fetchSecureAudioStreamWithRecordDeviceIndicator:from:numSamples:hostTime:error:.heartbeat
+ _getSecureAssetTypeUtilsClass.softClass
+ _getSecureAssetsPreinstalledBundleClass.softClass
+ _objc_msgSend$_languageCode
+ _objc_msgSend$asset
+ _objc_msgSend$assetVersion:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$getVoiceTriggerAssetBundle
+ _objc_msgSend$init:
+ _objc_msgSend$initWithAsset:languageCode:
+ _objc_msgSend$initWithExclaveAssetsController:
+ _objc_msgSend$resourcePathURL:
+ _objc_msgSend$useExclaveFastStart
+ _os_parse_boot_arg_int
+ _sharedHandler.onceToken.12743
+ _sharedHandler.sharedHandler.12745
+ _sharedInstance._sharedInstance.10385
+ _sharedInstance._sharedInstance.11260
+ _sharedInstance._sharedInstance.11875
+ _sharedInstance._sharedInstance.14536
+ _sharedInstance._sharedInstance.14592
+ _sharedInstance._sharedInstance.15080
+ _sharedInstance._sharedInstance.15169
+ _sharedInstance._sharedInstance.4154
+ _sharedInstance._sharedInstance.4923
+ _sharedInstance._sharedInstance.5563
+ _sharedInstance._sharedInstance.6427
+ _sharedInstance._sharedInstance.7028
+ _sharedInstance._sharedInstance.7252
+ _sharedInstance._sharedInstance.7573
+ _sharedInstance.onceToken.10383
+ _sharedInstance.onceToken.11258
+ _sharedInstance.onceToken.11463
+ _sharedInstance.onceToken.11873
+ _sharedInstance.onceToken.1329
+ _sharedInstance.onceToken.13495
+ _sharedInstance.onceToken.14534
+ _sharedInstance.onceToken.14590
+ _sharedInstance.onceToken.14985
+ _sharedInstance.onceToken.15078
+ _sharedInstance.onceToken.15167
+ _sharedInstance.onceToken.1549
+ _sharedInstance.onceToken.15497
+ _sharedInstance.onceToken.15735
+ _sharedInstance.onceToken.1620
+ _sharedInstance.onceToken.1692
+ _sharedInstance.onceToken.2342
+ _sharedInstance.onceToken.2398
+ _sharedInstance.onceToken.2664
+ _sharedInstance.onceToken.3432
+ _sharedInstance.onceToken.3883
+ _sharedInstance.onceToken.4152
+ _sharedInstance.onceToken.4760
+ _sharedInstance.onceToken.4921
+ _sharedInstance.onceToken.4969
+ _sharedInstance.onceToken.5561
+ _sharedInstance.onceToken.6425
+ _sharedInstance.onceToken.6572
+ _sharedInstance.onceToken.6813
+ _sharedInstance.onceToken.7026
+ _sharedInstance.onceToken.7250
+ _sharedInstance.onceToken.7571
+ _sharedInstance.onceToken.8478
+ _sharedInstance.onceToken.8533
+ _sharedInstance.onceToken.8997
+ _sharedInstance.onceToken.9200
+ _sharedInstance.onceToken.9742
+ _sharedInstance.onceToken.9873
+ _sharedInstance.onceToken.9981
+ _sharedInstance.sharedInstance.11465
+ _sharedInstance.sharedInstance.1331
+ _sharedInstance.sharedInstance.13497
+ _sharedInstance.sharedInstance.14987
+ _sharedInstance.sharedInstance.15499
+ _sharedInstance.sharedInstance.15737
+ _sharedInstance.sharedInstance.2344
+ _sharedInstance.sharedInstance.2400
+ _sharedInstance.sharedInstance.2666
+ _sharedInstance.sharedInstance.3434
+ _sharedInstance.sharedInstance.3885
+ _sharedInstance.sharedInstance.4971
+ _sharedInstance.sharedInstance.6574
+ _sharedInstance.sharedInstance.8480
+ _sharedInstance.sharedInstance.8999
+ _sharedInstance.sharedInstance.9202
+ _sharedInstance.sharedInstance.9875
+ _sharedInstance.sharedInstance.9983
+ _sharedInstance.sharedManager.6815
+ _sharedInstance.sharedManager.8535
+ _sharedLogger.onceToken.14047
+ _sharedLogger.onceToken.2776
+ _sharedLogger.onceToken.6640
+ _sharedLogger.onceToken.6831
+ _sharedLogger.shared.14049
+ _sharedManager.onceToken.14737
+ _sharedManager.onceToken.3324
+ _sharedManager.sharedManager.14739
+ _sharedMonitor.onceToken.5645
+ _sharedMonitor.sharedMonitor.5647
+ _sharedPreferences.onceToken.8935
+ _useExclaveFastStart.onceToken
+ _useExclaveFastStart.usingMicSensorFastStart
- -[CSRemoteAssetManager exclaveAssetsController]
- -[CSRemoteAssetManager setExclaveAssetsController:]
- GCC_except_table1237
- GCC_except_table1266
- GCC_except_table1339
- GCC_except_table1343
- GCC_except_table1344
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1348
- GCC_except_table1349
- GCC_except_table1350
- GCC_except_table1356
- GCC_except_table1359
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1364
- GCC_except_table1365
- GCC_except_table1366
- GCC_except_table1368
- GCC_except_table1371
- GCC_except_table1781
- GCC_except_table1782
- GCC_except_table1783
- GCC_except_table1784
- GCC_except_table1785
- GCC_except_table1789
- GCC_except_table1792
- GCC_except_table1793
- GCC_except_table1796
- GCC_except_table1802
- GCC_except_table1809
- GCC_except_table1811
- GCC_except_table1812
- GCC_except_table1826
- GCC_except_table1922
- GCC_except_table1927
- GCC_except_table1979
- GCC_except_table1989
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2032
- GCC_except_table2033
- GCC_except_table2039
- GCC_except_table2048
- GCC_except_table2055
- GCC_except_table2098
- GCC_except_table2171
- GCC_except_table2281
- GCC_except_table2316
- GCC_except_table2458
- GCC_except_table2462
- GCC_except_table2533
- GCC_except_table2544
- GCC_except_table2546
- GCC_except_table2551
- GCC_except_table2553
- GCC_except_table2566
- GCC_except_table2573
- GCC_except_table2575
- GCC_except_table2593
- GCC_except_table2652
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2712
- GCC_except_table2853
- GCC_except_table2990
- GCC_except_table2998
- GCC_except_table3006
- GCC_except_table3013
- GCC_except_table3017
- GCC_except_table3019
- GCC_except_table3020
- GCC_except_table3043
- GCC_except_table3099
- GCC_except_table3103
- GCC_except_table3158
- GCC_except_table3181
- GCC_except_table3212
- GCC_except_table3213
- GCC_except_table3214
- GCC_except_table3215
- GCC_except_table3238
- GCC_except_table3251
- GCC_except_table3410
- GCC_except_table3470
- GCC_except_table3484
- GCC_except_table3526
- GCC_except_table3556
- GCC_except_table3557
- GCC_except_table3559
- GCC_except_table3562
- GCC_except_table3563
- GCC_except_table3564
- GCC_except_table3587
- GCC_except_table3590
- GCC_except_table3594
- GCC_except_table3595
- GCC_except_table3596
- GCC_except_table3598
- GCC_except_table3611
- GCC_except_table3661
- GCC_except_table3663
- GCC_except_table3664
- GCC_except_table3665
- GCC_except_table3666
- GCC_except_table3676
- GCC_except_table3762
- GCC_except_table3763
- GCC_except_table3772
- GCC_except_table3774
- GCC_except_table3775
- GCC_except_table3776
- GCC_except_table3777
- GCC_except_table3780
- GCC_except_table3781
- GCC_except_table3784
- GCC_except_table3785
- GCC_except_table3786
- GCC_except_table3787
- GCC_except_table3788
- GCC_except_table3789
- GCC_except_table3790
- GCC_except_table3791
- GCC_except_table3792
- GCC_except_table3795
- GCC_except_table3796
- GCC_except_table3802
- GCC_except_table3803
- GCC_except_table3807
- GCC_except_table3808
- GCC_except_table3810
- GCC_except_table3811
- GCC_except_table3814
- GCC_except_table3822
- GCC_except_table3826
- GCC_except_table3905
- GCC_except_table3909
- GCC_except_table3959
- GCC_except_table3960
- GCC_except_table3967
- GCC_except_table3968
- GCC_except_table3969
- GCC_except_table3970
- GCC_except_table3972
- GCC_except_table3973
- GCC_except_table3994
- GCC_except_table3995
- GCC_except_table3996
- GCC_except_table3998
- GCC_except_table3999
- GCC_except_table4000
- GCC_except_table4001
- GCC_except_table4002
- GCC_except_table4005
- GCC_except_table4028
- GCC_except_table4029
- GCC_except_table4030
- GCC_except_table4031
- GCC_except_table4032
- GCC_except_table4033
- GCC_except_table4034
- GCC_except_table4036
- GCC_except_table4037
- GCC_except_table4041
- GCC_except_table4050
- GCC_except_table4052
- GCC_except_table4054
- GCC_except_table4055
- GCC_except_table4062
- GCC_except_table4079
- GCC_except_table4090
- GCC_except_table4097
- GCC_except_table4131
- GCC_except_table4231
- GCC_except_table4238
- GCC_except_table4284
- GCC_except_table4339
- GCC_except_table4351
- GCC_except_table4434
- GCC_except_table4446
- GCC_except_table4451
- GCC_except_table4558
- GCC_except_table475
- GCC_except_table504
- GCC_except_table507
- GCC_except_table512
- GCC_except_table597
- GCC_except_table600
- GCC_except_table603
- GCC_except_table604
- GCC_except_table763
- GCC_except_table770
- GCC_except_table833
- GCC_except_table834
- GCC_except_table841
- GCC_except_table856
- GCC_except_table857
- GCC_except_table858
- GCC_except_table862
- GCC_except_table863
- GCC_except_table864
- GCC_except_table865
- GCC_except_table866
- GCC_except_table868
- GCC_except_table869
- GCC_except_table870
- GCC_except_table873
- GCC_except_table874
- GCC_except_table875
- GCC_except_table877
- GCC_except_table878
- GCC_except_table893
- _AudioConverterFillComplexBuffer_BlockInvoke.7163
- _OBJC_IVAR_$_CSRemoteAssetManager._exclaveAssetsController
- ___58-[CSRemoteAssetManager _loadPreinstalledAssetMetaIfNeeded]_block_invoke
- ___Block_byref_object_copy_.12504
- ___Block_byref_object_copy_.12902
- ___Block_byref_object_copy_.13199
- ___Block_byref_object_copy_.13446
- ___Block_byref_object_copy_.13945
- ___Block_byref_object_copy_.14511
- ___Block_byref_object_copy_.14595
- ___Block_byref_object_copy_.1541
- ___Block_byref_object_copy_.15462
- ___Block_byref_object_copy_.2084
- ___Block_byref_object_copy_.2494
- ___Block_byref_object_copy_.3251
- ___Block_byref_object_copy_.4565
- ___Block_byref_object_copy_.4785
- ___Block_byref_object_copy_.5635
- ___Block_byref_object_copy_.6046
- ___Block_byref_object_copy_.7751
- ___Block_byref_object_copy_.8025
- ___Block_byref_object_copy_.8474
- ___Block_byref_object_copy_.9232
- ___Block_byref_object_dispose_.12505
- ___Block_byref_object_dispose_.12903
- ___Block_byref_object_dispose_.13200
- ___Block_byref_object_dispose_.13447
- ___Block_byref_object_dispose_.13946
- ___Block_byref_object_dispose_.14512
- ___Block_byref_object_dispose_.14596
- ___Block_byref_object_dispose_.1542
- ___Block_byref_object_dispose_.15463
- ___Block_byref_object_dispose_.2085
- ___Block_byref_object_dispose_.2495
- ___Block_byref_object_dispose_.3252
- ___Block_byref_object_dispose_.4566
- ___Block_byref_object_dispose_.4786
- ___Block_byref_object_dispose_.5636
- ___Block_byref_object_dispose_.6047
- ___Block_byref_object_dispose_.7752
- ___Block_byref_object_dispose_.8026
- ___Block_byref_object_dispose_.8475
- ___Block_byref_object_dispose_.9233
- ___block_literal_global.10109
- ___block_literal_global.10206
- ___block_literal_global.11079
- ___block_literal_global.11284
- ___block_literal_global.11439
- ___block_literal_global.11656
- ___block_literal_global.11693
- ___block_literal_global.12550
- ___block_literal_global.13015
- ___block_literal_global.1311
- ___block_literal_global.13299
- ___block_literal_global.13545
- ___block_literal_global.13851
- ___block_literal_global.1398
- ___block_literal_global.141
- ___block_literal_global.14234
- ___block_literal_global.1426
- ___block_literal_global.14336
- ___block_literal_global.14392
- ___block_literal_global.1453
- ___block_literal_global.14537
- ___block_literal_global.146
- ___block_literal_global.14831
- ___block_literal_global.14920
- ___block_literal_global.1497
- ___block_literal_global.151
- ___block_literal_global.15249
- ___block_literal_global.15487
- ___block_literal_global.1568
- ___block_literal_global.164
- ___block_literal_global.175
- ___block_literal_global.180.8152
- ___block_literal_global.20.13000
- ___block_literal_global.2101
- ___block_literal_global.2194
- ___block_literal_global.2250
- ___block_literal_global.2435
- ___block_literal_global.245
- ___block_literal_global.2510
- ___block_literal_global.256
- ___block_literal_global.261
- ___block_literal_global.2619
- ___block_literal_global.266
- ___block_literal_global.2668
- ___block_literal_global.268
- ___block_literal_global.27.8269
- ___block_literal_global.276.8093
- ___block_literal_global.2980
- ___block_literal_global.312
- ___block_literal_global.3163
- ___block_literal_global.317
- ___block_literal_global.322
- ___block_literal_global.327
- ___block_literal_global.3271
- ___block_literal_global.33
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.354
- ___block_literal_global.3575
- ___block_literal_global.360
- ___block_literal_global.365
- ___block_literal_global.370
- ___block_literal_global.3728
- ___block_literal_global.394
- ___block_literal_global.399
- ___block_literal_global.3993
- ___block_literal_global.404
- ___block_literal_global.406
- ___block_literal_global.41.8256
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.421
- ___block_literal_global.426
- ___block_literal_global.429
- ___block_literal_global.434
- ___block_literal_global.442
- ___block_literal_global.447
- ___block_literal_global.455
- ___block_literal_global.4593
- ___block_literal_global.46
- ___block_literal_global.460
- ___block_literal_global.465
- ___block_literal_global.470
- ___block_literal_global.475
- ___block_literal_global.4753
- ___block_literal_global.4801
- ___block_literal_global.486
- ___block_literal_global.491
- ___block_literal_global.496
- ___block_literal_global.51
- ___block_literal_global.511
- ___block_literal_global.516
- ___block_literal_global.527
- ___block_literal_global.532
- ___block_literal_global.5403
- ___block_literal_global.543
- ___block_literal_global.5487
- ___block_literal_global.551
- ___block_literal_global.6268
- ___block_literal_global.6415
- ___block_literal_global.6483
- ___block_literal_global.6540
- ___block_literal_global.6656
- ___block_literal_global.6674
- ___block_literal_global.6868
- ___block_literal_global.6931
- ___block_literal_global.6991
- ___block_literal_global.7092
- ___block_literal_global.7128
- ___block_literal_global.7413
- ___block_literal_global.8282
- ___block_literal_global.8302
- ___block_literal_global.8357
- ___block_literal_global.8758
- ___block_literal_global.8820
- ___block_literal_global.8967
- ___block_literal_global.9024
- ___block_literal_global.9259
- ___block_literal_global.9566
- ___block_literal_global.9697
- ___block_literal_global.9805
- _sharedHandler.onceToken.12549
- _sharedHandler.sharedHandler.12551
- _sharedInstance._sharedInstance.10207
- _sharedInstance._sharedInstance.11080
- _sharedInstance._sharedInstance.11694
- _sharedInstance._sharedInstance.14337
- _sharedInstance._sharedInstance.14393
- _sharedInstance._sharedInstance.14832
- _sharedInstance._sharedInstance.14921
- _sharedInstance._sharedInstance.3994
- _sharedInstance._sharedInstance.4754
- _sharedInstance._sharedInstance.5404
- _sharedInstance._sharedInstance.6269
- _sharedInstance._sharedInstance.6869
- _sharedInstance._sharedInstance.7093
- _sharedInstance._sharedInstance.7414
- _sharedInstance.onceToken.10205
- _sharedInstance.onceToken.11078
- _sharedInstance.onceToken.11283
- _sharedInstance.onceToken.11692
- _sharedInstance.onceToken.1310
- _sharedInstance.onceToken.13298
- _sharedInstance.onceToken.1425
- _sharedInstance.onceToken.14335
- _sharedInstance.onceToken.14391
- _sharedInstance.onceToken.14737
- _sharedInstance.onceToken.14830
- _sharedInstance.onceToken.14919
- _sharedInstance.onceToken.1496
- _sharedInstance.onceToken.15248
- _sharedInstance.onceToken.15486
- _sharedInstance.onceToken.1567
- _sharedInstance.onceToken.2193
- _sharedInstance.onceToken.2249
- _sharedInstance.onceToken.2509
- _sharedInstance.onceToken.3270
- _sharedInstance.onceToken.3727
- _sharedInstance.onceToken.3992
- _sharedInstance.onceToken.4592
- _sharedInstance.onceToken.4752
- _sharedInstance.onceToken.4800
- _sharedInstance.onceToken.5402
- _sharedInstance.onceToken.6267
- _sharedInstance.onceToken.6414
- _sharedInstance.onceToken.6655
- _sharedInstance.onceToken.6867
- _sharedInstance.onceToken.7091
- _sharedInstance.onceToken.7412
- _sharedInstance.onceToken.8301
- _sharedInstance.onceToken.8356
- _sharedInstance.onceToken.8819
- _sharedInstance.onceToken.9023
- _sharedInstance.onceToken.9565
- _sharedInstance.onceToken.9696
- _sharedInstance.onceToken.9804
- _sharedInstance.sharedInstance.11285
- _sharedInstance.sharedInstance.1312
- _sharedInstance.sharedInstance.13300
- _sharedInstance.sharedInstance.14739
- _sharedInstance.sharedInstance.15250
- _sharedInstance.sharedInstance.15488
- _sharedInstance.sharedInstance.2195
- _sharedInstance.sharedInstance.2251
- _sharedInstance.sharedInstance.2511
- _sharedInstance.sharedInstance.3272
- _sharedInstance.sharedInstance.3729
- _sharedInstance.sharedInstance.4802
- _sharedInstance.sharedInstance.6416
- _sharedInstance.sharedInstance.8303
- _sharedInstance.sharedInstance.8821
- _sharedInstance.sharedInstance.9025
- _sharedInstance.sharedInstance.9698
- _sharedInstance.sharedInstance.9806
- _sharedInstance.sharedManager.6657
- _sharedInstance.sharedManager.8358
- _sharedLogger.onceToken.13850
- _sharedLogger.onceToken.2618
- _sharedLogger.onceToken.6482
- _sharedLogger.onceToken.6673
- _sharedLogger.shared.13852
- _sharedManager.onceToken.14536
- _sharedMonitor.onceToken.5486
- _sharedMonitor.sharedMonitor.5488
- _sharedPreferences.onceToken.8757
CStrings:
+ "%s CSAudioProvider[%{public}@]:Audio Recorder Secure Sensor Invalidated"
+ "%s Language code requested: %@, Cached asset language code: %@. Returning cached asset"
+ "%s LanguageCode setting not found. Falling back to en-US asset"
+ "%s Secure sensor status invalidated"
+ "-[CSAudioProvider audioRecorderSensorInvalidated:]"
+ "-[CSAudioRecorder fetchSecureAudioStreamWithRecordDeviceIndicator:from:numSamples:hostTime:error:]"
+ "-[CSRemoteAssetManagerDarwinExclave _languageCode]"
+ "-[CSRemoteAssetManagerDarwinExclave assetForCurrentLanguageOfType:]_block_invoke"
+ "-[CSRemoteAssetManagerDarwinExclave setLanguageCode:resourcePath:configVersion:assetHash:assetType:]"
+ "@\"CSAsset\""
+ "@\"CSAsset\"24@0:8Q16"
+ "@\"CSRemoteAssetCache\""
+ "@\"NSString\"24@0:8Q16"
+ "CSRemoteAssetCache"
+ "CSRemoteAssetManagerDarwinExclave"
+ "CSRemoteAssetManagerFactory"
+ "CSRemoteAssetManagerProtocol"
+ "Exclave Siri Fast Start"
+ "SecureAssetTypeUtils"
+ "SecureAssetsPreinstalledBundle"
+ "T@\"CSAsset\",R,N,V_asset"
+ "T@\"NSString\",R,N,V_languageCode"
+ "_asset"
+ "_assetCache"
+ "asset"
+ "assetVersion:"
+ "audioRecorderSensorInvalidated:"
+ "com.apple.corespeech.remoteAssetManagerExclave"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClasses:forKey:"
+ "decodedInfo"
+ "encodeInteger:forKey:"
+ "getVoiceTriggerAssetBundle"
+ "init:"
+ "initWithAsset:languageCode:"
+ "initWithExclaveAssetsController:"
+ "needRetrainingForExclaveOnly"
+ "octopus_siri_darkwake"
+ "remoteAssetManager"
+ "resourcePathURL:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils"
+ "useExclaveFastStart"
+ "v32@0:8@\"<CSRemoteAssetManagerDelegate>\"16Q24"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40Q48"
- "-[CSRemoteAssetManager _loadPreinstalledAssetMetaIfNeeded]_block_invoke"

```
