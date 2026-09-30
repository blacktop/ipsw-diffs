## MXI

> `/System/Library/PrivateFrameworks/MXI.framework/MXI`

```diff

-29.40.1.0.0
-  __TEXT.__text: 0x42248
-  __TEXT.__auth_stubs: 0x8d0
+29.100.2.0.1
+  __TEXT.__text: 0x44420
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_methlist: 0xea8
-  __TEXT.__const: 0x9d40
-  __TEXT.__gcc_except_tab: 0x6250
-  __TEXT.__cstring: 0x3dc2
+  __TEXT.__const: 0x9c50
+  __TEXT.__gcc_except_tab: 0x6290
+  __TEXT.__cstring: 0x43a1
   __TEXT.__oslogstring: 0x37f2
-  __TEXT.__unwind_info: 0xc20
+  __TEXT.__unwind_info: 0xd30
   __TEXT.__objc_classname: 0x17f
   __TEXT.__objc_methname: 0x3d92
   __TEXT.__objc_methtype: 0xa0a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf48
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x3c8
   __AUTH_CONST.__cfstring: 0x37a0
   __AUTH_CONST.__objc_const: 0x1ff8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 57F15388-9CA0-3C1F-A431-811553BAAD0B
-  Functions: 730
-  Symbols:   451
-  CStrings:  2092
+  UUID: 93DDCB87-3B0F-3F67-B7E9-5872DE74D771
+  Functions: 748
+  Symbols:   449
+  CStrings:  2095
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x6
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9bugBS6jeowAmt6HH3TZiDU-6TqOzW7zAgxOI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9bugBS6jeowAmt6HH3TZiDU-6TqOzW7zAgxOI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9bugBS6jeowAmt6HH3TZiDU-6TqOzW7zAgxOI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9bugBS6jeowAmt6HH3TZiDU-6TqOzW7zAgxOI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9bugBS6jeowAmt6HH3TZiDU-6TqOzW7zAgxOI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "component == 3"
- "kmeans_assign"

```
