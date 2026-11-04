## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-776.2.0.0.0
-  __TEXT.__text: 0x6cca0
+780.2.0.0.0
+  __TEXT.__text: 0x6d374
   __TEXT.__const: 0x5ca8
-  __TEXT.__cstring: 0xc53c
+  __TEXT.__cstring: 0xcc2c
   __TEXT.__oslogstring: 0x2e3
   __TEXT.__objc_databytes: 0x493
   __TEXT.__gcc_except_tab: 0x64

   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift5_types2: 0x8
   __TEXT.__dof_CVPixelBu: 0x24a
-  __TEXT.__unwind_info: 0x23c0
+  __TEXT.__unwind_info: 0x23d0
   __TEXT.__eh_frame: 0x864
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
-  __DATA_CONST.__objc_arraydata: 0x4ca50
+  __DATA_CONST.__objc_arraydata: 0x51410
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x4bb8
   __AUTH_CONST.__cfstring: 0x2d00

   __AUTH_CONST.__objc_dictobj: 0x192d0
   __AUTH_CONST.__objc_intobj: 0x2268
   __AUTH_CONST.__objc_arrayobj: 0x4878
-  __AUTH_CONST.__auth_got: 0xeb0
+  __AUTH_CONST.__auth_got: 0xeb8
   __AUTH.__objc_dataobj: 0x9a8
   __AUTH.__objc_databytes: 0x330
   __AUTH.__data: 0x758

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3631
-  Symbols:   8150
-  CStrings:  1061
+  Functions: 3635
+  Symbols:   8152
+  CStrings:  1074
 
Symbols:
+ _OUTLINED_FUNCTION_5
+ _dyld_program_sdk_at_least
Functions:
~ _OUTLINED_FUNCTION_4 : 20 -> 16
+ _OUTLINED_FUNCTION_4
~ _OUTLINED_FUNCTION_2 : 16 -> 12
+ _OUTLINED_FUNCTION_3
~ _CVPixelBufferCreateWithBytes : 996 -> 1468
~ _CVPixelBufferCreateWithPlanarBytes : 972 -> 1984
+ _OUTLINED_FUNCTION_5
~ _CVPixelBufferCreate.cold.1 : 272 -> 236
+ _CVPixelBufferCreateWithBytes.cold.1
CStrings:
+ "CVPixelBufferCreateWithBytes called for a pixel format with block height %d which is greater than 1"
+ "CVPixelBufferCreateWithBytes returning err %d because bytesPerRow %u is too small for width %u (bytesPerElement %u, elementsPerBlock %u)"
+ "CVPixelBufferCreateWithBytes returning err %d because pixel format %c%c%c%c is planar (%ld planes); use CVPixelBufferCreateWithPlanarBytes()"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because kCVPixelFormatPlanes entry is not a CFArray"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because numberOfPlanes is %d whereas kCVPixelFormatPlanes indicates %d planes"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because planeBaseAddress %p + plane size %d overflows the address space for planeIndex %d"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because planeHeight %d * planeBytesPerRow %d overflows for planeIndex %d"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because planeHeight %d is not equal to %d required by image height %d and verticalSubsampling %d for planeIndex %d"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because planeWidth %d is not equal to %d required by image width %d and horizontalSubsampling %d for planeIndex %d"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because the planes %u do not fit inside dataPtr %p .. dataPtr+dataSize (%u bytes)"
+ "CVPixelBufferCreateWithPlanarBytes returning err %d because the planes span %d bytes which does not fit inside dataSize %d"
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planeHeight %d is not equal to %d required by image height %d and verticalSubsampling %d for planeIndex %d."
+ "WARNING: CVPixelBufferCreateWithPlanarBytes planeWidth %d is not equal to %d required by image width %d and horizontalSubsampling %d for planeIndex %d."
```
