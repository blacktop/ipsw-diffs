## PhotosPosterUI

> `/System/Library/PrivateFrameworks/PhotosPosterUI.framework/PhotosPosterUI`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0xc0c40
-  __TEXT.__objc_methlist: 0xa624
+916.40.110.0.0
+  __TEXT.__text: 0xc16f4
+  __TEXT.__objc_methlist: 0xa72c
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__const: 0x2f18
-  __TEXT.__constg_swiftt: 0x177c
-  __TEXT.__swift5_typeref: 0x50c2
+  __TEXT.__const: 0x2ed8
+  __TEXT.__constg_swiftt: 0x172c
+  __TEXT.__swift5_typeref: 0x4ffc
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xf71
-  __TEXT.__swift5_fieldmd: 0xb6c
+  __TEXT.__swift5_reflstr: 0xf21
+  __TEXT.__swift5_fieldmd: 0xb48
   __TEXT.__swift5_assocty: 0x2d8
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__cstring: 0x6e36
-  __TEXT.__swift5_capture: 0x8cc
-  __TEXT.__oslogstring: 0x49ee
+  __TEXT.__cstring: 0x6e7e
+  __TEXT.__swift5_capture: 0x8dc
+  __TEXT.__oslogstring: 0x4cf0
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__gcc_except_tab: 0x19ac
+  __TEXT.__gcc_except_tab: 0x19a4
   __TEXT.__ustring: 0xdc
-  __TEXT.__unwind_info: 0x3c68
+  __TEXT.__unwind_info: 0x3c80
   __TEXT.__eh_frame: 0x4dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d18
-  __DATA_CONST.__objc_classlist: 0x340
+  __DATA_CONST.__const: 0x2d90
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7370
+  __DATA_CONST.__objc_selrefs: 0x7420
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x1200
-  __AUTH_CONST.__const: 0x32c0
-  __AUTH_CONST.__cfstring: 0x5060
-  __AUTH_CONST.__objc_const: 0x119a8
+  __DATA_CONST.__got: 0x1208
+  __AUTH_CONST.__const: 0x32e0
+  __AUTH_CONST.__cfstring: 0x50c0
+  __AUTH_CONST.__objc_const: 0x11b38
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1b10
-  __AUTH.__objc_data: 0x3088
-  __AUTH.__data: 0x9b0
-  __DATA.__objc_ivar: 0xa88
-  __DATA.__data: 0x2c68
+  __AUTH_CONST.__auth_got: 0x1b48
+  __AUTH.__objc_data: 0x30d8
+  __AUTH.__data: 0x950
+  __DATA.__objc_ivar: 0xa90
+  __DATA.__data: 0x2c38
   __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5306
-  Symbols:   10166
-  CStrings:  1245
+  Functions: 5310
+  Symbols:   10227
+  CStrings:  1257
 
