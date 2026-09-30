## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

 250.0.0.0.0
-  __TEXT.__text: 0x279f8
-  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__text: 0x275e0
+  __TEXT.__auth_stubs: 0x1080
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x181
-  __TEXT.__cstring: 0x40a5
+  __TEXT.__cstring: 0x2fce
   __TEXT.__oslogstring: 0x2baa
   __TEXT.__gcc_except_tab: 0x1b68
   __TEXT.__dlopen_cstrs: 0x9e

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x858
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x1cc0
   __AUTH_CONST.__objc_const: 0x300

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F6E8BA9-33AD-3BF8-808F-6D08A261D195
+  UUID: F1B3F17A-229D-3425-937E-B0A8FD8EDE4F
   Functions: 679
-  Symbols:   544
-  CStrings:  1067
+  Symbols:   543
+  CStrings:  1055
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_234455060 -> sub_234513060 : 4140 -> 3844
~ sub_23445788c -> sub_234515764 : 504 -> 444
~ sub_234457a84 -> sub_234515920 : 744 -> 560
~ sub_234457d6c -> sub_234515b50 : 756 -> 580
~ sub_23445c258 -> sub_234519f8c : 548 -> 496
~ sub_23445c47c -> sub_23451a17c : 796 -> 660
~ sub_23445c798 -> sub_23451a410 : 800 -> 656
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlNugDt-2lnEXRRjHsLooM_8AMWaM8YEovyBVE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
