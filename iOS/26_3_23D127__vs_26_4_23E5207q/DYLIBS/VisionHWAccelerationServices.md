## VisionHWAccelerationServices

> `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices`

```diff

-4.3.6.0.0
-  __TEXT.__text: 0x1e1f4
-  __TEXT.__auth_stubs: 0xc40
+4.3.7.0.0
+  __TEXT.__text: 0x1e07c
+  __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0xfcc
+  __TEXT.__const: 0xf81
   __TEXT.__gcc_except_tab: 0x149c
   __TEXT.__oslogstring: 0x128c
-  __TEXT.__cstring: 0x118a
-  __TEXT.__unwind_info: 0x940
+  __TEXT.__cstring: 0x1c0f
+  __TEXT.__unwind_info: 0x950
   __TEXT.__objc_classname: 0x34
   __TEXT.__objc_methname: 0x3c1
   __TEXT.__objc_methtype: 0x1bf

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x630
-  __AUTH_CONST.__const: 0xcd8
+  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__const: 0xcf8
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x358
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF4133A9-67CC-350C-B7F3-9252FDCD3B6B
-  Functions: 440
-  Symbols:   274
-  CStrings:  385
+  UUID: 856C9463-ED41-344B-8DB9-3D1FB8E676F6
+  Functions: 448
+  Symbols:   271
+  CStrings:  392
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugBZCKwG5k3g5_M9aOY6M1Oqu9STMSFulIo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:412: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/63FD7625-5F60-44EF-8562-97DF7A06BA1C/TemporaryDirectory.5XxINX/Sources/VisionHWAccelerationServices/product/VisionHWAccelerationServices/VisionHWAccelerationServices/src/VisionHWAServices.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VisionHWAccelerationServices/product/VisionHWAccelerationServices/VisionHWAccelerationServices/src/VisionHWAServices.cpp"

```
