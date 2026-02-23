## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.878.0.0.0
-  __TEXT.__text: 0x476f9c
+32023.880.0.0.0
+  __TEXT.__text: 0x477240
   __TEXT.__auth_stubs: 0x50c0
   __TEXT.__init_offsets: 0x4c
-  __TEXT.__const: 0x272390
-  __TEXT.__cstring: 0x47ef32
+  __TEXT.__const: 0x272f50
+  __TEXT.__cstring: 0x47fa44
   __TEXT.__oslogstring: 0x47
   __TEXT.__unwind_info: 0x4f40
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0xdde08
+  __DATA_CONST.__const: 0xddfb0
   __AUTH_CONST.__auth_got: 0x2860
   __AUTH_CONST.__const: 0x95a0
   __AUTH.__thread_vars: 0x30

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  UUID: 00DACDA8-8B51-3293-A24C-6BFB84F4724D
-  Functions: 8306
+  UUID: 6D957267-8434-3A79-B4D0-03E4B5E5CB78
+  Functions: 8307
   Symbols:   3286
-  CStrings:  26693
+  CStrings:  26746
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAzWOSrdLCXJpXJqTtZiPOnP679lV4ezko/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "32023.880"
+ "AIR-PACK 32023.880 (metalfe-32023.880)"
+ "air.get_data_pointer_typed_global_tensor.s.i16.constant"
+ "air.get_data_pointer_typed_global_tensor.s.i16.global"
+ "air.get_data_pointer_typed_global_tensor.s.i16.local"
+ "air.get_data_pointer_typed_global_tensor.s.i16.private"
+ "air.get_data_pointer_typed_global_tensor.s.i32.constant"
+ "air.get_data_pointer_typed_global_tensor.s.i32.global"
+ "air.get_data_pointer_typed_global_tensor.s.i32.local"
+ "air.get_data_pointer_typed_global_tensor.s.i32.private"
+ "air.get_data_pointer_typed_global_tensor.s.i64.constant"
+ "air.get_data_pointer_typed_global_tensor.s.i64.global"
+ "air.get_data_pointer_typed_global_tensor.s.i64.local"
+ "air.get_data_pointer_typed_global_tensor.s.i64.private"
+ "air.get_data_pointer_typed_global_tensor.u.i16.constant"
+ "air.get_data_pointer_typed_global_tensor.u.i16.global"
+ "air.get_data_pointer_typed_global_tensor.u.i16.local"
+ "air.get_data_pointer_typed_global_tensor.u.i16.private"
+ "air.get_data_pointer_typed_global_tensor.u.i32.constant"
+ "air.get_data_pointer_typed_global_tensor.u.i32.global"
+ "air.get_data_pointer_typed_global_tensor.u.i32.local"
+ "air.get_data_pointer_typed_global_tensor.u.i32.private"
+ "air.get_data_pointer_typed_global_tensor.u.i64.constant"
+ "air.get_data_pointer_typed_global_tensor.u.i64.global"
+ "air.get_data_pointer_typed_global_tensor.u.i64.local"
+ "air.get_data_pointer_typed_global_tensor.u.i64.private"
+ "air.get_data_pointer_typed_private_tensor.s.i16.constant"
+ "air.get_data_pointer_typed_private_tensor.s.i16.global"
+ "air.get_data_pointer_typed_private_tensor.s.i16.local"
+ "air.get_data_pointer_typed_private_tensor.s.i16.private"
+ "air.get_data_pointer_typed_private_tensor.s.i32.constant"
+ "air.get_data_pointer_typed_private_tensor.s.i32.global"
+ "air.get_data_pointer_typed_private_tensor.s.i32.local"
+ "air.get_data_pointer_typed_private_tensor.s.i32.private"
+ "air.get_data_pointer_typed_private_tensor.s.i64.constant"
+ "air.get_data_pointer_typed_private_tensor.s.i64.global"
+ "air.get_data_pointer_typed_private_tensor.s.i64.local"
+ "air.get_data_pointer_typed_private_tensor.s.i64.private"
+ "air.get_data_pointer_typed_private_tensor.u.i16.constant"
+ "air.get_data_pointer_typed_private_tensor.u.i16.global"
+ "air.get_data_pointer_typed_private_tensor.u.i16.local"
+ "air.get_data_pointer_typed_private_tensor.u.i16.private"
+ "air.get_data_pointer_typed_private_tensor.u.i32.constant"
+ "air.get_data_pointer_typed_private_tensor.u.i32.global"
+ "air.get_data_pointer_typed_private_tensor.u.i32.local"
+ "air.get_data_pointer_typed_private_tensor.u.i32.private"
+ "air.get_data_pointer_typed_private_tensor.u.i64.constant"
+ "air.get_data_pointer_typed_private_tensor.u.i64.global"
+ "air.get_data_pointer_typed_private_tensor.u.i64.local"
+ "air.get_data_pointer_typed_private_tensor.u.i64.private"
+ "air.set_blend_color_render_command"
+ "air.set_depth_test_bounds_render_command"
+ "air.set_scissor_rects_render_command"
+ "air.set_stencil_reference_values_render_command"
+ "air.set_viewports_render_command"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "32023.878"
- "AIR-PACK 32023.878 (metalfe-32023.878)"

```
