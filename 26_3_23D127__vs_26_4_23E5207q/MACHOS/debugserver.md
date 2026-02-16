## debugserver

> `/usr/libexec/debugserver`

```diff

-1700.2.2.13.0
-  __TEXT.__text: 0x55750
-  __TEXT.__auth_stubs: 0x12e0
+1700.2.2.123.0
+  __TEXT.__text: 0x56cd0
+  __TEXT.__auth_stubs: 0x1300
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__init_offsets: 0x10
-  __TEXT.__cstring: 0xc324
-  __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x1010
+  __TEXT.__cstring: 0xd816
+  __TEXT.__const: 0x308
+  __TEXT.__gcc_except_tab: 0x100c
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x282
-  __TEXT.__unwind_info: 0xcd8
-  __DATA_CONST.__auth_got: 0x980
+  __TEXT.__unwind_info: 0xd50
+  __DATA_CONST.__auth_got: 0x990
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x3c00
+  __DATA_CONST.__const: 0x3c90
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xf8
   __DATA.__data: 0x9888
   __DATA.__common: 0x44
-  __DATA.__bss: 0x4006d8
+  __DATA.__bss: 0x6d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmenergy.dylib
   - /usr/lib/libpmsample.dylib
-  UUID: DC00ABEB-01C9-38B9-8859-D45E961FC2BC
-  Functions: 924
-  Symbols:   388
-  CStrings:  1772
+  UUID: 5BC30E29-9D54-3FE8-9579-5F5D49CFBCFA
+  Functions: 961
+  Symbols:   390
+  CStrings:  1793
 
Symbols:
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1461: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoeugC-LGjT35XTEvVTKkuYZGYgEXnpBHPQUwA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
+ "/Library/Caches/com.apple.xbs/E3869CE7-8CCB-463D-8D90-7DF4402899FD/TemporaryDirectory.KUSjTA/Sources/lldb/llvm-project/lldb/tools/debugserver/source/RNBRemote.cpp"
+ "::mach_vm_update_pointers_with_remote_tags ( task = 0x%4.4x, ptr_count = %d ) => %i ( ptr_count_out = %d)"
+ "E91"
+ "GetMemoryTags"
+ "MachTask::GetMemoryRegionInfo ( addr = 0x%8.8llx ) => %i  (start = 0x%8.8llx, size = 0x%8.8llx, permissions = %u)"
+ "MachTask::GetMemoryTags ( addr = 0x%8.8llx, size = 0x%8.8llx ) => %s ( tag count = %llu)"
+ "MachVMMemory.cpp"
+ "Return tags for a region of memory"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "err"
+ "flags:"
+ "hw.optional.arm.FEAT_MTE4"
+ "info = { prot = %u, max_prot = %u, inheritance = 0x%8.8x, offset = 0x%8.8llx, user_tag = 0x%8.8x, ref_count = %u, shadow_depth = %u, ext_pager = %u, share_mode = %u, is_submap = %d, behavior = %d, object_id = 0x%8.8x, user_wired_count = 0x%4.4x, flags = %d }"
+ "len == sizeof(val)"
+ "mach_vm_update_pointers_with_remote_tags"
+ "memory-tagging+;"
+ "ok"
+ "qMemTags"
+ "supports_memory_tagging"
- "/Library/Caches/com.apple.xbs/Sources/lldb/llvm-project/lldb/tools/debugserver/source/RNBRemote.cpp"
- "G"
- "MachTask::MemoryRegionInfo ( addr = 0x%8.8llx ) => %i  (start = 0x%8.8llx, size = 0x%8.8llx, permissions = %u)"
- "RNBRemote::HandlePacket_G(%s): extracted %llu of %llu bytes, size mismatch\n"
- "Read registers"
- "Write registers"
- "driverkit"
- "g"
- "info = { prot = %u, max_prot = %u, inheritance = 0x%8.8x, offset = 0x%8.8llx, user_tag = 0x%8.8x, ref_count = %u, shadow_depth = %u, ext_pager = %u, share_mode = %u, is_submap = %d, behavior = %d, object_id = 0x%8.8x, user_wired_count = 0x%4.4x }"
- "iossimulator"
- "maccatalyst"
- "tvossimulator"
- "watchossimulator"
- "xrossimulator"

```
