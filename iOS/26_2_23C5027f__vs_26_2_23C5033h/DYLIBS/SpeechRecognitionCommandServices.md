## SpeechRecognitionCommandServices

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices`

```diff

-3.1.95.5.0
-  __TEXT.__text: 0xf3ce4
+3.1.95.6.0
+  __TEXT.__text: 0xf3e40
   __TEXT.__auth_stubs: 0x17a0
   __TEXT.__objc_methlist: 0xe44
   __TEXT.__const: 0x7d0c
   __TEXT.__cstring: 0x22477
-  __TEXT.__gcc_except_tab: 0x59c4
+  __TEXT.__gcc_except_tab: 0x59d0
   __TEXT.__oslogstring: 0x40c
   __TEXT.__ustring: 0x13c
   __TEXT.__swift5_typeref: 0x8d6

   __TEXT.__unwind_info: 0x2d90
   __TEXT.__eh_frame: 0xcec
   __TEXT.__objc_classname: 0x17b
-  __TEXT.__objc_methname: 0x3b41
-  __TEXT.__objc_methtype: 0xa5b
+  __TEXT.__objc_methname: 0x3b60
+  __TEXT.__objc_methtype: 0xa87
   __TEXT.__objc_stubs: 0x2940
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x438

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9D39B9D6-60F2-33BC-814C-6169E4A9DCE2
-  Functions: 2815
-  Symbols:   6544
+  UUID: 3770EAA1-98CF-372E-85D3-3804F1B7E776
+  Functions: 2816
+  Symbols:   6547
   CStrings:  3987
 
Symbols:
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table59
+ __ZN9CMDPTokenC1ENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEyyydbb
+ __ZNSt3__111make_uniqueB8ne200100I9CMDPTokenJRNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERdS9_S9_S9_RbSA_ELi0EEENS_10unique_ptrIT_NS_14default_deleteISC_EEEEDpOT0_
+ _objc_msgSend$setExecutionCompleted:
+ _objc_msgSend$setExecutionCompletionDeterminedBySpokenCommandItself:
- GCC_except_table41
- GCC_except_table54
- GCC_except_table58
- __ZN9CMDPTokenC1ENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEddddbb
- _objc_msgSend$setCompletionDeterminedManually:
- _objc_msgSend$setExecuting:
CStrings:
+ "setExecutionCompleted:"
+ "setExecutionCompletionDeterminedBySpokenCommandItself:"
+ "{set<std::string, std::less<std::string>, std::allocator<std::string>>=\"__tree_\"{__tree<std::string, std::less<std::string>, std::allocator<std::string>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<CMDPNormalizer, std::default_delete<CMDPNormalizer>>=\"\"{?=\"__ptr_\"^{CMDPNormalizer}}}"
+ "{unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>, std::default_delete<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{vector<std::pair<std::string, std::unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>, std::allocator<std::pair<std::string, std::unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::unique_ptr<CMDPToken>, std::allocator<std::unique_ptr<CMDPToken>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::vector<std::vector<std::unique_ptr<CMDPToken>>>, std::allocator<std::vector<std::vector<std::unique_ptr<CMDPToken>>>>>=^v^v{?=^v}}24@0:8@16"
+ "{vector<std::vector<std::vector<std::unique_ptr<CMDPToken>>>, std::allocator<std::vector<std::vector<std::unique_ptr<CMDPToken>>>>>=^v^v{?=^v}}24@0:8^{__CFArray=}16"
- "setCompletionDeterminedManually:"
- "setExecuting:"
- "{set<std::string, std::less<std::string>, std::allocator<std::string>>=\"__tree_\"{__tree<std::string, std::less<std::string>, std::allocator<std::string>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<CMDPNormalizer, std::default_delete<CMDPNormalizer>>=\"__ptr_\"^{CMDPNormalizer}}"
- "{unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>, std::default_delete<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>=\"__ptr_\"^v}"
- "{vector<std::pair<std::string, std::unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>, std::allocator<std::pair<std::string, std::unique_ptr<fst::VectorFst<fst::ArcTpl<fst::TropicalWeightTpl<float>>>>>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::unique_ptr<CMDPToken>, std::allocator<std::unique_ptr<CMDPToken>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::vector<std::vector<std::unique_ptr<CMDPToken>>>, std::allocator<std::vector<std::vector<std::unique_ptr<CMDPToken>>>>>=^v^v^v}24@0:8@16"
- "{vector<std::vector<std::vector<std::unique_ptr<CMDPToken>>>, std::allocator<std::vector<std::vector<std::unique_ptr<CMDPToken>>>>>=^v^v^v}24@0:8^{__CFArray=}16"

```
