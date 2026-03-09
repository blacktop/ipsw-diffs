## VisionHWAccelerationServices

> `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices`

```diff

 4.3.7.0.0
-  __TEXT.__text: 0x1e07c
-  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__text: 0x1dd58
+  __TEXT.__auth_stubs: 0xc00
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0xf81
   __TEXT.__gcc_except_tab: 0x149c
   __TEXT.__oslogstring: 0x128c
-  __TEXT.__cstring: 0x1c0f
-  __TEXT.__unwind_info: 0x950
+  __TEXT.__cstring: 0x11c9
+  __TEXT.__unwind_info: 0x948
   __TEXT.__objc_classname: 0x34
   __TEXT.__objc_methname: 0x3c1
   __TEXT.__objc_methtype: 0x1bf

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH_CONST.__const: 0xcf8
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x358

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18FBA50C-BE91-3BD0-9D3D-DE11FAA7B722
+  UUID: 26835FAC-BEA6-3CB2-A163-FB9B263E0001
   Functions: 448
-  Symbols:   271
-  CStrings:  392
+  Symbols:   270
+  CStrings:  385
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_29823ce30 -> sub_298715e30 : 1056 -> 716
~ sub_298247fb8 -> sub_298720e64 : 308 -> 256
~ sub_298248b4c -> sub_2987219c4 : 2360 -> 2288
~ sub_29824956c -> sub_29872239c : 1904 -> 1908
~ sub_298249cdc -> sub_298722b10 : 628 -> 604
~ sub_298249f50 -> sub_298722d6c : 7876 -> 7844
~ sub_29824bed8 -> sub_298724cd4 : 3448 -> 3400
~ sub_29824f43c -> sub_298728208 : 2940 -> 2900
~ sub_298251268 -> sub_29872a00c : 1848 -> 1884
~ sub_29825246c -> sub_29872b234 : 3104 -> 2936
~ sub_298255f84 -> sub_29872eca4 : 2104 -> 2032
~ sub_298258be0 -> sub_2987318b8 : 1308 -> 1312
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugDyR-YuSwHo5RKD8nGP_FA0KKP3tUz4q8Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"

```
