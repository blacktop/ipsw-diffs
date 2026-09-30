## CoreNLP

> `/System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP`

```diff

-  __TEXT.__text: 0xf7e44
+  __TEXT.__text: 0xf782c
   __TEXT.__objc_methlist: 0x1b8
   __TEXT.__const: 0x35e0
   __TEXT.__gcc_except_tab: 0xf7f8

   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0xd28
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x2f8
+  __AUTH.__data: 0x2d8
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0x10
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x8bc
-  __DATA.__bss: 0x521
+  __DATA.__data: 0x87c
+  __DATA.__bss: 0x499
   __DATA.__common: 0x3c5
-  __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__data: 0x220
+  __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__thread_vars : content changed
Functions:
~ __ZN7CoreNLP19quoteStatusForTokenEPK10__CFString7CFRangePNS_17NLAttributedTokenEPi : 640 -> 644
~ __ZN7CoreNLP18WordDispatchTagger31enumeratePossibleTokenSequencesEU13block_pointerFvPbE : 272 -> 260
~ __ZN7CoreNLP13BERTEmbedding16fillTokenVectorsEPK9__CFArraymjPfPKfS6_ : 1424 -> 1420
~ __ZN6corelm13NeuralNetwork18releaseInputTensorEv : 272 -> 256
~ __ZN7CoreNLP15CompositeTagger36copyTagAndProbabilityForCurrentTokenEPK10__CFString : 812 -> 804
~ __ZN7CoreNLP8CRFModel5trainEP7__sFILE : 860 -> 840
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERPFbRK20NLLanguageHypothesisS4_EPS2_EEvT1_S9_T0_ : 244 -> 224
~ __ZNSt3__126__insertion_sort_unguardedB9nqe220106INS_17_ClassicAlgPolicyERPFbRK20NLLanguageHypothesisS4_EPS2_EEvT1_S9_T0_ : 192 -> 184
~ __ZNSt3__132__partition_with_equals_on_rightB9nqe220106INS_17_ClassicAlgPolicyEP20NLLanguageHypothesisRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_ : 304 -> 308
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERPFbRK20NLLanguageHypothesisS4_EPS2_EEbT1_S9_T0_ : 936 -> 916
~ __ZN7CoreNLP14ModelContainerC2EPK9__CFArray : 1096 -> 1084
~ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofB9nqe220106EPKcm : 144 -> 140
~ _NLTaggerTrainModel : 6792 -> 6756
~ __ZN7CoreNLP8CNNModel13initInferenceEv : 272 -> 260
~ __ZN10applesauce2CF7details15make_CFArrayRefINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEDaRKNS3_6vectorIT_NS7_ISC_EEEENS1_15counterpart_tagE : 356 -> 332
~ __ZN6corelm19TokenListVocabularyC2ENS_4util4PathENSt3__110unique_ptrINS_17AbstractTokenizerENS3_14default_deleteIS5_EEEES2_ : 1008 -> 996
~ __ZN6corelm10TokenIDMapC2ERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE : 300 -> 276
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN5boost11multi_index6detail14copy_map_entryINS7_18ordered_index_nodeINS7_19null_augment_policyENS9_ISA_NS7_15index_node_baseINS5_6bimaps8relation15mutant_relationINSC_4tags6taggedIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSD_9member_at4leftEEENSG_IKlNSO_5rightEEEN4mpl_2naELb1EEENSK_ISW_EEEEEEEEEELb0EEEvT1_S13_T0_NS_15iterator_traitsIS13_E15difference_typeEb : 2140 -> 2116
~ __ZNSt3__116__insertion_sortB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN5boost11multi_index6detail14copy_map_entryINS7_18ordered_index_nodeINS7_19null_augment_policyENS9_ISA_NS7_15index_node_baseINS5_6bimaps8relation15mutant_relationINSC_4tags6taggedIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSD_9member_at4leftEEENSG_IKlNSO_5rightEEEN4mpl_2naELb1EEENSK_ISW_EEEEEEEEEEEEvT1_S13_T0_ : 144 -> 140
~ __ZNSt3__132__partition_with_equals_on_rightB9nqe220106INS_17_ClassicAlgPolicyEPN5boost11multi_index6detail14copy_map_entryINS4_18ordered_index_nodeINS4_19null_augment_policyENS6_IS7_NS4_15index_node_baseINS2_6bimaps8relation15mutant_relationINS9_4tags6taggedIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSA_9member_at4leftEEENSD_IKlNSL_5rightEEEN4mpl_2naELb1EEENSH_IST_EEEEEEEEEERNS_6__lessIvvEEEENS_4pairIT0_bEES14_S14_T1_ : 196 -> 192
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN5boost11multi_index6detail14copy_map_entryINS7_18ordered_index_nodeINS7_19null_augment_policyENS9_ISA_NS7_15index_node_baseINS5_6bimaps8relation15mutant_relationINSC_4tags6taggedIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENSD_9member_at4leftEEENSG_IKlNSO_5rightEEEN4mpl_2naELb1EEENSK_ISW_EEEEEEEEEEEEbT1_S13_T0_ : 820 -> 808
~ __ZNSt3__19transformB9nqe220106INS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_20back_insert_iteratorINS_6vectorIlNS5_IlEEEEEEZNK6corelm18AbstractVocabulary11tokensToIDsERKNSB_IS7_NS5_IS7_EEEEEUlT_E_EET0_SL_SL_SN_T1_ : 300 -> 284
~ __ZN7CoreNLP5mecab12_GLOBAL__N_18PosRule8EPK12mecab_node_tS4_ : 316 -> 308
~ __ZNSt3__19__shuffleB9nqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPiEES4_RNS_23mersenne_twister_engineIjLm32ELm624ELm397ELm31ELj2567483615ELm11ELj4294967295ELm7ELj2636928640ELm15ELj4022730752ELm18ELj1812433253EEEEET0_S8_T1_OT2_ : 180 -> 172
~ __ZN7CoreNLP15ParagraphTagger22enumerateTokensInRangeE7CFRangemU13block_pointerFvP7NLTokenPbE : 312 -> 324
~ __ZN7CoreNLP15ParagraphTagger12getNextTokenEv : 424 -> 428
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN7CoreNLP19TransferSeqTagModel25prepareDataSubsetForBatchERNS_6vectorINS_5tupleIJiNS4_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS9_ISB_EEEESD_NS4_IiNS9_IiEEEESF_EEENS9_ISG_EEEERNS4_ISD_NS9_ISD_EEEERNS4_INS4_ISF_NS9_ISF_EEEENS9_ISO_EEEESM_RSF_SM_RSO_ST_E3$_0PSG_Lb0EEEvT1_SX_T0_NS_15iterator_traitsISX_E15difference_typeEb : 4204 -> 4184
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN7CoreNLP19TransferSeqTagModel25prepareDataSubsetForBatchERNS_6vectorINS_5tupleIJiNS4_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS9_ISB_EEEESD_NS4_IiNS9_IiEEEESF_EEENS9_ISG_EEEERNS4_ISD_NS9_ISD_EEEERNS4_INS4_ISF_NS9_ISF_EEEENS9_ISO_EEEESM_RSF_SM_RSO_ST_E3$_0PSG_EEbT1_SX_T0_ : 984 -> 968
~ __ZNSt3__16vectorINS_5tupleIJiNS0_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS5_IS7_EEEES9_NS0_IiNS5_IiEEEESB_EEENS5_ISC_EEE22__base_destruct_at_endB9nqe220106EPSC_ : 96 -> 84
~ __ZN12_GLOBAL__N_113shouldConnectERKNSt3__16vectorINS0_8functionIFbPK12mecab_node_tS5_lEEENS0_9allocatorIS7_EEEES5_l : 196 -> 188
~ __ZNSt3__135__uninitialized_allocator_copy_implB9nqe220106INS_9allocatorINS_8functionIFbPK12mecab_node_tS5_lEEEEEPKS7_SA_PS7_EET2_RT_T0_T1_SC_ : 152 -> 136
~ __ZN7CoreNLP13TaggerManager28copyTagAndProbabilityAtIndexE15NLTokenizerUnitlPK10__CFStringl : 1100 -> 1084
~ __ZN7CoreNLP16BERTANEEmbedding16fillTokenVectorsEPK9__CFArraymjPfPKfS6_ : 928 -> 924
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_7greaterImEEPmLb1EEEvT1_S6_T0_NS_15iterator_traitsIS6_E15difference_typeEb : 1448 -> 1436
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_7greaterImEEPmEEbT1_S6_T0_ : 656 -> 640
~ _NLGazetteerCopyAvailableLabels : 340 -> 316
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE22__base_destruct_at_endB9nqe220106EPS3_ : 96 -> 84
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe220106EPKvm : 532 -> 520
~ __ZN5boost9algorithm13trim_right_ifINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS0_6detail14is_classifiedFEEEvRT_T0_ : 312 -> 304
~ __ZNSt3__15dequeIcNS_9allocatorIcEEE19__add_back_capacityEv : 480 -> 468
~ __ZNSt3__15dequeIcNS_9allocatorIcEEE19__add_back_capacityEm : 792 -> 780
~ _NLEmbeddingCopyNeighbors : 516 -> 500
~ _NLStringEmbeddingCopyNeighbors : 360 -> 336
~ _NLEmbeddingCopyNeighborsWithDistances : 576 -> 552
~ _NLStringEmbeddingCopyNeighborsWithDistances : 412 -> 396
~ _NLStringEmbeddingCopyNeighborsForVector : 492 -> 468
~ _NLStringEmbeddingCopyNeighborsForVectorWithDistances : 544 -> 528
~ __ZNSt3__15dequeIiNS_9allocatorIiEEE19__add_back_capacityEv : 480 -> 468
~ __ZNSt3__15dequeIZNK5Darts15DoubleArrayImplIvvivE16predictiveSearchINS3_16result_pair_typeEEEmPKcPT_mmiE5StateNS_9allocatorISA_EEE19__add_back_capacityEv : 480 -> 468
~ __ZN13sentencepiece22SentencePieceProcessor4LoadENSt3__110unique_ptrINS_10ModelProtoENS1_14default_deleteIS3_EEEE : 2380 -> 2372
~ __ZNK13sentencepiece22SentencePieceProcessor17ParseExtraOptionsENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEEPNS1_6vectorINS0_11ExtraOptionENS1_9allocatorIS7_EEEE : 2152 -> 2124
~ __ZNK13sentencepiece22SentencePieceProcessor17ApplyExtraOptionsERKNSt3__16vectorINS0_11ExtraOptionENS1_9allocatorIS3_EEEEPNS_17SentencePieceTextE : 1480 -> 1472
~ __ZN13sentencepiece7unigram7Lattice7ViterbiEv : 704 -> 692
~ __ZN13sentencepiece7unigram7Lattice6SampleEf : 900 -> 884
~ __ZNK13sentencepiece7unigram5Model15EncodeOptimizedENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 1160 -> 1164
~ __ZNK13sentencepiece7unigram5Model20SampleEncodeAndScoreENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEfibb : 2972 -> 2964
~ __ZNK13sentencepiece4word5Model6EncodeENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 380 -> 356
~ __ZNK13sentencepiece31SentencePieceText_SentencePiece18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 708 -> 684
~ __ZN6google8protobuf2io19EpsCopyOutputStream23WriteStringMaybeAliasedEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 304 -> 292
~ __ZNK13sentencepiece17SentencePieceText18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 500 -> 492
~ __ZNK13sentencepiece22NBestSentencePieceText18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 368 -> 360
~ __ZNK13sentencepiece11TrainerSpec18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 4612 -> 4484
~ __ZNK13sentencepiece12SelfTestData18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 396 -> 388
~ __ZNK13sentencepiece24ModelProto_SentencePiece18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 432 -> 424
~ __ZNK13sentencepiece10ModelProto18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 1040 -> 1000
~ __ZNKSt3__114default_deleteIN13sentencepiece4util6Status3RepEEclB9nqe220106EPS4_ : 96 -> 100
~ __ZN6google8protobuf2io19EpsCopyOutputStream30WriteStringMaybeAliasedOutlineEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 396 -> 388
~ __ZN6google8protobuf2io19EpsCopyOutputStream18WriteStringOutlineEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 436 -> 428
~ __ZNK6google8protobuf8internal12ExtensionSet13IsInitializedEv : 212 -> 208
~ __ZNK6google8protobuf8internal12ExtensionSet9Extension44InternalSerializeFieldWithCachedSizesToArrayEiPhPNS0_2io19EpsCopyOutputStreamE : 11144 -> 10532
~ __ZN6google8protobuf8internal12ShutdownDataD2Ev : 164 -> 168
~ __ZN6google8protobuf8internal18EpsCopyInputStream10NextBufferEii : 1064 -> 1068
~ __ZN6google8protobuf8internal17VarintParseSlow32EPKcj : 104 -> 116
~ __ZN6google8protobuf8internal16WireFormatParserINS1_28UnknownFieldLiteParserHelperEEEPKcRT_S5_PNS1_12ParseContextE : 248 -> 252
~ __ZN6google8protobuf8internal11VarintParseIyEEPKcS4_PT_ : 124 -> 128
~ __ZN6google8protobuf8internal16ReadSizeFallbackEPKcj : 120 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/filesystem.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/mmap.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_factory.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_interface.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_interface.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/normalizer.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/unigram_model.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/util.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/filesystem.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/mmap.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_factory.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_interface.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_interface.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/normalizer.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/unigram_model.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/util.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"

```
