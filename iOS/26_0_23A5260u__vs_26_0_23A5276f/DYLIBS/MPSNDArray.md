## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.0.14.0.0
-  __TEXT.__text: 0xe6e9c
+129.0.15.0.0
+  __TEXT.__text: 0xe89e8
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x69fc
+  __TEXT.__objc_methlist: 0x6a14
   __TEXT.__const: 0x44900
-  __TEXT.__gcc_except_tab: 0x3708
-  __TEXT.__cstring: 0xb9a8
-  __TEXT.__unwind_info: 0x1770
+  __TEXT.__gcc_except_tab: 0x38d0
+  __TEXT.__cstring: 0xb9e9
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c3b
-  __TEXT.__objc_methname: 0x68a2
-  __TEXT.__objc_methtype: 0x1e06
-  __TEXT.__objc_stubs: 0x2e20
-  __DATA_CONST.__got: 0x298
+  __TEXT.__objc_methname: 0x6944
+  __TEXT.__objc_methtype: 0x1e33
+  __TEXT.__objc_stubs: 0x2f00
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__const: 0xe9f0
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1440
+  __DATA_CONST.__objc_selrefs: 0x1458
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x818
   __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0x3c00
-  __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0xe5f8
-  __DATA.__objc_ivar: 0x670
+  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__objc_const: 0xe6d8
+  __DATA.__objc_ivar: 0x68c
   __DATA.__data: 0x9c0
   __DATA.__bss: 0x450
   __DATA_DIRTY.__objc_data: 0x5280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D2F0263-BA40-373B-BD3D-4A6C8092258F
-  Functions: 2176
-  Symbols:   7286
-  CStrings:  3280
+  UUID: 32DAC294-A38D-3CB1-8A35-0B3CE14EA89B
+  Functions: 2179
+  Symbols:   7300
+  CStrings:  3294
 
Symbols:
+ -[MPSNDArrayScaledDotProductAttention createFallbackKernels:]
+ -[MPSNDArrayScaledDotProductAttention dealloc]
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table39
+ __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ _objc_msgSend$createFallbackKernels:
+ _objc_msgSend$initWithDevice:sourceCount:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$setIsLeftFused:
+ _objc_msgSend$setNormFusionDescriptor:
+ _objc_msgSend$setNormFusionType:
- GCC_except_table28
CStrings:
+ "@\"MPSNDArrayMatrixMultiplication\""
+ "Currently SDPA fallback only supports MPSNDArraySDPALayoutBHXF"
+ "Fallback to multi-dispatch (2Gemm) encoding\n"
+ "QK^T"
+ "_QKTMatmulKernel"
+ "_createdFallbackKernels"
+ "_finalMatmulKernel"
+ "_kernelDAGObject"
+ "_softMaxMatMulKernel"
+ "createFallbackKernels:"
+ "error: only supports scalar scale in MPSNDArraySDPALayoutBHXF layout"
+ "insertObject:atIndex:"
+ "keyTransposeTensor"
+ "maskAdd"
+ "maskTensor"
+ "numberWithInteger:"
+ "q24@0:8@16"
+ "queryTensor"
+ "scaleMul"
+ "scaleTensor"
- "could not find index 0 in the placeholder list"
- "could not find index 1 in the placeholder list"
- "could not find index 2 in the placeholder list"
- "could not find index 3 in the placeholder list"

```
