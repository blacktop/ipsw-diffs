## GPUToolsPlayback

> `/System/Library/PrivateFrameworks/GPUToolsPlayback.framework/GPUToolsPlayback`

```diff

-  __TEXT.__text: 0x63a4c
-  __TEXT.__objc_methlist: 0x30ec
+  __TEXT.__text: 0x638d4
+  __TEXT.__objc_methlist: 0x30fc
   __TEXT.__gcc_except_tab: 0xa664
   __TEXT.__cstring: 0x3428
   __TEXT.__const: 0x240
-  __TEXT.__unwind_info: 0x21f0
+  __TEXT.__unwind_info: 0x21e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a60
+  __DATA_CONST.__objc_selrefs: 0x2a68
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x6e8
   __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__cfstring: 0x1a40
-  __AUTH_CONST.__objc_const: 0x5480
+  __AUTH_CONST.__objc_const: 0x5488
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_arrayobj: 0x18
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Functions:
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqe220106EPKvm : 532 -> 520
~ -[DYMTLIndirectCommandBufferManager updateReplayerTranslationBuffer] : 1284 -> 1252
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN8GPUTools3MTL5Utils21DYMTLBufferGPUAddressEEEvT1_SA_T0_ : 180 -> 176
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN8GPUTools3MTL5Utils21DYMTLBufferGPUAddressEEEbT1_SA_T0_ : 1136 -> 1124
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10OffsetPairEEvT1_S7_T0_ : 212 -> 188
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10OffsetPairEEvT1_S7_T0_ : 224 -> 220
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEP10OffsetPairRNS_6__lessIvvEEEENS_4pairIT0_bEES8_S8_T1_ : 468 -> 464
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10OffsetPairEEbT1_S7_T0_ : 1208 -> 1184
~ __ZNSt3__119__partial_sort_implB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10OffsetPairS6_EET1_S7_S7_T2_OT0_ : 372 -> 352
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15PatchingRequestEEvT1_S7_T0_ : 292 -> 272
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15PatchingRequestEEvT1_S7_T0_ : 336 -> 348
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15PatchingRequestEEbT1_S7_T0_ : 836 -> 832
~ -[DYMTLIndirectArgumentBufferManager processResourceMapsData:] : 724 -> 720
~ -[DYMTLIndirectArgumentBufferManager notifyReplayerTargetIndirectArgumentBuffers:] : 444 -> 440
~ -[DYMTLIndirectArgumentBufferManager decodeReplayerIAB:offset:function:argument:] : 2260 -> 2264
~ __ZN8GPUTools3MTL27MakeMTLRenderPassDescriptorEPKvRNSt3__113unordered_mapIyU8__strongP11objc_objectNS3_4hashIyEENS3_8equal_toIyEENS3_9allocatorINS3_4pairIKyS7_EEEEEE : 1724 -> 1728
~ __ZN8GPUTools3MTL31MakeMTLRenderPipelineDescriptorEPKvRNSt3__113unordered_mapIyU8__strongP11objc_objectNS3_4hashIyEENS3_8equal_toIyEENS3_9allocatorINS3_4pairIKyS7_EEEEEE : 2292 -> 2320
~ __ZN8GPUTools3MTL35MakeMTLTileRenderPipelineDescriptorEPKvRNSt3__113unordered_mapIyU8__strongP11objc_objectNS3_4hashIyEENS3_8equal_toIyEENS3_9allocatorINS3_4pairIKyS7_EEEEEE : 612 -> 628
~ __ZN8GPUTools3MTL32MakeMTLComputePipelineDescriptorEPKvRNSt3__113unordered_mapIyU8__strongP11objc_objectNS3_4hashIyEENS3_8equal_toIyEENS3_9allocatorINS3_4pairIKyS7_EEEEEE : 884 -> 856
~ __ZN8GPUTools3MTL30MakeMTLImageFilterFunctionInfoEPKv : 256 -> 248
~ -[DYMTLDebugPlaybackEngineCounterSupport _profileSplitEncodersForProfileInfo:] : 5292 -> 5284
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyEEEEEvT1_S8_T0_ : 328 -> 312
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyEEEEEvT1_S8_T0_ : 424 -> 412
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyEEEEEbT1_S8_T0_ : 644 -> 620
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyyEEEEEvT1_S8_T0_ : 432 -> 400
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyyEEEEEvT1_S8_T0_ : 452 -> 428
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPNS_5tupleIJyyyyyyyEEERNS_6__lessIvvEEEENS_4pairIT0_bEES9_S9_T1_ : 596 -> 604
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_5tupleIJyyyyyyyEEEEEbT1_S8_T0_ : 700 -> 644
~ ___63-[DYMTLCommonDebugFunctionPlayer setupProfilingForCounterLists]_block_invoke_2 : 1736 -> 1720
~ __ZN14ShaderDebugger8Metadata12MDSerializer17serializeToBufferERNSt3__16vectorIhNS2_9allocatorIhEEEE : 1280 -> 1260
~ __ZN14ShaderDebugger8Metadata12MDSerializer22serializeCompositeTypeEyRKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEyyyytyRKNS2_6vectorINS2_4pairINS0_6MDBase12MetadataTypeEyEENS6_ISF_EEEE : 1100 -> 1088
~ __ZN14ShaderDebugger8Metadata12MDSerializer23serializeSubroutineTypeEyRKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEyyyytRKNS2_6vectorINS2_4pairINS0_6MDBase12MetadataTypeEyEENS6_ISF_EEEE : 984 -> 972
~ __ZNSt3__15dequeIU8__strongU13block_pointerFvvENS_9allocatorIS3_EEE19__add_back_capacityEv : 484 -> 472

```
