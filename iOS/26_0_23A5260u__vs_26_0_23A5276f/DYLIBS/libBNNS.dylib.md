## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-1835.0.0.0.0
-  __TEXT.__text: 0xe99534
+1858.0.0.0.1
+  __TEXT.__text: 0xeef658
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__gcc_except_tab: 0x2d8ac
-  __TEXT.__const: 0x29730
-  __TEXT.__cstring: 0x4a450
+  __TEXT.__gcc_except_tab: 0x2de3c
+  __TEXT.__const: 0x2a9d0
+  __TEXT.__cstring: 0x4bce8
   __TEXT.__oslogstring: 0x303
-  __TEXT.__unwind_info: 0x179c0
+  __TEXT.__unwind_info: 0x18d28
   __TEXT.__eh_frame: 0xbe94
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x4758
+  __DATA_CONST.__const: 0x4a58
   __AUTH_CONST.__auth_got: 0xb30
-  __AUTH_CONST.__const: 0x28ca8
+  __AUTH_CONST.__const: 0x2a658
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH.__data: 0x1aa8
-  __DATA.__data: 0x4508
-  __DATA.__bss: 0xd10
-  __DATA.__common: 0xbe8
-  __DATA_DIRTY.__data: 0x4e8
+  __AUTH.__data: 0x1c70
+  __DATA.__data: 0x4708
+  __DATA.__bss: 0xd28
+  __DATA.__common: 0xca8
+  __DATA_DIRTY.__data: 0x540
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CE0CDF48-DDBA-3F20-B09E-DE0176ACDA93
-  Functions: 32843
-  Symbols:   830
-  CStrings:  7084
+  UUID: B628EEE7-E9A4-3833-8931-1196B158E41F
+  Functions: 34247
+  Symbols:   831
+  CStrings:  7210
 
