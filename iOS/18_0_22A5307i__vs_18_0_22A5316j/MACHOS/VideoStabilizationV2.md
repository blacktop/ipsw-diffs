## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-563.1.11.0.0
-  __TEXT.__text: 0x48b58
+566.2.0.0.0
+  __TEXT.__text: 0x48d74
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__objc_stubs: 0x2880
-  __TEXT.__objc_methlist: 0x101c
-  __TEXT.__objc_classname: 0x1cc
-  __TEXT.__objc_methname: 0x467e
-  __TEXT.__objc_methtype: 0x1319
+  __TEXT.__objc_methlist: 0x1028
+  __TEXT.__objc_classname: 0x1d1
+  __TEXT.__objc_methname: 0x46c6
+  __TEXT.__objc_methtype: 0x1327
   __TEXT.__const: 0x630
-  __TEXT.__oslogstring: 0xb242
-  __TEXT.__cstring: 0x7d27
+  __TEXT.__oslogstring: 0xb2ac
+  __TEXT.__cstring: 0x7dab
   __TEXT.__gcc_except_tab: 0x230
   __TEXT.__unwind_info: 0x500
   __DATA_CONST.__auth_got: 0x610
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_intobj: 0x660
-  __DATA_CONST.__objc_arraydata: 0x16a0
-  __DATA_CONST.__objc_dictobj: 0x668
-  __DATA_CONST.__objc_arrayobj: 0xc00
+  __DATA_CONST.__objc_intobj: 0x6a8
+  __DATA_CONST.__objc_arraydata: 0x17f0
+  __DATA_CONST.__objc_dictobj: 0x6e0
+  __DATA_CONST.__objc_arrayobj: 0xc90
   __DATA.__objc_const: 0x48d0
-  __DATA.__objc_selrefs: 0xc50
+  __DATA.__objc_selrefs: 0xc58
   __DATA.__objc_ivar: 0x3e0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 483
-  Symbols:   1643
-  CStrings:  2367
+  Functions: 484
+  Symbols:   1644
+  CStrings:  2373
 
Symbols:
+ -[affineGPUMetal _blurDuplicatedPixelsOnPixelBuffer:validBufferRect:forDeltaMap:]
+ -[affineGPUMetal _getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:]
+ GCC_except_table35
+ _objc_msgSend$_blurDuplicatedPixelsOnPixelBuffer:validBufferRect:forDeltaMap:
- -[affineGPUMetal _blurDuplicatedPixelsOnPixelBuffer:validBufferRect:]
- GCC_except_table34
- _objc_msgSend$_blurDuplicatedPixelsOnPixelBuffer:validBufferRect:
CStrings:
+ "\x0f\x0f\x0f\x04\xf0\xf0\xf0\xf0\xf0\xf0\xb2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x12"
+ "-[affineGPUMetal _getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:]"
+ "<<<< affineGPUMetalV2 >>>> %!s(MISSING): Metal pixel buffer format not supported for deltamap blur borders pipeline"
+ "Cubes texture missing"
+ "[2I]"
+ "[2[2{?=\"count\"I\"texture\"[2@\"<MTLTexture>\"]}]]"
+ "[2[3{?=\"count\"I\"texture\"[2@\"<MTLTexture>\"]}]]"
+ "[44@\"<MTLRenderPipelineState>\"]"
+ "_blurDuplicatedPixelsOnPixelBuffer:validBufferRect:forDeltaMap:"
+ "_getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:"
+ "fragmentBlurDeltaMapBorders"
+ "v36@0:8^{__CVBuffer=}16^{CGRect={CGPoint=dd}{CGSize=dd}}24B32"
+ "vertexBlurDeltaMapBorders"
- "\x0f\x0f\x0f\x01\xf0\xf0\xf0\xf0\xf0\xf0\x92\x12\x12\x12\x12c\x12"
- "[2{?=\"count\"I\"texture\"[2@\"<MTLTexture>\"]}]"
- "[3{?=\"count\"I\"texture\"[2@\"<MTLTexture>\"]}]"
- "[41@\"<MTLRenderPipelineState>\"]"
- "_blurDuplicatedPixelsOnPixelBuffer:validBufferRect:"
- "cubes texture missing"
- "v32@0:8^{__CVBuffer=}16^{CGRect={CGPoint=dd}{CGSize=dd}}24"

```
