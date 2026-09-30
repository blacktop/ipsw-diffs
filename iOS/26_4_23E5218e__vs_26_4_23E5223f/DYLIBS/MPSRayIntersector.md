## MPSRayIntersector

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector`

```diff

-129.4.3.0.0
-  __TEXT.__text: 0x43c90
-  __TEXT.__auth_stubs: 0x640
+129.4.4.0.0
+  __TEXT.__text: 0x41bc8
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_methlist: 0x14c4
   __TEXT.__const: 0x5b8
   __TEXT.__gcc_except_tab: 0x16f0
-  __TEXT.__cstring: 0x704b
-  __TEXT.__unwind_info: 0xce8
+  __TEXT.__cstring: 0x5f47
+  __TEXT.__unwind_info: 0xd00
   __TEXT.__objc_classname: 0x283
   __TEXT.__objc_methname: 0x37c5
   __TEXT.__objc_methtype: 0xe84

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcb8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x398
   __AUTH_CONST.__cfstring: 0x33a0
   __AUTH_CONST.__objc_const: 0x24e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F648A19-0D30-39CB-9DAD-5C8818AB676B
-  Functions: 1040
-  Symbols:   204
-  CStrings:  1598
+  UUID: D058D2FA-5A88-3768-9BD0-869482E0092E
+  Functions: 1041
+  Symbols:   203
+  CStrings:  1586
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
