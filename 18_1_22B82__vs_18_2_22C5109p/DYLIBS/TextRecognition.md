## TextRecognition

> `/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition`

```diff

-394.0.0.0.0
-  __TEXT.__text: 0x16cec8
-  __TEXT.__auth_stubs: 0x2470
-  __TEXT.__objc_methlist: 0x9d04
+396.0.0.0.0
+  __TEXT.__text: 0x16d954
+  __TEXT.__auth_stubs: 0x2490
+  __TEXT.__objc_methlist: 0x9d2c
   __TEXT.__swift5_typeref: 0x153
   __TEXT.__swift5_capture: 0x3c
-  __TEXT.__cstring: 0x1a0fb
+  __TEXT.__cstring: 0x1a153
   __TEXT.__const: 0x1f1e
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__gcc_except_tab: 0x18374
-  __TEXT.__oslogstring: 0x4a67
+  __TEXT.__gcc_except_tab: 0x1844c
+  __TEXT.__oslogstring: 0x4baf
   __TEXT.__ustring: 0xa954
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x5bc8
+  __TEXT.__unwind_info: 0x5be8
   __TEXT.__eh_frame: 0x3ec
   __TEXT.__objc_classname: 0x1953
-  __TEXT.__objc_methname: 0x1a8de
-  __TEXT.__objc_methtype: 0xbdae
-  __TEXT.__objc_stubs: 0x11460
-  __DATA_CONST.__got: 0xc58
-  __DATA_CONST.__const: 0x20d8
+  __TEXT.__objc_methname: 0x1a963
+  __TEXT.__objc_methtype: 0xbdc3
+  __TEXT.__objc_stubs: 0x11500
+  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__const: 0x20e8
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50c8
+  __DATA_CONST.__objc_selrefs: 0x50e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x17a00
-  __AUTH_CONST.__auth_got: 0x1250
+  __AUTH_CONST.__auth_got: 0x1260
   __AUTH_CONST.__auth_ptr: 0x80
   __AUTH_CONST.__const: 0x1cc0
-  __AUTH_CONST.__cfstring: 0x2e2e0
+  __AUTH_CONST.__cfstring: 0x2e320
   __AUTH_CONST.__objc_const: 0x163c8
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x2ac0

   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5160
-  Symbols:   6610
-  CStrings:  15521
+  Functions: 5165
+  Symbols:   6618
+  CStrings:  15534
 
Symbols:
+ OBJC_IVAR_$_CRImage._vImage
+ _CRConvertFloat32BufferToUInt8Buffer
+ _CRCopyRectangleCropMemoryFromPixelBuffer
+ _CRImagePaddingValueForMode
+ _CRImageReaderKeepResourcesLoaded
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
- _kCVPixelBufferCGBitmapContextCompatibilityKey
CStrings:
+ "- HAS pixelBuffer (format: %!x(MISSING))"
+ "/tmp/batch_%!d(MISSING).png"
+ "@36@0:8@16i24^{?=[3]}28"
+ "@40@0:8^f16Q24Q32"
+ "CRImageReaderKeepResourcesLoaded"
+ "DEBUG_PRINT_RECOGNIZER_INPUT_BATCH"
+ "Failed to create image with float buffer: %!@(MISSING)"
+ "Ti,N,V_colorSpace"
+ "T{vImage_Buffer=^vQQQ},N,V_vImage"
+ "[CRImage initARGB8888WithCVPixelBuffer:] Unable to initialize ARGB8888 CRImage with Yp8 pixel buffer"
+ "[CRImage initARGB8888WithCVPixelBuffer:] Unsupported pixel buffer type %!x(MISSING)"
+ "[CRImage initAYUV8888WithCVPixelBuffer:] Unsupported pixel buffer type %!x(MISSING)"
+ "[CRImage initY8WithCVPixelBuffer:] Unsupported pixel buffer type %!x(MISSING)"
+ "[CRImage initYUV888WithCVPixelBuffer:] Unsupported pixel buffer type %!x(MISSING)"
+ "[CRImage_PixelBuffer imageByConvertingToColorSpace:forceDataCopy:] Unsupported color space %!d(MISSING)"
+ "[CRImage_PixelBuffer initWithCVPixelBuffer:] Unsupported pixel buffer type %!x(MISSING)"
+ "a\x12"
+ "imageByRectifyingRegion:toColorSpace:homography:"
+ "initWithFloatBuffer:width:height:"
+ "newTextureWithDescriptor:iosurface:plane:"
+ "setColorSpace:"
+ "setVImage:"
- "!\x12"
- "- HAS pixelBuffer (format: %!i(MISSING))"
- "@32@0:8@16^{?=[3]}24"
- "T{vImage_Buffer=^vQQQ},R,V_vImage"
- "[CRImage initARGB8888WithCVPixelBuffer:] Unsupported pixel buffer type %!i(MISSING)"
- "[CRImage initAYUV8888WithCVPixelBuffer:] Unsupported pixel buffer type %!i(MISSING)"
- "[CRImage initY8WithCVPixelBuffer:] Unsupported pixel buffer type %!i(MISSING)"
- "[CRImage initYUV888WithCVPixelBuffer:] Unsupported pixel buffer type %!i(MISSING)"
- "imageByRectifyingRegion:homography:"

```
