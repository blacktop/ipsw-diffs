## DirectResource

> `/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource`

```diff

 19.0.5.0.0
-  __TEXT.__text: 0x1beb8
+  __TEXT.__text: 0x1bf98
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x2a0
   __TEXT.__cstring: 0x5f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31188EFA-0B1E-3BE6-9C7B-5AC3C207C89F
+  UUID: A1E4A4DD-96F0-30F5-959A-8946EA797704
   Functions: 890
   Symbols:   2430
   CStrings:  172
Functions:
~ __ZNSt3__16vectorINS_8functionIFvPN2re11DirectFenceEEEENS_9allocatorIS6_EEE9push_backB8nn200100EOS6_ : 260 -> 264
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2re9SharedPtrINS1_20DirectMemoryResourceEEENS_9allocatorIS4_EEE8__appendEm : 296 -> 312
~ ____ZN2re20xpc_array_get_valuesINS_25DirectMeshVertexAttributeEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 292 -> 296
~ ____ZN2re20xpc_array_get_valuesINS_22DirectMeshVertexLayoutEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 324 -> 328
~ __ZNSt3__16vectorIN2re16CreateDirectMeshENS_9allocatorIS2_EEE7reserveEm : 204 -> 220
~ __ZNSt3__16vectorIN2re16CreateDirectMeshENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 388 -> 400
~ ____ZN2re20xpc_array_get_valuesINS_16UpdateDirectMeshEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 496 -> 500
~ ____ZN2re20xpc_array_get_valuesINS_19CreateDirectTextureEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 516 -> 520
~ ____ZN2re20xpc_array_get_valuesINS_19UpdateDirectTextureEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 360 -> 364
~ ____ZN2re20xpc_array_get_valuesINS_18CreateDirectBufferEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 464 -> 468
~ ____ZN2re20xpc_array_get_valuesINS_18UpdateDirectBufferEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 436 -> 440
~ __ZNSt3__16vectorIN2re19CreateDirectPayloadENS_9allocatorIS2_EEE7reserveEm : 192 -> 208
~ ____ZN2re20xpc_array_get_valuesINS_19CreateDirectPayloadEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 436 -> 452
~ ____ZN2re20xpc_array_get_valuesINS_15DestroyResourceEEEbPU24objcproto13OS_xpc_object8NSObjectRNSt3__16vectorIT_NS5_9allocatorIS7_EEEE_block_invoke : 332 -> 336
~ __ZN2re12makeCommandsEPKNS_21DirectResourcesCommitE : 2824 -> 2844
~ __ZNSt3__16vectorIN2re19CreateDirectPayloadENS_9allocatorIS2_EEE9push_backB8nn200100EOS2_ : 300 -> 316
~ __ZNSt3__16vectorIN2re25DirectMeshVertexAttributeENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2re22DirectMeshVertexLayoutENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZN2re28DirectResourcesPendingCommit8addFenceENS_10UnownedPtrINS_11DirectFenceEEE : 444 -> 448
~ __ZN2re21DirectResourceContext6commitEv : 524 -> 528
~ __ZN2re21DirectResourceContext14freeListAppendEONS_9SharedPtrINS_24DirectResourcesReuseListEEE : 292 -> 296
~ __ZN2re26DirectResourcesCommitQueue24enqueueCommit_threadSafeENS_9SharedPtrINS_29DirectResourcesResolvedCommitEEE : 320 -> 324
~ __ZNSt3__16vectorIN2re16DirectResourceIdENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2re9SharedPtrINS1_29DirectResourcesResolvedCommitEEENS_9allocatorIS4_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS4_RS6_EEPS4_ : 188 -> 192
~ __ZNSt3__16vectorIN2re9SharedPtrINS1_13DirectTextureEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_ : 252 -> 256
~ __ZNSt3__16vectorIN2re9SharedPtrINS1_13DirectTextureEEENS_9allocatorIS4_EEE7reserveEm : 160 -> 176
~ __ZNSt3__16vectorINS_4pairIN2re9SharedPtrINS2_13DirectTextureEEENS3_INS2_19DirectTextureUpdateEEEEENS_9allocatorIS8_EEE7reserveEm : 160 -> 176
~ __ZNSt3__16vectorINS_4pairIN2re9SharedPtrINS2_13DirectTextureEEENS3_INS2_19DirectTextureUpdateEEEEENS_9allocatorIS8_EEE9push_backB8nn200100EOS8_ : 272 -> 280
~ __ZNSt3__16vectorIN2re24DirectResourcesReuseList5EntryENS_9allocatorIS3_EEE9push_backB8nn200100EOS3_ : 340 -> 356
~ __ZNSt3__16vectorIN2re24DirectResourcesReuseList5EntryENS_9allocatorIS3_EEE11__vallocateB8nn200100Em : 80 -> 84
~ _DRMeshDescriptorSetVertexAttributeCount : 404 -> 388
~ _DRMeshDescriptorSetVertexLayoutCount : 384 -> 376

```
