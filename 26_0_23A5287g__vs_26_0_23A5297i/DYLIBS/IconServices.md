## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-714.101.0.0.0
-  __TEXT.__text: 0x5fa58
-  __TEXT.__auth_stubs: 0xf50
+719.1.0.0.0
+  __TEXT.__text: 0x61478
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x648c
-  __TEXT.__const: 0x493a
+  __TEXT.__objc_methlist: 0x6464
+  __TEXT.__const: 0x87c2
   __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x5202
-  __TEXT.__oslogstring: 0x3037
+  __TEXT.__cstring: 0x3c99
+  __TEXT.__oslogstring: 0x307b
   __TEXT.__unwind_info: 0x1788
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1224
-  __TEXT.__objc_methname: 0xbea6
-  __TEXT.__objc_methtype: 0x1775
-  __TEXT.__objc_stubs: 0x9560
-  __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0x520
+  __TEXT.__objc_classname: 0x11fc
+  __TEXT.__objc_methname: 0xbe23
+  __TEXT.__objc_methtype: 0x17dc
+  __TEXT.__objc_stubs: 0x9520
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fe8
+  __DATA_CONST.__objc_selrefs: 0x2fa0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0xc50
-  __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0xf60
-  __AUTH_CONST.__cfstring: 0x6880
-  __AUTH_CONST.__objc_const: 0x13200
+  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__const: 0x1168
+  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__objc_const: 0x132f0
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0xaf0
   __DATA.__objc_ivar: 0x694
   __DATA.__data: 0x1c88
-  __DATA.__bss: 0x5c8
-  __DATA_DIRTY.__objc_data: 0x2850
+  __DATA.__bss: 0x648
+  __DATA_DIRTY.__objc_data: 0x2800
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 40C74EE7-CE30-3635-AC35-6A19B2325327
-  Functions: 2440
-  Symbols:   9209
-  CStrings:  4766
+  UUID: 4905DDB1-1036-3D03-95AC-CF8BE1CB5804
+  Functions: 2476
+  Symbols:   9303
+  CStrings:  4100
 
