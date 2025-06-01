## DocumentCamera

> `/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`

```diff

-153.0.0.0.0
-  __TEXT.__text: 0x8a194
+160.0.0.0.0
+  __TEXT.__text: 0x8abac
   __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_methlist: 0x7ec4
+  __TEXT.__objc_methlist: 0x7f7c
   __TEXT.__const: 0x5c8
-  __TEXT.__gcc_except_tab: 0x827c
-  __TEXT.__cstring: 0x3571
-  __TEXT.__oslogstring: 0x1a16
+  __TEXT.__gcc_except_tab: 0x830c
+  __TEXT.__cstring: 0x35a8
+  __TEXT.__oslogstring: 0x1b80
   __TEXT.__ustring: 0x3a8
   __TEXT.__dlopen_cstrs: 0x2f6
-  __TEXT.__unwind_info: 0x28dc
+  __TEXT.__unwind_info: 0x28f8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1067
-  __TEXT.__objc_methname: 0x1ad57
-  __TEXT.__objc_methtype: 0x4057
-  __TEXT.__objc_stubs: 0x12a00
-  __DATA_CONST.__got: 0x490
+  __TEXT.__objc_methname: 0x1b223
+  __TEXT.__objc_methtype: 0x40ad
+  __TEXT.__objc_stubs: 0x12cc0
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x1618
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12b78
-  __DATA_CONST.__objc_selrefs: 0x58d8
+  __DATA_CONST.__objc_const: 0x12c68
+  __DATA_CONST.__objc_selrefs: 0x5990
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x640
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__cfstring: 0x38a0
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__objc_doubleobj: 0x140
+  __AUTH_CONST.__cfstring: 0x38e0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xa58
-  __DATA.__objc_ivar: 0x9ec
+  __DATA.__objc_ivar: 0xa00
   __DATA.__data: 0xfa8
   __DATA.__bss: 0x238
-  __DATA_DIRTY.__const: 0x3b8
+  __DATA_DIRTY.__const: 0x378
   __DATA_DIRTY.__objc_const: 0x26f0
   __DATA_DIRTY.__objc_data: 0x1ef0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B1EE4A0-D84B-3DBA-B387-9F0F122ECF27
-  Functions: 3441
-  Symbols:   12266
-  CStrings:  5914
+  UUID: 6750A47E-95EF-37CE-AE13-8FE932D53A81
+  Functions: 3463
+  Symbols:   12337
+  CStrings:  5959
 
Symbols:
+ +[ICDocCamImageFilters colorDocument:orientation:constantColor:]
+ +[ICDocCamImageFilters colorDocument:orientation:filterName:filterAmount:filterKey:]
+ +[ICDocCamImageFilters filteredImage:imageFilterType:constantColor:]
+ +[ICDocCamImageFilters filteredImage:orientation:imageFilterType:constantColor:]
+ -[ICDocCamDocumentInfo constantColor]
+ -[ICDocCamDocumentInfo setConstantColor:]
+ -[ICDocCamPhotoCaptureDelegate captureOutput:didFinishProcessingPhoto:error:].cold.2
+ -[ICDocCamPhotoCaptureDelegate captureOutput:didFinishProcessingPhoto:error:].cold.3
+ -[ICDocCamPhotoCaptureDelegate constantColorCenterWeightedMeanConfidenceLevel]
+ -[ICDocCamPhotoCaptureDelegate constantColorDeliveredFallBackPhoto]
+ -[ICDocCamPhotoCaptureDelegate constantColorDeliveredOriginalPhoto]
+ -[ICDocCamPhotoCaptureDelegate imageAttributes]
+ -[ICDocCamPhotoCaptureDelegate setConstantColorCenterWeightedMeanConfidenceLevel:]
+ -[ICDocCamPhotoCaptureDelegate setConstantColorDeliveredFallBackPhoto:]
+ -[ICDocCamPhotoCaptureDelegate setConstantColorDeliveredOriginalPhoto:]
+ -[ICDocCamPhotoCaptureDelegate setImageAttributes:]
+ -[ICDocCamViewController cropAndFilterImage:rects:filterType:constantColor:]
+ -[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]
+ -[ICDocCamViewController isConstantColorAvailable]
+ -[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]
+ -[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:].cold.1
+ -[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:].cold.2
+ -[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:].cold.3
+ -[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:].cold.4
+ GCC_except_table101
+ GCC_except_table115
+ GCC_except_table122
+ GCC_except_table130
+ GCC_except_table139
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table201
+ GCC_except_table206
+ GCC_except_table210
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table256
+ GCC_except_table265
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table96
+ GCC_except_table98
+ _OBJC_IVAR_$_ICDocCamDocumentInfo._constantColor
+ _OBJC_IVAR_$_ICDocCamPhotoCaptureDelegate._constantColorCenterWeightedMeanConfidenceLevel
+ _OBJC_IVAR_$_ICDocCamPhotoCaptureDelegate._constantColorDeliveredFallBackPhoto
+ _OBJC_IVAR_$_ICDocCamPhotoCaptureDelegate._constantColorDeliveredOriginalPhoto
+ _OBJC_IVAR_$_ICDocCamPhotoCaptureDelegate._imageAttributes
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke.541
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke_2
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke_2.542
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke_3
+ ___104-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:]_block_invoke_4
+ ___45-[ICDocCamViewController setupCaptureSession]_block_invoke.344
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke.554
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.555
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.cold.1
+ ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.cold.2
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.69
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.69.cold.1
+ ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.69.cold.2
+ ___61-[ICDocCamThumbnailZoomTransitionAnimator animateTransition:]_block_invoke.18
+ ___61-[ICDocCamThumbnailZoomTransitionAnimator animateTransition:]_block_invoke_2.19
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke.529
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke.529.cold.1
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke.534
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke.537
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_2
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_2.530
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_2.535
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_3
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_3.531
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_3.536
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_3.536.cold.1
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_4
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_4.532
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_5
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_5.533
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_6
+ ___91-[ICDocCamViewController saveCapturedImage:metaData:rects:constantColor:completionHandler:]_block_invoke_7
+ ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.198
+ ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.198.cold.1
+ ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.198.cold.2
+ ___Block_byref_object_copy_.513
+ ___Block_byref_object_dispose_.514
+ ___block_descriptor_115_ea8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8r96l8
+ ___block_descriptor_48_ea8_32s40w_e88_v40?0"ICDocCamPhotoCaptureDelegate"8^{__CVBuffer=}16"NSDictionary"24"NSDictionary"32lw40l8s32l8
+ ___block_descriptor_65_ea8_32s40s48s56bs_e45_v32?0B8"UIImage"12"ICDocCamImageQuad"20B28ls32l8s40l8s48l8s56l8
+ ___block_descriptor_67_ea8_32s40s48r56w_e5_v8?0lr48l8w56l8s32l8s40l8
+ ___block_descriptor_73_ea8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.303
+ ___block_literal_global.319
+ ___block_literal_global.376
+ ___block_literal_global.656
+ __unnamed_array_storage.406
+ __unnamed_array_storage.413
+ __unnamed_array_storage.416
+ __unnamed_array_storage.482
+ __unnamed_array_storage.485
+ __unnamed_array_storage.682
+ _kCIInputAmountKey
+ _objc_msgSend$colorDocument:orientation:constantColor:
+ _objc_msgSend$colorDocument:orientation:filterName:filterAmount:filterKey:
+ _objc_msgSend$constantColor
+ _objc_msgSend$constantColorCenterWeightedMeanConfidenceLevel
+ _objc_msgSend$constantColorDeliveredFallBackPhoto
+ _objc_msgSend$constantColorDeliveredOriginalPhoto
+ _objc_msgSend$cropAndFilterImage:rects:filterType:constantColor:
+ _objc_msgSend$detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:
+ _objc_msgSend$filteredImage:orientation:imageFilterType:constantColor:
+ _objc_msgSend$imageAttributes
+ _objc_msgSend$isConstantColorAvailable
+ _objc_msgSend$isConstantColorEnabled
+ _objc_msgSend$isConstantColorFallbackPhoto
+ _objc_msgSend$isConstantColorFallbackPhotoDeliveryEnabled
+ _objc_msgSend$isConstantColorSupported
+ _objc_msgSend$saveCapturedImage:metaData:rects:constantColor:completionHandler:
+ _objc_msgSend$setConstantColor:
+ _objc_msgSend$setConstantColorCenterWeightedMeanConfidenceLevel:
+ _objc_msgSend$setConstantColorClippingRecoveryEnabled:
+ _objc_msgSend$setConstantColorDeliveredFallBackPhoto:
+ _objc_msgSend$setConstantColorDeliveredOriginalPhoto:
+ _objc_msgSend$setConstantColorEnabled:
+ _objc_msgSend$setConstantColorFallbackPhotoDeliveryEnabled:
+ _objc_msgSend$setConstantColorSaturationBoostEnabled:
+ _objc_msgSend$setImageAttributes:
- -[ICDocCamViewController cropAndFilterImage:rects:filterType:]
- -[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]
- -[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]
- -[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:].cold.1
- -[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:].cold.2
- -[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:].cold.3
- -[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:].cold.4
- GCC_except_table102
- GCC_except_table116
- GCC_except_table123
- GCC_except_table131
- GCC_except_table140
- GCC_except_table146
- GCC_except_table148
- GCC_except_table150
- GCC_except_table161
- GCC_except_table163
- GCC_except_table171
- GCC_except_table178
- GCC_except_table187
- GCC_except_table195
- GCC_except_table202
- GCC_except_table207
- GCC_except_table212
- GCC_except_table218
- GCC_except_table221
- GCC_except_table225
- GCC_except_table227
- GCC_except_table232
- GCC_except_table235
- GCC_except_table238
- GCC_except_table249
- GCC_except_table251
- GCC_except_table257
- GCC_except_table266
- GCC_except_table281
- GCC_except_table284
- GCC_except_table309
- GCC_except_table94
- GCC_except_table97
- GCC_except_table99
- ___45-[ICDocCamViewController setupCaptureSession]_block_invoke.341
- ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke.549
- ___49-[ICDocCamViewController snapStillImageWithMode:]_block_invoke_2.550
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66.cold.1
- ___55-[ICRemoteDocCamViewController sidecarRequestDidFinish]_block_invoke.66.cold.2
- ___61-[ICDocCamThumbnailZoomTransitionAnimator animateTransition:]_block_invoke.15
- ___61-[ICDocCamThumbnailZoomTransitionAnimator animateTransition:]_block_invoke_2.16
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.524
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.524.cold.1
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.529
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke.532
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.525
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_2.530
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.526
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.531
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_3.531.cold.1
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_4
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_4.527
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_5
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_5.528
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_6
- ___77-[ICDocCamViewController saveCapturedImage:metaData:rects:completionHandler:]_block_invoke_7
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke.536
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_2
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_2.537
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_3
- ___90-[ICDocCamViewController detectRectanglesAndSaveCapturedImage:metadata:completionHandler:]_block_invoke_4
- ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.191
- ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.191.cold.1
- ___92+[ICDocCamDocumentInfoCollection infoCollectionFromImageSidecarItems:imageCache:completion:]_block_invoke.191.cold.2
- ___Block_byref_object_copy_.508
- ___Block_byref_object_dispose_.509
- ___block_descriptor_114_ea8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8r96l8
- ___block_descriptor_48_ea8_32s40w_e71_v32?0"ICDocCamPhotoCaptureDelegate"8^{__CVBuffer=}16"NSDictionary"24lw40l8s32l8
- ___block_descriptor_64_ea8_32s40s48s56bs_e45_v32?0B8"UIImage"12"ICDocCamImageQuad"20B28ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_ea8_32s40s48r56w_e5_v8?0lr48l8w56l8s32l8s40l8
- ___block_descriptor_72_ea8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.300
- ___block_literal_global.316
- ___block_literal_global.371
- ___block_literal_global.651
- __unnamed_array_storage.401
- __unnamed_array_storage.408
- __unnamed_array_storage.411
- __unnamed_array_storage.477
- __unnamed_array_storage.480
- __unnamed_array_storage.677
- _objc_msgSend$cropAndFilterImage:rects:filterType:
- _objc_msgSend$detectRectanglesAndSaveCapturedImage:metadata:completionHandler:
- _objc_msgSend$saveCapturedImage:metaData:rects:completionHandler:
CStrings:
+ "\"\x13"
+ "@32@0:8@16s24B28"
+ "@36@0:8@16q24B32"
+ "@40@0:8@16@24s32B36"
+ "@40@0:8@16q24s32B36"
+ "@52@0:8@16q24@32f40@44"
+ "CIDocumentEnhancer"
+ "T@\"NSMutableDictionary\",&,N,V_imageAttributes"
+ "TB,N,V_constantColor"
+ "TB,N,V_constantColorDeliveredFallBackPhoto"
+ "TB,N,V_constantColorDeliveredOriginalPhoto"
+ "Tf,N,V_constantColorCenterWeightedMeanConfidenceLevel"
+ "_constantColor"
+ "_constantColorCenterWeightedMeanConfidenceLevel"
+ "_constantColorDeliveredFallBackPhoto"
+ "_constantColorDeliveredOriginalPhoto"
+ "_imageAttributes"
+ "captureOutput:didFinishProcessingPhoto: ignoring constant color original capture since it didn't meet the minimum confidence level (got %f)"
+ "captureOutput:didFinishProcessingPhoto: using original capture since it met the minimum confidence level (got %f)"
+ "colorDocument:orientation:constantColor:"
+ "colorDocument:orientation:filterName:filterAmount:filterKey:"
+ "constantColor"
+ "constantColorCenterWeightedMeanConfidenceLevel"
+ "constantColorDeliveredFallBackPhoto"
+ "constantColorDeliveredOriginalPhoto"
+ "constantColorPhoto"
+ "cropAndFilterImage:rects:filterType:constantColor:"
+ "detectRectanglesAndSaveCapturedImage:metadata:constantColor:completionHandler:"
+ "filteredImage:imageFilterType:constantColor:"
+ "filteredImage:orientation:imageFilterType:constantColor:"
+ "imageAttributes"
+ "isConstantColorAvailable"
+ "isConstantColorEnabled"
+ "isConstantColorFallbackPhoto"
+ "isConstantColorFallbackPhotoDeliveryEnabled"
+ "isConstantColorSupported"
+ "saveCapturedImage:metaData:rects:constantColor:completionHandler:"
+ "setConstantColor:"
+ "setConstantColorCenterWeightedMeanConfidenceLevel:"
+ "setConstantColorClippingRecoveryEnabled:"
+ "setConstantColorDeliveredFallBackPhoto:"
+ "setConstantColorDeliveredOriginalPhoto:"
+ "setConstantColorEnabled:"
+ "setConstantColorFallbackPhotoDeliveryEnabled:"
+ "setConstantColorSaturationBoostEnabled:"
+ "setImageAttributes:"
+ "snapStillImage: color constancy NOT enabled for capture"
+ "snapStillImage: color constancy enabled for capture"
+ "v40@?0@\"ICDocCamPhotoCaptureDelegate\"8^{__CVBuffer=}16@\"NSDictionary\"24@\"NSDictionary\"32"
+ "v44@0:8^{__CVBuffer=}16@24B32@?36"
+ "v52@0:8@16@24@32B40@?44"
- "\x12\x12"
- "@36@0:8@16@24s32"
- "cropAndFilterImage:rects:filterType:"
- "detectRectanglesAndSaveCapturedImage:metadata:completionHandler:"
- "saveCapturedImage:metaData:rects:completionHandler:"
- "v32@?0@\"ICDocCamPhotoCaptureDelegate\"8^{__CVBuffer=}16@\"NSDictionary\"24"
- "v40@0:8^{__CVBuffer=}16@24@?32"
- "v48@0:8@16@24@32@?40"

```
