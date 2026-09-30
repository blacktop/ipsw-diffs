## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-1961.120.3.0.0
-  __TEXT.__text: 0xf82d2c
+1961.120.5.0.1
+  __TEXT.__text: 0xf8549c
   __TEXT.__auth_stubs: 0x16f0
   __TEXT.__const: 0x2c940
-  __TEXT.__gcc_except_tab: 0x2e4d4
-  __TEXT.__cstring: 0x4d91c
+  __TEXT.__gcc_except_tab: 0x2e4f4
+  __TEXT.__cstring: 0x4eb04
   __TEXT.__oslogstring: 0x303
-  __TEXT.__unwind_info: 0x17330
+  __TEXT.__unwind_info: 0x17338
   __TEXT.__eh_frame: 0xd360
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x5128

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AD94C02C-E922-3D65-9BB3-4376252EAE8C
-  Functions: 33023
-  Symbols:   842
-  CStrings:  7559
+  UUID: 52945A1E-2827-32E7-87D1-B6C6B581DEE3
+  Functions: 33031
+  Symbols:   843
+  CStrings:  7653
 
Symbols:
+ _BNNSGraphContextEnforceValidation
CStrings:
+ "BNNS Graph: %s : context not in valid state."
+ "BNNSGraphContextEnforceValidation"
+ "BNNSGraphContextEnforceValidation: operation parameter validation failed"
+ "BasicNeuralNetworkSubroutines-1961.120.5.0.1~22"
+ "Calls to BNNSGraphContextSetInternalValidation are invalid after call to BNNSGraphContextEnforceValidation."
+ "Constant Tensor %llxx read oob. Attempted to read %zu bytes from offset %llu of span (%p, %zu)\n"
+ "Input and output must have the same rank"
+ "Input and output shapes must match"
+ "Invalid data type size"
+ "Non-reduced axis output shape must match input shape"
+ "Non-scalar input0 and output shapes must match"
+ "Non-scalar input1 and output shapes must match"
+ "Non-scalar input2 and output shapes must match"
+ "Only supports first-major tensors"
+ "Op expects 1 to 2 inputs"
+ "Op expects exactly 1 inputs"
+ "Op expects exactly 1 outputs"
+ "Op expects exactly 2 inputs"
+ "Op expects exactly 3 inputs"
+ "Output rank inconsistent with input rank and reduction axes"
+ "Output shape inconsistent with input shape and padding amounts"
+ "Padding amount calculation overflowed"
+ "Parameter data type doesn't match argument data types"
+ "Parameter dest_type doesn't match output tensor type"
+ "Parameter input0 type doesn't match input0 tensor type"
+ "Parameter input1 type doesn't match input1 tensor type"
+ "Parameter input2 type doesn't match input2 tensor type"
+ "Parameter output type doesn't match output tensor type"
+ "Parameter src_type doesn't match input tensor type"
+ "Parameter type doesn't match argument data types"
+ "Reduced axis with keep_dims must have output size 1"
+ "Reduction axes reference dimensions beyond input rank"
+ "Shape Workspace Tensor %llxx accessed oob. Attempted to read %zu bytes from offset %llu of span (%p, %zu)\n"
+ "User-provided NDArray %llxx too small. Attempted to read %zu bytes from offset %llu of span (%p, %zu)\n"
+ "Validation not implemented for operation"
+ "Validation only supported for static shapes"
+ "View %llxx accessed oob. Attempted to read %zu bytes from offset %llu of span (%p, %zu)\n"
+ "Workspace Tensor %llxx accessed oob. Attempted to read %zu bytes from offset %llu of span (%p, %zu)\n"
+ "contig check calculations overflowed"
+ "contig_input data_type doesn't match orig_input data_type"
+ "contig_input footprint calculation overflowed"
+ "contig_input iteration exceeds input tensor footprint"
+ "contig_input ndim doesn't match orig_input ndim"
+ "contig_input size exceeds orig_input size"
+ "contig_input stride doesn't match orig_input stride"
+ "contig_output data_type doesn't match orig_output data_type"
+ "contig_output footprint calculation overflowed"
+ "contig_output iteration exceeds output tensor footprint"
+ "contig_output ndim doesn't match orig_output ndim"
+ "contig_output size exceeds orig_output size"
+ "contig_output stride doesn't match orig_output stride"
+ "dest footprint check calculation overflowed"
+ "dest max_index is beyond tensor footprint"
+ "invalid contig_size"
+ "invalid element count"
+ "invalid elements_per_block"
+ "invalid elements_per_block[0]"
+ "invalid elements_per_block[1]"
+ "invalid non_contig_rank"
+ "invalid num_contiguous_regions"
+ "invalid regions_per_block"
+ "ir_safe tensor descriptor has invalid data_type"
+ "ir_safe tensor descriptor has zero size in active dimension"
+ "ir_safe tensor descriptor ndim exceeds BNNS_MAX_TENSOR_DIMENSION"
+ "iteration parameter validation only supported on static shapes"
+ "max-element check calculation overflowed"
+ "max_index is beyond tensor footprint"
+ "non-contig check calculation overflowed"
+ "non_contig_size must be non-zero"
+ "non_contig_stride is not monotonically decreasing"
+ "num_contiguous_regions calculation overflowed"
+ "orig_input data_type doesn't match input tensor type"
+ "orig_input ndim doesn't match input tensor rank"
+ "orig_input size doesn't match input tensor shape"
+ "orig_input stride doesn't match input tensor stride"
+ "orig_output data_type doesn't match output tensor type"
+ "orig_output ndim doesn't match output tensor rank"
+ "orig_output size doesn't match output tensor shape"
+ "orig_output stride doesn't match output tensor stride"
+ "params ndim must be at most BNNS_MAX_TENSOR_DIMENSION"
+ "params.dst_ndim doesn't match output rank"
+ "params.dst_size doesn't match output shape"
+ "params.dst_stride doesn't match output stride"
+ "params.non_contig_rank must be at most BNNS_MAX_TENSOR_DIMENSION"
+ "params.non_contig_rank must be at most input.rank"
+ "params.non_contig_rank must be at most output.rank"
+ "params.src0_ndim doesn't match input0 rank"
+ "params.src0_size doesn't match input0 shape"
+ "params.src0_stride doesn't match input0 stride"
+ "params.src1_ndim doesn't match input1 rank"
+ "params.src1_size doesn't match input1 shape"
+ "params.src1_stride doesn't match input1 stride"
+ "source footprint check calculation overflowed"
+ "source max_index is beyond tensor footprint"
+ "transpose_size must be non-zero"
- "BasicNeuralNetworkSubroutines-1961.120.3~23"

```
