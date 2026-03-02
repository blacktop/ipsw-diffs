## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

 1002.101.0.0.0
-  __TEXT.__text: 0xb9bc4
-  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__text: 0xb3b5c
+  __TEXT.__auth_stubs: 0x19f0
   __TEXT.__objc_methlist: 0xb4
   __TEXT.__const: 0x939
-  __TEXT.__gcc_except_tab: 0x49f4
-  __TEXT.__cstring: 0x8479
+  __TEXT.__gcc_except_tab: 0x49e4
+  __TEXT.__cstring: 0x5c54
   __TEXT.__oslogstring: 0x9537
-  __TEXT.__unwind_info: 0x1340
+  __TEXT.__unwind_info: 0x1338
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0xd69
   __TEXT.__objc_methtype: 0x1e6

   __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH_CONST.__auth_got: 0xd08
   __AUTH_CONST.__const: 0x1f58
   __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x348

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4258022-32D6-30C2-904F-B586D25C46EA
-  Functions: 1182
-  Symbols:   961
-  CStrings:  2383
+  UUID: 200E5925-ABB6-32BE-8DA2-6E51F9F55B57
+  Functions: 1179
+  Symbols:   960
+  CStrings:  2353
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugBjNFmO1AM_WGnhXvJ4nsgpZWHlWXEHRC4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
