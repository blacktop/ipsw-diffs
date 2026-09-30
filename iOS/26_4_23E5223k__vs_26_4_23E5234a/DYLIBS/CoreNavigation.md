## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`

```diff

 373.0.1.0.0
-  __TEXT.__text: 0x30c47c
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__const: 0x4c2ba
-  __TEXT.__gcc_except_tab: 0x1561c
-  __TEXT.__cstring: 0x36c97
+  __TEXT.__text: 0x30005c
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__const: 0x4c2aa
+  __TEXT.__gcc_except_tab: 0x155a4
+  __TEXT.__cstring: 0x325dc
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0xc9f0
+  __TEXT.__unwind_info: 0xc990
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x850
   __AUTH_CONST.__const: 0x1c7c8
   __DATA.__data: 0x40
   __DATA.__bss: 0x480

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: C69557F7-32A0-3E64-851D-E392D1B40E49
-  Functions: 13934
-  Symbols:   11855
-  CStrings:  3540
+  UUID: 2A75C6CB-4E29-3333-8D84-55B40F56E358
+  Functions: 13915
+  Symbols:   11853
+  CStrings:  3493
 
Symbols:
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKFRugCUTl8uiS8K1SKIghJp_3000OwCHXyrr7Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CKFRugCUTl8uiS8K1SKIghJp_3000OwCHXyrr7Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CKFRugCUTl8uiS8K1SKIghJp_3000OwCHXyrr7Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~CKFRugCUTl8uiS8K1SKIghJp_3000OwCHXyrr7Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1559: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1572: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/regex:4739: libc++ Hardening assertion ready() failed: match_results::format() called when not ready\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1461: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~CJk6ugDH3NnWfVbdexSJpHZYqgyweRFrx7qpz-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"

```
