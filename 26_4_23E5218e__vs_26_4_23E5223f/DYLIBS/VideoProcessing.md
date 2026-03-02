## VideoProcessing

> `/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing`

```diff

 1350.3.1.0.0
-  __TEXT.__text: 0x1d22cc
-  __TEXT.__auth_stubs: 0x2200
+  __TEXT.__text: 0x1d10cc
+  __TEXT.__auth_stubs: 0x21f0
   __TEXT.__objc_methlist: 0x914
-  __TEXT.__const: 0x378e0
-  __TEXT.__cstring: 0x93c8
+  __TEXT.__const: 0x37900
+  __TEXT.__cstring: 0x71fb
   __TEXT.__gcc_except_tab: 0x53e8
   __TEXT.__oslogstring: 0xa33c
   __TEXT.__ustring: 0xa4
-  __TEXT.__unwind_info: 0x2c18
+  __TEXT.__unwind_info: 0x2c10
   __TEXT.__eh_frame: 0x568
   __TEXT.__objc_classname: 0x190
   __TEXT.__objc_methname: 0x288a

   __DATA_CONST.__objc_selrefs: 0x7d0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1110
+  __AUTH_CONST.__auth_got: 0x1108
   __AUTH_CONST.__const: 0x2270
   __AUTH_CONST.__cfstring: 0x4b20
   __AUTH_CONST.__objc_const: 0x21f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C105E1DA-C957-3134-94E4-7B0BE572CF00
-  Functions: 3308
-  Symbols:   1376
-  CStrings:  3160
+  UUID: FEA7505C-5CBE-35AF-9637-538459AAD866
+  Functions: 3305
+  Symbols:   1375
+  CStrings:  3134
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRiugCoBBbRaCOUML9L3buPl_B3uhdxpHAF5ok/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
