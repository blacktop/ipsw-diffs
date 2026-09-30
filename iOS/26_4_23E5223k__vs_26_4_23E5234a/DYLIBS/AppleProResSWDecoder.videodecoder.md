## AppleProResSWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder`

```diff

 50204.0.0.0.0
-  __TEXT.__text: 0x56950
-  __TEXT.__auth_stubs: 0x790
+  __TEXT.__text: 0x566fc
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__const: 0x696e8
   __TEXT.__gcc_except_tab: 0x4f8
-  __TEXT.__cstring: 0x896
+  __TEXT.__cstring: 0x4f3
   __TEXT.__oslogstring: 0x120
   __TEXT.__unwind_info: 0x5f8
   __TEXT.__eh_frame: 0x3e8

   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0xe70
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: F6BD3FE2-AB76-3FDC-BF8A-CA052904442B
+  UUID: 7A686F27-6C95-304E-960E-9A3189DEF8EF
   Functions: 853
-  Symbols:   2109
-  CStrings:  99
+  Symbols:   2108
+  CStrings:  96
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorI10DecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI13PRRDecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI17SliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI20PRRSliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIN10Bytestream11MemoryBlockENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
+ __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI10DecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI13PRRDecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI17SliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI20PRRSliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIN10Bytestream11MemoryBlockENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE9push_backB9foe210106EOS2_
- __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZN27PreFaultedCVPixelBufferPoolD2Ev : 276 -> 188
~ __ZN27PreFaultedCVPixelBufferPool16newCVPixelBufferEv : 264 -> 180
~ __ZN12FrameDecoder6decodeERK15SegmentedBufferPK11PixelBuffer13DownScaleModebPb : 2640 -> 2324
~ __ZN15PRRFrameDecoder6decodeE10BytestreamP14PRRPixelBufferjb : 2588 -> 2480
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlIugBgPr0fA1t7rYtJLqbeOo7upHzi7TNdIV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugBgPr0fA1t7rYtJLqbeOo7upHzi7TNdIV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlIugBgPr0fA1t7rYtJLqbeOo7upHzi7TNdIV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"

```
