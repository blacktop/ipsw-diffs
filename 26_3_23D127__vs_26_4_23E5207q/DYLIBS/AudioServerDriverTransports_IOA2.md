## AudioServerDriverTransports_IOA2

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`

```diff

-320.3.0.0.0
-  __TEXT.__text: 0x1ea1c
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x11a4
-  __TEXT.__gcc_except_tab: 0x40f8
+340.16.0.0.0
+  __TEXT.__text: 0x1fc04
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x11fc
+  __TEXT.__gcc_except_tab: 0x4254
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0xe1b
-  __TEXT.__oslogstring: 0x18a9
-  __TEXT.__unwind_info: 0x11c8
-  __TEXT.__objc_classname: 0x218
-  __TEXT.__objc_methname: 0x28bf
-  __TEXT.__objc_methtype: 0x1064
-  __TEXT.__objc_stubs: 0x2260
+  __TEXT.__cstring: 0xfb7
+  __TEXT.__oslogstring: 0x18f9
+  __TEXT.__unwind_info: 0x1240
+  __TEXT.__objc_classname: 0x219
+  __TEXT.__objc_methname: 0x2a79
+  __TEXT.__objc_methtype: 0x105c
+  __TEXT.__objc_stubs: 0x2400
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe0
+  __DATA_CONST.__objc_selrefs: 0xc48
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0xf8
-  __AUTH_CONST.__cfstring: 0xbe0
-  __AUTH_CONST.__objc_const: 0x1bd0
+  __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__objc_const: 0x1c30
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AD5B007-D2AA-3474-8D78-C21DDF2343F4
-  Functions: 677
-  Symbols:   2354
-  CStrings:  1027
+  UUID: C88650B2-C82A-3DC2-89AE-AA214EF58658
+  Functions: 693
+  Symbols:   2441
+  CStrings:  1052
 
