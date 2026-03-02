## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-130.12.0.0.0
-  __TEXT.__text: 0x292ac
-  __TEXT.__auth_stubs: 0xd90
+130.13.0.0.0
+  __TEXT.__text: 0x290f8
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x4e5c
-  __TEXT.__cstring: 0x63d4
+  __TEXT.__cstring: 0x603b
   __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae

   __DATA_CONST.__objc_selrefs: 0x2890
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
   __AUTH_CONST.__objc_const: 0x7e60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 009174F2-C274-3E00-B8D3-4CF993B3C9A7
+  UUID: BA4667BD-DE1A-33E6-B74A-945A2E1FB0C8
   Functions: 1464
-  Symbols:   4374
-  CStrings:  2979
+  Symbols:   4372
+  CStrings:  2976
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__113__tree_removeB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB9nqe210106IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE9push_backB9nqe210106ERKS1_
+ __ZNSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE9push_backB9nqe210106ERKS2_
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE9push_backB9nqe210106ERKs
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__113__tree_removeB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI24IOGPUIODecompressionArgsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI45IOGPUIOCommandQueueCommandBufferCallbackBlockEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIP8NSObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB9foe210106Em
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE16__init_with_sizeB9foe210106IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI45IOGPUIOCommandQueueCommandBufferCallbackBlockNS_9allocatorIS1_EEE9push_backB9foe210106ERKS1_
- __ZNSt3__16vectorIN26IOGPUMetalSuballocatorHeap6BufferENS1_9AllocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIP8NSObjectNS_9allocatorIS2_EEE9push_backB9foe210106ERKS2_
- __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIsN26IOGPUMetalSuballocatorHeap9AllocatorIsEEE9push_backB9foe210106ERKs
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- _objc_release_x24
Functions:
~ _IOGPUMetalSuballocatorAllocate : 2556 -> 2496
~ _IOGPUMetalSuballocatorFree : 812 -> 780
~ -[IOGPUMetalIOCommandQueue _submitAvailableCommands:] : 852 -> 824
~ ___146-[IOGPUMetalIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:]_block_invoke_4 : 580 -> 312
~ -[IOGPUMetalIOCommandBuffer completeCommandCallbackBlocks] : 168 -> 120
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRfugAqoUgX_xA7ckQQYwqMcCUuUcFkP5UsG9Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAqoUgX_xA7ckQQYwqMcCUuUcFkP5UsG9Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugAqoUgX_xA7ckQQYwqMcCUuUcFkP5UsG9Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
