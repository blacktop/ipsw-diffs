## PhotosFileProvider

> `/System/Applications/Photos.app/Contents/PlugIns/PhotosFileProvider.appex/Contents/MacOS/PhotosFileProvider`

```diff

-700.27.103.0.0
-  __TEXT.__text: 0x26f0
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x10c
+700.21.101.0.0
+  __TEXT.__text: 0x559c
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x902
-  __TEXT.__oslogstring: 0x4b3
-  __TEXT.__cstring: 0x22c
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0xd5
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x2c0
+  __TEXT.__objc_methname: 0x1110
+  __TEXT.__oslogstring: 0x7e2
+  __TEXT.__cstring: 0x361
+  __TEXT.__objc_classname: 0x44
+  __TEXT.__objc_methtype: 0x141
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x2b0
-  __DATA.__objc_selrefs: 0x258
-  __DATA.__objc_ivar: 0x14
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x400
+  __DATA.__objc_selrefs: 0x430
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CPAnalytics.framework/Versions/A/CPAnalytics
+  - /System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/MediaConversionService
   - /System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosUICore.framework/Versions/A/PhotosUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 32
-  Symbols:   67
-  CStrings:  26
+  Functions: 62
+  Symbols:   105
+  CStrings:  36
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_PAImageConversionServiceClient
+ _OBJC_CLASS_$_PAMediaConversionServiceDefaultImageMetadataPolicy
+ _OBJC_CLASS_$_PAMediaConversionServiceResourceURLCollection
+ _OBJC_CLASS_$_PHAssetCollection
+ _OBJC_CLASS_$_PHAssetExportRequest
+ _OBJC_CLASS_$_PHAssetExportRequestOptions
+ _OBJC_CLASS_$_PHCollectionList
+ _OBJC_CLASS_$_PHFetchOptions
+ _OBJC_CLASS_$_PHPerson
+ _OBJC_CLASS_$_PHSocialGroup
+ _OBJC_CLASS_$_PXExportContainer
+ _OBJC_CLASS_$_UTType
+ _PAMediaConversionServiceOptionApplyOrientationTransformKey
+ _PAMediaConversionServiceOptionJobPriorityKey
+ _PAMediaConversionServiceOptionMaximumLongSideLengthKey
+ _PAMediaConversionServiceOptionMetadataPolicyKey
+ _PAMediaConversionServiceOptionOutputFileTypeKey
+ _PAMediaConversionServiceOptionRequestReasonKey
+ _PHAssetExportRequestLivePhotoBundleURLKey
+ _PHAssetExportRequestPhotoFileURLKey
+ _PHAssetExportRequestVideoFileURLKey
+ _PXFind
+ _PXPhotosFileProviderTypeIdentifierForDownscalingAssetWithTypeIdentifier
+ _PXPhotosFileProviderURLQueryItemClientEncodingPolicyKey
+ _PXPhotosFileProviderURLQueryItemDownscalingTargetDimensionKey
+ _PXPhotosFileProviderURLQueryItemIncludeCaptionKey
+ _PXPhotosFileProviderURLQueryItemIncludeLocationKey
+ _PXPhotosFileProviderURLQueryItemItemTypeKey
+ _PXPhotosFileProviderURLQueryItemVideoPresetKey
+ _PXPhotosFileProviderVariantsSortedByClientEncodingPolicy
+ ___kCFBooleanTrue
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _OBJC_CLASS_$_PXPhotosExportConfiguration
- _OBJC_CLASS_$_PXPhotosExportUtilities
CStrings:
+ "AssetFetchResult-%!l(MISSING)f"
+ "B16@?0@\"NSNumber\"8"
+ "CollectionList-%!l(MISSING)f"
+ "Failed to fetch PHAsset."
+ "Failed to find a variant."
+ "PUPhotosFileProviderItemProvider downscaling image to target length: %!@(MISSING)"
+ "UUID: %!@(MISSING), PhotoLibrary: %!@(MISSING), ItemType: %!l(MISSING)d, EncodingPolicy: %!l(MISSING)d, IncludeLocation: %!@(MISSING), IncludeCaption: %!@(MISSING), DownscalingTargetDimension: %!@(MISSING)"
+ "configuration"
+ "exportRequest"
+ "q"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@?0q8@\"NSDictionary\"16@\"NSError\"24"
- "UUID: %!@(MISSING), PhotoLibrary: %!@(MISSING), ExportConfiguration: %!@(MISSING)"
- "thumbnailSize != PXPhotosFileProviderThumbnailSizeUndefined"

```
