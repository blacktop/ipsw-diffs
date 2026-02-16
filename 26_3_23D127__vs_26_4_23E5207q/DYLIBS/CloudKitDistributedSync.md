## CloudKitDistributedSync

> `/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync`

```diff

-2340.14.0.0.0
-  __TEXT.__text: 0xe0954
-  __TEXT.__auth_stubs: 0xbb0
+2350.30.0.0.0
+  __TEXT.__text: 0xe0964
+  __TEXT.__auth_stubs: 0xb70
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1bb4
-  __TEXT.__const: 0x7200
-  __TEXT.__gcc_except_tab: 0x73dc
-  __TEXT.__cstring: 0x4c24
+  __TEXT.__const: 0x7180
+  __TEXT.__gcc_except_tab: 0x7334
+  __TEXT.__cstring: 0x5acc
   __TEXT.__oslogstring: 0x4ec
-  __TEXT.__unwind_info: 0x3d28
-  __TEXT.__eh_frame: 0x98
+  __TEXT.__unwind_info: 0x3e38
+  __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x4dd
   __TEXT.__objc_methname: 0x3895
-  __TEXT.__objc_methtype: 0x1cc2
+  __TEXT.__objc_methtype: 0x1c98
   __TEXT.__objc_stubs: 0x2fa0
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__const: 0x888

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x5620
   __AUTH_CONST.__cfstring: 0x18e0
   __AUTH_CONST.__objc_const: 0x3050

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5BE6399A-44AD-3A10-92AA-52AE631E3CE3
-  Functions: 3204
-  Symbols:   361
-  CStrings:  1732
+  UUID: 6F79698E-4B29-377E-BAA0-A0B165DBD1F8
+  Functions: 3245
+  Symbols:   357
+  CStrings:  1741
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH-kugClXjPhEIELfwwUATzSg9PYK8Wno0Cn7q0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Binaries/CloudKit/install/TempContent/Objects/CloudKit.build/ORC.build/DerivedSources/cmake/c++/src/orc_proto.pb.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/arena.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/stubs/common.cc"
+ "/Library/Caches/com.apple.xbs/AB2722EF-87B6-4BB5-A071-BAA86EBB8683/TemporaryDirectory.hsi3PY/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/wire_format_lite.cc"
+ "{unordered_map<unsigned long long, CKXListInstance, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXListInstance>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXListInstance>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, CKXListInstance>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, CKXListInstance>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, CKXListInstance>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<unsigned long long, CKXProxyBase *, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXProxyBase *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, CKXProxyBase *>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, CKXProxyBase *>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, CKXProxyBase *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "/Library/Caches/com.apple.xbs/Binaries/CloudKit/install/TempContent/Objects/CloudKit.build/ORC.build/DerivedSources/cmake/c++/src/orc_proto.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/arena.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/message_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/stubs/common.cc"
- "/Library/Caches/com.apple.xbs/Sources/CloudKit/Submodules/CKDistributedSyncDependencies/orc-dependencies/protobuf-3.6.1/src/google/protobuf/wire_format_lite.cc"
- "{unordered_map<unsigned long long, CKXListInstance, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXListInstance>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXListInstance>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXListInstance>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXListInstance>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXListInstance>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
- "{unordered_map<unsigned long long, CKXProxyBase *, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CKXProxyBase *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CKXProxyBase *>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CKXProxyBase *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CKXProxyBase *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
