## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1667.40.3.0.0
-  __TEXT.__text: 0x342700
-  __TEXT.__objc_methlist: 0x159d0
+1667.40.5.0.0
+  __TEXT.__text: 0x34396c
+  __TEXT.__objc_methlist: 0x159f0
   __TEXT.__const: 0xe198
-  __TEXT.__gcc_except_tab: 0xa87c
-  __TEXT.__cstring: 0x104a1a
-  __TEXT.__oslogstring: 0xb275
-  __TEXT.__dlopen_cstrs: 0x3fd
+  __TEXT.__gcc_except_tab: 0xa8b4
+  __TEXT.__cstring: 0x104bb8
+  __TEXT.__oslogstring: 0xb37e
+  __TEXT.__dlopen_cstrs: 0x445
   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0xc800
+  __TEXT.__unwind_info: 0xc860
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6528
+  __DATA_CONST.__const: 0x65b8
   __DATA_CONST.__objc_classlist: 0x1078
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e68
+  __DATA_CONST.__objc_selrefs: 0x8e78
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1488
-  __DATA_CONST.__got: 0xb20
+  __DATA_CONST.__got: 0xb28
   __AUTH_CONST.__const: 0xde40
-  __AUTH_CONST.__cfstring: 0x1dba0
+  __AUTH_CONST.__cfstring: 0x1dcc0
   __AUTH_CONST.__objc_const: 0x2b4e0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xdc8

   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0x1898
-  __AUTH.__objc_data: 0x9dd0
+  __AUTH.__objc_data: 0x9a88
   __AUTH.__data: 0x278a0
   __DATA.__objc_ivar: 0x1fc0
   __DATA.__data: 0x67a8
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__objc_data: 0xa28
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x688
+  __DATA_DIRTY.__bss: 0x6a0
   __DATA_DIRTY.__common: 0x22c
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15173
-  Symbols:   28608
-  CStrings:  8883
+  Functions: 15193
+  Symbols:   28629
+  CStrings:  8900
 
Symbols:
+ -[CIImage isMonochrome]
+ -[CIRAWFilterImpl rawSensorPattern]
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table186
+ GCC_except_table331
+ GCC_except_table341
+ _CIRAWFilterDownloadNotNeeded
+ _CIRAWFilterStartDownload
+ _OBJC_CLASS_$_NSLock
+ _RawCameraLibraryCore
+ _RawCameraLibraryCore.frameworkLibrary
+ __ZN2CI6CGNode15restore_cgimageENS_10ImageIndexENS_22ImageLeafContentDigestEP7CGImageS4_PU28objcproto17OS_dispatch_queue8NSObject
+ __ZN2CI6CGNodeC1EiNS_10ImageIndexEP7CGImageS3_NS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
+ __ZN2CI6CGNodeC2EiNS_10ImageIndexEP7CGImageS3_NS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
+ __ZN2CI7CGImage18updateDecodedImageEv
+ __ZN2CIL25fillBlockFromDataProviderEP14CGDataProvidermP11__IOSurface
+ __ZZN2CI7CGImage18updateDecodedImageEvEN3$_08__invokeEPvPKvm
+ __ZZN2CI7CGImage18updateDecodedImageEvEN3$_18__invokeEPvPKvm
+ ___CIRAWFilterDownloadNotNeeded_block_invoke
+ ___CIRAWFilterStartDownload_block_invoke
+ ___CIRAWFilterStartDownload_block_invoke_2
+ ___CIRAWFilterStartDownload_block_invoke_3
+ ___RawCameraLibraryCore_block_invoke
+ ____ZN2CIL25fillBlockFromDataProviderEP14CGDataProvidermP11__IOSurface_block_invoke
+ ___block_descriptor_48_e8_32o40b_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_56_e8_32o40b48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_76_e23_v16?0r^{__IOSurface=}8l
+ ___getRCModelDownloadStartSymbolLoc_block_invoke
+ _audit_stringRawCamera
+ _getRCModelDownloadStartSymbolLoc
+ _getRCModelDownloadStartSymbolLoc.ptr
+ _objc_msgSend$rawSensorPattern
- GCC_except_table147
- GCC_except_table157
- GCC_except_table161
- GCC_except_table165
- GCC_except_table172
- GCC_except_table185
- GCC_except_table318
- GCC_except_table342
- GCC_except_table352
- __ZL27_cgImageProviderGetPropertyP15CGImageProviderPK10__CFString
- __ZN2CI6CGNode15restore_cgimageENS_10ImageIndexENS_22ImageLeafContentDigestEP7CGImagePU28objcproto17OS_dispatch_queue8NSObject
- __ZN2CI6CGNodeC1EiNS_10ImageIndexEP7CGImageNS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
- __ZN2CI6CGNodeC2EiNS_10ImageIndexEP7CGImageNS_22ImageLeafContentDigestEPU28objcproto17OS_dispatch_queue8NSObjectNS_11PixelFormatENS_8EdgeModeEbb
- ___62-[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]_block_invoke
- ___65+[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]_block_invoke
- ___block_descriptor_60_e23_v16?0r^{__IOSurface=}8l
CStrings:
+ "%{public}s Raw demosaic filter produced no image; the decoder's on-demand resources may be unavailable."
+ "%{public}s RawCamera is not available on this platform."
+ "%{public}s Unable to soft link RCModelDownloadStart from RawCamera."
+ "+[CIRAWFilter downloadAllResourcesWithTimeout:completionHandler:]"
+ "-[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]"
+ "1667.40.5"
+ "CIRAWFilter.m"
+ "CIRAWFilterErrorDomain"
+ "Failed to access data provider bytes."
+ "Failed to download %@."
+ "NSProgress *CI_RCModelDownloadStart(uint32_t, int, void (^)(BOOL))"
+ "RCModelDownloadStart"
+ "Source data provider is nil."
+ "Timed out downloading %@."
+ "inputPattern"
+ "softlink:o:path:/System/Library/CoreServices/RawCamera.bundle/RawCamera"
+ "the RAW decoder resources"
+ "the resources required to decode this image"
+ "v16@?0@\"NSError\"8"
+ "void *RawCameraLibrary(void)"
- "1667.40.3"
- "Source image provider is nil."
- "_inputImage != nil"
```
