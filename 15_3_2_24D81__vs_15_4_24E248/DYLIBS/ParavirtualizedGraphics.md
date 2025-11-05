## ParavirtualizedGraphics

> `/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/ParavirtualizedGraphics`

```diff

-40.3.2.0.0
-  __TEXT.__text: 0x4b144
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x394c
-  __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x26ac
-  __TEXT.__cstring: 0x5818
-  __TEXT.__oslogstring: 0x2602
-  __TEXT.__unwind_info: 0x19c8
-  __TEXT.__objc_classname: 0x5e2
-  __TEXT.__objc_methname: 0xbba5
-  __TEXT.__objc_methtype: 0x9f9f
-  __TEXT.__objc_stubs: 0x9060
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x88
-  __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_protolist: 0x90
+40.5.10.0.0
+  __TEXT.__text: 0x65174
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x4008
+  __TEXT.__const: 0x3181
+  __TEXT.__gcc_except_tab: 0x4ad8
+  __TEXT.__cstring: 0x615e
+  __TEXT.__oslogstring: 0x273c
+  __TEXT.__unwind_info: 0x2490
+  __TEXT.__objc_classname: 0x671
+  __TEXT.__objc_methname: 0xb204
+  __TEXT.__objc_methtype: 0x46b8
+  __TEXT.__objc_stubs: 0x8a40
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0x68
+  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2760
+  __DATA_CONST.__objc_selrefs: 0x2688
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__const: 0x858
-  __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x85c0
-  __AUTH.__objc_data: 0x1130
-  __DATA.__objc_ivar: 0x6fc
-  __DATA.__data: 0x6c0
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__const: 0xb48
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x71e8
+  __AUTH.__objc_data: 0x11d0
+  __DATA.__objc_ivar: 0x6a0
+  __DATA.__data: 0x780
   __DATA.__bss: 0x40
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8950B08-64BC-3D52-A89C-06C6519CCE65
-  Functions: 1984
-  Symbols:   488
-  CStrings:  3363
+  UUID: 7E5F1211-083D-3DBC-BC8C-AC8AEE46BE16
+  Functions: 2311
+  Symbols:   5379
+  CStrings:  3330
 
Symbols:
+ +[PGBackingResource pixelFormatForBacking:]
+ +[PGBackingResource pixelFormatForBacking:].cold.1
+ +[PGBackingResource validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:]
+ +[PGBackingResource validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:].cold.1
+ +[PGBackingResource validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:].cold.2
+ +[PGBufferResource newBufferResourceWithTask:objectType:descriptor:descriptorLength:placement:]
+ +[PGBufferResource newMapperRefBufferWithTask:descriptor:descriptorLength:placement:]
+ +[PGBufferResource newNormalBufferWithTask:descriptor:descriptorLength:placement:]
+ +[PGBufferResource newNormalBufferWithTask:descriptor:descriptorLength:placement:].cold.1
+ +[PGHeapResource newHeapResourceWithTask:objectType:descriptor:descriptorLength:placement:]
+ +[PGHeapResource newNormalHeapResourceWithTask:descriptor:descriptorLength:placement:]
+ +[PGHeapResource newNormalHeapResourceWithTask:descriptor:descriptorLength:placement:].cold.1
+ +[PGIOSurfaceHostDevice ioSurfaceHostDevice]
+ +[PGMemoryMap supportsSecureCoding]
+ +[PGMemoryMapSegment supportsSecureCoding]
+ +[PGTextureResource createSharedTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:]
+ +[PGTextureResource createTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:]
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:]
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.1
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.10
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.11
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.12
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.13
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.14
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.15
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.16
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.17
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.18
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.19
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.2
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.20
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.21
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.22
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.23
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.24
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.25
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.3
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.4
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.5
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.6
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.7
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.8
+ +[PGTextureResource validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:].cold.9
+ +[_PGDisplay initSerialNumDB]
+ +[_PGDisplay initSerialNumDB].cold.1
+ +[_PGDisplay reserveSerialNum:]
+ +[_PGDisplay reserveSerialNum:].cold.1
+ +[_PGDisplay unreserveSerialNum:]
+ -[PGBackingResource dealloc]
+ -[PGBackingResource discard]
+ -[PGBackingResource ensurePhysical]
+ -[PGBackingResource getIOSurface]
+ -[PGBackingResource initWithTask:descriptor:planes:planeCount:]
+ -[PGBackingResource ioSurface]
+ -[PGBackingResource prepareInEncoder:]
+ -[PGBackingResource prepareInEncoder:].cold.1
+ -[PGBackingResource synchronizeInEncoder:]
+ -[PGBackingResource synchronizeInEncoder:].cold.1
+ -[PGBackingResource textures]
+ -[PGBaseTask .cxx_construct]
+ -[PGBaseTask .cxx_destruct]
+ -[PGBaseTask addressRangesForVirtualPage:length:readOnly:]
+ -[PGBaseTask backingForID:]
+ -[PGBaseTask copyFromVirtualOffset:length:dst:]
+ -[PGBaseTask cursorFromVirtualOffset:length:]
+ -[PGBaseTask dataFromVirtualOffset:length:]
+ -[PGBaseTask dealloc]
+ -[PGBaseTask deleteObjectWithSerializedData:serializedDataSize:]
+ -[PGBaseTask deleteResource:]
+ -[PGBaseTask deserializer]
+ -[PGBaseTask discardResources:count:]
+ -[PGBaseTask flushResources]
+ -[PGBaseTask getExistingHostResource:]
+ -[PGBaseTask getHostResource:]
+ -[PGBaseTask getObject:entry:]
+ -[PGBaseTask invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:]
+ -[PGBaseTask invalidateResources:count:]
+ -[PGBaseTask mapMemoryAtOffset:length:]
+ -[PGBaseTask mappedAddressForOffset:length:needWritable:]
+ -[PGBaseTask mtlDevice]
+ -[PGBaseTask newBufferForVirtualPage:length:]
+ -[PGBaseTask newSharedTextureHandleForID:]
+ -[PGBaseTask newVirtualMapping:length:needWritable:]
+ -[PGBaseTask nextTraceID]
+ -[PGBaseTask objectListCount]
+ -[PGBaseTask pagingQueue]
+ -[PGBaseTask prepareBacking:inEncoder:]
+ -[PGBaseTask rebuildTask]
+ -[PGBaseTask releaseIOSurfaceWithMappingID:surface:]
+ -[PGBaseTask replacePhysical:]
+ -[PGBaseTask retainIOSurfaceWithMappingID:]
+ -[PGBaseTask setObjectListOffset:length:]
+ -[PGBaseTask supportsBufferWithAddressRanges]
+ -[PGBaseTask supportsHeapWithAddressRanges]
+ -[PGBaseTask supportsResourceDetachBacking]
+ -[PGBaseTask synchronizeBacking:inEncoder:]
+ -[PGBaseTask synchronizeResources:count:discard:completionHandler:]
+ -[PGBaseTask synchronizeResources:count:discard:completionHandler:].cold.1
+ -[PGBaseTask synchronizeResources:count:discard:completionHandler:].cold.2
+ -[PGBaseTask teardown]
+ -[PGBaseTask unmapMemoryAtOffset:length:]
+ -[PGBaseTask writableCursorFromVirtualOffset:length:]
+ -[PGBaseTask writeToVirtualOffset:length:src:]
+ -[PGChildFIFO .cxx_construct]
+ -[PGChildFIFO advance]
+ -[PGChildFIFO dealloc]
+ -[PGChildFIFO faultOffset]
+ -[PGChildFIFO getFifoBytes:into:]
+ -[PGChildFIFO initWithDevice:baseNode:fifoIndex:restoring:lastPending:]
+ -[PGChildFIFO isRootFifo]
+ -[PGChildFIFO latchCommandOffset]
+ -[PGChildFIFO resetPending]
+ -[PGChildFIFO setFaultOffset:]
+ -[PGChildFIFO setupMapping]
+ -[PGChildFIFO stampIndex]
+ -[PGChildFIFO start]
+ -[PGChildFIFO stop]
+ -[PGChildFIFO teardownMapping]
+ -[PGDeserializerBlitDecoder dealloc]
+ -[PGDeserializerBlitDecoder decodeBlitUpdateFenceWithIterator:]
+ -[PGDeserializerBlitDecoder decodeBlitWaitForFenceWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromBufferToBufferWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromBufferToTextureWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromTextureToBufferWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromTextureToTextureWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromTextureToTextureWithNumSliceLevelWithIterator:]
+ -[PGDeserializerBlitDecoder decodeCopyFromTextureToTextureWithOptionsWithIterator:]
+ -[PGDeserializerBlitDecoder decodeFillBufferWithIterator:]
+ -[PGDeserializerBlitDecoder decodeFillBufferWithPatternWithIterator:]
+ -[PGDeserializerBlitDecoder decodeFillTextureWithBytesWithIterator:]
+ -[PGDeserializerBlitDecoder decodeFillTextureWithColorWithIterator:]
+ -[PGDeserializerBlitDecoder decodeGenerateMipmapsWithIterator:]
+ -[PGDeserializerBlitDecoder decodeInvalidateCompressedTextureImageWithIterator:]
+ -[PGDeserializerBlitDecoder decodeInvalidateCompressedTextureWithIterator:]
+ -[PGDeserializerBlitDecoder decodeOptimizeForCPUAccessWithIterator:]
+ -[PGDeserializerBlitDecoder decodeOptimizeForGPUAccessWithIterator:]
+ -[PGDeserializerBlitDecoder decodeOptimizeImageForCPUAccessWithIterator:]
+ -[PGDeserializerBlitDecoder decodeOptimizeImageForGPUAccessWithIterator:]
+ -[PGDeserializerBlitDecoder decodeSynchronizeResourceWithIterator:]
+ -[PGDeserializerBlitDecoder decodeSynchronizeTextureImageWithIterator:]
+ -[PGDeserializerBlitDecoder decodeWithHeader:withIterator:]
+ -[PGDeserializerBlitDecoder fault]
+ -[PGDeserializerBlitDecoder initWithDeserializer:commandBuffer:]
+ -[PGDeserializerBlitDecoder type]
+ -[PGDeserializerComputeDecoder dealloc]
+ -[PGDeserializerComputeDecoder decodeBarrierResourcesWithIterator:]
+ -[PGDeserializerComputeDecoder decodeBarrierScopeWithIterator:]
+ -[PGDeserializerComputeDecoder decodeComputePassDescriptor:]
+ -[PGDeserializerComputeDecoder decodeDispatchThreadgroupsIndirectWithIterator:]
+ -[PGDeserializerComputeDecoder decodeDispatchThreadgroupsWithIterator:]
+ -[PGDeserializerComputeDecoder decodeDispatchThreadsWithIterator:]
+ -[PGDeserializerComputeDecoder decodeEncodeEndDoWhile:]
+ -[PGDeserializerComputeDecoder decodeEncodeEndDoWhile:].cold.1
+ -[PGDeserializerComputeDecoder decodeEncodeEndIf:]
+ -[PGDeserializerComputeDecoder decodeEncodeEndIf:].cold.1
+ -[PGDeserializerComputeDecoder decodeEncodeEndWhile:]
+ -[PGDeserializerComputeDecoder decodeEncodeEndWhile:].cold.1
+ -[PGDeserializerComputeDecoder decodeEncodeStartDoWhile:]
+ -[PGDeserializerComputeDecoder decodeEncodeStartElse:]
+ -[PGDeserializerComputeDecoder decodeEncodeStartIf:]
+ -[PGDeserializerComputeDecoder decodeEncodeStartWhile:]
+ -[PGDeserializerComputeDecoder decodeInsertCompressedTextureReinterpretationFlush:]
+ -[PGDeserializerComputeDecoder decodeSetBufferOffsetWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetBufferOffsetWithStrideWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetBuffersWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetBuffersWithStrideWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetComputePassDispatchTypeWithIterator:descriptor:]
+ -[PGDeserializerComputeDecoder decodeSetImageblockWidthWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetPipelineStateWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetSamplersLODClampWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetSamplersWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetStageInRegionIndirectWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetStageInRegionWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetTexturesWithIterator:]
+ -[PGDeserializerComputeDecoder decodeSetThreadgroupMemoryLengthWithIterator:]
+ -[PGDeserializerComputeDecoder decodeUpdateFenceWithIterator:]
+ -[PGDeserializerComputeDecoder decodeUseHeapsWithIterator:]
+ -[PGDeserializerComputeDecoder decodeUseResourcesWithIterator:]
+ -[PGDeserializerComputeDecoder decodeWaitForFenceWithIterator:]
+ -[PGDeserializerComputeDecoder decodeWithHeader:withIterator:]
+ -[PGDeserializerComputeDecoder fault]
+ -[PGDeserializerComputeDecoder initWithDeserializer:commandBuffer:]
+ -[PGDeserializerComputeDecoder type]
+ -[PGDeserializerInfoDecoder checkBuffer:bufferOffset:forSize:]
+ -[PGDeserializerInfoDecoder dealloc]
+ -[PGDeserializerInfoDecoder decodeBufferHostResourceInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeComputePipelineImageBlockMemoryLengthWithIterator:]
+ -[PGDeserializerInfoDecoder decodeComputePipelineStateInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeCopyRasterizationRateParameterBufferWithIterator:]
+ -[PGDeserializerInfoDecoder decodeCopyRasterizationRateParameterBufferWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeCopyRasterizationRateParameterBufferWithIterator:].cold.2
+ -[PGDeserializerInfoDecoder decodeGetRasterizationRateMapInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeGetRasterizationRateMapInfoWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeHeapHostResourceInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeHeapTextureDescriptorSizeAndAlignWithIterator:]
+ -[PGDeserializerInfoDecoder decodeHeapTextureDescriptorSizeAndAlignWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeMapPhysicalToScreenCoordinatesMultipleWithIterator:]
+ -[PGDeserializerInfoDecoder decodeMapPhysicalToScreenCoordinatesMultipleWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeMapPhysicalToScreenCoordinatesWithIterator:]
+ -[PGDeserializerInfoDecoder decodeMapPhysicalToScreenCoordinatesWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeMapScreenToPhysicalCoordinatesWithIterator:]
+ -[PGDeserializerInfoDecoder decodeMapScreenToPhysicalCoordinatesWithIterator:].cold.1
+ -[PGDeserializerInfoDecoder decodeObjectUniqueIdentifier:]
+ -[PGDeserializerInfoDecoder decodeRenderPipelineImageBlockMemoryLengthWithIterator:]
+ -[PGDeserializerInfoDecoder decodeRenderPipelineStateInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeSamplerStateHostResourceInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeTextureHostResourceInfoWithIterator:]
+ -[PGDeserializerInfoDecoder decodeWithHeader:withIterator:]
+ -[PGDeserializerInfoDecoder fault]
+ -[PGDeserializerInfoDecoder initWithDeserializer:]
+ -[PGDeserializerInfoDecoder type]
+ -[PGDeserializerRenderDecoder checkBuffer:bufferOffset:forSize:]
+ -[PGDeserializerRenderDecoder dealloc]
+ -[PGDeserializerRenderDecoder decodeDispatchThreadsPerTileInRegionWithIndexWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDispatchThreadsPerTileInRegionWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDispatchThreadsPerTileWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedBasePrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedBasePrimitives16_2WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedBasePrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedBasePrimitives64_2WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedPrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedInstancedPrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPatches16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPatches64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPatchesIndirectWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawIndexedPrimitivesIndirectWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawInstancedBasePrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawInstancedBasePrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawInstancedPrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawInstancedPrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPatches16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPatches64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPatchesIndirectWithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPrimitives16WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPrimitives64WithIterator:]
+ -[PGDeserializerRenderDecoder decodeDrawPrimitivesIndirectWithIterator:]
+ -[PGDeserializerRenderDecoder decodeExecuteCommandsInBufferRangedWithIterator:]
+ -[PGDeserializerRenderDecoder decodeExecuteCommandsInBufferWithIterator:]
+ -[PGDeserializerRenderDecoder decodeGetTileDimensionsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeImageBlockSampleLengthWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeRenderBarrierResourcesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeRenderBarrierScopeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeRenderDescribeRenderPassWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeRenderPassDescriptor:]
+ -[PGDeserializerRenderDecoder decodeRenderUpdateFenceWithIterator:]
+ -[PGDeserializerRenderDecoder decodeRenderWaitForFenceWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetAlphaTestReferenceValueWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetBlendColorWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetClipPlaneWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetColorResolveTextureWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetColorStoreActionOptionsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetColorStoreActionWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetCullModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDefaultColorSampleCountWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetDefaultRasterSampleCountWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetDepthBiasWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthClearedWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthClipModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthResolveTextureWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthStencilStateWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthStoreActionOptionsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetDepthStoreActionWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentBufferOffsetWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentBuffersWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentSamplerStateWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentSamplerStatesLODClampWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentSamplerStatesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFragmentTexturesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetFrontFacingWindingWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetLineWidthWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetPointSizeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetPrimitiveRestartIndexEnabledWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetProgrammableSamplePositionsWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetProvokingVertexModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetRenderPipelineStateWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetRenderThreadgroupMemoryLengthWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetScissorRectWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetScissorRectsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetStencilClearedWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetStencilRefWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetStencilResolveTextureWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetStencilStoreActionOptionsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetStencilStoreActionWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTesselationFactorBufferWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTesselationFactorScaleWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetThreadGroupMemoryLengthWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetTileBufferOffsetWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTileBuffersWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTileParametersWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetTileSamplerStatesLODClampWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTileSamplerStatesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTileTexturesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTransformFeedbackStateWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTriangleFillModeFrontBackWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetTriangleFillModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVariableRateRasterizationMapWithIterator:descriptor:]
+ -[PGDeserializerRenderDecoder decodeSetVertexAmplificationCountWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexAmplificationModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexBufferOffsetWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexBufferOffsetWithStrideWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexBuffersWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexBuffersWithStrideWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexSamplerStateWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexSamplerStatesLODClampWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexSamplerStatesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVertexTexturesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetViewportTransformEnabledWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetViewportWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetViewportsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeSetVisibilityResultModeWithIterator:]
+ -[PGDeserializerRenderDecoder decodeTextureBarrierWithIterator:]
+ -[PGDeserializerRenderDecoder decodeUseHeapsWithIterator:]
+ -[PGDeserializerRenderDecoder decodeUseHeapsWithStagesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeUseResourcesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeUseResourcesWithStagesWithIterator:]
+ -[PGDeserializerRenderDecoder decodeWithHeader:withIterator:]
+ -[PGDeserializerRenderDecoder fault]
+ -[PGDeserializerRenderDecoder initWithDeserializer:commandBuffer:]
+ -[PGDeserializerRenderDecoder type]
+ -[PGDetachBufferResource dealloc]
+ -[PGDetachBufferResource discard]
+ -[PGDetachBufferResource ensurePhysical]
+ -[PGDetachBufferResource getBuffer]
+ -[PGDetachBufferResource getResource]
+ -[PGDetachBufferResource initWithTask:descriptor:placement:]
+ -[PGDetachBufferResource initWithTask:descriptor:placement:].cold.1
+ -[PGDetachBufferResource initWithTask:descriptor:placement:].cold.2
+ -[PGDetachBufferResource isGuestValid]
+ -[PGDetachBufferResource isHostValid]
+ -[PGDetachBufferResource needsPrepare]
+ -[PGDetachBufferResource needsSync]
+ -[PGDetachBufferResource prepareInEncoder:]
+ -[PGDetachBufferResource setIsGuestValid:]
+ -[PGDetachBufferResource synchronizeInEncoder:]
+ -[PGDetachHeapResource dealloc]
+ -[PGDetachHeapResource devolatilize]
+ -[PGDetachHeapResource discard]
+ -[PGDetachHeapResource ensurePhysical]
+ -[PGDetachHeapResource getHeap]
+ -[PGDetachHeapResource initWithTask:descriptor:placement:]
+ -[PGDetachHeapResource initWithTask:descriptor:placement:].cold.1
+ -[PGDetachHeapResource initWithTask:descriptor:placement:].cold.2
+ -[PGDetachHeapResource initWithTask:descriptor:placement:].cold.3
+ -[PGDetachHeapResource initWithTask:descriptor:placement:].cold.4
+ -[PGDetachHeapResource needsPrepare]
+ -[PGDetachHeapResource needsSync]
+ -[PGDetachHeapResource newChildBufferResourceWithBuffer:]
+ -[PGDetachHeapResource prepareInEncoder:]
+ -[PGDetachHeapResource synchronizeInEncoder:]
+ -[PGDeviceDescriptor addTraceRange]
+ -[PGDeviceDescriptor createTask]
+ -[PGDeviceDescriptor dealloc]
+ -[PGDeviceDescriptor destroyTask]
+ -[PGDeviceDescriptor deviceFeatureLevel]
+ -[PGDeviceDescriptor device]
+ -[PGDeviceDescriptor displayPortCount]
+ -[PGDeviceDescriptor enableArgumentBuffers]
+ -[PGDeviceDescriptor enableProcessIsolation]
+ -[PGDeviceDescriptor enableProtectedContent]
+ -[PGDeviceDescriptor enableResourceDetachment]
+ -[PGDeviceDescriptor init]
+ -[PGDeviceDescriptor mapMemory]
+ -[PGDeviceDescriptor memoryMapDescriptor]
+ -[PGDeviceDescriptor mmioLength]
+ -[PGDeviceDescriptor raiseInterrupt]
+ -[PGDeviceDescriptor readMemory]
+ -[PGDeviceDescriptor removeTraceRange]
+ -[PGDeviceDescriptor setAddTraceRange:]
+ -[PGDeviceDescriptor setCreateTask:]
+ -[PGDeviceDescriptor setDestroyTask:]
+ -[PGDeviceDescriptor setDevice:]
+ -[PGDeviceDescriptor setDeviceFeatureLevel:]
+ -[PGDeviceDescriptor setDisplayPortCount:]
+ -[PGDeviceDescriptor setEnableArgumentBuffers:]
+ -[PGDeviceDescriptor setEnableProcessIsolation:]
+ -[PGDeviceDescriptor setEnableProtectedContent:]
+ -[PGDeviceDescriptor setEnableResourceDetachment:]
+ -[PGDeviceDescriptor setMapMemory:]
+ -[PGDeviceDescriptor setMemoryMapDescriptor:]
+ -[PGDeviceDescriptor setMmioLength:]
+ -[PGDeviceDescriptor setRaiseInterrupt:]
+ -[PGDeviceDescriptor setReadMemory:]
+ -[PGDeviceDescriptor setRemoveTraceRange:]
+ -[PGDeviceDescriptor setUnmapMemory:]
+ -[PGDeviceDescriptor setUsingIOSurfaceMapper:]
+ -[PGDeviceDescriptor unmapMemory]
+ -[PGDeviceDescriptor usingIOSurfaceMapper]
+ -[PGDiscardableHeapBufferResource supportsDiscard]
+ -[PGDiscardableSerializerTextureResource discard]
+ -[PGDiscardableSerializerTextureResource supportsDiscard]
+ -[PGDisplayDescriptor cursorGlyphHandler]
+ -[PGDisplayDescriptor cursorMoveHandler]
+ -[PGDisplayDescriptor cursorShowHandler]
+ -[PGDisplayDescriptor dealloc]
+ -[PGDisplayDescriptor init]
+ -[PGDisplayDescriptor modeChangeHandler]
+ -[PGDisplayDescriptor name]
+ -[PGDisplayDescriptor newFrameEventHandler]
+ -[PGDisplayDescriptor queue]
+ -[PGDisplayDescriptor setCursorGlyphHandler:]
+ -[PGDisplayDescriptor setCursorMoveHandler:]
+ -[PGDisplayDescriptor setCursorShowHandler:]
+ -[PGDisplayDescriptor setModeChangeHandler:]
+ -[PGDisplayDescriptor setName:]
+ -[PGDisplayDescriptor setNewFrameEventHandler:]
+ -[PGDisplayDescriptor setQueue:]
+ -[PGDisplayDescriptor setSizeInMillimeters:]
+ -[PGDisplayDescriptor sizeInMillimeters]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) colorSpace]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) compositorParametersHandler]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) configEpoch]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) connectionType]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) cursorGlyphHandler2]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) maxNits]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) maxSDRNits]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) minNits]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) modeListResponsivenessChangeHandler]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) optIntoUsingUnplugMethod]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) origin]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) scaleFactor]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setColorSpace:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setCompositorParametersHandler:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setConfigEpoch:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setConnectionType:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setCursorGlyphHandler2:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setMaxNits:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setMaxSDRNits:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setMinNits:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setModeListResponsivenessChangeHandler:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setOptIntoUsingUnplugMethod:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setOrigin:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setScaleFactor:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) setSleepHandler:]
+ -[PGDisplayDescriptor(PGDisplayDescriptorPrivate) sleepHandler]
+ -[PGDisplayMode initWithSizeInPixels:refreshRateInHz:]
+ -[PGDisplayMode refreshRate]
+ -[PGDisplayMode sizeInPixels]
+ -[PGDisplayMode(PGDisplayModePrivate) setSupports10bpc:]
+ -[PGDisplayMode(PGDisplayModePrivate) setSupportsEDR:]
+ -[PGDisplayMode(PGDisplayModePrivate) supports10bpc]
+ -[PGDisplayMode(PGDisplayModePrivate) supportsEDR]
+ -[PGDisplayPipelineCache dealloc]
+ -[PGDisplayPipelineCache initWithDevice:]
+ -[PGDisplayPipelineCache initWithDevice:].cold.1
+ -[PGDisplayPipelineCache initWithDevice:].cold.2
+ -[PGDisplayPipelineCache initWithDevice:].cold.3
+ -[PGDisplayPipelineCache initWithDevice:].cold.4
+ -[PGDisplayPipelineCache pipelineForDescriptor:]
+ -[PGDisplayPipelineDescriptor copyWithZone:]
+ -[PGDisplayPipelineDescriptor hasGamma]
+ -[PGDisplayPipelineDescriptor hash]
+ -[PGDisplayPipelineDescriptor isEqual:]
+ -[PGDisplayPipelineDescriptor renderTargetPixelFormat]
+ -[PGDisplayPipelineDescriptor setHasGamma:]
+ -[PGDisplayPipelineDescriptor setRenderTargetPixelFormat:]
+ -[PGDualPlaneBlitTextureResource dealloc]
+ -[PGDualPlaneBlitTextureResource ensurePhysical]
+ -[PGDualPlaneBlitTextureResource initWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:]
+ -[PGDualPlaneBlitTextureResource pageTextureInEncoder:isDownload:]
+ -[PGDualPlaneBlitTextureResource pageTextureInEncoder:isDownload:].cold.1
+ -[PGDualPlaneBlitTextureResource prepareInEncoder:]
+ -[PGDualPlaneBlitTextureResource prepareInEncoder:].cold.1
+ -[PGDualPlaneBlitTextureResource synchronizeInEncoder:]
+ -[PGDualPlaneBlitTextureResource synchronizeInEncoder:].cold.1
+ -[PGDualPlaneComputeTextureResource dealloc]
+ -[PGDualPlaneComputeTextureResource discard]
+ -[PGDualPlaneComputeTextureResource ensurePhysical]
+ -[PGDualPlaneComputeTextureResource initWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:]
+ -[PGDualPlaneComputeTextureResource needsComputePaging]
+ -[PGDualPlaneComputeTextureResource pageTextureInEncoder:isDownload:]
+ -[PGDualPlaneComputeTextureResource prepareInComputeEncoder:]
+ -[PGDualPlaneComputeTextureResource prepareInComputeEncoder:].cold.1
+ -[PGDualPlaneComputeTextureResource prepareInEncoder:]
+ -[PGDualPlaneComputeTextureResource setupFormatSpecific]
+ -[PGDualPlaneComputeTextureResource synchronizeInComputeEncoder:]
+ -[PGDualPlaneComputeTextureResource synchronizeInComputeEncoder:].cold.1
+ -[PGDualPlaneComputeTextureResource synchronizeInEncoder:]
+ -[PGDualPlaneSharedTextureBackingResource dealloc]
+ -[PGDualPlaneSharedTextureBackingResource initWithTask:pagingInfo:dimension:dimensionLength:texture:]
+ -[PGDualPlaneSharedTextureBackingResource initWithTask:pagingInfo:dimension:dimensionLength:texture:].cold.1
+ -[PGDualPlaneSharedTextureBackingResource needsComputePaging]
+ -[PGDualPlaneSharedTextureBackingResource newSharedTextureHandle]
+ -[PGDualPlaneSharedTextureBackingResource pageTextureInEncoder:isDownload:]
+ -[PGDualPlaneSharedTextureBackingResource pageTextureInEncoder:isDownload:].cold.1
+ -[PGDualPlaneSharedTextureBackingResource prepareInEncoder:]
+ -[PGDualPlaneSharedTextureBackingResource prepareInEncoder:].cold.1
+ -[PGDualPlaneSharedTextureBackingResource prepareSharedTextureBacking:]
+ -[PGDualPlaneSharedTextureBackingResource synchronizeInEncoder:]
+ -[PGDualPlaneSharedTextureBackingResource synchronizeInEncoder:].cold.1
+ -[PGEFIDisplay .cxx_destruct]
+ -[PGEFIDisplay cancelFramePresents]
+ -[PGEFIDisplay dealloc]
+ -[PGEFIDisplay getModeCount]
+ -[PGEFIDisplay getModeValue]
+ -[PGEFIDisplay getStrideAlignment]
+ -[PGEFIDisplay initWithDevice:]
+ -[PGEFIDisplay present]
+ -[PGEFIDisplay scheduleFramePresents]
+ -[PGEFIDisplay setDisplay:]
+ -[PGEFIDisplay setFramebufferDepth:]
+ -[PGEFIDisplay setFramebufferLength:]
+ -[PGEFIDisplay setFramebufferMode:]
+ -[PGEFIDisplay setFramebufferMode:].cold.1
+ -[PGEFIDisplay setFramebufferStart:]
+ -[PGEFIDisplay setFramebufferStride:]
+ -[PGEFIDisplay setModeSelect:]
+ -[PGEFIDisplay stopPresentation]
+ -[PGEFIDisplay teardown]
+ -[PGEFIDisplay updateFramebufferMapping]
+ -[PGEFIDisplay updateFramebufferMapping].cold.1
+ -[PGEFIDisplay updateFramebufferMapping].cold.2
+ -[PGEFIDisplay updateFramebufferMapping].cold.3
+ -[PGEFIDisplay updateFramebufferMode]
+ -[PGEFIDisplay updateFramebufferMode].cold.1
+ -[PGEFIDisplay updateFramebufferMode].cold.2
+ -[PGEFIDisplay updateFramebufferMode].cold.3
+ -[PGFIFO .cxx_construct]
+ -[PGFIFO .cxx_destruct]
+ -[PGFIFO CmdDebug:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDebug:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDefineChildFIFO:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDefineChildFIFO:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDefineChildFIFO:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDefineTask2:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDefineTask2:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDelay:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDelay:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteChildFIFO:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteChildFIFO:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteChildFIFO:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDeleteIOSurfaceBacking2:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteIOSurfaceBacking2:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteObject:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteObject:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteObject:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDeleteResource:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteResource:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteSharedTextureBacking:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteSharedTextureBacking:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteTask:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeleteTask:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDeleteTask:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDeprecated:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDeprecated:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDiscardResources:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDiscardResources:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDiscardResources:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDisplayAck:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayAck:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplayCompositorParameters:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayCompositorParameters:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplayCursorGlyph:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayCursorGlyph:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplayCursorShow:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayCursorShow:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySetGuestICCProfile:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplaySetGuestICCProfile:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySetGuestICCProfile:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDisplaySetProperties:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplaySetProperties:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySetProperties:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDisplaySetProperties:stampValue:withPayload:payloadSize:].cold.3
+ -[PGFIFO CmdDisplaySetProperties:stampValue:withPayload:payloadSize:].cold.4
+ -[PGFIFO CmdDisplaySetSharedStatePage:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplaySetSharedStatePage:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySleepState:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplaySleepState:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySwapMapping:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplaySwapMapping:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplaySwapMapping:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdDisplayTransaction2_DEPRECATED:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayTransaction2_DEPRECATED:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplayTransaction3:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdDisplayTransaction3:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdDisplayTransaction3:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdExecIndirect2:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdExecIndirect2:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdExecIndirect2:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdExecIndirect3:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdExecIndirect3:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdExecIndirect3:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdGetComputeInfo:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdGetComputeInfo:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdGetDeviceInfo:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdGetDeviceInfo:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdHeapTextureSizeAndAlign:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdHeapTextureSizeAndAlign:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdHeapTextureSizeAndAlign:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdInvalidateResources:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdInvalidateResources:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdInvalidateResources:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdMapMemory2:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdMapMemory2:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdNOP:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdReplacePhysical:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdReplacePhysical:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdResetRasterizationRateMap:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdResetRasterizationRateMap:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdSetObjectAndPlacementList:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdSetObjectAndPlacementList:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdSetObjectList:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdSetObjectList:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdSynchronizeAndDiscardResources:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdSynchronizeAndDiscardResources:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdSynchronizeAndDiscardResources:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdSynchronizeResources:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdSynchronizeResources:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO CmdSynchronizeResources:stampValue:withPayload:payloadSize:].cold.2
+ -[PGFIFO CmdUnmapMemory:stampValue:withPayload:payloadSize:]
+ -[PGFIFO CmdUnmapMemory:stampValue:withPayload:payloadSize:].cold.1
+ -[PGFIFO advance]
+ -[PGFIFO barrierWait:barrier:]
+ -[PGFIFO commandLength]
+ -[PGFIFO currentCommandOffset]
+ -[PGFIFO dealloc]
+ -[PGFIFO describePending]
+ -[PGFIFO device]
+ -[PGFIFO drain]
+ -[PGFIFO drain].cold.1
+ -[PGFIFO faultAtOffset:stampValue:]
+ -[PGFIFO faultAtStampValue:]
+ -[PGFIFO getFifoBytes:into:]
+ -[PGFIFO initWithDevice:lastPending:]
+ -[PGFIFO isQuiesced]
+ -[PGFIFO latchCommandOffset]
+ -[PGFIFO poke]
+ -[PGFIFO processFifo]
+ -[PGFIFO processFifo].cold.1
+ -[PGFIFO processFifo].cold.2
+ -[PGFIFO processFifo].cold.3
+ -[PGFIFO processFifo].cold.4
+ -[PGFIFO pushStamp:cmdID:]
+ -[PGFIFO quiesce]
+ -[PGFIFO resetPending]
+ -[PGFIFO resume]
+ -[PGFIFO setupMapping]
+ -[PGFIFO signalStampValue:]
+ -[PGFIFO start]
+ -[PGFIFO stop]
+ -[PGFIFO teardownMapping]
+ -[PGHeapBufferResource dealloc]
+ -[PGHeapBufferResource discard]
+ -[PGHeapBufferResource getBuffer]
+ -[PGHeapBufferResource getResource]
+ -[PGHeapBufferResource initWithBuffer:]
+ -[PGHeapBufferResource needsPrepare]
+ -[PGHeapBufferResource needsSync]
+ -[PGHeapBufferResource prepareInEncoder:]
+ -[PGHeapBufferResource supportsDiscard]
+ -[PGHeapBufferResource synchronizeInEncoder:]
+ -[PGIOSurfaceHostDevice createPlaneDictionaries:]
+ -[PGIOSurfaceHostDevice createPlaneDictionary:]
+ -[PGIOSurfaceHostDevice createPlaneDictionary:].cold.1
+ -[PGIOSurfaceHostDevice createSurfaceDictionaryWithDescriptor:hostData:]
+ -[PGIOSurfaceHostDevice createSurfaceDictionaryWithDescriptor:hostData:].cold.1
+ -[PGIOSurfaceHostDevice createSurfaceDictionaryWithDescriptor:hostData:].cold.2
+ -[PGIOSurfaceHostDevice dealloc]
+ -[PGIOSurfaceHostDevice initWithDescriptor:]
+ -[PGIOSurfaceHostDevice initWithDescriptor:].cold.1
+ -[PGIOSurfaceHostDevice initWithDescriptor:].cold.2
+ -[PGIOSurfaceHostDevice initWithDescriptor:].cold.3
+ -[PGIOSurfaceHostDevice mapSurface:]
+ -[PGIOSurfaceHostDevice mapSurface:].cold.1
+ -[PGIOSurfaceHostDevice mapSurface:].cold.2
+ -[PGIOSurfaceHostDevice mmioReadAtOffset:]
+ -[PGIOSurfaceHostDevice mmioWriteAtOffset:value:]
+ -[PGIOSurfaceHostDevice resetWithMemoryMap:]
+ -[PGIOSurfaceHostDevice reset]
+ -[PGIOSurfaceHostDevice restoreWithSavedState:error:]
+ -[PGIOSurfaceHostDevice restoreWithSavedState:error:].cold.1
+ -[PGIOSurfaceHostDevice restoreWithSavedState:error:].cold.2
+ -[PGIOSurfaceHostDevice retainSurfaceWithMappingID:]
+ -[PGIOSurfaceHostDevice retainSurfaceWithMappingID:].cold.1
+ -[PGIOSurfaceHostDevice saveState]
+ -[PGIOSurfaceHostDevice saveState].cold.1
+ -[PGIOSurfaceHostDevice setDescriptorBase:]
+ -[PGIOSurfaceHostDevice setDescriptorBase:].cold.1
+ -[PGIOSurfaceHostDevice setDescriptorEnable:]
+ -[PGIOSurfaceHostDevice setDescriptorEnable:].cold.1
+ -[PGIOSurfaceHostDevice setRingBase:]
+ -[PGIOSurfaceHostDevice setRingSize:]
+ -[PGIOSurfaceHostDevice setRingSize:].cold.1
+ -[PGIOSurfaceHostDevice setRingSize:].cold.2
+ -[PGIOSurfaceHostDevice setRingSize:].cold.3
+ -[PGIOSurfaceHostDevice teardownSurfaces]
+ -[PGIOSurfaceHostDevice teardownSurfaces].cold.1
+ -[PGIOSurfaceHostDevice testSurface:]
+ -[PGIOSurfaceHostDevice unmapSurface:]
+ -[PGIOSurfaceHostDevice unmapSurface:].cold.1
+ -[PGIOSurfaceHostDevice unmapSurface:].cold.2
+ -[PGIOSurfaceHostDevice wakeDevice]
+ -[PGIOSurfaceHostDeviceDescriptor dealloc]
+ -[PGIOSurfaceHostDeviceDescriptor init]
+ -[PGIOSurfaceHostDeviceDescriptor memoryMapDescriptor]
+ -[PGIOSurfaceHostDeviceDescriptor mmioLength]
+ -[PGIOSurfaceHostDeviceDescriptor raiseInterrupt]
+ -[PGIOSurfaceHostDeviceDescriptor setMemoryMapDescriptor:]
+ -[PGIOSurfaceHostDeviceDescriptor setMmioLength:]
+ -[PGIOSurfaceHostDeviceDescriptor setRaiseInterrupt:]
+ -[PGLegacyHeapResource dealloc]
+ -[PGLegacyHeapResource devolatilize]
+ -[PGLegacyHeapResource discard]
+ -[PGLegacyHeapResource ensurePhysical]
+ -[PGLegacyHeapResource getHeap]
+ -[PGLegacyHeapResource initWithTask:descriptor:placement:]
+ -[PGLegacyHeapResource initWithTask:descriptor:placement:].cold.1
+ -[PGLegacyHeapResource initWithTask:descriptor:placement:].cold.2
+ -[PGLegacyHeapResource newChildBufferResourceWithBuffer:]
+ -[PGLegacyHeapResource prepareInEncoder:]
+ -[PGLegacyHeapResource prepareInEncoder:].cold.1
+ -[PGLegacyHeapResource synchronizeInEncoder:]
+ -[PGLegacyHeapResource synchronizeInEncoder:].cold.1
+ -[PGLocalTask .cxx_construct]
+ -[PGLocalTask .cxx_destruct]
+ -[PGLocalTask addressForOffset:length:]
+ -[PGLocalTask argumentBuffersAllowed]
+ -[PGLocalTask backingForID:]
+ -[PGLocalTask blitInRGB_2P_XR10_A8_pipeline]
+ -[PGLocalTask blitOutRGB_2P_XR10_A8_pipeline]
+ -[PGLocalTask completeResources:sync:completionHandler:]
+ -[PGLocalTask copyFromVirtualOffset:length:dst:]
+ -[PGLocalTask cursorFromVirtualOffset:length:]
+ -[PGLocalTask cursorFromVirtualOffset:length:].cold.1
+ -[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:]
+ -[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:].cold.1
+ -[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:].cold.2
+ -[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:].cold.3
+ -[PGLocalTask dealloc]
+ -[PGLocalTask deleteBacking:completionHandler:]
+ -[PGLocalTask deleteObjectWithSerializedData:serializedDataSize:completionHandler:]
+ -[PGLocalTask deleteResource:completionHandler:]
+ -[PGLocalTask deserializer]
+ -[PGLocalTask device]
+ -[PGLocalTask discardResources:count:completionHandler:]
+ -[PGLocalTask doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:]
+ -[PGLocalTask doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:].cold.1
+ -[PGLocalTask execIndirect2WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:]
+ -[PGLocalTask execIndirect3WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:]
+ -[PGLocalTask features]
+ -[PGLocalTask fifoDeleted:completionHandler:]
+ -[PGLocalTask getComputeInfo:maxKey:count:offset:completionHandler:]
+ -[PGLocalTask heapTextureSizeAndAlign:serializerPayloadLength:replyVirtualOffset:replyLength:completionHandler:]
+ -[PGLocalTask heapTextureSizeAndAlign:serializerPayloadLength:replyVirtualOffset:replyLength:completionHandler:].cold.1
+ -[PGLocalTask initWithDevice:taskRoot:length:taskID:]
+ -[PGLocalTask initWithDevice:taskRoot:length:taskID:].cold.1
+ -[PGLocalTask invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:]
+ -[PGLocalTask invalidateResources:count:completionHandler:]
+ -[PGLocalTask ioSurfaceBuffersAllowed]
+ -[PGLocalTask legacyMappedAddressForOffset:length:]
+ -[PGLocalTask mapMemoryAtOffset:length:completionHandler:]
+ -[PGLocalTask mapMemoryInternalAtOffset:length:]
+ -[PGLocalTask mapMemoryInternalAtOffset:length:].cold.1
+ -[PGLocalTask mappedAddressForOffset:length:needWritable:]
+ -[PGLocalTask mappedAddressForPageNumber:length:]
+ -[PGLocalTask memoryMapMappedAddressForOffset:length:needWritable:]
+ -[PGLocalTask mtlDevice]
+ -[PGLocalTask newBufferForVirtualPage:length:]
+ -[PGLocalTask newLegacyBufferForVirtualPage:length:]
+ -[PGLocalTask newMemoryMapBufferForVirtualPage:length:]
+ -[PGLocalTask newSharedTextureHandleForID:]
+ -[PGLocalTask newSharedTextureHandleForID:].cold.1
+ -[PGLocalTask newVirtualMapping:length:needWritable:]
+ -[PGLocalTask nextTraceID]
+ -[PGLocalTask objectListCount]
+ -[PGLocalTask prepareBacking:inEncoder:]
+ -[PGLocalTask prepareResources:event:value:]
+ -[PGLocalTask preparedBackingForID:]
+ -[PGLocalTask releaseIOSurfaceWithMappingID:surface:]
+ -[PGLocalTask replacePhysical:completionHandler:]
+ -[PGLocalTask resetRasterizationRateMap:completionHandler:]
+ -[PGLocalTask resetRasterizationRateMap:completionHandler:].cold.1
+ -[PGLocalTask retainIOSurfaceWithMappingID:]
+ -[PGLocalTask retainIOSurfaceWithMappingID:].cold.1
+ -[PGLocalTask setObjectListOffset:objectListLength:placementListOffset:placementListLength:completionHandler:]
+ -[PGLocalTask setupTaskRoot:]
+ -[PGLocalTask setupTaskRoot:].cold.1
+ -[PGLocalTask setupTaskRoot:].cold.2
+ -[PGLocalTask synchronizeBacking:inEncoder:]
+ -[PGLocalTask unmapMemoryAtOffset:length:completionHandler:]
+ -[PGLocalTask validateRangeMapped:length:]
+ -[PGMapMapping dealloc]
+ -[PGMapMapping initWithVirtualAddress:length:writable:]
+ -[PGMapperRefBufferResource .cxx_destruct]
+ -[PGMapperRefBufferResource dealloc]
+ -[PGMapperRefBufferResource discard]
+ -[PGMapperRefBufferResource ensurePhysical]
+ -[PGMapperRefBufferResource getBuffer]
+ -[PGMapperRefBufferResource getResource]
+ -[PGMapperRefBufferResource initWithTask:descriptor:placement:]
+ -[PGMapperRefBufferResource isGuestValid]
+ -[PGMapperRefBufferResource isHostValid]
+ -[PGMapperRefBufferResource needsSync]
+ -[PGMapperRefBufferResource prepareInEncoder:]
+ -[PGMapperRefBufferResource supportsDiscard]
+ -[PGMapperRefBufferResource synchronizeInEncoder:]
+ -[PGMapperRefTextureResource .cxx_destruct]
+ -[PGMapperRefTextureResource dealloc]
+ -[PGMapperRefTextureResource ensurePhysical]
+ -[PGMapperRefTextureResource getResource]
+ -[PGMapperRefTextureResource getTexture]
+ -[PGMapperRefTextureResource initWithTask:mappingID:texture:]
+ -[PGMapperRefTextureResource isGuestValid]
+ -[PGMapperRefTextureResource isHostValid]
+ -[PGMapperRefTextureResource prepareInEncoder:]
+ -[PGMapperRefTextureResource supportsDiscard]
+ -[PGMapperRefTextureResource synchronizeInEncoder:]
+ -[PGMapping initWithVirtualAddress:length:]
+ -[PGMapping initWithVirtualAddress:length:writable:]
+ -[PGMapping length]
+ -[PGMapping virtualAddress]
+ -[PGMapping writable]
+ -[PGMappingTask baseAddress]
+ -[PGMappingTask dealloc]
+ -[PGMappingTask initWithSize:memoryMap:]
+ -[PGMappingTask initWithSize:memoryMap:].cold.1
+ -[PGMappingTask mapMemoryAtVirtualOffset:rangeCount:ranges:readOnly:]
+ -[PGMappingTask size]
+ -[PGMappingTask unmapMemoryAtVirtualOffset:length:]
+ -[PGMemoryMap .cxx_construct]
+ -[PGMemoryMap .cxx_destruct]
+ -[PGMemoryMap copyWithZone:]
+ -[PGMemoryMap dealloc]
+ -[PGMemoryMap encodeWithCoder:]
+ -[PGMemoryMap initWithCoder:]
+ -[PGMemoryMap initWithCoder:].cold.1
+ -[PGMemoryMap initWithDescriptor:]
+ -[PGMemoryMap initWithDescriptor:].cold.1
+ -[PGMemoryMap initWithDescriptor:].cold.2
+ -[PGMemoryMap initWithDescriptor:].cold.3
+ -[PGMemoryMap initWithDescriptor:].cold.4
+ -[PGMemoryMap initWithDescriptor:].cold.5
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:]
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.1
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.2
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.3
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.4
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.5
+ -[PGMemoryMap mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:].cold.6
+ -[PGMemoryMap newContiguousMapping:length:readOnly:]
+ -[PGMemoryMap newRangeMapping:rangeCount:totalLength:readOnly:]
+ -[PGMemoryMap newRangeMapping:rangeCount:totalLength:readOnly:].cold.1
+ -[PGMemoryMap read:length:dst:]
+ -[PGMemoryMap virtualAddressForPhysical:length:]
+ -[PGMemoryMap virtualAddressForPhysical:length:].cold.1
+ -[PGMemoryMap virtualAddressForPhysical:length:].cold.2
+ -[PGMemoryMap write:length:src:]
+ -[PGMemoryMapDescriptor .cxx_construct]
+ -[PGMemoryMapDescriptor .cxx_destruct]
+ -[PGMemoryMapDescriptor addRange:]
+ -[PGMemoryMapDescriptor getRanges]
+ -[PGMemoryMapSegment dealloc]
+ -[PGMemoryMapSegment encodeWithCoder:]
+ -[PGMemoryMapSegment initWithCoder:]
+ -[PGMemoryMapSegment initWithRange:]
+ -[PGMemoryMapSegment physicalAddress]
+ -[PGMemoryMapSegment physicalLength]
+ -[PGMemoryMapSegment virtualAddress]
+ -[PGPageTableIterator dealloc]
+ -[PGPageTableIterator initWithRoot:depth:allowHoles:read:]
+ -[PGPageTableIterator visitPagesInRange:length:visitor:]
+ -[PGPrivateBufferResource dealloc]
+ -[PGPrivateBufferResource devolatilize]
+ -[PGPrivateBufferResource discard]
+ -[PGPrivateBufferResource ensurePhysical]
+ -[PGPrivateBufferResource getBuffer]
+ -[PGPrivateBufferResource getResource]
+ -[PGPrivateBufferResource initWithTask:descriptor:placement:]
+ -[PGPrivateBufferResource initWithTask:descriptor:placement:].cold.1
+ -[PGPrivateBufferResource prepareInEncoder:]
+ -[PGPrivateBufferResource prepareInEncoder:].cold.1
+ -[PGPrivateBufferResource synchronizeInEncoder:]
+ -[PGPrivateBufferResource synchronizeInEncoder:].cold.1
+ -[PGRefTextureResource dealloc]
+ -[PGRefTextureResource evictInEncoder:]
+ -[PGRefTextureResource getResource]
+ -[PGRefTextureResource getTexture]
+ -[PGRefTextureResource initWithTask:objectType:texture:backing:]
+ -[PGRefTextureResource isGuestValid]
+ -[PGRefTextureResource isHostValid]
+ -[PGRefTextureResource prepareInEncoder:]
+ -[PGRefTextureResource setIsGuestValid:]
+ -[PGRefTextureResource setIsHostValid:]
+ -[PGRefTextureResource supportsDiscard]
+ -[PGRefTextureResource synchronizeInEncoder:]
+ -[PGRemoteTask .cxx_construct]
+ -[PGRemoteTask dealloc]
+ -[PGRemoteTask deleteObjectWithSerializedData:serializedDataSize:completionHandler:]
+ -[PGRemoteTask deleteResource:completionHandler:]
+ -[PGRemoteTask discardResources:count:completionHandler:]
+ -[PGRemoteTask doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:]
+ -[PGRemoteTask doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:].cold.1
+ -[PGRemoteTask doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:].cold.2
+ -[PGRemoteTask execIndirect2WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:]
+ -[PGRemoteTask execIndirect2WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:].cold.1
+ -[PGRemoteTask execIndirect3WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:]
+ -[PGRemoteTask execIndirect3WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:].cold.1
+ -[PGRemoteTask fifoDeleted:completionHandler:]
+ -[PGRemoteTask flushResources]
+ -[PGRemoteTask getComputeInfo:maxKey:count:offset:completionHandler:]
+ -[PGRemoteTask heapTextureSizeAndAlign:serializerPayloadLength:replyVirtualOffset:replyLength:completionHandler:]
+ -[PGRemoteTask initWithDevice:taskRoot:length:taskID:]
+ -[PGRemoteTask invalidateResources:count:completionHandler:]
+ -[PGRemoteTask mapMemoryAtOffset:length:completionHandler:]
+ -[PGRemoteTask replacePhysical:completionHandler:]
+ -[PGRemoteTask resetRasterizationRateMap:completionHandler:]
+ -[PGRemoteTask setObjectListOffset:objectListLength:placementListOffset:placementListLength:completionHandler:]
+ -[PGRemoteTask synchronizeResources:count:discard:completionHandler:]
+ -[PGRemoteTask teardown]
+ -[PGRemoteTask unmapMemoryAtOffset:length:completionHandler:]
+ -[PGRemoteTaskDeviceDelegate .cxx_construct]
+ -[PGRemoteTaskDeviceDelegate .cxx_destruct]
+ -[PGRemoteTaskDeviceDelegate async]
+ -[PGRemoteTaskDeviceDelegate completeAsyncTokenID:success:error:]
+ -[PGRemoteTaskDeviceDelegate initWithDevice:]
+ -[PGRemoteTaskDeviceDelegate invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:]
+ -[PGRemoteTaskDeviceDelegate invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:].cold.1
+ -[PGRemoteTaskDeviceDelegate newAsyncTokenWithBlock:]
+ -[PGRemoteTaskDeviceDelegate newAsyncToken]
+ -[PGRemoteTaskDeviceDelegate newSharedTextureHandleForID:reply:]
+ -[PGRemoteTaskDeviceDelegate newSharedTextureHandleForID:reply:].cold.1
+ -[PGRemoteTaskDeviceDelegate releaseIOSurfaceWithMappingID:]
+ -[PGRemoteTaskDeviceDelegate remoteCrashed]
+ -[PGRemoteTaskDeviceDelegate retainIOSurfaceWithMappingID:reply:]
+ -[PGRemoteTaskDeviceDelegate retainIOSurfaceWithMappingID:reply:].cold.1
+ -[PGResource discard]
+ -[PGResource evictInComputeEncoder:]
+ -[PGResource evictInEncoder:]
+ -[PGResource getBuffer]
+ -[PGResource getHeap]
+ -[PGResource getResource]
+ -[PGResource getSharedTextureBackingID]
+ -[PGResource getTexture]
+ -[PGResource isGuestValid]
+ -[PGResource isHostValid]
+ -[PGResource needsComputePaging]
+ -[PGResource needsPrepare]
+ -[PGResource needsSync]
+ -[PGResource newChildBufferResourceWithBuffer:]
+ -[PGResource newChildTextureResourceWithTexture:]
+ -[PGResource prepareInComputeEncoder:]
+ -[PGResource prepareInEncoder:]
+ -[PGResource setIsGuestValid:]
+ -[PGResource setIsHostValid:]
+ -[PGResource supportsDiscard]
+ -[PGResource synchronizeInComputeEncoder:]
+ -[PGResource synchronizeInEncoder:]
+ -[PGResourceManagerDelegate deleteBufferForReference:]
+ -[PGResourceManagerDelegate deleteComputePipelineStateForReference:]
+ -[PGResourceManagerDelegate deleteDepthStencilStateForReference:]
+ -[PGResourceManagerDelegate deleteFenceForReference:]
+ -[PGResourceManagerDelegate deleteFunctionForReference:]
+ -[PGResourceManagerDelegate deleteHeapForReference:]
+ -[PGResourceManagerDelegate deleteRasterizationRateMapForReference:]
+ -[PGResourceManagerDelegate deleteRenderPipelineStateForReference:]
+ -[PGResourceManagerDelegate deleteSamplerStateForReference:]
+ -[PGResourceManagerDelegate deleteTextureForReference:]
+ -[PGResourceManagerDelegate getBufferForReference:]
+ -[PGResourceManagerDelegate getBufferForReference:].cold.1
+ -[PGResourceManagerDelegate getComputePipelineStateForReference:]
+ -[PGResourceManagerDelegate getComputePipelineStateForReference:].cold.1
+ -[PGResourceManagerDelegate getDepthStencilStateForReference:]
+ -[PGResourceManagerDelegate getDepthStencilStateForReference:].cold.1
+ -[PGResourceManagerDelegate getFenceForReference:]
+ -[PGResourceManagerDelegate getFenceForReference:].cold.1
+ -[PGResourceManagerDelegate getFunctionForReference:]
+ -[PGResourceManagerDelegate getFunctionForReference:].cold.1
+ -[PGResourceManagerDelegate getHeapForReference:]
+ -[PGResourceManagerDelegate getHeapForReference:].cold.1
+ -[PGResourceManagerDelegate getRasterizationRateMapForReference:]
+ -[PGResourceManagerDelegate getRasterizationRateMapForReference:].cold.1
+ -[PGResourceManagerDelegate getRenderPipelineStateForReference:]
+ -[PGResourceManagerDelegate getRenderPipelineStateForReference:].cold.1
+ -[PGResourceManagerDelegate getResourceForReference:]
+ -[PGResourceManagerDelegate getSamplerStateForReference:]
+ -[PGResourceManagerDelegate getSamplerStateForReference:].cold.1
+ -[PGResourceManagerDelegate getTextureForReference:]
+ -[PGResourceManagerDelegate getTextureForReference:].cold.1
+ -[PGResourceManagerDelegate initWithResourceManager:]
+ -[PGResourceManagerDelegate newMemoryCursorForBuffer:]
+ -[PGResourceManagerDelegate textureDescriptorForDescriptor:]
+ -[PGResourceManagerDeserializationContext functionWithFunctionRef:]
+ -[PGResourceManagerDeserializationContext initWithResourceManager:]
+ -[PGRootFIFO advance]
+ -[PGRootFIFO faultOffset]
+ -[PGRootFIFO getFifoBytes:into:]
+ -[PGRootFIFO initWithDevice:length:basePointer:startOffset:lastPending:]
+ -[PGRootFIFO initWithDevice:length:basePointer:startOffset:lastPending:].cold.1
+ -[PGRootFIFO isRootFifo]
+ -[PGRootFIFO latchCommandOffset]
+ -[PGRootFIFO read]
+ -[PGRootFIFO resetPending]
+ -[PGRootFIFO reset]
+ -[PGRootFIFO setFaultOffset:]
+ -[PGRootFIFO setRead:]
+ -[PGRootFIFO setStartOffset:]
+ -[PGRootFIFO setWritten:]
+ -[PGRootFIFO setupMapping]
+ -[PGRootFIFO stampIndex]
+ -[PGRootFIFO startOffset]
+ -[PGRootFIFO teardownMapping]
+ -[PGRootFIFO written]
+ -[PGRootTaskMapping dealloc]
+ -[PGRootTaskMapping initWithVirtualAddress:length:device:]
+ -[PGRootTaskMapping initWithVirtualAddress:length:device:].cold.1
+ -[PGRootTaskMapping initWithVirtualAddress:length:device:].cold.2
+ -[PGRootTaskMapping initWithVirtualAddress:length:device:].cold.3
+ -[PGSerializerTextureResource dealloc]
+ -[PGSerializerTextureResource discard]
+ -[PGSerializerTextureResource getResource]
+ -[PGSerializerTextureResource getTexture]
+ -[PGSerializerTextureResource initWithTexture:]
+ -[PGSerializerTextureResource needsComputePaging]
+ -[PGSerializerTextureResource prepareInEncoder:]
+ -[PGSerializerTextureResource supportsDiscard]
+ -[PGSerializerTextureResource synchronizeInEncoder:]
+ -[PGSharedBufferResource dealloc]
+ -[PGSharedBufferResource discard]
+ -[PGSharedBufferResource ensurePhysical]
+ -[PGSharedBufferResource getBuffer]
+ -[PGSharedBufferResource getResource]
+ -[PGSharedBufferResource initWithTask:descriptor:placement:]
+ -[PGSharedBufferResource initWithTask:descriptor:placement:].cold.1
+ -[PGSharedBufferResource isGuestValid]
+ -[PGSharedBufferResource isHostValid]
+ -[PGSharedBufferResource needsSync]
+ -[PGSharedBufferResource prepareInEncoder:]
+ -[PGSharedBufferResource synchronizeInEncoder:]
+ -[PGSharedTextureResource dealloc]
+ -[PGSharedTextureResource discard]
+ -[PGSharedTextureResource ensurePhysical]
+ -[PGSharedTextureResource getResource]
+ -[PGSharedTextureResource getSharedTextureBackingID]
+ -[PGSharedTextureResource getTexture]
+ -[PGSharedTextureResource initWithTask:texture:sharedTextureBackingID:]
+ -[PGSharedTextureResource initWithTask:texture:sharedTextureBackingID:].cold.1
+ -[PGSharedTextureResource isGuestValid]
+ -[PGSharedTextureResource isHostValid]
+ -[PGSharedTextureResource prepareInEncoder:]
+ -[PGSharedTextureResource supportsDiscard]
+ -[PGSharedTextureResource synchronizeInEncoder:]
+ -[PGSinglePlaneSharedTextureBackingResource dealloc]
+ -[PGSinglePlaneSharedTextureBackingResource initWithTask:pagingInfo:dimension:dimensionLength:texture:]
+ -[PGSinglePlaneSharedTextureBackingResource initWithTask:pagingInfo:dimension:dimensionLength:texture:].cold.1
+ -[PGSinglePlaneSharedTextureBackingResource needsComputePaging]
+ -[PGSinglePlaneSharedTextureBackingResource newSharedTextureHandle]
+ -[PGSinglePlaneSharedTextureBackingResource pageTextureInEncoder:isDownload:]
+ -[PGSinglePlaneSharedTextureBackingResource pageTextureInEncoder:isDownload:].cold.1
+ -[PGSinglePlaneSharedTextureBackingResource prepareInEncoder:]
+ -[PGSinglePlaneSharedTextureBackingResource prepareInEncoder:].cold.1
+ -[PGSinglePlaneSharedTextureBackingResource prepareSharedTextureBacking:]
+ -[PGSinglePlaneSharedTextureBackingResource synchronizeInEncoder:]
+ -[PGSinglePlaneSharedTextureBackingResource synchronizeInEncoder:].cold.1
+ -[PGSinglePlaneTextureResource dealloc]
+ -[PGSinglePlaneTextureResource initWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:]
+ -[PGSinglePlaneTextureResource pageTextureInEncoder:isDownload:]
+ -[PGSinglePlaneTextureResource pageTextureInEncoder:isDownload:].cold.1
+ -[PGSinglePlaneTextureResource prepareInEncoder:]
+ -[PGSinglePlaneTextureResource prepareInEncoder:].cold.1
+ -[PGSinglePlaneTextureResource synchronizeInEncoder:]
+ -[PGSinglePlaneTextureResource synchronizeInEncoder:].cold.1
+ -[PGTaskMapping dealloc]
+ -[PGTaskMapping initWithVirtualOffset:length:taskInfo:device:]
+ -[PGTextureResource dealloc]
+ -[PGTextureResource devolatilize]
+ -[PGTextureResource discard]
+ -[PGTextureResource ensurePhysical]
+ -[PGTextureResource getResource]
+ -[PGTextureResource getTexture]
+ -[PGTextureResource initWithTexture:texture:]
+ -[PGTextureResource isDualPlane]
+ -[_PGDeserializer dealloc]
+ -[_PGDeserializer decodeSegmentWithHeader:withIterator:withDecoder:into:]
+ -[_PGDeserializer decodeSegments:lengths:count:into:]
+ -[_PGDeserializer deleteBufferForReference:]
+ -[_PGDeserializer deleteComputePipelineStateForReference:]
+ -[_PGDeserializer deleteDepthStencilStateForReference:]
+ -[_PGDeserializer deleteFenceForReference:]
+ -[_PGDeserializer deleteFunctionForReference:]
+ -[_PGDeserializer deleteHeapForReference:]
+ -[_PGDeserializer deleteRasterizationRateMapForReference:]
+ -[_PGDeserializer deleteRenderPipelineStateForReference:]
+ -[_PGDeserializer deleteSamplerStateForReference:]
+ -[_PGDeserializer deleteTextureForReference:]
+ -[_PGDeserializer device]
+ -[_PGDeserializer getBufferForReference:]
+ -[_PGDeserializer getBufferForReferenceNonNull:]
+ -[_PGDeserializer getComputePipelineStateForReference:]
+ -[_PGDeserializer getComputePipelineStateForReferenceNonNull:]
+ -[_PGDeserializer getDepthStencilStateForReference:]
+ -[_PGDeserializer getDepthStencilStateForReferenceNonNull:]
+ -[_PGDeserializer getFenceForReference:]
+ -[_PGDeserializer getFenceForReferenceNonNull:]
+ -[_PGDeserializer getFunctionForReference:]
+ -[_PGDeserializer getFunctionForReferenceNonNull:]
+ -[_PGDeserializer getHeapForReference:]
+ -[_PGDeserializer getHeapForReferenceNonNull:]
+ -[_PGDeserializer getRasterizationRateMapForReference:]
+ -[_PGDeserializer getRasterizationRateMapForReferenceNonNull:]
+ -[_PGDeserializer getRenderPipelineStateForReference:]
+ -[_PGDeserializer getRenderPipelineStateForReferenceNonNull:]
+ -[_PGDeserializer getResourceForReference:]
+ -[_PGDeserializer getSamplerStateForReference:]
+ -[_PGDeserializer getSamplerStateForReferenceNonNull:]
+ -[_PGDeserializer getTextureForReference:]
+ -[_PGDeserializer getTextureForReferenceNonNull:]
+ -[_PGDeserializer initWithDevice:objectDelegate:]
+ -[_PGDeserializer initWithDevice:objectDelegate:].cold.1
+ -[_PGDeserializer newMemoryCursorForBuffer:]
+ -[_PGDeserializer resetRasterizationRateMapWithSerializedData:serializedDataSize:rasterizationRateMap:]
+ -[_PGDeserializer resetRasterizationRateMapWithSerializedData:serializedDataSize:rasterizationRateMap:].cold.1
+ -[_PGDeserializer textureDescriptorForDescriptor:]
+ -[_PGDevice .cxx_construct]
+ -[_PGDevice .cxx_destruct]
+ -[_PGDevice addTraceRange:handler:]
+ -[_PGDevice addWait:waitingFor:value:]
+ -[_PGDevice addWait:waitingFor:value:].cold.1
+ -[_PGDevice addWait:waitingFor:value:].cold.2
+ -[_PGDevice addWait:waitingFor:value:].cold.3
+ -[_PGDevice addWait:waitingFor:value:].cold.4
+ -[_PGDevice attachDisplay:port:]
+ -[_PGDevice binaryVersion]
+ -[_PGDevice blitDownQueue]
+ -[_PGDevice blitInRGB_2P_XR10_A8_pipeline]
+ -[_PGDevice blitOutRGB_2P_XR10_A8_pipeline]
+ -[_PGDevice blitUpQueue]
+ -[_PGDevice checkEnableProtectedContent:]
+ -[_PGDevice checkEnableProtectedContent:].cold.1
+ -[_PGDevice checkSuspendDeviceInfo:error:]
+ -[_PGDevice checkSuspendDeviceInfo:error:].cold.1
+ -[_PGDevice createFIFO:]
+ -[_PGDevice createFIFOInternal:restoring:]
+ -[_PGDevice createFIFOInternal:restoring:].cold.1
+ -[_PGDevice createFIFOInternal:restoring:].cold.2
+ -[_PGDevice createFIFOInternal:restoring:].cold.3
+ -[_PGDevice createRootFifo]
+ -[_PGDevice createRootFifo].cold.1
+ -[_PGDevice createRootFifo].cold.2
+ -[_PGDevice createRootFifo].cold.3
+ -[_PGDevice createRootFifo].cold.4
+ -[_PGDevice createRootFifo].cold.5
+ -[_PGDevice createRootFifo].cold.6
+ -[_PGDevice createTask:taskInfo:]
+ -[_PGDevice createTaskID:taskRoot:length:restoring:]
+ -[_PGDevice dealloc]
+ -[_PGDevice deleteFIFO:]
+ -[_PGDevice deleteTaskID:]
+ -[_PGDevice destroyTask:]
+ -[_PGDevice detachDisplay:port:]
+ -[_PGDevice deviceFeatureLevel]
+ -[_PGDevice deviceTraceId]
+ -[_PGDevice didResume]
+ -[_PGDevice didResume].cold.1
+ -[_PGDevice didResume].cold.2
+ -[_PGDevice didResume].cold.3
+ -[_PGDevice didResume].cold.4
+ -[_PGDevice didResume].cold.5
+ -[_PGDevice didResume].cold.6
+ -[_PGDevice didResume].cold.7
+ -[_PGDevice displayPokePort:]
+ -[_PGDevice displayPortCount]
+ -[_PGDevice enableFifo]
+ -[_PGDevice enableFifo].cold.1
+ -[_PGDevice enableProtectedContent]
+ -[_PGDevice execQueue]
+ -[_PGDevice features]
+ -[_PGDevice fifoFaultOffset]
+ -[_PGDevice fifoForStampIndex:]
+ -[_PGDevice fifoForStampIndex:].cold.1
+ -[_PGDevice fifoForStampIndex:].cold.2
+ -[_PGDevice fifoForStampIndex:].cold.3
+ -[_PGDevice fifoForStampIndex:].cold.4
+ -[_PGDevice finishSuspend]
+ -[_PGDevice finishSuspend].cold.1
+ -[_PGDevice finishWait:]
+ -[_PGDevice getDeviceInfo:length:dst:]
+ -[_PGDevice getDisplayAtPort:]
+ -[_PGDevice getDisplayNubAtPort:]
+ -[_PGDevice getEFIModeCount]
+ -[_PGDevice getEFIModeValue]
+ -[_PGDevice getEFIStrideAlignment]
+ -[_PGDevice getKernelTask]
+ -[_PGDevice getTaskID:]
+ -[_PGDevice getUserTaskID:]
+ -[_PGDevice initWaitingInfo]
+ -[_PGDevice initWithDescriptor:]
+ -[_PGDevice initWithDescriptor:].cold.1
+ -[_PGDevice initWithDescriptor:].cold.2
+ -[_PGDevice initWithDescriptor:].cold.3
+ -[_PGDevice initWithDescriptor:].cold.4
+ -[_PGDevice initWithDescriptor:].cold.5
+ -[_PGDevice interrupt]
+ -[_PGDevice logDeviceFeatureLevel]
+ -[_PGDevice logDeviceFeatureLevel].cold.1
+ -[_PGDevice mapMemoryInTask:segmentCount:offset:readonly:ranges:]
+ -[_PGDevice mapMemoryInTask:segmentCount:offset:readonly:ranges:].cold.1
+ -[_PGDevice mapperService]
+ -[_PGDevice memoryMap]
+ -[_PGDevice mmioReadAtOffset:]
+ -[_PGDevice mmioWriteAtOffset:value:]
+ -[_PGDevice mtlDevice]
+ -[_PGDevice newContiguousMapping:length:]
+ -[_PGDevice newContiguousMapping:length:].cold.1
+ -[_PGDevice newDisplayWithDescriptor:port:serialNum:]
+ -[_PGDevice newRangeMapping:rangeCount:totalLength:readOnly:]
+ -[_PGDevice newRangeMapping:rangeCount:totalLength:readOnly:].cold.1
+ -[_PGDevice newRangeMapping:rangeCount:totalLength:readOnly:].cold.2
+ -[_PGDevice newTaskMapping:ranges:rangeCount:totalLength:offset:readOnly:]
+ -[_PGDevice newTaskMapping:ranges:rangeCount:totalLength:offset:readOnly:].cold.1
+ -[_PGDevice nextTraceID]
+ -[_PGDevice pause]
+ -[_PGDevice readFromPhysicalAddress:length:dst:]
+ -[_PGDevice readInterruptFault]
+ -[_PGDevice removeTraceRange:]
+ -[_PGDevice reportStampWaitTimeout]
+ -[_PGDevice reportStampWaitTimeout].cold.1
+ -[_PGDevice reportStampWaitTimeout].cold.2
+ -[_PGDevice reportStampWaitTimeout].cold.3
+ -[_PGDevice resetWithMemoryMap:]
+ -[_PGDevice resetWithMemoryMap:].cold.1
+ -[_PGDevice reset]
+ -[_PGDevice resumeChildFifo:]
+ -[_PGDevice resumeChildFifo:].cold.1
+ -[_PGDevice resumeChildFifo:].cold.2
+ -[_PGDevice resumeFifo]
+ -[_PGDevice ringDisplayDoorbellAtPort:]
+ -[_PGDevice ringDisplayDoorbellAtPort:].cold.1
+ -[_PGDevice runState]
+ -[_PGDevice saveState]
+ -[_PGDevice saveState].cold.1
+ -[_PGDevice serializeSuspendState]
+ -[_PGDevice setBinaryVersion:]
+ -[_PGDevice setBinaryVersion:].cold.1
+ -[_PGDevice setBinaryVersion:].cold.2
+ -[_PGDevice setEFIDisplay:]
+ -[_PGDevice setEFIFramebufferDepth:]
+ -[_PGDevice setEFIFramebufferLength:]
+ -[_PGDevice setEFIFramebufferMode:]
+ -[_PGDevice setEFIFramebufferStart:]
+ -[_PGDevice setEFIFramebufferStride:]
+ -[_PGDevice setEFIModeSelect:]
+ -[_PGDevice setFifoBasePage:]
+ -[_PGDevice setFifoBasePage:].cold.1
+ -[_PGDevice setFifoLength:]
+ -[_PGDevice setFifoLength:].cold.1
+ -[_PGDevice setFifoStart:]
+ -[_PGDevice setFifoStart:].cold.1
+ -[_PGDevice setFifoWritten:]
+ -[_PGDevice setRootPage:]
+ -[_PGDevice setRootPage:].cold.1
+ -[_PGDevice setSharedDisplayStatePage:forPort:restoring:]
+ -[_PGDevice setupBlitPipelines]
+ -[_PGDevice setupBlitPipelines].cold.1
+ -[_PGDevice setupBlitPipelines].cold.2
+ -[_PGDevice setupReporting]
+ -[_PGDevice signalFIFOs]
+ -[_PGDevice signalFaultInFIFO:]
+ -[_PGDevice signalStamp:value:]
+ -[_PGDevice signalStamp:value:].cold.1
+ -[_PGDevice stop]
+ -[_PGDevice supportsArgumentBuffers]
+ -[_PGDevice supportsBufferWithIOSurface]
+ -[_PGDevice supportsLargeKernelTasks]
+ -[_PGDevice supportsLargeUserTasks]
+ -[_PGDevice supportsRangeBuffer]
+ -[_PGDevice supportsSharedMemoryHeap]
+ -[_PGDevice supportsSharedTextures]
+ -[_PGDevice teardownDisplays]
+ -[_PGDevice teardownFifos]
+ -[_PGDevice teardownFifos].cold.1
+ -[_PGDevice teardownRoot]
+ -[_PGDevice teardownRoot].cold.1
+ -[_PGDevice teardownTasks]
+ -[_PGDevice unmap:]
+ -[_PGDevice unmap:].cold.1
+ -[_PGDevice unmap:].cold.2
+ -[_PGDevice unmapMemoryInTask:offset:length:]
+ -[_PGDevice unmapMemoryInTask:offset:length:].cold.1
+ -[_PGDevice unpause]
+ -[_PGDevice waitStamp:waitingFIFO:]
+ -[_PGDevice waitStamps:barriers:waitingFIFO:]
+ -[_PGDevice wakeFifo:]
+ -[_PGDevice wakeFifo:].cold.1
+ -[_PGDevice willResumeWithSuspendState:error:]
+ -[_PGDevice willResumeWithSuspendState:error:].cold.1
+ -[_PGDevice willResumeWithSuspendState:error:].cold.2
+ -[_PGDevice willResumeWithSuspendState:error:].cold.3
+ -[_PGDevice willSuspend]
+ -[_PGDevice willSuspend].cold.1
+ -[_PGDisplay .cxx_construct]
+ -[_PGDisplay .cxx_destruct]
+ -[_PGDisplay colorSpace]
+ -[_PGDisplay compositorParametersHandler]
+ -[_PGDisplay configEpoch]
+ -[_PGDisplay connectionType]
+ -[_PGDisplay cursorGlyphHandler2]
+ -[_PGDisplay cursorGlyphHandler]
+ -[_PGDisplay cursorMoveHandler]
+ -[_PGDisplay cursorPosition]
+ -[_PGDisplay cursorShowHandler]
+ -[_PGDisplay dealloc]
+ -[_PGDisplay encodeCurrentFrameToCommandBuffer:texture:region:]
+ -[_PGDisplay encodeRenderFrame:toDisplay:withCmdBuf:viewport:]
+ -[_PGDisplay encodeRenderFrame:toDisplay:withCmdBuf:viewport:].cold.1
+ -[_PGDisplay encodeRenderFrame:toDisplay:withCmdBuf:viewport:].cold.2
+ -[_PGDisplay guestColorSpaceDirty]
+ -[_PGDisplay guestColorSpace]
+ -[_PGDisplay guestPresentCount]
+ -[_PGDisplay hostPresentCount]
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:]
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.1
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.2
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.3
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.4
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.5
+ -[_PGDisplay initWithDevice:descriptor:port:serialNum:].cold.6
+ -[_PGDisplay internalEncodeCurrentFrameToCommandBuffer:texture:region:]
+ -[_PGDisplay maxNits]
+ -[_PGDisplay maxSDRNits]
+ -[_PGDisplay minNits]
+ -[_PGDisplay minimumTextureUsage]
+ -[_PGDisplay modeChangeHandler]
+ -[_PGDisplay modeChangeWidth:height:iosurfacePixelFormat:protectionRequirements:]
+ -[_PGDisplay modeListResponsivenessChangeHandler]
+ -[_PGDisplay modeListResponsiveness]
+ -[_PGDisplay modeList]
+ -[_PGDisplay name]
+ -[_PGDisplay newFrameEventHandler]
+ -[_PGDisplay nub]
+ -[_PGDisplay optIntoUsingUnplugMethod]
+ -[_PGDisplay origin]
+ -[_PGDisplay port]
+ -[_PGDisplay presentFrame:iosurfacePixelFormat:protectionRequirements:task:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:colorMatrix:completionBlock:]
+ -[_PGDisplay protectionOptions]
+ -[_PGDisplay protectionRequirements]
+ -[_PGDisplay queue]
+ -[_PGDisplay scaleFactor]
+ -[_PGDisplay serialNum]
+ -[_PGDisplay setGuestColorSpaceDirty:]
+ -[_PGDisplay setModeList:]
+ -[_PGDisplay setNub:]
+ -[_PGDisplay setProtectionOptions:]
+ -[_PGDisplay signalCurrentFrame]
+ -[_PGDisplay signalResponsiveness]
+ -[_PGDisplay sizeInMillimeters]
+ -[_PGDisplay sleepHandler]
+ -[_PGDisplay unplug]
+ -[_PGDisplay updateColorMatrix:]
+ -[_PGDisplay updateGammaSlopesRedSlopeAtZero:greenSlopeAtZero:blueSlopeAtZero:redSlopeAtOne:greenSlopeAtOne:blueSlopeAtOne:]
+ -[_PGDisplay updateGammaTable:virtualOffset:mappedLength:entryCount:sum:]
+ -[_PGDisplay updateGammaTable:virtualOffset:mappedLength:entryCount:sum:].cold.1
+ -[_PGDisplay updateGammaTable:virtualOffset:mappedLength:entryCount:sum:].cold.2
+ -[_PGDisplay updateResponsiveness]
+ -[_PGDisplay waitForPendingFrames:]
+ -[_PGDisplay waitForPendingFrames:].cold.1
+ -[_PGDisplayNub .cxx_construct]
+ -[_PGDisplayNub .cxx_destruct]
+ -[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:]
+ -[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:].cold.1
+ -[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:].cold.2
+ -[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:].cold.3
+ -[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:].cold.4
+ -[_PGDisplayNub _cursorShow:]
+ -[_PGDisplayNub _cursorShow:].cold.1
+ -[_PGDisplayNub _presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]
+ -[_PGDisplayNub _presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:].cold.1
+ -[_PGDisplayNub _presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:].cold.2
+ -[_PGDisplayNub _presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]
+ -[_PGDisplayNub _presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:].cold.1
+ -[_PGDisplayNub _presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:].cold.2
+ -[_PGDisplayNub _sleepState:]
+ -[_PGDisplayNub _sleepState:].cold.1
+ -[_PGDisplayNub ack:]
+ -[_PGDisplayNub client]
+ -[_PGDisplayNub compositorParametersConfigEpoch:origin:scaleFactor:]
+ -[_PGDisplayNub compositorSupportsLiveResize]
+ -[_PGDisplayNub copy_GuestBGRA_ToHostBGRA_Task:virtualOffset:mappedLength:stride:buffer:width:height:sum:]
+ -[_PGDisplayNub copy_GuestBGRA_toHostRGBA_Task:virtualOffset:mappedLength:stride:buffer:width:height:sum:]
+ -[_PGDisplayNub cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:]
+ -[_PGDisplayNub cursorPosition]
+ -[_PGDisplayNub cursorShow:]
+ -[_PGDisplayNub dealloc]
+ -[_PGDisplayNub delayFrames:]
+ -[_PGDisplayNub delayFrames:].cold.1
+ -[_PGDisplayNub doorbell]
+ -[_PGDisplayNub finishRestore]
+ -[_PGDisplayNub finishRestore].cold.1
+ -[_PGDisplayNub getDirtyColorMatrix]
+ -[_PGDisplayNub getDirtyColorMatrix].cold.1
+ -[_PGDisplayNub guestColorSpace]
+ -[_PGDisplayNub initWithDevice:port:sharedStatePage:]
+ -[_PGDisplayNub modeList]
+ -[_PGDisplayNub pause]
+ -[_PGDisplayNub presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]
+ -[_PGDisplayNub presentSurface:]
+ -[_PGDisplayNub presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]
+ -[_PGDisplayNub protectionOptions]
+ -[_PGDisplayNub setClient:]
+ -[_PGDisplayNub setGammaTableVirtualOffset:mappedLength:entryCount:sum:]
+ -[_PGDisplayNub setGammaTableVirtualOffset:mappedLength:entryCount:sum:].cold.1
+ -[_PGDisplayNub setGuestICCProfileLength:virtualOffset:]
+ -[_PGDisplayNub setModeList:]
+ -[_PGDisplayNub setProperty:value:wordCount:]
+ -[_PGDisplayNub setProtectionOptions:]
+ -[_PGDisplayNub setProtectionOptions:].cold.1
+ -[_PGDisplayNub sharedState]
+ -[_PGDisplayNub sharedState].cold.1
+ -[_PGDisplayNub sleepState:]
+ -[_PGDisplayNub stateMachineWithCaller:]
+ -[_PGDisplayNub testUpdateModeList:]
+ -[_PGDisplayNub testUpdateModeList:].cold.1
+ -[_PGDisplayNub testUpdateModeList:].cold.2
+ -[_PGDisplayNub testUpdateModeList:].cold.3
+ -[_PGDisplayNub testUpdateSettings:]
+ -[_PGDisplayNub testUpdateSettings:].cold.1
+ -[_PGDisplayNub testUpdateSettings:].cold.2
+ -[_PGDisplayNub unpause]
+ -[_PGDisplayNub updateGuestColorSpace]
+ -[_PGDisplayNub willRestore]
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table11
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table13
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table14
+ GCC_except_table146
+ GCC_except_table15
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table162
+ GCC_except_table169
+ GCC_except_table17
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table186
+ GCC_except_table19
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table276
+ GCC_except_table279
+ GCC_except_table28
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table29
+ GCC_except_table291
+ GCC_except_table296
+ GCC_except_table3
+ GCC_except_table30
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table31
+ GCC_except_table311
+ GCC_except_table316
+ GCC_except_table32
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table33
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table34
+ GCC_except_table342
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table349
+ GCC_except_table35
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table36
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table9
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ OBJC_IVAR_$_PGBackingResource._backingAllocationLength
+ OBJC_IVAR_$_PGBackingResource._backingVirtualPage
+ OBJC_IVAR_$_PGBackingResource._ioSurface
+ OBJC_IVAR_$_PGBackingResource._planeCount
+ OBJC_IVAR_$_PGBackingResource._planes
+ OBJC_IVAR_$_PGBackingResource._task
+ OBJC_IVAR_$_PGBackingResource._textures
+ OBJC_IVAR_$_PGBackingResource._transferBuffer
+ OBJC_IVAR_$_PGBaseTask._objectListCount
+ OBJC_IVAR_$_PGBaseTask._objectListManager
+ OBJC_IVAR_$_PGBaseTask._resourceManager
+ OBJC_IVAR_$_PGChildFIFO._baseNode
+ OBJC_IVAR_$_PGChildFIFO._basePointer
+ OBJC_IVAR_$_PGChildFIFO._cacheWritten
+ OBJC_IVAR_$_PGChildFIFO._cmdStart
+ OBJC_IVAR_$_PGChildFIFO._faultOffset
+ OBJC_IVAR_$_PGChildFIFO._lastReadCount
+ OBJC_IVAR_$_PGChildFIFO._lastReadOffset
+ OBJC_IVAR_$_PGChildFIFO._readCount
+ OBJC_IVAR_$_PGChildFIFO._readOffset
+ OBJC_IVAR_$_PGChildFIFO._stampIndex
+ OBJC_IVAR_$_PGDeserializerBlitDecoder._blitEncoder
+ OBJC_IVAR_$_PGDeserializerBlitDecoder._deserializer
+ OBJC_IVAR_$_PGDeserializerComputeDecoder._commandBuffer
+ OBJC_IVAR_$_PGDeserializerComputeDecoder._computeEncoder
+ OBJC_IVAR_$_PGDeserializerComputeDecoder._computePipeline
+ OBJC_IVAR_$_PGDeserializerComputeDecoder._deserializer
+ OBJC_IVAR_$_PGDeserializerInfoDecoder._deserializer
+ OBJC_IVAR_$_PGDeserializerRenderDecoder._commandBuffer
+ OBJC_IVAR_$_PGDeserializerRenderDecoder._deserializer
+ OBJC_IVAR_$_PGDeserializerRenderDecoder._maxColorAttachmentIndex
+ OBJC_IVAR_$_PGDeserializerRenderDecoder._pipelineState
+ OBJC_IVAR_$_PGDeserializerRenderDecoder._renderEncoder
+ OBJC_IVAR_$_PGDetachBufferResource._buffer
+ OBJC_IVAR_$_PGDetachBufferResource._bufferLength
+ OBJC_IVAR_$_PGDetachBufferResource._bufferVirtualPage
+ OBJC_IVAR_$_PGDetachBufferResource._isDetached
+ OBJC_IVAR_$_PGDetachBufferResource._isReadOnly
+ OBJC_IVAR_$_PGDetachBufferResource._task
+ OBJC_IVAR_$_PGDetachHeapResource._dummyAllocation
+ OBJC_IVAR_$_PGDetachHeapResource._heap
+ OBJC_IVAR_$_PGDetachHeapResource._heapLength
+ OBJC_IVAR_$_PGDetachHeapResource._heapVirtualPage
+ OBJC_IVAR_$_PGDetachHeapResource._isDetached
+ OBJC_IVAR_$_PGDetachHeapResource._isReadOnly
+ OBJC_IVAR_$_PGDetachHeapResource._isTracked
+ OBJC_IVAR_$_PGDetachHeapResource._task
+ OBJC_IVAR_$_PGDeviceDescriptor._deviceFeatureLevel
+ OBJC_IVAR_$_PGDeviceDescriptor._enableArgumentBuffers
+ OBJC_IVAR_$_PGDeviceDescriptor._enableProcessIsolation
+ OBJC_IVAR_$_PGDeviceDescriptor._enableProtectedContent
+ OBJC_IVAR_$_PGDeviceDescriptor._memoryMapDescriptor
+ OBJC_IVAR_$_PGDeviceDescriptor._usingIOSurfaceMapper
+ OBJC_IVAR_$_PGDeviceDescriptor.addTraceRange
+ OBJC_IVAR_$_PGDeviceDescriptor.createTask
+ OBJC_IVAR_$_PGDeviceDescriptor.destroyTask
+ OBJC_IVAR_$_PGDeviceDescriptor.device
+ OBJC_IVAR_$_PGDeviceDescriptor.displayPortCount
+ OBJC_IVAR_$_PGDeviceDescriptor.mapMemory
+ OBJC_IVAR_$_PGDeviceDescriptor.mmioLength
+ OBJC_IVAR_$_PGDeviceDescriptor.raiseInterrupt
+ OBJC_IVAR_$_PGDeviceDescriptor.readMemory
+ OBJC_IVAR_$_PGDeviceDescriptor.removeTraceRange
+ OBJC_IVAR_$_PGDeviceDescriptor.unmapMemory
+ OBJC_IVAR_$_PGDisplayDescriptor._colorSpace
+ OBJC_IVAR_$_PGDisplayDescriptor._compositorParametersHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._configEpoch
+ OBJC_IVAR_$_PGDisplayDescriptor._connectionType
+ OBJC_IVAR_$_PGDisplayDescriptor._cursorGlyphHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._cursorGlyphHandler2
+ OBJC_IVAR_$_PGDisplayDescriptor._cursorMoveHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._cursorShowHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._maxNits
+ OBJC_IVAR_$_PGDisplayDescriptor._maxSDRNits
+ OBJC_IVAR_$_PGDisplayDescriptor._minNits
+ OBJC_IVAR_$_PGDisplayDescriptor._modeChangeHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._modeListResponsivenessChangeHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._name
+ OBJC_IVAR_$_PGDisplayDescriptor._newFrameEventHandler
+ OBJC_IVAR_$_PGDisplayDescriptor._optIntoUsingUnplugMethod
+ OBJC_IVAR_$_PGDisplayDescriptor._origin
+ OBJC_IVAR_$_PGDisplayDescriptor._queue
+ OBJC_IVAR_$_PGDisplayDescriptor._scaleFactor
+ OBJC_IVAR_$_PGDisplayDescriptor._sizeInMillimeters
+ OBJC_IVAR_$_PGDisplayDescriptor._sleepHandler
+ OBJC_IVAR_$_PGDisplayMode._refreshRate
+ OBJC_IVAR_$_PGDisplayMode._refreshRateInHz
+ OBJC_IVAR_$_PGDisplayMode._sizeInPixels
+ OBJC_IVAR_$_PGDisplayMode._supports10bpc
+ OBJC_IVAR_$_PGDisplayMode._supportsEDR
+ OBJC_IVAR_$_PGDisplayPipelineCache._fragmentFunction
+ OBJC_IVAR_$_PGDisplayPipelineCache._fragmentFunctionGammaColorMatrix
+ OBJC_IVAR_$_PGDisplayPipelineCache._mtlDevice
+ OBJC_IVAR_$_PGDisplayPipelineCache._table
+ OBJC_IVAR_$_PGDisplayPipelineCache._vertexFunction
+ OBJC_IVAR_$_PGDisplayPipelineDescriptor.hasGamma
+ OBJC_IVAR_$_PGDisplayPipelineDescriptor.renderTargetPixelFormat
+ OBJC_IVAR_$_PGDualPlaneBlitTextureResource._planes
+ OBJC_IVAR_$_PGDualPlaneComputeTextureResource._blitDownState
+ OBJC_IVAR_$_PGDualPlaneComputeTextureResource._blitUpState
+ OBJC_IVAR_$_PGDualPlaneComputeTextureResource._planeTextureFormats
+ OBJC_IVAR_$_PGDualPlaneComputeTextureResource._planeTextures
+ OBJC_IVAR_$_PGDualPlaneComputeTextureResource._planes
+ OBJC_IVAR_$_PGDualPlaneSharedTextureBackingResource._planes
+ OBJC_IVAR_$_PGEFIDisplay._currentHeight
+ OBJC_IVAR_$_PGEFIDisplay._currentModeIndex
+ OBJC_IVAR_$_PGEFIDisplay._currentWidth
+ OBJC_IVAR_$_PGEFIDisplay._device
+ OBJC_IVAR_$_PGEFIDisplay._display
+ OBJC_IVAR_$_PGEFIDisplay._efiMapping
+ OBJC_IVAR_$_PGEFIDisplay._efiTaskInfo
+ OBJC_IVAR_$_PGEFIDisplay._framebufferDepth
+ OBJC_IVAR_$_PGEFIDisplay._framebufferLength
+ OBJC_IVAR_$_PGEFIDisplay._framebufferMode
+ OBJC_IVAR_$_PGEFIDisplay._framebufferStartPage
+ OBJC_IVAR_$_PGEFIDisplay._framebufferStride
+ OBJC_IVAR_$_PGEFIDisplay._mapped
+ OBJC_IVAR_$_PGEFIDisplay._mappedLength
+ OBJC_IVAR_$_PGEFIDisplay._presentQueue
+ OBJC_IVAR_$_PGEFIDisplay._presentSource
+ OBJC_IVAR_$_PGEFIDisplay._presentTimer
+ OBJC_IVAR_$_PGEFIDisplay._taskReady
+ OBJC_IVAR_$_PGEFIDisplay._texture
+ OBJC_IVAR_$_PGEFIDisplay._totalFramebufferSize
+ OBJC_IVAR_$_PGEFIDisplay._traceRange
+ OBJC_IVAR_$_PGEFIDisplay._usingTextureFromBytes
+ OBJC_IVAR_$_PGFIFO._running
+ OBJC_IVAR_$_PGHeapBufferResource._buffer
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._descriptorPageCount
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._descriptorPages
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._descriptorTableEntries
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._descriptorTableMapping
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._descriptorsPerPage
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._hostData
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._hostedOnlyAllocated
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._hwQueue
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._hwWakeSource
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._memoryMap
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._mmioLength
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._raiseInterrupt
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._ring
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._ringLength
+ OBJC_IVAR_$_PGIOSurfaceHostDevice._ringMapping
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_descEnable
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_descriptorBase
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_ringBase
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_ringRdCounter
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_ringSize
+ OBJC_IVAR_$_PGIOSurfaceHostDevice.reg_ringWrCounter
+ OBJC_IVAR_$_PGIOSurfaceHostDeviceDescriptor._memoryMapDescriptor
+ OBJC_IVAR_$_PGIOSurfaceHostDeviceDescriptor._mmioLength
+ OBJC_IVAR_$_PGIOSurfaceHostDeviceDescriptor._raiseInterrupt
+ OBJC_IVAR_$_PGLegacyHeapResource._heap
+ OBJC_IVAR_$_PGLegacyHeapResource._heapVirtualPage
+ OBJC_IVAR_$_PGLegacyHeapResource._isPrivate
+ OBJC_IVAR_$_PGLegacyHeapResource._length
+ OBJC_IVAR_$_PGLegacyHeapResource._task
+ OBJC_IVAR_$_PGLegacyHeapResource._transferBuffer
+ OBJC_IVAR_$_PGLegacyHeapResource._transferHeapBuffer
+ OBJC_IVAR_$_PGLocalTask._backingsFromMapperAllowed
+ OBJC_IVAR_$_PGLocalTask._blitIn2pXR10State
+ OBJC_IVAR_$_PGLocalTask._blitOut2pXR10State
+ OBJC_IVAR_$_PGLocalTask._device
+ OBJC_IVAR_$_PGLocalTask._dualPlaneAllowed
+ OBJC_IVAR_$_PGLocalTask._ioSurfaceBuffersAllowed
+ OBJC_IVAR_$_PGLocalTask._length
+ OBJC_IVAR_$_PGLocalTask._mappedRange
+ OBJC_IVAR_$_PGLocalTask._objectListCount
+ OBJC_IVAR_$_PGLocalTask._pageTableIterator
+ OBJC_IVAR_$_PGLocalTask._prepareMutex
+ OBJC_IVAR_$_PGLocalTask._taskID
+ OBJC_IVAR_$_PGLocalTask._taskInfo
+ OBJC_IVAR_$_PGLocalTask._taskRoot
+ OBJC_IVAR_$_PGLocalTask._taskRootMapping
+ OBJC_IVAR_$_PGLocalTask._usingMemoryMap
+ OBJC_IVAR_$_PGMapperRefBufferResource._buffer
+ OBJC_IVAR_$_PGMapperRefBufferResource._mappingID
+ OBJC_IVAR_$_PGMapperRefBufferResource._task
+ OBJC_IVAR_$_PGMapperRefTextureResource._mappingID
+ OBJC_IVAR_$_PGMapperRefTextureResource._task
+ OBJC_IVAR_$_PGMapperRefTextureResource._texture
+ OBJC_IVAR_$_PGMappingTask._baseAddress
+ OBJC_IVAR_$_PGMappingTask._memoryMap
+ OBJC_IVAR_$_PGMappingTask._size
+ OBJC_IVAR_$_PGMemoryMap._ranges
+ OBJC_IVAR_$_PGMemoryMap._segments
+ OBJC_IVAR_$_PGMemoryMapDescriptor._ranges
+ OBJC_IVAR_$_PGMemoryMapSegment._fromCoder
+ OBJC_IVAR_$_PGMemoryMapSegment._physicalAddress
+ OBJC_IVAR_$_PGMemoryMapSegment._physicalLength
+ OBJC_IVAR_$_PGMemoryMapSegment._shmem
+ OBJC_IVAR_$_PGMemoryMapSegment._virtualAddress
+ OBJC_IVAR_$_PGPageTableIterator._allowHoles
+ OBJC_IVAR_$_PGPageTableIterator._depth
+ OBJC_IVAR_$_PGPageTableIterator._device
+ OBJC_IVAR_$_PGPageTableIterator._read
+ OBJC_IVAR_$_PGPageTableIterator._root
+ OBJC_IVAR_$_PGPrivateBufferResource._buffer
+ OBJC_IVAR_$_PGPrivateBufferResource._bufferLength
+ OBJC_IVAR_$_PGPrivateBufferResource._bufferVirtualPage
+ OBJC_IVAR_$_PGPrivateBufferResource._task
+ OBJC_IVAR_$_PGPrivateBufferResource._transferBuffer
+ OBJC_IVAR_$_PGRefTextureResource._backing
+ OBJC_IVAR_$_PGRefTextureResource._texture
+ OBJC_IVAR_$_PGRemoteTask._delegate
+ OBJC_IVAR_$_PGRemoteTask._exportedDelegate
+ OBJC_IVAR_$_PGRemoteTask._lastFifoEvent
+ OBJC_IVAR_$_PGRemoteTask._service
+ OBJC_IVAR_$_PGRemoteTask._setStampIndices
+ OBJC_IVAR_$_PGRemoteTask._taskID
+ OBJC_IVAR_$_PGRemoteTask._taskPid
+ OBJC_IVAR_$_PGRemoteTaskDeviceDelegate._async
+ OBJC_IVAR_$_PGRemoteTaskDeviceDelegate._device
+ OBJC_IVAR_$_PGRemoteTaskDeviceDelegate._mutex
+ OBJC_IVAR_$_PGRemoteTaskDeviceDelegate._surfaces
+ OBJC_IVAR_$_PGResource._needsComputePaging
+ OBJC_IVAR_$_PGResourceManagerDelegate._resourceManager
+ OBJC_IVAR_$_PGResourceManagerDeserializationContext._resourceManager
+ OBJC_IVAR_$_PGRootFIFO._basePointer
+ OBJC_IVAR_$_PGRootFIFO._cmdStart
+ OBJC_IVAR_$_PGRootFIFO._faultOffset
+ OBJC_IVAR_$_PGRootFIFO._lastReadOffset
+ OBJC_IVAR_$_PGRootFIFO._pendingAdvance
+ OBJC_IVAR_$_PGRootFIFO._read
+ OBJC_IVAR_$_PGRootFIFO._readOffset
+ OBJC_IVAR_$_PGRootFIFO._startOffset
+ OBJC_IVAR_$_PGRootFIFO._written
+ OBJC_IVAR_$_PGRootTaskMapping._device
+ OBJC_IVAR_$_PGSerializerTextureResource._texture
+ OBJC_IVAR_$_PGSharedBufferResource._buffer
+ OBJC_IVAR_$_PGSharedBufferResource._bufferLength
+ OBJC_IVAR_$_PGSharedBufferResource._bufferVirtualPage
+ OBJC_IVAR_$_PGSharedBufferResource._task
+ OBJC_IVAR_$_PGSharedTextureResource._sharedTextureBackingID
+ OBJC_IVAR_$_PGSharedTextureResource._texture
+ OBJC_IVAR_$_PGSinglePlaneSharedTextureBackingResource._blitOption
+ OBJC_IVAR_$_PGSinglePlaneSharedTextureBackingResource._dimension
+ OBJC_IVAR_$_PGSinglePlaneTextureResource._blitOption
+ OBJC_IVAR_$_PGSinglePlaneTextureResource._dimension
+ OBJC_IVAR_$_PGSinglePlaneTextureResource._generateMipmaps
+ OBJC_IVAR_$_PGTaskMapping._device
+ OBJC_IVAR_$_PGTaskMapping._task
+ OBJC_IVAR_$_PGTaskMapping._virtualOffset
+ OBJC_IVAR_$_PGTextureResource._isDualPlane
+ OBJC_IVAR_$__PGDeserializer._device
+ OBJC_IVAR_$__PGDeserializer._eventListener
+ OBJC_IVAR_$__PGDeserializer._objectDelegate
+ OBJC_IVAR_$__PGDevice._addTraceRange
+ OBJC_IVAR_$__PGDevice._binaryVersion
+ OBJC_IVAR_$__PGDevice._blitDownQueue
+ OBJC_IVAR_$__PGDevice._blitInRGB_2P_XR10_A8_pipeline
+ OBJC_IVAR_$__PGDevice._blitOutRGB_2P_XR10_A8_pipeline
+ OBJC_IVAR_$__PGDevice._blitUpQueue
+ OBJC_IVAR_$__PGDevice._childFIFOs
+ OBJC_IVAR_$__PGDevice._createTask
+ OBJC_IVAR_$__PGDevice._destroyTask
+ OBJC_IVAR_$__PGDevice._deviceFeatureLevel
+ OBJC_IVAR_$__PGDevice._displayClient
+ OBJC_IVAR_$__PGDevice._displayMutex
+ OBJC_IVAR_$__PGDevice._displayNub
+ OBJC_IVAR_$__PGDevice._displayPortBusyMask
+ OBJC_IVAR_$__PGDevice._displayPortCount
+ OBJC_IVAR_$__PGDevice._efi
+ OBJC_IVAR_$__PGDevice._efiDisplay
+ OBJC_IVAR_$__PGDevice._enableProcessIsolation
+ OBJC_IVAR_$__PGDevice._enableProtectedContent
+ OBJC_IVAR_$__PGDevice._execQueue
+ OBJC_IVAR_$__PGDevice._features
+ OBJC_IVAR_$__PGDevice._fifo
+ OBJC_IVAR_$__PGDevice._fifoQueue
+ OBJC_IVAR_$__PGDevice._guestDeviceInfoMaxKey
+ OBJC_IVAR_$__PGDevice._interruptDisplay
+ OBJC_IVAR_$__PGDevice._interruptFaultMask
+ OBJC_IVAR_$__PGDevice._interruptStamp
+ OBJC_IVAR_$__PGDevice._mapMemory
+ OBJC_IVAR_$__PGDevice._mapperService
+ OBJC_IVAR_$__PGDevice._memoryMap
+ OBJC_IVAR_$__PGDevice._mtlDevice
+ OBJC_IVAR_$__PGDevice._raiseInterrupt
+ OBJC_IVAR_$__PGDevice._readMemory
+ OBJC_IVAR_$__PGDevice._readPage
+ OBJC_IVAR_$__PGDevice._removeTraceRange
+ OBJC_IVAR_$__PGDevice._reportStampWaitTimeoutSource
+ OBJC_IVAR_$__PGDevice._reportingQueue
+ OBJC_IVAR_$__PGDevice._rootFIFO
+ OBJC_IVAR_$__PGDevice._rootFIFOMapping
+ OBJC_IVAR_$__PGDevice._rootNode
+ OBJC_IVAR_$__PGDevice._rootNodeMapping
+ OBJC_IVAR_$__PGDevice._rootPageNumber
+ OBJC_IVAR_$__PGDevice._rootTask
+ OBJC_IVAR_$__PGDevice._rootTaskAllocator
+ OBJC_IVAR_$__PGDevice._rootTaskAllocatorMutex
+ OBJC_IVAR_$__PGDevice._rootTaskBase
+ OBJC_IVAR_$__PGDevice._rootTaskMutex
+ OBJC_IVAR_$__PGDevice._runState
+ OBJC_IVAR_$__PGDevice._signalCond
+ OBJC_IVAR_$__PGDevice._signalMutex
+ OBJC_IVAR_$__PGDevice._stampMemory
+ OBJC_IVAR_$__PGDevice._supportsArgumentBuffers
+ OBJC_IVAR_$__PGDevice._supportsBufferWithIOSurface
+ OBJC_IVAR_$__PGDevice._supportsLargeKernelTasks
+ OBJC_IVAR_$__PGDevice._supportsLargeUserTasks
+ OBJC_IVAR_$__PGDevice._supportsRangeBuffer
+ OBJC_IVAR_$__PGDevice._supportsResourceDetachBacking
+ OBJC_IVAR_$__PGDevice._supportsSharedMemoryHeap
+ OBJC_IVAR_$__PGDevice._supportsSharedTextures
+ OBJC_IVAR_$__PGDevice._taskFifoDeleted
+ OBJC_IVAR_$__PGDevice._taskMutex
+ OBJC_IVAR_$__PGDevice._tasks
+ OBJC_IVAR_$__PGDevice._tearingDownRoot
+ OBJC_IVAR_$__PGDevice._unmapMemory
+ OBJC_IVAR_$__PGDevice._usingMapperService
+ OBJC_IVAR_$__PGDevice._waitingInfo
+ OBJC_IVAR_$__PGDevice._waitingStamps
+ OBJC_IVAR_$__PGDevice.deviceTraceId
+ OBJC_IVAR_$__PGDisplay._attached
+ OBJC_IVAR_$__PGDisplay._colorSpace
+ OBJC_IVAR_$__PGDisplay._compositorParametersHandler
+ OBJC_IVAR_$__PGDisplay._configEpoch
+ OBJC_IVAR_$__PGDisplay._connectionType
+ OBJC_IVAR_$__PGDisplay._currentFrame
+ OBJC_IVAR_$__PGDisplay._currentFrameEncoded
+ OBJC_IVAR_$__PGDisplay._cursorGlyphHandler
+ OBJC_IVAR_$__PGDisplay._cursorGlyphHandler2
+ OBJC_IVAR_$__PGDisplay._cursorMoveHandler
+ OBJC_IVAR_$__PGDisplay._cursorShowHandler
+ OBJC_IVAR_$__PGDisplay._device
+ OBJC_IVAR_$__PGDisplay._displayMutex
+ OBJC_IVAR_$__PGDisplay._fragShaderProperties
+ OBJC_IVAR_$__PGDisplay._fragShaderPropertyBuf
+ OBJC_IVAR_$__PGDisplay._gammaTableTex
+ OBJC_IVAR_$__PGDisplay._guestColorSpace
+ OBJC_IVAR_$__PGDisplay._guestColorSpaceDirty
+ OBJC_IVAR_$__PGDisplay._guestPresentCount
+ OBJC_IVAR_$__PGDisplay._height
+ OBJC_IVAR_$__PGDisplay._hostPresentCount
+ OBJC_IVAR_$__PGDisplay._inFlightCondition
+ OBJC_IVAR_$__PGDisplay._inFlightFrameCount
+ OBJC_IVAR_$__PGDisplay._iosurfacePixelFormat
+ OBJC_IVAR_$__PGDisplay._maxNits
+ OBJC_IVAR_$__PGDisplay._maxSDRNits
+ OBJC_IVAR_$__PGDisplay._minNits
+ OBJC_IVAR_$__PGDisplay._minimumTextureUsage
+ OBJC_IVAR_$__PGDisplay._modeChangeHandler
+ OBJC_IVAR_$__PGDisplay._modeList
+ OBJC_IVAR_$__PGDisplay._modeListResponsiveness
+ OBJC_IVAR_$__PGDisplay._modeListResponsivenessChangeHandler
+ OBJC_IVAR_$__PGDisplay._mtlDevice
+ OBJC_IVAR_$__PGDisplay._name
+ OBJC_IVAR_$__PGDisplay._newFrameEventHandler
+ OBJC_IVAR_$__PGDisplay._newFrameEventSource
+ OBJC_IVAR_$__PGDisplay._nub
+ OBJC_IVAR_$__PGDisplay._nubMutex
+ OBJC_IVAR_$__PGDisplay._optIntoUsingUnplugMethod
+ OBJC_IVAR_$__PGDisplay._origin
+ OBJC_IVAR_$__PGDisplay._port
+ OBJC_IVAR_$__PGDisplay._posBuf
+ OBJC_IVAR_$__PGDisplay._protectionOptions
+ OBJC_IVAR_$__PGDisplay._protectionRequirements
+ OBJC_IVAR_$__PGDisplay._queue
+ OBJC_IVAR_$__PGDisplay._renderPipelineCache
+ OBJC_IVAR_$__PGDisplay._renderPipelineDescriptor
+ OBJC_IVAR_$__PGDisplay._reservedSerialNum
+ OBJC_IVAR_$__PGDisplay._scaleFactor
+ OBJC_IVAR_$__PGDisplay._serialNum
+ OBJC_IVAR_$__PGDisplay._sizeInMillimeters
+ OBJC_IVAR_$__PGDisplay._sleepHandler
+ OBJC_IVAR_$__PGDisplay._texBuf
+ OBJC_IVAR_$__PGDisplay._vtxCount
+ OBJC_IVAR_$__PGDisplay._width
+ OBJC_IVAR_$__PGDisplayNub._asleep
+ OBJC_IVAR_$__PGDisplayNub._client
+ OBJC_IVAR_$__PGDisplayNub._compositorSupportsLiveResize
+ OBJC_IVAR_$__PGDisplayNub._device
+ OBJC_IVAR_$__PGDisplayNub._didRestore
+ OBJC_IVAR_$__PGDisplayNub._frameDelayCount
+ OBJC_IVAR_$__PGDisplayNub._frameDelaySema
+ OBJC_IVAR_$__PGDisplayNub._guestColorSpace
+ OBJC_IVAR_$__PGDisplayNub._guestColorSpaceDirty
+ OBJC_IVAR_$__PGDisplayNub._modeList
+ OBJC_IVAR_$__PGDisplayNub._nubMutex
+ OBJC_IVAR_$__PGDisplayNub._paused
+ OBJC_IVAR_$__PGDisplayNub._port
+ OBJC_IVAR_$__PGDisplayNub._sharedState
+ OBJC_IVAR_$__PGDisplayNub._sharedStateMapping
+ OBJC_IVAR_$__PGDisplayNub._sharedStatePage
+ OBJC_IVAR_$__PGDisplayNub._willRestore
+ _OBJC_CLASS_$_PGDiscardableHeapBufferResource
+ _OBJC_CLASS_$_PGDiscardableSerializerTextureResource
+ _OBJC_CLASS_$_PGResourceManagerDelegate
+ _OBJC_CLASS_$_PGResourceManagerDeserializationContext
+ _OBJC_METACLASS_$_PGDiscardableHeapBufferResource
+ _OBJC_METACLASS_$_PGDiscardableSerializerTextureResource
+ _OBJC_METACLASS_$_PGResourceManagerDelegate
+ _OBJC_METACLASS_$_PGResourceManagerDeserializationContext
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _Z17newFunctionWithIRPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEE5PGPtrIP6NSDataE.cold.1
+ _Z19newIOSurfaceTextureP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z24newTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z25newTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.1
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.2
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.3
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.4
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.5
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.6
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.7
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.8
+ _Z27validateIOSurfaceDescriptorPU23objcproto12MTLDeviceSPI11objc_objectP20MTLTextureDescriptorP11__IOSurfacet.cold.9
+ _Z28newSerializerTextureWithHeapP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z29newSamplerStateWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement.cold.1
+ _Z30newSharedTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z31newIOSurfaceTextureWithRotationP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z31newSharedTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z33newRasterizationRateMapDescriptorP41PGOperationRasterizationRateMapDescriptorNSt3__110shared_ptrI21PGVirtualMemoryCursorEE.cold.1
+ _Z34newSerializerTextureViewWithBufferP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z34newSerializerTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z35newSerializerTextureViewWithSwizzleP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z35newSerializerTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z37newComputePipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement.cold.1
+ _Z39newSerializerTextureViewWithPixelFormatP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z39newSerializerTextureViewWithTextureTypeP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement.cold.1
+ _Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement.cold.1
+ _ZN17PGResourceManager12deleteObjectEPKvm.cold.1
+ _ZN17PGResourceManager14flushResourcesEv.cold.1
+ _ZN17PGResourceManager14flushResourcesEv.cold.2
+ _ZN17PGResourceManager14registerObjectIP10PGResourceEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU18objcproto8MTLFence11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU22objcproto11MTLFunction11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU26objcproto15MTLSamplerState11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU31objcproto20MTLDepthStencilState11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU34objcproto23MTLComputePipelineState11objc_objectEEbjT_.cold.1
+ _ZN17PGResourceManager14registerObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEEbjT_.cold.1
+ _ZN19PGObjectListManager13setObjectListEyjyjP12APVTaskRoot2.cold.1
+ _ZN19PGObjectListManager13setObjectListEyjyjP12APVTaskRoot2.cold.2
+ _ZN19PGPendingStampQueue15resumeFromFaultEv.cold.1
+ _ZN20PGMappedRangeTracker13removeAtIndexEj.cold.1
+ _ZN20PGMappedRangeTracker13removeAtIndexEj.cold.2
+ _ZN20PGMappedRangeTracker7compactEv.cold.1
+ _ZN20PGMappedRangeTracker7compactEv.cold.2
+ _ZN20PGMappedRangeTracker8RunBlock13insertAtIndexEjRKNS_3RunE.cold.1
+ _ZN20PGMappedRangeTracker8RunBlock13removeAtIndexEjj.cold.1
+ _ZN20PGMappedRangeTracker8RunBlock3addERKNS_3RunE.cold.1
+ _ZN20PGMappedRangeTracker8RunBlock5splitEv.cold.1
+ _ZN20PGMappedRangeTracker8RunBlock5splitEv.cold.2
+ _ZN20PGMappedRangeTracker8RunBlock6removeERKNS_3RunE.cold.1
+ _ZN20PGMappedRangeTracker8RunBlock6removeERKNS_3RunE.cold.2
+ _ZN25PGLegacyObjectListManager13mapObjectListEv.cold.1
+ _ZN28PGMemoryMapObjectListManager13mapObjectListEv.cold.1
+ _ZN28PGMemoryMapObjectListManager16mapPlacementListEv.cold.1
+ _ZNK20PGMappedRangeTracker3Run7compareERKS0_.cold.1
+ _ZNK26PGSuspendStateSerialized_t10validateV1EyPP7NSError.cold.1
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.1
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.2
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.3
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.4
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.5
+ _ZNK26PGSuspendStateSerialized_t10validateV2EyPP7NSError.cold.6
+ _ZNK26PGSuspendStateSerialized_t11checkLengthEmPyPP7NSError.cold.1
+ _ZNK26PGSuspendStateSerialized_t19getDeviceInfoMaxKeyEv.cold.1
+ _ZNK26PGSuspendStateSerialized_t21locateDeviceInfoPairsEv.cold.1
+ _ZNK26PGSuspendStateSerialized_t8validateEyPP7NSError.cold.1
+ _ZNK26PGSuspendStateSerialized_t8validateEyPP7NSError.cold.2
+ _ZNSt3__19__unicode32__extended_grapheme_cluster_viewIcE9__consumeB8ne190102Ev.cold.1
+ __126-[PGRemoteTask doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:]_block_invoke.141
+ __20-[_PGDevice unpause]_block_invoke.cold.1
+ __20-[_PGDevice unpause]_block_invoke.cold.2
+ __29-[_PGDevice resumeChildFifo:]_block_invoke.cold.1
+ __34-[_PGDisplay signalResponsiveness]_block_invoke.195
+ __37-[PGEFIDisplay scheduleFramePresents]_block_invoke.9
+ __37-[PGFIFO initWithDevice:lastPending:]_block_invoke.1
+ __44-[PGIOSurfaceHostDevice initWithDescriptor:]_block_invoke.29
+ __48-[PGLocalTask copyFromVirtualOffset:length:dst:]_block_invoke.cold.1
+ __49-[PGIOSurfaceHostDevice mmioWriteAtOffset:value:]_block_invoke.34
+ __54-[PGRemoteTask initWithDevice:taskRoot:length:taskID:]_block_invoke.129
+ __55-[_PGDisplay initWithDevice:descriptor:port:serialNum:]_block_invoke.186
+ __62-[_PGDisplay encodeRenderFrame:toDisplay:withCmdBuf:viewport:]_block_invoke.cold.1
+ __67-[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:]_block_invoke.cold.1
+ __67-[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:]_block_invoke.cold.2
+ __97-[PGLocalTask doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:]_block_invoke.86
+ __97-[PGLocalTask doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:]_block_invoke.cold.1
+ __98-[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:]_block_invoke.72
+ __Block_byref_object_copy_.25
+ __Block_byref_object_copy_.72
+ __Block_byref_object_copy_.75
+ __Block_byref_object_dispose_.26
+ __Block_byref_object_dispose_.73
+ __Block_byref_object_dispose_.76
+ __OBJC_$_CLASS_METHODS_PGBackingResource
+ __OBJC_$_CLASS_METHODS_PGBufferResource
+ __OBJC_$_CLASS_METHODS_PGHeapResource
+ __OBJC_$_CLASS_METHODS_PGIOSurfaceHostDevice
+ __OBJC_$_CLASS_METHODS_PGMemoryMap
+ __OBJC_$_CLASS_METHODS_PGMemoryMapSegment
+ __OBJC_$_CLASS_METHODS_PGTextureResource
+ __OBJC_$_CLASS_METHODS__PGDisplay
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_PGMemoryMap
+ __OBJC_$_CLASS_PROP_LIST_PGMemoryMapSegment
+ __OBJC_$_INSTANCE_METHODS_PGBackingResource
+ __OBJC_$_INSTANCE_METHODS_PGBaseTask
+ __OBJC_$_INSTANCE_METHODS_PGChildFIFO
+ __OBJC_$_INSTANCE_METHODS_PGDeserializerBlitDecoder
+ __OBJC_$_INSTANCE_METHODS_PGDeserializerComputeDecoder
+ __OBJC_$_INSTANCE_METHODS_PGDeserializerInfoDecoder
+ __OBJC_$_INSTANCE_METHODS_PGDeserializerRenderDecoder
+ __OBJC_$_INSTANCE_METHODS_PGDetachBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGDetachHeapResource
+ __OBJC_$_INSTANCE_METHODS_PGDeviceDescriptor
+ __OBJC_$_INSTANCE_METHODS_PGDiscardableHeapBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGDiscardableSerializerTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGDisplayDescriptor(PGDisplayDescriptorPrivate)
+ __OBJC_$_INSTANCE_METHODS_PGDisplayMode(PGDisplayModePrivate)
+ __OBJC_$_INSTANCE_METHODS_PGDisplayPipelineCache
+ __OBJC_$_INSTANCE_METHODS_PGDisplayPipelineDescriptor
+ __OBJC_$_INSTANCE_METHODS_PGDualPlaneBlitTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGDualPlaneComputeTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGDualPlaneSharedTextureBackingResource
+ __OBJC_$_INSTANCE_METHODS_PGEFIDisplay
+ __OBJC_$_INSTANCE_METHODS_PGFIFO
+ __OBJC_$_INSTANCE_METHODS_PGHeapBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGIOSurfaceHostDevice
+ __OBJC_$_INSTANCE_METHODS_PGIOSurfaceHostDeviceDescriptor
+ __OBJC_$_INSTANCE_METHODS_PGLegacyHeapResource
+ __OBJC_$_INSTANCE_METHODS_PGLocalTask
+ __OBJC_$_INSTANCE_METHODS_PGMapMapping
+ __OBJC_$_INSTANCE_METHODS_PGMapperRefBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGMapperRefTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGMapping
+ __OBJC_$_INSTANCE_METHODS_PGMappingTask
+ __OBJC_$_INSTANCE_METHODS_PGMemoryMap
+ __OBJC_$_INSTANCE_METHODS_PGMemoryMapDescriptor
+ __OBJC_$_INSTANCE_METHODS_PGMemoryMapSegment
+ __OBJC_$_INSTANCE_METHODS_PGPageTableIterator
+ __OBJC_$_INSTANCE_METHODS_PGPrivateBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGRefTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGRemoteTask
+ __OBJC_$_INSTANCE_METHODS_PGRemoteTaskDeviceDelegate
+ __OBJC_$_INSTANCE_METHODS_PGResource
+ __OBJC_$_INSTANCE_METHODS_PGResourceManagerDelegate
+ __OBJC_$_INSTANCE_METHODS_PGResourceManagerDeserializationContext
+ __OBJC_$_INSTANCE_METHODS_PGRootFIFO
+ __OBJC_$_INSTANCE_METHODS_PGRootTaskMapping
+ __OBJC_$_INSTANCE_METHODS_PGSerializerTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGSharedBufferResource
+ __OBJC_$_INSTANCE_METHODS_PGSharedTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_$_INSTANCE_METHODS_PGSinglePlaneTextureResource
+ __OBJC_$_INSTANCE_METHODS_PGTaskMapping
+ __OBJC_$_INSTANCE_METHODS_PGTextureResource
+ __OBJC_$_INSTANCE_METHODS__PGDeserializer
+ __OBJC_$_INSTANCE_METHODS__PGDevice
+ __OBJC_$_INSTANCE_METHODS__PGDisplay
+ __OBJC_$_INSTANCE_METHODS__PGDisplayNub
+ __OBJC_$_INSTANCE_VARIABLES_PGBackingResource
+ __OBJC_$_INSTANCE_VARIABLES_PGBaseTask
+ __OBJC_$_INSTANCE_VARIABLES_PGChildFIFO
+ __OBJC_$_INSTANCE_VARIABLES_PGDeserializerBlitDecoder
+ __OBJC_$_INSTANCE_VARIABLES_PGDeserializerComputeDecoder
+ __OBJC_$_INSTANCE_VARIABLES_PGDeserializerInfoDecoder
+ __OBJC_$_INSTANCE_VARIABLES_PGDeserializerRenderDecoder
+ __OBJC_$_INSTANCE_VARIABLES_PGDetachBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_PGDetachHeapResource
+ __OBJC_$_INSTANCE_VARIABLES_PGDeviceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PGDisplayDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PGDisplayMode
+ __OBJC_$_INSTANCE_VARIABLES_PGDisplayPipelineCache
+ __OBJC_$_INSTANCE_VARIABLES_PGDisplayPipelineDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PGDualPlaneBlitTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGDualPlaneComputeTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGDualPlaneSharedTextureBackingResource
+ __OBJC_$_INSTANCE_VARIABLES_PGEFIDisplay
+ __OBJC_$_INSTANCE_VARIABLES_PGFIFO
+ __OBJC_$_INSTANCE_VARIABLES_PGHeapBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_PGIOSurfaceHostDevice
+ __OBJC_$_INSTANCE_VARIABLES_PGIOSurfaceHostDeviceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PGLegacyHeapResource
+ __OBJC_$_INSTANCE_VARIABLES_PGLocalTask
+ __OBJC_$_INSTANCE_VARIABLES_PGMapperRefBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_PGMapperRefTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGMapping
+ __OBJC_$_INSTANCE_VARIABLES_PGMappingTask
+ __OBJC_$_INSTANCE_VARIABLES_PGMemoryMap
+ __OBJC_$_INSTANCE_VARIABLES_PGMemoryMapDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PGMemoryMapSegment
+ __OBJC_$_INSTANCE_VARIABLES_PGPageTableIterator
+ __OBJC_$_INSTANCE_VARIABLES_PGPrivateBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_PGRefTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGRemoteTask
+ __OBJC_$_INSTANCE_VARIABLES_PGRemoteTaskDeviceDelegate
+ __OBJC_$_INSTANCE_VARIABLES_PGResource
+ __OBJC_$_INSTANCE_VARIABLES_PGResourceManagerDelegate
+ __OBJC_$_INSTANCE_VARIABLES_PGResourceManagerDeserializationContext
+ __OBJC_$_INSTANCE_VARIABLES_PGRootFIFO
+ __OBJC_$_INSTANCE_VARIABLES_PGRootTaskMapping
+ __OBJC_$_INSTANCE_VARIABLES_PGSerializerTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGSharedBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_PGSharedTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_$_INSTANCE_VARIABLES_PGSinglePlaneTextureResource
+ __OBJC_$_INSTANCE_VARIABLES_PGTaskMapping
+ __OBJC_$_INSTANCE_VARIABLES_PGTextureResource
+ __OBJC_$_INSTANCE_VARIABLES__PGDeserializer
+ __OBJC_$_INSTANCE_VARIABLES__PGDevice
+ __OBJC_$_INSTANCE_VARIABLES__PGDisplay
+ __OBJC_$_INSTANCE_VARIABLES__PGDisplayNub
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_PGBackingResource
+ __OBJC_$_PROP_LIST_PGBaseTask
+ __OBJC_$_PROP_LIST_PGDeserializerBlitDecoder
+ __OBJC_$_PROP_LIST_PGDeserializerComputeDecoder
+ __OBJC_$_PROP_LIST_PGDeserializerDecoder
+ __OBJC_$_PROP_LIST_PGDeserializerInfoDecoder
+ __OBJC_$_PROP_LIST_PGDeserializerRenderDecoder
+ __OBJC_$_PROP_LIST_PGDeviceDescriptor
+ __OBJC_$_PROP_LIST_PGDisplay
+ __OBJC_$_PROP_LIST_PGDisplayPipelineDescriptor
+ __OBJC_$_PROP_LIST_PGDisplayPrivate
+ __OBJC_$_PROP_LIST_PGDualPlaneSharedTextureBackingResource
+ __OBJC_$_PROP_LIST_PGFIFO
+ __OBJC_$_PROP_LIST_PGIOSurfaceHostDeviceDescriptor
+ __OBJC_$_PROP_LIST_PGLocalTask
+ __OBJC_$_PROP_LIST_PGMapping
+ __OBJC_$_PROP_LIST_PGMappingTask
+ __OBJC_$_PROP_LIST_PGMemoryMapSegment
+ __OBJC_$_PROP_LIST_PGRemoteTask
+ __OBJC_$_PROP_LIST_PGRemoteTaskDeviceDelegate
+ __OBJC_$_PROP_LIST_PGResource
+ __OBJC_$_PROP_LIST_PGResourceManagerDelegate
+ __OBJC_$_PROP_LIST_PGResourceManagerDeserializationContext
+ __OBJC_$_PROP_LIST_PGRootFIFO
+ __OBJC_$_PROP_LIST_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_$_PROP_LIST_PGTask_Resource
+ __OBJC_$_PROP_LIST_PGTextureResource
+ __OBJC_$_PROP_LIST__PGDeserializer
+ __OBJC_$_PROP_LIST__PGDevice
+ __OBJC_$_PROP_LIST__PGDisplay
+ __OBJC_$_PROP_LIST__PGDisplayNub
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLDeserializationContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDeserializer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDeserializerDecoder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDeserializerObjectDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDisplay
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGDisplayPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGKernelTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGSharedTextureBackingResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGTask_ObjectListManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGTask_Resource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGTask_ResourceManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PGUserTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ParavirtualizedGraphicsGPUTaskProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLDeserializationContext
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDeserializer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDeserializerDecoder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDeserializerObjectDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDevice
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDisplay
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGDisplayPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGKernelTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGSharedTextureBackingResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGTask_ObjectListManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGTask_Resource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGTask_ResourceManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PGUserTask
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ParavirtualizedGraphicsGPUTaskProtocol
+ __OBJC_$_PROTOCOL_REFS_MTLDeserializationContext
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_PGDeserializer
+ __OBJC_$_PROTOCOL_REFS_PGDeserializerDecoder
+ __OBJC_$_PROTOCOL_REFS_PGDeserializerObjectDelegate
+ __OBJC_$_PROTOCOL_REFS_PGDevice
+ __OBJC_$_PROTOCOL_REFS_PGDisplay
+ __OBJC_$_PROTOCOL_REFS_PGDisplayPrivate
+ __OBJC_$_PROTOCOL_REFS_PGKernelTask
+ __OBJC_$_PROTOCOL_REFS_PGSharedTextureBackingResource
+ __OBJC_$_PROTOCOL_REFS_PGTask
+ __OBJC_$_PROTOCOL_REFS_PGTask_ObjectListManager
+ __OBJC_$_PROTOCOL_REFS_PGTask_Resource
+ __OBJC_$_PROTOCOL_REFS_PGTask_ResourceManager
+ __OBJC_$_PROTOCOL_REFS_PGUserTask
+ __OBJC_$_PROTOCOL_REFS_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_$_PROTOCOL_REFS_ParavirtualizedGraphicsGPUTaskProtocol
+ __OBJC_CLASS_PROTOCOLS_$_PGBaseTask
+ __OBJC_CLASS_PROTOCOLS_$_PGDeserializerBlitDecoder
+ __OBJC_CLASS_PROTOCOLS_$_PGDeserializerComputeDecoder
+ __OBJC_CLASS_PROTOCOLS_$_PGDeserializerInfoDecoder
+ __OBJC_CLASS_PROTOCOLS_$_PGDeserializerRenderDecoder
+ __OBJC_CLASS_PROTOCOLS_$_PGDisplayPipelineDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_PGDualPlaneSharedTextureBackingResource
+ __OBJC_CLASS_PROTOCOLS_$_PGLocalTask
+ __OBJC_CLASS_PROTOCOLS_$_PGMemoryMap
+ __OBJC_CLASS_PROTOCOLS_$_PGMemoryMapSegment
+ __OBJC_CLASS_PROTOCOLS_$_PGRemoteTask
+ __OBJC_CLASS_PROTOCOLS_$_PGRemoteTaskDeviceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PGResourceManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PGResourceManagerDeserializationContext
+ __OBJC_CLASS_PROTOCOLS_$_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_CLASS_PROTOCOLS_$__PGDeserializer
+ __OBJC_CLASS_PROTOCOLS_$__PGDevice
+ __OBJC_CLASS_PROTOCOLS_$__PGDisplay
+ __OBJC_CLASS_RO_$_PGBackingResource
+ __OBJC_CLASS_RO_$_PGBaseTask
+ __OBJC_CLASS_RO_$_PGBufferResource
+ __OBJC_CLASS_RO_$_PGChildFIFO
+ __OBJC_CLASS_RO_$_PGDeserializerBlitDecoder
+ __OBJC_CLASS_RO_$_PGDeserializerComputeDecoder
+ __OBJC_CLASS_RO_$_PGDeserializerInfoDecoder
+ __OBJC_CLASS_RO_$_PGDeserializerRenderDecoder
+ __OBJC_CLASS_RO_$_PGDetachBufferResource
+ __OBJC_CLASS_RO_$_PGDetachHeapResource
+ __OBJC_CLASS_RO_$_PGDeviceDescriptor
+ __OBJC_CLASS_RO_$_PGDiscardableHeapBufferResource
+ __OBJC_CLASS_RO_$_PGDiscardableSerializerTextureResource
+ __OBJC_CLASS_RO_$_PGDisplayDescriptor
+ __OBJC_CLASS_RO_$_PGDisplayMode
+ __OBJC_CLASS_RO_$_PGDisplayPipelineCache
+ __OBJC_CLASS_RO_$_PGDisplayPipelineDescriptor
+ __OBJC_CLASS_RO_$_PGDualPlaneBlitTextureResource
+ __OBJC_CLASS_RO_$_PGDualPlaneComputeTextureResource
+ __OBJC_CLASS_RO_$_PGDualPlaneSharedTextureBackingResource
+ __OBJC_CLASS_RO_$_PGEFIDisplay
+ __OBJC_CLASS_RO_$_PGFIFO
+ __OBJC_CLASS_RO_$_PGHeapBufferResource
+ __OBJC_CLASS_RO_$_PGHeapResource
+ __OBJC_CLASS_RO_$_PGIOSurfaceHostDevice
+ __OBJC_CLASS_RO_$_PGIOSurfaceHostDeviceDescriptor
+ __OBJC_CLASS_RO_$_PGLegacyHeapResource
+ __OBJC_CLASS_RO_$_PGLocalTask
+ __OBJC_CLASS_RO_$_PGMapMapping
+ __OBJC_CLASS_RO_$_PGMapperRefBufferResource
+ __OBJC_CLASS_RO_$_PGMapperRefTextureResource
+ __OBJC_CLASS_RO_$_PGMapping
+ __OBJC_CLASS_RO_$_PGMappingTask
+ __OBJC_CLASS_RO_$_PGMemoryMap
+ __OBJC_CLASS_RO_$_PGMemoryMapDescriptor
+ __OBJC_CLASS_RO_$_PGMemoryMapSegment
+ __OBJC_CLASS_RO_$_PGPageTableIterator
+ __OBJC_CLASS_RO_$_PGPrivateBufferResource
+ __OBJC_CLASS_RO_$_PGRefTextureResource
+ __OBJC_CLASS_RO_$_PGRemoteTask
+ __OBJC_CLASS_RO_$_PGRemoteTaskDeviceDelegate
+ __OBJC_CLASS_RO_$_PGResource
+ __OBJC_CLASS_RO_$_PGResourceManagerDelegate
+ __OBJC_CLASS_RO_$_PGResourceManagerDeserializationContext
+ __OBJC_CLASS_RO_$_PGRootFIFO
+ __OBJC_CLASS_RO_$_PGRootTaskMapping
+ __OBJC_CLASS_RO_$_PGSerializerTextureResource
+ __OBJC_CLASS_RO_$_PGSharedBufferResource
+ __OBJC_CLASS_RO_$_PGSharedTextureResource
+ __OBJC_CLASS_RO_$_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_CLASS_RO_$_PGSinglePlaneTextureResource
+ __OBJC_CLASS_RO_$_PGTaskMapping
+ __OBJC_CLASS_RO_$_PGTextureResource
+ __OBJC_CLASS_RO_$__PGDeserializer
+ __OBJC_CLASS_RO_$__PGDevice
+ __OBJC_CLASS_RO_$__PGDisplay
+ __OBJC_CLASS_RO_$__PGDisplayNub
+ __OBJC_LABEL_PROTOCOL_$_MTLDeserializationContext
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_PGDeserializer
+ __OBJC_LABEL_PROTOCOL_$_PGDeserializerDecoder
+ __OBJC_LABEL_PROTOCOL_$_PGDeserializerObjectDelegate
+ __OBJC_LABEL_PROTOCOL_$_PGDevice
+ __OBJC_LABEL_PROTOCOL_$_PGDisplay
+ __OBJC_LABEL_PROTOCOL_$_PGDisplayPrivate
+ __OBJC_LABEL_PROTOCOL_$_PGKernelTask
+ __OBJC_LABEL_PROTOCOL_$_PGSharedTextureBackingResource
+ __OBJC_LABEL_PROTOCOL_$_PGTask
+ __OBJC_LABEL_PROTOCOL_$_PGTask_ObjectListManager
+ __OBJC_LABEL_PROTOCOL_$_PGTask_Resource
+ __OBJC_LABEL_PROTOCOL_$_PGTask_ResourceManager
+ __OBJC_LABEL_PROTOCOL_$_PGUserTask
+ __OBJC_LABEL_PROTOCOL_$_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_LABEL_PROTOCOL_$_ParavirtualizedGraphicsGPUTaskProtocol
+ __OBJC_METACLASS_RO_$_PGBackingResource
+ __OBJC_METACLASS_RO_$_PGBaseTask
+ __OBJC_METACLASS_RO_$_PGBufferResource
+ __OBJC_METACLASS_RO_$_PGChildFIFO
+ __OBJC_METACLASS_RO_$_PGDeserializerBlitDecoder
+ __OBJC_METACLASS_RO_$_PGDeserializerComputeDecoder
+ __OBJC_METACLASS_RO_$_PGDeserializerInfoDecoder
+ __OBJC_METACLASS_RO_$_PGDeserializerRenderDecoder
+ __OBJC_METACLASS_RO_$_PGDetachBufferResource
+ __OBJC_METACLASS_RO_$_PGDetachHeapResource
+ __OBJC_METACLASS_RO_$_PGDeviceDescriptor
+ __OBJC_METACLASS_RO_$_PGDiscardableHeapBufferResource
+ __OBJC_METACLASS_RO_$_PGDiscardableSerializerTextureResource
+ __OBJC_METACLASS_RO_$_PGDisplayDescriptor
+ __OBJC_METACLASS_RO_$_PGDisplayMode
+ __OBJC_METACLASS_RO_$_PGDisplayPipelineCache
+ __OBJC_METACLASS_RO_$_PGDisplayPipelineDescriptor
+ __OBJC_METACLASS_RO_$_PGDualPlaneBlitTextureResource
+ __OBJC_METACLASS_RO_$_PGDualPlaneComputeTextureResource
+ __OBJC_METACLASS_RO_$_PGDualPlaneSharedTextureBackingResource
+ __OBJC_METACLASS_RO_$_PGEFIDisplay
+ __OBJC_METACLASS_RO_$_PGFIFO
+ __OBJC_METACLASS_RO_$_PGHeapBufferResource
+ __OBJC_METACLASS_RO_$_PGHeapResource
+ __OBJC_METACLASS_RO_$_PGIOSurfaceHostDevice
+ __OBJC_METACLASS_RO_$_PGIOSurfaceHostDeviceDescriptor
+ __OBJC_METACLASS_RO_$_PGLegacyHeapResource
+ __OBJC_METACLASS_RO_$_PGLocalTask
+ __OBJC_METACLASS_RO_$_PGMapMapping
+ __OBJC_METACLASS_RO_$_PGMapperRefBufferResource
+ __OBJC_METACLASS_RO_$_PGMapperRefTextureResource
+ __OBJC_METACLASS_RO_$_PGMapping
+ __OBJC_METACLASS_RO_$_PGMappingTask
+ __OBJC_METACLASS_RO_$_PGMemoryMap
+ __OBJC_METACLASS_RO_$_PGMemoryMapDescriptor
+ __OBJC_METACLASS_RO_$_PGMemoryMapSegment
+ __OBJC_METACLASS_RO_$_PGPageTableIterator
+ __OBJC_METACLASS_RO_$_PGPrivateBufferResource
+ __OBJC_METACLASS_RO_$_PGRefTextureResource
+ __OBJC_METACLASS_RO_$_PGRemoteTask
+ __OBJC_METACLASS_RO_$_PGRemoteTaskDeviceDelegate
+ __OBJC_METACLASS_RO_$_PGResource
+ __OBJC_METACLASS_RO_$_PGResourceManagerDelegate
+ __OBJC_METACLASS_RO_$_PGResourceManagerDeserializationContext
+ __OBJC_METACLASS_RO_$_PGRootFIFO
+ __OBJC_METACLASS_RO_$_PGRootTaskMapping
+ __OBJC_METACLASS_RO_$_PGSerializerTextureResource
+ __OBJC_METACLASS_RO_$_PGSharedBufferResource
+ __OBJC_METACLASS_RO_$_PGSharedTextureResource
+ __OBJC_METACLASS_RO_$_PGSinglePlaneSharedTextureBackingResource
+ __OBJC_METACLASS_RO_$_PGSinglePlaneTextureResource
+ __OBJC_METACLASS_RO_$_PGTaskMapping
+ __OBJC_METACLASS_RO_$_PGTextureResource
+ __OBJC_METACLASS_RO_$__PGDeserializer
+ __OBJC_METACLASS_RO_$__PGDevice
+ __OBJC_METACLASS_RO_$__PGDisplay
+ __OBJC_METACLASS_RO_$__PGDisplayNub
+ __OBJC_PROTOCOL_$_MTLDeserializationContext
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_PGDeserializer
+ __OBJC_PROTOCOL_$_PGDeserializerDecoder
+ __OBJC_PROTOCOL_$_PGDeserializerObjectDelegate
+ __OBJC_PROTOCOL_$_PGDevice
+ __OBJC_PROTOCOL_$_PGDisplay
+ __OBJC_PROTOCOL_$_PGDisplayPrivate
+ __OBJC_PROTOCOL_$_PGKernelTask
+ __OBJC_PROTOCOL_$_PGSharedTextureBackingResource
+ __OBJC_PROTOCOL_$_PGTask
+ __OBJC_PROTOCOL_$_PGTask_ObjectListManager
+ __OBJC_PROTOCOL_$_PGTask_Resource
+ __OBJC_PROTOCOL_$_PGTask_ResourceManager
+ __OBJC_PROTOCOL_$_PGUserTask
+ __OBJC_PROTOCOL_$_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_PROTOCOL_$_ParavirtualizedGraphicsGPUTaskProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ParavirtualizedGraphicsGPUDeviceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ParavirtualizedGraphicsGPUTaskProtocol
+ __Z17newFunctionWithIRPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEE5PGPtrIP6NSDataE
+ __Z19newIOSurfaceTextureP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z20newTextureDescriptorPK29PGSerializedTextureDescriptory
+ __Z20newTextureDescriptorPK30PGSerializedTextureDescriptor2y
+ __Z24newTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z25newTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z26newSharedTextureWithHandleP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP22MTLSharedTextureHandleNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z28newSerializerTextureWithHeapP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z29newSamplerStateWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z30newSharedTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z31newIOSurfaceTextureWithRotationP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectP9IOSurfaceNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z31newSharedTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z33newRasterizationRateMapDescriptorP41PGOperationRasterizationRateMapDescriptorNSt3__110shared_ptrI21PGVirtualMemoryCursorEE
+ __Z34newDepthStencilStateWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z34newSerializerTextureViewWithBufferP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z34newSerializerTextureWithDescriptorP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z35newSerializerTextureViewWithSwizzleP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z35newSerializerTextureWithDescriptor2P17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z36newRenderPipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z37newComputePipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z37newRasterizationRateMapWithDescriptorPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z39newSerializerTextureViewWithPixelFormatP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z39newSerializerTextureViewWithTextureTypeP17PGResourceManagerPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEPK18APVObjectPlacement
+ __Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z8newFencePU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZL11dumpPayloadPvm
+ __ZL11serialNumDB
+ __ZL16mapPhysicalRangeRK18PGMemoryMapRange_tRK23PGPhysicalMemoryRange_sy
+ __ZL16serialNumDBMutex
+ __ZL21copyStencilDescriptorP20MTLStencilDescriptorPK29PGSerializedStencilDescriptor
+ __ZL24getAPVFeaturesForVersion16APVBinaryVersion
+ __ZL24validateMTLPrimitiveType16MTLPrimitiveType
+ __ZL9CmpRangesR18PGMemoryMapRange_tS0_
+ __ZN14PGByteIteratorC1EPKvy
+ __ZN14PGByteIteratorC2EPKvy
+ __ZN17PGResourceManager10createHeapERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager10subManagerIP10PGResourceEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU18objcproto8MTLFence11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU22objcproto11MTLFunction11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU26objcproto15MTLSamplerState11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU31objcproto20MTLDepthStencilState11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU33objcproto22MTLRenderPipelineState11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU34objcproto23MTLComputePipelineState11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager10subManagerIPU34objcproto23MTLRasterizationRateMap11objc_objectEERNS_10SubManagerIT_EEv
+ __ZN17PGResourceManager12createBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIP10PGResourceEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU18objcproto8MTLFence11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU22objcproto11MTLFunction11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU26objcproto15MTLSamplerState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU31objcproto20MTLDepthStencilState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU34objcproto23MTLComputePipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12createObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEERK14APVObjectEntryNS3_10shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager12deleteObjectEPKvm
+ __ZN17PGResourceManager12deleteObjectIP10PGResourceEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU17objcproto7MTLHeap11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU18objcproto8MTLFence11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU19objcproto9MTLBuffer11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU21objcproto10MTLTexture11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU22objcproto11MTLFunction11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU26objcproto15MTLSamplerState11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU31objcproto20MTLDepthStencilState11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU34objcproto23MTLComputePipelineState11objc_objectEEvjb
+ __ZN17PGResourceManager12deleteObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEEvjb
+ __ZN17PGResourceManager13createBackingERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager13reserveObjectEjRK14APVObjectEntryRK18APVObjectPlacementRNS_16ReservationTableE
+ __ZN17PGResourceManager14flushResourcesEv
+ __ZN17PGResourceManager14getObjectEntryEj
+ __ZN17PGResourceManager14objectDelegateEv
+ __ZN17PGResourceManager14registerObjectIP10PGResourceEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU18objcproto8MTLFence11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU22objcproto11MTLFunction11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU26objcproto15MTLSamplerState11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU31objcproto20MTLDepthStencilState11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU34objcproto23MTLComputePipelineState11objc_objectEEbjT_
+ __ZN17PGResourceManager14registerObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEEbjT_
+ __ZN17PGResourceManager14reserveObjectsEv
+ __ZN17PGResourceManager15newMemoryCursorEym
+ __ZN17PGResourceManager16ReservationTableD1Ev
+ __ZN17PGResourceManager16createHeapBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager17getExistingObjectIP10PGResourceEENSt3__18optionalIT_EEj
+ __ZN17PGResourceManager17getExistingObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18optionalIT_EEj
+ __ZN17PGResourceManager19createNormalTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager19createSharedTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager20finalizeReservationsERNS_16ReservationTableE
+ __ZN17PGResourceManager21createMapperRefBufferERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager22createMapperRefTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23clearPlacementListEntryEj
+ __ZN17PGResourceManager23createBackingRefTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23createSerializerTextureERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager23heapTextureSizeAndAlignEPKvm
+ __ZN17PGResourceManager26createSharedTextureBackingERK14APVObjectEntryNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __ZN17PGResourceManager30textureDescriptorForDescriptorEPK29PGSerializedTextureDescriptor
+ __ZN17PGResourceManager32newWritableMemoryCursorForBufferEj
+ __ZN17PGResourceManager7getDataEym
+ __ZN17PGResourceManager9getObjectIP10PGResourceEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU17objcproto7MTLHeap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU18objcproto8MTLFence11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU19objcproto9MTLBuffer11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU21objcproto10MTLTexture11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU22objcproto11MTLFunction11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU22objcproto11MTLResource11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU26objcproto15MTLSamplerState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU31objcproto20MTLDepthStencilState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU34objcproto23MTLComputePipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9getObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIP10PGResourceEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU18objcproto8MTLFence11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU22objcproto11MTLFunction11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU26objcproto15MTLSamplerState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU31objcproto20MTLDepthStencilState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU33objcproto22MTLRenderPipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU34objcproto23MTLComputePipelineState11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManager9newObjectIPU34objcproto23MTLRasterizationRateMap11objc_objectEENSt3__18expectedIT_NS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEj
+ __ZN17PGResourceManagerC1EPU19objcproto9MTLDevice11objc_objectPU50objcproto15PGTask_Resource22PGTask_ResourceManager11objc_objectNSt3__110shared_ptrI19PGObjectListManagerEE
+ __ZN17PGResourceManagerC2EPU19objcproto9MTLDevice11objc_objectPU50objcproto15PGTask_Resource22PGTask_ResourceManager11objc_objectNSt3__110shared_ptrI19PGObjectListManagerEE
+ __ZN17PGResourceManagerD1Ev
+ __ZN17PGResourceManagerD2Ev
+ __ZN19PGObjectListManager13setObjectListEyjyjP12APVTaskRoot2
+ __ZN19PGObjectListManager14getObjectEntryEj
+ __ZN19PGObjectListManager21getPlacementListEntryEj
+ __ZN19PGObjectListManagerC2Eyb
+ __ZN19PGObjectListManagerD0Ev
+ __ZN19PGObjectListManagerD1Ev
+ __ZN19PGObjectListManagerD2Ev
+ __ZN19PGPendingStampQueue10faultStampEjj
+ __ZN19PGPendingStampQueue11signalStampEj
+ __ZN19PGPendingStampQueue15describePendingEv
+ __ZN19PGPendingStampQueue15resumeFromFaultEv
+ __ZN19PGPendingStampQueue4pumpEv
+ __ZN19PGPendingStampQueue5drainEv
+ __ZN19PGPendingStampQueue7quiesceEv
+ __ZN19PGPendingStampQueue9pushStampEjj
+ __ZN19PGPendingStampQueueD0Ev
+ __ZN19PGPendingStampQueueD1Ev
+ __ZN19PGPendingStampQueueD2Ev
+ __ZN19PGResourceList_implI26APVCmdExecIndirectResourceEixEy
+ __ZN19PGResourceList_implI27APVCmdExecIndirectResource3EixEy
+ __ZN21PGVirtualMemoryCursor16cursorWithRangesERNSt3__16vectorINS_5RangeENS0_9allocatorIS2_EEEE
+ __ZN21PGVirtualMemoryCursor17cursorWithPointerENSt3__110shared_ptrIvEEm
+ __ZN21PGVirtualMemoryCursor4readI13APVObjectHeapEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI15APVObjectBufferEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI16APVObjectBackingEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI16APVObjectTextureEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI17APVObjectFunctionEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI17MTLSamplePositionEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI17PGOperationHeaderEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI19APVObjectHeapBufferEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI19APVObjectRefTextureEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI19APVTextureDimensionEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI22APVObjectSharedTextureEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI24APVObjectMapperRefBufferEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI25APVObjectMapperRefTextureEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI29APVObjectSharedTextureBackingEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI29PGOperationNewTextureWithHeapEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI30PGOperationNewIOSurfaceTextureEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI35PGOperationNewTextureViewWithBufferEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI35PGOperationNewTextureWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI36PGOperationNewTextureViewWithSwizzleEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI36PGOperationNewTextureWithDescriptor2EENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI36PGOperationRasterizationRateMapLayerEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI40PGOperationNewSamplerStateWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI40PGOperationNewTextureViewWithPixelFormatEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI40PGOperationNewTextureViewWithTextureTypeEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI41PGOperationNewSharedTextureWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI42PGOperationNewIOSurfaceTextureWithRotationEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI42PGOperationNewSharedTextureWithDescriptor2EENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI45PGOperationNewDepthStencilStateWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI47PGOperationNewRenderPipelineStateWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI48PGOperationNewComputePipelineStateWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI48PGOperationNewRasterizationRateMapWithDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor4readI51PGOperationNewRenderPipelineStateWithTileDescriptorEENSt3__18expectedIT_NS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEv
+ __ZN21PGVirtualMemoryCursor7advanceEm
+ __ZN21PGVirtualMemoryCursor9readBytesEmPv
+ __ZN21PGVirtualMemoryCursorC1ENSt3__110shared_ptrIvEEm
+ __ZN21PGVirtualMemoryCursorC1ENSt3__16vectorINS_5RangeENS0_9allocatorIS2_EEEE
+ __ZN21PGVirtualMemoryCursorC2ENSt3__110shared_ptrIvEEm
+ __ZN21PGVirtualMemoryCursorC2ENSt3__16vectorINS_5RangeENS0_9allocatorIS2_EEEE
+ __ZN25PGLegacyObjectListManager10newMappingEyyb
+ __ZN25PGLegacyObjectListManager13mapObjectListEv
+ __ZN25PGLegacyObjectListManager15unmapObjectListEv
+ __ZN25PGLegacyObjectListManager16mapPlacementListEv
+ __ZN25PGLegacyObjectListManager18isObjectListMappedEv
+ __ZN25PGLegacyObjectListManager18unmapPlacementListEv
+ __ZN25PGLegacyObjectListManager21isPlacementListMappedEv
+ __ZN25PGLegacyObjectListManagerD0Ev
+ __ZN25PGLegacyObjectListManagerD1Ev
+ __ZN28PGMemoryMapObjectListManager10newMappingEyyb
+ __ZN28PGMemoryMapObjectListManager13mapObjectListEv
+ __ZN28PGMemoryMapObjectListManager15unmapObjectListEv
+ __ZN28PGMemoryMapObjectListManager16mapPlacementListEv
+ __ZN28PGMemoryMapObjectListManager18isObjectListMappedEv
+ __ZN28PGMemoryMapObjectListManager18unmapPlacementListEv
+ __ZN28PGMemoryMapObjectListManager21isPlacementListMappedEv
+ __ZN28PGMemoryMapObjectListManagerD0Ev
+ __ZN28PGMemoryMapObjectListManagerD1Ev
+ __ZN29PGWritableVirtualMemoryCursor10writeBytesEmPKv
+ __ZN29PGWritableVirtualMemoryCursor16cursorWithRangesERNSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS0_9allocatorIS3_EEEE
+ __ZN29PGWritableVirtualMemoryCursor17cursorWithPointerENSt3__110shared_ptrIvEEm
+ __ZN29PGWritableVirtualMemoryCursor5writeI13PGCmd2DSize16EENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI17MTLSamplePositionEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI21PGReplyHostObjectInfoEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI23PGReplyUniqueIdentifierEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI29PGReplyBufferHostResourceInfoEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI30PGReplyHeapTextureSizeAndAlignEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI30PGReplyRenderPipelineStateInfoEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI31PGReplyComputePipelineStateInfoEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI31PGReplyRasterizationRateMapInfoEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI37PGReplyRasterizationRateMapCoordinateEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursor5writeI42PGReplyPipelineStateImageBlockMemoryLengthEENSt3__18expectedIvNS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEERKT_
+ __ZN29PGWritableVirtualMemoryCursorC1ENSt3__110shared_ptrIvEEm
+ __ZN29PGWritableVirtualMemoryCursorC1ENSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS0_9allocatorIS3_EEEE
+ __ZN29PGWritableVirtualMemoryCursorC2ENSt3__110shared_ptrIvEEm
+ __ZN29PGWritableVirtualMemoryCursorC2ENSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS0_9allocatorIS3_EEEE
+ __ZN5PGPtrIP9PGMappingED1Ev
+ __ZN5PGPtrIP9PGMappingEaSERKS2_
+ __ZN5PGPtrIP9PGMappingEaSES1_
+ __ZN5PGPtrIPU36objcproto25MTLDeserializationContext11objc_objectED1Ev
+ __ZN5PGPtrIPU36objcproto25MTLDeserializationContext11objc_objectEaSERKS2_
+ __ZN5PGPtrIPU39objcproto28PGDeserializerObjectDelegate11objc_objectED1Ev
+ __ZN5PGPtrIPU39objcproto28PGDeserializerObjectDelegate11objc_objectEaSERKS2_
+ __ZN7PGAsync13completeTokenENSt3__110shared_ptrINS_5TokenEEE12PGExecResult
+ __ZN7PGAsync13completeTokenEy12PGExecResult
+ __ZN7PGAsync13newAsyncTokenEU13block_pointerFv12PGExecResultP7NSErrorE
+ __ZN7PGAsync13newAsyncTokenEv
+ __ZN7PGAsync5Token4waitEv
+ __ZN7PGAsync5Token6signalE12PGExecResult
+ __ZN7PGAsync5TokenC2EyU13block_pointerFv12PGExecResultP7NSErrorE
+ __ZN7PGAsync5TokenD2Ev
+ __ZN7PGAsync5drainEv
+ __ZN7PGAsync7crashedEv
+ __ZNKSt13runtime_error4whatEv
+ __ZNKSt3__112__hash_tableI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE4findIS1_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS1_PvEEEERKT_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__113__format_spec8__parserIcE10__validateB8ne190102ENS0_8__fieldsB8ne190102EPKcj
+ __ZNKSt3__113__format_spec8__parserIcE11__get_widthB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEEiRT_
+ __ZNKSt3__113__format_spec8__parserIcE15__get_precisionB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEEiRT_
+ __ZNKSt3__113__format_spec8__parserIcE31__get_parsed_std_specificationsB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENS0_23__parsed_specificationsIcEERT_
+ __ZNKSt3__116__formatter_charIcE6formatB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorEcRSA_
+ __ZNKSt3__118__formatter_stringIcE6formatB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorENS_17basic_string_viewIcNS_11char_traitsIcEEEERSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102IiNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102IjNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102InNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102IoNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102IxNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_integerIcE6formatB8ne190102IyNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorET_RSA_
+ __ZNKSt3__119__formatter_pointerIcE6formatB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorEPKvRSA_
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__16vectorI18PGMemoryMapRange_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI22PGGuestPhysicalRange_sNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI23PGPhysicalMemoryRange_sNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIjP10PGResourceEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP10PGResourceNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__19formatterIPKccE6formatB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorES2_RSC_
+ __ZNKSt3__19formatterIbcE6formatB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT_8iteratorEbRSA_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt12out_of_rangeD1Ev
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorD2Ev
+ __ZNSt3__110shared_ptrIvEC2B8ne190102IvPFvPvELi0EEEPT_T0_
+ __ZNSt3__110unique_ptrI17PGResourceManagerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__111__formatter13__format_boolB8ne190102IcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT0_8iteratorEbRS9_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IciNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IcjNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IcnNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IcoNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IcxNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter13__format_charB8ne190102IcyNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET0_T1_NS_13__format_spec23__parsed_specificationsIT_EE
+ __ZNSt3__111__formatter14__hex_to_upperB8ne190102Ec
+ __ZNSt3__111__formatter14__write_stringB8ne190102IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET0_NS_13__format_spec23__parsed_specificationsIS9_EE
+ __ZNSt3__111__formatter15__format_bufferB8ne190102IddEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_bbNS_13__format_spec6__signENS8_6__typeE
+ __ZNSt3__111__formatter15__format_bufferB8ne190102IdeEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_bbNS_13__format_spec6__signENS8_6__typeE
+ __ZNSt3__111__formatter15__format_bufferB8ne190102IffEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_bbNS_13__format_spec6__signENS8_6__typeE
+ __ZNSt3__111__formatter16__format_integerB8ne190102IjPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB8ne190102IjcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter16__format_integerB8ne190102ImPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB8ne190102ImcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter16__format_integerB8ne190102IoPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB8ne190102IocNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter16__format_integerB8ne190102IyPccNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT2_8iteratorET_RSA_NS_13__format_spec23__parsed_specificationsIT1_EEbT0_SI_PKci
+ __ZNSt3__111__formatter16__format_integerB8ne190102IycNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EEb
+ __ZNSt3__111__formatter19__write_transformedB8ne190102IPcccPFccENS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_ET_SB_T3_NS_13__format_spec23__parsed_specificationsIT1_EET2_
+ __ZNSt3__111__formatter21__format_escaped_charB8ne190102IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ET_T0_NS_13__format_spec23__parsed_specificationsIS8_EE
+ __ZNSt3__111__formatter23__format_buffer_defaultB8ne190102IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_Pc
+ __ZNSt3__111__formatter23__format_buffer_defaultB8ne190102IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_Pc
+ __ZNSt3__111__formatter23__format_buffer_defaultB8ne190102IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_Pc
+ __ZNSt3__111__formatter23__format_escaped_stringB8ne190102IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET0_NS_13__format_spec23__parsed_specificationsIS9_EE
+ __ZNSt3__111__formatter23__format_floating_pointB8ne190102IdcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EE
+ __ZNSt3__111__formatter23__format_floating_pointB8ne190102IecNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EE
+ __ZNSt3__111__formatter23__format_floating_pointB8ne190102IfcNS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEENT1_8iteratorET_RS9_NS_13__format_spec23__parsed_specificationsIT0_EE
+ __ZNSt3__111__formatter25__write_escaped_code_unitB8ne190102IcEEvRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEEDiPKS3_
+ __ZNSt3__111__formatter27__write_string_no_precisionB8ne190102IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET0_NS_13__format_spec23__parsed_specificationsIS9_EE
+ __ZNSt3__111__formatter28__write_using_trailing_zerosB8ne190102IccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp1_EPKT_SA_T1_NS_13__format_spec23__parsed_specificationsIT0_EEmSA_m
+ __ZNSt3__111__formatter29__format_locale_specific_formB8ne190102INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEdcEET_S7_RKNS0_14__float_bufferIT0_EERKNS0_14__float_resultENS_6localeENS_13__format_spec23__parsed_specificationsIT1_EE
+ __ZNSt3__111__formatter29__format_locale_specific_formB8ne190102INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEfcEET_S7_RKNS0_14__float_bufferIT0_EERKNS0_14__float_resultENS_6localeENS_13__format_spec23__parsed_specificationsIT1_EE
+ __ZNSt3__111__formatter29__is_escaped_sequence_writtenB8ne190102IcEEbRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEEDibNS0_23__escape_quotation_markE
+ __ZNSt3__111__formatter29__is_escaped_sequence_writtenB8ne190102IcEEbRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEEbDi
+ __ZNSt3__111__formatter32__write_using_decimal_separatorsB8ne190102INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEPccEET_S8_T0_S9_S9_ONS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEET1_NS_13__format_spec23__parsed_specificationsISH_EE
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB8ne190102IddEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB8ne190102IdeEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_buffer_general_lower_caseB8ne190102IffEENS0_14__float_resultERNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter34__format_floating_point_non_finiteB8ne190102INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEET_S7_NS_13__format_spec23__parsed_specificationsIT0_EEbb
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB8ne190102IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB8ne190102IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter37__format_buffer_scientific_lower_caseB8ne190102IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB8ne190102IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB8ne190102IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_lower_caseB8ne190102IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_upper_caseB8ne190102IddEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_upper_caseB8ne190102IdeEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter38__format_buffer_hexadecimal_upper_caseB8ne190102IffEENS0_14__float_resultERKNS0_14__float_bufferIT_EET0_iPc
+ __ZNSt3__111__formatter6__fillB8ne190102IcNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEET0_S7_mNS_13__format_spec12__code_pointIT_EE
+ __ZNSt3__111__formatter7__writeB8ne190102IccNS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEEEDtfp0_ENS_17basic_string_viewIT_NS_11char_traitsIS9_EEEET1_NS_13__format_spec23__parsed_specificationsIT0_EEl
+ __ZNSt3__111__formatter8__escapeB8ne190102IcEEvRNS_12basic_stringIT_NS_11char_traitsIS3_EENS_9allocatorIS3_EEEENS_17basic_string_viewIS3_S5_EENS0_23__escape_quotation_markE
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_Lb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb
+ __ZNSt3__111__sift_downB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_OT0_NS_15iterator_traitsIS8_E15difference_typeES8_
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__111unique_lockINS_15recursive_mutexEE8try_lockEv
+ __ZNSt3__112__destroy_atB8ne190102I21PGVirtualMemoryCursorLi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102I29PGWritableVirtualMemoryCursorLi0EEEvPT_
+ __ZNSt3__112__hash_tableI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE25__emplace_unique_key_argsIS1_JRKS1_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS1_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIjEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEENS_22__unordered_map_hasherIjS6_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE14__erase_uniqueIyEEmRKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE21__construct_node_hashIRKNS_21piecewise_construct_tEJNS_5tupleIJRKyEEENSM_IJRS4_EEEEEENS_10unique_ptrINS_11__hash_nodeIS6_PvEENS_22__hash_node_destructorINSF_ISV_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSM_IJRS4_EEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEENS_22__unordered_map_hasherIyS6_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE5clearEv
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEED2Ev
+ __ZNSt3__112__vformat_toB8ne190102INS_20back_insert_iteratorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEcNS1_INS_8__format15__output_bufferIcEEEEEET_SD_NS_17basic_string_viewIT0_NS3_ISF_EEEENS_17basic_format_argsINS_20basic_format_contextIT1_SF_EEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE18__insert_with_sizeIPcS7_EENS_11__wrap_iterIS7_EENS8_IPKcEET_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__init_with_sentinelB8ne190102IPcS7_EEvT_T0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__insert_from_safe_copyB8ne190102INS_11__wrap_iterIPKcEESA_EENS7_IPcEEmmT_T0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__insert_from_safe_copyB8ne190102IPcS7_EENS_11__wrap_iterIS7_EEmmT_T0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__112construct_atB8ne190102I21PGVirtualMemoryCursorJRNS_10shared_ptrIvEERmEPS1_EEPT_S8_DpOT0_
+ __ZNSt3__112construct_atB8ne190102I21PGVirtualMemoryCursorJRNS_6vectorINS1_5RangeENS_9allocatorIS3_EEEEEPS1_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8ne190102I29PGWritableVirtualMemoryCursorJRNS_10shared_ptrIvEERmEPS1_EEPT_S8_DpOT0_
+ __ZNSt3__112construct_atB8ne190102I29PGWritableVirtualMemoryCursorJRNS_6vectorIN21PGVirtualMemoryCursor5RangeENS_9allocatorIS4_EEEEEPS1_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB8ne190102I29PGWritableVirtualMemoryCursorJRS1_EPS1_EEPT_S5_DpOT0_
+ __ZNSt3__112format_errorC1B8ne190102EPKc
+ __ZNSt3__112format_errorD0Ev
+ __ZNSt3__112format_errorD1Ev
+ __ZNSt3__113__format_spec14__parse_arg_idB8ne190102IPKcNS_26basic_format_parse_contextIcEEEENS_8__format21__parse_number_resultIT_EES8_S8_RT0_
+ __ZNSt3__113__format_spec21__process_parsed_boolB8ne190102IcEEvRNS0_8__parserIT_EEPKc
+ __ZNSt3__113__format_spec21__process_parsed_charB8ne190102IcEEvRNS0_8__parserIT_EEPKc
+ __ZNSt3__113__format_spec23__estimate_column_widthB8ne190102IcPKcEENS0_21__column_width_resultIT0_EENS_17basic_string_viewIT_NS_11char_traitsIS8_EEEEmNS0_23__column_width_roundingE
+ __ZNSt3__113__format_spec24__process_parsed_integerB8ne190102IcEEvRNS0_8__parserIT_EEPKc
+ __ZNSt3__113__format_spec33__throw_invalid_type_format_errorB8ne190102EPKc
+ __ZNSt3__113__format_spec35__throw_invalid_option_format_errorB8ne190102EPKcS2_
+ __ZNSt3__113__format_spec8__detail43__estimate_column_width_grapheme_clusteringB8ne190102IPKcEENS0_21__column_width_resultIT_EES6_S6_mNS0_23__column_width_roundingE
+ __ZNSt3__113__format_spec8__parserIcE12__parse_typeB8ne190102IPKcEEvRT_
+ __ZNSt3__113__format_spec8__parserIcE13__parse_widthB8ne190102IPKcNS_26basic_format_parse_contextIcEEEEbRT_S8_RT0_
+ __ZNSt3__113__format_spec8__parserIcE17__parse_precisionB8ne190102IPKcNS_26basic_format_parse_contextIcEEEEbRT_S8_RT0_
+ __ZNSt3__113__format_spec8__parserIcE18__parse_fill_alignB8ne190102IPKcEEbRT_S6_
+ __ZNSt3__113__format_spec8__parserIcE7__parseB8ne190102INS_26basic_format_parse_contextIcEEEENT_8iteratorERS6_NS0_8__fieldsB8ne190102E
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113unordered_setI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEC2ERKS8_
+ __ZNSt3__113unordered_setI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEC2ESt16initializer_listIS1_E
+ __ZNSt3__115__expected_baseINS_10shared_ptrI29PGWritableVirtualMemoryCursorEENS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE6__repr22__destroy_union_memberB8ne190102Ev
+ __ZNSt3__115allocate_sharedB8ne190102I21PGVirtualMemoryCursorNS_9allocatorIS1_EEJRNS_10shared_ptrIvEERmELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I21PGVirtualMemoryCursorNS_9allocatorIS1_EEJRNS_6vectorINS1_5RangeENS2_IS5_EEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I25PGLegacyObjectListManagerNS_9allocatorIS1_EEJRybRP11PGLocalTaskELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEJRybRP11PGLocalTaskELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEJRNS_10shared_ptrIvEERmELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEJRNS_6vectorIN21PGVirtualMemoryCursor5RangeENS2_IS6_EEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEJRS1_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102IN7PGAsync5TokenENS_9allocatorIS2_EEJRyRU13block_pointerFv12PGExecResultP7NSErrorEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115recursive_mutex8try_lockEv
+ __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_S8_T0_
+ __ZNSt3__118__formatter_stringIcE5parseB8ne190102INS_26basic_format_parse_contextIcEEEENT_8iteratorERS5_
+ __ZNSt3__118__visit_format_argB8ne190102IZNS_13__format_spec19__substitute_arg_idB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEEjNS_16basic_format_argIT_EEEUlSB_E_S9_EEDcOSB_NSA_IT0_EE
+ __ZNSt3__118__visit_format_argB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_SC_EEDcOSD_NS_16basic_format_argISE_EE
+ __ZNSt3__119__formatter_pointerIcE5parseB8ne190102INS_26basic_format_parse_contextIcEEEENT_8iteratorERS5_
+ __ZNSt3__119__partial_sort_implB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_S7_EET1_S8_S8_T2_OT0_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__119__to_chars_integralB8ne190102IjEENS_15to_chars_resultEPcS2_T_iNS_17integral_constantIbLb0EEE
+ __ZNSt3__119__to_chars_integralB8ne190102IoEENS_15to_chars_resultEPcS2_T_iNS_17integral_constantIbLb0EEE
+ __ZNSt3__119__to_chars_integralB8ne190102IyEENS_15to_chars_resultEPcS2_T_iNS_17integral_constantIbLb0EEE
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEEC2B8ne190102IJRNS_10shared_ptrIvEERmES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEEC2B8ne190102IJRNS_6vectorINS1_5RangeENS2_IS7_EEEEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEEC2B8ne190102IJRybRP11PGLocalTaskES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEEC2B8ne190102IJRybRP11PGLocalTaskES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEEC2B8ne190102IJRNS_10shared_ptrIvEERmES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEEC2B8ne190102IJRNS_6vectorIN21PGVirtualMemoryCursor5RangeENS2_IS8_EEEEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEEC2B8ne190102IJRS1_ES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEEC2B8ne190102IJRyRU13block_pointerFv12PGExecResultP7NSErrorEES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIPvPFvS1_ENS_9allocatorIvEEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPvPFvS1_ENS_9allocatorIvEEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPvPFvS1_ENS_9allocatorIvEEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPvPFvS1_ENS_9allocatorIvEEED1Ev
+ __ZNSt3__120__throw_format_errorB8ne190102EPKc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__120__throw_system_errorEiPKc
+ __ZNSt3__120back_insert_iteratorINS_8__format15__output_bufferIcEEEaSB8ne190102ERKc
+ __ZNSt3__120basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcE6localeB8ne190102Ev
+ __ZNSt3__122__escaped_output_table14__needs_escapeB8ne190102EDi
+ __ZNSt3__122__escaped_output_table9__entriesB8ne190102E
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIP10PGResourceEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU18objcproto8MTLFence11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU22objcproto11MTLFunction11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU26objcproto15MTLSamplerState11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU31objcproto20MTLDepthStencilState11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU33objcproto22MTLRenderPipelineState11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLComputePipelineState11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj5PGPtrIPU34objcproto23MTLRasterizationRateMap11objc_objectEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIy5PGPtrIP9IOSurfaceEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__indic_conjunct_break14__get_propertyB8ne190102EDi
+ __ZNSt3__122__indic_conjunct_break9__entriesB8ne190102E
+ __ZNSt3__124__width_estimation_table17__estimated_widthB8ne190102EDi
+ __ZNSt3__124__width_estimation_table9__entriesB8ne190102E
+ __ZNSt3__125__to_chars_integral_widthB8ne190102IjEEiT_j
+ __ZNSt3__125__to_chars_integral_widthB8ne190102IoEEiT_j
+ __ZNSt3__125__to_chars_integral_widthB8ne190102IyEEiT_j
+ __ZNSt3__126__insertion_sort_unguardedB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_S8_T0_
+ __ZNSt3__126basic_format_parse_contextIcE11next_arg_idB8ne190102Ev
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEbT1_S8_T0_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__131__partition_with_equals_on_leftB8ne190102INS_17_ClassicAlgPolicyEP18PGMemoryMapRange_tRPFbRS2_S4_EEET0_S8_S8_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ne190102INS_17_ClassicAlgPolicyEP18PGMemoryMapRange_tRPFbRS2_S4_EEENS_4pairIT0_bEES9_S9_T1_
+ __ZNSt3__144__extended_grapheme_custer_property_boundary14__get_propertyB8ne190102EDi
+ __ZNSt3__144__extended_grapheme_custer_property_boundary9__entriesB8ne190102E
+ __ZNSt3__16__itoa10__append10B8ne190102IjEEPcS2_T_
+ __ZNSt3__16__itoa10__append10B8ne190102IyEEPcS2_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB8ne190102IjEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB8ne190102IoEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj16EE10__to_charsB8ne190102IyEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB8ne190102IjEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB8ne190102IoEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj2EE10__to_charsB8ne190102IyEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB8ne190102IjEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB8ne190102IoEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__integralILj8EE10__to_charsB8ne190102IyEENS_15to_chars_resultEPcS5_T_
+ __ZNSt3__16__itoa10__pow10_32E
+ __ZNSt3__16__itoa10__pow10_64E
+ __ZNSt3__16__itoa11__pow10_128E
+ __ZNSt3__16__itoa12__base_2_lutE
+ __ZNSt3__16__itoa12__base_8_lutE
+ __ZNSt3__16__itoa13__base_10_u32B8ne190102EPcj
+ __ZNSt3__16__itoa13__base_16_lutE
+ __ZNSt3__16__itoa13__traits_baseIyvE9__convertB8ne190102EPcy
+ __ZNSt3__16__itoa14__base_10_u128B8ne190102EPco
+ __ZNSt3__16__itoa16__digits_base_10E
+ __ZNSt3__16__treeINS_12__value_typeIyNS_10shared_ptrIN7PGAsync5TokenEEEEENS_19__map_value_compareIyS6_NS_4lessIyEELb1EEENS_9allocatorIS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSI_SI_
+ __ZNSt3__16__treeINS_12__value_typeIyNS_10shared_ptrIN7PGAsync5TokenEEEEENS_19__map_value_compareIyS6_NS_4lessIyEELb1EEENS_9allocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIyNS_10shared_ptrIN7PGAsync5TokenEEEEENS_19__map_value_compareIyS6_NS_4lessIyEELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIyJyRS5_EEENS_4pairINS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIyNS_10shared_ptrIN7PGAsync5TokenEEEEENS_19__map_value_compareIyS6_NS_4lessIyEELb1EEENS_9allocatorIS6_EEE5eraseENS_21__tree_const_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEE
+ __ZNSt3__16__treeINS_12__value_typeIyNS_10shared_ptrIN7PGAsync5TokenEEEEENS_19__map_value_compareIyS6_NS_4lessIyEELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16invokeB8ne190102IZNS_13__format_spec19__substitute_arg_idB8ne190102INS_20basic_format_contextINS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEcEEEEjNS_16basic_format_argIT_EEEUlSB_E_JRxEEENS_13invoke_resultISB_JDpT0_EE4typeEOSB_DpOSG_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRNS_17basic_string_viewIcNS_11char_traitsIcEEEEEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSP_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRPKvEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSN_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRS4_EEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRbEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRcEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRdEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JReEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRfEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRiEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRjEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRnEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRoEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRxEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16invokeB8ne190102IZNS_8__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_JRyEEENS_13invoke_resultISD_JDpT0_EE4typeEOSD_DpOSL_
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__16vectorI18PGMemoryMapRange_tNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI18PGMemoryMapRange_tNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI22PGGuestPhysicalRange_sNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI22PGGuestPhysicalRange_sNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIN21PGVirtualMemoryCursor5RangeENS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEjT1_S8_S8_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_S8_S8_S8_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_S8_S8_S8_S8_T0_
+ __ZNSt3__18__format12__vformat_toB8ne190102INS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS0_15__output_bufferIcEEEEcEEEENT0_8iteratorEOT_OSA_
+ __ZNSt3__18__format14__parse_arg_idB8ne190102IPKcNS_26basic_format_parse_contextIcEEEENS0_21__parse_number_resultIT_EES7_S7_RT0_
+ __ZNSt3__18__format14__parse_numberB8ne190102IPKcEENS0_21__parse_number_resultIT_EES5_S5_
+ __ZNSt3__18__format15__output_bufferIcE11__transformB8ne190102IPcPFccEcEEvT_S7_T0_
+ __ZNSt3__18__format15__output_bufferIcE6__copyB8ne190102IcEEvNS_17basic_string_viewIT_NS_11char_traitsIS5_EEEE
+ __ZNSt3__18__format15__output_bufferIcE6__fillB8ne190102Emc
+ __ZNSt3__18__format26__handle_replacement_fieldB8ne190102IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS0_15__output_bufferIcEEEEcEEEET_SC_SC_RT0_RT1_
+ __ZNSt3__18__format8__detail14__parse_manualB8ne190102IPKcNS_26basic_format_parse_contextIcEEEENS0_21__parse_number_resultIT_EES8_S8_RT0_
+ __ZNSt3__18expectedIP10PGResourceNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU18objcproto8MTLFence11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU21objcproto10MTLTexture11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU22objcproto11MTLFunction11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU26objcproto15MTLSamplerState11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU31objcproto20MTLDepthStencilState11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU33objcproto22MTLRenderPipelineState11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU34objcproto23MTLComputePipelineState11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18expectedIPU34objcproto23MTLRasterizationRateMap11objc_objectNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8ne190102EOS9_
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18optionalINS_6localeEEaSB8ne190102IS1_vEERS2_OT_
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERPFbR18PGMemoryMapRange_tS3_EPS2_EEvT1_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeE
+ __ZNSt3__19__unicode17__code_point_viewIcE9__consumeB8ne190102Ev
+ __ZNSt3__19__unicode32__extended_grapheme_cluster_viewIcE9__consumeB8ne190102Ev
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_break10__evaluateB8ne190102EDiNS_44__extended_grapheme_custer_property_boundary10__propertyE
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_break15__evaluate_noneB8ne190102EDiNS_44__extended_grapheme_custer_property_boundary10__propertyE
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_break21__evaluate_GB11_emojiB8ne190102EDiNS_44__extended_grapheme_custer_property_boundary10__propertyE
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_break36__evaluate_GB9c_indic_conjunct_breakB8ne190102EDiNS_44__extended_grapheme_custer_property_boundary10__propertyE
+ __ZNSt3__19__unicode33__extended_grapheme_cluster_breakC2B8ne190102EDi
+ __ZNSt3__19allocatorI18PGMemoryMapRange_tE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorI22PGGuestPhysicalRange_sE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorI23PGPhysicalMemoryRange_sE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorIN21PGVirtualMemoryCursor5RangeEE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorINS_4pairIjP10PGResourceEEE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorIP10PGResourceE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorIyE17allocate_at_leastB8ne190102Em
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZTINSt3__112format_errorE
+ __ZTISt11logic_error
+ __ZTISt12length_error
+ __ZTISt12out_of_range
+ __ZTISt13runtime_error
+ __ZTISt20bad_array_new_length
+ __ZTISt9bad_alloc
+ __ZTISt9exception
+ __ZTSNSt3__112format_errorE
+ __ZTSSt11logic_error
+ __ZTSSt12length_error
+ __ZTSSt12out_of_range
+ __ZTSSt13runtime_error
+ __ZTSSt20bad_array_new_length
+ __ZTSSt9bad_alloc
+ __ZTSSt9exception
+ __ZTV19PGObjectListManager
+ __ZTV19PGPendingStampQueue
+ __ZTV19PGResourceList_implI26APVCmdExecIndirectResourceE
+ __ZTV19PGResourceList_implI27APVCmdExecIndirectResource3E
+ __ZTV25PGLegacyObjectListManager
+ __ZTV28PGMemoryMapObjectListManager
+ __ZTVNSt3__112format_errorE
+ __ZTVNSt3__120__shared_ptr_emplaceI21PGVirtualMemoryCursorNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI25PGLegacyObjectListManagerNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI28PGMemoryMapObjectListManagerNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI29PGWritableVirtualMemoryCursorNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN7PGAsync5TokenENS_9allocatorIS2_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPvPFvS1_ENS_9allocatorIvEEEE
+ __ZTVSt12out_of_range
+ __ZZ29+[_PGDisplay initSerialNumDB]E9onceToken
+ __ZZ32-[_PGDevice initWithDescriptor:]E9onceToken
+ __ZZ49-[_PGDeserializer initWithDevice:objectDelegate:]E9onceToken
+ __ZZ55-[_PGDisplay initWithDevice:descriptor:port:serialNum:]E11colorMatrix
+ __ZZ55-[_PGDisplay initWithDevice:descriptor:port:serialNum:]E7posData
+ __ZZ55-[_PGDisplay initWithDevice:descriptor:port:serialNum:]E7texData
+ __ZZ75-[PGDualPlaneSharedTextureBackingResource pageTextureInEncoder:isDownload:]E11blitOptions
+ __ZZL29pixelFormatForIOSurfaceFormatP9_PGDevicejP14MTLPixelFormatPmE6logged
+ __ZZNSt3__18__format15__output_bufferIcEC1B8ne190102INS0_15__format_bufferINS_20back_insert_iteratorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEcEEEEPcmPT_ENUlSE_mPvE_8__invokeESE_mSH_
+ __ZZZ29-[_PGDevice resumeChildFifo:]EUb_E5count
+ ___111-[PGRemoteTask setObjectListOffset:objectListLength:placementListOffset:placementListLength:completionHandler:]_block_invoke
+ ___113-[PGRemoteTask heapTextureSizeAndAlign:serializerPayloadLength:replyVirtualOffset:replyLength:completionHandler:]_block_invoke
+ ___115-[_PGDisplayNub _presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]_block_invoke
+ ___121-[_PGDisplayNub _presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:]_block_invoke
+ ___126-[PGRemoteTask doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:]_block_invoke
+ ___20-[_PGDevice dealloc]_block_invoke
+ ___20-[_PGDevice unpause]_block_invoke
+ ___22-[_PGDevice wakeFifo:]_block_invoke
+ ___23-[PGEFIDisplay present]_block_invoke
+ ___23-[_PGDevice resumeFifo]_block_invoke
+ ___24-[PGEFIDisplay teardown]_block_invoke
+ ___24-[_PGDevice createFIFO:]_block_invoke
+ ___24-[_PGDevice deleteFIFO:]_block_invoke
+ ___24-[_PGDevice deleteFIFO:]_block_invoke_2
+ ___25-[_PGDisplayNub doorbell]_block_invoke
+ ___25-[_PGDisplayNub doorbell]_block_invoke_2
+ ___27-[_PGDevice setupReporting]_block_invoke
+ ___29+[_PGDisplay initSerialNumDB]_block_invoke
+ ___29-[PGLocalTask setupTaskRoot:]_block_invoke
+ ___29-[_PGDevice resumeChildFifo:]_block_invoke
+ ___29-[_PGDisplayNub _cursorShow:]_block_invoke
+ ___29-[_PGDisplayNub _sleepState:]_block_invoke
+ ___30-[PGIOSurfaceHostDevice reset]_block_invoke
+ ___30-[PGRemoteTask flushResources]_block_invoke
+ ___31-[PGEFIDisplay initWithDevice:]_block_invoke
+ ___31-[_PGDevice signalFaultInFIFO:]_block_invoke
+ ___32-[PGIOSurfaceHostDevice dealloc]_block_invoke
+ ___32-[_PGDevice initWithDescriptor:]_block_invoke
+ ___34-[PGIOSurfaceHostDevice saveState]_block_invoke
+ ___34-[_PGDevice serializeSuspendState]_block_invoke
+ ___34-[_PGDisplay signalResponsiveness]_block_invoke
+ ___37-[PGEFIDisplay scheduleFramePresents]_block_invoke
+ ___37-[PGEFIDisplay updateFramebufferMode]_block_invoke
+ ___37-[PGFIFO initWithDevice:lastPending:]_block_invoke
+ ___44-[PGIOSurfaceHostDevice initWithDescriptor:]_block_invoke
+ ___44-[PGIOSurfaceHostDevice resetWithMemoryMap:]_block_invoke
+ ___46-[PGRemoteTask fifoDeleted:completionHandler:]_block_invoke
+ ___48-[PGLocalTask copyFromVirtualOffset:length:dst:]_block_invoke
+ ___48-[PGLocalTask mapMemoryInternalAtOffset:length:]_block_invoke
+ ___49-[PGIOSurfaceHostDevice mmioWriteAtOffset:value:]_block_invoke
+ ___49-[PGIOSurfaceHostDevice mmioWriteAtOffset:value:]_block_invoke_2
+ ___49-[PGIOSurfaceHostDevice mmioWriteAtOffset:value:]_block_invoke_3
+ ___49-[PGRemoteTask deleteResource:completionHandler:]_block_invoke
+ ___49-[_PGDeserializer initWithDevice:objectDelegate:]_block_invoke
+ ___50-[PGRemoteTask replacePhysical:completionHandler:]_block_invoke
+ ___51-[PGLocalTask legacyMappedAddressForOffset:length:]_block_invoke
+ ___52-[PGIOSurfaceHostDevice retainSurfaceWithMappingID:]_block_invoke
+ ___53-[PGIOSurfaceHostDevice restoreWithSavedState:error:]_block_invoke
+ ___53-[PGLocalTask newVirtualMapping:length:needWritable:]_block_invoke
+ ___54-[PGRemoteTask initWithDevice:taskRoot:length:taskID:]_block_invoke
+ ___54-[PGRemoteTask initWithDevice:taskRoot:length:taskID:]_block_invoke_2
+ ___55-[PGLocalTask newMemoryMapBufferForVirtualPage:length:]_block_invoke
+ ___55-[_PGDisplay initWithDevice:descriptor:port:serialNum:]_block_invoke
+ ___57-[PGRemoteTask discardResources:count:completionHandler:]_block_invoke
+ ___59-[PGFIFO CmdMapMemory2:stampValue:withPayload:payloadSize:]_block_invoke
+ ___60-[PGDetachBufferResource initWithTask:descriptor:placement:]_block_invoke
+ ___60-[PGFIFO CmdUnmapMemory:stampValue:withPayload:payloadSize:]_block_invoke
+ ___60-[PGRemoteTask invalidateResources:count:completionHandler:]_block_invoke
+ ___60-[PGRemoteTask resetRasterizationRateMap:completionHandler:]_block_invoke
+ ___61-[PGFIFO CmdDeleteObject:stampValue:withPayload:payloadSize:]_block_invoke
+ ___61-[PGRemoteTask unmapMemoryAtOffset:length:completionHandler:]_block_invoke
+ ___62-[PGFIFO CmdExecIndirect2:stampValue:withPayload:payloadSize:]_block_invoke
+ ___62-[PGFIFO CmdExecIndirect3:stampValue:withPayload:payloadSize:]_block_invoke
+ ___62-[PGFIFO CmdSetObjectList:stampValue:withPayload:payloadSize:]_block_invoke
+ ___62-[_PGDisplay encodeRenderFrame:toDisplay:withCmdBuf:viewport:]_block_invoke
+ ___63-[PGFIFO CmdDeleteResource:stampValue:withPayload:payloadSize:]_block_invoke
+ ___63-[PGFIFO CmdGetComputeInfo:stampValue:withPayload:payloadSize:]_block_invoke
+ ___64-[PGFIFO CmdReplacePhysical:stampValue:withPayload:payloadSize:]_block_invoke
+ ___65-[PGFIFO CmdDiscardResources:stampValue:withPayload:payloadSize:]_block_invoke
+ ___67-[PGBaseTask synchronizeResources:count:discard:completionHandler:]_block_invoke
+ ___67-[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:]_block_invoke
+ ___68-[PGFIFO CmdInvalidateResources:stampValue:withPayload:payloadSize:]_block_invoke
+ ___68-[_PGDisplayNub compositorParametersConfigEpoch:origin:scaleFactor:]_block_invoke
+ ___69-[PGFIFO CmdSynchronizeResources:stampValue:withPayload:payloadSize:]_block_invoke
+ ___69-[PGRemoteTask getComputeInfo:maxKey:count:offset:completionHandler:]_block_invoke
+ ___69-[PGRemoteTask synchronizeResources:count:discard:completionHandler:]_block_invoke
+ ___72-[PGFIFO CmdDeleteIOSurfaceBacking2:stampValue:withPayload:payloadSize:]_block_invoke
+ ___72-[PGFIFO CmdHeapTextureSizeAndAlign:stampValue:withPayload:payloadSize:]_block_invoke
+ ___74-[PGFIFO CmdResetRasterizationRateMap:stampValue:withPayload:payloadSize:]_block_invoke
+ ___74-[PGFIFO CmdSetObjectAndPlacementList:stampValue:withPayload:payloadSize:]_block_invoke
+ ___75-[PGFIFO CmdDeleteSharedTextureBacking:stampValue:withPayload:payloadSize:]_block_invoke
+ ___79-[PGFIFO CmdSynchronizeAndDiscardResources:stampValue:withPayload:payloadSize:]_block_invoke
+ ___81-[_PGDisplay modeChangeWidth:height:iosurfacePixelFormat:protectionRequirements:]_block_invoke
+ ___84-[PGRemoteTask deleteObjectWithSerializedData:serializedDataSize:completionHandler:]_block_invoke
+ ___97-[PGLocalTask doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:]_block_invoke
+ ___98-[_PGDisplayNub _cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___ZL20getDeviceInfoStructsPK9_PGDevicePK15APVKeyValuePair_block_invoke.cold.1
+ ____Z17newFunctionWithIRPU19objcproto9MTLDevice11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEE5PGPtrIP6NSDataE_block_invoke
+ ____Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement_block_invoke
+ ____ZL20getDeviceInfoStructsPK9_PGDevicePK15APVKeyValuePair_block_invoke
+ ___block_descriptor_32_e12_v24?0^v8Q16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e20_v20?0I8"NSError"12l
+ ___block_descriptor_40_e8_32b_e5_v8?0l
+ ___block_descriptor_40_e8_32c20_ZTS5PGPtrIP6NSDataE_e5_v8?0l
+ ___block_descriptor_40_e8_32o_e11_B24?0Q8Q16l
+ ___block_descriptor_40_e8_32o_e12_v24?0^v8Q16l
+ ___block_descriptor_40_e8_32o_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_40_e8_32o_e36_v16?0^{PGPhysicalMemoryRange_s=QQ}8l
+ ___block_descriptor_40_e8_32o_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e15_B32?0Q8Q16^v24l
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e8_v12?0I8l
+ ___block_descriptor_41_e8_32o_e5_v8?0l
+ ___block_descriptor_44_e8_32o_e5_v8?0l
+ ___block_descriptor_44_e8_32w_e8_v12?0I8l
+ ___block_descriptor_48_e8_32o40b_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_48_e8_32o40o_e5_v8?0l
+ ___block_descriptor_48_e8_32o40r_e20_v20?0I8"NSError"12l
+ ___block_descriptor_48_e8_32o40r_e5_v8?0l
+ ___block_descriptor_48_e8_32o_e20_v20?0I8"NSError"12l
+ ___block_descriptor_48_e8_32o_e5_v8?0l
+ ___block_descriptor_52_e8_32o40o_e5_v8?0l
+ ___block_descriptor_52_e8_32o40r_e5_v8?0l
+ ___block_descriptor_52_e8_32o_e5_v8?0l
+ ___block_descriptor_53_e8_32o_e5_v8?0l
+ ___block_descriptor_56_e8_32o40c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE_e8_v12?0I8l
+ ___block_descriptor_56_e8_32o40r_e5_v8?0l
+ ___block_descriptor_60_e8_32o_e5_v8?0l
+ ___block_descriptor_64_e8_32o40o48c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE_e11_v16?0I8i12l
+ ___block_descriptor_64_e8_32o40r48r56r_e14_B24?0Q8I16I20l
+ ___block_descriptor_64_e8_32r40r48r56r_e14_B24?0Q8I16I20l
+ ___block_descriptor_72_e8_32c99_ZTSKNSt3__113unordered_setI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE_e8_B12?0i8l
+ ___block_descriptor_72_e8_32o40b_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_80_e8_32o40r48r_e14_B24?0Q8I16I20l
+ ___block_descriptor_88_e8_32o40r48r56c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE72c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE_e22_v24?0I8"NSData"12I20l
+ ___block_descriptor_88_e8_32o40r48r56r64r72r80r_e14_B24?0Q8I16I20l
+ ___block_descriptor_88_e8_32o_e5_v8?0l
+ ___block_literal_global
+ ___checkCapabilities_block_invoke
+ ___clang_call_terminate
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32c20_ZTS5PGPtrIP6NSDataE
+ ___copy_helper_block_e8_32c99_ZTSKNSt3__113unordered_setI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE
+ ___copy_helper_block_e8_32o
+ ___copy_helper_block_e8_32o40b
+ ___copy_helper_block_e8_32o40c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___copy_helper_block_e8_32o40o
+ ___copy_helper_block_e8_32o40o48c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___copy_helper_block_e8_32o40r
+ ___copy_helper_block_e8_32o40r48r
+ ___copy_helper_block_e8_32o40r48r56c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE72c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___copy_helper_block_e8_32o40r48r56r
+ ___copy_helper_block_e8_32o40r48r56r64r72r80r
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32r40r48r56r
+ ___copy_helper_block_e8_32w
+ ___cxa_end_catch
+ ___cxa_pure_virtual
+ ___cxa_rethrow
+ ___destroy_helper_block_e8_32b
+ ___destroy_helper_block_e8_32c20_ZTS5PGPtrIP6NSDataE
+ ___destroy_helper_block_e8_32c99_ZTSKNSt3__113unordered_setI16APVDeviceInfoKeyNS_4hashIS1_EENS_8equal_toIS1_EENS_9allocatorIS1_EEEE
+ ___destroy_helper_block_e8_32o
+ ___destroy_helper_block_e8_32o40b
+ ___destroy_helper_block_e8_32o40c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___destroy_helper_block_e8_32o40o
+ ___destroy_helper_block_e8_32o40o48c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___destroy_helper_block_e8_32o40r
+ ___destroy_helper_block_e8_32o40r48r
+ ___destroy_helper_block_e8_32o40r48r56c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE72c42_ZTSNSt3__110shared_ptrIN7PGAsync5TokenEEE
+ ___destroy_helper_block_e8_32o40r48r56r
+ ___destroy_helper_block_e8_32o40r48r56r64r72r80r
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r40r48r56r
+ ___destroy_helper_block_e8_32w
+ ___udivti3
+ ___umodti3
+ ___writeIOSurfaceHostDeviceSaveState_block_invoke
+ __block_literal_global.142
+ __checkCapabilities_block_invoke.1
+ __dispatch_data_destructor_free
+ _gPGIOSurfaceHostDevice
+ _memchr
+ _memset
+ _objc_msgSend$CmdDebug:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDefineChildFIFO:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDefineTask2:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDelay:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteChildFIFO:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteIOSurfaceBacking2:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteObject:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteResource:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteSharedTextureBacking:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeleteTask:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDeprecated:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDiscardResources:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayAck:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayCompositorParameters:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayCursorGlyph:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayCursorShow:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplaySetGuestICCProfile:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplaySetProperties:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplaySetSharedStatePage:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplaySleepState:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplaySwapMapping:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayTransaction2_DEPRECATED:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdDisplayTransaction3:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdExecIndirect2:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdExecIndirect3:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdGetComputeInfo:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdGetDeviceInfo:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdHeapTextureSizeAndAlign:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdInvalidateResources:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdMapMemory2:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdNOP:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdReplacePhysical:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdResetRasterizationRateMap:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdSetObjectAndPlacementList:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdSetObjectList:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdSynchronizeAndDiscardResources:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdSynchronizeResources:stampValue:withPayload:payloadSize:
+ _objc_msgSend$CmdUnmapMemory:stampValue:withPayload:payloadSize:
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:
+ _objc_msgSend$_cursorShow:
+ _objc_msgSend$_presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:
+ _objc_msgSend$_presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:
+ _objc_msgSend$_sleepState:
+ _objc_msgSend$_xpcConnection
+ _objc_msgSend$ack:
+ _objc_msgSend$addCompletedHandler:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addTraceRange
+ _objc_msgSend$addTraceRange:handler:
+ _objc_msgSend$addWait:waitingFor:value:
+ _objc_msgSend$addressRangesForVirtualPage:length:readOnly:
+ _objc_msgSend$advance
+ _objc_msgSend$allValues
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowLibrariesFromOtherPlatforms
+ _objc_msgSend$appendData:
+ _objc_msgSend$areRasterOrderGroupsSupported
+ _objc_msgSend$arrayLength
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$async
+ _objc_msgSend$attachDisplay:port:
+ _objc_msgSend$backFaceStencil
+ _objc_msgSend$backingForID:
+ _objc_msgSend$barrierWait:barrier:
+ _objc_msgSend$baseAddress
+ _objc_msgSend$bitmapData
+ _objc_msgSend$blitCommandEncoder
+ _objc_msgSend$blitDownQueue
+ _objc_msgSend$blitInRGB_2P_XR10_A8_pipeline
+ _objc_msgSend$blitOutRGB_2P_XR10_A8_pipeline
+ _objc_msgSend$blitUpQueue
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bytes
+ _objc_msgSend$cancelFramePresents
+ _objc_msgSend$checkBuffer:bufferOffset:forSize:
+ _objc_msgSend$checkEnableProtectedContent:
+ _objc_msgSend$checkSuspendDeviceInfo:error:
+ _objc_msgSend$client
+ _objc_msgSend$colorAttachments
+ _objc_msgSend$colorSpace
+ _objc_msgSend$commandBuffer
+ _objc_msgSend$commandLength
+ _objc_msgSend$commit
+ _objc_msgSend$completeResources:sync:completionHandler:
+ _objc_msgSend$compositorParametersConfigEpoch:origin:scaleFactor:
+ _objc_msgSend$compositorParametersHandler
+ _objc_msgSend$compositorSupportsLiveResize
+ _objc_msgSend$computeCommandEncoder
+ _objc_msgSend$computeCommandEncoderWithDescriptor:
+ _objc_msgSend$configEpoch
+ _objc_msgSend$connectionType
+ _objc_msgSend$containsString:
+ _objc_msgSend$contents
+ _objc_msgSend$copy
+ _objc_msgSend$copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
+ _objc_msgSend$copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:
+ _objc_msgSend$copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:
+ _objc_msgSend$copyFromVirtualOffset:length:dst:
+ _objc_msgSend$copyParameterDataToBuffer:offset:
+ _objc_msgSend$copy_GuestBGRA_ToHostBGRA_Task:virtualOffset:mappedLength:stride:buffer:width:height:sum:
+ _objc_msgSend$copy_GuestBGRA_toHostRGBA_Task:virtualOffset:mappedLength:stride:buffer:width:height:sum:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createFIFO:
+ _objc_msgSend$createFIFOInternal:restoring:
+ _objc_msgSend$createPlaneDictionaries:
+ _objc_msgSend$createPlaneDictionary:
+ _objc_msgSend$createRootFifo
+ _objc_msgSend$createSharedTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:
+ _objc_msgSend$createSurfaceDictionaryWithDescriptor:hostData:
+ _objc_msgSend$createTask
+ _objc_msgSend$createTask:taskInfo:
+ _objc_msgSend$createTaskID:taskRoot:length:restoring:
+ _objc_msgSend$createTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:
+ _objc_msgSend$currentCommandOffset
+ _objc_msgSend$cursorFromVirtualOffset:length:
+ _objc_msgSend$cursorGlyphHandler
+ _objc_msgSend$cursorGlyphHandler2
+ _objc_msgSend$cursorGlyphVirtualOffset:mappedLength:stride:width:height:hotSpotX:hotSpotY:sum:
+ _objc_msgSend$cursorMoveHandler
+ _objc_msgSend$cursorPosition
+ _objc_msgSend$cursorShow:
+ _objc_msgSend$cursorShowHandler
+ _objc_msgSend$dataFromVirtualOffset:length:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$decodeBarrierResourcesWithIterator:
+ _objc_msgSend$decodeBarrierScopeWithIterator:
+ _objc_msgSend$decodeBlitUpdateFenceWithIterator:
+ _objc_msgSend$decodeBlitWaitForFenceWithIterator:
+ _objc_msgSend$decodeBufferHostResourceInfoWithIterator:
+ _objc_msgSend$decodeComputePassDescriptor:
+ _objc_msgSend$decodeComputePipelineImageBlockMemoryLengthWithIterator:
+ _objc_msgSend$decodeComputePipelineStateInfoWithIterator:
+ _objc_msgSend$decodeCopyFromBufferToBufferWithIterator:
+ _objc_msgSend$decodeCopyFromBufferToTextureWithIterator:
+ _objc_msgSend$decodeCopyFromTextureToBufferWithIterator:
+ _objc_msgSend$decodeCopyFromTextureToTextureWithIterator:
+ _objc_msgSend$decodeCopyFromTextureToTextureWithNumSliceLevelWithIterator:
+ _objc_msgSend$decodeCopyFromTextureToTextureWithOptionsWithIterator:
+ _objc_msgSend$decodeCopyRasterizationRateParameterBufferWithIterator:
+ _objc_msgSend$decodeDispatchThreadgroupsIndirectWithIterator:
+ _objc_msgSend$decodeDispatchThreadgroupsWithIterator:
+ _objc_msgSend$decodeDispatchThreadsPerTileInRegionWithIndexWithIterator:
+ _objc_msgSend$decodeDispatchThreadsPerTileInRegionWithIterator:
+ _objc_msgSend$decodeDispatchThreadsPerTileWithIterator:
+ _objc_msgSend$decodeDispatchThreadsWithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedBasePrimitives16WithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedBasePrimitives16_2WithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedBasePrimitives64WithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedBasePrimitives64_2WithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedPrimitives16WithIterator:
+ _objc_msgSend$decodeDrawIndexedInstancedPrimitives64WithIterator:
+ _objc_msgSend$decodeDrawIndexedPatches16WithIterator:
+ _objc_msgSend$decodeDrawIndexedPatches64WithIterator:
+ _objc_msgSend$decodeDrawIndexedPatchesIndirectWithIterator:
+ _objc_msgSend$decodeDrawIndexedPrimitives16WithIterator:
+ _objc_msgSend$decodeDrawIndexedPrimitives64WithIterator:
+ _objc_msgSend$decodeDrawIndexedPrimitivesIndirectWithIterator:
+ _objc_msgSend$decodeDrawInstancedBasePrimitives16WithIterator:
+ _objc_msgSend$decodeDrawInstancedBasePrimitives64WithIterator:
+ _objc_msgSend$decodeDrawInstancedPrimitives16WithIterator:
+ _objc_msgSend$decodeDrawInstancedPrimitives64WithIterator:
+ _objc_msgSend$decodeDrawPatches16WithIterator:
+ _objc_msgSend$decodeDrawPatches64WithIterator:
+ _objc_msgSend$decodeDrawPatchesIndirectWithIterator:
+ _objc_msgSend$decodeDrawPrimitives16WithIterator:
+ _objc_msgSend$decodeDrawPrimitives64WithIterator:
+ _objc_msgSend$decodeDrawPrimitivesIndirectWithIterator:
+ _objc_msgSend$decodeEncodeEndDoWhile:
+ _objc_msgSend$decodeEncodeEndIf:
+ _objc_msgSend$decodeEncodeEndWhile:
+ _objc_msgSend$decodeEncodeStartDoWhile:
+ _objc_msgSend$decodeEncodeStartElse:
+ _objc_msgSend$decodeEncodeStartIf:
+ _objc_msgSend$decodeEncodeStartWhile:
+ _objc_msgSend$decodeExecuteCommandsInBufferRangedWithIterator:
+ _objc_msgSend$decodeExecuteCommandsInBufferWithIterator:
+ _objc_msgSend$decodeFillBufferWithIterator:
+ _objc_msgSend$decodeFillBufferWithPatternWithIterator:
+ _objc_msgSend$decodeFillTextureWithBytesWithIterator:
+ _objc_msgSend$decodeFillTextureWithColorWithIterator:
+ _objc_msgSend$decodeGenerateMipmapsWithIterator:
+ _objc_msgSend$decodeGetRasterizationRateMapInfoWithIterator:
+ _objc_msgSend$decodeGetTileDimensionsWithIterator:
+ _objc_msgSend$decodeHeapHostResourceInfoWithIterator:
+ _objc_msgSend$decodeHeapTextureDescriptorSizeAndAlignWithIterator:
+ _objc_msgSend$decodeImageBlockSampleLengthWithIterator:descriptor:
+ _objc_msgSend$decodeInsertCompressedTextureReinterpretationFlush:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeInvalidateCompressedTextureImageWithIterator:
+ _objc_msgSend$decodeInvalidateCompressedTextureWithIterator:
+ _objc_msgSend$decodeMapPhysicalToScreenCoordinatesMultipleWithIterator:
+ _objc_msgSend$decodeMapPhysicalToScreenCoordinatesWithIterator:
+ _objc_msgSend$decodeMapScreenToPhysicalCoordinatesWithIterator:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$decodeObjectUniqueIdentifier:
+ _objc_msgSend$decodeOptimizeForCPUAccessWithIterator:
+ _objc_msgSend$decodeOptimizeForGPUAccessWithIterator:
+ _objc_msgSend$decodeOptimizeImageForCPUAccessWithIterator:
+ _objc_msgSend$decodeOptimizeImageForGPUAccessWithIterator:
+ _objc_msgSend$decodeRenderBarrierResourcesWithIterator:
+ _objc_msgSend$decodeRenderBarrierScopeWithIterator:
+ _objc_msgSend$decodeRenderDescribeRenderPassWithIterator:descriptor:
+ _objc_msgSend$decodeRenderPassDescriptor:
+ _objc_msgSend$decodeRenderPipelineImageBlockMemoryLengthWithIterator:
+ _objc_msgSend$decodeRenderPipelineStateInfoWithIterator:
+ _objc_msgSend$decodeRenderUpdateFenceWithIterator:
+ _objc_msgSend$decodeRenderWaitForFenceWithIterator:
+ _objc_msgSend$decodeSamplerStateHostResourceInfoWithIterator:
+ _objc_msgSend$decodeSegmentWithHeader:withIterator:withDecoder:into:
+ _objc_msgSend$decodeSegments:lengths:count:into:
+ _objc_msgSend$decodeSetAlphaTestReferenceValueWithIterator:
+ _objc_msgSend$decodeSetBlendColorWithIterator:
+ _objc_msgSend$decodeSetBufferOffsetWithIterator:
+ _objc_msgSend$decodeSetBufferOffsetWithStrideWithIterator:
+ _objc_msgSend$decodeSetBuffersWithIterator:
+ _objc_msgSend$decodeSetBuffersWithStrideWithIterator:
+ _objc_msgSend$decodeSetClipPlaneWithIterator:
+ _objc_msgSend$decodeSetColorResolveTextureWithIterator:
+ _objc_msgSend$decodeSetColorStoreActionOptionsWithIterator:
+ _objc_msgSend$decodeSetColorStoreActionWithIterator:
+ _objc_msgSend$decodeSetComputePassDispatchTypeWithIterator:descriptor:
+ _objc_msgSend$decodeSetCullModeWithIterator:
+ _objc_msgSend$decodeSetDefaultColorSampleCountWithIterator:descriptor:
+ _objc_msgSend$decodeSetDefaultRasterSampleCountWithIterator:descriptor:
+ _objc_msgSend$decodeSetDepthBiasWithIterator:
+ _objc_msgSend$decodeSetDepthClearedWithIterator:
+ _objc_msgSend$decodeSetDepthClipModeWithIterator:
+ _objc_msgSend$decodeSetDepthResolveTextureWithIterator:
+ _objc_msgSend$decodeSetDepthStencilStateWithIterator:
+ _objc_msgSend$decodeSetDepthStoreActionWithIterator:
+ _objc_msgSend$decodeSetFragmentBufferOffsetWithIterator:
+ _objc_msgSend$decodeSetFragmentBuffersWithIterator:
+ _objc_msgSend$decodeSetFragmentSamplerStateWithIterator:
+ _objc_msgSend$decodeSetFragmentSamplerStatesLODClampWithIterator:
+ _objc_msgSend$decodeSetFragmentSamplerStatesWithIterator:
+ _objc_msgSend$decodeSetFragmentTexturesWithIterator:
+ _objc_msgSend$decodeSetFrontFacingWindingWithIterator:
+ _objc_msgSend$decodeSetImageblockWidthWithIterator:
+ _objc_msgSend$decodeSetLineWidthWithIterator:
+ _objc_msgSend$decodeSetPipelineStateWithIterator:
+ _objc_msgSend$decodeSetPointSizeWithIterator:
+ _objc_msgSend$decodeSetPrimitiveRestartIndexEnabledWithIterator:
+ _objc_msgSend$decodeSetProgrammableSamplePositionsWithIterator:descriptor:
+ _objc_msgSend$decodeSetProvokingVertexModeWithIterator:
+ _objc_msgSend$decodeSetRenderPipelineStateWithIterator:
+ _objc_msgSend$decodeSetRenderThreadgroupMemoryLengthWithIterator:
+ _objc_msgSend$decodeSetSamplersLODClampWithIterator:
+ _objc_msgSend$decodeSetSamplersWithIterator:
+ _objc_msgSend$decodeSetScissorRectWithIterator:
+ _objc_msgSend$decodeSetScissorRectsWithIterator:
+ _objc_msgSend$decodeSetStageInRegionIndirectWithIterator:
+ _objc_msgSend$decodeSetStageInRegionWithIterator:
+ _objc_msgSend$decodeSetStencilClearedWithIterator:
+ _objc_msgSend$decodeSetStencilRefWithIterator:
+ _objc_msgSend$decodeSetStencilResolveTextureWithIterator:
+ _objc_msgSend$decodeSetStencilStoreActionOptionsWithIterator:
+ _objc_msgSend$decodeSetStencilStoreActionWithIterator:
+ _objc_msgSend$decodeSetTesselationFactorBufferWithIterator:
+ _objc_msgSend$decodeSetTesselationFactorScaleWithIterator:
+ _objc_msgSend$decodeSetTexturesWithIterator:
+ _objc_msgSend$decodeSetThreadGroupMemoryLengthWithIterator:descriptor:
+ _objc_msgSend$decodeSetThreadgroupMemoryLengthWithIterator:
+ _objc_msgSend$decodeSetTileBufferOffsetWithIterator:
+ _objc_msgSend$decodeSetTileBuffersWithIterator:
+ _objc_msgSend$decodeSetTileParametersWithIterator:descriptor:
+ _objc_msgSend$decodeSetTileSamplerStatesLODClampWithIterator:
+ _objc_msgSend$decodeSetTileSamplerStatesWithIterator:
+ _objc_msgSend$decodeSetTileTexturesWithIterator:
+ _objc_msgSend$decodeSetTransformFeedbackStateWithIterator:
+ _objc_msgSend$decodeSetTriangleFillModeFrontBackWithIterator:
+ _objc_msgSend$decodeSetTriangleFillModeWithIterator:
+ _objc_msgSend$decodeSetVariableRateRasterizationMapWithIterator:descriptor:
+ _objc_msgSend$decodeSetVertexAmplificationCountWithIterator:
+ _objc_msgSend$decodeSetVertexAmplificationModeWithIterator:
+ _objc_msgSend$decodeSetVertexBufferOffsetWithIterator:
+ _objc_msgSend$decodeSetVertexBufferOffsetWithStrideWithIterator:
+ _objc_msgSend$decodeSetVertexBuffersWithIterator:
+ _objc_msgSend$decodeSetVertexBuffersWithStrideWithIterator:
+ _objc_msgSend$decodeSetVertexSamplerStateWithIterator:
+ _objc_msgSend$decodeSetVertexSamplerStatesLODClampWithIterator:
+ _objc_msgSend$decodeSetVertexSamplerStatesWithIterator:
+ _objc_msgSend$decodeSetVertexTexturesWithIterator:
+ _objc_msgSend$decodeSetViewportTransformEnabledWithIterator:
+ _objc_msgSend$decodeSetViewportWithIterator:
+ _objc_msgSend$decodeSetViewportsWithIterator:
+ _objc_msgSend$decodeSetVisibilityResultModeWithIterator:
+ _objc_msgSend$decodeSynchronizeResourceWithIterator:
+ _objc_msgSend$decodeSynchronizeTextureImageWithIterator:
+ _objc_msgSend$decodeTextureBarrierWithIterator:
+ _objc_msgSend$decodeTextureHostResourceInfoWithIterator:
+ _objc_msgSend$decodeUpdateFenceWithIterator:
+ _objc_msgSend$decodeUseHeapsWithIterator:
+ _objc_msgSend$decodeUseHeapsWithStagesWithIterator:
+ _objc_msgSend$decodeUseResourcesWithIterator:
+ _objc_msgSend$decodeUseResourcesWithStagesWithIterator:
+ _objc_msgSend$decodeWaitForFenceWithIterator:
+ _objc_msgSend$decodeWithHeader:withIterator:
+ _objc_msgSend$decodeXPCObjectOfType:forKey:
+ _objc_msgSend$deleteBacking:completionHandler:
+ _objc_msgSend$deleteBufferForReference:
+ _objc_msgSend$deleteComputePipelineStateForReference:
+ _objc_msgSend$deleteDepthStencilStateForReference:
+ _objc_msgSend$deleteFIFO:
+ _objc_msgSend$deleteFenceForReference:
+ _objc_msgSend$deleteFunctionForReference:
+ _objc_msgSend$deleteHeapForReference:
+ _objc_msgSend$deleteObjectWithSerializedData:reply:
+ _objc_msgSend$deleteObjectWithSerializedData:serializedDataSize:completionHandler:
+ _objc_msgSend$deleteRasterizationRateMapForReference:
+ _objc_msgSend$deleteRenderPipelineStateForReference:
+ _objc_msgSend$deleteResource:completionHandler:
+ _objc_msgSend$deleteResource:reply:
+ _objc_msgSend$deleteSamplerStateForReference:
+ _objc_msgSend$deleteTaskID:
+ _objc_msgSend$deleteTextureForReference:
+ _objc_msgSend$depth
+ _objc_msgSend$depthAttachment
+ _objc_msgSend$describePending
+ _objc_msgSend$description
+ _objc_msgSend$descriptorPrivate
+ _objc_msgSend$destroyTask
+ _objc_msgSend$destroyTask:
+ _objc_msgSend$detachBacking
+ _objc_msgSend$detachDisplay:port:
+ _objc_msgSend$device
+ _objc_msgSend$deviceFeatureLevel
+ _objc_msgSend$deviceLinearTextureAlignmentBytes
+ _objc_msgSend$deviceTraceId
+ _objc_msgSend$devolatilize
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didModifyData
+ _objc_msgSend$didModifyRange:
+ _objc_msgSend$discard
+ _objc_msgSend$discardResources:count:completionHandler:
+ _objc_msgSend$discardResources:count:reply:
+ _objc_msgSend$dispatchThreadgroups:threadsPerThreadgroup:
+ _objc_msgSend$dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$dispatchThreadsPerTile:
+ _objc_msgSend$dispatchThreadsPerTile:inRegion:
+ _objc_msgSend$dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:
+ _objc_msgSend$displayPokePort:
+ _objc_msgSend$displayPortCount
+ _objc_msgSend$doExecIndirect:cmdBuffers:resourceList:fifoEvent:fifoEventValue:completionHandler:
+ _objc_msgSend$doExecIndirectWithCmdBufCount:commandData:stampIndex:fifoEvent:fifoEventValue:resourceCount:completionHandler:
+ _objc_msgSend$doesNotRecognizeSelector:
+ _objc_msgSend$doorbell
+ _objc_msgSend$drain
+ _objc_msgSend$drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:
+ _objc_msgSend$drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:
+ _objc_msgSend$drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:
+ _objc_msgSend$drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:
+ _objc_msgSend$drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:
+ _objc_msgSend$drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:
+ _objc_msgSend$drawPrimitives:indirectBuffer:indirectBufferOffset:
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:instanceCount:
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:
+ _objc_msgSend$enableArgumentBuffers
+ _objc_msgSend$enableFifo
+ _objc_msgSend$enableProcessIsolation
+ _objc_msgSend$enableProtectedContent
+ _objc_msgSend$encodeEndDoWhile:offset:comparison:referenceValue:
+ _objc_msgSend$encodeEndIf
+ _objc_msgSend$encodeEndWhile
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encodeRenderFrame:toDisplay:withCmdBuf:viewport:
+ _objc_msgSend$encodeSignalEvent:value:
+ _objc_msgSend$encodeStartDoWhile
+ _objc_msgSend$encodeStartElse
+ _objc_msgSend$encodeStartIf:offset:comparison:referenceValue:
+ _objc_msgSend$encodeStartWhile:offset:comparison:referenceValue:
+ _objc_msgSend$encodeWaitForEvent:value:
+ _objc_msgSend$encodeXPCObject:forKey:
+ _objc_msgSend$endEncoding
+ _objc_msgSend$ensurePhysical
+ _objc_msgSend$error
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$evictInComputeEncoder:
+ _objc_msgSend$evictInEncoder:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$execIndirect2WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:
+ _objc_msgSend$execIndirect3WithCmdBufCount:cmdBuffers:resourceCount:resources:stampIndex:fifoEvent:fifoEventValue:completionHandler:
+ _objc_msgSend$execIndirect3WithData:cmdBufferCount:resourceCount:stampIndex:fifoEventValueIn:gpuCompletion:reply:
+ _objc_msgSend$execQueue
+ _objc_msgSend$fault
+ _objc_msgSend$faultAtOffset:stampValue:
+ _objc_msgSend$faultAtStampValue:
+ _objc_msgSend$faultOffset
+ _objc_msgSend$features
+ _objc_msgSend$fifoDeleted:completionHandler:
+ _objc_msgSend$fifoDeleted:reply:
+ _objc_msgSend$fifoFaultOffset
+ _objc_msgSend$fifoForStampIndex:
+ _objc_msgSend$fillBuffer:range:pattern4:
+ _objc_msgSend$fillBuffer:range:value:
+ _objc_msgSend$fillTexture:level:slice:region:bytes:length:
+ _objc_msgSend$fillTexture:level:slice:region:color:pixelFormat:
+ _objc_msgSend$finishRestore
+ _objc_msgSend$finishWait:
+ _objc_msgSend$floatValue
+ _objc_msgSend$flushResources
+ _objc_msgSend$flushResourcesWithReply:
+ _objc_msgSend$frontFaceStencil
+ _objc_msgSend$functionNames
+ _objc_msgSend$generateMipmapsForTexture:
+ _objc_msgSend$getBuffer
+ _objc_msgSend$getBufferForReference:
+ _objc_msgSend$getBufferForReferenceNonNull:
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$getComputeInfo:maxKey:count:offset:completionHandler:
+ _objc_msgSend$getComputeInfo:maxKey:count:offset:reply:
+ _objc_msgSend$getComputePipelineStateForReference:
+ _objc_msgSend$getComputePipelineStateForReferenceNonNull:
+ _objc_msgSend$getDepthStencilStateForReference:
+ _objc_msgSend$getDeviceInfo:length:dst:
+ _objc_msgSend$getDirtyColorMatrix
+ _objc_msgSend$getDisplayNubAtPort:
+ _objc_msgSend$getEFIModeCount
+ _objc_msgSend$getEFIModeValue
+ _objc_msgSend$getEFIStrideAlignment
+ _objc_msgSend$getExistingHostResource:
+ _objc_msgSend$getFenceForReference:
+ _objc_msgSend$getFenceForReferenceNonNull:
+ _objc_msgSend$getFifoBytes:into:
+ _objc_msgSend$getFunctionForReference:
+ _objc_msgSend$getHeap
+ _objc_msgSend$getHeapForReference:
+ _objc_msgSend$getHeapForReferenceNonNull:
+ _objc_msgSend$getHostResource:
+ _objc_msgSend$getKernelTask
+ _objc_msgSend$getModeCount
+ _objc_msgSend$getModeValue
+ _objc_msgSend$getObject:entry:
+ _objc_msgSend$getRanges
+ _objc_msgSend$getRasterizationRateMapForReference:
+ _objc_msgSend$getRasterizationRateMapForReferenceNonNull:
+ _objc_msgSend$getRenderPipelineStateForReference:
+ _objc_msgSend$getRenderPipelineStateForReferenceNonNull:
+ _objc_msgSend$getResource
+ _objc_msgSend$getResourceForReference:
+ _objc_msgSend$getSamplerStateForReference:
+ _objc_msgSend$getSamplerStateForReferenceNonNull:
+ _objc_msgSend$getSharedTextureBackingID
+ _objc_msgSend$getStrideAlignment
+ _objc_msgSend$getTaskID:
+ _objc_msgSend$getTexture
+ _objc_msgSend$getTextureForReference:
+ _objc_msgSend$getTextureForReferenceNonNull:
+ _objc_msgSend$getUserTaskID:
+ _objc_msgSend$gpuAddress
+ _objc_msgSend$gpuCoreCount
+ _objc_msgSend$gpuResourceID
+ _objc_msgSend$guestColorSpace
+ _objc_msgSend$handshakeWithTaskRoot:taskSize:taskID:configuration:features:memoryMap:reply:
+ _objc_msgSend$hasGamma
+ _objc_msgSend$heapBufferSizeAndAlignWithLength:options:
+ _objc_msgSend$heapTextureSizeAndAlign:serializerPayloadLength:replyVirtualOffset:replyLength:completionHandler:
+ _objc_msgSend$heapTextureSizeAndAlignWithDescriptor:
+ _objc_msgSend$heapTextureSizeAndAlignWithSerializedData:replyVirtualOffset:replyLength:reply:
+ _objc_msgSend$height
+ _objc_msgSend$horizontalSampleStorage
+ _objc_msgSend$imageblockMemoryLengthForDimensions:
+ _objc_msgSend$imageblockSampleLength
+ _objc_msgSend$init
+ _objc_msgSend$initSerialNumDB
+ _objc_msgSend$initWaitingInfo
+ _objc_msgSend$initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
+ _objc_msgSend$initWithBuffer:
+ _objc_msgSend$initWithBytesNoCopy:length:deallocator:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithDescriptor:
+ _objc_msgSend$initWithDeserializer:
+ _objc_msgSend$initWithDeserializer:commandBuffer:
+ _objc_msgSend$initWithDevice:
+ _objc_msgSend$initWithDevice:baseNode:fifoIndex:restoring:lastPending:
+ _objc_msgSend$initWithDevice:descriptor:port:serialNum:
+ _objc_msgSend$initWithDevice:length:basePointer:startOffset:lastPending:
+ _objc_msgSend$initWithDevice:objectDelegate:
+ _objc_msgSend$initWithDevice:port:sharedStatePage:
+ _objc_msgSend$initWithDevice:taskRoot:length:taskID:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithProperties:
+ _objc_msgSend$initWithRange:
+ _objc_msgSend$initWithRanges:count:
+ _objc_msgSend$initWithResourceManager:
+ _objc_msgSend$initWithRoot:depth:allowHoles:read:
+ _objc_msgSend$initWithSampleCount:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithSize:memoryMap:
+ _objc_msgSend$initWithTarget:selector:object:
+ _objc_msgSend$initWithTask:descriptor:placement:
+ _objc_msgSend$initWithTask:descriptor:planes:planeCount:
+ _objc_msgSend$initWithTask:mappingID:texture:
+ _objc_msgSend$initWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:
+ _objc_msgSend$initWithTask:objectType:texture:backing:
+ _objc_msgSend$initWithTask:pagingInfo:dimension:dimensionLength:texture:
+ _objc_msgSend$initWithTask:texture:sharedTextureBackingID:
+ _objc_msgSend$initWithTexture:
+ _objc_msgSend$initWithVirtualAddress:length:device:
+ _objc_msgSend$initWithVirtualAddress:length:writable:
+ _objc_msgSend$initWithVirtualOffset:length:taskInfo:device:
+ _objc_msgSend$insertCompressedTextureReinterpretationFlush
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$internalEncodeCurrentFrameToCommandBuffer:texture:region:
+ _objc_msgSend$interrupt
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateCompressedTexture:
+ _objc_msgSend$invalidateCompressedTexture:slice:level:
+ _objc_msgSend$invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:
+ _objc_msgSend$invalidateResources:count:completionHandler:
+ _objc_msgSend$invalidateResources:count:reply:
+ _objc_msgSend$ioSurface
+ _objc_msgSend$ioSurfaceHostDevice
+ _objc_msgSend$iosurface
+ _objc_msgSend$iosurfaceReadOnlyTextureAlignmentBytes
+ _objc_msgSend$iosurfaceTextureAlignmentBytes
+ _objc_msgSend$isDepth24Stencil8PixelFormatSupported
+ _objc_msgSend$isFramebufferReadSupported
+ _objc_msgSend$isGuestValid
+ _objc_msgSend$isHostValid
+ _objc_msgSend$isLargeMRTSupported
+ _objc_msgSend$isQuiesced
+ _objc_msgSend$isRGB10A2GammaSupported
+ _objc_msgSend$isRootFifo
+ _objc_msgSend$isShareable
+ _objc_msgSend$latchCommandOffset
+ _objc_msgSend$layerCount
+ _objc_msgSend$layers
+ _objc_msgSend$legacyMappedAddressForOffset:length:
+ _objc_msgSend$length
+ _objc_msgSend$limits
+ _objc_msgSend$linearTextureAlignmentBytes
+ _objc_msgSend$loadAction
+ _objc_msgSend$logDeviceFeatureLevel
+ _objc_msgSend$mapMemory
+ _objc_msgSend$mapMemoryAtOffset:length:completionHandler:
+ _objc_msgSend$mapMemoryAtVirtualAddress:ranges:rangeCount:readOnly:
+ _objc_msgSend$mapMemoryAtVirtualOffset:rangeCount:ranges:readOnly:
+ _objc_msgSend$mapMemoryInTask:segmentCount:offset:readonly:ranges:
+ _objc_msgSend$mapMemoryInternalAtOffset:length:
+ _objc_msgSend$mapPhysicalToScreenCoordinates:forLayer:
+ _objc_msgSend$mapScreenToPhysicalCoordinates:forLayer:
+ _objc_msgSend$mapSurface:
+ _objc_msgSend$mappedAddressForOffset:length:needWritable:
+ _objc_msgSend$mappedAddressForPageNumber:length:
+ _objc_msgSend$mapperService
+ _objc_msgSend$maxComputeBuffers
+ _objc_msgSend$maxComputeLocalMemorySizes
+ _objc_msgSend$maxComputeSamplers
+ _objc_msgSend$maxComputeTextures
+ _objc_msgSend$maxComputeThreadgroupMemory
+ _objc_msgSend$maxComputeThreadgroupMemoryAlignmentBytes
+ _objc_msgSend$maxFragmentBuffers
+ _objc_msgSend$maxFragmentSamplers
+ _objc_msgSend$maxFragmentTextures
+ _objc_msgSend$maxNits
+ _objc_msgSend$maxPredicatedNestingDepth
+ _objc_msgSend$maxRasterizationRateLayerCount
+ _objc_msgSend$maxSDRNits
+ _objc_msgSend$maxTextureHeight2D
+ _objc_msgSend$maxTextureLayers
+ _objc_msgSend$maxTextureWidth2D
+ _objc_msgSend$maxThreadgroupMemoryLength
+ _objc_msgSend$maxThreadsPerThreadgroup
+ _objc_msgSend$maxTileBuffers
+ _objc_msgSend$maxTileSamplers
+ _objc_msgSend$maxTileTextures
+ _objc_msgSend$maxTotalComputeThreadsPerThreadgroup
+ _objc_msgSend$maxTotalThreadsPerThreadgroup
+ _objc_msgSend$maxVertexAmplificationCount
+ _objc_msgSend$maxVertexBuffers
+ _objc_msgSend$maxVertexSamplers
+ _objc_msgSend$maxVertexTextures
+ _objc_msgSend$maxViewportCount
+ _objc_msgSend$memoryBarrierWithResources:count:
+ _objc_msgSend$memoryBarrierWithScope:
+ _objc_msgSend$memoryBarrierWithScope:afterStages:beforeStages:
+ _objc_msgSend$memoryMap
+ _objc_msgSend$memoryMapDescriptor
+ _objc_msgSend$memoryMapMappedAddressForOffset:length:needWritable:
+ _objc_msgSend$minNits
+ _objc_msgSend$minimumLinearTextureAlignmentForPixelFormat:
+ _objc_msgSend$mipmapLevelCount
+ _objc_msgSend$mmioLength
+ _objc_msgSend$modeChangeHandler
+ _objc_msgSend$modeChangeWidth:height:iosurfacePixelFormat:protectionRequirements:
+ _objc_msgSend$modeList
+ _objc_msgSend$modeListResponsivenessChangeHandler
+ _objc_msgSend$mtlDevice
+ _objc_msgSend$mutability
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$needsComputePaging
+ _objc_msgSend$needsPrepare
+ _objc_msgSend$needsSync
+ _objc_msgSend$newAsyncToken
+ _objc_msgSend$newAsyncTokenWithBlock:
+ _objc_msgSend$newBufferForVirtualPage:length:
+ _objc_msgSend$newBufferResourceWithTask:objectType:descriptor:descriptorLength:placement:
+ _objc_msgSend$newBufferWithBytesNoCopy:length:options:deallocator:
+ _objc_msgSend$newBufferWithDescriptor:
+ _objc_msgSend$newBufferWithIOSurface:
+ _objc_msgSend$newBufferWithLength:options:
+ _objc_msgSend$newBufferWithLength:options:offset:
+ _objc_msgSend$newChildBufferResourceWithBuffer:
+ _objc_msgSend$newChildTextureResourceWithTexture:
+ _objc_msgSend$newCommandQueue
+ _objc_msgSend$newComputePipelineDescriptorWithSerializedData:deserializationContext:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:options:reflection:error:
+ _objc_msgSend$newComputePipelineStateWithFunction:error:
+ _objc_msgSend$newContiguousMapping:length:
+ _objc_msgSend$newContiguousMapping:length:readOnly:
+ _objc_msgSend$newDefaultLibraryWithBundle:error:
+ _objc_msgSend$newDepthStencilStateWithDescriptor:
+ _objc_msgSend$newEvent
+ _objc_msgSend$newFence
+ _objc_msgSend$newFrameEventHandler
+ _objc_msgSend$newFunctionWithName:
+ _objc_msgSend$newHeapResourceWithTask:objectType:descriptor:descriptorLength:placement:
+ _objc_msgSend$newHeapWithDescriptor:
+ _objc_msgSend$newLegacyBufferForVirtualPage:length:
+ _objc_msgSend$newLibraryWithData:error:
+ _objc_msgSend$newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:
+ _objc_msgSend$newMapperRefBufferWithTask:descriptor:descriptorLength:placement:
+ _objc_msgSend$newMemoryCursorForBuffer:
+ _objc_msgSend$newMemoryMapBufferForVirtualPage:length:
+ _objc_msgSend$newNormalBufferWithTask:descriptor:descriptorLength:placement:
+ _objc_msgSend$newNormalHeapResourceWithTask:descriptor:descriptorLength:placement:
+ _objc_msgSend$newRangeMapping:rangeCount:totalLength:readOnly:
+ _objc_msgSend$newRasterizationRateMapWithDescriptor:
+ _objc_msgSend$newRenderPipelineDescriptorWithSerializedData:deserializationContext:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:options:reflection:error:
+ _objc_msgSend$newRenderPipelineStateWithTileDescriptor:options:reflection:error:
+ _objc_msgSend$newSamplerStateWithDescriptor:
+ _objc_msgSend$newSharedEvent
+ _objc_msgSend$newSharedEventHandle
+ _objc_msgSend$newSharedTextureHandle
+ _objc_msgSend$newSharedTextureHandleForID:
+ _objc_msgSend$newSharedTextureWithDescriptor:
+ _objc_msgSend$newSharedTextureWithHandle:withResourceIndex:
+ _objc_msgSend$newTaskMapping:ranges:rangeCount:totalLength:offset:readOnly:
+ _objc_msgSend$newTextureViewWithPixelFormat:
+ _objc_msgSend$newTextureViewWithPixelFormat:resourceIndex:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:
+ _objc_msgSend$newTextureWithDescriptor:
+ _objc_msgSend$newTextureWithDescriptor:iosurface:plane:
+ _objc_msgSend$newTextureWithDescriptor:offset:
+ _objc_msgSend$newTextureWithDescriptor:offset:bytesPerRow:
+ _objc_msgSend$newTileRenderPipelineDescriptorWithSerializedData:deserializationContext:
+ _objc_msgSend$newTiledTextureWithBytesNoCopy:length:descriptor:offset:bytesPerRow:
+ _objc_msgSend$newVirtualMapping:length:needWritable:
+ _objc_msgSend$nextTraceID
+ _objc_msgSend$nub
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$optIntoUsingUnplugMethod
+ _objc_msgSend$optimizeContentsForCPUAccess:
+ _objc_msgSend$optimizeContentsForCPUAccess:slice:level:
+ _objc_msgSend$optimizeContentsForGPUAccess:
+ _objc_msgSend$optimizeContentsForGPUAccess:slice:level:
+ _objc_msgSend$origin
+ _objc_msgSend$pageTextureInEncoder:isDownload:
+ _objc_msgSend$pagingQueue
+ _objc_msgSend$parameterBufferSizeAndAlign
+ _objc_msgSend$pause
+ _objc_msgSend$physicalAddress
+ _objc_msgSend$physicalGranularity
+ _objc_msgSend$physicalLength
+ _objc_msgSend$physicalSizeForLayer:
+ _objc_msgSend$pipelineForDescriptor:
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$pixelFormatForBacking:
+ _objc_msgSend$poke
+ _objc_msgSend$prepareInComputeEncoder:
+ _objc_msgSend$prepareInEncoder:
+ _objc_msgSend$prepareResources:event:value:
+ _objc_msgSend$prepareSharedTextureBacking:
+ _objc_msgSend$preparedBackingForID:
+ _objc_msgSend$present
+ _objc_msgSend$presentFrame:iosurfacePixelFormat:protectionRequirements:task:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:colorMatrix:completionBlock:
+ _objc_msgSend$presentMappedSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:
+ _objc_msgSend$presentSurface:
+ _objc_msgSend$presentSurface:gammaTableVirtualOffset:gammaTableMappedLength:gammaTableEntryCount:gammaTableSum:
+ _objc_msgSend$protectionOptions
+ _objc_msgSend$pushStamp:cmdID:
+ _objc_msgSend$queue
+ _objc_msgSend$quiesce
+ _objc_msgSend$raise:format:
+ _objc_msgSend$raiseInterrupt
+ _objc_msgSend$read
+ _objc_msgSend$read:length:dst:
+ _objc_msgSend$readFromPhysicalAddress:length:dst:
+ _objc_msgSend$readInterruptFault
+ _objc_msgSend$readMemory
+ _objc_msgSend$refreshRate
+ _objc_msgSend$registryID
+ _objc_msgSend$releaseIOSurfaceWithMappingID:surface:
+ _objc_msgSend$remoteCrashed
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeTraceRange
+ _objc_msgSend$removeTraceRange:
+ _objc_msgSend$renderCommandEncoderWithDescriptor:
+ _objc_msgSend$renderPassDescriptor
+ _objc_msgSend$renderTargetPixelFormat
+ _objc_msgSend$replaceBackingWithRanges:readOnly:
+ _objc_msgSend$replacePhysical:completionHandler:
+ _objc_msgSend$replacePhysical:reply:
+ _objc_msgSend$replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:
+ _objc_msgSend$reportStampWaitTimeout
+ _objc_msgSend$reserveResourceIndicesForResourceType:indices:indexCount:
+ _objc_msgSend$reserveSerialNum:
+ _objc_msgSend$reset
+ _objc_msgSend$resetPending
+ _objc_msgSend$resetRasterizationRateMap:completionHandler:
+ _objc_msgSend$resetRasterizationRateMap:reply:
+ _objc_msgSend$resetRasterizationRateMapWithSerializedData:serializedDataSize:rasterizationRateMap:
+ _objc_msgSend$resetUsingDescriptor:
+ _objc_msgSend$resourceIndex
+ _objc_msgSend$resourceOptions
+ _objc_msgSend$resume
+ _objc_msgSend$resumeChildFifo:
+ _objc_msgSend$resumeFifo
+ _objc_msgSend$retainIOSurfaceWithMappingID:
+ _objc_msgSend$retainSurfaceWithMappingID:
+ _objc_msgSend$ringDisplayDoorbellAtPort:
+ _objc_msgSend$rotation
+ _objc_msgSend$sampleCount
+ _objc_msgSend$scaleFactor
+ _objc_msgSend$scheduleFramePresents
+ _objc_msgSend$serialNum
+ _objc_msgSend$serializeSuspendState
+ _objc_msgSend$setAddressRanges:
+ _objc_msgSend$setAllowGPUOptimizedContents:
+ _objc_msgSend$setAlphaTestReferenceValue:
+ _objc_msgSend$setArrayLength:
+ _objc_msgSend$setBinaryVersion:
+ _objc_msgSend$setBlendColorRed:green:blue:alpha:
+ _objc_msgSend$setBorderColor:
+ _objc_msgSend$setBufferOffset:atIndex:
+ _objc_msgSend$setBufferOffset:attributeStride:atIndex:
+ _objc_msgSend$setBuffers:offsets:attributeStrides:withRange:
+ _objc_msgSend$setBuffers:offsets:withRange:
+ _objc_msgSend$setClass:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setClearColor:
+ _objc_msgSend$setClearDepth:
+ _objc_msgSend$setClearStencil:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setClipPlane:p2:p3:p4:atIndex:
+ _objc_msgSend$setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:
+ _objc_msgSend$setColorStoreAction:atIndex:
+ _objc_msgSend$setColorStoreActionOptions:atIndex:
+ _objc_msgSend$setCompareFunction:
+ _objc_msgSend$setComputePipelineState:
+ _objc_msgSend$setContents:
+ _objc_msgSend$setCullMode:
+ _objc_msgSend$setDeallocator:
+ _objc_msgSend$setDefaultColorSampleCount:
+ _objc_msgSend$setDefaultRasterSampleCount:
+ _objc_msgSend$setDepth:
+ _objc_msgSend$setDepthBias:slopeScale:clamp:
+ _objc_msgSend$setDepthCleared
+ _objc_msgSend$setDepthClipModeSPI:
+ _objc_msgSend$setDepthCompareFunction:
+ _objc_msgSend$setDepthFailureOperation:
+ _objc_msgSend$setDepthPlane:
+ _objc_msgSend$setDepthResolveFilter:
+ _objc_msgSend$setDepthResolveTexture:slice:depthPlane:level:yInvert:
+ _objc_msgSend$setDepthStencilPassOperation:
+ _objc_msgSend$setDepthStencilState:
+ _objc_msgSend$setDepthStoreAction:
+ _objc_msgSend$setDepthStoreActionOptions:
+ _objc_msgSend$setDepthWriteEnabled:
+ _objc_msgSend$setDescriptorBase:
+ _objc_msgSend$setDescriptorEnable:
+ _objc_msgSend$setDispatchType:
+ _objc_msgSend$setDisplay:
+ _objc_msgSend$setEFIDisplay:
+ _objc_msgSend$setEFIFramebufferDepth:
+ _objc_msgSend$setEFIFramebufferLength:
+ _objc_msgSend$setEFIFramebufferMode:
+ _objc_msgSend$setEFIFramebufferStart:
+ _objc_msgSend$setEFIFramebufferStride:
+ _objc_msgSend$setEFIModeSelect:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setFaultOffset:
+ _objc_msgSend$setFifoBasePage:
+ _objc_msgSend$setFifoEvent:forIndex:
+ _objc_msgSend$setFifoLength:
+ _objc_msgSend$setFifoStart:
+ _objc_msgSend$setFifoWritten:
+ _objc_msgSend$setForceResourceIndex:
+ _objc_msgSend$setFragmentBuffer:offset:atIndex:
+ _objc_msgSend$setFragmentBufferOffset:atIndex:
+ _objc_msgSend$setFragmentBuffers:offsets:withRange:
+ _objc_msgSend$setFragmentFunction:
+ _objc_msgSend$setFragmentSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:
+ _objc_msgSend$setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setFragmentSamplerStates:withRange:
+ _objc_msgSend$setFragmentTexture:atIndex:
+ _objc_msgSend$setFragmentTextures:withRange:
+ _objc_msgSend$setFramebufferDepth:
+ _objc_msgSend$setFramebufferLength:
+ _objc_msgSend$setFramebufferMode:
+ _objc_msgSend$setFramebufferOnly:
+ _objc_msgSend$setFramebufferStart:
+ _objc_msgSend$setFramebufferStride:
+ _objc_msgSend$setFrontFacingWinding:
+ _objc_msgSend$setGammaTableVirtualOffset:mappedLength:entryCount:sum:
+ _objc_msgSend$setGuestColorSpaceDirty:
+ _objc_msgSend$setGuestICCProfileLength:virtualOffset:
+ _objc_msgSend$setHasGamma:
+ _objc_msgSend$setHazardTrackingMode:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setImageblockSampleLength:
+ _objc_msgSend$setImageblockWidth:height:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsDrawable:
+ _objc_msgSend$setIsGuestValid:
+ _objc_msgSend$setIsHostValid:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLayer:atIndex:
+ _objc_msgSend$setLength:
+ _objc_msgSend$setLevel:
+ _objc_msgSend$setLineWidth:
+ _objc_msgSend$setLoadAction:
+ _objc_msgSend$setLodAverage:
+ _objc_msgSend$setLodMaxClamp:
+ _objc_msgSend$setLodMinClamp:
+ _objc_msgSend$setMagFilter:
+ _objc_msgSend$setMaxAnisotropy:
+ _objc_msgSend$setMinFactor:
+ _objc_msgSend$setMinFilter:
+ _objc_msgSend$setMipFilter:
+ _objc_msgSend$setMipmapLevelCount:
+ _objc_msgSend$setModeList:
+ _objc_msgSend$setModeSelect:
+ _objc_msgSend$setMutability:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNoCopy:
+ _objc_msgSend$setNormalizedCoordinates:
+ _objc_msgSend$setNub:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setObjectListOffset:objectListLength:placementListOffset:placementListLength:completionHandler:
+ _objc_msgSend$setObjectListOffset:objectListLength:placementListOffset:placementListLength:reply:
+ _objc_msgSend$setPinnedGPUAddress:
+ _objc_msgSend$setPixelFormat:
+ _objc_msgSend$setPointSize:
+ _objc_msgSend$setPrimitiveRestartEnabled:index:
+ _objc_msgSend$setProperty:value:wordCount:
+ _objc_msgSend$setProtectionOptions:
+ _objc_msgSend$setProvokingVertexMode:
+ _objc_msgSend$setPurgeableState:
+ _objc_msgSend$setRAddressMode:
+ _objc_msgSend$setRasterizationRateMap:
+ _objc_msgSend$setRead:
+ _objc_msgSend$setReadMask:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setRenderPipelineState:
+ _objc_msgSend$setRenderTargetArrayLength:
+ _objc_msgSend$setRenderTargetHeight:
+ _objc_msgSend$setRenderTargetPixelFormat:
+ _objc_msgSend$setRenderTargetWidth:
+ _objc_msgSend$setResolveDepthPlane:
+ _objc_msgSend$setResolveLevel:
+ _objc_msgSend$setResolveSlice:
+ _objc_msgSend$setResolveTexture:
+ _objc_msgSend$setResourceIndex:
+ _objc_msgSend$setResourceOptions:
+ _objc_msgSend$setRingBase:
+ _objc_msgSend$setRingSize:
+ _objc_msgSend$setRootPage:
+ _objc_msgSend$setRotation:
+ _objc_msgSend$setSAddressMode:
+ _objc_msgSend$setSampleCount:
+ _objc_msgSend$setSamplePositions:count:
+ _objc_msgSend$setSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setSamplerStates:withRange:
+ _objc_msgSend$setScissorRect:
+ _objc_msgSend$setScissorRects:count:
+ _objc_msgSend$setScreenSize:
+ _objc_msgSend$setSharedDisplayStatePage:forPort:restoring:
+ _objc_msgSend$setSize:
+ _objc_msgSend$setSlice:
+ _objc_msgSend$setStageInRegion:
+ _objc_msgSend$setStageInRegionWithIndirectBuffer:indirectBufferOffset:
+ _objc_msgSend$setStencilCleared
+ _objc_msgSend$setStencilCompareFunction:
+ _objc_msgSend$setStencilFailureOperation:
+ _objc_msgSend$setStencilFrontReferenceValue:backReferenceValue:
+ _objc_msgSend$setStencilResolveFilter:
+ _objc_msgSend$setStencilResolveTexture:slice:depthPlane:level:yInvert:
+ _objc_msgSend$setStencilStoreAction:
+ _objc_msgSend$setStencilStoreActionOptions:
+ _objc_msgSend$setStorageMode:
+ _objc_msgSend$setStoreAction:
+ _objc_msgSend$setStoreActionOptions:
+ _objc_msgSend$setSupportArgumentBuffers:
+ _objc_msgSend$setSwizzle:
+ _objc_msgSend$setTAddressMode:
+ _objc_msgSend$setTessellationFactorBuffer:offset:instanceStride:
+ _objc_msgSend$setTessellationFactorScale:
+ _objc_msgSend$setTexture:
+ _objc_msgSend$setTexture:atIndex:
+ _objc_msgSend$setTextureType:
+ _objc_msgSend$setTextures:withRange:
+ _objc_msgSend$setThreadgroupMemoryLength:
+ _objc_msgSend$setThreadgroupMemoryLength:atIndex:
+ _objc_msgSend$setThreadgroupMemoryLength:offset:atIndex:
+ _objc_msgSend$setTileBufferOffset:atIndex:
+ _objc_msgSend$setTileBuffers:offsets:withRange:
+ _objc_msgSend$setTileHeight:
+ _objc_msgSend$setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setTileSamplerStates:withRange:
+ _objc_msgSend$setTileTextures:withRange:
+ _objc_msgSend$setTileWidth:
+ _objc_msgSend$setTransformFeedbackState:
+ _objc_msgSend$setTriangleFillMode:
+ _objc_msgSend$setTriangleFrontFillMode:backFillMode:
+ _objc_msgSend$setType:
+ _objc_msgSend$setUsage:
+ _objc_msgSend$setVertexAmplificationCount:viewMappings:
+ _objc_msgSend$setVertexAmplificationMode:value:
+ _objc_msgSend$setVertexBuffer:offset:atIndex:
+ _objc_msgSend$setVertexBufferOffset:atIndex:
+ _objc_msgSend$setVertexBufferOffset:attributeStride:atIndex:
+ _objc_msgSend$setVertexBuffers:offsets:attributeStrides:withRange:
+ _objc_msgSend$setVertexBuffers:offsets:withRange:
+ _objc_msgSend$setVertexFunction:
+ _objc_msgSend$setVertexSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:
+ _objc_msgSend$setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:
+ _objc_msgSend$setVertexSamplerStates:withRange:
+ _objc_msgSend$setVertexTextures:withRange:
+ _objc_msgSend$setViewport:
+ _objc_msgSend$setViewportTransformEnabled:
+ _objc_msgSend$setViewports:count:
+ _objc_msgSend$setVisibilityResultBuffer:
+ _objc_msgSend$setVisibilityResultMode:offset:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$setWriteMask:
+ _objc_msgSend$setWriteSwizzleEnabled:
+ _objc_msgSend$setWritten:
+ _objc_msgSend$setupBlitPipelines
+ _objc_msgSend$setupFormatSpecific
+ _objc_msgSend$setupMapping
+ _objc_msgSend$setupReporting
+ _objc_msgSend$setupTaskRoot:
+ _objc_msgSend$sharedState
+ _objc_msgSend$signalCurrentFrame
+ _objc_msgSend$signalFIFOs
+ _objc_msgSend$signalFaultInFIFO:
+ _objc_msgSend$signalResponsiveness
+ _objc_msgSend$signalStamp:value:
+ _objc_msgSend$signalStampValue:
+ _objc_msgSend$sizeInMillimeters
+ _objc_msgSend$sizeInPixels
+ _objc_msgSend$sleepHandler
+ _objc_msgSend$sleepState:
+ _objc_msgSend$stampIndex
+ _objc_msgSend$start
+ _objc_msgSend$startOffset
+ _objc_msgSend$stateMachineWithCaller:
+ _objc_msgSend$staticThreadgroupMemoryLength
+ _objc_msgSend$status
+ _objc_msgSend$stencilAttachment
+ _objc_msgSend$stop
+ _objc_msgSend$stopPresentation
+ _objc_msgSend$storageMode
+ _objc_msgSend$storeAction
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$supportIndirectCommandBuffers
+ _objc_msgSend$supports10bpc
+ _objc_msgSend$supportsArgumentBuffers
+ _objc_msgSend$supportsBufferWithAddressRanges
+ _objc_msgSend$supportsBufferWithIOSurface
+ _objc_msgSend$supportsCommandBufferJump
+ _objc_msgSend$supportsComputeCompressedTextureWrite
+ _objc_msgSend$supportsDiscard
+ _objc_msgSend$supportsDynamicAttributeStride
+ _objc_msgSend$supportsEDR
+ _objc_msgSend$supportsExtendedXR10Formats
+ _objc_msgSend$supportsFamily:
+ _objc_msgSend$supportsFloat16BCubicFiltering
+ _objc_msgSend$supportsHeapWithAddressRanges
+ _objc_msgSend$supportsImageBlocks
+ _objc_msgSend$supportsLargeKernelTasks
+ _objc_msgSend$supportsLargeUserTasks
+ _objc_msgSend$supportsMemoryOrderAtomics
+ _objc_msgSend$supportsNativeHardwareFP16
+ _objc_msgSend$supportsNonSquareTileShaders
+ _objc_msgSend$supportsPrimitiveType:
+ _objc_msgSend$supportsProgrammableSamplePositions
+ _objc_msgSend$supportsRangeBuffer
+ _objc_msgSend$supportsResourceDetachBacking
+ _objc_msgSend$supportsSIMDReduction
+ _objc_msgSend$supportsSIMDShuffleAndFill
+ _objc_msgSend$supportsSharedMemoryHeap
+ _objc_msgSend$supportsSharedTextureHandles
+ _objc_msgSend$supportsSharedTextures
+ _objc_msgSend$supportsTexture2DMultisampleArray
+ _objc_msgSend$supportsTextureSampleCount:
+ _objc_msgSend$supportsTextureWriteRoundingMode:
+ _objc_msgSend$supportsTileShaders
+ _objc_msgSend$synchronizeInComputeEncoder:
+ _objc_msgSend$synchronizeInEncoder:
+ _objc_msgSend$synchronizeResource:
+ _objc_msgSend$synchronizeResources:count:discard:completionHandler:
+ _objc_msgSend$synchronizeResources:count:discard:reply:
+ _objc_msgSend$synchronizeTexture:slice:level:
+ _objc_msgSend$teardown
+ _objc_msgSend$teardownDisplays
+ _objc_msgSend$teardownFifos
+ _objc_msgSend$teardownMapping
+ _objc_msgSend$teardownRoot
+ _objc_msgSend$teardownSurfaces
+ _objc_msgSend$teardownTasks
+ _objc_msgSend$testSurface:
+ _objc_msgSend$testUpdateModeList:
+ _objc_msgSend$testUpdateSettings:
+ _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
+ _objc_msgSend$textureDescriptorForDescriptor:
+ _objc_msgSend$textureType
+ _objc_msgSend$textures
+ _objc_msgSend$threadExecutionWidth
+ _objc_msgSend$threadgroupSizeMatchesTileSize
+ _objc_msgSend$tileHeight
+ _objc_msgSend$tileWidth
+ _objc_msgSend$type
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$unmap:
+ _objc_msgSend$unmapMemory
+ _objc_msgSend$unmapMemoryAtOffset:length:completionHandler:
+ _objc_msgSend$unmapMemoryAtOffset:length:reply:
+ _objc_msgSend$unmapMemoryAtVirtualOffset:length:
+ _objc_msgSend$unmapMemoryInTask:offset:length:
+ _objc_msgSend$unmapSurface:
+ _objc_msgSend$unpause
+ _objc_msgSend$unplug
+ _objc_msgSend$unreserveSerialNum:
+ _objc_msgSend$updateColorMatrix:
+ _objc_msgSend$updateFence:
+ _objc_msgSend$updateFence:afterStages:
+ _objc_msgSend$updateFramebufferMapping
+ _objc_msgSend$updateFramebufferMode
+ _objc_msgSend$updateGammaSlopesRedSlopeAtZero:greenSlopeAtZero:blueSlopeAtZero:redSlopeAtOne:greenSlopeAtOne:blueSlopeAtOne:
+ _objc_msgSend$updateGammaTable:virtualOffset:mappedLength:entryCount:sum:
+ _objc_msgSend$updateGuestColorSpace
+ _objc_msgSend$updateResponsiveness
+ _objc_msgSend$usage
+ _objc_msgSend$useHeaps:count:
+ _objc_msgSend$useHeaps:count:stages:
+ _objc_msgSend$useResources:count:usage:
+ _objc_msgSend$useResources:count:usage:stages:
+ _objc_msgSend$usingIOSurfaceMapper
+ _objc_msgSend$validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:
+ _objc_msgSend$validateTextureDimension:dest:mipLevels:generateMipmaps:textureAllocationLength:texture:planeCount:isPVRTC:features:
+ _objc_msgSend$verticalSampleStorage
+ _objc_msgSend$virtualAddress
+ _objc_msgSend$virtualAddressForPhysical:length:
+ _objc_msgSend$visitPagesInRange:length:visitor:
+ _objc_msgSend$waitForFence:
+ _objc_msgSend$waitForFence:beforeStages:
+ _objc_msgSend$waitForPendingFrames:
+ _objc_msgSend$waitStamp:waitingFIFO:
+ _objc_msgSend$waitStamps:barriers:waitingFIFO:
+ _objc_msgSend$waitUntilCompleted
+ _objc_msgSend$waitUntilScheduled
+ _objc_msgSend$wakeDevice
+ _objc_msgSend$wakeFifo:
+ _objc_msgSend$width
+ _objc_msgSend$willRestore
+ _objc_msgSend$writable
+ _objc_msgSend$writableCursorFromVirtualOffset:length:
+ _objc_msgSend$written
+ _readRange
+ _strlen
+ _upgradeDescriptor
+ checkCapabilities.cold.1
+ checkCapabilities.cold.10
+ checkCapabilities.cold.11
+ checkCapabilities.cold.12
+ checkCapabilities.cold.13
+ checkCapabilities.cold.14
+ checkCapabilities.cold.15
+ checkCapabilities.cold.16
+ checkCapabilities.cold.17
+ checkCapabilities.cold.18
+ checkCapabilities.cold.19
+ checkCapabilities.cold.2
+ checkCapabilities.cold.20
+ checkCapabilities.cold.21
+ checkCapabilities.cold.22
+ checkCapabilities.cold.23
+ checkCapabilities.cold.24
+ checkCapabilities.cold.25
+ checkCapabilities.cold.26
+ checkCapabilities.cold.27
+ checkCapabilities.cold.28
+ checkCapabilities.cold.29
+ checkCapabilities.cold.3
+ checkCapabilities.cold.30
+ checkCapabilities.cold.31
+ checkCapabilities.cold.32
+ checkCapabilities.cold.33
+ checkCapabilities.cold.34
+ checkCapabilities.cold.35
+ checkCapabilities.cold.36
+ checkCapabilities.cold.37
+ checkCapabilities.cold.38
+ checkCapabilities.cold.39
+ checkCapabilities.cold.4
+ checkCapabilities.cold.40
+ checkCapabilities.cold.41
+ checkCapabilities.cold.42
+ checkCapabilities.cold.43
+ checkCapabilities.cold.44
+ checkCapabilities.cold.45
+ checkCapabilities.cold.46
+ checkCapabilities.cold.47
+ checkCapabilities.cold.48
+ checkCapabilities.cold.49
+ checkCapabilities.cold.5
+ checkCapabilities.cold.50
+ checkCapabilities.cold.51
+ checkCapabilities.cold.52
+ checkCapabilities.cold.53
+ checkCapabilities.cold.54
+ checkCapabilities.cold.55
+ checkCapabilities.cold.56
+ checkCapabilities.cold.57
+ checkCapabilities.cold.58
+ checkCapabilities.cold.59
+ checkCapabilities.cold.6
+ checkCapabilities.cold.60
+ checkCapabilities.cold.61
+ checkCapabilities.cold.62
+ checkCapabilities.cold.63
+ checkCapabilities.cold.64
+ checkCapabilities.cold.65
+ checkCapabilities.cold.66
+ checkCapabilities.cold.67
+ checkCapabilities.cold.68
+ checkCapabilities.cold.69
+ checkCapabilities.cold.7
+ checkCapabilities.cold.70
+ checkCapabilities.cold.71
+ checkCapabilities.cold.72
+ checkCapabilities.cold.73
+ checkCapabilities.cold.74
+ checkCapabilities.cold.75
+ checkCapabilities.cold.76
+ checkCapabilities.cold.77
+ checkCapabilities.cold.78
+ checkCapabilities.cold.79
+ checkCapabilities.cold.8
+ checkCapabilities.cold.80
+ checkCapabilities.cold.81
+ checkCapabilities.cold.82
+ checkCapabilities.cold.83
+ checkCapabilities.cold.84
+ checkCapabilities.cold.85
+ checkCapabilities.cold.86
+ checkCapabilities.cold.87
+ checkCapabilities.cold.88
+ checkCapabilities.cold.89
+ checkCapabilities.cold.9
+ initWithDescriptor:.onceToken
+ parseIOSurfaceHostDeviceSaveState.cold.1
+ parseIOSurfaceHostDeviceSaveState.cold.2
+ parseIOSurfaceHostDeviceSaveState.cold.3
+ parseIOSurfaceHostDeviceSaveState.cold.4
+ readRange.cold.1
+ readRange.cold.2
+ readRange.cold.3
- OBJC_IVAR_$_PGBaseTask._computePipelines
- OBJC_IVAR_$_PGBaseTask._depthStencils
- OBJC_IVAR_$_PGBaseTask._fences
- OBJC_IVAR_$_PGBaseTask._functions
- OBJC_IVAR_$_PGBaseTask._objectListMutex
- OBJC_IVAR_$_PGBaseTask._rasterizationRateMaps
- OBJC_IVAR_$_PGBaseTask._renderPipelines
- OBJC_IVAR_$_PGBaseTask._reservedSerializerTextures
- OBJC_IVAR_$_PGBaseTask._resources
- OBJC_IVAR_$_PGBaseTask._samplers
- _OBJC_CLASS_$_PGRangeBufferResource
- _OBJC_CLASS_$_PGRangeHeapResource
- _OBJC_METACLASS_$_PGRangeBufferResource
- _OBJC_METACLASS_$_PGRangeHeapResource
- __ZN14PGByteIteratorC1EPvy
- __ZN14PGByteIteratorC2EPvy
- __os_log_default
CStrings:
+ " does not allow the "
+ " formatting argument"
+ " option"
+ "!_usingMemoryMap"
+ "-[PGDeserializerInfoDecoder decodeHeapTextureDescriptorSizeAndAlignWithIterator:]"
+ "-[PGLocalTask cursorFromVirtualOffsetInternal:length:needWritable:]_block_invoke"
+ "-[PGLocalTask mapMemoryInternalAtOffset:length:]"
+ "0"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "@\"<MTLCommandQueue>\"16@0:8"
+ "@\"MTLTextureDescriptor\"24@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16"
+ "@\"PGMapping\"36@0:8Q16Q24B32"
+ "@24@0:8^v16"
+ "@24@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16"
+ "@32@0:8@16^v24"
+ "@36@0:8Q16Q24B32"
+ "@44@0:8@16^{?=QIIC}24^{?=IIIb24b8}32I40"
+ "@48@0:8@16I24^v28I36^v40"
+ "@48@0:8@16^v24I32B36^v40"
+ "@56@0:8@16r^{?=IQ}24r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}32Q40@48"
+ "@60@0:8@16I24r^{?=IQ}28r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}36Q44@52"
+ "An argument index may not have a negative value"
+ "Apple Paravirtual device"
+ "Argument buffer support %sabled"
+ "Attempting to create mapper ref against invalid surface ({})"
+ "Attempting to create shared texture backing from a non shared texture resource"
+ "Attempting to fetch invalid object: {}"
+ "Attempting to use unsupported dual-plane textures"
+ "B52@0:8^{?=QIIC}16r^{?=IIIb24b8}24^{?=IIIb24b8}32I40Q44"
+ "Cannot get backing from a non-zero task ID"
+ "EnableArgumentBuffers"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Error while setting object and placement list"
+ "Failed copy cursor"
+ "Failed malloc"
+ "Failed to alloc descriptor"
+ "Failed to alloc dimension"
+ "Failed to correctly place texture"
+ "Failed to create Buffer"
+ "Failed to create Function"
+ "Failed to create Heap"
+ "Failed to create Texture"
+ "Failed to create buffer host resource"
+ "Failed to create child resource"
+ "Failed to create compute pipeline: %@"
+ "Failed to create compute pipeline: {}"
+ "Failed to create cursor"
+ "Failed to create depth stencil state"
+ "Failed to create descriptor"
+ "Failed to create descriptor: {}"
+ "Failed to create dispatch data"
+ "Failed to create fence"
+ "Failed to create heap buffer"
+ "Failed to create heap buffer host resource"
+ "Failed to create heap host resource"
+ "Failed to create host resource"
+ "Failed to create host resource for shared texture backing"
+ "Failed to create library: {}"
+ "Failed to create mapper ref buffer host resource"
+ "Failed to create memory cursor"
+ "Failed to create rasterization rate map"
+ "Failed to create render pipeline: %@"
+ "Failed to create render pipeline: {}"
+ "Failed to create resource"
+ "Failed to create sampler state"
+ "Failed to create sampler state with correct resourceID"
+ "Failed to create shared texture"
+ "Failed to create texture"
+ "Failed to find backing"
+ "Failed to find backing: %s"
+ "Failed to get %s (%s)"
+ "Failed to get backing for ioSurfaceID ({})"
+ "Failed to get base buffer: {}"
+ "Failed to get base heap {}"
+ "Failed to get base heap: {}"
+ "Failed to get base texture: {}"
+ "Failed to get cursor for buffer"
+ "Failed to get function data"
+ "Failed to get function with ref %u: %s"
+ "Failed to get pipeline: %s"
+ "Failed to get placement: {}"
+ "Failed to get resource: %s"
+ "Failed to get shared texture handle for handle ({})"
+ "Failed to iterate: %@"
+ "Failed to make mapping"
+ "Failed to map object list"
+ "Failed to map object list: %@"
+ "Failed to map placement list"
+ "Failed to read buffer descriptor: {}"
+ "Failed to read command: {}"
+ "Failed to read descriptor: {}"
+ "Failed to read dimension: {}"
+ "Failed to read function header: {}"
+ "Failed to read guest coordinate"
+ "Failed to read heap buffer descriptor: {}"
+ "Failed to read heap descriptor: {}"
+ "Failed to read height samples at index ({}): {}"
+ "Failed to read layer at index ({}): {}"
+ "Failed to read mapper ref buffer descriptor: {}"
+ "Failed to read mapper ref texture descriptor: {}"
+ "Failed to read normal texture descriptor: {}"
+ "Failed to read planes: {}"
+ "Failed to read rest of dimension: {}"
+ "Failed to read serializer header: {}"
+ "Failed to read shared texture backing header: {}"
+ "Failed to read shared texture descriptor: {}"
+ "Failed to read texture dimension: {}"
+ "Failed to read width samples at index ({}): {}"
+ "Failed to register object"
+ "Failed to reserve objects: %s"
+ "Failed to validate IOSurface descriptor"
+ "Failed to write to cursor: %s"
+ "Failed: %s"
+ "Host's SupportedTextureWriteRoundingModes does not cover the requested value, host's capability: %u, requested: %u"
+ "Insufficient data in command"
+ "Integral value outside the range of the char type"
+ "Invalid command for deletion"
+ "Invalid command size"
+ "Invalid object type ({}) for compute pipeline state"
+ "Invalid object type ({}) for depthstencil state"
+ "Invalid object type ({}) for fence"
+ "Invalid object type ({}) for function"
+ "Invalid object type ({}) for rasterization rate map"
+ "Invalid object type ({}) for render pipeline state"
+ "Invalid object type ({}) for sampler state"
+ "Invalid object type {} for buffer cursor"
+ "Invalid placement of non-placeable render pipeline state"
+ "Invalid serializer command type ({})"
+ "Invalid storage mode"
+ "Invalid storage mode ({})"
+ "Mapping was not writable"
+ "Must have a memory map"
+ "Object list not mapped"
+ "ObjectRef ref({}) out of range({})"
+ "Out of range cursor request"
+ "PGDiscardableHeapBufferResource"
+ "PGDiscardableSerializerTextureResource"
+ "PGResourceManager.mm"
+ "PGResourceManagerDelegate"
+ "PGResourceManagerDeserializationContext"
+ "PGResourceManager_RasterizationRate.mm"
+ "PGResourceManager_Texture.mm"
+ "PGResource_Buffer.mm"
+ "PGResource_Heap.mm"
+ "PGResource_Texture.mm"
+ "PGTask_ObjectListManager"
+ "PGTask_ResourceManager"
+ "Placement list not mapped"
+ "Read from offset ({}) length ({}) > cursorLength ({})"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "SupportedTextureWriteRoundingModes"
+ "T@\"<MTLCommandQueue>\",R"
+ "TB,R,V_supportsLargeKernelTasks"
+ "TQ,R,V_objectListCount"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "Too many planes ({}) in backing resource"
+ "UTF8String"
+ "Unable to do placement list copy"
+ "Unexpected function count in library ({})"
+ "Unexpected object type ({}) for resource"
+ "Unexpected serializer command type ({}) for backing ref texture"
+ "Unexpected serializer command type ({}) for mapper backed texture"
+ "Unexpected serializer command type ({}) for normal texture"
+ "Unexpected serializer command type ({}) for serializer texture"
+ "Unexpected serializer command type ({}) for shared ref texture"
+ "Unexpected serializer command type ({}) for shared texture backing resource"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "Write offset ({}) length ({}) > cursorLength ({})"
+ "Zero length cursor request"
+ "[64{?=\"nextWaitingIndex\"I\"nextWaitingValue\"I\"lastPendingStamp\"{atomic<unsigned int>=\"__a_\"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>=\"__a_value\"AI}}}]"
+ "\\\""
+ "\\'"
+ "\\\\"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u{"
+ "\\x{"
+ "^v36@0:8Q16Q24B32"
+ "_enableArgumentBuffers"
+ "_objectListManager"
+ "_resourceManager"
+ "_supportsLargeKernelTasks"
+ "_tearingDownRoot"
+ "_usingMemoryMap"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "basic_string"
+ "command->rotation == (__typeof__(command->rotation))(*descriptor).rotation"
+ "computePipeline"
+ "containsString:"
+ "createSharedTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
+ "createTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
+ "cursorFromVirtualOffset:length:"
+ "cursorFromVirtualOffsetInternal:length:needWritable:"
+ "decodeHeapTextureDescriptorSizeAndAlignWithIterator:"
+ "depthStencil"
+ "dis"
+ "en"
+ "enableArgumentBuffers"
+ "fence"
+ "from must be non-null"
+ "function"
+ "heapTextureSizeAndAlign"
+ "host's SupportedTextureWriteRoundingModes capability not defined"
+ "infnanINFNAN"
+ "initWithBuffer:"
+ "initWithResourceManager:"
+ "initWithTask:descriptor:planes:planeCount:"
+ "initWithTexture:"
+ "into must be non-null"
+ "legacyMappedAddressForOffset:length:"
+ "lengthRemaining != 0"
+ "lengthRemaining >= lengthInPage"
+ "locale-specific form"
+ "mappedAddressForOffset:length:needWritable:"
+ "memoryMapMappedAddressForOffset:length:needWritable:"
+ "newChildBufferResourceWithBuffer:"
+ "newChildTextureResourceWithTexture:"
+ "newIOSurfaceTextureWithRotation"
+ "newLegacyBufferForVirtualPage:length:"
+ "newMemoryCursorForBuffer:"
+ "newMemoryMapBufferForVirtualPage:length:"
+ "newRasterizationRateMapDescriptor"
+ "newSharedTextureWithHandle:withResourceIndex:"
+ "newVirtualMapping:length:needWritable:"
+ "object"
+ "pagingQueue"
+ "precision"
+ "rasterizationRateMap"
+ "rateMapDescriptor.layerCount == desc->layerCount"
+ "rebuildTask"
+ "registerObject"
+ "renderPipeline"
+ "sampler"
+ "setEnableArgumentBuffers:"
+ "sign"
+ "supportsLargeKernelTasks"
+ "supportsLargeUserTasks"
+ "supportsTextureWriteRoundingMode:"
+ "textureDescriptorForDescriptor:"
+ "true"
+ "unique_lock::try_lock: already locked"
+ "unique_lock::try_lock: references null mutex"
+ "v116@0:8I16Q20I28{?=QB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@\"PGMemoryMap\"100@?<v@?Ii>108"
+ "v116@0:8I16Q20I28{?=QB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@100@?108"
+ "validateBackingDescriptor:srcPlanes:destPlanes:planeCount:backingAllocationLength:"
+ "writableCursorFromVirtualOffset:length:"
+ "zero-padding"
+ "{atomic<unsigned int>=\"__a_\"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>=\"__a_value\"AI}}"
+ "{shared_ptr<PGObjectListManager>=\"__ptr_\"^{PGObjectListManager}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<PGVirtualMemoryCursor>=^{PGVirtualMemoryCursor}^{__shared_weak_count}}32@0:8Q16Q24"
+ "{shared_ptr<PGVirtualMemoryCursor>=^{PGVirtualMemoryCursor}^{__shared_weak_count}}36@0:8Q16Q24B32"
+ "{shared_ptr<PGWritableVirtualMemoryCursor>=^{PGWritableVirtualMemoryCursor}^{__shared_weak_count}}20@0:8I16"
+ "{shared_ptr<PGWritableVirtualMemoryCursor>=^{PGWritableVirtualMemoryCursor}^{__shared_weak_count}}32@0:8Q16Q24"
+ "{unique_ptr<PGResourceManager, std::default_delete<PGResourceManager>>=\"__ptr_\"{__compressed_pair<PGResourceManager *, std::default_delete<PGResourceManager>>=\"__value_\"^{PGResourceManager}}}"
- "-[PGBaseTask newBackingRefTextureWithEntry:forReference:]"
- "-[PGBaseTask newNormalTextureWithEntry:forReference:]"
- "-[PGBaseTask newSerializerTextureWithEntry:forReference:]"
- "-[PGBaseTask newSharedTextureWithEntry:forReference:]"
- "-[PGBaseTask reserveObjects]"
- "-[PGBaseTask reservePlacedOtherSerializerReference:]"
- "-[PGDeserializerInfoDecoder decodeHeapTexturDescriptorSizeAndAlignWithIterator:]"
- "-[PGLocalTask getComputeInfo:maxKey:count:offset:completionHandler:]"
- "-[PGLocalTask invalidateGuestForSharedTextureBacking:sharedTextureBackingCount:]"
- "-[PGLocalTask newSharedTextureBackingForReference:]"
- "-[_PGDeserializer heapTextureSizeAndAlignWithSerializedData:serializedDataSize:]"
- "-[_PGDeserializer newTextureForSerializedData:serializedDataSize:ioSurface:resourceIndex:resourceID:]"
- "-[_PGDeserializer newTextureWithHeap:resourceIndex:resourceID:]"
- "-[_PGDeserializer reserveObjectWithSerializedData:serializedDataSize:placement:]"
- "@\"<MTLComputePipelineState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLDepthStencilState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLFence>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLFunction>\"40@0:8r*16Q24@\"NSObject<OS_dispatch_data>\"32"
- "@\"<MTLRasterizationRateMap>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLRenderPipelineState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLSamplerState>\"40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@\"<MTLTexture>\"40@0:8r*16Q24@\"MTLSharedTextureHandle\"32"
- "@\"<MTLTexture>\"48@0:8r*16Q24Q32Q40"
- "@\"<MTLTexture>\"56@0:8r*16Q24^{__IOSurface=}32Q40Q48"
- "@24@0:8r^{?=I{?=b3b1b1b1b26{?=b3b3b3b3b20II}{?=b3b3b3b3b20II}}}16"
- "@24@0:8r^{?=I}16"
- "@28@0:8^{?=b8b24Q}16I24"
- "@32@0:8@16^AI24"
- "@32@0:8^{?=II}16Q24"
- "@32@0:8^{?=I{?={?=SS}IIf[0{?={?=SS}}]}}16Q24"
- "@32@0:8r^{?=II}16Q24"
- "@32@0:8r^{?=I{?=b2b2b1b3b4b4b4b4b2b5b1b1b3b28ffQ}}16^(PGDeserializerPlacement=Q{?=QQ})24"
- "@32@0:8r^{?=b4b1b1b1b1b16IIIISSSSQCCCC}16Q24"
- "@32@0:8r^{?=b4b1b1b1b1b8b16IIISSSSQ}16Q24"
- "@36@0:8@16r^v24I32"
- "@40@0:8@16r^{?=IQQ}24^(?=Q{?=QQ})32"
- "@40@0:8^{?=IIQQ{?=b4b1b1b1b1b8b16IIISSSSQ}}16Q24Q32"
- "@40@0:8^{?=IISS{?=QQ}{?=QQ}CCCC}16Q24Q32"
- "@40@0:8^{?=IISS{?=QQ}{?=QQ}}16Q24Q32"
- "@40@0:8^{?=IIS}16Q24Q32"
- "@40@0:8^{?=II{?=b4b1b1b1b1b8b16IIISSSSQ}b1b31Q}16Q24Q32"
- "@40@0:8^{?=I{?=b4b1b1b1b1b16IIIISSSSQCCCC}}16Q24Q32"
- "@40@0:8^{?=I{?=b4b1b1b1b1b8b16IIISSSSQ}}16Q24Q32"
- "@40@0:8r*16Q24@32"
- "@40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "@48@0:8@16I24^v28I36^AI40"
- "@48@0:8@16^{?=AIAIISSI}24I32B36^AI40"
- "@48@0:8r*16Q24Q32Q40"
- "@52@0:8@16r^{?=IQ}24r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}32I40@44"
- "@56@0:8@16I24r^{?=IQ}28r^{?=b14b1b1SQQCCCC[0{?=QQQIII}]}36I44@48"
- "@56@0:8r*16Q24^{__IOSurface=}32Q40Q48"
- "AI"
- "AQ"
- "Attempting to create reference texture from mapper with invalid device"
- "Attempting to use unsupported multi-plane texture"
- "B44@0:8^{?=QIIC}16^{?=IIIb24b8}24I32Q36"
- "Disallowed to set both memoryMapDescriptor and any of mapMemory, unmapMemory"
- "Dual plane compute shared texture backing unsupported"
- "Enabling resource detachment"
- "Expected shared texture backing object instead of object type(%d) for resource ref(%d)"
- "Failed allocate copy"
- "Failed at Metal level"
- "Failed to create backing ref texture"
- "Failed to create backing texture"
- "Failed to create function"
- "Failed to create heap"
- "Failed to create host resource for mapperRef texture"
- "Failed to create host resource for ref texture"
- "Failed to create host resource for shared texture"
- "Failed to create mapper ref texture"
- "Failed to create normal texture"
- "Failed to create serializer texture"
- "Failed to create shared texture backing resource"
- "Failed to create shared texture with handle"
- "Failed to get shared texture handle"
- "Failed to shared texture with descriptor"
- "ForceAddressRangeResources"
- "Forcing address range resources"
- "Got invalid compute pipeline for ref(%d)"
- "Got invalid heap for ref(%d)"
- "Got invalid rate map for ref (%d)"
- "Got invalid render pipeline for ref(%d)"
- "Got invalid sampler state for ref(%d)"
- "Got invalid texture for ref(%d)"
- "Heap buffer size out of range"
- "Heap support not enabled"
- "IOSurface validation failed"
- "Invalid ComputePipelineState reference, %d"
- "Invalid ComputePipelineState reference, %d, object already exists"
- "Invalid DepthStencilState reference, %d"
- "Invalid DepthStencilState reference, %d, object already exists"
- "Invalid Fence reference, %d"
- "Invalid Fence reference, %d, object already exists"
- "Invalid RasterizationRateMap reference, %d"
- "Invalid RasterizationRateMap reference, %d, object already exists"
- "Invalid RenderPipelineState reference, %d"
- "Invalid RenderPipelineState reference, %d, object already exists"
- "Invalid SamplerState reference, %d"
- "Invalid SamplerState reference, %d, object already exists"
- "Invalid argument, entry isn't a buffer (%u)"
- "Invalid command"
- "Invalid function reference, %d"
- "Invalid function reference, %d, object already exists"
- "Invalid mip level count"
- "Invalid object ID"
- "Invalid reply size"
- "Invalid swizzle"
- "InvalidReference"
- "Non-kernel IOSurface backing task"
- "Not a backing resource"
- "Not a shared texture backing resource"
- "PGBaseTask.mm"
- "PGBufferResource.m"
- "PGHeapResource.m"
- "PGRangeBufferResource"
- "PGRangeHeapResource"
- "PGResource.m"
- "Placing compute pipeline states is not supported"
- "Placing depth stencil states is not supported"
- "Placing fences is not supported"
- "Placing rasterization rate maps is not supported"
- "Placing render pipeline states is not supported"
- "Placing texture"
- "Placing view"
- "Resource %d already exists"
- "SupportsLargeUserTasks"
- "T@?,C,V_mapMemory"
- "T@?,C,V_unmapMemory"
- "TB,R,V_forceAddressRangeResources"
- "TB,R,V_supportsResourceDetachment"
- "TQ,R,D"
- "Trying to delete non-buffer resource from buffer path"
- "Trying to delete non-heap resource from heap path"
- "Trying to delete non-texture resource from texture path"
- "Unexpected function count: %u"
- "Unexpected object type (%d) for heap ref(%d)"
- "Unexpected object type (%d) for resource ref(%d)"
- "Unexpected object type (%d) for serializer ref(%d)"
- "Unexpected object type (%d) for texture ref(%d)"
- "Unexpected object type for shared texture backing"
- "[64{?=\"nextWaitingIndex\"I\"nextWaitingValue\"I\"lastPendingStamp\"AI}]"
- "[it->second.get() respondsToSelector:@selector(newSharedTextureHandle)]"
- "^(?=Q{?=QQ})20@0:8I16"
- "^{?=AIAIISSI}"
- "^{?=I[14c]SSSSSIIff{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{?=(?={?=SS}AI)}CC[6C]QiIQfff[33I]AIAI[62I]I{?=S[128{?=SSI(?=Q{?=b1b1})}]}{APVColorMatrixState=[2[3[4f]]]CCCC}[227I]{?=(?={?=SS}AI)}B[62I]QQQIIBSSSSI[10Q]QQIIQIIBBQBIIQI}"
- "^{?=I[14c]SSSSSIIff{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{AppleParavirtGPUDisplayColorPoint_t=ff}{?=(?={?=SS}AI)}CC[6C]QiIQfff[33I]AIAI[62I]I{?=S[128{?=SSI(?=Q{?=b1b1})}]}{APVColorMatrixState=[2[3[4f]]]CCCC}[227I]{?=(?={?=SS}AI)}B[62I]QQQIIBSSSSI[10Q]QQIIQIIBBQBIIQI}16@0:8"
- "^{?=[256I][64{?=AIAIISSI}][8I]}"
- "^{?=b8b24Q}"
- "_computePipelines"
- "_depthStencils"
- "_enableResourceDetachment"
- "_fences"
- "_forceAddressRangeResources"
- "_functions"
- "_maxObjectCount"
- "_objectList"
- "_objectListLength"
- "_objectListMapped"
- "_objectListMutex"
- "_objectListOffset"
- "_rasterizationRateMaps"
- "_renderPipelines"
- "_reservedSerializerTextures"
- "_resources"
- "_samplers"
- "_supportsResourceDetachment"
- "clearPlacementEntry:"
- "command->rotation == (__typeof__(command->rotation))descriptor.rotation"
- "decodeHeapTexturDescriptorSizeAndAlignWithIterator:"
- "deleteResourceForReference:"
- "deleteResourceLocked:clearPlacementListEntry:"
- "forceAddressRangeResources"
- "getPlacementEntry:"
- "heapTextureSizeAndAlignWithSerializedData:serializedDataSize:"
- "initWithTask:descriptor:descriptorLength:"
- "initWithTask:texture:"
- "listEntry->objectType == APVObjRefTexture"
- "listEntry->objectType == APVObjSerializerResource || listEntry->objectType == APVObjMemorylessTexture"
- "listEntry->objectType == APVObjSharedTexture"
- "listEntry->objectType == APVObjTexture || listEntry->objectType == APVObjClientStorageTexture || listEntry->objectType == APVObjDualPlaneTexture"
- "mapObjectList"
- "mappedAddressForOffset:length:"
- "newBackingForReference:"
- "newBackingRefTextureWithEntry:forReference:"
- "newBufferForReference:"
- "newComputePipelineStateForReference:"
- "newComputePipelineStateWithDescriptor:serializedDataSize:"
- "newComputePipelineStateWithSerializedData:serializedDataSize:placement:"
- "newDepthStencilStateForReference:"
- "newDepthStencilStateWithSerializedData:serializedDataSize:placement:"
- "newFence:"
- "newFenceForReference:"
- "newFenceWithSerializedData:serializedDataSize:placement:"
- "newFunctionForReference:"
- "newFunctionWithSerializedData:serializedDataSize:metalLibData:"
- "newHeapBufferWithTask:descriptor:descriptorLength:placement:"
- "newHeapForReference:"
- "newMapperRefTextureWithEntry:forReference:"
- "newNormalTextureWithEntry:forReference:"
- "newRasterizationRateMapForReference:"
- "newRasterizationRateMapWithDescriptor:serializedDataSize:"
- "newRasterizationRateMapWithSerializedData:serializedDataSize:placement:"
- "newRenderPipelineStateForReference:"
- "newRenderPipelineStateWithDescriptor:serializedDataSize:"
- "newRenderPipelineStateWithSerializedData:serializedDataSize:placement:"
- "newRenderPipelineStateWithTileDescriptor:serializedDataSize:"
- "newResourceForReference:"
- "newSamplerStateForReference:"
- "newSamplerStateWithDescriptor:placement:"
- "newSamplerStateWithSerializedData:serializedDataSize:placement:"
- "newSerializerTextureWithEntry:forReference:"
- "newSharedTextureBackingForReference:"
- "newSharedTextureForSerializedData:serializedDataSize:sharedTextureHandle:"
- "newSharedTextureWithDescriptor2:resourceIndex:resourceID:"
- "newSharedTextureWithDescriptor:resourceIndex:resourceID:"
- "newSharedTextureWithEntry:forReference:"
- "newSharedTextureWithHandle:"
- "newTextureDescriptor2:resourceIndex:"
- "newTextureDescriptor:resourceIndex:"
- "newTextureForReference:"
- "newTextureForSerializedData:serializedDataSize:ioSurface:resourceIndex:resourceID:"
- "newTextureResourceWithTask:objectType:pagingInfo:dimension:dimensionLength:texture:"
- "newTextureViewWithBuffer:resourceIndex:resourceID:"
- "newTextureViewWithPixelFormat:resourceIndex:resourceID:"
- "newTextureViewWithSwizzle:resourceIndex:resourceID:"
- "newTextureViewWithTextureType:resourceIndex:resourceID:"
- "newTextureWithDescriptor2:resourceIndex:resourceID:"
- "newTextureWithDescriptor:resourceIndex:resourceID:"
- "newTextureWithHeap:resourceIndex:resourceID:"
- "newTextureWithSerializedData:serializedDataSize:resourceIndex:resourceID:"
- "pipeline"
- "placement"
- "rasterizationRateMapInfoReplySizeForLayerCount:"
- "registerComputePipelineStateForReference:computePipeline:"
- "registerDepthStencilStateForReference:depthStencil:"
- "registerFenceForReference:fence:"
- "registerFunctionForReference:function:"
- "registerHostResource:forReference:"
- "registerRasterizationRateMapForReference:rasterizationRateMap:"
- "registerRenderPipelineStateForReference:renderPipeline:"
- "registerSamplerStateForReference:sampler:"
- "reserveObjectWithSerializedData:serializedDataSize:placement:"
- "reserveObjects"
- "reservePlacedOtherSerializerReference:"
- "reservePlacedTextureForReference:indices:"
- "run.fStart == fRuns[target].fStart"
- "search"
- "self.features->supportsArgumentBuffers"
- "setReductionMode:"
- "supportsResourceDetachment"
- "target >= 0"
- "v116@0:8I16Q20I28{?=QBB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@\"PGMemoryMap\"100@?<v@?Ii>108"
- "v116@0:8I16Q20I28{?=QBB}32{APVFeatures=BBBBBBBBBBBBBBBBBIIBBBBBBBBBBBBBBBBBBBBBBBB}48@100@?108"
- "v24@0:8I16B20"
- "v28@0:8I16@20"
- "v28@0:8I16^v20"
- "v32@0:8r*16Q24"
- "v40@0:8r*16Q24^(PGDeserializerPlacement=Q{?=QQ})32"
- "validateBackingDescriptor:dest:planeCount:backingAllocationLength:"
- "{?=QQ}32@0:8r*16Q24"
- "{unordered_map<unsigned int, PGPtr<PGResource *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<PGResource *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<PGResource *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLComputePipelineState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLComputePipelineState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLComputePipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLDepthStencilState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLDepthStencilState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLDepthStencilState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLFence>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLFence>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFence>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLFunction>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLFunction>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLFunction>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLRasterizationRateMap>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLRasterizationRateMap>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRasterizationRateMap>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLRenderPipelineState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLRenderPipelineState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLRenderPipelineState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, PGPtr<id<MTLSamplerState>>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, PGPtr<id<MTLSamplerState>>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, PGPtr<id<MTLSamplerState>>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "{unordered_set<unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<unsigned int>>=\"__table_\"{__hash_table<unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<unsigned int>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<unsigned int, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<unsigned int, void *> *>, std::allocator<std::__hash_node<unsigned int, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<unsigned int, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<unsigned int>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<unsigned int>>=\"__value_\"f}}}"

```
