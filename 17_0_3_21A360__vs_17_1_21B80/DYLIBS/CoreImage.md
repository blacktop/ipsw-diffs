## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1400.68.0.0.0
-  __TEXT.__text: 0x2681d8
+1410.5.0.0.0
+  __TEXT.__text: 0x268b60
   __TEXT.__auth_stubs: 0x2de0
-  __TEXT.__objc_methlist: 0x147b8
-  __TEXT.__cstring: 0x9bc1a
+  __TEXT.__objc_methlist: 0x147cc
+  __TEXT.__cstring: 0x9bc4c
   __TEXT.__const: 0x94c0
-  __TEXT.__oslogstring: 0x7aec
-  __TEXT.__gcc_except_tab: 0x4190
+  __TEXT.__oslogstring: 0x7cbc
+  __TEXT.__gcc_except_tab: 0x41bc
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__runtimeheader: 0xb8e0
   __TEXT.__cikl2metal_pre: 0x47e
-  __TEXT.__unwind_info: 0x610c
+  __TEXT.__unwind_info: 0x6120
   __TEXT.__eh_frame: 0x240
   __TEXT.__objc_classname: 0x28a7
-  __TEXT.__objc_methname: 0x20e6c
-  __TEXT.__objc_methtype: 0x6d28
-  __TEXT.__objc_stubs: 0x11e80
+  __TEXT.__objc_methname: 0x20ee0
+  __TEXT.__objc_methtype: 0x6d91
+  __TEXT.__objc_stubs: 0x11ee0
   __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__const: 0x65a0
   __DATA_CONST.__objc_classlist: 0xfa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1cc90
-  __DATA_CONST.__objc_selrefs: 0x8b68
+  __DATA_CONST.__objc_const: 0x1cce0
+  __DATA_CONST.__objc_selrefs: 0x8b80
   __DATA_CONST.__objc_arraydata: 0x13e0
-  __AUTH_CONST.__cfstring: 0x1c300
+  __AUTH_CONST.__cfstring: 0x1c280
   __AUTH_CONST.__objc_const: 0xdf00
-  __AUTH_CONST.__const: 0xc098
+  __AUTH_CONST.__const: 0xc0d8
   __AUTH_CONST.__objc_doubleobj: 0x2800
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_dictobj: 0x460

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x5b8
   __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0x204c
+  __DATA.__objc_ivar: 0x2054
   __DATA.__data: 0x35c8
-  __DATA.__bss: 0x21d8
+  __DATA.__bss: 0x25e8
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x1a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8661A3A7-3038-3210-A432-59A1D69EB51F
-  Functions: 12904
-  Symbols:   37752
-  CStrings:  17912
+  UUID: 5A0231B8-907E-390A-9D45-B7B9BF7C37CE
+  Functions: 12917
+  Symbols:   37790
+  CStrings:  17924
 
