## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-657.10.0.0.0
-  __TEXT.__text: 0x48330
-  __TEXT.__auth_stubs: 0xd00
+705.100.0.0.0
+  __TEXT.__text: 0x5ce6c
+  __TEXT.__auth_stubs: 0xfd0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x4e2c
-  __TEXT.__const: 0x4638
-  __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x37a0
-  __TEXT.__oslogstring: 0x26d5
-  __TEXT.__unwind_info: 0x1280
-  __TEXT.__objc_classname: 0xd4f
-  __TEXT.__objc_methname: 0x965c
-  __TEXT.__objc_methtype: 0x127a
-  __TEXT.__objc_stubs: 0x7960
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x838
-  __DATA_CONST.__objc_classlist: 0x400
-  __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xc0
+  __TEXT.__objc_methlist: 0x62b4
+  __TEXT.__const: 0x48f2
+  __TEXT.__gcc_except_tab: 0x40c
+  __TEXT.__cstring: 0x526a
+  __TEXT.__oslogstring: 0x2da4
+  __TEXT.__swift5_typeref: 0x8
+  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__objc_classname: 0x11bb
+  __TEXT.__objc_methname: 0xbcd7
+  __TEXT.__objc_methtype: 0x1740
+  __TEXT.__objc_stubs: 0x93c0
+  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__objc_classlist: 0x518
+  __DATA_CONST.__objc_catlist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2730
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0xe20
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0xe578
-  __AUTH_CONST.__objc_intobj: 0x450
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x2f78
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x3c8
+  __DATA_CONST.__objc_arraydata: 0xc08
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__const: 0xea0
+  __AUTH_CONST.__cfstring: 0x6780
+  __AUTH_CONST.__objc_const: 0x12c60
+  __AUTH_CONST.__objc_intobj: 0x510
+  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x4e4
-  __DATA.__data: 0x1920
-  __DATA.__bss: 0x500
-  __DATA_DIRTY.__objc_data: 0x2350
+  __AUTH.__objc_data: 0xae0
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x680
+  __DATA.__data: 0x1c40
+  __DATA.__bss: 0x578
+  __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
+  - /System/Library/PrivateFrameworks/IconRendering.framework/IconRendering
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD505F70-EF28-3800-B94F-2DCCAC23B461
-  Functions: 1900
-  Symbols:   7287
-  CStrings:  3424
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 0FC3B73F-D276-30DC-85A9-68F863211103
+  Functions: 2398
+  Symbols:   9014
+  CStrings:  4727
 
