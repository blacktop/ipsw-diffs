## HealthActivityCache

> `/System/Library/Health/Plugins/HealthActivityCache.bundle/HealthActivityCache`

```diff

-6200.5.81.2.2
-  __TEXT.__text: 0x22450
-  __TEXT.__auth_stubs: 0x6a0
+6200.5.83.0.0
+  __TEXT.__text: 0x21e94
+  __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0xc84
-  __TEXT.__gcc_except_tab: 0x3234
+  __TEXT.__gcc_except_tab: 0x3230
   __TEXT.__const: 0x98
   __TEXT.__objc_methname: 0x4091
   __TEXT.__oslogstring: 0xe05
   __TEXT.__objc_classname: 0x38f
   __TEXT.__objc_methtype: 0x18be
-  __TEXT.__cstring: 0x1ec3
-  __TEXT.__unwind_info: 0xe78
-  __DATA_CONST.__auth_got: 0x368
+  __TEXT.__cstring: 0xb3a
+  __TEXT.__unwind_info: 0xe68
+  __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x558
   __DATA_CONST.__cfstring: 0x6a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9BB07E5E-09DB-37BE-9C78-5BBBAD84DD6C
-  Functions: 586
-  Symbols:   333
-  CStrings:  1026
+  UUID: 871D7CA0-A15C-322B-933C-DF6E1FD20DB0
+  Functions: 583
+  Symbols:   332
+  CStrings:  1012
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJR3ugD1z7G7kqVcNGeEQaLmsAbhOySBCTVJ6J0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
