## libllvm-flatbuffers.dylib

> `/usr/lib/libllvm-flatbuffers.dylib`

```diff

-32023.880.0.0.0
-  __TEXT.__text: 0x3cf80
-  __TEXT.__auth_stubs: 0x580
+32023.881.0.0.0
+  __TEXT.__text: 0x3bd54
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__const: 0x378
-  __TEXT.__cstring: 0x32b2
-  __TEXT.__unwind_info: 0x548
+  __TEXT.__cstring: 0x17de
+  __TEXT.__unwind_info: 0x560
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x290
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH_CONST.__const: 0x98
   __AUTH.__data: 0x10
   __DATA.__data: 0x22
   __DATA.__bss: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 874D31D1-47EC-31AF-881D-3E0C6F9FEC7B
-  Functions: 485
-  Symbols:   262
-  CStrings:  307
+  UUID: 30059D1A-17D8-3CE6-858C-74D217C06D28
+  Functions: 494
+  Symbols:   261
+  CStrings:  288
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIVugCS1IKPwSoGrIf4OlkRyXDParu4aZujmAA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
