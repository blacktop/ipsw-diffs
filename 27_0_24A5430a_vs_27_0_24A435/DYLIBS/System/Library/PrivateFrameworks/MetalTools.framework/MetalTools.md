## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

 382.5.3.0.0
-  __TEXT.__text: 0x1463dc
-  __TEXT.__objc_methlist: 0x1a71c
+  __TEXT.__text: 0x147030
+  __TEXT.__objc_methlist: 0x1a7f4
   __TEXT.__gcc_except_tab: 0x32ec
-  __TEXT.__cstring: 0x3550d
-  __TEXT.__const: 0x5a0
+  __TEXT.__cstring: 0x356c6
+  __TEXT.__const: 0x620
   __TEXT.__oslogstring: 0x28d1
-  __TEXT.__unwind_info: 0x5770
+  __TEXT.__unwind_info: 0x5780
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6ac8
+  __DATA_CONST.__objc_selrefs: 0x6b20
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0xf720
-  __AUTH_CONST.__objc_const: 0x490c8
+  __AUTH_CONST.__cfstring: 0xf800
+  __AUTH_CONST.__objc_const: 0x49460
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0x10f8
+  __DATA.__objc_ivar: 0x10fc
   __DATA.__data: 0x3b70
   __DATA_DIRTY.__objc_data: 0x4c90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8190
-  Symbols:   15111
-  CStrings:  3687
+  Functions: 8202
+  Symbols:   15133
+  CStrings:  3695
 
Symbols:
+ -[MTLGPUDebugComputeCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:]
+ -[MTLGPUDebugRenderCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:forStage:]
+ -[MTLToolsComputePipelineState forwardProgressUsage]
+ -[MTLToolsComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:]
+ -[MTLToolsDevice supportsAtomicWaitNotify]
+ -[MTLToolsDevice supportsMXUNarrowTileSizes]
+ -[MTLToolsDevice supportsPackUnpackSmallInteger]
+ -[MTLToolsDevice supportsRGBTextureBuffers]
+ -[MTLToolsDevice supportsSIMDGroupParallelForwardProgress]
+ -[MTLToolsDevice supportsTextureViewMinLOD]
+ -[MTLToolsTexture minLOD]
+ OBJC_IVAR_$_MTLGPUDebugDevice.textureWriteUsageTable
+ _isRGBPixelFormat
+ _objc_msgSend$forwardProgressUsage
+ _objc_msgSend$minLOD
+ _objc_msgSend$recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:
+ _objc_msgSend$setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:
+ _objc_msgSend$setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:forStage:
+ _objc_msgSend$setEnableYieldChecks:
+ _objc_msgSend$supportsAtomicWaitNotify
+ _objc_msgSend$supportsMXUNarrowTileSizes
+ _objc_msgSend$supportsPackUnpackSmallInteger
+ _objc_msgSend$supportsRGBTextureBuffers
+ _objc_msgSend$supportsSIMDGroupParallelForwardProgress
+ _objc_msgSend$supportsTextureViewMinLOD
- -[MTLGPUDebugComputeCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:]
- -[MTLGPUDebugRenderCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:forStage:]
- _objc_msgSend$setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:forStage:
CStrings:
+ "Device does not support textures with pixelFormat(%s)"
+ "MTL_SHADER_VALIDATION_YIELD_CHECK"
+ "Texture buffer with pixelFormat(%s) must be read-only"
+ "minLOD (%f) must be 0.0 because the device does not support TextureViewMinLOD."
+ "minLOD (%f) should be greater than or equal to 0.0."
+ "minLOD (%f) should be less than or equal to mipmapLevelCount (%lu) of the parent texture."
+ "pixelFormat(%s) can only be used with MTLTextureTypeTextureBuffer"
+ "yield-check"
```
