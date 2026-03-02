## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

```diff

-1827.4.3.2.0
-  __TEXT.__text: 0x6fa58
-  __TEXT.__auth_stubs: 0x17b0
-  __TEXT.__objc_stubs: 0x1ce0
+1827.4.6.0.0
+  __TEXT.__text: 0x6e06c
+  __TEXT.__auth_stubs: 0x17a0
+  __TEXT.__objc_stubs: 0x1d20
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x78c
-  __TEXT.__gcc_except_tab: 0x8d44
-  __TEXT.__cstring: 0x4256
-  __TEXT.__const: 0x17c8
+  __TEXT.__const: 0x17f8
+  __TEXT.__gcc_except_tab: 0x8d78
+  __TEXT.__cstring: 0x1b77
   __TEXT.__oslogstring: 0x13c8
   __TEXT.__objc_classname: 0x12b
   __TEXT.__ustring: 0x1a
-  __TEXT.__objc_methname: 0x1bc3
+  __TEXT.__objc_methname: 0x1c0b
   __TEXT.__objc_methtype: 0xe9b
-  __TEXT.__unwind_info: 0x3178
-  __DATA_CONST.__auth_got: 0xbe8
+  __TEXT.__unwind_info: 0x3190
+  __DATA_CONST.__auth_got: 0xbe0
   __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x1b58
+  __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_selrefs: 0x8f0
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x448
+  __DATA.__bss: 0x8c0
   __DATA.__common: 0x1be
-  __DATA.__bss: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5770D37F-6F38-32C9-88AA-ECE8EAEB851E
-  Functions: 1812
-  Symbols:   558
-  CStrings:  979
+  UUID: ACBAE225-5FBA-3AF4-B01A-F6AC88226E39
+  Functions: 1813
+  Symbols:   557
+  CStrings:  954
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/.resolve"
+ "_URLByRemovingResolveFlags"
+ "_resolveFlags"
+ "initWithURL:iconConfiguration:"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2438: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
