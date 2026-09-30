## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-129.3.2.0.0
-  __TEXT.__text: 0x29108
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4d94
-  __TEXT.__cstring: 0x5ffc
-  __TEXT.__const: 0x208
+130.12.0.0.0
+  __TEXT.__text: 0x292ac
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_methlist: 0x4e5c
+  __TEXT.__cstring: 0x63d4
+  __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
-  __TEXT.__unwind_info: 0xcd8
+  __TEXT.__unwind_info: 0xd18
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb7b1
-  __TEXT.__objc_methtype: 0x6c3c
+  __TEXT.__objc_methname: 0xb82c
+  __TEXT.__objc_methtype: 0x6c69
   __TEXT.__objc_stubs: 0x31c0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2870
+  __DATA_CONST.__objc_selrefs: 0x2890
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7e10
+  __AUTH_CONST.__objc_const: 0x7e60
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x398
+  __DATA.__objc_ivar: 0x39c
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23EFF665-069E-38BE-BBA1-09A5D0C09F86
-  Functions: 1429
-  Symbols:   4282
-  CStrings:  2968
+  UUID: AA3AF6AE-5D9C-3A26-99DC-E46C77A9849A
+  Functions: 1464
+  Symbols:   4374
+  CStrings:  2979
 
Symbols:
+ -[IOGPUMetal4CommandBuffer setLabel:]
+ -[IOGPUMetal4CommandQueue setScheduledHandler:]
+ -[IOGPUMetalPooledResource emitResourceInfoTraceEvent]
+ -[IOGPUMetalTensor doesAliasAllResources:count:]
+ -[IOGPUMetalTensor doesAliasAnyResources:count:]
+ -[IOGPUMetalTensor doesAliasResource:]
+ -[IOGPUMetalTensor getBytes:strides:fromSliceOrigin:sliceDimensions:]
+ -[IOGPUMetalTensor isAliasable]
+ -[IOGPUMetalTensor isComplete]
+ -[IOGPUMetalTensor isPurgeable]
+ -[IOGPUMetalTensor isWriteComplete]
+ -[IOGPUMetalTensor makeAliasable]
+ -[IOGPUMetalTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:]
+ -[IOGPUMetalTensor setPurgeableState:]
+ -[IOGPUMetalTensor waitUntilComplete]
+ GCC_except_table32
+ GCC_except_table39
+ GCC_except_table43
+ OBJC_IVAR_$__MTL4CommandBuffer._labelTraceID
+ _OBJC_IVAR_$_IOGPUMetal4CommandQueue._scheduledHandler
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __OBJC_$_INSTANCE_METHODS_IOGPUMetalPooledResource
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__113__tree_removeB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjNS_4pairIKjsEENS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS6_EEE15__emplace_multiIJNS4_IjsEEEEENS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjNS_4pairIKjsEENS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSI_SI_
+ __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjNS_4pairIKjsEENS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS6_EEE21__remove_node_pointerEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjNS_4pairIKjsEENS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS6_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB9foe210106IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE9push_backB9foe210106ERKS1_
+ __ZNSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE9push_backB9foe210106ERKs
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1352
+ ___77-[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:]_block_invoke_2
+ _objc_msgSend$initWithRank:values:
+ _objc_release_x24
- -[IOGPUMetalCommandEncoder globalTraceObjectID]
- GCC_except_table28
- GCC_except_table31
- GCC_except_table37
- GCC_except_table48
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjS2_NS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS2_EEE15__emplace_multiIJNS_4pairIjsEEEEENS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEDpOT_
- __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjS2_NS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSF_SF_
- __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjS2_NS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS2_EEE21__remove_node_pointerEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjS2_NS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
- __ZNSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
- __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE9push_backB8ne200100ERKs
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1346
- ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
- _objc_msgSend$initWithRank:extents:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugAY8CSaojJ9CD4pOoEXXMRJKVRDtzw2LTI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugAY8CSaojJ9CD4pOoEXXMRJKVRDtzw2LTI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugAY8CSaojJ9CD4pOoEXXMRJKVRDtzw2LTI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/Library/Caches/com.apple.xbs/46FA7DE8-5261-4E5A-A9DC-457EB3D415F7/TemporaryDirectory.K4ONPB/Sources/IOGPUFamily/IOGPU/IOGPUResourceRef.c"
+ "@\"MTLDeviceFeatureQueries\"16@0:8"
+ "T@\"MTLDeviceFeatureQueries\",R"
+ "_scheduledHandler"
+ "featureQueries"
+ "initWithRank:values:"
+ "isWriteComplete"
+ "setScheduledHandler:"
+ "supportsPlacementSparse"
+ "v24@0:8@?16"
- "/Library/Caches/com.apple.xbs/Sources/IOGPUFamily/IOGPU/IOGPUResourceRef.c"
- "initWithRank:extents:"

```
