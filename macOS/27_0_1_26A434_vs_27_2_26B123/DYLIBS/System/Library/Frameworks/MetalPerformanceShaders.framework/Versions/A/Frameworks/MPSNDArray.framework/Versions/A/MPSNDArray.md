## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray`

```diff

-130.0.19.0.0
-  __TEXT.__text: 0x1136d4
+130.1.4.0.0
+  __TEXT.__text: 0x114750
   __TEXT.__objc_methlist: 0x7274
   __TEXT.__const: 0x9c9e0
-  __TEXT.__gcc_except_tab: 0x4e8c
-  __TEXT.__cstring: 0x134ed
+  __TEXT.__gcc_except_tab: 0x4edc
+  __TEXT.__cstring: 0x133f7
   __TEXT.__oslogstring: 0x27
   __TEXT.__unwind_info: 0x1ba0
   __TEXT.__eh_frame: 0xb8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20b88
+  __DATA_CONST.__const: 0x20cd8
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x358
   __AUTH_CONST.__const: 0x4900
-  __AUTH_CONST.__cfstring: 0x9540
+  __AUTH_CONST.__cfstring: 0x9520
   __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0x7a4
-  __DATA.__data: 0x9ec
+  __DATA.__data: 0x68c
   __DATA.__bss: 0x650
-  __DATA_DIRTY.__objc_data: 0x54b0
+  __DATA_DIRTY.__objc_data: 0x5500
+  __DATA_DIRTY.__data: 0x360
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2490
-  Symbols:   5568
-  CStrings:  1738
+  Functions: 2491
+  Symbols:   5570
+  CStrings:  1737
 
Symbols:
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
Functions:
~ __ZL12EncodeDWConvPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 6924 -> 7024
~ __ZL36EncodeConstantInitializationInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob : 1664 -> 1668
~ -[MPSNDArrayLinearAttention extractShapesFromQueries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2736 -> 2900
~ -[MPSNDArrayLinearAttention buildParamsForQueries:keys:values:decayGates:betaValues:initialState:outputState:output:g_exp:shapes:] : 2516 -> 4624
~ -[MPSNDArrayLinearAttention dispatchExponentiationWithEncoder:decayGates:expGatesPso:shapes:] : 196 -> 468
~ -[MPSNDArrayLinearAttention dispatchChunkParallelWithEncoder:commandBuffer:params:A_chunks:B_chunks:initialState:S_state:shapes:laHash:] : 2300 -> 2336
~ -[MPSNDArrayLinearAttention encodeImpl:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2860 -> 3572
~ __ZL18validateArrayShapeP10MPSNDArrayP8NSStringSt16initializer_listImE : 284 -> 328
~ __ZL24is_qmm_generic_supportedRK46NDArrayQuantizedMatrixMultiplicationEncodeDataP14QmmGenericArgs : 1996 -> 2028
~ __ZL23EncodeQuantizedGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 17480 -> 18516
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
~ __ZL15EncodeReductionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 11628 -> 11240
~ __ZL19EncodeArrayIdentityPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 2880 -> 2888
~ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize : 10712 -> 10768
~ __ZL10EncodeSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 3612 -> 3648
~ __ZL19EncodeSDPACommonNewPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttentionj : 5956 -> 5796
~ __ZL30EncodeQuantizedSDPAVectorBasedPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention : 6792 -> 6680
~ __ZL32MPSNDArraySDPACreateUserConstantR36MPSNDArraySDPAStateFunctionConstants : 524 -> 568
~ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1819GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_ : 2664 -> 2648
~ __ZL12getArrayType11MPSDataType : 536 -> 556
CStrings:
+ "%@ %p \"%@\" Only MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
+ "Float8e8m0 inputs cannot be dequantized into Float16 outputs."
+ "depthwiseConv3d_cFirst4"
- "%@ %p \"%@\" For a MPSDataTypeInt32 source, detination must also be MPSDataTypeInt32.\n"
- "%@ %p \"%@\" For a MPSDataTypeUInt32 source, detination must also be MPSDataTypeUInt32.\n"
- "%@ %p \"%@\" Only MPSDataTypeUInt32 or MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
- "%@ %p \"%@\" This combination of data types is only supported for MPSNDArrayReduction where the operation is an argument minimum or maximum\n"
```
