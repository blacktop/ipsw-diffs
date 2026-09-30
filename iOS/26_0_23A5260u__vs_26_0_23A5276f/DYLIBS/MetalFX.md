## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-30.8.0.0.0
-  __TEXT.__text: 0x4db8c
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x3d0c
+30.9.0.0.0
+  __TEXT.__text: 0x4e940
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x3dec
   __TEXT.__const: 0x268
-  __TEXT.__gcc_except_tab: 0x834c
+  __TEXT.__gcc_except_tab: 0x85b4
   __TEXT.__cstring: 0x304b
-  __TEXT.__unwind_info: 0xba8
-  __TEXT.__objc_classname: 0x5ba
-  __TEXT.__objc_methname: 0x5385
-  __TEXT.__objc_methtype: 0xf3e
-  __TEXT.__objc_stubs: 0x2da0
+  __TEXT.__unwind_info: 0xbc0
+  __TEXT.__objc_classname: 0x5bc
+  __TEXT.__objc_methname: 0x5419
+  __TEXT.__objc_methtype: 0xec6
+  __TEXT.__objc_stubs: 0x2de0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_selrefs: 0x1058
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x2d40
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x3d20
-  __AUTH_CONST.__objc_const: 0xa630
+  __AUTH_CONST.__objc_const: 0xa830
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x2b98
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0xb30
+  __DATA.__objc_ivar: 0xb58
   __DATA.__data: 0x840
   __DATA.__bss: 0x1b0
-  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17208DB9-50C1-384E-9C0F-0D5CD11E7E9F
-  Functions: 1168
-  Symbols:   4144
-  CStrings:  2067
+  UUID: E7CCFFE5-0F26-39AA-8923-7849E0A380F6
+  Functions: 1185
+  Symbols:   4176
+  CStrings:  2075
 
