## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__AUTH_CONST.__const`

```diff

 962.0.0.0.0
-  __TEXT.__text: 0x151a58
+  __TEXT.__text: 0x151f10
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__const: 0xc013
   __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__oslogstring: 0x1461c
-  __TEXT.__cstring: 0x52ac
+  __TEXT.__oslogstring: 0x1482a
+  __TEXT.__cstring: 0x52ce
   __TEXT.__unwind_info: 0x19c8
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
-  Functions: 3773
-  Symbols:   3013
-  CStrings:  1937
+  Functions: 3778
+  Symbols:   3014
+  CStrings:  1944
 
Symbols:
+ _AppleAVDWrapperFghrnDecoderCleanUpMVAV1Resources
CStrings:
+ "16:41:59"
+ "16:42:00"
+ "16:42:01"
+ "AppleAVD: ERROR: %{public}s(): AppleAVDSetParameter call for kAppleAVDSetMVAV1DisplayLayerIDs returned ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): AppleAVD_FghrnDecoder - AppleAVDSetParameter kAppleAVDSetTaggedBufGroupArray returned ERROR\n"
+ "AppleAVD: ERROR: %{public}s(): RequestedMVAV1SpatialIDs is not set ERROR\n\n"
+ "AppleAVD: ERROR: %{public}s(): kVTDecompressionPropertyKey_RequestedMVAV1SpatialVideoLayerIDs error\n"
+ "AppleAVD: WARNING: %{public}s(): trying to set kAppleAVDSetMVAV1DisplayLayerIDs before videoContext was created!\n\n"
+ "Jul 11 2026"
+ "RequestedMVAV1SpatialIDs"
- "23:53:55"
- "23:53:56"
- "Jul  9 2026"
```
