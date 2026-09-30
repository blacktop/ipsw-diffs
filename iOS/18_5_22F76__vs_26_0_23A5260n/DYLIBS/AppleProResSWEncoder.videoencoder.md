## AppleProResSWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder`

```diff

-41213.0.0.0.0
-  __TEXT.__text: 0x2040c
-  __TEXT.__auth_stubs: 0x590
+50204.0.0.0.0
+  __TEXT.__text: 0x20e88
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xf990
-  __TEXT.__cstring: 0x41e
-  __TEXT.__oslogstring: 0xd7
+  __TEXT.__cstring: 0x40e
+  __TEXT.__oslogstring: 0xbc
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__unwind_info: 0x260
   __TEXT.__eh_frame: 0x50

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
-  UUID: 7A5D804F-0EF0-37BF-A871-68B963631423
+  UUID: 9227427C-0D26-3DDB-ABC5-1DC25DEE4B5F
   Functions: 156
-  Symbols:   548
-  CStrings:  84
+  Symbols:   547
+  CStrings:  82
 
Symbols:
+ GCC_except_table2
+ GCC_except_table6
+ __ZL30isAdditionalSupportedCPUFamilyv
+ __ZN12FrameEncoderC2EiPFvvE
+ __ZN12FrameEncoderC2EiPFvvE.cold.1
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
- GCC_except_table3
- __ZL11isTupaiH17Av
- __ZN10ThreadPoolI13EncoderWorker10EncoderJobvE6createEiPKv
- __ZN10ThreadPoolI13EncoderWorker10EncoderJobvE6createEiPKv.cold.1
- __ZNKSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
Functions:
~ __ZL11isTupaiH17Av -> __ZL30isAdditionalSupportedCPUFamilyv : 324 -> 200
~ __ZN10ThreadPoolI13EncoderWorker10EncoderJobvE6createEiPKv -> __ZN12FrameEncoderC2EiPFvvE : 292 -> 384
~ __ZN12FrameEncoderC1EiPFvvE : 164 -> 4
~ __ZN7Picture6encodeEP10ThreadPoolI13EncoderWorker10EncoderJobvEPK11PixelBufferR15RateControlInfoRb : 4016 -> 4168
~ __ZNSt3__16vectorI10EncoderJobNS_9allocatorIS1_EEE8__appendEm : 444 -> 460
~ __ZN12SliceEncoder18runLevelScanAndVlcILb0EEEvRiPjS1_S1_S1_PKtiiPKaR15BitstreamWriterIXT_EE : 1960 -> 1956
~ __Z12pixInGenericIL11PixelFormat846624121EL12ChromaFormat2EEvPKhPsiiii : 3716 -> 5072
~ __Z12pixInGenericIL11PixelFormat2037741171EL12ChromaFormat2EEvPKhPsiiii : 3716 -> 5072
CStrings:
- "Failed to get cpusubfamily"
- "hw.cpusubfamily"

```
