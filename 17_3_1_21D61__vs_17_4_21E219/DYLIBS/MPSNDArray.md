## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-127.1.3.0.0
-  __TEXT.__text: 0x7ae58
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x5dd4
-  __TEXT.__const: 0x42d00
-  __TEXT.__gcc_except_tab: 0x1f14
-  __TEXT.__cstring: 0x8520
-  __TEXT.__unwind_info: 0x15b8
-  __TEXT.__eh_frame: 0xac
-  __TEXT.__objc_classname: 0x1a29
-  __TEXT.__objc_methname: 0x5533
-  __TEXT.__objc_methtype: 0x1c49
-  __TEXT.__objc_stubs: 0x2480
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0xaa60
-  __DATA_CONST.__objc_classlist: 0x7c0
+127.4.8.0.0
+  __TEXT.__text: 0xc16cc
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_methlist: 0x6324
+  __TEXT.__const: 0x43320
+  __TEXT.__gcc_except_tab: 0x28dc
+  __TEXT.__cstring: 0x9935
+  __TEXT.__unwind_info: 0x1668
+  __TEXT.__eh_frame: 0x98
+  __TEXT.__objc_classname: 0x1b65
+  __TEXT.__objc_methname: 0x5d9b
+  __TEXT.__objc_methtype: 0x1d36
+  __TEXT.__objc_stubs: 0x2960
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0xc0f0
+  __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x58c0
-  __DATA_CONST.__objc_selrefs: 0x1020
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH_CONST.__const: 0x78
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x410
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xf8
-  __DATA.__objc_superrefs: 0x798
-  __DATA.__objc_ivar: 0x5c0
-  __DATA.__data: 0x348
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__const: 0x30d0
+  __DATA_CONST.__objc_const: 0x5df0
+  __DATA_CONST.__objc_selrefs: 0x11c8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x7e8
+  __AUTH_CONST.__const: 0xb20
+  __AUTH_CONST.__cfstring: 0x4e40
+  __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_ptr: 0x38
+  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x610
+  __DATA.__data: 0x308
+  __DATA.__bss: 0xb0
+  __DATA_DIRTY.__const: 0x3140
   __DATA_DIRTY.__objc_const: 0x81a8
   __DATA_DIRTY.__objc_data: 0x4c40
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1989
-  Symbols:   708
-  CStrings:  2042
+  Functions: 2066
+  Symbols:   760
+  CStrings:  2282
 
