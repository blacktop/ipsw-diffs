## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-146.102.0.0.0
-  __TEXT.__text: 0x31e3a8
-  __TEXT.__auth_stubs: 0x2cc0
-  __TEXT.__objc_methlist: 0x3b404
+155.0.0.0.0
+  __TEXT.__text: 0x31ee98
+  __TEXT.__auth_stubs: 0x2c80
+  __TEXT.__objc_methlist: 0x3b514
   __TEXT.__const: 0x6284
-  __TEXT.__cstring: 0x1ac2f
-  __TEXT.__gcc_except_tab: 0x3d9c
-  __TEXT.__oslogstring: 0xd240
-  __TEXT.__dlopen_cstrs: 0x52e
-  __TEXT.__ustring: 0x566
+  __TEXT.__cstring: 0x1b25f
+  __TEXT.__gcc_except_tab: 0x3d0c
+  __TEXT.__oslogstring: 0xd5b0
+  __TEXT.__dlopen_cstrs: 0x4c6
+  __TEXT.__ustring: 0x620
   __TEXT.__swift5_typeref: 0x179c
   __TEXT.__constg_swiftt: 0x83c
   __TEXT.__swift5_reflstr: 0x46a

   __TEXT.__swift5_capture: 0xf98
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe118
+  __TEXT.__unwind_info: 0xe128
   __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6d24
-  __TEXT.__objc_methname: 0x97d3c
-  __TEXT.__objc_methtype: 0x1901f
-  __TEXT.__objc_stubs: 0x581c0
+  __TEXT.__objc_classname: 0x6d25
+  __TEXT.__objc_methname: 0x982dc
+  __TEXT.__objc_methtype: 0x1906b
+  __TEXT.__objc_stubs: 0x58480
   __DATA_CONST.__got: 0x2220
-  __DATA_CONST.__const: 0x95b0
+  __DATA_CONST.__const: 0x9528
   __DATA_CONST.__objc_classlist: 0x1248
-  __DATA_CONST.__objc_catlist: 0x118
+  __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b330
-  __DATA_CONST.__objc_protorefs: 0x140
+  __DATA_CONST.__objc_selrefs: 0x1b468
+  __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe10
   __DATA_CONST.__objc_arraydata: 0x6d8
-  __AUTH_CONST.__auth_got: 0x1670
-  __AUTH_CONST.__const: 0x6238
-  __AUTH_CONST.__cfstring: 0x15720
-  __AUTH_CONST.__objc_const: 0x54248
+  __AUTH_CONST.__auth_got: 0x1650
+  __AUTH_CONST.__const: 0x61f8
+  __AUTH_CONST.__cfstring: 0x157c0
+  __AUTH_CONST.__objc_const: 0x542c8
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x5f88
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3a3c
+  __DATA.__objc_ivar: 0x3a58
   __DATA.__data: 0x8898
-  __DATA.__bss: 0x21f8
+  __DATA.__bss: 0x2208
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x5ca8
   __DATA_DIRTY.__data: 0xd8
-  __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5E71AF27-FCD0-312D-A2CB-130BD7AD09A3
-  Functions: 22182
-  Symbols:   63348
-  CStrings:  30139
+  UUID: 4E20D5A7-E58E-3465-8E50-740F2C1DE7BB
+  Functions: 22224
+  Symbols:   63398
+  CStrings:  30236
 
