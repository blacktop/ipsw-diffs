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
-  UUID: 4BD43A08-639B-34CE-BA5A-25BD70628629
-  Functions: 3771
-  Symbols:   10005
-  CStrings:  1996
+  UUID: 15F7333C-7EA7-31E4-9AD0-94187BEF437C
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
+ "20:33:42"
+ "20:33:43"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): RequestedMVAV1SpatialIDs is not set ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n\n"
+ "RequestedMVAV1SpatialIDs"
- "21:12:56"
- "21:12:57"

```
