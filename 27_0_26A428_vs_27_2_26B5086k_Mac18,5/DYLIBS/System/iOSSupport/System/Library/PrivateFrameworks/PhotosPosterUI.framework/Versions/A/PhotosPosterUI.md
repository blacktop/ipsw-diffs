## PhotosPosterUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosPosterUI.framework/Versions/A/PhotosPosterUI`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xa3d7c
-  __TEXT.__objc_methlist: 0x9a70
-  __TEXT.__const: 0x2690
-  __TEXT.__constg_swiftt: 0x119c
-  __TEXT.__swift5_typeref: 0x4c14
+916.41.100.0.0
+  __TEXT.__text: 0xa51d0
+  __TEXT.__objc_methlist: 0x9ba8
+  __TEXT.__const: 0x2640
+  __TEXT.__constg_swiftt: 0x114c
+  __TEXT.__swift5_typeref: 0x4b5e
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xb51
-  __TEXT.__swift5_fieldmd: 0x870
+  __TEXT.__swift5_reflstr: 0xb01
+  __TEXT.__swift5_fieldmd: 0x84c
   __TEXT.__swift5_assocty: 0x278
   __TEXT.__swift5_proto: 0x94
   __TEXT.__swift5_types: 0x90
-  __TEXT.__cstring: 0x5be6
-  __TEXT.__swift5_capture: 0x4b0
-  __TEXT.__oslogstring: 0x3ca1
+  __TEXT.__cstring: 0x5c7f
+  __TEXT.__swift5_capture: 0x500
+  __TEXT.__oslogstring: 0x3fbe
   __TEXT.__gcc_except_tab: 0x15cc
   __TEXT.__ustring: 0xdc
-  __TEXT.__unwind_info: 0x34b0
-  __TEXT.__eh_frame: 0x17c
+  __TEXT.__unwind_info: 0x3500
+  __TEXT.__eh_frame: 0x1b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2800
-  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__const: 0x2878
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68f8
+  __DATA_CONST.__objc_selrefs: 0x69d8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0xf50
-  __AUTH_CONST.__const: 0x2430
-  __AUTH_CONST.__cfstring: 0x3f80
-  __AUTH_CONST.__objc_const: 0x104b0
+  __DATA_CONST.__got: 0xf60
+  __AUTH_CONST.__const: 0x24f0
+  __AUTH_CONST.__cfstring: 0x4020
+  __AUTH_CONST.__objc_const: 0x10668
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x15a0
-  __AUTH.__objc_data: 0x2988
-  __AUTH.__data: 0x738
-  __DATA.__objc_ivar: 0xa5c
-  __DATA.__data: 0x2590
+  __AUTH_CONST.__auth_got: 0x15f8
+  __AUTH.__objc_data: 0x29d8
+  __AUTH.__data: 0x6d8
+  __DATA.__objc_ivar: 0xa68
+  __DATA.__data: 0x2560
   __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4640
-  Symbols:   9518
-  CStrings:  1020
+  Functions: 4667
+  Symbols:   9598
+  CStrings:  1035
 