Symbols:
+ +[SBIconImageView iconUpdateAnimationSettings]
+ +[SBIconProgressView _pieImageAtFraction:scale:]
+ +[SBIconProgressView _pieImageAtFraction:scale:].cold.1
+ +[SBIconProgressView _pieImagesMemoryPoolForScale:]
+ -[NSIndexSet(SBHAdditions) sbh_indexSetByAddingIndexes:]
+ -[SBHAddWidgetButton _addSymbolImageWithTintColor:]
+ -[SBHAddWidgetButton backgroundView]
+ -[SBHAddWidgetButton setBackgroundView:]
+ -[SBHIconManager performanceFlagDisableLightAngleUpdatesAssertion]
+ -[SBHIconManager primaryWindowScene]
+ -[SBHIconManager setPerformanceFlagDisableLightAngleUpdatesAssertion:]
+ -[SBHIconSettings lightAngleInitialDistanceThreshold]
+ -[SBHIconSettings lightAngleInitialVelocityThreshold]
+ -[SBHIconSettings setLightAngleInitialDistanceThreshold:]
+ -[SBHIconSettings setLightAngleInitialVelocityThreshold:]
+ -[SBHLibrarySearchController legibilitySettings]
+ -[SBHLibrarySearchController setLegibilitySettings:]
+ -[SBHLibraryViewController _updateSearchControllerLegibility]
+ -[SBHLightSourceManager accumulatedDistance]
+ -[SBHLightSourceManager initialDistanceThreshold]
+ -[SBHLightSourceManager initialLightDirection]
+ -[SBHLightSourceManager initialVelocityThreshold]
+ -[SBHLightSourceManager lastLightDirection2]
+ -[SBHLightSourceManager lastLightTimestamp2]
+ -[SBHLightSourceManager lastLightTimestamp]
+ -[SBHLightSourceManager pushLightAngleUpdateWithDirection:intensity:angle:]
+ -[SBHLightSourceManager setAccumulatedDistance:]
+ -[SBHLightSourceManager setInitialDistanceThreshold:]
+ -[SBHLightSourceManager setInitialLightDirection:]
+ -[SBHLightSourceManager setInitialVelocityThreshold:]
+ -[SBHLightSourceManager setLastLightDirection2:]
+ -[SBHLightSourceManager setLastLightTimestamp2:]
+ -[SBHLightSourceManager setLastLightTimestamp:]
+ -[SBHSearchTextField legibilitySettings]
+ -[SBHSearchTextField setLegibilitySettings:]
+ -[SBHShadowedWidgetView setShadowHidden:]
+ -[SBHWidgetIconStyleConfiguration backdropGroupName]
+ -[SBHWidgetIconStyleConfiguration initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:]
+ -[SBHWidgetIconStyleConfiguration initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:]
+ -[SBHWidgetIconStyleConfiguration initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:]
+ -[SBHWidgetIconStyleConfiguration setBackdropGroupName:]
+ -[SBHWidgetStyleManager backdropGroupNameIfAvailable]
+ -[SBHWidgetWrapperView backdropGroupName]
+ -[SBHWidgetWrapperView setBackdropGroupName:]
+ -[SBHWidgetWrapperView setShadowHidden:]
+ -[SBIconImageView areLightAngleUpdatesAllowed]
+ -[SBIconImageView beginLightAngleUpdatesIfAllowed]
+ -[SBIconListView _updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:]
+ -[SBIconListView contentVisibilityForIcon:]
+ -[SBIconListView gridCellIndexesToIncludeInLayout]
+ -[SBIconListView prefetchedGridCellIndexes]
+ -[SBIconListView prefetchedIcons]
+ -[SBIconListView setCellVisibility:visibleGridCellIndexes:prefetchedGridCellIndexes:]
+ -[SBIconListView setPrefetchedGridCellIndexes:]
+ -[SBIconListView setVisibleGridCellIndexes:prefetchedGridCellIndexes:]
+ -[SBIconViewCustomImageViewController backdropGroupNameForActiveDataSource:]
+ -[SBScaleIconZoomAnimator _prepareAnimation].cold.1
+ -[SBScaleIconZoomAnimator _prepareAnimation].cold.2
+ -[SBScaleIconZoomAnimator _prepareAnimation].cold.3
+ -[_SBHLibraryCategoryStackViewBackgroundView backdropGroupName]
+ -[_SBHLibraryCategoryStackViewBackgroundView initWithFrame:]
+ -[_SBHLibraryCategoryStackViewBackgroundView setBackdropGroupName:]
+ -[_SBHShadowView _updateBackdropCapture]
+ -[_SBHShadowView backdropGroupName]
+ -[_SBHShadowView setBackdropGroupName:]
+ GCC_except_table1025
+ GCC_except_table1048
+ GCC_except_table120
+ GCC_except_table140
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table233
+ GCC_except_table239
+ GCC_except_table244
+ GCC_except_table255
+ GCC_except_table273
+ GCC_except_table280
+ GCC_except_table297
+ GCC_except_table309
+ GCC_except_table337
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table373
+ GCC_except_table395
+ GCC_except_table398
+ GCC_except_table403
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table434
+ GCC_except_table447
+ GCC_except_table485
+ GCC_except_table505
+ GCC_except_table510
+ GCC_except_table532
+ GCC_except_table54
+ GCC_except_table559
+ GCC_except_table563
+ GCC_except_table591
+ GCC_except_table618
+ GCC_except_table650
+ GCC_except_table679
+ GCC_except_table689
+ GCC_except_table692
+ GCC_except_table701
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table718
+ GCC_except_table723
+ GCC_except_table726
+ GCC_except_table729
+ GCC_except_table732
+ GCC_except_table826
+ GCC_except_table882
+ GCC_except_table952
+ GCC_except_table972
+ GCC_except_table989
+ _OBJC_CLASS_$_CHSMutableGlassOptions
+ _OBJC_CLASS_$_MTStylingProvidingSolidColorView
+ _OBJC_IVAR_$_SBHAddWidgetButton._backgroundView
+ _OBJC_IVAR_$_SBHIconManager._performanceFlagDisableLightAngleUpdatesAssertion
+ _OBJC_IVAR_$_SBHIconSettings._lightAngleInitialDistanceThreshold
+ _OBJC_IVAR_$_SBHIconSettings._lightAngleInitialVelocityThreshold
+ _OBJC_IVAR_$_SBHLibrarySearchController._legibilitySettings
+ _OBJC_IVAR_$_SBHLightSourceManager._accumulatedDistance
+ _OBJC_IVAR_$_SBHLightSourceManager._initialDistanceThreshold
+ _OBJC_IVAR_$_SBHLightSourceManager._initialLightDirection
+ _OBJC_IVAR_$_SBHLightSourceManager._initialVelocityThreshold
+ _OBJC_IVAR_$_SBHLightSourceManager._lastLightDirection2
+ _OBJC_IVAR_$_SBHLightSourceManager._lastLightTimestamp
+ _OBJC_IVAR_$_SBHLightSourceManager._lastLightTimestamp2
+ _OBJC_IVAR_$_SBHSearchTextField._legibilitySettings
+ _OBJC_IVAR_$_SBHWidgetIconStyleConfiguration._backdropGroupName
+ _OBJC_IVAR_$_SBHWidgetWrapperView._backdropGroupName
+ _OBJC_IVAR_$_SBIconListView._prefetchedGridCellIndexes
+ _OBJC_IVAR_$__SBHLibraryCategoryStackViewBackgroundView._backdropGroupName
+ _OBJC_IVAR_$__SBHShadowView._backdropCaptureLayer
+ _OBJC_IVAR_$__SBHShadowView._backdropGroupName
+ _SBH3DPointDistance
+ _SBH3DPointVelocity
+ _SBH3DPointVelocityMagnitude
+ _SBH3DVelocityMagnitude
+ _SBHPerformanceFlagEnabled
+ _SBHPerformanceFlagEnabled.cold.1
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSIndexSet_$_SBHAdditions
+ __OBJC_$_CATEGORY_NSIndexSet_$_SBHAdditions
+ __OBJC_$_PROP_LIST__SBHShadowView
+ __OBJC_PROTOCOL_REFERENCE_$_SBIconViewCustomImageViewControlling
+ __SBHPerformanceFlagsHomeScreenDefaults.homeScreenDefaults
+ __SBHPerformanceFlagsHomeScreenDefaults.onceToken
+ ___121-[SBFolderIconImageSharedCache updateCachedImagesForFolderIcon:afterChangeToContainedForIcon:imageAppearance:updateType:]_block_invoke.176
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1094
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1096
+ ___38-[SBFolderView _updateScrollingState:]_block_invoke.95
+ ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.781
+ ___48+[SBIconProgressView _pieImageAtFraction:scale:]_block_invoke
+ ___48+[SBIconProgressView _pieImageAtFraction:scale:]_block_invoke_2
+ ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.971
+ ___56-[SBHAddWidgetSheetAppCollectionViewCell initWithFrame:]_block_invoke
+ ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.234
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.535
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.607
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.610
+ ____SBHPerformanceFlagsHomeScreenDefaults_block_invoke
+ ___block_descriptor_49_e18_B24?0{CGSize=dd}8l
+ ___block_descriptor_97_e8_32s40s48s_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.1016
+ ___block_literal_global.1055
+ ___block_literal_global.1173
+ ___block_literal_global.1226
+ ___block_literal_global.163
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.243
+ ___block_literal_global.250
+ ___block_literal_global.2521
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.309
+ ___block_literal_global.323
+ ___block_literal_global.347
+ ___block_literal_global.372
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.383
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.416
+ ___block_literal_global.50
+ ___block_literal_global.609
+ ___block_literal_global.669
+ ___block_literal_global.797
+ ___block_literal_global.823
+ ___block_literal_global.884
+ ___block_literal_global.91
+ ___block_literal_global.97
+ __pieImageAtFraction:scale:.onceToken
+ __pieImageAtFraction:scale:.pieImageCache
+ __pieImagesMemoryPoolForScale:.__pools
+ _block_copy_helper.19
+ _block_copy_helper.29
+ _block_copy_helper.39
+ _block_copy_helper.49
+ _block_copy_helper.59
+ _block_descriptor.21
+ _block_descriptor.31
+ _block_descriptor.41
+ _block_descriptor.51
+ _block_descriptor.61
+ _block_destroy_helper.20
+ _block_destroy_helper.30
+ _block_destroy_helper.40
+ _block_destroy_helper.50
+ _block_destroy_helper.60
+ _objc_msgSend$_addSymbolImageWithTintColor:
+ _objc_msgSend$_pieImageAtFraction:scale:
+ _objc_msgSend$_pieImagesMemoryPoolForScale:
+ _objc_msgSend$_updateBackdropCapture
+ _objc_msgSend$_updateSearchControllerLegibility
+ _objc_msgSend$_updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:
+ _objc_msgSend$accumulatedDistance
+ _objc_msgSend$areLightAngleUpdatesAllowed
+ _objc_msgSend$backdropGroupNameForActiveDataSource:
+ _objc_msgSend$backdropGroupNameIfAvailable
+ _objc_msgSend$beginLightAngleUpdatesIfAllowed
+ _objc_msgSend$cgColor
+ _objc_msgSend$contentVisibilityForIcon:
+ _objc_msgSend$gridCellIndexesToIncludeInLayout
+ _objc_msgSend$initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:
+ _objc_msgSend$initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:
+ _objc_msgSend$initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:
+ _objc_msgSend$initialDistanceThreshold
+ _objc_msgSend$initialLightDirection
+ _objc_msgSend$initialVelocityThreshold
+ _objc_msgSend$lastLightDirection2
+ _objc_msgSend$lastLightTimestamp
+ _objc_msgSend$lastLightTimestamp2
+ _objc_msgSend$lightAngleInitialDistanceThreshold
+ _objc_msgSend$lightAngleInitialVelocityThreshold
+ _objc_msgSend$prefetchedGridCellIndexes
+ _objc_msgSend$primaryWindowScene
+ _objc_msgSend$primaryWindowSceneForIconManager:
+ _objc_msgSend$pushLightAngleUpdateWithDirection:intensity:angle:
+ _objc_msgSend$sbh_applyAppLibraryPodGlass
+ _objc_msgSend$sbh_applyAppLibraryPodGlassWithGrouping:
+ _objc_msgSend$sbh_applySearchPillGlass
+ _objc_msgSend$sbh_applySearchPillGlassWithGrouping:
+ _objc_msgSend$sbh_hasGlass
+ _objc_msgSend$sbh_indexSetByAddingIndexes:
+ _objc_msgSend$setAccumulatedDistance:
+ _objc_msgSend$setCellVisibility:visibleGridCellIndexes:prefetchedGridCellIndexes:
+ _objc_msgSend$setInitialLightDirection:
+ _objc_msgSend$setLastLightDirection2:
+ _objc_msgSend$setLastLightTimestamp2:
+ _objc_msgSend$setLastLightTimestamp:
+ _objc_msgSend$setLightAngleInitialDistanceThreshold:
+ _objc_msgSend$setLightAngleInitialVelocityThreshold:
+ _objc_msgSend$setShadowHidden:
+ _objc_msgSend$setVisibleGridCellIndexes:prefetchedGridCellIndexes:
+ _objc_msgSend$setWantsHighlightsDisplayAngle:
+ _objc_msgSend$setWantsWhitePointBoost:
+ _objc_msgSend$shouldDisableDockSpecular
+ _objc_msgSend$shouldDisableFolderSpecular
+ _objc_msgSend$shouldDisableGlassDock
+ _objc_msgSend$shouldDisableParallax
+ _objc_msgSend$shouldDisableParallaxOnPageControl
+ _objc_msgSend$shouldDisableSpecularEverywhere
+ _objc_msgSend$shouldDisableWidgetSpecular
+ _objc_msgSend$shouldExcludeAllClearGlassShadows
+ _objc_msgSend$shouldExcludeDockShadow
+ _objc_msgSend$shouldExcludeSearchShadow
+ _objc_msgSend$shouldUseFlatIconsEverywhere
+ _objc_msgSend$systemGrayColor
+ _objc_msgSend$tintedGlassButtonConfiguration
- +[SBDockIconListView defaultFrameForOrientation:]
- +[SBIconProgressView _pieImageAtFraction:]
- +[SBIconProgressView _pieImageAtFraction:].cold.1
- +[SBIconProgressView _pieImagesMemoryPool]
- +[SBIconProgressView _pieImagesMemoryPool].cold.1
- -[SBFloatingDockViewController _backdropGroupNamespace]
- -[SBFolderController additionalPartialPagesToPrefetchIconLayers]
- -[SBFolderControllerConfiguration additionalPartialPagesToPrefetchIconLayers]
- -[SBFolderControllerConfiguration setAdditionalPartialPagesToPrefetchIconLayers:]
- -[SBFolderView additionalPartialPagesToPrefetchIconLayers]
- -[SBFolderView additionalScrollWidthToPrefetchIconLayersInBothDirections]
- -[SBFolderView prefetchIconLayersInListView:inRect:imageAppearance:]
- -[SBHLibraryCategoryStackView backdropGroupNamespace]
- -[SBHLibraryCategoryStackView setBackdropGroupNamespace:]
- -[SBHSearchTextField updateVisualStyling].cold.1
- -[SBHSmartStackElement icon:imageWithInfo:traitCollection:options:]
- -[SBHWidgetIconStyleConfiguration initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:]
- -[SBHWidgetIconStyleConfiguration initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:]
- -[SBHWidgetIconStyleConfiguration initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:]
- -[SBIcon makeIconImageWithInfo:traitCollection:options:]
- -[SBIcon makeIconLayerWithInfo:traitCollection:options:]
- -[SBIconImageView iconUpdateAnimationSettings]
- -[SBIconImageView overrideIconImageAppearance]
- -[SBIconImageView overrideIconImageStyleConfiguration]
- -[SBIconListView _updateVisibleIconViewsWithOldVisibleGridCellIndexes:metrics:]
- -[SBIconListView overrideIconImageAppearance]
- -[SBIconListView overrideIconImageStyleConfiguration]
- -[SBIconListView setCellVisibility:visibleGridCellIndexes:]
- -[SBIconListView setOverrideIconImageAppearance:]
- -[SBIconListView setOverrideIconImageStyleConfiguration:]
- -[SBIconView effectiveOverrideAccessoryIconImageAppearance]
- -[SBIconView overrideAccessoryIconImageAppearance]
- -[SBIconView overrideIconImageAppearance]
- -[SBIconView overrideIconImageStyleConfiguration]
- -[SBIconView setOverrideAccessoryIconImageAppearance:]
- -[SBIconView setOverrideIconImageAppearance:]
- -[SBIconView setOverrideIconImageStyleConfiguration:]
- -[SBIconView setOverrideImageAppearance:onCustomIconImageViewController:]
- -[SBIconView setOverrideImageStyleConfiguration:onCustomIconImageViewController:]
- -[SBIconView updateAccessoryViewOverrideIconImageAppearance]
- -[SBLeafIcon makeIconLayerWithInfo:traitCollection:options:]
- -[_SBHLibraryCategoryStackViewBackgroundView _setContinuousCornerRadius:]
- -[_SBHLibraryCategoryStackViewBackgroundView materialView]
- -[_SBHLibraryCategoryStackViewBackgroundView setMaterialView:]
- -[_SBHLibraryCategoryStackViewBackgroundView setTintingView:]
- -[_SBHLibraryCategoryStackViewBackgroundView tintingView]
- GCC_except_table1024
- GCC_except_table1047
- GCC_except_table119
- GCC_except_table138
- GCC_except_table175
- GCC_except_table177
- GCC_except_table234
- GCC_except_table238
- GCC_except_table243
- GCC_except_table250
- GCC_except_table251
- GCC_except_table272
- GCC_except_table312
- GCC_except_table340
- GCC_except_table356
- GCC_except_table362
- GCC_except_table377
- GCC_except_table394
- GCC_except_table401
- GCC_except_table425
- GCC_except_table428
- GCC_except_table433
- GCC_except_table446
- GCC_except_table484
- GCC_except_table504
- GCC_except_table509
- GCC_except_table531
- GCC_except_table571
- GCC_except_table590
- GCC_except_table627
- GCC_except_table659
- GCC_except_table678
- GCC_except_table688
- GCC_except_table691
- GCC_except_table700
- GCC_except_table702
- GCC_except_table704
- GCC_except_table706
- GCC_except_table708
- GCC_except_table711
- GCC_except_table713
- GCC_except_table715
- GCC_except_table717
- GCC_except_table722
- GCC_except_table725
- GCC_except_table728
- GCC_except_table731
- GCC_except_table825
- GCC_except_table84
- GCC_except_table881
- GCC_except_table951
- GCC_except_table971
- GCC_except_table988
- _CAColorMatrixConcat
- _CAColorMatrixMakeColorSourceOver
- _CAColorMatrixMakeContrast
- _CAColorMatrixMakeSaturation
- _OBJC_CLASS_$_CHSGlassOptions
- _OBJC_IVAR_$_SBFolderController._additionalPartialPagesToPrefetchIconLayers
- _OBJC_IVAR_$_SBFolderControllerConfiguration._additionalPartialPagesToPrefetchIconLayers
- _OBJC_IVAR_$_SBFolderView._additionalPartialPagesToPrefetchIconLayers
- _OBJC_IVAR_$_SBFolderView._iconLayerPrefetchAssertions
- _OBJC_IVAR_$_SBHLibraryCategoryStackView._backdropGroupNamespace
- _OBJC_IVAR_$_SBIconListView._overrideIconImageAppearance
- _OBJC_IVAR_$_SBIconListView._overrideIconImageStyleConfiguration
- _OBJC_IVAR_$_SBIconView._overrideAccessoryIconImageAppearance
- _OBJC_IVAR_$_SBIconView._overrideIconImageAppearance
- _OBJC_IVAR_$_SBIconView._overrideIconImageStyleConfiguration
- _OBJC_IVAR_$__SBHLibraryCategoryStackViewBackgroundView._materialView
- _OBJC_IVAR_$__SBHLibraryCategoryStackViewBackgroundView._tintingView
- _SBHScreenBounds
- ___121-[SBFolderIconImageSharedCache updateCachedImagesForFolderIcon:afterChangeToContainedForIcon:imageAppearance:updateType:]_block_invoke.177
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1090
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1092
- ___38-[SBFolderView _updateScrollingState:]_block_invoke.100
- ___41-[SBIconView pressesCancelled:withEvent:]_block_invoke
- ___41-[SBIconView touchesCancelled:withEvent:]_block_invoke
- ___42+[SBIconProgressView _pieImageAtFraction:]_block_invoke
- ___42+[SBIconProgressView _pieImageAtFraction:]_block_invoke_2
- ___42+[SBIconProgressView _pieImagesMemoryPool]_block_invoke
- ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.791
- ___49-[SBIconListView setOverrideIconImageAppearance:]_block_invoke
- ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.967
- ___53-[SBHLightSourceManager setUpLightSourceSubscription]_block_invoke_2
- ___57-[SBHLibraryCategoryStackView setBackdropGroupNamespace:]_block_invoke
- ___57-[SBIconListView setOverrideIconImageStyleConfiguration:]_block_invoke
- ___67-[SBFolderView updateVisibleColumnRangeWithIconVisibilityHandling:]_block_invoke_3
- ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.227
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.531
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.603
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.606
- ___block_descriptor_112_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_32_e33_v32?0"SBHIconLayerView"8Q16^B24l
- ___block_descriptor_48_e18_B24?0{CGSize=dd}8l
- ___block_descriptor_56_e8_32s40s48s_e71_v40?0"NSString"8"<BSInvalidatable>"16"SBHIconImageAppearance"24^B32ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8
- ___block_literal_global.1012
- ___block_literal_global.102
- ___block_literal_global.105
- ___block_literal_global.1051
- ___block_literal_global.1169
- ___block_literal_global.1222
- ___block_literal_global.158
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.242
- ___block_literal_global.251
- ___block_literal_global.2556
- ___block_literal_global.269
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.278
- ___block_literal_global.283
- ___block_literal_global.312
- ___block_literal_global.324
- ___block_literal_global.342
- ___block_literal_global.368
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.376
- ___block_literal_global.384
- ___block_literal_global.402
- ___block_literal_global.404
- ___block_literal_global.412
- ___block_literal_global.55
- ___block_literal_global.605
- ___block_literal_global.62
- ___block_literal_global.673
- ___block_literal_global.793
- ___block_literal_global.819
- ___block_literal_global.880
- ___block_literal_global.99
- __pieImageAtFraction:.onceToken
- __pieImageAtFraction:.pieImageCache
- __pieImagesMemoryPool.__pool
- __pieImagesMemoryPool.onceToken
- _block_copy_helper.18
- _block_copy_helper.38
- _block_copy_helper.48
- _block_copy_helper.58
- _block_descriptor.20
- _block_descriptor.40
- _block_descriptor.50
- _block_descriptor.60
- _block_destroy_helper.19
- _block_destroy_helper.39
- _block_destroy_helper.49
- _block_destroy_helper.59
- _kCABackdropNamespaceOwningContext
- _objc_msgSend$_backdropGroupNamespace
- _objc_msgSend$_pieImageAtFraction:
- _objc_msgSend$_pieImagesMemoryPool
- _objc_msgSend$_updateVisibleIconViewsWithOldVisibleGridCellIndexes:metrics:
- _objc_msgSend$additionalPartialPagesToPrefetchIconLayers
- _objc_msgSend$additionalScrollWidthToPrefetchIconLayersInBothDirections
- _objc_msgSend$appearanceForIcon:userInterfaceStyle:
- _objc_msgSend$backdropGroupNamespace
- _objc_msgSend$effectiveOverrideAccessoryIconImageAppearance
- _objc_msgSend$iconsByExpandingFirstListOfFolderIconsInIcons:
- _objc_msgSend$iconsForGridRange:gridCellInfoOptions:
- _objc_msgSend$imageForIconSize:scale:appearance:tintColor:
- _objc_msgSend$initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:
- _objc_msgSend$initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:
- _objc_msgSend$initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:
- _objc_msgSend$makeIconImageWithInfo:traitCollection:options:
- _objc_msgSend$makeIconLayerWithInfo:traitCollection:options:
- _objc_msgSend$overrideAccessoryIconImageAppearance
- _objc_msgSend$prefetchIconLayersInListView:inRect:imageAppearance:
- _objc_msgSend$removeImageForIconIdentifier:appearance:
- _objc_msgSend$sbh_applyDockGlassWithGrouping:
- _objc_msgSend$sbh_applyGlassWithTintColor:
- _objc_msgSend$sbh_iconImageAppearanceFromTraitCollection:overrideIconImageAppearance:overrideIconImageStyleConfiguration:
- _objc_msgSend$setAdditionalPartialPagesToPrefetchIconLayers:
- _objc_msgSend$setBackdropGroupNamespace:
- _objc_msgSend$setCellVisibility:visibleGridCellIndexes:
- _objc_msgSend$setMaterialView:
- _objc_msgSend$setOverrideAccessoryIconImageAppearance:
- _objc_msgSend$setOverrideImageAppearance:onCustomIconImageViewController:
- _objc_msgSend$setOverrideImageStyleConfiguration:onCustomIconImageViewController:
- _objc_msgSend$setTintingView:
- _objc_msgSend$setVisibleGridCellIndexes:
- _objc_msgSend$smartStackImageForIconSize:scale:
- _objc_msgSend$smartStackImageForIconSize:scale:appearance:tintColor:
- _objc_msgSend$subscribeOnQueue:activityLevelChangeHandler:
- _objc_msgSend$tintingView
- _objc_msgSend$updateAccessoryViewOverrideIconImageAppearance
- _objc_msgSend$withWhitePointBoost
- _updateVisualStyling.darkModeCancel
- _updateVisualStyling.darkModeMagnifyingGlass
- _updateVisualStyling.lightModeCancel
- _updateVisualStyling.lightModeMagnifyingGlass
- _updateVisualStyling.magnifyingGlassImage
CStrings:
+ "-[SBScaleIconZoomAnimator _prepareAnimation]"
+ "?"
+ "@\"<SBHApplicationInfoProviding>\""
+ "@\"<SBIconModelStore>\""
+ "@\"CABackdropLayer\""
+ "@\"CAShapeLayer\""
+ "@\"MTStylingProvidingSolidColorView\""
+ "@\"NSString\"24@0:8@\"<SBLeafIconDataSource>\"16"
+ "@\"SBHIconRepository\""
+ "@52@0:8@16@24@32B40@44"
+ "@60@0:8@16@24@32@40B48@52"
+ "@76@0:8@16@24@32@40@48@56B64@68"
+ "Home screen zoom scaling point anchor is NaN: scalingView: %@, scalingViewLayer origin: %@, scalingViewLayer frame: %@, scalingViewAnchor: %@, referenceIconCenter: %@, scalingViewBounds: %@, zoomScaleDimension: %f:%f, zoomedFrame: %@, iconSize: %@, xScale: %f, yScale: %f, targetIconView: %@, targetIcon: %@"
+ "Initial distance threshold"
+ "Initial velocity threshold"
+ "SBAddSheetWidget-%@"
+ "SBScaleIconZoomAnimator.m"
+ "T@\"<BSInvalidatable>\",&,N,V_performanceFlagDisableLightAngleUpdatesAssertion"
+ "T@\"BSAnimationSettings\",R,N"
+ "T@\"MTStylingProvidingSolidColorView\",&,N,V_backgroundView"
+ "Target icon zoom center is NaN! Calculated center: %@, targetIconPositioningView: %@, targetIconPositioningViewLayer frame: %@, targetIconPositioningViewAnchor: %@"
+ "Target icon zoom scaling point anchor is NaN: targetIconPositioningView: %@, targetIconPositioningViewLayer origin: %@, targetIconPositioningViewLayer frame: %@, targetIconPositioningViewAnchor: %@, targetCenter: %@, modelCenter: %@, cameraPosition: %@, targetIconPositioningViewBounds: %@, zoomScaleDimension: %f:%f, zoomedFrame: %@, iconSize: %@, xScale: %f, yScale: %f, targetIconView: %@, targetIcon: %@"
+ "Td,N,V_lightAngleInitialDistanceThreshold"
+ "Td,N,V_lightAngleInitialVelocityThreshold"
+ "Td,V_accumulatedDistance"
+ "Td,V_initialDistanceThreshold"
+ "Td,V_initialVelocityThreshold"
+ "Td,V_lastLightTimestamp"
+ "Td,V_lastLightTimestamp2"
+ "T{SBH3DPoint=ddd},V_initialLightDirection"
+ "T{SBH3DPoint=ddd},V_lastLightDirection"
+ "T{SBH3DPoint=ddd},V_lastLightDirection2"
+ "_accumulatedDistance"
+ "_addSymbolImageWithTintColor:"
+ "_backdropCaptureLayer"
+ "_initialDistanceThreshold"
+ "_initialLightDirection"
+ "_initialVelocityThreshold"
+ "_lastLightDirection2"
+ "_lastLightTimestamp"
+ "_lastLightTimestamp2"
+ "_lightAngleInitialDistanceThreshold"
+ "_lightAngleInitialVelocityThreshold"
+ "_performanceFlagDisableLightAngleUpdatesAssertion"
+ "_pieImageAtFraction:scale:"
+ "_pieImagesMemoryPoolForScale:"
+ "_prefetchedGridCellIndexes"
+ "_updateBackdropCapture"
+ "_updateSearchControllerLegibility"
+ "_updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:"
+ "accumulatedDistance"
+ "areLightAngleUpdatesAllowed"
+ "backdropGroupNameForActiveDataSource:"
+ "backdropGroupNameIfAvailable"
+ "beginLightAngleUpdatesIfAllowed"
+ "cgColor"
+ "com.apple.siri"
+ "contentVisibilityForIcon:"
+ "gridCellIndexesToIncludeInLayout"
+ "homescreenAppLibraryPod"
+ "initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:"
+ "initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:"
+ "initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:backdropGroupName:"
+ "initialDistanceThreshold"
+ "initialLightDirection"
+ "initialVelocityThreshold"
+ "lastLightDirection2"
+ "lastLightTimestamp"
+ "lastLightTimestamp2"
+ "lightAngleInitialDistanceThreshold"
+ "lightAngleInitialVelocityThreshold"
+ "performanceFlagDisableLightAngleUpdatesAssertion"
+ "performanceFlagDisableSpecularEverywhere"
+ "prefetchedGridCellIndexes"
+ "prefetchedIcons"
+ "primaryWindowScene"
+ "primaryWindowSceneForIconManager:"
+ "pushLightAngleUpdateWithDirection:intensity:angle:"
+ "removeApplicationPlaceholder:pruneEmptyIcons:"
+ "sbh_applyAppLibraryPodGlass"
+ "sbh_applyAppLibraryPodGlassWithGrouping:"
+ "sbh_applySearchPillGlass"
+ "sbh_applySearchPillGlassWithGrouping:"
+ "sbh_applySearchPillGlassWithUserInterfaceStyle:"
+ "sbh_indexSetByAddingIndexes:"
+ "sbh_pauseSpecularHighlightAnimationOnSearchPillGlass"
+ "sbh_resumeSpecularHighlightAnimationOnSearchPillGlass"
+ "setAccumulatedDistance:"
+ "setCellVisibility:visibleGridCellIndexes:prefetchedGridCellIndexes:"
+ "setInitialDistanceThreshold:"
+ "setInitialLightDirection:"
+ "setInitialVelocityThreshold:"
+ "setLastLightDirection2:"
+ "setLastLightTimestamp2:"
+ "setLastLightTimestamp:"
+ "setLightAngleInitialDistanceThreshold:"
+ "setLightAngleInitialVelocityThreshold:"
+ "setPerformanceFlagDisableLightAngleUpdatesAssertion:"
+ "setPrefetchedGridCellIndexes:"
+ "setShadowHidden:"
+ "setVisibleGridCellIndexes:prefetchedGridCellIndexes:"
+ "setWantsHighlightsDisplayAngle:"
+ "setWantsWhitePointBoost:"
+ "shouldDisableDockSpecular"
+ "shouldDisableFolderSpecular"
+ "shouldDisableGlassDock"
+ "shouldDisableParallax"
+ "shouldDisableParallaxOnPageControl"
+ "shouldDisableSpecularEverywhere"
+ "shouldDisableWidgetSpecular"
+ "shouldExcludeAllClearGlassShadows"
+ "shouldExcludeDockShadow"
+ "shouldExcludeSearchShadow"
+ "shouldUseFlatIconsEverywhere"
+ "systemGrayColor"
+ "tintedGlassButtonConfiguration"
+ "v40@0:8q16@24@32"
+ "v40@0:8{SBH3DPoint=ddd}16"
+ "v56@0:8{SBH3DPoint=ddd}16d40d48"
+ "{SBH3DPoint=\"x\"d\"y\"d\"z\"d}"
+ "{SBH3DPoint=ddd}16@0:8"
+ "{SBIconResizeHandleMetrics=dddddq{NSDirectionalEdgeInsets=dddd}}"
+ "\x84"
+ "\xf0\xf0qA"
+ "\xf0\xf0\x91\xf0\xb1\xf01\xc1\xf0Q"
+ "\xf1"
- "@\"SBHIconImageStyleConfiguration\"16@0:8"
- "@64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56"
- "@68@0:8@16@24@32@40@48@56B64"
- "SBIconAdornmentMaterialCloseBoxFauxGlass"
- "T@\"MTMaterialView\",&,N,V_materialView"
- "T@\"NSString\",C,N,V_backdropGroupNamespace"
- "T@\"SBHIconImageAppearance\",C,N,V_overrideAccessoryIconImageAppearance"
- "T@\"SBHIconImageStyleConfiguration\",?,C,N"
- "T@\"UIView\",&,N,V_tintingView"
- "Td,N,V_additionalPartialPagesToPrefetchIconLayers"
- "Td,R,N,V_additionalPartialPagesToPrefetchIconLayers"
- "T{_LSSVec3=ddd},V_lastLightDirection"
- "_additionalPartialPagesToPrefetchIconLayers"
- "_backdropGroupNamespace"
- "_iconLayerPrefetchAssertions"
- "_overrideAccessoryIconImageAppearance"
- "_pieImageAtFraction:"
- "_pieImagesMemoryPool"
- "_tintingView"
- "_updateVisibleIconViewsWithOldVisibleGridCellIndexes:metrics:"
- "additionalPartialPagesToPrefetchIconLayers"
- "additionalScrollWidthToPrefetchIconLayersInBothDirections"
- "backdropGroupNamespace"
- "effectiveOverrideAccessoryIconImageAppearance"
- "folder view scroll prefetch"
- "icon view press"
- "icon view touch"
- "imageForIconSize:scale:appearance:tintColor:"
- "initWithContainingApplicationBundleIdentifier:imageAppearance:customDisplayConfiguration:boostsWhitePoint:"
- "initWithWidgetDataSource:gridSizeClass:widgetViewController:widgetExtensionProvider:imageAppearance:customDisplayConfiguration:boostsWhitePoint:"
- "initWithWidgetExtension:widgetDescriptor:imageAppearance:customDisplayConfiguration:boostsWhitePoint:"
- "makeIconImageWithInfo:traitCollection:options:"
- "makeIconLayerWithInfo:traitCollection:options:"
- "overrideAccessoryIconImageAppearance"
- "prefetchIconLayersInListView:inRect:imageAppearance:"
- "setAdditionalPartialPagesToPrefetchIconLayers:"
- "setBackdropGroupNamespace:"
- "setCellVisibility:visibleGridCellIndexes:"
- "setMaterialView:"
- "setOverrideAccessoryIconImageAppearance:"
- "setOverrideImageAppearance:onCustomIconImageViewController:"
- "setOverrideImageStyleConfiguration:onCustomIconImageViewController:"
- "setTintingView:"
- "smartStackImageForIconSize:scale:"
- "smartStackImageForIconSize:scale:appearance:tintColor:"
- "subscribeOnQueue:activityLevelChangeHandler:"
- "tintingView"
- "updateAccessoryViewOverrideIconImageAppearance"
- "v24@0:8@\"SBHIconImageStyleConfiguration\"16"
- "v40@0:8{_LSSVec3=ddd}16"
- "v40@?0@\"NSString\"8@\"<BSInvalidatable>\"16@\"SBHIconImageAppearance\"24^B32"
- "withWhitePointBoost"
- "{_LSSVec3=\"x\"d\"y\"d\"z\"d}"
- "{_LSSVec3=ddd}16@0:8"
- "\xe1"
- "\xf0\xf0\x81A"
- "\xf0\xf0\x91\xf0\xb1\xf01\xc1\xf0A"

```
