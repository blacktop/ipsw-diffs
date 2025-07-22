## dyld

> `/usr/lib/dyld`

```diff

-1322.3.0.0.0
-  __TEXT.__text: 0x8a368
+1323.2.0.0.0
+  __TEXT.__text: 0x8a6a8
   __TEXT.__const: 0x2300
-  __TEXT.__cstring: 0xfe43
+  __TEXT.__cstring: 0xfe5d
   __TEXT.__unwind_info: 0x4f8
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x6e08
+  __DATA_CONST.__const: 0x6e20
   __DATA.__data: 0x2f0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0x70
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 4E9F3B1E-8F53-3E3B-849C-950CA957C64B
-  Functions: 2881
-  Symbols:   7274
-  CStrings:  1981
+  UUID: C5EE0815-D8E7-3D47-A6AA-91966E34F810
+  Functions: 2882
+  Symbols:   7276
+  CStrings:  1983
 
Symbols:
+ __ZN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE5eraseEPS6_S8_
+ ___Block_byref_object_copy_.295
+ ___Block_byref_object_copy_.46
+ ___Block_byref_object_copy_.56
+ ___Block_byref_object_copy_.83
+ ___Block_byref_object_copy_.92
+ ___Block_byref_object_dispose_.296
+ ___Block_byref_object_dispose_.47
+ ___Block_byref_object_dispose_.57
+ ___Block_byref_object_dispose_.84
+ ___Block_byref_object_dispose_.93
+ ____ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.66
+ ____ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.66.cold.1
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.149
+ ___block_descriptor_tmp.289
+ ___block_descriptor_tmp.291
+ ___block_descriptor_tmp.294
+ ___block_descriptor_tmp.298
+ ___block_descriptor_tmp.300
+ ___block_descriptor_tmp.303
+ ___block_descriptor_tmp.306
+ ___block_descriptor_tmp.310
+ ___block_descriptor_tmp.86
+ ___block_descriptor_tmp.91
- ___Block_byref_object_copy_.294
- ___Block_byref_object_copy_.48
- ___Block_byref_object_copy_.66
- ___Block_byref_object_copy_.91
- ___Block_byref_object_copy_.94
- ___Block_byref_object_dispose_.295
- ___Block_byref_object_dispose_.49
- ___Block_byref_object_dispose_.67
- ___Block_byref_object_dispose_.92
- ___Block_byref_object_dispose_.95
- ____ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.68
- ____ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.68.cold.1
- ___block_descriptor_tmp.288
- ___block_descriptor_tmp.290
- ___block_descriptor_tmp.292
- ___block_descriptor_tmp.296
- ___block_descriptor_tmp.299
- ___block_descriptor_tmp.302
- ___block_descriptor_tmp.305
- ___block_descriptor_tmp.308
- ___block_descriptor_tmp.93
Functions:
~ __ZN5dyld423ExternallyViewableState17createMinimalInfoERN3lsl9AllocatorEyPKcyS5_PK15DyldSharedCache : 1936 -> 1940
~ __ZN5dyld412RuntimeState16setObjCNotifiersENS_16ReadOnlyCallbackIPFvPKcPK11mach_headerEEENS1_IPFvS6_PvS6_PKvEEENS1_IPFvPK29_dyld_objc_notify_mapped_infoEEENS1_IPFvjSI_U13block_pointerFvjEEEE : 1144 -> 1140
~ __ZN5dyld412RuntimeState19partitionDelayLoadsENSt3__14spanIPKNS_6LoaderELm18446744073709551615EEES6_PN3lsl6VectorIS5_EE : 956 -> 1632
~ __ZNK5dyld46Loader11isDelayInitERNS_12RuntimeStateE.cold.1 : 64 -> 92
+ __ZN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE5eraseEPS6_S8_
~ __ZNK10AAREncoder10encodeLinkERKNS_4LinkER10ByteStream : 388 -> 356
CStrings:
+ "1323.2"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jul 14 23:00:51 PDT 2025; root:libignition-58~9226/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Mon Jul 14 23:00:51 PDT 2025; root:libignition-58~9226/libignition_core/RELEASE_ARM64E"
+ "armv8.1m.main"
+ "armv8m.main"
- "1322.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jun 30 21:48:11 PDT 2025; root:libignition-58~7356/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Jun 30 21:48:11 PDT 2025; root:libignition-58~7356/libignition_core/RELEASE_ARM64E"

```
