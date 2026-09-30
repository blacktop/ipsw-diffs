## CoreDisplay

> `/System/Library/Frameworks/CoreDisplay.framework/Versions/A/CoreDisplay`

```diff

-  __TEXT.__text: 0xe3514
+  __TEXT.__text: 0xe310c
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x178
   __TEXT.__dlopen_cstrs: 0x142
   __TEXT.__const: 0x5498
-  __TEXT.__gcc_except_tab: 0x8534
+  __TEXT.__gcc_except_tab: 0x8530
   __TEXT.__oslogstring: 0xbcc
   __TEXT.__cstring: 0x2178f
   __TEXT.__unwind_info: 0x3180
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9nqe220106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE : 1092 -> 1080
~ __IODisplayCreateInfoDictionary : 10192 -> 10076
~ __ZNSt3__13mapINS_4pairI12WireEncodingtEEyNS_4lessIS3_EENS_9allocatorINS1_IKS3_yEEEEEC2B9nqe220106ESt16initializer_listIS8_ERKS5_ : 428 -> 408
~ __ZNSt3__13mapINS_4pairI12WireEncoding9WireColorEEtNS_4lessIS4_EENS_9allocatorINS1_IKS4_tEEEEEC2B9nqe220106ESt16initializer_listIS9_ERKS6_ : 456 -> 436
~ _CGXExtendedDisplayStart : 1080 -> 1060
~ __ZN11CoreDisplay37CreateCoreDisplayStateDictWithOptionsEj : 27600 -> 27592
~ __ZNSt3__135__uninitialized_allocator_copy_implB9nqe220106INS_9allocatorI14CGSDisplayModeEEPS2_S4_S4_EET2_RT_T0_T1_S5_ : 296 -> 280
~ __ZNKSt3__111__copy_implclB9nqe220106IP15CGSDisplayStateS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_ : 240 -> 204
~ __ZL18update_cursor_dataP16CGXDisplayDevicePK12CursorBitmapb : 2576 -> 2564
~ __CDS_GetDisplaySystemState : 7520 -> 7508
~ ____ZN11CoreDisplay13GPUControllerC2Ev_block_invoke : 3624 -> 3612
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN11CoreDisplay13GPUController24RebuildMappedDisplayListEvE3$_0P16CGXMappedDisplayLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 5232 -> 5204
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN11CoreDisplay13GPUController24RebuildMappedDisplayListEvE3$_0P16CGXMappedDisplayEEbT1_S8_T0_ : 1452 -> 1432
~ __ZL14MPHWCopyRegionPK16CGXDisplayDeviceiP15CGSRegionObjectiij : 1828 -> 1800
~ __ZL14MPHWFillRegionP16CGXDisplayDeviceiP15CGSRegionObjectjj : 1992 -> 1988
~ __ZL14MPHWMoveRegionPK16CGXDisplayDeviceiP15CGSRegionObjectjiij : 2396 -> 2392
~ __ZL23get_display_device_infoP16CGXDisplayDevice : 5956 -> 5952
~ _CGRegionCreateBySimplifyingRegion : 1616 -> 1604
~ __ZNK11CoreDisplay16DisplayPipeStatecvNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEv : 2820 -> 2812
~ __ZN11CoreDisplay11DisplayPipe6CommitERKNS0_11TransactionEb : 11848 -> 11836
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN11CoreDisplay11DisplayPipe17RunGPUDisplayPipeEvE3$_3P6CGSizeLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 3000 -> 2940
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN11CoreDisplay11DisplayPipe17RunGPUDisplayPipeEvE3$_3P6CGSizeEEbT1_S8_T0_ : 748 -> 724
~ _WSDisplayAddActiveDisplaysToExternalDebuggingDictionary : 4980 -> 4960
~ _WSGLRegisterFramebufferService : 712 -> 692
~ _WSGLAssignUnitNumbers : 996 -> 940
~ _WSGLGetAssignedFramebufferUnitNumber : 228 -> 204
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbR19WSGLAcceleratorInfoS3_EPS2_Lb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 4920 -> 4648
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERPFbR19WSGLAcceleratorInfoS3_EPS2_EEbT1_S8_T0_ : 1164 -> 1124
~ __ZNSt3__16vectorI19WSGLFramebufferInfoNS_9allocatorIS1_EEE16__init_with_sizeB9nqe220106IPS1_S6_EEvT_T0_m : 384 -> 364
~ __ZN11CoreDisplay7SaveTGAEP11__IOSurfacePKcNSt3__16vectorI6CGRectNS4_9allocatorIS6_EEEES9_S9_ : 4776 -> 4732
~ ____ZN11CoreDisplayL49providerGetBytesAtPositionCallback_YCbYCr_surfaceEPvS0_xm_block_invoke : 268 -> 252
~ ____ZN11CoreDisplayL49providerGetBytesAtPositionCallback_CbYCrY_surfaceEPvS0_xm_block_invoke : 264 -> 256
~ ____ZN11CoreDisplayL53providerGetBytesAtPositionCallback_YCbYCrFull_surfaceEPvS0_xm_block_invoke : 268 -> 252
~ ____ZN11CoreDisplayL53providerGetBytesAtPositionCallback_CbYCrYFull_surfaceEPvS0_xm_block_invoke : 264 -> 256
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/Display/Display.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/DisplayPipe/DisplayPipe.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/Display.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/DisplayConfigure.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/MappedCursor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/MappedDisplay.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/Mux.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/IODisplay/VirtDisplay.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/Mach/Message.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/Renderer/Metal/MetalDevice.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/Surfaces/Surfaces.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ErK2e7/Sources/CoreDisplay/CoreDisplay/VirtualDisplay/VirtualDisplayClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/Display/Display.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/DisplayPipe/DisplayPipe.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/Display.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/DisplayConfigure.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/MappedCursor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/MappedDisplay.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/Mux.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/IODisplay/VirtDisplay.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/Mach/Message.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/Renderer/Metal/MetalDevice.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/Surfaces/Surfaces.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6uR5pC/Sources/CoreDisplay/CoreDisplay/VirtualDisplay/VirtualDisplayClient.mm"

```
