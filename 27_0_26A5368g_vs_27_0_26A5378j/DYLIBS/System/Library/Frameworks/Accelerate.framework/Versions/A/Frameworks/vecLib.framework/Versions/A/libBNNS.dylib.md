## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib`

```diff

-  __TEXT.__text: 0x10f59b4
-  __TEXT.__const: 0x629bc
-  __TEXT.__gcc_except_tab: 0x2ed2c
-  __TEXT.__cstring: 0x5be74
+  __TEXT.__text: 0x10f9efc
+  __TEXT.__const: 0x631bc
+  __TEXT.__gcc_except_tab: 0x2f29c
+  __TEXT.__cstring: 0x5c27d
   __TEXT.__oslogstring: 0x3a6
-  __TEXT.__unwind_info: 0x1bf50
-  __TEXT.__eh_frame: 0xdb60
+  __TEXT.__unwind_info: 0x1c158
+  __TEXT.__eh_frame: 0xdba0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x5608
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3c440
+  __AUTH_CONST.__const: 0x3c970
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
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib

   - /System/Library/PrivateFrameworks/MIL.framework/Versions/A/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39307
+  Functions: 39477
   Symbols:   827
-  CStrings:  8693
+  CStrings:  8714
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA_DIRTY.__data : content changed
CStrings:
+ " must be tensor of 1-bit unsigned integer values, but got "
+ " must be tensor of 4-bit unsigned integer or 4-bit signed integer or 8-bit unsigned integer or 8-bit signed integer or bfloat16 type or 16-bit float or 32-bit float values, but got "
+ "BasicNeuralNetworkSubroutines-2212.0.4~21"
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
- "BasicNeuralNetworkSubroutines-2211.0.0.0.1~87"
- "ConvertSDPAOp: custom scale is not supported"

```
