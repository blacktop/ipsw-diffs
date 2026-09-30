## CloudPhotoServices

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x72d8
-  __TEXT.__auth_stubs: 0x460
+840.1.220.0.0
+  __TEXT.__text: 0x7618
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x208
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x1d8
-  __TEXT.__cstring: 0x866
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__cstring: 0x8a5
   __TEXT.__oslogstring: 0x9fa
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a8
   __TEXT.__objc_classname: 0x46
   __TEXT.__objc_methname: 0x164f
   __TEXT.__objc_methtype: 0x2e6

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x540
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x198

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 998DE741-5F47-3A77-AF67-E4B0957D9791
+  UUID: 8A1BBAF1-9083-339C-9DAC-BBB4C2AB64FB
   Functions: 70
-  Symbols:   551
+  Symbols:   546
   CStrings:  345
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_storeStrong
Functions:
~ +[CloudPhotoServices _videoServiceClient] : 84 -> 100
~ +[CloudPhotoServices _imageServiceClient] : 84 -> 100
~ +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:] : 1740 -> 1748
~ ___CPLCloudPhotoServicesOSLogDomain : 84 -> 100
~ ___197+[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:]_block_invoke : 1176 -> 1224
~ +[CloudPhotoServices _shouldGenerateHDRMediumVideoDerivative] : 228 -> 232
~ +[CloudPhotoServices _shouldGenerateLargeVideoDerivativeForAVAsset:] : 516 -> 524
~ +[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:] : 4208 -> 4360
~ ___CPLDropDerivativesOSLogDomain : 84 -> 100
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke : 496 -> 516
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke_2 : 168 -> 172
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.139 : 184 -> 196
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.140 : 248 -> 256
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.141 : 112 -> 116
~ +[CloudPhotoServices _extractVideoMetadataResourceFrom:destinationDirectory:fingerprintScheme:] : 996 -> 1020
~ ___95+[CloudPhotoServices _extractVideoMetadataResourceFrom:destinationDirectory:fingerprintScheme:]_block_invoke_2 : 236 -> 240
~ +[CloudPhotoServices _createPosterFrameResourcesFromInputURL:withItemScopedIdentifier:includeDerivative:destinationDirectory:fingerprintScheme:outputResources:] : 584 -> 596
~ ___160+[CloudPhotoServices _createPosterFrameResourcesFromInputURL:withItemScopedIdentifier:includeDerivative:destinationDirectory:fingerprintScheme:outputResources:]_block_invoke : 112 -> 116
~ +[CloudPhotoServices _createCPLResourceFromURL:withResourceType:uniformType:itemScopedIdentifier:fingerprintScheme:] : 596 -> 584
~ +[CloudPhotoServices _createDerivativeResourcesFromInputURL:resourceTypes:withItemScopedIdentifier:destinationDirectory:fingerprintScheme:outputResources:convertToSRGB:] : 1204 -> 1240
~ ___169+[CloudPhotoServices _createDerivativeResourcesFromInputURL:resourceTypes:withItemScopedIdentifier:destinationDirectory:fingerprintScheme:outputResources:convertToSRGB:]_block_invoke : 112 -> 116
~ +[CloudPhotoServices _filenameForResourceWithItemScopedIdentifier:resourceType:extension:] : 244 -> 264
~ +[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:] : 368 -> 332
~ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_2 : 452 -> 444
~ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_3 : 2208 -> 2260
~ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.69 : 496 -> 516
~ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.93 : 124 -> 128
~ +[CloudPhotoServices generateFullSizeJPEGIfNecessaryFromInputResource:destinationDirectory:fingerprintScheme:completionHandler:] : 644 -> 660
~ ___128+[CloudPhotoServices generateFullSizeJPEGIfNecessaryFromInputResource:destinationDirectory:fingerprintScheme:completionHandler:]_block_invoke : 592 -> 608
~ +[CloudPhotoServices workQueue] : 84 -> 100
~ ___31+[CloudPhotoServices workQueue]_block_invoke : 92 -> 96
~ +[CloudPhotoServices generateDerivativeResourcesFromInputResource:withAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrameForVideo:completionHandler:] : 1384 -> 1448
~ +[CloudPhotoServices canGenerateImageDerivativesFromUTI:] : 80 -> 84
~ +[CloudPhotoServices isMovieUTI:] : 88 -> 92
~ +[CloudPhotoServices isUnsupportedOriginalFormatError:] : 108 -> 116
~ +[CloudPhotoServices involvedProcesses] : 84 -> 100
~ ___39+[CloudPhotoServices involvedProcesses]_block_invoke : 64 -> 68
~ +[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:] : 1632 -> 1668
~ ___120+[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:]_block_invoke : 396 -> 404
~ +[CloudPhotoServices generatePosterFrameForVideoAtURL:maximumPixelCount:destinationURL:reason:completionHandler:] : 872 -> 896
~ +[CloudPhotoServices generateGIFForVideoAtURL:destinationURL:completionHandler:] : 880 -> 912
~ +[CloudPhotoServices paMediaConversionColorSpaceForCloudPhotoDerivativeColorOutput:] : 32 -> 24
~ +[CloudPhotoServices resizeImageAtURL:destinationURL:options:completionHandler:] : 1396 -> 1456
~ +[CloudPhotoServices initialize] : 136 -> 140
~ +[CloudPhotoServicesUtilities getDimensionsFromImageProperties:orientationOut:widthOut:heightOut:] : 408 -> 448
~ +[CloudPhotoServicesUtilities newImageSourceFromImageAtURL:] : 284 -> 304
~ +[CloudPhotoServicesUtilities dimensionsForAVAsset:] : 244 -> 252
CStrings:
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/cloudphotolibrary/Framework/CloudPhotoServices/CloudPhotoServices.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/CloudPhotoServices/CloudPhotoServices.m"

```
