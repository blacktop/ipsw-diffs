## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-128.5.2.0.0
-  __TEXT.__text: 0xda98c
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x69e4
-  __TEXT.__const: 0x448b0
-  __TEXT.__gcc_except_tab: 0x3040
-  __TEXT.__cstring: 0xacb0
-  __TEXT.__unwind_info: 0x16e8
+129.0.14.0.0
+  __TEXT.__text: 0xe6e9c
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x69fc
+  __TEXT.__const: 0x44900
+  __TEXT.__gcc_except_tab: 0x3708
+  __TEXT.__cstring: 0xb9a8
+  __TEXT.__unwind_info: 0x1770
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c3b
-  __TEXT.__objc_methname: 0x6854
+  __TEXT.__objc_methname: 0x68a2
   __TEXT.__objc_methtype: 0x1e06
-  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_stubs: 0x2e20
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xe1b0
+  __DATA_CONST.__const: 0xe9f0
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1430
+  __DATA_CONST.__objc_selrefs: 0x1440
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x818
-  __AUTH_CONST.__auth_got: 0x4f8
-  __AUTH_CONST.__const: 0x3b20
-  __AUTH_CONST.__cfstring: 0x57e0
-  __AUTH_CONST.__objc_const: 0xe5d8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x66c
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0x3c00
+  __AUTH_CONST.__cfstring: 0x5c00
+  __AUTH_CONST.__objc_const: 0xe5f8
+  __DATA.__objc_ivar: 0x670
   __DATA.__data: 0x9c0
-  __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0x5230
-  __DATA_DIRTY.__bss: 0x38
+  __DATA.__bss: 0x450
+  __DATA_DIRTY.__objc_data: 0x5280
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C6727E3-9A6F-33A0-884E-A353E8FC3EC9
-  Functions: 2151
-  Symbols:   789
-  CStrings:  3187
+  UUID: 8D2F0263-BA40-373B-BD3D-4A6C8092258F
+  Functions: 2176
+  Symbols:   7286
+  CStrings:  3280
 
