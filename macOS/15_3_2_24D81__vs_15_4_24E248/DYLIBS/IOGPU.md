## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/Versions/A/IOGPU`

```diff

-104.1.2.0.0
-  __TEXT.__text: 0x2311c
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x2468
-  __TEXT.__cstring: 0x4ef6
-  __TEXT.__const: 0x510
-  __TEXT.__gcc_except_tab: 0x384
+104.4.1.0.0
+  __TEXT.__text: 0x22f7c
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x46dc
+  __TEXT.__cstring: 0x4ef4
+  __TEXT.__const: 0x500
+  __TEXT.__gcc_except_tab: 0x3a8
   __TEXT.__oslogstring: 0x82f
-  __TEXT.__unwind_info: 0xaa8
+  __TEXT.__unwind_info: 0xb08
   __TEXT.__objc_classname: 0x56c
   __TEXT.__objc_methname: 0xae11
   __TEXT.__objc_methtype: 0x5e1e

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15a8
+  __DATA_CONST.__objc_selrefs: 0x2630
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0xb7a0
+  __AUTH_CONST.__objc_const: 0x73c0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x350
   __DATA.__data: 0x730

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 153B19ED-E98A-3714-89B3-E0A992F861B2
-  Functions: 1193
-  Symbols:   2598
-  CStrings:  2760
+  UUID: 1E0624E8-E30F-3A8D-94A5-836BF0412714
+  Functions: 1236
+  Symbols:   2648
+  CStrings:  2759
 
Symbols:
+ +[IOGPUMemoryInfo initialize].cold.1
+ +[IOGPUMetalTexture initNewTextureDataWithDevice:descriptor:sysMemSize:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:].cold.1
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:].cold.1
+ -[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:].cold.2
+ -[IOGPUMetalCommandBuffer didCompleteWithStartTime:endTime:error:].cold.2
+ -[IOGPUMetalCommandBuffer encodeConditionalAbortEvent:].cold.1
+ -[IOGPUMetalCommandBuffer encodeSignalEvent:value:].cold.1
+ -[IOGPUMetalCommandBuffer encodeSignalEvent:value:agentMask:].cold.1
+ -[IOGPUMetalCommandBuffer encodeSignalEventScheduled:value:].cold.1
+ -[IOGPUMetalCommandBuffer encodeWaitForEvent:value:timeout:].cold.1
+ -[IOGPUMetalCommandBuffer setCurrentCommandEncoder:].cold.1
+ -[IOGPUMetalCommandBuffer setProtectionOptions:].cold.1
+ -[IOGPUMetalCommandBuffer setResponsibleTaskIDs:count:].cold.1
+ -[IOGPUMetalCommandBuffer validate].cold.1
+ -[IOGPUMetalCommandBuffer validate].cold.2
+ -[IOGPUMetalHeap initWithDevice:size:options:args:argsSize:desc:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithDescriptor:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithDescriptor:offset:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithSize:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithSize:offset:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithSize:offset:resourceIndex:].cold.1
+ -[IOGPUMetalHeap newAccelerationStructureWithSize:resourceIndex:].cold.1
+ -[IOGPUMetalHeap newSubResourceAtOffset:withLength:alignment:options:].cold.2
+ -[IOGPUMetalHeap newSubResourceWithLength:alignment:options:offset:].cold.2
+ -[IOGPUMetalIOCommandBuffer commit].cold.1
+ -[IOGPUMetalResource initWithDevice:remoteStorageResource:options:args:argsSize:].cold.3
+ -[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:].cold.3
+ -[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:].cold.4
+ -[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:].cold.5
+ -[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:].cold.6
+ IOGPUCommandQueueCreateWithQoS.cold.4
+ IOGPUCommandQueueGetTypeID.cold.1
+ IOGPUDeviceCreateWithAPIProperty.cold.2
+ IOGPUDeviceCreateWithAPIProperty.cold.3
+ IOGPUDeviceGetTypeID.cold.1
+ IOGPUIOCommandQueueCreate.cold.5
+ IOGPUIOCommandQueueGetTypeID.cold.1
+ IOGPUMetalCommandBufferStorageAddResidencySets.cold.1
+ IOGPUNotificationQueueCreate.cold.2
+ IOGPUNotificationQueueCreate.cold.3
+ IOGPUNotificationQueueGetTypeID.cold.1
+ IOGPUResourceCreate.cold.1
+ IOGPUResourceGetClientShared.cold.1
+ IOGPUResourceGetClientSharedPrivate.cold.1
+ IOGPUResourceGetDataBytes.cold.1
+ IOGPUResourceGetTypeID.cold.1
+ __39-[IOGPUMetalIOCommandBuffer addBarrier]_block_invoke.20.cold.1
+ __ZNKSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ioGPUCommandQueueFinalize.cold.1
+ ioGPUIOCommandQueueFinalize.cold.1
+ validateGPUPriority.cold.1
- _OUTLINED_FUNCTION_2
- __ZNKSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- _strcmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOGPUFamily/IOGPU/IOGPUResourceRef.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/IOGPUFamily/IOGPU/IOGPUResourceRef.c"
- "1"

```
