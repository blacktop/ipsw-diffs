## CloudKitDistributedSync

> `/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync`

```diff

-2260.10.3.0.0
-  __TEXT.__text: 0xe0d8c
-  __TEXT.__auth_stubs: 0xbc0
+2300.138.2.0.0
+  __TEXT.__text: 0xe0908
+  __TEXT.__auth_stubs: 0xbb0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x1bac
+  __TEXT.__objc_methlist: 0x1bb4
   __TEXT.__const: 0x7210
-  __TEXT.__gcc_except_tab: 0x75b4
-  __TEXT.__cstring: 0x4b6f
+  __TEXT.__gcc_except_tab: 0x73dc
+  __TEXT.__cstring: 0x4c24
   __TEXT.__oslogstring: 0x4ec
-  __TEXT.__unwind_info: 0x3ce0
+  __TEXT.__unwind_info: 0x3d38
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x4dd
-  __TEXT.__objc_methname: 0x388c
-  __TEXT.__objc_methtype: 0x2a10
-  __TEXT.__objc_stubs: 0x2f80
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x8d8
+  __TEXT.__objc_methname: 0x3895
+  __TEXT.__objc_methtype: 0x1c3e
+  __TEXT.__objc_stubs: 0x2fa0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe38
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x5620
-  __AUTH_CONST.__cfstring: 0x18a0
+  __AUTH_CONST.__cfstring: 0x18e0
   __AUTH_CONST.__objc_const: 0x3050
   __AUTH.__objc_data: 0xe10
   __AUTH.__data: 0x388

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 31834123-5475-3ECC-B7BB-012C6AEB003F
-  Functions: 3189
-  Symbols:   376
-  CStrings:  1727
+  UUID: 61430ECC-D928-3620-8529-C1B09363325B
+  Functions: 3204
+  Symbols:   373
+  CStrings:  1732
 
Symbols:
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/arena.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/stubs/common.cc"
+ "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/wire_format_lite.cc"
+ "Can not access a negative index: %ld"
+ "Trying to read index: %ld, but atom batch has %ld atoms"
+ "nthAtom:"
+ "{set<CKXStructInstance, std::less<CKXStructInstance>, std::allocator<CKXStructInstance>>=\"__tree_\"{__tree<CKXStructInstance, std::less<CKXStructInstance>, std::allocator<CKXStructInstance>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{unique_ptr<orc::ColumnVectorBatch, std::default_delete<orc::ColumnVectorBatch>>=\"__ptr_\"^{ColumnVectorBatch}}"
+ "{unique_ptr<orc::OutputStream, std::default_delete<orc::OutputStream>>=\"__ptr_\"^{OutputStream}}"
+ "{unique_ptr<orc::Reader, std::default_delete<orc::Reader>>=\"__ptr_\"^{Reader}}"
+ "{unique_ptr<orc::Writer, std::default_delete<orc::Writer>>=\"__ptr_\"^{Writer}}"
+ "{unordered_map<unsigned long long, CKXListInstance, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXListInstance>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXListInstance>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXListInstance>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long long, CKXProxyBase *, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXProxyBase *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXProxyBase *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<CKXFieldProperties, std::allocator<CKXFieldProperties>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<CKXStructProperties, std::allocator<CKXStructProperties>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<NSIndexSet *, std::allocator<NSIndexSet *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>>, std::allocator<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::vector<unsigned long long>, std::allocator<std::vector<unsigned long long>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/arena.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/message_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/stubs/common.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/wire_format_lite.cc"
- "{set<CKXStructInstance, std::less<CKXStructInstance>, std::allocator<CKXStructInstance>>=\"__tree_\"{__tree<CKXStructInstance, std::less<CKXStructInstance>, std::allocator<CKXStructInstance>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<CKXStructInstance, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<CKXStructInstance>>=\"__value_\"Q}}}"
- "{unique_ptr<orc::ColumnVectorBatch, std::default_delete<orc::ColumnVectorBatch>>=\"__ptr_\"{__compressed_pair<orc::ColumnVectorBatch *, std::default_delete<orc::ColumnVectorBatch>>=\"__value_\"^{ColumnVectorBatch}}}"
- "{unique_ptr<orc::OutputStream, std::default_delete<orc::OutputStream>>=\"__ptr_\"{__compressed_pair<orc::OutputStream *, std::default_delete<orc::OutputStream>>=\"__value_\"^{OutputStream}}}"
- "{unique_ptr<orc::Reader, std::default_delete<orc::Reader>>=\"__ptr_\"{__compressed_pair<orc::Reader *, std::default_delete<orc::Reader>>=\"__value_\"^{Reader}}}"
- "{unique_ptr<orc::Writer, std::default_delete<orc::Writer>>=\"__ptr_\"{__compressed_pair<orc::Writer *, std::default_delete<orc::Writer>>=\"__value_\"^{Writer}}}"
- "{unordered_map<unsigned long long, CKXListInstance, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXListInstance>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXListInstance>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXListInstance>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned long long, CKXProxyBase *, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXProxyBase *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXProxyBase *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{vector<CKXFieldProperties, std::allocator<CKXFieldProperties>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<CKXFieldProperties *, std::allocator<CKXFieldProperties>>=\"__value_\"^{?}}}"
- "{vector<CKXStructProperties, std::allocator<CKXStructProperties>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<CKXStructProperties *, std::allocator<CKXStructProperties>>=\"__value_\"^{?}}}"
- "{vector<NSIndexSet *, std::allocator<NSIndexSet *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<NSIndexSet *__strong *, std::allocator<NSIndexSet *>>=\"__value_\"^@}}"
- "{vector<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>>, std::allocator<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>> *, std::allocator<std::pair<std::unique_ptr<orc::RowReader>, std::unique_ptr<orc::ColumnVectorBatch>>>>=\"__value_\"^v}}"
- "{vector<std::vector<unsigned long long>, std::allocator<std::vector<unsigned long long>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<unsigned long long> *, std::allocator<std::vector<unsigned long long>>>=\"__value_\"^v}}"
- "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long long *, std::allocator<unsigned long long>>=\"__value_\"^Q}}"

```
