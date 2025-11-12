## MentalHealthDaemon

> `/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x1973c
+6200.3.8.0.0
+  __TEXT.__text: 0x19744
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_methlist: 0x164c
   __TEXT.__const: 0x44a

   __TEXT.__unwind_info: 0x798
   __TEXT.__objc_classname: 0x5dc
   __TEXT.__objc_methname: 0x4ad6
-  __TEXT.__objc_methtype: 0x12d7
+  __TEXT.__objc_methtype: 0x12f5
   __TEXT.__objc_stubs: 0x33e0
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0x4d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9186B061-CFE4-3E13-A48B-45B7A3E8F4FD
+  UUID: DAB96896-4676-3D7C-A109-D039CF3FDBA7
   Functions: 549
   Symbols:   2083
   CStrings:  1041
Symbols:
+ ___42-[HDMHSOMNotificationManager _queue_start]_block_invoke.319
+ ___63-[HDMHSOMNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.326
+ ___71-[HDMHAssessmentsNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.327
+ ___block_literal_global.316
+ ___block_literal_global.337
- ___42-[HDMHSOMNotificationManager _queue_start]_block_invoke.310
- ___63-[HDMHSOMNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.317
- ___71-[HDMHAssessmentsNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.318
- ___block_literal_global.307
- ___block_literal_global.319
Functions:
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIlU8__strongP16_HDMHDomainCountEENS_22__unordered_map_hasherIlS5_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIlJRKNS_21piecewise_construct_tENS_5tupleIJOlEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 604 -> 608
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIlU8__strongP16_HDMHDomainCountEENS_22__unordered_map_hasherIlS5_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIlJRKNS_4pairIKlS4_EEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 612 -> 616
CStrings:
+ "{unordered_map<long, _HDMHDomainCount *, std::hash<long>, std::equal_to<long>, std::allocator<std::pair<const long, _HDMHDomainCount *>>>=\"__table_\"{__hash_table<std::__hash_value_type<long, _HDMHDomainCount *>, std::__unordered_map_hasher<long, std::__hash_value_type<long, _HDMHDomainCount *>, std::hash<long>, std::equal_to<long>>, std::__unordered_map_equal<long, std::__hash_value_type<long, _HDMHDomainCount *>, std::equal_to<long>, std::hash<long>>, std::allocator<std::__hash_value_type<long, _HDMHDomainCount *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<long, _HDMHDomainCount *, std::hash<long>, std::equal_to<long>, std::allocator<std::pair<const long, _HDMHDomainCount *>>>=\"__table_\"{__hash_table<std::__hash_value_type<long, _HDMHDomainCount *>, std::__unordered_map_hasher<long, std::__hash_value_type<long, _HDMHDomainCount *>, std::hash<long>, std::equal_to<long>>, std::__unordered_map_equal<long, std::__hash_value_type<long, _HDMHDomainCount *>, std::equal_to<long>, std::hash<long>>, std::allocator<std::__hash_value_type<long, _HDMHDomainCount *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long, _HDMHDomainCount *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"

```
