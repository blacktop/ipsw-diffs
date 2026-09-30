## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3500.97.2.1.1
-  __TEXT.__text: 0x8b55c
+3500.104.2.0.0
+  __TEXT.__text: 0x8bbb0
   __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x64a0
+  __TEXT.__objc_methlist: 0x64f8
   __TEXT.__const: 0x4c8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0xfb18
+  __TEXT.__cstring: 0xfba6
   __TEXT.__swift5_typeref: 0xea
   __TEXT.__constg_swiftt: 0x320
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x18a
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2cd8
-  __TEXT.__oslogstring: 0xc592
-  __TEXT.__unwind_info: 0x1878
-  __TEXT.__objc_classname: 0xd8f
-  __TEXT.__objc_methname: 0x118dc
-  __TEXT.__objc_methtype: 0x2487
-  __TEXT.__objc_stubs: 0xa3e0
-  __DATA_CONST.__got: 0x930
-  __DATA_CONST.__const: 0x1cc8
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __TEXT.__gcc_except_tab: 0x2d40
+  __TEXT.__oslogstring: 0xc5bb
+  __TEXT.__unwind_info: 0x1890
+  __TEXT.__objc_classname: 0xda6
+  __TEXT.__objc_methname: 0x11a29
+  __TEXT.__objc_methtype: 0x24a3
+  __TEXT.__objc_stubs: 0xa4e0
+  __DATA_CONST.__got: 0x938
+  __DATA_CONST.__const: 0x1cd0
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ad8
+  __DATA_CONST.__objc_selrefs: 0x3b20
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x3b0
   __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x5100
-  __AUTH_CONST.__objc_const: 0xa980
+  __AUTH_CONST.__cfstring: 0x51a0
+  __AUTH_CONST.__objc_const: 0xaa70
   __AUTH_CONST.__objc_dictobj: 0x938
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x18b0
+  __AUTH.__objc_data: 0x1900
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x818
+  __DATA.__objc_ivar: 0x820
   __DATA.__data: 0x1000
   __DATA.__bss: 0xf0
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4957430A-EA08-3932-A676-76B294117352
-  Functions: 2365
-  Symbols:   8129
-  CStrings:  6012
+  UUID: E0352D7F-EE84-35CC-8F7E-09C9B52ACEF5
+  Functions: 2373
+  Symbols:   8153
+  CStrings:  6037
 