Symbols:
+ +[CIContext loadArchive:].cold.1
+ +[CIContext loadArchive:].cold.2
+ +[CIContext loadArchive:].cold.3
+ +[CIContext loadArchiveWithName:fromURL:].cold.1
+ +[CIContext loadArchiveWithName:fromURL:].cold.2
+ +[CIContext loadArchiveWithName:fromURL:].cold.3
+ -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:]
+ -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:].cold.1
+ -[CIImageProcessorOutput setError:]
+ -[CIKernelLibrary url]
+ GCC_except_table60
+ _CI_DISABLE_LOADING_ARCHIVES_BY_NAME
+ _CI_DUMP_PROGRAM_LIBRARIES_TYPE
+ _OBJC_IVAR_$_CIImageProcessorOutput._task
+ _OBJC_IVAR_$_CIKernelLibrary._url
+ __OBJC_$_PROP_LIST_CIImageProcessorInput.132
+ __OBJC_$_PROP_LIST_CIImageProcessorOutput.115
+ __ZN2CI11ConvertNodeC2EPNS_4NodeENS_11ConvertTypeEbU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNSB_9allocatorISD_EEEEPbS5_S7_S9_SD_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI11MetalKernelC2EPKcP15CIKernelLibraryP12NSDictionaryS6_bb
+ __ZN2CI13ProcessorNode12set_callbackEU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI13ProcessorNode14append_to_treeEPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPSV_PKbSV_bbbbbb
+ __ZN2CI13ProcessorNode14append_to_treeEU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEPNS_8TileTaskEERKSA_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatESR_bbbb
+ __ZN2CI13ProcessorNodeC2EPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPSV_PKbSV_bbbbbb
+ __ZN2CI13ProcessorNodeC2EPNS_4NodeEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatESV_SV_bbbbbb
+ __ZN2CI13ProcessorNodeC2EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEPNS_8TileTaskEERKSA_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatESR_bbbb
+ __ZN2CI14ProcessorImageC1EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESG_PbSK_SM_SO_S3_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC1EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESD_PbSH_SJ_SL_S3_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC2EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESG_PbSK_SM_SO_S3_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC2EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESD_PbSH_SJ_SL_S3_bPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI19LegacyDAGDescriptorC2Eb
+ __ZN2CI31StitchableFunctionDAGDescriptorC2Eb
+ __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERSA_
+ __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERSA_.cold.1
+ __ZNK2CI11MetalKernel41useMTLFunctionBitCodeHashForProgramDigestEv
+ __ZNK2CI13ProcessorNode6renderEPNS_8TileTaskEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERSA_
+ __ZNSt3__115allocate_sharedB7v160006IN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEJRbEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB7v160006IN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEJRbEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__120__shared_ptr_emplaceIN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEEC2B7v160006IJRbEEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEEC2B7v160006IJRbEEES4_DpOT_
+ __ZThn80_N2CI21PrecompiledWarpKernelD0Ev
+ __ZThn80_N2CI21PrecompiledWarpKernelD1Ev
+ __ZThn80_N2CI22PrecompiledColorKernelD0Ev
+ __ZThn80_N2CI22PrecompiledColorKernelD1Ev
+ __ZThn80_N2CI24PrecompiledGeneralKernelD0Ev
+ __ZThn80_N2CI24PrecompiledGeneralKernelD1Ev
+ __ZThn80_NK2CI21PrecompiledWarpKernel12metal_kernelEv
+ __ZThn80_NK2CI21PrecompiledWarpKernel13add_to_digestERNS_12XXHashHelperE
+ __ZThn80_NK2CI21PrecompiledWarpKernel14metalConstantsEv
+ __ZThn80_NK2CI21PrecompiledWarpKernel18metalConstantTypesEv
+ __ZThn80_NK2CI21PrecompiledWarpKernel20metalConstantsDigestEv
+ __ZThn80_NK2CI22PrecompiledColorKernel12metal_kernelEv
+ __ZThn80_NK2CI22PrecompiledColorKernel13add_to_digestERNS_12XXHashHelperE
+ __ZThn80_NK2CI22PrecompiledColorKernel14metalConstantsEv
+ __ZThn80_NK2CI22PrecompiledColorKernel18metalConstantTypesEv
+ __ZThn80_NK2CI22PrecompiledColorKernel20metalConstantsDigestEv
+ __ZThn80_NK2CI24PrecompiledGeneralKernel12metal_kernelEv
+ __ZThn80_NK2CI24PrecompiledGeneralKernel13add_to_digestERNS_12XXHashHelperE
+ __ZThn80_NK2CI24PrecompiledGeneralKernel14metalConstantsEv
+ __ZThn80_NK2CI24PrecompiledGeneralKernel18metalConstantTypesEv
+ __ZThn80_NK2CI24PrecompiledGeneralKernel20metalConstantsDigestEv
+ __ZZ30CI_DUMP_PROGRAM_LIBRARIES_TYPEE1v
+ __ZZ30CI_DUMP_PROGRAM_LIBRARIES_TYPEE8didCheck
+ __ZZ35CI_DISABLE_LOADING_ARCHIVES_BY_NAMEE13archives_name
+ __ZZ35CI_DISABLE_LOADING_ARCHIVES_BY_NAMEE6is_set
+ __ZZ35CI_DISABLE_LOADING_ARCHIVES_BY_NAMEE8didCheck
+ ___54+[CIKernelLibrary(Internal) coreImageDylibWithDevice:]_block_invoke.94
+ ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.302
+ ___CI_DISABLE_LOADING_ARCHIVES_BY_NAME_block_invoke
+ ___CI_DUMP_PROGRAM_LIBRARIES_TYPE_block_invoke
+ ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.389
+ ____ZN2CI11MetalKernelC2EPKcP15CIKernelLibraryP12NSDictionaryS6_bb_block_invoke
+ ___block_descriptor_112_e8_32r40r48r56r64r72r80r88r_e22_B36?0^v8^v16i24i28i32lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8
+ ___block_descriptor_48_e8_32o40b_e286_v148?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132^v140ls32l8s40l8
+ ___block_descriptor_72_e8_32o40o48o56b_e286_v148?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132^v140ls56l8s32l8s40l8s48l8
+ ___block_literal_global.113
+ ___block_literal_global.239
+ ___block_literal_global.248
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.256
+ ___block_literal_global.286
+ ___block_literal_global.295
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.323
+ ___block_literal_global.92
+ _nameSurface
+ _objc_msgSend$allObjects
+ _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:
+ _objc_msgSend$url
- -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:]
- -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:].cold.1
- __OBJC_$_PROP_LIST_CIImageProcessorInput.127
- __OBJC_$_PROP_LIST_CIImageProcessorOutput.110
- __ZN2CI11ConvertNodeC2EPNS_4NodeENS_11ConvertTypeEbU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNSB_9allocatorISD_EEEEPbS5_S7_S9_SD_bPNS_7ContextEE
- __ZN2CI11MetalKernelC2EPKcP15CIKernelLibraryP12NSDictionaryS6_b
- __ZN2CI13ProcessorNode12set_callbackEU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEE
- __ZN2CI13ProcessorNode14append_to_treeEPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPST_PKbST_bbbbbb
- __ZN2CI13ProcessorNode14append_to_treeEU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEERKSA_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatESP_bbbb
- __ZN2CI13ProcessorNodeC2EPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPST_PKbST_bbbbbb
- __ZN2CI13ProcessorNodeC2EPNS_4NodeEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestES8_PbSC_SE_SG_S5_bPNS_7ContextEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEST_ST_bbbbbb
- __ZN2CI13ProcessorNodeC2EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestENSt3__16vectorI6CGRectNS8_9allocatorISA_EEEEPbS2_S4_S6_SA_bPNS_7ContextEERKSA_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatESP_bbbb
- __ZN2CI14ProcessorImageC1EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESG_PbSK_SM_SO_S3_bPNS_7ContextEE
- __ZN2CI14ProcessorImageC1EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESD_PbSH_SJ_SL_S3_bPNS_7ContextEE
- __ZN2CI14ProcessorImageC2EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESG_PbSK_SM_SO_S3_bPNS_7ContextEE
- __ZN2CI14ProcessorImageC2EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvPP11__IOSurfacePNS_7TextureEPNS_17NodeContentDigestESD_PbSH_SJ_SL_S3_bPNS_7ContextEE
- __ZN2CI19LegacyDAGDescriptorC2Ev
- __ZN2CI31StitchableFunctionDAGDescriptorC2Ev
- __ZNK2CI11ConvertNode6renderEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERS8_
- __ZNK2CI11ConvertNode6renderEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERS8_.cold.1
- __ZNK2CI13ProcessorNode6renderEPNS_7ContextEPPKNS_14intermediate_tEjPK6CGRectP11__IOSurfaceNS_7TextureERS8_
- __ZNSt3__115allocate_sharedB7v160006IN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006IN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__120__shared_ptr_emplaceIN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEEC2B7v160006IJEEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEEC2B7v160006IJEEES4_DpOT_
- __ZThn72_N2CI21PrecompiledWarpKernelD0Ev
- __ZThn72_N2CI21PrecompiledWarpKernelD1Ev
- __ZThn72_N2CI22PrecompiledColorKernelD0Ev
- __ZThn72_N2CI22PrecompiledColorKernelD1Ev
- __ZThn72_N2CI24PrecompiledGeneralKernelD0Ev
- __ZThn72_N2CI24PrecompiledGeneralKernelD1Ev
- __ZThn72_NK2CI21PrecompiledWarpKernel12metal_kernelEv
- __ZThn72_NK2CI21PrecompiledWarpKernel13add_to_digestERNS_12XXHashHelperE
- __ZThn72_NK2CI21PrecompiledWarpKernel14metalConstantsEv
- __ZThn72_NK2CI21PrecompiledWarpKernel18metalConstantTypesEv
- __ZThn72_NK2CI21PrecompiledWarpKernel20metalConstantsDigestEv
- __ZThn72_NK2CI22PrecompiledColorKernel12metal_kernelEv
- __ZThn72_NK2CI22PrecompiledColorKernel13add_to_digestERNS_12XXHashHelperE
- __ZThn72_NK2CI22PrecompiledColorKernel14metalConstantsEv
- __ZThn72_NK2CI22PrecompiledColorKernel18metalConstantTypesEv
- __ZThn72_NK2CI22PrecompiledColorKernel20metalConstantsDigestEv
- __ZThn72_NK2CI24PrecompiledGeneralKernel12metal_kernelEv
- __ZThn72_NK2CI24PrecompiledGeneralKernel13add_to_digestERNS_12XXHashHelperE
- __ZThn72_NK2CI24PrecompiledGeneralKernel14metalConstantsEv
- __ZThn72_NK2CI24PrecompiledGeneralKernel18metalConstantTypesEv
- __ZThn72_NK2CI24PrecompiledGeneralKernel20metalConstantsDigestEv
- ___54+[CIKernelLibrary(Internal) coreImageDylibWithDevice:]_block_invoke.89
- ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.320
- ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.407
- ____ZN2CI11MetalKernelC2EPKcP15CIKernelLibraryP12NSDictionaryS6_b_block_invoke
- ___block_descriptor_104_e8_32r40r48r56r64r72r80r_e22_B36?0^v8^v16i24i28i32lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
- ___block_descriptor_48_e8_32o40b_e281_v140?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132ls32l8s40l8
- ___block_descriptor_72_e8_32o40o48o56b_e281_v140?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132ls56l8s32l8s40l8s48l8
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.250
- ___block_literal_global.259
- ___block_literal_global.262
- ___block_literal_global.293
- ___block_literal_global.296
- ___block_literal_global.317
CStrings:
+ "%{public}s Failed finding %@ AIR archive"
+ "%{public}s Failed loading  %@ binary archive"
+ "%{public}s Failed loading %@ AIR archive"
+ "%{public}s Failed loading %@ AIR archive from %@"
+ "%{public}s Failed loading %@ binary archive from %@"
+ "%{public}s Loaded %@ CoreImage binary archive from url %@"
+ "%{public}s No %@ AIR archive found in %@"
+ "+[CIContext loadArchive:]"
+ "+[CIContext loadArchiveWithName:fromURL:]"
+ "-[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:]"
+ "@100@0:8^{__IOSurface=}16{Texture=(?=Q{?=II}{?=^v^v})}24Q40B48{CGRect={CGPoint=dd}{CGSize=dd}}52^v84^v92"
+ "An archive loaded with these functions %{public}@"
+ "CCPortrait.bundle"
+ "CCPortrait.bundle/CoreImageKernels.ci.metallib"
+ "CCPortrait.bundle/CoreImageKernels_only.ci.metallib"
+ "CI_DISABLE_LOADING_ARCHIVES_BY_NAME"
+ "CI_DUMP_PROGRAM_LIBRARIES_TYPE"
+ "Internal error: Input texture: (%.4s: %lu x %lu) has volatile backing (%s) surface"
+ "Internal error: Input texture: (%ld: %lu x %lu) has volatile backing (%s) surface"
+ "T@\"NSURL\",R,V_url"
+ "_task"
+ "_url"
+ "allObjects"
+ "ccportrait_builtins_archive"
+ "initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:"
+ "setError:"
+ "v148@?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132^v140"
- "-[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:]"
- "Failed finding %@ AIR archive"
- "Failed loading  %@ binary archive"
- "Failed loading %@ AIR archive"
- "Failed loading %@ AIR archive from %@"
- "Failed loading %@ binary archive from %@"
- "Internal error: Input texture: (%lu x %lu) has volatile backing surface: (%s)"
- "Loaded %@ AIR archive"
- "No %@ AIR archive found in %@"
- "ccportrait_archive"
- "v140@?0^^{__IOSurface}8^{Texture=(?=Q{?=II}{?=^v^v})}16^Q24{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}32^B56^{__IOSurface=}64{Texture=(?=Q{?=II}{?=^v^v})}72Q88{CGRect={CGPoint=dd}{CGSize=dd}}96B128^v132"

```
