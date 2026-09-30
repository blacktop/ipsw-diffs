## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-163.101.0.0.0
-  __TEXT.__text: 0x324eec
-  __TEXT.__auth_stubs: 0x2cb0
-  __TEXT.__objc_methlist: 0x3b994
-  __TEXT.__const: 0x62a4
-  __TEXT.__cstring: 0x1b1ff
-  __TEXT.__gcc_except_tab: 0x3e48
+169.100.0.0.0
+  __TEXT.__text: 0x327f84
+  __TEXT.__auth_stubs: 0x2cc0
+  __TEXT.__objc_methlist: 0x3bbfc
+  __TEXT.__const: 0x62d4
+  __TEXT.__cstring: 0x1b38f
+  __TEXT.__gcc_except_tab: 0x3e74
   __TEXT.__oslogstring: 0xdd80
   __TEXT.__dlopen_cstrs: 0x4c6
   __TEXT.__ustring: 0x620

   __TEXT.__swift5_capture: 0xfb8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe270
+  __TEXT.__unwind_info: 0xe318
   __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6db6
-  __TEXT.__objc_methname: 0x98fc0
-  __TEXT.__objc_methtype: 0x19264
-  __TEXT.__objc_stubs: 0x58b80
-  __DATA_CONST.__got: 0x2250
-  __DATA_CONST.__const: 0x9668
+  __TEXT.__objc_classname: 0x6db8
+  __TEXT.__objc_methname: 0x99900
+  __TEXT.__objc_methtype: 0x19312
+  __TEXT.__objc_stubs: 0x58fa0
+  __DATA_CONST.__got: 0x2258
+  __DATA_CONST.__const: 0x96c0
   __DATA_CONST.__objc_classlist: 0x1268
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b690
+  __DATA_CONST.__objc_selrefs: 0x1b7d8
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe38
   __DATA_CONST.__objc_arraydata: 0x6d8
-  __AUTH_CONST.__auth_got: 0x1668
+  __AUTH_CONST.__auth_got: 0x1670
   __AUTH_CONST.__const: 0x6230
-  __AUTH_CONST.__cfstring: 0x15aa0
-  __AUTH_CONST.__objc_const: 0x54ab0
+  __AUTH_CONST.__cfstring: 0x15ca0
+  __AUTH_CONST.__objc_const: 0x54e30
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x6118
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3aac
-  __DATA.__data: 0x8878
+  __DATA.__objc_ivar: 0x3ad8
+  __DATA.__data: 0x88a8
   __DATA.__bss: 0x21f8
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x5c58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5E573D56-850E-3898-9108-DCB4B56C5EAE
-  Functions: 22366
-  Symbols:   63770
-  CStrings:  30427
+  UUID: 6F98990F-FCE4-3DC6-9282-EB080D9B8074
+  Functions: 22427
+  Symbols:   63935
+  CStrings:  30527
 
