## CorePrediction

> `/System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x4963c
+  __TEXT.__text: 0x49684
   __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_methlist: 0x844
   __TEXT.__gcc_except_tab: 0x3360

   __TEXT.__unwind_info: 0x1710
   __TEXT.__objc_classname: 0xa2
   __TEXT.__objc_methname: 0x17fd
-  __TEXT.__objc_methtype: 0x548
+  __TEXT.__objc_methtype: 0x54e
   __TEXT.__objc_stubs: 0x1400
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x450

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 898A5A31-EECA-3C0B-87F5-44FD5455D7D1
+  UUID: BEB9A71C-348A-3208-9782-B107FD1891AB
   Functions: 1110
   Symbols:   3356
   CStrings:  1374
Functions:
~ __ZNSt3__16vectorINS_8valarrayIcEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 272 -> 276
~ __ZNSt3__16vectorINS_8valarrayIdEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 272 -> 276
~ __ZN25CPMLNaiveBayesSuggestions14predict_sortedERKNSt3__16vectorINS1_IiNS0_9allocatorIiEEEENS2_IS4_EEEERKNS1_I9ProbIndexNS2_IS9_EEEEiRSB_ : 736 -> 744
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZN13CPMLOnlineSvmC2EP7CPMLCDBP17CPMLSerializationP15CPMLTunableData : 1328 -> 1320
~ __ZN35CPMLNaiveBayesSuggestionsClassifierC2EP14CPMLStatisticsP17CPMLSerializationP15CPMLTunableData : 1828 -> 1832
~ __ZN29CPLogisticRegressionClassfierC2EP7CPMLCDBP17CPMLSerializationP15CPMLTunableData : 1996 -> 2000
~ __ZNSt3__16vectorI13data_record_tNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 296 -> 300
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_I13data_record_tNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI13data_record_tNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_I13data_record_tNS_9allocatorIS1_EEEENS2_IS4_EEE18__assign_with_sizeB8ne200100IPS4_S8_EEvT_T0_l : 368 -> 372
~ __ZNSt3__16vectorI13data_record_tNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l : 324 -> 328
~ -[CPMLModelEvaluate constructVector:withColumnPosition:maxColNumber:withValue:] : 644 -> 652
~ -[CPMLModelEvaluate boundResult:] : 416 -> 412
~ __ZNSt3__16vectorINS_8valarrayIdEENS_9allocatorIS2_EEE8__appendEm : 296 -> 304
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_13unordered_mapIiiNS_4hashIiEENS_8equal_toIiEENS_9allocatorINS_4pairIKiiEEEEEEEENS_22__unordered_map_hasherIySD_NS3_IyEENS5_IyEELb1EEENS_21__unordered_map_equalIySD_SG_SF_Lb1EEENS7_ISD_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSQ_IJEEEEEENS8_INS_15__hash_iteratorIPNS_11__hash_nodeISD_PvEEEEbEERKT_DpOT0_ : 624 -> 628
~ __ZN28CPMLDelegateEngineNaiveBayes23preProcessPredictSortedERKNSt3__16vectorINS1_IiNS0_9allocatorIiEEEENS2_IS4_EEEERS6_ : 908 -> 912
~ __ZNSt3__16vectorI9ProbIndexNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 376 -> 380
CStrings:
+ "{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"\"{?=\"__cap_\"^i}}"
- "{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__cap_\"^i}"

```
