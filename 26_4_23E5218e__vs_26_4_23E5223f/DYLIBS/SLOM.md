## SLOM

> `/System/Library/PrivateFrameworks/SLOM.framework/SLOM`

```diff

 1.19.0.0.0
-  __TEXT.__text: 0x16f412c
-  __TEXT.__auth_stubs: 0x2330
-  __TEXT.__const: 0xdda50
-  __TEXT.__cstring: 0x69daa
-  __TEXT.__gcc_except_tab: 0x96cb4
+  __TEXT.__text: 0x15ebf44
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__const: 0xdded0
+  __TEXT.__gcc_except_tab: 0x97878
+  __TEXT.__cstring: 0x5cbe5
   __TEXT.__oslogstring: 0x3794
-  __TEXT.__unwind_info: 0x249d8
-  __TEXT.__eh_frame: 0x1b58
+  __TEXT.__unwind_info: 0x24368
+  __TEXT.__eh_frame: 0x1bf0
   __TEXT.__objc_methname: 0x233
   __TEXT.__objc_stubs: 0x2c0
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x17f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x11a8
-  __AUTH_CONST.__const: 0x32778
+  __AUTH_CONST.__auth_got: 0x11a0
+  __AUTH_CONST.__const: 0x32790
   __AUTH_CONST.__cfstring: 0x100
   __AUTH.__data: 0x18
   __DATA.__data: 0x8720

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92CDFBF0-C9BC-3B0B-B983-319C93BDBE12
-  Functions: 26251
-  Symbols:   724
-  CStrings:  7164
+  UUID: B0C1EF2A-B40A-31F4-A42D-A2CDEECD8071
+  Functions: 25920
+  Symbols:   723
+  CStrings:  7087
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "curr_pose_idx >= 1 && \"The latter pose index in a pair of consecutive poses cannot be less than 1.\""
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:799: libc++ Hardening assertion this->__has_val() failed: expected::operator-> requires the expected to contain a value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:805: libc++ Hardening assertion this->__has_val() failed: expected::operator* requires the expected to contain a value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:811: libc++ Hardening assertion this->__has_val() failed: expected::operator* requires the expected to contain a value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__iterator/counted_iterator.h:108: libc++ Hardening assertion __count_ > 0 failed: Iterator is equal to or past end.\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:498: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:538: libc++ Hardening assertion !empty() failed: span<T>::front() on empty span\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:543: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugASqcHqSPi0XAdZC4Jl5hs-17hzytLA4hM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:437: libc++ Hardening assertion __n <= size() failed: remove_suffix() can't remove more than size()\n"
- "ExactlyEqual(opt_npdr_base_state_and_timestamp_->timestamp, last_kf_timestamp)"
- "Outlier plane must be valid at this stage."
- "We must have a valid pose at this stage"
- "imu pred buffer must be empty"
- "imu_pred.empty()"
- "opt_plane_to_reject_tracks_"
- "opt_ref_to_curr_pose.has_value()"
- "switch_data->state_data.current_state == IMUFilterMotionMode::TransitionMoving2Stationary"
- "vio_resolution.has_value()"

```
