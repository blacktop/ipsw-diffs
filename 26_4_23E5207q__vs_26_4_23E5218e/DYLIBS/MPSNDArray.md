## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.4.1.0.0
-  __TEXT.__text: 0x11704c
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x6dec
-  __TEXT.__const: 0x896f0
-  __TEXT.__gcc_except_tab: 0x43d0
-  __TEXT.__cstring: 0xf6cb
-  __TEXT.__unwind_info: 0x18f8
+129.4.3.0.0
+  __TEXT.__text: 0x11c5e0
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x6ee4
+  __TEXT.__const: 0x89700
+  __TEXT.__gcc_except_tab: 0x453c
+  __TEXT.__cstring: 0x10295
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x1cbd
-  __TEXT.__objc_methname: 0x7350
-  __TEXT.__objc_methtype: 0x1ef1
-  __TEXT.__objc_stubs: 0x3400
+  __TEXT.__objc_classname: 0x1d25
+  __TEXT.__objc_methname: 0x720b
+  __TEXT.__objc_methtype: 0x1f1f
+  __TEXT.__objc_stubs: 0x34a0
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1b650
-  __DATA_CONST.__objc_classlist: 0x858
+  __DATA_CONST.__const: 0x1b668
+  __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1630
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x830
-  __AUTH_CONST.__auth_got: 0x598
+  __DATA_CONST.__objc_superrefs: 0x848
+  __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__const: 0x4340
-  __AUTH_CONST.__cfstring: 0x7180
-  __AUTH_CONST.__objc_const: 0xefe0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x734
+  __AUTH_CONST.__cfstring: 0x7ba0
+  __AUTH_CONST.__objc_const: 0xf2d8
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x750
   __DATA.__data: 0x9c4
   __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x52d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1978F275-4D09-3334-85A2-834147925157
-  Functions: 2321
-  Symbols:   7772
-  CStrings:  3826
+  UUID: E51830C6-E7EA-370C-AD77-217C0E46C550
+  Functions: 2341
+  Symbols:   7848
+  CStrings:  3999
 
