## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-104.5.0.0.0
-  __TEXT.__text: 0x211d4
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x42e4
-  __TEXT.__cstring: 0x4c3d
-  __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x398
-  __TEXT.__oslogstring: 0x82f
-  __TEXT.__unwind_info: 0xac0
-  __TEXT.__objc_classname: 0x556
-  __TEXT.__objc_methname: 0xa36a
-  __TEXT.__objc_methtype: 0x5884
-  __TEXT.__objc_stubs: 0x29c0
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x630
-  __DATA_CONST.__objc_classlist: 0x138
+124.1.0.0.0
+  __TEXT.__text: 0x28a7c
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x4cbc
+  __TEXT.__cstring: 0x5f7f
+  __TEXT.__const: 0x208
+  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__oslogstring: 0x8ae
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__objc_classname: 0x635
+  __TEXT.__objc_methname: 0xb4a9
+  __TEXT.__objc_methtype: 0x6ae0
+  __TEXT.__objc_stubs: 0x2fc0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_selrefs: 0x2798
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__objc_superrefs: 0x130
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
-  __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x6ea8
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x318
-  __DATA.__data: 0x720
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x690
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0x7cb0
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__data: 0x7e0
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D0A23B1-D8EA-3CE8-BA69-1CE6E0FBE205
-  Functions: 1154
-  Symbols:   3546
-  CStrings:  2603
+  UUID: 71DDBDE0-8A47-3181-BC29-3FAD25F59B86
+  Functions: 1420
+  Symbols:   4245
+  CStrings:  2935
 