Symbols:
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:]
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:].cold.1
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:].cold.2
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:].cold.3
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:].cold.4
+ +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:platform:].cold.5
+ +[IFColor(FolderAdditions) folderColor]
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:error:]
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:].cold.1
+ +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:].cold.2
+ +[ISCompositingDescriptor assetAppearanceForAppearance:appearanceVariant:]
+ +[ISFolderIconConfiguration supportsSecureCoding]
+ +[ISGenerationReport generationReportWithCustomRenderedTag:]
+ +[ISIconFactory _iconForURL:options:].cold.12
+ +[ISShapeDetection categorizeShapeWithWidth:height:cornerRadius:]
+ +[ISShapeDetection standardCornerRadiusForSize:]
+ +[ISStaticIconStackAssetCatalogResource _platformCatalogWithName:]
+ +[ISStaticIconStackAssetCatalogResource _platformCatalogWithName:].cold.1
+ +[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap]
+ +[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap].cold.1
+ +[ISStaticIconStackAssetCatalogResource iOSCatalog]
+ +[ISStaticIconStackAssetCatalogResource macOSCatalog]
+ +[ISStaticIconStackAssetCatalogResource watchOSCatalog]
+ -[CUICatalog(IconServicesAdditions) _IS_iconStackWithName:scale:locale:platform:appearance:]
+ -[CUICatalog(IconServicesAdditions) _IS_possibleIconStackExistsWithName:platform:]
+ -[CUINamedIconLayerStack(IconServicesAdditions) _IS_finalizedIconWithCompositingDescriptor:]
+ -[CUINamedIconLayerStack(IconServicesAdditions) _IS_finalizedIconWithCompositingDescriptor:].cold.1
+ -[CUINamedIconLayerStack(IconServicesAdditions) _IS_finalizedIconWithCompositingDescriptor:].cold.2
+ -[CUINamedIconLayerStack(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]
+ -[CUINamedIconLayerStack(IconServicesAdditions) _IS_imageWithSize:scale:platform:appearance:appearanceVariant:tintColor:isLegacy:background:]
+ -[CUINamedLookup(IconServicesAdditions) _IS_assetAppearance]
+ -[CUINamedMultisizeImage(IconServicesAdditions) _IS_iconStackWithRequestedAppearance:]
+ -[CUINamedMultisizeImage(IconServicesAdditions) _IS_nameWithRequestedAppearance:]
+ -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]
+ -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:].cold.1
+ -[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:].cold.2
+ -[IFImage(GenerationReport) generationReport]
+ -[IFImage(GenerationReport) setGenerationReport:]
+ -[IFImage(GenerationReport) setGenerationReport:].cold.1
+ -[IFImage(Internal) initWithIconStack:size:scale:]
+ -[IFImage(Internal) initWithIconStack:size:scale:].cold.1
+ -[ISAssetCatalogResource _tagForLongLife:]
+ -[ISAssetCatalogResource appearanceVariant]
+ -[ISAssetCatalogResource assetAppearance]
+ -[ISAssetCatalogResource background]
+ -[ISAssetCatalogResource initWithCatalog:imageName:platform:]
+ -[ISAssetCatalogResource setAppearanceVariant:]
+ -[ISAssetCatalogResource setBackground:]
+ -[ISAssetCatalogResource setShouldApplyMask:]
+ -[ISAssetCatalogResource setSuggestedRecipe:]
+ -[ISAssetCatalogResource setTintColor:]
+ -[ISAssetCatalogResource shouldApplyMask]
+ -[ISAssetCatalogResource suggestedRecipe]
+ -[ISAssetCatalogResource tintColor]
+ -[ISBiasedGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:samples:]
+ -[ISBiasedGrayscaleConversion energyRatio]
+ -[ISBiasedGrayscaleConversion init]
+ -[ISBiasedGrayscaleConversion saturation]
+ -[ISBiasedGrayscaleConversion setEnergyRatio:]
+ -[ISBiasedGrayscaleConversion setSaturation:]
+ -[ISCompositingDescriptor .cxx_destruct]
+ -[ISCompositingDescriptor CUINamedImageDeviceClass]
+ -[ISCompositingDescriptor CUINamedImageDeviceClass].cold.1
+ -[ISCompositingDescriptor ICRAppearance]
+ -[ISCompositingDescriptor ICRRenderingMode]
+ -[ISCompositingDescriptor appearanceVariant]
+ -[ISCompositingDescriptor appearance]
+ -[ISCompositingDescriptor assetAppearance]
+ -[ISCompositingDescriptor background]
+ -[ISCompositingDescriptor copyWithZone:]
+ -[ISCompositingDescriptor initWithImageDescriptor:]
+ -[ISCompositingDescriptor init]
+ -[ISCompositingDescriptor platformStyle]
+ -[ISCompositingDescriptor platform]
+ -[ISCompositingDescriptor scale]
+ -[ISCompositingDescriptor serializeLayerObjectForCaching]
+ -[ISCompositingDescriptor setAppearance:]
+ -[ISCompositingDescriptor setAppearanceVariant:]
+ -[ISCompositingDescriptor setBackground:]
+ -[ISCompositingDescriptor setPlatform:]
+ -[ISCompositingDescriptor setPlatformStyle:]
+ -[ISCompositingDescriptor setScale:]
+ -[ISCompositingDescriptor setSerializeLayerObjectForCaching:]
+ -[ISCompositingDescriptor setShouldApplyMask:]
+ -[ISCompositingDescriptor setSize:]
+ -[ISCompositingDescriptor setTintColor:]
+ -[ISCompositingDescriptor setUseLegacyCompatibilityMode:]
+ -[ISCompositingDescriptor shouldApplyMask]
+ -[ISCompositingDescriptor size]
+ -[ISCompositingDescriptor tintColor]
+ -[ISCompositingDescriptor updateWithImageDescriptor:]
+ -[ISCompositingDescriptor useLegacyCompatibilityMode]
+ -[ISDefaults featureOverride]
+ -[ISDefaults forceApperanceVariant]
+ -[ISDefaults forceApperanceVariant].cold.1
+ -[ISDefaults forceSymbolEmbossment]
+ -[ISDefaults forceSymbolEmbossment].cold.1
+ -[ISDefaults iconStackAppIconsAllowed]
+ -[ISDefaults isEnhancedGlassEnabled]
+ -[ISDefaults isInjectSolariumAssetsEnabled]
+ -[ISDefaults isSolariumCornerRadiusEnabled]
+ -[ISDefaults isSolariumEnabled]
+ -[ISDefaults isUniversalGladeEnabled]
+ -[ISDefaults metalCacheURL]
+ -[ISDocumentRecipe badgeWithSymbol]
+ -[ISDocumentRecipe curlResource]
+ -[ISDocumentRecipe hasBespokeBackground]
+ -[ISDocumentRecipe hasText]
+ -[ISDocumentRecipe hintedBadgeRect]
+ -[ISDocumentRecipe hintedPaperRect]
+ -[ISDocumentRecipe hintedShadowBlur]
+ -[ISDocumentRecipe hintedShadowBlur].cold.1
+ -[ISDocumentRecipe hintedShadowOffset]
+ -[ISDocumentRecipe hintedShadowOffset].cold.1
+ -[ISDocumentRecipe hintedShadowSpread]
+ -[ISDocumentRecipe hintedShadowSpread].cold.1
+ -[ISDocumentRecipe hintedSymbolFontSize]
+ -[ISDocumentRecipe hintedTextFontSize]
+ -[ISDocumentRecipe hintedTextRect]
+ -[ISDocumentRecipe iconSpecification]
+ -[ISDocumentRecipe layerTreeForSize:scale:]
+ -[ISDocumentRecipe maskBadgeResource]
+ -[ISDocumentRecipe pageResource]
+ -[ISDocumentRecipe platform]
+ -[ISDocumentRecipe setBadgeWithSymbol:]
+ -[ISDocumentRecipe setHasBespokeBackground:]
+ -[ISDocumentRecipe setHasText:]
+ -[ISDocumentRecipe setMaskBadgeResource:]
+ -[ISDocumentRecipe setPlatform:]
+ -[ISDocumentRecipe setTreatLikeSymbol:]
+ -[ISDocumentRecipe treatLikeSymbol]
+ -[ISFallbackIconDarkSegmented .cxx_destruct]
+ -[ISFallbackIconDarkSegmented darkImage]
+ -[ISFallbackIconDarkSegmented dealloc]
+ -[ISFallbackIconDarkSegmented drawsLightingEffects]
+ -[ISFallbackIconDarkSegmented feedback]
+ -[ISFallbackIconDarkSegmented initWithDarkImage:drawsLightingEffects:feedback:]
+ -[ISFallbackIconFactory _createDarkFallbackIcon_iOS]
+ -[ISFallbackIconFactory _createDarkFallbackIcon_macOS]
+ -[ISFallbackIconFactory _createLightFallbackIcon_iOS]
+ -[ISFallbackIconFactory _createLightFallbackIcon_macOS]
+ -[ISFallbackIconFactory _createTintedFallbackIcon_iOS]
+ -[ISFallbackIconFactory _createTintedFallbackIcon_macOS]
+ -[ISFallbackIconFactory createDarkFallbackIcon]
+ -[ISFallbackIconFactory createLightFallbackIcon]
+ -[ISFallbackIconFactory createTintedFallbackIcon]
+ -[ISFallbackIconFactory dealloc]
+ -[ISFallbackIconFactory initWithCGImage:idiom:]
+ -[ISFallbackIconFill .cxx_destruct]
+ -[ISFallbackIconFill dealloc]
+ -[ISFallbackIconFill feedback]
+ -[ISFallbackIconFill foregroundAndLightingEffectsImage]
+ -[ISFallbackIconFill image]
+ -[ISFallbackIconFill initWithImage:foregroundAndLightingEffectsImage:feedback:]
+ -[ISFallbackIconScaleDown .cxx_destruct]
+ -[ISFallbackIconScaleDown cornerRadius]
+ -[ISFallbackIconScaleDown dealloc]
+ -[ISFallbackIconScaleDown image]
+ -[ISFallbackIconScaleDown initWithImage:cornerRadius:]
+ -[ISFallbackIconTintedSegmented .cxx_destruct]
+ -[ISFallbackIconTintedSegmented dealloc]
+ -[ISFallbackIconTintedSegmented drawsLightingEffects]
+ -[ISFallbackIconTintedSegmented feedback]
+ -[ISFallbackIconTintedSegmented initWithTintableImage:drawsLightingEffects:feedback:]
+ -[ISFallbackIconTintedSegmented tintableImage]
+ -[ISFlattenLayerStackAssetCatalogResource imageForSize:scale:]
+ -[ISFloydGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:samples:]
+ -[ISFolderIconConfiguration .cxx_destruct]
+ -[ISFolderIconConfiguration colorString]
+ -[ISFolderIconConfiguration description]
+ -[ISFolderIconConfiguration digest]
+ -[ISFolderIconConfiguration emoji]
+ -[ISFolderIconConfiguration encodeWithCoder:]
+ -[ISFolderIconConfiguration folderEmpty]
+ -[ISFolderIconConfiguration hasTint]
+ -[ISFolderIconConfiguration initWithCoder:]
+ -[ISFolderIconConfiguration initWithIconDictionary:]
+ -[ISFolderIconConfiguration initWithSymbolName:systemTintColor:]
+ -[ISFolderIconConfiguration initWithSymbolName:tintColor:]
+ -[ISFolderIconConfiguration init]
+ -[ISFolderIconConfiguration plistExcerpt]
+ -[ISFolderIconConfiguration resolvedTintColorForAppearance:]
+ -[ISFolderIconConfiguration setEmoji:]
+ -[ISFolderIconConfiguration setFolderEmpty:]
+ -[ISFolderIconConfiguration setSymbolName:]
+ -[ISFolderIconConfiguration setSystemTintColor:]
+ -[ISFolderIconConfiguration setTintColor:]
+ -[ISFolderIconConfiguration symbolName]
+ -[ISFolderIconConfiguration systemTintColor]
+ -[ISFolderIconConfiguration tintColor]
+ -[ISFolderIconConfigurationParser initWithIconDictionary:]
+ -[ISFolderIconConfigurationParser initWithInfoDictionary:]
+ -[ISFolderIconConfigurationParser tintColor]
+ -[ISFolderRecipe .cxx_destruct]
+ -[ISFolderRecipe disableShadow]
+ -[ISFolderRecipe hintedBadgeRect]
+ -[ISFolderRecipe hintedBadgeRect].cold.1
+ -[ISFolderRecipe hintedFontSize]
+ -[ISFolderRecipe hintedFontSize].cold.1
+ -[ISFolderRecipe hintedImageBadgeRect]
+ -[ISFolderRecipe hintedImageBadgeRect].cold.1
+ -[ISFolderRecipe layerTreeForSize:scale:]
+ -[ISFolderRecipe setDisableShadow:]
+ -[ISFolderRecipe setTintColor:]
+ -[ISFolderRecipe tintColor]
+ -[ISFolderRecipe updateRecipeWithImageDescriptor:]
+ -[ISForegroundSegmentation computeMaskWithWidth:height:samples:foregroundMask:]
+ -[ISGenerationReport customRenderedTag]
+ -[ISGenerationReport hasLightingEffects]
+ -[ISGenerationReport iconTreatment]
+ -[ISGenerationReport initWithIconTreatment:hasLightingEffects:]
+ -[ISGenerationResponse setSharedMemory:]
+ -[ISGenerationResponse sharedMemory]
+ -[ISGraphicIconConfigurationParser aliasedConfigurationDictionary]
+ -[ISGraphicIconConfigurationParser enclosureColors]
+ -[ISGraphicIconConfigurationParser renderingMode]
+ -[ISGraphicIconConfigurationParser symbolColors]
+ -[ISGraphicIconConfigurationParser symbolName]
+ -[ISGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:samples:]
+ -[ISIcon _activeSignpostsForDescriptor:]
+ -[ISIcon _tweakCopiedImageDescriptorsIfNecessary:]
+ -[ISIconConfigurationMarkupParser .cxx_destruct]
+ -[ISIconConfigurationMarkupParser colorsForKey:]
+ -[ISIconConfigurationMarkupParser configDict]
+ -[ISIconConfigurationMarkupParser initWithConfigurationDictionary:]
+ -[ISIconConfigurationMarkupParser symbolName]
+ -[ISIconFactory initWithBundleIdentifier:imageLayers:]
+ -[ISIconFactory initWithType:iconConfiguration:]
+ -[ISIconFactory initWithTypeIdentifier:iconLayers:]
+ -[ISIconFactory initWithTypeIdentifier:layerGroups:]
+ -[ISIconLayer hasLightEffects]
+ -[ISIconLayer imageBag]
+ -[ISIconLayer images]
+ -[ISIconLayer initWithImages:]
+ -[ISIconLayer setHasLightEffects:]
+ -[ISIconLayerElement .cxx_destruct]
+ -[ISIconLayerElement effects]
+ -[ISIconLayerElement fillColorForAppearance:]
+ -[ISIconLayerElement fillColor]
+ -[ISIconLayerElement fillColors]
+ -[ISIconLayerElement fills]
+ -[ISIconLayerElement hasEffectsForAppearance:]
+ -[ISIconLayerElement hasEffects]
+ -[ISIconLayerElement imageBag]
+ -[ISIconLayerElement images]
+ -[ISIconLayerElement initWithImages:]
+ -[ISIconLayerElement opacities]
+ -[ISIconLayerElement opacityForAppearance:]
+ -[ISIconLayerElement opacity]
+ -[ISIconLayerElement setEffects:]
+ -[ISIconLayerElement setFillColor:]
+ -[ISIconLayerElement setFillColor:forAppearance:]
+ -[ISIconLayerElement setFillColors:]
+ -[ISIconLayerElement setFills:]
+ -[ISIconLayerElement setHasEffects:]
+ -[ISIconLayerElement setHasEffects:forAppearance:]
+ -[ISIconLayerElement setOpacities:]
+ -[ISIconLayerElement setOpacity:]
+ -[ISIconLayerElement setOpacity:forAppearance:]
+ -[ISIconLayerGroup .cxx_destruct]
+ -[ISIconLayerGroup blurForAppearance:]
+ -[ISIconLayerGroup blur]
+ -[ISIconLayerGroup blurs]
+ -[ISIconLayerGroup combineSpeculars]
+ -[ISIconLayerGroup hasOverlappingChildSpecularsCombinedForAppearance:]
+ -[ISIconLayerGroup hasOverlappingChildSpecularsCombined]
+ -[ISIconLayerGroup hasSpecularForAppearance:]
+ -[ISIconLayerGroup hasSpecular]
+ -[ISIconLayerGroup initWithLayers:]
+ -[ISIconLayerGroup layers]
+ -[ISIconLayerGroup opacities]
+ -[ISIconLayerGroup opacityForAppearance:]
+ -[ISIconLayerGroup opacity]
+ -[ISIconLayerGroup setBlur:]
+ -[ISIconLayerGroup setBlur:forAppearance:]
+ -[ISIconLayerGroup setBlurs:]
+ -[ISIconLayerGroup setCombineSpeculars:]
+ -[ISIconLayerGroup setHasOverlappingChildSpecularsCombined:]
+ -[ISIconLayerGroup setHasOverlappingChildSpecularsCombined:forAppearance:]
+ -[ISIconLayerGroup setHasSpecular:]
+ -[ISIconLayerGroup setHasSpecular:forAppearance:]
+ -[ISIconLayerGroup setLayers:]
+ -[ISIconLayerGroup setOpacities:]
+ -[ISIconLayerGroup setOpacity:]
+ -[ISIconLayerGroup setOpacity:forAppearance:]
+ -[ISIconLayerGroup setShadow:]
+ -[ISIconLayerGroup setShadow:forAppearance:]
+ -[ISIconLayerGroup setShadowStyle:]
+ -[ISIconLayerGroup setShadowStyle:forAppearance:]
+ -[ISIconLayerGroup setShadowStyles:]
+ -[ISIconLayerGroup setShadows:]
+ -[ISIconLayerGroup setSpeculars:]
+ -[ISIconLayerGroup setTranslucencies:]
+ -[ISIconLayerGroup setTranslucency:]
+ -[ISIconLayerGroup setTranslucency:forAppearance:]
+ -[ISIconLayerGroup shadowForAppearance:]
+ -[ISIconLayerGroup shadowStyleForAppearance:]
+ -[ISIconLayerGroup shadowStyle]
+ -[ISIconLayerGroup shadowStyles]
+ -[ISIconLayerGroup shadow]
+ -[ISIconLayerGroup shadows]
+ -[ISIconLayerGroup speculars]
+ -[ISIconLayerGroup translucencies]
+ -[ISIconLayerGroup translucencyForAppearance:]
+ -[ISIconLayerGroup translucency]
+ -[ISIconPackage .cxx_destruct]
+ -[ISIconPackage icons]
+ -[ISIconPackage initWithTypeIdentifier:]
+ -[ISIconPackage initWithTypeIdentifier:configuration:]
+ -[ISIconPackage initWithTypeIdentifier:configuration:].cold.1
+ -[ISIconPackage setIcons:]
+ -[ISIconSegmentation _computeImageWithCGImage:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:]
+ -[ISIconSegmentation _computeImageWithWidth:height:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:]
+ -[ISIconSegmentation _computeImageWithWidth:height:strict:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:]
+ -[ISIconSegmentation createDarkImageWithCGImage:feedback:]
+ -[ISIconSegmentation createForegroundImageWithCGImage:feedback:]
+ -[ISIconSegmentation createSolariumTintableImageWithCGImage:feedback:]
+ -[ISIconSegmentation createTintableImageMaskWithCGImage:tintableOpacityImageMask:]
+ -[ISIconSegmentation grayscaleConversion]
+ -[ISIconSegmentation initWithIdiom:]
+ -[ISIconSegmentationFeedback .cxx_destruct]
+ -[ISIconSegmentationFeedback background]
+ -[ISIconSegmentationFeedback foreground]
+ -[ISIconSegmentationFeedback initWithForeground:background:recolorForeground:]
+ -[ISIconSegmentationFeedback recolorForeground]
+ -[ISIconSegmentationFeedbackBilinearGradient dealloc]
+ -[ISIconSegmentationFeedbackBilinearGradient gradientWithSize:]
+ -[ISIconSegmentationFeedbackBilinearGradient initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:]
+ -[ISIconSegmentationFeedbackMultipleColors initWithNumberOfColors:]
+ -[ISIconSegmentationFeedbackMultipleColors numberOfColors]
+ -[ISIconSegmentationFeedbackSingleColor color]
+ -[ISIconSegmentationFeedbackSingleColor dealloc]
+ -[ISIconSegmentationFeedbackSingleColor initWithColor:]
+ -[ISIconStackAssetCatalogResource iconStackForSize:scale:]
+ -[ISIconStackAssetCatalogResource imageForSize:scale:]
+ -[ISIconStackAssetCatalogResource setUsesExternalCompositor:]
+ -[ISIconStackAssetCatalogResource usesExternalCompositor]
+ -[ISIconStackComposer assetAppearance]
+ -[ISIconStackComposer asset]
+ -[ISIconStackComposer dealloc]
+ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:]
+ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:].cold.1
+ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:].cold.2
+ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:].cold.3
+ -[ISIconStackComposer imageForCompositingDescriptor:]
+ -[ISIconStackComposer imageForCompositingDescriptor:].cold.1
+ -[ISIconStackComposer initWithLegacyAsset:assetAppearance:platform:]
+ -[ISIconStackComposer platform]
+ -[ISIconStackComposer segmentationIdiom]
+ -[ISIconStackComposer segmentationIdiom].cold.1
+ -[ISIconStackCompositeResource .cxx_destruct]
+ -[ISIconStackCompositeResource assetAppearance]
+ -[ISIconStackCompositeResource compositingDescriptor]
+ -[ISIconStackCompositeResource iconStackForSize:scale:]
+ -[ISIconStackCompositeResource imageForSize:scale:]
+ -[ISIconStackCompositeResource initWithResource:]
+ -[ISIconStackCompositeResource platform]
+ -[ISIconStackCompositeResource setCompositingDescriptor:]
+ -[ISIconStackCompositeResource wrappedResource]
+ -[ISImageDescriptor digest:size:]
+ -[ISImageDescriptor platform]
+ -[ISLayeredIcon .cxx_destruct]
+ -[ISLayeredIcon _IS_cuiShadowStyleFromStyle:]
+ -[ISLayeredIcon _IS_cuiShadowStyleFromStyle:].cold.1
+ -[ISLayeredIcon _generateImageWithDescriptor:]
+ -[ISLayeredIcon _generateImageWithDescriptor:].cold.1
+ -[ISLayeredIcon _init]
+ -[ISLayeredIcon _prepareImagesForImageDescriptors:]
+ -[ISLayeredIcon _tweakCopiedImageDescriptorsIfNecessary:]
+ -[ISLayeredIcon baseStackForDescriptor:]
+ -[ISLayeredIcon baseStackForDescriptor:].cold.1
+ -[ISLayeredIcon bundleIdentifier]
+ -[ISLayeredIcon bundlePlatform]
+ -[ISLayeredIcon getImageForImageDescriptor:completion:]
+ -[ISLayeredIcon iconLayers]
+ -[ISLayeredIcon iconStackForDescriptor:]
+ -[ISLayeredIcon imageCache]
+ -[ISLayeredIcon imageForImageDescriptor:]
+ -[ISLayeredIcon imageLayers]
+ -[ISLayeredIcon initWithBundleIdentifier:imageLayers:]
+ -[ISLayeredIcon initWithTypeIdentifier:iconLayers:]
+ -[ISLayeredIcon initWithTypeIdentifier:layerGroups:]
+ -[ISLayeredIcon layerGroups]
+ -[ISLayeredIcon setBundlePlatform:]
+ -[ISLayeredIcon setImageCache:]
+ -[ISLayeredIcon setLayerGroups:]
+ -[ISLayeredIcon typeIdentifier]
+ -[ISLuminanceGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:samples:]
+ -[ISMaskEffect filterWithBackgroundImage:inputImage:]
+ -[ISMonochromeTintEffect .cxx_destruct]
+ -[ISMonochromeTintEffect color]
+ -[ISMonochromeTintEffect filterWithBackgroundImage:inputImage:]
+ -[ISMonochromeTintEffect initWithColor:]
+ -[ISMonochromeTintEffect setColor:]
+ -[ISMultisizedAssetCatalogResource _iconStackComposerForNamedImage:]
+ -[ISMultisizedAssetCatalogResource _imageForMultisizeImage:size:scale:]
+ -[ISMultisizedAssetCatalogResource _lookupForSize:scale:]
+ -[ISMultisizedAssetCatalogResource extrapolateIconStack]
+ -[ISMultisizedAssetCatalogResource iconStackForSize:scale:]
+ -[ISMultisizedAssetCatalogResource imageForSize:scale:]
+ -[ISMultisizedAssetCatalogResource setExtrapolateIconStack:]
+ -[ISMultisizedAssetCatalogResource setUsesExternalCompositor:]
+ -[ISMultisizedAssetCatalogResource usesExternalCompositor]
+ -[ISPlatformInfo _platform:withinAllowedPlatforms:allowNative:]
+ -[ISPlatformInfo supportsRequestingIconStacksForPlatform:]
+ -[ISRecordResourceProvider _determineRecipe]
+ -[ISRecordResourceProvider _findTextResourceWithIconDictionary:]
+ -[ISRecordResourceProvider _isAppLike]
+ -[ISRecordResourceProvider _isApp]
+ -[ISRecordResourceProvider assignLayerResources]
+ -[ISRecordResourceProvider externalCompositingResource]
+ -[ISRecordResourceProvider iconStackResourcesAllowed]
+ -[ISRecordResourceProvider layeredIconResource]
+ -[ISRecordResourceProvider setLayeredIconResource:]
+ -[ISRecordResourceProvider shouldUseFolderRecipe:]
+ -[ISRecordResourceProvider treatLikeSymbol]
+ -[ISResourceProvider backgroundResource]
+ -[ISResourceProvider externalCompositingResource]
+ -[ISResourceProvider iconConfig]
+ -[ISResourceProvider setBackgroundResource:]
+ -[ISResourceProvider setIconConfig:]
+ -[ISResourceProvider setTextResource:]
+ -[ISResourceProvider textResource]
+ -[ISResourceProvider treatLikeSymbol]
+ -[ISResourceProvider(Convenience) isBadgedWithSymbol]
+ -[ISResourceProvider(Convenience) isCompositedDocument]
+ -[ISResourceProvider(Convenience) treatLikeSymbol]
+ -[ISShapeDetection detectShapeInCGImage:bounds:cornerRadius:]
+ -[ISShapeDetection detectShapeInImageWithWidth:height:samples:bounds:cornerRadius:]
+ -[ISSpecularClassification _prepareMaskIfNeeded]
+ -[ISSpecularClassification classifySpecularWithDebug:]
+ -[ISSpecularClassification classifySpecular]
+ -[ISSpecularClassification createSpecularImage]
+ -[ISSpecularClassification dealloc]
+ -[ISSpecularClassification initWithSpecularImage:useAlphaOnly:]
+ -[ISStaticIconStackAssetCatalogResource .cxx_destruct]
+ -[ISStaticIconStackAssetCatalogResource assetsURLs]
+ -[ISStaticIconStackAssetCatalogResource chicletHighlightColour]
+ -[ISStaticIconStackAssetCatalogResource compositingDescriptor]
+ -[ISStaticIconStackAssetCatalogResource iconStack]
+ -[ISStaticIconStackAssetCatalogResource imageForSize:scale:]
+ -[ISStaticIconStackAssetCatalogResource initWithBundleID:]
+ -[ISStaticIconStackAssetCatalogResource layerCount]
+ -[ISStaticIconStackAssetCatalogResource name]
+ -[ISStaticIconStackAssetCatalogResource platformCatalog]
+ -[ISStaticIconStackAssetCatalogResource primaryColour]
+ -[ISStaticIconStackAssetCatalogResource scale]
+ -[ISStaticIconStackAssetCatalogResource secondaryColour]
+ -[ISStaticIconStackAssetCatalogResource setChicletHighlightColour:]
+ -[ISStaticIconStackAssetCatalogResource setCompositingDescriptor:]
+ -[ISStaticIconStackAssetCatalogResource setIconStack:]
+ -[ISStaticIconStackAssetCatalogResource setLayerCount:]
+ -[ISStaticIconStackAssetCatalogResource setName:]
+ -[ISStaticIconStackAssetCatalogResource setPlatformCatalog:]
+ -[ISStaticIconStackAssetCatalogResource setPrimaryColour:]
+ -[ISStaticIconStackAssetCatalogResource setScale:]
+ -[ISStaticIconStackAssetCatalogResource setSecondaryColour:]
+ -[ISStaticIconStackAssetCatalogResource setUsesExternalCompositor:]
+ -[ISStaticIconStackAssetCatalogResource usesExternalCompositor]
+ -[ISStaticResources cacheMissIconResourceForPlatform:]
+ -[ISStaticResources cacheMissIconResourceForPlatform:].cold.1
+ -[ISStaticResources cacheMissIconResource]
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.3
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.4
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.5
+ -[ISSymbolEffect filterWithBackgroundImage:inputImage:]
+ -[ISTypeIcon iconConfig]
+ -[ISTypeIcon initWithType:iconConfiguration:]
+ -[NSDictionary(LayeredIconAdditions) _IS_layerObjectForKey:]
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CGBitmapContextCreate
+ _CGBitmapContextCreateImage
+ _CGColorCreate
+ _CGColorGetComponents
+ _CGColorGetConstantColor
+ _CGColorGetNumberOfComponents
+ _CGColorRelease
+ _CGColorRetain
+ _CGColorSpaceGetModel
+ _CGContextClip
+ _CGContextDrawImage
+ _CGContextRelease
+ _CGImageCreateWithImageInRect
+ _CGImageGetBytesPerRow
+ _CGImageGetColorSpace
+ _CGImageIsMask
+ _CGPathCreateWithContinuousRoundedRect
+ _ISAccelerateIconSegmentationComputeFlagForExtraConfidence
+ _ISCatalogAssetAppearanceForAssetAppearance
+ _ISCreateAlphaPremultipliedCGImageSegmentationMask
+ _ISCreateCGImageSegmentationSamples
+ _ISCreateCroppedCGImage
+ _ISCreateScaledCGImage
+ _ISSegmentationMask_readMaskValue_i
+ _ISSegmentationMask_readMaskValue_xy
+ _ISSegmentationMask_writeMaskValue_i
+ _ISSegmentationMask_writeMaskValue_xy
+ _ISSegmentationMathUtils_rand_closed
+ _ISSegmentationMathUtils_rand_open
+ _ISSegmentationSamples_readAlmostOpaqueSample_i
+ _ISSegmentationSamples_readAlmostOpaqueSample_xy
+ _ISSegmentationSamples_readOpaqueSample_i
+ _ISSegmentationSamples_readOpaqueSample_xy
+ _ISSegmentationSamples_readOpaqueUcharSample_i
+ _ISSegmentationSamples_readOpaqueUcharSample_xy
+ _ISSegmentationSamples_readSample_i
+ _ISSegmentationSamples_readSample_xy
+ _ISSegmentationSamples_readUcharSampleOpacity_i
+ _ISSegmentationSamples_readUcharSampleOpacity_xy
+ _ISSegmentationSamples_writeSample_i
+ _ISSegmentationSamples_writeSample_xy
+ _NSStringFromISIconTreatment
+ _OBJC_CLASS_$_CUIDesignLibrary
+ _OBJC_CLASS_$_CUIMutableNamedColor
+ _OBJC_CLASS_$_CUIMutableNamedGradient
+ _OBJC_CLASS_$_CUIMutableNamedIconLayerGroup
+ _OBJC_CLASS_$_CUIMutableNamedIconLayerStack
+ _OBJC_CLASS_$_CUIMutableNamedLayerImage
+ _OBJC_CLASS_$_CUIMutableNamedLayerVectorSVGImage
+ _OBJC_CLASS_$_CUINamedIconLayerStack
+ _OBJC_CLASS_$_CUINamedLookup
+ _OBJC_CLASS_$_CUINamedMultisizeImage
+ _OBJC_CLASS_$_ICRFinalizedIcon
+ _OBJC_CLASS_$_ICRGlobalConfiguration
+ _OBJC_CLASS_$_ICRIconLayer
+ _OBJC_CLASS_$_ICRRenderingMode
+ _OBJC_CLASS_$_ISCompositingDescriptor
+ _OBJC_CLASS_$_ISDocumentRecipe
+ _OBJC_CLASS_$_ISFallbackIconDarkSegmented
+ _OBJC_CLASS_$_ISFallbackIconFactory
+ _OBJC_CLASS_$_ISFallbackIconFill
+ _OBJC_CLASS_$_ISFallbackIconScaleDown
+ _OBJC_CLASS_$_ISFallbackIconTintedSegmented
+ _OBJC_CLASS_$_ISFlattenLayerStackAssetCatalogResource
+ _OBJC_CLASS_$_ISFolderIconConfiguration
+ _OBJC_CLASS_$_ISFolderIconConfigurationParser
+ _OBJC_CLASS_$_ISFolderRecipe
+ _OBJC_CLASS_$_ISGenerationReport
+ _OBJC_CLASS_$_ISGraphicIconConfigurationParser
+ _OBJC_CLASS_$_ISICRIconLayerWrapper
+ _OBJC_CLASS_$_ISIconConfigurationMarkupParser
+ _OBJC_CLASS_$_ISIconLayerElement
+ _OBJC_CLASS_$_ISIconLayerGroup
+ _OBJC_CLASS_$_ISIconPackage
+ _OBJC_CLASS_$_ISIconSegmentationFeedback
+ _OBJC_CLASS_$_ISIconSegmentationFeedbackBilinearGradient
+ _OBJC_CLASS_$_ISIconSegmentationFeedbackComplex
+ _OBJC_CLASS_$_ISIconSegmentationFeedbackMultipleColors
+ _OBJC_CLASS_$_ISIconSegmentationFeedbackSingleColor
+ _OBJC_CLASS_$_ISIconStackAssetCatalogResource
+ _OBJC_CLASS_$_ISIconStackComposer
+ _OBJC_CLASS_$_ISIconStackCompositeResource
+ _OBJC_CLASS_$_ISLayeredIcon
+ _OBJC_CLASS_$_ISMaskEffect
+ _OBJC_CLASS_$_ISMonochromeTintEffect
+ _OBJC_CLASS_$_ISMultisizedAssetCatalogResource
+ _OBJC_CLASS_$_ISShapeDetection
+ _OBJC_CLASS_$_ISSpecularClassification
+ _OBJC_CLASS_$_ISStaticIconStackAssetCatalogResource
+ _OBJC_CLASS_$_ISSymbolEffect
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$__ISWrapper_CUINamedIconLayerStack
+ _OBJC_IVAR_$_ISAssetCatalogResource._appearanceVariant
+ _OBJC_IVAR_$_ISAssetCatalogResource._background
+ _OBJC_IVAR_$_ISAssetCatalogResource._shouldApplyMask
+ _OBJC_IVAR_$_ISAssetCatalogResource._suggestedRecipe
+ _OBJC_IVAR_$_ISAssetCatalogResource._tintColor
+ _OBJC_IVAR_$_ISBiasedGrayscaleConversion._energyRatio
+ _OBJC_IVAR_$_ISBiasedGrayscaleConversion._saturation
+ _OBJC_IVAR_$_ISCompositingDescriptor._appearance
+ _OBJC_IVAR_$_ISCompositingDescriptor._appearanceVariant
+ _OBJC_IVAR_$_ISCompositingDescriptor._background
+ _OBJC_IVAR_$_ISCompositingDescriptor._platform
+ _OBJC_IVAR_$_ISCompositingDescriptor._platformStyle
+ _OBJC_IVAR_$_ISCompositingDescriptor._scale
+ _OBJC_IVAR_$_ISCompositingDescriptor._serializeLayerObjectForCaching
+ _OBJC_IVAR_$_ISCompositingDescriptor._shouldApplyMask
+ _OBJC_IVAR_$_ISCompositingDescriptor._size
+ _OBJC_IVAR_$_ISCompositingDescriptor._tintColor
+ _OBJC_IVAR_$_ISCompositingDescriptor._useLegacyCompatibilityMode
+ _OBJC_IVAR_$_ISDefaults._metalCacheURL
+ _OBJC_IVAR_$_ISDimmingConversion._samples
+ _OBJC_IVAR_$_ISDocumentRecipe._badgeWithSymbol
+ _OBJC_IVAR_$_ISDocumentRecipe._hasBespokeBackground
+ _OBJC_IVAR_$_ISDocumentRecipe._hasText
+ _OBJC_IVAR_$_ISDocumentRecipe._maskBadgeResource
+ _OBJC_IVAR_$_ISDocumentRecipe._platform
+ _OBJC_IVAR_$_ISDocumentRecipe._treatLikeSymbol
+ _OBJC_IVAR_$_ISFallbackIconDarkSegmented._darkImage
+ _OBJC_IVAR_$_ISFallbackIconDarkSegmented._drawsLightingEffects
+ _OBJC_IVAR_$_ISFallbackIconDarkSegmented._feedback
+ _OBJC_IVAR_$_ISFallbackIconFactory._cgImage
+ _OBJC_IVAR_$_ISFallbackIconFactory._idiom
+ _OBJC_IVAR_$_ISFallbackIconFill._feedback
+ _OBJC_IVAR_$_ISFallbackIconFill._foregroundAndLightingEffectsImage
+ _OBJC_IVAR_$_ISFallbackIconFill._image
+ _OBJC_IVAR_$_ISFallbackIconScaleDown._cornerRadius
+ _OBJC_IVAR_$_ISFallbackIconScaleDown._image
+ _OBJC_IVAR_$_ISFallbackIconTintedSegmented._drawsLightingEffects
+ _OBJC_IVAR_$_ISFallbackIconTintedSegmented._feedback
+ _OBJC_IVAR_$_ISFallbackIconTintedSegmented._tintableImage
+ _OBJC_IVAR_$_ISFolderIconConfiguration._emoji
+ _OBJC_IVAR_$_ISFolderIconConfiguration._folderEmpty
+ _OBJC_IVAR_$_ISFolderIconConfiguration._symbolName
+ _OBJC_IVAR_$_ISFolderIconConfiguration._systemTintColor
+ _OBJC_IVAR_$_ISFolderIconConfiguration._tintColor
+ _OBJC_IVAR_$_ISFolderRecipe._disableShadow
+ _OBJC_IVAR_$_ISFolderRecipe._tintColor
+ _OBJC_IVAR_$_ISGenerationReport._hasLightingEffects
+ _OBJC_IVAR_$_ISGenerationReport._iconTreatment
+ _OBJC_IVAR_$_ISGenerationResponse._sharedMemory
+ _OBJC_IVAR_$_ISIconConfigurationMarkupParser._configDict
+ _OBJC_IVAR_$_ISIconLayer._hasLightEffects
+ _OBJC_IVAR_$_ISIconLayer._imageBag
+ _OBJC_IVAR_$_ISIconLayer._images
+ _OBJC_IVAR_$_ISIconLayerElement._effects
+ _OBJC_IVAR_$_ISIconLayerElement._fillColors
+ _OBJC_IVAR_$_ISIconLayerElement._fills
+ _OBJC_IVAR_$_ISIconLayerElement._imageBag
+ _OBJC_IVAR_$_ISIconLayerElement._images
+ _OBJC_IVAR_$_ISIconLayerElement._opacities
+ _OBJC_IVAR_$_ISIconLayerGroup._blurs
+ _OBJC_IVAR_$_ISIconLayerGroup._combineSpeculars
+ _OBJC_IVAR_$_ISIconLayerGroup._layers
+ _OBJC_IVAR_$_ISIconLayerGroup._opacities
+ _OBJC_IVAR_$_ISIconLayerGroup._shadowStyles
+ _OBJC_IVAR_$_ISIconLayerGroup._shadows
+ _OBJC_IVAR_$_ISIconLayerGroup._speculars
+ _OBJC_IVAR_$_ISIconLayerGroup._translucencies
+ _OBJC_IVAR_$_ISIconPackage._icons
+ _OBJC_IVAR_$_ISIconSegmentation._idiom
+ _OBJC_IVAR_$_ISIconSegmentationFeedback._background
+ _OBJC_IVAR_$_ISIconSegmentationFeedback._foreground
+ _OBJC_IVAR_$_ISIconSegmentationFeedback._recolorForeground
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackBilinearGradient._bottomLeftColor
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackBilinearGradient._bottomRightColor
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackBilinearGradient._topLeftColor
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackBilinearGradient._topRightColor
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackMultipleColors._numberOfColors
+ _OBJC_IVAR_$_ISIconSegmentationFeedbackSingleColor._color
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._usesExternalCompositor
+ _OBJC_IVAR_$_ISIconStackComposer._asset
+ _OBJC_IVAR_$_ISIconStackComposer._assetAppearance
+ _OBJC_IVAR_$_ISIconStackComposer._platform
+ _OBJC_IVAR_$_ISIconStackCompositeResource._compositingDescriptor
+ _OBJC_IVAR_$_ISIconStackCompositeResource._platform
+ _OBJC_IVAR_$_ISIconStackCompositeResource._wrappedResource
+ _OBJC_IVAR_$_ISLayeredIcon._bundleIdentifier
+ _OBJC_IVAR_$_ISLayeredIcon._bundlePlatform
+ _OBJC_IVAR_$_ISLayeredIcon._iconLayers
+ _OBJC_IVAR_$_ISLayeredIcon._imageCache
+ _OBJC_IVAR_$_ISLayeredIcon._imageLayers
+ _OBJC_IVAR_$_ISLayeredIcon._layerGroups
+ _OBJC_IVAR_$_ISLayeredIcon._typeIdentifier
+ _OBJC_IVAR_$_ISMonochromeTintEffect._color
+ _OBJC_IVAR_$_ISMultisizedAssetCatalogResource._extrapolateIconStack
+ _OBJC_IVAR_$_ISMultisizedAssetCatalogResource._usesExternalCompositor
+ _OBJC_IVAR_$_ISRecordResourceProvider._layeredIconResource
+ _OBJC_IVAR_$_ISResourceProvider._externalCompositingResource
+ _OBJC_IVAR_$_ISResourceProvider._iconConfig
+ _OBJC_IVAR_$_ISResourceProvider._treatLikeSymbol
+ _OBJC_IVAR_$_ISSpecularClassification._cgImage
+ _OBJC_IVAR_$_ISSpecularClassification._data
+ _OBJC_IVAR_$_ISSpecularClassification._mask
+ _OBJC_IVAR_$_ISSpecularClassification._ucharMask
+ _OBJC_IVAR_$_ISSpecularClassification._useAlphaOnly
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._chicletHighlightColour
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._compositingDescriptor
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._iconStack
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._layerCount
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._name
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._platformCatalog
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._primaryColour
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._scale
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._secondaryColour
+ _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._usesExternalCompositor
+ _OBJC_IVAR_$_ISTypeIcon._iconConfig
+ _OBJC_METACLASS_$_ISCompositingDescriptor
+ _OBJC_METACLASS_$_ISDocumentRecipe
+ _OBJC_METACLASS_$_ISFallbackIconDarkSegmented
+ _OBJC_METACLASS_$_ISFallbackIconFactory
+ _OBJC_METACLASS_$_ISFallbackIconFill
+ _OBJC_METACLASS_$_ISFallbackIconScaleDown
+ _OBJC_METACLASS_$_ISFallbackIconTintedSegmented
+ _OBJC_METACLASS_$_ISFlattenLayerStackAssetCatalogResource
+ _OBJC_METACLASS_$_ISFolderIconConfiguration
+ _OBJC_METACLASS_$_ISFolderIconConfigurationParser
+ _OBJC_METACLASS_$_ISFolderRecipe
+ _OBJC_METACLASS_$_ISGenerationReport
+ _OBJC_METACLASS_$_ISGraphicIconConfigurationParser
+ _OBJC_METACLASS_$_ISICRIconLayerWrapper
+ _OBJC_METACLASS_$_ISIconConfigurationMarkupParser
+ _OBJC_METACLASS_$_ISIconLayerElement
+ _OBJC_METACLASS_$_ISIconLayerGroup
+ _OBJC_METACLASS_$_ISIconPackage
+ _OBJC_METACLASS_$_ISIconSegmentationFeedback
+ _OBJC_METACLASS_$_ISIconSegmentationFeedbackBilinearGradient
+ _OBJC_METACLASS_$_ISIconSegmentationFeedbackComplex
+ _OBJC_METACLASS_$_ISIconSegmentationFeedbackMultipleColors
+ _OBJC_METACLASS_$_ISIconSegmentationFeedbackSingleColor
+ _OBJC_METACLASS_$_ISIconStackAssetCatalogResource
+ _OBJC_METACLASS_$_ISIconStackComposer
+ _OBJC_METACLASS_$_ISIconStackCompositeResource
+ _OBJC_METACLASS_$_ISLayeredIcon
+ _OBJC_METACLASS_$_ISMaskEffect
+ _OBJC_METACLASS_$_ISMonochromeTintEffect
+ _OBJC_METACLASS_$_ISMultisizedAssetCatalogResource
+ _OBJC_METACLASS_$_ISShapeDetection
+ _OBJC_METACLASS_$_ISSpecularClassification
+ _OBJC_METACLASS_$_ISStaticIconStackAssetCatalogResource
+ _OBJC_METACLASS_$_ISSymbolEffect
+ _OBJC_METACLASS_$__ISWrapper_CUINamedIconLayerStack
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UTTypeApplication
+ _UTTypeFolder
+ __DATA_ISICRIconLayerWrapper
+ __DATA__ISWrapper_CUINamedIconLayerStack
+ __INSTANCE_METHODS_ISICRIconLayerWrapper
+ __INSTANCE_METHODS__ISWrapper_CUINamedIconLayerStack
+ __ISImageGenerationReportKey
+ __IS_colorStringFromColor
+ __IS_colorStringFromIFColor
+ __IS_colorStringFromSystemColor
+ __IVARS_ISICRIconLayerWrapper
+ __IVARS__ISWrapper_CUINamedIconLayerStack
+ __METACLASS_DATA_ISICRIconLayerWrapper
+ __METACLASS_DATA__ISWrapper_CUINamedIconLayerStack
+ __OBJC_$_CATEGORY_CLASS_METHODS_IFColor_$_FolderAdditions
+ __OBJC_$_CATEGORY_CUINamedIconLayerStack_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_CUINamedLookup_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_CUINamedMultisizeImage_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_ICRFinalizedIcon_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_IFColor_$_FolderAdditions
+ __OBJC_$_CATEGORY_IFImage_$_GenerationReport
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CUINamedIconLayerStack_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CUINamedLookup_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CUINamedMultisizeImage_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ICRFinalizedIcon_$_IconServicesAdditions
+ __OBJC_$_CLASS_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
+ __OBJC_$_CLASS_METHODS_ISCompositingDescriptor
+ __OBJC_$_CLASS_METHODS_ISFolderIconConfiguration
+ __OBJC_$_CLASS_METHODS_ISGenerationReport
+ __OBJC_$_CLASS_METHODS_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|LIIconVariant|TemplateHack)
+ __OBJC_$_CLASS_METHODS_ISShapeDetection
+ __OBJC_$_CLASS_METHODS_ISStaticIconStackAssetCatalogResource
+ __OBJC_$_CLASS_PROP_LIST_ISFolderIconConfiguration
+ __OBJC_$_INSTANCE_METHODS_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
+ __OBJC_$_INSTANCE_METHODS_ISAssetCatalogResource
+ __OBJC_$_INSTANCE_METHODS_ISCompositingDescriptor
+ __OBJC_$_INSTANCE_METHODS_ISDocumentRecipe
+ __OBJC_$_INSTANCE_METHODS_ISFallbackIconDarkSegmented
+ __OBJC_$_INSTANCE_METHODS_ISFallbackIconFactory
+ __OBJC_$_INSTANCE_METHODS_ISFallbackIconFill
+ __OBJC_$_INSTANCE_METHODS_ISFallbackIconScaleDown
+ __OBJC_$_INSTANCE_METHODS_ISFallbackIconTintedSegmented
+ __OBJC_$_INSTANCE_METHODS_ISFlattenLayerStackAssetCatalogResource
+ __OBJC_$_INSTANCE_METHODS_ISFolderIconConfiguration
+ __OBJC_$_INSTANCE_METHODS_ISFolderIconConfigurationParser
+ __OBJC_$_INSTANCE_METHODS_ISFolderRecipe
+ __OBJC_$_INSTANCE_METHODS_ISGenerationReport
+ __OBJC_$_INSTANCE_METHODS_ISGraphicIconConfigurationParser
+ __OBJC_$_INSTANCE_METHODS_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|LIIconVariant|TemplateHack)
+ __OBJC_$_INSTANCE_METHODS_ISIconConfigurationMarkupParser
+ __OBJC_$_INSTANCE_METHODS_ISIconLayerElement
+ __OBJC_$_INSTANCE_METHODS_ISIconLayerGroup
+ __OBJC_$_INSTANCE_METHODS_ISIconPackage
+ __OBJC_$_INSTANCE_METHODS_ISIconSegmentationFeedback
+ __OBJC_$_INSTANCE_METHODS_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_$_INSTANCE_METHODS_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_$_INSTANCE_METHODS_ISIconSegmentationFeedbackSingleColor
+ __OBJC_$_INSTANCE_METHODS_ISIconStackAssetCatalogResource
+ __OBJC_$_INSTANCE_METHODS_ISIconStackComposer
+ __OBJC_$_INSTANCE_METHODS_ISIconStackCompositeResource
+ __OBJC_$_INSTANCE_METHODS_ISLayeredIcon
+ __OBJC_$_INSTANCE_METHODS_ISMaskEffect
+ __OBJC_$_INSTANCE_METHODS_ISMonochromeTintEffect
+ __OBJC_$_INSTANCE_METHODS_ISMultisizedAssetCatalogResource
+ __OBJC_$_INSTANCE_METHODS_ISShapeDetection
+ __OBJC_$_INSTANCE_METHODS_ISSpecularClassification
+ __OBJC_$_INSTANCE_METHODS_ISStaticIconStackAssetCatalogResource
+ __OBJC_$_INSTANCE_METHODS_ISSymbolEffect
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(ISCompositorResourceProvider|LayeredIconAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_ISBiasedGrayscaleConversion
+ __OBJC_$_INSTANCE_VARIABLES_ISCompositingDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_ISDocumentRecipe
+ __OBJC_$_INSTANCE_VARIABLES_ISFallbackIconDarkSegmented
+ __OBJC_$_INSTANCE_VARIABLES_ISFallbackIconFactory
+ __OBJC_$_INSTANCE_VARIABLES_ISFallbackIconFill
+ __OBJC_$_INSTANCE_VARIABLES_ISFallbackIconScaleDown
+ __OBJC_$_INSTANCE_VARIABLES_ISFallbackIconTintedSegmented
+ __OBJC_$_INSTANCE_VARIABLES_ISFolderIconConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ISFolderRecipe
+ __OBJC_$_INSTANCE_VARIABLES_ISGenerationReport
+ __OBJC_$_INSTANCE_VARIABLES_ISIconConfigurationMarkupParser
+ __OBJC_$_INSTANCE_VARIABLES_ISIconLayerElement
+ __OBJC_$_INSTANCE_VARIABLES_ISIconLayerGroup
+ __OBJC_$_INSTANCE_VARIABLES_ISIconPackage
+ __OBJC_$_INSTANCE_VARIABLES_ISIconSegmentationFeedback
+ __OBJC_$_INSTANCE_VARIABLES_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_$_INSTANCE_VARIABLES_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_$_INSTANCE_VARIABLES_ISIconSegmentationFeedbackSingleColor
+ __OBJC_$_INSTANCE_VARIABLES_ISIconStackAssetCatalogResource
+ __OBJC_$_INSTANCE_VARIABLES_ISIconStackComposer
+ __OBJC_$_INSTANCE_VARIABLES_ISIconStackCompositeResource
+ __OBJC_$_INSTANCE_VARIABLES_ISLayeredIcon
+ __OBJC_$_INSTANCE_VARIABLES_ISMonochromeTintEffect
+ __OBJC_$_INSTANCE_VARIABLES_ISMultisizedAssetCatalogResource
+ __OBJC_$_INSTANCE_VARIABLES_ISSpecularClassification
+ __OBJC_$_INSTANCE_VARIABLES_ISStaticIconStackAssetCatalogResource
+ __OBJC_$_PROP_LIST_CUINamedLookup_$_IconServicesAdditions
+ __OBJC_$_PROP_LIST_ISBiasedGrayscaleConversion
+ __OBJC_$_PROP_LIST_ISCompositingDescriptor
+ __OBJC_$_PROP_LIST_ISDocumentRecipe
+ __OBJC_$_PROP_LIST_ISFallbackIconDarkSegmented
+ __OBJC_$_PROP_LIST_ISFallbackIconFill
+ __OBJC_$_PROP_LIST_ISFallbackIconScaleDown
+ __OBJC_$_PROP_LIST_ISFallbackIconTintedSegmented
+ __OBJC_$_PROP_LIST_ISFolderIconConfiguration
+ __OBJC_$_PROP_LIST_ISFolderIconConfigurationParser
+ __OBJC_$_PROP_LIST_ISFolderRecipe
+ __OBJC_$_PROP_LIST_ISGenerationReport
+ __OBJC_$_PROP_LIST_ISGraphicIconConfigurationParser
+ __OBJC_$_PROP_LIST_ISIconConfiguration
+ __OBJC_$_PROP_LIST_ISIconConfigurationMarkupParser
+ __OBJC_$_PROP_LIST_ISIconLayerElement
+ __OBJC_$_PROP_LIST_ISIconLayerGroup
+ __OBJC_$_PROP_LIST_ISIconPackage
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedback
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedbackComplex
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_$_PROP_LIST_ISIconSegmentationFeedbackSingleColor
+ __OBJC_$_PROP_LIST_ISIconStackAssetCatalogResource
+ __OBJC_$_PROP_LIST_ISIconStackComposer
+ __OBJC_$_PROP_LIST_ISIconStackCompositeResource
+ __OBJC_$_PROP_LIST_ISIconStackResource
+ __OBJC_$_PROP_LIST_ISLayeredIcon
+ __OBJC_$_PROP_LIST_ISMaskEffect
+ __OBJC_$_PROP_LIST_ISMonochromeTintEffect
+ __OBJC_$_PROP_LIST_ISMultisizedAssetCatalogResource
+ __OBJC_$_PROP_LIST_ISScalableCompositorResource
+ __OBJC_$_PROP_LIST_ISStaticIconStackAssetCatalogResource
+ __OBJC_$_PROP_LIST_ISSymbolEffect
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISIconConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISIconStackResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ISScalableCompositorResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ISIconConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ISIconStackResource
+ __OBJC_$_PROTOCOL_REFS_ISDarkFallbackIcon
+ __OBJC_$_PROTOCOL_REFS_ISFallbackIcon
+ __OBJC_$_PROTOCOL_REFS_ISIconConfiguration
+ __OBJC_$_PROTOCOL_REFS_ISIconSegmentationFeedbackBackground
+ __OBJC_$_PROTOCOL_REFS_ISIconSegmentationFeedbackForeground
+ __OBJC_$_PROTOCOL_REFS_ISIconSegmentationFeedbackRecolor
+ __OBJC_$_PROTOCOL_REFS_ISLightFallbackIcon
+ __OBJC_$_PROTOCOL_REFS_ISTintedFallbackIcon
+ __OBJC_CLASS_PROTOCOLS_$_IFImage(GenerationReport|ISScalableCompositorResource|Internal|ISPlaceholderImage)
+ __OBJC_CLASS_PROTOCOLS_$_ISCompositingDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_ISDocumentRecipe
+ __OBJC_CLASS_PROTOCOLS_$_ISFallbackIconDarkSegmented
+ __OBJC_CLASS_PROTOCOLS_$_ISFallbackIconFill
+ __OBJC_CLASS_PROTOCOLS_$_ISFallbackIconScaleDown
+ __OBJC_CLASS_PROTOCOLS_$_ISFallbackIconTintedSegmented
+ __OBJC_CLASS_PROTOCOLS_$_ISFolderIconConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_ISFolderRecipe
+ __OBJC_CLASS_PROTOCOLS_$_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|LIIconVariant|TemplateHack)
+ __OBJC_CLASS_PROTOCOLS_$_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_CLASS_PROTOCOLS_$_ISIconSegmentationFeedbackComplex
+ __OBJC_CLASS_PROTOCOLS_$_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_CLASS_PROTOCOLS_$_ISIconSegmentationFeedbackSingleColor
+ __OBJC_CLASS_PROTOCOLS_$_ISIconStackAssetCatalogResource
+ __OBJC_CLASS_PROTOCOLS_$_ISIconStackCompositeResource
+ __OBJC_CLASS_PROTOCOLS_$_ISMaskEffect
+ __OBJC_CLASS_PROTOCOLS_$_ISMonochromeTintEffect
+ __OBJC_CLASS_PROTOCOLS_$_ISMultisizedAssetCatalogResource
+ __OBJC_CLASS_PROTOCOLS_$_ISSymbolEffect
+ __OBJC_CLASS_RO_$_ISCompositingDescriptor
+ __OBJC_CLASS_RO_$_ISDocumentRecipe
+ __OBJC_CLASS_RO_$_ISFallbackIconDarkSegmented
+ __OBJC_CLASS_RO_$_ISFallbackIconFactory
+ __OBJC_CLASS_RO_$_ISFallbackIconFill
+ __OBJC_CLASS_RO_$_ISFallbackIconScaleDown
+ __OBJC_CLASS_RO_$_ISFallbackIconTintedSegmented
+ __OBJC_CLASS_RO_$_ISFlattenLayerStackAssetCatalogResource
+ __OBJC_CLASS_RO_$_ISFolderIconConfiguration
+ __OBJC_CLASS_RO_$_ISFolderIconConfigurationParser
+ __OBJC_CLASS_RO_$_ISFolderRecipe
+ __OBJC_CLASS_RO_$_ISGenerationReport
+ __OBJC_CLASS_RO_$_ISGraphicIconConfigurationParser
+ __OBJC_CLASS_RO_$_ISIconConfigurationMarkupParser
+ __OBJC_CLASS_RO_$_ISIconLayerElement
+ __OBJC_CLASS_RO_$_ISIconLayerGroup
+ __OBJC_CLASS_RO_$_ISIconPackage
+ __OBJC_CLASS_RO_$_ISIconSegmentationFeedback
+ __OBJC_CLASS_RO_$_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_CLASS_RO_$_ISIconSegmentationFeedbackComplex
+ __OBJC_CLASS_RO_$_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_CLASS_RO_$_ISIconSegmentationFeedbackSingleColor
+ __OBJC_CLASS_RO_$_ISIconStackAssetCatalogResource
+ __OBJC_CLASS_RO_$_ISIconStackComposer
+ __OBJC_CLASS_RO_$_ISIconStackCompositeResource
+ __OBJC_CLASS_RO_$_ISLayeredIcon
+ __OBJC_CLASS_RO_$_ISMaskEffect
+ __OBJC_CLASS_RO_$_ISMonochromeTintEffect
+ __OBJC_CLASS_RO_$_ISMultisizedAssetCatalogResource
+ __OBJC_CLASS_RO_$_ISShapeDetection
+ __OBJC_CLASS_RO_$_ISSpecularClassification
+ __OBJC_CLASS_RO_$_ISStaticIconStackAssetCatalogResource
+ __OBJC_CLASS_RO_$_ISSymbolEffect
+ __OBJC_LABEL_PROTOCOL_$_ISDarkFallbackIcon
+ __OBJC_LABEL_PROTOCOL_$_ISFallbackIcon
+ __OBJC_LABEL_PROTOCOL_$_ISIconConfiguration
+ __OBJC_LABEL_PROTOCOL_$_ISIconSegmentationFeedbackBackground
+ __OBJC_LABEL_PROTOCOL_$_ISIconSegmentationFeedbackForeground
+ __OBJC_LABEL_PROTOCOL_$_ISIconSegmentationFeedbackRecolor
+ __OBJC_LABEL_PROTOCOL_$_ISIconStackResource
+ __OBJC_LABEL_PROTOCOL_$_ISLightFallbackIcon
+ __OBJC_LABEL_PROTOCOL_$_ISTintedFallbackIcon
+ __OBJC_METACLASS_RO_$_ISCompositingDescriptor
+ __OBJC_METACLASS_RO_$_ISDocumentRecipe
+ __OBJC_METACLASS_RO_$_ISFallbackIconDarkSegmented
+ __OBJC_METACLASS_RO_$_ISFallbackIconFactory
+ __OBJC_METACLASS_RO_$_ISFallbackIconFill
+ __OBJC_METACLASS_RO_$_ISFallbackIconScaleDown
+ __OBJC_METACLASS_RO_$_ISFallbackIconTintedSegmented
+ __OBJC_METACLASS_RO_$_ISFlattenLayerStackAssetCatalogResource
+ __OBJC_METACLASS_RO_$_ISFolderIconConfiguration
+ __OBJC_METACLASS_RO_$_ISFolderIconConfigurationParser
+ __OBJC_METACLASS_RO_$_ISFolderRecipe
+ __OBJC_METACLASS_RO_$_ISGenerationReport
+ __OBJC_METACLASS_RO_$_ISGraphicIconConfigurationParser
+ __OBJC_METACLASS_RO_$_ISIconConfigurationMarkupParser
+ __OBJC_METACLASS_RO_$_ISIconLayerElement
+ __OBJC_METACLASS_RO_$_ISIconLayerGroup
+ __OBJC_METACLASS_RO_$_ISIconPackage
+ __OBJC_METACLASS_RO_$_ISIconSegmentationFeedback
+ __OBJC_METACLASS_RO_$_ISIconSegmentationFeedbackBilinearGradient
+ __OBJC_METACLASS_RO_$_ISIconSegmentationFeedbackComplex
+ __OBJC_METACLASS_RO_$_ISIconSegmentationFeedbackMultipleColors
+ __OBJC_METACLASS_RO_$_ISIconSegmentationFeedbackSingleColor
+ __OBJC_METACLASS_RO_$_ISIconStackAssetCatalogResource
+ __OBJC_METACLASS_RO_$_ISIconStackComposer
+ __OBJC_METACLASS_RO_$_ISIconStackCompositeResource
+ __OBJC_METACLASS_RO_$_ISLayeredIcon
+ __OBJC_METACLASS_RO_$_ISMaskEffect
+ __OBJC_METACLASS_RO_$_ISMonochromeTintEffect
+ __OBJC_METACLASS_RO_$_ISMultisizedAssetCatalogResource
+ __OBJC_METACLASS_RO_$_ISShapeDetection
+ __OBJC_METACLASS_RO_$_ISSpecularClassification
+ __OBJC_METACLASS_RO_$_ISStaticIconStackAssetCatalogResource
+ __OBJC_METACLASS_RO_$_ISSymbolEffect
+ __OBJC_PROTOCOL_$_ISDarkFallbackIcon
+ __OBJC_PROTOCOL_$_ISFallbackIcon
+ __OBJC_PROTOCOL_$_ISIconConfiguration
+ __OBJC_PROTOCOL_$_ISIconSegmentationFeedbackBackground
+ __OBJC_PROTOCOL_$_ISIconSegmentationFeedbackForeground
+ __OBJC_PROTOCOL_$_ISIconSegmentationFeedbackRecolor
+ __OBJC_PROTOCOL_$_ISIconStackResource
+ __OBJC_PROTOCOL_$_ISLightFallbackIcon
+ __OBJC_PROTOCOL_$_ISTintedFallbackIcon
+ __OBJC_PROTOCOL_REFERENCE_$_ISIconStackResource
+ __PROPERTIES__ISWrapper_CUINamedIconLayerStack
+ ___28-[ISGenerationResponse data]_block_invoke
+ ___32-[ISFolderRecipe hintedFontSize]_block_invoke
+ ___33-[ISFolderRecipe hintedBadgeRect]_block_invoke
+ ___34-[ISDocumentRecipe hintedTextRect]_block_invoke
+ ___35-[ISDefaults forceApperanceVariant]_block_invoke
+ ___35-[ISDefaults forceSymbolEmbossment]_block_invoke
+ ___35-[ISDocumentRecipe hintedBadgeRect]_block_invoke
+ ___35-[ISDocumentRecipe hintedPaperRect]_block_invoke
+ ___36-[ISDocumentRecipe hintedShadowBlur]_block_invoke
+ ___38-[ISDocumentRecipe hintedShadowOffset]_block_invoke
+ ___38-[ISDocumentRecipe hintedShadowSpread]_block_invoke
+ ___38-[ISDocumentRecipe hintedTextFontSize]_block_invoke
+ ___38-[ISFolderRecipe hintedImageBadgeRect]_block_invoke
+ ___40-[ISDocumentRecipe hintedSymbolFontSize]_block_invoke
+ ___44-[ISRecordResourceProvider resolveResources]_block_invoke
+ ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.18
+ ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.18.cold.1
+ ___54-[ISIconPackage initWithTypeIdentifier:configuration:]_block_invoke
+ ___54-[ISIconPackage initWithTypeIdentifier:configuration:]_block_invoke.cold.1
+ ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.24
+ ___60+[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap]_block_invoke
+ ___79+[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:platform:error:]_block_invoke
+ ___92-[CUICatalog(IconServicesAdditions) _IS_iconStackWithName:scale:locale:platform:appearance:]_block_invoke
+ ___block_descriptor_32_e12_v24?0^v8Q16l
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e29_v32?0"UTTypeRecord"8q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.19
+ ___block_literal_global.191
+ ___block_literal_global.193
+ ___block_literal_global.195
+ ___block_literal_global.199
+ ___block_literal_global.203
+ ___block_literal_global.207
+ ___block_literal_global.211
+ ___block_literal_global.215
+ ___block_literal_global.219
+ ___block_literal_global.262
+ ___block_literal_global.264
+ ___block_literal_global.30
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.32
+ ___block_literal_global.322
+ ___block_literal_global.326
+ ___block_literal_global.33
+ ___block_literal_global.337
+ ___block_literal_global.341
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.357
+ ___block_literal_global.361
+ ___block_literal_global.365
+ ___block_literal_global.41
+ ___block_literal_global.48
+ ___block_literal_global.59
+ ___block_literal_global.70
+ ___block_literal_global.78
+ ___block_literal_global.89
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __attemptDarkSegmentationWithCroppedCGImage
+ __attemptLightSegmentationWithCroppedCGImage
+ __attemptTintedSegmentationWithCroppedCGImage
+ __outpaintCGImage
+ __outpaintCorner
+ __removeShadow
+ __removeShadowInCGImage
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_IconServices
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_IconServices
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_IconServices
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_IconServices
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_IconServices
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_IconServices
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_IconServices
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_IconServices
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_IconServices
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_IconServices
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_IconServices
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_IconServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_IconServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_IconServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_IconServices
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_IconServices
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_IconServices
+ __swift_stdlib_reportUnimplementedInitializer
+ __xpc_type_shmem
+ _backgroundIsContinuousGradientVertically
+ _backgroundIsContinuousGradientVertically.cold.1
+ _bundleIDsToNamesMap.bundleIDsToNamesMap
+ _bundleIDsToNamesMap.onceToken
+ _class_getName
+ _forceApperanceVariant.apperanceVariant
+ _forceApperanceVariant.once
+ _forceSymbolEmbossment.once
+ _forceSymbolEmbossment.symbolName
+ _hintedBadgeRect.onceToken.104
+ _hintedBadgeRect.onceToken.197
+ _hintedBadgeRect.onceToken.339
+ _hintedBadgeRect.rect.103
+ _hintedBadgeRect.rect.196
+ _hintedBadgeRect.rect.338
+ _hintedCornerSize.onceToken.316
+ _hintedCornerSize.onceToken.347
+ _hintedCornerSize.size.315
+ _hintedCornerSize.size.346
+ _hintedFontSize.onceToken.205
+ _hintedFontSize.onceToken.355
+ _hintedFontSize.value.204
+ _hintedFontSize.value.354
+ _hintedPageCurlSize.onceToken.312
+ _hintedPageCurlSize.onceToken.343
+ _hintedPageCurlSize.size.311
+ _hintedPageCurlSize.size.342
+ _hintedPaperRect.onceToken.189
+ _hintedPaperRect.onceToken.306
+ _hintedPaperRect.onceToken.335
+ _hintedPaperRect.rect.188
+ _hintedPaperRect.rect.305
+ _hintedPaperRect.rect.334
+ _hintedShadowBlur.onceToken.209
+ _hintedShadowBlur.onceToken.320
+ _hintedShadowBlur.onceToken.359
+ _hintedShadowBlur.value.208
+ _hintedShadowBlur.value.319
+ _hintedShadowBlur.value.358
+ _hintedShadowOffset.onceToken.213
+ _hintedShadowOffset.onceToken.324
+ _hintedShadowOffset.onceToken.363
+ _hintedShadowOffset.value.212
+ _hintedShadowOffset.value.323
+ _hintedShadowOffset.value.362
+ _hintedShadowSpread.onceToken.217
+ _hintedShadowSpread.value.216
+ _hintedSymbolFontSize.onceToken
+ _hintedSymbolFontSize.value
+ _hintedTextFontSize.onceToken
+ _hintedTextFontSize.value
+ _hintedTextRect.onceToken.106
+ _hintedTextRect.onceToken.201
+ _hintedTextRect.onceToken.351
+ _hintedTextRect.rect.105
+ _hintedTextRect.rect.200
+ _hintedTextRect.rect.350
+ _kCGColorClear
+ _kCGColorWhite
+ _kISCatalogAssetAppearanceEmbeddedDark
+ _kISCatalogAssetAppearanceEmbeddedDefault
+ _kISCatalogAssetAppearanceEmbeddedLight
+ _kISCatalogAssetAppearanceMacDark
+ _kISCatalogAssetAppearanceMacDefault
+ _kISCatalogAssetAppearanceMacLight
+ _kISDefaultGraphicIconSymbolName
+ _kISDocumentIconConfiguration
+ _kISIconConfigurationKeyFolderIcon
+ _kISIconConfigurationKeySymbolName
+ _kISIconConfigurationKeyTintColor
+ _kISSecondaryResourceKey
+ _kISSymbolName
+ _kISTertiaryResourceKey
+ _objc_allocWithZone
+ _objc_getAssociatedObject
+ _objc_msgSend$CUINamedImageDeviceClass
+ _objc_msgSend$ICRAppearance
+ _objc_msgSend$ICRIconLayer
+ _objc_msgSend$ICRRenderingMode
+ _objc_msgSend$_IF_UUIDWithDigestBytes:size:
+ _objc_msgSend$_IF_arrayForKeys:
+ _objc_msgSend$_IS_appearanceNameFromAppearance:platform:
+ _objc_msgSend$_IS_assetAppearance
+ _objc_msgSend$_IS_cuiShadowStyleFromStyle:
+ _objc_msgSend$_IS_finalizedIconWithCompositingDescriptor:
+ _objc_msgSend$_IS_iconStackWithName:scale:locale:platform:appearance:
+ _objc_msgSend$_IS_imageWithCompositingDescriptor:
+ _objc_msgSend$_IS_layerObjectForKey:
+ _objc_msgSend$_IS_nameWithRequestedAppearance:
+ _objc_msgSend$_IS_possibleIconStackExistsWithName:platform:
+ _objc_msgSend$_activeSignpostsForDescriptor:
+ _objc_msgSend$_computeImageWithCGImage:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:
+ _objc_msgSend$_computeImageWithWidth:height:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:
+ _objc_msgSend$_computeImageWithWidth:height:strict:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:
+ _objc_msgSend$_createDarkFallbackIcon_iOS
+ _objc_msgSend$_createDarkFallbackIcon_macOS
+ _objc_msgSend$_createLightFallbackIcon_iOS
+ _objc_msgSend$_createLightFallbackIcon_macOS
+ _objc_msgSend$_createTintedFallbackIcon_iOS
+ _objc_msgSend$_createTintedFallbackIcon_macOS
+ _objc_msgSend$_determineRecipe
+ _objc_msgSend$_iconStackComposerForNamedImage:
+ _objc_msgSend$_imageForMultisizeImage:size:scale:
+ _objc_msgSend$_isApp
+ _objc_msgSend$_isAppLike
+ _objc_msgSend$_lookupForSize:scale:
+ _objc_msgSend$_platform:withinAllowedPlatforms:allowNative:
+ _objc_msgSend$_platformCatalogWithName:
+ _objc_msgSend$_prepareMaskIfNeeded
+ _objc_msgSend$_tagForLongLife:
+ _objc_msgSend$_tweakCopiedImageDescriptorsIfNecessary:
+ _objc_msgSend$addLayer:
+ _objc_msgSend$aliasedConfigurationDictionary
+ _objc_msgSend$alpha
+ _objc_msgSend$asset
+ _objc_msgSend$assetAppearance
+ _objc_msgSend$assetAppearanceForAppearance:appearanceVariant:
+ _objc_msgSend$assetsURLs
+ _objc_msgSend$assignLayerResources
+ _objc_msgSend$backgroundResource
+ _objc_msgSend$badgeWithSymbol
+ _objc_msgSend$baseStackForDescriptor:
+ _objc_msgSend$blue
+ _objc_msgSend$blurForAppearance:
+ _objc_msgSend$bundleIDsToNamesMap
+ _objc_msgSend$bundlePlatform
+ _objc_msgSend$cacheMissIconResourceForPlatform:
+ _objc_msgSend$categorizeShapeWithWidth:height:cornerRadius:
+ _objc_msgSend$classifySpecular
+ _objc_msgSend$classifySpecularWithDebug:
+ _objc_msgSend$colorString
+ _objc_msgSend$colorWithName:designSystem:palette:colorScheme:contrast:styling:displayGamut:error:
+ _objc_msgSend$colorsForKey:
+ _objc_msgSend$compositingDescriptor
+ _objc_msgSend$computeGrayscaleConversionColorWithWidth:height:samples:
+ _objc_msgSend$computeMaskWithWidth:height:samples:foregroundMask:
+ _objc_msgSend$configDict
+ _objc_msgSend$cornerRadius
+ _objc_msgSend$createDarkFallbackIcon
+ _objc_msgSend$createDarkImageWithCGImage:feedback:
+ _objc_msgSend$createForegroundImageWithCGImage:feedback:
+ _objc_msgSend$createLightFallbackIcon
+ _objc_msgSend$createSolariumTintableImageWithCGImage:feedback:
+ _objc_msgSend$createSpecularImage
+ _objc_msgSend$createTintableImageMaskWithCGImage:tintableOpacityImageMask:
+ _objc_msgSend$createTintedFallbackIcon
+ _objc_msgSend$curlResource
+ _objc_msgSend$darkImage
+ _objc_msgSend$decodeXPCObjectOfType:forKey:
+ _objc_msgSend$defaultMacUnknownFSObjectResource
+ _objc_msgSend$detectShapeInCGImage:bounds:cornerRadius:
+ _objc_msgSend$detectShapeInImageWithWidth:height:samples:bounds:cornerRadius:
+ _objc_msgSend$digest:size:
+ _objc_msgSend$disableShadow
+ _objc_msgSend$drawsLightingEffects
+ _objc_msgSend$emoji
+ _objc_msgSend$encodeXPCObject:forKey:
+ _objc_msgSend$enumerateChildTypesWithBlock:
+ _objc_msgSend$externalCompositingResource
+ _objc_msgSend$extrapolateIconStack
+ _objc_msgSend$featureOverride
+ _objc_msgSend$feedback
+ _objc_msgSend$fillColorForAppearance:
+ _objc_msgSend$finalizeAtSize:scale:
+ _objc_msgSend$finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:
+ _objc_msgSend$folderColor
+ _objc_msgSend$folderEmpty
+ _objc_msgSend$forceApperanceVariant
+ _objc_msgSend$forceSymbolEmbossment
+ _objc_msgSend$foreground
+ _objc_msgSend$foregroundAndLightingEffectsImage
+ _objc_msgSend$generationReport
+ _objc_msgSend$gradientWithSize:
+ _objc_msgSend$green
+ _objc_msgSend$hasBespokeBackground
+ _objc_msgSend$hasEffectsForAppearance:
+ _objc_msgSend$hasLightEffects
+ _objc_msgSend$hasLightingEffects
+ _objc_msgSend$hasOverlappingChildSpecularsCombinedForAppearance:
+ _objc_msgSend$hasSpecularForAppearance:
+ _objc_msgSend$hasText
+ _objc_msgSend$hasTint
+ _objc_msgSend$hintedSymbolFontSize
+ _objc_msgSend$hintedTextFontSize
+ _objc_msgSend$iOSCatalog
+ _objc_msgSend$iconConfig
+ _objc_msgSend$iconLayerStackWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:appearanceName:locale:
+ _objc_msgSend$iconLayers
+ _objc_msgSend$iconStack
+ _objc_msgSend$iconStackAppIconsAllowed
+ _objc_msgSend$iconStackForDescriptor:
+ _objc_msgSend$iconStackForSize:scale:
+ _objc_msgSend$iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:
+ _objc_msgSend$iconStackResourcesAllowed
+ _objc_msgSend$iconTreatment
+ _objc_msgSend$imageForCompositingDescriptor:
+ _objc_msgSend$imageLayers
+ _objc_msgSend$initWithBundleID:
+ _objc_msgSend$initWithBundleIdentifier:imageLayers:
+ _objc_msgSend$initWithCGColor:
+ _objc_msgSend$initWithCGImage:idiom:
+ _objc_msgSend$initWithCGImage:scale:finalizedIcon:
+ _objc_msgSend$initWithCGImage:scale:layerData:
+ _objc_msgSend$initWithCatalog:imageName:platform:
+ _objc_msgSend$initWithConfigurationDictionary:
+ _objc_msgSend$initWithDarkImage:drawsLightingEffects:feedback:
+ _objc_msgSend$initWithForeground:background:recolorForeground:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithIconDictionary:
+ _objc_msgSend$initWithIconStack:
+ _objc_msgSend$initWithIconTreatment:hasLightingEffects:
+ _objc_msgSend$initWithIdiom:
+ _objc_msgSend$initWithImage:cornerRadius:
+ _objc_msgSend$initWithImage:foregroundAndLightingEffectsImage:feedback:
+ _objc_msgSend$initWithImageDescriptor:
+ _objc_msgSend$initWithLegacyAsset:assetAppearance:platform:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithNumberOfColors:
+ _objc_msgSend$initWithResource:
+ _objc_msgSend$initWithSpecularImage:useAlphaOnly:
+ _objc_msgSend$initWithSymbolName:tintColor:
+ _objc_msgSend$initWithSystemColor:appearance:contrast:vibrancy:
+ _objc_msgSend$initWithTintableImage:drawsLightingEffects:feedback:
+ _objc_msgSend$initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:
+ _objc_msgSend$initWithType:iconConfiguration:
+ _objc_msgSend$initWithTypeIdentifier:configuration:
+ _objc_msgSend$initWithTypeIdentifier:iconLayers:
+ _objc_msgSend$initWithTypeIdentifier:layerGroups:
+ _objc_msgSend$isBadgedWithSymbol
+ _objc_msgSend$isCompositedDocument
+ _objc_msgSend$isEnhancedGlassEnabled
+ _objc_msgSend$isInjectSolariumAssetsEnabled
+ _objc_msgSend$isSolariumCornerRadiusEnabled
+ _objc_msgSend$isSolariumEnabled
+ _objc_msgSend$layerCount
+ _objc_msgSend$layerGroups
+ _objc_msgSend$layeredIconResource
+ _objc_msgSend$layers
+ _objc_msgSend$legacyFinalizedIconWithSize:scale:deviceClass:appearance:renderingMode:
+ _objc_msgSend$macOSCatalog
+ _objc_msgSend$macosIconSpecification
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$opacityForAppearance:
+ _objc_msgSend$pageResource
+ _objc_msgSend$platformCatalog
+ _objc_msgSend$primaryColour
+ _objc_msgSend$recolorForeground
+ _objc_msgSend$red
+ _objc_msgSend$renderCGImageAtSize:scale:
+ _objc_msgSend$renderedFullBleedIconWithConfiguration:
+ _objc_msgSend$renderedIconWithConfiguration:
+ _objc_msgSend$renderedLegacyCompatibleIconWithConfiguration:forDeviceClass:maskToIconShape:
+ _objc_msgSend$renderedSystemGlassCompatibleIconWithConfiguration:
+ _objc_msgSend$resolvedTintColorForAppearance:
+ _objc_msgSend$segmentationIdiom
+ _objc_msgSend$serializeLayerObjectForCaching
+ _objc_msgSend$serializedDataWithError:
+ _objc_msgSend$setBadgeWithSymbol:
+ _objc_msgSend$setBlur:forAppearance:
+ _objc_msgSend$setBlurStrength:
+ _objc_msgSend$setBundlePlatform:
+ _objc_msgSend$setCGColor:
+ _objc_msgSend$setColors:andStops:
+ _objc_msgSend$setCompositingDescriptor:
+ _objc_msgSend$setDisableShadow:
+ _objc_msgSend$setExtrapolateIconStack:
+ _objc_msgSend$setFillColor:forAppearance:
+ _objc_msgSend$setGathersSpecularByElement:
+ _objc_msgSend$setGenerationReport:
+ _objc_msgSend$setGradientEndPoint:
+ _objc_msgSend$setGradientStartPoint:
+ _objc_msgSend$setGradientType:
+ _objc_msgSend$setHasBespokeBackground:
+ _objc_msgSend$setHasEffects:
+ _objc_msgSend$setHasEffects:forAppearance:
+ _objc_msgSend$setHasLightingEffects:
+ _objc_msgSend$setHasOverlappingChildSpecularsCombined:
+ _objc_msgSend$setHasOverlappingChildSpecularsCombined:forAppearance:
+ _objc_msgSend$setHasSpecular:
+ _objc_msgSend$setHasSpecular:forAppearance:
+ _objc_msgSend$setHasText:
+ _objc_msgSend$setIconConfig:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setLayerGroups:
+ _objc_msgSend$setLayers:
+ _objc_msgSend$setMaskBadgeResource:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setOpacity:forAppearance:
+ _objc_msgSend$setSerializeLayerObjectForCaching:
+ _objc_msgSend$setShadow:
+ _objc_msgSend$setShadow:forAppearance:
+ _objc_msgSend$setShadowOpacity:
+ _objc_msgSend$setShadowStyle:
+ _objc_msgSend$setShadowStyle:forAppearance:
+ _objc_msgSend$setSvgDocumentURL:
+ _objc_msgSend$setSymbolName:
+ _objc_msgSend$setTranslucency:
+ _objc_msgSend$setTranslucency:forAppearance:
+ _objc_msgSend$setTreatLikeSymbol:
+ _objc_msgSend$setUseLegacyCompatibilityMode:
+ _objc_msgSend$setUsesExternalCompositor:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$shadowForAppearance:
+ _objc_msgSend$shadowStyleForAppearance:
+ _objc_msgSend$shouldUseFolderRecipe:
+ _objc_msgSend$standardCornerRadiusForSize:
+ _objc_msgSend$supportsRequestingIconStacksForPlatform:
+ _objc_msgSend$systemTintColor
+ _objc_msgSend$textResource
+ _objc_msgSend$tintWithRed:green:blue:alpha:
+ _objc_msgSend$tintableImage
+ _objc_msgSend$translucencyForAppearance:
+ _objc_msgSend$treatLikeSymbol
+ _objc_msgSend$updateWithImageDescriptor:
+ _objc_msgSend$useLegacyCompatibilityMode
+ _objc_msgSend$usesExternalCompositor
+ _objc_msgSend$watchOSCatalog
+ _objc_msgSend$wrappedResource
+ _objc_opt_self
+ _objc_release_x2
+ _objc_retain_x6
+ _objc_setAssociatedObject
+ _object_getClass
+ _sharedInstance.onceToken.17
+ _sharedInstance.onceToken.27
+ _sharedInstance.onceToken.39
+ _sharedInstance.onceToken.49
+ _sharedInstance.onceToken.65
+ _sharedInstance.sharedInstance.16
+ _sharedInstance.sharedInstance.26
+ _sharedInstance.sharedInstance.38
+ _sharedInstance.sharedInstance.48
+ _sharedInstance.sharedInstance.64
+ _swift_errorRelease
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _symbolic _____Sg 13IconRendering12ICRIconIdiomO
+ _updateFlag
+ _validateCorner
+ _validateOpaqueCenter
+ _validateTransparentMargin
+ _xpc_shmem_create_readonly
+ _xpc_shmem_map
- +[CUICatalog(IconServicesAdditions) _IS_appearanceNameFromAppearance:]
- +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:symbolName:platform:error:]
- +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:symbolName:platform:error:].cold.1
- +[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:symbolName:platform:error:].cold.2
- +[ISAssetCatalogResource assetCatalogResourceWithURL:symbolName:error:]
- +[ISAssetCatalogResource coreGlyphsCatalog]
- +[ISAssetCatalogResource coreGlyphsCatalog].cold.1
- +[ISIcon(CALayerDelegate) layerUpdateQueue]
- +[ISIcon(CALayerDelegate) layerUpdateQueue].cold.1
- -[ISAssetCatalogResource catalogAppearance]
- -[ISAssetCatalogResource initWithCatalog:imageName:symbolName:platform:]
- -[ISAssetCatalogResource symbolName]
- -[ISAssetCatalogResource(Symbols) symbolImageForFontSize:scale:symbolSize:symbolWeight:]
- -[ISAssetCatalogResource(Symbols) symbolImageForSize:scale:]
- -[ISBiasedGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:ucharSamples:]
- -[ISDefaults debugGraphicIconColor]
- -[ISDefaults debugGraphicIconColor].cold.1
- -[ISDefaults debugISIconGraphicIconColor]
- -[ISDefaults debugISIconGraphicIconColor].cold.1
- -[ISDefaults debugPreDefinedGraphicIconColor]
- -[ISDefaults debugPreDefinedGraphicIconColor].cold.1
- -[ISDefaults isDebugGraphicIconColourEnabled]
- -[ISDefaults isDebugGraphicIconColourEnabled].cold.1
- -[ISFloydGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:ucharSamples:]
- -[ISForegroundSegmentation computeMaskWithWidth:height:ucharSamplesAndMask:]
- -[ISGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:ucharSamples:]
- -[ISIcon _eventPrepareISIconSignpost:message:]
- -[ISIcon(CALayerDelegate) displayLayer:]
- -[ISIcon(CALayerDelegate) displayLayer:].cold.1
- -[ISIconLayer backgroundStyle]
- -[ISIconLayer badgeOptions]
- -[ISIconLayer drawBorder]
- -[ISIconLayer iconManager:didInvalidateIcons:]
- -[ISIconLayer iconShape]
- -[ISIconLayer icon]
- -[ISIconLayer initWithIcon:]
- -[ISIconLayer init]
- -[ISIconLayer setBackgroundStyle:]
- -[ISIconLayer setBadgeOptions:]
- -[ISIconLayer setDrawBorder:]
- -[ISIconLayer setIcon:]
- -[ISIconLayer setIconShape:]
- -[ISIconLayer setShouldApplyMask:]
- -[ISIconLayer setVariantOptions:]
- -[ISIconLayer shouldApplyMask]
- -[ISIconLayer variantOptions]
- -[ISIconSegmentation _computeImageWithCGImage:ucharTintable:ucharDark:feedback:]
- -[ISIconSegmentation _computeImageWithWidth:height:strict:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:]
- -[ISIconSegmentation _computeImageWithWidth:height:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:]
- -[ISIconSegmentation createTintableImageWithCGImage:]
- -[ISIconSegmentation init]
- -[ISLuminanceGrayscaleConversion computeGrayscaleConversionColorWithWidth:height:ucharSamples:]
- -[ISResourceProvider(Convenience) isDocumentBadge]
- _ISCreateCGImageMaskUchar4LastComponent
- _OBJC_CLASS_$_CALayer
- _OBJC_CLASS_$_IFSymbolImage
- _OBJC_IVAR_$_ISAssetCatalogResource._symbolName
- _OBJC_IVAR_$_ISDimmingConversion._alphaInfo
- _OBJC_IVAR_$_ISDimmingConversion._ucharSamples
- _OBJC_IVAR_$_ISGenerationResponse._data
- _OBJC_IVAR_$_ISIconLayer._backgroundStyle
- _OBJC_IVAR_$_ISIconLayer._badgeOptions
- _OBJC_IVAR_$_ISIconLayer._drawBorder
- _OBJC_IVAR_$_ISIconLayer._icon
- _OBJC_IVAR_$_ISIconLayer._iconShape
- _OBJC_IVAR_$_ISIconLayer._shape
- _OBJC_IVAR_$_ISIconLayer._shouldApplyMask
- _OBJC_IVAR_$_ISIconLayer._variantOptions
- _OBJC_METACLASS_$_CALayer
- __OBJC_$_CATEGORY_IFImage_$_ISScalableCompositorResource
- __OBJC_$_CATEGORY_INSTANCE_METHODS_IFImage_$_ISScalableCompositorResource
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ISCompositorResourceProvider
- __OBJC_$_CLASS_METHODS_IFImage(ISScalableCompositorResource|ISPlaceholderImage)
- __OBJC_$_CLASS_METHODS_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|CALayerDelegate|LIIconVariant|TemplateHack)
- __OBJC_$_INSTANCE_METHODS_ISAssetCatalogResource(Symbols)
- __OBJC_$_INSTANCE_METHODS_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|CALayerDelegate|LIIconVariant|TemplateHack)
- __OBJC_$_PROP_LIST_IFImage_$_ISScalableCompositorResource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CALayerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CALayerDelegate
- __OBJC_$_PROTOCOL_REFS_CALayerDelegate
- __OBJC_CATEGORY_PROTOCOLS_$_IFImage_$_ISScalableCompositorResource
- __OBJC_CLASS_PROTOCOLS_$_ISIcon(Experimental|Workaround|DebugAdditions|ISScalableCompositorResource|CALayerDelegate|LIIconVariant|TemplateHack)
- __OBJC_CLASS_PROTOCOLS_$_ISIconLayer
- __OBJC_LABEL_PROTOCOL_$_CALayerDelegate
- __OBJC_PROTOCOL_$_CALayerDelegate
- ___35-[ISDefaults debugGraphicIconColor]_block_invoke
- ___40-[ISIcon(CALayerDelegate) displayLayer:]_block_invoke
- ___41-[ISDefaults debugISIconGraphicIconColor]_block_invoke
- ___43+[ISAssetCatalogResource coreGlyphsCatalog]_block_invoke
- ___43+[ISIcon(CALayerDelegate) layerUpdateQueue]_block_invoke
- ___45-[ISDefaults debugPreDefinedGraphicIconColor]_block_invoke
- ___45-[ISDefaults isDebugGraphicIconColourEnabled]_block_invoke
- ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.20
- ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.20.cold.1
- ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.32
- ___90+[ISAssetCatalogResource assetCatalogResourceWithURL:imageName:symbolName:platform:error:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.104
- ___block_literal_global.106
- ___block_literal_global.117
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.239
- ___block_literal_global.243
- ___block_literal_global.247
- ___block_literal_global.251
- ___block_literal_global.265
- ___block_literal_global.269
- ___block_literal_global.27
- ___block_literal_global.273
- ___block_literal_global.277
- ___block_literal_global.281
- ___block_literal_global.285
- ___block_literal_global.289
- ___block_literal_global.293
- ___block_literal_global.35
- ___block_literal_global.40
- ___block_literal_global.43
- ___block_literal_global.45
- ___block_literal_global.49
- ___block_literal_global.56
- ___block_literal_global.65
- ___block_literal_global.72
- ___block_literal_global.74
- ___block_literal_global.82
- _colorsFromGraphicSymbolRecipe
- _computeIconSegmentationFlagForExtraConfidence
- _computeSampleAndLuma
- _coreGlyphsCatalog.catalog
- _coreGlyphsCatalog.onceToken
- _debugGraphicIconColor.color
- _debugGraphicIconColor.once
- _debugISIconGraphicIconColor.color
- _debugISIconGraphicIconColor.once
- _debugPreDefinedGraphicIconColor.color
- _debugPreDefinedGraphicIconColor.once
- _hintedBadgeRect.onceToken.111
- _hintedBadgeRect.onceToken.267
- _hintedBadgeRect.rect.110
- _hintedBadgeRect.rect.266
- _hintedCornerSize.onceToken.241
- _hintedCornerSize.onceToken.275
- _hintedCornerSize.size.240
- _hintedCornerSize.size.274
- _hintedFontSize.onceToken.119
- _hintedFontSize.onceToken.283
- _hintedFontSize.value.118
- _hintedFontSize.value.282
- _hintedPageCurlSize.onceToken.237
- _hintedPageCurlSize.onceToken.271
- _hintedPageCurlSize.size.236
- _hintedPageCurlSize.size.270
- _hintedPaperRect.onceToken.231
- _hintedPaperRect.onceToken.263
- _hintedPaperRect.rect.230
- _hintedPaperRect.rect.262
- _hintedShadowBlur.onceToken.245
- _hintedShadowBlur.onceToken.287
- _hintedShadowBlur.value.244
- _hintedShadowBlur.value.286
- _hintedShadowOffset.onceToken.249
- _hintedShadowOffset.onceToken.291
- _hintedShadowOffset.value.248
- _hintedShadowOffset.value.290
- _hintedTextRect.onceToken.115
- _hintedTextRect.onceToken.279
- _hintedTextRect.rect.114
- _hintedTextRect.rect.278
- _isDebugGraphicIconColourEnabled.once
- _isDebugGraphicIconColourEnabled.result
- _kISCatalogAssetAppearanceAny
- _kISCatalogAssetAppearanceDark
- _kISCatalogAssetAppearanceLight
- _kISForegroundSegmentationLooseBooleanThreshold
- _kISForegroundSegmentationStrictBooleanThreshold
- _kISIconSegmentationBackgroundStyleContinuousGradient
- _kISIconSegmentationBackgroundStyleKey
- _kISIconSegmentationBackgroundStyleSingleColor
- _kISIconSegmentationForegroundStyleContinuousGradient
- _kISIconSegmentationForegroundStyleKey
- _kISIconSegmentationForegroundStyleMultipleColors
- _kISIconSegmentationForegroundStyleSingleColor
- _kISIconSegmentationNumberOfForegroundColorsKey
- _layerUpdateQueue.layerUpdateQueue
- _layerUpdateQueue.onceToken
- _nameFromGraphicSymbolRecipe
- _objc_msgSend$_IS_appearanceNameFromAppearance:
- _objc_msgSend$_computeImageWithCGImage:ucharTintable:ucharDark:feedback:
- _objc_msgSend$_computeImageWithWidth:height:strict:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:
- _objc_msgSend$_computeImageWithWidth:height:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:
- _objc_msgSend$_eventPrepareISIconSignpost:message:
- _objc_msgSend$assetCatalogResourceWithURL:imageName:symbolName:platform:error:
- _objc_msgSend$catalogAppearance
- _objc_msgSend$computeGrayscaleConversionColorWithWidth:height:ucharSamples:
- _objc_msgSend$computeMaskWithWidth:height:ucharSamplesAndMask:
- _objc_msgSend$contentsScale
- _objc_msgSend$coreGlyphsCatalog
- _objc_msgSend$createTintableImageWithCGImage:
- _objc_msgSend$debugGraphicIconColor
- _objc_msgSend$debugISIconGraphicIconColor
- _objc_msgSend$debugPreDefinedGraphicIconColor
- _objc_msgSend$displayLayer:
- _objc_msgSend$iconShape
- _objc_msgSend$initWithCatalog:imageName:symbolName:platform:
- _objc_msgSend$initWithIcon:
- _objc_msgSend$initWithNamedVectorGlyph:
- _objc_msgSend$isDebugGraphicIconColourEnabled
- _objc_msgSend$isDocumentBadge
- _objc_msgSend$layerUpdateQueue
- _objc_msgSend$namedVectorGlyphWithName:scaleFactor:deviceIdiom:layoutDirection:glyphSize:glyphWeight:glyphPointSize:appearanceName:
- _objc_msgSend$preferredFrameSize
- _objc_msgSend$rasterizeImageUsingScaleFactor:forTargetSize:
- _objc_msgSend$setContents:
- _objc_msgSend$setDebugColourSet:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setNeedsDisplay
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$symbolImageForSize:scale:
- _rendingModeFromGraphicSymbolRecipe
- _sharedInstance.onceToken.15
- _sharedInstance.onceToken.25
- _sharedInstance.onceToken.37
- _sharedInstance.onceToken.47
- _sharedInstance.onceToken.63
- _sharedInstance.sharedInstance.14
- _sharedInstance.sharedInstance.24
- _sharedInstance.sharedInstance.36
- _sharedInstance.sharedInstance.46
- _sharedInstance.sharedInstance.62
CStrings:
+ "!"
+ "# non-continuous at x = %d, y = %d"
+ "%@ RETURNING App PLACEHOLDER: <ISImageDescriptor: %p> s (%0.2f, %0.2f)@%.0fx v:%lx a:%ld:%ld ps:%ld "
+ "%@ RETURNING AppClip PLACEHOLDER: <ISImageDescriptor: %p> s (%0.2f, %0.2f)@%.0fx v:%lx a:%ld:%ld ps:%ld "
+ "%@ RETURNING cache miss PLACEHOLDER: <ISImageDescriptor: %p> s (%0.2f, %0.2f)@%.0fx v:%lx a:%ld:%ld ps:%ld "
+ "%@ name:%@ scaleFactor:%f deviceIdiom:%d deviceSubtype:%d displayGamut:%d locale:%@ appearanceName:%@"
+ "%@, Symbol: %@, Emoji: %@, Tint: %ld - %@, Empty: %d"
+ "%@_Layer%d"
+ "%d"
+ "%f,%f,%f,%f"
+ "'"
+ "-[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:]"
+ ". Resolved item appearance: %@"
+ "01:31:22"
+ "48@0:8i16i20{?=iiiI^}24"
+ "<%s %p> Bundle URL: %@ type: %@ tag: %@ tag class: %@ digest:%@"
+ "<%s %p> Icon: %@, Alias: %@"
+ "<%s %p> Tag: %@, Class: %@, Base type: %@"
+ "<%s %p> Type: %@, Config: %@, Digest:%@"
+ "<%s %p> identity: %@ digest: %@"
+ "<%s %p>BundleID: %@ digest: %@"
+ "<%s %p>icon: %@ decorations: %@"
+ "<ISImageDescriptor: %p> (%0.2f, %0.2f)@%.0fx v:%lx l:%lu a:%ld:%ld:%ld:%ld t:%g:%g:%g:%g s:%ld ps: %ld digest: %@"
+ "@\"<ISIconConfiguration>\""
+ "@\"<ISIconSegmentationFeedbackBackground>\""
+ "@\"<ISIconSegmentationFeedbackForeground>\""
+ "@\"<ISIconSegmentationFeedbackRecolor>\""
+ "@\"CUINamedIconLayerStack\""
+ "@\"CUINamedIconLayerStack\"40@0:8{CGSize=dd}16d32"
+ "@\"ISCompositingDescriptor\""
+ "@\"ISIconSegmentationFeedback\""
+ "@\"NSObject<OS_xpc_object>\""
+ "@\"NSUUID\"16@0:8"
+ "@20@0:8S16"
+ "@20@0:8i16"
+ "@24@0:8^{CGColor=}16"
+ "@28@0:8Q16B24"
+ "@28@0:8^{CGImage=}16B24"
+ "@32@0:8^{CGImage=}16@24"
+ "@32@0:8^{CGImage=}16Q24"
+ "@32@0:8q16Q24"
+ "@36@0:8^{CGImage=}16B24@28"
+ "@40@0:8^{CGImage=}16^{CGImage=}24@32"
+ "@40@0:8^{CGImage=}16q24Q32"
+ "@48@0:8@16{CGSize=dd}24d40"
+ "@48@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40"
+ "@56@0:8@16d24@32Q40q48"
+ "@56@0:8{CGSize=dd}16d32q40^@48"
+ "@84@0:8{CGSize=dd}16q32Q40q48q56@64B72Q76"
+ "App Store"
+ "Attempting to finalize `%@ - %@` with (%0.2f, %0.2f)@%ld p:%ld a:%ld:%ld t:%@ isLegacy:%d"
+ "B136@0:8i16i20^{CGColorSpace=}24{?=iiiI^}32{?=iiiB(?=^*)}56*80*88^96^104*112^120^@128"
+ "B140@0:8i16i20B24^{CGColorSpace=}28{?=iiiI^}36{?=iiiB(?=^*)}60*84*92^100^108*116^124^@132"
+ "B24@0:8^16"
+ "B32@0:8^v16Q24"
+ "B36@0:8Q16@24B32"
+ "B40@0:8^{CGImage=}16^24^i32"
+ "B64@0:8i16i20{?=iiiI^}24^48^i56"
+ "B72@0:8i16i20{?=iiiI^}24{?=iiiB(?=^*)}48"
+ "B80@0:8^{CGImage=}16*24*32^40^48*56^64^@72"
+ "Books"
+ "CIColorMonochrome"
+ "CUINamedImageDeviceClass"
+ "CacheMissIcon_iOS"
+ "Cannot set generation report when one already exists."
+ "Center Emoji Text"
+ "DELAYING_PREPARE: - delay: %lf , "
+ "Dark Credenza"
+ "Dark Segmented"
+ "Emboss Layer"
+ "EnhancedGlass"
+ "Failed to compose icon stack for unknown appearance: %lu"
+ "Failed to construct finalized icon stack"
+ "Failed to create a flatten representation of the finalized icon"
+ "Failed to finalize icon"
+ "Failed to finalized ISLayeredIcon icon"
+ "Failed to find icon stack for"
+ "Failed to find icon stack for with named: %@ for size: (%f,%f) scale:(%lf)"
+ "Failed to find layer stack flatten image for with named: %@ for size: (%f,%f) scale:(%lf)"
+ "Failed to find multisized image for with named: %@ for size: (%f,%f) scale:(%lf)"
+ "Failed to generate image from composed icon stack"
+ "Failed to render icon stack to cgimage"
+ "Failed to retrieve cache miss icon resource for platform: %lu"
+ "Failed to serialize finalized icon. Error: %@"
+ "Failed to utilize overrides asset catalog %@. Error: %@"
+ "Fill"
+ "Find My"
+ "FolderAdditions"
+ "Found catalog image with query info name:%@ scaleFactor:%f deviceIdiom:%d deviceSubtype:%d displayGamut:%d layoutDirection:%d desiredSize:%f,%f appearanceName:%@]. Resolved appearance: %@"
+ "Found component type `%@` for icon package `%@`"
+ "Found icon stack with query info"
+ "Freeform"
+ "GenerationReport"
+ "ICRAppearance"
+ "ICRIconLayer"
+ "ICRRenderingMode"
+ "IGNORING_CACHE"
+ "ISA_GENERATEING_IMAGE"
+ "ISCompositingDescriptor"
+ "ISDarkFallbackIcon"
+ "ISDocumentIconConfiguration"
+ "ISDocumentRecipe"
+ "ISFallbackIcon"
+ "ISFallbackIconDarkSegmented"
+ "ISFallbackIconFactory"
+ "ISFallbackIconFill"
+ "ISFallbackIconScaleDown"
+ "ISFallbackIconTintedSegmented"
+ "ISFlattenLayerStackAssetCatalogResource"
+ "ISFolderIconConfiguration"
+ "ISFolderIconConfigurationParser"
+ "ISFolderRecipe"
+ "ISForceApperancVariant"
+ "ISForceSymbolEmbossment"
+ "ISGenerationReport"
+ "ISGraphicIconConfigurationParser"
+ "ISICRIconLayerWrapper"
+ "ISIcon: %@, descriptor: <ISImageDescriptor: %p> s (%0.2f, %0.2f)@%.0fx v:%lx a:%ld:%ld ps:%ld , func: %s, Digest=%{signpost.telemetry:string1}@, NumDescriptors=%{signpost.telemetry:number1}lu enableTelemetry=YES "
+ "ISIconConfiguration"
+ "ISIconConfigurationMarkupParser"
+ "ISIconLayerElement"
+ "ISIconLayerGroup"
+ "ISIconPackage"
+ "ISIconPackageIdentifier"
+ "ISIconSegmentationFeedback"
+ "ISIconSegmentationFeedbackBackground"
+ "ISIconSegmentationFeedbackBilinearGradient"
+ "ISIconSegmentationFeedbackComplex"
+ "ISIconSegmentationFeedbackForeground"
+ "ISIconSegmentationFeedbackMultipleColors"
+ "ISIconSegmentationFeedbackRecolor"
+ "ISIconSegmentationFeedbackSingleColor"
+ "ISIconStackAssetCatalogResource"
+ "ISIconStackComposer"
+ "ISIconStackComposer.m"
+ "ISIconStackCompositeResource"
+ "ISIconStackResource"
+ "ISLayeredIcon"
+ "ISLayers"
+ "ISLightFallbackIcon"
+ "ISMaskEffect"
+ "ISMonochromeTintEffect"
+ "ISMultisizedAssetCatalogResource"
+ "ISShapeDetection"
+ "ISSpecularClassification"
+ "ISStaticIconStackAssetCatalogResource"
+ "ISSymbolEffect"
+ "ISSymbolTreatment"
+ "ISTintedFallbackIcon"
+ "ISTypeIdentifiers"
+ "Internal"
+ "Internal Composite"
+ "Keynote"
+ "LayeredIconAdditions"
+ "Looking for resources matching the iconset naming convention. Named: %@ for size: (%f,%f) scale:(%lf)"
+ "Maps"
+ "Music"
+ "NO"
+ "NSAppearanceNameAqua"
+ "NSAppearanceNameDarkAqua"
+ "NSAppearanceNameSystem"
+ "Natural Icon Stack"
+ "News"
+ "No images provided!"
+ "Notes"
+ "Other Segmented"
+ "OverrideAssets_ios"
+ "OverrideAssets_macos"
+ "OverrideAssets_watchos"
+ "OverrideSolarium"
+ "Overriding tint/embossing with config content: %@"
+ "PREPARE_IGNORING_CACHE"
+ "PREPARE_IMAGE"
+ "Pages"
+ "Podcasts"
+ "Q28@0:8i16i20i24"
+ "RETURNING_PLACEHOLDER"
+ "RETURNING_STALE_PLACEHOLDER"
+ "Reminders"
+ "Retrieving component icons for icon package `%@`"
+ "S16@0:8"
+ "STORE_LOOKUP"
+ "Scale Down"
+ "Solarium"
+ "SolariumCornerRadius"
+ "Stocks"
+ "SwiftUI"
+ "SwiftWrappers_Internal._ISWrapper_CUINamedIconLayerStack"
+ "Symbol: %@, Emoji: %@, Colour string: %@, Empty: %d"
+ "T@\"<ISIconConfiguration>\",&,V_iconConfig"
+ "T@\"<ISIconConfiguration>\",R,V_iconConfig"
+ "T@\"<ISIconSegmentationFeedbackBackground>\",R,N,V_background"
+ "T@\"<ISIconSegmentationFeedbackForeground>\",R,N,V_foreground"
+ "T@\"<ISIconSegmentationFeedbackRecolor>\",R,N,V_recolorForeground"
+ "T@\"<ISScalableCompositorResource>\",&,N,V_layeredIconResource"
+ "T@\"<ISScalableCompositorResource>\",R,V_externalCompositingResource"
+ "T@\"<ISScalableCompositorResource>\",R,V_wrappedResource"
+ "T@\"CUICatalog\",&,N,V_platformCatalog"
+ "T@\"CUINamedIconLayerStack\",&,N,V_iconStack"
+ "T@\"CUINamedIconLayerStack\",N,R,ViconStack"
+ "T@\"IFColor\",&,V_chicletHighlightColour"
+ "T@\"IFColor\",&,V_primaryColour"
+ "T@\"IFColor\",&,V_secondaryColour"
+ "T@\"IFColor\",&,V_tintColor"
+ "T@\"IFColor\",C"
+ "T@\"IFColor\",C,V_tintColor"
+ "T@\"ISBiasedGrayscaleConversion\",R,N,V_grayscaleConversion"
+ "T@\"ISCompositingDescriptor\",&,V_compositingDescriptor"
+ "T@\"ISGenerationReport\",&"
+ "T@\"ISIconSegmentationFeedback\",R,N,V_feedback"
+ "T@\"NSArray\",&,V_layerGroups"
+ "T@\"NSArray\",C,V_icons"
+ "T@\"NSArray\",C,V_layers"
+ "T@\"NSArray\",R,V_iconLayers"
+ "T@\"NSArray\",R,V_imageLayers"
+ "T@\"NSDictionary\",R"
+ "T@\"NSDictionary\",R,V_configDict"
+ "T@\"NSMutableDictionary\",&,V_blurs"
+ "T@\"NSMutableDictionary\",&,V_combineSpeculars"
+ "T@\"NSMutableDictionary\",&,V_effects"
+ "T@\"NSMutableDictionary\",&,V_fillColors"
+ "T@\"NSMutableDictionary\",&,V_fills"
+ "T@\"NSMutableDictionary\",&,V_opacities"
+ "T@\"NSMutableDictionary\",&,V_shadowStyles"
+ "T@\"NSMutableDictionary\",&,V_shadows"
+ "T@\"NSMutableDictionary\",&,V_speculars"
+ "T@\"NSMutableDictionary\",&,V_translucencies"
+ "T@\"NSNumber\",R,N,V_cornerRadius"
+ "T@\"NSObject<OS_xpc_object>\",&,V_sharedMemory"
+ "T@\"NSString\",C,V_emoji"
+ "T@\"NSString\",C,V_symbolName"
+ "T@\"NSString\",R,V_typeIdentifier"
+ "T@\"NSURL\",R,V_metalCacheURL"
+ "T@,R"
+ "TB,?"
+ "TB,N,V_usesExternalCompositor"
+ "TB,R,N,V_drawsLightingEffects"
+ "TB,R,V_hasLightingEffects"
+ "TB,R,V_treatLikeSymbol"
+ "TB,V_badgeWithSymbol"
+ "TB,V_disableShadow"
+ "TB,V_extrapolateIconStack"
+ "TB,V_folderEmpty"
+ "TB,V_hasBespokeBackground"
+ "TB,V_hasLightEffects"
+ "TB,V_hasText"
+ "TB,V_serializeLayerObjectForCaching"
+ "TB,V_shouldApplyMask"
+ "TB,V_treatLikeSymbol"
+ "TB,V_useLegacyCompatibilityMode"
+ "TB,V_usesExternalCompositor"
+ "TQ,R,V_iconTreatment"
+ "TQ,V_background"
+ "TQ,V_bundlePlatform"
+ "TQ,V_platformStyle"
+ "TS,R"
+ "TV App"
+ "T^{CGColor=},R,N,V_color"
+ "T^{CGImage=},R,N,V_darkImage"
+ "T^{CGImage=},R,N,V_foregroundAndLightingEffectsImage"
+ "T^{CGImage=},R,N,V_image"
+ "T^{CGImage=},R,N,V_tintableImage"
+ "T^{CGImage=},R,V_asset"
+ "Td"
+ "Tf,N,V_energyRatio"
+ "Tf,N,V_saturation"
+ "Ti,R,N,V_numberOfColors"
+ "Ti,V_layerCount"
+ "Tinted Credenza"
+ "Tinted Segmented"
+ "Tq,R,V_assetAppearance"
+ "Tq,V_appearanceVariant"
+ "Tq,V_systemTintColor"
+ "T{CGSize=dd},V_size"
+ "Unable to find asset in %@ with name i:%@. Error: %@"
+ "Unable to map platform to device class for icon stack: %lu"
+ "Unexpected appearance requested for icon stack: %lu"
+ "Unexpected appearance variant requested for icon: %lu"
+ "Unknown"
+ "Unknown appearance configuration. A:%lu, AV:%lu"
+ "Unknown appearance name to choose when dark requested"
+ "Unknown appearance name to choose when light/default assumed"
+ "Unknown appearance name to choose when tintable requested"
+ "Unknown appearance type: %@"
+ "Unknown icon. Failing back to application icon"
+ "Unknown platform for icon stack conversion"
+ "Unknown platform. Assuming embedded"
+ "Unknown platform. Assuming mac"
+ "Unknown shadow configuration"
+ "Wallet"
+ "Weather"
+ "^{CGColor=}"
+ "^{CGColor=}16@0:8"
+ "^{CGImage=}32@0:8^{CGImage=}16^@24"
+ "^{CGImage=}32@0:8^{CGImage=}16^^{CGImage}24"
+ "^{CGImage=}40@0:8{CGSize=dd}16d32"
+ "_16"
+ "_IF_UUIDWithDigestBytes:size:"
+ "_IF_arrayForKeys:"
+ "_ISWrapper_CUINamedIconLayerStack"
+ "_IS_appearanceNameFromAppearance:platform:"
+ "_IS_assetAppearance"
+ "_IS_cuiShadowStyleFromStyle:"
+ "_IS_finalizedIconWithCompositingDescriptor:"
+ "_IS_iconStackWithName:scale:locale:platform:appearance:"
+ "_IS_iconStackWithRequestedAppearance:"
+ "_IS_imageWithCompositingDescriptor:"
+ "_IS_imageWithSize:scale:platform:appearance:appearanceVariant:tintColor:isLegacy:background:"
+ "_IS_layerObjectForKey:"
+ "_IS_nameWithRequestedAppearance:"
+ "_IS_possibleIconStackExistsWithName:platform:"
+ "__METAL_CACHE__"
+ "_activeSignpostsForDescriptor:"
+ "_asset"
+ "_assetAppearance"
+ "_badgeWithSymbol"
+ "_blurs"
+ "_bottomLeftColor"
+ "_bottomRightColor"
+ "_bundlePlatform"
+ "_chicletHighlightColour"
+ "_combineSpeculars"
+ "_compositingDescriptor"
+ "_computeImageWithCGImage:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:"
+ "_computeImageWithWidth:height:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:"
+ "_computeImageWithWidth:height:strict:colorSpace:samples:foregroundMask:ucharTintable:ucharTintableOpacity:ucharSolariumTintable:ucharForeground:ucharForegroundOpacity:ucharDark:feedback:"
+ "_configDict"
+ "_cornerRadius"
+ "_createDarkFallbackIcon_iOS"
+ "_createDarkFallbackIcon_macOS"
+ "_createLightFallbackIcon_iOS"
+ "_createLightFallbackIcon_macOS"
+ "_createTintedFallbackIcon_iOS"
+ "_createTintedFallbackIcon_macOS"
+ "_darkImage"
+ "_determineRecipe"
+ "_disableShadow"
+ "_drawsLightingEffects"
+ "_emoji"
+ "_energyRatio"
+ "_externalCompositingResource"
+ "_extrapolateIconStack"
+ "_feedback"
+ "_fillColors"
+ "_fills"
+ "_folderEmpty"
+ "_foreground"
+ "_foregroundAndLightingEffectsImage"
+ "_hasBespokeBackground"
+ "_hasLightEffects"
+ "_hasLightingEffects"
+ "_hasText"
+ "_iconConfig"
+ "_iconLayers"
+ "_iconStack"
+ "_iconStackComposerForNamedImage:"
+ "_iconTreatment"
+ "_icons"
+ "_idiom"
+ "_image"
+ "_imageForMultisizeImage:size:scale:"
+ "_imageLayers"
+ "_isApp"
+ "_isAppLike"
+ "_layerCount"
+ "_layerGroups"
+ "_layeredIconResource"
+ "_layers"
+ "_lookupForSize:scale:"
+ "_metalCacheURL"
+ "_numberOfColors"
+ "_opacities"
+ "_platform:withinAllowedPlatforms:allowNative:"
+ "_platformCatalog"
+ "_platformCatalogWithName:"
+ "_prepareMaskIfNeeded"
+ "_primaryColour"
+ "_recolorForeground"
+ "_samples"
+ "_saturation"
+ "_secondaryColour"
+ "_serializeLayerObjectForCaching"
+ "_shadowStyles"
+ "_shadows"
+ "_sharedMemory"
+ "_speculars"
+ "_systemTintColor"
+ "_tagForLongLife:"
+ "_tintableImage"
+ "_topLeftColor"
+ "_topRightColor"
+ "_translucencies"
+ "_treatLikeSymbol"
+ "_tweakCopiedImageDescriptorsIfNecessary:"
+ "_typeIdentifier"
+ "_ucharMask"
+ "_useAlphaOnly"
+ "_useLegacyCompatibilityMode"
+ "_usesExternalCompositor"
+ "_wrappedResource"
+ "accessibilityinspector"
+ "activitymonitor"
+ "addLayer:"
+ "airport.utility"
+ "alarms"
+ "aliasedConfigurationDictionary"
+ "alpha"
+ "apple.directory"
+ "appstoreconnect"
+ "archive.utility"
+ "asset"
+ "assetAppearance"
+ "assetAppearanceForAppearance:appearanceVariant:"
+ "assetCatalogResourceWithURL:error:"
+ "assetsURLs"
+ "assignLayerResources"
+ "audio.midi.setup"
+ "automator"
+ "backgroundResource"
+ "badgeWithSymbol"
+ "baseStackForDescriptor:"
+ "blood.oxygen"
+ "blue"
+ "bluetooth.file.exchange"
+ "blurForAppearance:"
+ "blurs"
+ "brown"
+ "bundleIDsToNamesMap"
+ "bundlePlatform"
+ "cacheMissIconResource"
+ "cacheMissIconResourceForPlatform:"
+ "calculator"
+ "calendar.static"
+ "calendar.tue1"
+ "camera"
+ "camera.remote"
+ "carplay"
+ "categorizeShapeWithWidth:height:cornerRadius:"
+ "chess"
+ "chicletHighlightColour"
+ "classical"
+ "classifySpecular"
+ "classifySpecularWithDebug:"
+ "climate"
+ "colorString"
+ "colorWithName:designSystem:palette:colorScheme:contrast:styling:displayGamut:error:"
+ "colorsForKey:"
+ "colorsync.utility"
+ "com.apple.AccessibilityInspector"
+ "com.apple.ActivityMonitor"
+ "com.apple.ActivityMonitorApp"
+ "com.apple.AddressBook"
+ "com.apple.AppStore"
+ "com.apple.AutoSettings"
+ "com.apple.Automator"
+ "com.apple.BluetoothFileExchange"
+ "com.apple.Bridge"
+ "com.apple.CarClimate"
+ "com.apple.CarRadio"
+ "com.apple.Chess"
+ "com.apple.ColorSyncUtility"
+ "com.apple.Compressor"
+ "com.apple.Console"
+ "com.apple.Depth"
+ "com.apple.DeskCam"
+ "com.apple.Dictionary"
+ "com.apple.DigitalColorMeter"
+ "com.apple.DiskUtility"
+ "com.apple.DocumentsApp"
+ "com.apple.EraseAssistant"
+ "com.apple.FaceTime"
+ "com.apple.FileMerge"
+ "com.apple.FinalCut"
+ "com.apple.Fitness"
+ "com.apple.FontBook"
+ "com.apple.GenerativePlaygroundApp"
+ "com.apple.Health"
+ "com.apple.HeartRate"
+ "com.apple.Home"
+ "com.apple.IconComposer"
+ "com.apple.IconStudio"
+ "com.apple.Image_Capture"
+ "com.apple.Keynote"
+ "com.apple.Magnifier"
+ "com.apple.Mandrake"
+ "com.apple.Maps"
+ "com.apple.Mind"
+ "com.apple.MobileAddressBook"
+ "com.apple.MobileSMS"
+ "com.apple.Motion"
+ "com.apple.Music"
+ "com.apple.NanoAlarm"
+ "com.apple.NanoBooks"
+ "com.apple.NanoCalculator.watchkitapp"
+ "com.apple.NanoCalendar"
+ "com.apple.NanoCamera"
+ "com.apple.NanoCompass.watchkitapp"
+ "com.apple.NanoContacts"
+ "com.apple.NanoHealthBalance"
+ "com.apple.NanoHeartRhythm"
+ "com.apple.NanoHome"
+ "com.apple.NanoMail"
+ "com.apple.NanoMaps"
+ "com.apple.NanoMedications"
+ "com.apple.NanoMenstrualCycles"
+ "com.apple.NanoMusic"
+ "com.apple.NanoNotes"
+ "com.apple.NanoNowPlaying"
+ "com.apple.NanoOxygenSaturation.watchkitapp"
+ "com.apple.NanoPassbook"
+ "com.apple.NanoPhone"
+ "com.apple.NanoPhotos"
+ "com.apple.NanoReminders"
+ "com.apple.NanoRemote"
+ "com.apple.NanoSettings"
+ "com.apple.NanoSleep.watchkitapp"
+ "com.apple.NanoStopwatch"
+ "com.apple.NanoTips"
+ "com.apple.NanoTranslate"
+ "com.apple.NanoWorldClock"
+ "com.apple.Noise"
+ "com.apple.Notes"
+ "com.apple.Numbers"
+ "com.apple.Pages"
+ "com.apple.Passbook"
+ "com.apple.Passwords"
+ "com.apple.Photos"
+ "com.apple.Preferences"
+ "com.apple.Preview"
+ "com.apple.QuickTimePlayerX"
+ "com.apple.SFSymbols"
+ "com.apple.Safari"
+ "com.apple.ScreenContinuity"
+ "com.apple.ScreenSharing"
+ "com.apple.SessionTrackerApp"
+ "com.apple.Siri"
+ "com.apple.Spotlight"
+ "com.apple.Stickies"
+ "com.apple.SystemProfiler"
+ "com.apple.TV"
+ "com.apple.TVRemoteUIService"
+ "com.apple.Terminal"
+ "com.apple.TestFlight"
+ "com.apple.TextEdit"
+ "com.apple.Translate"
+ "com.apple.VisualIntelligenceCamera"
+ "com.apple.VoiceMemos"
+ "com.apple.accessibility.AccessibilityReader"
+ "com.apple.airport.airportutility"
+ "com.apple.appleseed.FeedbackAssistant"
+ "com.apple.apps.launcher"
+ "com.apple.archiveutility"
+ "com.apple.artistconnect"
+ "com.apple.audio.AudioMIDISetup"
+ "com.apple.backup.launcher"
+ "com.apple.boardwalk.watchapp"
+ "com.apple.brook.BrookUI"
+ "com.apple.calculator"
+ "com.apple.camera"
+ "com.apple.carplayapp"
+ "com.apple.clock"
+ "com.apple.compass"
+ "com.apple.demo.Calendar"
+ "com.apple.dt.Devices"
+ "com.apple.dt.Instruments"
+ "com.apple.dt.Xcode"
+ "com.apple.exposelauncher"
+ "com.apple.facetime"
+ "com.apple.finder"
+ "com.apple.findmy"
+ "com.apple.findmy.finddevices"
+ "com.apple.findmy.finditems"
+ "com.apple.findmy.findpeople"
+ "com.apple.freeform"
+ "com.apple.gamecenter"
+ "com.apple.games"
+ "com.apple.garageband10"
+ "com.apple.grapher"
+ "com.apple.iBooks"
+ "com.apple.iBooksX"
+ "com.apple.iCal"
+ "com.apple.iMovie"
+ "com.apple.iMovieApp"
+ "com.apple.iWork.Keynote"
+ "com.apple.iWork.Numbers"
+ "com.apple.iWork.Pages"
+ "com.apple.icon-package-attribute.embossable"
+ "com.apple.icon-package-attribute.optional"
+ "com.apple.icon-package-attribute.tintable"
+ "com.apple.icon-package.folder"
+ "com.apple.intercom"
+ "com.apple.iphonesimulator"
+ "com.apple.ist.AppleConnect"
+ "com.apple.ist.AppleDirectory6"
+ "com.apple.journal"
+ "com.apple.logic10"
+ "com.apple.mail"
+ "com.apple.measure"
+ "com.apple.mobilecal"
+ "com.apple.mobilemail"
+ "com.apple.mobilenotes"
+ "com.apple.mobilephone"
+ "com.apple.mobilesafari"
+ "com.apple.mobileslideshow"
+ "com.apple.mobilestore"
+ "com.apple.mobiletimer"
+ "com.apple.music.classical"
+ "com.apple.nanomusicrecognition"
+ "com.apple.nanonews"
+ "com.apple.news"
+ "com.apple.photobooth"
+ "com.apple.podcasts"
+ "com.apple.preview"
+ "com.apple.private.NanoTimer"
+ "com.apple.purplebuddy"
+ "com.apple.reminders"
+ "com.apple.rsvp"
+ "com.apple.shortcuts"
+ "com.apple.shortcuts.watch"
+ "com.apple.siri.launcher"
+ "com.apple.stocks"
+ "com.apple.stocks.watchapp"
+ "com.apple.systempreferences"
+ "com.apple.tincan"
+ "com.apple.tips"
+ "com.apple.tv"
+ "com.apple.watchmemojieditor"
+ "com.apple.weather"
+ "com.apple.weather.watchapp"
+ "com.apple.wifi.diagnostics"
+ "com.shazam.Shazam"
+ "combineSpeculars"
+ "compass"
+ "compass.watchos"
+ "compositingDescriptor"
+ "compressor"
+ "computeGrayscaleConversionColorWithWidth:height:samples:"
+ "computeMaskWithWidth:height:samples:foregroundMask:"
+ "configDict"
+ "console"
+ "contacts"
+ "cornerRadius"
+ "createDarkFallbackIcon"
+ "createDarkImageWithCGImage:feedback:"
+ "createForegroundImageWithCGImage:feedback:"
+ "createLightFallbackIcon"
+ "createSolariumTintableImageWithCGImage:feedback:"
+ "createSpecularImage"
+ "createTintableImageMaskWithCGImage:tintableOpacityImageMask:"
+ "createTintedFallbackIcon"
+ "curlResource"
+ "customRenderedTag"
+ "cyan"
+ "cycle.tracking"
+ "d24@0:8d16"
+ "d24@0:8q16"
+ "darkImage"
+ "decodeXPCObjectOfType:forKey:"
+ "depth"
+ "deskview"
+ "detectShapeInCGImage:bounds:cornerRadius:"
+ "detectShapeInImageWithWidth:height:samples:bounds:cornerRadius:"
+ "developer"
+ "developer.apple.wwdc-Release"
+ "devices"
+ "digest:size:"
+ "digitalcolormeter"
+ "disableShadow"
+ "diskutility"
+ "document/solarium/page"
+ "document/solarium/page-fold"
+ "document/solarium_ios/page"
+ "document/solarium_ios/page-fold"
+ "drawsLightingEffects"
+ "ecg"
+ "emoji"
+ "encodeXPCObject:forKey:"
+ "energyRatio"
+ "enumerateChildTypesWithBlock:"
+ "eraseassistant"
+ "externalCompositingResource"
+ "extrapolateIconStack"
+ "facetime"
+ "feature-icons"
+ "featureOverride"
+ "feedback"
+ "feedbackassistant"
+ "filemerge"
+ "files"
+ "fillColorForAppearance:"
+ "fillColors"
+ "fills"
+ "finalcut"
+ "finalizeAtSize:scale:"
+ "finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:"
+ "finder"
+ "findevices"
+ "finditems"
+ "findpeople"
+ "fitness"
+ "folderColor"
+ "folderEmpty"
+ "fontbook"
+ "foo"
+ "forceApperanceVariant"
+ "forceSymbolEmbossment"
+ "foreground"
+ "foregroundAndLightingEffectsImage"
+ "gamecenter"
+ "games"
+ "garageband"
+ "generationReport"
+ "generationReportWithCustomRenderedTag:"
+ "gradientWithSize:"
+ "grapher"
+ "gray"
+ "grayscaleConversion"
+ "green"
+ "handwashing"
+ "hasBespokeBackground"
+ "hasEffects"
+ "hasEffectsForAppearance:"
+ "hasLightEffects"
+ "hasLightingEffects"
+ "hasOverlappingChildSpecularsCombined"
+ "hasOverlappingChildSpecularsCombinedForAppearance:"
+ "hasSpecular"
+ "hasSpecularForAppearance:"
+ "hasText"
+ "hasTint"
+ "health"
+ "heart.rate"
+ "hintedSymbolFontSize"
+ "hintedTextFontSize"
+ "home"
+ "iOSCatalog"
+ "icon.composer"
+ "iconConfig"
+ "iconLayerStackWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:appearanceName:locale:"
+ "iconLayers"
+ "iconStack"
+ "iconStackAppIconsAllowed"
+ "iconStackForDescriptor:"
+ "iconStackForSize:scale:"
+ "iconStackForSize:scale:desiredAssetAppearance:returningGenerationReport:"
+ "iconStackResourcesAllowed"
+ "iconTreatment"
+ "icons"
+ "imageForCompositingDescriptor:"
+ "imageLayers"
+ "imagecapture"
+ "imageplayground"
+ "imovie"
+ "indigo"
+ "init()"
+ "initWithBundleID:"
+ "initWithBundleIdentifier:imageLayers:"
+ "initWithCGColor:"
+ "initWithCGImage:idiom:"
+ "initWithCGImage:scale:finalizedIcon:"
+ "initWithCGImage:scale:layerData:"
+ "initWithCatalog:imageName:platform:"
+ "initWithConfigurationDictionary:"
+ "initWithDarkImage:drawsLightingEffects:feedback:"
+ "initWithForeground:background:recolorForeground:"
+ "initWithFormat:"
+ "initWithIconDictionary:"
+ "initWithIconStack:"
+ "initWithIconStack:size:scale:"
+ "initWithIconTreatment:hasLightingEffects:"
+ "initWithIdiom:"
+ "initWithImage:cornerRadius:"
+ "initWithImage:foregroundAndLightingEffectsImage:feedback:"
+ "initWithImageDescriptor:"
+ "initWithLayers:"
+ "initWithLegacyAsset:assetAppearance:platform:"
+ "initWithName:"
+ "initWithNumberOfColors:"
+ "initWithResource:"
+ "initWithSpecularImage:useAlphaOnly:"
+ "initWithSymbolName:systemTintColor:"
+ "initWithSymbolName:tintColor:"
+ "initWithSystemColor:appearance:contrast:vibrancy:"
+ "initWithTintableImage:drawsLightingEffects:feedback:"
+ "initWithTopLeftColor:topRightColor:bottomRightColor:bottomLeftColor:"
+ "initWithType:iconConfiguration:"
+ "initWithTypeIdentifier:configuration:"
+ "initWithTypeIdentifier:iconLayers:"
+ "initWithTypeIdentifier:layerGroups:"
+ "inject_solarium_assets"
+ "instruments"
+ "intercom"
+ "invites"
+ "ipadhomescreen"
+ "iphonemirroring"
+ "isBadgedWithSymbol"
+ "isCompositedDocument"
+ "isEnhancedGlassEnabled"
+ "isInjectSolariumAssetsEnabled"
+ "isSolariumCornerRadiusEnabled"
+ "isSolariumEnabled"
+ "isUniversalGladeEnabled"
+ "itunesstore"
+ "journal"
+ "kISSecondaryResourceKey"
+ "kISTertiaryResourceKey"
+ "layerCount"
+ "layerGroups"
+ "layeredIconResource"
+ "layers"
+ "legacyFinalizedIconWithSize:scale:deviceClass:appearance:renderingMode:"
+ "logic"
+ "macOSCatalog"
+ "macosIconSpecification"
+ "magnifier"
+ "mail"
+ "makeSnapshot"
+ "measure"
+ "medications"
+ "memoji.watchos"
+ "messages"
+ "metalCacheURL"
+ "mindfulness"
+ "mint"
+ "missioncontrol"
+ "motion"
+ "multisizeImageAppearance:%@_requestedAppearance:%ld:"
+ "musicforartists"
+ "no_colour"
+ "noise"
+ "nowplaying"
+ "numberOfColors"
+ "numberWithUnsignedInteger:"
+ "numbers"
+ "opacities"
+ "opacity"
+ "opacityForAppearance:"
+ "orange"
+ "page fold layer"
+ "pageResource"
+ "passwords"
+ "phone"
+ "photobooth"
+ "photos"
+ "pink"
+ "platformCatalog"
+ "plistExcerpt"
+ "preview"
+ "primary content layer"
+ "primaryColour"
+ "purple"
+ "q24@0:8q16"
+ "q32@0:8q16q24"
+ "quicktimeplayer"
+ "radio"
+ "reader"
+ "recolorForeground"
+ "red"
+ "remote"
+ "renderAtSize:scale:"
+ "renderCGImageAtSize:scale:"
+ "renderedFullBleedIconWithConfiguration:"
+ "renderedIconWithConfiguration:"
+ "renderedLegacyCompatibleIconWithConfiguration:forDeviceClass:maskToIconShape:"
+ "renderedSystemGlassCompatibleIconWithConfiguration:"
+ "resolvedTintColorForAppearance:"
+ "safari"
+ "saturation"
+ "screen.sharing"
+ "secondary resource layer"
+ "secondaryColour"
+ "segmentationIdiom"
+ "serializeLayerObjectForCaching"
+ "serializedDataWithError:"
+ "setBackgroundResource:"
+ "setBadgeWithSymbol:"
+ "setBlur:forAppearance:"
+ "setBlurStrength:"
+ "setBlurs:"
+ "setBundlePlatform:"
+ "setCGColor:"
+ "setChicletHighlightColour:"
+ "setColors:andStops:"
+ "setCombineSpeculars:"
+ "setCompositingDescriptor:"
+ "setDisableShadow:"
+ "setEmoji:"
+ "setEnergyRatio:"
+ "setExtrapolateIconStack:"
+ "setFillColor:forAppearance:"
+ "setFillColors:"
+ "setFills:"
+ "setFolderEmpty:"
+ "setGathersSpecularByElement:"
+ "setGenerationReport:"
+ "setGradientEndPoint:"
+ "setGradientStartPoint:"
+ "setGradientType:"
+ "setHasBespokeBackground:"
+ "setHasEffects:"
+ "setHasEffects:forAppearance:"
+ "setHasLightEffects:"
+ "setHasLightingEffects:"
+ "setHasOverlappingChildSpecularsCombined:"
+ "setHasOverlappingChildSpecularsCombined:forAppearance:"
+ "setHasSpecular:"
+ "setHasSpecular:forAppearance:"
+ "setHasText:"
+ "setIconConfig:"
+ "setIconStack:"
+ "setIcons:"
+ "setImage:"
+ "setLayerCount:"
+ "setLayerGroups:"
+ "setLayeredIconResource:"
+ "setLayers:"
+ "setOpacities:"
+ "setOpacity:"
+ "setOpacity:forAppearance:"
+ "setPlatformCatalog:"
+ "setPrimaryColour:"
+ "setSaturation:"
+ "setSecondaryColour:"
+ "setSerializeLayerObjectForCaching:"
+ "setShadow:"
+ "setShadow:forAppearance:"
+ "setShadowOpacity:"
+ "setShadowStyle:"
+ "setShadowStyle:forAppearance:"
+ "setShadowStyles:"
+ "setShadows:"
+ "setSharedMemory:"
+ "setSpeculars:"
+ "setSvgDocumentURL:"
+ "setSystemTintColor:"
+ "setTextResource:"
+ "setTranslucencies:"
+ "setTranslucency:"
+ "setTranslucency:forAppearance:"
+ "setTreatLikeSymbol:"
+ "setUseLegacyCompatibilityMode:"
+ "setUsesExternalCompositor:"
+ "setWithObjects:"
+ "settings"
+ "setupassistant"
+ "sfsymbols"
+ "shadowForAppearance:"
+ "shadowStyle"
+ "shadowStyleForAppearance:"
+ "shadowStyles"
+ "shadows"
+ "sharedMemory"
+ "shazam"
+ "shortcuts"
+ "shouldUseFolderRecipe:"
+ "simulator"
+ "siren"
+ "siri.appleintelligence"
+ "sleep"
+ "speculars"
+ "spotlight"
+ "standardCornerRadiusForSize:"
+ "stickies"
+ "stopwatch"
+ "suppliedBackground layer"
+ "supportsRequestingIconStacksForPlatform:"
+ "svg"
+ "system.information"
+ "systemTintColor"
+ "teal"
+ "terminal"
+ "tertiary resource layer"
+ "test"
+ "testflight"
+ "textResource"
+ "textedit"
+ "tides"
+ "timemachine"
+ "timers"
+ "tintWithRed:green:blue:alpha:"
+ "tintableImage"
+ "tips"
+ "translate"
+ "translucencies"
+ "translucency"
+ "translucencyForAppearance:"
+ "treatLikeSymbol"
+ "universal_glade"
+ "updateWithImageDescriptor:"
+ "useLegacyCompatibilityMode"
+ "usesExternalCompositor"
+ "v24@0:8^{CGImage=}16"
+ "v28@0:8B16q20"
+ "v32@0:8@16q24"
+ "v32@0:8d16q24"
+ "v32@0:8q16q24"
+ "vehicle"
+ "visualintelligence"
+ "vitals"
+ "voicememos"
+ "walkie.talkie"
+ "watch.companion"
+ "watchOSCatalog"
+ "wirelessdiagnostics"
+ "workout"
+ "world.clock"
+ "wrappedResource"
+ "xcode"
+ "yellow"
+ "{?=\"width\"i\"height\"i\"padding\"i\"alphaInfo\"I\"ucharSamples\"^}"
+ "{?=\"width\"i\"height\"i\"padding\"i\"usesUchar4LastComponent\"B\"\"(?=\"uchar4Array\"^\"ucharArray\"*)}"
- "%.0f:%ld:%@:%lu:%@:%@:%@:%@:%@"
- "%@ - (%0.2f, %0.2f)@%.0fx v:%lx l:%lu a:%@ t:%@ b:%@ s:%@ ps:%@ digest: %@"
- "%@ Bundle URL: %@ type: %@ tag: %@ tag class: %@ digest:%@"
- "%@ BundleID: %@ digest: %@"
- "%@ RETURNING App PLACEHOLDER: %@"
- "%@ RETURNING AppClip PLACEHOLDER: %@"
- "%@ RETURNING_PLACEHOLDER: %@"
- "%@ RETURNING_STALE_PLACEHOLDER: %@"
- "%@ Tag: %@, Class: %@, Base type: %@"
- "%@ icon: %@ decorations: %@"
- "%@ identity: %@ digest: %@"
- "%@,Type: %@"
- "%ld"
- "%ld:%ld:%ld:%ld"
- "(%@)"
- "02:09:54"
- "32@0:8i16i20r^24"
- "@\"<CAAction>\"32@0:8@\"CALayer\"16@\"NSString\"24"
- "@48@0:8@16@24@32Q40"
- "@48@0:8d16d24Q32q40"
- "@56@0:8@16@24@32Q40^@48"
- "B32@0:8i16i20^24"
- "B48@0:8^{CGImage=}16*24^32^@40"
- "B56@0:8i16i20^24*32^40^@48"
- "B60@0:8i16i20B24^28*36^44@52"
- "CALayerDelegate"
- "DELAYING_PREPARE: %@ - delay: %lf , %@"
- "Found catalog image with query info name:%@ scaleFactor:%f deviceIdiom:%d deviceSubtype:%d displayGamut:%d layoutDirection:%d desiredSize:%f,%f appearanceName:%@]"
- "IGNORING_CACHE: %@ - %@"
- "ISA_GENERATEING_IMAGE for %@ : %@"
- "ISDebugGraphicIcons"
- "ISIcon: %@, descriptor: %@, func: %s, Digest=%{signpost.telemetry:string1}@, NumDescriptors=%{signpost.telemetry:number1}lu enableTelemetry=YES "
- "Icon layer update queue"
- "Icon: %@, Alias: %@"
- "IconSegmentationBackgroundStyleContinuousGradient"
- "IconSegmentationBackgroundStyleKey"
- "IconSegmentationBackgroundStyleSingleColor"
- "IconSegmentationForegroundNumberOfColorsKey"
- "IconSegmentationForegroundStyleContinuousGradient"
- "IconSegmentationForegroundStyleKey"
- "IconSegmentationForegroundStyleMultipleColors"
- "IconSegmentationForegroundStyleSingleColor"
- "PREPARE_IGNORING_CACHE: %@ - %@"
- "PREPARE_IMAGE: %@ - %@"
- "STORE_LOOKUP: %@ - %@"
- "Symbols"
- "T@\"ISIcon\",&,N,V_icon"
- "TB,N,V_drawBorder"
- "TB,N,V_shouldApplyMask"
- "TQ,N,V_iconShape"
- "Unable to find asset in %@ with name i:%@ s:%@. Error: %@"
- "Unable to find icon image named: %@ for size: (%f,%f) scale:(%lf). Looking for resources matching the iconset naming convention."
- "Unable to find resources matching the iconset naming convention with base name: %@ for size: (%f,%f) scale:(%lf). Looking for a symbol."
- "Updateing layer for icon: %@"
- "_IS_appearanceNameFromAppearance:"
- "_alphaInfo"
- "_computeImageWithCGImage:ucharTintable:ucharDark:feedback:"
- "_computeImageWithWidth:height:strict:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:"
- "_computeImageWithWidth:height:ucharSamplesAndForegroundMask:ucharTintable:ucharDark:feedback:"
- "_drawBorder"
- "_eventPrepareISIconSignpost:message:"
- "_iconShape"
- "_shape"
- "_ucharSamples"
- "actionForLayer:forKey:"
- "assetCatalogResourceWithURL:imageName:symbolName:platform:error:"
- "assetCatalogResourceWithURL:symbolName:error:"
- "catalogAppearance"
- "computeGrayscaleConversionColorWithWidth:height:ucharSamples:"
- "computeMaskWithWidth:height:ucharSamplesAndMask:"
- "contentsScale"
- "coreGlyphsCatalog"
- "createTintableImageWithCGImage:"
- "debugGraphicIconColor"
- "debugISIconGraphicIconColor"
- "debugPreDefinedGraphicIconColor"
- "displayLayer:"
- "drawLayer:inContext:"
- "iconShape"
- "initWithCatalog:imageName:symbolName:platform:"
- "initWithIcon:"
- "initWithNamedVectorGlyph:"
- "isDebugGraphicIconColourEnabled"
- "isDocumentBadge"
- "layerUpdateQueue"
- "layerWillDraw:"
- "layoutSublayersOfLayer:"
- "namedVectorGlyphWithName:scaleFactor:deviceIdiom:layoutDirection:glyphSize:glyphWeight:glyphPointSize:appearanceName:"
- "preferredFrameSize"
- "r^"
- "rasterizeImageUsingScaleFactor:forTargetSize:"
- "setContents:"
- "setDebugColourSet:"
- "setDelegate:"
- "setIconShape:"
- "setNeedsDisplay"
- "stringWithUTF8String:"
- "symbolImageForFontSize:scale:symbolSize:symbolWeight:"
- "symbolImageForSize:scale:"
- "v24@0:8@\"CALayer\"16"
- "v32@0:8@\"CALayer\"16^{CGContext=}24"
- "v32@0:8@16^{CGContext=}24"

```
