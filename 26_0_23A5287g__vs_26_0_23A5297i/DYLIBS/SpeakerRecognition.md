## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3500.110.4.0.0
-  __TEXT.__text: 0x8bba8
+3500.115.2.0.0
+  __TEXT.__text: 0x8beac
   __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x64f8
+  __TEXT.__objc_methlist: 0x6530
   __TEXT.__const: 0x4c8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0xfba6
+  __TEXT.__cstring: 0xfc2a
   __TEXT.__swift5_typeref: 0xea
   __TEXT.__constg_swiftt: 0x320
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x18a
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2d40
+  __TEXT.__gcc_except_tab: 0x2d34
   __TEXT.__oslogstring: 0xc5bb
-  __TEXT.__unwind_info: 0x1890
+  __TEXT.__unwind_info: 0x18b0
   __TEXT.__objc_classname: 0xda6
-  __TEXT.__objc_methname: 0x11a29
+  __TEXT.__objc_methname: 0x11afc
   __TEXT.__objc_methtype: 0x24a3
-  __TEXT.__objc_stubs: 0xa4e0
+  __TEXT.__objc_stubs: 0xa520
   __DATA_CONST.__got: 0x938
   __DATA_CONST.__const: 0x1cd0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b20
+  __DATA_CONST.__objc_selrefs: 0x3b40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0x3b0
+  __DATA_CONST.__objc_arraydata: 0x3c0
   __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x51a0
+  __AUTH_CONST.__cfstring: 0x51c0
   __AUTH_CONST.__objc_const: 0xaa70
-  __AUTH_CONST.__objc_dictobj: 0x938
+  __AUTH_CONST.__objc_dictobj: 0x960
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E3F870A1-8502-31C8-8D99-BC52E878C94B
-  Functions: 2373
-  Symbols:   8153
-  CStrings:  6037
+  UUID: E2F97BFD-DC91-3957-A5C2-62ABD41DB8E2
+  Functions: 2377
+  Symbols:   8163
+  CStrings:  6044
 
