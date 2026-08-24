## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray`

```diff

-130.0.15.0.0
-  __TEXT.__text: 0x12d014
+130.0.19.0.0
+  __TEXT.__text: 0x10d750
   __TEXT.__objc_methlist: 0x7274
-  __TEXT.__const: 0x8ac40
-  __TEXT.__gcc_except_tab: 0x4760
-  __TEXT.__cstring: 0x13002
-  __TEXT.__oslogstring: 0x13
-  __TEXT.__unwind_info: 0x1ab0
+  __TEXT.__const: 0x928e0
+  __TEXT.__gcc_except_tab: 0x4b5c
+  __TEXT.__cstring: 0x13148
+  __TEXT.__oslogstring: 0x27
+  __TEXT.__unwind_info: 0x1b50
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17d0
+  __DATA_CONST.__objc_selrefs: 0x17d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x358

   __AUTH_CONST.__cfstring: 0x9280
   __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0x9c4
-  __DATA.__bss: 0x648
+  __DATA.__bss: 0x638
   __DATA_DIRTY.__objc_data: 0x54b0
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2463
-  Symbols:   5524
-  CStrings:  1689
+  Functions: 2466
+  Symbols:   5532
+  CStrings:  1708
 
Symbols:
+ -[MPSNDArrayAffineInt4Dequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution2D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution2DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution2DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution3D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution3DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayConvolution3DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayFourierTransform workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayHammingDistanceKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayIdentity workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayLUTGEMV workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayMaterializeSparseTensor workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayMatrixMultiplicationGradient workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayMatrixMultiplicationSparse workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayMultiaryBase workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayPoolingKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayQuantizedMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayStencilKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayStitchedReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ -[MPSNDArrayVectorLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:]
+ .str
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table129
+ GCC_except_table139
+ GCC_except_table15
+ GCC_except_table150
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table57
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table99
+ _MPSIsPerfTestCmdSignpostEnabled
+ __Z42MPSKernelEncodeSignpostPerfTestCommandlinePK24MPSNDArrayMultiaryKernelPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEESB_PU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZL12getArrayType11MPSDataType
+ __ZL33MPSKernelBuildPerfTestCommandlinePK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_b
+ __ZL35MPSNDArrayConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEbPU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZL37MPSNDArrayConvolution3DLogCommandLineP24MPSNDArrayMultiaryKernelR30NDArrayConvolution3DEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEPU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZL44MPSNDArrayQuantizedConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEbPU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZN19MPSSignpostMetadata3addIyEERS_PKcT_
+ __ZN29MPSWorkloadStatsEventSignpostC2ERK19MPSSignpostMetadata
+ _matmulA18STable
+ _objc_msgSend$globalTraceObjectID
+ _objc_msgSend$workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:encoder:
- -[MPSNDArrayAffineInt4Dequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution2D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution2DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution2DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution3D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution3DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayConvolution3DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayFourierTransform workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayFusedDepthwisePointwiseConvolution workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayHammingDistanceKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayIdentity workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayLUTGEMV workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayMaterializeSparseTensor workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayMatrixMultiplicationGradient workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayMatrixMultiplicationSparse workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayMultiaryBase workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayPoolingKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayQuantizedMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayQuantizedScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayStencilKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayStitchedReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- -[MPSNDArrayVectorLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
- GCC_except_table114
- GCC_except_table128
- GCC_except_table138
- GCC_except_table149
- GCC_except_table16
- GCC_except_table25
- GCC_except_table32
- GCC_except_table35
- GCC_except_table40
- GCC_except_table55
- GCC_except_table60
- GCC_except_table66
- GCC_except_table74
- GCC_except_table76
- GCC_except_table84
- GCC_except_table98
- __ZL33EncodeTextureMatrixMultiplicationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
- __ZL35MPSNDArrayConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEb
- __ZL37MPSNDArrayConvolution3DLogCommandLineP24MPSNDArrayMultiaryKernelR30NDArrayConvolution3DEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEE
- __ZL44MPSNDArrayQuantizedConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEb
- __ZN28MPSKernelEncodeEventSignpostC2ERK19MPSSignpostMetadata
- __ZZL28EncodeMatrixMultiplyQ4IntoQ8PKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE9predicate
- _objc_msgSend$workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:
CStrings:
+ "AffineInt4Dequantize"
+ "EncoderID"
+ "FourierTransform"
+ "FusedDepthwisePointwiseConvolution"
+ "HammingDistance"
+ "Identity"
+ "LUTDequantize"
+ "LUTGEMV"
+ "MPSPerfTestCmdline"
+ "MPSWorkloadStats"
+ "MaterializeSparseTensor"
+ "MatrixMultiplicationSparse"
+ "PerfTestCmdline"
+ "Pooling"
+ "QuantizedMatrixMultiplication"
+ "QuantizedScaledDotProductAttention"
+ "Reduction"
+ "Stencil"
+ "StitchedReduction"
+ "VectorLUTDequantize"
- "MPSKernelEncode"
```
