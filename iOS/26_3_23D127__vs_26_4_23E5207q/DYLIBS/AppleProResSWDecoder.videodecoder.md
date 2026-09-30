## AppleProResSWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder`

```diff

 50204.0.0.0.0
-  __TEXT.__text: 0x53b20
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__const: 0x69768
-  __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__cstring: 0x4f3
+  __TEXT.__text: 0x56950
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__const: 0x696e8
+  __TEXT.__gcc_except_tab: 0x4f8
+  __TEXT.__cstring: 0x896
   __TEXT.__oslogstring: 0x120
-  __TEXT.__unwind_info: 0x5e0
-  __TEXT.__eh_frame: 0x468
+  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__eh_frame: 0x3e8
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0xe70
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 18721F25-3EE2-3201-B5EF-6266606AF22B
-  Functions: 846
-  Symbols:   2092
-  CStrings:  96
+  UUID: D65E723B-8756-3C61-8C6A-4ED9C4124CDD
+  Functions: 853
+  Symbols:   2109
+  CStrings:  99
 
Symbols:
+ __ZN13DecoderWorker6runJobEP10DecoderJob.cold.1
+ __ZN13DecoderWorker6runJobEP10DecoderJob.cold.2
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI10DecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI13PRRDecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI17SliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI20PRRSliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN10Bytestream11MemoryBlockENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE9push_backB9foe210106EOS2_
+ __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorI10DecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI13PRRDecoderJobNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI17SliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI20PRRSliceDecodeParamsNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN10Bytestream11MemoryBlockENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIN17MemoryBufferCache18MemoryBufferRecordENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
- __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoNugABL6-XOYr1Mu7tLN-E44z4VSf0cQt0Auo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugABL6-XOYr1Mu7tLN-E44z4VSf0cQt0Auo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugABL6-XOYr1Mu7tLN-E44z4VSf0cQt0Auo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"

```
