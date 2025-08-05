## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-31.1.0.0.0
-  __TEXT.__text: 0x4db48
-  __TEXT.__auth_stubs: 0x910
+31.3.0.0.0
+  __TEXT.__text: 0x4e6ec
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x3da4
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x8024
-  __TEXT.__cstring: 0x2ce9
+  __TEXT.__gcc_except_tab: 0x81b8
+  __TEXT.__cstring: 0x2d86
   __TEXT.__unwind_info: 0xc10
   __TEXT.__objc_classname: 0x5db
-  __TEXT.__objc_methname: 0x52cb
+  __TEXT.__objc_methname: 0x52a2
   __TEXT.__objc_methtype: 0xd1f
-  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_stubs: 0x2ce0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x2808
-  __AUTH_CONST.__auth_got: 0x498
+  __DATA_CONST.__objc_arraydata: 0x2a38
+  __AUTH_CONST.__auth_got: 0x4a0
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x3d00
-  __AUTH_CONST.__objc_const: 0xa7f8
+  __AUTH_CONST.__objc_const: 0xa818
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x27a8
+  __AUTH_CONST.__objc_arrayobj: 0x2a48
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0xb54
+  __DATA.__objc_ivar: 0xb58
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70AE7CF0-8B7E-3570-B0A4-B8610926DC03
+  UUID: 2BFE459F-F975-3A12-BE98-617C2855EDB9
   Functions: 1188
   Symbols:   4176
-  CStrings:  2044
+  CStrings:  2043
 
