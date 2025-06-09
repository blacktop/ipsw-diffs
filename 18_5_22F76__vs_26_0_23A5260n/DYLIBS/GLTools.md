## GLTools

> `/System/Library/PrivateFrameworks/GLTools.framework/GLTools`

```diff

-304.7.0.0.0
-  __TEXT.__text: 0x3a28
+310.8.0.0.0
+  __TEXT.__text: 0x3840
   __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x190
-  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__gcc_except_tab: 0x128
   __TEXT.__cstring: 0x2f8
   __TEXT.__const: 0x48
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methname: 0x1047
-  __TEXT.__objc_methtype: 0x1dbd
+  __TEXT.__objc_methtype: 0x184b
   __TEXT.__objc_stubs: 0x460
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4580DE24-9315-31B0-883D-F2A6C62DA1AD
-  Functions: 76
+  UUID: 7422EEC2-8EBD-336D-830D-11B101B401A5
+  Functions: 75
   Symbols:   306
   CStrings:  132
 
Symbols:
+ __ZNSt3__110unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyNS0_IN8GPUTools8Playback2GL11ContextInfoENS_14default_deleteIS6_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEED1B8ne200100Ev
+ __ZNSt3__114__split_bufferIPNS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS7_EEE12emplace_backIJRS7_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS7_EEE12emplace_backIJS7_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS7_EEE13emplace_frontIJS7_EEEvDpOT_
+ __ZNSt3__15stackINS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_5dequeIS6_NS_9allocatorIS6_EEEEED1Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ _bzero
- __ZNSt3__110unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS2_EEED1B8ne190102Ev
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyNS0_IN8GPUTools8Playback2GL11ContextInfoENS_14default_deleteIS6_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEED1B8ne190102Ev
- __ZNSt3__114__split_bufferIPNS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS7_EEE10push_frontEOS7_
- __ZNSt3__114__split_bufferIPNS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS7_EEE9push_backEOS7_
- __ZNSt3__15dequeINS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE13__move_assignERS9_NS_17integral_constantIbLb1EEE
- __ZNSt3__15dequeINS_10unique_ptrIN8GPUTools8VMBufferENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B8ne190102Ev
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
CStrings:
+ "{unordered_map<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, std::unique_ptr<GPUTools::Playback::GL::ContextInfo>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>>=\"__value_\"f}}}"

```
