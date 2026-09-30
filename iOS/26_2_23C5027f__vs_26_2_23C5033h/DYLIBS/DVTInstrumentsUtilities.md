## DVTInstrumentsUtilities

> `/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities`

```diff

-64572.193.1.0.0
-  __TEXT.__text: 0x2c0a0
+64573.4.1.0.0
+  __TEXT.__text: 0x2c0cc
   __TEXT.__auth_stubs: 0x13d0
   __TEXT.__objc_methlist: 0x2ec4
   __TEXT.__const: 0x126c

   __TEXT.__eh_frame: 0x1c8
   __TEXT.__objc_classname: 0xac6
   __TEXT.__objc_methname: 0x5871
-  __TEXT.__objc_methtype: 0x1bc3
+  __TEXT.__objc_methtype: 0x1c11
   __TEXT.__objc_stubs: 0x43c0
   __DATA_CONST.__got: 0x558
   __DATA_CONST.__const: 0x2248

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 74493D03-4787-3A9E-B5D9-BC59AD285A52
+  UUID: C8F8D01C-372B-3908-BAD0-A1B7C26049CF
   Functions: 1335
   Symbols:   572
   CStrings:  3700
Functions:
~ sub_249112700 -> sub_249308700 : 1088 -> 1108
~ sub_24912c094 -> sub_2493220a8 : 604 -> 608
~ sub_24912c678 -> sub_249322690 : 604 -> 608
~ sub_24912d0c8 -> sub_2493230e4 : 188 -> 192
~ sub_2491331ac -> sub_2493291cc : 336 -> 340
~ sub_2491332fc -> sub_249329320 : 436 -> 440
~ sub_2491345ec -> sub_24932a614 : 60 -> 64
~ sub_2491346f8 -> sub_24932a724 : 60 -> 64
~ sub_249134838 -> sub_24932a868 : 484 -> 480
CStrings:
+ "{XRIndexSetImpl<unsigned long long, 4, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"_ranges\"{multiset<xray::internal::RangeImp<unsigned long long>, std::less<xray::internal::RangeImp<unsigned long long>>, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"__tree_\"{__tree<xray::internal::RangeImp<unsigned long long>, std::less<xray::internal::RangeImp<unsigned long long>>, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"_cache\"{array<xray::internal::RangeImp<unsigned long long>, 4UL>=\"__elems_\"[4{RangeImp<unsigned long long>=\"first\"Q\"last\"Q}]}\"_cacheIsValid\"B}"
+ "{unique_ptr<xray::scheduler::Commutator, std::default_delete<xray::scheduler::Commutator>>=\"\"{?=\"__ptr_\"^{Commutator}}}"
+ "{unordered_map<unsigned long long, id, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, id>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, id>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, id>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_set<const void *, std::hash<const void *>, std::equal_to<const void *>, std::allocator<const void *>>=\"__table_\"{__hash_table<const void *, std::hash<const void *>, std::equal_to<const void *>, std::allocator<const void *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<const void *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<const void *, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<const void *, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<const void *, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{XRIndexSetImpl<unsigned long long, 4, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"_ranges\"{multiset<xray::internal::RangeImp<unsigned long long>, std::less<xray::internal::RangeImp<unsigned long long>>, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"__tree_\"{__tree<xray::internal::RangeImp<unsigned long long>, std::less<xray::internal::RangeImp<unsigned long long>>, std::allocator<xray::internal::RangeImp<unsigned long long>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}\"_cache\"{array<xray::internal::RangeImp<unsigned long long>, 4UL>=\"__elems_\"[4{RangeImp<unsigned long long>=\"first\"Q\"last\"Q}]}\"_cacheIsValid\"B}"
- "{unique_ptr<xray::scheduler::Commutator, std::default_delete<xray::scheduler::Commutator>>=\"__ptr_\"^{Commutator}}"
- "{unordered_map<unsigned long long, id, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, id>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, id>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, id>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, id>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, id>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_set<const void *, std::hash<const void *>, std::equal_to<const void *>, std::allocator<const void *>>=\"__table_\"{__hash_table<const void *, std::hash<const void *>, std::equal_to<const void *>, std::allocator<const void *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<const void *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<const void *, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<const void *, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<const void *, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"

```
