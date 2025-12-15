## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.2.0.0.0
-  __TEXT.__text: 0x106e88
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x6aac
-  __TEXT.__const: 0x83c18
-  __TEXT.__gcc_except_tab: 0x3f1c
-  __TEXT.__cstring: 0xdcd0
+129.3.2.0.0
+  __TEXT.__text: 0x10c4a8
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x6aa4
+  __TEXT.__const: 0x895e8
+  __TEXT.__gcc_except_tab: 0x4154
+  __TEXT.__cstring: 0xe2e2
   __TEXT.__unwind_info: 0x1878
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6c90
-  __TEXT.__objc_methtype: 0x1ec3
-  __TEXT.__objc_stubs: 0x32e0
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0xedb0
+  __TEXT.__objc_methname: 0x6d11
+  __TEXT.__objc_methtype: 0x1ed4
+  __TEXT.__objc_stubs: 0x3360
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0xedd0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1558
+  __DATA_CONST.__objc_selrefs: 0x1570
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x3fe0
-  __AUTH_CONST.__cfstring: 0x6be0
-  __AUTH_CONST.__objc_const: 0xe8b8
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0x4080
+  __AUTH_CONST.__cfstring: 0x6f80
+  __AUTH_CONST.__objc_const: 0xe8d8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6ac
+  __DATA.__objc_ivar: 0x6b0
   __DATA.__data: 0x9c4
-  __DATA.__bss: 0x5d8
+  __DATA.__bss: 0x608
   __DATA_DIRTY.__objc_data: 0x5280
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore
+  - /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSHost.framework/MPSHost
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AFADED6-1B40-3682-9E72-F21B84A32C4C
-  Functions: 2240
-  Symbols:   7540
-  CStrings:  3670
+  UUID: CA3D151C-4BD7-32C7-8D71-0FB3E2EA2891
+  Functions: 2244
+  Symbols:   7571
+  CStrings:  3745
 
