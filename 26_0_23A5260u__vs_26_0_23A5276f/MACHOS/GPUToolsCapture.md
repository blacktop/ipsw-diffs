## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-310.22.0.0.0
-  __TEXT.__text: 0x2614ec
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x15d40
+310.25.0.0.0
+  __TEXT.__text: 0x262dac
+  __TEXT.__auth_stubs: 0x1790
+  __TEXT.__objc_stubs: 0x15f60
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x11f44
-  __TEXT.__const: 0x7950
-  __TEXT.__cstring: 0x26839
+  __TEXT.__objc_methlist: 0x12004
+  __TEXT.__const: 0x7970
+  __TEXT.__cstring: 0x26971
   __TEXT.__gcc_except_tab: 0x884
   __TEXT.__oslogstring: 0xedb
   __TEXT.__objc_classname: 0x1536
-  __TEXT.__objc_methname: 0x192fb
-  __TEXT.__objc_methtype: 0x9ad3
+  __TEXT.__objc_methname: 0x1941c
+  __TEXT.__objc_methtype: 0x9ab3
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x3e20
-  __DATA_CONST.__auth_got: 0xbd8
-  __DATA_CONST.__got: 0x800
+  __TEXT.__unwind_info: 0x3e38
+  __DATA_CONST.__auth_got: 0xbe0
+  __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1960
+  __DATA_CONST.__const: 0x1988
   __DATA_CONST.__cfstring: 0x3ba0
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19440
-  __DATA.__objc_selrefs: 0x6760
+  __DATA.__objc_const: 0x19520
+  __DATA.__objc_selrefs: 0x67c8
   __DATA.__objc_ivar: 0xa68
   __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x3398

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D2F175D7-AB5C-3DE3-B15E-E7BBDE4EA7E7
-  Functions: 7616
-  Symbols:   45283
-  CStrings:  8895
+  UUID: 3159B148-961F-3B7B-9135-3A8802BC9007
+  Functions: 7633
+  Symbols:   45387
+  CStrings:  8913
 
