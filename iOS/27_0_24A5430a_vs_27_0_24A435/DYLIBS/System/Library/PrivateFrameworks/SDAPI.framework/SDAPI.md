## SDAPI

> `/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI`

```diff

 19.0.0.0.0
-  __TEXT.__text: 0x308534
+  __TEXT.__text: 0x30881c
   __TEXT.__const: 0x2e1eb
   __TEXT.__cstring: 0x17afd
-  __TEXT.__gcc_except_tab: 0x22624
-  __TEXT.__unwind_info: 0xa6b8
+  __TEXT.__gcc_except_tab: 0x22628
+  __TEXT.__unwind_info: 0xa6b0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7408
   __DATA_CONST.__weak_got: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8087
+  Functions: 8086
   Symbols:   12569
   CStrings:  3261
 
Functions:
~ __ZN14EnumParamRangeC2EPK13EnumParamItem : 120 -> 124
~ __ZNSt3__115basic_stringbufIwNS_11char_traitsIwEENS_9allocatorIwEEE15__init_buf_ptrsB9fqe220106Ev : 256 -> 260
~ __ZNK6PhnMgr14savePhnMgrTextEP5DFileb : 652 -> 656
~ __ZNK9DgnString19checkWhiteSpaceFreeEj : 124 -> 128
~ __ZN9DgnBuffer12printfAppendEPKcz : 300 -> 280
~ __ZNSt3__16vectorIP8TItnRuleNS_9allocatorIS2_EEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorI16TPItnRuleControlNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIPK7TSymbolNS_9allocatorIS3_EEE6resizeEm : 284 -> 288
~ __ZN10Constraint12prunePreListEP17RecogGermIteratorb : 1880 -> 1888
~ __ZN10Constraint15addToReturnListER9RecogGermPj : 376 -> 380
~ __ZNK6PicMgr23saveAdaptPhonemesAsTextEP5DFileb : 1052 -> 1056
~ __ZNK6PicMgr13searchPicTreeERK3PicRK8DgnArrayI6BranchEtPj : 240 -> 244
~ __ZNK6PicMgr22getEndDuplicatesSearchERK8DgnArrayI3PicEP12DgnPrimArrayIjEPS0_I7PicNodeEPjS7_ : 540 -> 528
~ __ZNSt3__16vectorINS_4pairImmEENS_9allocatorIS2_EEE6resizeEm : 284 -> 288
~ __ZN4TRne13applyInternalERKNSt3__16vectorIPKwNS0_9allocatorIS3_EEEEPK8TLatticeRNS1_IP29TLatticeConstructionTransDataNS4_ISD_EEEERm : 4820 -> 4836
~ __ZNSt3__16vectorImNS_9allocatorImEEE6resizeEm : 284 -> 288
~ __ZN15GenoneClassTree17getDynamicClassesERK12DgnPrimArrayIjEjjjR8DgnArrayIS1_ES6_ : 2936 -> 2944
~ __ZNK11DgnTextFile5atosiEPKc : 564 -> 568
~ __ZN11DgnTextFile18checkAgainstFormatEPKc24B_DgnTextFileFieldFormat : 240 -> 244
~ __ZN17DgnTextFileParser18getNextHeaderFieldEP9DgnStringS1_b : 700 -> 704
~ __ZN17DgnTextFileParser28scanValueForLineFieldFormatsERK9DgnString : 1184 -> 1188
~ __ZN17DgnTextFileParser10readHeaderEv : 1344 -> 1348
~ __ZN13TLexiconScoreC2EPKwS1_mmRK11TLocaleInfo : 1956 -> 1964
~ __ZN8TLexiconD2Ev : 1392 -> 1384
~ __ZN8TLexicon18collationSearchRecEPKwRNSt3__16vectorIP5TWordNS2_9allocatorIS5_EEEER7TBufferIwERm : 568 -> 572
~ __ZN8TLexicon10cleanCacheEv : 1260 -> 1252
~ __ZN7LatticeI13WordLatticeLCE25maybeCreateAndConnectLinkEjjRKS0_bPj : 292 -> 296
~ __ZN7LatticeI13WordLatticeLCE13gcNonTerminalEv : 400 -> 404
~ __ZN7LatticeI13WordLatticeLCE12gcNonInitialEv : 400 -> 404
~ __ZN7LatticeI16PhonemeLatticeLCE11destroyNodeEj : 396 -> 400
~ __ZN7LatticeI13WordLatticeLCE16removeMultiLinksEv : 332 -> 336
~ __ZN7LatticeI13WordLatticeLCE15topSortInternalEb : 1308 -> 1320
~ __ZN6TLexerC2ER12TInputStreammPK13TLexerLexiconP10TAllocator : 1784 -> 1792
~ __ZNK31FstSearchLateLatticeHashBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 316 -> 320
~ __ZN31FstSearchLateLatticeHashBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 716 -> 720
~ __ZN27FstSearchLatticeHashBackoff26getCandidateTokensForTraceERK32FstSearchLatticeHashBackoffTraceR8DgnArrayI37FstSearchLatticeHashBackoffTraceTokenE : 428 -> 420
~ __ZN27FstSearchLatticeHashBackoff20annihilateNullTracesEv : 892 -> 888
~ __ZN31FstSearchLatticeDurationBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 720 -> 724
~ __ZN20FstSearchLatticeHash20annihilateNullTracesEv : 892 -> 888
~ __ZN28FstSearchDurationHashBackoff13advanceDeltasEiiP11SearchStatsb : 1644 -> 1640
~ __ZN28FstSearchDurationHashBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 660 -> 672
~ __ZNK9FstSearch12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 320 -> 324
~ __ZN9FstSearch18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 660 -> 672
~ __ZN35FstSearchLeafLatticeDurationBackoff13advanceDeltasEiiP11SearchStatsb : 2404 -> 2392
~ __ZN35FstSearchLeafLatticeDurationBackoff14propagateNullsEiiP11SearchStats : 1524 -> 1700
~ __ZNK35FstSearchLeafLatticeDurationBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 320 -> 324
~ __ZN28FstSearchLeafLatticeDuration13advanceDeltasEiiP11SearchStatsb : 2304 -> 2300
~ __ZN27FstSearchLeafLatticeBackoff13advanceDeltasEiiP11SearchStatsb : 2148 -> 2140
~ __ZN27FstSearchLeafLatticeBackoff29makeViterbiDecisionOnEmittingEv : 308 -> 312
~ __ZN27FstSearchLeafLatticeBackoff14propagateNullsEiiP11SearchStats : 1356 -> 1372
~ __ZNK27FstSearchLeafLatticeBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 312 -> 320
~ __ZN27FstSearchLeafLatticeBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 720 -> 724
~ __ZN20FstSearchLeafLattice13advanceDeltasEiiP11SearchStatsb : 2076 -> 2068
~ __ZN31FstSearchLatticeDurationBackoff13advanceDeltasEiiP11SearchStatsb : 2012 -> 2032
~ __ZN31FstSearchLatticeDurationBackoff29makeViterbiDecisionOnEmittingEv : 308 -> 312
~ __ZN31FstSearchLatticeDurationBackoff14propagateNullsEiiP11SearchStats : 1328 -> 1392
~ __ZNK31FstSearchLatticeDurationBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 308 -> 316
~ __ZN24FstSearchLatticeDuration13advanceDeltasEiiP11SearchStatsb : 1952 -> 1956
~ __ZN27FstSearchLateLatticeBackoff13advanceDeltasEiiP11SearchStatsb : 1624 -> 1636
~ __ZN23FstSearchLatticeBackoff14propagateNullsEiiP11SearchStats : 1452 -> 1428
~ __ZNK23FstSearchLatticeBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 316 -> 320
~ __ZN23FstSearchLatticeBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 700 -> 704
~ __ZN28FstSearchLeafDurationBackoff13advanceDeltasEiiP11SearchStatsb : 2176 -> 2188
~ __ZNK28FstSearchLeafDurationBackoff12getBestTraceEP15DgnPrimFixArrayIhEPS0_IbEb : 316 -> 320
~ __ZN28FstSearchLeafDurationBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 660 -> 672
~ __ZN21FstSearchLeafDuration13advanceDeltasEiiP11SearchStatsb : 2116 -> 2112
~ __ZN24FstSearchDurationBackoff13advanceDeltasEiiP11SearchStatsb : 1776 -> 1784
~ __ZN20FstSearchLeafBackoff13advanceDeltasEiiP11SearchStatsb : 1996 -> 2000
~ __ZN20FstSearchLeafBackoff18createLatticeNodesER15DgnPrimFixArrayIiER12DgnPrimArrayIjEP11WordLatticeR8DgnArrayIS3_IiEERS0_IhERS0_IbE : 644 -> 648
~ __ZN16FstSearchBackoff13advanceDeltasEiiP11SearchStatsb : 1620 -> 1632
~ __ZN13ActiveWordMgr13newActiveWordERK6CWIDACi18B_NodeSkippingTypeb : 608 -> 600
~ __ZNSt3__16vectorI12TRegExpMatchNS_9allocatorIS1_EEE6resizeEm : 372 -> 376
~ __ZN10TTokenizer20deleteExpensivePathsER6TGraph : 2232 -> 2228
~ __ZNK12TDigitObject5buildEPKwP7TVertexS3_P6TGraphP8TLexicon : 1096 -> 1104
~ __ZNK15TCountingObject5buildEPKwP7TVertexS3_P6TGraphP8TLexicon : 2840 -> 2848
~ __ZL20callBackSeqAltHelperPKN16TGrammarCompiler9TArgumentEmPKwP8TLexiconPw : 1184 -> 1200
~ __ZNK3Voc7getPicsERK6CWIDAC12B_PronSubsetPtS4_bR8DgnArrayI3PicE : 1052 -> 1064
~ __Z11isValidNamePKc : 104 -> 108
~ __ZN8TClitics8addWordsEP7TVertexP6TGraphP10TSegmenter : 3056 -> 3060
~ __ZNSt3__16vectorI16TItnControlStateNS_9allocatorIS1_EEE6resizeEm : 292 -> 296
~ __ZNK14TResultManager5alignEPKPP22TPItnResultHandle_fakemS4_mR7TBufferIcE : 1368 -> 1364
~ __ZN14TResultManager9applyHintEPP20TPItnHintHandle_fake : 5604 -> 5596
~ __ZNSt3__16vectorImNS_9allocatorImEEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKmEES9_EENS6_IPmEES9_T0_T1_l : 516 -> 532
~ __ZNSt3__16vectorI16TItnControlStateNS_9allocatorIS1_EEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKS1_EESA_EENS7_IPS1_EESA_T0_T1_l : 564 -> 580
~ __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPKjS7_EEvT0_T1_l : 308 -> 312
~ __ZN10TFormatter8addWordsEPKPP22TPItnResultHandle_fakeS4_bRNSt3__16vectorI12TItnWordDataNS5_9allocatorIS7_EEEE : 1052 -> 1056
~ __ZN10TFormatter7segmentERKNSt3__16vectorI12TItnWordDataNS0_9allocatorIS2_EEEEmm : 6344 -> 6356
- __ZNSt3__16vectorINS_4pairIjjEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
~ __ZNSt3__16vectorIPP22TPItnResultHandle_fakeNS_9allocatorIS3_EEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPKS3_SA_EENS_11__wrap_iterIPS3_EENSB_ISA_EET0_T1_l : 516 -> 532
~ __ZNK17WordLanguageModel17getWordTransducerE12DgnPrimArrayItER18DgnPrimStructArrayI19WordLMTransducerArcER8DgnArrayIS0_IjEEjsRS7_ : 5724 -> 5728
~ __ZL25callBackThousandSeparatorPKN16TGrammarCompiler9TArgumentEmPvS3_R10TAllocator : 1308 -> 1312
~ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE6resizeEm : 284 -> 288
~ __ZN18MultiLanguageModel19getTopicLmSlotNamesEP8DgnArrayI9DgnStringE : 448 -> 452
~ __ZN18MultiLanguageModel27getFactoryCorrectiveLmNamesEP8DgnArrayI9DgnStringE : 448 -> 452
~ __ZN18MultiLanguageModel13loadMultiTextEP5DFilebP12DgnPrimArrayIdEPb : 7916 -> 7920
~ __ZNK8WordList7getPronEjP12DgnPrimArrayItE : 132 -> 160
~ _TPItn_WordSequenceToResult : 5348 -> 5352
~ __ZN23BackTraceLatticeBuilder10getLMScoreERK6CWIDACS2_PiP7LMStats : 1132 -> 1136
~ __ZN23BackTraceLatticeBuilder16seedOneInContextEbRK9RecogGermS2_iiiiP11WordLatticeP7LMStatsPK8DgnArrayI18HistoryAndBigScoreEb : 3504 -> 3528
~ __ZN7LatticeI13WordLatticeLCE33maybeCreateAndConnectOrUpdateLinkEjjRKS0_bPj : 332 -> 336
~ __ZN23BackTraceLatticeBuilder17seedAllRightGermsER9RecogGermjP11WordLatticebPjS4_S4_P7LMStats : 1812 -> 1816
~ __ZN13BtNBestResult13maybeGetNBestILb0EEEPK8DgnArrayI18HistoryAndBigScoreEt : 368 -> 376
~ __ZN18DgnSharedMemStream12readWithModeEPcj19B_DgnStreamReadMode : 288 -> 292
~ __ZN18DgnSharedMemStream10writeBytesEPKcj : 356 -> 360
~ __ZN26ForwardLatticeNodeIteratorI13WordLatticeLCEC2EPK7LatticeIS0_E : 224 -> 228
~ __ZN16LexTreeNetScorer15updateTree_SkipEv : 1296 -> 1308
~ __ZN16LexTreeNetScorer14seedSuccessorsEjjjtij : 1476 -> 1480
~ __ZN9NeuralNet33fastFeedbackSendingWithDotProductEP14NeuralNetBlock : 184 -> 188
~ __ZN9NeuralNet16fastOutputLinearEP14NeuralNetBlock : 88 -> 92
~ __ZN9NeuralNet14fastOutputReluEP14NeuralNetBlock : 100 -> 104
~ __ZN8FileSpec23getDiagnosticMaskedNameEPKcP9DgnString : 224 -> 228
~ __ZN17RecogResultChoice19fillFromNBestChoiceEPK11NBestChoicejbbP8DgnArrayI18WordConfidenceInfoE : 872 -> 852
~ __ZN15NonCoartSyncNet16scoreNetInternalEiiiii : 552 -> 556
~ __ZNK10BigramData17initNewBigramDataEPS_P14HuffmanEncoderItjEP8DgnArrayI16DiskNgramContextEP9DgnIArrayIPS5_E : 1364 -> 1368
~ __ZNK10BigramData36savePersistentAndFillInNewBigramDataEP9DgnStreamRjPS_RK14HuffmanEncoderItjEj : 1020 -> 1024
~ __ZNK10BigramData27fillInFullyLoadedBigramDataEPS_ : 856 -> 860
~ __ZNK11TrigramData18initNewTrigramDataEPS_P14HuffmanEncoderItjEP8DgnArrayI16DiskNgramContextEP9DgnIArrayIPS5_EPK12DgnPrimArrayIdEb : 1692 -> 1696
~ __ZNK11TrigramData37savePersistentAndFillInNewTrigramDataEP9DgnStreamRjPS_RK14HuffmanEncoderItjEjj : 1020 -> 1024
~ __ZNK11TrigramData28fillInFullyLoadedTrigramDataEPS_ : 1084 -> 1088
~ __ZNK12QuadgramData16getScoreForIndexEjjj : 140 -> 144
~ __ZNK17WordLanguageModel8saveTextEP5DFileb : 7084 -> 7092
~ __ZN17WordLanguageModel18verifyUniScForBiScEv : 492 -> 496
~ __ZN17WordLanguageModel17throwOnBadTriBoWtEv : 444 -> 452
~ __ZN17WordLanguageModel19verifyUniScForTriScEv : 560 -> 564
~ __ZNK17WordLanguageModel13verifyBigramsEPKc : 900 -> 904
~ __ZNK17WordLanguageModel14verifyTrigramsEPKc : 920 -> 924
~ __ZN17WordLanguageModel13languageScoreEjjP7LMStatsP13LMContextDataP14LMScoreDetailsbbPb : 964 -> 972
~ __ZN17WordLanguageModel22languageScoreForSearchEjjP7LMStatsP13LMContextDatabPb : 872 -> 880
~ __ZN13NGramIterator5next2Ev : 452 -> 456
~ __ZN13NGramIterator5next3Ev : 720 -> 724
~ __ZN11AcousticNet14unpackEndTraceERK8DgnArrayI3PicE12B_ScoreOrder : 808 -> 812
~ __ZN10Recognizer22seedFromOnePredForwardEP14SeedActiveWordi : 7568 -> 7564
~ __ZNK10Recognizer26addCrumbsToPrefilterResultEbPK15PrefilterResultjPS0_ : 1024 -> 1032
~ __ZN7LatticeI16PhonemeLatticeLCE25maybeCreateAndConnectLinkEjjRKS0_bPj : 244 -> 252
~ __ZN7LatticeI16PhonemeLatticeLCE13gcNonTerminalEv : 400 -> 404
~ __ZN7LatticeI16PhonemeLatticeLCE12gcNonInitialEv : 400 -> 404
~ __ZN7LatticeI16PhonemeLatticeLCE15topSortInternalEb : 1308 -> 1320
~ __ZNSt3__16vectorIPP19TPItnTagHandle_fakeNS_9allocatorIS3_EEE6resizeEm : 284 -> 288
~ __ZN10TFormatter11collectTagsER4TFsaR7TBufferIwEmmR10TAllocatorRNSt3__16vectorIPK17TFormatProductionNS7_9allocatorISB_EEEERNS7_3setIPP19TPItnTagHandle_fakeNS7_4lessISJ_EENSC_ISJ_EEEE : 2772 -> 2776
~ __ZNSt3__16vectorIPP19TPItnTagHandle_fakeNS_9allocatorIS3_EEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEESE_EENS_11__wrap_iterIPS3_EENSF_IPKS3_EET0_T1_l : 640 -> 656
~ __Z15errWarnInternalPKciS0_iS0_z : 584 -> 552
~ __ZN22RealDFileSubFileStreamC2E19B_DgnStreamOpenModeRK8FileSpecP9RealDFilePKc17B_SubFileOpenModetjjby : 3016 -> 3024
~ __ZN9RealDFile10readHeaderEbP18B_DFileSupportTypeP9DgnString : 4956 -> 4960
~ __ZN11BaseSyncNet14unpackSequenceEPK3PiciPP4NodeS5_12B_ScoreOrder : 544 -> 548
~ __ZN7SyncNet16scoreNetInternalEiiiii : 1552 -> 1556
~ __ZN10TCondition7setEnumEPK11TFileObjectm : 1416 -> 1420
~ __ZL25callBackThousandSeparatorPKN16TGrammarCompiler9TArgumentEmPvS3_R10TAllocator : 1308 -> 1312
~ __ZNK8TLmScore10getLmScoreERKNSt3__16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEPKc : 352 -> 356
~ __ZNSt3__16vectorINS_4pairIPK5TWordmEENS_9allocatorIS5_EEE6resizeEm : 284 -> 288
~ __Z12mrec_qsort_rI12ParamSpecMgrEvPvmmS1_ : 2316 -> 2312
~ __ZN7LatticeI13WordLatticeLCE26maybeCreateAndConnectLink2EjjRKS0_ : 196 -> 200
~ __ZNK11WordLattice15fillLatticeDataEP11LatticeData : 696 -> 700
~ __ZNK11WordLattice21initializeEndNodeHeapEjRK8DgnArrayIS0_I11LatticePathEEP12DgnIOwnArrayIP16DgnPriorityQueueIS1_EERK12DgnPrimArrayIbE : 312 -> 316
~ __ZNK11WordLattice14wordSeqPresentERK11LatticePathjRK8DgnArrayIS3_IS0_EE : 500 -> 504
~ __ZN11WordLattice16addSegmentationsEPK6ActivePK6PhnMgrPK6PicMgr : 1476 -> 1480
~ __ZNK11WordLattice21computeBackwardScoresEP12DgnPrimArrayIiE : 432 -> 440
~ __ZNK11WordLattice33needToSplitNodeForBigramExpansionEjj : 248 -> 252
~ __ZNK11WordLattice27needToSplitNodeForExpansionEjjjP12DgnPrimArrayIjEPS0_IbES2_S4_PjS5_ : 1576 -> 1588
~ __ZN11WordLattice16rescoreLatticeLMEP14SearchLMScorerP12LatticeStatsb : 1612 -> 1624
~ __ZN11WordLattice18computeParseTokensEPK12DgnPrimArrayIjEPK8DgnArrayIS4_I10ParseTokenEE : 1216 -> 1228
~ __ZN27BackwardLatticeNodeIteratorI13WordLatticeLCEC2EPK7LatticeIS0_E : 224 -> 228
~ __ZN7NodeNet14unpackSequenceEPK3PiciPP4NodeS5_12B_ScoreOrder : 652 -> 656
~ __Z42PackedIntMICShortListGenoneScoringFunctionPK9PelScorertjPtPj : 368 -> 360
~ __Z39PackedIntShortListGenoneScoringFunctionPK9PelScorertjPtPj : 396 -> 392
~ __Z39PackedIntMICShortListPelScoringFunctionPK9PelScorertPj : 560 -> 556
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE6resizeEmb : 128 -> 132
~ __ZN13CWIDCrumbWACS10mergeCrumbERKS_PK10HistoryMgr : 1312 -> 1344
~ __ZNK18CWIDCrumbWACSFrame17getAccumHistScoreEPK10HistoryMgrjt : 156 -> 164
~ __ZNK18CWIDCrumbWACSFrame10getHistoryERK6CWIDACt : 140 -> 136
~ __ZN7CollMgr20newTwoLevelCollationEPKctt : 676 -> 680
~ __ZNK19EnumGlobalParamBase18getNameForEnumItemEi : 76 -> 80
~ __Z18GetNameForEnumItemPK13EnumParamItemi : 76 -> 80
```
