## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/Versions/A/MetalFX`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-40.5.0.0.0
-  __TEXT.__text: 0x78c14
-  __TEXT.__objc_methlist: 0x512c
-  __TEXT.__const: 0x618
-  __TEXT.__gcc_except_tab: 0xb1c4
-  __TEXT.__cstring: 0x5032
+40.6.0.0.0
+  __TEXT.__text: 0x7f020
+  __TEXT.__objc_methlist: 0x534c
+  __TEXT.__const: 0x624
+  __TEXT.__gcc_except_tab: 0xbbf8
+  __TEXT.__cstring: 0x525e
   __TEXT.__ustring: 0x186
-  __TEXT.__unwind_info: 0x1320
+  __TEXT.__unwind_info: 0x1508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1298
+  __DATA_CONST.__objc_selrefs: 0x1348
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x33e8
-  __DATA_CONST.__got: 0x290
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x53a0
-  __AUTH_CONST.__objc_const: 0xe0f0
-  __AUTH_CONST.__weak_auth_got: 0x1a0
-  __AUTH_CONST.__objc_intobj: 0x348
+  __DATA_CONST.__got: 0x2a0
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0x5540
+  __AUTH_CONST.__objc_const: 0xe468
+  __AUTH_CONST.__weak_auth_got: 0x1f8
+  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x35e8
   __AUTH_CONST.__auth_got: 0x298
-  __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x1028
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xf94
   __DATA.__data: 0x8a0
-  __DATA.__bss: 0x298
+  __DATA.__bss: 0x2a1
+  __DATA_DIRTY.__objc_data: 0xcd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1745
-  Symbols:   3793
-  CStrings:  746
+  Functions: 1831
+  Symbols:   3867
+  CStrings:  763
 
