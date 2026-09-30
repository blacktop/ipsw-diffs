## Quagga

> `/System/Library/PrivateFrameworks/Quagga.framework/Quagga`

```diff

 226.0.0.0.0
-  __TEXT.__text: 0xee544
-  __TEXT.__auth_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x8b4
-  __TEXT.__const: 0x24ff0
-  __TEXT.__cstring: 0x4ef0
+  __TEXT.__text: 0xfc948
+  __TEXT.__auth_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x8c4
+  __TEXT.__const: 0x24410
+  __TEXT.__cstring: 0x89f4
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__gcc_except_tab: 0x90e0
-  __TEXT.__oslogstring: 0x674a
-  __TEXT.__unwind_info: 0x3468
+  __TEXT.__gcc_except_tab: 0x9134
+  __TEXT.__oslogstring: 0x66de
+  __TEXT.__unwind_info: 0x3470
   __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0x1b66
+  __TEXT.__objc_methname: 0x1b7e
   __TEXT.__objc_methtype: 0x1475
   __TEXT.__objc_stubs: 0x7a0
   __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__const: 0x1328
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__auth_got: 0xf00
   __AUTH_CONST.__const: 0x7b68
-  __AUTH_CONST.__cfstring: 0x3ca0
-  __AUTH_CONST.__objc_const: 0xb88
+  __AUTH_CONST.__cfstring: 0x3c60
+  __AUTH_CONST.__objc_const: 0xba0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x490

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0267E67-0A5E-3FB3-AC2B-3084E11CF9BD
-  Functions: 3256
-  Symbols:   917
-  CStrings:  2234
+  UUID: 24813942-A77D-3E0C-B011-8C4F2952B188
+  Functions: 3254
+  Symbols:   919
+  CStrings:  2275
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x27
+ _wmemchr
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:832: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:840: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:325: libc++ Hardening assertion __count <= size() failed: span<T, N>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:351: libc++ Hardening assertion __count <= size() - __offset failed: span<T, N>::subspan(offset, count): offset + count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:360: libc++ Hardening assertion __idx < size() failed: span<T, N>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:297: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1461: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugB_IwsU5Xuw4AW3p7vYkbsoiZGW_0nfmnY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "supportsPlacementSparse"
- "Failed to allocate pixel rotation session."
- "Failed to allocate pixel rotation session: %{public}@"
- "Failed to allocate pixel transfer session."
- "Failed to allocate pixel transfer session: %{public}@"

```