Symbols:
+ -[_M4FXFrameInterpolatorEffect contentHeight]
+ -[_M4FXFrameInterpolatorEffect contentWidth]
+ -[_M4FXFrameInterpolatorEffect dealloc]
+ -[_M4FXFrameInterpolatorEffect setContentHeight:]
+ -[_M4FXFrameInterpolatorEffect setContentWidth:]
+ -[_MFXFrameInterpolatorEffect contentHeight]
+ -[_MFXFrameInterpolatorEffect contentWidth]
+ -[_MFXFrameInterpolatorEffect dealloc]
+ -[_MFXFrameInterpolatorEffect setContentHeight:]
+ -[_MFXFrameInterpolatorEffect setContentWidth:]
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table22
+ GCC_except_table57
+ GCC_except_table76
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._contentHeight
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._contentWidth
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._internalFence
+ _OBJC_IVAR_$__M4FXFrameInterpolatorEffect._pDevice
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._contentHeight
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._contentWidth
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._denoiserScaler
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._denoiserScaler4
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._impl
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._temporalScaler
+ _OBJC_IVAR_$__MFXFrameInterpolatorEffect._temporalScaler4
+ __ZN12FrameGenImplI10MFXDevice4ED2Ev
+ __ZN15BFNet_v1_FilterI10MFXDevice3E10encodePostEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU19objcproto9MTLBuffer11objc_objecth
+ __ZN15BFNet_v1_FilterI10MFXDevice3E12encodeAtrousERS0_PU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_S7_S7_S7_S7_S7_S7_S7_S7_S7_Dv2_fS8_h
+ __ZN15BFNet_v1_FilterI10MFXDevice3E14getEncodeIndexEv
+ __ZN15BFNet_v1_FilterI10MFXDevice3E9encodeMidEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_S6_S6_S6_S6_S6_Dv2_fS7_bRK13simd_float4x4SA_Dv4_fh
+ __ZN15BFNet_v1_FilterI10MFXDevice3E9encodePreEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_S6_S6_S6_PU19objcproto9MTLBuffer11objc_objectDv2_fS9_bh
+ __ZN15BFNet_v1_FilterI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
+ __ZN15BFNet_v1_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
+ __ZN15BFNet_v1_FilterI10MFXDevice3ED1Ev
+ __ZN15BFNet_v1_FilterI10MFXDevice3ED2Ev
+ __ZN15BRNet_v3_FilterI10MFXDevice3E10encodePostEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS8_S8_S8_Dv2_fS9_fffbDv2_th
+ __ZN15BRNet_v3_FilterI10MFXDevice3E14getEncodeIndexEv
+ __ZN15BRNet_v3_FilterI10MFXDevice3E18getFlowDiffTextureEv
+ __ZN15BRNet_v3_FilterI10MFXDevice3E19encodeMidForDenoiseEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_S6_Dv2_fS7_ffbDv2_tS7_h
+ __ZN15BRNet_v3_FilterI10MFXDevice3E19encodePreForDenoiseEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_S6_S6_S6_S6_S6_S6_S6_PU19objcproto9MTLBuffer11objc_objectDv2_fS9_ffbbbfDv2_th
+ __ZN15BRNet_v3_FilterI10MFXDevice3E19getInternalExposureEv
+ __ZN15BRNet_v3_FilterI10MFXDevice3E9encodeMidEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_Dv2_fS7_bDv2_tS7_h
+ __ZN15BRNet_v3_FilterI10MFXDevice3E9encodePreEPU27objcproto16MTLCommandBuffer11objc_object18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS6_S6_S6_S6_PU19objcproto9MTLBuffer11objc_objectDv2_fS9_ffbbbfDv2_th
+ __ZN15BRNet_v3_FilterI10MFXDevice3EC1ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
+ __ZN15BRNet_v3_FilterI10MFXDevice3ED1Ev
+ __ZN15BRNet_v3_FilterI10MFXDevice3ED2Ev
+ __ZN18MFXComputeEncoder4C2EPU19objcproto9MTLDevice11objc_objectPU26objcproto15MTLResidencySet11objc_object
+ ___block_literal_global.1340
+ _objc_msgSend$inputContentHeight
+ _objc_msgSend$inputContentWidth
- GCC_except_table113
- GCC_except_table116
- GCC_except_table55
- GCC_except_table66
- GCC_except_table68
- GCC_except_table74
- GCC_except_table75
- GCC_except_table82
- GCC_except_table83
- GCC_except_table90
- GCC_except_table94
- _OBJC_IVAR_$__M4FXFrameInterpolatorEffect.m_pDevice
- __ZN15BFNet_v1_Filter10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objecth
- __ZN15BFNet_v1_Filter12encodeAtrousEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_S5_S5_Dv2_fS6_h
- __ZN15BFNet_v1_Filter9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_Dv2_fS6_bRK13simd_float4x4S9_Dv4_fh
- __ZN15BFNet_v1_Filter9encodePreEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_bh
- __ZN15BFNet_v1_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
- __ZN15BFNet_v1_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb
- __ZN15BFNet_v1_FilterD2Ev
- __ZN15BRNet_v3_Filter10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS7_S7_S7_Dv2_fS8_fffbDv2_th
- __ZN15BRNet_v3_Filter19encodeMidForDenoiseEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_Dv2_fS6_ffbDv2_tS6_h
- __ZN15BRNet_v3_Filter19encodePreForDenoiseEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_S5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_ffbbbfDv2_th
- __ZN15BRNet_v3_Filter19getInternalExposureEv
- __ZN15BRNet_v3_Filter9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_Dv2_fS6_bDv2_tS6_h
- __ZN15BRNet_v3_Filter9encodePreEPU27objcproto16MTLCommandBuffer11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_S5_S5_PU19objcproto9MTLBuffer11objc_objectDv2_fS8_ffbbbfDv2_th
- __ZN15BRNet_v3_FilterC1EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
- __ZN15BRNet_v3_FilterC2EPU19objcproto9MTLDevice11objc_objectPU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb
- __ZN15BRNet_v3_FilterD2Ev
- __ZN18MFXComputeEncoder4C2EPU19objcproto9MTLDevice11objc_object
- ___block_literal_global.1341
- __denoiserScaler
- __denoiserScaler4
- __impl
- __temporalScaler
- __temporalScaler4
CStrings:
+ "#\xe5S"
+ "@\"<MTLFXTemporalDenoisedScalerSPI>\""
+ "@\"<MTLFXTemporalScalerSPI>\""
+ "TQ,N,V_contentHeight"
+ "TQ,N,V_contentWidth"
+ "_contentHeight"
+ "_contentWidth"
+ "_pDevice"
+ "_temporalScaler4"
+ "contentHeight"
+ "contentWidth"
+ "setContentHeight:"
+ "setContentWidth:"
- "\"\xe5S"
- "^{BFNet_v1_Filter=iiiiii@@@@@@@@[2@][2@]@[2@][2@]@@@[2@][2@][2@]@@@@BBBC}"
- "^{BRNet_v3_Filter=iiiiiiiiiiiiiiSSBBBBBBBBi@@@[2@][2@]C@@@@@@[2@][2@][2@]@@[2@]@[2@]@@@@@@@@@@@@@@@@@@@@@@@@}"
- "m_pDevice"
- "\xe5s"

```
