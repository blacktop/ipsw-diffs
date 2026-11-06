## PhotosPosterUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosPosterUI.framework/Versions/A/PhotosPosterUI`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0xa7fe0
-  __TEXT.__objc_methlist: 0x9a70
-  __TEXT.__const: 0x2690
-  __TEXT.__constg_swiftt: 0x119c
-  __TEXT.__swift5_typeref: 0x4c14
+916.58.114.0.0
+  __TEXT.__text: 0xaad4c
+  __TEXT.__objc_methlist: 0x9dc0
+  __TEXT.__const: 0x2670
+  __TEXT.__constg_swiftt: 0x1178
+  __TEXT.__swift5_typeref: 0x4b64
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xb51
-  __TEXT.__swift5_fieldmd: 0x870
+  __TEXT.__swift5_reflstr: 0xb01
+  __TEXT.__swift5_fieldmd: 0x85c
   __TEXT.__swift5_assocty: 0x278
   __TEXT.__swift5_proto: 0x94
-  __TEXT.__swift5_types: 0x90
-  __TEXT.__cstring: 0x5be6
-  __TEXT.__swift5_capture: 0x4b0
-  __TEXT.__oslogstring: 0x3ca1
-  __TEXT.__gcc_except_tab: 0x15cc
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__cstring: 0x5ca5
+  __TEXT.__swift5_capture: 0x500
+  __TEXT.__oslogstring: 0x40b1
+  __TEXT.__gcc_except_tab: 0x15c8
   __TEXT.__ustring: 0xdc
-  __TEXT.__unwind_info: 0x2af0
-  __TEXT.__eh_frame: 0x17c
+  __TEXT.__unwind_info: 0x2be8
+  __TEXT.__eh_frame: 0x1b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2800
-  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68f8
+  __DATA_CONST.__objc_selrefs: 0x6a98
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0xf50
-  __AUTH_CONST.__const: 0x2430
-  __AUTH_CONST.__cfstring: 0x3f80
-  __AUTH_CONST.__objc_const: 0x104b0
+  __DATA_CONST.__got: 0xf98
+  __AUTH_CONST.__const: 0x24f0
+  __AUTH_CONST.__cfstring: 0x4060
+  __AUTH_CONST.__objc_const: 0x10b38
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x15a0
+  __AUTH_CONST.__auth_got: 0x1608
   __AUTH_CONST.__auth_ptr: 0x6e0
-  __AUTH.__objc_data: 0x2988
-  __AUTH.__data: 0x738
-  __DATA.__objc_ivar: 0xa5c
-  __DATA.__data: 0x2590
+  __AUTH.__objc_data: 0x2b78
+  __AUTH.__data: 0x700
+  __DATA.__objc_ivar: 0xa9c
+  __DATA.__data: 0x25d0
   __DATA.__bss: 0x1600
   __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4640
-  Symbols:   9518
-  CStrings:  1020
+  Functions: 4722
+  Symbols:   9695
+  CStrings:  1040
 
