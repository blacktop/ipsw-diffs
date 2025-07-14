## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64561.91.2.0.0
-  __TEXT.__text: 0x99fac
-  __TEXT.__auth_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x55e0
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0xd0f1
-  __TEXT.__gcc_except_tab: 0x317c
-  __TEXT.__oslogstring: 0x1178
+64565.70.2.0.0
+  __TEXT.__text: 0x99878
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0x5750
+  __TEXT.__const: 0x1c0
+  __TEXT.__cstring: 0xd5e7
+  __TEXT.__gcc_except_tab: 0x32a4
+  __TEXT.__oslogstring: 0x11bc
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x23b0
+  __TEXT.__unwind_info: 0x2420
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x6dd
-  __TEXT.__objc_methname: 0xda9a
-  __TEXT.__objc_methtype: 0x3a35
-  __TEXT.__objc_stubs: 0x8da0
+  __TEXT.__objc_classname: 0x6ed
+  __TEXT.__objc_methname: 0xddd2
+  __TEXT.__objc_methtype: 0x3adf
+  __TEXT.__objc_stubs: 0x90a0
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x2c60
-  __DATA_CONST.__objc_classlist: 0x250
+  __DATA_CONST.__const: 0x2e08
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9358
-  __DATA_CONST.__objc_selrefs: 0x2f68
+  __DATA_CONST.__objc_const: 0x9538
+  __DATA_CONST.__objc_selrefs: 0x3038
+  __DATA_CONST.__objc_classrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x3d8
-  __AUTH_CONST.__cfstring: 0xae60
-  __AUTH_CONST.__objc_const: 0x168
-  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__cfstring: 0xb060
+  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xef8
-  __DATA.__objc_classrefs: 0x300
-  __DATA.__objc_superrefs: 0x1c0
-  __DATA.__objc_ivar: 0xaec
-  __DATA.__data: 0xe18
+  __AUTH_CONST.__auth_got: 0xf58
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xb1c
+  __DATA.__data: 0xe28
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x8
   __DATA.__bss: 0x3c0
   __DATA.__common: 0x1
-  __DATA_DIRTY.__const: 0x468
+  __DATA_DIRTY.__const: 0x388
   __DATA_DIRTY.__objc_const: 0x19e0
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EB42858A-4966-30A8-A9CC-AD59D40D9A9A
-  Functions: 2631
-  Symbols:   8925
-  CStrings:  6591
+  UUID: 213319AB-0FBC-3172-870A-18AE795A49C3
+  Functions: 2673
+  Symbols:   9076
+  CStrings:  6702
 
