## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib`

```diff

-2212.1.1.0.0
-  __TEXT.__text: 0x1117b0c
-  __TEXT.__const: 0x631bc
-  __TEXT.__gcc_except_tab: 0x2f2c0
-  __TEXT.__cstring: 0x6055c
+2212.41.1.0.0
+  __TEXT.__text: 0x111c7c4
+  __TEXT.__const: 0x6323c
+  __TEXT.__gcc_except_tab: 0x2f330
+  __TEXT.__cstring: 0x617e1
   __TEXT.__oslogstring: 0x40e
-  __TEXT.__unwind_info: 0x1c318
+  __TEXT.__unwind_info: 0x1c3e0
   __TEXT.__eh_frame: 0xdff8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x56d0
+  __DATA_CONST.__const: 0x56b8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x3ccd0

   - /System/Library/PrivateFrameworks/MIL.framework/Versions/A/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39520
+  Functions: 39540
   Symbols:   830
-  CStrings:  9060
+  CStrings:  9172
 
CStrings:
+ "    .contig_size = %llu, .non_contig_rank = %llu,\n"
+ "    .type = %s, .function = %s,"
+ "    .type = %s, .function = %u,"
+ " .input0_scalar = %c, .input1_scalar = %c\n"
+ "<null>"
+ "AMX reduce kernel requires a tensor of rank >= 1"
+ "AMX reduce kernel requires fp32 or fp16 input"
+ "AMX reduce kernel would over-read: contiguous reduce extent is not a multiple of the vector width"
+ "BasicNeuralNetworkSubroutines-2212.41.1~1"
+ "KERNEL_GASR_EINSUM_ATTENTION_NEON"
+ "Op expects 1 to 5 inputs"
+ "Op expects 3 to 4 inputs"
+ "Op expects 3 to 6 inputs"
+ "Op expects exactly 2 outputs"
+ "Op expects exactly 3 outputs"
+ "Unsupported data type for arithmetic unary op"
+ "Unsupported data type for elementwise activation"
+ "activation op has an unexpected input count for its function"
+ "arithmetic unary op has an unexpected input count for its function"
+ "divide"
+ "divide_no_nan"
+ "floor_divide"
+ "instancenorm: epsilon operand argument is missing"
+ "instancenorm: unexpected input argument count"
+ "int32 is not supported for this arithmetic unary function"
+ "matmul_softmax_matmul: Q/K/V/output must share rank >= 3"
+ "matmul_softmax_matmul: Q/K/V/output shapes are inconsistent"
+ "matmul_softmax_matmul: all tensors must be first-major"
+ "matmul_softmax_matmul: bias footprint overflow"
+ "matmul_softmax_matmul: bias operand must be first-major"
+ "matmul_softmax_matmul: bias operand must be fp16"
+ "matmul_softmax_matmul: bias operand must be statically shaped"
+ "matmul_softmax_matmul: bias operand shape/layout mismatch"
+ "matmul_softmax_matmul: bias tensor too small"
+ "matmul_softmax_matmul: dynamic shapes not supported"
+ "matmul_softmax_matmul: leading dimensions must match across tensors"
+ "matmul_softmax_matmul: only fp16 is supported"
+ "matmul_softmax_matmul: outer-loop size overflow"
+ "matmul_softmax_matmul: scratch footprint overflow"
+ "matmul_softmax_matmul: scratch inner dimension too small for 64*(C+D)"
+ "matmul_softmax_matmul: scratch must be rank 2"
+ "matmul_softmax_matmul: scratch size overflow"
+ "matmul_softmax_matmul: scratch tensor too small"
+ "matmul_softmax_matmul: tensors are not contiguous in the expected layout"
+ "maximum"
+ "minimum"
+ "multiply"
+ "multiply_no_nan"
+ "norm: addend must be first-major"
+ "norm: addend must be statically shaped"
+ "norm: addend rank must match output"
+ "norm: addend shape must match output"
+ "norm: addend type must match output"
+ "norm: input/output must be first-major"
+ "norm: input/output rank mismatch"
+ "norm: input/output shape mismatch"
+ "norm: input/output type mismatch"
+ "norm: only fp16/fp32/bf16 supported"
+ "norm: per-channel size overflow"
+ "norm: per-channel tensor (mean/rsqrtvar/gamma/beta) too small"
+ "norm: rank must be >= 3"
+ "norm: validation only supported for static shapes"
+ "resample: coordinates shape too small for accesses"
+ "resample: input/output/coordinates must be first-major"
+ "resample: input/output/coordinates must be rank 4"
+ "resample: input_scratch tensor too small for input size"
+ "resample: invalid coordinates_format"
+ "resample: invalid coordinates_mode"
+ "resample: invalid coordinates_type"
+ "resample: invalid padding_mode"
+ "resample: invalid sampling_mode"
+ "resample: output batch/channel must match input"
+ "resample: reflection padding requires input H and W >= 2"
+ "resample: scratch size overflow"
+ "resample: scratch tensor too small for output size"
+ "resample: validation only supported for static shapes"
+ "resize: bilinear requires a scratch output tensor"
+ "resize: dynamic (ios17 shape input) not supported"
+ "resize: input/output must be first-major"
+ "resize: input/output rank mismatch"
+ "resize: input/output type mismatch"
+ "resize: invalid interpolation method"
+ "resize: invalid sampling mode"
+ "resize: leading dimensions must match between input and output"
+ "resize: only fp16/fp32 supported"
+ "resize: output H/W exceeds supported maximum (kernel uses a stack VLA per extent)"
+ "resize: rank must be >= 3"
+ "resize: scratch tensor too small"
+ "resize: this resize configuration must not declare a scratch tensor"
+ "resize: unsupported geometry/mode/layout (fp16 neon path may read one column past the input)"
+ "resize: validation only supported for static shapes"
+ "scalar operand has unsupported type"
+ "scalar operand must be statically shaped"
+ "scalar operand tensor too small"
+ "subtract"
+ "topk: axis out of range"
+ "topk: input/output must be first-major"
+ "topk: k exceeds input axis size"
+ "topk: k exceeds supported maximum (kernel uses a stack VLA of size k)"
+ "topk: k must be >= 1"
+ "topk: output indices must be first-major"
+ "topk: output indices must be int32 or uint16"
+ "topk: output indices must be statically shaped"
+ "topk: output indices rank must match input"
+ "topk: output indices shape inconsistent with input/k"
+ "topk: output values rank must match input"
+ "topk: output values shape inconsistent with input/k"
+ "topk: output values type must match input"
+ "topk: runtime k operand not supported"
+ "topk: validation only supported for static shapes"
+ "trunc_divide"
+ "upsample_resize_shape(of:"
+ "}, .non_contig_src0_stride = {"
+ "}, .non_contig_src1_stride = {"
- "BasicNeuralNetworkSubroutines-2212.1.1~15"
- "h19a"
```
