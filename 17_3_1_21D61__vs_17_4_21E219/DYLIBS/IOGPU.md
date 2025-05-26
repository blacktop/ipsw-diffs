## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-93.10.1.0.0
-  __TEXT.__text: 0x1c898
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1f14
-  __TEXT.__cstring: 0x49e1
+93.40.3.0.0
+  __TEXT.__text: 0x1c990
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x1f1c
+  __TEXT.__cstring: 0x4a49
   __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0x6e4
-  __TEXT.__gcc_except_tab: 0x26c
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__unwind_info: 0x8e0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x4f4
-  __TEXT.__objc_methname: 0x9962
-  __TEXT.__objc_methtype: 0x4fbe
+  __TEXT.__objc_methname: 0x9a1e
+  __TEXT.__objc_methtype: 0x4fce
   __TEXT.__objc_stubs: 0x2760
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x5c0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9938
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_const: 0x99d8
+  __DATA_CONST.__objc_selrefs: 0x1260
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__objc_const: 0xae8
-  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x128
-  __DATA.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x600
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1032
-  Symbols:   3187
-  CStrings:  2316
+  Functions: 1033
+  Symbols:   3190
+  CStrings:  2328
 
Symbols:
+ -[IOGPUMetalCommandBuffer setResponsibleTaskIDs:count:]
+ __ZNKSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__113__tree_removeB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB8ue170006IPS1_S6_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ _memmove
- __ZNKSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__113__tree_removeB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEEC2ERKS4_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
CStrings:
+ "-[IOGPUMetalCommandBuffer setResponsibleTaskIDs:count:]"
+ "T@\"<MTLBuffer>\",?,&,N"
+ "T@\"MTLAccelerationStructureDescriptor\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "TB,?"
+ "TB,?,R,GisClampToHalfBorderSupported"
+ "TB,?,R,GisCustomBorderColorSupported"
+ "TB,?,R,GisQuadDataSharingSupported"
+ "TB,?,R,GisRGB10A2GammaSupported"
+ "TQ,?,N"
+ "TQ,?,R"
+ "TQ,?,R,N"
+ "setResponsibleTaskIDs: with uncommitted encoder"
+ "setResponsibleTaskIDs:count:"
+ "supportsArgumentBuffers"
+ "supportsResourceHeaps"
+ "v28@0:8r^I16I24"
+ "waitUntilSignaledValue:timeoutMS:"
- "T@\"MTLAccelerationStructureDescriptor\",&,N"
- "TB"
- "TB,R,GisClampToHalfBorderSupported"
- "TB,R,GisCustomBorderColorSupported"
- "TB,R,GisQuadDataSharingSupported"
- "TB,R,GisRGB10A2GammaSupported"

```