Symbols:
+ -[IOGPUMTLEvent _isSharedEvent]
+ -[IOGPUMTLEvent eventName]
+ -[IOGPUMetal4CommandAllocator allocatedSize]
+ -[IOGPUMetal4CommandAllocator dealloc]
+ -[IOGPUMetal4CommandAllocator getCommandBufferStorage:retainReferences:]
+ -[IOGPUMetal4CommandAllocator getGeneration]
+ -[IOGPUMetal4CommandAllocator initAllocatorWithDevice:]
+ -[IOGPUMetal4CommandAllocator initWithDevice:]
+ -[IOGPUMetal4CommandAllocator initWithDevice:descriptor:]
+ -[IOGPUMetal4CommandAllocator initWithDeviceAndAliasToDevicePools:]
+ -[IOGPUMetal4CommandAllocator reset]
+ -[IOGPUMetal4CommandAllocator returnCommandBufferStorage:commandAllocatorGeneration:]
+ -[IOGPUMetal4CommandAllocator setHwResourcePool:count:]
+ -[IOGPUMetal4CommandAllocator setHwResourcePool:count:].cold.1
+ -[IOGPUMetal4CommandAllocator setHwResourcePool:count:].cold.2
+ -[IOGPUMetal4CommandAllocator setHwResourcePool:count:].cold.3
+ -[IOGPUMetal4CommandBuffer _reserveKernelCommandBufferSpace:]
+ -[IOGPUMetal4CommandBuffer _reserveKernelCommandBufferSpace:].cold.1
+ -[IOGPUMetal4CommandBuffer _reserveKernelCommandBufferSpace:].cold.2
+ -[IOGPUMetal4CommandBuffer akPrivateResourceList]
+ -[IOGPUMetal4CommandBuffer akPrivateResourceList].cold.1
+ -[IOGPUMetal4CommandBuffer akResourceList]
+ -[IOGPUMetal4CommandBuffer akResourceList].cold.1
+ -[IOGPUMetal4CommandBuffer allocCommandBufferResourceAtIndex:]
+ -[IOGPUMetal4CommandBuffer allocDebugBuffer]
+ -[IOGPUMetal4CommandBuffer allocDebugBuffer].cold.1
+ -[IOGPUMetal4CommandBuffer allocateSidebandBuffer:]
+ -[IOGPUMetal4CommandBuffer allocateSidebandBuffer:].cold.1
+ -[IOGPUMetal4CommandBuffer beginCommandBufferWithAllocator:]
+ -[IOGPUMetal4CommandBuffer beginCommandBufferWithAllocator:options:]
+ -[IOGPUMetal4CommandBuffer beginIOGPUCommandBufferWithAllocator:options:]
+ -[IOGPUMetal4CommandBuffer beginIOGPUCommandBufferWithAllocator:options:].cold.1
+ -[IOGPUMetal4CommandBuffer beginSegment:]
+ -[IOGPUMetal4CommandBuffer beginSegment:].cold.1
+ -[IOGPUMetal4CommandBuffer commandBufferStorage]
+ -[IOGPUMetal4CommandBuffer commitEncoder]
+ -[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:]
+ -[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:].cold.1
+ -[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:].cold.2
+ -[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:].cold.3
+ -[IOGPUMetal4CommandBuffer dealloc]
+ -[IOGPUMetal4CommandBuffer encodePostMappingWaitEvent:postMappingValue:timeout:]
+ -[IOGPUMetal4CommandBuffer encodeSignalEvent:value:]
+ -[IOGPUMetal4CommandBuffer encodeWaitForEvent:value:]
+ -[IOGPUMetal4CommandBuffer encodeWaitForEvent:value:timeout:]
+ -[IOGPUMetal4CommandBuffer endCommandBuffer]
+ -[IOGPUMetal4CommandBuffer endCommandBuffer].cold.1
+ -[IOGPUMetal4CommandBuffer endCurrentSegment]
+ -[IOGPUMetal4CommandBuffer endCurrentSegment].cold.1
+ -[IOGPUMetal4CommandBuffer fillCommandBufferArgs:]
+ -[IOGPUMetal4CommandBuffer fillCommandBufferArgs:].cold.1
+ -[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferPointer:end:]
+ -[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferPointer:end:].cold.1
+ -[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferStart:current:end:]
+ -[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferStart:current:end:].cold.1
+ -[IOGPUMetal4CommandBuffer getDebugBufferPointerStart:end:]
+ -[IOGPUMetal4CommandBuffer getDebugBufferPointerStart:end:].cold.1
+ -[IOGPUMetal4CommandBuffer getSegmentListPointerStart:current:end:]
+ -[IOGPUMetal4CommandBuffer getSegmentListPointerStart:current:end:].cold.1
+ -[IOGPUMetal4CommandBuffer growDebugBuffer:]
+ -[IOGPUMetal4CommandBuffer growDebugBuffer:].cold.1
+ -[IOGPUMetal4CommandBuffer growKernelCommandBuffer:]
+ -[IOGPUMetal4CommandBuffer growKernelCommandBuffer:].cold.1
+ -[IOGPUMetal4CommandBuffer growSegmentList]
+ -[IOGPUMetal4CommandBuffer growSegmentList].cold.1
+ -[IOGPUMetal4CommandBuffer growSidebandBuffer:]
+ -[IOGPUMetal4CommandBuffer growSidebandBuffer:].cold.1
+ -[IOGPUMetal4CommandBuffer initWithDevice:]
+ -[IOGPUMetal4CommandBuffer ioGPUResourceList]
+ -[IOGPUMetal4CommandBuffer ioGPUResourceList].cold.1
+ -[IOGPUMetal4CommandBuffer protectionOptions]
+ -[IOGPUMetal4CommandBuffer resetCommandBuffer]
+ -[IOGPUMetal4CommandBuffer resetCommandBuffer].cold.1
+ -[IOGPUMetal4CommandBuffer setCurrentKernelCommandBufferPointer:]
+ -[IOGPUMetal4CommandBuffer setCurrentKernelCommandBufferPointer:].cold.1
+ -[IOGPUMetal4CommandBuffer setCurrentSegmentListPointer:]
+ -[IOGPUMetal4CommandBuffer setCurrentSegmentListPointer:].cold.1
+ -[IOGPUMetal4CommandBuffer setProtectionOptions:]
+ -[IOGPUMetal4CommandBuffer setProtectionOptions:].cold.1
+ -[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:]
+ -[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:].cold.1
+ -[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:].cold.2
+ -[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:].cold.3
+ -[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:].cold.4
+ -[IOGPUMetal4CommandBuffer useInternalResidencySet:]
+ -[IOGPUMetal4CommandBuffer useInternalResidencySet:].cold.1
+ -[IOGPUMetal4CommandBuffer useInternalResidencySets:count:]
+ -[IOGPUMetal4CommandBuffer useInternalResidencySets:count:].cold.1
+ -[IOGPUMetal4CommandBuffer useResidencySet:]
+ -[IOGPUMetal4CommandBuffer useResidencySet:].cold.1
+ -[IOGPUMetal4CommandBuffer useResidencySets:count:]
+ -[IOGPUMetal4CommandBuffer useResidencySets:count:].cold.1
+ -[IOGPUMetal4CommandQueue _commit:count:commitFeedback:]
+ -[IOGPUMetal4CommandQueue _commit:count:commitFeedback:].cold.1
+ -[IOGPUMetal4CommandQueue _commit:count:commitFeedback:].cold.2
+ -[IOGPUMetal4CommandQueue addInternalResidencySet:]
+ -[IOGPUMetal4CommandQueue addInternalResidencySets:count:]
+ -[IOGPUMetal4CommandQueue addResidencySet:]
+ -[IOGPUMetal4CommandQueue addResidencySets:count:]
+ -[IOGPUMetal4CommandQueue allocateMappingCommandBuffer]
+ -[IOGPUMetal4CommandQueue allocateMappingCommandBuffer].cold.1
+ -[IOGPUMetal4CommandQueue commandAllocator]
+ -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]
+ -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:].cold.1
+ -[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:]
+ -[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:].cold.1
+ -[IOGPUMetal4CommandQueue commitMappingCommandBuffer]
+ -[IOGPUMetal4CommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:]
+ -[IOGPUMetal4CommandQueue dealloc]
+ -[IOGPUMetal4CommandQueue endTier1MappingCommands]
+ -[IOGPUMetal4CommandQueue initIOGPUMTL4CommandQueue:descriptor:args:argsSize:]
+ -[IOGPUMetal4CommandQueue initIOGPUMTL4CommandQueue:descriptor:args:argsSize:].cold.1
+ -[IOGPUMetal4CommandQueue initIOGPUMTL4CommandQueue:descriptor:args:argsSize:].cold.2
+ -[IOGPUMetal4CommandQueue initWithDevice:]
+ -[IOGPUMetal4CommandQueue initWithDevice:descriptor:]
+ -[IOGPUMetal4CommandQueue initWithDevice:descriptor:args:argsSize:]
+ -[IOGPUMetal4CommandQueue preCommit:count:options:]
+ -[IOGPUMetal4CommandQueue removeInternalResidencySet:]
+ -[IOGPUMetal4CommandQueue removeInternalResidencySets:count:]
+ -[IOGPUMetal4CommandQueue removeResidencySet:]
+ -[IOGPUMetal4CommandQueue removeResidencySets:count:]
+ -[IOGPUMetal4CommandQueue signalEvent:value:]
+ -[IOGPUMetal4CommandQueue supportsBackgroundAppRole]
+ -[IOGPUMetal4CommandQueue updateBufferMappings:heap:operations:count:]
+ -[IOGPUMetal4CommandQueue waitForEvent:value:]
+ -[IOGPUMetal4CommandQueue waitForEvent:value:timeout:]
+ -[IOGPUMetal4ComputeCommandEncoder dealloc]
+ -[IOGPUMetal4ComputeCommandEncoder endEncoding]
+ -[IOGPUMetal4ComputeCommandEncoder getType]
+ -[IOGPUMetal4ComputeCommandEncoder initWithCommandAllocator:]
+ -[IOGPUMetal4ComputeCommandEncoder popDebugGroup]
+ -[IOGPUMetal4ComputeCommandEncoder pushDebugGroup:]
+ -[IOGPUMetal4ComputeCommandEncoder setLabel:]
+ -[IOGPUMetal4MachineLearningCommandEncoder dealloc]
+ -[IOGPUMetal4MachineLearningCommandEncoder endEncoding]
+ -[IOGPUMetal4MachineLearningCommandEncoder getType]
+ -[IOGPUMetal4MachineLearningCommandEncoder initWithCommandBuffer:allocator:]
+ -[IOGPUMetal4MachineLearningCommandEncoder popDebugGroup]
+ -[IOGPUMetal4MachineLearningCommandEncoder pushDebugGroup:]
+ -[IOGPUMetal4MachineLearningCommandEncoder setLabel:]
+ -[IOGPUMetal4RenderCommandEncoder dealloc]
+ -[IOGPUMetal4RenderCommandEncoder endEncoding]
+ -[IOGPUMetal4RenderCommandEncoder getType]
+ -[IOGPUMetal4RenderCommandEncoder initWithCommandAllocator:]
+ -[IOGPUMetal4RenderCommandEncoder popDebugGroup]
+ -[IOGPUMetal4RenderCommandEncoder pushDebugGroup:]
+ -[IOGPUMetal4RenderCommandEncoder setLabel:]
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:args:argsSize:deallocator:]
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:]
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:].cold.1
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:].cold.2
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:].cold.3
+ -[IOGPUMetalBuffer placementSparsePageSize]
+ -[IOGPUMetalCommandBuffer encodeWaitForEvent:value:].cold.1
+ -[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:]
+ -[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:].cold.1
+ -[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:].cold.2
+ -[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:].cold.3
+ -[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:].cold.4
+ -[IOGPUMetalCommandQueue supportsBackgroundAppRole]
+ -[IOGPUMetalDevice launchMappingThread]
+ -[IOGPUMetalDevice newDevicePoolAliasedCommandAllocator]
+ -[IOGPUMetalDevice supportsBackgroundAppRole]
+ -[IOGPUMetalDeviceShmemPool allocatedSize]
+ -[IOGPUMetalDeviceShmemPool dealloc].cold.1
+ -[IOGPUMetalHeap maxCompatiblePlacementSparsePageSize]
+ -[IOGPUMetalResource metadataVirtualAddress]
+ -[IOGPUMetalResourcePool allocatedSize]
+ -[IOGPUMetalResourcePool dealloc].cold.1
+ -[IOGPUMetalTensor buffer]
+ -[IOGPUMetalTensor dataType]
+ -[IOGPUMetalTensor dealloc]
+ -[IOGPUMetalTensor dimensions]
+ -[IOGPUMetalTensor getBytes:strides:fromSlice:]
+ -[IOGPUMetalTensor gpuResourceID]
+ -[IOGPUMetalTensor initWithBuffer:]
+ -[IOGPUMetalTensor internalMTLBuffer]
+ -[IOGPUMetalTensor iosurface]
+ -[IOGPUMetalTensor isTensorViewableWithReshapedDescriptor:]
+ -[IOGPUMetalTensor newTensorViewWithReshapedDescriptor:error:]
+ -[IOGPUMetalTensor newTensorViewWithSlice:error:]
+ -[IOGPUMetalTensor offset]
+ -[IOGPUMetalTensor parentTensor]
+ -[IOGPUMetalTensor plane]
+ -[IOGPUMetalTensor replaceSlice:withBytes:strides:]
+ -[IOGPUMetalTensor resourceIndex]
+ -[IOGPUMetalTensor strides]
+ -[IOGPUMetalTensor usage]
+ -[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:].cold.7
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:args:argsSize:]
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:]
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:].cold.1
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:].cold.2
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:].cold.3
+ -[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:].cold.4
+ -[IOGPUMetalTexture initWithDevice:descriptor:sysMemPointer:sysMemSize:sysMemLength:sysMemRowBytes:args:argsSize:deallocator:].cold.3
+ -[IOGPUMetalTexture placementSparsePageSize]
+ -[NSError(IOGPUMetalErrors) initWithIOGPUError:MTL4QueueError:]
+ -[NSError(IOGPUMetalErrors) initWithIOGPUError:MTL4QueueError:].cold.1
+ -[_IOGPUMetalMTLLateEvalEvent waitUntilSignaledValue:timeoutMS:]
+ -[_MTLSharedEvent(IOGPUFamilySupport) _isSharedEvent]
+ GCC_except_table12
+ GCC_except_table17
+ GCC_except_table22
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table8
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._aliasToDevice
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._busyQueue
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._busyQueueCount
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._commandBufferStoragePool
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._generation
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._lock
+ OBJC_IVAR_$_IOGPUMetal4CommandAllocator._storageCreateParams
+ OBJC_IVAR_$_IOGPUMetal4CommandBuffer._protectionOptions
+ OBJC_IVAR_$_IOGPUMetal4CommandBuffer._storage
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._commandAllocator
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._commandQueue
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._completionQueue
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._disableAsyncMapping
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._mappingCommandBuffer
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._mappingLock
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._postMappingEvent
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._postMappingValue
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._qosLevel
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._resourceGroups
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._resourceGroupsLock
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._tier1ResourceMapping
+ OBJC_IVAR_$_IOGPUMetalBuffer._placementSparsePageSize
+ OBJC_IVAR_$_IOGPUMetalHeap._device
+ OBJC_IVAR_$_IOGPUMetalHeap._size
+ OBJC_IVAR_$_IOGPUMetalTexture._placementSparsePageSize
+ OBJC_IVAR_$__MTL4CommandAllocator._device
+ OBJC_IVAR_$__MTL4CommandAllocator._globalTraceObjectID
+ OBJC_IVAR_$__MTL4CommandBuffer._commandAllocator
+ OBJC_IVAR_$__MTL4CommandBuffer._device
+ OBJC_IVAR_$__MTL4CommandBuffer._globalTraceObjectID
+ OBJC_IVAR_$__MTL4CommandEncoder._commandAllocator
+ OBJC_IVAR_$__MTL4CommandEncoder._device
+ OBJC_IVAR_$__MTL4CommandEncoder._globalTraceObjectID
+ OBJC_IVAR_$__MTL4CommandEncoder._labelTraceID
+ OBJC_IVAR_$__MTL4CommandQueue._device
+ OBJC_IVAR_$__MTL4CommandQueue._globalTraceObjectID
+ OBJC_IVAR_$__MTL4CommandQueue._lastCommittedCommandBuffer
+ OBJC_IVAR_$__MTL4CommandQueue._lastCommittedCommandBufferGeneration
+ OBJC_IVAR_$__MTL4CommandQueue._submissionQueue
+ _IOConnectTrap5
+ _IOGPUCommandQueueCreate.cold.1
+ _IOGPUCommandQueueCreate.cold.2
+ _IOGPUCommandQueueCreate.cold.3
+ _IOGPUCommandQueueCreate.cold.4
+ _IOGPUCommandQueueSignalMTLEvent
+ _IOGPUCommandQueueSignalMTLEvent.cold.1
+ _IOGPUCommandQueueSignalSharedEvent
+ _IOGPUCommandQueueSignalSharedEvent.cold.1
+ _IOGPUCommandQueueSupportsBackgroundAppRole
+ _IOGPUCommandQueueWaitMTLEvent
+ _IOGPUCommandQueueWaitMTLEvent.cold.1
+ _IOGPUCommandQueueWaitSharedEvent
+ _IOGPUCommandQueueWaitSharedEvent.cold.1
+ _IOGPUDeviceCreateWithOptions
+ _IOGPUDeviceCreateWithOptions.cold.1
+ _IOGPUDeviceCreateWithOptions.cold.2
+ _IOGPUDeviceCreateWithOptions.cold.3
+ _IOGPUDevicePerformMapping
+ _IOGPUMetal4CommandBufferStorageEndCommandBuffer
+ _IOGPUMetal4CommandBufferStorageFinalizeCommandBuffer
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.1
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.2
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.3
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.4
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.5
+ _IOGPUMetalCommandBufferStorageFinalizeResidencySetList.cold.6
+ _IOGPUMetalCommandBufferStorageMergeResidencySetList
+ _IOGPUMetalCommandBufferStorageMergeResidencySetList.cold.1
+ _IOGPUMetalCommandBufferStorageMergeResidencySetList.cold.2
+ _IOGPUMetalResidencySetListCreate
+ _IOGPUMetalResidencySetListCreate.cold.1
+ _IOGPUMetalResidencySetListDestroy
+ _IOGPUMetalResidencySetListDestroy.cold.1
+ _IOGPUMetalResidencySetListDuplicate
+ _IOGPUMetalResidencySetListDuplicate.cold.1
+ _IOGPUResourceGeMetadataBytes
+ _IOGPUResourceGetResourceType
+ _MTL4CommandQueueErrorDomain
+ _MTLTensorDomain
+ _OBJC_CLASS_$_IOGPUMetal4CommandAllocator
+ _OBJC_CLASS_$_IOGPUMetal4CommandBuffer
+ _OBJC_CLASS_$_IOGPUMetal4CommandQueue
+ _OBJC_CLASS_$_IOGPUMetal4ComputeCommandEncoder
+ _OBJC_CLASS_$_IOGPUMetal4MachineLearningCommandEncoder
+ _OBJC_CLASS_$_IOGPUMetal4RenderCommandEncoder
+ _OBJC_CLASS_$_IOGPUMetalTensor
+ _OBJC_CLASS_$_MTLTensorDescriptor
+ _OBJC_CLASS_$_MTLTensorExtents
+ _OBJC_CLASS_$__MTL4CommandAllocator
+ _OBJC_CLASS_$__MTL4CommandBuffer
+ _OBJC_CLASS_$__MTL4CommandQueue
+ _OBJC_CLASS_$__MTL4ComputeCommandEncoder
+ _OBJC_CLASS_$__MTL4MachineLearningCommandEncoder
+ _OBJC_CLASS_$__MTL4RenderCommandEncoder
+ _OBJC_IVAR_$_IOGPUMetalDevice._mappingQueue
+ _OBJC_IVAR_$_IOGPUMetalDeviceShmemPool._allocatedSize
+ _OBJC_IVAR_$_IOGPUMetalHeap._maxCompatiblePlacementSparsePageSize
+ _OBJC_IVAR_$_IOGPUMetalResourcePool._allocatedSize
+ _OBJC_IVAR_$_IOGPUMetalTensor._buffer
+ _OBJC_IVAR_$_IOGPUMetalTensor._parentTensor
+ _OBJC_METACLASS_$_IOGPUMetal4CommandAllocator
+ _OBJC_METACLASS_$_IOGPUMetal4CommandBuffer
+ _OBJC_METACLASS_$_IOGPUMetal4CommandQueue
+ _OBJC_METACLASS_$_IOGPUMetal4ComputeCommandEncoder
+ _OBJC_METACLASS_$_IOGPUMetal4MachineLearningCommandEncoder
+ _OBJC_METACLASS_$_IOGPUMetal4RenderCommandEncoder
+ _OBJC_METACLASS_$_IOGPUMetalTensor
+ _OBJC_METACLASS_$__MTL4CommandAllocator
+ _OBJC_METACLASS_$__MTL4CommandBuffer
+ _OBJC_METACLASS_$__MTL4CommandQueue
+ _OBJC_METACLASS_$__MTL4ComputeCommandEncoder
+ _OBJC_METACLASS_$__MTL4MachineLearningCommandEncoder
+ _OBJC_METACLASS_$__MTL4RenderCommandEncoder
+ __MTLIsInternalBuild
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4CommandAllocator
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4CommandBuffer
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4CommandQueue
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4ComputeCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4MachineLearningCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetal4RenderCommandEncoder
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetalTensor
+ __OBJC_$_INSTANCE_VARIABLES_IOGPUMetal4CommandAllocator
+ __OBJC_$_INSTANCE_VARIABLES_IOGPUMetal4CommandBuffer
+ __OBJC_$_INSTANCE_VARIABLES_IOGPUMetal4CommandQueue
+ __OBJC_$_INSTANCE_VARIABLES_IOGPUMetalTensor
+ __OBJC_$_PROP_LIST_IOGPUMetalTensor
+ __OBJC_$_PROP_LIST_MTLTensor
+ __OBJC_$_PROP_LIST_MTLTensorSPI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTensor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTensorSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTensor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTensorSPI
+ __OBJC_$_PROTOCOL_REFS_MTLTensor
+ __OBJC_$_PROTOCOL_REFS_MTLTensorSPI
+ __OBJC_CLASS_PROTOCOLS_$_IOGPUMetalTensor
+ __OBJC_CLASS_RO_$_IOGPUMetal4CommandAllocator
+ __OBJC_CLASS_RO_$_IOGPUMetal4CommandBuffer
+ __OBJC_CLASS_RO_$_IOGPUMetal4CommandQueue
+ __OBJC_CLASS_RO_$_IOGPUMetal4ComputeCommandEncoder
+ __OBJC_CLASS_RO_$_IOGPUMetal4MachineLearningCommandEncoder
+ __OBJC_CLASS_RO_$_IOGPUMetal4RenderCommandEncoder
+ __OBJC_CLASS_RO_$_IOGPUMetalTensor
+ __OBJC_LABEL_PROTOCOL_$_MTLTensor
+ __OBJC_LABEL_PROTOCOL_$_MTLTensorSPI
+ __OBJC_METACLASS_RO_$_IOGPUMetal4CommandAllocator
+ __OBJC_METACLASS_RO_$_IOGPUMetal4CommandBuffer
+ __OBJC_METACLASS_RO_$_IOGPUMetal4CommandQueue
+ __OBJC_METACLASS_RO_$_IOGPUMetal4ComputeCommandEncoder
+ __OBJC_METACLASS_RO_$_IOGPUMetal4MachineLearningCommandEncoder
+ __OBJC_METACLASS_RO_$_IOGPUMetal4RenderCommandEncoder
+ __OBJC_METACLASS_RO_$_IOGPUMetalTensor
+ __OBJC_PROTOCOL_$_MTLTensor
+ __OBJC_PROTOCOL_$_MTLTensorSPI
+ __ZL13_waitForEventP23IOGPUMetal4CommandQueuePU18objcproto8MTLEvent11objc_objectyjPP7NSError
+ __ZL17_addResidencySetsP23IOGPUMetal4CommandQueuePPU26objcproto15MTLResidencySet11objc_objectmm
+ __ZL20_removeResidencySetsP23IOGPUMetal4CommandQueuePPU26objcproto15MTLResidencySet11objc_objectmm
+ __ZL20_updateResidencySetsP23IOGPUMetal4CommandQueue
+ __ZL20_updateResidencySetsP23IOGPUMetal4CommandQueue.cold.1
+ __ZL20submitCommandBuffersPv
+ __ZL35_iogpuMetalCommandBufferStorageFreeP30IOGPUMetalCommandBufferStorage
+ __ZL35_iogpuMetalCommandBufferStorageFreeP30IOGPUMetalCommandBufferStorage.cold.1
+ __ZL35_iogpuMetalCommandBufferStorageFreeP30IOGPUMetalCommandBufferStorage.cold.2
+ __ZL37_IOGPUMetalResidencySetListInitializeR28__IOGPUMetalResidencySetListRK30IOGPUMetalCommandBufferStorage
+ __ZL37_IOGPUMetalResidencySetListInitializeR28__IOGPUMetalResidencySetListRK30IOGPUMetalCommandBufferStorage.cold.1
+ __ZL37_IOGPUMetalResidencySetListInitializeR28__IOGPUMetalResidencySetListRK30IOGPUMetalCommandBufferStorage.cold.2
+ __ZL37_IOGPUMetalResidencySetListInitializeR28__IOGPUMetalResidencySetListRK30IOGPUMetalCommandBufferStorage.cold.3
+ __ZL42_iogpuMetalCommandBufferStorageSetupShmemsP30IOGPUMetalCommandBufferStorageP42IOGPUMetalCommandBufferStorageCreateParams
+ __ZL45_mtlIOGPUCommandBufferStorageBeginSegmentListP30IOGPUMetalCommandBufferStorage
+ __ZL52_iogpuMetalCommandBufferStorageReleaseExtraResourcesP30IOGPUMetalCommandBufferStorage
+ __ZL54_iogpuMetalCommandBufferStorageReleaseCurrentResourcesP30IOGPUMetalCommandBufferStorage
+ __ZN28__IOGPUMetalResidencySetListaSERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE11__do_rehashILb0EEEvm
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE14__assign_multiINS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEEEEvT_SF_
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE15__emplace_multiIJRKjEEENS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEDpOT_
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE25__emplace_unique_key_argsIjJRKjEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIjPvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE27__node_insert_multi_performEPNS_11__hash_nodeIjPvEEPNS_16__hash_node_baseISB_EE
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE27__node_insert_multi_prepareEmRj
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE8__rehashILb0EEEvm
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE9push_backB8ne200100ERKs
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1326
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.cold.1
+ ___45-[IOGPUMetal4CommandQueue signalEvent:value:]_block_invoke
+ ___45-[IOGPUMetal4CommandQueue signalEvent:value:]_block_invoke_2
+ ___66-[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:]_block_invoke
+ ___77-[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:]_block_invoke
+ ___IOGPUDeviceCreateWithOptions_block_invoke
+ ___IOGPUMetal4CommandBufferStorageEndCommandBuffer_block_invoke
+ ____ZL13_waitForEventP23IOGPUMetal4CommandQueuePU18objcproto8MTLEvent11objc_objectyjPP7NSError_block_invoke
+ ____ZL13_waitForEventP23IOGPUMetal4CommandQueuePU18objcproto8MTLEvent11objc_objectyjPP7NSError_block_invoke_2
+ ____ZL20_updateResidencySetsP23IOGPUMetal4CommandQueue_block_invoke
+ ____ZL20_updateResidencySetsP23IOGPUMetal4CommandQueue_block_invoke_2
+ ____ZL20_updateResidencySetsP23IOGPUMetal4CommandQueue_block_invoke_2.cold.1
+ ____ZL20submitCommandBuffersPv_block_invoke
+ ____updateResidencySets_block_invoke_2
+ ____updateResidencySets_block_invoke_2.cold.1
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_52_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_60_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_60_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_60_e8_32r_e36_v24?0"IOGPUMetalResidencySet"8^B16lr32l8
+ ___block_descriptor_77_e8_32o40o48o56o_e17_v36?0Q8Q16I24Q28ls32l8s40l8s48l8s56l8
+ ___block_descriptor_tmp.5
+ ___block_descriptor_tmp.9
+ ___block_literal_global.7
+ ___cxa_end_catch
+ ___cxa_rethrow
+ _dispatch_async_f
+ _errorWithMessage
+ _launchMappingThread.onceToken
+ _objc_msgSend$_commit:count:commitFeedback:
+ _objc_msgSend$_isSharedEvent
+ _objc_msgSend$allocateMappingCommandBuffer
+ _objc_msgSend$beginCommandBufferWithAllocator:
+ _objc_msgSend$beginIOGPUCommandBufferWithAllocator:options:
+ _objc_msgSend$commandAllocator
+ _objc_msgSend$commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:
+ _objc_msgSend$commandBufferComplete:completionTime:error:executeHandlers:
+ _objc_msgSend$commandBufferStorage
+ _objc_msgSend$commitFillArgs:count:args:argsSize:commitFeedback:
+ _objc_msgSend$commitMappingCommandBuffer
+ _objc_msgSend$copyBufferMappingsFromBuffer:toBuffer:operations:count:
+ _objc_msgSend$dataType
+ _objc_msgSend$dimensions
+ _objc_msgSend$encodePostMappingWaitEvent:postMappingValue:timeout:
+ _objc_msgSend$endCommandBuffer
+ _objc_msgSend$endTier1MappingCommands
+ _objc_msgSend$eventName
+ _objc_msgSend$extentAtDimensionIndex:
+ _objc_msgSend$feedbackQueue
+ _objc_msgSend$fillCommandBufferArgs:
+ _objc_msgSend$getCommandBufferStorage:retainReferences:
+ _objc_msgSend$getGeneration
+ _objc_msgSend$getObjects:count:
+ _objc_msgSend$initAllocatorWithDevice:
+ _objc_msgSend$initIOGPUMTL4CommandQueue:descriptor:args:argsSize:
+ _objc_msgSend$initWithDevice:descriptor:args:argsSize:
+ _objc_msgSend$initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:
+ _objc_msgSend$initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:
+ _objc_msgSend$initWithDeviceAndAliasToDevicePools:
+ _objc_msgSend$initWithIOGPUError:MTL4QueueError:
+ _objc_msgSend$initWithRank:extents:
+ _objc_msgSend$isTensorViewableWithReshapedDescriptor:
+ _objc_msgSend$launchMappingThread
+ _objc_msgSend$maxCompatiblePlacementSparsePageSize
+ _objc_msgSend$newCommandBuffer
+ _objc_msgSend$newDevicePoolAliasedCommandAllocator
+ _objc_msgSend$newSharedEvent
+ _objc_msgSend$newTensorWithDescriptor:offset:error:
+ _objc_msgSend$placementSparsePageSize
+ _objc_msgSend$rank
+ _objc_msgSend$resetCommandBuffer
+ _objc_msgSend$returnCommandBufferStorage:commandAllocatorGeneration:
+ _objc_msgSend$setDataType:
+ _objc_msgSend$setDimensions:
+ _objc_msgSend$setStrides:
+ _objc_msgSend$setUsage:
+ _objc_msgSend$sparseTileSizeInBytesForSparsePageSize:
+ _objc_msgSend$strides
+ _objc_msgSend$updateBufferMappings:heap:operations:count:
+ _objc_msgSend$usage
+ _os_unfair_lock_assert_owner
+ _tensorDataTypeToString
- -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:].cold.1
- -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:].cold.2
- -[IOGPUMetalCommandQueue initWithDevice:descriptor:].cold.1
- -[IOGPUMetalCommandQueue initWithDevice:descriptor:].cold.2
- -[NSError(IOGPUMetalErrors) initWithIOGPUError:]
- GCC_except_table16
- GCC_except_table21
- GCC_except_table35
- GCC_except_table54
- GCC_except_table6
- GCC_except_table9
- _IOGPUCommandQueueCreateWithQoS
- _IOGPUCommandQueueCreateWithQoS.cold.1
- _IOGPUCommandQueueCreateWithQoS.cold.2
- _IOGPUCommandQueueCreateWithQoS.cold.3
- _IOGPUCommandQueueCreateWithQoS.cold.4
- _IOGPUDeviceCreateWithAPIProperty
- _IOGPUDeviceCreateWithAPIProperty.cold.1
- _IOGPUDeviceCreateWithAPIProperty.cold.2
- _IOGPUDeviceCreateWithAPIProperty.cold.3
- _OBJC_IVAR_$_IOGPUMetalHeap._device
- _OBJC_IVAR_$_IOGPUMetalHeap._size
- __ZNKSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___52-[IOGPUMetalCommandQueue initWithDevice:descriptor:]_block_invoke
- ___IOGPUDeviceCreateWithAPIProperty_block_invoke
- ___block_descriptor_48_e8_32r_e36_v24?0"IOGPUMetalResidencySet"8^B16lr32l8
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.8
- ___block_literal_global.6
- __iogpuMetalCommandBufferStorageFree
- __iogpuMetalCommandBufferStorageFree.cold.1
- __iogpuMetalCommandBufferStorageFree.cold.2
- __iogpuMetalCommandBufferStorageReleaseCurrentResources
- __iogpuMetalCommandBufferStorageReleaseExtraResources
- __iogpuMetalCommandBufferStorageSetupShmems
- __mtlIOGPUCommandBufferStorageBeginSegmentList
- _objc_msgSend$encodeWaitForEvent:value:timeout:
- _objc_msgSend$initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:
- _objc_msgSend$initWithIOGPUError:
CStrings:
+ "%s Failed to malloc for commit"
+ "-[IOGPUMetal4CommandAllocator setHwResourcePool:count:]"
+ "-[IOGPUMetal4CommandBuffer _reserveKernelCommandBufferSpace:]"
+ "-[IOGPUMetal4CommandBuffer akPrivateResourceList]"
+ "-[IOGPUMetal4CommandBuffer akResourceList]"
+ "-[IOGPUMetal4CommandBuffer allocDebugBuffer]"
+ "-[IOGPUMetal4CommandBuffer allocateSidebandBuffer:]"
+ "-[IOGPUMetal4CommandBuffer beginIOGPUCommandBufferWithAllocator:options:]"
+ "-[IOGPUMetal4CommandBuffer beginSegment:]"
+ "-[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:]"
+ "-[IOGPUMetal4CommandBuffer endCommandBuffer]"
+ "-[IOGPUMetal4CommandBuffer endCurrentSegment]"
+ "-[IOGPUMetal4CommandBuffer fillCommandBufferArgs:]"
+ "-[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferPointer:end:]"
+ "-[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferStart:current:end:]"
+ "-[IOGPUMetal4CommandBuffer getDebugBufferPointerStart:end:]"
+ "-[IOGPUMetal4CommandBuffer getSegmentListPointerStart:current:end:]"
+ "-[IOGPUMetal4CommandBuffer growDebugBuffer:]"
+ "-[IOGPUMetal4CommandBuffer growKernelCommandBuffer:]"
+ "-[IOGPUMetal4CommandBuffer growSegmentList]"
+ "-[IOGPUMetal4CommandBuffer growSidebandBuffer:]"
+ "-[IOGPUMetal4CommandBuffer ioGPUResourceList]"
+ "-[IOGPUMetal4CommandBuffer resetCommandBuffer]"
+ "-[IOGPUMetal4CommandBuffer setCurrentKernelCommandBufferPointer:]"
+ "-[IOGPUMetal4CommandBuffer setCurrentSegmentListPointer:]"
+ "-[IOGPUMetal4CommandBuffer setProtectionOptions:]"
+ "-[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:]"
+ "-[IOGPUMetal4CommandBuffer useInternalResidencySet:]"
+ "-[IOGPUMetal4CommandBuffer useInternalResidencySets:count:]"
+ "-[IOGPUMetal4CommandBuffer useResidencySet:]"
+ "-[IOGPUMetal4CommandBuffer useResidencySets:count:]"
+ "-[IOGPUMetal4CommandQueue _commit:count:commitFeedback:]"
+ "-[IOGPUMetal4CommandQueue allocateMappingCommandBuffer]"
+ "-[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]"
+ "-[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:]"
+ "-[IOGPUMetal4CommandQueue initIOGPUMTL4CommandQueue:descriptor:args:argsSize:]"
+ "-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:]"
+ "-[IOGPUMetalCommandBuffer encodeWaitForEvent:value:]"
+ "-[IOGPUMetalCommandQueue initWithDevice:descriptor:args:argsSize:]"
+ "-[IOGPUMetalDeviceShmemPool dealloc]"
+ "-[IOGPUMetalResourcePool dealloc]"
+ "-[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:]"
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
+ "@\"<MTLBuffer>\""
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTLFunction>\"16"
+ "@\"<MTLFunctionHandle>\"32@0:8@\"<MTLFunction>\"16Q24"
+ "@\"<MTLLibrary>\"40@0:8@\"NSURL\"16@\"NSString\"24^@32"
+ "@\"<MTLSharedEventSPI>\""
+ "@\"<MTLTensor>\""
+ "@\"<MTLTensor>\"16@0:8"
+ "@\"<MTLTensor>\"24@0:8{MTLResourceID=Q}16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTensor>\"40@0:8{MTLTensorSlice=@@}16^@32"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@\"IOGPUMetal4CommandAllocator\""
+ "@\"IOGPUMetal4CommandBuffer\""
+ "@\"MTLTensorExtents\"16@0:8"
+ "@104@0:8@16^v24Q32I40Q44Q52Q60Q68q76^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}84I92@?96"
+ "@112@0:8@16^v24Q32I40Q44Q52Q60Q68q76Q84^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}92I100@?104"
+ "@24@0:8{MTLResourceID=Q}16"
+ "@28@0:8q16B24"
+ "@40@0:8Q16Q24q32"
+ "@40@0:8r^@16Q24@32"
+ "@40@0:8{MTLTensorSlice=@@}16^@32"
+ "@44@0:8@16@24^{IOGPUDeviceNewCommandQueueArgs=[1024c]iCC[2C]}32I40"
+ "@44@0:8@16Q24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}32I40"
+ "@44@0:8@16^{__IOSurface=}24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}32I40"
+ "@48@0:8@16@24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}32Q40"
+ "@52@0:8@16#24r^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}32I40@44"
+ "@52@0:8@16Q24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}40I48"
+ "@52@0:8@16^{__IOSurface=}24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}40I48"
+ "@60@0:8@16@24^{__IOSurface=}32I40I44^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}48I56"
+ "@60@0:8@16Q24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}40I48@52"
+ "@60@0:8@16s24s28Q32Q40^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}48I56"
+ "@68@0:8@16@24Q32q40Q48^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}56I64"
+ "@68@0:8@16s24s28Q32Q40^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}48I56Q60"
+ "@76@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72"
+ "@76@0:8@16@24Q32q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72"
+ "@76@0:8@16^{IOGPUAddressRange=QQ}24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72"
+ "@80@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72B76"
+ "@84@0:8@16@24^v32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72@?76"
+ "@84@0:8@16^v24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64I72@?76"
+ "@88@0:8@16^v24Q32I40Q44Q52Q60^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}68I76@?80"
+ "@92@0:8@16s24s28Q32Q40@48Q56Q64Q72^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}80I88"
+ "@96@0:8@16^v24Q32I40Q44Q52Q60Q68^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}76I84@?88"
+ "B24@0:8@\"MTLTensorDescriptor\"16"
+ "BackgroundAppRole kr = 0x%X"
+ "Buffer is not a Placement Sparse Buffer"
+ "Command queue creation failed.  Worst processes %{public}@"
+ "Descriptor data type (%s) does not match tensor data type (%s)"
+ "Descriptor usage (%s) does not match tensor usage (%s)"
+ "Destination Buffer is not a Placement Sparse Buffer"
+ "Failed to create an IOGPUDevice... IOServiceOpen returned kIOReturn(0x%X)"
+ "Failed to creating mapping dispatch queue"
+ "Heap is not a Placement"
+ "Heap maxCompatiblePlacementSparsePageSize must be greater than or equal to the placementSparsePageSize of the buffer"
+ "IOGPUCommandQueueCreate"
+ "IOGPUCommandQueueSignalMTLEvent"
+ "IOGPUCommandQueueSignalSharedEvent"
+ "IOGPUCommandQueueWaitMTLEvent"
+ "IOGPUCommandQueueWaitSharedEvent"
+ "IOGPUMetal4CommandAllocator"
+ "IOGPUMetal4CommandAllocator.mm"
+ "IOGPUMetal4CommandBuffer"
+ "IOGPUMetal4CommandBuffer.mm"
+ "IOGPUMetal4CommandQueue"
+ "IOGPUMetal4CommandQueue.mm"
+ "IOGPUMetal4CommandQueue: command queue %s residency set limit of %u exceeded"
+ "IOGPUMetal4ComputeCommandEncoder"
+ "IOGPUMetal4MachineLearningCommandEncoder"
+ "IOGPUMetal4RenderCommandEncoder"
+ "IOGPUMetalCommandBufferStorage.mm"
+ "IOGPUMetalCommandBufferStorageFinalizeResidencySetList"
+ "IOGPUMetalCommandBufferStorageMergeResidencySetList"
+ "IOGPUMetalError: %@"
+ "IOGPUMetalResidencySetListCreate"
+ "IOGPUMetalResidencySetListDestroy"
+ "IOGPUMetalResidencySetListDuplicate"
+ "IOGPUMetalTensor"
+ "Impacting Interactivity"
+ "Invalid Input"
+ "Invalid Storage Mode %u for Placement Sparse Buffer"
+ "Invalid Storage Mode %u for Placement Sparse Texture"
+ "MTLTensor"
+ "MTLTensorDataTypeBFloat16"
+ "MTLTensorDataTypeFloat16"
+ "MTLTensorDataTypeFloat32"
+ "MTLTensorDataTypeInt16"
+ "MTLTensorDataTypeInt32"
+ "MTLTensorDataTypeInt8"
+ "MTLTensorDataTypeUInt16"
+ "MTLTensorDataTypeUInt32"
+ "MTLTensorDataTypeUInt8"
+ "MTLTensorSPI"
+ "MTLTensorUsageCompute"
+ "MTLTensorUsageRender"
+ "Mapping mode must be unmap for nil heap"
+ "Source Buffer is not a Placement Sparse Buffer"
+ "Source and Destination Buffers have different placement sparse page sizes"
+ "Specified slice is out of bounds with respect to this tensor"
+ "T@\"<MTLBuffer>\",R"
+ "T@\"<MTLBuffer>\",R,V_buffer"
+ "T@\"<MTLTensor>\",R"
+ "T@\"<MTLTensor>\",R,V_parentTensor"
+ "T@\"MTLTensorExtents\",R"
+ "T@\"MTLTensorExtents\",R,D"
+ "TB"
+ "TI,R,N,V_eventName"
+ "TQ,R,D,N"
+ "T^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B},R,V_storage"
+ "T^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}},R,V_resourceArgs"
+ "T^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ^v[0Q]},R"
+ "This operation is only permitted for tensors created with a buffer or an IOSurface"
+ "This tensor is not viewable with the given descriptor"
+ "Ti,R"
+ "Tq,R,V_maxCompatiblePlacementSparsePageSize"
+ "Tq,R,V_placementSparsePageSize"
+ "T{MTLResourceID=Q},R,D"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16@0:8"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}28@0:8Q16B24"
+ "^{IOGPUMetalCommandBufferStoragePool={gpuStorageQueue=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}{os_unfair_lock_s=I}iii@^{?}}"
+ "^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}"
+ "^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}16@0:8"
+ "^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ^v[0Q]}"
+ "^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ^v[0Q]}16@0:8"
+ "_IOGPUMetalResidencySetListInitialize"
+ "_aliasToDevice"
+ "_allocatedSize"
+ "_allocatedSize == 0"
+ "_busyQueue"
+ "_busyQueueCount"
+ "_commandAllocator"
+ "_commandAllocator && _storage"
+ "_commit:count:commitFeedback:"
+ "_completionQueue"
+ "_count <= _maxCount"
+ "_disableAsyncMapping"
+ "_generation"
+ "_isSharedEvent"
+ "_mappingCommandBuffer"
+ "_mappingLock"
+ "_mappingQueue"
+ "_maxCompatiblePlacementSparsePageSize"
+ "_parentTensor"
+ "_placementSparsePageSize"
+ "_postMappingEvent"
+ "_postMappingValue"
+ "_qosLevel"
+ "_storageCreateParams.hwResourcePools"
+ "_tier1ResourceMapping"
+ "_updateResidencySets"
+ "allocateMappingCommandBuffer"
+ "allocator && storage"
+ "args"
+ "args->comm.opt.virtualResource.virtual_bytes >= length"
+ "args->comm.opt.virtualResource.virtual_bytes >= placementSparseBytes"
+ "argsSize >= sizeof(sIOGPUDeviceNewCommandQueueArgs)"
+ "beginCommandBufferWithAllocator:"
+ "beginCommandBufferWithAllocator:options:"
+ "beginIOGPUCommandBufferWithAllocator:options:"
+ "cnt <= limit[groupIndex]"
+ "cnt <= resourceGroupArgs->groupCount"
+ "com.Metal.MappingDispatch"
+ "com.Metal4.CompletionQueue"
+ "commandAllocator"
+ "commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:"
+ "commandBufferComplete:completionTime:error:executeHandlers:"
+ "commandQueueRef->isMetal4Queue"
+ "commitFillArgs:count:args:argsSize:commitFeedback:"
+ "commitMappingCommandBuffer"
+ "copyBufferMappingsFromBuffer:toBuffer:operations:count:"
+ "dataType"
+ "defaultCompilerProcessesCount"
+ "descriptorPrivate->placementSparsePageSize == 0"
+ "dest"
+ "dest->resourceGroupArgs"
+ "dimensions"
+ "encodePostMappingWaitEvent:postMappingValue:timeout:"
+ "endCommandBuffer"
+ "endTier1MappingCommands"
+ "eventName"
+ "extentAtDimensionIndex:"
+ "feedbackQueue"
+ "fillCommandBufferArgs:"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithFunction:"
+ "functionHandleWithFunction:resourceIndex:"
+ "getBytes:strides:fromSlice:"
+ "getBytes:strides:fromSliceOrigin:sliceDimensions:"
+ "getCommandBufferStorage:retainReferences:"
+ "getGeneration"
+ "getObjects:count:"
+ "in"
+ "index == list->resourceGroup[0].size() + list->resourceGroup[1].size()"
+ "initAllocatorWithDevice:"
+ "initIOGPUMTL4CommandQueue:descriptor:args:argsSize:"
+ "initWithBuffer:"
+ "initWithCommandAllocator:"
+ "initWithCommandBuffer:allocator:"
+ "initWithDescriptor:device:"
+ "initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:args:argsSize:"
+ "initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:"
+ "initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:args:argsSize:deallocator:"
+ "initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:"
+ "initWithDeviceAndAliasToDevicePools:"
+ "initWithIOGPUError:MTL4QueueError:"
+ "initWithRank:extents:"
+ "internalMTLBuffer"
+ "isTensorViewableWithReshapedDescriptor:"
+ "kIOGPUCommandBufferCallbackErrorImpactingInteractivity"
+ "kIOGPUCommandBufferCallbackErrorInvalidInput"
+ "launchMappingThread"
+ "list"
+ "list->resourceGroup[0].size() <= limit[0]"
+ "list->resourceGroup[1].size() <= limit[1]"
+ "llvmVersion"
+ "maxCompatiblePlacementSparsePageSize"
+ "maximumCompilerProcessesCount"
+ "metadataVirtualAddress"
+ "mtlTensorFromGpuResourceID:"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCommandBuffer"
+ "newCompilerWithDescriptor:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newDevicePoolAliasedCommandAllocator"
+ "newLibraryWithMPSGraphPackageURL:name:error:"
+ "newMTL4CommandQueue"
+ "newMTL4CommandQueueWithDescriptor:error:"
+ "newPipelineDataSetSerializerWithDescriptor:"
+ "newTensorViewWithReshapedDescriptor:error:"
+ "newTensorViewWithSlice:error:"
+ "newTensorWithDescriptor:error:"
+ "newTensorWithDescriptor:offset:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "offset"
+ "parentTensor"
+ "placementSparsePageSize"
+ "plane"
+ "preCommit:count:options:"
+ "q"
+ "queryTimestampFrequency"
+ "rank"
+ "replaceSlice:withBytes:strides:"
+ "replaceSliceOrigin:sliceDimensions:withBytes:strides:"
+ "requiresLegacyCompilerProcessesCount"
+ "resetCommandBuffer"
+ "resourceGroupCount == _count"
+ "returnCommandBufferStorage:commandAllocatorGeneration:"
+ "setDataType:"
+ "setDimensions:"
+ "setRequiresLegacyCompilerProcessesCount:"
+ "setStrides:"
+ "setUsage:"
+ "sizeOfCounterHeapEntry:"
+ "source"
+ "source.resourceGroupArgs"
+ "strides"
+ "supportsAIRNTBinaryArchiveFunctionPointers"
+ "supportsAIRNTBinaryArchiveSpecializedFunctions"
+ "supportsAIRNTBinaryArchiveStitchedFunctions"
+ "supportsAtomicWaitNotify"
+ "supportsBackgroundAppRole"
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
+ "updateBufferMappings:heap:operations:count:"
+ "v24@0:8^{IOGPUCommandQueueCommandBufferArgs=III(?=@?Q)(?=@?Q)IQ}16"
+ "v28@0:8^@16I24"
+ "v28@0:8^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16I24"
+ "v28@0:8r^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}16I24"
+ "v32@0:8^{IOGPUCommandQueueCommandBufferArgs=III(?=@?Q)(?=@?Q)IQ}16@24"
+ "v36@0:8@16Q24S32"
+ "v40@0:8r^@16Q24@32"
+ "v48@0:8@\"MTLTensorExtents\"16@\"MTLTensorExtents\"24r^v32@\"MTLTensorExtents\"40"
+ "v48@0:8@16@24r^v32@40"
+ "v48@0:8@16@24r^{?=Q{_NSRange=QQ}Q}32Q40"
+ "v48@0:8@16@24r^{?={_NSRange=QQ}Q}32Q40"
+ "v48@0:8^v16@\"MTLTensorExtents\"24@\"MTLTensorExtents\"32@\"MTLTensorExtents\"40"
+ "v48@0:8^v16@\"MTLTensorExtents\"24{MTLTensorSlice=@@}32"
+ "v48@0:8^v16@24@32@40"
+ "v48@0:8^v16@24{MTLTensorSlice=@@}32"
+ "v48@0:8{MTLTensorSlice=@@}16r^v32@\"MTLTensorExtents\"40"
+ "v48@0:8{MTLTensorSlice=@@}16r^v32@40"
+ "v52@0:8^@16Q24Q32I40@44"
+ "v72@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I}{?=QQQI})}}64"
+ "v84@0:8@16@24I32^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}36Q44Q52I60@64@72B80"
+ "waitForEvent:value:timeout:"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"
+ "{_IOGPUMetalResource=\"vendor\"(?=\"reserved\"[4Q])\"info\"{IOGPUResourceInfo=\"iosurface\"^{__IOSurface}\"resourceSize\"b56\"iosurfaceField\"b8\"resourceID\"I}\"sharedAllocationUniqueId\"Q\"cachedAllocationUniqueId\"Q\"gpuAddress\"Q\"device\"@\"IOGPUMetalDevice<MTLDevice>\"\"label\"@\"NSString\"\"globalTraceObjectID\"Q\"labelTraceID\"Q\"resourceRef\"^{__IOGPUResource}\"clientSharedRO\"^{IOGPUClientSharedRO}\"virtualAddress\"^v\"options\"Q\"storageMode\"Q\"cpuCacheMode\"Q\"responsibleProcess\"i\"purgeableState\"Q\"purgeableAllowed\"B\"heap\"@\"IOGPUMetalHeap\"\"resource\"@\"IOGPUMetalResource\"\"offset\"Q\"length\"Q\"pinned\"B\"labelLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"metadataVirtualAddress\"^v}"
+ "{commandBufferStorageBusyQueue=\"tqh_first\"^{IOGPUMetalCommandBufferStorage}\"tqh_last\"^^{IOGPUMetalCommandBufferStorage}}"
+ "{vector<IOGPUIOCommandQueueCommandBufferCallbackBlock, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>=\"__begin_\"^(?)\"__end_\"^(?)\"__cap_\"^(?)}"
+ "\xf0\xf0!"
- ", buffer (parent dead, offset %lluB, stride %lluB)"
- ", dead"
- ", view (parent dead, slice %d, level %d)"
- "-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:]"
- "-[IOGPUMetalCommandQueue initWithDevice:descriptor:]"
- "@44@0:8@16Q24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}32I40"
- "@44@0:8@16^{__IOSurface=}24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}32I40"
- "@48@0:8@16@24^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}32Q40"
- "@52@0:8@16#24r^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}32I40@44"
- "@52@0:8@16Q24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}40I48"
- "@52@0:8@16^{__IOSurface=}24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}40I48"
- "@60@0:8@16@24^{__IOSurface=}32I40I44^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}48I56"
- "@60@0:8@16Q24Q32^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}40I48@52"
- "@60@0:8@16s24s28Q32Q40^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}48I56"
- "@68@0:8@16s24s28Q32Q40^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}48I56Q60"
- "@76@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64I72"
- "@76@0:8@16^{IOGPUAddressRange=QQ}24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64I72"
- "@80@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64I72B76"
- "@84@0:8@16@24^v32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64I72@?76"
- "@84@0:8@16^v24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64I72@?76"
- "@88@0:8@16^v24Q32I40Q44Q52Q60^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}68I76@?80"
- "@92@0:8@16s24s28Q32Q40@48Q56Q64Q72^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}80I88"
- "@96@0:8@16^v24Q32I40Q44Q52Q60Q68^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}76I84@?88"
- "Command queue creation failed.  Worst processes %@"
- "Failed to create an IOAccelDevice... IOServiceOpen returned kIOReturn(0x%X)"
- "IOGPUCommandQueueCreateWithQoS"
- "IOGPUMetalCommandBufferStorage.m"
- "Metal"
- "T^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]@},R,V_storage"
- "T^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}},R,V_resourceArgs"
- "T^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ[0Q]},R"
- "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]@}"
- "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]@}16@0:8"
- "^{IOGPUMetalCommandBufferStoragePool={gpuStorageQueue=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}{os_unfair_lock_s=I}iii@}"
- "^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}"
- "^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}16@0:8"
- "^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ[0Q]}"
- "^{__IOGPUResource={__CFRuntimeBase=QAQ}^{__IOGPUDevice}^vQQIIQQ^{IOGPUClientSharedRO}QQQQ[0Q]}16@0:8"
- "initWithIOGPUError:"
- "v28@0:8r^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}16I24"
- "v32@0:8^{IOGPUCommandQueueCommandBufferArgs=III(?=@?Q)(?=@?Q)I}16@24"
- "v72@0:8@16@24Q32Q40Q48Q56^{IOGPUNewResourceArgs={IOGPUNewResourceData=IISSSSCCCCIQQQII(?={?=QQQ(?=IQ)}{?=IIII[2Q]}{?=QQQ}{?=I})}}64"
- "{_IOGPUMetalResource=\"vendor\"(?=\"reserved\"[4Q])\"info\"{IOGPUResourceInfo=\"iosurface\"^{__IOSurface}\"resourceSize\"b56\"iosurfaceField\"b8\"resourceID\"I}\"sharedAllocationUniqueId\"Q\"cachedAllocationUniqueId\"Q\"gpuAddress\"Q\"device\"@\"IOGPUMetalDevice<MTLDevice>\"\"label\"@\"NSString\"\"globalTraceObjectID\"Q\"labelTraceID\"Q\"resourceRef\"^{__IOGPUResource}\"clientSharedRO\"^{IOGPUClientSharedRO}\"virtualAddress\"^v\"options\"Q\"storageMode\"Q\"cpuCacheMode\"Q\"responsibleProcess\"i\"purgeableState\"Q\"purgeableAllowed\"B\"heap\"@\"IOGPUMetalHeap\"\"resource\"@\"IOGPUMetalResource\"\"offset\"Q\"length\"Q\"pinned\"B\"labelLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}"
- "{vector<IOGPUIOCommandQueueCommandBufferCallbackBlock, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>=\"__begin_\"^(?)\"__end_\"^(?)\"__end_cap_\"{__compressed_pair<IOGPUIOCommandQueueCommandBufferCallbackBlock *, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>=\"__value_\"^(?)}}"

```
