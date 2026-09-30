## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

-370.50.4.0.0
-  __TEXT.__text: 0x1d74a8
+370.54.0.0.0
+  __TEXT.__text: 0x1d76b8
   __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0x1d6ac
-  __TEXT.__gcc_except_tab: 0xb2d4
-  __TEXT.__cstring: 0x21fed
-  __TEXT.__const: 0x2cdb0
+  __TEXT.__objc_methlist: 0x1d66c
+  __TEXT.__gcc_except_tab: 0xb2d0
+  __TEXT.__cstring: 0x2205f
+  __TEXT.__const: 0x2cda0
   __TEXT.__oslogstring: 0x1e1b
   __TEXT.__ustring: 0x1be
   __TEXT.text_env: 0x2574
-  __TEXT.__unwind_info: 0x81c8
+  __TEXT.__unwind_info: 0x81a8
   __TEXT.__eh_frame: 0x78
-  __TEXT.__objc_classname: 0x3f09
-  __TEXT.__objc_methname: 0x3542d
-  __TEXT.__objc_methtype: 0x17530
-  __TEXT.__objc_stubs: 0x155e0
-  __DATA_CONST.__got: 0x9a8
+  __TEXT.__objc_classname: 0x3ecb
+  __TEXT.__objc_methname: 0x354e4
+  __TEXT.__objc_methtype: 0x175c7
+  __TEXT.__objc_stubs: 0x15560
+  __DATA_CONST.__got: 0x9a0
   __DATA_CONST.__const: 0x3018
-  __DATA_CONST.__objc_classlist: 0xcd0
+  __DATA_CONST.__objc_classlist: 0xcc0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8778
+  __DATA_CONST.__objc_selrefs: 0x8798
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0xbd0
+  __DATA_CONST.__objc_superrefs: 0xbc0
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0xe90
   __AUTH_CONST.__const: 0x4f80
-  __AUTH_CONST.__cfstring: 0x123e0
-  __AUTH_CONST.__objc_const: 0x44a98
+  __AUTH_CONST.__cfstring: 0x12460
+  __AUTH_CONST.__objc_const: 0x44898
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3d40
-  __DATA.__objc_ivar: 0x20bc
+  __AUTH.__objc_data: 0x3ca0
+  __DATA.__objc_ivar: 0x20ac
   __DATA.__data: 0x4400
-  __DATA.__bss: 0x394
+  __DATA.__bss: 0x384
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x42e0
-  __DATA_DIRTY.__data: 0x78
+  __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__bss: 0x280
   __DATA_DIRTY.__common: 0x11
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5995FBE-3EC8-31D2-865B-29119744A3F4
-  Functions: 12804
-  Symbols:   40362
-  CStrings:  15641
+  UUID: 9D3D5E4D-AAA1-31D9-8D5A-662E6481D63C
+  Functions: 12798
+  Symbols:   40326
+  CStrings:  15651
 
