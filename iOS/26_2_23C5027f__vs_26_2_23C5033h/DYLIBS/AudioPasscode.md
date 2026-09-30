## AudioPasscode

> `/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode`

```diff

 65.0.0.0.0
-  __TEXT.__text: 0x1c200
+  __TEXT.__text: 0x1c214
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0xe74
   __TEXT.__const: 0x4fe0

   __TEXT.__unwind_info: 0xb90
   __TEXT.__objc_classname: 0x209
   __TEXT.__objc_methname: 0x26ee
-  __TEXT.__objc_methtype: 0xcc6
+  __TEXT.__objc_methtype: 0xd16
   __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 829EC8C5-94D9-3FC9-A215-0AE8B1DD89B6
+  UUID: B32FE2BA-99C6-3927-9F67-F1D3C7124A1B
   Functions: 583
   Symbols:   2263
   CStrings:  867
Functions:
~ __ZNSt3__16__treeINS_12__value_typeIjNS_3anyEEENS_19__map_value_compareIjS3_NS_4lessIjEELb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSF_IJEEEEEENS_4pairINS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEbEERKT_DpOT0_ : 240 -> 248
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__114__split_bufferIPhNS_9allocatorIS1_EEE13emplace_frontIJS1_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__15dequeIhNS_9allocatorIhEEE19__add_back_capacityEv : 468 -> 472
CStrings:
+ "{BufferList=\"mStorage\"{vector<char, std::allocator<char>>=\"__begin_\"*\"__end_\"*\"\"{?=\"__cap_\"*}}}"
+ "{array<std::unique_ptr<DecodedDataMessage>, 10UL>=\"__elems_\"[10{unique_ptr<DecodedDataMessage, std::default_delete<DecodedDataMessage>>=\"\"{?=\"__ptr_\"^{DecodedDataMessage}}}]}"
+ "{map<unsigned int, std::any, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, std::any>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, std::any>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, std::any>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, std::any>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<APCDecoderBase, std::default_delete<APCDecoderBase>>=\"\"{?=\"__ptr_\"^{APCDecoderBase}}}"
+ "{unique_ptr<APCDecoderBase, std::default_delete<APCDecoderBase>>={?=^{APCDecoderBase}}}40@0:8@16^v24^@32"
+ "{unique_ptr<APCEncoderBase, std::default_delete<APCEncoderBase>>=\"\"{?=\"__ptr_\"^{APCEncoderBase}}}"
+ "{unique_ptr<APCEncoderBase, std::default_delete<APCEncoderBase>>={?=^{APCEncoderBase}}}40@0:8@16^v24@32"
+ "{unique_ptr<AudioCapturerIfc, std::default_delete<AudioCapturerIfc>>=\"\"{?=\"__ptr_\"^{AudioCapturerIfc}}}"
+ "{unique_ptr<EOFReachedMessage, std::default_delete<EOFReachedMessage>>=\"\"{?=\"__ptr_\"^{EOFReachedMessage}}}"
+ "{unique_ptr<OpaqueExtAudioFile, applesauce::raii::detail::opaque_deletion_functor<OpaqueExtAudioFile *, &ExtAudioFileDispose>>=\"\"{?=\"__ptr_\"^{OpaqueExtAudioFile}}}"
+ "{unique_ptr<caulk::concurrent::messenger, std::default_delete<caulk::concurrent::messenger>>=\"\"{?=\"__ptr_\"^{messenger}}}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"\"{?=\"__cap_\"^f}}"
+ "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"\"{?=\"__cap_\"*}}"
- "{BufferList=\"mStorage\"{vector<char, std::allocator<char>>=\"__begin_\"*\"__end_\"*\"__cap_\"*}}"
- "{array<std::unique_ptr<DecodedDataMessage>, 10UL>=\"__elems_\"[10{unique_ptr<DecodedDataMessage, std::default_delete<DecodedDataMessage>>=\"__ptr_\"^{DecodedDataMessage}}]}"
- "{map<unsigned int, std::any, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, std::any>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, std::any>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, std::any>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, std::any>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<APCDecoderBase, std::default_delete<APCDecoderBase>>=\"__ptr_\"^{APCDecoderBase}}"
- "{unique_ptr<APCDecoderBase, std::default_delete<APCDecoderBase>>=^{APCDecoderBase}}40@0:8@16^v24^@32"
- "{unique_ptr<APCEncoderBase, std::default_delete<APCEncoderBase>>=\"__ptr_\"^{APCEncoderBase}}"
- "{unique_ptr<APCEncoderBase, std::default_delete<APCEncoderBase>>=^{APCEncoderBase}}40@0:8@16^v24@32"
- "{unique_ptr<AudioCapturerIfc, std::default_delete<AudioCapturerIfc>>=\"__ptr_\"^{AudioCapturerIfc}}"
- "{unique_ptr<EOFReachedMessage, std::default_delete<EOFReachedMessage>>=\"__ptr_\"^{EOFReachedMessage}}"
- "{unique_ptr<OpaqueExtAudioFile, applesauce::raii::detail::opaque_deletion_functor<OpaqueExtAudioFile *, &ExtAudioFileDispose>>=\"__ptr_\"^{OpaqueExtAudioFile}}"
- "{unique_ptr<caulk::concurrent::messenger, std::default_delete<caulk::concurrent::messenger>>=\"__ptr_\"^{messenger}}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
- "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__cap_\"*}"

```