Symbols:
+ OBJC_IVAR_$_MPSNDArray._rowElements
+ OBJC_IVAR_$_MPSNDArray._strideElements
+ _OBJC_CLASS_$_MPSKernelUserDAGInfo
+ _OBJC_CLASS_$_MPSKernelUserDAGObject
+ _OBJC_CLASS_$_MPSNDArrayAffineInt4Dequantize
+ _OBJC_CLASS_$_MPSNDArrayLUTDequantize
+ _OBJC_CLASS_$_MPSNDArrayLUTGEMV
+ _OBJC_CLASS_$_MPSNDArrayLUTQuantizationDescriptor
+ _OBJC_CLASS_$_MPSNDArrayMaterializeSparseTensor
+ _OBJC_CLASS_$_MPSNDArrayScaledDotProductAttention
+ _OBJC_CLASS_$_MPSNDArrayStitchedReduction
+ _OBJC_CLASS_$_MPSNDArrayStitchedReductionDescriptor
+ _OBJC_CLASS_$_MPSNDArrayStitchedReductionRMSNorm
+ _OBJC_CLASS_$_MPSNDArrayStitchedReductionSoftmax
+ _OBJC_CLASS_$_MPSUserDAGStitchableOperation
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_METACLASS_$_MPSNDArrayAffineInt4Dequantize
+ _OBJC_METACLASS_$_MPSNDArrayLUTDequantize
+ _OBJC_METACLASS_$_MPSNDArrayLUTGEMV
+ _OBJC_METACLASS_$_MPSNDArrayLUTQuantizationDescriptor
+ _OBJC_METACLASS_$_MPSNDArrayMaterializeSparseTensor
+ _OBJC_METACLASS_$_MPSNDArrayScaledDotProductAttention
+ _OBJC_METACLASS_$_MPSNDArrayStitchedReduction
+ _OBJC_METACLASS_$_MPSNDArrayStitchedReductionDescriptor
+ _OBJC_METACLASS_$_MPSNDArrayStitchedReductionRMSNorm
+ _OBJC_METACLASS_$_MPSNDArrayStitchedReductionSoftmax
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
+ __ZN12MPSKernelDAG12denaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14novenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14octonaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG14undenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG15duodenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG15septenaryCoreOpEP10BaseTensorS1_S1_S1_S1_S1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN13MPSAutoBuffer14AllocateBufferEP8NSString
+ __ZN16MPSKernelUserDAG10constantOpEf11MPSDataType
+ __ZN16MPSKernelUserDAG10constantOpEx11MPSDataType
+ __ZN16MPSKernelUserDAG11assignStateEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG11greaterThanEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG11subtractionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG12toValueCoordEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG14fromValueCoordEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG14multiplicationEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG17reverseSquareRootEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG22readStateFromReferenceEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG25assignStateFromValueCoordEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG25getMTLStitchingInputNodesEm
+ __ZN16MPSKernelUserDAG3expEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN16MPSKernelUserDAG6selectEP20MPSKernelUserDAGNodeS1_S1_11MPSDataType
+ __ZN16MPSKernelUserDAG8additionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG8divisionEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZN16MPSKernelUserDAG9readStateEP20MPSKernelUserDAGNodeS1_11MPSDataType
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
+ __ZTV16MPSKernelUserDAG
+ _objc_retain_x22
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_m
- __ZN12MPSKernelDAG6castOpEP10BaseTensorRKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "-functionName rmsnorm "
+ "-functionName softmax "
+ "-quantizationScheme "
+ "-runMode dataGrad "
+ "-runMode dataGradNew "
+ "-test MPSNDArrayScatterNDTest -srcShapes [%u,%u,%u,%u] [%u,%u,%u,%u] [%u,%u,%u,%u] -dstShapes [%u,%u,%u,%u] -srcDataTypes %s %s %s -dstDataTypes %s -scatterMode %s\n"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
+ "@\"MPSKernelUserDAGInfo\""
+ "@\"MPSNDArrayAffineQuantizationDescriptor\""
+ "@\"MPSNDArrayLUTGEMV\""
+ "@28@0:8I16@20"
+ "@28@0:8I16B20B24"
+ "@32@0:8@16B24B28"
+ "@36@0:8@16Q24f32"
+ "@36@0:8I16B20B24B28B32"
+ "@40@0:8@16@24Q32"
+ "@40@0:8@16Q24@32"
+ "@56@0:8Q16@?24@?32@?40@?48"
+ "@?"
+ "@?16@0:8"
+ "A and B Batch0 must match"
+ "A and B Batch1 must match"
+ "AScale dimension length has to be divisible by A"
+ "ArrayMaterializeSparseTensor"
+ "At least one of the matrix should be quantized to i4"
+ "At most one of the matrix should be quantized to i4"
+ "BScale dimension length has to be divisible by B"
+ "Batch dimension mismatch %lu vs %lu"
+ "Double quantization requires original scale to be MPSDataTypeInt8"
+ "Double quantization requires second scale to be MPSDataTypeFloat16 or MPSDataTypeFloat32"
+ "Error: unsupported input/output datatypes to MPSNDArrayMatrixMultiplication kernel"
+ "Fastest moving dimension of int4 quantized matrix should be aligned to 4-byte"
+ "Fastest moving dimension of int4 quantized zero-point array should be byte aligned"
+ "Inner dimnension of matrices must match, %d vs %d"
+ "Invalid data type for %@."
+ "Invalid shape for %@ LUT"
+ "Invalid shape for %@ Min."
+ "Invalid shape for %@ MinScale."
+ "Invalid shape for %@ NDArray."
+ "Invalid shape for %@ Scale."
+ "Invalid shape for %@ ScaleScale."
+ "Invalid shape for %@ ZeroPoint."
+ "Invalid shape for %@."
+ "Invalid shape for A NDArray."
+ "Invalid shape for B NDArray."
+ "Invalid transpose"
+ "Kernel sources > 12, means we need to add another kernelDAG coreOp, file a radar please"
+ "MPSNDArrayAffineInt4Dequantize"
+ "MPSNDArrayFourierTransform works only with float inputs."
+ "MPSNDArrayI4Quantized::NDArrayDequantizeInt4"
+ "MPSNDArrayI4Quantized::NDArrayI4MatrixMultiplyKContiguous"
+ "MPSNDArrayI4Quantized::NDArrayVectorMatrixMultiplyI4"
+ "MPSNDArrayI4Quantized::NDArrayVectorMatrixMultiplyI4KContiguous"
+ "MPSNDArrayI4Quantized::NDArrayVectorMatrixReduction"
+ "MPSNDArrayLUTDequantize"
+ "MPSNDArrayLUTDequantizeTest"
+ "MPSNDArrayLUTGEMV"
+ "MPSNDArrayLUTGEMVTest"
+ "MPSNDArrayLUTQuantizationDescriptor"
+ "MPSNDArrayMaterializeSparseTensor"
+ "MPSNDArrayQuantizationSchemeAffineAsymmetric"
+ "MPSNDArrayQuantizationSchemeAffineAsymmetricWithMinVal"
+ "MPSNDArrayQuantizationSchemeAffineSymmetric"
+ "MPSNDArrayQuantizationSchemeAffineSymmetricWithMinVal"
+ "MPSNDArrayQuantizationSchemeNone"
+ "MPSNDArrayQuantizedMatMulTest"
+ "MPSNDArrayScaledDotProductAttention"
+ "MPSNDArrayStitchedReduction"
+ "MPSNDArrayStitchedReductionDescriptor"
+ "MPSNDArrayStitchedReductionRMSNorm"
+ "MPSNDArrayStitchedReductionSoftmax"
+ "MPSNDArrayStitchedReductionTest"
+ "Matrix should be int4 quantized"
+ "Maximum left matrix dimensionality allowed is 3"
+ "Maximum right matrix dimensionality allowed is 3"
+ "NDArrayQuantizedMatmul"
+ "NDArrayQuantizedMatmul_int8Affine"
+ "NDArrayVectorMatrixMultiplyPerTensor"
+ "Only rank 3 matmul supported"
+ "Only rank 4 affine dequant supported"
+ "Q88@?0@\"MPSNDArray\"816Q80"
+ "T@\"NSArray\",C,N,V_vectorAxes"
+ "T@\"NSString\",?,R,C"
+ "T@?,N,V_invariantValueFn"
+ "T@?,N,V_mapFn"
+ "T@?,N,V_reduceFn"
+ "T@?,N,V_writeFn"
+ "TB,N,V_hasDoubleQuantMinVal"
+ "TB,N,V_hasDoubleQuantScale"
+ "TB,N,V_hasLUTLHS"
+ "TB,N,V_hasLUTRHS"
+ "TB,N,V_hasMinValue"
+ "TB,N,V_hasZeroPoint"
+ "TB,N,V_signedAsUnsigned"
+ "TI,N,V_sparseFormat"
+ "TQ,N,V_stateSize"
+ "Tf,N,V_alpha"
+ "Tf,N,V_epsilon"
+ "Ti,R,N,V_kernelType"
+ "Unsupported LUT quantization. Expecting 0 or 1 axes."
+ "Unsupported datatype"
+ "Vector should be half/fp16"
+ "[%@ encode...] Invalid LUT - should be 4 or 8 bits"
+ "[%@ encode...] LUTGEMV kernel dimension mismatch - dest[%d] = %d, srcA[%d] = %d"
+ "[%@ encode...] LUTGEMV kernel dimension mismatch - dest[%d] = %d, srcB[%d] = %d"
+ "[%@ encode...] LUTGEMV kernel dimension mismatch - dest[0] = %d, srcB[0] = %d"
+ "[%@ encode...] LUTGEMV kernel dimension mismatch - dest[1] = %d, srcA[1] = %d"
+ "[%@ encode...] LUTGEMV kernel dimension mismatch - srcA[0] = %d, srcB[1] = %d"
+ "\\[0\\]"
+ "\\[1\\]"
+ "\\[2\\]"
+ "\\[3\\]"
+ "_DAGInfo"
+ "_epsilon"
+ "_hasDoubleQuantMinVal"
+ "_hasDoubleQuantScale"
+ "_hasLUTLHS"
+ "_hasLUTRHS"
+ "_hasMinValue"
+ "_hasZeroPoint"
+ "_invariantValueFn"
+ "_lutGEMVKernel"
+ "_mapFn"
+ "_quantizationDescriptor"
+ "_reduceFn"
+ "_signedAsUnsigned"
+ "_sparseFormat"
+ "_stateSize"
+ "_vectorAxes"
+ "_writeFn"
+ "add"
+ "allValues"
+ "context length for input mask does not match the context length of K"
+ "context length for input tensor Q must be 1, the kernel does not yet support training"
+ "context length for input tensor V does not match the context length of K"
+ "context length of input mask does not match the context length of Q"
+ "could not find index 0 in the placeholder list"
+ "could not find index 1 in the placeholder list"
+ "could not find index 2 in the placeholder list"
+ "could not find index 3 in the placeholder list"
+ "denaryCoreOp"
+ "dictionary"
+ "dimension mismatch"
+ "div"
+ "doubleQuant channelsPerGroup must be a multiple of 4"
+ "duodenaryCoreOp"
+ "epsilon"
+ "error: unsupported scaled dot product attention kernel type"
+ "fastest moving dim has to be among lower 4 dimensions"
+ "feature length for input K does not match the feature length of Q"
+ "feature length for input tensor V does not match the feature length of Q"
+ "getDQuantMinValIndex"
+ "getDQuantScaleIndex"
+ "getLeftDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getLeftDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getLeftMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getLeftScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getLeftZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getMTLStitchingGraph"
+ "getMinValIndex"
+ "getNDArrayCount"
+ "getRightDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getRightDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getRightMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getRightScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getRightZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getScaleIndex"
+ "getUserDAGInfo"
+ "getVisibleFunctions"
+ "getZeroPointIndex"
+ "gpuAddress"
+ "group size in fastest moving dimension should be multiple of 8"
+ "hasDoubleQuantMinVal"
+ "hasDoubleQuantScale"
+ "hasLUTLHS"
+ "hasLUTRHS"
+ "hasMinValue"
+ "hasZeroPoint"
+ "indices not found."
+ "initWithDataType:hasZeroPoint:hasMinValue:"
+ "initWithDataType:hasZeroPoint:hasMinValue:hasDoubleQuantScale:hasDoubleQuantMinVal:"
+ "initWithDataType:vectorAxes:"
+ "initWithDevice:axis:descriptor:"
+ "initWithDevice:axis:epsilon:"
+ "initWithDevice:hasLUTLHS:hasLUTRHS:"
+ "initWithDevice:quantizationDescriptor:sourceCount:"
+ "initWithFunctionName:"
+ "initWithKernelUserDAG:"
+ "initWithMTLStitchingGraphs:visibleFunctions:stitchedFunctions:"
+ "initWithStateSize:invariantValueFn:mapFn:reduceFn:writeFn:"
+ "invariantValueFn"
+ "left vector should unquantized"
+ "mapFn"
+ "matrix index out of bound"
+ "matrix is nil"
+ "matrix slice length mismatch"
+ "matrix slice length should be multiple of minval slice length"
+ "matrix slice length should be multiple of scale slice length"
+ "matrix slice length should be multiple of zeropoint slice length"
+ "max"
+ "maxComputeThreadgroupMemory"
+ "maxThreadgroupMemoryLength"
+ "min"
+ "minVal and matrix dimension order should match"
+ "minVal should be half or float"
+ "minval index out of bound"
+ "minval is nil"
+ "minval slice length mismatch"
+ "mmul_kernel_a16_bfloat_bfloat_float"
+ "mmul_kernel_a16_bfloat_float_float"
+ "mmul_kernel_a16_float_bfloat_float"
+ "mmul_kernel_a16_float_float_float"
+ "mmul_kernel_a16_float_half_float"
+ "mmul_kernel_a16_half_float_float"
+ "mmul_kernel_a16_half_half_float"
+ "mul"
+ "ndArrayFFTRadix8"
+ "ndArrayFFTRadix8_half"
+ "ndArrayLUTGEMV_xReduce"
+ "ndArrayLUTGEMV_yReduce"
+ "ndArrayLUT_dequantize"
+ "ndArrayLUT_dequantize4BitUnaligned"
+ "novenaryCoreOp"
+ "number of batches for input K does not match the number of batches of Q"
+ "number of batches for input V does not match the number of batches of Q"
+ "number of batches for input mask does not match the number of batches of Q"
+ "number of heads for input K does not match the number of heads of V"
+ "number of heads for input Q needs to be divisible by the number of heads of K"
+ "number of heads for input Q needs to be divisible by the number of heads of V"
+ "number of heads for input mask does not match the number of heads of Q"
+ "octonaryCoreOp"
+ "offset"
+ "only per tensor minVal allowed"
+ "only per tensor scale allowed"
+ "only per tensor zero point allowed"
+ "q32@0:8@16@24"
+ "reduceFn"
+ "reduce_stitched"
+ "reductionStitched::invariantValue_fn"
+ "reductionStitched::map_fn"
+ "reductionStitched::reduce_fn"
+ "reductionStitched::write_fn"
+ "right indices array should be nil for singe source"
+ "right quant descriptor should be nil for singe source"
+ "right vector should be unquantized"
+ "scale and matrix dimension order should match"
+ "scale and min value dimension mismatch"
+ "scale and zero point dimension mismatch"
+ "scale buffer missing"
+ "scale index out of bound"
+ "scale is nil"
+ "scale missing for quantized matrix"
+ "scale should be half or float"
+ "scale slice length mismatch"
+ "sdpa does not currently support all combinations of dimension orders."
+ "sdpa_fwd"
+ "sdpa_scaled_reduction"
+ "septenaryCoreOp"
+ "set"
+ "setEpsilon:"
+ "setHasDoubleQuantMinVal:"
+ "setHasDoubleQuantScale:"
+ "setHasLUTLHS:"
+ "setHasLUTRHS:"
+ "setHasMinValue:"
+ "setHasZeroPoint:"
+ "setInvariantValueFn:"
+ "setMapFn:"
+ "setReduceFn:"
+ "setSignedAsUnsigned:"
+ "setSparseFormat:"
+ "setStateSize:"
+ "setValue:forKey:"
+ "setVectorAxes:"
+ "setWriteFn:"
+ "signedAsUnsigned"
+ "slice length in fastest moving dim has to be even"
+ "slice offset in fastest moving dim has to be even"
+ "source and destination dimension mismatch"
+ "source and destination tensor rank doesnt match"
+ "sparseFormat"
+ "specializedName"
+ "stateSize"
+ "sub"
+ "undenaryCoreOp"
+ "v16@?0@\"NSArray\"8"
+ "v24@0:8@?16"
+ "v24@?0^v8^{MPSKernelUserDAGNode=^^?@}16"
+ "v32@?0^v8^{MPSKernelUserDAGNode=^^?@}16^{MPSKernelUserDAGNode=^^?@}24"
+ "v40@?0^v8^{MPSKernelUserDAGNode=^^?@}16^{MPSKernelUserDAGNode=^^?@}24^{MPSKernelUserDAGNode=^^?@}32"
+ "vectorAxes"
+ "writeFn"
+ "zeroPoint and matrix dimension order should match"
+ "zeropoint index out of bound"
+ "zeropoint is nil"
+ "zeropoint should be Int4"
+ "zeropoint slice length mismatch"
+ "zeropoints should be int4 quantized"
- "@32@0:8I16B20B24B28"
- "@36@0:8I16@20@28"
- "ArrayMatrixMultiplicationSparseTransposeDense"
- "Kernel sources > 4, means we need to add another kernelDAG coreOp, file a radar please"
- "MPSNDArrayMatrixMultiplicationSparse.alpha"
- "MPSNDArrayMatrixMultiplicationSparse.beta"
- "MultiaryMultiDestinationNDArrayBase.ac"
- "MultiaryMultiDestinationNDArrayBase.oc"
- "MultiaryNDArrayBase.properties"
- "NDArrayMatrixMultiplyA16"
- "Plugin Winograd not efficient for small images. Falling back to MPS AMD implementation\n"
- "Plugin does not support fp16 correctly. Falling back to MPS AMD implementation\n"
- "Plugin not efficient for 1x1 f32 conv. Falling back to MPS AMD implementation\n"
- "Plugin only supports 1x1 and 3x3. Falling back to MPS AMD implementation\n"
- "Plugin only supports NCHW. Falling back to MPS AMD implementation\n"
- "Plugin only supports float and half source/destination. Falling back to MPS AMD implementation\n"
- "Plugin only supports float or half source/destination. Falling back to MPS AMD implementation\n"
- "Plugin only supports float source/destination. Falling back to MPS AMD implementation\n"
- "Plugin only supports packed source/destination. Falling back to MPS AMD implementation\n"
- "Plugin only supports source, weights and destination of same datatype. Falling back to MPS AMD implementation\n"
- "Plugin only supports symmetric padding. Falling back to MPS AMD implementation\n"
- "Plugin only supports unit dilation and unit stride. Falling back to MPS AMD implementation\n"
- "Prefix linking not supported by Plugin kernels. Falling back to MPS AMD implementation\n"
- "Quantization descriptor does not match right MPSNDArray quantization type"
- "Quantization kernels do not support GEMM shapes"
- "Quantization kernels do not support K that is not a multiple of 4"
- "Source and weights index not found for plugin kernels."
- "Source or weights or destination are sliced. Plugin doesnt support slicing. Falling back to MPS AMD implementation\n"
- "Source or weights or destination are transposed. Plugin doesnt support transposition. Falling back to MPS AMD implementation\n"
- "T@\"NSArray\",N,V_scale"
- "T@\"NSArray\",N,V_zeroPoint"
- "TB,N,V_isAsymmetric"
- "TB,N,V_isPerChannel"
- "TB,N,V_numGroups"
- "TB,N,V_supportsMinValue"
- "TQ,N,V_sparseRows"
- "_%@"
- "_isAsymmetric"
- "_isPerChannel"
- "_numGroups"
- "_sparseRows"
- "_supportsMinValue"
- "_zeroPoint"
- "cast"
- "castX"
- "initWithDataType:isPerChannel:isAsymmetric:supportsMinValue:"
- "initWithDataType:zeroPoint:scale:"
- "isAsymmetric"
- "isPerChannel"
- "numGroups"
- "numGroups are not a multiple of K"
- "setIsAsymmetric:"
- "setIsPerChannel:"
- "setNumGroups:"
- "setSparseRows:"
- "setSupportsMinValue:"
- "setZeroPoint:"
- "sparseRows"
- "stringByAppendingString:"
- "supportsMinValue"
- "zeroPoint"

```
