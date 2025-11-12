## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

 353.0.0.0.0
-  __TEXT.__text: 0x15b73c
+  __TEXT.__text: 0x15b79c
   __TEXT.__auth_stubs: 0x1c70
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x9af4

   __TEXT.__eh_frame: 0x1e4
   __TEXT.__objc_classname: 0x1816
   __TEXT.__objc_methname: 0x15e8d
-  __TEXT.__objc_methtype: 0x462c
+  __TEXT.__objc_methtype: 0x4646
   __TEXT.__objc_stubs: 0xe5e0
   __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__const: 0x3840

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 886EB6E7-BA4D-381D-8A69-1A77CB6FEEFA
+  UUID: 52A065D2-4737-3D06-8696-2AA5A1ECB45B
   Functions: 5225
   Symbols:   17737
   CStrings:  7911
Functions:
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__15dequeI7CGPointNS_9allocatorIS1_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIP7CGPointNS_9allocatorIS2_EEE13emplace_frontIJS2_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNK6homeai10clustering15GreedyClusterer17computeMergePairsERNSt3__13setIxNS2_4lessIxEENS2_9allocatorIxEEEES9_NS2_10shared_ptrINS2_6vectorINS2_5tupleIJxxfEEENS6_ISD_EEEEEEb : 704 -> 716
~ __ZNSt3__16__treeINS_12__value_typeImNS_4listIxNS_9allocatorIxEEEEEENS_19__map_value_compareImS6_NS_4lessImEELb1EEENS3_IS6_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJOmEEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_ : 244 -> 252
~ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_13unordered_setIxNS_4hashIxEENS_8equal_toIxEENS_9allocatorIxEEEEEENS_22__unordered_map_hasherIxSA_S4_S6_Lb1EEENS_21__unordered_map_equalIxSA_S6_S4_Lb1EEENS7_ISA_EEE25__emplace_unique_key_argsIxJRKNS_21piecewise_construct_tENS_5tupleIJRKxEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_ : 624 -> 628
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_6vectorIxNS_9allocatorIxEEEEEENS_22__unordered_map_hasherIxS6_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS6_SB_S9_Lb1EEENS3_IS6_EEE25__emplace_unique_key_argsIxJRKNS_21piecewise_construct_tENS_5tupleIJRKxEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 592 -> 600
~ +[HMIGreedyClustering centermostFaceprintInCluster:faceObservations:] : 1388 -> 1408
~ __ZNSt3__16vectorIN2cv3MatENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__15dequeIcNS_9allocatorIcEEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPcNS_9allocatorIS1_EEE13emplace_frontIJS1_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__16vectorIN2cv3MatENS_9allocatorIS2_EEE8__appendEm : 452 -> 460
~ __ZN2cv19goodFeaturesToTrackERKNS_11_InputArrayERKNS_12_OutputArrayEiddS2_ibd : 3476 -> 3480
~ __ZNSt3__16vectorINS0_IN2cv6Point_IfEENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN2cv6Point_IfEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 284 -> 280
CStrings:
+ "@172@0:8{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}16{vector<float, std::allocator<float>>=^f^f{?=^f}}40{vector<cv::Point_<float>, std::allocator<cv::Point_<float>>>=^v^v{?=^v}}64{vector<cv::Point_<float>, std::allocator<cv::Point_<float>>>=^v^v{?=^v}}88@112Q120{vector<cv::Mat, std::allocator<cv::Mat>>=^{Mat}^{Mat}{?=^{Mat}}}128{CGSize=dd}152f168"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"\"{?=\"__cap_\"^f}}"
- "@172@0:8{vector<unsigned char, std::allocator<unsigned char>>=***}16{vector<float, std::allocator<float>>=^f^f^f}40{vector<cv::Point_<float>, std::allocator<cv::Point_<float>>>=^v^v^v}64{vector<cv::Point_<float>, std::allocator<cv::Point_<float>>>=^v^v^v}88@112Q120{vector<cv::Mat, std::allocator<cv::Mat>>=^{Mat}^{Mat}^{Mat}}128{CGSize=dd}152f168"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"

```