Symbols:
+ +[MPSNDArrayDequantize libraryInfo:]
+ +[MPSNDArrayGatherMatrixMultiplication supportsPostfixForDevice:]
+ +[MPSNDArrayGatherMatrixMultiplication supportsPrefixForDevice:]
+ +[MPSNDArrayQuantizedGatherMatrixMultiplication supportsPostfixForDevice:]
+ +[MPSNDArrayQuantizedGatherMatrixMultiplication supportsPrefixForDevice:]
+ -[MPSNDArrayDequantize copyWithZone:device:]
+ -[MPSNDArrayDequantize dealloc]
+ -[MPSNDArrayDequantize initWithDevice:quantizationDescriptor:]
+ -[MPSNDArrayDequantize kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGatherMatrixMultiplication batchDims]
+ -[MPSNDArrayGatherMatrixMultiplication encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayGatherMatrixMultiplication initWithDevice:]
+ -[MPSNDArrayGatherMatrixMultiplication initWithDevice:isSorted:batchDims:sourceCount:]
+ -[MPSNDArrayGatherMatrixMultiplication initWithDevice:sourceCount:]
+ -[MPSNDArrayGatherMatrixMultiplication isSorted]
+ -[MPSNDArrayGatherMatrixMultiplication kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayGatherMatrixMultiplication kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication batchDims]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication encodePreProcessingToCommandEncoder:commandBuffer:sourceArrays:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:sourceCount:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:sourceCount:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication isSorted]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication kernelDimensionalityForSourceArrays:destinationArrays:kernelDAGObject:]
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table38
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table89
+ _OBJC_CLASS_$_MPSNDArrayDequantize
+ _OBJC_CLASS_$_MPSNDArrayGatherMatrixMultiplication
+ _OBJC_CLASS_$_MPSNDArrayQuantizedGatherMatrixMultiplication
+ _OBJC_CLASS_$_MTLTensorDescriptor
+ _OBJC_CLASS_$_MTLTensorExtents
+ _OBJC_IVAR_$_MPSNDArrayDequantize._quantizationDescriptor
+ _OBJC_METACLASS_$_MPSNDArrayDequantize
+ _OBJC_METACLASS_$_MPSNDArrayGatherMatrixMultiplication
+ _OBJC_METACLASS_$_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_$_CLASS_METHODS_MPSNDArrayDequantize
+ __OBJC_$_CLASS_METHODS_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_$_CLASS_METHODS_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayDequantize
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayDequantize
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_$_PROP_LIST_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_$_PROP_LIST_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayDequantize
+ __OBJC_CLASS_RO_$_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __OBJC_METACLASS_RO_$_MPSNDArrayDequantize
+ __OBJC_METACLASS_RO_$_MPSNDArrayGatherMatrixMultiplication
+ __OBJC_METACLASS_RO_$_MPSNDArrayQuantizedGatherMatrixMultiplication
+ __Z12validateSDPAP10MPSNDArrayS0_S0_S0_20MPSNDArraySDPALayout
+ __ZL14EncodeGatherMMPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL21EncodeArrayDequantizePKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL23EncodeQuantizedGatherMMPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL43MPSNDArrayMatrixMultiplyFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZNSt3__19to_stringEy
+ ___block_literal_global.247
+ ___block_literal_global.250
+ ___block_literal_global.253
+ ___block_literal_global.447
+ _objc_msgSend$batchDims
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$initWithDevice:isSorted:batchDims:sourceCount:
+ _objc_msgSend$initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:sourceCount:
+ _objc_msgSend$isSorted
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:destinationArray:]
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:]
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:outputStateIsTemporary:]
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:destinationArray:]
- -[MPSNDArrayMultiaryKernel encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
- -[MPSNDArrayUnaryKernel encodeToMTL4CommandBuffer:sourceArray:destinationArray:]
- -[MPSNDArrayUnaryKernel encodeToMTL4CommandBuffer:sourceArray:resultState:destinationArray:]
- GCC_except_table109
- GCC_except_table110
- GCC_except_table112
- GCC_except_table43
- GCC_except_table64
- GCC_except_table79
- GCC_except_table80
- GCC_except_table85
- GCC_except_table86
- GCC_except_table87
- GCC_except_table94
- GCC_except_table95
- __ZL12validateSDPAP10MPSNDArrayS0_S0_S0_20MPSNDArraySDPALayout
- __ZL46MPSNDArrayMatrixMultiplyA18FunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
- ___block_literal_global.211
- ___block_literal_global.214
- ___block_literal_global.217
- ___block_literal_global.441
CStrings:
+ "-batchDims "
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB5RxgK3CJx6EpKxfKrkjM5Ou0wfRbzdN8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/Fused/MPSNDArrayFusedDepthwisePointwiseConvolution.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMultiplyGeneric.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
+ "/Library/Caches/com.apple.xbs/B8C3AFF0-DF53-4011-9AD9-8794627EC8D8/TemporaryDirectory.z12FBF/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
+ "3 sources required: a, b, rhs_indices"
+ "3 sources required: x, w, rhs_indices"
+ ">1 explicit batch dimensions not supported"
+ "@44@0:8@16B24Q28Q36"
+ "@60@0:8@16@24@32B40Q44Q52"
+ "A array rank must match output array rank"
+ "At least 3 sources required: a, b, rhs_indices"
+ "Cannot broadcast A batch shape to index shape"
+ "Cannot instantiate GatherVectorMatrixMultiply kernel"
+ "Encoding %s\n"
+ "Input array a must have at least 1 dimension"
+ "Input array b must have at least 1 dimension"
+ "Input array w must have at least 1 dimension"
+ "Input array x must have at least 1 dimension"
+ "LHS quantization not supported"
+ "Last dimension of first input must match second to last dimension of second input"
+ "MPSNDArrayDequantize"
+ "MPSNDArrayGatherMMTest"
+ "MPSNDArrayGatherMatrixMultiplication"
+ "MPSNDArrayQuantizedGatherMMTest"
+ "MPSNDArrayQuantizedGatherMatrixMultiplication"
+ "Missing quantization parameters"
+ "NDArrayGatherVectorMatrixMultiply_bfloat"
+ "NDArrayGatherVectorMatrixMultiply_float"
+ "NDArrayGatherVectorMatrixMultiply_half"
+ "Only 2,4,8 bit quantization supported"
+ "Only RHS affine quantization supported"
+ "Output batch shape must match index shape"
+ "Sorted inputs batch must match output batch"
+ "Source indices not found."
+ "TB,R,N,V_isSorted"
+ "TQ,R,N,V_batchDims"
+ "Unsupported RHS quantization descriptor"
+ "_batchDims"
+ "_isSorted"
+ "activations tensor must be contiguous"
+ "batchDims"
+ "bias shape must match scales shape"
+ "biases type must match x type"
+ "dequant_mx_fp4_e2m1_fp8_e4m3_16"
+ "dequant_mx_fp4_e2m1_fp8_e8m0_32"
+ "dequant_mx_fp6_e2m3_fp8_e8m0_32"
+ "dequant_mx_fp6_e3m2_fp8_e8m0_32"
+ "dequant_mx_fp8_e4m3_fp8_e8m0_32"
+ "dequant_mx_fp8_e5m2_fp8_e8m0_32"
+ "dequant_mx_int8b_p6_fp8_e8m0_32"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "failed to load dequant kernel"
+ "indices array must be uint32_t"
+ "indices must be uint32_t"
+ "initWithDevice:isSorted:batchDims:sourceCount:"
+ "initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:sourceCount:"
+ "invalid biases format"
+ "invalid block size"
+ "invalid dequantize array dimensions"
+ "invalid scales format"
+ "invalid weights layout"
+ "isSorted"
+ "mps_gather_mm_rhs_nn_bfloat"
+ "mps_gather_mm_rhs_nn_float"
+ "mps_gather_mm_rhs_nn_half"
+ "mps_gather_mm_rhs_nt_bfloat"
+ "mps_gather_mm_rhs_nt_float"
+ "mps_gather_mm_rhs_nt_half"
+ "mps_gather_qmm_rhs_n_bfloat_16"
+ "mps_gather_qmm_rhs_n_bfloat_64"
+ "mps_gather_qmm_rhs_n_float_16"
+ "mps_gather_qmm_rhs_n_float_64"
+ "mps_gather_qmm_rhs_n_half_16"
+ "mps_gather_qmm_rhs_n_half_64"
+ "mps_gather_qmm_rhs_t_bfloat_16"
+ "mps_gather_qmm_rhs_t_bfloat_64"
+ "mps_gather_qmm_rhs_t_float_16"
+ "mps_gather_qmm_rhs_t_float_64"
+ "mps_gather_qmm_rhs_t_half_16"
+ "mps_gather_qmm_rhs_t_half_64"
+ "mps_gather_qvm_n_bfloat"
+ "mps_gather_qvm_n_float"
+ "mps_gather_qvm_n_half"
+ "mps_gather_qvm_t_bfloat"
+ "mps_gather_qvm_t_float"
+ "mps_gather_qvm_t_half"
+ "output type must match x type"
+ "quantization data dimensions must match"
+ "scales layout must match bias layout"
+ "scales rank must match biases rank"
+ "scales type must match x type"
+ "source arrays not found"
+ "source datatype must match destination datatype"
+ "source datatypes must match"
+ "unsupported dequantize scheme"
+ "unsupported dequantize types"
+ "unsupported quantization scheme"
+ "weight innermost dimension must be divisble by 32"
+ "weights layout must match scales layout"
+ "weights rank must match scales rank"
+ "x array cannot be complex"
+ "x array must be contiguous"
+ "x array must be floating point"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/Fused/MPSNDArrayFusedDepthwisePointwiseConvolution.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMultiplyGeneric.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayUnaryKernel.mm"
- "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
- "MTL3On4Unavailable"
- "encodeToMTL4CommandBuffer:sourceArray:destinationArray:"
- "encodeToMTL4CommandBuffer:sourceArray:resultState:destinationArray:"
- "encodeToMTL4CommandBuffer:sourceArrays:destinationArray:"
- "encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:"
- "encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:"
- "encodeToMTL4CommandBuffer:sourceArrays:resultState:outputStateIsTemporary:"
- "encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:destinationArray:"
- "encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:"

```
