## MPSBenchmarkLoop

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop`

```diff

-128.5.2.0.0
-  __TEXT.__text: 0x95fc
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x2acc
+129.0.14.0.0
+  __TEXT.__text: 0x97cc
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x2d04
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__cstring: 0x1536
+  __TEXT.__gcc_except_tab: 0x244
+  __TEXT.__cstring: 0x159c
   __TEXT.__ustring: 0x48
   __TEXT.__unwind_info: 0x300
   __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x7cc7
-  __TEXT.__objc_methtype: 0x3505
-  __TEXT.__objc_stubs: 0x1420
+  __TEXT.__objc_methname: 0x8337
+  __TEXT.__objc_methtype: 0x397d
+  __TEXT.__objc_stubs: 0x1480
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ad8
+  __DATA_CONST.__objc_selrefs: 0x1c60
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x4c58
+  __AUTH_CONST.__objc_const: 0x4f38
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x300
   __DATA.__common: 0xc
   __DATA.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA9FD509-F622-3593-B02F-279DF65282E0
-  Functions: 239
-  Symbols:   152
-  CStrings:  1674
+  UUID: FC6EAD8C-04E6-3588-92EC-DD5815C00F12
+  Functions: 240
+  Symbols:   151
+  CStrings:  1750
 
Symbols:
- __Znwm
CStrings:
+ "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
+ "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
+ "@\"<MTL4CommandAllocator>\"16@0:8"
+ "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
+ "@\"<MTL4CommandBuffer>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
+ "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
+ "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
+ "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTLFunction>\"16"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"<MTLFunction>\"16Q24"
+ "@\"<MTLLibrary>\"40@0:8@\"NSURL\"16@\"NSString\"24^@32"
+ "@\"<MTLTensor>\"24@0:8{MTLResourceID=Q}16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@24@0:8{MTLResourceID=Q}16"
+ "@40@0:8Q16Q24q32"
+ "MPS_BENCHMARK_LOOP_ENABLE_GPU_OVERLAP"
+ "MPS_BENCHMARK_LOOP_ENABLE_GPU_OVERLAP environment variable set\n"
+ "Ti,R"
+ "_commandBufferOverlap"
+ "barrierAfterQueueStages:beforeStages:"
+ "copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:"
+ "defaultCompilerProcessesCount"
+ "encodeSignalEvent:value:"
+ "encodeWaitForEvent:value:"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithFunction:"
+ "functionHandleWithFunction:resourceIndex:"
+ "llvmVersion"
+ "maximumCompilerProcessesCount"
+ "mtlTensorFromGpuResourceID:"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCommandBuffer"
+ "newCompilerWithDescriptor:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newLibraryWithMPSGraphPackageURL:name:error:"
+ "newMTL4CommandQueue"
+ "newMTL4CommandQueueWithDescriptor:error:"
+ "newPipelineDataSetSerializerWithDescriptor:"
+ "newTensorWithDescriptor:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "queryTimestampFrequency"
+ "requiresLegacyCompilerProcessesCount"
+ "setRequiresLegacyCompilerProcessesCount:"
+ "sizeOfCounterHeapEntry:"
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
+ "tensorSizeAndAlignWithDescriptor:"
+ "threadsPerCompilerProcess"
+ "v64@0:8@\"<MTLTensor>\"16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"<MTLTensor>\"40@\"MTLTensorExtents\"48@\"MTLTensorExtents\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"

```
