## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

 129.0.18.0.0
-  __TEXT.__text: 0xe8fdc
-  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__text: 0x105064
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x6a84
-  __TEXT.__const: 0x44900
-  __TEXT.__gcc_except_tab: 0x38d8
-  __TEXT.__cstring: 0xbb81
-  __TEXT.__unwind_info: 0x17a0
+  __TEXT.__const: 0x746a0
+  __TEXT.__gcc_except_tab: 0x3e80
+  __TEXT.__cstring: 0xd8ef
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6b34
-  __TEXT.__objc_methtype: 0x1e7e
-  __TEXT.__objc_stubs: 0x3160
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0xe9f0
+  __TEXT.__objc_methname: 0x6c21
+  __TEXT.__objc_methtype: 0x1ea9
+  __TEXT.__objc_stubs: 0x32c0
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0xedb0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f8
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x3be0
-  __AUTH_CONST.__cfstring: 0x5d00
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0x3f60
+  __AUTH_CONST.__cfstring: 0x6a40
   __AUTH_CONST.__objc_const: 0xe888
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x6a8
   __DATA.__data: 0x9c0
-  __DATA.__bss: 0x450
+  __DATA.__bss: 0x5b0
   __DATA_DIRTY.__objc_data: 0x5280
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E3E5A49-A6B4-3598-A88E-6233FFA46EAF
-  Functions: 2189
-  Symbols:   7362
-  CStrings:  3347
+  UUID: 50F3B4AF-56AD-39E8-A7BF-F728E7660232
+  Functions: 2232
+  Symbols:   7517
+  CStrings:  3627
 
