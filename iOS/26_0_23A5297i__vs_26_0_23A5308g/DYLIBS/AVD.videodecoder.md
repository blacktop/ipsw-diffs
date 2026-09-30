## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-901.0.0.0.0
-  __TEXT.__text: 0x1296a0
-  __TEXT.__auth_stubs: 0xe90
+904.1.0.0.0
+  __TEXT.__text: 0x12a508
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__const: 0xbe5f
   __TEXT.__gcc_except_tab: 0x7a4
-  __TEXT.__oslogstring: 0x1003e
-  __TEXT.__cstring: 0x5a83
-  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__oslogstring: 0x10355
+  __TEXT.__cstring: 0x5ac0
+  __TEXT.__unwind_info: 0x16f8
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x758
   __AUTH_CONST.__const: 0x3d40
   __AUTH_CONST.__cfstring: 0x720
   __DATA.__common: 0x38

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 47E81B63-84C7-3BF6-A343-FA7F7380434A
-  Functions: 1982
-  Symbols:   4876
-  CStrings:  1983
+  UUID: B60A0C7B-625F-314B-96EC-587ED5D0ECD9
+  Functions: 1984
+  Symbols:   4881
+  CStrings:  1994
 
Symbols:
+ _GetIOSurfaceTypeFromSessionPixelBufferAttributes
+ _VTDecoderSessionCopyResolvedPixelBufferAttributes
+ __ZN11CAVDDecoder15isSIODecryptionEv
+ _getIOSurfaceCompressionType
- _GetIOSurfaceTypeFromPool
CStrings:
+ "21:57:27"
+ "21:57:28"
+ "21:57:29"
+ "AppleAVD: ERROR: %s(): Failed to properly convert Pixel Buffer Format CFNumber to an integer!\n"
+ "AppleAVD: ERROR: %s(): Retrieved kCVPixelBufferPixelFormatTypeKey entry was not a CFNumber or CFArray!\n"
+ "AppleAVD: ERROR: %s(): Unrecognized pixel buffer format: %c%c%c%c - defaulting to kIOSurfaceCompressionTypeNone\n"
+ "AppleAVD: ERROR: %s(): VTDecoderSessionCopyResolvedPixelBufferAttributes failed with %d\n"
+ "AppleAVD: ERROR: %s(): kCVPixelBufferPixelFormatTypeKey was not present in retrieved dictionary\n"
+ "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeAGX\n"
+ "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeHTPC\n"
+ "AppleAVD: INFO: %s(): pixel buffer format: %c%c%c%c - kIOSurfaceCompressionTypeNone\n"
+ "AppleAVD: WARNING: %s(): Pixel Buffer Format array has %ld entries!\n"
+ "AppleAVD: encrypted slices size > MAX_SLICES:%d"
+ "GetIOSurfaceTypeFromSessionPixelBufferAttributes"
+ "Jul 25 2025"
+ "getIOSurfaceCompressionType"
- "23:39:59"
- "23:40:00"
- "AppleAVD: ERROR: %s(): CVPixelBufferPoolCreatePixelBuffer failed with err %d\n"
- "GetIOSurfaceTypeFromPool"
- "Jul 14 2025"

```
