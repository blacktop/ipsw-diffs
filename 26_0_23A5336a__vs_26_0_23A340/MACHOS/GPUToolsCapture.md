## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

 310.33.0.0.0
-  __TEXT.__text: 0x267dc4
+  __TEXT.__text: 0x26a1d8
   __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x16080
+  __TEXT.__objc_stubs: 0x167e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12194
-  __TEXT.__const: 0x79c8
-  __TEXT.__cstring: 0x26b12
-  __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__objc_methname: 0x19546
+  __TEXT.__objc_methlist: 0x12474
+  __TEXT.__const: 0x79d0
+  __TEXT.__cstring: 0x26b85
+  __TEXT.__gcc_except_tab: 0x8c8
+  __TEXT.__objc_methname: 0x19af8
   __TEXT.__objc_classname: 0x157b
-  __TEXT.__objc_methtype: 0x9bfe
+  __TEXT.__objc_methtype: 0x9c72
   __TEXT.__oslogstring: 0xedb
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x3ed0
+  __TEXT.__unwind_info: 0x3f00
   __DATA_CONST.__auth_got: 0xbd8
   __DATA_CONST.__got: 0x800
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1a78
+  __DATA_CONST.__const: 0x1bd8
   __DATA_CONST.__cfstring: 0x3ba0
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19800
-  __DATA.__objc_selrefs: 0x67d0
+  __DATA.__objc_const: 0x19a48
+  __DATA.__objc_selrefs: 0x69f8
   __DATA.__objc_ivar: 0xa8c
   __DATA.__objc_data: 0x1ea0
   __DATA.__data: 0x3458
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0x1018
-  __DATA.__bss: 0x4d8
+  __DATA.__bss: 0x530
   __DATA.__common: 0x4d
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 97670B4B-3C26-3C7C-8F80-1CA80FD893A4
-  Functions: 7697
-  Symbols:   45769
-  CStrings:  8937
+  UUID: 41C1F9D3-914C-3F6E-91EC-4ED4C4D55D4D
+  Functions: 7743
+  Symbols:   46102
+  CStrings:  9012
 
