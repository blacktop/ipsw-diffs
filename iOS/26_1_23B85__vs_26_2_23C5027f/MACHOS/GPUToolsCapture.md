## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-311.2.0.0.0
-  __TEXT.__text: 0x26a160
+312.2.0.0.0
+  __TEXT.__text: 0x26ab90
   __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x167e0
+  __TEXT.__objc_stubs: 0x16aa0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1247c
-  __TEXT.__const: 0x79d0
-  __TEXT.__cstring: 0x26b85
-  __TEXT.__gcc_except_tab: 0x8c8
-  __TEXT.__objc_methname: 0x19b1e
+  __TEXT.__objc_methlist: 0x12644
+  __TEXT.__const: 0x79c0
+  __TEXT.__cstring: 0x26c2e
+  __TEXT.__gcc_except_tab: 0x8dc
+  __TEXT.__objc_methname: 0x19c37
   __TEXT.__objc_classname: 0x157b
-  __TEXT.__objc_methtype: 0x9c72
+  __TEXT.__objc_methtype: 0x9c9c
   __TEXT.__oslogstring: 0xedb
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x3f00
+  __TEXT.__unwind_info: 0x3f78
   __DATA_CONST.__auth_got: 0xbd8
   __DATA_CONST.__got: 0x800
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1bd8
+  __DATA_CONST.__const: 0x1c50
   __DATA_CONST.__cfstring: 0x3ba0
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19a70
-  __DATA.__objc_selrefs: 0x6a00
-  __DATA.__objc_ivar: 0xa8c
+  __DATA.__objc_const: 0x19b80
+  __DATA.__objc_selrefs: 0x6a28
+  __DATA.__objc_ivar: 0xaa8
   __DATA.__objc_data: 0x1ea0
   __DATA.__data: 0x3458
   __DATA.__thread_vars: 0x48

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0155FD64-A588-3FE0-9A63-0A4CEC1CE18B
-  Functions: 7743
-  Symbols:   46102
-  CStrings:  9013
+  UUID: 4E8B0B62-15CB-3C74-8580-D3F9BD16FFC8
+  Functions: 7785
+  Symbols:   46347
+  CStrings:  9028
 