Symbols:
+ +[MPSNDArrayACos libraryInfo:]
+ +[MPSNDArrayACosGradient libraryInfo:]
+ +[MPSNDArrayACosh libraryInfo:]
+ +[MPSNDArrayACoshGradient libraryInfo:]
+ +[MPSNDArrayAND libraryInfo:]
+ +[MPSNDArrayANDPrimaryGradient libraryInfo:]
+ +[MPSNDArrayANDSecondaryGradient libraryInfo:]
+ +[MPSNDArrayASin libraryInfo:]
+ +[MPSNDArrayASinGradient libraryInfo:]
+ +[MPSNDArrayASinh libraryInfo:]
+ +[MPSNDArrayASinhGradient libraryInfo:]
+ +[MPSNDArrayATan libraryInfo:]
+ +[MPSNDArrayATan2 libraryInfo:]
+ +[MPSNDArrayATan2PrimaryGradient libraryInfo:]
+ +[MPSNDArrayATan2SecondaryGradient libraryInfo:]
+ +[MPSNDArrayATanGradient libraryInfo:]
+ +[MPSNDArrayATanh libraryInfo:]
+ +[MPSNDArrayATanhGradient libraryInfo:]
+ +[MPSNDArrayAbsolute libraryInfo:]
+ +[MPSNDArrayAbsoluteGradient libraryInfo:]
+ +[MPSNDArrayAddition libraryInfo:]
+ +[MPSNDArrayAdditionPrimaryGradient libraryInfo:]
+ +[MPSNDArrayAdditionSecondaryGradient libraryInfo:]
+ +[MPSNDArrayAffineInt4Dequantize libraryInfo:]
+ +[MPSNDArrayBandPart libraryInfo:]
+ +[MPSNDArrayBinaryKernel expectedVirtualSourceCount]
+ +[MPSNDArrayBinaryPrimaryGradientKernel expectedVirtualSourceCount]
+ +[MPSNDArrayBinarySecondaryGradientKernel expectedVirtualSourceCount]
+ +[MPSNDArrayCeil libraryInfo:]
+ +[MPSNDArrayCeilGradient libraryInfo:]
+ +[MPSNDArrayClamp libraryInfo:]
+ +[MPSNDArrayClampPrimaryGradient libraryInfo:]
+ +[MPSNDArrayClampSecondaryGradient libraryInfo:]
+ +[MPSNDArrayClampTertiaryGradient libraryInfo:]
+ +[MPSNDArrayCol2imKernel libraryInfo:]
+ +[MPSNDArrayConvolution2D libraryInfo:]
+ +[MPSNDArrayConvolution2D supportsPostfixForDevice:]
+ +[MPSNDArrayConvolution2D supportsPostfixForDevice:convolutionDescriptor:sourceTensorDescriptor:destinationTensorDescriptor:weightsTensorDescriptor:]
+ +[MPSNDArrayConvolution2D supportsPrefixForDevice:]
+ +[MPSNDArrayConvolution2DGradientWithInput libraryInfo:]
+ +[MPSNDArrayConvolution2DGradientWithInput supportsPostfixForDevice:]
+ +[MPSNDArrayConvolution2DGradientWithInput supportsPostfixForDevice:convolutionDescriptor:sourceTensorDescriptor:destinationTensorDescriptor:weightsTensorDescriptor:]
+ +[MPSNDArrayConvolution2DGradientWithInput supportsPrefixForDevice:]
+ +[MPSNDArrayConvolution2DGradientWithWeights libraryInfo:]
+ +[MPSNDArrayConvolution2DGradientWithWeights supportsPostfixForDevice:]
+ +[MPSNDArrayConvolution2DGradientWithWeights supportsPostfixForDevice:convolutionDescriptor:sourceTensorDescriptor:destinationTensorDescriptor:weightsTensorDescriptor:]
+ +[MPSNDArrayConvolution2DGradientWithWeights supportsPrefixForDevice:]
+ +[MPSNDArrayConvolution3D libraryInfo:]
+ +[MPSNDArrayConvolution3DGradientWithInput libraryInfo:]
+ +[MPSNDArrayConvolution3DGradientWithWeights libraryInfo:]
+ +[MPSNDArrayCos libraryInfo:]
+ +[MPSNDArrayCosGradient libraryInfo:]
+ +[MPSNDArrayCosh libraryInfo:]
+ +[MPSNDArrayCoshGradient libraryInfo:]
+ +[MPSNDArrayCostVolume libraryInfo:]
+ +[MPSNDArrayCropResize libraryInfo:]
+ +[MPSNDArrayDecompositionLU libraryInfo:]
+ +[MPSNDArrayDecompositionQR libraryInfo:]
+ +[MPSNDArrayDepthwiseConvolutionKernel libraryInfo:]
+ +[MPSNDArrayDepthwiseConvolutionKernel supportsPostfixForDevice:]
+ +[MPSNDArrayDepthwiseConvolutionKernel supportsPrefixForDevice:]
+ +[MPSNDArrayDivision libraryInfo:]
+ +[MPSNDArrayDivisionPrimaryGradient libraryInfo:]
+ +[MPSNDArrayDivisionSecondaryGradient libraryInfo:]
+ +[MPSNDArrayEqual libraryInfo:]
+ +[MPSNDArrayEqualPrimaryGradient libraryInfo:]
+ +[MPSNDArrayEqualSecondaryGradient libraryInfo:]
+ +[MPSNDArrayErf libraryInfo:]
+ +[MPSNDArrayErfGradient libraryInfo:]
+ +[MPSNDArrayExponent libraryInfo:]
+ +[MPSNDArrayExponentBase10 libraryInfo:]
+ +[MPSNDArrayExponentBase10Gradient libraryInfo:]
+ +[MPSNDArrayExponentBase2 libraryInfo:]
+ +[MPSNDArrayExponentBase2Gradient libraryInfo:]
+ +[MPSNDArrayExponentGradient libraryInfo:]
+ +[MPSNDArrayFloor libraryInfo:]
+ +[MPSNDArrayFloorGradient libraryInfo:]
+ +[MPSNDArrayFourierTransform libraryInfo:]
+ +[MPSNDArrayGather libraryInfo:]
+ +[MPSNDArrayGatherGradient libraryInfo:]
+ +[MPSNDArrayGatherND libraryInfo:]
+ +[MPSNDArrayGatherNDGradient libraryInfo:]
+ +[MPSNDArrayGreaterThan libraryInfo:]
+ +[MPSNDArrayGreaterThanOrEqualTo libraryInfo:]
+ +[MPSNDArrayGreaterThanOrEqualToPrimaryGradient libraryInfo:]
+ +[MPSNDArrayGreaterThanOrEqualToSecondaryGradient libraryInfo:]
+ +[MPSNDArrayGreaterThanPrimaryGradient libraryInfo:]
+ +[MPSNDArrayGreaterThanSecondaryGradient libraryInfo:]
+ +[MPSNDArrayGridSample libraryInfo:]
+ +[MPSNDArrayHammingDistanceKernel libraryInfo:]
+ +[MPSNDArrayHammingDistanceKernel supportsPostfixForDevice:]
+ +[MPSNDArrayHammingDistanceKernel supportsPrefixForDevice:]
+ +[MPSNDArrayIdentity libraryInfo:]
+ +[MPSNDArrayIm2colKernel libraryInfo:]
+ +[MPSNDArrayInitialization libraryInfo:]
+ +[MPSNDArrayIsFinite libraryInfo:]
+ +[MPSNDArrayIsFiniteGradient libraryInfo:]
+ +[MPSNDArrayIsInfinite libraryInfo:]
+ +[MPSNDArrayIsInfiniteGradient libraryInfo:]
+ +[MPSNDArrayIsNaN libraryInfo:]
+ +[MPSNDArrayIsNaNGradient libraryInfo:]
+ +[MPSNDArrayLUTDequantize libraryInfo:]
+ +[MPSNDArrayLUTGEMV libraryInfo:]
+ +[MPSNDArrayLessThan libraryInfo:]
+ +[MPSNDArrayLessThanOrEqualTo libraryInfo:]
+ +[MPSNDArrayLessThanOrEqualToPrimaryGradient libraryInfo:]
+ +[MPSNDArrayLessThanOrEqualToSecondaryGradient libraryInfo:]
+ +[MPSNDArrayLessThanPrimaryGradient libraryInfo:]
+ +[MPSNDArrayLessThanSecondaryGradient libraryInfo:]
+ +[MPSNDArrayLocalConvolution libraryInfo:]
+ +[MPSNDArrayLogSoftMax libraryInfo:]
+ +[MPSNDArrayLogSoftMaxGradient libraryInfo:]
+ +[MPSNDArrayLogarithm libraryInfo:]
+ +[MPSNDArrayLogarithmBase10 libraryInfo:]
+ +[MPSNDArrayLogarithmBase10Gradient libraryInfo:]
+ +[MPSNDArrayLogarithmBase2 libraryInfo:]
+ +[MPSNDArrayLogarithmBase2Gradient libraryInfo:]
+ +[MPSNDArrayLogarithmGradient libraryInfo:]
+ +[MPSNDArrayMaterializeSparseTensor expectedVirtualSourceCount]
+ +[MPSNDArrayMaterializeSparseTensor libraryInfo:]
+ +[MPSNDArrayMathBinaryKernel libraryInfo:]
+ +[MPSNDArrayMathBinaryPrimaryGradient libraryInfo:]
+ +[MPSNDArrayMathBinarySecondaryGradient libraryInfo:]
+ +[MPSNDArrayMathTernaryKernel libraryInfo:]
+ +[MPSNDArrayMathTernaryPrimaryGradient libraryInfo:]
+ +[MPSNDArrayMathTernarySecondaryGradient libraryInfo:]
+ +[MPSNDArrayMathTernaryTertiaryGradient libraryInfo:]
+ +[MPSNDArrayMathUnaryGradient libraryInfo:]
+ +[MPSNDArrayMathUnaryKernel libraryInfo:]
+ +[MPSNDArrayMatrixMultiplication expectedVirtualSourceCount]
+ +[MPSNDArrayMatrixMultiplication libraryInfo:]
+ +[MPSNDArrayMatrixMultiplication supportsPostfixForDevice:]
+ +[MPSNDArrayMatrixMultiplication supportsPrefixForDevice:]
+ +[MPSNDArrayMatrixMultiplicationGradient expectedVirtualSourceCount]
+ +[MPSNDArrayMatrixMultiplicationGradient libraryInfo:]
+ +[MPSNDArrayMatrixMultiplicationGradient supportsPostfixForDevice:]
+ +[MPSNDArrayMatrixMultiplicationGradient supportsPrefixForDevice:]
+ +[MPSNDArrayMatrixMultiplicationSparse expectedVirtualSourceCount]
+ +[MPSNDArrayMatrixMultiplicationSparse libraryInfo:]
+ +[MPSNDArrayMaximum libraryInfo:]
+ +[MPSNDArrayMaximumPrimaryGradient libraryInfo:]
+ +[MPSNDArrayMaximumSecondaryGradient libraryInfo:]
+ +[MPSNDArrayMinimum libraryInfo:]
+ +[MPSNDArrayMinimumPrimaryGradient libraryInfo:]
+ +[MPSNDArrayMinimumSecondaryGradient libraryInfo:]
+ +[MPSNDArrayModulo libraryInfo:]
+ +[MPSNDArrayModuloPrimaryGradient libraryInfo:]
+ +[MPSNDArrayModuloSecondaryGradient libraryInfo:]
+ +[MPSNDArrayMultiaryBase expectedVirtualSourceCount]
+ +[MPSNDArrayMultiaryBase supportsPostfixForDevice:]
+ +[MPSNDArrayMultiaryBase supportsPrefixForDevice:]
+ +[MPSNDArrayMultiaryKernel supportsDestinationQuantizationWithDescriptor:device:]
+ +[MPSNDArrayMultiaryKernel supportsSourceQuantizationWithDescriptor:atIndex:device:]
+ +[MPSNDArrayMultiplication libraryInfo:]
+ +[MPSNDArrayMultiplicationPrimaryGradient libraryInfo:]
+ +[MPSNDArrayMultiplicationSecondaryGradient libraryInfo:]
+ +[MPSNDArrayNAND libraryInfo:]
+ +[MPSNDArrayNANDPrimaryGradient libraryInfo:]
+ +[MPSNDArrayNANDSecondaryGradient libraryInfo:]
+ +[MPSNDArrayNMS libraryInfo:]
+ +[MPSNDArrayNOR libraryInfo:]
+ +[MPSNDArrayNORPrimaryGradient libraryInfo:]
+ +[MPSNDArrayNORSecondaryGradient libraryInfo:]
+ +[MPSNDArrayNOT libraryInfo:]
+ +[MPSNDArrayNOTGradient libraryInfo:]
+ +[MPSNDArrayNegative libraryInfo:]
+ +[MPSNDArrayNegativeGradient libraryInfo:]
+ +[MPSNDArrayNeuronGeLU libraryInfo:]
+ +[MPSNDArrayNeuronGeLUGradient libraryInfo:]
+ +[MPSNDArrayNeuronGradient libraryInfo:]
+ +[MPSNDArrayNeuronKernel libraryInfo:]
+ +[MPSNDArrayNotEqual libraryInfo:]
+ +[MPSNDArrayNotEqualPrimaryGradient libraryInfo:]
+ +[MPSNDArrayNotEqualSecondaryGradient libraryInfo:]
+ +[MPSNDArrayOR libraryInfo:]
+ +[MPSNDArrayORPrimaryGradient libraryInfo:]
+ +[MPSNDArrayORSecondaryGradient libraryInfo:]
+ +[MPSNDArrayOffsetIdentity libraryInfo:]
+ +[MPSNDArrayPadGradientKernel libraryInfo:]
+ +[MPSNDArrayPadKernel libraryInfo:]
+ +[MPSNDArrayPoolingKernel libraryInfo:]
+ +[MPSNDArrayPoolingMultiDestinationKernel libraryInfo:]
+ +[MPSNDArrayPower libraryInfo:]
+ +[MPSNDArrayPowerPrimaryGradient libraryInfo:]
+ +[MPSNDArrayPowerSecondaryGradient libraryInfo:]
+ +[MPSNDArrayPrune libraryInfo:]
+ +[MPSNDArrayQuantizedConvolution supportsDestinationQuantizationWithDescriptor:device:]
+ +[MPSNDArrayQuantizedConvolution supportsSourceQuantizationWithDescriptor:atIndex:device:]
+ +[MPSNDArrayQuantizedGatherND libraryInfo:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getDQuantMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getDQuantScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLUTIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLeftDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLeftDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLeftMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLeftScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getLeftZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightLUTIndexWithLeftLUTQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getRightZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication getZeroPointIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:]
+ +[MPSNDArrayQuantizedMatrixMultiplication supportsDestinationQuantizationWithDescriptor:device:]
+ +[MPSNDArrayQuantizedMatrixMultiplication supportsSourceQuantizationWithDescriptor:atIndex:device:]
+ +[MPSNDArrayQuantizedScaledDotProductAttention libraryInfo:]
+ +[MPSNDArrayQuantizedScaledDotProductAttention supportsPostfixForDevice:]
+ +[MPSNDArrayQuantizedScaledDotProductAttention supportsPrefixForDevice:]
+ +[MPSNDArrayRandom libraryInfo:]
+ +[MPSNDArrayRandomState libraryInfo:]
+ +[MPSNDArrayRandomStateDescriptor supportsSecureCoding]
+ +[MPSNDArrayReciprocal libraryInfo:]
+ +[MPSNDArrayReciprocalGradient libraryInfo:]
+ +[MPSNDArrayReduction libraryInfo:]
+ +[MPSNDArrayReductionGradient libraryInfo:]
+ +[MPSNDArrayResample libraryInfo:]
+ +[MPSNDArrayResampleGradient libraryInfo:]
+ +[MPSNDArrayReverseSquareRoot libraryInfo:]
+ +[MPSNDArrayReverseSquareRootGradient libraryInfo:]
+ +[MPSNDArrayRint libraryInfo:]
+ +[MPSNDArrayRintGradient libraryInfo:]
+ +[MPSNDArrayRound libraryInfo:]
+ +[MPSNDArrayRoundGradient libraryInfo:]
+ +[MPSNDArrayScaledDotProductAttention libraryInfo:]
+ +[MPSNDArrayScaledDotProductAttention supportsPostfixForDevice:]
+ +[MPSNDArrayScaledDotProductAttention supportsPrefixForDevice:]
+ +[MPSNDArrayScan libraryInfo:]
+ +[MPSNDArrayScanGradient libraryInfo:]
+ +[MPSNDArrayScatter libraryInfo:]
+ +[MPSNDArrayScatterGradient libraryInfo:]
+ +[MPSNDArraySelect libraryInfo:]
+ +[MPSNDArraySelectPrimaryGradient libraryInfo:]
+ +[MPSNDArraySelectSecondaryGradient libraryInfo:]
+ +[MPSNDArraySelectTertiaryGradient libraryInfo:]
+ +[MPSNDArraySign libraryInfo:]
+ +[MPSNDArraySignGradient libraryInfo:]
+ +[MPSNDArraySignbit libraryInfo:]
+ +[MPSNDArraySignbitGradient libraryInfo:]
+ +[MPSNDArraySin libraryInfo:]
+ +[MPSNDArraySinGradient libraryInfo:]
+ +[MPSNDArraySinh libraryInfo:]
+ +[MPSNDArraySinhGradient libraryInfo:]
+ +[MPSNDArraySoftMax libraryInfo:]
+ +[MPSNDArraySoftMaxGradient libraryInfo:]
+ +[MPSNDArraySolverLU libraryInfo:]
+ +[MPSNDArraySort libraryInfo:]
+ +[MPSNDArraySquare libraryInfo:]
+ +[MPSNDArraySquareGradient libraryInfo:]
+ +[MPSNDArraySquareRoot libraryInfo:]
+ +[MPSNDArraySquareRootGradient libraryInfo:]
+ +[MPSNDArrayStencilKernel libraryInfo:]
+ +[MPSNDArrayStitchedReduction libraryInfo:]
+ +[MPSNDArrayStridedSlice libraryInfo:]
+ +[MPSNDArrayStridedSliceGradient libraryInfo:]
+ +[MPSNDArraySubtraction libraryInfo:]
+ +[MPSNDArraySubtractionPrimaryGradient libraryInfo:]
+ +[MPSNDArraySubtractionSecondaryGradient libraryInfo:]
+ +[MPSNDArrayTan libraryInfo:]
+ +[MPSNDArrayTanGradient libraryInfo:]
+ +[MPSNDArrayTanh libraryInfo:]
+ +[MPSNDArrayTanhGradient libraryInfo:]
+ +[MPSNDArrayTileGradientKernel libraryInfo:]
+ +[MPSNDArrayTileKernel libraryInfo:]
+ +[MPSNDArrayTopK libraryInfo:]
+ +[MPSNDArrayTopKGradient libraryInfo:]
+ +[MPSNDArrayTopKMultiDestination libraryInfo:]
+ +[MPSNDArrayUnaryGradientKernel expectedVirtualSourceCount]
+ +[MPSNDArrayUnaryKernel expectedVirtualSourceCount]
+ +[MPSNDArrayVectorLUTDequantize libraryInfo:]
+ +[MPSNDArrayXNOR libraryInfo:]
+ +[MPSNDArrayXNORPrimaryGradient libraryInfo:]
+ +[MPSNDArrayXNORSecondaryGradient libraryInfo:]
+ +[MPSNDArrayXOR libraryInfo:]
+ +[MPSNDArrayXORPrimaryGradient libraryInfo:]
+ +[MPSNDArrayXORSecondaryGradient libraryInfo:]
+ -[MPSNDArrayACos initWithDevice:]
+ -[MPSNDArrayACosGradient initWithDevice:]
+ -[MPSNDArrayACosh initWithDevice:]
+ -[MPSNDArrayACoshGradient initWithDevice:]
+ -[MPSNDArrayAND initWithDevice:]
+ -[MPSNDArrayANDPrimaryGradient initWithDevice:]
+ -[MPSNDArrayANDSecondaryGradient initWithDevice:]
+ -[MPSNDArrayASTCQuantizationDescriptor copyWithZone:]
+ -[MPSNDArrayASTCQuantizationDescriptor getNDArrayCount]
+ -[MPSNDArrayASTCQuantizationDescriptor hasMinValue]
+ -[MPSNDArrayASTCQuantizationDescriptor initWithDataType:hasMinValue:]
+ -[MPSNDArrayASTCQuantizationDescriptor init]
+ -[MPSNDArrayASTCQuantizationDescriptor setHasMinValue:]
+ -[MPSNDArrayASin initWithDevice:]
+ -[MPSNDArrayASinGradient initWithDevice:]
+ -[MPSNDArrayASinh initWithDevice:]
+ -[MPSNDArrayASinhGradient initWithDevice:]
+ -[MPSNDArrayATan initWithDevice:]
+ -[MPSNDArrayATan2 initWithDevice:]
+ -[MPSNDArrayATan2PrimaryGradient initWithDevice:]
+ -[MPSNDArrayATan2SecondaryGradient initWithDevice:]
+ -[MPSNDArrayATanGradient initWithDevice:]
+ -[MPSNDArrayATanh initWithDevice:]
+ -[MPSNDArrayATanhGradient initWithDevice:]
+ -[MPSNDArrayAbsolute initWithDevice:]
+ -[MPSNDArrayAbsoluteGradient initWithDevice:]
+ -[MPSNDArrayAddition initWithDevice:]
+ -[MPSNDArrayAdditionPrimaryGradient initWithDevice:]
+ -[MPSNDArrayAdditionSecondaryGradient initWithDevice:]
+ -[MPSNDArrayAffineInt4Dequantize copyWithZone:device:]
+ -[MPSNDArrayAffineInt4Dequantize dealloc]
+ -[MPSNDArrayAffineInt4Dequantize encodeWithCoder:]
+ -[MPSNDArrayAffineInt4Dequantize initWithDevice:quantizationDescriptor:]
+ -[MPSNDArrayAffineInt4Dequantize initWithDevice:quantizationDescriptor:sourceCount:]
+ -[MPSNDArrayAffineInt4Dequantize kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayAffineInt4Dequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayAffineQuantizationDescriptor copyWithZone:]
+ -[MPSNDArrayAffineQuantizationDescriptor getDQuantMinValIndex]
+ -[MPSNDArrayAffineQuantizationDescriptor getDQuantScaleIndex]
+ -[MPSNDArrayAffineQuantizationDescriptor getMinValIndex]
+ -[MPSNDArrayAffineQuantizationDescriptor getNDArrayCount]
+ -[MPSNDArrayAffineQuantizationDescriptor getScaleIndex]
+ -[MPSNDArrayAffineQuantizationDescriptor getZeroPointIndex]
+ -[MPSNDArrayAffineQuantizationDescriptor hasDoubleQuantMinVal]
+ -[MPSNDArrayAffineQuantizationDescriptor hasDoubleQuantScale]
+ -[MPSNDArrayAffineQuantizationDescriptor hasMinValue]
+ -[MPSNDArrayAffineQuantizationDescriptor hasZeroPoint]
+ -[MPSNDArrayAffineQuantizationDescriptor implicitZeroPoint]
+ -[MPSNDArrayAffineQuantizationDescriptor initWithDataType:hasZeroPoint:hasMinValue:]
+ -[MPSNDArrayAffineQuantizationDescriptor initWithDataType:hasZeroPoint:hasMinValue:hasDoubleQuantScale:hasDoubleQuantMinVal:]
+ -[MPSNDArrayAffineQuantizationDescriptor init]
+ -[MPSNDArrayAffineQuantizationDescriptor setHasDoubleQuantMinVal:]
+ -[MPSNDArrayAffineQuantizationDescriptor setHasDoubleQuantScale:]
+ -[MPSNDArrayAffineQuantizationDescriptor setHasMinValue:]
+ -[MPSNDArrayAffineQuantizationDescriptor setHasZeroPoint:]
+ -[MPSNDArrayAffineQuantizationDescriptor setImplicitZeroPoint:]
+ -[MPSNDArrayArgSort initWithDevice:]
+ -[MPSNDArrayArgSort initWithDevice:axis:descending:]
+ -[MPSNDArrayBandPart copyWithZone:device:]
+ -[MPSNDArrayBandPart encodeWithCoder:]
+ -[MPSNDArrayBandPart initWithCoder:device:]
+ -[MPSNDArrayBandPart initWithDevice:]
+ -[MPSNDArrayBandPart kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayBandPart numLower]
+ -[MPSNDArrayBandPart numUpper]
+ -[MPSNDArrayBandPart setNumLower:]
+ -[MPSNDArrayBandPart setNumUpper:]
+ -[MPSNDArrayBinaryKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:]
+ -[MPSNDArrayBinaryKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:destinationArray:]
+ -[MPSNDArrayBinaryKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:resultState:destinationArray:]
+ -[MPSNDArrayBinaryKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:resultState:outputStateIsTemporary:]
+ -[MPSNDArrayBinaryKernel initWithCoder:device:]
+ -[MPSNDArrayBinaryKernel initWithDevice:]
+ -[MPSNDArrayBinaryKernel primaryDilationRates]
+ -[MPSNDArrayBinaryKernel primaryEdgeMode]
+ -[MPSNDArrayBinaryKernel primaryKernelSizes]
+ -[MPSNDArrayBinaryKernel primaryOffsets]
+ -[MPSNDArrayBinaryKernel primaryStrides]
+ -[MPSNDArrayBinaryKernel secondaryDilationRates]
+ -[MPSNDArrayBinaryKernel secondaryEdgeMode]
+ -[MPSNDArrayBinaryKernel secondaryKernelSizes]
+ -[MPSNDArrayBinaryKernel secondaryOffsets]
+ -[MPSNDArrayBinaryKernel secondaryStrides]
+ -[MPSNDArrayBinaryPrimaryGradientKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:]
+ -[MPSNDArrayBinaryPrimaryGradientKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayBinaryPrimaryGradientKernel initWithCoder:device:]
+ -[MPSNDArrayBinaryPrimaryGradientKernel initWithDevice:]
+ -[MPSNDArrayBinarySecondaryGradientKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:]
+ -[MPSNDArrayBinarySecondaryGradientKernel encodeToCommandBuffer:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayBinarySecondaryGradientKernel initWithCoder:device:]
+ -[MPSNDArrayBinarySecondaryGradientKernel initWithDevice:]
+ -[MPSNDArrayCeil initWithDevice:]
+ -[MPSNDArrayCeilGradient initWithDevice:]
+ -[MPSNDArrayClamp initWithDevice:]
+ -[MPSNDArrayClampPrimaryGradient initWithDevice:]
+ -[MPSNDArrayClampSecondaryGradient initWithDevice:]
+ -[MPSNDArrayClampTertiaryGradient initWithDevice:]
+ -[MPSNDArrayCol2imKernel copyWithZone:device:]
+ -[MPSNDArrayCol2imKernel dataLayout]
+ -[MPSNDArrayCol2imKernel dilationHeight]
+ -[MPSNDArrayCol2imKernel dilationWidth]
+ -[MPSNDArrayCol2imKernel encodeWithCoder:]
+ -[MPSNDArrayCol2imKernel initWithCoder:device:]
+ -[MPSNDArrayCol2imKernel initWithDevice:ndArrayIm2colDescriptor:]
+ -[MPSNDArrayCol2imKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayCol2imKernel kernelHeight]
+ -[MPSNDArrayCol2imKernel kernelWidth]
+ -[MPSNDArrayCol2imKernel paddingBottom]
+ -[MPSNDArrayCol2imKernel paddingLeft]
+ -[MPSNDArrayCol2imKernel paddingRight]
+ -[MPSNDArrayCol2imKernel paddingTop]
+ -[MPSNDArrayCol2imKernel setDataLayout:]
+ -[MPSNDArrayCol2imKernel setDilationHeight:]
+ -[MPSNDArrayCol2imKernel setDilationWidth:]
+ -[MPSNDArrayCol2imKernel setKernelHeight:]
+ -[MPSNDArrayCol2imKernel setKernelWidth:]
+ -[MPSNDArrayCol2imKernel setPaddingBottom:]
+ -[MPSNDArrayCol2imKernel setPaddingLeft:]
+ -[MPSNDArrayCol2imKernel setPaddingRight:]
+ -[MPSNDArrayCol2imKernel setPaddingTop:]
+ -[MPSNDArrayCol2imKernel setStrideHeight:]
+ -[MPSNDArrayCol2imKernel setStrideWidth:]
+ -[MPSNDArrayCol2imKernel strideHeight]
+ -[MPSNDArrayCol2imKernel strideWidth]
+ -[MPSNDArrayConvolution2D advanceAutoTuneIteration]
+ -[MPSNDArrayConvolution2D autoTuneIteration]
+ -[MPSNDArrayConvolution2D channelMultiplier]
+ -[MPSNDArrayConvolution2D copyWithZone:device:]
+ -[MPSNDArrayConvolution2D dataFormat]
+ -[MPSNDArrayConvolution2D dealloc]
+ -[MPSNDArrayConvolution2D destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayConvolution2D destinationStrides]
+ -[MPSNDArrayConvolution2D dilationRates]
+ -[MPSNDArrayConvolution2D dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution2D dimensionsToBeRetained]
+ -[MPSNDArrayConvolution2D encodeWithCoder:]
+ -[MPSNDArrayConvolution2D groups]
+ -[MPSNDArrayConvolution2D initWithCoder:device:]
+ -[MPSNDArrayConvolution2D initWithDevice:]
+ -[MPSNDArrayConvolution2D initWithDevice:ndArrayConvolution2DDescriptor:]
+ -[MPSNDArrayConvolution2D initWithDevice:ndArrayConvolution2DDescriptor:sourceCount:]
+ -[MPSNDArrayConvolution2D inputFeatureChannels]
+ -[MPSNDArrayConvolution2D kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution2D kernelSizes]
+ -[MPSNDArrayConvolution2D logNextAutoTuneParams]
+ -[MPSNDArrayConvolution2D offsets]
+ -[MPSNDArrayConvolution2D outputFeatureChannels]
+ -[MPSNDArrayConvolution2D setAutoTuneIteration:]
+ -[MPSNDArrayConvolution2D setAutoTuningParameters:]
+ -[MPSNDArrayConvolution2D setAutoTuningTarget:]
+ -[MPSNDArrayConvolution2D setLogNextAutoTuneParams:]
+ -[MPSNDArrayConvolution2D setOffsets:]
+ -[MPSNDArrayConvolution2D strideInPixels]
+ -[MPSNDArrayConvolution2D stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution2D weightsFormat]
+ -[MPSNDArrayConvolution2D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayConvolution2DDescriptor copyWithZone:]
+ -[MPSNDArrayConvolution2DDescriptor dataFormat]
+ -[MPSNDArrayConvolution2DDescriptor dilationRateInX]
+ -[MPSNDArrayConvolution2DDescriptor dilationRateInY]
+ -[MPSNDArrayConvolution2DDescriptor groups]
+ -[MPSNDArrayConvolution2DDescriptor init]
+ -[MPSNDArrayConvolution2DDescriptor inputFeatureChannels]
+ -[MPSNDArrayConvolution2DDescriptor kernelHeight]
+ -[MPSNDArrayConvolution2DDescriptor kernelWidth]
+ -[MPSNDArrayConvolution2DDescriptor outputFeatureChannels]
+ -[MPSNDArrayConvolution2DDescriptor setDataFormat:]
+ -[MPSNDArrayConvolution2DDescriptor setDilationRateInX:]
+ -[MPSNDArrayConvolution2DDescriptor setDilationRateInY:]
+ -[MPSNDArrayConvolution2DDescriptor setGroups:]
+ -[MPSNDArrayConvolution2DDescriptor setInputFeatureChannels:]
+ -[MPSNDArrayConvolution2DDescriptor setKernelHeight:]
+ -[MPSNDArrayConvolution2DDescriptor setKernelWidth:]
+ -[MPSNDArrayConvolution2DDescriptor setOutputFeatureChannels:]
+ -[MPSNDArrayConvolution2DDescriptor setStrideInPixelsX:]
+ -[MPSNDArrayConvolution2DDescriptor setStrideInPixelsY:]
+ -[MPSNDArrayConvolution2DDescriptor setWeightsFormat:]
+ -[MPSNDArrayConvolution2DDescriptor strideInPixelsX]
+ -[MPSNDArrayConvolution2DDescriptor strideInPixelsY]
+ -[MPSNDArrayConvolution2DDescriptor weightsFormat]
+ -[MPSNDArrayConvolution2DGradientWithInput channelMultiplier]
+ -[MPSNDArrayConvolution2DGradientWithInput copyWithZone:device:]
+ -[MPSNDArrayConvolution2DGradientWithInput dataFormat]
+ -[MPSNDArrayConvolution2DGradientWithInput dealloc]
+ -[MPSNDArrayConvolution2DGradientWithInput destinationStrides]
+ -[MPSNDArrayConvolution2DGradientWithInput dilationRates]
+ -[MPSNDArrayConvolution2DGradientWithInput dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution2DGradientWithInput dimensionsToBeRetained]
+ -[MPSNDArrayConvolution2DGradientWithInput encodeWithCoder:]
+ -[MPSNDArrayConvolution2DGradientWithInput groups]
+ -[MPSNDArrayConvolution2DGradientWithInput initWithCoder:device:]
+ -[MPSNDArrayConvolution2DGradientWithInput initWithDevice:]
+ -[MPSNDArrayConvolution2DGradientWithInput initWithDevice:ndArrayConvolution2DDescriptor:]
+ -[MPSNDArrayConvolution2DGradientWithInput inputFeatureChannels]
+ -[MPSNDArrayConvolution2DGradientWithInput kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution2DGradientWithInput kernelOffsets]
+ -[MPSNDArrayConvolution2DGradientWithInput kernelSizes]
+ -[MPSNDArrayConvolution2DGradientWithInput offsets]
+ -[MPSNDArrayConvolution2DGradientWithInput outputFeatureChannels]
+ -[MPSNDArrayConvolution2DGradientWithInput setAutoTuningParameters:]
+ -[MPSNDArrayConvolution2DGradientWithInput setAutoTuningTarget:]
+ -[MPSNDArrayConvolution2DGradientWithInput setKernelOffsets:]
+ -[MPSNDArrayConvolution2DGradientWithInput setOffsets:]
+ -[MPSNDArrayConvolution2DGradientWithInput strideInPixels]
+ -[MPSNDArrayConvolution2DGradientWithInput stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution2DGradientWithInput weightsFormat]
+ -[MPSNDArrayConvolution2DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayConvolution2DGradientWithWeights channelMultiplier]
+ -[MPSNDArrayConvolution2DGradientWithWeights copyWithZone:device:]
+ -[MPSNDArrayConvolution2DGradientWithWeights dataFormat]
+ -[MPSNDArrayConvolution2DGradientWithWeights dealloc]
+ -[MPSNDArrayConvolution2DGradientWithWeights destinationStrides]
+ -[MPSNDArrayConvolution2DGradientWithWeights dilationRates]
+ -[MPSNDArrayConvolution2DGradientWithWeights dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution2DGradientWithWeights dimensionsToBeRetained]
+ -[MPSNDArrayConvolution2DGradientWithWeights encodeWithCoder:]
+ -[MPSNDArrayConvolution2DGradientWithWeights groups]
+ -[MPSNDArrayConvolution2DGradientWithWeights initWithCoder:device:]
+ -[MPSNDArrayConvolution2DGradientWithWeights initWithDevice:]
+ -[MPSNDArrayConvolution2DGradientWithWeights initWithDevice:ndArrayConvolution2DDescriptor:]
+ -[MPSNDArrayConvolution2DGradientWithWeights inputFeatureChannels]
+ -[MPSNDArrayConvolution2DGradientWithWeights kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution2DGradientWithWeights kernelSizes]
+ -[MPSNDArrayConvolution2DGradientWithWeights offsets]
+ -[MPSNDArrayConvolution2DGradientWithWeights outputFeatureChannels]
+ -[MPSNDArrayConvolution2DGradientWithWeights setAutoTuning:]
+ -[MPSNDArrayConvolution2DGradientWithWeights setAutoTuningParameters:]
+ -[MPSNDArrayConvolution2DGradientWithWeights setOffsets:]
+ -[MPSNDArrayConvolution2DGradientWithWeights strideInPixels]
+ -[MPSNDArrayConvolution2DGradientWithWeights stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution2DGradientWithWeights weightsFormat]
+ -[MPSNDArrayConvolution2DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayConvolution3D dataFormat]
+ -[MPSNDArrayConvolution3D dealloc]
+ -[MPSNDArrayConvolution3D destinationStrides]
+ -[MPSNDArrayConvolution3D dilationRates]
+ -[MPSNDArrayConvolution3D dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution3D dimensionsToBeRetained]
+ -[MPSNDArrayConvolution3D groups]
+ -[MPSNDArrayConvolution3D initWithDevice:]
+ -[MPSNDArrayConvolution3D kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution3D offsets]
+ -[MPSNDArrayConvolution3D setDataFormat:]
+ -[MPSNDArrayConvolution3D setDilationRates:]
+ -[MPSNDArrayConvolution3D setGroups:]
+ -[MPSNDArrayConvolution3D setOffsets:]
+ -[MPSNDArrayConvolution3D setStrideInPixels:]
+ -[MPSNDArrayConvolution3D setWeightsFormat:]
+ -[MPSNDArrayConvolution3D strideInPixels]
+ -[MPSNDArrayConvolution3D stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution3D weightsFormat]
+ -[MPSNDArrayConvolution3D workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayConvolution3DGradientWithInput dataFormat]
+ -[MPSNDArrayConvolution3DGradientWithInput dealloc]
+ -[MPSNDArrayConvolution3DGradientWithInput destinationStrides]
+ -[MPSNDArrayConvolution3DGradientWithInput dilationRates]
+ -[MPSNDArrayConvolution3DGradientWithInput dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution3DGradientWithInput dimensionsToBeRetained]
+ -[MPSNDArrayConvolution3DGradientWithInput groups]
+ -[MPSNDArrayConvolution3DGradientWithInput initWithDevice:]
+ -[MPSNDArrayConvolution3DGradientWithInput kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution3DGradientWithInput kernelOffsets]
+ -[MPSNDArrayConvolution3DGradientWithInput offsets]
+ -[MPSNDArrayConvolution3DGradientWithInput setDataFormat:]
+ -[MPSNDArrayConvolution3DGradientWithInput setDilationRates:]
+ -[MPSNDArrayConvolution3DGradientWithInput setGroups:]
+ -[MPSNDArrayConvolution3DGradientWithInput setKernelOffsets:]
+ -[MPSNDArrayConvolution3DGradientWithInput setOffsets:]
+ -[MPSNDArrayConvolution3DGradientWithInput setStrideInPixels:]
+ -[MPSNDArrayConvolution3DGradientWithInput setWeightsFormat:]
+ -[MPSNDArrayConvolution3DGradientWithInput strideInPixels]
+ -[MPSNDArrayConvolution3DGradientWithInput stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution3DGradientWithInput weightsFormat]
+ -[MPSNDArrayConvolution3DGradientWithInput workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayConvolution3DGradientWithWeights dataFormat]
+ -[MPSNDArrayConvolution3DGradientWithWeights dealloc]
+ -[MPSNDArrayConvolution3DGradientWithWeights destinationStrides]
+ -[MPSNDArrayConvolution3DGradientWithWeights dilationRates]
+ -[MPSNDArrayConvolution3DGradientWithWeights dimensionsNotToBeBroadcast]
+ -[MPSNDArrayConvolution3DGradientWithWeights dimensionsToBeRetained]
+ -[MPSNDArrayConvolution3DGradientWithWeights groups]
+ -[MPSNDArrayConvolution3DGradientWithWeights initWithDevice:]
+ -[MPSNDArrayConvolution3DGradientWithWeights kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayConvolution3DGradientWithWeights kernelOffsets]
+ -[MPSNDArrayConvolution3DGradientWithWeights offsets]
+ -[MPSNDArrayConvolution3DGradientWithWeights setDataFormat:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setDilationRates:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setGroups:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setKernelOffsets:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setOffsets:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setStrideInPixels:]
+ -[MPSNDArrayConvolution3DGradientWithWeights setWeightsFormat:]
+ -[MPSNDArrayConvolution3DGradientWithWeights strideInPixels]
+ -[MPSNDArrayConvolution3DGradientWithWeights stridesAtSourceIndex:]
+ -[MPSNDArrayConvolution3DGradientWithWeights weightsFormat]
+ -[MPSNDArrayConvolution3DGradientWithWeights workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayCos initWithDevice:]
+ -[MPSNDArrayCosGradient initWithDevice:]
+ -[MPSNDArrayCosh initWithDevice:]
+ -[MPSNDArrayCoshGradient initWithDevice:]
+ -[MPSNDArrayCostVolume alignCorners]
+ -[MPSNDArrayCostVolume constantValue]
+ -[MPSNDArrayCostVolume coordinate1DInWidth]
+ -[MPSNDArrayCostVolume copyWithZone:device:]
+ -[MPSNDArrayCostVolume dataFormat]
+ -[MPSNDArrayCostVolume destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayCostVolume dimensionsToBeRetained]
+ -[MPSNDArrayCostVolume encodeWithCoder:]
+ -[MPSNDArrayCostVolume initWithCoder:device:]
+ -[MPSNDArrayCostVolume initWithDevice:]
+ -[MPSNDArrayCostVolume initWithDevice:ndArrayCostVolumeDescriptor:]
+ -[MPSNDArrayCostVolume kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayCostVolume nearestMode]
+ -[MPSNDArrayCostVolume normalizeCoordinates]
+ -[MPSNDArrayCostVolume paddingMode]
+ -[MPSNDArrayCostVolume relativeCoordinates]
+ -[MPSNDArrayCostVolume samplingMode]
+ -[MPSNDArrayCostVolume setAlignCorners:]
+ -[MPSNDArrayCostVolume setConstantValue:]
+ -[MPSNDArrayCostVolume setCoordinate1DInWidth:]
+ -[MPSNDArrayCostVolume setDataFormat:]
+ -[MPSNDArrayCostVolume setNearestMode:]
+ -[MPSNDArrayCostVolume setNormalizeCoordinates:]
+ -[MPSNDArrayCostVolume setPaddingMode:]
+ -[MPSNDArrayCostVolume setRelativeCoordinates:]
+ -[MPSNDArrayCostVolume setSamplingMode:]
+ -[MPSNDArrayCostVolume setWindowSizes:]
+ -[MPSNDArrayCostVolume supportsGradientForSourceIndex:]
+ -[MPSNDArrayCostVolume windowSizes]
+ -[MPSNDArrayCostVolumeDescriptor alignCorners]
+ -[MPSNDArrayCostVolumeDescriptor constantValue]
+ -[MPSNDArrayCostVolumeDescriptor coordinate1DInWidth]
+ -[MPSNDArrayCostVolumeDescriptor copyWithZone:]
+ -[MPSNDArrayCostVolumeDescriptor dataFormat]
+ -[MPSNDArrayCostVolumeDescriptor init]
+ -[MPSNDArrayCostVolumeDescriptor nearestMode]
+ -[MPSNDArrayCostVolumeDescriptor normalizeCoordinates]
+ -[MPSNDArrayCostVolumeDescriptor paddingMode]
+ -[MPSNDArrayCostVolumeDescriptor relativeCoordinates]
+ -[MPSNDArrayCostVolumeDescriptor samplingMode]
+ -[MPSNDArrayCostVolumeDescriptor setAlignCorners:]
+ -[MPSNDArrayCostVolumeDescriptor setConstantValue:]
+ -[MPSNDArrayCostVolumeDescriptor setCoordinate1DInWidth:]
+ -[MPSNDArrayCostVolumeDescriptor setDataFormat:]
+ -[MPSNDArrayCostVolumeDescriptor setNearestMode:]
+ -[MPSNDArrayCostVolumeDescriptor setNormalizeCoordinates:]
+ -[MPSNDArrayCostVolumeDescriptor setPaddingMode:]
+ -[MPSNDArrayCostVolumeDescriptor setRelativeCoordinates:]
+ -[MPSNDArrayCostVolumeDescriptor setSamplingMode:]
+ -[MPSNDArrayCostVolumeDescriptor setWindowSizes:]
+ -[MPSNDArrayCostVolumeDescriptor windowSizes]
+ -[MPSNDArrayCropResize coordinateMode]
+ -[MPSNDArrayCropResize copyWithZone:device:]
+ -[MPSNDArrayCropResize destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayCropResize dimensionsNotToBeBroadcast]
+ -[MPSNDArrayCropResize dimensionsToBeRetained]
+ -[MPSNDArrayCropResize encodeWithCoder:]
+ -[MPSNDArrayCropResize initWithCoder:device:]
+ -[MPSNDArrayCropResize initWithDevice:]
+ -[MPSNDArrayCropResize kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayCropResize normalizeCoordinates]
+ -[MPSNDArrayCropResize resampleMode]
+ -[MPSNDArrayCropResize resizeHeight]
+ -[MPSNDArrayCropResize resizeWidth]
+ -[MPSNDArrayCropResize samplingMode]
+ -[MPSNDArrayCropResize setCoordinateMode:]
+ -[MPSNDArrayCropResize setNormalizeCoordinates:]
+ -[MPSNDArrayCropResize setResampleMode:]
+ -[MPSNDArrayCropResize setResizeHeight:]
+ -[MPSNDArrayCropResize setResizeWidth:]
+ -[MPSNDArrayCropResize setSamplingMode:]
+ -[MPSNDArrayCropResize setSpatialScale:]
+ -[MPSNDArrayCropResize spatialScale]
+ -[MPSNDArrayDecompositionLU dealloc]
+ -[MPSNDArrayDecompositionLU encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArrays:status:]
+ -[MPSNDArrayDecompositionLU initWithDevice:]
+ -[MPSNDArrayDecompositionLU kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayDecompositionQR computeQ]
+ -[MPSNDArrayDecompositionQR computeR]
+ -[MPSNDArrayDecompositionQR initWithDevice:]
+ -[MPSNDArrayDecompositionQR setComputeQ:]
+ -[MPSNDArrayDecompositionQR setComputeR:]
+ -[MPSNDArrayDepthwiseConvolution2DDescriptor channelMultiplier]
+ -[MPSNDArrayDepthwiseConvolution2DDescriptor init]
+ -[MPSNDArrayDepthwiseConvolution2DDescriptor setChannelMultiplier:]
+ -[MPSNDArrayDepthwiseConvolutionKernel channelAxis]
+ -[MPSNDArrayDepthwiseConvolutionKernel convDilationRates]
+ -[MPSNDArrayDepthwiseConvolutionKernel convStrides]
+ -[MPSNDArrayDepthwiseConvolutionKernel copyWithZone:device:]
+ -[MPSNDArrayDepthwiseConvolutionKernel debugDescription]
+ -[MPSNDArrayDepthwiseConvolutionKernel dimensionsNotToBeBroadcast]
+ -[MPSNDArrayDepthwiseConvolutionKernel dimensionsToBeRetained]
+ -[MPSNDArrayDepthwiseConvolutionKernel encodeWithCoder:]
+ -[MPSNDArrayDepthwiseConvolutionKernel initWithCoder:device:]
+ -[MPSNDArrayDepthwiseConvolutionKernel initWithDevice:]
+ -[MPSNDArrayDepthwiseConvolutionKernel initWithDevice:kernelType:]
+ -[MPSNDArrayDepthwiseConvolutionKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayDepthwiseConvolutionKernel kernelType]
+ -[MPSNDArrayDepthwiseConvolutionKernel paddingConstant]
+ -[MPSNDArrayDepthwiseConvolutionKernel paddingMode]
+ -[MPSNDArrayDepthwiseConvolutionKernel setChannelAxis:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setConvDilationRates:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setConvStrides:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setKernelType:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setPaddingConstant:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setPaddingMode:]
+ -[MPSNDArrayDepthwiseConvolutionKernel setWindowOffsets:]
+ -[MPSNDArrayDepthwiseConvolutionKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayDepthwiseConvolutionKernel usesVectorFunctionsOnOutput:]
+ -[MPSNDArrayDepthwiseConvolutionKernel windowOffsets]
+ -[MPSNDArrayDivision initWithDevice:]
+ -[MPSNDArrayDivisionPrimaryGradient initWithDevice:]
+ -[MPSNDArrayDivisionSecondaryGradient initWithDevice:]
+ -[MPSNDArrayEqual initWithDevice:]
+ -[MPSNDArrayEqualPrimaryGradient initWithDevice:]
+ -[MPSNDArrayEqualSecondaryGradient initWithDevice:]
+ -[MPSNDArrayErf initWithDevice:]
+ -[MPSNDArrayErfGradient initWithDevice:]
+ -[MPSNDArrayExponent initWithDevice:]
+ -[MPSNDArrayExponentBase10 initWithDevice:]
+ -[MPSNDArrayExponentBase10Gradient initWithDevice:]
+ -[MPSNDArrayExponentBase2 initWithDevice:]
+ -[MPSNDArrayExponentBase2Gradient initWithDevice:]
+ -[MPSNDArrayExponentGradient initWithDevice:]
+ -[MPSNDArrayFloor initWithDevice:]
+ -[MPSNDArrayFloorGradient initWithDevice:]
+ -[MPSNDArrayFourierTransform axesMask]
+ -[MPSNDArrayFourierTransform copyWithZone:device:]
+ -[MPSNDArrayFourierTransform dealloc]
+ -[MPSNDArrayFourierTransform debugDescription]
+ -[MPSNDArrayFourierTransform encodeWithCoder:]
+ -[MPSNDArrayFourierTransform initWithCoder:device:]
+ -[MPSNDArrayFourierTransform initWithDevice:axesMask:scale:scalingMode:inverse:]
+ -[MPSNDArrayFourierTransform inverse]
+ -[MPSNDArrayFourierTransform kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayFourierTransform scale]
+ -[MPSNDArrayFourierTransform scalingMode]
+ -[MPSNDArrayFourierTransform setAxesMask:]
+ -[MPSNDArrayFourierTransform setInverse:]
+ -[MPSNDArrayFourierTransform setScale:]
+ -[MPSNDArrayFourierTransform setScalingMode:]
+ -[MPSNDArrayFourierTransform usesVectorFunctionsOnOutput:]
+ -[MPSNDArrayFourierTransform workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayGather axis]
+ -[MPSNDArrayGather destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayGather dimensionsNotToBeBroadcast]
+ -[MPSNDArrayGather encodeToCommandBuffer:primarySourceArray:secondarySourceArray:]
+ -[MPSNDArrayGather encodeToCommandBuffer:primarySourceArray:secondarySourceArray:destinationArray:]
+ -[MPSNDArrayGather initWithDevice:]
+ -[MPSNDArrayGather kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGather setAxis:]
+ -[MPSNDArrayGatherGradient dimensionsNotToBeBroadcast]
+ -[MPSNDArrayGatherGradient encodeToCommandBuffer:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayGatherGradient initWithDevice:]
+ -[MPSNDArrayGatherGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGatherGradientState destinationArrayDescriptorForSourceArrays:sourceGradientIndex:]
+ -[MPSNDArrayGatherND allowNegativeIndices]
+ -[MPSNDArrayGatherND batchDimensions]
+ -[MPSNDArrayGatherND copyWithZone:device:]
+ -[MPSNDArrayGatherND dimensionsNotToBeBroadcast]
+ -[MPSNDArrayGatherND encodeToCommandBuffer:primarySourceArray:secondarySourceArray:destinationArray:]
+ -[MPSNDArrayGatherND encodeWithCoder:]
+ -[MPSNDArrayGatherND initWithCoder:device:]
+ -[MPSNDArrayGatherND initWithDevice:]
+ -[MPSNDArrayGatherND kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGatherND setAllowNegativeIndices:]
+ -[MPSNDArrayGatherND setBatchDimensions:]
+ -[MPSNDArrayGatherNDGradient allowNegativeIndices]
+ -[MPSNDArrayGatherNDGradient batchDimensions]
+ -[MPSNDArrayGatherNDGradient copyWithZone:device:]
+ -[MPSNDArrayGatherNDGradient dealloc]
+ -[MPSNDArrayGatherNDGradient dimensionsNotToBeBroadcast]
+ -[MPSNDArrayGatherNDGradient encodeWithCoder:]
+ -[MPSNDArrayGatherNDGradient initWithCoder:device:]
+ -[MPSNDArrayGatherNDGradient initWithDevice:]
+ -[MPSNDArrayGatherNDGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGatherNDGradient setAllowNegativeIndices:]
+ -[MPSNDArrayGatherNDGradient setBatchDimensions:]
+ -[MPSNDArrayGradientState dealloc]
+ -[MPSNDArrayGradientState destinationArrayDescriptorForSourceArrays:sourceGradientIndex:]
+ -[MPSNDArrayGradientState initWithSourceCount:]
+ -[MPSNDArrayGreaterThan initWithDevice:]
+ -[MPSNDArrayGreaterThanOrEqualTo initWithDevice:]
+ -[MPSNDArrayGreaterThanOrEqualToPrimaryGradient initWithDevice:]
+ -[MPSNDArrayGreaterThanOrEqualToSecondaryGradient initWithDevice:]
+ -[MPSNDArrayGreaterThanPrimaryGradient initWithDevice:]
+ -[MPSNDArrayGreaterThanSecondaryGradient initWithDevice:]
+ -[MPSNDArrayGridSample alignCorners]
+ -[MPSNDArrayGridSample constantValue]
+ -[MPSNDArrayGridSample copyWithZone:device:]
+ -[MPSNDArrayGridSample dataFormat]
+ -[MPSNDArrayGridSample destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayGridSample dimensionsToBeRetained]
+ -[MPSNDArrayGridSample encodeWithCoder:]
+ -[MPSNDArrayGridSample initWithCoder:device:]
+ -[MPSNDArrayGridSample initWithDevice:]
+ -[MPSNDArrayGridSample kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGridSample nearestMode]
+ -[MPSNDArrayGridSample normalizeCoordinates]
+ -[MPSNDArrayGridSample paddingMode]
+ -[MPSNDArrayGridSample relativeCoordinates]
+ -[MPSNDArrayGridSample samplingMode]
+ -[MPSNDArrayGridSample setAlignCorners:]
+ -[MPSNDArrayGridSample setConstantValue:]
+ -[MPSNDArrayGridSample setDataFormat:]
+ -[MPSNDArrayGridSample setNearestMode:]
+ -[MPSNDArrayGridSample setNormalizeCoordinates:]
+ -[MPSNDArrayGridSample setPaddingMode:]
+ -[MPSNDArrayGridSample setRelativeCoordinates:]
+ -[MPSNDArrayGridSample setSamplingMode:]
+ -[MPSNDArrayGridSample supportsGradientForSourceIndex:]
+ -[MPSNDArrayHammingDistanceKernel copyWithZone:device:]
+ -[MPSNDArrayHammingDistanceKernel dimensionsNotToBeBroadcast]
+ -[MPSNDArrayHammingDistanceKernel dimensionsToBeRetained]
+ -[MPSNDArrayHammingDistanceKernel encodeWithCoder:]
+ -[MPSNDArrayHammingDistanceKernel initWithCoder:device:]
+ -[MPSNDArrayHammingDistanceKernel initWithDevice:]
+ -[MPSNDArrayHammingDistanceKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayHammingDistanceKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayHammingDistanceKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayIdentity copyWithZone:device:]
+ -[MPSNDArrayIdentity dealloc]
+ -[MPSNDArrayIdentity encodeWithCoder:]
+ -[MPSNDArrayIdentity initWithCoder:device:]
+ -[MPSNDArrayIdentity initWithDevice:]
+ -[MPSNDArrayIdentity kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayIdentity reshapeWithCommandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:]
+ -[MPSNDArrayIdentity reshapeWithCommandBuffer:sourceArray:shape:destinationArray:]
+ -[MPSNDArrayIdentity reshapeWithCommandEncoder:commandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:]
+ -[MPSNDArrayIdentity reshapeWithCommandEncoder:commandBuffer:sourceArray:shape:destinationArray:]
+ -[MPSNDArrayIdentity usesVectorFunctionsOnOutput:]
+ -[MPSNDArrayIdentity workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayIm2colDescriptor copyWithZone:]
+ -[MPSNDArrayIm2colDescriptor dataLayout]
+ -[MPSNDArrayIm2colDescriptor dilationRateInX]
+ -[MPSNDArrayIm2colDescriptor dilationRateInY]
+ -[MPSNDArrayIm2colDescriptor init]
+ -[MPSNDArrayIm2colDescriptor kernelHeight]
+ -[MPSNDArrayIm2colDescriptor kernelWidth]
+ -[MPSNDArrayIm2colDescriptor paddingBottom]
+ -[MPSNDArrayIm2colDescriptor paddingLeft]
+ -[MPSNDArrayIm2colDescriptor paddingRight]
+ -[MPSNDArrayIm2colDescriptor paddingTop]
+ -[MPSNDArrayIm2colDescriptor setDataLayout:]
+ -[MPSNDArrayIm2colDescriptor setDilationRateInX:]
+ -[MPSNDArrayIm2colDescriptor setDilationRateInY:]
+ -[MPSNDArrayIm2colDescriptor setKernelHeight:]
+ -[MPSNDArrayIm2colDescriptor setKernelWidth:]
+ -[MPSNDArrayIm2colDescriptor setPaddingBottom:]
+ -[MPSNDArrayIm2colDescriptor setPaddingLeft:]
+ -[MPSNDArrayIm2colDescriptor setPaddingRight:]
+ -[MPSNDArrayIm2colDescriptor setPaddingTop:]
+ -[MPSNDArrayIm2colDescriptor setStrideInPixelsX:]
+ -[MPSNDArrayIm2colDescriptor setStrideInPixelsY:]
+ -[MPSNDArrayIm2colDescriptor strideInPixelsX]
+ -[MPSNDArrayIm2colDescriptor strideInPixelsY]
+ -[MPSNDArrayIm2colKernel copyWithZone:device:]
+ -[MPSNDArrayIm2colKernel dataLayout]
+ -[MPSNDArrayIm2colKernel dilationHeight]
+ -[MPSNDArrayIm2colKernel dilationWidth]
+ -[MPSNDArrayIm2colKernel encodeWithCoder:]
+ -[MPSNDArrayIm2colKernel initWithCoder:device:]
+ -[MPSNDArrayIm2colKernel initWithDevice:ndArrayIm2colDescriptor:]
+ -[MPSNDArrayIm2colKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayIm2colKernel kernelHeight]
+ -[MPSNDArrayIm2colKernel kernelWidth]
+ -[MPSNDArrayIm2colKernel paddingBottom]
+ -[MPSNDArrayIm2colKernel paddingLeft]
+ -[MPSNDArrayIm2colKernel paddingRight]
+ -[MPSNDArrayIm2colKernel paddingTop]
+ -[MPSNDArrayIm2colKernel setDataLayout:]
+ -[MPSNDArrayIm2colKernel setDilationHeight:]
+ -[MPSNDArrayIm2colKernel setDilationWidth:]
+ -[MPSNDArrayIm2colKernel setKernelHeight:]
+ -[MPSNDArrayIm2colKernel setKernelWidth:]
+ -[MPSNDArrayIm2colKernel setPaddingBottom:]
+ -[MPSNDArrayIm2colKernel setPaddingLeft:]
+ -[MPSNDArrayIm2colKernel setPaddingRight:]
+ -[MPSNDArrayIm2colKernel setPaddingTop:]
+ -[MPSNDArrayIm2colKernel setStrideHeight:]
+ -[MPSNDArrayIm2colKernel setStrideWidth:]
+ -[MPSNDArrayIm2colKernel strideHeight]
+ -[MPSNDArrayIm2colKernel strideWidth]
+ -[MPSNDArrayInitialization copyWithZone:device:]
+ -[MPSNDArrayInitialization dealloc]
+ -[MPSNDArrayInitialization encodeToCommandBuffer:destinationArray:]
+ -[MPSNDArrayInitialization encodeToCommandBuffer:destinationDescriptor:]
+ -[MPSNDArrayInitialization encodeWithCoder:]
+ -[MPSNDArrayInitialization initWithCoder:device:]
+ -[MPSNDArrayInitialization initWithDevice:sourceCount:]
+ -[MPSNDArrayInitialization kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitialization kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayInitialization kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ -[MPSNDArrayInitializationConstant constantValue]
+ -[MPSNDArrayInitializationConstant copyWithZone:device:]
+ -[MPSNDArrayInitializationConstant initWithCoder:device:]
+ -[MPSNDArrayInitializationConstant initWithDevice:constantValue:]
+ -[MPSNDArrayInitializationConstant initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationConstant kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayInitializationGlorotNormal FanIn]
+ -[MPSNDArrayInitializationGlorotNormal FanOut]
+ -[MPSNDArrayInitializationGlorotNormal copyWithZone:device:]
+ -[MPSNDArrayInitializationGlorotNormal encodeToCommandBuffer:destinationArray:]
+ -[MPSNDArrayInitializationGlorotNormal initWithCoder:device:]
+ -[MPSNDArrayInitializationGlorotNormal initWithDevice:seed:]
+ -[MPSNDArrayInitializationGlorotNormal initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationGlorotNormal kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitializationGlorotNormal setFanIn:]
+ -[MPSNDArrayInitializationGlorotNormal setFanOut:]
+ -[MPSNDArrayInitializationGlorotUniform FanIn]
+ -[MPSNDArrayInitializationGlorotUniform FanOut]
+ -[MPSNDArrayInitializationGlorotUniform copyWithZone:device:]
+ -[MPSNDArrayInitializationGlorotUniform encodeToCommandBuffer:destinationArray:]
+ -[MPSNDArrayInitializationGlorotUniform initWithCoder:device:]
+ -[MPSNDArrayInitializationGlorotUniform initWithDevice:seed:]
+ -[MPSNDArrayInitializationGlorotUniform initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationGlorotUniform kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitializationGlorotUniform setFanIn:]
+ -[MPSNDArrayInitializationGlorotUniform setFanOut:]
+ -[MPSNDArrayInitializationIdentity copyWithZone:device:]
+ -[MPSNDArrayInitializationIdentity initWithCoder:device:]
+ -[MPSNDArrayInitializationIdentity initWithDevice:]
+ -[MPSNDArrayInitializationIdentity initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationIdentity kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayInitializationRandomNormal copyWithZone:device:]
+ -[MPSNDArrayInitializationRandomNormal initWithCoder:device:]
+ -[MPSNDArrayInitializationRandomNormal initWithDevice:mean:standardDeviation:seed:]
+ -[MPSNDArrayInitializationRandomNormal initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationRandomNormal kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitializationRandomNormal mean]
+ -[MPSNDArrayInitializationRandomNormal standardDeviation]
+ -[MPSNDArrayInitializationRandomUniform copyWithZone:device:]
+ -[MPSNDArrayInitializationRandomUniform initWithCoder:device:]
+ -[MPSNDArrayInitializationRandomUniform initWithDevice:minimum:maximum:seed:]
+ -[MPSNDArrayInitializationRandomUniform initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationRandomUniform kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitializationRandomUniform maximum]
+ -[MPSNDArrayInitializationRandomUniform minimum]
+ -[MPSNDArrayInitializationTruncatedNormal copyWithZone:device:]
+ -[MPSNDArrayInitializationTruncatedNormal initWithCoder:device:]
+ -[MPSNDArrayInitializationTruncatedNormal initWithDevice:mean:standardDeviation:seed:]
+ -[MPSNDArrayInitializationTruncatedNormal initWithDevice:sourceCount:]
+ -[MPSNDArrayInitializationTruncatedNormal kernelDimensionalityForDestinationArray:]
+ -[MPSNDArrayInitializationTruncatedNormal mean]
+ -[MPSNDArrayInitializationTruncatedNormal standardDeviation]
+ -[MPSNDArrayIsFinite initWithDevice:]
+ -[MPSNDArrayIsFiniteGradient initWithDevice:]
+ -[MPSNDArrayIsInfinite initWithDevice:]
+ -[MPSNDArrayIsInfiniteGradient initWithDevice:]
+ -[MPSNDArrayIsNaN initWithDevice:]
+ -[MPSNDArrayIsNaNGradient initWithDevice:]
+ -[MPSNDArrayLUTDequantize copyWithZone:device:]
+ -[MPSNDArrayLUTDequantize encodeWithCoder:]
+ -[MPSNDArrayLUTDequantize initWithCoder:device:]
+ -[MPSNDArrayLUTDequantize initWithDevice:]
+ -[MPSNDArrayLUTDequantize kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayLUTGEMV copyWithZone:device:]
+ -[MPSNDArrayLUTGEMV dealloc]
+ -[MPSNDArrayLUTGEMV encodeWithCoder:]
+ -[MPSNDArrayLUTGEMV hasLUTLHS]
+ -[MPSNDArrayLUTGEMV hasLUTRHS]
+ -[MPSNDArrayLUTGEMV initWithCoder:device:]
+ -[MPSNDArrayLUTGEMV initWithDevice:hasLUTLHS:hasLUTRHS:]
+ -[MPSNDArrayLUTGEMV initWithDevice:lhsDesc:rhsDesc:]
+ -[MPSNDArrayLUTGEMV kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayLUTGEMV setHasLUTLHS:]
+ -[MPSNDArrayLUTGEMV setHasLUTRHS:]
+ -[MPSNDArrayLUTGEMV workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayLUTQuantizationDescriptor copyWithZone:]
+ -[MPSNDArrayLUTQuantizationDescriptor dealloc]
+ -[MPSNDArrayLUTQuantizationDescriptor getNDArrayCount]
+ -[MPSNDArrayLUTQuantizationDescriptor initWithDataType:]
+ -[MPSNDArrayLUTQuantizationDescriptor initWithDataType:vectorAxes:]
+ -[MPSNDArrayLUTQuantizationDescriptor initWithDataType:vectorAxis:]
+ -[MPSNDArrayLUTQuantizationDescriptor setVectorAxes:]
+ -[MPSNDArrayLUTQuantizationDescriptor vectorAxes]
+ -[MPSNDArrayLessThan initWithDevice:]
+ -[MPSNDArrayLessThanOrEqualTo initWithDevice:]
+ -[MPSNDArrayLessThanOrEqualToPrimaryGradient initWithDevice:]
+ -[MPSNDArrayLessThanOrEqualToSecondaryGradient initWithDevice:]
+ -[MPSNDArrayLessThanPrimaryGradient initWithDevice:]
+ -[MPSNDArrayLessThanSecondaryGradient initWithDevice:]
+ -[MPSNDArrayLocalConvolution copyWithZone:device:]
+ -[MPSNDArrayLocalConvolution dataFormat]
+ -[MPSNDArrayLocalConvolution destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayLocalConvolution dilationRates]
+ -[MPSNDArrayLocalConvolution dimensionsNotToBeBroadcast]
+ -[MPSNDArrayLocalConvolution dimensionsToBeRetained]
+ -[MPSNDArrayLocalConvolution encodeWithCoder:]
+ -[MPSNDArrayLocalConvolution initWithCoder:device:]
+ -[MPSNDArrayLocalConvolution initWithDevice:]
+ -[MPSNDArrayLocalConvolution kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayLocalConvolution kernelSizes]
+ -[MPSNDArrayLocalConvolution setDataFormat:]
+ -[MPSNDArrayLocalConvolution setDilationRates:]
+ -[MPSNDArrayLocalConvolution setKernelSizes:]
+ -[MPSNDArrayLocalConvolution supportsGradientForSourceIndex:]
+ -[MPSNDArrayLogSoftMax axis]
+ -[MPSNDArrayLogSoftMax copyWithZone:device:]
+ -[MPSNDArrayLogSoftMax dimensionsToBeRetained]
+ -[MPSNDArrayLogSoftMax encodeWithCoder:]
+ -[MPSNDArrayLogSoftMax initWithCoder:device:]
+ -[MPSNDArrayLogSoftMax initWithDevice:]
+ -[MPSNDArrayLogSoftMax initWithDevice:axis:]
+ -[MPSNDArrayLogSoftMax kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayLogSoftMax reshapeFitToTileToCommandBuffer:currentSource:kernelDimension:dimensionsToBeRetained:]
+ -[MPSNDArrayLogSoftMax setAxis:]
+ -[MPSNDArrayLogSoftMaxGradient axis]
+ -[MPSNDArrayLogSoftMaxGradient copyWithZone:device:]
+ -[MPSNDArrayLogSoftMaxGradient dimensionsToBeRetained]
+ -[MPSNDArrayLogSoftMaxGradient encodeWithCoder:]
+ -[MPSNDArrayLogSoftMaxGradient initWithCoder:device:]
+ -[MPSNDArrayLogSoftMaxGradient initWithDevice:axis:]
+ -[MPSNDArrayLogSoftMaxGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayLogSoftMaxGradient setAxis:]
+ -[MPSNDArrayLogarithm initWithDevice:]
+ -[MPSNDArrayLogarithmBase10 initWithDevice:]
+ -[MPSNDArrayLogarithmBase10Gradient initWithDevice:]
+ -[MPSNDArrayLogarithmBase2 initWithDevice:]
+ -[MPSNDArrayLogarithmBase2Gradient initWithDevice:]
+ -[MPSNDArrayLogarithmGradient initWithDevice:]
+ -[MPSNDArrayMaterializeSparseTensor copyWithZone:device:]
+ -[MPSNDArrayMaterializeSparseTensor dealloc]
+ -[MPSNDArrayMaterializeSparseTensor dimensionsNotToBeBroadcast]
+ -[MPSNDArrayMaterializeSparseTensor encodeWithCoder:]
+ -[MPSNDArrayMaterializeSparseTensor initWithCoder:device:]
+ -[MPSNDArrayMaterializeSparseTensor initWithDevice:sourceCount:]
+ -[MPSNDArrayMaterializeSparseTensor kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMaterializeSparseTensor setSparseFormat:]
+ -[MPSNDArrayMaterializeSparseTensor sparseFormat]
+ -[MPSNDArrayMaterializeSparseTensor workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayMathBinaryKernel copyWithZone:device:]
+ -[MPSNDArrayMathBinaryKernel encodeWithCoder:]
+ -[MPSNDArrayMathBinaryKernel initWithCoder:device:]
+ -[MPSNDArrayMathBinaryKernel initWithDevice:]
+ -[MPSNDArrayMathBinaryPrimaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathBinaryPrimaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathBinaryPrimaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathBinaryPrimaryGradient initWithDevice:]
+ -[MPSNDArrayMathBinarySecondaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathBinarySecondaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathBinarySecondaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathBinarySecondaryGradient initWithDevice:]
+ -[MPSNDArrayMathTernaryKernel copyWithZone:device:]
+ -[MPSNDArrayMathTernaryKernel encodeWithCoder:]
+ -[MPSNDArrayMathTernaryKernel initWithCoder:device:]
+ -[MPSNDArrayMathTernaryKernel initWithDevice:]
+ -[MPSNDArrayMathTernaryPrimaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathTernaryPrimaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathTernaryPrimaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathTernaryPrimaryGradient initWithDevice:]
+ -[MPSNDArrayMathTernarySecondaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathTernarySecondaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathTernarySecondaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathTernarySecondaryGradient initWithDevice:]
+ -[MPSNDArrayMathTernaryTertiaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathTernaryTertiaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathTernaryTertiaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathTernaryTertiaryGradient initWithDevice:]
+ -[MPSNDArrayMathUnaryGradient copyWithZone:device:]
+ -[MPSNDArrayMathUnaryGradient encodeWithCoder:]
+ -[MPSNDArrayMathUnaryGradient initWithCoder:device:]
+ -[MPSNDArrayMathUnaryGradient initWithDevice:]
+ -[MPSNDArrayMathUnaryKernel copyWithZone:device:]
+ -[MPSNDArrayMathUnaryKernel encodeWithCoder:]
+ -[MPSNDArrayMathUnaryKernel initWithCoder:device:]
+ -[MPSNDArrayMathUnaryKernel initWithDevice:]
+ -[MPSNDArrayMatrixMultiplication alpha]
+ -[MPSNDArrayMatrixMultiplication beta]
+ -[MPSNDArrayMatrixMultiplication clearAutoTuningParameters]
+ -[MPSNDArrayMatrixMultiplication copyWithZone:device:]
+ -[MPSNDArrayMatrixMultiplication dealloc]
+ -[MPSNDArrayMatrixMultiplication destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayMatrixMultiplication dimensionsNotToBeBroadcast]
+ -[MPSNDArrayMatrixMultiplication encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMatrixMultiplication encodeToCommandEncoder:commandBuffer:sourceArrays:normScaleArray:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMatrixMultiplication encodeWithCoder:]
+ -[MPSNDArrayMatrixMultiplication initWithCoder:device:]
+ -[MPSNDArrayMatrixMultiplication initWithDevice:sourceCount:]
+ -[MPSNDArrayMatrixMultiplication kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMatrixMultiplication kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ -[MPSNDArrayMatrixMultiplication normFusionDescriptor]
+ -[MPSNDArrayMatrixMultiplication setAlpha:]
+ -[MPSNDArrayMatrixMultiplication setAutoTuningParameters:]
+ -[MPSNDArrayMatrixMultiplication setAutoTuningTarget:]
+ -[MPSNDArrayMatrixMultiplication setBeta:]
+ -[MPSNDArrayMatrixMultiplication setNormFusionDescriptor:]
+ -[MPSNDArrayMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayMatrixMultiplicationGradient alpha]
+ -[MPSNDArrayMatrixMultiplicationGradient beta]
+ -[MPSNDArrayMatrixMultiplicationGradient copyWithZone:device:]
+ -[MPSNDArrayMatrixMultiplicationGradient destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayMatrixMultiplicationGradient dimensionsNotToBeBroadcast]
+ -[MPSNDArrayMatrixMultiplicationGradient encodeWithCoder:]
+ -[MPSNDArrayMatrixMultiplicationGradient initWithCoder:device:]
+ -[MPSNDArrayMatrixMultiplicationGradient initWithDevice:sourceCount:sourceGradientIndex:]
+ -[MPSNDArrayMatrixMultiplicationGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMatrixMultiplicationGradient maxSupportedDimensionsForSourceArrays:destinationArray:]
+ -[MPSNDArrayMatrixMultiplicationGradient setAlpha:]
+ -[MPSNDArrayMatrixMultiplicationGradient setBeta:]
+ -[MPSNDArrayMatrixMultiplicationGradient workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayMatrixMultiplicationSparse copyWithZone:device:]
+ -[MPSNDArrayMatrixMultiplicationSparse dealloc]
+ -[MPSNDArrayMatrixMultiplicationSparse denseSparse]
+ -[MPSNDArrayMatrixMultiplicationSparse dimensionsNotToBeBroadcast]
+ -[MPSNDArrayMatrixMultiplicationSparse encodeWithCoder:]
+ -[MPSNDArrayMatrixMultiplicationSparse initWithCoder:device:]
+ -[MPSNDArrayMatrixMultiplicationSparse initWithDevice:sourceCount:]
+ -[MPSNDArrayMatrixMultiplicationSparse kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMatrixMultiplicationSparse setDenseSparse:]
+ -[MPSNDArrayMatrixMultiplicationSparse setSparseFormat:]
+ -[MPSNDArrayMatrixMultiplicationSparse setStructuredSparse:]
+ -[MPSNDArrayMatrixMultiplicationSparse setTransposeSparse:]
+ -[MPSNDArrayMatrixMultiplicationSparse sparseFormat]
+ -[MPSNDArrayMatrixMultiplicationSparse structuredSparse]
+ -[MPSNDArrayMatrixMultiplicationSparse transposeSparse]
+ -[MPSNDArrayMatrixMultiplicationSparse workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayMaximum initWithDevice:]
+ -[MPSNDArrayMaximumPrimaryGradient initWithDevice:]
+ -[MPSNDArrayMaximumSecondaryGradient initWithDevice:]
+ -[MPSNDArrayMinimum initWithDevice:]
+ -[MPSNDArrayMinimumPrimaryGradient initWithDevice:]
+ -[MPSNDArrayMinimumSecondaryGradient initWithDevice:]
+ -[MPSNDArrayModulo initWithDevice:]
+ -[MPSNDArrayModuloPrimaryGradient initWithDevice:]
+ -[MPSNDArrayModuloSecondaryGradient initWithDevice:]
+ -[MPSNDArrayMultiaryBase copyToGradientState:sourceArrays:sourceStates:destinationArray:]
+ -[MPSNDArrayMultiaryBase copyWithZone:device:]
+ -[MPSNDArrayMultiaryBase dealloc]
+ -[MPSNDArrayMultiaryBase destinationArrayAllocator]
+ -[MPSNDArrayMultiaryBase destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayMultiaryBase destinationStrides]
+ -[MPSNDArrayMultiaryBase dilationRatesForSourceIndex:]
+ -[MPSNDArrayMultiaryBase dimensionsNotToBeBroadcast]
+ -[MPSNDArrayMultiaryBase dimensionsToBeRetained]
+ -[MPSNDArrayMultiaryBase edgeModeAtSourceIndex:]
+ -[MPSNDArrayMultiaryBase encodeWithCoder:]
+ -[MPSNDArrayMultiaryBase getDestContiguousFunctionConstant:]
+ -[MPSNDArrayMultiaryBase initWithCoder:device:]
+ -[MPSNDArrayMultiaryBase initWithDevice:sourceCount:]
+ -[MPSNDArrayMultiaryBase kernelDAGObjectSetup:sourceArrays:sourceGradient:destination:]
+ -[MPSNDArrayMultiaryBase kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMultiaryBase kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ -[MPSNDArrayMultiaryBase kernelSizesForSourceIndex:]
+ -[MPSNDArrayMultiaryBase maxSupportedArraySizeForIsDestination:]
+ -[MPSNDArrayMultiaryBase maxSupportedDimensionsForSourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryBase offsetsAtSourceIndex:]
+ -[MPSNDArrayMultiaryBase reshapeFitToTileToCommandBuffer:currentSource:kernelDimension:dimensionsToBeRetained:]
+ -[MPSNDArrayMultiaryBase resultStateForSourceArrays:sourceStates:destinationArray:]
+ -[MPSNDArrayMultiaryBase setDestinationArrayAllocator:]
+ -[MPSNDArrayMultiaryBase setIndexingArithmaticTypeMask:sourceArrays:sourceGradient:destination:tileDimensions:]
+ -[MPSNDArrayMultiaryBase stridesAtSourceIndex:]
+ -[MPSNDArrayMultiaryBase stridesForSourceIndex:]
+ -[MPSNDArrayMultiaryBase temporaryResultStateForCommandBuffer:sourceArrays:sourceStates:destinationArray:]
+ -[MPSNDArrayMultiaryBase usesVectorFunctionsOnOutput:]
+ -[MPSNDArrayMultiaryBase workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayMultiaryBase workloadStatisticsForSourceArrays:destArrays:sourceState:]
+ -[MPSNDArrayMultiaryBase workloadStatisticsForSourceArrays:sourceState:]
+ -[MPSNDArrayMultiaryGradientKernel copyWithZone:device:]
+ -[MPSNDArrayMultiaryGradientKernel encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:]
+ -[MPSNDArrayMultiaryGradientKernel encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayMultiaryGradientKernel encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryGradientKernel encodeToCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryGradientKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryGradientKernel encodeWithCoder:]
+ -[MPSNDArrayMultiaryGradientKernel initWithCoder:device:]
+ -[MPSNDArrayMultiaryGradientKernel initWithDevice:sourceCount:sourceGradientIndex:]
+ -[MPSNDArrayMultiaryKernel copyWithZone:device:]
+ -[MPSNDArrayMultiaryKernel destinationGradientArrayDescriptorsForSourceArrays:sourceGradient:sourceState:]
+ -[MPSNDArrayMultiaryKernel destinationGradientsSupported]
+ -[MPSNDArrayMultiaryKernel encodeGradientsToCommandBuffer:sourceArrays:sourceGradient:gradientState:]
+ -[MPSNDArrayMultiaryKernel encodeGradientsToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:]
+ -[MPSNDArrayMultiaryKernel encodeGradientsToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodeGradientsToCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:resultState:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:resultState:outputStateIsTemporary:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel firstGradientDestinationFromDestinationGradients:outMaxNumDimensions:]
+ -[MPSNDArrayMultiaryKernel initWithCoder:device:]
+ -[MPSNDArrayMultiaryKernel initWithDevice:sourceCount:]
+ -[MPSNDArrayMultiaryKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayMultiaryMultiDestinationBase copyWithZone:device:]
+ -[MPSNDArrayMultiaryMultiDestinationBase dealloc]
+ -[MPSNDArrayMultiaryMultiDestinationBase encodeWithCoder:]
+ -[MPSNDArrayMultiaryMultiDestinationBase initWithCoder:device:]
+ -[MPSNDArrayMultiaryMultiDestinationBase initWithDevice:sourceCount:destinationCount:]
+ -[MPSNDArrayMultiaryMultiDestinationBase kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel copyWithZone:device:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel encodeToCommandBuffer:sourceArrays:destinationArrays:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArrays:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArrays:activeDestinationMask:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArrays:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArrays:activeDestinationMask:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel initWithCoder:device:]
+ -[MPSNDArrayMultiaryMultiDestinationKernel initWithDevice:sourceCount:destinationCount:]
+ -[MPSNDArrayMultiplication initWithDevice:]
+ -[MPSNDArrayMultiplicationPrimaryGradient initWithDevice:]
+ -[MPSNDArrayMultiplicationSecondaryGradient initWithDevice:]
+ -[MPSNDArrayNAND initWithDevice:]
+ -[MPSNDArrayNANDPrimaryGradient initWithDevice:]
+ -[MPSNDArrayNANDSecondaryGradient initWithDevice:]
+ -[MPSNDArrayNMS IOUThreshold]
+ -[MPSNDArrayNMS copyWithZone:device:]
+ -[MPSNDArrayNMS dealloc]
+ -[MPSNDArrayNMS encodeWithCoder:]
+ -[MPSNDArrayNMS initWithCoder:device:]
+ -[MPSNDArrayNMS initWithDevice:scoreThreshold:]
+ -[MPSNDArrayNMS kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayNMS maxBoxes]
+ -[MPSNDArrayNMS scoreThreshold]
+ -[MPSNDArrayNMS setIOUThreshold:]
+ -[MPSNDArrayNMS setMaxBoxes:]
+ -[MPSNDArrayNMS setScoreThreshold:]
+ -[MPSNDArrayNOR initWithDevice:]
+ -[MPSNDArrayNORPrimaryGradient initWithDevice:]
+ -[MPSNDArrayNORSecondaryGradient initWithDevice:]
+ -[MPSNDArrayNOT initWithDevice:]
+ -[MPSNDArrayNOTGradient initWithDevice:]
+ -[MPSNDArrayNegative initWithDevice:]
+ -[MPSNDArrayNegativeGradient initWithDevice:]
+ -[MPSNDArrayNeuronGeLU initWithDevice:]
+ -[MPSNDArrayNeuronGeLUGradient initWithDevice:]
+ -[MPSNDArrayNeuronGradient copyWithZone:device:]
+ -[MPSNDArrayNeuronGradient encodeWithCoder:]
+ -[MPSNDArrayNeuronGradient initWithCoder:device:]
+ -[MPSNDArrayNeuronGradient initWithDevice:]
+ -[MPSNDArrayNeuronKernel copyWithZone:device:]
+ -[MPSNDArrayNeuronKernel encodeWithCoder:]
+ -[MPSNDArrayNeuronKernel initWithCoder:device:]
+ -[MPSNDArrayNeuronKernel initWithDevice:]
+ -[MPSNDArrayNormFusionDescriptor copyWithZone:]
+ -[MPSNDArrayNormFusionDescriptor epsilon]
+ -[MPSNDArrayNormFusionDescriptor hasScale]
+ -[MPSNDArrayNormFusionDescriptor init]
+ -[MPSNDArrayNormFusionDescriptor isLeftFused]
+ -[MPSNDArrayNormFusionDescriptor normFusionType]
+ -[MPSNDArrayNormFusionDescriptor setEpsilon:]
+ -[MPSNDArrayNormFusionDescriptor setHasScale:]
+ -[MPSNDArrayNormFusionDescriptor setIsLeftFused:]
+ -[MPSNDArrayNormFusionDescriptor setNormFusionType:]
+ -[MPSNDArrayNotEqual initWithDevice:]
+ -[MPSNDArrayNotEqualPrimaryGradient initWithDevice:]
+ -[MPSNDArrayNotEqualSecondaryGradient initWithDevice:]
+ -[MPSNDArrayOR initWithDevice:]
+ -[MPSNDArrayORPrimaryGradient initWithDevice:]
+ -[MPSNDArrayORSecondaryGradient initWithDevice:]
+ -[MPSNDArrayOffsetIdentity hasDestinationOffset]
+ -[MPSNDArrayOffsetIdentity initWithDevice:]
+ -[MPSNDArrayOffsetIdentity kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayOffsetIdentity setHasDestinationOffset:]
+ -[MPSNDArrayPadGradientKernel copyWithZone:device:]
+ -[MPSNDArrayPadGradientKernel dimensionsToBeRetained]
+ -[MPSNDArrayPadGradientKernel edgeMode]
+ -[MPSNDArrayPadGradientKernel encodeWithCoder:]
+ -[MPSNDArrayPadGradientKernel initWithCoder:device:]
+ -[MPSNDArrayPadGradientKernel initWithDevice:edgeMode:paddingSize:]
+ -[MPSNDArrayPadGradientKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayPadGradientKernel paddingSize]
+ -[MPSNDArrayPadKernel constantValueImagPart]
+ -[MPSNDArrayPadKernel constantValue]
+ -[MPSNDArrayPadKernel copyWithZone:device:]
+ -[MPSNDArrayPadKernel dealloc]
+ -[MPSNDArrayPadKernel destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayPadKernel dimensionsNotToBeBroadcast]
+ -[MPSNDArrayPadKernel dimensionsToBeRetained]
+ -[MPSNDArrayPadKernel edgeMode]
+ -[MPSNDArrayPadKernel encodeWithCoder:]
+ -[MPSNDArrayPadKernel initWithCoder:device:]
+ -[MPSNDArrayPadKernel initWithDevice:edgeMode:constantValue:paddingSize:]
+ -[MPSNDArrayPadKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayPadKernel paddingSize]
+ -[MPSNDArrayPadKernel setConstantValueImagPart:]
+ -[MPSNDArrayPoolingKernel copyWithZone:device:]
+ -[MPSNDArrayPoolingKernel debugDescription]
+ -[MPSNDArrayPoolingKernel dimensionsNotToBeBroadcast]
+ -[MPSNDArrayPoolingKernel dimensionsToBeRetained]
+ -[MPSNDArrayPoolingKernel encodeWithCoder:]
+ -[MPSNDArrayPoolingKernel initWithCoder:device:]
+ -[MPSNDArrayPoolingKernel initWithDevice:kernelSizes:poolingMode:]
+ -[MPSNDArrayPoolingKernel initWithDevice:kernelSizes:poolingMode:returnIndicesMode:]
+ -[MPSNDArrayPoolingKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayPoolingKernel poolingDilationRates]
+ -[MPSNDArrayPoolingKernel poolingGradientWithIndices]
+ -[MPSNDArrayPoolingKernel poolingKernelSizes]
+ -[MPSNDArrayPoolingKernel poolingMode]
+ -[MPSNDArrayPoolingKernel poolingOffsets]
+ -[MPSNDArrayPoolingKernel poolingReturnIndicesDataType]
+ -[MPSNDArrayPoolingKernel poolingReturnIndicesMode]
+ -[MPSNDArrayPoolingKernel poolingStrides]
+ -[MPSNDArrayPoolingKernel setPoolingDilationRates:]
+ -[MPSNDArrayPoolingKernel setPoolingGradientWithIndices:]
+ -[MPSNDArrayPoolingKernel setPoolingOffsets:]
+ -[MPSNDArrayPoolingKernel setPoolingReturnIndicesDataType:]
+ -[MPSNDArrayPoolingKernel setPoolingReturnIndicesMode:]
+ -[MPSNDArrayPoolingKernel setPoolingStrides:]
+ -[MPSNDArrayPoolingKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayPoolingKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayPoolingMultiDestinationKernel computeGradient]
+ -[MPSNDArrayPoolingMultiDestinationKernel copyWithZone:device:]
+ -[MPSNDArrayPoolingMultiDestinationKernel encodeWithCoder:]
+ -[MPSNDArrayPoolingMultiDestinationKernel initWithCoder:device:]
+ -[MPSNDArrayPoolingMultiDestinationKernel initWithDevice:kernelSizes:poolingMode:]
+ -[MPSNDArrayPoolingMultiDestinationKernel initWithDevice:kernelSizes:poolingMode:computeGradient:]
+ -[MPSNDArrayPoolingMultiDestinationKernel initWithDevice:kernelSizes:poolingMode:returnIndicesMode:]
+ -[MPSNDArrayPoolingMultiDestinationKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingDilationRates]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingKernelSizes]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingMode]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingOffsets]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingReturnIndicesDataType]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingReturnIndicesMode]
+ -[MPSNDArrayPoolingMultiDestinationKernel poolingStrides]
+ -[MPSNDArrayPoolingMultiDestinationKernel setPoolingDilationRates:]
+ -[MPSNDArrayPoolingMultiDestinationKernel setPoolingOffsets:]
+ -[MPSNDArrayPoolingMultiDestinationKernel setPoolingReturnIndicesDataType:]
+ -[MPSNDArrayPoolingMultiDestinationKernel setPoolingReturnIndicesMode:]
+ -[MPSNDArrayPoolingMultiDestinationKernel setPoolingStrides:]
+ -[MPSNDArrayPoolingMultiDestinationKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayPower initWithDevice:]
+ -[MPSNDArrayPowerPrimaryGradient initWithDevice:]
+ -[MPSNDArrayPowerSecondaryGradient initWithDevice:]
+ -[MPSNDArrayPrune initWithCoder:device:]
+ -[MPSNDArrayPrune initWithDevice:]
+ -[MPSNDArrayPrune pruneMetric]
+ -[MPSNDArrayPrune pruneStructure]
+ -[MPSNDArrayPrune setPruneMetric:]
+ -[MPSNDArrayPrune setPruneStructure:]
+ -[MPSNDArrayPrune setSparsity:]
+ -[MPSNDArrayPrune sparsity]
+ -[MPSNDArrayPrune supportsGradientForSourceIndex:]
+ -[MPSNDArrayQuantizationDescriptor copyWithZone:]
+ -[MPSNDArrayQuantizationDescriptor getNDArrayCount]
+ -[MPSNDArrayQuantizationDescriptor initWithDataType:quantizationScheme:]
+ -[MPSNDArrayQuantizationDescriptor init]
+ -[MPSNDArrayQuantizationDescriptor quantizationDataType]
+ -[MPSNDArrayQuantizationDescriptor quantizationScheme]
+ -[MPSNDArrayQuantizationDescriptor setQuantizationDataType:]
+ -[MPSNDArrayQuantizedConvolution dealloc]
+ -[MPSNDArrayQuantizedConvolution initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:]
+ -[MPSNDArrayQuantizedConvolution initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:sourceCount:]
+ -[MPSNDArrayQuantizedGatherND copyWithZone:device:]
+ -[MPSNDArrayQuantizedGatherND dealloc]
+ -[MPSNDArrayQuantizedGatherND encodeWithCoder:]
+ -[MPSNDArrayQuantizedGatherND initWithCoder:device:]
+ -[MPSNDArrayQuantizedGatherND initWithDevice:quantizationDescriptor:]
+ -[MPSNDArrayQuantizedMatrixMultiplication dealloc]
+ -[MPSNDArrayQuantizedMatrixMultiplication encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayQuantizedMatrixMultiplication initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:]
+ -[MPSNDArrayQuantizedMatrixMultiplication initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:sourceCount:]
+ -[MPSNDArrayQuantizedMatrixMultiplication kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayQuantizedMatrixMultiplication kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ -[MPSNDArrayQuantizedMatrixMultiplication workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayRandom initWithDevice:]
+ -[MPSNDArrayRandom kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayRandomNormal copyWithZone:device:]
+ -[MPSNDArrayRandomNormal encodeWithCoder:]
+ -[MPSNDArrayRandomNormal initWithCoder:device:]
+ -[MPSNDArrayRandomNormal initWithDevice:]
+ -[MPSNDArrayRandomNormal initWithDevice:mean:standardDeviation:]
+ -[MPSNDArrayRandomNormal mean]
+ -[MPSNDArrayRandomNormal samplingMethod]
+ -[MPSNDArrayRandomNormal setMean:]
+ -[MPSNDArrayRandomNormal setSamplingMethod:]
+ -[MPSNDArrayRandomNormal setStandardDeviation:]
+ -[MPSNDArrayRandomNormal standardDeviation]
+ -[MPSNDArrayRandomState copyWithZone:device:]
+ -[MPSNDArrayRandomState counterStride]
+ -[MPSNDArrayRandomState encodeWithCoder:]
+ -[MPSNDArrayRandomState incrementKey]
+ -[MPSNDArrayRandomState initWithCoder:device:]
+ -[MPSNDArrayRandomState initWithDevice:]
+ -[MPSNDArrayRandomState kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayRandomState setCounterStride:]
+ -[MPSNDArrayRandomState setIncrementKey:]
+ -[MPSNDArrayRandomState setSkipElements:]
+ -[MPSNDArrayRandomState skipElements]
+ -[MPSNDArrayRandomStateDescriptor algorithm]
+ -[MPSNDArrayRandomStateDescriptor copyWithZone:]
+ -[MPSNDArrayRandomStateDescriptor dealloc]
+ -[MPSNDArrayRandomStateDescriptor encodeWithCoder:]
+ -[MPSNDArrayRandomStateDescriptor exportStateToNDArray:]
+ -[MPSNDArrayRandomStateDescriptor initPhiloxStateDescriptorWithCounterLow:counterHigh:key:]
+ -[MPSNDArrayRandomStateDescriptor initPhiloxStateDescriptorWithSeed:]
+ -[MPSNDArrayRandomStateDescriptor initWithCoder:]
+ -[MPSNDArrayRandomStateDescriptor init]
+ -[MPSNDArrayRandomStateDescriptor stateLength]
+ -[MPSNDArrayRandomStateDescriptor state]
+ -[MPSNDArrayRandomTruncatedNormal copyWithZone:device:]
+ -[MPSNDArrayRandomTruncatedNormal encodeWithCoder:]
+ -[MPSNDArrayRandomTruncatedNormal initWithCoder:device:]
+ -[MPSNDArrayRandomTruncatedNormal initWithDevice:]
+ -[MPSNDArrayRandomTruncatedNormal initWithDevice:mean:standardDeviation:]
+ -[MPSNDArrayRandomTruncatedNormal maximum]
+ -[MPSNDArrayRandomTruncatedNormal mean]
+ -[MPSNDArrayRandomTruncatedNormal minimum]
+ -[MPSNDArrayRandomTruncatedNormal samplingMethod]
+ -[MPSNDArrayRandomTruncatedNormal setMaximum:]
+ -[MPSNDArrayRandomTruncatedNormal setMean:]
+ -[MPSNDArrayRandomTruncatedNormal setMinimum:]
+ -[MPSNDArrayRandomTruncatedNormal setSamplingMethod:]
+ -[MPSNDArrayRandomTruncatedNormal setStandardDeviation:]
+ -[MPSNDArrayRandomTruncatedNormal standardDeviation]
+ -[MPSNDArrayRandomUniform copyWithZone:device:]
+ -[MPSNDArrayRandomUniform encodeWithCoder:]
+ -[MPSNDArrayRandomUniform initWithCoder:device:]
+ -[MPSNDArrayRandomUniform initWithDevice:]
+ -[MPSNDArrayRandomUniform initWithDevice:minimum:maximum:]
+ -[MPSNDArrayRandomUniform initWithDevice:minimumInteger:maximumInteger:]
+ -[MPSNDArrayRandomUniform maximumInteger]
+ -[MPSNDArrayRandomUniform maximum]
+ -[MPSNDArrayRandomUniform minimumInteger]
+ -[MPSNDArrayRandomUniform minimum]
+ -[MPSNDArrayRandomUniform setMaximum:]
+ -[MPSNDArrayRandomUniform setMaximumInteger:]
+ -[MPSNDArrayRandomUniform setMinimum:]
+ -[MPSNDArrayRandomUniform setMinimumInteger:]
+ -[MPSNDArrayReciprocal initWithDevice:]
+ -[MPSNDArrayReciprocalGradient initWithDevice:]
+ -[MPSNDArrayReduction axes]
+ -[MPSNDArrayReduction axis]
+ -[MPSNDArrayReduction copyWithZone:device:]
+ -[MPSNDArrayReduction dealloc]
+ -[MPSNDArrayReduction destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayReduction dimensionsNotToBeBroadcast]
+ -[MPSNDArrayReduction dimensionsToBeRetained]
+ -[MPSNDArrayReduction encodeWithCoder:]
+ -[MPSNDArrayReduction initWithCoder:device:]
+ -[MPSNDArrayReduction initWithDevice:axis:operation:]
+ -[MPSNDArrayReduction kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayReduction operation]
+ -[MPSNDArrayReduction setAxes:]
+ -[MPSNDArrayReduction setAxis:]
+ -[MPSNDArrayReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayReductionGradient axis]
+ -[MPSNDArrayReductionGradient copyWithZone:device:]
+ -[MPSNDArrayReductionGradient dimensionsToBeRetained]
+ -[MPSNDArrayReductionGradient encodeWithCoder:]
+ -[MPSNDArrayReductionGradient initWithCoder:device:]
+ -[MPSNDArrayReductionGradient initWithDevice:axis:operation:]
+ -[MPSNDArrayReductionGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayReductionGradient operation]
+ -[MPSNDArrayReductionGradient setAxis:]
+ -[MPSNDArrayReductionSum initWithDevice:axis:]
+ -[MPSNDArrayReductionSumGradient copyWithZone:device:]
+ -[MPSNDArrayReductionSumGradient encodeWithCoder:]
+ -[MPSNDArrayReductionSumGradient initWithCoder:device:]
+ -[MPSNDArrayReductionSumGradient initWithDevice:axis:]
+ -[MPSNDArrayResample copyWithZone:device:]
+ -[MPSNDArrayResample dataFormat]
+ -[MPSNDArrayResample encodeWithCoder:]
+ -[MPSNDArrayResample initWithCoder:device:]
+ -[MPSNDArrayResample initWithDevice:]
+ -[MPSNDArrayResample kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayResample nearestMode]
+ -[MPSNDArrayResample resampleMode]
+ -[MPSNDArrayResample scaleTransform]
+ -[MPSNDArrayResample setDataFormat:]
+ -[MPSNDArrayResample setNearestMode:]
+ -[MPSNDArrayResample setResampleMode:]
+ -[MPSNDArrayResample setScaleTransform:]
+ -[MPSNDArrayResampleGradient copyWithZone:device:]
+ -[MPSNDArrayResampleGradient dataFormat]
+ -[MPSNDArrayResampleGradient encodeWithCoder:]
+ -[MPSNDArrayResampleGradient initWithCoder:device:]
+ -[MPSNDArrayResampleGradient initWithDevice:]
+ -[MPSNDArrayResampleGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayResampleGradient nearestMode]
+ -[MPSNDArrayResampleGradient resampleMode]
+ -[MPSNDArrayResampleGradient scaleTransform]
+ -[MPSNDArrayResampleGradient setDataFormat:]
+ -[MPSNDArrayResampleGradient setNearestMode:]
+ -[MPSNDArrayResampleGradient setResampleMode:]
+ -[MPSNDArrayResampleGradient setScaleTransform:]
+ -[MPSNDArrayReverseSquareRoot initWithDevice:]
+ -[MPSNDArrayReverseSquareRootGradient initWithDevice:]
+ -[MPSNDArrayRint initWithDevice:]
+ -[MPSNDArrayRintGradient initWithDevice:]
+ -[MPSNDArrayRound initWithDevice:]
+ -[MPSNDArrayRoundGradient initWithDevice:]
+ -[MPSNDArrayScaledDotProductAttention alpha]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:sourceCount:]
+ -[MPSNDArrayScaledDotProductAttention kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayScaledDotProductAttention kernelType]
+ -[MPSNDArrayScaledDotProductAttention layout]
+ -[MPSNDArrayScaledDotProductAttention setAlpha:]
+ -[MPSNDArrayScaledDotProductAttention setLayout:]
+ -[MPSNDArrayScaledDotProductAttention workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayScan axis]
+ -[MPSNDArrayScan exclusive]
+ -[MPSNDArrayScan initWithCoder:device:]
+ -[MPSNDArrayScan initWithDevice:]
+ -[MPSNDArrayScan initWithDevice:axis:operation:exclusive:reverse:]
+ -[MPSNDArrayScan initWithDevice:operation:]
+ -[MPSNDArrayScan kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayScan operation]
+ -[MPSNDArrayScan reverse]
+ -[MPSNDArrayScan setAxis:]
+ -[MPSNDArrayScan setExclusive:]
+ -[MPSNDArrayScan setReverse:]
+ -[MPSNDArrayScanGradient axis]
+ -[MPSNDArrayScanGradient exclusive]
+ -[MPSNDArrayScanGradient initWithCoder:device:]
+ -[MPSNDArrayScanGradient initWithDevice:]
+ -[MPSNDArrayScanGradient initWithDevice:axis:operation:exclusive:reverse:]
+ -[MPSNDArrayScanGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayScanGradient operation]
+ -[MPSNDArrayScanGradient reverse]
+ -[MPSNDArrayScanGradient setAxis:]
+ -[MPSNDArrayScanGradient setExclusive:]
+ -[MPSNDArrayScanGradient setReverse:]
+ -[MPSNDArrayScatter batchDimensions]
+ -[MPSNDArrayScatter copyWithZone:device:]
+ -[MPSNDArrayScatter dealloc]
+ -[MPSNDArrayScatter dimensionsNotToBeBroadcast]
+ -[MPSNDArrayScatter encodeToCommandBuffer:primarySourceArray:secondarySourceArray:destinationArray:]
+ -[MPSNDArrayScatter encodeWithCoder:]
+ -[MPSNDArrayScatter initWithCoder:device:]
+ -[MPSNDArrayScatter initWithDevice:operation:]
+ -[MPSNDArrayScatter kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayScatter operation]
+ -[MPSNDArrayScatter setBatchDimensions:]
+ -[MPSNDArrayScatterGradient batchDimensions]
+ -[MPSNDArrayScatterGradient copyWithZone:device:]
+ -[MPSNDArrayScatterGradient dealloc]
+ -[MPSNDArrayScatterGradient dimensionsNotToBeBroadcast]
+ -[MPSNDArrayScatterGradient encodeWithCoder:]
+ -[MPSNDArrayScatterGradient initWithCoder:device:]
+ -[MPSNDArrayScatterGradient initWithDevice:operation:]
+ -[MPSNDArrayScatterGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayScatterGradient operation]
+ -[MPSNDArrayScatterGradient setBatchDimensions:]
+ -[MPSNDArraySelect initWithDevice:]
+ -[MPSNDArraySelectPrimaryGradient initWithDevice:]
+ -[MPSNDArraySelectSecondaryGradient initWithDevice:]
+ -[MPSNDArraySelectTertiaryGradient initWithDevice:]
+ -[MPSNDArraySign initWithDevice:]
+ -[MPSNDArraySignGradient initWithDevice:]
+ -[MPSNDArraySignbit initWithDevice:]
+ -[MPSNDArraySignbitGradient initWithDevice:]
+ -[MPSNDArraySin initWithDevice:]
+ -[MPSNDArraySinGradient initWithDevice:]
+ -[MPSNDArraySinh initWithDevice:]
+ -[MPSNDArraySinhGradient initWithDevice:]
+ -[MPSNDArraySoftMax axis]
+ -[MPSNDArraySoftMax copyWithZone:device:]
+ -[MPSNDArraySoftMax dimensionsToBeRetained]
+ -[MPSNDArraySoftMax encodeWithCoder:]
+ -[MPSNDArraySoftMax initWithCoder:device:]
+ -[MPSNDArraySoftMax initWithDevice:axis:]
+ -[MPSNDArraySoftMax kernelDimensionalityForSourceArrays:]
+ -[MPSNDArraySoftMax reshapeFitToTileToCommandBuffer:currentSource:kernelDimension:dimensionsToBeRetained:]
+ -[MPSNDArraySoftMax setAxis:]
+ -[MPSNDArraySoftMaxGradient axis]
+ -[MPSNDArraySoftMaxGradient copyWithZone:device:]
+ -[MPSNDArraySoftMaxGradient dimensionsToBeRetained]
+ -[MPSNDArraySoftMaxGradient encodeWithCoder:]
+ -[MPSNDArraySoftMaxGradient initWithCoder:device:]
+ -[MPSNDArraySoftMaxGradient initWithDevice:axis:]
+ -[MPSNDArraySoftMaxGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArraySoftMaxGradient setAxis:]
+ -[MPSNDArraySolverLU dealloc]
+ -[MPSNDArraySolverLU initWithDevice:sourceCount:]
+ -[MPSNDArraySolverLU kernelDimensionalityForSourceArrays:]
+ -[MPSNDArraySort axis]
+ -[MPSNDArraySort dealloc]
+ -[MPSNDArraySort descending]
+ -[MPSNDArraySort initWithDevice:]
+ -[MPSNDArraySort initWithDevice:axis:descending:]
+ -[MPSNDArraySort kernelDimensionalityForSourceArrays:]
+ -[MPSNDArraySort setAxis:]
+ -[MPSNDArraySort setDescending:]
+ -[MPSNDArraySquare initWithDevice:]
+ -[MPSNDArraySquareGradient initWithDevice:]
+ -[MPSNDArraySquareRoot initWithDevice:]
+ -[MPSNDArraySquareRootGradient initWithDevice:]
+ -[MPSNDArrayStencilKernel copyWithZone:device:]
+ -[MPSNDArrayStencilKernel debugDescription]
+ -[MPSNDArrayStencilKernel dimensionsNotToBeBroadcast]
+ -[MPSNDArrayStencilKernel dimensionsToBeRetained]
+ -[MPSNDArrayStencilKernel encodeWithCoder:]
+ -[MPSNDArrayStencilKernel initWithCoder:device:]
+ -[MPSNDArrayStencilKernel initWithDevice:]
+ -[MPSNDArrayStencilKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayStencilKernel paddingConstant]
+ -[MPSNDArrayStencilKernel paddingMode]
+ -[MPSNDArrayStencilKernel reductionMode]
+ -[MPSNDArrayStencilKernel setPaddingConstant:]
+ -[MPSNDArrayStencilKernel setPaddingMode:]
+ -[MPSNDArrayStencilKernel setReductionMode:]
+ -[MPSNDArrayStencilKernel setStencilDilationRates:]
+ -[MPSNDArrayStencilKernel setStencilOffsets:]
+ -[MPSNDArrayStencilKernel setStencilStrides:]
+ -[MPSNDArrayStencilKernel stencilDilationRates]
+ -[MPSNDArrayStencilKernel stencilOffsets]
+ -[MPSNDArrayStencilKernel stencilStrides]
+ -[MPSNDArrayStencilKernel supportsGradientForSourceIndex:]
+ -[MPSNDArrayStencilKernel workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayStitchedReduction axes]
+ -[MPSNDArrayStitchedReduction axis]
+ -[MPSNDArrayStitchedReduction dealloc]
+ -[MPSNDArrayStitchedReduction destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayStitchedReduction dimensionsToBeRetained]
+ -[MPSNDArrayStitchedReduction getUserDAGInfo]
+ -[MPSNDArrayStitchedReduction initWithDevice:axis:descriptor:]
+ -[MPSNDArrayStitchedReduction invariantValueFn]
+ -[MPSNDArrayStitchedReduction kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayStitchedReduction mapFn]
+ -[MPSNDArrayStitchedReduction reduceFn]
+ -[MPSNDArrayStitchedReduction setAxes:]
+ -[MPSNDArrayStitchedReduction setAxis:]
+ -[MPSNDArrayStitchedReduction setInvariantValueFn:]
+ -[MPSNDArrayStitchedReduction setMapFn:]
+ -[MPSNDArrayStitchedReduction setReduceFn:]
+ -[MPSNDArrayStitchedReduction setStateSize:]
+ -[MPSNDArrayStitchedReduction setWriteFn:]
+ -[MPSNDArrayStitchedReduction stateSize]
+ -[MPSNDArrayStitchedReduction workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayStitchedReduction writeFn]
+ -[MPSNDArrayStitchedReductionDescriptor dealloc]
+ -[MPSNDArrayStitchedReductionDescriptor initWithStateSize:invariantValueFn:mapFn:reduceFn:writeFn:]
+ -[MPSNDArrayStitchedReductionDescriptor invariantValueFn]
+ -[MPSNDArrayStitchedReductionDescriptor mapFn]
+ -[MPSNDArrayStitchedReductionDescriptor reduceFn]
+ -[MPSNDArrayStitchedReductionDescriptor setInvariantValueFn:]
+ -[MPSNDArrayStitchedReductionDescriptor setMapFn:]
+ -[MPSNDArrayStitchedReductionDescriptor setReduceFn:]
+ -[MPSNDArrayStitchedReductionDescriptor setStateSize:]
+ -[MPSNDArrayStitchedReductionDescriptor setWriteFn:]
+ -[MPSNDArrayStitchedReductionDescriptor stateSize]
+ -[MPSNDArrayStitchedReductionDescriptor writeFn]
+ -[MPSNDArrayStitchedReductionRMSNorm epsilon]
+ -[MPSNDArrayStitchedReductionRMSNorm initWithDevice:axis:epsilon:]
+ -[MPSNDArrayStitchedReductionRMSNorm setEpsilon:]
+ -[MPSNDArrayStitchedReductionSoftmax initWithDevice:axis:]
+ -[MPSNDArrayStridedSlice destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayStridedSlice initWithDevice:]
+ -[MPSNDArrayStridedSlice kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayStridedSlice setStrides:]
+ -[MPSNDArrayStridedSlice stridesAtSourceIndex:]
+ -[MPSNDArrayStridedSlice strides]
+ -[MPSNDArrayStridedSliceGradient dealloc]
+ -[MPSNDArrayStridedSliceGradient destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayStridedSliceGradient encodeToCommandBuffer:sourceArray:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayStridedSliceGradient encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayStridedSliceGradient initWithDevice:]
+ -[MPSNDArrayStridedSliceGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayStridedSliceGradient stridesAtSourceIndex:]
+ -[MPSNDArraySubtraction initWithDevice:]
+ -[MPSNDArraySubtractionPrimaryGradient initWithDevice:]
+ -[MPSNDArraySubtractionSecondaryGradient initWithDevice:]
+ -[MPSNDArrayTan initWithDevice:]
+ -[MPSNDArrayTanGradient initWithDevice:]
+ -[MPSNDArrayTanh initWithDevice:]
+ -[MPSNDArrayTanhGradient initWithDevice:]
+ -[MPSNDArrayTileGradientKernel copyWithZone:device:]
+ -[MPSNDArrayTileGradientKernel dimensionsToBeRetained]
+ -[MPSNDArrayTileGradientKernel encodeWithCoder:]
+ -[MPSNDArrayTileGradientKernel initWithCoder:device:]
+ -[MPSNDArrayTileGradientKernel initWithDevice:]
+ -[MPSNDArrayTileGradientKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayTileGradientKernel multiples]
+ -[MPSNDArrayTileGradientKernel setMultiples:]
+ -[MPSNDArrayTileKernel copyWithZone:device:]
+ -[MPSNDArrayTileKernel destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayTileKernel dimensionsToBeRetained]
+ -[MPSNDArrayTileKernel encodeWithCoder:]
+ -[MPSNDArrayTileKernel initWithCoder:device:]
+ -[MPSNDArrayTileKernel initWithDevice:]
+ -[MPSNDArrayTileKernel kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayTileKernel multiples]
+ -[MPSNDArrayTileKernel setMultiples:]
+ -[MPSNDArrayTopK K]
+ -[MPSNDArrayTopK copyWithZone:device:]
+ -[MPSNDArrayTopK destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayTopK dimensionsNotToBeBroadcast]
+ -[MPSNDArrayTopK encodeWithCoder:]
+ -[MPSNDArrayTopK findIndices]
+ -[MPSNDArrayTopK initWithCoder:device:]
+ -[MPSNDArrayTopK initWithDevice:K:]
+ -[MPSNDArrayTopK initWithDevice:K:findIndices:]
+ -[MPSNDArrayTopK initWithDevice:]
+ -[MPSNDArrayTopK kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayTopK setFindIndices:]
+ -[MPSNDArrayTopK setK:]
+ -[MPSNDArrayTopKGradient K]
+ -[MPSNDArrayTopKGradient copyWithZone:device:]
+ -[MPSNDArrayTopKGradient destinationArrayDescriptorForSourceArrays:sourceState:]
+ -[MPSNDArrayTopKGradient dimensionsNotToBeBroadcast]
+ -[MPSNDArrayTopKGradient encodeWithCoder:]
+ -[MPSNDArrayTopKGradient initWithCoder:device:]
+ -[MPSNDArrayTopKGradient initWithDevice:K:]
+ -[MPSNDArrayTopKGradient initWithDevice:]
+ -[MPSNDArrayTopKGradient kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayTopKGradient setK:]
+ -[MPSNDArrayTopKMultiDestination K]
+ -[MPSNDArrayTopKMultiDestination computeGradient]
+ -[MPSNDArrayTopKMultiDestination copyWithZone:device:]
+ -[MPSNDArrayTopKMultiDestination destinationArrayDescriptorsForSourceArrays:sourceState:]
+ -[MPSNDArrayTopKMultiDestination dimensionsNotToBeBroadcast]
+ -[MPSNDArrayTopKMultiDestination encodeWithCoder:]
+ -[MPSNDArrayTopKMultiDestination initWithCoder:device:]
+ -[MPSNDArrayTopKMultiDestination initWithDevice:K:]
+ -[MPSNDArrayTopKMultiDestination initWithDevice:K:computeGradient:]
+ -[MPSNDArrayTopKMultiDestination initWithDevice:]
+ -[MPSNDArrayTopKMultiDestination kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayTopKMultiDestination setK:]
+ -[MPSNDArrayTopKMultiDestination supportsGradientForSourceIndex:]
+ -[MPSNDArrayUnaryGradientKernel encodeToCommandBuffer:sourceArray:sourceGradient:gradientState:]
+ -[MPSNDArrayUnaryGradientKernel encodeToCommandBuffer:sourceArray:sourceGradient:gradientState:destinationArray:]
+ -[MPSNDArrayUnaryGradientKernel initWithCoder:device:]
+ -[MPSNDArrayUnaryGradientKernel initWithDevice:]
+ -[MPSNDArrayUnaryKernel dilationRates]
+ -[MPSNDArrayUnaryKernel edgeMode]
+ -[MPSNDArrayUnaryKernel encodeToCommandBuffer:sourceArray:]
+ -[MPSNDArrayUnaryKernel encodeToCommandBuffer:sourceArray:destinationArray:]
+ -[MPSNDArrayUnaryKernel encodeToCommandBuffer:sourceArray:resultState:destinationArray:]
+ -[MPSNDArrayUnaryKernel encodeToCommandBuffer:sourceArray:resultState:outputStateIsTemporary:]
+ -[MPSNDArrayUnaryKernel initWithCoder:device:]
+ -[MPSNDArrayUnaryKernel initWithDevice:]
+ -[MPSNDArrayUnaryKernel kernelSizes]
+ -[MPSNDArrayUnaryKernel offsets]
+ -[MPSNDArrayUnaryKernel setDilationRates:]
+ -[MPSNDArrayUnaryKernel setEdgeMode:]
+ -[MPSNDArrayUnaryKernel setKernelSizes:]
+ -[MPSNDArrayUnaryKernel setOffsets:]
+ -[MPSNDArrayUnaryKernel setStrides:]
+ -[MPSNDArrayUnaryKernel strides]
+ -[MPSNDArrayVectorLUTDequantize copyWithZone:device:]
+ -[MPSNDArrayVectorLUTDequantize encodeWithCoder:]
+ -[MPSNDArrayVectorLUTDequantize initWithCoder:device:]
+ -[MPSNDArrayVectorLUTDequantize initWithDevice:axis:]
+ -[MPSNDArrayVectorLUTDequantize kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayVectorLUTDequantize setVectorAxis:]
+ -[MPSNDArrayVectorLUTDequantize vectorAxis]
+ -[MPSNDArrayVectorLUTDequantize workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayXNOR initWithDevice:]
+ -[MPSNDArrayXNORPrimaryGradient initWithDevice:]
+ -[MPSNDArrayXNORSecondaryGradient initWithDevice:]
+ -[MPSNDArrayXOR initWithDevice:]
+ -[MPSNDArrayXORPrimaryGradient initWithDevice:]
+ -[MPSNDArrayXORSecondaryGradient initWithDevice:]
+ -[MPSPluginNDArrayConvolutionDescriptor channelMultiplier]
+ -[MPSPluginNDArrayConvolutionDescriptor dataFormat]
+ -[MPSPluginNDArrayConvolutionDescriptor dilationRates]
+ -[MPSPluginNDArrayConvolutionDescriptor groups]
+ -[MPSPluginNDArrayConvolutionDescriptor initWithKernelSizes:inputFeatureChannels:outputFeatureChannels:strides:dilationRates:groups:channelMultiplier:subPixelScaleFactor:dataFormat:weightsFormat:]
+ -[MPSPluginNDArrayConvolutionDescriptor inputFeatureChannels]
+ -[MPSPluginNDArrayConvolutionDescriptor kernelSizes]
+ -[MPSPluginNDArrayConvolutionDescriptor outputFeatureChannels]
+ -[MPSPluginNDArrayConvolutionDescriptor strides]
+ -[MPSPluginNDArrayConvolutionDescriptor subPixelScaleFactor]
+ -[MPSPluginNDArrayConvolutionDescriptor weightsFormat]
+ <redacted>
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table11
+ GCC_except_table118
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table139
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table5
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table7
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table9
+ GCC_except_table98
+ GCC_except_table99
+ OBJC_IVAR_$_MPSNDArrayConvolution2D._allowFP16WinogradTransformIntermediate
+ _MPSNDArrayVersionNumber
+ _MPSNDArrayVersionString
+ _OBJC_IVAR_$_MPSNDArrayASTCQuantizationDescriptor._hasMinValue
+ _OBJC_IVAR_$_MPSNDArrayAffineInt4Dequantize._quantizationDescriptor
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._dataFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._dataQuantizationDescriptor
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._dilationRateInX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._dilationRateInY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._inputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._kernelHeight
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._kernelWidth
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._ndArrayIdentity
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._offsets
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._outputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._plugin
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._quantizationNDArrays
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._strideInPixelsX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._strideInPixelsY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._weightsFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution2D._weightsQuantizationDescriptor
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._channelMultiplier
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._dataFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._dilationRateInX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._dilationRateInY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._inputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._kernelHeight
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._kernelWidth
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._outputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._strideInPixelsX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._strideInPixelsY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DDescriptor._weightsFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithInput._ndArrayIdentity
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithInput._plugin
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._dataFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._dilationRateInX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._dilationRateInY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._inputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._kernelHeight
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._kernelWidth
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._offsets
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._outputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._plugin
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._strideInPixelsX
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._strideInPixelsY
+ _OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithWeights._weightsFormat
+ _OBJC_IVAR_$_MPSNDArrayConvolution3D._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution3DGradientWithInput._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution3DGradientWithInput._kernelOffsets
+ _OBJC_IVAR_$_MPSNDArrayConvolution3DGradientWithWeights._groups
+ _OBJC_IVAR_$_MPSNDArrayConvolution3DGradientWithWeights._kernelOffsets
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._alignCorners
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._constantValue
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._coordinate1DInWidth
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._dataFormat
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._nearestMode
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._normalizeCoordinates
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._paddingMode
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._relativeCoordinates
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._samplingMode
+ _OBJC_IVAR_$_MPSNDArrayCostVolumeDescriptor._windowSizes
+ _OBJC_IVAR_$_MPSNDArrayDepthwiseConvolutionKernel._paddingConstant
+ _OBJC_IVAR_$_MPSNDArrayGather._axis
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._dataLayout
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._dilationRateInX
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._dilationRateInY
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._kernelHeight
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._kernelWidth
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._paddingBottom
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._paddingLeft
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._paddingRight
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._paddingTop
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._strideInPixelsX
+ _OBJC_IVAR_$_MPSNDArrayIm2colDescriptor._strideInPixelsY
+ _OBJC_IVAR_$_MPSNDArrayLUTQuantizationDescriptor._vectorAxes
+ _OBJC_IVAR_$_MPSNDArrayLogSoftMax._axis
+ _OBJC_IVAR_$_MPSNDArrayLogSoftMaxGradient._axis
+ _OBJC_IVAR_$_MPSNDArrayMaterializeSparseTensor._sparseFormat
+ _OBJC_IVAR_$_MPSNDArrayMathBinaryKernel._opType
+ _OBJC_IVAR_$_MPSNDArrayMathBinaryPrimaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathBinarySecondaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathTernaryKernel._opType
+ _OBJC_IVAR_$_MPSNDArrayMathTernaryPrimaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathTernarySecondaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathTernaryTertiaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathUnaryGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayMathUnaryKernel._opType
+ _OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._leftQuantizationDescriptor
+ _OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._rightQuantizationDescriptor
+ _OBJC_IVAR_$_MPSNDArrayMultiaryBase._destinationArrayAllocator
+ _OBJC_IVAR_$_MPSNDArrayMultiaryBase._encodeData
+ _OBJC_IVAR_$_MPSNDArrayMultiaryBase._encodeGradient
+ _OBJC_IVAR_$_MPSNDArrayMultiaryBase._srcCount
+ _OBJC_IVAR_$_MPSNDArrayMultiaryGradientKernel._sourceGradientIndex
+ _OBJC_IVAR_$_MPSNDArrayMultiaryKernel._encode
+ _OBJC_IVAR_$_MPSNDArrayMultiaryMultiDestinationBase._encodeData
+ _OBJC_IVAR_$_MPSNDArrayMultiaryMultiDestinationKernel._encode
+ _OBJC_IVAR_$_MPSNDArrayNeuronGradient._opType
+ _OBJC_IVAR_$_MPSNDArrayNeuronKernel._opType
+ _OBJC_IVAR_$_MPSNDArrayNormFusionDescriptor._epsilon
+ _OBJC_IVAR_$_MPSNDArrayNormFusionDescriptor._hasScale
+ _OBJC_IVAR_$_MPSNDArrayNormFusionDescriptor._isLeftFused
+ _OBJC_IVAR_$_MPSNDArrayNormFusionDescriptor._normFusionType
+ _OBJC_IVAR_$_MPSNDArrayOffsetIdentity._hasDestinationOffset
+ _OBJC_IVAR_$_MPSNDArrayPrune._pruneMetric
+ _OBJC_IVAR_$_MPSNDArrayPrune._pruneStructure
+ _OBJC_IVAR_$_MPSNDArrayPrune._sparsity
+ _OBJC_IVAR_$_MPSNDArrayQuantizationDescriptor._quantizationDataType
+ _OBJC_IVAR_$_MPSNDArrayQuantizationDescriptor._quantizationScheme
+ _OBJC_IVAR_$_MPSNDArrayQuantizedGatherND._quant_desc
+ _OBJC_IVAR_$_MPSNDArrayQuantizedMatrixMultiplication._lutGEMVKernel
+ _OBJC_IVAR_$_MPSNDArrayRandomStateDescriptor._algorithm
+ _OBJC_IVAR_$_MPSNDArrayRandomStateDescriptor._state
+ _OBJC_IVAR_$_MPSNDArraySoftMax._axis
+ _OBJC_IVAR_$_MPSNDArraySoftMaxGradient._axis
+ _OBJC_IVAR_$_MPSNDArraySolverLU._mslu
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionDescriptor._invariantValueFn
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionDescriptor._mapFn
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionDescriptor._reduceFn
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionDescriptor._stateSize
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionDescriptor._writeFn
+ _OBJC_IVAR_$_MPSNDArrayStitchedReductionRMSNorm._epsilon
+ _OBJC_IVAR_$_MPSNDArrayStridedSlice._strides
+ _OBJC_IVAR_$_MPSNDArrayStridedSliceGradient._zeroFillKernel
+ _OBJC_IVAR_$_MPSNDArrayTileGradientKernel._multiples
+ _OBJC_IVAR_$_MPSNDArrayTileKernel._multiples
+ _OBJC_IVAR_$_MPSNDArrayUnaryKernel._dilationRates
+ _OBJC_IVAR_$_MPSNDArrayUnaryKernel._edgeMode
+ _OBJC_IVAR_$_MPSNDArrayUnaryKernel._kernelSizes
+ _OBJC_IVAR_$_MPSNDArrayUnaryKernel._offsets
+ _OBJC_IVAR_$_MPSNDArrayUnaryKernel._strides
+ _OBJC_IVAR_$_MPSNDArrayVectorLUTDequantize._vectorAxis
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._channelMultiplier
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._dataFormat
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._dilationRates
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._groups
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._inputFeatureChannels
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._kernelSizes
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._outputFeatureChannels
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._strides
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._subPixelScaleFactor
+ _OBJC_IVAR_$_MPSPluginNDArrayConvolutionDescriptor._weightsFormat
+ __MergedGlobals
+ __MergedGlobals.11
+ __MergedGlobals.17
+ __MergedGlobals.3
+ __MergedGlobals.30
+ __MergedGlobals.7
+ __MergedGlobals.9
+ __OBJC_$_CLASS_METHODS_MPSNDArrayACos
+ __OBJC_$_CLASS_METHODS_MPSNDArrayACosGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayACosh
+ __OBJC_$_CLASS_METHODS_MPSNDArrayACoshGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAND
+ __OBJC_$_CLASS_METHODS_MPSNDArrayANDPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayANDSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayASin
+ __OBJC_$_CLASS_METHODS_MPSNDArrayASinGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayASinh
+ __OBJC_$_CLASS_METHODS_MPSNDArrayASinhGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATan
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATan2
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATan2PrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATan2SecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATanGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATanh
+ __OBJC_$_CLASS_METHODS_MPSNDArrayATanhGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAbsolute
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAbsoluteGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAddition
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAdditionPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAdditionSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayAffineInt4Dequantize
+ __OBJC_$_CLASS_METHODS_MPSNDArrayBandPart
+ __OBJC_$_CLASS_METHODS_MPSNDArrayBinaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayBinaryPrimaryGradientKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayBinarySecondaryGradientKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCeil
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCeilGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayClamp
+ __OBJC_$_CLASS_METHODS_MPSNDArrayClampPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayClampSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayClampTertiaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCol2imKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution2D
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution3D
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_$_CLASS_METHODS_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCos
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCosGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCosh
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCoshGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCostVolume
+ __OBJC_$_CLASS_METHODS_MPSNDArrayCropResize
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDecompositionLU
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDecompositionQR
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDivision
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDivisionPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDivisionSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayEqual
+ __OBJC_$_CLASS_METHODS_MPSNDArrayEqualPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayEqualSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayErf
+ __OBJC_$_CLASS_METHODS_MPSNDArrayErfGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponent
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponentBase10
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponentBase10Gradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponentBase2
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponentBase2Gradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayExponentGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayFloor
+ __OBJC_$_CLASS_METHODS_MPSNDArrayFloorGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayFourierTransform
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGather
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGatherGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGatherND
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGatherNDGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThan
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThanOrEqualTo
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThanOrEqualToPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThanOrEqualToSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThanPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGreaterThanSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGridSample
+ __OBJC_$_CLASS_METHODS_MPSNDArrayHammingDistanceKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIdentity
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIm2colKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayInitialization
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsFinite
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsFiniteGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsInfinite
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsInfiniteGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsNaN
+ __OBJC_$_CLASS_METHODS_MPSNDArrayIsNaNGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLUTDequantize
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLUTGEMV
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThan
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThanOrEqualTo
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThanOrEqualToPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThanOrEqualToSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThanPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLessThanSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLocalConvolution
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogSoftMax
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogSoftMaxGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithm
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithmBase10
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithmBase10Gradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithmBase2
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithmBase2Gradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLogarithmGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMaterializeSparseTensor
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathBinaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathBinaryPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathBinarySecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathTernaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathTernaryPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathTernarySecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathTernaryTertiaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathUnaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMathUnaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMatrixMultiplication
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMaximum
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMaximumPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMaximumSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMinimum
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMinimumPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMinimumSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayModulo
+ __OBJC_$_CLASS_METHODS_MPSNDArrayModuloPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayModuloSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMultiaryBase
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMultiaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMultiplication
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMultiplicationPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayMultiplicationSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNAND
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNANDPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNANDSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNMS
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNOR
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNORPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNORSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNOT
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNOTGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNegative
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNegativeGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNeuronGeLU
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNeuronGeLUGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNeuronGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNeuronKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNotEqual
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNotEqualPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayNotEqualSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayOR
+ __OBJC_$_CLASS_METHODS_MPSNDArrayORPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayORSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayOffsetIdentity
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPadGradientKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPadKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPoolingKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPower
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPowerPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPowerSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayPrune
+ __OBJC_$_CLASS_METHODS_MPSNDArrayQuantizedConvolution
+ __OBJC_$_CLASS_METHODS_MPSNDArrayQuantizedGatherND
+ __OBJC_$_CLASS_METHODS_MPSNDArrayQuantizedMatrixMultiplication
+ __OBJC_$_CLASS_METHODS_MPSNDArrayQuantizedScaledDotProductAttention
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRandom
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRandomState
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRandomStateDescriptor
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReciprocal
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReciprocalGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReduction
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReductionGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayResample
+ __OBJC_$_CLASS_METHODS_MPSNDArrayResampleGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReverseSquareRoot
+ __OBJC_$_CLASS_METHODS_MPSNDArrayReverseSquareRootGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRint
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRintGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRound
+ __OBJC_$_CLASS_METHODS_MPSNDArrayRoundGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayScaledDotProductAttention
+ __OBJC_$_CLASS_METHODS_MPSNDArrayScan
+ __OBJC_$_CLASS_METHODS_MPSNDArrayScanGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayScatter
+ __OBJC_$_CLASS_METHODS_MPSNDArrayScatterGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySelect
+ __OBJC_$_CLASS_METHODS_MPSNDArraySelectPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySelectSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySelectTertiaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySign
+ __OBJC_$_CLASS_METHODS_MPSNDArraySignGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySignbit
+ __OBJC_$_CLASS_METHODS_MPSNDArraySignbitGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySin
+ __OBJC_$_CLASS_METHODS_MPSNDArraySinGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySinh
+ __OBJC_$_CLASS_METHODS_MPSNDArraySinhGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySoftMax
+ __OBJC_$_CLASS_METHODS_MPSNDArraySoftMaxGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySolverLU
+ __OBJC_$_CLASS_METHODS_MPSNDArraySort
+ __OBJC_$_CLASS_METHODS_MPSNDArraySquare
+ __OBJC_$_CLASS_METHODS_MPSNDArraySquareGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySquareRoot
+ __OBJC_$_CLASS_METHODS_MPSNDArraySquareRootGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayStencilKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayStitchedReduction
+ __OBJC_$_CLASS_METHODS_MPSNDArrayStridedSlice
+ __OBJC_$_CLASS_METHODS_MPSNDArrayStridedSliceGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySubtraction
+ __OBJC_$_CLASS_METHODS_MPSNDArraySubtractionPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArraySubtractionSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTan
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTanGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTanh
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTanhGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTileGradientKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTileKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTopK
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTopKGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayTopKMultiDestination
+ __OBJC_$_CLASS_METHODS_MPSNDArrayUnaryGradientKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayUnaryKernel
+ __OBJC_$_CLASS_METHODS_MPSNDArrayVectorLUTDequantize
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXNOR
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXNORPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXNORSecondaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXOR
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXORPrimaryGradient
+ __OBJC_$_CLASS_METHODS_MPSNDArrayXORSecondaryGradient
+ __OBJC_$_CLASS_PROP_LIST_MPSNDArrayRandomStateDescriptor
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayACos
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayACosGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayACosh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayACoshGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAND
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayANDPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayANDSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayASTCQuantizationDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayASin
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayASinGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayASinh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayASinhGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATan
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATan2
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATan2PrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATan2SecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATanGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATanh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayATanhGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAbsolute
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAbsoluteGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAddition
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAdditionPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAdditionSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAffineInt4Dequantize
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAffineQuantizationDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayArgSort
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayBandPart
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayBinaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayBinaryPrimaryGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayBinarySecondaryGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCeil
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCeilGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayClamp
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayClampPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayClampSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayClampTertiaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCol2imKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution2D
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution2DDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution3D
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCos
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCosGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCosh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCoshGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCostVolume
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCostVolumeDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayCropResize
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDecompositionLU
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDecompositionQR
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDepthwiseConvolution2DDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDivision
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDivisionPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDivisionSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayEqual
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayEqualPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayEqualSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayErf
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayErfGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponent
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponentBase10
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponentBase10Gradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponentBase2
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponentBase2Gradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayExponentGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayFloor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayFloorGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayFourierTransform
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGather
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGatherGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGatherGradientState
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGatherND
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGatherNDGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGradientState
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThan
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThanOrEqualTo
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThanOrEqualToPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThanOrEqualToSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThanPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGreaterThanSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGridSample
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayHammingDistanceKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIdentity
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIm2colDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIm2colKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitialization
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationConstant
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationGlorotNormal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationGlorotUniform
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationIdentity
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationRandomNormal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationRandomUniform
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayInitializationTruncatedNormal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsFinite
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsFiniteGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsInfinite
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsInfiniteGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsNaN
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayIsNaNGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLUTDequantize
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLUTGEMV
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLUTQuantizationDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThan
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThanOrEqualTo
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThanOrEqualToPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThanOrEqualToSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThanPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLessThanSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLocalConvolution
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogSoftMax
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogSoftMaxGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithm
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithmBase10
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithmBase10Gradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithmBase2
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithmBase2Gradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLogarithmGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMaterializeSparseTensor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathBinaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathBinaryPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathBinarySecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathTernaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathTernaryPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathTernarySecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathTernaryTertiaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathUnaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMathUnaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMatrixMultiplication
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMaximum
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMaximumPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMaximumSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMinimum
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMinimumPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMinimumSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayModulo
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayModuloPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayModuloSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiaryBase
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiaryGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiaryMultiDestinationBase
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiaryMultiDestinationKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiplication
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiplicationPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayMultiplicationSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNAND
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNANDPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNANDSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNMS
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNOR
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNORPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNORSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNOT
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNOTGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNegative
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNegativeGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNeuronGeLU
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNeuronGeLUGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNeuronGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNeuronKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNormFusionDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNotEqual
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNotEqualPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayNotEqualSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayOR
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayORPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayORSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayOffsetIdentity
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPadGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPadKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPoolingKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPower
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPowerPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPowerSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayPrune
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizationDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizedConvolution
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizedGatherND
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizedMatrixMultiplication
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizedScaledDotProductAttention
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandom
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandomNormal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandomState
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandomStateDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandomTruncatedNormal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRandomUniform
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReciprocal
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReciprocalGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReduction
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReductionGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReductionSum
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReductionSumGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayResample
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayResampleGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReverseSquareRoot
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayReverseSquareRootGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRint
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRintGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRound
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayRoundGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayScaledDotProductAttention
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayScan
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayScanGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayScatter
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayScatterGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySelect
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySelectPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySelectSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySelectTertiaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySign
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySignGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySignbit
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySignbitGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySin
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySinGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySinh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySinhGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySoftMax
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySoftMaxGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySolverLU
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySort
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySquare
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySquareGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySquareRoot
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySquareRootGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStencilKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStitchedReduction
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStitchedReductionDescriptor
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStitchedReductionRMSNorm
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStitchedReductionSoftmax
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStridedSlice
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayStridedSliceGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySubtraction
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySubtractionPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArraySubtractionSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTan
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTanGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTanh
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTanhGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTileGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTileKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTopK
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTopKGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayTopKMultiDestination
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayUnaryGradientKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayUnaryKernel
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayVectorLUTDequantize
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXNOR
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXNORPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXNORSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXOR
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXORPrimaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayXORSecondaryGradient
+ __OBJC_$_INSTANCE_METHODS_MPSPluginNDArrayConvolutionDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayASTCQuantizationDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayAffineInt4Dequantize
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayAffineQuantizationDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayBandPart
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayCol2imKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution2D
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution2DDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution3D
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayCostVolume
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayCostVolumeDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayCropResize
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayDecompositionLU
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayDecompositionQR
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayFourierTransform
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGather
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGatherGradientState
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGatherND
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGatherNDGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGradientState
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGridSample
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayIdentity
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayIm2colDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayIm2colKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitialization
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitializationGlorotNormal
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitializationGlorotUniform
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitializationRandomNormal
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitializationRandomUniform
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayInitializationTruncatedNormal
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLUTGEMV
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLUTQuantizationDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLocalConvolution
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLogSoftMax
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLogSoftMaxGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMaterializeSparseTensor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathBinaryKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathBinaryPrimaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathBinarySecondaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathTernaryKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathTernaryPrimaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathTernarySecondaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathTernaryTertiaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathUnaryGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMathUnaryKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMatrixMultiplication
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMultiaryBase
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMultiaryGradientKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMultiaryKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMultiaryMultiDestinationBase
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayMultiaryMultiDestinationKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayNMS
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayNeuronGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayNeuronKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayNormFusionDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayOffsetIdentity
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayPadGradientKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayPadKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayPoolingKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayPrune
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayQuantizationDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayQuantizedGatherND
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayQuantizedMatrixMultiplication
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayQuantizedScaledDotProductAttention
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayRandomNormal
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayRandomState
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayRandomStateDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayRandomTruncatedNormal
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayRandomUniform
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayReduction
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayReductionGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayResample
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayResampleGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayScaledDotProductAttention
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayScan
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayScanGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayScatter
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayScatterGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArraySoftMax
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArraySoftMaxGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArraySolverLU
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArraySort
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStencilKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStitchedReduction
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStitchedReductionDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStitchedReductionRMSNorm
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStridedSlice
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayStridedSliceGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayTileGradientKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayTileKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayTopK
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayTopKGradient
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayTopKMultiDestination
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayUnaryKernel
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayVectorLUTDequantize
+ __OBJC_$_INSTANCE_VARIABLES_MPSPluginNDArrayConvolutionDescriptor
+ __OBJC_$_PROP_LIST_MPSAutoTuneKernel
+ __OBJC_$_PROP_LIST_MPSExternalNDArrayBinary
+ __OBJC_$_PROP_LIST_MPSExternalNDArrayBinaryGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayASTCQuantizationDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayAffineQuantizationDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayBandPart
+ __OBJC_$_PROP_LIST_MPSNDArrayBinaryKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayCol2imKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution2D
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution2DDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution3D
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_$_PROP_LIST_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_$_PROP_LIST_MPSNDArrayCostVolume
+ __OBJC_$_PROP_LIST_MPSNDArrayCostVolumeDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayCropResize
+ __OBJC_$_PROP_LIST_MPSNDArrayDecompositionQR
+ __OBJC_$_PROP_LIST_MPSNDArrayDepthwiseConvolution2DDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayFourierTransform
+ __OBJC_$_PROP_LIST_MPSNDArrayGather
+ __OBJC_$_PROP_LIST_MPSNDArrayGatherND
+ __OBJC_$_PROP_LIST_MPSNDArrayGatherNDGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayGridSample
+ __OBJC_$_PROP_LIST_MPSNDArrayIm2colDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayIm2colKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationConstant
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationGlorotNormal
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationGlorotUniform
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationRandomNormal
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationRandomUniform
+ __OBJC_$_PROP_LIST_MPSNDArrayInitializationTruncatedNormal
+ __OBJC_$_PROP_LIST_MPSNDArrayLUTGEMV
+ __OBJC_$_PROP_LIST_MPSNDArrayLUTQuantizationDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayLocalConvolution
+ __OBJC_$_PROP_LIST_MPSNDArrayLogSoftMax
+ __OBJC_$_PROP_LIST_MPSNDArrayLogSoftMaxGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayMaterializeSparseTensor
+ __OBJC_$_PROP_LIST_MPSNDArrayMatrixMultiplication
+ __OBJC_$_PROP_LIST_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_$_PROP_LIST_MPSNDArrayMultiaryBase
+ __OBJC_$_PROP_LIST_MPSNDArrayNMS
+ __OBJC_$_PROP_LIST_MPSNDArrayNormFusionDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayOffsetIdentity
+ __OBJC_$_PROP_LIST_MPSNDArrayPadGradientKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayPadKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayPoolingKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayPrune
+ __OBJC_$_PROP_LIST_MPSNDArrayQuantizationDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayRandomNormal
+ __OBJC_$_PROP_LIST_MPSNDArrayRandomState
+ __OBJC_$_PROP_LIST_MPSNDArrayRandomStateDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayRandomTruncatedNormal
+ __OBJC_$_PROP_LIST_MPSNDArrayRandomUniform
+ __OBJC_$_PROP_LIST_MPSNDArrayReduction
+ __OBJC_$_PROP_LIST_MPSNDArrayReductionGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayResample
+ __OBJC_$_PROP_LIST_MPSNDArrayResampleGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayScaledDotProductAttention
+ __OBJC_$_PROP_LIST_MPSNDArrayScan
+ __OBJC_$_PROP_LIST_MPSNDArrayScanGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayScatter
+ __OBJC_$_PROP_LIST_MPSNDArrayScatterGradient
+ __OBJC_$_PROP_LIST_MPSNDArraySoftMax
+ __OBJC_$_PROP_LIST_MPSNDArraySoftMaxGradient
+ __OBJC_$_PROP_LIST_MPSNDArraySort
+ __OBJC_$_PROP_LIST_MPSNDArrayStencilKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayStitchedReduction
+ __OBJC_$_PROP_LIST_MPSNDArrayStitchedReductionDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayStitchedReductionRMSNorm
+ __OBJC_$_PROP_LIST_MPSNDArrayStridedSlice
+ __OBJC_$_PROP_LIST_MPSNDArrayTileGradientKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayTileKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayTopK
+ __OBJC_$_PROP_LIST_MPSNDArrayTopKGradient
+ __OBJC_$_PROP_LIST_MPSNDArrayTopKMultiDestination
+ __OBJC_$_PROP_LIST_MPSNDArrayUnaryKernel
+ __OBJC_$_PROP_LIST_MPSNDArrayVectorLUTDequantize
+ __OBJC_$_PROP_LIST_MPSPluginNDArrayConvolutionDescriptor
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MPSAutoTuneKernel
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MPSExternalPluginBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MPSNDArrayAllocator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MPSExternalNDArrayBinary
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MPSExternalNDArrayBinaryGradient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPSAutoTuneKernel
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPSExternalNDArrayBinary
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPSExternalNDArrayBinaryGradient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPSExternalPluginBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPSNDArrayAllocator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_MPSExternalNDArrayBinary
+ __OBJC_$_PROTOCOL_REFS_MPSExternalNDArrayBinaryGradient
+ __OBJC_$_PROTOCOL_REFS_MPSExternalPluginBase
+ __OBJC_$_PROTOCOL_REFS_MPSNDArrayAllocator
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_MPSExternalNDArrayBinary
+ __OBJC_CLASS_PROTOCOLS_$_MPSExternalNDArrayBinaryGradient
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayConvolution2D
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayConvolution2DDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayCostVolumeDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayIm2colDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayNormFusionDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayQuantizationDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayRandomStateDescriptor
+ __OBJC_CLASS_RO_$_MPSExternalNDArrayBinary
+ __OBJC_CLASS_RO_$_MPSExternalNDArrayBinaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayACos
+ __OBJC_CLASS_RO_$_MPSNDArrayACosGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayACosh
+ __OBJC_CLASS_RO_$_MPSNDArrayACoshGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayAND
+ __OBJC_CLASS_RO_$_MPSNDArrayANDPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayANDSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayASTCQuantizationDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayASin
+ __OBJC_CLASS_RO_$_MPSNDArrayASinGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayASinh
+ __OBJC_CLASS_RO_$_MPSNDArrayASinhGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayATan
+ __OBJC_CLASS_RO_$_MPSNDArrayATan2
+ __OBJC_CLASS_RO_$_MPSNDArrayATan2PrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayATan2SecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayATanGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayATanh
+ __OBJC_CLASS_RO_$_MPSNDArrayATanhGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayAbsolute
+ __OBJC_CLASS_RO_$_MPSNDArrayAbsoluteGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayAddition
+ __OBJC_CLASS_RO_$_MPSNDArrayAdditionPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayAdditionSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayAffineInt4Dequantize
+ __OBJC_CLASS_RO_$_MPSNDArrayAffineQuantizationDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayArgSort
+ __OBJC_CLASS_RO_$_MPSNDArrayBandPart
+ __OBJC_CLASS_RO_$_MPSNDArrayBinaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayBinaryPrimaryGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayBinarySecondaryGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayCeil
+ __OBJC_CLASS_RO_$_MPSNDArrayCeilGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayClamp
+ __OBJC_CLASS_RO_$_MPSNDArrayClampPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayClampSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayClampTertiaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayCol2imKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution2D
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution2DDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution3D
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_CLASS_RO_$_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_CLASS_RO_$_MPSNDArrayCos
+ __OBJC_CLASS_RO_$_MPSNDArrayCosGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayCosh
+ __OBJC_CLASS_RO_$_MPSNDArrayCoshGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayCostVolume
+ __OBJC_CLASS_RO_$_MPSNDArrayCostVolumeDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayCropResize
+ __OBJC_CLASS_RO_$_MPSNDArrayDecompositionLU
+ __OBJC_CLASS_RO_$_MPSNDArrayDecompositionQR
+ __OBJC_CLASS_RO_$_MPSNDArrayDepthwiseConvolution2DDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayDivision
+ __OBJC_CLASS_RO_$_MPSNDArrayDivisionPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayDivisionSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayEqual
+ __OBJC_CLASS_RO_$_MPSNDArrayEqualPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayEqualSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayErf
+ __OBJC_CLASS_RO_$_MPSNDArrayErfGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayExponent
+ __OBJC_CLASS_RO_$_MPSNDArrayExponentBase10
+ __OBJC_CLASS_RO_$_MPSNDArrayExponentBase10Gradient
+ __OBJC_CLASS_RO_$_MPSNDArrayExponentBase2
+ __OBJC_CLASS_RO_$_MPSNDArrayExponentBase2Gradient
+ __OBJC_CLASS_RO_$_MPSNDArrayExponentGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayFloor
+ __OBJC_CLASS_RO_$_MPSNDArrayFloorGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayFourierTransform
+ __OBJC_CLASS_RO_$_MPSNDArrayGather
+ __OBJC_CLASS_RO_$_MPSNDArrayGatherGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGatherGradientState
+ __OBJC_CLASS_RO_$_MPSNDArrayGatherND
+ __OBJC_CLASS_RO_$_MPSNDArrayGatherNDGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGradientState
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThan
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThanOrEqualTo
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThanOrEqualToPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThanOrEqualToSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThanPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGreaterThanSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayGridSample
+ __OBJC_CLASS_RO_$_MPSNDArrayHammingDistanceKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayIdentity
+ __OBJC_CLASS_RO_$_MPSNDArrayIm2colDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayIm2colKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayInitialization
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationConstant
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationGlorotNormal
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationGlorotUniform
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationIdentity
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationRandomNormal
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationRandomUniform
+ __OBJC_CLASS_RO_$_MPSNDArrayInitializationTruncatedNormal
+ __OBJC_CLASS_RO_$_MPSNDArrayIsFinite
+ __OBJC_CLASS_RO_$_MPSNDArrayIsFiniteGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayIsInfinite
+ __OBJC_CLASS_RO_$_MPSNDArrayIsInfiniteGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayIsNaN
+ __OBJC_CLASS_RO_$_MPSNDArrayIsNaNGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLUTDequantize
+ __OBJC_CLASS_RO_$_MPSNDArrayLUTGEMV
+ __OBJC_CLASS_RO_$_MPSNDArrayLUTQuantizationDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThan
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThanOrEqualTo
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThanOrEqualToPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThanOrEqualToSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThanPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLessThanSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLocalConvolution
+ __OBJC_CLASS_RO_$_MPSNDArrayLogSoftMax
+ __OBJC_CLASS_RO_$_MPSNDArrayLogSoftMaxGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithm
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithmBase10
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithmBase10Gradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithmBase2
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithmBase2Gradient
+ __OBJC_CLASS_RO_$_MPSNDArrayLogarithmGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMaterializeSparseTensor
+ __OBJC_CLASS_RO_$_MPSNDArrayMathBinaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMathBinaryPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathBinarySecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathTernaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMathTernaryPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathTernarySecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathTernaryTertiaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathUnaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMathUnaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMatrixMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_CLASS_RO_$_MPSNDArrayMaximum
+ __OBJC_CLASS_RO_$_MPSNDArrayMaximumPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMaximumSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMinimum
+ __OBJC_CLASS_RO_$_MPSNDArrayMinimumPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMinimumSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayModulo
+ __OBJC_CLASS_RO_$_MPSNDArrayModuloPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayModuloSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiaryBase
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiaryGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiaryMultiDestinationBase
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiaryMultiDestinationKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiplicationPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayMultiplicationSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNAND
+ __OBJC_CLASS_RO_$_MPSNDArrayNANDPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNANDSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNMS
+ __OBJC_CLASS_RO_$_MPSNDArrayNOR
+ __OBJC_CLASS_RO_$_MPSNDArrayNORPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNORSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNOT
+ __OBJC_CLASS_RO_$_MPSNDArrayNOTGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNegative
+ __OBJC_CLASS_RO_$_MPSNDArrayNegativeGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNeuronGeLU
+ __OBJC_CLASS_RO_$_MPSNDArrayNeuronGeLUGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNeuronGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNeuronKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayNormFusionDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayNotEqual
+ __OBJC_CLASS_RO_$_MPSNDArrayNotEqualPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayNotEqualSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayOR
+ __OBJC_CLASS_RO_$_MPSNDArrayORPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayORSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayOffsetIdentity
+ __OBJC_CLASS_RO_$_MPSNDArrayPadGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayPadKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayPoolingKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayPower
+ __OBJC_CLASS_RO_$_MPSNDArrayPowerPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayPowerSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayPrune
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizationDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizedConvolution
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizedGatherND
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizedMatrixMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizedScaledDotProductAttention
+ __OBJC_CLASS_RO_$_MPSNDArrayRandom
+ __OBJC_CLASS_RO_$_MPSNDArrayRandomNormal
+ __OBJC_CLASS_RO_$_MPSNDArrayRandomState
+ __OBJC_CLASS_RO_$_MPSNDArrayRandomStateDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayRandomTruncatedNormal
+ __OBJC_CLASS_RO_$_MPSNDArrayRandomUniform
+ __OBJC_CLASS_RO_$_MPSNDArrayReciprocal
+ __OBJC_CLASS_RO_$_MPSNDArrayReciprocalGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayReduction
+ __OBJC_CLASS_RO_$_MPSNDArrayReductionGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayReductionSum
+ __OBJC_CLASS_RO_$_MPSNDArrayReductionSumGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayResample
+ __OBJC_CLASS_RO_$_MPSNDArrayResampleGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayReverseSquareRoot
+ __OBJC_CLASS_RO_$_MPSNDArrayReverseSquareRootGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayRint
+ __OBJC_CLASS_RO_$_MPSNDArrayRintGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayRound
+ __OBJC_CLASS_RO_$_MPSNDArrayRoundGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayScaledDotProductAttention
+ __OBJC_CLASS_RO_$_MPSNDArrayScan
+ __OBJC_CLASS_RO_$_MPSNDArrayScanGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayScatter
+ __OBJC_CLASS_RO_$_MPSNDArrayScatterGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySelect
+ __OBJC_CLASS_RO_$_MPSNDArraySelectPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySelectSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySelectTertiaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySign
+ __OBJC_CLASS_RO_$_MPSNDArraySignGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySignbit
+ __OBJC_CLASS_RO_$_MPSNDArraySignbitGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySin
+ __OBJC_CLASS_RO_$_MPSNDArraySinGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySinh
+ __OBJC_CLASS_RO_$_MPSNDArraySinhGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySoftMax
+ __OBJC_CLASS_RO_$_MPSNDArraySoftMaxGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySolverLU
+ __OBJC_CLASS_RO_$_MPSNDArraySort
+ __OBJC_CLASS_RO_$_MPSNDArraySquare
+ __OBJC_CLASS_RO_$_MPSNDArraySquareGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySquareRoot
+ __OBJC_CLASS_RO_$_MPSNDArraySquareRootGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayStencilKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayStitchedReduction
+ __OBJC_CLASS_RO_$_MPSNDArrayStitchedReductionDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayStitchedReductionRMSNorm
+ __OBJC_CLASS_RO_$_MPSNDArrayStitchedReductionSoftmax
+ __OBJC_CLASS_RO_$_MPSNDArrayStridedSlice
+ __OBJC_CLASS_RO_$_MPSNDArrayStridedSliceGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySubtraction
+ __OBJC_CLASS_RO_$_MPSNDArraySubtractionPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArraySubtractionSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayTan
+ __OBJC_CLASS_RO_$_MPSNDArrayTanGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayTanh
+ __OBJC_CLASS_RO_$_MPSNDArrayTanhGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayTileGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayTileKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayTopK
+ __OBJC_CLASS_RO_$_MPSNDArrayTopKGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayTopKMultiDestination
+ __OBJC_CLASS_RO_$_MPSNDArrayUnaryGradientKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayUnaryKernel
+ __OBJC_CLASS_RO_$_MPSNDArrayVectorLUTDequantize
+ __OBJC_CLASS_RO_$_MPSNDArrayXNOR
+ __OBJC_CLASS_RO_$_MPSNDArrayXNORPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayXNORSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayXOR
+ __OBJC_CLASS_RO_$_MPSNDArrayXORPrimaryGradient
+ __OBJC_CLASS_RO_$_MPSNDArrayXORSecondaryGradient
+ __OBJC_CLASS_RO_$_MPSPluginNDArrayConvolutionDescriptor
+ __OBJC_LABEL_PROTOCOL_$_MPSAutoTuneKernel
+ __OBJC_LABEL_PROTOCOL_$_MPSExternalNDArrayBinary
+ __OBJC_LABEL_PROTOCOL_$_MPSExternalNDArrayBinaryGradient
+ __OBJC_LABEL_PROTOCOL_$_MPSExternalPluginBase
+ __OBJC_LABEL_PROTOCOL_$_MPSNDArrayAllocator
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_MPSExternalNDArrayBinary
+ __OBJC_METACLASS_RO_$_MPSExternalNDArrayBinaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayACos
+ __OBJC_METACLASS_RO_$_MPSNDArrayACosGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayACosh
+ __OBJC_METACLASS_RO_$_MPSNDArrayACoshGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayAND
+ __OBJC_METACLASS_RO_$_MPSNDArrayANDPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayANDSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayASTCQuantizationDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayASin
+ __OBJC_METACLASS_RO_$_MPSNDArrayASinGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayASinh
+ __OBJC_METACLASS_RO_$_MPSNDArrayASinhGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayATan
+ __OBJC_METACLASS_RO_$_MPSNDArrayATan2
+ __OBJC_METACLASS_RO_$_MPSNDArrayATan2PrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayATan2SecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayATanGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayATanh
+ __OBJC_METACLASS_RO_$_MPSNDArrayATanhGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayAbsolute
+ __OBJC_METACLASS_RO_$_MPSNDArrayAbsoluteGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayAddition
+ __OBJC_METACLASS_RO_$_MPSNDArrayAdditionPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayAdditionSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayAffineInt4Dequantize
+ __OBJC_METACLASS_RO_$_MPSNDArrayAffineQuantizationDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayArgSort
+ __OBJC_METACLASS_RO_$_MPSNDArrayBandPart
+ __OBJC_METACLASS_RO_$_MPSNDArrayBinaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayBinaryPrimaryGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayBinarySecondaryGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayCeil
+ __OBJC_METACLASS_RO_$_MPSNDArrayCeilGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayClamp
+ __OBJC_METACLASS_RO_$_MPSNDArrayClampPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayClampSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayClampTertiaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayCol2imKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution2D
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution2DDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution2DGradientWithInput
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution2DGradientWithWeights
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution3D
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution3DGradientWithInput
+ __OBJC_METACLASS_RO_$_MPSNDArrayConvolution3DGradientWithWeights
+ __OBJC_METACLASS_RO_$_MPSNDArrayCos
+ __OBJC_METACLASS_RO_$_MPSNDArrayCosGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayCosh
+ __OBJC_METACLASS_RO_$_MPSNDArrayCoshGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayCostVolume
+ __OBJC_METACLASS_RO_$_MPSNDArrayCostVolumeDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayCropResize
+ __OBJC_METACLASS_RO_$_MPSNDArrayDecompositionLU
+ __OBJC_METACLASS_RO_$_MPSNDArrayDecompositionQR
+ __OBJC_METACLASS_RO_$_MPSNDArrayDepthwiseConvolution2DDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayDepthwiseConvolutionKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayDivision
+ __OBJC_METACLASS_RO_$_MPSNDArrayDivisionPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayDivisionSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayEqual
+ __OBJC_METACLASS_RO_$_MPSNDArrayEqualPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayEqualSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayErf
+ __OBJC_METACLASS_RO_$_MPSNDArrayErfGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponent
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponentBase10
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponentBase10Gradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponentBase2
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponentBase2Gradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayExponentGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayFloor
+ __OBJC_METACLASS_RO_$_MPSNDArrayFloorGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayFourierTransform
+ __OBJC_METACLASS_RO_$_MPSNDArrayGather
+ __OBJC_METACLASS_RO_$_MPSNDArrayGatherGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGatherGradientState
+ __OBJC_METACLASS_RO_$_MPSNDArrayGatherND
+ __OBJC_METACLASS_RO_$_MPSNDArrayGatherNDGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGradientState
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThan
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThanOrEqualTo
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThanOrEqualToPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThanOrEqualToSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThanPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGreaterThanSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayGridSample
+ __OBJC_METACLASS_RO_$_MPSNDArrayHammingDistanceKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayIdentity
+ __OBJC_METACLASS_RO_$_MPSNDArrayIm2colDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayIm2colKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitialization
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationConstant
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationGlorotNormal
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationGlorotUniform
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationIdentity
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationRandomNormal
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationRandomUniform
+ __OBJC_METACLASS_RO_$_MPSNDArrayInitializationTruncatedNormal
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsFinite
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsFiniteGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsInfinite
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsInfiniteGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsNaN
+ __OBJC_METACLASS_RO_$_MPSNDArrayIsNaNGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLUTDequantize
+ __OBJC_METACLASS_RO_$_MPSNDArrayLUTGEMV
+ __OBJC_METACLASS_RO_$_MPSNDArrayLUTQuantizationDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThan
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThanOrEqualTo
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThanOrEqualToPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThanOrEqualToSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThanPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLessThanSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLocalConvolution
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogSoftMax
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogSoftMaxGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithm
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithmBase10
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithmBase10Gradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithmBase2
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithmBase2Gradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayLogarithmGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMaterializeSparseTensor
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathBinaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathBinaryPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathBinarySecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathTernaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathTernaryPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathTernarySecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathTernaryTertiaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathUnaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMathUnaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMatrixMultiplication
+ __OBJC_METACLASS_RO_$_MPSNDArrayMatrixMultiplicationGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMatrixMultiplicationSparse
+ __OBJC_METACLASS_RO_$_MPSNDArrayMaximum
+ __OBJC_METACLASS_RO_$_MPSNDArrayMaximumPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMaximumSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMinimum
+ __OBJC_METACLASS_RO_$_MPSNDArrayMinimumPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMinimumSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayModulo
+ __OBJC_METACLASS_RO_$_MPSNDArrayModuloPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayModuloSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiaryBase
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiaryGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiaryMultiDestinationBase
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiaryMultiDestinationKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiplication
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiplicationPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayMultiplicationSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNAND
+ __OBJC_METACLASS_RO_$_MPSNDArrayNANDPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNANDSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNMS
+ __OBJC_METACLASS_RO_$_MPSNDArrayNOR
+ __OBJC_METACLASS_RO_$_MPSNDArrayNORPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNORSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNOT
+ __OBJC_METACLASS_RO_$_MPSNDArrayNOTGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNegative
+ __OBJC_METACLASS_RO_$_MPSNDArrayNegativeGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNeuronGeLU
+ __OBJC_METACLASS_RO_$_MPSNDArrayNeuronGeLUGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNeuronGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNeuronKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayNormFusionDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayNotEqual
+ __OBJC_METACLASS_RO_$_MPSNDArrayNotEqualPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayNotEqualSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayOR
+ __OBJC_METACLASS_RO_$_MPSNDArrayORPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayORSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayOffsetIdentity
+ __OBJC_METACLASS_RO_$_MPSNDArrayPadGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayPadKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayPoolingKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayPoolingMultiDestinationKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayPower
+ __OBJC_METACLASS_RO_$_MPSNDArrayPowerPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayPowerSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayPrune
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizationDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizedConvolution
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizedGatherND
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizedMatrixMultiplication
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizedScaledDotProductAttention
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandom
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandomNormal
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandomState
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandomStateDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandomTruncatedNormal
+ __OBJC_METACLASS_RO_$_MPSNDArrayRandomUniform
+ __OBJC_METACLASS_RO_$_MPSNDArrayReciprocal
+ __OBJC_METACLASS_RO_$_MPSNDArrayReciprocalGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayReduction
+ __OBJC_METACLASS_RO_$_MPSNDArrayReductionGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayReductionSum
+ __OBJC_METACLASS_RO_$_MPSNDArrayReductionSumGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayResample
+ __OBJC_METACLASS_RO_$_MPSNDArrayResampleGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayReverseSquareRoot
+ __OBJC_METACLASS_RO_$_MPSNDArrayReverseSquareRootGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayRint
+ __OBJC_METACLASS_RO_$_MPSNDArrayRintGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayRound
+ __OBJC_METACLASS_RO_$_MPSNDArrayRoundGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayScaledDotProductAttention
+ __OBJC_METACLASS_RO_$_MPSNDArrayScan
+ __OBJC_METACLASS_RO_$_MPSNDArrayScanGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayScatter
+ __OBJC_METACLASS_RO_$_MPSNDArrayScatterGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySelect
+ __OBJC_METACLASS_RO_$_MPSNDArraySelectPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySelectSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySelectTertiaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySign
+ __OBJC_METACLASS_RO_$_MPSNDArraySignGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySignbit
+ __OBJC_METACLASS_RO_$_MPSNDArraySignbitGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySin
+ __OBJC_METACLASS_RO_$_MPSNDArraySinGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySinh
+ __OBJC_METACLASS_RO_$_MPSNDArraySinhGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySoftMax
+ __OBJC_METACLASS_RO_$_MPSNDArraySoftMaxGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySolverLU
+ __OBJC_METACLASS_RO_$_MPSNDArraySort
+ __OBJC_METACLASS_RO_$_MPSNDArraySquare
+ __OBJC_METACLASS_RO_$_MPSNDArraySquareGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySquareRoot
+ __OBJC_METACLASS_RO_$_MPSNDArraySquareRootGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayStencilKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayStitchedReduction
+ __OBJC_METACLASS_RO_$_MPSNDArrayStitchedReductionDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayStitchedReductionRMSNorm
+ __OBJC_METACLASS_RO_$_MPSNDArrayStitchedReductionSoftmax
+ __OBJC_METACLASS_RO_$_MPSNDArrayStridedSlice
+ __OBJC_METACLASS_RO_$_MPSNDArrayStridedSliceGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySubtraction
+ __OBJC_METACLASS_RO_$_MPSNDArraySubtractionPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArraySubtractionSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayTan
+ __OBJC_METACLASS_RO_$_MPSNDArrayTanGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayTanh
+ __OBJC_METACLASS_RO_$_MPSNDArrayTanhGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayTileGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayTileKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayTopK
+ __OBJC_METACLASS_RO_$_MPSNDArrayTopKGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayTopKMultiDestination
+ __OBJC_METACLASS_RO_$_MPSNDArrayUnaryGradientKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayUnaryKernel
+ __OBJC_METACLASS_RO_$_MPSNDArrayVectorLUTDequantize
+ __OBJC_METACLASS_RO_$_MPSNDArrayXNOR
+ __OBJC_METACLASS_RO_$_MPSNDArrayXNORPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayXNORSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayXOR
+ __OBJC_METACLASS_RO_$_MPSNDArrayXORPrimaryGradient
+ __OBJC_METACLASS_RO_$_MPSNDArrayXORSecondaryGradient
+ __OBJC_METACLASS_RO_$_MPSPluginNDArrayConvolutionDescriptor
+ __OBJC_PROTOCOL_$_MPSAutoTuneKernel
+ __OBJC_PROTOCOL_$_MPSExternalNDArrayBinary
+ __OBJC_PROTOCOL_$_MPSExternalNDArrayBinaryGradient
+ __OBJC_PROTOCOL_$_MPSExternalPluginBase
+ __OBJC_PROTOCOL_$_MPSNDArrayAllocator
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_MPSNDArrayAllocator
+ __Z10getStridesP10MPSNDArrayPmm
+ __Z15IsNDArraySlicedPK10MPSNDArrayPb
+ __Z17CallNDArrayEncodePK24MPSNDArrayMultiaryKernelPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectmmP23NDArrayMultiaryCallInfo
+ __Z19IsNDArrayTransposedDv16_h33MPSNDArrayConvolution2DDataFormatRS0_
+ __Z20mpsMatrixFromNDArrayP10MPSNDArraym
+ __Z23MPSGetLinearOffsetBytesP10MPSNDArraymmP26MPSNDArrayKernelParametersb
+ __Z25CallNDArrayGradientEncodePK32MPSNDArrayMultiaryGradientKernelPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectmmP23NDArrayMultiaryCallInfob
+ __Z25ndArrayConvDeviceBehaviorP9MPSDevicey
+ __Z27ndArrayConv3DDeviceBehaviorP9MPSDevicey
+ __Z28CallNDArrayNewGradientEncodePK32MPSNDArrayMultiaryGradientKernelPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectmmP23NDArrayMultiaryCallInfo
+ __Z28ndArrayConvDeviceBehaviorAMDP9MPSDevicey
+ __Z29MPSNDArraySDPAA14BehaviorCtorP9MPSDevicey
+ __Z29ndArrayConvDeviceBehaviorAGX3P9MPSDevicey
+ __Z29ndArrayConvDeviceBehaviorCebuP9MPSDevicey
+ __Z30MPSNDArrayScanAMDBehaviorsCtorP9MPSDevicey
+ __Z30MPSNDArraySortAMDBehaviorsCtorP9MPSDevicey
+ __Z30MPSSetNDArraysOnComputeEncoderP17MPSComputeEncoderPK23NDArrayMultiaryCallInfombb
+ __Z30ndArrayA14MatMulDeviceBehaviorP9MPSDevicey
+ __Z30ndArrayConvDeviceBehaviorArubaP9MPSDevicey
+ __Z30ndArrayConvDeviceBehaviorJadeCP9MPSDevicey
+ __Z30ndArrayConvDeviceBehaviorJadeSP9MPSDevicey
+ __Z31GetNaviKernelParametersNCHWFP16RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetNaviKernelParametersNCHWFP32RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetNaviKernelParametersNHWCFP16RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetNaviKernelParametersNHWCFP32RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetVegaKernelParametersNCHWFP16RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetVegaKernelParametersNCHWFP32RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetVegaKernelParametersNHWCFP16RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31GetVegaKernelParametersNHWCFP32RK35MPSNDArrayConvolutionDispatchKeyAMD
+ __Z31MPSKernelLogPerfTestCommandlinePK24MPSNDArrayMultiaryKernelPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEESB_
+ __Z31ParseAutoTuningKernelParametersP42MPSGradientWithWeightsAutoTuningParametersR50MPSNDArrayConvolutionGradientWithWeightsParametersR56MPSNDArrayConvolutionGradientWithWeightsKernelParameters
+ __Z31ndArrayConvDeviceBehaviorPreG13P9MPSDevicey
+ __Z32GetPlaceHolderIndexInSourceArrayP12MPSKernelDAGPmS1_
+ __Z32MPSNDArrayScanIntelBehaviorsCtorP9MPSDevicey
+ __Z32MPSNDArraySortCreateUserConstantR44MPSNDArraySortPipelineStateFunctionConstants
+ __Z32MPSNDArraySortIntelBehaviorsCtorP9MPSDevicey
+ __Z32ndArrayConvDeviceBehaviorRhodesCP9MPSDevicey
+ __Z33CallNDArrayEncodeMultiDestinationPK40MPSNDArrayMultiaryMultiDestinationKernelPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectmmP39NDArrayMultiaryMultiDestinationCallInfo
+ __Z33MPSNDArrayLUTGEMVAMDBehaviorsCtorP9MPSDevicey
+ __Z33MPSNDArraySDPADefaultBehaviorCtorP9MPSDevicey
+ __Z33mainSourcesHaveRectangularStridesP28NDArrayConvolutionEncodeData
+ __Z33ndArrayCommonMatMulDeviceBehaviorP9MPSDevicey
+ __Z34MPSNDArrayIdentityAMDBehaviorsCtorP9MPSDevicey
+ __Z34MPSNDArrayScanDefaultBehaviorsCtorP9MPSDevicey
+ __Z34MPSNDArraySortDefaultBehaviorsCtorP9MPSDevicey
+ __Z35EncodePoolingMultiDestination1DPassPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfoimmmlPU19objcproto9MTLBuffer11objc_objectS9_Dv4_jSA_b11MPSDataType
+ __Z35MPSNDArrayLUTGEMVAppleBehaviorsCtorP9MPSDevicey
+ __Z35MPSNDArrayReductionAMDBehaviorsCtorP9MPSDevicey
+ __Z36MPSNDArrayIdentityAppleBehaviorsCtorP9MPSDevicey
+ __Z36MPSNDArrayReductionAA10BehaviorsCtorP9MPSDevicey
+ __Z36ndArrayConvDeviceBehaviorSicilyTongaP9MPSDevicey
+ __Z39MPSNDArrayConvPreG13FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __Z39MPSNDArrayReductionDefaultBehaviorsCtorP9MPSDevicey
+ __Z40MPSNDArrayOptimGEMVI8FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __Z41MPSNDArrayReductionCreateUserConstantAxesR53MPSNDArrayReductionPipelineStateFunctionConstantsAxes
+ __Z42GetPlaceHolderIndexInSourceArrayAffineGEMMP12MPSKernelDAGP38MPSNDArrayAffineQuantizationDescriptorPlS2_S3_bPPK10BaseTensorS7_
+ __Z43EncodeQuantizedMatrixMultiplicationFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __Z43MPSNDArrayVectorMultiplyFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __Z45GetPlaceHolderIndexInSourceArrayQuantizedGEMMP12MPSKernelDAGP32MPSNDArrayQuantizationDescriptorPlS2_S3_bPb
+ __Z59MPSNDArrayConvolutionGradientWithWeightsFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __Z9getOffsetP10MPSNDArrayPm
+ __ZL10A10Threads
+ __ZL10AMDThreads
+ __ZL10EncodeSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL10EncodeScanPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL10EncodeSortPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL10EncodeTilePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL10EncodeTopKPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL10jadeCTable
+ __ZL10jadeSTable
+ __ZL10tongaTable
+ __ZL11FlattenTo2DP10MPSNDArrayP18MPSNDArrayIdentityPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectm
+ __ZL11FlattenTo3DP10MPSNDArrayP18MPSNDArrayIdentityPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZL12EncodeDWConvPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL12EncodeGatherPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL12flattenAliasPU27objcproto16MTLCommandBuffer11objc_objectPK10MPSNDArrayDv16_jm
+ __ZL12validateSDPAP10MPSNDArrayS0_S0_S0_20MPSNDArraySDPALayout
+ __ZL13CommonKernels
+ __ZL13EncodeArgSortPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL13EncodePoolingPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL13EncodeScatterPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL13EncodeStencilPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL13c_passRadixes
+ __ZL13reshapeTensorP10BaseTensorP10MPSNDArray
+ __ZL13resolvePassesPmRmmbDv4_ii11MPSDataTypePK22MPSNDArrayFFTBehaviorsm
+ __ZL13unpackSourcesP28NDArrayConvolutionEncodeDataP37MPSNDArrayQuantizedConvolutionSources
+ __ZL14EncodeArrayFFTPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL14EncodeGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL14EncodeResamplePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL14EncodeSolverLUPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL14defaultThreads
+ __ZL14naviParameters
+ __ZL14vegaParameters
+ __ZL15EncodeReductionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL15a16KernelParams
+ __ZL15canAliasToShapePK10MPSNDArrayDv16_jm
+ __ZL15decodeMultiplesP7NSCoderR15MPSNDArraySizes
+ __ZL15encodeMultiplesP7NSCoderRK15MPSNDArraySizes
+ __ZL15nchwDirectTable
+ __ZL16EncodeArrayPrunePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL16EncodeCostVolumePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL16EncodeGridSamplePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL16EncodeScanCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringmjmbb
+ __ZL16EncodeTopKCommonPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP10MPSLibrarymbbb
+ __ZL16RhodesDParams6x6
+ __ZL16RhodesDParams8x5
+ __ZL16get3DTileStridesP10MPSNDArrayPm
+ __ZL16printDWTransposeP36MPSNDArrayDepthwiseConvolutionKernelRDv16_hmb
+ __ZL17EncodeArrayCol2imPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL17EncodeArrayIm2colPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL17EncodeArrayNeuronPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL17EncodePadGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL17MPSKernel_LogInfoP9MPSKernelmPKcz
+ __ZL17cebuNCHWxHWIOHalf
+ __ZL17cebuNHWCxHWIOHalf
+ __ZL17getDispatchParamsPjPb7MTLSizemmbm
+ __ZL17isI8GEMVSupportedP46NDArrayQuantizedMatrixMultiplicationEncodeData
+ __ZL17nchwWinogradTable
+ __ZL18EncodeArrayLUTGEMVPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL18EncodeArraySoftMaxPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL18EncodeGatherCommonPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfobb
+ __ZL18EncodeRandomNormalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL18EncodeScanGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL18EncodeStridedSlicePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL18EncodeTileGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL18EncodeTopKGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL18aliasSqueezeExpandPK10MPSNDArrayPU27objcproto16MTLCommandBuffer11objc_objectmDv16_j
+ __ZL18arubaNCHWxHWIOHalf
+ __ZL18arubaNHWCxHWIOHalf
+ __ZL18cebuNCHWxHWIOFloat
+ __ZL18cebuNHWCxHWIOFloat
+ __ZL18readSrcTempNDArrayPK23NDArrayMultiaryCallInfoPS_PU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectP18MPSNDArrayIdentitymmmmmb
+ __ZL18updateDAGDestShapePP18MPSKernelDAGObjectP10MPSNDArray
+ __ZL19EncodeArrayBandPartPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL19EncodeArrayIdentityPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL19EncodeArrayMultiplyPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL19EncodeQuantizedSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL19EncodeRandomUniformPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL19EncodeSDPACommonNewPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttentionj
+ __ZL19EncodeScatterCommonPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP18MPSNDArrayIdentity26MPSNDArrayScatterOperationmbb
+ __ZL19arubaNCHWxHWIOFloat
+ __ZL19arubaNHWCxHWIOFloat
+ __ZL19checkInputAndWeightP10BaseTensorS0_RK26MPSNDArrayConvolutionSizes10DataLayout
+ __ZL20EncodeArrayFFTKernelPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoR12MPSAutoCachej26MPSNDArrayFFTScalingMode_sdb11MPSDataTypeSB_Dv4_iSC_15FFTKernelType_sPU19objcproto9MTLBuffer11objc_objectSF_SF_
+ __ZL20EncodeArrayMathUnaryPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL20EncodeDWConvGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL20EncodeGatherGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL20EncodeMatrixMultiplyPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP10MPSNDArrayS6_S6_S6_PK23NDArrayMultiaryCallInfoRb
+ __ZL20EncodeRandomInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo34MPSNDArrayRandomDistributionParams
+ __ZL20MPSNDArrayFFTKernels
+ __ZL20MPSNDArrayNMSKernels
+ __ZL20MPSNDArrayPadKernels
+ __ZL21EncodeArrayCropResizePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodeArrayLUTDequantPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodeArrayMathBinaryPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodeDecompositionLUPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL21EncodeHammingDistancePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodePoolingGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL21EncodeQRDecompositionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodeScatterGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL21MPSNDArraySDPAKernels
+ __ZL21MPSNDArrayScanKernels
+ __ZL21MPSNDArraySortKernels
+ __ZL21MPSNDArrayTileKernels
+ __ZL21MPSNDArrayTopKKernels
+ __ZL21validateQuantizedSDPAP10MPSNDArrayS0_S0_S0_S0_S0_S0_20MPSNDArraySDPALayout
+ __ZL22AdjustKernelParametersRK35MPSNDArrayConvolutionDispatchKeyAMDR40MPSNDArrayConvolutionKernelParametersAMD
+ __ZL22EncodeArrayMathTernaryPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL22EncodeGatherNDGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL22EncodeLocalConvolutionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL22EncodeResampleGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL22MPSNDArrayPruneKernels
+ __ZL23AddFunctionConstantListP25MTLFunctionConstantValuesRK23MPSFunctionConstantList
+ __ZL23EncodeQuantizedGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL23EncodeRandomStateUpdatePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL23EncodeStitchedReductionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL23MPSNDArrayCol2imKernels
+ __ZL23MPSNDArrayDWConvKernels
+ __ZL23MPSNDArrayGatherKernels
+ __ZL23MPSNDArrayIm2colKernels
+ __ZL23MPSNDArrayNeuronKernels
+ __ZL23MPSNDArrayRandomKernels
+ __ZL23a14WinogradLaunchParams
+ __ZL24EncodeArrayPruneGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL24EncodeGridSampleGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL24EncodeStridedSliceCommonPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfobb
+ __ZL24MPSNDArrayLUTGEMVKernels
+ __ZL24MPSNDArrayPoolingKernels
+ __ZL24MPSNDArrayScatterKernels
+ __ZL24MPSNDArraySoftMaxKernels
+ __ZL24MPSNDArraySolveLUKernels
+ __ZL24RandomStateCommonKernels
+ __ZL24isDescSupportedByLUTGEMVP32MPSNDArrayQuantizationDescriptor
+ __ZL24sicilyTongaNCHWxHWIOHalf
+ __ZL24sicilyTongaNHWCxHWIOHalf
+ __ZL25EncodeArrayIdentityOffsetPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL25EncodeArrayMultiplySparsePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL25EncodeArrayNeuronGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL25MPSNDArrayBandPartKernels
+ __ZL25MPSNDArrayGatherNDKernels
+ __ZL25MPSNDArrayIdentityKernels
+ __ZL25MPSNDArrayResampleKernels
+ __ZL25sicilyTongaNCHWxHWIOFloat
+ __ZL25sicilyTongaNHWCxHWIOFloat
+ __ZL26EncodeArraySoftMaxGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL26EncodeGlorotInitializationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL26EncodeMatrixVectorMultiplyPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP10MPSNDArrayS6_S6_S6_PK23NDArrayMultiaryCallInfo
+ __ZL26EncodeNDArrayConvolution2DPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL26EncodeNDArrayConvolution3DPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL26EncodeRandomInitializationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL26EncodeStridedSliceGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL26EncodeTopKMultiDestinationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL26MPSNDArrayMathUnaryKernels
+ __ZL26MPSNDArrayReductionKernels
+ __ZL27EncodeArrayAffieInt4DequantPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL27EncodeArrayMultiplyGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL27EncodeArrayVectorLUTDequantPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL27EncodeMatrixMultiplyLinkingPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL27EncodeRandomTruncatedNormalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL27MPSFunctionConstantListNone
+ __ZL27MPSNDArrayCostVolumeKernels
+ __ZL27MPSNDArrayCropResizeKernels
+ __ZL27MPSNDArrayGridSampleKernels
+ __ZL27MPSNDArrayMathBinaryKernels
+ __ZL28EncodeArrayMathUnaryGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL28EncodeConstantInitializationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL28EncodeIdentityInitializationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL28MPSNDArrayMathTernaryKernels
+ __ZL28MPSNDArrayRandomStateKernels
+ __ZL28MPSNDArraySDPALogCommandLineP24MPSNDArrayMultiaryKernelPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
+ __ZL28getFlattenedDimensionsVectorPK10MPSNDArrayDv16_jmPDv16_hPS2_
+ __ZL28threadGroupSizeInfoListApple
+ __ZL29EncodeArrayMathBinaryGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL29EncodeMaterializeSparseTensorPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL29EncodeMatrixMultiplyMPSMatrixPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP18MPSNDArrayIdentityP10MPSNDArrayS8_S8_S8_PK23NDArrayMultiaryCallInfo
+ __ZL29EncodePoolingMultiDestinationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL29GetKernelParametersNCHWCommonRK35MPSNDArrayConvolutionDispatchKeyAMD
+ __ZL29MPSNDArrayFFTBehaviorsCtorA10P9MPSDevicey
+ __ZL29MPSNDArrayStridedSliceKernels
+ __ZL30EncodeArrayMathTernaryGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL30EncodeLocalConvolutionGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL30EncodeMatrixMultiplyLinkingA14PKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL30EncodeMatrixVectorMultiplyInt8PKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL30EncodeQuantizedSDPAVectorBasedPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention
+ __ZL30EncodeTopKMultiDestinationBasePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL30IsOptimizedInt4KernelSupportedPK39MPSNDArrayQuantizedMatrixMultiplicationPK23NDArrayMultiaryCallInfo
+ __ZL31EncodeArrayReductionGradientNewPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL31MPSNDArrayGridSampleConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL31MPSNDArrayInitializationKernels
+ __ZL31threadGroupSizeInfoListNonApple
+ __ZL31validateLUTMatrixMultiplicationP7NSArrayIP10MPSNDArrayEbmmmP8NSString
+ __ZL32EncodeDWConvGradientBackPropImplPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfobb
+ __ZL32MPSNDArrayDecompositionLUKernels
+ __ZL32MPSNDArrayDecompositionQRKernels
+ __ZL32MPSNDArrayDequantInt4LibraryInfo
+ __ZL32MPSNDArrayFFTFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL32MPSNDArrayHammingDistanceKernels
+ __ZL32MPSNDArraySDPACreateUserConstantR36MPSNDArraySDPAStateFunctionConstants
+ __ZL32MPSNDArrayScanCreateUserConstantR44MPSNDArrayScanPipelineStateFunctionConstants
+ __ZL33CommonKernelsConvolution2DForward
+ __ZL33CommonKernelsConvolution3DForward
+ __ZL33EncodePoolingMultiDestinationBasePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL33GetNaviKernelParametersNHWCCommonRK35MPSNDArrayConvolutionDispatchKeyAMD
+ __ZL33GetVegaKernelParametersNHWCCommonRK35MPSNDArrayConvolutionDispatchKeyAMD
+ __ZL33MPSNDArrayFFTDefaultBehaviorsCtorP9MPSDevicey
+ __ZL33MPSNDArrayInt4FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL33MPSNDArrayLocalConvolutionKernels
+ __ZL33MPSNDArraySDPAFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL33a14DirectConvolutionNCHWxHWIOHalf
+ __ZL33a14DirectConvolutionNHWCxHWIOHalf
+ __ZL34EncodeQuantizedConvolutionFallbackPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZL34EncodeRandomInitializationInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP39MPSParallelRandomDistributionDescriptor
+ __ZL34MPSNDArrayPruneFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL34MPSNDArrayQuantizedGatherNDKernels
+ __ZL34MPSNDArrayStitchedReductionKernels
+ __ZL34a14DirectConvolutionNCHWxHWIOFloat
+ __ZL34a14DirectConvolutionNHWCxHWIOFloat
+ __ZL34a14SDirectConvolutionNCHWxHWIOHalf
+ __ZL34a14SDirectConvolutionNHWCxHWIOHalf
+ __ZL34a15XDirectConvolutionNCHWxHWIOHalf
+ __ZL34a15XDirectConvolutionNHWCxHWIOHalf
+ __ZL34validateAffineMatrixMultiplicationP7NSArrayIP10MPSNDArrayEmmP8NSString
+ __ZL35EncodeQuantizedMatrixMultiplicationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL35GetPlaceHolderIndexInSourceArrayLUTP12MPSKernelDAGbbPmS1_jb
+ __ZL35MPSNDArrayConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEb
+ __ZL35a14SDirectConvolutionNCHWxHWIOFloat
+ __ZL35a14SDirectConvolutionNHWCxHWIOFloat
+ __ZL35a15XDirectConvolutionNCHWxHWIOFloat
+ __ZL35a15XDirectConvolutionNHWCxHWIOFloat
+ __ZL36EncodeConstantInitializationInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL36MPSNDArrayLUTGEMVFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL36MPSNDArrayPoolingFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL37MPSNDArrayConvolution2DForwardKernels
+ __ZL37MPSNDArrayConvolution3DForwardKernels
+ __ZL37MPSNDArrayConvolution3DLogCommandLineP24MPSNDArrayMultiaryKernelR30NDArrayConvolution3DEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEE
+ __ZL37MPSNDArrayIdentityFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL37MPSNDArrayLUTGEMVDefaultBehaviorsCtorP9MPSDevicey
+ __ZL37MPSNDArrayLocalConvolutionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL37MPSNDArrayMatrixMultiplicationKernels
+ __ZL37MPSNDArrayResampleFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL38EncodeNDArrayQuantizationConvolution2DPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL38MPSNDArrayIdentityDefaultBehaviorsCtorP9MPSDevicey
+ __ZL39GetPlaceHolderIndexInSourceArrayLUTGEMMP12MPSKernelDAGP35MPSNDArrayLUTQuantizationDescriptorPlS2_S3_b
+ __ZL39MPSNDArrayFunctionConstructorSparseGEMMPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL41MPSNDArrayQuantizedConvolutionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL43CommonKernelsConvolution2DGradientWithInput
+ __ZL43CommonKernelsConvolution3DGradientWithInput
+ __ZL43MPSNDArrayConvolutionA14FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL43MPSNDArrayConvolutionAMDFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL43MPSNDArrayMatrixMultiplicationSparseKernels
+ __ZL44EncodeNDArrayConvolution2DGradientWithIntputPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL44EncodeNDArrayConvolution3DGradientWithIntputPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL44MPSNDArrayFunctionConstructorQRDecompositionPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL44MPSNDArrayPoolingGradientFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL44MPSNDArrayQuantizedConvolutionLogCommandLineP24MPSNDArrayMultiaryKernelR28NDArrayConvolutionEncodeDataPK23NDArrayMultiaryCallInfoNSt3__112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEEb
+ __ZL45CommonKernelsConvolution2DGradientWithWeights
+ __ZL45EncodeNDArrayConvolution2DGradientWithWeightsPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL45EncodeNDArrayConvolution3DGradientWithWeightsPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZL46GetPlaceHolderIndexInSourceArrayQuantizedGEMM2P12MPSKernelDAGP32MPSNDArrayQuantizationDescriptorPlS2_S3_b
+ __ZL46MPSNDArrayMatrixMultiplyA14FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL47MPSNDArrayConvolution2DGradientWithInputKernels
+ __ZL49GetKernelDispatchParametersForKeyIntrinsicsCommonR32MPSNDArrayConvolutionDispatchKey37MPSNDArrayConvolutionDispatchDataType35MPSNDArrayConvolutionDispatchFormatP36MPSForwardDirectAutoTuningParametersPK57MPSNDArrayConvolutionKernelParametersTableEntryIntrinsicsmPK24MPSNDArrayConvolutionKeyP9MPSDevice
+ __ZL49MPSNDArrayConvolution2DGradientWithWeightsKernels
+ __ZL4keys
+ __ZL50MPSNDArrayQuantizedMatrixMultiplicationConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL51MPSNDArrayQ4IntoQ8MatrixMultiplyFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL52MPSNDArrayDepthwiseConvWeightGradFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL8rawAliasPU27objcproto16MTLCommandBuffer11objc_objectPK10MPSNDArrayDv16_jmb
+ __ZL9EncodeNMSPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL9EncodePadPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZN14MPSAutoEncoderD1Ev
+ __ZN14MPSAutoEncoderD2Ev
+ __ZN14MPSBufferCache9getBufferEPU19objcproto9MTLDevice11objc_objectmU13block_pointerFvPU19objcproto9MTLBuffer11objc_objectE
+ __ZN14MPSBufferCacheD1Ev
+ __ZN16MPSKernelUserDAG10reciprocalEP20MPSKernelUserDAGNode11MPSDataType
+ __ZN17ScopedMPSSignpostD1Ev
+ __ZN22MPSNDArrayFFTBehaviorsD0Ev
+ __ZN22MPSNDArrayFFTBehaviorsD1Ev
+ __ZN23MPSNDArrayScanBehaviorsD0Ev
+ __ZN23MPSNDArrayScanBehaviorsD1Ev
+ __ZN25MPSNDArraySDPAA14BehaviorD0Ev
+ __ZN25MPSNDArraySDPAA14BehaviorD1Ev
+ __ZN26MPSNDArrayLUTGEMVBehaviorsD0Ev
+ __ZN26MPSNDArrayLUTGEMVBehaviorsD1Ev
+ __ZN27MPSNDArrayIdentityBehaviorsD0Ev
+ __ZN27MPSNDArrayIdentityBehaviorsD1Ev
+ __ZN28MPSNDArrayReductionBehaviorsD0Ev
+ __ZN28MPSNDArrayReductionBehaviorsD1Ev
+ __ZN28MPSNDArraySDPADeviceBehaviorD0Ev
+ __ZN28MPSNDArraySDPADeviceBehaviorD1Ev
+ __ZN29MPSNDArrayLUTGEMVAMDBehaviorsD0Ev
+ __ZN29MPSNDArrayLUTGEMVAMDBehaviorsD1Ev
+ __ZN29MPSNDArraySortDeviceBehaviorsD0Ev
+ __ZN29MPSNDArraySortDeviceBehaviorsD1Ev
+ __ZN30MPSNDArrayIdentityAMDBehaviorsD0Ev
+ __ZN30MPSNDArrayIdentityAMDBehaviorsD1Ev
+ __ZN30MPSNDArrayMatMulDeviceBehaviorC2EP9MPSDevicey
+ __ZN30MPSNDArrayMatMulDeviceBehaviorD0Ev
+ __ZN30MPSNDArrayMatMulDeviceBehaviorD1Ev
+ __ZN31MPSNDArrayLUTGEMVAppleBehaviorsD0Ev
+ __ZN31MPSNDArrayLUTGEMVAppleBehaviorsD1Ev
+ __ZN32MPSNDArrayIdentityAppleBehaviorsD0Ev
+ __ZN32MPSNDArrayIdentityAppleBehaviorsD1Ev
+ __ZN33MPSNDArrayMatMulA14DeviceBehaviorD0Ev
+ __ZN33MPSNDArrayMatMulA14DeviceBehaviorD1Ev
+ __ZN35MPSNDArrayConvolutionDeviceBehaviorD0Ev
+ __ZN35MPSNDArrayConvolutionDeviceBehaviorD1Ev
+ __ZN36MPSNDArrayMatMulCommonDeviceBehaviorD0Ev
+ __ZN36MPSNDArrayMatMulCommonDeviceBehaviorD1Ev
+ __ZN37MPSNDArrayConvolution3DDeviceBehaviorD0Ev
+ __ZN37MPSNDArrayConvolution3DDeviceBehaviorD1Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA14C2EPK55MPSNDArrayConvolutionGradientWithWeightsParametersTablemP9MPSDevice
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA14D0Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA14D1Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA16D0Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorA16D1Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorAMDC2EPK51MPSNDArrayConvolutionGradientWithWeightsKeyValueAMDmP9MPSDevice
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorAMDD0Ev
+ __ZN38MPSNDArrayConvolutionDeviceBehaviorAMDD1Ev
+ __ZN39MPSNDArrayConvolutionDeviceBehaviorA15XD0Ev
+ __ZN39MPSNDArrayConvolutionDeviceBehaviorA15XD1Ev
+ __ZN39MPSNDArrayConvolutionDeviceBehaviorCebuD0Ev
+ __ZN39MPSNDArrayConvolutionDeviceBehaviorCebuD1Ev
+ __ZN40MPSNDArrayConvolutionDeviceBehaviorArubaD0Ev
+ __ZN40MPSNDArrayConvolutionDeviceBehaviorArubaD1Ev
+ __ZN41MPSNDArrayConvolutionDeviceBehaviorPreG13C2EPK47MPSNDArrayConvolutionKernelParametersTableEntryS2_S2_S2_P9MPSDevice
+ __ZN41MPSNDArrayConvolutionDeviceBehaviorPreG13D0Ev
+ __ZN41MPSNDArrayConvolutionDeviceBehaviorPreG13D1Ev
+ __ZNK10BaseTensor15GetNDArrayShapeEv
+ __ZNK10BaseTensor19GetDebugDescriptionERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNK13BaseOperation22GetNodeIdForBaseTensorERNSt3__13mapIPK10BaseTensorDv2_iNS0_4lessIS4_EENS0_9allocatorINS0_4pairIKS4_S5_EEEEEERiS4_b
+ __ZNK13BaseOperation23DebugDescriptionPrivateERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS0_3mapIPK10BaseTensorDv2_iNS0_4lessISB_EENS4_INS0_4pairIKSB_SC_EEEEEERi
+ __ZNK22MPSNDArrayFFTBehaviors13getMinDimSizeEv
+ __ZNK22MPSNDArrayFFTBehaviors14getLaunchOrderEDv4_iS0_S0_Pi
+ __ZNK22MPSNDArrayFFTBehaviors18isMediumCombinedOkEDv4_ii11MPSDataType
+ __ZNK22MPSNDArrayFFTBehaviors19allowCombinedKernelEDv4_ii11MPSDataTypem
+ __ZNK22MPSNDArrayFFTBehaviors23getNZStepsLog2PerThreadEbDv4_j
+ __ZNK23MPSNDArrayScanBehaviors10getThreadsEv
+ __ZNK25MPSNDArraySDPAA14Behavior10EncodeSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK25MPSNDArraySDPAA14Behavior19EncodeQuantizedSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK26MPSNDArrayLUTGEMVBehaviors13getMinDimSizeEv
+ __ZNK26MPSNDArrayLUTGEMVBehaviors13getNResPerDimERK26MPSNDArrayLUTGEMV_params_sb11MPSDataTypejb
+ __ZNK26MPSNDArrayLUTGEMVBehaviors14getLaunchOrderEDv4_iS0_S0_Pi
+ __ZNK27MPSNDArrayIdentityBehaviors13getMinDimSizeEv
+ __ZNK27MPSNDArrayIdentityBehaviors14getLaunchOrderEDv4_iS0_S0_Pi
+ __ZNK27MPSNDArrayIdentityBehaviors21getNXResultsPerThreadEDv4_iS0_
+ __ZNK27MPSNDArrayIdentityBehaviors23getNZStepsLog2PerThreadEbDv4_i
+ __ZNK28MPSNDArrayReductionBehaviors10getThreadsEv
+ __ZNK28MPSNDArraySDPADeviceBehavior10EncodeSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK28MPSNDArraySDPADeviceBehavior10getThreadsEv
+ __ZNK28MPSNDArraySDPADeviceBehavior19EncodeQuantizedSDPAEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK29MPSNDArraySortDeviceBehaviors10getThreadsEv
+ __ZNK29MPSNDArraySortDeviceBehaviors17EncodeNDArraySortEP14MPSNDArraySortPU19objcproto9MTLDevice11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringmP14MPSNDArrayScanmbb
+ __ZNK29MPSNDArraySortDeviceBehaviors18isArgsortSupportedEv
+ __ZNK29MPSNDArraySortDeviceBehaviors23isSortGradientSupportedEv
+ __ZNK29MPSNDArraySortDeviceBehaviors58getCutoffArraySizeForMultipleThreadgroupWaveMatchRadixSortEv
+ __ZNK30MPSNDArrayIdentityAMDBehaviors23getNZStepsLog2PerThreadEbDv4_i
+ __ZNK30MPSNDArrayMatMulDeviceBehavior19EncodeArrayMultiplyEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK30MPSNDArrayMatMulDeviceBehavior21EncodeArrayMultiplyI4EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK30MPSNDArrayMatMulDeviceBehavior33IsInt8AffineSupportedQuantizationEP46NDArrayQuantizedMatrixMultiplicationEncodeData
+ __ZNK30MPSNDArrayMatMulDeviceBehavior37IsInt2Int8AffineSupportedQuantizationEP46NDArrayQuantizedMatrixMultiplicationEncodeData
+ __ZNK30MPSNDArrayMatMulDeviceBehavior45EncodeQuantizedMatrixMultiplicationInt8AffineEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK30MPSNDArrayMatMulDeviceBehavior49EncodeQuantizedMatrixMultiplicationInt2Int8AffineEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK31MPSNDArrayLUTGEMVAppleBehaviors13getMinDimSizeEv
+ __ZNK31MPSNDArrayLUTGEMVAppleBehaviors14getLaunchOrderEDv4_iS0_S0_Pi
+ __ZNK32MPSNDArrayIdentityAppleBehaviors13getMinDimSizeEv
+ __ZNK32MPSNDArrayIdentityAppleBehaviors14getLaunchOrderEDv4_iS0_S0_Pi
+ __ZNK33MPSNDArrayMatMulA14DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
+ __ZNK33MPSNDArrayMatMulA14DeviceBehavior19EncodeArrayMultiplyEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior13log2SIMDWidthEv
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior17transposedWeightsEP18MPSNDArrayIdentityPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectP10MPSNDArrayRNSt3__16vectorIlNS8_9allocatorIlEEEE36MPSNDArrayConvolution2DWeightsFormatSE_
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior21IsDataFormatSupportedE33MPSNDArrayConvolution2DDataFormat
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior22IsConvolutionSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior23IsQuantizationSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior24EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior24IsWeightsFormatSupportedE36MPSNDArrayConvolution2DWeightsFormat
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior30DoWeightsNeedPhysicalTransposeEP10MPSNDArrayS1_P28NDArrayConvolutionEncodeData
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior41IsConvolutionGradientWithWeightsSupportedEP42MPSNDArrayConvolution2DGradientWithWeightsPK23NDArrayMultiaryCallInfo
+ __ZNK35MPSNDArrayConvolutionDeviceBehavior43EncodeNDArrayConvolutionGradientWithWeightsEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZNK36MPSNDArrayMatMulCommonDeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
+ __ZNK36MPSNDArrayMatMulCommonDeviceBehavior19EncodeArrayMultiplyEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZNK37MPSNDArrayConvolution3DDeviceBehavior26EncodeNDArrayConvolution3DEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP30NDArrayConvolution3DEncodeData
+ __ZNK37MPSNDArrayConvolution3DDeviceBehavior45EncodeNDArrayConvolution3DGradientWithWeightsEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP30NDArrayConvolution3DEncodeDatab
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1419GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1419IsWinogradSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1421IsIntrinsicsSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1422IsConvolutionSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1423IsQuantizationSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1424EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1432EncodeNDArrayConvolutionWinogradEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1434EncodeNDArrayConvolutionIntrinsicsEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1443EncodeNDArrayConvolutionGradientWithWeightsEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1443GetKernelDispatchParametersForKeyIntrinsicsER32MPSNDArrayConvolutionDispatchKey37MPSNDArrayConvolutionDispatchDataType35MPSNDArrayConvolutionDispatchFormatP36MPSForwardDirectAutoTuningParameters
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1619GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1643GetKernelDispatchParametersForKeyIntrinsicsER32MPSNDArrayConvolutionDispatchKey37MPSNDArrayConvolutionDispatchDataType35MPSNDArrayConvolutionDispatchFormatP36MPSForwardDirectAutoTuningParameters
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorAMD22IsConvolutionSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorAMD24EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorAMD30DoWeightsNeedPhysicalTransposeEP10MPSNDArrayS1_P28NDArrayConvolutionEncodeData
+ __ZNK38MPSNDArrayConvolutionDeviceBehaviorAMD43EncodeNDArrayConvolutionGradientWithWeightsEPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob
+ __ZNK39MPSNDArrayConvolutionDeviceBehaviorA15X19GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_
+ __ZNK39MPSNDArrayConvolutionDeviceBehaviorA15X43GetKernelDispatchParametersForKeyIntrinsicsER32MPSNDArrayConvolutionDispatchKey37MPSNDArrayConvolutionDispatchDataType35MPSNDArrayConvolutionDispatchFormatP36MPSForwardDirectAutoTuningParameters
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1321IsDataFormatSupportedE33MPSNDArrayConvolution2DDataFormat
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1322IsConvolutionSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1323IsQuantizationSupportedEP28NDArrayConvolutionEncodeData
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1324EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP28NDArrayConvolutionEncodeData
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1324IsWeightsFormatSupportedE36MPSNDArrayConvolution2DWeightsFormat
+ __ZNK41MPSNDArrayConvolutionDeviceBehaviorPreG1333GetKernelDispatchParametersForKeyEP9MPSKernelR32MPSNDArrayConvolutionDispatchKey37MPSNDArrayConvolutionDispatchDataType35MPSNDArrayConvolutionDispatchFormatP42MPSForwardDirectPreG13AutoTuningParameters
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110shared_ptrI12MPSKernelDAGED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI12MPSKernelDAGED2B8ne200100Ev
+ __ZNSt3__110shared_ptrI16MPSKernelUserDAGED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED2B8ne200100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__113unordered_mapIjjNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjjEEEEED1B8ne200100Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__shared_ptr_pointerIP12MPSKernelDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP12MPSKernelDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP12MPSKernelDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP12MPSKernelDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIP16MPSKernelUserDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP16MPSKernelUserDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP16MPSKernelUserDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP16MPSKernelUserDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ __ZNSt3__16__treeINS_12__value_typeIPK10BaseTensorDv2_iEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
+ __ZNSt3__16vectorIP10BaseTensorNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIP14MPSDAGKernelOpNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE8__appendEm
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__19to_stringEf
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTISt11logic_error
+ __ZTISt12length_error
+ __ZTISt12out_of_range
+ __ZTISt20bad_array_new_length
+ __ZTISt9bad_alloc
+ __ZTISt9exception
+ __ZTSSt11logic_error
+ __ZTSSt12length_error
+ __ZTSSt12out_of_range
+ __ZTSSt20bad_array_new_length
+ __ZTSSt9bad_alloc
+ __ZTSSt9exception
+ __ZTV22MPSNDArrayFFTBehaviors
+ __ZTV23MPSNDArrayScanBehaviors
+ __ZTV25MPSNDArraySDPAA14Behavior
+ __ZTV26MPSNDArrayLUTGEMVBehaviors
+ __ZTV27MPSNDArrayIdentityBehaviors
+ __ZTV28MPSNDArrayReductionBehaviors
+ __ZTV28MPSNDArraySDPADeviceBehavior
+ __ZTV29MPSNDArrayLUTGEMVAMDBehaviors
+ __ZTV29MPSNDArraySortDeviceBehaviors
+ __ZTV30MPSNDArrayIdentityAMDBehaviors
+ __ZTV30MPSNDArrayMatMulDeviceBehavior
+ __ZTV31MPSNDArrayLUTGEMVAppleBehaviors
+ __ZTV32MPSNDArrayIdentityAppleBehaviors
+ __ZTV33MPSNDArrayMatMulA14DeviceBehavior
+ __ZTV35MPSNDArrayConvolutionDeviceBehavior
+ __ZTV36MPSNDArrayMatMulCommonDeviceBehavior
+ __ZTV37MPSNDArrayConvolution3DDeviceBehavior
+ __ZTV38MPSNDArrayConvolutionDeviceBehaviorA14
+ __ZTV38MPSNDArrayConvolutionDeviceBehaviorA16
+ __ZTV38MPSNDArrayConvolutionDeviceBehaviorAMD
+ __ZTV39MPSNDArrayConvolutionDeviceBehaviorA15X
+ __ZTV39MPSNDArrayConvolutionDeviceBehaviorCebu
+ __ZTV40MPSNDArrayConvolutionDeviceBehaviorAruba
+ __ZTV41MPSNDArrayConvolutionDeviceBehaviorPreG13
+ __ZTVNSt3__120__shared_ptr_pointerIP12MPSKernelDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP16MPSKernelUserDAGNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZZ25GetAxisIndexForDataFormat33MPSNDArrayConvolution2DDataFormatE4axis
+ __ZZ28GetAxisIndexForWeightsFormat36MPSNDArrayConvolution2DWeightsFormatE4axis
+ __ZZL19setParametersFromEVP30MPSNDArrayMatrixMultiplicationP9MPSDeviceE15setEVTileParams
+ __ZZL21validateQuantizedSDPAP10MPSNDArrayS0_S0_S0_S0_S0_S0_20MPSNDArraySDPALayoutENK3$_0clES0_S0_
+ __ZZL25GetAxisIndexForDataFormat33MPSNDArrayConvolution3DDataFormatE4axis
+ __ZZL28GetAxisIndexForWeightsFormat36MPSNDArrayConvolution3DWeightsFormatE4axis
+ __ZZL35EncodeQuantizedMatrixMultiplicationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE23quantizationSchemeNames
+ __ZZNK30MPSNDArrayMatMulDeviceBehavior21EncodeArrayMultiplyI4EPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoE5table
+ __ZZNK38MPSNDArrayConvolutionDeviceBehaviorAMD19GetKernelParametersEP9MPSKernelRK35MPSNDArrayConvolutionDispatchKeyAMDPvE25amdKernelParametersGetter
+ ___121-[MPSNDArrayIdentity reshapeWithCommandEncoder:commandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:]_block_invoke
+ ___45-[MPSNDArrayStitchedReduction getUserDAGInfo]_block_invoke
+ ___49-[MPSNDArrayStitchedReductionRMSNorm setEpsilon:]_block_invoke
+ ___58-[MPSNDArrayStitchedReductionSoftmax initWithDevice:axis:]_block_invoke
+ ___58-[MPSNDArrayStitchedReductionSoftmax initWithDevice:axis:]_block_invoke_2
+ ___58-[MPSNDArrayStitchedReductionSoftmax initWithDevice:axis:]_block_invoke_3
+ ___58-[MPSNDArrayStitchedReductionSoftmax initWithDevice:axis:]_block_invoke_4
+ ___66-[MPSNDArrayStitchedReductionRMSNorm initWithDevice:axis:epsilon:]_block_invoke
+ ___66-[MPSNDArrayStitchedReductionRMSNorm initWithDevice:axis:epsilon:]_block_invoke_2
+ ___66-[MPSNDArrayStitchedReductionRMSNorm initWithDevice:axis:epsilon:]_block_invoke_3
+ ___66-[MPSNDArrayStitchedReductionRMSNorm initWithDevice:axis:epsilon:]_block_invoke_4
+ ____ZL19setParametersFromEVP30MPSNDArrayMatrixMultiplicationP9MPSDevice_block_invoke
+ ____ZL21EncodeDecompositionLUPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo_block_invoke
+ ____ZL21EncodePoolingGradientPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob_block_invoke
+ ____ZL22forceDirectConvolutionv_block_invoke
+ ____ZL27GetValueForCommandBufferKeyPU27objcproto16MTLCommandBuffer11objc_objectPK8NSString_block_invoke
+ ____ZL28EncodeMatrixMultiplyQ4IntoQ8PKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo_block_invoke
+ ____ZL37EncodePoolingGradientMultiDestinationPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo_block_invoke
+ ____ZN9MPSDevice17IsShaderProfilingEv_block_invoke
+ ____ZNK29MPSNDArraySortDeviceBehaviors43EncodeSingleThreadgroupWaveMatchNDArraySortEP14MPSNDArraySortPU19objcproto9MTLDevice11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringmP14MPSNDArrayScanmbb_block_invoke
+ ____ZNK29MPSNDArraySortDeviceBehaviors45EncodeMultipleThreadgroupWaveMatchNDArraySortEP14MPSNDArraySortPU19objcproto9MTLDevice11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryP8NSStringmP14MPSNDArrayScanmbb_block_invoke
+ ____ZNK38MPSNDArrayConvolutionDeviceBehaviorA1419IsWinogradSupportedEP28NDArrayConvolutionEncodeData_block_invoke
+ ___block_descriptor_32_e21_v16?0"<MTLBuffer>"8l
+ ___block_descriptor_32_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_32_e39_v24?0^v8^{MPSKernelUserDAGNode=^^?}16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e69_v32?0^v8^{MPSKernelUserDAGNode=^^?}16^{MPSKernelUserDAGNode=^^?}24l
+ ___block_descriptor_32_e99_v40?0^v8^{MPSKernelUserDAGNode=^^?}16^{MPSKernelUserDAGNode=^^?}24^{MPSKernelUserDAGNode=^^?}32l
+ ___block_descriptor_36_e99_v40?0^v8^{MPSKernelUserDAGNode=^^?}16^{MPSKernelUserDAGNode=^^?}24^{MPSKernelUserDAGNode=^^?}32l
+ ___block_descriptor_40_e8_32o_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32o_e28_v16?0"<MTLCommandBuffer>"8ls32l8
+ ___block_descriptor_48_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o48o_e35_v24?0"MPSNDArray"8"MPSNDArray"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o40o_e75_v32?0"<MTLComputeCommandEncoder>"8"<MTLCommandBuffer>"16"<MTLBuffer>"24ls32l8s40l8
+ ___block_literal_global
+ ___block_literal_global.159
+ ___block_literal_global.19
+ ___block_literal_global.374
+ ___block_literal_global.38
+ ___block_literal_global.40
+ ___block_literal_global.43
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___clang_call_terminate
+ ___cxa_atexit
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addCompletedHandler:
+ _objc_msgSend$addObject:
+ _objc_msgSend$algorithm
+ _objc_msgSend$allValues
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowNegativeIndices
+ _objc_msgSend$alpha
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$arrayForCommandBuffer:arrayDescriptor:kernel:
+ _objc_msgSend$arrayViewWithCommandBuffer:descriptor:aliasing:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$axes
+ _objc_msgSend$axis
+ _objc_msgSend$batchDimensions
+ _objc_msgSend$beta
+ _objc_msgSend$buffer
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$columns
+ _objc_msgSend$commandQueue
+ _objc_msgSend$computeQ
+ _objc_msgSend$computeR
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$contents
+ _objc_msgSend$coordinateMode
+ _objc_msgSend$copy
+ _objc_msgSend$copyToGradientState:sourceArrays:sourceStates:destinationArray:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$copyWithZone:device:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$counterStride
+ _objc_msgSend$dataFormat
+ _objc_msgSend$dataLayout
+ _objc_msgSend$dataType
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeBytesForKey:returnedLength:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultAllocator
+ _objc_msgSend$denseSparse
+ _objc_msgSend$descending
+ _objc_msgSend$descriptor
+ _objc_msgSend$descriptorWithDataType:dimensionCount:dimensionSizes:
+ _objc_msgSend$descriptorWithDataType:shape:
+ _objc_msgSend$destinationArrayDescriptorForSourceArrays:sourceGradientIndex:
+ _objc_msgSend$destinationArrayDescriptorForSourceArrays:sourceState:
+ _objc_msgSend$destinationDataType
+ _objc_msgSend$destinationGradientArrayDescriptorsForSourceArrays:sourceGradient:sourceState:
+ _objc_msgSend$device
+ _objc_msgSend$deviceMemoryBytesRead
+ _objc_msgSend$deviceMemoryBytesWrite
+ _objc_msgSend$dictionary
+ _objc_msgSend$dilationHeight
+ _objc_msgSend$dilationRateInX
+ _objc_msgSend$dilationRateInY
+ _objc_msgSend$dilationRates
+ _objc_msgSend$dilationRatesForSourceIndex:
+ _objc_msgSend$dilationWidth
+ _objc_msgSend$dimensionsNotToBeBroadcast
+ _objc_msgSend$dispatchThreadgroups:threadsPerThreadgroup:
+ _objc_msgSend$edgeModeAtSourceIndex:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeBytes:length:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$encodeGradientsToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:
+ _objc_msgSend$encodeGradientsToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:kernelDAGObject:
+ _objc_msgSend$encodeGradientsToCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationGradients:kernelDAGObject:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeToCommandBuffer:computeEncoder:destinationBuffer:destinationOffset:numEntries:stride:
+ _objc_msgSend$encodeToCommandBuffer:destinationArray:
+ _objc_msgSend$encodeToCommandBuffer:encoder:leftMatrix:rightMatrix:resultMatrix:
+ _objc_msgSend$encodeToCommandBuffer:primarySourceArray:secondarySourceArray:destinationArray:
+ _objc_msgSend$encodeToCommandBuffer:sourceArray:sourceGradient:gradientState:destinationArray:
+ _objc_msgSend$encodeToCommandBuffer:sourceArrays:resultState:destinationArray:
+ _objc_msgSend$encodeToCommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:
+ _objc_msgSend$encodeToCommandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArray:
+ _objc_msgSend$encodeToCommandEncoder:commandBuffer:sourceArrays:destinationArrays:
+ _objc_msgSend$encodeToCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeToCommandEncoder:commandBuffer:sourceMatrix:resultMatrix:pivotIndices:status:
+ _objc_msgSend$encodeToCommandEncoder:commandBuffer:sourceMatrix:rightHandSideMatrix:pivotIndices:solutionMatrix:
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArray:
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArrays:
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:destinationArrays:activeDestinationMask:
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:
+ _objc_msgSend$encodeWithCoder:
+ _objc_msgSend$endEncoding
+ _objc_msgSend$epsilon
+ _objc_msgSend$exclusive
+ _objc_msgSend$finalOp
+ _objc_msgSend$firstGradientDestinationFromDestinationGradients:outMaxNumDimensions:
+ _objc_msgSend$float16Ops
+ _objc_msgSend$float32Ops
+ _objc_msgSend$floatValue
+ _objc_msgSend$getDQuantMinValIndex
+ _objc_msgSend$getDQuantMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$getDQuantScaleIndex
+ _objc_msgSend$getDQuantScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$getDestContiguousFunctionConstant:
+ _objc_msgSend$getLUTIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$getLeftDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getLeftDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getLeftMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getLeftScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getLeftZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getMTLStitchingGraph
+ _objc_msgSend$getMinValIndex
+ _objc_msgSend$getMinValIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$getNDArrayCount
+ _objc_msgSend$getObjects:range:
+ _objc_msgSend$getRightDQuantMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getRightDQuantScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getRightMinValIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getRightScaleIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getRightZeroPointIndexWithLeftAffineQuantizationDescriptor:rightQuantizationDescriptor:
+ _objc_msgSend$getScaleIndex
+ _objc_msgSend$getScaleIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$getShape
+ _objc_msgSend$getShapeVector
+ _objc_msgSend$getUserDAGInfo
+ _objc_msgSend$getVisibleFunctions
+ _objc_msgSend$getZeroPointIndex
+ _objc_msgSend$getZeroPointIndexWithLeftQuantizationDescriptor:rightQuantizationDescriptor:isForLeft:
+ _objc_msgSend$gpuAddress
+ _objc_msgSend$graph
+ _objc_msgSend$groups
+ _objc_msgSend$hasDoubleQuantMinVal
+ _objc_msgSend$hasDoubleQuantScale
+ _objc_msgSend$hasMinValue
+ _objc_msgSend$hasScale
+ _objc_msgSend$hasZeroPoint
+ _objc_msgSend$height
+ _objc_msgSend$implicitZeroPoint
+ _objc_msgSend$incrementKey
+ _objc_msgSend$init
+ _objc_msgSend$initPhiloxStateDescriptorWithCounterLow:counterHigh:key:
+ _objc_msgSend$initPhiloxStateDescriptorWithSeed:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithBuffer:descriptor:
+ _objc_msgSend$initWithBuffer:offset:descriptor:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCoder:device:
+ _objc_msgSend$initWithCommandBuffer:withDispatchType:
+ _objc_msgSend$initWithComputeCommandEncoder:
+ _objc_msgSend$initWithDataType:dimensions:sizes:
+ _objc_msgSend$initWithDataType:quantizationScheme:
+ _objc_msgSend$initWithDataType:vectorAxes:
+ _objc_msgSend$initWithDevice:
+ _objc_msgSend$initWithDevice:K:computeGradient:
+ _objc_msgSend$initWithDevice:axis:
+ _objc_msgSend$initWithDevice:axis:descending:
+ _objc_msgSend$initWithDevice:axis:epsilon:
+ _objc_msgSend$initWithDevice:axis:operation:
+ _objc_msgSend$initWithDevice:axis:operation:exclusive:reverse:
+ _objc_msgSend$initWithDevice:constantValue:
+ _objc_msgSend$initWithDevice:descriptor:
+ _objc_msgSend$initWithDevice:destinationDataType:seed:distributionDescriptor:
+ _objc_msgSend$initWithDevice:kernelSizes:poolingMode:
+ _objc_msgSend$initWithDevice:kernelSizes:poolingMode:computeGradient:
+ _objc_msgSend$initWithDevice:kernelType:
+ _objc_msgSend$initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:
+ _objc_msgSend$initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:kernelType:sourceCount:
+ _objc_msgSend$initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:lhsDesc:rhsDesc:
+ _objc_msgSend$initWithDevice:mean:standardDeviation:
+ _objc_msgSend$initWithDevice:mean:standardDeviation:seed:
+ _objc_msgSend$initWithDevice:minimum:maximum:
+ _objc_msgSend$initWithDevice:minimum:maximum:seed:
+ _objc_msgSend$initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:ndArrayConvolution2DDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:quantizationDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:rows:columns:
+ _objc_msgSend$initWithDevice:seed:
+ _objc_msgSend$initWithDevice:transpose:order:numberOfRightHandSides:
+ _objc_msgSend$initWithDevice:transposeLeft:transposeRight:resultRows:resultColumns:interiorColumns:alpha:beta:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithFunctionName:
+ _objc_msgSend$initWithKernelDAG:finalOp:
+ _objc_msgSend$initWithKernelUserDAG:
+ _objc_msgSend$initWithMTLStitchingGraphs:visibleFunctions:stitchedFunctions:
+ _objc_msgSend$initWithResource:
+ _objc_msgSend$initWithSourceCount:
+ _objc_msgSend$initWithStateSize:invariantValueFn:mapFn:reduceFn:writeFn:
+ _objc_msgSend$inputTensorAtIndex:
+ _objc_msgSend$invariantValueFn
+ _objc_msgSend$isDestinationActiveAtIndex:
+ _objc_msgSend$isLeftFused
+ _objc_msgSend$kernelDAGObjectSetup:sourceArrays:sourceGradient:destination:
+ _objc_msgSend$kernelDimensionalityForDestinationArray:
+ _objc_msgSend$kernelDimensionalityForSourceArrays:
+ _objc_msgSend$kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:
+ _objc_msgSend$kernelHeight
+ _objc_msgSend$kernelOffsets
+ _objc_msgSend$kernelSizesForSourceIndex:
+ _objc_msgSend$kernelType
+ _objc_msgSend$kernelWidth
+ _objc_msgSend$label
+ _objc_msgSend$layout
+ _objc_msgSend$length
+ _objc_msgSend$lengthOfDimension:
+ _objc_msgSend$mapFn
+ _objc_msgSend$matrixDescriptorWithRows:columns:matrices:rowBytes:matrixBytes:dataType:
+ _objc_msgSend$matrixDescriptorWithRows:columns:rowBytes:dataType:
+ _objc_msgSend$maxComputeThreadgroupMemory
+ _objc_msgSend$maxSupportedArraySizeForIsDestination:
+ _objc_msgSend$maxSupportedDimensionsForSourceArrays:destinationArray:
+ _objc_msgSend$maxThreadgroupMemoryLength
+ _objc_msgSend$maxTotalThreadsPerThreadgroup
+ _objc_msgSend$maximum
+ _objc_msgSend$maximumInteger
+ _objc_msgSend$mean
+ _objc_msgSend$minimum
+ _objc_msgSend$minimumInteger
+ _objc_msgSend$multiples
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$newBufferWithLength:options:
+ _objc_msgSend$normFusionType
+ _objc_msgSend$normalDistributionDescriptorWithMean:standardDeviation:
+ _objc_msgSend$normalDistributionDescriptorWithMean:standardDeviation:minimum:maximum:
+ _objc_msgSend$normalizeCoordinates
+ _objc_msgSend$null
+ _objc_msgSend$numLower
+ _objc_msgSend$numUpper
+ _objc_msgSend$numberOfDimensions
+ _objc_msgSend$numberOfInputTensors
+ _objc_msgSend$numberOfOutputTensors
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$offset
+ _objc_msgSend$offsets
+ _objc_msgSend$offsetsAtSourceIndex:
+ _objc_msgSend$operation
+ _objc_msgSend$outputTensorAtIndex:
+ _objc_msgSend$paddingBottom
+ _objc_msgSend$paddingLeft
+ _objc_msgSend$paddingRight
+ _objc_msgSend$paddingTop
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$popDebugGroup
+ _objc_msgSend$pushDebugGroup:
+ _objc_msgSend$quantizationDataType
+ _objc_msgSend$quantizationScheme
+ _objc_msgSend$readCount
+ _objc_msgSend$reduceFn
+ _objc_msgSend$reinitializeDistributionDescriptor:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resampleMode
+ _objc_msgSend$reshapeWithCommandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:
+ _objc_msgSend$reshapeWithCommandEncoder:commandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:
+ _objc_msgSend$reshapeWithCommandEncoder:commandBuffer:sourceArray:shape:destinationArray:
+ _objc_msgSend$reshapeWithDimensionCount:dimensionSizes:
+ _objc_msgSend$resizeHeight
+ _objc_msgSend$resizeWidth
+ _objc_msgSend$resourceSize
+ _objc_msgSend$resultStateForSourceArrays:sourceStates:destinationArray:
+ _objc_msgSend$reverse
+ _objc_msgSend$rowBytes
+ _objc_msgSend$rows
+ _objc_msgSend$safeArrayViewWithCommandBuffer:computeEncoder:descriptor:aliasing:
+ _objc_msgSend$safeArrayViewWithCommandBuffer:descriptor:aliasing:
+ _objc_msgSend$samplingMethod
+ _objc_msgSend$samplingMode
+ _objc_msgSend$setAlpha:
+ _objc_msgSend$setAutoTuningParameters:
+ _objc_msgSend$setAutoTuningTarget:
+ _objc_msgSend$setAxes:
+ _objc_msgSend$setAxis:
+ _objc_msgSend$setBatchDimensions:
+ _objc_msgSend$setBeta:
+ _objc_msgSend$setBuffer:offset:atIndex:
+ _objc_msgSend$setBytes:length:atIndex:
+ _objc_msgSend$setColumns:
+ _objc_msgSend$setComputePipelineState:
+ _objc_msgSend$setConstantValue:type:atIndex:
+ _objc_msgSend$setCopyBlock:
+ _objc_msgSend$setDestinationArrayAllocator:
+ _objc_msgSend$setDeviceMemoryBytesRead:
+ _objc_msgSend$setDeviceMemoryBytesWrite:
+ _objc_msgSend$setDynamicFCs:
+ _objc_msgSend$setEpsilon:
+ _objc_msgSend$setFloat16Ops:
+ _objc_msgSend$setFloat32Ops:
+ _objc_msgSend$setIndexingArithmaticTypeMask:sourceArrays:sourceGradient:destination:tileDimensions:
+ _objc_msgSend$setK:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLengthOfDimension:atIndex:
+ _objc_msgSend$setM:
+ _objc_msgSend$setN:
+ _objc_msgSend$setNumberOfRightHandSides:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setOrder:
+ _objc_msgSend$setPreferPackedRows:
+ _objc_msgSend$setReadCount:
+ _objc_msgSend$setRows:
+ _objc_msgSend$setTexture:atIndex:
+ _objc_msgSend$setTextures:withRange:
+ _objc_msgSend$setThreadgroupMemoryLength:atIndex:
+ _objc_msgSend$setTransA:
+ _objc_msgSend$setTransB:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setWorkspace:
+ _objc_msgSend$setWriteFn:
+ _objc_msgSend$skipElements
+ _objc_msgSend$sliceDimension:withSubrange:
+ _objc_msgSend$sliceRangeForDimension:
+ _objc_msgSend$sparseFormat
+ _objc_msgSend$spatialScale
+ _objc_msgSend$specializedName
+ _objc_msgSend$standardDeviation
+ _objc_msgSend$state
+ _objc_msgSend$stateLength
+ _objc_msgSend$stateSize
+ _objc_msgSend$strideHeight
+ _objc_msgSend$strideInPixels
+ _objc_msgSend$strideInPixelsX
+ _objc_msgSend$strideInPixelsY
+ _objc_msgSend$strideWidth
+ _objc_msgSend$stridesAtSourceIndex:
+ _objc_msgSend$stridesForSourceIndex:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$structuredSparse
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$supportsGradientForSourceIndex:
+ _objc_msgSend$supportsPostfixForDevice:
+ _objc_msgSend$supportsPrefixForDevice:
+ _objc_msgSend$temporaryNDArrayWithCommandBuffer:descriptor:
+ _objc_msgSend$temporaryResultStateForCommandBuffer:sourceArrays:sourceStates:destinationArray:
+ _objc_msgSend$threadExecutionWidth
+ _objc_msgSend$transposeDimension:withDimension:
+ _objc_msgSend$transposeSparse
+ _objc_msgSend$trsmKernel
+ _objc_msgSend$trsmL
+ _objc_msgSend$trsmU
+ _objc_msgSend$uniformDistributionDescriptorWithMinimum:maximum:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updateStrides
+ _objc_msgSend$userDictionary
+ _objc_msgSend$usesVectorFunctionsOnOutput:
+ _objc_msgSend$vectorAxes
+ _objc_msgSend$weightsFormat
+ _objc_msgSend$width
+ _objc_msgSend$workloadStatisticsForSourceArrays:destArrays:sourceState:
+ _objc_msgSend$workspace
+ _objc_msgSend$writeBytes:strideBytes:
+ _objc_msgSend$writeFn
+ _puts
- __Znwm
CStrings:
+ " -kernelType 0 -packed 3"
+ " -layout "
+ "\" Single threadgroup can only sort %u elements (is %u)"
+ "-alpha "
+ "-dataQuantizationScheme "
+ "-weightsQuantizationScheme "
+ "A14 Encoder: Encoding 8x8 TEC based QuantizedSDPA kernel\n"
+ "A14 Encoder: Encoding 8x8 TEC based SDPA kernel\n"
+ "A14 Encoder: Encoding failed, fall back to vector based QuantizedSDPA kernel\n"
+ "Default Encoder: Encoding vector based SDPA\n"
+ "Encoding vector based QuantizedSDPA kernel\n"
+ "MPSNDArrayQuantizationTypeAffine"
+ "MPSNDArrayQuantizationTypeNone"
+ "MPSNDArrayQuantizedConv2DTest"
+ "MPSNDArrayQuantizedScaledDotProductAttentionTest"
+ "MPSNDArrayScaledDotProductAttentionTest"
+ "Quantized tensor should be in int8"
+ "QuantizedSDPA: Q is not quantized, Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask Datatype: %s, KScale Datatype: %s, VScale Datatype: %s, Dest Datatype: %s\t"
+ "QuantizedSDPA: Q is quantized, Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask Datatype: %s, QScale Datatype: %s, KScale Datatype: %s, VScale Datatype: %s, Dest Datatype: %s\t"
+ "QuantizedSDPA: f16Ops=%f, f32Ops=%f, BytesRead=%f, BytesWritten=%f, OpsPerByte=%f\n"
+ "QuantizedSDPA: kernel %s is encoded, threadsPerGroup: (%lu, %lu, %lu), threadGroups: (%lu, %lu, %lu)\n"
+ "SDPA: Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask Datatype: %s, Dest Datatype: %s\t"
+ "SDPA: f16Ops=%f, f32Ops=%f, BytesRead=%f, BytesWritten=%f, OpsPerByte=%f\n"
+ "SDPA: kernel %s is encoded, threadsPerGroup: (%lu, %lu, %lu), threadGroups: (%lu, %lu, %lu)\n"
+ "Scale tensor should be in fp16 or fp32"
+ "Sort requires 64bits index array data type"
+ "Source tensor data type should be fp16 or fp32 when is it not quantized"
+ "UTF8String"
+ "Using EncodeQuantizedMatrixMultiplicationInt2Int8Affine encode path\n"
+ "[Q4Q8] MatMul Paramters: TileK: %d, TileM: %d, TileN: %d simdM: %d simdN: %d kSplits: %d\n"
+ "[Q4Q8] No A matrix scales found."
+ "[Q4Q8] No B matrix scales found."
+ "[Q4Q8] Only AxB^T supported."
+ "[Q4Q8] Only batch size of 1 supported."
+ "[Q4Q8] TG Tile size clamped between 32 and 256\n"
+ "[Q4Q8] Warning: MPS_MATMUL_KSPLITS, MPS_MATMUL_SIMDM, MPS_MATMUL_SIMDN not currently supported.\n"
+ "[Q4Q8] tileK cannot be smaller than the blocksize."
+ "_allowFP16WinogradTransformIntermediate"
+ "batch size in the scale array should equal to 1 or match the quantized array"
+ "could not find index %lu in the placeholder list"
+ "destination must be float16 or float32"
+ "feature length in the scale array should be 1"
+ "maxThreadgroupMemoryLength"
+ "number of heads in the scale array should equal to 1 or match the quantized array"
+ "number of tokens in the scale array should equal to 1 or match the quantized array"
+ "per_tensor_quantized_sdpa_tile_fwd_16x16x16_doEdgeCheck"
+ "per_tensor_quantized_sdpa_tile_fwd_16x16x16_noEdgeCheck"
+ "per_tensor_quantized_sdpa_tile_fwd_8x8x8_doEdgeCheck"
+ "per_tensor_quantized_sdpa_tile_fwd_8x8x8_noEdgeCheck"
+ "q4q8_gemm"
+ "quantized_sdpa_fwdNew"
+ "quantized_sdpa_tile_fwd_16x16x16_doEdgeCheck"
+ "quantized_sdpa_tile_fwd_16x16x16_noEdgeCheck"
+ "quantized_sdpa_tile_fwd_8x8x8_doEdgeCheck"
+ "quantized_sdpa_tile_fwd_8x8x8_noEdgeCheck"
+ "sdpa_tile_fwd_16x16x16_doEdgeCheck"
+ "sdpa_tile_fwd_16x16x16_noEdgeCheck"
+ "sdpa_tile_fwd_8x8x8_doEdgeCheck"
+ "sdpa_tile_fwd_8x8x8_noEdgeCheck"
+ "too much threadgroup memory usage %lu bytes is over the limit: %lu"
+ "too much threadgroup memory usage. Fallback"
+ "v16@?0@\"<MTLBuffer>\"8"
+ "wavematch_multiple_threadgroup_copy"
+ "wavematch_multiple_threadgroup_histogram"
+ "wavematch_multiple_threadgroup_scatter"
+ "wavematch_single_threadgroup"
- "MPS_MATMUL_KSPLITS"
- "MPS_MATMUL_SIMDM"
- "MPS_MATMUL_SIMDN"
- "NDArrayQ4IntoQ8"
- "WARNING: Tile size fixed to 64x32x64 and currently does not support all powers of 2.\n"
- "sdpa_tile_fwd"

```