Symbols:
+ -[CaptureMTL4RenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[CaptureMTLArgumentEncoder setDepthStencilState:atIndex:]
+ -[CaptureMTLArgumentEncoder setDepthStencilStates:withRange:]
+ -[CaptureMTLDepthStencilState gpuResourceID]
+ -[CaptureMTLDepthStencilState resourceIndex]
+ -[CaptureMTLDepthStencilState uniqueIdentifier]
+ -[CaptureMTLDevice samplerReductionModeSupport]
+ -[CaptureMTLIndirectRenderCommand getBlendColor]
+ -[CaptureMTLIndirectRenderCommand getCullMode]
+ -[CaptureMTLIndirectRenderCommand getDepthBiasInfo]
+ -[CaptureMTLIndirectRenderCommand getDepthClipMode]
+ -[CaptureMTLIndirectRenderCommand getDepthStencilStateUniqueIdentifier]
+ -[CaptureMTLIndirectRenderCommand getDepthStencilState]
+ -[CaptureMTLIndirectRenderCommand getDepthTestBounds]
+ -[CaptureMTLIndirectRenderCommand getFrontFacingWinding]
+ -[CaptureMTLIndirectRenderCommand getScissorRects]
+ -[CaptureMTLIndirectRenderCommand getStencilReferenceValues]
+ -[CaptureMTLIndirectRenderCommand getTriangleFillMode]
+ -[CaptureMTLIndirectRenderCommand getViewports]
+ -[CaptureMTLIndirectRenderCommand setBlendColorRed:green:blue:alpha:]
+ -[CaptureMTLIndirectRenderCommand setCullMode:]
+ -[CaptureMTLIndirectRenderCommand setDepthBias:slopeScale:clamp:]
+ -[CaptureMTLIndirectRenderCommand setDepthClipMode:]
+ -[CaptureMTLIndirectRenderCommand setDepthStencilState:]
+ -[CaptureMTLIndirectRenderCommand setDepthTestMinBound:maxBound:]
+ -[CaptureMTLIndirectRenderCommand setFrontFacingWinding:]
+ -[CaptureMTLIndirectRenderCommand setScissorRect:]
+ -[CaptureMTLIndirectRenderCommand setScissorRects:count:]
+ -[CaptureMTLIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:]
+ -[CaptureMTLIndirectRenderCommand setStencilReferenceValue:]
+ -[CaptureMTLIndirectRenderCommand setTriangleFillMode:]
+ -[CaptureMTLIndirectRenderCommand setViewport:]
+ -[CaptureMTLIndirectRenderCommand setViewports:count:]
+ -[CaptureMTLRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[CaptureMTLRenderCommandEncoder setDepthTestMinBound:maxBound:]
+ GCC_except_table1504
+ GCC_except_table1529
+ GCC_except_table1634
+ GCC_except_table1635
+ GCC_except_table1639
+ GCC_except_table1640
+ GCC_except_table1641
+ GCC_except_table1642
+ GCC_except_table1643
+ GCC_except_table1849
+ GCC_except_table1850
+ GCC_except_table1852
+ GCC_except_table1854
+ GCC_except_table1863
+ GCC_except_table2007
+ GCC_except_table2044
+ GCC_except_table2988
+ GCC_except_table3149
+ GCC_except_table3243
+ GCC_except_table3960
+ GCC_except_table4500
+ GCC_except_table644
+ GTAccelerationStructureDescriptorDownloader_processCopy.7849
+ GTAccelerationStructureDescriptorDownloader_processRefit.7850
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.46
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.51
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.56
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.61
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.66
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.71
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.76
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.81
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.86
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.91
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.96
+ GetStream.19681
+ RetainObjectForDescriptorDownloader.9443
+ StoreMTLCompileOptionsUsingEncode.16206
+ __Block_byref_object_copy_.11526
+ __Block_byref_object_copy_.3915
+ __Block_byref_object_copy_.4419
+ __Block_byref_object_dispose_.11527
+ __Block_byref_object_dispose_.3916
+ __Block_byref_object_dispose_.4420
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_10
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_11
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_12
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_13
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_3
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_4
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_5
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_6
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_7
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_8
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_9
+ __block_descriptor_tmp.14936
+ __block_literal_global.10265
+ __block_literal_global.10761
+ __block_literal_global.11530
+ __block_literal_global.11977
+ __block_literal_global.14849
+ __block_literal_global.15034
+ __block_literal_global.15101
+ __block_literal_global.15114
+ __block_literal_global.1672
+ __block_literal_global.20066
+ __block_literal_global.2959
+ __block_literal_global.4243
+ __block_literal_global.4428
+ __block_literal_global.472
+ __block_literal_global.48
+ __block_literal_global.53
+ __block_literal_global.58
+ __block_literal_global.63
+ __block_literal_global.68
+ __block_literal_global.7262
+ __block_literal_global.73
+ __block_literal_global.78
+ __block_literal_global.8032
+ __block_literal_global.83
+ __block_literal_global.8460
+ __block_literal_global.88
+ __block_literal_global.93
+ __block_literal_global.9420
+ __block_literal_global.98
+ _objc_msgSend$alpha
+ _objc_msgSend$backReferenceValue
+ _objc_msgSend$blue
+ _objc_msgSend$clamp
+ _objc_msgSend$depthBias
+ _objc_msgSend$dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:
+ _objc_msgSend$frontReferenceValue
+ _objc_msgSend$getBlendColor
+ _objc_msgSend$getCullMode
+ _objc_msgSend$getDepthBiasInfo
+ _objc_msgSend$getDepthClipMode
+ _objc_msgSend$getDepthStencilState
+ _objc_msgSend$getDepthStencilStateUniqueIdentifier
+ _objc_msgSend$getDepthTestBounds
+ _objc_msgSend$getFrontFacingWinding
+ _objc_msgSend$getScissorRects
+ _objc_msgSend$getStencilReferenceValues
+ _objc_msgSend$getTriangleFillMode
+ _objc_msgSend$getViewports
+ _objc_msgSend$green
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
+ _objc_msgSend$lodBias
+ _objc_msgSend$maxBounds
+ _objc_msgSend$maxScissorRectCount
+ _objc_msgSend$minBounds
+ _objc_msgSend$red
+ _objc_msgSend$reductionMode
+ _objc_msgSend$samplerReductionModeSupport
+ _objc_msgSend$scissorRects
+ _objc_msgSend$setDepthStencilState:atIndex:
+ _objc_msgSend$setDepthStencilStates:withRange:
+ _objc_msgSend$setDepthTestMinBound:maxBound:
+ _objc_msgSend$setInheritBlendColor:
+ _objc_msgSend$setInheritCullMode:
+ _objc_msgSend$setInheritDepthBias:
+ _objc_msgSend$setInheritDepthClipMode:
+ _objc_msgSend$setInheritDepthStencilState:
+ _objc_msgSend$setInheritDepthTestBounds:
+ _objc_msgSend$setInheritFrontFacingWinding:
+ _objc_msgSend$setInheritScissorRects:
+ _objc_msgSend$setInheritStencilReferenceValues:
+ _objc_msgSend$setInheritTriangleFillMode:
+ _objc_msgSend$setInheritViewports:
+ _objc_msgSend$setLodBias:
+ _objc_msgSend$setMaxScissorRectCount:
+ _objc_msgSend$setMaxViewportCount:
+ _objc_msgSend$setReductionMode:
+ _objc_msgSend$slopeScale
+ _objc_msgSend$viewports
+ name_array.16148
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7823
+ s_downloaderPipelines.0.7830
+ s_downloaderPipelines.1.7831
+ s_downloaderPipelines.2.7832
+ s_downloaderPipelines.3.7833
+ s_downloaderPipelines.4.7834
+ waitUntilSignaledValue:timeoutMS:.onceToken.13362
- GCC_except_table1491
- GCC_except_table1516
- GCC_except_table1618
- GCC_except_table1619
- GCC_except_table1623
- GCC_except_table1624
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table1627
- GCC_except_table1833
- GCC_except_table1834
- GCC_except_table1836
- GCC_except_table1838
- GCC_except_table1847
- GCC_except_table1991
- GCC_except_table2028
- GCC_except_table2968
- GCC_except_table3129
- GCC_except_table3223
- GCC_except_table3940
- GCC_except_table4454
- GCC_except_table633
- GTAccelerationStructureDescriptorDownloader_processCopy.7837
- GTAccelerationStructureDescriptorDownloader_processRefit.7838
- GetStream.19609
- RetainObjectForDescriptorDownloader.9434
- StoreMTLCompileOptionsUsingEncode.16134
- __Block_byref_object_copy_.11516
- __Block_byref_object_copy_.3894
- __Block_byref_object_copy_.4397
- __Block_byref_object_dispose_.11517
- __Block_byref_object_dispose_.3895
- __Block_byref_object_dispose_.4398
- __block_descriptor_tmp.14876
- __block_literal_global.10255
- __block_literal_global.10751
- __block_literal_global.11520
- __block_literal_global.11966
- __block_literal_global.14789
- __block_literal_global.14974
- __block_literal_global.15041
- __block_literal_global.15054
- __block_literal_global.1656
- __block_literal_global.19994
- __block_literal_global.2936
- __block_literal_global.4221
- __block_literal_global.4406
- __block_literal_global.457
- __block_literal_global.7250
- __block_literal_global.8020
- __block_literal_global.8447
- __block_literal_global.9411
- name_array.16076
- s_accelerationStructureDescriptorDownloaderPipelinesToken.7811
- s_downloaderPipelines.0.7818
- s_downloaderPipelines.1.7819
- s_downloaderPipelines.2.7820
- s_downloaderPipelines.3.7821
- s_downloaderPipelines.4.7822
- waitUntilSignaledValue:timeoutMS:.onceToken.13306
CStrings:
+ "Conditional Tile Dispatch"
+ "Tq,?,R"
+ "alpha"
+ "backReferenceValue"
+ "blue"
+ "clamp"
+ "depthBias"
+ "dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:"
+ "dispatchThreadsPerTile:withCondition:"
+ "frontReferenceValue"
+ "getBlendColor"
+ "getCullMode"
+ "getDepthBiasInfo"
+ "getDepthClipMode"
+ "getDepthStencilState"
+ "getDepthStencilStateUniqueIdentifier"
+ "getDepthTestBounds"
+ "getFrontFacingWinding"
+ "getScissorRects"
+ "getStencilReferenceValues"
+ "getTriangleFillMode"
+ "getViewports"
+ "green"
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
+ "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
+ "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
+ "lodBias"
+ "maxBounds"
+ "maxScissorRectCount"
+ "minBounds"
+ "red"
+ "reductionMode"
+ "resetTileCondition"
+ "samplerReductionModeSupport"
+ "scissorRects"
+ "setDepthStencilState:atIndex:"
+ "setDepthStencilStates:withRange:"
+ "setDepthTestMinBound:maxBound:"
+ "setInheritBlendColor:"
+ "setInheritCullMode:"
+ "setInheritDepthBias:"
+ "setInheritDepthClipMode:"
+ "setInheritDepthStencilState:"
+ "setInheritDepthTestBounds:"
+ "setInheritFrontFacingWinding:"
+ "setInheritScissorRects:"
+ "setInheritStencilReferenceValues:"
+ "setInheritTriangleFillMode:"
+ "setInheritViewports:"
+ "setLodBias:"
+ "setMaxScissorRectCount:"
+ "setMaxViewportCount:"
+ "setReductionMode:"
+ "slopeScale"
+ "supportsConditionalTileDispatch"
+ "supportsDepthBoundsTesting"
+ "supportsExtendedIndirectRenderCommand"
+ "supportsFP8"
+ "supportsMXU"
+ "supportsSamplerReductionMode"
+ "supportsTextureAccessPatterns"
+ "v100@0:8{?=QQQ}16{?={?=QQQ}{?=QQQ}}40I88q92"
+ "v24@0:8f16f20"
+ "v32@0:8@\"<MTLDepthStencilState>\"16Q24"
+ "v48@0:8{?=QQQ}16q40"
+ "viewports"
+ "writeAccessPattern"
- "0xffffc0e9"
- "0xffffc0ea"

```
