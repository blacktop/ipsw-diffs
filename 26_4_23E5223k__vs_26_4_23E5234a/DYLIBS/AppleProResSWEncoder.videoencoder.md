## AppleProResSWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder`

```diff

 50204.0.0.0.0
-  __TEXT.__text: 0x20ad8
-  __TEXT.__auth_stubs: 0x590
+  __TEXT.__text: 0x20a58
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xf990
-  __TEXT.__cstring: 0x541
+  __TEXT.__cstring: 0x40e
   __TEXT.__oslogstring: 0xbc
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__unwind_info: 0x258

   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41C5D69F-7D8C-3268-8BA3-164961DE0433
+  UUID: 6FDE81DB-DDED-3A08-9B0C-1509A999914A
   Functions: 160
-  Symbols:   560
-  CStrings:  83
+  Symbols:   559
+  CStrings:  82
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZN7Picture6encodeEP10ThreadPoolI13EncoderWorker10EncoderJobvEPK11PixelBufferR15RateControlInfoRb : 4284 -> 4156
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlIugBgPr0fA1t7rYtJLqbeOo7upHzi7TNdIV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
