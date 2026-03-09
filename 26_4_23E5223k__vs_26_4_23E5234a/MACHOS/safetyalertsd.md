## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 67.0.4.0.0
-  __TEXT.__text: 0xfb878
-  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__text: 0xfac24
+  __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_stubs: 0x3160
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb04
   __TEXT.__const: 0x9419
-  __TEXT.__gcc_except_tab: 0xf308
-  __TEXT.__cstring: 0x7ec0
+  __TEXT.__gcc_except_tab: 0xf2bc
+  __TEXT.__cstring: 0x6606
   __TEXT.__oslogstring: 0x3f1d8
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x3a6f
   __TEXT.__objc_methtype: 0x1b29
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4338
-  __DATA_CONST.__auth_got: 0x810
+  __TEXT.__unwind_info: 0x4328
+  __DATA_CONST.__auth_got: 0x808
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x85b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50A61FD6-201C-3A5C-AB07-808AE7651BBF
-  Functions: 3502
-  Symbols:   452
-  CStrings:  5585
+  UUID: 744EE8FB-E6AA-39CE-9543-5CEF4F105D7D
+  Functions: 3500
+  Symbols:   451
+  CStrings:  5567
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
