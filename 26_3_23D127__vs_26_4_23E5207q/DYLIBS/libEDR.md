## libEDR

> `/System/Library/PrivateFrameworks/libEDR.framework/libEDR`

```diff

 68.0.0.0.0
-  __TEXT.__text: 0x107ec
-  __TEXT.__auth_stubs: 0x880
+  __TEXT.__text: 0x10890
+  __TEXT.__auth_stubs: 0x860
   __TEXT.__const: 0x1848
-  __TEXT.__gcc_except_tab: 0x79c
+  __TEXT.__gcc_except_tab: 0x7d0
   __TEXT.__oslogstring: 0xe25
-  __TEXT.__cstring: 0x1e48
+  __TEXT.__cstring: 0x2349
   __TEXT.__unwind_info: 0x4e0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0xab

   __DATA_CONST.__const: 0x25f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x5a0
   __DATA.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2108B57-22A3-39DF-8992-232F8BF6C2EF
-  Functions: 232
-  Symbols:   198
-  CStrings:  409
+  UUID: 0DAAD788-FE7F-3094-8DE7-9940C5982632
+  Functions: 240
+  Symbols:   196
+  CStrings:  413
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBYOM1i8rGfL8dyT9Ipo10fvRqY2eyh9M0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBYOM1i8rGfL8dyT9Ipo10fvRqY2eyh9M0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBYOM1i8rGfL8dyT9Ipo10fvRqY2eyh9M0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:825: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoRugBYOM1i8rGfL8dyT9Ipo10fvRqY2eyh9M0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:830: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"

```
