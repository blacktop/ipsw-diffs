## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.3.8.1.0
-  __TEXT.__text: 0x10d738
+129.4.1.0.0
+  __TEXT.__text: 0x11704c
   __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x6ab4
-  __TEXT.__const: 0x895e8
-  __TEXT.__gcc_except_tab: 0x41bc
-  __TEXT.__cstring: 0xe474
-  __TEXT.__unwind_info: 0x1888
-  __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6d86
+  __TEXT.__objc_methlist: 0x6dec
+  __TEXT.__const: 0x896f0
+  __TEXT.__gcc_except_tab: 0x43d0
+  __TEXT.__cstring: 0xf6cb
+  __TEXT.__unwind_info: 0x18f8
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x1cbd
+  __TEXT.__objc_methname: 0x7350
   __TEXT.__objc_methtype: 0x1ef1
-  __TEXT.__objc_stubs: 0x3380
+  __TEXT.__objc_stubs: 0x3400
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0xf050
-  __DATA_CONST.__objc_classlist: 0x848
+  __DATA_CONST.__const: 0x1b650
+  __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_selrefs: 0x1630
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x820
+  __DATA_CONST.__objc_superrefs: 0x830
   __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x4060
-  __AUTH_CONST.__cfstring: 0x7020
-  __AUTH_CONST.__objc_const: 0xe918
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6b8
+  __AUTH_CONST.__const: 0x4340
+  __AUTH_CONST.__cfstring: 0x7180
+  __AUTH_CONST.__objc_const: 0xefe0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x734
   __DATA.__data: 0x9c4
   __DATA.__bss: 0x600
-  __DATA_DIRTY.__objc_data: 0x5280
+  __DATA_DIRTY.__objc_data: 0x52d0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 834C1E7E-7388-3A88-84BC-C52C7828B97D
-  Functions: 2246
-  Symbols:   7576
-  CStrings:  3759
+  UUID: 1978F275-4D09-3334-85A2-834147925157
+  Functions: 2321
+  Symbols:   7772
+  CStrings:  3826
 
