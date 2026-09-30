## libmecab.dylib

> `/usr/lib/libmecab.dylib`

```diff

-  __TEXT.__text: 0x52d18
+  __TEXT.__text: 0x52818
   __TEXT.__const: 0x1548
   __TEXT.__cstring: 0x7a34
-  __TEXT.__gcc_except_tab: 0x2f40
+  __TEXT.__gcc_except_tab: 0x2f3c
   __TEXT.__unwind_info: 0x11c0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb98
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Functions:
~ __ZN5MeCab19DictionaryGenerator6gencidEPKcPNS_18DictionaryRewriterEPNS_9ContextIDE : 1880 -> 1848
~ __ZN5MeCab19DictionaryGenerator6gendicEPKcS2_RKNS_12CharPropertyEPNS_18DictionaryRewriterERKNS_9ContextIDEPNS_19DecoderFeatureIndexEbi : 3748 -> 3736
~ __ZN5MeCab11tokenizeCSVINSt3__120back_insert_iteratorINS1_6vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS7_IS9_EEEEEEEEmPcT_m : 464 -> 452
~ __ZNK5MeCab12RewriteRules7rewriteEmPPKcPNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE : 1928 -> 1920
~ __ZNK5MeCab18DictionaryRewriter7rewriteERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPS7_SA_SA_ : 1136 -> 1124
~ __ZNK5MeCab14POSIDGenerator2idEPKc : 1068 -> 1056
~ _mecab_test_gen : 2516 -> 2508
~ __ZN5MeCab4Eval4readEPNSt3__113basic_istreamIcNS1_11char_traitsIcEEEEPNS1_6vectorINS7_INS1_12basic_stringIcS4_NS1_9allocatorIcEEEENS9_ISB_EEEENS9_ISD_EEEERKNS7_IiNS9_IiEEEE : 1788 -> 1768
~ __ZN5MeCab13ChunkFreeListIcE5allocEm : 272 -> 276
~ __ZN5MeCab12FeatureIndex19buildUnigramFeatureEP20mecab_learner_path_tPKc : 1804 -> 1780
~ __ZN5MeCab12FeatureIndex18buildBigramFeatureEP20mecab_learner_path_tPKcS4_ : 2156 -> 2136
~ __ZN5MeCab13ChunkFreeListIiE5allocEm : 284 -> 288
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIydEELb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 3804 -> 3772
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIydEEEEbT1_S8_T0_ : 1128 -> 1088
~ __ZN5MeCab12CharProperty7compileEPKcS2_S2_ : 8500 -> 8488
~ __ZN5MeCab5LBFGS14lbfgs_optimizeEiiPddPKdS1_S1_bdPi : 3172 -> 3112
~ __ZN5MeCab12_GLOBAL__N_110CRFLearner3runEPNS_5ParamE : 9968 -> 9948
~ __ZNSt3__16vectorIN5MeCab12_GLOBAL__N_114learner_threadENS_9allocatorIS3_EEED1B9nqe220106Ev : 128 -> 120
~ __ZN5MeCab20EncoderLearnerTagger4readEPNSt3__113basic_istreamIcNS1_11char_traitsIcEEEEPNS1_6vectorIdNS1_9allocatorIdEEEE : 3172 -> 3148
~ __ZN5MeCab10Dictionary25assignUserDictionaryCostsERKNS_5ParamERKNSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEEPKc : 6204 -> 6192
~ __ZN5MeCab10Dictionary7compileERKNS_5ParamERKNSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEEPKcRKNS_14CompileOptionsE : 17520 -> 17312
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN5MeCab10Dictionary7compileERKNS2_5ParamERKNS_6vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSB_ISD_EEEEPKcRKNS2_14CompileOptionsEE3$_0NS_11__wrap_iterIPNS_4pairISD_P13mecab_token_tEEEEEEvT1_SW_T0_NS_15iterator_traitsISW_E15difference_typeEPNSZ_10value_typeEl : 1104 -> 1012
~ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERZN5MeCab10Dictionary7compileERKNS2_5ParamERKNS_6vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSB_ISD_EEEEPKcRKNS2_14CompileOptionsEE3$_0NS_11__wrap_iterIPNS_4pairISD_P13mecab_token_tEEEEEEvT1_SW_T0_NS_15iterator_traitsISW_E15difference_typeEPNSZ_10value_typeE : 984 -> 964
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZN5MeCab10Dictionary7compileERKNS2_5ParamERKNS_6vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSB_ISD_EEEEPKcRKNS2_14CompileOptionsEE3$_0NS_11__wrap_iterIPNS_4pairISD_P13mecab_token_tEEEEEEvT1_SW_SW_OT0_NS_15iterator_traitsISW_E15difference_typeES11_PNS10_10value_typeEl : 1532 -> 1476
~ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB9nqe220106IPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEP13mecab_token_tEESE_SE_EENS4_IT_T1_EESF_T0_SG_ : 152 -> 132
~ __ZN5MeCab5Param4openEiPPcPKNS_6OptionE : 2600 -> 2644
~ __ZN5MeCab5Param4openEPKcPKNS_6OptionE : 716 -> 708
~ __ZN5MeCab11LatticeImpl10set_resultEPKc : 1852 -> 1844
~ __ZN5MeCab7Viterbi11initPartialEPNS_7LatticeE : 1944 -> 1936
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEPNSH_10value_typeEl : 1036 -> 944
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEEEvT1_SE_SE_OT0_NS_15iterator_traitsISE_E15difference_typeESJ_PNSI_10value_typeEl : 1604 -> 1548
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe220106EPKvm : 1096 -> 1084
~ __ZNK5MeCab9TokenizerI12mecab_node_t12mecab_path_tE6lookupILb1EEEPS1_PKcS7_PNS_9AllocatorIS1_S2_EEPNS_7LatticeE : 2772 -> 2776
~ __ZN5MeCab12_GLOBAL__N_113is_valid_nodeI12mecab_node_tEEbPKNS_7LatticeEPT_ : 1576 -> 1552
~ __ZN5MeCab10Dictionary17compressedFeatureERK13mecab_token_tPKDsPDsm : 216 -> 208
~ __ZNK5MeCab10Dictionary11copyFeatureEPK12mecab_node_tPDsm : 172 -> 156
~ __ZN5MeCab9TokenizerI12mecab_node_t12mecab_path_tE4openERKNS_5ParamE : 3828 -> 3832
~ __ZN5MeCab9TokenizerI20mecab_learner_node_t20mecab_learner_path_tE4openERKNS_5ParamE : 3828 -> 3832
~ __ZNK5MeCab6Writer9writeNodeEPNS_7LatticeEPKcPK12mecab_node_tPNS_12StringBufferE : 3940 -> 3872
~ __ZN5MeCab12StringBufferlsEt : 200 -> 192
~ __ZN5MeCab12StringBufferlsEi : 224 -> 212
~ __ZNK6marisa8grimoire4trie9LoudsTrie14reverse_lookupERNS_5AgentE : 544 -> 512
~ __ZN6marisa8grimoire4trie9LoudsTrie10build_trieINS1_3KeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : 496 -> 484
~ __ZN6marisa8grimoire4trie9LoudsTrie10build_trieINS1_10ReverseKeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : 496 -> 484
~ __ZNSt3__15dequeIN6marisa8grimoire4trie5RangeENS_9allocatorIS4_EEE19__add_back_capacityEv : 480 -> 468
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERNS_7greaterIN6marisa8grimoire4trie13WeightedRangeEEEPS6_EEvT1_SA_T0_ : 184 -> 168
~ __ZNSt3__124__buffered_inplace_mergeB9nqe220106INS_17_ClassicAlgPolicyERNS_7greaterIN6marisa8grimoire4trie13WeightedRangeEEEPS6_EEvT1_SA_SA_OT0_NS_15iterator_traitsISA_E15difference_typeESF_PNSE_10value_typeE : 260 -> 252
~ __ZNSt3__122__rotate_random_accessB9nqe220106INS_17_ClassicAlgPolicyEPN6marisa8grimoire4trie13WeightedRangeES6_EET0_S7_S7_T1_ : 256 -> 216
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIjjEEEEvT1_S8_T0_ : 220 -> 192
~ __ZNSt3__126__insertion_sort_unguardedB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIjjEEEEvT1_S8_T0_ : 172 -> 140
~ __ZNSt3__132__partition_with_equals_on_rightB9nqe220106INS_17_ClassicAlgPolicyEPNS_4pairIjjEERNS_6__lessIvvEEEENS2_IT0_bEES8_S8_T1_ : 412 -> 400
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIjjEEEEbT1_S8_T0_ : 684 -> 640
~ __ZNK6marisa8grimoire4trie4Tail7restoreERNS_5AgentEm : 152 -> 140
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/include/marisa/scoped-ptr.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:21: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:106: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:107: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:70: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:78: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:79: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:130: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:148: MARISA_IO_ERROR: size_written <= 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:153: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:154: MARISA_IO_ERROR: ::fflush(file_) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:160: MARISA_IO_ERROR: !stream_->write(static_cast<const char *>(data), size)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:162: MARISA_IO_ERROR: std::ios_base::failure"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:79: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:32: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:34: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:32: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:235: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:37: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:40: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/char_property.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/connector.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/context_id.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/dictionary.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/dictionary_compiler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/dictionary_generator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/dictionary_rewriter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/eval.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/feature_index.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/learner.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/learner_tagger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/mmap.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/param.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/quantized_connector.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/tagger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/tokenizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/viterbi.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gzY0Ce/Sources/Mecabra/src/writer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/char_property.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/connector.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/context_id.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/dictionary.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/dictionary_compiler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/dictionary_generator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/dictionary_rewriter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/eval.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/feature_index.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/learner.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/learner_tagger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/mmap.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/param.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/quantized_connector.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/tagger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/tokenizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/viterbi.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JCWZUG/Sources/Mecabra/src/writer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/include/marisa/scoped-ptr.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/agent.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/agent.cc:21: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:106: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:107: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:70: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:78: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:79: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:130: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:148: MARISA_IO_ERROR: size_written <= 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:153: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:154: MARISA_IO_ERROR: ::fflush(file_) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:160: MARISA_IO_ERROR: !stream_->write(static_cast<const char *>(data), size)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:162: MARISA_IO_ERROR: std::ios_base::failure"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:79: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:32: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:34: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:32: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/trie.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/trie.cc:235: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/trie.cc:37: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kOcnTc/Sources/Marisa/lib/marisa/trie.cc:40: MARISA_MEMORY_ERROR: temp.get() == NULL"

```
