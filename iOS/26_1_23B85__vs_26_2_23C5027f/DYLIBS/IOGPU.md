## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

 129.2.10.0.0
-  __TEXT.__text: 0x29044
+  __TEXT.__text: 0x29054
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x4d94
   __TEXT.__cstring: 0x5ffc

   __TEXT.__unwind_info: 0xcd8
   __TEXT.__objc_classname: 0x635
   __TEXT.__objc_methname: 0xb7b1
-  __TEXT.__objc_methtype: 0x6c36
+  __TEXT.__objc_methtype: 0x6c3c
   __TEXT.__objc_stubs: 0x31c0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x768

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23510EFA-D0E4-382C-8E23-97D9FB2A0DF3
+  UUID: AE663A5C-805E-308E-99A6-5BA0A4F54535
   Functions: 1429
   Symbols:   4282
   CStrings:  2968
Functions:
~ __ZNSt3__16__treeINS_12__value_typeIjsEENS_19__map_value_compareIjS2_NS_4lessIjEELb1EEEN26IOGPUMetalSuballocatorHeap9AllocatorIS2_EEE15__emplace_multiIJNS_4pairIjsEEEEENS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEDpOT_ : 152 -> 160
~ -[IOGPUMetalIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:] : 1948 -> 1952
~ __ZNSt3__16vectorI24IOGPUIODecompressionArgsNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
CStrings:
+ "{vector<IOGPUIOCommandQueueCommandBufferCallbackBlock, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>=\"__begin_\"^(?)\"__end_\"^(?)\"\"{?=\"__cap_\"^(?)}}"
- "{vector<IOGPUIOCommandQueueCommandBufferCallbackBlock, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>=\"__begin_\"^(?)\"__end_\"^(?)\"__cap_\"^(?)}"

```
