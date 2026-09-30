## libswiftMLCompute.dylib

> `/usr/lib/swift/libswiftMLCompute.dylib`

```diff

 84.0.0.0.0
-  __TEXT.__text: 0x4100
-  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__text: 0x48ec
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__const: 0x10c
-  __TEXT.__cstring: 0x18a
+  __TEXT.__cstring: 0x15a
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift_as_entry: 0x10

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x188
   __TEXT.__eh_frame: 0x140
   __TEXT.__objc_methname: 0x825
+  __TEXT.__objc_methtype: 0x23
+  __TEXT.__objc_stubs: 0x740
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d0
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x260
   __DATA.__data: 0x30
   __DATA.__common: 0x1

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 476B0B0D-0DF5-3632-8EC5-64B56E0F422E
-  Functions: 124
-  Symbols:   354
+  UUID: 5111061B-999C-353F-9F1B-CC673729843D
+  Functions: 115
+  Symbols:   389
   CStrings:  66
 
Symbols:
+ _objc_msgSend$averagePoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:countIncludesPadding:
+ _objc_msgSend$batchSizePerSequenceStep
+ _objc_msgSend$countIncludesPadding
+ _objc_msgSend$descriptorWithEmbeddingCount:embeddingDimension:
+ _objc_msgSend$descriptorWithEmbeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:
+ _objc_msgSend$descriptorWithShape:dataType:
+ _objc_msgSend$descriptorWithShape:sequenceLengths:sortedSequences:dataType:
+ _objc_msgSend$descriptorWithType:kernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:
+ _objc_msgSend$dilationRateInX
+ _objc_msgSend$dilationRateInY
+ _objc_msgSend$dimensions
+ _objc_msgSend$embeddingCount
+ _objc_msgSend$embeddingDimension
+ _objc_msgSend$end
+ _objc_msgSend$executeForwardWithBatchSize:options:outputsData:completionHandler:
+ _objc_msgSend$executeGradientWithBatchSize:options:outputsData:completionHandler:
+ _objc_msgSend$executeOptimizerUpdateWithOptions:completionHandler:
+ _objc_msgSend$executeWithInputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:completionHandler:
+ _objc_msgSend$kernelHeight
+ _objc_msgSend$kernelWidth
+ _objc_msgSend$l2NormPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:
+ _objc_msgSend$layerWithConstantPadding:constantValue:
+ _objc_msgSend$layerWithDimensions:
+ _objc_msgSend$layerWithNormalizedShape:beta:gamma:varianceEpsilon:
+ _objc_msgSend$layerWithReductionType:dimensions:
+ _objc_msgSend$layerWithReflectionPadding:
+ _objc_msgSend$layerWithShape:
+ _objc_msgSend$layerWithShape:sampleMode:alignsCorners:
+ _objc_msgSend$layerWithSplitSectionLengths:dimension:
+ _objc_msgSend$layerWithSymmetricPadding:
+ _objc_msgSend$layerWithZeroPadding:
+ _objc_msgSend$maxPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:
+ _objc_msgSend$maximumNorm
+ _objc_msgSend$normalizedShape
+ _objc_msgSend$pNorm
+ _objc_msgSend$paddingIndex
+ _objc_msgSend$paddingPolicy
+ _objc_msgSend$paddingSizeInX
+ _objc_msgSend$paddingSizeInY
+ _objc_msgSend$poolingType
+ _objc_msgSend$reshapeWithShape:source:
+ _objc_msgSend$sequenceLengths
+ _objc_msgSend$shape
+ _objc_msgSend$sliceLayerWithStart:end:stride:
+ _objc_msgSend$splitSectionLengths
+ _objc_msgSend$splitWithSource:splitSectionLengths:dimension:
+ _objc_msgSend$start
+ _objc_msgSend$stride
+ _objc_msgSend$strideInX
+ _objc_msgSend$strideInY
+ _objc_msgSend$tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:data:
+ _objc_msgSend$tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:
+ _objc_msgSend$tensorWithShape:
+ _objc_msgSend$tensorWithShape:data:dataType:
+ _objc_msgSend$tensorWithShape:dataType:
+ _objc_msgSend$tensorWithShape:fillWithData:dataType:
+ _objc_msgSend$tensorWithShape:randomInitializerType:
+ _objc_msgSend$transposeWithDimensions:source:
- _$sSo13MLCSliceLayerC9MLComputeE5startSaySiGvgTm
- _$sSo15MLCPaddingLayerC9MLComputeE17reflectionPaddingABSaySiG_tcfCTm
- _$sSo19MLCTensorDescriptorC9MLComputeE15sequenceLengthsSaySiGSgvgTm
- _$sSo19MLCTensorDescriptorC9MLComputeE5shapeSaySiGvgTm
- _$sSo20MLCPoolingDescriptorC9MLComputeE11kernelSizesSi6height_Si5widthtvgTm
- _$sSo22MLCEmbeddingDescriptorC9MLComputeE11maximumNormSfSgvgTm
- _$sSo22MLCEmbeddingDescriptorC9MLComputeE14embeddingCountSivgTm
- _$sSo24MLCConvolutionDescriptorC9MLComputeE11kernelSizesSi6height_Si5widthtvgTm
- _$sSo8MLCGraphC9MLComputeE7reshape5shape6sourceSo9MLCTensorCSgSaySiG_AHtFTm
- _$sSo9MLCTensorC9MLComputeE5shape21randomInitializerTypeABSaySiG_So09MLCRandomeF0VtcfCTm
- _$sSo9MLCTensorC9MLComputeE5shape4data0D4TypeABSaySiG_So0A4DataCSo07MLCDataE0VtcfCTm
- _objc_release_x28

```
