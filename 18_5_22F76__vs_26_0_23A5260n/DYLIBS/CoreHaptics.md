## CoreHaptics

> `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`

```diff

-250.501.0.0.0
-  __TEXT.__text: 0x535e8
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x2354
-  __TEXT.__const: 0x4c8
-  __TEXT.__gcc_except_tab: 0x96c8
-  __TEXT.__cstring: 0x6853
-  __TEXT.__oslogstring: 0x8901
-  __TEXT.__unwind_info: 0x1b30
-  __TEXT.__objc_classname: 0x3b4
-  __TEXT.__objc_methname: 0x4ed8
-  __TEXT.__objc_methtype: 0x2331
-  __TEXT.__objc_stubs: 0x4260
-  __DATA_CONST.__got: 0x228
+270.0.0.0.0
+  __TEXT.__text: 0x55238
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x23e4
+  __TEXT.__const: 0x568
+  __TEXT.__gcc_except_tab: 0x9970
+  __TEXT.__cstring: 0x68d4
+  __TEXT.__oslogstring: 0x8ac9
+  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__objc_classname: 0x3b8
+  __TEXT.__objc_methname: 0x4f71
+  __TEXT.__objc_methtype: 0x1c31
+  __TEXT.__objc_stubs: 0x4340
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1440
+  __DATA_CONST.__objc_selrefs: 0x1488
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x4a8
-  __AUTH_CONST.__cfstring: 0x2b40
-  __AUTH_CONST.__objc_const: 0x43b0
+  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__const: 0x5a8
+  __AUTH_CONST.__cfstring: 0x2b60
+  __AUTH_CONST.__objc_const: 0x44a0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x22c
-  __DATA.__data: 0x630
+  __DATA.__objc_ivar: 0x240
+  __DATA.__data: 0x640
   __DATA.__bss: 0x69
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libAudioStatistics.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 694E3E51-AFE8-39A1-AD2E-600601D9D41D
-  Functions: 980
-  Symbols:   3964
-  CStrings:  2838
+  UUID: B3B0D1A3-3C00-304E-AF15-DC325D51E085
+  Functions: 1038
+  Symbols:   4174
+  CStrings:  2867
 
Symbols:
+ -[AdvancedPatternPlayer .cxx_construct]
+ -[AdvancedPatternPlayer clearSeekOffset]
+ -[AdvancedPatternPlayer setVolume:]
+ -[AdvancedPatternPlayer volume]
+ -[CHHapticEngine createProcessTaskToken]
+ -[CHHapticEngine deallocateProcessTaskToken]
+ -[CHHapticEngine doUnregisterAllAudioResources]
+ -[CHHapticEngine intendedSpatialExperience]
+ -[CHHapticEngine setIntendedSpatialExperience:]
+ -[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]
+ -[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:].cold.1
+ -[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:].cold.2
+ -[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:error:]
+ -[HapticCommandConverter defaultEventParameterValueForParameter:eventType:]
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table161
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table78
+ _OBJC_CLASS_$_AVHapticProcessTaskToken
+ _OBJC_IVAR_$_AVHapticClient._configurationReplyWatchdogFactory
+ _OBJC_IVAR_$_AdvancedPatternPlayer._volume
+ _OBJC_IVAR_$_CHHapticEngine._intendedSpatialExperience
+ _OBJC_IVAR_$_CHHapticEngine._processTaskToken
+ _OBJC_IVAR_$_CHHapticEngine._processTaskTokenDict
+ _OBJC_IVAR_$_CHHapticEngine._storedOptions
+ __OBJC_$_PROP_LIST_CHHapticAdvancedPatternPlayerExtended
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CHHapticServerInterface
+ __ZGVZN16ResourceRegistry8instanceEvE9gRegistry
+ __ZN10applesauce3xpc4dict6createEv
+ __ZN10applesauce3xpceqERKNS0_6objectES3_
+ __ZN16ResourceRegistry18cleanUpRefCountKeyEPKv
+ __ZN16ResourceRegistry23decrementReferenceCountEmPKv
+ __ZN16ResourceRegistry31incrementReferenceCountNoCreateEmPKv
+ __ZN16ResourceRegistry5clearEv
+ __ZN16ResourceRegistry7emplaceEmNSt3__110shared_ptrI13AudioResourceEEP5NSURLP12NSDictionaryPKv
+ __ZN16ResourceRegistry8instanceEv
+ __ZN16ResourceRegistry8instanceEv.cold.1
+ __ZN5caulk3xpc22reply_watchdog_factory10make_timerEi
+ __ZN5caulk3xpc22reply_watchdog_factory18reply_with_timeoutIJmEEEU13block_pointerFvDpT_ES6_i
+ __ZN5caulk3xpc22reply_watchdog_factory5init2EiNSt3__18functionIFvvEEE
+ __ZN5caulk3xpc22reply_watchdog_factoryC1Ev
+ __ZNK10applesauce3xpc4dict3getEv
+ __ZNK10applesauce8dispatch2v16sourcedeEv
+ __ZNK16ResourceRegistry14findIdealMatchEP5NSURLP12NSDictionaryPKv
+ __ZNK16ResourceRegistry14findIdealMatchEP5NSURLP12NSDictionaryPKv.cold.1
+ __ZNK16ResourceRegistry20isResourceRegisteredEm
+ __ZNK16ResourceRegistry21isResourceLoopEnabledEm
+ __ZNK16ResourceRegistry22getDurationForResourceEm
+ __ZNK16ResourceRegistry5emptyEv
+ __ZNK5caulk12log_categorycvPU19objcproto9OS_os_log8NSObjectEv
+ __ZNKSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE7__cloneEv
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findIS3_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110__function12__value_funcIFbPKvEEC2B8ne200100EOS5_
+ __ZNSt3__110__function12__value_funcIFbPKvEEC2B8ne200100ERKS5_
+ __ZNSt3__110__function12__value_funcIFbPKvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFviEEC2B8ne200100EOS3_
+ __ZNSt3__110__function12__value_funcIFviEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFviEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvvEED2B8ne200100Ev
+ __ZNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEEclEv
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeImU8__strongP21AVHapticSequenceEntryEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEENS_22__unordered_map_hasherIS2_S6_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS6_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEENS_22__unordered_map_hasherIS2_S6_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE28__node_insert_unique_prepareB8ne200100EmRS6_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE14__erase_uniqueIS2_EEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS2_JRKNS_4pairIKS2_fEEEEENSG_INS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypefEENS_22__unordered_map_hasherIS2_S3_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S3_S8_S6_Lb1EEENS_9allocatorIS3_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE14__erase_uniqueIS3_EEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIS3_JNS_4pairIKS3_jEEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIS3_JRKNS_4pairIKS3_jEEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEEC2EOSF_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKvjEENS_22__unordered_map_hasherIS3_S4_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
+ __ZNSt3__112__hash_tableImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeImPvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEED2Ev
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3EEEEJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEC2B8ne200100IJLm0ELm1ELm2ELm3EEJS5_S8_SB_SO_EJEJEJRS5_RS8_RSB_RSO_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSW_IJDpT2_EEEDpOT3_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112construct_atB8ne200100IN18CASmartPreferences4PrefEJRPK10__CFStringS6_RNS_8functionIFbPKvEEEEPS2_EEPT_SF_DpOT0_
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_mapIPKvjNS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_jEEEEEC2ERKSC_
+ __ZNSt3__113unordered_mapIPKvjNS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_jEEEEEC2ESt16initializer_listISA_E
+ __ZNSt3__115allocate_sharedB8ne200100I13AudioResourceNS_9allocatorIS1_EEJRU8__strongP5NSURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISG_EENS_8equal_toISG_EENS1_INS_4pairIKSG_jEEEEEEEEEEEPvEEEEE7destroyB8ne200100INSL_IKmSQ_EEvLi0EEEvRSU_PT_
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI12AVFASoftLinkE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__shared_ptr_emplaceI13AudioResourceNS_9allocatorIS1_EEEC2B8ne200100IJRU8__strongP5NSURLES3_Li0EEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__invoke_void_return_wrapperIbLb0EE6__callB8ne200100IJRZN18CASmartPreferences10AddHandlerIiEEvPK10__CFStringS7_PFT_PKvRbENS_8functionIFvS8_EEEEUlSA_E_SA_EEEbDpOT_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN18CASmartPreferences4PrefEEEPS3_EEvRT_T0_S8_S8_
+ __ZNSt3__15tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISC_EENS_8equal_toISC_EENS_9allocatorINS_4pairIKSC_jEEEEEEEED2Ev
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE16__construct_nodeIJRmSP_EEENS_10unique_ptrINS_11__tree_nodeISQ_PvEENS_22__tree_node_destructorINSJ_IS12_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERS11_S11_
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE21__remove_node_pointerEPNS_11__tree_nodeISQ_PvEE
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE25__emplace_unique_key_argsImJRmSP_EEENSK_INS_15__tree_iteratorISQ_PNS_11__tree_nodeISQ_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE5eraseENS_21__tree_const_iteratorISQ_PNS_11__tree_nodeISQ_PvEElEE
+ __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP5NSURLU8__strongP12NSDictionaryNS_13unordered_mapIPKvjNS_4hashISE_EENS_8equal_toISE_EENS_9allocatorINS_4pairIKSE_jEEEEEEEEEEENS_19__map_value_compareImSQ_NS_4lessImEELb1EEENSJ_ISQ_EEE7destroyEPNS_11__tree_nodeISQ_PvEE
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI28AVHapticPlayerFixedParameterNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI28AVHapticPlayerFixedParameterNS_9allocatorIS1_EEE9push_backB8ne200100EOS1_
+ __ZNSt3__16vectorIN18CASmartPreferences4PrefENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB8ne200100IPmS5_EEvT_T0_m
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8ne200100ERKm
+ __ZNSt3__19allocatorI28AVHapticPlayerFixedParameterE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN18CASmartPreferences4PrefEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorImE17allocate_at_leastB8ne200100Em
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTINSt3__110__function6__baseIFvvEEE
+ __ZTINSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEEE
+ __ZTIZ24-[AVHapticClient doInit]E3$_0
+ __ZTSNSt3__110__function6__baseIFvvEEE
+ __ZTSNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEEE
+ __ZTSZ24-[AVHapticClient doInit]E3$_0
+ __ZTVNSt3__110__function6__funcIZ24-[AVHapticClient doInit]E3$_0NS_9allocatorIS2_EEFvvEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZZ25isMultiAudioOutputEnabledvE30gHapticAudioMultiOutputEnabled
+ __ZZ25isMultiAudioOutputEnabledvE4once
+ __ZZN16ResourceRegistry8instanceEvE9gRegistry
+ ___29-[CHHapticEngine finishInit:]_block_invoke.185
+ ___29-[CHHapticEngine finishInit:]_block_invoke.186
+ ___29-[CHHapticEngine finishInit:]_block_invoke.187
+ ___31-[CHHapticEngine handleFinish:]_block_invoke.191
+ ___31-[CHHapticEngine handleFinish:]_block_invoke.192
+ ___31-[CHHapticEngine handleFinish:]_block_invoke.193
+ ___31-[CHHapticEngine handleFinish:]_block_invoke.194
+ ___32-[CHHapticEngine beginIdleTimer]_block_invoke.189
+ ___32-[CHHapticEngine beginIdleTimer]_block_invoke.190
+ ___38-[CHHapticEngine doPlayPattern:error:]_block_invoke.246
+ ___39-[CHHapticEngine doStartEngineAndWait:]_block_invoke.226
+ ___44-[CHHapticEngine stopWithCompletionHandler:]_block_invoke.231
+ ___45-[CHHapticEngine startWithCompletionHandler:]_block_invoke.225
+ ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.229
+ ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.230
+ ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.221
+ ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.222
+ ___47-[CHHapticEngine doUnregisterAllAudioResources]_block_invoke
+ ___51-[AVHapticClient setupConnectionWithOptions:error:]_block_invoke.142
+ ___51-[AVHapticClient setupConnectionWithOptions:error:]_block_invoke_2.143
+ ___86-[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:error:]_block_invoke
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.485
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.490
+ ____Z25isMultiAudioOutputEnabledv_block_invoke
+ ____ZN5caulk3xpc22reply_watchdog_factory18reply_with_timeoutIJmEEEU13block_pointerFvDpT_ES6_i_block_invoke
+ ___block_descriptor_40_ea8_32r_e8_v16?0Q8lr32l8
+ ___block_descriptor_48_ea8_32c100_ZTSKZN5caulk3xpc22reply_watchdog_factory18reply_with_timeoutIJmEEEU13block_pointerFvDpT_ES6_iEUlmE__e8_v16?0Q8l
+ ___block_literal_global.216
+ ___block_literal_global.228
+ ___block_literal_global.353
+ ___block_literal_global.356
+ ___block_literal_global.69
+ ___copy_helper_block_ea8_32c100_ZTSKZN5caulk3xpc22reply_watchdog_factory18reply_with_timeoutIJmEEEU13block_pointerFvDpT_ES6_iEUlmE_
+ ___destroy_helper_block_ea8_32c100_ZTSKZN5caulk3xpc22reply_watchdog_factory18reply_with_timeoutIJmEEEU13block_pointerFvDpT_ES6_iEUlmE_
+ __xpc_type_dictionary
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_moveWeak
+ _objc_msgSend$clearSeekOffset
+ _objc_msgSend$createProcessTaskToken
+ _objc_msgSend$deallocateProcessTaskToken
+ _objc_msgSend$defaultEventParameterValueForParameter:eventType:
+ _objc_msgSend$defaultValue
+ _objc_msgSend$doRegisterAudioResource:options:fromPattern:error:
+ _objc_msgSend$doUnregisterAllAudioResources
+ _objc_msgSend$doUnregisterAudioResource:fromPattern:error:
+ _objc_msgSend$initWithXPCDictionary:
+ _objc_msgSend$setVolume:
+ _task_create_identity_token
+ _xpc_dictionary_create
+ _xpc_dictionary_set_mach_send
+ _xpc_equal
+ _xpc_get_type
+ _xpc_null_create
- +[CHHapticEngine lazyInitResourceMap]
- +[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]
- +[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:].cold.1
- +[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:].cold.2
- +[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:player:error:]
- -[AVHapticPlayer initWithSessionID:sessionIsShared:error:]
- GCC_except_table133
- GCC_except_table137
- GCC_except_table159
- GCC_except_table174
- GCC_except_table178
- GCC_except_table179
- GCC_except_table180
- GCC_except_table182
- GCC_except_table184
- GCC_except_table185
- GCC_except_table197
- GCC_except_table211
- GCC_except_table212
- GCC_except_table81
- _CFPreferencesGetAppIntegerValue
- _OBJC_IVAR_$_AVHapticClient._serverTimeout
- __ZL17_sResourceEntries
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__16vectorI28AVHapticPlayerFixedParameterNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN18CASmartPreferences4PrefENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt9type_infoeqB8ne190102ERKS_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110__function12__value_funcIFbPKvEEC2B8ne190102EOS5_
- __ZNSt3__110__function12__value_funcIFbPKvEEC2B8ne190102ERKS5_
- __ZNSt3__110__function12__value_funcIFbPKvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFviEEC2B8ne190102EOS3_
- __ZNSt3__110__function12__value_funcIFviEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFviEED2B8ne190102Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeImU8__strongP21AVHapticSequenceEntryEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKmNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEEEEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEENS_22__unordered_map_hasherIS2_S6_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS6_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI23AVHapticPlayerEventTypeU8__strongP8NSStringEENS_22__unordered_map_hasherIS2_S6_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE28__node_insert_unique_prepareB8ne190102EmRS6_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__115allocate_sharedB8ne190102I13AudioResourceNS_9allocatorIS1_EEJRU8__strongP5NSURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__117__call_once_paramINS_5tupleIJOZN12CADeprecated10TSingletonI12AVFASoftLinkE8instanceEvEUlvE_EEEE9__executeB8ne190102IJEEEvNS_15__tuple_indicesIJXspT_EEEE
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI12AVFASoftLinkE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI28AVHapticPlayerFixedParameterEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18CASmartPreferences4PrefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__shared_ptr_emplaceI13AudioResourceNS_9allocatorIS1_EEEC2B8ne190102IJRU8__strongP5NSURLES3_Li0EEES3_DpOT_
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__invoke_void_return_wrapperIbLb0EE6__callB8ne190102IJRZN18CASmartPreferences10AddHandlerIiEEvPK10__CFStringS7_PFT_PKvRbENS_8functionIFvS8_EEEEUlSA_E_SA_EEEbDpOT_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN18CASmartPreferences4PrefEEES3_EEvRT_PT0_S8_S8_
- __ZNSt3__15tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEED1Ev
- __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEEEEENS_19__map_value_compareImSA_NS_4lessImEELb1EEENS_9allocatorISA_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSM_SM_
- __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEEEEENS_19__map_value_compareImSA_NS_4lessImEELb1EEENS_9allocatorISA_EEE21__remove_node_pointerEPNS_11__tree_nodeISA_PvEE
- __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEEEEENS_19__map_value_compareImSA_NS_4lessImEELb1EEENS_9allocatorISA_EEE25__emplace_unique_key_argsImJRmS9_EEENS_4pairINS_15__tree_iteratorISA_PNS_11__tree_nodeISA_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeImNS_5tupleIJNS_10shared_ptrI13AudioResourceEEU8__strongP12NSDictionaryjEEEEENS_19__map_value_compareImSA_NS_4lessImEELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeISA_PvEE
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB8ne190102IPmS5_EEvT_T0_m
- __ZNSt3__19allocatorIN18CASmartPreferences4PrefEE9constructB8ne190102IS2_JRPK10__CFStringS8_RNS_8functionIFbPKvEEEEEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___29-[CHHapticEngine finishInit:]_block_invoke.181
- ___29-[CHHapticEngine finishInit:]_block_invoke.182
- ___29-[CHHapticEngine finishInit:]_block_invoke.183
- ___31-[CHHapticEngine handleFinish:]_block_invoke.187
- ___31-[CHHapticEngine handleFinish:]_block_invoke.188
- ___31-[CHHapticEngine handleFinish:]_block_invoke.189
- ___31-[CHHapticEngine handleFinish:]_block_invoke.190
- ___32-[CHHapticEngine beginIdleTimer]_block_invoke.185
- ___32-[CHHapticEngine beginIdleTimer]_block_invoke.186
- ___38-[CHHapticEngine doPlayPattern:error:]_block_invoke.235
- ___44-[CHHapticEngine stopWithCompletionHandler:]_block_invoke.220
- ___45-[CHHapticEngine startWithCompletionHandler:]_block_invoke.217
- ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.218
- ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.219
- ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.213
- ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.214
- ___51-[AVHapticClient setupConnectionWithOptions:error:]_block_invoke.144
- ___51-[AVHapticClient setupConnectionWithOptions:error:]_block_invoke_2.145
- ___93+[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:player:error:]_block_invoke
- ___99+[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]_block_invoke
- ___99+[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]_block_invoke.461
- ___99+[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]_block_invoke.466
- ___block_descriptor_48_ea8_32s40r_e8_v16?0Q8lr40l8s32l8
- ___block_literal_global.208
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.65
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$doRegisterAudioResource:options:fromPattern:player:error:
- _objc_msgSend$doUnregisterAudioResource:fromPattern:player:error:
- _objc_msgSend$lazyInitResourceMap
CStrings:
+ "%25s:%-5d %s: -- Entry list has '%@' with ID %u"
+ "%25s:%-5d %s: ERROR creating identify token with error %d. Resource memory usage will be billed to server"
+ "%25s:%-5d %s: ERROR: async stop after timeout failed with error %@"
+ "%25s:%-5d %s: Error setting player %p audio and haptics volume to %.3f: %@"
+ "%25s:%-5d %s: Initial XPC call to server timed out. Invalidating connection to prevent hang"
+ "%25s:%-5d %s: Setting player %p audio and haptics volume to %.3f. Server will clamp volume argument to [0, 1]"
+ "%25s:%-5d %s: Warning: engine start timed out but server side may be running, triggering async stop"
+ "%25s:%-5d %s: fixed param[%u]: source value: %.2f, immediateParameter value: %.2f, result value: %.2f (%s)"
+ "%25s:%-5d %s: releasing resource ID %u from engine dealloc"
+ "%25s:%-5d ASSERTION FAILURE [(resourceEntries.emplace(copiedResourceID, resource, resource->url(), options, refCountKey) == true) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(resourceEntries.emplace(resourceID, resource, resource->url(), options, refCountKey) == true) != 0 is false]: "
+ "-[AdvancedPatternPlayer setVolume:]"
+ "-[CHHapticEngine createProcessTaskToken]"
+ "-[CHHapticEngine doUnregisterAllAudioResources]"
+ "-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]"
+ "-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke"
+ "-[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:error:]"
+ "@\"CASpatialAudioExperience\""
+ "B48@0:8Q16{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}24"
+ "ClientProcessTaskToken"
+ "Failed to recreate HapticServerConfig"
+ "Q44@0:8@16@24B32^@36"
+ "T@\"CASpatialAudioExperience\",C,V_intendedSpatialExperience"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticContinuousNonsustainedIDs"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticContinuousSustainedIDs"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},R,V_hapticTransientIDs"
+ "XPC_ProcessTaskToken"
+ "_configurationReplyWatchdogFactory"
+ "_intendedSpatialExperience"
+ "_processTaskToken"
+ "_processTaskTokenDict"
+ "_storedOptions"
+ "_volume"
+ "additive"
+ "clearSeekOffset"
+ "createProcessTaskToken"
+ "deallocateProcessTaskToken"
+ "defaultEventParameterValueForParameter:eventType:"
+ "doRegisterAudioResource:options:fromPattern:error:"
+ "doUnregisterAllAudioResources"
+ "doUnregisterAudioResource:fromPattern:error:"
+ "haptic_audio_multi_output"
+ "initWithXPCDictionary:"
+ "intendedSpatialExperience"
+ "multiplicative"
+ "operator()"
+ "setIntendedSpatialExperience:"
+ "setIntendedSpatialExperience:reply:"
+ "setVolume:"
+ "v32@0:8@\"CASpatialAudioExperience\"16@?<v@?@\"NSError\">24"
+ "volume"
+ "{dict=\"fObj\"{object=\"fObj\"@\"NSObject<OS_xpc_object>\"}}"
+ "{map<unsigned long, AVHapticSequenceEntry *, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, AVHapticSequenceEntry *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<unsigned long, std::pair<NSURL *, NSDictionary *>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}"
+ "{reply_watchdog_factory=\"mDebugging\"B\"mDefaultTimeoutMS\"i\"mTimeoutHandler\"{function<void ()>=\"__f_\"{__value_func<void ()>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}}"
+ "{unordered_map<AVHapticPlayerEventType, NSString *, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::__unordered_map_hasher<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>, std::__unordered_map_equal<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>, std::allocator<std::__hash_value_type<AVHapticPlayerEventType, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16@0:8"
- "%25s:%-5d %s: -- Entry list has '%@' with ID %u, and count %u"
- "%25s:%-5d %s: Creating resource map on first use"
- "%25s:%-5d %s: Initial XPC call to server timed out"
- "%25s:%-5d %s: fixed param[%u]: source value: %.2f, immediateParameter value: %.2f, result value: %.2f"
- "%25s:%-5d %s: initWithInternalSessionID entered"
- "%25s:%-5d ASSERTION FAILURE [(_sResourceEntries->emplace(copiedResourceID, ResourceEntry(resource, options, 1)).second == true) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_sResourceEntries->emplace(resourceID, ResourceEntry(resource, options, 1)).second == true) != 0 is false]: "
- "+[CHHapticEngine lazyInitResourceMap]"
- "+[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]"
- "+[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:player:error:]_block_invoke"
- "+[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:player:error:]"
- "-[AVHapticPlayer initWithSessionID:sessionIsShared:error:]"
- "@32@0:8I16B20^@24"
- "B44@0:8Q16B24@28^@36"
- "B48@0:8Q16{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}24"
- "Q52@0:8@16@24B32@36^@44"
- "Td,V_seekOffset"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}},R,V_hapticContinuousNonsustainedIDs"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}},R,V_hapticContinuousSustainedIDs"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}},R,V_hapticTransientIDs"
- "_serverTimeout"
- "doRegisterAudioResource:options:fromPattern:player:error:"
- "doUnregisterAudioResource:fromPattern:player:error:"
- "hapticserver_timeout"
- "initWithSessionID:sessionIsShared:error:"
- "lazyInitResourceMap"
- "{map<unsigned long, AVHapticSequenceEntry *, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, AVHapticSequenceEntry *>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned long, AVHapticSequenceEntry *>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>>=\"__value_\"Q}}}"
- "{map<unsigned long, std::pair<NSURL *, NSDictionary *>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>>=\"__value_\"Q}}}"
- "{unordered_map<AVHapticPlayerEventType, NSString *, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::__unordered_map_hasher<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>, std::__unordered_map_equal<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>, std::allocator<std::__hash_value_type<AVHapticPlayerEventType, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<AVHapticPlayerEventType, std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>>=\"__value_\"f}}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}16@0:8"

```
