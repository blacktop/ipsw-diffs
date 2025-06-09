## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64570.58.1.0.0
-  __TEXT.__text: 0xaaecc
-  __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x6408
+64572.120.2.0.0
+  __TEXT.__text: 0xac8e8
+  __TEXT.__auth_stubs: 0x21b0
+  __TEXT.__objc_methlist: 0x64f8
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xfa20
-  __TEXT.__gcc_except_tab: 0x4f28
-  __TEXT.__oslogstring: 0x1614
+  __TEXT.__cstring: 0xfcb5
+  __TEXT.__gcc_except_tab: 0x4ea4
+  __TEXT.__oslogstring: 0x1642
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x27f0
-  __TEXT.__objc_classname: 0x81d
-  __TEXT.__objc_methname: 0xf160
-  __TEXT.__objc_methtype: 0x85e5
-  __TEXT.__objc_stubs: 0x9720
-  __DATA_CONST.__got: 0x430
+  __TEXT.__unwind_info: 0x2820
+  __TEXT.__objc_classname: 0x83a
+  __TEXT.__objc_methname: 0xf329
+  __TEXT.__objc_methtype: 0x5dd8
+  __TEXT.__objc_stubs: 0x9900
+  __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0x3638
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3478
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x3508
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
-  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__auth_got: 0x10f0
   __AUTH_CONST.__const: 0xb88
-  __AUTH_CONST.__cfstring: 0xd3e0
-  __AUTH_CONST.__objc_const: 0xb9e0
+  __AUTH_CONST.__cfstring: 0xd7c0
+  __AUTH_CONST.__objc_const: 0xbb80
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x3c0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc58
+  __DATA.__objc_ivar: 0xc6c
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x550
-  __DATA.__common: 0xf1
-  __DATA_DIRTY.__objc_data: 0x1860
-  __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA.__bss: 0x530
+  __DATA.__common: 0xf9
+  __DATA_DIRTY.__objc_data: 0x17c0
+  __DATA_DIRTY.__crash_info: 0x148
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 93E58491-EDA4-394D-B11E-1AEC731C7CA1
-  Functions: 2982
-  Symbols:   10300
-  CStrings:  7597
+  UUID: E54A98F2-B84C-3485-9BE4-3EA79FF8E574
+  Functions: 3006
+  Symbols:   10355
+  CStrings:  7692
 
