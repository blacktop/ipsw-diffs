## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-29.2.1.0.0
-  __TEXT.__text: 0x164f4
+29.3.0.0.0
+  __TEXT.__text: 0x168d4
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xe94
-  __TEXT.__gcc_except_tab: 0x219c
-  __TEXT.__cstring: 0x14a9
+  __TEXT.__objc_methlist: 0xf34
+  __TEXT.__gcc_except_tab: 0x21cc
+  __TEXT.__cstring: 0x14c2
   __TEXT.__const: 0x1e0
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x35c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1bd
-  __TEXT.__objc_methname: 0x2811
-  __TEXT.__objc_methtype: 0x8e8
-  __TEXT.__objc_stubs: 0x1900
+  __TEXT.__objc_methname: 0x2a5b
+  __TEXT.__objc_methtype: 0x8e9
+  __TEXT.__objc_stubs: 0x19c0
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35c8
-  __DATA_CONST.__objc_selrefs: 0x880
+  __DATA_CONST.__objc_const: 0x3868
+  __DATA_CONST.__objc_selrefs: 0x8c8
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0xd58
   __AUTH_CONST.__cfstring: 0x1dc0
   __AUTH_CONST.__objc_intobj: 0x180

   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x250
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x2dc
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x240
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 336
-  Symbols:   1478
-  CStrings:  785
+  Functions: 349
+  Symbols:   1523
+  CStrings:  808
 
Symbols:
+ -[MTLFXTemporalScalerDescriptor isReactiveMaskTextureEnabled]
+ -[MTLFXTemporalScalerDescriptor reactiveMaskTextureFormat]
+ -[MTLFXTemporalScalerDescriptor setReactiveMaskTextureEnabled:]
+ -[MTLFXTemporalScalerDescriptor setReactiveMaskTextureFormat:]
+ -[_MFXTemporalScalingEffectDebug reactiveMaskTexture]
+ -[_MFXTemporalScalingEffectDebug reactiveTextureUsage]
+ -[_MFXTemporalScalingEffectDebug setReactiveMaskTexture:]
+ -[_MFXTemporalScalingEffectNRS reactiveMaskTexture]
+ -[_MFXTemporalScalingEffectNRS reactiveTextureUsage]
+ -[_MFXTemporalScalingEffectNRS setReactiveMaskTexture:]
+ -[_MFXTemporalScalingEffectV3 reactiveMaskTexture]
+ -[_MFXTemporalScalingEffectV3 reactiveTextureUsage]
+ -[_MFXTemporalScalingEffectV3 setReactiveMaskTexture:]
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table77
+ GCC_except_table79
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._enableLateLatch
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._prevReactiveTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._reactiveMaskEnabled
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._reactiveMaskTextureFormat
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._reactiveTexture
+ OBJC_IVAR_$__MFXTemporalScalingEffectV3._reactiveTextureUsage
+ _OBJC_IVAR_$_MTLFXTemporalScalerDescriptor.reactiveMaskTextureEnabled
+ _OBJC_IVAR_$_MTLFXTemporalScalerDescriptor.reactiveMaskTextureFormat
+ _OBJC_IVAR_$__MFXTemporalScalingEffectDebug._reactiveMaskTexture
+ _OBJC_IVAR_$__MFXTemporalScalingEffectDebug._reactiveTextureUsage
+ _OBJC_IVAR_$__MFXTemporalScalingEffectNRS._reactiveMaskTexture
+ _OBJC_IVAR_$__MFXTemporalScalingEffectNRS._reactiveTextureUsage
+ _OBJC_IVAR_$__MFXTemporalScalingEffectV3._reactiveMaskTexture
+ __ZN15BRNet_v3_Filter10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS7_S7_S7_Dv2_fS8_fffbDv2_t
+ __ZN15BRNet_v3_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibb
+ __ZN15BRNet_v3_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibb
+ ___block_descriptor_170_ea8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_170_ea8_32s40s48s56s64s72s80s88s_e76_B24?0"<MTLCommandBuffer>"8r^{_MTLCommandBufferSynchronizationInfo=iQ^Q}16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ _objc_msgSend$blitCommandEncoder
+ _objc_msgSend$copyFromTexture:toTexture:
+ _objc_msgSend$isReactiveMaskTextureEnabled
+ _objc_msgSend$reactiveMaskTextureFormat
+ _objc_msgSend$setReactiveMaskTextureEnabled:
+ _objc_msgSend$setReactiveMaskTextureFormat:
- GCC_except_table34
- GCC_except_table35
- GCC_except_table74
- GCC_except_table76
- __ZN15BRNet_v3_Filter10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS7_Dv2_ffffbDv2_t
- __ZN15BRNet_v3_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriib
- __ZN15BRNet_v3_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriib
- ___block_descriptor_162_ea8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_162_ea8_32s40s48s56s64s72s80s_e76_B24?0"<MTLCommandBuffer>"8r^{_MTLCommandBufferSynchronizationInfo=iQ^Q}16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
CStrings:
+ "\x01\xec\xb9!\xf0\xf0\xa1\x12"
+ "!\x1e\x16\xa4\x84"
+ "%\x94\x84"
+ "MTLFX_DISABLE_LATE_LATCH"
+ "T@\"<MTLTexture>\",&,N,V_reactiveMaskTexture"
+ "T@\"NSString\",?,R,C"
+ "TB,N,GisReactiveMaskTextureEnabled,VreactiveMaskTextureEnabled"
+ "TQ,N,VreactiveMaskTextureFormat"
+ "TQ,R,N,V_reactiveTextureUsage"
+ "^{BRNet_v3_Filter=iiiiiiiiiiiiiSSBBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@]@@@@@@@@@@@@@@@@@@@@@@}"
+ "_enableLateLatch"
+ "_prevReactiveTexture"
+ "_reactiveMaskEnabled"
+ "_reactiveMaskTexture"
+ "_reactiveMaskTextureFormat"
+ "_reactiveTexture"
+ "_reactiveTextureUsage"
+ "blitCommandEncoder"
+ "copyFromTexture:toTexture:"
+ "isReactiveMaskTextureEnabled"
+ "reactiveMaskTexture"
+ "reactiveMaskTextureEnabled"
+ "reactiveMaskTextureFormat"
+ "reactiveTextureUsage"
+ "setReactiveMaskTexture:"
+ "setReactiveMaskTextureEnabled:"
+ "setReactiveMaskTextureFormat:"
- "\x01ڹ!\xf0\xf0\xa1\x11"
- "!\x1e\x16\x94\x83"
- "%\x84\x83"
- "^{BRNet_v3_Filter=iiiiiiiiiiiiiSSBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@]@@@@@@@@@@@@@@@@@@@@@@}"

```
