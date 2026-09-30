## libGPUCompilerImplLazy.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib`

```diff

-32023.864.0.0.0
-  __TEXT.__text: 0x1191890
-  __TEXT.__auth_stubs: 0x6d00
+32023.878.0.0.0
+  __TEXT.__text: 0x116d00c
+  __TEXT.__auth_stubs: 0x6cf0
   __TEXT.__init_offsets: 0x14
-  __TEXT.__const: 0xd02b0
-  __TEXT.__cstring: 0x137ce2
-  __TEXT.__unwind_info: 0x18ff8
+  __TEXT.__const: 0xd4ce0
+  __TEXT.__cstring: 0x13db6b
+  __TEXT.__unwind_info: 0x17ed8
   __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x193770
-  __AUTH_CONST.__auth_got: 0x3680
-  __AUTH_CONST.__const: 0xf4b20
-  __AUTH.__data: 0x4b10
+  __DATA_CONST.__const: 0x192918
+  __AUTH_CONST.__auth_got: 0x3678
+  __AUTH_CONST.__const: 0xf4b78
+  __AUTH.__data: 0x4b40
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__data: 0x1700
+  __DATA.__data: 0x16c8
   __DATA.__bss: 0x58
   __DATA.__common: 0xd
-  __DATA_DIRTY.__data: 0x10e0
+  __DATA_DIRTY.__data: 0x1120
   __DATA_DIRTY.__bss: 0x15a8
   __DATA_DIRTY.__common: 0x250
   - /System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
-  UUID: 3C25F012-59A9-3615-8969-69AE456A1CBA
-  Functions: 38310
-  Symbols:   1846
-  CStrings:  56555
+  UUID: 6822066F-B883-358E-994B-E0853123EB93
+  Functions: 38177
+  Symbols:   1845
+  CStrings:  56589
 
Symbols:
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _wmemchr
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc
- _memset_pattern16
CStrings:
+ " (^"
+ " [[late_always_inline"
+ " isEqual:"
+ " version 32023.878"
+ "\"32023.878 "
+ "' is not in the form <symbol>=<value>"
+ "--disable-legacy-trace-buffer"
+ "--external-initialization"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:692: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:697: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:832: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1466: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "878"
+ "=&A"
+ "AIR-LLD 32023.878 (metalfe-32023.878)"
+ "Metal 32023.878"
+ "MetalLateAlwaysInline"
+ "MetalLateAlwaysInlineAttr"
+ "__METAL_PACKED_NUMERIC_FORMAT_SINT4B__"
+ "__METAL_PACKED_NUMERIC_FORMAT_UINT4B__"
+ "_spt"
+ "air-late-always-inline"
+ "bss_seg"
+ "clang -cc1 version 32023.878"
+ "data_seg"
+ "int4b_format"
+ "late_always_inline"
+ "metalfe-32023.878"
+ "uint4b_format"
- " double"
- " version 32023.864"
- "\"32023.864 "
- "&("
- "+cdecp0"
- "+cdecp7"
- "+wavefrontsize64"
- "---unknown"
- "/**<"
- "///<"
- "864"
- "AIR-LLD 32023.864 (metalfe-32023.864)"
- "CF_OPTIONS"
- "Metal 32023.864"
- "NS_OPTIONS"
- "OBJC_OPTIONS"
- "SWIFT_OPTIONS"
- "__metal_placeholder_54"
- "__metal_placeholder_55"
- "__metal_placeholder_56"
- "__metal_placeholder_57"
- "clang -cc1 version 32023.864"
- "daifclr"
- "daifset"
- "ifs-v1"
- "metalfe-32023.864"
- "misexpect"
- "pan"
- "softfp"
- "spsel"
- "uao"
- "utf-8"

```
