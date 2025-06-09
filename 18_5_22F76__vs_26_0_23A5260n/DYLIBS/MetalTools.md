## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-368.12.0.0.0
-  __TEXT.__text: 0xefb74
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x1433c
-  __TEXT.__cstring: 0x24c8a
-  __TEXT.__gcc_except_tab: 0x2798
-  __TEXT.__const: 0x260
-  __TEXT.__oslogstring: 0x280f
-  __TEXT.__unwind_info: 0x4340
-  __TEXT.__objc_classname: 0x1be4
-  __TEXT.__objc_methname: 0x17c58
-  __TEXT.__objc_methtype: 0x1a1bc
-  __TEXT.__objc_stubs: 0x12240
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__const: 0x16a8
-  __DATA_CONST.__objc_classlist: 0x5f0
-  __DATA_CONST.__objc_protolist: 0x310
+370.50.4.0.0
+  __TEXT.__text: 0x12a2f4
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x18bcc
+  __TEXT.__cstring: 0x31343
+  __TEXT.__const: 0x308
+  __TEXT.__gcc_except_tab: 0x2b50
+  __TEXT.__oslogstring: 0x282e
+  __TEXT.__unwind_info: 0x5040
+  __TEXT.__objc_classname: 0x2520
+  __TEXT.__objc_methname: 0x1e11b
+  __TEXT.__objc_methtype: 0x1795d
+  __TEXT.__objc_stubs: 0x164e0
+  __DATA_CONST.__got: 0xae8
+  __DATA_CONST.__const: 0x1b28
+  __DATA_CONST.__objc_classlist: 0x748
+  __DATA_CONST.__objc_protolist: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ef0
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x510
-  __AUTH_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__objc_selrefs: 0x60e8
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x640
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xb1a0
-  __AUTH_CONST.__objc_const: 0x38d88
+  __AUTH_CONST.__cfstring: 0xe2a0
+  __AUTH_CONST.__objc_const: 0x45aa8
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0xd40
-  __DATA.__data: 0x24d0
-  __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x3b60
+  __DATA.__objc_ivar: 0xfe4
+  __DATA.__data: 0x3970
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0x4880
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25C1577A-3DAA-3220-BB74-7BAF414194F0
-  Functions: 6316
-  Symbols:   19956
-  CStrings:  8607
+  UUID: 98E77F70-116E-3CD5-B080-92DFB2F2F3CE
+  Functions: 7641
+  Symbols:   24259
+  CStrings:  10853
 
Symbols:
+ +[MTLToolsDevice newUnwrappedMTLRelocations:]
+ -[GPUDebugRetainedReportingData .cxx_construct]
+ -[GPUDebugRetainedReportingData .cxx_destruct]
+ -[GPUDebugRetainedReportingData addUsedBuffer:]
+ -[GPUDebugRetainedReportingData cbAllocations]
+ -[GPUDebugRetainedReportingData cbResidencySet]
+ -[GPUDebugRetainedReportingData dealloc]
+ -[GPUDebugRetainedReportingData encoderLabels]
+ -[GPUDebugRetainedReportingData init:]
+ -[GPUDebugRetainedReportingData privateData]
+ -[GPUDebugRetainedReportingData setCbAllocations:]
+ -[GPUDebugRetainedReportingData setCbResidencySet:]
+ -[GPUDebugRetainedReportingData setEncoderLabelForIndex:encoderIndex:]
+ -[GPUDebugRetainedReportingData setEncoderLabels:]
+ -[GPUDebugRetainedReportingData setPrivateData:]
+ -[GPUDebugRetainedReportingData setUsedBuffers:]
+ -[GPUDebugRetainedReportingData setUsedPipelineStates:]
+ -[GPUDebugRetainedReportingData usedBuffers]
+ -[GPUDebugRetainedReportingData usedPipelineStates]
+ -[MTL4DebugArchive initWithArchive:device:]
+ -[MTL4DebugArchive newArchiveReplyForPipelineFunctionWithDescriptor:functionType:functionId:]
+ -[MTL4DebugArchive newBinaryFunctionWithDescriptor:error:]
+ -[MTL4DebugArchive newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4DebugArchive newComputePipelineStateWithDescriptor:error:]
+ -[MTL4DebugArchive newComputePipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4DebugArchive newComputePipelineStateWithName:error:]
+ -[MTL4DebugArchive newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4DebugArchive newRenderPipelineStateWithDescriptor:error:]
+ -[MTL4DebugArchive newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4DebugArchive newRenderPipelineStateWithName:error:]
+ -[MTL4DebugArgumentTable .cxx_construct]
+ -[MTL4DebugArgumentTable .cxx_destruct]
+ -[MTL4DebugArgumentTable bufferBindingAtIndex:]
+ -[MTL4DebugArgumentTable initWithArgumentTable:device:descriptor:]
+ -[MTL4DebugArgumentTable samplerBindingAtIndex:]
+ -[MTL4DebugArgumentTable setAddress:atIndex:]
+ -[MTL4DebugArgumentTable setAddress:attributeStride:atIndex:]
+ -[MTL4DebugArgumentTable setResource:atBufferIndex:]
+ -[MTL4DebugArgumentTable setSamplerState:atIndex:]
+ -[MTL4DebugArgumentTable setTexture:atIndex:]
+ -[MTL4DebugArgumentTable textureBindingAtIndex:]
+ -[MTL4DebugCommandAllocator currentGeneration]
+ -[MTL4DebugCommandAllocator initWithBaseObject:parent:]
+ -[MTL4DebugCommandAllocator reset]
+ -[MTL4DebugCommandBuffer .cxx_construct]
+ -[MTL4DebugCommandBuffer .cxx_destruct]
+ -[MTL4DebugCommandBuffer _clearSuspendResumeRenderPassInfo]
+ -[MTL4DebugCommandBuffer _resetRenderPassAttachmentTracking]
+ -[MTL4DebugCommandBuffer aggregatedEncoderMask]
+ -[MTL4DebugCommandBuffer attachmentSet]
+ -[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:]
+ -[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:options:]
+ -[MTL4DebugCommandBuffer commandAllocator]
+ -[MTL4DebugCommandBuffer computeCommandEncoderWithSubstreamCount:]
+ -[MTL4DebugCommandBuffer computeCommandEncoder]
+ -[MTL4DebugCommandBuffer currentState]
+ -[MTL4DebugCommandBuffer dealloc]
+ -[MTL4DebugCommandBuffer endCommandBuffer]
+ -[MTL4DebugCommandBuffer initWithCommandBuffer:device:]
+ -[MTL4DebugCommandBuffer isAllocatorGenerationValid]
+ -[MTL4DebugCommandBuffer machineLearningCommandEncoder]
+ -[MTL4DebugCommandBuffer onCurrentEncoderEnded]
+ -[MTL4DebugCommandBuffer popDebugGroup]
+ -[MTL4DebugCommandBuffer pushDebugGroup:]
+ -[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:]
+ -[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:options:]
+ -[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:]
+ -[MTL4DebugCommandBuffer sampledComputeCommandEncoder:capacity:]
+ -[MTL4DebugCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:]
+ -[MTL4DebugCommandBuffer setCurrentState:]
+ -[MTL4DebugCommandBuffer suspendResumeRenderPassInfo]
+ -[MTL4DebugCommandBuffer useResidencySet:]
+ -[MTL4DebugCommandBuffer useResidencySets:count:]
+ -[MTL4DebugCommandBuffer writeTimestampIntoHeap:atIndex:]
+ -[MTL4DebugCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[MTL4DebugCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[MTL4DebugCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[MTL4DebugCommandEncoder canEndEncoding]
+ -[MTL4DebugCommandEncoder commandBatchIdOffset]
+ -[MTL4DebugCommandEncoder commandBatchIdRangeMin:max:]
+ -[MTL4DebugCommandEncoder endEncodingAndRetrieveProgramAddressTable]
+ -[MTL4DebugCommandEncoder endEncodingPreamble]
+ -[MTL4DebugCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:]
+ -[MTL4DebugCommandEncoder hasEndEncoding]
+ -[MTL4DebugCommandEncoder initWithBaseObject:device:commandBuffer:encoderStageMask:]
+ -[MTL4DebugCommandEncoder resetEncoderState]
+ -[MTL4DebugCommandEncoder setCanEndEncoding:]
+ -[MTL4DebugCommandEncoder updateFence:afterEncoderStages:]
+ -[MTL4DebugCommandEncoder validateFunctionArguments:stage:functionName:argumentTable:boundThreadgroupMemoryArguments:bindings:allowNullBufferBindings:]
+ -[MTL4DebugCommandEncoder waitForFence:beforeEncoderStages:]
+ -[MTL4DebugCommandQueue addResidencySet:]
+ -[MTL4DebugCommandQueue addResidencySets:count:]
+ -[MTL4DebugCommandQueue commit:count:]
+ -[MTL4DebugCommandQueue commit:count:options:]
+ -[MTL4DebugCommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:]
+ -[MTL4DebugCommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:]
+ -[MTL4DebugCommandQueue dealloc]
+ -[MTL4DebugCommandQueue initWithBaseObject:parent:]
+ -[MTL4DebugCommandQueue removeResidencySet:]
+ -[MTL4DebugCommandQueue removeResidencySets:count:]
+ -[MTL4DebugCommandQueue signalDrawable:]
+ -[MTL4DebugCommandQueue signalEvent:value:]
+ -[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:]
+ -[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:].cold.1
+ -[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:].cold.2
+ -[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:].cold.3
+ -[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:]
+ -[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:].cold.1
+ -[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:].cold.2
+ -[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:].cold.3
+ -[MTL4DebugCommandQueue validateBufferAccess:range:resourceSparsePageSize:context:]
+ -[MTL4DebugCommandQueue validateBufferAccess:region:resourceSparsePageSize:context:]
+ -[MTL4DebugCommandQueue validateCommitCommon:commandBuffers:count:]
+ -[MTL4DebugCommandQueue validateHeapAccess:rangeOffset:tileRegions:resourceSparsePageSize:context:]
+ -[MTL4DebugCommandQueue validateTextureAccess:region:mipLevel:slice:context:]
+ -[MTL4DebugCommandQueue validateTextureAccess:region:mipLevel:slice:context:].cold.1
+ -[MTL4DebugCommandQueue validateTextureAccess:region:mipLevel:slice:context:].cold.2
+ -[MTL4DebugCommandQueue waitForDrawable:]
+ -[MTL4DebugCommandQueue waitForEvent:value:]
+ -[MTL4DebugCommandQueue waitForEvent:value:timeout:]
+ -[MTL4DebugCompiler hasUnspecializedProperties:]
+ -[MTL4DebugCompiler initWithCompiler:device:]
+ -[MTL4DebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4DebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4DebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4DebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4DebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4DebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4DebugCompiler newDynamicLibrary:completionHandler:]
+ -[MTL4DebugCompiler newDynamicLibrary:error:]
+ -[MTL4DebugCompiler newDynamicLibraryWithURL:completionHandler:]
+ -[MTL4DebugCompiler newDynamicLibraryWithURL:error:]
+ -[MTL4DebugCompiler newDynamicLibraryWithURL:options:completionHandler:]
+ -[MTL4DebugCompiler newDynamicLibraryWithURL:options:error:]
+ -[MTL4DebugCompiler newLibraryWithDescriptor:completionHandler:]
+ -[MTL4DebugCompiler newLibraryWithDescriptor:error:]
+ -[MTL4DebugCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:]
+ -[MTL4DebugCompiler newMachineLearningPipelineStateWithDescriptor:error:]
+ -[MTL4DebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]
+ -[MTL4DebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:]
+ -[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4DebugCompiler newSpecializedMTL4PipelineDescriptor:descriptor:]
+ -[MTL4DebugComputeCommandEncoder .cxx_construct]
+ -[MTL4DebugComputeCommandEncoder .cxx_destruct]
+ -[MTL4DebugComputeCommandEncoder _resetEncoder]
+ -[MTL4DebugComputeCommandEncoder _updateEncoderStateAfterDispatch]
+ -[MTL4DebugComputeCommandEncoder _validateComputeFunctionArguments:]
+ -[MTL4DebugComputeCommandEncoder _validateComputeFunctionArguments:].cold.1
+ -[MTL4DebugComputeCommandEncoder _validateComputeFunctionBuiltinArguments:threadsPerThreadgroup:threadgroupsPerGrid:]
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:]
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.1
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.2
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:].cold.1
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:].cold.2
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.1
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.2
+ -[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.3
+ -[MTL4DebugComputeCommandEncoder _validateFillTextureCommon:texture:level:slice:region:]
+ -[MTL4DebugComputeCommandEncoder _validateFillTextureCommon:texture:level:slice:region:].cold.1
+ -[MTL4DebugComputeCommandEncoder _validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:]
+ -[MTL4DebugComputeCommandEncoder _validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:].cold.1
+ -[MTL4DebugComputeCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[MTL4DebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[MTL4DebugComputeCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[MTL4DebugComputeCommandEncoder beginVirtualSubstream]
+ -[MTL4DebugComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:]
+ -[MTL4DebugComputeCommandEncoder commandBuffer]
+ -[MTL4DebugComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:]
+ -[MTL4DebugComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:]
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.1
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:]
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:].cold.1
+ -[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:].cold.2
+ -[MTL4DebugComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:]
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:].cold.1
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:]
+ -[MTL4DebugComputeCommandEncoder copyFromTexture:toTexture:]
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:]
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.1
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.2
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.3
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.4
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.5
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.6
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.7
+ -[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.8
+ -[MTL4DebugComputeCommandEncoder dealloc]
+ -[MTL4DebugComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:]
+ -[MTL4DebugComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:]
+ -[MTL4DebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:]
+ -[MTL4DebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:]
+ -[MTL4DebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:]
+ -[MTL4DebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:]
+ -[MTL4DebugComputeCommandEncoder enableNullBufferBinds:]
+ -[MTL4DebugComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:]
+ -[MTL4DebugComputeCommandEncoder encodeEndIf]
+ -[MTL4DebugComputeCommandEncoder encodeEndWhile]
+ -[MTL4DebugComputeCommandEncoder encodeStartDoWhile]
+ -[MTL4DebugComputeCommandEncoder encodeStartElse]
+ -[MTL4DebugComputeCommandEncoder encodeStartIf:comparison:referenceValue:]
+ -[MTL4DebugComputeCommandEncoder encodeStartWhile:comparison:referenceValue:]
+ -[MTL4DebugComputeCommandEncoder endEncoding]
+ -[MTL4DebugComputeCommandEncoder endVirtualSubstream]
+ -[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4DebugComputeCommandEncoder fillBuffer:range:pattern4:]
+ -[MTL4DebugComputeCommandEncoder fillBuffer:range:pattern4:].cold.1
+ -[MTL4DebugComputeCommandEncoder fillBuffer:range:value:]
+ -[MTL4DebugComputeCommandEncoder fillBuffer:range:value:].cold.1
+ -[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:bytes:length:]
+ -[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:]
+ -[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:]
+ -[MTL4DebugComputeCommandEncoder generateMipmapsForTexture:]
+ -[MTL4DebugComputeCommandEncoder generateMipmapsForTexture:].cold.1
+ -[MTL4DebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:]
+ -[MTL4DebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:numSubstreams:]
+ -[MTL4DebugComputeCommandEncoder insertCompressedTextureReinterpretationFlush]
+ -[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:]
+ -[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:slice:level:]
+ -[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:slice:level:].cold.1
+ -[MTL4DebugComputeCommandEncoder nextVirtualSubstream]
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:]
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:]
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:].cold.1
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:]
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:]
+ -[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:].cold.1
+ -[MTL4DebugComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:]
+ -[MTL4DebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:]
+ -[MTL4DebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:]
+ -[MTL4DebugComputeCommandEncoder resetCommandsInBuffer:withRange:]
+ -[MTL4DebugComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder setArgumentTable:]
+ -[MTL4DebugComputeCommandEncoder setComputePipelineState:]
+ -[MTL4DebugComputeCommandEncoder setImageblockWidth:height:]
+ -[MTL4DebugComputeCommandEncoder setSubstream:]
+ -[MTL4DebugComputeCommandEncoder setSubstream:].cold.1
+ -[MTL4DebugComputeCommandEncoder setThreadgroupDistributionMode:]
+ -[MTL4DebugComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:]
+ -[MTL4DebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:]
+ -[MTL4DebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTL4DebugComputeCommandEncoder signalProgress:]
+ -[MTL4DebugComputeCommandEncoder updateFence:afterEncoderStages:]
+ -[MTL4DebugComputeCommandEncoder validateRefit:descriptor:destination:scratchBuffer:options:]
+ -[MTL4DebugComputeCommandEncoder waitForFence:beforeEncoderStages:]
+ -[MTL4DebugComputeCommandEncoder waitForProgress:]
+ -[MTL4DebugComputeCommandEncoder waitForVirtualSubstream:]
+ -[MTL4DebugComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:]
+ -[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:]
+ -[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:]
+ -[MTL4DebugComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:]
+ -[MTL4DebugCounterHeap initWithCounterHeap:device:]
+ -[MTL4DebugCounterHeap invalidateCounterRange:]
+ -[MTL4DebugCounterHeap resolveCounterRange:]
+ -[MTL4DebugMachineLearningCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[MTL4DebugMachineLearningCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[MTL4DebugMachineLearningCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[MTL4DebugMachineLearningCommandEncoder commandBuffer]
+ -[MTL4DebugMachineLearningCommandEncoder dealloc]
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:]
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.1
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.2
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.3
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.4
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.5
+ -[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:].cold.6
+ -[MTL4DebugMachineLearningCommandEncoder endEncoding]
+ -[MTL4DebugMachineLearningCommandEncoder initWithMLCommandEncoder:commandBuffer:]
+ -[MTL4DebugMachineLearningCommandEncoder mlPipelineState]
+ -[MTL4DebugMachineLearningCommandEncoder setArgumentTable:]
+ -[MTL4DebugMachineLearningCommandEncoder setArgumentTable:].cold.1
+ -[MTL4DebugMachineLearningCommandEncoder setArgumentTable:].cold.2
+ -[MTL4DebugMachineLearningCommandEncoder setPipelineState:]
+ -[MTL4DebugMachineLearningCommandEncoder setPipelineState:].cold.1
+ -[MTL4DebugMachineLearningCommandEncoder setPipelineState:].cold.2
+ -[MTL4DebugMachineLearningCommandEncoder updateFence:afterEncoderStages:]
+ -[MTL4DebugMachineLearningCommandEncoder waitForFence:beforeEncoderStages:]
+ -[MTL4DebugMachineLearningPipelineState dealloc]
+ -[MTL4DebugMachineLearningPipelineState descriptor]
+ -[MTL4DebugMachineLearningPipelineState initWithMLPipelineState:parent:descriptor:]
+ -[MTL4DebugRenderCommandEncoder .cxx_construct]
+ -[MTL4DebugRenderCommandEncoder .cxx_destruct]
+ -[MTL4DebugRenderCommandEncoder _resetEncoderWithDescriptor:]
+ -[MTL4DebugRenderCommandEncoder _updateEncoderStateAfterDispatch]
+ -[MTL4DebugRenderCommandEncoder _updateEncoderStateAfterDraw]
+ -[MTL4DebugRenderCommandEncoder _validateDispatchThreadsPerTileCommon:threadsPerTile:]
+ -[MTL4DebugRenderCommandEncoder _validateDispatchThreadsPerTileCommon:threadsPerTile:].cold.1
+ -[MTL4DebugRenderCommandEncoder _validateDispatchThreadsPerTileCommon:threadsPerTile:].cold.2
+ -[MTL4DebugRenderCommandEncoder _validateDrawCommon:primitiveType:instanceCount:]
+ -[MTL4DebugRenderCommandEncoder _validateFramebufferCompatibility:pipelineState:]
+ -[MTL4DebugRenderCommandEncoder _validateFunctionArguments:stages:]
+ -[MTL4DebugRenderCommandEncoder _validateIndexedDrawCommon:indexBuffer:indexType:indexBufferLength:]
+ -[MTL4DebugRenderCommandEncoder _validateLBRT:]
+ -[MTL4DebugRenderCommandEncoder _validateMeshDrawCommon:]
+ -[MTL4DebugRenderCommandEncoder _validateThreadgroupSize:stage:context:]
+ -[MTL4DebugRenderCommandEncoder _validateThreadsPerObjectThreadgroup:threadsPerMeshThreadgroup:context:]
+ -[MTL4DebugRenderCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[MTL4DebugRenderCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[MTL4DebugRenderCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[MTL4DebugRenderCommandEncoder commandBuffer]
+ -[MTL4DebugRenderCommandEncoder dealloc]
+ -[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:]
+ -[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:]
+ -[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:]
+ -[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:]
+ -[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:]
+ -[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:]
+ -[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:]
+ -[MTL4DebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4DebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4DebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4DebugRenderCommandEncoder drawPrimitives:indirectBuffer:]
+ -[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:]
+ -[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:]
+ -[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]
+ -[MTL4DebugRenderCommandEncoder endEncoding]
+ -[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4DebugRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:]
+ -[MTL4DebugRenderCommandEncoder setArgumentTable:atStages:]
+ -[MTL4DebugRenderCommandEncoder setBlendColorRed:green:blue:alpha:]
+ -[MTL4DebugRenderCommandEncoder setColorAttachmentMap:]
+ -[MTL4DebugRenderCommandEncoder setColorStoreAction:atIndex:]
+ -[MTL4DebugRenderCommandEncoder setCommandDataCorruptModeSPI:]
+ -[MTL4DebugRenderCommandEncoder setCullMode:]
+ -[MTL4DebugRenderCommandEncoder setCullMode:].cold.1
+ -[MTL4DebugRenderCommandEncoder setDepthBias:slopeScale:clamp:]
+ -[MTL4DebugRenderCommandEncoder setDepthClipMode:]
+ -[MTL4DebugRenderCommandEncoder setDepthClipMode:].cold.1
+ -[MTL4DebugRenderCommandEncoder setDepthClipModeSPI:]
+ -[MTL4DebugRenderCommandEncoder setDepthStencilState:]
+ -[MTL4DebugRenderCommandEncoder setDepthStoreAction:]
+ -[MTL4DebugRenderCommandEncoder setFrontFacingWinding:]
+ -[MTL4DebugRenderCommandEncoder setFrontFacingWinding:].cold.1
+ -[MTL4DebugRenderCommandEncoder setLineWidth:]
+ -[MTL4DebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]
+ -[MTL4DebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTL4DebugRenderCommandEncoder setRenderPipelineState:]
+ -[MTL4DebugRenderCommandEncoder setScissorRect:]
+ -[MTL4DebugRenderCommandEncoder setScissorRects:count:]
+ -[MTL4DebugRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:]
+ -[MTL4DebugRenderCommandEncoder setStencilReferenceValue:]
+ -[MTL4DebugRenderCommandEncoder setStencilStoreAction:]
+ -[MTL4DebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:]
+ -[MTL4DebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:].cold.1
+ -[MTL4DebugRenderCommandEncoder setTriangleFillMode:]
+ -[MTL4DebugRenderCommandEncoder setTriangleFillMode:].cold.1
+ -[MTL4DebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:]
+ -[MTL4DebugRenderCommandEncoder setVertexAmplificationMode:value:]
+ -[MTL4DebugRenderCommandEncoder setViewport:]
+ -[MTL4DebugRenderCommandEncoder setViewports:count:]
+ -[MTL4DebugRenderCommandEncoder setVisibilityResultMode:offset:]
+ -[MTL4DebugRenderCommandEncoder setVisibilityResultMode:offset:].cold.1
+ -[MTL4DebugRenderCommandEncoder setVisibilityResultMode:offset:].cold.2
+ -[MTL4DebugRenderCommandEncoder updateFence:afterEncoderStages:]
+ -[MTL4DebugRenderCommandEncoder waitForFence:beforeEncoderStages:]
+ -[MTL4DebugRenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:]
+ -[MTL4GPUDebugArchive newBinaryFunctionWithDescriptor:error:]
+ -[MTL4GPUDebugArchive newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4GPUDebugArchive newComputePipelineStateWithDescriptor:error:]
+ -[MTL4GPUDebugArchive newComputePipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4GPUDebugArchive newComputePipelineStateWithName:error:]
+ -[MTL4GPUDebugArchive newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4GPUDebugArchive newRenderPipelineStateWithDescriptor:error:]
+ -[MTL4GPUDebugArchive newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4GPUDebugArchive newRenderPipelineStateWithName:error:]
+ -[MTL4GPUDebugBinaryFunction initImageData:]
+ -[MTL4GPUDebugCommandBuffer .cxx_construct]
+ -[MTL4GPUDebugCommandBuffer .cxx_destruct]
+ -[MTL4GPUDebugCommandBuffer _Init]
+ -[MTL4GPUDebugCommandBuffer _lateInit]
+ -[MTL4GPUDebugCommandBuffer _temporaryBufferWithLength:]
+ -[MTL4GPUDebugCommandBuffer addResidencySetGPUDebug:fromEncoder:]
+ -[MTL4GPUDebugCommandBuffer addUsedPipelineState:]
+ -[MTL4GPUDebugCommandBuffer applyResidencySets:]
+ -[MTL4GPUDebugCommandBuffer beginCommandBufferWithAllocator:]
+ -[MTL4GPUDebugCommandBuffer beginCommandBufferWithAllocator:options:]
+ -[MTL4GPUDebugCommandBuffer beginningEncoder:type:]
+ -[MTL4GPUDebugCommandBuffer computeCommandEncoderWithSubstreamCount:]
+ -[MTL4GPUDebugCommandBuffer computeCommandEncoder]
+ -[MTL4GPUDebugCommandBuffer dealloc]
+ -[MTL4GPUDebugCommandBuffer encodeResourceTableBuffers:type:]
+ -[MTL4GPUDebugCommandBuffer endCommandBuffer]
+ -[MTL4GPUDebugCommandBuffer endingEncoder:type:]
+ -[MTL4GPUDebugCommandBuffer getRetainedData]
+ -[MTL4GPUDebugCommandBuffer initReportBufferInPrivateData:]
+ -[MTL4GPUDebugCommandBuffer initWithCommandBuffer:device:]
+ -[MTL4GPUDebugCommandBuffer markBuffer:usage:stages:]
+ -[MTL4GPUDebugCommandBuffer markHeap:stages:]
+ -[MTL4GPUDebugCommandBuffer markHeap:usage:stages:]
+ -[MTL4GPUDebugCommandBuffer markTexture:usage:stages:]
+ -[MTL4GPUDebugCommandBuffer numDispatches]
+ -[MTL4GPUDebugCommandBuffer preCommit:]
+ -[MTL4GPUDebugCommandBuffer renderCommandEncoderWithDescriptor:]
+ -[MTL4GPUDebugCommandBuffer renderCommandEncoderWithDescriptor:options:]
+ -[MTL4GPUDebugCommandBuffer resourceUsageForBuffer:stage:]
+ -[MTL4GPUDebugCommandBuffer setNumDispatches:]
+ -[MTL4GPUDebugCommandBuffer setResidencyForResource:]
+ -[MTL4GPUDebugCommandBuffer setUpShaderLoggingPrivateData]
+ -[MTL4GPUDebugCommandBuffer temporaryBufferWithBytes:length:]
+ -[MTL4GPUDebugCommandBuffer temporaryBufferWithLength:]
+ -[MTL4GPUDebugCommandBuffer useResidencySet:]
+ -[MTL4GPUDebugCommandBuffer useResidencySets:count:]
+ -[MTL4GPUDebugCommandQueue _checkReportBuffers:outputArray:encoderLabels:]
+ -[MTL4GPUDebugCommandQueue _commit:count:options:]
+ -[MTL4GPUDebugCommandQueue _decodeReportLogState:outputArray:encoderLabels:]
+ -[MTL4GPUDebugCommandQueue commit:count:]
+ -[MTL4GPUDebugCommandQueue commit:count:options:]
+ -[MTL4GPUDebugCommandQueue dealloc]
+ -[MTL4GPUDebugCommandQueue initWithCommandQueue:device:]
+ -[MTL4GPUDebugCommandQueue setUpLogState:]
+ -[MTL4GPUDebugCommandQueue tracePath]
+ -[MTL4GPUDebugCompiler _modifyComputeDynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyComputePipelineDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyComputePipelineDescriptor:dynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyDynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyRenderDynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyRenderPipelineDescriptor:]
+ -[MTL4GPUDebugCompiler _modifyRenderPipelineDescriptor:dynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4GPUDebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4GPUDebugCompiler newDynamicLibrary:completionHandler:]
+ -[MTL4GPUDebugCompiler newDynamicLibrary:error:]
+ -[MTL4GPUDebugCompiler newDynamicLibraryWithURL:completionHandler:]
+ -[MTL4GPUDebugCompiler newDynamicLibraryWithURL:error:]
+ -[MTL4GPUDebugCompiler newLibraryWithDescriptor:completionHandler:]
+ -[MTL4GPUDebugCompiler newLibraryWithDescriptor:error:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4BinaryFunctionDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4ComputeDynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4ComputePipelineDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4ComputePipelineDescriptor:dynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4RenderDynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4RenderPipelineDescriptor:]
+ -[MTL4GPUDebugCompiler newUnwrappedMTL4RenderPipelineDescriptor:dynamicLinkingDescriptor:]
+ -[MTL4GPUDebugCompiler wrapDynamicLibraries:]
+ -[MTL4GPUDebugComputeCommandEncoder .cxx_construct]
+ -[MTL4GPUDebugComputeCommandEncoder beginVirtualSubstream]
+ -[MTL4GPUDebugComputeCommandEncoder bindInternalBuffer:index:]
+ -[MTL4GPUDebugComputeCommandEncoder bindInternalBufferWithOffset:offset:index:]
+ -[MTL4GPUDebugComputeCommandEncoder bindInternalValue:index:]
+ -[MTL4GPUDebugComputeCommandEncoder blitAccelerationStructureType:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder blitChildrenWrappersBufferAddress:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder blitInstanceTypetoAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder blitPrimitiveTypetoAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder blitTypeFromAccelerationStructure:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder blitTypeFromAccelerationStructureDescriptor:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder copyFromInternalBuffer:sourceOffset:toInternalBuffer:destinationOffset:size:]
+ -[MTL4GPUDebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:]
+ -[MTL4GPUDebugComputeCommandEncoder createChildrenWrappersBufferWithASDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder createChildrenWrappersBufferWithIASDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder createChildrenWrappersBufferWithIndirectIASDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder createChildrenWrappersBufferWithInstanceDescriptorBufferRange:maxInstanceCount:instanceCountBufferRange:instanceDescriptorStride:instanceDescriptorType:]
+ -[MTL4GPUDebugComputeCommandEncoder dealloc]
+ -[MTL4GPUDebugComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:]
+ -[MTL4GPUDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:]
+ -[MTL4GPUDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:]
+ -[MTL4GPUDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeCopyAndUnwrapChildrenWithInstanceDescriptorBufferRange:dstInstanceDescriptorBufferRange:instanceDescriptorStride:instanceIDOffset:maxInstanceCount:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeEndIf]
+ -[MTL4GPUDebugComputeCommandEncoder encodeEndWhile]
+ -[MTL4GPUDebugComputeCommandEncoder encodeStartDoWhile]
+ -[MTL4GPUDebugComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeUnwrapAccelerationStructureDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeUnwrapWithIASDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder encodeUnwrapWithIndirectIASDescriptor:]
+ -[MTL4GPUDebugComputeCommandEncoder encoderID]
+ -[MTL4GPUDebugComputeCommandEncoder endEncoding]
+ -[MTL4GPUDebugComputeCommandEncoder endVirtualSubstream]
+ -[MTL4GPUDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4GPUDebugComputeCommandEncoder flushBindings]
+ -[MTL4GPUDebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:encoderID:]
+ -[MTL4GPUDebugComputeCommandEncoder internalValueAtIndex:]
+ -[MTL4GPUDebugComputeCommandEncoder newComputePipelineStateWithFunctionName:]
+ -[MTL4GPUDebugComputeCommandEncoder nextVirtualSubstream]
+ -[MTL4GPUDebugComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:]
+ -[MTL4GPUDebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:]
+ -[MTL4GPUDebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:]
+ -[MTL4GPUDebugComputeCommandEncoder setArgumentTable:]
+ -[MTL4GPUDebugComputeCommandEncoder setBufferUsageTable:textureUsageTable:]
+ -[MTL4GPUDebugComputeCommandEncoder setComputePipelineState:]
+ -[MTL4GPUDebugComputeCommandEncoder setComputePipelineStateBuffers:]
+ -[MTL4GPUDebugComputeCommandEncoder setInternalBytes:length:atIndex:]
+ -[MTL4GPUDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:]
+ -[MTL4GPUDebugComputeCommandEncoder temporaryBufferWithBytes:length:]
+ -[MTL4GPUDebugComputeCommandEncoder temporaryBufferWithLength:]
+ -[MTL4GPUDebugComputeCommandEncoder useResidencySet:]
+ -[MTL4GPUDebugComputeCommandEncoder useResidencySets:count:]
+ -[MTL4GPUDebugComputeCommandEncoder waitForVirtualSubstream:]
+ -[MTL4GPUDebugRenderCommandEncoder .cxx_construct]
+ -[MTL4GPUDebugRenderCommandEncoder _internalBindingTableForStage:]
+ -[MTL4GPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:]
+ -[MTL4GPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:offset:]
+ -[MTL4GPUDebugRenderCommandEncoder bindInternalValueForStage:index:stage:]
+ -[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:]
+ -[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:]
+ -[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:]
+ -[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:]
+ -[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:]
+ -[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:]
+ -[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:]
+ -[MTL4GPUDebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4GPUDebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4GPUDebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4GPUDebugRenderCommandEncoder drawPrimitives:indirectBuffer:]
+ -[MTL4GPUDebugRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:]
+ -[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:]
+ -[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:]
+ -[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]
+ -[MTL4GPUDebugRenderCommandEncoder encoderID]
+ -[MTL4GPUDebugRenderCommandEncoder endEncoding]
+ -[MTL4GPUDebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:]
+ -[MTL4GPUDebugRenderCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4GPUDebugRenderCommandEncoder flushBindings]
+ -[MTL4GPUDebugRenderCommandEncoder getInternalValueForStage:stage:]
+ -[MTL4GPUDebugRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:encoderID:]
+ -[MTL4GPUDebugRenderCommandEncoder prepareExecuteIndirect:variant:]
+ -[MTL4GPUDebugRenderCommandEncoder restoreInternalState:]
+ -[MTL4GPUDebugRenderCommandEncoder setArgumentTable:atStages:]
+ -[MTL4GPUDebugRenderCommandEncoder setBufferUsageTable:textureUsageTable:forStage:]
+ -[MTL4GPUDebugRenderCommandEncoder setDepthStencilState:]
+ -[MTL4GPUDebugRenderCommandEncoder setInternalBytesForStage:length:atIndex:stage:]
+ -[MTL4GPUDebugRenderCommandEncoder setRenderPipelineState:]
+ -[MTL4GPUDebugRenderCommandEncoder setRenderPipelineStateBuffers:]
+ -[MTL4GPUDebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:]
+ -[MTL4GPUDebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:]
+ -[MTL4GPUDebugRenderCommandEncoder temporaryBufferWithBytes:length:]
+ -[MTL4GPUDebugRenderCommandEncoder temporaryBufferWithLength:]
+ -[MTL4ToolsArchive initWithBaseObject:parent:]
+ -[MTL4ToolsArchive label]
+ -[MTL4ToolsArchive newArchiveReplyForPipelineFunctionWithDescriptor:functionType:functionId:]
+ -[MTL4ToolsArchive newBinaryFunctionWithDescriptor:error:]
+ -[MTL4ToolsArchive newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4ToolsArchive newComputePipelineStateWithDescriptor:error:]
+ -[MTL4ToolsArchive newComputePipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4ToolsArchive newComputePipelineStateWithName:error:]
+ -[MTL4ToolsArchive newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[MTL4ToolsArchive newRenderPipelineStateWithDescriptor:error:]
+ -[MTL4ToolsArchive newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:]
+ -[MTL4ToolsArchive newRenderPipelineStateWithName:error:]
+ -[MTL4ToolsArchive setLabel:]
+ -[MTL4ToolsArgumentTable bufferBindingCount]
+ -[MTL4ToolsArgumentTable dealloc]
+ -[MTL4ToolsArgumentTable getBufferBindings:bindingCount:]
+ -[MTL4ToolsArgumentTable getTextureBindings:bindingCount:]
+ -[MTL4ToolsArgumentTable initWithBaseObject:parent:]
+ -[MTL4ToolsArgumentTable label]
+ -[MTL4ToolsArgumentTable samplerBindingCount]
+ -[MTL4ToolsArgumentTable setAddress:atIndex:]
+ -[MTL4ToolsArgumentTable setAddress:attributeStride:atIndex:]
+ -[MTL4ToolsArgumentTable setResource:atBufferIndex:]
+ -[MTL4ToolsArgumentTable setSamplerState:atIndex:]
+ -[MTL4ToolsArgumentTable setTexture:atIndex:]
+ -[MTL4ToolsArgumentTable textureBindingCount]
+ -[MTL4ToolsBinaryFunction dealloc]
+ -[MTL4ToolsBinaryFunction debugInstrumentationData]
+ -[MTL4ToolsBinaryFunction functionType]
+ -[MTL4ToolsBinaryFunction initWithBaseObject:parent:]
+ -[MTL4ToolsBinaryFunction name]
+ -[MTL4ToolsBinaryFunction reflection]
+ -[MTL4ToolsBinaryFunction relocations]
+ -[MTL4ToolsBinaryFunction setRelocations:]
+ -[MTL4ToolsCommandAllocator addResetHandler:]
+ -[MTL4ToolsCommandAllocator allocatedSize]
+ -[MTL4ToolsCommandAllocator attachCommandBuffer:]
+ -[MTL4ToolsCommandAllocator currentCommandBuffer]
+ -[MTL4ToolsCommandAllocator detachCommandBuffer]
+ -[MTL4ToolsCommandAllocator initWithBaseObject:parent:]
+ -[MTL4ToolsCommandAllocator label]
+ -[MTL4ToolsCommandAllocator reset]
+ -[MTL4ToolsCommandBuffer beginCommandBufferWithAllocator:]
+ -[MTL4ToolsCommandBuffer beginCommandBufferWithAllocator:options:]
+ -[MTL4ToolsCommandBuffer commandAllocator]
+ -[MTL4ToolsCommandBuffer computeCommandEncoderWithSubstreamCount:]
+ -[MTL4ToolsCommandBuffer computeCommandEncoder]
+ -[MTL4ToolsCommandBuffer currentGeneration]
+ -[MTL4ToolsCommandBuffer dealloc]
+ -[MTL4ToolsCommandBuffer endCommandBuffer]
+ -[MTL4ToolsCommandBuffer initWithBaseObject:parent:]
+ -[MTL4ToolsCommandBuffer label]
+ -[MTL4ToolsCommandBuffer machineLearningCommandEncoder]
+ -[MTL4ToolsCommandBuffer popDebugGroup]
+ -[MTL4ToolsCommandBuffer privateDataOffset]
+ -[MTL4ToolsCommandBuffer privateData]
+ -[MTL4ToolsCommandBuffer pushDebugGroup:]
+ -[MTL4ToolsCommandBuffer renderCommandEncoderWithDescriptor:]
+ -[MTL4ToolsCommandBuffer renderCommandEncoderWithDescriptor:options:]
+ -[MTL4ToolsCommandBuffer resetCommandBuffer]
+ -[MTL4ToolsCommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:]
+ -[MTL4ToolsCommandBuffer sampledComputeCommandEncoder:capacity:]
+ -[MTL4ToolsCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:]
+ -[MTL4ToolsCommandBuffer setLabel:]
+ -[MTL4ToolsCommandBuffer setPrivateData:]
+ -[MTL4ToolsCommandBuffer setPrivateDataOffset:]
+ -[MTL4ToolsCommandBuffer unwrappedMTL4RenderPassDescriptor:]
+ -[MTL4ToolsCommandBuffer useResidencySet:]
+ -[MTL4ToolsCommandBuffer useResidencySets:count:]
+ -[MTL4ToolsCommandBuffer usedResidencySets]
+ -[MTL4ToolsCommandBuffer writeTimestampIntoHeap:atIndex:]
+ -[MTL4ToolsCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:options:]
+ -[MTL4ToolsCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[MTL4ToolsCommandEncoder barrierAfterQueueStages:beforeStages:options:]
+ -[MTL4ToolsCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[MTL4ToolsCommandEncoder barrierAfterStages:beforeQueueStages:options:]
+ -[MTL4ToolsCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[MTL4ToolsCommandEncoder commandAllocator]
+ -[MTL4ToolsCommandEncoder commandBatchIdOffset]
+ -[MTL4ToolsCommandEncoder commandBatchIdRangeMin:max:]
+ -[MTL4ToolsCommandEncoder commandBuffer]
+ -[MTL4ToolsCommandEncoder dealloc]
+ -[MTL4ToolsCommandEncoder endEncodingAndRetrieveProgramAddressTable]
+ -[MTL4ToolsCommandEncoder endEncoding]
+ -[MTL4ToolsCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:]
+ -[MTL4ToolsCommandEncoder initWithBaseObject:parent:]
+ -[MTL4ToolsCommandEncoder initWithCommandEncoder:commandBuffer:]
+ -[MTL4ToolsCommandEncoder insertDebugSignpost:]
+ -[MTL4ToolsCommandEncoder label]
+ -[MTL4ToolsCommandEncoder popDebugGroup]
+ -[MTL4ToolsCommandEncoder pushDebugGroup:]
+ -[MTL4ToolsCommandEncoder setLabel:]
+ -[MTL4ToolsCommandEncoder updateFence:afterEncoderStages:]
+ -[MTL4ToolsCommandEncoder waitForFence:beforeEncoderStages:]
+ -[MTL4ToolsCommandQueue addResidencySet:]
+ -[MTL4ToolsCommandQueue addResidencySets:count:]
+ -[MTL4ToolsCommandQueue addedResidencySets]
+ -[MTL4ToolsCommandQueue commit:count:]
+ -[MTL4ToolsCommandQueue commit:count:options:]
+ -[MTL4ToolsCommandQueue commit:count:options:preprocessHandler:]
+ -[MTL4ToolsCommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:]
+ -[MTL4ToolsCommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:]
+ -[MTL4ToolsCommandQueue dealloc]
+ -[MTL4ToolsCommandQueue initWithBaseObject:parent:]
+ -[MTL4ToolsCommandQueue label]
+ -[MTL4ToolsCommandQueue lastCommittedCommandBufferGeneration]
+ -[MTL4ToolsCommandQueue lastCommittedCommandBuffer]
+ -[MTL4ToolsCommandQueue removeResidencySet:]
+ -[MTL4ToolsCommandQueue removeResidencySets:count:]
+ -[MTL4ToolsCommandQueue signalDrawable:]
+ -[MTL4ToolsCommandQueue signalEvent:value:]
+ -[MTL4ToolsCommandQueue updateBufferMappings:heap:operations:count:]
+ -[MTL4ToolsCommandQueue updateTextureMappings:heap:operations:count:]
+ -[MTL4ToolsCommandQueue waitForDrawable:]
+ -[MTL4ToolsCommandQueue waitForEvent:value:]
+ -[MTL4ToolsCommandQueue waitForEvent:value:timeout:]
+ -[MTL4ToolsCompiler cancel]
+ -[MTL4ToolsCompiler destinationBinaryArchive]
+ -[MTL4ToolsCompiler initWithBaseObject:parent:]
+ -[MTL4ToolsCompiler label]
+ -[MTL4ToolsCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4ToolsCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4ToolsCompiler newDynamicLibrary:completionHandler:]
+ -[MTL4ToolsCompiler newDynamicLibrary:error:]
+ -[MTL4ToolsCompiler newDynamicLibraryWithURL:completionHandler:]
+ -[MTL4ToolsCompiler newDynamicLibraryWithURL:error:]
+ -[MTL4ToolsCompiler newDynamicLibraryWithURL:options:completionHandler:]
+ -[MTL4ToolsCompiler newDynamicLibraryWithURL:options:error:]
+ -[MTL4ToolsCompiler newLibraryWithDescriptor:completionHandler:]
+ -[MTL4ToolsCompiler newLibraryWithDescriptor:error:]
+ -[MTL4ToolsCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:]
+ -[MTL4ToolsCompiler newMachineLearningPipelineStateWithDescriptor:error:]
+ -[MTL4ToolsCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]
+ -[MTL4ToolsCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:]
+ -[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]
+ -[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[MTL4ToolsCompiler pipelineDataSetSerializer]
+ -[MTL4ToolsCompiler setLabel:]
+ -[MTL4ToolsCompiler setPipelineDataSetSerializer:]
+ -[MTL4ToolsCompiler shouldMaximizeConcurrentCompilation]
+ -[MTL4ToolsCompilerTask compiler]
+ -[MTL4ToolsCompilerTask initWithBaseObject:parent:]
+ -[MTL4ToolsCompilerTask initWithCompiler:]
+ -[MTL4ToolsCompilerTask status]
+ -[MTL4ToolsCompilerTask tryCancel]
+ -[MTL4ToolsCompilerTask waitUntilCompleted]
+ -[MTL4ToolsComputeCommandEncoder beginVirtualSubstream]
+ -[MTL4ToolsComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:]
+ -[MTL4ToolsComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:]
+ -[MTL4ToolsComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:]
+ -[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]
+ -[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:]
+ -[MTL4ToolsComputeCommandEncoder copyFromTexture:toTexture:]
+ -[MTL4ToolsComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:]
+ -[MTL4ToolsComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:]
+ -[MTL4ToolsComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:]
+ -[MTL4ToolsComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:]
+ -[MTL4ToolsComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:]
+ -[MTL4ToolsComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:]
+ -[MTL4ToolsComputeCommandEncoder dispatchThreadsWithIndirectBuffer:]
+ -[MTL4ToolsComputeCommandEncoder enableNullBufferBinds:]
+ -[MTL4ToolsComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:]
+ -[MTL4ToolsComputeCommandEncoder encodeEndIf]
+ -[MTL4ToolsComputeCommandEncoder encodeEndWhile]
+ -[MTL4ToolsComputeCommandEncoder encodeStartDoWhile]
+ -[MTL4ToolsComputeCommandEncoder encodeStartElse]
+ -[MTL4ToolsComputeCommandEncoder encodeStartIf:comparison:referenceValue:]
+ -[MTL4ToolsComputeCommandEncoder encodeStartWhile:comparison:referenceValue:]
+ -[MTL4ToolsComputeCommandEncoder endVirtualSubstream]
+ -[MTL4ToolsComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[MTL4ToolsComputeCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4ToolsComputeCommandEncoder fillBuffer:range:pattern4:]
+ -[MTL4ToolsComputeCommandEncoder fillBuffer:range:value:]
+ -[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:bytes:length:]
+ -[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:color:]
+ -[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:]
+ -[MTL4ToolsComputeCommandEncoder generateMipmapsForTexture:]
+ -[MTL4ToolsComputeCommandEncoder initWithBaseObject:parent:]
+ -[MTL4ToolsComputeCommandEncoder insertCompressedTextureReinterpretationFlush]
+ -[MTL4ToolsComputeCommandEncoder invalidateCompressedTexture:]
+ -[MTL4ToolsComputeCommandEncoder invalidateCompressedTexture:slice:level:]
+ -[MTL4ToolsComputeCommandEncoder nextVirtualSubstream]
+ -[MTL4ToolsComputeCommandEncoder optimizeContentsForCPUAccess:]
+ -[MTL4ToolsComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:]
+ -[MTL4ToolsComputeCommandEncoder optimizeContentsForGPUAccess:]
+ -[MTL4ToolsComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:]
+ -[MTL4ToolsComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:]
+ -[MTL4ToolsComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:]
+ -[MTL4ToolsComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:]
+ -[MTL4ToolsComputeCommandEncoder resetCommandsInBuffer:withRange:]
+ -[MTL4ToolsComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder setArgumentTable:]
+ -[MTL4ToolsComputeCommandEncoder setComputePipelineState:]
+ -[MTL4ToolsComputeCommandEncoder setImageblockWidth:height:]
+ -[MTL4ToolsComputeCommandEncoder setSubstream:]
+ -[MTL4ToolsComputeCommandEncoder setThreadgroupDistributionMode:]
+ -[MTL4ToolsComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:]
+ -[MTL4ToolsComputeCommandEncoder setThreadgroupMemoryLength:atIndex:]
+ -[MTL4ToolsComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:]
+ -[MTL4ToolsComputeCommandEncoder signalProgress:]
+ -[MTL4ToolsComputeCommandEncoder stages]
+ -[MTL4ToolsComputeCommandEncoder waitForProgress:]
+ -[MTL4ToolsComputeCommandEncoder waitForVirtualSubstream:]
+ -[MTL4ToolsComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:]
+ -[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:]
+ -[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:]
+ -[MTL4ToolsComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:]
+ -[MTL4ToolsCounterHeap count]
+ -[MTL4ToolsCounterHeap fillWithByte:]
+ -[MTL4ToolsCounterHeap initWithBaseObject:parent:]
+ -[MTL4ToolsCounterHeap invalidateCounterRange:]
+ -[MTL4ToolsCounterHeap label]
+ -[MTL4ToolsCounterHeap resolveCounterRange:]
+ -[MTL4ToolsCounterHeap setLabel:]
+ -[MTL4ToolsCounterHeap type]
+ -[MTL4ToolsMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:]
+ -[MTL4ToolsMachineLearningCommandEncoder endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:]
+ -[MTL4ToolsMachineLearningCommandEncoder endEventValue]
+ -[MTL4ToolsMachineLearningCommandEncoder initWithBaseObject:parent:]
+ -[MTL4ToolsMachineLearningCommandEncoder setArgumentTable:]
+ -[MTL4ToolsMachineLearningCommandEncoder setPipelineState:]
+ -[MTL4ToolsMachineLearningCommandEncoder startEventValue]
+ -[MTL4ToolsMachineLearningPipelineState allocatedSize]
+ -[MTL4ToolsMachineLearningPipelineState device]
+ -[MTL4ToolsMachineLearningPipelineState initWithBaseObject:parent:]
+ -[MTL4ToolsMachineLearningPipelineState intermediatesHeapSize]
+ -[MTL4ToolsMachineLearningPipelineState label]
+ -[MTL4ToolsMachineLearningPipelineState optimizedBytecode]
+ -[MTL4ToolsMachineLearningPipelineState reflection]
+ -[MTL4ToolsMachineLearningPipelineState resourceBlobForByteCodeSignature:resourceName:error:]
+ -[MTL4ToolsMachineLearningPipelineState runWithInputsArray:resultsArray:intermediateOperations:]
+ -[MTL4ToolsPipelineDataSetSerializer addBinaryFunctionWithDescriptor:]
+ -[MTL4ToolsPipelineDataSetSerializer addPipelineWithDescriptor:]
+ -[MTL4ToolsPipelineDataSetSerializer destinationBinaryArchive]
+ -[MTL4ToolsPipelineDataSetSerializer initWithBaseObject:parent:]
+ -[MTL4ToolsPipelineDataSetSerializer serializeAsArchiveAndFlushToURL:error:]
+ -[MTL4ToolsPipelineDataSetSerializer serializeAsPipelinesScriptWithError:]
+ -[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:]
+ -[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:inRegion:]
+ -[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:]
+ -[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:]
+ -[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:]
+ -[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:]
+ -[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:]
+ -[MTL4ToolsRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4ToolsRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4ToolsRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[MTL4ToolsRenderCommandEncoder drawPrimitives:indirectBuffer:]
+ -[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:]
+ -[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:]
+ -[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]
+ -[MTL4ToolsRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[MTL4ToolsRenderCommandEncoder executeCommandsInBuffer:withRange:]
+ -[MTL4ToolsRenderCommandEncoder isMemorylessRender]
+ -[MTL4ToolsRenderCommandEncoder setArgumentTable:atStages:]
+ -[MTL4ToolsRenderCommandEncoder setBlendColorRed:green:blue:alpha:]
+ -[MTL4ToolsRenderCommandEncoder setColorAttachmentMap:]
+ -[MTL4ToolsRenderCommandEncoder setColorStoreAction:atIndex:]
+ -[MTL4ToolsRenderCommandEncoder setCommandDataCorruptModeSPI:]
+ -[MTL4ToolsRenderCommandEncoder setCullMode:]
+ -[MTL4ToolsRenderCommandEncoder setDepthBias:slopeScale:clamp:]
+ -[MTL4ToolsRenderCommandEncoder setDepthClipMode:]
+ -[MTL4ToolsRenderCommandEncoder setDepthClipModeSPI:]
+ -[MTL4ToolsRenderCommandEncoder setDepthStencilState:]
+ -[MTL4ToolsRenderCommandEncoder setDepthStoreAction:]
+ -[MTL4ToolsRenderCommandEncoder setFrontFacingWinding:]
+ -[MTL4ToolsRenderCommandEncoder setLineWidth:]
+ -[MTL4ToolsRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]
+ -[MTL4ToolsRenderCommandEncoder setRenderPipelineState:]
+ -[MTL4ToolsRenderCommandEncoder setScissorRect:]
+ -[MTL4ToolsRenderCommandEncoder setScissorRects:count:]
+ -[MTL4ToolsRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:]
+ -[MTL4ToolsRenderCommandEncoder setStencilReferenceValue:]
+ -[MTL4ToolsRenderCommandEncoder setStencilStoreAction:]
+ -[MTL4ToolsRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:]
+ -[MTL4ToolsRenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:]
+ -[MTL4ToolsRenderCommandEncoder setTriangleFillMode:]
+ -[MTL4ToolsRenderCommandEncoder setVertexAmplificationCount:viewMappings:]
+ -[MTL4ToolsRenderCommandEncoder setVertexAmplificationMode:value:]
+ -[MTL4ToolsRenderCommandEncoder setViewport:]
+ -[MTL4ToolsRenderCommandEncoder setViewports:count:]
+ -[MTL4ToolsRenderCommandEncoder setVisibilityResultMode:offset:]
+ -[MTL4ToolsRenderCommandEncoder tileHeight]
+ -[MTL4ToolsRenderCommandEncoder tileWidth]
+ -[MTL4ToolsRenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:]
+ -[MTLDebugAccelerationStructureCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLDebugAccelerationStructureCommandEncoder barrierAfterQueueStages:beforeStages:].cold.1
+ -[MTLDebugBlitCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLDebugBlitCommandEncoder barrierAfterQueueStages:beforeStages:].cold.1
+ -[MTLDebugBlitCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]
+ -[MTLDebugBuffer initWithBuffer:device:options:placementSparsePageSize:]
+ -[MTLDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:].cold.4
+ -[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.5
+ -[MTLDebugBuffer placementSparsePageSize]
+ -[MTLDebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLDebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:].cold.1
+ -[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:]
+ -[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:binaryFunction:]
+ -[MTLDebugComputePipelineState functionHandleWithBinaryFunction:]
+ -[MTLDebugComputePipelineState functionHandleWithName:]
+ -[MTLDebugComputePipelineState initCommon]
+ -[MTLDebugComputePipelineState initWithComputePipelineState:parent:mtl4Descriptor:]
+ -[MTLDebugComputePipelineState initWithComputePipelineState:reflection:parent:mtl4Descriptor:]
+ -[MTLDebugComputePipelineState mtl4Descriptor]
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:].cold.5
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:]
+ -[MTLDebugComputePipelineState newComputePipelineStateWithBinaryFunctions:error:]
+ -[MTLDebugComputePipelineState validationReflection]
+ -[MTLDebugDevice functionHandleWithFunction:]
+ -[MTLDebugDevice functionHandleWithFunction:].cold.1
+ -[MTLDebugDevice functionHandleWithFunction:].cold.2
+ -[MTLDebugDevice functionHandleWithFunction:resourceIndex:]
+ -[MTLDebugDevice functionHandleWithFunction:resourceIndex:].cold.1
+ -[MTLDebugDevice functionHandleWithFunction:resourceIndex:].cold.2
+ -[MTLDebugDevice newArchiveWithURL:error:]
+ -[MTLDebugDevice newArgumentTableWithDescriptor:error:]
+ -[MTLDebugDevice newBufferWithLength:options:placementSparsePageSize:]
+ -[MTLDebugDevice newCommandAllocatorWithDescriptor:error:]
+ -[MTLDebugDevice newCommandAllocator]
+ -[MTLDebugDevice newCommandBuffer]
+ -[MTLDebugDevice newCompilerWithDescriptor:error:]
+ -[MTLDebugDevice newCounterHeapWithDescriptor:error:]
+ -[MTLDebugDevice newMTL4CommandQueueWithDescriptor:error:]
+ -[MTLDebugDevice newMTL4CommandQueue]
+ -[MTLDebugDevice newTextureViewPoolWithDescriptor:error:]
+ -[MTLDebugDevice sizeOfCounterHeapEntry:]
+ -[MTLDebugFunction getIntersectionFunctionSignature]
+ -[MTLDebugFunction initWithFunction:library:]
+ -[MTLDebugFunction intersectionFunctionSignature]
+ -[MTLDebugFunction setIntersectionFunctionSignature:]
+ -[MTLDebugFunction validateIsIFBFunction]
+ -[MTLDebugFunction validateIsIFBFunction].cold.1
+ -[MTLDebugFunction validateIsIFBFunction].cold.2
+ -[MTLDebugFunctionHandle gpuResourceID]
+ -[MTLDebugFunctionHandle initWithBaseObject:parent:binaryFunction:stage:]
+ -[MTLDebugFunctionHandle initWithBaseObject:parent:stage:]
+ -[MTLDebugFunctionHandle resourceIndex]
+ -[MTLDebugHeap initWithHeap:device:maxCompatiblePlacementSparsePageSize:]
+ -[MTLDebugHeap maxCompatiblePlacementSparsePageSize]
+ -[MTLDebugIntersectionFunctionTable setFunction:atIndex:].cold.3
+ -[MTLDebugIntersectionFunctionTable setFunction:atIndex:].cold.4
+ -[MTLDebugLibrary validateDescriptor:expectedClass:].cold.4
+ -[MTLDebugRenderCommandEncoder _validateLBRT:]
+ -[MTLDebugRenderCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLDebugRenderCommandEncoder barrierAfterQueueStages:beforeStages:].cold.1
+ -[MTLDebugRenderCommandEncoder setColorAttachmentMap:]
+ -[MTLDebugRenderPipelineState _updateCachedMTL4MeshPipelineState]
+ -[MTLDebugRenderPipelineState _updateCachedMTL4PipelineState]
+ -[MTLDebugRenderPipelineState _updateCachedMTL4TilePipelineState]
+ -[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:binaryFunction:stage:]
+ -[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:stage:]
+ -[MTLDebugRenderPipelineState functionHandleWithBinaryFunction:stage:]
+ -[MTLDebugRenderPipelineState functionHandleWithName:stage:]
+ -[MTLDebugRenderPipelineState hasMetal4Descriptor]
+ -[MTLDebugRenderPipelineState initWithRenderPipelineState:parent:mtl4Descriptor:]
+ -[MTLDebugRenderPipelineState initWithRenderPipelineState:reflection:parent:mtl4Descriptor:]
+ -[MTLDebugRenderPipelineState mtl4Descriptor]
+ -[MTLDebugRenderPipelineState mtl4MeshDescriptor]
+ -[MTLDebugRenderPipelineState mtl4TileDescriptor]
+ -[MTLDebugRenderPipelineState newRenderPipelineDescriptorForSpecialization]
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.10
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.11
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.12
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.7
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.8
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.9
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:].cold.4
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:].cold.5
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:]
+ -[MTLDebugRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.3
+ -[MTLDebugRenderPipelineState validationReflection]
+ -[MTLDebugResourceStateCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLDebugResourceStateCommandEncoder barrierAfterQueueStages:beforeStages:].cold.1
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:].cold.3
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:].cold.4
+ -[MTLDebugResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:].cold.4
+ -[MTLDebugResourceViewPool initWithResourceViewPool:device:]
+ -[MTLDebugTensor getBytes:strides:fromSlice:]
+ -[MTLDebugTensor getBytes:strides:fromSliceOrigin:sliceDimensions:]
+ -[MTLDebugTensor replaceSlice:withBytes:strides:]
+ -[MTLDebugTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:]
+ -[MTLDebugTensor verifyGetBytesReplaceSliceWithContext:strides:slice:]
+ -[MTLDebugTexture evaluateSloppyUsage:]
+ -[MTLDebugTexture evaluateUsage:]
+ -[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:descriptor:]
+ -[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:descriptor:]
+ -[MTLDebugTexture initWithBaseTexture:device:placementSparsePageSize:]
+ -[MTLDebugTexture newTextureViewWithDescriptor:]
+ -[MTLDebugTexture placementSparsePageSize]
+ -[MTLDebugTextureViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:]
+ -[MTLDebugTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]
+ -[MTLDebugTextureViewPool initWithTextureViewPool:device:]
+ -[MTLDebugTextureViewPool setTextureView:atIndex:]
+ -[MTLDebugTextureViewPool setTextureView:atIndex:].cold.1
+ -[MTLDebugTextureViewPool setTextureView:descriptor:atIndex:]
+ -[MTLDebugTextureViewPool setTextureView:descriptor:atIndex:].cold.1
+ -[MTLDebugTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:]
+ -[MTLDebugTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:].cold.1
+ -[MTLDebugVisibleFunctionTable setFunction:atIndex:].cold.4
+ -[MTLGPUDebugBuffer .cxx_construct]
+ -[MTLGPUDebugBuffer .cxx_destruct]
+ -[MTLGPUDebugBuffer addView:]
+ -[MTLGPUDebugBuffer getActiveViews]
+ -[MTLGPUDebugBuffer removeView:]
+ -[MTLGPUDebugCommandBuffer _addUsedBuffer:]
+ -[MTLGPUDebugCommandBuffer _decodeReportLogState:]
+ -[MTLGPUDebugCommandBuffer _internalBindingTableForStage:]
+ -[MTLGPUDebugCommandBuffer _setInternalBindingTables:type:]
+ -[MTLGPUDebugCommandBuffer numDispatches]
+ -[MTLGPUDebugCommandBuffer setNumDispatches:]
+ -[MTLGPUDebugComputeCommandEncoder bindInternalBuffer:index:]
+ -[MTLGPUDebugComputeCommandEncoder bindInternalBufferWithOffset:offset:index:]
+ -[MTLGPUDebugComputeCommandEncoder bindInternalValue:index:]
+ -[MTLGPUDebugComputeCommandEncoder setInternalBindingTable:]
+ -[MTLGPUDebugComputeCommandEncoder setInternalBytes:length:atIndex:]
+ -[MTLGPUDebugComputePipelineState _initConstantsBuffer:]
+ -[MTLGPUDebugComputePipelineState functionHandleWithBinaryFunction:]
+ -[MTLGPUDebugComputePipelineState functionHandleWithName:]
+ -[MTLGPUDebugComputePipelineState initWithComputePipelineState:binaryFunctions:withState:device:]
+ -[MTLGPUDebugComputePipelineState initWithComputePipelineState:descriptor:device:]
+ -[MTLGPUDebugComputePipelineState initWithComputePipelineState:descriptor:dynamicLinkingDescriptor:device:]
+ -[MTLGPUDebugComputePipelineState newComputePipelineStateWithBinaryFunctions:error:]
+ -[MTLGPUDebugDevice ICB_Inherit_Both_Mesh_VertexPipelineState]
+ -[MTLGPUDebugDevice ICB_Inherit_Both_VertexPipelineState]
+ -[MTLGPUDebugDevice incrementCurrentEncoderID]
+ -[MTLGPUDebugDevice instrumentationHeapInit]
+ -[MTLGPUDebugDevice newCommandBuffer]
+ -[MTLGPUDebugDevice newCompilerWithDescriptor:error:]
+ -[MTLGPUDebugDevice newDynamicLibraryWithDescriptor:error:]
+ -[MTLGPUDebugDevice newMTL4CommandQueueWithDescriptor:error:]
+ -[MTLGPUDebugDevice newMTL4CommandQueue]
+ -[MTLGPUDebugDevice newTextureViewPoolWithDescriptor:error:]
+ -[MTLGPUDebugDevice prepareInsertLibraries:]
+ -[MTLGPUDebugFunctionHandle initWithFunctionHandle:computePipelineState:]
+ -[MTLGPUDebugFunctionHandle initWithFunctionHandle:renderPipelineState:stage:]
+ -[MTLGPUDebugGPULog computePipeline]
+ -[MTLGPUDebugGPULog functionName]
+ -[MTLGPUDebugGPULog functionType]
+ -[MTLGPUDebugGPULog renderPipeline]
+ -[MTLGPUDebugGPULog setComputePipeline:]
+ -[MTLGPUDebugGPULog setFunctionName:]
+ -[MTLGPUDebugGPULog setFunctionType:]
+ -[MTLGPUDebugGPULog setRenderPipeline:]
+ -[MTLGPUDebugImageData binaryFunction]
+ -[MTLGPUDebugImageData initWithBinaryFunction:debugInstrumentationData:device:]
+ -[MTLGPUDebugImageData initWithFunctionName:functionType:debugInstrumentationData:device:]
+ -[MTLGPUDebugIndirectCommandBuffer SVBindingTableFragmentBuffer]
+ -[MTLGPUDebugIndirectCommandBuffer SVBindingTableMeshBuffer]
+ -[MTLGPUDebugIndirectCommandBuffer SVBindingTableObjectBuffer]
+ -[MTLGPUDebugIndirectCommandBuffer SVBindingTableVertexKernelBuffer]
+ -[MTLGPUDebugIndirectCommandBuffer hasOnlyRender]
+ -[MTLGPUDebugIndirectCommandBuffer initializedTables]
+ -[MTLGPUDebugIndirectCommandBuffer setInitializedTables:]
+ -[MTLGPUDebugIndirectCommandBuffer setSVBindingTableFragmentBuffer:]
+ -[MTLGPUDebugIndirectCommandBuffer setSVBindingTableMeshBuffer:]
+ -[MTLGPUDebugIndirectCommandBuffer setSVBindingTableObjectBuffer:]
+ -[MTLGPUDebugIndirectCommandBuffer setSVBindingTableVertexKernelBuffer:]
+ -[MTLGPUDebugIndirectComputeCommand setToolsDispatchBufferSPI:atIndex:]
+ -[MTLGPUDebugIndirectRenderCommand setToolsDispatchBufferSPI:atIndex:stages:]
+ -[MTLGPUDebugLibrary newFunctionWithDescriptor:destinationArchive:error:]
+ -[MTLGPUDebugRenderCommandEncoder _internalBindingTableForStage:]
+ -[MTLGPUDebugRenderCommandEncoder _setBufferForStage:atIndex:stage:]
+ -[MTLGPUDebugRenderCommandEncoder _setInternalBindingTableForStage:stage:]
+ -[MTLGPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:]
+ -[MTLGPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:offset:]
+ -[MTLGPUDebugRenderCommandEncoder bindInternalValueForStage:index:stage:]
+ -[MTLGPUDebugRenderCommandEncoder setInternalBytesForStage:length:atIndex:stage:]
+ -[MTLGPUDebugRenderPipelineState _initConstantsBuffer:]
+ -[MTLGPUDebugRenderPipelineState functionHandleWithBinaryFunction:stage:]
+ -[MTLGPUDebugRenderPipelineState functionHandleWithName:stage:]
+ -[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:device:]
+ -[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:dynamicLinkingDescriptor:device:]
+ -[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:originalObject:descriptor:device:]
+ -[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:]
+ -[MTLGPUDebugRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:]
+ -[MTLGPUDebugTexture .cxx_construct]
+ -[MTLGPUDebugTexture .cxx_destruct]
+ -[MTLGPUDebugTexture addView:]
+ -[MTLGPUDebugTexture dealloc]
+ -[MTLGPUDebugTexture getActiveViews]
+ -[MTLGPUDebugTexture newTextureViewWithDescriptor:]
+ -[MTLGPUDebugTexture removeView:]
+ -[MTLGPUDebugTextureViewPool .cxx_construct]
+ -[MTLGPUDebugTextureViewPool .cxx_destruct]
+ -[MTLGPUDebugTextureViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:]
+ -[MTLGPUDebugTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]
+ -[MTLGPUDebugTextureViewPool dealloc]
+ -[MTLGPUDebugTextureViewPool getViewableAt:]
+ -[MTLGPUDebugTextureViewPool initWithTextureViewPool:device:]
+ -[MTLGPUDebugTextureViewPool setTextureView:atIndex:]
+ -[MTLGPUDebugTextureViewPool setTextureView:descriptor:atIndex:]
+ -[MTLGPUDebugTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:]
+ -[MTLGPUDebugTextureViewPool setView:resourceID:type:index:]
+ -[MTLLegacySVTexture newTextureViewWithDescriptor:]
+ -[MTLToolsBlitCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]
+ -[MTLToolsBlitCommandEncoder endEncoding]
+ -[MTLToolsBlitCommandEncoder insertDebugSignpost:]
+ -[MTLToolsBlitCommandEncoder popDebugGroup]
+ -[MTLToolsBlitCommandEncoder pushDebugGroup:]
+ -[MTLToolsBuffer newTensorWithDescriptor:offset:error:]
+ -[MTLToolsBuffer sparseBufferTier]
+ -[MTLToolsCommandBuffer __waitUntilCompletedAsync:]
+ -[MTLToolsCommandBuffer __waitUntilScheduledAsync:]
+ -[MTLToolsCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[MTLToolsCommandQueue residencySetsLock]
+ -[MTLToolsComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:]
+ -[MTLToolsComputePipelineState functionHandleWithBinaryFunction:]
+ -[MTLToolsComputePipelineState functionHandleWithName:]
+ -[MTLToolsComputePipelineState functionReflectionWithFunctionDescriptor:]
+ -[MTLToolsComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:]
+ -[MTLToolsComputePipelineState newComputePipelineStateWithBinaryFunctions:error:]
+ -[MTLToolsComputePipelineState reflection]
+ -[MTLToolsComputePipelineState requiredThreadsPerThreadgroup]
+ -[MTLToolsComputePipelineState shaderValidationState]
+ -[MTLToolsComputePipelineState shaderValidation]
+ -[MTLToolsDevice defaultCompilerProcessesCount]
+ -[MTLToolsDevice functionHandleWithBinaryFunction:]
+ -[MTLToolsDevice functionHandleWithFunction:]
+ -[MTLToolsDevice functionHandleWithFunction:resourceIndex:]
+ -[MTLToolsDevice llvmVersion]
+ -[MTLToolsDevice maximumCompilerProcessesCount]
+ -[MTLToolsDevice mtlTensorFromGpuResourceID:]
+ -[MTLToolsDevice newArchiveWithURL:error:]
+ -[MTLToolsDevice newArgumentTableWithDescriptor:error:]
+ -[MTLToolsDevice newBufferWithLength:options:placementSparsePageSize:]
+ -[MTLToolsDevice newCommandAllocatorWithDescriptor:error:]
+ -[MTLToolsDevice newCommandAllocator]
+ -[MTLToolsDevice newCommandBuffer]
+ -[MTLToolsDevice newCommandQueue4]
+ -[MTLToolsDevice newCompilerWithDescriptor:error:]
+ -[MTLToolsDevice newCounterHeapWithDescriptor:error:]
+ -[MTLToolsDevice newLibraryWithMPSGraphPackageURL:name:error:]
+ -[MTLToolsDevice newMTL4CommandQueueWithDescriptor:error:]
+ -[MTLToolsDevice newMTL4CommandQueue]
+ -[MTLToolsDevice newPipelineDataSetSerializerWithDescriptor:]
+ -[MTLToolsDevice newTensorWithDescriptor:error:]
+ -[MTLToolsDevice newTextureViewPoolWithDescriptor:error:]
+ -[MTLToolsDevice newUnwrappedMTL4BinaryFunctionDescriptor:]
+ -[MTLToolsDevice newUnwrappedMTL4CompilerTaskOptions:]
+ -[MTLToolsDevice newUnwrappedMTL4FunctionDescriptor:]
+ -[MTLToolsDevice newUnwrappedMTL4LinkedFunctions:]
+ -[MTLToolsDevice newUnwrappedMTL4PipelineDescriptor:]
+ -[MTLToolsDevice newUnwrappedMTL4PipelineStageDynamicLinkingDescriptor:]
+ -[MTLToolsDevice newUnwrappedMTL4RenderPipelineBinaryFunctionsDescriptor:]
+ -[MTLToolsDevice newUnwrappedMTL4RenderPipelineDynamicLinkingDescriptor:]
+ -[MTLToolsDevice newUnwrappedStaticLinkingDescriptor:]
+ -[MTLToolsDevice queryTimestampFrequency]
+ -[MTLToolsDevice requiresLegacyCompilerProcessesCount]
+ -[MTLToolsDevice setRequiresLegacyCompilerProcessesCount:]
+ -[MTLToolsDevice sizeOfCounterHeapEntry:]
+ -[MTLToolsDevice supportsAIRNTBinaryArchiveFunctionPointers]
+ -[MTLToolsDevice supportsAIRNTBinaryArchiveSpecializedFunctions]
+ -[MTLToolsDevice supportsAIRNTBinaryArchiveStitchedFunctions]
+ -[MTLToolsDevice supportsAtomicWaitNotify]
+ -[MTLToolsDevice supportsCommandQueueBarriers]
+ -[MTLToolsDevice supportsIntersectionFunctionBuffers]
+ -[MTLToolsDevice supportsMTL4CommandAllocator]
+ -[MTLToolsDevice supportsMTL4CommandQueue]
+ -[MTLToolsDevice supportsMTL4Compiler]
+ -[MTLToolsDevice supportsMTL4ComputeCommandEncoder]
+ -[MTLToolsDevice supportsMTL4Counters]
+ -[MTLToolsDevice supportsMTL4LateBoundRenderTargets]
+ -[MTLToolsDevice supportsMTL4PSOSpecialization]
+ -[MTLToolsDevice supportsMTL4PlacementSparse]
+ -[MTLToolsDevice supportsMTL4RenderCommandEncoder]
+ -[MTLToolsDevice supportsMTLTextureViewPools]
+ -[MTLToolsDevice supportsMachineLearningCommandEncoders]
+ -[MTLToolsDevice supportsTensors]
+ -[MTLToolsDevice tensorSizeAndAlignWithDescriptor:]
+ -[MTLToolsDevice threadsPerCompilerProcess]
+ -[MTLToolsFunction functionConstants]
+ -[MTLToolsFunctionHandle binaryFunction]
+ -[MTLToolsFunctionHandle gpuResourceID]
+ -[MTLToolsFunctionHandle initWithBaseObject:parent:binaryFunction:]
+ -[MTLToolsFunctionHandle resourceIndex]
+ -[MTLToolsLibrary reflectionForFunctionWithName:]
+ -[MTLToolsRenderCommandEncoder setColorAttachmentMap:]
+ -[MTLToolsRenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:]
+ -[MTLToolsRenderPipelineState functionHandleWithBinaryFunction:stage:]
+ -[MTLToolsRenderPipelineState functionHandleWithName:stage:]
+ -[MTLToolsRenderPipelineState functionReflectionWithFunctionDescriptor:stage:]
+ -[MTLToolsRenderPipelineState newRenderPipelineDescriptorForSpecialization]
+ -[MTLToolsRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:]
+ -[MTLToolsRenderPipelineState reflectionForFunctionDescriptor:]
+ -[MTLToolsRenderPipelineState reflection]
+ -[MTLToolsRenderPipelineState requiredThreadsPerMeshThreadgroup]
+ -[MTLToolsRenderPipelineState requiredThreadsPerObjectThreadgroup]
+ -[MTLToolsRenderPipelineState requiredThreadsPerTileThreadgroup]
+ -[MTLToolsRenderPipelineState shaderValidationState]
+ -[MTLToolsRenderPipelineState shaderValidation]
+ -[MTLToolsResourceViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:]
+ -[MTLToolsResourceViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]
+ -[MTLToolsResourceViewPool dealloc]
+ -[MTLToolsResourceViewPool initWithBaseObject:parent:]
+ -[MTLToolsTensor bufferOffset]
+ -[MTLToolsTensor buffer]
+ -[MTLToolsTensor dataType]
+ -[MTLToolsTensor dealloc]
+ -[MTLToolsTensor dimensions]
+ -[MTLToolsTensor getBytes:strides:fromSlice:]
+ -[MTLToolsTensor getBytes:strides:fromSliceOrigin:sliceDimensions:]
+ -[MTLToolsTensor gpuResourceID]
+ -[MTLToolsTensor initWithBaseObject:buffer:]
+ -[MTLToolsTensor initWithBaseObject:parentTensor:]
+ -[MTLToolsTensor isTensorViewableWithReshapedDescriptor:]
+ -[MTLToolsTensor newTensorViewWithReshapedDescriptor:error:]
+ -[MTLToolsTensor newTensorViewWithSlice:error:]
+ -[MTLToolsTensor offset]
+ -[MTLToolsTensor parentTensor]
+ -[MTLToolsTensor replaceSlice:withBytes:strides:]
+ -[MTLToolsTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:]
+ -[MTLToolsTensor resourceIndex]
+ -[MTLToolsTensor strides]
+ -[MTLToolsTensor usage]
+ -[MTLToolsTensor wrapChildTensor:]
+ -[MTLToolsTexture newTextureViewWithDescriptor:]
+ -[MTLToolsTexture sparseTextureTier]
+ -[MTLToolsTextureViewPool baseResourceID]
+ -[MTLToolsTextureViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:]
+ -[MTLToolsTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]
+ -[MTLToolsTextureViewPool dealloc]
+ -[MTLToolsTextureViewPool initWithBaseObject:parent:]
+ -[MTLToolsTextureViewPool label]
+ -[MTLToolsTextureViewPool resourceViewCount]
+ -[MTLToolsTextureViewPool setTextureView:atIndex:]
+ -[MTLToolsTextureViewPool setTextureView:descriptor:atIndex:]
+ -[MTLToolsTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table151
+ GCC_except_table175
+ GCC_except_table179
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table233
+ GCC_except_table243
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table292
+ GCC_except_table296
+ GCC_except_table306
+ GCC_except_table45
+ GCC_except_table51
+ GCC_except_table67
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table91
+ OBJC_IVAR_$_MTLGPUDebugDevice._currentEncoderID
+ OBJC_IVAR_$_MTLGPUDebugDevice.commonResidencySet
+ OBJC_IVAR_$_MTLGPUDebugDevice.textureTypeTable
+ OBJC_IVAR_$__MTLCommandBuffer._privateData
+ OBJC_IVAR_$__MTLCommandBuffer._privateDataOffset
+ OBJC_IVAR_$__MTLCommandQueue._privateDataTable
+ OBJC_IVAR_$__MTLLogState._logBuffer
+ OBJC_IVAR_$__MTLLogState._logBufferResidencySet
+ _MTLFunctionHandleToToolsFunctionHandleWithBinaryFunction
+ _MTLFunctionHandleToToolsFunctionHandleWithDevice
+ _MTLGPUDebugReadReportBuffer.cold.1
+ _MTLSparsePageSizeString
+ _MTLTensorDataTypeString
+ _OBJC_CLASS_$_GPUDebugRetainedReportingData
+ _OBJC_CLASS_$_MTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureCurveGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureTriangleGeometryDescriptor
+ _OBJC_CLASS_$_MTL4ArgumentTableDescriptor
+ _OBJC_CLASS_$_MTL4BinaryFunctionDescriptor
+ _OBJC_CLASS_$_MTL4CommitOptions
+ _OBJC_CLASS_$_MTL4CompilerDescriptor
+ _OBJC_CLASS_$_MTL4CompilerTaskOptions
+ _OBJC_CLASS_$_MTL4ComputePipelineDescriptor
+ _OBJC_CLASS_$_MTL4CounterHeapDescriptor
+ _OBJC_CLASS_$_MTL4DebugArchive
+ _OBJC_CLASS_$_MTL4DebugArgumentTable
+ _OBJC_CLASS_$_MTL4DebugBinaryFunction
+ _OBJC_CLASS_$_MTL4DebugCommandAllocator
+ _OBJC_CLASS_$_MTL4DebugCommandBuffer
+ _OBJC_CLASS_$_MTL4DebugCommandEncoder
+ _OBJC_CLASS_$_MTL4DebugCommandQueue
+ _OBJC_CLASS_$_MTL4DebugCompiler
+ _OBJC_CLASS_$_MTL4DebugComputeCommandEncoder
+ _OBJC_CLASS_$_MTL4DebugCounterHeap
+ _OBJC_CLASS_$_MTL4DebugMachineLearningCommandEncoder
+ _OBJC_CLASS_$_MTL4DebugMachineLearningPipelineState
+ _OBJC_CLASS_$_MTL4DebugRenderCommandEncoder
+ _OBJC_CLASS_$_MTL4GPUDebugArchive
+ _OBJC_CLASS_$_MTL4GPUDebugBinaryFunction
+ _OBJC_CLASS_$_MTL4GPUDebugCommandBuffer
+ _OBJC_CLASS_$_MTL4GPUDebugCommandQueue
+ _OBJC_CLASS_$_MTL4GPUDebugCompiler
+ _OBJC_CLASS_$_MTL4GPUDebugComputeCommandEncoder
+ _OBJC_CLASS_$_MTL4GPUDebugRenderCommandEncoder
+ _OBJC_CLASS_$_MTL4IndirectInstanceAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4InstanceAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4LibraryDescriptor
+ _OBJC_CLASS_$_MTL4LibraryFunctionDescriptor
+ _OBJC_CLASS_$_MTL4MachineLearningPipelineDescriptor
+ _OBJC_CLASS_$_MTL4MeshRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4PipelineOptions
+ _OBJC_CLASS_$_MTL4PrimitiveAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4RenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4SpecializedFunctionDescriptor
+ _OBJC_CLASS_$_MTL4StitchedFunctionDescriptor
+ _OBJC_CLASS_$_MTL4TileRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4ToolsArchive
+ _OBJC_CLASS_$_MTL4ToolsArgumentTable
+ _OBJC_CLASS_$_MTL4ToolsBinaryFunction
+ _OBJC_CLASS_$_MTL4ToolsCommandAllocator
+ _OBJC_CLASS_$_MTL4ToolsCommandBuffer
+ _OBJC_CLASS_$_MTL4ToolsCommandEncoder
+ _OBJC_CLASS_$_MTL4ToolsCommandQueue
+ _OBJC_CLASS_$_MTL4ToolsCompiler
+ _OBJC_CLASS_$_MTL4ToolsCompilerTask
+ _OBJC_CLASS_$_MTL4ToolsComputeCommandEncoder
+ _OBJC_CLASS_$_MTL4ToolsCounterHeap
+ _OBJC_CLASS_$_MTL4ToolsMachineLearningCommandEncoder
+ _OBJC_CLASS_$_MTL4ToolsMachineLearningPipelineState
+ _OBJC_CLASS_$_MTL4ToolsPipelineDataSetSerializer
+ _OBJC_CLASS_$_MTL4ToolsRenderCommandEncoder
+ _OBJC_CLASS_$_MTLBufferDescriptor
+ _OBJC_CLASS_$_MTLDebugResourceViewPool
+ _OBJC_CLASS_$_MTLDebugTensor
+ _OBJC_CLASS_$_MTLDebugTextureViewPool
+ _OBJC_CLASS_$_MTLGPUDebugTextureViewPool
+ _OBJC_CLASS_$_MTLLogStateDescriptor
+ _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMap
+ _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
+ _OBJC_CLASS_$_MTLResidencySetDescriptor
+ _OBJC_CLASS_$_MTLResourceViewPoolDescriptor
+ _OBJC_CLASS_$_MTLToolsResourceViewPool
+ _OBJC_CLASS_$_MTLToolsTensor
+ _OBJC_CLASS_$_MTLToolsTextureViewPool
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$__MTLLibrary
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._cbAllocations
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._cbResidencySet
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._encoderLabels
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._privateData
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._usedBuffers
+ _OBJC_IVAR_$_GPUDebugRetainedReportingData._usedPipelineStates
+ _OBJC_IVAR_$_MTL4DebugArgumentTable._bufferBindings
+ _OBJC_IVAR_$_MTL4DebugArgumentTable._samplerBindings
+ _OBJC_IVAR_$_MTL4DebugArgumentTable._supportsAttributeStrides
+ _OBJC_IVAR_$_MTL4DebugArgumentTable._textureBindings
+ _OBJC_IVAR_$_MTL4DebugCommandAllocator._currentGeneration
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._aggregatedEncoderMask
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._allocatorGeneration
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._attachmentSet
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._currentAttachments
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._currentEncoder
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._currentState
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._debugCommandAllocator
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._prevAttachments
+ _OBJC_IVAR_$_MTL4DebugCommandBuffer._suspendResumeRenderPassInfo
+ _OBJC_IVAR_$_MTL4DebugCommandEncoder._baseObject
+ _OBJC_IVAR_$_MTL4DebugCommandEncoder._commandBuffer
+ _OBJC_IVAR_$_MTL4DebugCommandEncoder._device
+ _OBJC_IVAR_$_MTL4DebugCommandEncoder._encoderStageMask
+ _OBJC_IVAR_$_MTL4DebugCommandEncoder._encoderState
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._allowsNullBufferBindings
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentArgumentTable
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentComputePipelineState
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentImageBlockSize
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentSubstreamProgressLabels
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentThreadgroupMemoryLengths
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentVirtualSubstreamHasEncodedDispatch
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._currentVirtualSubstreamIndex
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._debugCommandEncoder
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._encoderState
+ _OBJC_IVAR_$_MTL4DebugComputeCommandEncoder._numSubstreams
+ _OBJC_IVAR_$_MTL4DebugMachineLearningCommandEncoder._currentArgumentTable
+ _OBJC_IVAR_$_MTL4DebugMachineLearningCommandEncoder._currentPipelineState
+ _OBJC_IVAR_$_MTL4DebugMachineLearningCommandEncoder._debugCommandEncoder
+ _OBJC_IVAR_$_MTL4DebugMachineLearningCommandEncoder._mlPipelineState
+ _OBJC_IVAR_$_MTL4DebugMachineLearningPipelineState._descriptor
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._allVisibilityOffsets
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._colorAttachmentMap
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentBlendColorAlpha
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentBlendColorBlue
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentBlendColorGreen
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentBlendColorRed
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentCullMode
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthBias
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthClamp
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthClipMode
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthSlopeScale
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthStencilState
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentFragmentArgumentTable
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentFrontFacingWinding
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentMeshArgumentTable
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentObjectArgumentTable
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentObjectThreadgroupMemoryLengths
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentRenderPipelineState
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentScissorRects
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentStencilBackReferenceValue
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentStencilFrontReferenceValue
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentThreadgroupMemoryArguments
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentTileArgumentTable
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentTriangleFillMode
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentVertexAmplificationCount
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentVertexArgumentTable
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentViewports
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentVisibilityResultMode
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentVisibilityResultModeOffset
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._debugCommandEncoder
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._descriptor
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._encoderState
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._height
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._resolvedColorSampleCount
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._resolvedRasterSampleCount
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._unknownStoreActions
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._width
+ _OBJC_IVAR_$_MTL4GPUDebugBinaryFunction.data
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._allocationLock
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._allocator
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._bufferUsageTables
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._currentPooledBuffer
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._currentPooledBufferOffset
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._deviceOptions
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._encodersResourceUsage
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._heapUsageTable
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._initialized
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._numDispatches
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._options
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._reportLogState
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._residencySets
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._supportsMeshStage
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._supportsTileStage
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._tempBufLock
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._textureTypeTables
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._textureUsageTables
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer.retainedData
+ _OBJC_IVAR_$_MTL4GPUDebugCommandQueue._commitMutex
+ _OBJC_IVAR_$_MTL4GPUDebugCommandQueue._deviceOptions
+ _OBJC_IVAR_$_MTL4GPUDebugCommandQueue._tracePath
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._accelerationStructureSupportLibrary
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._commandBufferJumpNestingLevel
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._computeEncoderBoundBufAddressTable
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._computeEncoderBoundBuffers
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._currentPipeline
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._dispatchID
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._enableUseResourceValidation
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._internalBindingTable
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._options
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder._threadgroup
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder.currentArgumentTable
+ _OBJC_IVAR_$_MTL4GPUDebugComputeCommandEncoder.useResourceIteration
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._currentDepthStencil
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._currentPipeline
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._drawID
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._enableUseResourceValidation
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._encoderType
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._fragmentStageActive
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._internalBindingTables
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._meshStageActive
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._meshThreadgroup
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._objectStageActive
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._options
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._tileStageActive
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._tileStageUsed
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._tileThreadgroup
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._vertexAmpState
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._vertexStageActive
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder.currentArgumentTables
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder.useResourceIteration
+ _OBJC_IVAR_$_MTL4ToolsBinaryFunction._relocations
+ _OBJC_IVAR_$_MTL4ToolsCommandAllocator._currentCommandBuffer
+ _OBJC_IVAR_$_MTL4ToolsCommandAllocator._label
+ _OBJC_IVAR_$_MTL4ToolsCommandBuffer._commandAllocator
+ _OBJC_IVAR_$_MTL4ToolsCommandBuffer._privateData
+ _OBJC_IVAR_$_MTL4ToolsCommandBuffer._usedResidencySets
+ _OBJC_IVAR_$_MTL4ToolsCommandEncoder._commandAllocator
+ _OBJC_IVAR_$_MTL4ToolsCommandEncoder._commandBuffer
+ _OBJC_IVAR_$_MTL4ToolsCommandQueue._addedResidencySets
+ _OBJC_IVAR_$_MTL4ToolsCommandQueue._lastCommittedCommandBuffer
+ _OBJC_IVAR_$_MTL4ToolsCompilerTask.compiler
+ _OBJC_IVAR_$_MTLDebugBuffer._placementSparsePageSize
+ _OBJC_IVAR_$_MTLDebugComputePipelineState._mtl4Descriptor
+ _OBJC_IVAR_$_MTLDebugComputePipelineState._validationReflection
+ _OBJC_IVAR_$_MTLDebugFunction._intersectionFunctionSignature
+ _OBJC_IVAR_$_MTLDebugHeap._maxCompatiblePlacementSparsePageSize
+ _OBJC_IVAR_$_MTLDebugRenderCommandEncoder._colorAttachmentMap
+ _OBJC_IVAR_$_MTLDebugRenderPipelineState._mtl4Descriptor
+ _OBJC_IVAR_$_MTLDebugRenderPipelineState._mtl4MeshDescriptor
+ _OBJC_IVAR_$_MTLDebugRenderPipelineState._mtl4TileDescriptor
+ _OBJC_IVAR_$_MTLDebugRenderPipelineState._validationReflection
+ _OBJC_IVAR_$_MTLDebugTexture._placementSparsePageSize
+ _OBJC_IVAR_$_MTLGPUDebugBuffer._activeViews
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._commandQueue
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._internalBindingTables
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._numDispatches
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._reportLogState
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._usedBytesBuffers
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._usedBytesBuffersLock
+ _OBJC_IVAR_$_MTLGPUDebugComputeCommandEncoder._computeEncoderBoundBuffers
+ _OBJC_IVAR_$_MTLGPUDebugComputeCommandEncoder._internalBindingTable
+ _OBJC_IVAR_$_MTLGPUDebugDevice._icbInheritBothMeshVertexPipelineState
+ _OBJC_IVAR_$_MTLGPUDebugDevice._icbInheritBothVertexPipelineState
+ _OBJC_IVAR_$_MTLGPUDebugGPULog._computePipeline
+ _OBJC_IVAR_$_MTLGPUDebugGPULog._functionName
+ _OBJC_IVAR_$_MTLGPUDebugGPULog._functionType
+ _OBJC_IVAR_$_MTLGPUDebugGPULog._renderPipeline
+ _OBJC_IVAR_$_MTLGPUDebugImageData._binaryFunction
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._SVBindingTableFragmentBuffer
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._SVBindingTableMeshBuffer
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._SVBindingTableObjectBuffer
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._SVBindingTableVertexKernelBuffer
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._hasOnlyRender
+ _OBJC_IVAR_$_MTLGPUDebugIndirectCommandBuffer._initializedTables
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._fragmentEncoderBoundBuffers
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._internalBindingTables
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._meshEncoderBoundBuffers
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._objectEncoderBoundBuffers
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._vertexEncoderBoundBuffers
+ _OBJC_IVAR_$_MTLGPUDebugTexture._activeViews
+ _OBJC_IVAR_$_MTLGPUDebugTextureViewPool.viewables
+ _OBJC_IVAR_$_MTLToolsFunctionHandle._binaryFunction
+ _OBJC_IVAR_$_MTLToolsTensor._buffer
+ _OBJC_IVAR_$_MTLToolsTensor._parentTensor
+ _OBJC_METACLASS_$_GPUDebugRetainedReportingData
+ _OBJC_METACLASS_$_MTL4DebugArchive
+ _OBJC_METACLASS_$_MTL4DebugArgumentTable
+ _OBJC_METACLASS_$_MTL4DebugBinaryFunction
+ _OBJC_METACLASS_$_MTL4DebugCommandAllocator
+ _OBJC_METACLASS_$_MTL4DebugCommandBuffer
+ _OBJC_METACLASS_$_MTL4DebugCommandEncoder
+ _OBJC_METACLASS_$_MTL4DebugCommandQueue
+ _OBJC_METACLASS_$_MTL4DebugCompiler
+ _OBJC_METACLASS_$_MTL4DebugComputeCommandEncoder
+ _OBJC_METACLASS_$_MTL4DebugCounterHeap
+ _OBJC_METACLASS_$_MTL4DebugMachineLearningCommandEncoder
+ _OBJC_METACLASS_$_MTL4DebugMachineLearningPipelineState
+ _OBJC_METACLASS_$_MTL4DebugRenderCommandEncoder
+ _OBJC_METACLASS_$_MTL4GPUDebugArchive
+ _OBJC_METACLASS_$_MTL4GPUDebugBinaryFunction
+ _OBJC_METACLASS_$_MTL4GPUDebugCommandBuffer
+ _OBJC_METACLASS_$_MTL4GPUDebugCommandQueue
+ _OBJC_METACLASS_$_MTL4GPUDebugCompiler
+ _OBJC_METACLASS_$_MTL4GPUDebugComputeCommandEncoder
+ _OBJC_METACLASS_$_MTL4GPUDebugRenderCommandEncoder
+ _OBJC_METACLASS_$_MTL4ToolsArchive
+ _OBJC_METACLASS_$_MTL4ToolsArgumentTable
+ _OBJC_METACLASS_$_MTL4ToolsBinaryFunction
+ _OBJC_METACLASS_$_MTL4ToolsCommandAllocator
+ _OBJC_METACLASS_$_MTL4ToolsCommandBuffer
+ _OBJC_METACLASS_$_MTL4ToolsCommandEncoder
+ _OBJC_METACLASS_$_MTL4ToolsCommandQueue
+ _OBJC_METACLASS_$_MTL4ToolsCompiler
+ _OBJC_METACLASS_$_MTL4ToolsCompilerTask
+ _OBJC_METACLASS_$_MTL4ToolsComputeCommandEncoder
+ _OBJC_METACLASS_$_MTL4ToolsCounterHeap
+ _OBJC_METACLASS_$_MTL4ToolsMachineLearningCommandEncoder
+ _OBJC_METACLASS_$_MTL4ToolsMachineLearningPipelineState
+ _OBJC_METACLASS_$_MTL4ToolsPipelineDataSetSerializer
+ _OBJC_METACLASS_$_MTL4ToolsRenderCommandEncoder
+ _OBJC_METACLASS_$_MTLDebugResourceViewPool
+ _OBJC_METACLASS_$_MTLDebugTensor
+ _OBJC_METACLASS_$_MTLDebugTextureViewPool
+ _OBJC_METACLASS_$_MTLGPUDebugTextureViewPool
+ _OBJC_METACLASS_$_MTLToolsResourceViewPool
+ _OBJC_METACLASS_$_MTLToolsTensor
+ _OBJC_METACLASS_$_MTLToolsTextureViewPool
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __Block_object_assign
+ __MTL4DebugFunctionDescriptorName
+ __MTLDebugBlitOptionString
+ __MTLDebugCullModeString
+ __MTLDebugDepthClipModeString
+ __MTLDebugFindMaxTextureWidth
+ __MTLDebugIndexTypeSize
+ __MTLDebugIsValidSparsePageSize
+ __MTLDebugTriangleFillModeString
+ __MTLDebugValidateBlitOption
+ __MTLDebugValidateRenderPassDescriptorAndTrackAttachments
+ __MTLDebugValidateStoreLoadTransitionAndTrackAttachments
+ __MTLDebugVisibilityResultModeString
+ __MTLDebugWindingString
+ __MTLLoadActionString
+ __MTLMultisampleDepthResolveFilterString
+ __MTLStoreActionString
+ __MTLTensorElementCount
+ __MTLTensorExtentsAreEqual
+ __MTLValidateRenderPassDescriptorTileProperties
+ __OBJC_$_INSTANCE_METHODS_GPUDebugRetainedReportingData
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugArchive
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugArgumentTable
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCommandAllocator
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCommandBuffer
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCommandQueue
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCompiler
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugComputeCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugCounterHeap
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugMachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugMachineLearningPipelineState
+ __OBJC_$_INSTANCE_METHODS_MTL4DebugRenderCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugArchive
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugBinaryFunction
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugCommandBuffer
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugCommandQueue
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugCompiler
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsArchive
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsArgumentTable
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsBinaryFunction
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCommandAllocator
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCommandBuffer
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCommandQueue
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCompiler
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCompilerTask
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsComputeCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsCounterHeap
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsMachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsMachineLearningPipelineState
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsPipelineDataSetSerializer
+ __OBJC_$_INSTANCE_METHODS_MTL4ToolsRenderCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_MTLDebugResourceViewPool
+ __OBJC_$_INSTANCE_METHODS_MTLDebugTensor
+ __OBJC_$_INSTANCE_METHODS_MTLDebugTextureViewPool
+ __OBJC_$_INSTANCE_METHODS_MTLGPUDebugTextureViewPool
+ __OBJC_$_INSTANCE_METHODS_MTLToolsResourceViewPool
+ __OBJC_$_INSTANCE_METHODS_MTLToolsTensor
+ __OBJC_$_INSTANCE_METHODS_MTLToolsTextureViewPool
+ __OBJC_$_INSTANCE_VARIABLES_GPUDebugRetainedReportingData
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugArgumentTable
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugCommandAllocator
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugCommandBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugComputeCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugMachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugMachineLearningPipelineState
+ __OBJC_$_INSTANCE_VARIABLES_MTL4DebugRenderCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4GPUDebugBinaryFunction
+ __OBJC_$_INSTANCE_VARIABLES_MTL4GPUDebugCommandBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MTL4GPUDebugCommandQueue
+ __OBJC_$_INSTANCE_VARIABLES_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsBinaryFunction
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsCommandAllocator
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsCommandBuffer
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsCommandQueue
+ __OBJC_$_INSTANCE_VARIABLES_MTL4ToolsCompilerTask
+ __OBJC_$_INSTANCE_VARIABLES_MTLGPUDebugTextureViewPool
+ __OBJC_$_INSTANCE_VARIABLES_MTLToolsTensor
+ __OBJC_$_PROP_LIST_GPUDebugRetainedReportingData
+ __OBJC_$_PROP_LIST_MTL4Archive
+ __OBJC_$_PROP_LIST_MTL4ArgumentTable
+ __OBJC_$_PROP_LIST_MTL4BinaryFunction
+ __OBJC_$_PROP_LIST_MTL4BinaryFunctionSPI
+ __OBJC_$_PROP_LIST_MTL4CommandAllocator
+ __OBJC_$_PROP_LIST_MTL4CommandBuffer
+ __OBJC_$_PROP_LIST_MTL4CommandBufferGGDSPI
+ __OBJC_$_PROP_LIST_MTL4CommandBufferSPI
+ __OBJC_$_PROP_LIST_MTL4CommandEncoder
+ __OBJC_$_PROP_LIST_MTL4CommandEncoderGGDSPI
+ __OBJC_$_PROP_LIST_MTL4CommandQueue
+ __OBJC_$_PROP_LIST_MTL4CommandQueueSPI
+ __OBJC_$_PROP_LIST_MTL4Compiler
+ __OBJC_$_PROP_LIST_MTL4CompilerGGDSPI
+ __OBJC_$_PROP_LIST_MTL4CompilerTask
+ __OBJC_$_PROP_LIST_MTL4CounterHeap
+ __OBJC_$_PROP_LIST_MTL4DebugCommandAllocator
+ __OBJC_$_PROP_LIST_MTL4DebugCommandBuffer
+ __OBJC_$_PROP_LIST_MTL4DebugCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4DebugMachineLearningCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4DebugMachineLearningPipelineState
+ __OBJC_$_PROP_LIST_MTL4GPUDebugCommandBuffer
+ __OBJC_$_PROP_LIST_MTL4GPUDebugCommandQueue
+ __OBJC_$_PROP_LIST_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4MachineLearningPipelineState
+ __OBJC_$_PROP_LIST_MTL4RenderCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4ToolsArchive
+ __OBJC_$_PROP_LIST_MTL4ToolsArgumentTable
+ __OBJC_$_PROP_LIST_MTL4ToolsBinaryFunction
+ __OBJC_$_PROP_LIST_MTL4ToolsCommandAllocator
+ __OBJC_$_PROP_LIST_MTL4ToolsCommandBuffer
+ __OBJC_$_PROP_LIST_MTL4ToolsCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4ToolsCommandQueue
+ __OBJC_$_PROP_LIST_MTL4ToolsCompiler
+ __OBJC_$_PROP_LIST_MTL4ToolsCompilerTask
+ __OBJC_$_PROP_LIST_MTL4ToolsComputeCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4ToolsCounterHeap
+ __OBJC_$_PROP_LIST_MTL4ToolsMachineLearningCommandEncoder
+ __OBJC_$_PROP_LIST_MTL4ToolsMachineLearningPipelineState
+ __OBJC_$_PROP_LIST_MTL4ToolsPipelineDataSetSerializer
+ __OBJC_$_PROP_LIST_MTL4ToolsRenderCommandEncoder
+ __OBJC_$_PROP_LIST_MTLDrawable
+ __OBJC_$_PROP_LIST_MTLDrawableSPI
+ __OBJC_$_PROP_LIST_MTLFunctionHandleSPI
+ __OBJC_$_PROP_LIST_MTLResourceViewPool
+ __OBJC_$_PROP_LIST_MTLTensor
+ __OBJC_$_PROP_LIST_MTLTensorSPI
+ __OBJC_$_PROP_LIST_MTLToolsResourceViewPool
+ __OBJC_$_PROP_LIST_MTLToolsTensor
+ __OBJC_$_PROP_LIST_MTLToolsTextureViewPool
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4Archive
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ArchiveGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ArgumentTableGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandAllocatorGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandBufferGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandBufferSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandQueueGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandQueueSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4Compiler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CompilerGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CompilerTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CompilerTaskGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ComputeCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CounterHeapGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningPipelineStateGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4PipelineDataSetSerializerGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4RenderCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLDrawable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLDrawableSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFunctionHandleSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLGPUDebugViewable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTensor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTensorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTextureViewPool
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTLDrawableSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTLIndirectComputeCommandSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4Archive
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ArchiveGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ArgumentTableGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandAllocatorGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandBufferGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandBufferSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandQueueGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandQueueSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4Compiler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CompilerGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CompilerTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CompilerTaskGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ComputeCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CounterHeapGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningPipelineStateGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4PipelineDataSetSerializerGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4RenderCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLDrawable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLDrawableSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFunctionHandleSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLGPUDebugViewable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTensor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTensorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTextureViewPool
+ __OBJC_$_PROTOCOL_REFS_MTL4Archive
+ __OBJC_$_PROTOCOL_REFS_MTL4ArchiveGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4ArchiveSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_REFS_MTL4ArgumentTableGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4ArgumentTableSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_REFS_MTL4BinaryFunctionGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandAllocatorGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandAllocatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandBufferGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandBufferSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandQueueGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandQueueSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4Compiler
+ __OBJC_$_PROTOCOL_REFS_MTL4CompilerGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CompilerSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CompilerTask
+ __OBJC_$_PROTOCOL_REFS_MTL4CompilerTaskGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CompilerTaskSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4ComputeCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_REFS_MTL4CounterHeapGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningPipelineStateGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningPipelineStateSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_REFS_MTL4PipelineDataSetSerializerGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4PipelineDataSetSerializerSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4RenderCommandEncoderGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTLDrawable
+ __OBJC_$_PROTOCOL_REFS_MTLDrawableSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFunctionHandleSPI
+ __OBJC_$_PROTOCOL_REFS_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_REFS_MTLResourceViewPoolGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTLResourceViewPoolSPI
+ __OBJC_$_PROTOCOL_REFS_MTLTensor
+ __OBJC_$_PROTOCOL_REFS_MTLTensorSPI
+ __OBJC_$_PROTOCOL_REFS_MTLTextureViewPool
+ __OBJC_$_PROTOCOL_REFS_MTLTextureViewPoolGGDSPI
+ __OBJC_$_PROTOCOL_REFS_MTLTextureViewPoolSPI
+ __OBJC_CLASS_PROTOCOLS_$_MTL4GPUDebugCommandBuffer
+ __OBJC_CLASS_PROTOCOLS_$_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsArchive
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsArgumentTable
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsBinaryFunction
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCommandAllocator
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCommandBuffer
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCommandQueue
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCompiler
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCompilerTask
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsComputeCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsCounterHeap
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsMachineLearningCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsMachineLearningPipelineState
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsPipelineDataSetSerializer
+ __OBJC_CLASS_PROTOCOLS_$_MTL4ToolsRenderCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_MTLDebugTensor
+ __OBJC_CLASS_PROTOCOLS_$_MTLToolsResourceViewPool
+ __OBJC_CLASS_PROTOCOLS_$_MTLToolsTensor
+ __OBJC_CLASS_PROTOCOLS_$_MTLToolsTextureViewPool
+ __OBJC_CLASS_RO_$_GPUDebugRetainedReportingData
+ __OBJC_CLASS_RO_$_MTL4DebugArchive
+ __OBJC_CLASS_RO_$_MTL4DebugArgumentTable
+ __OBJC_CLASS_RO_$_MTL4DebugBinaryFunction
+ __OBJC_CLASS_RO_$_MTL4DebugCommandAllocator
+ __OBJC_CLASS_RO_$_MTL4DebugCommandBuffer
+ __OBJC_CLASS_RO_$_MTL4DebugCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4DebugCommandQueue
+ __OBJC_CLASS_RO_$_MTL4DebugCompiler
+ __OBJC_CLASS_RO_$_MTL4DebugComputeCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4DebugCounterHeap
+ __OBJC_CLASS_RO_$_MTL4DebugMachineLearningCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4DebugMachineLearningPipelineState
+ __OBJC_CLASS_RO_$_MTL4DebugRenderCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4GPUDebugArchive
+ __OBJC_CLASS_RO_$_MTL4GPUDebugBinaryFunction
+ __OBJC_CLASS_RO_$_MTL4GPUDebugCommandBuffer
+ __OBJC_CLASS_RO_$_MTL4GPUDebugCommandQueue
+ __OBJC_CLASS_RO_$_MTL4GPUDebugCompiler
+ __OBJC_CLASS_RO_$_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4ToolsArchive
+ __OBJC_CLASS_RO_$_MTL4ToolsArgumentTable
+ __OBJC_CLASS_RO_$_MTL4ToolsBinaryFunction
+ __OBJC_CLASS_RO_$_MTL4ToolsCommandAllocator
+ __OBJC_CLASS_RO_$_MTL4ToolsCommandBuffer
+ __OBJC_CLASS_RO_$_MTL4ToolsCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4ToolsCommandQueue
+ __OBJC_CLASS_RO_$_MTL4ToolsCompiler
+ __OBJC_CLASS_RO_$_MTL4ToolsCompilerTask
+ __OBJC_CLASS_RO_$_MTL4ToolsComputeCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4ToolsCounterHeap
+ __OBJC_CLASS_RO_$_MTL4ToolsMachineLearningCommandEncoder
+ __OBJC_CLASS_RO_$_MTL4ToolsMachineLearningPipelineState
+ __OBJC_CLASS_RO_$_MTL4ToolsPipelineDataSetSerializer
+ __OBJC_CLASS_RO_$_MTL4ToolsRenderCommandEncoder
+ __OBJC_CLASS_RO_$_MTLDebugResourceViewPool
+ __OBJC_CLASS_RO_$_MTLDebugTensor
+ __OBJC_CLASS_RO_$_MTLDebugTextureViewPool
+ __OBJC_CLASS_RO_$_MTLGPUDebugTextureViewPool
+ __OBJC_CLASS_RO_$_MTLToolsResourceViewPool
+ __OBJC_CLASS_RO_$_MTLToolsTensor
+ __OBJC_CLASS_RO_$_MTLToolsTextureViewPool
+ __OBJC_LABEL_PROTOCOL_$_MTL4Archive
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArchiveGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArchiveSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArgumentTable
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArgumentTableGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArgumentTableSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4BinaryFunction
+ __OBJC_LABEL_PROTOCOL_$_MTL4BinaryFunctionGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4BinaryFunctionSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandAllocator
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandAllocatorGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandAllocatorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandBuffer
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandBufferGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandBufferSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandEncoderGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandQueue
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandQueueGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandQueueSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4Compiler
+ __OBJC_LABEL_PROTOCOL_$_MTL4CompilerGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CompilerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CompilerTask
+ __OBJC_LABEL_PROTOCOL_$_MTL4CompilerTaskGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CompilerTaskSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4ComputeCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4ComputeCommandEncoderGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4ComputeCommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CounterHeap
+ __OBJC_LABEL_PROTOCOL_$_MTL4CounterHeapGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningCommandEncoderGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningPipelineState
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningPipelineStateGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningPipelineStateSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4PipelineDataSetSerializer
+ __OBJC_LABEL_PROTOCOL_$_MTL4PipelineDataSetSerializerGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4PipelineDataSetSerializerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4RenderCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4RenderCommandEncoderGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4RenderCommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLDrawable
+ __OBJC_LABEL_PROTOCOL_$_MTLDrawableSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFunctionHandleSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLGPUDebugViewable
+ __OBJC_LABEL_PROTOCOL_$_MTLResourceViewPool
+ __OBJC_LABEL_PROTOCOL_$_MTLResourceViewPoolGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLResourceViewPoolSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLTensor
+ __OBJC_LABEL_PROTOCOL_$_MTLTensorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLTextureViewPool
+ __OBJC_LABEL_PROTOCOL_$_MTLTextureViewPoolGGDSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLTextureViewPoolSPI
+ __OBJC_METACLASS_RO_$_GPUDebugRetainedReportingData
+ __OBJC_METACLASS_RO_$_MTL4DebugArchive
+ __OBJC_METACLASS_RO_$_MTL4DebugArgumentTable
+ __OBJC_METACLASS_RO_$_MTL4DebugBinaryFunction
+ __OBJC_METACLASS_RO_$_MTL4DebugCommandAllocator
+ __OBJC_METACLASS_RO_$_MTL4DebugCommandBuffer
+ __OBJC_METACLASS_RO_$_MTL4DebugCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4DebugCommandQueue
+ __OBJC_METACLASS_RO_$_MTL4DebugCompiler
+ __OBJC_METACLASS_RO_$_MTL4DebugComputeCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4DebugCounterHeap
+ __OBJC_METACLASS_RO_$_MTL4DebugMachineLearningCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4DebugMachineLearningPipelineState
+ __OBJC_METACLASS_RO_$_MTL4DebugRenderCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugArchive
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugBinaryFunction
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugCommandBuffer
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugCommandQueue
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugCompiler
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugComputeCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4GPUDebugRenderCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4ToolsArchive
+ __OBJC_METACLASS_RO_$_MTL4ToolsArgumentTable
+ __OBJC_METACLASS_RO_$_MTL4ToolsBinaryFunction
+ __OBJC_METACLASS_RO_$_MTL4ToolsCommandAllocator
+ __OBJC_METACLASS_RO_$_MTL4ToolsCommandBuffer
+ __OBJC_METACLASS_RO_$_MTL4ToolsCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4ToolsCommandQueue
+ __OBJC_METACLASS_RO_$_MTL4ToolsCompiler
+ __OBJC_METACLASS_RO_$_MTL4ToolsCompilerTask
+ __OBJC_METACLASS_RO_$_MTL4ToolsComputeCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4ToolsCounterHeap
+ __OBJC_METACLASS_RO_$_MTL4ToolsMachineLearningCommandEncoder
+ __OBJC_METACLASS_RO_$_MTL4ToolsMachineLearningPipelineState
+ __OBJC_METACLASS_RO_$_MTL4ToolsPipelineDataSetSerializer
+ __OBJC_METACLASS_RO_$_MTL4ToolsRenderCommandEncoder
+ __OBJC_METACLASS_RO_$_MTLDebugResourceViewPool
+ __OBJC_METACLASS_RO_$_MTLDebugTensor
+ __OBJC_METACLASS_RO_$_MTLDebugTextureViewPool
+ __OBJC_METACLASS_RO_$_MTLGPUDebugTextureViewPool
+ __OBJC_METACLASS_RO_$_MTLToolsResourceViewPool
+ __OBJC_METACLASS_RO_$_MTLToolsTensor
+ __OBJC_METACLASS_RO_$_MTLToolsTextureViewPool
+ __OBJC_PROTOCOL_$_MTL4Archive
+ __OBJC_PROTOCOL_$_MTL4ArchiveGGDSPI
+ __OBJC_PROTOCOL_$_MTL4ArchiveSPI
+ __OBJC_PROTOCOL_$_MTL4ArgumentTable
+ __OBJC_PROTOCOL_$_MTL4ArgumentTableGGDSPI
+ __OBJC_PROTOCOL_$_MTL4ArgumentTableSPI
+ __OBJC_PROTOCOL_$_MTL4BinaryFunction
+ __OBJC_PROTOCOL_$_MTL4BinaryFunctionGGDSPI
+ __OBJC_PROTOCOL_$_MTL4BinaryFunctionSPI
+ __OBJC_PROTOCOL_$_MTL4CommandAllocator
+ __OBJC_PROTOCOL_$_MTL4CommandAllocatorGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CommandAllocatorSPI
+ __OBJC_PROTOCOL_$_MTL4CommandBuffer
+ __OBJC_PROTOCOL_$_MTL4CommandBufferGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CommandBufferSPI
+ __OBJC_PROTOCOL_$_MTL4CommandEncoder
+ __OBJC_PROTOCOL_$_MTL4CommandEncoderGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTL4CommandQueue
+ __OBJC_PROTOCOL_$_MTL4CommandQueueGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CommandQueueSPI
+ __OBJC_PROTOCOL_$_MTL4Compiler
+ __OBJC_PROTOCOL_$_MTL4CompilerGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CompilerSPI
+ __OBJC_PROTOCOL_$_MTL4CompilerTask
+ __OBJC_PROTOCOL_$_MTL4CompilerTaskGGDSPI
+ __OBJC_PROTOCOL_$_MTL4CompilerTaskSPI
+ __OBJC_PROTOCOL_$_MTL4ComputeCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4ComputeCommandEncoderGGDSPI
+ __OBJC_PROTOCOL_$_MTL4ComputeCommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTL4CounterHeap
+ __OBJC_PROTOCOL_$_MTL4CounterHeapGGDSPI
+ __OBJC_PROTOCOL_$_MTL4MachineLearningCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4MachineLearningCommandEncoderGGDSPI
+ __OBJC_PROTOCOL_$_MTL4MachineLearningPipelineState
+ __OBJC_PROTOCOL_$_MTL4MachineLearningPipelineStateGGDSPI
+ __OBJC_PROTOCOL_$_MTL4MachineLearningPipelineStateSPI
+ __OBJC_PROTOCOL_$_MTL4PipelineDataSetSerializer
+ __OBJC_PROTOCOL_$_MTL4PipelineDataSetSerializerGGDSPI
+ __OBJC_PROTOCOL_$_MTL4PipelineDataSetSerializerSPI
+ __OBJC_PROTOCOL_$_MTL4RenderCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4RenderCommandEncoderGGDSPI
+ __OBJC_PROTOCOL_$_MTL4RenderCommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTLDrawable
+ __OBJC_PROTOCOL_$_MTLDrawableSPI
+ __OBJC_PROTOCOL_$_MTLFunctionHandleSPI
+ __OBJC_PROTOCOL_$_MTLGPUDebugViewable
+ __OBJC_PROTOCOL_$_MTLResourceViewPool
+ __OBJC_PROTOCOL_$_MTLResourceViewPoolGGDSPI
+ __OBJC_PROTOCOL_$_MTLResourceViewPoolSPI
+ __OBJC_PROTOCOL_$_MTLTensor
+ __OBJC_PROTOCOL_$_MTLTensorSPI
+ __OBJC_PROTOCOL_$_MTLTextureViewPool
+ __OBJC_PROTOCOL_$_MTLTextureViewPoolGGDSPI
+ __OBJC_PROTOCOL_$_MTLTextureViewPoolSPI
+ __OBJC_PROTOCOL_REFERENCE_$_MTLDrawableSPI
+ __OBJC_PROTOCOL_REFERENCE_$_MTLEvent
+ __OBJC_PROTOCOL_REFERENCE_$_MTLFence
+ __OBJC_PROTOCOL_REFERENCE_$_MTLGPUDebugViewable
+ __OBJC_PROTOCOL_REFERENCE_$_MTLLibrary
+ __OBJC_PROTOCOL_REFERENCE_$_MTLRenderPipelineState
+ __Z11checkBufferP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectPU19objcproto9MTLBuffer11objc_objectmbP8NSString
+ __Z16checkBufferRangeP18_MTLMessageContextPU19objcproto9MTLDevice11objc_object15MTL4BufferRangebP8NSString
+ __Z16dumpBindingTablePU19objcproto9MTLBuffer11objc_object
+ __Z16dumpBindingTablePy
+ __Z18checkPrimitiveDataP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP43MTL4AccelerationStructureGeometryDescriptorm
+ __Z18checkPrimitiveDataP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP43MTL4AccelerationStructureGeometryDescriptorm.cold.1
+ __Z18checkPrimitiveDataP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP43MTL4AccelerationStructureGeometryDescriptorm.cold.2
+ __Z18checkPrimitiveDataP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP43MTL4AccelerationStructureGeometryDescriptorm.cold.3
+ __Z19DebugCompileOptionsP17MTLGPUDebugDeviceP17MTLCompileOptions
+ __Z20checkMotionParameterP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP44MTL4PrimitiveAccelerationStructureDescriptor
+ __Z20checkMotionParameterP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP44MTL4PrimitiveAccelerationStructureDescriptor.cold.1
+ __Z22resourceUsageForBufferP17MTLGPUDebugBuffermPK16BufferUsageTable
+ __Z23MTL4TransformTypeStride16MTLTransformType
+ __Z26checkAccelerationStructureP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectPU35objcproto24MTLAccelerationStructure11objc_objectbP8NSString
+ __Z26hasUnspecializedPropertiesI28MTL4RenderPipelineDescriptorEbPT_
+ __Z26hasUnspecializedPropertiesI32MTL4MeshRenderPipelineDescriptorEbPT_
+ __Z31validateUnspecializedPropertiesI28MTL4RenderPipelineDescriptorEvP14MTLDebugDevicePT_P18_MTLMessageContext
+ __Z31validateUnspecializedPropertiesI32MTL4MeshRenderPipelineDescriptorEvP14MTLDebugDevicePT_P18_MTLMessageContext
+ __Z32specializeMTL4PipelineDescriptorI28MTL4RenderPipelineDescriptorEvPT_S2_
+ __Z32specializeMTL4PipelineDescriptorI32MTL4MeshRenderPipelineDescriptorEvPT_S2_
+ __Z34generatePipelineHashWithDescriptorP22MTL4PipelineDescriptor
+ __Z36validateMTL4RenderPipelineDescriptorP14MTLDebugDeviceP22MTL4PipelineDescriptorP18_MTLMessageContext
+ __Z43MTL4AccelerationStructureTypeFromDescriptorP35MTL4AccelerationStructureDescriptor
+ __Z54isValidMTL4AccelerationStructureInstanceDescriptorType46MTLAccelerationStructureInstanceDescriptorType
+ __Z7logHeapPvi
+ __ZGVZ56_MTLDebugValidateRenderPassDescriptorAndTrackAttachmentsE50is_dyld_program_sdk_at_least_fall_2025_os_versions
+ __ZL12newImageDataP22MTL4FunctionDescriptor15MTLFunctionTypeP27MTLDebugInstrumentationDataP17MTLGPUDebugDevice
+ __ZL19addReflectionOptionP22MTL4PipelineDescriptor
+ __ZL20argumentTypeToString22MTLArgumentTypePrivate
+ __ZL22PrepareExecuteIndirectP33MTL4GPUDebugComputeCommandEncoderP32MTLGPUDebugIndirectCommandBufferNSt3__17variantIJNS3_4pairIymEE38MTLIndirectCommandBufferExecutionRangeEEE
+ __ZL29_prepareBinaryLinkedFunctionsP41MTL4PipelineStageDynamicLinkingDescriptorP17MTLGPUDebugDevice
+ __ZL32validateNewDynamicLibraryWithURLP5NSURLP18_MTLMessageContext
+ __ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDeviceP22MTL4PipelineDescriptorS2_
+ __ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDeviceP22MTL4PipelineDescriptorS2_.cold.1
+ __ZL45validateBeginCommandBufferWithAllocatorCommonP18_MTLMessageContextPU28objcproto17MTL4CommandBuffer11objc_objectPU31objcproto20MTL4CommandAllocator11objc_object
+ __ZL45validateBeginCommandBufferWithAllocatorCommonP18_MTLMessageContextPU28objcproto17MTL4CommandBuffer11objc_objectPU31objcproto20MTL4CommandAllocator11objc_object.cold.1
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.1
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.10
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.11
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.12
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.13
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.14
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.15
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.16
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.17
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.18
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.19
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.2
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.20
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.21
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.22
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.23
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.24
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.25
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.26
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.27
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.28
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.29
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.3
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.30
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.31
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.32
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.33
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.34
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.4
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.5
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.6
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.7
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.8
+ __ZL56checkMTL4AccelerationStructureDescriptorWithRefitOptionsP18_MTLMessageContextPU19objcproto9MTLDevice11objc_objectP35MTL4AccelerationStructureDescriptorbm.cold.9
+ __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU26objcproto15MTLSamplerState11objc_objectEEJPKfS9_8_NSRangeEEEvRT_RKT0_DpRKT1_
+ __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKfEEJS5_8_NSRangeEEEvRT_RKT0_DpRKT1_
+ __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferEPU21objcproto10MTLTexture11objc_objectJmm9MTLOriginmEEEvRT_RKT0_DpRKT1_
+ __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferENS_5ArrayIKPU19objcproto9MTLBuffer11objc_objectEEJNS2_IKmEES8_8_NSRangeEEEvRT_RKT0_DpRKT1_
+ __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferENS_5ArrayIKPU26objcproto15MTLSamplerState11objc_objectEEJNS2_IKfEES8_8_NSRangeEEEvRT_RKT0_DpRKT1_
+ __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferEPU21objcproto10MTLTexture11objc_objectJmm9MTLOrigin7MTLSizePU19objcproto9MTLBuffer11objc_objectmmmEEEvRT_RKT0_DpRKT1_
+ __ZN14HeapUsageTable23mergeHeapStagesAndUsageEP15MTLGPUDebugHeapmm
+ __ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5_
+ __ZN16BufferUsageTable11addResourceEP17MTLGPUDebugDeviceP17MTLGPUDebugBufferm
+ __ZN16BufferUsageTable5allocEP17MTLGPUDebugDevicej
+ __ZN16BufferUsageTable8setUsageEjm
+ __ZN16TextureTypeTable11addResourceEP17MTLGPUDebugDeviceP18MTLGPUDebugTexture
+ __ZN16TextureTypeTable14removeResourceEP17MTLGPUDebugDeviceP18MTLGPUDebugTexture
+ __ZN16TextureTypeTable7setTypeEy14MTLTextureType
+ __ZN17TextureUsageTable11addResourceEP17MTLGPUDebugDeviceym
+ __ZN17TextureUsageTable8setUsageEjm
+ __ZN18ResourceUsageTable4freeEv
+ __ZN18ResourceUsageTable5allocEP17MTLGPUDebugDevicem
+ __ZN18ResourceUsageTable7reallocEP17MTLGPUDebugDevicem
+ __ZN20GPUDebugFunctionInfoC1EPU22objcproto11MTLFunction11objc_object15MTLFunctionTypeP8NSString
+ __ZN24resolvedSharedPacketDataC2EP14ErrorLogPacketP17MTLGPUDebugDeviceP17MTLGPUDebugGPULogRKNSt3__113unordered_mapIjP8NSStringNS6_4hashIjEENS6_8equal_toIjEENS6_9allocatorINS6_4pairIKjS9_EEEEEE
+ __ZN24resolvedSharedPacketDataD2Ev
+ __ZN26AttachmentDescriptorSimpleC1ERK40MTLRenderPassAttachmentDescriptorPrivate14MTLStoreActionm
+ __ZN26AttachmentDescriptorSimpleC1Ev
+ __ZN26AttachmentDescriptorSimpleC2Ev
+ __ZN28GPUDebugBufferDescriptorHeap12createHandleEv
+ __ZN28GPUDebugBufferDescriptorHeap12createHandleEv.cold.1
+ __ZN28GPUDebugBufferDescriptorHeap12createHandleEv.cold.2
+ __ZN30resolvedSharedPacketDataLegacyI19GPUDebugStackPacketE21setPipelineIdentifierEP8NSString
+ __ZN30resolvedSharedPacketDataLegacyI19GPUDebugStackPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
+ __ZN30resolvedSharedPacketDataLegacyI19GPUDebugStackPacketED2Ev
+ __ZN30resolvedSharedPacketDataLegacyI23GPUDebugBadAccessPacketE21setPipelineIdentifierEP8NSString
+ __ZN30resolvedSharedPacketDataLegacyI23GPUDebugBadAccessPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
+ __ZN30resolvedSharedPacketDataLegacyI23GPUDebugBadAccessPacketED2Ev
+ __ZN30resolvedSharedPacketDataLegacyI24GPUDebugBadTexturePacketE21setPipelineIdentifierEP8NSString
+ __ZN30resolvedSharedPacketDataLegacyI24GPUDebugBadTexturePacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
+ __ZN30resolvedSharedPacketDataLegacyI24GPUDebugBadTexturePacketED2Ev
+ __ZN30resolvedSharedPacketDataLegacyI26GPUDebugFunctionTrapPacketE21setPipelineIdentifierEP8NSString
+ __ZN30resolvedSharedPacketDataLegacyI26GPUDebugFunctionTrapPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
+ __ZN30resolvedSharedPacketDataLegacyI26GPUDebugFunctionTrapPacketED2Ev
+ __ZN30resolvedSharedPacketDataLegacyI35GPUDebugAccelerationStructurePacketE21setPipelineIdentifierEP8NSString
+ __ZN30resolvedSharedPacketDataLegacyI35GPUDebugAccelerationStructurePacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
+ __ZN30resolvedSharedPacketDataLegacyI35GPUDebugAccelerationStructurePacketED2Ev
+ __ZNK16BufferUsageTable8getUsageEP17MTLGPUDebugBuffer
+ __ZNK16TextureTypeTable7getTypeEy
+ __ZNK17TextureUsageTable8getUsageEP18MTLGPUDebugTexture
+ __ZNK26AttachmentDescriptorSimple6hash_tclERKS_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findIjEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne200100EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrI29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI29LegacySVArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29LegacySVArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImN12_GLOBAL__N_120EncoderResourceUsageEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B8ne200100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS3_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_prepareB8ne200100EmRS3_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE11__do_rehashILb0EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE14__assign_multiINS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEEEEvT_SN_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE15__emplace_multiIJRKNS_4pairIKjS3_EEEEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSK_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIjJRKNS_4pairIKjS3_EEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIjJRjRS3_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE26__node_handle_merge_uniqueB8ne200100ISF_EEvRT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE27__node_insert_multi_performEPNS_11__hash_nodeIS4_PvEEPNS_16__hash_node_baseISJ_EE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE27__node_insert_multi_prepareEmRS4_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne200100EmRS4_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb0EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP8NSStringEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImN12_GLOBAL__N_120EncoderResourceUsageEEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS4_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherImS4_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne200100EmRS4_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne200100EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne200100EmRS4_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE14__erase_uniqueIyEEmRKT_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE25__emplace_unique_key_argsIyJRKyEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIyPvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIyPvEEEERKT_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIyPvEEEE
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIyPvEEEE
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEED2Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__113unordered_mapIPU24objcproto13MTLAllocation11objc_objectN12_GLOBAL__N_154_MTLToolsResidencySetInternalCommittedAllocationsTable24CommittedAllocationEntryENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S5_EEEEE4findB8ne200100ERSC_
+ __ZNSt3__113unordered_mapIjP8NSStringNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjS2_EEEEEC2ERKSC_
+ __ZNSt3__113unordered_mapImN12_GLOBAL__N_120EncoderResourceUsageENS_4hashImEENS_8equal_toImEENS_9allocatorINS_4pairIKmS2_EEEEE5clearB8ne200100Ev
+ __ZNSt3__113unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEC2ERKS7_
+ __ZNSt3__114__split_bufferIPP11objc_objectNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPP11objc_objectNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPP11objc_objectNS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPP11objc_objectRNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPP11objc_objectRNS_9allocatorIS3_EEE13emplace_frontIJRS3_EEEvDpOT_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ44-[MTLGPUDebugDevice instrumentationHeapInit]E3$_1EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZL23instrumentationHeapInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI11MTLViewportEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI11MetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI13MTLResourceIDEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI14MTLScissorRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI19LegacySVMetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI20MTL4DebugBindingInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI9MemberRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN14HeapUsageTable19HeapUsageTableEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIP6NSDatamEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIPKc24MTLShaderValidationStateEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIPKc26MTLLegacySVValidationStateEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIPKcN14MTLBoundsCheck8FailModeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIj14MTLTextureTypeEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP15MTLStructMemberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP16MTLDebugLocationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP17MTLGPUDebugBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP17MTLLegacySVBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP29GPUDebugRetainedReportingDataEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU17objcproto7MTLHeap11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU21objcproto10MTLTexture11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU22objcproto11MTLResource11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU24objcproto13MTLAllocation11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU26objcproto15MTLResidencySet11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU26objcproto15MTLSamplerState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU28objcproto17MTL4CommandBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU28objcproto17MTLFunctionHandle11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU30objcproto19MTLGPUDebugViewable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU33objcproto22MTLRenderPipelineState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU34objcproto23MTLVisibleFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne200100EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26MTLTelemetryStatisticUIRecEEPvEEEEEclB8ne200100EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPKcEEPvEEEEEclB8ne200100EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__126__throw_bad_variant_accessB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__15dequeIP11objc_objectNS_9allocatorIS2_EEED2B8ne200100Ev
+ __ZNSt3__16__treeIjNS_4lessIjEENS_9allocatorIjEEE25__emplace_unique_key_argsIjJRjEEENS_4pairINS_15__tree_iteratorIjPNS_11__tree_nodeIjPvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSA_SA_
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE25__emplace_unique_key_argsImJRmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE7destroyEPNS_11__tree_nodeImPvEE
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE7reserveEm
+ __ZNSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13MTLResourceIDNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI13MTLResourceIDNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13MTLResourceIDNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE7reserveEm
+ __ZNSt3__16vectorI19LegacySVMetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI20MTL4DebugBindingInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI20MTL4DebugBindingInfoNS_9allocatorIS1_EEE6resizeEmRKS1_
+ __ZNSt3__16vectorI20MTL4DebugBindingInfoNS_9allocatorIS1_EEE8__appendEmRKS1_
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN12_GLOBAL__N_112_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN12_GLOBAL__N_117ReportBufferEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN14HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIP6NSDatamEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPKc24MTLShaderValidationStateEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4pairIPKc24MTLShaderValidationStateEENS_9allocatorIS5_EEE16__init_with_sizeB8ne200100IPKS5_SB_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIPKc24MTLShaderValidationStateEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPKc26MTLLegacySVValidationStateEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4pairIPKc26MTLLegacySVValidationStateEENS_9allocatorIS5_EEE16__init_with_sizeB8ne200100IPKS5_SB_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIPKc26MTLLegacySVValidationStateEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPKcN14MTLBoundsCheck8FailModeEEENS_9allocatorIS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4pairIPKcN14MTLBoundsCheck8FailModeEEENS_9allocatorIS6_EEE16__init_with_sizeB8ne200100IPKS6_SC_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIPKcN14MTLBoundsCheck8FailModeEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIj14MTLTextureTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP15MTLStructMemberNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP17MTLGPUDebugBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP17MTLLegacySVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP29GPUDebugRetainedReportingDataNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU28objcproto17MTL4CommandBuffer11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU28objcproto17MTL4CommandBuffer11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU28objcproto17MTL4CommandBuffer11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU30objcproto19MTLGPUDebugViewable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU30objcproto19MTLGPUDebugViewable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU30objcproto19MTLGPUDebugViewable11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectENS_9allocatorIS4_EEE9push_backB8ne200100ERKS4_
+ __ZNSt3__16vectorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB8ne200100IPKmS6_EEvT_T0_m
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B8ne200100Em
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100EOy
+ __ZNSt3__17getlineB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZZ56_MTLDebugValidateRenderPassDescriptorAndTrackAttachmentsE50is_dyld_program_sdk_at_least_fall_2025_os_versions
+ ___100-[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___101-[MTL4DebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]_block_invoke
+ ___101-[MTL4ToolsCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]_block_invoke
+ ___104-[MTL4GPUDebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]_block_invoke
+ ___105-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:dynamicLinkingDescriptor:device:]_block_invoke
+ ___121-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___121-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___122-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___122-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___124-[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___125-[MTL4GPUDebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___45-[MTL4ToolsCompiler newDynamicLibrary:error:]_block_invoke
+ ___50-[MTL4GPUDebugCommandQueue _commit:count:options:]_block_invoke
+ ___52-[MTL4ToolsCompiler newDynamicLibraryWithURL:error:]_block_invoke
+ ___57-[MTL4DebugCompiler newDynamicLibrary:completionHandler:]_block_invoke
+ ___57-[MTL4ToolsCompiler newDynamicLibrary:completionHandler:]_block_invoke
+ ___58-[MTLGPUDebugComputePipelineState functionHandleWithName:]_block_invoke
+ ___60-[MTL4GPUDebugCompiler newDynamicLibrary:completionHandler:]_block_invoke
+ ___60-[MTL4ToolsCompiler newDynamicLibraryWithURL:options:error:]_block_invoke
+ ___63-[MTLGPUDebugRenderPipelineState functionHandleWithName:stage:]_block_invoke
+ ___64-[MTL4DebugCompiler newDynamicLibraryWithURL:completionHandler:]_block_invoke
+ ___64-[MTL4DebugCompiler newLibraryWithDescriptor:completionHandler:]_block_invoke
+ ___64-[MTL4ToolsCommandQueue commit:count:options:preprocessHandler:]_block_invoke
+ ___64-[MTL4ToolsCompiler newDynamicLibraryWithURL:completionHandler:]_block_invoke
+ ___64-[MTL4ToolsCompiler newLibraryWithDescriptor:completionHandler:]_block_invoke
+ ___67-[MTL4GPUDebugCompiler newDynamicLibraryWithURL:completionHandler:]_block_invoke
+ ___67-[MTL4GPUDebugCompiler newLibraryWithDescriptor:completionHandler:]_block_invoke
+ ___68-[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:]_block_invoke
+ ___68-[MTLGPUDebugComputePipelineState functionHandleWithBinaryFunction:]_block_invoke
+ ___72-[MTL4DebugCompiler newDynamicLibraryWithURL:options:completionHandler:]_block_invoke
+ ___72-[MTL4ToolsCompiler newDynamicLibraryWithURL:options:completionHandler:]_block_invoke
+ ___73-[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:stage:]_block_invoke
+ ___73-[MTLGPUDebugRenderPipelineState functionHandleWithBinaryFunction:stage:]_block_invoke
+ ___83-[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:binaryFunction:]_block_invoke
+ ___85-[MTL4DebugCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:]_block_invoke
+ ___85-[MTL4ToolsCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:]_block_invoke
+ ___88-[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:binaryFunction:stage:]_block_invoke
+ ___91-[MTL4DebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___91-[MTL4ToolsCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___94-[MTL4GPUDebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___95-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:originalObject:descriptor:device:]_block_invoke
+ ___96-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___96-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___97-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___97-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___99-[MTL4GPUDebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_copy_.9
+ ___Block_byref_object_dispose_
+ ___Block_byref_object_dispose_.10
+ ___MTLFunctionHandleToToolsFunctionHandleWithBinaryFunction_block_invoke
+ ___MTLFunctionHandleToToolsFunctionHandleWithDevice_block_invoke
+ ____ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDeviceP22MTL4PipelineDescriptorS2__block_invoke
+ ____ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDeviceP22MTL4PipelineDescriptorS2__block_invoke_3
+ ____ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDeviceP22MTL4PipelineDescriptorS2__block_invoke_4
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_10
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_11
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_12
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_2
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_3
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_4
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_5
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_6
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_7
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_8
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3_R16TextureTypeTableS5_S5_S5__block_invoke_9
+ ____ZZL18WrapDynamicLibraryIZ45-[MTL4GPUDebugCompiler wrapDynamicLibraries:]E3$_0EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ45-[MTLGPUDebugDevice newDynamicLibrary:error:]E4$_17EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ48-[MTL4GPUDebugCompiler newDynamicLibrary:error:]E3$_2EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ55-[MTL4GPUDebugCompiler newDynamicLibraryWithURL:error:]E3$_3EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ59-[MTLGPUDebugDevice newDynamicLibraryWithDescriptor:error:]E4$_16EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ60-[MTLGPUDebugDevice newDynamicLibraryWithURL:options:error:]E4$_15EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ63-[MTLGPUDebugDevice newDynamicLibrary:computeDescriptor:error:]E4$_18EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ____ZZL18WrapDynamicLibraryIZ83-[MTLGPUDebugDevice loadDynamicLibrariesForFunction:insertLibraries:options:error:]E4$_19EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
+ ___assign_helper_atomic_property_
+ ___assign_helper_atomic_property_.6
+ ___block_descriptor_48_e8_32o40b_e41_v24?0"<MTLDynamicLibrary>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e42_v24?0"<MTL4BinaryFunction>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e56_v24?0"<MTL4MachineLearningPipelineState>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32o40o_e11_v24?0Q8Q16ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e29_"MTLToolsFunctionHandle"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e30_v16?0"<MTL4CommitFeedback>"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e34_v24?0"<MTLLibrary>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32o40o48b_e42_v24?0"<MTL4BinaryFunction>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32o40o_e29_"MTLToolsFunctionHandle"8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e30_v16?0"<MTL4CommitFeedback>"8lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32o40o48o56b_e42_v24?0"<MTL4BinaryFunction>"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32o40o48o56b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48o56b_e56_v24?0"<MTL4MachineLearningPipelineState>"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48o56o_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_80_e8_32o40o48o56o64o72b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32o40o48o56o64o72b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_80_e8_32o40o48o56o64o72b_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32o40o48o56o64o72b_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_88_e8_32o40o48o56o64o72o80b_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1657
+ ___copy_helper_atomic_property_
+ ___copy_helper_atomic_property_.5
+ ___cxa_guard_abort
+ __validateTextureView
+ __validateTextureView.cold.1
+ _checkMTL4AccelerationStructureDescriptor
+ _dyld_program_sdk_at_least
+ _hasUnspecializedProperties
+ _objc_copyCppObjectAtomic
+ _objc_msgSend$SVBindingTableVertexKernelBuffer
+ _objc_msgSend$_Init
+ _objc_msgSend$__waitUntilCompletedAsync:
+ _objc_msgSend$__waitUntilScheduledAsync:
+ _objc_msgSend$_addUsedBuffer:
+ _objc_msgSend$_checkReportBuffers:outputArray:encoderLabels:
+ _objc_msgSend$_clearSuspendResumeRenderPassInfo
+ _objc_msgSend$_commit:count:options:
+ _objc_msgSend$_decodeReportLogState:
+ _objc_msgSend$_decodeReportLogState:outputArray:encoderLabels:
+ _objc_msgSend$_initConstantsBuffer:
+ _objc_msgSend$_internalBindingTableForStage:
+ _objc_msgSend$_modifyComputeDynamicLinkingDescriptor:
+ _objc_msgSend$_modifyComputePipelineDescriptor:
+ _objc_msgSend$_modifyComputePipelineDescriptor:dynamicLinkingDescriptor:
+ _objc_msgSend$_modifyDynamicLinkingDescriptor:
+ _objc_msgSend$_modifyRenderDynamicLinkingDescriptor:
+ _objc_msgSend$_modifyRenderPipelineDescriptor:
+ _objc_msgSend$_modifyRenderPipelineDescriptor:dynamicLinkingDescriptor:
+ _objc_msgSend$_resetEncoder
+ _objc_msgSend$_resetEncoderWithDescriptor:
+ _objc_msgSend$_resetRenderPassAttachmentTracking
+ _objc_msgSend$_setInternalBindingTableForStage:stage:
+ _objc_msgSend$_setInternalBindingTables:type:
+ _objc_msgSend$_updateCachedMTL4MeshPipelineState
+ _objc_msgSend$_updateCachedMTL4PipelineState
+ _objc_msgSend$_updateCachedMTL4TilePipelineState
+ _objc_msgSend$_updateEncoderStateAfterDispatch
+ _objc_msgSend$_updateEncoderStateAfterDraw
+ _objc_msgSend$_validateComputeFunctionArguments:
+ _objc_msgSend$_validateComputeFunctionBuiltinArguments:threadsPerThreadgroup:threadgroupsPerGrid:
+ _objc_msgSend$_validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:
+ _objc_msgSend$_validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:
+ _objc_msgSend$_validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:
+ _objc_msgSend$_validateDispatchThreadsPerTileCommon:threadsPerTile:
+ _objc_msgSend$_validateDrawCommon:primitiveType:instanceCount:
+ _objc_msgSend$_validateFillTextureCommon:texture:level:slice:region:
+ _objc_msgSend$_validateFramebufferCompatibility:pipelineState:
+ _objc_msgSend$_validateFunctionArguments:stages:
+ _objc_msgSend$_validateIndexedDrawCommon:indexBuffer:indexType:indexBufferLength:
+ _objc_msgSend$_validateLBRT:
+ _objc_msgSend$_validateMeshDrawCommon:
+ _objc_msgSend$_validateThreadsPerObjectThreadgroup:threadsPerMeshThreadgroup:context:
+ _objc_msgSend$_validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:
+ _objc_msgSend$addBinaryFunctionWithDescriptor:
+ _objc_msgSend$addFeedbackHandler:
+ _objc_msgSend$addPipelineWithDescriptor:
+ _objc_msgSend$addResetHandler:
+ _objc_msgSend$addUsedBuffer:
+ _objc_msgSend$addUsedPipelineState:
+ _objc_msgSend$addView:
+ _objc_msgSend$addedResidencySets
+ _objc_msgSend$aggregatedEncoderMask
+ _objc_msgSend$alphaBlendOperation
+ _objc_msgSend$alphaToCoverageState
+ _objc_msgSend$alphaToOneState
+ _objc_msgSend$applyResidencySets:
+ _objc_msgSend$attachCommandBuffer:
+ _objc_msgSend$attachmentSet
+ _objc_msgSend$barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:
+ _objc_msgSend$barrierAfterQueueStages:beforeStages:
+ _objc_msgSend$barrierAfterQueueStages:beforeStages:visibilityOptions:
+ _objc_msgSend$barrierAfterStages:beforeQueueStages:visibilityOptions:
+ _objc_msgSend$baseResourceID
+ _objc_msgSend$beginCommandBufferWithAllocator:
+ _objc_msgSend$beginCommandBufferWithAllocator:options:
+ _objc_msgSend$beginningEncoder:type:
+ _objc_msgSend$binaryLinkedFunctions
+ _objc_msgSend$bindInternalBuffer:index:
+ _objc_msgSend$bindInternalBufferForStage:index:stage:
+ _objc_msgSend$bindInternalBufferForStage:index:stage:offset:
+ _objc_msgSend$bindInternalBufferWithOffset:offset:index:
+ _objc_msgSend$bindInternalValue:index:
+ _objc_msgSend$bindInternalValueForStage:index:stage:
+ _objc_msgSend$blendingState
+ _objc_msgSend$bufferBindingAtIndex:
+ _objc_msgSend$bufferBindingCount
+ _objc_msgSend$buildAccelerationStructure:descriptor:scratchBuffer:
+ _objc_msgSend$cancel
+ _objc_msgSend$cbAllocations
+ _objc_msgSend$checkAndGetMessage:logBuffer:message:
+ _objc_msgSend$colorAttachmentMappingState
+ _objc_msgSend$commandAllocator
+ _objc_msgSend$commandBatchIdOffset
+ _objc_msgSend$commandBatchIdRangeMin:max:
+ _objc_msgSend$commit:count:
+ _objc_msgSend$commit:count:options:
+ _objc_msgSend$commitFeedbackDispatch
+ _objc_msgSend$computeCommandEncoderWithSubstreamCount:
+ _objc_msgSend$computeFunctionDescriptor
+ _objc_msgSend$containsAllocation:
+ _objc_msgSend$copyBufferMappingsFromBuffer:toBuffer:operations:count:
+ _objc_msgSend$copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:
+ _objc_msgSend$copyFromTensor:sourceSlice:toTensor:destinationSlice:
+ _objc_msgSend$copyResourceStatesFromPool:sourceRange:destinationLocation:
+ _objc_msgSend$copyResourceViewsFromPool:sourceRange:destinationIndex:
+ _objc_msgSend$copyTextureMappingsFromTexture:toTexture:operations:count:
+ _objc_msgSend$createChildrenWrappersBufferWithInstanceDescriptorBufferRange:maxInstanceCount:instanceCountBufferRange:instanceDescriptorStride:instanceDescriptorType:
+ _objc_msgSend$currentCommandBuffer
+ _objc_msgSend$currentState
+ _objc_msgSend$curveEndCaps
+ _objc_msgSend$defaultCompilerProcessesCount
+ _objc_msgSend$deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:
+ _objc_msgSend$deserializePrimitiveAccelerationStructure:fromBuffer:
+ _objc_msgSend$destinationAlphaBlendFactor
+ _objc_msgSend$destinationBinaryArchive
+ _objc_msgSend$destinationRGBBlendFactor
+ _objc_msgSend$detachCommandBuffer
+ _objc_msgSend$dimensions
+ _objc_msgSend$dispatchNetworkWithIntermediatesHeap:
+ _objc_msgSend$dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:
+ _objc_msgSend$dispatchThreadsWithIndirectBuffer:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:
+ _objc_msgSend$drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:
+ _objc_msgSend$drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:
+ _objc_msgSend$drawPrimitives:indirectBuffer:
+ _objc_msgSend$enableBoundsChecking
+ _objc_msgSend$enableResourceUsageValidation
+ _objc_msgSend$enableStackOverflow
+ _objc_msgSend$enableTextureChecks
+ _objc_msgSend$enableThreadgroupMemoryChecks
+ _objc_msgSend$encodeCopyAndUnwrapChildrenWithInstanceDescriptorBufferRange:dstInstanceDescriptorBufferRange:instanceDescriptorStride:instanceIDOffset:maxInstanceCount:
+ _objc_msgSend$encodeEndDoWhile:comparison:referenceValue:
+ _objc_msgSend$encodeStartIf:comparison:referenceValue:
+ _objc_msgSend$encodeStartWhile:comparison:referenceValue:
+ _objc_msgSend$encodeUnwrapWithIASDescriptor:
+ _objc_msgSend$encodeUnwrapWithIndirectIASDescriptor:
+ _objc_msgSend$encoderLabels
+ _objc_msgSend$endCommandBuffer
+ _objc_msgSend$endEncodingPreamble
+ _objc_msgSend$endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:
+ _objc_msgSend$endEventValue
+ _objc_msgSend$entryCount
+ _objc_msgSend$evaluateSloppyUsage:
+ _objc_msgSend$evaluateUsage:
+ _objc_msgSend$executeBlocksWithCommitFeedback:
+ _objc_msgSend$executeCommandsInBuffer:indirectBuffer:
+ _objc_msgSend$extentAtDimensionIndex:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fillWithByte:
+ _objc_msgSend$fragmentAdditionalBinaryFunctionResourceIndices
+ _objc_msgSend$fragmentBindings
+ _objc_msgSend$fragmentFunctionDescriptor
+ _objc_msgSend$fragmentLinkingDescriptor
+ _objc_msgSend$fragmentStaticLinkingDescriptor
+ _objc_msgSend$functionConstants
+ _objc_msgSend$functionDescriptor
+ _objc_msgSend$functionDescriptors
+ _objc_msgSend$functionGraph
+ _objc_msgSend$functionHandleToDebugFunctionHandle:
+ _objc_msgSend$functionHandleToDebugFunctionHandle:binaryFunction:
+ _objc_msgSend$functionHandleToDebugFunctionHandle:binaryFunction:stage:
+ _objc_msgSend$functionHandleToDebugFunctionHandle:stage:
+ _objc_msgSend$functionHandleWithBinaryFunction:
+ _objc_msgSend$functionHandleWithBinaryFunction:stage:
+ _objc_msgSend$functionHandleWithFunction:resourceIndex:
+ _objc_msgSend$functionHandleWithName:
+ _objc_msgSend$functionHandleWithName:stage:
+ _objc_msgSend$functionReflectionWithFunctionDescriptor:
+ _objc_msgSend$functionReflectionWithFunctionDescriptor:stage:
+ _objc_msgSend$getActiveViews
+ _objc_msgSend$getBufferBindings:bindingCount:
+ _objc_msgSend$getBytes:strides:fromSlice:
+ _objc_msgSend$getBytes:strides:fromSliceOrigin:sliceDimensions:
+ _objc_msgSend$getIntersectionFunctionSignature
+ _objc_msgSend$getPhysicalIndexForLogicalIndex:
+ _objc_msgSend$getPrivateDataAndOffset:privateDataOffset:
+ _objc_msgSend$getRetainedData
+ _objc_msgSend$getTextureBindings:bindingCount:
+ _objc_msgSend$getViewableAt:
+ _objc_msgSend$hasEndEncoding
+ _objc_msgSend$hasMetal4Descriptor
+ _objc_msgSend$hasUnspecializedProperties:
+ _objc_msgSend$incrementCurrentEncoderID
+ _objc_msgSend$initCommon
+ _objc_msgSend$initImageData:
+ _objc_msgSend$initReportBufferInPrivateData:
+ _objc_msgSend$initWithArgumentTable:device:descriptor:
+ _objc_msgSend$initWithBaseObject:buffer:
+ _objc_msgSend$initWithBaseObject:device:commandBuffer:encoderStageMask:
+ _objc_msgSend$initWithBaseObject:parent:binaryFunction:
+ _objc_msgSend$initWithBaseObject:parent:binaryFunction:stage:
+ _objc_msgSend$initWithBaseObject:parent:stage:
+ _objc_msgSend$initWithBaseObject:parentTensor:
+ _objc_msgSend$initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:descriptor:
+ _objc_msgSend$initWithBaseTexture:device:buffer:offset:bytesPerRow:descriptor:
+ _objc_msgSend$initWithBaseTexture:device:placementSparsePageSize:
+ _objc_msgSend$initWithBinaryFunction:debugInstrumentationData:device:
+ _objc_msgSend$initWithBuffer:device:options:placementSparsePageSize:
+ _objc_msgSend$initWithCommandBuffer:device:
+ _objc_msgSend$initWithCommandEncoder:commandBuffer:
+ _objc_msgSend$initWithCompiler:
+ _objc_msgSend$initWithComputeCommandEncoder:commandBuffer:
+ _objc_msgSend$initWithComputeCommandEncoder:commandBuffer:encoderID:
+ _objc_msgSend$initWithComputePipelineState:binaryFunctions:withState:device:
+ _objc_msgSend$initWithComputePipelineState:descriptor:device:
+ _objc_msgSend$initWithComputePipelineState:descriptor:dynamicLinkingDescriptor:device:
+ _objc_msgSend$initWithComputePipelineState:parent:mtl4Descriptor:
+ _objc_msgSend$initWithComputePipelineState:reflection:parent:mtl4Descriptor:
+ _objc_msgSend$initWithCounterHeap:device:
+ _objc_msgSend$initWithFunctionHandle:computePipelineState:
+ _objc_msgSend$initWithFunctionHandle:renderPipelineState:stage:
+ _objc_msgSend$initWithFunctionName:functionType:debugInstrumentationData:device:
+ _objc_msgSend$initWithHeap:device:maxCompatiblePlacementSparsePageSize:
+ _objc_msgSend$initWithMLCommandEncoder:commandBuffer:
+ _objc_msgSend$initWithMLPipelineState:parent:descriptor:
+ _objc_msgSend$initWithRenderCommandEncoder:commandBuffer:descriptor:
+ _objc_msgSend$initWithRenderPipelineState:descriptor:device:
+ _objc_msgSend$initWithRenderPipelineState:descriptor:dynamicLinkingDescriptor:device:
+ _objc_msgSend$initWithRenderPipelineState:originalObject:descriptor:device:
+ _objc_msgSend$initWithRenderPipelineState:parent:mtl4Descriptor:
+ _objc_msgSend$initWithRenderPipelineState:reflection:parent:mtl4Descriptor:
+ _objc_msgSend$initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:
+ _objc_msgSend$initWithTextureViewPool:device:
+ _objc_msgSend$initializeBindings
+ _objc_msgSend$initializedTables
+ _objc_msgSend$instrumentationHeapInit
+ _objc_msgSend$intermediatesHeapSize
+ _objc_msgSend$internalValueAtIndex:
+ _objc_msgSend$intersectionFunctionSignature
+ _objc_msgSend$invalidateCounterRange:
+ _objc_msgSend$invokeLogHandlers:category:level:message:
+ _objc_msgSend$isAllocatorGenerationValid
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isTensorViewableWithReshapedDescriptor:
+ _objc_msgSend$isUsed
+ _objc_msgSend$lastCommittedCommandBufferGeneration
+ _objc_msgSend$levels
+ _objc_msgSend$llvmVersion
+ _objc_msgSend$lock
+ _objc_msgSend$lookupArchives
+ _objc_msgSend$machineLearningCommandEncoder
+ _objc_msgSend$machineLearningFunctionDescriptor
+ _objc_msgSend$maxBufferBindCount
+ _objc_msgSend$maxCommands
+ _objc_msgSend$maxCompatiblePlacementSparsePageSize
+ _objc_msgSend$maxSamplerStateBindCount
+ _objc_msgSend$maxTextureBindCount
+ _objc_msgSend$maximumCompilerProcessesCount
+ _objc_msgSend$meshAdditionalBinaryFunctionResourceIndices
+ _objc_msgSend$meshBindings
+ _objc_msgSend$meshFunctionDescriptor
+ _objc_msgSend$meshLinkingDescriptor
+ _objc_msgSend$meshStaticLinkingDescriptor
+ _objc_msgSend$mtl4Descriptor
+ _objc_msgSend$mtl4MeshDescriptor
+ _objc_msgSend$mtl4TileDescriptor
+ _objc_msgSend$mtlTensorFromGpuResourceID:
+ _objc_msgSend$newArchiveReplyForPipelineFunctionWithDescriptor:functionType:functionId:
+ _objc_msgSend$newArchiveWithURL:error:
+ _objc_msgSend$newArgumentTableWithDescriptor:error:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:error:
+ _objc_msgSend$newBufferWithLength:options:placementSparsePageSize:
+ _objc_msgSend$newCommandAllocator
+ _objc_msgSend$newCommandAllocatorWithDescriptor:error:
+ _objc_msgSend$newCommandBuffer
+ _objc_msgSend$newCompilerWithDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:
+ _objc_msgSend$newComputePipelineStateWithBinaryFunctions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithFunctionName:
+ _objc_msgSend$newComputePipelineStateWithName:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithName:error:
+ _objc_msgSend$newCounterHeapWithDescriptor:error:
+ _objc_msgSend$newDynamicLibrary:completionHandler:
+ _objc_msgSend$newDynamicLibraryWithURL:completionHandler:
+ _objc_msgSend$newDynamicLibraryWithURL:options:completionHandler:
+ _objc_msgSend$newLibraryWithDescriptor:completionHandler:
+ _objc_msgSend$newLibraryWithDescriptor:error:
+ _objc_msgSend$newLibraryWithMPSGraphPackageURL:name:error:
+ _objc_msgSend$newMTL4CommandQueue
+ _objc_msgSend$newMTL4CommandQueueWithDescriptor:error:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:completionHandler:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:error:
+ _objc_msgSend$newPipelineDataSetSerializerWithDescriptor:
+ _objc_msgSend$newRenderPipelineDescriptorForSpecialization
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:
+ _objc_msgSend$newRenderPipelineStateWithBinaryFunctions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithName:error:
+ _objc_msgSend$newSpecializedMTL4PipelineDescriptor:descriptor:
+ _objc_msgSend$newTensorViewWithReshapedDescriptor:error:
+ _objc_msgSend$newTensorViewWithSlice:error:
+ _objc_msgSend$newTensorWithDescriptor:error:
+ _objc_msgSend$newTensorWithDescriptor:offset:error:
+ _objc_msgSend$newTextureViewPoolWithDescriptor:error:
+ _objc_msgSend$newTextureViewWithDescriptor:
+ _objc_msgSend$newUnwrappedMTL4BinaryFunctionDescriptor:
+ _objc_msgSend$newUnwrappedMTL4CompilerTaskOptions:
+ _objc_msgSend$newUnwrappedMTL4ComputeDynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTL4ComputePipelineDescriptor:
+ _objc_msgSend$newUnwrappedMTL4ComputePipelineDescriptor:dynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTL4FunctionDescriptor:
+ _objc_msgSend$newUnwrappedMTL4PipelineDescriptor:
+ _objc_msgSend$newUnwrappedMTL4PipelineStageDynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTL4RenderDynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTL4RenderPipelineBinaryFunctionsDescriptor:
+ _objc_msgSend$newUnwrappedMTL4RenderPipelineDescriptor:
+ _objc_msgSend$newUnwrappedMTL4RenderPipelineDescriptor:dynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTL4RenderPipelineDynamicLinkingDescriptor:
+ _objc_msgSend$newUnwrappedMTLRelocations:
+ _objc_msgSend$newUnwrappedStaticLinkingDescriptor:
+ _objc_msgSend$numDispatches
+ _objc_msgSend$objectAdditionalBinaryFunctionResourceIndices
+ _objc_msgSend$objectBindings
+ _objc_msgSend$objectFunctionDescriptor
+ _objc_msgSend$objectLinkingDescriptor
+ _objc_msgSend$objectStaticLinkingDescriptor
+ _objc_msgSend$onCurrentEncoderEnded
+ _objc_msgSend$optimizedBytecode
+ _objc_msgSend$pipelineDataSetSerializer
+ _objc_msgSend$placementSparsePageSize
+ _objc_msgSend$populateDefaultLoggerCache:logger:
+ _objc_msgSend$preCommit:
+ _objc_msgSend$prepareInsertLibraries:
+ _objc_msgSend$privateData
+ _objc_msgSend$privateDataOffset
+ _objc_msgSend$privateFunctionDescriptors
+ _objc_msgSend$queryTimestampFrequency
+ _objc_msgSend$rank
+ _objc_msgSend$refitAccelerationStructure:descriptor:destination:scratchBuffer:
+ _objc_msgSend$refitAccelerationStructure:descriptor:destination:scratchBuffer:options:
+ _objc_msgSend$reflectionForFunctionDescriptor:
+ _objc_msgSend$reflectionForFunctionWithName:
+ _objc_msgSend$removeView:
+ _objc_msgSend$renderCommandEncoderWithDescriptor:options:
+ _objc_msgSend$replaceSlice:withBytes:strides:
+ _objc_msgSend$replaceSliceOrigin:sliceDimensions:withBytes:strides:
+ _objc_msgSend$requiredThreadsPerMeshThreadgroup
+ _objc_msgSend$requiredThreadsPerObjectThreadgroup
+ _objc_msgSend$requiredThreadsPerThreadgroup
+ _objc_msgSend$requiredThreadsPerTileThreadgroup
+ _objc_msgSend$requiresLegacyCompilerProcessesCount
+ _objc_msgSend$resetEncoderState
+ _objc_msgSend$residencySetsLock
+ _objc_msgSend$resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:
+ _objc_msgSend$resourceBlobForByteCodeSignature:resourceName:error:
+ _objc_msgSend$resourceViewCount
+ _objc_msgSend$rgbBlendOperation
+ _objc_msgSend$runWithInputsArray:resultsArray:intermediateOperations:
+ _objc_msgSend$sampledComputeCommandEncoder:capacity:
+ _objc_msgSend$samplerBindingAtIndex:
+ _objc_msgSend$samplerBindingCount
+ _objc_msgSend$serializeAsArchiveAndFlushToURL:error:
+ _objc_msgSend$serializeAsPipelinesScriptWithError:
+ _objc_msgSend$serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:
+ _objc_msgSend$serializePrimitiveAccelerationStructure:toBuffer:
+ _objc_msgSend$setAddress:atIndex:
+ _objc_msgSend$setAddress:attributeStride:atIndex:
+ _objc_msgSend$setAlphaBlendOperation:
+ _objc_msgSend$setAlphaToCoverageState:
+ _objc_msgSend$setAlphaToOneState:
+ _objc_msgSend$setArgumentTable:
+ _objc_msgSend$setArgumentTable:atStages:
+ _objc_msgSend$setBinaryLinkedFunctions:
+ _objc_msgSend$setBlendingState:
+ _objc_msgSend$setBufferSize:
+ _objc_msgSend$setCanEndEncoding:
+ _objc_msgSend$setColorAttachmentMap:
+ _objc_msgSend$setCommitFeedbackDispatch:
+ _objc_msgSend$setComputeFunctionDescriptor:
+ _objc_msgSend$setComputePipeline:
+ _objc_msgSend$setContents:
+ _objc_msgSend$setCurrentState:
+ _objc_msgSend$setDebugInstrumentationDataForStage:stage:
+ _objc_msgSend$setDestinationAlphaBlendFactor:
+ _objc_msgSend$setDestinationRGBBlendFactor:
+ _objc_msgSend$setEnableBoundsChecking:
+ _objc_msgSend$setEnableResourceUsageValidation:
+ _objc_msgSend$setEnableStackOverflow:
+ _objc_msgSend$setEnableTextureChecks:
+ _objc_msgSend$setEnableThreadgroupMemoryChecks:
+ _objc_msgSend$setEncoderLabelForIndex:encoderIndex:
+ _objc_msgSend$setFragmentAdditionalBinaryFunctionResourceIndices:
+ _objc_msgSend$setFragmentFunctionDescriptor:
+ _objc_msgSend$setFragmentStaticLinkingDescriptor:
+ _objc_msgSend$setFunctionDescriptor:
+ _objc_msgSend$setFunctionDescriptors:
+ _objc_msgSend$setFunctionType:
+ _objc_msgSend$setInitialCapacity:
+ _objc_msgSend$setInitializeBindings:
+ _objc_msgSend$setInitializedTables:
+ _objc_msgSend$setInternalBindingTable:
+ _objc_msgSend$setInternalBytes:length:atIndex:
+ _objc_msgSend$setInternalBytesForStage:length:atIndex:stage:
+ _objc_msgSend$setLookupArchives:
+ _objc_msgSend$setMachineLearningFunctionDescriptor:
+ _objc_msgSend$setMaxBufferBindCount:
+ _objc_msgSend$setMaxMeshBufferBindCount:
+ _objc_msgSend$setMaxObjectBufferBindCount:
+ _objc_msgSend$setMaxToolsDispatchBindings:
+ _objc_msgSend$setMeshAdditionalBinaryFunctionResourceIndices:
+ _objc_msgSend$setMeshFunctionDescriptor:
+ _objc_msgSend$setMeshStaticLinkingDescriptor:
+ _objc_msgSend$setNoCopy:
+ _objc_msgSend$setNumDispatches:
+ _objc_msgSend$setObjectAdditionalBinaryFunctionResourceIndices:
+ _objc_msgSend$setObjectFunctionDescriptor:
+ _objc_msgSend$setObjectStaticLinkingDescriptor:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setPipelineDataSetSerializer:
+ _objc_msgSend$setPipelineState:
+ _objc_msgSend$setPointerTag:
+ _objc_msgSend$setPrivateData:
+ _objc_msgSend$setPrivateDataOffset:
+ _objc_msgSend$setPrivateFunctionDescriptors:
+ _objc_msgSend$setRenderPipeline:
+ _objc_msgSend$setReportBufferInPrivateData:privateDataOffset:logState:
+ _objc_msgSend$setRequiresLegacyCompilerProcessesCount:
+ _objc_msgSend$setResidencyForResource:
+ _objc_msgSend$setResource:atBufferIndex:
+ _objc_msgSend$setRgbBlendOperation:
+ _objc_msgSend$setShaderReflection:
+ _objc_msgSend$setShaderValidation:
+ _objc_msgSend$setSourceAlphaBlendFactor:
+ _objc_msgSend$setSourceRGBBlendFactor:
+ _objc_msgSend$setStaticLinkingDescriptor:
+ _objc_msgSend$setSupportDynamicAttributeStride:
+ _objc_msgSend$setTextureView:atIndex:
+ _objc_msgSend$setTextureView:descriptor:atIndex:
+ _objc_msgSend$setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:
+ _objc_msgSend$setTileAdditionalBinaryFunctionResourceIndices:
+ _objc_msgSend$setTileFunctionDescriptor:
+ _objc_msgSend$setToolsDispatchBufferSPI:atIndex:
+ _objc_msgSend$setToolsDispatchBufferSPI:atIndex:stages:
+ _objc_msgSend$setUpLogState:
+ _objc_msgSend$setUpShaderLoggingPrivateData
+ _objc_msgSend$setUsedForShaderValidation:
+ _objc_msgSend$setVertexAdditionalBinaryFunctionResourceIndices:
+ _objc_msgSend$setVertexFunctionDescriptor:
+ _objc_msgSend$setVertexStaticLinkingDescriptor:
+ _objc_msgSend$setView:resourceID:type:index:
+ _objc_msgSend$shaderReflection
+ _objc_msgSend$shaderValidationConfig
+ _objc_msgSend$shouldMaximizeConcurrentCompilation
+ _objc_msgSend$signalDrawable:
+ _objc_msgSend$signalEvent:value:
+ _objc_msgSend$sizeOfCounterHeapEntry:
+ _objc_msgSend$slices
+ _objc_msgSend$source
+ _objc_msgSend$sourceAlphaBlendFactor
+ _objc_msgSend$sourceRGBBlendFactor
+ _objc_msgSend$sparseBufferTier
+ _objc_msgSend$sparseTextureTier
+ _objc_msgSend$specializedName
+ _objc_msgSend$stages
+ _objc_msgSend$startEventValue
+ _objc_msgSend$staticLinkingDescriptor
+ _objc_msgSend$strides
+ _objc_msgSend$supportAttributeStrides
+ _objc_msgSend$supportBinaryLinking
+ _objc_msgSend$supportColorAttachmentMapping
+ _objc_msgSend$supportFragmentBinaryLinking
+ _objc_msgSend$supportMeshBinaryLinking
+ _objc_msgSend$supportObjectBinaryLinking
+ _objc_msgSend$supportVertexBinaryLinking
+ _objc_msgSend$supportsAIRNTBinaryArchiveFunctionPointers
+ _objc_msgSend$supportsAIRNTBinaryArchiveSpecializedFunctions
+ _objc_msgSend$supportsAIRNTBinaryArchiveStitchedFunctions
+ _objc_msgSend$supportsAtomicWaitNotify
+ _objc_msgSend$supportsCommandQueueBarriers
+ _objc_msgSend$supportsIntersectionFunctionBuffers
+ _objc_msgSend$supportsMTL4CommandAllocator
+ _objc_msgSend$supportsMTL4CommandQueue
+ _objc_msgSend$supportsMTL4Compiler
+ _objc_msgSend$supportsMTL4ComputeCommandEncoder
+ _objc_msgSend$supportsMTL4Counters
+ _objc_msgSend$supportsMTL4LateBoundRenderTargets
+ _objc_msgSend$supportsMTL4PSOSpecialization
+ _objc_msgSend$supportsMTL4PlacementSparse
+ _objc_msgSend$supportsMTL4RenderCommandEncoder
+ _objc_msgSend$supportsMTLTextureViewPools
+ _objc_msgSend$supportsMachineLearningCommandEncoders
+ _objc_msgSend$supportsTensors
+ _objc_msgSend$suspendResumeRenderPassInfo
+ _objc_msgSend$tagType
+ _objc_msgSend$tags
+ _objc_msgSend$tensorSizeAndAlignWithDescriptor:
+ _objc_msgSend$textureBindingAtIndex:
+ _objc_msgSend$textureBindingCount
+ _objc_msgSend$threadsPerCompilerProcess
+ _objc_msgSend$tileAdditionalBinaryFunctionResourceIndices
+ _objc_msgSend$tileFunctionDescriptor
+ _objc_msgSend$tileLinkingDescriptor
+ _objc_msgSend$unlock
+ _objc_msgSend$unwrappedMTL4RenderPassDescriptor:
+ _objc_msgSend$updateBufferMappings:heap:operations:count:
+ _objc_msgSend$updateFence:afterEncoderStages:
+ _objc_msgSend$updateTextureMappings:heap:operations:count:
+ _objc_msgSend$usedPipelineStates
+ _objc_msgSend$usedResidencySets
+ _objc_msgSend$validateBufferAccess:range:resourceSparsePageSize:context:
+ _objc_msgSend$validateCommitCommon:commandBuffers:count:
+ _objc_msgSend$validateFunctionArguments:stage:functionName:argumentTable:boundThreadgroupMemoryArguments:bindings:allowNullBufferBindings:
+ _objc_msgSend$validateHeapAccess:rangeOffset:tileRegions:resourceSparsePageSize:context:
+ _objc_msgSend$validateIsIFBFunction
+ _objc_msgSend$validateRefit:descriptor:destination:scratchBuffer:options:
+ _objc_msgSend$validateTextureAccess:region:mipLevel:slice:context:
+ _objc_msgSend$validationReflection
+ _objc_msgSend$verifyGetBytesReplaceSliceWithContext:strides:slice:
+ _objc_msgSend$vertexAdditionalBinaryFunctionResourceIndices
+ _objc_msgSend$vertexBindings
+ _objc_msgSend$vertexDescriptor
+ _objc_msgSend$vertexFunctionDescriptor
+ _objc_msgSend$vertexLinkingDescriptor
+ _objc_msgSend$vertexStaticLinkingDescriptor
+ _objc_msgSend$visibilityResultType
+ _objc_msgSend$waitForDrawable:
+ _objc_msgSend$waitForEvent:value:
+ _objc_msgSend$waitForEvent:value:timeout:
+ _objc_msgSend$waitForFence:beforeEncoderStages:
+ _objc_msgSend$wrapChildTensor:
+ _objc_msgSend$wrapDynamicLibraries:
+ _objc_msgSend$writeAccelerationStructureSerializationData:toBuffer:
+ _objc_msgSend$writeAccelerationStructureTraversalDepth:toBuffer:
+ _objc_msgSend$writeCompactedAccelerationStructureSize:toBuffer:
+ _objc_msgSend$writeDeserializedAccelerationStructureSize:toBuffer:
+ _objc_msgSend$writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:
+ _objc_msgSend$writeSerializedAccelerationStructureSize:toBuffer:
+ _objc_msgSend$writeTimestampIntoHeap:atIndex:
+ _objc_msgSend$writeTimestampWithGranularity:afterStage:intoHeap:atIndex:
+ _objc_msgSend$writeTimestampWithGranularity:intoHeap:atIndex:
+ _objc_retain_x28
+ _putchar
+ _validateDispatchThreadsPerThreadgroupWithRTPTG
+ _validateUnspecializedProperties
+ _verifyCopyFromTensorToTensor
+ _verifyCopyFromTensorToTensor.cold.1
+ _verifySlice
+ _verifyStrides
- -[MTLDebugComputePipelineState reflection]
- -[MTLDebugRenderPipelineState reflection]
- -[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:]
- -[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:]
- -[MTLGPUDebugAccelerationStructureErrorLog functionName]
- -[MTLGPUDebugAccelerationStructureErrorLog setFunctionName:]
- -[MTLGPUDebugArgumentEncoder setArgumentBuffer:offset:]
- -[MTLGPUDebugArgumentEncoder setArgumentBuffer:startOffset:arrayElement:]
- -[MTLGPUDebugArgumentEncoder setBuffer:offset:atIndex:]
- -[MTLGPUDebugArgumentEncoder setBuffers:offsets:withRange:]
- -[MTLGPUDebugCommandBuffer _allocReportEntryStorageForType:]
- -[MTLGPUDebugCommandBuffer _checkReportBuffers].cold.1
- -[MTLGPUDebugCommandBuffer _encodeReportBuffer:type:]
- -[MTLGPUDebugCommandBuffer _newReportBuffer]
- -[MTLGPUDebugCommandBuffer beginUseOfMeshShadersInEncoder:]
- -[MTLGPUDebugCommandBuffer encodeBuffers:offsets:withRange:resultOffset:]
- -[MTLGPUDebugCommandBuffer encoderIdentifierForEncoderIndex:]
- -[MTLGPUDebugCommandBuffer resourceTypeForTexture:stage:]
- -[MTLGPUDebugCommandBuffer resourceUsageForBuffer:stage:]
- -[MTLGPUDebugComputeCommandEncoder _initBufferArgumentData:]
- -[MTLGPUDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:]
- -[MTLGPUDebugComputeCommandEncoder setKernelReportBuffer:offset:]
- -[MTLGPUDebugComputePipelineState _initConstantsBuffer:device:]
- -[MTLGPUDebugDevice _prepareInsertLibraries:]
- -[MTLGPUDebugIndirectCommandBuffer setBuffer:offset:atIndex:forStage:commandIndex:]
- -[MTLGPUDebugIndirectCommandBuffer setBuffer:offset:attributeStride:atIndex:forStage:commandIndex:]
- -[MTLGPUDebugIndirectCommandBuffer setTessellationControlPointIndexBuffer:offset:commandIndex:]
- -[MTLGPUDebugRenderCommandEncoder _initBufferArgumentData:]
- -[MTLGPUDebugRenderCommandEncoder setFragmentBufferOffset:atIndex:]
- -[MTLGPUDebugRenderCommandEncoder setFragmentReportBuffer:offset:]
- -[MTLGPUDebugRenderCommandEncoder setMeshBufferOffset:atIndex:]
- -[MTLGPUDebugRenderCommandEncoder setMeshReportBuffer:offset:]
- -[MTLGPUDebugRenderCommandEncoder setObjectBufferOffset:atIndex:]
- -[MTLGPUDebugRenderCommandEncoder setObjectReportBuffer:offset:]
- -[MTLGPUDebugRenderCommandEncoder setTessellationControlPointIndexBuffer:offset:]
- -[MTLGPUDebugRenderCommandEncoder setTileBufferOffset:atIndex:]
- -[MTLGPUDebugRenderCommandEncoder setTileReportBuffer:offset:]
- -[MTLGPUDebugRenderCommandEncoder setVertexBufferOffset:attributeStride:atIndex:]
- -[MTLGPUDebugRenderCommandEncoder setVertexReportBuffer:offset:]
- -[MTLGPUDebugRenderPipelineState _initConstantsBuffer:device:]
- -[MTLGPUDebugStackOverflowErrorLog functionName]
- -[MTLGPUDebugStackOverflowErrorLog setFunctionName:]
- -[MTLGPUDebugTrapErrorLog functionName]
- -[MTLGPUDebugTrapErrorLog setFunctionName:]
- -[MTLToolsDevice unwrapMTLRelocations:]
- GCC_except_table102
- GCC_except_table109
- GCC_except_table113
- GCC_except_table185
- GCC_except_table187
- GCC_except_table193
- GCC_except_table205
- GCC_except_table225
- GCC_except_table235
- GCC_except_table267
- GCC_except_table274
- GCC_except_table280
- GCC_except_table284
- GCC_except_table298
- GCC_except_table47
- GCC_except_table82
- GCC_except_table89
- _OBJC_IVAR_$_MTLDebugComputePipelineState._reflection
- _OBJC_IVAR_$_MTLDebugRenderPipelineState._reflection
- _OBJC_IVAR_$_MTLGPUDebugAccelerationStructureErrorLog._functionName
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._currentReportID
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._fragmentReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._fragmentReportOffset
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._hasDeferredBindingObjectAndMeshReportBuffers
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._reportBufferList
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._reportEntryList
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._vertexComputeReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._vertexComputeReportOffset
- _OBJC_IVAR_$_MTLGPUDebugComputeCommandEncoder._reportBuffer
- _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._fragmentReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._meshReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._objectReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._tileReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._vertexReportBuffer
- _OBJC_IVAR_$_MTLGPUDebugStackOverflowErrorLog._functionName
- _OBJC_IVAR_$_MTLGPUDebugTrapErrorLog._functionName
- __OBJC_$_INSTANCE_VARIABLES_MTLGPUDebugStackOverflowErrorLog
- __OBJC_$_INSTANCE_VARIABLES_MTLGPUDebugTrapErrorLog
- __OBJC_$_PROP_LIST_MTLGPUDebugStackOverflowErrorLog
- __OBJC_$_PROP_LIST_MTLGPUDebugTrapErrorLog
- __ZL19DebugCompileOptionsP17MTLGPUDebugDeviceP17MTLCompileOptions
- __ZL19MTLBlitOptionStringm
- __ZL19findMaxTextureWidthPU23objcproto12MTLDeviceSPI11objc_objectPU21objcproto10MTLTexture11objc_object
- __ZL20_validateTextureViewP15MTLDebugTexture14MTLPixelFormat14MTLTextureType
- __ZL20_validateTextureViewP15MTLDebugTexture14MTLPixelFormat14MTLTextureType.cold.1
- __ZL21validateMTLBlitOptionmP18_MTLMessageContext
- __ZL22InitResourceIdentifierP18MTLGPUDebugTexture
- __ZL23instrumentationHeapInitP17MTLGPUDebugDevice
- __ZL27addBufferForUsageValidationP15MTLGPUDebugHeapP17MTLGPUDebugBuffer
- __ZL27addBufferForUsageValidationP15MTLLegacySVHeapP17MTLLegacySVBuffer
- __ZL28addTextureForUsageValidationP15MTLGPUDebugHeapP18MTLGPUDebugTexture
- __ZL28addTextureForUsageValidationP15MTLLegacySVHeapP18MTLLegacySVTexture
- __ZL28validateRenderPassDescriptorP31MTLRenderPassDescriptorInternalPU19objcproto9MTLDevice11objc_objectRNSt3__118unordered_multisetI26AttachmentDescriptorSimpleNS5_6hash_tENS5_7equal_tENS3_9allocatorIS5_EEEERNS3_5arrayIS5_Lm8EEESE_
- __ZL28validateSupportsTessellationPU19objcproto9MTLDevice11objc_objectbPKc
- __ZL33indirectCommandBufferPipelineInitP17MTLGPUDebugDevice
- __ZN11MTLGPUDebug16EncoderVariantT2INS_16MeshEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug16EncoderVariantT2INS_16TileEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug16EncoderVariantT2INS_18KernelEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug16EncoderVariantT2INS_18ObjectEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug16EncoderVariantT2INS_18VertexEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug16EncoderVariantT2INS_20FragmentEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_16MeshEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_16TileEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_18KernelEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_18ObjectEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_18VertexEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN11MTLGPUDebug19EncoderVariantT1AGXINS_20FragmentEncoderClassEE12setResourcesEPK29MTLGPUDebugStageBufferHandles11MTLBitFieldIyEmm
- __ZN12BinaryBuffer10WriteValueIN12AppendBuffer12StreamBufferEEEvRT_RK13MTLClearColor
- __ZN12BinaryBuffer10WriteValueIN12AppendBuffer12StreamBufferEEEvRT_RK9MTLRegion
- __ZN12BinaryBuffer10WriteValueINS_13ScratchBufferEEEvRT_RK9MTLRegion
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferE7MTLSizeJPU19objcproto9MTLBuffer11objc_objectmmmEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferE9MTLOriginJ7MTLSizePU19objcproto9MTLBuffer11objc_objectmmmEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferE9MTLOriginJ7MTLSizePU21objcproto10MTLTexture11objc_objectmmS3_mEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferE9MTLOriginJmEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU21objcproto10MTLTexture11objc_objectEEJ8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU22objcproto11MTLResource11objc_objectEEJmmmEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU26objcproto15MTLSamplerState11objc_objectEEJ8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU26objcproto15MTLSamplerState11objc_objectEEJNS3_IKfEES9_8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU34objcproto23MTLVisibleFunctionTable11objc_objectEEJ8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKPU39objcproto28MTLIntersectionFunctionTable11objc_objectEEJ8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferENS_5ArrayIKfEEJ8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferEPKfJS4_8_NSRangeEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsIN12AppendBuffer12StreamBufferEPU21objcproto10MTLTexture11objc_objectJmm9MTLRegion13MTLClearColor14MTLPixelFormatEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferE9MTLOriginJ7MTLSizePU19objcproto9MTLBuffer11objc_objectmmmEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferEPU21objcproto10MTLTexture11objc_objectJmm9MTLRegion13MTLClearColorEEEvRT_RKT0_DpRKT1_
- __ZN12BinaryBuffer14WriteArgumentsINS_13ScratchBufferEmJm9MTLRegion13MTLClearColor14MTLPixelFormatEEEvRT_RKT0_DpRKT1_
- __ZN12StringBuffer6AppendIJA10_cP8NSStringA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA11_cPK23MTLCountersCommandQueueA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA11_cPU19objcproto9MTLDevice11objc_objectA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA12_cA6_cA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA12_cPKvA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA23_cmA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA24_cmA11_cmA2_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA24_cmEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA24_cyA14_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJA2_cPK8NSStringA3_cmEEEvDpRKT_
- __ZN12StringBuffer6AppendIJPKcA10_cP8NSStringA3_cEEEvDpRKT_
- __ZN12StringBuffer6AppendIJPKcA14_cS2_A2_cEEEvDpRKT_
- __ZN12_GLOBAL__N_116BufferUsageTable11addResourceEP17MTLGPUDebugDeviceP17MTLGPUDebugBufferm
- __ZN12_GLOBAL__N_116TextureTypeTable11addResourceEP17MTLGPUDebugDeviceP18MTLGPUDebugTexture
- __ZN12_GLOBAL__N_117TextureUsageTable11addResourceEP17MTLGPUDebugDeviceP18MTLGPUDebugTexturem
- __ZN12_GLOBAL__N_118ResourceUsageTable7reallocEP17MTLGPUDebugDevicem
- __ZN12_GLOBAL__N_118ResourceUsageTableD2Ev
- __ZN15MetalBufferHeap11allocBufferEv.cold.2
- __ZN15MetalBufferHeap4growEj.cold.2
- __ZN24resolvedSharedPacketDataI19GPUDebugStackPacketE21setPipelineIdentifierEP8NSString
- __ZN24resolvedSharedPacketDataI19GPUDebugStackPacketEC2ERKS0_15MTLFunctionTypeP24MTLGPUDebugCommandBufferP17MTLGPUDebugGPULog
- __ZN24resolvedSharedPacketDataI19GPUDebugStackPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
- __ZN24resolvedSharedPacketDataI19GPUDebugStackPacketED2Ev
- __ZN24resolvedSharedPacketDataI23GPUDebugBadAccessPacketE21setPipelineIdentifierEP8NSString
- __ZN24resolvedSharedPacketDataI23GPUDebugBadAccessPacketEC2ERKS0_15MTLFunctionTypeP24MTLGPUDebugCommandBufferP17MTLGPUDebugGPULog
- __ZN24resolvedSharedPacketDataI23GPUDebugBadAccessPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
- __ZN24resolvedSharedPacketDataI23GPUDebugBadAccessPacketED2Ev
- __ZN24resolvedSharedPacketDataI24GPUDebugBadTexturePacketE21setPipelineIdentifierEP8NSString
- __ZN24resolvedSharedPacketDataI24GPUDebugBadTexturePacketEC2ERKS0_15MTLFunctionTypeP24MTLGPUDebugCommandBufferP17MTLGPUDebugGPULog
- __ZN24resolvedSharedPacketDataI24GPUDebugBadTexturePacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
- __ZN24resolvedSharedPacketDataI24GPUDebugBadTexturePacketED2Ev
- __ZN24resolvedSharedPacketDataI26GPUDebugFunctionTrapPacketE21setPipelineIdentifierEP8NSString
- __ZN24resolvedSharedPacketDataI26GPUDebugFunctionTrapPacketEC2ERKS0_15MTLFunctionTypeP24MTLGPUDebugCommandBufferP17MTLGPUDebugGPULog
- __ZN24resolvedSharedPacketDataI26GPUDebugFunctionTrapPacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
- __ZN24resolvedSharedPacketDataI26GPUDebugFunctionTrapPacketED2Ev
- __ZN24resolvedSharedPacketDataI35GPUDebugAccelerationStructurePacketE21setPipelineIdentifierEP8NSString
- __ZN24resolvedSharedPacketDataI35GPUDebugAccelerationStructurePacketEC2ERKS0_15MTLFunctionTypeP24MTLGPUDebugCommandBufferP17MTLGPUDebugGPULog
- __ZN24resolvedSharedPacketDataI35GPUDebugAccelerationStructurePacketEC2ERKS0_15MTLFunctionTypeP24MTLLegacySVCommandBufferP17MTLLegacySVGPULog
- __ZN24resolvedSharedPacketDataI35GPUDebugAccelerationStructurePacketED2Ev
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_16MeshEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_16TileEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_18KernelEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_18ObjectEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_18VertexEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug16EncoderVariantT2INS1_20FragmentEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_16MeshEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_16TileEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_18KernelEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_18ObjectEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_18VertexEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug19EncoderVariantT1AGXINS1_20FragmentEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_16MeshEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_16TileEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_18KernelEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_18ObjectEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_18VertexEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZN29MTLGPUDebugStageBufferHandles5flushIN11MTLGPUDebug25EncoderVariantIndirectionINS1_20FragmentEncoderClassEEEEEv11MTLBitFieldIyET_mm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne190102EPKvm
- __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorI19LegacySVMetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_112_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_117ReportBufferEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIP6NSDatamEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIj14MTLTextureTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP15MTLStructMemberNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP17MTLGPUDebugBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP17MTLLegacySVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110unique_ptrI29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI29LegacySVArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29LegacySVArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImN12_GLOBAL__N_120EncoderResourceUsageEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B8ne190102Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS3_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_prepareB8ne190102EmRS3_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS4_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne190102EmRS4_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS4_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne190102EmRS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__113unordered_mapIPU24objcproto13MTLAllocation11objc_objectN12_GLOBAL__N_154_MTLToolsResidencySetInternalCommittedAllocationsTable24CommittedAllocationEntryENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S5_EEEEE4findB8ne190102ERSC_
- __ZNSt3__114__split_bufferIPP11objc_objectNS_9allocatorIS3_EEE10push_frontEOS3_
- __ZNSt3__114__split_bufferIPP11objc_objectNS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__114__split_bufferIPP11objc_objectRNS_9allocatorIS3_EEE10push_frontERKS3_
- __ZNSt3__114__split_bufferIPP11objc_objectRNS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne190102Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL23instrumentationHeapInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL23instrumentationHeapInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11MTLViewportEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11MetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI14MTLScissorRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19LegacySVMetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI9MemberRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIP6NSDatamEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIj14MTLTextureTypeEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15MTLStructMemberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP16MTLDebugLocationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17MTLGPUDebugBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17MTLLegacySVBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU17objcproto7MTLHeap11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU21objcproto10MTLTexture11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU22objcproto11MTLResource11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU24objcproto13MTLAllocation11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU26objcproto15MTLResidencySet11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU26objcproto15MTLSamplerState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU28objcproto17MTLFunctionHandle11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU33objcproto22MTLRenderPipelineState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU34objcproto23MTLVisibleFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne190102EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26MTLTelemetryStatisticUIRecEEPvEEEEEclB8ne190102EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPKcEEPvEEEEEclB8ne190102EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__15dequeIP11objc_objectNS_9allocatorIS2_EEED2B8ne190102Ev
- __ZNSt3__16removeB8ne190102INS_11__wrap_iterIPjEEjEET_S4_S4_RKT0_
- __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEEC2B8ne190102Em
- __ZNSt3__17getlineB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_10
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_11
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_12
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_2
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_3
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_4
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_5
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_6
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_7
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_8
- ____ZN12_GLOBAL__N_114HeapUsageTable5applyERNS_16BufferUsageTableES2_S2_S2_RNS_17TextureUsageTableES4_S4_S4_RNS_16TextureTypeTableES6_S6_S6__block_invoke_9
- ____ZZL18WrapDynamicLibraryIZ45-[MTLGPUDebugDevice newDynamicLibrary:error:]E4$_15EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
- ____ZZL18WrapDynamicLibraryIZ60-[MTLGPUDebugDevice newDynamicLibraryWithURL:options:error:]E4$_14EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
- ____ZZL18WrapDynamicLibraryIZ63-[MTLGPUDebugDevice newDynamicLibrary:computeDescriptor:error:]E4$_16EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
- ____ZZL18WrapDynamicLibraryIZ83-[MTLGPUDebugDevice loadDynamicLibrariesForFunction:insertLibraries:options:error:]E4$_17EP25MTLGPUDebugDynamicLibraryP17MTLGPUDebugDeviceT_ENKUlS5_E_clIPU28objcproto17MTLDynamicLibrary11objc_objectEEDaS5__block_invoke
- ___block_literal_global.1648
- _objc_msgSend$initWithBaseTexture:device:buffer:offset:bytesPerRow:
- _objc_msgSend$initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:
- _objc_msgSend$unwrapMTLRelocations:
- _objc_retain_x26
- _wmemchr
CStrings:
+ "\n\t{ function name: \"%@\" }"
+ "\n\t{ function specializedName: \"%@\" }"
+ "\n\t{ functionGraph name: \"%@\" }"
+ "\n%u : "
+ "%20u %20u|"
+ "%@ Function(%@): %@ binding at index %lu for %@ cannot be null."
+ "%@ Function(%@): %@ binding at index %lu for %@ should have been set with setAddress:atIndex:."
+ "%@ Function(%@): %@ binding at index %lu for %@ should have been set with setResource:atBufferIndex:."
+ "%@ Function(%@): %@ binding at index %lu for %@ was never set."
+ "%@ Function(%@): A sparse texture is being bound at index %lu to a shader argument with write access enabled. Sparse textures do not support writes from shaders on this platform."
+ "%@ Function(%@): incorrect threadgroupMemory binding at index %lu for %@."
+ "%@ Function(%@): missing %@ binding at index %lu for %@. Argument table only supports %lu buffer bindings."
+ "%@ Function(%@): missing sampler binding at index %lu for %@. Argument table only supports %lu sampler bindings."
+ "%@ Function(%@): missing texture binding at index %lu for %@. Argument table only supports %lu texture bindings."
+ "%@ Function(%@): sampler binding at index %lu for %@ was never set."
+ "%@ Function(%@): texture binding at index %lu for %@ was never set."
+ "%@ Function(%@): threadgroupMemoryLength(%lu) must be >= %lu for threadgroupMemory binding at index %lu for %@."
+ "%@ length (%lu) must not be 0."
+ "%@ offset (%lu) must be 0 when %@ is nil."
+ "%s is not allowed unless MTLBlitOptionRowLinearPVRTC option is used."
+ "(destinationOffset + size)(%llu) must be <= [destinationBuffer length](%llu)."
+ "(range.location + range.length)(%lu) must be <= widthInTiles(%lu)."
+ "(rect.x(%lu) + rect.width(%lu))(%lu) for scissorRect (at index %lu) must be <= render pass width(%lu)"
+ "(rect.y(%lu) + rect.height(%lu))(%lu) for scissorRect (at index %lu) must be <= render pass height(%lu)"
+ "(sourceOffset + size)(%llu) must be <= [sourceBuffer length](%llu)."
+ "(sourceSize.width(%lu) * sourceSize.height(%lu) * sourceSize.depth(%lu))(%lu) must be > 0."
+ "(threadsPerGrid.width(%lu) * threadsPerGrid.y(%lu) * threadsPerGrid.depth(%lu))(%lu) must be > 0."
+ "(threadsPerThreadgroup.width(%lu) * threadsPerThreadgroup.height(%lu) * threadsPerThreadgroup.depth(%lu))(%lu) must be <= %lu."
+ "(threadsPerThreadgroup.width(%lu) * threadsPerThreadgroup.height(%lu) * threadsPerThreadgroup.depth(%lu))(%lu) must be > 0."
+ "-[MTL4DebugArgumentTable setAddress:atIndex:]"
+ "-[MTL4DebugArgumentTable setAddress:attributeStride:atIndex:]"
+ "-[MTL4DebugArgumentTable setResource:atBufferIndex:]"
+ "-[MTL4DebugArgumentTable setSamplerState:atIndex:]"
+ "-[MTL4DebugArgumentTable setTexture:atIndex:]"
+ "-[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:]"
+ "-[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:options:]"
+ "-[MTL4DebugCommandBuffer commandAllocator]"
+ "-[MTL4DebugCommandBuffer computeCommandEncoderWithSubstreamCount:]"
+ "-[MTL4DebugCommandBuffer computeCommandEncoder]"
+ "-[MTL4DebugCommandBuffer endCommandBuffer]"
+ "-[MTL4DebugCommandBuffer machineLearningCommandEncoder]"
+ "-[MTL4DebugCommandBuffer popDebugGroup]"
+ "-[MTL4DebugCommandBuffer pushDebugGroup:]"
+ "-[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:]"
+ "-[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:options:]"
+ "-[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:]"
+ "-[MTL4DebugCommandBuffer sampledComputeCommandEncoder:capacity:]"
+ "-[MTL4DebugCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:]"
+ "-[MTL4DebugCommandBuffer useResidencySet:]"
+ "-[MTL4DebugCommandBuffer useResidencySets:count:]"
+ "-[MTL4DebugCommandBuffer writeTimestampIntoHeap:atIndex:]"
+ "-[MTL4DebugCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]"
+ "-[MTL4DebugCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]"
+ "-[MTL4DebugCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]"
+ "-[MTL4DebugCommandEncoder endEncodingPreamble]"
+ "-[MTL4DebugCommandEncoder updateFence:afterEncoderStages:]"
+ "-[MTL4DebugCommandEncoder waitForFence:beforeEncoderStages:]"
+ "-[MTL4DebugCommandQueue addResidencySet:]"
+ "-[MTL4DebugCommandQueue addResidencySets:count:]"
+ "-[MTL4DebugCommandQueue commit:count:]"
+ "-[MTL4DebugCommandQueue commit:count:options:]"
+ "-[MTL4DebugCommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:]"
+ "-[MTL4DebugCommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:]"
+ "-[MTL4DebugCommandQueue removeResidencySet:]"
+ "-[MTL4DebugCommandQueue removeResidencySets:count:]"
+ "-[MTL4DebugCommandQueue signalDrawable:]"
+ "-[MTL4DebugCommandQueue signalEvent:value:]"
+ "-[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:]"
+ "-[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:]"
+ "-[MTL4DebugCommandQueue validateTextureAccess:region:mipLevel:slice:context:]"
+ "-[MTL4DebugCommandQueue waitForDrawable:]"
+ "-[MTL4DebugCommandQueue waitForEvent:value:]"
+ "-[MTL4DebugCommandQueue waitForEvent:value:timeout:]"
+ "-[MTL4DebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]"
+ "-[MTL4DebugCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:]"
+ "-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]"
+ "-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:]"
+ "-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]"
+ "-[MTL4DebugCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]"
+ "-[MTL4DebugCompiler newDynamicLibrary:completionHandler:]"
+ "-[MTL4DebugCompiler newDynamicLibrary:error:]"
+ "-[MTL4DebugCompiler newDynamicLibraryWithURL:completionHandler:]"
+ "-[MTL4DebugCompiler newDynamicLibraryWithURL:error:]"
+ "-[MTL4DebugCompiler newDynamicLibraryWithURL:options:completionHandler:]"
+ "-[MTL4DebugCompiler newDynamicLibraryWithURL:options:error:]"
+ "-[MTL4DebugCompiler newLibraryWithDescriptor:completionHandler:]"
+ "-[MTL4DebugCompiler newLibraryWithDescriptor:error:]"
+ "-[MTL4DebugCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:]"
+ "-[MTL4DebugCompiler newMachineLearningPipelineStateWithDescriptor:error:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:]"
+ "-[MTL4DebugCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]"
+ "-[MTL4DebugComputeCommandEncoder _validateComputeFunctionArguments:]"
+ "-[MTL4DebugComputeCommandEncoder beginVirtualSubstream]"
+ "-[MTL4DebugComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder commandBuffer]"
+ "-[MTL4DebugComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:]"
+ "-[MTL4DebugComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:]"
+ "-[MTL4DebugComputeCommandEncoder copyFromTexture:toTexture:]"
+ "-[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:]"
+ "-[MTL4DebugComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:]"
+ "-[MTL4DebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:]"
+ "-[MTL4DebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:]"
+ "-[MTL4DebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:]"
+ "-[MTL4DebugComputeCommandEncoder encodeEndIf]"
+ "-[MTL4DebugComputeCommandEncoder encodeEndWhile]"
+ "-[MTL4DebugComputeCommandEncoder encodeStartDoWhile]"
+ "-[MTL4DebugComputeCommandEncoder encodeStartElse]"
+ "-[MTL4DebugComputeCommandEncoder encodeStartIf:comparison:referenceValue:]"
+ "-[MTL4DebugComputeCommandEncoder encodeStartWhile:comparison:referenceValue:]"
+ "-[MTL4DebugComputeCommandEncoder endVirtualSubstream]"
+ "-[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:withRange:]"
+ "-[MTL4DebugComputeCommandEncoder fillBuffer:range:pattern4:]"
+ "-[MTL4DebugComputeCommandEncoder fillBuffer:range:value:]"
+ "-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:bytes:length:]"
+ "-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:]"
+ "-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:]"
+ "-[MTL4DebugComputeCommandEncoder generateMipmapsForTexture:]"
+ "-[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:]"
+ "-[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:slice:level:]"
+ "-[MTL4DebugComputeCommandEncoder nextVirtualSubstream]"
+ "-[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:]"
+ "-[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:]"
+ "-[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:]"
+ "-[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:]"
+ "-[MTL4DebugComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:]"
+ "-[MTL4DebugComputeCommandEncoder resetCommandsInBuffer:withRange:]"
+ "-[MTL4DebugComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder setArgumentTable:]"
+ "-[MTL4DebugComputeCommandEncoder setComputePipelineState:]"
+ "-[MTL4DebugComputeCommandEncoder setImageblockWidth:height:]"
+ "-[MTL4DebugComputeCommandEncoder setSubstream:]"
+ "-[MTL4DebugComputeCommandEncoder setThreadgroupDistributionMode:]"
+ "-[MTL4DebugComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:]"
+ "-[MTL4DebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:]"
+ "-[MTL4DebugComputeCommandEncoder signalProgress:]"
+ "-[MTL4DebugComputeCommandEncoder validateRefit:descriptor:destination:scratchBuffer:options:]"
+ "-[MTL4DebugComputeCommandEncoder waitForProgress:]"
+ "-[MTL4DebugComputeCommandEncoder waitForVirtualSubstream:]"
+ "-[MTL4DebugComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:]"
+ "-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:]"
+ "-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:]"
+ "-[MTL4DebugComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:]"
+ "-[MTL4DebugCounterHeap invalidateCounterRange:]"
+ "-[MTL4DebugCounterHeap resolveCounterRange:]"
+ "-[MTL4DebugMachineLearningCommandEncoder commandBuffer]"
+ "-[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:]"
+ "-[MTL4DebugMachineLearningCommandEncoder setArgumentTable:]"
+ "-[MTL4DebugMachineLearningCommandEncoder setPipelineState:]"
+ "-[MTL4DebugRenderCommandEncoder commandBuffer]"
+ "-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:]"
+ "-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:]"
+ "-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:]"
+ "-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:]"
+ "-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:]"
+ "-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:]"
+ "-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:]"
+ "-[MTL4DebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]"
+ "-[MTL4DebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]"
+ "-[MTL4DebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]"
+ "-[MTL4DebugRenderCommandEncoder drawPrimitives:indirectBuffer:]"
+ "-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:]"
+ "-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:]"
+ "-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]"
+ "-[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:]"
+ "-[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:withRange:]"
+ "-[MTL4DebugRenderCommandEncoder setArgumentTable:atStages:]"
+ "-[MTL4DebugRenderCommandEncoder setBlendColorRed:green:blue:alpha:]"
+ "-[MTL4DebugRenderCommandEncoder setColorAttachmentMap:]"
+ "-[MTL4DebugRenderCommandEncoder setColorStoreAction:atIndex:]"
+ "-[MTL4DebugRenderCommandEncoder setCommandDataCorruptModeSPI:]"
+ "-[MTL4DebugRenderCommandEncoder setCullMode:]"
+ "-[MTL4DebugRenderCommandEncoder setDepthBias:slopeScale:clamp:]"
+ "-[MTL4DebugRenderCommandEncoder setDepthClipMode:]"
+ "-[MTL4DebugRenderCommandEncoder setDepthClipModeSPI:]"
+ "-[MTL4DebugRenderCommandEncoder setDepthStencilState:]"
+ "-[MTL4DebugRenderCommandEncoder setDepthStoreAction:]"
+ "-[MTL4DebugRenderCommandEncoder setFrontFacingWinding:]"
+ "-[MTL4DebugRenderCommandEncoder setLineWidth:]"
+ "-[MTL4DebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]"
+ "-[MTL4DebugRenderCommandEncoder setRenderPipelineState:]"
+ "-[MTL4DebugRenderCommandEncoder setScissorRect:]"
+ "-[MTL4DebugRenderCommandEncoder setScissorRects:count:]"
+ "-[MTL4DebugRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:]"
+ "-[MTL4DebugRenderCommandEncoder setStencilReferenceValue:]"
+ "-[MTL4DebugRenderCommandEncoder setStencilStoreAction:]"
+ "-[MTL4DebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:]"
+ "-[MTL4DebugRenderCommandEncoder setTriangleFillMode:]"
+ "-[MTL4DebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:]"
+ "-[MTL4DebugRenderCommandEncoder setVertexAmplificationMode:value:]"
+ "-[MTL4DebugRenderCommandEncoder setViewport:]"
+ "-[MTL4DebugRenderCommandEncoder setViewports:count:]"
+ "-[MTL4DebugRenderCommandEncoder setVisibilityResultMode:offset:]"
+ "-[MTL4DebugRenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:]"
+ "-[MTLDebugAccelerationStructureCommandEncoder barrierAfterQueueStages:beforeStages:]"
+ "-[MTLDebugBlitCommandEncoder barrierAfterQueueStages:beforeStages:]"
+ "-[MTLDebugBlitCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:]"
+ "-[MTLDebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:]"
+ "-[MTLDebugComputePipelineState functionHandleWithBinaryFunction:]"
+ "-[MTLDebugComputePipelineState functionHandleWithName:]"
+ "-[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:]"
+ "-[MTLDebugComputePipelineState newComputePipelineStateWithBinaryFunctions:error:]"
+ "-[MTLDebugDevice functionHandleWithFunction:]"
+ "-[MTLDebugDevice functionHandleWithFunction:resourceIndex:]"
+ "-[MTLDebugDevice newArchiveWithURL:error:]"
+ "-[MTLDebugDevice newArgumentTableWithDescriptor:error:]"
+ "-[MTLDebugDevice newBufferWithLength:options:placementSparsePageSize:]"
+ "-[MTLDebugDevice newCompilerWithDescriptor:error:]"
+ "-[MTLDebugDevice newCounterHeapWithDescriptor:error:]"
+ "-[MTLDebugDevice newTextureViewPoolWithDescriptor:error:]"
+ "-[MTLDebugDevice sizeOfCounterHeapEntry:]"
+ "-[MTLDebugFunction validateIsIFBFunction]"
+ "-[MTLDebugRenderCommandEncoder barrierAfterQueueStages:beforeStages:]"
+ "-[MTLDebugRenderPipelineState functionHandleWithBinaryFunction:stage:]"
+ "-[MTLDebugRenderPipelineState functionHandleWithName:stage:]"
+ "-[MTLDebugRenderPipelineState newRenderPipelineDescriptorForSpecialization]"
+ "-[MTLDebugRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:]"
+ "-[MTLDebugResourceStateCommandEncoder barrierAfterQueueStages:beforeStages:]"
+ "-[MTLDebugTensor getBytes:strides:fromSlice:]"
+ "-[MTLDebugTensor getBytes:strides:fromSliceOrigin:sliceDimensions:]"
+ "-[MTLDebugTensor replaceSlice:withBytes:strides:]"
+ "-[MTLDebugTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:]"
+ "-[MTLDebugTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]"
+ "-[MTLDebugTextureViewPool setTextureView:atIndex:]"
+ "-[MTLDebugTextureViewPool setTextureView:descriptor:atIndex:]"
+ "-[MTLDebugTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:]"
+ "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
+ "@\"<MTL4ArgumentTable>\""
+ "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
+ "@\"<MTL4BinaryFunction>\"32@0:8@\"MTL4BinaryFunctionDescriptor\"16^@24"
+ "@\"<MTL4BinaryFunction>\"40@0:8@\"MTL4BinaryFunctionDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTL4CommandAllocator>\""
+ "@\"<MTL4CommandAllocator>\"16@0:8"
+ "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
+ "@\"<MTL4CommandBuffer>\""
+ "@\"<MTL4CommandBuffer>\"16@0:8"
+ "@\"<MTL4CommandEncoder>\""
+ "@\"<MTL4CommandQueue>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
+ "@\"<MTL4Compiler>\""
+ "@\"<MTL4Compiler>\"16@0:8"
+ "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"<MTLLibrary>\"16@?<v@?@\"<MTLDynamicLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"MTL4LibraryDescriptor\"16@?<v@?@\"<MTLLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"MTL4MachineLearningPipelineDescriptor\"16@?<v@?@\"<MTL4MachineLearningPipelineState>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"NSURL\"16@?<v@?@\"<MTLDynamicLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4BinaryFunctionDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTL4BinaryFunction>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTLComputePipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"<MTLRenderPipelineState>\"24@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"NSURL\"16Q24@?<v@?@\"<MTLDynamicLibrary>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"48@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32@?<v@?@\"<MTLComputePipelineState>\"@\"NSError\">40"
+ "@\"<MTL4CompilerTask>\"48@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">40"
+ "@\"<MTL4ComputeCommandEncoder>\"16@0:8"
+ "@\"<MTL4ComputeCommandEncoder>\"20@0:8I16"
+ "@\"<MTL4ComputeCommandEncoder>\"32@0:8^(?={?=b8b24IQQ}{?=b8b24IQQ})16Q24"
+ "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
+ "@\"<MTL4MachineLearningCommandEncoder>\"16@0:8"
+ "@\"<MTL4MachineLearningPipelineState>\""
+ "@\"<MTL4MachineLearningPipelineState>\"32@0:8@\"MTL4MachineLearningPipelineDescriptor\"16^@24"
+ "@\"<MTL4PipelineDataSetSerializer>\"16@0:8"
+ "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
+ "@\"<MTL4RenderCommandEncoder>\"24@0:8@\"MTL4RenderPassDescriptor\"16"
+ "@\"<MTL4RenderCommandEncoder>\"32@0:8@\"MTL4RenderPassDescriptor\"16Q24"
+ "@\"<MTL4RenderCommandEncoder>\"40@0:8@\"MTL4RenderPassDescriptor\"16^(?={?=b8b24IQQ}{?=b8b24IQQ})24Q32"
+ "@\"<MTLBinaryArchive>\"16@0:8"
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLComputePipelineState>\"32@0:8@\"MTL4ComputePipelineDescriptor\"16^@24"
+ "@\"<MTLComputePipelineState>\"32@0:8@\"NSString\"16^@24"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"NSArray\"16^Q24^@32"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"NSString\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLComputePipelineState>\"48@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32^@40"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"NSString\"16"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"<MTL4BinaryFunction>\"16Q24"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"NSString\"16Q24"
+ "@\"<MTLLibrary>\"32@0:8@\"MTL4LibraryDescriptor\"16^@24"
+ "@\"<MTLLibrary>\"40@0:8@\"NSURL\"16@\"NSString\"24^@32"
+ "@\"<MTLLogState>\""
+ "@\"<MTLRenderPipelineState>\"32@0:8@\"MTL4PipelineDescriptor\"16^@24"
+ "@\"<MTLRenderPipelineState>\"32@0:8@\"MTL4RenderPipelineBinaryFunctionsDescriptor\"16^@24"
+ "@\"<MTLRenderPipelineState>\"32@0:8@\"NSString\"16^@24"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"<MTLRenderPipelineState>\"24^@32"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"NSString\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLRenderPipelineState>\"48@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32^@40"
+ "@\"<MTLResidencySet>\""
+ "@\"<MTLTensor>\""
+ "@\"<MTLTensor>\"16@0:8"
+ "@\"<MTLTensor>\"24@0:8{MTLResourceID=Q}16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTensor>\"40@0:8@\"MTLTensorDescriptor\"16Q24^@32"
+ "@\"<MTLTensor>\"40@0:8{MTLTensorSlice=@@}16^@32"
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@\"GPUDebugRetainedReportingData\""
+ "@\"MTL4BinaryFunctionReflection\"16@0:8"
+ "@\"MTL4ComputePipelineDescriptor\""
+ "@\"MTL4DebugCommandAllocator\""
+ "@\"MTL4DebugCommandBuffer\""
+ "@\"MTL4DebugCommandEncoder\""
+ "@\"MTL4GPUDebugBinaryFunction\""
+ "@\"MTL4MachineLearningPipelineDescriptor\""
+ "@\"MTL4MachineLearningPipelineReflection\"16@0:8"
+ "@\"MTL4MeshRenderPipelineDescriptor\""
+ "@\"MTL4PipelineDescriptor\"16@0:8"
+ "@\"MTL4RenderPassDescriptor\""
+ "@\"MTL4RenderPipelineDescriptor\""
+ "@\"MTL4TileRenderPipelineDescriptor\""
+ "@\"MTL4ToolsArgumentTable\""
+ "@\"MTL4ToolsBinaryFunction\""
+ "@\"MTL4ToolsMachineLearningPipelineState\""
+ "@\"MTLComputePipelineReflection\"16@0:8"
+ "@\"MTLFunctionReflection\"24@0:8@\"MTL4FunctionDescriptor\"16"
+ "@\"MTLFunctionReflection\"24@0:8@\"NSString\"16"
+ "@\"MTLFunctionReflection\"32@0:8@\"MTL4FunctionDescriptor\"16Q24"
+ "@\"MTLGPUDebugCommandQueue\""
+ "@\"MTLLogicalToPhysicalColorAttachmentMap\""
+ "@\"MTLLogicalToPhysicalColorAttachmentMapSPI\""
+ "@\"MTLRenderPipelineReflection\"16@0:8"
+ "@\"MTLTensorExtents\"16@0:8"
+ "@\"NSArray\"40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"NSData\"24@0:8^@16"
+ "@\"NSData\"40@0:8@\"NSString\"16@\"NSString\"24^@32"
+ "@\"NSLock\""
+ "@\"_MTL4CommitFeedback\"40@0:8r^@16Q24@\"MTL4CommitOptions\"32"
+ "@24@0:8^@16"
+ "@24@0:8{MTLResourceID=Q}16"
+ "@32@0:8^@16^@24"
+ "@40@0:8@16@24@?32"
+ "@40@0:8@16@24q32"
+ "@40@0:8@16Q24@?32"
+ "@40@0:8@16Q24^{?=[32C]}32"
+ "@40@0:8@16^Q24^@32"
+ "@40@0:8Q16Q24q32"
+ "@40@0:8r^@16Q24@32"
+ "@40@0:8{MTLTensorSlice=@@}16^@32"
+ "@48@0:8@16@24@32@?40"
+ "@48@0:8@16@24Q32q40"
+ "@48@0:8@16Q24@32@40"
+ "@64@0:8@16@24@32Q40Q48@56"
+ "@72@0:8@16@24@32Q40Q48Q56@64"
+ "@72@0:8{MTL4BufferRange=QQ}16Q32{MTL4BufferRange=QQ}40Q56Q64"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "Acceleration structure descriptor must be a MTL4PrimitiveAccelerationStructureDescriptor, a MTL4InstanceAccelerationStructureDescriptor or a MTL4IndirectInstanceAccelerationStructureDescriptor"
+ "Add Residency Set Validation"
+ "Add Residency Sets Validation"
+ "Additional binary function (at index %lu) is not a MTL4BinaryFunction."
+ "Additional fragment binary function (at index %lu) is not a MTL4BinaryFunction."
+ "Additional mesh binary function (at index %lu) is not a MTL4BinaryFunction."
+ "Additional object binary function (at index %lu) is not a MTL4BinaryFunction."
+ "Additional tile binary function (at index %lu) is not a MTL4BinaryFunction."
+ "Additional vertex binary function (at index %lu) is not a MTL4BinaryFunction."
+ "All associated command encoders must be ended before endCommandBuffer is called."
+ "Archive with URL Validation"
+ "Argument Table Descriptor Validation"
+ "Argument Table Validation"
+ "Argument table cannot be nil"
+ "Argument table does not specifies enough bind points"
+ "Async Binary Function with Descriptor Validation"
+ "Async Compute Pipeline with Descriptor Validation"
+ "Async Dynamic Library with Library Validation"
+ "Async Dynamic Library with URL Validation"
+ "Async Library with Descriptor Validation"
+ "Async ML Pipeline with Descriptor Validation"
+ "Async Render Pipeline by Specialization with Descriptor Validation"
+ "Async Render Pipeline with Descriptor Validation"
+ "Attachment texture (Label: %s) used in command buffer (at index %lu) is not added to any residency set on the command buffer or command queue."
+ "B24@0:8@\"MTLTensorDescriptor\"16"
+ "B32@0:8^I16^I24"
+ "B36@0:8Q16Q24I32"
+ "Base: %llX End: %llX"
+ "Begin Command Buffer Validation"
+ "Binary Function with Descriptor Validation"
+ "Bounding box buffer address (%lu) must be a multiple of %lu bytes"
+ "Bounding box buffer size (%lu) must be at least the bounding box stride (%lu) times the number of bounding boxes (%lu)"
+ "Buffer placementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "CPU access for tensors with MTLResourceStorageModePrivate storage mode is disallowed."
+ "Call beginCommandBufferWithAllocator before creating a command encoder."
+ "Call beginCommandBufferWithAllocator before popDebugGroup."
+ "Call beginCommandBufferWithAllocator before pushDebugGroup."
+ "Call beginCommandBufferWithAllocator before resolving timestamps."
+ "Call beginCommandBufferWithAllocator before writing a timestamp."
+ "Can only be called when virtual substreams are being used."
+ "Cannot be called when command buffer jumps are being used."
+ "Cannot be called when virtual substreams are being used."
+ "Cannot place resource at offset %lu extending beyond the heap size %lu (required size for region %lu)"
+ "Cannot write compacted acceleration structure size because it exceeds end of buffer with length (%lu)."
+ "Command Buffer Get Command Allocator Validation"
+ "Command Buffer Pop Debug Group Validation"
+ "Command Buffer Push Debug Group Validation"
+ "Command Encoder Barrier Validation"
+ "Command Encoder End Encoding Validation"
+ "Command Encoder Get Command Buffer Validation"
+ "Command Encoder Update Fence Validation"
+ "Command Encoder Wait For Fence Validation"
+ "Command allocator for command buffer (at index %lu) was reset or released before the command buffer was committed."
+ "Command buffer (at index: %lu) cannot be committed as it does not resume the suspended render pass from command buffer (at index: %lu)."
+ "Command buffer (at index: %lu) is attempting to resume a render pass but there is no suspended render pass."
+ "Command buffer (at index: %lu) is not a MTL4CommandBuffer."
+ "Command buffer (at index: %lu) should not be nil."
+ "Command buffer (found at indices %lu and %lu) can only be committed once."
+ "Command buffer already has an open command encoder."
+ "Command buffer has already been committed. Call beginCommandBufferWithAllocator to reuse the command buffer (at index %lu)."
+ "Command buffers with suspending render command encoders cannot start any new command encoders."
+ "Commit Residency Set"
+ "Commit Validation"
+ "Commit With Options Validation"
+ "Compiler Validation"
+ "Compute Command Encoder Acceleration Structure Descriptor Validation"
+ "Compute Command Encoder Begin Virtual Substream Validation"
+ "Compute Command Encoder Build Acceleration Structure Validation"
+ "Compute Command Encoder Copy Acceleration Structure Validation"
+ "Compute Command Encoder Copy From Buffer To Buffer Validation"
+ "Compute Command Encoder Copy From Texture To Buffer Validation"
+ "Compute Command Encoder Copy From Texture To Texture Validation"
+ "Compute Command Encoder Copy Indirect Command Buffer Validation"
+ "Compute Command Encoder Copy and Write Compacted Acceleration Structure Validation"
+ "Compute Command Encoder Deserialize Instance Acceleration Structure Validation"
+ "Compute Command Encoder Deserialize Primitive Acceleration Structure Validation"
+ "Compute Command Encoder Dispatch Threadgroups Validation"
+ "Compute Command Encoder Dispatch Threadgroups With Indirect Buffer Validation"
+ "Compute Command Encoder Dispatch Threads Validation"
+ "Compute Command Encoder Dispatch Threads With Indirect Buffer Validation"
+ "Compute Command Encoder End Do While Validation"
+ "Compute Command Encoder End If Validation"
+ "Compute Command Encoder End Virtual Substream Validation"
+ "Compute Command Encoder End While Validation"
+ "Compute Command Encoder Execute Commands In Buffer Validation"
+ "Compute Command Encoder Fill Buffer Validation"
+ "Compute Command Encoder Fill Texture Validation"
+ "Compute Command Encoder Generate Mipmaps For Texture Validation"
+ "Compute Command Encoder Invalidate Compressed Texture Validation"
+ "Compute Command Encoder Next Virtual Substream Validation"
+ "Compute Command Encoder Optimize Contents for CPU Access Validation"
+ "Compute Command Encoder Optimize Contents for GPU Access Validation"
+ "Compute Command Encoder Optimize Indirect Command Buffer Validation"
+ "Compute Command Encoder Refit Acceleration Structure Validation"
+ "Compute Command Encoder Reset Commands In Buffer Validation"
+ "Compute Command Encoder Serialize Instance Acceleration Structure Validation"
+ "Compute Command Encoder Serialize Primitive Acceleration Structure Validation"
+ "Compute Command Encoder Set Argument Table Validation"
+ "Compute Command Encoder Set Compute Pipeline State Validation"
+ "Compute Command Encoder Set Imageblock Width and Height Validation"
+ "Compute Command Encoder Set Substream Validation"
+ "Compute Command Encoder Set Threadgroup Distribution Mode Validation"
+ "Compute Command Encoder Set Threadgroup Memory Length Validation"
+ "Compute Command Encoder Signal Progress Validation"
+ "Compute Command Encoder Start Do While Validation"
+ "Compute Command Encoder Start Else Validation"
+ "Compute Command Encoder Start If Validation"
+ "Compute Command Encoder Start While Validation"
+ "Compute Command Encoder Validation"
+ "Compute Command Encoder Wait For Progress Validation"
+ "Compute Command Encoder Wait For Virtual Substream Validation"
+ "Compute Command Encoder With Substream Count Validation"
+ "Compute Command Encoder Write Acceleration Structure Serialization Data Validation"
+ "Compute Command Encoder Write Acceleration Structure Traversal Depth Validation"
+ "Compute Command Encoder Write Compacted Acceleration Structure Size Validation"
+ "Compute Command Encoder Write Generic BVH Structure Sizes of Acceleration Structure Validation"
+ "Compute Command Encoder Write Generic BVH Structure of Acceleration Structure Validation"
+ "Compute Command Encoder Write Serialized Acceleration Structure Size Validation"
+ "Compute Function(%@): missing threadgroupMemory binding at index %lu for %@."
+ "Compute Function(%@): total used threadgroupMemoryLength(%lu) must be <= %lu."
+ "Compute Pipeline State with Binary Functions Validation"
+ "Compute Pipeline State with Binary Functions and Resource Indices Validation"
+ "Compute Pipeline with Descriptor Validation"
+ "Control point buffer address (%lu) must be a multiple of %lu bytes"
+ "Copy From Tensor Validation"
+ "Copy Placement Sparse Buffer Mappings Validation"
+ "Copy Placement Sparse Texture Mappings Validation"
+ "Copying texture mappings from texture views is not supported"
+ "Copying texture mappings to texture views is not supported"
+ "Counter Heap Descriptor Validation"
+ "Counter Heap Validation"
+ "Current set renderPipelineState is not a valid mesh render pipeline for draw."
+ "Current set renderPipelineState is not a valid render pipeline for draw."
+ "Current set renderPipelineState is not a valid tile render pipeline for dispatch."
+ "Data type of sourceTensor (%s) should match the data type of destinationTensor (%s)"
+ "Device Scoped Allocations Residency Set"
+ "Dimensions of tensor at buffer index %u does not match pipeline state argument dimensions"
+ "Drawable is not a CAMetalDrawable."
+ "Dynamic Library with Library Validation"
+ "Encode Compute Timestamps Validation"
+ "Encode Render Timestamps Validation"
+ "End Command Buffer Validation"
+ "Failed to begin command buffer (label: %s) as command allocator (label: %s) already has an open command buffer (label: %s)."
+ "Fill Texture Level and Slice Validation"
+ "Fill Texture Region Validation"
+ "For color attachment %u, the renderPipelineState pixelFormat must be MTLPixelFormatInvalid, as no texture is set."
+ "For color attachment %u, the texture sample count (%lu) does not match the renderPipelineState colorSampleCount (%lu)."
+ "For color attachment %u, the texture sample count (%lu) does not match the renderPipelineState sampleCount (%lu)."
+ "Fragment binary functions can only be added to render pipeline states or mesh render pipeline states."
+ "Function '%@' cannot be used with intersection function tables since it has the intersection_function_buffer tag"
+ "Function Handle with Binary Function Validation"
+ "Function Handle with Binary Function and Stage Validation"
+ "Function Handle with Name Validation"
+ "Function Handle with Name and Stage Validation"
+ "Function must be an intersection function"
+ "Function must have the intersection_function_buffer tag"
+ "Function was not compiled with MTLFunctionOptionCompileToBinary."
+ "Function was not compiled with MTLFunctionOptionPipelineIndependent."
+ "GPUDebugRetainedReportingData"
+ "Heap cannot be nil"
+ "Heap maxCompatiblePlacementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "Heap must be a placement heap"
+ "Heap must be of type MTLHeapTypePlacement"
+ "Heap parameter can be nil only when the mapping mode is MTLSparseTextureMappingModeUnmap (operation at index %lu has mapping mode MTLSparseTextureMappingModeMap)"
+ "I40@0:8r^@16Q24^@32"
+ "ICB_Inherit_Both_Mesh"
+ "ICB_Inherit_Both_Mesh_VertexPipelineState"
+ "ICB_Inherit_Both_Vertex"
+ "ICB_Inherit_Both_VertexPipelineState"
+ "Imageblock"
+ "Imageblock Data"
+ "Index buffer address (%lu) must be a multiple of the index data type stride (%lu)"
+ "Instance Acceleration Structure"
+ "Instance count buffer size (%lu) must be at least the size of a 32-bit unsigned integer"
+ "Instance descriptor buffer size (%lu) must be at least the instance descriptor stride (%lu) times the maximum number of instances (%lu)"
+ "Intersection Function Table"
+ "Invalid Shader Validation Log!"
+ "Invalid function type %@ bound to intersection function table, function must be of type MTLFunctionTypeIntersection."
+ "Invalid function type %@ bound to visible function table, function must be of type MTLFunctionTypeVisible."
+ "Invalid transformation buffer address (%lu) or length (%lu)."
+ "Invalid usage because device does not support vertex amplification."
+ "Invalid usage because encoding has ended."
+ "Library with Descriptor Validation"
+ "Logical (%s) and physical (%s) pixel formats do not match after being remapped"
+ "ML Pipeline with Descriptor Validation"
+ "MTL4Archive"
+ "MTL4ArchiveGGDSPI"
+ "MTL4ArchiveSPI"
+ "MTL4ArgumentTable"
+ "MTL4ArgumentTableGGDSPI"
+ "MTL4ArgumentTableSPI"
+ "MTL4BinaryFunction"
+ "MTL4BinaryFunctionGGDSPI"
+ "MTL4BinaryFunctionSPI"
+ "MTL4CommandAllocator"
+ "MTL4CommandAllocatorGGDSPI"
+ "MTL4CommandAllocatorSPI"
+ "MTL4CommandBuffer"
+ "MTL4CommandBufferGGDSPI"
+ "MTL4CommandBufferSPI"
+ "MTL4CommandEncoder"
+ "MTL4CommandEncoderGGDSPI"
+ "MTL4CommandEncoderSPI"
+ "MTL4CommandQueue"
+ "MTL4CommandQueueGGDSPI"
+ "MTL4CommandQueueSPI"
+ "MTL4Compiler"
+ "MTL4CompilerGGDSPI"
+ "MTL4CompilerSPI"
+ "MTL4CompilerTask"
+ "MTL4CompilerTaskGGDSPI"
+ "MTL4CompilerTaskSPI"
+ "MTL4ComputeCommandEncoder"
+ "MTL4ComputeCommandEncoderGGDSPI"
+ "MTL4ComputeCommandEncoderSPI"
+ "MTL4CounterHeap"
+ "MTL4CounterHeapGGDSPI"
+ "MTL4DebugArchive"
+ "MTL4DebugArgumentTable"
+ "MTL4DebugBinaryFunction"
+ "MTL4DebugCommandAllocator"
+ "MTL4DebugCommandBuffer"
+ "MTL4DebugCommandEncoder"
+ "MTL4DebugCommandQueue"
+ "MTL4DebugCompiler"
+ "MTL4DebugComputeCommandEncoder"
+ "MTL4DebugCounterHeap"
+ "MTL4DebugMachineLearningCommandEncoder"
+ "MTL4DebugMachineLearningPipelineState"
+ "MTL4DebugRenderCommandEncoder"
+ "MTL4GPUDebugArchive"
+ "MTL4GPUDebugBinaryFunction"
+ "MTL4GPUDebugCommandBuffer"
+ "MTL4GPUDebugCommandQueue"
+ "MTL4GPUDebugCompiler"
+ "MTL4GPUDebugComputeCommandEncoder"
+ "MTL4GPUDebugRenderCommandEncoder"
+ "MTL4MachineLearningCommandEncoder"
+ "MTL4MachineLearningCommandEncoderGGDSPI"
+ "MTL4MachineLearningPipelineState"
+ "MTL4MachineLearningPipelineStateGGDSPI"
+ "MTL4MachineLearningPipelineStateSPI"
+ "MTL4PipelineDataSetSerializer"
+ "MTL4PipelineDataSetSerializerGGDSPI"
+ "MTL4PipelineDataSetSerializerSPI"
+ "MTL4RenderCommandEncoder"
+ "MTL4RenderCommandEncoderGGDSPI"
+ "MTL4RenderCommandEncoderSPI"
+ "MTL4ToolsArchive"
+ "MTL4ToolsArgumentTable"
+ "MTL4ToolsBinaryFunction"
+ "MTL4ToolsCommandAllocator"
+ "MTL4ToolsCommandBuffer"
+ "MTL4ToolsCommandEncoder"
+ "MTL4ToolsCommandQueue"
+ "MTL4ToolsCompiler"
+ "MTL4ToolsCompilerTask"
+ "MTL4ToolsComputeCommandEncoder"
+ "MTL4ToolsCounterHeap"
+ "MTL4ToolsMachineLearningCommandEncoder"
+ "MTL4ToolsMachineLearningPipelineState"
+ "MTL4ToolsPipelineDataSetSerializer"
+ "MTL4ToolsRenderCommandEncoder"
+ "MTLAccelerationStructureSerializationData exceeds end of buffer with length (%lu)."
+ "MTLDebugResourceViewPool"
+ "MTLDebugTensor"
+ "MTLDebugTextureViewPool"
+ "MTLDrawable"
+ "MTLDrawableSPI"
+ "MTLFunctionHandleSPI"
+ "MTLFunctionOptionPipelineIndependent requires MTLFunctionOptionCompileToBinary."
+ "MTLGPUDebugTextureViewPool"
+ "MTLGPUDebugViewable"
+ "MTLLoadActionClear"
+ "MTLPackedFloat4x3 exceeds end of transformation buffer with length (%lu)."
+ "MTLResourceViewPool"
+ "MTLResourceViewPoolGGDSPI"
+ "MTLResourceViewPoolSPI"
+ "MTLTensor"
+ "MTLTensorSPI"
+ "MTLTextureTypeInvalid"
+ "MTLTextureUsageShaderWrite is not supported for MTLHeapTypeSparse on this platform."
+ "MTLTextureViewPool"
+ "MTLTextureViewPoolGGDSPI"
+ "MTLTextureViewPoolSPI"
+ "MTLToolsResourceViewPool"
+ "MTLToolsTensor"
+ "MTLToolsTextureViewPool"
+ "Machine Learning Command Encoder Validation"
+ "Mapping modifications on texture views are not supported"
+ "Mappings can only be copied from placement sparse resources"
+ "Mappings can only be copied to placement sparse resources"
+ "Mesh binary functions can only be added to mesh render pipeline states."
+ "Mesh render pipeline states created with a MTL4Compiler must be created with the supportFragmentBinaryLinking property of a MTL4MeshRenderPipelineDescriptor set to YES to add fragment binary functions."
+ "Mesh render pipeline states created with a MTL4Compiler must be created with the supportMeshBinaryLinking property of a MTL4MeshRenderPipelineDescriptor set to YES to add object binary functions."
+ "Mesh render pipeline states created with a MTL4Compiler must be created with the supportObjectBinaryLinking property of a MTL4MeshRenderPipelineDescriptor set to YES to add object binary functions."
+ "Motion transform buffer size (%lu) must be at least the motion transform stride (%lu) times the maximum number of motion transforms (%lu)"
+ "Motion transform count buffer size (%lu) must be at least the size of a 32-bit unsigned integer"
+ "No Tensor specified for resource at buffer index %u"
+ "No argument table was set on the encoder"
+ "No pipeline state was set on the encoder"
+ "Number of indices to read (segment count) (%lu) times index stride (%lu) must be less than or equal to length (%lu)"
+ "Number of indices to read (triangle count multiplied by 3) (%lu) times index stride (%lu) must be less than or equal to index buffer length (%lu)"
+ "Number of indices to read (triangle count multiplied by 3) (%lu) times index stride (%lu) must be less than or equal to length (%lu)"
+ "Number of vertices to read (triangle count multiplied by 3) (%lu) times vertex stride (%lu) must be less than or equal to vertex buffer length (%lu)"
+ "Object Payload"
+ "Object binary functions can only be added to mesh render pipeline states."
+ "Offset(%lu) + result size(%lu) must be <= Render Pass Descriptor's [visibilityResultBuffer length](%lu)."
+ "Only heaps of type MTL4CounterHeapTypeTimestamp are supported."
+ "Only placement sparse resources support mapping modifications"
+ "Only triangles may be drawn when using a rasterization rate map."
+ "Pipeline state cannot be nil"
+ "Pipeline states created with a MTL4Compiler must be created with the supportBinaryLinking property of a MTL4ComputePipelineDescriptor set to YES to add binary functions."
+ "Pipeline states created with a MTL4Compiler must be created with the supportFragmentBinaryLinking property of a MTL4RenderPipelineDescriptor set to YES to add fragment binary functions."
+ "Pipeline states created with a MTL4Compiler must be created with the supportVertexBinaryLinking property of a MTL4RenderPipelineDescriptor set to YES to add vertex binary functions."
+ "Placement sparse textures are not supported."
+ "Previous setBlendColor was unused."
+ "Previous setComputePipelineState was unused."
+ "Previous setCullMode was unused."
+ "Previous setDepthBias was unused."
+ "Previous setDepthClipMode was unused."
+ "Previous setDepthStencilState was unused."
+ "Previous setFrontFacingWinding was unused."
+ "Previous setRenderPipelineState was unused."
+ "Previous setScissorRect was unused."
+ "Previous setStencilReferenceValue was unused."
+ "Previous setTriangleFillMode was unused."
+ "Previous setVertexAmplificationCount was unused."
+ "Previous setViewport was unused."
+ "Previous setVisibilityResultMode was unused."
+ "PreviousSubstream (%lu) must be less than the current substream (%lu)."
+ "Primitive Acceleration Structure"
+ "Radius buffer address (%lu) must be a multiple of %lu bytes"
+ "Redundant call to setBlendColor."
+ "Redundant call to setComputePipelineState."
+ "Redundant call to setCullMode. (setCullMode called with %s but cull mode was already set)"
+ "Redundant call to setDepthBias."
+ "Redundant call to setDepthClipMode. (setDepthClipMode called with %s but depth clip mode was already set)"
+ "Redundant call to setDepthStencilState."
+ "Redundant call to setFrontFacingWinding. (setFrontFacingWinding called with %s but front facing winding was already set.)"
+ "Redundant call to setRenderPipelineState."
+ "Redundant call to setScissorRect."
+ "Redundant call to setStencilReferenceValue."
+ "Redundant call to setTriangleFillMode. (setTriangleFillMode called with %s but triangle fill mode was already set.)"
+ "Redundant call to setVertexAmplificationCount."
+ "Redundant call to setViewport."
+ "Redundant call to setVisibilityResultMode. (setVisibilityResultMode called with mode %s and offset %lu, but mode and offset were already set.)"
+ "Remove Residency Set Validation"
+ "Remove Residency Sets Validation"
+ "Render Command Encoder Dispatch Threads Per Tile Validation"
+ "Render Command Encoder Draw Indexed Primitives Validation"
+ "Render Command Encoder Draw Mesh Threadgroups Validation"
+ "Render Command Encoder Draw Mesh Threadgroups With Indirect Buffer Validation"
+ "Render Command Encoder Draw Mesh Threads Validation"
+ "Render Command Encoder Draw Primitives Validation"
+ "Render Command Encoder Draw Primitives Validation."
+ "Render Command Encoder Execute Commands In Buffer Validation"
+ "Render Command Encoder Set Argument Table Validation"
+ "Render Command Encoder Set Blend Color Validation."
+ "Render Command Encoder Set Color Attachment Map Validation"
+ "Render Command Encoder Set Color Store Action Validation."
+ "Render Command Encoder Set Command Data Corrupt Validation"
+ "Render Command Encoder Set Cull Mode Validation."
+ "Render Command Encoder Set Depth Bias Validation."
+ "Render Command Encoder Set Depth Clip Mode Validation"
+ "Render Command Encoder Set Depth Clip Mode Validation."
+ "Render Command Encoder Set Depth Stencil State Validation."
+ "Render Command Encoder Set Depth Store Action Validation."
+ "Render Command Encoder Set Front Facing Winding Validation"
+ "Render Command Encoder Set Line Width Validation"
+ "Render Command Encoder Set Object Threadgroup Memory Length Validation"
+ "Render Command Encoder Set Render Pipeline State Validation"
+ "Render Command Encoder Set Scissor Rect Validation."
+ "Render Command Encoder Set Scissor Rects Validation."
+ "Render Command Encoder Set Stencil Reference Value Validation."
+ "Render Command Encoder Set Stencil Store Action Validation."
+ "Render Command Encoder Set Threadgroup Memory Length Validation"
+ "Render Command Encoder Set Triangle Fill Mode Validation."
+ "Render Command Encoder Set Vertex Amplification Count Validation."
+ "Render Command Encoder Set Vertex Amplification Mode Validation."
+ "Render Command Encoder Set Viewport Validation"
+ "Render Command Encoder Set Viewports Validation"
+ "Render Command Encoder Set Visibility Result Mode Validation."
+ "Render Command Encoder With Descriptor Validation"
+ "Render Command Encoder must be created with a Render Pass Descriptor that has a visibilityResultBuffer."
+ "Render Pipeline Descriptor for Specialization Validation"
+ "Render Pipeline State with Binary Functions Validation"
+ "Render Pipeline by Specialization with Descriptor Validation"
+ "Render Pipeline with Descriptor Validation"
+ "Render pipeline states created with a MTL4Compiler must be created with the supportFragmentBinaryLinking property of a MTL4RenderPipelineDescriptor set to YES to add fragment binary functions."
+ "Render pipeline states created with a MTL4Compiler must be created with the supportVertexBinaryLinking property of a MTL4RenderPipelineDescriptor set to YES to add vertex binary functions."
+ "Replace Slice Validation"
+ "Resuming render command encoders must be the first encoder created in a command buffer."
+ "SVBindingTableFragmentBuffer"
+ "SVBindingTableMeshBuffer"
+ "SVBindingTableObjectBuffer"
+ "SVBindingTableVertexKernelBuffer"
+ "Scratch buffer length (%lu) must be at least scratch buffer size (%lu)"
+ "Setting attribute strides is not enabled on this argument table. Set supportAttributeStrides to YES on the argument table descriptor to enable attribute strides."
+ "Signal Drawable Validation"
+ "Signal Event Validation"
+ "Sparse textures are not supported as depth attachments on this device, unless they are placement sparse textures with a sparseTextureTier of MTLTextureSparseTier1 or greater."
+ "Sparse textures are not supported as stencil attachments on this device, unless they are placement sparse textures with a sparseTextureTier of MTLTextureSparseTier1 or greater."
+ "Sparse textures cannot be created with dual-plane texture formats on this platform."
+ "Specified range (loc=%lu, len=%lu) is not inside indirectCommandBuffer(size=%lu)."
+ "Suspended render pass from command buffer (at index: %lu) and resuming render pass from command buffer (at index: %lu) are not equal."
+ "Suspended render pass from command buffer (at index: %lu) was never resumed."
+ "Suspending or resuming render passes with a non-nil visibilityResultBuffer must use MTLVisibilityResultTypeAccumulate."
+ "T@\"<MTL4CommandAllocator>\",R"
+ "T@\"<MTL4CommandAllocator>\",R,N"
+ "T@\"<MTL4CommandBuffer>\",R,N"
+ "T@\"<MTL4Compiler>\",R"
+ "T@\"<MTL4Compiler>\",R,Vcompiler"
+ "T@\"<MTL4MachineLearningPipelineState>\",R,N,V_mlPipelineState"
+ "T@\"<MTL4PipelineDataSetSerializer>\",R"
+ "T@\"<MTLBinaryArchive>\",R"
+ "T@\"<MTLBuffer>\",&,N"
+ "T@\"<MTLBuffer>\",?,N"
+ "T@\"<MTLBuffer>\",N,V_SVBindingTableFragmentBuffer"
+ "T@\"<MTLBuffer>\",N,V_SVBindingTableMeshBuffer"
+ "T@\"<MTLBuffer>\",N,V_SVBindingTableObjectBuffer"
+ "T@\"<MTLBuffer>\",N,V_SVBindingTableVertexKernelBuffer"
+ "T@\"<MTLBuffer>\",V_privateData"
+ "T@\"<MTLComputePipelineState>\",&,N,V_computePipeline"
+ "T@\"<MTLRenderPipelineState>\",&,N,V_renderPipeline"
+ "T@\"<MTLResidencySet>\",V_cbResidencySet"
+ "T@\"<MTLTensor>\",R"
+ "T@\"<MTLTensor>\",R,V_parentTensor"
+ "T@\"MTL4BinaryFunctionReflection\",R"
+ "T@\"MTL4ComputePipelineDescriptor\",R,N,V_mtl4Descriptor"
+ "T@\"MTL4GPUDebugBinaryFunction\",R,W,N,V_binaryFunction"
+ "T@\"MTL4MachineLearningPipelineDescriptor\",R,N,V_descriptor"
+ "T@\"MTL4MachineLearningPipelineReflection\",R"
+ "T@\"MTL4MeshRenderPipelineDescriptor\",R,N,V_mtl4MeshDescriptor"
+ "T@\"MTL4RenderPipelineDescriptor\",R,N,V_mtl4Descriptor"
+ "T@\"MTL4TileRenderPipelineDescriptor\",R,N,V_mtl4TileDescriptor"
+ "T@\"MTL4ToolsBinaryFunction\",R,V_binaryFunction"
+ "T@\"MTLComputePipelineReflection\",R"
+ "T@\"MTLComputePipelineReflection\",R,N,V_validationReflection"
+ "T@\"MTLRenderPipelineReflection\",R"
+ "T@\"MTLRenderPipelineReflection\",R,N,V_validationReflection"
+ "T@\"MTLTensorExtents\",R"
+ "T@\"NSMutableArray\",V_cbAllocations"
+ "T@\"NSMutableArray\",V_usedPipelineStates"
+ "T@\"NSString\",R,V_label"
+ "TB,N,V_initializedTables"
+ "TI,V_numDispatches"
+ "TQ,N,V_currentState"
+ "TQ,N,V_functionType"
+ "TQ,N,V_intersectionFunctionSignature"
+ "TQ,R,N,V_aggregatedEncoderMask"
+ "TQ,R,N,V_currentGeneration"
+ "TQ,R,N,V_maxFragmentBindings"
+ "TQ,R,N,V_maxKernelBindings"
+ "TQ,R,N,V_maxMeshBindings"
+ "TQ,R,N,V_maxObjectBindings"
+ "TQ,R,N,V_maxVertexBindings"
+ "Td,R,N"
+ "Tensor"
+ "Texture View Pool Descriptor Validation"
+ "Texture View Pool Validation"
+ "Texture View from Descriptor Validation"
+ "Texture descriptor placementSparsePageSize(%@) and buffer placementSparsePageSize(%@) must be the same."
+ "Texture descriptor placementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "Texture placementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "The combination of MTLBlitOptionDepthFromDepthStencil and MTLBlitOptionStencilFromDepthStencil is not allowed."
+ "The function handle for function '%s' was not created from the pipeline state that created this function table."
+ "The number of bits set to 1 in value(%u) must be between (inclusive) 1 and the maximum amplification factor for the current device (%u)"
+ "Threadgroup Memory"
+ "Ti,R"
+ "Tile binary functions can only be added to tile render pipeline states."
+ "Tile pipeline states created with a MTL4Compiler must be created with the supportBinaryLinking property of a MTL4TileRenderPipelineDescriptor set to YES to add tile binary functions."
+ "Tile render pipeline states created with a MTL4Compiler must be created with the supportBinaryLinking property of a MTL4TileRenderPipelineDescriptor set to YES to add tile binary functions."
+ "Timestamp Resolve Validation"
+ "Timestamp Validation"
+ "Tq,R,N,V_maxCompatiblePlacementSparsePageSize"
+ "Tq,R,N,V_placementSparsePageSize"
+ "Transformation buffer requires 4 byte alignment, found address %lu."
+ "T{MTLResourceID=Q},R,N"
+ "T{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>={__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=^v}Qf}},V_encoderLabels"
+ "T{vector<MetalBuffer, std::allocator<MetalBuffer>>=^{MetalBuffer}^{MetalBuffer}^{MetalBuffer}},V_usedBuffers"
+ "Update Placement Sparse Buffer Mappings Validation"
+ "Update Placement Sparse Texture Mappings Validation"
+ "Use Residency Set Validation"
+ "Use Residency Sets Validation"
+ "Use residency sets between beginCommandBufferWithAllocator and endCommandBuffer."
+ "Using the same offset (%lu) in the visibility buffer twice in the same command encoder is not allowed."
+ "Vertex binary functions can only be added to render pipeline states."
+ "Vertex buffer address (%lu) must be a multiple of %lu bytes"
+ "Visible Function Table"
+ "Volume of sourceSlice (%llu) should match the volume of destinationSlice (%llu)"
+ "Wait For Drawable Validation"
+ "Wait For Event Validation"
+ "Wait For Event With Timeout Validation"
+ "[31{GPUDebugEncoderBoundBufAddress=\"gpuAddress\"Q\"stride\"Q}]"
+ "[31{GPUDebugEncoderBoundBuffers=\"resource\"@\"<MTLResource>\"\"offset\"Q\"stride\"Q\"type\"Q}]"
+ "[40Q]"
+ "[4{BufferUsageTable=\"_backingMemory\"@\"<MTLBuffer>\"\"_residencySet\"@\"<MTLResidencySet>\"}]"
+ "[4{TextureTypeTable=\"_backingMemory\"@\"<MTLBuffer>\"\"_residencySet\"@\"<MTLResidencySet>\"}]"
+ "[4{TextureUsageTable=\"_backingMemory\"@\"<MTLBuffer>\"\"_residencySet\"@\"<MTLResidencySet>\"}]"
+ "[5@\"<MTL4ArgumentTable>\"]"
+ "[5@\"<MTLBuffer>\"]"
+ "[5[40Q]]"
+ "[sourceTexture sampleCount](%lu) and [destinationTexture sampleCount](%lu) must be equal."
+ "[texture mipmapLevelCount](%lu) must be > 1."
+ "^Q24@0:8Q16"
+ "_Init"
+ "_MTLDebugValidateRenderPassDescriptorAndTrackAttachments"
+ "_SVBindingTableFragmentBuffer"
+ "_SVBindingTableMeshBuffer"
+ "_SVBindingTableObjectBuffer"
+ "_SVBindingTableVertexKernelBuffer"
+ "__waitUntilCompletedAsync:"
+ "__waitUntilScheduledAsync:"
+ "_activeViews"
+ "_addUsedBuffer:"
+ "_addedResidencySets"
+ "_aggregatedEncoderMask"
+ "_allVisibilityOffsets"
+ "_allocator"
+ "_allocatorGeneration"
+ "_allowsNullBufferBindings"
+ "_binaryFunction"
+ "_bufferBindings"
+ "_cbAllocations"
+ "_cbResidencySet"
+ "_checkReportBuffers:outputArray:encoderLabels:"
+ "_clearSuspendResumeRenderPassInfo"
+ "_colorAttachmentMap"
+ "_commandAllocator"
+ "_commit:count:options:"
+ "_commitMutex"
+ "_computeEncoderBoundBufAddressTable"
+ "_computeEncoderBoundBuffers"
+ "_computePipeline"
+ "_currentArgumentTable"
+ "_currentAttachments"
+ "_currentBlendColorAlpha"
+ "_currentBlendColorBlue"
+ "_currentBlendColorGreen"
+ "_currentBlendColorRed"
+ "_currentCommandBuffer"
+ "_currentComputePipelineState"
+ "_currentCullMode"
+ "_currentDepthBias"
+ "_currentDepthClamp"
+ "_currentDepthClipMode"
+ "_currentDepthSlopeScale"
+ "_currentDepthStencilState"
+ "_currentFragmentArgumentTable"
+ "_currentFrontFacingWinding"
+ "_currentGeneration"
+ "_currentImageBlockSize"
+ "_currentMeshArgumentTable"
+ "_currentObjectArgumentTable"
+ "_currentObjectThreadgroupMemoryLengths"
+ "_currentPipelineState"
+ "_currentRenderPipelineState"
+ "_currentScissorRects"
+ "_currentState"
+ "_currentStencilBackReferenceValue"
+ "_currentStencilFrontReferenceValue"
+ "_currentSubstreamProgressLabels"
+ "_currentThreadgroupMemoryArguments"
+ "_currentThreadgroupMemoryLengths"
+ "_currentTileArgumentTable"
+ "_currentTriangleFillMode"
+ "_currentVertexAmplificationCount"
+ "_currentVertexArgumentTable"
+ "_currentViewports"
+ "_currentVirtualSubstreamHasEncodedDispatch"
+ "_currentVisibilityResultMode"
+ "_currentVisibilityResultModeOffset"
+ "_debugCommandAllocator"
+ "_debugCommandEncoder"
+ "_decodeReportLogState:"
+ "_decodeReportLogState:outputArray:encoderLabels:"
+ "_encoderStageMask"
+ "_fragmentEncoderBoundBuffers"
+ "_hasOnlyRender"
+ "_icbInheritBothMeshVertexPipelineState"
+ "_icbInheritBothVertexPipelineState"
+ "_initConstantsBuffer:"
+ "_initializedTables"
+ "_internalBindingTable"
+ "_internalBindingTableForStage:"
+ "_internalBindingTables"
+ "_intersectionFunctionSignature"
+ "_lastCommittedCommandBuffer"
+ "_maxCompatiblePlacementSparsePageSize"
+ "_meshEncoderBoundBuffers"
+ "_mlPipelineState"
+ "_modifyComputeDynamicLinkingDescriptor:"
+ "_modifyComputePipelineDescriptor:"
+ "_modifyComputePipelineDescriptor:dynamicLinkingDescriptor:"
+ "_modifyDynamicLinkingDescriptor:"
+ "_modifyRenderDynamicLinkingDescriptor:"
+ "_modifyRenderPipelineDescriptor:"
+ "_modifyRenderPipelineDescriptor:dynamicLinkingDescriptor:"
+ "_mtl4Descriptor"
+ "_mtl4MeshDescriptor"
+ "_mtl4TileDescriptor"
+ "_numDispatches"
+ "_objectEncoderBoundBuffers"
+ "_parentTensor"
+ "_placementSparsePageSize"
+ "_privateData"
+ "_renderPipeline"
+ "_reportLogState"
+ "_resetEncoder"
+ "_resetEncoderWithDescriptor:"
+ "_resetRenderPassAttachmentTracking"
+ "_resolvedColorSampleCount"
+ "_samplerBindings"
+ "_setBufferForStage:atIndex:stage:"
+ "_setInternalBindingTableForStage:stage:"
+ "_setInternalBindingTables:type:"
+ "_supportsAttributeStrides"
+ "_suspendResumeRenderPassInfo"
+ "_textureBindings"
+ "_updateCachedMTL4MeshPipelineState"
+ "_updateCachedMTL4PipelineState"
+ "_updateCachedMTL4TilePipelineState"
+ "_updateEncoderStateAfterDispatch"
+ "_updateEncoderStateAfterDraw"
+ "_usedBytesBuffers"
+ "_usedBytesBuffersLock"
+ "_usedPipelineStates"
+ "_usedResidencySets"
+ "_validateComputeFunctionArguments:"
+ "_validateComputeFunctionBuiltinArguments:threadsPerThreadgroup:threadgroupsPerGrid:"
+ "_validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:"
+ "_validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:"
+ "_validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:"
+ "_validateDispatchThreadsPerTileCommon:threadsPerTile:"
+ "_validateDrawCommon:primitiveType:instanceCount:"
+ "_validateFillTextureCommon:texture:level:slice:region:"
+ "_validateFramebufferCompatibility:pipelineState:"
+ "_validateFunctionArguments:stages:"
+ "_validateIndexedDrawCommon:indexBuffer:indexType:indexBufferLength:"
+ "_validateLBRT:"
+ "_validateMeshDrawCommon:"
+ "_validateTextureViewDescriptor"
+ "_validateThreadsPerObjectThreadgroup:threadsPerMeshThreadgroup:context:"
+ "_validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:"
+ "_validationReflection"
+ "_vertexEncoderBoundBuffers"
+ "addBinaryFunctionWithDescriptor:"
+ "addFeedbackHandler:"
+ "addPipelineWithDescriptor:"
+ "addPresentScheduledHandler:"
+ "addPresentedHandler:"
+ "addResetHandler:"
+ "addUsedBuffer:"
+ "addUsedPipelineState:"
+ "addView:"
+ "addedResidencySets"
+ "additionalBinaryFunctions must not be nil"
+ "afterEncoderStages must be a valid combination of MTLStages for the current encoder type."
+ "afterQueueStages must be a valid combination of MTLStages."
+ "afterStages must be a valid combination of MTLStages."
+ "aggregatedEncoderMask"
+ "alphaBlendOperation"
+ "alphaToCoverageState"
+ "alphaToOneState"
+ "applyResidencySets:"
+ "argumentTable is not a MTL4ArgumentTable"
+ "argumentTable is not a MTL4ArgumentTable."
+ "attachCommandBuffer:"
+ "attachmentSet"
+ "barrierAfterEncoderStages:beforeEncoderStages:options:"
+ "barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:"
+ "barrierAfterQueueStages:beforeStages:"
+ "barrierAfterQueueStages:beforeStages:options:"
+ "barrierAfterQueueStages:beforeStages:visibilityOptions:"
+ "barrierAfterStages:beforeQueueStages:options:"
+ "barrierAfterStages:beforeQueueStages:visibilityOptions:"
+ "baseResourceID"
+ "beforeEncoderStages must be a valid combination of MTLStages for the current encoder type."
+ "beforeQueueStages must be a valid combination of MTLStages."
+ "beforeStages must be a valid combination of MTLStages."
+ "beginCommandBufferWithAllocator has already been called."
+ "beginCommandBufferWithAllocator must be called before endCommandBuffer."
+ "beginCommandBufferWithAllocator:"
+ "beginCommandBufferWithAllocator:options:"
+ "beginningEncoder:type:"
+ "binaryFunction"
+ "binaryFunctionsDescriptor must not be nil"
+ "binaryLinkedFunctions"
+ "bindInternalBuffer:index:"
+ "bindInternalBufferForStage:index:stage:"
+ "bindInternalBufferForStage:index:stage:offset:"
+ "bindInternalBufferWithOffset:offset:index:"
+ "bindInternalValue:index:"
+ "bindInternalValueForStage:index:stage:"
+ "bindingIndex (%d) must not be higher than the maxBufferBindCount (%d)."
+ "bindingIndex (%d) must not be higher than the maxSamplerStateCount (%d)."
+ "bindingIndex (%d) must not be higher than the maxTextureBindCount (%d)."
+ "blend state set to disabled, but blending substate set to Unspecialized. Blending substate is ignored."
+ "blendingState"
+ "buffer and the compute command encoder must be associated with the same device."
+ "bufferBindingAtIndex:"
+ "bufferBindingCount"
+ "buildAccelerationStructure:descriptor:scratchBuffer:"
+ "cancel"
+ "cbAllocations"
+ "cbResidencySet"
+ "checkAndGetMessage:logBuffer:message:"
+ "checkMTL4AccelerationStructureDescriptor"
+ "colorAttachmentIndex(%lu) must be < %lu"
+ "colorAttachmentMappingState"
+ "commandAllocator"
+ "commandAllocator is not a MTL4CommandAllocator."
+ "commandAllocator must be called between beginCommandBufferWithAllocator: and endCommandBuffer."
+ "commandAllocator must not be nil."
+ "commandBatchIdOffset"
+ "commandBatchIdRangeMin:max:"
+ "commit:count:"
+ "commit:count:options:"
+ "commit:count:options:preprocessHandler:"
+ "commitFeedbackDispatch"
+ "commonResidencySet"
+ "compiler"
+ "compilerTaskOptions is not a MTL4CompilerTaskOptions"
+ "compute command encoder is not encoding multiple substreams."
+ "computeCommandEncoderWithSubstreamCount:"
+ "computeFunctionDescriptor"
+ "computePipeline"
+ "copyBufferMappingsFromBuffer:toBuffer:operations:count:"
+ "copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:"
+ "copyFromTensor:sourceSlice:toTensor:destinationSlice:"
+ "copyResourceStatesFromPool:sourceRange:destinationLocation:"
+ "copyResourceViewsFromPool:sourceRange:destinationIndex:"
+ "copyTextureMappingsFromTexture:toTexture:operations:count:"
+ "copy_and_unwrap_mtl4_acceleration_structure_descriptor_buffer"
+ "corruptionMode (%lu) is not a valid MTLCommandDataCorruptionMode."
+ "count (%lu) is not supported on this device. See supportsVertexAmplificationCount:(NSUInteger)."
+ "count must be greater than 0."
+ "counterHeap is the wrong type."
+ "counterHeap must not be nil."
+ "createChildrenWrappersBufferWithInstanceDescriptorBufferRange:maxInstanceCount:instanceCountBufferRange:instanceDescriptorStride:instanceDescriptorType:"
+ "cullMode (%lu) is not a valid MTLCullMode."
+ "currentArgumentTable"
+ "currentArgumentTables"
+ "currentCommandBuffer"
+ "currentState"
+ "curveEndCaps"
+ "defaultCompilerProcessesCount"
+ "depthClipMode (%lu) is not a valid MTLDepthClipMode."
+ "descriptor is not a MTL4BinaryFunctionDescriptor"
+ "descriptor is not a MTL4CompilerDescriptor"
+ "descriptor is not a MTL4ComputePipelineDescriptor"
+ "descriptor is not a MTL4CounterHeapDescriptor"
+ "descriptor is not a MTL4LibraryDescriptor"
+ "descriptor is not a MTL4MachineLearningPipelineDescriptor"
+ "descriptor is not an MTL4ArgumentTableDescriptor."
+ "descriptor is not an MTLResourceViewPoolDescriptor."
+ "descriptor must be one of MTL4MeshRenderPipelineDescriptor, MTL4RenderPipelineDescriptor or MTL4TileRenderPipelineDescriptor"
+ "descriptor must not be nil"
+ "descriptor should not be nil."
+ "descriptor.computeFunctionDescriptor must not be nil"
+ "descriptor.fragmentFunctionDescriptor is not required when descriptor.isRasterizationEnabled is NO."
+ "descriptor.function must not be nil"
+ "descriptor.functionDescriptor must not be nil"
+ "descriptor.meshFunctionDescriptor must not be nil"
+ "descriptor.name must not be nil"
+ "descriptor.options must not be nil"
+ "descriptor.source must not be nil"
+ "descriptor.tileFunctionDescriptor must not be nil"
+ "descriptor.vertexFunctionDescriptor must not be nil"
+ "deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:"
+ "deserializePrimitiveAccelerationStructure:fromBuffer:"
+ "destinationAlphaBlendFactor"
+ "destinationBinaryArchive"
+ "destinationBuffer and the compute command encoder must be associated with the same device."
+ "destinationIndex (%d) and source length (%d) must be within the destination texture view pool size (%d)."
+ "destinationRGBBlendFactor"
+ "destinationSlice"
+ "destinationTensor"
+ "destinationTexture and the compute command encoder must be associated with the same device."
+ "destinationTexture cannot have storage mode MTLStorageModeMemoryless."
+ "detachCommandBuffer"
+ "device does not support argument tables."
+ "device does not support texture view pools."
+ "device must support placement sparse"
+ "dimensions"
+ "dispatchNetworkWithIntermediatesHeap:"
+ "dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:"
+ "dispatchThreadsWithIndirectBuffer:"
+ "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:"
+ "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:"
+ "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:"
+ "drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:"
+ "drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:"
+ "drawPrimitives:indirectBuffer:"
+ "drawable must not be nil."
+ "drawableID"
+ "enableBoundsChecking"
+ "enableResourceUsageValidation"
+ "enableStackOverflow"
+ "enableTextureChecks"
+ "enableThreadgroupMemoryChecks"
+ "encodeCopyAndUnwrapChildrenWithInstanceDescriptorBufferRange:dstInstanceDescriptorBufferRange:instanceDescriptorStride:instanceIDOffset:maxInstanceCount:"
+ "encodeEndDoWhile:comparison:referenceValue:"
+ "encodeStartIf:comparison:referenceValue:"
+ "encodeStartWhile:comparison:referenceValue:"
+ "encodeUnwrapWithIASDescriptor:"
+ "encodeUnwrapWithIndirectIASDescriptor:"
+ "encoderLabels"
+ "endCommandBuffer"
+ "endCommandBuffer must be called before committing the command buffer (at index %lu)."
+ "endEncoding called for an encoder with no side effects."
+ "endEncoding was already called!"
+ "endEncodingPreamble"
+ "endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:"
+ "endEventValue"
+ "entryCount"
+ "entryCount must not be more than 4096."
+ "evaluateSloppyUsage:"
+ "evaluateUsage:"
+ "event is not a MTLEvent."
+ "event should not be nil."
+ "executeBlocksWithCommitFeedback:"
+ "executeCommandsInBuffer:indirectBuffer:"
+ "extentAtDimensionIndex:"
+ "fence should conform to the MTLFence protocol."
+ "fence should not be nil."
+ "fenceToUpdate is the wrong type."
+ "fenceToWait is the wrong type."
+ "fileExistsAtPath:isDirectory:"
+ "fillMode (%lu) is not a valid MTLTriangleFillMode."
+ "fillWithByte:"
+ "fragmentAdditionalBinaryFunctionResourceIndices"
+ "fragmentBindings"
+ "fragmentFunctionDescriptor"
+ "fragmentLinkingDescriptor"
+ "fragmentStaticLinkingDescriptor"
+ "frontFacingWinding (%lu) is not a valid MTLWinding."
+ "function (at index %lu) is not a MTLFunction."
+ "function is not a MTL4BinaryFunction."
+ "function must not be nil"
+ "functionConstants"
+ "functionDescriptor"
+ "functionDescriptors"
+ "functionGraph"
+ "functionHandleToDebugFunctionHandle:"
+ "functionHandleToDebugFunctionHandle:binaryFunction:"
+ "functionHandleToDebugFunctionHandle:binaryFunction:stage:"
+ "functionHandleToDebugFunctionHandle:stage:"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithBinaryFunction:stage:"
+ "functionHandleWithFunction:resourceIndex:"
+ "functionHandleWithName:"
+ "functionHandleWithName:stage:"
+ "functionReflectionWithFunctionDescriptor:"
+ "functionReflectionWithFunctionDescriptor:stage:"
+ "functions must not be nil"
+ "getActiveViews"
+ "getBufferBindings:bindingCount:"
+ "getBytes:strides:fromSlice:"
+ "getBytes:strides:fromSliceOrigin:sliceDimensions:"
+ "getInternalValueForStage:stage:"
+ "getIntersectionFunctionSignature"
+ "getPhysicalIndexForLogicalIndex:"
+ "getPrivateDataAndOffset:privateDataOffset:"
+ "getRetainedData"
+ "getTextureBindings:bindingCount:"
+ "getViewableAt:"
+ "hasMetal4Descriptor"
+ "hasOnlyRender"
+ "hasUnspecializedProperties:"
+ "heap free space (%lu) is too small, %lu bytes is required"
+ "heap type must be MTLHeapTypePlacement"
+ "height (%lu) must be > 0 and a power of two."
+ "incrementCurrentEncoderID"
+ "index (%d) must not be higher than the resource view count (%d)."
+ "index (%lu) is larger than heap size (%lu)."
+ "index (%lu) must be < %lu."
+ "index (%lu) must be within heap size (%lu)."
+ "indexBuffer must not be 0."
+ "indexBufferLength (%lu) must be a multiple of %lu bytes"
+ "indirectBuffer must not be 0."
+ "indirectCommandBuffer inherits pipelines (inheritPipelineState = YES) but the compute pipeline set on this encoder does not support indirect command buffers (supportIndirectCommandBuffers = NO)"
+ "indirectCommandBuffer is not a MTLIndirectCommandBuffer."
+ "indirectRangeBuffer must not be 0."
+ "initCommon"
+ "initImageData:"
+ "initReportBufferInPrivateData:"
+ "initWithArchive:device:"
+ "initWithArgumentTable:device:descriptor:"
+ "initWithBaseObject:buffer:"
+ "initWithBaseObject:device:commandBuffer:encoderStageMask:"
+ "initWithBaseObject:parent:binaryFunction:"
+ "initWithBaseObject:parent:binaryFunction:stage:"
+ "initWithBaseObject:parent:stage:"
+ "initWithBaseObject:parentTensor:"
+ "initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:descriptor:"
+ "initWithBaseTexture:device:buffer:offset:bytesPerRow:descriptor:"
+ "initWithBaseTexture:device:placementSparsePageSize:"
+ "initWithBinaryFunction:debugInstrumentationData:device:"
+ "initWithBuffer:device:options:placementSparsePageSize:"
+ "initWithCommandBuffer:device:"
+ "initWithCommandEncoder:commandBuffer:"
+ "initWithCompiler:"
+ "initWithCompiler:device:"
+ "initWithComputeCommandEncoder:commandBuffer:"
+ "initWithComputeCommandEncoder:commandBuffer:encoderID:"
+ "initWithComputeCommandEncoder:commandBuffer:numSubstreams:"
+ "initWithComputePipelineState:binaryFunctions:withState:device:"
+ "initWithComputePipelineState:descriptor:device:"
+ "initWithComputePipelineState:descriptor:dynamicLinkingDescriptor:device:"
+ "initWithComputePipelineState:parent:mtl4Descriptor:"
+ "initWithComputePipelineState:reflection:parent:mtl4Descriptor:"
+ "initWithCounterHeap:device:"
+ "initWithFunctionHandle:computePipelineState:"
+ "initWithFunctionHandle:renderPipelineState:stage:"
+ "initWithFunctionName:functionType:debugInstrumentationData:device:"
+ "initWithHeap:device:maxCompatiblePlacementSparsePageSize:"
+ "initWithMLCommandEncoder:commandBuffer:"
+ "initWithMLPipelineState:parent:descriptor:"
+ "initWithRenderCommandEncoder:commandBuffer:descriptor:"
+ "initWithRenderPipelineState:descriptor:device:"
+ "initWithRenderPipelineState:descriptor:dynamicLinkingDescriptor:device:"
+ "initWithRenderPipelineState:originalObject:descriptor:device:"
+ "initWithRenderPipelineState:parent:mtl4Descriptor:"
+ "initWithRenderPipelineState:reflection:parent:mtl4Descriptor:"
+ "initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:"
+ "initWithResourceViewPool:device:"
+ "initWithTextureViewPool:device:"
+ "initializeBindings"
+ "initializedTables"
+ "insertSplit"
+ "instanceCount (%lu) must be non-zero."
+ "instrumentationHeapInit"
+ "intermediatesHeapSize"
+ "internalMTLBuffer"
+ "internalValueAtIndex:"
+ "intersectionFunctionSignature"
+ "invalid granularity specified."
+ "invalid stage (%lu) specified."
+ "invalidateCounterRange:"
+ "invokeLogHandlers:category:level:message:"
+ "isAllocatorGenerationValid"
+ "isTensorViewableWithReshapedDescriptor:"
+ "isUsed"
+ "lastCommittedCommandBuffer"
+ "lastCommittedCommandBufferGeneration"
+ "length (%lu) must be <= %lu."
+ "levelCount must be > 0."
+ "levels"
+ "library does not conform to MTLLibrary protocol"
+ "library is not a MTLDynamicLibrary"
+ "library must not be nil"
+ "llvmVersion"
+ "lock"
+ "lookupArchives"
+ "machineLearningCommandEncoder"
+ "machineLearningFunctionDescriptor"
+ "mapping should not be nil."
+ "max buffer bind count must not be more than 31."
+ "max sampler state bind count must not be more than 16."
+ "max texture bind count must not be more than 128."
+ "maxBufferBindCount"
+ "maxCompatiblePlacementSparsePageSize"
+ "maxCompatiblePlacementSparsePageSize of the heap (%s) must be at least as large as the placementSparsePageSize of the buffer (%s)"
+ "maxCompatiblePlacementSparsePageSize of the heap (%s) must be at least as large as the placementSparsePageSize of the texture (%s)"
+ "maxCompatiblePlacementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "maxSamplerStateBindCount"
+ "maxTextureBindCount"
+ "maximumCompilerProcessesCount"
+ "meshAdditionalBinaryFunctionResourceIndices"
+ "meshBindings"
+ "meshFunctionDescriptor"
+ "meshLinkingDescriptor"
+ "meshStaticLinkingDescriptor"
+ "mlPipelineState"
+ "mode (%lu) is not a valid MTLVisibilityResultMode."
+ "mtl4Descriptor"
+ "mtl4MeshDescriptor"
+ "mtl4TileDescriptor"
+ "mtlTensorFromGpuResourceID:"
+ "name must not be nil"
+ "newArchiveReplyForPipelineFunctionWithDescriptor:functionType:functionId:"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:"
+ "newBinaryFunctionWithDescriptor:compilerTaskOptions:error:"
+ "newBinaryFunctionWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCommandBuffer"
+ "newCommandQueue4"
+ "newCompilerWithDescriptor:error:"
+ "newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:"
+ "newComputePipelineStateWithBinaryFunctions:error:"
+ "newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:"
+ "newComputePipelineStateWithDescriptor:compilerTaskOptions:error:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:"
+ "newComputePipelineStateWithFunctionName:"
+ "newComputePipelineStateWithName:dynamicLinkingDescriptor:error:"
+ "newComputePipelineStateWithName:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newDynamicLibrary:completionHandler:"
+ "newDynamicLibraryWithURL:completionHandler:"
+ "newDynamicLibraryWithURL:options:completionHandler:"
+ "newLibraryWithMPSGraphPackageURL:name:error:"
+ "newMTL4CommandQueue"
+ "newMTL4CommandQueueWithDescriptor:error:"
+ "newMachineLearningPipelineStateWithDescriptor:completionHandler:"
+ "newMachineLearningPipelineStateWithDescriptor:error:"
+ "newPipelineDataSetSerializerWithDescriptor:"
+ "newRenderPipelineDescriptorForSpecialization"
+ "newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:"
+ "newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:"
+ "newRenderPipelineStateWithBinaryFunctions:error:"
+ "newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:"
+ "newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:"
+ "newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:"
+ "newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:"
+ "newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:"
+ "newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:"
+ "newRenderPipelineStateWithName:error:"
+ "newSpecializedMTL4PipelineDescriptor:descriptor:"
+ "newTensorViewWithReshapedDescriptor:error:"
+ "newTensorViewWithSlice:error:"
+ "newTensorWithDescriptor:error:"
+ "newTensorWithDescriptor:offset:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "newTextureViewWithDescriptor:"
+ "newUnwrappedMTL4BinaryFunctionDescriptor:"
+ "newUnwrappedMTL4CompilerTaskOptions:"
+ "newUnwrappedMTL4ComputeDynamicLinkingDescriptor:"
+ "newUnwrappedMTL4ComputePipelineDescriptor:"
+ "newUnwrappedMTL4ComputePipelineDescriptor:dynamicLinkingDescriptor:"
+ "newUnwrappedMTL4FunctionDescriptor:"
+ "newUnwrappedMTL4LinkedFunctions:"
+ "newUnwrappedMTL4PipelineDescriptor:"
+ "newUnwrappedMTL4PipelineStageDynamicLinkingDescriptor:"
+ "newUnwrappedMTL4RenderDynamicLinkingDescriptor:"
+ "newUnwrappedMTL4RenderPipelineBinaryFunctionsDescriptor:"
+ "newUnwrappedMTL4RenderPipelineDescriptor:"
+ "newUnwrappedMTL4RenderPipelineDescriptor:dynamicLinkingDescriptor:"
+ "newUnwrappedMTL4RenderPipelineDynamicLinkingDescriptor:"
+ "newUnwrappedMTLRelocations:"
+ "newUnwrappedStaticLinkingDescriptor:"
+ "numDispatches"
+ "objectAdditionalBinaryFunctionResourceIndices"
+ "objectBindings"
+ "objectFunctionDescriptor"
+ "objectLinkingDescriptor"
+ "objectStaticLinkingDescriptor"
+ "offset(%lu) + length(%lu) must be <= %lu."
+ "onCurrentEncoderEnded"
+ "only heaps of type MTL4CounterHeapTypeTimestamp are supported"
+ "optimizedBytecode"
+ "options should be nil or an instance of the MTL4CommitOptions class."
+ "parentTensor"
+ "pipeline does not conform to MTLRenderPipelineState protocol"
+ "pipeline does not have unspecialized properties to specialize"
+ "pipeline format is not blendable, but blending is not set to disabled."
+ "pipeline must not be nil"
+ "pipelineDataSetSerializer"
+ "pipelineState is not a MTL4MachineLearningPipelineState"
+ "pipelineState is not a MTLRenderPipelineState."
+ "pipelineState should not be nil."
+ "placementSparsePageSize"
+ "placementSparsePageSize must be 0 as device does not support placement sparse."
+ "placementSparsePageSize must be 0 when creating a shared texture."
+ "placementSparsePageSize must be 0 when creating an iosurface backed texture."
+ "placementSparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "populateDefaultLoggerCache:logger:"
+ "preCommit:"
+ "preCommit:count:error:"
+ "preCommit:count:options:"
+ "prepareInsertLibraries:"
+ "present"
+ "presentAfterMinimumDuration:"
+ "presentAtTime:"
+ "presentWithOptions:"
+ "presentedTime"
+ "primitiveDataBuffer.length (%lu) is not large enough to contain %lu primitives with, primitiveDataStride (%lu), and primitiveDataElementSize (%lu)."
+ "privateFunctionDescriptors"
+ "queryTimestampFrequency"
+ "r^{MTL4DebugBindingInfo=iB}20@0:8I16"
+ "range cannot extend past heap size."
+ "rangeMode (at index: %lu) has value MTLSparseTextureMappingModeMap, heap must not be nil."
+ "rank"
+ "refitAccelerationStructure:descriptor:destination:scratchBuffer:"
+ "refitAccelerationStructure:descriptor:destination:scratchBuffer:options:"
+ "reflectionForFunctionDescriptor:"
+ "reflectionForFunctionWithName:"
+ "removeView:"
+ "renderCommandEncoderWithDescriptor:options:"
+ "renderPipeline"
+ "replaceSlice:withBytes:strides:"
+ "replaceSliceOrigin:sliceDimensions:withBytes:strides:"
+ "requested range (location=%lu, length=%lu) is larger than heap (%lu)."
+ "requested writing beyond the end of the destination buffer."
+ "requiredThreadsPerMeshThreadgroup"
+ "requiredThreadsPerObjectThreadgroup"
+ "requiredThreadsPerThreadgroup"
+ "requiredThreadsPerTileThreadgroup"
+ "requiresLegacyCompilerProcessesCount"
+ "resetCommandBuffer"
+ "resetEncoderState"
+ "residencySet (at index %lu) should not be nil."
+ "residencySet (at index: %lu) is not a MTLResidencySet."
+ "residencySet (at index: %lu) should not be nil."
+ "residencySet is not a MTLResidencySet."
+ "residencySet should not be nil."
+ "residencySetsLock"
+ "resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:"
+ "resourceBlobForByteCodeSignature:resourceName:error:"
+ "resourceViewCount"
+ "resourceViewCount for a texture view pool needs to be greater than zero."
+ "retainedData"
+ "rgbBlendOperation"
+ "roundup2(threadsPerTile.width(%lu)) * roundup2(threadsPerTile.height(%lu)) * threadsPerTile.depth(%lu) must be <= maxTotalThreadsPerThreadgroup(%lu), both threadsPerTile.width and threadsPerTile.height are rounded up to nearest even number"
+ "roundup2(threadsPerTile.width(%lu)) * roundup2(threadsPerTile.height(%lu)) * threadsPerTile.depth(%lu) must be <= maxTotalThreadsPerThreadgroup(%lu), both width and height are rounded up to nearest even number"
+ "runWithInputsArray:resultsArray:intermediateOperations:"
+ "sampledComputeCommandEncoder:capacity:"
+ "samplerBindingAtIndex:"
+ "samplerBindingCount"
+ "serializeAsArchiveAndFlushToURL:error:"
+ "serializeAsPipelinesScriptWithError:"
+ "serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:"
+ "serializePrimitiveAccelerationStructure:toBuffer:"
+ "setAddress:atIndex:"
+ "setAddress:attributeStride:atIndex:"
+ "setAlphaBlendOperation:"
+ "setAlphaToCoverageState:"
+ "setAlphaToOneState:"
+ "setArgumentTable:"
+ "setArgumentTable:atStages:"
+ "setBinaryLinkedFunctions:"
+ "setBlendingState:"
+ "setBufferSize:"
+ "setCanEndEncoding:"
+ "setCbAllocations:"
+ "setCbResidencySet:"
+ "setColorAttachmentMap:"
+ "setCommitFeedbackDispatch:"
+ "setComputeFunctionDescriptor:"
+ "setComputePipeline:"
+ "setContents:"
+ "setCurrentState:"
+ "setDebugInstrumentationDataForStage:stage:"
+ "setDestinationAlphaBlendFactor:"
+ "setDestinationRGBBlendFactor:"
+ "setEnableBoundsChecking:"
+ "setEnableResourceUsageValidation:"
+ "setEnableStackOverflow:"
+ "setEnableTextureChecks:"
+ "setEnableThreadgroupMemoryChecks:"
+ "setEncoderLabelForIndex:encoderIndex:"
+ "setEncoderLabels:"
+ "setFragmentAdditionalBinaryFunctionResourceIndices:"
+ "setFragmentFunctionDescriptor:"
+ "setFragmentStaticLinkingDescriptor:"
+ "setFunctionDescriptor:"
+ "setFunctionDescriptors:"
+ "setFunctionType:"
+ "setInitialCapacity:"
+ "setInitializeBindings:"
+ "setInitializedTables:"
+ "setInternalBindingTable:"
+ "setInternalBytes:length:atIndex:"
+ "setInternalBytesForStage:length:atIndex:stage:"
+ "setIntersectionFunctionSignature:"
+ "setLookupArchives:"
+ "setMachineLearningFunctionDescriptor:"
+ "setMaxBufferBindCount:"
+ "setMaxMeshBufferBindCount:"
+ "setMaxObjectBufferBindCount:"
+ "setMaxToolsDispatchBindings:"
+ "setMeshAdditionalBinaryFunctionResourceIndices:"
+ "setMeshFunctionDescriptor:"
+ "setMeshStaticLinkingDescriptor:"
+ "setNoCopy:"
+ "setNumDispatches:"
+ "setObjectAdditionalBinaryFunctionResourceIndices:"
+ "setObjectFunctionDescriptor:"
+ "setObjectStaticLinkingDescriptor:"
+ "setOptions:"
+ "setPipelineDataSetSerializer:"
+ "setPipelineState:"
+ "setPointerTag:"
+ "setPrivateFunctionDescriptors:"
+ "setRenderPipeline:"
+ "setReportBufferInPrivateData:privateDataOffset:logState:"
+ "setRequiresLegacyCompilerProcessesCount:"
+ "setResidencyForResource:"
+ "setResource:atBufferIndex:"
+ "setRgbBlendOperation:"
+ "setSVBindingTableFragmentBuffer:"
+ "setSVBindingTableMeshBuffer:"
+ "setSVBindingTableObjectBuffer:"
+ "setSVBindingTableVertexKernelBuffer:"
+ "setShaderReflection:"
+ "setShaderValidation:"
+ "setSourceAlphaBlendFactor:"
+ "setSourceRGBBlendFactor:"
+ "setStaticLinkingDescriptor:"
+ "setSubstream must be called before any dispatches inside a virtual substream."
+ "setSupportDynamicAttributeStride:"
+ "setTextureView:atIndex:"
+ "setTextureView:descriptor:atIndex:"
+ "setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:"
+ "setTileAdditionalBinaryFunctionResourceIndices:"
+ "setTileFunctionDescriptor:"
+ "setToolsDispatchBufferSPI:atIndex:"
+ "setToolsDispatchBufferSPI:atIndex:stages:"
+ "setUpLogState:"
+ "setUpShaderLoggingPrivateData"
+ "setUsedBuffers:"
+ "setUsedForShaderValidation:"
+ "setUsedPipelineStates:"
+ "setVertexAdditionalBinaryFunctionResourceIndices:"
+ "setVertexFunctionDescriptor:"
+ "setVertexStaticLinkingDescriptor:"
+ "setView:resourceID:type:index:"
+ "shaderReflection"
+ "shaderValidationConfig"
+ "shouldMaximizeConcurrentCompilation"
+ "signalDrawable:"
+ "signalOnCommandQueue:"
+ "size(%llu) must not be 0."
+ "sizeOfCounterHeapEntry:"
+ "sliceCount must be > 0."
+ "slices"
+ "source"
+ "sourceAlphaBlendFactor"
+ "sourceBuffer and the compute command encoder must be associated with the same device."
+ "sourcePool must be a texture view pool."
+ "sourceRGBBlendFactor"
+ "sourceRange location (%d) and length (%d) must be within the source texture view pool size (%d)."
+ "sourceSlice"
+ "sourceTensor"
+ "sourceTexture and the compute command encoder must be associated with the same device."
+ "sourceTexture cannot have storage mode MTLStorageModeMemoryless."
+ "sparseBufferTier"
+ "sparsePageSize(%lu) must be MTLSparsePageSize16, MTLSparsePageSize64, MTLSparsePageSize256 or 0."
+ "sparseTextureTier"
+ "specializedName"
+ "stage (%lu) must be one of MTLRenderStageVertex, MTLRenderStageFragment, MTLRenderStageTile, MTLRenderStageObject or MTLRenderStageMesh."
+ "stages"
+ "stages(%lu) must be a combination of MTLRenderStages. (MTLRenderStageVertex, MTLRenderStageFragment, MTLRenderStageTile, MTLRenderStageObject and MTLRenderStageMesh.)"
+ "startEventValue"
+ "state is not a MTLComputePipelineState."
+ "state should not be nil."
+ "staticLinkingDescriptor"
+ "strides"
+ "substream is out of bounds."
+ "supportAttributeStrides"
+ "supportBinaryLinking"
+ "supportColorAttachmentMapping"
+ "supportFragmentBinaryLinking"
+ "supportMeshBinaryLinking"
+ "supportObjectBinaryLinking"
+ "supportVertexBinaryLinking"
+ "supportsAIRNTBinaryArchiveFunctionPointers"
+ "supportsAIRNTBinaryArchiveSpecializedFunctions"
+ "supportsAIRNTBinaryArchiveStitchedFunctions"
+ "supportsAtomicWaitNotify"
+ "supportsCommandQueueBarriers"
+ "supportsIntersectionFunctionBuffers"
+ "supportsMTL4CommandAllocator"
+ "supportsMTL4CommandQueue"
+ "supportsMTL4Compiler"
+ "supportsMTL4ComputeCommandEncoder"
+ "supportsMTL4Counters"
+ "supportsMTL4LateBoundRenderTargets"
+ "supportsMTL4PSOSpecialization"
+ "supportsMTL4PlacementSparse"
+ "supportsMTL4RenderCommandEncoder"
+ "supportsMTLTextureViewPools"
+ "supportsMachineLearningCommandEncoders"
+ "supportsTensors"
+ "suspendResumeRenderPassInfo"
+ "tagType"
+ "tags"
+ "tensor"
+ "tensorSizeAndAlignWithDescriptor:"
+ "texture and the compute command encoder must be associated with the same device."
+ "texture must not have storage mode MTLStorageModeMemoryless."
+ "texture(%s) is not colorRenderable."
+ "texture(%s) is not filterable."
+ "textureBindingAtIndex:"
+ "textureBindingCount"
+ "textureTypeTable"
+ "threadgroupsPerGrid.depth (%llu) must be <= UINT32_MAX."
+ "threadgroupsPerGrid.height (%llu) must be <= UINT32_MAX."
+ "threadgroupsPerGrid.width (%llu) must be <= UINT32_MAX."
+ "threadsPerCompilerProcess"
+ "threadsPerGrid.depth (%llu) must be <= UINT32_MAX."
+ "threadsPerGrid.height (%llu) must be <= UINT32_MAX."
+ "threadsPerGrid.width (%llu) must be <= UINT32_MAX."
+ "threadsPerThreadgroup.depth (%lu) must be <= %lu."
+ "threadsPerThreadgroup.height (%lu) must be <= %lu."
+ "threadsPerThreadgroup.width (%lu) must be <= %lu."
+ "threadsPerTile (%lu, %lu) must equal tile size (%lu, %lu) when threadgroupSizeMatchesTileSize is true."
+ "tile pipelines are not supported for specialization."
+ "tileAdditionalBinaryFunctionResourceIndices"
+ "tileFunctionDescriptor"
+ "tileLinkingDescriptor"
+ "type must be MTL4CounterHeapTypeTimestamp."
+ "unlock"
+ "unused binding in encoder at object threadgroupMemory index %lu."
+ "unused binding in encoder at threadgroupMemory index %lu."
+ "unwrappedMTL4RenderPassDescriptor:"
+ "updateBufferMappings:heap:operations:count:"
+ "updateFence:afterEncoderStages:"
+ "updateTextureMappings:heap:operations:count:"
+ "url is not a NSURL object."
+ "url must be a file URL"
+ "url must not be nil"
+ "url must not point to a directory"
+ "url must point to an existing file"
+ "usageRequested 0x%lx is not compatible with usageRequired 0x%lx"
+ "usedBuffers"
+ "usedPipelineStates"
+ "usedResidencySets"
+ "v136@0:8^{_MTLMessageContext=q*I@q@*}16@24Q32Q40Q48{?=QQQ}56@80Q88Q96{?=QQQ}104Q128"
+ "v136@0:8^{_MTLMessageContext=q*I@q@*}16@24Q32Q40{?=QQQ}48{?=QQQ}72@96Q104Q112Q120Q128"
+ "v144@0:8^{_MTLMessageContext=q*I@q@*}16@24Q32Q40{?=QQQ}48{?=QQQ}72@96Q104Q112{?=QQQ}120"
+ "v16@?0@\"<MTL4CommitFeedback>\"8"
+ "v16@?0Q8"
+ "v24@0:8@\"<MTL4ArgumentTable>\"16"
+ "v24@0:8@\"<MTL4CommandAllocator>\"16"
+ "v24@0:8@\"<MTL4CommandQueue>\"16"
+ "v24@0:8@\"<MTL4MachineLearningPipelineState>\"16"
+ "v24@0:8@\"MTL4BinaryFunctionDescriptor\"16"
+ "v24@0:8@\"MTL4PipelineDescriptor\"16"
+ "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMap\"16"
+ "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMapSPI\"16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"<MTLDrawable>\">16"
+ "v24@?0@\"<MTL4BinaryFunction>\"8@\"NSError\"16"
+ "v24@?0@\"<MTL4MachineLearningPipelineState>\"8@\"NSError\"16"
+ "v24@?0@\"<MTLDynamicLibrary>\"8@\"NSError\"16"
+ "v24@?0Q8Q16"
+ "v28@0:8@16I24"
+ "v32@0:8@\"<MTL4ArgumentTable>\"16Q24"
+ "v32@0:8@\"<MTL4CommandAllocator>\"16@\"MTL4CommandBufferOptions\"24"
+ "v32@0:8@\"<MTL4CounterHeap>\"16Q24"
+ "v32@0:8^@16Q24"
+ "v32@0:8^{MTLResourceID=Q}16Q24"
+ "v32@0:8^{_MTLMessageContext=q*I@q@*}16@24"
+ "v32@0:8^{_MTLMessageContext=q*I@q@*}16Q24"
+ "v32@0:8q16Q24"
+ "v32@0:8{MTLResourceID=Q}16Q24"
+ "v32@0:8{MetalBuffer=^{MetalBufferHeap}I}16"
+ "v36@0:8@\"<MTLEvent>\"16Q24S32"
+ "v36@0:8@16Q24S32"
+ "v36@0:8Q16Q24I32"
+ "v40@0:8@\"<MTLAccelerationStructure>\"16{MTL4BufferRange=QQ}24"
+ "v40@0:8@16@24r^v32"
+ "v40@0:8@16{MTL4BufferRange=QQ}24"
+ "v40@0:8Q16Q24q32"
+ "v40@0:8^{_MTLMessageContext=q*I@q@*}16Q24Q32"
+ "v40@0:8^{_MTLMessageContext=q*I@q@*}16r^@24Q32"
+ "v40@0:8q16@\"<MTL4CounterHeap>\"24Q32"
+ "v40@0:8q16@24Q32"
+ "v40@0:8r^@16Q24@\"MTL4CommitOptions\"32"
+ "v40@0:8r^@16Q24@32"
+ "v40@0:8{vector<MetalBuffer, std::allocator<MetalBuffer>>=^{MetalBuffer}^{MetalBuffer}^{MetalBuffer}}16"
+ "v48@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24{MTL4BufferRange=QQ}32"
+ "v48@0:8@\"<MTLAccelerationStructure>\"16@\"NSArray\"24{MTL4BufferRange=QQ}32"
+ "v48@0:8@\"<MTLBuffer>\"16@\"<MTLBuffer>\"24r^{?={_NSRange=QQ}Q}32Q40"
+ "v48@0:8@\"<MTLBuffer>\"16@\"<MTLHeap>\"24r^{?=Q{_NSRange=QQ}Q}32Q40"
+ "v48@0:8@\"<MTLSharedEvent>\"16@\"<MTLSharedEvent>\"24Q32Q40"
+ "v48@0:8@\"<MTLTexture>\"16@\"<MTLHeap>\"24r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}32Q40"
+ "v48@0:8@\"<MTLTexture>\"16@\"<MTLTexture>\"24r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}32Q40"
+ "v48@0:8@\"MTLTensorExtents\"16@\"MTLTensorExtents\"24r^v32@\"MTLTensorExtents\"40"
+ "v48@0:8@16@24r^v32@40"
+ "v48@0:8@16@24r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}32Q40"
+ "v48@0:8@16@24r^{?=Q{_NSRange=QQ}Q}32Q40"
+ "v48@0:8@16@24r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}32Q40"
+ "v48@0:8@16@24r^{?={_NSRange=QQ}Q}32Q40"
+ "v48@0:8@16@24{MTL4BufferRange=QQ}32"
+ "v48@0:8@16{_NSRange=QQ}24Q40"
+ "v48@0:8Q16{?=QQQ}24"
+ "v48@0:8^v16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"MTLTensorExtents\"40"
+ "v48@0:8^v16@\"MTLTensorExtents\"24{MTLTensorSlice=@@}32"
+ "v48@0:8^v16@24@32@40"
+ "v48@0:8^v16@24{MTLTensorSlice=@@}32"
+ "v48@0:8^{_MTLMessageContext=q*I@q@*}16@24{MTLTensorSlice=@@}32"
+ "v48@0:8^{_MTLMessageContext=q*I@q@*}16Q24Q32Q40"
+ "v48@0:8^{_MTLMessageContext=q*I@q@*}16{?=QQQ}24"
+ "v48@0:8q16Q24@\"<MTL4CounterHeap>\"32Q40"
+ "v48@0:8q16Q24@32Q40"
+ "v48@0:8r^@16Q24@32@?40"
+ "v48@0:8{MTL4BufferRange=QQ}16{MTL4BufferRange=QQ}32"
+ "v48@0:8{MTLTensorSlice=@@}16r^v32@\"MTLTensorExtents\"40"
+ "v48@0:8{MTLTensorSlice=@@}16r^v32@40"
+ "v56@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24@\"<MTLAccelerationStructure>\"32{MTL4BufferRange=QQ}40"
+ "v56@0:8@16@24@32{MTL4BufferRange=QQ}40"
+ "v56@0:8@16{_NSRange=QQ}24q40^{_MTLMessageContext=q*I@q@*}48"
+ "v56@0:8{?=QQQ}16Q40^{_MTLMessageContext=q*I@q@*}48"
+ "v56@0:8{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>={__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=^v}Qf}}16"
+ "v64@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24@\"<MTLAccelerationStructure>\"32{MTL4BufferRange=QQ}40Q56"
+ "v64@0:8@\"<MTLTensor>\"16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"<MTLTensor>\"40@\"MTLTensorExtents\"48@\"MTLTensorExtents\"56"
+ "v64@0:8@\"<MTLTensor>\"16{MTLTensorSlice=@@}24@\"<MTLTensor>\"40{MTLTensorSlice=@@}48"
+ "v64@0:8@16@24@32@40@48@56"
+ "v64@0:8@16@24@32{MTL4BufferRange=QQ}40Q56"
+ "v64@0:8@16{MTLTensorSlice=@@}24@40{MTLTensorSlice=@@}48"
+ "v64@0:8Q16Q24Q32Q40Q48Q56"
+ "v68@0:8^{_MTLMessageContext=q*I@q@*}16@24@32@40^{MTLDebugFunctionArgument=BBQ@QQQQQQBff}48@56B64"
+ "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24@\"<MTLBuffer>\"40Q48@\"<MTLFence>\"56@\"<MTLFence>\"64"
+ "v72@0:8@16{_NSRange=QQ}24@40Q48@56@64"
+ "v72@0:8Q16{?=QQQ}24{?=QQQ}48"
+ "v72@0:8^{_MTLMessageContext=q*I@q@*}16{?=QQQ}24{?=QQQ}48"
+ "v72@0:8{?=QQQ}16{?=QQQ}40^{_MTLMessageContext=q*I@q@*}64"
+ "v72@0:8{MTL4BufferRange=QQ}16{MTL4BufferRange=QQ}32Q48Q56Q64"
+ "v80@0:8Q16Q24Q32Q40Q48Q56q64Q72"
+ "v88@0:8@16{?={?=QQQ}{?=QQQ}}24q72^{_MTLMessageContext=q*I@q@*}80"
+ "v96@0:8@16Q24{?={?=QQQ}{?=QQQ}}32q80^{_MTLMessageContext=q*I@q@*}88"
+ "v96@0:8@16{?={?=QQQ}{?=QQQ}}24Q72Q80^{_MTLMessageContext=q*I@q@*}88"
+ "v96@0:8^{_MTLMessageContext=q*I@q@*}16@24Q32Q40{?={?=QQQ}{?=QQQ}}48"
+ "validateBufferAccess:range:resourceSparsePageSize:context:"
+ "validateBufferAccess:region:resourceSparsePageSize:context:"
+ "validateCommitCommon:commandBuffers:count:"
+ "validateFunctionArguments:stage:functionName:argumentTable:boundThreadgroupMemoryArguments:bindings:allowNullBufferBindings:"
+ "validateHeapAccess:rangeOffset:tileRegions:resourceSparsePageSize:context:"
+ "validateIsIFBFunction"
+ "validateRefit:descriptor:destination:scratchBuffer:options:"
+ "validateTextureAccess:region:mipLevel:slice:context:"
+ "validationReflection"
+ "verifyGetBytesReplaceSliceWithContext:strides:slice:"
+ "vertexAdditionalBinaryFunctionResourceIndices"
+ "vertexAmplificationMode (%lu) is not a valid MTLVertexAmplificationMode."
+ "vertexBindings"
+ "vertexDescriptor"
+ "vertexFunctionDescriptor"
+ "vertexLinkingDescriptor"
+ "vertexStaticLinkingDescriptor"
+ "viewables"
+ "viewport (at index %lu) height must not be NaN."
+ "viewport (at index %lu) height must not be infinite."
+ "viewport (at index %lu) originX must not be NaN."
+ "viewport (at index %lu) originX must not be infinite."
+ "viewport (at index %lu) originY must not be NaN."
+ "viewport (at index %lu) originY must not be infinite."
+ "viewport (at index %lu) width must not be NaN."
+ "viewport (at index %lu) width must not be infinite."
+ "viewport (at index %lu) zfar must not be NaN."
+ "viewport (at index %lu) zfar must not be infinite."
+ "viewport (at index %lu) znear must not be NaN."
+ "viewport (at index %lu) znear must not be infinite."
+ "viewport height must not be NaN."
+ "viewport height must not be infinite."
+ "viewport originX must not be NaN."
+ "viewport originX must not be infinite."
+ "viewport originY must not be NaN."
+ "viewport originY must not be infinite."
+ "viewport width must not be NaN."
+ "viewport width must not be infinite."
+ "viewport zfar must not be NaN."
+ "viewport zfar must not be infinite."
+ "viewport znear must not be NaN."
+ "viewport znear must not be infinite."
+ "visibilityOptions must be a valid combination of MTL4VisibilityOptions."
+ "visibilityResultType"
+ "waitForDrawable:"
+ "waitForEvent:value:timeout:"
+ "waitForFence:beforeEncoderStages:"
+ "waitForVirtualSubstream must be called before any dispatches."
+ "waitOnCommandQueue:"
+ "width (%lu) * height (%lu) be <= 1024"
+ "width (%lu) must be > 0 and a power of two."
+ "wrapChildTensor:"
+ "wrapDynamicLibraries:"
+ "writeAccelerationStructureSerializationData:toBuffer:"
+ "writeAccelerationStructureTraversalDepth:toBuffer:"
+ "writeCompactedAccelerationStructureSize:toBuffer:"
+ "writeDeserializedAccelerationStructureSize:toBuffer:"
+ "writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:"
+ "writeSerializedAccelerationStructureSize:toBuffer:"
+ "writeTimestampIntoHeap:atIndex:"
+ "writeTimestampWithGranularity:afterStage:intoHeap:atIndex:"
+ "writeTimestampWithGranularity:intoHeap:atIndex:"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"
+ "{CheckerboardRenderTargetPipelineCache=\"_cacheLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"_library\"@\"<MTLLibrary>\"\"_vertexFunction\"@\"<MTLFunction>\"\"_depthStencilState\"[2@\"<MTLDepthStencilState>\"]\"_fConstants\"@\"MTLFunctionConstantValues\"\"_cache\"{unordered_map<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>, std::allocator<std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::__unordered_map_hasher<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>>, std::__unordered_map_equal<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::equal_to<MTLDebugCheckerboardFillHashKey>, MTLDebugCheckerboardFillHashKey::Hash>, std::allocator<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}}"
+ "{GPUDebugBufferDescriptorHeap=\"s\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_freeIndexList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"_bufferList\"{vector<MTLGPUDebugBuffer *, std::allocator<MTLGPUDebugBuffer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"_freeIndex\"Q\"_argumentEncoder\"@\"<MTLArgumentEncoder>\"\"_descriptorHeap\"@\"<MTLBuffer>\"}"
+ "{GPUDebugConstantBufferCache=\"_totalUsedMemory\"Q\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_cache\"{unordered_map<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value, GPUDebugConstantBufferCache::Key::Hash, std::equal_to<GPUDebugConstantBufferCache::Key>, std::allocator<std::pair<const GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>>>=\"__table_\"{__hash_table<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, std::__unordered_map_hasher<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, GPUDebugConstantBufferCache::Key::Hash, std::equal_to<GPUDebugConstantBufferCache::Key>>, std::__unordered_map_equal<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, std::equal_to<GPUDebugConstantBufferCache::Key>, GPUDebugConstantBufferCache::Key::Hash>, std::allocator<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"_device\"@\"MTLGPUDebugDevice\"}"
+ "{GlobalResidentBufferList=\"device\"@\"MTLGPUDebugDevice\"\"_iteration\"I\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_bufferList\"{list<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__end_\"{__list_node_base<id<MTLBuffer>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}}"
+ "{HeapUsageTable=\"_heapUsage\"Q\"_heapEntries\"{vector<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry, std::allocator<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>=\"__begin_\"^{HeapUsageTableEntry}\"__end_\"^{HeapUsageTableEntry}\"__cap_\"^{HeapUsageTableEntry}}}"
+ "{HeapUsageTable=\"_heapUsage\"Q\"_heapEntries\"{vector<HeapUsageTable::HeapUsageTableEntry, std::allocator<HeapUsageTable::HeapUsageTableEntry>>=\"__begin_\"^{HeapUsageTableEntry}\"__end_\"^{HeapUsageTableEntry}\"__cap_\"^{HeapUsageTableEntry}}}"
+ "{LegacySVBufferDescriptorHeap=\"s\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_freeIndexList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"_bufferList\"{vector<MTLLegacySVBuffer *, std::allocator<MTLLegacySVBuffer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"_freeIndex\"Q\"_argumentEncoder\"@\"<MTLArgumentEncoder>\"\"_descriptorHeap\"@\"<MTLBuffer>\"}"
+ "{LegacySVConstantBufferCache=\"_totalUsedMemory\"Q\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_cache\"{unordered_map<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>, std::allocator<std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>=\"__table_\"{__hash_table<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::__unordered_map_hasher<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>>, std::__unordered_map_equal<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::equal_to<LegacySVConstantBufferCache::Key>, LegacySVConstantBufferCache::Key::Hash>, std::allocator<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"_device\"@\"MTLLegacySVDevice\"}"
+ "{LegacySVGlobalResidentBufferList=\"_iteration\"I\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_bufferList\"{list<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__end_\"{__list_node_base<id<MTLBuffer>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}}"
+ "{LegacySVMetalBufferHeap=\"_mutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_buffers\"{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"_freeList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"_currentFreeIndex\"i\"_totalMemoryAllocated\"Q\"_totalMemoryInUse\"Q\"_bufferLength\"Q\"_device\"@\"MTLLegacySVDevice\"}"
+ "{MTL4DebugCommandEncoderState=\"canEndEncoding\"b1\"hasEndEncoding\"b1}"
+ "{MTL4DebugComputeCommandEncoderState=\"canSetComputePipelineState\"b1\"hasSetComputePipelineState\"b1\"hasEncodedCommandBufferJump\"b1\"isEncodingVirtualSubstream\"b1\"isEncodingCommandBufferJump\"b1}"
+ "{MTL4DebugRenderCommandEncoderState=\"canSetRenderPipelineState\"b1\"canSetViewport\"b1\"canSetVertexAmplificationFactor\"b1\"canSetCullMode\"b1\"canSetDepthClipMode\"b1\"canSetDepthBias\"b1\"canSetScissorRect\"b1\"canSetTriangleFillMode\"b1\"canSetBlendColor\"b1\"canSetDepthStencilState\"b1\"canSetStencilReferenceValue\"b1\"canSetVisibilityResultMode\"b1\"canSetFrontFacingWinding\"b1\"hasSetRenderPipelineState\"b1\"hasSetViewport\"b1\"hasSetVertexAmplificationFactor\"b1\"hasSetCullMode\"b1\"hasSetDepthClipMode\"b1\"hasSetDepthBias\"b1\"hasSetScissorRect\"b1\"hasSetTriangleFillMode\"b1\"hasSetBlendColor\"b1\"hasSetDepthStencilState\"b1\"hasSetStencilReferenceValue\"b1\"hasSetVisibilityResultMode\"b1\"hasSetFrontFacingWinding\"b1}"
+ "{MTL4DebugRenderPassInfo=\"resumingRenderPassDescriptor\"@\"MTL4RenderPassDescriptor\"\"suspendingRenderPassDescriptor\"@\"MTL4RenderPassDescriptor\"}"
+ "{MTL4DebugRenderPassInfo=@@}16@0:8"
+ "{MTLResourceID=Q}32@0:8@\"<MTLTexture>\"16Q24"
+ "{MTLResourceID=Q}32@0:8@16Q24"
+ "{MTLResourceID=Q}40@0:8@\"<MTLTexture>\"16@\"MTLTextureViewDescriptor\"24Q32"
+ "{MTLResourceID=Q}40@0:8@16@24Q32"
+ "{MTLResourceID=Q}48@0:8@\"<MTLResourceViewPool>\"16{_NSRange=QQ}24Q40"
+ "{MTLResourceID=Q}48@0:8@16{_NSRange=QQ}24Q40"
+ "{MTLResourceID=Q}56@0:8@\"<MTLBuffer>\"16@\"MTLTextureDescriptor\"24Q32Q40Q48"
+ "{MTLResourceID=Q}56@0:8@16@24Q32Q40Q48"
+ "{MTLSamplerDescriptorHashMap=\"_map\"{unordered_map<std::array<unsigned long long, 3>, unsigned int, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t, std::allocator<std::pair<const std::array<unsigned long long, 3>, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, std::__unordered_map_hasher<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t>, std::__unordered_map_equal<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::equal_t, MTLSamplerDescriptorHashMap::hash_t>, std::allocator<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"_limit\"I}"
+ "{MTLTelemetrySupportQueryStatRec=\"featureSetCount\"{unordered_map<std::string, unsigned int, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, unsigned int>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, unsigned int>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, unsigned int>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"texSampleCount\"{MTLTelemetryStatisticUIRec=\"min\"I\"max\"I\"total\"Q\"count\"I}}"
+ "{MetalBufferHeap=\"_mutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_buffers\"{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}\"_freeList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}\"_currentFreeIndex\"i\"_totalMemoryAllocated\"Q\"_totalMemoryInUse\"Q\"_bufferLength\"Q\"_device\"@\"MTLGPUDebugDevice\"}"
+ "{TextureTypeTable=\"_backingMemory\"@\"<MTLBuffer>\"\"_residencySet\"@\"<MTLResidencySet>\"}"
+ "{deque<id, std::allocator<id>>=\"__map_\"{__split_buffer<id *, std::allocator<id *>>=\"__first_\"^^@\"__begin_\"^^@\"__end_\"^^@\"__cap_\"^^@}\"__start_\"Q\"__size_\"Q}"
+ "{list<LegacySVResourceAndUsage, std::allocator<LegacySVResourceAndUsage>>=\"__end_\"{__list_node_base<LegacySVResourceAndUsage, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
+ "{list<id<MTLHeap>, std::allocator<id<MTLHeap>>>=\"__end_\"{__list_node_base<id<MTLHeap>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
+ "{list<resourceAndUsage, std::allocator<resourceAndUsage>>=\"__end_\"{__list_node_base<resourceAndUsage, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
+ "{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=\"__tree_\"{__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__tree_\"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{unordered_map<MTLPixelFormat, MTLTelemetryBlitDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<MTLPixelFormat, MTLTelemetryRenderTargetDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<MTLPixelFormat, MTLTelemetryTextureDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryTextureDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<SubView, unsigned long, SubView::hash_t, SubView::equal_t, std::allocator<std::pair<const SubView, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<SubView, unsigned long>, std::__unordered_map_hasher<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::hash_t, SubView::equal_t>, std::__unordered_map_equal<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::equal_t, SubView::hash_t>, std::allocator<std::__hash_value_type<SubView, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<std::string, MTLTelemetryStatisticUIRec, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, MTLTelemetryStatisticUIRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, MTLTelemetryComputePipelineUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryComputePipelineUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, MTLTelemetryKernelUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryKernelUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, MTLTelemetryRenderFuncUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryRenderFuncUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, MTLTelemetryRenderPipelineUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryRenderPipelineUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>={__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, NSString *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>=^v}Qf}}16@0:8"
+ "{unordered_map<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, (anonymous namespace)::EncoderResourceUsage, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, MTLGPUDebugResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, MTLLegacySVResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLLegacySVResidencySet *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_multiset<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>=\"__table_\"{__hash_table<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>=\"__table_\"{__hash_table<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>=\"__table_\"{__hash_table<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>=\"__table_\"{__hash_table<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__table_\"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>={unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<unsigned long long, void *> *>=^v}Qf}}16@0:8"
+ "{vector<(anonymous namespace)::ReportBufferEntry, std::allocator<(anonymous namespace)::ReportBufferEntry>>=\"__begin_\"^{ReportBufferEntry}\"__end_\"^{ReportBufferEntry}\"__cap_\"^{ReportBufferEntry}}"
+ "{vector<LegacySVMetalBuffer, std::allocator<LegacySVMetalBuffer>>=\"__begin_\"^{LegacySVMetalBuffer}\"__end_\"^{LegacySVMetalBuffer}\"__cap_\"^{LegacySVMetalBuffer}}"
+ "{vector<MTL4DebugBindingInfo, std::allocator<MTL4DebugBindingInfo>>=\"__begin_\"^{MTL4DebugBindingInfo}\"__end_\"^{MTL4DebugBindingInfo}\"__cap_\"^{MTL4DebugBindingInfo}}"
+ "{vector<MTLGPUDebugBuffer *, std::allocator<MTLGPUDebugBuffer *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<MTLScissorRect, std::allocator<MTLScissorRect>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<MTLViewport, std::allocator<MTLViewport>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<MetalBuffer, std::allocator<MetalBuffer>>=\"__begin_\"^{MetalBuffer}\"__end_\"^{MetalBuffer}\"__cap_\"^{MetalBuffer}}"
+ "{vector<MetalBuffer, std::allocator<MetalBuffer>>=^{MetalBuffer}^{MetalBuffer}^{MetalBuffer}}16@0:8"
+ "{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<id, std::allocator<id>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<id<MTLGPUDebugViewable>, std::allocator<id<MTLGPUDebugViewable>>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<std::pair<NSData *, unsigned long>, std::allocator<std::pair<NSData *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::pair<unsigned int, MTLTextureType>, std::allocator<std::pair<unsigned int, MTLTextureType>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
+ "{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>=\"__begin_\"^@?\"__end_\"^@?\"__cap_\"^@?}"
+ "{vector<void (^)(id<MTLIOCommandBuffer>), std::allocator<void (^)(id<MTLIOCommandBuffer>)>>=\"__begin_\"^@?\"__end_\"^@?\"__cap_\"^@?}"
+ "\xf0s"
- "%@ Function(%@): A sparse texture is being bound at index %lu to a shader argument with write access enabled. Sparse textures do not support writes from shaders."
- "@64@0:8@16@24@32Q40Q48Q56"
- "Invalid tile dimensions (%lu, %lu)"
- "MTLTextureUsageShaderWrite is not supported for MTLHeapTypeSparse on this platform"
- "Per pixel storage cannot be greater than 256B"
- "Per sample storage cannot be greater than 64B"
- "Q32@0:8@16Q24"
- "Sparse textures cannot be created with dual-plane texture formats"
- "T@\"<MTLBuffer>\",?"
- "T@\"MTLComputePipelineReflection\",R,N,V_reflection"
- "T@\"MTLRenderPipelineReflection\",R,N,V_reflection"
- "TQ,?"
- "The function handle for function '%s' was not created from the pipeline state that created this MTLVisibleFunctionTable."
- "Total allocated thread group memory (%lu) cannot be greater than (%lu)"
- "[4{TextureTypeTable=\"_backingMemory\"@\"<MTLBuffer>\"}]"
- "_reflection"
- "initWithBaseTexture:device:buffer:offset:bytesPerRow:"
- "initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:"
- "resourceTypeForTexture:stage:"
- "roundup2(threadsPerTile.width(%lu)) * roundup2(threadsPerTile.height(%lu)) * threadsPerTile.depth(%lu) must be <= %lu, both width and height are rounded up to nearest even number "
- "unwrapMTLRelocations:"
- "usageRequested 0x%lx != usageRequired 0x%lx"
- "validateRenderPassDescriptor"
- "validateTileDimensions"
- "{CheckerboardRenderTargetPipelineCache=\"_cacheLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"_library\"@\"<MTLLibrary>\"\"_vertexFunction\"@\"<MTLFunction>\"\"_depthStencilState\"[2@\"<MTLDepthStencilState>\"]\"_fConstants\"@\"MTLFunctionConstantValues\"\"_cache\"{unordered_map<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>, std::allocator<std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::__unordered_map_hasher<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>>, std::__unordered_map_equal<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::equal_to<MTLDebugCheckerboardFillHashKey>, MTLDebugCheckerboardFillHashKey::Hash>, std::allocator<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<MTLDebugCheckerboardFillHashKey, std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::equal_to<MTLDebugCheckerboardFillHashKey>, MTLDebugCheckerboardFillHashKey::Hash>>=\"__value_\"f}}}}"
- "{GPUDebugBufferDescriptorHeap=\"s\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_freeIndexList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}\"_bufferList\"{vector<MTLGPUDebugBuffer *, std::allocator<MTLGPUDebugBuffer *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<MTLGPUDebugBuffer **, std::allocator<MTLGPUDebugBuffer *>>=\"__value_\"^@}}\"_freeIndex\"Q\"_argumentEncoder\"@\"<MTLArgumentEncoder>\"\"_descriptorHeap\"@\"<MTLBuffer>\"}"
- "{GPUDebugConstantBufferCache=\"_totalUsedMemory\"Q\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_cache\"{unordered_map<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value, GPUDebugConstantBufferCache::Key::Hash, std::equal_to<GPUDebugConstantBufferCache::Key>, std::allocator<std::pair<const GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>>>=\"__table_\"{__hash_table<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, std::__unordered_map_hasher<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, GPUDebugConstantBufferCache::Key::Hash, std::equal_to<GPUDebugConstantBufferCache::Key>>, std::__unordered_map_equal<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, std::equal_to<GPUDebugConstantBufferCache::Key>, GPUDebugConstantBufferCache::Key::Hash>, std::allocator<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, GPUDebugConstantBufferCache::Key::Hash, std::equal_to<GPUDebugConstantBufferCache::Key>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<GPUDebugConstantBufferCache::Key, std::__hash_value_type<GPUDebugConstantBufferCache::Key, GPUDebugConstantBufferCache::Value>, std::equal_to<GPUDebugConstantBufferCache::Key>, GPUDebugConstantBufferCache::Key::Hash>>=\"__value_\"f}}}\"_device\"@\"MTLGPUDebugDevice\"}"
- "{GlobalResidentBufferList=\"_iteration\"I\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_bufferList\"{list<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__end_\"{__list_node_base<id<MTLBuffer>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<id<MTLBuffer>, void *>>>=\"__value_\"Q}}}"
- "{HeapUsageTable=\"_heapUsage\"Q\"_heapEntries\"{vector<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry, std::allocator<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>=\"__begin_\"^{HeapUsageTableEntry}\"__end_\"^{HeapUsageTableEntry}\"__end_cap_\"{__compressed_pair<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry *, std::allocator<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>=\"__value_\"^{HeapUsageTableEntry}}}}"
- "{HeapUsageTable=\"_heapUsage\"Q\"_heapEntries\"{vector<(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry, std::allocator<(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>=\"__begin_\"^{HeapUsageTableEntry}\"__end_\"^{HeapUsageTableEntry}\"__end_cap_\"{__compressed_pair<(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry *, std::allocator<(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>=\"__value_\"^{HeapUsageTableEntry}}}}"
- "{LegacySVBufferDescriptorHeap=\"s\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_freeIndexList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}\"_bufferList\"{vector<MTLLegacySVBuffer *, std::allocator<MTLLegacySVBuffer *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<MTLLegacySVBuffer **, std::allocator<MTLLegacySVBuffer *>>=\"__value_\"^@}}\"_freeIndex\"Q\"_argumentEncoder\"@\"<MTLArgumentEncoder>\"\"_descriptorHeap\"@\"<MTLBuffer>\"}"
- "{LegacySVConstantBufferCache=\"_totalUsedMemory\"Q\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_cache\"{unordered_map<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>, std::allocator<std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>=\"__table_\"{__hash_table<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::__unordered_map_hasher<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>>, std::__unordered_map_equal<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::equal_to<LegacySVConstantBufferCache::Key>, LegacySVConstantBufferCache::Key::Hash>, std::allocator<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<LegacySVConstantBufferCache::Key, std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::equal_to<LegacySVConstantBufferCache::Key>, LegacySVConstantBufferCache::Key::Hash>>=\"__value_\"f}}}\"_device\"@\"MTLLegacySVDevice\"}"
- "{LegacySVGlobalResidentBufferList=\"_iteration\"I\"_accessMutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_bufferList\"{list<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__end_\"{__list_node_base<id<MTLBuffer>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<id<MTLBuffer>, void *>>>=\"__value_\"Q}}}"
- "{LegacySVMetalBufferHeap=\"_mutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_buffers\"{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<id<MTLBuffer> *, std::allocator<id<MTLBuffer>>>=\"__value_\"^@}}\"_freeList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}\"_currentFreeIndex\"i\"_totalMemoryAllocated\"Q\"_totalMemoryInUse\"Q\"_bufferLength\"Q\"_device\"@\"MTLLegacySVDevice\"}"
- "{MTLGPUDebugBufferSubAlloc=\"buffer\"@\"<MTLBuffer>\"\"offset\"Q}"
- "{MTLSamplerDescriptorHashMap=\"_map\"{unordered_map<std::array<unsigned long long, 3>, unsigned int, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t, std::allocator<std::pair<const std::array<unsigned long long, 3>, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, std::__unordered_map_hasher<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t>, std::__unordered_map_equal<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::equal_t, MTLSamplerDescriptorHashMap::hash_t>, std::allocator<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::array<unsigned long long, 3>, std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::equal_t, MTLSamplerDescriptorHashMap::hash_t>>=\"__value_\"f}}}\"_limit\"I}"
- "{MTLTelemetrySupportQueryStatRec=\"featureSetCount\"{unordered_map<std::string, unsigned int, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, unsigned int>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, unsigned int>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, unsigned int>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, unsigned int>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, unsigned int>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}\"texSampleCount\"{MTLTelemetryStatisticUIRec=\"min\"I\"max\"I\"total\"Q\"count\"I}}"
- "{MetalBufferHeap=\"_mutex\"{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}\"_buffers\"{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<id<MTLBuffer> *, std::allocator<id<MTLBuffer>>>=\"__value_\"^@}}\"_freeList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}\"_currentFreeIndex\"i\"_totalMemoryAllocated\"Q\"_totalMemoryInUse\"Q\"_bufferLength\"Q\"_device\"@\"MTLGPUDebugDevice\"}"
- "{deque<id, std::allocator<id>>=\"__map_\"{__split_buffer<id *, std::allocator<id *>>=\"__first_\"^^@\"__begin_\"^^@\"__end_\"^^@\"__end_cap_\"{__compressed_pair<id **, std::allocator<id *>>=\"__value_\"^^@}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<id>>=\"__value_\"Q}}"
- "{list<LegacySVResourceAndUsage, std::allocator<LegacySVResourceAndUsage>>=\"__end_\"{__list_node_base<LegacySVResourceAndUsage, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<LegacySVResourceAndUsage, void *>>>=\"__value_\"Q}}"
- "{list<id<MTLHeap>, std::allocator<id<MTLHeap>>>=\"__end_\"{__list_node_base<id<MTLHeap>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<id<MTLHeap>, void *>>>=\"__value_\"Q}}"
- "{list<resourceAndUsage, std::allocator<resourceAndUsage>>=\"__end_\"{__list_node_base<resourceAndUsage, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<resourceAndUsage, void *>>>=\"__value_\"Q}}"
- "{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=\"__tree_\"{__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned int, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<unsigned int>>=\"__value_\"Q}}}"
- "{unordered_map<MTLPixelFormat, MTLTelemetryBlitDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{unordered_map<MTLPixelFormat, MTLTelemetryRenderTargetDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{unordered_map<MTLPixelFormat, MTLTelemetryTextureDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryTextureDistribution>>>=\"__table_\"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<MTLPixelFormat, std::__hash_value_type<MTLPixelFormat, MTLTelemetryTextureDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>>=\"__value_\"f}}}"
- "{unordered_map<SubView, unsigned long, SubView::hash_t, SubView::equal_t, std::allocator<std::pair<const SubView, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<SubView, unsigned long>, std::__unordered_map_hasher<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::hash_t, SubView::equal_t>, std::__unordered_map_equal<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::equal_t, SubView::hash_t>, std::allocator<std::__hash_value_type<SubView, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::hash_t, SubView::equal_t>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<SubView, std::__hash_value_type<SubView, unsigned long>, SubView::equal_t, SubView::hash_t>>=\"__value_\"f}}}"
- "{unordered_map<std::string, MTLTelemetryStatisticUIRec, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, MTLTelemetryStatisticUIRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, MTLTelemetryStatisticUIRec>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, MTLTelemetryComputePipelineUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryComputePipelineUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryComputePipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, MTLTelemetryKernelUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryKernelUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryKernelUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, MTLTelemetryRenderFuncUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryRenderFuncUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderFuncUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, MTLTelemetryRenderPipelineUsageRec, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, MTLTelemetryRenderPipelineUsageRec>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, MTLTelemetryRenderPipelineUsageRec>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unique_ptr<LegacySVArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned long, (anonymous namespace)::EncoderResourceUsage, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned long, MTLGPUDebugResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned long, MTLLegacySVResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLLegacySVResidencySet *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>>=\"__value_\"f}}}"
- "{unordered_multiset<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>=\"__table_\"{__hash_table<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *>, std::allocator<std::__hash_node<AttachmentDescriptorSimple, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, AttachmentDescriptorSimple::hash_t>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, AttachmentDescriptorSimple::equal_t>=\"__value_\"f}}}"
- "{unordered_set<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>=\"__table_\"{__hash_table<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *>, std::allocator<std::__hash_node<MTLDebugCommandBuffer *, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<MTLDebugCommandBuffer *>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<MTLDebugCommandBuffer *>>=\"__value_\"f}}}"
- "{unordered_set<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>=\"__table_\"{__hash_table<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *>, std::allocator<std::__hash_node<MTLToolsObject *, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<MTLToolsObject *>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<MTLToolsObject *>>=\"__value_\"f}}}"
- "{unordered_set<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>=\"__table_\"{__hash_table<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *>, std::allocator<std::__hash_node<id<MTLDebugResourcePurgeable>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<id<MTLDebugResourcePurgeable>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<id<MTLDebugResourcePurgeable>>>=\"__value_\"f}}}"
- "{vector<(anonymous namespace)::ReportBufferEntry, std::allocator<(anonymous namespace)::ReportBufferEntry>>=\"__begin_\"^{ReportBufferEntry}\"__end_\"^{ReportBufferEntry}\"__end_cap_\"{__compressed_pair<(anonymous namespace)::ReportBufferEntry *, std::allocator<(anonymous namespace)::ReportBufferEntry>>=\"__value_\"^{ReportBufferEntry}}}"
- "{vector<LegacySVMetalBuffer, std::allocator<LegacySVMetalBuffer>>=\"__begin_\"^{LegacySVMetalBuffer}\"__end_\"^{LegacySVMetalBuffer}\"__end_cap_\"{__compressed_pair<LegacySVMetalBuffer *, std::allocator<LegacySVMetalBuffer>>=\"__value_\"^{LegacySVMetalBuffer}}}"
- "{vector<MTLScissorRect, std::allocator<MTLScissorRect>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<MTLScissorRect *, std::allocator<MTLScissorRect>>=\"__value_\"^{?}}}"
- "{vector<MTLViewport, std::allocator<MTLViewport>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<MTLViewport *, std::allocator<MTLViewport>>=\"__value_\"^{?}}}"
- "{vector<MetalBuffer, std::allocator<MetalBuffer>>=\"__begin_\"^{MetalBuffer}\"__end_\"^{MetalBuffer}\"__end_cap_\"{__compressed_pair<MetalBuffer *, std::allocator<MetalBuffer>>=\"__value_\"^{MetalBuffer}}}"
- "{vector<NSString *, std::allocator<NSString *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<NSString **, std::allocator<NSString *>>=\"__value_\"^@}}"
- "{vector<id, std::allocator<id>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<id *, std::allocator<id>>=\"__value_\"^@}}"
- "{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<id<MTLBuffer> *, std::allocator<id<MTLBuffer>>>=\"__value_\"^@}}"
- "{vector<std::pair<NSData *, unsigned long>, std::allocator<std::pair<NSData *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<NSData *, unsigned long> *, std::allocator<std::pair<NSData *, unsigned long>>>=\"__value_\"^v}}"
- "{vector<std::pair<unsigned int, MTLTextureType>, std::allocator<std::pair<unsigned int, MTLTextureType>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<unsigned int, MTLTextureType> *, std::allocator<std::pair<unsigned int, MTLTextureType>>>=\"__value_\"^v}}"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}"
- "{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>=\"__begin_\"^@?\"__end_\"^@?\"__end_cap_\"{__compressed_pair<void (^*)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>=\"__value_\"^@?}}"
- "{vector<void (^)(id<MTLIOCommandBuffer>), std::allocator<void (^)(id<MTLIOCommandBuffer>)>>=\"__begin_\"^@?\"__end_\"^@?\"__end_cap_\"{__compressed_pair<void (^*)(id<MTLIOCommandBuffer>), std::allocator<void (^)(id<MTLIOCommandBuffer>)>>=\"__value_\"^@?}}"

```