Symbols:
+ +[SBHClockApplicationIconImageView _minuteTimerFired:]
+ +[SBHClockApplicationIconImageView hidesSecondHandDidChange]
+ +[SBHClockApplicationIconImageView lowPowerModeDidChange:]
+ +[SBHIconImageAppearance clearAppearanceForUserInterfaceStyle:]
+ +[SBHIconImageAppearance colorAppearanceForUserInterfaceStyle:]
+ +[SBIconView defaultCursorHitTestPadding]
+ -[SBCustomPlaceholderIcon _setPropertiesFromIcon:]
+ -[SBFolderIcon _setPropertiesFromIcon:]
+ -[SBFolderIconImageView _currentPageListModel]
+ -[SBFolderIconImageView cellIconImageOptions]
+ -[SBFolderIconImageView didAnimateListLayoutProviderChange:context:]
+ -[SBFolderIconImageView willAnimateListLayoutProviderChange:context:]
+ -[SBHClockApplicationIconImageView hidesSecondHand]
+ -[SBHClockApplicationIconImageView updateSecondsHandHidden]
+ -[SBHFloatyFolderVisualConfiguration setTitleBottomInset:]
+ -[SBHFloatyFolderVisualConfiguration setTitleVerticallyCentered:]
+ -[SBHFloatyFolderVisualConfiguration titleBottomInset]
+ -[SBHFloatyFolderVisualConfiguration titleVerticallyCentered]
+ -[SBHIconImageIdentity iconImageInfo]
+ -[SBHIconImageIdentity initWithIcon:iconImageInfo:imageGeneration:imageAppearance:]
+ -[SBHIconImageIdentity initWithIcon:iconImageInfo:imageGeneration:imageAppearance:masked:]
+ -[SBHIconImageIdentity initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:]
+ -[SBHIconImageIdentity initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:masked:]
+ -[SBHIconImageIdentity isEqualToIconImageIdentityExcludingImageGeneration:]
+ -[SBHIconManager beginNewRootFolderContentSession]
+ -[SBHIconManager folderMiniIconImageInfo]
+ -[SBHIconManager iconPrecachingMediumPriorityQueue]
+ -[SBHIconManager limitsWidgetStackPageControlFlashesToSession]
+ -[SBHIconManager multiplexingManager:cachedRecentViewController:forIdentifier:]
+ -[SBHIconManager rootFolderContentSessionIdentifierNumber]
+ -[SBHIconManager rootFolderContentSessionIdentifier]
+ -[SBHIconManager rootListLayout]
+ -[SBHIconManager setIconPrecachingMediumPriorityQueue:]
+ -[SBHIconManager setLimitsWidgetStackPageControlFlashesToSession:]
+ -[SBHIconManager setRootFolderContentSessionIdentifierNumber:]
+ -[SBHIconManager widgetStackViewControllerCanFlashPageControl:]
+ -[SBHIconManager widgetStackViewControllerDidFlashPageControl:]
+ -[SBHMultiplexingViewController appendDescriptionToFormatter:]
+ -[SBHMultiplexingViewController description]
+ -[SBHWidgetStyleManager displayedIconImageAppearance]
+ -[SBIcon iconImageIdentityWithIconImageInfo:imageAppearance:masked:]
+ -[SBIcon iconImageIdentityWithIconImageInfo:traitCollection:masked:]
+ -[SBIcon prefetchIconLayerWithInfo:imageAppearance:imageOptions:priority:reason:prefetchBehavior:]
+ -[SBIcon prefetchIconLayerWithInfo:traitCollection:imageOptions:priority:reason:prefetchBehavior:]
+ -[SBIconImageView didAnimateListLayoutProviderChange:context:]
+ -[SBIconImageView imageLoadPriority]
+ -[SBIconImageView isAnimatingIconImageInfoChange]
+ -[SBIconImageView isAnimatingListLayoutProviderChange]
+ -[SBIconImageView listLayoutProvider]
+ -[SBIconImageView setAnimatingIconImageInfoChange:]
+ -[SBIconImageView setAnimatingListLayoutProviderChange:]
+ -[SBIconImageView setListLayoutProvider:]
+ -[SBIconImageView shouldForceBitmapImages]
+ -[SBIconImageView willAnimateListLayoutProviderChange:context:]
+ -[SBIconLabelImageMetrics hash]
+ -[SBIconListModel _notifyListObserversDidAddIcons:didRemoveIcons:movedIcons:options:]
+ -[SBIconListModel _targetListForGridCellInfo:]
+ -[SBIconListModel fixedLocationForIcon:gridCellInfoOptions:]
+ -[SBIconListModel hasFixedIconLocationsWithGridCellInfo:]
+ -[SBIconListModel hasFixedIconLocationsWithGridCellInfoOptions:]
+ -[SBIconListModel isEligibleForSimpleMutationsWithGridCellInfoOptions:mutationOptions:]
+ -[SBIconView iconImageView]
+ -[SBPlaceholderIcon _setPropertiesFromIcon:]
+ -[SBPlaceholderIcon canBeReceivedByIcon]
+ -[SBPlaceholderIcon isClusteredIconPlaceholder]
+ -[SBPlaceholderIcon isGrabbedIconPlaceholder]
+ GCC_except_table1027
+ GCC_except_table1050
+ GCC_except_table121
+ GCC_except_table141
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table171
+ GCC_except_table188
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table212
+ GCC_except_table222
+ GCC_except_table256
+ GCC_except_table280
+ GCC_except_table282
+ GCC_except_table288
+ GCC_except_table299
+ GCC_except_table345
+ GCC_except_table354
+ GCC_except_table394
+ GCC_except_table396
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table438
+ GCC_except_table451
+ GCC_except_table467
+ GCC_except_table469
+ GCC_except_table489
+ GCC_except_table507
+ GCC_except_table514
+ GCC_except_table536
+ GCC_except_table539
+ GCC_except_table558
+ GCC_except_table565
+ GCC_except_table594
+ GCC_except_table628
+ GCC_except_table660
+ GCC_except_table681
+ GCC_except_table691
+ GCC_except_table694
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table709
+ GCC_except_table711
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table718
+ GCC_except_table725
+ GCC_except_table728
+ GCC_except_table731
+ GCC_except_table734
+ GCC_except_table741
+ GCC_except_table743
+ GCC_except_table828
+ GCC_except_table884
+ GCC_except_table954
+ GCC_except_table974
+ GCC_except_table991
+ _OBJC_IVAR_$_SBHFloatyFolderVisualConfiguration._titleBottomInset
+ _OBJC_IVAR_$_SBHFloatyFolderVisualConfiguration._titleVerticallyCentered
+ _OBJC_IVAR_$_SBHIconImageIdentity._iconImageInfo
+ _OBJC_IVAR_$_SBHIconManager._iconPrecachingMediumPriorityQueue
+ _OBJC_IVAR_$_SBHIconManager._limitsWidgetStackPageControlFlashesToSession
+ _OBJC_IVAR_$_SBHIconManager._rootFolderContentSessionIdentifierNumber
+ _OBJC_IVAR_$_SBHIconManager._widgetIconIdentifiersForPageControlFlashes
+ _OBJC_IVAR_$_SBHLibraryPodIconZoomAnimator._disableGlassGroupingAssertionsForIconViews
+ _OBJC_IVAR_$_SBIconImageView._animatingIconImageInfoChange
+ _OBJC_IVAR_$_SBIconImageView._animatingListLayoutProviderChange
+ _OBJC_IVAR_$_SBIconImageView._listLayoutProvider
+ _OUTLINED_FUNCTION_16
+ _SBIconImageInfoHash
+ _SBIconModelMemoryStoreErrorDomain
+ _UIRectRoundToScale
+ __OBJC_$_CLASS_PROP_LIST_SBHIconImageIdentity
+ __OBJC_CLASS_PROTOCOLS_$_SBHMultiplexingViewController
+ __SBClockIconResetMinuteTimer
+ __SBClockIconResetTimer
+ ___106-[SBHWidgetStackViewController _removeWidgetWithUniqueIdentifier:widgetContainerViewControllers:animated:]_block_invoke.101
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1087
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1089
+ ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.969
+ ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.965
+ ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.155
+ ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.155.cold.1
+ ___58+[SBHClockApplicationIconImageView lowPowerModeDidChange:]_block_invoke
+ ___62-[SBHMultiplexingViewController appendDescriptionToFormatter:]_block_invoke
+ ___62-[SBRootFolderView setSpecialLayoutManager:completionHandler:]_block_invoke_6
+ ___62-[SBRootFolderView setSpecialLayoutManager:completionHandler:]_block_invoke_7
+ ___67-[SBHIconManager _precacheImagesForRootIconsForStyleConfiguration:]_block_invoke_7
+ ___69-[SBFolderIconImageView willAnimateListLayoutProviderChange:context:]_block_invoke
+ ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke.125
+ ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke_2.126
+ ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.236
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.527
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.599
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.602
+ ___96-[SBHWidgetStackViewController _updateBackgroundViewWithAnimationUpdateMode:allowingOutsetting:]_block_invoke.131
+ ___block_descriptor_104_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_120_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e32_v32?0"SBIconListModel"8Q16^B24ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_88_e8_32s40s_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8
+ ___block_literal_global.1009
+ ___block_literal_global.1048
+ ___block_literal_global.1166
+ ___block_literal_global.1219
+ ___block_literal_global.1231
+ ___block_literal_global.203
+ ___block_literal_global.222
+ ___block_literal_global.226
+ ___block_literal_global.2725
+ ___block_literal_global.278
+ ___block_literal_global.339
+ ___block_literal_global.364
+ ___block_literal_global.371
+ ___block_literal_global.400
+ ___block_literal_global.408
+ ___block_literal_global.52
+ ___block_literal_global.601
+ ___block_literal_global.785
+ ___block_literal_global.811
+ ___block_literal_global.856
+ ___block_literal_global.878
+ ___minuteTimer
+ _objc_msgSend$_currentPageListModel
+ _objc_msgSend$_layoutScale
+ _objc_msgSend$_notifyListObserversDidAddIcons:didRemoveIcons:movedIcons:options:
+ _objc_msgSend$_targetListForGridCellInfo:
+ _objc_msgSend$cellIconImageOptions
+ _objc_msgSend$clearGlassButtonConfiguration
+ _objc_msgSend$colorAppearanceForUserInterfaceStyle:
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$defaultCursorHitTestPadding
+ _objc_msgSend$didAnimateListLayoutProviderChange:context:
+ _objc_msgSend$displayedIconImageAppearance
+ _objc_msgSend$filterStyle
+ _objc_msgSend$folderMiniIconImageInfo
+ _objc_msgSend$hasFixedIconLocationsWithGridCellInfo:
+ _objc_msgSend$hasFixedIconLocationsWithGridCellInfoOptions:
+ _objc_msgSend$hidesSecondHand
+ _objc_msgSend$hidesSecondHandDidChange
+ _objc_msgSend$iconImageIdentityWithIconImageInfo:imageAppearance:masked:
+ _objc_msgSend$iconImageIdentityWithIconImageInfo:traitCollection:masked:
+ _objc_msgSend$iconPrecachingMediumPriorityQueue
+ _objc_msgSend$imageLoadPriority
+ _objc_msgSend$initWithIcon:iconImageInfo:imageGeneration:imageAppearance:
+ _objc_msgSend$initWithIcon:iconImageInfo:imageGeneration:imageAppearance:masked:
+ _objc_msgSend$initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:
+ _objc_msgSend$initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:masked:
+ _objc_msgSend$isAnimatingListLayoutProviderChange
+ _objc_msgSend$isEligibleForSimpleMutationsWithGridCellInfoOptions:mutationOptions:
+ _objc_msgSend$isEqualToIconImageIdentityExcludingImageGeneration:
+ _objc_msgSend$limitsWidgetStackPageControlFlashesToSession
+ _objc_msgSend$multiplexingManager:cachedRecentViewController:forIdentifier:
+ _objc_msgSend$prefetchIconLayerWithInfo:imageAppearance:imageOptions:priority:reason:prefetchBehavior:
+ _objc_msgSend$prefetchIconLayerWithInfo:traitCollection:imageOptions:priority:reason:prefetchBehavior:
+ _objc_msgSend$primaryTintColor
+ _objc_msgSend$prominentGlassButtonConfiguration
+ _objc_msgSend$setAnimatingListLayoutProviderChange:
+ _objc_msgSend$setIconPrecachingMediumPriorityQueue:
+ _objc_msgSend$setLabelFont:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setNanosecond:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$setTitleBottomInset:
+ _objc_msgSend$setTitleVerticallyCentered:
+ _objc_msgSend$shouldForceBitmapImages
+ _objc_msgSend$titleBottomInset
+ _objc_msgSend$titleVerticallyCentered
+ _objc_msgSend$updateSecondsHandHidden
+ _objc_msgSend$widgetStackViewControllerCanFlashPageControl:
+ _objc_msgSend$widgetStackViewControllerDidFlashPageControl:
+ _objc_msgSend$willAnimateListLayoutProviderChange:context:
- +[SBHClockApplicationIconImageView cacheIconServicesDataWithIconImageInfo:appearance:options:]
- +[SBIconImageView generatesContentsImage]
- -[SBFolderIconImageView didAnimateIconImageInfoChange]
- -[SBFolderIconImageView willAnimateIconImageInfoChange]
- -[SBHAddWidgetSheetViewController iconListView:willConfigureIconView:forIcon:]
- -[SBHIconImageIdentity initWithIcon:imageGeneration:imageAppearance:]
- -[SBHIconImageIdentity initWithIcon:imageGeneration:imageAppearance:masked:]
- -[SBHIconImageIdentity initWithIconIdentifier:imageGeneration:imageAppearance:]
- -[SBHIconImageIdentity initWithIconIdentifier:imageGeneration:imageAppearance:masked:]
- -[SBIcon prefetchIconLayerWithInfo:imageAppearance:imageOptions:reason:prefetchBehavior:]
- -[SBIcon prefetchIconLayerWithInfo:traitCollection:imageOptions:reason:prefetchBehavior:]
- -[SBIcon(SBPlaceholderIcon) isClusteredIconPlaceholder]
- -[SBIcon(SBPlaceholderIcon) isGrabbedIconPlaceholder]
- -[SBIconImageView effectivelyPrefersFlatImageLayers]
- -[SBIconImageView updateCachedImages]
- -[SBIconImageView updateImageContentsFromGeneratedImageAnimated:]
- -[SBPlaceholderIcon isPlaceholder]
- GCC_except_table1019
- GCC_except_table1042
- GCC_except_table120
- GCC_except_table140
- GCC_except_table153
- GCC_except_table170
- GCC_except_table186
- GCC_except_table201
- GCC_except_table203
- GCC_except_table206
- GCC_except_table211
- GCC_except_table251
- GCC_except_table252
- GCC_except_table259
- GCC_except_table279
- GCC_except_table343
- GCC_except_table352
- GCC_except_table389
- GCC_except_table391
- GCC_except_table395
- GCC_except_table398
- GCC_except_table401
- GCC_except_table428
- GCC_except_table441
- GCC_except_table462
- GCC_except_table464
- GCC_except_table484
- GCC_except_table502
- GCC_except_table504
- GCC_except_table531
- GCC_except_table534
- GCC_except_table553
- GCC_except_table557
- GCC_except_table586
- GCC_except_table627
- GCC_except_table659
- GCC_except_table673
- GCC_except_table683
- GCC_except_table686
- GCC_except_table695
- GCC_except_table697
- GCC_except_table699
- GCC_except_table701
- GCC_except_table706
- GCC_except_table708
- GCC_except_table710
- GCC_except_table712
- GCC_except_table717
- GCC_except_table723
- GCC_except_table726
- GCC_except_table735
- GCC_except_table737
- GCC_except_table820
- GCC_except_table876
- GCC_except_table946
- GCC_except_table966
- GCC_except_table983
- _NSStringFromRange
- _UIRectRoundToViewScale
- ___106-[SBHWidgetStackViewController _removeWidgetWithUniqueIdentifier:widgetContainerViewControllers:animated:]_block_invoke.97
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1085
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1087
- ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.968
- ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.962
- ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.151
- ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.151.cold.1
- ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke.121
- ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke_2.122
- ___77-[SBHIconManager _ensureWidgetIsVisibleForDebuggingWithDescriptor:sizeClass:]_block_invoke.234
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.525
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.597
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.600
- ___96-[SBHWidgetStackViewController _updateBackgroundViewWithAnimationUpdateMode:allowingOutsetting:]_block_invoke.127
- ___block_descriptor_48_e8_32s40s_e32_v32?0"SBIconListModel"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e32_v32?0"SBIconListModel"8Q16^B24ls32l8s40l8r48l8
- ___block_descriptor_88_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1007
- ___block_literal_global.1046
- ___block_literal_global.1164
- ___block_literal_global.1217
- ___block_literal_global.1224
- ___block_literal_global.198
- ___block_literal_global.200
- ___block_literal_global.221
- ___block_literal_global.224
- ___block_literal_global.26
- ___block_literal_global.2718
- ___block_literal_global.276
- ___block_literal_global.281
- ___block_literal_global.337
- ___block_literal_global.362
- ___block_literal_global.365
- ___block_literal_global.399
- ___block_literal_global.406
- ___block_literal_global.41
- ___block_literal_global.599
- ___block_literal_global.782
- ___block_literal_global.808
- ___block_literal_global.855
- ___block_literal_global.875
- _objc_msgSend$_clearGlassButtonConfiguration
- _objc_msgSend$cacheIconServicesDataWithIconImageInfo:appearance:options:
- _objc_msgSend$effectivelyPrefersFlatImageLayers
- _objc_msgSend$generatesContentsImage
- _objc_msgSend$iconImageIdentityWithTraitCollection:masked:
- _objc_msgSend$initWithIcon:imageGeneration:imageAppearance:
- _objc_msgSend$initWithIcon:imageGeneration:imageAppearance:masked:
- _objc_msgSend$initWithIconIdentifier:imageGeneration:imageAppearance:
- _objc_msgSend$initWithIconIdentifier:imageGeneration:imageAppearance:masked:
- _objc_msgSend$isColor
- _objc_msgSend$plk_sha256HashForObject:error:
- _objc_msgSend$prefetchIconLayerWithInfo:imageAppearance:imageOptions:reason:prefetchBehavior:
- _objc_msgSend$prefetchIconLayerWithInfo:traitCollection:imageOptions:reason:prefetchBehavior:
- _objc_msgSend$squareContentsImage
- _objc_msgSend$tintedGlassButtonConfiguration
- _objc_msgSend$updateImageContentsFromGeneratedImageAnimated:
CStrings:
+ "@60@0:8{SBIconImageInfo={CGSize=dd}dd}16@48B56"
+ "@72@0:8@16{SBIconImageInfo={CGSize=dd}dd}24Q56@64"
+ "@76@0:8@16{SBIconImageInfo={CGSize=dd}dd}24Q56@64B72"
+ "@88@0:8{SBIconImageInfo={CGSize=dd}dd}16@48Q56q64@72q80"
+ "@@%@_%lu_%lu_%@@@"
+ "B24@0:8@\"SBHWidgetStackViewController\"16"
+ "LibraryPodZoom"
+ "PageManagementExit"
+ "SBDisableClockIconSecondsHand"
+ "SBFolderIconImageViewPrefetchAssertions"
+ "SBIconModelMemoryStoreErrorDomain"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_iconPrecachingMediumPriorityQueue"
+ "T@\"SBIconImageView\",R,N,V_iconImageView"
+ "T@\"UIFont\",R,N"
+ "TB,N,GisAnimatingListLayoutProviderChange,V_animatingListLayoutProviderChange"
+ "TB,N,V_limitsWidgetStackPageControlFlashesToSession"
+ "TB,N,V_titleVerticallyCentered"
+ "TB,R,N,GisClusteredIconPlaceholder"
+ "TB,R,N,GisGrabbedIconPlaceholder"
+ "TB,R,N,GisImageLoadingBehaviorAsynchronous"
+ "TB,R,N,GisImageLoadingBehaviorSynchronous"
+ "TQ,N,V_rootFolderContentSessionIdentifierNumber"
+ "Td,N,V_titleBottomInset"
+ "_animatingListLayoutProviderChange"
+ "_currentPageListModel"
+ "_iconPrecachingMediumPriorityQueue"
+ "_limitsWidgetStackPageControlFlashesToSession"
+ "_minuteTimerFired:"
+ "_notifyListObserversDidAddIcons:didRemoveIcons:movedIcons:options:"
+ "_rootFolderContentSessionIdentifierNumber"
+ "_targetListForGridCellInfo:"
+ "_titleBottomInset"
+ "_titleVerticallyCentered"
+ "_widgetIconIdentifiersForPageControlFlashes"
+ "animatingListLayoutProviderChange"
+ "beginNewRootFolderContentSession"
+ "cellIconImageOptions"
+ "clearAppearanceForUserInterfaceStyle:"
+ "clearGlassButtonConfiguration"
+ "clusteredIconPlaceholder"
+ "colorAppearanceForUserInterfaceStyle:"
+ "com.apple.SpringBoardHome.icon-precaching-medium"
+ "dateFromComponents:"
+ "defaultCursorHitTestPadding"
+ "didAnimateListLayoutProviderChange:context:"
+ "displayedIconImageAppearance"
+ "filterStyle"
+ "fixedLocationForIcon:gridCellInfoOptions:"
+ "folder icon animation"
+ "folderMiniIconImageInfo"
+ "grabbedIconPlaceholder"
+ "hasFixedIconLocationsWithGridCellInfo:"
+ "hasFixedIconLocationsWithGridCellInfoOptions:"
+ "hidesSecondHand"
+ "hidesSecondHandDidChange"
+ "iconImageIdentityWithIconImageInfo:imageAppearance:masked:"
+ "iconImageIdentityWithIconImageInfo:traitCollection:masked:"
+ "iconImageInfoContinuousCornerRadius"
+ "iconImageInfoHeight"
+ "iconImageInfoScale"
+ "iconImageInfoWidth"
+ "iconPrecachingMediumPriorityQueue"
+ "imageLoadPriority"
+ "imageLoadingBehaviorAsynchronous"
+ "imageLoadingBehaviorSynchronous"
+ "initWithIcon:iconImageInfo:imageGeneration:imageAppearance:"
+ "initWithIcon:iconImageInfo:imageGeneration:imageAppearance:masked:"
+ "initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:"
+ "initWithIconIdentifier:iconImageInfo:imageGeneration:imageAppearance:masked:"
+ "isAnimatingListLayoutProviderChange"
+ "isEligibleForSimpleMutationsWithGridCellInfoOptions:mutationOptions:"
+ "isEqualToIconImageIdentityExcludingImageGeneration:"
+ "limitsWidgetStackPageControlFlashesToSession"
+ "multiplexingManager:cachedRecentViewController:forIdentifier:"
+ "prefetchIconLayerWithInfo:imageAppearance:imageOptions:priority:reason:prefetchBehavior:"
+ "prefetchIconLayerWithInfo:traitCollection:imageOptions:priority:reason:prefetchBehavior:"
+ "primaryTintColor"
+ "prominentGlassButtonConfiguration"
+ "rootFolderContentSessionIdentifier"
+ "rootFolderContentSessionIdentifierNumber"
+ "setAnimatingListLayoutProviderChange:"
+ "setIconPrecachingMediumPriorityQueue:"
+ "setLimitsWidgetStackPageControlFlashesToSession:"
+ "setMinute:"
+ "setNanosecond:"
+ "setRootFolderContentSessionIdentifierNumber:"
+ "setSecond:"
+ "setTitleBottomInset:"
+ "setTitleVerticallyCentered:"
+ "shouldForceBitmapImages"
+ "titleBottomInset"
+ "titleVerticallyCentered"
+ "updateSecondsHandHidden"
+ "very high"
+ "very low"
+ "widgetStackViewControllerCanFlashPageControl:"
+ "widgetStackViewControllerDidFlashPageControl:"
+ "willAnimateListLayoutProviderChange:context:"
+ "\xf0\xf0\x91\xf0\xc1\xf01\xc1\xf0q"
- "@44@0:8@16Q24@32B40"
- "@80@0:8{SBIconImageInfo={CGSize=dd}dd}16@48Q56@64q72"
- "@@%@@@"
- "_clearGlassButtonConfiguration"
- "cacheIconServicesDataWithIconImageInfo:appearance:options:"
- "effectivelyPrefersFlatImageLayers"
- "generatesContentsImage"
- "initWithIcon:imageGeneration:imageAppearance:"
- "initWithIcon:imageGeneration:imageAppearance:masked:"
- "initWithIconIdentifier:imageGeneration:imageAppearance:"
- "initWithIconIdentifier:imageGeneration:imageAppearance:masked:"
- "plk_sha256HashForObject:error:"
- "prefetchIconLayerWithInfo:imageAppearance:imageOptions:reason:prefetchBehavior:"
- "prefetchIconLayerWithInfo:traitCollection:imageOptions:reason:prefetchBehavior:"
- "tintedGlassButtonConfiguration"
- "updateCachedImages"
- "updateImageContentsFromGeneratedImageAnimated:"
- "visibleRows"
- "\xf0\xf0\x91\xf0\xb1\xf01\xc1\xf0Q"

```
