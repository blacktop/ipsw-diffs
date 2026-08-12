## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-600.45.0.0.0
-  __TEXT.__text: 0x221d0
-  __TEXT.__gcc_except_tab: 0x468
+600.53.0.0.0
+  __TEXT.__text: 0x21a74
+  __TEXT.__gcc_except_tab: 0x494
   __TEXT.__const: 0x743e0
-  __TEXT.__cstring: 0x12e6
-  __TEXT.__oslogstring: 0x46ce
+  __TEXT.__cstring: 0x1304
+  __TEXT.__oslogstring: 0x487d
   __TEXT.__unwind_info: 0x450
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 538
+  Functions: 545
   Symbols:   581
-  CStrings:  424
+  CStrings:  430
 
CStrings:
+ "AppleProResHW (0x%x): %s(): Invalid Homography Matrix size: %zu, expected: %zu"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW: GetSubFrameInfo failed for YCbCr\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ERROR Downscaled stream height+offsetV > BufferPool Plane Height\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ERROR Downscaled stream width+offsetH > BufferPool Plane Width\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): GetSubFrameInfo failed for RAW\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): LSC metadata keys not present in metadataDictionary\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Malformed metadataExt for frame %d: metadataSetSize %u out of bounds (remaining %u), skip sending all metadata\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Slice table for picture %d exceeds frameSize %u\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): VDD metadata keys not present in metadataDictionary\n"
+ "ProResDecoder_GetSubFrameInfo"
- "WARNING AppleProResHW (0x%x): %d: %s(): Invalid Homography Matrix size: %zu, expected: %zu\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): LSC metadata keys not present in metadataDictionary\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): Malformed metadataExt for frame %d: metadataSetSize %u out of bounds (remaining %u), skip sending all metadata\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): VDD metadata keys not present in metadataDictionary\n"
```
