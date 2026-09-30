## CoreSceneUnderstanding

> `/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`

```diff

-69.2.0.0.0
-  __TEXT.__text: 0xbf050
-  __TEXT.__auth_stubs: 0x14b0
+76.0.0.0.0
+  __TEXT.__text: 0xc365c
+  __TEXT.__auth_stubs: 0x1490
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x387c
+  __TEXT.__objc_methlist: 0x38dc
   __TEXT.__const: 0x1f80
-  __TEXT.__gcc_except_tab: 0xebe8
-  __TEXT.__cstring: 0x8a88
-  __TEXT.__oslogstring: 0xb68
+  __TEXT.__gcc_except_tab: 0xee00
+  __TEXT.__cstring: 0x8b3d
+  __TEXT.__oslogstring: 0xc68
   __TEXT.__swift5_typeref: 0x69
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x4388
+  __TEXT.__unwind_info: 0x43f8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xb41
-  __TEXT.__objc_methname: 0xb4d5
-  __TEXT.__objc_methtype: 0x595a
-  __TEXT.__objc_stubs: 0x48c0
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x700
+  __TEXT.__objc_methname: 0xb02a
+  __TEXT.__objc_methtype: 0x3ce5
+  __TEXT.__objc_stubs: 0x4900
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_selrefs: 0x1b80
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0xa70
-  __AUTH_CONST.__const: 0x26e8
-  __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x8cd8
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__const: 0x2778
+  __AUTH_CONST.__cfstring: 0x35a0
+  __AUTH_CONST.__objc_const: 0x8d98
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78

   __AUTH.__data: 0x168
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x6a8
+  __DATA.__objc_ivar: 0x6b8
   __DATA.__data: 0x370
   __DATA.__bss: 0x1e1
   __DATA.__common: 0x3d5

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 52CA3E97-3692-36C0-B450-CFF8F9D0DD4F
-  Functions: 3012
-  Symbols:   587
-  CStrings:  3246
+  UUID: BB227CF7-25A3-31D3-8A47-B9B2413BDEBA
+  Functions: 3055
+  Symbols:   585
+  CStrings:  3280
 
Symbols:
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x9
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x2
CStrings:
+ "!5Y"
+ "@48@0:8{vector<std::vector<unsigned int>, std::allocator<std::vector<unsigned int>>>=^v^v^v}16^@40"
+ "B24@0:8q16"
+ "Cannot set backend - this platform uses precompiled models"
+ "Encountered null input while getting tokens for text %@!"
+ "No tokens generated for text - is empty or NULL %@!"
+ "SafetyNetLight_v1.1.0_vx6zphgfsp_15880_safetynet_quant"
+ "SceneNet model configuration revision is %ld"
+ "Scenenet 5.10 model is loaded"
+ "Scenenet 5.11 model is loaded"
+ "Scenenet 5.13 model is loaded"
+ "SystemSearch/v6.0.0/"
+ "TB,N,V_updated"
+ "Tq,N,V_computeUnits"
+ "Tq,N,V_defaultComputeUnits"
+ "Tq,R,N,V_backend"
+ "T{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v^v})B}@ffQiif},N,V_beamSearchOptions"
+ "T{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}},N,V_encodedFeaturesBuffer"
+ "T{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}},R,N,V_inputTokens"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},R,N,V_stateInputEspressoBuffers"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},R,N,V_stateOutputEspressoBuffers"
+ "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},R,N,V_stateInputEspressoBuffersShape"
+ "T{vector<float, std::allocator<float>>=^f^f^f},R,N,V_inWords"
+ "T{vector<float, std::allocator<float>>=^f^f^f},R,N,V_inputMask"
+ "T{vector<float, std::allocator<float>>=^f^f^f},R,N,V_positionInput"
+ "T{vector<float, std::allocator<float>>=^f^f^f},R,N,V_scaleInput"
+ "T{vector<float, std::allocator<float>>=^f^f^f},R,N,V_wordProbs"
+ "_backend"
+ "_computeUnits"
+ "_defaultComputeUnits"
+ "_updated"
+ "backend"
+ "computeUnits"
+ "defaultComputeUnits"
+ "default_compute_units"
+ "getConfigurationForRevision_v6_0_Tier0WithError:"
+ "norm_to_orig"
+ "normalized"
+ "scenenet_v5_custom_classifiers/SafetyNetLight/SafetyNetLight_v1.1.0"
+ "setDefaultComputeUnits:"
+ "setInferenceBackend:"
+ "setUpdated:"
+ "spm_omnie_v01_100k"
+ "text_md6_ctx_512_77"
+ "token_md6"
+ "updated"
+ "v112@0:8{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v^v})B}@ffQiif}16"
+ "v72@0:8{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}16"
+ "{BeamSearchOptions=\"maxSeqLen\"Q\"terminateAtEOS\"B\"maxSteps\"{optional<int>=\"\"(?=\"__null_state_\"c\"__val_\"i)\"__engaged_\"B}\"excludeTokens\"{optional<std::vector<std::string>>=\"\"(?=\"__null_state_\"c\"__val_\"{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v})\"__engaged_\"B}\"denyListRules\"@\"NSArray\"\"lengthNormalizationAlpha\"f\"lengthNormFactor\"f\"scorerType\"Q\"beamWidth\"i\"topKPerStep\"i\"lengthNormalizationAlpha\"f}"
+ "{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v^v})B}@ffQiif}16@0:8"
+ "{EspressoTensor=\"_vptr$Tensor\"^^?\"type_\"i\"shape_\"{TensorShape=\"sizes_\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}}\"storage_\"{shared_ptr<ik::TensorStorage>=\"__ptr_\"^{TensorStorage}\"__cntrl_\"^{__shared_weak_count}}}"
+ "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}16@0:8"
+ "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}24@0:8@16"
+ "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}48@0:8@16Q24Q32Q40"
+ "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}48@0:8{vector<std::vector<unsigned int>, std::allocator<std::vector<unsigned int>>>=^v^v^v}16^@40"
+ "{ModelOutput={vector<float, std::allocator<float>>=^f^f^f}{shared_ptr<std::unordered_map<std::string, std::vector<float>>>=^v^{__shared_weak_count}}B}16@0:8"
+ "{ModelOutput={vector<float, std::allocator<float>>=^f^f^f}{shared_ptr<std::unordered_map<std::string, std::vector<float>>>=^v^{__shared_weak_count}}B}36@0:8r^v16r^v24I32"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8r^v16"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{unique_ptr<ImageDescriptorProcessorHyperplaneLSH, std::default_delete<ImageDescriptorProcessorHyperplaneLSH>>=\"__ptr_\"^{ImageDescriptorProcessorHyperplaneLSH}}"
+ "{unique_ptr<csu::SentencePieceVocabulary, std::default_delete<csu::SentencePieceVocabulary>>=\"__ptr_\"^{SentencePieceVocabulary}}"
+ "{unique_ptr<ik::EspressoNet, std::default_delete<ik::EspressoNet>>=\"__ptr_\"^{EspressoNet}}"
+ "{unique_ptr<ik::PixelBufferTransfer, std::default_delete<ik::PixelBufferTransfer>>=\"__ptr_\"^{PixelBufferTransfer}}"
+ "{unordered_map<std::string, ik::EspressoTensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::EspressoTensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::EspressoTensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::EspressoTensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}Qf}}24@0:8@16"
+ "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}Qf}}40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}16"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
+ "{vector<float, std::allocator<float>>=^f^f^f}16@0:8"
+ "{vector<float, std::allocator<float>>=^f^f^f}24@0:8@16"
+ "{vector<float, std::allocator<float>>=^f^f^f}28@0:8r^v16I24"
+ "{vector<std::pair<NSString *, unsigned long>, std::allocator<std::pair<NSString *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}40@0:8@16B24B28^@32"
- "!59"
- "@48@0:8{vector<std::vector<unsigned int>, std::allocator<std::vector<unsigned int>>>=^v^v{__compressed_pair<std::vector<unsigned int> *, std::allocator<std::vector<unsigned int>>>=^v}}16^@40"
- "OK"
- "SafetyNetLight_v1.0.0_39v8f3cmqe_1320"
- "T{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}})B}@ffQiif},N,V_beamSearchOptions"
- "T{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}},N,V_encodedFeaturesBuffer"
- "T{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}},R,N,V_inputTokens"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}},R,N,V_stateInputEspressoBuffers"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}},R,N,V_stateOutputEspressoBuffers"
- "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=Q}}},R,N,V_stateInputEspressoBuffersShape"
- "T{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}},R,N,V_inWords"
- "T{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}},R,N,V_inputMask"
- "T{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}},R,N,V_positionInput"
- "T{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}},R,N,V_scaleInput"
- "T{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}},R,N,V_wordProbs"
- "getConfigurationForRevision_v5_0_Tier0WithError:"
- "scenenet_v5_custom_classifiers/SafetyNetLight/SafetyNetLight_v1.0.0"
- "text_model_ctx_512_77"
- "token_model_md5_mubb_enum"
- "v112@0:8{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}})B}@ffQiif}16"
- "v72@0:8{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}16"
- "{BeamSearchOptions=\"maxSeqLen\"Q\"terminateAtEOS\"B\"maxSteps\"{optional<int>=\"\"(?=\"__null_state_\"c\"__val_\"i)\"__engaged_\"B}\"excludeTokens\"{optional<std::vector<std::string>>=\"\"(?=\"__null_state_\"c\"__val_\"{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}})\"__engaged_\"B}\"denyListRules\"@\"NSArray\"\"lengthNormalizationAlpha\"f\"lengthNormFactor\"f\"scorerType\"Q\"beamWidth\"i\"topKPerStep\"i\"lengthNormalizationAlpha\"f}"
- "{BeamSearchOptions=QB{optional<int>=(?=ci)B}{optional<std::vector<std::string>>=(?=c{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}})B}@ffQiif}16@0:8"
- "{EspressoTensor=\"_vptr$Tensor\"^^?\"type_\"i\"shape_\"{TensorShape=\"sizes_\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}}\"storage_\"{shared_ptr<ik::TensorStorage>=\"__ptr_\"^{TensorStorage}\"__cntrl_\"^{__shared_weak_count}}}"
- "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}16@0:8"
- "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}24@0:8@16"
- "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}48@0:8@16Q24Q32Q40"
- "{EspressoTensor=^^?i{TensorShape={vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}}{shared_ptr<ik::TensorStorage>=^{TensorStorage}^{__shared_weak_count}}}48@0:8{vector<std::vector<unsigned int>, std::allocator<std::vector<unsigned int>>>=^v^v{__compressed_pair<std::vector<unsigned int> *, std::allocator<std::vector<unsigned int>>>=^v}}16^@40"
- "{ModelOutput={vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{shared_ptr<std::unordered_map<std::string, std::vector<float>>>=^v^{__shared_weak_count}}B}16@0:8"
- "{ModelOutput={vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{shared_ptr<std::unordered_map<std::string, std::vector<float>>>=^v^{__shared_weak_count}}B}36@0:8r^v16r^v24I32"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@0:8r^v16"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}}16@0:8"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=Q}}}16@0:8"
- "{unique_ptr<ImageDescriptorProcessorHyperplaneLSH, std::default_delete<ImageDescriptorProcessorHyperplaneLSH>>=\"__ptr_\"{__compressed_pair<ImageDescriptorProcessorHyperplaneLSH *, std::default_delete<ImageDescriptorProcessorHyperplaneLSH>>=\"__value_\"^{ImageDescriptorProcessorHyperplaneLSH}}}"
- "{unique_ptr<csu::SentencePieceVocabulary, std::default_delete<csu::SentencePieceVocabulary>>=\"__ptr_\"{__compressed_pair<csu::SentencePieceVocabulary *, std::default_delete<csu::SentencePieceVocabulary>>=\"__value_\"^{SentencePieceVocabulary}}}"
- "{unique_ptr<ik::EspressoNet, std::default_delete<ik::EspressoNet>>=\"__ptr_\"{__compressed_pair<ik::EspressoNet *, std::default_delete<ik::EspressoNet>>=\"__value_\"^{EspressoNet}}}"
- "{unique_ptr<ik::PixelBufferTransfer, std::default_delete<ik::PixelBufferTransfer>>=\"__ptr_\"{__compressed_pair<ik::PixelBufferTransfer *, std::default_delete<ik::PixelBufferTransfer>>=\"__value_\"^{PixelBufferTransfer}}}"
- "{unordered_map<std::string, ik::EspressoTensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::EspressoTensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::EspressoTensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::EspressoTensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::EspressoTensor>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::EspressoTensor>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=Q}}}}{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *>>>={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>>=Q}{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>>=f}}}24@0:8@16"
- "{unordered_map<std::string, ik::Tensor, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, ik::Tensor>>>={__hash_table<std::__hash_value_type<std::string, ik::Tensor>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, ik::Tensor>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>={__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>={__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *> *>>=Q}}}}{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *>>>={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, ik::Tensor>, void *> *>=^v}}{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::hash<std::string>, std::equal_to<std::string>>>=Q}{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, ik::Tensor>, std::equal_to<std::string>, std::hash<std::string>>>=f}}}40@0:8{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}16"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}16@0:8"
- "{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}24@0:8@16"
- "{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}28@0:8r^v16I24"
- "{vector<std::pair<NSString *, unsigned long>, std::allocator<std::pair<NSString *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<NSString *, unsigned long> *, std::allocator<std::pair<NSString *, unsigned long>>>=\"__value_\"^v}}"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}40@0:8@16B24B28^@32"

```
