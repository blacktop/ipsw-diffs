## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-128.2.0.0.0
-  __TEXT.__text: 0xdd840
+128.4.6.0.0
+  __TEXT.__text: 0xdaae0
   __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x65ec
-  __TEXT.__const: 0x43e50
-  __TEXT.__gcc_except_tab: 0x2dc0
-  __TEXT.__cstring: 0xa702
-  __TEXT.__unwind_info: 0x1748
+  __TEXT.__objc_methlist: 0x69e4
+  __TEXT.__const: 0x440b0
+  __TEXT.__gcc_except_tab: 0x3048
+  __TEXT.__cstring: 0xac3b
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x1bfc
-  __TEXT.__objc_methname: 0x61dc
-  __TEXT.__objc_methtype: 0x1d75
-  __TEXT.__objc_stubs: 0x2b80
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xc4f0
-  __DATA_CONST.__objc_classlist: 0x838
-  __DATA_CONST.__objc_protolist: 0x40
+  __TEXT.__objc_classname: 0x1c3b
+  __TEXT.__objc_methname: 0x6854
+  __TEXT.__objc_methtype: 0x1e06
+  __TEXT.__objc_stubs: 0x2dc0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0xe1b0
+  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a0
+  __DATA_CONST.__objc_selrefs: 0x1430
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x810
+  __DATA_CONST.__objc_superrefs: 0x818
   __AUTH_CONST.__auth_got: 0x4f8
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH_CONST.__const: 0x3a80
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0xe6b8
-  __DATA.__objc_ivar: 0x640
-  __DATA.__data: 0x6b0
-  __DATA.__bss: 0xc8
+  __AUTH_CONST.__const: 0x3b20
+  __AUTH_CONST.__cfstring: 0x57c0
+  __AUTH_CONST.__objc_const: 0xe5d8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x66c
+  __DATA.__data: 0x718
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x5230
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2488
-  Symbols:   784
-  CStrings:  2408
+  Functions: 2150
+  Symbols:   789
+  CStrings:  2483
 