Symbols:
+ -[VMUBacktrace .cxx_destruct]
+ -[VMUBacktrace asyncRecursionInfoArray]
+ -[VMUBacktrace initWithSamplingContext:thread:]
+ -[VMUBacktrace originalLength]
+ -[VMUBacktrace recursionInfoArray]
+ -[VMUBacktraceRecursionInfo coldestElided]
+ -[VMUBacktraceRecursionInfo depth]
+ -[VMUBacktraceRecursionInfo description]
+ -[VMUBacktraceRecursionInfo dictionary]
+ -[VMUBacktraceRecursionInfo hottestElided]
+ -[VMUBacktraceRecursionInfo initWithDictionary:]
+ -[VMUBacktraceRecursionInfo keyPC]
+ -[VMUBacktraceRecursionInfo setColdestElided:]
+ -[VMUBacktraceRecursionInfo setDepth:]
+ -[VMUBacktraceRecursionInfo setHottestElided:]
+ -[VMUBacktraceRecursionInfo setKeyPC:]
+ -[VMUClassInfo isOSObject]
+ -[VMUObjectIdentifier labelForNSCFData:length:remoteAddress:]
+ -[VMUObjectIdentifier setNeedToValidateRemoteMirrorReadAddressRange:]
+ -[VMUSampler formatFrame:showBinaryImage:]
+ -[VMUSampler printRecursiveBacktrace:threadIndex:]
+ -[VMUSampler recordSampleTo:timestamp:thread:clearMemoryCache:]
+ -[VMUSampler recordSampleTo:timestamp:thread:clearMemoryCache:].cold.1
+ -[VMUSampler recordSampleTo:timestamp:thread:clearMemoryCache:].cold.2
+ -[VMUSampler recordSampleTo:timestamp:thread:clearMemoryCache:].cold.3
+ -[VMUSampler recordSampleTo:timestamp:thread:clearMemoryCache:].cold.4
+ -[VMUSampler setUpForFormatFrame:]
+ -[VMUSampler wasAllRecursionPreviouslyPrinted:]
+ -[VMUTaskMemoryScanner regionIdentifier]
+ -[VMUVMRegion fixNonEmptyMallocRegionType]
+ GCC_except_table136
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table185
+ GCC_except_table31
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table77
+ GCC_except_table86
+ _CSSymbolIsDeduplicated
+ _CSTaskHasNotStarted
+ _NSFreeMapTable
+ _OBJC_CLASS_$_VMUBacktraceRecursionInfo
+ _OBJC_IVAR_$_VMUBacktraceRecursionInfo._coldestElided
+ _OBJC_IVAR_$_VMUBacktraceRecursionInfo._depth
+ _OBJC_IVAR_$_VMUBacktraceRecursionInfo._hottestElided
+ _OBJC_IVAR_$_VMUBacktraceRecursionInfo._keyPC
+ _OBJC_IVAR_$_VMUSampler._previousRecursionKeyPCs
+ _OBJC_METACLASS_$_VMUBacktraceRecursionInfo
+ __OBJC_$_INSTANCE_METHODS_VMUBacktraceRecursionInfo
+ __OBJC_$_INSTANCE_VARIABLES_VMUBacktraceRecursionInfo
+ __OBJC_$_PROP_LIST_VMUBacktraceRecursionInfo
+ __OBJC_CLASS_RO_$_VMUBacktraceRecursionInfo
+ __OBJC_METACLASS_RO_$_VMUBacktraceRecursionInfo
+ __ZN37small_objc_portable_task_crash_info_tD2Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne200100EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS6_IyEEEEEEPvEENS_22__hash_node_destructorINS6_ISI_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__111__sift_downB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS5_IyEEEEEELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS5_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ne200100EmRS5_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__116__insertion_sortB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__119__partial_sort_implB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne200100EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB8ne200100EPS7_
+ __ZNSt3__126__insertion_sort_unguardedB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEbT1_S9_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB8ne200100INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEET0_S9_S9_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ne200100INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI25_CSBinaryImageInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI30_CSBinaryRelocationInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_Li0EEEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__19allocatorI10_CSTypeRefE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI14RangeAndStringE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI25_CSBinaryImageInformationE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI30_CSBinaryRelocationInformationE17allocate_at_leastB8ne200100Em
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___Block_byref_object_copy_.17
+ ___Block_byref_object_dispose_.18
+ ___block_descriptor_73_ea8_32s40s48s56bs64bs_e14_v24?0Q8I16I20ls32l8s56l8s64l8s40l8s48l8
+ ___block_literal_global.114
+ ___block_literal_global.227
+ ___block_literal_global.454
+ ___block_literal_global.467
+ ___block_literal_global.498
+ ___block_literal_global.520
+ ___block_literal_global.601
+ ___block_literal_global.818
+ ___shouldCopyMemoryForRemoteMirror_block_invoke
+ __free_bytes_function
+ __free_bytes_function.cold.1
+ _createRemoteAddressToLocalAddressAndSizeMap
+ _createRemoteStringToLengthMap
+ _getMemoryForRemoteMirror
+ _getMemoryForRemoteMirror.cold.1
+ _getSanitizedPathForSymbolOwner
+ _objc_msgSend$coldestElided
+ _objc_msgSend$depth
+ _objc_msgSend$descriptionForRange:
+ _objc_msgSend$fixNonEmptyMallocRegionType
+ _objc_msgSend$formatFrame:showBinaryImage:
+ _objc_msgSend$hottestElided
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
+ _objc_msgSend$initWithSamplingContext:thread:
+ _objc_msgSend$isOSObject
+ _objc_msgSend$keyPC
+ _objc_msgSend$originalLength
+ _objc_msgSend$printRecursiveBacktrace:threadIndex:
+ _objc_msgSend$recordSampleTo:timestamp:thread:clearMemoryCache:
+ _objc_msgSend$recursionInfoArray
+ _objc_msgSend$regionIdentifier
+ _objc_msgSend$setUpForFormatFrame:
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$wasAllRecursionPreviouslyPrinted:
+ _puts
+ _sampling_context_get_options
+ _shouldCopyMemoryForRemoteMirror.onceToken
+ _shouldCopyMemoryForRemoteMirror.result
- -[VMUBacktrace initWithSamplingContext:thread:recordFramePointers:]
- -[VMUObjectIdentifier flushRemoteMirrorMemoryCacheEntryForAddress:]
- -[VMUObjectIdentifier labelForNSConcreteMutableData:length:remoteAddress:]
- -[VMUObjectIdentifier labelForNSData:length:remoteAddress:]
- -[VMUSampler recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:]
- -[VMUSampler recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:].cold.1
- -[VMUSampler recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:].cold.2
- -[VMUSampler recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:].cold.3
- -[VMUSampler recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:].cold.4
- -[VMUSampler sampleAllThreadsOnceWithFramePointers:]
- GCC_except_table112
- GCC_except_table126
- GCC_except_table135
- GCC_except_table144
- GCC_except_table147
- GCC_except_table152
- GCC_except_table155
- GCC_except_table159
- GCC_except_table161
- GCC_except_table167
- GCC_except_table172
- GCC_except_table174
- GCC_except_table184
- GCC_except_table26
- GCC_except_table60
- GCC_except_table80
- GCC_except_table85
- _CFDataCreate
- _CSTaskHasStarted
- __ZN37small_objc_portable_task_crash_info_tD1Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne190102EPKvm
- __ZNKSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI25_CSBinaryImageInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI30_CSBinaryRelocationInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS6_IyEEEEEEPvEENS_22__hash_node_destructorINS6_ISI_EEEEE5resetB8ne190102EPSI_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__111__sift_downB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS5_IyEEEEEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS5_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ne190102EmRS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
- __ZNSt3__119__partial_sort_implB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne190102EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB8ne190102EPS7_
- __ZNSt3__126__insertion_sort_unguardedB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEbT1_S9_T0_
- __ZNSt3__131__partition_with_equals_on_leftB8ne190102INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEET0_S9_S9_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne190102INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_S9_T0_
- __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__19allocatorI10_CSTypeRefE17allocate_at_leastB8ne190102Em
- __ZNSt3__19allocatorI14RangeAndStringE17allocate_at_leastB8ne190102Em
- __ZNSt3__19allocatorI25_CSBinaryImageInformationE17allocate_at_leastB8ne190102Em
- __ZNSt3__19allocatorI30_CSBinaryRelocationInformationE17allocate_at_leastB8ne190102Em
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZZL22demangleSwiftClassNamePKcE16s_demodularRegex
- __Znwm
- ___Block_byref_object_copy_.16
- ___Block_byref_object_dispose_.17
- ___block_descriptor_81_ea8_32s40s48s56s64bs72bs_e14_v24?0Q8I16I20ls32l8s64l8s72l8s40l8s48l8s56l8
- ___block_literal_global.113
- ___block_literal_global.224
- ___block_literal_global.32
- ___block_literal_global.450
- ___block_literal_global.469
- ___block_literal_global.500
- ___block_literal_global.522
- ___block_literal_global.595
- ___stringFromMappedNSCFData_block_invoke
- _objc_msgSend$flushRemoteMirrorMemoryCacheEntryForAddress:
- _objc_msgSend$initWithSamplingContext:thread:recordFramePointers:
- _objc_msgSend$recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:
- _objc_msgSend$sampleAllThreadsOnceWithFramePointers:
- _objc_retain_x11
- _stringFromMappedNSCFData.cfDataSize
- _stringFromMappedNSCFData.cold.1
- _stringFromMappedNSCFData.onceToken
- _task_peek_if_pages_exist
CStrings:
+ "\n    "
+ " (%@:%@)"
+ " (empty)"
+ " [inlined]"
+ "%#llx %@"
+ "%-*u %@"
+ "%@\t%#18llx %@"
+ "%@ + %llu%@%@"
+ "%@ -- failed to read content due to insufficient buffer length"
+ "%@ -- failed to read content due to memory allocation failure - is length reasonable?"
+ "%@ -- failed to read content from %#llx-%#llx[%ld] %@\n"
+ "%p + %llu"
+ "%s ELIDED %u LEVELS OF RECURSION THROUGH %s"
+ "%s RECURSION %u, LEVEL %u"
+ "%s RECURSION LEVEL %u"
+ "*** ignoring non-numeric symbolLocation: '%@'"
+ "--------"
+ "@28@0:8^{sampling_context_t=}16I24"
+ "MULTIPLE RANGES OF RECURSION: %zu\n"
+ "Q40@0:8@16Q24I32B36"
+ "T@\"VMUVMRegionIdentifier\",R,N,V_regionIdentifier"
+ "TI,N,V_coldestElided"
+ "TI,N,V_depth"
+ "TI,N,V_hottestElided"
+ "TQ,N,V_keyPC"
+ "Thread %u::  %s\n"
+ "VMUBacktraceRecursionInfo"
+ "_coldestElided"
+ "_depth"
+ "_hottestElided"
+ "_keyPC"
+ "_previousRecursionKeyPCs"
+ "alloc_typed"
+ "asyncRecursionInfoArray"
+ "audiomxd"
+ "base"
+ "coldestElided"
+ "depth"
+ "failed to read content - bad data length %llu causes range overflow"
+ "fixNonEmptyMallocRegionType"
+ "formatFrame:showBinaryImage:"
+ "hottestElided"
+ "hottestElided: %u  coldestElided: %u  depth: %u  %#llx"
+ "imageOffset"
+ "initWithDictionary:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "initWithSamplingContext:thread:"
+ "inline"
+ "isOSObject"
+ "keyPC"
+ "labelForNSCFData:length:remoteAddress:"
+ "mediaplaybackd"
+ "operator_new_impl"
+ "originalLength"
+ "printRecursiveBacktrace:threadIndex:"
+ "recordSampleTo:timestamp:thread:clearMemoryCache:"
+ "recursionInfoArray"
+ "regionIdentifier"
+ "setColdestElided:"
+ "setDepth:"
+ "setHottestElided:"
+ "setKeyPC:"
+ "setUpForFormatFrame:"
+ "sourceFile"
+ "sourceLine"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "symbol"
+ "symbolLocation"
+ "videocodecd"
+ "wasAllRecursionPreviouslyPrinted:"
+ "wifid"
+ "{?=\"context\"{?=\"pid\"i\"thread\"I\"run_state\"i\"dispatch_queue_serial_num\"Q}\"frames\"^Q\"framePtrs\"^Q\"length\"I\"originalLength\"I\"recursionInfoArray\"@\"NSArray\"}"
+ "{unordered_map<NSString *, unsigned int, NSStringHashFunctor, NSStringEqualsFunctor, std::allocator<std::pair<NSString *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, unsigned int>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringHashFunctor, NSStringEqualsFunctor>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringEqualsFunctor, NSStringHashFunctor>, std::allocator<std::__hash_value_type<NSString *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<SwiftFieldKey, unsigned int, std::hash<SwiftFieldKey>, std::equal_to<SwiftFieldKey>, std::allocator<std::pair<const SwiftFieldKey, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<SwiftFieldKey, unsigned int>, std::__unordered_map_hasher<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::hash<SwiftFieldKey>, std::equal_to<SwiftFieldKey>>, std::__unordered_map_equal<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::equal_to<SwiftFieldKey>, std::hash<SwiftFieldKey>>, std::allocator<std::__hash_value_type<SwiftFieldKey, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<VMUClassInfo *, unsigned int, std::hash<VMUClassInfo *>, std::equal_to<VMUClassInfo *>, std::allocator<std::pair<VMUClassInfo *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<VMUClassInfo *, unsigned int>, std::__unordered_map_hasher<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::hash<VMUClassInfo *>, std::equal_to<VMUClassInfo *>>, std::__unordered_map_equal<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::equal_to<VMUClassInfo *>, std::hash<VMUClassInfo *>>, std::allocator<std::__hash_value_type<VMUClassInfo *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<VMUFieldInfo *, unsigned int, std::hash<VMUFieldInfo *>, std::equal_to<VMUFieldInfo *>, std::allocator<std::pair<VMUFieldInfo *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::__unordered_map_hasher<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::hash<VMUFieldInfo *>, std::equal_to<VMUFieldInfo *>>, std::__unordered_map_equal<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::equal_to<VMUFieldInfo *>, std::hash<VMUFieldInfo *>>, std::allocator<std::__hash_value_type<VMUFieldInfo *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<const char *, unsigned int, cstring_callbacks, cstring_callbacks, std::allocator<std::pair<const char *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, unsigned int>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>, std::allocator<std::__hash_value_type<const char *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<std::string, std::unordered_set<unsigned long long>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::unordered_set<unsigned long long>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long long, unsigned int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, unsigned int>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__table_\"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<RangeAndString, std::allocator<RangeAndString>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "\x81a"
- "$2"
- "@32@0:8^{sampling_context_t=}16I24B28"
- "B24@0:8r^*16"
- "Q44@0:8@16Q24I32B36B40"
- "^([0-9a-zA-Z]+)\\.([0-9a-zA-Z].+)"
- "content length %ld -- failed to read data from %#llx"
- "flushRemoteMirrorMemoryCacheEntryForAddress:"
- "initWithSamplingContext:thread:recordFramePointers:"
- "labelForNSConcreteMutableData:length:remoteAddress:"
- "labelForNSData:length:remoteAddress:"
- "recordSampleTo:timestamp:thread:recordFramePointers:clearMemoryCache:"
- "sampleAllThreadsOnceWithFramePointers:"
- "{?=\"context\"{?=\"pid\"i\"thread\"I\"run_state\"i\"dispatch_queue_serial_num\"Q}\"frames\"^Q\"framePtrs\"^Q\"length\"I}"
- "{unordered_map<NSString *, unsigned int, NSStringHashFunctor, NSStringEqualsFunctor, std::allocator<std::pair<NSString *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, unsigned int>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringHashFunctor, NSStringEqualsFunctor>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringEqualsFunctor, NSStringHashFunctor>, std::allocator<std::__hash_value_type<NSString *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringHashFunctor, NSStringEqualsFunctor>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, unsigned int>, NSStringEqualsFunctor, NSStringHashFunctor>>=\"__value_\"f}}}"
- "{unordered_map<SwiftFieldKey, unsigned int, std::hash<SwiftFieldKey>, std::equal_to<SwiftFieldKey>, std::allocator<std::pair<const SwiftFieldKey, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<SwiftFieldKey, unsigned int>, std::__unordered_map_hasher<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::hash<SwiftFieldKey>, std::equal_to<SwiftFieldKey>>, std::__unordered_map_equal<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::equal_to<SwiftFieldKey>, std::hash<SwiftFieldKey>>, std::allocator<std::__hash_value_type<SwiftFieldKey, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<SwiftFieldKey, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::hash<SwiftFieldKey>, std::equal_to<SwiftFieldKey>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<SwiftFieldKey, std::__hash_value_type<SwiftFieldKey, unsigned int>, std::equal_to<SwiftFieldKey>, std::hash<SwiftFieldKey>>>=\"__value_\"f}}}"
- "{unordered_map<VMUClassInfo *, unsigned int, std::hash<VMUClassInfo *>, std::equal_to<VMUClassInfo *>, std::allocator<std::pair<VMUClassInfo *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<VMUClassInfo *, unsigned int>, std::__unordered_map_hasher<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::hash<VMUClassInfo *>, std::equal_to<VMUClassInfo *>>, std::__unordered_map_equal<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::equal_to<VMUClassInfo *>, std::hash<VMUClassInfo *>>, std::allocator<std::__hash_value_type<VMUClassInfo *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<VMUClassInfo *, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::hash<VMUClassInfo *>, std::equal_to<VMUClassInfo *>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<VMUClassInfo *, std::__hash_value_type<VMUClassInfo *, unsigned int>, std::equal_to<VMUClassInfo *>, std::hash<VMUClassInfo *>>>=\"__value_\"f}}}"
- "{unordered_map<VMUFieldInfo *, unsigned int, std::hash<VMUFieldInfo *>, std::equal_to<VMUFieldInfo *>, std::allocator<std::pair<VMUFieldInfo *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::__unordered_map_hasher<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::hash<VMUFieldInfo *>, std::equal_to<VMUFieldInfo *>>, std::__unordered_map_equal<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::equal_to<VMUFieldInfo *>, std::hash<VMUFieldInfo *>>, std::allocator<std::__hash_value_type<VMUFieldInfo *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<VMUFieldInfo *, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::hash<VMUFieldInfo *>, std::equal_to<VMUFieldInfo *>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<VMUFieldInfo *, std::__hash_value_type<VMUFieldInfo *, unsigned int>, std::equal_to<VMUFieldInfo *>, std::hash<VMUFieldInfo *>>>=\"__value_\"f}}}"
- "{unordered_map<const char *, unsigned int, cstring_callbacks, cstring_callbacks, std::allocator<std::pair<const char *const, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, unsigned int>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>, std::allocator<std::__hash_value_type<const char *, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, unsigned int>, cstring_callbacks, cstring_callbacks>>=\"__value_\"f}}}"
- "{unordered_map<std::string, std::unordered_set<unsigned long long>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::unordered_set<unsigned long long>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::unordered_set<unsigned long long>>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned long long, unsigned int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, unsigned int>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, unsigned int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__table_\"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *>, std::allocator<std::__hash_node<unsigned long long, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<unsigned long long>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<unsigned long long>>=\"__value_\"f}}}"
- "{vector<RangeAndString, std::allocator<RangeAndString>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<RangeAndString *, std::allocator<RangeAndString>>=\"__value_\"^{?}}}"

```
