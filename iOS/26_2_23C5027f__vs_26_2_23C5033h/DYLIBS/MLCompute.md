## MLCompute

> `/System/Library/Frameworks/MLCompute.framework/MLCompute`

```diff

 84.0.0.0.0
-  __TEXT.__text: 0x11bbf8
+  __TEXT.__text: 0x11bcf8
   __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_methlist: 0xaefc
   __TEXT.__const: 0x5a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98D0105B-45E6-32A2-ACD7-DE3E67FE41F4
+  UUID: 1D8C93B7-C1B2-3D1B-B6A8-E4F1B777A1B4
   Functions: 4220
   Symbols:   13842
   CStrings:  6460
Functions:
~ -[MLCTensorDescriptor initTensorWithShape:stride:sequenceLengths:sortedSequences:fanIn:fanOut:dataType:] : 2164 -> 2184
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateBatchNormalizationLayer:optimizer:betaParameter:gammaParameter:meanTensor:varianceTensor:arrayOfParams:] : 1084 -> 1104
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateFullyConnectedLayer:optimizer:weightsParameter:biasesParameter:arrayOfParams:] : 984 -> 1004
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) optimizerStepForSingleParameterLSTM:tensorParameters:parameterForGateDesc:gradientsForGateDesc:parameterMomentumDescData:gateIndex:deviceOptimizers:isStackedInputWeight:] : 1268 -> 1288
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateRNNLayer:optimizer:inputWeightsParameter:hiddenWeightsParameter:biasesParameter:arrayOfParams:] : 2328 -> 2388
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateMultiheadAttentionLayer:optimizer:weightsParameter:biasesParameter:arrayOfParams:] : 2392 -> 2448
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateEmbeddingLayer:weightsParameter:optimizer:arrayOfParams:] : 1184 -> 1204
~ -[MLCDeviceCPU(MLComputeEngineOptimizerUpdate) updateTensorParameter:optimizer:gradient:arrayOfParams:] : 872 -> 892
~ -[MLCTensor dataContainsScalarWhere:] : 480 -> 500

```
