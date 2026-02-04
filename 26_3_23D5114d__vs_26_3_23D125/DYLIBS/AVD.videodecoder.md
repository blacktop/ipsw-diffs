## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 908.0.0.0.0
-  __TEXT.__text: 0x153268
+  __TEXT.__text: 0x1536c8
   __TEXT.__auth_stubs: 0xe80
   __TEXT.__const: 0xc153
   __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x101fa
-  __TEXT.__cstring: 0x5ba9
+  __TEXT.__oslogstring: 0x10386
+  __TEXT.__cstring: 0x5bcb
   __TEXT.__unwind_info: 0x1980
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 82B8CA2C-FB17-34D0-B4ED-11160CEF60DF
-  Functions: 2245
-  Symbols:   5506
-  CStrings:  1981
+  UUID: E76A047A-8826-3ED1-8340-611AA546DCE0
+  Functions: 2246
+  Symbols:   5508
+  CStrings:  1988
 
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
+ "20:56:07"
+ "20:56:08"
+ "AppleAVD: %s - kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error"
+ "AppleAVD: AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR"
+ "AppleAVD: ERROR: %s() - AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n"
+ "AppleAVD: WARNING: %s() - trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n"
+ "Jan 26 2026"
+ "RequestedMVAV1SpatialIDs"
- "21:28:35"
- "Jan 22 2026"

```