Symbols:
+ -[CaptureMTL4Archive captureDevice]
+ -[CaptureMTL4Archive initWithBaseObject:captureDevice:]
+ -[CaptureMTL4Archive newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[CaptureMTL4Archive newComputePipelineStateWithDescriptor:error:]
+ -[CaptureMTL4Archive newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:]
+ -[CaptureMTL4Archive newRenderPipelineStateWithDescriptor:error:]
+ -[CaptureMTL4BinaryFunction initWithBaseObject:captureArchive:]
+ -[CaptureMTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]
+ -[CaptureMTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:]
+ -[CaptureMTL4ComputeCommandEncoder commandBatchIdOffset]
+ -[CaptureMTL4ComputeCommandEncoder commandBatchIdRangeMin:max:]
+ -[CaptureMTL4ComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:]
+ -[CaptureMTL4ComputeCommandEncoder stages]
+ -[CaptureMTL4MachineLearningCommandEncoder commandBatchIdOffset]
+ -[CaptureMTL4MachineLearningCommandEncoder commandBatchIdRangeMin:max:]
+ -[CaptureMTL4RenderCommandEncoder commandBatchIdOffset]
+ -[CaptureMTL4RenderCommandEncoder commandBatchIdRangeMin:max:]
+ -[CaptureMTL4RenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:]
+ -[CaptureMTLComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:]
+ -[CaptureMTLComputePipelineState captureReflection]
+ -[CaptureMTLComputePipelineState initWithBaseObject:descriptor:captureArchive:]
+ -[CaptureMTLComputePipelineState initWithBaseObject:descriptor:dynamicLinkingDescriptor:captureArchive:]
+ -[CaptureMTLComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:]
+ -[CaptureMTLComputePipelineState setCaptureReflection:]
+ -[CaptureMTLDevice compileVisibleFunction:withDescriptor:completionHandler:]
+ -[CaptureMTLDevice mtlTensorFromGpuResourceID:]
+ -[CaptureMTLDevice newComputePipelineStateWithDescriptor:completionHandler:]
+ -[CaptureMTLDevice newRenderPipelineStateWithTileDescriptor:completionHandler:]
+ -[CaptureMTLDevice queryTimestampFrequency]
+ -[CaptureMTLDevice sizeOfCounterHeapEntry:]
+ -[CaptureMTLDevice supportsNonUniformThreadgroupSize]
+ -[CaptureMTLFunction reflectionWithOptions:completionHandler:]
+ -[CaptureMTLIndirectRenderCommand setToolsDispatchBufferSPI:atIndex:stages:]
+ -[CaptureMTLLibrary reflectionForFunctionWithName:]
+ -[CaptureMTLLogState addLogHandler:]
+ -[CaptureMTLRenderCommandEncoder addSplitHandler:]
+ -[CaptureMTLRenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:]
+ -[CaptureMTLRenderPipelineState captureReflection]
+ -[CaptureMTLRenderPipelineState initWithBaseObject:descriptor:captureArchive:]
+ -[CaptureMTLRenderPipelineState initWithBaseObject:descriptor:dynamicLinkingDescriptor:captureArchive:]
+ -[CaptureMTLRenderPipelineState setCaptureReflection:]
+ -[CaptureMTLTensor internalMTLBuffer]
+ GCC_except_table1522
+ GCC_except_table1547
+ GCC_except_table1652
+ GCC_except_table1653
+ GCC_except_table1657
+ GCC_except_table1658
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1661
+ GCC_except_table1868
+ GCC_except_table1869
+ GCC_except_table1871
+ GCC_except_table1873
+ GCC_except_table1882
+ GCC_except_table2026
+ GCC_except_table2062
+ GCC_except_table3026
+ GCC_except_table3188
+ GCC_except_table3282
+ GCC_except_table4003
+ GCC_except_table4544
+ GCC_except_table649
+ GTAccelerationStructureDescriptorDownloader_processCopy.7892
+ GTAccelerationStructureDescriptorDownloader_processRefit.7893
+ GetStream.19755
+ OBJC_IVAR_$_CaptureMTL4Archive._captureDevice
+ OBJC_IVAR_$_CaptureMTL4BinaryFunction._captureArchive
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._lastCommittedCaptureCommandBuffer
+ OBJC_IVAR_$_CaptureMTLComputePipelineState._captureArchive
+ OBJC_IVAR_$_CaptureMTLComputePipelineState._captureReflection
+ OBJC_IVAR_$_CaptureMTLRenderPipelineState._captureArchive
+ OBJC_IVAR_$_CaptureMTLRenderPipelineState._captureReflection
+ OBJC_IVAR_$_CaptureMTLTensor._captureBuffer
+ OBJC_IVAR_$_CaptureMTLTensor._parentTensor
+ RetainObjectForDescriptorDownloader.9495
+ StoreMTLCompileOptionsUsingEncode.16287
+ _DYTraceEncode_MTL4MachineLearningPipelineState_allocatedSize
+ _SaveMTL4CopySparseBufferMappingOperation
+ _SaveMTL4CopySparseTextureMappingOperation
+ _SaveMTLShaderSamplingProgramInfo
+ __Block_byref_object_copy_.11592
+ __Block_byref_object_copy_.3903
+ __Block_byref_object_copy_.4409
+ __Block_byref_object_dispose_.11593
+ __Block_byref_object_dispose_.3904
+ __Block_byref_object_dispose_.4410
+ ___103-[CaptureMTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:]_block_invoke
+ ___76-[CaptureMTLDevice newComputePipelineStateWithDescriptor:completionHandler:]_block_invoke
+ ___79-[CaptureMTLDevice newRenderPipelineStateWithTileDescriptor:completionHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e46_v24?0"<MTLRenderPipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e47_v24?0"<MTLComputePipelineState>"8"NSError"16ls32l8s40l8s48l8s56l8
+ __block_descriptor_tmp.15017
+ __block_literal_global.10321
+ __block_literal_global.10826
+ __block_literal_global.11596
+ __block_literal_global.12045
+ __block_literal_global.14930
+ __block_literal_global.15115
+ __block_literal_global.15182
+ __block_literal_global.15195
+ __block_literal_global.1670
+ __block_literal_global.184
+ __block_literal_global.20140
+ __block_literal_global.2945
+ __block_literal_global.4231
+ __block_literal_global.4418
+ __block_literal_global.482
+ __block_literal_global.7302
+ __block_literal_global.8075
+ __block_literal_global.8505
+ __block_literal_global.9472
+ _objc_msgSend$addLogHandler:
+ _objc_msgSend$addSplitHandler:
+ _objc_msgSend$commandBatchIdOffset
+ _objc_msgSend$commandBatchIdRangeMin:max:
+ _objc_msgSend$compileVisibleFunction:withDescriptor:completionHandler:
+ _objc_msgSend$initWithBaseObject:captureArchive:
+ _objc_msgSend$initWithBaseObject:descriptor:captureArchive:
+ _objc_msgSend$initWithBaseObject:descriptor:dynamicLinkingDescriptor:captureArchive:
+ _objc_msgSend$internalMTLBuffer
+ _objc_msgSend$mtlTensorFromGpuResourceID:
+ _objc_msgSend$newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:completionHandler:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:
+ _objc_msgSend$newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:
+ _objc_msgSend$newRenderPipelineStateWithTileDescriptor:completionHandler:
+ _objc_msgSend$queryTimestampFrequency
+ _objc_msgSend$reflectionWithOptions:completionHandler:
+ _objc_msgSend$setCaptureReflection:
+ _objc_msgSend$setToolsDispatchBufferSPI:atIndex:
+ _objc_msgSend$setToolsDispatchBufferSPI:atIndex:stages:
+ _objc_msgSend$sizeOfCounterHeapEntry:
+ _objc_msgSend$stages
+ name_array.16229
+ newHeapWithDescriptor:.onceToken.182
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7866
+ s_downloaderPipelines.0.7873
+ s_downloaderPipelines.1.7874
+ s_downloaderPipelines.2.7875
+ s_downloaderPipelines.3.7876
+ s_downloaderPipelines.4.7877
+ waitUntilSignaledValue:timeoutMS:.onceToken.13443
- -[CaptureMTL4Archive initWithBaseObject:captureContext:]
- -[CaptureMTL4BinaryFunction initWithBaseObject:captureContext:]
- -[CaptureMTLComputePipelineState setReflection:]
- -[CaptureMTLRenderPipelineState setReflection:]
- GCC_except_table1504
- GCC_except_table1529
- GCC_except_table1634
- GCC_except_table1635
- GCC_except_table1639
- GCC_except_table1640
- GCC_except_table1641
- GCC_except_table1642
- GCC_except_table1643
- GCC_except_table1849
- GCC_except_table1850
- GCC_except_table1852
- GCC_except_table1854
- GCC_except_table1863
- GCC_except_table2007
- GCC_except_table2044
- GCC_except_table2988
- GCC_except_table3149
- GCC_except_table3243
- GCC_except_table3960
- GCC_except_table4500
- GCC_except_table644
- GTAccelerationStructureDescriptorDownloader_processCopy.7848
- GTAccelerationStructureDescriptorDownloader_processRefit.7849
- GetStream.19685
- OBJC_IVAR_$_CaptureMTLComputePipelineState._reflection
- OBJC_IVAR_$_CaptureMTLRenderPipelineState._reflection
- RetainObjectForDescriptorDownloader.9442
- StoreMTLCompileOptionsUsingEncode.16210
- _DYTraceEncode_MTL4CommandQueue_copyBufferMappingsFromBuffer_toBuffer_operations_count
- _DYTraceEncode_MTL4CommandQueue_copyTextureMappingsFromTexture_toTexture_operations_count
- _DYTraceEncode_MTLCommandBuffer_sampledComputeCommandEncoderWithDescriptor_programInfoBuffer_capacity
- __Block_byref_object_copy_.11525
- __Block_byref_object_copy_.3913
- __Block_byref_object_copy_.4417
- __Block_byref_object_dispose_.11526
- __Block_byref_object_dispose_.3914
- __Block_byref_object_dispose_.4418
- __block_descriptor_tmp.14940
- __block_literal_global.10264
- __block_literal_global.10760
- __block_literal_global.11529
- __block_literal_global.11976
- __block_literal_global.14853
- __block_literal_global.15038
- __block_literal_global.15105
- __block_literal_global.15118
- __block_literal_global.1671
- __block_literal_global.181
- __block_literal_global.20070
- __block_literal_global.2957
- __block_literal_global.4241
- __block_literal_global.4426
- __block_literal_global.472
- __block_literal_global.7261
- __block_literal_global.8031
- __block_literal_global.8459
- __block_literal_global.9419
- _objc_msgSend$lastCommittedCommandBuffer
- _objc_msgSend$parentTensor
- _objc_msgSend$setReflection:
- name_array.16152
- newHeapWithDescriptor:.onceToken.179
- s_accelerationStructureDescriptorDownloaderPipelinesToken.7822
- s_downloaderPipelines.0.7829
- s_downloaderPipelines.1.7830
- s_downloaderPipelines.2.7831
- s_downloaderPipelines.3.7832
- s_downloaderPipelines.4.7833
- waitUntilSignaledValue:timeoutMS:.onceToken.13366
CStrings:
+ "0xffffc0e9"
+ "0xffffc0ea"
+ "@\"CaptureMTL4Archive\""
+ "@\"CaptureMTLTensor\""
+ "C@%zut@%zuul@%zuul@2ul"
+ "Internal SPI"
+ "Metal 4 Counter Heap"
+ "Render pipeline specialization"
+ "Resource pinning SPI"
+ "T@\"MTLComputePipelineReflection\",&,N,V_captureReflection"
+ "T@\"MTLRenderPipelineReflection\",&,N,V_captureReflection"
+ "_captureArchive"
+ "_captureReflection"
+ "_lastCommittedCaptureCommandBuffer"
+ "_parentTensor"
+ "captureReflection"
+ "initWithBaseObject:captureArchive:"
+ "initWithBaseObject:descriptor:captureArchive:"
+ "initWithBaseObject:descriptor:dynamicLinkingDescriptor:captureArchive:"
+ "internalMTLBuffer"
+ "kDYFEMTL4MachineLearningPipelineState_allocatedSize"
+ "kDYFEMTLLogState_addLogHandler"
+ "kDYFEMTLRenderCommandEncoder_setToolsDispatchBufferSPI_atIndex_stages"
+ "parentSliceCount >= texture->parentRelativeSlice"
+ "setCaptureReflection:"
- "C@%zutU<b>@2ul"
- "C@%zutU<b>U<b>@2ul"
- "CUU<b>ul"
- "CttU<b>ul"
- "T@\"MTLComputePipelineReflection\",&,N,V_reflection"
- "T@\"MTLRenderPipelineReflection\",&,N,V_reflection"
- "_reflection"
- "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
- "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
- "setReflection:"

```
