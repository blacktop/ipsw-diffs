## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

```diff

 3567.0.0.0.0
-  __TEXT.__text: 0x22283c
+  __TEXT.__text: 0x222810
   __TEXT.__init_offsets: 0xc0
   __TEXT.__objc_methlist: 0x10af0
   __TEXT.__dlopen_cstrs: 0x781

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa080
+  __DATA_CONST.__objc_selrefs: 0xa088
   __DATA_CONST.__objc_superrefs: 0x728
   __DATA_CONST.__objc_arraydata: 0x10a8
   __DATA_CONST.__got: 0x18b8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 10539
-  Symbols:   21820
+  Symbols:   21821
   CStrings:  4086
 
Symbols:
+ _objc_msgSend$isFeatureEnabledForInternalBuilds
Functions:
~ __ZNSt3__16vectorIN2KB6StringENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 224 -> 232
~ -[TIFeedbackController isFCSBuild] : 8 -> 104
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_ : 208 -> 200
~ __ZNK14TIInputManager18apply_case_changesERN2KB9CandidateERKNSt3__16vectorINS0_5InputENS3_9allocatorIS5_EEEEj14TIShiftContextbRKN3WTF6RefPtrINS0_19DictionaryContainerEEEP10__CFString : 2732 -> 2736
~ __ZNK14TIInputManager32lookup_static_dynamic_candidatesERN2KB19CandidateCollectionENS0_10LookupTypeERKNS0_6StringEU13block_pointerFvS2_P10__CFStringEj : 900 -> 912
~ -[TISKMetricCollector _coalesceTaps] : 928 -> 932
~ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJmEEEPmDpOT_ : 208 -> 200
~ __Z14asMCNearbyKeysRKN3WTF6VectorINS_6RefPtrIN2TI8Favonius8KeyMatchEEELm0EEEm : 296 -> 292
~ __ZNK2KB16LanguageModelStr30conditional_likelihood_batchedERKNSt3__16vectorINS_9CandidateENS1_9allocatorIS3_EEEERKNS2_INS2_IN17language_modeling2v113TokenMetadataENS4_ISB_EEEENS4_ISD_EEEERKNS_20LanguageModelContextEP10__CFStringb : 1960 -> 1956
~ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 208 -> 200
~ __ZNSt3__16vectorIN17language_modeling2v114CompletionStemENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 276 -> 268
~ -[TIKeyboardInputManagerMecabra saveGeometryForInput:atIndex:] : 692 -> 696
~ __ZN3WTF6VectorINS_6RefPtrIN2TI8Favonius8KeyMatchEEELm0EEC2ERKS6_ : 152 -> 148
~ __ZNK2TI2CP4PatheqERKS1_ : 296 -> 300
~ __ZN2TI2CP4Path6resizeEj : 448 -> 452
~ _UnikeySetup : 932 -> 948
~ __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 312 -> 304
~ __ZNSt3__16vectorIN10applesauce2CF8ArrayRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 288 -> 272
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZN2KB22CandidateFilterFactory21FilterStackDefinitionC1ERKNS_6vectorIN10applesauce2CF8ArrayRefENS_9allocatorIS8_EEEEE3$_0NS_11__wrap_iterIPNS7_13DictionaryRefEEEEEvT1_SK_SK_OT0_NS_15iterator_traitsISK_E15difference_typeESP_PNSO_10value_typeEl : 1680 -> 1668
~ __ZNK2KB22LanguageModelContainer17lexicon_id_vectorEv : 368 -> 372
~ __ZNK2KB22LanguageModelContainer32active_locale_identifiers_vectorEv : 364 -> 368
~ __ZNK2KB22LanguageModelContainer27prior_lexicon_probabilitiesEv : 384 -> 388
~ __ZN2KB22LanguageModelContainer29PredictionEnumeratorContainer28update_next_prediction_indexEv : 212 -> 216
~ __ZN14TIInputManager9add_inputERKN2KB6StringEj : 1092 -> 1084
~ __ZN14TIInputManager13text_acceptedERKN2KB6StringES3_j14TIShiftContextb : 1888 -> 1884
~ __ZNSt3__110__function6__funcIZNK14TIInputManager21candidates_for_stringERKN2KB6StringE14TIShiftContextE3$_0FvRNS3_19CandidateCollectionENS3_20CandidateFilterFlagsEbEEclESA_OSB_Ob : 1592 -> 1588
~ __ZNSt3__110__function6__funcIZNK14TIInputManager22predictions_for_stringERKN2KB6StringENS3_10LookupTypeEE3$_0FvRNS3_19CandidateCollectionENS3_20CandidateFilterFlagsEbEEclESA_OSB_Ob : 2096 -> 2100
~ __ZN3WTF6VectorIjLm32EEaSERKS1_ : 228 -> 232
~ __ZNSt3__16vectorIN2KB6StringENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 244 -> 252
~ __ZNK2TI2CP13PathResampler19is_inflection_pointEj : 788 -> 784
~ __ZN2TI2CP25ContextualShapeRecognizer19hypotheses_for_pathERKNS0_4PathE : 2904 -> 2792
~ __ZN2TI2CP25ContextualShapeRecognizer12store_shapesEv : 568 -> 572
~ __ZN2TI8Favonius14KeyboardLayoutC2ERKN3WTF6VectorINS2_6RefPtrINS0_9LayoutKeyEEELm0EEE : 212 -> 208
~ __ZNK2TI8Favonius10SearchNode23get_language_extensionsERN3WTF6VectorINS2_6RefPtrINS0_16TypingHypothesisEEELm0EEERKNS4_INS0_3KeyEEE : 508 -> 504
~ __ZN2TI8Favonius10SearchNode30create_key_sequence_extensionsERNSt3__16vectorIN3WTF6RefPtrIS1_EENS2_9allocatorIS6_EEEERKNS3_INS2_4pairINS5_INS0_12TouchHistoryEEENS5_INS0_8KeyMatchEEEEENS7_ISG_EEEEf : 944 -> 936
~ __ZN3WTF6VectorINS_6RefPtrIN2TI8Favonius16TypingHypothesisEEELm0EEC2ERKS6_ : 156 -> 152
~ __ZNK2TI8Favonius10BeamSearch6extendEN3WTF10PassRefPtrINS0_12TouchHistoryEEENS3_INS0_8KeyMatchEEEb : 4160 -> 4156
~ __ZNK2TI8Favonius10BeamSearch21extend_with_backspaceEN3WTF10PassRefPtrINS0_12TouchHistoryEEENS3_INS0_6SearchEEERKNSt3__16vectorINS8_4pairINS2_6RefPtrIS4_EENSB_INS0_8KeyMatchEEEEENS8_9allocatorISF_EEEE : 1572 -> 1576
~ __ZNK2TI8Favonius10BeamSearch12drop_touchesERKNSt3__16vectorIbNS2_9allocatorIbEEEERKN2KB20LanguageModelContextERKNS9_6StringEN3WTF10PassRefPtrINS0_11TypingModelEEENSH_INS0_18CandidateGeneratorEEE : 476 -> 480
~ __ZN2TI8Favonius26FavoniusStrokeBuildManager19InputTouchAlignment17replace_alignmentEjjRKN2KB9AlignmentE : 628 -> 644
~ __ZNK2TI8Favonius26FavoniusStrokeBuildManager24is_ml_tap_typing_enabledEv : 224 -> 220
~ __ZN2TI8Favonius26FavoniusStrokeBuildManager24align_candidate_to_inputERKN2KB6StringES5_RKNS2_9AlignmentE : 920 -> 912
~ __ZNSt3__16vectorIPN2TI8Favonius16SearchNodeSourceENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_ : 208 -> 200
~ __ZNK20TIFitAffineMLLMatrix6valuesEv : 348 -> 352
~ ____ZNK2KB23DynamicDictionaryCursor35merge_children_with_static_siblingsERNSt3__16vectorINS_17DictionaryCursorsENS1_9allocatorIS3_EEEERKNS_16StaticDictionaryERKNS_17DynamicDictionaryE_block_invoke_2 : 1288 -> 1296
~ __ZN2TI2CP6Search17initialize_searchEv : 512 -> 508
~ __ZNK2KB22StaticDictionaryCursor14finishes_wordsEv : 80 -> 76
~ __ZNK2KB22NgramCandidateRefinery27add_context_weights_batchedERNSt3__16vectorINS_9CandidateENS1_9allocatorIS3_EEEE : 1632 -> 1636
~ __ZL33_sortkey_for_string_with_collatorRKN2KB6StringEPK9UCollator : 876 -> 868
```
