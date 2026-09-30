## LocalAuthenticationPrivateUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`

```diff

-2005.60.8.0.0
-  __TEXT.__text: 0x331e4
+2005.60.9.0.0
+  __TEXT.__text: 0x3323c
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x1c18
   __TEXT.__const: 0x9a0

   __TEXT.__unwind_info: 0x1480
   __TEXT.__objc_classname: 0x48d
   __TEXT.__objc_methname: 0x5040
-  __TEXT.__objc_methtype: 0x1794
+  __TEXT.__objc_methtype: 0x17c4
   __TEXT.__objc_stubs: 0x4c40
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x708

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71ABE411-BE5C-3180-A7A4-5199AEA2FE43
+  UUID: E1ACEAF4-B9AC-3580-A5A2-A5CD2FC86C1D
   Functions: 1065
   Symbols:   4043
   CStrings:  1632
Functions:
~ -[LAUIPearlGlyphLabel _updateText] : 1448 -> 1452
~ __ZNSt3__16vectorIU8__strongP6UIViewNS_9allocatorIS3_EEE13shrink_to_fitEv : 200 -> 196
~ __ZNSt3__16__treeINS_12__value_typeIP7CALayerU8__strongS3_EENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSI_IJEEEEEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_ : 236 -> 244
~ __ZN36LAUI_uniform_cubic_b_spline_renderer10renderer_t12add_instanceERKNS_20indexed_identifier_tINS_8spline_tEJEEERKNS2_10instance_tERKNS6_7state_tE : 892 -> 876
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer10renderer_t9buffers_tENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 336 -> 340
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer10renderer_t18spline_container_tENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS1_20indexed_identifier_tINS1_8spline_tEJEEERKS9_RKNS_4spanIN44LAUI_uniform_cubic_b_spline_renderer_private13control_pointELm18446744073709551615EEERKNS9_7state_tEEEEPS3_DpOT_ : 380 -> 392
~ __ZN17LAUI_CA_utilities38animation_completion_handler_container7executeERNSt3__16vectorIS0_NS1_9allocatorIS0_EEEEb : 384 -> 388
~ -[LAUICheckmarkLayer _updateRevealedAnimated:] : 1200 -> 1204
~ __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE13shrink_to_fitEv : 244 -> 256
~ __ZNSt3__16vectorIU8__strongP12CAShapeLayerNS_9allocatorIS3_EEE13shrink_to_fitEv : 200 -> 196
~ __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN17LAUI_CA_utilities38animation_completion_handler_containerENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRU8__strongU13block_pointerFvbEEEEPS2_DpOT_ : 268 -> 272
~ -[LAUIPearlGlyphView initWithConfiguration:] : 6428 -> 6432
~ __ZNSt3__16vectorIU8__strongU13block_pointerFvbENS_9allocatorIS3_EEE13shrink_to_fitEv : 200 -> 196
~ __ZNSt3__16vectorIN12_GLOBAL__N_118face_id_animator_t14ring_context_tENS_9allocatorIS3_EEE12emplace_backIJNS3_14static_state_tERNS1_15face_id_state_tEEEERS3_DpOT_ : 340 -> 348
~ __ZZN12_GLOBAL__N_118face_id_animator_tC1ERN36LAUI_uniform_cubic_b_spline_renderer10renderer_tE23LAUIPearlGlyphPathStylefRKNS_15face_id_state_tEENKUlNS_10quadrant_tEE_clES8_ : 2836 -> 2840
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer8spline_t7state_tENS_9allocatorIS3_EEE7reserveEm : 220 -> 236
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer8spline_t7state_tENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJNS0_IDv3_fNS4_IS8_EEEEEEEPS3_DpOT_ : 340 -> 344
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer20indexed_identifier_tINS1_8spline_t10instance_tEJS3_EEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer10animator_tIDv3_fLNS1_27animator_interpolation_typeE0EEENS_9allocatorIS5_EEE7reserveEm : 220 -> 236
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN36LAUI_uniform_cubic_b_spline_renderer10animator_tIDv3_fLNS1_27animator_interpolation_typeE0EEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_ : 324 -> 328
~ -[LAUISecureFaceIDView _isFullyVisible] : 128 -> 124
~ -[LAUIPearlGlyphStaticConfiguration _init] : 88 -> 84
~ -[LAUIPearlGlyphView _executeCompletionHandlers:] : 124 -> 120
~ -[LAUIPearlGlyphView setModelTransform:] : 92 -> 100
CStrings:
+ "{map<CALayer *__unsafe_unretained, CALayer *, std::less<CALayer *__unsafe_unretained>, std::allocator<std::pair<CALayer *const __unsafe_unretained, CALayer *>>>=\"__tree_\"{__tree<std::__value_type<CALayer *__unsafe_unretained, CALayer *>, std::__map_value_compare<CALayer *__unsafe_unretained, std::__value_type<CALayer *__unsafe_unretained, CALayer *>, std::less<CALayer *__unsafe_unretained>>, std::allocator<std::__value_type<CALayer *__unsafe_unretained, CALayer *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<(anonymous namespace)::face_id_animator_t, std::default_delete<(anonymous namespace)::face_id_animator_t>>=\"\"{?=\"__ptr_\"^{face_id_animator_t}}}"
+ "{unique_ptr<LAUI_uniform_cubic_b_spline_renderer::renderer_t, std::default_delete<LAUI_uniform_cubic_b_spline_renderer::renderer_t>>=\"\"{?=\"__ptr_\"^{renderer_t}}}"
+ "{vector<CAShapeLayer *, std::allocator<CAShapeLayer *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<LAUI_CA_utilities::animation_completion_handler_container, std::allocator<LAUI_CA_utilities::animation_completion_handler_container>>=\"__begin_\"^{animation_completion_handler_container}\"__end_\"^{animation_completion_handler_container}\"\"{?=\"__cap_\"^{animation_completion_handler_container}}}"
+ "{vector<UIView *, std::allocator<UIView *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<void (^)(bool), std::allocator<void (^)(bool)>>=\"__begin_\"^@?\"__end_\"^@?\"\"{?=\"__cap_\"^@?}}"
- "{map<CALayer *__unsafe_unretained, CALayer *, std::less<CALayer *__unsafe_unretained>, std::allocator<std::pair<CALayer *const __unsafe_unretained, CALayer *>>>=\"__tree_\"{__tree<std::__value_type<CALayer *__unsafe_unretained, CALayer *>, std::__map_value_compare<CALayer *__unsafe_unretained, std::__value_type<CALayer *__unsafe_unretained, CALayer *>, std::less<CALayer *__unsafe_unretained>>, std::allocator<std::__value_type<CALayer *__unsafe_unretained, CALayer *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<(anonymous namespace)::face_id_animator_t, std::default_delete<(anonymous namespace)::face_id_animator_t>>=\"__ptr_\"^{face_id_animator_t}}"
- "{unique_ptr<LAUI_uniform_cubic_b_spline_renderer::renderer_t, std::default_delete<LAUI_uniform_cubic_b_spline_renderer::renderer_t>>=\"__ptr_\"^{renderer_t}}"
- "{vector<CAShapeLayer *, std::allocator<CAShapeLayer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<LAUI_CA_utilities::animation_completion_handler_container, std::allocator<LAUI_CA_utilities::animation_completion_handler_container>>=\"__begin_\"^{animation_completion_handler_container}\"__end_\"^{animation_completion_handler_container}\"__cap_\"^{animation_completion_handler_container}}"
- "{vector<UIView *, std::allocator<UIView *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<void (^)(bool), std::allocator<void (^)(bool)>>=\"__begin_\"^@?\"__end_\"^@?\"__cap_\"^@?}"

```
