## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

 128.3.0.0.0
-  __TEXT.__text: 0x28c00
+  __TEXT.__text: 0x28ca8
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4cdc
+  __TEXT.__objc_methlist: 0x4d3c
   __TEXT.__cstring: 0x5f8c
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
   __TEXT.__unwind_info: 0xcc8
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb4f1
-  __TEXT.__objc_methtype: 0x6aec
-  __TEXT.__objc_stubs: 0x2fe0
+  __TEXT.__objc_methname: 0xb6dc
+  __TEXT.__objc_methtype: 0x6c34
+  __TEXT.__objc_stubs: 0x31a0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a0
+  __DATA_CONST.__objc_selrefs: 0x2848
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7d08
+  __AUTH_CONST.__objc_const: 0x7dc8
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x7e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B912152-CD88-3478-A10B-95602493B2A1
+  UUID: EE751060-0675-3463-B44D-A5CC2E80719E
   Functions: 1422
-  Symbols:   4252
-  CStrings:  2938
+  Symbols:   4266
+  CStrings:  2959
 
Symbols:
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1344
+ _objc_msgSend$allowOverrideRenderStates
+ _objc_msgSend$inheritBlendColor
+ _objc_msgSend$inheritCullMode
+ _objc_msgSend$inheritDepthBias
+ _objc_msgSend$inheritDepthClipMode
+ _objc_msgSend$inheritDepthStencilState
+ _objc_msgSend$inheritDepthTestBounds
+ _objc_msgSend$inheritFrontFacingWinding
+ _objc_msgSend$inheritScissorRects
+ _objc_msgSend$inheritStencilReferenceValues
+ _objc_msgSend$inheritTriangleFillMode
+ _objc_msgSend$inheritViewports
+ _objc_msgSend$maxScissorRectCount
+ _objc_msgSend$maxViewportCount
- ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1328
Functions:
~ -[IOGPUMetalIndirectCommandBuffer initWithBuffer:descriptor:maxCommandCount:] : 452 -> 620
CStrings:
+ "allowOverrideRenderStates"
+ "inheritBlendColor"
+ "inheritCullMode"
+ "inheritDepthBias"
+ "inheritDepthClipMode"
+ "inheritDepthStencilState"
+ "inheritDepthTestBounds"
+ "inheritFrontFacingWinding"
+ "inheritScissorRects"
+ "inheritStencilReferenceValues"
+ "inheritTriangleFillMode"
+ "inheritViewports"
+ "maxScissorRectCount"
+ "samplerReductionModeSupport"
+ "supportsConditionalTileDispatch"
+ "supportsDepthBoundsTesting"
+ "supportsExtendedIndirectRenderCommand"
+ "supportsFP8"
+ "supportsMXU"
+ "supportsSamplerReductionMode"
+ "supportsTextureAccessPatterns"
+ "{MTLIndirectCommandBufferHeader=\"headerSize\"Q\"commandTypes\"I\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"C\"maxFragmentBufferBindCount\"C\"maxKernelBufferBindCount\"C\"maxObjectBufferBindCount\"C\"maxMeshBufferBindCount\"C\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"maxKernelThreadgroupMemoryBindCount\"C\"maxObjectThreadgroupMemoryBindCount\"C\"maxScissorRectCount\"C\"maxViewportCount\"C\"inheritDepthStencilState\"B\"inheritDepthBias\"B\"inheritStencilReferenceValues\"B\"inheritDepthClipMode\"B\"inheritCullMode\"B\"inheritFrontFacingWinding\"B\"inheritTriangleFillMode\"B\"inheritDepthTestBounds\"B\"inheritScissorRects\"B\"inheritViewports\"B\"inheritBlendColor\"B\"allowOverrideRenderStates\"q\"size\"Q}"
- "{MTLIndirectCommandBufferHeader=\"headerSize\"Q\"commandTypes\"I\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"C\"maxFragmentBufferBindCount\"C\"maxKernelBufferBindCount\"C\"maxObjectBufferBindCount\"C\"maxMeshBufferBindCount\"C\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"maxKernelThreadgroupMemoryBindCount\"C\"maxObjectThreadgroupMemoryBindCount\"C\"size\"Q}"

```
