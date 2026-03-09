## CiderAudioServer

> `/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer`

```diff

 34.202.0.0.0
-  __TEXT.__text: 0x37180
-  __TEXT.__auth_stubs: 0x780
+  __TEXT.__text: 0x36260
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x50c
   __TEXT.__const: 0x930
-  __TEXT.__gcc_except_tab: 0x6090
-  __TEXT.__cstring: 0x1684
+  __TEXT.__gcc_except_tab: 0x6078
+  __TEXT.__cstring: 0xa50
   __TEXT.__oslogstring: 0x1121
   __TEXT.__unwind_info: 0xbe8
   __TEXT.__objc_classname: 0x91

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x580

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B95C6F11-AC5C-3C06-845C-03F5FD2F7EA2
+  UUID: E5271DD5-1F11-346F-BDCC-8D39778282E6
   Functions: 414
-  Symbols:   177
-  CStrings:  397
+  Symbols:   176
+  CStrings:  387
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_2497e1d30 -> sub_249867d30 : 1840 -> 1800
~ sub_2497e2460 -> sub_249868438 : 1900 -> 1860
~ sub_2497e6154 -> sub_24986c104 : 2608 -> 2580
~ sub_2497e704c -> sub_24986cfe0 : 1956 -> 1864
~ sub_2497e78e4 -> sub_24986d81c : 1228 -> 1184
~ sub_2497e7db0 -> sub_24986dcbc : 1384 -> 1344
~ sub_2497ee120 -> sub_249874004 : 276 -> 264
~ sub_2497ee234 -> sub_24987410c : 352 -> 284
~ sub_2497ee3e0 -> sub_249874274 : 476 -> 432
~ sub_2497ee5bc -> sub_249874424 : 128 -> 148
~ sub_2497ee8dc -> sub_249874758 : 196 -> 208
~ sub_2497efa90 -> sub_249875918 : 92564 -> 92168
~ sub_249806464 -> sub_24988c160 : 1828 -> 1688
~ sub_24980bad0 -> sub_249891740 : 864 -> 704
~ sub_24980bf68 -> sub_249891b38 : 5016 -> 3980
~ sub_24980d504 -> sub_249892cc8 : 1264 -> 892
~ sub_24980e4d4 -> sub_249893b24 : 208 -> 180
~ sub_24981011c -> sub_249895750 : 328 -> 80
~ sub_249810264 -> sub_2498957a0 : 436 -> 164
~ sub_249810454 -> sub_249895880 : 212 -> 56
~ sub_249810610 -> sub_2498959a0 : 136 -> 48
~ sub_249810a0c -> sub_249895d44 : 3088 -> 2868
~ sub_2498132d0 -> sub_24989852c : 2124 -> 1996
~ sub_249814250 -> sub_24989942c : 216 -> 188
~ sub_249814410 -> sub_2498995d0 : 228 -> 140
~ sub_24981461c -> sub_249899784 : 316 -> 268
~ sub_249815588 -> sub_24989a6c0 : 508 -> 420
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/regex:4739: libc++ Hardening assertion ready() failed: match_results::format() called when not ready\n"
- "/AppleInternal/Library/BuildRoots/4~CJlsugCLxiibJPZW-fl2sGrRBGgNvyQduTZ-u6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
