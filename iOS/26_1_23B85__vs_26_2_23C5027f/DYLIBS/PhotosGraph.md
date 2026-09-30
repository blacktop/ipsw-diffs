## PhotosGraph

> `/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph`

```diff

-812.40.117.0.0
-  __TEXT.__text: 0x63fd90
+820.0.140.0.0
+  __TEXT.__text: 0x63fddc
   __TEXT.__auth_stubs: 0x4ae0
   __TEXT.__objc_methlist: 0x2c1f4
   __TEXT.__const: 0x1d5e8

   __TEXT.__eh_frame: 0x10c1c
   __TEXT.__objc_classname: 0x8866
   __TEXT.__objc_methname: 0x6c93d
-  __TEXT.__objc_methtype: 0x8451
+  __TEXT.__objc_methtype: 0x8493
   __TEXT.__objc_stubs: 0x38f80
   __DATA_CONST.__got: 0x3bc0
   __DATA_CONST.__const: 0xd450

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E421366C-787B-34D2-B54B-6BF8D610F8C1
+  UUID: EB61CCA3-0B48-3160-9317-C8F44AF01AB1
   Functions: 26757
   Symbols:   56599
   CStrings:  30350
Functions:
~ sub_22f15d3d0 -> sub_23000a3d0 : 312 -> 300
~ sub_22f15d570 -> sub_23000a564 : 372 -> 360
~ sub_22f196f00 -> sub_230043ee8 : 920 -> 916
~ sub_22f197298 -> sub_23004427c : 1072 -> 1064
~ sub_22f1dd83c -> sub_23008a818 : 2300 -> 2332
~ sub_22f1de30c -> sub_23008b308 : 3780 -> 3812
~ sub_22f254fb4 -> sub_230101fd0 : 3724 -> 3748
~ sub_22f28ac68 -> sub_230137c9c : 2972 -> 2892
~ sub_22f2a9d58 -> sub_230156d3c : 1244 -> 1352
~ sub_22f2cb144 -> sub_230178194 : 6240 -> 6268
~ sub_22f2ce2c8 -> sub_23017b334 : 1336 -> 1228
~ sub_22f35275c -> sub_2301ff75c : 1124 -> 1128
~ sub_22f369d80 -> sub_230216d84 : 2112 -> 2152
~ sub_22f36daec -> sub_23021ab18 : 2296 -> 2300
~ sub_22f36e3e4 -> sub_23021b414 : 2200 -> 2280
~ sub_22f390c5c -> sub_23023dcdc : 6300 -> 6216
~ sub_22f3a1c30 -> sub_23024ec5c : 8488 -> 8484
~ sub_22f3a43ac -> sub_2302513d4 : 2680 -> 2684
~ sub_22f3ab520 -> sub_23025854c : 2856 -> 2844
~ sub_22f3af418 -> sub_23025c438 : 4048 -> 4072
~ sub_22f3d668c -> sub_2302836c4 : 2624 -> 2652
~ sub_22f3d70cc -> sub_230284120 : 3752 -> 3768
~ -[PGEventLabelerE5Model initWithFilePath:error:] : 3248 -> 3212
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN4E5RT6IOPortEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE14__assign_multiINS_21__hash_const_iteratorIPNS_11__hash_nodeISC_PvEEEEEEvT_SU_ : 380 -> 384
~ __ZNKSt3__120__shared_ptr_pointerIPN4E5RT12BufferObjectENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 64 -> 68
~ __ZNKSt3__120__shared_ptr_pointerIPN4E5RT24ExecutionStreamOperationENS_14default_deleteIS2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 64 -> 68
CStrings:
+ "{unique_ptr<E5RT::ExecutionStream, std::default_delete<E5RT::ExecutionStream>>=\"\"{?=\"__ptr_\"^{ExecutionStream}}}"
+ "{unordered_map<std::string, std::shared_ptr<E5RT::BufferObject>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<E5RT::BufferObject>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<std::string, std::shared_ptr<E5RT::IOPort>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<E5RT::IOPort>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unique_ptr<E5RT::ExecutionStream, std::default_delete<E5RT::ExecutionStream>>=\"__ptr_\"^{ExecutionStream}}"
- "{unordered_map<std::string, std::shared_ptr<E5RT::BufferObject>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<E5RT::BufferObject>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::BufferObject>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<std::string, std::shared_ptr<E5RT::IOPort>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<E5RT::IOPort>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<E5RT::IOPort>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"

```
