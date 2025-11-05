## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools`

```diff

-367.6.0.0.0
-  __TEXT.__text: 0xf3c6c
+368.11.4.0.0
+  __TEXT.__text: 0xf6970
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0xf568
-  __TEXT.__cstring: 0x25bbc
-  __TEXT.__gcc_except_tab: 0x2640
-  __TEXT.__const: 0x288
+  __TEXT.__objc_methlist: 0x14eb4
+  __TEXT.__cstring: 0x25bb0
+  __TEXT.__gcc_except_tab: 0x27b0
+  __TEXT.__const: 0x270
   __TEXT.__oslogstring: 0x280f
-  __TEXT.__unwind_info: 0x4078
+  __TEXT.__unwind_info: 0x44d8
   __TEXT.__objc_classname: 0x1cb5
-  __TEXT.__objc_methname: 0x18b11
-  __TEXT.__objc_methtype: 0x1a6cf
-  __TEXT.__objc_stubs: 0x12fc0
+  __TEXT.__objc_methname: 0x18b9f
+  __TEXT.__objc_methtype: 0x1a6f6
+  __TEXT.__objc_stubs: 0x12fe0
   __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50e8
+  __DATA_CONST.__objc_selrefs: 0x5238
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x528
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0xa70
   __AUTH_CONST.__cfstring: 0xb6e0
-  __AUTH_CONST.__objc_const: 0x45c28
+  __AUTH_CONST.__objc_const: 0x3aff0
   __AUTH.__objc_data: 0x3cf0
+  __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0xd60
+  __DATA.__objc_ivar: 0xd6c
   __DATA.__data: 0x25f0
   __DATA.__bss: 0x78
-  __DATA_DIRTY.__thread_vars: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96903DB1-40B9-33C2-8A15-5467628D2E30
-  Functions: 5874
-  Symbols:   12878
-  CStrings:  8874
+  UUID: F33F5BC7-F3F9-383B-AA7E-D0347F204287
+  Functions: 6519
+  Symbols:   13715
+  CStrings:  8878
 
Symbols:
+ -[MTLCountersCommandBuffer initWithCommandBuffer:commandQueue:descriptor:].cold.1
+ -[MTLDebugAccelerationStructure setPurgeableState:].cold.1
+ -[MTLDebugAccelerationStructure setPurgeableState:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:].cold.3
+ -[MTLDebugAccelerationStructureCommandEncoder copyAccelerationStructure:toAccelerationStructure:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder deserializeAccelerationStructure:fromBuffer:serializedBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder deserializeAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder serializeAccelerationStructure:toBuffer:serializedBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.3
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.4
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.5
+ -[MTLDebugAccelerationStructureCommandEncoder validateRefit:descriptor:destination:scratchBuffer:scratchBufferOffset:options:].cold.6
+ -[MTLDebugAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:].cold.3
+ -[MTLDebugAccelerationStructureCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:offset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:offset:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:].cold.2
+ -[MTLDebugAccelerationStructureCommandEncoder writeDeserializedPrimitiveAccelerationStructureSizes:serializedOffset:toBuffer:sizesBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:].cold.1
+ -[MTLDebugAccelerationStructureCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:].cold.2
+ -[MTLDebugBinaryArchive addComputePipelineFunctionsWithDescriptor:options:error:].cold.1
+ -[MTLDebugBinaryArchive addComputePipelineFunctionsWithDescriptor:options:error:].cold.2
+ -[MTLDebugBinaryArchive addComputePipelineFunctionsWithDescriptor:options:error:].cold.3
+ -[MTLDebugBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:options:error:].cold.1
+ -[MTLDebugBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:options:error:].cold.2
+ -[MTLDebugBinaryArchive addRenderPipelineFunctionsWithDescriptor:options:error:].cold.1
+ -[MTLDebugBinaryArchive addRenderPipelineFunctionsWithDescriptor:options:error:].cold.2
+ -[MTLDebugBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:options:error:].cold.1
+ -[MTLDebugBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:options:error:].cold.2
+ -[MTLDebugBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:options:error:].cold.3
+ -[MTLDebugBinaryArchive serializeToURL:error:].cold.1
+ -[MTLDebugBinaryArchive serializeToURL:error:].cold.2
+ -[MTLDebugBinaryArchive serializeToURL:options:error:].cold.1
+ -[MTLDebugBinaryArchive serializeToURL:options:error:].cold.2
+ -[MTLDebugBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:].cold.1
+ -[MTLDebugBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:].cold.2
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.1
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.2
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.3
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.4
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.5
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.6
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.7
+ -[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:].cold.8
+ -[MTLDebugBlitCommandEncoder endEncoding].cold.1
+ -[MTLDebugBlitCommandEncoder endEncoding].cold.2
+ -[MTLDebugBlitCommandEncoder fillBuffer:range:pattern4:].cold.1
+ -[MTLDebugBlitCommandEncoder fillBuffer:range:value:].cold.1
+ -[MTLDebugBlitCommandEncoder generateMipmapsForTexture:].cold.1
+ -[MTLDebugBlitCommandEncoder generateMipmapsForTexture:].cold.2
+ -[MTLDebugBlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:].cold.1
+ -[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.1
+ -[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.2
+ -[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.3
+ -[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.4
+ -[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.5
+ -[MTLDebugBlitCommandEncoder invalidateCompressedTexture:slice:level:].cold.1
+ -[MTLDebugBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:].cold.1
+ -[MTLDebugBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:].cold.1
+ -[MTLDebugBlitCommandEncoder pageoffTexture:slice:mipmapLevel:].cold.1
+ -[MTLDebugBlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:].cold.1
+ -[MTLDebugBlitCommandEncoder synchronizeResource:].cold.1
+ -[MTLDebugBlitCommandEncoder synchronizeTexture:slice:level:].cold.1
+ -[MTLDebugBlitCommandEncoder synchronizeTexture:slice:level:].cold.2
+ -[MTLDebugBlitCommandEncoder validateCopyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.1
+ -[MTLDebugBlitCommandEncoder validateCopyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.2
+ -[MTLDebugBlitCommandEncoder validateCopyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:].cold.3
+ -[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:].cold.1
+ -[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:].cold.2
+ -[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:].cold.3
+ -[MTLDebugBlitCommandEncoder validateTextureAccess:region:mipLevel:slice:].cold.1
+ -[MTLDebugBlitCommandEncoder validateTextureAccess:region:mipLevel:slice:].cold.2
+ -[MTLDebugBuffer detachBacking].cold.1
+ -[MTLDebugBuffer didModifyRange:].cold.1
+ -[MTLDebugBuffer makeAliasable].cold.1
+ -[MTLDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:].cold.1
+ -[MTLDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:].cold.2
+ -[MTLDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:].cold.3
+ -[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.1
+ -[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.2
+ -[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.3
+ -[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.4
+ -[MTLDebugBuffer newTiledTextureWithDescriptor:offset:bytesPerRow:].cold.1
+ -[MTLDebugBuffer newTiledTextureWithDescriptor:offset:bytesPerRow:].cold.2
+ -[MTLDebugBuffer newTiledTextureWithDescriptor:offset:bytesPerRow:].cold.3
+ -[MTLDebugBuffer newTiledTextureWithDescriptor:offset:bytesPerRow:].cold.4
+ -[MTLDebugBuffer replaceBackingWithBytesNoCopy:length:deallocator:].cold.1
+ -[MTLDebugBuffer replaceBackingWithRanges:readOnly:].cold.1
+ -[MTLDebugBuffer setPurgeableState:].cold.1
+ -[MTLDebugBuffer setPurgeableState:].cold.2
+ -[MTLDebugCommandBuffer accelerationStructureCommandEncoder].cold.1
+ -[MTLDebugCommandBuffer addCompletedHandler:].cold.1
+ -[MTLDebugCommandBuffer addScheduledHandler:].cold.1
+ -[MTLDebugCommandBuffer blitCommandEncoder].cold.1
+ -[MTLDebugCommandBuffer commitWithDeadline:].cold.1
+ -[MTLDebugCommandBuffer commitWithDeadline:].cold.2
+ -[MTLDebugCommandBuffer computeCommandEncoderWithDispatchType:].cold.1
+ -[MTLDebugCommandBuffer computeCommandEncoder].cold.1
+ -[MTLDebugCommandBuffer encodeSignalEvent:value:].cold.1
+ -[MTLDebugCommandBuffer encodeWaitForEvent:value:].cold.1
+ -[MTLDebugCommandBuffer encodeWaitForEvent:value:timeout:].cold.1
+ -[MTLDebugCommandBuffer lockPurgeableObjects].cold.1
+ -[MTLDebugCommandBuffer preCommit].cold.1
+ -[MTLDebugCommandBuffer resourceStateCommandEncoder].cold.1
+ -[MTLDebugCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:].cold.1
+ -[MTLDebugCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:].cold.1
+ -[MTLDebugCommandBuffer useInternalResidencySet:].cold.1
+ -[MTLDebugCommandBuffer useInternalResidencySets:count:].cold.1
+ -[MTLDebugCommandBuffer useResidencySet:].cold.1
+ -[MTLDebugCommandBuffer useResidencySets:count:].cold.1
+ -[MTLDebugCommandBuffer videoCommandEncoder].cold.1
+ -[MTLDebugCommandBuffer waitUntilCompleted].cold.1
+ -[MTLDebugCommandBuffer waitUntilScheduled].cold.1
+ -[MTLDebugCommandQueue addInternalResidencySet:].cold.1
+ -[MTLDebugCommandQueue addInternalResidencySets:count:].cold.1
+ -[MTLDebugCommandQueue addResidencySet:].cold.1
+ -[MTLDebugCommandQueue addResidencySets:count:].cold.1
+ -[MTLDebugCommandQueue insertDebugCaptureBoundary].cold.1
+ -[MTLDebugCommandQueue removeInternalResidencySet:].cold.1
+ -[MTLDebugCommandQueue removeInternalResidencySets:count:].cold.1
+ -[MTLDebugCommandQueue removeResidencySet:].cold.1
+ -[MTLDebugCommandQueue removeResidencySets:count:].cold.1
+ -[MTLDebugCommandQueue validateDeadlineAwareness:].cold.1
+ -[MTLDebugCommandQueue validateDeadlineAwareness:].cold.2
+ -[MTLDebugComputeCommandEncoder _validateThreadsPerThreadgroup:].cold.1
+ -[MTLDebugComputeCommandEncoder _validateThreadsPerThreadgroup:].cold.2
+ -[MTLDebugComputeCommandEncoder _validateThreadsPerThreadgroup:].cold.3
+ -[MTLDebugComputeCommandEncoder _validateThreadsPerThreadgroup:].cold.4
+ -[MTLDebugComputeCommandEncoder beginVirtualSubstream].cold.1
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:].cold.1
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:].cold.2
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:].cold.3
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:].cold.4
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:].cold.5
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.1
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.2
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.3
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.4
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.5
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.6
+ -[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:].cold.7
+ -[MTLDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:].cold.1
+ -[MTLDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:].cold.2
+ -[MTLDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:].cold.3
+ -[MTLDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:].cold.4
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.1
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.2
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.3
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.4
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.5
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.6
+ -[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:].cold.7
+ -[MTLDebugComputeCommandEncoder endEncoding_private].cold.1
+ -[MTLDebugComputeCommandEncoder endEncoding_private].cold.2
+ -[MTLDebugComputeCommandEncoder endVirtualSubstream].cold.1
+ -[MTLDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:].cold.1
+ -[MTLDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:].cold.2
+ -[MTLDebugComputeCommandEncoder executeCommandsInBuffer:withRange:].cold.1
+ -[MTLDebugComputeCommandEncoder executeCommandsInBuffer:withRange:].cold.2
+ -[MTLDebugComputeCommandEncoder memoryBarrierWithResources:count:].cold.1
+ -[MTLDebugComputeCommandEncoder memoryBarrierWithScope:].cold.1
+ -[MTLDebugComputeCommandEncoder nextVirtualSubstream].cold.1
+ -[MTLDebugComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:].cold.1
+ -[MTLDebugComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:].cold.2
+ -[MTLDebugComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:].cold.3
+ -[MTLDebugComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:].cold.4
+ -[MTLDebugComputeCommandEncoder setAccelerationStructure:atBufferIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setAccelerationStructure:atBufferIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setAccelerationStructure:atBufferIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.6
+ -[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:].cold.7
+ -[MTLDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:].cold.6
+ -[MTLDebugComputeCommandEncoder setBytes:length:attributeStride:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setBytes:length:attributeStride:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setBytes:length:attributeStride:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.1
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.2
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.3
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.4
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.5
+ -[MTLDebugComputeCommandEncoder setComputePipelineState:].cold.6
+ -[MTLDebugComputeCommandEncoder setImageblockWidth:height:].cold.1
+ -[MTLDebugComputeCommandEncoder setImageblockWidth:height:].cold.2
+ -[MTLDebugComputeCommandEncoder setImageblockWidth:height:].cold.3
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setSamplerState:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setSamplerState:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setSamplerState:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setSamplerState:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setSamplerState:atIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setSamplerStates:withRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setSamplerStates:withRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setSamplerStates:withRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setSamplerStates:withRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setSamplerStates:withRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:].cold.1
+ -[MTLDebugComputeCommandEncoder setSubstream:].cold.1
+ -[MTLDebugComputeCommandEncoder setSubstream:].cold.2
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.6
+ -[MTLDebugComputeCommandEncoder setTexture:atIndex:].cold.7
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.6
+ -[MTLDebugComputeCommandEncoder setTextures:withRange:].cold.7
+ -[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.1
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.2
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.3
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.4
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.5
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:].cold.6
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.1
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.2
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.3
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.4
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.5
+ -[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:].cold.6
+ -[MTLDebugComputeCommandEncoder signalProgress:].cold.1
+ -[MTLDebugComputeCommandEncoder signalProgress:].cold.2
+ -[MTLDebugComputeCommandEncoder signalProgress:].cold.3
+ -[MTLDebugComputeCommandEncoder useHeap:].cold.1
+ -[MTLDebugComputeCommandEncoder useResidencySet:].cold.1
+ -[MTLDebugComputeCommandEncoder useResidencySets:count:].cold.1
+ -[MTLDebugComputeCommandEncoder useResource:usage:].cold.1
+ -[MTLDebugComputeCommandEncoder useResource:usage:].cold.2
+ -[MTLDebugComputeCommandEncoder useResource:usage:].cold.3
+ -[MTLDebugComputeCommandEncoder useResources:count:usage:].cold.1
+ -[MTLDebugComputeCommandEncoder validateFunctionTableUseResource:selectorName:].cold.1
+ -[MTLDebugComputeCommandEncoder waitForProgress:].cold.1
+ -[MTLDebugComputeCommandEncoder waitForProgress:].cold.2
+ -[MTLDebugComputeCommandEncoder waitForVirtualSubstream:].cold.1
+ -[MTLDebugComputeCommandEncoder waitForVirtualSubstream:].cold.2
+ -[MTLDebugComputePipelineState functionHandleWithFunction:].cold.1
+ -[MTLDebugComputePipelineState functionHandleWithFunction:].cold.2
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:].cold.1
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:].cold.2
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:].cold.3
+ -[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:].cold.4
+ -[MTLDebugComputePipelineState newIntersectionFunctionTableWithDescriptor:].cold.1
+ -[MTLDebugComputePipelineState newIntersectionFunctionTableWithDescriptor:].cold.2
+ -[MTLDebugComputePipelineState newVisibleFunctionTableWithDescriptor:].cold.1
+ -[MTLDebugComputePipelineState newVisibleFunctionTableWithDescriptor:].cold.2
+ -[MTLDebugComputePipelineState newVisibleFunctionTableWithDescriptor:].cold.3
+ -[MTLDebugComputePipelineState validateHandleForSetFunction:].cold.1
+ -[MTLDebugCounterSampleBuffer resolveCounterRange:].cold.1
+ -[MTLDebugCounterSampleBuffer resolveCounterRange:].cold.2
+ -[MTLDebugDeadlineProfile validateCommandQueue:].cold.1
+ -[MTLDebugDevice _newComputePipelineStateWithDescriptor:options:completionHandler:].cold.1
+ -[MTLDebugDevice _newComputePipelineStateWithDescriptor:options:completionHandler:].cold.2
+ -[MTLDebugDevice deserializeInstanceAccelerationStructure:fromBytes:primitiveAccelerationStructures:withDescriptor:].cold.1
+ -[MTLDebugDevice deserializeInstanceAccelerationStructure:fromBytes:primitiveAccelerationStructures:withDescriptor:].cold.2
+ -[MTLDebugDevice deserializeInstanceAccelerationStructureFromBytes:primitiveAccelerationStructures:withDescriptor:].cold.1
+ -[MTLDebugDevice deserializePrimitiveAccelerationStructure:fromBytes:withDescriptor:].cold.1
+ -[MTLDebugDevice deserializePrimitiveAccelerationStructure:fromBytes:withDescriptor:].cold.2
+ -[MTLDebugDevice deserializePrimitiveAccelerationStructureFromBytes:withDescriptor:].cold.1
+ -[MTLDebugDevice heapTextureSizeAndAlignWithDescriptor:].cold.1
+ -[MTLDebugDevice heapTextureSizeAndAlignWithDescriptor:].cold.2
+ -[MTLDebugDevice initWithBaseObject:parent:].cold.1
+ -[MTLDebugDevice minimumLinearTextureAlignmentForPixelFormat:].cold.1
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:].cold.1
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:].cold.2
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:].cold.3
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:].cold.4
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:resourceIndex:].cold.1
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:resourceIndex:].cold.2
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:resourceIndex:].cold.3
+ -[MTLDebugDevice newAccelerationStructureWithBuffer:offset:resourceIndex:].cold.4
+ -[MTLDebugDevice newBinaryLibraryWithOptions:url:error:].cold.1
+ -[MTLDebugDevice newBufferWithIOSurface:].cold.1
+ -[MTLDebugDevice newCounterSampleBufferWithDescriptor:error:].cold.1
+ -[MTLDebugDevice newCounterSampleBufferWithDescriptor:error:].cold.2
+ -[MTLDebugDevice newDepthStencilStateWithDescriptor:].cold.1
+ -[MTLDebugDevice newDepthStencilStateWithDescriptor:].cold.2
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.1
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.2
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.3
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.4
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.5
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.6
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.7
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.8
+ -[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:].cold.9
+ -[MTLDebugDevice newIntersectionFunctionTableWithDescriptor:].cold.1
+ -[MTLDebugDevice newIntersectionFunctionTableWithDescriptor:].cold.2
+ -[MTLDebugDevice newLibraryWithData:error:].cold.1
+ -[MTLDebugDevice newLibraryWithFile:error:].cold.1
+ -[MTLDebugDevice newLibraryWithFile:error:].cold.2
+ -[MTLDebugDevice newLibraryWithURL:error:].cold.1
+ -[MTLDebugDevice newLibraryWithURL:error:].cold.2
+ -[MTLDebugDevice newLibraryWithURL:error:].cold.3
+ -[MTLDebugDevice newMotionEstimationPipelineWithDescriptor:].cold.1
+ -[MTLDebugDevice newMotionEstimationPipelineWithDescriptor:].cold.2
+ -[MTLDebugDevice newMotionEstimationPipelineWithDescriptor:].cold.3
+ -[MTLDebugDevice newMotionEstimationPipelineWithDescriptor:].cold.4
+ -[MTLDebugDevice newPipelineLibraryWithFilePath:error:].cold.1
+ -[MTLDebugDevice newPipelineLibraryWithFilePath:error:].cold.2
+ -[MTLDebugDevice newResidencySetWithDescriptor:error:].cold.1
+ -[MTLDebugDevice newSamplerStateWithDescriptor:].cold.1
+ -[MTLDebugDevice newSamplerStateWithDescriptor:].cold.2
+ -[MTLDebugDevice newVisibleFunctionTableWithDescriptor:].cold.1
+ -[MTLDebugDevice newVisibleFunctionTableWithDescriptor:].cold.2
+ -[MTLDebugDevice relaxedTextureArrayBindingsEnabled]
+ -[MTLDebugDevice validateDynamicLibrary:state:error:].cold.1
+ -[MTLDebugDevice validateDynamicLibraryURL:error:].cold.1
+ -[MTLDebugDevice validateLinkedFunctions:context:].cold.1
+ -[MTLDebugDevice validateRaytracing].cold.1
+ -[MTLDebugDevice writeMeshShaderEmulatorDataStructureHeader:meshShaderPSO:scalingFactor:].cold.1
+ -[MTLDebugDevice writeMeshShaderEmulatorDataStructureHeader:meshShaderPSO:scalingFactor:].cold.2
+ -[MTLDebugDevice writeMeshShaderEmulatorDataStructureHeader:meshShaderPSO:scalingFactor:].cold.3
+ -[MTLDebugDynamicLibrary serializeToURL:error:].cold.1
+ -[MTLDebugDynamicLibrary serializeToURL:error:].cold.2
+ -[MTLDebugDynamicLibrary serializeToURL:options:error:].cold.1
+ -[MTLDebugDynamicLibrary serializeToURL:options:error:].cold.2
+ -[MTLDebugHeap detachBacking].cold.1
+ -[MTLDebugHeap maxAvailableSizeWithAlignment:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithDescriptor:offset:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithSize:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithSize:].cold.2
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:].cold.2
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:].cold.3
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:resourceIndex:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:resourceIndex:].cold.2
+ -[MTLDebugHeap newAccelerationStructureWithSize:offset:resourceIndex:].cold.3
+ -[MTLDebugHeap newAccelerationStructureWithSize:resourceIndex:].cold.1
+ -[MTLDebugHeap newAccelerationStructureWithSize:resourceIndex:].cold.2
+ -[MTLDebugHeap newBufferWithLength:options:].cold.1
+ -[MTLDebugHeap newBufferWithLength:options:offset:].cold.1
+ -[MTLDebugHeap replaceBackingWithRanges:readOnly:].cold.1
+ -[MTLDebugHeap setPurgeableState:].cold.1
+ -[MTLDebugHeap validateRaytracingHeap].cold.1
+ -[MTLDebugHeap validateRaytracingHeap].cold.2
+ -[MTLDebugIOCommandBuffer addCompletedHandler:].cold.1
+ -[MTLDebugIOCommandBuffer internalValidateLoadBuffer:offset:size:sourceHandle:sourceHandleOffset:].cold.1
+ -[MTLDebugIOCommandBuffer internalValidateLoadBuffer:offset:size:sourceHandle:sourceHandleOffset:].cold.2
+ -[MTLDebugIOCommandBuffer internalValidateLoadBytes:size:sourceHandle:sourceHandleOffset:].cold.1
+ -[MTLDebugIOCommandBuffer internalValidateLoadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:].cold.1
+ -[MTLDebugIOCommandBuffer internalValidateLoadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:].cold.2
+ -[MTLDebugIndirectCommandBuffer indirectComputeCommandAtIndex:].cold.1
+ -[MTLDebugIndirectCommandBuffer indirectComputeCommandAtIndex:].cold.2
+ -[MTLDebugIndirectCommandBuffer indirectRenderCommandAtIndex:].cold.1
+ -[MTLDebugIndirectCommandBuffer indirectRenderCommandAtIndex:].cold.2
+ -[MTLDebugIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:].cold.1
+ -[MTLDebugIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:].cold.1
+ -[MTLDebugIndirectComputeCommand setComputePipelineState:].cold.1
+ -[MTLDebugIndirectComputeCommand setComputePipelineState:].cold.2
+ -[MTLDebugIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:].cold.1
+ -[MTLDebugIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:].cold.2
+ -[MTLDebugIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:].cold.3
+ -[MTLDebugIndirectComputeCommand setThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTLDebugIndirectRenderCommand clearBarrier].cold.1
+ -[MTLDebugIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:].cold.1
+ -[MTLDebugIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:].cold.1
+ -[MTLDebugIndirectRenderCommand setBarrier].cold.1
+ -[MTLDebugIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTLDebugIntersectionFunctionTable setFunction:atIndex:].cold.1
+ -[MTLDebugIntersectionFunctionTable setFunction:atIndex:].cold.2
+ -[MTLDebugIntersectionFunctionTable setPurgeableState:].cold.1
+ -[MTLDebugIntersectionFunctionTable setPurgeableState:].cold.2
+ -[MTLDebugLibrary newFunctionWithName:].cold.1
+ -[MTLDebugLibrary newFunctionWithName:].cold.2
+ -[MTLDebugLibrary validateDescriptor:expectedClass:].cold.1
+ -[MTLDebugLibrary validateDescriptor:expectedClass:].cold.2
+ -[MTLDebugLibrary validateDescriptor:expectedClass:].cold.3
+ -[MTLDebugParallelRenderCommandEncoder endEncoding_private].cold.1
+ -[MTLDebugParallelRenderCommandEncoder endEncoding_private].cold.2
+ -[MTLDebugParallelRenderCommandEncoder endEncoding_private].cold.3
+ -[MTLDebugParallelRenderCommandEncoder endEncoding_private].cold.4
+ -[MTLDebugParallelRenderCommandEncoder setColorStoreAction:atIndex:].cold.1
+ -[MTLDebugParallelRenderCommandEncoder setColorStoreActionOptions:atIndex:].cold.1
+ -[MTLDebugPipelineLibrary newComputePipelineStateWithName:options:reflection:error:].cold.1
+ -[MTLDebugPipelineLibrary newComputePipelineStateWithName:options:reflection:error:].cold.2
+ -[MTLDebugPipelineLibrary newRenderPipelineStateWithName:options:reflection:error:].cold.1
+ -[MTLDebugPipelineLibrary newRenderPipelineStateWithName:options:reflection:error:].cold.2
+ -[MTLDebugRenderCommandEncoder _validateDispatchThreadsPerTile:context:].cold.1
+ -[MTLDebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:].cold.1
+ -[MTLDebugRenderCommandEncoder setAccelerationStructure:atBufferIndex:maxBuffers:buffers:buffersLength:stage:].cold.1
+ -[MTLDebugRenderCommandEncoder setColorResolveTexture:slice:depthPlane:level:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setDepthStoreAction:].cold.1
+ -[MTLDebugRenderCommandEncoder setDepthStoreActionOptions:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentBuffer:offset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentBufferOffset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentBuffers:offsets:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentSamplerState:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentSamplerStates:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentTexture:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentTexture:atTextureIndex:samplerState:atSamplerIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setFragmentTexture:atTextureIndex:samplerState:atSamplerIndex:].cold.2
+ -[MTLDebugRenderCommandEncoder setFragmentTextures:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setIntersectionFunctionTable:atBufferIndex:maxBuffers:buffers:buffersLength:stage:].cold.1
+ -[MTLDebugRenderCommandEncoder setIntersectionFunctionTable:atBufferIndex:maxBuffers:buffers:buffersLength:stage:].cold.2
+ -[MTLDebugRenderCommandEncoder setIntersectionFunctionTables:withBufferRange:maxBuffers:buffers:buffersLength:stage:].cold.1
+ -[MTLDebugRenderCommandEncoder setIntersectionFunctionTables:withBufferRange:maxBuffers:buffers:buffersLength:stage:].cold.2
+ -[MTLDebugRenderCommandEncoder setMeshBuffer:offset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshBufferOffset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshBuffers:offsets:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshSamplerState:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshSamplerStates:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshTexture:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setMeshTextures:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectBuffer:offset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectBufferOffset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectBuffers:offsets:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectSamplerState:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectSamplerStates:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectTexture:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectTextures:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setRenderPipelineState:].cold.1
+ -[MTLDebugRenderCommandEncoder setStencilStoreAction:].cold.1
+ -[MTLDebugRenderCommandEncoder setStencilStoreActionOptions:].cold.1
+ -[MTLDebugRenderCommandEncoder setTessellationFactorBuffer:offset:instanceStride:].cold.1
+ -[MTLDebugRenderCommandEncoder setTessellationFactorScale:].cold.1
+ -[MTLDebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileBuffer:offset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileBufferOffset:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileBuffers:offsets:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileSamplerState:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileSamplerStates:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileTexture:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setTileTextures:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexBuffer:offset:attributeStride:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexBufferOffset:attributeStride:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexBuffers:offsets:attributeStrides:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexSamplerState:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexSamplerStates:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexTexture:atIndex:].cold.1
+ -[MTLDebugRenderCommandEncoder setVertexTextures:withRange:].cold.1
+ -[MTLDebugRenderCommandEncoder setVisibleFunctionTable:atBufferIndex:maxBuffers:buffers:buffersLength:stage:].cold.1
+ -[MTLDebugRenderCommandEncoder setVisibleFunctionTables:withBufferRange:maxBuffers:buffers:buffersLength:stage:].cold.1
+ -[MTLDebugRenderCommandEncoder setVisibleFunctionTables:withBufferRange:maxBuffers:buffers:buffersLength:stage:].cold.2
+ -[MTLDebugRenderCommandEncoder updateFence:afterStages:].cold.1
+ -[MTLDebugRenderCommandEncoder useHeap:].cold.1
+ -[MTLDebugRenderCommandEncoder useResidencySet:].cold.1
+ -[MTLDebugRenderCommandEncoder useResidencySets:count:].cold.1
+ -[MTLDebugRenderCommandEncoder validateFunctionTableUseResource:stages:context:selectorName:].cold.1
+ -[MTLDebugRenderCommandEncoder waitForFence:beforeStages:].cold.1
+ -[MTLDebugRenderPipelineState functionHandleWithFunction:stage:].cold.1
+ -[MTLDebugRenderPipelineState functionHandleWithFunction:stage:].cold.2
+ -[MTLDebugRenderPipelineState functionHandleWithFunction:stage:selector:].cold.1
+ -[MTLDebugRenderPipelineState functionHandleWithFunction:stage:selector:].cold.2
+ -[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:].cold.1
+ -[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:].cold.2
+ -[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:withStage:selector:].cold.1
+ -[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:withStage:selector:].cold.2
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.1
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.2
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.3
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.4
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.5
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.6
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:].cold.1
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:].cold.2
+ -[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:].cold.3
+ -[MTLDebugRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.1
+ -[MTLDebugRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:].cold.2
+ -[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:].cold.1
+ -[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:].cold.2
+ -[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:selector:].cold.1
+ -[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:selector:].cold.2
+ -[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:selector:].cold.3
+ -[MTLDebugRenderPipelineState validateBinaryFunctions:stage:].cold.1
+ -[MTLDebugRenderPipelineState validateBinaryFunctions:stage:].cold.2
+ -[MTLDebugRenderPipelineState validateHandleForSetFunction:].cold.1
+ -[MTLDebugResidencySet validateHeap:].cold.1
+ -[MTLDebugResidencySet validateResource:].cold.1
+ -[MTLDebugResidencySet validateResource:].cold.2
+ -[MTLDebugResourceStateCommandEncoder endEncoding].cold.1
+ -[MTLDebugResourceStateCommandEncoder endEncoding].cold.2
+ -[MTLDebugResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.1
+ -[MTLDebugResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.2
+ -[MTLDebugResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:].cold.3
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:].cold.1
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:].cold.2
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:].cold.1
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:].cold.2
+ -[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:].cold.3
+ -[MTLDebugResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:].cold.1
+ -[MTLDebugResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:].cold.2
+ -[MTLDebugResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:].cold.3
+ -[MTLDebugResourceStateCommandEncoder validateSparseTextureMappingMode:].cold.1
+ -[MTLDebugResourceStateCommandEncoder validateTextureAccess:region:mipLevel:slice:].cold.1
+ -[MTLDebugResourceStateCommandEncoder validateTextureAccess:region:mipLevel:slice:].cold.2
+ -[MTLDebugResourceStateCommandEncoder validateTextureAccess:region:mipLevel:slice:].cold.3
+ -[MTLDebugTexture dealloc].cold.1
+ -[MTLDebugTexture makeAliasable].cold.1
+ -[MTLDebugTexture makeAliasable].cold.2
+ -[MTLDebugTexture makeAliasable].cold.3
+ -[MTLDebugTexture makeAliasable].cold.4
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.1
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.10
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.11
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.12
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.13
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.14
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.15
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.16
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.17
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.18
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.19
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.2
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.20
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.21
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.22
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.3
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.4
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.5
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.6
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.7
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.8
+ -[MTLDebugVideoCommandEncoder generateMotionVectorsForTexture:previousTexture:resultBuffer:bufferOffset:].cold.9
+ -[MTLDebugVisibleFunctionTable setFunction:atIndex:].cold.1
+ -[MTLDebugVisibleFunctionTable setFunction:atIndex:].cold.2
+ -[MTLDebugVisibleFunctionTable setFunction:atIndex:].cold.3
+ -[MTLDebugVisibleFunctionTable setFunctions:withRange:].cold.1
+ -[MTLDebugVisibleFunctionTable setPurgeableState:].cold.1
+ -[MTLDebugVisibleFunctionTable setPurgeableState:].cold.2
+ -[MTLGPUDebugDevice dealloc].cold.2
+ -[MTLGPUDebugDevice initWithBaseObject:parent:].cold.4
+ -[MTLGPUDebugDevice initWithBaseObject:parent:].cold.5
+ -[MTLGPUDebugDevice initWithBaseObject:parent:].cold.6
+ -[MTLGPUDebugDevice validateRaytracing].cold.1
+ -[MTLLegacySVDevice dealloc].cold.2
+ -[MTLLegacySVDevice initWithBaseObject:parent:].cold.4
+ -[MTLLegacySVDevice initWithBaseObject:parent:].cold.5
+ -[MTLLegacySVDevice initWithBaseObject:parent:].cold.6
+ -[MTLLegacySVDevice validateRaytracing].cold.1
+ -[MTLTelemetryCommandBuffer postCompletionHandlers].cold.1
+ -[MTLToolsDevice unwrapMTLCommandBufferDescriptor:alwaysCopy:].cold.1
+ GCC_except_table210
+ GCC_except_table214
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table53
+ OBJC_IVAR_$_MTLDebugDevice._relaxedTextureArrayBindingsEnabled
+ OBJC_IVAR_$_MTLToolsResidencySet._pendingAdds
+ OBJC_IVAR_$_MTLToolsResidencySet._pendingRemoves
+ _MTLDebugValidateDeferredStoreActionOnDevice.cold.1
+ _MTLValidateDepthStencilStoreState.cold.1
+ _MTLValidateDepthStencilStoreState.cold.2
+ _MTLValidateDepthStencilStoreStateWithContext.cold.1
+ _MTLValidateResolveTexture.cold.1
+ _MTLValidateResolveTexture.cold.10
+ _MTLValidateResolveTexture.cold.11
+ _MTLValidateResolveTexture.cold.12
+ _MTLValidateResolveTexture.cold.13
+ _MTLValidateResolveTexture.cold.2
+ _MTLValidateResolveTexture.cold.3
+ _MTLValidateResolveTexture.cold.4
+ _MTLValidateResolveTexture.cold.5
+ _MTLValidateResolveTexture.cold.6
+ _MTLValidateResolveTexture.cold.7
+ _MTLValidateResolveTexture.cold.8
+ _MTLValidateResolveTexture.cold.9
+ _MTLValidateResolveTextureWithContext.cold.1
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _Z11checkBufferPU19objcproto9MTLDevice11objc_objectPU19objcproto9MTLBuffer11objc_objectmbP8NSString.cold.1
+ _Z11checkBufferPU19objcproto9MTLDevice11objc_objectPU19objcproto9MTLBuffer11objc_objectmbP8NSString.cold.2
+ _Z14MTLGPUDebugLogv.cold.1
+ _Z14MTLLegacySVLogv.cold.1
+ _Z15checkCurveBasis13MTLCurveBasism.cold.1
+ _Z15checkCurveBasis13MTLCurveBasism.cold.2
+ _Z15checkCurveBasis13MTLCurveBasism.cold.3
+ _Z15checkCurveBasis13MTLCurveBasism.cold.4
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.1
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.2
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.3
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.4
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.5
+ _Z18checkPrimitiveDataPU19objcproto9MTLDevice11objc_objectP42MTLAccelerationStructureGeometryDescriptorm.cold.6
+ _Z18newArgumentEncoderP16MTLDebugFunctionmPP11MTLArgumentPU29objcproto18MTLPipelineLibrary11objc_objectP7NSArrayIPU27objcproto16MTLBinaryArchive11objc_objectE.cold.1
+ _Z18newArgumentEncoderP16MTLDebugFunctionmPP11MTLArgumentPU29objcproto18MTLPipelineLibrary11objc_objectP7NSArrayIPU27objcproto16MTLBinaryArchive11objc_objectE.cold.2
+ _Z20checkMotionParameterPU19objcproto9MTLDevice11objc_objectP43MTLPrimitiveAccelerationStructureDescriptor.cold.1
+ _Z20checkMotionParameterPU19objcproto9MTLDevice11objc_objectP43MTLPrimitiveAccelerationStructureDescriptor.cold.2
+ _Z37validateSharedTextureHandleWithDeviceP22MTLSharedTextureHandlePU23objcproto12MTLDeviceSPI11objc_object.cold.1
+ _Z37validateSharedTextureHandleWithDeviceP22MTLSharedTextureHandlePU23objcproto12MTLDeviceSPI11objc_object.cold.2
+ _Z37validateSharedTextureHandleWithDeviceP22MTLSharedTextureHandlePU23objcproto12MTLDeviceSPI11objc_object.cold.3
+ _Z37validateSharedTextureHandleWithDeviceP22MTLSharedTextureHandlePU23objcproto12MTLDeviceSPI11objc_object.cold.4
+ _Z40validateNewFunctionWithConstantArgumentsP8NSStringP25MTLFunctionConstantValues.cold.1
+ _Z40validateNewFunctionWithConstantArgumentsP8NSStringP25MTLFunctionConstantValues.cold.2
+ _Z40validateNewFunctionWithConstantArgumentsP8NSStringP25MTLFunctionConstantValues.cold.3
+ _ZL17_validateGetBytesP15MTLDebugTexture9MTLOrigin7MTLSizemmPvmbmm.cold.1
+ _ZL17_validateGetBytesP15MTLDebugTexture9MTLOrigin7MTLSizemmPvmbmm.cold.2
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.1
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.10
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.2
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.3
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.4
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.5
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.6
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.7
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.8
+ _ZL18validateNewTextureP14MTLDebugBufferP20MTLTextureDescriptormmjjb.cold.9
+ _ZL20_validateTextureViewP15MTLDebugTexture14MTLPixelFormat14MTLTextureType.cold.1
+ _ZL21validateTextureRegionP14MTLToolsDevicePU21objcproto10MTLTexture11objc_objectmmRK9MTLRegion.cold.1
+ _ZL22_validateReplaceRegionP15MTLDebugTexture9MTLOrigin7MTLSizemmPKvmbmm.cold.1
+ _ZL22_validateReplaceRegionP15MTLDebugTexture9MTLOrigin7MTLSizemmPKvmbmm.cold.2
+ _ZL25validateFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_mP43MTLRenderPassColorAttachmentDescriptorArrayP47MTLRenderPipelineColorAttachmentDescriptorArraymP25MTLDepthStencilDescriptorP12NSMutableSetIP34MTLDebugRenderTargetAttachmentInfoEyS6_mbPKbP18_MTLMessageContextb.cold.1
+ _ZL26LogInstrumentationFailuresP20MTLGPUDebugImageDataP27MTLDebugInstrumentationData.cold.1
+ _ZL26LogInstrumentationFailuresP20MTLGPUDebugImageDataP27MTLDebugInstrumentationData.cold.2
+ _ZL26LogInstrumentationFailuresP20MTLLegacySVImageDataP27MTLDebugInstrumentationData.cold.1
+ _ZL26LogInstrumentationFailuresP20MTLLegacySVImageDataP27MTLDebugInstrumentationData.cold.2
+ _ZL26MTLGPUDebugParsePerPSOListRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.cold.2
+ _ZL26MTLLegacySVParsePerPSOListRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE.cold.2
+ _ZL26validateAttachmentOnDevicePU19objcproto9MTLDevice11objc_objectPK40MTLRenderPassAttachmentDescriptorPrivate29_MTLRenderPassAttachmentIndexPmmRbS6_bS6_P18_MTLMessageContext.cold.1
+ _ZL26validateAttachmentOnDevicePU19objcproto9MTLDevice11objc_objectPK40MTLRenderPassAttachmentDescriptorPrivate29_MTLRenderPassAttachmentIndexPmmRbS6_bS6_P18_MTLMessageContext.cold.2
+ _ZL26validateAttachmentOnDevicePU19objcproto9MTLDevice11objc_objectPK40MTLRenderPassAttachmentDescriptorPrivate29_MTLRenderPassAttachmentIndexPmmRbS6_bS6_P18_MTLMessageContext.cold.3
+ _ZL27validateStoreLoadTransitioniRNSt3__118unordered_multisetI26AttachmentDescriptorSimpleNS1_6hash_tENS1_7equal_tENS_9allocatorIS1_EEEEPK40MTLRenderPassAttachmentDescriptorPrivateRNS_5arrayIS1_Lm8EEESD_m.cold.1
+ _ZL27validateStoreLoadTransitioniRNSt3__118unordered_multisetI26AttachmentDescriptorSimpleNS1_6hash_tENS1_7equal_tENS_9allocatorIS1_EEEEPK40MTLRenderPassAttachmentDescriptorPrivateRNS_5arrayIS1_Lm8EEESD_m.cold.2
+ _ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.1
+ _ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.2
+ _ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.3
+ _ZL37MTLGPUDebugSetValidationChecksOptionsP17MTLGPUDebugDevicePU22objcproto11MTLFunction11objc_objectS2_S2_P8NSString19MTLShaderValidationS5_Rm.cold.2
+ _ZL37MTLLegacySVSetValidationChecksOptionsP17MTLLegacySVDevicePU22objcproto11MTLFunction11objc_objectS2_S2_P8NSString19MTLShaderValidationS5_Rm.cold.2
+ _ZN15MetalBufferHeap11allocBufferEv.cold.2
+ _ZN15MetalBufferHeap4growEj.cold.2
+ _ZN23LegacySVMetalBufferHeap11allocBufferEv.cold.2
+ _ZN23LegacySVMetalBufferHeap4growEj.cold.2
+ _ZN27GPUDebugConstantBufferCache17getOrCreateBufferEP6NSData.cold.2
+ _ZN27LegacySVConstantBufferCache17getOrCreateBufferEP6NSData.cold.2
+ _ZN27MTLSamplerDescriptorHashMap3addEP20MTLSamplerDescriptor.cold.1
+ _ZN28GPUDebugBufferDescriptorHeap12createHandleEP17MTLGPUDebugBuffer.cold.2
+ _ZN28GPUDebugBufferDescriptorHeap4initEP17MTLGPUDebugDevicej.cold.2
+ _ZN28LegacySVBufferDescriptorHeap12createHandleEP17MTLLegacySVBuffer.cold.2
+ _ZN28LegacySVBufferDescriptorHeap4initEP17MTLLegacySVDevicej.cold.2
+ __MergedGlobals
+ __ZL29stringifyMTLTelemetryBlitType20MTLTelemetryBlitType
+ __ZL32MTLTelemetryStringifyTextureType14MTLTextureType
+ __ZL32stringifyMTLTelemetryCompareFunc18MTLCompareFunction
+ __ZL33_MTLTelemetryStringifyTextureType14MTLTextureType
+ __ZN24resolvedSharedPacketDataI19GPUDebugStackPacketE21setPipelineIdentifierEP8NSString
+ __ZN24resolvedSharedPacketDataI23GPUDebugBadAccessPacketE21setPipelineIdentifierEP8NSString
+ __ZN24resolvedSharedPacketDataI24GPUDebugBadTexturePacketE21setPipelineIdentifierEP8NSString
+ __ZN24resolvedSharedPacketDataI26GPUDebugFunctionTrapPacketE21setPipelineIdentifierEP8NSString
+ __ZN24resolvedSharedPacketDataI35GPUDebugAccelerationStructurePacketE21setPipelineIdentifierEP8NSString
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne190102EPKvm
+ __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNKSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNKSt3__16vectorI19LegacySVMetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN12_GLOBAL__N_112_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN12_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN12_GLOBAL__N_117ReportBufferEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIP6NSDatamEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIj14MTLTextureTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP15MTLStructMemberNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP17MTLGPUDebugBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP17MTLLegacySVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrI29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI29LegacySVArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29LegacySVArgumentEncoderLayoutNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImN12_GLOBAL__N_120EncoderResourceUsageEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B8ne190102Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS3_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_prepareB8ne190102EmRS3_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne190102EmRS4_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS4_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne190102EmRS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__113unordered_mapIPU24objcproto13MTLAllocation11objc_objectN12_GLOBAL__N_154_MTLToolsResidencySetInternalCommittedAllocationsTable24CommittedAllocationEntryENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S5_EEEEE4findB8ne190102ERSC_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne190102Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL23instrumentationHeapInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL23instrumentationHeapInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11MTLViewportEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11MetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI14MTLScissorRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19LegacySVMetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI9MemberRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIP6NSDatamEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIj14MTLTextureTypeEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15MTLStructMemberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP16MTLDebugLocationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17MTLGPUDebugBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP17MTLLegacySVBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU17objcproto7MTLHeap11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU21objcproto10MTLTexture11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU22objcproto11MTLResource11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU24objcproto13MTLAllocation11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU26objcproto15MTLResidencySet11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU26objcproto15MTLSamplerState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU28objcproto17MTLFunctionHandle11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU33objcproto22MTLRenderPipelineState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU34objcproto23MTLVisibleFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne190102EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26MTLTelemetryStatisticUIRecEEPvEEEEEclB8ne190102EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPKcEEPvEEEEEclB8ne190102EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__15dequeIP11objc_objectNS_9allocatorIS2_EEED2B8ne190102Ev
+ __ZNSt3__16removeB8ne190102INS_11__wrap_iterIPjEEjEET_S4_S4_RKT0_
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPKS1_S7_EEvT_T0_l
+ __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
+ __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B8ne190102Em
+ __ZNSt3__17getlineB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ _objc_msgSend$relaxedTextureArrayBindingsEnabled
+ _validateTextureBufferDescriptor.cold.1
+ _validateTextureBufferDescriptor.cold.2
+ _validateTextureBufferDescriptor.cold.3
+ _validateTextureBufferDescriptor.cold.4
+ _validateTextureBufferDescriptor.cold.5
+ _validateTextureBufferDescriptor.cold.6
+ checkAccelerationStructure.cold.1
+ checkAccelerationStructure.cold.2
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.1
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.10
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.11
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.12
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.13
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.14
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.15
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.16
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.17
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.18
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.19
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.2
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.20
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.21
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.22
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.23
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.24
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.25
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.26
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.27
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.28
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.29
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.3
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.30
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.31
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.32
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.33
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.34
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.35
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.36
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.37
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.38
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.39
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.4
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.40
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.41
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.42
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.43
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.44
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.45
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.46
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.47
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.48
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.49
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.5
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.50
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.51
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.52
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.53
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.54
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.55
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.56
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.57
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.58
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.59
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.6
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.60
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.61
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.62
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.63
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.64
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.65
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.66
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.67
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.68
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.69
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.7
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.70
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.71
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.72
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.73
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.74
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.75
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.76
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.77
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.78
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.79
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.8
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.80
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.81
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.82
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.83
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.84
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.85
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.86
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.87
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.88
+ checkAccelerationStructureDescriptorWithRefitOptions.cold.9
+ validateMTLSamplerDescriptor.cold.1
+ validateMTLSamplerDescriptor.cold.2
+ validateMTLSamplerDescriptor.cold.3
- GCC_except_table209
- GCC_except_table213
- GCC_except_table236
- GCC_except_table237
- GCC_except_table238
- GCC_except_table239
- GCC_except_table56
- __ZGVZ51-[MTLTelemetryCommandBuffer postCompletionHandlers]E9forceEmit
- __ZGVZ74-[MTLCountersCommandBuffer initWithCommandBuffer:commandQueue:descriptor:]E10dumpEvents
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne180100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne180100EPKvm
- __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne180100Ev
- __ZNKSt3__16vectorI11MetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne180100Ev
- __ZNKSt3__16vectorI19LegacySVMetalBufferNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_112_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_114HeapUsageTable19HeapUsageTableEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN12_GLOBAL__N_117ReportBufferEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIP6NSDatamEENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIj14MTLTextureTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP15MTLStructMemberNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP16MTLDebugLocationNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP17MTLGPUDebugBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP17MTLLegacySVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrI29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI29LegacySVArgumentEncoderLayoutNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImN12_GLOBAL__N_120EncoderResourceUsageEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B8ne180100Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIS3_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI7SubViewmEENS_22__unordered_map_hasherIS2_S3_NS2_6hash_tENS2_7equal_tELb1EEENS_21__unordered_map_equalIS2_S3_S6_S5_Lb1EEENS_9allocatorIS3_EEE28__node_insert_unique_prepareB8ne180100EmRS3_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIS4_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLGPUDebugResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne180100EmRS4_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIS4_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyP23MTLLegacySVResidencySetEENS_22__unordered_map_hasherIyS4_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE28__node_insert_unique_prepareB8ne180100EmRS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne180100Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__117__call_once_proxyB8ne180100INS_5tupleIJOZL23instrumentationHeapInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne180100INS_5tupleIJOZL23instrumentationHeapInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne180100INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLGPUDebugDeviceE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne180100INS_5tupleIJOZL33indirectCommandBufferPipelineInitP17MTLLegacySVDeviceE3$_0EEEEEvPv
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI11MTLViewportEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI11MetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI14MTLScissorRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI19LegacySVMetalBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI9MemberRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIP6NSDatamEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIj14MTLTextureTypeEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP15MTLStructMemberEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP16MTLDebugLocationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP17MTLGPUDebugBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP17MTLLegacySVBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPP11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU17objcproto7MTLHeap11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU21objcproto10MTLTexture11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU22objcproto11MTLResource11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU24objcproto13MTLAllocation11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU26objcproto15MTLResidencySet11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU26objcproto15MTLSamplerState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU28objcproto17MTLFunctionHandle11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU33objcproto22MTLRenderPipelineState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU34objcproto23MTLVisibleFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU13block_pointerFvPU27objcproto16MTLCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU13block_pointerFvPU29objcproto18MTLIOCommandBuffer11objc_objectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne180100EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26MTLTelemetryStatisticUIRecEEPvEEEEEclB8ne180100EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPKcEEPvEEEEEclB8ne180100EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI29GPUDebugArgumentEncoderLayoutNS_14default_deleteIS5_EEEEEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI29LegacySVArgumentEncoderLayoutNS_14default_deleteIS5_EEEEEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__126__throw_bad_variant_accessB8ne180100Ev
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__15dequeIP11objc_objectNS_9allocatorIS2_EEED2B8ne180100Ev
- __ZNSt3__16removeB8ne180100INS_11__wrap_iterIPjEEjEET_S4_S4_RKT0_
- __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI11MTLViewportNS_9allocatorIS1_EEE18__assign_with_sizeB8ne180100IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI14MTLScissorRectNS_9allocatorIS1_EEE18__assign_with_sizeB8ne180100IPKS1_S7_EEvT_T0_l
- __ZNSt3__16vectorI9MemberRefNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU17objcproto7MTLHeap11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU21objcproto10MTLTexture11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU22objcproto11MTLResource11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU24objcproto13MTLAllocation11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU26objcproto15MTLResidencySet11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU26objcproto15MTLSamplerState11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU28objcproto17MTLFunctionHandle11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU33objcproto22MTLRenderPipelineState11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU34objcproto23MTLVisibleFunctionTable11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPU39objcproto28MTLIntersectionFunctionTable11objc_objectNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorImNS_9allocatorImEEEC2Em
- __ZNSt3__17getlineB8ne180100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ51-[MTLTelemetryCommandBuffer postCompletionHandlers]E9forceEmit
- __ZZ74-[MTLCountersCommandBuffer initWithCommandBuffer:commandQueue:descriptor:]E10dumpEvents
CStrings:
+ "TB,R,V_relaxedTextureArrayBindingsEnabled"
+ "^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}"
+ "_pendingAdds"
+ "_pendingRemoves"
+ "_relaxedTextureArrayBindingsEnabled"
+ "relaxedTextureArrayBindingsEnabled"
+ "{Options=\"version\"I\"mode\"i\"accessTypes\"i\"failMode\"i\"maxTrackedResourcesMultiplier\"I\"\"{?=\"enableForPerPSO\"b1\"enableReporting\"b1\"packPointerAddresses\"b1\"unpackPointerAddress\"b1\"forceInline\"b1\"enableBacktracking\"b1\"optimizeConstantDeref\"b1\"skipVertexFetchLoads\"b1\"enableGEPOptimization\"b1\"enableRuntimeStacktrace\"b1\"emitBoundsChecking\"b1\"runStandardOptimizations\"b1\"backtrackFailuresAssumeSafe\"b1\"pageDataIs32bitLength\"b1\"forceUnrollLoops\"b1\"mergeAccessChecks\"b1\"convertToAB\"b1\"arraysOfBuffersAB\"b1\"noInlineTrivialFunctions\"b1\"unrollMemCpyWA\"b1\"checkGlobalConstants\"b1\"enableTextureChecks\"b1\"demoteGlobalConstantsToArg\"b1\"argumentPointerIndirection\"b1\"enableThreadgroupMemoryChecks\"b1\"mergeThreadgroupGlobals\"b1\"mergeThreadgroupArguments\"b1\"tagThreadgroupPointers\"b1\"enableJumpThreading\"b1\"enableICBSupport\"b1\"enableGlobalRelocations\"b1\"enableTrapReporting\"b1\"enableRaytracing\"b1\"enableResourceUsageValidation\"b1\"enableStackOverflow\"b1\"enableDumpToStderr\"b1\"enableAccelerationStructureChecking\"b1\"enableRelaxedTextureArrayBindings\"b1}}"
- "BlitUnknown"
- "^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}}"
- "{Options=\"version\"I\"mode\"i\"accessTypes\"i\"failMode\"i\"maxTrackedResourcesMultiplier\"I\"\"{?=\"enableForPerPSO\"b1\"enableReporting\"b1\"packPointerAddresses\"b1\"unpackPointerAddress\"b1\"forceInline\"b1\"enableBacktracking\"b1\"optimizeConstantDeref\"b1\"skipVertexFetchLoads\"b1\"enableGEPOptimization\"b1\"enableRuntimeStacktrace\"b1\"emitBoundsChecking\"b1\"runStandardOptimizations\"b1\"backtrackFailuresAssumeSafe\"b1\"pageDataIs32bitLength\"b1\"forceUnrollLoops\"b1\"mergeAccessChecks\"b1\"convertToAB\"b1\"arraysOfBuffersAB\"b1\"noInlineTrivialFunctions\"b1\"unrollMemCpyWA\"b1\"checkGlobalConstants\"b1\"enableTextureChecks\"b1\"demoteGlobalConstantsToArg\"b1\"argumentPointerIndirection\"b1\"enableThreadgroupMemoryChecks\"b1\"mergeThreadgroupGlobals\"b1\"mergeThreadgroupArguments\"b1\"tagThreadgroupPointers\"b1\"enableJumpThreading\"b1\"enableICBSupport\"b1\"enableGlobalRelocations\"b1\"enableTrapReporting\"b1\"enableRaytracing\"b1\"enableResourceUsageValidation\"b1\"enableStackOverflow\"b1\"enableDumpToStderr\"b1\"enableAccelerationStructureChecking\"b1}}"

```
