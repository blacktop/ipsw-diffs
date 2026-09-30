## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0x27cb4
+250.0.0.0.0
+  __TEXT.__text: 0x279f8
   __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x181
-  __TEXT.__cstring: 0x300d
-  __TEXT.__oslogstring: 0x2bda
-  __TEXT.__gcc_except_tab: 0x1b7c
+  __TEXT.__cstring: 0x40a5
+  __TEXT.__oslogstring: 0x2baa
+  __TEXT.__gcc_except_tab: 0x1b68
   __TEXT.__dlopen_cstrs: 0x9e
   __TEXT.__ustring: 0x6
-  __TEXT.__unwind_info: 0xa48
+  __TEXT.__unwind_info: 0xa60
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x11de
+  __TEXT.__objc_methname: 0x11cd
   __TEXT.__objc_methtype: 0xfb
-  __TEXT.__objc_stubs: 0x1260
+  __TEXT.__objc_stubs: 0x1240
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
+  __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1d20
+  __AUTH_CONST.__cfstring: 0x1cc0
   __AUTH_CONST.__objc_const: 0x300
-  __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x6b8
-  __DATA_DIRTY.__objc_data: 0x28
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x21b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0268835-BEE5-310C-AE53-2E820084E3A5
-  Functions: 666
+  UUID: 10AA960A-4BA7-31D0-A0C5-401663B1DEC6
+  Functions: 679
   Symbols:   544
-  CStrings:  1064
+  CStrings:  1067
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoVugAGUg0-2egLh98tUxynEqj0MaNYffpHULQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "S0x0180,S0x01A1,S0x01A4,S0x01B2,C0x03,S0x0401,S0x0402,S0x0507,S0x0524,S0x052A,S0x060B,S0x0615,S0x062A,C0x07,C0x20,S0x2103,S0x2104,S0x2105,S0x210A,S0x210C,S0x210D,S0x210E,S0x210F,S0x2111,S0x2180,S0x2181,S0x2182,C0x24,S0x2616,S0x262c,S0x2641,S0x27f8,C0x2B,C0x31,C0x34,S0x3200,S0x32ff,S0x8001,S0x8200,S0x8205,S0x8206,S0x820a,S0x820c,S0x8228,S0x823f,S0x8502,S0x8590,S0x8592,S0x8599,S0x8700"
- "IconServices"
- "Missing libhwtrace in %s in CPUTrace pause+stop"
- "S0x0180,S0x01A1,S0x01A4,C0x03,S0x0401,S0x0402,S0x0507,S0x0524,S0x052A,S0x060B,S0x0615,S0x062A,C0x07,C0x20,S0x2103,S0x2104,S0x2105,S0x210A,S0x210C,S0x210D,S0x210E,S0x210F,S0x2111,S0x2180,S0x2181,S0x2182,C0x24,S0x2616,S0x262c,S0x2641,S0x27f8,C0x2B,C0x31,C0x34,S0x3200,S0x32ff,S0x8001,S0x8200,S0x8205,S0x8206,S0x820a,S0x820c,S0x8228,S0x823f,S0x8502,S0x8590,S0x8592,S0x8599,S0x8700"
- "Solarium"
- "SwiftUI"
- "isEqualToString:"
- "tailspin_save_trace_with_standard_chunks"

```