Symbols:
+ +[PUWallpaperPosterDisplayFallback shouldReframeLayerStack:deviceConfiguration:]
+ +[PUWallpaperPosterDisplayFallback substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:]
+ -[PUWallpaperPosterController _applyReframedLayerStack:style:displayContext:posterMedia:]
+ -[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]
+ -[PUWallpaperPosterEditModel editConfigurationsPerDisplayMergedWith:posterWideConfiguration:]
+ -[PUWallpaperPosterEditorController _compoundLayerStack:matchesDisplayContext:]
+ -[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:]
+ -[PUWallpaperPosterEditorController _displayContextForCurrentContainer]
+ -[PUWallpaperPosterEditorController _displayContextForSize:]
+ -[PUWallpaperPosterEditorController _displayScale]
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
+ GCC_except_table1027
+ GCC_except_table1064
+ GCC_except_table1070
+ GCC_except_table1075
+ GCC_except_table1080
+ GCC_except_table1103
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table1152
+ GCC_except_table1432
+ GCC_except_table1433
+ GCC_except_table155
+ GCC_except_table1553
+ GCC_except_table1554
+ GCC_except_table1578
+ GCC_except_table165
+ GCC_except_table1779
+ GCC_except_table1784
+ GCC_except_table1806
+ GCC_except_table1850
+ GCC_except_table1858
+ GCC_except_table1885
+ GCC_except_table1893
+ GCC_except_table1894
+ GCC_except_table1900
+ GCC_except_table1901
+ GCC_except_table1902
+ GCC_except_table1927
+ GCC_except_table1931
+ GCC_except_table1942
+ GCC_except_table1946
+ GCC_except_table1951
+ GCC_except_table1954
+ GCC_except_table1957
+ GCC_except_table1966
+ GCC_except_table2005
+ GCC_except_table2067
+ GCC_except_table2092
+ GCC_except_table2095
+ GCC_except_table2106
+ GCC_except_table2112
+ GCC_except_table2115
+ GCC_except_table2131
+ GCC_except_table2134
+ GCC_except_table2170
+ GCC_except_table2187
+ GCC_except_table2190
+ GCC_except_table2201
+ GCC_except_table2203
+ GCC_except_table2206
+ GCC_except_table2213
+ GCC_except_table2219
+ GCC_except_table2220
+ GCC_except_table2225
+ GCC_except_table2227
+ GCC_except_table2231
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2243
+ GCC_except_table2248
+ GCC_except_table2280
+ GCC_except_table2299
+ GCC_except_table2408
+ GCC_except_table2428
+ GCC_except_table2430
+ GCC_except_table2669
+ GCC_except_table2687
+ GCC_except_table3143
+ GCC_except_table3146
+ GCC_except_table3181
+ GCC_except_table3183
+ GCC_except_table3203
+ GCC_except_table3204
+ GCC_except_table3234
+ GCC_except_table3245
+ GCC_except_table3248
+ GCC_except_table3309
+ GCC_except_table3331
+ GCC_except_table3334
+ GCC_except_table3384
+ GCC_except_table3387
+ GCC_except_table3391
+ GCC_except_table3395
+ GCC_except_table3409
+ GCC_except_table426
+ GCC_except_table429
+ GCC_except_table430
+ GCC_except_table690
+ GCC_except_table751
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table889
+ GCC_except_table900
+ _CGSizeCreateDictionaryRepresentation
+ _CVPixelBufferGetHeight
+ _CVPixelBufferGetWidth
+ _OBJC_CLASS_$_PFParallaxLayerStack
+ _OBJC_CLASS_$_PUWallpaperPosterDisplayFallback
+ _OBJC_IVAR_$_PUWallpaperPosterEditorController._transitioningContainerSize
+ _OBJC_IVAR_$__PUWallpaperPosterEditorDebugPreferences._pu_contextLinkingMode
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
+ ___74-[PUWallpaperPosterEditorController(OutfillStatus) _showOutfillStatusView]_block_invoke_2
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e39_B32?0"PFPosterDisplayContext"8Q16^B24ls32l8
+ ___block_descriptor_72_e8_32s40s48w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8s48l8w72l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0ls32l8s40l8s48l8w80l8s56l8s64l8s72l8
+ ___swift_closure_destructor.121Tm
+ ___swift_memcpy65_8
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACy06PhotosA6UICore0E10AsyncImageVyAA012_ConditionalD0VyAHyACyAA0H0VAA18_AspectRatioLayoutVGAA5ColorVGAOGAD0eg5AssetH8ProviderVGAA06_FrameL0VGAA11_ClipEffectVyAA16RoundedRectangleVGGA0_GAA4ViewHPA1_AAA3_HPAwAA3_HPAtAA3_HPyHC_AvA0U8ModifierHPyHCHC_A0_AAA4_HPyHCHC_A0_AAA4_HPyHCHC
+ _objc_msgSend$_applyReframedLayerStack:style:displayContext:posterMedia:
+ _objc_msgSend$_compoundLayerStack:matchesDisplayContext:
+ _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:
+ _objc_msgSend$_displayContextForCurrentContainer
+ _objc_msgSend$_displayContextForSize:
+ _objc_msgSend$_displayScale
+ _objc_msgSend$_loadContentForDisplayContext:containerSize:
+ _objc_msgSend$_reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:
+ _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:containerSize:
+ _objc_msgSend$_transitionToDisplayContext:containerSize:withCoordinator:
+ _objc_msgSend$canvasSize
+ _objc_msgSend$contextLinkingMode
+ _objc_msgSend$editConfigurationsPerDisplayMergedWith:posterWideConfiguration:
+ _objc_msgSend$initWithImage:frame:zPosition:identifier:
+ _objc_msgSend$initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:userAdjustedVisibleFrame:
+ _objc_msgSend$layoutByUpdatingInactiveFrame:
+ _objc_msgSend$layoutByUpgradingToConfiguration:
+ _objc_msgSend$loadFromArchiveURL:error:
+ _objc_msgSend$px_canvasSize
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setContextLinkingMode:
+ _objc_msgSend$setPu_contextLinkingMode:
+ _objc_msgSend$setSupportsLandscapeConfiguration:
+ _objc_msgSend$setTransitioningContainerSize:
+ _objc_msgSend$shouldReframeLayerStack:deviceConfiguration:
+ _objc_msgSend$startTimedProgressWithExpectedDuration:
+ _objc_msgSend$substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:
+ _objc_msgSend$transitioningContainerSize
+ _symbolic SaySo6UIViewCGz_Xx
+ _symbolic _____yAAyAAy_____y_____yACyAAy__________G_____GAGG_____G_____G_____y_____GGAPG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V AA11_ClipEffectV AA16RoundedRectangleV
+ _symbolic _____yAAy_____y_____yACyAAy__________G_____GAGG_____G_____G_____y_____GG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V AA11_ClipEffectV AA16RoundedRectangleV
+ _symbolic _____y_____yABy_____y__________G_____GAGG_____G 17PhotosSwiftUICore0A10AsyncImageV 0B2UI19_ConditionalContentV AD08ModifiedH0V AD0E0V AD18_AspectRatioLayoutV AD5ColorV AA0ad5AssetE8ProviderV
+ _symbolic _____y_____y_____yACyAAy__________G_____GAGG_____G_____G 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA5ColorV AD0eg5AssetH8ProviderV AA06_FrameL0V
- -[PUWallpaperPosterController _detectDisplayContextChangeWithSize:]
- -[PUWallpaperPosterEditModel editConfigurationsPerDisplay]
- -[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:]
- -[PUWallpaperPosterEditorController _currentDisplaySupportsLandscape]
- -[PUWallpaperPosterEditorController _displayContextFromContainerSize:]
- -[PUWallpaperPosterEditorController _displayContextFromPresentationContext:]
- -[PUWallpaperPosterEditorController _loadContentForDisplayContext:]
- -[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:]
- -[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]
- GCC_except_table1021
- GCC_except_table1058
- GCC_except_table1063
- GCC_except_table1068
- GCC_except_table1091
- GCC_except_table1093
- GCC_except_table1095
- GCC_except_table1140
- GCC_except_table1420
- GCC_except_table1421
- GCC_except_table152
- GCC_except_table1541
- GCC_except_table1542
- GCC_except_table1566
- GCC_except_table162
- GCC_except_table1759
- GCC_except_table1764
- GCC_except_table1786
- GCC_except_table1830
- GCC_except_table1839
- GCC_except_table1866
- GCC_except_table1874
- GCC_except_table1875
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1908
- GCC_except_table1912
- GCC_except_table1924
- GCC_except_table1928
- GCC_except_table1930
- GCC_except_table1933
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table1987
- GCC_except_table2049
- GCC_except_table2074
- GCC_except_table2077
- GCC_except_table2088
- GCC_except_table2094
- GCC_except_table2097
- GCC_except_table2113
- GCC_except_table2116
- GCC_except_table2152
- GCC_except_table2163
- GCC_except_table2165
- GCC_except_table2168
- GCC_except_table2171
- GCC_except_table2186
- GCC_except_table2193
- GCC_except_table2195
- GCC_except_table2199
- GCC_except_table2200
- GCC_except_table2205
- GCC_except_table2207
- GCC_except_table2212
- GCC_except_table2217
- GCC_except_table2224
- GCC_except_table2229
- GCC_except_table2261
- GCC_except_table2278
- GCC_except_table2387
- GCC_except_table2407
- GCC_except_table2409
- GCC_except_table2648
- GCC_except_table2666
- GCC_except_table3117
- GCC_except_table3120
- GCC_except_table3155
- GCC_except_table3157
- GCC_except_table3177
- GCC_except_table3178
- GCC_except_table3208
- GCC_except_table3219
- GCC_except_table3222
- GCC_except_table3283
- GCC_except_table3305
- GCC_except_table3308
- GCC_except_table3358
- GCC_except_table3361
- GCC_except_table3365
- GCC_except_table3368
- GCC_except_table3382
- GCC_except_table420
- GCC_except_table423
- GCC_except_table424
- GCC_except_table684
- GCC_except_table744
- GCC_except_table756
- GCC_except_table757
- GCC_except_table882
- GCC_except_table893
- _OUTLINED_FUNCTION_74
- _OUTLINED_FUNCTION_75
- _OUTLINED_FUNCTION_76
- _PXGetWallpaperOverlayForLockScreen
- ___109-[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:]_block_invoke
- ___49-[PUWallpaperPosterEditorController _actionsMenu]_block_invoke_6
- ___81-[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]_block_invoke
- ___81-[PUWallpaperPosterEditorController _transitionToDisplayContext:withCoordinator:]_block_invoke_2
- ___89-[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:]_block_invoke
- ___block_descriptor_56_e8_32s40s48w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw48l8s32l8s40l8
- ___swift_closure_destructor.128Tm
- ___swift_memcpy73_8
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACy06PhotosA6UICore0E10AsyncImageVyAA012_ConditionalD0VyAHyACyACyAA0H0VAA18_AspectRatioLayoutVGAA16_OverlayModifierVyACyAmA06_FrameL0VGSgGGAA5ColorVGAWGAD0eg5AssetH8ProviderVGAQGAA11_ClipEffectVyAA16RoundedRectangleVGGA6_GAA4ViewHPA7_AAA9_HPA1_AAA9_HPA0_AAA9_HPyHC_AqA0wN0HPyHCHC_A6_AAA10_HPyHCHC_A6_AAA10_HPyHCHC
- _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:
- _objc_msgSend$_currentDisplaySupportsLandscape
- _objc_msgSend$_detectDisplayContextChangeWithSize:
- _objc_msgSend$_displayContextFromContainerSize:
- _objc_msgSend$_loadContentForDisplayContext:
- _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:
- _objc_msgSend$_transitionToDisplayContext:withCoordinator:
- _objc_msgSend$currentEditViewModel
- _objc_msgSend$editConfigurationsPerDisplay
- _objc_msgSend$startTimedProgressWithExpectedDuration:showText:
- _symbolic So7UIImageC
- _symbolic So7UIImageCSg
- _symbolic _____yAAyAAy_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG_____y_____GGAUG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV AA11_ClipEffectV AA16RoundedRectangleV
- _symbolic _____yAAy__________G_____GSg 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameH0V
- _symbolic _____yAAy__________G_____yAAyAD_____GSgGG 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameH0V
- _symbolic _____yAAy_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG_____y_____GG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV AA11_ClipEffectV AA16RoundedRectangleV
- _symbolic _____y_____yABy__________G_____GSgG 7SwiftUI16_OverlayModifierV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameJ0V
- _symbolic _____y_____yABy_____yACy__________G_____yACyAF_____GSgGG_____GAMG_____G 17PhotosSwiftUICore0A10AsyncImageV 0B2UI19_ConditionalContentV AD08ModifiedH0V AD0E0V AD18_AspectRatioLayoutV AD16_OverlayModifierV AD06_FrameL0V AD5ColorV AA0ad5AssetE8ProviderV
- _symbolic _____y_____y_____yACyAAyAAy__________G_____yAAyAF_____GSgGG_____GAMG_____GAHG 7SwiftUI15ModifiedContentV 06PhotosA6UICore0E10AsyncImageV AA012_ConditionalD0V AA0H0V AA18_AspectRatioLayoutV AA16_OverlayModifierV AA06_FrameL0V AA5ColorV AD0eg5AssetH8ProviderV
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
+ "Initial display context: %{public}@ (landscape=%d)"
+ "Initializing display context: bounds %.0f×%.0f, canvas %.0f×%.0f, embedded=%d, callServices=%d%{public}@"
+ "Layer stack was baked for %.0fx%.0f but display %{public}@ is %.0fx%.0f; re-rendering"
+ "Poster retains %.0f%% of its saved crop on this display (saved for %{public}@, display portrait %{public}@ landscape %{public}@)"
+ "Reframed poster: portrait visible %{public}@, landscape visible %{public}@, decoded %zu×%zu"
+ "Transitioning to display context: %{public}@ (landscape=%d)"
+ "asset.resource"
+ "input.segmentation"
- "Attempt to load wallpaper from poster url: %{public}@"
- "Display context change detected from bounds: %{public}@ -> %{public}@"
- "Initial display context from view frame: %{public}@"
- "LemonadeSearchCentralizedFeedbackFCSTitle"
- "Set initial display context from bounds: %{public}@"
- "Transitioning to display context: %{public}@"
- "exclamationmark.bubble"
```
