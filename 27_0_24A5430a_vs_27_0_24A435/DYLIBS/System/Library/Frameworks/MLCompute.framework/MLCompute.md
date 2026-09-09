## MLCompute

> `/System/Library/Frameworks/MLCompute.framework/MLCompute`

```diff

 87.0.0.0.0
-  __TEXT.__text: 0x112e84
+  __TEXT.__text: 0x112ef0
   __TEXT.__objc_methlist: 0xaf14
   __TEXT.__const: 0x5b0
   __TEXT.__oslogstring: 0x8ece

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4281
+  Functions: 4282
   Symbols:   7872
   CStrings:  1384
 
Functions:
+ _OUTLINED_FUNCTION_1
~ -[MLCDeviceGPU allocateDeviceHeapForGraph:forInference:] : 3660 -> 3656
~ -[MLCDeviceCPU(MLCLayerOperations) embeddingWeightsGradients:embeddingCount:embeddingDimension:] : 508 -> 512
~ -[MLCDeviceGPU(MLCEngineDispatch) dispatchGradientInstanceNormalizationKernel:sourceGradientTensor:resultGradientTensor:deviceIndex:] : 2312 -> 2300
~ -[MLCDeviceGPU(MLCEngineDispatch) dispatchForwardAndGradientLossLayer:sourceTensor:labelsTensor:labelsTensorStride:weightsTensor:resultTensor:resultGradientTensor:] : 3648 -> 3712
~ -[MLCDeviceCPU(MLCEngineDispatch) dispatchForwardEmbeddingLayer:weight:sourceTensor:resultTensor:] : 1424 -> 1444
~ -[MLCDeviceCPU(MLCEngineDispatch) dispatchGradientEmbeddingLayer:sourceGradientTensor:] : 804 -> 808
~ _saveOrRestoreLSTMWeightsAndAccumulatorsHelper : 36 -> 40
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateRNNLayer:optimizer:inputWeightsParameter:hiddenWeightsParameter:biasesParameter:arrayOfParams:] : 2400 -> 2396
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateEmbeddingLayer:weightsParameter:optimizer:arrayOfParams:] : 1208 -> 1216
~ -[MLCGraph nodeWithMultiOutputLayer:source:forTraining:] : 2028 -> 2040
~ _ANE_CreateSliceLayer.cold.1 : 72 -> 76
~ _ANE_CreateSliceLayer.cold.2 : 72 -> 76
~ _ANE_CreateSliceLayer.cold.3 : 100 -> 88
~ _ANE_CompileSliceLayer.cold.1 : 92 -> 96
~ _ANE_CompileSliceLayer.cold.2 : 80 -> 68
```