Symbols:
+ OBJC_IVAR_$_MPSNDArrayConvolution2D._autoTuneIteration
+ OBJC_IVAR_$_MPSNDArrayConvolution2D._logNextAutoTuneParams
+ OBJC_IVAR_$_MPSNDArrayConvolution2D._nextAutoTuneIteration
+ _OBJC_CLASS_$_MPSNDArrayQuantizedScaledDotProductAttention
+ _OBJC_METACLASS_$_MPSNDArrayQuantizedScaledDotProductAttention
+ _objc_retain_x20
- _objc_retain_x22
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
+ "@\"MPSNDArrayOffsetIdentity\""
+ "@36@0:8@16i24Q28"
+ "@52@0:8@16i24@28@36@44"
+ "@56@0:8@16@24@32@40Q48"
+ "@60@0:8@16i24@28@36@44Q52"
+ "Failed to extract expected sources from DAG"
+ "Failed to transpose weights"
+ "Invalid quantization descriptors passed to quantized convolution"
+ "MPSAutoTuneKernel"
+ "MPSNDArrayASTCQuantized::NDArrayMatrixMultiplyNT_ASTC"
+ "MPSNDArrayQuantizedScaledDotProductAttention"
+ "MPS_MATMUL_KSPLITS"
+ "MPS_MATMUL_SIMDM"
+ "MPS_MATMUL_SIMDN"
+ "NDArrayI4MatrixMultiplyKContiguousA18"
+ "NDArrayQ4IntoQ8"
+ "NDArrayQuantizedConv"
+ "NDArrayVectorMatrixMultiplyPerTensor_float_activation_float_scale"
+ "NDArrayVectorMatrixMultiplyPerTensor_float_activation_half_scale"
+ "NDArrayVectorMatrixMultiplyPerTensor_half_activation_float_scale"
+ "NDArrayVectorMatrixMultiplyPerTensor_half_activation_half_scale"
+ "Non rectangular strides are not supported by A14 convolution. Falling back.\n"
+ "Q20@0:8B16"
+ "Quantization scheme for Q or K or V should be symmetric. i.e, no zero point or min value"
+ "TB,N"
+ "TB,N,V_logNextAutoTuneParams"
+ "Ti,N,V_layout"
+ "Tq,N"
+ "Tq,N,V_autoTuneIteration"
+ "Using EncodeMatrixMultiplyQ4IntoQ8 encode path\n"
+ "Using EncodeQuantizedMatrixMultiplicationInt8Affine encode path\n"
+ "WARNING: Tile size fixed to 64x32x64 and currently does not support all powers of 2.\n"
+ "[%@ encode...] Invalid quantized A input - should be 4 or 8 bits"
+ "[%@ encode...] Invalid quantized B input - should be 4 or 8 bits"
+ "[%@ encodeToCommandBuffer:] destination: [\n%@]\t is too large for kernel.  Encode failed.\n"
+ "[%@ encodeToCommandBuffer:] source gradient: [\n%@]\t is too large for kernel.  Encode failed.\n"
+ "[%@ encodeToCommandBuffer:] source: [\n%@]\t is too large for kernel.  Encode failed.\n"
+ "_autoTuneIteration"
+ "_kQuantizationDescriptor"
+ "_layout"
+ "_lhsDesc"
+ "_logNextAutoTuneParams"
+ "_nextAutoTuneIteration"
+ "_offsetKernel"
+ "_qQuantizationDescriptor"
+ "_rhsDesc"
+ "_vQuantizationDescriptor"
+ "_zeroOffsetsArray"
+ "advanceAutoTuneIteration"
+ "autoTuneIteration"
+ "depthwiseConvGradData_k4x4_s2x2_2Sources_cFirst"
+ "depthwiseConvGradData_k4x4_s2x2_cFirst"
+ "getDQuantMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "getDQuantScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "getDestContiguousFunctionConstant:"
+ "getLUTIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "getMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "getRightLUTIndexWithLeftLUTQuantizationDescriptor:rightQuantizationDescriptor:"
+ "getScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "getZeroPointIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:"
+ "initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:"
+ "initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:"
+ "initWithDevice:kernelType:sourceCount:"
+ "initWithDevice:lhsDesc:rhsDesc:"
+ "initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:"
+ "initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:sourceCount:"
+ "initWithDevice:ndArrayConvolution2DDescriptor:sourceCount:"
+ "initWithDevice:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:"
+ "layout"
+ "logNextAutoTuneParams"
+ "maxSupportedArraySizeForIsDestination:"
+ "ndArrayConvolution2DGradientWithWeights_bfloat_bfloat"
+ "ndArrayConvolution2DGradientWithWeights_float_float"
+ "ndArrayConvolution2DGradientWithWeights_half_half"
+ "only half vector data type supported"
+ "q36@0:8@16@24B32"
+ "sdpa_tile_fwd"
+ "setAutoTuneIteration:"
+ "setDynamicFCs:"
+ "setLayout:"
+ "setLogNextAutoTuneParams:"
+ "the inner most dimension (ie., %lu) is not a multiple of zpElemsPerByte %lu, nor 1"
+ "usesVectorFunctionsOnOutput:"
+ "v24@?0@\"MPSNDArray\"8@\"MPSNDArray\"16"
- "MPSNDArrayASTCQuantized::NDArrayMatrixMultiplyNT_ASTC_uint"
- "MPSNDArrayASTCQuantized::NDArrayMatrixMultiplyNT_ASTC_ushort"
- "MPSNDArrayI4Quantized::NDArrayI4MatrixMultiplyKContiguous_bfloat"
- "MPSNDArrayI4Quantized::NDArrayI4MatrixMultiplyKContiguous_float"
- "MPSNDArrayI4Quantized::NDArrayI4MatrixMultiplyKContiguous_half"
- "NDArrayVectorMatrixMultiplyPerTensor"
- "Using EncodeQuantizedMatrixMultiplication_Int8Affine encode path\n"
- "initWithDevice:ndArrayConvolution2DDescriptor:activationQuantizationDescriptor:weightsQuantizationDescriptor:"
- "ndArrayConvolution2DGradientWithWeightsA14"
- "the inner most dimension (ie., %lu) is not a multiple of zpElemsPerByte %lu"

```