Symbols:
+ -[Conv1x1OutputHead dispatchWithEncoder:argTable:feed:skip:target:]
+ -[Conv1x1OutputHead dispatchWithEncoder:argTable:feedTexture:skip:target:]
+ -[Conv1x1OutputHead executeWithMTL4CommandBuffer:feed:skip:target:fence:]
+ -[Conv1x1OutputHead executeWithMTL4CommandBuffer:feedTexture:skip:target:fence:]
+ -[Conv1x1OutputHead internalAllocations]
+ -[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:skip:target:]
+ -[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:skip:targetTexture:]
+ -[Conv3x3Stride1 dispatchWithEncoder:argTable:feedTexture:skip:target:]
+ -[Conv3x3Stride1 executeWithMTL4CommandBuffer:feed:skip:target:fence:]
+ -[Conv3x3Stride1 executeWithMTL4CommandBuffer:feed:skip:targetTexture:fence:]
+ -[Conv3x3Stride1 executeWithMTL4CommandBuffer:feedTexture:skip:target:fence:]
+ -[Conv3x3Stride1 internalAllocations]
+ -[Conv3x3Stride2 dispatchWithEncoder:argTable:feed:target:]
+ -[Conv3x3Stride2 executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[Conv3x3Stride2 internalAllocations]
+ -[SBBRNet_MLP executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[SBBRNet_MLP internalAllocations]
+ -[_M4FXTemporalScalingEffectBBR .cxx_construct]
+ -[_M4FXTemporalScalingEffectBBR .cxx_destruct]
+ -[_M4FXTemporalScalingEffectBBR colorTextureBarrierStages]
+ -[_M4FXTemporalScalingEffectBBR dilatedMotionVectors]
+ -[_M4FXTemporalScalingEffectBBR encodeToCommandBuffer:]
+ -[_M4FXTemporalScalingEffectBBR executionMode]
+ -[_M4FXTemporalScalingEffectBBR initWithDevice:descriptor:compiler:history:]
+ -[_M4FXTemporalScalingEffectBBR outputTextureBarrierStages]
+ -[_M4FXTemporalScalingEffectBBR setColorTextureBarrierStages:]
+ -[_M4FXTemporalScalingEffectBBR setOutputTextureBarrierStages:]
+ -[_MFXFrameInterpolatorEffect .cxx_construct]
+ -[_MFXTemporalScalingEffectBase .cxx_destruct]
+ -[_MFXTemporalScalingEffectBase _emitTelemetry:forDevice:]
+ -[_MFXTemporalScalingEffectBase colorContentOffsetX]
+ -[_MFXTemporalScalingEffectBase colorContentOffsetY]
+ -[_MFXTemporalScalingEffectBase colorTextureFormat]
+ -[_MFXTemporalScalingEffectBase colorTextureUsage]
+ -[_MFXTemporalScalingEffectBase colorTexture]
+ -[_MFXTemporalScalingEffectBase currentViewToClipMatrix]
+ -[_MFXTemporalScalingEffectBase currentWorldToViewMatrix]
+ -[_MFXTemporalScalingEffectBase debugTexture]
+ -[_MFXTemporalScalingEffectBase depthContentOffsetX]
+ -[_MFXTemporalScalingEffectBase depthContentOffsetY]
+ -[_MFXTemporalScalingEffectBase depthReversed]
+ -[_MFXTemporalScalingEffectBase depthTextureFormat]
+ -[_MFXTemporalScalingEffectBase depthTextureUsage]
+ -[_MFXTemporalScalingEffectBase depthTexture]
+ -[_MFXTemporalScalingEffectBase exposureTexture]
+ -[_MFXTemporalScalingEffectBase fence]
+ -[_MFXTemporalScalingEffectBase initWithDevice:descriptor:]
+ -[_MFXTemporalScalingEffectBase inputContentHeight]
+ -[_MFXTemporalScalingEffectBase inputContentMaxScale]
+ -[_MFXTemporalScalingEffectBase inputContentMinScale]
+ -[_MFXTemporalScalingEffectBase inputContentWidth]
+ -[_MFXTemporalScalingEffectBase inputHeight]
+ -[_MFXTemporalScalingEffectBase inputWidth]
+ -[_MFXTemporalScalingEffectBase jitterOffsetX]
+ -[_MFXTemporalScalingEffectBase jitterOffsetY]
+ -[_MFXTemporalScalingEffectBase jitterOffset]
+ -[_MFXTemporalScalingEffectBase motionContentOffsetX]
+ -[_MFXTemporalScalingEffectBase motionContentOffsetY]
+ -[_MFXTemporalScalingEffectBase motionTextureFormat]
+ -[_MFXTemporalScalingEffectBase motionTextureUsage]
+ -[_MFXTemporalScalingEffectBase motionTexture]
+ -[_MFXTemporalScalingEffectBase motionVectorScaleX]
+ -[_MFXTemporalScalingEffectBase motionVectorScaleY]
+ -[_MFXTemporalScalingEffectBase motionVectorScale]
+ -[_MFXTemporalScalingEffectBase outputHeight]
+ -[_MFXTemporalScalingEffectBase outputOffsetX]
+ -[_MFXTemporalScalingEffectBase outputOffsetY]
+ -[_MFXTemporalScalingEffectBase outputTextureFormat]
+ -[_MFXTemporalScalingEffectBase outputTextureUsage]
+ -[_MFXTemporalScalingEffectBase outputTexture]
+ -[_MFXTemporalScalingEffectBase outputWidth]
+ -[_MFXTemporalScalingEffectBase preExposure]
+ -[_MFXTemporalScalingEffectBase previousJitterOffset]
+ -[_MFXTemporalScalingEffectBase previousViewToClipMatrix]
+ -[_MFXTemporalScalingEffectBase previousWorldToViewMatrix]
+ -[_MFXTemporalScalingEffectBase reactiveMaskContentOffsetX]
+ -[_MFXTemporalScalingEffectBase reactiveMaskContentOffsetY]
+ -[_MFXTemporalScalingEffectBase reactiveMaskTextureFormat]
+ -[_MFXTemporalScalingEffectBase reactiveMaskTextureUsage]
+ -[_MFXTemporalScalingEffectBase reactiveMaskTexture]
+ -[_MFXTemporalScalingEffectBase reactiveTextureUsage]
+ -[_MFXTemporalScalingEffectBase reset]
+ -[_MFXTemporalScalingEffectBase setColorContentOffsetX:]
+ -[_MFXTemporalScalingEffectBase setColorContentOffsetY:]
+ -[_MFXTemporalScalingEffectBase setColorTexture:]
+ -[_MFXTemporalScalingEffectBase setColorTextureFormat:]
+ -[_MFXTemporalScalingEffectBase setColorTextureUsage:]
+ -[_MFXTemporalScalingEffectBase setCurrentViewToClipMatrix:]
+ -[_MFXTemporalScalingEffectBase setCurrentWorldToViewMatrix:]
+ -[_MFXTemporalScalingEffectBase setDebugTexture:]
+ -[_MFXTemporalScalingEffectBase setDepthContentOffsetX:]
+ -[_MFXTemporalScalingEffectBase setDepthContentOffsetY:]
+ -[_MFXTemporalScalingEffectBase setDepthReversed:]
+ -[_MFXTemporalScalingEffectBase setDepthTexture:]
+ -[_MFXTemporalScalingEffectBase setDepthTextureFormat:]
+ -[_MFXTemporalScalingEffectBase setDepthTextureUsage:]
+ -[_MFXTemporalScalingEffectBase setExposureTexture:]
+ -[_MFXTemporalScalingEffectBase setFence:]
+ -[_MFXTemporalScalingEffectBase setInputContentHeight:]
+ -[_MFXTemporalScalingEffectBase setInputContentMaxScale:]
+ -[_MFXTemporalScalingEffectBase setInputContentMinScale:]
+ -[_MFXTemporalScalingEffectBase setInputContentWidth:]
+ -[_MFXTemporalScalingEffectBase setInputHeight:]
+ -[_MFXTemporalScalingEffectBase setInputWidth:]
+ -[_MFXTemporalScalingEffectBase setJitterOffset:]
+ -[_MFXTemporalScalingEffectBase setJitterOffsetX:]
+ -[_MFXTemporalScalingEffectBase setJitterOffsetY:]
+ -[_MFXTemporalScalingEffectBase setMotionContentOffsetX:]
+ -[_MFXTemporalScalingEffectBase setMotionContentOffsetY:]
+ -[_MFXTemporalScalingEffectBase setMotionTexture:]
+ -[_MFXTemporalScalingEffectBase setMotionTextureFormat:]
+ -[_MFXTemporalScalingEffectBase setMotionTextureUsage:]
+ -[_MFXTemporalScalingEffectBase setMotionVectorScale:]
+ -[_MFXTemporalScalingEffectBase setMotionVectorScaleX:]
+ -[_MFXTemporalScalingEffectBase setMotionVectorScaleY:]
+ -[_MFXTemporalScalingEffectBase setOutputHeight:]
+ -[_MFXTemporalScalingEffectBase setOutputOffsetX:]
+ -[_MFXTemporalScalingEffectBase setOutputOffsetY:]
+ -[_MFXTemporalScalingEffectBase setOutputTexture:]
+ -[_MFXTemporalScalingEffectBase setOutputTextureFormat:]
+ -[_MFXTemporalScalingEffectBase setOutputTextureUsage:]
+ -[_MFXTemporalScalingEffectBase setOutputWidth:]
+ -[_MFXTemporalScalingEffectBase setPreExposure:]
+ -[_MFXTemporalScalingEffectBase setPreviousJitterOffset:]
+ -[_MFXTemporalScalingEffectBase setPreviousViewToClipMatrix:]
+ -[_MFXTemporalScalingEffectBase setPreviousWorldToViewMatrix:]
+ -[_MFXTemporalScalingEffectBase setReactiveMaskContentOffsetX:]
+ -[_MFXTemporalScalingEffectBase setReactiveMaskContentOffsetY:]
+ -[_MFXTemporalScalingEffectBase setReactiveMaskTexture:]
+ -[_MFXTemporalScalingEffectBase setReactiveMaskTextureFormat:]
+ -[_MFXTemporalScalingEffectBase setReactiveTextureUsage:]
+ -[_MFXTemporalScalingEffectBase setReset:]
+ -[sBBRNet executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[sBBRNet initWithDevice:library:descriptor:residencySet:]
+ -[tBBRNet executeWithMTL4CommandBuffer:feed:target:fence:]
+ -[tBBRNet initWithDevice:library:descriptor:residencySet:]
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ OBJC_IVAR_$__M4FXTemporalScalingEffectBBR._filter
+ OBJC_IVAR_$__MFXFrameInterpolatorEffect._mfxDevice
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._autoExposureEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._colorContentOffsetX
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._colorContentOffsetY
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._colorTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._colorTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._colorTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._currentViewToClipMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._currentWorldToViewMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._debugTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._depthContentOffsetX
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._depthContentOffsetY
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._depthTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._depthTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._depthTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._exposureTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._fence
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputContentHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputContentMaxScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputContentMinScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputContentWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._inputWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._jitterOffset
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._jitteredMotionVectorsEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._linelockingEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionContentOffsetX
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionContentOffsetY
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._motionVectorScale
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputHeight
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputOffsetX
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputOffsetY
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputResolutionMotionVectorsEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._outputWidth
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._preExposure
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._previousJitterOffset
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._previousViewToClipMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._previousWorldToViewMatrix
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveMaskContentOffsetX
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveMaskContentOffsetY
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveMaskEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveMaskTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveMaskTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reactiveTextureUsage
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reset
+ OBJC_IVAR_$__MFXTemporalScalingEffectBase._reversedDepth
+ OBJC_IVAR_$_tBBRNet.residencySet_
+ OBJC_IVAR_$_tBBRNet.sharedArgTable_
+ _OBJC_CLASS_$_MPSGraphExecutable
+ _OBJC_CLASS_$__M4FXTemporalScalingEffectBBR
+ _OBJC_CLASS_$__MFXTemporalScalingEffectBase
+ _OBJC_METACLASS_$__M4FXTemporalScalingEffectBBR
+ _OBJC_METACLASS_$__MFXTemporalScalingEffectBase
+ _OUTLINED_FUNCTION_5
+ _ZN13BBRNet_FilterI10MFXDevice3E14validateInputsEv
+ _ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbbb
+ _ZN13BBRNet_FilterI10MFXDevice4E14validateInputsEv
+ _ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbbb
+ __OBJC_$_INSTANCE_METHODS__M4FXTemporalScalingEffectBBR
+ __OBJC_$_INSTANCE_METHODS__MFXTemporalScalingEffectBase
+ __OBJC_$_INSTANCE_VARIABLES__M4FXTemporalScalingEffectBBR
+ __OBJC_$_INSTANCE_VARIABLES__MFXTemporalScalingEffectBase
+ __OBJC_$_PROP_LIST__M4FXTemporalScalingEffectBBR
+ __OBJC_$_PROP_LIST__MFXTemporalScalingEffectBase
+ __OBJC_CLASS_PROTOCOLS_$__M4FXTemporalScalingEffectBBR
+ __OBJC_CLASS_RO_$__M4FXTemporalScalingEffectBBR
+ __OBJC_CLASS_RO_$__MFXTemporalScalingEffectBase
+ __OBJC_METACLASS_RO_$__M4FXTemporalScalingEffectBBR
+ __OBJC_METACLASS_RO_$__MFXTemporalScalingEffectBase
+ __ZL26getDefaultBBRNetDescriptor13BBRNetVersionii
+ __ZN10MFXDevice314computeEncoderEPU27objcproto16MTLCommandBuffer11objc_object
+ __ZN10MFXDevice318getTransientBufferEPKvm
+ __ZN10MFXDevice329emitSignPostForComputeEncoderEyy
+ __ZN10MFXDevice3C2EPU19objcproto9MTLDevice11objc_objectb
+ __ZN13BBRNet_FilterI10MFXDevice3E10encodePostER18MFXComputeEncoder319MFXTransientBuffer3
+ __ZN13BBRNet_FilterI10MFXDevice3E14validateInputsEv
+ __ZN13BBRNet_FilterI10MFXDevice3E17emitTraceSignpostEy
+ __ZN13BBRNet_FilterI10MFXDevice3E17updateBRNetParamsEv
+ __ZN13BBRNet_FilterI10MFXDevice3E29setOutputTextureBarrierStagesEm
+ __ZN13BBRNet_FilterI10MFXDevice3E4initEPU21objcproto10MTLTexture11objc_objectbbb
+ __ZN13BBRNet_FilterI10MFXDevice3E6encodeEPU27objcproto16MTLCommandBuffer11objc_objectybb
+ __ZN13BBRNet_FilterI10MFXDevice3E9encodeMidER18MFXComputeEncoder319MFXTransientBuffer3
+ __ZN13BBRNet_FilterI10MFXDevice3E9encodePreER18MFXComputeEncoder319MFXTransientBuffer3
+ __ZN13BBRNet_FilterI10MFXDevice3EC1ENSt3__110unique_ptrIS0_NS2_14default_deleteIS0_EEEEP29_MFXTemporalScalingEffectBase
+ __ZN13BBRNet_FilterI10MFXDevice3EC2ENSt3__110unique_ptrIS0_NS2_14default_deleteIS0_EEEEP29_MFXTemporalScalingEffectBase
+ __ZN13BBRNet_FilterI10MFXDevice4E10encodePostER18MFXComputeEncoder4y
+ __ZN13BBRNet_FilterI10MFXDevice4E14validateInputsEv
+ __ZN13BBRNet_FilterI10MFXDevice4E17emitTraceSignpostEy
+ __ZN13BBRNet_FilterI10MFXDevice4E17updateBRNetParamsEv
+ __ZN13BBRNet_FilterI10MFXDevice4E29setOutputTextureBarrierStagesEm
+ __ZN13BBRNet_FilterI10MFXDevice4E4initEPU21objcproto10MTLTexture11objc_objectbbb
+ __ZN13BBRNet_FilterI10MFXDevice4E6encodeEPU28objcproto17MTL4CommandBuffer11objc_objectybb
+ __ZN13BBRNet_FilterI10MFXDevice4E9encodeMidER18MFXComputeEncoder4y
+ __ZN13BBRNet_FilterI10MFXDevice4E9encodePreER18MFXComputeEncoder4y
+ __ZN13BBRNet_FilterI10MFXDevice4EC1ENSt3__110unique_ptrIS0_NS2_14default_deleteIS0_EEEEP29_MFXTemporalScalingEffectBase
+ __ZN13BBRNet_FilterI10MFXDevice4EC2ENSt3__110unique_ptrIS0_NS2_14default_deleteIS0_EEEEP29_MFXTemporalScalingEffectBase
+ __ZN13MFXMLNetwork316activeExecutableEb
+ __ZN13MFXMLNetwork33runEPU26objcproto15MTLCommandQueue11objc_objectP18MPSGraphTensorDataS3_bbPU25objcproto14MTLSharedEvent11objc_objectyy
+ __ZN13MFXMLNetwork33runEPU27objcproto16MTLCommandBuffer11objc_objectP18MPSGraphTensorDataS3_bb
+ __ZN13MFXMLNetwork37prewarmEPU26objcproto15MTLCommandQueue11objc_objectRK14MFXTensorView3S4_by
+ __ZN13MFXMLNetwork3C2EPU19objcproto9MTLDevice11objc_objectP8NSStringiii
+ __ZN13MFXMLNetwork3D2Ev
+ __ZN13MFXMLNetwork43runEPU28objcproto17MTL4CommandBuffer11objc_objectR10MFXDevice4RK14MFXTensorView4S6_PU18objcproto8MTLFence11objc_object
+ __ZN13MFXMLNetwork4C2EPU19objcproto9MTLDevice11objc_objectPU23objcproto12MTL4Compiler11objc_objectP8NSStringiiiPU26objcproto15MTLResidencySet11objc_object
+ __ZN14MFXTensorView3C2EPU19objcproto9MTLBuffer11objc_objectiiib29MPSGraphTensorNamedDataLayoutPU26objcproto15MTLResidencySet11objc_object
+ __ZN14MFXTensorView4C2EPU19objcproto9MTLBuffer11objc_objectiiib29MPSGraphTensorNamedDataLayoutPU26objcproto15MTLResidencySet11objc_object
+ __ZN17MFXRenderEncoder322setTileTransientBufferE19MFXTransientBuffer3j
+ __ZN18MFXComputeEncoder318setTransientBufferE19MFXTransientBuffer3j
+ __ZNK13BBRNet_FilterI10MFXDevice3E26outputTextureBarrierStagesEv
+ __ZNK13BBRNet_FilterI10MFXDevice4E26outputTextureBarrierStagesEv
+ __ZNSt3__110unique_ptrI10MFXDevice3NS_14default_deleteIS1_EEE5resetB9nqe220106EPS1_
+ __ZNSt3__110unique_ptrI10MFXDevice3NS_14default_deleteIS1_EEED1B9nqe220106Ev
+ __ZNSt3__110unique_ptrI10MFXDevice4NS_14default_deleteIS1_EEED1B9nqe220106Ev
+ __ZNSt3__110unique_ptrI13BBRNet_FilterI10MFXDevice3ENS_14default_deleteIS3_EEE5resetB9nqe220106EPS3_
+ __ZNSt3__110unique_ptrI13BBRNet_FilterI10MFXDevice4ENS_14default_deleteIS3_EEE5resetB9nqe220106EPS3_
+ ___58-[_MFXTemporalScalingEffectBase _emitTelemetry:forDevice:]_block_invoke
+ ____ZN13MFXMLNetwork37prewarmEPU26objcproto15MTLCommandQueue11objc_objectRK14MFXTensorView3S4_by_block_invoke
+ ___block_descriptor_104_ea8_32s40s_e26_"NSMutableDictionary"8?0l
+ ___block_descriptor_64_ea8_32s40s48s_e5_v8?0l
+ ___copy_helper_block_ea8_32s40s48s
+ ___destroy_helper_block_ea8_32s40s48s
+ _objc_msgSend$array
+ _objc_msgSend$dispatchWithEncoder:argTable:feed:skip:target:
+ _objc_msgSend$dispatchWithEncoder:argTable:feed:skip:targetTexture:
+ _objc_msgSend$dispatchWithEncoder:argTable:feed:target:
+ _objc_msgSend$dispatchWithEncoder:argTable:feedTexture:skip:target:
+ _objc_msgSend$executeWithMTL4CommandBuffer:feed:target:fence:
+ _objc_msgSend$initWithDevice:library:descriptor:residencySet:
+ _objc_msgSend$initWithMPSGraphPackageAtURL:compilationDescriptor:
+ _objc_msgSend$internalAllocations
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$size
+ _objc_msgSend$specializeWithDevice:inputTypes:compilationDescriptor:
- -[Conv1x1OutputHead executeWithMTL4CommandBuffer:feed:skip:target:]
- -[Conv3x3Stride1 executeWithMTL4CommandBuffer:feed:skip:target:]
- -[SBBRNet_MLP executeWithMTL4CommandBuffer:feed:target:]
- -[_MFXTemporalScalingEffectBBR colorContentOffsetX]
- -[_MFXTemporalScalingEffectBBR colorContentOffsetY]
- -[_MFXTemporalScalingEffectBBR colorTextureFormat]
- -[_MFXTemporalScalingEffectBBR colorTextureUsage]
- -[_MFXTemporalScalingEffectBBR colorTexture]
- -[_MFXTemporalScalingEffectBBR currentViewToClipMatrix]
- -[_MFXTemporalScalingEffectBBR currentWorldToViewMatrix]
- -[_MFXTemporalScalingEffectBBR dealloc]
- -[_MFXTemporalScalingEffectBBR debugTexture]
- -[_MFXTemporalScalingEffectBBR depthContentOffsetX]
- -[_MFXTemporalScalingEffectBBR depthContentOffsetY]
- -[_MFXTemporalScalingEffectBBR depthTextureFormat]
- -[_MFXTemporalScalingEffectBBR depthTextureUsage]
- -[_MFXTemporalScalingEffectBBR depthTexture]
- -[_MFXTemporalScalingEffectBBR exposureTexture]
- -[_MFXTemporalScalingEffectBBR fence]
- -[_MFXTemporalScalingEffectBBR inputContentHeight]
- -[_MFXTemporalScalingEffectBBR inputContentMaxScale]
- -[_MFXTemporalScalingEffectBBR inputContentMinScale]
- -[_MFXTemporalScalingEffectBBR inputContentWidth]
- -[_MFXTemporalScalingEffectBBR inputHeight]
- -[_MFXTemporalScalingEffectBBR inputWidth]
- -[_MFXTemporalScalingEffectBBR isDepthReversed]
- -[_MFXTemporalScalingEffectBBR jitterOffsetX]
- -[_MFXTemporalScalingEffectBBR jitterOffsetY]
- -[_MFXTemporalScalingEffectBBR jitterOffset]
- -[_MFXTemporalScalingEffectBBR motionContentOffsetX]
- -[_MFXTemporalScalingEffectBBR motionContentOffsetY]
- -[_MFXTemporalScalingEffectBBR motionTextureFormat]
- -[_MFXTemporalScalingEffectBBR motionTextureUsage]
- -[_MFXTemporalScalingEffectBBR motionTexture]
- -[_MFXTemporalScalingEffectBBR motionVectorScaleX]
- -[_MFXTemporalScalingEffectBBR motionVectorScaleY]
- -[_MFXTemporalScalingEffectBBR motionVectorScale]
- -[_MFXTemporalScalingEffectBBR outputHeight]
- -[_MFXTemporalScalingEffectBBR outputOffsetX]
- -[_MFXTemporalScalingEffectBBR outputOffsetY]
- -[_MFXTemporalScalingEffectBBR outputTextureFormat]
- -[_MFXTemporalScalingEffectBBR outputTextureUsage]
- -[_MFXTemporalScalingEffectBBR outputTexture]
- -[_MFXTemporalScalingEffectBBR outputWidth]
- -[_MFXTemporalScalingEffectBBR preExposure]
- -[_MFXTemporalScalingEffectBBR previousJitterOffset]
- -[_MFXTemporalScalingEffectBBR previousViewToClipMatrix]
- -[_MFXTemporalScalingEffectBBR previousWorldToViewMatrix]
- -[_MFXTemporalScalingEffectBBR reactiveMaskContentOffsetX]
- -[_MFXTemporalScalingEffectBBR reactiveMaskContentOffsetY]
- -[_MFXTemporalScalingEffectBBR reactiveMaskTextureFormat]
- -[_MFXTemporalScalingEffectBBR reactiveMaskTextureUsage]
- -[_MFXTemporalScalingEffectBBR reactiveMaskTexture]
- -[_MFXTemporalScalingEffectBBR reactiveTextureUsage]
- -[_MFXTemporalScalingEffectBBR reset]
- -[_MFXTemporalScalingEffectBBR reversedDepth]
- -[_MFXTemporalScalingEffectBBR setColorContentOffsetX:]
- -[_MFXTemporalScalingEffectBBR setColorContentOffsetY:]
- -[_MFXTemporalScalingEffectBBR setColorTexture:]
- -[_MFXTemporalScalingEffectBBR setCurrentViewToClipMatrix:]
- -[_MFXTemporalScalingEffectBBR setCurrentWorldToViewMatrix:]
- -[_MFXTemporalScalingEffectBBR setDebugTexture:]
- -[_MFXTemporalScalingEffectBBR setDepthContentOffsetX:]
- -[_MFXTemporalScalingEffectBBR setDepthContentOffsetY:]
- -[_MFXTemporalScalingEffectBBR setDepthReversed:]
- -[_MFXTemporalScalingEffectBBR setDepthTexture:]
- -[_MFXTemporalScalingEffectBBR setExposureTexture:]
- -[_MFXTemporalScalingEffectBBR setFence:]
- -[_MFXTemporalScalingEffectBBR setInputContentHeight:]
- -[_MFXTemporalScalingEffectBBR setInputContentWidth:]
- -[_MFXTemporalScalingEffectBBR setJitterOffset:]
- -[_MFXTemporalScalingEffectBBR setJitterOffsetX:]
- -[_MFXTemporalScalingEffectBBR setJitterOffsetY:]
- -[_MFXTemporalScalingEffectBBR setMotionContentOffsetX:]
- -[_MFXTemporalScalingEffectBBR setMotionContentOffsetY:]
- -[_MFXTemporalScalingEffectBBR setMotionTexture:]
- -[_MFXTemporalScalingEffectBBR setMotionVectorScale:]
- -[_MFXTemporalScalingEffectBBR setMotionVectorScaleX:]
- -[_MFXTemporalScalingEffectBBR setMotionVectorScaleY:]
- -[_MFXTemporalScalingEffectBBR setOutputOffsetX:]
- -[_MFXTemporalScalingEffectBBR setOutputOffsetY:]
- -[_MFXTemporalScalingEffectBBR setOutputTexture:]
- -[_MFXTemporalScalingEffectBBR setPreExposure:]
- -[_MFXTemporalScalingEffectBBR setPreviousJitterOffset:]
- -[_MFXTemporalScalingEffectBBR setPreviousViewToClipMatrix:]
- -[_MFXTemporalScalingEffectBBR setPreviousWorldToViewMatrix:]
- -[_MFXTemporalScalingEffectBBR setReactiveMaskContentOffsetX:]
- -[_MFXTemporalScalingEffectBBR setReactiveMaskContentOffsetY:]
- -[_MFXTemporalScalingEffectBBR setReactiveMaskTexture:]
- -[_MFXTemporalScalingEffectBBR setReset:]
- -[_MFXTemporalScalingEffectBBR setReversedDepth:]
- -[sBBRNet executeWithMTL4CommandBuffer:feed:target:]
- -[tBBRNet executeWithMTL4CommandBuffer:feed:target:]
- GCC_except_table110
- GCC_except_table113
- GCC_except_table114
- GCC_except_table118
- GCC_except_table122
- GCC_except_table127
- GCC_except_table133
- GCC_except_table134
- GCC_except_table146
- GCC_except_table147
- GCC_except_table66
- GCC_except_table70
- GCC_except_table71
- GCC_except_table77
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- GCC_except_table89
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._FusedsBBRNet
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._FusedtBBRNet
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._asyncQueue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._autoExposureEnabled
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._colorContentOffsetX
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._colorContentOffsetY
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._colorTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._colorTextureFormat
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._colorTextureUsage
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._commandQueue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._currentViewToClipMatrix
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._currentWorldToViewMatrix
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._debugTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._depthContentOffsetX
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._depthContentOffsetY
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._depthTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._depthTextureFormat
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._depthTextureUsage
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._device
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._dummyFence
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._enableLateLatch
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._exposureTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._fence
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._framePowerOnSharedEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._frameSharedEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._historyTensorStride
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._history_input_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._history_output_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputContentHeight
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputContentMaxScale
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputContentMinScale
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputContentWidth
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputEventValue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputHeight
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._inputWidth
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._jitterOffset
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._linelockingEnabled
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._midBicubicWarp
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._midProcessingDoneEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._midProcessingStartEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionContentOffsetX
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionContentOffsetY
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionTextureFormat
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionTextureUsage
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._motionVectorScale
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._netEventValue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._netSyncEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputEventValue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputHeight
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputOffsetX
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputOffsetY
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputResolutionMotionVectorsEnabled
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputTextureFormat
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputTextureUsage
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._outputWidth
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._overlapNetwork
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._preExposure
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._prefilterSharedEvent
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._prefilterSharedEventValue
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._prefilter_net_wrapper
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._previousJitterOffset
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._previousViewToClipMatrix
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._previousWorldToViewMatrix
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._prewarmComplete
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveMaskContentOffsetX
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveMaskContentOffsetY
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveMaskEnabled
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveMaskTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveMaskTextureFormat
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveTexture
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reactiveTextureUsage
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reset
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._reversedDepth
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._sbbr_net_wrapper
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._spatialInTensorStride
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._spatialOutTensorStride
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._spatial_input_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._spatial_output_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._tbbr_net_wrapper
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._temporalInTensorStride
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._temporalOutTensorStride
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._temporal_input_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._temporal_output_TensorData
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._timingRecord
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._useANE
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._useFusedBBRNet
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR._waitForCompletion
- OBJC_IVAR_$__MFXTemporalScalingEffectBBR.frameIndex
- __ZN13BBRNet_FilterI10MFXDevice3E10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU19objcproto9MTLBuffer11objc_objectS7_S7_PU21objcproto10MTLTexture11objc_objectS9_fbRK17BRNetShaderParamsh
- __ZN13BBRNet_FilterI10MFXDevice3E14getEncodeIndexEv
- __ZN13BBRNet_FilterI10MFXDevice3E9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_PU19objcproto9MTLBuffer11objc_objectbRK17BRNetShaderParamsfh
- __ZN13BBRNet_FilterI10MFXDevice3E9encodePreEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_S7_S7_PU19objcproto9MTLBuffer11objc_objectS9_S9_S9_bbbfRK17BRNetShaderParamsh
- __ZN13BBRNet_FilterI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiPU21objcproto10MTLTexture11objc_objectbbbbbbb14MTLPixelFormatbbb
- __ZN13BBRNet_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiPU21objcproto10MTLTexture11objc_objectbbbbbbb14MTLPixelFormatbbb
- __ZN13BBRNet_FilterI10MFXDevice4E10encodePostEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU19objcproto9MTLBuffer11objc_objectS7_S7_PU21objcproto10MTLTexture11objc_objectS9_fbRK17BRNetShaderParamsh
- __ZN13BBRNet_FilterI10MFXDevice4E14getEncodeIndexEv
- __ZN13BBRNet_FilterI10MFXDevice4E9encodeMidEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS7_PU19objcproto9MTLBuffer11objc_objectbRK17BRNetShaderParamsfh
- __ZN13BBRNet_FilterI10MFXDevice4E9encodePreEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS7_S7_S7_PU19objcproto9MTLBuffer11objc_objectS9_S9_S9_bbbfRK17BRNetShaderParamsh
- __ZN13BBRNet_FilterI10MFXDevice4EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiPU21objcproto10MTLTexture11objc_objectbbbbbbb14MTLPixelFormatbbb
- __ZN13BBRNet_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiPU21objcproto10MTLTexture11objc_objectbbbbbbb14MTLPixelFormatbbb
- __ZNK13BBRNet_FilterI10MFXDevice3E18computeMotionScaleEDv2_fDv2_tS3_
- __ZNK13BBRNet_FilterI10MFXDevice4E18computeMotionScaleEDv2_fDv2_tS3_
CStrings:
+ "$\xe5q\xc3"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/BBRNet_Filter.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/BRNet4_1.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Common/common_host.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv12x12Stride4/Conv12x12Stride4.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1FusedBilinear/Conv1x1FusedBilinear.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1OutputHead/../Common/common_host.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1OutputHead/Conv1x1OutputHead.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3SigmoidD2S/Conv3x3SigmoidD2S.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride1/Conv3x3Stride1.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride2/../Common/common_host.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride2/Conv3x3Stride2.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/SBBRNet.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/SBBRNet_MLP/SBBRNet_MLP.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/BR_Net/FusedNetwork/TBBRNet.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MPSGraphMPSGraphExecutableWrapper.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/Metal4FXFrameInterpolatorEffect.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/Metal4FXSpatialScalingEffectV1.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/Metal4FXTemporalDenoisingScalingEffect.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/Metal4FXTemporalScalingEffectV4.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXDebugError.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXFrameInterpolatorEffect.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXSpatialScalingEffectV1.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalDenoisingScalingEffect.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectBase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectDebug.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectNRS.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectV3.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectV4.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Ws9pyY/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.mm"
+ "@\"NSMutableDictionary\"8@?0"
+ "BBRNet_Filter: default.metallib not found"
+ "BBRNet_Filter: failed to load metallib"
+ "BBRNet_Filter: failed to load network weights"
+ "BBRNet_Filter: sacneh.mtlpackage not found"
+ "Failed to create bilinear resource"
+ "Failed to create conv resource"
+ "ML network mtlpackage error: %@"
+ "ML network pipeline error: %@"
+ "MetalFX_Temporal_BBR_MidProcessing"
+ "MetalFX_Temporal_BBR_PostProcessing"
+ "MetalFX_Temporal_BBR_PreProcessing"
+ "className"
+ "encoderVersion"
+ "gpuName"
+ "library.mpsgraphpackage"
+ "sacneh"
+ "\xf0\xc6B"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/BRNet4_1.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Common/common_host.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv12x12Stride4/Conv12x12Stride4.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1FusedBilinear/Conv1x1FusedBilinear.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv1x1OutputHead/Conv1x1OutputHead.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3SigmoidD2S/Conv3x3SigmoidD2S.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride1/../Common/common_host.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride1/Conv3x3Stride1.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride2/../Common/common_host.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/Conv3x3Stride2/Conv3x3Stride2.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/SBBRNet.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/SBBRNet_MLP/SBBRNet_MLP.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/BR_Net/FusedNetwork/TBBRNet.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MPSGraphMPSGraphExecutableWrapper.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/Metal4FXFrameInterpolatorEffect.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/Metal4FXSpatialScalingEffectV1.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/Metal4FXTemporalDenoisingScalingEffect.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/Metal4FXTemporalScalingEffectV4.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXDebugError.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXFrameInterpolatorEffect.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXSpatialScalingEffectV1.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalDenoisingScalingEffect.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectBBR.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectDebug.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectNRS.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectV3.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/Framework/MetalFXTemporalScalingEffectV4.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OEyJpx/Sources/MetalFX/MetalFX-Utilities/MetalFX-Utilities.mm"
- "MTL4 path requires buffer input (useTextureInput must be false)"
- "TAAUBBR | ANE"
- "emit_sacneh_constants.dat"
```
