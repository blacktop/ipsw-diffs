## speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

-3515.11.1.0.0
-  __TEXT.__text: 0x23ef8
+3520.87.3.1.5
+  __TEXT.__text: 0x24ef4
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_stubs: 0x32c0
   __TEXT.__objc_methlist: 0xebc
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x3372
-  __TEXT.__cstring: 0x1d88
+  __TEXT.__objc_classname: 0x280
+  __TEXT.__objc_methname: 0x337a
+  __TEXT.__objc_methtype: 0x1691
+  __TEXT.__const: 0x108
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_reflstr: 0x8
   __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__cstring: 0x1f79
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x36c4
-  __TEXT.__objc_classname: 0x271
-  __TEXT.__objc_methtype: 0x1671
+  __TEXT.__gcc_except_tab: 0x36a0
   __TEXT.__oslogstring: 0x20c8
   __TEXT.__ustring: 0xec
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x838
   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 22E56D8A-70B7-379F-A419-79E6CBC292D8
+  UUID: 6A6C17FC-206B-30F6-9713-4DF530B88FE9
   Functions: 353
   Symbols:   293
-  CStrings:  1501
+  CStrings:  1499
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x7
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "SRAudioDecoder"
+ "{unordered_map<int, float, std::hash<int>, std::equal_to<int>, std::allocator<std::pair<const int, float>>>=\"__table_\"{__hash_table<std::__hash_value_type<int, float>, std::__unordered_map_hasher<int, std::pair<const int, float>, std::hash<int>, std::equal_to<int>>, std::__unordered_map_equal<int, std::pair<const int, float>, std::equal_to<int>, std::hash<int>>, std::allocator<std::pair<const int, float>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<std::string, unsigned long, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, unsigned long>, std::__unordered_map_hasher<std::string, std::pair<const std::string, unsigned long>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, unsigned long>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<int, float, std::hash<int>, std::equal_to<int>, std::allocator<std::pair<const int, float>>>=\"__table_\"{__hash_table<std::__hash_value_type<int, float>, std::__unordered_map_hasher<int, std::__hash_value_type<int, float>, std::hash<int>, std::equal_to<int>>, std::__unordered_map_equal<int, std::__hash_value_type<int, float>, std::equal_to<int>, std::hash<int>>, std::allocator<std::__hash_value_type<int, float>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<int, float>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<std::string, unsigned long, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, unsigned long>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, unsigned long>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, unsigned long>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
