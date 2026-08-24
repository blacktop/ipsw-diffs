## AppleProResHWDecoder

> `/System/Library/Video/Plug-Ins/AppleProResHWDecoder.bundle/Contents/MacOS/AppleProResHWDecoder`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-600.45.0.0.0
-  __TEXT.__text: 0x21400
+600.52.0.0.0
+  __TEXT.__text: 0x20c94
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__const: 0x743c0
-  __TEXT.__gcc_except_tab: 0x448
-  __TEXT.__cstring: 0x1143
-  __TEXT.__oslogstring: 0x446c
+  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__cstring: 0x1161
+  __TEXT.__oslogstring: 0x462e
   __TEXT.__unwind_info: 0x408
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0xc0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 515
+  Functions: 520
   Symbols:   233
-  CStrings:  384
+  CStrings:  390
 
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW: GetSubFrameInfo failed for YCbCr\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ERROR Downscaled stream height+offsetV > BufferPool Plane Height\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): ERROR Downscaled stream width+offsetH > BufferPool Plane Width\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): GetSubFrameInfo failed for RAW\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Slice table for picture %d exceeds frameSize %u\n"
+ "ProResDecoder_GetSubFrameInfo"
```
