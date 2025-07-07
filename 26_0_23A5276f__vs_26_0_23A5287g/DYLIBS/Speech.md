## Speech

> `/System/Library/Frameworks/Speech.framework/Speech`

```diff

-3500.93.1.0.0
-  __TEXT.__text: 0x1d0dd4
-  __TEXT.__auth_stubs: 0x2ba0
-  __TEXT.__objc_methlist: 0x45d4
-  __TEXT.__const: 0xc858
-  __TEXT.__cstring: 0xa851
+3500.97.2.0.0
+  __TEXT.__text: 0x1d1a68
+  __TEXT.__auth_stubs: 0x2bb0
+  __TEXT.__objc_methlist: 0x45ec
+  __TEXT.__const: 0xc870
+  __TEXT.__cstring: 0xa85b
   __TEXT.__constg_swiftt: 0x4430
   __TEXT.__swift5_typeref: 0x62ac
   __TEXT.__swift5_reflstr: 0x4575

   __TEXT.__swift5_assocty: 0x9c0
   __TEXT.__swift5_proto: 0x864
   __TEXT.__swift5_types: 0x358
-  __TEXT.__oslogstring: 0x3f77
-  __TEXT.__swift5_capture: 0x26c4
+  __TEXT.__oslogstring: 0x3f97
+  __TEXT.__swift5_capture: 0x26e4
   __TEXT.__swift5_acfuncs: 0x564
   __TEXT.__swift_as_entry: 0x9fc
   __TEXT.__swift_as_ret: 0xa0c
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x868
-  __TEXT.__unwind_info: 0x8ae8
-  __TEXT.__eh_frame: 0x120c0
+  __TEXT.__gcc_except_tab: 0x890
+  __TEXT.__unwind_info: 0x87b0
+  __TEXT.__eh_frame: 0x12108
   __TEXT.__objc_classname: 0xadc
-  __TEXT.__objc_methname: 0xe23e
-  __TEXT.__objc_methtype: 0x2a3d
-  __TEXT.__objc_stubs: 0x4e60
+  __TEXT.__objc_methname: 0xe2cc
+  __TEXT.__objc_methtype: 0x2a5b
+  __TEXT.__objc_stubs: 0x4ec0
   __DATA_CONST.__got: 0xd70
   __DATA_CONST.__const: 0x1428
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bb8
+  __DATA_CONST.__objc_selrefs: 0x2bd8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x15e0
-  __AUTH_CONST.__const: 0xbcb0
+  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__const: 0xbcd0
   __AUTH_CONST.__cfstring: 0x3f20
   __AUTH_CONST.__objc_const: 0xcd20
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__objc_data: 0x1540
   __AUTH.__data: 0x2990
   __DATA.__objc_ivar: 0x574
-  __DATA.__data: 0x3988
+  __DATA.__data: 0x3948
   __DATA.__common: 0x300
   __DATA.__bss: 0xdc80
   __DATA_DIRTY.__objc_data: 0xf08
   __DATA_DIRTY.__data: 0x2b18
-  __DATA_DIRTY.__bss: 0x4d9
+  __DATA_DIRTY.__bss: 0x4e9
   __DATA_DIRTY.__common: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 228E4992-6BA6-3B90-8985-33E7C279C186
-  Functions: 12658
-  Symbols:   14554
-  CStrings:  4455
+  UUID: A5047C1C-4CAF-3A49-B2B2-AF028EBDBC03
+  Functions: 12675
+  Symbols:   14612
+  CStrings:  4461
 
Symbols:
+ +[SFSpeechAssetManager supportedLanguagesForTaskHint:]
+ +[SFUtilities continuousTimeToNanoseconds:]
+ -[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:synchronous:completion:]
+ GCC_except_table1035
+ GCC_except_table1063
+ GCC_except_table1146
+ GCC_except_table1167
+ GCC_except_table1353
+ GCC_except_table1358
+ GCC_except_table1362
+ GCC_except_table1366
+ GCC_except_table1368
+ GCC_except_table1374
+ GCC_except_table1383
+ GCC_except_table1384
+ GCC_except_table1388
+ GCC_except_table1390
+ GCC_except_table865
+ GCC_except_table899
+ GCC_except_table907
+ GCC_except_table909
+ GCC_except_table911
+ GCC_except_table920
+ GCC_except_table961
+ _SFSpeechErrorCodeCannotAllocateUnsupportedLocale
+ ___102-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]_block_invoke.57
+ ___43+[SFUtilities continuousTimeToNanoseconds:]_block_invoke
+ ___54+[SFSpeechAssetManager supportedLanguagesForTaskHint:]_block_invoke
+ ___88-[SFLocalSpeechRecognitionClient installedLanguagesForAssetType:synchronous:completion:]_block_invoke.52
+ ___88-[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:synchronous:completion:]_block_invoke
+ ___88-[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:synchronous:completion:]_block_invoke.50
+ ___88-[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:synchronous:completion:]_block_invoke_2
+ ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke.56
+ ___Block_byref_object_copy_.1715
+ ___Block_byref_object_copy_.1836
+ ___Block_byref_object_copy_.2153
+ ___Block_byref_object_copy_.2413
+ ___Block_byref_object_copy_.3018
+ ___Block_byref_object_dispose_.1716
+ ___Block_byref_object_dispose_.1837
+ ___Block_byref_object_dispose_.2154
+ ___Block_byref_object_dispose_.2414
+ ___Block_byref_object_dispose_.3019
+ ___block_descriptor_40_e8_32s_e25_B32?0"NSString"8Q16^B24ls32l8
+ ___block_literal_global.1734
+ ___block_literal_global.1897
+ ___block_literal_global.2112
+ ___block_literal_global.2446
+ ___block_literal_global.2821
+ ___block_literal_global.3072
+ ___block_literal_global.437
+ ___block_literal_global.445
+ ___block_literal_global.460.2107
+ ___block_literal_global.462
+ ___block_literal_global.54
+ ___block_literal_global.59
+ _block_copy_helper.117
+ _block_copy_helper.125
+ _block_copy_helper.147
+ _block_copy_helper.156
+ _block_copy_helper.164
+ _block_copy_helper.182
+ _block_copy_helper.191
+ _block_copy_helper.219
+ _block_copy_helper.228
+ _block_copy_helper.236
+ _block_copy_helper.254
+ _block_copy_helper.263
+ _block_copy_helper.271
+ _block_copy_helper.289
+ _block_copy_helper.306
+ _block_copy_helper.324
+ _block_copy_helper.333
+ _block_copy_helper.341
+ _block_descriptor.119
+ _block_descriptor.127
+ _block_descriptor.149
+ _block_descriptor.158
+ _block_descriptor.166
+ _block_descriptor.184
+ _block_descriptor.193
+ _block_descriptor.221
+ _block_descriptor.230
+ _block_descriptor.238
+ _block_descriptor.256
+ _block_descriptor.265
+ _block_descriptor.273
+ _block_descriptor.291
+ _block_descriptor.308
+ _block_descriptor.326
+ _block_descriptor.335
+ _block_descriptor.343
+ _block_destroy_helper.118
+ _block_destroy_helper.126
+ _block_destroy_helper.148
+ _block_destroy_helper.157
+ _block_destroy_helper.165
+ _block_destroy_helper.183
+ _block_destroy_helper.192
+ _block_destroy_helper.220
+ _block_destroy_helper.229
+ _block_destroy_helper.237
+ _block_destroy_helper.255
+ _block_destroy_helper.264
+ _block_destroy_helper.272
+ _block_destroy_helper.290
+ _block_destroy_helper.307
+ _block_destroy_helper.325
+ _block_destroy_helper.334
+ _block_destroy_helper.342
+ _continuousTimeToNanoseconds:.clockToNanoseconds
+ _continuousTimeToNanoseconds:.onceToken
+ _get_type_metadata 15Synchronization5MutexVy6Speech15AnalysisContextCSgG.87
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$supportedLanguagesForAssetType:synchronous:completion:
+ _objc_msgSend$supportedLanguagesForTaskHint:
+ _objectdestroy.102Tm
+ _objectdestroy.109Tm
+ _objectdestroy.115Tm
+ _sharedInstance.onceToken.1896
+ _sharedInstance.onceToken.1941
+ _sharedInstance.sharedManager.1898
+ _sharedInstance.sharedManager.1942
- -[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:completion:]
- GCC_except_table1032
- GCC_except_table1057
- GCC_except_table1143
- GCC_except_table1164
- GCC_except_table1350
- GCC_except_table1355
- GCC_except_table1359
- GCC_except_table1363
- GCC_except_table1365
- GCC_except_table1371
- GCC_except_table1377
- GCC_except_table1378
- GCC_except_table1379
- GCC_except_table864
- GCC_except_table898
- GCC_except_table906
- GCC_except_table908
- GCC_except_table910
- GCC_except_table919
- GCC_except_table960
- _OUTLINED_FUNCTION_640
- ___102-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]_block_invoke.56
- ___76-[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:completion:]_block_invoke
- ___76-[SFLocalSpeechRecognitionClient supportedLanguagesForAssetType:completion:]_block_invoke_2
- ___88-[SFLocalSpeechRecognitionClient installedLanguagesForAssetType:synchronous:completion:]_block_invoke.51
- ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke.55
- ___Block_byref_object_copy_.1718
- ___Block_byref_object_copy_.1839
- ___Block_byref_object_copy_.2165
- ___Block_byref_object_copy_.2428
- ___Block_byref_object_copy_.3034
- ___Block_byref_object_dispose_.1719
- ___Block_byref_object_dispose_.1840
- ___Block_byref_object_dispose_.2166
- ___Block_byref_object_dispose_.2429
- ___Block_byref_object_dispose_.3035
- ___block_descriptor_40_e8_32s_e22_B24?0"NSString"8^B16ls32l8
- ___block_literal_global.1737
- ___block_literal_global.1900
- ___block_literal_global.2116
- ___block_literal_global.2460
- ___block_literal_global.2836
- ___block_literal_global.3087
- ___block_literal_global.436
- ___block_literal_global.444
- ___block_literal_global.459
- ___block_literal_global.53
- ___block_literal_global.58
- _block_copy_helper.112
- _block_copy_helper.120
- _block_copy_helper.142
- _block_copy_helper.151
- _block_copy_helper.159
- _block_copy_helper.177
- _block_copy_helper.186
- _block_copy_helper.194
- _block_copy_helper.214
- _block_copy_helper.223
- _block_copy_helper.249
- _block_copy_helper.258
- _block_copy_helper.266
- _block_copy_helper.284
- _block_copy_helper.293
- _block_copy_helper.301
- _block_copy_helper.328
- _block_copy_helper.336
- _block_descriptor.114
- _block_descriptor.122
- _block_descriptor.144
- _block_descriptor.153
- _block_descriptor.161
- _block_descriptor.179
- _block_descriptor.188
- _block_descriptor.196
- _block_descriptor.216
- _block_descriptor.225
- _block_descriptor.251
- _block_descriptor.260
- _block_descriptor.268
- _block_descriptor.286
- _block_descriptor.295
- _block_descriptor.303
- _block_descriptor.330
- _block_descriptor.338
- _block_destroy_helper.113
- _block_destroy_helper.121
- _block_destroy_helper.143
- _block_destroy_helper.152
- _block_destroy_helper.160
- _block_destroy_helper.178
- _block_destroy_helper.187
- _block_destroy_helper.195
- _block_destroy_helper.215
- _block_destroy_helper.224
- _block_destroy_helper.250
- _block_destroy_helper.259
- _block_destroy_helper.267
- _block_destroy_helper.285
- _block_destroy_helper.294
- _block_destroy_helper.302
- _block_destroy_helper.329
- _block_destroy_helper.337
- _get_type_metadata 15Synchronization5MutexVy6Speech15AnalysisContextCSgG.91
- _objc_msgSend$objectsPassingTest:
- _objectdestroy.104Tm
- _objectdestroy.110Tm
- _objectdestroy.118Tm
- _objectdestroy.97Tm
- _sharedInstance.onceToken.1899
- _sharedInstance.onceToken.1944
- _sharedInstance.sharedManager.1901
- _sharedInstance.sharedManager.1945
CStrings:
+ "+[SFSpeechAssetManager supportedLanguagesForTaskHint:]"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "Cannot use modules with unallocated locales %s. Currently allocated locales are %s. This will be an error in a future release!"
+ "Vv36@0:8Q16B24@?28"
+ "continuousTimeToNanoseconds:"
+ "d24@0:8Q16"
+ "indexesOfObjectsPassingTest:"
+ "objectsAtIndexes:"
+ "supportedLanguagesForAssetType:synchronous:completion:"
+ "supportedLanguagesForTaskHint:"
- "B24@?0@\"NSString\"8^B16"
- "Cannot use modules with unallocated locales "
- "[To be implemented in rdar://105899082] - SpeechDetector: Yielded (dummy) result"
- "objectsPassingTest:"

```
