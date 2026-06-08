## libswiftMLCompute.dylib

> `/usr/lib/swift/libswiftMLCompute.dylib`

```diff

-84.0.0.0.0
-  __TEXT.__text: 0x48ec
-  __TEXT.__auth_stubs: 0x3c0
+87.0.0.0.0
+  __TEXT.__text: 0x4d5c
   __TEXT.__const: 0x10c
   __TEXT.__cstring: 0x15a
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift_as_cont: 0x30
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__eh_frame: 0x140
-  __TEXT.__objc_methname: 0x825
-  __TEXT.__objc_methtype: 0x23
-  __TEXT.__objc_stubs: 0x740
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__eh_frame: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d0
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__auth_got: 0x228
   __DATA.__data: 0x30
   __DATA.__common: 0x1
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 61002F81-06AA-362A-8024-CD3D61566AA0
-  Functions: 115
-  Symbols:   389
-  CStrings:  66
+  UUID: BE1643C0-3E96-3D19-B4BD-79A9120D2EC7
+  Functions: 124
+  Symbols:   425
+  CStrings:  7
 
Symbols:
+ _$sScA15unownedExecutorScevgTj
+ _$sSo16MLCTrainingGraphC9MLComputeE14executeForward9batchSize7options11outputsDataSo9MLCTensorCSg6result_Sd13executionTimetSi_So19MLCExecutionOptionsVSDySSSo0kJ0CGSgtYaKFTY2_
+ _$sSo16MLCTrainingGraphC9MLComputeE14executeForward9batchSize7options11outputsDataSo9MLCTensorCSg6result_Sd13executionTimetSi_So19MLCExecutionOptionsVSDySSSo0kJ0CGSgtYaKFTY3_
+ _$sSo16MLCTrainingGraphC9MLComputeE15executeGradient9batchSize7options11outputsDataSdSi_So19MLCExecutionOptionsVSDySSSo09MLCTensorJ0CGSgtYaKFTY2_
+ _$sSo16MLCTrainingGraphC9MLComputeE15executeGradient9batchSize7options11outputsDataSdSi_So19MLCExecutionOptionsVSDySSSo09MLCTensorJ0CGSgtYaKFTY3_
+ _$sSo16MLCTrainingGraphC9MLComputeE22executeOptimizerUpdate7optionsSdSo19MLCExecutionOptionsV_tYaKFTY2_
+ _$sSo16MLCTrainingGraphC9MLComputeE22executeOptimizerUpdate7optionsSdSo19MLCExecutionOptionsV_tYaKFTY3_
+ _$sSo17MLCInferenceGraphC9MLComputeE7execute10inputsData010lossLabelsF00g12LabelWeightsF007outputsF09batchSize7optionsSo9MLCTensorCSg6result_Sd13executionTimetSDySSSo0oF0CG_ARSgA2SSiSo19MLCExecutionOptionsVtYaKFTY2_
+ _$sSo17MLCInferenceGraphC9MLComputeE7execute10inputsData010lossLabelsF00g12LabelWeightsF007outputsF09batchSize7optionsSo9MLCTensorCSg6result_Sd13executionTimetSDySSSo0oF0CG_ARSgA2SSiSo19MLCExecutionOptionsVtYaKFTY3_
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.3
+ __swift_implicitisolationactor_to_executor_cast
+ _objc_release_x28
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
- _objc_release_x26
- _objc_retain_x20
- _swift_retain
CStrings:
- "averagePoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:countIncludesPadding:"
- "batchSizePerSequenceStep"
- "countIncludesPadding"
- "descriptorWithEmbeddingCount:embeddingDimension:"
- "descriptorWithEmbeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:"
- "descriptorWithShape:dataType:"
- "descriptorWithShape:sequenceLengths:sortedSequences:dataType:"
- "descriptorWithType:kernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:"
- "dilationRateInX"
- "dilationRateInY"
- "dimensions"
- "embeddingCount"
- "embeddingDimension"
- "end"
- "executeForwardWithBatchSize:options:outputsData:completionHandler:"
- "executeGradientWithBatchSize:options:outputsData:completionHandler:"
- "executeOptimizerUpdateWithOptions:completionHandler:"
- "executeWithInputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:completionHandler:"
- "kernelHeight"
- "kernelWidth"
- "l2NormPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:"
- "layerWithConstantPadding:constantValue:"
- "layerWithDimensions:"
- "layerWithNormalizedShape:beta:gamma:varianceEpsilon:"
- "layerWithReductionType:dimensions:"
- "layerWithReflectionPadding:"
- "layerWithShape:"
- "layerWithShape:sampleMode:alignsCorners:"
- "layerWithSplitSectionLengths:dimension:"
- "layerWithSymmetricPadding:"
- "layerWithZeroPadding:"
- "maxPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:"
- "maximumNorm"
- "normalizedShape"
- "pNorm"
- "paddingIndex"
- "paddingPolicy"
- "paddingSizeInX"
- "paddingSizeInY"
- "poolingType"
- "reshapeWithShape:source:"
- "sequenceLengths"
- "shape"
- "sliceLayerWithStart:end:stride:"
- "splitSectionLengths"
- "splitWithSource:splitSectionLengths:dimension:"
- "start"
- "stride"
- "strideInX"
- "strideInY"
- "tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:data:"
- "tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:"
- "tensorWithShape:"
- "tensorWithShape:data:dataType:"
- "tensorWithShape:dataType:"
- "tensorWithShape:fillWithData:dataType:"
- "tensorWithShape:randomInitializerType:"
- "transposeWithDimensions:source:"
- "v32@?0@\"MLCTensor\"8@\"NSError\"16d24"

```
