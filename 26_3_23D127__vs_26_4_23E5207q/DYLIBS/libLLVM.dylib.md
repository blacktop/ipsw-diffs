## libLLVM.dylib

> `/usr/lib/libLLVM.dylib`

```diff

-32023.864.0.0.0
-  __TEXT.__text: 0x20c6314
-  __TEXT.__auth_stubs: 0x2d90
+32023.878.0.0.0
+  __TEXT.__text: 0x1fc4f08
+  __TEXT.__auth_stubs: 0x2d40
   __TEXT.__init_offsets: 0x680
-  __TEXT.__const: 0x26840dc
-  __TEXT.__cstring: 0x110c4f
+  __TEXT.__const: 0x26845e0
+  __TEXT.__cstring: 0x11a9a1
   __TEXT.__oslogstring: 0x106
-  __TEXT.__unwind_info: 0x2ce98
-  __TEXT.__eh_frame: 0x3348
+  __TEXT.__unwind_info: 0x2cbe8
+  __TEXT.__eh_frame: 0x32f8
   __DATA_CONST.__got: 0x6e8
-  __DATA_CONST.__const: 0x26c160
-  __AUTH_CONST.__auth_got: 0x16c8
-  __AUTH_CONST.__const: 0x65298
+  __DATA_CONST.__const: 0x26c148
+  __AUTH_CONST.__auth_got: 0x16a0
+  __AUTH_CONST.__const: 0x65238
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH.__data: 0x128
+  __AUTH.__data: 0x398
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0xdff
   __DATA.__data: 0x24b0
-  __DATA.__bss: 0x9f08
-  __DATA.__common: 0xc78
-  __DATA_DIRTY.__data: 0x1468
-  __DATA_DIRTY.__bss: 0x3fb2c
-  __DATA_DIRTY.__common: 0xbf78
+  __DATA.__bss: 0xa560
+  __DATA.__common: 0xc30
+  __DATA_DIRTY.__data: 0x11f8
+  __DATA_DIRTY.__bss: 0x3f738
+  __DATA_DIRTY.__common: 0xbd58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
-  UUID: 495CA055-49BF-3BA2-9064-04217A8E1687
-  Functions: 73019
-  Symbols:   21857
-  CStrings:  42997
+  UUID: 9F909086-5BE3-36AF-A778-08CE424AEA69
+  Functions: 72703
+  Symbols:   21856
+  CStrings:  43031
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _wmemchr
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- _memset_pattern16
CStrings:
+ "-macos"
+ ".flatbuffer_end"
+ ".imports"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:692: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1559: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH8zugD42D0gVqMRPG6DQ9JeRjnmQsNvO_VhoP4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/Library/Caches/com.apple.xbs/DA8F0235-CE21-4E50-8AD6-BFA728F84D51/TemporaryDirectory.f3qbwh/Sources/llvmCore_Device/llvm/include/llvm/ADT/GenericCycleImpl.h"
+ "32023.878"
+ "CacheCtl"
+ "LLVM version 32023.878"
+ "__DATA,__objc_catlist"
+ "__OBJC,__category"
+ "_addr"
+ "_value"
+ "agx.has.texture.store"
+ "index.bc"
+ "llvm-mc (based on LLVM 32023.878)"
- ", isFlat"
- ".lock"
- ".rdata$"
- "/Library/Caches/com.apple.xbs/Sources/llvmCore_Device/llvm/include/llvm/ADT/GenericCycleImpl.h"
- "32023.864"
- "@@@"
- "LLVM version 32023.864"
- "NumFastIselFailures"
- "NumFastIselSuccess"
- "NumFunctionsReset"
- "bypl1_bypl2"
- "bypl1_cacl2"
- "cacl1_cacl2"
- "dynamic-library"
- "ehcontguard"
- "fp4-dp-d16"
- "fp4-sp-d16"
- "fp5-dp-d16"
- "fp5-sp-d16"
- "fpv4-dp-d16"
- "fpv5-dp-d16"
- "gcroot intrinsic not compatible with safestack attribute"
- "labels"
- "llvm-mc (based on LLVM 32023.864)"
- "low"
- "native"
- "neon-vfpv3"
- "object_passthrough"
- "openmp-device"
- "utility"
- "vfp3-d16"
- "vfp4-d16"
- "vfpv4-sp-d16"

```