Symbols:
+ -[CaptureMTL4ArgumentTable setAddress:attributeStride:atIndex:]
+ -[CaptureMTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:]
+ -[CaptureMTLDevice commandQueueLimit]
+ -[CaptureMTLDevice currentCommandQueueCount]
+ -[CaptureMTLDevice defaultCompilerProcessesCount]
+ -[CaptureMTLDevice maximumCompilerProcessesCount]
+ -[CaptureMTLDevice requiresLegacyCompilerProcessesCount]
+ -[CaptureMTLDevice setRequiresLegacyCompilerProcessesCount:]
+ -[CaptureMTLDevice threadsPerCompilerProcess]
+ GCC_except_table1473
+ GCC_except_table1499
+ GCC_except_table1602
+ GCC_except_table1606
+ GCC_except_table1607
+ GCC_except_table1608
+ GCC_except_table1609
+ GCC_except_table1610
+ GCC_except_table1816
+ GCC_except_table1817
+ GCC_except_table1819
+ GCC_except_table1830
+ GCC_except_table1974
+ GCC_except_table2011
+ GCC_except_table2948
+ GCC_except_table3109
+ GCC_except_table3203
+ GCC_except_table3902
+ GCC_except_table4414
+ GTAccelerationStructureDescriptorDownloader_processCopy.7815
+ GTAccelerationStructureDescriptorDownloader_processRefit.7816
+ GetStream.19550
+ RetainObjectForDescriptorDownloader.9402
+ StoreMTLCompileOptionsUsingEncode.16102
+ _DYTraceEncode_MTL4ArgumentTable_setAddress_attributeStride_atIndex
+ _DYTraceEncode_MTLCommandBuffer___waitUntilCompletedAsync
+ _DYTraceEncode_MTLCommandBuffer___waitUntilScheduledAsync
+ _DYTraceEncode_MTLDevice_setRequiresLegacyCompilerProcessesCount
+ _DYTraceEncode_MTLFXTemporalDenoisedScaler_executionMode
+ _GTMTL4SMArgumentTable_bufferBindingHasAttributeStride
+ _GTMTL4SMArgumentTable_bufferBindingsMatch
+ _GTMTL4SMArgumentTable_clearBufferBindingHasAttributeStride
+ _GTMTL4SMArgumentTable_setBufferBindingHasAttributeStride
+ __Block_byref_object_copy_.11481
+ __Block_byref_object_copy_.3886
+ __Block_byref_object_copy_.4389
+ __Block_byref_object_dispose_.11482
+ __Block_byref_object_dispose_.3887
+ __Block_byref_object_dispose_.4390
+ ___53-[CaptureMTLCommandBuffer __waitUntilCompletedAsync:]_block_invoke
+ ___53-[CaptureMTLCommandBuffer __waitUntilScheduledAsync:]_block_invoke
+ ___block_descriptor_40_e8_32s_e1263_v28?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLAttribute}^{GTMTLAttribute}^**}16B24ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8s48l8
+ __block_descriptor_tmp.14836
+ __block_literal_global.10223
+ __block_literal_global.10719
+ __block_literal_global.11485
+ __block_literal_global.11931
+ __block_literal_global.14749
+ __block_literal_global.14934
+ __block_literal_global.15001
+ __block_literal_global.15014
+ __block_literal_global.1660
+ __block_literal_global.19931
+ __block_literal_global.2935
+ __block_literal_global.4212
+ __block_literal_global.4398
+ __block_literal_global.7230
+ __block_literal_global.7998
+ __block_literal_global.8417
+ __block_literal_global.9379
+ _objc_msgSend$commandQueueLimit
+ _objc_msgSend$currentCommandQueueCount
+ _objc_msgSend$defaultCompilerProcessesCount
+ _objc_msgSend$maxMeshBufferBindCount
+ _objc_msgSend$maxObjectBufferBindCount
+ _objc_msgSend$maxObjectThreadgroupMemoryBindCount
+ _objc_msgSend$maximumCompilerProcessesCount
+ _objc_msgSend$requiresLegacyCompilerProcessesCount
+ _objc_msgSend$resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:
+ _objc_msgSend$setAddress:attributeStride:atIndex:
+ _objc_msgSend$setMaxMeshBufferBindCount:
+ _objc_msgSend$setMaxObjectBufferBindCount:
+ _objc_msgSend$setMaxObjectThreadgroupMemoryBindCount:
+ _objc_msgSend$setRequiresLegacyCompilerProcessesCount:
+ _objc_msgSend$setSupportMTLEvent:
+ _objc_msgSend$supportMTLEvent
+ _objc_msgSend$threadsPerCompilerProcess
+ _objc_retain_x7
+ name_array.16043
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7789
+ s_downloaderPipelines.0.7796
+ s_downloaderPipelines.1.7797
+ s_downloaderPipelines.2.7798
+ s_downloaderPipelines.3.7799
+ s_downloaderPipelines.4.7800
+ waitUntilSignaledValue:timeoutMS:.onceToken.13265
- GCC_except_table1464
- GCC_except_table1490
- GCC_except_table1592
- GCC_except_table1593
- GCC_except_table1597
- GCC_except_table1598
- GCC_except_table1599
- GCC_except_table1600
- GCC_except_table1807
- GCC_except_table1808
- GCC_except_table1810
- GCC_except_table1812
- GCC_except_table1965
- GCC_except_table2002
- GCC_except_table2938
- GCC_except_table3099
- GCC_except_table3193
- GCC_except_table3892
- GCC_except_table4403
- GTAccelerationStructureDescriptorDownloader_processCopy.7809
- GTAccelerationStructureDescriptorDownloader_processRefit.7810
- GetStream.19513
- RetainObjectForDescriptorDownloader.9397
- StoreMTLCompileOptionsUsingEncode.16073
- _GTFenum_isSetTextureViewWithDescriptor
- _MakeGTMTLLogicalToPhysicalColorAttachmentMapSPI
- _MakeMTLLogicalToPhysicalColorAttachmentMapSPI
- _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __Block_byref_object_copy_.11476
- __Block_byref_object_copy_.3870
- __Block_byref_object_copy_.4375
- __Block_byref_object_dispose_.11477
- __Block_byref_object_dispose_.3871
- __Block_byref_object_dispose_.4376
- ___block_descriptor_40_e8_32s_e1269_v28?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLVertexAttribute}^{GTMTLAttribute}^**}16B24ls32l8
- __block_descriptor_tmp.14824
- __block_literal_global.10220
- __block_literal_global.10716
- __block_literal_global.11480
- __block_literal_global.11925
- __block_literal_global.14736
- __block_literal_global.14922
- __block_literal_global.14990
- __block_literal_global.15003
- __block_literal_global.1659
- __block_literal_global.19894
- __block_literal_global.2919
- __block_literal_global.4196
- __block_literal_global.4384
- __block_literal_global.7224
- __block_literal_global.7992
- __block_literal_global.8412
- __block_literal_global.9374
- name_array.16014
- s_accelerationStructureDescriptorDownloaderPipelinesToken.7783
- s_downloaderPipelines.0.7790
- s_downloaderPipelines.1.7791
- s_downloaderPipelines.2.7792
- s_downloaderPipelines.3.7793
- s_downloaderPipelines.4.7794
- waitUntilSignaledValue:timeoutMS:.onceToken.13259
CStrings:
+ "@\"<MTL4CompilerSPI>\""
+ "contentHeight"
+ "contentWidth"
+ "kDYFEMTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence"
+ "kDYFEMTLDevice_defaultCompilerProcessesCount"
+ "kDYFEMTLDevice_maximumCompilerProcessesCount"
+ "kDYFEMTLDevice_setRequiresLegacyCompilerProcessesCount"
+ "kDYFEMTLDevice_threadsPerCompilerProcess"
+ "kDYFEMTLFXTemporalDenoisedScaler_executionMode"
+ "maxMeshBufferBindCount"
+ "maxObjectBufferBindCount"
+ "maxObjectThreadgroupMemoryBindCount"
+ "resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:"
+ "setContentHeight:"
+ "setContentWidth:"
+ "setMaxMeshBufferBindCount:"
+ "setMaxObjectBufferBindCount:"
+ "setMaxObjectThreadgroupMemoryBindCount:"
+ "setSupportMTLEvent:"
+ "supportMTLEvent"
+ "supportsAtomicFloat"
+ "v28@?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLAttribute}^{GTMTLAttribute}^**}16B24"
+ "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@\"<MTLFence>\"56@\"<MTLFence>\"64"
+ "v72@0:8@16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@56@64"
- "@\"<MTL4Compiler>\""
- "resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:"
- "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMapSPI\"16"
- "v28@?0^{GTMTLRenderPipelineReflection=QQQ^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^{GTMTLBinding}^*^*{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}{GTData=^vQ}ISSSSSSSSSS{?={?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}{?=[1{?=QQ}][2{?=QQ}][1Q]}}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}^{GTMTL4FunctionReflection}}8^{GTMTLPipelineReflectionAllocator=^{GTMTLAccelerationStructureInfo}^{GTMTLBufferInfo}^{GTMTLDynamicLibraryInfo}^{GTMTLFunctionInfo}^{GTMTLFunctionHandleInfo}^{GTMTLIndirectCommandBufferInfo}^{GTMTLIntersectionFunctionTableInfo}^{GTMTLLibraryInfo}^{GTMTLPipelineLibraryInfo}^{GTMTLSamplerStateInfo}^{GTMTLDepthStencilStateInfo}^{GTMTLTensorInfo}^{GTMTLTextureInfo}^{GTMTLVisibleFunctionTableInfo}^{GTMTLComputePipelineReflection}^{GTMTLRenderPipelineReflection}^{GTMTL4MachineLearningPipelineReflection}^{GTMTL4FunctionReflection}^{GTMTLTextureLevelInfo}^{GTMTLBinding}^{GTMTLPointerType}^{GTMTLStructType}^{GTMTLStructMember}^{GTMTLArrayType}^{GTMTLTextureReferenceType}^{GTMTLTensorReferenceType}^{GTMTLVertexAttribute}^{GTMTLAttribute}^**}16B24"
- "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24@\"<MTLBuffer>\"40Q48@\"<MTLFence>\"56@\"<MTLFence>\"64"
- "v72@0:8@16{_NSRange=QQ}24@40Q48@56@64"

```
