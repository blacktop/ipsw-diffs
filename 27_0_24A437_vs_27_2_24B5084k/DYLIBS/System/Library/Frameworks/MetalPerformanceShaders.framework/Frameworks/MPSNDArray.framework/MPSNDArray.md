## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-130.0.19.0.0
-  __TEXT.__text: 0x111fc8
+130.1.1.0.0
+  __TEXT.__text: 0x111e48
   __TEXT.__objc_methlist: 0x7274
   __TEXT.__const: 0x9c9b0
   __TEXT.__gcc_except_tab: 0x4ed8
-  __TEXT.__cstring: 0x126c1
+  __TEXT.__cstring: 0x125b3
   __TEXT.__oslogstring: 0x27
   __TEXT.__unwind_info: 0x1f80
   __TEXT.__eh_frame: 0xb8

   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x350
   __AUTH_CONST.__const: 0x4800
-  __AUTH_CONST.__cfstring: 0x9520
+  __AUTH_CONST.__cfstring: 0x94e0
   __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x5b0

   - /usr/lib/libobjc.A.dylib
   Functions: 2477
   Symbols:   5554
-  CStrings:  1718
+  CStrings:  1716
 
Functions:
~ __ZL36EncodeConstantInitializationInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob : 1764 -> 1712
~ -[MPSNDArrayLinearAttention extractShapesFromQueries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2728 -> 2880
~ __ZL18validateArrayShapeP10MPSNDArrayP8NSStringSt16initializer_listImE : 284 -> 328
~ __ZL24is_qmm_generic_supportedRK46NDArrayQuantizedMatrixMultiplicationEncodeDataP14QmmGenericArgs : 2032 -> 2048
~ __ZL23EncodeQuantizedGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 18588 -> 18612
~ __ZL15EncodeReductionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 11572 -> 11184
~ __ZL19EncodeArrayIdentityPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 2844 -> 2848
~ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize : 10456 -> 10536
~ __ZL19EncodeSDPACommonNewPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttentionj : 5972 -> 5764
~ __ZL30EncodeQuantizedSDPAVectorBasedPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention : 6808 -> 6684
~ __ZL32MPSNDArraySDPACreateUserConstantR36MPSNDArraySDPAStateFunctionConstants : 524 -> 568
~ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1819GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_ : 2584 -> 2588
~ __ZL12getArrayType11MPSDataType : 536 -> 556
CStrings:
+ "%@ %p \"%@\" Only MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
+ "Float8e8m0 inputs cannot be dequantized into Float16 outputs."
- "%@ %p \"%@\" For a MPSDataTypeInt32 source, detination must also be MPSDataTypeInt32.\n"
- "%@ %p \"%@\" For a MPSDataTypeUInt32 source, detination must also be MPSDataTypeUInt32.\n"
- "%@ %p \"%@\" Only MPSDataTypeUInt32 or MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
- "%@ %p \"%@\" This combination of data types is only supported for MPSNDArrayReduction where the operation is an argument minimum or maximum\n"
```
