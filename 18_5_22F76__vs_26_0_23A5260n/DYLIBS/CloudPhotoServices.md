## CloudPhotoServices

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x68d0
-  __TEXT.__auth_stubs: 0x470
+800.14.111.0.0
+  __TEXT.__text: 0x72d8
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x208
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__gcc_except_tab: 0x1d8
   __TEXT.__cstring: 0x866
-  __TEXT.__oslogstring: 0x979
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__oslogstring: 0x9fa
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x15a6
-  __TEXT.__objc_methtype: 0x2e3
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x298
+  __TEXT.__objc_methname: 0x164f
+  __TEXT.__objc_methtype: 0x2e6
+  __TEXT.__objc_stubs: 0x1400
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x540
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x198

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 230B5963-A968-3DEB-8910-933050BA5631
-  Functions: 65
-  Symbols:   529
-  CStrings:  336
+  UUID: C5250E9C-2D9B-3C26-971B-B4CA108A7125
+  Functions: 70
+  Symbols:   551
+  CStrings:  345
 
Symbols:
+ +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:]
+ GCC_except_table14
+ GCC_except_table23
+ _OBJC_CLASS_$_CPLErrors
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyAddPFMetadata
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyComposite
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyDefault
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.93
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_3
+ ___197+[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:]_block_invoke
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.132
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.139
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.140
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.141
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88r96r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e33_v24?0"CPLResource"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.119
+ ___block_literal_global.134
+ ___block_literal_global.144
+ ___block_literal_global.164
+ ___block_literal_global.167
+ ___block_literal_global.229
+ ___block_literal_global.232
+ _objc_msgSend$_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:
+ _objc_msgSend$currentProgress
+ _objc_msgSend$isCancelled
+ _objc_msgSend$operationCancelledError
+ _objc_msgSend$performAsCurrentWithPendingUnitCount:usingBlock:
+ _objc_msgSend$progressWithTotalUnitCount:
+ _objc_msgSend$setCompletedUnitCount:
- +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:error:]
- GCC_except_table20
- _OBJC_CLASS_$_PAMediaConversionServiceAddPFMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceCompositeImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceDefaultImageMetadataPolicy
- ___180+[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:error:]_block_invoke
- ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.131
- ___block_descriptor_104_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e33_v24?0"CPLResource"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.118
- ___block_literal_global.133
- ___block_literal_global.139
- ___block_literal_global.159
- ___block_literal_global.162
- ___block_literal_global.224
- ___block_literal_global.227
- _objc_msgSend$_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:error:
- _objc_retain_x28
CStrings:
+ "Added %@ from %@"
+ "B92@0:8@16@24@32Q40B48@52@60@68q76^@84"
+ "Derivatives generation of %@ for %@ has been cancelled"
+ "Derivatives generation of %@ for %@ has been interrupted by service"
+ "Derivatives generation of %@ for %@ has failed: %@"
+ "_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:"
+ "currentProgress"
+ "isCancelled"
+ "operationCancelledError"
+ "performAsCurrentWithPendingUnitCount:usingBlock:"
+ "progressWithTotalUnitCount:"
+ "setCompletedUnitCount:"
- "Added video metadata resource to derivative resource list: %@"
- "B84@0:8@16@24@32Q40B48@52@60@68^@76"
- "_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:error:"

```