Symbols:
+ -[VMUDirectedGraph plistRepresentationWithOptions:fromOriginalMemgraph:]
+ -[VMUFakeSampler .cxx_destruct]
+ -[VMUFakeSampler initWithProcessObjectGraph:]
+ -[VMUFakeSampler threadDescriptionStringForBacktrace:returnedAddress:]
+ -[VMUObjectIdentifier countFromPointerInAutoreleasePool:]
+ -[VMUProcessObjectGraph autoreleasePoolOffsets]
+ -[VMUProcessObjectGraph initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:autoreleasePoolOffsets:]
+ -[VMUProcessObjectGraph parseAddressesFromNodeLabelsIntoSymbolStore]
+ -[VMUStackLogReaderBase vmuTask]
+ -[VMUSwiftRuntimeInfo initWithSwiftCore:memoryReader:isExclave:]
+ -[VMUTask addressIsInSharedCache:]
+ -[VMUTask isExclaveCore]
+ -[VMUTask isExclaveKit]
+ -[VMUTask isExclave]
+ -[VMUTask ptrauthStripCodePointer:]
+ -[VMUTask ptrauthStripDataPointer:]
+ -[VMUTask ptrauthStripFunctionPointer:]
+ -[VMUTask rangeIsInSharedCache:]
+ -[VMUTask taskDyldSharedCacheRange]
+ -[VMUTaskMemoryCache coreHasInfoRequiredForMemoryAnalysis]
+ -[VMUTaskMemoryCache getExclaveVMFlagsForAddress:exclaveVMFlags:]
+ -[VMUTaskMemoryCache isExclaveCore]
+ -[VMUTaskMemoryCache isExclaveKit]
+ -[VMUTaskMemoryCache isExclave]
+ -[VMUTaskMemoryScanner initWithVMUTask:options:].cold.1
+ -[VMUVMRegion getVMRegionExclaveFlagsData:]
+ -[VMUVMRegion isActivityTracing]
+ -[VMUVMRegion isAnalysisToolRegion]
+ -[VMUVMRegion isFoundation]
+ -[VMUVMRegion isHeapRelated]
+ -[VMUVMRegion isIOSurface]
+ -[VMUVMRegion isJavascriptJitExecutableAllocator]
+ -[VMUVMRegion isOwnedUnmappedMemory]
+ -[VMUVMRegion isSanitizer]
+ -[VMUVMRegion isStack]
+ -[VMUVMRegion isUnsharedPmap]
+ -[VMUVMRegion setVMRegionExclaveFlagsData:]
+ -[VMUVMRegion splitOutRange:fromRegionIndex:regions:]
+ -[VMUVMRegion splitOutRange:fromRegionIndex:regions:].cold.1
+ -[VMUVMRegion willNotHoldPointers]
+ GCC_except_table127
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table33
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table72
+ OBJC_IVAR_$_VMUStackLogReaderBase._vmuTask
+ OBJC_IVAR_$_VMUVMRegion.exclaveFlags
+ OBJC_IVAR_$_VMUVMRegion.isExclaveRegion
+ _CSSymbolicatorGetSymbolOwner
+ _OBJC_CLASS_$_VMUFakeSampler
+ _OBJC_IVAR_$_VMUFakeSampler._graph
+ _OBJC_IVAR_$_VMUProcessObjectGraph._autoreleasePoolOffsets
+ _OBJC_IVAR_$_VMUSymbolStore.hexFromLabels
+ _OBJC_IVAR_$_VMUTask._isExclave
+ _OBJC_IVAR_$_VMUTask._isExclaveCore
+ _OBJC_IVAR_$_VMUTask._isExclaveKit
+ _OBJC_IVAR_$_VMUTask._taskDyldSharedCacheRange
+ _OBJC_IVAR_$_VMUTaskMemoryCache._isExclave
+ _OBJC_IVAR_$_VMUTaskMemoryCache._isExclaveCore
+ _OBJC_METACLASS_$_VMUFakeSampler
+ _VMUExclaveOrDarwinRegionTypeDescriptionForTagShareProtAndPager
+ _VMUExclaveRegionTypeDescriptionForTagShareProtAndPager
+ __OBJC_$_INSTANCE_METHODS_VMUFakeSampler
+ __OBJC_$_INSTANCE_VARIABLES_VMUFakeSampler
+ __OBJC_CLASS_RO_$_VMUFakeSampler
+ __OBJC_METACLASS_RO_$_VMUFakeSampler
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ue170006ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ue170006EPKvm
+ __ZNKSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ue170006ERKS6_S9_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt12out_of_rangeC1B8ue170006EPKc
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_Lb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb
+ __ZNSt3__111__sift_downB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__116__insertion_sortB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS1_IyEEEEEEPvEEEEE7destroyB8ue170006INS_4pairIKS8_SF_EEvvEEvRSJ_PT_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI10_CSTypeRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI14RangeAndStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__partial_sort_implB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ue170006EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ue170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ue170006EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ue170006EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB8ue170006EPS7_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS1_IyEEEEEEPvEEEEEclB8ue170006EPSI_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEEEEEclB8ue170006EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEEEEEclB8ue170006EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEEEEEclB8ue170006EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEEEEEclB8ue170006EPS9_
+ __ZNSt3__126__insertion_sort_unguardedB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEbT1_S9_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB8ue170006INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEET0_S9_S9_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ue170006INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE16__init_with_sizeB8ue170006IPS1_S6_EEvT_T0_m
+ __ZNSt3__17__sort3B8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_T0_
+ __ZNSt3__17__sort4B8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__19__sift_upB8ue170006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.265
+ ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.279
+ ___62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.123
+ ___62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.140
+ ___64-[VMUSwiftRuntimeInfo initWithSwiftCore:memoryReader:isExclave:]_block_invoke
+ ___66-[VMUObjectGraph initWithArchived:version:options:diskLogs:error:]_block_invoke
+ ___68-[VMUProcessObjectGraph parseAddressesFromNodeLabelsIntoSymbolStore]_block_invoke
+ ___72-[VMUDirectedGraph plistRepresentationWithOptions:fromOriginalMemgraph:]_block_invoke
+ ____getRegionMallocStatistics_block_invoke
+ ____getRegionMallocStatistics_block_invoke_2
+ ____getRegionMallocStatistics_block_invoke_3
+ ____getRegionMallocStatistics_block_invoke_3.cold.1
+ ____markRegionsForMallocZones_block_invoke
+ ____markRegionsForMallocZones_block_invoke_2
+ ____markRegionsForMallocZones_block_invoke_3
+ ____markRegionsForMallocZones_block_invoke_4
+ ____markRegionsForMallocZones_block_invoke_4.cold.1
+ ____markRegionsForMallocZones_block_invoke_4.cold.2
+ ___block_descriptor_104_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_114_e8_32s40s48s56s64r72r_e22_v24?0{_CSTypeRef=QQ}8lr64l8s32l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_48_e8_32s_e9_v16?0^?8ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e12_v20?0I8^B12ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e9_v16?0^?8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e18_v16?0"NSString"8lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40r_e27_v32?0{_VMURange=QQ}8I24i28lr40l8s32l8
+ ___block_descriptor_64_e8_32s40r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24lr40l8s32l8
+ ___block_descriptor_72_e8_32s40bs48r56r_e27_v32?0{_VMURange=QQ}8I24i28lr48l8s40l8s32l8r56l8
+ ___block_descriptor_72_e8_32s40s48r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24lr48l8s32l8s40l8
+ ___block_descriptor_73_ea8_32s40s48s56bs64bs_e14_v24?0Q8I16I20ls32l8s56l8s64l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.145
+ ___block_literal_global.29
+ ___block_literal_global.317
+ ___block_literal_global.321
+ ___block_literal_global.382
+ ___block_literal_global.437
+ ___block_literal_global.457
+ ___block_literal_global.46
+ ___block_literal_global.486
+ ___block_literal_global.503
+ ___block_literal_global.511
+ ___block_literal_global.690
+ ___block_literal_global.73
+ ___destructor_8_s0_s56_s64_sb72
+ ___remoteZoneIntrospection_block_invoke.71
+ __mallocEnumerationHandler
+ _dyld_process_create_for_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_get_shared_cache
+ _dyld_shared_cache_get_base_address
+ _dyld_shared_cache_get_mapped_size
+ _dyld_shared_cache_is_mapped_private
+ _mapped_memory_core_file_get_exclave_vm_flags_for_address
+ _mapped_memory_core_file_is_exclave
+ _mapped_memory_core_file_is_exclavecore
+ _objc_msgSend$addressIsInSharedCache:
+ _objc_msgSend$coreHasInfoRequiredForMemoryAnalysis
+ _objc_msgSend$countFromPointerInAutoreleasePool:
+ _objc_msgSend$getExclaveVMFlagsForAddress:exclaveVMFlags:
+ _objc_msgSend$getVMRegionExclaveFlagsData:
+ _objc_msgSend$initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:autoreleasePoolOffsets:
+ _objc_msgSend$initWithProcessObjectGraph:
+ _objc_msgSend$initWithSwiftCore:memoryReader:isExclave:
+ _objc_msgSend$isActivityTracing
+ _objc_msgSend$isAnalysisToolRegion
+ _objc_msgSend$isExclave
+ _objc_msgSend$isExclaveCore
+ _objc_msgSend$isExclaveKit
+ _objc_msgSend$isFoundation
+ _objc_msgSend$isHeapRelated
+ _objc_msgSend$isIOSurface
+ _objc_msgSend$isJavascriptJitExecutableAllocator
+ _objc_msgSend$isOwnedUnmappedMemory
+ _objc_msgSend$isSanitizer
+ _objc_msgSend$isStack
+ _objc_msgSend$isUnsharedPmap
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$parseAddressesFromNodeLabelsIntoSymbolStore
+ _objc_msgSend$plistRepresentationWithOptions:fromOriginalMemgraph:
+ _objc_msgSend$rangeIsInSharedCache:
+ _objc_msgSend$setVMRegionExclaveFlagsData:
+ _objc_msgSend$splitOutRange:fromRegionIndex:regions:
+ _objc_msgSend$taskDyldSharedCacheRange
+ _objc_msgSend$willNotHoldPointers
+ _objc_release_x10
+ _recursivelyListAllRegions
+ _remoteZoneIntrospection.exclaveIntrospectionDetails
+ _remoteZoneIntrospection.exclaveIntrospectionDetailsToken
+ _remoteZoneIntrospection.getExclaveIntrospectionSucceeded
- -[VMUProcessObjectGraph initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:]
- -[VMUSwiftRuntimeInfo initWithSwiftCore:memoryReader:]
- -[VMUTaskMemoryCache coreHasInfoRequriedForMemoryAnalysis]
- GCC_except_table116
- GCC_except_table126
- GCC_except_table130
- GCC_except_table133
- GCC_except_table137
- GCC_except_table45
- GCC_except_table61
- GCC_except_table64
- GCC_except_table84
- _LZ4HC_compress_generic
- _LZ4_compressHC2_limitedOutput
- _LZ4_compressHC_limitedOutput
- _LZ4_compress_limitedOutput
- _LZ4_decompress_generic.dec64table
- _LZ4_decompress_safe
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB7v160006ERKS6_S9_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt12out_of_rangeC1B7v160006EPKc
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__111__sift_downB7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS1_IyEEEEEEPvEEEEE7destroyB7v160006INS_4pairIKS8_SF_EEvvEEvRSJ_PT_
- __ZNSt3__118__insertion_sort_3B7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI10_CSTypeRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI14RangeAndStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__partial_sort_implB7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__120__throw_out_of_rangeB7v160006EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EEclEPKvm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB7v160006EPS7_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS1_IyEEEEEEPvEEEEEclB7v160006EPSI_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEEEEEclB7v160006EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEEEEEclB7v160006EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEEEEEclB7v160006EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEEEEEclB7v160006EPS9_
- __ZNSt3__127__insertion_sort_incompleteIRPFbRK14RangeAndStringS3_EPS1_EEbT0_S8_T_
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_T0_
- __ZNSt3__17__sort4B7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5IRPFbRK14RangeAndStringS3_EPS1_EEjT0_S8_S8_S8_S8_T_
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___47-[VMUProcessObjectGraph sampleBacktracesString]_block_invoke
- ___54-[VMUSwiftRuntimeInfo initWithSwiftCore:memoryReader:]_block_invoke
- ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.262
- ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.276
- ___62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.120
- ___62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.137
- ___62-[VMUProcessObjectGraph _generateSymbolStoreFromExistingGraph]_block_invoke_3
- ___VMUCompressedBuffer_block_invoke_5
- ___block_descriptor_105_e8_32s40s48r56r_e20_v24?0I8^{?=QQ}12I20ls32l8s40l8r48l8r56l8
- ___block_descriptor_106_e8_32s40s48s56r64r_e22_v24?0{_CSTypeRef=QQ}8lr56l8s32l8r64l8s40l8s48l8
- ___block_descriptor_32_e15_B32?08Q16^B24l
- ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
- ___block_descriptor_50_e9_Q16?0^v8l
- ___block_descriptor_65_ea8_32s40s48bs56bs_e14_v24?0Q8I16I20ls48l8s56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s_e9_v16?0^?8ls32l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s56r_e22_v24?0{_CSTypeRef=QQ}8lr56l8s32l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24ls32l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56r_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8r56l8s48l8
- ___block_literal_global.316
- ___block_literal_global.320
- ___block_literal_global.381
- ___block_literal_global.44
- ___block_literal_global.458
- ___block_literal_global.487
- ___block_literal_global.504
- ___block_literal_global.505
- ___block_literal_global.686
- ___block_literal_global.78
- ___markMallocAreas_block_invoke_2
- ___markMallocAreas_block_invoke_3
- ___markMallocAreas_block_invoke_4
- _lz4_decode
- _lz4_decode_fast
- _lz4_decode_safe
- _lz4_encode
- _objc_msgSend$coreHasInfoRequriedForMemoryAnalysis
- _objc_msgSend$initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:
- _objc_msgSend$initWithSwiftCore:memoryReader:
- _objc_msgSend$replaceObjectsAtIndexes:withObjects:
- _objc_msgSend$rootForSamples:symbolicator:
CStrings:
+ "\x01\x14"
+ "\x112"
+ "*** task_malloc_get_all_zones: target has no active zones\n"
+ "*** task_malloc_get_all_zones: unexpected number of binaries in ExclaveCore target\n"
+ "-[VMUTaskMemoryScanner _initWithTask:options:]: region identifier detected no regions, so returning nil VMUTaskMemoryScanner"
+ "-[VMUVMRegion splitOutRange:fromRegionIndex:regions:]"
+ "/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector"
+ "/usr/lib/system/libsystem_blocks.dylib"
+ "1\x13\x15\x12\x12A\x14\x11"
+ "1A"
+ "@32@0:8Q16@24"
+ "@44@0:8{_CSTypeRef=QQ}16@?32B40"
+ "@48@0:8{_VMURange=QQ}16Q32@40"
+ "@60@0:8@16{_CSTypeRef=QQ}24@40@48B56"
+ "@80@0:8i16^{_VMUBlockNode=Qb3b2b36b23}20I28@32@40@48@56^v64^{VMUAutoreleasePoolPageLayout=IIIQI}72"
+ "@88@0:8Q16Q24I32I36@40Q48Q56Q64Q72@80"
+ "CNODE"
+ "DATA"
+ "EXCLAVEDRIVERKIT"
+ "Exclave memory tag %hhu"
+ "ExclaveCore"
+ "ExclaveKit"
+ "Failed to find xzm zone introspection structure"
+ "Failed to get udata pointers for core file."
+ "Firmware"
+ "GUARD"
+ "LAUNCHERDATA"
+ "LINKEDIT"
+ "MALLOC (empty)"
+ "MALLOC_BIG"
+ "MALLOC_DATA"
+ "MALLOC_PTR"
+ "MMAP"
+ "MMIO"
+ "MallocStackLoggingLiteZone"
+ "MallocStackLoggingLiteZone_Wrapper"
+ "Number of addresses sent to VMUSymbolStore by client classes:\nFor backtrace sample: %zu\nFor binary sections: %zu\nFor global variables: %zu\nFor malloc stack logging: %zu\nFor hex found in node labels: %zu\nTotal unique addresses to be saved to symbolicator signature: %zu\nNumber of UUIDs in the signature: %zu\n"
+ "Q24@0:8^v16"
+ "SANITIZER"
+ "SHARED"
+ "STACK"
+ "SurfaceID: %#x  %llux%llu (%s) %s"
+ "T@\"NSString\",?,R,C"
+ "T@\"VMUTask\",R,V_vmuTask"
+ "TEXT"
+ "TQ,?,R"
+ "TQ,R,V_height"
+ "TQ,R,V_width"
+ "TRACE"
+ "Thread_%u"
+ "USER"
+ "Unable to deserialize the memgraph %@"
+ "VAS_CNODE"
+ "VAS_DATA"
+ "VMUFakeSampler"
+ "VMUMaxRange(newVMRangeForZone) == rangeStartInRegion"
+ "VMURangeContainsRange(self->range, rangeToExtract)"
+ "VMUVMRegionIdentifier.m"
+ "[Exclave Flag Data] Count: %u\n\n"
+ "_autoreleasePoolOffsets"
+ "_getRegionMallocStatistics_block_invoke_3"
+ "_isExclave"
+ "_isExclaveCore"
+ "_isExclaveKit"
+ "_markRegionsForMallocZones_block_invoke_4"
+ "_objc_debug_autoreleasepoolpage_child_offset"
+ "_taskDyldSharedCacheRange"
+ "addressIsInSharedCache:"
+ "autoreleasePoolOffsets"
+ "childPageOffset"
+ "coreHasInfoRequiredForMemoryAnalysis"
+ "countFromPointerInAutoreleasePool:"
+ "exclaveFlagData"
+ "exclaveFlags"
+ "firstEntryOffset"
+ "getExclaveVMFlagsForAddress:exclaveVMFlags:"
+ "getVMRegionExclaveFlagsData:"
+ "hexFromLabels"
+ "i32@0:8Q16^I24"
+ "initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:autoreleasePoolOffsets:"
+ "initWithProcessObjectGraph:"
+ "initWithSwiftCore:memoryReader:isExclave:"
+ "isActivityTracing"
+ "isAnalysisToolRegion"
+ "isExclave"
+ "isExclaveCore"
+ "isExclaveKit"
+ "isExclaveRegion"
+ "isFoundation"
+ "isHeapRelated"
+ "isIOSurface"
+ "isJavascriptJitExecutableAllocator"
+ "isOwnedUnmappedMemory"
+ "isSanitizer"
+ "isStack"
+ "isUnsharedPmap"
+ "localizedFailureReason"
+ "marking malloc VM regions"
+ "marking malloc allocations in VM regions"
+ "parentPageOffset"
+ "parseAddressesFromNodeLabelsIntoSymbolStore"
+ "plistRepresentationWithOptions:fromOriginalMemgraph:"
+ "rangeIsInSharedCache:"
+ "sepOS"
+ "setVMRegionExclaveFlagsData:"
+ "splitOutRange:fromRegionIndex:regions:"
+ "taskDyldSharedCacheRange"
+ "v24@0:8^{_VMUVMRegionExclaveFlagsData=I}16"
+ "v32@?0@8@16^B24"
+ "v32@?0{_VMURange=QQ}8I24i28"
+ "visionOS"
+ "visionOS Simulator"
+ "willNotHoldPointers"
+ "xzm_malloc_zone_introspect"
+ "{?=III}16@0:8"
+ "\xf0\x91"
- "\x11\x12"
- "\x14"
- "    1 "
- "    1 Thread_"
- "    1 Thread_%x"
- "-[VMUTaskMemoryScanner _initWithTask:options:]: region identifer detected no regions, so returning nil VMUTaskMemoryScanner"
- "1\x13\x15\x11\x12A\x14\x11"
- "@40@0:8{_CSTypeRef=QQ}16@?32"
- "@56@0:8I16{_CSTypeRef=QQ}20@36@44B52"
- "@72@0:8i16^{_VMUBlockNode=Qb3b2b36b23}20I28@32@40@48@56^v64"
- "@80@0:8Q16Q24I32I36@40I48I52Q56Q64@72"
- "A!"
- "B32@?0@8Q16^B24"
- "MallocStackLoggingLite"
- "Number of addresses sent to VMUSymbolStore by client classes:\nFor backtrace sample: %zu\nFor binary sections: %zu\nFor global variables: %zu\nFor malloc stack logging: %zu\nTotal unique addresses to be saved to symbolicator signature: %zu\nNumber of UUIDs in the signature: %zu\n"
- "SurfaceID: %#x  %ux%u (%s) %s"
- "TI,R,V_height"
- "TI,R,V_width"
- "__block variable"
- "coreHasInfoRequriedForMemoryAnalysis"
- "initWithPid:nodes:nodeCount:zoneNames:classInfoMap:regions:pthreadOffsets:userMarked:"
- "initWithSwiftCore:memoryReader:"
- "replaceObjectsAtIndexes:withObjects:"
- "\xf0\x81"

```
