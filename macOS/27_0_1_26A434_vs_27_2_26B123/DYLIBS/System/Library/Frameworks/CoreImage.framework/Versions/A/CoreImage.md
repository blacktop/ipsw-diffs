## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage`

```diff

-1667.21.2.0.0
-  __TEXT.__text: 0x352bcc
-  __TEXT.__objc_methlist: 0x16078
+1667.40.6.0.0
+  __TEXT.__text: 0x354f38
+  __TEXT.__objc_methlist: 0x160b0
   __TEXT.__const: 0xe268
-  __TEXT.__gcc_except_tab: 0xaa58
-  __TEXT.__cstring: 0x105a08
-  __TEXT.__oslogstring: 0xb95c
-  __TEXT.__dlopen_cstrs: 0x3fd
+  __TEXT.__gcc_except_tab: 0xaaa8
+  __TEXT.__cstring: 0x105c24
+  __TEXT.__oslogstring: 0xba57
+  __TEXT.__dlopen_cstrs: 0x445
   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
   __TEXT.__cruft: 0x36d1
-  __TEXT.__unwind_info: 0xaab0
+  __TEXT.__unwind_info: 0xab30
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4690
+  __DATA_CONST.__const: 0x46a8
   __DATA_CONST.__objc_classlist: 0x10c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9098
+  __DATA_CONST.__objc_selrefs: 0x90c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1478
-  __DATA_CONST.__got: 0xb38
-  __AUTH_CONST.__const: 0x10440
-  __AUTH_CONST.__cfstring: 0x1de40
-  __AUTH_CONST.__objc_const: 0x2bdf0
+  __DATA_CONST.__got: 0xb68
+  __AUTH_CONST.__const: 0x10500
+  __AUTH_CONST.__cfstring: 0x1df60
+  __AUTH_CONST.__objc_const: 0x2be10
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xde0
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_doubleobj: 0x2a50
   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__auth_got: 0x1808
+  __AUTH_CONST.__auth_got: 0x1848
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x9880
+  __AUTH.__objc_data: 0x97e0
   __AUTH.__data: 0x277f0
   __DATA.__objc_ivar: 0x200c
   __DATA.__data: 0x6668
   __DATA.__bss: 0x3628
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0xb28
+  __DATA_DIRTY.__bss: 0xb38
   __DATA_DIRTY.__common: 0x230
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15314
-  Symbols:   29336
-  CStrings:  9009
+  Functions: 15349
+  Symbols:   29393
+  CStrings:  9027
 
Symbols:
+ +[CIContextCache currentEntryCount]
+ +[CIContextCache peakEntryCount]
+ +[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]
+ -[CIImage isMonochrome]
+ -[CIRAWFilterImpl rawSensorPattern]
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table195
+ GCC_except_table286
+ GCC_except_table313
+ GCC_except_table315
+ GCC_except_table339
+ GCC_except_table349
+ GetSurfaceCacheEntryCount
+ GetSurfaceCachePeakEntryCount
+ RawCameraLibraryCore.frameworkLibrary
+ _CGColorSpaceContainsISO5Metadata
+ _CGColorSpaceCopyColorSyncProfile
+ _CGColorSpaceGetISO5Headroom
+ _CIRAWFilterDownloadNotNeeded
+ _CIRAWFilterStartDownload
+ _ColorSyncProfileCopyData
+ _ColorSyncProfileCreate
+ _ColorSyncProfileCreateCopyWithISO5Metadata
+ _ColorSyncProfileGetCICPInfo
+ _ColorSyncProfileGetISO5AverageLightLevel
+ _GetSurfaceCacheEntryCount
+ _GetSurfaceCachePeakEntryCount
+ _OBJC_CLASS_$_NSLock
+ _RawCameraLibraryCore
+ _ZN2CIL25fillBlockFromDataProviderEP14CGDataProvidermP11__IOSurface
+ __CIRAWFilterStartDownload_block_invoke
+ __ZL19CreateNewMTLTexturePU19objcproto9MTLDevice11objc_objectP11__IOSurfacej
+ __ZL21CCPortraitLibraryCorePPc
+ __ZN2CI44ColorSpaceCreateCopyWithISO5HeadroomMetadataEP12CGColorSpaceff
+ __ZN2CI6CGNode15restore_cgimageENS_10ImageIndexENS_22ImageLeafContentDigestEP7CGImageS4_PU28objcproto17OS_dispatch_queue8NSObject
+ __ZN2CI6CGNodeC1EiNS_10ImageIndexEP7CGImageS3_NS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
+ __ZN2CI6CGNodeC2EiNS_10ImageIndexEP7CGImageS3_NS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
+ __ZN2CI7CGImage18updateDecodedImageEv
+ __ZN2CIL22subdivide_program_roisEPNS_7ContextEmPNS_4NodeE6CGRectPNSt3__13mapIPKS2_NS_13useCountDepthENS5_4lessIS8_EENS5_9allocatorINS5_4pairIKS8_S9_EEEEEEbRKNS5_6vectorIS8_NSC_IS8_EEEERNS5_5dequeIPKNS_11ProgramNodeENSC_ISR_EEEERSL_Rm
+ __ZN2CIL25fillBlockFromDataProviderEP14CGDataProvidermP11__IOSurface
+ __ZN2CIL27pqOrExtendedRangeLightlevelEP12CGColorSpace
+ __ZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERmm
+ __ZNK2CI18TagColorSpaceImage10lightlevelEv
+ __ZZN2CI7CGImage18updateDecodedImageEvEN3$_08__invokeEPvPKvm
+ __ZZN2CI7CGImage18updateDecodedImageEvEN3$_18__invokeEPvPKvm
+ __ZZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEEmEN13SignpostTimerD1Ev
+ __ZZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERmmEN13SignpostTimerD1Ev
+ ___102-[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:]_block_invoke
+ ___CIRAWFilterDownloadNotNeeded_block_invoke
+ ___CIRAWFilterStartDownload_block_invoke
+ ___GetSurfaceCacheEntryCount_block_invoke
+ ___GetSurfaceCachePeakEntryCount_block_invoke
+ ___RawCameraLibraryCore_block_invoke
+ ____ZL14getFlexMapInfoPK15CGImageMetadata_block_invoke
+ ____ZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEEm_block_invoke
+ ____ZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEEm_block_invoke_2
+ ____ZN2CIL25fillBlockFromDataProviderEP14CGDataProvidermP11__IOSurface_block_invoke
+ ___block_descriptor_48_e8_32o40b_e8_v12?0B8l
+ ___block_descriptor_56_e8_32o40b48r_e17_v16?0"NSError"8l
+ ___block_descriptor_76_e23_v16?0r^{__IOSurface=}8l
+ ___copy_helper_block_e8_32o40b48r
+ ___destroy_helper_block_e8_32o40b48r
+ ___getRCModelDownloadStartSymbolLoc_block_invoke
+ __getRCModelDownloadStartSymbolLoc_block_invoke
+ _audit_stringRawCamera
+ _getRCModelDownloadStartSymbolLoc
+ _kColorSyncAverageLightLevel
+ _kColorSyncCLLInfo
+ _kColorSyncMaxLightLevel
+ _kColorSyncPrimaries
+ _kColorSyncReferenceWhite
+ _objc_msgSend$rawSensorPattern
+ getRCModelDownloadStartSymbolLoc.ptr
- GCC_except_table158
- GCC_except_table159
- GCC_except_table167
- GCC_except_table171
- GCC_except_table183
- GCC_except_table216
- GCC_except_table324
- GCC_except_table360
- GCC_except_table90
- __ZL27_cgImageProviderGetPropertyP15CGImageProviderPK10__CFString
- __ZN2CI6CGNode15restore_cgimageENS_10ImageIndexENS_22ImageLeafContentDigestEP7CGImagePU28objcproto17OS_dispatch_queue8NSObject
- __ZN2CI6CGNodeC1EiNS_10ImageIndexEP7CGImageNS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
- __ZN2CI6CGNodeC2EiNS_10ImageIndexEP7CGImageNS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
- __ZN2CIL22subdivide_program_roisEPNS_7ContextEPNS_4NodeE6CGRectPNSt3__13mapIPKS2_NS_13useCountDepthENS5_4lessIS8_EENS5_9allocatorINS5_4pairIKS8_S9_EEEEEEbRKNS5_6vectorIS8_NSC_IS8_EEEERNS5_5dequeIPKNS_11ProgramNodeENSC_ISR_EEEERSL_Rm
- __ZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERm
- __ZZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEEEN13SignpostTimerD1Ev
- __ZZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERmEN13SignpostTimerD1Ev
- ___62-[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]_block_invoke
- ____ZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEE_block_invoke
- ____ZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEE_block_invoke_2
- ___block_descriptor_60_e23_v16?0r^{__IOSurface=}8l
- _kCIImageRepresentationSemanticSegmentationSkyMatteImage_block_invoke
CStrings:
+ "%{public}s Raw demosaic filter produced no image; the decoder's on-demand resources may be unavailable."
+ "%{public}s RawCamera is not available on this platform."
+ "%{public}s Unable to soft link RCModelDownloadStart from RawCamera."
+ "+[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]"
+ "-[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]"
+ "/System/Library/CoreServices/RawCamera.bundle/Contents/MacOS/RawCamera"
+ "1667.40.6"
+ "CGImage base address (%p) is not aligned to its pixel size (%lu bytes)!\n"
+ "CIRAWFilter.m"
+ "CIRAWFilterErrorDomain"
+ "Cannot get the provider from a CGImage.\n"
+ "Failed to access data provider bytes."
+ "Failed to download %@."
+ "Failed to load CoreImage.metallib from %{public}@: %{public}@\n"
+ "Failed to serialize CoreImage.metallib from %{public}@ to %{public}@: %{public}@\n"
+ "NSProgress *CI_RCModelDownloadStart(uint32_t, int, void (^)(BOOL))"
+ "RCModelDownloadStart"
+ "Source data provider is nil."
+ "Timed out downloading %@."
+ "inputPattern"
+ "softlink:o:path:/System/Library/CoreServices/RawCamera.bundle/RawCamera"
+ "softlink:o:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
+ "the RAW decoder resources"
+ "the resources required to decode this image"
+ "v16@?0@\"NSError\"8"
+ "void *RawCameraLibrary(void)"
+ "workingformat=%s "
- "\noutputFormat=%s"
- "\nthreadgroupsPerGrid=(%d,%d,%d)"
- "\nthreadsPerGroup=(%d,%d,%d)"
- "%{public}s a CIImageProcessorInput with a empty region cannot be accessed via its base address."
- "1667.21.2"
- "Failed loading CoreImage.metallib from %{public}@: %{public}@\n"
- "Source image provider is nil."
- "_inputImage != nil"
- "softlink:r:path:/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait"
```
