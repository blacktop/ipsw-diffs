## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-130.1.3.0.0
-  __TEXT.__text: 0x1122ec
+130.1.4.0.0
+  __TEXT.__text: 0x112f14
   __TEXT.__objc_methlist: 0x7274
   __TEXT.__const: 0x9c9b0
   __TEXT.__gcc_except_tab: 0x4f24
Functions:
~ -[MPSNDArrayLinearAttention buildParamsForQueries:keys:values:decayGates:betaValues:initialState:outputState:output:g_exp:shapes:] : 2516 -> 4632
~ -[MPSNDArrayLinearAttention dispatchExponentiationWithEncoder:decayGates:expGatesPso:shapes:] : 196 -> 468
~ -[MPSNDArrayLinearAttention dispatchChunkParallelWithEncoder:commandBuffer:params:A_chunks:B_chunks:initialState:S_state:shapes:laHash:] : 2300 -> 2336
~ -[MPSNDArrayLinearAttention encodeImpl:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2876 -> 3564
```