Symbols:
+ GCC_except_table29
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table66
+ _MPSDisableMatrixUnit
+ _MPSForceMatrixUnit
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSData
+ _OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._identity
+ __MergedGlobals.18
+ __MergedGlobals.31
+ __MergedGlobals.5
+ __OBJC_PROTOCOL_REFERENCE_$_MPSAutoTuneKernel
+ __Z28ndArrayConvDeviceBehaviorA18P9MPSDevicey
+ __Z29MPSNDArraySDPAA18BehaviorCtorP9MPSDevicey
+ __Z30ndArrayA18MatMulDeviceBehaviorP9MPSDevicey
+ __Z34MPSNDArrayVectorCompatibleWithDimsP10MPSNDArrayS0_mmP9MPSDeviceP29MPSMatMulAutoTuningParameters
+ __ZL14matmulA18Table
+ __ZL15a18KernelParams
+ __ZL15directA18CTable
+ __ZL15directA18GTable
+ __ZL15directA18STable
+ __ZL15directA19PTable
+ __ZL17winogradA18CTable
+ __ZL17winogradA18GTable
+ __ZL17winogradA18STable
+ __ZL17winogradA19PTable
+ __ZL21kernelIDToFileNameMap
+ __ZL25EncodeSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttention7MTLSize
+ __ZL33EncodeTextureMatrixMultiplicationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize
+ __ZL43MPSNDArrayConvolutionA18FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL46MPSNDArrayMatrixMultiplyA18FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL50MPSNDArrayMatrixMultiplyI2I8A18FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL51MPSNDArrayConvolutionWinogradA18FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZN12MPSKernelDAG10divisionOpEP10BaseTensorS1_RKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN12MPSKernelDAG12dequantizeOpEP10BaseTensorRKNSt3__16vectorIlNS2_9allocatorIlEEEE11MPSDataTypePKc
+ __ZN25MPSNDArraySDPAA18BehaviorD0Ev
+ __ZN25MPSNDArraySDPAA18BehaviorD1Ev
+ __ZN33MPSNDArrayMatMulA18DeviceBehaviorD0Ev
+ __ZN33MPSNDArrayMatMulA18DeviceBehaviorD1Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA16D2Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA18D0Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA18D1Ev
+ __ZNK25MPSNDArraySDPAA18Behavior10EncodeSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK25MPSNDArraySDPAA18Behavior19EncodeQuantizedSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior19EncodeArrayMultiplyEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior33IsInt8AffineSupportedQuantizationEP46NDArrayQuantizedMatrixMultiplicationEncodeData
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior37IsInt2Int8AffineSupportedQuantizationEP46NDArrayQuantizedMatrixMultiplicationEncodeData
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior45EncodeQuantizedMatrixMultiplicationInt8AffineEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior49EncodeQuantizedMatrixMultiplicationInt2Int8AffineEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1819GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1819IsWinogradSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1821IsIntrinsicsSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1822IsConvolutionSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1823IsQuantizationSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1824EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1830DoWeightsNeedPhysicalTransposeEP10MPSNDArrayS1_P28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1832EncodeNDArrayConvolutionWinogradEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1834EncodeNDArrayConvolutionIntrinsicsEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1841IsConvolutionGradientWithWeightsSupportedEP42MPSNDArrayConvolution2DGradientWithWeightsPK23NDArrayMultiaryCallInfo
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1843EncodeNDArrayConvolutionGradientWithWeightsEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZTV25MPSNDArraySDPAA18Behavior
+ __ZTV33MPSNDArrayMatMulA18DeviceBehavior
+ __ZTV38MPSNDArrayConvolutionDeviceBehaviorA18
+ __ZZL28EncodeMatrixMultiplyQ4IntoQ8PKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE9predicate
+ ____ZL19MPSWinogradForceF16v_block_invoke
+ ____ZL20MPSEnableAutoTuneLogv_block_invoke
+ ____ZL20MPSWinogradForceFP19v_block_invoke
+ ____ZL22MPSSDPAForceMatrixUnitv_block_invoke
+ ____ZL24MPSDisableAutoTuneTablesv_block_invoke
+ ___block_literal_global.298
+ ___block_literal_global.301
+ ___block_literal_global.326
+ ___block_literal_global.418
+ _fprintf
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$newlineCharacterSet
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$recordNode:kernelID:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$writeToURL:atomically:encoding:error:
+ _sscanf
+ _winogradA18DTableSize
+ _winogradA19PTableSize
- GCC_except_table23
- GCC_except_table24
- GCC_except_table30
- GCC_except_table39
- GCC_except_table42
- GCC_except_table44
- GCC_except_table49
- GCC_except_table62
- GCC_except_table91
- __MergedGlobals.30
- ___block_literal_global.374
CStrings:
+ ""
+ "    %@,\n"
+ "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
+ "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
+ "//"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
+ "A scale not found."
+ "A18 Autotuning: Using MXU direct conv\n"
+ "A18 Encoder: Encoding 16x16 MXU based SDPA kernel\n"
+ "A18 Encoder: failed, fall back A14 encoder\n"
+ "A18 Encoder:Encoding 16x16 MXU based QuantizedSDPA kernel\n"
+ "A18 Winograd kernel does not support FP32 precision"
+ "Autotuning params not set"
+ "Convolution inputs are FP32 and MXU is not forced. Falling back to TEC implementation."
+ "Convolution inputs are not supported on MXU. Falling back to TEC implementation."
+ "Direct A18 kernel running auto tune iteration %7ld key with params:    {%s, %s}\n"
+ "Direct A18 kernel running key with params:    {%s, %s}\n"
+ "Direct A18 parameters loaded. %d parameters found"
+ "Error parsing contents of Winograd A18 param table: \n %s %s\n No direct A18 parameters loaded.\n"
+ "Error parsing contents of Winograd A18 param table: \n Provided parameter does not match expected format. \n %s \n No Winograd A18 parameters loaded."
+ "Error parsing contents of direct A18 param table: \n %s %s\n No direct A18 parameters loaded.\n"
+ "Error parsing contents of direct A18 param table: \n Provided parameter does not match expected format. \n %s \n No direct A18 parameters loaded."
+ "Error parsing contents of matmul A18 param table: \n %s %s\n No matmul A18 parameters loaded.\n"
+ "Error parsing contents of matmul A18 param table: \n Provided parameter does not match expected format. \n %s \n No matmul A18 parameters loaded."
+ "Exceeds TG memory limit"
+ "FP8 not supported by device"
+ "Invalid A data type in matmul key"
+ "Invalid auto tune iteration for Direct A18 kernel"
+ "Invalid auto tune iteration for Winograd A18 kernel"
+ "Invalid auto tune iteration for matmul A18 kernel"
+ "Low channels should fall back to generic implementation\n"
+ "MPSNDARRAY_CONV_FORCE_MXU is set to 1. Forcing A18 MXU Winograd using fp19 precision.\n"
+ "MPSNDARRAY_DIRECTCONV_LICMPTRS"
+ "MPSNDARRAY_DIRECTCONV_LM_DATA"
+ "MPSNDARRAY_DIRECTCONV_SIMDSX"
+ "MPSNDARRAY_DIRECTCONV_SIMDSY"
+ "MPSNDARRAY_DIRECTCONV_TG_SWIZZLE"
+ "MPSNDARRAY_DIRECTCONV_TILEK"
+ "MPSNDARRAY_DIRECTCONV_TILEM"
+ "MPSNDARRAY_DIRECTCONV_TILEN"
+ "MPSNDARRAY_SDPA_FORCE_MXU"
+ "MPSNDARRAY_UNROLL_FACTOR"
+ "MPSNDARRAY_WINOGRAD_FP16_INTERMEDIATE"
+ "MPSNDARRAY_WINOGRAD_FP16_INTERMEDIATE is set. Running A18 MXU Winograd using fp16 precision.\n"
+ "MPSNDARRAY_WINOGRAD_FP19_INTERMEDIATE"
+ "MPSNDARRAY_WINOGRAD_FP19_INTERMEDIATE is set. Running A18 MXU Winograd using fp19 precision.\n"
+ "MPSNDArrayA18ConvolutionKey"
+ "MPSNDArrayA18MatMulKey"
+ "MPSNDArrayASTCQuantized::NDArrayMatrixMultiplyNT_ASTC_A18"
+ "MPSNDArrayConvolutionDirectA18"
+ "MPSNDArrayConvolutionWinogradA18"
+ "MPSNDArrayMatMulA18"
+ "MPSNDArrayMatMulI4A18"
+ "MPS_DIRECT_CONV_A18_PARAM_TABLE_PATH"
+ "MPS_DISABLE_AUTO_TUNE_TABLES"
+ "MPS_LOG_AUTO_TUNE"
+ "MPS_MATMUL_A18_PARAM_TABLE_PATH"
+ "MPS_MATMUL_BARRIER_ITERATIONS"
+ "MPS_MATMUL_ELASTIC_BARRIER"
+ "MPS_MATMUL_KSPLITS"
+ "MPS_MATMUL_SIMDM"
+ "MPS_MATMUL_SIMDN"
+ "MPS_MATMUL_TGMEM_SIZE"
+ "MPS_MATMUL_UBERM"
+ "MPS_MATMUL_UBERN"
+ "MPS_MATMUL_UNROLLK"
+ "MPS_MATMUL_UNROLLM"
+ "MPS_MATMUL_UNROLLN"
+ "MPS_WINOGRAD_CONV_A18_PARAM_TABLE_PATH"
+ "MXU explicitly disabled. Falling back to TEC implementation."
+ "MXU not supported on device. Falling back to TEC implementation."
+ "MatMul A18 kernel running auto tune iteration %7ld key with params:    {%s, %s}\n"
+ "MatMul A18 kernel running key with params:    {%s, %s}\n"
+ "Matmul A18 parameters loaded. %d parameters found"
+ "NDArrayI4MatrixMultiplyKContiguousA18"
+ "Non rectangular strides are not supported by A18 convolution. Falling back.\n"
+ "Only FP32, BF16, FP16 or FP8 convolution supported"
+ "Only FP32, BF16, FP16, FP8, I8 and UI8 convolution supported"
+ "Only NHWC and NCHW data formats supported"
+ "Only NHWC or NCHW destination format is supported"
+ "Only NHWC or NCHW source format is supported"
+ "Only supports rank 3"
+ "Only the A18 device behavior should handle the Winograd auto tuning params."
+ "The file \"%s\" does not exist.\n No Winograd A18 parameters loaded.\n"
+ "The file \"%s\" does not exist.\n No direct A18 parameters loaded.\n"
+ "The file \"%s\" does not exist.\n No matmul A18 parameters loaded.\n"
+ "Using MXU Winograd\n"
+ "Using MXU direct conv\n"
+ "Using TEC Winograd\n"
+ "Using TEC direct conv\n"
+ "Winograd A18 kernel running auto tune iteration %7ld key with params:    {%s, %s}\n"
+ "Winograd A18 kernel running key with params:    {%s, %s}\n"
+ "Winograd A18 parameters loaded. %d parameters found"
+ "Winograd parameter GEMMLoops must be less than or equal to batchTilesPerSIMD"
+ "Winograd parameter MortonOrderTileSize must be less than or equal to 4"
+ "Winograd parameter batchTilesPerSIMD must be less than or equal to 8"
+ "Winograd parameter imageTileSize and batchTileSize product must be equal to dataTileSize"
+ "Winograd parameter kernelDataTiles must be less than or equal to 4"
+ "Winograd parameter kernelResultTiles must be less than or equal to 16"
+ "Winograd parameter kernelWeightTiles must be less than or equal to 4"
+ "Winograd parameter selection requires too many registers"
+ "Winograd parameter writeLoops must be less than or equal to kernelResultTiles"
+ "Winograd parameters totalSIMD must be greater than or equal to kernelResultTiles"
+ "Winograd parameters totalSIMD must be less than or equal to 32"
+ "allowReducedPrecision flag is set. Running A18 MXU Winograd using fp16 precision.\n"
+ "batch dimension cannot be inner most"
+ "clearScaleBuffer"
+ "componentsSeparatedByCharactersInSet:"
+ "const %@ nodeTable[] {\n"
+ "conv2d_a18_float_bfloat_bfloat"
+ "conv2d_a18_float_float8e4m3_float8e4m3"
+ "conv2d_a18_float_float8e4m3fn_float8e4m3fn"
+ "conv2d_a18_float_float8e5me_float8e5me"
+ "conv2d_a18_float_float_float"
+ "conv2d_a18_float_half_half"
+ "conv2d_a18_float_half_int8"
+ "conv2d_a18_float_half_uint8"
+ "conv2d_a18_float_int8_half"
+ "conv2d_a18_float_uint8_half"
+ "conv2d_a18_int32_int8_int8"
+ "conv2d_a18_int32_uint8_int8"
+ "conv2d_a18_int32_uint8_uint8"
+ "core"
+ "datatype mismatch"
+ "divide"
+ "fp8 data type should match for A and B"
+ "gemm_a18"
+ "gemm_i2i8_a18"
+ "getBytes:length:"
+ "initWithBytes:length:"
+ "minval and scale datatype should match"
+ "ndArrayConvWinogradGEMMA18"
+ "ndArrayConvWinogradWeightsTransformA18"
+ "ndArrayConvolution2DGradientWithWeights_float8e4m3_float8e4m3"
+ "ndArrayConvolution2DGradientWithWeights_float8e4m3fn_float8e4m3fn"
+ "ndArrayConvolution2DGradientWithWeights_float8e5m2_float8e5m2"
+ "newlineCharacterSet"
+ "no min val allowed for fp8"
+ "no zero point allowed for fp8"
+ "only half vector data type supported"
+ "only per channel and per tensor quantization supported"
+ "only supports NT"
+ "parameter selection error"
+ "product of simdsx and simdsy must be less than or equal to 4"
+ "quant"
+ "quantized data type should be i8/ui8/fp8"
+ "r^{MPSLibraryInfo=iI*^?{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}}24@0:8^v16"
+ "rangeOfString:"
+ "requires multiple of 16 elements in reduction dimension"
+ "scale cannot be nil"
+ "scale data type of A and B must match"
+ "scale should be float for fp8"
+ "scale should be fp16/bf16"
+ "striding in fastest moving dimension not allowed"
+ "stringByAppendingString:"
+ "stringWithContentsOfURL:encoding:error:"
+ "stringWithUTF8String:"
+ "tileK must be power of 2 and less than or equal to 32"
+ "tileM cannot block over simdx for NCHW"
+ "tileM cannot block over simdy for NHWC"
+ "tileM must be power of 2 and less than or equal to 128"
+ "tileN cannot block over simdx for NHWC"
+ "tileN cannot block over simdy for NCHW"
+ "tileN must be power of 2 and less than or equal to 128"
+ "unsupported types for I2I8 affine A18 kernel"
+ "writeToURL:atomically:encoding:error:"
+ "zp and matrix datatype should match"
+ "{"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
+ "}"
+ "};\n"
- "r^{MPSLibraryInfo=iI*^?{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}{MPSDeviceSpecificInfo=^{MPSKernelInfo}^?Q}}24@0:8^v16"

```
