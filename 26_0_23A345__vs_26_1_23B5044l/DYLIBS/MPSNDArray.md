## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.0.18.0.0
-  __TEXT.__text: 0x105064
+129.1.1.0.0
+  __TEXT.__text: 0x10538c
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x6a84
-  __TEXT.__const: 0x746a0
+  __TEXT.__const: 0x83c08
   __TEXT.__gcc_except_tab: 0x3e80
-  __TEXT.__cstring: 0xd8ef
-  __TEXT.__unwind_info: 0x1868
+  __TEXT.__cstring: 0xd947
+  __TEXT.__unwind_info: 0x1870
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
   __TEXT.__objc_methname: 0x6c21

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x3f60
-  __AUTH_CONST.__cfstring: 0x6a40
+  __AUTH_CONST.__const: 0x3f80
+  __AUTH_CONST.__cfstring: 0x6a60
   __AUTH_CONST.__objc_const: 0xe888
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x6a8
-  __DATA.__data: 0x9c0
-  __DATA.__bss: 0x5b0
+  __DATA.__data: 0x9c4
+  __DATA.__bss: 0x5b8
   __DATA_DIRTY.__objc_data: 0x5280
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50F3B4AF-56AD-39E8-A7BF-F728E7660232
-  Functions: 2232
-  Symbols:   7517
-  CStrings:  3627
+  UUID: 9030AE1D-13A3-3CD6-9CBB-375910DEEE9C
+  Functions: 2233
+  Symbols:   7523
+  CStrings:  3630
 
Symbols:
+ GCC_except_table57
+ __ZZL21MPSSDPAElasticBarriervE6result
+ __ZZL21MPSSDPAElasticBarriervE9predicate
+ ____ZL21MPSSDPAElasticBarrierv_block_invoke
+ ___block_literal_global.194
+ ___block_literal_global.421
+ _winogradA18GTableSize
- GCC_except_table55
- ___block_literal_global.418
Functions:
~ __ZNK33MPSNDArrayMatMulA18DeviceBehavior19EncodeArrayMultiplyEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 18524 -> 18460
~ __ZNK30MPSNDArrayMatMulDeviceBehavior21EncodeArrayMultiplyI4EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 15964 -> 16172
~ __ZL25EncodeSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttention7MTLSize : 5048 -> 5436
~ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize : 8504 -> 8696
~ __ZL10EncodeSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 944 -> 804
+ ____ZL21MPSSDPAElasticBarrierv_block_invoke
~ __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 6708 -> 6864
CStrings:
+ "MPSNDARRAY_SDPA_ElasticBarrier"
+ "NDArrayI4MatrixMultiplyKContiguousA18_bfloat"
+ "NDArrayI4MatrixMultiplyKContiguousA18_half"
+ "only half/bfloat vector data type supported"
- "NDArrayI4MatrixMultiplyKContiguousA18"
- "only half vector data type supported"

```
