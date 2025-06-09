## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-304.7.0.0.0
-  __TEXT.__text: 0x1b9bd4
-  __TEXT.__auth_stubs: 0x1720
-  __TEXT.__objc_stubs: 0x137a0
-  __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0xd92c
-  __TEXT.__const: 0x7078
-  __TEXT.__cstring: 0x1deb4
-  __TEXT.__gcc_except_tab: 0x78c
-  __TEXT.__objc_classname: 0xf95
-  __TEXT.__objc_methname: 0x15b9f
-  __TEXT.__objc_methtype: 0x7887
-  __TEXT.__oslogstring: 0xf7d
+310.22.0.0.0
+  __TEXT.__text: 0x2614ec
+  __TEXT.__auth_stubs: 0x1780
+  __TEXT.__objc_stubs: 0x15d40
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__objc_methlist: 0x11f44
+  __TEXT.__const: 0x7950
+  __TEXT.__cstring: 0x26839
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__oslogstring: 0xedb
+  __TEXT.__objc_classname: 0x1536
+  __TEXT.__objc_methname: 0x192fb
+  __TEXT.__objc_methtype: 0x9ad3
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x2f58
-  __DATA_CONST.__auth_got: 0xba8
-  __DATA_CONST.__got: 0x6c0
+  __TEXT.__unwind_info: 0x3e20
+  __DATA_CONST.__auth_got: 0xbd8
+  __DATA_CONST.__got: 0x800
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1638
-  __DATA_CONST.__cfstring: 0x3c20
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__const: 0x1960
+  __DATA_CONST.__cfstring: 0x3ba0
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x300
+  __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x2f8
+  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x132c8
-  __DATA.__objc_selrefs: 0x5b78
-  __DATA.__objc_ivar: 0x7ac
-  __DATA.__objc_data: 0x1810
-  __DATA.__data: 0x2481
-  __DATA.__thread_vars: 0x60
-  __DATA.__thread_bss: 0x1058
-  __DATA.__bss: 0x300
-  __DATA.__common: 0x35
+  __DATA.__objc_const: 0x19440
+  __DATA.__objc_selrefs: 0x6760
+  __DATA.__objc_ivar: 0xa68
+  __DATA.__objc_data: 0x1e50
+  __DATA.__data: 0x3398
+  __DATA.__thread_vars: 0x48
+  __DATA.__thread_bss: 0x1018
+  __DATA.__bss: 0x4d8
+  __DATA.__common: 0x4d
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7FDB8252-E17C-3B33-B129-F36CC79FF271
-  Functions: 5715
-  Symbols:   34643
-  CStrings:  7656
+  UUID: D2F175D7-AB5C-3DE3-B15E-E7BBDE4EA7E7
+  Functions: 7616
+  Symbols:   45283
+  CStrings:  8895
 
