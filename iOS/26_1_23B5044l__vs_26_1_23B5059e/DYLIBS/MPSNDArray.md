## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.1.1.0.0
-  __TEXT.__text: 0x10538c
+129.1.4.0.0
+  __TEXT.__text: 0x104d64
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x6a84
-  __TEXT.__const: 0x83c08
-  __TEXT.__gcc_except_tab: 0x3e80
-  __TEXT.__cstring: 0xd947
-  __TEXT.__unwind_info: 0x1870
+  __TEXT.__const: 0x83c18
+  __TEXT.__gcc_except_tab: 0x3d04
+  __TEXT.__cstring: 0xdad8
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6c21
+  __TEXT.__objc_methname: 0x6bf8
   __TEXT.__objc_methtype: 0x1ea9
-  __TEXT.__objc_stubs: 0x32c0
+  __TEXT.__objc_stubs: 0x3260
   __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__const: 0xedb0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1530
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x3f80
-  __AUTH_CONST.__cfstring: 0x6a60
+  __AUTH_CONST.__const: 0x3fe0
+  __AUTH_CONST.__cfstring: 0x6ba0
   __AUTH_CONST.__objc_const: 0xe888
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x6a8
   __DATA.__data: 0x9c4
-  __DATA.__bss: 0x5b8
+  __DATA.__bss: 0x5d8
   __DATA_DIRTY.__objc_data: 0x5280
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9030AE1D-13A3-3CD6-9CBB-375910DEEE9C
-  Functions: 2233
-  Symbols:   7523
-  CStrings:  3630
+  UUID: DFED76E7-6CB5-3ECB-8730-619AD7FA1B40
+  Functions: 2236
+  Symbols:   7527
+  CStrings:  3645
 
Symbols:
+ __Z18encode_qmm_genericPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP10MPSLibraryRK14QmmGenericArgs
+ ____ZL14MPSSDPATGTileHv_block_invoke
+ ____ZL16MPSSDPASimdTileHv_block_invoke
+ ____ZL16MPSSDPASimdTileWv_block_invoke
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.215
+ ___block_literal_global.422
- GCC_except_table56
- GCC_except_table57
- __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
- __ZZL21MPSSDPAElasticBarriervE9predicate
- ___block_literal_global.194
- ___block_literal_global.421
- _objc_msgSend$createFallbackKernels:
- _objc_msgSend$insertObject:atIndex:
- _objc_msgSend$numberWithInteger:
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMultiplyGeneric.mm"
+ "Data in the fastest moving dimension of K must be contiguous"
+ "Data in the fastest moving dimension of M must be contiguous"
+ "Data in the fastest moving dimension of Q must be contiguous"
+ "Data in the fastest moving dimension of V must be contiguous"
+ "MPSNDARRAY_SDPA_SIMD_TILE_H"
+ "MPSNDARRAY_SDPA_SIMD_TILE_W"
+ "MPSNDARRAY_SDPA_TG_TILE_H"
+ "Using encode_qmm_generic encode path\n"
+ "failed to load pipeline state"
+ "qmm_n_bfloat"
+ "qmm_n_float"
+ "qmm_n_half"
+ "qmm_t_bfloat"
+ "qmm_t_float"
+ "qmm_t_half"
- "Currently SDPA fallback only supports MPSNDArraySDPALayoutBHXF"
- "Fallback to multi-dispatch (2Gemm) encoding\n"
- "QK^T"
- "insertObject:atIndex:"
- "keyTransposeTensor"
- "maskAdd"
- "maskTensor"
- "numberWithInteger:"
- "queryTensor"
- "scaleMul"
- "scaleTensor"

```