Symbols:
+ +[MPSNDArrayFusedDepthwisePointwiseConvolution libraryInfo:]
+ +[MPSNDArrayFusedDepthwisePointwiseConvolution supportsPostfixForDevice:]
+ +[MPSNDArrayFusedDepthwisePointwiseConvolution supportsPrefixForDevice:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution dealloc]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution depthwiseWeightsFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution destinationStrides]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution dilationRates]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution dimensionsNotToBeBroadcast]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution dimensionsToBeRetained]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution groups]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution initWithDevice:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution initWithDevice:ndArrayFusedConvolutionDescriptor:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution initWithDevice:ndArrayFusedConvolutionDescriptor:sourceCount:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution inputDataFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution inputFeatureChannels]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution kernelDimensionalityForSourceArrays:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution kernelSizes]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution offsets]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution outputDataFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution outputFeatureChannels]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution pointwiseWeightsFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution setOffsets:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution strideInPixels]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution stridesAtSourceIndex:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolution workloadStatisticsForSourceArrays:destArrays:kernel:kernelDAGObject:sourceState:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor copyWithZone:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor depthwiseWeightsFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor dilationRateInX]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor dilationRateInY]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor groups]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor init]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor inputDataFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor inputFeatureChannels]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor kernelHeight]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor kernelWidth]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor outputDataFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor outputFeatureChannels]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor pointwiseWeightsFormat]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setDepthwiseWeightsFormat:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setDilationRateInX:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setDilationRateInY:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setGroups:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setInputDataFormat:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setInputFeatureChannels:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setKernelHeight:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setKernelWidth:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setOutputDataFormat:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setOutputFeatureChannels:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setPointwiseWeightsFormat:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setStrideInPixelsX:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor setStrideInPixelsY:]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor strideInPixelsX]
+ -[MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor strideInPixelsY]
+ -[MPSNDArrayMultiaryBase kernelMDAGObjectSetup:sourceArrays:sourceGradient:destination:]
+ -[MPSNDArrayMultiaryKernel encodeToCommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObjects:]
+ -[MPSNDArrayMultiaryKernel encodeToMPSCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObjects:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandBuffer:sourceArrays:resultState:outputStateIsTemporary:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:destinationArray:]
+ -[MPSNDArrayMultiaryKernel encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:]
+ -[MPSNDArrayScaledDotProductAttention setWindowSize:]
+ -[MPSNDArrayScaledDotProductAttention windowSize]
+ -[MPSNDArrayUnaryKernel encodeToMTL4CommandBuffer:sourceArray:destinationArray:]
+ -[MPSNDArrayUnaryKernel encodeToMTL4CommandBuffer:sourceArray:resultState:destinationArray:]
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table122
+ GCC_except_table143
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table43
+ GCC_except_table67
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table95
+ _OBJC_CLASS_$_MPSNDArrayFusedDepthwisePointwiseConvolution
+ _OBJC_CLASS_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ _OBJC_IVAR_$_MPSNDArrayAffineQuantizationDescriptor._hasDoubleQuantMinVal
+ _OBJC_IVAR_$_MPSNDArrayAffineQuantizationDescriptor._hasDoubleQuantScale
+ _OBJC_IVAR_$_MPSNDArrayAffineQuantizationDescriptor._hasMinValue
+ _OBJC_IVAR_$_MPSNDArrayAffineQuantizationDescriptor._hasZeroPoint
+ _OBJC_IVAR_$_MPSNDArrayAffineQuantizationDescriptor._signedAsUnsigned
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._channelMultiplier
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._depthwiseWeightsFormat
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._dilationRateInX
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._dilationRateInY
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._groups
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._inputDataFormat
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._inputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._kernelHeight
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._kernelWidth
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._outputDataFormat
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._outputFeatureChannels
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._pointwiseWeightsFormat
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._strideInPixelsX
+ _OBJC_IVAR_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor._strideInPixelsY
+ _OBJC_METACLASS_$_MPSNDArrayFusedDepthwisePointwiseConvolution
+ _OBJC_METACLASS_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __MergedGlobals.18
+ __MergedGlobals.8
+ __OBJC_$_CLASS_METHODS_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __OBJC_$_PROP_LIST_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_$_PROP_LIST_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __OBJC_CLASS_RO_$_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_CLASS_RO_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __OBJC_METACLASS_RO_$_MPSNDArrayFusedDepthwisePointwiseConvolution
+ __OBJC_METACLASS_RO_$_MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor
+ __Z30ndArrayFusedConvDeviceBehaviorP9MPSDevicey
+ __Z38MPSSetNDArraysOnComputeEncoderWithMDAGP17MPSComputeEncoderPK23NDArrayMultiaryCallInfombb
+ __ZL12fixTransposeP10MPSNDArrayP18MPSNDArrayIdentityPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_object
+ __ZL16reshapeFitToTilePU27objcproto16MTLCommandBuffer11objc_objectP10MPSNDArraymDv16_hm
+ __ZL29EncodeNDArrayFusedConvolutionPKvPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPK23NDArrayMultiaryCallInfo
+ __ZL45MPSNDArrayFusedConvolutionFunctionConstructorPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoRK23MPSFunctionConstantListRK33MPSFunctionConstructorExtraParamsPP7NSError
+ __ZL54CommonKernelsFusedDepthwisePointwiseConvolutionForward
+ __ZL58MPSNDArrayFusedDepthwisePointwiseConvolutionForwardKernels
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptions23MPSForwardProgressUsageP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_EPSR_ISO_E
+ __ZN40MPSNDArrayFusedConvolutionDeviceBehaviorD0Ev
+ __ZN40MPSNDArrayFusedConvolutionDeviceBehaviorD1Ev
+ __ZNK40MPSNDArrayFusedConvolutionDeviceBehavior13log2SIMDWidthEv
+ __ZNK40MPSNDArrayFusedConvolutionDeviceBehavior24EncodeNDArrayConvolutionEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectP33NDArrayFusedConvolutionEncodeData
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt12out_of_rangeC1B9foe210106EPKc
+ __ZNSt3__110shared_ptrI12MPSKernelDAGED1B9foe210106Ev
+ __ZNSt3__110shared_ptrI12MPSKernelDAGED2B9foe210106Ev
+ __ZNSt3__110shared_ptrI16MPSKernelUserDAGED1B9foe210106Ev
+ __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED1B9foe210106Ev
+ __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED2B9foe210106Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSO_IJEEEEEENS7_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S4_EENS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S9_SD_SB_Lb1EEENS_9allocatorIS9_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjNS_4pairIKjjEENS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__113unordered_mapIjjNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjjEEEEED1B9foe210106Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__120__throw_out_of_rangeB9foe210106EPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIP10BaseTensorNS_9allocatorIS2_EEE20__throw_out_of_rangeB9foe210106Ev
+ __ZNSt3__16vectorIP14MPSDAGKernelOpNS_9allocatorIS2_EEE20__throw_out_of_rangeB9foe210106Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_out_of_rangeB9foe210106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZTV40MPSNDArrayFusedConvolutionDeviceBehavior
+ ___block_literal_global.160
+ ___block_literal_global.214
+ ___block_literal_global.217
+ ___block_literal_global.259
+ ___block_literal_global.290
+ ___block_literal_global.317
+ ___block_literal_global.320
+ ___block_literal_global.344
+ ___block_literal_global.441
+ _objc_msgSend$encodeToMPSCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObjects:
+ _objc_msgSend$initWithDevice:ndArrayFusedConvolutionDescriptor:sourceCount:
+ _objc_msgSend$kernelMDAGObjectSetup:sourceArrays:sourceGradient:destination:
+ _objc_msgSend$windowSize
- GCC_except_table100
- GCC_except_table102
- GCC_except_table121
- GCC_except_table142
- GCC_except_table33
- GCC_except_table41
- GCC_except_table56
- GCC_except_table65
- GCC_except_table74
- GCC_except_table75
- GCC_except_table84
- GCC_except_table91
- __ZL18updateDAGDestShapePP18MPSKernelDAGObjectP10MPSNDArray
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt12out_of_rangeC1B8ne200100EPKc
- __ZNSt3__110shared_ptrI12MPSKernelDAGED1B8ne200100Ev
- __ZNSt3__110shared_ptrI12MPSKernelDAGED2B8ne200100Ev
- __ZNSt3__110shared_ptrI16MPSKernelUserDAGED1B8ne200100Ev
- __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED1B8ne200100Ev
- __ZNSt3__110unique_ptrIKNS_6vectorIlNS_9allocatorIlEEEENS_14default_deleteIS5_EEED2B8ne200100Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPvPU19objcproto9MTLBuffer11objc_objectEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS5_S2_EEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJOjEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjjEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__113unordered_mapIjjNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjjEEEEED1B8ne200100Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
- __ZNSt3__16vectorIP10BaseTensorNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
- __ZNSt3__16vectorIP14MPSDAGKernelOpNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
- __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_out_of_rangeB8ne200100Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___block_literal_global.159
- ___block_literal_global.205
- ___block_literal_global.208
- ___block_literal_global.253
- ___block_literal_global.284
- ___block_literal_global.316
- ___block_literal_global.319
- ___block_literal_global.343
- ___block_literal_global.440
- _memset_pattern16
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9OugAi1RAwYdGJmpK-QxkLwK441-jodIHH1nw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/Fused/MPSNDArrayFusedDepthwisePointwiseConvolution.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMultiplyGeneric.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayUnaryKernel.mm"
+ "/Library/Caches/com.apple.xbs/F80A0678-B51C-499B-83B0-28296C029534/TemporaryDirectory.S4zphl/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"
+ "3 sources needed: source tensor, depthwise weights, and pointwise weights"
+ "MPSNDArrayFusedDepthwisePointwiseConvolution"
+ "MPSNDArrayFusedDepthwisePointwiseConvolutionDescriptor"
+ "MTL3On4Unavailable"
+ "Only depthwise weight format of HWIO supported"
+ "Only input format of NCHW type supported"
+ "Only output format of NHWC type supported"
+ "Only pointwise weight format of HWIO supported"
+ "Only supports equal strides across X and Y dimensions"
+ "Please initialize the %@ class with initWithDevice:ndArrayFusedConvolutionDescriptor\n"
+ "TI,N,V_depthwiseWeightsFormat"
+ "TI,N,V_inputDataFormat"
+ "TI,N,V_outputDataFormat"
+ "TI,N,V_pointwiseWeightsFormat"
+ "TI,R,N,V_depthwiseWeightsFormat"
+ "TI,R,N,V_inputDataFormat"
+ "TI,R,N,V_outputDataFormat"
+ "TI,R,N,V_pointwiseWeightsFormat"
+ "Ti,N,V_windowSize"
+ "_depthwiseWeightsFormat"
+ "_inputDataFormat"
+ "_outputDataFormat"
+ "_pointwiseWeightsFormat"
+ "_windowSize"
+ "allowReducedPrecision flag is set. Running A18 MXU Winograd using bf16 precision.\n"
+ "depthwiseWeightsFormat"
+ "encodeToCommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObjects:"
+ "encodeToMPSCommandEncoder:commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObjects:"
+ "encodeToMTL4CommandBuffer:sourceArray:destinationArray:"
+ "encodeToMTL4CommandBuffer:sourceArray:resultState:destinationArray:"
+ "encodeToMTL4CommandBuffer:sourceArrays:destinationArray:"
+ "encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:"
+ "encodeToMTL4CommandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:"
+ "encodeToMTL4CommandBuffer:sourceArrays:resultState:outputStateIsTemporary:"
+ "encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:destinationArray:"
+ "encodeToMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:resultState:destinationArray:kernelDAGObject:"
+ "initWithDevice:ndArrayFusedConvolutionDescriptor:"
+ "initWithDevice:ndArrayFusedConvolutionDescriptor:sourceCount:"
+ "inputDataFormat"
+ "kernelMDAGObjectSetup:sourceArrays:sourceGradient:destination:"
+ "ndArrayFusedDepthwisePointwiseConvolution"
+ "ndArrayFusedDepthwisePointwiseConvolutionTILEC"
+ "ndArrayFusedDepthwisePointwiseConvolutionTILECTILEO"
+ "outputDataFormat"
+ "pointwiseWeightsFormat"
+ "setDepthwiseWeightsFormat:"
+ "setInputDataFormat:"
+ "setOutputDataFormat:"
+ "setPointwiseWeightsFormat:"
+ "setWindowSize:"
+ "windowSize"
- "/Library/Caches/com.apple.xbs/Binaries/MetalPerformanceShaders/install/Symbols/BuiltProducts/MPSCore.framework/PrivateHeaders/Internal/MPSCoreInternal.h"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolution3D.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.h"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA14.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.h"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionA18.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionAMD.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayConvolutionPreG13.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCostVolume.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayCropResize.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayDepthwiseConvolution.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayFourierTransform.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGather.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGatherND.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayGridSample.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayHammingDistance.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIdentity.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayIm2col.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLUTGEMV.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayLocalConvolution.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMatrixMultiplication.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayMultiaryKernel.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayNMS.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPad.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayPooling.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantization.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedConvolution.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedGatherND.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMatrixMultiplication.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayQuantizedMultiplyGeneric.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayRandom.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayReduction.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayResample.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScaledDotProductAttention.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScan.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayScatter.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySoftMax.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArraySort.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStitchedReduction.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayStridedSlice.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/Kernels/MPSNDArrayTopK.mm"
- "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/MPSNDArrayMatrixMultiplicationA18.h"

```