Symbols:
+ +[PUWallpaperPosterDisplayFallback shouldReframeLayerStack:deviceConfiguration:]
+ +[PUWallpaperPosterDisplayFallback substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:]
+ -[PUParallaxImageLayerContentView _shouldAnimatePropertyWithKey:]
+ -[PUParallaxImageLayerView blurLayer]
+ -[PUParallaxLayerLayoutInfo viewBoundsSize]
+ -[PUParallaxLayerView blurLayer]
+ -[PUPosterGlobalEditProperties .cxx_destruct]
+ -[PUPosterGlobalEditProperties initWithEditViewModel:]
+ -[PUPosterGlobalEditProperties initWithStyle:spatialPhotoEnabled:settlingEffectEnabled:depthEnabled:userAdjustedVisibleFrame:]
+ -[PUPosterGlobalEditProperties isDepthEnabled]
+ -[PUPosterGlobalEditProperties isSettlingEffectEnabled]
+ -[PUPosterGlobalEditProperties isSpatialPhotoEnabled]
+ -[PUPosterGlobalEditProperties style]
+ -[PUPosterGlobalEditProperties userAdjustedVisibleFrame]
+ -[PUWallpaperCachedLayerStack .cxx_destruct]
+ -[PUWallpaperCachedLayerStack layerStack]
+ -[PUWallpaperCachedLayerStack options]
+ -[PUWallpaperCachedLayerStack setLayerStack:]
+ -[PUWallpaperCachedLayerStack setOptions:]
+ -[PUWallpaperCachedLayerStack setSpatialScenes:]
+ -[PUWallpaperCachedLayerStack setWallpaperURL:]
+ -[PUWallpaperCachedLayerStack spatialScenes]
+ -[PUWallpaperCachedLayerStack wallpaperURL]
+ -[PUWallpaperPosterController _cacheLayerStack:forWallpaperURL:displayContext:options:]
+ -[PUWallpaperPosterController _cachedLayerStackForWallpaperURL:displayContext:options:]
+ -[PUWallpaperPosterController _deviceConfigurationForCurrentDisplay]
+ -[PUWallpaperPosterController _deviceConfigurationForDisplayContext:]
+ -[PUWallpaperPosterController _displayContextForScaledSize:scale:primary:]
+ -[PUWallpaperPosterController _invalidateLayerStackCache]
+ -[PUWallpaperPosterController _retainSpatialSceneForCurrentDisplay]
+ -[PUWallpaperPosterController _savedStyleForPosterMedia:displayContext:]
+ -[PUWallpaperPosterController _shouldReframeLayerStack:displayContext:]
+ -[PUWallpaperPosterController _substituteLayerStackForBakedLayerStack:wallpaperURL:displayContext:]
+ -[PUWallpaperPosterController _wantsLayerStackCache]
+ -[PUWallpaperPosterController forcedPosterUpgradeReason]
+ -[PUWallpaperPosterController setForcedPosterUpgradeReason:]
+ -[PUWallpaperPosterEditModel _updateCurrentEditViewModel]
+ -[PUWallpaperPosterEditModel _updateGlobalEditProperties]
+ -[PUWallpaperPosterEditModel editConfigurationsPerDisplayMergedWith:posterWideConfiguration:]
+ -[PUWallpaperPosterEditModel globalEditProperties]
+ -[PUWallpaperPosterEditModel invalidateInactiveEditViewModels]
+ -[PUWallpaperPosterEditModel observable:didChange:context:]
+ -[PUWallpaperPosterEditModel setCurrentEditViewModel:]
+ -[PUWallpaperPosterEditModel setGlobalEditProperties:]
+ -[PUWallpaperPosterEditViewModel applyGlobalEditProperties:]
+ -[PUWallpaperPosterEditorController _canAdoptBakedLayoutAtWallpaperURL:]
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
+ GCC_except_table1003
+ GCC_except_table1039
+ GCC_except_table1047
+ GCC_except_table1057
+ GCC_except_table1077
+ GCC_except_table1079
+ GCC_except_table1109
+ GCC_except_table1386
+ GCC_except_table1387
+ GCC_except_table151
+ GCC_except_table1523
+ GCC_except_table1524
+ GCC_except_table1548
+ GCC_except_table161
+ GCC_except_table1745
+ GCC_except_table1750
+ GCC_except_table1814
+ GCC_except_table1822
+ GCC_except_table1857
+ GCC_except_table1858
+ GCC_except_table1884
+ GCC_except_table1888
+ GCC_except_table1893
+ GCC_except_table1897
+ GCC_except_table1899
+ GCC_except_table1902
+ GCC_except_table1905
+ GCC_except_table1908
+ GCC_except_table1917
+ GCC_except_table1956
+ GCC_except_table2018
+ GCC_except_table2043
+ GCC_except_table2046
+ GCC_except_table2057
+ GCC_except_table2063
+ GCC_except_table2066
+ GCC_except_table2127
+ GCC_except_table2129
+ GCC_except_table2133
+ GCC_except_table2136
+ GCC_except_table2148
+ GCC_except_table2150
+ GCC_except_table2154
+ GCC_except_table2155
+ GCC_except_table2160
+ GCC_except_table2162
+ GCC_except_table2166
+ GCC_except_table2170
+ GCC_except_table2172
+ GCC_except_table2179
+ GCC_except_table2213
+ GCC_except_table2232
+ GCC_except_table2341
+ GCC_except_table2361
+ GCC_except_table2363
+ GCC_except_table2603
+ GCC_except_table2621
+ GCC_except_table3073
+ GCC_except_table3076
+ GCC_except_table3113
+ GCC_except_table3133
+ GCC_except_table3134
+ GCC_except_table3164
+ GCC_except_table3175
+ GCC_except_table3178
+ GCC_except_table3239
+ GCC_except_table3261
+ GCC_except_table3264
+ GCC_except_table422
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table740
+ GCC_except_table752
+ GCC_except_table753
+ OBJC_IVAR_$_PUPosterGlobalEditProperties._depthEnabled
+ OBJC_IVAR_$_PUPosterGlobalEditProperties._settlingEffectEnabled
+ OBJC_IVAR_$_PUPosterGlobalEditProperties._spatialPhotoEnabled
+ OBJC_IVAR_$_PUPosterGlobalEditProperties._style
+ OBJC_IVAR_$_PUPosterGlobalEditProperties._userAdjustedVisibleFrame
+ OBJC_IVAR_$_PUWallpaperCachedLayerStack._layerStack
+ OBJC_IVAR_$_PUWallpaperCachedLayerStack._options
+ OBJC_IVAR_$_PUWallpaperCachedLayerStack._spatialScenes
+ OBJC_IVAR_$_PUWallpaperCachedLayerStack._wallpaperURL
+ OBJC_IVAR_$_PUWallpaperPosterController._forcedPosterUpgradeReason
+ OBJC_IVAR_$_PUWallpaperPosterController._layerStacksByDisplayContext
+ OBJC_IVAR_$_PUWallpaperPosterController._spatialRendererReuseAssertion
+ OBJC_IVAR_$_PUWallpaperPosterEditModel._currentEditViewModel
+ OBJC_IVAR_$_PUWallpaperPosterEditModel._globalEditProperties
+ OBJC_IVAR_$_PUWallpaperPosterEditorController._transitioningContainerSize
+ OBJC_IVAR_$__PUWallpaperPosterEditorDebugPreferences._pu_contextLinkingMode
+ _CGImageRetain
+ _CGRectIntegral
+ _CGSizeCreateDictionaryRepresentation
+ _CVPixelBufferGetHeight
+ _CVPixelBufferGetWidth
+ _OBJC_CLASS_$_PFParallaxLayerStack
+ _OBJC_CLASS_$_PUParallaxImageLayerContentView
+ _OBJC_CLASS_$_PUPosterGlobalEditProperties
+ _OBJC_CLASS_$_PUSpatialPhotoRendererReuseAssertion
+ _OBJC_CLASS_$_PUWallpaperCachedLayerStack
+ _OBJC_CLASS_$_PUWallpaperPosterDisplayFallback
+ _OBJC_METACLASS_$_PUParallaxImageLayerContentView
+ _OBJC_METACLASS_$_PUPosterGlobalEditProperties
+ _OBJC_METACLASS_$_PUSpatialPhotoRendererReuseAssertion
+ _OBJC_METACLASS_$_PUWallpaperCachedLayerStack
+ _OBJC_METACLASS_$_PUWallpaperPosterDisplayFallback
+ _PFFigCreateCVPixelBufferFromURL
+ _PFFigDecodeOptionsWithMaxPixelSize
+ _PFParallaxLayerID_InactiveBackground
+ _PFParallaxZPositionOnlyBackground
+ _PPPosterContextLinkingModeUsingEditingPreferences
+ _PPPosterContextLinkingModeUsingMutableEditingPreferences
+ _PPPosterSetContextLinkingModeUsingMutableEditingPreferences
+ _PUWallpaperCacheURLForWallpaperURL
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
+ __DATA_PUSpatialPhotoRendererReuseAssertion
+ __INSTANCE_METHODS_PUSpatialPhotoRendererReuseAssertion
+ __METACLASS_DATA_PUSpatialPhotoRendererReuseAssertion
+ __OBJC_$_CLASS_METHODS_PUWallpaperPosterDisplayFallback
+ __OBJC_$_INSTANCE_METHODS_PUParallaxImageLayerContentView
+ __OBJC_$_INSTANCE_METHODS_PUPosterGlobalEditProperties
+ __OBJC_$_INSTANCE_METHODS_PUWallpaperCachedLayerStack
+ __OBJC_$_INSTANCE_VARIABLES_PUPosterGlobalEditProperties
+ __OBJC_$_INSTANCE_VARIABLES_PUWallpaperCachedLayerStack
+ __OBJC_$_PROP_LIST_PUPosterGlobalEditProperties
+ __OBJC_$_PROP_LIST_PUWallpaperCachedLayerStack
+ __OBJC_CLASS_PROTOCOLS_$_PUWallpaperPosterEditModel
+ __OBJC_CLASS_RO_$_PUParallaxImageLayerContentView
+ __OBJC_CLASS_RO_$_PUPosterGlobalEditProperties
+ __OBJC_CLASS_RO_$_PUWallpaperCachedLayerStack
+ __OBJC_CLASS_RO_$_PUWallpaperPosterDisplayFallback
+ __OBJC_METACLASS_RO_$_PUParallaxImageLayerContentView
+ __OBJC_METACLASS_RO_$_PUPosterGlobalEditProperties
+ __OBJC_METACLASS_RO_$_PUWallpaperCachedLayerStack
+ __OBJC_METACLASS_RO_$_PUWallpaperPosterDisplayFallback
+ ___103-[PUWallpaperPosterEditorController _renderLayerStackForDisplayContext:segmentationItem:containerSize:]_block_invoke
+ ___123-[PUWallpaperPosterEditorController _createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:]_block_invoke
+ ___60-[PUWallpaperPosterEditViewModel applyGlobalEditProperties:]_block_invoke
+ ___64-[PUWallpaperPosterEditorController _handleOutfillButtonTapped:]_block_invoke_2
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke
+ ___95-[PUWallpaperPosterEditorController _transitionToDisplayContext:containerSize:withCoordinator:]_block_invoke_2
+ ___block_descriptor_64_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_72_e8_32s40s48w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___swift_memcpy65_8
+ __swift_closure_destructor.121Tm
+ _objc_msgSend$_cacheLayerStack:forWallpaperURL:displayContext:options:
+ _objc_msgSend$_cachedLayerStackForWallpaperURL:displayContext:options:
+ _objc_msgSend$_canAdoptBakedLayoutAtWallpaperURL:
+ _objc_msgSend$_compoundLayerStack:matchesDisplayContext:
+ _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:containerSize:
+ _objc_msgSend$_deviceConfigurationForCurrentDisplay
+ _objc_msgSend$_deviceConfigurationForDisplayContext:
+ _objc_msgSend$_displayContextForCurrentContainer
+ _objc_msgSend$_displayContextForScaledSize:scale:primary:
+ _objc_msgSend$_displayContextForSize:
+ _objc_msgSend$_displayScale
+ _objc_msgSend$_effectiveDeviceOrientation
+ _objc_msgSend$_invalidateLayerStackCache
+ _objc_msgSend$_loadContentForDisplayContext:containerSize:
+ _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:containerSize:
+ _objc_msgSend$_retainSpatialSceneForCurrentDisplay
+ _objc_msgSend$_savedStyleForPosterMedia:displayContext:
+ _objc_msgSend$_shouldReframeLayerStack:displayContext:
+ _objc_msgSend$_substituteLayerStackForBakedLayerStack:wallpaperURL:displayContext:
+ _objc_msgSend$_transitionToDisplayContext:containerSize:withCoordinator:
+ _objc_msgSend$_updateCurrentEditViewModel
+ _objc_msgSend$_updateGlobalEditProperties
+ _objc_msgSend$_wantsLayerStackCache
+ _objc_msgSend$applyGlobalEditProperties:
+ _objc_msgSend$canvasSize
+ _objc_msgSend$contextLinkingMode
+ _objc_msgSend$deviceConfigurationForDisplayContext:
+ _objc_msgSend$editConfigurationsPerDisplayMergedWith:posterWideConfiguration:
+ _objc_msgSend$ensureLayoutsForAllDisplayContexts:preservesLayout:completion:
+ _objc_msgSend$forcedPosterUpgradeReason
+ _objc_msgSend$globalEditProperties
+ _objc_msgSend$imageFileURL
+ _objc_msgSend$initWithEditViewModel:
+ _objc_msgSend$initWithImage:frame:zPosition:identifier:
+ _objc_msgSend$initWithLayers:layout:depthEnabled:parallaxDisabled:clockAreaLuminance:settlingEffectEnabled:spatialPhotoEnabled:userAdjustedVisibleFrame:
+ _objc_msgSend$initWithStyle:spatialPhotoEnabled:settlingEffectEnabled:depthEnabled:userAdjustedVisibleFrame:
+ _objc_msgSend$invalidateInactiveEditViewModels
+ _objc_msgSend$isAnyFrameUsingHeadroom
+ _objc_msgSend$isSegmentedStyle:
+ _objc_msgSend$layoutByUpdatingInactiveFrame:
+ _objc_msgSend$layoutByUpgradingToConfiguration:
+ _objc_msgSend$length
+ _objc_msgSend$loadFromArchiveURL:error:
+ _objc_msgSend$px_canvasSize
+ _objc_msgSend$renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setContextLinkingMode:
+ _objc_msgSend$setCurrentEditViewModel:
+ _objc_msgSend$setForcedPosterUpgradeReason:
+ _objc_msgSend$setGlobalEditProperties:
+ _objc_msgSend$setPu_contextLinkingMode:
+ _objc_msgSend$setSpatialScenes:
+ _objc_msgSend$setSupportsLandscapeConfiguration:
+ _objc_msgSend$setTransitioningContainerSize:
+ _objc_msgSend$setWallpaperURL:
+ _objc_msgSend$shouldReframeLayerStack:deviceConfiguration:
+ _objc_msgSend$substituteLayerStackForWallpaperURL:bakedLayerStack:deviceConfiguration:
+ _objc_msgSend$transitioningContainerSize
+ _objc_msgSend$viewBoundsSize
+ _objc_msgSend$wallpaperURL
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
+ _symbolic SaySo6UIViewCGz_Xx
+ _symbolic _____ 14PhotosPosterUI36PUSpatialPhotoRendererReuseAssertionC
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
- GCC_except_table2094
- GCC_except_table2096
- GCC_except_table2100
- GCC_except_table2101
- GCC_except_table2106
- GCC_except_table2108
- GCC_except_table2113
- GCC_except_table2118
- GCC_except_table2125
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
- GCC_except_table3097
- GCC_except_table3108
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
- ___block_descriptor_72_e8_32s40s48s56w_e51_v24?0"PFWallpaperCompoundLayerStack"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32r40r_e5_v8?0lr32l8r40l8
- ___swift_memcpy73_8
- __swift_closure_destructor.129Tm
- _objc_msgSend$_createAndSetViewModelForDisplayContext:withLayerStack:segmentationItem:
- _objc_msgSend$_currentDisplaySupportsLandscape
- _objc_msgSend$_detectDisplayContextChangeWithSize:
- _objc_msgSend$_displayContextFromContainerSize:
- _objc_msgSend$_loadContentForDisplayContext:
- _objc_msgSend$_renderLayerStackForDisplayContext:segmentationItem:
- _objc_msgSend$_transitionToDisplayContext:withCoordinator:
- _objc_msgSend$displayContextWithSize:scale:
- _objc_msgSend$editConfigurationsPerDisplay
- _objc_msgSend$ensureLayoutsForAllDisplayContexts:completion:
- _objc_msgSend$renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:
- _objc_msgSend$screenScale
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
+ "-%@"
+ "Attempt to load wallpaper for context %{public}@ from poster url: %{public}@"
+ "CancelOutfill"
+ "Cannot initialize display context: neither backgroundView bounds nor canvas size are known yet"
+ "Cannot reframe poster: failed to load its asset resource: %{public}@"
+ "Cannot reframe poster: its asset resource holds no full-size image"
+ "Cannot resolve initial display context: neither view bounds nor canvas size are known"
+ "Contact poster resources were laid out for the lock screen, re-segmenting"
+ "ExtendOutfill"
+ "Failed to decode poster asset for display fallback, code: %d"
+ "Failed to load baked layer stack for contact poster, re-segmenting: %{public}@"
+ "Forcing depth off for stand-in layout on display %{public}@"
+ "GlobalEditPropertiesObservationContext"
+ "Initial display context: %{public}@ (landscape=%d)"
+ "Initialized display context: %{public}@ (landscape=%d)"
+ "Initializing display context: bounds %.0f×%.0f, canvas %.0f×%.0f, embedded=%d, callServices=%d%{public}@"
+ "Layer stack was baked for %.0fx%.0f but display %{public}@ is %.0fx%.0f; re-rendering"
+ "Layout configuration mismatch detected, updating layout for display %{public}@"
+ "Not reframing poster: it has the %{public}@ photo style applied"
+ "Poster retains %.0f%% of its saved crop on this display (saved for %{public}@, display portrait %{public}@ landscape %{public}@)"
+ "Reframed poster: portrait visible %{public}@, landscape visible %{public}@, decoded %zu×%zu"
+ "Reusing cached layer stack for context %{public}@"
+ "Transitioning to display context: %{public}@ (landscape=%d)"
+ "Triggering poster upgrade: %{public}@"
+ "Warmup load succeeded (complete: %{public}@), screen: %.0f×%.0f, image: %.0f×%.0f"
+ "asset.resource"
+ "filters.gaussianBlur.inputBounds"
+ "input.segmentation"
- "Attempt to load wallpaper from poster url: %{public}@"
- "Display context change detected from bounds: %{public}@ -> %{public}@"
- "Forcing depth off for not-yet-migrated poster on landscape-capable display"
- "Initial display context from view frame: %{public}@"
- "Initialized display context: %{public}@"
- "Layout configuration mismatch detected, updating layout for current device"
- "Set initial display context from bounds: %{public}@"
- "Transitioning to display context: %{public}@"
- "Warmup load succeeded, screen: %.0f×%.0f, image: %.0f×%.0f"
```