Symbols:
+ -[CaptureMTL4Archive .cxx_destruct]
+ -[CaptureMTL4Archive baseObject]
+ -[CaptureMTL4Archive conformsToProtocol:]
+ -[CaptureMTL4Archive dealloc]
+ -[CaptureMTL4Archive description]
+ -[CaptureMTL4Archive forwardingTargetForSelector:]
+ -[CaptureMTL4Archive initWithBaseObject:captureContext:]
+ -[CaptureMTL4Archive label]
+ -[CaptureMTL4Archive newBinaryFunctionWithDescriptor:error:]
+ -[CaptureMTL4Archive originalObject]
+ -[CaptureMTL4Archive respondsToSelector:]
+ -[CaptureMTL4Archive setLabel:]
+ -[CaptureMTL4Archive streamReference]
+ -[CaptureMTL4Archive touch]
+ -[CaptureMTL4Archive traceContext]
+ -[CaptureMTL4Archive traceStream]
+ -[CaptureMTL4ArgumentTable .cxx_destruct]
+ -[CaptureMTL4ArgumentTable baseObject]
+ -[CaptureMTL4ArgumentTable conformsToProtocol:]
+ -[CaptureMTL4ArgumentTable dealloc]
+ -[CaptureMTL4ArgumentTable description]
+ -[CaptureMTL4ArgumentTable device]
+ -[CaptureMTL4ArgumentTable forwardingTargetForSelector:]
+ -[CaptureMTL4ArgumentTable initWithBaseObject:captureDevice:]
+ -[CaptureMTL4ArgumentTable label]
+ -[CaptureMTL4ArgumentTable originalObject]
+ -[CaptureMTL4ArgumentTable respondsToSelector:]
+ -[CaptureMTL4ArgumentTable setAddress:atIndex:]
+ -[CaptureMTL4ArgumentTable setResource:atBufferIndex:]
+ -[CaptureMTL4ArgumentTable setSamplerState:atIndex:]
+ -[CaptureMTL4ArgumentTable setTexture:atIndex:]
+ -[CaptureMTL4ArgumentTable streamReference]
+ -[CaptureMTL4ArgumentTable touch]
+ -[CaptureMTL4ArgumentTable traceContext]
+ -[CaptureMTL4ArgumentTable traceStream]
+ -[CaptureMTL4BinaryFunction .cxx_destruct]
+ -[CaptureMTL4BinaryFunction baseObject]
+ -[CaptureMTL4BinaryFunction conformsToProtocol:]
+ -[CaptureMTL4BinaryFunction dealloc]
+ -[CaptureMTL4BinaryFunction debugInstrumentationData]
+ -[CaptureMTL4BinaryFunction description]
+ -[CaptureMTL4BinaryFunction forwardingTargetForSelector:]
+ -[CaptureMTL4BinaryFunction functionType]
+ -[CaptureMTL4BinaryFunction initWithBaseObject:captureContext:]
+ -[CaptureMTL4BinaryFunction name]
+ -[CaptureMTL4BinaryFunction originalObject]
+ -[CaptureMTL4BinaryFunction reflection]
+ -[CaptureMTL4BinaryFunction relocations]
+ -[CaptureMTL4BinaryFunction respondsToSelector:]
+ -[CaptureMTL4BinaryFunction setRelocations:]
+ -[CaptureMTL4BinaryFunction streamReference]
+ -[CaptureMTL4BinaryFunction touch]
+ -[CaptureMTL4BinaryFunction traceContext]
+ -[CaptureMTL4BinaryFunction traceStream]
+ -[CaptureMTL4CommandAllocator .cxx_destruct]
+ -[CaptureMTL4CommandAllocator allocatedSize]
+ -[CaptureMTL4CommandAllocator baseObject]
+ -[CaptureMTL4CommandAllocator conformsToProtocol:]
+ -[CaptureMTL4CommandAllocator dealloc]
+ -[CaptureMTL4CommandAllocator description]
+ -[CaptureMTL4CommandAllocator device]
+ -[CaptureMTL4CommandAllocator forwardingTargetForSelector:]
+ -[CaptureMTL4CommandAllocator initWithBaseObject:captureDevice:]
+ -[CaptureMTL4CommandAllocator label]
+ -[CaptureMTL4CommandAllocator originalObject]
+ -[CaptureMTL4CommandAllocator reset]
+ -[CaptureMTL4CommandAllocator respondsToSelector:]
+ -[CaptureMTL4CommandAllocator streamReference]
+ -[CaptureMTL4CommandAllocator touch]
+ -[CaptureMTL4CommandAllocator traceContext]
+ -[CaptureMTL4CommandAllocator traceStream]
+ -[CaptureMTL4CommandBuffer .cxx_destruct]
+ -[CaptureMTL4CommandBuffer accelerationStructureCommandEncodingPreamble]
+ -[CaptureMTL4CommandBuffer accelerationStructureDescriptorProcessEventValue]
+ -[CaptureMTL4CommandBuffer accelerationStructureDescriptorProcessEvent]
+ -[CaptureMTL4CommandBuffer baseObject]
+ -[CaptureMTL4CommandBuffer beginCommandBufferWithAllocator:]
+ -[CaptureMTL4CommandBuffer beginCommandBufferWithAllocator:options:]
+ -[CaptureMTL4CommandBuffer computeCommandEncoder]
+ -[CaptureMTL4CommandBuffer conformsToProtocol:]
+ -[CaptureMTL4CommandBuffer currentGeneration]
+ -[CaptureMTL4CommandBuffer dealloc]
+ -[CaptureMTL4CommandBuffer description]
+ -[CaptureMTL4CommandBuffer device]
+ -[CaptureMTL4CommandBuffer endCommandBuffer]
+ -[CaptureMTL4CommandBuffer forwardingTargetForSelector:]
+ -[CaptureMTL4CommandBuffer initWithBaseObject:captureDevice:funcRef:]
+ -[CaptureMTL4CommandBuffer label]
+ -[CaptureMTL4CommandBuffer machineLearningCommandEncoder]
+ -[CaptureMTL4CommandBuffer originalObject]
+ -[CaptureMTL4CommandBuffer parentStream]
+ -[CaptureMTL4CommandBuffer popDebugGroup]
+ -[CaptureMTL4CommandBuffer pushDebugGroup:]
+ -[CaptureMTL4CommandBuffer renderCommandEncoderWithDescriptor:]
+ -[CaptureMTL4CommandBuffer renderCommandEncoderWithDescriptor:options:]
+ -[CaptureMTL4CommandBuffer respondsToSelector:]
+ -[CaptureMTL4CommandBuffer retainedObjects]
+ -[CaptureMTL4CommandBuffer sampledComputeCommandEncoder:capacity:]
+ -[CaptureMTL4CommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:]
+ -[CaptureMTL4CommandBuffer setLabel:]
+ -[CaptureMTL4CommandBuffer streamReference]
+ -[CaptureMTL4CommandBuffer touch]
+ -[CaptureMTL4CommandBuffer traceContext]
+ -[CaptureMTL4CommandBuffer traceStream]
+ -[CaptureMTL4CommandBuffer useResidencySet:]
+ -[CaptureMTL4CommandBuffer useResidencySets:count:]
+ -[CaptureMTL4CommandQueue .cxx_destruct]
+ -[CaptureMTL4CommandQueue _addRequestsToDownloadQueueForCommandBuffers:count:atIndex:]
+ -[CaptureMTL4CommandQueue _addScheduledTrigger:count:atIndex:]
+ -[CaptureMTL4CommandQueue _commitCommandBuffers:count:atIndex:]
+ -[CaptureMTL4CommandQueue _encodeDownloadPoint:]
+ -[CaptureMTL4CommandQueue _postCommit:count:]
+ -[CaptureMTL4CommandQueue _triggerCommit:count:atIndex:]
+ -[CaptureMTL4CommandQueue addResidencySet:]
+ -[CaptureMTL4CommandQueue addResidencySets:count:]
+ -[CaptureMTL4CommandQueue baseObject]
+ -[CaptureMTL4CommandQueue commit:count:]
+ -[CaptureMTL4CommandQueue commit:count:options:]
+ -[CaptureMTL4CommandQueue conformsToProtocol:]
+ -[CaptureMTL4CommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:]
+ -[CaptureMTL4CommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:]
+ -[CaptureMTL4CommandQueue dealloc]
+ -[CaptureMTL4CommandQueue description]
+ -[CaptureMTL4CommandQueue device]
+ -[CaptureMTL4CommandQueue forwardingTargetForSelector:]
+ -[CaptureMTL4CommandQueue initWithBaseObject:captureDevice:]
+ -[CaptureMTL4CommandQueue label]
+ -[CaptureMTL4CommandQueue lastCommittedCommandBufferGeneration]
+ -[CaptureMTL4CommandQueue lastCommittedCommandBuffer]
+ -[CaptureMTL4CommandQueue originalObject]
+ -[CaptureMTL4CommandQueue removeResidencySet:]
+ -[CaptureMTL4CommandQueue removeResidencySets:count:]
+ -[CaptureMTL4CommandQueue respondsToSelector:]
+ -[CaptureMTL4CommandQueue signalDrawable:]
+ -[CaptureMTL4CommandQueue signalEvent:value:]
+ -[CaptureMTL4CommandQueue streamReference]
+ -[CaptureMTL4CommandQueue touch]
+ -[CaptureMTL4CommandQueue traceContext]
+ -[CaptureMTL4CommandQueue traceStream]
+ -[CaptureMTL4CommandQueue updateBufferMappings:heap:operations:count:]
+ -[CaptureMTL4CommandQueue updateTextureMappings:heap:operations:count:]
+ -[CaptureMTL4CommandQueue waitForDrawable:]
+ -[CaptureMTL4CommandQueue waitForEvent:value:]
+ -[CaptureMTL4Compiler .cxx_destruct]
+ -[CaptureMTL4Compiler baseObject]
+ -[CaptureMTL4Compiler cancel]
+ -[CaptureMTL4Compiler captureDevice]
+ -[CaptureMTL4Compiler conformsToProtocol:]
+ -[CaptureMTL4Compiler dealloc]
+ -[CaptureMTL4Compiler description]
+ -[CaptureMTL4Compiler device]
+ -[CaptureMTL4Compiler forwardingTargetForSelector:]
+ -[CaptureMTL4Compiler initWithBaseObject:captureDevice:]
+ -[CaptureMTL4Compiler label]
+ -[CaptureMTL4Compiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[CaptureMTL4Compiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[CaptureMTL4Compiler newDynamicLibrary:error:]
+ -[CaptureMTL4Compiler newDynamicLibraryWithURL:error:]
+ -[CaptureMTL4Compiler newLibraryWithDescriptor:error:]
+ -[CaptureMTL4Compiler newMachineLearningPipelineStateWithDescriptor:error:]
+ -[CaptureMTL4Compiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:]
+ -[CaptureMTL4Compiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:]
+ -[CaptureMTL4Compiler originalObject]
+ -[CaptureMTL4Compiler pipelineDataSetSerializer]
+ -[CaptureMTL4Compiler respondsToSelector:]
+ -[CaptureMTL4Compiler streamReference]
+ -[CaptureMTL4Compiler touch]
+ -[CaptureMTL4Compiler traceContext]
+ -[CaptureMTL4Compiler traceStream]
+ -[CaptureMTL4ComputeCommandEncoder .cxx_destruct]
+ -[CaptureMTL4ComputeCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[CaptureMTL4ComputeCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[CaptureMTL4ComputeCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[CaptureMTL4ComputeCommandEncoder baseObject]
+ -[CaptureMTL4ComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder captureDevice]
+ -[CaptureMTL4ComputeCommandEncoder commandBuffer]
+ -[CaptureMTL4ComputeCommandEncoder conformsToProtocol:]
+ -[CaptureMTL4ComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:]
+ -[CaptureMTL4ComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:]
+ -[CaptureMTL4ComputeCommandEncoder copyFromTexture:toTexture:]
+ -[CaptureMTL4ComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:]
+ -[CaptureMTL4ComputeCommandEncoder dealloc]
+ -[CaptureMTL4ComputeCommandEncoder description]
+ -[CaptureMTL4ComputeCommandEncoder descriptorDownloader]
+ -[CaptureMTL4ComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:]
+ -[CaptureMTL4ComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:]
+ -[CaptureMTL4ComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:]
+ -[CaptureMTL4ComputeCommandEncoder dispatchThreadsWithIndirectBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder endEncodingAndRetrieveProgramAddressTable]
+ -[CaptureMTL4ComputeCommandEncoder endEncoding]
+ -[CaptureMTL4ComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder executeCommandsInBuffer:withRange:]
+ -[CaptureMTL4ComputeCommandEncoder fillBuffer:range:pattern4:]
+ -[CaptureMTL4ComputeCommandEncoder fillBuffer:range:value:]
+ -[CaptureMTL4ComputeCommandEncoder fillTexture:level:slice:region:bytes:length:]
+ -[CaptureMTL4ComputeCommandEncoder fillTexture:level:slice:region:color:]
+ -[CaptureMTL4ComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:]
+ -[CaptureMTL4ComputeCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:]
+ -[CaptureMTL4ComputeCommandEncoder forwardingTargetForSelector:]
+ -[CaptureMTL4ComputeCommandEncoder generateMipmapsForTexture:]
+ -[CaptureMTL4ComputeCommandEncoder initWithBaseObject:captureCommandBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder insertDebugSignpost:]
+ -[CaptureMTL4ComputeCommandEncoder label]
+ -[CaptureMTL4ComputeCommandEncoder optimizeContentsForCPUAccess:]
+ -[CaptureMTL4ComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:]
+ -[CaptureMTL4ComputeCommandEncoder optimizeContentsForGPUAccess:]
+ -[CaptureMTL4ComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:]
+ -[CaptureMTL4ComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:]
+ -[CaptureMTL4ComputeCommandEncoder originalObject]
+ -[CaptureMTL4ComputeCommandEncoder popDebugGroup]
+ -[CaptureMTL4ComputeCommandEncoder pushDebugGroup:]
+ -[CaptureMTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:]
+ -[CaptureMTL4ComputeCommandEncoder resetCommandsInBuffer:withRange:]
+ -[CaptureMTL4ComputeCommandEncoder respondsToSelector:]
+ -[CaptureMTL4ComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder setArgumentTable:]
+ -[CaptureMTL4ComputeCommandEncoder setComputePipelineState:]
+ -[CaptureMTL4ComputeCommandEncoder setImageblockWidth:height:]
+ -[CaptureMTL4ComputeCommandEncoder setLabel:]
+ -[CaptureMTL4ComputeCommandEncoder setThreadgroupMemoryLength:atIndex:]
+ -[CaptureMTL4ComputeCommandEncoder streamReference]
+ -[CaptureMTL4ComputeCommandEncoder touch]
+ -[CaptureMTL4ComputeCommandEncoder traceContext]
+ -[CaptureMTL4ComputeCommandEncoder traceStream]
+ -[CaptureMTL4ComputeCommandEncoder updateFence:afterEncoderStages:]
+ -[CaptureMTL4ComputeCommandEncoder waitForFence:beforeEncoderStages:]
+ -[CaptureMTL4ComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:]
+ -[CaptureMTL4ComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:]
+ -[CaptureMTL4ComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:]
+ -[CaptureMTL4ComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:]
+ -[CaptureMTL4FXFrameInterpolator .cxx_destruct]
+ -[CaptureMTL4FXFrameInterpolator aspectRatio]
+ -[CaptureMTL4FXFrameInterpolator baseObject]
+ -[CaptureMTL4FXFrameInterpolator colorTextureBarrierStages]
+ -[CaptureMTL4FXFrameInterpolator colorTextureFormat]
+ -[CaptureMTL4FXFrameInterpolator colorTextureUsage]
+ -[CaptureMTL4FXFrameInterpolator colorTexture]
+ -[CaptureMTL4FXFrameInterpolator conformsToProtocol:]
+ -[CaptureMTL4FXFrameInterpolator dealloc]
+ -[CaptureMTL4FXFrameInterpolator debugTexture]
+ -[CaptureMTL4FXFrameInterpolator deltaTime]
+ -[CaptureMTL4FXFrameInterpolator depthTextureFormat]
+ -[CaptureMTL4FXFrameInterpolator depthTextureUsage]
+ -[CaptureMTL4FXFrameInterpolator depthTexture]
+ -[CaptureMTL4FXFrameInterpolator description]
+ -[CaptureMTL4FXFrameInterpolator encodeToCommandBuffer:]
+ -[CaptureMTL4FXFrameInterpolator farPlane]
+ -[CaptureMTL4FXFrameInterpolator fence]
+ -[CaptureMTL4FXFrameInterpolator fieldOfView]
+ -[CaptureMTL4FXFrameInterpolator forwardingTargetForSelector:]
+ -[CaptureMTL4FXFrameInterpolator initWithBaseObject:captureDevice:captureCompiler:]
+ -[CaptureMTL4FXFrameInterpolator inputHeight]
+ -[CaptureMTL4FXFrameInterpolator inputWidth]
+ -[CaptureMTL4FXFrameInterpolator isDepthReversed]
+ -[CaptureMTL4FXFrameInterpolator isUITextureComposited]
+ -[CaptureMTL4FXFrameInterpolator jitterOffsetX]
+ -[CaptureMTL4FXFrameInterpolator jitterOffsetY]
+ -[CaptureMTL4FXFrameInterpolator motionTextureFormat]
+ -[CaptureMTL4FXFrameInterpolator motionTextureUsage]
+ -[CaptureMTL4FXFrameInterpolator motionTexture]
+ -[CaptureMTL4FXFrameInterpolator motionVectorScaleX]
+ -[CaptureMTL4FXFrameInterpolator motionVectorScaleY]
+ -[CaptureMTL4FXFrameInterpolator nearPlane]
+ -[CaptureMTL4FXFrameInterpolator originalObject]
+ -[CaptureMTL4FXFrameInterpolator outputHeight]
+ -[CaptureMTL4FXFrameInterpolator outputTextureBarrierStages]
+ -[CaptureMTL4FXFrameInterpolator outputTextureFormat]
+ -[CaptureMTL4FXFrameInterpolator outputTextureUsage]
+ -[CaptureMTL4FXFrameInterpolator outputTexture]
+ -[CaptureMTL4FXFrameInterpolator outputWidth]
+ -[CaptureMTL4FXFrameInterpolator prevColorTexture]
+ -[CaptureMTL4FXFrameInterpolator reset]
+ -[CaptureMTL4FXFrameInterpolator respondsToSelector:]
+ -[CaptureMTL4FXFrameInterpolator setAspectRatio:]
+ -[CaptureMTL4FXFrameInterpolator setColorTexture:]
+ -[CaptureMTL4FXFrameInterpolator setColorTextureBarrierStages:]
+ -[CaptureMTL4FXFrameInterpolator setDebugTexture:]
+ -[CaptureMTL4FXFrameInterpolator setDeltaTime:]
+ -[CaptureMTL4FXFrameInterpolator setDepthReversed:]
+ -[CaptureMTL4FXFrameInterpolator setDepthTexture:]
+ -[CaptureMTL4FXFrameInterpolator setFarPlane:]
+ -[CaptureMTL4FXFrameInterpolator setFence:]
+ -[CaptureMTL4FXFrameInterpolator setFieldOfView:]
+ -[CaptureMTL4FXFrameInterpolator setIsUITextureComposited:]
+ -[CaptureMTL4FXFrameInterpolator setJitterOffsetX:]
+ -[CaptureMTL4FXFrameInterpolator setJitterOffsetY:]
+ -[CaptureMTL4FXFrameInterpolator setMotionTexture:]
+ -[CaptureMTL4FXFrameInterpolator setMotionVectorScaleX:]
+ -[CaptureMTL4FXFrameInterpolator setMotionVectorScaleY:]
+ -[CaptureMTL4FXFrameInterpolator setNearPlane:]
+ -[CaptureMTL4FXFrameInterpolator setOutputTexture:]
+ -[CaptureMTL4FXFrameInterpolator setPrevColorTexture:]
+ -[CaptureMTL4FXFrameInterpolator setShouldResetHistory:]
+ -[CaptureMTL4FXFrameInterpolator setUITexture:]
+ -[CaptureMTL4FXFrameInterpolator shouldResetHistory]
+ -[CaptureMTL4FXFrameInterpolator streamReference]
+ -[CaptureMTL4FXFrameInterpolator touch]
+ -[CaptureMTL4FXFrameInterpolator traceContext]
+ -[CaptureMTL4FXFrameInterpolator traceStream]
+ -[CaptureMTL4FXFrameInterpolator uiTextureFormat]
+ -[CaptureMTL4FXFrameInterpolator uiTexture]
+ -[CaptureMTL4FXSpatialScaler .cxx_destruct]
+ -[CaptureMTL4FXSpatialScaler baseObject]
+ -[CaptureMTL4FXSpatialScaler colorProcessingMode]
+ -[CaptureMTL4FXSpatialScaler colorTextureBarrierStages]
+ -[CaptureMTL4FXSpatialScaler colorTextureFormat]
+ -[CaptureMTL4FXSpatialScaler colorTextureUsage]
+ -[CaptureMTL4FXSpatialScaler colorTexture]
+ -[CaptureMTL4FXSpatialScaler conformsToProtocol:]
+ -[CaptureMTL4FXSpatialScaler dealloc]
+ -[CaptureMTL4FXSpatialScaler debugTexture]
+ -[CaptureMTL4FXSpatialScaler description]
+ -[CaptureMTL4FXSpatialScaler encodeToCommandBuffer:]
+ -[CaptureMTL4FXSpatialScaler fence]
+ -[CaptureMTL4FXSpatialScaler forwardingTargetForSelector:]
+ -[CaptureMTL4FXSpatialScaler initWithBaseObject:captureDevice:captureCompiler:]
+ -[CaptureMTL4FXSpatialScaler inputContentHeight]
+ -[CaptureMTL4FXSpatialScaler inputContentWidth]
+ -[CaptureMTL4FXSpatialScaler inputHeight]
+ -[CaptureMTL4FXSpatialScaler inputWidth]
+ -[CaptureMTL4FXSpatialScaler originalObject]
+ -[CaptureMTL4FXSpatialScaler outputHeight]
+ -[CaptureMTL4FXSpatialScaler outputTextureBarrierStages]
+ -[CaptureMTL4FXSpatialScaler outputTextureFormat]
+ -[CaptureMTL4FXSpatialScaler outputTextureUsage]
+ -[CaptureMTL4FXSpatialScaler outputTexture]
+ -[CaptureMTL4FXSpatialScaler outputWidth]
+ -[CaptureMTL4FXSpatialScaler respondsToSelector:]
+ -[CaptureMTL4FXSpatialScaler setColorTexture:]
+ -[CaptureMTL4FXSpatialScaler setColorTextureBarrierStages:]
+ -[CaptureMTL4FXSpatialScaler setDebugTexture:]
+ -[CaptureMTL4FXSpatialScaler setFence:]
+ -[CaptureMTL4FXSpatialScaler setInputContentHeight:]
+ -[CaptureMTL4FXSpatialScaler setInputContentWidth:]
+ -[CaptureMTL4FXSpatialScaler setOutputTexture:]
+ -[CaptureMTL4FXSpatialScaler streamReference]
+ -[CaptureMTL4FXSpatialScaler touch]
+ -[CaptureMTL4FXSpatialScaler traceContext]
+ -[CaptureMTL4FXSpatialScaler traceStream]
+ -[CaptureMTL4FXTemporalDenoisedScaler .cxx_destruct]
+ -[CaptureMTL4FXTemporalDenoisedScaler baseObject]
+ -[CaptureMTL4FXTemporalDenoisedScaler colorTextureBarrierStages]
+ -[CaptureMTL4FXTemporalDenoisedScaler colorTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler colorTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler colorTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler conformsToProtocol:]
+ -[CaptureMTL4FXTemporalDenoisedScaler dealloc]
+ -[CaptureMTL4FXTemporalDenoisedScaler debugTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler denoiseStrengthMaskTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler depthTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler depthTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler depthTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler description]
+ -[CaptureMTL4FXTemporalDenoisedScaler diffuseAlbedoTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler diffuseAlbedoTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler diffuseAlbedoTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler dilatedMotionVectors]
+ -[CaptureMTL4FXTemporalDenoisedScaler encodeToCommandBuffer:]
+ -[CaptureMTL4FXTemporalDenoisedScaler exposureTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler fence]
+ -[CaptureMTL4FXTemporalDenoisedScaler forwardingTargetForSelector:]
+ -[CaptureMTL4FXTemporalDenoisedScaler initWithBaseObject:captureDevice:captureCompiler:]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputContentHeight]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputContentMaxScale]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputContentMinScale]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputContentWidth]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputHeight]
+ -[CaptureMTL4FXTemporalDenoisedScaler inputWidth]
+ -[CaptureMTL4FXTemporalDenoisedScaler isDepthReversed]
+ -[CaptureMTL4FXTemporalDenoisedScaler jitterOffsetX]
+ -[CaptureMTL4FXTemporalDenoisedScaler jitterOffsetY]
+ -[CaptureMTL4FXTemporalDenoisedScaler motionTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler motionTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler motionTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler motionVectorScaleX]
+ -[CaptureMTL4FXTemporalDenoisedScaler motionVectorScaleY]
+ -[CaptureMTL4FXTemporalDenoisedScaler normalTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler normalTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler normalTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler originalObject]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputHeight]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputTextureBarrierStages]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler outputWidth]
+ -[CaptureMTL4FXTemporalDenoisedScaler preExposure]
+ -[CaptureMTL4FXTemporalDenoisedScaler reactiveMaskTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler reactiveMaskTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler reactiveTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler reset]
+ -[CaptureMTL4FXTemporalDenoisedScaler respondsToSelector:]
+ -[CaptureMTL4FXTemporalDenoisedScaler roughnessTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler roughnessTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler roughnessTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler setColorTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setColorTextureBarrierStages:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setDebugTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setDenoiseStrengthMaskTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setDepthReversed:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setDepthTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setDiffuseAlbedoTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setExposureTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setFence:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setInputContentHeight:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setInputContentWidth:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setJitterOffsetX:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setJitterOffsetY:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setMotionTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setMotionVectorScaleX:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setMotionVectorScaleY:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setNormalTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setOutputTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setPreExposure:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setReactiveMaskTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setRoughnessTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setShouldResetHistory:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setSpecularAlbedoTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setSpecularHitDistanceTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setTransparencyOverlayTexture:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setViewToClipMatrix:]
+ -[CaptureMTL4FXTemporalDenoisedScaler setWorldToViewMatrix:]
+ -[CaptureMTL4FXTemporalDenoisedScaler shouldResetHistory]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularAlbedoTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularAlbedoTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularAlbedoTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularHitDistanceTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularHitDistanceTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler specularHitDistanceTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler streamReference]
+ -[CaptureMTL4FXTemporalDenoisedScaler touch]
+ -[CaptureMTL4FXTemporalDenoisedScaler traceContext]
+ -[CaptureMTL4FXTemporalDenoisedScaler traceStream]
+ -[CaptureMTL4FXTemporalDenoisedScaler transparencyOverlayTextureFormat]
+ -[CaptureMTL4FXTemporalDenoisedScaler transparencyOverlayTextureUsage]
+ -[CaptureMTL4FXTemporalDenoisedScaler transparencyOverlayTexture]
+ -[CaptureMTL4FXTemporalDenoisedScaler viewToClipMatrix]
+ -[CaptureMTL4FXTemporalDenoisedScaler worldToViewMatrix]
+ -[CaptureMTL4FXTemporalScaler .cxx_destruct]
+ -[CaptureMTL4FXTemporalScaler baseObject]
+ -[CaptureMTL4FXTemporalScaler colorTextureBarrierStages]
+ -[CaptureMTL4FXTemporalScaler colorTextureFormat]
+ -[CaptureMTL4FXTemporalScaler colorTextureUsage]
+ -[CaptureMTL4FXTemporalScaler colorTexture]
+ -[CaptureMTL4FXTemporalScaler conformsToProtocol:]
+ -[CaptureMTL4FXTemporalScaler currentViewToClipMatrix]
+ -[CaptureMTL4FXTemporalScaler currentWorldToViewMatrix]
+ -[CaptureMTL4FXTemporalScaler dealloc]
+ -[CaptureMTL4FXTemporalScaler debugTexture]
+ -[CaptureMTL4FXTemporalScaler depthTextureFormat]
+ -[CaptureMTL4FXTemporalScaler depthTextureUsage]
+ -[CaptureMTL4FXTemporalScaler depthTexture]
+ -[CaptureMTL4FXTemporalScaler description]
+ -[CaptureMTL4FXTemporalScaler dilatedMotionVectors]
+ -[CaptureMTL4FXTemporalScaler encodeToCommandBuffer:]
+ -[CaptureMTL4FXTemporalScaler executionMode]
+ -[CaptureMTL4FXTemporalScaler exposureTexture]
+ -[CaptureMTL4FXTemporalScaler fence]
+ -[CaptureMTL4FXTemporalScaler forwardingTargetForSelector:]
+ -[CaptureMTL4FXTemporalScaler initWithBaseObject:captureDevice:captureCompiler:]
+ -[CaptureMTL4FXTemporalScaler inputContentHeight]
+ -[CaptureMTL4FXTemporalScaler inputContentMaxScale]
+ -[CaptureMTL4FXTemporalScaler inputContentMinScale]
+ -[CaptureMTL4FXTemporalScaler inputContentWidth]
+ -[CaptureMTL4FXTemporalScaler inputHeight]
+ -[CaptureMTL4FXTemporalScaler inputWidth]
+ -[CaptureMTL4FXTemporalScaler isDepthReversed]
+ -[CaptureMTL4FXTemporalScaler jitterOffsetX]
+ -[CaptureMTL4FXTemporalScaler jitterOffsetY]
+ -[CaptureMTL4FXTemporalScaler motionTextureFormat]
+ -[CaptureMTL4FXTemporalScaler motionTextureUsage]
+ -[CaptureMTL4FXTemporalScaler motionTexture]
+ -[CaptureMTL4FXTemporalScaler motionVectorScaleX]
+ -[CaptureMTL4FXTemporalScaler motionVectorScaleY]
+ -[CaptureMTL4FXTemporalScaler originalObject]
+ -[CaptureMTL4FXTemporalScaler outputHeight]
+ -[CaptureMTL4FXTemporalScaler outputTextureBarrierStages]
+ -[CaptureMTL4FXTemporalScaler outputTextureFormat]
+ -[CaptureMTL4FXTemporalScaler outputTextureUsage]
+ -[CaptureMTL4FXTemporalScaler outputTexture]
+ -[CaptureMTL4FXTemporalScaler outputWidth]
+ -[CaptureMTL4FXTemporalScaler preExposure]
+ -[CaptureMTL4FXTemporalScaler previousJitterOffset]
+ -[CaptureMTL4FXTemporalScaler previousViewToClipMatrix]
+ -[CaptureMTL4FXTemporalScaler previousWorldToViewMatrix]
+ -[CaptureMTL4FXTemporalScaler reactiveMaskTextureFormat]
+ -[CaptureMTL4FXTemporalScaler reactiveMaskTexture]
+ -[CaptureMTL4FXTemporalScaler reactiveTextureUsage]
+ -[CaptureMTL4FXTemporalScaler reset]
+ -[CaptureMTL4FXTemporalScaler respondsToSelector:]
+ -[CaptureMTL4FXTemporalScaler setColorTexture:]
+ -[CaptureMTL4FXTemporalScaler setColorTextureBarrierStages:]
+ -[CaptureMTL4FXTemporalScaler setCurrentViewToClipMatrix:]
+ -[CaptureMTL4FXTemporalScaler setCurrentWorldToViewMatrix:]
+ -[CaptureMTL4FXTemporalScaler setDebugTexture:]
+ -[CaptureMTL4FXTemporalScaler setDepthReversed:]
+ -[CaptureMTL4FXTemporalScaler setDepthTexture:]
+ -[CaptureMTL4FXTemporalScaler setExposureTexture:]
+ -[CaptureMTL4FXTemporalScaler setFence:]
+ -[CaptureMTL4FXTemporalScaler setInputContentHeight:]
+ -[CaptureMTL4FXTemporalScaler setInputContentWidth:]
+ -[CaptureMTL4FXTemporalScaler setJitterOffsetX:]
+ -[CaptureMTL4FXTemporalScaler setJitterOffsetY:]
+ -[CaptureMTL4FXTemporalScaler setMotionTexture:]
+ -[CaptureMTL4FXTemporalScaler setMotionVectorScaleX:]
+ -[CaptureMTL4FXTemporalScaler setMotionVectorScaleY:]
+ -[CaptureMTL4FXTemporalScaler setOutputTexture:]
+ -[CaptureMTL4FXTemporalScaler setPreExposure:]
+ -[CaptureMTL4FXTemporalScaler setPreviousJitterOffset:]
+ -[CaptureMTL4FXTemporalScaler setPreviousViewToClipMatrix:]
+ -[CaptureMTL4FXTemporalScaler setPreviousWorldToViewMatrix:]
+ -[CaptureMTL4FXTemporalScaler setReactiveMaskTexture:]
+ -[CaptureMTL4FXTemporalScaler setReset:]
+ -[CaptureMTL4FXTemporalScaler streamReference]
+ -[CaptureMTL4FXTemporalScaler touch]
+ -[CaptureMTL4FXTemporalScaler traceContext]
+ -[CaptureMTL4FXTemporalScaler traceStream]
+ -[CaptureMTL4MachineLearningCommandEncoder .cxx_destruct]
+ -[CaptureMTL4MachineLearningCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[CaptureMTL4MachineLearningCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[CaptureMTL4MachineLearningCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[CaptureMTL4MachineLearningCommandEncoder baseObject]
+ -[CaptureMTL4MachineLearningCommandEncoder commandBuffer]
+ -[CaptureMTL4MachineLearningCommandEncoder conformsToProtocol:]
+ -[CaptureMTL4MachineLearningCommandEncoder dealloc]
+ -[CaptureMTL4MachineLearningCommandEncoder description]
+ -[CaptureMTL4MachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:]
+ -[CaptureMTL4MachineLearningCommandEncoder endEncodingAndRetrieveProgramAddressTable]
+ -[CaptureMTL4MachineLearningCommandEncoder endEncoding]
+ -[CaptureMTL4MachineLearningCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:]
+ -[CaptureMTL4MachineLearningCommandEncoder forwardingTargetForSelector:]
+ -[CaptureMTL4MachineLearningCommandEncoder initWithBaseObject:captureCommandBuffer:]
+ -[CaptureMTL4MachineLearningCommandEncoder insertDebugSignpost:]
+ -[CaptureMTL4MachineLearningCommandEncoder label]
+ -[CaptureMTL4MachineLearningCommandEncoder originalObject]
+ -[CaptureMTL4MachineLearningCommandEncoder popDebugGroup]
+ -[CaptureMTL4MachineLearningCommandEncoder pushDebugGroup:]
+ -[CaptureMTL4MachineLearningCommandEncoder respondsToSelector:]
+ -[CaptureMTL4MachineLearningCommandEncoder setArgumentTable:]
+ -[CaptureMTL4MachineLearningCommandEncoder setLabel:]
+ -[CaptureMTL4MachineLearningCommandEncoder setPipelineState:]
+ -[CaptureMTL4MachineLearningCommandEncoder streamReference]
+ -[CaptureMTL4MachineLearningCommandEncoder touch]
+ -[CaptureMTL4MachineLearningCommandEncoder traceContext]
+ -[CaptureMTL4MachineLearningCommandEncoder traceStream]
+ -[CaptureMTL4MachineLearningCommandEncoder updateFence:afterEncoderStages:]
+ -[CaptureMTL4MachineLearningCommandEncoder waitForFence:beforeEncoderStages:]
+ -[CaptureMTL4MachineLearningPipelineState .cxx_destruct]
+ -[CaptureMTL4MachineLearningPipelineState allocatedSize]
+ -[CaptureMTL4MachineLearningPipelineState baseObject]
+ -[CaptureMTL4MachineLearningPipelineState conformsToProtocol:]
+ -[CaptureMTL4MachineLearningPipelineState dealloc]
+ -[CaptureMTL4MachineLearningPipelineState description]
+ -[CaptureMTL4MachineLearningPipelineState device]
+ -[CaptureMTL4MachineLearningPipelineState forwardingTargetForSelector:]
+ -[CaptureMTL4MachineLearningPipelineState initWithBaseObject:descriptor:captureCompiler:]
+ -[CaptureMTL4MachineLearningPipelineState intermediatesHeapSize]
+ -[CaptureMTL4MachineLearningPipelineState label]
+ -[CaptureMTL4MachineLearningPipelineState originalObject]
+ -[CaptureMTL4MachineLearningPipelineState reflection]
+ -[CaptureMTL4MachineLearningPipelineState respondsToSelector:]
+ -[CaptureMTL4MachineLearningPipelineState streamReference]
+ -[CaptureMTL4MachineLearningPipelineState touch]
+ -[CaptureMTL4MachineLearningPipelineState traceContext]
+ -[CaptureMTL4MachineLearningPipelineState traceStream]
+ -[CaptureMTL4PipelineDataSetSerializer .cxx_destruct]
+ -[CaptureMTL4PipelineDataSetSerializer baseObject]
+ -[CaptureMTL4PipelineDataSetSerializer conformsToProtocol:]
+ -[CaptureMTL4PipelineDataSetSerializer dealloc]
+ -[CaptureMTL4PipelineDataSetSerializer description]
+ -[CaptureMTL4PipelineDataSetSerializer forwardingTargetForSelector:]
+ -[CaptureMTL4PipelineDataSetSerializer initWithBaseObject:captureContext:]
+ -[CaptureMTL4PipelineDataSetSerializer originalObject]
+ -[CaptureMTL4PipelineDataSetSerializer respondsToSelector:]
+ -[CaptureMTL4PipelineDataSetSerializer serializeAsArchiveAndFlushToURL:error:]
+ -[CaptureMTL4PipelineDataSetSerializer serializeAsPipelinesScriptWithError:]
+ -[CaptureMTL4PipelineDataSetSerializer streamReference]
+ -[CaptureMTL4PipelineDataSetSerializer touch]
+ -[CaptureMTL4PipelineDataSetSerializer traceContext]
+ -[CaptureMTL4PipelineDataSetSerializer traceStream]
+ -[CaptureMTL4RenderCommandEncoder .cxx_destruct]
+ -[CaptureMTL4RenderCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:]
+ -[CaptureMTL4RenderCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:]
+ -[CaptureMTL4RenderCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:]
+ -[CaptureMTL4RenderCommandEncoder baseObject]
+ -[CaptureMTL4RenderCommandEncoder commandBuffer]
+ -[CaptureMTL4RenderCommandEncoder conformsToProtocol:]
+ -[CaptureMTL4RenderCommandEncoder dealloc]
+ -[CaptureMTL4RenderCommandEncoder description]
+ -[CaptureMTL4RenderCommandEncoder dispatchThreadsPerTile:]
+ -[CaptureMTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:]
+ -[CaptureMTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:]
+ -[CaptureMTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:]
+ -[CaptureMTL4RenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:]
+ -[CaptureMTL4RenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[CaptureMTL4RenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[CaptureMTL4RenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:]
+ -[CaptureMTL4RenderCommandEncoder drawPrimitives:indirectBuffer:]
+ -[CaptureMTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:]
+ -[CaptureMTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:]
+ -[CaptureMTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]
+ -[CaptureMTL4RenderCommandEncoder endEncodingAndRetrieveProgramAddressTable]
+ -[CaptureMTL4RenderCommandEncoder endEncoding]
+ -[CaptureMTL4RenderCommandEncoder executeCommandsInBuffer:indirectBuffer:]
+ -[CaptureMTL4RenderCommandEncoder executeCommandsInBuffer:withRange:]
+ -[CaptureMTL4RenderCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:]
+ -[CaptureMTL4RenderCommandEncoder forwardingTargetForSelector:]
+ -[CaptureMTL4RenderCommandEncoder initWithBaseObject:captureCommandBuffer:]
+ -[CaptureMTL4RenderCommandEncoder insertDebugSignpost:]
+ -[CaptureMTL4RenderCommandEncoder label]
+ -[CaptureMTL4RenderCommandEncoder originalObject]
+ -[CaptureMTL4RenderCommandEncoder popDebugGroup]
+ -[CaptureMTL4RenderCommandEncoder pushDebugGroup:]
+ -[CaptureMTL4RenderCommandEncoder respondsToSelector:]
+ -[CaptureMTL4RenderCommandEncoder setArgumentTable:atStages:]
+ -[CaptureMTL4RenderCommandEncoder setBlendColorRed:green:blue:alpha:]
+ -[CaptureMTL4RenderCommandEncoder setColorAttachmentMap:]
+ -[CaptureMTL4RenderCommandEncoder setColorStoreAction:atIndex:]
+ -[CaptureMTL4RenderCommandEncoder setCullMode:]
+ -[CaptureMTL4RenderCommandEncoder setDepthBias:slopeScale:clamp:]
+ -[CaptureMTL4RenderCommandEncoder setDepthClipMode:]
+ -[CaptureMTL4RenderCommandEncoder setDepthStencilState:]
+ -[CaptureMTL4RenderCommandEncoder setDepthStoreAction:]
+ -[CaptureMTL4RenderCommandEncoder setFrontFacingWinding:]
+ -[CaptureMTL4RenderCommandEncoder setLabel:]
+ -[CaptureMTL4RenderCommandEncoder setLineWidth:]
+ -[CaptureMTL4RenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]
+ -[CaptureMTL4RenderCommandEncoder setRenderPipelineState:]
+ -[CaptureMTL4RenderCommandEncoder setScissorRect:]
+ -[CaptureMTL4RenderCommandEncoder setScissorRects:count:]
+ -[CaptureMTL4RenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:]
+ -[CaptureMTL4RenderCommandEncoder setStencilReferenceValue:]
+ -[CaptureMTL4RenderCommandEncoder setStencilStoreAction:]
+ -[CaptureMTL4RenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:]
+ -[CaptureMTL4RenderCommandEncoder setTriangleFillMode:]
+ -[CaptureMTL4RenderCommandEncoder setVertexAmplificationCount:viewMappings:]
+ -[CaptureMTL4RenderCommandEncoder setViewport:]
+ -[CaptureMTL4RenderCommandEncoder setViewports:count:]
+ -[CaptureMTL4RenderCommandEncoder setVisibilityResultMode:offset:]
+ -[CaptureMTL4RenderCommandEncoder streamReference]
+ -[CaptureMTL4RenderCommandEncoder tileHeight]
+ -[CaptureMTL4RenderCommandEncoder tileWidth]
+ -[CaptureMTL4RenderCommandEncoder touch]
+ -[CaptureMTL4RenderCommandEncoder traceContext]
+ -[CaptureMTL4RenderCommandEncoder traceStream]
+ -[CaptureMTL4RenderCommandEncoder updateFence:afterEncoderStages:]
+ -[CaptureMTL4RenderCommandEncoder waitForFence:beforeEncoderStages:]
+ -[CaptureMTLAccelerationStructure captureDevice]
+ -[CaptureMTLAccelerationStructureCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLAccelerationStructureCommandEncoder insertSplit]
+ -[CaptureMTLBlitCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:]
+ -[CaptureMTLBlitCommandEncoder insertSplit]
+ -[CaptureMTLBuffer captureDevice]
+ -[CaptureMTLBuffer newTensorWithDescriptor:offset:error:]
+ -[CaptureMTLBuffer sparseBufferTier]
+ -[CaptureMTLCommandBuffer __waitUntilCompletedAsync:]
+ -[CaptureMTLCommandBuffer __waitUntilScheduledAsync:]
+ -[CaptureMTLCommandBuffer protectionOptions]
+ -[CaptureMTLCommandQueue captureDevice]
+ -[CaptureMTLComputeCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLComputeCommandEncoder insertSplit]
+ -[CaptureMTLComputePipelineState functionHandleWithBinaryFunction:]
+ -[CaptureMTLComputePipelineState functionHandleWithName:]
+ -[CaptureMTLComputePipelineState functionReflectionWithFunctionDescriptor:]
+ -[CaptureMTLComputePipelineState initWithBaseObject:descriptor:captureCompiler:]
+ -[CaptureMTLComputePipelineState newComputePipelineStateWithBinaryFunctions:error:]
+ -[CaptureMTLComputePipelineState requiredThreadsPerThreadgroup]
+ -[CaptureMTLDevice functionHandleWithBinaryFunction:]
+ -[CaptureMTLDevice functionHandleWithFunction:]
+ -[CaptureMTLDevice functionHandleWithFunction:resourceIndex:]
+ -[CaptureMTLDevice llvmVersion]
+ -[CaptureMTLDevice newArchiveWithURL:error:]
+ -[CaptureMTLDevice newArgumentTableWithDescriptor:error:]
+ -[CaptureMTLDevice newBufferWithLength:options:placementSparsePageSize:]
+ -[CaptureMTLDevice newCommandAllocatorWithDescriptor:error:]
+ -[CaptureMTLDevice newCommandAllocator]
+ -[CaptureMTLDevice newCommandBuffer]
+ -[CaptureMTLDevice newCompilerWithDescriptor:error:]
+ -[CaptureMTLDevice newFunctionHandle:associatedWithBaseFunctionHandle:captureFunction:]
+ -[CaptureMTLDevice newLibraryWithMPSGraphPackageURL:name:error:]
+ -[CaptureMTLDevice newMTL4CommandQueueWithDescriptor:error:]
+ -[CaptureMTLDevice newMTL4CommandQueue]
+ -[CaptureMTLDevice newPipelineDataSetSerializerWithDescriptor:]
+ -[CaptureMTLDevice newTensorWithDescriptor:error:]
+ -[CaptureMTLDevice newTextureViewPoolWithDescriptor:error:]
+ -[CaptureMTLDevice tensorSizeAndAlignWithDescriptor:]
+ -[CaptureMTLDrawable drawableID]
+ -[CaptureMTLDrawable presentedTime]
+ -[CaptureMTLDynamicLibrary initWithBaseObject:captureCompiler:]
+ -[CaptureMTLFXFrameInterpolator .cxx_destruct]
+ -[CaptureMTLFXFrameInterpolator aspectRatio]
+ -[CaptureMTLFXFrameInterpolator baseObject]
+ -[CaptureMTLFXFrameInterpolator colorTextureFormat]
+ -[CaptureMTLFXFrameInterpolator colorTextureUsage]
+ -[CaptureMTLFXFrameInterpolator colorTexture]
+ -[CaptureMTLFXFrameInterpolator conformsToProtocol:]
+ -[CaptureMTLFXFrameInterpolator dealloc]
+ -[CaptureMTLFXFrameInterpolator debugTexture]
+ -[CaptureMTLFXFrameInterpolator deltaTime]
+ -[CaptureMTLFXFrameInterpolator depthTextureFormat]
+ -[CaptureMTLFXFrameInterpolator depthTextureUsage]
+ -[CaptureMTLFXFrameInterpolator depthTexture]
+ -[CaptureMTLFXFrameInterpolator description]
+ -[CaptureMTLFXFrameInterpolator encodeToCommandBuffer:]
+ -[CaptureMTLFXFrameInterpolator farPlane]
+ -[CaptureMTLFXFrameInterpolator fence]
+ -[CaptureMTLFXFrameInterpolator fieldOfView]
+ -[CaptureMTLFXFrameInterpolator forwardingTargetForSelector:]
+ -[CaptureMTLFXFrameInterpolator initWithBaseObject:captureDevice:]
+ -[CaptureMTLFXFrameInterpolator inputHeight]
+ -[CaptureMTLFXFrameInterpolator inputWidth]
+ -[CaptureMTLFXFrameInterpolator isDepthReversed]
+ -[CaptureMTLFXFrameInterpolator isUITextureComposited]
+ -[CaptureMTLFXFrameInterpolator jitterOffsetX]
+ -[CaptureMTLFXFrameInterpolator jitterOffsetY]
+ -[CaptureMTLFXFrameInterpolator motionTextureFormat]
+ -[CaptureMTLFXFrameInterpolator motionTextureUsage]
+ -[CaptureMTLFXFrameInterpolator motionTexture]
+ -[CaptureMTLFXFrameInterpolator motionVectorScaleX]
+ -[CaptureMTLFXFrameInterpolator motionVectorScaleY]
+ -[CaptureMTLFXFrameInterpolator nearPlane]
+ -[CaptureMTLFXFrameInterpolator originalObject]
+ -[CaptureMTLFXFrameInterpolator outputHeight]
+ -[CaptureMTLFXFrameInterpolator outputTextureFormat]
+ -[CaptureMTLFXFrameInterpolator outputTextureUsage]
+ -[CaptureMTLFXFrameInterpolator outputTexture]
+ -[CaptureMTLFXFrameInterpolator outputWidth]
+ -[CaptureMTLFXFrameInterpolator prevColorTexture]
+ -[CaptureMTLFXFrameInterpolator respondsToSelector:]
+ -[CaptureMTLFXFrameInterpolator setAspectRatio:]
+ -[CaptureMTLFXFrameInterpolator setColorTexture:]
+ -[CaptureMTLFXFrameInterpolator setDebugTexture:]
+ -[CaptureMTLFXFrameInterpolator setDeltaTime:]
+ -[CaptureMTLFXFrameInterpolator setDepthReversed:]
+ -[CaptureMTLFXFrameInterpolator setDepthTexture:]
+ -[CaptureMTLFXFrameInterpolator setFarPlane:]
+ -[CaptureMTLFXFrameInterpolator setFence:]
+ -[CaptureMTLFXFrameInterpolator setFieldOfView:]
+ -[CaptureMTLFXFrameInterpolator setIsUITextureComposited:]
+ -[CaptureMTLFXFrameInterpolator setJitterOffsetX:]
+ -[CaptureMTLFXFrameInterpolator setJitterOffsetY:]
+ -[CaptureMTLFXFrameInterpolator setMotionTexture:]
+ -[CaptureMTLFXFrameInterpolator setMotionVectorScaleX:]
+ -[CaptureMTLFXFrameInterpolator setMotionVectorScaleY:]
+ -[CaptureMTLFXFrameInterpolator setNearPlane:]
+ -[CaptureMTLFXFrameInterpolator setOutputTexture:]
+ -[CaptureMTLFXFrameInterpolator setPrevColorTexture:]
+ -[CaptureMTLFXFrameInterpolator setShouldResetHistory:]
+ -[CaptureMTLFXFrameInterpolator setUITexture:]
+ -[CaptureMTLFXFrameInterpolator shouldResetHistory]
+ -[CaptureMTLFXFrameInterpolator streamReference]
+ -[CaptureMTLFXFrameInterpolator touch]
+ -[CaptureMTLFXFrameInterpolator traceContext]
+ -[CaptureMTLFXFrameInterpolator traceStream]
+ -[CaptureMTLFXFrameInterpolator uiTextureFormat]
+ -[CaptureMTLFXFrameInterpolator uiTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler .cxx_destruct]
+ -[CaptureMTLFXTemporalDenoisedScaler baseObject]
+ -[CaptureMTLFXTemporalDenoisedScaler colorTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler colorTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler colorTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler conformsToProtocol:]
+ -[CaptureMTLFXTemporalDenoisedScaler dealloc]
+ -[CaptureMTLFXTemporalDenoisedScaler debugTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler denoiseStrengthMaskTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler denoiseStrengthMaskTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler denoiseStrengthMaskTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler depthTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler depthTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler depthTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler description]
+ -[CaptureMTLFXTemporalDenoisedScaler diffuseAlbedoTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler diffuseAlbedoTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler diffuseAlbedoTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler dilatedMotionVectors]
+ -[CaptureMTLFXTemporalDenoisedScaler encodeToCommandBuffer:]
+ -[CaptureMTLFXTemporalDenoisedScaler encodeToCommandQueue:]
+ -[CaptureMTLFXTemporalDenoisedScaler exposureTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler fence]
+ -[CaptureMTLFXTemporalDenoisedScaler forwardingTargetForSelector:]
+ -[CaptureMTLFXTemporalDenoisedScaler initWithBaseObject:captureDevice:]
+ -[CaptureMTLFXTemporalDenoisedScaler inputContentHeight]
+ -[CaptureMTLFXTemporalDenoisedScaler inputContentMaxScale]
+ -[CaptureMTLFXTemporalDenoisedScaler inputContentMinScale]
+ -[CaptureMTLFXTemporalDenoisedScaler inputContentWidth]
+ -[CaptureMTLFXTemporalDenoisedScaler inputHeight]
+ -[CaptureMTLFXTemporalDenoisedScaler inputWidth]
+ -[CaptureMTLFXTemporalDenoisedScaler isDepthReversed]
+ -[CaptureMTLFXTemporalDenoisedScaler jitterOffsetX]
+ -[CaptureMTLFXTemporalDenoisedScaler jitterOffsetY]
+ -[CaptureMTLFXTemporalDenoisedScaler motionTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler motionTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler motionTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler motionVectorScaleX]
+ -[CaptureMTLFXTemporalDenoisedScaler motionVectorScaleY]
+ -[CaptureMTLFXTemporalDenoisedScaler normalTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler normalTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler normalTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler originalObject]
+ -[CaptureMTLFXTemporalDenoisedScaler outputHeight]
+ -[CaptureMTLFXTemporalDenoisedScaler outputTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler outputTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler outputTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler outputWidth]
+ -[CaptureMTLFXTemporalDenoisedScaler preExposure]
+ -[CaptureMTLFXTemporalDenoisedScaler reactiveMaskTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler reactiveMaskTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler reactiveTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler reset]
+ -[CaptureMTLFXTemporalDenoisedScaler respondsToSelector:]
+ -[CaptureMTLFXTemporalDenoisedScaler roughnessTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler roughnessTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler roughnessTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler setColorTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setDebugTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setDenoiseStrengthMaskTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setDepthReversed:]
+ -[CaptureMTLFXTemporalDenoisedScaler setDepthTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setDiffuseAlbedoTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setExposureTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setFence:]
+ -[CaptureMTLFXTemporalDenoisedScaler setInputContentHeight:]
+ -[CaptureMTLFXTemporalDenoisedScaler setInputContentWidth:]
+ -[CaptureMTLFXTemporalDenoisedScaler setJitterOffsetX:]
+ -[CaptureMTLFXTemporalDenoisedScaler setJitterOffsetY:]
+ -[CaptureMTLFXTemporalDenoisedScaler setMotionTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setMotionVectorScaleX:]
+ -[CaptureMTLFXTemporalDenoisedScaler setMotionVectorScaleY:]
+ -[CaptureMTLFXTemporalDenoisedScaler setNormalTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setOutputTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setPreExposure:]
+ -[CaptureMTLFXTemporalDenoisedScaler setReactiveMaskTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setRoughnessTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setShouldResetHistory:]
+ -[CaptureMTLFXTemporalDenoisedScaler setSpecularAlbedoTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setSpecularHitDistanceTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setTransparencyOverlayTexture:]
+ -[CaptureMTLFXTemporalDenoisedScaler setViewToClipMatrix:]
+ -[CaptureMTLFXTemporalDenoisedScaler setWorldToViewMatrix:]
+ -[CaptureMTLFXTemporalDenoisedScaler shouldResetHistory]
+ -[CaptureMTLFXTemporalDenoisedScaler specularAlbedoTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler specularAlbedoTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler specularAlbedoTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler specularHitDistanceTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler specularHitDistanceTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler specularHitDistanceTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler streamReference]
+ -[CaptureMTLFXTemporalDenoisedScaler touch]
+ -[CaptureMTLFXTemporalDenoisedScaler traceContext]
+ -[CaptureMTLFXTemporalDenoisedScaler traceStream]
+ -[CaptureMTLFXTemporalDenoisedScaler transparencyOverlayTextureFormat]
+ -[CaptureMTLFXTemporalDenoisedScaler transparencyOverlayTextureUsage]
+ -[CaptureMTLFXTemporalDenoisedScaler transparencyOverlayTexture]
+ -[CaptureMTLFXTemporalDenoisedScaler viewToClipMatrix]
+ -[CaptureMTLFXTemporalDenoisedScaler worldToViewMatrix]
+ -[CaptureMTLFXTemporalScaler dilatedMotionVectors]
+ -[CaptureMTLFXTemporalScaler reactiveMaskTextureFormat]
+ -[CaptureMTLFunctionHandle gpuResourceID]
+ -[CaptureMTLFunctionHandle initWithBaseObject:captureDevice:captureFunction:]
+ -[CaptureMTLFunctionHandle resourceIndex]
+ -[CaptureMTLHeap captureDevice]
+ -[CaptureMTLLibrary initWithBaseObject:captureCompiler:]
+ -[CaptureMTLParallelRenderCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLParallelRenderCommandEncoder insertSplit]
+ -[CaptureMTLRenderCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLRenderCommandEncoder insertSplit]
+ -[CaptureMTLRenderCommandEncoder setColorAttachmentMap:]
+ -[CaptureMTLRenderPipelineState functionHandleWithBinaryFunction:stage:]
+ -[CaptureMTLRenderPipelineState functionHandleWithName:stage:]
+ -[CaptureMTLRenderPipelineState functionReflectionWithFunctionDescriptor:stage:]
+ -[CaptureMTLRenderPipelineState initWithBaseObject:descriptor:captureCompiler:]
+ -[CaptureMTLRenderPipelineState newRenderPipelineDescriptorForSpecialization]
+ -[CaptureMTLRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:]
+ -[CaptureMTLRenderPipelineState reflectionForFunctionDescriptor:]
+ -[CaptureMTLRenderPipelineState requiredThreadsPerMeshThreadgroup]
+ -[CaptureMTLRenderPipelineState requiredThreadsPerObjectThreadgroup]
+ -[CaptureMTLRenderPipelineState requiredThreadsPerTileThreadgroup]
+ -[CaptureMTLResourceStateCommandEncoder barrierAfterQueueStages:beforeStages:]
+ -[CaptureMTLResourceStateCommandEncoder insertSplit]
+ -[CaptureMTLTensor .cxx_destruct]
+ -[CaptureMTLTensor allocatedSize]
+ -[CaptureMTLTensor allocationID]
+ -[CaptureMTLTensor baseObject]
+ -[CaptureMTLTensor bufferOffset]
+ -[CaptureMTLTensor buffer]
+ -[CaptureMTLTensor conformsToProtocol:]
+ -[CaptureMTLTensor cpuCacheMode]
+ -[CaptureMTLTensor dataType]
+ -[CaptureMTLTensor dealloc]
+ -[CaptureMTLTensor description]
+ -[CaptureMTLTensor device]
+ -[CaptureMTLTensor dimensions]
+ -[CaptureMTLTensor doesAliasAllResources:count:]
+ -[CaptureMTLTensor doesAliasAnyResources:count:]
+ -[CaptureMTLTensor doesAliasResource:]
+ -[CaptureMTLTensor forwardingTargetForSelector:]
+ -[CaptureMTLTensor getBytes:strides:fromSliceOrigin:sliceDimensions:]
+ -[CaptureMTLTensor gpuResourceID]
+ -[CaptureMTLTensor hazardTrackingMode]
+ -[CaptureMTLTensor heapOffset]
+ -[CaptureMTLTensor heap]
+ -[CaptureMTLTensor initWithBaseObject:captureBuffer:]
+ -[CaptureMTLTensor initWithBaseObject:captureDevice:]
+ -[CaptureMTLTensor initWithBaseObject:captureTensor:]
+ -[CaptureMTLTensor isAliasable]
+ -[CaptureMTLTensor isComplete]
+ -[CaptureMTLTensor isPurgeable]
+ -[CaptureMTLTensor isTensorViewableWithReshapedDescriptor:]
+ -[CaptureMTLTensor label]
+ -[CaptureMTLTensor makeAliasable]
+ -[CaptureMTLTensor newTensorViewWithReshapedDescriptor:error:]
+ -[CaptureMTLTensor newTensorViewWithSlice:error:]
+ -[CaptureMTLTensor offset]
+ -[CaptureMTLTensor originalObject]
+ -[CaptureMTLTensor parentTensor]
+ -[CaptureMTLTensor protectionOptions]
+ -[CaptureMTLTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:]
+ -[CaptureMTLTensor resourceIndex]
+ -[CaptureMTLTensor resourceOptions]
+ -[CaptureMTLTensor respondsToSelector:]
+ -[CaptureMTLTensor responsibleProcess]
+ -[CaptureMTLTensor setLabel:]
+ -[CaptureMTLTensor setOwnerWithIdentity:]
+ -[CaptureMTLTensor setPurgeableState:]
+ -[CaptureMTLTensor setResponsibleProcess:]
+ -[CaptureMTLTensor storageMode]
+ -[CaptureMTLTensor streamReference]
+ -[CaptureMTLTensor strides]
+ -[CaptureMTLTensor touch]
+ -[CaptureMTLTensor traceContext]
+ -[CaptureMTLTensor traceStream]
+ -[CaptureMTLTensor unfilteredResourceOptions]
+ -[CaptureMTLTensor usage]
+ -[CaptureMTLTensor waitUntilComplete]
+ -[CaptureMTLTexture newTextureViewWithDescriptor:]
+ -[CaptureMTLTexture sparseTextureTier]
+ -[CaptureMTLTexture updateDrawableStream:]
+ -[CaptureMTLTextureViewPool .cxx_destruct]
+ -[CaptureMTLTextureViewPool baseObject]
+ -[CaptureMTLTextureViewPool baseResourceID]
+ -[CaptureMTLTextureViewPool conformsToProtocol:]
+ -[CaptureMTLTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:]
+ -[CaptureMTLTextureViewPool dealloc]
+ -[CaptureMTLTextureViewPool description]
+ -[CaptureMTLTextureViewPool device]
+ -[CaptureMTLTextureViewPool forwardingTargetForSelector:]
+ -[CaptureMTLTextureViewPool initWithBaseObject:captureDevice:]
+ -[CaptureMTLTextureViewPool label]
+ -[CaptureMTLTextureViewPool originalObject]
+ -[CaptureMTLTextureViewPool resourceViewCount]
+ -[CaptureMTLTextureViewPool respondsToSelector:]
+ -[CaptureMTLTextureViewPool setTextureView:atIndex:]
+ -[CaptureMTLTextureViewPool setTextureView:descriptor:atIndex:]
+ -[CaptureMTLTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:]
+ -[CaptureMTLTextureViewPool streamReference]
+ -[CaptureMTLTextureViewPool touch]
+ -[CaptureMTLTextureViewPool traceContext]
+ -[CaptureMTLTextureViewPool traceStream]
+ -[GTDownloadGPUBuffer getTensorAlias:]
+ GCC_except_table110
+ GCC_except_table1464
+ GCC_except_table1490
+ GCC_except_table1592
+ GCC_except_table1593
+ GCC_except_table1597
+ GCC_except_table1598
+ GCC_except_table1599
+ GCC_except_table1600
+ GCC_except_table1601
+ GCC_except_table1807
+ GCC_except_table1808
+ GCC_except_table1810
+ GCC_except_table1812
+ GCC_except_table1821
+ GCC_except_table19
+ GCC_except_table1965
+ GCC_except_table2002
+ GCC_except_table222
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table2938
+ GCC_except_table301
+ GCC_except_table3099
+ GCC_except_table3193
+ GCC_except_table326
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table3892
+ GCC_except_table4403
+ GCC_except_table46
+ GCC_except_table617
+ GTAccelerationStructureDescriptorDownloader_MTL4_postProcess.descriptorDownloaderEventListener
+ GTAccelerationStructureDescriptorDownloader_MTL4_postProcess.descriptorDownloaderToken
+ GTAccelerationStructureDescriptorDownloader_processCopy.7809
+ GTAccelerationStructureDescriptorDownloader_processRefit.7810
+ GTCoreLogInit.once
+ GTCoreLog_getLogForTag.s_logs
+ GTCorePlatformInfoGet.info
+ GTCorePlatformInfoGet.onceToken
+ GTMTLCaptureEventBuffer_add.computePipeline
+ GTMTLCaptureEventBuffer_add.onceToken
+ GTMTLDecodeIndirectRenderCommandBuffer.onceToken.41
+ GTMTLTensor_wholeSlice.origin
+ GetStream.19513
+ OBJC_IVAR_$_CaptureMTL4Archive._baseObject
+ OBJC_IVAR_$_CaptureMTL4Archive._traceContext
+ OBJC_IVAR_$_CaptureMTL4Archive._traceStream
+ OBJC_IVAR_$_CaptureMTL4ArgumentTable._baseObject
+ OBJC_IVAR_$_CaptureMTL4ArgumentTable._captureDevice
+ OBJC_IVAR_$_CaptureMTL4ArgumentTable._traceContext
+ OBJC_IVAR_$_CaptureMTL4ArgumentTable._traceStream
+ OBJC_IVAR_$_CaptureMTL4BinaryFunction._baseObject
+ OBJC_IVAR_$_CaptureMTL4BinaryFunction._traceContext
+ OBJC_IVAR_$_CaptureMTL4BinaryFunction._traceStream
+ OBJC_IVAR_$_CaptureMTL4CommandAllocator._baseObject
+ OBJC_IVAR_$_CaptureMTL4CommandAllocator._captureDevice
+ OBJC_IVAR_$_CaptureMTL4CommandAllocator._traceContext
+ OBJC_IVAR_$_CaptureMTL4CommandAllocator._traceStream
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._accelerationStructureDescriptorCopyEventValue
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._accelerationStructureDescriptorProcessEvent
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._baseObject
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._captureDevice
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._parentStream
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._retainedObjects
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._traceContext
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._traceStream
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._baseObject
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._captureDevice
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._currentResidencySets
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._downloadEvent
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._downloadQueue
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._downloadQueueLock
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._downloadSignal
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._inFlightCommandBuffersCompletedEvent
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._inFlightCommandBuffersCompletedEventValue
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._lastSnapshot
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._listener
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._scheduled
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._snapshotCreated
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._submissionListener
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._traceContext
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._traceStream
+ OBJC_IVAR_$_CaptureMTL4Compiler._baseObject
+ OBJC_IVAR_$_CaptureMTL4Compiler._captureDevice
+ OBJC_IVAR_$_CaptureMTL4Compiler._traceContext
+ OBJC_IVAR_$_CaptureMTL4Compiler._traceStream
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._baseObject
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._captureCommandBuffer
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._captureDevice
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._descriptorDownloader
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._retainedDescriptorObjectsByStreamRef
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._retainedObjects
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._traceContext
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._traceStream
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._baseObject
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureColorTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureCompiler
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureDepthTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureDevice
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureFence
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureMotionTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._capturePrevColorTexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._captureUITexture
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._traceContext
+ OBJC_IVAR_$_CaptureMTL4FXFrameInterpolator._traceStream
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._baseObject
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureColorTexture
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureCompiler
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureDevice
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureFence
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._traceContext
+ OBJC_IVAR_$_CaptureMTL4FXSpatialScaler._traceStream
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._baseObject
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureColorTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureCompiler
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureDenoiseStrengthMaskTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureDepthTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureDevice
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureDiffuseAlbedoTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureExposureTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureFence
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureMotionTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureNormalTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureReactiveMaskTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureRoughnessTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureSpecularAlbedoTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureSpecularHitDistanceTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._captureTransparencyOverlayTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._traceContext
+ OBJC_IVAR_$_CaptureMTL4FXTemporalDenoisedScaler._traceStream
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._baseObject
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureColorTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureCompiler
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureDepthTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureDevice
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureExposureTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureFence
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureMotionTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureNormalTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._captureReactiveMaskTexture
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._traceContext
+ OBJC_IVAR_$_CaptureMTL4FXTemporalScaler._traceStream
+ OBJC_IVAR_$_CaptureMTL4MachineLearningCommandEncoder._baseObject
+ OBJC_IVAR_$_CaptureMTL4MachineLearningCommandEncoder._retainedObjects
+ OBJC_IVAR_$_CaptureMTL4MachineLearningCommandEncoder._traceContext
+ OBJC_IVAR_$_CaptureMTL4MachineLearningCommandEncoder._traceStream
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._baseObject
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._captureCompiler
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._captureDevice
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._captureLibrary
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._mtl4Descriptor
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._traceContext
+ OBJC_IVAR_$_CaptureMTL4MachineLearningPipelineState._traceStream
+ OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._baseObject
+ OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._traceContext
+ OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._traceStream
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._baseObject
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._retainedObjects
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._traceContext
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._traceStream
+ OBJC_IVAR_$_CaptureMTLAccelerationStructureCommandEncoder._bufferCache
+ OBJC_IVAR_$_CaptureMTLComputePipelineState._captureCompiler
+ OBJC_IVAR_$_CaptureMTLComputePipelineState._mtl4Descriptor
+ OBJC_IVAR_$_CaptureMTLDevice._cachedFunctionHandleLock
+ OBJC_IVAR_$_CaptureMTLDevice._cachedFunctionHandleMap
+ OBJC_IVAR_$_CaptureMTLDevice._dummyDepthStencilStateIndex
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._baseObject
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureColorTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureDepthTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureDevice
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureFence
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureMotionTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._capturePrevColorTexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._captureUITexture
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._traceContext
+ OBJC_IVAR_$_CaptureMTLFXFrameInterpolator._traceStream
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._baseObject
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureColorTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureDebugTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureDepthTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureDevice
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureDiffuseAlbedoTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureExposureTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureFence
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureMotionTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureNormalTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureOutputTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureReactiveMaskTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureRoughnessTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureSpecularAlbedoTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureSpecularHitDistanceTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._captureTransparencyOverlayTexture
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._traceContext
+ OBJC_IVAR_$_CaptureMTLFXTemporalDenoisedScaler._traceStream
+ OBJC_IVAR_$_CaptureMTLLibrary._captureCompiler
+ OBJC_IVAR_$_CaptureMTLRenderPipelineState._captureCompiler
+ OBJC_IVAR_$_CaptureMTLRenderPipelineState._mtl4Descriptor
+ OBJC_IVAR_$_CaptureMTLTensor._baseObject
+ OBJC_IVAR_$_CaptureMTLTensor._captureDevice
+ OBJC_IVAR_$_CaptureMTLTensor._traceContext
+ OBJC_IVAR_$_CaptureMTLTensor._traceStream
+ OBJC_IVAR_$_CaptureMTLTexture._drawableStream
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._baseObject
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._captureDevice
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._pool
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._streamRefs
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._textureViews
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._textureViewsCopy
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._traceContext
+ OBJC_IVAR_$_CaptureMTLTextureViewPool._traceStream
+ OBJC_IVAR_$_GTDownloadGPUBuffer._tensor
+ RetainObjectForDescriptorDownloader.9397
+ StoreMTLCompileOptionsUsingEncode.16073
+ _AllocateStateBuffer
+ _BlitBufferWithCache
+ _BlitBufferWithLength
+ _CFNumberGetValue
+ _CFStringGetCString
+ _CaptureAGXInit
+ _CaptureAGXProcessCompletedCommandBuffer
+ _CaptureAGXProcessCompletedCommandBufferEmpty
+ _CaptureAGXProcessCompletedCommandBufferImpl
+ _CopyGTMTLTextureDescriptor
+ _CopyGTMTLTextureViewDescriptor
+ _DYTraceEncode_MTL4ArgumentTable_dealloc
+ _DYTraceEncode_MTL4ArgumentTable_setAddress_atIndex
+ _DYTraceEncode_MTL4ArgumentTable_setResource_atBufferIndex
+ _DYTraceEncode_MTL4ArgumentTable_setSamplerState_atIndex
+ _DYTraceEncode_MTL4ArgumentTable_setTexture_atIndex
+ _DYTraceEncode_MTL4CommandAllocator_dealloc
+ _DYTraceEncode_MTL4CommandAllocator_reset
+ _DYTraceEncode_MTL4CommandBuffer_beginCommandBufferWithAllocator
+ _DYTraceEncode_MTL4CommandBuffer_computeCommandEncoder
+ _DYTraceEncode_MTL4CommandBuffer_dealloc
+ _DYTraceEncode_MTL4CommandBuffer_endCommandBuffer
+ _DYTraceEncode_MTL4CommandBuffer_machineLearningCommandEncoder
+ _DYTraceEncode_MTL4CommandBuffer_popDebugGroup
+ _DYTraceEncode_MTL4CommandBuffer_pushDebugGroup
+ _DYTraceEncode_MTL4CommandBuffer_renderCommandEncoderWithDescriptor
+ _DYTraceEncode_MTL4CommandBuffer_renderCommandEncoderWithDescriptor_options
+ _DYTraceEncode_MTL4CommandBuffer_setLabel
+ _DYTraceEncode_MTL4CommandBuffer_useResidencySet
+ _DYTraceEncode_MTL4CommandBuffer_useResidencySets_count
+ _DYTraceEncode_MTL4CommandQueue_addResidencySet
+ _DYTraceEncode_MTL4CommandQueue_addResidencySets_count
+ _DYTraceEncode_MTL4CommandQueue_commit_count
+ _DYTraceEncode_MTL4CommandQueue_commit_count_options
+ _DYTraceEncode_MTL4CommandQueue_copyBufferMappingsFromBuffer_toBuffer_operations_count
+ _DYTraceEncode_MTL4CommandQueue_copyTextureMappingsFromTexture_toTexture_operations_count
+ _DYTraceEncode_MTL4CommandQueue_dealloc
+ _DYTraceEncode_MTL4CommandQueue_removeResidencySet
+ _DYTraceEncode_MTL4CommandQueue_removeResidencySets_count
+ _DYTraceEncode_MTL4CommandQueue_signalDrawable
+ _DYTraceEncode_MTL4CommandQueue_signalEvent_value
+ _DYTraceEncode_MTL4CommandQueue_waitForDrawable
+ _DYTraceEncode_MTL4CommandQueue_waitForEvent_value
+ _DYTraceEncode_MTL4Compiler_newComputePipelineStateWithDescriptor_compilerTaskOptions_error
+ _DYTraceEncode_MTL4Compiler_newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error
+ _DYTraceEncode_MTL4Compiler_newDynamicLibraryWithURL_error
+ _DYTraceEncode_MTL4Compiler_newDynamicLibrary_error
+ _DYTraceEncode_MTL4Compiler_newLibraryWithDescriptor_completionHandler
+ _DYTraceEncode_MTL4Compiler_newLibraryWithDescriptor_error
+ _DYTraceEncode_MTL4Compiler_newMachineLearningPipelineStateWithDescriptor_completionHandler
+ _DYTraceEncode_MTL4Compiler_newMachineLearningPipelineStateWithDescriptor_error
+ _DYTraceEncode_MTL4Compiler_newRenderPipelineStateWithDescriptor_compilerTaskOptions_error
+ _DYTraceEncode_MTL4Compiler_newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error
+ _DYTraceEncode_MTL4ComputeCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions
+ _DYTraceEncode_MTL4ComputeCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions
+ _DYTraceEncode_MTL4ComputeCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions
+ _DYTraceEncode_MTL4ComputeCommandEncoder_buildAccelerationStructure_descriptor_scratchBuffer
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyAccelerationStructure_toAccelerationStructure
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyAndCompactAccelerationStructure_toAccelerationStructure
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTensor_sourceOrigin_sourceDimensions_toTensor_destinationOrigin_destinationDimensions
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount
+ _DYTraceEncode_MTL4ComputeCommandEncoder_copyFromTexture_toTexture
+ _DYTraceEncode_MTL4ComputeCommandEncoder_dealloc
+ _DYTraceEncode_MTL4ComputeCommandEncoder_dispatchThreadgroups_threadsPerThreadgroup
+ _DYTraceEncode_MTL4ComputeCommandEncoder_dispatchThreads_threadsPerThreadgroup
+ _DYTraceEncode_MTL4ComputeCommandEncoder_endEncoding
+ _DYTraceEncode_MTL4ComputeCommandEncoder_fillBuffer_range_value
+ _DYTraceEncode_MTL4ComputeCommandEncoder_generateMipmapsForTexture
+ _DYTraceEncode_MTL4ComputeCommandEncoder_insertDebugSignpost
+ _DYTraceEncode_MTL4ComputeCommandEncoder_optimizeContentsForCPUAccess
+ _DYTraceEncode_MTL4ComputeCommandEncoder_optimizeContentsForCPUAccess_slice_level
+ _DYTraceEncode_MTL4ComputeCommandEncoder_optimizeContentsForGPUAccess
+ _DYTraceEncode_MTL4ComputeCommandEncoder_optimizeContentsForGPUAccess_slice_level
+ _DYTraceEncode_MTL4ComputeCommandEncoder_popDebugGroup
+ _DYTraceEncode_MTL4ComputeCommandEncoder_pushDebugGroup
+ _DYTraceEncode_MTL4ComputeCommandEncoder_refitAccelerationStructure_descriptor_destination_scratchBuffer
+ _DYTraceEncode_MTL4ComputeCommandEncoder_refitAccelerationStructure_descriptor_destination_scratchBuffer_options
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setAccelerationStructureDescriptor
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setAccelerationStructureState
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setArgumentTable
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setComputePipelineState
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setImageblockWidth_height
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setLabel
+ _DYTraceEncode_MTL4ComputeCommandEncoder_setThreadgroupMemoryLength_atIndex
+ _DYTraceEncode_MTL4ComputeCommandEncoder_updateFence_afterEncoderStages
+ _DYTraceEncode_MTL4ComputeCommandEncoder_waitForFence_beforeEncoderStages
+ _DYTraceEncode_MTL4ComputeCommandEncoder_writeAccelerationStructureTraversalDepth_toBuffer
+ _DYTraceEncode_MTL4ComputeCommandEncoder_writeCompactedAccelerationStructureSize_toBuffer
+ _DYTraceEncode_MTL4FXFrameInterpolator_dealloc
+ _DYTraceEncode_MTL4FXFrameInterpolator_encodeToCommandBuffer
+ _DYTraceEncode_MTL4FXFrameInterpolator_setAspectRatio
+ _DYTraceEncode_MTL4FXFrameInterpolator_setColorTexture
+ _DYTraceEncode_MTL4FXFrameInterpolator_setColorTextureBarrierStages
+ _DYTraceEncode_MTL4FXFrameInterpolator_setDeltaTime
+ _DYTraceEncode_MTL4FXFrameInterpolator_setDepthReversed
+ _DYTraceEncode_MTL4FXFrameInterpolator_setDepthTexture
+ _DYTraceEncode_MTL4FXFrameInterpolator_setFarPlane
+ _DYTraceEncode_MTL4FXFrameInterpolator_setFence
+ _DYTraceEncode_MTL4FXFrameInterpolator_setFieldOfView
+ _DYTraceEncode_MTL4FXFrameInterpolator_setIsUITextureComposited
+ _DYTraceEncode_MTL4FXFrameInterpolator_setJitterOffsetX
+ _DYTraceEncode_MTL4FXFrameInterpolator_setJitterOffsetY
+ _DYTraceEncode_MTL4FXFrameInterpolator_setMotionTexture
+ _DYTraceEncode_MTL4FXFrameInterpolator_setMotionVectorScaleX
+ _DYTraceEncode_MTL4FXFrameInterpolator_setMotionVectorScaleY
+ _DYTraceEncode_MTL4FXFrameInterpolator_setNearPlane
+ _DYTraceEncode_MTL4FXFrameInterpolator_setOutputTexture
+ _DYTraceEncode_MTL4FXFrameInterpolator_setPrevColorTexture
+ _DYTraceEncode_MTL4FXFrameInterpolator_setShouldResetHistory
+ _DYTraceEncode_MTL4FXFrameInterpolator_setUITexture
+ _DYTraceEncode_MTL4FXSpatialScaler_dealloc
+ _DYTraceEncode_MTL4FXSpatialScaler_encodeToCommandBuffer
+ _DYTraceEncode_MTL4FXSpatialScaler_setColorTexture
+ _DYTraceEncode_MTL4FXSpatialScaler_setColorTextureBarrierStages
+ _DYTraceEncode_MTL4FXSpatialScaler_setFence
+ _DYTraceEncode_MTL4FXSpatialScaler_setInputContentHeight
+ _DYTraceEncode_MTL4FXSpatialScaler_setInputContentWidth
+ _DYTraceEncode_MTL4FXSpatialScaler_setOutputTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_dealloc
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_encodeToCommandBuffer
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setColorTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setColorTextureBarrierStages
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setDenoiseStrengthMaskTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setDepthReversed
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setDepthTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setDiffuseAlbedoTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setExposureTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setFence
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setInputContentHeight
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setInputContentWidth
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setJitterOffsetX
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setJitterOffsetY
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setMotionTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setMotionVectorScaleX
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setMotionVectorScaleY
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setNormalTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setOutputTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setPreExposure
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setReactiveMaskTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setRoughnessTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setShouldResetHistory
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setSpecularAlbedoTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setSpecularHitDistanceTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setTransparencyOverlayTexture
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setViewToClipMatrix
+ _DYTraceEncode_MTL4FXTemporalDenoisedScaler_setWorldToViewMatrix
+ _DYTraceEncode_MTL4FXTemporalScaler_dealloc
+ _DYTraceEncode_MTL4FXTemporalScaler_encodeToCommandBuffer
+ _DYTraceEncode_MTL4FXTemporalScaler_executionMode
+ _DYTraceEncode_MTL4FXTemporalScaler_setColorTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setColorTextureBarrierStages
+ _DYTraceEncode_MTL4FXTemporalScaler_setDepthReversed
+ _DYTraceEncode_MTL4FXTemporalScaler_setDepthTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setExposureTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setFence
+ _DYTraceEncode_MTL4FXTemporalScaler_setInputContentHeight
+ _DYTraceEncode_MTL4FXTemporalScaler_setInputContentWidth
+ _DYTraceEncode_MTL4FXTemporalScaler_setJitterOffsetX
+ _DYTraceEncode_MTL4FXTemporalScaler_setJitterOffsetY
+ _DYTraceEncode_MTL4FXTemporalScaler_setMotionTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setMotionVectorScaleX
+ _DYTraceEncode_MTL4FXTemporalScaler_setMotionVectorScaleY
+ _DYTraceEncode_MTL4FXTemporalScaler_setOutputTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setPreExposure
+ _DYTraceEncode_MTL4FXTemporalScaler_setReactiveMaskTexture
+ _DYTraceEncode_MTL4FXTemporalScaler_setReset
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_dealloc
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_dispatchNetworkWithIntermediatesHeap
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_endEncoding
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_insertDebugSignpost
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_popDebugGroup
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_pushDebugGroup
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_setArgumentTable
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_setLabel
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_setPipelineState
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_updateFence_afterEncoderStages
+ _DYTraceEncode_MTL4MachineLearningCommandEncoder_waitForFence_beforeEncoderStages
+ _DYTraceEncode_MTL4MachineLearningPipelineState_dealloc
+ _DYTraceEncode_MTL4RenderCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions
+ _DYTraceEncode_MTL4RenderCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions
+ _DYTraceEncode_MTL4RenderCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions
+ _DYTraceEncode_MTL4RenderCommandEncoder_dealloc
+ _DYTraceEncode_MTL4RenderCommandEncoder_dispatchThreadsPerTile
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount
+ _DYTraceEncode_MTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance
+ _DYTraceEncode_MTL4RenderCommandEncoder_endEncoding
+ _DYTraceEncode_MTL4RenderCommandEncoder_insertDebugSignpost
+ _DYTraceEncode_MTL4RenderCommandEncoder_popDebugGroup
+ _DYTraceEncode_MTL4RenderCommandEncoder_pushDebugGroup
+ _DYTraceEncode_MTL4RenderCommandEncoder_setArgumentTable_atStages
+ _DYTraceEncode_MTL4RenderCommandEncoder_setBlendColorRed_green_blue_alpha
+ _DYTraceEncode_MTL4RenderCommandEncoder_setColorAttachmentMap
+ _DYTraceEncode_MTL4RenderCommandEncoder_setColorStoreAction_atIndex
+ _DYTraceEncode_MTL4RenderCommandEncoder_setCullMode
+ _DYTraceEncode_MTL4RenderCommandEncoder_setDepthBias_slopeScale_clamp
+ _DYTraceEncode_MTL4RenderCommandEncoder_setDepthClipMode
+ _DYTraceEncode_MTL4RenderCommandEncoder_setDepthStencilState
+ _DYTraceEncode_MTL4RenderCommandEncoder_setDepthStoreAction
+ _DYTraceEncode_MTL4RenderCommandEncoder_setDepthTestMinBound_maxBound
+ _DYTraceEncode_MTL4RenderCommandEncoder_setFrontFacingWinding
+ _DYTraceEncode_MTL4RenderCommandEncoder_setLabel
+ _DYTraceEncode_MTL4RenderCommandEncoder_setLineWidth
+ _DYTraceEncode_MTL4RenderCommandEncoder_setObjectThreadgroupMemoryLength_atIndex
+ _DYTraceEncode_MTL4RenderCommandEncoder_setRenderPipelineState
+ _DYTraceEncode_MTL4RenderCommandEncoder_setScissorRect
+ _DYTraceEncode_MTL4RenderCommandEncoder_setScissorRects_count
+ _DYTraceEncode_MTL4RenderCommandEncoder_setStencilFrontReferenceValue_backReferenceValue
+ _DYTraceEncode_MTL4RenderCommandEncoder_setStencilReferenceValue
+ _DYTraceEncode_MTL4RenderCommandEncoder_setStencilStoreAction
+ _DYTraceEncode_MTL4RenderCommandEncoder_setThreadgroupMemoryLength_offset_atIndex
+ _DYTraceEncode_MTL4RenderCommandEncoder_setTriangleFillMode
+ _DYTraceEncode_MTL4RenderCommandEncoder_setVertexAmplificationCount_viewMappings
+ _DYTraceEncode_MTL4RenderCommandEncoder_setViewport
+ _DYTraceEncode_MTL4RenderCommandEncoder_setViewports_count
+ _DYTraceEncode_MTL4RenderCommandEncoder_setVisibilityResultMode_offset
+ _DYTraceEncode_MTL4RenderCommandEncoder_updateFence_afterEncoderStages
+ _DYTraceEncode_MTL4RenderCommandEncoder_waitForFence_beforeEncoderStages
+ _DYTraceEncode_MTLAccelerationStructureCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLArgumentEncoder_setDepthStencilState_atIndex
+ _DYTraceEncode_MTLArgumentEncoder_setDepthStencilStates_withRange
+ _DYTraceEncode_MTLBlitCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLBlitCommandEncoder_copyFromTensor_sourceOrigin_sourceDimensions_toTensor_destinationOrigin_destinationDimensions
+ _DYTraceEncode_MTLBuffer_newTensorWithDescriptor_offset_error
+ _DYTraceEncode_MTLCaptureManager_sharedCaptureManager
+ _DYTraceEncode_MTLCommandBuffer_encodeSignalEvent_value_agentMask
+ _DYTraceEncode_MTLComputeCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLDepthStencilState_gpuResourceID
+ _DYTraceEncode_MTLDepthStencilState_uniqueIdentifier
+ _DYTraceEncode_MTLDevice_functionHandleWithFunction
+ _DYTraceEncode_MTLDevice_newArgumentTableWithDescriptor_error
+ _DYTraceEncode_MTLDevice_newCommandAllocator
+ _DYTraceEncode_MTLDevice_newCommandAllocatorWithDescriptor_error
+ _DYTraceEncode_MTLDevice_newCommandBuffer
+ _DYTraceEncode_MTLDevice_newCompilerWithDescriptor_error
+ _DYTraceEncode_MTLDevice_newFrameInterpolatorWithDescriptor
+ _DYTraceEncode_MTLDevice_newMTL4CommandQueue
+ _DYTraceEncode_MTLDevice_newMTL4CommandQueueWithDescriptor_error
+ _DYTraceEncode_MTLDevice_newMTL4FrameInterpolatorWithDescriptor_compiler
+ _DYTraceEncode_MTLDevice_newMTL4SpatialScalerWithDescriptor_compiler
+ _DYTraceEncode_MTLDevice_newMTL4TemporalDenoisedScalerWithDescriptor_compiler
+ _DYTraceEncode_MTLDevice_newMTL4TemporalScalerWithDescriptor_compiler
+ _DYTraceEncode_MTLDevice_newTemporalDenoisedScalerWithDescriptor
+ _DYTraceEncode_MTLDevice_newTensorWithDescriptor_error
+ _DYTraceEncode_MTLDevice_newTextureViewPoolWithDescriptor_error
+ _DYTraceEncode_MTLFXFrameInterpolator_dealloc
+ _DYTraceEncode_MTLFXFrameInterpolator_encodeToCommandBuffer
+ _DYTraceEncode_MTLFXFrameInterpolator_setAspectRatio
+ _DYTraceEncode_MTLFXFrameInterpolator_setColorTexture
+ _DYTraceEncode_MTLFXFrameInterpolator_setDeltaTime
+ _DYTraceEncode_MTLFXFrameInterpolator_setDepthReversed
+ _DYTraceEncode_MTLFXFrameInterpolator_setDepthTexture
+ _DYTraceEncode_MTLFXFrameInterpolator_setFarPlane
+ _DYTraceEncode_MTLFXFrameInterpolator_setFence
+ _DYTraceEncode_MTLFXFrameInterpolator_setFieldOfView
+ _DYTraceEncode_MTLFXFrameInterpolator_setIsUITextureComposited
+ _DYTraceEncode_MTLFXFrameInterpolator_setJitterOffsetX
+ _DYTraceEncode_MTLFXFrameInterpolator_setJitterOffsetY
+ _DYTraceEncode_MTLFXFrameInterpolator_setMotionTexture
+ _DYTraceEncode_MTLFXFrameInterpolator_setMotionVectorScaleX
+ _DYTraceEncode_MTLFXFrameInterpolator_setMotionVectorScaleY
+ _DYTraceEncode_MTLFXFrameInterpolator_setNearPlane
+ _DYTraceEncode_MTLFXFrameInterpolator_setOutputTexture
+ _DYTraceEncode_MTLFXFrameInterpolator_setPrevColorTexture
+ _DYTraceEncode_MTLFXFrameInterpolator_setShouldResetHistory
+ _DYTraceEncode_MTLFXFrameInterpolator_setUITexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_dealloc
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_encodeToCommandBuffer
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_encodeToCommandQueue
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setColorTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setDenoiseStrengthMaskTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setDepthReversed
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setDepthTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setDiffuseAlbedoTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setExposureTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setFence
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setInputContentHeight
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setInputContentWidth
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setJitterOffsetX
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setJitterOffsetY
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setMotionTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setMotionVectorScaleX
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setMotionVectorScaleY
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setNormalTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setOutputTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setPreExposure
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setReactiveMaskTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setRoughnessTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setShouldResetHistory
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setSpecularAlbedoTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setSpecularHitDistanceTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setTransparencyOverlayTexture
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setViewToClipMatrix
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_setWorldToViewMatrix
+ _DYTraceEncode_MTLFunctionHandle_gpuResourceID
+ _DYTraceEncode_MTLFunctionHandle_resourceIndex
+ _DYTraceEncode_MTLIndirectRenderCommand_setBlendColorRed_green_blue_alpha
+ _DYTraceEncode_MTLIndirectRenderCommand_setCullMode
+ _DYTraceEncode_MTLIndirectRenderCommand_setDepthBias_slopeScale_clamp
+ _DYTraceEncode_MTLIndirectRenderCommand_setDepthClipMode
+ _DYTraceEncode_MTLIndirectRenderCommand_setDepthStencilState
+ _DYTraceEncode_MTLIndirectRenderCommand_setDepthTestMinBound_maxBound
+ _DYTraceEncode_MTLIndirectRenderCommand_setFrontFacingWinding
+ _DYTraceEncode_MTLIndirectRenderCommand_setScissorRect
+ _DYTraceEncode_MTLIndirectRenderCommand_setScissorRects_count
+ _DYTraceEncode_MTLIndirectRenderCommand_setStencilFrontReferenceValue_backReferenceValue
+ _DYTraceEncode_MTLIndirectRenderCommand_setStencilReferenceValue
+ _DYTraceEncode_MTLIndirectRenderCommand_setTriangleFillMode
+ _DYTraceEncode_MTLIndirectRenderCommand_setViewport
+ _DYTraceEncode_MTLIndirectRenderCommand_setViewports_count
+ _DYTraceEncode_MTLParallelRenderCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLRenderCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLRenderCommandEncoder_setColorAttachmentMap
+ _DYTraceEncode_MTLRenderCommandEncoder_setDepthTestMinBound_maxBound
+ _DYTraceEncode_MTLResourceStateCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DYTraceEncode_MTLTensor_allocatedSize
+ _DYTraceEncode_MTLTensor_allocationID
+ _DYTraceEncode_MTLTensor_dealloc
+ _DYTraceEncode_MTLTensor_gpuResourceID
+ _DYTraceEncode_MTLTensor_makeAliasable
+ _DYTraceEncode_MTLTensor_replaceSliceOrigin_sliceDimensions_withBytes_strides
+ _DYTraceEncode_MTLTensor_resourceIndex
+ _DYTraceEncode_MTLTensor_setLabel
+ _DYTraceEncode_MTLTensor_setPurgeableState
+ _DYTraceEncode_MTLTensor_setResponsibleProcess
+ _DYTraceEncode_MTLTensor_timeSinceTouched
+ _DYTraceEncode_MTLTensor_uniqueIdentifier
+ _DYTraceEncode_MTLTextureViewPool_copyResourceViewsFromPool_sourceRange_destinationIndex
+ _DYTraceEncode_MTLTextureViewPool_dealloc
+ _DYTraceEncode_MTLTextureViewPool_setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex
+ _DYTraceEncode_MTLTextureViewPool_setTextureView_atIndex
+ _DYTraceEncode_MTLTextureViewPool_setTextureView_descriptor_atIndex
+ _DYTraceEncode_MTLTexture_newTextureViewWithDescriptor
+ _DYTraceEncode_MTLVideoCommandEncoder_barrierAfterQueueStages_beforeStages
+ _DecodeDYMTL4ArgumentTableDescriptor
+ _DecodeDYMTL4BinaryFunctionDescriptor
+ _DecodeDYMTL4CommandAllocatorDescriptor
+ _DecodeDYMTL4CommandQueueDescriptor
+ _DecodeDYMTL4CompilerDescriptor
+ _DecodeDYMTL4CompilerTaskOptions
+ _DecodeDYMTL4FunctionDescriptor
+ _DecodeDYMTL4LibraryDescriptor
+ _DecodeDYMTL4PipelineDataSetSerializerDescriptor
+ _DecodeDYMTL4PipelineDescriptor
+ _DecodeDYMTL4PipelineStageDynamicLinkingDescriptor
+ _DecodeDYMTL4RenderPassDescriptor
+ _DecodeDYMTL4RenderPipelineDynamicLinkingDescriptor
+ _DecodeDYMTLCaptureDescriptorInternal
+ _DecodeDYMTLFXFrameInterpolatorDescriptor
+ _DecodeDYMTLFXTemporalDenoisedScalerDescriptor
+ _DecodeDYMTLResourceViewPoolDescriptor
+ _DecodeDYMTLTensorDescriptor
+ _DecodeDYMTLTextureViewDescriptor
+ _DeviceForCommandQueue
+ _DirToDict
+ _DisableMTLDebugErrors
+ _DownloadTensor
+ _EncodeDYMTL4ArgumentTableDescriptor
+ _EncodeDYMTL4BinaryFunctionDescriptor
+ _EncodeDYMTL4CommandAllocatorDescriptor
+ _EncodeDYMTL4CommandQueueDescriptor
+ _EncodeDYMTL4CompilerDescriptor
+ _EncodeDYMTL4CompilerTaskOptions
+ _EncodeDYMTL4FunctionDescriptor
+ _EncodeDYMTL4LibraryDescriptor
+ _EncodeDYMTL4PipelineDataSetSerializerDescriptor
+ _EncodeDYMTL4PipelineDescriptor
+ _EncodeDYMTL4PipelineStageDynamicLinkingDescriptor
+ _EncodeDYMTL4RenderPassDescriptor
+ _EncodeDYMTL4RenderPipelineDynamicLinkingDescriptor
+ _EncodeDYMTLCaptureDescriptorInternal
+ _EncodeDYMTLFXFrameInterpolatorDescriptor
+ _EncodeDYMTLFXTemporalDenoisedScalerDescriptor
+ _EncodeDYMTLResourceViewPoolDescriptor
+ _EncodeDYMTLTensorDescriptor
+ _EncodeDYMTLTextureViewDescriptor
+ _EncodeSetTextureView
+ _EncodeSetTextureViewFromBuffer
+ _EncodeSetTextureViewWithDescriptor
+ _FillCaptureObjectTypeError
+ _FillInstanceAccelerationStructureHeader_MTL4
+ _FlushChainedMachineLearningPipelineStateInfo
+ _FlushChainedMachineLearningPipelineStateInfo_
+ _FlushGTMTL4FunctionReflection
+ _GTAccelerationStructureDescriptorDownloader_MTL4_destroy
+ _GTAccelerationStructureDescriptorDownloader_MTL4_make
+ _GTAccelerationStructureDescriptorDownloader_MTL4_postProcess
+ _GTAccelerationStructureDescriptorDownloader_processBuild
+ _GTAccelerationStructureDescriptorDownloader_processCopy
+ _GTAccelerationStructureDescriptorDownloader_processEndEncoding
+ _GTAccelerationStructureDescriptorDownloader_processRefit
+ _GTAccelerationStructureDescriptorDownloader_suballocate
+ _GTCaptureArchive_addFile
+ _GTCaptureArchive_create
+ _GTCaptureArchive_fillBufferSeparateFile
+ _GTCaptureArchive_isFileSymlink
+ _GTCaptureArchive_isValid
+ _GTCaptureArchive_linkFile
+ _GTCaptureArchive_mapDataSeparateFile
+ _GTCaptureArchive_removeFile
+ _GTCaptureArchive_resizeBackingStore
+ _GTCaptureArchive_save
+ _GTCoreLog_getLogForTag
+ _GTCorePlatformInfoGet
+ _GTErrorKeyMTL4CommitFeedback
+ _GTError_copy
+ _GTError_flags
+ _GTError_single
+ _GTError_string
+ _GTEventTracker_processWait
+ _GTFenum_getConstructorType
+ _GTFenum_getReceiverType
+ _GTFenum_getTargetType
+ _GTFenum_isAccelerationEncodeCall
+ _GTFenum_isAddResidencySetCall
+ _GTFenum_isArgumentTableSnapshotCall
+ _GTFenum_isBarrier
+ _GTFenum_isBeginCommandBuffer
+ _GTFenum_isBlitCall
+ _GTFenum_isCommandBufferCommit
+ _GTFenum_isCommandBufferRelated
+ _GTFenum_isCommandEncoder
+ _GTFenum_isComputeCall
+ _GTFenum_isConstructor
+ _GTFenum_isCreateCommandBuffer
+ _GTFenum_isCreateCommandQueue
+ _GTFenum_isCreateMIOCommandBuffer
+ _GTFenum_isCreateMIOCommandQueue
+ _GTFenum_isCreateMTL4CommandEncoder
+ _GTFenum_isCreateMTL4CommandQueue
+ _GTFenum_isCreateMTLCommandEncoder
+ _GTFenum_isCreateResource
+ _GTFenum_isDestructor
+ _GTFenum_isDrawCall
+ _GTFenum_isEncodeSignalEvent
+ _GTFenum_isEncodeUpdateFence
+ _GTFenum_isEncodeWaitForEvent
+ _GTFenum_isEncodeWaitForFence
+ _GTFenum_isEndCommandBuffer
+ _GTFenum_isEndEncoding
+ _GTFenum_isFrameBoundary
+ _GTFenum_isGPUCommandCall
+ _GTFenum_isIndirectExecuteCall
+ _GTFenum_isIndirectExecuteComputeCall
+ _GTFenum_isIndirectExecuteRenderCall
+ _GTFenum_isMFXEncode
+ _GTFenum_isMIOCall
+ _GTFenum_isMIOCommandBufferCommit
+ _GTFenum_isMIOCommandBufferRelated
+ _GTFenum_isMLCall
+ _GTFenum_isMPSDispatchCall
+ _GTFenum_isMPSEncodeCall
+ _GTFenum_isMTL4CommandBufferRelated
+ _GTFenum_isMTL4CommandEncoder
+ _GTFenum_isMTL4CommandEncoderCall
+ _GTFenum_isMTL4CommandQueueCommit
+ _GTFenum_isMTL4EndEncoding
+ _GTFenum_isMTLCommandEncoder
+ _GTFenum_isMTLResource
+ _GTFenum_isMeshCall
+ _GTFenum_isParallelCommandEncoderCall
+ _GTFenum_isPatchCall
+ _GTFenum_isPopDebugGroup
+ _GTFenum_isPresent
+ _GTFenum_isPushDebugGroup
+ _GTFenum_isRemoveResidencySetCall
+ _GTFenum_isResourceCall
+ _GTFenum_isSampleCall
+ _GTFenum_isSampledBlitCall
+ _GTFenum_isSampledBlitCallAGX
+ _GTFenum_isSetArgumentTable
+ _GTFenum_isSetLabel
+ _GTFenum_isSetTextureViewWithDescriptor
+ _GTFenum_isSharedResourceConstructor
+ _GTFenum_isStreamConstructor
+ _GTFenum_isSupported
+ _GTFenum_isTileCall
+ _GTFenum_isUseResidencySetCall
+ _GTFenum_isUseResourceCall
+ _GTFenum_isVRSubmitCall
+ _GTFenum_isVideoCall
+ _GTFileSystem_delete
+ _GTFileSystem_fileExists
+ _GTFile_printf
+ _GTHash_blocks
+ _GTHash_data
+ _GTHash_diff
+ _GTMTL4FXSMFrameInterpolator_init
+ _GTMTL4FXSMFrameInterpolator_processTraceFuncWithMap
+ _GTMTL4FXSMFrameInterpolator_processTraceFuncWithPool
+ _GTMTL4FXSMSpatialScaler_init
+ _GTMTL4FXSMSpatialScaler_processTraceFuncWithMap
+ _GTMTL4FXSMSpatialScaler_processTraceFuncWithPool
+ _GTMTL4FXSMTemporalDenoisedScaler_init
+ _GTMTL4FXSMTemporalDenoisedScaler_processTraceFuncWithMap
+ _GTMTL4FXSMTemporalDenoisedScaler_processTraceFuncWithPool
+ _GTMTL4FXSMTemporalScaler_init
+ _GTMTL4FXSMTemporalScaler_processTraceFuncWithMap
+ _GTMTL4FXSMTemporalScaler_processTraceFuncWithPool
+ _GTMTL4FunctionDescriptor_identifier
+ _GTMTL4RenderPassDescriptorDefaults
+ _GTMTL4SMArgumentTable_init
+ _GTMTL4SMArgumentTable_isBufferBindingGPUAddress
+ _GTMTL4SMArgumentTable_processTraceFuncWithMap
+ _GTMTL4SMArgumentTable_processTraceFuncWithPool
+ _GTMTL4SMArgumentTable_setBufferBindingAsGPUAddress
+ _GTMTL4SMArgumentTable_setBufferBindingAsResourceID
+ _GTMTL4SMBuilder_argumentTable
+ _GTMTL4SMBuilder_commandAllocator
+ _GTMTL4SMBuilder_commandBuffer
+ _GTMTL4SMBuilder_commandQueue
+ _GTMTL4SMBuilder_compiler
+ _GTMTL4SMBuilder_machineLearningPipelineState
+ _GTMTL4SMCommandAllocator_init
+ _GTMTL4SMCommandAllocator_processTraceFuncWithMap
+ _GTMTL4SMCommandAllocator_processTraceFuncWithPool
+ _GTMTL4SMCommandBuffer_init
+ _GTMTL4SMCommandBuffer_processTraceFunc
+ _GTMTL4SMCommandEncoder_init
+ _GTMTL4SMCommandEncoder_processTraceFunc
+ _GTMTL4SMCommandEncoder_renderCommandEncoder
+ _GTMTL4SMCommandEncoder_renderPassDescriptor
+ _GTMTL4SMCommandQueue_init
+ _GTMTL4SMCommandQueue_processTraceFuncWithMap
+ _GTMTL4SMCommandQueue_processTraceFuncWithPool
+ _GTMTL4SMCompiler_init
+ _GTMTL4SMCompiler_processTraceFuncWithMap
+ _GTMTL4SMCompiler_processTraceFuncWithPool
+ _GTMTL4SMComputeCommandEncoder_init
+ _GTMTL4SMContext_getArgumentTable
+ _GTMTL4SMContext_getArgumentTables
+ _GTMTL4SMContext_getCommandAllocators
+ _GTMTL4SMContext_getCommandBuffers
+ _GTMTL4SMContext_getCommandQueues
+ _GTMTL4SMContext_getMachineLearningPipelineState
+ _GTMTL4SMContext_getMachineLearningPipelineStates
+ _GTMTL4SMMachineLearningCommandEncoder_init
+ _GTMTL4SMMachineLearningPipelineState_init
+ _GTMTL4SMMachineLearningPipelineState_processTraceFuncWithMap
+ _GTMTL4SMMachineLearningPipelineState_processTraceFuncWithPool
+ _GTMTL4SMRenderCommandEncoder_init
+ _GTMTLCaptureEventBuffer_add
+ _GTMTLCaptureEventBuffer_getElements
+ _GTMTLCaptureManager_dumpDeviceFilesLocal
+ _GTMTLCaptureManager_preCaptureTakeSnapshots
+ _GTMTLCaptureManager_prepareForSerialization
+ _GTMTLCaptureState_getCaptureArchive
+ _GTMTLCaptureState_notifyCommandBuffersCaptured
+ _GTMTLCoreSync_acquireSignalValue
+ _GTMTLCoreSync_event
+ _GTMTLCoreSync_init
+ _GTMTLCoreSync_waitValue
+ _GTMTLFXSMFrameInterpolator_init
+ _GTMTLFXSMFrameInterpolator_processTraceFuncWithMap
+ _GTMTLFXSMFrameInterpolator_processTraceFuncWithPool
+ _GTMTLFXSMTemporalDenoisedScaler_init
+ _GTMTLFXSMTemporalDenoisedScaler_processTraceFuncWithMap
+ _GTMTLFXSMTemporalDenoisedScaler_processTraceFuncWithPool
+ _GTMTLGPUAddressResource_translateToResourceOffset
+ _GTMTLGuestAppClientAddMTL4CommandQueueInfo
+ _GTMTLGuestAppClientRemoveMTL4CommandQueueInfo
+ _GTMTLIndirectCommandEncoder_getBlendColor
+ _GTMTLIndirectCommandEncoder_getCullMode
+ _GTMTLIndirectCommandEncoder_getDepthBias
+ _GTMTLIndirectCommandEncoder_getDepthClipMode
+ _GTMTLIndirectCommandEncoder_getDepthStencilState
+ _GTMTLIndirectCommandEncoder_getDepthTestBounds
+ _GTMTLIndirectCommandEncoder_getFrontFacingWinding
+ _GTMTLIndirectCommandEncoder_getScissorRects
+ _GTMTLIndirectCommandEncoder_getScissorRectsCount
+ _GTMTLIndirectCommandEncoder_getStencilReferenceValues
+ _GTMTLIndirectCommandEncoder_getTriangleFillMode
+ _GTMTLIndirectCommandEncoder_getViewports
+ _GTMTLIndirectCommandEncoder_getViewportsCount
+ _GTMTLIndirectCommandEncoder_setBlendColor
+ _GTMTLIndirectCommandEncoder_setCullMode
+ _GTMTLIndirectCommandEncoder_setDepthBias
+ _GTMTLIndirectCommandEncoder_setDepthClipMode
+ _GTMTLIndirectCommandEncoder_setDepthStencilState
+ _GTMTLIndirectCommandEncoder_setDepthTestBounds
+ _GTMTLIndirectCommandEncoder_setFrontFacingWinding
+ _GTMTLIndirectCommandEncoder_setScissorRects
+ _GTMTLIndirectCommandEncoder_setScissorRectsCount
+ _GTMTLIndirectCommandEncoder_setStencilReferenceValues
+ _GTMTLIndirectCommandEncoder_setTriangleFillMode
+ _GTMTLIndirectCommandEncoder_setViewports
+ _GTMTLIndirectCommandEncoder_setViewportsCount
+ _GTMTLIndirectResources_depthStencilStateIdForUniqueIdentifier
+ _GTMTLIndirectResources_resourceForGPUAddress
+ _GTMTLLogicalToPhysicalColorAttachmentMapEqual
+ _GTMTLLogicalToPhysicalColorAttachmentMapFromArgs
+ _GTMTLLogicalToPhysicalColorAttachmentMapIdentity
+ _GTMTLRenderStageFromIndex
+ _GTMTLResourceViewPoolResourceArray_resourceForUniqueIdentifier
+ _GTMTLResourceViewPoolResource_fillHashMapByKey
+ _GTMTLResourceViewPoolResource_fillHashMapWithArraysByResourceID
+ _GTMTLResourceViewPoolResource_getKey
+ _GTMTLSMBuilder_frameInterpolator
+ _GTMTLSMBuilder_ioFileHandle
+ _GTMTLSMBuilder_mtl4FrameInterpolator
+ _GTMTLSMBuilder_mtl4SpatialScaler
+ _GTMTLSMBuilder_mtl4TemporalDenoisedScaler
+ _GTMTLSMBuilder_mtl4TemporalScaler
+ _GTMTLSMBuilder_temporalDenoisedScaler
+ _GTMTLSMBuilder_tensor
+ _GTMTLSMBuilder_textureViewPool
+ _GTMTLSMComputePipelineState_computePipelineDescriptor4
+ _GTMTLSMComputePipelineState_hasDescriptor4
+ _GTMTLSMContext_createDescriptorFromBuffer
+ _GTMTLSMContext_firstObject
+ _GTMTLSMContext_firstTensor
+ _GTMTLSMContext_getBufferDescriptor
+ _GTMTLSMContext_getCompilers
+ _GTMTLSMContext_getFrameInterpolator
+ _GTMTLSMContext_getFrameInterpolators
+ _GTMTLSMContext_getObjectFunctionIndexRange
+ _GTMTLSMContext_getParentAllocation
+ _GTMTLSMContext_getParentResource
+ _GTMTLSMContext_getRootAllocation
+ _GTMTLSMContext_getTemporalDenoisedScaler
+ _GTMTLSMContext_getTemporalDenoisedScalers
+ _GTMTLSMContext_getTensor
+ _GTMTLSMContext_getTensors
+ _GTMTLSMContext_getTextureViewPool
+ _GTMTLSMContext_getTextureViewPools
+ _GTMTLSMContext_lastRenderPipelineState
+ _GTMTLSMContext_resolveResourceHazardTrackingMode
+ _GTMTLSMContext_resolveRootResourceAllocatedSize
+ _GTMTLSMDepthStencilState_uniqueIdentifierArray
+ _GTMTLSMIOFileHandle_init
+ _GTMTLSMIOHandle_processTraceFuncWithMap
+ _GTMTLSMIOHandle_processTraceFuncWithPool
+ _GTMTLSMObject_lastObject
+ _GTMTLSMObject_objectAtIndex
+ _GTMTLSMRenderPipelineState_MTL4MeshPipelineDescriptor
+ _GTMTLSMRenderPipelineState_MTL4RenderPipelineDescriptor
+ _GTMTLSMRenderPipelineState_MTL4TilePipelineDescriptor
+ _GTMTLSMTensor_init
+ _GTMTLSMTensor_processTraceFuncWithMap
+ _GTMTLSMTensor_processTraceFuncWithPool
+ _GTMTLSMTextureViewPool_init
+ _GTMTLSMTextureViewPool_processTraceFuncWithMap
+ _GTMTLSMTextureViewPool_processTraceFuncWithPool
+ _GTMTLTensorDataType_bytesLength
+ _GTMTLTensorExtentsFromArgs
+ _GTMTLTensorExtentsToArgs
+ _GTMTLTensorExtents_bytesLength
+ _GTMTLTensorExtents_computeStrides
+ _GTMTLTensorSliceFromArgs
+ _GTMTLTensorSliceToArgs
+ _GTMTLTensorSlice_dimensions
+ _GTMTLTensorSlice_origin
+ _GTMTLTensorSlice_wholeSlice
+ _GTMTLTensor_wholeSlice
+ _GTMTLUniqueIdentifierResource_getKey
+ _GTResourceTrackerMakeWithDescriptor
+ _GTResourceTrackerProcessCommandBufferAndResidencySets
+ _GTResourceTrackerUsingFrameInterpolator
+ _GTResourceTrackerUsingMTL4FrameInterpolator
+ _GTSetIntersection
+ _GTString_endsWith
+ _GTTelemetry_addMTL4CommandQueue
+ _GTTelemetry_removeMTL4CommandQueue
+ _GTTelemetry_trackMTL4Commit
+ _GTTraceContext_openChildStream
+ _GTTraceDispatch_setArgumentTableStateForGPUCommandStage
+ _GTTraceDump_buildCommandBufferInfo
+ _GTTraceDump_getCommandBufferCommitIndex
+ _GTTraceDump_getCommandBufferInfo
+ _GTTraceDump_getCommandBufferQueue
+ _GTTraceDump_setCommandBufferInfo
+ _GTTraceDump_writeCaptureDescriptor
+ _GTTraceFuncArgs_getMtl4Commits
+ _GTTraceStream_deviceObjectForDownloader
+ _GTUnstableRemove
+ _GetCommandBufferParentStreamRef
+ _GetObjectStream_
+ _GetUUIDFromMetadata
+ _IORegistryEntryCreateCFProperties
+ _IOServiceNameMatching
+ _IsTextureType1D
+ _IsTextureTypeArray
+ _IsTextureTypeCube
+ _MTL4AddResidencySet
+ _MTL4CommandQueueCaptureResidencySetSnapshots
+ _MTL4CommandQueueTakeSnapshot
+ _MTLDevice_create
+ _MTLDevice_newAccelerationStructureWithDescriptor
+ _MTLDevice_newAccelerationStructureWithSize
+ _MTLDevice_newAccelerationStructureWithSize_resourceIndex
+ _MTLDevice_newAccelerationStructureWithSize_withDescriptor
+ _MTLDevice_newTextureWithDescriptor
+ _MTLFXFrameInterpolatorDescriptor_newFrameInterpolatorWithDevice
+ _MTLFXFrameInterpolatorDescriptor_newFrameInterpolatorWithDeviceIMP
+ _MTLFXFrameInterpolatorDescriptor_newMTL4FrameInterpolatorWithDevice_compiler
+ _MTLFXFrameInterpolatorDescriptor_newMTL4FrameInterpolatorWithDevice_compilerIMP
+ _MTLFXSpatialScalerDescriptor_newMTL4SpatialScalerWithDevice_compiler
+ _MTLFXSpatialScalerDescriptor_newMTL4SpatialScalerWithDevice_compilerIMP
+ _MTLFXTemporalDenoisedScalerDescriptor_newMTL4TemporalDenoisedScalerWithDevice_compiler
+ _MTLFXTemporalDenoisedScalerDescriptor_newMTL4TemporalDenoisedScalerWithDevice_compilerIMP
+ _MTLFXTemporalDenoisedScalerDescriptor_newTemporalDenoisedScalerWithDevice
+ _MTLFXTemporalDenoisedScalerDescriptor_newTemporalDenoisedScalerWithDeviceIMP
+ _MTLFXTemporalScalerDescriptor_newMTL4TemporalScalerWithDevice_compiler
+ _MTLFXTemporalScalerDescriptor_newMTL4TemporalScalerWithDevice_compilerIMP
+ _MTLFailureTypeGetErrorModeType
+ _MTLFailureTypeSetErrorModeType
+ _MTLTensorDataType_bytesLength
+ _MTLTensorExtents_bytesLength
+ _MTLTensorExtents_computeStrides
+ _MTLTensor_bytesLength
+ _MTLTextureSwizzleChannelsToKey
+ _MTLTextureSwizzleKeyToChannels
+ _MakeDYMTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureCurveGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureDescriptor
+ _MakeDYMTL4AccelerationStructureGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _MakeDYMTL4AccelerationStructureTriangleGeometryDescriptor
+ _MakeDYMTL4ComputePipelineDescriptor
+ _MakeDYMTL4FunctionDescriptor
+ _MakeDYMTL4IndirectInstanceAccelerationStructureDescriptor
+ _MakeDYMTL4InstanceAccelerationStructureDescriptor
+ _MakeDYMTL4LibraryFunctionDescriptor
+ _MakeDYMTL4MachineLearningPipelineDescriptor
+ _MakeDYMTL4MeshRenderPipelineDescriptor
+ _MakeDYMTL4PipelineOptions
+ _MakeDYMTL4PipelineStageDynamicLinkingDescriptor
+ _MakeDYMTL4PrimitiveAccelerationStructureDescriptor
+ _MakeDYMTL4RenderPipelineColorAttachmentDescriptor
+ _MakeDYMTL4RenderPipelineDescriptor
+ _MakeDYMTL4SpecializedFunctionDescriptor
+ _MakeDYMTL4TileRenderPipelineDescriptor
+ _MakeDYMTLAccelerationStructureBoundingBoxGeometryDescriptor
+ _MakeDYMTLAccelerationStructureCurveGeometryDescriptor
+ _MakeDYMTLAccelerationStructureGeometryDescriptor
+ _MakeDYMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _MakeDYMTLAccelerationStructureMotionCurveGeometryDescriptor
+ _MakeDYMTLAccelerationStructureMotionTriangleGeometryDescriptor
+ _MakeDYMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
+ _MakeDYMTLAccelerationStructureTriangleGeometryDescriptor
+ _MakeDYMTLAttributeDescriptor
+ _MakeDYMTLBlitPassSampleBufferAttachmentDescriptor
+ _MakeDYMTLBufferLayoutDescriptor
+ _MakeDYMTLComputePassSampleBufferAttachmentDescriptor
+ _MakeDYMTLFunctionConstant
+ _MakeDYMTLMotionKeyframeData
+ _MakeDYMTLPipelineBufferDescriptor
+ _MakeDYMTLPrimitiveAccelerationStructureDescriptor
+ _MakeDYMTLRasterizationRateLayerDescriptor
+ _MakeDYMTLRenderPassColorAttachmentDescriptor
+ _MakeDYMTLRenderPassDepthAttachmentDescriptor
+ _MakeDYMTLRenderPassSampleBufferAttachmentDescriptor
+ _MakeDYMTLRenderPassStencilAttachmentDescriptor
+ _MakeDYMTLResourceStatePassSampleBufferAttachmentDescriptor
+ _MakeDYMTLStencilDescriptor
+ _MakeDYMTLTileRenderPipelineColorAttachmentDescriptor
+ _MakeDYMTLVertexAttributeDescriptor
+ _MakeDYMTLVertexBufferLayoutDescriptor
+ _MakeDYMTLVertexDescriptor
+ _MakeGTMTLLogicalToPhysicalColorAttachmentMap
+ _MakeGTMTLLogicalToPhysicalColorAttachmentMapSPI
+ _MakeGTMTLTensorExtents
+ _MakeMTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _MakeMTL4AccelerationStructureCurveGeometryDescriptor
+ _MakeMTL4AccelerationStructureDescriptor
+ _MakeMTL4AccelerationStructureGeometryDescriptor
+ _MakeMTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _MakeMTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _MakeMTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _MakeMTL4AccelerationStructureTriangleGeometryDescriptor
+ _MakeMTL4ArgumentTableDescriptor
+ _MakeMTL4BinaryFunctionDescriptor
+ _MakeMTL4CommandAllocatorDescriptor
+ _MakeMTL4CommandQueueDescriptor
+ _MakeMTL4CompilerDescriptor
+ _MakeMTL4CompilerTaskOptions
+ _MakeMTL4ComputePipelineDescriptor
+ _MakeMTL4FunctionDescriptor
+ _MakeMTL4IndirectInstanceAccelerationStructureDescriptor
+ _MakeMTL4InstanceAccelerationStructureDescriptor
+ _MakeMTL4LibraryDescriptor
+ _MakeMTL4LibraryFunctionDescriptor
+ _MakeMTL4MachineLearningPipelineDescriptor
+ _MakeMTL4MeshRenderPipelineDescriptor
+ _MakeMTL4PipelineDataSetSerializerDescriptor
+ _MakeMTL4PipelineDescriptor
+ _MakeMTL4PipelineStageDynamicLinkingDescriptor
+ _MakeMTL4PrimitiveAccelerationStructureDescriptor
+ _MakeMTL4RenderPassDescriptor
+ _MakeMTL4RenderPipelineDescriptor
+ _MakeMTL4RenderPipelineDynamicLinkingDescriptor
+ _MakeMTL4SpecializedFunctionDescriptor
+ _MakeMTL4TileRenderPipelineDescriptor
+ _MakeMTLAccelerationStructureBoundingBoxGeometryDescriptor
+ _MakeMTLAccelerationStructureCurveGeometryDescriptor
+ _MakeMTLAccelerationStructureGeometryDescriptor
+ _MakeMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _MakeMTLAccelerationStructureMotionCurveGeometryDescriptor
+ _MakeMTLAccelerationStructureMotionTriangleGeometryDescriptor
+ _MakeMTLAccelerationStructureTriangleGeometryDescriptor
+ _MakeMTLFXFrameInterpolatorDescriptor
+ _MakeMTLFXTemporalDenoisedScalerDescriptor
+ _MakeMTLIndirectInstanceAccelerationStructureDescriptor
+ _MakeMTLInstanceAccelerationStructureDescriptor
+ _MakeMTLLogicalToPhysicalColorAttachmentMap
+ _MakeMTLLogicalToPhysicalColorAttachmentMapSPI
+ _MakeMTLPrimitiveAccelerationStructureDescriptor
+ _MakeMTLResourceViewPoolDescriptor
+ _MakeMTLResourceViewPoolDescriptorWithBaseResourceID
+ _MakeMTLResourceViewPoolDescriptorWithoutBaseResourceID
+ _MakeMTLTensorDescriptorWithResourceIndex
+ _MakeMTLTensorDescriptorWithoutResourceIndex
+ _MakeMTLTensorExtents
+ _MakeMTLTextureViewDescriptor
+ _MakeNestedMTL4PipelineOptions
+ _MakeNestedMTL4PipelineStageDynamicLinkingDescriptor
+ _MakeNestedMTL4RenderPipelineColorAttachmentDescriptor
+ _MakeNestedMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
+ _MakeNestedMTLAttributeDescriptor
+ _MakeNestedMTLBlitPassSampleBufferAttachmentDescriptor
+ _MakeNestedMTLBufferLayoutDescriptor
+ _MakeNestedMTLComputePassSampleBufferAttachmentDescriptor
+ _MakeNestedMTLLinkedFunctions
+ _MakeNestedMTLLinkedFunctionsAuto
+ _MakeNestedMTLMotionKeyframeData
+ _MakeNestedMTLPipelineBufferDescriptor
+ _MakeNestedMTLRenderPassAttachmentDescriptor
+ _MakeNestedMTLRenderPassColorAttachmentDescriptor
+ _MakeNestedMTLRenderPassDepthAttachmentDescriptor
+ _MakeNestedMTLRenderPassSampleBufferAttachmentDescriptor
+ _MakeNestedMTLRenderPassStencilAttachmentDescriptor
+ _MakeNestedMTLRenderPipelineColorAttachmentDescriptor
+ _MakeNestedMTLResourceStatePassSampleBufferAttachmentDescriptor
+ _MakeNestedMTLStageInputOutputDescriptor
+ _MakeNestedMTLStencilDescriptor
+ _MakeNestedMTLTileRenderPipelineColorAttachmentDescriptor
+ _MakeNestedMTLVertexAttributeDescriptor
+ _MakeNestedMTLVertexBufferLayoutDescriptor
+ _MakeNestedMTLVertexDescriptor
+ _OBJC_CLASS_$_CaptureMTL4Archive
+ _OBJC_CLASS_$_CaptureMTL4ArgumentTable
+ _OBJC_CLASS_$_CaptureMTL4BinaryFunction
+ _OBJC_CLASS_$_CaptureMTL4CommandAllocator
+ _OBJC_CLASS_$_CaptureMTL4CommandBuffer
+ _OBJC_CLASS_$_CaptureMTL4CommandQueue
+ _OBJC_CLASS_$_CaptureMTL4Compiler
+ _OBJC_CLASS_$_CaptureMTL4ComputeCommandEncoder
+ _OBJC_CLASS_$_CaptureMTL4FXFrameInterpolator
+ _OBJC_CLASS_$_CaptureMTL4FXSpatialScaler
+ _OBJC_CLASS_$_CaptureMTL4FXTemporalDenoisedScaler
+ _OBJC_CLASS_$_CaptureMTL4FXTemporalScaler
+ _OBJC_CLASS_$_CaptureMTL4MachineLearningCommandEncoder
+ _OBJC_CLASS_$_CaptureMTL4MachineLearningPipelineState
+ _OBJC_CLASS_$_CaptureMTL4PipelineDataSetSerializer
+ _OBJC_CLASS_$_CaptureMTL4RenderCommandEncoder
+ _OBJC_CLASS_$_CaptureMTLFXFrameInterpolator
+ _OBJC_CLASS_$_CaptureMTLFXTemporalDenoisedScaler
+ _OBJC_CLASS_$_CaptureMTLTensor
+ _OBJC_CLASS_$_CaptureMTLTextureViewPool
+ _OBJC_CLASS_$_MTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureCurveGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _OBJC_CLASS_$_MTL4AccelerationStructureTriangleGeometryDescriptor
+ _OBJC_CLASS_$_MTL4ArgumentTableDescriptor
+ _OBJC_CLASS_$_MTL4BinaryFunctionDescriptor
+ _OBJC_CLASS_$_MTL4CommandAllocatorDescriptor
+ _OBJC_CLASS_$_MTL4CommandQueueDescriptor
+ _OBJC_CLASS_$_MTL4CommitOptions
+ _OBJC_CLASS_$_MTL4CompilerDescriptor
+ _OBJC_CLASS_$_MTL4CompilerTaskOptions
+ _OBJC_CLASS_$_MTL4ComputePipelineDescriptor
+ _OBJC_CLASS_$_MTL4IndirectInstanceAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4InstanceAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4LibraryDescriptor
+ _OBJC_CLASS_$_MTL4LibraryFunctionDescriptor
+ _OBJC_CLASS_$_MTL4MachineLearningPipelineDescriptor
+ _OBJC_CLASS_$_MTL4MeshRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4PipelineDataSetSerializerDescriptor
+ _OBJC_CLASS_$_MTL4PipelineOptions
+ _OBJC_CLASS_$_MTL4PipelineStageDynamicLinkingDescriptor
+ _OBJC_CLASS_$_MTL4PrimitiveAccelerationStructureDescriptor
+ _OBJC_CLASS_$_MTL4RenderPassDescriptor
+ _OBJC_CLASS_$_MTL4RenderPipelineDescriptor
+ _OBJC_CLASS_$_MTL4RenderPipelineDynamicLinkingDescriptor
+ _OBJC_CLASS_$_MTL4SpecializedFunctionDescriptor
+ _OBJC_CLASS_$_MTL4StitchedFunctionDescriptor
+ _OBJC_CLASS_$_MTL4TileRenderPipelineDescriptor
+ _OBJC_CLASS_$_MTLFXFrameInterpolatorDescriptor
+ _OBJC_CLASS_$_MTLFXTemporalDenoisedScalerDescriptor
+ _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMap
+ _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
+ _OBJC_CLASS_$_MTLResourceViewPoolDescriptor
+ _OBJC_CLASS_$_MTLTensorDescriptor
+ _OBJC_CLASS_$_MTLTensorExtents
+ _OBJC_CLASS_$_MTLTextureViewDescriptor
+ _OBJC_CLASS_$_MTLVertexDescriptor
+ _OBJC_METACLASS_$_CaptureMTL4Archive
+ _OBJC_METACLASS_$_CaptureMTL4ArgumentTable
+ _OBJC_METACLASS_$_CaptureMTL4BinaryFunction
+ _OBJC_METACLASS_$_CaptureMTL4CommandAllocator
+ _OBJC_METACLASS_$_CaptureMTL4CommandBuffer
+ _OBJC_METACLASS_$_CaptureMTL4CommandQueue
+ _OBJC_METACLASS_$_CaptureMTL4Compiler
+ _OBJC_METACLASS_$_CaptureMTL4ComputeCommandEncoder
+ _OBJC_METACLASS_$_CaptureMTL4FXFrameInterpolator
+ _OBJC_METACLASS_$_CaptureMTL4FXSpatialScaler
+ _OBJC_METACLASS_$_CaptureMTL4FXTemporalDenoisedScaler
+ _OBJC_METACLASS_$_CaptureMTL4FXTemporalScaler
+ _OBJC_METACLASS_$_CaptureMTL4MachineLearningCommandEncoder
+ _OBJC_METACLASS_$_CaptureMTL4MachineLearningPipelineState
+ _OBJC_METACLASS_$_CaptureMTL4PipelineDataSetSerializer
+ _OBJC_METACLASS_$_CaptureMTL4RenderCommandEncoder
+ _OBJC_METACLASS_$_CaptureMTLFXFrameInterpolator
+ _OBJC_METACLASS_$_CaptureMTLFXTemporalDenoisedScaler
+ _OBJC_METACLASS_$_CaptureMTLTensor
+ _OBJC_METACLASS_$_CaptureMTLTextureViewPool
+ _ReenableMTLDebugErrors
+ _ResidencySetAllocationsContainDrawableTexture
+ _ResidencySetHashContainsDrawableTexture
+ _ResourceAccess_isArgumentBuffer
+ _ResourceTracker_addDynamicLinkingDescriptor
+ _ResourceTracker_addTextureViewPools
+ _RetrieveGPUCaptureTexture
+ _SaveDYMTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureCurveGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureDescriptor
+ _SaveDYMTL4AccelerationStructureGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _SaveDYMTL4AccelerationStructureTriangleGeometryDescriptor
+ _SaveDYMTL4ComputePipelineDescriptor
+ _SaveDYMTL4FunctionDescriptor
+ _SaveDYMTL4IndirectInstanceAccelerationStructureDescriptor
+ _SaveDYMTL4InstanceAccelerationStructureDescriptor
+ _SaveDYMTL4LibraryFunctionDescriptor
+ _SaveDYMTL4MachineLearningPipelineDescriptor
+ _SaveDYMTL4MeshRenderPipelineDescriptor
+ _SaveDYMTL4PipelineOptions
+ _SaveDYMTL4PipelineStageDynamicLinkingDescriptor
+ _SaveDYMTL4PrimitiveAccelerationStructureDescriptor
+ _SaveDYMTL4RenderPipelineColorAttachmentDescriptor
+ _SaveDYMTL4RenderPipelineDescriptor
+ _SaveDYMTL4SpecializedFunctionDescriptor
+ _SaveDYMTL4TileRenderPipelineDescriptor
+ _SaveDYMTLAccelerationStructureBoundingBoxGeometryDescriptor
+ _SaveDYMTLAccelerationStructureCurveGeometryDescriptor
+ _SaveDYMTLAccelerationStructureGeometryDescriptor
+ _SaveDYMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _SaveDYMTLAccelerationStructureMotionCurveGeometryDescriptor
+ _SaveDYMTLAccelerationStructureMotionTriangleGeometryDescriptor
+ _SaveDYMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
+ _SaveDYMTLAccelerationStructureTriangleGeometryDescriptor
+ _SaveDYMTLAttributeDescriptor
+ _SaveDYMTLBlitPassSampleBufferAttachmentDescriptor
+ _SaveDYMTLBufferLayoutDescriptor
+ _SaveDYMTLComputePassSampleBufferAttachmentDescriptor
+ _SaveDYMTLFunctionConstant
+ _SaveDYMTLPipelineBufferDescriptor
+ _SaveDYMTLRasterizationRateLayerDescriptor
+ _SaveDYMTLRenderPassColorAttachmentDescriptor
+ _SaveDYMTLRenderPassDepthAttachmentDescriptor
+ _SaveDYMTLRenderPassSampleBufferAttachmentDescriptor
+ _SaveDYMTLRenderPassStencilAttachmentDescriptor
+ _SaveDYMTLResourceStatePassSampleBufferAttachmentDescriptor
+ _SaveDYMTLStageInputOutputDescriptor
+ _SaveDYMTLTileRenderPipelineColorAttachmentDescriptor
+ _SaveDYMTLVertexAttributeDescriptor
+ _SaveDYMTLVertexBufferLayoutDescriptor
+ _SaveDYMTLVertexDescriptor
+ _SaveGTMTLSize
+ _SaveGTMTLTensorExtents
+ _SaveMTL4ArgumentTableDescriptor
+ _SaveMTL4BinaryFunctionDescriptor
+ _SaveMTL4CommandAllocatorDescriptor
+ _SaveMTL4CommandQueueDescriptor
+ _SaveMTL4CompilerDescriptor
+ _SaveMTL4CompilerTaskOptions
+ _SaveMTL4ComputePipelineDescriptor
+ _SaveMTL4FunctionDescriptor
+ _SaveMTL4LibraryDescriptor
+ _SaveMTL4MachineLearningPipelineDescriptor
+ _SaveMTL4MachineLearningPipelineReflection
+ _SaveMTL4PipelineDataSetSerializerDescriptor
+ _SaveMTL4PipelineDescriptor
+ _SaveMTL4PipelineStageDynamicLinkingDescriptor
+ _SaveMTL4RenderPassDescriptor
+ _SaveMTL4RenderPipelineDynamicLinkingDescriptor
+ _SaveMTLComputePipelineReflectionMTL4
+ _SaveMTLDepthStencilStateInfo
+ _SaveMTLFXFrameInterpolatorDescriptor
+ _SaveMTLFXTemporalDenoisedScalerDescriptor
+ _SaveMTLFunctionHandleInfo
+ _SaveMTLPipelineReflectionMTL4
+ _SaveMTLRenderPipelineReflectionCommon
+ _SaveMTLResourceViewPoolDescriptor
+ _SaveMTLTensorDescriptor
+ _SaveMTLTensorInfo
+ _SaveMTLTextureViewDescriptor
+ _StoreMTL4ArgumentTableDescriptorUsingEncode
+ _StoreMTL4CommandAllocatorDescriptorUsingEncode
+ _StoreMTL4CommandQueueDescriptorUsingEncode
+ _StoreMTL4CompilerDescriptorUsingEncode
+ _StoreMTL4CompilerTaskOptionsUsingEncode
+ _StoreMTL4LibraryDescriptorUsingEncode
+ _StoreMTL4PipelineDescriptorUsingEncode
+ _StoreMTL4PipelineStageDynamicLinkingDescriptorUsingEncode
+ _StoreMTL4RenderPassDescriptorUsingEncode
+ _StoreMTL4RenderPipelineDynamicLinkingDescriptorUsingEncode
+ _StoreMTLCaptureDescriptorInternalUsingEncode
+ _StoreMTLFXFrameInterpolatorDescriptorUsingEncode
+ _StoreMTLFXTemporalDenoisedScalerDescriptorUsingEncode
+ _StoreMTLResourceViewPoolDescriptorUsingEncode
+ _StoreMTLTensorDescriptorUsingEncode
+ _StoreMTLTextureViewDescriptorUsingEncode
+ _TextureViewPoolTakeSnapshot
+ _TranslateGTMTL4ArgumentTableDescriptor
+ _TranslateGTMTL4BinaryFunctionDescriptor
+ _TranslateGTMTL4CommandAllocatorDescriptor
+ _TranslateGTMTL4CommandQueueDescriptor
+ _TranslateGTMTL4CompilerDescriptor
+ _TranslateGTMTL4CompilerTaskOptions
+ _TranslateGTMTL4FunctionDescriptor
+ _TranslateGTMTL4FunctionDescriptorNested
+ _TranslateGTMTL4FunctionDescriptorReflection
+ _TranslateGTMTL4LibraryDescriptor
+ _TranslateGTMTL4MachineLearningPipelineReflection
+ _TranslateGTMTL4PipelineDataSetSerializerDescriptor
+ _TranslateGTMTL4PipelineDescriptor
+ _TranslateGTMTL4PipelineStageDynamicLinkingDescriptor
+ _TranslateGTMTL4RenderPassDescriptor
+ _TranslateGTMTL4RenderPipelineDynamicLinkingDescriptor
+ _TranslateGTMTLDepthStencilStateInfo
+ _TranslateGTMTLFXFrameInterpolatorDescriptor
+ _TranslateGTMTLFXTemporalDenoisedScalerDescriptor
+ _TranslateGTMTLFunctionHandleInfo
+ _TranslateGTMTLResourceViewPoolDescriptor
+ _TranslateGTMTLTensorDescriptor
+ _TranslateGTMTLTensorInfo
+ _TranslateGTMTLTextureDescriptorDirectly
+ _TranslateGTMTLTextureViewDescriptor
+ _TranslateGTMTLTextureViewDescriptorDirectly
+ _TranslateNestedGTMTL4AccelerationStructureBoundingBoxGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureCurveGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureMotionCurveGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureMotionTriangleGeometryDescriptor
+ _TranslateNestedGTMTL4AccelerationStructureTriangleGeometryDescriptor
+ _TranslateNestedGTMTL4ComputePipelineDescriptor
+ _TranslateNestedGTMTL4IndirectInstanceAccelerationStructureDescriptor
+ _TranslateNestedGTMTL4InstanceAccelerationStructureDescriptor
+ _TranslateNestedGTMTL4LibraryFunctionDescriptor
+ _TranslateNestedGTMTL4MachineLearningPipelineDescriptor
+ _TranslateNestedGTMTL4MeshRenderPipelineDescriptor
+ _TranslateNestedGTMTL4PipelineOptions
+ _TranslateNestedGTMTL4PipelineStageDynamicLinkingDescriptor
+ _TranslateNestedGTMTL4PrimitiveAccelerationStructureDescriptor
+ _TranslateNestedGTMTL4RenderPipelineColorAttachmentDescriptor
+ _TranslateNestedGTMTL4RenderPipelineDescriptor
+ _TranslateNestedGTMTL4SpecializedFunctionDescriptor
+ _TranslateNestedGTMTL4TileRenderPipelineDescriptor
+ _TranslateNestedGTMTLAccelerationStructureBoundingBoxGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructureCurveGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructureGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructureMotionCurveGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructureMotionTriangleGeometryDescriptor
+ _TranslateNestedGTMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
+ _TranslateNestedGTMTLAccelerationStructureTriangleGeometryDescriptor
+ _TranslateNestedGTMTLAttributeDescriptor
+ _TranslateNestedGTMTLBlitPassSampleBufferAttachmentDescriptor
+ _TranslateNestedGTMTLBufferLayoutDescriptor
+ _TranslateNestedGTMTLComputePassSampleBufferAttachmentDescriptor
+ _TranslateNestedGTMTLIndirectInstanceAccelerationStructureDescriptor
+ _TranslateNestedGTMTLInstanceAccelerationStructureDescriptor
+ _TranslateNestedGTMTLLinkedFunctions
+ _TranslateNestedGTMTLLinkedFunctionsAuto
+ _TranslateNestedGTMTLMotionKeyframeData
+ _TranslateNestedGTMTLPipelineBufferDescriptor
+ _TranslateNestedGTMTLPrimitiveAccelerationStructureDescriptor
+ _TranslateNestedGTMTLRenderPassAttachmentDescriptor
+ _TranslateNestedGTMTLRenderPassColorAttachmentDescriptor
+ _TranslateNestedGTMTLRenderPassDepthAttachmentDescriptor
+ _TranslateNestedGTMTLRenderPassSampleBufferAttachmentDescriptor
+ _TranslateNestedGTMTLRenderPassStencilAttachmentDescriptor
+ _TranslateNestedGTMTLRenderPipelineColorAttachmentDescriptor
+ _TranslateNestedGTMTLResourceStatePassSampleBufferAttachmentDescriptor
+ _TranslateNestedGTMTLStageInputOutputDescriptor
+ _TranslateNestedGTMTLStencilDescriptor
+ _TranslateNestedGTMTLTileRenderPipelineColorAttachmentDescriptor
+ _TranslateNestedGTMTLVertexAttributeDescriptor
+ _TranslateNestedGTMTLVertexBufferLayoutDescriptor
+ _TranslateNestedGTMTLVertexDescriptor
+ _TryGetRestartReportString
+ _WriteArgumentTableForGPUCommandStage
+ _WriteDepthStencilStateInfo
+ _WriteDepthStencilStateInfo_
+ _WriteFunctionHandleInfo
+ _WriteFunctionHandleInfo_
+ _WriteGTMTLAnySMCommandQueue_residencySets
+ _WriteGTMTLAnySMCommandQueue_residencySetsDelta
+ _WriteGTMTLSMTextureViewPool
+ _WriteResidencySets
+ _WriteTensorInfo
+ __Block_byref_object_copy_.11476
+ __Block_byref_object_copy_.3870
+ __Block_byref_object_copy_.4375
+ __Block_byref_object_dispose_.11477
+ __Block_byref_object_dispose_.3871
+ __Block_byref_object_dispose_.4376
+ __GTAccelerationStructureDescriptorDownloader_MTL4_postProcess_block_invoke.41
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4Archive
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4ArgumentTable
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4BinaryFunction
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4CommandAllocator
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4CommandBuffer
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4CommandQueue
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4Compiler
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4ComputeCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4FXFrameInterpolator
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4FXSpatialScaler
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4FXTemporalScaler
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4MachineLearningPipelineState
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4RenderCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_CaptureMTLFXFrameInterpolator
+ __OBJC_$_INSTANCE_METHODS_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_METHODS_CaptureMTLTensor
+ __OBJC_$_INSTANCE_METHODS_CaptureMTLTextureViewPool
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4Archive
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4ArgumentTable
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4BinaryFunction
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4CommandAllocator
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4CommandBuffer
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4CommandQueue
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4Compiler
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4ComputeCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4FXFrameInterpolator
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4FXSpatialScaler
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4FXTemporalScaler
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4MachineLearningPipelineState
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4RenderCommandEncoder
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTLFXFrameInterpolator
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTLTensor
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTLTextureViewPool
+ __OBJC_$_PROP_LIST_CaptureMTL4Archive
+ __OBJC_$_PROP_LIST_CaptureMTL4ArgumentTable
+ __OBJC_$_PROP_LIST_CaptureMTL4BinaryFunction
+ __OBJC_$_PROP_LIST_CaptureMTL4CommandAllocator
+ __OBJC_$_PROP_LIST_CaptureMTL4CommandBuffer
+ __OBJC_$_PROP_LIST_CaptureMTL4CommandQueue
+ __OBJC_$_PROP_LIST_CaptureMTL4Compiler
+ __OBJC_$_PROP_LIST_CaptureMTL4ComputeCommandEncoder
+ __OBJC_$_PROP_LIST_CaptureMTL4FXFrameInterpolator
+ __OBJC_$_PROP_LIST_CaptureMTL4FXSpatialScaler
+ __OBJC_$_PROP_LIST_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROP_LIST_CaptureMTL4FXTemporalScaler
+ __OBJC_$_PROP_LIST_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_$_PROP_LIST_CaptureMTL4MachineLearningPipelineState
+ __OBJC_$_PROP_LIST_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_$_PROP_LIST_CaptureMTL4RenderCommandEncoder
+ __OBJC_$_PROP_LIST_CaptureMTLFXFrameInterpolator
+ __OBJC_$_PROP_LIST_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_$_PROP_LIST_CaptureMTLTensor
+ __OBJC_$_PROP_LIST_CaptureMTLTextureViewPool
+ __OBJC_$_PROP_LIST_MTL4Archive
+ __OBJC_$_PROP_LIST_MTL4ArgumentTable
+ __OBJC_$_PROP_LIST_MTL4BinaryFunction
+ __OBJC_$_PROP_LIST_MTL4BinaryFunctionSPI
+ __OBJC_$_PROP_LIST_MTL4CommandAllocator
+ __OBJC_$_PROP_LIST_MTL4CommandBuffer
+ __OBJC_$_PROP_LIST_MTL4CommandEncoder
+ __OBJC_$_PROP_LIST_MTL4CommandQueue
+ __OBJC_$_PROP_LIST_MTL4Compiler
+ __OBJC_$_PROP_LIST_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROP_LIST_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROP_LIST_MTL4MachineLearningPipelineState
+ __OBJC_$_PROP_LIST_MTL4RenderCommandEncoder
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROP_LIST_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROP_LIST_MTLFXSpatialScalerBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROP_LIST_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROP_LIST_MTLFXTemporalScalerBase
+ __OBJC_$_PROP_LIST_MTLResourceViewPool
+ __OBJC_$_PROP_LIST_MTLTensor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTObservableService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4Archive
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4Compiler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXTemporalScalerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTensor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTextureViewPool
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTObservableService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4Archive
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4Compiler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXTemporalScalerBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTensor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTextureViewPool
+ __OBJC_$_PROTOCOL_REFS_GTMTLCaptureService
+ __OBJC_$_PROTOCOL_REFS_GTMTLTelemetryService
+ __OBJC_$_PROTOCOL_REFS_MTL4Archive
+ __OBJC_$_PROTOCOL_REFS_MTL4ArgumentTable
+ __OBJC_$_PROTOCOL_REFS_MTL4ArgumentTableSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4BinaryFunction
+ __OBJC_$_PROTOCOL_REFS_MTL4BinaryFunctionSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandAllocator
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandBuffer
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4CommandQueue
+ __OBJC_$_PROTOCOL_REFS_MTL4Compiler
+ __OBJC_$_PROTOCOL_REFS_MTL4ComputeCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4ComputeCommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXFrameInterpolator
+ __OBJC_$_PROTOCOL_REFS_MTL4FXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXSpatialScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4FXSpatialScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4FXTemporalScaler
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4MachineLearningPipelineState
+ __OBJC_$_PROTOCOL_REFS_MTL4PipelineDataSetSerializer
+ __OBJC_$_PROTOCOL_REFS_MTL4RenderCommandEncoder
+ __OBJC_$_PROTOCOL_REFS_MTL4RenderCommandEncoderSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolator
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXFrameInterpolatorSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXSpatialScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScaler
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_$_PROTOCOL_REFS_MTLFXTemporalScalerBase
+ __OBJC_$_PROTOCOL_REFS_MTLResourceViewPool
+ __OBJC_$_PROTOCOL_REFS_MTLTensor
+ __OBJC_$_PROTOCOL_REFS_MTLTextureViewPool
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4Archive
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4ArgumentTable
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4BinaryFunction
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4CommandAllocator
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4CommandBuffer
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4CommandQueue
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4Compiler
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4ComputeCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4FXFrameInterpolator
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4FXSpatialScaler
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4FXTemporalScaler
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4MachineLearningPipelineState
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4RenderCommandEncoder
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTLFXFrameInterpolator
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTLTensor
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTLTextureViewPool
+ __OBJC_CLASS_RO_$_CaptureMTL4Archive
+ __OBJC_CLASS_RO_$_CaptureMTL4ArgumentTable
+ __OBJC_CLASS_RO_$_CaptureMTL4BinaryFunction
+ __OBJC_CLASS_RO_$_CaptureMTL4CommandAllocator
+ __OBJC_CLASS_RO_$_CaptureMTL4CommandBuffer
+ __OBJC_CLASS_RO_$_CaptureMTL4CommandQueue
+ __OBJC_CLASS_RO_$_CaptureMTL4Compiler
+ __OBJC_CLASS_RO_$_CaptureMTL4ComputeCommandEncoder
+ __OBJC_CLASS_RO_$_CaptureMTL4FXFrameInterpolator
+ __OBJC_CLASS_RO_$_CaptureMTL4FXSpatialScaler
+ __OBJC_CLASS_RO_$_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_CLASS_RO_$_CaptureMTL4FXTemporalScaler
+ __OBJC_CLASS_RO_$_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_CLASS_RO_$_CaptureMTL4MachineLearningPipelineState
+ __OBJC_CLASS_RO_$_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_CLASS_RO_$_CaptureMTL4RenderCommandEncoder
+ __OBJC_CLASS_RO_$_CaptureMTLFXFrameInterpolator
+ __OBJC_CLASS_RO_$_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_CLASS_RO_$_CaptureMTLTensor
+ __OBJC_CLASS_RO_$_CaptureMTLTextureViewPool
+ __OBJC_LABEL_PROTOCOL_$_GTObservableService
+ __OBJC_LABEL_PROTOCOL_$_MTL4Archive
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArgumentTable
+ __OBJC_LABEL_PROTOCOL_$_MTL4ArgumentTableSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4BinaryFunction
+ __OBJC_LABEL_PROTOCOL_$_MTL4BinaryFunctionSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandAllocator
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandBuffer
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4CommandQueue
+ __OBJC_LABEL_PROTOCOL_$_MTL4Compiler
+ __OBJC_LABEL_PROTOCOL_$_MTL4ComputeCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4ComputeCommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXFrameInterpolatorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXSpatialScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXSpatialScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXTemporalScaler
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4MachineLearningPipelineState
+ __OBJC_LABEL_PROTOCOL_$_MTL4PipelineDataSetSerializer
+ __OBJC_LABEL_PROTOCOL_$_MTL4RenderCommandEncoder
+ __OBJC_LABEL_PROTOCOL_$_MTL4RenderCommandEncoderSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXSpatialScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_LABEL_PROTOCOL_$_MTLFXTemporalScalerBase
+ __OBJC_LABEL_PROTOCOL_$_MTLResourceViewPool
+ __OBJC_LABEL_PROTOCOL_$_MTLTensor
+ __OBJC_LABEL_PROTOCOL_$_MTLTextureViewPool
+ __OBJC_METACLASS_RO_$_CaptureMTL4Archive
+ __OBJC_METACLASS_RO_$_CaptureMTL4ArgumentTable
+ __OBJC_METACLASS_RO_$_CaptureMTL4BinaryFunction
+ __OBJC_METACLASS_RO_$_CaptureMTL4CommandAllocator
+ __OBJC_METACLASS_RO_$_CaptureMTL4CommandBuffer
+ __OBJC_METACLASS_RO_$_CaptureMTL4CommandQueue
+ __OBJC_METACLASS_RO_$_CaptureMTL4Compiler
+ __OBJC_METACLASS_RO_$_CaptureMTL4ComputeCommandEncoder
+ __OBJC_METACLASS_RO_$_CaptureMTL4FXFrameInterpolator
+ __OBJC_METACLASS_RO_$_CaptureMTL4FXSpatialScaler
+ __OBJC_METACLASS_RO_$_CaptureMTL4FXTemporalDenoisedScaler
+ __OBJC_METACLASS_RO_$_CaptureMTL4FXTemporalScaler
+ __OBJC_METACLASS_RO_$_CaptureMTL4MachineLearningCommandEncoder
+ __OBJC_METACLASS_RO_$_CaptureMTL4MachineLearningPipelineState
+ __OBJC_METACLASS_RO_$_CaptureMTL4PipelineDataSetSerializer
+ __OBJC_METACLASS_RO_$_CaptureMTL4RenderCommandEncoder
+ __OBJC_METACLASS_RO_$_CaptureMTLFXFrameInterpolator
+ __OBJC_METACLASS_RO_$_CaptureMTLFXTemporalDenoisedScaler
+ __OBJC_METACLASS_RO_$_CaptureMTLTensor
+ __OBJC_METACLASS_RO_$_CaptureMTLTextureViewPool
+ __OBJC_PROTOCOL_$_GTObservableService
+ __OBJC_PROTOCOL_$_MTL4Archive
+ __OBJC_PROTOCOL_$_MTL4ArgumentTable
+ __OBJC_PROTOCOL_$_MTL4ArgumentTableSPI
+ __OBJC_PROTOCOL_$_MTL4BinaryFunction
+ __OBJC_PROTOCOL_$_MTL4BinaryFunctionSPI
+ __OBJC_PROTOCOL_$_MTL4CommandAllocator
+ __OBJC_PROTOCOL_$_MTL4CommandBuffer
+ __OBJC_PROTOCOL_$_MTL4CommandEncoder
+ __OBJC_PROTOCOL_$_MTL4CommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTL4CommandQueue
+ __OBJC_PROTOCOL_$_MTL4Compiler
+ __OBJC_PROTOCOL_$_MTL4ComputeCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4ComputeCommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTL4FXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTL4FXFrameInterpolatorSPI
+ __OBJC_PROTOCOL_$_MTL4FXSpatialScaler
+ __OBJC_PROTOCOL_$_MTL4FXSpatialScalerSPI
+ __OBJC_PROTOCOL_$_MTL4FXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTL4FXTemporalScaler
+ __OBJC_PROTOCOL_$_MTL4MachineLearningCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4MachineLearningPipelineState
+ __OBJC_PROTOCOL_$_MTL4PipelineDataSetSerializer
+ __OBJC_PROTOCOL_$_MTL4RenderCommandEncoder
+ __OBJC_PROTOCOL_$_MTL4RenderCommandEncoderSPI
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolator
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorBase
+ __OBJC_PROTOCOL_$_MTLFXFrameInterpolatorSPI
+ __OBJC_PROTOCOL_$_MTLFXSpatialScalerBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScaler
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerBase
+ __OBJC_PROTOCOL_$_MTLFXTemporalDenoisedScalerSPI
+ __OBJC_PROTOCOL_$_MTLFXTemporalScalerBase
+ __OBJC_PROTOCOL_$_MTLResourceViewPool
+ __OBJC_PROTOCOL_$_MTLTensor
+ __OBJC_PROTOCOL_$_MTLTextureViewPool
+ __OBJC_PROTOCOL_REFERENCE_$_MTL4CommandQueue
+ __ZL16InitNewTransportP19GTMTLGuestAppClient
+ __ZNSt3__16vectorI16GTTelemetryLayerNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
+ __ZNSt3__16vectorI17GTTelemetryDeviceNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ ___52-[CaptureMTLCommandQueue insertDebugCaptureBoundary]_block_invoke
+ ___60-[CaptureMTL4CommandQueue initWithBaseObject:captureDevice:]_block_invoke
+ ___62-[CaptureMTL4CommandQueue _addScheduledTrigger:count:atIndex:]_block_invoke
+ ___63-[CaptureMTL4CommandQueue _commitCommandBuffers:count:atIndex:]_block_invoke
+ ___74-[CaptureMTLCommandBuffer initWithBaseObject:captureCommandQueue:funcRef:]_block_invoke_2
+ ___FillGTMTLCaptureDescriptor_block_invoke
+ ___FillGTMTLCaptureDescriptor_block_invoke_2
+ ___GTAccelerationStructureDescriptorDownloader_MTL4_make_block_invoke
+ ___GTAccelerationStructureDescriptorDownloader_MTL4_postProcess_block_invoke
+ ___GTCaptureArchive_addFile_block_invoke
+ ___GTCoreLogInit_block_invoke
+ ___GTCoreLog_getLogForTag_block_invoke
+ ___GTCorePlatformInfoGet_block_invoke
+ ___GTMTLCaptureEventBuffer_add_block_invoke
+ ___GTMTLDecodeIndirectRenderCommandBuffer_block_invoke_2
+ ___GTTelemetry_trackMTL4Commit_block_invoke
+ ___SaveMTLPipelineReflectionMTL4_block_invoke
+ ___block_descriptor_40_e8_32r_e29_v24?0"<MTLSharedEvent>"8Q16lr32l8
+ ___block_descriptor_40_e8_32s_e1269_v28?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLVertexAttribute}^{GTMTLAttribute}^**}16B24ls32l8
+ ___block_descriptor_44_e5_v8?0l
+ ___block_descriptor_48_e30_v16?0"<MTL4CommitFeedback>"8l
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e9_v16?0r*8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e9_v16?0r*8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___snprintf_chk
+ ___sprintf_chk
+ __block_descriptor_tmp.14824
+ __block_literal_global.10220
+ __block_literal_global.10716
+ __block_literal_global.11480
+ __block_literal_global.11925
+ __block_literal_global.124
+ __block_literal_global.127
+ __block_literal_global.128
+ __block_literal_global.14736
+ __block_literal_global.14922
+ __block_literal_global.14990
+ __block_literal_global.15003
+ __block_literal_global.1659
+ __block_literal_global.181
+ __block_literal_global.19894
+ __block_literal_global.205
+ __block_literal_global.266
+ __block_literal_global.269
+ __block_literal_global.2919
+ __block_literal_global.359
+ __block_literal_global.363
+ __block_literal_global.365
+ __block_literal_global.4196
+ __block_literal_global.43
+ __block_literal_global.4384
+ __block_literal_global.54
+ __block_literal_global.7224
+ __block_literal_global.74
+ __block_literal_global.7992
+ __block_literal_global.8412
+ __block_literal_global.9374
+ __setMTLDeviceProfile
+ _apr_array_push_n
+ _compression_encode_buffer
+ _compression_encode_scratch_buffer_size
+ _copyAndNullifyReferencesInAccelerationStructureDescriptor
+ _dispatch_data_create
+ _eventBuffer
+ _g_completedCommandBufferCallback
+ _gt_error_assert_add_error
+ _gt_snprintf
+ _hostname
+ _hwtarget
+ _newDYMTL4CommandQueueInfo
+ _null_string
+ _objc_msgSend$__waitUntilCompletedAsync:
+ _objc_msgSend$__waitUntilScheduledAsync:
+ _objc_msgSend$_addRequestsToDownloadQueueForCommandBuffers:count:atIndex:
+ _objc_msgSend$_addScheduledTrigger:count:atIndex:
+ _objc_msgSend$_commitCommandBuffers:count:atIndex:
+ _objc_msgSend$_encodeDownloadPoint:
+ _objc_msgSend$_postCommit:count:
+ _objc_msgSend$_triggerCommit:count:atIndex:
+ _objc_msgSend$accelerationStructureCommandEncodingPreamble
+ _objc_msgSend$accelerationStructureDescriptorProcessEventValue
+ _objc_msgSend$addFeedbackHandler:
+ _objc_msgSend$alphaToCoverageState
+ _objc_msgSend$alphaToOneState
+ _objc_msgSend$aspectRatio
+ _objc_msgSend$barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:
+ _objc_msgSend$barrierAfterQueueStages:beforeStages:
+ _objc_msgSend$barrierAfterQueueStages:beforeStages:visibilityOptions:
+ _objc_msgSend$barrierAfterStages:beforeQueueStages:visibilityOptions:
+ _objc_msgSend$baseResourceID
+ _objc_msgSend$beginCommandBufferWithAllocator:
+ _objc_msgSend$beginCommandBufferWithAllocator:options:
+ _objc_msgSend$binaryLinkedFunctions
+ _objc_msgSend$blendingState
+ _objc_msgSend$buildAccelerationStructure:descriptor:scratchBuffer:
+ _objc_msgSend$captureCommandQueue
+ _objc_msgSend$captureDevice
+ _objc_msgSend$colorAttachmentMappingState
+ _objc_msgSend$colorTextureBarrierStages
+ _objc_msgSend$commit:count:options:
+ _objc_msgSend$computeFunctionDescriptor
+ _objc_msgSend$copyBufferMappingsFromBuffer:toBuffer:operations:count:
+ _objc_msgSend$copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$copyResourceViewsFromPool:sourceRange:destinationIndex:
+ _objc_msgSend$copyTextureMappingsFromTexture:toTexture:operations:count:
+ _objc_msgSend$curveEndCaps
+ _objc_msgSend$debugInstrumentationData
+ _objc_msgSend$debugTexture
+ _objc_msgSend$deltaTime
+ _objc_msgSend$denoiseStrengthMaskTexture
+ _objc_msgSend$denoiseStrengthMaskTextureFormat
+ _objc_msgSend$denoiseStrengthMaskTextureUsage
+ _objc_msgSend$denoiserScaler
+ _objc_msgSend$denoiserScaler4
+ _objc_msgSend$descriptorDownloader
+ _objc_msgSend$deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:
+ _objc_msgSend$deserializePrimitiveAccelerationStructure:fromBuffer:
+ _objc_msgSend$diffuseAlbedoTextureFormat
+ _objc_msgSend$diffuseAlbedoTextureUsage
+ _objc_msgSend$dilatedMotionVectors
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
+ _objc_msgSend$drawableID
+ _objc_msgSend$enableAccelerationStructureViewerInstrumentation
+ _objc_msgSend$enablePerformanceStatistics
+ _objc_msgSend$enablePostMeshDump
+ _objc_msgSend$enablePostVertexDump
+ _objc_msgSend$enableResourcePatchingInstrumentation
+ _objc_msgSend$enableResourceUsageInstrumentation
+ _objc_msgSend$endCommandBuffer
+ _objc_msgSend$endEncodingAndRetrieveProgramAddressTable
+ _objc_msgSend$executeCommandsInBuffer:indirectBuffer:
+ _objc_msgSend$extents
+ _objc_msgSend$farPlane
+ _objc_msgSend$fieldOfView
+ _objc_msgSend$filterCounterRangeWithFirstBatch:lastBatch:filterIndex:
+ _objc_msgSend$forceBaseResourceID
+ _objc_msgSend$fragmentFunctionDescriptor
+ _objc_msgSend$fragmentLinkingDescriptor
+ _objc_msgSend$functionDescriptor
+ _objc_msgSend$functionDescriptors
+ _objc_msgSend$functionGraph
+ _objc_msgSend$functionHandleWithBinaryFunction:
+ _objc_msgSend$functionHandleWithBinaryFunction:stage:
+ _objc_msgSend$functionHandleWithFunction:resourceIndex:
+ _objc_msgSend$functionHandleWithName:
+ _objc_msgSend$functionHandleWithName:stage:
+ _objc_msgSend$functionReflectionWithFunctionDescriptor:
+ _objc_msgSend$functionReflectionWithFunctionDescriptor:stage:
+ _objc_msgSend$getBytes:strides:fromSliceOrigin:sliceDimensions:
+ _objc_msgSend$getPhysicalIndexForLogicalIndex:
+ _objc_msgSend$getTensorAlias:
+ _objc_msgSend$hostName
+ _objc_msgSend$initWithBaseObject:captureCompiler:
+ _objc_msgSend$initWithBaseObject:captureDevice:captureCompiler:
+ _objc_msgSend$initWithBaseObject:captureDevice:captureFunction:
+ _objc_msgSend$initWithBaseObject:captureDevice:funcRef:
+ _objc_msgSend$initWithBaseObject:captureTensor:
+ _objc_msgSend$initWithBaseObject:descriptor:captureCompiler:
+ _objc_msgSend$initWithRank:extents:
+ _objc_msgSend$initializeBindings
+ _objc_msgSend$insertSplit
+ _objc_msgSend$intermediatesHeapSize
+ _objc_msgSend$isDenoiseStrengthMaskTextureEnabled
+ _objc_msgSend$isSpecularHitDistanceTextureEnabled
+ _objc_msgSend$isTensorViewableWithReshapedDescriptor:
+ _objc_msgSend$isTransparencyOverlayTextureEnabled
+ _objc_msgSend$isUITextureComposited
+ _objc_msgSend$lastCommittedCommandBuffer
+ _objc_msgSend$lastCommittedCommandBufferGeneration
+ _objc_msgSend$levelRange
+ _objc_msgSend$library
+ _objc_msgSend$llvmVersion
+ _objc_msgSend$lookupArchives
+ _objc_msgSend$machineLearningCommandEncoder
+ _objc_msgSend$machineLearningFunctionDescriptor
+ _objc_msgSend$maxBufferBindCount
+ _objc_msgSend$maxCompatiblePlacementSparsePageSize
+ _objc_msgSend$maxNumRegisters
+ _objc_msgSend$maxSamplerStateBindCount
+ _objc_msgSend$maxTextureBindCount
+ _objc_msgSend$maxToolsDispatchBindings
+ _objc_msgSend$meshFunctionDescriptor
+ _objc_msgSend$meshLinkingDescriptor
+ _objc_msgSend$nearPlane
+ _objc_msgSend$newArchiveWithURL:error:
+ _objc_msgSend$newArgumentTableWithDescriptor:error:
+ _objc_msgSend$newBinaryFunctionWithDescriptor:error:
+ _objc_msgSend$newBufferWithLength:options:placementSparsePageSize:
+ _objc_msgSend$newCommandAllocator
+ _objc_msgSend$newCommandAllocatorWithDescriptor:error:
+ _objc_msgSend$newCompilerWithDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithBinaryFunctions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newIndexedConstantArray
+ _objc_msgSend$newLibraryWithMPSGraphPackageURL:name:error:
+ _objc_msgSend$newMTL4CommandQueue
+ _objc_msgSend$newMTL4CommandQueueWithDescriptor:error:
+ _objc_msgSend$newMachineLearningPipelineStateWithDescriptor:error:
+ _objc_msgSend$newPipelineDataSetSerializerWithDescriptor:
+ _objc_msgSend$newRenderPipelineDescriptorForSpecialization
+ _objc_msgSend$newRenderPipelineStateWithBinaryFunctions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:
+ _objc_msgSend$newTensorViewWithReshapedDescriptor:error:
+ _objc_msgSend$newTensorViewWithSlice:error:
+ _objc_msgSend$newTensorWithDescriptor:error:
+ _objc_msgSend$newTensorWithDescriptor:offset:error:
+ _objc_msgSend$newTextureViewPoolWithDescriptor:error:
+ _objc_msgSend$newTextureViewWithDescriptor:
+ _objc_msgSend$normalTextureFormat
+ _objc_msgSend$normalTextureUsage
+ _objc_msgSend$objectFunctionDescriptor
+ _objc_msgSend$objectLinkingDescriptor
+ _objc_msgSend$outputTextureBarrierStages
+ _objc_msgSend$parentStream
+ _objc_msgSend$parentTensor
+ _objc_msgSend$pipelineDataSetSerializer
+ _objc_msgSend$pipelineOptions
+ _objc_msgSend$postVertexDumpBufferIndex
+ _objc_msgSend$presentDownloadSize
+ _objc_msgSend$rank
+ _objc_msgSend$refitAccelerationStructure:descriptor:destination:scratchBuffer:
+ _objc_msgSend$refitAccelerationStructure:descriptor:destination:scratchBuffer:options:
+ _objc_msgSend$reflectionForFunctionDescriptor:
+ _objc_msgSend$reflectionForFunctionWithName:
+ _objc_msgSend$renderCommandEncoderWithDescriptor:options:
+ _objc_msgSend$replaceSliceOrigin:sliceDimensions:withBytes:strides:
+ _objc_msgSend$requiredThreadsPerMeshThreadgroup
+ _objc_msgSend$requiredThreadsPerObjectThreadgroup
+ _objc_msgSend$requiredThreadsPerThreadgroup
+ _objc_msgSend$requiredThreadsPerTileThreadgroup
+ _objc_msgSend$resourceViewCount
+ _objc_msgSend$roughnessTextureFormat
+ _objc_msgSend$roughnessTextureUsage
+ _objc_msgSend$sampledComputeCommandEncoder:capacity:
+ _objc_msgSend$scaler
+ _objc_msgSend$scaler4
+ _objc_msgSend$serializeAsArchiveAndFlushToURL:error:
+ _objc_msgSend$serializeAsPipelinesScriptWithError:
+ _objc_msgSend$serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:
+ _objc_msgSend$serializePrimitiveAccelerationStructure:toBuffer:
+ _objc_msgSend$setAddress:atIndex:
+ _objc_msgSend$setAlphaToCoverageState:
+ _objc_msgSend$setAlphaToOneState:
+ _objc_msgSend$setArgumentTable:
+ _objc_msgSend$setArgumentTable:atStages:
+ _objc_msgSend$setAspectRatio:
+ _objc_msgSend$setBaseResourceID:
+ _objc_msgSend$setBinaryLinkedFunctions:
+ _objc_msgSend$setBlendingState:
+ _objc_msgSend$setColorAttachmentMap:
+ _objc_msgSend$setColorAttachmentMappingState:
+ _objc_msgSend$setColorTextureBarrierStages:
+ _objc_msgSend$setComputeFunctionDescriptor:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setCurrentViewToClipMatrix:
+ _objc_msgSend$setCurrentWorldToViewMatrix:
+ _objc_msgSend$setCurveEndCaps:
+ _objc_msgSend$setDeltaTime:
+ _objc_msgSend$setDenoiseStrengthMaskTexture:
+ _objc_msgSend$setDenoiseStrengthMaskTextureEnabled:
+ _objc_msgSend$setDenoiseStrengthMaskTextureFormat:
+ _objc_msgSend$setDenoiserScaler4:
+ _objc_msgSend$setDenoiserScaler:
+ _objc_msgSend$setDiffuseAlbedoTexture:
+ _objc_msgSend$setDiffuseAlbedoTextureFormat:
+ _objc_msgSend$setDimensions:
+ _objc_msgSend$setEnableAccelerationStructureViewerInstrumentation:
+ _objc_msgSend$setEnablePerformanceStatistics:
+ _objc_msgSend$setEnablePostMeshDump:
+ _objc_msgSend$setEnablePostVertexDump:
+ _objc_msgSend$setEnableResourcePatchingInstrumentation:
+ _objc_msgSend$setEnableResourceUsageInstrumentation:
+ _objc_msgSend$setFarPlane:
+ _objc_msgSend$setFieldOfView:
+ _objc_msgSend$setForceBaseResourceID:
+ _objc_msgSend$setFragmentFunctionDescriptor:
+ _objc_msgSend$setFunctionDescriptor:
+ _objc_msgSend$setFunctionDescriptors:
+ _objc_msgSend$setFunctionGraph:
+ _objc_msgSend$setInitializeBindings:
+ _objc_msgSend$setIsUITextureComposited:
+ _objc_msgSend$setLevelRange:
+ _objc_msgSend$setLibrary:
+ _objc_msgSend$setLookupArchives:
+ _objc_msgSend$setMachineLearningFunctionDescriptor:
+ _objc_msgSend$setMaxBufferBindCount:
+ _objc_msgSend$setMaxCompatiblePlacementSparsePageSize:
+ _objc_msgSend$setMaxNumRegisters:
+ _objc_msgSend$setMaxSamplerStateBindCount:
+ _objc_msgSend$setMaxTextureBindCount:
+ _objc_msgSend$setMaxToolsDispatchBindings:
+ _objc_msgSend$setMaxTotalThreadgroupsPerMeshGrid:
+ _objc_msgSend$setMeshFunctionDescriptor:
+ _objc_msgSend$setNearPlane:
+ _objc_msgSend$setNormalTexture:
+ _objc_msgSend$setNormalTextureFormat:
+ _objc_msgSend$setObjectFunctionDescriptor:
+ _objc_msgSend$setOwnerWithIdentity:
+ _objc_msgSend$setPhysicalIndex:forLogicalIndex:
+ _objc_msgSend$setPipelineDataSetSerializer:
+ _objc_msgSend$setPipelineState:
+ _objc_msgSend$setPostVertexDumpBufferIndex:
+ _objc_msgSend$setPresentDownloadSize:
+ _objc_msgSend$setPrevColorTexture:
+ _objc_msgSend$setPreviousJitterOffset:
+ _objc_msgSend$setPreviousViewToClipMatrix:
+ _objc_msgSend$setPreviousWorldToViewMatrix:
+ _objc_msgSend$setRequiredThreadsPerMeshThreadgroup:
+ _objc_msgSend$setRequiredThreadsPerObjectThreadgroup:
+ _objc_msgSend$setRequiredThreadsPerThreadgroup:
+ _objc_msgSend$setResource:atBufferIndex:
+ _objc_msgSend$setResourceViewCount:
+ _objc_msgSend$setRoughnessTexture:
+ _objc_msgSend$setRoughnessTextureFormat:
+ _objc_msgSend$setScaler4:
+ _objc_msgSend$setScaler:
+ _objc_msgSend$setShaderReflection:
+ _objc_msgSend$setShaderValidation:
+ _objc_msgSend$setShouldResetHistory:
+ _objc_msgSend$setSliceRange:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setSpecularAlbedoTexture:
+ _objc_msgSend$setSpecularAlbedoTextureFormat:
+ _objc_msgSend$setSpecularHitDistanceTexture:
+ _objc_msgSend$setSpecularHitDistanceTextureEnabled:
+ _objc_msgSend$setSpecularHitDistanceTextureFormat:
+ _objc_msgSend$setStrides:
+ _objc_msgSend$setSupportAttributeStrides:
+ _objc_msgSend$setSupportBinaryLinking:
+ _objc_msgSend$setSupportColorAttachmentMapping:
+ _objc_msgSend$setSupportFragmentBinaryLinking:
+ _objc_msgSend$setSupportMeshBinaryLinking:
+ _objc_msgSend$setSupportObjectBinaryLinking:
+ _objc_msgSend$setSupportVertexBinaryLinking:
+ _objc_msgSend$setTextureView:atIndex:
+ _objc_msgSend$setTextureView:descriptor:atIndex:
+ _objc_msgSend$setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:
+ _objc_msgSend$setTileFunctionDescriptor:
+ _objc_msgSend$setTransparencyOverlayTexture:
+ _objc_msgSend$setTransparencyOverlayTextureEnabled:
+ _objc_msgSend$setTransparencyOverlayTextureFormat:
+ _objc_msgSend$setUITexture:
+ _objc_msgSend$setUITextureFormat:
+ _objc_msgSend$setVertexDescriptor:
+ _objc_msgSend$setVertexFunctionDescriptor:
+ _objc_msgSend$setViewToClipMatrix:
+ _objc_msgSend$setVisibilityResultType:
+ _objc_msgSend$setWorldToViewMatrix:
+ _objc_msgSend$shaderReflection
+ _objc_msgSend$shouldResetHistory
+ _objc_msgSend$signalDrawable:
+ _objc_msgSend$sliceRange
+ _objc_msgSend$source
+ _objc_msgSend$sparseBufferTier
+ _objc_msgSend$sparseTextureTier
+ _objc_msgSend$specularAlbedoTextureFormat
+ _objc_msgSend$specularAlbedoTextureUsage
+ _objc_msgSend$specularHitDistanceTextureFormat
+ _objc_msgSend$specularHitDistanceTextureUsage
+ _objc_msgSend$strides
+ _objc_msgSend$supportAttributeStrides
+ _objc_msgSend$supportBinaryLinking
+ _objc_msgSend$supportColorAttachmentMapping
+ _objc_msgSend$supportFragmentBinaryLinking
+ _objc_msgSend$supportMeshBinaryLinking
+ _objc_msgSend$supportObjectBinaryLinking
+ _objc_msgSend$supportVertexBinaryLinking
+ _objc_msgSend$tensorDataType
+ _objc_msgSend$tensorSizeAndAlignWithDescriptor:
+ _objc_msgSend$tileFunctionDescriptor
+ _objc_msgSend$tileLinkingDescriptor
+ _objc_msgSend$transparencyOverlayTextureFormat
+ _objc_msgSend$transparencyOverlayTextureUsage
+ _objc_msgSend$uiTextureFormat
+ _objc_msgSend$updateBufferMappings:heap:operations:count:
+ _objc_msgSend$updateDrawableStream:
+ _objc_msgSend$updateFence:afterEncoderStages:
+ _objc_msgSend$updateTextureMappings:heap:operations:count:
+ _objc_msgSend$validationReflection
+ _objc_msgSend$vertexFunctionDescriptor
+ _objc_msgSend$vertexLinkingDescriptor
+ _objc_msgSend$viewToClipMatrix
+ _objc_msgSend$visibilityResultType
+ _objc_msgSend$waitForDrawable:
+ _objc_msgSend$waitForEvent:value:timeout:
+ _objc_msgSend$waitForFence:beforeEncoderStages:
+ _objc_msgSend$worldToViewMatrix
+ _objc_msgSend$writeAccelerationStructureSerializationData:toBuffer:
+ _objc_msgSend$writeAccelerationStructureTraversalDepth:toBuffer:
+ _objc_msgSend$writeCompactedAccelerationStructureSize:toBuffer:
+ _objc_msgSend$writeDeserializedAccelerationStructureSize:toBuffer:
+ _objc_msgSend$writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:
+ _objc_msgSend$writeSerializedAccelerationStructureSize:toBuffer:
+ _objc_release_x2
+ _osbuild
+ _proc_name
+ _readlink
+ _s_tagInfo
+ _strncpy
+ _sysctl
+ _unwrapFrameInterpolatorDescriptor
+ _unwrapInPlaceMTL4PipelineStageDynamicLinkingDescriptor
+ _unwrapMTL4AccelerationStructureDescriptor
+ _unwrapMTL4CompilerDescriptor
+ _unwrapMTL4CompilerTaskOptions
+ _unwrapMTL4ComputePipelineDescriptor
+ _unwrapMTL4FunctionDescriptor
+ _unwrapMTL4LibraryDescriptor
+ _unwrapMTL4MachineLearningPipelineDescriptor
+ _unwrapMTL4PipelineDescriptor
+ _unwrapMTL4PipelineStageDynamicLinkingDescriptor
+ _unwrapMTL4RenderPassDescriptor_
+ _unwrapMTL4RenderPipelineBinaryFunctionsDescriptor
+ _unwrapMTL4RenderPipelineDynamicLinkingDescriptor
+ _vdprintf
+ _vsnprintf
+ initWithBaseObject:captureDevice:.listener
+ initWithBaseObject:captureDevice:.submissionListener
+ initWithBaseObject:captureDevice:.token
+ insertDebugCaptureBoundary.onceToken
+ name_array.16014
+ newHeapWithDescriptor:.onceToken.179
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7783
+ s_downloaderPipelines.0.7790
+ s_downloaderPipelines.1.7791
+ s_downloaderPipelines.2.7792
+ s_downloaderPipelines.3.7793
+ s_downloaderPipelines.4.7794
+ waitUntilSignaledValue:timeoutMS:.onceToken.13259
- -[GTResourceDownloader _downloadRequestNew:atPoint:dispatchGroup:]
- DEVICEOBJECT.10014
- DEVICEOBJECT.10136
- DEVICEOBJECT.10321
- DEVICEOBJECT.10691
- DEVICEOBJECT.10876
- DEVICEOBJECT.1094
- DEVICEOBJECT.11223
- DEVICEOBJECT.128
- DEVICEOBJECT.1348
- DEVICEOBJECT.14554
- DEVICEOBJECT.1487
- DEVICEOBJECT.1648
- DEVICEOBJECT.1755
- DEVICEOBJECT.1894
- DEVICEOBJECT.2016
- DEVICEOBJECT.2205
- DEVICEOBJECT.2410
- DEVICEOBJECT.2653
- DEVICEOBJECT.2757
- DEVICEOBJECT.3010
- DEVICEOBJECT.3186
- DEVICEOBJECT.3254
- DEVICEOBJECT.3493
- DEVICEOBJECT.3822
- DEVICEOBJECT.3928
- DEVICEOBJECT.4028
- DEVICEOBJECT.4167
- DEVICEOBJECT.430
- DEVICEOBJECT.4310
- DEVICEOBJECT.4479
- DEVICEOBJECT.4836
- DEVICEOBJECT.5197
- DEVICEOBJECT.5368
- DEVICEOBJECT.5430
- DEVICEOBJECT.5623
- DEVICEOBJECT.5898
- DEVICEOBJECT.614
- DEVICEOBJECT.6266
- DEVICEOBJECT.6485
- DEVICEOBJECT.6594
- DEVICEOBJECT.6698
- DEVICEOBJECT.6892
- DEVICEOBJECT.7060
- DEVICEOBJECT.7226
- DEVICEOBJECT.7440
- DEVICEOBJECT.7744
- DEVICEOBJECT.7907
- DEVICEOBJECT.8051
- DEVICEOBJECT.8195
- DEVICEOBJECT.8350
- DEVICEOBJECT.853
- DEVICEOBJECT.8604
- DEVICEOBJECT.8850
- DEVICEOBJECT.8971
- DEVICEOBJECT.9093
- DEVICEOBJECT.9616
- DEVICEOBJECT.9746
- DEVICEOBJECT.9896
- GCC_except_table1063
- GCC_except_table11
- GCC_except_table1187
- GCC_except_table1188
- GCC_except_table1192
- GCC_except_table1193
- GCC_except_table1194
- GCC_except_table1195
- GCC_except_table1196
- GCC_except_table1382
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table16
- GCC_except_table200
- GCC_except_table223
- GCC_except_table224
- GCC_except_table2324
- GCC_except_table24
- GCC_except_table2484
- GCC_except_table2624
- GCC_except_table2630
- GCC_except_table279
- GCC_except_table304
- GCC_except_table3315
- GCC_except_table3500
- GCC_except_table88
- GTMTLDecodeIndirectRenderCommandBuffer.onceToken.44
- GTMessageKindAsString.str
- GTMessageKindAsString.str$tlv$init
- GetEnvDefault.4948
- GetStream.11294
- OBJC_IVAR_$_GTMTLCaptureService._log
- OBJC_IVAR_$_GTMTLTelemetryService._log
- StoreMTLCompileOptionsUsingEncode.14097
- _ActiveCommandQueues
- _ActiveDevices
- _CaptureExit
- _CaptureMTLCommandQueue_enqueuedCommandBufferRefs
- _CommandBufferCommitIndex
- _CommandBufferQueue
- _CompareRequestsByDescendingSize
- _CompareStream
- _CompareUInt64
- _CopyResourcesToBuffer
- _CreateBuffer
- _DecodeDYMTLCaptureDescriptor
- _DownloadNewArchiveRequests
- _EncodeDYMTLCaptureDescriptor
- _GTCaptureArchive_fillBufferSeperateFile
- _GTCaptureArchive_mapDataSeperateFile
- _GTMTLCaptureState_dumpDeviceFilesLocal
- _GTMTLCaptureState_notifyAllCaptureDataSent
- _GTMTLCaptureState_notifyUsedDataSentWithDictionary
- _GTMTLGPUAddressResource_translateToBufferOffset
- _GTMTLGuestAppClient_collectFrameProfilingData
- _GTMTLGuestAppClient_initTransportWithHostURL
- _GTMTLGuestAppClient_isUsingNewTransport
- _GTMTLGuestAppClient_processMessage
- _GTMTLGuestAppClient_sendInferiorLaunchedMessage
- _GTMTLGuestAppClient_supportsRemoteCapture
- _GTMTLIndirectResources_visibleFunctionTableIdForGPUAddress
- _GTMessageKindAsString
- _GTResourceTypeAsString
- _GTTraceDump_startContext
- _GTTraceDump_writeNewArchive
- _GatherCommandQueueResidencySetsUpToIndexIgnoringRemoves
- _GatherCommandQueueResidencySetsUpToIndexInternal
- _GatherResidencySetAllocationsUpToIndexIgnoringRemoves
- _GatherResidencySetAllocationsUpToIndexInternal
- _GetFuncEnumConstructorType
- _GetFuncEnumReceiverType
- _IORegistryEntryCreateCFProperty
- _IsCommandEncoder
- _IsFuncEnumAccelerationEncodeCall
- _IsFuncEnumBlitCall
- _IsFuncEnumCommandBufferCommit
- _IsFuncEnumCommandBufferRelated
- _IsFuncEnumComputeCall
- _IsFuncEnumConstructor
- _IsFuncEnumCreateCommandBuffer
- _IsFuncEnumCreateCommandEncoder
- _IsFuncEnumCreateIOCommandBuffer
- _IsFuncEnumCreateResource
- _IsFuncEnumDestructor
- _IsFuncEnumDisplayableCall
- _IsFuncEnumDrawCall
- _IsFuncEnumEncodeSignalEvent
- _IsFuncEnumEncodeWaitForEvent
- _IsFuncEnumEndEncoding
- _IsFuncEnumFrameBoundary
- _IsFuncEnumGPUCommandCall
- _IsFuncEnumIOCall
- _IsFuncEnumIOCommandBufferCommit
- _IsFuncEnumIndirectExecuteCall
- _IsFuncEnumIndirectExecuteComputeCall
- _IsFuncEnumIndirectExecuteRenderCall
- _IsFuncEnumMPSDispatchCall
- _IsFuncEnumMPSEncodeCall
- _IsFuncEnumMeshCall
- _IsFuncEnumMetalFXEncode
- _IsFuncEnumParallelCommandEncoderCall
- _IsFuncEnumPatchCall
- _IsFuncEnumPopDebugGroup
- _IsFuncEnumPresent
- _IsFuncEnumPushDebugGroup
- _IsFuncEnumResourceCall
- _IsFuncEnumSampleCall
- _IsFuncEnumSampledBlitCall
- _IsFuncEnumSampledBlitCallAGX
- _IsFuncEnumSetLabel
- _IsFuncEnumSharedResourceConstructor
- _IsFuncEnumTileCall
- _IsFuncEnumUseResidencySetCall
- _IsFuncEnumUseResourceCall
- _IsFuncEnumVRSubmitCall
- _IsFuncEnumVideoCall
- _IsFuncIOCommandBufferRelated
- _MakeMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
- _MakeMTLAttributeDescriptor
- _MakeMTLBlitPassSampleBufferAttachmentDescriptor
- _MakeMTLBufferLayoutDescriptor
- _MakeMTLCompileOptionsAuto
- _MakeMTLComputePassSampleBufferAttachmentDescriptor
- _MakeMTLLinkedFunctions
- _MakeMTLLinkedFunctionsAuto
- _MakeMTLPipelineBufferDescriptor
- _MakeMTLRenderPassAttachmentDescriptor
- _MakeMTLRenderPassColorAttachmentDescriptor
- _MakeMTLRenderPassDepthAttachmentDescriptor
- _MakeMTLRenderPassSampleBufferAttachmentDescriptor
- _MakeMTLRenderPassStencilAttachmentDescriptor
- _MakeMTLRenderPipelineColorAttachmentDescriptor
- _MakeMTLResourceStatePassSampleBufferAttachmentDescriptor
- _MakeMTLStageInputOutputDescriptor
- _MakeMTLStencilDescriptor
- _MakeMTLTileRenderPipelineColorAttachmentDescriptor
- _MakeMTLVertexAttributeDescriptor
- _MakeMTLVertexBufferLayoutDescriptor
- _MakeMTLVertexDescriptor
- _NSRoundUpToMultipleOfPageSize
- _OrderDispatchCommandBuffers
- _ProcessIOSurfaceTextureRequest
- _ResourceTracker_addCommandQueues
- _ResourceTracker_addDrawables
- _ResourceTracker_addIndirectCommands
- _SnapshotResidencySets
- _StoreMTLCaptureDescriptorUsingEncode
- _TranslateGTMTLAccelerationStructurePassSampleBufferAttachmentDescriptor
- _TranslateGTMTLAttributeDescriptor
- _TranslateGTMTLBlitPassSampleBufferAttachmentDescriptor
- _TranslateGTMTLBufferLayoutDescriptor
- _TranslateGTMTLComputePassSampleBufferAttachmentDescriptor
- _TranslateGTMTLLinkedFunctions
- _TranslateGTMTLLinkedFunctionsAuto
- _TranslateGTMTLPipelineBufferDescriptor
- _TranslateGTMTLRenderPassAttachmentDescriptor
- _TranslateGTMTLRenderPassColorAttachmentDescriptor
- _TranslateGTMTLRenderPassDepthAttachmentDescriptor
- _TranslateGTMTLRenderPassSampleBufferAttachmentDescriptor
- _TranslateGTMTLRenderPassStencilAttachmentDescriptor
- _TranslateGTMTLRenderPipelineColorAttachmentDescriptor
- _TranslateGTMTLResourceStatePassSampleBufferAttachmentDescriptor
- _TranslateGTMTLStageInputOutputDescriptor
- _TranslateGTMTLStencilDescriptor
- _TranslateGTMTLTileRenderPipelineColorAttachmentDescriptor
- _TranslateGTMTLVertexAttributeDescriptor
- _TranslateGTMTLVertexBufferLayoutDescriptor
- _TranslateGTMTLVertexDescriptor
- _WriteGTMTLSMCommandQueue_residencySets
- _WriteGTMTLSMCommandQueue_residencySetsDelta
- __Block_byref_object_copy_.2466
- __Block_byref_object_copy_.8853
- __Block_byref_object_dispose_.2467
- __Block_byref_object_dispose_.8854
- __GTMTLDecodeIndirectRenderCommandBuffer_block_invoke.45
- __OBJC_$_PROP_LIST_MTLFXSpatialScaler
- __OBJC_$_PROP_LIST_MTLFXTemporalScaler
- __ZL12DEVICEOBJECTP8NSObject
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __Znwm
- ___61-[CaptureMTLCaptureManager startCaptureWithDescriptor:error:]_block_invoke_2
- ___66-[GTResourceDownloader _downloadRequestNew:atPoint:dispatchGroup:]_block_invoke
- ___CreateBuffer_block_invoke
- ___GLOBAL_init_65535
- ____ZL24InitTransportWithHostURLP19GTMTLGuestAppClientPKc_block_invoke
- ____ZL24InitTransportWithHostURLP19GTMTLGuestAppClientPKc_block_invoke_2
- ___block_descriptor_40_e36_v16?0"GTTransportMessage_capture"8l
- ___block_descriptor_40_e8_32s_e9_v16?0r*8ls32l8
- ___block_descriptor_64_e8_32s40s48s56r_e31_v24?0"<MTLLateEvalEvent>"8Q16lr56l8s32l8s40l8s48l8
- ___copy_constructor_8_8_s0_s8_s16_s24
- ___cxa_atexit
- ___destructor_8_s0_s8_s16_s24
- ___gt_default_log_block_invoke
- ___udivti3
- __block_descriptor_tmp.14393
- __block_literal_global.10934
- __block_literal_global.115
- __block_literal_global.125
- __block_literal_global.140
- __block_literal_global.14739
- __block_literal_global.14879
- __block_literal_global.160
- __block_literal_global.197
- __block_literal_global.216
- __block_literal_global.258
- __block_literal_global.261
- __block_literal_global.2774
- __block_literal_global.340
- __block_literal_global.347
- __block_literal_global.3669
- __block_literal_global.425
- __block_literal_global.47
- __block_literal_global.5128
- __block_literal_global.56
- __block_literal_global.5631
- __block_literal_global.6039
- __block_literal_global.64
- __block_literal_global.6894
- __block_literal_global.7760
- __block_literal_global.8265
- __block_literal_global.9298
- __buildLibraryLinkTimeVersionsDictionary
- __buildQueueThreadLabelsDictionary
- __sendTimebaseUpdate
- __setTraceMode
- _copyAndNullifyReferencesInDescriptor
- _copyAndPatchExtraBuffersInDescriptor
- _deflate
- _deflateEnd
- _deflateInit_
- _deflateReset
- _dy_hash_string
- _fbstream_flush
- _fbstream_send
- _g_DYTimebaseInfo
- _getpagesize
- _gt_default_log
- _objc_msgSend$_downloadRequestNew:atPoint:dispatchGroup:
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$category
- _objc_msgSend$customMessage
- _objc_msgSend$doubleForKey:
- _objc_msgSend$enqueuedCommandBuffers
- _objc_msgSend$executablePath
- _objc_msgSend$fenum
- _objc_msgSend$insertDebugCaptureBoundary
- _objc_msgSend$maxMeshBufferBindCount
- _objc_msgSend$maxObjectBufferBindCount
- _objc_msgSend$maxObjectThreadgroupMemoryBindCount
- _objc_msgSend$messageWithKind:
- _objc_msgSend$messageWithKind:attributes:
- _objc_msgSend$messageWithKind:attributes:objectPayload:
- _objc_msgSend$messageWithKind:attributes:payload:
- _objc_msgSend$messageWithKind:attributes:plistPayload:
- _objc_msgSend$messageWithKind:objectPayload:
- _objc_msgSend$messageWithKind:plistPayload:
- _objc_msgSend$newSourceWithQueue:
- _objc_msgSend$plistPayload
- _objc_msgSend$resume
- _objc_msgSend$send:error:
- _objc_msgSend$send:inReplyTo:error:
- _objc_msgSend$setMaxMeshBufferBindCount:
- _objc_msgSend$setMaxObjectBufferBindCount:
- _objc_msgSend$setMaxObjectThreadgroupMemoryBindCount:
- _objc_msgSend$setMessageHandler:
- _objc_msgSend$setRegistrationHandler:
- _objc_msgSend$setSynchronous:
- _objc_msgSend$uint32ForKey:
- _objc_msgSend$uint64ForKey:
- _objc_msgSend$writeToFile:atomically:
- _s_defaultLog
- _s_logCount
- _s_logs
- _sandbox_extension_consume
- _sandbox_extension_release
- _strerror
- _symlink
- _unwrapSpatialScalerDescriptor
- _unwrapTemporalScalerDescriptor
- gt_default_log.onceToken
- name_array.11370
- newHeapWithDescriptor:.onceToken.158
- waitUntilSignaledValue:timeoutMS:.onceToken.10138
CStrings:
+ "\tDevice object: "
+ "\tFenum: "
+ "\tFilename: "
+ "\tFunc index: "
+ "\tReason: "
+ "\n"
+ "\n\tFenum: "
+ "\n\tFunc index: "
+ "\n\tLabel: "
+ "\n\tPage fault offset: "
+ "\n\tReason: "
+ "\n\tResource GPU Address Range: "
+ "\n\tResource type: "
+ "\n\taddress: "
+ "\n\tgpuResourceID: "
+ "\n\tis_read: "
+ "\n\tlevel: "
+ "\n\tpm_protect: "
+ "\n\trequestor: "
+ "\n\tsideband: "
+ "\v"
+ "\f"
+ " Archive data:\n\tFilename: "
+ " DYDecode:\n\tFunc index: "
+ " GetStream:\n\tDevice object: "
+ " fault"
+ " is false"
+ "!(entry->flags & DY_CAPTURE_FILE_FLAG_SEPARATE_FILE)"
+ "!GTFileSystem_fileExists(indexPath, NULL)"
+ "#include <metal_stdlib>\nusing namespace metal;kernel void AddEventToBuffer(device atomic_uint& count [[buffer(0)]], device ulong* events [[buffer(1)]], constant ulong& event [[buffer(2)]]){ events[atomic_fetch_add_explicit(&count, 1, memory_order_relaxed)] = event; }"
+ "%s.%s.enableLog"
+ "(none)"
+ ".mtlpackage"
+ "0x%llx"
+ "0x%llx - 0x%llx"
+ "0xffffc0e9"
+ "0xffffc0ea"
+ "@\"<MTL4Archive>\""
+ "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
+ "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
+ "@\"<MTL4ArgumentTableSPI>\""
+ "@\"<MTL4BinaryFunction>\"32@0:8@\"MTL4BinaryFunctionDescriptor\"16^@24"
+ "@\"<MTL4BinaryFunction>\"40@0:8@\"MTL4BinaryFunctionDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTL4BinaryFunctionSPI>\""
+ "@\"<MTL4CommandAllocator>\""
+ "@\"<MTL4CommandAllocator>\"16@0:8"
+ "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
+ "@\"<MTL4CommandBuffer>\"16@0:8"
+ "@\"<MTL4CommandBufferSPI>\""
+ "@\"<MTL4CommandEncoderSPI><MTL4ComputeCommandEncoderSPI>\""
+ "@\"<MTL4CommandQueue>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
+ "@\"<MTL4CommandQueueSPI>\""
+ "@\"<MTL4Compiler>\""
+ "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"<MTLLibrary>\"16@?<v@?@\"<MTLDynamicLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"MTL4LibraryDescriptor\"16@?<v@?@\"<MTLLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"MTL4MachineLearningPipelineDescriptor\"16@?<v@?@\"<MTL4MachineLearningPipelineState>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"32@0:8@\"NSURL\"16@?<v@?@\"<MTLDynamicLibrary>\"@\"NSError\">24"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4BinaryFunctionDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTL4BinaryFunction>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTLComputePipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"<MTLRenderPipelineState>\"24@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">32"
+ "@\"<MTL4CompilerTask>\"48@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32@?<v@?@\"<MTLComputePipelineState>\"@\"NSError\">40"
+ "@\"<MTL4CompilerTask>\"48@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">40"
+ "@\"<MTL4ComputeCommandEncoder>\"16@0:8"
+ "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
+ "@\"<MTL4FXFrameInterpolatorSPI>\""
+ "@\"<MTL4FXSpatialScalerSPI>\""
+ "@\"<MTL4FXTemporalDenoisedScalerSPI>\""
+ "@\"<MTL4FXTemporalScalerSPI>\""
+ "@\"<MTL4MachineLearningCommandEncoder>\"16@0:8"
+ "@\"<MTL4MachineLearningCommandEncoder><MTL4CommandEncoderSPI>\""
+ "@\"<MTL4MachineLearningPipelineState>\""
+ "@\"<MTL4MachineLearningPipelineState>\"32@0:8@\"MTL4MachineLearningPipelineDescriptor\"16^@24"
+ "@\"<MTL4PipelineDataSetSerializer>\""
+ "@\"<MTL4PipelineDataSetSerializer>\"16@0:8"
+ "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
+ "@\"<MTL4RenderCommandEncoder>\"24@0:8@\"MTL4RenderPassDescriptor\"16"
+ "@\"<MTL4RenderCommandEncoder>\"32@0:8@\"MTL4RenderPassDescriptor\"16Q24"
+ "@\"<MTL4RenderCommandEncoderSPI><MTL4CommandEncoderSPI>\""
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLComputePipelineState>\"32@0:8@\"MTL4ComputePipelineDescriptor\"16^@24"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLComputePipelineState>\"40@0:8@\"NSArray\"16^Q24^@32"
+ "@\"<MTLComputePipelineState>\"48@0:8@\"MTL4ComputePipelineDescriptor\"16@\"MTL4PipelineStageDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32^@40"
+ "@\"<MTLFXFrameInterpolatorSPI>\""
+ "@\"<MTLFXTemporalDenoisedScalerSPI>\""
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"NSString\"16"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"<MTL4BinaryFunction>\"16Q24"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"NSString\"16Q24"
+ "@\"<MTLLibrary>\"32@0:8@\"MTL4LibraryDescriptor\"16^@24"
+ "@\"<MTLLibrary>\"40@0:8@\"NSURL\"16@\"NSString\"24^@32"
+ "@\"<MTLRenderPipelineState>\"32@0:8@\"MTL4PipelineDescriptor\"16^@24"
+ "@\"<MTLRenderPipelineState>\"32@0:8@\"MTL4RenderPipelineBinaryFunctionsDescriptor\"16^@24"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"<MTLRenderPipelineState>\"24^@32"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4CompilerTaskOptions\"24^@32"
+ "@\"<MTLRenderPipelineState>\"40@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24^@32"
+ "@\"<MTLRenderPipelineState>\"48@0:8@\"MTL4PipelineDescriptor\"16@\"MTL4RenderPipelineDynamicLinkingDescriptor\"24@\"MTL4CompilerTaskOptions\"32^@40"
+ "@\"<MTLResourceSPI><MTLTensorSPI>\""
+ "@\"<MTLTensor>\""
+ "@\"<MTLTensor>\"24@0:8{MTLResourceID=Q}16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTensor>\"40@0:8@\"MTLTensorDescriptor\"16Q24^@32"
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@\"<MTLTextureViewPool><MTLResourceViewPool>\""
+ "@\"CaptureMTL4CommandBuffer\""
+ "@\"CaptureMTL4Compiler\""
+ "@\"MTL4BinaryFunctionReflection\"16@0:8"
+ "@\"MTL4MachineLearningPipelineReflection\"16@0:8"
+ "@\"MTL4PipelineDescriptor\""
+ "@\"MTL4PipelineDescriptor\"16@0:8"
+ "@\"MTLComputePipelineReflection\"16@0:8"
+ "@\"MTLFunctionReflection\"24@0:8@\"MTL4FunctionDescriptor\"16"
+ "@\"MTLFunctionReflection\"24@0:8@\"NSString\"16"
+ "@\"MTLFunctionReflection\"32@0:8@\"MTL4FunctionDescriptor\"16Q24"
+ "@\"MTLRenderPipelineReflection\"16@0:8"
+ "@\"MTLTensorExtents\"16@0:8"
+ "@\"NSData\"24@0:8^@16"
+ "@24@0:8^@16"
+ "@24@0:8^{GTMTLGuestAppClient=@@@{os_unfair_lock_s=I}IQQQAq@@@@iiQdB[7c]}16"
+ "@24@0:8{MTLResourceID=Q}16"
+ "@32@0:8@16^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}24"
+ "@40@0:8@16@24@?32"
+ "@40@0:8@16^Q24^@32"
+ "@40@0:8Q16Q24q32"
+ "@40@0:8{MTLTensorSlice=@@}16^@32"
+ "@48@0:8@16@24@32@?40"
+ "AGXRestartReport"
+ "AddEventToBuffer"
+ "Archive data error: \n"
+ "B32@0:8@\"<MTLAccelerationStructure>\"16@\"MTLGenericBVHBufferSizesSPI\"24"
+ "B32@0:8@\"<MTLAccelerationStructure>\"16@\"MTLGenericBVHBuffersSPI\"24"
+ "B32@0:8^I16^I24"
+ "BIF"
+ "C@%zutult"
+ "C@17ul@17ulU<b>@17ul"
+ "CUUU<b>t"
+ "CaptureMTL4Archive"
+ "CaptureMTL4ArgumentTable"
+ "CaptureMTL4BinaryFunction"
+ "CaptureMTL4CommandAllocator"
+ "CaptureMTL4CommandBuffer"
+ "CaptureMTL4CommandQueue"
+ "CaptureMTL4Compiler"
+ "CaptureMTL4ComputeCommandEncoder"
+ "CaptureMTL4FXFrameInterpolator"
+ "CaptureMTL4FXSpatialScaler"
+ "CaptureMTL4FXTemporalDenoisedScaler"
+ "CaptureMTL4FXTemporalScaler"
+ "CaptureMTL4MachineLearningCommandEncoder"
+ "CaptureMTL4MachineLearningPipelineState"
+ "CaptureMTL4PipelineDataSetSerializer"
+ "CaptureMTL4RenderCommandEncoder"
+ "CaptureMTLFXFrameInterpolator"
+ "CaptureMTLFXTemporalDenoisedScaler"
+ "CaptureMTLTensor"
+ "CaptureMTLTextureViewPool"
+ "Command Encoder Insert Split"
+ "CommandBuffers"
+ "CrashReport"
+ "Critical"
+ "Ct@17ul@17ult@17ul@17ul"
+ "Ct@2ulul@%llut"
+ "CtUt@2ul"
+ "CtUt@2ulul"
+ "CtUululult"
+ "CttU<b>ul"
+ "Culululuwul"
+ "Culululuwulul"
+ "Culululuwulullul"
+ "Cululuwuluw"
+ "DYDecode failed: \n"
+ "DownloadTensor[name=%lu, ref=%llu]"
+ "Error #"
+ "Failed to read dictionary content at %@: %@"
+ "Found a resource at page fault address:"
+ "GTAccelerationStructureDescriptorDownloader_MTL4_postProcess"
+ "GTAccelerationStructureDescriptorDownloader_MTL4_postProcess_event"
+ "GTErrorKeyMTL4CommitFeedback"
+ "GTFileSystem_symlink(target, fullLinkPath)"
+ "GTObservableService"
+ "GetStream failed: \n"
+ "Harvest"
+ "Internal error: unrecognized capture mode."
+ "Intersection Function Buffers"
+ "MTL4Archive"
+ "MTL4ArgumentTable"
+ "MTL4ArgumentTableSPI"
+ "MTL4BinaryFunction"
+ "MTL4BinaryFunctionSPI"
+ "MTL4CommandAllocator"
+ "MTL4CommandBuffer"
+ "MTL4CommandEncoder"
+ "MTL4CommandEncoderSPI"
+ "MTL4CommandQueue"
+ "MTL4Compiler"
+ "MTL4CompilerTask"
+ "MTL4ComputeCommandEncoder"
+ "MTL4ComputeCommandEncoderSPI"
+ "MTL4ComputePipelineState"
+ "MTL4FXFrameInterpolator"
+ "MTL4FXFrameInterpolatorSPI"
+ "MTL4FXSpatialScaler"
+ "MTL4FXSpatialScalerSPI"
+ "MTL4FXTemporalDenoisedScaler"
+ "MTL4FXTemporalScaler"
+ "MTL4MachineLearningCommandEncoder"
+ "MTL4MachineLearningPipelineState"
+ "MTL4PipelineDataSetSerializer"
+ "MTL4RenderCommandEncoder"
+ "MTL4RenderCommandEncoderSPI"
+ "MTL4RenderPipelineState"
+ "MTLCAPTURE_DISABLE_CADISPLAY"
+ "MTLCAPTURE_DISABLE_SWIZZLE_PROTECTION"
+ "MTLCAPTURE_ENABLE_EVENT_BUFFER"
+ "MTLCAPTURE_ENABLE_STREAMREF_AS_OBJECT_ID"
+ "MTLCAPTURE_FORCE_WAIT_SHARED_EVENT_TIMEOUT_CPU"
+ "MTLCAPTURE_GPU_RESTART_DEBUGGING"
+ "MTLCAPTURE_PRESENT_DOWNLOAD_SIZE"
+ "MTLCAPTURE_RESOURCES_ON_HEAPS"
+ "MTLCAPTURE_WAIT_SHARED_EVENT_TIMEOUT_CPU"
+ "MTLCaptureDescriptor"
+ "MTLFXFrameInterpolator"
+ "MTLFXFrameInterpolatorBase"
+ "MTLFXFrameInterpolatorDescriptor"
+ "MTLFXFrameInterpolatorSPI"
+ "MTLFXSpatialScalerBase"
+ "MTLFXTemporalDenoisedScaler"
+ "MTLFXTemporalDenoisedScalerBase"
+ "MTLFXTemporalDenoisedScalerDescriptor"
+ "MTLFXTemporalDenoisedScalerSPI"
+ "MTLFXTemporalScalerBase"
+ "MTLHeapType"
+ "MTLResourceViewPool"
+ "MTLTensor"
+ "MTLTensor-%llu-%u"
+ "MTLTensorBinding"
+ "MTLTextureViewPool"
+ "Metal 4 Additional Binary Functions"
+ "Metal 4 Archive"
+ "Metal 4 Binary Function"
+ "Metal 4 Binary Functions"
+ "Metal 4 Command Buffer"
+ "Metal 4 Compiler"
+ "Metal 4 Compute Command Encoder"
+ "Metal 4 Device"
+ "Metal 4 Device SPI"
+ "Metal 4 Function Stitching"
+ "Metal 4 Harvesting Data Set"
+ "Metal 4 Profiling SPI"
+ "Metal 4 Render Command Encoder"
+ "Metal4 Sparse Buffers"
+ "Metal4 Sparse Textures"
+ "Profiling"
+ "Requested heap type is not available"
+ "Restores"
+ "T@\"<MTL4Archive>\",R"
+ "T@\"<MTL4ArgumentTable>\",R"
+ "T@\"<MTL4BinaryFunction>\",R"
+ "T@\"<MTL4CommandAllocator>\",R"
+ "T@\"<MTL4CommandBuffer>\",R"
+ "T@\"<MTL4CommandBuffer>\",R,N"
+ "T@\"<MTL4CommandQueue>\",R"
+ "T@\"<MTL4CommandQueue>\",R,N"
+ "T@\"<MTL4Compiler>\",R"
+ "T@\"<MTL4ComputeCommandEncoder>\",R"
+ "T@\"<MTL4FXFrameInterpolator>\",R"
+ "T@\"<MTL4FXSpatialScaler>\",R"
+ "T@\"<MTL4FXTemporalDenoisedScaler>\",R"
+ "T@\"<MTL4FXTemporalScaler>\",R"
+ "T@\"<MTL4MachineLearningCommandEncoder>\",R"
+ "T@\"<MTL4MachineLearningPipelineState>\",R"
+ "T@\"<MTL4PipelineDataSetSerializer>\",R"
+ "T@\"<MTL4RenderCommandEncoder>\",R"
+ "T@\"<MTLBuffer>\",?,N"
+ "T@\"<MTLFXFrameInterpolator>\",R"
+ "T@\"<MTLFXTemporalDenoisedScaler>\",R"
+ "T@\"<MTLTensor>\",R"
+ "T@\"<MTLTexture>\",&,N,SsetUITexture:"
+ "T@\"<MTLTexture>\",R,N"
+ "T@\"<MTLTextureViewPool>\",R"
+ "T@\"CaptureMTLDevice\",R"
+ "T@\"CaptureMTLDevice\",R,V_captureDevice"
+ "T@\"MTL4BinaryFunctionReflection\",R"
+ "T@\"MTL4MachineLearningPipelineReflection\",R"
+ "T@\"MTLComputePipelineReflection\",R"
+ "T@\"MTLRenderPipelineReflection\",R"
+ "T@\"MTLTensorExtents\",R"
+ "T@\"NSString\",R,N"
+ "TB,N,GisUITextureComposited,SsetIsUITextureComposited:"
+ "TQ,R,V_accelerationStructureDescriptorCopyEventValue"
+ "T^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]},R"
+ "T^{GTTraceStream=},R,V_parentStream"
+ "Tensor"
+ "Ti,R"
+ "T{MTLResourceID=Q},R,N"
+ "[12B]"
+ "^Q"
+ "^{GTAccelerationStructureDescriptorDownloader_MTL4=}"
+ "^{GTAccelerationStructureDescriptorDownloader_MTL4=}16@0:8"
+ "^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}"
+ "^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}16@0:8"
+ "^{TextureViewSlot={MTLResourceID=Q}b63b1(?={?=QQ{GTMTLTextureDescriptor=QQIIISSSSSCCCCCCCCCCCCC[5C]}}{?=B[7c]{GTMTLTextureViewDescriptor={GTRange=QQ}{GTRange=QQ}ISC[1C]}})}"
+ "__waitUntilCompletedAsync:"
+ "__waitUntilScheduledAsync:"
+ "_addRequestsToDownloadQueueForCommandBuffers:count:atIndex:"
+ "_addScheduledTrigger:count:atIndex:"
+ "_bufferCache"
+ "_cachedFunctionHandleLock"
+ "_cachedFunctionHandleMap"
+ "_captureCompiler"
+ "_captureDenoiseStrengthMaskTexture"
+ "_captureDiffuseAlbedoTexture"
+ "_captureNormalTexture"
+ "_capturePrevColorTexture"
+ "_captureRoughnessTexture"
+ "_captureSpecularAlbedoTexture"
+ "_captureSpecularHitDistanceTexture"
+ "_captureTransparencyOverlayTexture"
+ "_captureUITexture"
+ "_commitCommandBuffers:count:atIndex:"
+ "_descriptorDownloader"
+ "_downloadQueueLock"
+ "_downloadSignal"
+ "_drawableStream"
+ "_dummyDepthStencilStateIndex"
+ "_encodeDownloadPoint:"
+ "_inFlightCommandBuffersCompletedEvent"
+ "_inFlightCommandBuffersCompletedEventValue"
+ "_listener"
+ "_mtl4Descriptor"
+ "_parentStream"
+ "_postCommit:count:"
+ "_scheduled"
+ "_streamRefs"
+ "_submissionListener"
+ "_tensor"
+ "_textureViews"
+ "_textureViewsCopy"
+ "_triggerCommit:count:atIndex:"
+ "acceleration structure"
+ "accelerationStructureCommandEncodingPreamble"
+ "accelerationStructureDescriptorProcessEventValue"
+ "addFeedbackHandler:"
+ "alphaToCoverageState"
+ "alphaToOneState"
+ "an MTLCommandQueue or MTL4CommandQueue"
+ "analysis"
+ "and more...\n"
+ "aspectRatio"
+ "barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:"
+ "barrierAfterQueueStages:beforeStages:"
+ "barrierAfterQueueStages:beforeStages:visibilityOptions:"
+ "barrierAfterStages:beforeQueueStages:visibilityOptions:"
+ "baseResourceID"
+ "beginCommandBufferWithAllocator:"
+ "beginCommandBufferWithAllocator:options:"
+ "bif0_fault"
+ "bif1_fault"
+ "binaryLinkedFunctions"
+ "blendingState"
+ "buffer != ((void*)0)"
+ "buildAccelerationStructure:descriptor:scratchBuffer:"
+ "bytes != MAP_FAILED"
+ "captureDevice"
+ "colorAttachmentMappingState"
+ "colorTextureBarrierStages"
+ "com.apple.gputools.ASBuilder"
+ "com.apple.gputools.ASViewer"
+ "com.apple.gputools.CaptureMTL4CommandBufferSubmission"
+ "com.apple.gputools.CaptureMTL4CommandQueue"
+ "com.apple.gputools.GTAccelerationStructureDescriptorDownloader_MTL4"
+ "com.apple.gputools.GTAccelerationStructureDescriptorDownloader_MTL4_argumentTable"
+ "com.apple.gputools.GTAccelerationStructureDescriptorDownloader_MTL4_residencySet"
+ "com.apple.gputools.MTLHeapBackBuffer_0x%llx"
+ "com.apple.gputools.cli"
+ "com.apple.gputools.core"
+ "com.apple.gputools.diagnostics"
+ "com.apple.gputools.perf"
+ "com.apple.gputools.replay"
+ "commandBatchIdOffset"
+ "commandBatchIdRangeMin:max:"
+ "commit:count:"
+ "commit:count:options:"
+ "compiler"
+ "compilers"
+ "compositedUITexture"
+ "computeFunctionDescriptor"
+ "copyBufferMappingsFromBuffer:toBuffer:operations:count:"
+ "copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:"
+ "copyItemAtURL:toURL:error:"
+ "copyResourceViewsFromPool:sourceRange:destinationIndex:"
+ "copyTextureMappingsFromTexture:toTexture:operations:count:"
+ "curveEndCaps"
+ "defaultCompilerProcessesCount"
+ "deltaTime"
+ "denoiseStrengthMaskTexture"
+ "denoiseStrengthMaskTextureFormat"
+ "denoiseStrengthMaskTextureUsage"
+ "denoiserScaler"
+ "denoiserScaler4"
+ "descriptorDownloader"
+ "deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:"
+ "deserializePrimitiveAccelerationStructure:fromBuffer:"
+ "dest != NULL"
+ "diffuseAlbedoTexture"
+ "diffuseAlbedoTextureFormat"
+ "diffuseAlbedoTextureUsage"
+ "dilatedMotionVectors"
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
+ "enableAccelerationStructureViewerInstrumentation"
+ "enablePerformanceStatistics"
+ "enablePostMeshDump"
+ "enablePostVertexDump"
+ "enableResourcePatchingInstrumentation"
+ "enableResourceUsageInstrumentation"
+ "end > it"
+ "endCommandBuffer"
+ "entry->flags & DY_CAPTURE_FILE_FLAG_SEPARATE_FILE"
+ "entry->storage_offset <= self->backingStore.length"
+ "executeCommandsInBuffer:indirectBuffer:"
+ "extents"
+ "fail: %s"
+ "fail: Couldn't find a resource responsible for page fault"
+ "fail: Failed to create MTLTensor target for downloading: %@"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the library: %s"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the pipeline state: %s"
+ "fail: Invalid log tag: %u"
+ "fail: Page fault: %s"
+ "farPlane"
+ "fd > 0"
+ "fd >= 0"
+ "fieldOfView"
+ "filterCounterRangeWithFirstBatch:lastBatch:filterIndex:"
+ "forceBaseResourceID"
+ "fragmentFunctionDescriptor"
+ "fragmentLinkingDescriptor"
+ "functionDescriptor"
+ "functionDescriptors"
+ "functionGraph"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithBinaryFunction:stage:"
+ "functionHandleWithFunction:resourceIndex:"
+ "functionHandleWithName:"
+ "functionHandleWithName:stage:"
+ "functionReflectionWithFunctionDescriptor:"
+ "functionReflectionWithFunctionDescriptor:stage:"
+ "getBytes:strides:fromSliceOrigin:sliceDimensions:"
+ "getPhysicalIndexForLogicalIndex:"
+ "getTensorAlias:"
+ "gputools.ADSIndirectInstanceDescriptorBuffer"
+ "gputools.ADSMotionCurveIndexBuffer"
+ "header != MAP_FAILED"
+ "header->fourcc == DY_CAPTURE_INDEX_FOURCC || header->version == DY_CAPTURE_INDEX_VERSION_0"
+ "hostName"
+ "indexStat.st_size - BUFFER_DELTA2(header, file_table) >= sizeof(dy_capture_index_file_entry_t) * header->file_table_length"
+ "indexStat.st_size - BUFFER_DELTA2(header, hash_table) >= sizeof(dy_capture_index_hash_entry_t) * header->hash_table_length"
+ "indexStat.st_size - BUFFER_DELTA2(header, name_table) >= sizeof(dy_capture_index_name_entry_t) * header->name_table_length"
+ "indexStat.st_size >= sizeof(dy_capture_index_header_t)"
+ "initWithBaseObject:captureCompiler:"
+ "initWithBaseObject:captureDevice:captureCompiler:"
+ "initWithBaseObject:captureDevice:captureFunction:"
+ "initWithBaseObject:captureDevice:funcRef:"
+ "initWithBaseObject:captureTensor:"
+ "initWithBaseObject:descriptor:captureCompiler:"
+ "initWithRank:extents:"
+ "initializeBindings"
+ "insertSplit"
+ "intermediatesHeapSize"
+ "isDenoiseStrengthMaskTextureEnabled"
+ "isSpecularHitDistanceTextureEnabled"
+ "isTensorViewableWithReshapedDescriptor:"
+ "isTransparencyOverlayTextureEnabled"
+ "isUITextureComposited"
+ "is_read"
+ "kDYFEMTL4Archive_dealloc"
+ "kDYFEMTL4Archive_newBinaryFunctionWithDescriptor_error"
+ "kDYFEMTL4Archive_newBinaryFunctionWithDescriptor_functionType_error"
+ "kDYFEMTL4Archive_newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_error"
+ "kDYFEMTL4Archive_newComputePipelineStateWithDescriptor_error"
+ "kDYFEMTL4Archive_newComputePipelineStateWithName_dynamicLinkingDescriptor_error"
+ "kDYFEMTL4Archive_newComputePipelineStateWithName_error"
+ "kDYFEMTL4Archive_newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_error"
+ "kDYFEMTL4Archive_newRenderPipelineStateWithDescriptor_error"
+ "kDYFEMTL4Archive_newRenderPipelineStateWithName_dynamicLinkingDescriptor_error"
+ "kDYFEMTL4Archive_newRenderPipelineStateWithName_error"
+ "kDYFEMTL4Archive_setLabel"
+ "kDYFEMTL4ArgumentTable_dealloc"
+ "kDYFEMTL4ArgumentTable_setAddress_atIndex"
+ "kDYFEMTL4ArgumentTable_setAddress_attributeStride_atIndex"
+ "kDYFEMTL4ArgumentTable_setResource_atBufferIndex"
+ "kDYFEMTL4ArgumentTable_setSamplerState_atIndex"
+ "kDYFEMTL4ArgumentTable_setTexture_atIndex"
+ "kDYFEMTL4BinaryFunction_dealloc"
+ "kDYFEMTL4BinaryFunction_setRelocations"
+ "kDYFEMTL4CommandAllocator_allocatedSize"
+ "kDYFEMTL4CommandAllocator_dealloc"
+ "kDYFEMTL4CommandAllocator_reset"
+ "kDYFEMTL4CommandBuffer_beginCommandBufferWithAllocator"
+ "kDYFEMTL4CommandBuffer_beginCommandBufferWithAllocator_options"
+ "kDYFEMTL4CommandBuffer_computeCommandEncoder"
+ "kDYFEMTL4CommandBuffer_dealloc"
+ "kDYFEMTL4CommandBuffer_endCommandBuffer"
+ "kDYFEMTL4CommandBuffer_machineLearningCommandEncoder"
+ "kDYFEMTL4CommandBuffer_popDebugGroup"
+ "kDYFEMTL4CommandBuffer_pushDebugGroup"
+ "kDYFEMTL4CommandBuffer_renderCommandEncoderWithDescriptor"
+ "kDYFEMTL4CommandBuffer_renderCommandEncoderWithDescriptor_options"
+ "kDYFEMTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_atOffset_waitFence_updateFence"
+ "kDYFEMTL4CommandBuffer_sampledComputeCommandEncoder_capacity"
+ "kDYFEMTL4CommandBuffer_sampledRenderCommandEncoderWithDescriptor_programInfoBuffer_capacity"
+ "kDYFEMTL4CommandBuffer_setLabel"
+ "kDYFEMTL4CommandBuffer_status"
+ "kDYFEMTL4CommandBuffer_useResidencySet"
+ "kDYFEMTL4CommandBuffer_useResidencySets_count"
+ "kDYFEMTL4CommandBuffer_writeTimestampIntoHeap_atIndex"
+ "kDYFEMTL4CommandQueue_addResidencySet"
+ "kDYFEMTL4CommandQueue_addResidencySets_count"
+ "kDYFEMTL4CommandQueue_barrierAfterQueueStages_beforeQueueStages_scope_error"
+ "kDYFEMTL4CommandQueue_commit_count"
+ "kDYFEMTL4CommandQueue_commit_count_error"
+ "kDYFEMTL4CommandQueue_commit_count_options"
+ "kDYFEMTL4CommandQueue_commit_count_options_error"
+ "kDYFEMTL4CommandQueue_copyBufferMappingsFromBuffer_sourceOffsets_sourceLengths_numLengths_toBuffer_destinationOffsets"
+ "kDYFEMTL4CommandQueue_copyBufferMappingsFromBuffer_toBuffer_operations_count"
+ "kDYFEMTL4CommandQueue_copyTextureMappingsFromTexture_sourceSlices_sourceLevels_sourceOrigins_sourceSizes_numSizes_toTexture_destinationSlices_destinationLevels_destinationOrigins"
+ "kDYFEMTL4CommandQueue_copyTextureMappingsFromTexture_toTexture_operations_count"
+ "kDYFEMTL4CommandQueue_dealloc"
+ "kDYFEMTL4CommandQueue_presentDrawable"
+ "kDYFEMTL4CommandQueue_presentDrawable_afterMinimumDuration"
+ "kDYFEMTL4CommandQueue_presentDrawable_atTime"
+ "kDYFEMTL4CommandQueue_removeResidencySet"
+ "kDYFEMTL4CommandQueue_removeResidencySets_count"
+ "kDYFEMTL4CommandQueue_signalDrawable"
+ "kDYFEMTL4CommandQueue_signalDrawable_error"
+ "kDYFEMTL4CommandQueue_signalEvent_value"
+ "kDYFEMTL4CommandQueue_signalEvent_value_error"
+ "kDYFEMTL4CommandQueue_updateBufferMappings_heap_operations_count"
+ "kDYFEMTL4CommandQueue_updateBufferMappings_numRegions_regions_heap_rangeModes_rangeOffsets"
+ "kDYFEMTL4CommandQueue_updateTextureMappings_heap_operations_count"
+ "kDYFEMTL4CommandQueue_updateTextureMappings_numRegions_regions_levels_slices_heap_rangeModes_rangeOffsets"
+ "kDYFEMTL4CommandQueue_waitEvent_value_error"
+ "kDYFEMTL4CommandQueue_waitForDrawable"
+ "kDYFEMTL4CommandQueue_waitForDrawable_error"
+ "kDYFEMTL4CommandQueue_waitForEvent_value"
+ "kDYFEMTL4CommandQueue_waitForEvent_value_error"
+ "kDYFEMTL4CompilerTask_dealloc"
+ "kDYFEMTL4CompilerTask_waitUntilComplete"
+ "kDYFEMTL4CompilerTask_waitUntilCompleted"
+ "kDYFEMTL4Compiler_cancel"
+ "kDYFEMTL4Compiler_dealloc"
+ "kDYFEMTL4Compiler_newBinaryFunctionWithDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newBinaryFunctionWithDescriptor_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newBinaryFunctionWithDescriptor_functionType_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newBinaryFunctionWithDescriptor_functionType_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newComputePipelineStateWithDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newComputePipelineStateWithDescriptor_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newDynamicLibraryWithURL_completionHandler"
+ "kDYFEMTL4Compiler_newDynamicLibraryWithURL_error"
+ "kDYFEMTL4Compiler_newDynamicLibrary_completionHandler"
+ "kDYFEMTL4Compiler_newDynamicLibrary_error"
+ "kDYFEMTL4Compiler_newLibraryWithDescriptor_completionHandler"
+ "kDYFEMTL4Compiler_newLibraryWithDescriptor_error"
+ "kDYFEMTL4Compiler_newMachineLearningPipelineStateWithDescriptor_completionHandler"
+ "kDYFEMTL4Compiler_newMachineLearningPipelineStateWithDescriptor_error"
+ "kDYFEMTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler"
+ "kDYFEMTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error"
+ "kDYFEMTL4Compiler_newRenderPipelineStateWithDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newRenderPipelineStateWithDescriptor_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4Compiler_newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error"
+ "kDYFEMTL4Compiler_newRenderPipelineStateWithDescriptor_linkingDescriptor_compilerTaskOptions_completionHandler"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_options"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterQueueStages_beforeStages_options"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterQueueStages_beforeStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterStages_beforeQueueStages_options"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterStages_beforeQueueStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions"
+ "kDYFEMTL4ComputeCommandEncoder_barrierUpdate_afterEncoderStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierUpdate_afterQueueStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierWait_beforeEncoderStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_barrierWait_beforeQueueStages_scope"
+ "kDYFEMTL4ComputeCommandEncoder_buildAccelerationStructure_descriptor_scratchBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_commandBatchIdOffset"
+ "kDYFEMTL4ComputeCommandEncoder_commandBatchIdRangeMin_max"
+ "kDYFEMTL4ComputeCommandEncoder_copyAccelerationStructure_toAccelerationStructure"
+ "kDYFEMTL4ComputeCommandEncoder_copyAndCompactAccelerationStructure_toAccelerationStructure"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTensor_sourceOrigin_sourceDimensions_toTensor_destinationOrigin_destinationDimensions"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTensor_sourceSlice_toTensor_destinationSlice"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount"
+ "kDYFEMTL4ComputeCommandEncoder_copyFromTexture_toTexture"
+ "kDYFEMTL4ComputeCommandEncoder_copyIndirectCommandBuffer_sourceRange_destination_destinationIndex"
+ "kDYFEMTL4ComputeCommandEncoder_dealloc"
+ "kDYFEMTL4ComputeCommandEncoder_dispatchThreadgroupsWithIndirectBuffer_threadsPerThreadgroup"
+ "kDYFEMTL4ComputeCommandEncoder_dispatchThreadgroups_threadsPerThreadgroup"
+ "kDYFEMTL4ComputeCommandEncoder_dispatchThreadsWithIndirectBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_dispatchThreads_threadsPerThreadgroup"
+ "kDYFEMTL4ComputeCommandEncoder_endEncoding"
+ "kDYFEMTL4ComputeCommandEncoder_endEncodingAndRetrieveProgramAddressTable"
+ "kDYFEMTL4ComputeCommandEncoder_executeCommandsInBuffer_indirectBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_executeCommandsInBuffer_withRange"
+ "kDYFEMTL4ComputeCommandEncoder_fillBuffer_range_pattern4"
+ "kDYFEMTL4ComputeCommandEncoder_fillBuffer_range_value"
+ "kDYFEMTL4ComputeCommandEncoder_fillTexture_level_slice_region_bytes_length"
+ "kDYFEMTL4ComputeCommandEncoder_fillTexture_level_slice_region_color"
+ "kDYFEMTL4ComputeCommandEncoder_fillTexture_level_slice_region_color_pixelFormat"
+ "kDYFEMTL4ComputeCommandEncoder_filterCounterRangeWithFirstBatch_lastBatch_filterIndex"
+ "kDYFEMTL4ComputeCommandEncoder_generateMipmapsForTexture"
+ "kDYFEMTL4ComputeCommandEncoder_insertDebugSignpost"
+ "kDYFEMTL4ComputeCommandEncoder_optimizeContentsForCPUAccess"
+ "kDYFEMTL4ComputeCommandEncoder_optimizeContentsForCPUAccess_slice_level"
+ "kDYFEMTL4ComputeCommandEncoder_optimizeContentsForGPUAccess"
+ "kDYFEMTL4ComputeCommandEncoder_optimizeContentsForGPUAccess_slice_level"
+ "kDYFEMTL4ComputeCommandEncoder_optimizeIndirectCommandBuffer_withRange"
+ "kDYFEMTL4ComputeCommandEncoder_popDebugGroup"
+ "kDYFEMTL4ComputeCommandEncoder_pushDebugGroup"
+ "kDYFEMTL4ComputeCommandEncoder_refitAccelerationStructure_descriptor_destination_scratchBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_refitAccelerationStructure_descriptor_destination_scratchBuffer_options"
+ "kDYFEMTL4ComputeCommandEncoder_resetCommandsInBuffer_withRange"
+ "kDYFEMTL4ComputeCommandEncoder_setAccelerationStructureDescriptor"
+ "kDYFEMTL4ComputeCommandEncoder_setAccelerationStructureState"
+ "kDYFEMTL4ComputeCommandEncoder_setArgumentTable"
+ "kDYFEMTL4ComputeCommandEncoder_setComputePipelineState"
+ "kDYFEMTL4ComputeCommandEncoder_setImageblockWidth_height"
+ "kDYFEMTL4ComputeCommandEncoder_setLabel"
+ "kDYFEMTL4ComputeCommandEncoder_setThreadgroupMemoryLength_atIndex"
+ "kDYFEMTL4ComputeCommandEncoder_setToolsDispatchBufferSPI_atIndex"
+ "kDYFEMTL4ComputeCommandEncoder_stages"
+ "kDYFEMTL4ComputeCommandEncoder_updateFence_afterEncoderStages"
+ "kDYFEMTL4ComputeCommandEncoder_waitForFence_beforeEncoderStages"
+ "kDYFEMTL4ComputeCommandEncoder_writeAccelerationStructureTraversalDepth_toBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_writeCompactedAccelerationStructureSize_toBuffer"
+ "kDYFEMTL4ComputeCommandEncoder_writeTimestampWithGranularity_intoHeap_atIndex"
+ "kDYFEMTL4ComputePipelineState_dealloc"
+ "kDYFEMTL4ComputePipelineState_functionHandleWithBinaryFunction"
+ "kDYFEMTL4ComputePipelineState_functionHandleWithFunction"
+ "kDYFEMTL4ComputePipelineState_functionHandleWithName"
+ "kDYFEMTL4ComputePipelineState_getComputeKernelTelemetryID"
+ "kDYFEMTL4ComputePipelineState_imageblockMemoryLengthForDimensions"
+ "kDYFEMTL4ComputePipelineState_newComputePipelineStateWithAdditionalBinaryFunctions_error"
+ "kDYFEMTL4ComputePipelineState_newIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4ComputePipelineState_newVisibleFunctionTableWithDescriptor"
+ "kDYFEMTL4FXFrameInterpolator_dealloc"
+ "kDYFEMTL4FXFrameInterpolator_encodeToCommandBuffer"
+ "kDYFEMTL4FXFrameInterpolator_setAspectRatio"
+ "kDYFEMTL4FXFrameInterpolator_setColorTexture"
+ "kDYFEMTL4FXFrameInterpolator_setColorTextureBarrierStages"
+ "kDYFEMTL4FXFrameInterpolator_setDeltaTime"
+ "kDYFEMTL4FXFrameInterpolator_setDepthReversed"
+ "kDYFEMTL4FXFrameInterpolator_setDepthTexture"
+ "kDYFEMTL4FXFrameInterpolator_setFarPlane"
+ "kDYFEMTL4FXFrameInterpolator_setFence"
+ "kDYFEMTL4FXFrameInterpolator_setFieldOfView"
+ "kDYFEMTL4FXFrameInterpolator_setIsUITextureComposited"
+ "kDYFEMTL4FXFrameInterpolator_setJitterOffsetX"
+ "kDYFEMTL4FXFrameInterpolator_setJitterOffsetY"
+ "kDYFEMTL4FXFrameInterpolator_setMaskTexture"
+ "kDYFEMTL4FXFrameInterpolator_setMotionTexture"
+ "kDYFEMTL4FXFrameInterpolator_setMotionVectorScaleX"
+ "kDYFEMTL4FXFrameInterpolator_setMotionVectorScaleY"
+ "kDYFEMTL4FXFrameInterpolator_setNearPlane"
+ "kDYFEMTL4FXFrameInterpolator_setOutputTexture"
+ "kDYFEMTL4FXFrameInterpolator_setOutputTextureBarrierStages"
+ "kDYFEMTL4FXFrameInterpolator_setPrevColorTexture"
+ "kDYFEMTL4FXFrameInterpolator_setReset"
+ "kDYFEMTL4FXFrameInterpolator_setResetHistory"
+ "kDYFEMTL4FXFrameInterpolator_setShouldResetHistory"
+ "kDYFEMTL4FXFrameInterpolator_setUITexture"
+ "kDYFEMTL4FXSpatialScaler_dealloc"
+ "kDYFEMTL4FXSpatialScaler_encodeToCommandBuffer"
+ "kDYFEMTL4FXSpatialScaler_setColorTexture"
+ "kDYFEMTL4FXSpatialScaler_setColorTextureBarrierStages"
+ "kDYFEMTL4FXSpatialScaler_setFence"
+ "kDYFEMTL4FXSpatialScaler_setInputContentHeight"
+ "kDYFEMTL4FXSpatialScaler_setInputContentWidth"
+ "kDYFEMTL4FXSpatialScaler_setOutputTexture"
+ "kDYFEMTL4FXSpatialScaler_setOutputTextureBarrierStages"
+ "kDYFEMTL4FXTemporalDenoisedScaler_dealloc"
+ "kDYFEMTL4FXTemporalDenoisedScaler_encodeToCommandBuffer"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setColorTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setColorTextureBarrierStages"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setDenoiseStrengthMaskTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setDepthReversed"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setDepthTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setDiffuseAlbedoTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setExposureTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setFence"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setInputContentHeight"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setInputContentWidth"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setJitterOffsetX"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setJitterOffsetY"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setMotionTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setMotionVectorScaleX"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setMotionVectorScaleY"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setNormalTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setOutputTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setOutputTextureBarrierStages"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setPreExposure"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setPreUpscaleComposeTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setReactiveMaskTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setReset"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setResetHistory"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setRoughnessTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setShouldResetHistory"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setSpecularAlbedoTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setSpecularHitDistanceTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setTransparencyOverlayTexture"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setViewToClipMatrix"
+ "kDYFEMTL4FXTemporalDenoisedScaler_setWorldToViewMatrix"
+ "kDYFEMTL4FXTemporalScaler_dealloc"
+ "kDYFEMTL4FXTemporalScaler_encodeToCommandBuffer"
+ "kDYFEMTL4FXTemporalScaler_executionMode"
+ "kDYFEMTL4FXTemporalScaler_setColorTexture"
+ "kDYFEMTL4FXTemporalScaler_setColorTextureBarrierStages"
+ "kDYFEMTL4FXTemporalScaler_setDepthReversed"
+ "kDYFEMTL4FXTemporalScaler_setDepthTexture"
+ "kDYFEMTL4FXTemporalScaler_setExposureTexture"
+ "kDYFEMTL4FXTemporalScaler_setFence"
+ "kDYFEMTL4FXTemporalScaler_setInputContentHeight"
+ "kDYFEMTL4FXTemporalScaler_setInputContentWidth"
+ "kDYFEMTL4FXTemporalScaler_setJitterOffsetX"
+ "kDYFEMTL4FXTemporalScaler_setJitterOffsetY"
+ "kDYFEMTL4FXTemporalScaler_setMotionTexture"
+ "kDYFEMTL4FXTemporalScaler_setMotionVectorScaleX"
+ "kDYFEMTL4FXTemporalScaler_setMotionVectorScaleY"
+ "kDYFEMTL4FXTemporalScaler_setOutputTexture"
+ "kDYFEMTL4FXTemporalScaler_setOutputTextureBarrierStages"
+ "kDYFEMTL4FXTemporalScaler_setPreExposure"
+ "kDYFEMTL4FXTemporalScaler_setReactiveMaskTexture"
+ "kDYFEMTL4FXTemporalScaler_setReset"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_options"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterQueueStages_beforeStages_options"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterQueueStages_beforeStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterStages_beforeQueueStages_options"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterStages_beforeQueueStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierUpdate_afterEncoderStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierUpdate_afterQueueStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierWait_beforeEncoderStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_barrierWait_beforeQueueStages_scope"
+ "kDYFEMTL4MachineLearningCommandEncoder_commandBatchIdOffset"
+ "kDYFEMTL4MachineLearningCommandEncoder_commandBatchIdRangeMin_max"
+ "kDYFEMTL4MachineLearningCommandEncoder_dealloc"
+ "kDYFEMTL4MachineLearningCommandEncoder_dispatchNetworkWithIntermediatesHeap"
+ "kDYFEMTL4MachineLearningCommandEncoder_endEncoding"
+ "kDYFEMTL4MachineLearningCommandEncoder_endEncodingAndRetrieveProgramAddressTable"
+ "kDYFEMTL4MachineLearningCommandEncoder_filterCounterRangeWithFirstBatch_lastBatch_filterIndex"
+ "kDYFEMTL4MachineLearningCommandEncoder_insertDebugSignpost"
+ "kDYFEMTL4MachineLearningCommandEncoder_popDebugGroup"
+ "kDYFEMTL4MachineLearningCommandEncoder_pushDebugGroup"
+ "kDYFEMTL4MachineLearningCommandEncoder_setArgumentTable"
+ "kDYFEMTL4MachineLearningCommandEncoder_setLabel"
+ "kDYFEMTL4MachineLearningCommandEncoder_setPipelineState"
+ "kDYFEMTL4MachineLearningCommandEncoder_updateFence_afterEncoderStages"
+ "kDYFEMTL4MachineLearningCommandEncoder_waitForFence_beforeEncoderStages"
+ "kDYFEMTL4MachineLearningPipelineState_dealloc"
+ "kDYFEMTL4PipelineDataSetSerializer_dealloc"
+ "kDYFEMTL4PipelineDataSetSerializer_serializeAsArchiveAndFlushToURL_error"
+ "kDYFEMTL4PipelineDataSetSerializer_serializeAsPipelinesScriptWithError"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_options"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterQueueStages_beforeStages_options"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterQueueStages_beforeStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterQueueStages_beforeStages_visibilityOptions"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterStages_beforeQueueStages_options"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterStages_beforeQueueStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierAfterStages_beforeQueueStages_visibilityOptions"
+ "kDYFEMTL4RenderCommandEncoder_barrierUpdate_afterEncoderStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierUpdate_afterQueueStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierWait_beforeEncoderStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_barrierWait_beforeQueueStages_scope"
+ "kDYFEMTL4RenderCommandEncoder_commandBatchIdOffset"
+ "kDYFEMTL4RenderCommandEncoder_commandBatchIdRangeMin_max"
+ "kDYFEMTL4RenderCommandEncoder_dealloc"
+ "kDYFEMTL4RenderCommandEncoder_dispatchThreadsPerTile"
+ "kDYFEMTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength"
+ "kDYFEMTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount"
+ "kDYFEMTL4RenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance"
+ "kDYFEMTL4RenderCommandEncoder_drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer"
+ "kDYFEMTL4RenderCommandEncoder_drawMeshThreadgroupsWithIndirectBuffer_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup"
+ "kDYFEMTL4RenderCommandEncoder_drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup"
+ "kDYFEMTL4RenderCommandEncoder_drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup"
+ "kDYFEMTL4RenderCommandEncoder_drawPrimitives_indirectBuffer"
+ "kDYFEMTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount"
+ "kDYFEMTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount"
+ "kDYFEMTL4RenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance"
+ "kDYFEMTL4RenderCommandEncoder_endEncoding"
+ "kDYFEMTL4RenderCommandEncoder_endEncodingAndRetrieveProgramAddressTable"
+ "kDYFEMTL4RenderCommandEncoder_executeCommandsInBuffer_indirectBuffer"
+ "kDYFEMTL4RenderCommandEncoder_executeCommandsInBuffer_withRange"
+ "kDYFEMTL4RenderCommandEncoder_filterCounterRangeWithFirstBatch_lastBatch_filterIndex"
+ "kDYFEMTL4RenderCommandEncoder_insertDebugSignpost"
+ "kDYFEMTL4RenderCommandEncoder_popDebugGroup"
+ "kDYFEMTL4RenderCommandEncoder_pushDebugGroup"
+ "kDYFEMTL4RenderCommandEncoder_setArgumentTable_atStages"
+ "kDYFEMTL4RenderCommandEncoder_setBlendColorRed_green_blue_alpha"
+ "kDYFEMTL4RenderCommandEncoder_setColorAttachmentMap"
+ "kDYFEMTL4RenderCommandEncoder_setColorStoreAction_atIndex"
+ "kDYFEMTL4RenderCommandEncoder_setCullMode"
+ "kDYFEMTL4RenderCommandEncoder_setDepthBias_slopeScale_clamp"
+ "kDYFEMTL4RenderCommandEncoder_setDepthClipMode"
+ "kDYFEMTL4RenderCommandEncoder_setDepthStencilState"
+ "kDYFEMTL4RenderCommandEncoder_setDepthStoreAction"
+ "kDYFEMTL4RenderCommandEncoder_setDepthTestMinBound_maxBound"
+ "kDYFEMTL4RenderCommandEncoder_setFrontFacingWinding"
+ "kDYFEMTL4RenderCommandEncoder_setLabel"
+ "kDYFEMTL4RenderCommandEncoder_setLineWidth"
+ "kDYFEMTL4RenderCommandEncoder_setObjectThreadgroupMemoryLength_atIndex"
+ "kDYFEMTL4RenderCommandEncoder_setRenderPipelineState"
+ "kDYFEMTL4RenderCommandEncoder_setScissorRect"
+ "kDYFEMTL4RenderCommandEncoder_setScissorRects_count"
+ "kDYFEMTL4RenderCommandEncoder_setStencilFrontReferenceValue_backReferenceValue"
+ "kDYFEMTL4RenderCommandEncoder_setStencilReferenceValue"
+ "kDYFEMTL4RenderCommandEncoder_setStencilStoreAction"
+ "kDYFEMTL4RenderCommandEncoder_setThreadgroupMemoryLength_offset_atIndex"
+ "kDYFEMTL4RenderCommandEncoder_setToolsDispatchBufferSPI_atIndex_stages"
+ "kDYFEMTL4RenderCommandEncoder_setTriangleFillMode"
+ "kDYFEMTL4RenderCommandEncoder_setVertexAmplificationCount_viewMappings"
+ "kDYFEMTL4RenderCommandEncoder_setViewport"
+ "kDYFEMTL4RenderCommandEncoder_setViewports_count"
+ "kDYFEMTL4RenderCommandEncoder_setVisibilityResultMode_offset"
+ "kDYFEMTL4RenderCommandEncoder_updateFence_afterEncoderStages"
+ "kDYFEMTL4RenderCommandEncoder_waitForFence_beforeEncoderStages"
+ "kDYFEMTL4RenderCommandEncoder_writeTimestampWithGranularity_afterStage_intoHeap_atIndex"
+ "kDYFEMTL4RenderPipelineState_dealloc"
+ "kDYFEMTL4RenderPipelineState_fragmentFunctionHandleWithFunction"
+ "kDYFEMTL4RenderPipelineState_functionHandleWithBinaryFunction_stage"
+ "kDYFEMTL4RenderPipelineState_functionHandleWithFunction_stage"
+ "kDYFEMTL4RenderPipelineState_functionHandleWithName_stage"
+ "kDYFEMTL4RenderPipelineState_getFragmentShaderTelemetryID"
+ "kDYFEMTL4RenderPipelineState_getVertexShaderTelemetryID"
+ "kDYFEMTL4RenderPipelineState_imageblockMemoryLengthForDimensions"
+ "kDYFEMTL4RenderPipelineState_meshFunctionHandleWithFunction"
+ "kDYFEMTL4RenderPipelineState_newFragmentIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newFragmentShaderDebugInfo"
+ "kDYFEMTL4RenderPipelineState_newIntersectionFunctionTableWithDescriptor_stage"
+ "kDYFEMTL4RenderPipelineState_newMeshIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newObjectIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newRenderPipelineDescriptorForSpecialization"
+ "kDYFEMTL4RenderPipelineState_newRenderPipelineStateWithAdditionalBinaryFunctions_error"
+ "kDYFEMTL4RenderPipelineState_newRenderPipelineStateWithAdditionalBinaryFunctions_fragmentAdditionalBinaryFunctions_error"
+ "kDYFEMTL4RenderPipelineState_newTileIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newTileRenderPipelineStateWithAdditionalBinaryFunctions_error"
+ "kDYFEMTL4RenderPipelineState_newVertexIntersectionFunctionTableWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVertexShaderDebugInfo"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableFromFragmentStageWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableFromMeshStageWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableFromObjectStageWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableFromTileStageWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableFromVertexStageWithDescriptor"
+ "kDYFEMTL4RenderPipelineState_newVisibleFunctionTableWithDescriptor_stage"
+ "kDYFEMTL4RenderPipelineState_objectFunctionHandleWithFunction"
+ "kDYFEMTL4RenderPipelineState_reflectionForFunctionDescriptor"
+ "kDYFEMTL4RenderPipelineState_setEmulationMeshMaxPrimitiveCount"
+ "kDYFEMTL4RenderPipelineState_setEmulationMeshMaxVertexCount"
+ "kDYFEMTL4RenderPipelineState_setEmulationMeshShaderIntermediateBufferSlot"
+ "kDYFEMTL4RenderPipelineState_setEmulationMeshShaderPSO"
+ "kDYFEMTL4RenderPipelineState_setEmulationMeshSize"
+ "kDYFEMTL4RenderPipelineState_setEmulationObjectShaderIntermediateBufferSlot"
+ "kDYFEMTL4RenderPipelineState_setEmulationObjectShaderPSO"
+ "kDYFEMTL4RenderPipelineState_setEmulationPayloadMemoryLength"
+ "kDYFEMTL4RenderPipelineState_setEmulationPrimitiveTopology"
+ "kDYFEMTL4RenderPipelineState_setEmulationVertexShaderIntermediateBufferSlot"
+ "kDYFEMTL4RenderPipelineState_setUsesMeshShaderEmulation"
+ "kDYFEMTL4RenderPipelineState_tileFunctionHandleWithFunction"
+ "kDYFEMTL4RenderPipelineState_vertexFunctionHandleWithFunction"
+ "kDYFEMTLAccelerationStructureCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLAccelerationStructureCommandEncoder_insertSplit"
+ "kDYFEMTLBlitCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLBlitCommandEncoder_copyFromTensor_sourceOrigin_sourceDimensions_toTensor_destinationOrigin_destinationDimensions"
+ "kDYFEMTLBlitCommandEncoder_copyFromTensor_sourceSlice_toTensor_destinationSlice"
+ "kDYFEMTLBlitCommandEncoder_insertSplit"
+ "kDYFEMTLBuffer_newTensorWithDescriptor_offset_error"
+ "kDYFEMTLCommandBuffer___waitUntilCompletedAsync"
+ "kDYFEMTLCommandBuffer___waitUntilScheduledAsync"
+ "kDYFEMTLComputeCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLComputeCommandEncoder_insertSplit"
+ "kDYFEMTLComputeCommandEncoder_setToolsDispatchBufferSPI_atIndex"
+ "kDYFEMTLComputePipelineState_functionHandleWithBinaryFunction"
+ "kDYFEMTLComputePipelineState_functionHandleWithName"
+ "kDYFEMTLComputePipelineState_newComputePipelineStateWithAdditionalBinaryFunctions_resourceIndices_error"
+ "kDYFEMTLComputePipelineState_newComputePipelineStateWithBinaryFunctions_error"
+ "kDYFEMTLDepthStencilState_gpuResourceID"
+ "kDYFEMTLDepthStencilState_uniqueIdentifier"
+ "kDYFEMTLDevice_functionHandleWithBinaryFunction"
+ "kDYFEMTLDevice_functionHandleWithFunction"
+ "kDYFEMTLDevice_functionHandleWithFunction_resourceIndex"
+ "kDYFEMTLDevice_mtlTensorFromGpuResourceID"
+ "kDYFEMTLDevice_newArchiveWithURL_error"
+ "kDYFEMTLDevice_newArgumentTableWithDescriptor_error"
+ "kDYFEMTLDevice_newBufferWithLength_options_placementSparsePageSize"
+ "kDYFEMTLDevice_newCommandAllocator"
+ "kDYFEMTLDevice_newCommandAllocatorWithDescriptor_error"
+ "kDYFEMTLDevice_newCommandBuffer"
+ "kDYFEMTLDevice_newCommandQueue4"
+ "kDYFEMTLDevice_newCompilerWithDescriptor_error"
+ "kDYFEMTLDevice_newCounterHeapWithDescriptor_error"
+ "kDYFEMTLDevice_newFrameInterpolatorWithDescriptor"
+ "kDYFEMTLDevice_newLibraryWithData_name_error"
+ "kDYFEMTLDevice_newLibraryWithMPSGraphPackageURL_name_error"
+ "kDYFEMTLDevice_newLibraryWithURL_name_error"
+ "kDYFEMTLDevice_newMTL4CommandQueue"
+ "kDYFEMTLDevice_newMTL4CommandQueueWithDescriptor_error"
+ "kDYFEMTLDevice_newMTL4FrameInterpolatorWithDescriptor_compiler"
+ "kDYFEMTLDevice_newMTL4SpatialScalerWithDescriptor_compiler"
+ "kDYFEMTLDevice_newMTL4TemporalDenoisedScalerWithDescriptor_compiler"
+ "kDYFEMTLDevice_newMTL4TemporalScalerWithDescriptor_compiler"
+ "kDYFEMTLDevice_newPipelineDataSetSerializerWithDescriptor"
+ "kDYFEMTLDevice_newTemporalDenoisedScalerWithDescriptor"
+ "kDYFEMTLDevice_newTensorWithBuffer_descriptor_offset_strides_error"
+ "kDYFEMTLDevice_newTensorWithDescriptor_error"
+ "kDYFEMTLDevice_newTensorWithIOSurface_descriptor_plane_offset_strides_error"
+ "kDYFEMTLDevice_newTextureViewPoolWithDescriptor_error"
+ "kDYFEMTLDevice_queryTimestampFrequency"
+ "kDYFEMTLDevice_sizeOfCounterHeapEntry"
+ "kDYFEMTLDevice_tensorSizeAndAlignWithDescriptor"
+ "kDYFEMTLFXFrameInterpolator_dealloc"
+ "kDYFEMTLFXFrameInterpolator_encodeToCommandBuffer"
+ "kDYFEMTLFXFrameInterpolator_setAspectRatio"
+ "kDYFEMTLFXFrameInterpolator_setColorTexture"
+ "kDYFEMTLFXFrameInterpolator_setDeltaTime"
+ "kDYFEMTLFXFrameInterpolator_setDepthReversed"
+ "kDYFEMTLFXFrameInterpolator_setDepthTexture"
+ "kDYFEMTLFXFrameInterpolator_setFarPlane"
+ "kDYFEMTLFXFrameInterpolator_setFence"
+ "kDYFEMTLFXFrameInterpolator_setFieldOfView"
+ "kDYFEMTLFXFrameInterpolator_setIsUITextureComposited"
+ "kDYFEMTLFXFrameInterpolator_setJitterOffsetX"
+ "kDYFEMTLFXFrameInterpolator_setJitterOffsetY"
+ "kDYFEMTLFXFrameInterpolator_setMaskTexture"
+ "kDYFEMTLFXFrameInterpolator_setMotionTexture"
+ "kDYFEMTLFXFrameInterpolator_setMotionVectorScaleX"
+ "kDYFEMTLFXFrameInterpolator_setMotionVectorScaleY"
+ "kDYFEMTLFXFrameInterpolator_setNearPlane"
+ "kDYFEMTLFXFrameInterpolator_setOutputTexture"
+ "kDYFEMTLFXFrameInterpolator_setPrevColorTexture"
+ "kDYFEMTLFXFrameInterpolator_setReset"
+ "kDYFEMTLFXFrameInterpolator_setResetHistory"
+ "kDYFEMTLFXFrameInterpolator_setShouldResetHistory"
+ "kDYFEMTLFXFrameInterpolator_setUITexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_dealloc"
+ "kDYFEMTLFXTemporalDenoisedScaler_encodeToCommandBuffer"
+ "kDYFEMTLFXTemporalDenoisedScaler_encodeToCommandQueue"
+ "kDYFEMTLFXTemporalDenoisedScaler_setColorTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setDenoiseStrengthMaskTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setDepthReversed"
+ "kDYFEMTLFXTemporalDenoisedScaler_setDepthTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setDiffuseAlbedoTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setExposureTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setFence"
+ "kDYFEMTLFXTemporalDenoisedScaler_setInputContentHeight"
+ "kDYFEMTLFXTemporalDenoisedScaler_setInputContentWidth"
+ "kDYFEMTLFXTemporalDenoisedScaler_setJitterOffsetX"
+ "kDYFEMTLFXTemporalDenoisedScaler_setJitterOffsetY"
+ "kDYFEMTLFXTemporalDenoisedScaler_setMotionTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setMotionVectorScaleX"
+ "kDYFEMTLFXTemporalDenoisedScaler_setMotionVectorScaleY"
+ "kDYFEMTLFXTemporalDenoisedScaler_setNormalTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setOutputTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setPreExposure"
+ "kDYFEMTLFXTemporalDenoisedScaler_setPreUpscaleComposeTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setReactiveMaskTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setReset"
+ "kDYFEMTLFXTemporalDenoisedScaler_setResetHistory"
+ "kDYFEMTLFXTemporalDenoisedScaler_setRoughnessTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setShouldResetHistory"
+ "kDYFEMTLFXTemporalDenoisedScaler_setSpecularAlbedoTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setSpecularHitDistanceTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setTransparencyOverlayTexture"
+ "kDYFEMTLFXTemporalDenoisedScaler_setViewToClipMatrix"
+ "kDYFEMTLFXTemporalDenoisedScaler_setWorldToViewMatrix"
+ "kDYFEMTLFunctionHandle_gpuResourceID"
+ "kDYFEMTLFunctionHandle_resourceIndex"
+ "kDYFEMTLIndirectRenderCommand_setBlendColorRed_green_blue_alpha"
+ "kDYFEMTLIndirectRenderCommand_setCullMode"
+ "kDYFEMTLIndirectRenderCommand_setDepthBias_slopeScale_clamp"
+ "kDYFEMTLIndirectRenderCommand_setDepthClipMode"
+ "kDYFEMTLIndirectRenderCommand_setDepthStencilState"
+ "kDYFEMTLIndirectRenderCommand_setDepthTestMinBound_maxBound"
+ "kDYFEMTLIndirectRenderCommand_setFrontFacingWinding"
+ "kDYFEMTLIndirectRenderCommand_setScissorRect"
+ "kDYFEMTLIndirectRenderCommand_setScissorRects_count"
+ "kDYFEMTLIndirectRenderCommand_setStencilFrontReferenceValue_backReferenceValue"
+ "kDYFEMTLIndirectRenderCommand_setStencilReferenceValue"
+ "kDYFEMTLIndirectRenderCommand_setToolsDispatchBufferSPI_atIndex_stages"
+ "kDYFEMTLIndirectRenderCommand_setTriangleFillMode"
+ "kDYFEMTLIndirectRenderCommand_setViewport"
+ "kDYFEMTLIndirectRenderCommand_setViewports_count"
+ "kDYFEMTLLibrary_reflectionForFunctionWithName"
+ "kDYFEMTLParallelRenderCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLParallelRenderCommandEncoder_insertSplit"
+ "kDYFEMTLRenderCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLRenderCommandEncoder_insertSplit"
+ "kDYFEMTLRenderCommandEncoder_setColorAttachmentMap"
+ "kDYFEMTLRenderCommandEncoder_setDepthTestMinBound_maxBound"
+ "kDYFEMTLRenderPipelineState_functionHandleWithBinaryFunction_stage"
+ "kDYFEMTLRenderPipelineState_functionHandleWithName_stage"
+ "kDYFEMTLRenderPipelineState_newRenderPipelineStateWithBinaryFunctions_error"
+ "kDYFEMTLResourceStateCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLResourceStateCommandEncoder_insertSplit"
+ "kDYFEMTLTensorBinding_dealloc"
+ "kDYFEMTLTensor_allocatedSize"
+ "kDYFEMTLTensor_allocationID"
+ "kDYFEMTLTensor_dealloc"
+ "kDYFEMTLTensor_doesAliasAllResources_count"
+ "kDYFEMTLTensor_doesAliasAnyResources_count"
+ "kDYFEMTLTensor_doesAliasResource"
+ "kDYFEMTLTensor_getBytes_strides_fromSlice"
+ "kDYFEMTLTensor_gpuResourceID"
+ "kDYFEMTLTensor_harvested_replaceSliceOrigin_sliceDimensions_withBytes_strides"
+ "kDYFEMTLTensor_isAliasable"
+ "kDYFEMTLTensor_isComplete"
+ "kDYFEMTLTensor_isPurgeable"
+ "kDYFEMTLTensor_isTensorViewableWithReshapedDescriptor"
+ "kDYFEMTLTensor_isWriteComplete"
+ "kDYFEMTLTensor_makeAliasable"
+ "kDYFEMTLTensor_newTensorViewWithReshapedDescriptor_error"
+ "kDYFEMTLTensor_newTensorViewWithSlice_error"
+ "kDYFEMTLTensor_replaceSliceOrigin_sliceDimensions_withBytes_strides"
+ "kDYFEMTLTensor_replaceSlice_withBytes_strides"
+ "kDYFEMTLTensor_resourceIndex"
+ "kDYFEMTLTensor_setLabel"
+ "kDYFEMTLTensor_setOwnerWithIdentity"
+ "kDYFEMTLTensor_setPurgeableState"
+ "kDYFEMTLTensor_setResponsibleProcess"
+ "kDYFEMTLTensor_timeSinceTouched"
+ "kDYFEMTLTensor_uniqueIdentifier"
+ "kDYFEMTLTensor_waitUntilComplete"
+ "kDYFEMTLTextureViewPool_copyResourceStatesFromPool_sourceRange_destinationIndex"
+ "kDYFEMTLTextureViewPool_copyResourceViewsFromPool_sourceRange_destinationIndex"
+ "kDYFEMTLTextureViewPool_dealloc"
+ "kDYFEMTLTextureViewPool_setBufferView_descriptor_offset_bytesPerRow_atIndex"
+ "kDYFEMTLTextureViewPool_setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex"
+ "kDYFEMTLTextureViewPool_setTextureView_atIndex"
+ "kDYFEMTLTextureViewPool_setTextureView_descriptor_atIndex"
+ "kDYFEMTLTexture_newTextureViewWithDescriptor"
+ "kDYFEMTLVideoCommandEncoder_barrierAfterQueueStages_beforeStages"
+ "kDYFEMTLVideoCommandEncoder_insertSplit"
+ "lastCommittedCommandBuffer"
+ "lastCommittedCommandBufferGeneration"
+ "levelRange"
+ "llvmVersion"
+ "lookupArchives"
+ "machineLearningCommandEncoder"
+ "machineLearningFunctionDescriptor"
+ "maxBufferBindCount"
+ "maxCompatiblePlacementSparsePageSize"
+ "maxNumRegisters"
+ "maxSamplerStateBindCount"
+ "maxTextureBindCount"
+ "maxToolsDispatchBindings"
+ "maximumCompilerProcessesCount"
+ "meshFunctionDescriptor"
+ "meshLinkingDescriptor"
+ "metalfx-frame-interpolators"
+ "metalfx-mtl4-frame-interpolators"
+ "metalfx-mtl4-spatial-scalers"
+ "metalfx-mtl4-temporal-scalers"
+ "metalfx-temporal-denoised-scalers"
+ "ml-pipeline-state"
+ "ml-pipeline-states"
+ "mtl4-argument-table"
+ "mtl4-command-allocator"
+ "mtl4-command-buffer"
+ "mtl4-command-queue"
+ "mtl4CommandQueue"
+ "mtlTensorFromGpuResourceID:"
+ "nearPlane"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:"
+ "newBinaryFunctionWithDescriptor:compilerTaskOptions:error:"
+ "newBinaryFunctionWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCompilerWithDescriptor:error:"
+ "newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:"
+ "newComputePipelineStateWithBinaryFunctions:error:"
+ "newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:"
+ "newComputePipelineStateWithDescriptor:compilerTaskOptions:error:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:"
+ "newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newDynamicLibrary:completionHandler:"
+ "newDynamicLibraryWithURL:completionHandler:"
+ "newFrameInterpolatorWithDevice:"
+ "newFrameInterpolatorWithDevice:compiler:"
+ "newIndexedConstantArray"
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
+ "newSpatialScalerWithDevice:compiler:"
+ "newTemporalDenoisedScalerWithDevice:"
+ "newTemporalDenoisedScalerWithDevice:compiler:"
+ "newTemporalScalerWithDevice:compiler:"
+ "newTensorViewWithReshapedDescriptor:error:"
+ "newTensorViewWithSlice:error:"
+ "newTensorWithDescriptor:error:"
+ "newTensorWithDescriptor:offset:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "newTextureViewWithDescriptor:"
+ "normalTexture"
+ "normalTextureFormat"
+ "normalTextureUsage"
+ "objectFunctionDescriptor"
+ "objectLinkingDescriptor"
+ "outputTextureBarrierStages"
+ "parentStream"
+ "parentTensor"
+ "pipelineDataSetSerializer"
+ "pipelineOptions"
+ "pm_protect"
+ "postVertexDumpBufferIndex"
+ "presentDownloadSize"
+ "prevColorTexture"
+ "process_name"
+ "queryTimestampFrequency"
+ "rank"
+ "refitAccelerationStructure:descriptor:destination:scratchBuffer:"
+ "refitAccelerationStructure:descriptor:destination:scratchBuffer:options:"
+ "reflectionForFunctionDescriptor:"
+ "reflectionForFunctionWithName:"
+ "renderCommandEncoderWithDescriptor:options:"
+ "replaceSliceOrigin:sliceDimensions:withBytes:strides:"
+ "requestor"
+ "requiredThreadsPerMeshThreadgroup"
+ "requiredThreadsPerObjectThreadgroup"
+ "requiredThreadsPerThreadgroup"
+ "requiredThreadsPerTileThreadgroup"
+ "requiresLegacyCompilerProcessesCount"
+ "resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:"
+ "resourceViewCount"
+ "restart_reason"
+ "roughnessTexture"
+ "roughnessTextureFormat"
+ "roughnessTextureUsage"
+ "sampledComputeCommandEncoder:capacity:"
+ "scaler"
+ "scaler4"
+ "serializeAsArchiveAndFlushToURL:error:"
+ "serializeAsPipelinesScriptWithError:"
+ "serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:"
+ "serializePrimitiveAccelerationStructure:toBuffer:"
+ "setAddress:atIndex:"
+ "setAddress:attributeStride:atIndex:"
+ "setAlphaToCoverageState:"
+ "setAlphaToOneState:"
+ "setArgumentTable:"
+ "setArgumentTable:atStages:"
+ "setAspectRatio:"
+ "setBaseResourceID:"
+ "setBinaryLinkedFunctions:"
+ "setBlendingState:"
+ "setColorAttachmentMap:"
+ "setColorAttachmentMappingState:"
+ "setColorTextureBarrierStages:"
+ "setCompositedUITexture:"
+ "setComputeFunctionDescriptor:"
+ "setConfiguration:"
+ "setCurveEndCaps:"
+ "setDeltaTime:"
+ "setDenoiseStrengthMaskTexture:"
+ "setDenoiseStrengthMaskTextureEnabled:"
+ "setDenoiseStrengthMaskTextureFormat:"
+ "setDenoiserScaler4:"
+ "setDenoiserScaler:"
+ "setDiffuseAlbedoTexture:"
+ "setDiffuseAlbedoTextureFormat:"
+ "setDimensions:"
+ "setEnableAccelerationStructureViewerInstrumentation:"
+ "setEnablePerformanceStatistics:"
+ "setEnablePostMeshDump:"
+ "setEnablePostVertexDump:"
+ "setEnableResourcePatchingInstrumentation:"
+ "setEnableResourceUsageInstrumentation:"
+ "setFarPlane:"
+ "setFieldOfView:"
+ "setForceBaseResourceID:"
+ "setFragmentFunctionDescriptor:"
+ "setFunctionDescriptor:"
+ "setFunctionDescriptors:"
+ "setFunctionGraph:"
+ "setInitializeBindings:"
+ "setIsUITextureComposited:"
+ "setLevelRange:"
+ "setLibrary:"
+ "setLookupArchives:"
+ "setMachineLearningFunctionDescriptor:"
+ "setMaxBufferBindCount:"
+ "setMaxCompatiblePlacementSparsePageSize:"
+ "setMaxNumRegisters:"
+ "setMaxSamplerStateBindCount:"
+ "setMaxTextureBindCount:"
+ "setMaxToolsDispatchBindings:"
+ "setMaxTotalThreadgroupsPerMeshGrid:"
+ "setMeshFunctionDescriptor:"
+ "setNearPlane:"
+ "setNormalTexture:"
+ "setNormalTextureFormat:"
+ "setObjectFunctionDescriptor:"
+ "setPhysicalIndex:forLogicalIndex:"
+ "setPipelineDataSetSerializer:"
+ "setPipelineState:"
+ "setPostVertexDumpBufferIndex:"
+ "setPresentDownloadSize:"
+ "setPrevColorTexture:"
+ "setRequiredThreadsPerMeshThreadgroup:"
+ "setRequiredThreadsPerObjectThreadgroup:"
+ "setRequiredThreadsPerThreadgroup:"
+ "setRequiresLegacyCompilerProcessesCount:"
+ "setResource:atBufferIndex:"
+ "setResourceViewCount:"
+ "setRoughnessTexture:"
+ "setRoughnessTextureFormat:"
+ "setScaler4:"
+ "setScaler:"
+ "setShaderReflection:"
+ "setShaderValidation:"
+ "setShouldResetHistory:"
+ "setSliceRange:"
+ "setSource:"
+ "setSpecularAlbedoTexture:"
+ "setSpecularAlbedoTextureFormat:"
+ "setSpecularHitDistanceTexture:"
+ "setSpecularHitDistanceTextureEnabled:"
+ "setSpecularHitDistanceTextureFormat:"
+ "setStrides:"
+ "setSupportAttributeStrides:"
+ "setSupportBinaryLinking:"
+ "setSupportColorAttachmentMapping:"
+ "setSupportFragmentBinaryLinking:"
+ "setSupportMeshBinaryLinking:"
+ "setSupportObjectBinaryLinking:"
+ "setSupportVertexBinaryLinking:"
+ "setTextureView:atIndex:"
+ "setTextureView:descriptor:atIndex:"
+ "setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:"
+ "setTileFunctionDescriptor:"
+ "setToolsDispatchBufferSPI:atIndex:"
+ "setToolsDispatchBufferSPI:atIndex:stages:"
+ "setTransparencyOverlayTexture:"
+ "setTransparencyOverlayTextureEnabled:"
+ "setTransparencyOverlayTextureFormat:"
+ "setUITexture:"
+ "setUITextureFormat:"
+ "setVertexDescriptor:"
+ "setVertexFunctionDescriptor:"
+ "setViewToClipMatrix:"
+ "setVisibilityResultType:"
+ "setWorldToViewMatrix:"
+ "shaderReflection"
+ "shouldResetHistory"
+ "sideband"
+ "signalDrawable:"
+ "sizeOfCounterHeapEntry:"
+ "sliceRange"
+ "source"
+ "sparseBufferTier"
+ "sparseTextureTier"
+ "specularAlbedoTexture"
+ "specularAlbedoTextureFormat"
+ "specularAlbedoTextureUsage"
+ "specularHitDistanceTexture"
+ "specularHitDistanceTextureFormat"
+ "specularHitDistanceTextureUsage"
+ "stages"
+ "strcmp(targetFile->name, target) == 0"
+ "strides"
+ "strlen(link) > 0 && strlen(target) > 0"
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
+ "supportsMetal4FX:"
+ "supportsTensors"
+ "targetFile"
+ "tensor"
+ "tensorDataType"
+ "tensorSizeAndAlignWithDescriptor:"
+ "tensors"
+ "texture->arraySliceCount == 6"
+ "texture->arraySliceCount >= 6 && texture->arraySliceCount % 6 == 0"
+ "texture-view-pool"
+ "texture-view-pools"
+ "threadsPerCompilerProcess"
+ "tileFunctionDescriptor"
+ "tileLinkingDescriptor"
+ "transparencyOverlayTexture"
+ "transparencyOverlayTextureFormat"
+ "transparencyOverlayTextureUsage"
+ "uiTexture"
+ "uiTextureComposited"
+ "uiTextureFormat"
+ "uiTextureUsage"
+ "unknown"
+ "unmapResult == 0"
+ "updateBufferMappings:heap:operations:count:"
+ "updateDrawableStream:"
+ "updateFence:afterEncoderStages:"
+ "updateTextureMappings:heap:operations:count:"
+ "v104@0:8@\"<MTLTexture>\"16Q24Q32{?={?=QQQ}{?=QQQ}}40r^v88Q96"
+ "v120@0:8@\"<MTLTexture>\"16Q24Q32{?={?=QQQ}{?=QQQ}}40{?=dddd}88"
+ "v128@0:8@\"<MTLTexture>\"16Q24Q32{?={?=QQQ}{?=QQQ}}40{?=dddd}88Q120"
+ "v16@?0@\"<MTL4CommitFeedback>\"8"
+ "v24@0:8@\"<MTL4ArgumentTable>\"16"
+ "v24@0:8@\"<MTL4CommandAllocator>\"16"
+ "v24@0:8@\"<MTL4CommandBuffer>\"16"
+ "v24@0:8@\"<MTL4MachineLearningPipelineState>\"16"
+ "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMap\"16"
+ "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMapSPI\"16"
+ "v24@0:8^{GTTraceStream=}16"
+ "v28@0:8I16I20I24"
+ "v28@?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLVertexAttribute}^{GTMTLAttribute}^**}16B24"
+ "v32@0:8@\"<MTL4ArgumentTable>\"16Q24"
+ "v32@0:8@\"<MTL4CommandAllocator>\"16@\"MTL4CommandBufferOptions\"24"
+ "v32@0:8@\"<MTL4CounterHeap>\"16Q24"
+ "v32@0:8{MTLResourceID=Q}16Q24"
+ "v40@0:8@\"<MTLAccelerationStructure>\"16{MTL4BufferRange=QQ}24"
+ "v40@0:8@16{MTL4BufferRange=QQ}24"
+ "v40@0:8Q16Q24q32"
+ "v40@0:8q16@\"<MTL4CounterHeap>\"24Q32"
+ "v40@0:8q16@24Q32"
+ "v40@0:8r^@16Q24@\"MTL4CommitOptions\"32"
+ "v40@0:8r^@16Q24@32"
+ "v44@0:8@\"<MTLBuffer>\"16{_NSRange=QQ}24I40"
+ "v48@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24{MTL4BufferRange=QQ}32"
+ "v48@0:8@\"<MTLAccelerationStructure>\"16@\"NSArray\"24{MTL4BufferRange=QQ}32"
+ "v48@0:8@\"<MTLBuffer>\"16@\"<MTLBuffer>\"24r^{?={_NSRange=QQ}Q}32Q40"
+ "v48@0:8@\"<MTLBuffer>\"16@\"<MTLHeap>\"24r^{?=Q{_NSRange=QQ}Q}32Q40"
+ "v48@0:8@\"<MTLTexture>\"16@\"<MTLHeap>\"24r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}32Q40"
+ "v48@0:8@\"<MTLTexture>\"16@\"<MTLTexture>\"24r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}32Q40"
+ "v48@0:8@\"MTLTensorExtents\"16@\"MTLTensorExtents\"24r^v32@\"MTLTensorExtents\"40"
+ "v48@0:8@16@24r^v32@40"
+ "v48@0:8@16@24r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}32Q40"
+ "v48@0:8@16@24r^{?=Q{_NSRange=QQ}Q}32Q40"
+ "v48@0:8@16@24r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}32Q40"
+ "v48@0:8@16@24r^{?={_NSRange=QQ}Q}32Q40"
+ "v48@0:8@16@24{MTL4BufferRange=QQ}32"
+ "v48@0:8Q16{?=QQQ}24"
+ "v48@0:8^v16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"MTLTensorExtents\"40"
+ "v48@0:8^v16@24@32@40"
+ "v48@0:8q16Q24@\"<MTL4CounterHeap>\"32Q40"
+ "v48@0:8q16Q24@32Q40"
+ "v48@0:8{MTL4BufferRange=QQ}16{MTL4BufferRange=QQ}32"
+ "v56@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24@\"<MTLAccelerationStructure>\"32{MTL4BufferRange=QQ}40"
+ "v56@0:8@16@24@32{MTL4BufferRange=QQ}40"
+ "v64@0:8@\"<MTLAccelerationStructure>\"16@\"MTL4AccelerationStructureDescriptor\"24@\"<MTLAccelerationStructure>\"32{MTL4BufferRange=QQ}40Q56"
+ "v64@0:8@\"<MTLTensor>\"16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"<MTLTensor>\"40@\"MTLTensorExtents\"48@\"MTLTensorExtents\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "v64@0:8@16@24@32{MTL4BufferRange=QQ}40Q56"
+ "v64@0:8Q16Q24Q32Q40Q48Q56"
+ "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24@\"<MTLBuffer>\"40Q48@\"<MTLFence>\"56@\"<MTLFence>\"64"
+ "v72@0:8@16{_NSRange=QQ}24@40Q48@56@64"
+ "v72@0:8Q16{?=QQQ}24{?=QQQ}48"
+ "v80@0:8Q16Q24Q32Q40Q48Q56q64Q72"
+ "validationReflection"
+ "vertexFunctionDescriptor"
+ "vertexLinkingDescriptor"
+ "viewToClipMatrix"
+ "visibilityResultType"
+ "waitForDrawable:"
+ "waitForEvent:value:timeout:"
+ "waitForFence:beforeEncoderStages:"
+ "warning: -[MTLCommandQueue insertDebugCaptureBoundary] is not considered a valid gputrace boundary anymore."
+ "worldToViewMatrix"
+ "writeAccelerationStructureSerializationData:toBuffer:"
+ "writeAccelerationStructureTraversalDepth:toBuffer:"
+ "writeCompactedAccelerationStructureSize:toBuffer:"
+ "writeDeserializedAccelerationStructureSize:toBuffer:"
+ "writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:"
+ "writeSerializedAccelerationStructureSize:toBuffer:"
+ "writeTimestampIntoHeap:atIndex:"
+ "writeTimestampWithGranularity:afterStage:intoHeap:atIndex:"
+ "writeTimestampWithGranularity:intoHeap:atIndex:"
+ "written == true"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"
+ "{GTMTLCoreSync=\"event\"@\"<MTLSharedEvent>\"\"nextSignal\"AQ}"
+ "{MTLResourceID=Q}32@0:8@\"<MTLTexture>\"16Q24"
+ "{MTLResourceID=Q}32@0:8@16Q24"
+ "{MTLResourceID=Q}40@0:8@\"<MTLTexture>\"16@\"MTLTextureViewDescriptor\"24Q32"
+ "{MTLResourceID=Q}40@0:8@16@24Q32"
+ "{MTLResourceID=Q}48@0:8@\"<MTLResourceViewPool>\"16{_NSRange=QQ}24Q40"
+ "{MTLResourceID=Q}48@0:8@16{_NSRange=QQ}24Q40"
+ "{MTLResourceID=Q}56@0:8@\"<MTLBuffer>\"16@\"MTLTextureDescriptor\"24Q32Q40Q48"
+ "{MTLResourceID=Q}56@0:8@16@24Q32Q40Q48"
+ "🔄 Transition aborted: waiting until command buffer %llu is scheduled"
+ "🔄 Transition aborted: waiting until command buffer %llu is scheduled\n"
- "\t"
- "        armPreparedCapture: true"
- "        armPreparedCapture: true\n"
- "        lockGraphicsAfterCapture: true"
- "        lockGraphicsAfterCapture: true\n"
- "        sandboxExtensionHandle: %llu"
- "        sandboxExtensionHandle: %llu\n"
- "       useNewArchiveFormat: true"
- "       useNewArchiveFormat: true\n"
- "!(entry->flags & 0x00000002)"
- "%@.%@.enableLog"
- "0 <= entry->name_entry && entry->name_entry < self->index.string_table->nelts"
- "0 <= fd"
- "1.2.12"
- "@\"NSObject<OS_os_log>\""
- "@24@0:8^{GTMTLGuestAppClient=@@@@{os_unfair_lock_s=I}IQQQAq@@@@iiQdBB[6c]}16"
- "@32@0:8@16^{GTTraceContext={_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}24"
- "BoundaryLess"
- "Buffer"
- "Capture-ProcessMessage"
- "CaptureSentAllData"
- "CaptureSentAllMetadata"
- "CaptureSentUsedData"
- "CaptureService"
- "DYCaptureSession.unusedAccelerationStructureCount"
- "DYCaptureSession.unusedEventCount"
- "DYCaptureSession.unusedFenceCount"
- "DYCaptureSession.unusedHeapCount"
- "DYCaptureSession.unusedIOCommandQueueCount"
- "DYCaptureSession.unusedIndirectCommandBufferCount"
- "DYCaptureSession.unusedInternalAccelerationStructureCount"
- "DYCaptureSession.unusedInternalBufferCount"
- "DYCaptureSession.unusedInternalCommandQueueCount"
- "DYCaptureSession.unusedInternalComputePipelineStateCount"
- "DYCaptureSession.unusedInternalDepthStencilStateCount"
- "DYCaptureSession.unusedInternalEventCount"
- "DYCaptureSession.unusedInternalFenceCount"
- "DYCaptureSession.unusedInternalFunctionCount"
- "DYCaptureSession.unusedInternalHeapCount"
- "DYCaptureSession.unusedInternalIndirectCommandBufferCount"
- "DYCaptureSession.unusedInternalLibraryCount"
- "DYCaptureSession.unusedInternalRenderPipelineStateCount"
- "DYCaptureSession.unusedInternalSamplerStateCount"
- "DYCaptureSession.unusedInternalTextureCount"
- "DYCaptureSession.unusedInternalTextureLayoutCount"
- "DYCaptureSession.unusedTextureLayoutCount"
- "GPUTOOLS(warning): Log uninitialized, please call GTCoreLogInit(), logging to OS_LOG_DEFAULT instead"
- "GT_HOST_URL_MTL"
- "Indirect command buffer"
- "LinkedOnApexOrLater"
- "LockOpenGLAfterCompletion"
- "Log already initialized, did you call GTCoreLogInit twice?"
- "MTLCAPTURE_NEW_ARCHIVE_FORMAT"
- "PerformanceStatistics"
- "PerformanceStatisticsActiveDevices"
- "Q24@0:8@\"<GTMTLCaptureServiceObserver>\"16"
- "Q24@0:8@\"<GTMTLTelemetryServiceObserver>\"16"
- "Rasterization rate map"
- "Resource"
- "Shared event agent mask"
- "T@\"<MTLBuffer>\",?,&"
- "TQ,?"
- "T^{GTTraceContext={_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]},R"
- "TelemetryService"
- "Texture"
- "Threadgroup buffer"
- "TriggerOnNextGLCommand"
- "Unrecognized message: %d"
- "[9B]"
- "^{GTTraceContext={_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}"
- "^{GTTraceContext={_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}16@0:8"
- "_downloadRequestNew:atPoint:dispatchGroup:"
- "_log"
- "an MTLCommandQueue"
- "buffer name"
- "bundleIdentifier"
- "capture serial"
- "captured frames counter"
- "category"
- "customMessage"
- "device profile"
- "entry->flags & 0x00000002"
- "executable-path"
- "executablePath"
- "fail: Invalid log tag: %llu"
- "fenum"
- "frame duration"
- "frame index"
- "gputools.global_sync"
- "gttrace-dna"
- "gttrace-downloadXXXXXX"
- "gttrace-range"
- "gttrace-store"
- "gttrace-streams"
- "has pstream header"
- "interpose-feature-version"
- "interpose-patch-version"
- "kDYDaemonResumeInferior"
- "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
- "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
- "kDYGenerateShaderDebuggerTrace"
- "kDYMessageApplicationIcon"
- "kDYMessageApplicationList"
- "kDYMessageBreakpoint"
- "kDYMessageBreakpointContinue"
- "kDYMessageBringGuestAppToForeground"
- "kDYMessageCaptureActivateSession"
- "kDYMessageCaptureCreateAlias"
- "kDYMessageCaptureData"
- "kDYMessageCaptureDataChunk"
- "kDYMessageCaptureDataReferenceCounts"
- "kDYMessageCaptureInvalidateSession"
- "kDYMessageCaptureSentAllData"
- "kDYMessageCaptureSentAllMetadata"
- "kDYMessageCaptureSentUsedData"
- "kDYMessageCaptureStart"
- "kDYMessageCaptureStarted"
- "kDYMessageCaptureStop"
- "kDYMessageClearResourceOverrides"
- "kDYMessageCurrentDrawFramebufferImage"
- "kDYMessageDaemonCreateGuestAppTransport"
- "kDYMessageDaemonDeviceCapabilities"
- "kDYMessageDaemonLaunchDebugServer"
- "kDYMessageDaemonRegisterInferior"
- "kDYMessageDeviceCompatibilityCapabilities"
- "kDYMessageFSStreamAbort"
- "kDYMessageFSStreamFinishedSending"
- "kDYMessageFSStreamFinishedSendingAck"
- "kDYMessageFSStreamInitializeTransfer"
- "kDYMessageFSStreamInitializeTransferAck"
- "kDYMessageFSStreamItemData"
- "kDYMessageFetchResourceList"
- "kDYMessageFetchResourceObject"
- "kDYMessageFetchResourceObjectBatch"
- "kDYMessageFetchState"
- "kDYMessageGPUToolsVersionQuery"
- "kDYMessageGuestAppCADisplayLinkEvent"
- "kDYMessageGuestAppCAMetalLayersInfo"
- "kDYMessageGuestAppCSSignature"
- "kDYMessageGuestAppGLContextsInfo"
- "kDYMessageGuestAppInvalidateSavePointerAliases"
- "kDYMessageGuestAppLockGraphics"
- "kDYMessageGuestAppMTLCaptureScopesInfo"
- "kDYMessageGuestAppMTLCommandBuffersCaptured"
- "kDYMessageGuestAppMTLCommandQueuesInfo"
- "kDYMessageGuestAppMTLDevicesInfo"
- "kDYMessageGuestAppMultitaskingSuspensionState"
- "kDYMessageGuestAppProfilingData"
- "kDYMessageGuestAppTerminated"
- "kDYMessageGuestAppTimebase"
- "kDYMessageGuestAppUnlockGraphics"
- "kDYMessageInferiorLaunched"
- "kDYMessageInferiorSignalInterposeSemaphore"
- "kDYMessageKillGuestApp"
- "kDYMessageLaunchGuestApp"
- "kDYMessageMobileDaemonPosixSpawn"
- "kDYMessageMobileDaemonReloadUIServer"
- "kDYMessageReplayerAppReady"
- "kDYMessageReplayerArchivesDirectoryPath"
- "kDYMessageReplayerBeginDebugArchive"
- "kDYMessageReplayerDebugDisableFunctions"
- "kDYMessageReplayerDebugEnableDrawCallPresent"
- "kDYMessageReplayerDebugEnableFunctions"
- "kDYMessageReplayerDebugEnableOutlinePresent"
- "kDYMessageReplayerDebugEnableWireframePresent"
- "kDYMessageReplayerDebugFuncStop"
- "kDYMessageReplayerDebugStatus"
- "kDYMessageReplayerDebugWireframeLineColor"
- "kDYMessageReplayerDebugWireframeLineWidth"
- "kDYMessageReplayerDeleteAllArchives"
- "kDYMessageReplayerDerivedCounterData"
- "kDYMessageReplayerEndDebugArchive"
- "kDYMessageReplayerExperimentResult"
- "kDYMessageReplayerGenerateDependencyGraphThumbnails"
- "kDYMessageReplayerGenerateThumbnails"
- "kDYMessageReplayerLoadArchives"
- "kDYMessageReplayerQueryLoadedArchivesInfo"
- "kDYMessageReplayerQueryShaderInfo"
- "kDYMessageReplayerReplayArchive"
- "kDYMessageReplayerReplayFinished"
- "kDYMessageReplayerSetBackgroundImage"
- "kDYMessageReplayerSetBackgroundImageData"
- "kDYMessageSendGuestAppToBackground"
- "kDYMessageTerminateDaemon"
- "kDYMessageTraceBufferedFstreamData"
- "kDYMessageTraceConfiguration"
- "kDYMessageTraceFlushBuffers"
- "kDYMessageTraceModeChanged"
- "kDYMessageTraceOverridesConfiguration"
- "kDYMessageUpdateResourceObject"
- "kGTMessageDiagnosticsReceivedData"
- "kGTMessageReplayerResourcesUsedForFunctionIndex"
- "kGTMessageRunnablePID"
- "library link-time versions"
- "mach absolute timestamp"
- "mach timebase denominator"
- "mach timebase numerator"
- "maxMeshBufferBindCount"
- "maxObjectBufferBindCount"
- "maxObjectThreadgroupMemoryBindCount"
- "nanoseconds since epoch timestamp"
- "override_flags"
- "override_scale_tesselation_factor"
- "pid"
- "profiling flags"
- "profiling send period"
- "queue/thread labels"
- "queues"
- "sandbox_extensions"
- "setMaxMeshBufferBindCount:"
- "setMaxObjectBufferBindCount:"
- "setMaxObjectThreadgroupMemoryBindCount:"
- "threads"
- "trace host type"
- "trace mode"
- "v16@?0@\"GTTransportMessage_capture\"8"
- "v24@?0@\"<MTLLateEvalEvent>\"8Q16"
- "warning: Cannot decode ICB mesh buffer binding, missing SPI"
- "warning: Cannot decode ICB object buffer binding, missing SPI"
- "warning: Failed to send kGTMessageGuestAppUnsupportedFenumDetected with fenum %s, error: %s"
- "warning: File %s not found\n"
- "warning: Invalid tag ID for %s, %d expected. Falling back to OS_LOG_DEFAULT"
- "warning: failed to create store0 (%s)"
- "writeToFile:atomically:"
- "🔄 Transition aborted: waiting until command buffer is scheduled"
- "🔄 Transition aborted: waiting until command buffer is scheduled\n"

```
