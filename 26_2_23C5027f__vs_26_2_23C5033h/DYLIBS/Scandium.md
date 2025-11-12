## Scandium

> `/System/Library/PrivateFrameworks/Scandium.framework/Scandium`

```diff

 85.0.0.0.0
-  __TEXT.__text: 0x27058
+  __TEXT.__text: 0x27078
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x290
   __TEXT.__const: 0x3020

   __TEXT.__unwind_info: 0xd38
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methname: 0x9ce
-  __TEXT.__objc_methtype: 0x28d
+  __TEXT.__objc_methtype: 0x293
   __TEXT.__objc_stubs: 0x860
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCC828E9-8492-3F8E-BEF0-1D24C6670408
+  UUID: 26E31932-7AA5-37B7-B960-CBBACC8C4B50
   Functions: 664
   Symbols:   2015
   CStrings:  754
Functions:
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN8Scandium11ScandiumPPG30scandium_signal_conditioning_t7processENS1_12module_inputERNS1_13module_outputE : 716 -> 720
~ __ZN8Scandium11sort_medianEPKfi : 596 -> 600
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_7variantIJbixfdS7_NS8_IJNS_6vectorIbNS5_IbEEEENS9_IiNS5_IiEEEENS9_IxNS5_IxEEEENS9_IfNS5_IfEEEENS9_IdNS5_IdEEEENS9_IS7_NS5_IS7_EEEEEEEEEEEENS_22__unordered_map_hasherIS7_SO_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SO_ST_SR_Lb1EEENS5_ISO_EEE25__emplace_unique_key_argsIS7_JRKNS_4pairIKS7_SN_EEEEENS10_INS_15__hash_iteratorIPNS_11__hash_nodeISO_PvEEEEbEERKT_DpOT0_ : 604 -> 608
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em : 68 -> 72
~ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__120back_insert_iteratorINS_6vectorIfNS_9allocatorIfEEEEEaSB8ne200100EOf : 240 -> 244
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN8Scandium11ScandiumPPG25channel_combination_ret_tENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_22__unordered_map_hasherIS4_SB_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SB_SG_SE_Lb1EEENS8_ISB_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS4_EEENSQ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISB_PvEEEEbEERKT_DpOT0_ : 604 -> 612
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZN8Scandium11ScandiumPPG14scandium_bga_t17compute_ppg_snipsERKNSt3__16vectorIfNS2_9allocatorIfEEEERNS0_7beats_tENS0_12beats_info_tERNS0_5BGA_tERNS3_IbNS4_IbEEEENS0_11led_color_tE : 1076 -> 1068
~ __ZN8Scandium25scandium_mvmt_detection_t11processMvmtERKNSt3__15arrayINS2_IfLm960EEELm3EEEjjf : 508 -> 512
CStrings:
+ "{unique_ptr<scandium::Processor, std::default_delete<scandium::Processor>>=\"\"{?=\"__ptr_\"^{Processor}}}"
- "{unique_ptr<scandium::Processor, std::default_delete<scandium::Processor>>=\"__ptr_\"^{Processor}}"

```
