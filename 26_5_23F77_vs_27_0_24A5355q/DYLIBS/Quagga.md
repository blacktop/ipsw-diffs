## Quagga

> `/System/Library/PrivateFrameworks/Quagga.framework/Quagga`

```diff

-226.0.0.0.0
-  __TEXT.__text: 0xed338
-  __TEXT.__auth_stubs: 0x1dd0
-  __TEXT.__objc_methlist: 0x8c4
-  __TEXT.__const: 0x24410
-  __TEXT.__cstring: 0x4e9a
+234.0.0.0.0
+  __TEXT.__text: 0xf2bc0
+  __TEXT.__objc_methlist: 0x8cc
+  __TEXT.__const: 0x24768
+  __TEXT.__cstring: 0x4ef0
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__gcc_except_tab: 0x90f0
-  __TEXT.__oslogstring: 0x66de
-  __TEXT.__unwind_info: 0x3440
-  __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0x1b7e
-  __TEXT.__objc_methtype: 0x1475
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x1328
+  __TEXT.__gcc_except_tab: 0x8f64
+  __TEXT.__oslogstring: 0x6fed
+  __TEXT.__unwind_info: 0x34d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1368
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__weak_got: 0x18
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xef8
-  __AUTH_CONST.__const: 0x7b68
-  __AUTH_CONST.__cfstring: 0x3c60
-  __AUTH_CONST.__objc_const: 0xba0
+  __DATA_CONST.__got: 0x588
+  __AUTH_CONST.__const: 0x7b90
+  __AUTH_CONST.__cfstring: 0x3ba0
+  __AUTH_CONST.__objc_const: 0xba8
+  __AUTH_CONST.__weak_auth_got: 0x38
+  __AUTH_CONST.__auth_got: 0xee0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x300
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x1f8
-  __DATA_DIRTY.__bss: 0xd40
+  __DATA_DIRTY.__bss: 0xd30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6FFC62F-9FD0-327D-B06B-B7918A05A577
-  Functions: 3249
-  Symbols:   918
-  CStrings:  2229
+  UUID: B8CB3844-797A-3142-A95B-146C008D5FF9
+  Functions: 3289
+  Symbols:   922
+  CStrings:  1866
 
Symbols:
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_retain_x9
+ _os_unfair_lock_lock
+ _os_unfair_lock_trylock
+ _os_unfair_lock_trylock_with_options
+ _os_variant_has_internal_diagnostics
+ _pthread_get_qos_class_np
+ _pthread_mach_thread_np
+ _pthread_override_qos_class_end_np
+ _pthread_override_qos_class_start_np
+ _pthread_self
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- ___cxa_rethrow
- _dispatch_time
- _malloc_create_zone
- _malloc_type_zone_malloc
- _malloc_type_zone_realloc
- _malloc_zone_free
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x27
- _perror
CStrings:
+ "<unknown>"
+ "<unknown> (%#x)"
+ "ACBS2D"
+ "ANMDModel"
+ "Current thread %{public}p with id %{public}#llx has QoS %{public}s (%#x) with relative priority %{public}d"
+ "Elapsed time waiting for model to be loaded: %{public}llu nanoseconds"
+ "Elapsed time waiting for model to be loaded: %{public}llu units in terms of mach absolute time"
+ "Encountered luminance source with zero width and/or height: width=%{public}d, height=%{public}d, isMaster=%{public, bool}d, pyramidLevelIndex=%{public}zd"
+ "Ended overriding QoS of preflight thread with token %{public}p"
+ "Failed to end QoS of preflight thread with token %{public}p: %{public, errno}d"
+ "HasAppleNeuralEngine"
+ "IIEModel"
+ "LegacyPyramidGenerationSession"
+ "Model loading is likely in-progress, attempting to wait with a timeout after %{public}llu nanoseconds, current QoS is %{public}x, relative priority is %{public}d"
+ "ModelLoadingTimeoutFault"
+ "Preflight thread %{public}p with id %{public}#llx has QoS %{public}s (%#x) with relative priority %{public}d"
+ "Preflight thread has higher priority than the current thread, skipping priority boosting"
+ "Preflight thread has lower priority than the current thread, attempt to boost priority for likely upcoming priority inversion"
+ "Proceed to load model, current QoS is %{public}x, relative priority is %{public}d"
+ "PyramidGenerationSession"
+ "Started overriding QoS of preflight thread with token %{public}p"
+ "Threading"
+ "Unable to override QoS of preflight thread"
+ "Unable to retrieve QoS from the current thread %{public}p with id %{public}#llx"
+ "Unable to retrieve QoS from the preflight thread %{public}p with id %{public}#llx"
+ "Underlying context has on-going preflight on thread %{public}p with id %{public}#llx"
+ "[PREFLIGHTING] context %{public}p: done preflighting %{public}.*s"
+ "[PREFLIGHTING] context %{public}p: done preflighting on thread %{public}p with id %{public}#llx"
+ "[PREFLIGHTING] context %{public}p: failed to preflight %{public}.*s, error: %{public}@"
+ "[PREFLIGHTING] context %{public}p: on-going preflight on thread %{public}p with id %{public}#llx, skipping recording the current preflight thread %{public}p with id %{public}#llx for possible priority boosting"
+ "[PREFLIGHTING] context %{public}p: preflighting %{public}.*s"
+ "[PREFLIGHTING] context %{public}p: starts preflighting on thread %{public}p with id %{public}#llx"
+ "mach_timebase_info failed: %{public}d"
+ "maintenance"
+ "pthread_get_qos_class_np failed: %{public, errno}d"
+ "pthread_get_qos_class_np(%{public}p) failed: %{public, errno}d"
+ "pthread_threadid_np(%{public}p) failed: %{public, errno}d"
- "#16@0:8"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ".cxx_destruct"
- "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
- "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
- "@\"<MTL4CommandAllocator>\"16@0:8"
- "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
- "@\"<MTL4CommandBuffer>\"16@0:8"
- "@\"<MTL4CommandQueue>\"16@0:8"
- "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
- "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
- "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
- "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
- "@\"<MTLAccelerationStructure>\"24@0:8@\"MTLAccelerationStructureDescriptor\"16"
- "@\"<MTLAccelerationStructure>\"24@0:8Q16"
- "@\"<MTLArgumentEncoder>\"24@0:8@\"<MTLBufferBinding>\"16"
- "@\"<MTLArgumentEncoder>\"24@0:8@\"NSArray\"16"
- "@\"<MTLBinaryArchive>\"32@0:8@\"MTLBinaryArchiveDescriptor\"16^@24"
- "@\"<MTLBuffer>\"32@0:8Q16Q24"
- "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
- "@\"<MTLBuffer>\"40@0:8r^v16Q24Q32"
- "@\"<MTLBuffer>\"48@0:8^v16Q24Q32@?<v@?^vQ>40"
- "@\"<MTLCommandBuffer>\""
- "@\"<MTLCommandQueue>\""
- "@\"<MTLCommandQueue>\"16@0:8"
- "@\"<MTLCommandQueue>\"24@0:8@\"MTLCommandQueueDescriptor\"16"
- "@\"<MTLCommandQueue>\"24@0:8Q16"
- "@\"<MTLComputePipelineState>\""
- "@\"<MTLComputePipelineState>\"32@0:8@\"<MTLFunction>\"16^@24"
- "@\"<MTLComputePipelineState>\"48@0:8@\"<MTLFunction>\"16Q24^@32^@40"
- "@\"<MTLComputePipelineState>\"48@0:8@\"MTLComputePipelineDescriptor\"16Q24^@32^@40"
- "@\"<MTLCounterSampleBuffer>\"32@0:8@\"MTLCounterSampleBufferDescriptor\"16^@24"
- "@\"<MTLDepthStencilState>\"24@0:8@\"MTLDepthStencilDescriptor\"16"
- "@\"<MTLDevice>\""
- "@\"<MTLDynamicLibrary>\"32@0:8@\"<MTLLibrary>\"16^@24"
- "@\"<MTLDynamicLibrary>\"32@0:8@\"NSURL\"16^@24"
- "@\"<MTLEvent>\"16@0:8"
- "@\"<MTLFence>\"16@0:8"
- "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
- "@\"<MTLFunctionHandle>\"24@0:8@\"<MTLFunction>\"16"
- "@\"<MTLHeap>\"24@0:8@\"MTLHeapDescriptor\"16"
- "@\"<MTLIOCommandQueue>\"32@0:8@\"MTLIOCommandQueueDescriptor\"16^@24"
- "@\"<MTLIOFileHandle>\"32@0:8@\"NSURL\"16^@24"
- "@\"<MTLIOFileHandle>\"40@0:8@\"NSURL\"16q24^@32"
- "@\"<MTLIndirectCommandBuffer>\"40@0:8@\"MTLIndirectCommandBufferDescriptor\"16Q24Q32"
- "@\"<MTLLibrary>\""
- "@\"<MTLLibrary>\"16@0:8"
- "@\"<MTLLibrary>\"32@0:8@\"MTLStitchedLibraryDescriptor\"16^@24"
- "@\"<MTLLibrary>\"32@0:8@\"NSBundle\"16^@24"
- "@\"<MTLLibrary>\"32@0:8@\"NSObject<OS_dispatch_data>\"16^@24"
- "@\"<MTLLibrary>\"32@0:8@\"NSString\"16^@24"
- "@\"<MTLLibrary>\"32@0:8@\"NSURL\"16^@24"
- "@\"<MTLLibrary>\"40@0:8@\"NSString\"16@\"MTLCompileOptions\"24^@32"
- "@\"<MTLLogState>\"32@0:8@\"MTLLogStateDescriptor\"16^@24"
- "@\"<MTLRasterizationRateMap>\"24@0:8@\"MTLRasterizationRateMapDescriptor\"16"
- "@\"<MTLRenderPipelineState>\"32@0:8@\"MTLRenderPipelineDescriptor\"16^@24"
- "@\"<MTLRenderPipelineState>\"48@0:8@\"MTLMeshRenderPipelineDescriptor\"16Q24^@32^@40"
- "@\"<MTLRenderPipelineState>\"48@0:8@\"MTLRenderPipelineDescriptor\"16Q24^@32^@40"
- "@\"<MTLRenderPipelineState>\"48@0:8@\"MTLTileRenderPipelineDescriptor\"16Q24^@32^@40"
- "@\"<MTLResidencySet>\"32@0:8@\"MTLResidencySetDescriptor\"16^@24"
- "@\"<MTLSamplerState>\"24@0:8@\"MTLSamplerDescriptor\"16"
- "@\"<MTLSharedEvent>\"16@0:8"
- "@\"<MTLSharedEvent>\"24@0:8@\"MTLSharedEventHandle\"16"
- "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
- "@\"<MTLTexture>\"24@0:8@\"MTLSharedTextureHandle\"16"
- "@\"<MTLTexture>\"24@0:8@\"MTLTextureDescriptor\"16"
- "@\"<MTLTexture>\"40@0:8@\"MTLTextureDescriptor\"16^{__IOSurface=}24Q32"
- "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
- "@\"MTLArchitecture\"16@0:8"
- "@\"NSArray\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"_MRCMetalContext\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@32@0:8Q16Q24"
- "@32@0:8^{__CVBuffer=}16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16^{__IOSurface=}24Q32"
- "@40@0:8@16q24^@32"
- "@40@0:8Q16Q24q32"
- "@40@0:8r^v16Q24Q32"
- "@48@0:8@16Q24^@32^@40"
- "@48@0:8^v16Q24Q32@?40"
- "@72@0:8^{__IOSurface=}16Q24Q32Q40Q48Q56^@64"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8q16"
- "BYTE"
- "ECI"
- "GPUEndTime"
- "GPUStartTime"
- "HANZI"
- "KANJI"
- "MTLDevice"
- "NSObject"
- "NUMERIC"
- "Q16@0:8"
- "Q24@0:8Q16"
- "Q24@0:8q16"
- "T#,R"
- "T@\"<MTLCommandBuffer>\",R,N,V_currentCommandBuffer"
- "T@\"<MTLCommandQueue>\",R,N,V_commandQueue"
- "T@\"<MTLDevice>\",R,N,V_device"
- "T@\"<MTLLibrary>\",R,N,V_library"
- "T@\"MTLArchitecture\",R"
- "T@\"NSArray\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TB,R"
- "TB,R,GareBarycentricCoordsSupported"
- "TB,R,GareProgrammableSamplePositionsSupported"
- "TB,R,GareRasterOrderGroupsSupported"
- "TB,R,GisDepth24Stencil8PixelFormatSupported"
- "TB,R,GisHeadless"
- "TB,R,GisLowPower"
- "TB,R,GisRemovable"
- "TQ,R"
- "T{?=QQQ},R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_MRCBase_DummyClass___"
- "_MRCMetalContext"
- "_MRCMetalHybridBinarizer"
- "__MRCCFType"
- "__MRCCFTypeWithRedactedDescription"
- "_calcuateBlackPointsPipelineState"
- "_cfTypeID"
- "_commandQueue"
- "_currentCommandBuffer"
- "_device"
- "_fixBlackPointsPipelineState"
- "_isDeallocating"
- "_library"
- "_metalContext"
- "_thresholdPipelineState"
- "_tryRetain"
- "accelerationStructureSizesWithDescriptor:"
- "architecture"
- "areBarycentricCoordsSupported"
- "areProgrammableSamplePositionsSupported"
- "areRasterOrderGroupsSupported"
- "argumentBuffersSupport"
- "automaticallyNotifiesObserversForKey:"
- "autorelease"
- "barycentricCoordsSupported"
- "beginCommandBuffer"
- "beginCommandBufferWithError:"
- "bundleForClass:"
- "bundleURL"
- "bundleWithURL:"
- "class"
- "commandBuffer"
- "commandQueue"
- "commit"
- "commitCommandBuffer"
- "commitCommandBufferShouldWaitUntilCompleted:"
- "computeCommandEncoder"
- "conformsToProtocol:"
- "convertSparsePixelRegions:toTileRegions:withTileSize:alignmentMode:numRegions:"
- "convertSparseTileRegions:toPixelRegions:withTileSize:numRegions:"
- "copy"
- "counterSets"
- "currentAllocatedSize"
- "currentCommandBuffer"
- "debugDescription"
- "defaultManager"
- "depth24Stencil8PixelFormatSupported"
- "description"
- "device"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "doesNotRecognizeSelector:"
- "endEncoding"
- "environment"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileURLWithPath:"
- "functionHandleWithBinaryFunction:"
- "functionHandleWithFunction:"
- "getBytes:bytesPerRow:fromRegion:mipmapLevel:"
- "getDefaultSamplePositions:count:"
- "hasUnifiedMemory"
- "hash"
- "headless"
- "heapAccelerationStructureSizeAndAlignWithDescriptor:"
- "heapAccelerationStructureSizeAndAlignWithSize:"
- "heapBufferSizeAndAlignWithLength:options:"
- "heapTextureSizeAndAlignWithDescriptor:"
- "init"
- "initWithDevice:libraryURL:error:"
- "initWithMetalContext:error:"
- "initWithSuiteName:"
- "isDepth24Stencil8PixelFormatSupported"
- "isEqual:"
- "isHeadless"
- "isKindOfClass:"
- "isLowPower"
- "isMemberOfClass:"
- "isProxy"
- "isRemovable"
- "length"
- "library"
- "lowPower"
- "malloc_create_zone"
- "maxArgumentBufferSamplerCount"
- "maxBufferLength"
- "maxThreadgroupMemoryLength"
- "maxThreadsPerThreadgroup"
- "maxTotalThreadsPerThreadgroup"
- "maximumConcurrentCompilationTaskCount"
- "metalDevice"
- "minimumLinearTextureAlignmentForPixelFormat:"
- "minimumTextureBufferAlignmentForPixelFormat:"
- "name"
- "newAccelerationStructureWithDescriptor:"
- "newAccelerationStructureWithSize:"
- "newArchiveWithURL:error:"
- "newArgumentEncoderWithArguments:"
- "newArgumentEncoderWithBufferBinding:"
- "newArgumentTableWithDescriptor:error:"
- "newBinaryArchiveWithDescriptor:error:"
- "newBufferWithBytes:length:options:"
- "newBufferWithBytesNoCopy:length:options:deallocator:"
- "newBufferWithLength:options:"
- "newBufferWithLength:options:placementSparsePageSize:"
- "newCommandAllocator"
- "newCommandAllocatorWithDescriptor:error:"
- "newCommandBuffer"
- "newCommandQueue"
- "newCommandQueueWithDescriptor:"
- "newCommandQueueWithMaxCommandBufferCount:"
- "newCompilerWithDescriptor:error:"
- "newComputePipelineStateWithDescriptor:options:completionHandler:"
- "newComputePipelineStateWithDescriptor:options:reflection:error:"
- "newComputePipelineStateWithFunction:completionHandler:"
- "newComputePipelineStateWithFunction:error:"
- "newComputePipelineStateWithFunction:options:completionHandler:"
- "newComputePipelineStateWithFunction:options:reflection:error:"
- "newComputePipelineStateWithFunctionName:constantValues:error:"
- "newCounterHeapWithDescriptor:error:"
- "newCounterSampleBufferWithDescriptor:error:"
- "newDefaultLibrary"
- "newDefaultLibraryWithBundle:error:"
- "newDepthStencilStateWithDescriptor:"
- "newDynamicLibrary:error:"
- "newDynamicLibraryWithURL:error:"
- "newEvent"
- "newFence"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:error:"
- "newHeapWithDescriptor:"
- "newIOCommandQueueWithDescriptor:error:"
- "newIOFileHandleWithURL:compressionMethod:error:"
- "newIOFileHandleWithURL:error:"
- "newIOHandleWithURL:compressionMethod:error:"
- "newIOHandleWithURL:error:"
- "newIndirectCommandBufferWithDescriptor:maxCommandCount:options:"
- "newLibraryWithData:error:"
- "newLibraryWithFile:error:"
- "newLibraryWithSource:options:completionHandler:"
- "newLibraryWithSource:options:error:"
- "newLibraryWithStitchedDescriptor:completionHandler:"
- "newLibraryWithStitchedDescriptor:error:"
- "newLibraryWithURL:error:"
- "newLogStateWithDescriptor:error:"
- "newMTL4CommandQueue"
- "newMTL4CommandQueueWithDescriptor:error:"
- "newPipelineDataSetSerializerWithDescriptor:"
- "newRasterizationRateMapWithDescriptor:"
- "newRenderPipelineStateWithDescriptor:completionHandler:"
- "newRenderPipelineStateWithDescriptor:error:"
- "newRenderPipelineStateWithDescriptor:options:completionHandler:"
- "newRenderPipelineStateWithDescriptor:options:reflection:error:"
- "newRenderPipelineStateWithMeshDescriptor:options:completionHandler:"
- "newRenderPipelineStateWithMeshDescriptor:options:reflection:error:"
- "newRenderPipelineStateWithTileDescriptor:options:completionHandler:"
- "newRenderPipelineStateWithTileDescriptor:options:reflection:error:"
- "newResidencySetWithDescriptor:error:"
- "newSamplerStateWithDescriptor:"
- "newSharedEvent"
- "newSharedEventWithHandle:"
- "newSharedTextureWithDescriptor:"
- "newSharedTextureWithHandle:"
- "newTensorWithDescriptor:error:"
- "newTextureByBinarizingPixelBuffer:error:"
- "newTextureByBindingIOSurface:pixelFormat:width:height:usage:plane:error:"
- "newTextureViewPoolWithDescriptor:error:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "objectForKey:"
- "pathForResource:ofType:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "programmableSamplePositionsSupported"
- "queryTimestampFrequency"
- "rasterOrderGroupsSupported"
- "readWriteTextureSupport"
- "recommendedMaxWorkingSetSize"
- "redactedDescription"
- "registryID"
- "release"
- "removable"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sampleTimestamps:gpuTimestamp:"
- "self"
- "setBackgroundGPUPriority:"
- "setComputePipelineState:"
- "setGPUPriority:"
- "setTexture:atIndex:"
- "setUsage:"
- "sizeOfCounterHeapEntry:"
- "sparseTileSizeInBytes"
- "sparseTileSizeInBytesForSparsePageSize:"
- "sparseTileSizeWithTextureType:pixelFormat:sampleCount:"
- "sparseTileSizeWithTextureType:pixelFormat:sampleCount:sparsePageSize:"
- "standardUserDefaults"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "supports32BitFloatFiltering"
- "supports32BitMSAA"
- "supportsBCTextureCompression"
- "supportsCounterSampling:"
- "supportsDynamicLibraries"
- "supportsFamily:"
- "supportsFeatureSet:"
- "supportsFunctionPointers"
- "supportsFunctionPointersFromRender"
- "supportsPlacementSparse"
- "supportsPrimitiveMotionBlur"
- "supportsPullModelInterpolation"
- "supportsQueryTextureLOD"
- "supportsRasterizationRateMapWithLayerCount:"
- "supportsRaytracing"
- "supportsRaytracingFromRender"
- "supportsRenderDynamicLibraries"
- "supportsShaderBarycentricCoordinates"
- "supportsTextureSampleCount:"
- "supportsVertexAmplificationCount:"
- "tensorSizeAndAlignWithDescriptor:"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "threadExecutionWidth"
- "unspecified (0x%x)"
- "v16@0:8"
- "v20@0:8B16"
- "v32@0:8@\"<MTLFunction>\"16@?<v@?@\"<MTLComputePipelineState>\"@\"NSError\">24"
- "v32@0:8@\"MTLRenderPipelineDescriptor\"16@?<v@?@\"<MTLRenderPipelineState>\"@\"NSError\">24"
- "v32@0:8@\"MTLStitchedLibraryDescriptor\"16@?<v@?@\"<MTLLibrary>\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8^Q16^Q24"
- "v32@0:8^{?=ff}16Q24"
- "v40@0:8@\"<MTLFunction>\"16Q24@?<v@?@\"<MTLComputePipelineState>\"@\"MTLComputePipelineReflection\"@\"NSError\">32"
- "v40@0:8@\"MTLComputePipelineDescriptor\"16Q24@?<v@?@\"<MTLComputePipelineState>\"@\"MTLComputePipelineReflection\"@\"NSError\">32"
- "v40@0:8@\"MTLMeshRenderPipelineDescriptor\"16Q24@?<v@?@\"<MTLRenderPipelineState>\"@\"MTLRenderPipelineReflection\"@\"NSError\">32"
- "v40@0:8@\"MTLRenderPipelineDescriptor\"16Q24@?<v@?@\"<MTLRenderPipelineState>\"@\"MTLRenderPipelineReflection\"@\"NSError\">32"
- "v40@0:8@\"MTLTileRenderPipelineDescriptor\"16Q24@?<v@?@\"<MTLRenderPipelineState>\"@\"MTLRenderPipelineReflection\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"MTLCompileOptions\"24@?<v@?@\"<MTLLibrary>\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v64@0:8r^{?={?=QQQ}{?=QQQ}}16^{?={?=QQQ}{?=QQQ}}24{?=QQQ}32Q56"
- "v72@0:8r^{?={?=QQQ}{?=QQQ}}16^{?={?=QQQ}{?=QQQ}}24{?=QQQ}32Q56Q64"
- "waitUntilCompleted"
- "zone"
- "{?=QQQ}16@0:8"
- "{?=QQQ}24@0:8@\"MTLAccelerationStructureDescriptor\"16"
- "{?=QQQ}24@0:8@16"
- "{?=QQQ}40@0:8Q16Q24Q32"
- "{?=QQQ}48@0:8Q16Q24Q32q40"
- "{?=QQ}24@0:8@\"MTLAccelerationStructureDescriptor\"16"
- "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"
- "{?=QQ}24@0:8@\"MTLTextureDescriptor\"16"
- "{?=QQ}24@0:8@16"
- "{?=QQ}24@0:8Q16"
- "{?=QQ}32@0:8Q16Q24"

```
