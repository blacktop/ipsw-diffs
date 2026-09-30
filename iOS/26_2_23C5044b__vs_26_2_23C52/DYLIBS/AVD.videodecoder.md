## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 906.0.0.0.0
-  __TEXT.__text: 0x153b08
+  __TEXT.__text: 0x153f68
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__const: 0xc153
   __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x1035b
-  __TEXT.__cstring: 0x5bef
+  __TEXT.__oslogstring: 0x104e7
+  __TEXT.__cstring: 0x5c08
   __TEXT.__unwind_info: 0x1990
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x758
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__cfstring: 0x740
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 20EC0201-13B3-3424-B809-731E54AA8101
-  Functions: 2245
-  Symbols:   5511
-  CStrings:  1992
+  UUID: CA1F0351-26E1-3693-B56C-37257496E399
+  Functions: 2246
+  Symbols:   5513
+  CStrings:  1998
 
Symbols:
+ _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
Functions:
~ _DisplayCallBack : 228 -> 268
~ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params : 4708 -> 4728
~ _AppleAVDWrapperFghrnDecoderCreateInstance : 628 -> 640
~ _Fghrn_createSupportedPropertyDictionary : 916 -> 924
~ _AppleAVDWrapperFghrnDecoderCopyProperty : 976 -> 1008
~ _AppleAVDWrapperFghrnDecoderSetProperty : 1396 -> 1796
~ _AppleAVDWrapperFghrnDecoderCleanUp : 408 -> 416
+ _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
~ _AppleAVDWrapperFghrnDecoderStartSession : 3456 -> 3636
~ _AppleAVDWrapperFghrnDecoderDecodeFrame : 4704 -> 4864
~ _AppleAVDWrapperFghrnDecoderDecodeTile : 2272 -> 2308
~ _CreateAVDFghrnInstance : 2188 -> 2280
CStrings:
+ "21:02:20"
+ "21:02:21"
+ "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
+ "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
+ "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
+ "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
+ "Nov 18 2025"
+ "RequestedMVAV1SpatialIDs"
- "22:03:26"
- "22:03:27"
- "Nov 12 2025"

```
