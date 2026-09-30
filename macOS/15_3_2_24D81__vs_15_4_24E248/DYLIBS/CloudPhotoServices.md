## CloudPhotoServices

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/Versions/A/CloudPhotoServices`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x7bb0
+751.0.104.0.0
+  __TEXT.__text: 0x7b98
   __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x1a8
+  __TEXT.__objc_methlist: 0x208
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__cstring: 0x990
   __TEXT.__oslogstring: 0x94c
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x155e
+  __TEXT.__objc_methname: 0x1584
   __TEXT.__objc_methtype: 0x2e3
   __TEXT.__objc_stubs: 0x1320
   __DATA_CONST.__got: 0x2b0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
+  __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x210
+  __AUTH_CONST.__objc_const: 0x198
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7487F2FC-6D68-34D3-9D47-5E7420D9387B
-  Functions: 82
-  Symbols:   451
-  CStrings:  347
+  UUID: 5AF454E2-B9D6-3DC6-A695-F8696BE30783
+  Functions: 83
+  Symbols:   452
+  CStrings:  348
 
Symbols:
+ +[CloudPhotoServices isTransientDerivativeGenerationError:]
+ __block_literal_global.251
+ __block_literal_global.254
- __block_literal_global.250
- __block_literal_global.253
Functions:
~ +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:error:] : 1880 -> 1856
~ +[CloudPhotoServices _shouldGenerateLargeVideoDerivativeForAVAsset:] : 532 -> 544
~ +[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:] : 3124 -> 3140
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke : 540 -> 544
~ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke_2 : 184 -> 176
~ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_2 : 2144 -> 2128
~ __176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.92 : 540 -> 544
~ +[CloudPhotoServices generateDerivativeResourcesFromInputResource:withAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrameForVideo:completionHandler:] : 1548 -> 1552
+ +[CloudPhotoServices isTransientDerivativeGenerationError:]
~ +[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:] : 2128 -> 2116
~ +[CloudPhotoServices generateGIFForVideoAtURL:destinationURL:completionHandler:] : 1184 -> 1192
~ +[CloudPhotoServices resizeImageAtURL:destinationURL:options:completionHandler:] : 1912 -> 1916
~ +[CloudPhotoServicesUtilities getDimensionsFromImageProperties:orientationOut:widthOut:heightOut:] : 480 -> 460
~ +[CloudPhotoServicesUtilities sizeOfImageAtURL:orientationOut:] : 172 -> 168
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/CloudPhotoServices/CloudPhotoServices.m"
+ "isTransientDerivativeGenerationError:"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/cloudphotolibrary/Framework/CloudPhotoServices/CloudPhotoServices.m"

```