Symbols:
+ +[SSRUtils getEmbeddingFileName:]
+ +[SSRUtils needProfileEmbeddingsForDarwin]
+ -[SSRSecureAssetProvider _fetchSecureAssetForCommunalDevice:]
+ -[SSRSecureAssetProvider _fetchSecureAssetForNonCommunalDevice:withAsset:]
+ -[SSRSecureAssetProvider _secureAssetWithAssetResourcePathURL:assetFileName:assetVersion:]
+ -[SSRSecureAssetProvider fetchSecureAssetForLocale:withAsset:]
+ -[SSRSpeakerRecognitionContext secureAsset]
+ -[SSRSpeakerRecognitionContext setSecureAsset:]
+ -[SSRVoiceProfileComposer _addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:withError:]
+ -[SSRVoiceProfileComposer addUtterance:toProfile:withAsset:error:]
+ -[SSRVoiceProfileComposer addUtterance:toProfile:withSecureAsset:error:]
+ -[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]
+ -[SSRVoiceProfileRetrainingContext secureAsset]
+ -[SSRVoiceProfileRetrainingContext setSecureAsset:]
+ GCC_except_table1053
+ GCC_except_table1075
+ GCC_except_table1129
+ GCC_except_table1133
+ GCC_except_table1151
+ GCC_except_table1239
+ GCC_except_table1240
+ GCC_except_table1394
+ GCC_except_table1443
+ GCC_except_table1458
+ GCC_except_table1474
+ GCC_except_table1481
+ GCC_except_table1551
+ GCC_except_table1658
+ GCC_except_table1664
+ GCC_except_table1679
+ GCC_except_table1689
+ GCC_except_table1699
+ GCC_except_table1704
+ GCC_except_table1720
+ GCC_except_table1724
+ GCC_except_table1728
+ GCC_except_table1734
+ GCC_except_table1742
+ GCC_except_table1806
+ GCC_except_table1810
+ GCC_except_table1852
+ GCC_except_table1887
+ GCC_except_table1952
+ GCC_except_table1961
+ GCC_except_table1970
+ GCC_except_table1981
+ GCC_except_table1990
+ GCC_except_table2009
+ GCC_except_table2039
+ GCC_except_table732
+ GCC_except_table808
+ GCC_except_table849
+ GCC_except_table854
+ GCC_except_table870
+ GCC_except_table873
+ GCC_except_table955
+ GCC_except_table956
+ GCC_except_table959
+ GCC_except_table960
+ GCC_except_table971
+ GCC_except_table976
+ _OBJC_CLASS_$_SSRSecureAssetProvider
+ _OBJC_IVAR_$_SSRSpeakerRecognitionContext._secureAsset
+ _OBJC_IVAR_$_SSRVoiceProfileRetrainingContext._secureAsset
+ _OBJC_METACLASS_$_SSRSecureAssetProvider
+ __OBJC_$_INSTANCE_METHODS_SSRSecureAssetProvider
+ __OBJC_CLASS_RO_$_SSRSecureAssetProvider
+ __OBJC_METACLASS_RO_$_SSRSecureAssetProvider
+ ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke
+ ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.328
+ ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.342
+ ___87-[SSRVTUITrainingManager CSVTUITrainingSession:hasTrainUtterance:languageCode:payload:]_block_invoke
+ ___Block_byref_object_copy_.2041
+ ___Block_byref_object_copy_.2270
+ ___Block_byref_object_copy_.2435
+ ___Block_byref_object_copy_.3115
+ ___Block_byref_object_copy_.3699
+ ___Block_byref_object_copy_.3854
+ ___Block_byref_object_copy_.4014
+ ___Block_byref_object_copy_.4803
+ ___Block_byref_object_copy_.5156
+ ___Block_byref_object_copy_.5289
+ ___Block_byref_object_copy_.5498
+ ___Block_byref_object_copy_.5692
+ ___Block_byref_object_copy_.5896
+ ___Block_byref_object_copy_.6728
+ ___Block_byref_object_copy_.7183
+ ___Block_byref_object_copy_.7297
+ ___Block_byref_object_copy_.7523
+ ___Block_byref_object_copy_.7874
+ ___Block_byref_object_copy_.8373
+ ___Block_byref_object_dispose_.2042
+ ___Block_byref_object_dispose_.2271
+ ___Block_byref_object_dispose_.2436
+ ___Block_byref_object_dispose_.3116
+ ___Block_byref_object_dispose_.3700
+ ___Block_byref_object_dispose_.3855
+ ___Block_byref_object_dispose_.4015
+ ___Block_byref_object_dispose_.4804
+ ___Block_byref_object_dispose_.5157
+ ___Block_byref_object_dispose_.5290
+ ___Block_byref_object_dispose_.5499
+ ___Block_byref_object_dispose_.5693
+ ___Block_byref_object_dispose_.5897
+ ___Block_byref_object_dispose_.6729
+ ___Block_byref_object_dispose_.7184
+ ___Block_byref_object_dispose_.7298
+ ___Block_byref_object_dispose_.7524
+ ___Block_byref_object_dispose_.7875
+ ___Block_byref_object_dispose_.8374
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.2049
+ ___block_literal_global.3003
+ ___block_literal_global.3875
+ ___block_literal_global.3937
+ ___block_literal_global.4466
+ ___block_literal_global.4846
+ ___block_literal_global.5034
+ ___block_literal_global.5981
+ ___block_literal_global.6183
+ ___block_literal_global.6792
+ ___block_literal_global.7307
+ ___block_literal_global.7557
+ ___block_literal_global.7748
+ ___block_literal_global.8025
+ ___block_literal_global.8213
+ ___block_literal_global.8628
+ ___block_literal_global.8997
+ _objc_msgSend$_addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:withError:
+ _objc_msgSend$_fetchSecureAssetForNonCommunalDevice:withAsset:
+ _objc_msgSend$_secureAssetWithAssetResourcePathURL:assetFileName:assetVersion:
+ _objc_msgSend$addUtterance:toProfile:withAsset:error:
+ _objc_msgSend$addUtterance:toProfile:withSecureAsset:error:
+ _objc_msgSend$assetHash
+ _objc_msgSend$assetVersion
+ _objc_msgSend$assetVersion:
+ _objc_msgSend$fetchSecureAssetForLocale:withAsset:
+ _objc_msgSend$getEmbeddingFileName:
+ _objc_msgSend$importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:
+ _objc_msgSend$initWithResourcePath:assetFileName:assetVersion:assetHash:
+ _objc_msgSend$needProfileEmbeddingsForDarwin
+ _objc_msgSend$setPersonaId:
+ _sharedInstance.onceToken.3936
+ _sharedInstance.onceToken.8024
+ _sharedInstance.onceToken.8212
+ _sharedManager.onceToken.7556
- -[SSRVoiceProfileComposer _addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:]
- -[SSRVoiceProfileComposer addUtterance:toProfile:withAsset:]
- -[SSRVoiceProfileComposer addUtterance:toProfile:withSecureAsset:]
- -[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]
- -[SSRVoiceProfileRetrainerFactory _fetchSecureAssetForCommunalDevice:]
- -[SSRVoiceProfileRetrainerFactory _fetchSecureAssetForNonCommunalDevice:]
- -[SSRVoiceProfileRetrainerFactory _secureAssetWithAssetResourcePathURL:assetFileName:]
- GCC_except_table1055
- GCC_except_table1077
- GCC_except_table1131
- GCC_except_table1135
- GCC_except_table1153
- GCC_except_table1241
- GCC_except_table1244
- GCC_except_table1392
- GCC_except_table1441
- GCC_except_table1456
- GCC_except_table1472
- GCC_except_table1479
- GCC_except_table1549
- GCC_except_table1656
- GCC_except_table1662
- GCC_except_table1677
- GCC_except_table1687
- GCC_except_table1697
- GCC_except_table1702
- GCC_except_table1718
- GCC_except_table1722
- GCC_except_table1726
- GCC_except_table1732
- GCC_except_table1740
- GCC_except_table1804
- GCC_except_table1808
- GCC_except_table1850
- GCC_except_table1885
- GCC_except_table1950
- GCC_except_table1959
- GCC_except_table1968
- GCC_except_table1979
- GCC_except_table1988
- GCC_except_table2007
- GCC_except_table2037
- GCC_except_table731
- GCC_except_table810
- GCC_except_table851
- GCC_except_table856
- GCC_except_table872
- GCC_except_table875
- GCC_except_table957
- GCC_except_table958
- GCC_except_table969
- GCC_except_table972
- GCC_except_table975
- GCC_except_table978
- ___128-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]_block_invoke
- ___128-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]_block_invoke.328
- ___128-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]_block_invoke.342
- ___Block_byref_object_copy_.2039
- ___Block_byref_object_copy_.2285
- ___Block_byref_object_copy_.2450
- ___Block_byref_object_copy_.3137
- ___Block_byref_object_copy_.3719
- ___Block_byref_object_copy_.3874
- ___Block_byref_object_copy_.4033
- ___Block_byref_object_copy_.4820
- ___Block_byref_object_copy_.5175
- ___Block_byref_object_copy_.5308
- ___Block_byref_object_copy_.5512
- ___Block_byref_object_copy_.5709
- ___Block_byref_object_copy_.5913
- ___Block_byref_object_copy_.6749
- ___Block_byref_object_copy_.7200
- ___Block_byref_object_copy_.7314
- ___Block_byref_object_copy_.7540
- ___Block_byref_object_copy_.7896
- ___Block_byref_object_copy_.8395
- ___Block_byref_object_dispose_.2040
- ___Block_byref_object_dispose_.2286
- ___Block_byref_object_dispose_.2451
- ___Block_byref_object_dispose_.3138
- ___Block_byref_object_dispose_.3720
- ___Block_byref_object_dispose_.3875
- ___Block_byref_object_dispose_.4034
- ___Block_byref_object_dispose_.4821
- ___Block_byref_object_dispose_.5176
- ___Block_byref_object_dispose_.5309
- ___Block_byref_object_dispose_.5513
- ___Block_byref_object_dispose_.5710
- ___Block_byref_object_dispose_.5914
- ___Block_byref_object_dispose_.6750
- ___Block_byref_object_dispose_.7201
- ___Block_byref_object_dispose_.7315
- ___Block_byref_object_dispose_.7541
- ___Block_byref_object_dispose_.7897
- ___Block_byref_object_dispose_.8396
- ___block_literal_global.2047
- ___block_literal_global.3017
- ___block_literal_global.3895
- ___block_literal_global.3956
- ___block_literal_global.4485
- ___block_literal_global.4863
- ___block_literal_global.5053
- ___block_literal_global.5998
- ___block_literal_global.6200
- ___block_literal_global.6813
- ___block_literal_global.7324
- ___block_literal_global.7574
- ___block_literal_global.7774
- ___block_literal_global.8047
- ___block_literal_global.8235
- ___block_literal_global.8650
- ___block_literal_global.9008
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SpeakerRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SpeakerRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SpeakerRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SpeakerRecognition
- _objc_msgSend$_addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:
- _objc_msgSend$_fetchSecureAssetForNonCommunalDevice:
- _objc_msgSend$addUtterance:toProfile:withAsset:
- _objc_msgSend$addUtterance:toProfile:withSecureAsset:
- _objc_msgSend$importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:
- _objc_msgSend$initWithResourcePath:assetFileName:
- _sharedInstance.onceToken.3955
- _sharedInstance.onceToken.8046
- _sharedInstance.onceToken.8234
- _sharedManager.onceToken.7573
CStrings:
+ "%@_%@"
+ "%s asset hash is %@, asset version is %@"
+ "+[SSRUtils getEmbeddingFileName:]"
+ "-[SSRSecureAssetProvider _fetchSecureAssetForCommunalDevice:]"
+ "-[SSRSecureAssetProvider _fetchSecureAssetForNonCommunalDevice:withAsset:]"
+ "-[SSRVoiceProfileComposer _addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:withError:]"
+ "-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]"
+ "-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke"
+ "0.0"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32d40^@48"
+ "SSRSecureAssetProvider"
+ "T@\"SecureAsset\",&,N,V_secureAsset"
+ "_addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:withError:"
+ "_fetchSecureAssetForNonCommunalDevice:withAsset:"
+ "_secureAsset"
+ "_secureAssetWithAssetResourcePathURL:assetFileName:assetVersion:"
+ "addUtterance:toProfile:withAsset:error:"
+ "addUtterance:toProfile:withSecureAsset:error:"
+ "assetHash"
+ "assetVersion"
+ "assetVersion:"
+ "com.apple.speakerrecognition.enrollment"
+ "fetchSecureAssetForLocale:withAsset:"
+ "getEmbeddingFileName:"
+ "importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:"
+ "initWithResourcePath:assetFileName:assetVersion:assetHash:"
+ "needProfileEmbeddingsForDarwin"
+ "nohash"
+ "secureAsset"
+ "setSecureAsset:"
+ "utteranceAdditionErrorCode"
+ "v76@0:8@16@24@32@40@48@56B64@?68"
- "-[SSRVoiceProfileComposer _addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:]"
- "-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]"
- "-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:]_block_invoke"
- "-[SSRVoiceProfileRetrainerFactory _fetchSecureAssetForCommunalDevice:]"
- "-[SSRVoiceProfileRetrainerFactory _fetchSecureAssetForNonCommunalDevice:]"
- "B48@0:8@16@24@32d40"
- "_addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:"
- "_fetchSecureAssetForNonCommunalDevice:"
- "addUtterance:toProfile:withAsset:"
- "addUtterance:toProfile:withSecureAsset:"
- "importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:doUtteranceDonation:withCompletion:"
- "initWithResourcePath:assetFileName:"
- "v68@0:8@16@24@32@40@48B56@?60"

```
