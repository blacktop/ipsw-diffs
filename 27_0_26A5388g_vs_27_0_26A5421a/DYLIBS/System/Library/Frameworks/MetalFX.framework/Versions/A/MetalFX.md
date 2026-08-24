## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/Versions/A/MetalFX`

```diff

-40.6.0.0.0
-  __TEXT.__text: 0x7f020
-  __TEXT.__objc_methlist: 0x534c
-  __TEXT.__const: 0x624
-  __TEXT.__gcc_except_tab: 0xbbf8
-  __TEXT.__cstring: 0x525e
-  __TEXT.__ustring: 0x186
-  __TEXT.__unwind_info: 0x1508
+40.8.0.0.0
+  __TEXT.__text: 0x85720
+  __TEXT.__objc_methlist: 0x55f4
+  __TEXT.__gcc_except_tab: 0xc294
+  __TEXT.__const: 0x608
+  __TEXT.__cstring: 0x5e5b
+  __TEXT.__ustring: 0x632
+  __TEXT.__unwind_info: 0x1768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x188
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x13e8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0x33e8
-  __DATA_CONST.__got: 0x2a0
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x5540
-  __AUTH_CONST.__objc_const: 0xe468
-  __AUTH_CONST.__weak_auth_got: 0x1f8
-  __AUTH_CONST.__objc_intobj: 0x360
-  __AUTH_CONST.__objc_arrayobj: 0x35e8
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xf94
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0x2ad8
+  __DATA_CONST.__got: 0x2b8
+  __AUTH_CONST.__const: 0x9f0
+  __AUTH_CONST.__cfstring: 0x5be0
+  __AUTH_CONST.__objc_const: 0xefd0
+  __AUTH_CONST.__weak_auth_got: 0x218
+  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_arrayobj: 0x2a78
+  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x10c8
   __DATA.__data: 0x8a0
-  __DATA.__bss: 0x2a1
-  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA.__bss: 0x2c1
+  __DATA_DIRTY.__objc_data: 0xc80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1831
-  Symbols:   3867
-  CStrings:  763
+  Functions: 1909
+  Symbols:   4083
+  CStrings:  861
 
Symbols:
+ +[DBFNet intermediateBufferSizesForDescriptor:]
+ +[UBFNet intermediateBufferSizesForDescriptor:]
+ -[Conv12x12Stride4 dispatchWithEncoder:argTable:feed:target:]
+ -[Conv12x12Stride4 internalAllocations]
+ -[Conv1x1FusedBilinear dispatchWithEncoder:argTable:feed:skip:target:]
+ -[Conv1x1FusedBilinear internalAllocations]
+ -[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:target:temporalTex:rnnTex:]
+ -[Conv3x3Stride1 dispatchWithEncoder:argTable:feedU8:feedF16:target:]
+ -[Conv3x3Stride1 executeWithCommandBuffer:feed:target:temporalTex:rnnTex:]
+ -[Conv3x3Stride1 executeWithCommandBuffer:feedU8:feedF16:target:]
+ -[Conv3x3Stride1 prepareImageTensorFeed:]
+ -[ConvKxKStride2 .cxx_construct]
+ -[ConvKxKStride2 .cxx_destruct]
+ -[ConvKxKStride2 computeGrid6x6]
+ -[ConvKxKStride2 computeGridAndTGSize]
+ -[ConvKxKStride2 createBuffers]
+ -[ConvKxKStride2 dispatchWithEncoder:argTable:feed:rowSum:target:]
+ -[ConvKxKStride2 dispatchWithEncoder:argTable:feed:target:]
+ -[ConvKxKStride2 executeWithCommandBuffer:feed:rowSum:target:]
+ -[ConvKxKStride2 executeWithCommandBuffer:feed:target:]
+ -[ConvKxKStride2 executeWithMTL4CommandBuffer:feed:target:]
+ -[ConvKxKStride2 executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[ConvKxKStride2 initWithDescriptor:library:]
+ -[ConvKxKStride2 internalAllocations]
+ -[ConvKxKStride2 mxu3ConvUses4DImageTensor]
+ -[ConvKxKStride2 rowSumOutBuffer]
+ -[ConvKxKStride2 schemeHasZeroPoint]
+ -[ConvKxKStride2 setupMetalWithLibrary:]
+ -[DBFNet .cxx_destruct]
+ -[DBFNet executeWithCommandBuffer:feed:target:]
+ -[DBFNet executeWithCommandBuffer:feed:target:intermediates:]
+ -[DBFNet executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[DBFNet initWithDevice:descriptor:]
+ -[DBFNet initWithDevice:library:descriptor:]
+ -[DBFNet initWithDevice:library:descriptor:residencySet:]
+ -[DBFNet printDescriptor]
+ -[DBFNet setupBuffers]
+ -[DBFNet setupModelWithLibrary:]
+ -[MaxPoolConv .cxx_construct]
+ -[MaxPoolConv .cxx_destruct]
+ -[MaxPoolConv computeGridAndTGSize]
+ -[MaxPoolConv createBuffers]
+ -[MaxPoolConv dispatchWithEncoder:argTable:feed:skip:target:]
+ -[MaxPoolConv executeWithCommandBuffer:feed:skip:target:]
+ -[MaxPoolConv initWithDescriptor:library:]
+ -[MaxPoolConv internalAllocations]
+ -[MaxPoolConv prepareImageTensorFeed:]
+ -[MaxPoolConv scratchBuffer]
+ -[MaxPoolConv setupMetalWithLibrary:]
+ -[UBFNet .cxx_destruct]
+ -[UBFNet executeWithCommandBuffer:feed:target:]
+ -[UBFNet executeWithCommandBuffer:feed:target:intermediates:]
+ -[UBFNet executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[UBFNet initWithDevice:descriptor:]
+ -[UBFNet initWithDevice:library:descriptor:]
+ -[UBFNet initWithDevice:library:descriptor:residencySet:]
+ -[UBFNet printDescriptor]
+ -[UBFNet setupBuffers]
+ -[UBFNet setupModelWithLibrary:]
+ -[tBBRNet executeWithCommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:]
+ -[tBBRNet executeWithCommandBuffer:feed:target:temporalTex:rnnTex:]
+ -[tBBRNet executeWithCommandBuffer:feedU8:feedF16:target:intermediates:]
+ -[tBBRNet executeWithCommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:]
+ -[tBBRNet executeWithMTL4CommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:fence:]
+ -[tBBRNet executeWithMTL4CommandBuffer:feed:target:temporalTex:rnnTex:fence:]
+ -[tBBRNet executeWithMTL4CommandBuffer:feedU8:feedF16:target:fence:]
+ -[tBBRNet executeWithMTL4CommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:fence:]
+ GCC_except_table102
+ GCC_except_table45
+ GCC_except_table61
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ OBJC_IVAR_$_BRNet4_1.mtl4ArgTable_
+ OBJC_IVAR_$_Conv3x3Stride1._bufWeightsFirst16
+ OBJC_IVAR_$_Conv3x3Stride1._bufWeightsLast16
+ OBJC_IVAR_$_ConvKxKStride2._bufBias
+ OBJC_IVAR_$_ConvKxKStride2._bufQsW
+ OBJC_IVAR_$_ConvKxKStride2._bufRowSumOut
+ OBJC_IVAR_$_ConvKxKStride2._bufWeights
+ OBJC_IVAR_$_ConvKxKStride2._bufZP
+ OBJC_IVAR_$_ConvKxKStride2._convPSO
+ OBJC_IVAR_$_ConvKxKStride2._desc
+ OBJC_IVAR_$_ConvKxKStride2._is6x6
+ OBJC_IVAR_$_ConvKxKStride2._isFP16
+ OBJC_IVAR_$_ConvKxKStride2._kTile6x6
+ OBJC_IVAR_$_ConvKxKStride2._mxu_version
+ OBJC_IVAR_$_ConvKxKStride2._nsimdPerTG
+ OBJC_IVAR_$_ConvKxKStride2._produceRowSum
+ OBJC_IVAR_$_ConvKxKStride2._threadsPerGrid
+ OBJC_IVAR_$_ConvKxKStride2._threadsPerThreadgroup
+ OBJC_IVAR_$_ConvKxKStride2._use6x6Gemv
+ OBJC_IVAR_$_ConvKxKStride2._useRowSumIn
+ OBJC_IVAR_$_DBFNet.buf0_
+ OBJC_IVAR_$_DBFNet.buf1_
+ OBJC_IVAR_$_DBFNet.cellD1_
+ OBJC_IVAR_$_DBFNet.cellD2_
+ OBJC_IVAR_$_DBFNet.cellD3_
+ OBJC_IVAR_$_DBFNet.cellE1_
+ OBJC_IVAR_$_DBFNet.cellE2_
+ OBJC_IVAR_$_DBFNet.cellE3_
+ OBJC_IVAR_$_DBFNet.cellE4_
+ OBJC_IVAR_$_DBFNet.desc_
+ OBJC_IVAR_$_DBFNet.device_
+ OBJC_IVAR_$_DBFNet.residencySet_
+ OBJC_IVAR_$_DBFNet.sharedArgTable_
+ OBJC_IVAR_$_DBFNet.skipL2_
+ OBJC_IVAR_$_DBFNet.skipL4_
+ OBJC_IVAR_$_DBFNet.skipL6_
+ OBJC_IVAR_$_MaxPoolConv._bilinearPSO
+ OBJC_IVAR_$_MaxPoolConv._bilinearThreadsPerGrid
+ OBJC_IVAR_$_MaxPoolConv._bilinearThreadsPerTG
+ OBJC_IVAR_$_MaxPoolConv._bufBias
+ OBJC_IVAR_$_MaxPoolConv._bufQsW
+ OBJC_IVAR_$_MaxPoolConv._bufWeights1x1
+ OBJC_IVAR_$_MaxPoolConv._bufWeights3x3
+ OBJC_IVAR_$_MaxPoolConv._bufWeightsHead
+ OBJC_IVAR_$_MaxPoolConv._bufZeroPoints
+ OBJC_IVAR_$_MaxPoolConv._desc
+ OBJC_IVAR_$_MaxPoolConv._hElemsPerTG
+ OBJC_IVAR_$_MaxPoolConv._mxu_version
+ OBJC_IVAR_$_MaxPoolConv._nmatsHW
+ OBJC_IVAR_$_MaxPoolConv._nmatsK
+ OBJC_IVAR_$_MaxPoolConv._pso
+ OBJC_IVAR_$_MaxPoolConv._scratchBuf
+ OBJC_IVAR_$_MaxPoolConv._tWeights1x1
+ OBJC_IVAR_$_MaxPoolConv._tWeights3x3
+ OBJC_IVAR_$_MaxPoolConv._tWeightsHead
+ OBJC_IVAR_$_MaxPoolConv._threadsPerGrid
+ OBJC_IVAR_$_MaxPoolConv._threadsPerThreadgroup
+ OBJC_IVAR_$_MaxPoolConv._wElemsPerTG
+ OBJC_IVAR_$_UBFNet.bottleneck_
+ OBJC_IVAR_$_UBFNet.buf0_
+ OBJC_IVAR_$_UBFNet.buf1_
+ OBJC_IVAR_$_UBFNet.desc_
+ OBJC_IVAR_$_UBFNet.device_
+ OBJC_IVAR_$_UBFNet.e0_
+ OBJC_IVAR_$_UBFNet.e1_
+ OBJC_IVAR_$_UBFNet.e2_
+ OBJC_IVAR_$_UBFNet.e3_
+ OBJC_IVAR_$_UBFNet.e4_
+ OBJC_IVAR_$_UBFNet.head_
+ OBJC_IVAR_$_UBFNet.residencySet_
+ OBJC_IVAR_$_UBFNet.sharedArgTable_
+ OBJC_IVAR_$_UBFNet.skipA_
+ OBJC_IVAR_$_UBFNet.skipB_
+ OBJC_IVAR_$_UBFNet.skipC_
+ OBJC_IVAR_$_UBFNet.u1_
+ OBJC_IVAR_$_UBFNet.u2_
+ OBJC_IVAR_$_UBFNet.u3ab_
+ OBJC_IVAR_$_UBFNet.u3c_
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._dbfnetFused
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._ubfnetFused
+ OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._useFusedDenoiser
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._FusedBRNet
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._mxuVersion
+ OBJC_IVAR_$__M4FXTemporalScalingEffectV4._useFusedBRNet
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._dbfnetFused
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._ubfnetFused
+ OBJC_IVAR_$__MFXTemporalDenoisingScalingEffect._useFusedDenoiser
+ OBJC_IVAR_$_tBBRNet.conv3x3s1_step11_
+ OBJC_IVAR_$_tBBRNet.useSplitInput_
+ _OBJC_CLASS_$_ConvKxKStride2
+ _OBJC_CLASS_$_DBFNet
+ _OBJC_CLASS_$_MaxPoolConv
+ _OBJC_CLASS_$_UBFNet
+ _OBJC_METACLASS_$_ConvKxKStride2
+ _OBJC_METACLASS_$_DBFNet
+ _OBJC_METACLASS_$_MaxPoolConv
+ _OBJC_METACLASS_$_UBFNet
+ _Z32getTemporalDenoiserFusedOverrideb
+ _ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbb
+ _ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbb
+ _ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ _ZN15BRNet_v3_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ __96-[tBBRNet executeWithCommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:]_block_invoke
+ __OBJC_$_CLASS_METHODS_DBFNet
+ __OBJC_$_CLASS_METHODS_UBFNet
+ __OBJC_$_INSTANCE_METHODS_ConvKxKStride2
+ __OBJC_$_INSTANCE_METHODS_DBFNet
+ __OBJC_$_INSTANCE_METHODS_MaxPoolConv
+ __OBJC_$_INSTANCE_METHODS_UBFNet
+ __OBJC_$_INSTANCE_VARIABLES_ConvKxKStride2
+ __OBJC_$_INSTANCE_VARIABLES_DBFNet
+ __OBJC_$_INSTANCE_VARIABLES_MaxPoolConv
+ __OBJC_$_INSTANCE_VARIABLES_UBFNet
+ __OBJC_CLASS_RO_$_ConvKxKStride2
+ __OBJC_CLASS_RO_$_DBFNet
+ __OBJC_CLASS_RO_$_MaxPoolConv
+ __OBJC_CLASS_RO_$_UBFNet
+ __OBJC_METACLASS_RO_$_ConvKxKStride2
+ __OBJC_METACLASS_RO_$_DBFNet
+ __OBJC_METACLASS_RO_$_MaxPoolConv
+ __OBJC_METACLASS_RO_$_UBFNet
+ __Z28getSBBRNetMPSGraphExecutableP6NSDatammP29MPSGraphCompilationDescriptor
+ __Z28getTBBRNetMPSGraphExecutableP6NSDatammP29MPSGraphCompilationDescriptor
+ __Z32getTemporalDenoiserFusedOverrideb
+ __Z32tBBRNet_GenerateConv3x3S1_Step11PU19objcproto9MTLDevice11objc_objectP6NSDatattb
+ __ZL10dbgDumpTexPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLCommandQueue11objc_objectPU21objcproto10MTLTexture11objc_objectPKciS6_
+ __ZN12FrameGenImplI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bbb
+ __ZN12FrameGenImplI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bbb
+ __ZN12FrameGenImplI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bbb
+ __ZN12_GLOBAL__N_116UBF_GenerateHeadEPU19objcproto9MTLDevice11objc_objectP6NSDatattttmm
+ __ZN12_GLOBAL__N_119UBF_GenerateEncoderEPU19objcproto9MTLDevice11objc_objectP6NSDatatttttttmm
+ __ZN12_GLOBAL__N_120UBF_GenerateHeadOnlyEPU19objcproto9MTLDevice11objc_objectP6NSDatatttttbttN3mfx10ActivationES5_mmmm
+ __ZN12_GLOBAL__N_123DBF_GenerateDecoderCellEPU19objcproto9MTLDevice11objc_objectP6NSDatattttttmmmmtmmN3mfx10ActivationE
+ __ZN12_GLOBAL__N_123DBF_GenerateEncoderCellEPU19objcproto9MTLDevice11objc_objectP6NSDatattttttmmmm
+ __ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbb
+ __ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbb
+ __ZN13MFXMLNetwork33runEPU27objcproto16MTLCommandBuffer11objc_objectP12NSDictionaryIP8NSNumberP18MPSGraphTensorDataES6_bb
+ __ZN15BFNet_v1_FilterI10MFXDevice3E12dbgDumpStateEPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLCommandQueue11objc_objectPKci
+ __ZN15BFNet_v1_FilterI10MFXDevice3EC1ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbbb
+ __ZN15BFNet_v1_FilterI10MFXDevice3EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbbb
+ __ZN15BFNet_v1_FilterI10MFXDevice4E12dbgDumpStateEPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLCommandQueue11objc_objectPKci
+ __ZN15BFNet_v1_FilterI10MFXDevice4EC1ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbbb
+ __ZN15BFNet_v1_FilterI10MFXDevice4EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice3E12dbgDumpStateEPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLCommandQueue11objc_objectPKci
+ __ZN15BRNet_v3_FilterI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice4E12dbgDumpStateEPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLCommandQueue11objc_objectPKci
+ __ZN15BRNet_v3_FilterI10MFXDevice4EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbbb
+ __ZN21MaxPoolConvDescriptorD1Ev
+ __ZN21MaxPoolConvDescriptorD2Ev
+ __ZN21MaxPoolConvDescriptoraSERKS_
+ __ZN24Conv3x3Stride1DescriptorC2ERKS_
+ __ZN24ConvKxKStride2DescriptorD1Ev
+ __ZN24ConvKxKStride2DescriptorD2Ev
+ __ZN24ConvKxKStride2DescriptoraSERKS_
+ __ZN3mfx7weights12toBlockMajorIDhEEP6NSDataS3_tttt
+ __ZN3mfx7weights12toBlockMajorIhEEP6NSDataS3_tttt
+ __ZN3mfx7weights12toCInnermostIDhEEP6NSDataS3_tttt
+ __ZN3mfx7weights12toCInnermostIhEEP6NSDataS3_tttt
+ __ZN3mfx7weights23adjustBiasForInputActZpEP6NSDataS2_S2_S2_ttttff
+ __ZZ60-[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]E3s_q
+ __ZZ60-[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:]E5s_enc
+ __ZZ61-[_M4FXTemporalDenoisingScalingEffect encodeToCommandBuffer:]E3s_q
+ __ZZ61-[_M4FXTemporalDenoisingScalingEffect encodeToCommandBuffer:]E5s_enc
+ ___53-[BRNet4_1 executeWithMTL4CommandBuffer:feed:target:]_block_invoke
+ ___57-[DBFNet executeWithMTL4CommandBuffer:feed:target:fence:]_block_invoke
+ ___57-[UBFNet executeWithMTL4CommandBuffer:feed:target:fence:]_block_invoke
+ ___61-[DBFNet executeWithCommandBuffer:feed:target:intermediates:]_block_invoke
+ ___61-[UBFNet executeWithCommandBuffer:feed:target:intermediates:]_block_invoke
+ ___92-[tBBRNet executeWithMTL4CommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:fence:]_block_invoke
+ ___96-[tBBRNet executeWithCommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:]_block_invoke
+ ___ZL41Emit_tBBRNet_nhwc_getMPSGraphExecutable_qP6NSDatammP29MPSGraphCompilationDescriptorb_block_invoke
+ ____ZL41Emit_tBBRNet_nhwc_getMPSGraphExecutable_qP6NSDatammP29MPSGraphCompilationDescriptorb_block_invoke_2
+ ___block_descriptor_40_ea8_32s_e48_v28?0"<MTLCommandBuffer>"8"<MTLTexture>"16i24l
+ ___block_descriptor_40_ea8_32s_e5_v8?0l
+ ___block_descriptor_40_ea8_32s_e78_"MPSGraphTensor"32?0"MPSGraphTensor"8"MPSGraphTensor"16"MPSGraphTensor"24l
+ ___block_descriptor_48_ea8_32s40s_e24_v20?0"<MTLBuffer>"8i16l
+ ___block_descriptor_48_ea8_32s40s_e27_"MPSGraphTensor"24?0Q8Q16l
+ ___block_descriptor_48_ea8_32s40s_e42_"MPSGraphTensor"64?0Q8Q16Q24Q32Q40Q48Q56l
+ ___block_descriptor_56_ea8_32s40s48s_e40_"MPSGraphTensor"16?0"MPSGraphTensor"8l
+ ___chkstk_darwin
+ _fclose
+ _fopen
+ _fwrite
+ _kDBFNetNumIntermediates
+ _kDBFNetStepNames
+ _kUBFNetNumIntermediates
+ _kUBFNetStepNames
+ _matrix_identity_float4x4
+ _mkdir
+ _objc_msgSend$arrayLength
+ _objc_msgSend$computeGrid6x6
+ _objc_msgSend$concatTensors:dimension:name:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
+ _objc_msgSend$dispatchWithEncoder:argTable:feed:rowSum:target:
+ _objc_msgSend$dispatchWithEncoder:argTable:feed:target:temporalTex:rnnTex:
+ _objc_msgSend$dispatchWithEncoder:argTable:feedU8:feedF16:target:
+ _objc_msgSend$executeWithCommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:
+ _objc_msgSend$executeWithCommandBuffer:feed:rowSum:target:
+ _objc_msgSend$executeWithCommandBuffer:feed:target:temporalTex:rnnTex:
+ _objc_msgSend$executeWithCommandBuffer:feedU8:feedF16:target:
+ _objc_msgSend$executeWithCommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:
+ _objc_msgSend$executeWithMTL4CommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:fence:
+ _objc_msgSend$executeWithMTL4CommandBuffer:feed:target:temporalTex:rnnTex:fence:
+ _objc_msgSend$executeWithMTL4CommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:fence:
+ _objc_msgSend$mxu3ConvUses4DImageTensor
+ _objc_msgSend$prepareImageTensorFeed:
+ _objc_msgSend$schemeHasZeroPoint
+ _objc_msgSend$scratchBuffer
+ _objc_msgSend$setAneBondedCompileMode:
+ _snprintf
- -[Conv1x1OutputHead .cxx_construct]
- -[Conv1x1OutputHead .cxx_destruct]
- -[Conv1x1OutputHead SanityCheckKC]
- -[Conv1x1OutputHead _encodeBody:feed:feedTexture:skip:target:]
- -[Conv1x1OutputHead computeGridAndTGSize]
- -[Conv1x1OutputHead createBuffers]
- -[Conv1x1OutputHead dispatchWithEncoder:argTable:feed:skip:target:]
- -[Conv1x1OutputHead dispatchWithEncoder:argTable:feedTexture:skip:target:]
- -[Conv1x1OutputHead executeWithCommandBuffer:feed:skip:target:]
- -[Conv1x1OutputHead executeWithCommandBuffer:feedTexture:skip:target:]
- -[Conv1x1OutputHead executeWithMTL4CommandBuffer:feed:skip:target:fence:]
- -[Conv1x1OutputHead executeWithMTL4CommandBuffer:feedTexture:skip:target:fence:]
- -[Conv1x1OutputHead initWithDescriptor:library:]
- -[Conv1x1OutputHead internalAllocations]
- -[Conv1x1OutputHead setupMetalWithLibrary:]
- GCC_except_table108
- GCC_except_table76
- OBJC_IVAR_$_Conv1x1OutputHead._bufBias
- OBJC_IVAR_$_Conv1x1OutputHead._bufBiasFP16
- OBJC_IVAR_$_Conv1x1OutputHead._bufQsW
- OBJC_IVAR_$_Conv1x1OutputHead._bufWeightZPExpanded
- OBJC_IVAR_$_Conv1x1OutputHead._bufWeights
- OBJC_IVAR_$_Conv1x1OutputHead._bufWeightsFP16
- OBJC_IVAR_$_Conv1x1OutputHead._convPSO
- OBJC_IVAR_$_Conv1x1OutputHead._desc
- OBJC_IVAR_$_Conv1x1OutputHead._mxu_version
- OBJC_IVAR_$_Conv1x1OutputHead._threadsPerGrid
- OBJC_IVAR_$_Conv1x1OutputHead._threadsPerThreadgroup
- OBJC_IVAR_$_tBBRNet.outputHead_
- _OBJC_CLASS_$_Conv1x1OutputHead
- _OBJC_METACLASS_$_Conv1x1OutputHead
- _ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbbb
- _ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbbb
- _ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- _ZN15BRNet_v3_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- __OBJC_$_INSTANCE_METHODS_Conv1x1OutputHead
- __OBJC_$_INSTANCE_VARIABLES_Conv1x1OutputHead
- __OBJC_CLASS_RO_$_Conv1x1OutputHead
- __OBJC_METACLASS_RO_$_Conv1x1OutputHead
- __Z26tBBRNet_GenerateOutputHeadPU19objcproto9MTLDevice11objc_objectP6NSDatatt
- __Z28getSBBRNetMPSGraphExecutableP6NSDatammP29MPSGraphCompilationDescriptorb
- __Z28getTBBRNetMPSGraphExecutableP6NSDatammP29MPSGraphCompilationDescriptorb
- __ZL42Emit_tBBRNet_nhwc_getMPSGraphExecutable_nqP6NSDatammP29MPSGraphCompilationDescriptorb
- __ZN12FrameGenImplI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bb
- __ZN12FrameGenImplI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bb
- __ZN12FrameGenImplI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectyyyy14MTLPixelFormatS5_bb
- __ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbbb
- __ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbbb
- __ZN13MFXMLNetwork43runEPU28objcproto17MTL4CommandBuffer11objc_objectR10MFXDevice4RK14MFXTensorView4S6_PU18objcproto8MTLFence11objc_object
- __ZN13MFXMLNetwork4C2EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectP8NSStringiiiPU26objcproto15MTLResidencySet11objc_object
- __ZN15BFNet_v1_FilterI10MFXDevice3EC1ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbb
- __ZN15BFNet_v1_FilterI10MFXDevice3EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbb
- __ZN15BFNet_v1_FilterI10MFXDevice4EC1ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbb
- __ZN15BFNet_v1_FilterI10MFXDevice4EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiiiRK16DBFNetDescriptorbbbb
- __ZN15BRNet_v3_FilterI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- __ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- __ZN15BRNet_v3_FilterI10MFXDevice4EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- __ZN15BRNet_v3_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbbbbb
- __ZN24Conv3x3Stride1DescriptorC1ERKS_
- __ZN27Conv1x1OutputHeadDescriptorC2ERKS_
- __ZN27Conv1x1OutputHeadDescriptorD2Ev
- __ZN27Conv1x1OutputHeadDescriptoraSERKS_
- __ZN27Conv3x3SigmoidD2SDescriptorD1Ev
- __ZZL41Emit_tBBRNet_nhwc_getMPSGraphExecutable_qP6NSDatammP29MPSGraphCompilationDescriptorbE19kInputDequantScales
- ___62-[tBBRNet executeWithCommandBuffer:feed:target:intermediates:]_block_invoke
- _objc_msgSend$_encodeBody:feed:feedTexture:skip:target:
- _objc_msgSend$executeWithMTL4CommandBuffer:feed:skip:target:
- _objc_msgSend$leakyReLUWithTensor:alphaTensor:name:
- _objc_msgSend$size
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/ConvKxKStride2/ConvKxKStride2.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/DBFNet.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/MaxPoolConv/MaxPoolConv.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/SBBRNet_MLP/../Common/common_host.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/UBFNet.mm"
+ "/var/root/dbg_temporal"
+ "/var/root/dbg_temporal/%s_f%02d_%s.bin"
+ "@\"MPSGraphTensor\"16@?0@\"MPSGraphTensor\"8"
+ "@\"MPSGraphTensor\"24@?0Q8Q16"
+ "@\"MPSGraphTensor\"32@?0@\"MPSGraphTensor\"8@\"MPSGraphTensor\"16@\"MPSGraphTensor\"24"
+ "@\"MPSGraphTensor\"64@?0Q8Q16Q24Q32Q40Q48Q56"
+ "BFNet3_Fused: DBFNet (Metal4) init failed; filter is already in fused (fc-15 NHWC) layout — cannot safely fall back to MPSGraph. Failing scaler creation."
+ "BFNet3_Fused: DBFNet init failed; filter is already in fused (fc-15 NHWC) layout — cannot safely fall back to MPSGraph. Failing scaler creation."
+ "BFNet3_Fused: UBFNet (Metal4) init failed; filter is already in fused (fc-15 NHWC) layout — cannot safely fall back to MPSGraph. Failing scaler creation."
+ "BFNet3_Fused: UBFNet init failed; filter is already in fused (fc-15 NHWC) layout — cannot safely fall back to MPSGraph. Failing scaler creation."
+ "BilinearUpsample2xSkipF16"
+ "Conv3x3Stride1Enc0FQSplit"
+ "ConvKxKStride2MXU2_K3x3_F16"
+ "ConvKxKStride2MXU2_K6x6"
+ "ConvKxKStride2MXU3_K3x3_F16_K%u_C%u"
+ "ConvKxKStride2MXU3_K6x6_F16_CONV2D_K16_C8_E0"
+ "ConvKxKStride2MXU3_K6x6_F16_CONV2D_K32_C8"
+ "ConvKxKStride2MXU3_K6x6_F16_K%u_C32"
+ "ConvKxKStride2_K3x3_F16"
+ "ConvKxKStride2_K6x6"
+ "DBFNet weight file too small: %zu bytes (expected >= %zu)"
+ "Denoiser fused path is overridden from %d to %d using Env MTLFX_TEMPORAL_DENOISER_FUSED"
+ "E0"
+ "E1"
+ "E2"
+ "E3"
+ "E4_bn"
+ "Failed to allocate DBFNet internal buffer"
+ "Failed to allocate MaxPoolConv bilinear scratch"
+ "Failed to allocate UBFNet internal buffer"
+ "Failed to allocate enc0 split weight buffers"
+ "Failed to create BRNet argument table"
+ "Failed to create DBFNet argument table: %@"
+ "Failed to create MaxPoolConv PSO: %@"
+ "Failed to create MaxPoolConv bilinear PSO: %@"
+ "Failed to create UBFNet argument table: %@"
+ "Failed to init DBFNet cell D1"
+ "Failed to init DBFNet cell D2"
+ "Failed to init DBFNet cell D3"
+ "Failed to init DBFNet cell E1"
+ "Failed to init DBFNet cell E2"
+ "Failed to init DBFNet cell E3"
+ "Failed to init DBFNet cell E4"
+ "Failed to init UBFNet E0"
+ "Failed to init UBFNet E1"
+ "Failed to init UBFNet E2"
+ "Failed to init UBFNet E3"
+ "Failed to init UBFNet E4"
+ "Failed to init UBFNet U1"
+ "Failed to init UBFNet U2"
+ "Failed to init UBFNet U3a/b"
+ "Failed to init UBFNet U3c"
+ "Failed to init UBFNet bottleneck"
+ "Failed to init UBFNet head"
+ "Failed to initialize network output layer 11"
+ "Failed to load DBFNet model data"
+ "Failed to load UBFNet model data"
+ "I"
+ "Invalid split input or output buffer"
+ "K%ux%u"
+ "MFX_DUMP_TEMPORAL"
+ "MTL3"
+ "MTL4"
+ "MTLFX_FRC_DISOCC_BLEND"
+ "MTLFX_TEMPORAL_DENOISER_FUSED"
+ "MaxPoolConv"
+ "MaxPoolConv: Biases NSData too small (%lu < %lu bytes); zero-filling"
+ "MaxPoolConv: failed to create encoder"
+ "MaxPoolConv: invalid input or output buffer"
+ "MaxPoolConv: unsupported MXU version %u"
+ "MetalFX_Temporal_FusedNetwork_Signal"
+ "MetalFX_Temporal_FusedNetwork_Wait"
+ "U1"
+ "U2"
+ "U3"
+ "UBFNet weight file too small: %zu bytes (expected >= %zu)"
+ "[MFX_DUMP_TEMPORAL] %s f%d %-22s %llux%llu fmt=%lu fnv=%016llx"
+ "[MetalFX] UBFNet fused-MXU path ACTIVE (Metal3; NHWC-native)"
+ "[MetalFX] UBFNet fused-MXU path ACTIVE (Metal4; NHWC-native)"
+ "[MetalFX] dBFNet fused-MXU path ACTIVE (Metal3; NHWC-native)"
+ "[MetalFX] dBFNet fused-MXU path ACTIVE (Metal4; NHWC-native)"
+ "bottleneck_B"
+ "cell_D1"
+ "cell_D2"
+ "cell_D3"
+ "cell_L1L2"
+ "cell_L3L4"
+ "cell_L5L6"
+ "cell_L7L8_bn"
+ "conv1"
+ "conv10"
+ "conv11"
+ "conv1_enc0"
+ "conv2"
+ "conv2_enc1"
+ "conv3"
+ "conv3_enc2"
+ "conv4"
+ "conv4_enc3"
+ "conv5"
+ "conv5_bn"
+ "conv6"
+ "conv7"
+ "conv8"
+ "conv9"
+ "dbf_demodColor0"
+ "dbf_demodColor1"
+ "dbf_demodY0"
+ "dbf_demodY1"
+ "dbf_frameCnt0"
+ "dbf_frameCnt1"
+ "dbf_history"
+ "dbf_mean0"
+ "dbf_mean1"
+ "dbf_mirror0"
+ "dbf_mirror1"
+ "dbf_shortMean0"
+ "dbf_shortMean1"
+ "depthToSpace"
+ "deqW_%lu"
+ "pF16"
+ "pU8"
+ "pU8_to_f16"
+ "resize1"
+ "resize2"
+ "resize3"
+ "skip1"
+ "skip2"
+ "skip3"
+ "tail_sigmoid_all"
+ "u8_dequant"
+ "v20@?0@\"<MTLBuffer>\"8i16"
+ "v28@?0@\"<MTLCommandBuffer>\"8@\"<MTLTexture>\"16i24"
+ "v3_EMA0"
+ "v3_EMA1"
+ "v3_EMTV0"
+ "v3_EMTV1"
+ "v3_aabbMax"
+ "v3_aabbMin"
+ "v3_flowAdjHist"
+ "v3_outTemporal"
+ "v3_sampleCnt0"
+ "v3_sampleCnt1"
+ "v3_sampleEMA0"
+ "v3_sampleEMA1"
+ "v3_sampleEMTV0"
+ "v3_sampleEMTV1"
+ "wb"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1OutputHead/../Common/common_host.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1OutputHead/Conv1x1OutputHead.mm"
- "Conv1x1OutputHead"
- "Conv3x3Stride1Enc0FQ"
- "Failed to initialize network output layer"
- "ML network mtlpackage error: %@"
- "ML network pipeline error: %@"
- "bias0"
- "bias1"
- "bias2"
- "bias3"
- "bias_out"
- "dec0"
- "dec1_0"
- "dec1_2"
- "dec2_0"
- "dec2_2"
- "dec3_0"
- "emit_sbbrnet_nhwc_nq_constants.dat"
- "enc0"
- "enc1"
- "enc2"
- "enc3"
- "nmatsHW must be 1, 2, or 4 (got %d)"
- "oh_in"
- "oh_l0_dec3_2"
- "oh_l1_up_0"
- "tensor15"
- "tensor16"
- "tensor17"
- "tensor18"
- "tensor183_sigmoid_all"
- "tensor19"
- "tensor20"
- "tensor21"
- "tensor22"
- "tensor23"
- "tensor24"
- "tensor25"
- "tensor26"
- "tensor27"
- "tensor28"
- "tensor29"
- "tensor30"
- "tensor31"
- "tensor35"
- "tensor36_biasReshape"
- "tensor39_biasReshape"
- "tensor42_biasReshape"
- "tensor49_biasReshape"
- "tensor57_biasReshape"
- "tensor60_biasReshape"
- "tensor65_biasReshape"
- "tensor68_biasReshape"
- "tensor79_biasReshape"
```
