## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`

```diff

-4024.500.30.0.0
-  __TEXT.__text: 0x540f0
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x5274
-  __TEXT.__const: 0x3a0
+4025.100.95.0.0
+  __TEXT.__text: 0x59820
+  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0x567c
+  __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__gcc_except_tab: 0x1398
-  __TEXT.__cstring: 0x5d3a
-  __TEXT.__oslogstring: 0x2b5b
+  __TEXT.__cstring: 0x5fd7
+  __TEXT.__gcc_except_tab: 0x1320
+  __TEXT.__oslogstring: 0x2c4d
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x1670
-  __TEXT.__objc_classname: 0xaa5
-  __TEXT.__objc_methname: 0xb633
-  __TEXT.__objc_methtype: 0x1c0f
-  __TEXT.__objc_stubs: 0x7840
-  __DATA_CONST.__got: 0x630
-  __DATA_CONST.__const: 0x1438
-  __DATA_CONST.__objc_classlist: 0x2f8
-  __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x90
+  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__objc_classname: 0xb1e
+  __TEXT.__objc_methname: 0xbc72
+  __TEXT.__objc_methtype: 0x1d23
+  __TEXT.__objc_stubs: 0x7b60
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0x14b0
+  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__objc_catlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d80
+  __DATA_CONST.__objc_selrefs: 0x2ee0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0xf30
-  __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x56c0
-  __AUTH_CONST.__objc_const: 0x9430
+  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0x9aa0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_ivar: 0x64c
-  __DATA.__data: 0x6d0
-  __DATA.__bss: 0x21c
-  __DATA_DIRTY.__objc_data: 0xe10
+  __AUTH.__objc_data: 0x14a0
+  __AUTH.__data: 0xc8
+  __DATA.__objc_ivar: 0x694
+  __DATA.__data: 0x730
+  __DATA.__bss: 0x234
+  __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EA6D0177-D92B-3A0C-B40E-BDFC026706CF
-  Functions: 1999
-  Symbols:   7156
-  CStrings:  4290
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 4BF453B0-7A3E-3234-AF34-25D9527A2154
+  Functions: 2080
+  Symbols:   7429
+  CStrings:  4428
 
Symbols:
+ +[MSVLyricsTranslation _translationTypeForText:]
+ +[NSEnumerator(MSVSequence) msv_concatArrays:]
+ -[MSVLyricsSongInfo setTranslations:]
+ -[MSVLyricsSongInfo setTransliterations:]
+ -[MSVLyricsSongInfo translations]
+ -[MSVLyricsSongInfo transliterations]
+ -[MSVLyricsTTMLParser setTranslations:]
+ -[MSVLyricsTTMLParser setTransliterations:]
+ -[MSVLyricsTTMLParser translations]
+ -[MSVLyricsTTMLParser transliterations]
+ -[MSVLyricsTranslation isAutomaticallyCreated]
+ -[MSVLyricsTranslation linesMap]
+ -[MSVLyricsTranslation setAutomaticallyCreated:]
+ -[MSVLyricsTranslation setLinesMap:]
+ -[MSVLyricsTranslation setType:]
+ -[MSVLyricsTranslation setTypeText:]
+ -[MSVLyricsTranslation translationForLine:]
+ -[MSVLyricsTranslation typeText]
+ -[MSVLyricsTranslation type]
+ -[MSVLyricsTransliteration .cxx_destruct]
+ -[MSVLyricsTransliteration description]
+ -[MSVLyricsTransliteration isAutomaticallyCreated]
+ -[MSVLyricsTransliteration language]
+ -[MSVLyricsTransliteration linesMap]
+ -[MSVLyricsTransliteration setAutomaticallyCreated:]
+ -[MSVLyricsTransliteration setLanguage:]
+ -[MSVLyricsTransliteration setLinesMap:]
+ -[MSVLyricsTransliteration transliterationForLine:]
+ -[MSVLyricsTransliterationText .cxx_destruct]
+ -[MSVLyricsTransliterationText description]
+ -[MSVLyricsTransliterationText init]
+ -[MSVLyricsTransliterationText lyricsLineKey]
+ -[MSVLyricsTransliterationText setLyricsLineKey:]
+ -[MSVSQLDatabase _installArraySupport]
+ -[MSVSQLDatabaseTransaction _installArraySupport]
+ -[MSVSQLStatement _bindCStringArray:length:toParameterAtIndex:]
+ -[MSVSQLStatement _bindCStringArray:length:toParameterNamed:]
+ -[MSVSQLStatement _bindDoubleArray:length:toParameterAtIndex:]
+ -[MSVSQLStatement _bindDoubleArray:length:toParameterNamed:]
+ -[MSVSQLStatement _bindInt32Array:length:toParameterAtIndex:]
+ -[MSVSQLStatement _bindInt32Array:length:toParameterNamed:]
+ -[MSVSQLStatement _bindInt64Array:length:toParameterAtIndex:]
+ -[MSVSQLStatement _bindInt64Array:length:toParameterNamed:]
+ -[MSVSQLStatement _bindNoCopyDataValue:toParameterAtIndex:]
+ -[MSVSQLStatement _bindNoCopyDataValue:toParameterNamed:]
+ -[MSVSQLStatement _bindNoCopyStringValue:toParameterAtIndex:]
+ -[MSVSQLStatement _bindNoCopyStringValue:toParameterNamed:]
+ -[MSVSQLStatement _bindVariantArray:length:toParameterAtIndex:]
+ -[MSVSQLStatement _bindVariantArray:length:toParameterNamed:]
+ -[MSVSQLStatement bindJSONConvertible:toParameterAtIndex:error:]
+ -[MSVSQLStatement bindJSONConvertible:toParameterNamed:error:]
+ -[MSVSectionedCollection allElementsEnumerator]
+ -[NSArray(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSArray(MSVJSONConvertible) msv_jsonValue]
+ -[NSData(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSData(MSVJSONConvertible) msv_jsonValue]
+ -[NSDate(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSDate(MSVJSONConvertible) msv_jsonValue]
+ -[NSDictionary(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSDictionary(MSVJSONConvertible) msv_jsonValue]
+ -[NSEnumerator(MSVSequence) msv_lazyFilter:]
+ -[NSError(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSError(MSVJSONConvertible) msv_jsonValue]
+ -[NSError(MSVJSONConvertible) msv_userInfoJSONValue]
+ -[NSMutableArray(MSVAdditions) msv_removeLastObject]
+ -[NSMutableArray(MSVAdditions) msv_removeWhere:]
+ -[NSURL(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSURL(MSVJSONConvertible) msv_jsonValue]
+ -[NSUUID(MSVJSONConvertible) msv_initWithJSONValue:]
+ -[NSUUID(MSVJSONConvertible) msv_jsonValue]
+ -[_MSVConcatArrayEnumerator .cxx_destruct]
+ -[_MSVConcatArrayEnumerator nextObject]
+ -[_MSVLazyFilterEnumerator .cxx_destruct]
+ -[_MSVLazyFilterEnumerator nextObject]
+ -[_MSVSQLConnection _installArraySupport]
+ GCC_except_table100
+ GCC_except_table111
+ GCC_except_table1197
+ GCC_except_table1201
+ GCC_except_table1203
+ GCC_except_table1217
+ GCC_except_table1223
+ GCC_except_table125
+ GCC_except_table1283
+ GCC_except_table1486
+ GCC_except_table1490
+ GCC_except_table1492
+ GCC_except_table1494
+ GCC_except_table1496
+ GCC_except_table1498
+ GCC_except_table1500
+ GCC_except_table1502
+ GCC_except_table1504
+ GCC_except_table1506
+ GCC_except_table1508
+ GCC_except_table1512
+ GCC_except_table1589
+ GCC_except_table1598
+ GCC_except_table1602
+ GCC_except_table1606
+ GCC_except_table1647
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table1832
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table1989
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table2026
+ GCC_except_table2042
+ GCC_except_table2043
+ GCC_except_table2044
+ GCC_except_table207
+ GCC_except_table316
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table356
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table420
+ GCC_except_table422
+ GCC_except_table423
+ GCC_except_table424
+ GCC_except_table429
+ GCC_except_table441
+ GCC_except_table464
+ GCC_except_table472
+ GCC_except_table51
+ GCC_except_table518
+ GCC_except_table538
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table607
+ GCC_except_table609
+ GCC_except_table61
+ GCC_except_table643
+ GCC_except_table644
+ GCC_except_table648
+ GCC_except_table657
+ GCC_except_table66
+ GCC_except_table688
+ GCC_except_table69
+ GCC_except_table713
+ GCC_except_table78
+ GCC_except_table990
+ _MSVFastHexStringFromBytes.hexCharacters.4808
+ _MSVNanoIDCreateEightChar
+ _MSVNanoIDCreateFourChar
+ _MSVWithCStringArray
+ _NSURLErrorFailingURLErrorKey
+ _OBJC_CLASS_$_MSVLyricsTransliteration
+ _OBJC_CLASS_$_MSVLyricsTransliterationText
+ _OBJC_CLASS_$__MSVConcatArrayEnumerator
+ _OBJC_CLASS_$__MSVLazyFilterEnumerator
+ _OBJC_IVAR_$_MSVBlockGuard._lock
+ _OBJC_IVAR_$_MSVLyricsSongInfo._availableTranslations
+ _OBJC_IVAR_$_MSVLyricsSongInfo._translations
+ _OBJC_IVAR_$_MSVLyricsSongInfo._transliterations
+ _OBJC_IVAR_$_MSVLyricsTTMLParser._translations
+ _OBJC_IVAR_$_MSVLyricsTTMLParser._transliterations
+ _OBJC_IVAR_$_MSVLyricsTranslation._automaticallyCreated
+ _OBJC_IVAR_$_MSVLyricsTranslation._linesMap
+ _OBJC_IVAR_$_MSVLyricsTranslation._type
+ _OBJC_IVAR_$_MSVLyricsTranslation._typeText
+ _OBJC_IVAR_$_MSVLyricsTransliteration._automaticallyCreated
+ _OBJC_IVAR_$_MSVLyricsTransliteration._language
+ _OBJC_IVAR_$_MSVLyricsTransliteration._linesMap
+ _OBJC_IVAR_$_MSVLyricsTransliterationText._lyricsLineKey
+ _OBJC_IVAR_$__MSVConcatArrayEnumerator._arrays
+ _OBJC_IVAR_$__MSVConcatArrayEnumerator._index
+ _OBJC_IVAR_$__MSVConcatArrayEnumerator._innerIndex
+ _OBJC_IVAR_$__MSVLazyFilterEnumerator._block
+ _OBJC_IVAR_$__MSVLazyFilterEnumerator._enumerator
+ _OBJC_IVAR_$__MSVSQLConnection._arraySupportInstalled
+ _OBJC_METACLASS_$_MSVLyricsTransliteration
+ _OBJC_METACLASS_$_MSVLyricsTransliterationText
+ _OBJC_METACLASS_$__MSVConcatArrayEnumerator
+ _OBJC_METACLASS_$__MSVLazyFilterEnumerator
+ __CATEGORY_NSError_$_MediaServices
+ __CATEGORY_NSString_$_MSVSymbols
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSEnumerator_$_MSVSequence
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_MSVJSONConvertible
+ __OBJC_$_CATEGORY_NSArray_$_MSVJSONConvertible
+ __OBJC_$_CATEGORY_NSData_$_MSVJSONConvertible
+ __OBJC_$_CATEGORY_NSDate_$_MSVJSONConvertible
+ __OBJC_$_CATEGORY_NSDictionary_$_MSVJSONConvertible
+ __OBJC_$_CATEGORY_NSURL_$_MSVJSONConvertible
+ __OBJC_$_CLASS_METHODS_MSVLyricsTranslation
+ __OBJC_$_CLASS_METHODS_NSDictionary(MSVJSONConvertible|MSVAdditions|MSVSequence)
+ __OBJC_$_CLASS_METHODS_NSError(MediaServices|MSVJSONConvertible|MSVErrorAdditions|MSVDependencyError)
+ __OBJC_$_CLASS_METHODS_NSURL(MSVJSONConvertible|MSVAdditions)
+ __OBJC_$_INSTANCE_METHODS_MSVLyricsTransliteration
+ __OBJC_$_INSTANCE_METHODS_MSVLyricsTransliterationText
+ __OBJC_$_INSTANCE_METHODS_NSArray(MSVJSONConvertible|MSVAdditions|MSVSequence)
+ __OBJC_$_INSTANCE_METHODS_NSDate(MSVJSONConvertible|MSVAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(MSVJSONConvertible|MSVAdditions|MSVSequence)
+ __OBJC_$_INSTANCE_METHODS_NSError(MediaServices|MSVJSONConvertible|MSVErrorAdditions|MSVDependencyError)
+ __OBJC_$_INSTANCE_METHODS_NSString(MSVSymbols|MSVAdditions|MSVLyricsTTMLParser)
+ __OBJC_$_INSTANCE_METHODS_NSURL(MSVJSONConvertible|MSVAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSUUID(MSVBase64|MSVJSONConvertible)
+ __OBJC_$_INSTANCE_METHODS__MSVConcatArrayEnumerator
+ __OBJC_$_INSTANCE_METHODS__MSVLazyFilterEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_MSVLyricsTransliteration
+ __OBJC_$_INSTANCE_VARIABLES_MSVLyricsTransliterationText
+ __OBJC_$_INSTANCE_VARIABLES__MSVConcatArrayEnumerator
+ __OBJC_$_INSTANCE_VARIABLES__MSVLazyFilterEnumerator
+ __OBJC_$_PROP_LIST_MSVLyricsTransliteration
+ __OBJC_$_PROP_LIST_MSVLyricsTransliterationText
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MSVJSONConvertible
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MSVJSONConvertible
+ __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_MSVJSONConvertible
+ __OBJC_CATEGORY_PROTOCOLS_$_NSData_$_MSVJSONConvertible
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDate_$_MSVJSONConvertible
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_MSVJSONConvertible
+ __OBJC_CATEGORY_PROTOCOLS_$_NSURL_$_MSVJSONConvertible
+ __OBJC_CLASS_PROTOCOLS_$_NSError(MediaServices|MSVJSONConvertible|MSVErrorAdditions|MSVDependencyError)
+ __OBJC_CLASS_PROTOCOLS_$_NSUUID(MSVBase64|MSVJSONConvertible)
+ __OBJC_CLASS_RO_$_MSVLyricsTransliteration
+ __OBJC_CLASS_RO_$_MSVLyricsTransliterationText
+ __OBJC_CLASS_RO_$__MSVConcatArrayEnumerator
+ __OBJC_CLASS_RO_$__MSVLazyFilterEnumerator
+ __OBJC_LABEL_PROTOCOL_$_MSVJSONConvertible
+ __OBJC_METACLASS_RO_$_MSVLyricsTransliteration
+ __OBJC_METACLASS_RO_$_MSVLyricsTransliterationText
+ __OBJC_METACLASS_RO_$__MSVConcatArrayEnumerator
+ __OBJC_METACLASS_RO_$__MSVLazyFilterEnumerator
+ __OBJC_PROTOCOL_$_MSVJSONConvertible
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI7ITColorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEbT1_S7_T0_
+ __ZNSt3__16vectorI14sortColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI22sortQuantizeColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI22sortQuantizeColorEntryNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI7ITColorNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_Li0EEEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_Li0EEEvT1_S7_S7_S7_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___44-[NSArray(MSVJSONConvertible) msv_jsonValue]_block_invoke
+ ___49-[NSDictionary(MSVJSONConvertible) msv_jsonValue]_block_invoke
+ ___52-[NSError(MSVJSONConvertible) msv_userInfoJSONValue]_block_invoke
+ ___52-[NSError(MSVJSONConvertible) msv_userInfoJSONValue]_block_invoke_2
+ ___53-[NSArray(MSVJSONConvertible) msv_initWithJSONValue:]_block_invoke
+ ___53-[NSError(MSVJSONConvertible) msv_initWithJSONValue:]_block_invoke
+ ___53-[NSError(MSVJSONConvertible) msv_initWithJSONValue:]_block_invoke_2
+ ___58-[NSDictionary(MSVJSONConvertible) msv_initWithJSONValue:]_block_invoke
+ ___Block_byref_object_copy_.1311
+ ___Block_byref_object_copy_.1667
+ ___Block_byref_object_copy_.1933
+ ___Block_byref_object_copy_.2111
+ ___Block_byref_object_copy_.3341
+ ___Block_byref_object_copy_.3438
+ ___Block_byref_object_copy_.3509
+ ___Block_byref_object_copy_.4510
+ ___Block_byref_object_copy_.4720
+ ___Block_byref_object_copy_.4802
+ ___Block_byref_object_copy_.5180
+ ___Block_byref_object_copy_.6061
+ ___Block_byref_object_dispose_.1312
+ ___Block_byref_object_dispose_.1668
+ ___Block_byref_object_dispose_.1934
+ ___Block_byref_object_dispose_.2112
+ ___Block_byref_object_dispose_.3342
+ ___Block_byref_object_dispose_.3439
+ ___Block_byref_object_dispose_.3510
+ ___Block_byref_object_dispose_.4511
+ ___Block_byref_object_dispose_.4721
+ ___Block_byref_object_dispose_.4803
+ ___Block_byref_object_dispose_.5181
+ ___Block_byref_object_dispose_.6062
+ ___MSVJSONDateFormatter
+ ___MSVJSONDateFormatter.__iso8601Formatter
+ ___MSVJSONDateFormatter.onceToken
+ _____MSVJSONDateFormatter_block_invoke
+ ___assertion.5819
+ ___assertionCount.5814
+ ___assertionInvalidationNonce.5818
+ ___assertionLock.5813
+ ___block_descriptor_48_e8_32s_e11_24?0816ls32l8
+ ___block_descriptor_48_e8_32s_e24_16?0"<MSVJSONValue>"8ls32l8
+ ___block_descriptor_48_e8_32s_e8_16?08ls32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.122.4640
+ ___block_literal_global.1506
+ ___block_literal_global.1602
+ ___block_literal_global.1716
+ ___block_literal_global.2408
+ ___block_literal_global.2910
+ ___block_literal_global.3286
+ ___block_literal_global.3384
+ ___block_literal_global.3625
+ ___block_literal_global.37
+ ___block_literal_global.391
+ ___block_literal_global.3936
+ ___block_literal_global.403
+ ___block_literal_global.42
+ ___block_literal_global.44
+ ___block_literal_global.4639
+ ___block_literal_global.4658
+ ___block_literal_global.48
+ ___block_literal_global.5087
+ ___block_literal_global.5183
+ ___block_literal_global.5427
+ ___block_literal_global.5486
+ ___block_literal_global.55.5854
+ ___block_literal_global.5859
+ ___block_literal_global.5944
+ ___block_literal_global.624
+ ___block_literal_global.891
+ ___block_literal_global.977
+ ___swift_reflection_version
+ __dyld_get_prog_image_header
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_MediaServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_MediaServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MediaServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MediaServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MediaServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_MediaServices
+ _azType
+ _carrayBestIndex
+ _carrayBindDel
+ _carrayClose
+ _carrayColumn
+ _carrayConnect
+ _carrayDisconnect
+ _carrayEof
+ _carrayFilter
+ _carrayNext
+ _carrayOpen
+ _carrayRowid
+ _dispatch_block_create_with_qos_class
+ _msv_carrayModule
+ _msv_dispatch_async_on_queue_with_qos
+ _msv_sql_carray_bind
+ _objc_msgSend$_bindCStringArray:length:toParameterAtIndex:
+ _objc_msgSend$_bindDoubleArray:length:toParameterAtIndex:
+ _objc_msgSend$_bindInt32Array:length:toParameterAtIndex:
+ _objc_msgSend$_bindInt64Array:length:toParameterAtIndex:
+ _objc_msgSend$_bindNoCopyDataValue:toParameterAtIndex:
+ _objc_msgSend$_bindNoCopyStringValue:toParameterAtIndex:
+ _objc_msgSend$_bindVariantArray:length:toParameterAtIndex:
+ _objc_msgSend$_installArraySupport
+ _objc_msgSend$_translationTypeForText:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$bindJSONValue:toParameterNamed:error:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$linesMap
+ _objc_msgSend$msv_concatArrays:
+ _objc_msgSend$msv_initWithJSONValue:
+ _objc_msgSend$msv_jsonValue
+ _objc_msgSend$msv_mapValues:
+ _objc_msgSend$msv_userInfoJSONValue
+ _objc_msgSend$nextObject
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$setAutomaticallyCreated:
+ _objc_msgSend$setLinesMap:
+ _objc_msgSend$setTranslations:
+ _objc_msgSend$setTransliterations:
+ _objc_msgSend$setTypeText:
+ _objc_msgSend$translations
+ _objc_msgSend$transliterations
+ _sec_protocol_options_set_pqtls_mode
+ _sqlite3_create_module
+ _sqlite3_declare_vtab
+ _sqlite3_free
+ _sqlite3_malloc
+ _sqlite3_malloc64
+ _sqlite3_mprintf
+ _sqlite3_result_blob
+ _sqlite3_stricmp
+ _swift_bridgeObjectRelease
- -[MSVLyricsTTMLParser setTranslationsMap:]
- -[MSVLyricsTTMLParser translationsMap]
- GCC_except_table1001
- GCC_except_table1008
- GCC_except_table1010
- GCC_except_table1039
- GCC_except_table1057
- GCC_except_table1061
- GCC_except_table1065
- GCC_except_table1169
- GCC_except_table1209
- GCC_except_table1215
- GCC_except_table1416
- GCC_except_table1523
- GCC_except_table1527
- GCC_except_table1529
- GCC_except_table153
- GCC_except_table1531
- GCC_except_table1533
- GCC_except_table1535
- GCC_except_table1537
- GCC_except_table1539
- GCC_except_table1541
- GCC_except_table1545
- GCC_except_table1614
- GCC_except_table1615
- GCC_except_table1617
- GCC_except_table1619
- GCC_except_table1620
- GCC_except_table1622
- GCC_except_table1623
- GCC_except_table1624
- GCC_except_table1628
- GCC_except_table1631
- GCC_except_table1635
- GCC_except_table1637
- GCC_except_table1639
- GCC_except_table1640
- GCC_except_table1645
- GCC_except_table1738
- GCC_except_table1814
- GCC_except_table1818
- GCC_except_table1820
- GCC_except_table1855
- GCC_except_table1891
- GCC_except_table1896
- GCC_except_table1912
- GCC_except_table1913
- GCC_except_table1914
- GCC_except_table255
- GCC_except_table278
- GCC_except_table284
- GCC_except_table503
- GCC_except_table508
- GCC_except_table533
- GCC_except_table534
- GCC_except_table535
- GCC_except_table55
- GCC_except_table568
- GCC_except_table57
- GCC_except_table59
- GCC_except_table630
- GCC_except_table632
- GCC_except_table637
- GCC_except_table639
- GCC_except_table64
- GCC_except_table641
- GCC_except_table646
- GCC_except_table658
- GCC_except_table665
- GCC_except_table67
- GCC_except_table695
- GCC_except_table70
- GCC_except_table703
- GCC_except_table790
- GCC_except_table810
- GCC_except_table984
- GCC_except_table987
- GCC_except_table988
- GCC_except_table992
- _CC_MD5
- _CC_MD5_Init
- _CC_SHA1_Init
- _CC_SHA256
- _CC_SHA256_Init
- _MSVCryptoDigestForContentsOfFile
- _MSVCryptoDigestForContentsOfInputStream
- _MSVCryptoDigestForData
- _MSVCryptoUtilitiesDigestDataFromHexString
- _MSVCryptoUtilitiesHexStringFromDigest
- _MSVFastHexStringFromBytes.hexCharacters.3703
- _OBJC_IVAR_$_MSVBlockGuard._accessQueue
- _OBJC_IVAR_$_MSVLyricsTTMLParser._translationsMap
- __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_MSVAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_NSURL_$_MSVAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDate_$_MSVAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_MSVErrorAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURL_$_MSVAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_MSVBase64
- __OBJC_$_CATEGORY_NSArray_$_MSVAdditions
- __OBJC_$_CATEGORY_NSDate_$_MSVAdditions
- __OBJC_$_CATEGORY_NSDictionary_$_MSVAdditions
- __OBJC_$_CATEGORY_NSError_$_MSVErrorAdditions
- __OBJC_$_CATEGORY_NSString_$_MSVLyricsTTMLParser
- __OBJC_$_CATEGORY_NSURL_$_MSVAdditions
- __OBJC_$_CLASS_METHODS_NSError(MSVErrorAdditions|MSVDependencyError)
- __OBJC_$_INSTANCE_METHODS_NSArray(MSVAdditions|MSVSequence)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(MSVAdditions|MSVSequence)
- __OBJC_$_INSTANCE_METHODS_NSString(MSVLyricsTTMLParser|MSVAdditions)
- __OBJC_$_PROP_LIST_NSArray_$_MSVAdditions
- __OBJC_$_PROP_LIST_NSDate_$_MSVAdditions
- __OBJC_$_PROP_LIST_NSDictionary_$_MSVAdditions
- __OBJC_$_PROP_LIST_NSError_$_MSVErrorAdditions
- __OBJC_$_PROP_LIST_NSString_$_MSVLyricsTTMLParser
- __OBJC_$_PROP_LIST_NSURL_$_MSVAdditions
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI14sortColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI22sortQuantizeColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI7ITColorNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI22sortQuantizeColorEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI7ITColorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEbT1_S7_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEjT1_S7_S7_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEvT1_S7_S7_S7_S7_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEvT1_S7_S7_S7_S7_T0_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___23-[MSVBlockGuard disarm]_block_invoke
- ___38-[MSVBlockGuard _interruptWithReason:]_block_invoke
- ___Block_byref_object_copy_.1741
- ___Block_byref_object_copy_.1825
- ___Block_byref_object_copy_.2267
- ___Block_byref_object_copy_.2810
- ___Block_byref_object_copy_.3126
- ___Block_byref_object_copy_.3649
- ___Block_byref_object_copy_.3693
- ___Block_byref_object_copy_.3949
- ___Block_byref_object_copy_.4083
- ___Block_byref_object_copy_.4226
- ___Block_byref_object_copy_.4502
- ___Block_byref_object_copy_.5244
- ___Block_byref_object_copy_.5639
- ___Block_byref_object_copy_.6001
- ___Block_byref_object_dispose_.1742
- ___Block_byref_object_dispose_.1826
- ___Block_byref_object_dispose_.2268
- ___Block_byref_object_dispose_.2811
- ___Block_byref_object_dispose_.3127
- ___Block_byref_object_dispose_.3650
- ___Block_byref_object_dispose_.3694
- ___Block_byref_object_dispose_.3950
- ___Block_byref_object_dispose_.4084
- ___Block_byref_object_dispose_.4227
- ___Block_byref_object_dispose_.4503
- ___Block_byref_object_dispose_.5245
- ___Block_byref_object_dispose_.5640
- ___Block_byref_object_dispose_.6002
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_2
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_3
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_4
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_5
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_6
- ___MSVCryptoDigestForContentsOfInputStream_block_invoke_7
- ___assertion.5517
- ___assertionCount.5512
- ___assertionInvalidationNonce.5516
- ___assertionLock.5511
- ___block_descriptor_40_e16_v16?0"NSData"8l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_64_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_literal_global.1166
- ___block_literal_global.122.2342
- ___block_literal_global.1275
- ___block_literal_global.1593
- ___block_literal_global.1938
- ___block_literal_global.2033
- ___block_literal_global.2156
- ___block_literal_global.2201
- ___block_literal_global.2319
- ___block_literal_global.2672
- ___block_literal_global.3038
- ___block_literal_global.3070
- ___block_literal_global.3209
- ___block_literal_global.392
- ___block_literal_global.3940
- ___block_literal_global.4087
- ___block_literal_global.4462
- ___block_literal_global.5192
- ___block_literal_global.5556
- ___block_literal_global.5646
- ___block_literal_global.591
- ___block_literal_global.5923
- ___block_literal_global.953
- _objc_msgSend$availableTranslations
- _objc_msgSend$getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
- _strtol
CStrings:
+ "0"
+ "<translation> end element expects translations to be set by start of <translations> element"
+ "<transliteration> element must specify a language with <xml:lang> attribute"
+ "<transliteration> end element expects transliterations to be set by start of <transliterations> element"
+ "@\"<MSVJSONValue>\"16@0:8"
+ "@\"NSEnumerator\""
+ "@16@?0@\"<MSVJSONValue>\"8"
+ "@24@0:8@\"<MSVJSONValue>\"16"
+ "At end of <text> element, an MSVLyricsTransliterationText object should be top of stack"
+ "CREATE TABLE x(value,idx,tag,pointer hidden,count hidden,ctype hidden)"
+ "Found non-JSON value inside JSON array: %@"
+ "Found non-JSON value inside JSON dictionary: %@"
+ "Found non-JSON value while converting to JSON array: %@"
+ "Found non-JSON value while converting to JSON dictionary: %@"
+ "Found non-string key in dictionary while converting to JSON: %@"
+ "Foundation+Sequence.m"
+ "Invalid transliteration text element at line %ld: %@"
+ "MSVJSON.m"
+ "MSVJSONConvertible"
+ "MSVLyricsTransliteration"
+ "MSVLyricsTransliterationText"
+ "MSVSymbols"
+ "T@\"NSArray\",&,N,V_translations"
+ "T@\"NSArray\",&,N,V_transliterations"
+ "T@\"NSArray\",R,N,V_availableTranslations"
+ "T@\"NSMutableArray\",&,N,V_translations"
+ "T@\"NSMutableArray\",&,N,V_transliterations"
+ "T@\"NSMutableDictionary\",&,N,V_linesMap"
+ "T@\"NSString\",C,N,V_typeText"
+ "T@\"NSString\",N,R"
+ "TB,N,GisAutomaticallyCreated,V_automaticallyCreated"
+ "Transliterated Line"
+ "Type: %@, duration: %g, %ld sections, %ld lines, songwriters: %@, translations: %@, transliterations: %@"
+ "Warning: <transliteration> element must be inside <transliterations>"
+ "Warning: <transliterations> element should be inside <iTunesMetadata>"
+ "_MSVConcatArrayEnumerator"
+ "_MSVLazyFilterEnumerator"
+ "_arraySupportInstalled"
+ "_arrays"
+ "_automaticallyCreated"
+ "_availableTranslations"
+ "_bindCStringArray:length:toParameterAtIndex:"
+ "_bindCStringArray:length:toParameterNamed:"
+ "_bindDoubleArray:length:toParameterAtIndex:"
+ "_bindDoubleArray:length:toParameterNamed:"
+ "_bindInt32Array:length:toParameterAtIndex:"
+ "_bindInt32Array:length:toParameterNamed:"
+ "_bindInt64Array:length:toParameterAtIndex:"
+ "_bindInt64Array:length:toParameterNamed:"
+ "_bindNoCopyDataValue:toParameterAtIndex:"
+ "_bindNoCopyDataValue:toParameterNamed:"
+ "_bindNoCopyStringValue:toParameterAtIndex:"
+ "_bindNoCopyStringValue:toParameterNamed:"
+ "_bindVariantArray:length:toParameterAtIndex:"
+ "_bindVariantArray:length:toParameterNamed:"
+ "_enumerator"
+ "_index"
+ "_innerIndex"
+ "_installArraySupport"
+ "_linesMap"
+ "_translationTypeForText:"
+ "_translations"
+ "_transliterations"
+ "_typeText"
+ "allElementsEnumerator"
+ "arrayByAddingObjectsFromArray:"
+ "arrays"
+ "automaticallyCreated"
+ "b1"
+ "bindJSONConvertible:toParameterAtIndex:error:"
+ "bindJSONConvertible:toParameterNamed:error:"
+ "carray"
+ "carray-bind"
+ "char*"
+ "initWithArrays:"
+ "initWithDomain:code:userInfo:"
+ "int32"
+ "int64"
+ "isAutomaticallyCreated"
+ "linesMap"
+ "msv_carray"
+ "msv_concatArrays:"
+ "msv_initWithJSONValue:"
+ "msv_jsonValue"
+ "msv_lazyFilter:"
+ "msv_removeLastObject"
+ "msv_removeWhere:"
+ "msv_symbol"
+ "msv_treeDescription"
+ "msv_userInfoJSONValue"
+ "objectsAtIndexes:"
+ "replace"
+ "setAutomaticallyCreated:"
+ "setLinesMap:"
+ "setTranslations:"
+ "setTransliterations:"
+ "setTypeText:"
+ "struct iovec"
+ "subtitle"
+ "translationForLine:"
+ "transliteration"
+ "transliterationForLine:"
+ "transliterations"
+ "treeDescription"
+ "true"
+ "typeText"
+ "unknown datatype: %Q"
+ "v40@0:8^d16q24@32"
+ "v40@0:8^d16q24q32"
+ "v40@0:8^i16q24@32"
+ "v40@0:8^i16q24q32"
+ "v40@0:8^q16q24@32"
+ "v40@0:8^q16q24q32"
+ "v40@0:8^{?=C(?=qd@)q}16q24@32"
+ "v40@0:8^{?=C(?=qd@)q}16q24q32"
+ "v40@0:8r^*16q24@32"
+ "v40@0:8r^*16q24q32"
+ "variant"
- "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
- "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
- "8"
- "<translation> end element expects translationsMap to be set by start of <translations> element"
- "CryptoUtil"
- "Invalid crypto format: %d"
- "T@\"NSMutableDictionary\",&,N,V_translationsMap"
- "Type: %@, duration: %g, %ld sections, %ld lines, songwriters: %@, translations: %@"
- "_mh_execute_header"
- "com.apple.MediaServices/MSVBlockGuard/access"
- "getBytes:maxLength:usedLength:encoding:options:range:remainingRange:"

```
