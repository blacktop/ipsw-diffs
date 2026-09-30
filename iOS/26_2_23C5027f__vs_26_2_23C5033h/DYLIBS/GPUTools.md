## GPUTools

> `/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools`

```diff

 310.8.0.0.0
-  __TEXT.__text: 0x2a7b8
+  __TEXT.__text: 0x2a7e4
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x2344
   __TEXT.__gcc_except_tab: 0xd6c

   __TEXT.__unwind_info: 0xdc8
   __TEXT.__objc_classname: 0x32d
   __TEXT.__objc_methname: 0x6685
-  __TEXT.__objc_methtype: 0x29a5
+  __TEXT.__objc_methtype: 0x2a3b
   __TEXT.__objc_stubs: 0x40e0
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x808

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2E652163-431D-383C-8DDB-B873BA837E71
+  UUID: 8724AEB4-B809-383D-BC54-6EFD781F67D1
   Functions: 1098
-  Symbols:   3847
+  Symbols:   3848
   CStrings:  2164
 
Symbols:
+ ___chkstk_darwin
Functions:
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE25__emplace_unique_key_argsIS7_JNS_4pairIS7_S8_EEEEENSL_INS_15__hash_iteratorIPNS_11__hash_nodeIS9_S8_EEEEbEERKT_DpOT0_ : 632 -> 636
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPvEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeIS9_S8_EEEERKT_ : 252 -> 256
~ -[DYCaptureArchiveStack getSortedFilePositionsForDataCaching] : 1428 -> 1400
~ __ZNSt3__16vectorIN8GPUTools8objc_refIP16DYCaptureArchiveEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRS4_EEEPS5_DpOT_ : 272 -> 276
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcNS_4pairIP29dy_capture_index_file_entry_tmEEEENS_22__unordered_map_hasherIS3_S8_N8GPUTools11CStringHash4hashENSB_5equalELb1EEENS_21__unordered_map_equalIS3_S8_SD_SC_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS3_JRS3_S7_EEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 604 -> 608
~ +[NSData(DYNSDataZlibAdditions) dy_decompressData:inMutableData:error:] : 396 -> 416
~ +[NSData(DYNSDataZlibAdditions) dy_dataWithContentsOfGzipFileAtPath:error:] : 416 -> 436
~ -[DYFunctionPlayer processArguments] : 2316 -> 2332
~ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS5_IS8_EEE24__emplace_back_slow_pathIJNS1_IPKcbEEEEEPS8_DpOT_ : 260 -> 264
~ -[DYFSStreamer _invalidate] : 80 -> 76
CStrings:
+ "[16{vector<std::pair<std::string, bool>, std::allocator<std::pair<std::string, bool>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}]"
+ "[16{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}]"
+ "{SequenceCache=\"_state\"I\"_streamIdx\"I\"_streamNum\"I\"_dataIdx\"I\"_dataNum\"I\"_dataList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}\"_compressedDataList\"{vector<std::vector<std::pair<unsigned int, unsigned int>>, std::allocator<std::vector<std::pair<unsigned int, unsigned int>>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8^{OpaqueJSString=}16"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@0:8^{OpaqueJSValue=}16"
+ "{unique_ptr<GPUTools::RunningStatistics<unsigned long long>, std::default_delete<GPUTools::RunningStatistics<unsigned long long>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{unordered_map<const char *, OpaqueJSString *, std::hash<const char *>, std::equal_to<const char *>, std::allocator<std::pair<const char *const, OpaqueJSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, OpaqueJSString *>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, OpaqueJSString *>, std::hash<const char *>, std::equal_to<const char *>>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, OpaqueJSString *>, std::equal_to<const char *>, std::hash<const char *>>, std::allocator<std::__hash_value_type<const char *, OpaqueJSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<const char *, OpaqueJSValue *, std::hash<const char *>, std::equal_to<const char *>, std::allocator<std::pair<const char *const, OpaqueJSValue *>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, OpaqueJSValue *>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, OpaqueJSValue *>, std::hash<const char *>, std::equal_to<const char *>>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, OpaqueJSValue *>, std::equal_to<const char *>, std::hash<const char *>>, std::allocator<std::__hash_value_type<const char *, OpaqueJSValue *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<void *, unsigned long, std::hash<void *>, std::equal_to<void *>, std::allocator<std::pair<void *const, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<void *, unsigned long>, std::__unordered_map_hasher<void *, std::__hash_value_type<void *, unsigned long>, std::hash<void *>, std::equal_to<void *>>, std::__unordered_map_equal<void *, std::__hash_value_type<void *, unsigned long>, std::equal_to<void *>, std::hash<void *>>, std::allocator<std::__hash_value_type<void *, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<DYCaptureArchiveCacheEntry, std::allocator<DYCaptureArchiveCacheEntry>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}"
+ "{vector<GPUTools::objc_ref<DYCaptureArchive *>, std::allocator<GPUTools::objc_ref<DYCaptureArchive *>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}"
+ "{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q{?=^Q}}16@0:8"
- "[16{vector<std::pair<std::string, bool>, std::allocator<std::pair<std::string, bool>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}]"
- "[16{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}]"
- "{SequenceCache=\"_state\"I\"_streamIdx\"I\"_streamNum\"I\"_dataIdx\"I\"_dataNum\"I\"_dataList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"_compressedDataList\"{vector<std::vector<std::pair<unsigned int, unsigned int>>, std::allocator<std::vector<std::pair<unsigned int, unsigned int>>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8^{OpaqueJSString=}16"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8^{OpaqueJSValue=}16"
- "{unique_ptr<GPUTools::RunningStatistics<unsigned long long>, std::default_delete<GPUTools::RunningStatistics<unsigned long long>>>=\"__ptr_\"^v}"
- "{unordered_map<const char *, OpaqueJSString *, std::hash<const char *>, std::equal_to<const char *>, std::allocator<std::pair<const char *const, OpaqueJSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, OpaqueJSString *>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, OpaqueJSString *>, std::hash<const char *>, std::equal_to<const char *>>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, OpaqueJSString *>, std::equal_to<const char *>, std::hash<const char *>>, std::allocator<std::__hash_value_type<const char *, OpaqueJSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSString *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<const char *, OpaqueJSValue *, std::hash<const char *>, std::equal_to<const char *>, std::allocator<std::pair<const char *const, OpaqueJSValue *>>>=\"__table_\"{__hash_table<std::__hash_value_type<const char *, OpaqueJSValue *>, std::__unordered_map_hasher<const char *, std::__hash_value_type<const char *, OpaqueJSValue *>, std::hash<const char *>, std::equal_to<const char *>>, std::__unordered_map_equal<const char *, std::__hash_value_type<const char *, OpaqueJSValue *>, std::equal_to<const char *>, std::hash<const char *>>, std::allocator<std::__hash_value_type<const char *, OpaqueJSValue *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<const char *, OpaqueJSValue *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<void *, unsigned long, std::hash<void *>, std::equal_to<void *>, std::allocator<std::pair<void *const, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<void *, unsigned long>, std::__unordered_map_hasher<void *, std::__hash_value_type<void *, unsigned long>, std::hash<void *>, std::equal_to<void *>>, std::__unordered_map_equal<void *, std::__hash_value_type<void *, unsigned long>, std::equal_to<void *>, std::hash<void *>>, std::allocator<std::__hash_value_type<void *, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<void *, unsigned long>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<DYCaptureArchiveCacheEntry, std::allocator<DYCaptureArchiveCacheEntry>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
- "{vector<GPUTools::objc_ref<DYCaptureArchive *>, std::allocator<GPUTools::objc_ref<DYCaptureArchive *>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
- "{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q^Q}16@0:8"

```
