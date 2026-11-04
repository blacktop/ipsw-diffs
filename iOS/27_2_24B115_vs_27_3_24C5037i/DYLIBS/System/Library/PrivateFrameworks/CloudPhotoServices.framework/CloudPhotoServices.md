## CloudPhotoServices

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x79f8
-  __TEXT.__objc_methlist: 0x220
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x200
+920.7.110.0.0
+  __TEXT.__text: 0x7ad4
+  __TEXT.__objc_methlist: 0x238
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__cstring: 0x900
-  __TEXT.__oslogstring: 0xbd2
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__oslogstring: 0xbfe
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x578
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x198
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__common: 0x2
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 74
-  Symbols:   316
+  Functions: 76
+  Symbols:   318
   CStrings:  115
 
Symbols:
+ +[CloudPhotoServices shouldGenerateHDRMediumVideoDerivativeForOrientedPixelSize:sourceIsHDR:isVideoComplement:deviceHEVCCapabilities:]
+ +[CloudPhotoServices shouldGenerateLargeVideoDerivativeForOrientedPixelSize:creationDate:sourceIsHDR:isSpatialMedia:deviceHEVCCapabilities:]
+ +[CloudPhotoServices shouldGenerateMediumVideoDerivativeForOrientedPixelSize:]
+ +[CloudPhotoServices shouldGenerateVideoDerivativeForAVAsset:forResourceType:adjusted:isVideoComplement:]
+ GCC_except_table18
+ GCC_except_table27
+ ___140+[CloudPhotoServices shouldGenerateLargeVideoDerivativeForOrientedPixelSize:creationDate:sourceIsHDR:isSpatialMedia:deviceHEVCCapabilities:]_block_invoke
+ ___block_descriptor_66_e8_32s40s48bs_e25_B32?0"NSNumber"8Q16^B24ls48l8s32l8s40l8
+ _shouldGenerateLargeVideoDerivativeForOrientedPixelSize:creationDate:sourceIsHDR:isSpatialMedia:deviceHEVCCapabilities:.s_comparisonDate
+ _shouldGenerateLargeVideoDerivativeForOrientedPixelSize:creationDate:sourceIsHDR:isSpatialMedia:deviceHEVCCapabilities:.s_onceToken
- +[CloudPhotoServices _shouldGenerateHDRMediumVideoDerivative]
- +[CloudPhotoServices _shouldGenerateLargeVideoDerivativeForAVAsset:]
- GCC_except_table16
- GCC_except_table25
- ___68+[CloudPhotoServices _shouldGenerateLargeVideoDerivativeForAVAsset:]_block_invoke
- ___block_descriptor_65_e8_32s40s48bs_e25_B32?0"NSNumber"8Q16^B24ls48l8s32l8s40l8
- __shouldGenerateLargeVideoDerivativeForAVAsset:.s_comparisonDate
- __shouldGenerateLargeVideoDerivativeForAVAsset:.s_onceToken
CStrings:
+ "Should generate HDR medium video derivative (%d): HDR=%d videoComplement=%d dimensions=%.0fx%.0f deviceCapabilities=%u"
+ "Should generate medium video derivative (%d): dimensions=%.0fx%.0f"
- "Should generate HDR medium video derivative (%d): deviceCapabilities=%u"
- "Video resource %@ is HDR, requesting additional HDR medium derivative"
```