Symbols:
+ -[MPSNDArrayConvolution2D encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayQuantizedConvolution encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayScaledDotProductAttention encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:sourceCount:]
+ GCC_except_table100
+ GCC_except_table120
+ GCC_except_table14
+ GCC_except_table141
+ GCC_except_table24
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table56
+ GCC_except_table65
+ GCC_except_table90
+ _OBJC_CLASS_$_MPSNDArrayConvolution2DGradientWithInputHost
+ _OBJC_CLASS_$_MPSNDArrayConvolution2DGradientWithWeightsHost
+ _OBJC_CLASS_$_MPSNDArrayConvolution2DHost
+ _OBJC_CLASS_$_MPSNDArrayDepthwiseConvolutionKernelHost
+ _OBJC_CLASS_$_MPSNDArrayHammingDistanceKernelHost
+ _OBJC_CLASS_$_MPSNDArrayMatrixMultiplicationGradientHost
+ _OBJC_CLASS_$_MPSNDArrayMatrixMultiplicationHost
+ _OBJC_CLASS_$_MPSNDArrayMultiaryBaseHost
+ _OBJC_CLASS_$_MPSNDArrayQuantizedScaledDotProductAttentionHost
+ _OBJC_CLASS_$_MPSNDArrayScaledDotProductAttentionHost
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._srcDataFormat
+ __MergedGlobals.1
+ __MergedGlobals.13
+ __Z12setDTypeEnum11MPSDataType
+ __Z25_A18HeuristicFor10CoreGPUR22MPSNDArrayA18MatMulKeyP32MPSMatMulAutoTuningParametersA18
+ __ZL10splitAliasPU27objcproto16MTLCommandBuffer11objc_objectPK10MPSNDArrayDv16_jmS4_
+ __ZL15canAliasToShapePK10MPSNDArrayDv16_jmRS2_Rb
+ __ZN12MPSKernelDAG12getDimSizeOpEmRKNSt3__16vectorIlNS0_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG13greaterThanOpEP10BaseTensorS1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG13subtractionOpEP10BaseTensorS1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG15getCoordValueOpEmRKNSt3__16vectorIlNS0_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG6castOpEP10BaseTensorRKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG8selectOpEP10BaseTensorS1_S1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN29MPSNDArrayScanDeviceBehaviorsD0Ev
+ __ZN29MPSNDArrayScanDeviceBehaviorsD1Ev
+ __ZNK29MPSNDArrayScanDeviceBehaviors10getThreadsEv
+ __ZNK29MPSNDArrayScanDeviceBehaviors17EncodeNDArrayScanEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringm23MPSNDArrayScanOperationmbb
+ __ZNK30MPSNDArrayMatMulDeviceBehavior30EncodeArrayMultiplyI4I2IntoF16EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior33GetKernelDispatchParametersForKeyEP9MPSKernelR22MPSNDArrayA18MatMulKeyP32MPSMatMulAutoTuningParametersA18
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior29DoInputsNeedPhysicalTransposeEP10MPSNDArrayP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1429DoInputsNeedPhysicalTransposeEP10MPSNDArrayP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1829DoInputsNeedPhysicalTransposeEP10MPSNDArrayP28NDArrayConvolutionEncodeData
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZTV29MPSNDArrayScanDeviceBehaviors
+ __ZZ135-[MPSNDArrayScaledDotProductAttention encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]ENK3$_0clEP10MPSNDArray
+ __ZZNK30MPSNDArrayMatMulDeviceBehavior30EncodeArrayMultiplyI4I2IntoF16EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE5table
+ ____ZL20MPSSDPAForceFallbackv_block_invoke
+ ____ZL28MPSSDPAAllowReducedPrecisionv_block_invoke
+ ____ZN33MPSNDArrayMatMulA18DeviceBehaviorC2EP9MPSDevicey_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_literal_global.190
+ ___block_literal_global.193
+ ___block_literal_global.196
+ ___block_literal_global.238
+ ___block_literal_global.269
+ ___block_literal_global.272
+ ___block_literal_global.315
+ ___block_literal_global.318
+ ___block_literal_global.342
+ ___block_literal_global.407
+ ___block_literal_global.440
+ _matmulA18CTable
+ _matmulA18GTable
+ _matmulI4A18CTable
+ _matmulI4A18GTable
+ _objc_msgSend$initWithDevice:kernelType:maskType:
+ _objc_msgSend$normFusionDescriptor
+ _objc_msgSend$supportsPostfixForDevice:environment:
+ _objc_msgSend$supportsPrefixForDevice:environment:
- -[MPSNDArrayMatrixMultiplication advanceAutoTuneIteration]
- -[MPSNDArrayMatrixMultiplication autoTuneIteration]
- -[MPSNDArrayMatrixMultiplication logNextAutoTuneParams]
- -[MPSNDArrayMatrixMultiplication setAutoTuneIteration:]
- -[MPSNDArrayMatrixMultiplication setLogNextAutoTuneParams:]
- GCC_except_table103
- GCC_except_table105
- GCC_except_table118
- GCC_except_table12
- GCC_except_table139
- GCC_except_table15
- GCC_except_table30
- GCC_except_table38
- GCC_except_table43
- GCC_except_table46
- GCC_except_table51
- GCC_except_table52
- GCC_except_table55
- GCC_except_table61
- GCC_except_table66
- GCC_except_table88
- __MergedGlobals.18
- __MergedGlobals.3
- __Z43EncodeQuantizedMatrixMultiplicationFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
- __ZL14matmulA18Table
- __ZL15canAliasToShapePK10MPSNDArrayDv16_jm
- __ZL16EncodeScanCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringmjmbb
- __ZL28MPSNDArraySDPALogCommandLineP24MPSNDArrayMultiaryKernelPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
- __ZL30IsOptimizedInt4KernelSupportedPK39MPSNDArrayQuantizedMatrixMultiplicationPK23NDArrayMultiaryCallInfo
- __ZN23MPSNDArrayScanBehaviorsD0Ev
- __ZN23MPSNDArrayScanBehaviorsD1Ev
- __ZNK10BaseTensor19GetDebugDescriptionERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK13BaseOperation22GetNodeIdForBaseTensorERNSt3__13mapIPK10BaseTensorDv2_iNS0_4lessIS4_EENS0_9allocatorINS0_4pairIKS4_S5_EEEEEERiS4_b
- __ZNK13BaseOperation23DebugDescriptionPrivateERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS0_3mapIPK10BaseTensorDv2_iNS0_4lessISB_EENS4_INS0_4pairIKSB_SC_EEEEEERi
- __ZNK23MPSNDArrayScanBehaviors10getThreadsEv
- __ZNK30MPSNDArrayMatMulDeviceBehavior21EncodeArrayMultiplyI4EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
- __ZNSt3__16__treeINS_12__value_typeIPK10BaseTensorDv2_iEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
- __ZNSt3__19to_stringEl
- __ZTV23MPSNDArrayScanBehaviors
- __ZZNK30MPSNDArrayMatMulDeviceBehavior21EncodeArrayMultiplyI4EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE5table
- ___block_literal_global.178
- ___block_literal_global.181
- ___block_literal_global.184
- ___block_literal_global.223
- ___block_literal_global.298
- ___block_literal_global.301
- ___block_literal_global.326
- ___block_literal_global.422
- _winogradA18DTableSize
- _winogradA18GTableSize
- _winogradA19PTableSize
CStrings:
+ "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
+ "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
+ " -queryQuantized "
+ "-test MPSNDArrayInt4Int2Dequantize\n"
+ "@36@0:8@16i24Q28"
+ "At least one of the matrix should be quantized to i4 or i2"
+ "At most one of the matrix should be quantized to i4 or i2"
+ "B scale not found."
+ "Error encoding kernel"
+ "Fasted moving dim slice offset should be aligned to %d"
+ "K dimension is inconsistently defined..."
+ "LORADOWN GEMV Kernel - doKDimTGEdgeCheck can only be true if doKDimTiledTGEdgeCheck is true too."
+ "LORADOWN GEMV Kernel - matrixRowPadElements will overflow its fc bit allocation."
+ "LORADOWN GEMV Kernel - vectorRowPadElements will overflow its fc bit allocation."
+ "LORADOWN GEMV Kernel only supports fp16 datatype."
+ "LORADOWN GEMV kernel - Currently the max tileK is 16."
+ "LORADOWN GEMV kernel - we currently only support power-of-two SIMD Groups."
+ "LORADOWN GEMV kernel does not support M-dimensional edge checking"
+ "LORADOWN_gemv_kernel"
+ "MPSNDARRAY_DIRECTCONV_BARRIER_ITERATIONS"
+ "MPSNDARRAY_DIRECTCONV_LINEARIZETGS"
+ "MPSNDARRAY_SDPA_ALLOW_REDUCED_PRECISION"
+ "MPSNDARRAY_SDPA_FORCE_FALLBACK"
+ "MPSNDArrayI4Quantized::NDArrayDequantizeInt2"
+ "MPS_MATMUL_BARRIER_INSIDE"
+ "MPS_MATMUL_LINEARIZE"
+ "MPS_MATMUL_MORTON"
+ "MPS_MATMUL_RASTER_MBIAS"
+ "Matrix should be either Int2 or Int4 quantized"
+ "Matrix should be int4 or int2 quantized"
+ "USING LORADOWN ENCODER\n"
+ "Using EncodeArrayMultiplyI4I2IntoF16 encode path\n"
+ "X"
+ "Y"
+ "_srcDataFormat"
+ "castToFloat"
+ "conv2d_a18_"
+ "delta"
+ "dimX"
+ "dimY"
+ "float_bfloat_bfloat"
+ "float_bfloat_int8"
+ "float_bfloat_uint8"
+ "float_float8e4m3_float8e4m3"
+ "float_float8e4m3fn_float8e4m3fn"
+ "float_float8e5me_float8e5me"
+ "float_float_float"
+ "float_half_half"
+ "float_half_int8"
+ "float_half_uint8"
+ "float_int8_half"
+ "float_uint8_half"
+ "group size in fastest moving dimension should be multiple of 16"
+ "initWithDevice:kernelType:sourceCount:"
+ "int32_int8_int8"
+ "int32_uint8_int8"
+ "int32_uint8_uint8"
+ "maskValue"
+ "maskZero"
+ "offsetX"
+ "product of simdsx and simdsy must be less than or equal to 32"
+ "qmm_n_16_bfloat"
+ "qmm_n_16_float"
+ "qmm_n_16_half"
+ "qmm_n_64_bfloat"
+ "qmm_n_64_float"
+ "qmm_n_64_half"
+ "qmm_t_16_bfloat"
+ "qmm_t_16_float"
+ "qmm_t_16_half"
+ "qmm_t_64_bfloat"
+ "qmm_t_64_float"
+ "qmm_t_64_half"
+ "qvm_t_bfloat"
+ "qvm_t_float"
+ "qvm_t_half"
+ "scaleT"
+ "simdsx must be less than or equal to 8"
+ "simdsy must be less than or equal to 8"
+ "smallVal"
+ "supportsPostfixForDevice:environment:"
+ "supportsPrefixForDevice:environment:"
+ "theFutureConan?"
+ "tileK must be power of 2 and less than or equal to 64"
+ "tileM must be power of 2 and less than or equal to 256"
+ "tileN must be power of 2 and less than or equal to 256"
+ "vector data type should be bfloat with bfloat scale data type"
+ "vector data type should be float with float scale data type"
+ "vector data type should be half with half scale data type"
+ "zero"
+ "zeropoint should be either Int2 or Int4"
+ "zeropoints should be int2 quantized"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
- "  "
- "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
- " = "
- "%"
- "("
- ")"
- ", "
- "-test MPSNDArrayInt4Dequantize\n"
- ":"
- "At least one of the matrix should be quantized to i4"
- "At most one of the matrix should be quantized to i4"
- "COREOP:"
- "MPSNDArrayLUTGEMVTest"
- "Matrix should be int4 quantized"
- "Using EncodeArrayMultiplyI4 encode path\n"
- "["
- "]"
- "]["
- "conv2d_a18_float_bfloat_bfloat"
- "conv2d_a18_float_float8e4m3_float8e4m3"
- "conv2d_a18_float_float8e4m3fn_float8e4m3fn"
- "conv2d_a18_float_float8e5me_float8e5me"
- "conv2d_a18_float_float_float"
- "conv2d_a18_float_half_half"
- "conv2d_a18_float_half_int8"
- "conv2d_a18_float_half_uint8"
- "conv2d_a18_float_int8_half"
- "conv2d_a18_float_uint8_half"
- "conv2d_a18_int32_int8_int8"
- "conv2d_a18_int32_uint8_int8"
- "conv2d_a18_int32_uint8_uint8"
- "datatype mismatch"
- "fastest moving dim slice offset should be even"
- "matrix is nil"
- "only half/bfloat vector data type supported"
- "product of simdsx and simdsy must be less than or equal to 4"
- "qmm_n_bfloat"
- "qmm_n_float"
- "qmm_n_half"
- "qmm_t_bfloat"
- "qmm_t_float"
- "qmm_t_half"
- "tileK must be power of 2 and less than or equal to 32"
- "tileM must be power of 2 and less than or equal to 128"
- "tileN must be power of 2 and less than or equal to 128"
- "zeropoint is nil"
- "zeropoint should be Int4"
- "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"

```
