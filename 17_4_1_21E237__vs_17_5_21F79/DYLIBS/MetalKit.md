## MetalKit

> `/System/Library/Frameworks/MetalKit.framework/MetalKit`

```diff

-163.0.0.0.0
-  __TEXT.__text: 0x10224
+165.2.0.0.0
+  __TEXT.__text: 0x109cc
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0xd84
   __TEXT.__const: 0xc48
-  __TEXT.__cstring: 0x1783
+  __TEXT.__cstring: 0x1b47
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x484
   __TEXT.__objc_classname: 0x267
-  __TEXT.__objc_methname: 0x330d
+  __TEXT.__objc_methname: 0x338b
   __TEXT.__objc_methtype: 0xd16
-  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_stubs: 0x2a00
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3458
-  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_classrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x750
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0xf40
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0xb08
   __DATA.__common: 0x8
   __DATA.__bss: 0x40
+  __DATA_DIRTY.__const: 0x80
+  __DATA_DIRTY.__objc_const: 0x708
   __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TextureIO.framework/TextureIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 397
-  Symbols:   1680
-  CStrings:  966
+  Functions: 402
+  Symbols:   1696
+  CStrings:  989
 
Symbols:
+ +[MTKTextureLoaderASTCHelper isASTCHDRData:is3DBlocks:error:]
+ -[MTKTextureLoader _loadData:options:uploader:label:completionHandler:].cold.1
+ -[MTKTextureLoader _loadData:options:uploader:label:completionHandler:].cold.2
+ -[MTKTextureLoaderKTX initWithData:options:error:].cold.1
+ -[MTKTextureLoaderPVR initWithData:options:error:].cold.1
+ -[MTKTextureUploader newTextureWithData:options:error:]
+ _MTLTextureTypeString
+ ___61+[MTKTextureLoaderASTCHelper isASTCHDRData:is3DBlocks:error:]_block_invoke
+ ___61+[MTKTextureLoaderASTCHelper isASTCHDRData:is3DBlocks:error:]_block_invoke.cold.1
+ ___block_descriptor_41_e8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
+ _objc_msgSend$isASTCHDRData:is3DBlocks:error:
+ _objc_msgSend$maxTextureDepth3D
+ _objc_msgSend$maxTextureDimensionCube
+ _objc_msgSend$maxTextureHeight2D
+ _objc_msgSend$maxTextureHeight3D
+ _objc_msgSend$maxTextureLayers
+ _objc_msgSend$maxTextureWidth1D
+ _objc_msgSend$maxTextureWidth2D
+ _objc_msgSend$maxTextureWidth3D
+ _objc_msgSend$newTextureWithData:options:error:
- +[MTKTextureLoaderASTCHelper isASTCHDRData:textureType:error:]
- -[MTKTextureUploader newTextureWithData:options:]
- ___62+[MTKTextureLoaderASTCHelper isASTCHDRData:textureType:error:]_block_invoke
- ___62+[MTKTextureLoaderASTCHelper isASTCHDRData:textureType:error:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
- _objc_msgSend$isASTCHDRData:textureType:error:
- _objc_msgSend$newTextureWithData:options:
- _objc_setProperty_nonatomic
CStrings:
+ "!\"No texture loader supports MSAA or TexBuffers\""
+ "!error && \"Should not get here if we already encountered an error\""
+ "+[MTKTextureLoaderASTCHelper isASTCHDRData:is3DBlocks:error:]_block_invoke"
+ "-[MTKTextureLoader _loadData:options:uploader:label:completionHandler:]"
+ "-[MTKTextureLoaderKTX initWithData:options:error:]"
+ "-[MTKTextureLoaderPVR initWithData:options:error:]"
+ "MTKTextureLoaderKTX.m"
+ "MTKTextureLoaderPVR.m"
+ "T@\"NSString\",N,V_imageOrigin"
+ "Texture array element count %lu exceeds device support of 1..%lu for texture type %@"
+ "Texture depth %lu exceeds device support of 1..%lu for texture type %@"
+ "Texture face count %lu does not match expected value %lu for texture type %@"
+ "Texture height %lu exceeds device support of 1..%lu for texture type %@"
+ "Texture malformed."
+ "Texture mipmap level count %lu invalid for texture with dimensions %lux%lux%lu"
+ "Texture width %lu exceeds device support of 1..%lu for texture type %@"
+ "[MTKTextureLoaderKTX isKTXFile:data] && \"Function should not be reachable.\""
+ "[MTKTextureLoaderPVR isPVRFile:data] && \"This function should not be reachable.\""
+ "isASTCHDRData:is3DBlocks:error:"
+ "maxTextureDepth3D"
+ "maxTextureDimensionCube"
+ "maxTextureHeight2D"
+ "maxTextureHeight3D"
+ "maxTextureLayers"
+ "maxTextureWidth1D"
+ "maxTextureWidth2D"
+ "maxTextureWidth3D"
+ "q36@0:8@16B24^@28"
- "+[MTKTextureLoaderASTCHelper isASTCHDRData:textureType:error:]_block_invoke"
- "T@\"NSString\",&,N,V_imageOrigin"
- "isASTCHDRData:textureType:error:"
- "newTextureWithData:options:"
- "q40@0:8@16Q24^@32"

```
