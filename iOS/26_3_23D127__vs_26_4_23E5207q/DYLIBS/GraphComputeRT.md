## GraphComputeRT

> `/System/Library/PrivateFrameworks/GraphComputeRT.framework/GraphComputeRT`

```diff

-2.2.4.0.0
-  __TEXT.__text: 0x5f71b8
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__const: 0x54770
-  __TEXT.__cstring: 0x131d0
+2.2.7.0.0
+  __TEXT.__text: 0x5e9bfc
+  __TEXT.__auth_stubs: 0x1900
+  __TEXT.__const: 0x51520
+  __TEXT.__cstring: 0x169a0
   __TEXT.__oslogstring: 0x1ba
-  __TEXT.__gcc_except_tab: 0x3c398
-  __TEXT.__unwind_info: 0x12000
+  __TEXT.__gcc_except_tab: 0x3c0d0
+  __TEXT.__unwind_info: 0x11df8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x321

   __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
-  __AUTH_CONST.__auth_got: 0xc98
-  __AUTH_CONST.__const: 0x28090
+  __AUTH_CONST.__auth_got: 0xc90
+  __AUTH_CONST.__const: 0x28050
   __AUTH.__data: 0x1b8
   __DATA.__data: 0x75c0
-  __DATA.__bss: 0x13b38
+  __DATA.__bss: 0x13b78
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F972C9A-3B15-3FD5-9B0C-32D4D499F7CC
-  Functions: 15312
-  Symbols:   5122
-  CStrings:  1717
+  UUID: 3DCA0418-8EAA-39E6-9823-EEB8B39609AE
+  Functions: 15320
+  Symbols:   5121
+  CStrings:  1768
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _dsytrf$NEWLAPACK
+ _dsytrs$NEWLAPACK
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _ssytrf$NEWLAPACK
+ _ssytrs$NEWLAPACK
+ _wmemchr
- _dsytrf_
- _dsytrs_
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
- _ssytrf_
- _ssytrs_
CStrings:
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1530: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1559: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:832: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/221A0E2B-0CFC-460F-905D-30AC7622869D/TemporaryDirectory.WzeMng/Sources/GraphCompute_RunTime/src/GraphCompute/estimator/lang/blockmatrix.cpp"
+ "/Library/Caches/com.apple.xbs/221A0E2B-0CFC-460F-905D-30AC7622869D/TemporaryDirectory.WzeMng/Sources/GraphCompute_RunTime/src/GraphCompute/models/camera/pinhole.cpp"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:273 Assert failed: prev_hash_entry != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:360 Assert failed: entry->more_recent != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:364 Assert failed: least_recently_used == entry\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:367 Assert failed: entry->more_recent != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:458 Assert failed: no_host_pointers_equal\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/cache.cpp:536 Assert failed: entry->in_use_count > 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:249 Assert failed: buf->device == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:314 Assert failed: buf->device == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:401 Assert failed: buf->device == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:419 Assert failed: buf->device == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1016 Assert failed: offset == total_args_size\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1029 Assert failed: arg_sizes[i] == sizeof(uint64_t)\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1165 Assert failed: dst_device_interface == NULL || dst_device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1169 Assert failed: dst_device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1180 Assert failed: to_host || dst->device\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1224 Assert failed: from_host\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1233 Assert failed: total_size != 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1356 Assert failed: buf->device == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1379 Assert failed: buf->device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1392 Assert failed: buf->device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1407 Assert failed: buf->device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1421 Assert failed: buf->device_interface == &metal_device_interface\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:387 Assert failed: (device == 0) || (queue != 0)\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:543 Assert failed: size != 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:551 Assert failed: buf->dim[i].stride > 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:604 Assert failed: (((device_handle *)buf->device)->offset == 0) && \"halide_metal_device_free on buffer obtained from halide_device_crop\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:818 Assert failed: buffer->host && buffer->device\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:832 Assert failed: total_size != 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:861 Assert failed: buffer->host && buffer->device\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:862 Assert failed: buffer->dimensions <= MAX_COPY_DIMS\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:969 Assert failed: (arg_sizes[i] & (arg_sizes[i] - 1)) == 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/metal.cpp:995 Assert failed: padded_args_size >= total_args_size\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:210 Assert failed: p_stats != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:237 Assert failed: p_stats != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:238 Assert failed: func_id >= 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:239 Assert failed: func_id < p_stats->num_funcs\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:273 Assert failed: p_stats != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:274 Assert failed: func_id >= 0\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:275 Assert failed: func_id < p_stats->num_funcs\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/synchronization_common.h:1096 Assert failed: val & 0x1\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/synchronization_common.h:382 Assert failed: next != NULL\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/thread_pool_common.h:153 Assert failed: bytes == limit && \"Logic error in thread pool work queue initialization.\\n\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/thread_pool_common.h:500 Assert failed: (min_threads <= ((task_parent->task.min_threads * task_parent->active_workers) - task_parent->threads_reserved)) && \"Logic error: thread over commit.\\n\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:115 Assert failed: success && \"Could not write to trace file\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:215 Assert failed: print_bits <= 64 && \"Tracing bad type\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:284 Assert failed: print_bits >= 16 && \"Tracing a bad type\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:345 Assert failed: file && \"Failed to open trace file\\n\"\n"
+ "/Library/Caches/com.apple.xbs/9D8F2F71-BC90-4880-B913-E15EE94D9C66/TemporaryDirectory.zQkXhk/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:86 Assert failed: size <= buffer_size\n"
+ "EqualShape"
+ "EqualSize"
+ "EqualType"
+ "ExactShape"
+ "ExactType"
+ "FunctionOfShape"
+ "FunctionOfType"
+ "MatrixProductShape"
- "/Library/Caches/com.apple.xbs/Sources/GraphCompute_RunTime/src/GraphCompute/estimator/lang/blockmatrix.cpp"
- "/Library/Caches/com.apple.xbs/Sources/GraphCompute_RunTime/src/GraphCompute/models/camera/pinhole.cpp"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:273 Assert failed: prev_hash_entry != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:360 Assert failed: entry->more_recent != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:364 Assert failed: least_recently_used == entry\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:367 Assert failed: entry->more_recent != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:458 Assert failed: no_host_pointers_equal\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/cache.cpp:536 Assert failed: entry->in_use_count > 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:249 Assert failed: buf->device == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:314 Assert failed: buf->device == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:401 Assert failed: buf->device == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/device_interface.cpp:419 Assert failed: buf->device == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1016 Assert failed: offset == total_args_size\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1029 Assert failed: arg_sizes[i] == sizeof(uint64_t)\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1165 Assert failed: dst_device_interface == NULL || dst_device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1169 Assert failed: dst_device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1180 Assert failed: to_host || dst->device\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1224 Assert failed: from_host\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1233 Assert failed: total_size != 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1356 Assert failed: buf->device == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1379 Assert failed: buf->device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1392 Assert failed: buf->device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1407 Assert failed: buf->device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:1421 Assert failed: buf->device_interface == &metal_device_interface\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:387 Assert failed: (device == 0) || (queue != 0)\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:543 Assert failed: size != 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:551 Assert failed: buf->dim[i].stride > 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:604 Assert failed: (((device_handle *)buf->device)->offset == 0) && \"halide_metal_device_free on buffer obtained from halide_device_crop\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:818 Assert failed: buffer->host && buffer->device\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:832 Assert failed: total_size != 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:861 Assert failed: buffer->host && buffer->device\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:862 Assert failed: buffer->dimensions <= MAX_COPY_DIMS\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:969 Assert failed: (arg_sizes[i] & (arg_sizes[i] - 1)) == 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/metal.cpp:995 Assert failed: padded_args_size >= total_args_size\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:210 Assert failed: p_stats != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:237 Assert failed: p_stats != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:238 Assert failed: func_id >= 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:239 Assert failed: func_id < p_stats->num_funcs\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:273 Assert failed: p_stats != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:274 Assert failed: func_id >= 0\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/profiler.cpp:275 Assert failed: func_id < p_stats->num_funcs\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/synchronization_common.h:1096 Assert failed: val & 0x1\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/synchronization_common.h:382 Assert failed: next != NULL\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/thread_pool_common.h:153 Assert failed: bytes == limit && \"Logic error in thread pool work queue initialization.\\n\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/thread_pool_common.h:500 Assert failed: (min_threads <= ((task_parent->task.min_threads * task_parent->active_workers) - task_parent->threads_reserved)) && \"Logic error: thread over commit.\\n\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:115 Assert failed: success && \"Could not write to trace file\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:215 Assert failed: print_bits <= 64 && \"Tracing bad type\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:284 Assert failed: print_bits >= 16 && \"Tracing a bad type\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:345 Assert failed: file && \"Failed to open trace file\\n\"\n"
- "/Library/Caches/com.apple.xbs/Sources/LoopKit_host/halide/src/runtime/tracing.cpp:86 Assert failed: size <= buffer_size\n"
- "Affine"

```
