## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 960.0.0.0.0
-  __TEXT.__text: 0x1513c8
+  __TEXT.__text: 0x151880
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__const: 0xc013
   __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__oslogstring: 0x145d3
-  __TEXT.__cstring: 0x5296
+  __TEXT.__oslogstring: 0x147e1
+  __TEXT.__cstring: 0x52af
   __TEXT.__unwind_info: 0x19c0
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__cfstring: 0x680
   __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6E113214-0F41-3EA1-B803-12E50CD76513
-  Functions: 3771
-  Symbols:   10005
-  CStrings:  1996
+  UUID: 759B10DA-0105-38E5-8F41-F772982BECF4
+  Functions: 3776
+  Symbols:   10015
+  CStrings:  2003
 
Symbols:
+ _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
+ _AppleAVDWrapperFghrnDecoderCopyProperty.cold.2
+ _AppleAVDWrapperFghrnDecoderSetProperty.cold.4
+ _AppleAVDWrapperFghrnDecoderSetProperty.cold.5
+ _CreateAVDFghrnInstance.cold.19
CStrings:
+ "00:17:39"
+ "00:17:40"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): RequestedMVAV1SpatialIDs is not set ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n\n"
+ "Mar  6 2026"
+ "RequestedMVAV1SpatialIDs"
- "23:52:53"
- "23:52:54"
- "Mar  5 2026"

```
