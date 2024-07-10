## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

-64566.89.1.0.0
-  __TEXT.__text: 0xb24c0
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x5e4c
+64566.95.1.0.0
+  __TEXT.__text: 0xb3a30
+  __TEXT.__auth_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x5e84
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xf0f7
-  __TEXT.__gcc_except_tab: 0x45b4
+  __TEXT.__cstring: 0xf494
+  __TEXT.__gcc_except_tab: 0x4ff8
   __TEXT.__oslogstring: 0x152f
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x2730
-  __TEXT.__objc_classname: 0x84d
-  __TEXT.__objc_methname: 0xee1c
-  __TEXT.__objc_methtype: 0x3d17
-  __TEXT.__objc_stubs: 0x97c0
+  __TEXT.__unwind_info: 0x2850
+  __TEXT.__objc_classname: 0x84f
+  __TEXT.__objc_methname: 0xee51
+  __TEXT.__objc_methtype: 0x8507
+  __TEXT.__objc_stubs: 0x9800
   __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xca8
+  __DATA_CONST.__const: 0xce0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33a8
-  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_selrefs: 0x33c0
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x718
-  __AUTH_CONST.__auth_got: 0xf18
+  __AUTH_CONST.__auth_got: 0xf08
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x38f0
-  __AUTH_CONST.__cfstring: 0xc880
+  __AUTH_CONST.__const: 0x3950
+  __AUTH_CONST.__cfstring: 0xc9a0
   __AUTH_CONST.__objc_const: 0xc658
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0xc48
-  __DATA.__data: 0xd48
+  __DATA.__data: 0xd58
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x608
   __DATA.__common: 0x9

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2979
-  Symbols:   7132
-  CStrings:  2558
+  Functions: 2997
+  Symbols:   7187
+  CStrings:  2582
 
