## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray`

```diff

-130.0.19.0.0
-  __TEXT.__text: 0x1124cc
+130.1.1.0.0
+  __TEXT.__text: 0x112400
   __TEXT.__objc_methlist: 0x7274
   __TEXT.__const: 0x9c9e0
   __TEXT.__gcc_except_tab: 0x4e8c
-  __TEXT.__cstring: 0x134ed
+  __TEXT.__cstring: 0x133df
   __TEXT.__oslogstring: 0x27
   __TEXT.__unwind_info: 0x1fb0
   __TEXT.__eh_frame: 0xb8

   __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x358
   __AUTH_CONST.__const: 0x4900
-  __AUTH_CONST.__cfstring: 0x9540
+  __AUTH_CONST.__cfstring: 0x9500
   __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x570

   - /usr/lib/libobjc.A.dylib
   Functions: 2490
   Symbols:   5568
-  CStrings:  1738
+  CStrings:  1736
 
Functions:
~ __ZL36EncodeConstantInitializationInternalPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfob : 1660 -> 1664
~ -[MPSNDArrayLinearAttention extractShapesFromQueries:keys:values:decayGates:betaValues:initialState:outputState:output:] : 2728 -> 2892
~ __ZL18validateArrayShapeP10MPSNDArrayP8NSStringSt16initializer_listImE : 284 -> 328
~ __ZL24is_qmm_generic_supportedRK46NDArrayQuantizedMatrixMultiplicationEncodeDataP14QmmGenericArgs : 1996 -> 2028
~ __ZL23EncodeQuantizedGatherNDPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 17476 -> 17560
~ __ZL15EncodeReductionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 11600 -> 11212
~ __ZL19EncodeArrayIdentityPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 2856 -> 2864
~ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize : 10404 -> 10460
~ __ZL19EncodeSDPACommonNewPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttentionj : 5936 -> 5776
~ __ZL30EncodeQuantizedSDPAVectorBasedPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention : 6772 -> 6660
~ __ZL32MPSNDArraySDPACreateUserConstantR36MPSNDArraySDPAStateFunctionConstants : 524 -> 568
~ __ZL12getArrayType11MPSDataType : 536 -> 556
CStrings:
+ "%@ %p \"%@\" Only MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
+ "Float8e8m0 inputs cannot be dequantized into Float16 outputs."
- "%@ %p \"%@\" For a MPSDataTypeInt32 source, detination must also be MPSDataTypeInt32.\n"
- "%@ %p \"%@\" For a MPSDataTypeUInt32 source, detination must also be MPSDataTypeUInt32.\n"
- "%@ %p \"%@\" Only MPSDataTypeUInt32 or MPSDataTypeInt32 destinations are supported for Argument Reductions.\n"
- "%@ %p \"%@\" This combination of data types is only supported for MPSNDArrayReduction where the operation is an argument minimum or maximum\n"
```
