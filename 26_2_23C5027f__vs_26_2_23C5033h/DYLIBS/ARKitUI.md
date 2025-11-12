## ARKitUI

> `/System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI`

```diff

 738.60.1.0.0
-  __TEXT.__text: 0x29cdc
+  __TEXT.__text: 0x29cf4
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x28a0
   __TEXT.__const: 0x96c
   __TEXT.__oslogstring: 0x1917
   __TEXT.__cstring: 0xdb9
-  __TEXT.__gcc_except_tab: 0xd44
+  __TEXT.__gcc_except_tab: 0xd40
   __TEXT.__unwind_info: 0xc20
   __TEXT.__objc_classname: 0x635
   __TEXT.__objc_methname: 0x8126
-  __TEXT.__objc_methtype: 0x1ea0
+  __TEXT.__objc_methtype: 0x1ee2
   __TEXT.__objc_stubs: 0x6d20
   __DATA_CONST.__got: 0x588
   __DATA_CONST.__const: 0x3a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B289BCF9-F60A-3E51-BAF4-8CAB48C4C8BD
+  UUID: 194C2A97-69D3-33F5-8409-2F5F49B0349B
   Functions: 976
   Symbols:   4150
   CStrings:  2173
Functions:
~ -[ARSCNPlaneGeometry updateFromPlaneGeometry:] : 932 -> 940
~ -[GTMeshData findIndexOrPushVertex:] : 452 -> 448
~ -[ARCoachingMetalSplineData recordState] : 692 -> 696
~ -[ARCoachingMetalSplineData shapeBlendWithStart:startCount:end:endCount:t:] : 468 -> 480
~ __ZNSt3__16vectorI22ARCoachingControlPointNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
CStrings:
+ "{unordered_map<GTVertexData, unsigned int, std::hash<GTVertexData>, std::equal_to<GTVertexData>, std::allocator<std::pair<const GTVertexData, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<GTVertexData, unsigned int>, std::__unordered_map_hasher<GTVertexData, std::__hash_value_type<GTVertexData, unsigned int>, std::hash<GTVertexData>, std::equal_to<GTVertexData>>, std::__unordered_map_equal<GTVertexData, std::__hash_value_type<GTVertexData, unsigned int>, std::equal_to<GTVertexData>, std::hash<GTVertexData>>, std::allocator<std::__hash_value_type<GTVertexData, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<ARCoachingControlPoint, std::allocator<ARCoachingControlPoint>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}"
+ "{vector<ARCoachingPatchData, std::allocator<ARCoachingPatchData>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}"
+ "{vector<GTVertexData, std::allocator<GTVertexData>>=\"__begin_\"^{GTVertexData}\"__end_\"^{GTVertexData}\"\"{?=\"__cap_\"^{GTVertexData}}}"
+ "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}"
+ "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}"
- "{unordered_map<GTVertexData, unsigned int, std::hash<GTVertexData>, std::equal_to<GTVertexData>, std::allocator<std::pair<const GTVertexData, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<GTVertexData, unsigned int>, std::__unordered_map_hasher<GTVertexData, std::__hash_value_type<GTVertexData, unsigned int>, std::hash<GTVertexData>, std::equal_to<GTVertexData>>, std::__unordered_map_equal<GTVertexData, std::__hash_value_type<GTVertexData, unsigned int>, std::equal_to<GTVertexData>, std::hash<GTVertexData>>, std::allocator<std::__hash_value_type<GTVertexData, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<GTVertexData, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<ARCoachingControlPoint, std::allocator<ARCoachingControlPoint>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
- "{vector<ARCoachingPatchData, std::allocator<ARCoachingPatchData>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
- "{vector<GTVertexData, std::allocator<GTVertexData>>=\"__begin_\"^{GTVertexData}\"__end_\"^{GTVertexData}\"__cap_\"^{GTVertexData}}"
- "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
- "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}"

```