Symbols:
+ +[PUWallpaperPosterDisplayFallback shouldReframeLayerStack:deviceConfiguration:]
+ +[PUWallpaperPosterDisplayFallback substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:]
+ -[PUWallpaperPosterController _applyReframedLayerStack:style:displayContext:posterMedia:]
+ -[PUWallpaperPosterController _deviceConfigurationForCurrentDisplay]
+ -[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]
+ -[PUWallpaperPosterController forcedPosterUpgradeReason]
+ -[PUWallpaperPosterController setForcedPosterUpgradeReason:]
+ -[PUWallpaperPosterEditModel editConfigurationsPerDisplayMergedWith:posterWideConfiguration:]
+ -[PUWallpaperPosterEditorController _compoundLayerStack:matchesDisplayContext:]
+ -[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:]
+ -[PUWallpaperPosterEditorController _displayContextForCurrentContainer]
+ -[PUWallpaperPosterEditorController _displayContextForSize:]
+ -[PUWallpaperPosterEditorController _displayScale]
+ -[PUWallpaperPosterEditorController _effectiveDeviceOrientation]
+ -[PUWallpaperPosterEditorController _loadContentForDisplayContext:containerSize:]
+ -[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:containerSize:]
+ -[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]
+ -[PUWallpaperPosterEditorController setTransitioningContainerSize:]
+ -[PUWallpaperPosterEditorController transitioningContainerSize]
+ -[_PUMutablePosterEditorPreferences pu_contextLinkingMode]
+ -[_PUMutablePosterEditorPreferences setPu_contextLinkingMode:]
+ -[_PUPosterEditingEnvironment px_canvasSize]
+ -[_PUPosterEditingPreferences pu_contextLinkingMode]
+ -[_PUPosterRenderingEnvironment px_canvasSize]
+ -[_PUWallpaperDebugRenderingEnvironment px_canvasSize]
+ -[_PUWallpaperPosterEditorDebugEnvironment px_canvasSize]
+ -[_PUWallpaperPosterEditorDebugPreferences pu_contextLinkingMode]
+ -[_PUWallpaperPosterEditorDebugPreferences setPu_contextLinkingMode:]
+ GCC_except_table1028
+ GCC_except_table1034
+ GCC_except_table1039
+ GCC_except_table1044
+ GCC_except_table1064
+ GCC_except_table1066
+ GCC_except_table1068
+ GCC_except_table1096
+ GCC_except_table1372
+ GCC_except_table1373
+ GCC_except_table1493
+ GCC_except_table1494
+ GCC_except_table151
+ GCC_except_table1518
+ GCC_except_table161
+ GCC_except_table1715
+ GCC_except_table1720
+ GCC_except_table1740
+ GCC_except_table1784
+ GCC_except_table1792
+ GCC_except_table1826
+ GCC_except_table1827
+ GCC_except_table1828
+ GCC_except_table1854
+ GCC_except_table1858
+ GCC_except_table1863
+ GCC_except_table1867
+ GCC_except_table1869
+ GCC_except_table1872
+ GCC_except_table1875
+ GCC_except_table1878
+ GCC_except_table1887
+ GCC_except_table1926
+ GCC_except_table1988
+ GCC_except_table2013
+ GCC_except_table2016
+ GCC_except_table2027
+ GCC_except_table2033
+ GCC_except_table2036
+ GCC_except_table2050
+ GCC_except_table2053
+ GCC_except_table2086
+ GCC_except_table2097
+ GCC_except_table2099
+ GCC_except_table2103
+ GCC_except_table2120
+ GCC_except_table2124
+ GCC_except_table2130
+ GCC_except_table2132
+ GCC_except_table2136
+ GCC_except_table2139
+ GCC_except_table2141
+ GCC_except_table2148
+ GCC_except_table2182
+ GCC_except_table2201
+ GCC_except_table2309
+ GCC_except_table2329
+ GCC_except_table2331
+ GCC_except_table2569
+ GCC_except_table2587
+ GCC_except_table3037
+ GCC_except_table3040
+ GCC_except_table3075
+ GCC_except_table3077
+ GCC_except_table3098
+ GCC_except_table3128
+ GCC_except_table3139
+ GCC_except_table3142
+ GCC_except_table3203
+ GCC_except_table3225
+ GCC_except_table3228
+ GCC_except_table422
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table740
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table992
+ OBJC_IVAR_$_PUWallpaperPosterController._forcedPosterUpgradeReason
+ OBJC_IVAR_$_PUWallpaperPosterEditorController._transitioningContainerSize
+ OBJC_IVAR_$__PUWallpaperPosterEditorDebugPreferences._pu_contextLinkingMode
+ _CGSizeCreateDictionaryRepresentation
+ _CVPixelBufferGetHeight
+ _CVPixelBufferGetWidth
+ _OBJC_CLASS_$_PFParallaxLayerStack
+ _OBJC_CLASS_$_PUWallpaperPosterDisplayFallback
+ _OBJC_METACLASS_$_PUWallpaperPosterDisplayFallback
+ _PFFigCreateCVPixelBufferFromURL
+ _PFFigDecodeOptionsWithMaxPixelSize
+ _PFParallaxZPositionOnlyBackground
+ _PPPosterContextLinkingModeUsingEditingPreferences
+ _PPPosterContextLinkingModeUsingMutableEditingPreferences
+ _PPPosterSetContextLinkingModeUsingMutableEditingPreferences
+ _PUWallpaperPosterReframedLayout
+ _PUWallpaperPosterRetainedCropFilling
+ _PUWallpaperPosterRetainedCropForDisplay
+ _PUWallpaperPosterSubstituteStack
+ _PXRectArea
+ _PXRectWithCenterAndSize
+ _PXSizeClampToSize
+ _PXSizeGetArea
+ _PXSizeGetAspectRatioWithDefault
+ _PXSizeWithAspectRatioFillingSize
+ __95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke
+ __OBJC_$_CLASS_METHODS_PUWallpaperPosterDisplayFallback
+ __OBJC_CLASS_RO_$_PUWallpaperPosterDisplayFallback
+ __OBJC_METACLASS_RO_$_PUWallpaperPosterDisplayFallback
+ ___103-[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:containerSize:]_block_invoke
+ ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke
+ ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_2
+ ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_3
+ ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_4
+ ___123-[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:]_block_invoke
+ ___64-[PUWallpaperPosterEditorController _handleOutfillButtonTapped:]_block_invoke_2
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e39_B32?0"PFPosterDisplayContext"8Q16^B24ls32l8
+ ___block_descriptor_72_e8_32s40s48w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8s48l8w72l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0ls32l8s40l8s48l8w80l8s56l8s64l8s72l8
+ ___swift_memcpy65_8
+ __swift_closure_destructor.121Tm
+ _objc_msgSend$_applyReframedLayerStack:style:displayContext:posterMedia:
+ _objc_msgSend$_compoundLayerStack:matchesDisplayContext:
+ _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:
+ _objc_msgSend$_deviceConfigurationForCurrentDisplay
+ _objc_msgSend$_displayContextForCurrentContainer
+ _objc_msgSend$_displayContextForSize:
+ _objc_msgSend$_displayScale
+ _objc_msgSend$_effectiveDeviceOrientation
+ _objc_msgSend$_loadContentForDisplayContext:containerSize:
+ _objc_msgSend$_reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:
+ _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:containerSize:
+ _objc_msgSend$_transitionToDisplayContext:containerSize:withCoordinator:
+ _objc_msgSend$canvasSize
+ _objc_msgSend$contextLinkingMode
+ _objc_msgSend$deviceConfigurationForDisplayContext:
+ _objc_msgSend$editConfigurationsPerDisplayMergedWith:posterWideConfiguration:
+ _objc_msgSend$ensureLayoutsForAllDisplayContexts:preservesLayout:completion:
+ _objc_msgSend$forcedPosterUpgradeReason
+ _objc_msgSend$imageFileURL
+ _objc_msgSend$initWithImage:frame:zPosition:identifier:
+ _objc_msgSend$initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:userAdjustedVisibleFrame:
+ _objc_msgSend$isAnyFrameUsingHeadroom
+ _objc_msgSend$layoutByUpdatingInactiveFrame:
+ _objc_msgSend$layoutByUpgradingToConfiguration:
+ _objc_msgSend$loadFromArchiveURL:error:
+ _objc_msgSend$px_canvasSize
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setContextLinkingMode:
+ _objc_msgSend$setForcedPosterUpgradeReason:
+ _objc_msgSend$setPu_contextLinkingMode:
+ _objc_msgSend$setSupportsLandscapeConfiguration:
+ _objc_msgSend$setTransitioningContainerSize:
+ _objc_msgSend$shouldReframeLayerStack:deviceConfiguration:
+ _objc_msgSend$substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:
+ _objc_msgSend$transitioningContainerSize
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
+ _symbolic SaySo6UIViewCGz_Xx
+ _symbolic _____yAAyAAy_____y_____yACyAAy__________G_____GAGG_____G_____G_____y_____GGAPG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V AA11_ClipEffectV AA16RoundedRectangleV
+ _symbolic _____yAAy_____y_____yACyAAy__________G_____GAGG_____G_____G_____y_____GG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V AA11_ClipEffectV AA16RoundedRectangleV
+ _symbolic _____y_____yABy_____y__________G_____GAGG_____G 17PhotosSwiftUICore0A10AsyncImageV 0B2UI19_ConditionalContentV AD08ModifiedH0V AD0E0V AD18_AspectRatioLayoutV AD5ColorV AA0ad5AssetE8ProviderV
+ _symbolic _____y_____y_____yACyAAy__________G_____GAGG_____G_____G 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V
+ get_witness_table 7SwiftUI15ModifiedContentVyACyACy06PhotosA6UICore0E10AsyncImageVyAA012_ConditionalD0VyAHyACyAA0H0VAA18_AspectRatioLayoutVGAA5ColorVGAOGAD0eg5AssetH8ProviderVGAA06_FrameL0VGAA11_ClipEffectVyAA16RoundedRectangleVGGA0_GAA4ViewHPA1_AAA3_HPAwAA3_HPAtAA3_HPyHC_AvA0U8ModifierHPyHCHC_A0_AAA4_HPyHCHC_A0_AAA4_HPyHCHC
- -[PUWallpaperPosterController _detectDisplayContextChangeWithSize:]
- -[PUWallpaperPosterEditModel editConfigurationsPerDisplay]
- -[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:]
- -[PUWallpaperPosterEditorController _currentDisplaySupportsLandscape]
- -[PUWallpaperPosterEditorController _displayContextFromContainerSize:]
- -[PUWallpaperPosterEditorController _displayContextFromPresentationContext:]
- -[PUWallpaperPosterEditorController _loadContentForDisplayContext:]
- -[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:]
- -[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]
- GCC_except_table1019
- GCC_except_table1024
- GCC_except_table1029
- GCC_except_table1049
- GCC_except_table1051
- GCC_except_table1053
- GCC_except_table1081
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1478
- GCC_except_table1479
- GCC_except_table148
- GCC_except_table1503
- GCC_except_table158
- GCC_except_table1692
- GCC_except_table1697
- GCC_except_table1717
- GCC_except_table1761
- GCC_except_table1770
- GCC_except_table1804
- GCC_except_table1805
- GCC_except_table1806
- GCC_except_table1832
- GCC_except_table1836
- GCC_except_table1841
- GCC_except_table1845
- GCC_except_table1847
- GCC_except_table1850
- GCC_except_table1853
- GCC_except_table1856
- GCC_except_table1865
- GCC_except_table1904
- GCC_except_table1966
- GCC_except_table1991
- GCC_except_table1994
- GCC_except_table2005
- GCC_except_table2011
- GCC_except_table2014
- GCC_except_table2028
- GCC_except_table2031
- GCC_except_table2064
- GCC_except_table2075
- GCC_except_table2077
- GCC_except_table2080
- GCC_except_table2083
- GCC_except_table2094
- GCC_except_table2096
- GCC_except_table2100
- GCC_except_table2101
- GCC_except_table2108
- GCC_except_table2113
- GCC_except_table2116
- GCC_except_table2158
- GCC_except_table2175
- GCC_except_table2283
- GCC_except_table2303
- GCC_except_table2305
- GCC_except_table2543
- GCC_except_table2561
- GCC_except_table3006
- GCC_except_table3009
- GCC_except_table3044
- GCC_except_table3046
- GCC_except_table3066
- GCC_except_table3067
- GCC_except_table3108
- GCC_except_table3111
- GCC_except_table3172
- GCC_except_table3194
- GCC_except_table3197
- GCC_except_table416
- GCC_except_table419
- GCC_except_table420
- GCC_except_table733
- GCC_except_table745
- GCC_except_table746
- GCC_except_table983
- __81-[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]_block_invoke
- ___109-[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:]_block_invoke
- ___81-[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]_block_invoke
- ___81-[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]_block_invoke_2
- ___89-[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:]_block_invoke
- ___block_descriptor_56_e8_32s40s48w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw48l8s32l8s40l8
- ___swift_memcpy73_8
- __swift_closure_destructor.129Tm
- _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:
- _objc_msgSend$_currentDisplaySupportsLandscape
- _objc_msgSend$_detectDisplayContextChangeWithSize:
- _objc_msgSend$_displayContextFromContainerSize:
- _objc_msgSend$_loadContentForDisplayContext:
- _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:
- _objc_msgSend$_transitionToDisplayContext:withCoordinator:
- _objc_msgSend$currentEditViewModel
- _objc_msgSend$editConfigurationsPerDisplay
- _objc_msgSend$ensureLayoutsForAllDisplayContexts:completion:
- _symbolic So7UIImageCSg
- _symbolic _____yAAyAAy_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG_____y_____GGAUG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV AA11_ClipEffectV AA16RoundedRectangleV
- _symbolic _____yAAy__________G_____GSg 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameH0V
- _symbolic _____yAAy__________G_____yAAyAD_____GSgGG 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameH0V
- _symbolic _____yAAy_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG_____y_____GG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV AA11_ClipEffectV AA16RoundedRectangleV
- _symbolic _____y_____yABy__________G_____GSgG 7SwiftUI16_OverlayModifierV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameJ0V
- _symbolic _____y_____yABy_____yACy__________G_____yACyAF_____GSgGG_____GAMG_____G 17PhotosSwiftUICore0A10AsyncImageV 0B2UI19_ConditionalContentV AD08ModifiedH0V AD0E0V AD18_AspectRatioLayoutV AD16_OverlayModifierV AD06_FrameL0V AD5ColorV AA0ad5AssetE8ProviderV
- _symbolic _____y_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV
- get_witness_table 7SwiftUI15ModifiedContentVyACyACy06PhotosA6UICore0E10AsyncImageVyAA012_ConditionalD0VyAHyACyACyAA0H0VAA18_AspectRatioLayoutVGAA16_OverlayModifierVyACyAmA06_FrameL0VGSgGGAA5ColorVGAWGAD0eg5AssetH8ProviderVGAQGAA11_ClipEffectVyAA16RoundedRectangleVGGA6_GAA4ViewHPA7_AAA9_HPA1_AAA9_HPA0_AAA9_HPyHC_AqA0wN0HPyHCHC_A6_AAA10_HPyHCHC_A6_AAA10_HPyHCHC
CStrings:
+ ", normalized landscape to portrait"
+ "Attempt to load wallpaper for context %{public}@ from poster url: %{public}@"
+ "B32@?0@\"PFPosterDisplayContext\"8Q16^B24"
+ "CancelOutfill"
+ "Cannot initialize display context: neither backgroundView bounds nor canvas size are known yet"
+ "Cannot reframe poster: failed to load its asset resource: %{public}@"
+ "Cannot reframe poster: its asset resource holds no full-size image"
+ "Cannot resolve initial display context: neither view bounds nor canvas size are known"
+ "Discarding reframed poster for stale display context or media"
+ "ExtendOutfill"
+ "Failed to decode poster asset for display fallback, code: %d"
+ "Forcing depth off for stand-in layout on display %{public}@"
+ "Initial display context: %{public}@ (landscape=%d)"
+ "Initializing display context: bounds %.0f×%.0f, canvas %.0f×%.0f, embedded=%d, callServices=%d%{public}@"
+ "Layer stack was baked for %.0fx%.0f but display %{public}@ is %.0fx%.0f; re-rendering"
+ "Layout configuration mismatch detected, updating layout for display %{public}@"
+ "Poster retains %.0f%% of its saved crop on this display (saved for %{public}@, display portrait %{public}@ landscape %{public}@)"
+ "Reframed poster: portrait visible %{public}@, landscape visible %{public}@, decoded %zu×%zu"
+ "Transitioning to display context: %{public}@ (landscape=%d)"
+ "Triggering poster upgrade: %{public}@"
+ "asset.resource"
+ "input.segmentation"
- "Attempt to load wallpaper from poster url: %{public}@"
- "Display context change detected from bounds: %{public}@ -> %{public}@"
- "Forcing depth off for not-yet-migrated poster on landscape-capable display"
- "Initial display context from view frame: %{public}@"
- "Layout configuration mismatch detected, updating layout for current device"
- "Set initial display context from bounds: %{public}@"
- "Transitioning to display context: %{public}@"
```
