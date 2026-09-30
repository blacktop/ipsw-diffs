## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

 382.5.3.0.0
-  __TEXT.__text: 0x1e6d38
-  __TEXT.__objc_methlist: 0x1eb8c
-  __TEXT.__cstring: 0x233f9
-  __TEXT.__gcc_except_tab: 0xc3ac
-  __TEXT.__const: 0x2d790
+  __TEXT.__text: 0x1e8758
+  __TEXT.__objc_methlist: 0x1ee04
+  __TEXT.__cstring: 0x2378c
+  __TEXT.__gcc_except_tab: 0xc3bc
+  __TEXT.__const: 0x2e620
   __TEXT.__oslogstring: 0x22d6
   __TEXT.__ustring: 0x1be
-  __TEXT.__unwind_info: 0x8b18
+  __TEXT.__unwind_info: 0x8b08
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x8e80
+  __DATA_CONST.__objc_selrefs: 0x8f38
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xc08
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xa30
   __AUTH_CONST.__const: 0x4f80
-  __AUTH_CONST.__cfstring: 0x12ca0
-  __AUTH_CONST.__objc_const: 0x46bf0
+  __AUTH_CONST.__cfstring: 0x12e00
+  __AUTH_CONST.__objc_const: 0x46f58
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xe98
   __AUTH.__objc_data: 0x4380
-  __DATA.__objc_ivar: 0x2234
+  __DATA.__objc_ivar: 0x225c
   __DATA.__data: 0x4498
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x40b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13495
-  Symbols:   25322
-  CStrings:  4572
+  Functions: 13563
+  Symbols:   25419
+  CStrings:  4604
 