Symbols:
+ -[MTL4CompilerDescriptor dealloc]
+ -[MTL4CompilerTaskOptions dealloc]
+ -[MTL4CounterHeapDescriptor count]
+ -[MTL4CounterHeapDescriptor setCount:]
+ -[MTL4LibraryDescriptor dealloc]
+ -[MTL4PipelineDescriptor reset]
+ -[MTLDeviceFeatureQueries familySupportsAtomicFloat]
+ -[MTLDeviceFeatureQueries supportsAtomicFloat]
+ -[MTLFunctionStitchingGraph hash]
+ -[MTLFunctionStitchingGraph isEqual:]
+ -[MTLRenderPassDescriptor setSupportColorAttachmentMapping:]
+ -[MTLRenderPassDescriptor supportColorAttachmentMapping]
+ -[MTLTensorDescriptor validateWithBuffer:offset:error:].cold.3
+ -[MTLTensorDescriptor validateWithBuffer:offset:error:].cold.4
+ -[MTLTensorDescriptor validateWithBuffer:offset:error:].cold.5
+ -[_MTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:]
+ -[_MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:]
+ -[_MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:]
+ -[_MTLCommandEncoder setColorAttachmentMap:]
+ -[_MTLDevice supportsAtomicFloat]
+ -[_MTLDeviceFeatureQueries familySupportsAtomicFloat]
+ GCC_except_table300
+ GCC_except_table377
+ GCC_except_table391
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table444
+ GCC_except_table447
+ GCC_except_table452
+ GCC_except_table710
+ GCC_except_table748
+ GCC_except_table750
+ GCC_except_table797
+ GCC_except_table819
+ _MTLShouldEnableNewCompilerScheduler
+ _OBJC_IVAR_$_MTL4CounterHeapDescriptor._count
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsAtomicFloat
+ _OBJC_IVAR_$_MTLRenderPassDescriptor._supportColorAttachmentMapping
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CompilerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CompilerSPI
+ __ZGVZN19MTLEnvVarAggregator34GET_MTL_COMPILER_SCHEDULER_VERSIONEbiE2ev
+ __ZL19MTLGPUFamilyApple9B
+ __ZN15MTL4ArchiveImpl14copyRemapArrayEP38MTLLogicalToPhysicalColorAttachmentMapS1_
+ __ZN19MTLEnvVarAggregator34GET_MTL_COMPILER_SCHEDULER_VERSIONEbi
+ __ZN19MTLEnvVarAggregator34GET_MTL_COMPILER_SCHEDULER_VERSIONEbi.cold.1
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN20MTLCompilerScheduler16initializeCountsEvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN26MTLLegacyCompilerScheduler16initializeCountsEvE3$_0EEEEEvPv
+ __ZNSt3__16vectorI12MTLGPUFamilyNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZZN19MTLEnvVarAggregator34GET_MTL_COMPILER_SCHEDULER_VERSIONEbiE2ev
+ ___block_literal_global.1276
+ ___block_literal_global.1356
+ ___block_literal_global.1698
+ ___block_literal_global.1812
+ ___block_literal_global.1815
+ ___block_literal_global.1975
+ ___block_literal_global.2100
+ ___block_literal_global.2320
+ ___block_literal_global.2323
+ ___block_literal_global.2325
+ _objc_msgSend$familySupportsAtomicFloat
+ _objc_msgSend$supportsAtomicFloat
- -[MTL4LinkedFunctions binaryFunctions]
- -[MTL4LinkedFunctions copyWithZone:]
- -[MTL4LinkedFunctions dealloc]
- -[MTL4LinkedFunctions functionDescriptors]
- -[MTL4LinkedFunctions groups]
- -[MTL4LinkedFunctions hash]
- -[MTL4LinkedFunctions init]
- -[MTL4LinkedFunctions isEqual:]
- -[MTL4LinkedFunctions privateFunctionDescriptors]
- -[MTL4LinkedFunctions setBinaryFunctions:]
- -[MTL4LinkedFunctions setFunctionDescriptors:]
- -[MTL4LinkedFunctions setGroups:]
- -[MTL4LinkedFunctions setPrivateFunctionDescriptors:]
- -[MTL4MachineLearningPipelineDescriptor label]
- -[MTL4MachineLearningPipelineDescriptor setLabel:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI copyWithZone:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI getPhysicalIndexForLogicalIndex:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI hash]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI init]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI isEqual:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI map:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI reset]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI setPhysicalIndex:forLogicalIndex:]
- -[MTLLogicalToPhysicalColorAttachmentMapSPI setPhysicalIndex:forLogicalIndex:].cold.1
- -[MTLLogicalToPhysicalColorAttachmentMapSPI setPhysicalIndex:forLogicalIndex:].cold.2
- -[_MTLResource getBytes:strides:fromSliceOrigin:sliceDimensions:]
- -[_MTLResource replaceSliceOrigin:sliceDimensions:withBytes:strides:]
- GCC_except_table366
- GCC_except_table369
- GCC_except_table372
- GCC_except_table375
- GCC_except_table390
- GCC_except_table406
- GCC_except_table408
- GCC_except_table419
- GCC_except_table443
- GCC_except_table446
- GCC_except_table451
- GCC_except_table453
- GCC_except_table749
- GCC_except_table796
- GCC_except_table799
- GCC_except_table808
- GCC_except_table813
- GCC_except_table818
- _MTLRenderTargetRemapIndexDiscard
- _OBJC_CLASS_$_MTL4LinkedFunctions
- _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- _OBJC_IVAR_$_MTL4CounterHeapDescriptor._entryCount
- _OBJC_IVAR_$_MTL4LinkedFunctions._binaryFunctions
- _OBJC_IVAR_$_MTL4LinkedFunctions._functionDescriptors
- _OBJC_IVAR_$_MTL4LinkedFunctions._groups
- _OBJC_IVAR_$_MTL4LinkedFunctions._privateFunctionDescriptors
- _OBJC_IVAR_$_MTL4MachineLearningPipelineDescriptor._label
- _OBJC_IVAR_$_MTLLogicalToPhysicalColorAttachmentMapSPI._logicalToPhysicalMap
- _OBJC_METACLASS_$_MTL4LinkedFunctions
- _OBJC_METACLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __OBJC_$_INSTANCE_METHODS_MTL4LinkedFunctions
- __OBJC_$_INSTANCE_METHODS_MTLLogicalToPhysicalColorAttachmentMapSPI
- __OBJC_$_INSTANCE_VARIABLES_MTL4LinkedFunctions
- __OBJC_$_INSTANCE_VARIABLES_MTLLogicalToPhysicalColorAttachmentMapSPI
- __OBJC_$_PROP_LIST_MTL4LinkedFunctions
- __OBJC_CLASS_PROTOCOLS_$_MTL4LinkedFunctions
- __OBJC_CLASS_PROTOCOLS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __OBJC_CLASS_RO_$_MTL4LinkedFunctions
- __OBJC_CLASS_RO_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __OBJC_METACLASS_RO_$_MTL4LinkedFunctions
- __OBJC_METACLASS_RO_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __ZGVZN19MTLEnvVarAggregator39GET_MTL_NEW_COMPILER_SCHEDULER_INTERNALEbbE2ev
- __ZGVZN19MTLEnvVarAggregator47GET_MTL_DISABLE_NEW_COMPILER_SCHEDULER_INTERNALEbbE2ev
- __ZN15MTL4ArchiveImpl14copyRemapArrayEP41MTLLogicalToPhysicalColorAttachmentMapSPIP38MTLLogicalToPhysicalColorAttachmentMap
- __ZN19MTLEnvVarAggregator39GET_MTL_NEW_COMPILER_SCHEDULER_INTERNALEbb
- __ZN19MTLEnvVarAggregator39GET_MTL_NEW_COMPILER_SCHEDULER_INTERNALEbb.cold.1
- __ZN19MTLEnvVarAggregator47GET_MTL_DISABLE_NEW_COMPILER_SCHEDULER_INTERNALEbb
- __ZN19MTLEnvVarAggregator47GET_MTL_DISABLE_NEW_COMPILER_SCHEDULER_INTERNALEbb.cold.1
- __ZZN19MTLEnvVarAggregator39GET_MTL_NEW_COMPILER_SCHEDULER_INTERNALEbbE2ev
- __ZZN19MTLEnvVarAggregator47GET_MTL_DISABLE_NEW_COMPILER_SCHEDULER_INTERNALEbbE2ev
- __ZZN20MTLCompilerScheduler16initializeCountsEvE9onceToken
- __ZZN26MTLLegacyCompilerScheduler16initializeCountsEvE9onceToken
- ____ZN20MTLCompilerScheduler16initializeCountsEv_block_invoke
- ____ZN26MTLLegacyCompilerScheduler16initializeCountsEv_block_invoke
- ___block_literal_global.1274
- ___block_literal_global.1354
- ___block_literal_global.1696
- ___block_literal_global.1810
- ___block_literal_global.1813
- ___block_literal_global.1974
- ___block_literal_global.2099
- ___block_literal_global.2319
- ___block_literal_global.2322
- ___block_literal_global.2324
- _objc_msgSend$fragmentLinkingDescriptor
- _objc_msgSend$meshLinkingDescriptor
- _objc_msgSend$objectLinkingDescriptor
- _objc_msgSend$setBinaryFunctions:
- _objc_msgSend$tileLinkingDescriptor
- _objc_msgSend$vertexLinkingDescriptor
CStrings:
+ "23:18:55"
+ "Atomic Float"
+ "If objectFunction is nil, requiredThreadsPerObjectThreadgroup must be [0, 0, 0] but is [%lu, %lu, %lu]"
+ "Jun 15 2025"
+ "Jun 15 2025 23:18:55"
+ "MTL_COMPILER_SCHEDULER_VERSION"
+ "T@\"MTL4PipelineOptions\",&,N,V_pipelineOptions"
+ "TB,N,V_supportColorAttachmentMapping"
+ "TB,R,N,V_familySupportsAtomicFloat"
+ "TQ,N,V_count"
+ "Tensor's cpu cache mode (0x%lu) should match the buffer's cpu cache mode (0x%lu)"
+ "Tensor's hazard tracking mode (0x%lu) should match the buffer's hazard tracking mode (0x%lu)"
+ "Tensor's storage mode (0x%lu) should match the buffer's storage mode (0x%lu)"
+ "[224{?=\"name\"@\"NSString\"\"requirement\"q\"supported\"B}]"
+ "_familySupportsAtomicFloat"
+ "_supportColorAttachmentMapping"
+ "familySupportsAtomicFloat"
+ "resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:"
+ "setCount:"
+ "supportsAtomicFloat"
+ "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@\"<MTLFence>\"56@\"<MTLFence>\"64"
+ "v72@0:8@16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@56@64"
- "-[MTLLogicalToPhysicalColorAttachmentMapSPI setPhysicalIndex:forLogicalIndex:]"
- "23:48:06"
- "MTL4LinkedFunctions"
- "MTLLogicalToPhysicalColorAttachmentMapSPI"
- "MTL_DISABLE_NEW_COMPILER_SCHEDULER_INTERNAL"
- "MTL_NEW_COMPILER_SCHEDULER_INTERNAL"
- "May 27 2025"
- "May 27 2025 23:48:06"
- "T@\"MTL4PipelineOptions\",N,V_pipelineOptions"
- "T@\"NSArray\",C,N,V_binaryFunctions"
- "TQ,N,V_entryCount"
- "Tensor's resource options (0x%lx) should match the buffer's resource options (0x%lx)"
- "[223{?=\"name\"@\"NSString\"\"requirement\"q\"supported\"B}]"
- "_binaryFunctions"
- "_entryCount"
- "bitset test argument out of range"

```