Symbols:
+ -[ASDTIOA2Device exclavesOutputBufferName]
+ -[ASDTIOA2Device isolatedOutputUseCaseID]
+ -[ASDTIOA2Device setExclavesOutputBufferName:]
+ -[ASDTIOA2Device setIsolatedOutputUseCaseID:]
+ -[ASDTIOA2Stream processIsolatedOutputMix]
+ -[NSDictionary(ASDTIOA2Config) asdtExclavesOutputBufferName]
+ -[NSDictionary(ASDTIOA2Config) asdtIsolatedOutputUseCaseID]
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table213
+ GCC_except_table215
+ _OBJC_IVAR_$_ASDTIOA2Device._exclavesOutputBufferName
+ _OBJC_IVAR_$_ASDTIOA2Device._isolatedOutputUseCaseID
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.1
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.2
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.3
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.4
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.5
+ __ZL27FillBasicFormatInfoFromDictRKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.6
+ __ZN10applesauce2CF10convert_toIjLi0EEET_PK10__CFNumber.cold.1
+ __ZN10applesauce2CF14make_StringRefEPK10__CFStringz.cold.1
+ __ZN10applesauce2CF19DictionaryRef_proxyC1ERKNS0_13DictionaryRefE.cold.1
+ __ZN10applesauce2CF7details15make_CFArrayRefIPKvEEDaRKNSt3__16vectorIT_NS6_9allocatorIS8_EEEENS1_10raw_cf_tagE.cold.1
+ __ZN10applesauce2CF7details5at_toINS0_7TypeRefEEET_PK9__CFArraymNS1_17applesauce_cf_tagE.cold.1
+ __ZN4ASDT14IOA2UserClient20GetControlInfo_ValueERKN10applesauce2CF13DictionaryRefERj.cold.1
+ __ZN4ASDT14IOA2UserClient21MapBlockControlBufferERKN10applesauce2CF13DictionaryRefE.cold.4
+ __ZN4ASDT14IOA2UserClient25GetControlInfo_IsReadOnlyERKN10applesauce2CF13DictionaryRefE.cold.1
+ __ZN4ASDT14IOA2UserClient27ConstructASBDFromDictionaryERKN10applesauce2CF13DictionaryRefER27AudioStreamBasicDescription.cold.1
+ __ZN4ASDT14IOA2UserClient27ConstructASRDFromDictionaryERKN10applesauce2CF13DictionaryRefER28AudioStreamRangedDescription.cold.1
+ __ZN4ASDT14IOA2UserClient27ConstructASRDFromDictionaryERKN10applesauce2CF13DictionaryRefER28AudioStreamRangedDescription.cold.2
+ __ZN4ASDT14IOA2UserClient28GetStreamInfo_UsesIsolatedIOERKN10applesauce2CF13DictionaryRefE.cold.1
+ __ZN4ASDT8Exclaves13InboundBuffer5WriteEPKhjj
+ __ZN4ASDT8Exclaves13InboundBuffer5WriteEPKhjjjy
+ __ZNK10applesauce2CF7TypeRefcvNS0_13DictionaryRefEEv.cold.1
+ __ZNK4ASDT21StreamFormatConverter13convertBufferEjPKvPjPv
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EclB9foe210106Ev
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B9foe210106Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEE4lockB9foe210106Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEE6unlockB9foe210106Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B9foe210106Ev
+ __ZNSt3__111unique_lockINS_5mutexEE6unlockB9foe210106Ev
+ __ZNSt3__112__destroy_atB9foe210106IN10applesauce2CF9NumberRefELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__114__split_bufferIN10applesauce2CF11TypeRefPairERNS_9allocatorIS3_EEE17__destruct_at_endB9foe210106EPS3_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB9foe210106IS4_Li0EEEvRS5_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB9foe210106IS4_JRKNS3_9StringRefERKNS3_7TypeRefEELi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF9NumberRefEEEE9constructB9foe210106IS4_JjELi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__118condition_variable10wait_untilB9foe210106INS_6chrono12system_clockENS2_8durationIdNS_5ratioILl1ELl1000000EEEEEEENS_9cv_statusERNS_11unique_lockINS_5mutexEEERKNS2_10time_pointIT_T0_EE
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe210106Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__122condition_variable_any10wait_untilB9foe210106INS_11unique_lockINS_12shared_mutexEEENS_6chrono12system_clockENS5_8durationIdNS_5ratioILl1ELl1000000EEEEEEENS_9cv_statusERT_RKNS5_10time_pointIT0_T1_EE
+ __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS5_EEED2B9foe210106Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__134__uninitialized_allocator_relocateB9foe210106INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B9foe210106IS3_NS2_9NumberRefELi0EEEOT_OT0_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_NS_4pairIKS4_S5_EENS_4lessIS4_EELb1EEENS_9allocatorISA_EEE12__find_equalIS4_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISL_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_NS_4pairIKS4_S5_EENS_4lessIS4_EELb1EEENS_9allocatorISA_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSL_SL_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_NS_4pairIKS4_S5_EENS_4lessIS4_EELb1EEENS_9allocatorISA_EEE25__emplace_unique_key_argsIS4_JS4_NS3_9NumberRefEEEENS8_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_NS_4pairIKS4_S5_EENS_4lessIS4_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIN4ASDT8RawPointENS2_7DBPointEEENS_19__map_value_compareIS3_NS_4pairIKS3_S4_EENS_4lessIS3_EELb1EEENS_9allocatorIS9_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE22__base_destruct_at_endB9foe210106EPS3_
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B9foe210106Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9foe210106Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B9foe210106EmRKc
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9foe210106IPKjS6_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB9foe210106IPjS5_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B9foe210106Em
+ __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB9foe210106Em
+ __ZNSt3__19allocatorIN10applesauce2CF9NumberRefEE17allocate_at_leastB9foe210106Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB9foe210106Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB9foe210106Em
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___42-[ASDTIOA2Stream processIsolatedOutputMix]_block_invoke
+ ___42-[ASDTIOA2Stream processIsolatedOutputMix]_block_invoke.cold.1
+ ___42-[ASDTIOA2Stream processIsolatedOutputMix]_block_invoke.cold.2
+ ___block_descriptor_93_ea8_32s_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36ls32l8
+ _kASDTIOA2ConfigKeyExclavesOutputBufferName
+ _kASDTIOA2ConfigKeyIsolatedOutputUseCaseID
+ _objc_msgSend$asdtExclavesOutputBufferName
+ _objc_msgSend$asdtIsolatedOutputUseCaseID
+ _objc_msgSend$exclavesInboundBuffer
+ _objc_msgSend$exclavesOutputBufferName
+ _objc_msgSend$ioBufferSize
+ _objc_msgSend$isLinearBuffer
+ _objc_msgSend$isolatedOutputUseCaseID
+ _objc_msgSend$setExclavesOutputBufferName:
+ _objc_msgSend$setIsLinearBuffer:
+ _objc_msgSend$setIsolatedOutputUseCaseID:
+ _objc_msgSend$setUsesVirtualFormatForIO:
+ _objc_msgSend$streamFormatConverter
+ _objc_msgSend$usesVirtualFormatForIO
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- GCC_except_table147
- GCC_except_table150
- GCC_except_table153
- GCC_except_table154
- GCC_except_table159
- GCC_except_table163
- GCC_except_table168
- GCC_except_table173
- GCC_except_table177
- GCC_except_table182
- GCC_except_table187
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table200
- GCC_except_table202
- GCC_except_table205
- GCC_except_table210
- GCC_except_table214
- GCC_except_table218
- __ZN10applesauce2CF13DictionaryRefD2Ev
- __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED2Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EclB8ne200100Ev
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne200100Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEE4lockB8ne200100Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEE6unlockB8ne200100Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne200100Ev
- __ZNSt3__111unique_lockINS_5mutexEE6unlockB8ne200100Ev
- __ZNSt3__112__destroy_atB8ne200100IN10applesauce2CF9NumberRefELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__114__split_bufferIN10applesauce2CF11TypeRefPairERNS_9allocatorIS3_EEE17__destruct_at_endB8ne200100EPS3_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB8ne200100IS4_vLi0EEEvRS5_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB8ne200100IS4_JRKNS3_9StringRefERKNS3_7TypeRefEEvLi0EEEvRS5_PT_DpOT0_
- __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF9NumberRefEEEE9constructB8ne200100IS4_JjEvLi0EEEvRS5_PT_DpOT0_
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__122condition_variable_any10wait_untilINS_11unique_lockINS_12shared_mutexEEENS_6chrono12system_clockENS5_8durationIdNS_5ratioILl1ELl1000000EEEEEEENS_9cv_statusERT_RKNS5_10time_pointIT0_T1_EE
- __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS5_EEED2B8ne200100Ev
- __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne200100IS3_NS2_9NumberRefELi0EEEOT_OT0_
- __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE12__find_equalIS4_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISI_EERKT_
- __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSI_SI_
- __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS4_JS4_NS3_9NumberRefEEEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__16__treeINS_12__value_typeIN4ASDT8RawPointENS2_7DBPointEEENS_19__map_value_compareIS3_S5_NS_4lessIS3_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tree_nodeIS5_PvEE
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE22__base_destruct_at_endB8ne200100EPS3_
- __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne200100Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100EmRKc
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100IPKjS6_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100IPjS5_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B8ne200100Em
- __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB8ne200100Em
- __ZNSt3__19allocatorIN10applesauce2CF9NumberRefEE17allocate_at_leastB8ne200100Em
- __ZNSt3__19allocatorIPKvE17allocate_at_leastB8ne200100Em
- __ZNSt3__19allocatorIjE17allocate_at_leastB8ne200100Em
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "%@:%@: processIsolatedOutputMix Failed: %c%c%c%c"
+ "%@:%@: unexpected direction=%u"
+ "-[ASDTIOA2Stream processIsolatedOutputMix]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CHoMugBbg4KqwR4rOavVYWtBq_ec054DL1ybVx4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "ExclavesOutputBufferName"
+ "IsolatedOutputUseCaseID"
+ "T@\"NSString\",&,N,V_exclavesOutputBufferName"
+ "TQ,N,V_isolatedOutputUseCaseID"
+ "_exclavesOutputBufferName"
+ "_isolatedOutputUseCaseID"
+ "asdtExclavesOutputBufferName"
+ "asdtIsolatedOutputUseCaseID"
+ "exclavesInboundBuffer"
+ "exclavesOutputBufferName"
+ "isLinearBuffer"
+ "isolatedOutputUseCaseID"
+ "processIsolatedOutputMix"
+ "setExclavesOutputBufferName:"
+ "setIsLinearBuffer:"
+ "setIsolatedOutputUseCaseID:"
+ "setUsesVirtualFormatForIO:"
+ "streamFormatConverter"
+ "usesVirtualFormatForIO"
+ "{VolumeCurve=\"mTag\"I\"mCurveMap\"{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=\"__tree_\"{__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::pair<const ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"mIsApplyingTransferFunction\"B\"mTransferFunction\"I\"mRawToScalarExponentNumerator\"f\"mRawToScalarExponentDenominator\"f}"
+ "{VolumeCurve=I{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>={__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::pair<const ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}BIff}24@0:8@16"
- "{VolumeCurve=\"mTag\"I\"mCurveMap\"{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=\"__tree_\"{__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"mIsApplyingTransferFunction\"B\"mTransferFunction\"I\"mRawToScalarExponentNumerator\"f\"mRawToScalarExponentDenominator\"f}"
- "{VolumeCurve=I{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>={__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}BIff}24@0:8@16"

```
