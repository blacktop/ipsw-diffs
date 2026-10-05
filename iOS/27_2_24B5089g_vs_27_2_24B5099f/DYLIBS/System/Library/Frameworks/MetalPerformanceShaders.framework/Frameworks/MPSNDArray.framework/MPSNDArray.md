## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-130.1.1.0.0
-  __TEXT.__text: 0x111e48
+130.1.3.0.0
+  __TEXT.__text: 0x1122ec
   __TEXT.__objc_methlist: 0x7274
   __TEXT.__const: 0x9c9b0
-  __TEXT.__gcc_except_tab: 0x4ed8
-  __TEXT.__cstring: 0x125b3
+  __TEXT.__gcc_except_tab: 0x4f24
+  __TEXT.__cstring: 0x125cb
   __TEXT.__oslogstring: 0x27
-  __TEXT.__unwind_info: 0x1f80
+  __TEXT.__unwind_info: 0x1f88
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20c68
+  __DATA_CONST.__const: 0x20db8
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x350
   __AUTH_CONST.__const: 0x4878
-  __AUTH_CONST.__cfstring: 0x94e0
+  __AUTH_CONST.__cfstring: 0x9500
   __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x5b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2477
-  Symbols:   5103
-  CStrings:  1716
+  Functions: 2478
+  Symbols:   5105
+  CStrings:  1717
 
Symbols:
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
Functions:
~ __ZL12EncodeDWConvPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 6888 -> 6956
~ -[MPSNDArrayLinearAttention encodeImpl:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2852 -> 2876
~ __ZL23EncodeQuantizedGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 18612 -> 19456
+ __ZNSt3__16vectorINS_4pairIPKiPKjEENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
~ __ZL10EncodeSDPAPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 3612 -> 3648
~ __ZNK38MPSNDArrayConvolutionDeviceBehaviorA1819GetKernelParametersEP9MPSKernelR50MPSNDArrayConvolutionGradientWithWeightsParametersPv11MPSDataTypeS5_S5_ : 2588 -> 2584
CStrings:
+ "depthwiseConv3d_cFirst4"
```
