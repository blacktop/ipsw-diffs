## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI`

```diff

-917.3.0.0.0
-  __TEXT.__text: 0xe73f4
-  __TEXT.__auth_stubs: 0x2b20
-  __TEXT.__objc_methlist: 0x95b0
-  __TEXT.__const: 0x8c58
-  __TEXT.__cstring: 0x29fc0
-  __TEXT.__gcc_except_tab: 0x1804
+918.3.0.0.0
+  __TEXT.__text: 0xe6d60
+  __TEXT.__auth_stubs: 0x2b50
+  __TEXT.__objc_methlist: 0x9b18
+  __TEXT.__const: 0x8c88
+  __TEXT.__cstring: 0x29fe0
+  __TEXT.__gcc_except_tab: 0x1864
   __TEXT.__oslogstring: 0x52
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__swift5_typeref: 0x80

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x3b90
+  __TEXT.__unwind_info: 0x3b38
   __TEXT.__objc_classname: 0x1069
-  __TEXT.__objc_methname: 0x1581c
+  __TEXT.__objc_methname: 0x15823
   __TEXT.__objc_methtype: 0x622c
-  __TEXT.__objc_stubs: 0xe8c0
+  __TEXT.__objc_stubs: 0xe8e0
   __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__const: 0x1b6470
+  __DATA_CONST.__const: 0x1b6478
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4dd0
+  __DATA_CONST.__objc_selrefs: 0x4e58
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x17d0
-  __AUTH_CONST.__auth_got: 0x15a8
+  __AUTH_CONST.__auth_got: 0x15c0
   __AUTH_CONST.__const: 0x3e18
-  __AUTH_CONST.__cfstring: 0x14340
-  __AUTH_CONST.__objc_const: 0xf830
+  __AUTH_CONST.__cfstring: 0x143a0
+  __AUTH_CONST.__objc_const: 0xee28
   __AUTH_CONST.__objc_intobj: 0x14d0
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x4b0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1DEC2A76-1D0E-388A-8B33-89A87FDD508F
-  Functions: 5147
-  Symbols:   12133
-  CStrings:  12873
+  UUID: 3D3EFA87-BDD0-370D-8350-BD80BAD50628
+  Functions: 5280
+  Symbols:   12413
+  CStrings:  12876
 
Symbols:
+ +[CUICatalog defaultUICatalogForBundle:].cold.1
+ +[CUIDesignLibraryCatalog catalogForDesignSystem:colorScheme:contrast:styling:error:].cold.1
+ +[CUIDesignLibraryCompositeCatalog compositeCatalogForDesignSystem:colorScheme:contrast:styling:error:].cold.1
+ +[CUINamedLayerStack radiosityImageWithImage:displayScale:completionHandler:].cold.1
+ +[CUINamedVectorGlyph _backgroundImageNamesAtom].cold.1
+ +[CUINamedVectorGlyph _colorStyleNames].cold.1
+ +[CUINamedVectorGlyph _hasImageFillsAtom].cold.1
+ +[CUINamedVectorGlyph _layerHierarchyStyleNames].cold.1
+ +[CUINamedVectorGlyph _rotatesClockwiseAtom].cold.1
+ +[CUINamedVectorGlyph _variableColorContinuousAtom].cold.1
+ +[CUINamedVectorGlyph _wiggleAngleAtom].cold.1
+ +[CUINamedVectorGlyph _wiggleStyleAtom].cold.1
+ +[CUIRuntimeStatistics sharedRuntimeStatistics].cold.1
+ +[CUIShapeEffectStack preferredCIContextOptions].cold.1
+ +[CUIShapeEffectStack sharedCIContext].cold.1
+ +[CUISharedArtCatalog _duplicateNamesDict].cold.1
+ +[CUISharedArtCatalog iconNamesAndCreatorCodes].cold.1
+ +[CUIThemeFacet _facetWithKeyList:andRenditionKeyClass:orRenditionKey:fromTheme:].cold.1
+ +[CUIThemeFacet _facetWithKeyList:andRenditionKeyClass:orRenditionKey:fromTheme:].cold.2
+ +[CUIThemeFacet _facetWithKeyList:andRenditionKeyClass:orRenditionKey:fromTheme:].cold.3
+ +[CUIThemeSchema schemaForPlatform:].cold.1
+ +[CUIVectorGlyphLayer _alwaysBreathesAtom].cold.1
+ +[CUIVectorGlyphLayer _alwaysPulsesAtom].cold.1
+ +[CUIVectorGlyphLayer _alwaysRotatesAtom].cold.1
+ +[CUIVectorGlyphLayer _clearBehindAtom].cold.1
+ +[CUIVectorGlyphLayer _fillActionAtom].cold.1
+ +[CUIVectorGlyphLayer _layerHierarchyStyleNames].cold.1
+ +[CUIVectorGlyphLayer _layerTagsAtom].cold.1
+ +[CUIVectorGlyphLayer _motionGroupAtom].cold.1
+ +[CUIVectorGlyphLayer _subpathIndicesAtom].cold.1
+ +[CUIVectorGlyphLayer _variableThresholdAtom].cold.1
+ +[CUIVectorGlyphMutator _interpolationData].cold.1
+ +[_CSIRenditionBlockData sharedCache].cold.1
+ -[CSIBitmapWrapper bitmapContext].cold.1
+ -[CUICatalog _vibrantColorMatrixBrightnessSaturationForColor:saturation:brightness:].cold.1
+ -[CUICatalog colorWithName:displayGamut:deviceIdiom:appearanceName:].cold.1
+ -[CUIHueSaturationFilterLocal _kernel].cold.1
+ -[CUIInnerBevelEmbossFilterLocal _kernelInvertMask].cold.1
+ -[CUIInnerBevelEmbossFilterLocal _kernelMultiplyByMask].cold.1
+ -[CUIInnerBevelEmbossFilterLocal outputImage].cold.1
+ -[CUIInnerGlowFilterLocal outputImage].cold.1
+ -[CUIInnerGlowOrShadowFilterLocal _kernel].cold.1
+ -[CUIInnerShadowFilterLocal outputImage].cold.1
+ -[CUIMutableCommonAssetStorage setRenditionKey:hotSpot:forName:].cold.1
+ -[CUIMutableCommonAssetStorage setRenditionKey:hotSpot:forName:].cold.2
+ -[CUIMutableThemeRendition initWithCGImage:withDescription:forKey:].cold.1
+ -[CUIMutableThemeRendition initWithCGImage:withDescription:forKey:].cold.2
+ -[CUINamedVectorGlyph alignmentRectUnrounded].cold.1
+ -[CUINamedVectorGlyph alignmentRect].cold.1
+ -[CUINamedVectorGlyph containsNamedColorStyles].cold.1
+ -[CUINamedVectorGlyph contentBoundsUnrounded].cold.1
+ -[CUINamedVectorGlyph contentBounds].cold.1
+ -[CUINamedVectorGlyph drawInContext:withPaletteColors:].cold.1
+ -[CUINamedVectorGlyph drawInContext:withPaletteColors:].cold.2
+ -[CUINamedVectorGlyph graphicVariantWithOptions:].cold.1
+ -[CUINamedVectorGlyph hierarchyLayers].cold.1
+ -[CUINamedVectorGlyph hierarchyLevels].cold.1
+ -[CUINamedVectorGlyph imageWithHierarchicalPrimaryColor:].cold.1
+ -[CUINamedVectorGlyph multicolorColorNames].cold.1
+ -[CUINamedVectorGlyph multicolorLayerColorNames].cold.1
+ -[CUINamedVectorGlyph paletteLevels].cold.1
+ -[CUINamedVectorGlyph rasterizeImageUsingScaleFactor:forTargetSize:hierarchicalPrimaryColor:].cold.1
+ -[CUINamedVectorPDFImage rasterizeImageUsingScaleFactor:forTargetSize:].cold.1
+ -[CUINamedVectorPDFImage rasterizeImageUsingScaleFactor:forTargetSize:].cold.2
+ -[CUINamedVectorSVGImage rasterizeImageUsingScaleFactor:forTargetSize:].cold.1
+ -[CUINamedVectorSVGImage rasterizeImageUsingScaleFactor:forTargetSize:].cold.2
+ -[CUIOuterBevelEmbossFilterLocal _kernelColorizeWithImageMask].cold.1
+ -[CUIOuterBevelEmbossFilterLocal _kernelColorize].cold.1
+ -[CUIOuterBevelEmbossFilterLocal _kernel].cold.1
+ -[CUIOuterBevelEmbossFilterLocal outputImage].cold.1
+ -[CUIOuterGlowFilterLocal outputImage].cold.1
+ -[CUIOuterGlowOrShadowFilterLocal _kernelWithImageMask].cold.1
+ -[CUIOuterGlowOrShadowFilterLocal _kernel].cold.1
+ -[CUIOuterGlowOrShadowFilterLocal outputImage].cold.1
+ -[CUIOuterShadowFilterLocal outputImage].cold.1
+ -[CUIPSDGradientEvaluator initWithColorStops:colorMidpoints:opacityStops:opacityMidpoints:smoothingCoefficient:fillColor:dither:].cold.1
+ -[CUIPSDGradientStop initWithLocation:].cold.1
+ -[CUIScaleClampFilterLocal _kernel].cold.1
+ -[CUIShapeEffectStack standardEffectCompositeWithShapeImage:blendOntoImage:].cold.1
+ -[CUISmoothEmbossFilterLocal outputImage].cold.1
+ -[CUIStructuredThemeStore localizationWorkaroundForKeyList:withLocale:].cold.1
+ -[CUIThemeDataEffectPreset initWithEffectData:forScaleFactor:].cold.1
+ -[CUIThemeFacet initWithCoder:].cold.1
+ -[CUIThemeFacet initWithRenditionKey:fromTheme:].cold.1
+ -[CUIThemeFacet thumbnail].cold.1
+ -[CUIThemeFacet updateLayer:effects:].cold.1
+ -[CUIThemeGradient initWithColors:colorlocations:colorMidpoints:opacities:opacityLocations:opacityMidpoints:smoothingCoefficient:fillColor:colorSpace:dither:].cold.1
+ -[CUIThemeGradient initWithColors:colorlocations:colorMidpoints:opacities:opacityLocations:opacityMidpoints:smoothingCoefficient:fillColor:colorSpace:dither:].cold.2
+ -[CUIThemeSchemaRenditionGroup mutablePSDImageRefColumnStyle].cold.1
+ -[_CUIExternalLinkRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIExternalLinkRendition _initWithCSIHeader:version:].cold.2
+ -[_CUIExternalLinkRendition _initWithCSIHeader:version:].cold.3
+ -[_CUIInternalLinkRendition _initWithCSIHeader:version:].cold.1
+ -[_CUILayerStackRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIRawDataRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIRawPixelRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemeColorRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemeModelAssetRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemeModelMeshRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemeModelSubmeshRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemeMultisizeImageSetRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemePDFRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemePDFRendition _initWithCSIHeader:version:].cold.2
+ -[_CUIThemePixelRendition _initWithCSIHeader:version:].cold.1
+ -[_CUIThemePixelRendition _initWithCSIHeader:version:].cold.2
+ -[_CUIThemeTextStyleRendition _initWithCSIHeader:version:].cold.1
+ BOMExceptionHandlerSet.cold.1
+ BOMStorageCopyFromBlockRange.cold.1
+ BOMStorageCopyToBlockRange.cold.1
+ BOMStorageCopyToBlockRange.cold.2
+ BOMStorageCopyToBlockRange.cold.3
+ BOMStorageCopyToBlockRange.cold.4
+ BOMStorageCopyToBlockRange.cold.5
+ BOMStreamReadBuffer.cold.1
+ CUIAddClipStrokeKeyframeDataToNode.cold.1
+ CUIConstantToMapID.cold.1
+ CUICreateClipStrokeKeyframeDataFromNode.cold.1
+ CUIGetConstantForMapID.cold.1
+ CUIImageCompressedWithColorQuantization.cold.1
+ CUIImageCompressedWithColorQuantization.cold.2
+ CUIImageCompressedWithColorQuantization.cold.3
+ CUIImageIsWideGamut.cold.1
+ CUILogHandle.cold.1
+ CUIUncompressHEVCInfoData.cold.1
+ GCC_except_table658
+ GCC_except_table660
+ GCC_except_table674
+ GCC_except_table680
+ GCC_except_table681
+ GCC_except_table686
+ GCC_except_table696
+ GCC_except_table703
+ GCC_except_table704
+ PerformBlockWithThemeRefCache.cold.1
+ _BOMFileInit.cold.1
+ _BOMFileInit.cold.2
+ _CUIColorGetSRGBBlack.cold.1
+ _CUIColorGetSRGBClear.cold.1
+ _CUIColorGetSRGBWhite.cold.1
+ _CUIColorSpaceGetDisplayP3.cold.1
+ _CUIColorSpaceGetExtendedGray.cold.1
+ _CUIColorSpaceGetExtendedLinearSRGB.cold.1
+ _CUIColorSpaceGetExtendedRangeSRGB.cold.1
+ _CUIColorSpaceGetGenericRGB.cold.1
+ _CUIColorSpaceGetGray.cold.1
+ _CUIColorSpaceGetGrayGamma2_2.cold.1
+ _CUIColorSpaceGetSRGB.cold.1
+ _CUICreateMenuPath.cold.1
+ _CUICreateNewPopoverPath.cold.1
+ _CUIDebugAllowHardwareRendering.cold.1
+ _CUIDebugShowGraphicVariantMetrics.cold.1
+ _CUIDebugShowInputBounds.cold.1
+ _CUIDebugUseDeferredImageRendering.cold.1
+ _CUIDebugUseShapeEffects.cold.1
+ _CUIDebugUseSimplifiedTextAntialiasing.cold.1
+ _CUIDebugUseSimplifiedTextEffects.cold.1
+ _CUIDebugUseStandardRendering.cold.1
+ _CUILog.cold.2
+ _CUILog.cold.3
+ _CUILog.cold.4
+ _CUILog.cold.5
+ _CUILog.cold.6
+ _CUILog.cold.7
+ _CUIMetricsGatheringEnabled.cold.1
+ _CUIThreadLock.cold.1
+ _CUIVectorGlyphIncompatiblePointsException
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN11CUIRenderer28CreateLayerContentsFromImageEPK13CUIDescriptorPP7CGImageP6CGRect.cold.1
+ _ZNK20CUICoreThemeRenderer19CopyCustomColorCoreEPK10__CFStringPK14__CFDictionary.cold.1
+ _ZNK20CUICoreThemeRenderer19CopyCustomColorCoreEPK10__CFStringPK14__CFDictionary.cold.2
+ _ZNK20CUICoreThemeRenderer19CopyCustomColorCoreEPK10__CFStringPK14__CFDictionary.cold.3
+ _ZNK20CUICoreThemeRenderer19CopyCustomColorCoreEPK10__CFStringPK14__CFDictionary.cold.4
+ _ZNK20CUICoreThemeRenderer28CopyCustomFontDescriptorCoreEPK10__CFStringdPd.cold.1
+ _ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI15CPSDLayerRecordEES2_EEvRT_PT0_S7_S7_.cold.1
+ __105-[CUINamedVectorGlyph _legacy_drawHierarchicalLayerNamed:inContext:scaleFactor:targetSize:colorResolver:]_block_invoke.167
+ __32-[CUISmallBlurLocal outputImage]_block_invoke.cold.1
+ __35-[CUIScaleClampFilterLocal _kernel]_block_invoke.cold.1
+ __36-[CUINamedVectorGlyph paletteLevels]_block_invoke.cold.1
+ __38-[CUIHueSaturationFilterLocal _kernel]_block_invoke.cold.1
+ __38-[CUIInnerGlowFilterLocal outputImage]_block_invoke.cold.1
+ __38-[CUIOuterGlowFilterLocal outputImage]_block_invoke.cold.1
+ __39-[CUIShapeEffectBlur1Local outputImage]_block_invoke.cold.1
+ __40-[CUIInnerShadowFilterLocal outputImage]_block_invoke.cold.1
+ __40-[CUIOuterShadowFilterLocal outputImage]_block_invoke.cold.1
+ __41-[CUIOuterBevelEmbossFilterLocal _kernel]_block_invoke.cold.1
+ __41-[CUISmoothEmbossFilterLocal outputImage]_block_invoke.cold.1
+ __42-[CUIInnerGlowOrShadowFilterLocal _kernel]_block_invoke.cold.1
+ __42-[CUIOuterGlowOrShadowFilterLocal _kernel]_block_invoke.cold.1
+ __43-[CUINamedVectorGlyph multicolorColorNames]_block_invoke.cold.1
+ __46-[CUINamedVectorGlyph imageWithPaletteColors:]_block_invoke.114
+ __46-[CUINamedVectorGlyph templateLayerThresholds]_block_invoke.66
+ __47-[CUINamedVectorGlyph containsNamedColorStyle:]_block_invoke.cold.1
+ __48-[CUINamedVectorGlyph multicolorLayerColorNames]_block_invoke.cold.1
+ __49-[CUIOuterBevelEmbossFilterLocal _kernelColorize]_block_invoke.cold.1
+ __50-[CUINamedVectorGlyph hierarchicalLayerThresholds]_block_invoke.cold.1
+ __51-[CUIInnerBevelEmbossFilterLocal _kernelInvertMask]_block_invoke.cold.1
+ __55-[CUIInnerBevelEmbossFilterLocal _kernelMultiplyByMask]_block_invoke.cold.1
+ __55-[CUINamedVectorGlyph drawInContext:withPaletteColors:]_block_invoke.119
+ __55-[CUIOuterGlowOrShadowFilterLocal _kernelWithImageMask]_block_invoke.cold.1
+ __62-[CUIOuterBevelEmbossFilterLocal _kernelColorizeWithImageMask]_block_invoke.cold.1
+ __63-[CUINamedVectorGlyph _layerNamesForRenderingMode:inRendition:]_block_invoke.286
+ __BOMExceptionMessageString.cold.1
+ __BOMGlobalExceptionHandler.cold.1
+ __CUIImageCompressedWithDeepmap.cold.1
+ __CUIImageCompressedWithDeepmap2.cold.1
+ __MergedGlobals
+ __PerformBlockWithThemeRegistry.cold.1
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI10CPSDStringEEPS2_EclB8ne190102Ev
+ __ZNKSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI20PSDGradientColorStopNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI22PSDGradientOpacityStopNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP21CPSDLayerChannelGroupNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP23CPSDActionBaseComponentNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__114__split_bufferI10CPSDStringRNS_9allocatorIS1_EEE17__destruct_at_endB8ne190102EPS1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI10CPSDStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI15CPSDLayerRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19CPSDActionKeyedItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI20PSDGradientColorStopEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI21CPSDChannelLengthInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI22PSDGradientOpacityStopEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI23CPSDChannelBlendingInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP21CPSDLayerChannelGroupEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP23CPSDActionBaseComponentEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI10CPSDStringEEPS3_EEED2B8ne190102Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI10CPSDStringEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI15CPSDLayerRecordEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI19CPSDActionKeyedItemEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI21CPSDChannelLengthInfoEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI23CPSDChannelBlendingInfoEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE22__construct_one_at_endB8ne190102IJRKS1_EEEvDpOT_
+ __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___CUIDebugUseDeferredImageRendering_block_invoke.cold.1
+ __block_literal_global.180
+ __block_literal_global.182
+ __block_literal_global.184
+ __block_literal_global.186
+ __block_literal_global.192
+ __block_literal_global.251
+ __block_literal_global.71
+ __getDeviceTraits.cold.1
+ _objc_exception_rethrow
+ _objc_msgSend$reason
+ _objc_terminate
+ _swift_unknownObjectRelease_n
- -[CUIVectorGlyphMutator initWithPointSize:regular:ultralight:black:].cold.1
- -[CUIVectorGlyphMutator initWithPointSize:regular:ultralight:black:].cold.2
- GCC_except_table659
- GCC_except_table662
- GCC_except_table678
- GCC_except_table682
- GCC_except_table683
- GCC_except_table692
- GCC_except_table700
- GCC_except_table705
- GCC_except_table706
- _ZN4File12CopyToBufferEPKvl.cold.1
- _ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorI15CPSDLayerRecordEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_.cold.1
- __105-[CUINamedVectorGlyph _legacy_drawHierarchicalLayerNamed:inContext:scaleFactor:targetSize:colorResolver:]_block_invoke.166
- __46-[CUINamedVectorGlyph imageWithPaletteColors:]_block_invoke.113
- __46-[CUINamedVectorGlyph templateLayerThresholds]_block_invoke.65
- __55-[CUINamedVectorGlyph drawInContext:withPaletteColors:]_block_invoke.118
- __63-[CUINamedVectorGlyph _layerNamesForRenderingMode:inRendition:]_block_invoke.285
- __ZN22CPSDGradientDescriptor13GetIsDitheredEv
- __ZN22CPSDGradientDescriptor13GetIsReversedEv
- __ZN22CPSDGradientDescriptor8GetAngleEv
- __ZN4File12CopyToBufferEPKvl
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI10CPSDStringEENS_16reverse_iteratorIPS2_EEEclB8ne180100Ev
- __ZNKSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI20PSDGradientColorStopNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI22PSDGradientOpacityStopNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP21CPSDLayerChannelGroupNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP23CPSDActionBaseComponentNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__114__split_bufferI10CPSDStringRNS_9allocatorIS1_EEE17__destruct_at_endB8ne180100EPS1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI10CPSDStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI15CPSDLayerRecordEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI19CPSDActionKeyedItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI20PSDGradientColorStopEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI21CPSDChannelLengthInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI22PSDGradientOpacityStopEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI23CPSDChannelBlendingInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP21CPSDLayerChannelGroupEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP23CPSDActionBaseComponentEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI10CPSDStringEENS_16reverse_iteratorIPS3_EEEEED2B8ne180100Ev
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorI10CPSDStringEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorI15CPSDLayerRecordEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE22__construct_one_at_endB8ne180100IJRKS1_EEEvDpOT_
- __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___VectorGlyphDimension2ToPointSizeTableWatch
- ___nonOpaqueProviderOptions
- ___opaqueProviderOptions
- ___providerOptionsOnce
- __block_literal_global.181
- __block_literal_global.183
- __block_literal_global.185
- __block_literal_global.187
- __block_literal_global.189
- __block_literal_global.191
- __block_literal_global.250
- __block_literal_global.70
- _allocateImageBytes.__once
- _allocateImageBytes.__use_malloc
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMFile.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMStack.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMSystemCmds.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStorage.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMTree.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/CUICatalog.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIHEVCCompression.m"
+ "CUIVectorGlyphIncompatiblePointsException"
+ "CoreUI: Incompatible points when attempting to interpolate: Ultralight=%lu, Regular=%lu, Black=%lu"
+ "CoreUI: Incompatible points when attempting to interpolate: bundle-id=\"%@\""
+ "CoreUI: Incompatible points when attempting to interpolate: glyph-name=\"%@\""
+ "Incompatible glyph \"%@\" in bundle \"%@\". %@"
+ "Point counts: Ultralight=%lu, Regular=%lu, Black=%lu"
+ "reason"
- "(_ioBufferPosition + size) <= kIOBufferSize"
- "-[CUIVectorGlyphMutator initWithPointSize:regular:ultralight:black:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMBufferManager.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMFile.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMStack.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMSystemCmds.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStorage.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMTree.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/CUICatalog.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmap2Compression.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIDeepmapCompression.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/CoreTheme/ImageUtils/CUIHEVCCompression.m"
- "CopyToBuffer"
- "CoreUI: Error while decoding '%s' compressed image block data name: '%s' (rows %d rowbytes %zu format %d)"
- "WinFile.cpp"
- "_originPoints.numPoints == _blackDeltas.numDeltas"
- "_originPoints.numPoints == _ultralightDeltas.numDeltas"

```
