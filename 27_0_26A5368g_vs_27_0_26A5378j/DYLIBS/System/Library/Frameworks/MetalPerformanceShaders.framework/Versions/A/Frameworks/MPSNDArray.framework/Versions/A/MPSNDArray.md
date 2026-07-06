## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray`

```diff

-  __TEXT.__text: 0x127a80
-  __TEXT.__objc_methlist: 0x70dc
-  __TEXT.__const: 0x8a4e0
-  __TEXT.__gcc_except_tab: 0x4670
-  __TEXT.__cstring: 0x11f8f
+  __TEXT.__text: 0x12d004
+  __TEXT.__objc_methlist: 0x7274
+  __TEXT.__const: 0x8ac40
+  __TEXT.__gcc_except_tab: 0x4760
+  __TEXT.__cstring: 0x13002
   __TEXT.__oslogstring: 0x13
-  __TEXT.__unwind_info: 0x1a60
+  __TEXT.__unwind_info: 0x1ab0
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b7a8
-  __DATA_CONST.__objc_classlist: 0x878
+  __DATA_CONST.__const: 0x1fc18
+  __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1730
+  __DATA_CONST.__objc_selrefs: 0x17d0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x850
+  __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__got: 0x358
   __AUTH_CONST.__const: 0x46a0
-  __AUTH_CONST.__cfstring: 0x8620
-  __AUTH_CONST.__objc_const: 0xf5c0
+  __AUTH_CONST.__cfstring: 0x9280
+  __AUTH_CONST.__objc_const: 0xf7d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x784
+  __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0x9c4
-  __DATA.__bss: 0x640
+  __DATA.__bss: 0x648
   __DATA_DIRTY.__objc_data: 0x54b0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2426
-  Symbols:   5656
-  CStrings:  2661
+  Functions: 2463
+  Symbols:   5720
+  CStrings:  2860
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[MPSNDArrayLinearAttention libraryInfo:]
+ +[MPSNDArrayLinearAttention supportsPostfixForDevice:]
+ +[MPSNDArrayLinearAttention supportsPrefixForDevice:]
+ -[MPSNDArrayLinearAttention buildParamsForQueries:keys:values:decayGates:betaValues:initialState:outputState:output:g_exp:shapes:]
+ -[MPSNDArrayLinearAttention dealloc]
+ -[MPSNDArrayLinearAttention dispatchChunkParallelWithEncoder:commandBuffer:params:A_chunks:B_chunks:initialState:S_state:shapes:laHash:]
+ -[MPSNDArrayLinearAttention dispatchExponentiationWithEncoder:decayGates:expGatesPso:shapes:]
+ -[MPSNDArrayLinearAttention dispatchSequentialWithEncoder:commandBuffer:params:shapes:laHash:]
+ -[MPSNDArrayLinearAttention encodeImpl:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:]
+ -[MPSNDArrayLinearAttention encodeWithEncoder:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:]
+ -[MPSNDArrayLinearAttention extractShapesFromQueries:keys:values:decayGates:betaValues:initialState:outputState:output:]
+ -[MPSNDArrayLinearAttention gatesAreLogSpace]
+ -[MPSNDArrayLinearAttention initWithDevice:]
+ -[MPSNDArrayLinearAttention kernelOverride]
+ -[MPSNDArrayLinearAttention qScaleFactor]
+ -[MPSNDArrayLinearAttention setGatesAreLogSpace:]
+ -[MPSNDArrayLinearAttention setKernelOverride:]
+ -[MPSNDArrayLinearAttention setQScaleFactor:]
+ -[MPSNDArrayLinearAttention setUseQKL2Norm:]
+ -[MPSNDArrayLinearAttention setVariant:]
+ -[MPSNDArrayLinearAttention useQKL2Norm]
+ -[MPSNDArrayLinearAttention variant]
+ -[MPSNDArrayMatrixMultiplication advanceAutoTuneIteration]
+ -[MPSNDArrayMatrixMultiplication autoTuneIteration]
+ -[MPSNDArrayMatrixMultiplication logNextAutoTuneParams]
+ -[MPSNDArrayMatrixMultiplication setAutoTuneIteration:]
+ -[MPSNDArrayMatrixMultiplication setLogNextAutoTuneParams:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication hasLHSIndices]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication hasUnsortOrder]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:hasLHSIndices:hasUnsortOrder:sourceCount:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication setBatchDims:]
+ -[MPSNDArrayQuantizedGatherMatrixMultiplication setIsSorted:]
+ GCC_except_table114
+ GCC_except_table49
+ OBJC_IVAR_$_MPSNDArrayConvolution2DGradientWithInput._srcDataFormat
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._gatesAreLogSpace
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._identity
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._kernelOverride
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._qScaleFactor
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._useQKL2Norm
+ OBJC_IVAR_$_MPSNDArrayLinearAttention._variant
+ _OBJC_CLASS_$_MPSNDArrayLinearAttention
+ _OBJC_METACLASS_$_MPSNDArrayLinearAttention
+ __OBJC_$_CLASS_METHODS_MPSNDArrayLinearAttention
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayLinearAttention
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayLinearAttention
+ __OBJC_$_PROP_LIST_MPSNDArrayLinearAttention
+ __OBJC_CLASS_RO_$_MPSNDArrayLinearAttention
+ __OBJC_METACLASS_RO_$_MPSNDArrayLinearAttention
+ __ZL18validateArrayShapeP10MPSNDArrayP8NSStringSt16initializer_listImE
+ __ZL21EncodeLinearAttentionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK39NDArrayMultiaryMultiDestinationCallInfo
+ __ZL26kLinearAttentionKernelInfo
+ __ZL32MPSNDArrayLinearAttentionKernels
+ __ZL44MPSNDArrayLinearAttentionFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL62MPSNDArrayMatrixMultiplyGlobalKSplitsHelperFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL6getPsoP10MPSLibraryjPK13MPSKernelInfoyPU27objcproto16MTLCommandBuffer11objc_object
+ __ZNK33MPSNDArrayMatMulA14DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfoPNSt3__18optionalIbEE
+ __ZNK33MPSNDArrayMatMulA18DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfoPNSt3__18optionalIbEE
+ __ZNK36MPSNDArrayMatMulCommonDeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfoPNSt3__18optionalIbEE
+ _objc_msgSend$buildParamsForQueries:keys:values:decayGates:betaValues:initialState:outputState:output:g_exp:shapes:
+ _objc_msgSend$dispatchChunkParallelWithEncoder:commandBuffer:params:A_chunks:B_chunks:initialState:S_state:shapes:laHash:
+ _objc_msgSend$dispatchExponentiationWithEncoder:decayGates:expGatesPso:shapes:
+ _objc_msgSend$dispatchSequentialWithEncoder:commandBuffer:params:shapes:laHash:
+ _objc_msgSend$encodeImpl:commandBuffer:queries:keys:values:decayGates:betaValues:initialState:outputState:output:
+ _objc_msgSend$extractShapesFromQueries:keys:values:decayGates:betaValues:initialState:outputState:output:
+ _objc_msgSend$initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:hasLHSIndices:hasUnsortOrder:sourceCount:
+ _objc_msgSend$memoryBarrierWithScope:
+ _objc_msgSend$useResource:usage:
+ _objc_msgSend$variant
- GCC_except_table57
- GCC_except_table83
- __ZNK33MPSNDArrayMatMulA14DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
- __ZNK33MPSNDArrayMatMulA18DeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
- __ZNK36MPSNDArrayMatMulCommonDeviceBehavior17IsMatMulSupportedEPKvPK23NDArrayMultiaryCallInfo
- _objc_msgSend$initWithDevice:leftQuantizationDescriptor:rightQuantizationDescriptor:isSorted:batchDims:sourceCount:
CStrings:
+ "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
+ "%@: dimension %lu is %lu, expected %lu"
+ "%@: expected %lu dimensions, got %lu"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/Fused/MPSNDArrayFusedDepthwisePointwiseConvolution.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherMatrixMultiplication.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLinearAttention.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherMatrixMultiplication.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayUnaryKernel.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rlQSlj/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
+ "4 sources required when hasLHSIndices is set"
+ "4 sources required when hasUnsortOrder is set"
+ "A matrix cannot be transposed"
+ "Attempting to use global KSplits without linearization. This is currently not tested."
+ "Bad value dimensions"
+ "Cannot broadcast A to LHS indices"
+ "Cannot broadcast x to lhs_indices"
+ "Chunked algorithm selected but no valid pass 2 kernel for dk=%lu dv=%lu. Falling back to sequential algorithm."
+ "Dk (%zu) exceeds maximum supported value (128)"
+ "Dk (%zu) must be a power of 2"
+ "Dv (%zu) exceeds maximum supported value (128)"
+ "Dv (%zu) must be a power of 2"
+ "GEMMGlobalKSplits_Initializer::gemmA18InitializeAtomicCounterToZero"
+ "GEMMGlobalReduction::gemmA18GlobalReduction"
+ "GLA variant requires 4D decayGates [B, N_v, S, Dk]"
+ "Key tensor is empty"
+ "Mamba2 variant requires 3D decayGates [B, N_v, S]"
+ "N_v (%zu) must be a multiple of N_kq (%zu) for Q/K head broadcasting"
+ "Quantized tensor should be in 8 bits"
+ "Required threads for pass 2 (%lu) exceeds limit (%lu)"
+ "Scale tensor should be in fp16, bf16 or fp32"
+ "Sub tiles must be power of 2 when using morton order"
+ "Unable to create pso for kernelName='%@', hash=%llx"
+ "Unexpected dimension value"
+ "Unsort order size must match x size"
+ "Unsupported data type %u"
+ "Unsupported pass2 shape Dk x Dv = (%lux%lu)"
+ "betaValues"
+ "betaValues.dataType (%u) must match keys.dataType (%u)."
+ "decayGates"
+ "decayGates must be 3D [B,N_v,S] (GDN/Mamba2) or 4D [B,N_v,S,Dk] (KDA/GLA)"
+ "decayGates.dataType (%u) must match keys.dataType (%u)."
+ "encoder nil"
+ "g_exp nil"
+ "gatedDeltaChunkScanPass2TensorOpsLastRound_128_128"
+ "gatedDeltaChunkScanPass2TensorOpsLastRound_16_16"
+ "gatedDeltaChunkScanPass2TensorOpsLastRound_64_64"
+ "gatedDeltaChunkScanPass2TensorOps_128_128"
+ "gatedDeltaChunkScanPass2TensorOps_16_16"
+ "gatedDeltaChunkScanPass2TensorOps_64_64"
+ "gatedDeltaChunkScan_pass1_dv2col_narrow_bfloat"
+ "gatedDeltaChunkScan_pass1_dv2col_narrow_float"
+ "gatedDeltaChunkScan_pass1_dv2col_narrow_half"
+ "gatedDeltaChunkScan_pass1_dv2col_wide_bfloat"
+ "gatedDeltaChunkScan_pass1_dv2col_wide_float"
+ "gatedDeltaChunkScan_pass1_dv2col_wide_half"
+ "gatedDeltaChunkScan_pass1_narrow_bfloat"
+ "gatedDeltaChunkScan_pass1_narrow_float"
+ "gatedDeltaChunkScan_pass1_narrow_half"
+ "gatedDeltaChunkScan_pass1_wide_bfloat"
+ "gatedDeltaChunkScan_pass1_wide_float"
+ "gatedDeltaChunkScan_pass1_wide_half"
+ "gatedDeltaChunkScan_pass3_2col_narrow_bfloat"
+ "gatedDeltaChunkScan_pass3_2col_narrow_float"
+ "gatedDeltaChunkScan_pass3_2col_narrow_half"
+ "gatedDeltaChunkScan_pass3_2col_wide_bfloat"
+ "gatedDeltaChunkScan_pass3_2col_wide_float"
+ "gatedDeltaChunkScan_pass3_2col_wide_half"
+ "gatedDeltaChunkScan_pass3_narrow_bfloat"
+ "gatedDeltaChunkScan_pass3_narrow_float"
+ "gatedDeltaChunkScan_pass3_narrow_half"
+ "gatedDeltaChunkScan_pass3_wide_bfloat"
+ "gatedDeltaChunkScan_pass3_wide_float"
+ "gatedDeltaChunkScan_pass3_wide_half"
+ "gatedDeltaExponentiateGates_bfloat"
+ "gatedDeltaExponentiateGates_float"
+ "gatedDeltaExponentiateGates_half"
+ "gatedDeltaExponentiateGates_wide_bfloat"
+ "gatedDeltaExponentiateGates_wide_float"
+ "gatedDeltaExponentiateGates_wide_half"
+ "gatedDeltaUpdate_col_narrow_bfloat"
+ "gatedDeltaUpdate_col_narrow_float"
+ "gatedDeltaUpdate_col_narrow_half"
+ "gatedDeltaUpdate_col_wide_bfloat"
+ "gatedDeltaUpdate_col_wide_float"
+ "gatedDeltaUpdate_col_wide_half"
+ "gatedDeltaUpdate_dv2col_narrow_bfloat"
+ "gatedDeltaUpdate_dv2col_narrow_float"
+ "gatedDeltaUpdate_dv2col_narrow_half"
+ "gatedDeltaUpdate_dv2col_wide_bfloat"
+ "gatedDeltaUpdate_dv2col_wide_float"
+ "gatedDeltaUpdate_dv2col_wide_half"
+ "initialState"
+ "initialState.dataType (%u) must match keys.dataType (%u)."
+ "keys.numberOfDimensions != 4"
+ "keys.numberOfDimensions != 4 (%lu)"
+ "lhs_indices must be uint32_t or int32_t"
+ "lhs_indices source required when hasLHSIndices is set"
+ "output"
+ "output.dataType (%u) must match keys.dataType (%u)."
+ "outputState"
+ "outputState.dataType (%u) must match keys.dataType (%u)."
+ "queries"
+ "queries.dataType (%u) must match keys.dataType (%u)."
+ "unsort_order must be uint32_t or int32_t"
+ "unsort_order source required when hasUnsortOrder is set"
+ "values.dataType (%u) must match keys.dataType (%u)."
+ "values.numberOfDimensions != 4"
+ "values.numberOfDimensions <= 3 (%lu)"
+ "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"
- "    {{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}, {%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}},"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/Fused/MPSNDArrayFusedDepthwisePointwiseConvolution.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherMatrixMultiplication.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherMatrixMultiplication.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayUnaryKernel.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g5t0aI/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
- "Quantized tensor should be in int8"
- "Scale tensor should be in fp16 or fp32"
- "{%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d}"

```
