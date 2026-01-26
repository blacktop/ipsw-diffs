## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.3.5.0.0
-  __TEXT.__text: 0x10cfb0
+129.3.8.0.0
+  __TEXT.__text: 0x10d738
   __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x6aa4
+  __TEXT.__objc_methlist: 0x6ab4
   __TEXT.__const: 0x895e8
-  __TEXT.__gcc_except_tab: 0x41a4
+  __TEXT.__gcc_except_tab: 0x41bc
   __TEXT.__cstring: 0xe474
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__unwind_info: 0x1888
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6d11
-  __TEXT.__objc_methtype: 0x1ed4
-  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_methname: 0x6d86
+  __TEXT.__objc_methtype: 0x1ef1
+  __TEXT.__objc_stubs: 0x3380
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0xf050
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1570
+  __DATA_CONST.__objc_selrefs: 0x1578
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x598

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A717907-3F80-3099-A330-DCD30C74B73A
-  Functions: 2244
-  Symbols:   7570
-  CStrings:  3757
+  UUID: 5C80CCC0-9E52-3D68-90AA-35268A59BA6B
+  Functions: 2246
+  Symbols:   7576
+  CStrings:  3759
 
Symbols:
+ -[MPSNDArrayConvolution2DGradientWithInput encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryGradientKernel encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:]
+ GCC_except_table102
+ GCC_except_table121
+ GCC_except_table142
+ GCC_except_table81
+ GCC_except_table91
+ _objc_msgSend$encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:
- GCC_except_table101
- GCC_except_table120
- GCC_except_table141
- GCC_except_table90
- GCC_except_table98
- __MergedGlobals.5
Functions:
~ __ZNK33MPSNDArrayMatMulA18DeviceBehavior33GetKernelDispatchParametersForKeyEP9MPSKernelR22MPSNDArrayA18MatMulKeyP32MPSMatMulAutoTuningParametersA18 : 1308 -> 1600
~ __Z18encode_qmm_genericPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP10MPSLibraryRK14QmmGenericArgs : 1732 -> 1764
+ -[MPSNDArrayMultiaryGradientKernel encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:]
~ -[MPSNDArrayMultiaryGradientKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:sourceGradient:gradientState:destinationArray:kernelDAGObject:] : 2512 -> 2548
+ -[MPSNDArrayConvolution2DGradientWithInput encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:]
~ __ZL25EncodeSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttention7MTLSize : 7108 -> 7168
~ __ZL34EncodeQuantizedSDPATileBasedCommonPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention7MTLSize : 9888 -> 9948
~ __ZL19EncodeSDPACommonNewPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK35MPSNDArrayScaledDotProductAttentionj : 5596 -> 5592
~ __ZL30EncodeQuantizedSDPAVectorBasedPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfoP9MPSDeviceP10MPSLibraryPK44MPSNDArrayQuantizedScaledDotProductAttention : 6548 -> 6604
~ __ZL18EncodeSDPAFallbackPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo : 11828 -> 11972
~ __ZL27getWinogradA18PrecisionModeP9MPSKernel11MPSDataTypeS1_S1_ : 480 -> 444
CStrings:
+ "@64@0:8@16@24@32^@40^@48^@56"
+ "encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:sourceGradientArray:destinationArray:kernelDAGObject:"

```
