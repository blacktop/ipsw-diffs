## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 906.0.0.0.0
-  __TEXT.__text: 0x153f68
+  __TEXT.__text: 0x153b08
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__const: 0xc153
   __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x104e7
-  __TEXT.__cstring: 0x5c08
+  __TEXT.__oslogstring: 0x1035b
+  __TEXT.__cstring: 0x5bef
   __TEXT.__unwind_info: 0x1990
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x758
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CA1F0351-26E1-3693-B56C-37257496E399
-  Functions: 2246
-  Symbols:   5513
-  CStrings:  1998
+  UUID: D8FDF6D8-5518-3978-A4FC-049E2EE4607C
+  Functions: 2245
+  Symbols:   5511
+  CStrings:  1992
 
Symbols:
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
Functions:
~ _DisplayCallBack : 268 -> 228
~ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params : 4728 -> 4708
~ _AppleAVDWrapperFghrnDecoderCreateInstance : 640 -> 628
~ _Fghrn_createSupportedPropertyDictionary : 924 -> 916
~ _AppleAVDWrapperFghrnDecoderCopyProperty : 1008 -> 976
~ _AppleAVDWrapperFghrnDecoderSetProperty : 1796 -> 1396
~ _AppleAVDWrapperFghrnDecoderCleanUp : 416 -> 408
- _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
~ _AppleAVDWrapperFghrnDecoderStartSession : 3636 -> 3456
~ _AppleAVDWrapperFghrnDecoderDecodeFrame : 4864 -> 4704
~ _AppleAVDWrapperFghrnDecoderDecodeTile : 2308 -> 2272
~ _CreateAVDFghrnInstance : 2280 -> 2188
CStrings:
+ "20:24:15"
+ "20:24:16"
+ "Dec  8 2025"
- "21:02:20"
- "21:02:21"
- "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
- "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
- "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
- "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
- "Nov 18 2025"
- "RequestedMVAV1SpatialIDs"

```
