## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-578.0.3.0.0
-  __TEXT.__text: 0x59ed5c
-  __TEXT.__auth_stubs: 0x35c0
-  __TEXT.__objc_stubs: 0x19200
+578.0.3.0.2
+  __TEXT.__text: 0x59fcc8
+  __TEXT.__auth_stubs: 0x35d0
+  __TEXT.__objc_stubs: 0x19240
   __TEXT.__init_offsets: 0x70c
   __TEXT.__objc_methlist: 0x10a14
-  __TEXT.__gcc_except_tab: 0x585c8
-  __TEXT.__const: 0x3fc1a0
-  __TEXT.__cstring: 0x3a821
-  __TEXT.__objc_methname: 0x26ed5
+  __TEXT.__gcc_except_tab: 0x586a0
+  __TEXT.__const: 0x3fc1b0
+  __TEXT.__cstring: 0x3a83b
+  __TEXT.__objc_methname: 0x26f05
   __TEXT.__oslogstring: 0x691cd
   __TEXT.__objc_classname: 0x2486
-  __TEXT.__objc_methtype: 0x2457b
+  __TEXT.__objc_methtype: 0x246fb
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0xcec
   __TEXT.__swift5_capture: 0xc54

   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x23760
+  __TEXT.__unwind_info: 0x237a0
   __TEXT.__eh_frame: 0x728
   __DATA_CONST.__const: 0x217d8
   __DATA_CONST.__cfstring: 0x18320

   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_intobj: 0x978
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1af8
+  __DATA_CONST.__auth_got: 0x1b00
   __DATA_CONST.__got: 0xf48
   __DATA_CONST.__auth_ptr: 0x408
   __DATA.__objc_const: 0x1de38
-  __DATA.__objc_selrefs: 0x79b0
+  __DATA.__objc_selrefs: 0x79c0
   __DATA.__objc_ivar: 0x1bf4
   __DATA.__objc_data: 0x5b60
   __DATA.__data: 0x49dc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25041
-  Symbols:   1444
-  CStrings:  20955
+  Functions: 25051
+  Symbols:   1445
+  CStrings:  20960
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
CStrings:
+ "0000"
+ "C03DDF74/A584A42A"
+ "C03DDF74/A9A8962C"
+ "proximityServiceManufacturerID"
+ "proximityServiceModelID"
+ "{unordered_map<unsigned long long, std::pair<signed char, std::optional<std::string>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, std::pair<signed char, std::optional<std::string>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, std::pair<signed char, std::optional<std::string>>>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, std::pair<signed char, std::optional<std::string>>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, std::pair<signed char, std::optional<std::string>>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, std::pair<signed char, std::optional<std::string>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::pair<signed char, std::optional<std::string>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::pair<signed char, std::optional<std::string>>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::pair<signed char, std::optional<std::string>>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::pair<signed char, std::optional<std::string>>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long long, signed char, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, signed char>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, signed char>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, signed char>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, signed char>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, signed char>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, signed char>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, signed char>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, signed char>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, signed char>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
```