Symbols:
+ +[ISRecipeInfo appRecipeForPlatform:descriptor:preferRichRecipe:]
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:preferRichRecipe:]
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:preferRichRecipe:].cold.1
+ -[ISCompositingDescriptor assetPlatformHint]
+ -[ISCompositingDescriptor assetPlatform]
+ -[ISCompositingDescriptor description]
+ -[ISCompositingDescriptor encapsulationShape]
+ -[ISCompositingDescriptor languageDirection]
+ -[ISCompositingDescriptor setAssetPlatformHint:]
+ -[ISCompositingDescriptor setLanguageDirection:]
+ -[ISCompositingDescriptor setShape:]
+ -[ISCompositingDescriptor shape]
+ -[ISDocumentRecipe hintedBadgeRect].cold.1
+ -[ISDocumentRecipe hintedBadgeRect].cold.2
+ -[ISDocumentRecipe hintedBadgeRect].cold.3
+ -[ISDocumentRecipe hintedBadgeRect].cold.4
+ -[ISDocumentRecipe hintedPaperRect].cold.1
+ -[ISDocumentRecipe hintedPaperRect].cold.2
+ -[ISDocumentRecipe hintedSymbolFontSize].cold.1
+ -[ISDocumentRecipe hintedSymbolFontSize].cold.2
+ -[ISDocumentRecipe hintedSymbolFontSize].cold.3
+ -[ISDocumentRecipe hintedSymbolFontSize].cold.4
+ -[ISDocumentRecipe hintedTextFontSize].cold.1
+ -[ISDocumentRecipe hintedTextFontSize].cold.2
+ -[ISDocumentRecipe hintedTextRect].cold.1
+ -[ISDocumentRecipe hintedTextRect].cold.2
+ -[ISFolderIconConfiguration assetCatalogImageName]
+ -[ISFolderIconConfiguration setAssetCatalogImageName:]
+ -[ISFolderIconConfigurationParser assetCatalogImageName]
+ -[ISIconStackAssetCatalogResource generationReport]
+ -[ISIconStackAssetCatalogResource languageDirection]
+ -[ISIconStackAssetCatalogResource platformStyle]
+ -[ISIconStackAssetCatalogResource setGenerationReport:]
+ -[ISIconStackAssetCatalogResource setLanguageDirection:]
+ -[ISIconStackAssetCatalogResource setPlatformStyle:]
+ -[ISIconStackAssetCatalogResource setShape:]
+ -[ISIconStackAssetCatalogResource shape]
+ -[ISIconStackCompositeResource generationReport]
+ -[ISIconStackCompositeResource setGenerationReport:]
+ -[ISImageDescriptor assetPlatformHint]
+ -[ISImageDescriptor setAssetPlatformHint:]
+ -[ISImageDescriptor(CompositorRecipe) _recipePreferRichRecipe:]
+ -[ISRecipeFactory preferRichRecipe]
+ _ISAccelerateIconComputeMask_foregroundSingleColor_backgroundContinuousGradient
+ _ISAccelerateIconSegmentationComputeMask
+ _ISAccelerateIconSegmentationFlagForConnectedBackground
+ _ISAccelerateIconSegmentationFlagForConnectedBackgroundHelper
+ _ISAccelerateIconSegmentationSamples_readAlmostOpaqueSample_i_AlphaLast_NoOpacity_Padding0
+ _ISAccelerateIconSegmentationSamples_readAlmostOpaqueSample_i_NoOpacity
+ _OBJC_CLASS_$_CUIEncapsulationShape
+ _OBJC_IVAR_$_ISCompositingDescriptor._assetPlatformHint
+ _OBJC_IVAR_$_ISCompositingDescriptor._languageDirection
+ _OBJC_IVAR_$_ISCompositingDescriptor._shape
+ _OBJC_IVAR_$_ISFolderIconConfiguration._assetCatalogImageName
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._languageDirection
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._platformStyle
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource._shape
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource.generationReport
+ _OBJC_IVAR_$_ISIconStackCompositeResource.generationReport
+ _OBJC_IVAR_$_ISImageDescriptor._assetPlatformHint
+ __ISInvalidateCacheEntries
+ ___34-[ISDocumentRecipe hintedTextRect]_block_invoke_2
+ ___35-[ISDocumentRecipe hintedBadgeRect]_block_invoke_2
+ ___35-[ISDocumentRecipe hintedBadgeRect]_block_invoke_3
+ ___35-[ISDocumentRecipe hintedBadgeRect]_block_invoke_4
+ ___35-[ISDocumentRecipe hintedPaperRect]_block_invoke_2
+ ___38-[ISDocumentRecipe hintedTextFontSize]_block_invoke_2
+ ___40-[ISDocumentRecipe hintedSymbolFontSize]_block_invoke_2
+ ___40-[ISDocumentRecipe hintedSymbolFontSize]_block_invoke_3
+ ___40-[ISDocumentRecipe hintedSymbolFontSize]_block_invoke_4
+ ____ISInvalidateCacheEntries_block_invoke
+ ____ISInvalidateCacheEntries_block_invoke.7
+ ____ISInvalidateCacheEntries_block_invoke.7.cold.1
+ ____ISInvalidateCacheEntries_block_invoke.cold.1
+ ___block_literal_global.104
+ ___block_literal_global.112
+ ___block_literal_global.116
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.128
+ ___block_literal_global.132
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.144
+ ___block_literal_global.148
+ ___block_literal_global.152
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.241
+ ___block_literal_global.245
+ ___block_literal_global.249
+ ___block_literal_global.253
+ ___block_literal_global.257
+ ___block_literal_global.261
+ ___block_literal_global.265
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.36
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.383
+ ___block_literal_global.387
+ ___block_literal_global.391
+ ___block_literal_global.395
+ ___block_literal_global.399
+ ___block_literal_global.403
+ ___block_literal_global.407
+ ___block_literal_global.411
+ ___block_literal_global.6
+ _chi2cdf3_values
+ _computeMask_Default
+ _computeMask_ucharDark
+ _computeMask_ucharForeground
+ _computeMask_ucharForegroundOpacity
+ _computeMask_ucharSolariumTintable
+ _computeMask_ucharTintable
+ _computeMask_ucharTintableOpacity
+ _hintedBadgeRect.onceToken.110
+ _hintedBadgeRect.onceToken.114
+ _hintedBadgeRect.onceToken.118
+ _hintedBadgeRect.onceToken.122
+ _hintedBadgeRect.onceToken.243
+ _hintedBadgeRect.onceToken.385
+ _hintedBadgeRect.rect.109
+ _hintedBadgeRect.rect.113
+ _hintedBadgeRect.rect.117
+ _hintedBadgeRect.rect.121
+ _hintedBadgeRect.rect.242
+ _hintedBadgeRect.rect.384
+ _hintedCornerSize.onceToken.362
+ _hintedCornerSize.onceToken.393
+ _hintedCornerSize.size.361
+ _hintedCornerSize.size.392
+ _hintedFontSize.onceToken.251
+ _hintedFontSize.onceToken.401
+ _hintedFontSize.value.250
+ _hintedFontSize.value.400
+ _hintedPageCurlSize.onceToken.358
+ _hintedPageCurlSize.onceToken.389
+ _hintedPageCurlSize.size.357
+ _hintedPageCurlSize.size.388
+ _hintedPaperRect.onceToken.106
+ _hintedPaperRect.onceToken.235
+ _hintedPaperRect.onceToken.352
+ _hintedPaperRect.onceToken.381
+ _hintedPaperRect.rect.105
+ _hintedPaperRect.rect.234
+ _hintedPaperRect.rect.351
+ _hintedPaperRect.rect.380
+ _hintedShadowBlur.onceToken.255
+ _hintedShadowBlur.onceToken.366
+ _hintedShadowBlur.onceToken.405
+ _hintedShadowBlur.value.254
+ _hintedShadowBlur.value.365
+ _hintedShadowBlur.value.404
+ _hintedShadowOffset.onceToken.259
+ _hintedShadowOffset.onceToken.370
+ _hintedShadowOffset.onceToken.409
+ _hintedShadowOffset.value.258
+ _hintedShadowOffset.value.369
+ _hintedShadowOffset.value.408
+ _hintedShadowSpread.onceToken.263
+ _hintedShadowSpread.value.262
+ _hintedSymbolFontSize.onceToken.142
+ _hintedSymbolFontSize.onceToken.146
+ _hintedSymbolFontSize.onceToken.150
+ _hintedSymbolFontSize.value.141
+ _hintedSymbolFontSize.value.145
+ _hintedSymbolFontSize.value.149
+ _hintedTextFontSize.onceToken.136
+ _hintedTextFontSize.value.135
+ _hintedTextRect.onceToken.126
+ _hintedTextRect.onceToken.130
+ _hintedTextRect.onceToken.247
+ _hintedTextRect.onceToken.397
+ _hintedTextRect.rect.125
+ _hintedTextRect.rect.129
+ _hintedTextRect.rect.246
+ _hintedTextRect.rect.396
+ _kISAssetCatalogImageName
+ _memset
+ _objc_msgSend$_recipePreferRichRecipe:
+ _objc_msgSend$appRecipeForPlatform:descriptor:preferRichRecipe:
+ _objc_msgSend$appRecipeForPlatformStyle:descriptor:resourcePlatform:preferRichRecipe:
+ _objc_msgSend$assetCatalogImageName
+ _objc_msgSend$assetPlatform
+ _objc_msgSend$assetPlatformHint
+ _objc_msgSend$clearAllCachedItemsWithReply:
+ _objc_msgSend$encapsulationShape
+ _objc_msgSend$finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:layoutDirection:isLegacyContent:
+ _objc_msgSend$newCircle
+ _objc_msgSend$newRoundedRect
+ _objc_msgSend$preferRichRecipe
+ _objc_msgSend$setAssetPlatformHint:
+ _objc_msgSend$setEncapsulationShape:
+ _readAlmostOpaqueSample_i_AlphaLast
+ _readAlmostOpaqueSample_i_AlphaNoneSkipLast
+ _readAlmostOpaqueSample_i_AlphaPremultipliedLast
+ _readAlmostOpaqueSample_i_Default
+ _readSample
- +[ISRecipeInfo appRecipeForPlatform:descriptor:]
- +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:]
- +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:resourcePlatform:].cold.1
- +[ISStaticIconStackAssetCatalogResource _platformCatalogWithName:]
- +[ISStaticIconStackAssetCatalogResource _platformCatalogWithName:].cold.1
- +[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap]
- +[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap].cold.1
- +[ISStaticIconStackAssetCatalogResource iOSCatalog]
- +[ISStaticIconStackAssetCatalogResource macOSCatalog]
- +[ISStaticIconStackAssetCatalogResource watchOSCatalog]
- -[ISDefaults isInjectSolariumAssetsEnabled]
- -[ISIconStackComposer imageForCompositingDescriptor:]
- -[ISIconStackComposer imageForCompositingDescriptor:].cold.1
- -[ISStaticIconStackAssetCatalogResource .cxx_destruct]
- -[ISStaticIconStackAssetCatalogResource assetsURLs]
- -[ISStaticIconStackAssetCatalogResource chicletHighlightColour]
- -[ISStaticIconStackAssetCatalogResource compositingDescriptor]
- -[ISStaticIconStackAssetCatalogResource iconStack]
- -[ISStaticIconStackAssetCatalogResource imageForSize:scale:]
- -[ISStaticIconStackAssetCatalogResource initWithBundleID:]
- -[ISStaticIconStackAssetCatalogResource layerCount]
- -[ISStaticIconStackAssetCatalogResource name]
- -[ISStaticIconStackAssetCatalogResource platformCatalog]
- -[ISStaticIconStackAssetCatalogResource primaryColour]
- -[ISStaticIconStackAssetCatalogResource scale]
- -[ISStaticIconStackAssetCatalogResource secondaryColour]
- -[ISStaticIconStackAssetCatalogResource setChicletHighlightColour:]
- -[ISStaticIconStackAssetCatalogResource setCompositingDescriptor:]
- -[ISStaticIconStackAssetCatalogResource setIconStack:]
- -[ISStaticIconStackAssetCatalogResource setLayerCount:]
- -[ISStaticIconStackAssetCatalogResource setName:]
- -[ISStaticIconStackAssetCatalogResource setPlatformCatalog:]
- -[ISStaticIconStackAssetCatalogResource setPrimaryColour:]
- -[ISStaticIconStackAssetCatalogResource setScale:]
- -[ISStaticIconStackAssetCatalogResource setSecondaryColour:]
- -[ISStaticIconStackAssetCatalogResource setUsesExternalCompositor:]
- -[ISStaticIconStackAssetCatalogResource usesExternalCompositor]
- _OBJC_CLASS_$_CUIMutableNamedLayerVectorSVGImage
- _OBJC_CLASS_$_ISStaticIconStackAssetCatalogResource
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._chicletHighlightColour
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._compositingDescriptor
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._iconStack
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._layerCount
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._name
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._platformCatalog
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._primaryColour
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._scale
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._secondaryColour
- _OBJC_IVAR_$_ISStaticIconStackAssetCatalogResource._usesExternalCompositor
- _OBJC_METACLASS_$_ISStaticIconStackAssetCatalogResource
- __OBJC_$_CLASS_METHODS_ISStaticIconStackAssetCatalogResource
- __OBJC_$_INSTANCE_METHODS_ISStaticIconStackAssetCatalogResource
- __OBJC_$_INSTANCE_VARIABLES_ISStaticIconStackAssetCatalogResource
- __OBJC_$_PROP_LIST_ISStaticIconStackAssetCatalogResource
- __OBJC_CLASS_RO_$_ISStaticIconStackAssetCatalogResource
- __OBJC_METACLASS_RO_$_ISStaticIconStackAssetCatalogResource
- ___60+[ISStaticIconStackAssetCatalogResource bundleIDsToNamesMap]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.110
- ___block_literal_global.113
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.199
- ___block_literal_global.203
- ___block_literal_global.207
- ___block_literal_global.211
- ___block_literal_global.215
- ___block_literal_global.219
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.30
- ___block_literal_global.314
- ___block_literal_global.318
- ___block_literal_global.322
- ___block_literal_global.326
- ___block_literal_global.337
- ___block_literal_global.341
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.361
- ___block_literal_global.365
- _bundleIDsToNamesMap.bundleIDsToNamesMap
- _bundleIDsToNamesMap.onceToken
- _computeIconSegmentationFlagForConnectedBackground
- _computeMask_foregroundSingleColor_backgroundContinuousGradient
- _hintedBadgeRect.onceToken.104
- _hintedBadgeRect.onceToken.197
- _hintedBadgeRect.onceToken.339
- _hintedBadgeRect.rect.103
- _hintedBadgeRect.rect.196
- _hintedBadgeRect.rect.338
- _hintedCornerSize.onceToken.316
- _hintedCornerSize.onceToken.347
- _hintedCornerSize.size.315
- _hintedCornerSize.size.346
- _hintedFontSize.onceToken.205
- _hintedFontSize.onceToken.355
- _hintedFontSize.value.204
- _hintedFontSize.value.354
- _hintedPageCurlSize.onceToken.312
- _hintedPageCurlSize.onceToken.343
- _hintedPageCurlSize.size.311
- _hintedPageCurlSize.size.342
- _hintedPaperRect.onceToken.189
- _hintedPaperRect.onceToken.306
- _hintedPaperRect.onceToken.335
- _hintedPaperRect.rect.188
- _hintedPaperRect.rect.305
- _hintedPaperRect.rect.334
- _hintedShadowBlur.onceToken.209
- _hintedShadowBlur.onceToken.320
- _hintedShadowBlur.onceToken.359
- _hintedShadowBlur.value.208
- _hintedShadowBlur.value.319
- _hintedShadowBlur.value.358
- _hintedShadowOffset.onceToken.213
- _hintedShadowOffset.onceToken.324
- _hintedShadowOffset.onceToken.363
- _hintedShadowOffset.value.212
- _hintedShadowOffset.value.323
- _hintedShadowOffset.value.362
- _hintedShadowSpread.onceToken.217
- _hintedShadowSpread.value.216
- _hintedTextRect.onceToken.106
- _hintedTextRect.onceToken.201
- _hintedTextRect.onceToken.351
- _hintedTextRect.rect.105
- _hintedTextRect.rect.200
- _hintedTextRect.rect.350
- _objc_msgSend$_platformCatalogWithName:
- _objc_msgSend$appRecipeForPlatform:descriptor:
- _objc_msgSend$appRecipeForPlatformStyle:descriptor:resourcePlatform:
- _objc_msgSend$assetsURLs
- _objc_msgSend$bundleIDsToNamesMap
- _objc_msgSend$iOSCatalog
- _objc_msgSend$iconStack
- _objc_msgSend$initWithBundleID:
- _objc_msgSend$initWithResource:
- _objc_msgSend$isInjectSolariumAssetsEnabled
- _objc_msgSend$layerCount
- _objc_msgSend$macOSCatalog
- _objc_msgSend$platformCatalog
- _objc_msgSend$primaryColour
- _objc_msgSend$setSvgDocumentURL:
- _objc_msgSend$watchOSCatalog
CStrings:
+ "%@, Symbol: %@, Emoji: %@, Tint: %ld - %@, Image: %@, Empty: %d"
+ "19:31:56"
+ "<ISCompositingDescriptor: %p> (%0.2f, %0.2f)@%.0fx a:%ld:..:%ld t:%g:%g:%g:%g ps:%ld b:%ld p:%ld mask:%d legCap:%d ld:%ld shape:%ld "
+ "@\"ISGenerationReport\""
+ "@\"ISGenerationReport\"16@0:8"
+ "@36@0:8Q16@24B32"
+ "@44@0:8Q16@24Q32B40"
+ "Center Content Emboss"
+ "Clear entire cache started."
+ "Couldn't find image resource %@ for %@: %@"
+ "Error clearing entire icon cache: %@"
+ "Error fetching remote object while clearing entire icon cache: %@"
+ "ISAssetCatalogImageName"
+ "T@\"ISGenerationReport\",&,VgenerationReport"
+ "T@\"NSString\",&,V_assetCatalogImageName"
+ "TQ,N,V_assetPlatformHint"
+ "TQ,N,V_languageDirection"
+ "TQ,N,V_shape"
+ "TQ,V_assetPlatformHint"
+ "_assetCatalogImageName"
+ "_assetPlatformHint"
+ "_recipePreferRichRecipe:"
+ "_shape"
+ "appRecipeForPlatform:descriptor:preferRichRecipe:"
+ "appRecipeForPlatformStyle:descriptor:resourcePlatform:preferRichRecipe:"
+ "assetCatalogImageName"
+ "assetPlatform"
+ "assetPlatformHint"
+ "clearAllCachedItemsWithReply:"
+ "encapsulationShape"
+ "finalizedIconWithSize:scale:deviceClass:appearance:renderingMode:layoutDirection:isLegacyContent:"
+ "newCircle"
+ "newRoundedRect"
+ "preferRichRecipe"
+ "setAssetCatalogImageName:"
+ "setAssetPlatformHint:"
+ "setEncapsulationShape:"
+ "v24@0:8@\"ISGenerationReport\"16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
- "%@, Symbol: %@, Emoji: %@, Tint: %ld - %@, Empty: %d"
- "%@_Layer%d"
- "%d"
- "'"
- "21:02:54"
- "@\"CUINamedIconLayerStack\""
- "@40@0:8Q16@24Q32"
- "App Store"
- "Books"
- "Failed to generate image from composed icon stack"
- "Failed to utilize overrides asset catalog %@. Error: %@"
- "Find My"
- "Freeform"
- "ISStaticIconStackAssetCatalogResource"
- "Keynote"
- "Maps"
- "Music"
- "News"
- "Notes"
- "OverrideAssets_ios"
- "OverrideAssets_macos"
- "OverrideAssets_watchos"
- "Pages"
- "Podcasts"
- "Reminders"
- "Stocks"
- "T@\"CUICatalog\",&,N,V_platformCatalog"
- "T@\"CUINamedIconLayerStack\",&,N,V_iconStack"
- "T@\"IFColor\",&,V_chicletHighlightColour"
- "T@\"IFColor\",&,V_primaryColour"
- "T@\"IFColor\",&,V_secondaryColour"
- "TB,N,V_usesExternalCompositor"
- "TV App"
- "Ti,V_layerCount"
- "Wallet"
- "Weather"
- "_chicletHighlightColour"
- "_iconStack"
- "_layerCount"
- "_platformCatalog"
- "_platformCatalogWithName:"
- "_primaryColour"
- "_secondaryColour"
- "accessibilityinspector"
- "activitymonitor"
- "airport.utility"
- "alarms"
- "appRecipeForPlatform:descriptor:"
- "appRecipeForPlatformStyle:descriptor:resourcePlatform:"
- "apple.directory"
- "appstoreconnect"
- "archive.utility"
- "assetsURLs"
- "audio.midi.setup"
- "automator"
- "blood.oxygen"
- "bluetooth.file.exchange"
- "bundleIDsToNamesMap"
- "calculator"
- "calendar.static"
- "calendar.tue1"
- "camera"
- "camera.remote"
- "carplay"
- "chess"
- "chicletHighlightColour"
- "classical"
- "climate"
- "colorsync.utility"
- "com.apple.AccessibilityInspector"
- "com.apple.ActivityMonitor"
- "com.apple.ActivityMonitorApp"
- "com.apple.AddressBook"
- "com.apple.AppStore"
- "com.apple.AutoSettings"
- "com.apple.Automator"
- "com.apple.BluetoothFileExchange"
- "com.apple.Bridge"
- "com.apple.CarClimate"
- "com.apple.CarRadio"
- "com.apple.Chess"
- "com.apple.ColorSyncUtility"
- "com.apple.Compressor"
- "com.apple.Console"
- "com.apple.Depth"
- "com.apple.DeskCam"
- "com.apple.Dictionary"
- "com.apple.DigitalColorMeter"
- "com.apple.DiskUtility"
- "com.apple.DocumentsApp"
- "com.apple.EraseAssistant"
- "com.apple.FaceTime"
- "com.apple.FileMerge"
- "com.apple.FinalCut"
- "com.apple.Fitness"
- "com.apple.FontBook"
- "com.apple.GenerativePlaygroundApp"
- "com.apple.Health"
- "com.apple.HeartRate"
- "com.apple.Home"
- "com.apple.IconComposer"
- "com.apple.IconStudio"
- "com.apple.Image_Capture"
- "com.apple.Keynote"
- "com.apple.Magnifier"
- "com.apple.Mandrake"
- "com.apple.Maps"
- "com.apple.Mind"
- "com.apple.MobileAddressBook"
- "com.apple.MobileSMS"
- "com.apple.Motion"
- "com.apple.Music"
- "com.apple.NanoAlarm"
- "com.apple.NanoBooks"
- "com.apple.NanoCalculator.watchkitapp"
- "com.apple.NanoCalendar"
- "com.apple.NanoCamera"
- "com.apple.NanoCompass.watchkitapp"
- "com.apple.NanoContacts"
- "com.apple.NanoHealthBalance"
- "com.apple.NanoHeartRhythm"
- "com.apple.NanoHome"
- "com.apple.NanoMail"
- "com.apple.NanoMaps"
- "com.apple.NanoMedications"
- "com.apple.NanoMenstrualCycles"
- "com.apple.NanoMusic"
- "com.apple.NanoNotes"
- "com.apple.NanoNowPlaying"
- "com.apple.NanoOxygenSaturation.watchkitapp"
- "com.apple.NanoPassbook"
- "com.apple.NanoPhone"
- "com.apple.NanoPhotos"
- "com.apple.NanoReminders"
- "com.apple.NanoRemote"
- "com.apple.NanoSettings"
- "com.apple.NanoSleep.watchkitapp"
- "com.apple.NanoStopwatch"
- "com.apple.NanoTips"
- "com.apple.NanoTranslate"
- "com.apple.NanoWorldClock"
- "com.apple.Noise"
- "com.apple.Notes"
- "com.apple.Numbers"
- "com.apple.Pages"
- "com.apple.Passbook"
- "com.apple.Passwords"
- "com.apple.PhotoBooth"
- "com.apple.Photos"
- "com.apple.Preferences"
- "com.apple.Preview"
- "com.apple.QuickTimePlayerX"
- "com.apple.SFSymbols"
- "com.apple.SOSBuddy"
- "com.apple.Safari"
- "com.apple.ScreenContinuity"
- "com.apple.ScreenSharing"
- "com.apple.SessionTrackerApp"
- "com.apple.Siri"
- "com.apple.Spotlight"
- "com.apple.Stickies"
- "com.apple.SupportFlow"
- "com.apple.SystemProfiler"
- "com.apple.TV"
- "com.apple.TVRemoteUIService"
- "com.apple.Terminal"
- "com.apple.TestFlight"
- "com.apple.TextEdit"
- "com.apple.Translate"
- "com.apple.VisionProApp"
- "com.apple.VisualIntelligenceCamera"
- "com.apple.VoiceMemos"
- "com.apple.accessibility.AccessibilityReader"
- "com.apple.airport.airportutility"
- "com.apple.appleseed.FeedbackAssistant"
- "com.apple.apps.launcher"
- "com.apple.archiveutility"
- "com.apple.artistconnect"
- "com.apple.audio.AudioMIDISetup"
- "com.apple.backup.launcher"
- "com.apple.boardwalk.watchapp"
- "com.apple.brook.BrookUI"
- "com.apple.calculator"
- "com.apple.camera"
- "com.apple.carplayapp"
- "com.apple.clock"
- "com.apple.compass"
- "com.apple.demo.Calendar"
- "com.apple.dt.Devices"
- "com.apple.dt.Instruments"
- "com.apple.dt.Xcode"
- "com.apple.exposelauncher"
- "com.apple.facetime"
- "com.apple.finder"
- "com.apple.findmy"
- "com.apple.findmy.finddevices"
- "com.apple.findmy.finditems"
- "com.apple.findmy.findpeople"
- "com.apple.freeform"
- "com.apple.gamecenter"
- "com.apple.games"
- "com.apple.garageband10"
- "com.apple.grapher"
- "com.apple.iBooks"
- "com.apple.iBooksX"
- "com.apple.iCal"
- "com.apple.iMovie"
- "com.apple.iMovieApp"
- "com.apple.iWork.Keynote"
- "com.apple.iWork.Numbers"
- "com.apple.iWork.Pages"
- "com.apple.intercom"
- "com.apple.iphonesimulator"
- "com.apple.ist.AppleConnect"
- "com.apple.ist.AppleDirectory6"
- "com.apple.journal"
- "com.apple.logic10"
- "com.apple.mail"
- "com.apple.measure"
- "com.apple.mobilecal"
- "com.apple.mobilemail"
- "com.apple.mobilenotes"
- "com.apple.mobilephone"
- "com.apple.mobilesafari"
- "com.apple.mobileslideshow"
- "com.apple.mobilestore"
- "com.apple.mobiletimer"
- "com.apple.music.classical"
- "com.apple.nanomusicrecognition"
- "com.apple.nanonews"
- "com.apple.news"
- "com.apple.photobooth"
- "com.apple.podcasts"
- "com.apple.preview"
- "com.apple.private.NanoTimer"
- "com.apple.purplebuddy"
- "com.apple.reminders"
- "com.apple.rsvp"
- "com.apple.shortcuts"
- "com.apple.shortcuts.watch"
- "com.apple.siri.launcher"
- "com.apple.stocks"
- "com.apple.stocks.watchapp"
- "com.apple.systempreferences"
- "com.apple.tincan"
- "com.apple.tips"
- "com.apple.tv"
- "com.apple.watchmemojieditor"
- "com.apple.weather"
- "com.apple.weather.watchapp"
- "com.apple.wifi.diagnostics"
- "com.shazam.Shazam"
- "compass"
- "compass.watchos"
- "compressor"
- "connection.assistant"
- "console"
- "contacts"
- "cycle.tracking"
- "depth"
- "deskview"
- "developer"
- "developer.apple.wwdc-Release"
- "devices"
- "digitalcolormeter"
- "diskutility"
- "ecg"
- "eraseassistant"
- "facetime"
- "feedbackassistant"
- "filemerge"
- "files"
- "finalcut"
- "finder"
- "findevices"
- "finditems"
- "findpeople"
- "fitness"
- "fontbook"
- "gamecenter"
- "games"
- "garageband"
- "grapher"
- "handwashing"
- "health"
- "heart.rate"
- "home"
- "iOSCatalog"
- "icon.composer"
- "iconStack"
- "imageForCompositingDescriptor:"
- "imagecapture"
- "imageplayground"
- "imovie"
- "initWithBundleID:"
- "inject_alternate_assets"
- "instruments"
- "intercom"
- "invites"
- "ipadhomescreen"
- "iphonemirroring"
- "isInjectSolariumAssetsEnabled"
- "itunesstore"
- "journal"
- "layerCount"
- "logic"
- "macOSCatalog"
- "magnifier"
- "mail"
- "measure"
- "medications"
- "memoji.watchos"
- "messages"
- "mindfulness"
- "missioncontrol"
- "motion"
- "musicforartists"
- "noise"
- "nowplaying"
- "numbers"
- "passwords"
- "phone"
- "photobooth"
- "photos"
- "platformCatalog"
- "preview"
- "primaryColour"
- "quicktimeplayer"
- "radio"
- "reader"
- "remote"
- "safari"
- "screen.sharing"
- "secondaryColour"
- "setChicletHighlightColour:"
- "setIconStack:"
- "setLayerCount:"
- "setPlatformCatalog:"
- "setPrimaryColour:"
- "setSecondaryColour:"
- "setSvgDocumentURL:"
- "settings"
- "setupassistant"
- "sfsymbols"
- "shazam"
- "shortcuts"
- "simulator"
- "siren"
- "siri.appleintelligence"
- "sleep"
- "spotlight"
- "stepbystepguides"
- "stickies"
- "stopwatch"
- "svg"
- "system.information"
- "terminal"
- "test"
- "testflight"
- "textedit"
- "tides"
- "timemachine"
- "timers"
- "tips"
- "translate"
- "vehicle"
- "visionpro.companion"
- "visualintelligence"
- "vitals"
- "voicememos"
- "walkie.talkie"
- "watch.companion"
- "watchOSCatalog"
- "wirelessdiagnostics"
- "workout"
- "world.clock"
- "xcode"

```
