## GeometryCompression

> `/System/Library/PrivateFrameworks/GeometryCompression.framework/GeometryCompression`

```diff

 18.0.0.0.0
-  __TEXT.__text: 0x2a364
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__const: 0x7ac
+  __TEXT.__text: 0x3c0d8
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__const: 0x744
   __TEXT.__oslogstring: 0x36
   __TEXT.__gcc_except_tab: 0xe8c
-  __TEXT.__cstring: 0x798
-  __TEXT.__unwind_info: 0x770
+  __TEXT.__cstring: 0x1ad0
+  __TEXT.__unwind_info: 0x768
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x58
-  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x3f0
   __DATA.__data: 0x630
   __DATA.__bss: 0x20
   __DATA.__common: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: BBECAE85-DADA-33D3-997A-7F41C7A6EAA5
-  Functions: 325
-  Symbols:   114
-  CStrings:  100
+  UUID: 584C4E75-64B0-38FA-9B83-3BBE8C874A00
+  Functions: 335
+  Symbols:   115
+  CStrings:  114
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZdaPvSt19__type_descriptor_t
+ __ZdlPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
- __ZdaPv
- __Znam
- __Znwm
- _memset_pattern16
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAt051Nc-HQGBcV3jlNzdfpOzSlCTDDcR4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"

```