Symbols:
+ +[SSRRPISampledAudioUploader _getAudioFileMetadata:]
+ +[SSRRPISampledAudioUploader _uploadAudioFilePath:requestId:audioId:metadataDict:completion:]
+ +[SSRRPISampledAudioUploader uploadAudioFilePath:requestId:audioId:completion:]
+ -[SSRVoiceProfileManager _updateUserProfileAndAddVoiceProfile:withCompletion:]
+ -[SSRVoiceProfileManager updateVoiceProfileIdInUserProfile:personaId:completion:]
+ GCC_except_table1345
+ GCC_except_table1351
+ GCC_except_table1355
+ GCC_except_table1362
+ GCC_except_table1368
+ GCC_except_table1397
+ GCC_except_table1446
+ GCC_except_table1461
+ GCC_except_table1477
+ GCC_except_table1484
+ GCC_except_table1554
+ GCC_except_table1662
+ GCC_except_table1668
+ GCC_except_table1683
+ GCC_except_table1693
+ GCC_except_table1703
+ GCC_except_table1708
+ GCC_except_table1732
+ GCC_except_table1738
+ GCC_except_table1746
+ GCC_except_table1814
+ GCC_except_table1856
+ GCC_except_table1891
+ GCC_except_table1956
+ GCC_except_table1965
+ GCC_except_table1974
+ GCC_except_table1985
+ GCC_except_table1994
+ GCC_except_table2013
+ GCC_except_table2043
+ ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.335
+ ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.349
+ ___93+[SSRRPISampledAudioUploader _uploadAudioFilePath:requestId:audioId:metadataDict:completion:]_block_invoke
+ ___Block_byref_object_copy_.5164
+ ___Block_byref_object_copy_.5297
+ ___Block_byref_object_copy_.5506
+ ___Block_byref_object_copy_.5700
+ ___Block_byref_object_copy_.5904
+ ___Block_byref_object_copy_.6741
+ ___Block_byref_object_copy_.7167
+ ___Block_byref_object_copy_.7281
+ ___Block_byref_object_copy_.7507
+ ___Block_byref_object_copy_.7859
+ ___Block_byref_object_copy_.8359
+ ___Block_byref_object_dispose_.5165
+ ___Block_byref_object_dispose_.5298
+ ___Block_byref_object_dispose_.5507
+ ___Block_byref_object_dispose_.5701
+ ___Block_byref_object_dispose_.5905
+ ___Block_byref_object_dispose_.6742
+ ___Block_byref_object_dispose_.7168
+ ___Block_byref_object_dispose_.7282
+ ___Block_byref_object_dispose_.7508
+ ___Block_byref_object_dispose_.7860
+ ___Block_byref_object_dispose_.8360
+ ___block_descriptor_56_e8_32s40s48r_e20_v20?0B8"NSError"12ls32l8r48l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.5057
+ ___block_literal_global.5989
+ ___block_literal_global.6191
+ ___block_literal_global.6776
+ ___block_literal_global.7291
+ ___block_literal_global.7541
+ ___block_literal_global.7738
+ ___block_literal_global.8011
+ ___block_literal_global.8199
+ ___block_literal_global.8614
+ ___block_literal_global.8983
+ _objc_msgSend$_getAudioFileMetadata:
+ _objc_msgSend$_uploadAudioFilePath:requestId:audioId:metadataDict:completion:
+ _sharedInstance.onceToken.8010
+ _sharedInstance.onceToken.8198
+ _sharedManager.onceToken.7540
- -[SSRVoiceProfileManager updateVoiceProfileIDInUserProfile:]
- GCC_except_table1342
- GCC_except_table1348
- GCC_except_table1352
- GCC_except_table1356
- GCC_except_table1365
- GCC_except_table1394
- GCC_except_table1443
- GCC_except_table1458
- GCC_except_table1474
- GCC_except_table1481
- GCC_except_table1551
- GCC_except_table1658
- GCC_except_table1664
- GCC_except_table1679
- GCC_except_table1689
- GCC_except_table1699
- GCC_except_table1704
- GCC_except_table1720
- GCC_except_table1734
- GCC_except_table1742
- GCC_except_table1806
- GCC_except_table1852
- GCC_except_table1887
- GCC_except_table1952
- GCC_except_table1961
- GCC_except_table1970
- GCC_except_table1981
- GCC_except_table1990
- GCC_except_table2009
- GCC_except_table2039
- ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.328
- ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.342
- ___83+[SSRRPISampledAudioUploader uploadAudioFileWithRequestId:audioId:date:completion:]_block_invoke
- ___Block_byref_object_copy_.5156
- ___Block_byref_object_copy_.5289
- ___Block_byref_object_copy_.5498
- ___Block_byref_object_copy_.5692
- ___Block_byref_object_copy_.5896
- ___Block_byref_object_copy_.6728
- ___Block_byref_object_copy_.7183
- ___Block_byref_object_copy_.7297
- ___Block_byref_object_copy_.7523
- ___Block_byref_object_copy_.7874
- ___Block_byref_object_copy_.8373
- ___Block_byref_object_dispose_.5157
- ___Block_byref_object_dispose_.5290
- ___Block_byref_object_dispose_.5499
- ___Block_byref_object_dispose_.5693
- ___Block_byref_object_dispose_.5897
- ___Block_byref_object_dispose_.6729
- ___Block_byref_object_dispose_.7184
- ___Block_byref_object_dispose_.7298
- ___Block_byref_object_dispose_.7524
- ___Block_byref_object_dispose_.7875
- ___Block_byref_object_dispose_.8374
- ___block_descriptor_57_e8_32s40r48r_e5_v8?0lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0B8"NSError"12ls32l8r48l8r56l8s40l8
- ___block_literal_global.5034
- ___block_literal_global.5981
- ___block_literal_global.6183
- ___block_literal_global.6792
- ___block_literal_global.7307
- ___block_literal_global.7557
- ___block_literal_global.7748
- ___block_literal_global.8025
- ___block_literal_global.8213
- ___block_literal_global.8628
- ___block_literal_global.8997
- _sharedInstance.onceToken.8024
- _sharedInstance.onceToken.8212
- _sharedManager.onceToken.7556
CStrings:
+ "+[SSRRPISampledAudioUploader _uploadAudioFilePath:requestId:audioId:metadataDict:completion:]"
+ "Cannot get metadata for requestId: %@"
+ "_getAudioFileMetadata:"
+ "_updateUserProfileAndAddVoiceProfile:withCompletion:"
+ "_uploadAudioFilePath:requestId:audioId:metadataDict:completion:"
+ "updateVoiceProfileIdInUserProfile:personaId:completion:"
+ "uploadAudioFilePath:requestId:audioId:completion:"
- "updateVoiceProfileIDInUserProfile:"

```
