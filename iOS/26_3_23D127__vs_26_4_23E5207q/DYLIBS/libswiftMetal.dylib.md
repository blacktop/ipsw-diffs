## libswiftMetal.dylib

> `/usr/lib/swift/libswiftMetal.dylib`

```diff

-371.5.0.0.0
-  __TEXT.__text: 0x4638
-  __TEXT.__auth_stubs: 0x3e0
+372.11.0.0.0
+  __TEXT.__text: 0x4c18
+  __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_methlist: 0x530
-  __TEXT.__const: 0x202
+  __TEXT.__const: 0x20a
   __TEXT.__swift5_typeref: 0x1d3
   __TEXT.__swift5_reflstr: 0x20
   __TEXT.__swift5_assocty: 0x38
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__constg_swiftt: 0x7c
-  __TEXT.__cstring: 0x1d6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xb0
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x2c0
-  __TEXT.__eh_frame: 0x3d8
-  __TEXT.__objc_classname: 0xc8
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__eh_frame: 0x410
+  __TEXT.__objc_classname: 0xf5
   __TEXT.__objc_methname: 0x1d78
-  __TEXT.__objc_methtype: 0x7de
+  __TEXT.__objc_methtype: 0x9a4
+  __TEXT.__objc_stubs: 0xf60
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__data: 0x460
   __DATA.__bss: 0x110
   __DATA.__common: 0x1
-  __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__data: 0x88
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: AF781BAF-E42A-3CA4-BE0D-EE7BDA069A73
-  Functions: 289
-  Symbols:   703
-  CStrings:  303
+  UUID: 8C191750-A40F-363B-B473-3D2A5B1EDA33
+  Functions: 290
+  Symbols:   830
+  CStrings:  304
 
Symbols:
+ _$sSo14MTLSharedEventP5MetalE13valueSignaledyys6UInt64VYaFTY2_
+ _$sSo15MTLCommandQueueP5MetalE16addResidencySetsyySaySo15MTLResidencySet_pGFTm
+ _$sSo15MTLCommandQueueP5MetalE19removeResidencySetsyySaySo15MTLResidencySet_pGFTm
+ _$sSo16MTLCommandBufferP5MetalE9completedyyYaFTY2_
+ _$sSo16MTLCommandBufferP5MetalE9completedyyYaFySccyyts5NeverOGXEfU_
+ _$sSo16MTLCommandBufferP5MetalE9scheduledyyYaFTY2_
+ _$sSo16MTLCommandBufferP5MetalE9scheduledyyYaFySccyyts5NeverOGXEfU_
+ _$sSo21MTLBlitCommandEncoderP5MetalE016optimizeIndirectB6Buffer_5rangeySo011MTLIndirectbG0_p_SnySiGtFTm
+ _$sSo23MTLRenderCommandEncoderP5MetalE23executeCommandsInBuffer_5rangeySo011MTLIndirectbH0_p_SnySiGtFTm
+ _$sSo24MTLComputeCommandEncoderP5MetalE11setTextures_5rangeySaySo10MTLTexture_pSgG_SnySiGtFTm
+ _$sSo24MTLComputeCommandEncoderP5MetalE16setSamplerStates_5rangeySaySo15MTLSamplerState_pSgG_SnySiGtFTm
+ _$sSo28MTLIntersectionFunctionTableP5MetalE010setVisibleB6Tables_11bufferRangeySaySo010MTLVisiblebC0_pSgG_SnySiGtFTm
+ _$sSo38MTLAccelerationStructureCommandEncoderP5MetalE8useHeapsyySaySo7MTLHeap_pGFTm
+ _block_copy_helper.26
+ _block_copy_helper.32
+ _block_copy_helper.38
+ _block_copy_helper.44
+ _block_copy_helper.50
+ _block_copy_helper.56
+ _block_copy_helper.62
+ _block_copy_helper.68
+ _block_copy_helper.74
+ _block_copy_helper.80
+ _block_descriptor.28
+ _block_descriptor.34
+ _block_descriptor.40
+ _block_descriptor.46
+ _block_descriptor.52
+ _block_descriptor.58
+ _block_descriptor.64
+ _block_descriptor.70
+ _block_descriptor.76
+ _block_descriptor.82
+ _block_destroy_helper.27
+ _block_destroy_helper.33
+ _block_destroy_helper.39
+ _block_destroy_helper.45
+ _block_destroy_helper.51
+ _block_destroy_helper.57
+ _block_destroy_helper.63
+ _block_destroy_helper.69
+ _block_destroy_helper.75
+ _block_destroy_helper.81
+ _objc_msgSend$__getRawArray:
+ _objc_msgSend$__waitUntilCompletedAsync:
+ _objc_msgSend$__waitUntilScheduledAsync:
+ _objc_msgSend$addAllocations:count:
+ _objc_msgSend$addDebugMarker:range:
+ _objc_msgSend$addResidencySets:count:
+ _objc_msgSend$barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:
+ _objc_msgSend$barrierAfterQueueStages:beforeStages:visibilityOptions:
+ _objc_msgSend$barrierAfterStages:beforeQueueStages:visibilityOptions:
+ _objc_msgSend$commit:count:
+ _objc_msgSend$commit:count:options:
+ _objc_msgSend$copyBufferMappingsFromBuffer:toBuffer:operations:count:
+ _objc_msgSend$copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:
+ _objc_msgSend$copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:
+ _objc_msgSend$copyResourceViewsFromPool:sourceRange:destinationIndex:
+ _objc_msgSend$copyTextureMappingsFromTexture:toTexture:operations:count:
+ _objc_msgSend$didModifyRange:
+ _objc_msgSend$executeCommandsInBuffer:withRange:
+ _objc_msgSend$extentAtDimensionIndex:
+ _objc_msgSend$fillBuffer:range:value:
+ _objc_msgSend$getDefaultSamplePositions:count:
+ _objc_msgSend$getPhysicalIndexForLogicalIndex:
+ _objc_msgSend$getSamplePositions:count:
+ _objc_msgSend$initWithRank:values:
+ _objc_msgSend$initWithSampleCount:horizontal:vertical:
+ _objc_msgSend$invalidateCounterRange:
+ _objc_msgSend$levelRange
+ _objc_msgSend$logs
+ _objc_msgSend$memoryBarrierWithResources:count:
+ _objc_msgSend$memoryBarrierWithResources:count:afterStages:beforeStages:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:error:
+ _objc_msgSend$newDynamicLibrary:completionHandler:
+ _objc_msgSend$newDynamicLibraryWithURL:completionHandler:
+ _objc_msgSend$newLibraryWithDescriptor:completionHandler:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:completionHandler:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithMeshDescriptor:options:reflection:error:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:
+ _objc_msgSend$notifyListener:atValue:block:
+ _objc_msgSend$optimizeIndirectCommandBuffer:withRange:
+ _objc_msgSend$rank
+ _objc_msgSend$rasterizationRateMapDescriptorWithScreenSize:
+ _objc_msgSend$rasterizationRateMapDescriptorWithScreenSize:layer:
+ _objc_msgSend$rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:
+ _objc_msgSend$removeAllocations:count:
+ _objc_msgSend$removeResidencySets:count:
+ _objc_msgSend$resetCommandsInBuffer:withRange:
+ _objc_msgSend$resetWithRange:
+ _objc_msgSend$resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:
+ _objc_msgSend$resolveCounterRange:
+ _objc_msgSend$resolveCounters:inRange:destinationBuffer:destinationOffset:
+ _objc_msgSend$sampleTimestamps:gpuTimestamp:
+ _objc_msgSend$setBuffers:offsets:attributeStrides:withRange:
+ _objc_msgSend$setBuffers:offsets:withRange:
+ _objc_msgSend$setConstantValues:type:withRange:
+ _objc_msgSend$setDepthStencilStates:withRange:
+ _objc_msgSend$setDepthTestMinBound:maxBound:
+ _objc_msgSend$setFragmentBuffers:offsets:withRange:
+ _objc_msgSend$setFragmentIntersectionFunctionTables:withBufferRange:
+ _objc_msgSend$setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setFragmentSamplerStates:withRange:
+ _objc_msgSend$setFragmentTextures:withRange:
+ _objc_msgSend$setFragmentVisibleFunctionTables:withBufferRange:
+ _objc_msgSend$setFunctions:withRange:
+ _objc_msgSend$setIndirectCommandBuffers:withRange:
+ _objc_msgSend$setInputDimensions:withRange:
+ _objc_msgSend$setIntersectionFunctionTables:withBufferRange:
+ _objc_msgSend$setIntersectionFunctionTables:withRange:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLevelRange:
+ _objc_msgSend$setMeshBuffers:offsets:withRange:
+ _objc_msgSend$setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setMeshSamplerStates:withRange:
+ _objc_msgSend$setMeshTextures:withRange:
+ _objc_msgSend$setObjectBuffers:offsets:withRange:
+ _objc_msgSend$setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setObjectSamplerStates:withRange:
+ _objc_msgSend$setObjectTextures:withRange:
+ _objc_msgSend$setPhysicalIndex:forLogicalIndex:
+ _objc_msgSend$setRenderPipelineStates:withRange:
+ _objc_msgSend$setSamplePositions:count:
+ _objc_msgSend$setSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setSamplerStates:withRange:
+ _objc_msgSend$setScissorRects:count:
+ _objc_msgSend$setSliceRange:
+ _objc_msgSend$setTextures:withRange:
+ _objc_msgSend$setTileBuffers:offsets:withRange:
+ _objc_msgSend$setTileIntersectionFunctionTables:withBufferRange:
+ _objc_msgSend$setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setTileSamplerStates:withRange:
+ _objc_msgSend$setTileTextures:withRange:
+ _objc_msgSend$setTileVisibleFunctionTables:withBufferRange:
+ _objc_msgSend$setVertexAmplificationCount:viewMappings:
+ _objc_msgSend$setVertexBuffers:offsets:attributeStrides:withRange:
+ _objc_msgSend$setVertexBuffers:offsets:withRange:
+ _objc_msgSend$setVertexIntersectionFunctionTables:withBufferRange:
+ _objc_msgSend$setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setVertexSamplerStates:withRange:
+ _objc_msgSend$setVertexTextures:withRange:
+ _objc_msgSend$setVertexVisibleFunctionTables:withBufferRange:
+ _objc_msgSend$setViewports:count:
+ _objc_msgSend$setVisibleFunctionTables:withBufferRange:
+ _objc_msgSend$setVisibleFunctionTables:withRange:
+ _objc_msgSend$sharedListener
+ _objc_msgSend$sliceRange
+ _objc_msgSend$updateBufferMappings:heap:operations:count:
+ _objc_msgSend$updateTextureMappings:heap:operations:count:
+ _objc_msgSend$useHeaps:count:
+ _objc_msgSend$useResidencySets:count:
+ _objc_msgSend$useResources:count:usage:
- _$sSS11withCStringyxxSPys4Int8VGKXEKlFSvSg_Tg5085$s5Metal29MTLIOCreateCompressionContextySvSgSS_So22MTLIOCompressionMethodVSitFACSPys4C7VGXEfU_So0mN0VSiTf1cn_n
- _$sSo11MTL4ArchiveP5MetalE24makeComputePipelineState10descriptor24dynamicLinkingDescriptorSo010MTLComputefG0_pSo0aefK0C_So0af12StageDynamicjK0CSgtKFTm
- _$sSo12MTL4CompilerP5MetalE24makeComputePipelineState10descriptor24dynamicLinkingDescriptor19compilerTaskOptionsSo010MTLComputefG0_pSo0aefK0C_So0af12StageDynamicjK0CSgSo0abmN0CSgtKFTm
- _$sSo16MTLCommandBufferP5MetalE9scheduledyyYaFySccyyts5NeverOGXEfU_Tm
- _$sSo24MTLComputeCommandEncoderP5MetalE10setBuffers_7offsets16attributeStrides5rangeySaySo9MTLBuffer_pSgG_SaySiGAKSnySiGtFTm
- _$sSo24MTLTextureViewDescriptorC5MetalE10levelRangeSnySiGvM.resume.0Tm
- _$sSo24MTLTextureViewDescriptorC5MetalE10levelRangeSnySiGvgTm
- _$sSo24MTLTextureViewDescriptorC5MetalE10levelRangeSnySiGvpABTKTm
- _$sSo24MTLTextureViewDescriptorC5MetalE10levelRangeSnySiGvpABTkTm
- _$sSo24MTLTextureViewDescriptorC5MetalE10levelRangeSnySiGvsTm
- _$sSo9MTLBufferP5MetalE14didModifyRangeyySnySiGFTm
- _block_copy_helper.25
- _block_copy_helper.31
- _block_copy_helper.37
- _block_copy_helper.43
- _block_copy_helper.49
- _block_copy_helper.55
- _block_copy_helper.61
- _block_copy_helper.67
- _block_copy_helper.73
- _block_copy_helper.79
- _block_descriptor.27
- _block_descriptor.33
- _block_descriptor.39
- _block_descriptor.45
- _block_descriptor.51
- _block_descriptor.57
- _block_descriptor.63
- _block_descriptor.69
- _block_descriptor.75
- _block_descriptor.81
- _block_destroy_helper.26
- _block_destroy_helper.32
- _block_destroy_helper.38
- _block_destroy_helper.44
- _block_destroy_helper.50
- _block_destroy_helper.56
- _block_destroy_helper.62
- _block_destroy_helper.68
- _block_destroy_helper.74
- _block_destroy_helper.80
CStrings:
+ "Metal"

```