Symbols:
+ _OBJC_IVAR_$__M4FXTemporalDenoisingScalingEffect._prevViewProjectionMatrix
+ __ZL38EmitDBF_Net_V3_2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor
+ ____ZL38EmitDBF_Net_V3_2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke
+ ____ZL38EmitDBF_Net_V3_2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke_2
+ ___block_literal_global.1284
+ ___block_literal_global.611
- __ZL36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor
- ____ZL36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke
- ____ZL36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor_block_invoke_2
- ___block_literal_global.1206
- ___block_literal_global.610
- _objc_msgSend$concatTensors:dimension:interleave:name:
Functions:
~ __ZL36EmitDBF_Net_V3_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor -> __ZL38EmitDBF_Net_V3_2_getMPSGraphExecutableP6NSDataP14NSMutableArrayIP18MPSGraphShapedTypeES5_P29MPSGraphCompilationDescriptorRK16DBFNetDescriptor : 8124 -> 10892
~ -[_MFXTemporalDenoisingScalingEffect encodeToCommandBuffer:] : 2828 -> 2784
~ __ZL41EmitBR_Net_V41_nchw_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor : 16936 -> 16844
~ __ZL41EmitBR_Net_V41_nhwc_getMPSGraphExecutableP6NSDataRK15BRNetDescriptorP29MPSGraphCompilationDescriptor : 16836 -> 16752
~ -[MTLFXTemporalScalerDescriptor newTemporalScalerWithHistoryTexture:] : 220 -> 212
~ -[MTLFXTemporalScalerDescriptor newTemporalScalerWithDevice:] : 504 -> 480
~ -[_M4FXTemporalDenoisingScalingEffect initWithDevice:compiler:descriptor:history:] : 5540 -> 5544
~ -[_M4FXTemporalDenoisingScalingEffect encodeToCommandBuffer:] : 2956 -> 3252
~ __ZN15BFNet_v1_FilterI10MFXDevice3EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb : 1864 -> 1836
~ __ZN15BFNet_v1_FilterI10MFXDevice3E12encodeAtrousERS0_PU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS8_S8_S8_S8_S8_S8_S8_S8_S8_S8_PU19objcproto9MTLBuffer11objc_objectSA_fDv2_fSB_h : 1976 -> 1784
~ __ZN15BFNet_v1_FilterI10MFXDevice3ED2Ev : 292 -> 284
~ __ZN15BRNet_v3_FilterI10MFXDevice3EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb : 3232 -> 3396
~ __ZN15BRNet_v3_FilterI10MFXDevice3E9encodePreEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_S7_S7_S7_PU19objcproto9MTLBuffer11objc_objectDv2_fSA_ffbbbfDv2_th : 2072 -> 2104
~ __ZN15BRNet_v3_FilterI10MFXDevice3E19encodePreForDenoiseEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_S7_S7_S7_S7_S7_S7_S7_PU19objcproto9MTLBuffer11objc_objectDv2_fSA_ffbbbfDv2_th : 1608 -> 1640
~ __ZN15BRNet_v3_FilterI10MFXDevice3E9encodeMidEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU21objcproto10MTLTexture11objc_objectS7_Dv2_fS8_bDv2_tS8_h : 1324 -> 1356
~ __ZN15BRNet_v3_FilterI10MFXDevice3E10encodePostEPU27objcproto16MTLCommandBuffer11objc_objectR18MFXComputeEncoder3PU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS9_S9_S9_Dv2_fSA_fffbDv2_th : 1344 -> 1388
~ __ZN15BRNet_v3_FilterI10MFXDevice3ED2Ev : 436 -> 452
~ __ZN15BFNet_v1_FilterI10MFXDevice4EC2ERS0_PK15BRNet_v3_FilterIS0_EPU21objcproto10MTLLibrary11objc_objectiiiiRK16DBFNetDescriptorbbb : 1960 -> 1928
~ __ZN15BFNet_v1_FilterI10MFXDevice4E12encodeAtrousERS0_PU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS8_S8_S8_S8_S8_S8_S8_S8_S8_S8_PU19objcproto9MTLBuffer11objc_objectSA_fDv2_fSB_h : 2036 -> 1824
~ __ZN15BFNet_v1_FilterI10MFXDevice4ED2Ev : 292 -> 284
~ __ZN15BRNet_v3_FilterI10MFXDevice4EC2ERS0_PU21objcproto10MTLLibrary11objc_objectiiiiRK15BRNetDescriptoriibbbbbb : 3340 -> 3512
~ __ZN15BRNet_v3_FilterI10MFXDevice4E9encodePreEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS7_S7_S7_S7_PU19objcproto9MTLBuffer11objc_objectDv2_fSA_ffbbbfDv2_th : 2140 -> 2172
~ __ZN15BRNet_v3_FilterI10MFXDevice4E19encodePreForDenoiseEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS7_S7_S7_S7_S7_S7_S7_S7_PU19objcproto9MTLBuffer11objc_objectDv2_fSA_ffbbbfDv2_th : 1644 -> 1676
~ __ZN15BRNet_v3_FilterI10MFXDevice4E9encodeMidEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU21objcproto10MTLTexture11objc_objectS7_Dv2_fS8_bDv2_tS8_h : 1424 -> 1456
~ __ZN15BRNet_v3_FilterI10MFXDevice4E10encodePostEPU28objcproto17MTL4CommandBuffer11objc_objectR18MFXComputeEncoder4PU19objcproto9MTLBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS9_S9_S9_Dv2_fSA_fffbDv2_th : 1408 -> 1448
~ __ZN15BRNet_v3_FilterI10MFXDevice4ED2Ev : 436 -> 452
CStrings:
+ "emit_dbfnet_v3_2_constants.dat"
+ "emit_ubfnet_v3_2_constants.dat"
+ "internal_blend"
+ "internal_flow_adj_blend"
+ "tensor38_biasReshape"
+ "tensor45_biasReshape"
+ "tensor48_biasReshape"
+ "tensor52_biasReshape"
+ "tensor55_biasReshape"
+ "tensor70_biasReshape"
+ "tensor75_biasReshape"
+ "tensor78_biasReshape"
+ "tensor83_biasReshape"
+ "tensor86_biasReshape"
+ "tensor89_biasReshape"
- "concatTensors:dimension:interleave:name:"
- "emit_dbfnet_v3_constants.dat"
- "emit_ubfnet_v3_constants.dat"
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
- "tensor32"
- "tensor33"
- "tensor34"

```
