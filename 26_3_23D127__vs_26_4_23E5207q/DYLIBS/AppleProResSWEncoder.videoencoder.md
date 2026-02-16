## AppleProResSWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder`

```diff

 50204.0.0.0.0
-  __TEXT.__text: 0x20ea4
-  __TEXT.__auth_stubs: 0x580
+  __TEXT.__text: 0x20ad8
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xf990
-  __TEXT.__cstring: 0x40e
+  __TEXT.__cstring: 0x541
   __TEXT.__oslogstring: 0xbc
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__eh_frame: 0x50
+  __TEXT.__unwind_info: 0x258
   __TEXT.__objc_methname: 0x2f
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0DDF5A5-ED38-34B4-B232-79F64BB505AE
-  Functions: 156
-  Symbols:   545
-  CStrings:  82
+  UUID: 850E3F14-8599-3D01-B411-8A2F00FD7965
+  Functions: 160
+  Symbols:   560
+  CStrings:  83
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ __ZL30allocateIntermediateV216BufferR11PixelBufferPKS_i.cold.1
+ __ZN12FrameEncoderC2EiPFvvE.cold.2
+ __ZN12SliceEncoder9encodeVlcILb1EEEvR5SlicePKtiiiPi.cold.1
+ __ZN13EncoderWorker6runJobEP10EncoderJob.cold.2
+ __ZN7Picture6encodeEP10ThreadPoolI13EncoderWorker10EncoderJobvEPK11PixelBufferR15RateControlInfoRb.cold.1
+ __ZN7Picture6encodeEP10ThreadPoolI13EncoderWorker10EncoderJobvEPK11PixelBufferR15RateControlInfoRb.cold.2
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoNugABL6-XOYr1Mu7tLN-E44z4VSf0cQt0Auo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
