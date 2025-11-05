## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

```diff

-644.11.0.0.0
-  __TEXT.__text: 0x6513c
-  __TEXT.__auth_stubs: 0x1420
+657.10.0.0.0
+  __TEXT.__text: 0x65668
+  __TEXT.__auth_stubs: 0x1440
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x582c
-  __TEXT.__const: 0x53aa
+  __TEXT.__objc_methlist: 0x5d2c
+  __TEXT.__const: 0x537a
   __TEXT.__gcc_except_tab: 0x67c
-  __TEXT.__cstring: 0x468a
+  __TEXT.__cstring: 0x4759
   __TEXT.__oslogstring: 0x2793
-  __TEXT.__unwind_info: 0x16e8
-  __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xfde
-  __TEXT.__objc_methname: 0xac14
-  __TEXT.__objc_methtype: 0x1874
-  __TEXT.__objc_stubs: 0x9080
+  __TEXT.__unwind_info: 0x1760
+  __TEXT.__objc_classname: 0xfe1
+  __TEXT.__objc_methname: 0xad9d
+  __TEXT.__objc_methtype: 0x1885
+  __TEXT.__objc_stubs: 0x91c0
   __DATA_CONST.__got: 0x738
   __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ca8
+  __DATA_CONST.__objc_selrefs: 0x2d90
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0xa28
-  __AUTH_CONST.__const: 0x16b0
-  __AUTH_CONST.__cfstring: 0x4c40
-  __AUTH_CONST.__objc_const: 0x11a48
+  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__const: 0x16e0
+  __AUTH_CONST.__cfstring: 0x4d40
+  __AUTH_CONST.__objc_const: 0x11388
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x2df0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x598
+  __DATA.__objc_ivar: 0x5a8
   __DATA.__data: 0x1d58
-  __DATA.__bss: 0x7f0
+  __DATA.__bss: 0x800
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
   - /System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DFF8ACED-11E6-3C47-8C72-77E8B67CC399
-  Functions: 2207
-  Symbols:   6405
-  CStrings:  4150
+  UUID: BCAE0A81-641C-395D-8A35-A218BC3328B3
+  Functions: 2329
+  Symbols:   6570
+  CStrings:  4185
 
Symbols:
+ +[CIContext(IconServicesAdditions) _IS_sharedIconCompositorContext].cold.1
+ +[CUICatalog(IconServicesAdditions) _IS_coreGlyphsBundleURL].cold.1
+ +[ISAliasIcon aliasUUID].cold.1
+ +[ISAssetCatalogResource coreGlyphsCatalog].cold.1
+ +[ISCurrentDeviceIcon sharedInstance].cold.1
+ +[ISCustomIconManager defaultSpecialFolderTypeMapping].cold.1
+ +[ISCustomIconManager overrideTypeMapping].cold.1
+ +[ISCustomIconManager sharedInstance].cold.1
+ +[ISDefaults sharedInstance].cold.1
+ +[ISDeviceInfo sharedInstance].cold.1
+ +[ISGenericApplicationIcon sharedInstance].cold.1
+ +[ISGenericDocumentIcon sharedInstance].cold.1
+ +[ISGenericFolderIcon sharedInstance].cold.1
+ +[ISIcns(SystemIcons) genericAppIconResource].cold.1
+ +[ISIcns(SystemIcons) genericDocumentIconResource].cold.1
+ +[ISIcns(SystemIcons) notLoadedIconResource].cold.1
+ +[ISIcns(SystemIcons) placeholderIconResource].cold.1
+ +[ISIcon(CALayerDelegate) layerUpdateQueue].cold.1
+ +[ISIconCache defaultIconCache].cold.1
+ +[ISIconManager sharedInstance].cold.1
+ +[ISIconResourceLocator genericIconrResourceLocator].cold.1
+ +[ISImageStyleDescriptor defaultStyleDescriptor].cold.1
+ +[ISMutableIcns(ImageCoding) _iconIndexSmallerThanSize:scale:template:].cold.1
+ +[ISMutableIcns(ImageCoding) _iconIndexSmallerThanSize:scale:template:].cold.2
+ +[ISMutableIcns(ImageCoding) _scaledCGImage:forICSNSizeAtScale:template:scaleToFit:].cold.1
+ +[ISPlatformInfo sharedInstance].cold.1
+ +[ISPrefsCache sharedInstance].cold.1
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:]
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:].cold.1
+ +[ISShapeCompositorResource circleShape].cold.1
+ +[ISShapeCompositorResource continuousRoundedRectShape].cold.1
+ +[ISShapeCompositorResource tvOSRoundedRectShape].cold.1
+ +[ISStaticResources sharedInstance].cold.1
+ +[ISSymbol _generateVariantKeyFromOptions:].cold.2
+ +[ISTransparentIcon sharedInstance].cold.1
+ +[ISURLResourcePropertySpecification sharedInstance].cold.1
+ +[ISUnknownIcon sharedInstance].cold.1
+ +[ISVariant resourceTypes].cold.1
+ +[ISVolumeIcon IOKitPort].cold.1
+ +[ISVolumeIcon concreteIconForVolumeURL:].cold.2
+ +[LSRecord(IconServices) _is_remapLSDatabase].cold.1
+ +[NSBundle(IconServicesAdditions) __IS__frameworkBundle].cold.1
+ +[NSBundle(IconServicesAdditions) __IS__iconsetResourceBundle].cold.1
+ +[NSData(ISCompositorResourceValidationToken) _is_invalidToken].cold.1
+ +[NSData(ISCompositorResourceValidationToken) _is_staleToken].cold.1
+ +[NSData(ISCompositorResourceValidationToken) _is_validToken].cold.1
+ +[NSURL(IconServicesInternalAdditions) __is__isNetBoot].cold.1
+ +[NSURL(IconServicesInternalAdditions) _is_unregisteredPersonlityFileExtensions].cold.1
+ +[NSURL(UTIAdditions) __is_coreTypesURL].cold.1
+ +[NSXPCInterface(ISIconCacheServiceProtocol) _IS_iconCacheServiceInterface].cold.1
+ -[ISAliasIcon initWithCoder:].cold.1
+ -[ISAppNotificationBadgeRecipe hintedBadgeRect].cold.1
+ -[ISAppNotificationBadgeRecipe hintedMaskRect].cold.1
+ -[ISBundleIdentifierIcon bundleVersion]
+ -[ISCenterBadgeRecipe hintedBadgeRect].cold.1
+ -[ISCenterEmbossRecipe hintedBadgeRect].cold.1
+ -[ISCenterEmbossRecipe hintedFontSize].cold.1
+ -[ISCenterEmbossRecipe hintedImageBadgeRect].cold.1
+ -[ISClippingRecipe hintedBadgeRect].cold.1
+ -[ISClippingRecipe hintedCornerSize].cold.1
+ -[ISClippingRecipe hintedFontSize].cold.1
+ -[ISClippingRecipe hintedPageCurlSize].cold.1
+ -[ISClippingRecipe hintedPaperRect].cold.1
+ -[ISClippingRecipe hintedShadowBlur].cold.1
+ -[ISClippingRecipe hintedShadowOffset].cold.1
+ -[ISClippingRecipe hintedTextRect].cold.1
+ -[ISCompositVariantResourceLayer isActiveAtSize:].cold.3
+ -[ISCompositor analyticsSegmented]
+ -[ISCompositor setAnalyticsSegmented:]
+ -[ISDecoratedIcon initWithCoder:].cold.1
+ -[ISDefaults debugGraphicIconColor].cold.1
+ -[ISDefaults debugISIconGraphicIconColor].cold.1
+ -[ISDefaults debugPreDefinedGraphicIconColor].cold.1
+ -[ISDefaults forceApperance].cold.1
+ -[ISDefaults isDebugGraphicIconColourEnabled].cold.1
+ -[ISDefaults isIconSegmentationAnalyticsForAllIconsEnabled]
+ -[ISDefaults isUnsupportedDecorationDisabled].cold.1
+ -[ISDefaults prepareImageDelay].cold.1
+ -[ISDefaults tintColor].cold.1
+ -[ISEmbossedFolder hintedBadgeRect].cold.1
+ -[ISEmbossedFolder hintedFontSize].cold.1
+ -[ISEmbossedFolder hintedImageBadgeRect].cold.1
+ -[ISGenerationRequest(Generation) sendAnalytics:compositor:imageDescriptor:]
+ -[ISIcns(ImageCoding) CGImageWithData:iconIndexInfo:].cold.1
+ -[ISIcns(ImageCoding) copyCGImageWithIndex:].cold.1
+ -[ISIcns(ImageCoding) findMaskIndex:].cold.1
+ -[ISIcns(ImageCoding) findMaskIndex:].cold.2
+ -[ISIcns(ImageCoding) findMaskIndex:].cold.3
+ -[ISLeadingStatusBadgeRecipe leadingBottomBadgeRect].cold.1
+ -[ISMultipleFilesRecipe hintedCornerSize].cold.1
+ -[ISMultipleFilesRecipe hintedPageCurlSize].cold.1
+ -[ISMultipleFilesRecipe hintedPaperRect].cold.1
+ -[ISMultipleFilesRecipe hintedShadowBlur].cold.1
+ -[ISMultipleFilesRecipe hintedShadowOffset].cold.1
+ -[ISMultipleFilesRecipe hintedUnderPaperRect].cold.1
+ -[ISMutableIcns(ImageCoding) addCGImage:scale:error:].cold.2
+ -[ISMutableIcns(ImageCoding) addCGImage:scale:error:].cold.3
+ -[ISMutableIcns(ImageCoding) addImageData:iconIndex:].cold.1
+ -[ISSegmentDarkEffect hasSegmentedImage]
+ -[ISSegmentDarkEffect setHasSegmentedImage:]
+ -[ISSegmentTintEffect hasSegmentedImage]
+ -[ISSegmentTintEffect setHasSegmentedImage:]
+ -[ISTrailingStatusBadgeRecipe trailingBottomBadgeRect].cold.1
+ -[ISiOSAppClipRecipe appRect].cold.1
+ -[ISiOSAppClipRecipe blurRadius].cold.1
+ -[ISiOSAppOverhangingBadgeRecipe hintedBadgeRect].cold.1
+ -[ISiOSAppOverhangingBadgeRecipe hintedMainIconBadgeRect].cold.1
+ -[ISiOSMacAppRecipe badgeRect].cold.1
+ -[ISiOSMacAppRecipe hintedShadowBlur].cold.1
+ -[ISiOSMacAppRecipe hintedShadowOffset].cold.1
+ -[ISiosDocumentRecipe backgroundSizeForSize:scale:].cold.1
+ -[ISiosDocumentRecipe badgeSizeForSize:scale:].cold.1
+ -[ISiosmacDocumentRecipe hintedBadgeRect].cold.1
+ -[ISmacosDocumentRecipe hintedBadgeRect].cold.1
+ -[ISmacosDocumentRecipe hintedFontSize].cold.1
+ -[ISmacosDocumentRecipe hintedTextRect].cold.1
+ -[ISmacosDocumentRecipe1016 hintedBadgeRect].cold.1
+ -[ISmacosDocumentRecipe1016 hintedCornerSize].cold.1
+ -[ISmacosDocumentRecipe1016 hintedFontSize].cold.1
+ -[ISmacosDocumentRecipe1016 hintedPageCurlSize].cold.1
+ -[ISmacosDocumentRecipe1016 hintedPaperRect].cold.1
+ -[ISmacosDocumentRecipe1016 hintedShadowBlur].cold.1
+ -[ISmacosDocumentRecipe1016 hintedShadowOffset].cold.1
+ -[ISmacosDocumentRecipe1016 hintedShadowSpread].cold.1
+ -[ISmacosDocumentRecipe1016 hintedTextRect].cold.1
+ -[LSExtensionPointRecord(IconServicesAdditions) _IS_extensionsShouldFallbackToContainerIcon].cold.1
+ -[NSString(FileNameConventionAdditions) _IS_imageMetadataFromFileName].cold.3
+ -[NSString(FileNameConventionAdditions) _IS_scaleableResourceMetadataFromFileName].cold.3
+ ISIsResourceKey.cold.1
+ OBJC_IVAR_$_ISBundleIdentifierIcon._bundleVersion
+ OBJC_IVAR_$_ISCompositor._analyticsSegmented
+ OBJC_IVAR_$_ISSegmentDarkEffect._hasSegmentedImage
+ OBJC_IVAR_$_ISSegmentTintEffect._hasSegmentedImage
+ _AnalyticsSendEventLazy
+ _ISDefaultLog.cold.1
+ _ISGetCurrentColorSpace.cold.1
+ _ISIcnsIndexGetInfo.cold.1
+ _ISIconRefIntersectsCGRect.cold.1
+ _ISPrepareISIconSignpostLog.cold.1
+ _ISProcessIsInInstallEnvironment.cold.1
+ _ISTraceLog.cold.1
+ _ISURLCacheLog.cold.1
+ _IsBindingLoggingEnabled.cold.1
+ _IsRequestLoggingEnabled.cold.1
+ _ZL34_ISPixelSizeInfoIndexFromPixelSizej.cold.1
+ _ZN18CIconIndexIterator14_nextPixelSizeEv.cold.1
+ _ZN18CIconIndexIterator14_nextPixelSizeEv.cold.2
+ _ZN18CIconIndexIterator14_nextPixelSizeEv.cold.3
+ _ZN18CIconIndexIterator5resetEv.cold.1
+ __46-[ISIcns(ImageCoding) iconIndexForSize:scale:]_block_invoke.cold.1
+ ___76-[ISGenerationRequest(Generation) sendAnalytics:compositor:imageDescriptor:]_block_invoke
+ ___block_descriptor_59_e8_32s40s_e19_"NSDictionary"8?0l
+ __analyticsMessageCount
+ __lastAnalyticsStartDate
+ _arc4random_uniform
+ _objc_msgSend$analyticsSegmented
+ _objc_msgSend$appRecipeForPlatformStyle:descriptor:resourcePlatform:
+ _objc_msgSend$bundleVersion
+ _objc_msgSend$date
+ _objc_msgSend$hasSegmentedImage
+ _objc_msgSend$initWithTimeIntervalSinceNow:
+ _objc_msgSend$isIconSegmentationAnalyticsForAllIconsEnabled
+ _objc_msgSend$sendAnalytics:compositor:imageDescriptor:
+ _objc_msgSend$setAnalyticsSegmented:
+ _objc_msgSend$setHasSegmentedImage:
+ _objc_msgSend$timeIntervalSinceDate:
+ hintedShadowBlur.cold.1
+ hintedShadowSpread.cold.1
+ legacyResourceNames.cold.1
- +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:]
- +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:].cold.1
- _objc_msgSend$appRecipeForPlatformStyle:descriptor:
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "@40@0:8Q16@24Q32"
+ "HasDarkResources"
+ "HasTintedResources"
+ "HomeScreenStyle"
+ "Identifier"
+ "Segmentable"
+ "T@\"NSString\",R,V_bundleVersion"
+ "TB,N,V_analyticsSegmented"
+ "TB,V_hasSegmentedImage"
+ "Version"
+ "_analyticsSegmented"
+ "_bundleVersion"
+ "_hasSegmentedImage"
+ "analyticsSegmented"
+ "appRecipeForPlatformStyle:descriptor:resourcePlatform:"
+ "bundleVersion"
+ "com.apple.SpringBoard.Analytics.IconStatsMetric"
+ "date"
+ "hasSegmentedImage"
+ "icon_segmentation_analytics_for_all_icons"
+ "initWithTimeIntervalSinceNow:"
+ "isIconSegmentationAnalyticsForAllIconsEnabled"
+ "sendAnalytics:compositor:imageDescriptor:"
+ "setAnalyticsSegmented:"
+ "setHasSegmentedImage:"
+ "timeIntervalSinceDate:"
- "appRecipeForPlatformStyle:descriptor:"

```
