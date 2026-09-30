## Recon3D

> `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D`

```diff

 8.25.11.4.5
-  __TEXT.__text: 0x1889d14
-  __TEXT.__auth_stubs: 0x2b30
-  __TEXT.__const: 0x1194e0
-  __TEXT.__cstring: 0x553a8
-  __TEXT.__gcc_except_tab: 0xf25c4
+  __TEXT.__text: 0x1856148
+  __TEXT.__auth_stubs: 0x2b20
+  __TEXT.__const: 0x119460
+  __TEXT.__cstring: 0x4b810
+  __TEXT.__gcc_except_tab: 0xf2a7c
   __TEXT.__oslogstring: 0x8331
-  __TEXT.__unwind_info: 0x35310
+  __TEXT.__unwind_info: 0x351c8
   __TEXT.__eh_frame: 0x125c
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0xc58

   __DATA_CONST.__const: 0x1ca8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x438
-  __AUTH_CONST.__auth_got: 0x15a8
-  __AUTH_CONST.__const: 0x60b30
+  __AUTH_CONST.__auth_got: 0x15a0
+  __AUTH_CONST.__const: 0x60b78
   __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__data: 0x10

   __AUTH.__thread_bss: 0x38
   __DATA.__data: 0x57b0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x250
+  __DATA.__bss: 0x70
   __DATA.__common: 0x7a8
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x3d78
+  __DATA_DIRTY.__bss: 0x3f38
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53F73B3C-705C-3E4F-B7B0-3EC161517D46
-  Functions: 37787
-  Symbols:   1832
-  CStrings:  7491
+  UUID: 6A374E0B-63A8-347D-8EF8-035567C07488
+  Functions: 37656
+  Symbols:   1831
+  CStrings:  7419
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJpzugAqjK1XDsRAmUqtAjHSoC5mVw-4dWUv8cY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CJpzugAqjK1XDsRAmUqtAjHSoC5mVw-4dWUv8cY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CJpzugAqjK1XDsRAmUqtAjHSoC5mVw-4dWUv8cY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CJpzugAqjK1XDsRAmUqtAjHSoC5mVw-4dWUv8cY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:697: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1530: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/regex:4739: libc++ Hardening assertion ready() failed: match_results::format() called when not ready\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:543: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:297: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJRiugDdc1ajAD_ohMnlODHq-AjsTnchfAkampc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/rational.hpp"
- "vt1 == nullptr"

```