Symbols:
+ _BNNSBitTranspose
CStrings:
+ " Rank of input needs to be same as len(axes), but input.rank == "
+ " alignInBits("
+ " and indices with rank "
+ " cannot produce a value of type "
+ " elements in dilation"
+ " elements in output_shape"
+ " elements in padding"
+ " elements in strides"
+ " must be 1D tensor of Boolean type. values, but got "
+ " must be 1D tensor of Index type. or 32-bit float values, but got "
+ " must be 5D tensor of 16-bit float or 32-bit float or f8E5M2 type or f8E4M3FN type or 4/8/16/32/64-bit signed integer or 4/8/16/32/64-bit unsigned integer or complex type with 16-bit float elements or complex type with 32-bit float elements values, but got "
+ " must be 5D tensor of 16-bit float or 32-bit float or f8E5M2 type or f8E4M3FN type or complex type with 16-bit float elements or complex type with 32-bit float elements values, but got "
+ " must be CoreML Tensor of 4/8/16/32/64-bit signed integer or 4/8/16/32/64-bit unsigned integer or Boolean type. values, but got "
+ " must be tensor of 1-bit unsigned integer values, but got "
+ " parameter `axes` needs to be constant and compile-time known"
+ " parameter `input` needs to be a ranked tensor"
+ " to a class or import"
+ " when the input has rank "
+ " whereas len(axes) == "
+ "' failed to satisfy constraint: 64-bit unsigned integer attribute"
+ "' failed to satisfy constraint: CoreML ResizeByScale Op's interpolation mode to use: 'linear' | 'nearest_neighbor'"
+ "' failed to satisfy constraint: CoreML ResizeByScale Op's sampling mode to use: 'half_pixel' | 'align_corners'"
+ "' failed to satisfy constraint: CoreML ScatterAlongAxis Op's mode to use: 'update' | 'add' | 'sub' | 'mul' | 'div' | 'max' | 'min'"
+ ", but indices shape ["
+ ", expected Axis between 0 and "
+ ", inclusive"
+ "Axis passed to cumsum is:"
+ "BNNS: unsupported input type amx2 reduce min/max op"
+ "BNNS: unsupported input type amx3 reduce min/max op"
+ "BNNS: unsupported reduce function type"
+ "BasicNeuralNetworkSubroutines-1858.0.0.0.1~16"
+ "CVPixelBuffer"
+ "First dimension should match for input and output in the op."
+ "Input shape["
+ "Invalid attribute `alignInBits` in property conversion: "
+ "Invalid attribute `asShim` in property conversion: "
+ "Invalid attribute `interpolation_mode` in property conversion: "
+ "Invalid attribute `member` in property conversion: "
+ "Invalid attribute `sampling_mode` in property conversion: "
+ "Invalid attribute `scatter_mode` in property conversion: "
+ "Invalid attribute `symbolsToImport` in property conversion: "
+ "Invalid axis "
+ "KERNEL_ARITHMETIC_VSMUL_FP16_MLA2"
+ "KERNEL_CONV_MLA_WITH_ACTIVATION_DYNAMIC"
+ "KERNEL_CONV_VERSION_2_WITH_ACTIVATION_DYNAMIC"
+ "KERNEL_REDUCE_FP_SUM_AMX3_DYNAMIC"
+ "KERNEL_REDUCE_FP_SUM_AXM2_DYNAMIC"
+ "KERNEL_REDUCE_FP_SUM_GENERIC_DYNAMIC"
+ "KERNEL_REDUCE_FP_SUM_SME2_DYNAMIC"
+ "KERNEL_REDUCE_MIN_MAX_AMX2_DYNAMIC"
+ "KERNEL_REDUCE_MIN_MAX_AMX3_DYNAMIC"
+ "KERNEL_REDUCE_MIN_MAX_GENERIC_DYNAMIC"
+ "KERNEL_REDUCE_MIN_MAX_SME2_DYNAMIC"
+ "MTLTexture"
+ "Number of input channels should be divisible by groupSize in conv_transpose."
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = (anonymous namespace)::DeleteTargetSpecOp]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::HashableOpInterface::Trait<Empty>]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::HashableOpInterface]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::InterpolationModeAttr]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::SamplingModeAttr]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::ScatterModeAttr]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::detail::FFIImportOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::detail::GetMemberOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::detail::ResizeByScaleOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::detail::ScatterAlongAxisOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::CoreML::detail::SetMemberOpGenericAdaptorBase::Properties]"
+ "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::ODIE::Compiler::HashableAttrInterface]"
+ "Unable to get value of constant axis"
+ "alignInBits"
+ "along"
+ "asShim"
+ "call_stack"
+ "coreml.avg_pool_3d"
+ "coreml.bitwise_and"
+ "coreml.bitwise_or"
+ "coreml.bitwise_xor"
+ "coreml.conv3d"
+ "coreml.conv_transpose2d"
+ "coreml.conv_transpose3d"
+ "coreml.cumsum"
+ "coreml.decomposable.batch_to_space"
+ "coreml.decomposable.depth_to_space"
+ "coreml.decomposable.space_to_batch"
+ "coreml.gather_along_axis"
+ "coreml.interpolation_mode"
+ "coreml.keep_placeholder"
+ "coreml.keep_placeholder requested"
+ "coreml.llo.ffi.import"
+ "coreml.llo.get_member"
+ "coreml.llo.set_member"
+ "coreml.max_pool_3d"
+ "coreml.resize_by_scale"
+ "coreml.round"
+ "coreml.sampling_mode"
+ "coreml.scatter_along_axis"
+ "coreml.scatter_mode"
+ "coremlax.image_constraints"
+ "could not resolve "
+ "custom parser failed to parse parameter 'rowAlignmentsPerPlane'"
+ "expect "
+ "expected exactly 4 operands"
+ "expected keyword for An enum corresponding to the backing type to be used for allocations of image types."
+ "failed to parse CMLAX_ImageConstraints parameter 'backing' which is to be a `ImageContainerTypeEnum`"
+ "failed to parse CMLAX_ImageConstraints parameter 'fourCC' which is to be a `::llvm::StringRef`"
+ "failed to parse InterpolationModeAttr parameter 'value' which is to be a `mlir::ODIE::Compiler::CoreML::InterpolationMode`"
+ "failed to parse SamplingModeAttr parameter 'value' which is to be a `mlir::ODIE::Compiler::CoreML::SamplingMode`"
+ "failed to parse ScatterModeAttr parameter 'value' which is to be a `mlir::ODIE::Compiler::CoreML::ScatterMode`"
+ "failed to verify that Result 0 and operand 1 must have the same rank."
+ "fourCC"
+ "getting a member of type "
+ "half_pixel"
+ "image_constraints"
+ "input must have the same rank as indices, but got input with rank "
+ "input rank must be >= 1, but got "
+ "internal.instance_norm"
+ "invalid An enum corresponding to the backing type to be used for allocations of image types. specification: "
+ "keep dims argument should contain a single bool"
+ "member"
+ "mlir::ODIE::Compiler::CoreML::InterpolationMode"
+ "mlir::ODIE::Compiler::CoreML::SamplingMode"
+ "mlir::ODIE::Compiler::CoreML::ScatterMode"
+ "must have a valid SymbolRefAttr to flatten"
+ "nearest_neighbor"
+ "padding must be <= kernel_size / "
+ "requires attribute 'interpolation_mode'"
+ "requires attribute 'member'"
+ "requires attribute 'path'"
+ "requires attribute 'sampling_mode'"
+ "requires attribute 'symbolsToImport'"
+ "rowAlignmentsPerPlane"
+ "scatter_mode"
+ "shim"
+ "shim "
+ "symbolsToImport"
- " expect result rank to be "
- "BasicNeuralNetworkSubroutines-1835~189"
- "ENABLE_ODIE_COREMLAX_COPY_FOLDING"
- "StringRef llvm::detail::getTypeNameImpl() [DesiredTypeName = mlir::OpTrait::ODIE::Compiler::CoreML::KernelNotImplemented<Empty>]"
- "expect exactly two elements for "
- "expect two elements in dilation"
- "expect two elements in padding"
- "expect two elements in strides"

```