Symbols:
+ -[MTL4ComputePipelineDescriptor contentionRelief]
+ -[MTL4ComputePipelineDescriptor forwardProgressUsage]
+ -[MTL4ComputePipelineDescriptor optimizeForPersistentKernel]
+ -[MTL4ComputePipelineDescriptor setContentionRelief:]
+ -[MTL4ComputePipelineDescriptor setForwardProgressUsage:]
+ -[MTL4ComputePipelineDescriptor setOptimizeForPersistentKernel:]
+ -[MTLComputePipelineDescriptorInternal contentionRelief]
+ -[MTLComputePipelineDescriptorInternal forwardProgressUsage]
+ -[MTLComputePipelineDescriptorInternal optimizeForPersistentKernel]
+ -[MTLComputePipelineDescriptorInternal setContentionRelief:]
+ -[MTLComputePipelineDescriptorInternal setForwardProgressUsage:]
+ -[MTLComputePipelineDescriptorInternal setOptimizeForPersistentKernel:]
+ -[MTLDeviceFeatureQueries familySupportsAtomicWaitNotify]
+ -[MTLDeviceFeatureQueries familySupportsMXUNarrowTileSizes]
+ -[MTLDeviceFeatureQueries familySupportsPackUnpackSmallInteger]
+ -[MTLDeviceFeatureQueries familySupportsRGBTextureBuffers]
+ -[MTLDeviceFeatureQueries familySupportsSIMDGroupParallelForwardProgress]
+ -[MTLDeviceFeatureQueries familySupportsTextureViewMinLOD]
+ -[MTLDeviceFeatureQueries supportsAtomicWaitNotify]
+ -[MTLDeviceFeatureQueries supportsMXUNarrowTileSizes]
+ -[MTLDeviceFeatureQueries supportsPackUnpackSmallInteger]
+ -[MTLDeviceFeatureQueries supportsRGBTextureBuffers]
+ -[MTLDeviceFeatureQueries supportsSIMDGroupParallelForwardProgress]
+ -[MTLDeviceFeatureQueries supportsTextureViewMinLOD]
+ -[MTLShaderValidationConfiguration enableYieldChecks]
+ -[MTLShaderValidationConfiguration setEnableYieldChecks:]
+ -[MTLTextureViewDescriptor minLOD]
+ -[MTLTextureViewDescriptor setMinLOD:]
+ -[MTLTileRenderPipelineDescriptorInternal driverCompilerOptions]
+ -[MTLTileRenderPipelineDescriptorInternal setDriverCompilerOptions:]
+ -[_MTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:]
+ -[_MTLDevice supportsAtomicWaitNotify]
+ -[_MTLDevice supportsMXUNarrowTileSizes]
+ -[_MTLDevice supportsPackUnpackSmallInteger]
+ -[_MTLDevice supportsRGBTextureBuffers]
+ -[_MTLDevice supportsSIMDGroupParallelForwardProgress]
+ -[_MTLDevice supportsTextureViewMinLOD]
+ -[_MTLDeviceFeatureQueries familySupportsAtomicWaitNotify]
+ -[_MTLDeviceFeatureQueries familySupportsMXUNarrowTileSizes]
+ -[_MTLDeviceFeatureQueries familySupportsPackUnpackSmallInteger]
+ -[_MTLDeviceFeatureQueries familySupportsRGBTextureBuffers]
+ -[_MTLDeviceFeatureQueries familySupportsSIMDGroupParallelForwardProgress]
+ -[_MTLDeviceFeatureQueries familySupportsTextureViewMinLOD]
+ -[_MTLResource minLOD]
+ GCC_except_table156
+ GCC_except_table324
+ GCC_except_table336
+ GCC_except_table398
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table434
+ GCC_except_table445
+ GCC_except_table477
+ GCC_except_table480
+ GCC_except_table736
+ GCC_except_table779
+ GCC_except_table781
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table858
+ GCC_except_table862
+ _OBJC_IVAR_$_MTL4ComputePipelineDescriptor._contentionRelief
+ _OBJC_IVAR_$_MTL4ComputePipelineDescriptor._forwardProgressUsage
+ _OBJC_IVAR_$_MTL4ComputePipelineDescriptor._optimizeForPersistentKernel
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsAtomicWaitNotify
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsMXUNarrowTileSizes
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsPackUnpackSmallInteger
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsRGBTextureBuffers
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsSIMDGroupParallelForwardProgress
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsTextureViewMinLOD
+ _OBJC_IVAR_$_MTLShaderValidationConfiguration._enableYieldChecks
+ __ZZ22MTLGetPackSintFunctionEN4$_128__invokeEPKiPv
+ __ZZ22MTLGetPackSintFunctionEN4$_138__invokeEPKiPv
+ __ZZ22MTLGetPackSintFunctionEN4$_148__invokeEPKiPv
+ __ZZ22MTLGetPackUintFunctionEN4$_148__invokeEPKjPv
+ __ZZ22MTLGetPackUintFunctionEN4$_158__invokeEPKjPv
+ __ZZ22MTLGetPackUintFunctionEN4$_168__invokeEPKjPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_498__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_508__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_518__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_528__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_538__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_548__invokeEPKfPv
+ __ZZ23MTLGetPackFloatFunctionEN4$_558__invokeEPKfPv
+ __ZZ24MTLGetUnpackSintFunctionEN4$_128__invokeEPKvPi
+ __ZZ24MTLGetUnpackSintFunctionEN4$_138__invokeEPKvPi
+ __ZZ24MTLGetUnpackSintFunctionEN4$_148__invokeEPKvPi
+ __ZZ24MTLGetUnpackUintFunctionEN4$_148__invokeEPKvPj
+ __ZZ24MTLGetUnpackUintFunctionEN4$_158__invokeEPKvPj
+ __ZZ24MTLGetUnpackUintFunctionEN4$_168__invokeEPKvPj
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_498__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_508__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_518__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_528__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_538__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_548__invokeEPKvPf
+ __ZZ25MTLGetUnpackFloatFunctionEN4$_558__invokeEPKvPf
+ _isRGBPixelFormat
+ _objc_msgSend$contentionRelief
+ _objc_msgSend$enableYieldChecks
+ _objc_msgSend$familySupportsAtomicWaitNotify
+ _objc_msgSend$familySupportsMXUNarrowTileSizes
+ _objc_msgSend$familySupportsPackUnpackSmallInteger
+ _objc_msgSend$familySupportsRGBTextureBuffers
+ _objc_msgSend$familySupportsSIMDGroupParallelForwardProgress
+ _objc_msgSend$familySupportsTextureViewMinLOD
+ _objc_msgSend$forwardProgressUsage
+ _objc_msgSend$minLOD
+ _objc_msgSend$optimizeForPersistentKernel
+ _objc_msgSend$setContentionRelief:
+ _objc_msgSend$setForwardProgressUsage:
+ _objc_msgSend$setMinLOD:
+ _objc_msgSend$setOptimizeForPersistentKernel:
+ _objc_msgSend$supportsAtomicWaitNotify
+ _objc_msgSend$supportsMXUNarrowTileSizes
+ _objc_msgSend$supportsPackUnpackSmallInteger
+ _objc_msgSend$supportsRGBTextureBuffers
+ _objc_msgSend$supportsSIMDGroupParallelForwardProgress
+ _objc_msgSend$supportsTextureViewMinLOD
- GCC_except_table149
- GCC_except_table318
- GCC_except_table330
- GCC_except_table386
- GCC_except_table389
- GCC_except_table396
- GCC_except_table426
- GCC_except_table439
- GCC_except_table463
- GCC_except_table466
- GCC_except_table474
- GCC_except_table729
- GCC_except_table733
- GCC_except_table773
- GCC_except_table775
- GCC_except_table778
- GCC_except_table780
- GCC_except_table832
- GCC_except_table833
- GCC_except_table836
- GCC_except_table837
- GCC_except_table845
- GCC_except_table852
- GCC_except_table856
CStrings:
+ "-[_MTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:]"
+ "Atomic Wait and Notify"
+ "ForwardProgressUsageFnAttr"
+ "MTLGPUFamilyApple11"
+ "MTLPixelFormatRGB16Bfloat"
+ "MTLPixelFormatRGB16Float"
+ "MTLPixelFormatRGB16Sint"
+ "MTLPixelFormatRGB16Snorm"
+ "MTLPixelFormatRGB16Uint"
+ "MTLPixelFormatRGB16Unorm"
+ "MTLPixelFormatRGB32Float"
+ "MTLPixelFormatRGB32Sint"
+ "MTLPixelFormatRGB32Uint"
+ "MTLPixelFormatRGB8Sint"
+ "MTLPixelFormatRGB8Snorm"
+ "MTLPixelFormatRGB8Uint"
+ "MTLPixelFormatRGB8Unorm"
+ "MXU Narrow Tile Sizes, 8x16 and 16x8"
+ "Pack and unpack support of 16b integers"
+ "PersistentFnAttr"
+ "RGB Pixel Formats for Texture Buffers"
+ "SIMDgroup Parallel Forward Progress"
+ "Texture View Min LOD"
+ "applegpu_g17d"
+ "applegpu_g18g"
+ "applegpu_g18m"
+ "applegpu_g19p"
+ "contentionRelief ="
+ "enable-yield-check"
+ "forwardProgressUsage ="
+ "optimizeForPersistentKernel ="
+ "recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup must be overridden by the driver."
```
