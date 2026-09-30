## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-  __TEXT.__text: 0x1137a2c
-  __TEXT.__const: 0x62a3c
-  __TEXT.__gcc_except_tab: 0x2e3e4
-  __TEXT.__cstring: 0x5f847
+  __TEXT.__text: 0x113f1d4
+  __TEXT.__const: 0x6323c
+  __TEXT.__gcc_except_tab: 0x2e95c
+  __TEXT.__cstring: 0x5fc50
   __TEXT.__oslogstring: 0x3a6
-  __TEXT.__unwind_info: 0x1bda8
-  __TEXT.__eh_frame: 0xd9e8
+  __TEXT.__unwind_info: 0x1c150
+  __TEXT.__eh_frame: 0xdae0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x6da0
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3a830
+  __AUTH_CONST.__const: 0x3ad60
   __AUTH_CONST.__cfstring: 0x440
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__auth_got: 0xb60
-  __AUTH.__data: 0x2220
-  __DATA.__data: 0x2858
+  __AUTH.__data: 0x2240
+  __DATA.__data: 0x2878
   __DATA.__bss: 0x7f8
-  __DATA.__common: 0x1098
+  __DATA.__common: 0x10a0
   __DATA_DIRTY.__data: 0x578
   __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39318
+  Functions: 39486
   Symbols:   827
-  CStrings:  8740
+  CStrings:  8761
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA_DIRTY.__data : content changed
CStrings:
+ " must be tensor of 1-bit unsigned integer values, but got "
+ " must be tensor of 4-bit unsigned integer or 4-bit signed integer or 8-bit unsigned integer or 8-bit signed integer or bfloat16 type or 16-bit float or 32-bit float values, but got "
+ "BasicNeuralNetworkSubroutines-2212.0.4~20"
+ "ConvertSDPAOp: failed to parse scale"
+ "ConvertSparseToDenseOp: expected 2 operands"
+ "ConvertSparseToDenseOp: expected exactly one result"
+ "ConvertSparseToDenseOp: failed to convert result type"
+ "ConvertSparseToDenseOp: mask must be constant"
+ "ConvertSparseToDenseOp: nonzero_data must be constant"
+ "Invalid attribute `scale` in property conversion: "
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::bnns::ConvertSparseToDenseOp]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::bnns::detail::SDPAOpGenericAdaptorBase::Properties]"
+ "bnns.sparse_to_dense"
+ "execute_affine_dequantize_conv_repack_op: unsupported tensor type combination"
+ "internal.rsqrt"
+ "matmul op requires input and output tensors of rank >= 2"
+ "scale_tensor"
+ "sdpa_dynamic_scale"
+ "sdpa_head_dim_fp"
+ "sdpa_head_dim_int"
+ "sdpa_query_shape"
+ "sparse_to_dense"
+ "sparse_to_dense: failed to parse output"
- "BasicNeuralNetworkSubroutines-2211.0.0.0.1~50"
- "ConvertSDPAOp: custom scale is not supported"

```