Symbols:
+ -[VMUClassInfoMap .cxx_construct]
+ -[VMUNodeToStringMap .cxx_construct]
+ -[VMURangeArray containsLocation:]
+ -[VMURangeArray containsRange:]
+ -[VMURangeToStringMap .cxx_construct]
+ -[VMUSimpleDeserializer .cxx_construct]
+ -[VMUSimpleSerializer .cxx_construct]
+ -[VMUSimpleSerializer .cxx_destruct]
+ -[VMUVMRegion isUntaggedRegion]
+ -[VMUVMRegion setAsMallocRegion]
+ GCC_except_table106
+ GCC_except_table131
+ GCC_except_table143
+ GCC_except_table172
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table69
+ GCC_except_table89
+ OBJC_IVAR_$_VMUClassInfoMap._classInfoToIndexMap
+ OBJC_IVAR_$_VMUClassInfoMap._fieldInfoToIndexMap
+ OBJC_IVAR_$_VMUClassInfoMap._isaAddressToIndexMap
+ OBJC_IVAR_$_VMUClassInfoMap._swiftFieldToIndexMap
+ OBJC_IVAR_$_VMUNodeToStringMap._nodeToStringIndexMap
+ OBJC_IVAR_$_VMUNodeToStringMap._stringToIndexMap
+ OBJC_IVAR_$_VMURangeToStringMap._rangeAndStringVector
+ OBJC_IVAR_$_VMURangeToStringMap._stringToIndexMap
+ OBJC_IVAR_$_VMUSimpleDeserializer._stringCache
+ OBJC_IVAR_$_VMUSimpleSerializer._internMap
+ VMUMallocRangeTypeString.cold.1
+ _VMUMallocRangeTypeString
+ _VMUmallocOtherRegionLabel
+ _VMUuntaggedRegionLabel
+ __33-[VMUClassInfoMap initWithCoder:]_block_invoke.25
+ __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.186
+ __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.195
+ __47-[VMUVMRegionIdentifier initWithGraph:options:]_block_invoke.139
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.280
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.286
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.289
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.290
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.321
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.336
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.353
+ __68-[VMUProcessDescription initWithVMUTaskMemoryCache:getBinariesList:]_block_invoke.56
+ __98-[VMUStackLogReaderBase identifyNonObjectsUsingStackBacktraces:classInfoMap:classInfoSetterBlock:]_block_invoke.311
+ __99-[VMUVMRegionIdentifier descriptionOfRegionsAroundAddress:options:maximumLength:memorySizeDivisor:]_block_invoke.160
+ __Block_byref_object_copy_.26
+ __Block_byref_object_copy_.77
+ __Block_byref_object_dispose_.27
+ __Block_byref_object_dispose_.78
+ __ZL24_compareBinaryImageDictsP11objc_objectS0_Pv
+ __ZN37small_objc_portable_task_crash_info_tD1Ev
+ __ZNKSt3__16vectorI25_CSBinaryImageInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
+ __ZNKSt3__16vectorI30_CSBinaryRelocationInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE20__node_insert_uniqueEPNS_11__hash_nodeIS5_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE21__emplace_unique_implIJNS_4pairIU8__strongP19VMUMutableClassInfojEEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEEDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JNS_4pairIS4_jEEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIS5_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ne180100EmRS5_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JNS_4pairIS4_jEEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjS5_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIjJNS_4pairIjS4_EEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyjEENS_22__unordered_map_hasherIyS2_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIyJNS_4pairIyjEEEEENSF_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI25_CSBinaryImageInformationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI30_CSBinaryRelocationInformationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZZ36-[VMUProcessDescription _bundleLock]E11_bundleLock
+ __ZZ36-[VMUProcessDescription _bundleLock]E9onceToken
+ ___56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke_2
+ ___block_descriptor_176_e8_32s40s48s56s64r72r80r88r96r104r112r120r_e20_v36?0I8Q12I20I24Q28l
+ ___block_descriptor_40_ea8_32w_e113_v44?0I8{_CSNotificationData={_CSTypeRef=QQ}(?={Ping=I}{DyldLoad={_CSTypeRef=QQ}}{DyldUnload={_CSTypeRef=QQ}})}12l
+ ___block_descriptor_40_ea8_32w_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_41_e8_32s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
+ ___block_descriptor_48_e8_32s40r_e25_v44?0I8{?=Qb60b4}12^B36l
+ ___block_descriptor_48_ea8_32r40r_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_49_e8_32s40r_e23_v28?0I8I12^{?=QQ}16I24l
+ ___block_descriptor_49_e8_32s_e9_v16?0^?8l
+ ___block_descriptor_56_e8_32r_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_56_ea8_32s40s48r_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_57_e8_32s40s_e9_v16?0^?8l
+ ___block_descriptor_65_e8_32s40r_e27_v32?0{_VMURange=QQ}8I24i28l
+ ___block_descriptor_65_e8_32s40r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
+ ___block_descriptor_65_ea8_32s40r48r_e37_v32?0"NSTextCheckingResult"8Q16^B24l
+ ___block_descriptor_73_e8_32s40bs48r56r_e27_v32?0{_VMURange=QQ}8I24i28l
+ ___block_descriptor_73_e8_32s40s48r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r112r120r
+ ___copy_helper_block_ea8_32s40r48r
+ ___copy_helper_block_ea8_32w
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r112r120r
+ ___destroy_helper_block_ea8_32s40r48r
+ ___destroy_helper_block_ea8_32w
+ ___markRegionsForMallocZones_block_invoke.454
+ ___markRegionsForMallocZones_block_invoke.454.cold.1
+ ___markRegionsForMallocZones_block_invoke.454.cold.2
+ __block_literal_global.105
+ __block_literal_global.111
+ __block_literal_global.122
+ __block_literal_global.157
+ __block_literal_global.197
+ __block_literal_global.228
+ __block_literal_global.250
+ __block_literal_global.275
+ __block_literal_global.539
+ __block_literal_global.613
+ __listKernelCoreRegions_block_invoke.406
+ __listKernelCoreRegions_block_invoke.411
+ __markMachOLibraries_block_invoke.437
+ __markMachOLibraries_block_invoke_2.438
+ _addSpecialNodesFromTask.onceToken.120
+ _objc_msgSend$containsLocation:
+ _objc_msgSend$isUntaggedRegion
+ _objc_msgSend$setAsMallocRegion
- -[VMUClassInfoMap dealloc]
- -[VMUNodeToStringMap dealloc]
- -[VMURangeToStringMap dealloc]
- -[VMUSimpleDeserializer dealloc]
- -[VMUSimpleSerializer init]
- -[VMUTaskMemoryScanner callRemoteMallocPrints:printer:]
- GCC_except_table100
- GCC_except_table122
- GCC_except_table134
- OBJC_IVAR_$_VMUClassInfoMap._classInfoMap1
- OBJC_IVAR_$_VMUClassInfoMap._classInfoMap2
- OBJC_IVAR_$_VMUClassInfoMap._fieldInfoMap1
- OBJC_IVAR_$_VMUClassInfoMap._fieldInfoMap2
- OBJC_IVAR_$_VMUNodeToStringMap._nodeToStringIndexMapVoidPtr
- OBJC_IVAR_$_VMUNodeToStringMap._stringToIndexMapVoidPtr
- OBJC_IVAR_$_VMURangeToStringMap._rangeAndStringVectorVoidPtr
- OBJC_IVAR_$_VMURangeToStringMap._stringToIndexMapVoidPtr
- OBJC_IVAR_$_VMUSimpleDeserializer._cache
- OBJC_IVAR_$_VMUSimpleSerializer._map
- __33-[VMUClassInfoMap initWithCoder:]_block_invoke.27
- __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.188
- __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.197
- __47-[VMUVMRegionIdentifier initWithGraph:options:]_block_invoke.128
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.282
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.288
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.293
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.294
- __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.323
- __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.340
- __68-[VMUProcessDescription initWithVMUTaskMemoryCache:getBinariesList:]_block_invoke.54
- __98-[VMUStackLogReaderBase identifyNonObjectsUsingStackBacktraces:classInfoMap:classInfoSetterBlock:]_block_invoke.305
- __99-[VMUVMRegionIdentifier descriptionOfRegionsAroundAddress:options:maximumLength:memorySizeDivisor:]_block_invoke.149
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JNS_4pairIU8__strongKS3_jEEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JNS_4pairIU8__strongKS3_jEEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjU8__strongP8NSStringEENS_22__unordered_map_hasherIjS5_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIjJNS_4pairIKjS4_EEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyjEENS_22__unordered_map_hasherIyS2_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIyJNS_4pairIKyjEEEEENSF_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZdlPvSt19__type_descriptor_t
- __ZnwmSt19__type_descriptor_t
- ___55-[VMUTaskMemoryScanner callRemoteMallocPrints:printer:]_block_invoke
- ___55-[VMUTaskMemoryScanner callRemoteMallocPrints:printer:]_block_invoke_2
- ___block_descriptor_40_e8_32w_e113_v44?0I8{_CSNotificationData={_CSTypeRef=QQ}(?={Ping=I}{DyldLoad={_CSTypeRef=QQ}}{DyldUnload={_CSTypeRef=QQ}})}12l
- ___block_descriptor_40_e8_32w_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_48_e8_32r40r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_48_e8_32s40r_e23_v28?0I8I12^{?=QQ}16I24l
- ___block_descriptor_48_e8_32s_e9_v16?0^?8l
- ___block_descriptor_52_e8_32s_e17_v16?0?<^v?QQ>8l
- ___block_descriptor_52_e8_32s_e9_v16?0^?8l
- ___block_descriptor_56_e8_32s40s48r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_56_e8_32s40s_e9_v16?0^?8l
- ___block_descriptor_64_e8_32s40r_e27_v32?0{_VMURange=QQ}8I24i28l
- ___block_descriptor_64_e8_32s40r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
- ___block_descriptor_72_e8_32s40bs48r56r_e27_v32?0{_VMURange=QQ}8I24i28l
- ___block_descriptor_72_e8_32s40s48r_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
- ___block_descriptor_81_e8_32s40r48r56r64r_e37_v32?0"NSTextCheckingResult"8Q16^B24l
- ___copy_helper_block_e8_32s40r48r56r64r
- ___copy_helper_block_e8_32w
- ___destroy_helper_block_e8_32s40r48r56r64r
- ___destroy_helper_block_e8_32w
- ___destructor_8_s0_s8_s16_s24
- ___markRegionsForMallocZones_block_invoke.445
- ___markRegionsForMallocZones_block_invoke.445.cold.1
- ___markRegionsForMallocZones_block_invoke.445.cold.2
- __block_literal_global.109
- __block_literal_global.115
- __block_literal_global.126
- __block_literal_global.160
- __block_literal_global.199
- __block_literal_global.219
- __block_literal_global.252
- __block_literal_global.277
- __block_literal_global.518
- __block_literal_global.617
- __compareBinaryImageDicts
- __listKernelCoreRegions_block_invoke.398
- __listKernelCoreRegions_block_invoke.403
- __markMachOLibraries_block_invoke.429
- __markMachOLibraries_block_invoke_2.430
- _addSpecialNodesFromTask.onceToken.124
- _bundleLock._bundleLock
- _bundleLock.onceToken
- _objc_msgSend$intersectsLocation:
CStrings:
+ "    Old region name was %!s(MISSING)\n"
+ "$_0::operator()"
+ "-[VMUTaskMemoryScanner _fixupBlockIsas]"
+ "-[VMUTaskMemoryScanner addRootNodesFromTaskWithError:]_block_invoke"
+ "ADMIN_REGION"
+ "ADMIN_REGION  PTR_IN_USE"
+ "ADMIN_REGION  PTR_REGION"
+ "ADMIN_REGION  PTR_REGION  PTR_IN_USE"
+ "ISSUE:  Region user_tag should already be set; setting to VM_MEMORY_MALLOC in %!s(MISSING) based on enumeration range for  %!s(MISSING)\n"
+ "PTR_IN_USE"
+ "PTR_REGION"
+ "PTR_REGION  PTR_IN_USE"
+ "Setting region name in %!s(MISSING) based on _zoneNames[_blocks[i].isa_index for  %!s(MISSING)\n"
+ "Setting region name in %!s(MISSING) based on _zoneNames[zone_index] for  %!s(MISSING)\n"
+ "Setting region name in %!s(MISSING) based on enumeration for  %!s(MISSING)\n"
+ "Setting region name in %!s(MISSING) based on enumeration range for  %!s(MISSING)\n"
+ "Setting region name in %!s(MISSING) based on malloc zone structure address for  %!s(MISSING)\n"
+ "Unexpected range type value %!x(MISSING) from malloc zone enumerator\n"
+ "__typed_operator_new_impl"
+ "_main_thread"
+ "_malloc_type"
+ "_malloc_type_"
+ "_malloc_zone"
+ "_outlined"
+ "_zone"
+ "markMallocAreas_block_invoke"
+ "swift_reflection_dumpInfoForInstance"
- "Active Block"
- "Administrative"
- "Block-containing"

```
