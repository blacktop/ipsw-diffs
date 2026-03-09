## MLCompilerServices

> `/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices`

```diff

 3404.3.1.0.0
-  __TEXT.__text: 0x135c0
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__gcc_except_tab: 0xccc
+  __TEXT.__text: 0x12b8c
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__gcc_except_tab: 0xcc8
   __TEXT.__const: 0x177
-  __TEXT.__cstring: 0x2d09
+  __TEXT.__cstring: 0x1b98
   __TEXT.__oslogstring: 0x2bb
   __TEXT.__dlopen_cstrs: 0x6b
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__unwind_info: 0x5b8
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x550
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__cfstring: 0x120
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3B444E89-5D5F-32C4-8370-3192B0C6A1CB
+  UUID: 5F707941-E88F-3E65-9FB7-10D79CE977B0
   Functions: 262
-  Symbols:   232
-  CStrings:  290
+  Symbols:   231
+  CStrings:  278
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ _mlc_services_model_create_bundled : 2372 -> 2340
~ sub_25dd43fd4 -> sub_25dcc6fb4 : 932 -> 668
~ sub_25dd447c0 -> sub_25dcc7698 : 3360 -> 2320
~ sub_25dd457fc -> sub_25dcc82c4 : 556 -> 332
~ sub_25dd45a30 -> sub_25dcc8418 : 656 -> 588
~ sub_25dd45cc0 -> sub_25dcc8664 : 1332 -> 892
~ sub_25dd461f4 -> sub_25dcc89e0 : 500 -> 348
~ sub_25dd47584 -> sub_25dcc9cd8 : 472 -> 364
~ sub_25dd4775c -> sub_25dcc9e44 : 944 -> 812
~ sub_25dd47b0c -> sub_25dcca170 : 904 -> 780
~ sub_25dd4be80 -> sub_25dcce468 : 4792 -> 4764
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugBNfZ6P1_4Ycbz71Or6r4YAt7ZE3xqnjLU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
